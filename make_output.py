"""Builds the formatted Excel output table (the deliverable the brief asks for).
Run:  python make_output.py        (writes output/Razorpay_P3_Output.xlsx)
The app's Download button uses the same code."""
import io
import os

import pandas as pd
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

import agent as ag
import actions as AC
import findings as FD
from openpyxl.chart import BarChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.worksheet.properties import PageSetupProperties

FONT = 'Arial'
HEAD = PatternFill('solid', start_color='012652')
FILL = {'GREEN': 'DCFCE7', 'AMBER': 'FEF3C7', 'RED': 'FEE2E2'}
LABEL = {'GREEN': 'Automatic', 'AMBER': 'Check first', 'RED': 'Person handles'}
THIN = Side(style='thin', color='D1D5DB')
WIDTH = {'Priority rank': 9, 'Application': 12, 'Light': 15, 'Diagnosed cause': 38, 'Evidence': 26, 'AI second opinion': 30, 'Fixable': 14,
         'Recoverable': 13, 'Decision': 40, 'Action': 42, 'Owner': 24, 'Call slot': 18, 'Lane': 22, 'Send status': 30, 'Why it waits': 40,
         'Language': 11, 'Channel': 11, 'Email subject (Day 0)': 34, 'Email subject (Day 3)': 34, 'Email subject (Day 7)': 34,
         'Day 0 message': 70, 'Day 3 follow-up': 55, 'Day 7 follow-up': 55, 'English meaning': 70, 'Guardrail check': 16, 'Data flag': 30}


def _style_header(ws, ncols, row=1):
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = Font(name=FONT, bold=True, color='FFFFFF', size=10)
        cell.fill = HEAD
        cell.alignment = Alignment(wrap_text=True, vertical='center')
    ws.row_dimensions[row].height = 30


BLUE, GREY = '0D94FB', '94A3B8'


def _bar(ws, title, cats, vals, anchor, color=BLUE, ytitle=None):
    """Horizontal bar chart from a cell range. cats and vals are Reference objects."""
    ch = BarChart()
    ch.type = 'bar'
    ch.style = 10
    ch.title = title
    ch.legend = None
    ch.add_data(vals, titles_from_data=True)
    ch.set_categories(cats)
    ch.series[0].graphicalProperties.solidFill = color
    ch.series[0].graphicalProperties.line.solidFill = color
    ch.dataLabels = DataLabelList()
    ch.dataLabels.showVal = True
    ch.dataLabels.showSerName = False
    ch.dataLabels.showCatName = False
    ch.dataLabels.showLegendKey = False
    ch.x_axis.scaling.orientation = 'maxMin'   # biggest on top
    ch.x_axis.delete = False
    ch.y_axis.delete = False
    ch.y_axis.majorGridlines = None
    if ytitle:
        ch.y_axis.title = ytitle
    ch.width, ch.height = 17, 8
    ws.add_chart(ch, anchor)


def _put(ws, r, c, v, bold=False, fill=None, color='000000', wrap=False, fmt=None):
    cell = ws.cell(row=r, column=c, value=v)
    cell.font = Font(name=FONT, size=10, bold=bold, color=color)
    cell.alignment = Alignment(wrap_text=wrap, vertical='top')
    if fill:
        cell.fill = PatternFill('solid', start_color=fill)
    if fmt:
        cell.number_format = fmt
    return cell


def _table(ws, r0, headers, rows, fmts=None):
    for j, h in enumerate(headers, 1):
        _put(ws, r0, j, h, bold=True, fill='012652', color='FFFFFF', wrap=True)
    for i, row in enumerate(rows, 1):
        for j, v in enumerate(row, 1):
            _put(ws, r0 + i, j, v, wrap=(j == 1), fmt=(fmts or {}).get(j))
            ws.cell(row=r0 + i, column=j).border = Border(bottom=THIN)
    return r0 + 1, r0 + len(rows)


