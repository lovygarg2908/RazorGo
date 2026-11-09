"""Checks that prove the agent works. Run:  python test_agent.py"""
import agent as ag, messages as M, rules as R

A, CAT = ag.load_data()
P, S = ag.run(A, CAT)
checks = []
def check(name, ok): checks.append((name, bool(ok))); print(('PASS ' if ok else 'FAIL ') + name)

check('100 applications read, 25 excluded, 75 in scope', (S['total'], S['excluded'], S['in_scope']) == (100, 25, 75))
check('67 recoverable worth Rs 933.9 lakh', (S['recoverable'], S['recoverable_tpv']) == (67, 933.9))
check('5 closures and 3 Compliance holds', (S['closures'], S['holds']) == (5, 3))
check('0 guardrail failures on the 75 rows', S['guardrail_fail'] == 0)
check('No nudge to a closure, Compliance or review case', not ((P.kind != 'nudge') & P.msg.str.contains(r'\[resume link\]')).any())
check('No WhatsApp message to a merchant who did not opt in', not ((~P.opted) & (P.channel == 'WhatsApp')).any())
check('Every closure waits for a person', (P[P.kind == 'closure'].light == 'RED').all())
check('56 Automatic, 11 Check first, 8 Person handles', (S['lights'].get('GREEN'), S['lights'].get('AMBER'), S['lights'].get('RED')) == (56, 11, 8))
check('Tamil, Kannada and Marathi cases are not held for language review', not P.send_status.str.contains('Native').any())
check('Every email nudge has a subject line for Day 0, and for Day 3 and Day 7 when sent',
      ((P[(P.channel == 'Email') & (P.msg != '')].email_subject != '').all())
      and ((P[(P.channel == 'Email') & (P.day3 != '')].subject3 != '').all()) and ((P[(P.channel == 'Email') & (P.day7 != '') & (P.kind == 'nudge')].subject7 != '').all()))
check('Reviewer-text keywords: blurry reads as unreadable, bank account verify reads as bank verification, PAN verify stays PAN',
      (R.kw('photo is blurry'), R.kw('bank account verify nahi hua'), R.kw('PAN verify nahi hua')) == ('R05', 'R04', 'R01'))
check('Same output on a second run', ag.output_hash(P) == ag.output_hash(ag.run(A, CAT)[0]))

n = fails = 0
for lang in M.LANGS:
    for code in list(M.BODY):
        for tone in ['soft', 'reminder', 'gentle']:
            for stuck in [False, True]:
                for ch in ['WhatsApp', 'Email']:
                    for step in (['Business details', 'KYC docs', 'Bank verification'] if code == 'R13' else [None]):
                        n += 1; fails += bool(R.check(M.day0(code, lang, tone=tone, channel=ch, stuck=stuck, step=step), 'nudge', lang, code, ch, True if ch == 'WhatsApp' else None))
check('All %d Day 0 message variants in six languages pass the checker' % n, fails == 0)
n3 = f3 = 0; longest = 0
for lang in M.LANGS:
    for code in list(M.BODY):
        for step in (['Business details', 'KYC docs', 'Bank verification', 'Website/App review'] if code == 'R13' else [None]):
            for fn in (M.day3, M.day7):
                for ch in ['WhatsApp', 'Email']:
                    m = M.wrap(fn(code, lang, step), lang, ch); n3 += 1
                    f3 += bool(R.check(m, 'nudge', lang, code, ch, True if ch == 'WhatsApp' else None))
                    if ch == 'WhatsApp': longest = max(longest, len(m))
check('All %d Day 3 and Day 7 variants pass the checker' % n3, f3 == 0)
longest0 = max(len(M.day0(c, 'English', tone=t, channel='WhatsApp', stuck=True, step='KYC docs' if c == 'R13' else None)) for c in M.BODY for t in ['soft', 'reminder', 'gentle'])
check('Longest English WhatsApp Day 0 is under 1,000 characters (%d)' % longest0, longest0 < 1000)
check('Steps line counts from the current step to the end', M.steps_line('English', 'Business details').endswith('a few steps away from completing it.')
      and 'one step' in M.steps_line('English', 'Website/App review') and 'two steps' in M.steps_line('English', 'Bank verification'))
check('Name is used when safe, otherwise the standard greeting', M.greeting('English', 'Zenith Exports') == 'Dear Zenith Exports,'
      and M.greeting('English', None) == 'Dear Valued Merchant,' and M.greeting('English', 'Risk Traders 24') == 'Dear Valued Merchant,')
check('HELP goes to a person, STOP opts out', ag.handle_reply('HELP')[0] == 'Send to a person' and ag.handle_reply('stop')[0] == 'Opt out')
check('No emoji in any English Day 0 message', not any(R.has_emoji(M.day0(c, 'English', 'soft', 'WhatsApp', False, 'KYC docs' if c == 'R13' else None)) for c in M.BODY))
bad = {'promise and date': 'Your account will be approved within 2 days. Continue here: [resume link] Reply STOP',
       'screening reason': 'On hold due to compliance screening. Continue here: [resume link] Reply STOP'}
check('Bad messages are blocked', all(R.check(t, 'nudge', 'English', 'R01', 'WhatsApp', True) for t in bad.values()))
print('\n%d of %d checks passed' % (sum(ok for _, ok in checks), len(checks)))
