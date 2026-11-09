"""Razorpay merchant onboarding recovery agent.

What it does, in order, for every application:
  input checks -> status gate -> diagnose (catalog code, keyword rules, saved AI second opinion, safety override)
  -> route -> lane -> priority score -> weekly call budget -> build messages from the approved library
  -> guardrail check -> send status and colour light.

Deterministic: no randomness and no network calls. The same input always gives the same output.
Run from a terminal:  python agent.py      (prints the colour-coded run report)
"""
import os, json, hashlib
import pandas as pd, numpy as np
import rules as R          # keyword diagnosis + guardrail checker
import messages as M       # approved six-language message library

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(HERE, 'onboarding_data.xlsx')
AI_FILE = os.path.join(HERE, 'ai_second_opinion.json')

SNAPSHOT = pd.Timestamp('2026-09-30')
LANE_A_TPV = 30.0                    # Rs lakh per month
AI_CONFIDENCE_FLOOR = 80
CALLED = ['Value slot', 'Stuck small-merchant slot']
EXPECTED_STEP = {'R01': 'KYC docs', 'R02': 'KYC docs', 'R05': 'KYC docs', 'R08': 'KYC docs', 'R09': 'KYC docs',
                 'R03': 'Bank verification', 'R04': 'Bank verification',
                 'R06': 'Website/App review', 'R07': 'Website/App review', 'R11': 'Website/App review'}


NAME_COLS = ('business_name', 'merchant_name', 'contact_name')   # not in the current data; used automatically if a name column is added


def load_data(path=DATA_FILE):
    x = pd.ExcelFile(path)
    return x.parse('Applications'), x.parse('RejectionCatalog').set_index('code')


def load_ai(path=AI_FILE):
    try:
        return json.load(open(path, encoding='utf-8'))['answers']
    except FileNotFoundError:
        return {}


def input_checks(A):
    dup = A.application_id[A.application_id.duplicated()].tolist()
    if dup:
        raise ValueError('Input check failed: duplicate application_id ' + ', '.join(dup))


# ---------- scoring helpers ----------
def tone(days):
    return 'soft' if days <= 7 else 'reminder' if days <= 30 else 'gentle'


def fresh(d):
    return 1.0 if d <= 7 else 0.85 if d <= 14 else 0.6 if d <= 30 else 0.35


def ease(n):
    return {0: 1.0, 1: 1.0, 2: 0.9, 3: 0.8}[int(min(n, 3))]


def evid(src):
    return 1.0 if src.startswith('Catalog') else 0.9 if src.startswith('Inferred') else 0.7


# ---------- diagnosis ----------
def diagnose(r, ai):
    """Returns code, source, ai_note. Keyword rules first, then the saved AI second opinion for blank codes."""
    code, src, note = R.classify(r.rejection_code, r.rejection_message)
    ai_note = ''
    if src.startswith('Inferred'):
        a = ai.get(r.application_id)
        if a is None or a.get('text') != r.rejection_message:
            ai_note = 'No saved AI answer for this text: a person confirms the code'
        else:
            ai_note = 'AI says %s at %d%%' % (a['code'], a['confidence'])
            if a['code'] in ('R10', 'R12') and a['code'] != code:
                code, src = a['code'], 'AI flagged a safety signal'
                ai_note += ': safety wins, a person decides'
            elif a['code'] != code or a['confidence'] < AI_CONFIDENCE_FLOOR:
                code, src = 'UNCLASSIFIED', 'Rules and AI disagree, or AI unsure'
                ai_note += ' (rules said %s): a person decides' % R.classify(r.rejection_code, r.rejection_message)[0]
            else:
                ai_note += ', agrees with the rules'
    return code, src, ai_note


