# P46 canonical State-A results ledger

This writer-side ledger was mechanically regenerated from the protected
canonical State-A snapshot. It reports implementation replay separately
from analytic proof and does not claim external priority.

## Bound input

- Result-ledger SHA-256: `fa22dde6ec3a9cbd473528ebb619863ac7beb0d1c9cc807394541501153add37`
- Science projection SHA-256: `8f03cf68855e1614b368d8f464349b4f96cc6ab1ac0faaddaa35c748e63080de`
- Provenance state: `A` (all commit fields remain pending; no paper manifest)

## Exact finite replay

| Surface | Canonical cases | Mismatches |
|---|---:|---:|
| complete support cutoffs | 4 | 0 |
| ordered dyadic label tuples | 335922 | 0 |
| exact rational finite traces | 36 | 0 |

Strict recursive type-and-value equality: `true`.
Finite evidence type: `FINITE_EXACT_DIAGNOSTIC`; infinite
status: `NOT_INFERRED_FROM_FINITE_EVIDENCE`.
Finite traces retain a scale-dependent odd cutoff and are never collapsed
to the infinite geometric factor.

## Analytic proof replay

The proof auditor replayed 8 frozen anchors,
reported 0 theorem failures, and recorded
finite-grid-as-proof as `false`.
Its certificate covers the strict `0`, `1/2`, and `1` walls, the exact
valuation direct sum, the odd/even cycle classification, and the separately
typed infinite trace identity.

## Independence and adversarial closeout

The evaluator source digests are distinct (`89a82d8c15162931333c448094ccafd4a2d7e8e134e01b5e4f0ad1c5a7259337`
and `d24f6354effadec12525c97f5a9a25f89ae861e5d11fee8f487119a3f14f66f1`), with no project-local
imports, shared expanded fixtures, or serialized intermediates.
All 62 mutations in 25 families were
rejected across 162 designated invocations;
survivors: `0`. The frozen external audit rejected all
13 physical clones across
22 invocations.

## Source and Route boundary

Fournier--Wagner novelty credit is `0`;
priority claimed is `false`; bounded-search
disposition is `SEARCH_BOUNDED_NO_EXACT_PACKAGE_HIT`.
The two Route validators passed 10/10 and
18/18 checks and agree on
`[A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC,
A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL]`.
Route B remains locked.

## Use in the manuscript

These results support statements about exact implementation agreement and
reproducibility. Infinite operator thresholds, determinant legality, and the
cycle theorem are established by the manuscript's proofs; this ledger is not
used to infer an endpoint, novelty, rational-prime emergence, or a target divisor.
