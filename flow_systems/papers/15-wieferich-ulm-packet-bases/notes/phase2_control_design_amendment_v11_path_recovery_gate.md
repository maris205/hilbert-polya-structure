# Replacement Paper 15 amendment-v11 path-recovery gate

Status: **PASS TO ONE EXACT PATH-RECOVERY TRANSACTION ONLY — CURRENT REVIEW REMAINS REVISE C0/M1/m1**  
Date: 2026-08-17 (Asia/Shanghai)  
Gate class: exact-byte incident recovery; no design-content, review, implementation, or execution authority  
Sole recovery-gate write: `papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_amendment_v11_path_recovery_gate.md`  
Sole recoverable candidate digest: `7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269`  
Current open findings: `P15R-REOPEN-M1`, `P15R-V9-M1`,
`P15R-V9-m1`, `P15R-V10-M1`, and `P15R-V10-m1`  
Source, design-content edit, fresh amendment, review append, implementation,
run, generated-artifact, Route, manuscript, release, archive, and Git
authority: **none**

## Material Passport

- **Material type:** one bounded path-recovery governance gate.
- **Incident:** the authorized package-relative amendment-v11 bytes were
  mistakenly materialized at workspace-root
  `notes/phase2_control_design_amendment_v11.md`, while the intended paper
  target remained absent.
- **Determination:** the frozen v11 remediation gate cannot authorize an
  append to itself or an ungoverned copy/delete repair.  It declares any
  gate drift or extra amendment/design path terminal and authorizes only one
  exact amendment path.  This separate gate therefore supplies the sole,
  exceptional, path-only recovery authority.
- **Recovery ceiling:** the already frozen 49,086-byte candidate is immutable.
  Recovery may create one byte-identical regular file at the intended path,
  verify it while the pinned source remains, and only then delete that exact
  pinned source.  No byte, newline, mode, field, claim, or design meaning may
  change.
- **Review posture:** the current append-only review remains exactly
  `REVISE_C0_M1_m1`.  No finding closes and no review may begin until the
  recovery transaction commits and receives its external final receipt.
- **Failure posture:** recovery is a logical transaction with a single
  attempt.  A mismatch before source deletion rolls back only the newly
  created target and stops.  Any other failure stops without improvisation.

## 1. Exact authority and incident state

### 1.1 Applicable ARS integrity rules

Before this sole gate write, the complete applicable ARS-Codex 0.1.25 root,
academic-paper-review workflow, integrity-verification agent, and integrity
review protocol were freshly read and re-hashed.  Their independent-review,
read-only-audit, exact-evidence, no-fabrication, and fail-closed rules govern
this incident gate.

| Complete ARS rule | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| academic-research-suite/SKILL.md | 369 | 26603 | `14eb5b7b5957c0ae81c33df026ae4227152c95b5029af45f279987a4b654bd5b` |
| academic-paper-reviewer/WORKFLOW.md | 488 | 36007 | `01422d386ac9a42cbc7a9383b2ce9c461c571cebe38cc1fb74a4893c9bb2e800` |
| integrity_verification_agent.md | 823 | 61081 | `d0f567fa7e895596016d217eb0764741da5625d92db419829038df1ab5a63a58` |
| integrity_review_protocol.md | 103 | 6374 | `3c970ef4972b9277626ff9e95d8e9cf47bc476e022257515abe170fad8f5675c` |

This intake and every check before the gate write were static byte/metadata
reads.  No project file was imported, sourced, parsed as project code,
compiled, or executed.  No preflight, runtime probe, generator, verifier,
unittest, wrapper, result, cache, temporary, lock, manifest, or generated
member was created or run.

### 1.2 Frozen original v11 gate is immutable

The complete original gate was freshly read and re-hashed:

```text
workspace_relative_path=papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_remediation_gate_v11.md
paper_relative_path=notes/phase2_control_design_remediation_gate_v11.md
type=regular
mode=0644
nlink=1
lines=1221
bytes=54839
sha256=d86991eedee2e88ddf38617f8f7c12f51944f49541e70f13088da0d39bfc160e
```

Those 54,839 bytes are an immutable authority object.  This recovery gate
does not append, edit, supersede semantically, normalize, or replace them.
The original gate's design contract, findings, form budget, counts, fence,
and later review contract remain unchanged.

The reason a separate gate is mandatory is exact.  Original-gate Section
9.2 says any gate/input drift or extra amendment/design path stops, and its
authorization matrix states:

```text
AUTHORIZED_AMENDMENT_PATH=notes/phase2_control_design_amendment_v11.md
AMENDMENT_ATTEMPTS_AUTHORIZED=1
OTHER_AMENDMENT_OR_DESIGN_PATH_AUTHORIZED=false
```

Appending a correction to the original gate would change its bound digest
and invalidate the candidate's original-gate receipt.  No such append is
authorized here.

### 1.3 Current review is unchanged

The current paper review remains:

```text
workspace_relative_path=papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_peer_review.md
type=regular
mode=0644
nlink=1
lines=5080
bytes=270649
sha256=764e2d0940f01d17c69ac0e6e0fba33d939823746cd52e6930bf92b5272ddb07
verdict=REVISE_C0_M1_m1
```

Its retained nested boundaries remain exactly:

```text
PRESERVED_V10_INPUT_PREFIX_LINES=4634
PRESERVED_V10_INPUT_PREFIX_BYTES=245023
PRESERVED_V10_INPUT_PREFIX_SHA256=baf9a22a08cc18f2ea9fabdf198ebd28bd6b8352dcccfbde49a801a7b545925c
PRESERVED_V9_INPUT_PREFIX_LINES=4236
PRESERVED_V9_INPUT_PREFIX_BYTES=223999
PRESERVED_V9_INPUT_PREFIX_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
PRESERVED_HISTORICAL_PASS_PREFIX_LINES=3961
PRESERVED_HISTORICAL_PASS_PREFIX_BYTES=209656
PRESERVED_HISTORICAL_PASS_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b
```

No review append has occurred.  Recovery supplies no review judgment.

### 1.4 Workspace anchor and exact pinned paths

For this incident only, every path in the recovery transaction is resolved
from this exact workspace anchor, never from the paper package directory:

```text
WORKSPACE_ROOT=/root/rh_dyna/flow_systems

PINNED_STRAY_PATH=notes/phase2_control_design_amendment_v11.md
INTENDED_TARGET_PATH=papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_amendment_v11.md
RECOVERY_GATE_PATH=papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_amendment_v11_path_recovery_gate.md
```

The complete stray candidate was freshly read in full and re-hashed.  Its
exact pre-gate object receipt is:

```text
path=notes/phase2_control_design_amendment_v11.md
type=regular
mode=0644
nlink=1
lines=1072
bytes=49086
sha256=7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269
st_dev=64515
st_ino=2104062
```

The candidate text itself binds the correct package-relative intended path,
the immutable original-gate digest, and `AMENDMENT_V11_WRITE_CONSUMED=true`.
Its content is neither accepted nor reviewed here; it is only pinned as the
sole recoverable byte source.

Immediately before this gate was written, both `lstat` and ordinary
existence checks established:

```text
INTENDED_TARGET_ABSENT=true
RECOVERY_GATE_TARGET_ABSENT=true
OTHER_THAN_PINNED_STRAY_V11_AMENDMENT_NAMED_PATHS=0
PINNED_STRAY_IS_SOLE_EXISTING_V11_AMENDMENT_NAMED_PATH=true
```

The workspace-root and paper `notes/` directories are regular directories,
mode `0755`, on device `64515`.  The intended target is not a symlink,
dangling symlink, hardlink, or hidden pre-existing file; it is absent.

### 1.5 Sole write of this authoring step

This recovery gate is the sole repository write in its gate-authoring step.
The original gate, stray candidate, intended target, review, source,
implementation, Route, manuscript, result, generated, cache, temporary,
lock, receipt, archive, and Git state were not changed.  The recovery
transaction below is a later, separately receipted operation.

## 2. Narrow supersession and nonsemantic recovery

### 2.1 Exact exceptional authority

This gate narrowly supersedes the original gate's path-stop condition only
for the one transaction in Section 3.  It does not reopen the consumed
amendment-author attempt and does not authorize a second content draft.

The distinction is exact:

```text
ORIGINAL_AMENDMENT_AUTHORING_ATTEMPT_CONSUMED=true
NEW_AMENDMENT_AUTHORING_ATTEMPT_AUTHORIZED=false
DESIGN_CONTENT_CHANGE_AUTHORIZED=false
PATH_RECOVERY_ATTEMPTS_AUTHORIZED=1
RECOVERABLE_SOURCE_SHA256=7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269
RECOVERED_TARGET_REQUIRED_SHA256=7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269
```

