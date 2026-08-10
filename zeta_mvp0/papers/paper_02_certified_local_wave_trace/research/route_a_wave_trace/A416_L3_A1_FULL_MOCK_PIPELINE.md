# A4.16 L3-A1 full 204-cell mock pipeline

Date: 2026-08-10 (UTC)

Protocol family: `R401-VAL-L3-A1`

Status: **FULL MOCK ENGINEERING PIPELINE / NON_LICENSING / NO DISPATCH**

## Outcome and authority

The A4.16 L3-A1 engineering implementation now closes one complete temporary
mock pipeline:

```text
102 synthetic static cells
  -> static aggregate
  -> independent static checker
  -> write-once static postcheck
102 synthetic branch cells
  -> branch aggregate
  -> independent branch checker
  -> write-once branch postcheck
both component chains
  -> composite controls
  -> independent composite checker
  -> write-once composite postcheck
mock report + MOCK_MAIN_FREEZE
  -> exact 68-role mock release
  -> verify-only replay.
```

This is an implementation milestone, not a scientific milestone.  No formal
static evaluator, CAPD branch evaluator, representative evaluator, held-out
slab, or all-slab scientific evaluator was dispatched.  The temporary mock
release has

```text
release_status = PASS_MOCK_PROVENANCE_REPLAY
scientific_licensing_enabled = false
component_status = null
milestone_status = null
theorem_status = null
final_status = null.
```

It is not `PASS_LOCAL_PHASE_TUBE_ALL_SLABS`, does not satisfy a pre-freeze
review, and cannot authorize a main freeze or production run.

## Implemented chain

| Surface | Present mock implementation | Formal boundary |
|---|---|---|
| scheduler | exact 51-slab by two-precision matrices for static and branch components; deterministic barriers, resume, no-replace publication, aggregate-last closure, composite controls | production initialization and evaluator dispatch fail closed |
| static checker | no-import 102-cell proof/record/manifest and aggregate replay; write-once checker/postcheck | diagnostics explicitly state that scientific proof replay was not performed |
| branch producer | synthetic executable emits the complete 12-string and 64-phase transcript ABI with zero slow coordinates | performs no CAPD integration and supplies no flow enclosure |
| branch checker | independently replays accepted L1 primary domains, raw/record/manifest bytes, 6,528 phase records, Arb `omega_minus`, rational tube implications, aggregate roots, and cross-precision agreement | result is `PASS_MOCK_INDEPENDENT_REPLAY`, not a branch-tube theorem |
| composite checker | binds both 102-cell component checker/postcheck chains and independently recomputes the archive-generation digest | upstream scientific replay is false and `s0_compatibility` is null |
| release builder | mock-only 53-input plus 15-publication-object DAG, exact 68 roles, build/idempotent-build/verify-only paths | accepts only `MOCK_MAIN_FREEZE`; formal release construction is unimplemented |

The formal CAPD C++ candidate and hardened one-cell branch transaction runtime
remain useful upstream implementation evidence, but the mock pipeline did not
execute the C++ evaluator and did not install a persistent binary.

## Independent hardening

The final implementation review did not treat hash closure as sufficient.  It
constructed coherent adversarial rebindings and required semantic rejection
at every authority boundary.  Review-driven repairs include:

1. exact claim-boundary checks for component and composite
   checker/postcheck objects, even when an attacker also updates dependent
   hashes;
2. deep null-status and authority validation of static proof/record and
   branch record payloads rather than trusting their manifests;
3. rejection of nested authority fields, hidden authoritative paths, changed
   roles, noncanonical payloads, and executing source bytes that differ from
   their mock-freeze bindings;
4. generation-wide captured-byte replay for both direct function APIs and CLI
   entry points; and
5. a post-release namespace gate under which the scheduler must refuse to
   reopen the sealed result root while leaving release bytes unchanged.

The independent nine-module focused replay reached 280 passing cases without
a new P0 after these repairs.  The final independent verdict was
`ACCEPT` with P0=0 and P1=0; its only P2 was the now-corrected documentation
count from 279 to 280.  This remains engineering evidence, not a freeze test
record.

## Final implementation evidence

| Gate | Result | Authority boundary |
|---|---:|---|
| branch independent checker focused suite | 32/32 pass | synthetic archive replay only |
| L3-A1 nine-module implementation suite | 280/280 pass | mock/non-licensing |
| complete Paper 02 pytest suite | 675/675 pass | repository regression; no scientific dispatch |
| final independent correctness review | ACCEPT; P0=0, P1=0 | implementation increment only; not `ACCEPT_FOR_FREEZE` |

