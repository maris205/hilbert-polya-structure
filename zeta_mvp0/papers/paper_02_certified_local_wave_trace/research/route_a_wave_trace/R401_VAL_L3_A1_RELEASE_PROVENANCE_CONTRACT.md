# R401-VAL-L3-A1 release-provenance contract candidate

Contract identifier: `R401-VAL-L3-A1-RELEASE-PROVENANCE-CONTRACT`

Contract version: `write_once_exact_hash_dag_v1_candidate`

Prepared: 2026-08-09 UTC

Status: **PROSPECTIVE_NON_LICENSING / REJECT_FOR_DISPATCH**

## 1. Purpose and non-implementation boundary

This contract defines the exact candidate role maps and acyclic publication
rules for a future L3-A1 production release.  It does not assert that any
listed implementation candidate, machine freeze, main freeze, pre-freeze
review, production result, checker, postcheck, or release currently exists.

The future release builder never runs an evaluator and never creates
scientific authority.  It may publish only after reopening and independently
reproducing an already passing three-checker plus three-postcheck chain.

## 2. Exact 53-role main-freeze input map candidate

The future main freeze must bind exactly the following ordered 53 roles.  The
paths are implementation candidates until their bytes stabilize; changing a
name or path requires updating this contract before independent pre-freeze
review and before main-freeze construction.

| # | role | exact candidate path |
|---:|---|---|
| 1 | `a416_derivation` | `research/route_a_wave_trace/A416_PHASE_FLOWBOX_DERIVATION.md` |
| 2 | `s0_protocol` | `research/route_a_wave_trace/R401_VAL_L3_PHASE_TUBE_PROTOCOL_DRAFT.md` |
| 3 | `s0_report` | `research/route_a_wave_trace/A416_REPRESENTATIVE_PHASE_TUBE_SMOKE.md` |
| 4 | `prefreeze_design` | `research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_DESIGN.md` |
| 5 | `implementation_design_review` | `research/route_a_wave_trace/R401_VAL_L3_A1_DESIGN_REVIEW.md` |
| 6 | `formal_protocol` | `research/route_a_wave_trace/R401_VAL_L3_A1_PROTOCOL.md` |
| 7 | `scheduler_contract` | `research/route_a_wave_trace/R401_VAL_L3_A1_SCHEDULER_CONTRACT.md` |
| 8 | `checker_contract` | `research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md` |
| 9 | `release_contract` | `research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md` |
| 10 | `machine_freeze` | `research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json` |
| 11 | `prefreeze_tests` | `research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_TESTS.json` |
| 12 | `prefreeze_review` | `research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_REVIEW.md` |
| 13 | `s0_compatibility` | `research/route_a_wave_trace/R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json` |
| 14 | `capd_dependency` | `validated/CAPD_DEPENDENCY.md` |
| 15 | `static_evaluator` | `scripts/evaluate_r401_val_l3_a1_static_cell.py` |
| 16 | `branch_evaluator_source` | `validated/capd_r401_phase_branch_tube_mp_a1.cpp` |
| 17 | `branch_evaluator_binary` | `validated/bin/capd_r401_phase_branch_tube_mp_a1` |
| 18 | `branch_runtime` | `scripts/r401_val_l3_a1_branch_runtime.py` |
| 19 | `scheduler` | `scripts/run_r401_val_l3_a1_all_slabs.py` |
| 20 | `static_checker_source` | `scripts/check_r401_val_l3_a1_static_independent.py` |
| 21 | `branch_checker_source` | `scripts/check_r401_val_l3_a1_branch_independent.py` |
| 22 | `composite_checker_source` | `scripts/check_r401_val_l3_a1_composite_independent.py` |
| 23 | `s0_adapter` | `scripts/replay_r401_val_l3_s0_through_a1_checkers.py` |
| 24 | `release_builder` | `scripts/build_r401_val_l3_a1_release_provenance.py` |
| 25 | `test_static_evaluator` | `tests/test_r401_val_l3_a1_static_cell.py` |
| 26 | `test_static_scheduler` | `tests/test_r401_val_l3_a1_static_scheduler.py` |
| 27 | `test_static_checker` | `tests/test_r401_val_l3_a1_static_checker.py` |
| 28 | `test_branch_scheduler` | `tests/test_r401_val_l3_a1_branch_scheduler.py` |
| 29 | `test_branch_checker` | `tests/test_r401_val_l3_a1_branch_checker.py` |
| 30 | `test_s0_compatibility` | `tests/test_r401_val_l3_a1_s0_compatibility.py` |
| 31 | `test_composite` | `tests/test_r401_val_l3_a1_composite_contract.py` |
| 32 | `test_adversarial` | `tests/test_r401_val_l3_a1_adversarial_e2e.py` |
| 33 | `test_release` | `tests/test_r401_val_l3_a1_release_provenance.py` |
| 34 | `l1_final_plan` | `research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json` |
| 35 | `l1_summary` | `results/r401_val_l1_branch/summary.json` |
| 36 | `l1_manifest` | `results/r401_val_l1_branch/manifest.json` |
| 37 | `l1_checker` | `results/r401_val_l1_branch/independent_checker.json` |
| 38 | `l1_postcheck` | `results/r401_val_l1_branch/POSTCHECK_STATUS.json` |
| 39 | `l1_release` | `results/r401_val_l1_branch/RELEASE_PROVENANCE.json` |
| 40 | `a415_summary` | `results/r401_val_l2_all_slabs/aggregate_summary.json` |
| 41 | `a415_manifest` | `results/r401_val_l2_all_slabs/aggregate_manifest.json` |
| 42 | `a415_checker` | `results/r401_val_l2_all_slabs/independent_checker.json` |
| 43 | `a415_postcheck` | `results/r401_val_l2_all_slabs/POSTCHECK_STATUS.json` |
| 44 | `a415_release` | `results/r401_val_l2_all_slabs/RELEASE_PROVENANCE.json` |
| 45 | `s0_static_summary` | `results/r401_val_l3_phase_tube_smoke/summary.json` |
| 46 | `s0_static_manifest` | `results/r401_val_l3_phase_tube_smoke/manifest.json` |
| 47 | `s0_static_checker` | `results/r401_val_l3_phase_tube_smoke/independent_checker.json` |
| 48 | `s0_branch_summary` | `results/r401_val_l3_branch_tube_smoke/summary.json` |
| 49 | `s0_branch_manifest` | `results/r401_val_l3_branch_tube_smoke/manifest.json` |
| 50 | `s0_branch_checker` | `results/r401_val_l3_branch_tube_smoke/independent_checker.json` |
| 51 | `s0_composite_summary` | `results/r401_val_l3_s0_composite/summary.json` |
| 52 | `s0_composite_manifest` | `results/r401_val_l3_s0_composite/manifest.json` |
| 53 | `s0_composite_checker` | `results/r401_val_l3_s0_composite/independent_checker.json` |

