# A4.16 L3-A1 role-10 machine-publication implementation increment

Date: 2026-08-10 (UTC)

Protocol family: `R401-VAL-L3-A1`

Repository baseline before this increment:
`b1f4a36baff9c38a04d46c7a4aa5087a849b0d77`

Authority: **NON_LICENSING / engineering publisher implementation /
canonical role 10 absent / no role 54 / no scientific dispatch**

## Outcome and exact boundary

This increment implements a one-shot role-19 publication surface for a
separately captured and independently checked machine-freeze candidate.  It
does not execute that surface and does not create the canonical artifact.
At the recorded implementation bytes:

```text
machine_publisher_implemented = true
canonical_machine_role10_exists = false
main_freeze_role54_exists = false
prefreeze_accept_exists = false
production_authorized = false
dispatch_authorized = false
component_status = null
milestone_status = null
theorem_status = null
final_status = null
```

The prospective machine object retains
`authority=MACHINE_ADMISSION_ONLY`,
`scientific_licensing_enabled=true`, and
`production_authorized=false`.  The licensing Boolean is only a capability
of the machine-admission schema.  It is not production, scientific,
milestone, theorem, final, or dispatch authority.

## Acyclic role order

The ordered main-freeze input map has exactly 53 roles.  The canonical
machine freeze is input role 10, the capture/publisher tool is role 19, and
the independent release-side verifier is role 24.  The main freeze is not
one of those 53 inputs: it is downstream release role 54 and may be generated
only after all 53 input roles have stable final bytes.

The publication order is therefore:

```text
stable current live on-disk role-19 source bytes + stable role-24 verifier bytes
  -> fresh temp-only machine candidate binding only the role-19 source bytes
  -> role-24 verify-only replay of the temporary candidate
  -> explicit one-shot role-19 publication to the fixed role-10 path
  -> separate role-24 verify-only replay of the published role-10 bytes
  -> remaining roles 1--53 become final and receive the independent review
  -> role-54 main freeze, only after all 53 inputs are final
```

There is no self-cycle.  The machine object contains neither its own digest
nor a role-10 role-map entry.  It binds the capture tool path and role-19
digest.  Role 24 is not imported by role 19 and is not embedded as a machine
self-hash; roles 10, 19, and 24 are later co-bound only by the downstream
ordered 53-role main-freeze map.  Role 19 and role 24 must remain immutable
after their respective role-10 publication and verification edges.

The temporary candidate recorded by the preceding capture increment binds
the preceding role-19 bytes.  Changing role 19 to add this publisher makes
that candidate historical rather than publishable.  A fresh candidate must
be captured and independently replayed only after the publisher bytes are
stable.

## Exact role-19 CLI and fixed destination

From the Paper 02 directory, the implemented surface is:

```text
python scripts/run_r401_val_l3_a1_all_slabs.py \
  --publish-machine-freeze \
  --candidate ABSOLUTE_TMP_CANDIDATE_PATH \
  --expected-sha256 EXACT_64_LOWERHEX \
  --authority-root EXACT_PAPER02_ROOT
```

This mode is exact-exclusive from capture, mock, initialize, resume,
production, and scientific-execution modes.  It accepts no output or
destination override.  Role 19 derives the sole destination from the exact
authority root and the fixed role-10 relative path:

```text
research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json
```

The expected digest is an explicit byte-intent pin.  Operationally it must be
the digest independently recomputed by role 24 on the temporary candidate;
role 19 cannot infer or manufacture the history of that separate invocation.
The publisher independently hashes and fully validates the same captured
candidate bytes again before publication.

## Source-candidate and machine-envelope gate

The candidate must be the strict 23-key `MACHINE_FREEZE` object produced in
`CJ_COMPACT_V1`, at an exact absolute regular single-link path in the allowed
temporary namespace.  Its exact byte size must be in the closed integer range
`1..1048576`; the frozen maximum is
`MACHINE_PUBLICATION_MAX_CANDIDATE_BYTES=1048576`.  Through the pinned parent,
role 19 first performs a no-follow pre-open stat and requires a regular
single-link file, exact mode `0644`, and size in that range.  Only then does it
open with `O_NONBLOCK|O_NOFOLLOW`, compare the opened identity to the pre-open
identity, capture the bounded raw bytes and inode metadata, and repeat the
identity check.  It requires the supplied digest to equal the raw-byte SHA-256
and replays the complete live machine envelope.  In particular it requires:

- `capture.capture_tool_path` to be the fixed role-19 scheduler path and
  `capture.capture_tool_sha256` to equal the stable current live on-disk
  role-19 source bytes, whose path, hash, device/inode, size, timestamps,
  mode, and link identity remain unchanged across the transaction;
- the current boot, Python/Conda/Arb, CAPD, compiler, persistent ELF,
  runtime-library, filesystem, and public resource bindings to replay;
- `artifact_role=MACHINE_FREEZE`, `status=FROZEN_FOR_PRODUCTION`, and
  `authority=MACHINE_ADMISSION_ONLY` only within the closed machine schema;
- `production_authorized=false` and all four scientific result statuses
  null; and
- no self-hash, release authority, main-freeze authority, or dispatch flag.

Immediately before the no-replace operation, role 19 repeats the complete
live machine-envelope, role-19-hash, boot, candidate-byte, and candidate-inode
checks.  The source candidate remains an input: it is not moved, linked,
renamed, truncated, deleted, chmodded, or otherwise mutated.  Its path, full
lexical parent-chain device/inode/type signatures, leaf device/inode, bytes,
digest, size, nanosecond modification/change timestamps, mode, and link count
must remain unchanged across the operation.

## Same-parent write-once publication

Publication uses only a new hidden staging inode in the canonical role-10
parent directory.  Its basename is exactly
`.R401_VAL_L3_A1_MACHINE_FREEZE.json.publish-` followed by 32 lowercase hex
digits.  Role 19 creates it exclusively relative to a pinned parent
descriptor, tries at most 32 independently generated basenames, never adopts
or overwrites a collision or residue, writes the captured candidate bytes,
explicitly sets `0644` rather than trusting the caller's umask, flushes the
complete staging file, and verifies its exact bytes.  It then performs one
Linux `renameat2(RENAME_NOREPLACE)` publication to the fixed canonical basename.
The same private bounded reader enforces `1..1048576` bytes on staging and
canonical reopen; both must additionally equal the captured candidate size
and bytes exactly.
The exact method literal is
`SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1`.  Role 19 reopens the canonical
path without following symlinks to verify raw bytes, digest, size, mode, link
count, and the published inode identity; it flushes the published file and
the pinned parent directory before success.

Any pre-existing canonical path is fatal, including a regular single-link
file containing byte-identical candidate bytes.  Machine publication has no
idempotent-success branch and never overwrites, replaces, repairs, or
normalizes role 10.  A staging collision, link/path alias, parent or leaf
symlink, hard link, candidate mutation, live-binding change, destination
race, no-replace failure, reopened-inode mismatch, byte mismatch, or flush
failure rejects.

Before the atomic no-replace edge, owned staging bytes may be removed on
failure without touching the candidate.  Once role 10 has been atomically
published, a later local replay, hook, or directory-flush failure is reported
fail-closed but the canonical object is never rolled back, unlinked,
overwritten, or retried as idempotent success.  Only the independent role-24
read-only replay may classify the surviving object.

The three recovery classes are asymmetric:

```text
pre-rename exception                 = NOT_PUBLISHED
owned hidden residue only            = NONCANONICAL_STAGING_RESIDUE_ONLY
rename-edge or post-rename exception = CANONICAL_PUBLICATION_REQUIRES_MANUAL_AUDIT
```

Only the first case permits inode-guarded cleanup of a stage owned by the
current invocation.  A process or power loss at the rename boundary is never
inferred to be either success or safe retry.  Any later canonical leaf makes
a second publisher call fail, and role 24 may only audit it read-only.

## Publication receipt and role-24 post-verification

On success role 19 emits one transient sorted-key compact JSON line.  It is
not a sidecar or a release object.  Its closed fields are:

```text
schema_version
protocol_id
artifact_role = MACHINE_FREEZE_PUBLICATION_RECEIPT
artifact_status = PUBLISHED_WRITE_ONCE_PENDING_INDEPENDENT_VERIFY
authority = ROLE19_PUBLICATION_ONLY
candidate_path
canonical_path
machine_freeze_sha256
size_bytes
mode
nlink
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

`mode` is the string `0644` and `nlink` is the integer `1`.  The receipt is
serialized with the strict compact sorted-key serializer and exactly one
final LF.  `candidate_path` is the exact accepted canonical absolute
candidate spelling, while `canonical_path` is the absolute fixed destination
derived from the exact authority root.  `machine_freeze_sha256` hashes the
candidate/canonical machine bytes; it is not a receipt self-hash, and the
transient receipt has no self-hash.

The receipt reports only role-19 publication facts.  Its status deliberately
remains pending independent verification.  Role 19 imports, invokes, and
spawns neither role 24 nor any evaluator or other subprocess.

Successful CLI exit is zero and stdout is exactly that one receipt line.
Every handled CLI failure exits one, emits no stdout, and writes exactly
`ERROR: <ExceptionType>: <message>` plus one LF to stderr.  An error after the
rename edge still follows the no-rollback rule above.

After publication, the operator must separately run:

```text
python scripts/build_r401_val_l3_a1_release_provenance.py \
  --verify-machine-freeze \
  ABSOLUTE_CANONICAL_ROLE10_PATH
