# A4.16 L3-A1 pre-freeze supplemental tracker

Updated: 2026-08-10 UTC

Design baseline: `529697ce3feccf11d16f739d0e07d27a2d1c4d16`

Implementation baseline before this working-tree increment: `e010200`

Authority: **engineering implementation increment only / non-licensing / no dispatch**

`scientific_licensing_enabled = false`; `milestone_status`,
`theorem_status`, and `final_status` remain null.

Latest formal-control-plane implementation review: **ACCEPT; P0=0, P1=0,
P2=0**.  This is an implementation verdict only.  The exact machine/main
freeze schemas and the independent pre-freeze scientific authorization have
not been completed.

This tracker is independent of the S0 experiment plan and tracker already
bound by the accepted representative composite.  It does not amend those
files.

| ID | Unit | State | Exit gate | Notes |
|---|---|---|---|---|
| A1-D00 | read-only L2/S0 architecture audit | COMPLETE | reuse/rewrite ledger and blocker list recorded | no evaluator dispatched |
| A1-D01 | prospective 102-cell design | COMPLETE / NON_LICENSING | exact two-component matrix, status contract, DAG, budgets, tests, and launch gates documented | `R401_VAL_L3_A1_PREFREEZE_DESIGN.md` |
| A1-D02 | independent implementation-design review | COMPLETE / NON_LICENSING | `ACCEPT_FOR_IMPLEMENTATION_DESIGN`; P0=0 and P1=0 | not `ACCEPT_FOR_FREEZE`; no evaluator dispatch authority |
| A1-I01 | formal static one-cell evaluator | COMPLETE / IMPLEMENTATION CANDIDATE / NON_LICENSING | exact candidate ABI, four-tree order, single-snapshot L1 binding, closed status table, tree/cell budgets, no canonical telemetry, and write-once proof implemented | independent implementation review: P0=0, P1=0; no scientific dispatch |
| A1-I02 | formal static transaction scheduler | COMPLETE FOR MOCK + FORMAL PREFLIGHT IMPLEMENTATION CANDIDATE / CANONICAL PROHIBITED | exact 102-cell mock path plus a 53-role same-byte formal handshake, temporary initialize-only binding, exact 26-string static pure plan, atomic no-replace preflight publication, and 102-only nonpromotable aggregate candidates implemented | no formal cell or aggregate publication; production dispatch remains unconditionally fail-closed |
| A1-I03 | no-import static checker + postcheck | COMPLETE FOR MOCK / NON_LICENSING | full 102-cell proof/record/manifest replay, aggregate-root closure, cross-precision mock gates, write-once checker, and `STATIC_POSTCHECK_STATUS.json` implemented | mock pass assigns no component, milestone, theorem, or final status |
| A1-I04 | persistent formal CAPD evaluator | PARTIAL / IMPLEMENTATION CANDIDATE / CANONICAL PROHIBITED | closed branch evaluator ABI and formal C++ source implemented; pinned CAPD compile/link passes with warnings as errors; formal-source RSS calibration on six public S0 inputs is complete | calibration binary was temporary and uninstalled; canonical A1 persistent binary, exact production build record, and machine/runtime binding remain absent |
| A1-I05 | formal branch transaction scheduler | COMPLETE FOR MOCK + FORMAL PURE-PLAN CANDIDATE / CANONICAL PROHIBITED / NON_LICENSING | reviewed bounded one-cell runtime, exact 102-cell L1-derived mock matrix, six-cell barriers, resume, mock aggregate publication, and a persistent-binary-bound formal pure plan implemented | the formal runner is never called; canonical A1 persistent binary and machine binding remain absent |
| A1-I06 | no-import branch checker + postcheck | COMPLETE FOR MOCK / NON_LICENSING | exact L1 chain, raw/record/manifest, 64-phase, rational tube-implication, aggregate-root, and cross-precision replay plus write-once `BRANCH_POSTCHECK_STATUS.json` implemented | synthetic transcript replay is not a second ODE integration and licenses no tube theorem |
| A1-I07 | composite checker + postcheck | COMPLETE FOR MOCK / NON_LICENSING | both 102-cell component checker/postcheck chains, exact aggregate roots, composite controls, generation binding, write-once checker, and `POSTCHECK_STATUS.json` replayed | mock composite keeps component/milestone/theorem/final null; formal scientific promotion remains absent |
| A1-I08 | S0-to-A1 compatibility replay | COMPLETE / NON_LICENSING_COMPATIBILITY | exact six accepted cells, 26 branch roles, 18 composite bindings, and nine sealed controls replay read-only; 31 focused tests pass | canonical replay object intentionally absent; no S0 bytes or authority changed |
| A1-I09 | release-provenance builder | COMPLETE FOR MOCK / FORMAL BLOCKED / NON_LICENSING | exact mock 53-input plus 15-publication-object DAG, deep payload/status/claim/source replay, write-once build, idempotent identical build, and verify-only path implemented | accepts only `MOCK_MAIN_FREEZE`; canonical production release remains unimplemented and fail-closed |
| A1-T01 | full mocked 204-cell E2E | COMPLETE / MOCK_ONLY_NON_LICENSING | 102 static cells, static checker/postcheck, 102 branch cells, branch checker/postcheck, composite controls/checker/postcheck, and exact 68-role mock release close in a temporary project | no canonical result root or scientific artifact was published |
| A1-T02 | crash/resume/quarantine suite | COMPLETE FOR MOCK ENGINEERING SCOPE | static/branch transaction boundaries, signal/lock faults, partial-to-full resume, whole-generation quarantine, post-release scheduler refusal, and write-once release recovery have adversarial coverage | formal production recovery remains subject to a future freeze and machine binding |
| A1-T03 | strict schema/path/TOCTOU suite | COMPLETE FOR CURRENT MOCK SURFACES | static, branch, composite, and release paths reject duplicate/type/nonfinite/path/link/inode/snapshot, coherent rebind, nested-authority, and claim-boundary mutations | this does not validate absent formal production artifacts |
| A1-R01 | representative-only peak-RSS calibration | COMPLETE / FORMAL SOURCE ON PUBLIC S0 INPUTS ONLY / NON_LICENSING | six public S0 jobs ran through a temporary binary compiled from the formal A1 source with exact source/binary/CAPD toolchain hashes; worst peak RSS `202428 KiB`; six-worker candidate inequality `24339234816 < 51539607552` bytes | no held-out or all-slab input was used; temporary binary was not installed and the canonical calibration object is absent |
| A1-P01 | formal L3-A1 protocol/contracts | COMPLETE AS PROSPECTIVE CONTRACT SET / NON_LICENSING | four prospective contracts and exact candidate 53-input/68-release role maps exist | not a freeze review and not dispatch authority; do not edit S0-bound protocol |
| A1-F01 | L3 machine freeze | TODO / BLOCKED | Python/Arb, CAPD, persistent binary, runtime, host, storage all bound | old L2 machine freeze is template only |
| A1-P02 | independent pre-freeze review | TODO / BLOCKED | sole exact line `Verdict: ACCEPT_FOR_FREEZE` | reviewer must be independent of final producer/checker authorship |
| A1-F02 | main L3-A1 freeze | PROHIBITED | all prior rows through A1-P02 complete; freeze generated last | current repository has no dispatch authority |
| A1-L00 | initialize-only run config | COMPLETE AS TEMPORARY IMPLEMENTATION CANDIDATE / CANONICAL PROHIBITED | a disposable authority fixture passes the exact ordered 53-role same-byte handshake and atomically publishes one nonresumable, nonpromotable `run_config.json` outside every canonical namespace | not the future production run config; canonical initialize-only remains prohibited until exact schemas/contracts, persistent binary, machine freeze, and independent review exist |
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
| branch workers | 6 | formal-source calibration on six public S0 inputs complete; no held-out work; still a candidate until machine freeze |
| branch stdout / stderr cap | 16 MiB / 1 MiB | bounded streaming required; process group terminated on exhaustion |
| branch record / total-cell cap | 4 MiB / 32 MiB | authoritative record and complete cell remain separately bounded |
| memory admission pause | 48 GiB | exact candidate arithmetic passes: baseline `14505582592` + `6 x 207286272` + reserve `8589934592` = `24339234816 < 51539607552` bytes, leaving `27200372736` bytes headroom; worst public-S0 input job `202428 KiB`; not frozen |
| memory reserve | 8 GiB | required in the pre-freeze worker-admission inequality |
| launch free storage | 200 GiB | about 347 GiB observed during design audit |
| storage warning / pause / recovery | 180 / 150 / 120 GiB | operational only |
| global scientific budget | `null` | resource exhaustion is inconclusive |