The recovery operator is a transport custodian, not an amendment author or
reviewer.  It may neither select, rewrite, improve, normalize, truncate,
extend, reformat, or reinterpret content nor claim the candidate conforms to
the design gate.  Equality is a byte fact, not a design verdict.

### 2.2 Closed path and operation set

Exactly three existing/possible material paths participate:

1. the immutable recovery gate itself;
2. the pinned workspace-root stray source; and
3. the absent intended paper target.

The only authorized mutations in the later transaction are:

1. one `apply_patch` Add File operation at the exact intended target; then,
2. only after exact equality, one `apply_patch` Delete File operation on the
   exact pinned stray source; or
3. on a pre-delete mismatch only, one `apply_patch` Delete File rollback of
   the just-created mismatched intended target.

No `cp`, `mv`, `rename`, `ln`, shell redirection, editor save, temporary
file, backup, swap, alternate target, chmod, hardlink, or symlink is
authorized.  No other path may be created, modified, renamed, or removed.

### 2.3 Logical transaction and commit point

The recovery is one logical transaction, though its checks and two possible
mutations are ordered.  Read-only preflight does not consume the attempt.
The attempt is consumed when the exact intended-target Add File operation
begins.  There is no retry under this gate.

The transaction commits only after:

1. the intended target has passed every exact equality check;
2. the exact pinned stray has then been deleted; and
3. final verification proves the intended target still exact, the stray
   path absent, and every frozen authority unchanged.

Before that commit point, no stable amendment receipt exists and no review
is authorized.

## 3. Exact one-transaction recovery protocol

### 3.1 Operator count and stable-gate prerequisite

Exactly one recovery operator may perform exactly one transaction.  Before
any transaction mutation, an external coordinator must supply this recovery
gate's final regular-file receipt.  The operator fresh-reads this complete
gate and requires its actual path/type/mode/nlink/line/byte/SHA-256 tuple to
match that receipt.

```text
RECOVERY_OPERATOR_COUNT=1
RECOVERY_TRANSACTION_ATTEMPTS=1
RECOVERY_GATE_SELF_REPORTED_DIGEST_AUTHORIZED=false
```

Any incomplete or mutable recovery-gate receipt blocks before the attempt.

### 3.2 T0 — mutation-free preflight

The operator performs only `lstat`, metadata, line/byte count, SHA-256,
exact byte-read, and inventory checks.  T0 must prove simultaneously:

1. the original gate is the exact immutable `d86991...` object in Section
   1.2;
2. the current review is the exact `764e2d...` object in Section 1.3;
3. the recovery gate matches its external final receipt;
4. the stray source matches every Section-1.4 coordinate, including exact
   path, regular type, `0644`, nlink one, 1,072 lines, 49,086 bytes,
   SHA-256, device, and inode;
5. the intended target is absent under both ordinary and `lstat` checks;
6. no second v11-amendment named path, alternate recovery gate, symlink,
   hardlink, temporary, backup, or partial target exists; and
7. no review append or authority drift has occurred.

Every hash is written in full during comparison; prefixes such as
`d86991...` and `764e2d...` in prose are labels only.  A single mismatch
blocks with zero mutation and does not consume the recovery attempt.

### 3.3 T1 — create only the intended target

After T0 passes, the operator invokes exactly one `apply_patch` Add File for:

```text
papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_amendment_v11.md
```

The added content must be the complete exact bytes read from the still
present pinned source.  The operation may not normalize line endings, add or
remove a terminal newline, change Markdown, substitute a path string, or
make any content repair.  The source remains present and untouched through
T1 and T2.

If Add File refuses because the target exists, writes a different path, or
cannot complete, the operator stops.  It may not overwrite, merge, retry,
or select another target.

### 3.4 T2 — equality gate while source remains

Before any deletion, the operator read-only verifies both files.  Success
requires every condition below:

```text
source.path=notes/phase2_control_design_amendment_v11.md
source.type=regular
source.mode=0644
source.nlink=1
source.lines=1072
source.bytes=49086
source.sha256=7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269
source.st_dev=64515
source.st_ino=2104062

target.path=papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_amendment_v11.md
target.type=regular
target.mode=0644
target.nlink=1
target.lines=1072
target.bytes=49086
target.sha256=7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269

BYTE_FOR_BYTE_COMPARISON_EQUAL=true
SOURCE_AND_TARGET_ARE_DISTINCT_INODES=true
```

