# Canonical exact experiment plan — Paper 36 / SD-C38

Freeze date: 2026-08-15 UTC.

Status: frozen after the root `SOURCE_LOCK.md`, root `PREREGISTRATION.md`, and
`experiments/PREREGISTRATION.md`, and before authority code or results.

## 1. Claim-to-certificate matrix

| ID | Frozen audit | Exact success condition | Primary artifact |
|---|---|---|---|
| E1 | affine and free identity words | independent counts agree through length 12; first excess is exactly at `r+3` | `trace_audit.csv` |
| E2 | relation word and marker | relation is an identity, primitive, cyclically nonbacktracking; side lengths and marker verdicts agree | `marker_audit.csv` |
| E3 | damped relation coefficient | exact `S_r` and `theta^(2S_r)` agree; baseline is `2^-46` | `operator_cycle_audit.csv` |
| E4 | finite cellular controls | every boundary square vanishes; exact rational homology dimensions agree | `finite_chain_audit.csv` |
| E5 | generic scalar lift | all sampled powers vanish and the symbolic Euler multiplier is zero | `graded_control.json` |
| E6 | balanced and mutation controls | `r=1` preserves the marker but full filling kills `H_1`; every `r=2..5` mutation fails the marker | `control_summary.json` |
| E7 | prototype bridge | all frozen prototype semantic values agree, without importing its result as authority output | `prototype_bridge_certificate.json` |
| E8 | reproducibility and integrity | fresh A/B and cold C are byte-identical; research/dependency locks, exact inventory, SHA and hygiene gates pass | reproducibility and integrity payloads |

## 2. Frozen parameter matrix

```text
main r values:             2,3,4,5
composite baseline:        4
balanced control:          1
maximum word length:       12
oriented alphabet:         u,U,v,V
damping theta:             1/2
finite controls:           (1,4,3),(2,3,2),(3,4,2),
                           (4,5,2),(4,7,3),(5,6,2)
finite coefficient field:  Q via fractions.Fraction
hash seed:                 0
target-zero data:          none
network/GPU:               unused
Route B:                   false / locked
```

## 3. Independent algorithms

The source uses the prototype affine product, state-distribution dynamic
program, reduced-word stack, and finite path-chain construction. The
evaluator uses a separately implemented affine right-action recurrence,
independent free-word normal forms, independent finite matrix construction,
Gauss-Jordan rank, direct boundary multiplication, and direct marker/weight
formulas. It imports neither `source_core.py` nor `source_generator.py`.

The evaluator must compare raw source rows field for field before assigning
any gate status. Source/evaluator disagreement is a hard failure even if both
sides match the preregistered prototype aggregate.

## 4. Milestones

### M0 — plan and bridge freeze

- Authority experiment preregistration and plan exist first.
- Root research package and all prototype hashes match the frozen values.
- Source and evaluator process files are physically distinct.

### M1 — source generation

- Generate exact affine/free counts through length 12.
- Generate relation marker and damped-cycle data for `r=1..5`.
- Generate exact finite boundary matrices for all six controls.
- Write only deterministic JSON/CSV-ready raw payloads.

### M2 — independent evaluation

- Reconstruct every source datum without importing candidate modules.
- Verify relation identity, primitivity, cyclic nonbacktracking, and length.
- Verify first excess lengths `5,6,7,8` and excess counts `10,12,14,32`.
- Verify the baseline lower-bound cycle weight is
  `1/70368744177664=2^-46`.
- Verify all affine/full boundary squares and rational dimensions.
- Verify the `(1-2+1)` generic multiplier and all sampled powers.

### M3 — tests and analysis

- Reproduce the frozen `33/33` prototype semantic checks.
- Add authority-only firewall, exact-schema, and independent-agreement tests.
- Emit a raw comparison table, numbered findings, implications, and the next
  smallest test in the human-readable analysis report.

### M4 — reproducibility

- Run complete scientific stages in fresh A and B directories.
- Require byte equality for all declared payloads and captured stdout.
- Purge caches and run a fresh cold C directory.
- Publish A only after A=B=C.

### M5 — route and integrity seal

- Freeze strict Route-A v0.2 YAML with the exact rejected tuple.
- Use paired `PENDING_FIRST_ARTIFACT_COMMIT` in all three provenance fields;
  permit only a later simultaneous replacement by one lowercase 40-hex commit.
- Lock research-document and dependency hashes.
- Generate an exact sorted 43-entry SHA-256 ledger and aggregate, excluding
  the metadata-mutable Route YAML.
- Verify exact result inventory, UTF-8/LF, exactly one LF at EOF, no trailing
  whitespace/control bytes/caches, source/evaluator separation, route schema,
  scoped A2 metrics, research pointers, A/B/C certificates, and the canonical
  presence and hygiene of the nonrecursive idempotence certificate.
- Verify that Route dummy sealing and root-manifest presence/absence leave both
  the immutable ledger and complete integrity output byte-identical.

## 5. Acceptance gates

1. All authority scientific and integration tests pass.
2. The independent evaluator agrees with every raw source row.
3. Prototype semantics match all 33 frozen checks, but the authority output
   receives its own newly generated aggregate SHA-256.
4. Six finite controls have affine residual dimensions `2,1,1,1,1,1` and
   complete-presentation residual dimension zero.
5. The route tuple and overall verdict match the source lock exactly.
6. A2 contains all nine v0.2 metrics; target-zero and stability fields are
   scoped `not_applicable;...` values.
7. `source_commit`, top-level `code_commit`, and
   `source_lock.code_commit` are either the identical pending token or the
   same lowercase 40-hex metadata-only seal.
8. Route B is false and proves-too-much risk is realized.
9. A/B/C, research, dependency, inventory, SHA, hygiene, and cache gates pass.

## 6. Canonical output families

- Raw and evaluated JSON/CSV artifacts under `results/`.
- `results/ANALYSIS_REPORT.md` with the analyze-results raw table and findings.
- `EXPERIMENT_REPORT.md` with scope, execution order, exact results, and
  canonical hashes.
- `docs/EXPERIMENT_ARTIFACT_SCHEMA.md`, candidate registry, and obstruction
  registry.
- `evaluations/route_a/SD-C38/2026-08-15.yaml`.

The Route card remains in the artifact inventory but not in the immutable
Stage-1 SHA ledger. It is schema/provenance-audited separately.

No writer-owned file, root manifest, repository README, Git state, mirror, or
Route-B artifact is modified by experiment integration.
