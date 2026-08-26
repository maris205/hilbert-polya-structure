# Phase 2 control implementation peer review — ATTEMPT_3

## 0. Decision and authority ceiling

```text
REVIEW_KIND=FRESH_INDEPENDENT_STATIC_IMPLEMENTATION_CONFORMANCE
ATTEMPT=ATTEMPT_3
OVERALL_REVIEW_VERDICT=REVISE_C0_M12_m0
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=12
MINOR_FINDINGS=0
PASS_C0_M0_m0=false
SOURCE_CONFORMANCE_ACCEPTED=false
CURRENT_RUN_PROFILE_ACCEPTED=false
HC_ACCEPTED=false
PROFILE_HASH_IS_EVIDENCE=false
CURRENT_EXECUTION_AUTHORITY=false
PLATFORM_PREFLIGHT_AUTHORIZED=false
GENERATED_ARTIFACT_MATERIALIZATION_AUTHORIZED=false
REPRODUCTION_RUN_AUTHORIZED=false
POST_FREEZE_PATCH_AUTHORIZED=false
POST_REVIEW_REPAIR_AUTHORIZED=false
SEPARATE_EXECUTION_GATE_REQUIRED=true
```

This is the sole fresh independent static review admitted after the
ATTEMPT_3 six-source freeze.  Twelve independent Major findings prevent the
only accepting verdict.  The deterministic FD10/FD11 namespace-view defect
is a run-blocking failure, but is counted Major rather than Critical because
it fails closed before governed work and cannot itself produce a false
successful result.  That calibration does not soften the decision: the
frozen attempt is rejected and receives no execution authority.

The six frozen sources are an immutable failed attempt.  This review is not
repair authority, does not replenish the consumed ATTEMPT_3 budget, and does
not authorize ATTEMPT_4.  No source, design, gate, README, generated member,
or other note was modified during this review.

## 1. Reviewer method and evidence boundary

I used the ARS academic-research-suite reviewer, methodology, experiment-
integrity, reproducibility, and code-runner rules as the review framework.
The review treated the author plan, freeze self-audits, comments, constants,
READMEs, expected-token tables, and plausible hashes as untrusted claims.
Findings below are based on independent lexical, structural, call/dataflow,
state-machine, and cross-source reconstruction.

Permitted checks performed were limited to complete static reads, SHA-256,
`lstat`/inventory receipts, UTF-8/LF/NUL checks, lexical tokenization, Python
AST parse, in-memory nonexecuting compilation with cache writing disabled,
nonexecuting shell syntax parse, literal reconstruction, symbol/callgraph
inspection, and manual state/dataflow audit.  No code object was executed.

```text
PROJECT_CODE_IMPORTED=false
PROJECT_CODE_EXECUTED=false
PROJECT_SOURCE_COMMANDS=0
PROJECT_CLI_INVOCATIONS=0
GENERATOR_RUN_ATTEMPTS=0
VERIFIER_RUN_ATTEMPTS=0
UNITTEST_RUN_ATTEMPTS=0
WRAPPER_RUN_ATTEMPTS=0
PREFLIGHT_RUN_ATTEMPTS=0
SOCKET_RUN_ATTEMPTS=0
NAMESPACE_RUN_ATTEMPTS=0
CGROUP_RUN_ATTEMPTS=0
ROOT_RUN_ATTEMPTS=0
LOCK_RUN_ATTEMPTS=0
GIT_OPERATIONS=0
REVIEW_TARGET_WRITES_BEFORE_CONCLUSION=0
```

The present shell quarantine remains effective: `experiments/reproduce.sh`
sets `CURRENT_RUN_PROFILE_ACCEPTED=false` and fails before path resolution,
the embedded Python, or `profile_window_begin`.  The static future function
`successor_execution_gate_entry` is not current authority.  HC's 41-line
preimage, 2928-byte length, and digest are static facts only and were not
treated as evidence of custody, platform acceptance, or an execution window.

## 2. Frozen six-source binding

The ordered tuple was read in full at intake and again immediately before
this one-shot review creation.  Both receipts were identical.  Every member
was a regular file, mode 0644, nlink 1, UTF-8 with terminal LF and without CR
or NUL.

| # | Frozen source | Lines | Bytes | SHA-256 |
|---:|---|---:|---:|---|
| 1 | `code/generate_controls.py` | 1133 | 60497 | `4bfe2d3e019f401c5e3b917c9b3f1cd9abd7ac5fcdfef2ae641a2195f298b020` |
| 2 | `code/test_controls.py` | 1655 | 129574 | `c8fb9f67faf06b79858a4052196335e9db880529af6f561160027121f362bfac` |
| 3 | `code/README.md` | 95 | 5267 | `96c9f0b268315d639bb363d33241929e447ba01a154bfc9a01da72305b768aee` |
| 4 | `experiments/reproduce.sh` | 6270 | 469357 | `dcd1176bcd69ac0adcb1c43b63a9b33b869f7805be2be8e5946f13e23dedba59` |
| 5 | `experiments/README.md` | 226 | 14697 | `ce60186c80af6a53c9afa2d4a48155526046359a58113e26de9765a9956303a6` |
| 6 | `results/README.md` | 76 | 3221 | `03c0350c849c8dd412f62421ac3b90adb731602796251fecfe13e3e8655f341c` |

