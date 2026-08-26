# Paper 15 control-implementation remediation governance gate v5

Status: **STOP — DESIGN REOPEN REQUIRED**
V5 role: `V4_FAIL_CLOSED_CORRIGENDUM_AND_ATTEMPT4_SUSPENSION`
V5 verdict: `STOP_DESIGN_REOPEN_REQUIRED`
ATTEMPT_4 status: unconsumed, zero source mutation, not currently usable
Source-plan acceptance, author admission, source edit, source freeze, static
implementation review, execution, generation, manuscript, release, archive,
and Git authority: none

This record is the sole notes-only successor-governance write authorized by
the owner/orchestrator after the fresh no-write audit marked
`P15R_IMPL_GATE_V4_CORRIGENDUM_SCOPE_AUDIT_V1`.  That audit found two narrow
wording/specification defects in v4 and one decisive authority defect.  The
decisive defect is that v4 M12 calls G-side stable P-lifetime evidence
"current design-authorized", although the active design closes L's inherited
descriptor set before the nested PID/proc transition and authorizes no such
capability.

This v5 record therefore operates fail-closed.  It corrects the two narrow
v4 statements, records the missing design authority, and suspends every v4
plan/admission/source/review/run effect before ATTEMPT_4 is consumed.  It is
not a source attempt, does not replenish or enlarge an attempt budget, does
not itself reopen the design, and does not authorize a design amendment.

## 0. Global precedence and decision

This Section has global precedence over every v4 clause.  Where v4 says or
implies that a stable v4 receipt, an ATTEMPT_4 plan, or an author admission
can make ATTEMPT_4 source authority usable, the controlling value after a
stable receipt for this v5 file is **false**.

```text
V5_ROLE=V4_FAIL_CLOSED_CORRIGENDUM_AND_ATTEMPT4_SUSPENSION
V5_VERDICT=STOP_DESIGN_REOPEN_REQUIRED

V4_SOURCE_GO_EFFECTIVE=false
V4_PLAN_ACCEPTANCE_EFFECTIVE=false
V4_AUTHOR_ADMISSION_EFFECTIVE=false
V4_SOURCE_TRANSACTION_EFFECTIVE=false
V4_FINAL_SOURCE_FREEZE_EFFECTIVE=false
V4_FUTURE_STATIC_REVIEW_EFFECTIVE=false
V4_EXECUTION_EFFECTIVE=false

ATTEMPT_4_CONSUMED=false
ATTEMPT_4_SOURCE_MUTATION_COUNT=0
ATTEMPT_4_SOURCE_AUTHORITY=false
ATTEMPT_4_PLAN_ACCEPTANCE_AUTHORITY=false
ATTEMPT_4_AUTHOR_ADMISSION_AUTHORITY=false
ATTEMPT_4_REVIEW_AUTHORITY=false
ATTEMPT_4_RUN_AUTHORITY=false
ATTEMPT_4_BUDGET_STATUS=UNCONSUMED_NOT_CURRENTLY_USABLE
ATTEMPT_4_ATTEMPTS_ADDED_BY_V5=0
ATTEMPT_5_AUTHORIZED=false
```

V4 remains an immutable byte record.  Its historical receipts, its binding
of the rejected ATTEMPT_3 review, its six-source tuple, its no-run ceiling,
and every unaffected descriptive fact remain evidence.  Its source-GO
conclusion and all downstream authority that depended on M12 being reparable
inside the current design do not remain operative.

The only possible successor sequence is an owner-gated design reopen, a
fresh independently reviewed design delta with `PASS_C0_M0_m0`, and only
then a new successor implementation-governance decision.  This v5 record
describes that requirement but grants none of those later writes.

## 1. Material Passport and exact intake

### 1.1 Sole v5 target and author boundary

The sole path created by this author is:

```text
papers/15-wieferich-ulm-packet-bases/notes/phase2_control_implementation_remediation_gate_v5.md
```

Immediately before its one creation, that target was absent under ordinary
and symlink-aware checks.  Its parents already existed and were not replaced,
renamed, linked, mounted, or widened.  Every other repository-path write was
zero.

The complete applicable ARS-Codex 0.1.25 academic-research-suite router and
experiment workflow were reread before this write.  The complete v4 gate,
current v14 design gate and amendment, ATTEMPT_3 implementation review, and
all six frozen sources were read and re-hashed.  Static hashes and governance
text were not treated as source conformance, profile acceptance, or runtime
evidence.

This file intentionally contains no predicted self-hash, line count, or byte
count.  An external coordinator must compute them after creation, perform a
second complete unchanged read, and issue the stable v5 receipt required by
Section 8.

### 1.2 Exact controlling records

Each record below was a regular mode-0644, nlink-one file at the final
pre-write check:

| Role | Path under `papers/15-wieferich-ulm-packet-bases/notes/` | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---|
| implementation-remediation gate v2 | `phase2_control_implementation_remediation_gate_v2.md` | 1084 | 59542 | `69563f95d9407ffe98c3e0c78c664ea8105f0f8e5f8994c4337f85fafb2063b1` |
| implementation corrigendum v3 | `phase2_control_implementation_remediation_gate_v3.md` | 263 | 15114 | `2587ed86e794e47edab00e5a6d4b9d8c42fb3b95deb1c2191efc00b7f646f0f5` |
| implementation successor gate v4 | `phase2_control_implementation_remediation_gate_v4.md` | 1311 | 62273 | `b70dc8d42fbec891dba645160bade6effd177b0118db717de12dba403bddd912` |
| immutable ATTEMPT_3 review | `phase2_control_implementation_peer_review.md` | 643 | 37947 | `637a63e1ac182e7b8c09984e7cd5110eebedbcf5f1b580fd2b3a3263a87b7c88` |
| active design amendment v2 | `phase2_control_design_amendment_v2.md` | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` |
| governing design-remediation gate v14 | `phase2_control_design_remediation_gate_v14.md` | 1665 | 84029 | `cb9100863e241f3271781512b8ed83971241974bedd9db9741b5b9acc596c292` |
| active design amendment v14 | `phase2_control_design_amendment_v14.md` | 1414 | 65752 | `b20be3afd58f4eb82ab77b071057effe9678389c7a9525a5c86f6301f158939c` |

The complete current design review remains 6431 lines, 346453 bytes,
SHA-256
`2bb21b0e75ebf6a65bc51a1e42047931c34e9a86be8d641c977ef8c06a9d5e19`,
with current verdict `PASS_C0_M0_m0` under its static conditional-unverified
HC ceiling.  The active amendment order remains v1 through v11, then v13,
then v14.  Amendment v12 remains absent and skipped.

The exact HC profile remains 41 items, 2928 preimage bytes, SHA-256
`1d2c38d460a280b7a4555f6ec0df0be2f81bf3ee5b05ecf8c554295a21cd8cb1`.
Its hash remains non-evidence:

```text
PROFILE_HASH_IS_EVIDENCE=false
CURRENT_RUN_PROFILE_ACCEPTED=false
CURRENT_RUNTIME_ATTESTATION_PRESENT=false
CURRENT_EXECUTION_AUTHORITY=false
```

### 1.3 Exact unchanged ATTEMPT_3 six-source tuple

| # | Frozen path under `papers/15-wieferich-ulm-packet-bases/` | Type | Mode | nlink | Lines | Bytes | SHA-256 |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | `code/generate_controls.py` | regular | 0644 | 1 | 1133 | 60497 | `4bfe2d3e019f401c5e3b917c9b3f1cd9abd7ac5fcdfef2ae641a2195f298b020` |
| 2 | `code/test_controls.py` | regular | 0644 | 1 | 1655 | 129574 | `c8fb9f67faf06b79858a4052196335e9db880529af6f561160027121f362bfac` |
| 3 | `code/README.md` | regular | 0644 | 1 | 95 | 5267 | `96c9f0b268315d639bb363d33241929e447ba01a154bfc9a01da72305b768aee` |
| 4 | `experiments/reproduce.sh` | regular | 0644 | 1 | 6270 | 469357 | `dcd1176bcd69ac0adcb1c43b63a9b33b869f7805be2be8e5946f13e23dedba59` |
| 5 | `experiments/README.md` | regular | 0644 | 1 | 226 | 14697 | `ce60186c80af6a53c9afa2d4a48155526046359a58113e26de9765a9956303a6` |
| 6 | `results/README.md` | regular | 0644 | 1 | 76 | 3221 | `03c0350c849c8dd412f62421ac3b90adb731602796251fecfe13e3e8655f341c` |

```text
FROZEN_SOURCE_PATH_COUNT=6
FROZEN_SOURCE_LINES=9455
FROZEN_SOURCE_BYTES=682613
FROZEN_SOURCE_ALL_REGULAR_0644_NLINK1=true
FROZEN_SOURCE_REVIEW_VERDICT=REVISE_C0_M12_m0
SOURCE_DRIFT_BEFORE_V5=false
ATTEMPT_4_SOURCE_MUTATION_COUNT=0
```

The complete one-level inventories of `code/`, `experiments/`, and
`results/` contained exactly these six entries.  All nine generated CSV/JSON
members, `notes/phase2_control_execution_gate.md`, and
`notes/phase2_control_result_review.md` were absent.  No package-local cache,
temporary, helper, backup, log, lock, pyc, pyo, link, rename, or inventory
residue was admitted.

### 1.4 Independent audit and rejected plan receipt

The fresh independent no-write scope audit is identified by:

```text
AUDIT_MARKER=P15R_IMPL_GATE_V4_CORRIGENDUM_SCOPE_AUDIT_V1
AUDIT_VERDICT=STOP_DESIGN_REOPEN_REQUIRED
AUDIT_REPOSITORY_WRITES=0
AUDIT_SOURCE_MUTATIONS=0
AUDIT_PROJECT_RUN_ATTEMPTS=0
```

The fresh ATTEMPT_4 candidate author stopped before admission and before any
source mutation.  Its external candidate plan receipt is bound only as
rejected provenance:

```text
PLAN_DOMAIN=P15R_ATTEMPT4_REWRITE_PLAN_V1
PLAN_CANDIDATE_BYTES=55682
PLAN_CANDIDATE_SHA256=187dbb8feb534f468553341ad6a1e6d916a387654484e721fc3527d5c5394a01
PLAN_CANDIDATE_STATUS=REJECTED_UNACCEPTED
PLAN_REUSABLE=false
AUTHOR_ADMISSION_V1_ISSUED=false
ATTEMPT_4_SOURCE_MUTATION_COUNT=0
ATTEMPT_4_CONSUMED=false
```

That candidate is not an accepted plan, not a repository artifact, not a
seventh source, and not a future-plan template.  Its existence cannot admit
an author or make v4 authority usable.

## 2. Exact v4 supersession boundary

### 2.1 What remains binding

V2 and v3 remain immutable.  V4 remains immutable and supplies historical
provenance, but is read together with this later fail-closed corrigendum.
Except where Sections 0 and 2.2 suspend authority or Sections 3--5 replace an
exact statement, the following remain binding:

- the frozen v14 design and current `PASS_C0_M0_m0` design-review receipt;
- the ATTEMPT_3 `REVISE_C0_M12_m0` review and all twelve findings;
- the exact six-source writable-set ceiling and no-seventh-path rule;
- all unaffected M1--M11 and IMPL-01--IMPL-43 conformance obligations;
- the prohibitions on source retry, post-freeze patch, new wire form,
  generated artifacts, execution, manuscript, release, archive, and Git;
- the separation between source conformance, profile acceptance, runtime
  receipts, and execution evidence; and
- the current false profile/run state.

`PASS_STATIC` remains only a scoped nonfinding at ATTEMPT_3 bytes.  It is not
source acceptance and does not override this STOP.

### 2.2 Authority clauses globally suspended

The audit found that v4's initial conclusion that all twelve findings can be
repaired without design change is false for M12.  V4 Sections 0 and 13 are
superseded wherever they state zero remaining governance blockers, zero need
for design change, or GO to one ATTEMPT_4 source transaction.

The following v4 surfaces are globally suspended, including every dependent
cross-reference even when not repeated here:

1. the conditional source-authority declaration and prerequisite chain in
   v4's opening status and Sections 0, 2, 3, and 4;
2. stable-v4-receipt source-admission effect;
3. canonical ATTEMPT_4 plan acceptance and any plan-to-source effect;
4. fresh ATTEMPT_4 author admission;
5. the sole six-path source transaction, permitted source-side static-check
   phase, and final ATTEMPT_4 source freeze in Sections 7--9;
6. the disposition of M12 as an implementation-only repair in Sections 5
   and 6;
7. any future ATTEMPT_4 static-review sequence in Section 11; and
8. every final-matrix statement that v4 currently authorizes ATTEMPT_4 after
   receipt/plan/admission.

This suspension has higher precedence than a v4-only external receipt.  An
authentic receipt can prove v4's bytes; it cannot restore the suspended
authority.

```text
V4_ONLY_RECEIPT_SUFFICIENT_FOR_SOURCE=false
V4_ONLY_PLAN_SUFFICIENT_FOR_SOURCE=false
V4_ONLY_ADMISSION_SUFFICIENT_FOR_SOURCE=false
V4_ONLY_FREEZE_SUFFICIENT_FOR_REVIEW=false
V4_AUTHORITY_RESTORABLE_BY_SOURCE_AUTHOR=false
```

## 3. Corrigendum A — two disjoint close-only child roles

V4 conflates the P denial child with a future G normal worker child.  The
active v14 design gives them different owners, endpoints, creation cuts, and
lifetimes.  This Section supersedes the ambiguous v4 M7 dependency sentence,
the erroneous v4 M9 dependency sentence, and the IMPL-35 matrix echo.

### 3.1 Replacement for v4 M7 dependency wording

V4's phrase "the child first-instruction EP_G close" in the M7 dependency
paragraph means only:

```text
G_POST_SEAL_NORMAL_WORKER_CHILD:
  creator=G
  creation_precondition=LIVE_G_OBSERVED_EXACT_BOOTSTRAP_SEALED_FULL_RETURN
  inherited_actual_endpoint=EP_G
  first_instruction=close inherited transient EP_G alias and prove EBADF
  other_endpoint_action_before_close=FORBIDDEN