def _findings_sheet(wb, S):
    """First sheet: the key findings a product manager needs, as tables plus charts."""
    ws = wb.create_sheet('Key findings', 0)
    ws.sheet_view.showGridLines = False
    _put(ws, 1, 1, 'Key findings: merchant onboarding recovery (sample data, nothing is sent)', bold=True).font = Font(name=FONT, size=14, bold=True)
    _put(ws, 2, 1, '%d read, %d already activated and left out, %d in scope. Payments are expected monthly volume (TPV), an estimate of what is at stake, not money recovered.'
         % (S['total'], S['excluded'], S['in_scope']), color='4B5563')
    CT = FD.cause_table(S)
    # Table 1: causes
    _put(ws, 4, 1, '1. Which causes block the most merchants (recoverable applications)', bold=True)
    a, b = _table(ws, 5, ['Cause', 'Merchants', 'Payments (Rs lakh a month)', 'Share of recoverable'],
                  [[r['Cause'], r['Merchants'], r['Payments (Rs lakh a month)'], r['Share of recoverable']] for _, r in CT.iterrows()],
                  fmts={3: '0.0', 4: '0%'})
    n1 = b
    # Table 2: where the applications go
    r2 = b + 3
    _put(ws, r2 - 1, 1, '2. Where the %d applications go' % S['in_scope'], bold=True)
    a2, b2 = _table(ws, r2, ['Outcome', 'Applications'], [[k, v] for k, v in FD.where_they_go(S)])
    # Table 3: who acts
    r3 = b2 + 3
    _put(ws, r3 - 1, 1, '3. Who acts', bold=True)
    a3, b3 = _table(ws, r3, ['Light', 'Applications'], [[k, v] for k, v in FD.who_acts(S)])
    # Table 4: channel
    r4 = b3 + 3
    _put(ws, r4 - 1, 1, '4. Channel', bold=True)
    a4, b4 = _table(ws, r4, ['Channel', 'Applications'], [['WhatsApp (opted in)', S['whatsapp']], ['Email (not opted in)', S['email']]])
    # Table 5: proposed fixes
    r5 = b4 + 3
    _put(ws, r5 - 1, 1, '5. Proposed product change for each cause (a proposal, not a fact from the data)', bold=True)
    for i, (_, r) in enumerate(CT.iterrows()):
        _put(ws, r5 + i, 1, r['Cause'], bold=True, wrap=True)
        c = _put(ws, r5 + i, 2, r['Proposed product change'], wrap=True)
        ws.merge_cells(start_row=r5 + i, start_column=2, end_row=r5 + i, end_column=4)
        ws.row_dimensions[r5 + i].height = 42
    ws.column_dimensions['A'].width = 40
    ws.column_dimensions['B'].width = 14
    ws.column_dimensions['C'].width = 18
    ws.column_dimensions['D'].width = 18
    ws.column_dimensions['E'].width = 3
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    # charts to the right
    _bar(ws, 'Merchants blocked, by cause', Reference(ws, min_col=1, min_row=a, max_row=b), Reference(ws, min_col=2, min_row=a - 1, max_row=b), 'F4')
    _bar(ws, 'Payments at stake by cause (Rs lakh a month)', Reference(ws, min_col=1, min_row=a, max_row=b),
         Reference(ws, min_col=3, min_row=a - 1, max_row=b), 'F21', color='0E7490')
    _bar(ws, 'Where the %d applications go' % S['in_scope'], Reference(ws, min_col=1, min_row=a2, max_row=b2),
         Reference(ws, min_col=2, min_row=a2 - 1, max_row=b2), 'F38', color='7C3AED')
    _bar(ws, 'Who acts (Automatic / Check first / Person handles)', Reference(ws, min_col=1, min_row=a3, max_row=b3),
         Reference(ws, min_col=2, min_row=a3 - 1, max_row=b3), 'F55', color='1E7E34')


