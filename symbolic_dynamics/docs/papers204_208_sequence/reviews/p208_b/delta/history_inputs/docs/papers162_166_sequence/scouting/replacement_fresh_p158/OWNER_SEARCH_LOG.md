# Owner and internal-collision audit — MRC3

**Candidate:** ternary modular run consolidation (`MRC3`)  
**Audit date:** 2026-09-03 UTC  
**External status:** `HOLD_EXTERNAL`  
**Decision:** `KILL_INTERNAL_P147_SAME_RUN_CONSOLIDATION_ENGINE`

A bounded source search cannot establish novelty, priority, freedom to
operate, or an exhaustive negative result.  Here it only identifies material
that must receive zero contribution credit and tests whether a direct owner is
visible under plausible terminology.

## Literal and structural queries

The following query families were run with ordinary spelling variants and,
where useful, `paper`, `arXiv`, `DOI`, `2025`, and `2026`:

```text
"run-length" "modulo 3" word transformation runs sum
"replace each run" sum word dynamical system
"adjacent equal" merge modulo word dynamics
word runs coalescence sum modulo
"maximal constant runs" word map sum
"constant runs" "sum modulo" words combinatorics
"run contraction" words semigroup
"run-length encoding" iteration dynamics word
Smirnov words adjacent distinct letters generating function primary paper
Carlitz words adjacent unequal letters enumeration paper DOI
```

The search surfaced ordinary run-length encoding, repeated locally consistent
parsing, static Smirnov-word enumeration, run waiting times, and unrelated
coalescent/contraction uses.  It did not surface the literal self-map

```text
r^ell -> ell*r in Z/3Z
```

or its sharp-clock/every-target-fibre conjunction.  This is only a bounded
non-hit.  Search vocabulary may be incomplete, and an observation may be
embedded in semigroup, rewriting, compression, or recreational literature.

## Primary-source subtraction

