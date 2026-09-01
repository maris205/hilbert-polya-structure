# P150 primary-source verification

Status: `HOLD_EXTERNAL`. Sources are used only to delimit zero-credit
background. No source-search result is evidence of novelty or priority.

## Verified sources

| key | verified source | primary claim checked | use in P150 | relation |
|---|---|---|---|---|
| `HoneKouloukas2023` | A. N. W. Hone and T. E. Kouloukas, *Deformations of cluster mutations and invariant presymplectic forms*, Journal of Algebraic Combinatorics 57(3), 763--791 (2023); DOI [`10.1007/s10801-022-01203-5`](https://doi.org/10.1007/s10801-022-01203-5); author manuscript [`arXiv:2107.11866`](https://arxiv.org/abs/2107.11866). Published online 29 December 2022; version-of-record citation year 2023. | The Lyness five-cycle is the simplest type-`A_2` cluster example and deforms to the Lyness integrable family. | Subtracts the five-cycle and cluster interpretation. | **Direct for background; not the zero-totalized graph.** |
| `Hone2020` | A. N. W. Hone, *Efficient ECM Factorization in Parallel with the Lyness Map*, ISSAC 2020, 234--240; DOI [`10.1145/3373207.3404044`](https://doi.org/10.1145/3373207.3404044); [author accepted manuscript](https://kar.kent.ac.uk/81862/1/Hone_ISSAC_final.pdf). | Gives the rational Lyness map, the special period-five recurrence, its QRT/elliptic setting, and projective-coordinate denominator handling for arithmetic computation. | Subtracts the rational map, its five-period identity, QRT interpretation, and arithmetic/projective context. | **Direct for the rational core; not the `inv0` affine completion.** |
| `JogiaRobertsVivaldi2006` | D. Jogia, J. A. G. Roberts, and F. Vivaldi, *An algebraic geometric approach to integrable maps of the plane*, Journal of Physics A 39(5), 1133--1149; DOI [`10.1088/0305-4470/39/5/008`](https://doi.org/10.1088/0305-4470/39/5/008); [author-hosted manuscript](https://web.maths.unsw.edu.au/~jagr/IntegrabilityRS.pdf). | Develops the algebraic-geometric treatment of integrable birational plane maps over general fields and discusses finite-field periodic-orbit behavior. | Subtracts general finite-field birational/integrable dynamics. | **Nearest, not a same-map totalization owner.** |
| `Lyness1942` | R. C. Lyness, “1581. Cycles,” *The Mathematical Gazette* 26(268), 62 (1942), DOI [`10.2307/3606036`](https://doi.org/10.2307/3606036). | Historical source for the recurrence's cycle. | Subtracts the original cycle observation and priority. | **Historical direct background; no affine totalization.** |
| `Kanki2013` | M. Kanki, “Integrability of Discrete Equations Modulo a Prime,” *SIGMA* 9, 056 (2013), DOI [`10.3842/SIGMA.2013.056`](https://doi.org/10.3842/SIGMA.2013.056), [primary full text](https://www.emis.de/journals/SIGMA/2013/056/). | Treats finite-field division-by-zero and indeterminacy through extension of the initial-condition space and p-adic almost-good reduction. | Subtracts the general singularity/finite-field extension problem. | **Adjacent convention, not `inv0(0)=0` affine totalization.** |

## Metadata verification

BibTeX metadata was fetched from the five publisher DOI endpoints using the
`application/x-bibtex` content type and checked against the author-hosted or
arXiv records. For Hone--Kouloukas, the online-publication date is 29 December
2022 but the version of record is volume 57 (2023), so the bibliography uses
the citation year 2023. The bibliography contains only these five cited
entries.

## Direct-owner subtraction

P150 claims no credit for:

1. the recurrence `x_(n+2)x_n=x_(n+1)+1`;
2. the rational map `(x,y)->(y,(1+y)/x)`;
3. its period-five identity where all rational iterates are defined;
4. its type-`A_2`, associahedral, QRT, elliptic, or integrable interpretation;
5. general projective or finite-field rational-map techniques;
6. generic finite-map zeta bookkeeping.
7. Lyness's original cycle observation; and
8. finite-field singularity handling by projective/initial-space extension or
   almost-good reduction.

The only residual conjunction is the exact `inv0(0)=0` self-map on all of
`F_q^2`, together with its disjoint five-stratum decomposition, sharp tails,
complete cycle/zeta census, every-target fibres, image, and exceptional
in-tree.

## Replayable bounded search ledger

**Access date:** 2026-09-01 UTC.  Primary records were screened through
publisher DOI pages, arXiv/author manuscripts, SIGMA full text, and citation
trails.  Query families were:

```text
Lyness finite field functional graph
Lyness division by zero finite field
Lyness inverse-or-zero
Lyness zero-totalized OR totalized field
(x,y)->(y,(1+y)/x) singular affine completion
finite field rational map division by zero functional graph
Lyness singularity confinement almost good reduction
```

| candidate | classification and exclusion |
|---|---|
| Lyness 1942 | historical direct owner of the cycle observation; no finite-field all-affine map |
| Hone 2020 | direct rational Lyness/QRT arithmetic background; handles denominators projectively, not by `inv0` |
| Hone--Kouloukas 2023 | direct cluster/Lyness-family background; no totalized affine functional graph |
| Jogia--Roberts--Vivaldi 2006 | nearest general finite-field birational framework; no same boundary scheduler |
| Kanki 2013 | nearest division-by-zero convention; extends the state space or uses almost-good reduction rather than assigning `0^{-1}=0` |

The bounded search did not locate a direct owner of the residual conjunction.
It does not exhaust older, non-English, thesis, book, or differently
conjugated treatments. A later direct owner reopens the slot. No novelty,
priority, ownership, submission, or release conclusion follows.
