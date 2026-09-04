# P191 Review-A source, owner, and collision audit

## Bibliography and cite-key check

- Source cite keys and bibliography keys agree exactly:
  `Stanley2011EC1`, `BilleraThomasVanWilligenburg2006`,
  `HeubachMansour2009`, `BenderCanfield2005`,
  `Navarro2026OEISA398023`.
- The three citation sites in `main.tex` align with the five cited records:
  composition/cut-set background, coarsening language, locally restricted
  compositions, and the static OEIS neighbour.
- The manuscript does not cite any source as an owner of the literal dynamic
  cut-deletion rule.

## Nearest external neighbour

OEIS A398023 was reopened because its wording is the easiest confusion risk.
The distinction remains literal:

```text
A398023: index i divides the prefix sum s_i; static counting.
P191:    current part a_i divides prefix s_i; failing old cuts are deleted,
         parts change, and the rule iterates.
```

The OEIS entry does not state the iterative self-map, the sharp transient
theorem, or the one-step every-target inverse atlas proved here.

## Internal collision boundary

The reviewer reopened the manuscript's subtraction boundary against the nearest
internal Route-A neighbours:

- `P126`: same composition carrier, but it splits parts and adds cuts.
- `P147`: same coarsening direction, but it merges equal runs rather than
  testing incoming gaps against endpoints.
- `P181`: prefix-triggered, but acts on permutations with reversal and
  possible two-cycles.
- `P186`: subset/rank erosion on cut-set encodings, not composition-part
  divisibility.

The current owner search remains bounded.  This review confirms only that the
bounded non-hit is described conservatively; it does not upgrade the search
into novelty, priority, completeness, or freedom-to-operate evidence.
