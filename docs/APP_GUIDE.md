# App guide

A two-minute tour, and where each requirement in the brief lives.

## Two-minute tour

1. Open **Summary**. The blue banner gives the three headline numbers. Below it: where the 75 applications go, who acts, the top three fixable causes, and a chart with a dropdown. Hover any (?) for the definition.
2. Open **Action queue**. The top row is what the agent already did. Below it, the 19 cases that need a person are grouped by who acts, with the next step and time limit. Open any case at the bottom.
3. Open **Applications**. Click the first row (A3031). Scroll down. Four boxes show the case:
   1. **Why it stalled**: the cause and how we know it.
   2. **The fix, in simple words**: in the merchant's language, with the English meaning beside it.
   3. **Decision**: fixable, recoverable, who handles it, and whether a call is planned.
   4. **The drafted message**: Day 0, Day 3 and Day 7, as a WhatsApp message or an email with a subject line.
4. In **Applications**, choose "Closed or Compliance" and click A3051. It has no rejection code, only a note saying the category is not supported. The agent treats it as a restricted business: no fix message, a polite closure after a person approves.
5. Open **Product team** to see which fixable causes block the most merchants.
6. Open **Safety and tests** and try "Promises approval and a date" in the safety checker. It is blocked, with the reason.

## What the three labels mean

| Label | Meaning |
| --- | --- |
| Automatic | Goes out on its own after the safety check |
| Check first | A person checks it first (a planned call, or a code read from the reviewer's note) |
| Person handles | A person owns it from start to finish (closure, Compliance, or unclear) |

## The brief, point by point

| The brief asks for | Where it is |
| --- | --- |
| Diagnose why each application stalled | Applications, box 1 |
| Explain the fix in simple language in the merchant's language | Applications, box 2 |
| Decide recoverable, close, or route to Compliance | Applications, box 3 (and the Recoverable column) |
| Draft the right nudge | Applications, box 4 |
| For every non-activated application: cause, fixable or not, recoverable or not, drafted nudge in language and channel | Applications table and `output/Razorpay_P3_Output.xlsx` |
| WhatsApp only if opted in; email otherwise | Box 4 states the channel and why. 56 WhatsApp, 19 email |
| Never suggest a workaround for restricted categories; never reveal compliance reasons | Safety and tests; closure and holding-note wording |
| Summary: recoverable count, TPV at stake, top three causes | Summary (and the Key findings sheet in the Excel, with charts) |
| Human in the loop: what a person must look at, next steps, what is done | Action queue |
| Tell the product team which fixable causes affect the most merchants | Product team |
| Prioritise by TPV and days since activity | Priority score and call slots (More, How it works; the priority rank is in the Excel) |
| Propose a product change for the top cause | Product team, "Fix this first" |
| Follow-up sequence with stopping rules | More, Follow-up plan |

## The written answers

More, Written answers lists all 11 questions with the live number that backs each one and the screen to look at.

## Notes

- Everything is a dry run. Nothing is sent.
- Numbers on screen come from the same code the tests check, so the screen cannot drift from the tests.
- The 30-case labelling result (builder-labelled, cause only) is on **Safety and tests**, read from `gold_results.json`, with its limits stated.
