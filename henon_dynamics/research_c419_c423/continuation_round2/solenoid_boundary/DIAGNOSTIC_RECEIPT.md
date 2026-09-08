# AS1-R2 bounded finite-semigroup result

2026-09-07. Status: WHOLE-CIRCLE CLAIM STILL NOT JUSTIFIED; NOT ADMITTED.

## Actual execution

The [frozen diagnostic](FROZEN_CONTRACT.md) preceded computation.
One execution of `python semigroup_probe.py` under Python 3.12.3 exited
zero. It used exact Python integers, exhaustive reachable-state closure,
strongly connected components (SCCs), and integer gcds of edge-depth
differences. There was no floating-point eigenvalue calculation, GPU
job, word-period cutoff extrapolation, or repetition of old C14 checks.
All six requested finite graphs completed, far below the 250,000-state
cap; the combined measured per-level time was about 0.0011 seconds.

The executed [program](semigroup_probe.py) has SHA256
`96a8ddbde573c95ad70f99e5a0fccab7ed9775e825da0733e74b274804660357`.
These are producer diagnostics, not independently certified outputs.

| Precision $2^k$ | Reachable states | Edges | All SCCs | Closed SCCs | Closed SCC period |
|---|---:|---:|---:|---:|---:|
| $k=1$ | 5 | 8 | 3 | 2 | both 1 |
| $k=2$ | 9 | 14 | 3 | 2 | both 2 |
| $k=3$ | 9 | 14 | 3 | 2 | both 2 |
| $k=4$ | 39 | 65 | 6 | 3 | all 2 |
| $k=5$ | 75 | 125 | 6 | 3 | all 2 |
| $k=6$ | 147 | 245 | 6 | 3 | all 2 |

Closed component sizes are respectively $(2,2)$, $(4,4)$, $(4,4)$,
$(12,12,12)$, $(24,24,24)$, and $(48,48,48)$.
Their trace-one state counts are $(2,1)$, $(2,1)$, $(2,1)$,
$(3,3,2)$, $(3,3,2)$, and $(3,3,2)$.
Each period-two component's accepted states occupy one depth-parity
class. The choice of root changes its displayed parity, not the invariant.

## What this finite result means

Let $S_k$ be the adjacency matrix of this reachable graph, with an edge
counted once per allowed letter. On states whose last letter is $A$ put
$v=1$, and on states whose last letter is $B$ put $v=\varphi$.
The admissible outgoing letters give
$S_kv=\varphi v$ away from the one transient initial state:
after $A$ there is only $B$, and after $B$ there are $A$ and $B$.

For a closed irreducible component the restricted positive vector is
therefore a Perron eigenvector of eigenvalue $\varphi$. For a nonclosed
irreducible component the restriction satisfies the corresponding
inequality, strict at a vertex with an exiting edge. Irreducibility
then makes its spectral radius strictly less than $\varphi$.
The peripheral phases of a closed irreducible nonnegative matrix are
its period roots of unity. Thus the verified graphs at levels two
through six have only the possible leading phases $+1,-1$; level one
has only $+1$.

The accepted-word count is an entry of a finite matrix resolvent. For
$n\ge\lceil k/3\rceil$, $\det M_w=8^n\equiv0\pmod {2^k}$, so the actual
fixed-layer condition is exactly $\operatorname{tr}M_w\equiv1\pmod {2^k}$.
The finite initial-length correction changes a polynomial only.
Consequently these six layers cannot themselves supply the dense
peripheral singularities required by the proposed closure route.
This is not a proof that deeper layers behave the same way.

## Whole-tower gap retained

No uniform period classification, uniform spectral gap, or nonzero
aggregate-residue density theorem has resulted from this diagnostic.
In particular, the apparent parity pattern is not extrapolated.
Near-peripheral poles at unbounded depth could still be relevant, but
one would have to establish an actual continuation domain and prove
that their contributions survive the full infinite weighted sum.

The already proved inside-disk radial tail bound is retained unchanged;
it does not imply convergence in an annulus beyond the circle.
Neither the established two-real-point obstruction nor this low-level
SCC table satisfies the full-circle contract. We stop the bounded
AS1-R2 attempt here, with no new admission or manuscript.

## Fresh source applicability

Six new search formulations covered noncommuting solenoid zeta,
congruence-semigroup natural boundaries, p-adic random-matrix spectral
gaps, recent switching-zeta boundaries (183-day filter), group-extended
transfer operators, and S-integer semigroup zeta. Unrelated or empty
results are not evidence of novelty. Crawl dates were not publication
dates. The following primary statements were actually inspected:

- [Bell--Miles--Ward, Theorem 15](https://arxiv.org/html/1307.2369v1#S3):
  the single-automorphism number-field product hypotheses remain
  unverified for this switching sequence, just as in the first pass.
- [Carvalho--Rodrigues--Varandas, Theorem B](https://arxiv.org/html/1601.04275v2):
  its averaged count and Ruelle-expanding-generator assumptions do not
  supply the missing all-depth spectral statement for this localized
  solenoid. Real matrix expansion is not an applicability proof.
- [Boyle--Schmieding, finite group extensions of shifts of finite type](https://arxiv.org/pdf/1503.02050):
  arXiv record and opening material inspected, not all 41 pages. Finite
  extension periodic-data invariants do not by themselves establish
  convergence or noncancellation for an infinite congruence tower.

The earlier [full source applicability audit](../../arithmetic_spectral/solenoid_review/SOURCE_APPLICABILITY.md)
is retained; no already-owned finite-state or radial-tail mechanism is
presented as new mathematical substance.
