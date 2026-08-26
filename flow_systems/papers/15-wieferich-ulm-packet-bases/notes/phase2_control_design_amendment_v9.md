# Replacement Paper 15 deterministic-control design amendment v9

Status: **FROZEN DESIGN AMENDMENT v9 — P15R-REOPEN-M1 REMAINS OPEN PENDING FRESH INDEPENDENT REREVIEW**  
Version: P15R-CONTROLS-AMENDMENT-v9.0  
Date: 2026-08-17 (Asia/Shanghai)  
Current independent verdict retained: **REVISE — C0/M1/m0**  
Control implementation, source review, or execution performed here: **no**  
Universal prime recovery: **OPEN_NOT_AUTHORIZED**  
Route B: **false**

## Material Passport

- Origin Skill: ARS academic-research-suite experiment, integrity,
  reproducibility, and authoring discipline
- Origin Mode: deterministic exact-byte control-design amendment
- Origin Date: 2026-08-17
- Verification Status: UNVERIFIED_PENDING_FRESH_INDEPENDENT_REREVIEW
- Version Label: p15r_control_design_amendment_v9
- Scope: only the P-to-G privilege-drop release between complete
  LAUNCHER_REAPED and GUARDIAN_READY, its exact attestation, owner states,
  fail-before-write fence, failure tombstone, and the append-only successor
  needed to bind this amendment; no implementation, source review, run,
  result, theorem, Route, manuscript, release, or publication claim

## 1. Exact authority, current verdict, and byte state

### 1.1 Sole amendment gate and reopen authority

The sole target
notes/phase2_control_design_amendment_v9.md was confirmed absent immediately
before its first write.  Before this amendment was written, the complete
authority was freshly read and independently re-hashed:

| Record | Package-relative path | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---|
| remediation gate v9 | notes/phase2_control_design_remediation_gate_v9.md | 1060 | 48563 | c4da0d0684ec64d21ef046abe9686147545e7a1035f7c6f3c8d712972b69dc90 |
| design-reopen gate v1 | notes/phase2_control_design_reopen_gate_v1.md | 434 | 21256 | 8af1bbdca261cc419d090319521a80a80c7c54a8dfb46fa02a257fa18a008973 |
| current append-only design review | notes/phase2_control_design_peer_review.md | 4236 | 223999 | e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1 |

The current review's first 209,656 bytes and first 3,961 lines remain the
byte-identical pre-reopen PASS prefix:

~~~text
HISTORICAL_PASS_PREFIX_LINES=3961
HISTORICAL_PASS_PREFIX_BYTES=209656
HISTORICAL_PASS_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b
HISTORICAL_PASS_PREFIX_VERDICT=PASS_C0_M0_m0
~~~

The later 14,343-byte reopen-review suffix supersedes the current
adjudicative result, not the historical bytes.  At authoring start the exact
current verdict was REVISE_C0_M1_m0 and its sole finding
P15R-REOPEN-M1 was OPEN.  This author document is not independent closure
evidence, does not close or downgrade that finding, and predicts no later
review verdict.

### 1.2 Complete effective design chain

The complete base design and all eight prior amendment records were freshly
read in full and independently re-hashed:

| Effective member | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| notes/phase2_control_design_lock.md | 1183 | 62887 | db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d |
| notes/phase2_control_design_amendment_v1.md | 931 | 49257 | cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe |
| notes/phase2_control_design_amendment_v2.md | 1750 | 98006 | c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea |
| notes/phase2_control_design_amendment_v3.md | 986 | 43781 | f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b |
| notes/phase2_control_design_amendment_v4.md | 996 | 43881 | f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592 |
| notes/phase2_control_design_amendment_v5.md | 411 | 20580 | 2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8 |
| notes/phase2_control_design_amendment_v6.md | 1498 | 80822 | 0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363 |
| notes/phase2_control_design_amendment_v7.md | 1199 | 60145 | bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7 |
| notes/phase2_control_design_amendment_v8.md | 884 | 45610 | e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147 |

Amendment v5 is exactly the blocked/no-op provenance member.  It supplies no
operational state, record, supersession, repair, or authority.  The
operative chain before this file is base plus v1 through v4, blocked/no-op
v5, and v6 through v8.  After this file is externally frozen, the versioned
chain adds v9; this file does not embed, predict, or self-authenticate its
own digest.

### 1.3 Historical implementation governance and source quarantine

The two complete implementation-governance records were freshly read in
full and independently re-hashed:

| Record | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| notes/phase2_control_implementation_gate.md | 735 | 35164 | e5834c01d49465d84baf4540a25321f7bed0ae9bd1f2bc1b688511abb2b6ddc8 |
| notes/phase2_control_implementation_remediation_gate_v1.md | 660 | 32800 | 52a716286a0e46046083f256502820fb5e269913eb7893522ce63b70622b119f |

They bind the old base-plus-v1-through-v8 design and historical
209,656-byte PASS review.  Their original and replacement source attempts
are consumed.  Neither is a design amendment, and neither grants source
authority under the current REVISE verdict or after v9 changes the effective
design.  This amendment does not revive, extend, or reinterpret either
implementation admission.

