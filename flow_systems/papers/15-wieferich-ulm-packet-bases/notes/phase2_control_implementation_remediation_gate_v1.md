# Replacement Paper 15 control-implementation remediation gate v1

Status: **PASS TO ONE REPLACEMENT SIX-PATH SOURCE REIMPLEMENTATION ONLY — CURRENT PROVISIONAL SNAPSHOT REMAINS REVISE**  
Version: `P15R-P2-CONTROL-IMPLEMENTATION-REMEDIATION-GATE-v1.0`  
Date: 2026-08-17 (Asia/Shanghai)  
Final control design: **PASS — C0/M0/m0**  
Current provisional implementation accepted or frozen: **no**  
First implementation attempt consumed: **yes**  
Generated artifacts authorized here: **no**  
Control execution or reproduction authorized here: **no**  
Universal prime recovery: **OPEN_NOT_AUTHORIZED**  
Route B: **false**

## Material Passport

- Origin Skill: ARS academic-research-suite experiment integrity,
  reproducibility, code-runner, and workflow discipline
- Origin Mode: owner/orchestrator source-remediation admission after a
  read-only static failure audit
- Origin Date: 2026-08-17
- Verification Status: `PASS_TO_ONE_REPLACEMENT_SOURCE_ATTEMPT_ONLY`
- Version Label: `p15r_phase2_control_implementation_remediation_gate_v1`
- Scope: one new implementation author may replace the six exact provisional
  source files, within those same six paths only, and then publish one stable
  external source-freeze receipt for a fresh independent static review
- Explicitly outside scope: import or execution of project code, generator or
  verifier invocation, unit tests, shell sourcing, top-level reproduction,
  runtime platform probing, lock or private-root acquisition, CSV or manifest
  generation, another repository path, proof work, Route A/B, composition,
  manuscript or figure work, release, archive, Git, and public synchronization

This gate is a governance repair, not a design amendment and not an
implementation review.  It does not accept any current source byte.  It
authorizes replacement source authoring only because the first attempt is
consumed, the current six files are explicitly provisional and REVISE, and
no Section-6 source freeze under the original implementation gate ever
became effective.

## 1. Exact authority and current-byte receipts

### 1.1 Governing implementation and final design

The target of this gate was confirmed absent before this file was created.
The original implementation gate and the final independent design review
were freshly read in full and independently re-hashed:

| Package-relative path | Lines | Bytes | Recomputed SHA-256 |
|---|---:|---:|---|
| `notes/phase2_control_implementation_gate.md` | 735 | 35164 | `e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8` |
| `notes/phase2_control_design_peer_review.md` | 3961 | 209656 | `3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b` |

The final review's active effective-design tuple is base plus v1 through v8
in exact order.  Every member was freshly re-hashed on its complete current
bytes:

| Effective member | Lines | Bytes | Recomputed SHA-256 |
|---|---:|---:|---|
| `notes/phase2_control_design_lock.md` | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` |
| `notes/phase2_control_design_amendment_v1.md` | 931 | 49257 | `cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe` |
| `notes/phase2_control_design_amendment_v2.md` | 1750 | 98006 | `c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea` |
| `notes/phase2_control_design_amendment_v3.md` | 986 | 43781 | `f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b` |
| `notes/phase2_control_design_amendment_v4.md` | 996 | 43881 | `f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592` |
| `notes/phase2_control_design_amendment_v5.md` | 411 | 20580 | `2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8` |
| `notes/phase2_control_design_amendment_v6.md` | 1498 | 80822 | `0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363` |
| `notes/phase2_control_design_amendment_v7.md` | 1199 | 60145 | `bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7` |
| `notes/phase2_control_design_amendment_v8.md` | 884 | 45610 | `e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147` |

Amendment v5 is the frozen blocked/no-op provenance member and contributes
no operational repair.  The final review retains all nested append-only
prefixes and ends at `PASS_C0_M0_m0`.  The corrected design-remediation
gates v1 through v8 were also re-hashed at the exact digests already bound
by the implementation gate:

```text
v1=98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16
v2=00045134aed2b21bc0046dda9c0bc87119f6943a15ed9674b337d7137be0a705
v3=e367e632490cb03ef9bc066b52ca8259988669949a237a04c0b15770240479ac
v4=df1ae4b43615f0f824681b13698256bac215fc593e590b29e32bf34c44065647
v5=55f655b6bcf6e62972c7fdc3301c9177a57df9c25602f0a61a13d8f06bf599d7
v6=a1950889a0b2ce632627194a1f26151db6b3c9771db971257df33cfa1f53cf00
v7=a27ab525537fe41e2917713fd0b2462c6b6efe41c96c5f277de4c48d85ccd576
v8=342faf7880ed80bc1406792953c3d64b8ae057740f2d4b2e12d9543612308de8
```

No authority byte drift was observed.  This gate does not reinterpret or
supersede any effective-design clause.

### 1.2 Exact provisional-source quarantine receipt

The first implementation author supplied a REVISE snapshot.  A fresh
read-only inventory, `lstat`, complete byte read, line/byte count, and
SHA-256 pass independently reproduce it:

| Exact provisional path | Type | Mode | nlink | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---:|---:|---|
| `code/generate_controls.py` | regular | `0644` | 1 | 1046 | 54695 | `156d027576e97361e21b0714d09220a7c70700f57e36ed35a38f91230b21961f` |
| `code/test_controls.py` | regular | `0644` | 1 | 716 | 50602 | `e1a65fd3947259a8ac071ad3d6ede577d4d9283e58e67ae9c9e09d1a3f417fa4` |
| `code/README.md` | regular | `0644` | 1 | 42 | 2267 | `12de45fb6b2aebf6a7a9376c35e3c4c0aebb84e442b7cf7d438c9b0a9941ce46` |
| `experiments/reproduce.sh` | regular | `0644` | 1 | 1449 | 83980 | `d7339450ba4d26f63bb397db27563e2cbb9cb452d8a0295d0a99b6e2721ab558` |
| `experiments/README.md` | regular | `0644` | 1 | 49 | 2660 | `df7933a3b7d61deaa68a68c43e3756f6d0213aa6d4791bf88fe3f73b75be89eb` |
| `results/README.md` | regular | `0644` | 1 | 49 | 2038 | `864a8be34c2c352bd6e08574a642ea9a4eb479800ddb9fc90980ee0a8584c370` |

The tuple totals 3,351 lines and 196,242 bytes.  The complete current
inventories of `code/`, `experiments/`, and `results/` contain exactly those
six paths.  All nine generated paths are absent; no cache, lock, helper,
fixture, temporary file, or extra directory was observed.

This table is a **quarantine/start receipt only**.  It is not the original
gate's Section-6 source freeze, a manifest input, an accepted implementation
receipt, or permission to run.  No provisional hash may be copied forward
as an expected final hash.

### 1.3 Audit method and non-execution receipt

The source audit used only complete text reads, exact hash/count/inventory
operations, and static call-site/state/ownership comparison against the
effective design.  It did not import either Python source, compile or
execute project code, source or invoke the shell wrapper, call a project
function, create a socket or namespace, probe the kernel, acquire a lock,
create a root, generate a CSV/JSON byte, or run a test.  No project file was
written before this sole gate.

## 2. Governance determination and exact narrow supersession

### 2.1 Why attempt one is consumed and cannot continue by implication

The original implementation gate Section 4.1 authorized one implementation
author to create six then-absent paths and required the transaction to stop
if any target already existed at its start.  Those six paths now exist.
Creation of the first target consumed that admission even though the
resulting tuple did not become acceptable.

The same gate permits edits during one not-yet-frozen authoring transaction,
but it is expressly not a license for a second author or second design.
Therefore a replacement author cannot infer overwrite authority from the
old gate, from the provisional author's REVISE label, or from the mere
absence of generated artifacts.

### 2.2 Why no source freeze or review authority attached to these bytes

The original gate Section 6.1 requires one stable external receipt binding
all six final path/type/mode/nlink/line/byte/hash values, the gate, complete
design authority, exact source inventory, generated-path absence, static
check receipts, and zero execution attempts.  No such accepted final receipt
was fixed.  The supplied hash tuple is explicitly provisional and REVISE.

Consequently:

```text
ATTEMPT_1_CONSUMED=true
ATTEMPT_1_SOURCE_FREEZE_EFFECTIVE=false
ATTEMPT_1_INDEPENDENT_REVIEW_ADMITTED=false
ATTEMPT_1_IMPLEMENTATION_ACCEPTED=false
ATTEMPT_1_EXECUTION_AUTHORITY=false
```

The current bytes cannot be reviewed as if Section 6.1 had passed, cannot
be used to seek an execution gate, and cannot be silently repaired after a
fictional freeze.

### 2.3 Owner authority for this remediation gate

A primary owner/orchestrator may issue this narrow successor because it
does not change the final control design, implementation inventory,
generated inventory, manifest schema, authority-binding count, or DAG.  It
is a governance note beneath `notes/`, outside all three checked-in source
scan roots.  It is not a seventh implementation path, generated artifact,
manifest member, authority binding, or lifecycle node.

This gate supersedes only these two admissions in original implementation
gate Section 4.1:

1. the start-time requirement that all six target paths be absent is
   replaced, for this attempt only, by the requirement that all six exist
   as regular nlink-one files and match the exact quarantine hashes in
   Section 1.2 before the first replacement write; and
2. the first author's already consumed cardinality is followed by exactly
   one new replacement implementation author and one bounded replacement
   transaction.

Every other clause of the original implementation gate remains binding.
In particular, this is not a second control design, does not add a source or
helper, does not alter the frozen manifest binding named
`implementation_gate`, and does not insert this remediation note into the
manifest or the `A,D,R,G,I,C,M,V` adjacency.  The future manifest continues
to bind the original implementation gate and the eventual six final source
digests exactly as frozen by the design.

## 3. Blocking provisional-source findings

These findings determine only that the current snapshot is unsuitable for
freeze.  They are not a substitute for the future authorized independent
review and do not assign a formal review severity count.

### 3.1 The required P/L/G object model is not on the reachable entry path

The effective design requires a real single-threaded host coordinator P,
an atomically placed launcher L, and L's sole later child G as inner PID 1,
with the exact U1/U2 mapping, mount/PID/proc, cgroup, source-capability,
bootstrap-control, privilege-drop, and reap sequence.

The provisional wrapper instead enters `main -> Workflow().run()` at lines
1435--1448.  Its source contains constants for `CLONE_NEWUSER`,
`CLONE_NEWNS`, `CLONE_NEWPID`, and `SYS_UNSHARE`, but no call implementing
that namespace sequence and no reachable P/L/G bootstrap.  Its
`MutationGuardian` is instantiated as an object in the same workflow
process at lines 1375--1378, not as the required authenticated G process.

There is also a deterministic pre-protocol construction defect.  The
declared `RegisteredRunner` constructor requires `workers_fd`, `control`,
and `records`, while line 1397 calls it with only a `CgroupTree` object and
the records list.  Thus the printed main path cannot reach even its simulated
pre-suite sequence.  Constants, class bodies, comments, and unreachable
branches are not an implementation of an object model.

### 3.2 The v3 owner/admission/descriptor and object ledgers are not owned by P and G

The design requires six exact session-zero G children, P-derived admission,
two independent P descriptor audits around the four-phase barrier, and
creator-specific pre-access/post-reap object registration.  The provisional
`RegisteredRunner` constructs, admits, starts, drains, reaps, and records
children inside one object.  It appends its own `CHILD_ADMITTED` and `START`
records and has no authenticated distinct P verifier on the live path.

Its generation/lock/root cleanup also reintroduces the forbidden
identity-check-to-pathname-delete window.  `OwnedDirectory.dispose` checks a
path, closes the retained FD, reopens the path, and finally calls pathname
`rmdir` at lines 439--456.  `PackageLock.release` likewise checks the path
and later removes that pathname at lines 620--625.  These operations do not
implement v2's private-namespace retained-capability deletion and may not be
preserved as an equivalent primitive.

### 3.3 The v7 FD-5 and D-M1 session protocol is declarative, unwired, and causally incomplete

The exact twelve requester--P FD-5 forms and exact twelve D-M1 P--G session
forms appear as constant tuples.  The only `AuthSession` class occurs at
lines 548--596 and has no construction/call site from the reachable main.
The provisional runner creates an audit socketpair at lines 1234--1238,
passes FD 5 to the child, never services the P-held peer, and closes that
peer at line 1296.

The actual test worker instead sends package and receipt requests directly
through `P15R_GUARDIAN_RPC_FD` in `code/test_controls.py` lines 379--402,
480, and 625.  That is the FD-4 guardian lane, not the P-owned FD-5 direct
witness.

Even the unreachable `AuthSession` body is not the frozen v7 algorithm: it
does not send the exact create receipt before actual FD-4 create, does not
validate `CREATE_ACCEPTED` raw capability and immutable first-buffer bytes,
uses fixed placeholder coordinates, does not perform the exact activation
join/receipt, accepts important records by `startswith`, and fabricates a
terminal reply as `PASS`.  A list of form names cannot establish their
direction, exact codec, cardinality, owner, causal secret boundary, state,
failure, replay, or tombstone contract.

### 3.4 D-M2 actual-FD possession evidence is unreachable and its preflight is the wrong object

`FDAuditor.audit` is defined at lines 464--545, but no reachable call
constructs `FDAuditor` or invokes `audit`.  The ordinary preflight at lines
366--390 opens a pidfd for `os.getpid()` and duplicates its own FD.  That is
not the required actual nested dumpable-zero child/guardian
`PREFLIGHT_PROBE/FD8` row, four retained proc capabilities, two live
descriptor snapshots, reciprocal child/G peer correlation, common reverse
unwind, immediate per-acquisition EBADF proof, holder restoration, and ABA
closure.

The four quiescence form strings and an unused parser do not prove G was
quiescent across any actual P snapshots or acquired duplicates.

### 3.5 The v8 terminal-reap and global final lifecycle is unreachable

`global_final` is defined at lines 1351--1366 and is never called.  The
unreachable `AuthSession.terminal` stops after sending the inherited
`CHILD_REAPED_ACK`; it does not keep the same authenticated P--G control
live through `AUTH_REAP_RECONCILED`, the inherited global
`FREEZE_REQUEST -> FROZEN_FINAL -> KILL_REQUEST -> KILL_ISSUED -> REAPED ->
CGROUP_EMPTY -> CLEANUP_RESULT* -> optional SIGNAL_CLEANED -> EXIT`, G exit,
P pidfd reap, populated-zero, and ordered cgroup disposal.

The reachable runner reaps a child itself, closes its pidfd, emits a local
record, and even returns the already closed pidfd at lines 1290--1298.  It
does not implement v8's separate P/G ownership, exact requester mapping,
FD-4 anomaly-free drain, FD-5 clean EOF, reap record/ACK join, early-EOF
failure, or total tombstone semantics.

### 3.6 The oracle and receipt paths contain same-source and hard-coded acceptance

`code/test_controls.py` lines 617--624 construct a synthetic tuple called
`baseline` and hand-edit a mode or mtime value.  They do not clone an actual
whole-root receipt collected from the real filesystem, so they cannot be
the v2 exact-one-coordinate mode and `mtime_ns` falsifiers.

The guardian's `serve_receipts` at wrapper lines 1016--1024 actually checks
only one valid fixture and one P01-malformed fixture, then emits a canned
string claiming mode, mtime, ctime, transient, and root rejection plus
cleanup proof.  Those unperformed variants are not evidence.  Likewise the
package-test side maps a requested case directly to an expected detector
string.  A guardian assertion, expected-token lookup, self-equality, or
hard-coded `cleanup=PROVED` cannot replace the independent causal oracle and
real receipt operations.

### 3.7 Consequence

The defects span process authority, descriptor ownership, causal wire
protocol, possession proof, terminal lifecycle, cleanup, and oracle
independence.  Connecting a few currently unused classes, adding form names,
or changing expected strings would retain the same invalid architecture.
The current snapshot therefore remains:

```text
PROVISIONAL_SOURCE_VERDICT=REVISE
SOURCE_FREEZE_AUTHORIZED_ON_CURRENT_BYTES=false
INDEPENDENT_REVIEW_AUTHORIZED_ON_CURRENT_BYTES=false
EXECUTION_AUTHORIZED=false
```

## 4. Mandatory replacement contract

### 4.1 Full-design derivation, not local pseudo-repair

The replacement author must rederive the implementation from the complete
base-plus-v1--v8 effective design and the original implementation gate.
Every current byte is untrusted source material.  No provisional block is
accepted merely because it contains a correct constant, plausible class,
comment, state name, hash, expected token, or README claim.

Before the first source write, the replacement author must publish outside
the repository one complete rewrite plan which:

1. maps each effective-design contract to one of the exact six paths;
2. draws the real P/L/G process tree and names the owner of every long-lived
   process, pidfd, proc capability, cgroup capability, filesystem
   capability, FD-4/FD-5/FD-8 endpoint, audit duplicate, entropy value,
   request ledger, object ledger, and terminal state;
3. enumerates the closed direction/state/cardinality tables for bootstrap,
   admission, v7 FD-5, D-M1 P--G, D-M2 quiescence, inherited child/object,
   and v8 final records;
4. maps every success and failure edge, including partial send, EOF, crash,
   wrong-first, duplicate, replacement, cleanup, unwind, and tombstone;
5. maps all 173 literal methods, 35 semantic chains, 28 package classes,
   whole-root receipts, and the two actual-receipt coordinate probes to an
   oracle that does not trust subject or guardian expected values; and
6. lists every provisional block proposed for retention, with its design
   derivation and independence/reachability rationale, and every block that
   will be deleted or replaced.

The plan is an external authoring checkpoint, not a seventh file.  A plan
that proposes only to call the unused classes, repair line 1397, add token
checks, or preserve the single-process workflow is rejected before source
write.

### 4.2 Exact six-path boundary

The only writable paths are, in this order:

```text
code/generate_controls.py
code/test_controls.py
code/README.md
experiments/reproduce.sh
experiments/README.md
results/README.md
```

No backup, patch receipt, temporary file, helper, service, module, fixture,
generated binding, package metadata, lock, cache, log, CSV, JSON, or seventh
source is authorized.  Parent directories already exist and may not be
replaced, linked, mounted, or widened.  All six final paths must be regular,
non-symlink, nlink-one files.

The replacement transaction may edit these six files repeatedly while the
same authoring transaction remains active and no freeze receipt exists.
The first write to any one consumes the sole replacement attempt.  It does
not authorize a concurrent author, a restart by another author, or a later
repair after freeze.  Drift of any Section-1.2 starting hash before the
first write, or a write outside these six paths, stops this authority.

### 4.3 Exact path responsibilities retained

The original implementation gate Section 4.2 remains exact:

- `code/generate_controls.py` is the sole deterministic subject with only
  the exact verify-only and generate interfaces, canonical 8-CSV/120-row
  and manifest bytes, fourteen authority bindings, effective-amendment
  dereference, exact whole-root metadata receipts, and capability-relative
  fresh-root creation;
- `code/test_controls.py` is the independent 173-literal-method oracle with
  separate primitive algorithms, the 35 exact causal chains including
  unparameterized `SG_SCOPE`, real exact-one-coordinate receipt probes, and
  28 operational package classes requested without expected detector
  authority;
- `experiments/reproduce.sh` contains the shell prefix and the one complete
  byte-bound operational implementation of the real P/L/G process tree,
  platform preflight, cgroup/namespaces, worker admission, RPC and audit
  endpoints, D-M1/D-M2, object and cleanup ledgers, two generations,
  three-way identity, suite, residue, signals, and v8 final lifecycle;
- the three READMEs state only the exact interfaces, inventories,
  platform/threat ceiling, and present no-execution/no-generated-artifact
  status.  They must not convert source presence or static host facts into a
  runtime PASS.

Python remains standard-library plus the already frozen direct Linux UAPI
inside `reproduce.sh`; no external helper or opaque authority is legal.

### 4.4 Reachability and ownership acceptance floor

Static review must be able to trace from the sole entry, not merely find a
definition, to all of the following:

1. P performs the pre-write gates, creates and retains the initial-root
   cgroup/proc/pidfd/diag/control authorities, atomically creates L in the
   guardian cgroup, validates U1/U2 and G as inner PID 1, and never owns G's
   private filesystem paths;
2. L performs only the exact bootstrap and exits/reaps before READY;
3. G alone owns the private mount/tmpfs, package lock, roots, members,
   child creation, RPC, object ledgers, capability-relative cleanup, and
   direct-child reap, while P independently validates the frozen facts;
4. the six pre-suite rows and every later method child use the exact v3
   owner/role/admission/FDSET/barrier/order tables, with P's two real audits;
5. P owns the sole requester FD-5 peer, G owns the sole FD-4 peer, neither
   lane is substituted for the other, and the exact v7 twelve/twelve forms
   are handled by one closed parser/dispatcher with no prefix or alias
   acceptance;
6. D-M2 uses actual `pidfd_open`/`pidfd_getfd` duplicates against the exact
   nested child and G, the exact v4 Unix-diag ABI, quiescence across both
   snapshots, common total unwind, immediate EBADF, restored-holder proof,
   and both ABA exclusions;
7. v7 create, active, and terminal secrets are P-only at their frozen
   causal edges, including immutable first-FD4-buffer acceptance and the
   explicit non-Byzantine-G/first-active-use ceiling; and
8. v8 holds the same P--G control through requester receipt/EOF/reap,
   inherited `CHILD_REAPED/ACK`, `AUTH_REAP_RECONCILED`, the retained global
   final sequence, validated EXIT, exact G reap, populated-zero, and ordered
   cgroup disposal.  EOF alone is never success.

An unreachable class, enum-only assertion, constant count, README statement,
expected-token table, G-only claim, self-pid probe, path-stat fallback,
same-process simulation, hard-coded PASS, or cleanup-after-foreign-delete
does not satisfy this floor.

### 4.5 Oracle and receipt acceptance floor

Every one of the 35 semantic methods must implement the frozen seven-stage
primitive-seed, one-mutation, canonical serialize/reparse, typed projection,
receipt-free predicate rejection, inverse restoration, and receipt-field
counterfactual chain.  Expected class/detector values are compared only
after the primitive predicate has returned its typed result.

The mode and `mtime_ns` probes must each clone one actual filesystem receipt
and change exactly that selected coordinate while every other coordinate,
including the comparator's ctime value, remains byte-for-byte fixed.  A
hand-authored tuple or canned guardian result is forbidden.

Every package method must start from a real independently verified baseline,
perform its exact registered operation in a method-owned G-private fixture,
run the actual byte-bound subject/wrapper through an admitted child, observe
the detector from actual stderr/status under frozen precedence, and complete
the real freeze/reference/capability cleanup proof.  The requester may name
the mutation class and variants; it may not supply or authorize the expected
detector or `cleanup=PROVED` result.

## 5. Replacement authoring and source-freeze protocol

### 5.1 Admission before the first replacement write

The replacement author may begin only after an external coordinator has
published this gate's stable final `path, lines, bytes, sha256` receipt.  The
author must independently re-hash that receipt, the original implementation
gate, final design review, base and v1--v8, and all six Section-1.2 start
files.  Any mismatch stops before source write.

Exactly one replacement author is admitted.  The provisional author and
this gate author do not silently continue as a second concurrent author.
The replacement author must acknowledge in the external plan:

```text
PROVISIONAL_SNAPSHOT_IS_FREEZE=false
ATTEMPT_1_IS_CONSUMED=true
REPLACEMENT_ATTEMPT_BUDGET=1
WRITABLE_PATHS=6
EXECUTION_AUTHORITY=false
```

### 5.2 Permitted author-side checks

The original implementation gate Section 5 remains the closed permitted
set.  Complete text/byte reads, hashes, `lstat`/`fstat`, canonical-path
checks, Python lexical/AST parsing, in-memory compile without import or
execution, nonexecuting shell syntax parsing, and in-memory literal/count/
state/call-site reconstruction are permitted only with bytecode/cache
creation disabled and complete before/after inventory receipts.

The author may not import a project module, call a project function,
instantiate a test class, source the shell, invoke either CLI, create a
socket/namespace/cgroup/root/lock, or run a generator, verifier, unittest,
or top-level wrapper.  Removing residue after an unauthorized action does
not restore validity.

### 5.3 One final external source freeze

After all six files are complete, the replacement author stops writing and
publishes one external receipt in the exact path order above containing:

```text
path, type, mode, nlink, lines, bytes, sha256
```

It must additionally bind:

- this remediation gate's externally computed final hash/lines/bytes;
- original implementation gate, final design review, base, and v1--v8
  hashes;
- the Section-1.2 quarantine tuple as the consumed start state;
- exact current inventory of `code/`, `experiments/`, and `results/`;
- absence of all nine generated paths and all caches/residue;
- every permitted static check's complete before/after metadata receipt;
- an explicit six-path change/retention map to the external rewrite plan;
- `PROJECT_CODE_IMPORTED=false` and `PROJECT_CODE_EXECUTED=false`; and
- zero generator, verifier, test, wrapper, platform-probe, or run attempts.

Only that complete receipt freezes the replacement bytes.  A partial tuple,
self-predicted digest, copied provisional hash, or source change after the
receipt invalidates the freeze and stops.  This gate supplies no third
implementation attempt or post-freeze patch authority.

## 6. Fresh independent static successor review

Only after the replacement freeze is stable may one fresh independent
reviewer create the already reserved target:

```text
notes/phase2_control_implementation_peer_review.md
```

The reviewer must read this gate, the original implementation gate, the
complete effective design, final design review, the external rewrite plan
and freeze receipt, and all six exact final source bytes.  It must repeat
the permitted static/in-memory checks independently and treat the author's
plan, hashes, comments, constants, READMEs, source assertions, and claimed
reachability as untrusted.

In addition to every original-gate Section-6.2 obligation, the reviewer must
explicitly attack:

- the real P/L/G process and authority split from the sole entry;
- all six fixed pre-suite children and every method child admission;
- FD-5 P ownership, exact v7 twelve/twelve forms, raw-secret disclosure,
  first-buffer binding, replay, send failure, and tombstones;
- D-M2 actual-FD acquisition, four proc capabilities, quiescence, two
  snapshots, Unix-diag reciprocity, unwind, EBADF, holder restoration, and
  ABA worlds;
- the v8 post-finalization requester-reap/ACK/global-final/EXIT suffix;
- retained-capability cleanup and foreign replacement preservation; and
- the independent causal oracle, real receipt clones, actual package
  variants, detector provenance, and cleanup receipts.

The review imports or executes no project code and performs no runtime
probe.  Its only clean verdict is `PASS_C0_M0_m0`.  Any critical, major, or
minor finding returns REVISE and blocks every execution or generated action.
It does not authorize a repair; another owner decision would be required.

An independent static PASS would still authorize no run.  The separate
execution gate required by the original implementation gate remains a
future owner decision and must bind this remediation gate, the replacement
freeze, and the independent PASS externally without changing the frozen
manifest schema or DAG.

## 7. Frozen invariants and authorization matrix

This remediation changes no scientific or generated invariant:

```text
IMPLEMENTATION_PATHS=6
CSV_ARTIFACTS=8
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=9
CSV_BODY_ROWS=120
CSV_HEADER_WIDTHS=18,19,22,17,16,19,13,10
EXPLICIT_NEGATIVE_ROWS=35
SEMANTIC_MUTATION_CLASSES=35
PACKAGE_MUTATION_CLASSES=28
UNITTEST_METHODS=173
AUTHORITY_BINDINGS=14
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
PRINTED_DAG_NODES=8
PRINTED_DAG_DISTINCT_EDGES=12
TOLERANCE_POLICY=EXACT_ZERO
NETWORK_USED=false
MANIFEST_SELF_HASH=false
MANIFEST_FUTURE_RESULT_EDGE=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false
```

The exact present authorization is:

```text
P15R_IMPLEMENTATION_REMEDIATION_GATE=P15R-P2-CONTROL-IMPLEMENTATION-REMEDIATION-GATE-v1.0
GATE_VERDICT=PASS_TO_ONE_REPLACEMENT_SIX_PATH_SOURCE_REIMPLEMENTATION_ONLY
CURRENT_PROVISIONAL_SOURCE_VERDICT=REVISE
CURRENT_PROVISIONAL_SOURCE_FROZEN=false
FIRST_IMPLEMENTATION_ATTEMPT_CONSUMED=true

