# Paper 39 claim-driven exact experiment plan — SD-C41

Date frozen: 2026-08-16

Version: `SD-C41-stage1-plan-v1`

## Material passport

- Origin skills: `experiment-plan`, `experiment-bridge`, and
  `analyze-results`
- Origin mode: authority implementation plan for an exact retrospective audit
- Verification status at freeze: `UNVERIFIED_IN_AUTHORITY`
- Experiment type: deterministic exact parsing and graph validation

## Objective and hypothesis

The experiment reproduces the byte-frozen Paper-39 typed affine closure
certificate inside the authority tree. It audits endpoint-obstruction
totality, typed transfer ownership, finite repair/token coverage, the expanded
proof-DAG projection, adversarial rejection, and registry-only handoff.

The hypothesis is deliberately terminal and contract-relative: the exact
retrospective 14-class/16-token encoding is completely classified, creates no
new mechanism, and returns control to the already source-locked non-affine
registry. It is not a universal no-go for affine constructions and not a
prospective preregistration of P35--P38 outcomes.

## Claim map

| Claim | Minimum convincing evidence | Block |
|---|---|---|
| C1: endpoint-obstruction totality on the frozen domain | every token has an explicit path, endpoint, and nonempty obstruction or exit map | B2 |
| C2: typed finite classification | exact 14-class 6/6/2 census and 16-token 8/8 census; exits never count as failures | B2 |
| C3: expanded proof evidence is retained | exact 6/5 spine, 22/28 DAG, 17 tags, total auditable many-to-one fibers, and valid E22 firewall | B2 |
| C4: the firewall rejects semantic escape | both evaluators reject all 29 mutations | B3 |
| C5: registry handoff creates no mechanism | six existing rows, zero insertion/ranking/proposal, realized return plus executed empty-fixture fallback | B4 |
| C6: authority result is reproducible | fresh A/B, isolated cold C, two full runs, hidden-provenance audit, exact sets, ledger, and hygiene all pass | B5 |

Anti-claim: category exit, auxiliary historical firewall, reflexive endpoint,
or similarity of underlying bases supplies a mathematical obstruction or
candidate-state inheritance witness.

## Setup

- Language: Python 3 standard library only.
- Arithmetic: exact strings, integers, booleans, lists, maps, and SHA-256; no
  floating-point statistics.
- Entry command from the paper directory:
  `PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 python3 -I -B code/run_exact_integration.py`
- Independent audit command:
  `PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 python3 -I -B code/audit_integrity.py`
- Hidden-provenance audit command: prefix the audit with
  `PAPER39_HIDE_EXTERNAL_PROVENANCE=1`.
- Hardware: CPU only; no GPU.
- Network and external datasets: forbidden.
- Expected wall time: under one minute.
- Timeout: five minutes; overrun is a failure, not permission to broaden the
  finite contract.

## Inputs

| Input | Path | Role |
|---|---|---|
| immutable research lock | `docs/RESEARCH_LOCK.json` | nine authority-local immutable writer/audit files plus frozen experiment-plan pointers |
| prototype provenance lock | `docs/PROTOTYPE_LOCK.json` | final v4 prototype, math manifest/aggregate, literature, DA, counts, and exact science hash |
| dependency lock | `docs/DEPENDENCY_LOCK.json` | exact standard-library import surface; no external dependency |
| source core | `code/source/source_core.py` | emits normalized source records only |
| source emitter | `code/source/emit_packet.py` | canonical JSON transport over stdout |
| main evaluator | `code/evaluator/evaluate_packet.py` | validates the frozen contract without importing source code |
| independent evaluator | `code/evaluator/independent_evaluator.py` | separately implemented scientific validator |
| Route evaluator | `code/evaluator/evaluate_route_a.py` | derives only the strict all-FAIL/NA Route tuple from accepted science |

The integrated code and immutable authority inputs contain all runtime logic
and data. `/tmp/paper39_*` is provenance-only and is never a runtime
dependency.

## Experimental blocks

### B1 — Immutable extraction and provenance

1. Verify all nine immutable authority research hashes and both experiment
   plan hashes before any scientific output is accepted.
2. Verify final math bridge v4, math manifest, package aggregate, corrected
   literature audit, DA report, Route-A evaluator v0.2, P35--P38 authority
   artifacts, and Session-4 registry/preregistration locks.
3. Machine-extract and normalize every inherited obligation, source object,
   marker, operator owner, determinant owner, obstruction, forbidden escape,
   and terminal code.
4. Independently parse the registry. Treat chronology as a trusted hashed
   source assertion only.

Decision gate: every declared path and SHA matches exactly; otherwise stop
before classification.

### B2 — Typed closure-DAG evaluation

1. Validate the 6-node/5-edge structural spine and the exact 22-node/28-edge
   expanded DAG.
2. Validate the disjoint 28-edge partition: 17 internal, 5 closure, 3 token
   exits, 1 non-domain firewall, and 2 guards.
3. Validate exact ranks, acyclicity, path continuity, endpoint classes, all 17
   internal tags, all 14 repair classes, and all 16 ordered unique tokens.
4. Validate total structural node/edge projection fibers while preserving all
   expanded artifacts. Never assert injectivity or inverse reconstruction.
5. Enforce the closed transfer enum. Require exact identity or a declared
   theorem-backed equivalence for carry; require new authority for reset; keep
   exit separate from failed-`Good` evidence.
