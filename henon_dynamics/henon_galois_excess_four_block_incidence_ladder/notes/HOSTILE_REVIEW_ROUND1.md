# Hostile review — round 1

Date: 2026-08-14

Manuscript: HCS-P56 initial draft

Decision: **MAJOR REVISION, REPAIRABLE**

## Strongest counter-argument

The infinite incidence relation is elementary once the two word families are
known, but the paper uses the new period-six multiplier field in a
load-bearing exact inequality.  The initial draft stated that its reciprocal
quartic was irreducible after “direct factorization” without publishing a
reproducible irreducibility witness.  If that quartic split over
\(\mathbb Q\), the claimed Galois orbit and excess interpretation would have
the wrong field degree.  This does not attack the symbolic ladder, but it
does attack the algebraic bridge used by the four-block theorem.

A second scope risk is more conceptual.  The all-width relation supplies a
necessary sequence for a one-sided Hölder potential; it does not by itself
show that the sequence fails exponential decay, construct a potential, or
transfer automatically to an arbitrary two-sided representative.  The paper
must keep the finite width-four no-go separate from the open Hölder problem.

## Findings

### CRITICAL

None.  No exact counterexample to the incidence identity or strict
four-block inequality was found.

### MAJOR

| ID | Finding | Evidence anchor | Confidence | Required repair |
|---|---|---|---|---|
| R1-M1 | The degree-four multiplier polynomial was called irreducible without a finite certificate. | initial §4, multiplier-polynomial paragraph | 5/5, exact algebra audit | Publish a good-prime reduction and prove absence of degree-one and degree-two factors.  Mirror the computation in both executable paths. |
| R1-M2 | The regularity narrative could be read as promoting an infinite incidence family to a general Hölder no-go. | abstract, §7 and conclusion | 5/5, quantifier/scope audit | State the explicit one-sided necessary bound, retain the two-sided cohomology caveat, and mark the asymptotics of \(\Delta_m\) OPEN. |

### MINOR

| ID | Finding | Evidence anchor | Confidence | Required repair |
|---|---|---|---|---|
| R1-m1 | The period-one row was denoted \(A_1\), colliding with the family \(A_m\), which is defined only for \(m\geq3\). | initial §6 finite-sharpness rows | 5/5, notation audit | Rename the period-one row \(C_1=(0)\) in the manuscript and proof package. |
| R1-m2 | The independent implementation name appeared as raw prose rather than code typography. | initial §8 reproducibility paragraph | 5/5, PDF/source comparison | Typeset `Counter` with `\texttt{}`. |

## Adjudication and revision outcome

- `R1-M1`: validated.  The producer and independent checker now reduce the
  quartic modulo 13 to
  \(z^4+3z^3+6z^2+3z+1\) and verify that its gcd with both
  \(z^{13}-z\) and \(z^{169}-z\) has degree zero.  A reducible quartic must
  have a linear or quadratic factor, so irreducibility follows.
- `R1-M2`: validated and repaired throughout the abstract, §7, conclusion,
  README, certificate and evaluator records.  No unrestricted Hölder or
  arithmetic conclusion is promoted.
- `R1-m1`: repaired by using \(C_1\).
- `R1-m2`: repaired and visually checked in the PDF.

The finite-memory theorem survives unchanged; the revised manuscript gives
stronger evidence and a narrower, correct regularity claim.
