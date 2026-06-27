# Daily Drift Trace Automation Prompt

Run one Daily Drift trace for this repository.

Follow the repository rules in `README.md` and the template in
`templates/trace.md`. Create exactly one new dated folder under
`days/YYYY-MM-DD-slug/` for today's date. The slug should be short, concrete,
and based on what the run actually became.

Start by checking whether a trace for today already exists under
`days/YYYY-MM-DD-*/`. If today's trace already exists, do nothing else: create
no duplicate, make no edits, perform no fixes, do not commit, do not push, and
do not send email. Just report that today's trace already exists.

If today's trace does not already exist, begin from zero. Do not start from
yesterday's topic, ending note, open question, style, source type, or medium.
Do not add an ending hook for a later run. Each run must stand alone as a fresh
act of attention.

Choose one strong encounter or experiment for today. Prefer public encounters:
web pages, essays, docs, papers, repos, archives, manuals, images, datasets,
maps, standards, legal texts, source code, bug reports, protocols, public
tools, or other public materials. A day may instead be explicitly
local-material, silence-based, or self-contained, but only when that choice is
the point of the trace. Cite public sources with links or bibliographic notes.

Produce a clear, deliberate `trace.md` with these sections:

- Frame
- Encounter
- Work
- Result
- Made

`Frame` states the object, claim, behavior, or tension and why it matters now.
`Encounter` gives the source or material. `Work` shows what was actually done:
tested, built, coded, mapped, calculated, compared, annotated, diagrammed,
measured, translated, reconstructed, broken, repaired, or made visible.
`Result` gives the strongest clear finding, including uncertainty or limits
when they matter. `Made` links to files created today.

Before writing, define the reader-facing frame in plain language:

- What is the object, claim, or behavior?
- Why is it worth a serious trace today?
- Who or what is affected by the distinction?
- Where did the public encounter happen?
- What did the trace do that a summary would not do?

Write for a general curious audience, not only for computer-science readers.
The minimum target reader is about 17 years old, but the piece should still
reward readers from high school through university, professional, and research
levels. Explain specialist terms through concrete examples. Do not over-explain
common ideas, do not dumb the material down, and do not assume the reader
already belongs to the field.

Prefer a sharp public reading path over a private notebook shape. Open with the
reason the trace exists, give the concrete example early, and make the central
distinction impossible to miss. The trace should be deep, bold, strong, and
very clear. It may be prose, code, diagram, data, screenshot, quote commentary,
interactive artifact, failed attempt, odd format, or any mix that serves the
day. Do not make a code artifact by default. Do not make an essay by default.
Choose the medium because it makes today's point clearer.

Avoid attractors:

- Do not continue from the previous day unless the encounter itself demands it.
- Do not mention yesterday merely as a ritual opening.
- Do not end with a next step, future-work note, or note for another day.
- Do not repeat a medium, tone, or source type because it worked recently.
- Do not let the repository template become a substitute for judgment.
- Do not preserve uncertainty as vagueness; state what is known, what is not
  known, and why the difference matters.

Optional files are allowed when they serve the day: code, notes, diagrams,
screenshots, data, quotes-with-commentary, sketches, failed attempts,
experiments, or odd formats. If an artifact exists, the trace must explain why
it exists and how to read or run it.

After creating the day packet:

- Update `journal.md` in reverse chronological order.
- Update `README.md` Latest Trace to point to the new trace.
- Verify local Markdown links resolve.
- If any HTML or code artifact was created, run the smallest reasonable syntax
  or smoke check.
- Commit the changes with message: `Add daily drift trace for YYYY-MM-DD`.
- Push to `origin main`.
- Send the email notification from the official main local checkout:
  `/Users/carlo/Documents/varie/hacks/scratch/llm/free_llm`.
  Run `python3 scripts/notify_daily_trace.py` there after ensuring that checkout
  contains the pushed trace. The script reads ignored local files `.env` and
  `recipients.json`, which live in that official checkout rather than in the
  Codex worktree. It sends one separate email per recipient, with that
  recipient in `To`. The email body should contain one reading-start link:
  prefer a single Markdown artifact if one exists, otherwise link directly to
  `trace.md`, and only fall back to the day folder when no Markdown reading
  start exists. If sending fails, report the failure clearly and do not retry
  blindly.

Do not backfill missed days.

Keep the same conversation to avoid polluting the workspace with many threads,
and change the automation only once in a while.
