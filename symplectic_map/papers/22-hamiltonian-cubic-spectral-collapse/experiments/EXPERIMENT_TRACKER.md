# Paper 22 — Analytic Verification Tracker

## Current state

| Field | Value |
|---|---|
| Lifecycle stage | source design only |
| Scientific runs | 0 |
| Numerical orbits | 0 |
| Symbolic or CAS runs | 0 |
| Network actions by source-design author | 0 |
| Datasets | none |
| Figures | none |
| Manuscript or bibliography | none |
| Build or PDF artifacts | none |
| Source lock or publication lock | none |
| External uploads or messages | none |
| Independent source-design review | pending |

No author-side entry below is a PASS. All proof checks remain planned for a
fresh reviewer.

## Verification ledger

| ID | Exact check | Expected evidence | Status |
|---|---|---|---|
| A01 | gradients, inverses, and symplectic blocks | literal derivative and pullback calculation | planned |
| A02 | complete gradient support inventory | $2r$ rows and exactly two competitive rows | planned |
| A03 | exact $A$, $B$, and $C=BA$ | row-by-row derivation from monomials | planned |
| A04 | normalized variables | $\sigma=\sum_{i=2}^r u_i/u_1$, excluding $x_1$ | planned |
| A05 | first selector | $h-1-2\sigma>0$ | planned |
| A06 | second selector | both coefficient cases, strict at $h=2m+4$ | planned |
| A07 | seed and all cone walls | lower faces, upper height, least $m,h$ | planned |
| A08 | carried $p$-coordinates | $Au_n>Au_{n-1}$ after the base phase | planned |
| A09 | carried $q$-coordinates | $(C-I)u_n>0$ | planned |
| A10 | leading-form survival | polynomial-domain induction | planned |
| A11 | four-coefficient corollary | only $\alpha\beta\gamma\delta\ne0$ on fixed supports | planned |
| A12 | last-coordinate visibility | strict for $n\ge1$, tie disclosed for $n=0$ | planned |
| A13 | exact degree and Perron limit | $d_n=e_r^{\mathsf T}C^n\mathbf1$ and PF visibility | planned |
| A14 | invariant decomposition | $K^r=U\oplus E$, $\dim U=r-3$ | planned |
| A15 | quotient and cubic | exact $3\times3$ matrix, $P_{m,h}$, $P(1)$ | planned |
| A16 | exact unit multiplicity | no quotient eigenvalue $1$ | planned |
| A17 | sharp boundary | seed/selected-face tie at $g=2r$ only | planned |
| A18 | Paper 21 specialization | predecessor consistency at $m=1$ only | planned |
| A19 | citation and collision wording | primary metadata/context only | planned |
| A20 | anti-claims and permissions | no classification, priority, or external effect | planned |

## Failure actions

| Failure class | Required response |
|---|---|
| A selector ties in the stated open cone | stop; repair or narrow the theorem |
| A cone wall lacks a strict output inequality | stop; do not substitute samples |
| A carried term can meet the selected degree | stop; recurrence is not exact |
| A leading form may vanish after an allowed specialization | stop; narrow the coefficient corollary |
| $e_r$ fails to dominate one coordinate at $n\ge1$ | stop; degree formula not established |
| Quotient convention or cubic coefficient differs | stop; recompute from $A$ and $B$ |
| $P(1)=0$ for an allowed parameter | stop; exact multiplicity claim fails |
| Paper 20/21 overlap is hidden | stop; restore successor disclosure |
| An empirical or external action is proposed | stop; seek new authority |

The tracker has no runtime, hardware, random-seed, or dataset columns because
the headline theorem is entirely analytic.
