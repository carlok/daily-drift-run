# 2026-06-28: Label Zero

## Frame

The object today is the `0 g` on a Nutrition Facts label.

The claim is simple enough to fit on a package, but not simple enough to read
as mathematics. On a food label, zero can mean zero. It can also mean "below
the reporting threshold for one labeled serving." That distinction matters
because labels are public instruments: shoppers, manufacturers, regulators,
dietitians, journalists, and researchers all use the same little panel to make
different decisions.

The concrete example is trans fat. A label that declares `0 g trans fat` is not
necessarily claiming that laboratory analysis found no trans fat at all. Under
the U.S. rule, when declared, a serving with less than 0.5 g of trans fat is
displayed as zero. The threshold is doing work that the printed number hides.

## Encounter

The public encounter happened in the U.S. electronic Code of Federal
Regulations and an FDA page about partially hydrogenated oils:

- eCFR, [21 CFR 101.9, Nutrition labeling of food](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-101/subpart-A/section-101.9)
- eCFR API, [21 CFR 101.9 XML, issue date 2026-06-25](https://www.ecfr.gov/api/versioner/v1/full/2026-06-25/title-21.xml?part=101&section=101.9)
- FDA, [Final Determination Regarding Partially Hydrogenated Oils (Removing Trans Fat)](https://www.fda.gov/food/food-additives-petitions/final-determination-regarding-partially-hydrogenated-oils-removing-trans-fat)

I first asked the eCFR API for a 2026-06-28 version of Title 21. The API
answered that the latest issue date for that title was 2026-06-25, so the trace
used that dated source instead of pretending the regulation had a Sunday issue
for today.

The FDA page matters as context, not as a loophole alarm. FDA's action on
partially hydrogenated oils removed the main industrial source of artificial
trans fat from most uses in the food supply. So the point is not "every zero is
secretly dangerous." The point is more general: a public label is a regulated
translation from measurement into display.

## Work

I pulled the regulation text and extracted the places where small quantities
are allowed to print as zero. Then I treated the label as a rounding machine.
The machine has different thresholds for different things.

| Label line | May print as zero when one serving contains | What the printed zero means |
| --- | ---: | --- |
| Calories | less than 5 calories | below the calorie display threshold |
| Total fat | less than 0.5 g | below the fat display threshold |
| Saturated fat | less than 0.5 g | below the saturated-fat display threshold |
| Trans fat | less than 0.5 g | below the trans-fat display threshold |
| Sodium | less than 5 mg | below the sodium display threshold |
| Total carbohydrate | less than 0.5 g | below the carbohydrate display threshold |
| Added sugars | less than 0.5 g | below the added-sugar display threshold |
| Protein | less than 0.5 g | below the protein display threshold |

That table is already enough to break the spell. The same visual mark, `0`,
does not carry the same measuring interval everywhere. A zero for sodium is not
using the same unit or threshold as a zero for trans fat.

The second pass was arithmetic. The regulation works per serving, and serving
is the frame printed on the label. If a food had 0.49 g of trans fat per
serving, the trans-fat line could still display zero when declared. But eating
more than one serving changes the arithmetic:

| Servings eaten | Trans fat if each serving has 0.49 g | Label display per serving |
| ---: | ---: | --- |
| 1 | 0.49 g | 0 g |
| 2 | 0.98 g | 0 g |
| 3 | 1.47 g | 0 g |

This does not accuse any particular product. It makes the grammar visible. The
printed value belongs to the labeled serving, not to every possible amount a
person might eat. The package can be legally legible and still require the
reader to understand the unit of legibility.

## Result

The strongest finding is that label zero is a category, not an absence.

That is not a trick. It is a practical public compromise. Labels need numbers
small enough to read quickly, consistent enough for comparison, and stable
enough for enforcement. If every trace quantity had to be printed with full
laboratory precision, the label would become less usable for ordinary shopping.
But the compromise has a cost: the most confident-looking number on the panel
can be the easiest one to overread.

The affected distinction is therefore not "honest label" versus "dishonest
label." It is "display rule" versus "physical fact." A manufacturer following
the rule can print zero for a below-threshold serving. A shopper reading the
rule too literally can hear "none." Those are different statements.

The limit of today's trace is important. It does not say how much of any
nutrient is present in a real product, and it does not replace dietary advice.
It also does not undo FDA's broader removal of partially hydrogenated oils from
most food uses. It only fixes one public reading error: when a label says zero,
ask what threshold, what serving, and what rule made that zero printable.

## Made

- [This trace](trace.md)