# ---------- messages ----------
def build_messages(r):
    lang, ch = r.language, ('WhatsApp' if r.opted else 'Email')
    out = dict(channel=ch, email_subject='', subject3='', subject7='', msg='', day3='', day7='', eng='', fails=[])
    opted = r.opted if ch == 'WhatsApp' else None
    if r.kind == 'nudge':
        t = tone(r.days)
        step = r.step if r.code == 'R13' else None
        out['msg'] = M.day0(r.code, lang, tone=t, channel=ch, stuck=bool(r.stuck), step=step, name=r.merchant_name)
        out['eng'] = M.day0(r.code, 'English', tone=t, channel=ch, stuck=bool(r.stuck), step=step, name=r.merchant_name)
        out['fails'] = R.check(out['msg'], 'nudge', lang, r.code, ch, opted)
        if ch == 'Email':
            out['email_subject'] = M.SUBJ['day0'][lang]
        if r.days <= 30:                      # idle 31 days or more: Day 0 only
            out['day3'] = M.wrap(M.day3(r.code, lang, step, r.merchant_name), lang, ch)
            out['day7'] = M.wrap(M.day7(r.code, lang, step, r.merchant_name), lang, ch)
            if ch == 'Email':
                out['subject3'], out['subject7'] = M.SUBJ['day3'][lang], M.SUBJ['day7'][lang]
            out['fails'] += R.check(out['day3'], 'nudge', lang, r.code, ch, opted)
            out['fails'] += R.check(out['day7'], 'nudge', lang, r.code, ch, opted)
    elif r.kind == 'closure':
        out['msg'], out['eng'] = M.personalise(M.CLOSE[lang], lang, r.merchant_name), M.personalise(M.CLOSE['English'], 'English', r.merchant_name)
        out['email_subject'] = M.SUBJ['plain'][lang] if ch == 'Email' else ''
        out['fails'] = R.check(out['msg'], 'closure', lang, 'R10')
    elif r.kind == 'hold':
        out['msg'], out['day7'], out['eng'] = M.personalise(M.HOLD0[lang], lang, r.merchant_name), M.personalise(M.HOLD7[lang], lang, r.merchant_name), M.personalise(M.HOLD0['English'], 'English', r.merchant_name)
        out['email_subject'] = M.SUBJ['plain'][lang] if ch == 'Email' else ''
        out['fails'] = R.check(out['msg'], 'hold', lang, 'R12') + R.check(out['day7'], 'hold', lang, 'R12')
    return out


def send_status(r):
    why, s = [], 'Ready to send'
    if r.kind == 'closure':
        s = 'Human only: approve before sending'
        why.append('Closing an application is hard to undo, so a person approves each closure.')
    elif r.kind == 'hold':
        s = 'Compliance approves wording, then automatic'
        why.append('Compliance owns all contact. Neutral holding note only, no reason given.')
    elif r.kind is None or (isinstance(r.kind, float) and pd.isna(r.kind)):
        s = 'Human review: no message'
        why.append('Status Rejected with a fixable code, or reviewer text that is unclear. A person decides.')
    else:
        if r.source.startswith('Inferred'):
            s = 'Confirm inferred code first'
            why.append('Cause read from reviewer text, so a person confirms the code first.')
        if r.call_slot in CALLED:
            if s.startswith('Ready'):
                s = 'Call first, nudge is backup'
            why.append('Has a call slot this week. The written nudge still goes as backup.')
    return pd.Series([s, ' '.join(why)])


# ---------- merchant replies (simulated) ----------
def handle_reply(text):
    """What the agent does with a merchant's reply. Keywords only, no free-text AI. Returns (action, detail)."""
    t = (text or '').strip().strip('"\'').lower()
    if t == 'stop':
        return 'Opt out', 'Stop all messages to this merchant now. Cancel Day 3 and Day 7.'
    if t == 'help':
        return 'Send to a person', 'High-priority case in the Onboarding Ops queue. Cancel Day 3 and Day 7. A person replies.'
    return 'Send to a person', 'Not a keyword the agent handles. A person reads it. Day 3 and Day 7 are paused.'


