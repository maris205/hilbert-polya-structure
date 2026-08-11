# A4.16 L3-A1 role-11 pre-freeze test-evidence implementation increment

Prepared: 2026-08-11 UTC

Protocol: `R401-VAL-L3-A1-PREFREEZE-TESTS`

Authority: **DESIGN / IMPLEMENTATION EVIDENCE ONLY / NON_LICENSING / role 11
absent / role 12 absent / role 54 absent / no scientific dispatch**

## 1. Purpose and present boundary

This increment fixes the non-scientific evidence contract for prospective
main-freeze input role 11,
`research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_TESTS.json`.  It defines
the exact top-level schema, the acyclic 51-role pre-review snapshot, seven
fixed command-result positions, the independent no-subprocess checker, and a
fixed-destination no-replace publisher.

This implementation increment does not create a candidate, publish role 11,
create the future independent role-12 review, or construct downstream role 54.
The implementation, independent checker, focused tests, command identities,
and exact test totals are now mechanically locked below.  The recorded
durations are engineering observations only; the future candidate will embed
fresh per-command durations from its one authorized capture run.

Current canonical facts that are already outside this implementation edge are:

```text
canonical_machine_role10_exists = true
canonical_machine_role10_sha256 = 0d5c46726ee8142e0e53f97c904213dfc9b795ac300b423277bc27a711f5c21e
canonical_machine_role10_size_bytes = 54526
canonical_machine_role10_mode = 0644
canonical_machine_role10_nlink = 1
canonical_machine_role10_publication_commit = 5086e33c7c66f33785338e90b340347e086d9941
canonical_machine_role10_role24_postverify = PASS_MACHINE_FREEZE_VERIFY_ONLY
canonical_s0_compatibility_role13_exists = true
canonical_s0_compatibility_role13_sha256 = d2844c9fd98f76bd41dda937e8f19f978aa48468c17c5a24ebd25baf125f5e30
canonical_s0_compatibility_role13_size_bytes = 8820
canonical_s0_compatibility_role13_mode = 0644
canonical_s0_compatibility_role13_nlink = 1
canonical_s0_compatibility_role13_publication_commit = be2a732625d9cab97879539873a756e1eabd366d
canonical_prefreeze_tests_role11_exists = false
canonical_prefreeze_review_role12_exists = false
main_freeze_role54_exists = false
scientific_licensing_enabled = false
production_authorized = false
scientific_dispatch_performed = false
component_status = null
milestone_status = null
theorem_status = null
final_status = null
```

Role 10 is machine admission only.  Role 13 is the exact representative S0
compatibility replay only.  Neither supplies role-12 review authority, role-54
freeze authority, production authorization, or a scientific result.

## 2. Exact closed 22-key role-11 schema

The role-11 object has exactly these top-level keys, with no aliases or extras:

```text
schema_version
protocol_id
artifact_role
artifact_status
authority
recorded_at_utc
scientific_licensing_enabled
production_authorized
scientific_dispatch_performed
held_out_policy
repository_snapshot
prerequisite_bindings
pre_review_input_roles
evidence_tool_bindings
command_results
test_totals
covered_gates
claim_boundary
component_status
milestone_status
theorem_status
final_status
```

The following literals and null/Boolean ceilings are already fixed:

```text
schema_version = 1
protocol_id = R401-VAL-L3-A1-PREFREEZE-TESTS
artifact_role = PREFREEZE_TEST_RECORD
artifact_status = PASS_PENDING_INDEPENDENT_PREFREEZE_REVIEW
authority = PREFREEZE_TEST_EVIDENCE_ONLY
scientific_licensing_enabled = false
production_authorized = false
scientific_dispatch_performed = false
component_status = null
milestone_status = null
theorem_status = null
final_status = null
```

`recorded_at_utc` is a strict UTC timestamp recorded only after all seven
commands and the terminal repository replay complete.  A passing artifact
status means only that the bounded engineering evidence record is internally
complete.  It is not `ACCEPT_FOR_FREEZE`, a component pass, a theorem pass,
or a dispatch license.

The implementation freezes the nested domains as follows (each brace is an
exact key set, not a minimum):

