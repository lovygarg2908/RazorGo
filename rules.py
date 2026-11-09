"""Rules: diagnosis keywords, guardrail checker and safety lists. No AI, no randomness."""
import re, unicodedata, pandas as pd


# ---------- 1. classification (rules first, safety signals override everything) ----------
KW = [('R12', ['compliance', 'screening', 'sanction']),
      ('R10', ['restricted', 'not supported', 'support nahi kar', 'prohibited']),
      ('R11', ['differs from website']), ('R09', ['signatory']), ('R08', ['address']),
      ('R07', ['khul nahi', 'requires login', 'not live']), ('R06', ['policy']),
      ('R05', ['not readable', 'blur', 'clear nahi', 'unreadable', 'cropped', 'illegible']),
      ('R04', ['ifsc', 'bank verify', 'bank verification', 'account verify', 'account verification', 'account number']),
      ('R03', ['bank account', 'account name', 'account ka naam', 'account holder']),
      ('R02', ['gst']), ('R01', ['pan'])]
def kw(msg):
    m = str(msg).lower()
    for c, ws in KW:
        if any(w in m for w in ws): return c
    return None

def classify(code, msg):
    """returns (final_code, source, note). final_code may be 'UNCLASSIFIED' (goes to a human, never nudged)."""
    code = code if isinstance(code, str) else None
    msg = msg if isinstance(msg, str) else None
    inferred = kw(msg) if msg else None
    # SAFETY OVERRIDE: any compliance or restricted signal in the text wins, even if the code says "fixable"
    if inferred in ('R10', 'R12'):
        if code in (None, inferred):
            return inferred, ('Catalog code' if code else 'Inferred from reviewer text'), ''
        return inferred, 'Safety override (text signal beats code)', 'Code %s but text signals %s' % (code, inferred)
    if code:
        note = '' if (not inferred or inferred == code) else 'CHECK: text suggests %s but code is %s' % (inferred, code)
        return code, 'Catalog code', note
    if inferred: return inferred, 'Inferred from reviewer text', ''
    if msg: return 'UNCLASSIFIED', 'Reviewer text not recognised', 'Unmatched text'
    return 'R13', 'No rejection: abandoned at step', ''

# ---------- 2. guardrails ----------
FORBID_EN = ['guarantee', 'approved', 'approval', 'will be live', 'within', 'today', 'tomorrow', 'refund of', 'waive',
             'waiver', 'sanction', 'screening', 'compliance', 'risk', 'restricted', 'blacklist', 'workaround',
             'alternative', 'loophole', 'bypass']
FORBID_HI_TOKENS = ['aaj', 'kal', 'guarantee', 'gaurantee']
FORBID_NATIVE = ['गारंटी', 'मंज़ूर', 'मंजूर', 'स्वीकृत', 'जोखिम', 'प्रतिबंध', 'स्क्रीनिंग', 'अनुपालन', 'पाबंदी',
                 'உத்தரவாதம்', 'ஒப்புதல்', 'இன்றே', 'நாளை', 'ಖಾತರಿ', 'ಅನುಮೋದನೆ', 'ಇಂದೇ', 'ನಾಳೆ',
                 'இணக்க', 'திரையிடல்', 'ஸ்கிரீனிங்', 'கட்டுப்பாடு', 'ஆபத்து', 'அபாய', 'ಅನುಸರಣೆ', 'ಸ್ಕ್ರೀನಿಂಗ್', 'ನಿರ್ಬಂಧ', 'ಅಪಾಯ']
FORBID_NATIVE_TOKENS = ['आज', 'कल', 'उद्या', 'आजच']
CLOSURE_FORBID = ['workaround', 'alternative', 'reapply', 'resubmit', 'appeal', 'sanction', 'screening', 'compliance',
                  'risk', 'change your', 'instead', 'again', 'dobara', 'phir se', 'दोबारा', 'पुन्हा', 'மீண்டும்', 'ಮತ್ತೆ']
HOLD_FORBID = CLOSURE_FORBID + ['restricted', 'not supported', 'closed', 'band', 'reject', 'बंद']
R13_NO_REASON = ['reject', 'mismatch', 'invalid', 'wrong', 'galat', 'alag', 'blur', 'fail']
BLOCKS = {'Hindi': (0x0900, 0x097F), 'Marathi': (0x0900, 0x097F), 'Tamil': (0x0B80, 0x0BFF), 'Kannada': (0x0C80, 0x0CFF)}

