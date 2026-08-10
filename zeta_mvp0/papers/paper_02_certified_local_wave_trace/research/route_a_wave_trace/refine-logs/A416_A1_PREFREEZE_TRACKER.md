# A4.16 L3-A1 pre-freeze supplemental tracker

Updated: 2026-08-10 UTC

Design baseline: `529697ce3feccf11d16f739d0e07d27a2d1c4d16`

Implementation baseline before this working-tree increment: `e010200`

Authority: **engineering implementation increment only / NON_LICENSING / no
machine freeze / no main freeze / no dispatch / no canonical results**

`scientific_licensing_enabled = false`; `milestone_status`,
`theorem_status`, and `final_status` remain null.

Latest machine-binding and formal-schema engineering cross-review: **ACCEPT;
P0=0, P1=0, P2=0**.  This is an implementation verdict only, not
`ACCEPT_FOR_FREEZE`.  Exact candidate schemas and independent validators now
exist.  Role 19 now also has a temp-only capture candidate and role 24 has a
zero-write, zero-subprocess independent verify-only path, but no canonical
role-10 machine freeze, role-54 main freeze, or independent pre-freeze
scientific authorization exists.

The temp-capture and independent-verifier evidence is stable after the
subreaper/group-wait repair: the two focused modules pass `201/201`, the
nine-module regression passes `457/457`, and `24/24` parallel timeout replays
pass with the caller's subreaper state restored.  The pre-repair `456` pass,
`1` fail run and its candidates are withdrawn.  This remains engineering
evidence only and grants no role-10 publication or dispatch authority.

This tracker is independent of the S0 experiment plan and tracker already
bound by the accepted representative composite.  It does not amend those
files.

