"""Writes docs/Message_Library.csv: every approved message piece in all six languages.
Run:  python export_message_library.py"""
import csv, os
import messages as M

rows = []
for ll in M.LANGS:
    pieces = [('Greeting', '', M.GREET[ll]), ('Opener, idle 7 days or less', '', M.OPEN_TONE['soft'][ll]),
              ('Opener, idle 8 to 30 days', '', M.OPEN_TONE['reminder'][ll]), ('Opener, idle 31 days or more', '', M.OPEN_TONE['gentle'][ll])]
    pieces += [('Steps line, %s left' % w, '', M.STEPS[ll][i]) for i, w in enumerate(['one step', 'two steps', 'three steps', 'four steps'])]
    pieces += [('Empathy line (stuck merchants)', '', M.EMPATHY[ll]), ('Fix label, choose one', '', M.FIX_LABEL['choose'][ll]),
               ('Fix label, steps to do', '', M.FIX_LABEL['do'][ll]), ('Fix label, abandoned', '', M.FIX_LABEL['r13'][ll]),
               ('Why it matters', '', M.WHY[ll]), ('Link line', '', M.CTA[ll]), ('Help line (WhatsApp)', '', M.HELP_W[ll]),
               ('Help line (email)', '', M.HELP_E[ll]), ('Opt-out line (WhatsApp)', '', M.STOP[ll]), ('Sign-off (email)', '', M.SIGN[ll]),
               ('Email subject, Day 0', '', M.SUBJ['day0'][ll]), ('Email subject, Day 3', '', M.SUBJ['day3'][ll]),
               ('Email subject, Day 7', '', M.SUBJ['day7'][ll]), ('Email subject, closure or holding note', '', M.SUBJ['plain'][ll])]
    pieces += [('Problem', k, v[ll][0]) for k, v in M.BODY.items()] + [('Fix', k, v[ll][1]) for k, v in M.BODY.items()]
    pieces += [('R10 closure', 'R10', M.CLOSE[ll]), ('R12 holding note, Day 0', 'R12', M.HOLD0[ll]), ('R12 holding note, Day 7', 'R12', M.HOLD7[ll])]
    rows += [(p, c, ll, t) for p, c, t in pieces]
os.makedirs('docs', exist_ok=True)
with open(os.path.join('docs', 'Message_Library.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['piece', 'code', 'language', 'text'])
    w.writerows(rows)
print('Wrote docs/Message_Library.csv with %d rows' % len(rows))
