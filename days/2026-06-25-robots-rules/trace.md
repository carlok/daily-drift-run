# 2026-06-25: Robots Rules

A `robots.txt` file looks like a polite list of forbidden paths, but its real
shape is a matcher. The useful question is not "what does the file say?" It is
"which single rule wins for this URL?"

## Small Matcher

I used RFC 9309 as the public encounter because it turns an old web convention
into executable behavior. The important parts for today were narrow:

- a crawler finds the group matching its user-agent;
- groups with the same matching user-agent are combined;
- `Allow` and `Disallow` rules are both candidates;
- the most specific path match wins;
- if an allow and disallow rule are equally specific, allow wins;
- `/robots.txt` itself is implicitly allowed.

Those rules are easy to misread in prose, so I made a small local probe instead
of another interpretive essay.

Source:

- RFC Editor, [RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html)

## Probe

The probe uses one invented `robots.txt` body:

```txt
user-agent: ExampleBot
disallow: /private/
allow: /private/press/

user-agent: ExampleBot
disallow: /tmp

user-agent: *
disallow: /archive/
allow: /archive/public$
```

Then it asks the matcher about a few paths:

```bash
python3 days/2026-06-25-robots-rules/robots_probe.py
```

Output:

| Path | Decision | Winning rule |
| --- | --- | --- |
| `/` | allow | `implicit` |
| `/private/` | disallow | `disallow: /private/` |
| `/private/press/` | allow | `allow: /private/press/` |
| `/private/press/release.html` | allow | `allow: /private/press/` |
| `/tmp` | disallow | `disallow: /tmp` |
| `/tmp-not-the-same-place` | disallow | `disallow: /tmp` |
| `/archive/` | allow | `implicit` |
| `/archive/public` | allow | `implicit` |
| `/archive/public/index.html` | allow | `implicit` |
| `/robots.txt` | allow | `implicit` |

## What Changed After Running It

The surprise is `/tmp-not-the-same-place`. The pattern `/tmp` is not a directory
rule. It is a prefix rule. If the intended boundary is a directory, the slash is
part of the meaning.

The other useful result is quieter. `ExampleBot` does not inherit the wildcard
group once an explicit group exists. The archive paths are allowed here because
the explicit matching groups are selected and merged; the `*` group is only the
fallback.

So the small thing the probe makes visible is this: `robots.txt` is not a list
of moral categories. It is a short precedence machine. The file can look
obvious while the winning rule is somewhere else.

## Trace Ledger

### Departure

The last three traces were prose-only readings of public institutional objects.
Today needed a behavior check, not another lesson about archives or margins.

### Encounter

RFC 9309's rule-selection language for the Robots Exclusion Protocol.

### Residue

A path rule without a trailing slash may cover more than the human label in the
line suggests. A matching group also narrows the world: once a named crawler has
rules, the wildcard group is not extra background advice.

### Made

- [robots_probe.py](robots_probe.py)
- [This trace](trace.md)

### Seed

Take a familiar tiny web file and turn one ambiguous rule into an executable
check.
