"""Key findings shared by the app (Summary, Product team) and the Excel download,
so the screen and the spreadsheet always show the same numbers."""
import pandas as pd

# Proposed product changes for the product team (proposals, not facts from the data)
PRODUCT_FIX = {
    'Name mismatch (PAN R01 + bank R03)': ('Show the name found on the PAN or bank account next to the business name, right when the merchant uploads it, '
                                           'with a one-tap choice to correct either.'),
    'R06': 'Show a checklist of the four pages needed (Terms, Privacy, Refund, Contact) and check the website link before the merchant submits.',
    'R02': 'Check the GST number against the business name and address while the merchant types it, and show any mismatch before submit.',
    'R04': 'Verify the bank account on the spot and show a clear error and retry, instead of a rejection days later.',
    'R05': 'Check the photo quality and file size at upload, and ask for a clearer picture straight away.',
    'R09': 'Show the name and date of birth read from the ID next to what was typed, before submit.',
    'R07': 'Test that the website link is public before submit and say what is missing.',
    'R08': 'Say which proof is accepted and how recent it must be, next to the upload box.',
    'R11': 'At category selection, ask for a short note or website evidence when the website looks different from the category.',
    'R13': 'Add a one-tap "What stopped you?" question when a merchant leaves, so the reason is known next time.',
}
CAUSE_NAME = {'R01': 'PAN name mismatch', 'R03': 'Bank account name mismatch', 'R02': 'GST details not verified', 'R04': 'Bank verification failed',
              'R05': 'Document unreadable', 'R06': 'Website missing policy pages', 'R07': 'Website not live', 'R08': 'Address proof missing or old',
              'R09': 'Signatory details incomplete', 'R11': 'Category differs from website', 'R13': 'Abandoned, reason unknown'}
NAME_KEY = 'Name mismatch (PAN R01 + bank R03)'
LABEL = {'GREEN': 'Automatic', 'AMBER': 'Check first', 'RED': 'Person handles'}


def grouped(S):
    """Recoverable causes grouped for the product team: {key: [merchants, payments]}.
    PAN (R01) and bank-name (R03) mismatch are one product fix, so they are one cause."""
    grp = {}
    for r in S['by_code']:
        key = NAME_KEY if r['code'] in ('R01', 'R03') else r['code']
        g = grp.setdefault(key, [0, 0.0])
        g[0] += int(r['n'])
        g[1] += float(r['tpv'])
    return grp


def cause_table(S):
    """One row per cause (abandoned included, last flag marks it), biggest first."""
    rows = []
    for key, (n, tp) in grouped(S).items():
        nm = 'Name mismatch (PAN and bank account)' if key == NAME_KEY else CAUSE_NAME.get(key, key)
        rows.append({'Cause': nm, 'Merchants': n, 'Payments (Rs lakh a month)': round(tp, 1),
                     'Share of recoverable': round(n / max(S['recoverable'], 1), 3),
                     'Proposed product change': PRODUCT_FIX.get(key, ''), 'key': key})
    df = pd.DataFrame(rows)
    df['_a'] = (df['key'] == 'R13')
    return df.sort_values(['_a', 'Merchants', 'Payments (Rs lakh a month)'], ascending=[True, False, False]).drop(columns='_a').reset_index(drop=True)


def where_they_go(S):
    """The four places the in-scope applications end up. Adds up to in_scope."""
    ab = grouped(S).get('R13', [0, 0.0])[0]
    return [('Fixable: a specific fix message', S['recoverable'] - ab),
            ('Abandoned: reason unknown', ab),
            ('Closed politely (a person approves)', S['closures']),
            ('Compliance (neutral holding note)', S['holds'])]


def who_acts(S):
    return [(LABEL[k], S['lights'].get(k, 0)) for k in ('GREEN', 'AMBER', 'RED')]
