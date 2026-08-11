# A4.16 L3-A1 role-13 S0-compatibility publication implementation increment

Prepared: 2026-08-11 UTC

Protocol: `R401-VAL-L3-A1-PREFREEZE-S0-COMPATIBILITY`

Authority: **IMPLEMENTATION ONLY / NON_LICENSING / canonical role 13 absent /
no role 54 / no scientific dispatch**

## 1. Exact boundary and current repository state

This increment records the capture and fixed-destination publication surface
for main-freeze input role 13,
`R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json`.  It does not publish that
artifact.  At the time of this record the live canonical role-13 path is
absent, the publisher has not been executed against the repository, and no
receipt in this document is evidence of publication.

Canonical machine-admission input role 10 is a separate, already completed
edge.  Its exact current identity is:

```text
canonical_machine_role10_exists = true
canonical_machine_role10_sha256 = 0d5c46726ee8142e0e53f97c904213dfc9b795ac300b423277bc27a711f5c21e
canonical_machine_role10_size_bytes = 54526
canonical_machine_role10_mode = 0644
canonical_machine_role10_nlink = 1
canonical_machine_role10_publication_commit = 5086e33c7c66f33785338e90b340347e086d9941
canonical_machine_role10_role24_postverify = PASS_MACHINE_FREEZE_VERIFY_ONLY
canonical_s0_compatibility_role13_exists = false
main_freeze_role54_exists = false
scientific_dispatch_performed = false
component_status = null
milestone_status = null
theorem_status = null
final_status = null
```

Role 10 remains machine admission only.  It does not authorize role-13
publication, role-54 construction, a production run, or a scientific result.

## 2. The original compatibility artifact is unchanged

The publication implementation does not add a self-hash, publication field,
or authority field to the compatibility artifact.  The artifact remains the
closed exact 18-key object:

```text
schema_version
protocol_id
artifact_role
artifact_status
source_protocols
matrix
static_facts
branch_facts
composite_facts
control_hashes
role_sets
source_bindings
replay_status
failures
claim_boundary
milestone_status
theorem_status
final_status
```

Its exact authority-bearing literals remain

```text
artifact_role = S0_TO_A1_COMPATIBILITY_REPLAY
artifact_status = NON_LICENSING
replay_status = PASS_S0_COMPATIBILITY_REPLAY
failures = []
milestone_status = null
theorem_status = null
final_status = null
```

Its byte serializer is `CJ_COMPACT_V1`; `serializer` is not an added
top-level artifact key.

The object still replays only the sealed representative
`{S000,S025,S050} x {128,256}` archive, its six static proof entries, exact
26-role branch manifest, 18 composite bindings, and nine fixed S0 control
hashes.  It invokes no evaluator, changes no S0 byte, covers no held-out slab,
and grants no component, milestone, theorem, final, production, or dispatch
authority.

## 3. Four exact live source bindings

Every candidate binds these four exact live source roles:

```text
scripts/replay_r401_val_l3_s0_through_a1_checkers.py
research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_DESIGN.md
research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md
research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md
```

Capture snapshots all four byte images and records their SHA-256 values in
the original artifact's `source_bindings` object.  Publication reconstructs
the complete compatibility object from the live Paper 02 tree and requires
byte identity with the supplied candidate.  It repeats that live rebuild at
the terminal pre-rename boundary and again after publication, so the final
gate replays all four source bindings rather than trusting quoted hashes.

Consequently the three bound formal documents and the adapter source must be
stable before a fresh role-13 candidate is captured.  Any later edit to any
of those four roles makes the earlier candidate stale and non-publishable.
There is no cycle: the adapter fixes the role-13 path but contains no
role-13 digest, and the compatibility object contains no self-hash.

## 4. Exact-exclusive CLI

From the exact live Paper 02 root, capture mode is:

```text
python scripts/replay_r401_val_l3_s0_through_a1_checkers.py \
  --capture-s0-compatibility \
  --output /tmp/EXACT_NEW_COMPATIBILITY_CANDIDATE.json
```

Publication mode is:

```text
python scripts/replay_r401_val_l3_s0_through_a1_checkers.py \
  --publish-s0-compatibility \
  --candidate /tmp/EXACT_COMPATIBILITY_CANDIDATE.json \
  --expected-sha256 EXACT_64_LOWERHEX \
  --authority-root EXACT_LIVE_PAPER02_ROOT
```

The two modes are an exact XOR.  Capture requires only `--output`.
Publication requires exactly `--candidate`, `--expected-sha256`, and
`--authority-root`, without `--output`.  Publication accepts no destination
override: the only derived destination is

```text
research/route_a_wave_trace/R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json
```

The authority root must equal the exact live Paper 02 root, not an alias,
fixture root, parent directory, or alternate checkout.

## 5. Temporary capture contract

Capture accepts one canonical absolute `/tmp` leaf outside the project tree.
It uses an exclusive, no-follow create and requires a new regular inode with
mode `0600` and link count one.  The encoded candidate must be nonempty, no
larger than `1048576` bytes, exact `CJ_COMPACT_V1`, strict JSON, and valid
under the unchanged 18-key compatibility schema.  It is flushed, reopened,
and compared with the captured, already source-replayed encoded bytes before
the transient capture receipt is emitted.