Stable implementation hashes at final review:

| Object | SHA-256 |
|---|---|
| mock scheduler | `2db057a12e17aca95ed99e94e17cb025f1f188ee7e32c68084724b269f31060d` |
| synthetic branch evaluator | `8d712a48a5c25ba4aafa0ff76b36eca4b380693cc557bebc390aa70957463830` |
| static independent checker | `14ca70bcd9ffd068e97d2033cbd2516f0d7309b73ccecd26e28ba3eb4b27ddbc` |
| branch independent checker | `b5b1216e2abb4671cdb9159ecf2ed3348180b1224d28a93b900e7704b90c977c` |
| composite independent checker | `a9ed20304d1c7e6110f44b7e7342b0368201cf17fb9bdddb98237b0394182480` |
| mock release-provenance builder | `464bf20bd15774a0e2193652adf2b1bf464de3d0caaf52f00d59ce00329443ed` |
| full mock E2E test | `58e1eb452bc82c29c51a7c7897ea58362cbc288a1abe8fff612a0a4c29f4475f` |
| composite checker tests | `17e51bf822a1a9fbe0cfdf1d30729eb97bc3b007a0d256d6ada4ce11c84f2823` |
| release-provenance tests | `28170ba06a83b4d466fb7205d50c72017759ce28360ed292fe1d7a9175675c51` |

## Canonical absence checks

At this milestone all of the following canonical objects remain absent:

```text
results/r401_val_l3_all_slabs/
results/r401_val_l3_all_slabs.operational/
research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json
research/route_a_wave_trace/R401_VAL_L3_A1_FREEZE.json
research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_TESTS.json
research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_REVIEW.md
validated/bin/capd_r401_phase_branch_tube_mp_a1
```

All complete 204-cell and 68-role objects used by tests were created under
temporary test roots and were not copied into the canonical result namespace.

## Intended Git scope

The implementation increment is limited to the following code and tests:

```text
scripts/check_r401_val_l3_a1_static_independent.py
scripts/run_r401_val_l3_a1_all_slabs.py
scripts/mock_r401_val_l3_a1_branch_evaluator.py
scripts/check_r401_val_l3_a1_branch_independent.py
scripts/check_r401_val_l3_a1_composite_independent.py
scripts/build_r401_val_l3_a1_release_provenance.py
tests/test_r401_val_l3_a1_static_checker.py
tests/test_r401_val_l3_a1_branch_scheduler.py
tests/test_r401_val_l3_a1_branch_checker.py
tests/test_r401_val_l3_a1_composite_contract.py
tests/test_r401_val_l3_a1_release_provenance.py
tests/test_r401_val_l3_a1_adversarial_e2e.py
```

The documentation scope is exactly this file plus:

```text
research/route_a_wave_trace/refine-logs/A416_A1_PREFREEZE_TRACKER.md
research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md
research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md
```

The accepted S0-bound derivation, protocol, and L1 plan are read-only inputs
and are outside this change:

```text
research/route_a_wave_trace/A416_PHASE_FLOWBOX_DERIVATION.md
research/route_a_wave_trace/R401_VAL_L3_PHASE_TUBE_PROTOCOL_DRAFT.md
research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json
```

No result archive, binary, freeze, pre-freeze verdict, or S0 artifact belongs
in this Git increment.

## Remaining freeze blockers

- build and bind the persistent CAPD binary without treating the present
  temporary compile/link check as a machine record;
- perform separately authorized representative-only peak-RSS calibration;
- record the exact Python, Arb, CAPD, compiler, runtime-library, host, memory,
  storage, and filesystem binding in an L3-specific machine freeze;
- create the canonical S0 compatibility replay and formal pre-freeze test
  record;
- obtain an independent review containing the sole exact line
  `Verdict: ACCEPT_FOR_FREEZE`;
- generate the main freeze last; and
- obtain separate authorization before initialize-only or any scientific
  evaluator dispatch.

Until all of those gates close, the formal component, milestone, theorem, and
release statuses remain absent.

## Current decision

```text
full_mock_pipeline = COMPLETE
mock_matrix = 102_static_plus_102_branch
mock_release_roles = 68
mock_scientific_licensing_enabled = false
final_independent_review = ACCEPT_P0_0_P1_0
l3_a1_implementation_tests = 280/280
paper02_regression = 675/675
formal_pipeline_complete = false
canonical_result_exists = false
machine_freeze_exists = false
main_freeze_exists = false
accept_for_freeze = false
dispatch_authorized = false
milestone_status = null
theorem_status = null
final_status = null
```