WA_LIMIT = 1000   # WhatsApp message length limit we set ourselves (template bodies allow about 1,024)

def has_emoji(msg):
    return any(0x1F000 <= ord(c) <= 0x1FAFF or 0x2600 <= ord(c) <= 0x27BF for c in msg)

def tokens(msg): return [t.strip('.,!?:;()[]।"\'').lower() for t in msg.split()]
def digits_present(msg):
    m = msg.replace('5 MB', '').replace('[resume link]', '')
    return any(unicodedata.category(c) == 'Nd' for c in m)
def script_ok(msg, lang):
    letters = [c for c in msg if c.isalpha()]
    if not letters: return False
    if lang in BLOCKS:
        lo, hi = BLOCKS[lang]
        return sum(lo <= ord(c) <= hi for c in letters) / len(letters) >= 0.5
    return sum(ord(c) < 0x250 for c in letters) / len(letters) >= 0.99

def check(msg, kind, lang, code, channel=None, opted_in=None):
    """kind: 'nudge' | 'closure' | 'hold'. Returns list of failures (empty = pass)."""
    f = []
    low = msg.lower(); tk = tokens(msg)
    if kind == 'nudge':
        if code in ('R10', 'R12', 'UNCLASSIFIED'): f.append('never nudge this code')
        if '[resume link]' not in msg: f.append('missing resume link')
        if any(w in low for w in FORBID_EN): f.append('forbidden word (EN)')
        if any(t in FORBID_HI_TOKENS for t in tk): f.append('forbidden token (Hinglish)')
        if any(w in msg for w in FORBID_NATIVE): f.append('forbidden word (native script)')
        if any(t in FORBID_NATIVE_TOKENS for t in tk): f.append('forbidden token (native script)')
        if code == 'R13' and any(w in low for w in R13_NO_REASON): f.append('R13 must not guess a reason')
        if channel == 'WhatsApp' and len(msg) > WA_LIMIT: f.append('WhatsApp message too long')
        if channel == 'WhatsApp' and 'STOP' not in msg: f.append('WhatsApp nudge missing STOP line')
        if channel == 'WhatsApp' and 'HELP' not in msg: f.append('WhatsApp nudge missing HELP line')
    else:
        bad = CLOSURE_FORBID if kind == 'closure' else HOLD_FORBID
        if any(w in low for w in bad if w.isascii()) or any(w in msg for w in bad if not w.isascii()):
            f.append('closure/hold wording not allowed')
        if '[resume link]' in msg: f.append('no resume link in closure/hold')
        if any(w in msg for w in FORBID_NATIVE): f.append('forbidden word (native script)')
    if has_emoji(msg): f.append('emoji present')
    if digits_present(msg): f.append('number or date present')
    if '{' in msg or '}' in msg: f.append('unfilled placeholder')
    if not script_ok(msg, lang): f.append('wrong script for language')
    if channel == 'WhatsApp' and opted_in is not True: f.append('WhatsApp without opt-in')
    return f

# ---------- 3. decision ----------
def decide(r, code, source):
    """returns dict: route, lane_base, escalation_team, risk"""
    if code == 'R10':
        return dict(route='Close politely (human approves, no workaround)', team='Onboarding Ops (closure approval)', risk='High', kind='closure')
    if code == 'R12':
        return dict(route='Compliance team (applicant told "under review", no reason)', team='Compliance', risk='High', kind='hold')
    if code == 'UNCLASSIFIED':
        return dict(route='Human review (could not classify, no message sent)', team='Onboarding Ops (triage)', risk='High', kind=None)
    stuck = (r.attempts >= 3) or (r.support_contacts >= 2)
    if stuck or r.expected_monthly_tpv_inr_lakh >= 30:
        return dict(route='Human call first, automated nudge as backup', team='Onboarding Ops (assisted)', risk='Medium', kind='nudge')
    return dict(route='Automated nudge sequence', team='', risk='Low', kind='nudge')

def tone_for(days):
    return 'soft' if days <= 7 else 'reminder' if days <= 30 else 'last'