# ---------- the whole pipeline ----------
def run(A, CAT, budget_value=8, budget_small=2, ai=None):
    ai = load_ai() if ai is None else ai
    input_checks(A)
    rows, excluded = [], []
    for _, r in A.iterrows():
        if r.application_status == 'Activated':
            excluded.append(r.application_id)
            continue
        code, src, ai_note = diagnose(r, ai)
        locked = (r.application_status == 'Rejected') and code not in ('R10', 'R12')
        kind = ('closure' if code == 'R10' else 'hold' if code == 'R12'
                else None if (code == 'UNCLASSIFIED' or locked) else 'nudge')
        rows.append(dict(application_id=r.application_id, code=code, source=src, ai_note=ai_note, kind=kind,
                         status=r.application_status, language=r.preferred_language,
                         opted=(r.whatsapp_opted_in == 'Yes'), days=int(r.days_since_last_activity),
                         attempts=int(r.attempts), contacts=int(r.support_contacts),
                         tpv=float(r.expected_monthly_tpv_inr_lakh), step=r.step_reached,
                         merchant_name=next((str(r[c]) for c in NAME_COLS if c in A.columns and isinstance(r[c], str) and r[c].strip()), None),
                         btype=r.business_type, reviewer_text=r.rejection_message if isinstance(r.rejection_message, str) else '',
                         signup=r.signup_date))
    P = pd.DataFrame(rows)
    rec = P[P.kind == 'nudge']
    median_tpv = float(rec.tpv.median()) if len(rec) else 0.0

    P['stuck'] = (P.attempts >= 3) | (P.contacts >= 2)
    P['lane'] = np.where(P.kind != 'nudge', 'X: Closure, compliance or review',
                np.where(P.tpv >= LANE_A_TPV, 'A: White-glove',
                np.where(P.stuck, 'B: Assisted', 'C: Self-serve')))
    P['days_to_fix'] = P.code.map(lambda c: int(CAT.loc[c, 'typical_days_to_fix']) if c in CAT.index else 0)
    P['score'] = np.where(P.kind == 'nudge',
                          P.tpv * P.days.map(fresh) * P.days_to_fix.map(ease) * P.source.map(evid), np.nan)
    P['score'] = P.score.round(1)
    P = P.sort_values(['score', 'application_id'], ascending=[False, True], na_position='last').reset_index(drop=True)
    P['priority_rank'] = np.where(P.kind == 'nudge', P.index + 1, np.nan)

    cand = P[P.kind == 'nudge']
    value_ids = cand.head(budget_value).application_id.tolist()
    small_ids = cand[(~cand.application_id.isin(value_ids)) & (cand.tpv < median_tpv) & cand.stuck].head(budget_small).application_id.tolist()
    next_ids = cand[~cand.application_id.isin(value_ids + small_ids)].head(5).application_id.tolist()
    P['call_slot'] = np.where(P.application_id.isin(value_ids), 'Value slot',
                     np.where(P.application_id.isin(small_ids), 'Stuck small-merchant slot',
                     np.where(P.application_id.isin(next_ids), 'Next in line', '')))

    P = pd.concat([P, P.apply(build_messages, axis=1, result_type='expand')], axis=1)
    P['guardrail_result'] = P.apply(lambda r: 'NO MESSAGE (person decides)' if not r.msg
                                    else 'PASS' if not r.fails else 'FAIL: ' + '; '.join(sorted(set(r.fails))), axis=1)
    P[['send_status', 'hold_reason']] = P.apply(send_status, axis=1)
    P['light'] = P.send_status.map(lambda s: 'GREEN' if s == 'Ready to send' else
                                   'RED' if s.startswith(('Human only', 'Human review', 'Compliance')) else 'AMBER')
    P.loc[P.guardrail_result.str.startswith('FAIL'), 'light'] = 'RED'

    P['fixable'] = P.code.map(lambda c: CAT.loc[c, 'fixable'] if c in CAT.index else 'Unknown')
    P['recoverable'] = np.where(P.kind == 'nudge', 'Yes', 'No')
    P['decision'] = P.kind.map({'nudge': 'Recoverable: send the fix message', 'closure': 'Not recoverable: close politely (a person approves)',
                                'hold': 'Route to Compliance: neutral holding note only'}).fillna('Unclear: a person decides, no message')
    P['cause'] = P.code.map(lambda c: (c + ': ' + CAT.loc[c, 'reviewer_reason']) if c in CAT.index else 'Unclassified: a person reads it')
    P.loc[P.code == 'R13', 'cause'] = 'R13: Abandoned at ' + P.step
    P['evidence'] = P.source.map(lambda s: 'Catalog code' if s.startswith('Catalog') else
                                 'Inferred from reviewer text (confirm)' if s.startswith('Inferred') else
                                 'Reason unknown (abandoned)' if s.startswith('No rej') else s)
    P['owner'] = np.where(P.kind == 'hold', 'Compliance', np.where(P.kind == 'closure', 'Onboarding Ops lead',
                 np.where(P.kind.isna(), 'Onboarding Ops (triage)',
                 np.where(P.call_slot.isin(CALLED), 'Onboarding Ops / RM (call)', 'Automated'))))
    P['action'] = np.select(
        [P.kind == 'hold', P.kind == 'closure', P.kind.isna(), P.call_slot.isin(CALLED), P.call_slot == 'Next in line'],
        ['Compliance holding note on Day 0 and Day 7', 'Polite closure after a person approves; no workaround',
         'A person decides; no message', 'Call this week; Day 0 message goes as backup',
         'Send nudge sequence; call if a slot frees up'],
        'Send nudge sequence (Day 0, 3, 7)')
    age = P.signup.map(lambda d: (SNAPSHOT - pd.to_datetime(d, format='%d %b %Y')).days)
    P['data_flag'] = np.where(P.days > age, 'Date check: idle longer than account age', '')
    bad = P.code.map(EXPECTED_STEP).notna() & (P.code.map(EXPECTED_STEP) != P.step)
    P.loc[bad, 'data_flag'] = (P.loc[bad, 'data_flag'] + ' | Step check: code at an unexpected step').str.strip(' |')

    S = summary(P, excluded, median_tpv)
    return P, S