The six current provisional paths were read only to freeze governance
state.  Their exact quarantine tuple at authoring start was:

| Exact provisional path | Type | Mode | nlink | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---:|---:|---|
| code/generate_controls.py | regular | 0644 | 1 | 1086 | 56136 | d1f1db09edade24a2d6ac48ee943079ecfc51217cd9cd05cc2a8241eaa7be9fc |
| code/test_controls.py | regular | 0644 | 1 | 1239 | 98421 | d2b124daa27040c0df5d19f6a278092b5977b0a37f6c0379cff3ffa6745bc756 |
| code/README.md | regular | 0644 | 1 | 75 | 3722 | 6d270eb371c1a30f3466d5fa7639a590ca669bbbe2213789a89ec797c72f7beb |
| experiments/reproduce.sh | regular | 0644 | 1 | 4452 | 316515 | 930c6f8fc16ab9d64b15c00bc27a526df9057b9b52033ed247d7b6281d3cdc66 |
| experiments/README.md | regular | 0644 | 1 | 94 | 5419 | 266b902f840e70aa3bc872cb9c8ea9ff651f53771e7705524ec56f2311e96959 |
| results/README.md | regular | 0644 | 1 | 55 | 2342 | b49120d0f2a7aba089d4a04b7d83a2fb9b89d3514d2e70768ac1f03fa7517028 |

The tuple is exactly 7,001 lines and 482,555 bytes.  The complete current
inventories under code/, experiments/, and results/ contain exactly those
six regular nlink-one files and no other member or nested directory.  All
nine generated CSV/manifest paths are absent.

This tuple remains quarantined, stopped, unfrozen, unaccepted, and
unreviewable under present authority.  It is not design evidence, an
amendment input, a source-freeze receipt, an accepted implementation, or a
reason to weaken this contract.  No source byte was edited or statically
reviewed here.

### 1.4 Non-execution and sole-write receipt

The authority audit used only complete byte reads, hashes, counts, metadata,
inventory, and static comparison of governance and design text.  It did not
import, compile, parse as project code, source, or execute a project path;
invoke a project function, CLI, generator, verifier, unittest, or wrapper;
create a socket, namespace, cgroup, lock, private root, result, manifest,
cache, temporary file, or generated member; or perform a runtime platform
probe.  This exact amendment is the sole repository write authorized or
performed by the v9 author.

## 2. Exact supersession budget

### 2.1 Sole semantic delta

The complete operational delta is exactly one new authenticated global
bootstrap control form and its necessary owner-state join:

~~~text
new global bootstrap P--G form, exactly one:
  PRIVILEGE_DROP_RELEASE

new P suffix states:
  PRIVILEGE_DROP_RELEASE_SENT
  GUARDIAN_READY_RECEIVED

new G suffix states:
  G_LOCAL_DROP_COMPLETE
  PRIVILEGE_DROP_RELEASE_VALIDATED
  GUARDIAN_READY_SENT

new failure sub-tombstone:
  PRIVILEGE_DROP_RELEASE_FAILED_TOMBSTONE
~~~

LAUNCHER_REAPED_SENT, LAUNCHER_REAPED_RECEIVED, and
PRIVILEGE_DROP_ATTESTED below are owner-qualified spellings of already
required v2 events, not new wire forms.  No acknowledgment, challenge,
nonce, retry, alternate record, second release, compatibility form, or
fallback is authorized.  GUARDIAN_READY remains the only response form.

### 2.2 Exact amendment-v2 surfaces superseded

This amendment supersedes amendment-v2 Section 5.3 only on these affected
surfaces:

1. the bootstrap suffix from LAUNCHER_REAPED through
   PRIVILEGE_DROP_ATTESTED and GUARDIAN_READY, solely by replacing its
   ambiguous shared-state order with the exact P/G suffixes and causal join
   in Section 3.6;
2. creation steps 10 and 11, solely after complete LAUNCHER_REAPED, to
   require P's complete attestation receipt, one release send, G's full
   receive and validation in its already dropped state, and only then
   GUARDIAN_READY;
3. the v2-derived authenticated P--G closed enum, solely by inserting
   PRIVILEGE_DROP_RELEASE immediately after LAUNCHER_REAPED and immediately
   before GUARDIAN_READY at this bootstrap boundary;
4. the exact-payload list, solely by inserting the one payload in Section
   3.1 in that same position;
5. the direction/cardinality sentence which previously gave only
   LAUNCHER_REAPED P-to-G and GUARDIAN_READY G-to-P, solely by replacing it
   with the exact three-record order and cardinality in Section 3.5; and
6. the affected fail-closed and pre-lock wording, solely to impose the
   pre-write fence and total release-failure rules in Sections 3.7--3.9.

No other v2 bootstrap, namespace, mapping, cgroup, source, child, object,
lock, cleanup, signal, exit, framing, credential, ancillary, or retained-
capability clause is superseded.  V4's P-only PEER_ORACLE_PREFLIGHTED
insertion before U1 mapping remains exact and is unaffected.

### 2.3 No later-contract supersession