def _queue_sheet(wb, P):
    """Second sheet: the reviewer's to-do list (cases that need a person)."""
    ws = wb.create_sheet('Action queue', 1)
    Q = AC.action_queue(P).drop(columns=['g', 'Next step'])
    cols = ['Group', 'Application', 'Do this', 'Owner', 'Time limit', 'Language', 'Channel', 'Payments (Rs lakh)', 'Days idle', 'Light']
    for j, h in enumerate(cols, 1):
        _put(ws, 1, j, h, bold=True, fill='012652', color='FFFFFF', wrap=True)
    for i, (_, r) in enumerate(Q.iterrows(), 2):
        for j, h in enumerate(cols, 1):
            v = LABEL[r[h]] if h == 'Light' else r[h]
            c = _put(ws, i, j, v, wrap=True)
            c.border = Border(bottom=THIN)
        ws.cell(row=i, column=10).fill = PatternFill('solid', start_color=FILL[r['Light']])
    for col, w in zip('ABCDEFGHIJ', (26, 12, 70, 24, 26, 11, 11, 14, 10, 15)):
        ws.column_dimensions[col].width = w
    ws.row_dimensions[1].height = 30
    ws.freeze_panes = 'C2'
    ws.auto_filter.ref = ws.dimensions


def excel_bytes(P, S):
    T = ag.output_table(P).copy()
    lights = T['Light'].tolist()
    T['Light'] = T['Light'].map(LABEL)
    by = pd.DataFrame(S['by_code'])
    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine='openpyxl') as xw:
        # Summary sheet
        summ = pd.DataFrame([
            ['Applications read', S['total']], ['Already activated (left out)', S['excluded']], ['In scope (stalled or rejected)', S['in_scope']],
            ['Recoverable', S['recoverable']], ['Expected payments at stake (Rs lakh a month)', S['recoverable_tpv']],
            ['Closed politely after a person approves', S['closures']], ['Routed to Compliance', S['holds']],
            ['Automatic', S['lights'].get('GREEN', 0)], ['Check first', S['lights'].get('AMBER', 0)], ['Person handles', S['lights'].get('RED', 0)],
            ['Sent by WhatsApp (opted in)', S['whatsapp']], ['Sent by email (not opted in)', S['email']],
            ['Messages blocked by the safety checker', S['guardrail_fail']], ['Output check code', ag.output_hash(P)]],
            columns=['Measure', 'Value'])
        summ.to_excel(xw, sheet_name='Summary', index=False)
        # Causes sheet (fixable causes, merchants and payments)
        T.to_excel(xw, sheet_name='Output', index=False)

        ws = xw.sheets['Summary']
        _style_header(ws, 2)
        ws.column_dimensions['A'].width = 48
        ws.column_dimensions['B'].width = 16
        for row in ws.iter_rows(min_row=2):
            for cell in row:
                cell.font = Font(name=FONT, size=10)
                cell.border = Border(bottom=THIN)
        wo = xw.sheets['Output']
        ncols = wo.max_column
        _style_header(wo, ncols)
        headers = [wo.cell(row=1, column=i).value for i in range(1, ncols + 1)]
        for i, h in enumerate(headers, 1):
            wo.column_dimensions[get_column_letter(i)].width = WIDTH.get(h, 14)
        for r_idx in range(2, wo.max_row + 1):
            for c_idx in range(1, ncols + 1):
                cell = wo.cell(row=r_idx, column=c_idx)
                cell.font = Font(name=FONT, size=10)
                cell.alignment = Alignment(wrap_text=True, vertical='top')
                cell.border = Border(bottom=THIN)
            wo.cell(row=r_idx, column=3).fill = PatternFill('solid', start_color=FILL[lights[r_idx - 2]])
        wo.freeze_panes = 'C2'
        wo.auto_filter.ref = wo.dimensions
        _findings_sheet(xw.book, S)
        _queue_sheet(xw.book, P)
    return buf.getvalue()


if __name__ == '__main__':
    A, CAT = ag.load_data()
    P, S = ag.run(A, CAT)
    os.makedirs('output', exist_ok=True)
    with open(os.path.join('output', 'Razorpay_P3_Output.xlsx'), 'wb') as f:
        f.write(excel_bytes(P, S))
    print('Wrote output/Razorpay_P3_Output.xlsx  (hash %s)' % ag.output_hash(P))
