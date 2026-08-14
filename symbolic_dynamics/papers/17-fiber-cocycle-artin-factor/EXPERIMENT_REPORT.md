# Paper 17 Authority Exact Experiment Report — SD-C19

**Outcome:** The prototype certifies the first lawful same-object finite-fiber
Artin factor in this Session and simultaneously certifies why it does not
advance RH selectivity.  Every formal identity passes, genuine recurrent fiber
motion exists, and the one-letter clean branch collapses to universal cyclic
factor count.

## Raw data table

| Block | Frozen scale | Exact outcome |
|---|---:|---:|
| Formal `C2` determinants | `n=1,...,10` | 0 mismatch terms across `D_plus`, `D_minus`, `D_reg`, and same-object product |
| Trace/repetition coefficients | 300 | 300 exact |
| `C2` fiber graphs | 10 | 10 transitive; `n=1` period two; 9/9 with `n>=2` mixing |
| `C_m` character certificates | 350 | 350 exact |
| Regular local determinants | 7 | 7 exact: `det(I-xL_a)=1-x^m` |
| Primitive/lift census | 350 | all frozen Paper17 pilot counts reproduced |
| Natural cardinality tables | 72,079 across 35 cells | exactly 35 operator-coefficient-clean rules—one power rule per cell |
| Vertex coboundary controls | 63 | 63 have zero tested periodic holonomy and zero gauge mismatch |
| Noncoboundary negative controls | 21 | 21 have periodic witnesses |
| Transition controls | 4 | one gauge-exact; three noncoboundary with determinant leakage |
| Inventory controls | 64 | 64 reproduce all four identities; identity pass-rate margin `0` |
| Post-result unit tests | 14 | 14 pass |

The raw files are in `results/`; `results/analysis_summary.json` contains the
machine-readable aggregate.

## Finding 1 — same-object Artin factor is exact

**Observation.** For every `n<=10`, exact sparse-polynomial comparison gives

```text
D_plus  = product_i(1-x_i),
D_minus = product_i(1+x_i),
D_reg   = D_plus D_minus = product_i(1-x_i^2)
```

with zero mismatching coefficients.  All 300 trace/repetition coefficients and
all 350 `C_m` coefficient/phase rows also match.

**Interpretation.** The parity cocycle is a genuine recurrent skew extension,
not a relabeling of distinct roofs.  Character blocks and the regular
determinant arise from one transfer and use one normalization.

**Implication.** Freeze
`GO_GENUINE_COMMUTING_FIBER / GO_SAME_OBJECT_ARTIN_FACTORIZATION /
GO_ATOM_LOCAL_CHARACTER_FACTORS_AT_Z_EQ_1`.

**Next step.** In the paper, always call `D_reg` the whole-extension determinant
and `D_plus,D_minus` its isotypic block determinants.  Dynamical Artin
`L`-factors, if mentioned, are their inverses.

## Finding 2 — the fiber moves, but the primitive arithmetic clock fails

**Observation.** The `C2` graph is transitive at every nonempty finite cutoff;
it is mixing for `n>=2` and period two for `n=1`.  Nevertheless every one of
the 40 `C2` census rows with `n>=2` has mixed base primitives that close after
one traversal.  At the largest row `n=5,r=10,m=2`, the exact census contains

```text
81,962,825,835,072 primitive base necklaces,
40,981,411,486,080 mixed immediate closures,
122,944,237,321,152 primitive lifted cycles.
```

**Interpretation.** The clean determinant results from signed aggregation; it
does not delete mixed primitives.  A prime singleton has `c=1` and needs two
base traversals in the primary extension, while an even-cardinality mixed edge
can close immediately.

**Implication.** `A1_WEAK` and `STOP_PRIMITIVE_LIFT` are forced.  “No mixed
local Euler factor” must not be rewritten as “no mixed coefficient” or “no
mixed primitive lift.”

**Next step.** Report base primitive, immediate-closure, and lifted-cycle counts
separately; never present the character product as a prime-orbit bijection.

## Finding 3 — natural one-letter cleanliness is uniquely cyclic

**Observation.** The suite exhausts 72,079 inclusion-compatible cardinality
tables across 35 `(maximum degree, group order)` cells.  Exactly one table per
cell is clean in the full regular representation:

```text
r_k=k mod m.
```

Some nonfaithful selected characters hide wrong tables, exactly as predicted,
but no wrong table survives the regular audit.

**Interpretation.** Relabeling naturality plus operator-coherent atom locality
forces degree-power holonomy.  The image is cyclic, and a transitive full fiber
therefore cannot supply a one-letter nonabelian escape.