```text
FROZEN_SOURCE_LINES_TOTAL=9455
FROZEN_SOURCE_BYTES_TOTAL=682613
FROZEN_SOURCE_REGULAR_0644_NLINK1=6
```

The three source roots contained exactly those six entries.  The nine future
generated members, amendment v12, the execution gate, the result review, and
cache/temp/helper/backup/log/lock residue were absent.  This review target
was also absent at intake and at the final pre-write check.

## 3. External and repository governance bindings

The exact external rewrite-plan block from
`P15R_ATTEMPT3_REWRITE_PLAN_V1` through
`END=P15R_ATTEMPT3_REWRITE_PLAN_V1`, including its terminal LF, is bound as:

```text
PLAN_BYTES=15998
PLAN_SHA256=8e9200df4f78edf303cd22b68e31f807bcb076019af90cd09ea5b69ca4f89a22
```

The exact external freeze record is bound by marker
`P15R_ATTEMPT3_FINAL_FREEZE_RECEIPT_V1`, the ordered six receipts in Section
2, `ATTEMPT3_CONSUMED=true`, `EXECUTION_AUTHORITY=false`, and
`CURRENT_RUN_PROFILE_ACCEPTED=false`.  A relay copied the v14 gate token as
`...b5a69ca4f89a22`; the immediately supplied one-token transport correction
restored the author-origin and repository-rehashed value
`cb9100863e241f3271781512b8ed83971241974bedd9db9741b5b9acc596c292`.
This was treated as a disclosed transport correction, not source drift.

Key complete repository bindings were independently rehashed:

| Record | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| current complete design review | 6431 | 346453 | `2bb21b0e75ebf6a65bc51a1e42047931c34e9a86be8d641c977ef8c06a9d5e19` |
| v14 remediation gate | 1665 | 84029 | `cb9100863e241f3271781512b8ed83971241974bedd9db9741b5b9acc596c292` |
| active v14 amendment | 1414 | 65752 | `b20be3afd58f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c` |
| original implementation gate | 735 | 35164 | `e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8` |
| implementation remediation v1 | 660 | 32800 | `52a716286a0e46046083f256502820fb5e269913eb7893522ce63b70622b119f` |
| implementation remediation v2 | 1084 | 59542 | `69563f95d9407ffe98c3e0c78c664ea8105f0f8e5f8994c4337f85fafb2063b1` |
| implementation remediation v3 | 263 | 15114 | `2587ed86e794e47edab00e5a6d4b9d8c42fb3b95deb1c2191efc00b7f646f0f5` |

The base design and exact active count-thirteen amendment chain were:

```text
base db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d 1183/62887
v1   cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe 931/49257
v2   c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea 1750/98006
v3   f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b 986/43781
v4   f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592 996/43881
v5   2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8 411/20580
v6   0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363 1498/80822
v7   bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7 1199/60145
v8   e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147 884/45610
v9   0947e635093c04fae2a50f1e7b9ece7ae6e2fa4ed783bb514b60c13b9d437829 870/40366
v10  d973b858b0db268cd35d7372e6e2e34bdceced839d53390b491a8980c758b50f 1133/50487
v11  7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269 1072/49086
v13  4f1dcb90f1569534d816925cfa5d639b8b279b326b6026d6612cd10632a7be27 1057/48820
v14  b20be3afd58f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c 1414/65752
```

Recovery/governance receipts were also full-read and rehashed:

```text
reopen-v1 8af1bbdca261cc419d090319521a80a80c7c54a8dfb46fa02a257fa18a008973 434/21256
v11-path-recovery 41d8b223a65708c750b2e36f437b94ee4a6fb5337ed03c577913ac86ef7d9888 528/21386
v13-append-recovery 2a0ac6ea868fd5b37b77d21df5c4375123942b5f3ef50926a7609307e048de16 495/23827
design-gate 0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3 272/10820
remediation-base 98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16 188/7023
remediation-v2 00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705 405/20113
remediation-v3 e367e632490cb03ef9bc066b52ca8259988669949a237a04c0b15770240479ac 578/27299
remediation-v4 df1ae4b43615f0f824681b13698256bac215fc593e590b29e32bf34c44065647 645/30174
remediation-v5 55f655b6bcf6e62972c7fdc3301c9177a57df9c25602f0a61a13d8f06bf599d7 839/41734
remediation-v6 a1950889a0b2ce632627194a1f26151db6b3c9771db971257df33cfa1f53cf00 1252/62896
remediation-v7 a27ab525537fe41e2917713fd0b2462c6b6efe41c96c5f277de4c48d85ccd576 776/38865
remediation-v8 342faf7880ed80bc1406792953c3d64b8ae057740f2d4b2e12d9543612308de8 852/43684
remediation-v9 c4da0d0684ec64d21ef046abe9686147545e7a1035f7c6f3c8d712972b69dc90 1060/48563
remediation-v10 48e32570de67c6df3bba7662940c0b7e72b3b0add5efd4b164154d9fe618c9a5 1002/45658
remediation-v11 d86991eedee2e88ddf38617f8f7c12f51944f49541e70f13088da0d39bfc160e 1221/54839
remediation-v12 ac5e997419f1123218c662ab579e42274ad8774faf3634db1d7b6c51e8ccc999 789/37732
remediation-v13 5253cebde296df494aee9d63bdc275f7622e79182c61732715bbaf94bd8e2dca 1324/61873
remediation-v14 cb9100863e241f3271781512b8ed83971241974bedd9db9741b5b9acc596c292 1665/84029
```