6. Require all four `E36_37` identity fields to reset under the P37 source
   lock, with zero equivalence bindings. Bind historical provenance only as
   non-state metadata through endpoints, E07, exact P36/P37 hashes, and packet
   locks.
7. Require E22 to be the unique auxiliary non-domain firewall with empty
   class/token fibers and zero coverage credit.

Decision gate: main evaluator 535/535, independent evaluator 278/278,
science projection SHA-256
`77a45be483807b81ba61fe0f16b16be20fcd7e6e4ff1f3f74f34d052c6881d93`,
class census 6/6/2, token census 8/8.

### B3 — Adversarial controls

Execute the 29 frozen mutation cases from the preregistration. Each mutation
must be evaluated by both implementations, and each implementation must fail
at least one mutation-specific semantic check. Acceptance by either evaluator
is a terminal integrity failure.

Decision gate: 29/29 rejected by the main evaluator and 29/29 rejected by the
independent evaluator.

### B4 — Registry handoff

Parse exactly `SD-C01` through `SD-C06` without ranking, selection, proposal,
or new identifier. Require the live terminal
`RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY`. Execute a separately
hash-locked zero-row fixture and require
`STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR` only on that synthetic branch.

Decision gate: six live rows, zero new mechanism/ranking/proposal, both live
and conditional branches executed with their distinct exact terminal codes.

### B5 — Reproducibility, Route, and integrity

1. Parse all Python imports and enforce physical/source-import separation.
2. Run source and both evaluators in fresh processes for empty runs A and B.
3. Copy only the declared integration inputs to a new temporary directory
   whose `results/` starts empty; hide all external `/tmp` provenance; run the
   complete authority runner for cold C.
4. Require A/B/C identity for source packet, canonical science, and Route
   evaluation bytes. Require both evaluators to agree on the canonical science
   projection, not on implementation-local check ordering.
5. Test absent, null, empty, and populated transport metadata and simulated
   root-manifest absent/present stability.
6. Materialize the complete managed result set twice and require the second
   pass to report `changed_paths = 0`.
7. Freeze a self-excluding ledger, exact result set, exact managed-text set,
   research/dependency/prototype locks, source/evaluator boundary, and
   idempotence evidence.
8. Run standalone normal and hidden-provenance audits and require byte
   identity.
9. Require Stage-1 root-manifest absence and the literal pending Route
   provenance triple.

Decision gate: every exact-set, lock, ledger, hygiene, separation, metadata,
manifest, idempotence, normal/hidden, and cold-copy assertion passes.

## Expected outputs and success criteria

| Output class | Path | Criterion |
|---|---|---|
| source and science | `results/source_packet.json`, `results/scientific_results.json` | accepted canonical bytes; science SHA exactly `77a45be...` |
| evaluator details | `results/main_evaluation.json`, `results/independent_evaluation.json` | 535/535 and 278/278 |
| fresh runs | `results/runs/{A,B,C}/` | source/science/Route byte identity |
| mutations | `results/adversarial_tests.json` | 29/29 rejected by both |
| exact analysis | `results/analysis_summary.json` | retrospective 6/6/2 and 8/8 classification; no universal claim |
| reproducibility | `results/reproducibility_certificate.json` | A/B/cold-C and full-run identity pass |
| integrity | `results/integrity_audit.json`, exact-set files, and `results/SHA256SUMS.txt` | every managed check passes; ledger excludes itself/Route/root manifest |
| fixed Route card | `evaluations/route_a/SD-C41/2026-08-16.yaml` | strict v0.2, all gates FAIL, B false, metrics NA, pending triple |
| report | `EXPERIMENT_REPORT.md` | exact evidence, scope boundary, and registry handoff stated |

The abbreviated science hash in the table is presentation-only; executable
locks and reports must use the full 64-hex value.

## Route-A output contract

The Route evaluator consumes accepted canonical science only. It emits
`A0_FAIL`, `A1_FAIL`, `A2_FAIL`, `A3_FAIL`, and `A4_FAIL`, with `B = false` and
status `REJECTED`. All target and root metrics are typed `NA`. It must not infer
scientific validity from the Route seed snapshot; the source/evaluator result
is authoritative for the integrated output.

The fixed card keeps the literal Stage-1 triple
`PENDING_FIRST_ARTIFACT_COMMIT`. Stage 1 must not create
`PAPER_MANIFEST.sha256`. The immutable result ledger excludes itself, this
mutable Route card, and the future root manifest. Stage 2 is explicitly limited
to the fixed Route card plus a self-excluding root manifest.

## Run order and stopping

1. Freeze these two experiment documents and record their exact SHA-256 values.
2. Verify immutable research/prototype/dependency locks and manifest absence.
3. Run B1 provenance checks.
4. Run B2 main and independent science evaluators.
5. Run B3 mutations and B4 registry branches.
6. Run fresh A/B and empty-copy cold C.
7. Materialize exact results, report, and pending Route card.
8. Rerun the complete pipeline and require zero changed paths.
9. Run byte-identical normal and hidden standalone audits.

Any failed exact assertion stops publication. Failure does not authorize
repair-alphabet expansion, object/marker/operator substitution, Route B,
successor proposal, ranking, target-data access, or a review loop.