This exact 53-role candidate supersedes the incomplete 49-role draft.  The
four added direct bindings are the accepted implementation-design review,
the static evaluator test, the branch runtime module, and the
S0-compatibility test.  They affect implementation authority or replay
semantics and therefore cannot be hidden behind another role's hash.

The map is a strict ordered role-to-`{path,sha256}` object.  A path cannot
serve two roles, a role cannot have two paths, and no extra hash is accepted.
Every listed byte sequence is strict-parsed or semantically audited according
to its role before its digest is accepted.

## 3. Main freeze edge

`R401_VAL_L3_A1_FREEZE.json` is generated last among the 53 inputs and does
not contain its own hash.  It must have exact status
`FROZEN_FOR_PRODUCTION`, bind the exact 102-cell matrix, both ABIs, scheduler
policy, resource limits, machine requirements, archive layout, closed status
tables, checker hashes, 53-role map, and claim boundary.

Its pre-freeze review input must contain exactly one authority declaration:

```text
Verdict: ACCEPT_FOR_FREEZE
```

Near matches, duplicate verdicts, decorated substitutes, a pending verdict,
or author self-approval are rejected.  This candidate neither creates that
review nor creates the main freeze.

## 4. Exact 68-role release map candidate

The future release role map is the ordered union of:

1. the exact 53 roles in section 2;
2. role 54, `main_freeze`, at
   `research/route_a_wave_trace/R401_VAL_L3_A1_FREEZE.json`; and
3. these exact 14 downstream roles.