Allowed verification is read-only `stat`/`lstat`, `wc`, `sha256sum`, and
byte comparison.  No project code is imported or executed.

### 3.5 T2 mismatch branch — rollback target and stop

If any T2 equality condition fails, the stray source must remain.  Before
rollback, the operator re-verifies that the source is still the complete
exact pinned object in Section 1.4 and that the mismatched target is the
regular nlink-one file created by this transaction at a path proven absent
at T0.

Only with both proofs may the operator use one `apply_patch` Delete File to
delete that newly created mismatched intended target.  It then verifies:

```text
PINNED_STRAY_RETAINED_EXACT=true
INTENDED_TARGET_ABSENT=true
RECOVERY_TRANSACTION_COMMITTED=false
RECOVERY_ATTEMPT_CONSUMED=true
```

The operator stops.  This gate grants no retry.  If either rollback proof is
missing, it performs no deletion and stops for new governance.

### 3.6 T3 — delete only the exact pinned stray after equality

Only a fully passing T2 opens T3.  Immediately before deletion, the operator
again requires the complete source and target tuples in Section 3.4 and an
unchanged recovery-gate receipt.

It then invokes exactly one `apply_patch` Delete File on:

```text
notes/phase2_control_design_amendment_v11.md
```

Deletion is authorized only for the exact regular object with
`st_dev=64515`, `st_ino=2104062`, mode `0644`, nlink one, 1,072 lines,
49,086 bytes, and SHA-256
`7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269`.
If any coordinate drifts, no deletion occurs.  A similarly named, replaced,
linked, or changed object is not the pinned stray and may not be removed.

If the exact deletion fails, the operator stops with both exact copies or
the observed failure state retained.  It must not delete the valid intended
target, retry deletion, or begin review; successor governance is required.

### 3.7 T4 — final commit verification

After T3, the operator fresh-reads and proves:

```text
RECOVERY_TRANSACTION_COMMITTED=true

intended.path=papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_amendment_v11.md
intended.type=regular
intended.mode=0644
intended.nlink=1
intended.lines=1072
intended.bytes=49086
intended.sha256=7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269

PINNED_STRAY_PATH_ABSENT=true
ORIGINAL_GATE_SHA256=d86991eedee2e88ddf38617f8f7c12f51944f49541e70f13088da0d39bfc160e
CURRENT_REVIEW_SHA256=764e2d0940f01d17c69ac0e6e0fba33d939823746cd52e6930bf92b5272ddb07
OTHER_PATH_MUTATIONS=0
```

The operator reports the intended target's exact path/type/mode/nlink/line/
byte/SHA-256 receipt, the stray-absence fact, this recovery gate's unchanged
receipt, and the unchanged original gate/review hashes.  The removed stray
is not recoverable from its old path; its exact bytes remain at the intended
target only after commit.

## 4. Review boundary after successful recovery

### 4.1 No new review budget

This gate creates no second review attempt and no alternate review path.
Before T4 commit, review is prohibited.  After T4 commit and its external
receipt, the already existing v11 closure contract supplies the only review
authority: one fresh independent append-only design review at
`papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_peer_review.md`.

The reviewer must additionally bind this recovery gate's final receipt and
the T4 recovery receipt as path provenance.  The effective design content is
the exact 7d232... amendment bytes; this recovery gate adds no design clause
and is not an effective amendment.

The review retains the exact 5,080-line, 270,649-byte, `764e2d...` prefix and
the original gate's count-eleven, independence, attack, finding-closure, and
zero-finding requirements.  Only a fresh evidence-backed
`PASS_C0_M0_m0` may close the five named findings.  Recovery predicts no
review result.

### 4.2 Downstream authority remains absent

Even successful recovery or later design PASS grants no source edit,
implementation review, preflight, run, generated artifact, Route,
manuscript, release, archive, or Git authority.  The original gate's
mandatory successor implementation-governance requirement remains exact.

## 5. Recovery-gate external freeze

After this sole gate file is complete, its author stops.  An external
coordinator computes and freezes:

```text
path=papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_amendment_v11_path_recovery_gate.md
type=regular
mode=<actual>
nlink=1
lines=<actual>
bytes=<actual>
sha256=<actual 64-lowercase-hex digest>
```

