# Review summary

## Decision

- **Candidate:** `ROUTE_A_REJECTED`
- **Project:** `READY_AS_SCOPED_OBSTRUCTION`
- **Final adversarial score:** 52/60
- **Route B:** not authorized

## Review progression

The initial proposal correctly identified modular scattering as a noncompact
positive control but stated the denominator failure too narrowly and used
language that could be read as excluding all cusp-derived roofs.  Two
adversarial rounds required four substantive upgrades:

1. distinguish open double cosets from closed conjugacy classes;
2. replace a counterexample for `2 log c` by the arbitrary-`F`, fixed-scale
   zero theorem;
3. promote stable homogenization equal to Selberg length to a main theorem;
4. define the allowed zero-free normalization class and list all excluded
   extensions.

The final review found no mathematical blocker in the frozen
final-denominator-only scope.  It rated external novelty as limited and
Route-A value as high.  A promised independent checker was then implemented;
it reverified 910 rows at 110 digits without importing the producer and passed
7/7 tests, including tamper rejection.  The validation score rose from 8/10
to 10/10.

A separate manuscript audit found no critical issue and one major wording
ambiguity: “positive hyperbolic” had not specified whether positivity referred
to trace or entries. The released theorem now says explicitly that all four
matrix entries are strictly positive; the proof uses only that subfamily.
The same pass froze closed-orbit orientation, declared that the numerical
stable audit uses `alpha = 1`, documented the primitive/even-rotation word
census, and completed recent-paper identifiers.

## Strongest theorem

For every fixed `alpha > 0`, if

```text
F(alpha * |c(g^2)|) = 2 F(alpha * |c(g)|)
```

for every hyperbolic modular matrix whose four entries are strictly positive,
then `F` vanishes on `alpha * N_{>0}`. No regularity assumption is used.

## Claim boundary retained by review

The result does not exclude local denominator increments, cyclic sums,
coboundaries, trace/word/endpoint data, matrix cocycles, open groupoid traces,
multi-cusp scattering, or divisor-carrying compensators.  It does not claim
that the stable limit is the unique repair among all homogeneous class
functions.