```text
held_out_policy = {
  held_out_l3_scientific_outputs_read,
  held_out_l3_evaluator_dispatched,
  scientific_evaluator_dispatch_count,
  new_archive_scope,
  s0_archive_access,
  canonical_result_created
}
repository_snapshot = {
  authority_root, branch, capture_commit_oid, capture_tree_oid, origin_url,
  origin_main_oid, live_remote_main_oid, head_equals_origin_main,
  head_equals_live_remote_main, ahead, behind,
  worktree_clean_before, worktree_clean_after
}
prerequisite_bindings = {
  machine_role10, s0_compatibility_role13,
  second_fresh_rebuild_replay, canonical_absence
}
canonical_absence = {
  prefreeze_review_role12_exists, main_freeze_role54_exists,
  canonical_result_root_exists, canonical_operational_root_exists
}
evidence_tool_bindings = {producer, independent_checker, focused_test}
file_binding = {path, sha256, size_bytes, mode, nlink}
role_entry = {role, path, sha256, size_bytes, mode, nlink}
verify_receipt = {
  verification_status, authority, candidate_sha256,
  size_bytes, promotion_authorized
}
command_result = {
  name, kind, argv, cwd, environment, return_code,
  started_at_utc, wall_duration_ms,
  stdout_utf8, stdout_sha256, stdout_size_bytes,
  stderr_utf8, stderr_sha256, stderr_size_bytes,
  pytest_counts, semantic_receipt
}
pytest_counts = {passed, failed, skipped, xfailed, xpassed}
test_total = {passed, failed, skipped, xfailed, xpassed, wall_duration_ms}
test_totals = {prefreeze_focused, l3_a1_modules, paper02_full}
```

The second-rebuild semantic receipt is an exact 19-key object and includes
`staging_output_removed=true`; its other fields bind the source, persistent
binary before/after SHA and inode, temporary build SHA/size/mode,
byte-for-byte equality, no persistent overwrite, and no scientific dispatch.
The implementation independently rejects duplicate keys, non-finite numbers,
Boolean/integer aliases, non-string object keys, tuple/list aliases in the
in-memory builders, malformed timestamps, and non-canonical JSON bytes.

## 3. Held-out and repository invariants

The final `held_out_policy` must prove, using exact closed fields, all of the
following:

- no held-out/all-slab L3 cell was read or evaluated;
- no static or branch scientific evaluator was dispatched;
- the canonical S0 compatibility object was read only;
- all newly created archives were temporary engineering/test fixtures; and
- the second fresh rebuild compiled only the already frozen branch source to
  a new temporary output and did not execute that binary scientifically.

The final `repository_snapshot` must bind a single exact commit/index/worktree
view and the absence of role 11, role 12, role 54, canonical production run
config, production result root, and canonical L3-A1 release before role-11
publication.  It must bind the presence and exact raw/stat identities of
canonical roles 10 and 13.  Dirty-index, dirty-worktree, untracked
authoritative-path, symlink, hard-link, path-alias, or concurrent-mutation
states fail closed.

The exact clean-environment allowlist, process-group timeout, output caps, and
terminal cleanup rules are authority-bearing implementation details.  Every
subprocess must use an argv list with `shell=false`, a deterministic minimal
environment, a new process group, bounded stdout/stderr capture, TERM/KILL
escalation, and complete descendant cleanup before its result is classified.

## 4. Exact 51-role pre-review snapshot

`pre_review_input_roles` is an ordered array of exactly 51 entries.  It starts
from the frozen 53-role main-freeze order and excludes only:

```text
role 11 = prefreeze_tests
role 12 = prefreeze_review
```

There is no renumbering or sorting after exclusion.  Every entry has exactly:

```text
{role, path, sha256, size_bytes, mode, nlink}
```

`role`, `path`, and `sha256` are strings; `size_bytes` and `nlink` are exact
integers; `mode` is the exact four-character octal string.  SHA-256 is over
the raw byte image captured from a pinned single-link regular file.  The
semantic parse and digest use the same bytes, and every entry is terminally
reopened before candidate construction.

The exact retained order and paths are:

| frozen # | role | exact path |
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

The future capture computes every raw hash/stat field from the clean committed
input generation and terminally replays it.  No role-11 candidate digest is
inserted into this 51-role array, and future role 12 is absent by construction.

## 5. Direct prerequisite bindings

`prerequisite_bindings` must independently strict-parse and bind canonical
roles 10 and 13 in addition to their entries in the 51-role array.