```

It does not refer to the P denial child.  It does not authorize a worker
before the exact live-G Seal full-return fence.  All new worker-inspection
capabilities still need exact ownership and close proof and may not become an
alternate endpoint holder.

### 3.2 Replacement for v4 M9 dependency wording

The exact replacement for v4's sentence that the
"denial/post-return child" closes EP_G is:

```text
P_DENIAL_CHILD:
  creator=P
  creation_phase=EP_P_PRE_HOLDER_FREEZE_F12_DENIAL_BRANCH
  inherited_actual_endpoint=EP_P
  first_instruction=close EP_P and every inherited global-endpoint alias
  action_before_all_required_closes=FORBIDDEN
  endpoint_io_dup_shutdown_transfer_registration_barrier=FORBIDDEN

G_POST_SEAL_NORMAL_WORKER_CHILD:
  creator=G
  creation_phase=AFTER_LIVE_G_EXACT_BOOTSTRAP_SEALED_FULL_RETURN
  inherited_actual_endpoint=EP_G
  first_instruction=close transient EP_G alias and prove EBADF
  action_before_required_close=FORBIDDEN
  endpoint_io_dup_shutdown_transfer_registration_barrier=FORBIDDEN
```

These are two disjoint stubs.  Neither role may be used as evidence for the
other, and neither close exception authorizes any read, send, receive, peek,
drain, shutdown, duplication, transfer, registration, or barrier passage.

### 3.3 Replacement IMPL-35 treatment

The v4 IMPL-35 matrix row is superseded by:

| Row | ATTEMPT_3 review | Controlling no-regression treatment |
|---|---|---|
| IMPL-35 | PASS_STATIC | Preserve two disjoint close-only stubs: the P-created F12 denial child closes inherited EP_P and all inherited global aliases before any non-close action; only a G-created trusted normal worker after live G's exact Seal full return closes its transient inherited EP_G alias before any non-close action. |

This correction adds no child, descriptor, endpoint, wire form, or source
authority.

## 4. Corrigendum B — namespace-correct M6 owner receipt

This Section wholly supersedes v4 M6's **Mandatory repair** and **Static
acceptance** blocks.  The frozen defect and affected paths remain accurate,
but an exact U1/U2 map proves that initial-userns uid 0 is unmapped in U2; it
does not derive a host-independent numeric overflow display value.

### 4.1 Exact four-part receipt

Any future design-authorized implementation of M6 must keep these four
logically separate components:

```text
OBJECT_INVARIANT =
  (S_IFMT(st_mode), S_IMODE(st_mode), st_dev, st_ino)