```

The only accepted read-only success remains:

```text
machine_freeze_verification=PASS_MACHINE_FREEZE_VERIFY_ONLY authority=NON_AUTHORITATIVE_VERIFY_ONLY candidate_sha256=<64-lowerhex> size_bytes=<positive-int> promotion_authorized=false
```

The independently recomputed digest and size must equal the role-19 receipt
and the prepublication candidate receipt.  Role 24 performs zero writes and
zero subprocesses.  Its success does not edit the role-19 receipt, does not
create a promotion record, and does not authorize production.  A failure
leaves the write-once role-10 bytes in place for audit and blocks every
downstream freeze action.

## Verification evidence

The stable implementation ledger is:

| Object | SHA-256 |
|---|---|
| role-19 scheduler / capture and fixed publisher | `262985fcb1fc82890501b635bfce163712f1821e2d92276aee9f363ee0473a82` |
| role-26 static-scheduler / capture and publisher tests | `d5a4a018547e3f80f2f1a5375e530eb39120e686cc489925a1cf049a5e3dbf5f` |

From repository root `/root/autodl-tmp/zeta/hilbert-polya-structure`, the
publisher-focused command was exactly:

```text
pytest -q zeta_mvp0/papers/paper_02_certified_local_wave_trace/tests/test_r401_val_l3_a1_static_scheduler.py -k 'machine_publication'
```

It passed `23/23` publisher tests with `107` deselected in `13.70 s`.  The
complete role-26 module command was exactly:

```text
pytest -q zeta_mvp0/papers/paper_02_certified_local_wave_trace/tests/test_r401_val_l3_a1_static_scheduler.py
```

It passed `130/130` tests in `40.35 s`.  The exact compile check was:

```text
python -m py_compile \
  zeta_mvp0/papers/paper_02_certified_local_wave_trace/scripts/run_r401_val_l3_a1_all_slabs.py \
  zeta_mvp0/papers/paper_02_certified_local_wave_trace/tests/test_r401_val_l3_a1_static_scheduler.py
```

It returned zero with empty stdout/stderr; `git diff --check` also returned
zero with empty output on the same implementation boundary.

The separate final nine-module L3-A1 regression passed `480/480` tests in
`164.03 s`.  The complete Paper 02 regression then passed `875/875` tests in
`218.37 s`.  Both broader runs used the same locked role-19/role-26 bytes,
performed no canonical role-10 publication, and invoked no scientific
evaluator.

The focused suite covers the exact 21-key receipt, fixed destination,
`1..1048576` bounded pre-open type gate, digest and live-role drift, symlink/
hard-link/path/namespace mutations, every pre-existing destination type,
staging collision/residue, rename race, pre- and post-rename crash boundaries,
source and role-19 terminal mutation, CLI XOR/stdout/stderr, no rollback, and
zero subprocesses.  All success fixtures use isolated temporary authority
roots.  No test invoked a scientific evaluator or created the canonical
role-10 path in the repository.

## Exact absence and remaining gate

At completion of this implementation increment, no canonical
`R401_VAL_L3_A1_MACHINE_FREEZE.json`, canonical
`R401_VAL_L3_A1_FREEZE.json`, canonical S0 compatibility replay, pre-freeze
test record, accepted pre-freeze review, run config, production result,
report, or release exists.

The next bounded authority action is not role 54 or scientific execution.  It
is to stabilize and review the publisher implementation, capture a new
candidate bound to those stable role-19 source bytes, independently verify the
temporary bytes, and only under separate publication authorization execute
the one-shot role-10 operation followed by role-24 verification.  All 53
inputs and the exact `Verdict: ACCEPT_FOR_FREEZE` review must then become
final before downstream role 54 can be constructed.

This increment asserts no A4.16 all-slab theorem, global tube routing, trace
formula, Hilbert--Polya operator, zeta-zero reconstruction, RH conclusion, or
implication toward RH.