V9 does not supersede an operational clause in v1, v3, v4, blocked/no-op v5,
v6, v7, or v8.  It composes with the v3/v4/v6 additions to the same global
control enum but changes none of their forms, fields, directions,
cardinalities, states, or ancillary rules.  It changes no D-M1 requester or
session contract, no D-M2 audit contract, and no v8 post-finalization,
requester-reap, CHILD_REAPED/ACK, same-control global-FINAL, EXIT, G-reap,
or cgroup-removal contract.

The later count-nine review receipt extends the review-node history; it does
not semantically weaken or rewrite amendment v8.  Every omitted
base/v1--v8 clause remains binding.

## 3. Exact PRIVILEGE_DROP_RELEASE contract

### 3.1 Form, fields, framing, and field grammar

The sole new payload is exactly one canonical ASCII line without LF, NUL,
or trailing byte:

~~~text
PRIVILEGE_DROP_RELEASE session=DEC g_outer_pid=DEC g_inner_pid=1 g_starttime=DEC guardian_dev=DEC guardian_ino=DEC attestation_sha256=LOWERHEX64
~~~

Fields occur exactly once and in exactly that order.  DEC is the inherited
v2 canonical nonnegative-decimal grammar: zero is exactly 0, a nonzero value
has no leading zero, and sign, whitespace, width variant, or alternate base
is forbidden.  LOWERHEX64 is the inherited exact 64-character lowercase
hexadecimal grammar with no prefix.

The record uses the existing authenticated P--G SOCK_SEQPACKET control
connection.  It inherits the v2 four-byte unsigned big-endian payload
length, 4096-byte ceiling, canonical-ASCII, exact-length, no-trailing-byte,
peer-credential, endpoint-identity, complete-send, complete-receive, and
closed-state rules.  It carries no ancillary item, SCM_RIGHTS object,
SCM_CREDENTIALS override, descriptor, new socket, bootstrap-channel byte,
or requester FD-4/FD-5 byte.  The sole inherited ancillary-bearing rules
remain unchanged.

### 3.2 Exact field bindings

The fields bind only already retained bootstrap identities:

1. session is the exact nonzero bootstrap/global-control session coordinate
   already used by the one accepted WORKERS_CGROUP_FD and
   WORKERS_CGROUP_FD_ACK pair.  It is not a v6/v7 opaque D-M1 auth-session
   coordinate and cannot be freshly allocated for this release.
2. g_outer_pid is the exact canonical outer PID bound by P to G's accepted
   control peer, retained pidfd, stable proc identity, parentage, NSpid
   ending in 1, starttime, and guardian membership.  It equals the outer_pid
   in the already accepted PID1_READY, LAUNCHER_REAPED, and future
   GUARDIAN_READY records.
3. g_inner_pid is the literal 1; no other decimal is legal.
4. g_starttime is the exact canonical decimal starttime from the stable G
   identity already retained independently by P and G.  It is not a wall
   clock, timestamp, elapsed duration, or freshly inferred PID alias.
5. guardian_dev and guardian_ino are the exact device/inode identity of the
   already retained guardian cgroup directory.  P uses its original
   root-owned retained receipt.  Before hiding cgroup2 and closing
   setup-only descriptors, G retains the same immutable pair from its
   successfully validated guardian membership.  No cgroup path string or
   later pathname lookup substitutes for this pair.
6. attestation_sha256 is the exact digest defined in Section 3.3.  It is an
   authenticated P assertion bound to this session, G identity, cgroup,
   denial-probe evidence, probe reap, and fresh raw proc bytes.  It is not a
   secret, capability, nonce, generated artifact, manifest field, or
   independent G observation of P's private probe.

### 3.3 Exact seven-item attestation preimage and raw boundaries

The binary grammar is exact.  Define:

~~~text
U16BE(n) = unsigned n encoded as exactly 2 big-endian bytes
U32BE(n) = unsigned n encoded as exactly 4 big-endian bytes
U64BE(n) = unsigned n encoded as exactly 8 big-endian bytes
ITEM(tag,value) = U16BE(tag) || U64BE(byte_length(value)) || value
~~~

The complete digest preimage is exactly:

~~~text
ASCII("P15R-PRIVILEGE-DROP-ATTESTATION-v9") ||
U32BE(7) ||
ITEM(1,binding_ascii) ||
ITEM(2,probe_identity_ascii) ||
ITEM(3,denial_ledger_binary) ||
ITEM(4,probe_reap_ascii) ||
ITEM(5,status_raw) ||
ITEM(6,cgroup_raw) ||
ITEM(7,pass_vector_ascii)
~~~

There is no separator, NUL, LF, padding, native-endian value, omitted item,
duplicate item, reordered item, alternate tag, normalization, or trailing
byte outside the value bytes explicitly described below.

binding_ascii is exactly the release's first six ordered fields, without
the record name and without the digest field:

~~~text
session=DEC g_outer_pid=DEC g_inner_pid=1 g_starttime=DEC guardian_dev=DEC guardian_ino=DEC
~~~

probe_identity_ascii is exactly:

~~~text
probe_outer_pid=DEC probe_starttime=DEC uid_r=65534 uid_e=65534 uid_s=65534 uid_fs=65534 gid_r=65534 gid_e=65534 gid_s=65534 gid_fs=65534 groups=EMPTY cap_inh=0 cap_prm=0 cap_eff=0 cap_bnd=0 cap_amb=0
~~~

The two probe decimals identify the one disposable initial-user-namespace
probe child through P's retained pidfd/proc identity.  Every credential and
capability field is validated before an attempt.  EMPTY is the literal
token, not an empty field.  A different credential, surviving group, or
nonzero capability set prevents construction of the receipt.

denial_ledger_binary serializes the complete inherited v2 step-11 denial
vector and nothing else:

~~~text
U32BE(attempt_count) || attempt[0] || ... || attempt[attempt_count-1]

attempt = U16BE(surface_kind) ||
          U64BE(byte_length(relative_name)) ||
          relative_name ||
          U32BE(observed_errno)
~~~

Its exact rules are:

1. attempt_count is two plus the number of namespace-entry basenames in P's
   one stable pre-attempt snapshot of G's /proc/<g_outer_pid>/ns.
2. Attempt zero has surface_kind=1 and relative_name=ASCII("fd").
   Attempt one has surface_kind=2 and relative_name=ASCII("root").
3. Every remaining attempt has surface_kind=3 and
   relative_name=ASCII("ns/") || exact_namespace_basename_bytes.
   The complete current namespace snapshot is included once, sorted by
   unsigned raw basename byte order, with no ., .., duplicate, missing,
   added, normalized, locale-ordered, or post-snapshot name.
4. Every attempt is performed by the same retained disposable probe identity
   against the same retained G proc identity using the inherited v2 denial
   operation.  observed_errno is exactly unsigned Linux EPERM=1 or
   EACCES=13.  ENOENT, ESRCH, a transient lookup failure, success, a
   different errno, a changed namespace snapshot, or G identity drift is
   not denial evidence and prevents release.
5. P revalidates the probe and G identities around the vector.  The ledger
   records observed results; it cannot contain a copied expected-pass token
   in place of the actual attempts.

probe_reap_ascii is exactly:

~~~text
probe_outer_pid=DEC probe_starttime=DEC pidfd_kill_signal=9 pidfd_kill_result=0 waitid_si_pid=DEC waitid_si_code=2 waitid_si_status=9 reaped=1 process_gone=1
~~~

Both first decimals repeat probe_identity_ascii; waitid_si_pid equals
probe_outer_pid; Linux SIGKILL=9 and CLD_KILLED=2 are literal decimal
values.  P constructs this item only after its retained pidfd kill succeeds,
one exact waitid reap returns that identity and status, duplicate wait yields
the inherited no-child result, and the probe is independently absent.  A
live probe, wrong PID/starttime, wrong signal/status, ambiguous wait, second
child, or missing process-gone proof prevents release.

status_raw is the exact byte string from one fresh P open and complete
read-to-EOF of G's retained /proc/<g_outer_pid>/status after the probe is
reaped.  The item begins at the first byte returned and ends immediately at
that file description's EOF.  Natural bytes, including a final LF if the
kernel returned one, are retained; no path bytes, length text, NUL,
terminator, trimming, newline conversion, field reordering, decoding,
re-encoding, or synthesized byte is included.  P parses this same exact byte
string under the inherited v2 G-status predicates.  A short, partial,
changed, malformed, or predicate-failing read prevents release.

cgroup_raw is analogously the exact byte string from the immediately
following one fresh P open and complete read-to-EOF of G's retained
/proc/<g_outer_pid>/cgroup.  Its boundaries and no-normalization rule are
identical to status_raw.  P parses these same bytes and requires the exact
single unified-cgroup membership to resolve to the retained guardian
device/inode receipt.  A path-text match without the retained identity join,
extra line, short or changed read, or predicate failure prevents release.

pass_vector_ascii is exactly:

~~~text
denial_vector_pass=1 probe_kill_reap_pass=1 g_status_pass=1 g_cgroup_pass=1
~~~

P constructs that literal only after all four complete predicates are true
on the exact items above.  It then computes SHA-256 over the complete
preimage and lowercase-hex encodes the 32 digest bytes to obtain
attestation_sha256.  A hash of rendered Markdown, field values alone,
normalized proc text, expected values, a previous attempt, or a prior
session is not this receipt.

### 3.4 P construction and complete-send rule

P sends no release before every inherited step-11 obligation is complete:

1. the one disposable probe has the exact identity and irreversible
   credentials in Section 3.3;
2. every inherited fd/root/namespace denial attempt passes and its actual
   result is in the exact ledger;
3. the probe is pidfd-killed, reaped once, proven gone, and cannot act;
4. the fresh complete G status bytes pass every inherited privilege-drop
   predicate;
5. the fresh complete G cgroup bytes join the exact retained guardian
   identity; and
6. P recomputes the complete preimage and digest, constructs the exact
   release payload, re-parses it canonically, and verifies every serialized
   binding against its retained bootstrap values.

Only that join enters PRIVILEGE_DROP_ATTESTED.  P then performs exactly one
send attempt.  Only a return equal to the exact complete framed-record
length enters PRIVILEGE_DROP_RELEASE_SENT.  Zero, short, partial,
interrupted, errored, ambiguous, or unobservable send is terminal; P neither
retries nor sends a replacement digest or alternate form.