def summary(P, excluded, median_tpv):
    rec = P[P.kind == 'nudge']
    by = rec.groupby('code').agg(n=('tpv', 'size'), tpv=('tpv', 'sum')).round(1)
    g = lambda c, k: float(by.loc[c, k]) if c in by.index else 0
    return dict(
        total=len(P) + len(excluded), excluded=len(excluded), in_scope=len(P),
        recoverable=len(rec), recoverable_tpv=round(rec.tpv.sum(), 1),
        closures=int((P.kind == 'closure').sum()), holds=int((P.kind == 'hold').sum()),
        person_review=int(P.kind.isna().sum()),
        lights=P.light.value_counts().to_dict(), statuses=P.send_status.value_counts().to_dict(),
        lanes=P.lane.str[0].value_counts().to_dict(), whatsapp=int(P.opted.sum()), email=int((~P.opted).sum()),
        guardrail_fail=int(P.guardrail_result.str.startswith('FAIL').sum()),
        date_flags=int(P.data_flag.str.contains('Date').sum()), step_flags=int(P.data_flag.str.contains('Step').sum()),
        median_tpv=round(median_tpv, 1),
        causes=[('Name mismatch (PAN R01 + bank R03)', int(g('R01', 'n') + g('R03', 'n')), round(g('R01', 'tpv') + g('R03', 'tpv'), 1)),
                ('Missing website policy pages (R06)', int(g('R06', 'n')), g('R06', 'tpv')),
                ('GST details not verified (R02)', int(g('R02', 'n')), g('R02', 'tpv')),
                ('Abandoned, reason unknown (R13)', int(g('R13', 'n')), g('R13', 'tpv'))],
        by_code=by.reset_index().to_dict('records'),
        called=P[P.call_slot.isin(CALLED)].application_id.tolist())


