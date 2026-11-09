"""The reviewer's to-do list: every case that needs a person, grouped by who acts,
with the next step and the time limit (from the PRD). Used by the Action queue tab and the Excel download."""
import pandas as pd

# (send_status -> group). Each case lands in exactly one group.
GROUPS = [
    ('Confirm the inferred code', 'Onboarding Ops (triage)', 'Same working day'),
    ('Make the call', 'Onboarding Ops or the RM', 'Within the week'),
    ('Approve the closure', 'Onboarding Ops lead', '2 working days'),
    ('Approve the holding note', 'Compliance', 'Wording signed off before launch'),
    ('Read the case and decide', 'Onboarding Ops', 'Same working day'),
]
BY_STATUS = {'Confirm inferred code first': 0, 'Call first, nudge is backup': 1,
             'Human only: approve before sending': 2, 'Compliance approves wording, then automatic': 3}


def _cause(c):
    return c.split(': ', 1)[1] if ': ' in c else c


def _step(r, g):
    c = _cause(r.cause)
    if g == 0:
        s = 'Check that "%s" (%s) is the right reason. Correct it if not.' % (c, r.code)
        return s + (' Then make the call.' if r.call_slot else ' Then the nudge goes out.')
    if g == 1:
        return 'Call in %s about: %s. The Day 0 message goes out anyway; Day 3 and 7 pause if the call connects.' % (r.language, c.lower())
    if g == 2:
        return 'Read the case. Approve the polite closure, or reopen it if the category is wrong. Nothing is sent until you approve.'
    if g == 3:
        return 'Compliance approves the neutral holding note, then owns every later contact. No reason is ever given to the merchant.'
    return 'Read the case and decide.'


def _short(r, g):
    c = _cause(r.cause)
    return ['Confirm %s%s' % (r.code, ', then call' if r.call_slot else ', then nudge goes out'),
            'Call in %s: %s' % (r.language, c.lower().replace(' mandatory', '').replace(' or mismatched', '')),
            'Approve or reopen the closure', 'Compliance approves the holding note', 'Read the case and decide'][g]


def action_queue(P):
    W = P[P.light != 'GREEN'].copy()
    W['g'] = W.send_status.map(BY_STATUS).fillna(4).astype(int)
    rows = []
    for r in W.itertuples():
        name, owner, limit = GROUPS[r.g]
        rows.append({'g': r.g, 'Group': name, 'Application': r.application_id, 'Next step': _short(r, r.g), 'Do this': _step(r, r.g), 'Owner': owner,
                     'Time limit': limit, 'Language': r.language, 'Channel': r.channel,
                     'Payments (Rs lakh)': r.tpv, 'Days idle': r.days, 'Light': r.light})
    df = pd.DataFrame(rows)
    return df.sort_values(['g', 'Payments (Rs lakh)'], ascending=[True, False]).reset_index(drop=True)


def done_by_agent(P, S):
    """What the agent already did, so the person sees what is NOT left for them."""
    green = int((P.light == 'GREEN').sum())
    return [('Diagnosed', len(P), 'every in-scope application has a cause and a source'),
            ('Messages drafted', int((P.msg != '').sum()), 'in the merchant\'s language, with follow-ups'),
            ('Safety-checked', len(P) - S['guardrail_fail'], 'blocked by the checker: %d' % S['guardrail_fail']),
            ('Queued automatically', green, 'no person needed')]
