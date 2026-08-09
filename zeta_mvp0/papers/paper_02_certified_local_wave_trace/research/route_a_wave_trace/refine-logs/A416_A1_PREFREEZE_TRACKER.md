# A4.16 L3-A1 pre-freeze supplemental tracker

Updated: 2026-08-09 UTC

Baseline: `529697ce3feccf11d16f739d0e07d27a2d1c4d16`

Authority: **planning only / non-licensing / no dispatch**

This tracker is independent of the S0 experiment plan and tracker already
bound by the accepted representative composite.  It does not amend those
files.

| ID | Unit | State | Exit gate | Notes |
|---|---|---|---|---|
| A1-D00 | read-only L2/S0 architecture audit | COMPLETE | reuse/rewrite ledger and blocker list recorded | no evaluator dispatched |
| A1-D01 | prospective 102-cell design | COMPLETE / NON_LICENSING | exact two-component matrix, status contract, DAG, budgets, tests, and launch gates documented | `R401_VAL_L3_A1_PREFREEZE_DESIGN.md` |
| A1-D02 | independent implementation-design review | COMPLETE / NON_LICENSING | `ACCEPT_FOR_IMPLEMENTATION_DESIGN`; P0=0 and P1=0 | not `ACCEPT_FOR_FREEZE`; no evaluator dispatch authority |
| A1-I01 | formal static one-cell evaluator | TODO / BLOCKED | exact frozen ABI; no telemetry in canonical proof; all S0-compatible math tests pass | derive from S0 static core, not S0 main |
| A1-I02 | formal static transaction scheduler | TODO / BLOCKED | exact 102 matrix; atomic commit; resume/quarantine; write-once; mock tests pass | candidate 8 workers, not frozen |
| A1-I03 | no-import static checker + postcheck | TODO / BLOCKED | independent 102-cell replay, write-once `STATIC_POSTCHECK_STATUS.json`, and mutation suite pass | only checker may assign static component pass |
| A1-I04 | persistent formal CAPD evaluator | TODO / BLOCKED | source/build/binary/runtime hashes stable; closed production status ABI | no build inside result directory |
| A1-I05 | formal branch transaction scheduler | TODO / BLOCKED | process-group timeout, atomic cells, exact resume and resource pause tests pass | candidate 6 workers, not frozen |
| A1-I06 | no-import branch checker + postcheck | TODO / BLOCKED | exact phase cover, exact-rational slow-radius replay, and write-once `BRANCH_POSTCHECK_STATUS.json` pass | checker is not a second ODE integration |
| A1-I07 | composite checker + postcheck | TODO / BLOCKED | both 102-cell component checker/postcheck chains plus L1/A4.15 chains bind exactly | sole owner of `PASS_LOCAL_PHASE_TUBE_ALL_SLABS`; final `POSTCHECK_STATUS.json` is separate |
| A1-I08 | S0-to-A1 compatibility replay | TODO / BLOCKED | six accepted cells replay without changing S0 facts or authority | read-only accepted archive |
| A1-I09 | release-provenance builder | TODO / BLOCKED | write-once/verify-only exact DAG and adversarial tests pass | no self-hash, null final value |
| A1-T01 | full mocked 102-cell E2E | TODO / BLOCKED | 102 static + 102 branch synthetic cells close through release | no scientific evaluator dispatch |
| A1-T02 | crash/resume/quarantine suite | TODO / BLOCKED | every transaction boundary and binding mismatch covered | whole-generation nonmixing |
| A1-T03 | strict schema/path/TOCTOU suite | TODO / BLOCKED | duplicate/type/nonfinite/path/link/mutation cases fail closed | adapt accepted L2 patterns |
| A1-R01 | representative-only peak-RSS calibration | UNAUTHORIZED | separate instruction; S0 cells only; recorded before worker freeze | no held-out slab allowed |
| A1-P01 | formal L3-A1 protocol/contracts | TODO / BLOCKED | final exact bytes and claim boundary independently reviewed | do not edit S0-bound protocol |
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
| static maximum nodes per cell | 1,000,000 | must be made explicit and race-tested |
| static cell timeout | 1,800 s | operational headroom only |
| static workers | 8 | separate processes; mock and memory gates pending |
| branch phase cells | 64 | exact S0 phase cover |
| branch Taylor order | 24 | exact S0 evaluator value |
| branch tolerance 128/256 | `1e-30` / `1e-60` | must be stated exactly in formal protocol |
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

- B1--B6: no formal static/branch evaluators, transaction scheduler,
  102-cell checkers, compatibility adapter, or unambiguous static cell cap.
- B7--B8: no peak-RSS calibration and no L3-specific machine freeze.
- B9--B10: production failure vocabulary and A4.15 release binding are not
  implemented.
- B11--B12: no full mock/fault/release suite, independent pre-freeze review,
  or main freeze.

## Current decision

```text
next_authorized_action = IMPLEMENT_AND_MOCK_TEST_STATIC_CELL_CHAIN
independent_design_review_complete = true
accept_for_freeze = false
representative_evaluator_dispatch = false
held_out_evaluator_dispatch = false
all_slab_evaluator_dispatch = false
dispatch_authorized = false
milestone_status = null
theorem_status = null
final_status = null
```
