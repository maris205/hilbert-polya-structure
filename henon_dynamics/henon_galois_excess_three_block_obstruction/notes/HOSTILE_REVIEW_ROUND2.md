# Hostile review — round 2

Date: 2026-08-14
Input: round-1 revised manuscript and executable certificate
Decision: **PASS AFTER MINOR CORRECTIONS**

## Independent stress test

The revised manuscript now separates three logically different claims:
(i) an exact no-go for width at most three; (ii) finite width-four
interpolation on only five witnesses; and (iii) a necessary exponential
discrepancy condition for one-sided Hölder data.  I attempted to collapse
these distinctions, to relabel a nonphysical trace root as physical, and to
invalidate the exact inequality by changing the root order.  The attacks do
not survive the revised evidence.  The physical coordinate interval contains
one root; derivative Sturm counts and signs fix the symbolic word and the
strictly decreasing trace branch; all six trace roots are isolated; and the
positive nonphysical root `(390,391)` is necessarily included in the excess.
The finite interpolation proposition is also sound because a sufficiently
long cylinder separates one chosen point from the finite union of orbit
points.  The remaining general Hölder question is explicitly open, so it
cannot be used as a counterexample to what the paper actually claims.

## Findings

### CRITICAL

None.

### MAJOR

None.

### MINOR

| ID | Finding | Evidence anchor | Confidence | Disposition |
|---|---|---|---|---|
| R2-m1 | Two additional bare `qquad` strings remained in the coordinate displays. | text: revised §4 coordinate equations | 5/5, source/PDF comparison | Corrected all remaining occurrences and recompiled. |
| R2-m2 | The concluding open theorem should repeat the one-sided qualifier introduced in §6. | text: revised §8 “find higher-block relations” | 5/5, scope comparison | Changed to forward relations on the one-sided presentation. |

## Verification receipt

- Exact producer and independent checker: PASS.
- Physical-embedding certificate: independently matched.
- Incidence relations and width-four unimodular minor: independently matched.
- General two-sided Hölder realization: still OPEN, with no promotion.
- Route A/B status: unchanged and conservative.

No unresolved Critical or Major finding remains.