## Current blockers

- The full 204-cell mock transaction/checker/composite/release chain now
  exists only as an engineering implementation and temporary test replay.  It
  is not a formal scientific generation and does not license one.
- Representative-only RSS calibration is complete, but the canonical A1
  persistent CAPD binary, complete Python/Arb/CAPD runtime binding, exact
  production schemas/contracts, and L3-specific machine freeze are absent.
- The canonical compatibility replay, production result root, production
  report, formal release, and all formal component/composite statuses remain
  absent; the implemented formal entry paths fail closed.
- No formal pre-freeze test record or independent `ACCEPT_FOR_FREEZE` review
  exists.  Main freeze generation and every scientific dispatch remain
  prohibited.

## Final mock implementation evidence

| Gate | Result | Boundary |
|---|---:|---|
| branch checker focused | 32/32 pass | synthetic branch archive only |
| L3-A1 nine-module suite | 280/280 pass | full mock engineering chain |
| Paper 02 regression | 675/675 pass | no scientific evaluator dispatch |
| independent implementation review | ACCEPT; P0=0, P1=0 | not `ACCEPT_FOR_FREEZE` |

The review's sole P2 was the stale intermediate documentation count 279; the
final count is 280.  Stable implementation hashes and the exact Git scope are
recorded in `../A416_L3_A1_FULL_MOCK_PIPELINE.md`.