For role 10 it replays the closed machine schema, the current raw digest and
stat identity, role-19 source binding, and the separate role-24 canonical
verify-only result.  For role 13 it replays the unchanged exact 18-key
`NON_LICENSING` compatibility object, its four frozen source bindings, nine
sealed S0 control hashes, raw digest, size, mode, link count, and null
milestone/theorem/final values.

The duplicated direct bindings are intentional cross-checks, not alternate
authorities.  A mismatch between `prerequisite_bindings` and the corresponding
51-role entries is fatal.

## 6. Seven fixed command-result positions

`command_results` is an ordered array of exactly seven results in this
semantic order:

1. **role-24 canonical machine verify:** zero-write verification of the fixed
   canonical role-10 inode and all current live machine bindings;
2. **role-13 canonical compatibility verify:** zero-write independent replay
   of the fixed canonical role-13 bytes, exact 18-key schema, sealed S0 facts,
   and four source bindings;
3. **role-11 focused pytest:** the dedicated producer/checker/publication
   contract module only;
4. **ten-module L3-A1 pytest:** the existing nine owned L3-A1 modules plus the
   new role-11 focused module, with no scientific evaluator dispatch;
5. **complete Paper 02 pytest:** the full Paper 02 regression under the same
   clean implementation bytes;
6. **Git diff check:** exact `git diff --check` success over the stable tree;
7. **second fresh branch rebuild:** one new owned temporary rebuild of the
   frozen branch evaluator source, proving exact equality with the persistent
   role-17 binary without overwriting or executing it scientifically.

All commands use the exact Paper 02 root as cwd, `shell=false`, child
`umask=0022`, a new process group, a 600-second timeout, two-second TERM grace,
one-second pipe-close grace, and separate 1 MiB stdout/stderr caps.  The exact
environment is:

```text
PATH=/root/miniconda3/bin:/usr/bin:/bin
LANG=C.UTF-8
LC_ALL=C.UTF-8
TZ=UTC
PYTHONHASHSEED=0
PYTHONNOUSERSITE=1
PYTHONDONTWRITEBYTECODE=1
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
OMP_NUM_THREADS=1
OPENBLAS_NUM_THREADS=1
MKL_NUM_THREADS=1
NUMEXPR_NUM_THREADS=1
```

The three pytest argv arrays all begin with
`/root/miniconda3/bin/python3 -m pytest -q -p no:cacheprovider --color=no`.
They respectively append the focused role-11 test, the exact ten L3-A1 test
modules listed above, or no path (complete Paper 02 discovery).  The other
fixed argv arrays invoke role 24 `--verify-machine-freeze`, the independent
role-11 checker `--verify-s0-compatibility`, and
`/usr/bin/git diff --check HEAD --`.  The seventh outer argv invokes this
producer with `--second-fresh-rebuild-only --output` followed by its unique
owned `/tmp` output; its semantic receipt binds the exact inner compiler argv.
An eighth command, omitted/reordered command, shell string, alternate plugin
set, or post-hoc rerun substitution is rejected.

## 7. Raw transcript and total-replay requirement

Hash-and-size-only command receipts are insufficient.  Every command result
must contain bounded raw `stdout_utf8` and `stderr_utf8` preimages, together
with their exact encoded byte sizes and SHA-256 values.  The final nested
command-result schema binds the exact argv list, working directory,
environment identity, return code, bounded raw transcripts, duration, and
command-specific parsed facts.  The producer implementation separately
enforces `shell=false`, the frozen timeout policy, new-process-group execution,
TERM/KILL escalation, and descendant cleanup; those process-control facts are
implementation invariants, not extra artifact keys.

The independent checker must:

1. encode both stored UTF-8 strings itself and reproduce size and SHA-256;
2. independently parse pytest summaries and recompute the exact stored
   passed/failed/skipped/xfailed/xpassed totals rather than trusting producer
   totals, while rejecting any `errors`, `deselected`, or other unmodelled
   summary token;
3. enforce the exact empty/nonempty stderr rule for each command;
4. independently parse the role-24 and role-13 verify outputs;
5. replay diff-check success from the exact captured empty output contract;
6. validate the second rebuild receipt and persistent-binary equality; and
7. reproduce the three `test_totals` entries from their corresponding
   validated pytest results.