| # | role | exact candidate path |
|---:|---|---|
| 55 | `run_config` | `results/r401_val_l3_all_slabs/run_config.json` |
| 56 | `static_aggregate_summary` | `results/r401_val_l3_all_slabs/static/aggregate_summary.json` |
| 57 | `static_aggregate_manifest` | `results/r401_val_l3_all_slabs/static/aggregate_manifest.json` |
| 58 | `static_checker_result` | `results/r401_val_l3_all_slabs/independent_static_checker.json` |
| 59 | `static_postcheck` | `results/r401_val_l3_all_slabs/STATIC_POSTCHECK_STATUS.json` |
| 60 | `branch_aggregate_summary` | `results/r401_val_l3_all_slabs/branch/aggregate_summary.json` |
| 61 | `branch_aggregate_manifest` | `results/r401_val_l3_all_slabs/branch/aggregate_manifest.json` |
| 62 | `branch_checker_result` | `results/r401_val_l3_all_slabs/independent_branch_checker.json` |
| 63 | `branch_postcheck` | `results/r401_val_l3_all_slabs/BRANCH_POSTCHECK_STATUS.json` |
| 64 | `composite_summary` | `results/r401_val_l3_all_slabs/composite_summary.json` |
| 65 | `composite_manifest` | `results/r401_val_l3_all_slabs/composite_manifest.json` |
| 66 | `composite_checker_result` | `results/r401_val_l3_all_slabs/independent_checker.json` |
| 67 | `composite_postcheck` | `results/r401_val_l3_all_slabs/POSTCHECK_STATUS.json` |
| 68 | `production_report` | `results/r401_val_l3_all_slabs/R401_VAL_L3_A1_REPORT.md` |

`RELEASE_PROVENANCE.json` is not in its own role map and contains no self-
hash.  The 204 per-cell manifests and their proof/raw payloads are not top-
level roles; the builder independently traverses them and requires the two
aggregate manifests to bind their exact ordered sets.

## 5. Candidate exact release schema

The future release top-level key set is exactly:

```text
schema_version
protocol_id
release_contract
release_status
authority
scientific_licensing_enabled
matrix_id
main_freeze_sha256
machine_freeze_sha256
run_config_sha256
archive_generation_sha256
ordered_static_manifest_root
ordered_branch_manifest_root
roles
component_chains
composite_chain
upstream_chains
s0_compatibility
claim_boundary
milestone_status
theorem_status
final_status
```

A passing future release has:

```text
release_contract = write_once_exact_hash_dag_v1
release_status = PASS_LOCAL_PHASE_TUBE_ALL_SLABS
authority = RELEASE_BINDING_ONLY
scientific_licensing_enabled = true
milestone_status = PASS_LOCAL_PHASE_TUBE_ALL_SLABS
theorem_status = PASS_LOCAL_PHASE_TUBE_ALL_SLABS
final_status = null.
```

The release merely reproduces the composite checker and postcheck.  If either
does not already carry the exact passing value, no passing release can be
built.

## 6. Independent generation recomputation

Before publication, the builder independently:

1. validates and hashes all 53 main-freeze inputs and the main freeze;
2. compares the main-freeze 53-role map with section 2 exactly;
3. validates the sealed run config and complete freeze/machine handshake;
4. scans exactly 102 static and 102 branch cell/manifest identities;
5. reopens every cell manifest and rehashes every proof/raw/record byte;
6. recomputes both ordered component-manifest roots and archive-generation
   digest;
7. validates both component aggregate and checker/postcheck chains;
8. validates the composite producer, checker, and postcheck chain;
9. rehashes and semantically validates both upstream five-object chains;
10. reproduces the closed S0 compatibility facts and nine direct controls;
11. checks the report's exact authority and claim-boundary declarations; and
12. builds the exact ordered 68-role map from captured bytes.

No quoted hash is accepted without reopening its source object.  Per-cell
scientific replay remains the checker responsibility, but the builder
requires checker/postcheck hashes and directly recomputes archive structure
and provenance.

## 7. Same-byte and path safety

Semantic validation and hashing use the same immutable in-memory byte
snapshot.  After each input is opened, the builder records device, inode,
mode, size, and modification metadata and rejects concurrent mutation before
using the snapshot.

Original lexical paths are validated before resolution.  Path traversal,
absolute or normalized aliases, backslashes, symlinked leaf or parent
components, unexpected hidden paths, and duplicate role paths are rejected.
Write-once control objects with a second hard-link name are rejected.

