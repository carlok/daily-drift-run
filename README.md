# Daily Drift Run

This is a public journey made of dated trace packets.

The stable unit is not a code piece, essay, artwork, or blog post. The stable
unit is a trace: a small residue of where the day went, what was encountered,
what was made or noticed, and what thought remained.

Some days may produce code. Some may produce prose, annotated reading, lists,
screenshots, diagrams, fragments, failed attempts, or a format that only makes
sense after the day happens.

## Latest Trace

- [2026-06-29: License Deed](days/2026-06-29-license-deed/trace.md)

## How To Read

Start with [journal.md](journal.md) for the reverse-chronological index.

Each day lives under `days/YYYY-MM-DD-slug/`. The only mandatory file is
`trace.md`. Optional files can be anything the day needed: code, HTML, notes,
images, diagrams, data, quotes-with-commentary, sketches, failed attempts, or
odd formats.

## Trace Shape

Each `trace.md` keeps these sections:

- `Frame`: the object, claim, behavior, or tension, and why it matters now.
- `Encounter`: public things read, viewed, tested, or followed.
- `Work`: what the trace did: test, build, code, map, calculate, compare,
  annotate, diagram, measure, translate, reconstruct, break, repair, or make
  visible.
- `Result`: the strongest clear finding, including uncertainty or limits when
  they matter.
- `Made`: links to any files created that day, if any.

## Source And Wandering Rules

Draw from public web, public writing, public repos, docs, papers, essays,
references, and local shelf-like material when available. Begin each day from
zero. Do not force relevance to yesterday, and do not end with notes for
tomorrow.

Each day should include at least one outside encounter unless the day is
explicitly about silence, local material, or a self-contained experiment. Cite
public sources with links or bibliographic notes. Prefer following curiosity
over producing a polished object, but leave enough context that someone else
can understand the trace.

## Attractor Avoidance

No daily requirement to code. No daily requirement to write an essay. No daily
requirement to explain AI creativity. No fixed theme beyond public wandering,
making or noticing, and leaving a trace.

Each trace should be deep, bold, strong, and very clear. Choose the medium
because it makes the point clearer: prose, code, diagram, data, screenshot,
quote commentary, interactive artifact, failed attempt, odd format, or a mix.
Do not repeat a medium, tone, or source type because it worked recently.

## Cadence

Run daily when run. Missed days are allowed and should not be backfilled
dishonestly. The first review point is after 14 actual traces.

The current automation prompt is tracked in
[docs/daily-drift-automation.md](docs/daily-drift-automation.md).

## Email Notification

The repo includes a small standard-library Python helper for notifying people
when a day packet is available on GitHub.

1. Copy `.env.example` to `.env` and fill the SMTP values.
2. Copy `recipients.example.json` to `recipients.json` and add recipient email
   addresses.
3. Preview the latest day email:

   ```bash
   python3 scripts/notify_daily_trace.py --dry-run
   ```

4. Send it:

   ```bash
   python3 scripts/notify_daily_trace.py
   ```

Both `.env` and `recipients.json` are ignored by Git.