| ID | Unit | State | Exit gate | Notes |
|---|---|---|---|---|
| A1-D00 | read-only L2/S0 architecture audit | COMPLETE | reuse/rewrite ledger and blocker list recorded | no evaluator dispatched |
| A1-D01 | prospective 102-cell design | COMPLETE / NON_LICENSING | exact two-component matrix, status contract, DAG, budgets, tests, and launch gates documented | `R401_VAL_L3_A1_PREFREEZE_DESIGN.md` |
| A1-D02 | independent implementation-design review | COMPLETE / NON_LICENSING | `ACCEPT_FOR_IMPLEMENTATION_DESIGN`; P0=0 and P1=0 | not `ACCEPT_FOR_FREEZE`; no evaluator dispatch authority |
| A1-I01 | formal static one-cell evaluator | COMPLETE / IMPLEMENTATION CANDIDATE / NON_LICENSING | exact 26-string ABI, four-tree order, single-snapshot L1 binding, closed status table, strict `CJ_COMPACT_V1`, tree/cell budgets, and write-once proof implemented | no scientific dispatch |
| A1-I02 | formal static transaction scheduler | COMPLETE AS EXACT-SCHEMA IMPLEMENTATION CANDIDATE / CANONICAL PROHIBITED | exact 102-cell mock path plus 53-role same-byte formal handshake, closed machine/main/run/cell/aggregate schemas, exact static plan, atomic no-replace preflight publication, and nonpromotable aggregate candidates implemented | no formal cell or aggregate publication; production dispatch remains fail-closed |
| A1-I03 | no-import static checker + postcheck | COMPLETE FOR MOCK + FORMAL FOUR-FILE REPLAY CANDIDATE / NON_LICENSING | exact `proof.json`, `stdout.txt`, `stderr.txt`, `record.json` replay; strict proof/record/manifest bindings; `STATIC_PROOF_ABSENT`; aggregate-root closure; cross-precision gates; and postcheck implemented | nonpass is never component-eligible; no formal promotion |
| A1-I04 | persistent formal CAPD evaluator | COMPLETE AS PERSISTENT IMPLEMENTATION INPUT / NON_LICENSING | deterministic rebuild and install at `validated/bin/capd_r401_phase_branch_tube_mp_a1`; SHA-256 `25aec3d7...25e521`, size `2419064`, mode `0755`, build ID `3cff449e...ba386`; exact public-calibration byte transfer | binary existence is not a machine freeze, result, or dispatch authority |
| A1-I05 | formal branch transaction scheduler | COMPLETE FOR MOCK + FORMAL PURE-PLAN CANDIDATE / CANONICAL PROHIBITED / NON_LICENSING | reviewed bounded runtime, exact 102-cell L1-derived matrix, six-cell barriers, resume, aggregate publication, persistent-binary-bound pure plan, and exact millisecond budgets implemented | `600000/2000/1000` ms; formal dispatcher remains fail-closed |
| A1-I06 | no-import branch checker + postcheck | COMPLETE FOR MOCK + STRICT-SERIALIZER CANDIDATE / NON_LICENSING | exact L1 chain, pretty-byte task/argv/record/manifest digest replay, 64-phase rational tube implication, aggregate root, cross-precision replay, and postcheck implemented | `CJ_PRETTY_2_V1`; synthetic transcript replay is not a second ODE integration and licenses no tube theorem |
| A1-I07 | composite checker + postcheck | COMPLETE FOR MOCK + FORMAL-SHAPED REPLAY / NON_LICENSING | both 102-cell component chains, exact aggregate roots, millisecond branch limits, strict serializer bindings, composite controls, generation binding, checker, and postcheck replayed | component/milestone/theorem/final remain null; formal scientific promotion absent |
| A1-I08 | S0-to-A1 compatibility replay | COMPLETE / NON_LICENSING_COMPATIBILITY | exact six accepted cells, 26 branch roles, 18 composite bindings, and nine sealed controls replay read-only; 31 focused tests pass | canonical replay object intentionally absent; no S0 bytes or authority changed |
| A1-I09 | release-provenance builder and independent machine validator | COMPLETE FOR MOCK + EXACT FORMAL VALIDATION CANDIDATE / NON_LICENSING | mock 53-input release replay plus producer-independent exact machine validation of live Python/Conda/Arb, CAPD/compiler/ELF/runtime, embedded resource bytes, admission arithmetic, and filesystem bindings | no canonical machine receipt or release; formal publication remains fail-closed |
| A1-I10 | deterministic temp-only machine capture + independent verify-only CLI | COMPLETE AS NON-AUTHORITATIVE ENGINEERING SURFACE / CANONICAL PROHIBITED / NON_LICENSING | role 19 can capture a compact candidate at a new `/tmp` path, perform one owned fresh argv-list build with `shell=false`, and prove no-overwrite equality to role 17; role 24 replays exact bytes and live bindings with zero writes and zero subprocesses | no canonical role 10, role 54, run config, result, publication, promotion, or scientific dispatch |
| A1-T01 | full mocked 204-cell E2E | COMPLETE / MOCK_ONLY_NON_LICENSING | 102 static cells, static checker/postcheck, 102 branch cells, branch checker/postcheck, composite controls/checker/postcheck, and exact 68-role mock release close in a temporary project | no canonical result root or scientific artifact was published |
| A1-T02 | crash/resume/quarantine suite | COMPLETE FOR MOCK ENGINEERING SCOPE | static/branch transaction boundaries, signal/lock faults, partial-to-full resume, whole-generation quarantine, post-release scheduler refusal, and write-once release recovery have adversarial coverage | formal production recovery remains subject to a future freeze and machine binding |
| A1-T03 | strict schema/path/TOCTOU suite | COMPLETE FOR CURRENT MOCK SURFACES | static, branch, composite, and release paths reject duplicate/type/nonfinite/path/link/inode/snapshot, coherent rebind, nested-authority, and claim-boundary mutations | this does not validate absent formal production artifacts |
| A1-R01 | public-only peak-RSS calibrations | COMPLETE AS TEMPORARY RESOURCE EVIDENCE / NON_LICENSING | final static payload `8afc8a0a...22de92`: 14/14 exact 26-string runs and eight-worker inequality `33960800256 < 51539607552`; branch payload `2cd38931...af99a`: 6/6 exact 12-string runs and persistent-binary transfer | public `S000/S025/S050 x 128/256` only; final static payload remains in `/tmp`; no canonical calibration object |
| A1-P01 | formal L3-A1 protocol/contracts | COMPLETE AS EXACT IMPLEMENTATION CONTRACT SET / NON_LICENSING | exact machine/main/run/cell/aggregate/checker/release schemas, serializer definitions, candidate 53-input/68-release role maps, and fail-closed execution policy exist | not a freeze review and not dispatch authority; do not edit S0-bound protocol |
| A1-F01 | canonical L3 machine input | PARTIAL / CANONICAL ROLE 10 PROHIBITED | under separate authorization, publish byte-identical independently verified candidate bytes once as role 10 and complete the final input audit | temp capture/verify exists, but no canonical machine object exists; old L2 freeze is template only |
| A1-P02 | independent pre-freeze review | TODO / BLOCKED | sole exact line `Verdict: ACCEPT_FOR_FREEZE` | reviewer must be independent of final producer/checker authorship |
| A1-F02 | main L3-A1 freeze | PROHIBITED | all 53 ordered inputs are final; main freeze is then generated as downstream role 54 | current repository has no dispatch authority |
| A1-L00 | initialize-only run config | COMPLETE AS TEMPORARY IMPLEMENTATION CANDIDATE / CANONICAL PROHIBITED | a disposable authority fixture passes the exact ordered 53-role same-byte handshake and atomically publishes one nonresumable, nonpromotable `run_config.json` outside every canonical namespace | not the future production run config; canonical initialize-only remains prohibited until the deterministic machine freeze and independent review chain exist |
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
| static workers | 8 | final public-only stress calibration complete; still a candidate until machine freeze |
| branch phase cells | 64 | exact S0 phase cover |
| branch Taylor order | 24 | exact S0 evaluator value |
| branch tolerance 128/256 | `1e-30` / `1e-60` | stated exactly in the protocol; persistent binary exists, machine freeze pending |
| branch cell timeout | `600000 ms` | exact millisecond schema; runtime converts only at the wait boundary |
| branch workers | 6 | formal-source calibration on six public S0 inputs complete; no held-out work; still a candidate until machine freeze |
| branch stdout / stderr cap | 16 MiB / 1 MiB | bounded streaming required; process group terminated on exhaustion |
| branch record / total-cell cap | 4 MiB / 32 MiB | authoritative record and complete cell remain separately bounded |
| memory admission pause | 48 GiB | final static candidate: `24891273216 + 8 x 59949056 + 8589934592 = 33960800256 < 51539607552`, headroom `17578807296`; branch public evidence separately records `14505582592 + 6 x 207286272 + 8589934592 = 24339234816`; future machine receipt must recompute both from one conservative observed baseline; not frozen |
| memory reserve | 8 GiB | required in the pre-freeze worker-admission inequality |
| launch free storage | 200 GiB | about 347 GiB observed during design audit |
| storage warning / pause / recovery | 180 / 150 / 120 GiB | operational only |
| global scientific budget | `null` | resource exhaustion is inconclusive |