Capture does not write the canonical role-13 path and cannot be combined with
publication.  Its receipt is `CAPTURED_VALIDATED_TEMP_ONLY` under
`NON_AUTHORITATIVE_CAPTURE_ONLY`; licensing, production authorization, and
scientific dispatch are false, while component, milestone, theorem, and final
statuses are null.

## 6. Fixed-destination write-once publication

Before allocating or reading candidate content, publication no-follow stats
the candidate through a pinned parent directory and requires:

```text
type = regular file
mode = 0600
nlink = 1
size_bytes in 1..1048576
```

It then uses `O_NONBLOCK|O_NOFOLLOW`, pins and replays the complete file
identity, checks the operator-supplied digest, strict-parses the exact compact
bytes, and reconstructs the live compatibility object from the four source
bindings and sealed S0 controls.  A stale candidate fails before publication.

The fixed canonical destination must be absent.  Every pre-existing entry is
fatal, including a byte-identical single-link regular file; there is no
idempotent role-13 publication success.  Candidate, authority-root, and
canonical-parent namespace identities remain pinned across the transaction.

Publication creates only a fresh hidden same-parent staging inode, initially
exclusive and then explicitly set to mode `0644`.  It writes the exact
candidate bytes, flushes and reopens the stage, replays the source candidate,
the pinned namespaces, all four live source bindings, and the stage, and then
uses Linux `renameat2(RENAME_NOREPLACE)` relative to the pinned canonical
parent.  No link-based, replace-capable, portable-rename, copy, or overwrite
fallback is authorized.  The canonical inode must finish as an exact
single-link `0644` regular file with the expected bytes and digest.

Before rename, cleanup may remove only the inode-matched stage owned by the
current invocation.  Crash residue is noncanonical and conveys no role-13
authority.  Once rename succeeds, any later reopen, byte, source-binding,
namespace, hook, or fsync failure is fail-closed evidence.  It never
authorizes rollback, unlink, repair, overwrite, or a second publication
attempt; recovery is read-only/manual audit of the write-once inode.

## 7. Exact publication receipt and authority ceiling

A completely successful local transaction emits one compact transient
receipt with exactly these 21 keys:

```text
schema_version
protocol_id
artifact_role
artifact_status
authority
candidate_path
canonical_path
compatibility_sha256
size_bytes
mode
nlink
serializer
publication_method
independent_verification_performed
scientific_licensing_enabled
production_authorized
scientific_dispatch_performed
component_status
milestone_status
theorem_status
final_status
```

Its exact authority boundary is:

```text
artifact_role = S0_COMPATIBILITY_PUBLICATION_RECEIPT
artifact_status = PUBLISHED_WRITE_ONCE_NON_LICENSING
authority = ROLE23_ADAPTER_PUBLICATION_ONLY
mode = "0644"
nlink = 1
serializer = CJ_COMPACT_V1
publication_method = SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1
independent_verification_performed = false
scientific_licensing_enabled = false
production_authorized = false
scientific_dispatch_performed = false
component_status = null
milestone_status = null
theorem_status = null
final_status = null
```

The adapter's own post-rename byte/source replay is not independent
verification, so `independent_verification_performed` remains false.  The
receipt is stdout metadata, not the role-13 artifact and not a role-54,
production, checker, theorem, release, or dispatch authorization.

## 8. Evidence ledger and next edge

The implementation owner declared the adapter and focused-test bytes stable
before candidate capture.  The three source-bound formal documents are also
locked at this prepublication snapshot.  Their exact hashes and the
implementation-only replay are:

```text
s0_compatibility_adapter_sha256 = a00117303874eec16c7d116f344179c1e586856046cb725efb92c7b8c22640b0
s0_compatibility_test_sha256 = f93832a2de731bad2972a08534adf5c8001c84805e57f01c5970a810bae2e95d
prefreeze_design_sha256 = 5162c163f158511aefc3b204060755ef5275725d7d567140ad04a3f936967291
checker_contract_sha256 = c53a21f8de39940be276629cadc328ba214d5743e7214678d4ebb79a8359d33c
release_contract_sha256 = 0b03ced880be3da0b6022de83861bdfb1e4fa99df9888acbfce97cd806a0872c
focused_tests = 72/72
focused_seconds = 1.42
nine_module_regression = 521/521
nine_module_seconds = 165.35
paper02_regression = 916/916
paper02_seconds = 223.44
python_compile = PASS
implementation_owner_diff_check = PASS
independent_implementation_review = ACCEPT_P0_0_P1_0_P2_0
```

The focused module and both broader suites used only sealed S0 reads, mocks,
and temporary fixtures and invoked no scientific evaluator.  Canonical role
13 remained absent before and after all three runs.  These values establish
implementation bytes; they are not a candidate digest, canonical role-13
identity, receipt, freeze, or dispatch authority.

The current next edge is therefore ordered as follows:

1. preserve the locked adapter and three formal-document bytes listed above;
2. verify the implementation-only hash/test ledger against that stable tree;
3. capture a fresh `0600` candidate at a new `/tmp` path;
4. only under a separate explicit authorization, execute the fixed
   no-replace role-13 publisher; and
5. only after role 11, role 12, role 13, and every other input are final,
   consider construction of downstream role 54.

This increment performs none of steps 3--5.  Canonical role 13 remains absent.
No scientific evaluator was invoked, no production was authorized, and the
component, milestone, theorem, and final statuses remain null.