### 3.5 G receive, full validation, direction, and cardinality

The exact successful bootstrap traffic at this boundary is:

~~~text
P -> G: LAUNCHER_REAPED outer_pid=DEC                       exactly once
P -> G: PRIVILEGE_DROP_RELEASE session=DEC ...             exactly once
G -> P: GUARDIAN_READY outer_pid=DEC inner_pid=1            exactly once
~~~

The ellipsis above is presentational only and means all exact Section-3.1
fields in their printed order.  It is never a wildcard payload.

The release is P-to-G only.  It occurs zero times on every failure path and
exactly once on a successful bootstrap.  It is accepted only after G has
completely received and validated LAUNCHER_REAPED and completed its entire
inherited local step-11 drop.  It is accepted only before any
GUARDIAN_READY attempt.  No other state or direction is legal.

G performs one full record receive and validates, before any READY send:

1. inherited frame length, exact payload length, canonical ASCII, exact
   record name, exact field count/order, no extra byte, no ancillary item,
   exact authenticated peer, and expected control endpoint;
2. session against the retained bootstrap/global-control session;
3. g_outer_pid, literal inner PID 1, and g_starttime against its retained
   accepted G identity and the already accepted launcher/PID1 records;
4. guardian_dev and guardian_ino against the exact pair G retained before
   hiding cgroup2 and closing setup-only descriptors;
5. attestation_sha256 against canonical LOWERHEX64 grammar and the rule that
   no digest or release has previously been accepted in this bootstrap; and
6. its current local state is exactly G_LOCAL_DROP_COMPLETE, with every
   inherited bounding, securebits, capability, no_new_privs, dumpable,
   source-boundary, cgroup-hide, and descriptor-close predicate still true.

G cannot recompute P-only probe observations.  Within the frozen trusted-P
boundary, the exact authenticated release and its P-computed digest are the
causal evidence of those observations.  This limitation is explicit: the
digest does not provide Byzantine-P resistance and no G self-check is
relabelled as P evidence.  Complete field and state validation enters
PRIVILEGE_DROP_RELEASE_VALIDATED; only then may G attempt the one exact
GUARDIAN_READY send.

### 3.6 Exact owner-state and causal join

The affected v2 suffix is replaced exactly by:

~~~text
P:
  LAUNCHER_REAPED_SENT
    -> PRIVILEGE_DROP_ATTESTED
    -> PRIVILEGE_DROP_RELEASE_SENT
    -> GUARDIAN_READY_RECEIVED

G:
  LAUNCHER_REAPED_RECEIVED
    -> G_LOCAL_DROP_COMPLETE
    -> PRIVILEGE_DROP_RELEASE_VALIDATED
    -> GUARDIAN_READY_SENT

any first release-boundary failure on either side:
  -> PRIVILEGE_DROP_RELEASE_FAILED_TOMBSTONE
  -> BOOTSTRAP_FAILED
~~~

The exact causal order is:

1. P completely sends and G completely validates LAUNCHER_REAPED.
2. G completes and locally revalidates every inherited privilege-drop action
   before entering G_LOCAL_DROP_COMPLETE.
3. P independently completes the denial vector, probe reap, fresh status,
   fresh cgroup, and exact digest construction before entering
   PRIVILEGE_DROP_ATTESTED.
4. P completely sends the one release and enters
   PRIVILEGE_DROP_RELEASE_SENT.
5. G completely receives, parses, and validates that record while still in
   G_LOCAL_DROP_COMPLETE, then enters
   PRIVILEGE_DROP_RELEASE_VALIDATED.
6. G completely sends the one inherited GUARDIAN_READY and enters
   GUARDIAN_READY_SENT; P enters GUARDIAN_READY_RECEIVED only after full
   receipt and validation of its exact bound outer/inner identity.
7. Only the completed release validation permits G's READY send.  Only the
   completed READY edge may enter the inherited lock state.

P's attestation and G's local-drop branch are independent prerequisites
joined by the release.  Scheduler order, elapsed time, absence of failure,
poll readiness, EOF, or one side's copied state cannot discharge the other
branch.

### 3.7 Exact fail-before-write fence

From complete CGROUP_PREFLIGHTED through
PRIVILEGE_DROP_RELEASE_VALIDATED, the only permitted actions are the
already required launcher reap, G local drop and read-only revalidation,
P's one disposable probe and read-only observations, the exact control
records above, and retained bootstrap failure containment.

Before PRIVILEGE_DROP_RELEASE_VALIDATED, G and every possible child are
forbidden to:

- create a lock candidate or .owner member;
- enter ACQUIRING, call the package-lock bind, or claim lock possession;
- create a generation root, method root, subject root, package copy, result,
  generated member, manifest member, or publication staging object;
- admit, start, or expose any subject, top-level suite, copied wrapper,
  generator, verifier, test, or mutation worker;
- accept or execute SESSION_CREATE, LOCK_ACQUIRE, ROOT_CREATE, SPAWN,
  AUDITED_SPAWN, object-member authorization, cleanup, exchange,
  foreign-audit, or another transaction operation; or
