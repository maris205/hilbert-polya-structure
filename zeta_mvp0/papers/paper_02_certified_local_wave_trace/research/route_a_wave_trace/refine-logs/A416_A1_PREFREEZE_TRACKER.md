# A4.16 L3-A1 pre-freeze supplemental tracker

Updated: 2026-08-09 UTC

Design baseline: `529697ce3feccf11d16f739d0e07d27a2d1c4d16`

Implementation baseline: `04f2d8841fa4309bc3460c91f7a7389268332f98`

Authority: **engineering implementation increment only / non-licensing / no dispatch**

`scientific_licensing_enabled = false`; `milestone_status`,
`theorem_status`, and `final_status` remain null.

This tracker is independent of the S0 experiment plan and tracker already
bound by the accepted representative composite.  It does not amend those
files.

| ID | Unit | State | Exit gate | Notes |
|---|---|---|---|---|
| A1-D00 | read-only L2/S0 architecture audit | COMPLETE | reuse/rewrite ledger and blocker list recorded | no evaluator dispatched |
| A1-D01 | prospective 102-cell design | COMPLETE / NON_LICENSING | exact two-component matrix, status contract, DAG, budgets, tests, and launch gates documented | `R401_VAL_L3_A1_PREFREEZE_DESIGN.md` |
| A1-D02 | independent implementation-design review | COMPLETE / NON_LICENSING | `ACCEPT_FOR_IMPLEMENTATION_DESIGN`; P0=0 and P1=0 | not `ACCEPT_FOR_FREEZE`; no evaluator dispatch authority |
| A1-I01 | formal static one-cell evaluator | COMPLETE / IMPLEMENTATION CANDIDATE / NON_LICENSING | exact candidate ABI, four-tree order, single-snapshot L1 binding, closed status table, tree/cell budgets, no canonical telemetry, and write-once proof implemented | independent implementation review: P0=0, P1=0; no scientific dispatch |
| A1-I02 | formal static transaction scheduler | PARTIAL / MOCK_ONLY_NON_LICENSING | exact 102-cell static matrix, no-replace cell/manifest commits, resume, retained staging, whole-generation quarantine, and mock aggregate implemented | production dispatch remains unconditionally fail-closed; two-component scheduler absent |
| A1-I03 | no-import static checker + postcheck | PARTIAL / PROOF_CORE_ONLY | independent proof/tree mathematics, frozen resource caps, upstream release chain, paths, and source bindings replayed | full 102-cell aggregate checker and `STATIC_POSTCHECK_STATUS.json` remain absent |
| A1-I04 | persistent formal CAPD evaluator | PARTIAL / SOURCE_AND_BUILD_CHECK_ONLY | closed branch evaluator ABI and formal C++ source implemented; pinned CAPD compile/link passes with warnings as errors | persistent binary, machine/runtime binding, and production build record absent |
| A1-I05 | formal branch transaction scheduler | PARTIAL / REVIEWED_RUNTIME_CORE / NON_LICENSING | bounded streams, process-group and adopted-child cleanup, pinned executable, exact locks/staging, signal-safe ownership, resume, no-replace publication, and fail-closed guard deadline pass 74 focused tests | independent reliability review: P0=0, P1=0; 102-cell branch scheduler/aggregate still absent |
| A1-I06 | no-import branch checker + postcheck | TODO / BLOCKED | exact phase cover, exact-rational slow-radius replay, and write-once `BRANCH_POSTCHECK_STATUS.json` pass | checker is not a second ODE integration |
| A1-I07 | composite checker + postcheck | TODO / BLOCKED | both 102-cell component checker/postcheck chains plus L1/A4.15 chains bind exactly | sole owner of `PASS_LOCAL_PHASE_TUBE_ALL_SLABS`; final `POSTCHECK_STATUS.json` is separate |
| A1-I08 | S0-to-A1 compatibility replay | COMPLETE / NON_LICENSING_COMPATIBILITY | exact six accepted cells, 26 branch roles, 18 composite bindings, and nine sealed controls replay read-only; 31 focused tests pass | canonical replay object intentionally absent; no S0 bytes or authority changed |
| A1-I09 | release-provenance builder | TODO / BLOCKED | write-once/verify-only exact DAG and adversarial tests pass | no self-hash, null final value |
| A1-T01 | full mocked 102-cell E2E | PARTIAL / STATIC_102_MOCK_ONLY | the static 102-cell mock closes through its aggregate | 102 branch cells, both component postchecks, composite, and release remain missing |
| A1-T02 | crash/resume/quarantine suite | PARTIAL | implemented static and branch transaction boundaries, signal/lock faults, resume, quarantine, and nonmixing cases have focused coverage | complete two-component generation and release fault suite remains missing |
| A1-T03 | strict schema/path/TOCTOU suite | PARTIAL | current static, branch-runtime, and S0-adapter surfaces reject duplicate/type/nonfinite/path/link/inode/snapshot mutations | future branch/composite/release surfaces remain untested |
| A1-R01 | representative-only peak-RSS calibration | UNAUTHORIZED | separate instruction; S0 cells only; recorded before worker freeze | no held-out slab allowed |
| A1-P01 | formal L3-A1 protocol/contracts | COMPLETE AS PROSPECTIVE CONTRACT SET / NON_LICENSING | four prospective contracts and exact candidate 53-input/68-release role maps exist | not a freeze review and not dispatch authority; do not edit S0-bound protocol |
| A1-F01 | L3 machine freeze | TODO / BLOCKED | Python/Arb, CAPD, persistent binary, runtime, host, storage all bound | old L2 machine freeze is template only |
| A1-P02 | independent pre-freeze review | TODO / BLOCKED | sole exact line `Verdict: ACCEPT_FOR_FREEZE` | reviewer must be independent of final producer/checker authorship |
| A1-F02 | main L3-A1 freeze | PROHIBITED | all prior rows through A1-P02 complete; freeze generated last | current repository has no dispatch authority |
| A1-L00 | initialize-only run config | PROHIBITED | exact main freeze exists and handshake passes without evaluator launch | first post-freeze action |
| A1-L01 | held-out/all-slab production | PROHIBITED | explicit later authorization after initialize-only audit | do not dispatch now |
| A1-G01 | global tube routing | OPEN / SEPARATE | independent global complement theorem | not part of L3-A1 production |
| A1-HP | trace / Hilbert--Polya / zeta / RH promotion | UNAUTHORIZED | separate later theorems | `final_status` remains null |