## Current blockers

- The full 204-cell mock transaction/checker/composite/release chain now
  exists only as an engineering implementation and temporary test replay.  It
  is not a formal scientific generation and does not license one.
- Exact schemas, the persistent CAPD binary, both public-only resource
  payloads, the role-19 temp-only capture path, and role-24 read-only verifier
  now exist as engineering inputs.  A temporary candidate is not input role
  10; separately authorized canonical no-replace publication and the rest of
  the 53-input freeze chain remain absent.
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

The canonical machine freeze, main freeze, S0 compatibility replay,
production result root, and operational root remain absent.  The exact
preflight implementation record is
`../A416_L3_A1_FORMAL_PREFLIGHT_INCREMENT.md`.

## Machine-binding and exact-schema increment evidence

| Gate | Result | Boundary |
|---|---:|---|
| final public-only static calibration | 14/14 pass | six sequential plus eight concurrent public S0 cells; exact 26-string ABI; no held-out input |
| persistent branch binary transfer | exact SHA-256 match | public branch calibration binary and installed persistent binary both `25aec3d7...25e521` |
| core regression immediately before final embedded branch resource binary-digest/persistent-binary binding | 419/419 pass | precise pre-binding evidence |
| complete Paper 02 regression at the machine-binding increment bytes | 814/814 pass | historical machine-binding integration evidence; no scientific dispatch |
| independent machine/schema cross-review | ACCEPT; P0=0, P1=0, P2=0 | engineering correctness only; not `ACCEPT_FOR_FREEZE` |

The final static resource byte image is
`/tmp/a416-l3a1-static-rss-final.4CBiaA/static_calibration.json`, size `30030`
bytes, SHA-256
`8afc8a0a0929da077a1a1ad19ddc0c19e754c49646c4b3d806f3f4cf5522de92`.
Its exact candidate arithmetic is
`24891273216 + 8 x 59949056 + 8589934592 = 33960800256 < 51539607552`
bytes with `17578807296` bytes headroom.  It remains a temporary input image;
the capture implementation does not move it, or any resulting candidate, to
the canonical role-10 path.

The public-only branch resource byte image remains
`/tmp/a416-l3a1-rss.jzXoy2/calibration.json`, size `7402` bytes, SHA-256
`2cd389315867cff7598c2977543a8e1f3d0a3dc60d99b51f1e7826f9f95af99a`.
The installed persistent binary has SHA-256
`25aec3d7d68883c2a97f765682a40cabc3feb91f159f67ac2910b6f82025e521`,
size `2419064`, mode `0755`, and build ID
`3cff449e0a265fe63d1fa1d1350ea48f324ba386`.  These are implementation and
resource bindings only.

The exact source/test ledger and serializer boundary are recorded in
`../A416_L3_A1_MACHINE_BINDING_INCREMENT.md`.  Static formal cells use exactly
`proof.json`, `stdout.txt`, `stderr.txt`, and `record.json` under
`CJ_COMPACT_V1`; branch task/argument/record/manifest bindings use
`CJ_PRETTY_2_V1` and exact `600000/2000/1000` millisecond limits.

## Temp-only machine-capture and independent-verify evidence