P_OWNER =
  (observer=P,
   user_namespace=INITIAL_USER_NAMESPACE,
   st_uid_before=0,
   st_uid_after=0,
   before_after_same_object=true)

MAP =
  (U1_uid_map="65534 65534 1\n",
   U2_uid_map="0 65534 1\n",
   owner_initial_uid=0,
   owner_relation_in_U2=UNMAPPED,
   namespace_provenance=EXACT_U1_THEN_U2)

G_DISPLAY =
  (observer=G,
   user_namespace=U2,
   raw_st_uid=<actual fstat result>,
   expected_numeric=NONE,
   owner_authority=false,
   pass_predicate=false)
```

For FD10 and FD11 separately:

1. P records `OBJECT_INVARIANT` and `P_OWNER` before L creation while P is
   in the initial user namespace.
2. The exact inherited descriptor, not a reopened path, remains bound by
   unchanged type/mode/dev/ino and descriptor-lifetime evidence through L
   and G.
3. The exact U1 and U2 map bytes and namespace identities prove only the
   displayed `UNMAPPED` relation for the initial uid-0 owner.
4. G records its actual numeric `st_uid` only as the raw, U2-tagged
   `G_DISPLAY` observation.  No expected numeric value exists.
5. P revalidates the initial-userns owner and identical object before its
   source-capability copies are closed at the future design-authorized cut.
6. Owner authority comes only from P's initial-userns before/after evidence,
   joined to the invariant object and exact inherited-FD continuity.

### 4.2 Exact acceptance and prohibitions

```text
INITIAL_UID0_TO_U2_MAP_RELATION=UNMAPPED
G_DISPLAY_EXPECTED_NUMERIC=NONE
G_DISPLAY_IS_OWNER_AUTHORITY=false
G_DISPLAY_IS_IDENTITY_AUTHORITY=false
G_DISPLAY_IS_PASS_PREDICATE=false
CROSS_USERNS_RAW_ST_UID_EQUALITY_AUTHORIZED=false
OVERFLOWUID_HARDCODE_AUTHORIZED=false
OVERFLOWUID_SYSCTL_DEPENDENCY_AUTHORIZED=false
HC_OVERFLOWUID_DEPENDENCY_AUTHORIZED=false
```

Static acceptance requires exact object invariants, P's two-sided
initial-userns ownership evidence, exact map bytes/provenance, the UNMAPPED
classification, inherited-FD continuity, and G's labeled raw observation.
It rejects any comparison of P's raw uid to G's raw uid; any expectation that
G display 65534 or another numeric value; any derivation from HC; any
`/proc/sys/kernel/overflowuid` dependency; and deletion of P owner evidence.

This correction does not expand HC, change a wire grammar, or convert a
namespace-local display into global ownership authority.

## 5. Corrigendum C — M12 requires new design authority

### 5.1 V4's current-design-authorized assertion is false

V4 M12 item 3 says G must possess "current design-authorized" stable P
pidfd/proc lifetime evidence.  No such acquisition or retained descriptor is
authorized by the current effective design.

Active design amendment v2 Section 5.3 step 2 requires L to retain only:

```text
the inherited bootstrap endpoint
source slot 10
source slot 11
```

and to close every other P descriptor before any namespace call.  The same
design additionally requires:

- the inherited bootstrap channel to carry no descriptor or ancillary item;
- the authenticated P--G control connection to hand off exactly one
  descriptor, the workers-cgroup FD, and no second ancillary item;
- setup slots 10/11 to remain the fixed source-root capabilities with their
  exact lifetime and purpose; and
- every additional descriptor field, environment field, transition, or
  trusted actor needed by an implementation to trigger a new design finding
  and STOP.

Later amendments, including v14, do not expressly supersede that closed
descriptor set for a P-lifetime capability.  In the current architecture G
also remounts procfs for the nested PID namespace; it cannot defer the
acquisition and then reopen initial-namespace P by an outer PID through that
nested proc view.

Therefore:

```text
V4_M12_CURRENT_DESIGN_AUTHORIZED_ASSERTION=false
CURRENT_DESIGN_P_LIFETIME_CAPABILITY_FOR_G=false
CURRENT_DESIGN_EXTRA_L_INHERITED_DESCRIPTOR=false
CURRENT_DESIGN_SECOND_BOOTSTRAP_ANCILLARY=false
CURRENT_DESIGN_SECOND_P_G_SCM_RIGHTS_DESCRIPTOR=false
CURRENT_DESIGN_FD12_AUTHORIZED=false
CURRENT_DESIGN_FD13_AUTHORIZED=false
CURRENT_DESIGN_REPURPOSE_FD10_OR_FD11_AUTHORIZED=false
M12_REPAIRABLE_AS_IMPLEMENTATION_ONLY=false
DESIGN_REOPEN_REQUIRED=true
```

V4 M12's mandatory-repair and static-acceptance blocks are suspended in full.
The owner-generic terminal goal is not rejected, but it cannot be imposed on
a source author until a new design explicitly authorizes a feasible
P-lifetime capability and independently closes its consequences.

### 5.2 Why no source workaround is legal

The following are not implementation workarounds:

- assigning the capability to FD12/13 or any other new slot;
- repurposing FD10/11;
- retaining an otherwise closed P descriptor in L;
- adding ancillary data to the inherited bootstrap channel;
- piggybacking another FD on WORKERS_CGROUP_FD;
- transferring a capability in a new or revised P--G wire form;
- reopening `/proc/PID_DEC` or calling `pidfd_open(PID_DEC)` from G after the
  nested PID/proc transition;
- inferring P death from EOF alone while a producer or alias may remain;
- treating G as able to `waitid`/reap nonchild P; or
- using a shared path, service, file, or persistent store.

Each would change the current descriptor/transition/actor design or weaken
the exact no-future-producer proof.  A source author, plan author, gate
receipt, or static reviewer cannot authorize it.

### 5.3 Non-authorizing minimum design-reopen candidate

For scoping only, the independent audit identified the following minimum
candidate that a future design-governance process must attack.  It is not an
authorized design and no slot number is selected here:

1. While P still has initial PID/proc visibility and before cloning L, P
   would acquire a stable self pidfd plus a stable initial-proc P directory
   capability and construct an immutable P-identity receipt.
2. A future design would choose exact new descriptor slots and expressly
   supersede v2 Section 5.3 step 2, the complete descriptor enums,
   cardinalities, close order, and every affected holder/FDSET rule.
3. L and then G would inherit those exact capabilities without a wire handoff;
   G would validate them before PID1_READY, while P and L would close their
   copies at exact authorized cuts.
4. G would retain one fully stateful P-lifetime ledger through the terminal
   branch, prevent every worker/child inheritance, and prove exact close plus
   immediate EBADF on every exit/unwind.
5. G could treat readiness on the inherited P pidfd as P-death evidence but
   could not claim to wait or reap nonchild P.  A no-future-producer claim
   would additionally require the holder ceiling, complete P-to-G drain to
   exact EOF, and all owner-specific terminal evidence.
6. The future design would close interactions with HC, endpoint holder cuts,
   L/P/G lifecycle, PID-namespace visibility, setup/worker FDSETs, source
   capabilities, cgroup cleanup, raw17, C14, and every failure unwind.

The candidate may be revised or rejected by a future independent design
review.  V5 selects no FD, adds no descriptor, creates no design-amendment
path, and pre-judges no design verdict.

## 6. Attempt ledger and fail-closed handling

| Attempt | Source mutation | Review | Status after v5 |
|---|---|---|---|
| ATTEMPT_1 | consumed | none | closed historical attempt |
| ATTEMPT_2 | consumed | none | closed historical attempt |
| ATTEMPT_3 | consumed and frozen | `REVISE_C0_M12_m0` | immutable failed attempt |
| ATTEMPT_4 | none | none | unconsumed, suspended, not currently usable |

```text
HISTORICAL_ATTEMPTS_CONSUMED=3
ATTEMPT_4_CONSUMED=false
ATTEMPT_4_FIRST_SOURCE_MUTATION_OCCURRED=false
ATTEMPT_4_SOURCE_CONTENT_MUTATIONS=0
ATTEMPT_4_SOURCE_METADATA_MUTATIONS=0
ATTEMPT_4_LINK_RENAME_INVENTORY_MUTATIONS=0
ATTEMPT_4_PLAN_CANDIDATE_ACCEPTED=false
ATTEMPT_4_AUTHOR_ADMITTED=false
ATTEMPT_4_BUDGET_REFUNDED_BY_V5=false
ATTEMPT_4_BUDGET_INCREMENTED_BY_V5=false
ATTEMPT_4_CURRENTLY_USABLE=false
ATTEMPT_5_AUTHORIZED=false
```

V5 does not retroactively erase a mutation.  Its `ATTEMPT_4_CONSUMED=false`
statement is conditional on and bound to the exact unchanged six-source
tuple and zero-write receipt in Section 1.  If contrary evidence of a source,
metadata, link, rename, or inventory mutation appears, this record cannot
refund or relabel it; the owner must STOP and issue new governance.

No v4-only plan, admission, or receipt may be carried across a future design
reopen.  After a design PASS, a fresh successor implementation gate must
decide whether the still-unconsumed ATTEMPT_4 name/budget remains usable and
must require a newly authored canonical plan and fresh admission.  V5 makes
no such future decision.

## 7. Required successor sequence and present nonauthority

The required order is:

1. owner-gated design-reopen governance;
2. one explicitly authorized design amendment that resolves the complete
   P-lifetime capability, descriptor closure, and all dependent semantics;
3. external stable freeze of that design amendment;
4. a fresh independent complete design review with `PASS_C0_M0_m0` as the
   only accepting verdict;
5. a new owner decision and successor implementation gate binding the entire
   new design/review tuple, this v5 STOP, the ATTEMPT_3 review, and the exact
   unchanged or newly adjudicated source start tuple;
6. only after that gate's independent prerequisites, a new plan and fresh
   source-author admission; and
7. a separately governed static implementation review, still with no run
   authority unless another execution gate later accepts the exact profile.

V5 does not authorize step 1 or any later step.  It records the mandatory
dependency and stops the implementation workflow.

```text
DESIGN_REOPEN_WRITE_AUTHORIZED_BY_V5=false
DESIGN_AMENDMENT_WRITE_AUTHORIZED_BY_V5=false
DESIGN_REVIEW_WRITE_AUTHORIZED_BY_V5=false
IMPLEMENTATION_SUCCESSOR_GATE_WRITE_AUTHORIZED_BY_V5=false
ATTEMPT_4_PLAN_ACCEPTANCE_AUTHORIZED_BY_V5=false
ATTEMPT_4_AUTHOR_ADMISSION_AUTHORIZED_BY_V5=false
CONTROL_SOURCE_EDIT_AUTHORIZED_BY_V5=false
ATTEMPT_4_FINAL_FREEZE_AUTHORIZED_BY_V5=false
ATTEMPT_4_STATIC_REVIEW_AUTHORIZED_BY_V5=false
EXECUTION_GATE_CREATION_AUTHORIZED_BY_V5=false
RESULT_REVIEW_CREATION_AUTHORIZED_BY_V5=false
```

## 8. Stable v5 receipt and drift rule

An external coordinator must issue one
`P15R_ATTEMPT4_SUSPENSION_GATE_V5_STABLE_RECEIPT_V1` containing:

1. this exact v5 path, regular type, mode 0644, nlink 1, line and byte counts,
   SHA-256, UTF-8, terminal-LF, and no-NUL results;
2. two complete unchanged reads of this file;
3. the exact v2, v3, v4, ATTEMPT_3 review, active design-v2, v14 gate,
   v14 amendment, and current design-review receipts in Section 1;
4. the exact frozen six-source tuple and two unchanged read/hash passes;
5. the exact three-root inventory and generated-nine/execution-gate/
   result-review/cache/residue absences;
6. the rejected 55682-byte plan-candidate receipt and absent admission;
7. confirmation that this author wrote only this v5 path once; and
8. zero source, design, review, generated, run, and Git attempts.

This receipt authenticates the STOP.  It does not accept a plan, admit an
author, restore v4, authorize design work, or authorize a run.  Any drift in
v5, v4, the current design/review tuple, or the six-source tuple after the
receipt is a STOP requiring new owner governance.

## 9. Runtime, generated, review, and publication nonauthority

All of the following remain false:

```text
CURRENT_RUN_PROFILE_ACCEPTED=false
PROFILE_HASH_IS_EVIDENCE=false
CURRENT_RUNTIME_ATTESTATION_PRESENT=false
CURRENT_PLATFORM_AVAILABILITY_CLAIM=false
CURRENT_EXECUTION_AUTHORITY=false