## 4. Static reconstruction receipts

The frozen sources passed syntax/shape checks, but syntax success is not
implementation conformance:

- `generate_controls.py` and `test_controls.py` passed UTF-8 tokenization,
  AST parse, and in-memory compile; the extracted 6232-line embedded Python
  in `reproduce.sh` passed the same checks; nonexecuting `sh -n` passed.
- Recursive symbol inspection found no unresolved global in G or T.  The
  embedded program's only apparent injected names were
  `P15R_AUDIT_HANDLE` and `P15R_AUTH_SERIAL`, both supplied by the worker
  namespace.  `guardian_start_identity` is an unused redundant helper;
  `successor_execution_gate_entry` is the intentionally noncurrent future
  root.  Neither was used as evidence for a requirement.
- Literal reconstruction found 173 unique explicit unittest methods in
  exact source order; 35 semantic programs; 28 package registrations; eight
  CSVs; 120 rows; widths `18,19,22,17,16,19,13,10`; negative total 35;
  14 authority bindings; six implementation bindings; eight DAG nodes and
  12 distinct edges.
- S02/S03 recompute raw valuations from primitive `p,r`; the owner tests
  parse the actual 2x2 automorphism matrix, determinant, action, and bare
  type; the semantic path contains forward mutation, canonical serialization,
  independent reparse, typed predicate, inverse from postimage, and receipt
  counterfactual.
- The v3-corrected `test_rep_010` path obtains equal actual Q before/after,
  creates separate deep Q_mode/Q_mtime structures, changes one mode or
  mtime coordinate, retains ctime and all other coordinates, and runs the
  independent difference oracle before `receipt_compare`.
- Stream capture has independent exact 16,777,216-byte stdout and stderr
  ceilings and joined length/chunk/hash fields.  `SPAWN_RESULT` contains and
  checks the rich request/audit/serial/nonce/digest/target/method/purpose/
  handle/child/status/stream/capability core.
- Static wire counts were 12 FD5, 12 D-M1, four D-M2 and exactly one ADMIT;
  FD8 payload sizes were 9/5/12/5.  C14 had the exact 15 vectors, row 14
  `111001`, row 15 `111100`, and one nominal success.  The raw registry had
  17 unique labels and the exact precedence permutation.
- HP7/HG7/HM4/MECH5/H construction and the Release/Ready/ACK/Seal grammar
  are attached to the actual endpoint types.  HC reconstructed to 41 items,
  2928 bytes, SHA-256
  `1d2c38d460a280b7a4555f6ec0df0be2f81bf3ee5b05ecf8c554295a21cd8cb1`.
  Those shape facts do not close the failure paths below.
- Forbidden superseded public/local validation, attempt/return, X_P/X_G,
  ACK-of-Seal, retry, fallback, reconnect, old count, and stale active-v1-v8
  authority surfaces were not found.

The freeze self-audit's claims of PASS/no definite gap were not evidence.
Its statement that literal `IMPL-01` through `IMPL-43` traceability markers
were present is not literally true in the six sources; semantic row coverage,
not comments, was audited.  The absence of marker comments is not counted as
a separate finding.  The README statements that all full-return carriers are
reconciled and queued Seal always reaches row 15 are contradicted by M10 and
M11 below.

## 5. Findings

### M1 — Generation capability admits noncontract paths and reopens after FD validation

**Evidence.** `code/generate_controls.py:275-289` deliberately accepts a
relative output argument by opening it beneath `.`.  At
`generate_controls.py:1022-1055`, `validate_generation_capability` validates
FD9, then reopens `output_argument` through `open_argument_directory`, checks
only the target directory's dev/ino/uid/mode, and never lstats or validates
the private parent.  Active amendment v1 `:530-593` instead requires
`ABSOLUTE_NEW_DIR`, an lstat of the target and private parent, exact parent
ownership/mode, and no path reopen after the FD receipt.

**Impact.** The accepted CLI/capability language is strictly wider than the
frozen interface and omits a required parent receipt.  Matching a relative
path to FD9 is accepted even though it is not an authorized generation call.

