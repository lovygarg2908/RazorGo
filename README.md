# Merchant Onboarding Recovery Agent

Razorpay Campus AI Build-a-thon, Problem 3 (merchant onboarding and KYC drop-off recovery). Individual submission by Deeksha Das Sandeepan, BITSoM.

You can check out the app here -> https://razorgo-5ts7rypg5ljjldcbhnekas.streamlit.app/

An internal tool for the Razorpay Onboarding Ops team. For every stalled or rejected application it:

1. **Diagnoses why it stalled** (rejection code, reviewer note, or the step where the merchant stopped).
2. **Explains the fix in simple words**, in the merchant's language (English, Hindi, Hinglish, Tamil, Kannada or Marathi).
3. **Decides** whether the case is recoverable, must be closed politely, or goes to Compliance.
4. **Drafts the nudge** on the right channel: WhatsApp only if the merchant opted in, otherwise email with a subject line.

It also tells the product team which fixable causes block the most merchants.

**Live app:** `[paste your Streamlit link here]`
**Sample data only. Dry run: no message is ever sent.**

---

## Results on the sample data (snapshot 30 Sep 2026)

| Measure | Result |
| --- | --- |
| Applications read | 100 (25 already activated, 75 in scope) |
| Recoverable | **67**, worth **Rs 933.9 lakh a month** in expected payment volume (what is at stake, not money recovered) |
| Closed politely after a person approves (restricted business) | 5 |
| Routed to Compliance (neutral holding note, no reason given) | 3 |
| Automatic / Check first / Person handles | 56 / 11 / 8 |
| Channel | 56 WhatsApp (opted in), 19 email |
| Top fixable causes | Name mismatch 16 (Rs 132.2 lakh), website policy pages 7 (Rs 128.1 lakh), GST details 6 (Rs 106.3 lakh) |
| Abandoned, reason unknown | 22 (Rs 307.6 lakh). The agent never guesses a reason for these |
| Message variants checked by the safety checker | 1,272, with 0 blocked |
| App checks | 20 of 20 pass |
| Output check code | `d9e1209e` (same input gives the same code on every run) |

There is no outcome data in the pack, so **no recovery rate is claimed**.

## What to look at in the app

| Screen | What it shows |
| --- | --- |
| **Summary** | One screen of key findings: 67 of 75 recoverable, payments at stake, where the 75 go, who acts (Automatic, Check first, Person handles), top three fixable causes, channel and language, and a chart you can switch with a dropdown. Hover the (?) for definitions |
| **Action queue** | The reviewer's to-do list: what the agent already did, then the 19 cases that need a person, grouped by who acts (confirm a code, make a call, approve a closure, Compliance note) with the next step and time limit. Tick cases off (kept for this visit only: a dry run) and open any case |
| **Applications** | Every application with why it stalled, fixable, recoverable, language and channel. Click a row to see the case in four numbered boxes: why it stalled, the fix in simple words (merchant's language and English), the decision, and the drafted message (Day 0, 3, 7; WhatsApp bubble or email with subject) |
| **Product team** | Fixable causes ranked by merchants or by payments, with the proposed product change for each |
| **Safety and tests** | All app checks, message checks, the 30-case labelling result with its limits, a hard case (A3051), and a box to test any message against the safety checker |
| **More** | How it works, follow-up plan, the written answers with live numbers, simulated outbox, message library, and a "try a case" form |

A short guide with the mapping from the brief to the app is in [`docs/APP_GUIDE.md`](docs/APP_GUIDE.md). The full product document is in [`docs/Razorpay_P3_PRD.pdf`](docs/Razorpay_P3_PRD.pdf).

## Safety rules (built in, tested)

- **No workaround is ever suggested for a restricted business.** The merchant gets a polite closure, after a person approves.
- **No compliance or screening reason is ever shown to a merchant.** Compliance cases get a neutral holding note only.
- Reviewer text that signals a restriction or screening **beats a fixable code**, even if the code looks fixable.
- Messages are built **only from approved pieces**. AI never writes text to a merchant.
- A checker blocks promises, dates, banned words in six languages, wrong script, missing HELP or STOP lines, and WhatsApp without opt-in.
- AI is used for one narrow job: a second opinion on the 4 applications with a blank rejection code. Its answers are saved, so every run is identical.

## Message format

Every nudge follows one pattern: greeting, thank-you opener (changes with how long the merchant has been idle), steps-left line, "We noticed" problem in bold, fix as bullets, why it matters, resume link, HELP line, then a STOP line (WhatsApp) or a sign-off (email). WhatsApp messages stay under 1,000 characters. Emails carry a subject line for Day 0, Day 3 and Day 7. Tamil, Kannada and Marathi wording was reviewed and approved by native speakers. All pieces are in [`docs/Message_Library.csv`](docs/Message_Library.csv).

Follow-ups go on Day 3 and Day 7. The sequence stops when the merchant replies, finishes, opts out, or after three messages. Merchants idle 31 days or more get one gentle message only.

## Files

| File | What it is |
| --- | --- |
| `app.py` | The app (Streamlit) |
| `agent.py` | The agent. All decisions happen here |
| `rules.py` | Diagnosis keywords and the safety checker |
| `messages.py` | The approved message library in six languages |
| `ai_second_opinion.json` | Saved AI answers for the 4 blank-code notes |
| `onboarding_data.xlsx` | Sample applications and the rejection catalog (synthetic) |
| `test_agent.py` | The 20 checks |
| `findings.py` | Key findings shared by the Summary screen and the Excel download |
| `actions.py` | Builds the Action queue (who acts, next step, time limit) |
| `make_output.py` | Builds the Excel output (Key findings charts, Action queue, Summary, one row per application) |
| `export_message_library.py` | Builds the message library CSV |
| `output/Razorpay_P3_Output.xlsx` | The output table: one row per application |
| `docs/` | Product document (PDF and Word), app guide, message library |
| `.streamlit/config.toml` | Keeps the app in light mode |
| `requirements.txt` | Python packages |

## Run it

- **Online:** open the live app link above.
- **On a computer with Python:** `pip install -r requirements.txt`, then `streamlit run app.py`.
- **Tests:** `python test_agent.py` (expect "20 of 20 checks passed").
- **Output table:** `python make_output.py`.
- **Live data:** keep the same column names in `onboarding_data.xlsx` and replace the rows.

## Limits and assumptions

- No outcome data, so no recovery rate is claimed. Payments at stake is an estimate, not money recovered.
- The step order (Business details, KYC docs, Bank verification, Website/App review) is assumed.
- The Compliance holding-note wording still needs Compliance sign-off before any live use.
- Accuracy check: 30 cases labelled by the builder. Cause matched 30 of 30 after 8 labels were corrected to the sheet rule (22 of 30 before), safety routes 8 of 8, routes not scored. It is a self-check, not an independent score. Labelling about 200 cases blind is the first step of the pilot.
- 21 rows show more idle days than the account's age. They are flagged, not changed.
- Data is synthetic. No real merchant or personal data is used.