- perform any subject, package, result, lock, object, generation, manifest,
  or repository write.

The cgroup hierarchy and private setup mounts which the inherited bootstrap
already creates are not reclassified as subject/transaction writes.  They
remain usable only for setup and total failure containment.  No failure
branch may exploit that exception to create a lock, object, package, result,
or subject artifact.

### 3.8 Exact 17-cause failure enum, no retry, no fallback, and no reuse

The release-boundary first-cause enum is exact and nonserialized:

~~~text
MISSING
MALFORMED
DUPLICATE
REPLAY
WRONG_SESSION
WRONG_G_IDENTITY
WRONG_CGROUP
WRONG_ATTESTATION
WRONG_DIRECTION
WRONG_STATE
REORDERED
PARTIAL
EOF
TIMEOUT
P_CRASH
G_CRASH
TRANSPORT_ERROR
~~~

Any one of those causes enters
PRIVILEGE_DROP_RELEASE_FAILED_TOMBSTONE before a prohibited write and then
the inherited BOOTSTRAP_FAILED containment.  WRONG_ATTESTATION includes a
P-side recomputation mismatch, wrong item count/tag/order/value boundary,
wrong raw-byte binding, noncanonical digest, or any later inconsistency
between retained release bytes and the frozen digest.  An unknown cause is
MALFORMED or TRANSPORT_ERROR, never a new success case.

The exact total rules are:

1. P emits no release in a failed attestation world.
2. A missing release or live silent peer produces nonprogress or an explicit
   failure/timeout, never READY and never success inferred from silence.
3. The first malformed, duplicate, replayed, reordered, wrong-direction,
   wrong-state, wrong-session, wrong-identity, wrong-cgroup, or
   invalid-digest record is consumed as the terminal offending record.  G
   performs no compatibility parse and does not wait for a corrected second
   record.
4. A partial/error send or receive is terminal.  Neither side retries,
   reconnects, reuses a record, changes the digest, or falls back to
   LAUNCHER_REAPED, EOF, time, G-local checks, or a requester channel.
5. A release from an earlier bootstrap cannot validate in a later one:
   session, G PID/starttime, guardian device/inode, exact endpoint, and
   one-use state must all match.  A byte-identical replay in the same bootstrap
   is a duplicate and fails.
6. P or G crash and any pre-release EOF use the inherited cgroup/pidfd
   kill/reap/populated-zero bootstrap containment before any lock/object or
   project write.  Physical cleanup does not convert the failed tombstone to
   READY, ABSENT, or PASS.
7. GUARDIAN_READY received or sent before complete release validation is a
   reordered/wrong-state failure.  A later valid-looking release cannot
   repair it.

### 3.9 Retention and tombstone auditability

P retains in memory, through either successful global finalization or
complete bootstrap-failure containment:

~~~text
bootstrap/global session
G outer PID, inner PID, starttime, peer and pidfd identity
guardian device/inode receipt
probe PID/starttime/credential receipt
complete denial_ledger_binary
complete probe_reap_ascii
exact status_raw and cgroup_raw bytes
complete attestation preimage and attestation_sha256
exact release payload/framed bytes and send result
READY receive result or first failure cause/state
~~~

G retains through the same terminal boundary:

~~~text
bootstrap/global session and exact authenticated peer
its retained outer PID, inner PID, starttime and guardian device/inode
exact received release payload/framed bytes and digest
complete field/state validation result
READY send result or first failure cause/state
~~~

The success records are never recycled into another bootstrap.  A failure
tombstone retains the first cause, exact state, endpoint identity, complete
or partial bytes observed, and every already completed predecessor fact.
Later EOF, cleanup, process death, or namespace destruction cannot erase or
upgrade it.  These receipts are operational, in-memory, and nonserialized;
they add no CSV column, generated member, manifest key, authority binding,
DAG node/edge, result byte, log path, or repository artifact.

## 4. Fixed-observation closure and mandatory hostile pairs

### 4.1 PASS and FAIL worlds

This design explicitly separates the two worlds confirmed by the reopen
review:

- In PASS, P completes every attestation item and sends the exact release.
  G, already in G_LOCAL_DROP_COMPLETE, validates it and may send READY.
- In FAIL, one P-only denial, reap, status, or cgroup predicate differs.  P
  sends no release.  G's earlier local facts may be identical, but it cannot
  enter PRIVILEGE_DROP_RELEASE_VALIDATED, send READY, or mutate a governed
  object.

### 4.2 Mandatory hostile-pair obligations

The fresh independent reviewer must attack at least:

1. exact release versus no release with identical G-local drop state;
2. complete record versus partial send followed by EOF;
3. exact current record versus byte-identical duplicate;
4. exact current record versus replay under a different session;
5. correct session with wrong G PID/starttime;
6. correct G identity with wrong guardian device/inode;
7. exact binding fields with malformed or incorrectly recomputed digest;
8. valid record received before local drop completion;
9. valid record received after an early READY attempt; and
10. failed P attestation followed by absence of a failure message.