Malformed UTF-8, truncated output, cap overflow, digest/size mismatch,
unparseable or ambiguous pytest text, timeout, signal, surviving descendant,
unexpected skip/failure, or command/result identity mismatch rejects the
record.  Wall time is operational evidence only and cannot repair a failed
authority gate.

## 8. Independent checker boundary

The independent role-11 checker must use a separately bound source image.  It
may read the candidate, 51 live input roles, canonical roles 10 and 13, and
the evidence-tool sources.  It must not import the producer, invoke a
subprocess, rerun a command, write a sidecar, publish role 11, construct role
12 or role 54, or invoke any scientific evaluator.

It independently enforces the exact 22-key schema and nested schemas, strict
JSON/CJ serializer, closed authority literals, UTC timestamp, held-out policy,
repository snapshot, 51-role order and six-key entries, prerequisite
cross-bindings, evidence-tool hashes, seven transcript preimages, recomputed
test totals, covered gates, and claim boundary.  Its success is verify-only
engineering evidence and must retain promotion, production, dispatch, and all
scientific statuses as false or null.

The checker source is
`scripts/check_r401_val_l3_a1_prefreeze_tests_independent.py`.  It is a
stdlib-only implementation which does not import the producer and exposes two
mutually exclusive read-only modes: `--verify-s0-compatibility` and
`--verify-prefreeze-tests` (with `--candidate` as the exact alias used by the
publisher).  A role-11 success line has the exact form:

```text
prefreeze_test_verification=PASS_PREFREEZE_TEST_RECORD_VERIFY_ONLY authority=NON_AUTHORITATIVE_VERIFY_ONLY candidate_sha256=<lowercase SHA-256> size_bytes=<integer> promotion_authorized=false
```

Before final pass totals are frozen, role-11 success is mechanically disabled.
For a temporary candidate, the checker also replays the current commit/tree,
v2 index image, every tracked blob/mode, terminal 51-role and three-tool file
images, and fixed forbidden namespaces.  When later reading the canonical
historical role 11, it validates the captured Git object DAG without falsely
requiring the current branch or future role-12/role-54 namespaces to remain at
their prepublication state.  The final checker source hash was recorded only
after the exact test totals were locked.

## 9. Fixed-destination no-replace publication

The role-11 publisher has exactly one derived destination:

```text
research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_TESTS.json
```

The producer CLI has exactly three mutually exclusive modes:

```text
--capture-prefreeze-tests --output <new /tmp candidate>
--publish-prefreeze-tests --candidate <candidate> --expected-sha256 <lower64> --authority-root <exact Paper02 root>
--second-fresh-rebuild-only --output <owned /tmp binary>
```

The candidate is a nonempty, at-most-4-MiB, single-link regular file with mode
`0600`, located as the only leaf under one euid-owned mode-`0700` directory
directly below `/tmp`.  Capture uses exclusive creation and performs a final
candidate inode/bytes/parent replay after all long live-input replays.
Publication has the following fixed transaction boundary:

- the source candidate is outside the canonical tree and remains unchanged;
- the expected digest expresses exact operator byte intent;
- the publisher terminally replays the candidate, independent-checker
  success, evidence-tool bindings, 51 roles, and canonical roles 10 and 13;
- it creates only a new explicit-mode same-parent staging inode;
- publication uses Linux `renameat2(RENAME_NOREPLACE)` with no overwrite or
  replace-capable fallback;
- every pre-existing destination is fatal, including byte-identical content;
- only an inode-matched pre-rename stage owned by the invocation may be
  cleaned; and
- after rename, no failure authorizes rollback, unlink, repair, overwrite, or
  idempotent republish.

Cooperating publishers acquire a nonblocking advisory lock on the already
pinned canonical parent directory inode; this creates no lock file and avoids
cross-invocation staging cleanup invalidating the winning terminal replay.
The lock is only coordination: Linux `renameat2(RENAME_NOREPLACE)` remains the
integrity boundary, so a non-cooperating writer still cannot overwrite an
existing destination.

The separate publication receipt has exactly 25 keys.  Its fixed literals are
`artifact_role=PREFREEZE_TEST_PUBLICATION_RECEIPT`,
`artifact_status=PUBLISHED_WRITE_ONCE_NON_LICENSING`,
`authority=PREFREEZE_TEST_PRODUCER_PUBLICATION_ONLY`,
`publication_method=SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1`, and
`independent_verification_status=PASS_PREFREEZE_TEST_RECORD_VERIFY_ONLY`.
It binds candidate/canonical paths, role-11 digest/size/mode/nlink, serializer,
independent checker path/digest, and `independent_verification_performed=true`;
promotion/licensing/production/dispatch remain false and all four scientific
statuses remain null.  This receipt cannot fabricate the future role-12
verdict or authorize role 54.