## Candidate budget register

None of these values is frozen.

| Resource | Candidate | Evidence or unresolved gate |
|---|---:|---|
| static maximum depth per tree | 24 | S0 maximum 14 |
| static maximum nodes per tree | 250,000 | S0 implementation value |
| static maximum nodes per cell | 1,000,000 | explicit in the prospective protocol and implementation; focused limit tests pass; not frozen |
| static cell timeout | 1,800 s | operational headroom only |
| static workers | 8 | separate processes; mock and memory gates pending |
| branch phase cells | 64 | exact S0 phase cover |
| branch Taylor order | 24 | exact S0 evaluator value |
| branch tolerance 128/256 | `1e-30` / `1e-60` | stated exactly in the prospective protocol; persistent binary and machine binding pending |
| branch cell timeout | 600 s | exact S0 runner value |
| branch workers | 6 | S0 concurrency; peak RSS still missing |
| branch stdout / stderr cap | 16 MiB / 1 MiB | bounded streaming required; process group terminated on exhaustion |
| branch record / total-cell cap | 4 MiB / 32 MiB | authoritative record and complete cell remain separately bounded |
| memory admission pause | 48 GiB | 60-GiB cgroup; representative calibration pending |
| memory reserve | 8 GiB | required in the pre-freeze worker-admission inequality |
| launch free storage | 200 GiB | about 347 GiB observed during design audit |
| storage warning / pause / recovery | 180 / 150 / 120 GiB | operational only |
| global scientific budget | `null` | resource exhaustion is inconclusive |

## Current blockers

- The static aggregate checker/postcheck and the 102-cell branch
  scheduler/aggregate/checker/postcheck do not yet exist.
- The composite checker/postcheck, release-provenance builder, and complete
  102-static plus 102-branch mock E2E do not yet exist.
- The persistent CAPD binary, representative peak-RSS calibration, complete
  Python/Arb/CAPD runtime binding, and L3-specific machine freeze are absent.
- No formal pre-freeze test record or independent `ACCEPT_FOR_FREEZE` review
  exists.  Main freeze generation and every scientific dispatch remain
  prohibited.

## Current decision

```text
next_authorized_action = IMPLEMENT_COMPONENT_AGGREGATES_CHECKERS_AND_POSTCHECKS
independent_design_review_complete = true
static_implementation_increment_review = ACCEPT_P0_0_P1_0
branch_runtime_increment_review = ACCEPT_P0_0_P1_0
s0_compatibility_increment_review = ACCEPT_NON_LICENSING
accept_for_freeze = false
representative_evaluator_dispatch = false
held_out_evaluator_dispatch = false
all_slab_evaluator_dispatch = false
dispatch_authorized = false
milestone_status = null
theorem_status = null
final_status = null
```
