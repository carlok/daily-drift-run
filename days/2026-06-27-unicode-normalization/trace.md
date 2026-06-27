# 2026-06-27: Unicode Normalization

## Frame

The object today is a small trap in digital text: two strings can look the same
to a reader and still be different to a computer.

The concrete example is the letter `é`. It can be stored as one character,
`U+00E9 LATIN SMALL LETTER E WITH ACUTE`, or as two characters, `U+0065 LATIN
SMALL LETTER E` followed by `U+0301 COMBINING ACUTE ACCENT`. On the screen,
both forms usually look like the same letter. In memory, they are not the same
sequence.

That distinction matters because names, search boxes, filenames, database keys,
user handles, passwords, citations, and school records all pass through systems
that compare text. If the system compares only raw code points, two people can
type what looks like the same word and land in different places.

## Encounter

The public encounter was Unicode Standard Annex #15, "Unicode Normalization
Forms":

- Unicode Consortium, [Unicode Standard Annex #15: Unicode Normalization
  Forms](https://www.unicode.org/reports/tr15/)
- Unicode Consortium, [Unicode Character Database: NormalizationTest.txt](https://www.unicode.org/Public/UCD/latest/ucd/NormalizationTest.txt)

The annex defines normalization as a way to turn equivalent text into a chosen
regular form. The useful public promise is not that all visible differences
disappear. It is narrower and more important: when two strings are equivalent
in the Unicode sense, normalization gives software a stable way to compare
them.

There are two main families in the encounter:

- canonical normalization, where text keeps the same ordinary meaning but may
  be decomposed or recomposed;
- compatibility normalization, where Unicode may also fold special presentation
  forms into more ordinary forms.

The difference is not decorative. Canonical normalization can make the two
forms of `é` line up. Compatibility normalization can go further: `①` can
become `1`. That may be exactly right for search. It may be wrong for a
transcription, a legal identifier, or a mathematical symbol.

## Work

I used Python's Unicode database interface as a small measuring instrument, not
as the source of authority. The test asked three simple questions:

1. What code points are actually present?
2. Do the visually similar strings compare equal before normalization?
3. What changes under canonical and compatibility normalization?

The raw inspection:

| Text | Stored as | Length | UTF-8 bytes |
| --- | --- | ---: | ---: |
| `é` | `U+00E9` | 1 | 2 |
| `é` | `U+0065 U+0301` | 2 | 3 |
| `①` | `U+2460` | 1 | 3 |
| `1` | `U+0031` | 1 | 1 |
| `Å` | `U+212B` | 1 | 3 |
| `Å` | `U+00C5` | 1 | 2 |

The comparison result:

| Test | Result |
| --- | --- |
| raw `é == é` | `False` |
| NFC-normalized `é == é` | `True` |
| NFD-normalized `é == é` | `True` |
| NFC `①` | remains `U+2460` |
| NFKC `①` | becomes `U+0031` |

NFC means "Normalization Form C": it tries to use composed characters when
there is a canonical composed form. NFD means "Normalization Form D": it breaks
characters into canonical pieces. NFKC and NFKD are the compatibility versions:
they also handle characters that Unicode treats as compatibility variants, such
as circled numbers or some unit-like symbols.

So the trace did not merely summarize the annex. It put two look-alike strings
through a comparison and made the hidden boundary visible: one operation repairs
equivalent spelling of the same text, while another may erase meaningful
formatting or symbol distinctions.

## Result

The strongest finding is that "make text comparable" is not one action.

For ordinary accented words, canonical normalization is often the right first
question. It can make `é` and `é` meet without deciding that every decorative
or symbolic variant should collapse. For search, indexing, loose matching, or
input cleanup, compatibility normalization may be useful because users often
care about the ordinary value more than the presentation. But it is a stronger
move. It does not just tidy text; it can change which distinctions survive.

That is why the affected group is broad. A library catalog, a government form,
a login system, and a classroom spreadsheet may all need normalization, but not
for the same reason. A search engine wants generous matching. A passport office
or source-code parser may need stricter preservation. The important question is
not "is this text normalized?" It is "which distinctions is this system allowed
to forget?"

The limit of today's trace is also clear. Unicode normalization does not solve
all text confusion. It does not decide whether two names in different scripts
are the same person. It does not translate languages. It does not make security
risks disappear. It gives software a defined operation for one specific class
of sameness, and that definition is powerful precisely because it is limited.

## Made

- [This trace](trace.md)
