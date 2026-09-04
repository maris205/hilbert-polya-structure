# P192 Review-A source and owner-collision audit

**Audit date:** 2026-09-04 UTC  
**Decision:** required source revision accepted; no literal-map owner
established.  
**Gate:** `OWNER_RED_AMBER / HOLD_EXTERNAL`.

## Accepted bibliography verification

The six cited keys are exactly the six generated bibliography entries in the
accepted repair.

| Record | Checked metadata and scope | Result |
|---|---|---|
| Dénes, *The Representation of a Permutation as the Product of a Minimal Number of Transpositions, and Its Connection with the Theory of Graphs* | Hungarian Academy repository: volume 4(1), 63--71 (1959); minimal full-cycle factorization/Cayley count | PASS |
| Gorsky--Gorsky, *A braid group action on parking functions* | arXiv:1112.0381v2, revised 2013; direct braid action on parking functions | PASS |
| Stanley, *Parking Functions and Noncrossing Partitions* | *Electronic Journal of Combinatorics* 4(2), R20, conventional volume year 1997, DOI [10.37236/1335](https://doi.org/10.37236/1335) | PASS |
| Irving--Rattan, *Trees, Parking Functions and Factorizations of Full Cycles* | *European Journal of Combinatorics* 93 (2021), 103257, DOI [10.1016/j.ejc.2020.103257](https://doi.org/10.1016/j.ejc.2020.103257) | PASS |
| Stanley, *Enumerative Combinatorics*, Vol. 2, 2nd ed. | Cambridge University Press, 2023, DOI [10.1017/9781009262538](https://doi.org/10.1017/9781009262538); Pollak circular parking background | PASS |
| Campion Loth--Rattan, *Centrality of star and monotone factorisations* | *Bulletin of the London Mathematical Society* 57(11), 3567--3585 (2025), DOI [10.1112/blms.70170](https://doi.org/10.1112/blms.70170); deterministic conditional Hurwitz/string-reordering neighbour | PASS; zero contribution credit |

The corrected records support the classical carrier counts, correspondence,
and circular-parking argument.  They do not own P192's adaptive scheduler.

## Finding P192-A1: located deterministic neighbour — RESOLVED

The bounded search used combinations of `first/equal lower endpoint`,
`priority/greedy collision`, `conditional Hurwitz move`, `monotone
factorization`, `minimal long-cycle factorization`, `parking function`,
`scheduler`, `normal form`, and `inverse fibre`.

It located Jesse Campion Loth and Amarpreet Rattan,
[*Centrality of star and monotone factorisations*](https://doi.org/10.1112/blms.70170),
*Bulletin of the London Mathematical Society* 57(11), 3567--3585 (2025).
Their Theorem 7 constructs an order-changing bijection between monotone
factorization classes.  In Stage 1 it scans maximal contiguous strings and
conditionally applies Hurwitz moves; its Case 2 is triggered by adjacent
transpositions `(a,i_j),(a,i_(j+1))` with equal lower endpoint.

This overlap is mechanistic and must be cited, but it is not a demonstrated
literal collision.  The source uses a whole-string reversible bijection,
different left/right move terminology and orientation, and a changing
monotonicity order.  P192 fixes the product `c_n`, numeric endpoint order, and
one orientation, applies one move at the least current collision per epoch,
terminates, and derives target indegrees.  The located article does not state
that finite map or its four proved axes.

Disposition: P192-A1 is implemented and accepted; the external owner gate
remains red amber.  The bounded search still does not establish novelty,
priority, completeness, or freedom to operate.

## Internal P1--P191 subtraction

The live definitions and the historical kill records were reread at the level
of carrier, literal update, and proof engine.

| Prior system or scout | Shared surface | Literal/proof separation |
|---|---|---|
| P107--P191 direct Hurwitz-pair scouts | the named two-strand Hurwitz generator and product preservation | those are fixed braid generators/permutations with singleton fibres; P192 gives the generator zero credit and studies an adaptive terminating selector plus nonuniform atlas |
| P157 `HWT` | exactly the reduced full-cycle-factorization carrier and a left-to-right Hurwitz sweep | the sweep is a bijection/full-twist action with periodic orbits; P192 conditionally moves only the least equal-lower pair and has a strict rightward clock |
| P181 first-descent prefix reversal | least defect index on permutations, target fibres, maximum indegree `n-1` | P181 reverses one prefix, has a depth-two core with two-cycles, and its inverses are decreasing runs; P192 changes adjacent factors and only fixed recurrence remains |
| P105 cycle-minimum pruning | adaptive minimum selection, absorption, target-resolved fibres | P105 deletes/sutures arrows in functional cycles and changes rank; it has no factorization product or Hurwitz inverse test |
| parking-function canonicalization/outcome scouts | parking carrier, Pollak rotations, and labelled counts | P192 never updates a parking word by the parking algorithm; it imports the lower-endpoint bijection only for a fixed-state census |
| P194 within-batch crystal scheduler | least usable color and a monotone history statistic | P194 changes one word letter by a Kashiwara operator and uses weight/Schur fibres; no Hurwitz or factor-product proof transfers |

The history-set product resembles the occurrence set of a distinguished
Prüfer letter.  Equality of finite enumerators is not a scheduler-compatible
bijection, and this comparison cannot promote Conjecture 5.1.

## Binding disposition

The internal residual is still the conjunction of the strict least-collision
clock and target-resolved inverse Hurwitz atlas.  Direct Hurwitz actions,
minimal factorization counts, parking/tree correspondences, Pollak's proof,
Prüfer counts, and the Campion Loth--Rattan conditional-move mechanism all
receive zero contribution credit.  Status remains
`OWNER_RED_AMBER / HOLD_EXTERNAL` after repair.