PROJECT_CODE_IMPORT_AUTHORIZED=false
PROJECT_CODE_EXECUTION_AUTHORIZED=false
SHELL_SOURCE_AUTHORIZED=false
PLATFORM_PREFLIGHT_AUTHORIZED=false
PLATFORM_RUNTIME_PROBE_AUTHORIZED=false
GENERATOR_EXECUTION_AUTHORIZED=false
VERIFY_ONLY_EXECUTION_AUTHORIZED=false
UNITTEST_EXECUTION_AUTHORIZED=false
WRAPPER_EXECUTION_AUTHORIZED=false
REPRODUCTION_RUN_AUTHORIZED=false

GENERATED_ARTIFACT_MATERIALIZATION_AUTHORIZED=false
CSV_GENERATION_AUTHORIZED=false
MANIFEST_GENERATION_AUTHORIZED=false
RESULT_REGENERATION_AUTHORIZED=false

SOURCE_FREEZE_CREATION_AUTHORIZED=false
IMPLEMENTATION_REVIEW_CREATION_AUTHORIZED=false
IMPLEMENTATION_REVIEW_OVERWRITE_OR_APPEND_AUTHORIZED=false
RESULT_REVIEW_CREATION_AUTHORIZED=false

PROOF_MODIFICATION_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ARCHIVE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
```

No source hash, HC hash, v5 receipt, or future design idea is execution
evidence.

## 10. Manifest and authority nonmembership

V5 is external governance.  It is not a seventh source, generated member,
manifest member, authority binding, DAG node, DAG edge, implementation review,
design amendment, profile object, or execution receipt.  It does not change
the current manifest schema or the historical original implementation-gate
binding.

```text
V5_IS_SEVENTH_SOURCE=false
V5_IS_GENERATED_MEMBER=false
V5_IS_MANIFEST_MEMBER=false
V5_IS_AUTHORITY_BINDING=false
V5_IS_DAG_NODE_OR_EDGE=false
MANIFEST_AUTHORITY_BINDINGS=14
MANIFEST_DAG_NODES=8
MANIFEST_DAG_DISTINCT_EDGES=12
MANIFEST_SCHEMA_CHANGE_AUTHORIZED=false
DAG_CHANGE_AUTHORIZED=false
NEW_WIRE_FORM_AUTHORIZED=false
```

## 11. Final authorization matrix

```text
P15R_CONTROL_IMPLEMENTATION_REMEDIATION_GATE=P15R-P2-CONTROL-IMPLEMENTATION-REMEDIATION-GATE-v5.0
V5_ROLE=V4_FAIL_CLOSED_CORRIGENDUM_AND_ATTEMPT4_SUSPENSION
V5_VERDICT=STOP_DESIGN_REOPEN_REQUIRED
V5_PRECEDENCE=GLOBAL_OVER_V4_PLAN_ADMISSION_SOURCE_REVIEW_RUN_EFFECTS