## Formal preflight and calibration evidence

| Gate | Result | Boundary |
|---|---:|---|
| formal scheduler focused suite | 79/79 pass | preflight/control plane only; no evaluator |
| owned L3-A1 implementation suite | 194/194 pass | mock plus non-dispatch formal implementation surfaces |
| Paper 02 regression | 710/710 pass | no scientific dispatch and no canonical publication |
| independent formal-control-plane review | ACCEPT; P0=0, P1=0, P2=0 | implementation verdict only; not a freeze or theorem decision |
| formal-source RSS calibration on public S0 inputs | 6/6 jobs recorded | representative resource calibration; worst `202428 KiB`; no held-out input; temporary binary uninstalled |

Stable formal-preflight source hashes are:

```text
scheduler_sha256 = e39caaed78468be1dc7791efde5b85f97668e07ef7117a7c2560decfea7d06bf
scheduler_test_sha256 = 41655000a7904547f80aadf1726c01f1392239c1e1dea94394df6931e41ad508
```

The calibration used the formal A1 source SHA-256
`66588bf25ae777c854f60a747af4299e3166efdd51db2659e33a28194abc59c5`
and temporary binary SHA-256
`25aec3d7d68883c2a97f765682a40cabc3feb91f159f67ac2910b6f82025e521`.
Its CAPD commit was `731079217a9254ea2948d742df2b170895effe7f`;
the `capd-config`, ordered flags, `libcapd.a`, and `libfilib.a` hashes were,
respectively,
`c758bc9101beb9c633817b0402df9168c6dea9f652d36833101af3273c50338a`,
`f55b78c25c899b2a8040719240dc309e58f65f99468479e47260acb1cc4315de`,
`970088d4ba5024c1b59124299d5e46df41f19936ba53446a5a40a0671968b086`,
and
`51c40a22a2405faec793d97a0396022212d7a32f4cca4bf38b994adacaf9be85`.
The temporary calibration JSON had SHA-256
`2cd389315867cff7598c2977543a8e1f3d0a3dc60d99b51f1e7826f9f95af99a`.
Neither it nor the temporary binary was installed as a canonical object.

The canonical machine freeze, main freeze, S0 compatibility replay, A1
persistent binary, production result root, and operational root remain
absent.  The exact implementation record is
`../A416_L3_A1_FORMAL_PREFLIGHT_INCREMENT.md`.

## Current decision

```text
next_authorized_action = FINALIZE_EXACT_SCHEMAS_AND_CONTRACTS_THEN_BUILD_PERSISTENT_BINARY_AND_MACHINE_FREEZE
independent_design_review_complete = true
static_implementation_increment_review = ACCEPT_P0_0_P1_0
branch_runtime_increment_review = ACCEPT_P0_0_P1_0
s0_compatibility_increment_review = ACCEPT_NON_LICENSING
full_204_cell_mock_pipeline = PASS_MOCK_ONLY_NON_LICENSING
mock_68_role_release_replay = PASS_MOCK_PROVENANCE_REPLAY
full_mock_pipeline_review = ACCEPT_P0_0_P1_0
l3_a1_implementation_tests = 280/280
formal_control_plane_implementation_review = ACCEPT_P0_0_P1_0_P2_0
formal_scheduler_focused_tests = 79/79
formal_preflight_owned_tests = 194/194
paper02_regression = 710/710
representative_rss_calibration = COMPLETE_FORMAL_SOURCE_ON_PUBLIC_S0_INPUTS_6_JOBS
canonical_initialize_only = false
formal_pipeline_complete = false
accept_for_freeze = false
representative_evaluator_dispatch = false
held_out_evaluator_dispatch = false
all_slab_evaluator_dispatch = false
dispatch_authorized = false
milestone_status = null
theorem_status = null
final_status = null
```
