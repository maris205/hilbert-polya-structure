# Paper 37 exact integration preregistration — SD-C39

Date: 2026-08-15
Protocol: strict Route A v0.2; Route B locked
Status at freeze: preartifact / no Git mutation authorized

## Frozen authority and bridge

The integration may use only this Paper 37 authority tree and the three
explicit bridge inputs below. Their bytes are frozen before implementation.

- `/tmp/paper37_research_package.md`: `e39a8c89975670926461c46c9c82df58e886647e49fb77244fc530d3a060f3aa`
- `/tmp/paper37_source_lock.md`: `d725f03caffc6c5fab916314df25097b7383af7494287052496516deab0dcb4e`
- `/tmp/paper37_exact_prototype/`: source, evaluator, driver, preregistration,
  and plan are bridged by a hash-pinned research lock; the frozen canonical
  scientific result must remain
  `b17967f294da018e2e045ae70ac7731f5612f4bd4693115ea33dbaebb7fc0d6e`.

The writer-owned root `README.md`, `SOURCE_LOCK.md`, `PREREGISTRATION.md`,
`PROOF_PACKAGE.md`, `DERIVATION_PACKAGE.md`, `LITERATURE_AUDIT.md`,
`NARRATIVE_REPORT.md`, manuscript sources, PDF/build artifacts, any root
manifest, and Git state are read-only.

## Frozen scientific question and fixture

Audit the frozen rank-two even/odd shear fixture on the full unquotiented
cyclically nonbacktracking affine Cayley edge shift. Preserve one free marker
per original transition. Exact cancellation means equality of complete
determinant polynomials and all repetitions, never only a first trace.

The source owns presentations, words, bounded normal-closure products, and
the matrices

```text
A=[[1,1],[0,1]], B_plus(r)=[[1,0],[r,1]], B_minus(r)=[[1,0],[-r,1]].
```

The independent evaluator owns reduction, affine evaluation, matrix
arithmetic, factor comparison, controls, counts, and the Route decision. It
must not import the source module. Scientific arithmetic is exact over
integers and `fractions.Fraction`.

## Frozen finite census and expected bridge result

- affine rows `r=1,...,8`, with `r=4` the composite baseline;
- six fixed one-relator mutations;
- 48 deterministic random one-relator controls, seed `370037`;
- 24 paired random two-relator controls;
- bounded two-conjugate products, conjugator length at most three for affine
  rows and at most two for random controls;
- power supertraces through order 12;
- boundary controls for flat balanced parity, traceless invertible,
  nilpotent, and inverse-edge backtracks.

The expected prototype bridge is `131/131` exact checks, affine direct
cancellation `8/8`, affine mixed leaks `8/8`, random direct matches `9/48`
with mixed leaks `9/9`, paired all-direct matches `2/24` with leaks `2/2`,
and the exact scientific aggregate frozen above. A mismatch is a hard stop;
expected values are evaluator assertions, not source labels.

## Reproducibility and metadata contract

The source and evaluator are physically separated directories and communicate
only through canonical JSON over subprocess pipes. Runs A and B are fresh
processes. Run C is cold: it executes an isolated temporary code copy with no
inherited Python path or bytecode cache. A, B, and C must produce byte-identical
canonical scientific JSON.

Transport metadata is tested in four states: absent, explicit null, empty
mapping, and populated mapping. All four must produce the same scientific
bytes and Route evaluation. Environment metadata is excluded from the
scientific payload.

## Strict Route-A preartifact contract

The only Route card path is
`evaluations/route_a/SD-C39/2026-08-15.yaml`. Before the first artifact commit,
its top-level `source_commit`, top-level `code_commit`, and nested
`source_lock.code_commit` are all literally
`PENDING_FIRST_ARTIFACT_COMMIT`. Its `freeze_note` must state that Stage 1 is
pending and that Stage 2 is metadata-only.

No `PAPER_MANIFEST.sha256` is created at Stage 1. At a later owner-authorized
Stage 2, all three commit fields must change to the same lowercase 40-hex
artifact commit, `freeze_note` may be sealed, and the root may add the sorted,
unique, self-excluding `PAPER_MANIFEST.sha256`. This integration performs no
Git action and no Stage-2 mutation.

The immutable Stage-1 ledger is `results/SHA256SUMS.txt`. It excludes itself,
the mutable Route YAML, and the absent/future `PAPER_MANIFEST.sha256`. Route
YAML may be listed as an artifact path and receives a separate integrity hash.
Manifest-absent and manifest-present metadata simulations must leave the
science aggregate and Route decision stable.

## Artifact and hygiene gates

The exact result set is closed and machine-audited. Every managed text file
must be valid UTF-8 without BOM, use LF only, and end in exactly one LF. No
`__pycache__`, `.pyc`, `.pyo`, `.pytest_cache`, or retained cold-run temporary
directory is allowed. Research and standard-library dependency locks are
mandatory. A second full integration pass must be idempotent at the managed
artifact level.

## Frozen decision boundary

The expected strict decision remains:

```text
STOP_LOCAL_COEFFICIENT_SATURATION
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)
overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

Finite results audit implementation and adversarial controls only. The
nilpotence criterion, trace-class ownership, and normal-closure saturation
remain theorem-owned.