**Implication.** Freeze `STOP_FUNCTORIAL_NONABELIAN`.  This is a scoped theorem
for one-letter rules, not a no-go for transition cocycles.

**Next step.** Do not expand the one-letter group search.  The next legal test is
transition incidence holonomy.

## Finding 4 — coboundaries behave correctly; transition powers are dangerous

The exact two-atom transition comparison is:

| Control | Coboundary? | Nearest atom-local block | First leak | Periodic witness |
|---|---|---|---|---|
| degree vertex coboundary | yes | `D_plus` | none | none |
| diagonal return | no | `D_minus` | `-2xy` | singleton loop |
| incidence-intersection parity | no | `D_minus` | `2xy^2` (tie with `2x^2y`) | singleton loop |
| strict symbol change | no | `D_plus` | `-4x^2y^2` | three-symbol cycle |

**Observation.** All 63 vertex-coboundary controls have zero periodic holonomy
through length six and exact gauge agreement.  Every negative control has a
periodic witness.  Strict symbol change passes the squarefree two-atom ledger
but leaks at temporal repetition multidegree `(2,2)`.

**Interpretation.** Transition dependence is a real boundary of Paper 17's
theorem.  It can hide leakage from a squarefree-only audit.

**Implication.** Paper 18 must test `p^2q^2` temporal powers at the same time as
its `p,q,r` merge-order commutator.

**Next step.** Use only incidence-derived transition labels; do not import a
prime-indexed table.

## Finding 5 — exact controls prove too much

| Inventory | Seeds | All identities exact | Failures | Identity pass-rate margin |
|---|---:|---:|---:|---:|
| prime | 16 | 16 | 0 | 0 |
| composite | 16 | 16 | 0 | 0 |
| shuffled prime | 16 | 16 | 0 | 0 |
| random rational | 16 | 16 | 0 | 0 |

The stronger free-commutative calculation already proves why these controls
must tie in identity pass rate.  Their numerical determinant values generally
differ because their inventory values differ; that numerical equality is not
claimed.

**Interpretation.** After variables are supplied, the mechanism does not see
primality, entropy order, or unique factorization.

**Implication.** Freeze
`STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH`.  Additional one-letter
inventory sweeps cannot restore a nonzero margin.

**Next step.** Arithmetic promotion requires a new transition invariant or a
later-session carrier; it cannot come from retuning this cocycle.

## GO/STOP registry

```text
GO_GENUINE_COMMUTING_FIBER
GO_GENUINE_ARTIN_FACTOR
GO_SAME_OBJECT_ARTIN_FACTORIZATION
GO_TRIVIAL_EULER_FACTOR
GO_NONTRIVIAL_RECURRENT_CHARACTER
GO_ATOM_LOCAL_CHARACTER_FACTORS_AT_Z_EQ_1

STOP_FUNCTORIAL_NONABELIAN
STOP_PRIMITIVE_LIFT
STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH
```

## Route result

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

`A2` credits an exact analytic finite-fiber determinant in `Re(s)>1`; it is not
a target-zero or full-divisor match.  `A3` is only partial because continuation
is imported from the arithmetic identity and no completed functional equation,
Gamma factor, Weil compression, or intrinsic Fredholm continuation is derived.

## Paper 18 obligation

Move to a transition cocycle derived solely from subset-incidence data.  On the
`p,q,r` refinement grammar, compare two merge orders and their commutator
holonomy while simultaneously checking squarefree degree four and temporal
power four, especially `p^2q^2`.  Either produce a nonabelian clean factor or
prove that no leakage forces `degree count + vertex coboundary`.

This remains entirely inside Symbolic Dynamics.  Any geometric or quantum
carrier is only a `ROUND2_CLUE` and is not part of this prototype.

## Authority reproducibility and provenance

- Authority artifact base: `papers/17-fiber-cocycle-artin-factor/`.
- Scientific outputs are exactly equal to the frozen prototype after CSV
  newline normalization; the authority copy intentionally converts CSV to LF.
  Authority-only test/integrity/SHA files are excluded from that comparison.
- JSON parsing, CSV LF endings, cache cleanliness, 14 tests, and SHA verification
  are mandatory gates.
- Results omit timestamps and elapsed-time values so a consecutive double run
  has an identical result-ledger hash.
- `source_commit` and `code_commit` remain placeholders in the Route-A YAML
  until the first provenance commit; the evaluation metadata is sealed in a
  second-stage commit.