| source checked | ownership boundary |
|---|---|
| B. Ellzey and M. L. Wachs, [*On enumerators of Smirnov words by descents and cyclic descents*](https://doi.org/10.4310/JOC.2020.v11.n3.a1), *Journal of Combinatorics* 11 (2020), 413–456; [primary preprint](https://arxiv.org/abs/1901.01591) | Directly owns Smirnov words—words with adjacent letters distinct—and refined static enumeration.  Hence the fixed-locus definition and its static counting context are zero credit.  It does not state the modular run-sum iteration. |
| H. Prodinger, [*Ternary Smirnov Words and Generating Functions*](https://www.finanz.math.tugraz.at/~prodinger/tichy-60.pdf), *Integers* 18 (2018), A69 | Directly treats the ternary fixed class and its generating functions.  The elementary count `3*2^(n-1)` is background, not a contribution. |
| H. S. Wilf, [*The Distribution of Run Lengths in Integer Compositions*](https://doi.org/10.37236/2019), *Electronic Journal of Combinatorics* 18(2) (2011), P23 | Owns maximal equal-run terminology and static run-length generating functions in compositions.  It does not provide this finite-group iterate, but maximal-run bookkeeping itself is zero credit. |
| A. Knopfmacher and H. Prodinger, [*On Carlitz Compositions*](https://doi.org/10.1006/eujc.1998.0216), *European Journal of Combinatorics* 19 (1998), 579–589 | Owns adjacent-unequal integer compositions and their generating functions.  It is a carrier/fixed-class neighbour, not a direct owner of MRC3. |
| D. Bevan and D. Threlfall, [*On the evolution of random integer compositions*](https://doi.org/10.37236/13010), *Electronic Journal of Combinatorics* 32(1) (2025), P1.21 | Studies a different random weak-composition growth process, including equal-run phenomena.  Random growth and its disappearance-of-equality results are zero credit and do not state MRC3. |
| B. Hopkins and A. Tangboonduangjit, [*Arndt and Carlitz Compositions*](https://doi.org/10.1016/j.tcs.2026.116156), *Theoretical Computer Science* 1082 (2026), 116156; [primary preprint](https://arxiv.org/abs/2512.12354) | Current static adjacent-restriction neighbour.  It owns no modular run-consolidation dynamics, but reinforces that fixed-class enumeration is not residual value. |

No inspected primary source is recorded as a direct literal owner.  That does
not produce a positive disposition because the internal gate below is
decisive.

## P1--P161 internal collision audit

| internal object | literal/proof overlap | conclusion |
|---|---|---|
| **P147, adjacent-run consolidation** | P147 factors a composition into maximal runs `s^ell` and replaces each by `ell*s`; MRC3 performs the identical schema in `Z/3Z`.  P147's every-target inverse chooses adjacent-distinct source run labels satisfying `ell*s=b`; MRC3 replaces divisibility by the congruence `ell*r=y mod 3`. | **Fatal.**  This is a coefficient-monoid deformation of a live map, not a new dynamical type. |
| P117, odd-run reversal on cyclic binary words | Both use maximal runs and torsion/parity-created boundary coalescence.  The literal updates differ, but all generic “run parity causes later coalescence” rhetoric is already occupied. | Supporting collision; not needed for the kill. |
| P121, adjacent product-plus-one coalescence | Both shrink ordered words by merging, but P121 is asynchronous/stochastic and uses a Yule-averaged transform. | Not literal; generic coalescence language is zero credit. |
| P126, composition refinement | Opposite direction and different decoder; relevant only as a carrier-neighbour already subtracted when P147 was frozen. | No new kill beyond P147. |
| P98, equal-block-sum torsion shifts | Uses finite-field block sums in a fixed-length subshift and studies invertible shift cycles.  MRC3 changes word length by run contraction. | Separated literal system; finite-field/torsion vocabulary alone is zero credit. |
| P90/P134/P138/P139 and current `CEF` | These occupy binary CA, border, palindrome, Lyndon, and equality-feedback word maps.  MRC3 is not any of those literal updates. | Separated from `CEF`, but word dynamics is already a crowded category. |
| P158 and current `RTI` | Random intersections/erosion on subsets, cuts, or rank statistics; MRC3 is deterministic and uses no intersection. | Clean categorical separation, but insufficient to override P147. |

The particularly close P147 comparison is exact at both theorem interfaces:

```text
P147 temporal: positive weight forces logarithmic ancestry growth.
MRC3 temporal: torsion permits cancellation; length rank gives N-1.

P147 inverse: adjacent-distinct path over divisors s of a target part b.
MRC3 inverse: adjacent-distinct path over r with ell*r=y in Z/3Z.
```

The changed clock is a genuine phenomenon, but after assigning the shared
maximal-run map and adjacent-label inverse construction zero credit, its proof
is one monotone-rank line and an alternating witness.  That residual is below
the required paper scale.

## Current P162 kill-ledger firewall

The selection was made only after excluding the active killed systems: `CPE`,
`EDP`, `DGD`, `RPS`, `AQN`, `USP`, `RFW`, `CNG`, the geometry/group empty pool,
the nonlinear-algebra pool, both stochastic replacement pools, the
matching/incidence pool, the arithmetic-hybrid and cross-class pools, and the
poset/language pool.  It does not revive their partition-lattice, LDU,
finite-linear, GCD/derivative, group-power, closure, random-intersection, or
feedback-register mechanisms.

An early cyclic-subgroup idea was discarded before selection because the
P97--P101 ledger already reserves `H -> pH` beside P100.  It is not counted as
the candidate in this lane.

## Claim subtraction and final owner gate

The following receive zero contribution credit:

1. run-length factorization and encoding;
2. Smirnov/Carlitz fixed words and all static enumeration;
3. generic termination by a strictly decreasing word length;
4. generic transfer-matrix/path enumeration; and
5. most decisively, the P147 update schema and adjacent-distinct inverse path.

What remains is the ternary torsion witness producing the linear sharp clock
and explicit three-state local weights.  It is a useful exact control, not a
separate paper contract.

```text
DIRECT_EXTERNAL_OWNER = NOT_FOUND_IN_BOUNDED_SEARCH
INTERNAL_OWNER = P147_EXACT_SCHEMA_AND_INVERSE_ENGINE
FINAL = KILL_INTERNAL_P147_SAME_RUN_CONSOLIDATION_ENGINE
EXTERNAL = HOLD_EXTERNAL
```