| Gate | Result | Boundary |
|---|---:|---|
| role-19 capture-producer module | 107/107 pass in 26.62 s | temp-only capture and process control; no scientific dispatch |
| role-24 independent-verifier module on final role-19 bytes | 94/94 pass in 35.20 s | zero-write, zero-subprocess verification only |
| current two-module focused replay | 201/201 pass in 61.89 s | independently reproduced after the repair |
| nine-module regression | 457/457 pass in 152.37 s | no canonical publication or scientific dispatch |
| complete Paper 02 regression | 852/852 pass in 207.85 s | current machine-capture code/documentation set; no scientific dispatch |
| parallel timeout replay | 24/24 pass | descendant cleanup; subreaper enabled state restored to `false` after return |
| live temp candidate | capture + independent verify pass | `/tmp` only; role 10 remains absent |

Stable implementation hashes are:

```text
role19_scheduler_sha256 = 48e6fba9a7c567faddc15c49f7e0d3a3b7a0ff77afae6d80e87d0b1b101638ad
role19_test_sha256 = 6d8f8cd2d73ab8e6e003b7f1763a88fed917ba4863ad55b24f91ae8a7f28681f
role24_builder_sha256 = e1ab0e0f23fdf73406425243cc2203c02cae69cd382dd84e76631a0b63b9a0e7
role24_test_sha256 = a4b0e1c3aa514c01e10ee14c63db7973237e245da74c70643e6e33639c663c40
```

The final temporary candidate is
`/tmp/a416-machine-capture-subreaper-final.UF30tt/machine-candidate.json`,
SHA-256
`eb3395cb3de902685da62b9d18b74e0ba2109d2cce08da2e29a48f966ca7b0e7`,
size `54526`, mode `0644`, and link count `1`.  Role 24 recomputed that digest
and size and returned `PASS_MACHINE_FREEZE_VERIFY_ONLY` with
`promotion_authorized=false`.  The owned fresh-build directory is absent;
the receipt records `shell_used=false`, byte equality, unchanged persistent
identity, and no persistent overwrite.  The pre-repair `456` pass, `1` fail
run and all of its candidate bytes remain withdrawn.

## Current decision

```text
next_authorized_action = SEPARATELY_AUTHORIZE_CANONICAL_ROLE10_AND_COMPLETE_ALL_53_INPUTS_BEFORE_ROLE54
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
formal_exact_schemas_implemented = true
persistent_a1_binary_installed = true
persistent_a1_binary_sha256 = 25aec3d7d68883c2a97f765682a40cabc3feb91f159f67ac2910b6f82025e521
static_four_file_surface = CJ_COMPACT_V1
branch_pretty_serializer = CJ_PRETTY_2_V1
branch_budget_ms = 600000_2000_1000
final_public_static_calibration = PASS_14_OF_14_PUBLIC_S0_ONLY
final_public_static_calibration_sha256 = 8afc8a0a0929da077a1a1ad19ddc0c19e754c49646c4b3d806f3f4cf5522de92
machine_binding_formal_schema_review = ACCEPT_P0_0_P1_0_P2_0
temp_only_machine_capture_implemented = true
machine_verify_only_implemented = true
machine_verify_only_zero_write = true
machine_verify_only_zero_subprocess = true
canonical_machine_role10_exists = false
main_freeze_role54_exists = false
machine_capture_scheduler_sha256 = 48e6fba9a7c567faddc15c49f7e0d3a3b7a0ff77afae6d80e87d0b1b101638ad
machine_capture_test_sha256 = 6d8f8cd2d73ab8e6e003b7f1763a88fed917ba4863ad55b24f91ae8a7f28681f
machine_capture_focused_tests = 107/107
machine_verify_builder_sha256 = e1ab0e0f23fdf73406425243cc2203c02cae69cd382dd84e76631a0b63b9a0e7
machine_verify_test_sha256 = a4b0e1c3aa514c01e10ee14c63db7973237e245da74c70643e6e33639c663c40
machine_verify_focused_tests = 94/94
machine_capture_verify_focused_tests = 201/201
machine_capture_broad_regression = 457/457
paper02_regression_at_machine_capture_bytes = 852/852
paper02_regression_at_machine_capture_seconds = 207.85
machine_capture_parallel_timeout_replays = 24/24
subreaper_enabled_after_return = false
temporary_machine_candidate_sha256 = eb3395cb3de902685da62b9d18b74e0ba2109d2cce08da2e29a48f966ca7b0e7
temporary_machine_candidate_size_bytes = 54526
pre_subreaper_regression = WITHDRAWN_FAIL_456_PASS_1
core_tests_pre_final_branch_resource_binary_binding = 419/419
paper02_regression_at_machine_binding_bytes = 814/814
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