CONTROLLING_V4_SHA256=b70dc8d42fbec891dba645160bade6effd177b0118db717de12dba403bddd912
CONTROLLING_ATTEMPT_3_REVIEW_SHA256=637a63e1ac182e7b8c09984e7cd5110eebedbcf5f1b580fd2b3a3263a87b7c88
CONTROLLING_ATTEMPT_3_REVIEW_VERDICT=REVISE_C0_M12_m0
CURRENT_DESIGN_REVIEW_VERDICT=PASS_C0_M0_m0
AUDIT_MARKER=P15R_IMPL_GATE_V4_CORRIGENDUM_SCOPE_AUDIT_V1
AUDIT_VERDICT=STOP_DESIGN_REOPEN_REQUIRED

CORRIGENDUM_A_DISJOINT_CHILD_ROLES=true
P_DENIAL_CHILD_CLOSE_TARGET=EP_P_AND_ALL_INHERITED_GLOBAL_ALIASES
G_POST_SEAL_CHILD_CLOSE_TARGET=TRANSIENT_EP_G
P_DENIAL_CHILD_IS_G_POST_SEAL_CHILD=false

CORRIGENDUM_B_M6_RECEIPT=OBJECT_INVARIANT,P_OWNER,MAP,G_DISPLAY
INITIAL_UID0_TO_U2_MAP_RELATION=UNMAPPED
G_DISPLAY_EXPECTED_NUMERIC=NONE
G_DISPLAY_OWNER_AUTHORITY=false
G_DISPLAY_PASS_PREDICATE=false
OVERFLOWUID_DEPENDENCY_AUTHORIZED=false