**Minimum correction obligation.** In a newly authorized attempt, require an
absolute target; lstat target and parent under the exact nonsymlink/owner/
0700 contract; compare target identity to FD9 without opening it again; and
use FD9 alone for enumeration and exclusive writes.  This review authorizes
no such patch.

### M2 — The independent CSV oracle contains dead and vacuous invariant checks

**Evidence.** `code/test_controls.py:1048-1065` defines generic checks for
schema, negative count, row status, width, row count, uniqueness, mutation
count, and tolerance.  Complete callsite enumeration gives zero calls for
indices 3 through 8.  Index 14 is called only at `test_controls.py:1337` for
the kernel table, whose header has no tolerance field, so
`row.get("tolerance", "") in {"", "0"}` is vacuously true.  The parser at
`:651-665` checks bytes/header/width but not these row semantics.
`test_pkg_005` sums the literal `NEGATIVE_COUNTS`; it does not derive 35
negative rows from the eight parsed CSVs.  No independent whole-output check
requires every row status to be PASS or closes schema/negative/mutation tags
across all tables.

**Impact.** A subject and its own verifier can agree on a wrong row schema,
status, negative tagging, mutation tagging, or nonzero valuation tolerance
while the purported independent suite still passes.  This violates the
design's receipt-field and zero-tolerance rules (`design_lock:163-173,
221-235,680-683`) and the same-source-oracle prohibition.

**Minimum correction obligation.** Make independent, reachable tests derive
every invariant from all eight parsed roots and real rows: schema, status,
width/count/unique ID, case kind, mutation/negative cardinality and pairing,
and every present tolerance.  Demonstrate callgraph reachability rather than
leaving helper branches unused.

### M3 — DAG validation preempts five registered package detectors

**Evidence.** `generate_controls.py:819-827` makes DAG-node presence depend
on exact authority, design, review, gate, and manifest-status values.
`validate_dag` at `:834-837` maps any such mismatch to `E_DAG_CYCLE`.
`verify_manifest` calls it at `:938`, before the dedicated branches at
`:939-954`.  Therefore the frozen mutations produce:

```text
P10 expected E_MANIFEST_SEMANTICS                 -> E_DAG_CYCLE first
P12 expected E_AUTHORITY_BINDING                  -> E_DAG_CYCLE first
P13 expected E_DESIGN_BINDING                     -> E_DAG_CYCLE first
P14 expected E_REVIEW_BINDING                     -> E_DAG_CYCLE first
P15 expected E_IMPLEMENTATION_GATE_BINDING        -> E_DAG_CYCLE first
```

The expected registry is at `test_controls.py:917,919-922`; the frozen
detector precedence is `design_lock:865-875`.

**Impact.** At least five of the 28 explicit package methods are statically
incapable of observing their registered detector.

**Minimum correction obligation.** Separate graph shape/edge validation from
the semantic values of existing blocks, and order the dedicated binding and
manifest-semantic detectors before the graph-cycle fallback exactly as the
frozen precedence specifies.

### M4 — P23 never performs the registered repair attempt and its exit contract is inconsistent

**Evidence.** The P23 construction at `test_controls.py:1560` omits
`target=`, so it takes `MutationSurface.target="VERIFY_ONLY_GENERATOR"` from
`:903`.  `run_package` at `:1200-1204` always requires status 1.  In the
wrapper, `apply_mutation` treats `CLI_REPAIR` as a receipt-only operation
(`reproduce.sh:4619-4622`), while the VERIFY_ONLY_GENERATOR branch at
`:4951` uses the ordinary `--verify-only --input-dir` argv; the `--repair`
argv at `:4973` exists only in the COPIED_REPRODUCE branch that P23 does not
select.  If the real generator is given `--repair`, it correctly emits
`E_VERIFY_ONLY_WRITE` at `generate_controls.py:1105-1106` but maps that
reserved CLI rejection to exit class 2 at `:1123-1126`, consistent with
`design_lock:1017-1019`, not the test's required 1.

**Impact.** Without `--repair`, P23 returns a normal verify result and cannot
observe the detector; with it, the actual subject returns the frozen CLI exit
class that the oracle rejects.  P23 is unsatisfiable.

**Minimum correction obligation.** Route P23 to the actual admitted
generator with exact `--verify-only --input-dir ... --repair`, preserve the
reserved exit class 2, and make the independent oracle expect both status 2
and the sole exact stderr detector.

### M5 — Cleanup, foreign, lock, and terminal outcomes are parsed but not joined

**Evidence.** The generic package path parses `CLEANED.outcome`,
`FOREIGN_AUDITED.outcome`, `LOCK_RELEASED.outcome`, and
`SESSION_CLOSED.outcome` at `test_controls.py:1207-1219`, but comparisons
omit every outcome.  The first P25 replacement at `:1223-1239` checks the
cleanup detector but not the required cleanup outcome; the second P25
replacement uses the generic path and checks neither the displaced-cleanup
nor foreign-retention outcome.  `GuardianClient.close` at `:876-890` parses
request/session/outcome/capability and a terminal receipt, yet finally
compares only reply digest and close request.

**Impact.** `ERROR`, a wrong displacement state, a false foreign result, or
an inconsistent terminal outcome can survive the independent oracle.  Rich
SPAWN_RESULT does not repair missing cleanup/terminal joins.  IMPL-10 and the
foreign-outcome obligations remain open.

**Minimum correction obligation.** Derive the expected outcome for every
fixture from the actual replacement/cleanup state and assert every parsed
outcome plus request/session/capability/digest joins in the method path and
top-level close.  P25's two replacement subfixtures must separately prove
`DISPLACED_CLEANED`, `FOREIGN_RETAINED`, and the matching terminal outcome.

### M6 — FD10/FD11 owner receipts compare incompatible user-namespace views

**Evidence.** `reproduce.sh:5731-5734` includes caller-view `st_uid` in the
source capability tuple.  P stores FD10/FD11 tuples at `:6040-6053` while in
the initial user namespace; both frozen directory roots are initially owned
by uid 0.  P installs U1 map `65534 65534 1` at `:6123-6125`; L enters uid
65534 at `:5707-5715`; U2 then maps `0 65534 1` at `:5718-5728`.  Initial uid
0 is therefore unmapped in G/U2 and `fstat` exposes the configured overflow
uid rather than P's initial-view 0.  On the present static host that value is
65534.  G nevertheless requires whole-dictionary equality at `:5737-5738`
after drop at `:5973-5974`.

**Impact.** On the frozen host facts, the only difference is uid 0 versus
65534, so `source capability receipt drift` is deterministic before HG,
epoch-2 REAPED, Release, Seal, or governed work.  More generally, HC does not
bind overflowuid, and a namespace-relative displayed UID is not a valid
cross-namespace owner proof.  Current quarantine is not the cause: a future
valid `ExternalProfileAcceptance` would still encounter this code.

**Minimum correction obligation.** Preserve P's initial-userns owner proof,
but split namespace-invariant type/mode/dev/ino from namespace-tagged owner
observations.  P must retain and revalidate the initial view; G must validate
the invariant identity and a map-derived local projection.  Merely deleting
owner evidence or hard-coding 65534 is insufficient and ambiguous.

### M7 — P authorizes workers without independently verifying cwd or the complete FDSET

**Evidence.** G selects and fstats `cwd_fd` at `reproduce.sh:3190-3199`, then
sends claimed `cwd_dev/cwd_ino` at `:3218`.  P parses both fields at
`:3784-3786` but never stores or compares them, never stats
`/proc/<child>/cwd`, and still sends CHILD_ADMITTED at `:3869`.

D-M2 records whole child snapshots at `:2423,2463`, but `:2466` checks only
before/after equality.  It never compares the snapshot with the complete
role/phase FDSET or verifies every remote slot's type, identity, flags and
CLOEXEC; P's targeted audits cover only FD8/4/5.  `F_GETFD` on a fresh
`pidfd_getfd` duplicate proves the local duplicate's CLOEXEC, not the target
slot's original flag.  The child's own `close_except` and low-FD assertion
at `:2970-2985` are not P-independent pre-admission evidence.

**Impact.** The exact v2 rule at `design_amendment_v2:844-850` requires P to
verify credentials, cwd and the complete descriptor set before admission.
An extra non-socket descriptor, wrong cwd, or wrong remote flag is not
rejected by the P admission decision.

**Minimum correction obligation.** Under a retained proc/pidfd identity with
before/after ABA checks, P must stat cwd and compare the registered identity,
enumerate the complete `/proc/PID/fd` set, verify every exact phase slot and
its type/dev/ino/target flags/CLOEXEC, reject extras, and only then send
CHILD_ADMITTED.  D-M2 snapshot stability alone is not semantic validation.

### M8 — F12 reads G status/cgroup before the denial vector and begins HP before the required fresh revalidation

**Evidence.** `attest_guardian_privilege_drop` reads and parses G
`status_raw` and `cgroup_raw` at `reproduce.sh:5855-5863`, then runs the
denial child/vector/reap at `:5864`.  Active v14 F12
`design_amendment_v14:536-547` requires the opposite: denial vector, kill,
exact reap, duplicate-wait no-child, process-gone, then fresh complete G
status/cgroup and all pass predicates.  `p_v14_exchange` begins HP at
`:5901`; it does not parse the probe-reap predecessor until `:5903-5905`.
The sole-G check at `:6172` occurs before the denial sequence and is not
freshly repeated after denial/process-gone and before HP.

**Impact.** Release binds pre-vector raw bytes, not the required post-vector
evidence, and HP can begin before F12's evidence-complete boundary.  The
claimed F12 order and Release attestation are false even if every individual
operation succeeds.

**Minimum correction obligation.** Implement the exact order: denial vector
→ pidfd kill/exact reap/ECHILD/process-gone → fresh complete G status/cgroup
and predicates → fresh L-reaped/sole-G/process-gone revalidation → HP → HM →
Launcher → Release.  No earlier raw-byte cache may be substituted.

### M9 — The denial probe's identity and credentials are child-authored constants, not P-retained evidence

**Evidence.** The denial child sets credentials/caps and constructs a string
containing fixed `uid_*`, `gid_*`, `groups=EMPTY`, and `cap_*=0` fields at
`reproduce.sh:5804-5811`.  P at `:5825-5843` checks only gross length and
attempt count, extracts starttime with string splitting, and does not exactly
parse/bind `probe_outer_pid`, compare it to the clone PID, or validate the
reported credentials/caps from a retained proc identity.  There is no probe
proc/pidfd lifetime identity ledger or P-side before/after identity check
around the vector; G identity is likewise not revalidated on both sides.

**Impact.** The v9 requirement at `design_amendment_v9:302-306,331-339`
explicitly requires P-retained PID/starttime identity, every credential/cap
field validated before attempts, and probe/G identity revalidation around the
vector.  A child-authored expected-pass string cannot be that evidence.

**Minimum correction obligation.** P must retain the probe pidfd and stable
proc capability, independently read and bind PID/starttime/credential/cap
state before releasing the vector, and revalidate probe and G identities on
both sides.  Only those readbacks may construct `probe_identity_ascii` and
the denial ledger.

### M10 — A full-return actual enqueue can be lost before the outbound receipt is appended

**Evidence.** `FramedControl.send` at `reproduce.sh:1377-1384` records the
syscall count, but after a full return still performs fallible dispatcher
commit, `fstat`, dataclass construction and list append before
`boundary_outbound` contains the receipt.  A handled PossessionFailure,
OSError, or MemoryError in that interval leaves
`last_send_count == len(last_send_packet)` and no appended receipt.
`retain_v14_failure` at `:989-994` rebuilds full sends only from the appended
list and adds `last_send_*` only for a proper short send.

**Impact.** An actual fully enqueued Release or ACK can disappear during
containment and freeze RE or AE as zero, violating C14 actual-enqueue
monotonicity and outbound reconciliation.

**Minimum correction obligation.** Journal full syscall return as an
indelible endpoint-bound, one-use reconciliation source before any later
fallible work; bind identity from the frozen/failure-time endpoint receipt;
and deduplicate it with the normal appended receipt.  Full return must never
fall through the short-send-only retention branch.

### M11 — A valid queued Seal is misclassified when its expected-frame cache was not yet populated

**Evidence.** P consumes Seal via `_bootstrap_record` at
`reproduce.sh:5926`, then constructs `expected_seal` and calls
`ledger.expect_carrier` at `:5928`.  A local MemoryError between those steps
is retained by `:6173-6179` with the exact received packet but no expected
Seal entry.  `complete_v14_terminal_survivor.expected_matches` at
`:1025-1036` can reconstruct only GUARDIAN_READY when a cache entry is absent;
for BOOTSTRAP_SEALED it returns false at `:1028`.  The exact retained Seal is
then marked `WRONG_ATTESTATION` at `:1046-1047` (or `:1077-1078`) and SS is
not committed.

**Impact.** After peer death and EOF, an actual canonical Seal enqueue can
freeze as row 13/14 failure instead of the required row 15 non-live success.
A local cache-construction failure is falsely promoted into a wire
attestation failure.

**Minimum correction obligation.** Deterministically reconstruct Seal from
the retained Launcher/Release/Ready/ACK/contract chain before classifying the
packet, or retain an unreconciled tombstone if the oracle cannot be
established.  Never assert WRONG_ATTESTATION solely because local expected
state is absent.

### M12 — Terminal reconciliation has only a P survivor; P_CRASH and G-side evidence cannot finalize

**Evidence.** `complete_v14_terminal_survivor` at
`reproduce.sh:1019-1096` rejects `context.owner != "P"` at `:1020`, drains
only G-to-P at `:1058-1084`, and freezes with hard-coded
`owners=("P",)`/`owner_evidence={"P": ...}` at `:1096`.  G constructs an
owner-G context at `:5980-5984`, immediately reraises, performs only local
auth containment, and exits at `:5990-5997`.  The sole completion call is P's
at `:3739`; no G completion call exists.

**Impact.** If P dies after G has validated Release and holds the HP/HM/HC/HG
ceiling, G is the authenticated single survivor with EP_G, but cannot drain
P-to-G, reconcile its outbound receipts, close with proof, or freeze
P_CRASH.  G-only and two-owner evidence, including the required P-before-G
same-label tie, are unreachable.  The nominal 17-label registry is therefore
not a total terminal classifier.

**Minimum correction obligation.** Implement owner-generic symmetric
completion, including G-side P-to-G drain, P-death/no-future-producer proof,
G outbound reconciliation, endpoint close/EBADF, and preservation of every
admissible owner evidence/tie.  A P-only hard-coded freeze cannot satisfy the
survivor contract.

## 6. IMPL-01 through IMPL-43 adjudication

`PASS_STATIC` below means only that this review found no additional definite
static defect in that row at the frozen bytes.  It is not runtime evidence
and cannot override any cross-cutting finding.

| Row | Disposition | Evidence summary |
|---|---|---|
| IMPL-01 | REVISE — M2 | Counts/literals are exact, but independent whole-CSV semantic closure is incomplete. |
| IMPL-02 | REVISE — M1, M4 | Generation capability/path contract and reserved repair CLI path are not exact. |
| IMPL-03 | PASS_STATIC | S02/S03 independently derive raw valuation from primitive p/r. |
| IMPL-04 | PASS_STATIC | Actual matrix, determinant, action, labels and bare type are checked. |
| IMPL-05 | PASS_STATIC | Seven-stage semantic mutation/inverse/counterfactual chain is statically present. |
| IMPL-06 | PASS_STATIC | 173 explicit methods and independent 16 MiB stream ceilings are present. |
| IMPL-07 | REVISE — M3, M4, M5 | Registered detectors/outcomes are not all reachable or independently joined. |
| IMPL-08 (v3) | PASS_STATIC | Actual equal Q, deep clones, exact one-coordinate diff, ctime preservation, and pre-comparator oracle are present. |
| IMPL-09 | PASS_STATIC | Nominal manifest blocks and unique 8-node/12-edge reconstruction are present; M3 is detector precedence. |
| IMPL-10 | REVISE — M5 | Spawn core is rich, but cleanup/foreign/terminal outcomes and capabilities are not fully joined by the oracle. |
| IMPL-11 | REVISE — M7 | P/L/G ownership exists, but P does not independently prove worker cwd/complete FD state before admission. |
| IMPL-12 | REVISE — M6, M7 | Source-boundary success is unreachable on the frozen host; child cwd/FD admission is incomplete. |
| IMPL-13 | REVISE — M7 | Staging exists, but P does not verify every remote target FD/type/flag/CLOEXEC before admission. |
| IMPL-14 | REVISE — M7 | Registries exist, but claimed cwd/FDSET is not independently resolved by P. |
| IMPL-15 | PASS_STATIC | Monotone audit handles, auth serials, deterministic nonce domain, ownership and terminal states are present. |
| IMPL-16 | PASS_STATIC | FD8 exact bare bytes/directions/cardinality are present. |
| IMPL-17 | PASS_STATIC | Audited-spawn outer-byte equality and ACCEPTED/CONFIRMED order are present. |
| IMPL-18 | PASS_STATIC | Native Unix-diag request/reply sizes, port/seq/deadline/cross/reciprocal/drain structure is present. |
| IMPL-19 | REVISE — M7 | D-M2's 21-tag/quiescence/unwind structure exists, but snapshots are not interpreted as the complete target FDSET/CLOEXEC admission proof. |
| IMPL-20 | PASS_STATIC | Owner-local ledgers and immediate-EBADF close paths were found in the admitted normal paths. |
| IMPL-21 | PASS_STATIC | Distinct 12/12 forms, closed states, byte joins and terminal auth/replay rules are present. |
| IMPL-22 | REVISE — M5 | R preserves foreign objects, but the independent oracle does not close all foreign/cleanup outcomes. |
| IMPL-23 | PASS_STATIC | Lock candidate/ACQUIRING/HELD/CLEANING and signal-after-bind structure is present. |
| IMPL-24 | PASS_STATIC | Same-control requester terminal/EOF/reap/ACK/global-final/G-reap/cgroup sequence is present. |
| IMPL-25 | REVISE — M8, M9 | Release attestation order and denial identity evidence are not the active v9/v14 contract. |
| IMPL-26 | REVISE — M12 | Nominal raw17 vector exists, but P_CRASH/G-survivor/tie finalization is not total. |
| IMPL-27 | PASS_STATIC | Revised ACK owner/one-use/frame joins are present and forbidden old coordinates are absent. |
| IMPL-28 | REVISE — M10, M11, M12 | Seal enqueue survival and symmetric crash-survivor evidence are incomplete. |
| IMPL-29 | REVISE — M10, M11, M12 | Nominal C14 table is exact, but actual-carrier terminal reconciliation is not total. |
| IMPL-30 | PASS_STATIC | Actual EP_P/EP_G and HP/HG/HM/MECH/H construction paths are present. |
| IMPL-31 | PASS_STATIC | HC41/2928/digest is exact static non-evidence and current profile remains false. |
| IMPL-32 | PASS_STATIC | Four revised frame grammars/directions/digest cuts are statically present. |
| IMPL-33 | REVISE — M6, M8, M9 | F12 cannot reach HG on the frozen host and denial evidence/order is wrong. |
| IMPL-34 | REVISE — M12 | Live endpoint window structure exists, but G cannot be the required terminal survivor after P death. |
| IMPL-35 | PASS_STATIC | Denial/post-return child close-only stub closes before other endpoint action. |
| IMPL-36 | PASS_STATIC | Live-G governed write/normal clone remains fenced on actual Seal full return. |
| IMPL-37 | REVISE — M8, M10, M11, M12 | Failure containment does not preserve/reconcile every committed carrier or survivor case. |
| IMPL-38 | PASS_STATIC | READMEs state current quarantine, no run, no generated artifacts and proof/profile ceilings, though their terminal claims are contradicted by findings. |
| IMPL-39 | PASS_STATIC | Review/base/active13 and historical gate bindings are current; stale authority is absent. |
| IMPL-40 | PASS_STATIC | Canonical versus mutation environment context separation is statically present. |
| IMPL-41 | REVISE — M6 | Pre-drop capability exists but cross-namespace owner identity is compared incorrectly and blocks source use. |
| IMPL-42 | REVISE — M6 | FD10/11 alias timing exists, but the exact owner/identity receipt cannot survive the prescribed namespace transition. |
| IMPL-43 | PASS_STATIC | P-PID cgroup naming, collision failure, membership/populated/disposal joins are present. |

## 7. Cross-cutting original-gate adjudication

- **Scientific arithmetic and semantic controls:** raw valuation,
  automorphism, seven-step inverse, 35 semantic programs, and v3 Q handling
  have no additional definite static defect.  M2 nevertheless leaves the
  emitted CSV receipt fields under an incomplete independent oracle, so the
  science/package layer as a whole is not accepted.
- **Counts, canonical bytes and manifest:** nominal 8/120/35, widths,
  173/28, 14/6, 8/12 and canonical serialization shapes are exact.  M3 and
  M4 make six registered package methods impossible; M1 widens generation
  authority; M5 leaves outcome receipts unclosed.
- **P/L/G runtime ownership and containment:** initial P authority, atomic L,
  nested G PID1, high-FD staging, bare FD8, audited spawn, Unix-diag, D-M2
  quiescence/unwind, pidfds, object preservation, lock/signal and v8 global
  final structures are present.  M6 through M9 prevent the required source,
  child-admission and F12 evidence paths from conforming.
- **v14 endpoint/profile boundary:** actual endpoints, nominal HP/HG/HM/MECH/H,
  four frame grammars, HC static profile, F14 close-only exception and live-G
  full-return fence are present.  M10 through M12 invalidate actual-carrier
  retention and terminal reconciliation.  Static HC or the present host
  cannot repair those code paths.
- **Documentation, inventory and governance:** the three README inventories,
  current quarantine, generated absence, authority13, and six-source binding
  are statically aligned.  Documentation is not implementation evidence and
  cannot override the twelve findings.

## 8. REPLAY and other hostile checks not counted as findings

`replay_observed=False` at `reproduce.sh:395` was specifically challenged.
Active v11 `:723-725` defines REPLAY as an actual complete observation that
authenticates to a consumed earlier bootstrap/boundary/old one-use coordinate.
The frozen current process has one fresh endpoint, dispatcher and
`BoundaryLedger`, no endpoint handoff, no prior authenticated-coordinate
input and no shared persistent history.  Under that exact one-shot evidence
domain, false is the conservative result; a wrong session alone cannot guess
replay.  This is not a separate finding.  A future multi-bootstrap or imported
history design would need a real authenticated history authority and could
not retain the constant.

No new definite defect was found in the nominal FD5/D-M1 state tables,
Unix-diag byte ABI, D-M2 reverse-close/EBADF unwind, foreign-object
preservation in R, lock/signal order, CgroupTree PID naming, F14 close-only
stub, superseded-field deletion, or current static profile-false gate.  These
nonfindings are scoped static observations, never evidence of runtime
availability.

## 9. Final disposition

The only accepting gate verdict is `PASS_C0_M0_m0`; this review has twelve
Major findings.  Therefore:

```text
ATTEMPT_3_STATIC_REVIEW_ACCEPTED=false
ATTEMPT_3_FROZEN_BYTES_PRESERVED=true
ATTEMPT_3_POST_FREEZE_REPAIR=false
ATTEMPT_3_RUN_AUTHORITY=false
CURRENT_RUN_PROFILE_ACCEPTED=false
HC_IS_RUNTIME_EVIDENCE=false
PLATFORM_PREFLIGHT_AUTHORIZED=false
GENERATED_AUTHORITY=false
SEPARATE_FUTURE_EXECUTION_GATE_CANNOT_BE_CREATED_FROM_THIS_REVIEW=true
FINAL_VERDICT=REVISE_C0_M12_m0
```

The minimal correction obligations in Section 5 describe what a separately
authorized future source attempt would have to prove; they grant no write,
retry, restart, or execution authority.  Because the current governance says
ATTEMPT_3 is consumed and ATTEMPT_4 is false, the present authorized action
ends with this review record.

This record intentionally does not embed a self-hash.  Its type, mode,
nlink, line count, byte count, terminal-LF result, and SHA-256 must be
reported as an external read-only post-creation receipt.  No post-creation
edit is authorized.
