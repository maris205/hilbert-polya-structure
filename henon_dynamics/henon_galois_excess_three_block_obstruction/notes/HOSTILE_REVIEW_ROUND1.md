# Hostile review — round 1

Date: 2026-08-14
Manuscript: HCS-P55 initial draft
Decision: **MAJOR REVISION, REPAIRABLE**

## Strongest counter-argument

The paper's exact three-block contradiction is attractive, but its broader
regularity narrative could overstate what the finite certificate proves.  A
relation among forward cyclic blocks controls forward locally constant
potentials.  It does not, without a cohomological reduction, justify the
same quantitative approximation argument for an arbitrary two-sided
Hölder potential using a vaguely defined “central word length.”  Separately,
the period-five resultant has six real trace roots, so identifying the root
in `(4445,4446)` as the physical embedding requires an exact branch argument,
not only endpoint values at the ends of the coordinate interval.  Without
monotonicity or an equivalent elimination certificate, an interior turning
point could in principle move the physical trace outside the asserted
interval.  These gaps do not refute the finite-memory theorem, but they leave
two load-bearing statements under-certified: the physical labeling used in
the Galois excess and the claimed all-period Hölder gate.  The narrow repair
is available: certify derivative root counts and coordinate signs on the
physical interval, and state the Hölder theorem on the one-sided H6
presentation whose forward cylinders are exactly measured by the incidence
vectors.

## Findings

### CRITICAL

None.  The symbolic incidence relation and the strict excess inequality are
repairable without changing the main theorem.

### MAJOR

| ID | Finding | Evidence anchor | Confidence | Required repair |
|---|---|---|---|---|
| R1-M1 | The physical period-five trace was assigned to the final trace interval without certifying that the reduced trace has no turning point on the isolated coordinate interval. | equation: initial §4, physical-root paragraph and Appendix A | 5/5, exact real-algebra audit | Add exact derivative Sturm counts, midpoint derivative signs, endpoint inequalities, and the symbolic sign word. |
| R1-M2 | The Hölder gate mixed a two-sided central-cylinder metric with forward block incidence. | equation: initial Theorem 6.1 and its proof | 5/5, symbolic-dynamics audit | Restrict the theorem to the one-sided H6 presentation, or supply an explicit future-dependent cohomological reduction. |

### MINOR

| ID | Finding | Evidence anchor | Confidence | Required repair |
|---|---|---|---|---|
| R1-m1 | The period-four coordinate display contained the literal text `,qquad`. | text: initial §4 “(a,b,-a,b),qquad” | 5/5, direct source inspection | Restore `\qquad`. |
| R1-m2 | The abstract and introduction did not identify the one-sided scope of the quantitative gate. | text: initial abstract “quantitative higher-block condition” | 4/5, scope audit | Mirror the one-sided qualifier and retain the unrestricted-Hölder firewall. |

## Adjudication and revision outcome

- `R1-M1`: validated and repaired in producer, independent checker, tests,
  §4 and Appendix A.
- `R1-M2`: validated and repaired by an explicit one-sided metric and a
  two-sided non-promotion sentence.
- `R1-m1`: repaired.
- `R1-m2`: repaired in the final abstract/introduction and project summary.

No finding was withdrawn merely because a repair was convenient.  The main
finite-memory theorem survives; the broader Hölder statement is deliberately
narrower and more precise.