Every additional JSON role is strict-parsed even when its digest matches.
Duplicate keys, nonfinite numbers, Boolean/integer aliases, integral floats in
integer fields, extra status keys, and nested authority aliases are fatal.

## 8. Write-once publication

The expected canonical release bytes are first written to a new same-
filesystem temporary inode, flushed, and re-read.  Publication uses a pinned
directory descriptor and an atomic no-overwrite operation.  The builder then
opens the published inode, checks identity and exact bytes, and flushes the
parent directory.

If an identical canonical release already exists, build mode may verify and
return it without changing bytes.  A different pre-existing release is never
overwritten.  `--verify-only` performs no write and reconstructs the complete
68-role DAG from current source bytes.

No object includes its own hash.  The main freeze is upstream of the run
config; cell manifests are upstream of aggregates; component checkers and
postchecks are upstream of composite controls; the composite checker and
postcheck are upstream of report and release.

## 9. Three-checker and three-postcheck status gate

The builder requires:

```text
static component_status = PASS_STATIC_PHASE_ANCHOR_ALL_SLABS
static milestone/theorem/final = null/null/null
static postcheck = PASS_WRITE_ONCE_POSTCHECK

branch component_status = PASS_BRANCH_TUBE_ALL_SLABS
branch milestone/theorem/final = null/null/null
branch postcheck = PASS_WRITE_ONCE_POSTCHECK

composite component_status = null
composite milestone/theorem = PASS_LOCAL_PHASE_TUBE_ALL_SLABS
composite final = null
composite postcheck = PASS_WRITE_ONCE_POSTCHECK.
```

Any discrepancy, extra authority field, subset status, or non-null final value
blocks release.

## 10. Report contract

The production report must contain one exact authority block:

```text
Status: PASS_LOCAL_PHASE_TUBE_ALL_SLABS
milestone_status = PASS_LOCAL_PHASE_TUBE_ALL_SLABS
theorem_status = PASS_LOCAL_PHASE_TUBE_ALL_SLABS
final_status = null
Claim boundary: complete-period local-tube candidate uniqueness modulo time translation and distinguished-branch tube membership only; no global routing, trace-formula, Hilbert-Polya, zeta-zero, or RH promotion
```

Conflicting or decorated status declarations, arbitrary `*_status` tokens,
HTML/entity substitutes, duplicate verdicts, or a weakened claim boundary are
rejected.  Component statuses may appear only in a separately delimited
component-evidence table and cannot replace the authority block.

## 11. Failure and recovery

A producer or provenance defect invalidates the generation; it is not fixed
in place.  A repaired implementation requires a new future freeze and fresh
generation.  A scientific or resource non-pass remains archived and cannot
be removed from a release candidate by shrinking the role map.

The operational staging sibling and sibling quarantine-transaction journal
are not release roles.  The builder requires the journal to be absent and the
operational sibling to be absent or quiescent, then requires the
authoritative result root to contain its exact final path set and no hidden,
staging, or extra object.  A live journal must first be closed by the
scheduler's deterministic recovery transaction; the builder cannot close it.
Quarantined generations are recoverable evidence but never release inputs.

## 12. Required release tests

Before freeze construction, tests must cover all 53 missing-input cases, all
68 missing/extra/duplicate/reordered role cases, self-hash injection,
main-freeze/hash disagreement, cell/aggregate mutation, status mismatch,
report boundary mutation, strict JSON/type/nonfinite failures, symlink/hard-
link/path aliases, same-byte TOCTOU, publication inode swap, overwrite refusal,
idempotent identical verification, and read-only `--verify-only` behavior.

The exact test file and its final hash are role 33 of the main-freeze input
map.  Passing mock tests do not authorize production.

## 13. Claim boundary and present status

Even a future release proves only the conditional local phase-tube theorem in
the formal protocol.  It does not prove global tube routing, global orbit
uniqueness, a trace formula, a Hilbert--Polya operator, zeta-zero
reconstruction, RH, or any implication toward RH.

Current exact state:

```text
contract_status = PROSPECTIVE_NON_LICENSING
role_map_status = IMPLEMENTATION_CANDIDATE
main_freeze_exists = false
release_exists = false
dispatch_authorized = false
milestone_status = null
theorem_status = null
final_status = null
```

This contract creates neither a freeze nor a release and invokes no evaluator.