CORRIGENDUM_C_V4_M12_CURRENT_DESIGN_AUTHORIZED=false
CURRENT_DESIGN_G_SIDE_P_LIFETIME_CAPABILITY=false
CURRENT_DESIGN_FD12_FD13_AUTHORIZED=false
M12_IMPLEMENTATION_ONLY_REPAIR_AUTHORIZED=false
DESIGN_REOPEN_REQUIRED=true

ATTEMPT_4_PLAN_CANDIDATE_BYTES=55682
ATTEMPT_4_PLAN_CANDIDATE_SHA256=187dbb8feb534f468553341ad6a1e6d916a387654484e721fc3527d5c5394a01
ATTEMPT_4_PLAN_CANDIDATE_ACCEPTED=false
ATTEMPT_4_AUTHOR_ADMISSION_ISSUED=false
ATTEMPT_4_SOURCE_MUTATION_COUNT=0
ATTEMPT_4_CONSUMED=false
ATTEMPT_4_CURRENT_SOURCE_AUTHORITY=false
ATTEMPT_4_CURRENT_PLAN_AUTHORITY=false
ATTEMPT_4_CURRENT_REVIEW_AUTHORITY=false
ATTEMPT_4_CURRENT_RUN_AUTHORITY=false
ATTEMPT_4_BUDGET_REFUNDED=false
ATTEMPT_4_BUDGET_INCREMENTED=false
ATTEMPT_5_AUTHORIZED=false