## 10. Acyclic authority DAG

The construction order is:

```text
stable 51 pre-review input roles
        + canonical role 10 and role-24 replay
        + canonical role 13 and independent replay
        + stable producer/checker/test tools
                         |
                         v
             seven fixed bounded commands
                         |
                         v
        exact 22-key temporary role-11 candidate
                         |
                         v
       separate no-subprocess independent checker
                         |
                         v
  separately authorized fixed no-replace role-11 publication
                         |
                         v
      independent role-12 `Verdict: ACCEPT_FOR_FREEZE`
                         |
                         v
 all 53 inputs final -> downstream role-54 main freeze
                         |
                         v
 initialize-only audit -> separate production authorization
```

The 51-role snapshot excludes role 11 and role 12, so the role-11 object does
not contain itself and does not predict its reviewer.  The later main freeze
binds all 53 final inputs, including the now-canonical role 11 and the later
independent role 12.  Role 54 remains external and downstream; it contains no
self-hash.

## 11. Covered gates and explicit nonclaims

The final closed `covered_gates` array is ordered exactly as follows:

```text
EXACT_51_ROLE_ORDER_AND_SAME_BYTE_SNAPSHOTS
CANONICAL_ROLE10_AND_ROLE13_REPLAY
SEVEN_FIXED_COMMAND_IDENTITIES
BOUNDED_RAW_UTF8_TRANSCRIPT_REHASH
PYTEST_SUMMARY_REPARSE_AND_ZERO_NONPASS_COUNTS
CLEAN_REPOSITORY_AND_FIXED_ENVIRONMENT
PROCESS_GROUP_TIMEOUT_AND_DESCENDANT_CLEANUP
SECOND_REBUILD_NO_OVERWRITE_BYTE_EQUALITY
STRICT_SCHEMA_TYPES_PATHS_LINKS_AND_TOCTOU_REPLAY
INDEPENDENT_CHECKER_SOURCE_SEPARATION
WRITE_ONCE_FIXED_DESTINATION_NOREPLACE_PUBLICATION
```

The exact `claim_boundary` must state that role 11 is pre-freeze engineering
evidence only.  It proves no L3-A1 component, milestone, theorem, or final
status; reads no held-out/all-slab result; authorizes no scientific dispatch;
and makes no global tube-routing, trace-formula, Hilbert--Polya, zeta-zero, RH,
or implication-toward-RH claim.

## 12. Mechanical completion ledger

The implementation lock is:

```text
producer_path = scripts/build_r401_val_l3_a1_prefreeze_tests.py
producer_sha256 = 2744f044d444e1cddb472ca436afc24339a547e360631f400a8d672d105e4e58
independent_checker_path = scripts/check_r401_val_l3_a1_prefreeze_tests_independent.py
independent_checker_sha256 = 7cba6a562fa398719ac833dba596b892abaf45c197d5880eb159757c5758c9ef
focused_test_path = tests/test_r401_val_l3_a1_prefreeze_tests.py
focused_test_sha256 = f931855f8394f196f4080698be5f9fcc04f7a5ef7d15e139638fb95de2781fcf
seven_exact_argv_arrays = LOCKED_IN_PRODUCER_AND_INDEPENDENT_CHECKER
expected_test_passed = {prefreeze_focused:100,l3_a1_modules:621,paper02_full:1016}
post_lock_focused = 100 passed in 6.14s
post_lock_ten_module = 621 passed in 168.52s
post_lock_paper02 = 1016 passed in 223.80s
publisher_concurrency_stress = 180 fork rounds, exactly one winner per round
producer_checker_differential = 710 scalar + 210 container mutations, 0 mismatches
independent_implementation_review = ACCEPT / P0=0 / P1=0 / P2=0
```

No role-11 candidate hash or publication receipt exists at this implementation
boundary.  Role 12, role 54, run config, scientific results, and scientific
dispatch authority also remain absent.  No scientific evaluator was invoked
while implementing or validating this increment.