The coordinator re-hashes the immutable original gate, current review, and
pinned stray, and rechecks intended-target absence.  Drift, an extra path,
symlink, hardlink, nonregular gate, predicted self-digest, or post-receipt
edit blocks recovery.  No transaction begins on a partial, self-reported,
or mutable gate.

## 6. Authorization matrix and stop

```text
GATE_KIND=AMENDMENT_V11_PATH_RECOVERY_ONLY
GATE_VERDICT=PASS_TO_ONE_EXACT_PATH_RECOVERY_TRANSACTION_ONLY
CURRENT_REVIEW_VERDICT=REVISE_C0_M1_m1
P15R_REOPEN_M1_STATUS=OPEN
P15R_V9_M1_STATUS=OPEN
P15R_V9_m1_STATUS=OPEN
P15R_V10_M1_STATUS=OPEN
P15R_V10_m1_STATUS=OPEN

ORIGINAL_V11_GATE_IMMUTABLE=true
ORIGINAL_V11_GATE_SHA256=d86991eedee2e88ddf38617f8f7c12f51944f49541e70f13088da0d39bfc160e
RECOVERY_OPERATOR_COUNT=1
RECOVERY_TRANSACTION_ATTEMPTS_AUTHORIZED=1
RECOVERY_WITH_APPLY_PATCH_ONLY=true
RECOVERY_CONTENT_EDIT_AUTHORIZED=false
RECOVERY_NORMALIZATION_AUTHORIZED=false
NEW_AMENDMENT_AUTHORING_ATTEMPT_AUTHORIZED=false

PINNED_STRAY_PATH=notes/phase2_control_design_amendment_v11.md
PINNED_STRAY_SHA256=7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269
INTENDED_TARGET_PATH=papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_amendment_v11.md
INTENDED_TARGET_REQUIRED_SHA256=7d2323235b26f4badbeae4bdfb0f9f1975545497e5ff72f977eeff80eaa46269
DELETE_STRAY_BEFORE_EXACT_EQUALITY_AUTHORIZED=false
DELETE_PINNED_STRAY_AFTER_EXACT_EQUALITY_AUTHORIZED=true
DELETE_ANY_OTHER_OBJECT_AUTHORIZED=false
MISMATCHED_NEW_TARGET_ROLLBACK_AUTHORIZED=true
RECOVERY_RETRY_AUTHORIZED=false
OTHER_PATH_MUTATION_AUTHORIZED=false

REVIEW_BEFORE_RECOVERY_COMMIT_AUTHORIZED=false
FRESH_APPEND_ONLY_REVIEW_AFTER_RECOVERY_COMMIT_ONLY=true
ADDITIONAL_REVIEW_ATTEMPT_AUTHORIZED=false
AUTHOR_SELF_CLOSURE_AUTHORIZED=false
REVIEW_VERDICT_PREJUDGED=false

CONTROL_SOURCE_EDIT_AUTHORIZED=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
INDEPENDENT_IMPLEMENTATION_REVIEW_AUTHORIZED=false
PROJECT_CODE_IMPORT_AUTHORIZED=false
PROJECT_CODE_EXECUTION_AUTHORIZED=false
SHELL_SOURCE_AUTHORIZED=false
PLATFORM_PREFLIGHT_AUTHORIZED=false
PLATFORM_RUNTIME_PROBE_AUTHORIZED=false
GENERATED_ARTIFACT_MATERIALIZATION_AUTHORIZED=false
RESULT_REGENERATION_AUTHORIZED=false
CSV_GENERATION_AUTHORIZED=false
MANIFEST_GENERATION_AUTHORIZED=false
GENERATOR_EXECUTION_AUTHORIZED=false
VERIFY_ONLY_EXECUTION_AUTHORIZED=false
UNITTEST_EXECUTION_AUTHORIZED=false
TOP_LEVEL_WRAPPER_EXECUTION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
REPRODUCTION_RUN_AUTHORIZED=false

MANIFEST_SCHEMA_CHANGE_AUTHORIZED=false
DAG_CHANGE_AUTHORIZED=false
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

Final determination: **PASS TO ONE EXACT PATH-RECOVERY TRANSACTION ONLY**.
The original v11 gate remains frozen at `d86991...`; the current review
remains `REVISE_C0_M1_m1`; the only recoverable content is the exact
`7d232...` candidate.  Create the intended byte-identical target first,
prove exact equality while retaining the pinned source, and only then delete
that exact source.  No content change, second authoring attempt, review,
source action, execution, or other path operation is authorized here.