V4_ONLY_RECEIPT_PLAN_ADMISSION_SUFFICIENT=false
SOURCE_WRITE_AUTHORIZED=false
SOURCE_FREEZE_AUTHORIZED=false
STATIC_IMPLEMENTATION_REVIEW_AUTHORIZED=false
DESIGN_WRITE_AUTHORIZED=false
EXECUTION_GATE_AUTHORIZED=false
GENERATED_ARTIFACT_AUTHORIZED=false
MANUSCRIPT_RELEASE_ARCHIVE_GIT_AUTHORIZED=false

CURRENT_RUN_PROFILE_ACCEPTED=false
PROFILE_HASH_IS_EVIDENCE=false
CURRENT_RUNTIME_ATTESTATION_PRESENT=false
CURRENT_EXECUTION_AUTHORITY=false

V5_IS_MANIFEST_MEMBER=false
V5_IS_AUTHORITY_BINDING=false
V5_IS_DAG_NODE_OR_EDGE=false
MANIFEST_AUTHORITY_BINDINGS=14
MANIFEST_DAG_NODES=8
MANIFEST_DAG_DISTINCT_EDGES=12
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
```

Final determination: **STOP — DESIGN REOPEN REQUIRED.**  V4's conflated
child-role wording and numeric UID-projection requirement are corrected
above, but its M12 source-GO premise is false under the active exact
descriptor closure.  ATTEMPT_4 remains unconsumed only because the plan
candidate was rejected, admission was absent, and all six source paths remain
byte-for-byte unchanged.  No plan, admission, source edit, freeze, review, or
run may proceed.  A fresh design-governance process must first authorize and
independently review the missing P-lifetime capability design; only a later
successor implementation gate may decide whether implementation work can
resume.