OUTPUT_COLUMNS = {
    'priority_rank': 'Priority rank', 'application_id': 'Application', 'light': 'Light', 'cause': 'Diagnosed cause',
    'evidence': 'Evidence', 'ai_note': 'AI second opinion', 'fixable': 'Fixable', 'recoverable': 'Recoverable', 'decision': 'Decision',
    'action': 'Action', 'owner': 'Owner', 'call_slot': 'Call slot', 'lane': 'Lane', 'send_status': 'Send status',
    'hold_reason': 'Why it waits', 'language': 'Language', 'channel': 'Channel', 'email_subject': 'Email subject (Day 0)', 'subject3': 'Email subject (Day 3)', 'subject7': 'Email subject (Day 7)',
    'msg': 'Day 0 message', 'day3': 'Day 3 follow-up', 'day7': 'Day 7 follow-up', 'eng': 'English meaning',
    'guardrail_result': 'Guardrail check', 'data_flag': 'Data flag', 'score': 'Priority score', 'days': 'Days idle',
    'attempts': 'Attempts', 'contacts': 'Support contacts', 'tpv': 'Expected TPV (Rs lakh)', 'step': 'Step reached',
    'btype': 'Business type', 'reviewer_text': 'Reviewer text'}


def output_table(P):
    T = P[list(OUTPUT_COLUMNS)].rename(columns=OUTPUT_COLUMNS)
    T['Priority rank'] = T['Priority rank'].astype('Int64')
    return T.sort_values(['Priority rank', 'Application'], na_position='last').reset_index(drop=True)


def output_hash(P):
    return hashlib.sha256(output_table(P).to_csv(index=False).encode('utf-8')).hexdigest()[:8]


if __name__ == '__main__':
    A, CAT = load_data()
    P, S = run(A, CAT)
    G, Y, Rd, B, X = '\033[92m', '\033[93m', '\033[91m', '\033[1m', '\033[0m'
    lt, st = S['lights'], S['statuses']
    print(B + 'RAZORPAY ONBOARDING RECOVERY: RUN ON SNAPSHOT 30 Sep 2026' + X + '   output hash ' + output_hash(P))
    print('%d read | %d excluded (activated) | %d in scope' % (S['total'], S['excluded'], S['in_scope']))
    print(B + 'RECOVERABLE   %d applications | Rs %.1f lakh a month' % (S['recoverable'], S['recoverable_tpv']) + X)
    print('NOT RECOVERABLE  %d  (%d closures, %d Compliance, %d person review)' % (S['in_scope'] - S['recoverable'], S['closures'], S['holds'], S['person_review']))
    print(G + 'GREEN  %2d  send automatically after the check' % lt.get('GREEN', 0) + X)
    print(Y + 'AMBER  %2d  NEEDS YOU: %d calls, %d codes to confirm' % (
        lt.get('AMBER', 0), st.get('Call first, nudge is backup', 0), st.get('Confirm inferred code first', 0)) + X)
    print(Rd + 'RED    %2d  PERSON OWNS: %d closures, %d Compliance holds, %d person review' % (
        lt.get('RED', 0), st.get('Human only: approve before sending', 0), st.get('Compliance approves wording, then automatic', 0), st.get('Human review: no message', 0)) + X)
    print((Rd if S['guardrail_fail'] else G) + 'BLOCKED %d guardrail failures' % S['guardrail_fail'] + X)
    print(Y + 'DATA   %2d  date-check flags | %d step-check flags' % (S['date_flags'], S['step_flags']) + X)
    print('TOP CAUSES  ' + ' | '.join('%s: %d (Rs %.1f lakh)' % c for c in S['causes']))
    print('CALLS THIS WEEK  ' + ' '.join(S['called']))