REPLACEMENT_SOURCE_IMPLEMENTATION_AUTHORIZED=true
REPLACEMENT_IMPLEMENTATION_AUTHOR_COUNT=1
REPLACEMENT_IMPLEMENTATION_ATTEMPTS_AUTHORIZED=1
AUTHORIZED_IMPLEMENTATION_PATH_COUNT=6
EXISTING_PROVISIONAL_PATH_OVERWRITE_AUTHORIZED=true
PATH_ADDITION_AUTHORIZED=false
DESIGN_CHANGE_AUTHORIZED=false
MANIFEST_SCHEMA_CHANGE_AUTHORIZED=false
DAG_CHANGE_AUTHORIZED=false

STATIC_IN_MEMORY_SOURCE_CHECK_AUTHORIZED=true
PROJECT_CODE_IMPORT_AUTHORIZED=false
PROJECT_CODE_EXECUTION_AUTHORIZED=false
SHELL_SOURCE_AUTHORIZED=false

GENERATED_ARTIFACT_MATERIALIZATION_AUTHORIZED=false
RESULT_REGENERATION_AUTHORIZED=false
CSV_GENERATION_AUTHORIZED=false
MANIFEST_GENERATION_AUTHORIZED=false
GENERATOR_EXECUTION_AUTHORIZED=false
VERIFY_ONLY_EXECUTION_AUTHORIZED=false
UNITTEST_EXECUTION_AUTHORIZED=false
TOP_LEVEL_WRAPPER_EXECUTION_AUTHORIZED=false
PLATFORM_RUNTIME_PROBE_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
REPRODUCTION_RUN_AUTHORIZED=false
AUTHOR_TOP_LEVEL_RUN_ATTEMPTS_AUTHORIZED=0
INDEPENDENT_TOP_LEVEL_RUN_ATTEMPTS_AUTHORIZED=0

FRESH_INDEPENDENT_STATIC_REVIEW_REQUIRED=true
FRESH_INDEPENDENT_STATIC_REVIEW_AUTHORIZED_AFTER_REPLACEMENT_FREEZE=true
SEPARATE_EXECUTION_GATE_REQUIRED=true
PLATFORM_RUNTIME_VERIFIED=false
FALLBACK_AUTHORIZED=false
AUTOMATIC_RETRY_AUTHORIZED=false

TRUSTED_INITIAL_ROOT_KERNEL_LSM_ADMIN_CEILING_RETAINED=true
BYTE_BOUND_NON_BYZANTINE_G_CEILING_RETAINED=true
ACTIVE_CAP_PER_OPERATION_PROVENANCE_CLAIMED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
PROOF_MODIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ARCHIVE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```

No project code was imported or executed, and no implementation, generated
artifact, platform probe, lock, root, test, reproduction, proof, Route,
composition, manuscript, figure, release, archive, or Git operation was
performed by this gate.  Its final digest is intentionally not embedded.
Only after an external stable receipt of this gate may the one replacement
author begin the bounded six-path reimplementation described above.