Every pair yields a different state before a prohibited write.  No pair is
distinguished only by an expected flag, copied digest, source assertion,
timeout-derived success, or post-write cleanup.

## 5. Exact preservation of D-M1, D-M2, v8, and all prior closures

### 5.1 Closed enum counts and scoped plus-one

The new form is an inherited global bootstrap P--G record.  It is not a
requester--P FD-5 form, not a v6/v7 D-M1 P--G session form, not a D-M2
quiescence form, and not a v8 post-finalization form:

~~~text
GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=1
SECOND_NEW_BOOTSTRAP_FORM_AUTHORIZED=false
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
PRIVILEGE_DROP_RELEASE_IS_D_M1_FORM=false
PRIVILEGE_DROP_RELEASE_IS_D_M2_FORM=false
PRIVILEGE_DROP_RELEASE_IS_REQUESTER_FORM=false
~~~

The unavoidable scoped delta is exactly plus one member in the v2-derived
global P--G closed enum and exactly one later effective amendment.  It
changes no exact twelve/twelve/four enum or other existing count.

### 5.2 Prior closure preservation

Without weakening, v9 retains:

1. v1's primitive-only causal controls and exact evidence ceiling;
2. v2's two-level namespace/cgroup possession, atomic placement, private
   tmpfs, source capabilities, retained-capability lock/object cleanup,
   foreign preservation, signal, crash, and global-final semantics outside
   the exact bootstrap suffix in Section 2;
3. v3's six pre-suite rows, owner/admission/FDSET barriers, source/start
   joins, child/object registration and acknowledgments, member-ledger
   closure, and unexpected-object nondeletion;
4. v4's requester-direct FD 5, actual FD-4 join, audited admission, exact
   reciprocal Unix-diag ABI, and P-only peer-oracle preflight;
5. blocked v5's no-op provenance;
6. v6's P-issued capabilities, exact D-M1 and D-M2 evidence contracts,
   native pidfd acquisition, proc identities, quiescence, two snapshots,
   reciprocal diagnostics, reverse unwind, EBADF, holder restoration, and
   ABA exclusions;
7. v7's commitment-only create, immutable first receive, wrong-first
   terminalization, active-cap first-use/evidence ceiling, direct terminal
   observation, exact twelve FD-5 and twelve P--G D-M1 forms, and every
   partial-send/replay/tombstone rule; and
8. v8's post-FINALIZED_ACK requester receipt, FD-4/FD-5 clean closure,
   exact requester reap, inherited CHILD_REAPED/ACK, auth-reap
   reconciliation, same live control through global FINAL, validated EXIT,
   G reap, populated-zero, and ordered cgroup removal.

No prior closure is traded for P15R-REOPEN-M1.  A repair requiring another
message, descriptor, channel, syscall, helper, target, method, detector,
outcome, path, generated byte, schema field, binding, node, edge, Route, or
broader trust claim is outside this amendment and stops as a new design
finding.

## 6. Frozen scientific, package, path, count, and DAG vector

The exact invariant vector remains:

~~~text
DESIGN_SCHEMA=paper15r-wieferich-ulm-controls/1
MANIFEST_SCHEMA=paper15r-wieferich-ulm-controls-manifest/1
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
CONCURRENT_PROOF_HASH_CYCLE=false
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false
~~~

The six implementation paths, eight CSVs, nine generated paths, literal
headers, 120 rows, 35 negatives, 35 semantic methods, 28 package methods,
173 tests, fourteen authority bindings, two generations, three identical
copies, and eight-node/twelve-edge DAG remain byte- and count-invariant.
The graph remains nodes A,D,R,G,I,C,M,V, the seven chain edges, and the five
additional A,D,R,G,I -> M edges.  The sole governance count change after a
valid externally frozen amendment is:

~~~text
EFFECTIVE_AMENDMENT_COUNT=9
~~~

V9 adds no implementation path, generated member, manifest key, authority
binding, graph node, edge, self-hash, future-result edge, or proof cycle.

## 7. Append-only count-nine successor and independent-review boundary

The complete current 223,999-byte / 4,236-line review at SHA-256
e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
remains unchanged.  Its nested 209,656-byte historical prefix at SHA-256
3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b
also remains exact.

Only after this amendment has a stable external path/line/byte/hash receipt
may one fresh independent reviewer preserve those complete bytes as an
exact prefix and append one sole active successor block, with no blank or
commentary line inside:

~~~text
[P15R-EFFECTIVE-DESIGN-AMENDMENTS v8]
count=9
1.path=notes/phase2_control_design_amendment_v1.md
1.sha256=cd0b4ab2eb4afc594b3e48a0cc971e69e3e03e237f47405af947dda1ffa8c4fe
2.path=notes/phase2_control_design_amendment_v2.md
2.sha256=c1d104d23fd1a0f42232a04468b8c8b0bb2addf115630ae8e3778e48fc0f44ea
3.path=notes/phase2_control_design_amendment_v3.md
3.sha256=f6a0af9c4e13b451241b6dac701ac434f3b133b367691a61804b0f2bc43caa5b
4.path=notes/phase2_control_design_amendment_v4.md
4.sha256=f55479260adcc588b1bc915fda12d7039ef1a6df8eca3aba9ae1e3dfe936d592
5.path=notes/phase2_control_design_amendment_v5.md
5.sha256=2204471c8a4fe11c1090c9810e54300ec0f2831ac7b894a9791e219a947a6bc8
6.path=notes/phase2_control_design_amendment_v6.md
6.sha256=0e8a90cf4e91d7364b1b7349a1b88dac15c45323f0986024c94ebd2a14f88363
7.path=notes/phase2_control_design_amendment_v7.md
7.sha256=bbdd30c398a20cd06b026ef4ac0ffece08f682083fed1242141891c99addccb7
8.path=notes/phase2_control_design_amendment_v8.md
8.sha256=e3d66503e997232e03623d8ab5da881abe1224ad02961e37a057e84fb2a1e147
9.path=notes/phase2_control_design_amendment_v9.md
9.sha256=<exact externally computed final v9 SHA-256>
[/P15R-EFFECTIVE-DESIGN-AMENDMENTS]
~~~

The reviewer independently reads and hashes all nine amendment files in
that exact order before treating the block as authenticated.  The block
adds no manifest key, authority binding, implementation path, generated
member, DAG node, or edge.

Only a fresh evidence-backed PASS_C0_M0_m0 may close P15R-REOPEN-M1.  Any
critical, major, or minor defect returns REVISE with the exact new vector.
This amendment predicts neither outcome and is not its own independent
review.

## 8. Author-side contract audit and authorization stop

The author-side audit is limited to exact contract presence:

| Gate obligation | Frozen v9 surface | Independent status |
|---|---|---|
| sole exact authenticated release and field/cardinality contract | Sections 2--3 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |
| seven-item domain-separated length-delimited preimage and raw boundaries | Section 3.3 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |
| P/G complete-send/receive validation and causal state join | Sections 3.4--3.6 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |
| pre-write fence, 17 causes, total tombstone, no retry/fallback/reuse | Sections 3.7--3.9 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |
| fixed-observation and ten hostile-pair separation | Section 4 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |
| D-M1/D-M2/v8, prior closures, vector, and count-nine successor | Sections 5--7 | OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW |

~~~text
P15R_CONTROL_DESIGN_AMENDMENT_V9=FROZEN_DESIGN_ONLY_PENDING_FRESH_INDEPENDENT_REREVIEW
V9_REMEDIATION_GATE_SHA256=c4da0d0684ec64d21ef046abe9686147545e7a1035f7c6f3c8d712972b69dc90
V9_REMEDIATION_GATE_LINES=1060
V9_REMEDIATION_GATE_BYTES=48563
DESIGN_REOPEN_GATE_SHA256=8af1bbdca261cc419d090319521a80a80c7c54a8dfb46fa02a257fa18a008973
CURRENT_REVIEW_SHA256=e68522e6fb826cf110149de98737e6ec181689c2e042dc71277dd5cdc8ec3df1
CURRENT_REVIEW_LINES=4236
CURRENT_REVIEW_BYTES=223999
HISTORICAL_PASS_PREFIX_SHA256=3c7b8447cceb23a377e36705fe98b0b6883568641839d45cbca283a399c72a4b

CURRENT_INDEPENDENT_VERDICT=REVISE_C0_M1_m0
P15R_REOPEN_M1_STATUS=OPEN_PENDING_FRESH_INDEPENDENT_REREVIEW
INDEPENDENT_FINDINGS_CLOSED_BY_AUTHOR=false
INDEPENDENT_PASS_CLAIMED=false
FRESH_APPEND_ONLY_REREVIEW_REQUIRED=true

GLOBAL_BOOTSTRAP_NEW_FORM_COUNT=1
SECOND_NEW_BOOTSTRAP_FORM_AUTHORIZED=false
D_M1_FD5_FORM_COUNT=12
D_M1_P_G_SESSION_FORM_COUNT=12
D_M2_QUIESCENCE_FORM_COUNT=4
EFFECTIVE_AMENDMENT_COUNT_AFTER_EXTERNAL_FREEZE=9

CONTROL_SOURCE_IMPLEMENTATION_AUTHORIZED=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
SOURCE_REVIEW_AUTHORIZED=false
PROJECT_CODE_IMPORT_AUTHORIZED=false
PROJECT_CODE_EXECUTION_AUTHORIZED=false
PLATFORM_PREFLIGHT_AUTHORIZED=false
GENERATED_ARTIFACT_MATERIALIZATION_AUTHORIZED=false
GENERATOR_EXECUTION_AUTHORIZED=false
VERIFY_ONLY_EXECUTION_AUTHORIZED=false
UNITTEST_EXECUTION_AUTHORIZED=false
TOP_LEVEL_WRAPPER_EXECUTION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
REPRODUCTION_RUN_AUTHORIZED=false
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
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
~~~

No source, implementation review, generated artifact, platform probe,
control execution, reproduction run, proof, Route, composition, manuscript,
figure, release, archive, Git operation, or public synchronization is
authorized or performed by this amendment.  Work stops at
REVISE_C0_M1_m0 until a separate fresh independent append-only reviewer
reads and attacks the final exact v9 bytes and reaches its own verdict.
