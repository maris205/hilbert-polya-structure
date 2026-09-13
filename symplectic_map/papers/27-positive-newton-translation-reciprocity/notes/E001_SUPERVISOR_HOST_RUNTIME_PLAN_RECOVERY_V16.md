# Paper 27 E001 supervisor host runtime plan recovery V16

Status: AUTHOR-ONLY STATIC CONTROL SUCCESSOR. No execution, manifest, review,
test, validator-process, build, evidence, reservation, or release authority is
created by this document.

## 1. Authority and append-only succession

This file is the sole fresh successor authorized by B07-E0381. The immutable
predecessor is E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V15.md at 519774
bytes, 5569 LF, and SHA256
007a16325c8b90f573f62036bc52279068d76fdde5dea7d3bb5b4079c9112fe4.
V15 is not edited, reinterpreted, or retroactively passed. "Append-only
successor" means a new regular V16 control file whose closed protocol surface
is inherited from that exact predecessor and whose affected transition
definitions are replaced below.

The embedded spans are inert printable-ASCII transition text. They are not
imported, tokenized, parsed as a programming language, compiled, evaluated, or
executed. Names resembling a programming language are merely a compact static
notation. A static reviewer must read the transitions themselves; a claimed
census, assertion, or validator row cannot replace them.

The following predecessor obligations remain normative without relaxation:

- OPEN-only refusal finality, positive polling, actor mark order, the
  RefusalFinalityPending route, recovery resampling, the 80 ms finality cap,
  and the distinct nonborrowable 130 ms closure tail.
- ACK construction and immutable cache before close, ACK activation only
  after CLOSED_NO_CONSUME, no-consume uncertainty, nonpoison candidate receipt,
  actor-loss plus fully drained control EOF, and no fabricated receipt state.
- One immutable transfer or refusal offer, one possible send, no resend,
  retained acceptance uncertainty, carrier construction before O_EXCL
  reservation, and no sequence consumption by an unactivated candidate.
- Seventeen typed semantic deltas, candidate/final report-union validation,
  durability reconciliation, verified publication, exactly one kill ticket
  and kill call, sticky PASS, and terminal durable ordering.
- The 13 positive terminal ceilings totaling 2510 ms, the 210 ms refusal
  schedule, the 80 ms finality point, and the seven positive generic-transfer
  phases remain unchanged. Every fallible nonownership check is before closure
  activation. Once closure is active, safety is no longer deadline-bounded.

## 2. Frozen carriers and nonauthority

The frozen Host V15 carrier, Binder V8, actor V3, derivation V6, embedded
validator, certificate, envelope, reservation, issuer, external-owner, and
outer-reconciler identities remain exactly those bound by the predecessor and
ledger. No byte here changes or discharges any such identity. The prospective
138-row manifest frame, including the immutable failed Runner V12 row, is not
modified. Runners V13, V14, and V15 remain nonmanifest failures.

This file grants no filesystem effect beyond its own authoring, and no access
to any prohibited subtree. It creates no auxiliary file and requires no
runtime observation.

## 3. Exact six unresolved external gates

The unresolved non-executable premise set is exactly:

1. CLONE3_CPYTHON
2. DELETED_CGROUP_FD
3. SEALED_SNAPSHOT_CONSTRUCTION
4. EXTERNAL_SURVIVAL
5. OUTER_RECONCILER
6. ISSUER_CRYPTOGRAPHY

The fd range and CPython cached-small-integer statement below is a conjunct
inside CLONE3_CPYTHON. It is not an additional named gate.

## 4. V16 authoritative physical ownership model

Every descriptor is represented by one preallocated physical record with an
immutable record_id and provenance cell. Its only physical states are CLOSED,
ACQUIRING, OWNED, and CLOSE_RETRY. There is no owns bit. A record in ACQUIRING
with raw_fd at least zero is live and is included in every exhaustive census.
CLOSED, and only CLOSED, proves physical release.

Every producing operation also has a preallocated raw fallback cell whose
states are EMPTY, LOCAL_RAW, SHADOW_OF_RECORD, and DISARMED. The protected
region begins before the producing call. Each returned scalar is copied first
into its raw cell and then shadowed into its already-ACQUIRING record. Finally
cleanup resolves LOCAL_RAW regardless of the record state. Pair outputs are
independent. The clone3 pidfd record is ACQUIRING before the syscall and its
preallocated C output cell is captured before any branch.

All physical records, raw cells, C integer outputs, five receive frames,
control buffers, quarantine records, overflow cells, identity/access cells,
poller cells, endpoint cells, stream buffers, journal cells, close plans,
close cursors, and the acceptance commit object are allocated before the
acquisition epoch. Acquisition, receive capture, quarantine, promotion,
wrapper handoff, poller handoff, and close handoff perform no allocation and
create no dictionary, list, tuple, journal, poller, or wrapper container.

The actor producer census is exact: actor_acquire_open, actor_acquire_dup,
actor_acquire_f_dupfd_cloexec, actor_acquire_dup2, actor_acquire_memfd,
actor_acquire_pipe2, actor_acquire_socketpair, actor_acquire_pidfd, and the
clone3 pidfd output. The watchdog producer census is exact:
watchdog_acquire_open, watchdog_acquire_memfd, and watchdog_acquire_dup.
Inherited and received rights use the same prearmed adoption primitive.

## 5. Bounded fd scalar premise inside CLONE3_CPYTHON

Before descriptor-producing work, the soft RLIMIT_NOFILE is exactly 256 and
the hard limit is at least 256. Every explicit dup target is in 0 through 255.
The capacity proof tables in both spans bound the actor simultaneous live
count at 219 and the watchdog simultaneous live count at 112. A successful returned
descriptor is therefore in 0 through 255. The frozen CPython image premise
must separately establish that each scalar in that range is a preexisting
cached small integer and that the selected libc/ctypes call boundary writes
only into preallocated cells. This complete conjunct is subordinate to
CLONE3_CPYTHON and does not alter the six-gate set.

## 6. Five receive boundaries and deferred semantics

The five sites and fixed capacities are:

| site | semantic rights | overflow capture | installed capacity |
| --- | ---: | ---: | ---: |
| actor_control | 4 | 1 | 5 |
| monitored | 4 | 1 | 5 |
| external_control | 13 | 1 | 14 |
| external_receipt | 13 | 1 | 14 |
| refusal | 4 | 1 | 5 |

Each ancillary buffer is at least installed_capacity times
CMSG_SPACE(sizeof(int)). Every call uses MSG_CMSG_CLOEXEC. The first
post-recvmsg transition is a bounded in-place CMSG walk that copies every
visible installed right into a nonsemantic physical quarantine record or its
preallocated overflow raw cell. No checkpoint, packet framing, address test,
deadline test, allocation, ancillary conversion, semantic assertion, or
caller dispatch precedes this capture. MSG_TRUNC, MSG_CTRUNC, overflow, bad
headers, rejection, and exceptions are handled only after all captured rights
are reconciled.

Rights remain QUARANTINE with unknown semantic_role throughout complete
framing, deadline, count, order, identity, type, access, inode, cgroup, and
stream validation. Only the fully validated caller promotes in place:

- stream_arm promotes three records to OUT_FD, ERR_FD, and EVENTS_FD.
- pidfd_arm promotes one record to OUTER_PIDFD.
- stage_bind promotes one record to STAGE_DIRFD.
- containment_bind promotes one record to CGROUP_DIRFD.

The external receipt site captures before its first checkpoint. Receipt
carrier temporaries are validated and closed; they are never promoted to a
permanent semantic role.

## 7. Promotion, wrappers, pollers, and physical close

Promotion revalidates the same number, complete identity, actual access, and
global physical uniqueness immediately before changing semantic_role in the
same record. No destination record becomes live. Poller cells refer only to
record_id. A close transition sets CLOSE_RETRY before identity revalidation,
poller reconciliation, endpoint detachment, or the close syscall.

Endpoint state is one of NO_WRAPPER, ATTACHED, DETACH_REQUESTED, DETACHED, and
PROVED_CLOSED. Wrapper construction and binding are inside one protected
primitive. A local wrapper fallback is either stored as the record's strong
reference or detached and reconciled. Destructor behavior is never ownership
or close proof. If detach succeeds before later bookkeeping faults, a retry
observes fileno equal to -1, repairs the state to DETACHED using the recorded
raw number, and never detaches twice.

All pidfd event masks pass through pidfd_ready_event. POLLNVAL is a fault.
Closing a record reconciles every poller cell that names its record_id.

## 8. Exact watchdog 97-record partition

The generic partition is unchanged and exhaustive:

- Exactly 13 offered permanent slots: attempt, attempt_base_fd, stage_fd,
  cgfd, root_events_fd, root_kill_fd, out_fd, err_fd, events_fd, outer_pidfd,
  cgroup_base_fd, actor_control_fd, pending_expected_raw_fd.
- Exactly 12 unconditional safe-local-only slots: transfer_control_fd,
  actor_pidfd_fd, external_owner_pidfd_fd, certificate_carrier_fd,
  envelope_carrier_fd, snapshot_carrier_fd, plan_carrier_fd,
  actor_source_carrier_fd, host_source_carrier_fd, reservation_carrier_fd,
  external_manifest_carrier_fd, watchdog_source_carrier_fd.
- The remaining exact 72 records are blocking transient or quarantine slots.

Every live record at freeze, immediately before the one possible send, and
acceptance is classified. A live blocking record, ACQUIRING record, raw
LOCAL_RAW cell, quarantine, CLOSE_RETRY, or unknown identity/access blocks.
The full-live, offered, and safe-local sets must match their frozen snapshots.

Refusal has one separately guarded actor-control special case. Its offered
rights set is exactly empty. It neither reclassifies actor_control_fd as
safe-local nor changes the generic 13/12/72 partition.

Unique kill scans every live physical record by bound leaf identity and actual
writable access. Semantic labels are irrelevant. Unknown leaf identity or
access blocks. The sender and receiver bind the exhaustive installed history,
full-live census, and kill census at ARM, kill, freeze, pre-send, and commit.
Receiver history includes a received-then-closed outer pidfd. After release,
the local writable-kill cardinality is exactly zero.

## 9. Frozen capability identity and mutable readiness

Outer capability byte identity is separate from readiness. Before freeze,
readiness observed from PRE_READY omits and rebuilds the candidate. At freeze,
PRE_READY becomes PRE_READY_OFFER_FROZEN. Later readiness changes only the
mutable state to POST_OFFER_READY_RETAINED; offer bytes, registry identity,
sequence, predecessor, and possible-send state remain unchanged. Registry
assertions accept the frozen identity in both allowed readiness states.
Authenticated acceptance then performs the recorded close/omit transition.

One preallocated acceptance commit object binds the offer identity, frozen
outer capability identity, current late-readiness state, exhaustive receiver
installed history, full-live census, kill census, no-replay fact, durable
receipt, and issuer result. COMMITTED has no downgrade.

## 10. One no-return closure

There is one preallocated ClosureCell. Its phase is NOT_STARTED, ACTIVE,
CLOSED, or RELEASED. Its mode is GENERIC_ACCEPTED, REFUSAL_ACCEPTED, or
DIRECT. It owns the immutable plan, cursor, current record_id, retry delay,
and timing-overrun observation. No split ownership, completion, or release
flags exist.

All nonownership checks, deadlines, offer and acceptance checks, actor closure
packet decisions, and immutable plan installation finish before ACTIVE. Once
ACTIVE, no checkpoint, deadline, offer construction, send, resend, receive,
state downgrade, caller return, main return, or process exit is reachable.
The same no-return driver resumes the same cursor until RELEASED. Persistent
errors use a positive bounded wait in 10 through 50 ms. Under the existing
EXTERNAL_SURVIVAL premise, safety continues even when the earlier timely tail
can no longer be certified.

close_probe is idempotent after RELEASED. It verifies all physical records
CLOSED, every raw fallback EMPTY or DISARMED, all poller cells inactive, all
endpoint cells PROVED_CLOSED or NO_WRAPPER, and zero local writable-kill
capabilities.

## 11. Sticky stream drain correction

Each stream has a preallocated byte buffer plus used, overflow, and eof cells.
room is computed only after a successful nonempty read. overflow is monotone
OR and eof is monotone. EAGAIN and EOF return directly without referring to a
chunk or room from another iteration. EOF cannot clear an earlier overflow.

## 12. Embedded transition source boundaries

All content between delimiters is inert raw text. Delimiters are not source.
The embedded validator is nested within the actor span and is itself inert.

P27 RUNNER V16 ACTOR SOURCE BEGIN 6C8A16F1
# STATIC-TRANSITION-TEXT; DO NOT IMPORT OR EXECUTE
TAG = b"P27E001V16"
PREDECESSOR_SHA256 = b"007a16325c8b90f573f62036bc52279068d76fdde5dea7d3bb5b4079c9112fe4"
PHYSICAL_STATES = (b"CLOSED", b"ACQUIRING", b"OWNED", b"CLOSE_RETRY")
RAW_STATES = (b"EMPTY", b"LOCAL_RAW", b"SHADOW_OF_RECORD", b"DISARMED")
ENDPOINT_STATES = (b"NO_WRAPPER", b"ATTACHED", b"DETACH_REQUESTED", b"DETACHED", b"PROVED_CLOSED")
EXTERNAL_GATES = (b"CLONE3_CPYTHON", b"DELETED_CGROUP_FD", b"SEALED_SNAPSHOT_CONSTRUCTION", b"EXTERNAL_SURVIVAL", b"OUTER_RECONCILER", b"ISSUER_CRYPTOGRAPHY")
CONTEXT_DOMAIN = b"P27E001_V16_DETACHED_ENVELOPE_CONTEXT\x00"
CERTIFICATE_DOMAIN = b"P27E001_V16_CERTIFICATE_DIGEST\x00"
ENVELOPE_TBS_DOMAIN = b"P27E001_V16_ENVELOPE_TBS\x00"
SIGNATURE_DOMAIN = b"P27E001_V16_ISSUER_SIGNATURE_PREIMAGE\x00"
RECEIPT_DOMAIN = b"P27E001_V16_ISSUER_RECEIPT\x00"
RESERVATION_TBS_DOMAIN = b"P27E001_V16_RESERVATION_TBS\x00"
RESERVATION_SIGNATURE_DOMAIN = b"P27E001_V16_RESERVATION_SIGNATURE\x00"
RESERVATION_RECEIPT_DOMAIN = b"P27E001_V16_RESERVATION_RECEIPT\x00"
FINAL_ENVELOPE_DOMAIN = b"P27E001_V16_FINAL_ENVELOPE\x00"
AUTH_DOMAIN = b"P27E001_V16_SESSION_AUTH\x00"
EXTERNAL_ACCEPTANCE_DOMAIN = b"P27E001_V16_EXTERNAL_ACCEPTANCE\x00"
ISSUER_KEY_BIND_DOMAIN = b"P27E001_V16_ISSUER_KEY_BIND\x00"
EMPTY_SHA = b"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
DOMAIN_SPEC = (
 CONTEXT_DOMAIN,CERTIFICATE_DOMAIN,ENVELOPE_TBS_DOMAIN,SIGNATURE_DOMAIN,
 RECEIPT_DOMAIN,RESERVATION_TBS_DOMAIN,RESERVATION_SIGNATURE_DOMAIN,
 RESERVATION_RECEIPT_DOMAIN,FINAL_ENVELOPE_DOMAIN,AUTH_DOMAIN,
 EXTERNAL_ACCEPTANCE_DOMAIN,ISSUER_KEY_BIND_DOMAIN,
)
FD_LIMIT = 256
FD_MIN = 0
FD_MAX = 255
ACTOR_HIGH_WATER_COMPONENTS = (
 (b"PHYSICAL_RECORD_CAPACITY",211),
 (b"MAX_RECEIVE_RAW_CAPTURE",5),
 (b"MAX_PAIR_RAW_CAPTURE",2),
 (b"MAX_SINGLE_OR_CLONE_RAW_CAPTURE",1),
)
ACTOR_LIVE_HIGH_WATER = 219
ACTOR_PHASE_HIGH_WATER = (
 (b"ENTRY", 14, 110),
 (b"STATIC_VERIFY", 92, 201),
 (b"MAPPING", 207, 255),
 (b"PROBE_FORK", 219, 255),
 (b"POST_TRANSFER", 83, 255),
)
CLONE3_CPYTHON_CONJUNCT = (
 b"SOFT_RLIMIT_NOFILE_EQ_256",
 b"HARD_RLIMIT_NOFILE_GE_256",
 b"ALL_TARGETS_0_THROUGH_255",
 b"ALL_SUCCESSFUL_RESULTS_0_THROUGH_255",
 b"CPYTHON_CACHED_SMALL_INT_0_THROUGH_255",
 b"PREALLOCATED_CTYPES_OUTPUT_CELLS",
)

TERMINAL_PHASE_NS = (
 (b"CANDIDATE_RECORD",100000000),
 (b"NOTICE",100000000),
 (b"TERMINAL_SEEN_RECORD",100000000),
 (b"REPORT_RECORD",1000000000),
 (b"PASS_COMMIT",100000000),
 (b"PASS_MARGIN",10000000),
 (b"ACK",500000000),
 (b"ACTOR_ACK_RECEIPT",100000000),
 (b"ACK_RECEIPT_RECORD",100000000),
 (b"RECONCILIATION_RECORD",100000000),
 (b"OWNER_CLOSURE_RECORD",100000000),
 (b"CLOSURE_PACKET",100000000),
 (b"WATCHDOG_EXIT",100000000),
)
REFUSAL_PHASE_NS = (
 (b"REFUSAL_RECORD",20000000),
 (b"REFUSAL_ACK",20000000),
 (b"REFUSAL_RECEIPT_WAIT",30000000),
 (b"REFUSAL_FINALITY_COMMIT",10000000),
 (b"REFUSAL_OFFER_BUILD",10000000),
 (b"REFUSAL_OFFER_SEND",20000000),
 (b"REFUSAL_ACCEPTANCE_RECEIVE",30000000),
 (b"REFUSAL_ACCEPTANCE_VERIFY",20000000),
 (b"REFUSAL_ACCEPTANCE_COMMIT",10000000),
 (b"REFUSAL_ACTOR_CLOSURE",20000000),
 (b"REFUSAL_CAPABILITY_CLOSE",10000000),
 (b"REFUSAL_CLOSURE",10000000),
)
GENERIC_TRANSFER_PHASE_NS = (
 (b"TRANSFER_OFFER_BUILD",20000000),
 (b"TRANSFER_OFFER_SEND",30000000),
 (b"TRANSFER_ACCEPTANCE_RECEIVE",50000000),
 (b"TRANSFER_ACCEPTANCE_VERIFY",50000000),
 (b"TRANSFER_ACCEPTANCE_COMMIT",30000000),
 (b"TRANSFER_CAPABILITY_CLOSE",30000000),
 (b"TRANSFER_CLOSURE",30000000),
)
RECORD_DELTA_KINDS = (
 b"ATTEMPT_INTENT", b"ATTEMPT_COLLISION", b"CONSUMPTION_INTENT",
 b"CONSUMPTION_COMMIT", b"STAGE_BIND", b"CONTAINMENT_BIND",
 b"STREAM_BIND", b"PIDFD_BIND", b"RELEASE_RECORD", b"RESULT_NOTICE",
 b"RESULT_FRAME", b"RESULT_END", b"VALIDATED_RECORD", b"ACK_INTENT",
 b"COMMITTED_RECORD", b"TERMINAL_RECORD", b"OWNER_CLOSURE",
)
CERTIFICATE_SCHEMA = (
 b"INHERIT_EXACT_192_KEYS_FROM_FROZEN_HOST_V15",
 b"INHERITED_TUPLE_BYTES_4840",
 b"INHERITED_TUPLE_LF_1",
 b"INHERITED_TUPLE_SHA256_ede6bffba35fb0331ea92e1c68f4b104dad0ff50822f0520853f28bc9476e196",
 b"V16_DOMAIN_AND_CONTROL_LABEL_BINDING_REQUIRED",
 b"EXACT_SIX_GATE_RECEIPTS_REQUIRED",
)
EXTERNAL_MANIFEST_KEYS = (
 b"VERSION",b"SESSION_AUTH_POLICY",b"OWNER_PID",b"OWNER_STARTTIME",
 b"OWNER_UID",b"OWNER_GID",b"ENDPOINT_TYPE",b"PIDFD_REQUIRED",
 b"MAX_PACKET_BYTES",b"RIGHTS_TYPES",b"REFUSAL_RECEIPT_PROTOCOL",
 b"TRANSFER_PROTOCOL",b"NO_REPLAY",
)
EXTERNAL_MANIFEST_VALUES_V16 = (
 b"16",b"AUTH_V16_LENGTH_FRAMED",b"CERT_OWNER_PID",b"CERT_OWNER_STARTTIME",
 b"CERT_OWNER_UID",b"CERT_OWNER_GID",b"SOCK_SEQPACKET",b"1",b"65536",
 b"ATTEMPT_DIRFD,ATTEMPT_BASE_DIRFD,STAGE_DIRFD,CGROUP_DIRFD,ROOT_EVENTS_FD,ROOT_KILL_FD,OUT_FD,ERR_FD,EVENTS_FD,OUTER_PIDFD,CGROUP_BASE_DIRFD,ACTOR_CONTROL_FD,PENDING_EXPECTED_RAW_FD",
 b"MONOTONE_O_EXCL_ISSUER_V16",b"OFFER_ACCEPTED_DURABLE_V16",b"1",
)
GENERIC_OFFER_V16_FIELDS = (
 b"offer_sha256",b"record_seq",b"predecessor_sha256",b"reason",
 b"rights_count",b"rights_manifest_sha256",b"full_live_census_sha256",
 b"offered_set_sha256",b"safe_local_set_sha256",b"kill_census_sha256",
 b"outer_frozen_identity",b"outer_readiness_state",b"pending_delta_sha256",
 b"terminal_subject_sha256",b"chain_head_sha256",b"no_replay",
)
ACCEPTANCE_V16_FIELDS = (
 b"offer_sha256",b"record_seq",b"predecessor_sha256",
 b"durable_receipt_sha256",b"issuer_signature",b"receiver_pid",
 b"receiver_starttime",b"installed_history_sha256",
 b"full_live_census_sha256",b"kill_census_sha256",
 b"outer_frozen_identity",b"outer_readiness_state",b"no_replay",
)
REFUSAL_OFFER_V16_FIELDS = (
 b"offer_sha256",b"record_seq",b"predecessor_sha256",b"request_sha256",
 b"ack_sha256",b"authoritative_receipt_sha256",b"finality_evidence_sha256",
 b"finality_deadline_ns",b"closure_deadline_ns",b"schedule_sha256",
 b"rights_count_exact_zero",b"no_replay",
)

CONTROL_SPEC = (
 (b"V16_ABORT",b"ABORTING",b"*",b"ABORT_NOTICE",b"control_deadline_ns"),
 (b"V16_READY",b"READY",b"WAIT_READY",b"NO_EFFECT",b"ready_deadline_ns"),
 (b"V16_REFUSE_PREBEGIN",b"REFUSE_PREBEGIN",b"WAIT_BEGIN",b"NO_CONSUME_REFUSAL",b"consume_deadline_ns"),
 (b"V16_REFUSE_POSTARM",b"REFUSE_POSTARM",b"WAIT_COMMIT",b"NO_CONSUME_REFUSAL",b"consume_deadline_ns"),
 (b"V16_REFUSE_ACK",b"REFUSAL_CLOSED_NO_CONSUME",b"WAIT_REFUSAL_ACK",b"REFUSAL_ACK_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 (b"V16_REFUSE_ACK_RECEIPT",b"REFUSAL_ACK_RECEIVED",b"WAIT_REFUSAL_RECEIPT",b"NO_REPLAY_RECEIPT",b"consume_deadline_ns"),
 (b"V16_REFUSAL_CLOSED",b"REFUSAL_DURABLY_CLOSED",b"WAIT_REFUSAL_CLOSED",b"OWNER_CLOSURE",b"consume_deadline_ns"),
 (b"V16_CONSUME_BEGIN",b"CONSUME_BEGIN",b"WAIT_BEGIN",b"BEGIN_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 (b"V16_CONSUME_ARMED",b"CONSUME_ARMED",b"WAIT_ARM",b"ARM_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 (b"V16_CONSUME_COMMIT",b"CONSUME_COMMIT",b"WAIT_COMMIT",b"COMMIT_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 (b"V16_CONSUMED_DURABLE",b"CONSUMED_DURABLE",b"WAIT_CONSUMED",b"INTENT_DURABLE",b"consume_deadline_ns"),
 (b"V16_STAGE_DURABLE",b"STAGE_DURABLE",b"WAIT_STAGE",b"FD_TRANSFER",b"stage_deadline_ns"),
 (b"V16_STAGE_ACK",b"STAGE_BOUND",b"WAIT_STAGE_ACK",b"STAGE_VERIFIED",b"stage_deadline_ns"),
 (b"V16_CONTAINMENT",b"CONTAINMENT_CANDIDATE",b"WAIT_CONTAINMENT",b"FD_TRANSFER",b"contain_deadline_ns"),
 (b"V16_CONTAINMENT_ACK",b"CONTAINMENT_BOUND",b"WAIT_CONTAINMENT_ACK",b"CONTAINMENT_VERIFIED",b"contain_deadline_ns"),
 (b"V16_STREAM_ARM",b"STREAM_ARM",b"WAIT_STREAM_ARM",b"FD_TRANSFER",b"launch_deadline_ns"),
 (b"V16_STREAMS_ARMED",b"STREAMS_ARMED",b"WAIT_STREAMS_ARMED",b"FD_VERIFIED",b"launch_deadline_ns"),
 (b"V16_PIDFD_ARM",b"PIDFD_ARM",b"WAIT_PIDFD_ARM",b"FD_TRANSFER",b"launch_deadline_ns"),
 (b"V16_PIDFD_ARMED",b"PIDFD_ARMED",b"WAIT_PIDFD_ARMED",b"PIDFD_VERIFIED",b"launch_deadline_ns"),
 (b"V16_RELEASE_CANDIDATE",b"RELEASE_CANDIDATE",b"WAIT_RELEASE",b"RELEASE_AUTHORIZATION",b"launch_deadline_ns"),
 (b"V16_RELEASE_DURABLE",b"RELEASE_DURABLE",b"WAIT_RELEASE_DURABLE",b"RELEASE_RECORD_DURABLE",b"launch_deadline_ns"),
 (b"V16_RESULT",b"RESULT",b"WAIT_RESULT",b"RESULT_NOTICE",b"result_deadline_ns"),
 (b"V16_RESULT_FRAME",b"RESULT_FRAME",b"WAIT_RESULT_FRAME",b"RESULT_FRAME",b"result_deadline_ns"),
 (b"V16_RESULT_END",b"RESULT_END",b"WAIT_RESULT_END",b"RESULT_COMPLETE",b"result_deadline_ns"),
 (b"V16_VALIDATED_CANDIDATE",b"VALIDATED_CANDIDATE",b"WAIT_VALIDATED",b"VALIDATION_NOTICE",b"ack_deadline_ns"),
 (b"V16_VALIDATED_DURABLE",b"VALIDATED_DURABLE",b"WAIT_VALIDATED_DURABLE",b"VALIDATED_RECORD_DURABLE",b"ack_deadline_ns"),
 (b"V16_ACK_COMMIT_INTENT",b"ACK_COMMIT_INTENT",b"WAIT_ACK_INTENT",b"ACK_COMMIT",b"ack_deadline_ns"),
 (b"V16_COMMITTED",b"COMMITTED",b"WAIT_COMMITTED",b"COMMIT_RECORD_DURABLE",b"ack_deadline_ns"),
 (b"V16_COMMITTED_SEEN",b"COMMITTED_SEEN",b"WAIT_COMMITTED_SEEN",b"ACK_RECEIPT",b"ack_deadline_ns"),
 (b"V16_EMPTY_FINAL_QUERY",b"EMPTY_FINAL_QUERY",b"WAIT_EMPTY_QUERY",b"REMOVE_QUERY",b"remove_deadline_ns"),
 (b"V16_EMPTY_FINAL_CONFIRMED",b"EMPTY_FINAL_CONFIRMED",b"WAIT_EMPTY_CONFIRMED",b"EMPTY_OBSERVED",b"remove_deadline_ns"),
 (b"V16_CGROUP_REMOVED",b"CGROUP_REMOVED",b"WAIT_REMOVED",b"REMOVE_EFFECT",b"remove_deadline_ns"),
 (b"V16_REMOVE_ACK",b"REMOVE_ACK",b"WAIT_REMOVE_ACK",b"REMOVAL_VERIFIED",b"remove_deadline_ns"),
 (b"V16_FINALIZE_CANDIDATE",b"FINALIZE_CANDIDATE",b"WAIT_FINALIZE",b"FINALIZE_NOTICE",b"candidate_deadline_ns"),
 (b"V16_TERMINAL_CANDIDATE_DURABLE",b"TERMINAL_CANDIDATE_DURABLE",b"WAIT_TERMINAL_CANDIDATE",b"CANDIDATE_DURABLE",b"candidate_deadline_ns"),
 (b"V16_TERMINAL_FAILURE_DURABLE",b"TERMINAL_FAILURE_DURABLE",b"WAIT_TERMINAL_FAILURE",b"FAILURE_REPORT_DURABLE",b"candidate_deadline_ns"),
 (b"V16_TERMINAL_SEEN",b"TERMINAL_SEEN",b"WAIT_TERMINAL_SEEN",b"TERMINAL_SEEN",b"seen_deadline_ns"),
 (b"V16_TERMINAL_ACK",b"TERMINAL_ACK",b"WAIT_TERMINAL_ACK",b"ACK_SEND_EFFECT_UNKNOWN",b"ack_deadline_ns"),
 (b"V16_TERMINAL_ACK_RECEIPT",b"ACK_RECEIVED_NO_REPLAY",b"WAIT_ACK_RECEIPT",b"NO_REPLAY_RECEIPT",b"receipt_deadline_ns"),
 (b"V16_TERMINAL_CLOSED",b"OWNER_CLOSED",b"WAIT_OWNER_CLOSED",b"OWNER_CLOSURE",b"closure_deadline_ns"),
)

class PhysicalRecord:
 __preallocated_fields__ = (
  b"record_id",b"state",b"semantic_role",b"raw_fd",b"identity",
  b"access",b"provenance",b"endpoint_state",b"wrapper_ref",
  b"detached_raw_fd",b"leaf_identity",
 )

class RawCell:
 __preallocated_fields__ = (b"cell_id",b"state",b"raw_fd",b"record_id")

class IdentityCell:
 __preallocated_fields__ = (
  b"dev",b"ino",b"mode",b"nlink",b"uid",b"gid",b"access",b"known",
 )

class ActorReceiveFrame:
 __preallocated_fields__ = (
  b"msghdr",b"iov",b"payload_65536",b"control_5_cmsg_space",
  b"semantic_capacity_4",b"installed_capacity_5",b"quarantine_record_ids",
  b"capture_raw_cells_5",b"overflow_raw_cell",b"installed_count",
  b"payload_count",b"msg_flags",b"capture_complete",b"validation_complete",
  b"capture_fault",
 )

ACTOR_FIXED_RECORD_COUNT = 63
ACTOR_DIR_POOL_COUNT = 32
ACTOR_FILE_POOL_COUNT = 64
ACTOR_QUARANTINE_RECORD_COUNT = 4
ACTOR_MAPPING_PARK_COUNT = 24
ACTOR_MAPPING_TARGET_COUNT = 24
ACTOR_RECORD_COUNT = 211
ACTOR_CONTROL_FRAME = PREALLOC_ACTOR_RECEIVE_FRAME(
 b"actor_control", semantic_capacity=4, installed_capacity=5,
 ancillary_bytes=5*CMSG_SPACE(sizeof_int), msg_cmsg_cloexec=True,
)
ACTOR_RECORDS = PREALLOC_PHYSICAL_RECORDS(ACTOR_RECORD_COUNT)
ACTOR_RAW_CELLS = PREALLOC_RAW_CELLS_FOR_EVERY_PRODUCER_AND_RECORD()
ACTOR_IDENTITIES = PREALLOC_IDENTITY_CELLS(ACTOR_RECORD_COUNT)
ACTOR_PIPE2_OUT = PREALLOC_C_INT_PAIR()
ACTOR_SOCKETPAIR_OUT = PREALLOC_C_INT_PAIR()
ACTOR_CLONE3_OUTCOME = PREALLOC_CLONE3_OUTCOME(parent_pid=-1,pidfd=-1,branch=b"UNSET")
ACTOR_WRAPPER_FALLBACK = PREALLOC_WRAPPER_CELL()
ACTOR_POLLER_CELLS = PREALLOC_POLLER_CELLS()
ACTOR_JOURNAL_CELLS = PREALLOC_BOUNDED_JOURNAL_CELLS()
ACTOR_STREAM_CELLS = PREALLOC_STREAM_CELLS()
ACQUISITION_EPOCH = False

def actor_enter_acquisition_epoch():
 require(not ACQUISITION_EPOCH)
 require(rlimit_hard_nofile() >= 256)
 set_rlimit_soft_nofile(256)
 require(rlimit_soft_nofile() == 256)
 require(max_explicit_fd_target() <= 255)
 require(sum_fixed(ACTOR_HIGH_WATER_COMPONENTS) == 219)
 require(max_phase_live_records(ACTOR_PHASE_HIGH_WATER) == 219)
 ACQUISITION_EPOCH = True

def actor_record_begin(record, semantic_role, provenance):
 require(ACQUISITION_EPOCH)
 require(record.state == b"CLOSED")
 record.state = b"ACQUIRING"
 record.semantic_role = semantic_role
 record.raw_fd = -1
 record.identity.known = False
 record.access = b"UNKNOWN"
 record.provenance = provenance
 record.endpoint_state = b"NO_WRAPPER"
 record.wrapper_ref = NONE
 record.detached_raw_fd = -1

def actor_raw_begin(cell, record):
 require(cell.state in (b"EMPTY",b"DISARMED"))
 require(record.state == b"ACQUIRING" and record.raw_fd == -1)
 cell.state = b"EMPTY"
 cell.raw_fd = -1
 cell.record_id = record.record_id

def actor_capture_scalar_first(cell, record, raw_fd):
 cell.raw_fd = raw_fd
 cell.state = b"LOCAL_RAW"
 require(record.state == b"ACQUIRING" and record.raw_fd == -1)
 require(FD_MIN <= raw_fd <= FD_MAX)
 record.raw_fd = raw_fd
 cell.state = b"SHADOW_OF_RECORD"

def actor_identity_revalidate_into(record):
 require(record.state in (b"ACQUIRING",b"OWNED",b"CLOSE_RETRY"))
 C_FSTAT_INTO_PREALLOCATED(record.raw_fd, record.identity)
 C_FCNTL_ACCESS_INTO_PREALLOCATED(record.raw_fd, record.identity)
 require(record.identity.known)
 record.access = record.identity.access

def actor_finish_adoption(cell, record):
 require(record.state == b"ACQUIRING")
 require(cell.state == b"SHADOW_OF_RECORD")
 require(cell.raw_fd == record.raw_fd and record.raw_fd >= 0)
 actor_identity_revalidate_into(record)
 require(global_record_owner_count(record.raw_fd, record.record_id) == 0)
 record.state = b"OWNED"
 cell.raw_fd = -1
 cell.state = b"DISARMED"
 bounded_journal_write_noalloc(record.record_id,b"OWNED")
 return record.raw_fd

def actor_resolve_raw_finally(cell, record):
 if cell.state == b"LOCAL_RAW":
  STRICT_CLOSE_RAW_RETRY_SAME_NUMBER(cell)
  cell.raw_fd = -1
  cell.state = b"DISARMED"
 if cell.state == b"SHADOW_OF_RECORD":
  require(record.raw_fd == cell.raw_fd)
  if record.state == b"ACQUIRING":
   actor_physical_close(record)
  cell.raw_fd = -1
  cell.state = b"DISARMED"
 require(cell.state in (b"EMPTY",b"DISARMED"))

def actor_adopt_inherited(record, cell, semantic_role, raw_fd, provenance):
 actor_record_begin(record,semantic_role,provenance)
 actor_raw_begin(cell,record)
 try:
  actor_capture_scalar_first(cell,record,raw_fd)
  return actor_finish_adoption(cell,record)
 finally:
  actor_resolve_raw_finally(cell,record)

def actor_acquire_open(record, cell, path, flags, mode, dir_fd, semantic_role, provenance):
 actor_record_begin(record,semantic_role,provenance)
 actor_raw_begin(cell,record)
 try:
  raw_fd = OS_OPEN_SCALAR(path,flags,mode,dir_fd)
  actor_capture_scalar_first(cell,record,raw_fd)
  return actor_finish_adoption(cell,record)
 finally:
  actor_resolve_raw_finally(cell,record)

def actor_acquire_dup(record, cell, source, semantic_role, provenance):
 actor_record_begin(record,semantic_role,provenance)
 actor_raw_begin(cell,record)
 try:
  raw_fd = OS_DUP_SCALAR(source)
  actor_capture_scalar_first(cell,record,raw_fd)
  return actor_finish_adoption(cell,record)
 finally:
  actor_resolve_raw_finally(cell,record)

def actor_acquire_f_dupfd_cloexec(record, cell, source, minimum, semantic_role, provenance):
 require(0 <= minimum <= 255)
 actor_record_begin(record,semantic_role,provenance)
 actor_raw_begin(cell,record)
 try:
  raw_fd = FCNTL_F_DUPFD_CLOEXEC_SCALAR(source,minimum)
  actor_capture_scalar_first(cell,record,raw_fd)
  return actor_finish_adoption(cell,record)
 finally:
  actor_resolve_raw_finally(cell,record)

def actor_acquire_dup2(record, cell, source, target, semantic_role, provenance):
 require(0 <= target <= 255)
 require(global_record_owner_count(target,NONE) == 0)
 actor_record_begin(record,semantic_role,provenance)
 actor_raw_begin(cell,record)
 try:
  raw_fd = OS_DUP2_SCALAR(source,target,inheritable=True)
  actor_capture_scalar_first(cell,record,raw_fd)
  require(raw_fd == target)
  return actor_finish_adoption(cell,record)
 finally:
  actor_resolve_raw_finally(cell,record)

def actor_acquire_memfd(record, cell, label, semantic_role, provenance):
 actor_record_begin(record,semantic_role,provenance)
 actor_raw_begin(cell,record)
 try:
  raw_fd = OS_MEMFD_CREATE_SCALAR(label,MFD_CLOEXEC|MFD_ALLOW_SEALING)
  actor_capture_scalar_first(cell,record,raw_fd)
  return actor_finish_adoption(cell,record)
 finally:
  actor_resolve_raw_finally(cell,record)

def actor_capture_pair_first(out_pair, left_cell, left_record, right_cell, right_record):
 left_cell.raw_fd = out_pair.cell_0
 left_cell.state = b"LOCAL_RAW"
 right_cell.raw_fd = out_pair.cell_1
 right_cell.state = b"LOCAL_RAW"
 require(left_record.state == b"ACQUIRING" and left_record.raw_fd == -1)
 require(right_record.state == b"ACQUIRING" and right_record.raw_fd == -1)
 require(0 <= left_cell.raw_fd <= 255 and 0 <= right_cell.raw_fd <= 255)
 left_record.raw_fd = left_cell.raw_fd
 left_cell.state = b"SHADOW_OF_RECORD"
 right_record.raw_fd = right_cell.raw_fd
 right_cell.state = b"SHADOW_OF_RECORD"

def actor_acquire_pipe2(read_record, read_cell, write_record, write_cell, flags):
 actor_record_begin(read_record,b"PIPE_READ",b"PIPE2")
 actor_record_begin(write_record,b"PIPE_WRITE",b"PIPE2")
 actor_raw_begin(read_cell,read_record)
 actor_raw_begin(write_cell,write_record)
 ACTOR_PIPE2_OUT.cell_0 = -1
 ACTOR_PIPE2_OUT.cell_1 = -1
 try:
  C_PIPE2_INTO_PREALLOCATED(ACTOR_PIPE2_OUT,flags)
  actor_capture_pair_first(ACTOR_PIPE2_OUT,read_cell,read_record,write_cell,write_record)
  actor_finish_adoption(read_cell,read_record)
  actor_finish_adoption(write_cell,write_record)
  return read_record.raw_fd,write_record.raw_fd
 except BaseFailure:
  if read_record.state != b"CLOSED":
   actor_physical_close(read_record)
  if write_record.state != b"CLOSED":
   actor_physical_close(write_record)
  raise
 finally:
  actor_resolve_raw_finally(read_cell,read_record)
  actor_resolve_raw_finally(write_cell,write_record)

def actor_acquire_socketpair(left_record, left_cell, right_record, right_cell):
 actor_record_begin(left_record,b"CONTROL_LEFT",b"SOCKETPAIR")
 actor_record_begin(right_record,b"CONTROL_RIGHT",b"SOCKETPAIR")
 actor_raw_begin(left_cell,left_record)
 actor_raw_begin(right_cell,right_record)
 ACTOR_SOCKETPAIR_OUT.cell_0 = -1
 ACTOR_SOCKETPAIR_OUT.cell_1 = -1
 try:
  C_SOCKETPAIR_INTO_PREALLOCATED(
   AF_UNIX,SOCK_SEQPACKET|SOCK_CLOEXEC|SOCK_NONBLOCK,ACTOR_SOCKETPAIR_OUT,
  )
  actor_capture_pair_first(ACTOR_SOCKETPAIR_OUT,left_cell,left_record,right_cell,right_record)
  actor_finish_adoption(left_cell,left_record)
  actor_finish_adoption(right_cell,right_record)
  actor_adopt_socket_wrapper(left_record,ACTOR_WRAPPER_FALLBACK.left)
  actor_adopt_socket_wrapper(right_record,ACTOR_WRAPPER_FALLBACK.right)
  return left_record.wrapper_ref,right_record.wrapper_ref
 except BaseFailure:
  if left_record.state != b"CLOSED":
   actor_physical_close(left_record)
  if right_record.state != b"CLOSED":
   actor_physical_close(right_record)
  raise
 finally:
  actor_resolve_wrapper_fallback(ACTOR_WRAPPER_FALLBACK.left,left_record)
  actor_resolve_wrapper_fallback(ACTOR_WRAPPER_FALLBACK.right,right_record)
  actor_resolve_raw_finally(left_cell,left_record)
  actor_resolve_raw_finally(right_cell,right_record)

def actor_acquire_pidfd(record, cell, pid):
 actor_record_begin(record,b"PIDFD",b"PIDFD_OPEN")
 actor_raw_begin(cell,record)
 try:
  raw_fd = OS_PIDFD_OPEN_SCALAR(pid,0)
  actor_capture_scalar_first(cell,record,raw_fd)
  return actor_finish_adoption(cell,record)
 finally:
  actor_resolve_raw_finally(cell,record)

def actor_clone3_pidfd_prepare(record, cell, clone_args):
 actor_record_begin(record,b"CLONE3_PIDFD",b"CLONE3")
 actor_raw_begin(cell,record)
 ACTOR_CLONE3_OUTCOME.parent_pid = -1
 ACTOR_CLONE3_OUTCOME.pidfd = -1
 ACTOR_CLONE3_OUTCOME.branch = b"UNSET"
 clone_args.pidfd_pointer = ADDRESS_OF_PREALLOCATED(ACTOR_CLONE3_OUTCOME.pidfd)
 clone_args.flags = CLONE_PIDFD|CLONE_INTO_CGROUP

def actor_clone3_with_pidfd(record, cell, clone_args):
 actor_clone3_pidfd_prepare(record,cell,clone_args)
 try:
  C_CLONE3_AND_CAPTURE_OUTCOME_PREALLOCATED(clone_args,ACTOR_CLONE3_OUTCOME)
  actor_clone3_capture_parent_or_disarm_child_first(
   ACTOR_CLONE3_OUTCOME,cell,record,
  )
  if ACTOR_CLONE3_OUTCOME.branch == b"PARENT":
   actor_finish_adoption(cell,record)
   return ACTOR_CLONE3_OUTCOME.parent_pid,record.raw_fd
  require(ACTOR_CLONE3_OUTCOME.branch == b"CHILD")
  require(record.state == b"CLOSED" and cell.state == b"DISARMED")
  return 0,-1
 finally:
  actor_resolve_raw_finally(cell,record)

def actor_clone3_capture_parent_or_disarm_child_first(outcome, cell, record):
 if outcome.pidfd >= 0:
  cell.raw_fd = outcome.pidfd
  cell.state = b"LOCAL_RAW"
  require(outcome.branch == b"PARENT")
  require(record.state == b"ACQUIRING" and record.raw_fd == -1)
  require(outcome.pidfd <= 255)
  record.raw_fd = outcome.pidfd
  cell.state = b"SHADOW_OF_RECORD"
  return
 require(outcome.parent_pid == 0 and outcome.pidfd == -1)
 require(outcome.branch == b"CHILD")
 record.raw_fd = -1
 record.semantic_role = b"NONE"
 record.state = b"CLOSED"
 cell.raw_fd = -1
 cell.state = b"DISARMED"

def actor_adopt_socket_wrapper(record, wrapper_cell):
 require(record.state == b"OWNED")
 require(record.endpoint_state == b"NO_WRAPPER")
 wrapper_cell.ref = NONE
 wrapper_cell.raw_fd = record.raw_fd
 try:
  wrapper_cell.ref = SOCKET_WRAPPER_CONSTRUCT_PROTECTED(record.raw_fd)
  require(wrapper_cell.ref.fileno() == record.raw_fd)
  record.wrapper_ref = wrapper_cell.ref
  record.endpoint_state = b"ATTACHED"
  wrapper_cell.ref = NONE
  wrapper_cell.raw_fd = -1
  return record.wrapper_ref
 except BaseFailure:
  actor_resolve_wrapper_fallback(wrapper_cell,record)
  if record.state != b"CLOSED":
   actor_physical_close(record)
  raise
 finally:
  actor_resolve_wrapper_fallback(wrapper_cell,record)

def actor_resolve_wrapper_fallback(wrapper_cell, record):
 if wrapper_cell.ref is not NONE:
  observed = wrapper_cell.ref.fileno()
  if observed == record.raw_fd:
   detached = wrapper_cell.ref.detach()
   require(detached == record.raw_fd)
  elif observed != -1:
   fault(b"WRAPPER_IDENTITY_MISMATCH")
  wrapper_cell.ref = NONE
  wrapper_cell.raw_fd = -1

def actor_promote_record(record, new_semantic_role, expected_identity, expected_access):
 require(record.state == b"OWNED")
 require(record.semantic_role == b"QUARANTINE")
 actor_identity_revalidate_into(record)
 require(identity_equal(record.identity,expected_identity))
 require(record.access == expected_access)
 require(global_record_owner_count(record.raw_fd,record.record_id) == 0)
 require(poller_cells_consistent_for_record(record.record_id))
 record.semantic_role = new_semantic_role
 bounded_journal_write_noalloc(record.record_id,b"PROMOTED")
 return record.raw_fd

def actor_endpoint_detach_repair(record):
 require(record.state == b"CLOSE_RETRY")
 if record.endpoint_state == b"ATTACHED":
  record.endpoint_state = b"DETACH_REQUESTED"
 if record.endpoint_state == b"DETACH_REQUESTED":
  observed = record.wrapper_ref.fileno()
  if observed == -1:
   record.detached_raw_fd = record.raw_fd
   record.wrapper_ref = NONE
   record.endpoint_state = b"DETACHED"
  else:
   detached = record.wrapper_ref.detach()
   require(detached == record.raw_fd)
   record.detached_raw_fd = detached
   record.wrapper_ref = NONE
   record.endpoint_state = b"DETACHED"
 require(record.endpoint_state in (b"NO_WRAPPER",b"DETACHED"))

def actor_physical_close(record):
 if record.state == b"CLOSED":
  return b"CLOSED"
 require(record.state in (b"ACQUIRING",b"OWNED",b"CLOSE_RETRY"))
 record.state = b"CLOSE_RETRY"
 actor_identity_revalidate_into_or_ebadf(record)
 if identity_result_is_ebadf(record):
  record.raw_fd = -1
  record.endpoint_state = b"PROVED_CLOSED"
  record.state = b"CLOSED"
  return b"CLOSED"
 require(global_record_owner_count(record.raw_fd,record.record_id) == 0)
 reconcile_all_poller_cells_by_record_id(record.record_id)
 actor_endpoint_detach_repair(record)
 result = C_CLOSE_SAME_NUMBER(record.raw_fd)
 if result == b"RETURNED" or C_FSTAT_PROVES_EBADF(record.raw_fd):
  record.raw_fd = -1
  record.endpoint_state = b"PROVED_CLOSED"
  record.state = b"CLOSED"
  bounded_journal_write_noalloc(record.record_id,b"CLOSED")
  return b"CLOSED"
 require(C_FSTAT_IDENTITY_EQUALS(record.raw_fd,record.identity))
 record.state = b"CLOSE_RETRY"
 raise RetryPhysicalClose(record.record_id)

def actor_capture_rights_first(frame):
 C_CAPTURE_ALL_RIGHTS_TO_RAW_CELLS_NOFAIL(
  frame.msghdr,frame.capture_raw_cells_5,frame.installed_capacity_5,
 )
 frame.installed_count = frame.capture_raw_cells_5.installed_count
 frame.bad_header = frame.capture_raw_cells_5.bad_header
 frame.capture_complete = True
 frame.capture_fault = b"NONE"
 index = 0
 while index < min_noalloc(frame.installed_count,frame.semantic_capacity_4):
  record = frame.quarantine_record_ids[index]
  cell = frame.capture_raw_cells_5[index]
  try:
   require(cell.state == b"LOCAL_RAW")
   actor_record_begin(record,b"QUARANTINE",b"ACTOR_CONTROL_RECV")
   record.raw_fd = cell.raw_fd
   cell.record_id = record.record_id
   cell.state = b"SHADOW_OF_RECORD"
   actor_finish_adoption(cell,record)
  except BaseFailure:
   frame.capture_fault = b"QUARANTINE_ADOPTION_FAULT"
  index += 1
 frame.overflow_raw_cell = frame.capture_raw_cells_5[4]
 if frame.capture_fault != b"NONE":
  raise CaptureFaultAfterAllRightsAccounted()

def actor_reconcile_receive_frame(frame):
 index = 0
 while index < frame.semantic_capacity_4:
  record = frame.quarantine_record_ids[index]
  if record.state != b"CLOSED":
   actor_physical_close(record)
  index += 1
 index = 0
 while index < frame.installed_capacity_5:
  cell = frame.capture_raw_cells_5[index]
  if cell.state == b"LOCAL_RAW":
   STRICT_CLOSE_RAW_RETRY_SAME_NUMBER(cell)
   cell.state = b"DISARMED"
   cell.raw_fd = -1
  elif cell.state == b"SHADOW_OF_RECORD":
   record = actor_record_by_id(cell.record_id)
   if record.state != b"CLOSED":
    actor_physical_close(record)
   require(record.state == b"CLOSED")
   cell.state = b"DISARMED"
   cell.raw_fd = -1
  index += 1

def actor_recv_control(control_record, deadline):
 frame = ACTOR_CONTROL_FRAME
 actor_frame_reset_preallocated(frame)
 while True:
  positive_poll_actor_control(control_record,deadline)
  try:
   C_RECVMSG_INTO_PREALLOCATED(
    control_record.raw_fd,frame.msghdr,MSG_CMSG_CLOEXEC,
   )
   actor_capture_rights_first(frame)
   checkpoint_after_capture(deadline)
   require(not frame.msg_flags & (MSG_TRUNC|MSG_CTRUNC))
   require(frame.installed_count == 0)
   require(not frame.bad_header)
   require(frame.payload_count > 0 and frame.peer_address_empty)
   frame.validation_complete = True
   return frame.payload_65536,frame.payload_count
  except WouldBlock:
   actor_reconcile_receive_frame(frame)
   actor_frame_reset_preallocated(frame)
   continue
  except BaseFailure:
   actor_reconcile_receive_frame(frame)
   raise

# P27 RUNNER V16 EMBEDDED VALIDATOR BEGIN 4D2B16C7
# STATIC-VALIDATOR-TEXT; NO VALIDATOR PROCESS IS AUTHORIZED
VALID_PHYSICAL_TRANSITIONS = (
 (b"CLOSED",b"ACQUIRING"),
 (b"ACQUIRING",b"OWNED"),
 (b"ACQUIRING",b"CLOSE_RETRY"),
 (b"OWNED",b"CLOSE_RETRY"),
 (b"CLOSE_RETRY",b"CLOSE_RETRY"),
 (b"CLOSE_RETRY",b"CLOSED"),
)
VALID_RAW_TRANSITIONS = (
 (b"EMPTY",b"LOCAL_RAW"),
 (b"LOCAL_RAW",b"SHADOW_OF_RECORD"),
 (b"LOCAL_RAW",b"DISARMED"),
 (b"SHADOW_OF_RECORD",b"DISARMED"),
 (b"DISARMED",b"EMPTY"),
)
VALID_ENDPOINT_TRANSITIONS = (
 (b"NO_WRAPPER",b"ATTACHED"),
 (b"ATTACHED",b"DETACH_REQUESTED"),
 (b"DETACH_REQUESTED",b"DETACHED"),
 (b"DETACHED",b"PROVED_CLOSED"),
 (b"NO_WRAPPER",b"PROVED_CLOSED"),
)
RECEIVE_SITE_SPEC = (
 (b"actor_control",4,1,5),
 (b"monitored",4,1,5),
 (b"external_control",13,1,14),
 (b"external_receipt",13,1,14),
 (b"refusal",4,1,5),
)
MONITORED_PROMOTION_SPEC = (
 (b"stream_arm",(b"OUT_FD",b"ERR_FD",b"EVENTS_FD")),
 (b"pidfd_arm",(b"OUTER_PIDFD",)),
 (b"stage_bind",(b"STAGE_DIRFD",)),
 (b"containment_bind",(b"CGROUP_DIRFD",)),
)
OFFERED_13_VALIDATOR = (
 b"attempt",b"attempt_base_fd",b"stage_fd",b"cgfd",b"root_events_fd",
 b"root_kill_fd",b"out_fd",b"err_fd",b"events_fd",b"outer_pidfd",
 b"cgroup_base_fd",b"actor_control_fd",b"pending_expected_raw_fd",
)
SAFE_LOCAL_12_VALIDATOR = (
 b"transfer_control_fd",b"actor_pidfd_fd",b"external_owner_pidfd_fd",
 b"certificate_carrier_fd",b"envelope_carrier_fd",b"snapshot_carrier_fd",
 b"plan_carrier_fd",b"actor_source_carrier_fd",b"host_source_carrier_fd",
 b"reservation_carrier_fd",b"external_manifest_carrier_fd",
 b"watchdog_source_carrier_fd",
)
CLOSURE_PHASES_VALIDATOR = (b"NOT_STARTED",b"ACTIVE",b"CLOSED",b"RELEASED")
CLOSURE_MODES_VALIDATOR = (b"GENERIC_ACCEPTED",b"REFUSAL_ACCEPTED",b"DIRECT")
OUTER_READINESS_VALIDATOR = (
 b"PRE_READY",b"PRE_READY_OFFER_FROZEN",b"POST_OFFER_READY_RETAINED",
 b"POST_READY_OMITTED",b"ACCEPTED_CLOSED",b"ACCEPTED_OMITTED",
)

def validate_fixed_arithmetic():
 static_require(ACTOR_FIXED_RECORD_COUNT == 63)
 static_require(ACTOR_DIR_POOL_COUNT == 32)
 static_require(ACTOR_FILE_POOL_COUNT == 64)
 static_require(ACTOR_QUARANTINE_RECORD_COUNT == 4)
 static_require(ACTOR_MAPPING_PARK_COUNT == 24)
 static_require(ACTOR_MAPPING_TARGET_COUNT == 24)
 static_require(ACTOR_RECORD_COUNT == 211)
 static_require(sum_fixed(TERMINAL_PHASE_NS) == 2510000000)
 static_require(sum_fixed(REFUSAL_PHASE_NS) == 210000000)
 static_require(prefix_sum_fixed(REFUSAL_PHASE_NS,4) == 80000000)
 static_require(sum_fixed(REFUSAL_PHASE_NS[4:]) == 130000000)
 static_require(sum_fixed(GENERIC_TRANSFER_PHASE_NS) == 240000000)
 static_require(fixed_count(RECORD_DELTA_KINDS) == 17)
 static_require(fixed_count(CONTROL_SPEC) == 40)
 static_require(fixed_count(EXTERNAL_GATES) == 6)
 static_require(ACTOR_LIVE_HIGH_WATER < FD_LIMIT)

def validate_record_authority():
 static_require(no_field_named_owns(PhysicalRecord))
 static_require(b"CLOSED" in PHYSICAL_STATES)
 static_require(acquiring_with_fd_is_live())
 static_require(closed_is_only_release_proof())
 static_require(all_producers_begin_before_call())
 static_require(all_producers_have_raw_finally())
 static_require(pair_outputs_have_independent_cells())
 static_require(clone3_record_armed_before_syscall())
 static_require(no_allocating_operation_in_acquire_quarantine_promote_close())

def validate_receive_authority():
 static_require(RECEIVE_SITE_SPEC[0] == (b"actor_control",4,1,5))
 static_require(RECEIVE_SITE_SPEC[1] == (b"monitored",4,1,5))
 static_require(RECEIVE_SITE_SPEC[2] == (b"external_control",13,1,14))
 static_require(RECEIVE_SITE_SPEC[3] == (b"external_receipt",13,1,14))
 static_require(RECEIVE_SITE_SPEC[4] == (b"refusal",4,1,5))
 static_require(all_frames_use_msg_cmsg_cloexec())
 static_require(all_ancillary_capacities_include_overflow())
 static_require(capture_is_first_post_recvmsg_transition())
 static_require(no_semantic_role_before_full_validation())
 static_require(MONITORED_PROMOTION_SPEC[0][1] == (b"OUT_FD",b"ERR_FD",b"EVENTS_FD"))
 static_require(receipt_carriers_never_promote())

def validate_offer_and_close_authority():
 static_require(fixed_count(OFFERED_13_VALIDATOR) == 13)
 static_require(fixed_count(SAFE_LOCAL_12_VALIDATOR) == 12)
 static_require(watchdog_record_count() == 97)
 static_require(watchdog_blocking_count() == 72)
 static_require(refusal_offered_rights_are_exactly_empty())
 static_require(kill_scan_uses_leaf_and_actual_access_not_label())
 static_require(receiver_history_includes_received_then_closed())
 static_require(CLOSURE_PHASES_VALIDATOR == (b"NOT_STARTED",b"ACTIVE",b"CLOSED",b"RELEASED"))
 static_require(active_closure_has_no_return_edge())
 static_require(close_retry_wait_min_ms() >= 10)
 static_require(close_retry_wait_max_ms() <= 50)
 static_require(postrelease_kill_count() == 0)

def validate_preservation():
 static_require(open_only_refusal_finality_preserved())
 static_require(positive_polling_preserved())
 static_require(ack_cached_before_close_preserved())
 static_require(no_consume_uncertainty_preserved())
 static_require(nonpoison_receipt_preserved())
 static_require(actor_loss_plus_drained_eof_preserved())
 static_require(one_send_no_resend_preserved())
 static_require(carrier_before_o_excl_preserved())
 static_require(report_union_and_17_deltas_preserved())
 static_require(one_kill_sticky_pass_terminal_order_preserved())
 static_require(exact_six_external_gates_only())
# P27 RUNNER V16 EMBEDDED VALIDATOR END 4D2B16C7

def actor_protocol_preservation_surface():
 transition(b"OPEN",b"REFUSAL_STAGED_IMMUTABLE")
 transition(b"REFUSAL_STAGED_IMMUTABLE",b"ACK_CACHED_PRE_CLOSE")
 transition(b"ACK_CACHED_PRE_CLOSE",b"CLOSE_EFFECT_UNKNOWN")
 transition(b"CLOSE_EFFECT_UNKNOWN",b"CLOSED_NO_CONSUME")
 transition(b"CLOSED_NO_CONSUME",b"ACK_READY_CLOSED")
 transition(b"ACK_READY_CLOSED",b"ACK_EFFECT_UNKNOWN")
 transition(b"ACK_EFFECT_UNKNOWN",b"WAITING_RECEIPT")
 transition(b"WAITING_RECEIPT",b"RECEIPT_VERIFIED")
 transition(b"WAITING_RECEIPT",b"ACTOR_LOSS_DRAINED")
 transition(b"WAITING_RECEIPT",b"FINALITY_CAP_EXPIRED_HOLD")
 forbid_transition(b"FINALITY_CAP_EXPIRED_HOLD",b"OFFER_ELIGIBLE")
 require(mark_before_send(b"BEGIN_SEND_EFFECT_UNKNOWN"))
 require(mark_before_send(b"ARM_SEND_EFFECT_UNKNOWN"))
 require(candidate_receipt_nonpoisoning())
 require(receipt_commit_checks_deadline_after_recv_after_parse_before_commit())
 require(actor_loss_requires_pidfd_and_control_eof())
 require(no_offer_before_refusal_finality())
 require(refusal_tail_is_nonborrowable_130ms())

def actor_report_and_durability_surface():
 require(candidate_report_key_count() == 26)
 require(final_report_key_count() == 34)
 require(validate_report_union_occurs_at_candidate_final_and_reconciliation())
 require(record_delta_branch_count() == 17)
 require(carrier_is_complete_before_reservation_o_excl())
 require(publication_requires_verified_file_and_directory_durability())
 require(pass_is_sticky_after_durable_commit())
 require(terminal_order_is_candidate_seen_report_pass_ack_receipt_reconcile_close())

def actor_control_callsites(control_record, deadlines):
 ready = actor_recv_control(control_record,deadlines.ready)
 begin = actor_recv_control(control_record,deadlines.consume)
 commit = actor_recv_control(control_record,deadlines.consume)
 terminal_ack = actor_recv_control(control_record,deadlines.terminal)
 require(all_rights_empty(ready,begin,commit,terminal_ack))

def actor_main_static_transition():
 actor_enter_acquisition_epoch()
 actor_bootstrap_all_inherited_through_actor_adopt_inherited()
 actor_verify_frozen_inputs_without_trusting_peer_assertions()
 actor_protocol_preservation_surface()
 actor_report_and_durability_surface()
 actor_construct_carriers_before_reservations()
 actor_run_probe_sequence_with_exact_17_deltas()
 actor_publish_only_after_report_union_and_reconciliation()
 actor_terminal_handshake_ack_before_owner_close()
 actor_close_every_live_record_to_closed()
 actor_require_no_local_raw_and_no_active_poller()
 return b"STATIC_CONTROL_COMPLETE_NOT_EXECUTED"
P27 RUNNER V16 ACTOR SOURCE END 6C8A16F1

P27 RUNNER V16 WATCHDOG SOURCE BEGIN 91BE16D4
# STATIC-TRANSITION-TEXT; DO NOT IMPORT OR EXECUTE
TAG = b"P27E001V16"
PHYSICAL_STATES = (b"CLOSED", b"ACQUIRING", b"OWNED", b"CLOSE_RETRY")
RAW_STATES = (b"EMPTY", b"LOCAL_RAW", b"SHADOW_OF_RECORD", b"DISARMED")
ENDPOINT_STATES = (b"NO_WRAPPER", b"ATTACHED", b"DETACH_REQUESTED", b"DETACHED", b"PROVED_CLOSED")
CLOSURE_PHASES = (b"NOT_STARTED",b"ACTIVE",b"CLOSED",b"RELEASED")
CLOSURE_MODES = (b"GENERIC_ACCEPTED",b"REFUSAL_ACCEPTED",b"DIRECT")
CONTEXT_DOMAIN = b"P27E001_V16_DETACHED_ENVELOPE_CONTEXT\x00"
CERTIFICATE_DOMAIN = b"P27E001_V16_CERTIFICATE_DIGEST\x00"
ENVELOPE_TBS_DOMAIN = b"P27E001_V16_ENVELOPE_TBS\x00"
SIGNATURE_DOMAIN = b"P27E001_V16_ISSUER_SIGNATURE_PREIMAGE\x00"
RECEIPT_DOMAIN = b"P27E001_V16_ISSUER_RECEIPT\x00"
RESERVATION_TBS_DOMAIN = b"P27E001_V16_RESERVATION_TBS\x00"
RESERVATION_SIGNATURE_DOMAIN = b"P27E001_V16_RESERVATION_SIGNATURE\x00"
RESERVATION_RECEIPT_DOMAIN = b"P27E001_V16_RESERVATION_RECEIPT\x00"
FINAL_ENVELOPE_DOMAIN = b"P27E001_V16_FINAL_ENVELOPE\x00"
AUTH_DOMAIN = b"P27E001_V16_SESSION_AUTH\x00"
EXTERNAL_ACCEPTANCE_DOMAIN = b"P27E001_V16_EXTERNAL_ACCEPTANCE\x00"
ISSUER_KEY_BIND_DOMAIN = b"P27E001_V16_ISSUER_KEY_BIND\x00"
EMPTY_SHA = b"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
DOMAIN_SPEC = (
 CONTEXT_DOMAIN,CERTIFICATE_DOMAIN,ENVELOPE_TBS_DOMAIN,SIGNATURE_DOMAIN,
 RECEIPT_DOMAIN,RESERVATION_TBS_DOMAIN,RESERVATION_SIGNATURE_DOMAIN,
 RESERVATION_RECEIPT_DOMAIN,FINAL_ENVELOPE_DOMAIN,AUTH_DOMAIN,
 EXTERNAL_ACCEPTANCE_DOMAIN,ISSUER_KEY_BIND_DOMAIN,
)
OUTER_STATES = (
 b"PRE_READY",b"PRE_READY_OFFER_FROZEN",b"POST_OFFER_READY_RETAINED",
 b"POST_READY_OMITTED",b"ACCEPTED_CLOSED",b"ACCEPTED_OMITTED",
)
FD_LIMIT = 256
WATCHDOG_HIGH_WATER_COMPONENTS = (
 (b"PHYSICAL_RECORD_CAPACITY",97),
 (b"MAX_EXTERNAL_RECEIVE_RAW_CAPTURE",14),
 (b"MAX_SINGLE_PRODUCER_RAW_CAPTURE",1),
)
WATCHDOG_LIVE_HIGH_WATER = 112
WATCHDOG_PHASE_HIGH_WATER = (
 (b"ENTRY",15,110),
 (b"STATIC_VERIFY",57,210),
 (b"CONTAINMENT",91,255),
 (b"TRANSFER_RECEIVE",112,255),
 (b"CLOSURE",97,255),
)
CONTROL_SPEC = (
 (b"V16_ABORT",b"ABORTING",b"*",b"ABORT_NOTICE",b"control_deadline_ns"),
 (b"V16_READY",b"READY",b"WAIT_READY",b"NO_EFFECT",b"ready_deadline_ns"),
 (b"V16_REFUSE_PREBEGIN",b"REFUSE_PREBEGIN",b"WAIT_BEGIN",b"NO_CONSUME_REFUSAL",b"consume_deadline_ns"),
 (b"V16_REFUSE_POSTARM",b"REFUSE_POSTARM",b"WAIT_COMMIT",b"NO_CONSUME_REFUSAL",b"consume_deadline_ns"),
 (b"V16_REFUSE_ACK",b"REFUSAL_CLOSED_NO_CONSUME",b"WAIT_REFUSAL_ACK",b"REFUSAL_ACK_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 (b"V16_REFUSE_ACK_RECEIPT",b"REFUSAL_ACK_RECEIVED",b"WAIT_REFUSAL_RECEIPT",b"NO_REPLAY_RECEIPT",b"consume_deadline_ns"),
 (b"V16_REFUSAL_CLOSED",b"REFUSAL_DURABLY_CLOSED",b"WAIT_REFUSAL_CLOSED",b"OWNER_CLOSURE",b"consume_deadline_ns"),
 (b"V16_CONSUME_BEGIN",b"CONSUME_BEGIN",b"WAIT_BEGIN",b"BEGIN_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 (b"V16_CONSUME_ARMED",b"CONSUME_ARMED",b"WAIT_ARM",b"ARM_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 (b"V16_CONSUME_COMMIT",b"CONSUME_COMMIT",b"WAIT_COMMIT",b"COMMIT_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 (b"V16_CONSUMED_DURABLE",b"CONSUMED_DURABLE",b"WAIT_CONSUMED",b"INTENT_DURABLE",b"consume_deadline_ns"),
 (b"V16_STAGE_DURABLE",b"STAGE_DURABLE",b"WAIT_STAGE",b"FD_TRANSFER",b"stage_deadline_ns"),
 (b"V16_STAGE_ACK",b"STAGE_BOUND",b"WAIT_STAGE_ACK",b"STAGE_VERIFIED",b"stage_deadline_ns"),
 (b"V16_CONTAINMENT",b"CONTAINMENT_CANDIDATE",b"WAIT_CONTAINMENT",b"FD_TRANSFER",b"contain_deadline_ns"),
 (b"V16_CONTAINMENT_ACK",b"CONTAINMENT_BOUND",b"WAIT_CONTAINMENT_ACK",b"CONTAINMENT_VERIFIED",b"contain_deadline_ns"),
 (b"V16_STREAM_ARM",b"STREAM_ARM",b"WAIT_STREAM_ARM",b"FD_TRANSFER",b"launch_deadline_ns"),
 (b"V16_STREAMS_ARMED",b"STREAMS_ARMED",b"WAIT_STREAMS_ARMED",b"FD_VERIFIED",b"launch_deadline_ns"),
 (b"V16_PIDFD_ARM",b"PIDFD_ARM",b"WAIT_PIDFD_ARM",b"FD_TRANSFER",b"launch_deadline_ns"),
 (b"V16_PIDFD_ARMED",b"PIDFD_ARMED",b"WAIT_PIDFD_ARMED",b"PIDFD_VERIFIED",b"launch_deadline_ns"),
 (b"V16_RELEASE_CANDIDATE",b"RELEASE_CANDIDATE",b"WAIT_RELEASE",b"RELEASE_AUTHORIZATION",b"launch_deadline_ns"),
 (b"V16_RELEASE_DURABLE",b"RELEASE_DURABLE",b"WAIT_RELEASE_DURABLE",b"RELEASE_RECORD_DURABLE",b"launch_deadline_ns"),
 (b"V16_RESULT",b"RESULT",b"WAIT_RESULT",b"RESULT_NOTICE",b"result_deadline_ns"),
 (b"V16_RESULT_FRAME",b"RESULT_FRAME",b"WAIT_RESULT_FRAME",b"RESULT_FRAME",b"result_deadline_ns"),
 (b"V16_RESULT_END",b"RESULT_END",b"WAIT_RESULT_END",b"RESULT_COMPLETE",b"result_deadline_ns"),
 (b"V16_VALIDATED_CANDIDATE",b"VALIDATED_CANDIDATE",b"WAIT_VALIDATED",b"VALIDATION_NOTICE",b"ack_deadline_ns"),
 (b"V16_VALIDATED_DURABLE",b"VALIDATED_DURABLE",b"WAIT_VALIDATED_DURABLE",b"VALIDATED_RECORD_DURABLE",b"ack_deadline_ns"),
 (b"V16_ACK_COMMIT_INTENT",b"ACK_COMMIT_INTENT",b"WAIT_ACK_INTENT",b"ACK_COMMIT",b"ack_deadline_ns"),
 (b"V16_COMMITTED",b"COMMITTED",b"WAIT_COMMITTED",b"COMMIT_RECORD_DURABLE",b"ack_deadline_ns"),
 (b"V16_COMMITTED_SEEN",b"COMMITTED_SEEN",b"WAIT_COMMITTED_SEEN",b"ACK_RECEIPT",b"ack_deadline_ns"),
 (b"V16_EMPTY_FINAL_QUERY",b"EMPTY_FINAL_QUERY",b"WAIT_EMPTY_QUERY",b"REMOVE_QUERY",b"remove_deadline_ns"),
 (b"V16_EMPTY_FINAL_CONFIRMED",b"EMPTY_FINAL_CONFIRMED",b"WAIT_EMPTY_CONFIRMED",b"EMPTY_OBSERVED",b"remove_deadline_ns"),
 (b"V16_CGROUP_REMOVED",b"CGROUP_REMOVED",b"WAIT_REMOVED",b"REMOVE_EFFECT",b"remove_deadline_ns"),
 (b"V16_REMOVE_ACK",b"REMOVE_ACK",b"WAIT_REMOVE_ACK",b"REMOVAL_VERIFIED",b"remove_deadline_ns"),
 (b"V16_FINALIZE_CANDIDATE",b"FINALIZE_CANDIDATE",b"WAIT_FINALIZE",b"FINALIZE_NOTICE",b"candidate_deadline_ns"),
 (b"V16_TERMINAL_CANDIDATE_DURABLE",b"TERMINAL_CANDIDATE_DURABLE",b"WAIT_TERMINAL_CANDIDATE",b"CANDIDATE_DURABLE",b"candidate_deadline_ns"),
 (b"V16_TERMINAL_FAILURE_DURABLE",b"TERMINAL_FAILURE_DURABLE",b"WAIT_TERMINAL_FAILURE",b"FAILURE_REPORT_DURABLE",b"candidate_deadline_ns"),
 (b"V16_TERMINAL_SEEN",b"TERMINAL_SEEN",b"WAIT_TERMINAL_SEEN",b"TERMINAL_SEEN",b"seen_deadline_ns"),
 (b"V16_TERMINAL_ACK",b"TERMINAL_ACK",b"WAIT_TERMINAL_ACK",b"ACK_SEND_EFFECT_UNKNOWN",b"ack_deadline_ns"),
 (b"V16_TERMINAL_ACK_RECEIPT",b"ACK_RECEIVED_NO_REPLAY",b"WAIT_ACK_RECEIPT",b"NO_REPLAY_RECEIPT",b"receipt_deadline_ns"),
 (b"V16_TERMINAL_CLOSED",b"OWNER_CLOSED",b"WAIT_OWNER_CLOSED",b"OWNER_CLOSURE",b"closure_deadline_ns"),
)
CERTIFICATE_SCHEMA = (
 b"INHERIT_EXACT_192_KEYS_FROM_FROZEN_HOST_V15",
 b"INHERITED_TUPLE_BYTES_4840",
 b"INHERITED_TUPLE_LF_1",
 b"INHERITED_TUPLE_SHA256_ede6bffba35fb0331ea92e1c68f4b104dad0ff50822f0520853f28bc9476e196",
 b"V16_DOMAIN_AND_CONTROL_LABEL_BINDING_REQUIRED",
 b"EXACT_SIX_GATE_RECEIPTS_REQUIRED",
)
GENERIC_OFFER_V16_FIELDS = (
 b"offer_sha256",b"record_seq",b"predecessor_sha256",b"reason",
 b"rights_count",b"rights_manifest_sha256",b"full_live_census_sha256",
 b"offered_set_sha256",b"safe_local_set_sha256",b"kill_census_sha256",
 b"outer_frozen_identity",b"outer_readiness_state",b"pending_delta_sha256",
 b"terminal_subject_sha256",b"chain_head_sha256",b"no_replay",
)
ACCEPTANCE_V16_FIELDS = (
 b"offer_sha256",b"record_seq",b"predecessor_sha256",
 b"durable_receipt_sha256",b"issuer_signature",b"receiver_pid",
 b"receiver_starttime",b"installed_history_sha256",
 b"full_live_census_sha256",b"kill_census_sha256",
 b"outer_frozen_identity",b"outer_readiness_state",b"no_replay",
)
REFUSAL_OFFER_V16_FIELDS = (
 b"offer_sha256",b"record_seq",b"predecessor_sha256",b"request_sha256",
 b"ack_sha256",b"authoritative_receipt_sha256",b"finality_evidence_sha256",
 b"finality_deadline_ns",b"closure_deadline_ns",b"schedule_sha256",
 b"rights_count_exact_zero",b"no_replay",
)

OFFERED_13 = (
 b"attempt",b"attempt_base_fd",b"stage_fd",b"cgfd",b"root_events_fd",
 b"root_kill_fd",b"out_fd",b"err_fd",b"events_fd",b"outer_pidfd",
 b"cgroup_base_fd",b"actor_control_fd",b"pending_expected_raw_fd",
)
SAFE_LOCAL_12 = (
 b"transfer_control_fd",b"actor_pidfd_fd",b"external_owner_pidfd_fd",
 b"certificate_carrier_fd",b"envelope_carrier_fd",b"snapshot_carrier_fd",
 b"plan_carrier_fd",b"actor_source_carrier_fd",b"host_source_carrier_fd",
 b"reservation_carrier_fd",b"external_manifest_carrier_fd",
 b"watchdog_source_carrier_fd",
)
BLOCKING_FIXED_38 = (
 b"cap_status_fd",b"proc_starttime_fd",b"mount_fdinfo_fd",b"mount_table_fd",
 b"boot_id_fd",b"mount_graph_fd",b"dependency_root_fd",
 b"dependency_current_fd",b"dependency_following_fd",b"dependency_leaf_fd",
 b"reconcile_record_fd",b"record_create_fd",b"record_reopen_fd",
 b"attempt_received",b"pidfd_arm_procs_fd",b"pidfd_arm_status_fd",
 b"recovery_stage_base_fd",b"recovery_stage_received",
 b"recovery_stage_leaf_fd",b"stage_base_verify_fd",b"stage_received",
 b"stage_leaf_verify_fd",b"containment_received",b"containment_type_fd",
 b"containment_controllers_fd",b"containment_subtree_fd",
 b"containment_root_events_received",b"containment_root_kill_received",
 b"stream_out_received",b"stream_err_received",b"stream_events_received",
 b"outer_pidfd_received",b"static_runtime_root_fd",b"static_safe_base_fd",
 b"static_cgroup_type_fd",b"static_cgroup_controllers_fd",
 b"static_cgroup_subtree_fd",b"refusal_runtime_root_fd",
)
CONTROL_QUARANTINE_4 = (
 b"unexpected_control_right_0",b"unexpected_control_right_1",
 b"unexpected_control_right_2",b"unexpected_control_right_3",
)
EXTERNAL_QUARANTINE_13 = (
 b"external_unexpected_right_0",b"external_unexpected_right_1",
 b"external_unexpected_right_2",b"external_unexpected_right_3",
 b"external_unexpected_right_4",b"external_unexpected_right_5",
 b"external_unexpected_right_6",b"external_unexpected_right_7",
 b"external_unexpected_right_8",b"external_unexpected_right_9",
 b"external_unexpected_right_10",b"external_unexpected_right_11",
 b"external_unexpected_right_12",
)
RECEIPT_QUARANTINE_13 = (
 b"external_receipt_carrier_0",b"external_receipt_carrier_1",
 b"external_receipt_carrier_2",b"external_receipt_carrier_3",
 b"external_receipt_carrier_4",b"external_receipt_carrier_5",
 b"external_receipt_carrier_6",b"external_receipt_carrier_7",
 b"external_receipt_carrier_8",b"external_receipt_carrier_9",
 b"external_receipt_carrier_10",b"external_receipt_carrier_11",
 b"external_receipt_carrier_12",
)
REFUSAL_QUARANTINE_4 = (
 b"refusal_unexpected_right_0",b"refusal_unexpected_right_1",
 b"refusal_unexpected_right_2",b"refusal_unexpected_right_3",
)
BLOCKING_72 = (
 BLOCKING_FIXED_38 + CONTROL_QUARANTINE_4 + EXTERNAL_QUARANTINE_13
 + RECEIPT_QUARANTINE_13 + REFUSAL_QUARANTINE_4
)
WATCHDOG_SLOT_SPEC = OFFERED_13 + SAFE_LOCAL_12 + BLOCKING_72
require_static_count(OFFERED_13,13)
require_static_count(SAFE_LOCAL_12,12)
require_static_count(BLOCKING_FIXED_38,38)
require_static_count(BLOCKING_72,72)
require_static_count(WATCHDOG_SLOT_SPEC,97)
require_static_disjoint(OFFERED_13,SAFE_LOCAL_12,BLOCKING_72)

EXTERNAL_RIGHTS_ORDER = (
 b"ATTEMPT_DIRFD",b"ATTEMPT_BASE_DIRFD",b"STAGE_DIRFD",b"CGROUP_DIRFD",
 b"ROOT_EVENTS_FD",b"ROOT_KILL_FD",b"OUT_FD",b"ERR_FD",b"EVENTS_FD",
 b"OUTER_PIDFD",b"CGROUP_BASE_DIRFD",b"ACTOR_CONTROL_FD",
 b"PENDING_EXPECTED_RAW_FD",
)
SLOT_TO_EXTERNAL_ROLE = (
 (b"attempt",b"ATTEMPT_DIRFD"),
 (b"attempt_base_fd",b"ATTEMPT_BASE_DIRFD"),
 (b"stage_fd",b"STAGE_DIRFD"),
 (b"cgfd",b"CGROUP_DIRFD"),
 (b"root_events_fd",b"ROOT_EVENTS_FD"),
 (b"root_kill_fd",b"ROOT_KILL_FD"),
 (b"out_fd",b"OUT_FD"),
 (b"err_fd",b"ERR_FD"),
 (b"events_fd",b"EVENTS_FD"),
 (b"outer_pidfd",b"OUTER_PIDFD"),
 (b"cgroup_base_fd",b"CGROUP_BASE_DIRFD"),
 (b"actor_control_fd",b"ACTOR_CONTROL_FD"),
 (b"pending_expected_raw_fd",b"PENDING_EXPECTED_RAW_FD"),
)

class PhysicalRecord:
 __preallocated_fields__ = (
  b"record_id",b"slot",b"state",b"semantic_role",b"raw_fd",b"identity",
  b"access",b"leaf_identity",b"provenance",b"endpoint_state",
  b"wrapper_ref",b"detached_raw_fd",
 )

class RawCell:
 __preallocated_fields__ = (b"cell_id",b"state",b"raw_fd",b"record_id")

class ReceiveFrame:
 __preallocated_fields__ = (
  b"site",b"msghdr",b"iov",b"payload_65536",b"control_buffer",
  b"semantic_capacity",b"installed_capacity",b"quarantine_records",
  b"capture_raw_cells",b"overflow_raw_cell",b"installed_count",
  b"payload_count",b"msg_flags",b"capture_complete",
  b"validation_complete",b"history_cells",b"validated_view",
  b"capture_fault",
 )

class PollerCell:
 __preallocated_fields__ = (b"cell_id",b"poller_ref",b"record_id",b"mask",b"active")

class EndpointCell:
 __preallocated_fields__ = (b"record_id",b"state",b"wrapper_ref",b"raw_fd")

class StreamCell:
 __preallocated_fields__ = (b"record_id",b"buffer",b"used",b"overflow",b"eof")

class AcceptanceCommit:
 __preallocated_fields__ = (
  b"state",b"offer_sha256",b"sequence",b"predecessor",b"frozen_outer_identity",
  b"outer_readiness",b"installed_history_digest",b"full_live_digest",
  b"kill_census_digest",b"durable_receipt_sha256",b"issuer_result",
  b"no_replay",b"receiver_pid",b"receiver_starttime",
 )

class ClosureCell:
 __preallocated_fields__ = (
  b"phase",b"mode",b"plan_record_ids",b"plan_length",b"cursor",
  b"current_record_id",b"retry_wait_ms",b"timing_overrun",
 )

WATCHDOG_RECORDS = PREALLOC_PHYSICAL_RECORDS_EXACT(WATCHDOG_SLOT_SPEC)
WATCHDOG_RAW_CELLS = PREALLOC_RAW_CELLS_FOR_EVERY_RECORD_AND_PRODUCER()
WATCHDOG_IDENTITIES = PREALLOC_IDENTITY_CELLS(97)
WATCHDOG_POLLER_CELLS = PREALLOC_POLLER_CELLS()
WATCHDOG_ENDPOINT_CELLS = PREALLOC_ENDPOINT_CELLS()
WATCHDOG_JOURNAL_CELLS = PREALLOC_BOUNDED_JOURNAL_CELLS()
WATCHDOG_CLOSE_PLAN = PREALLOC_RECORD_ID_PLAN(97)
WATCHDOG_CLOSURE = PREALLOC_CLOSURE_CELL(
 phase=b"NOT_STARTED",mode=b"DIRECT",plan=WATCHDOG_CLOSE_PLAN,
)
WATCHDOG_ACCEPTANCE = PREALLOC_ACCEPTANCE_COMMIT(state=b"EMPTY")
WATCHDOG_STREAMS = PREALLOC_STREAM_CELLS_FOR_OUT_ERR()
MONITORED_FRAME = PREALLOC_RECEIVE_FRAME(
 b"monitored",4,5,5*CMSG_SPACE(sizeof_int),PREALLOC_RECORD_REFERENCE_CELLS(4),
)
EXTERNAL_CONTROL_FRAME = PREALLOC_RECEIVE_FRAME(
 b"external_control",13,14,14*CMSG_SPACE(sizeof_int),EXTERNAL_QUARANTINE_13,
)
EXTERNAL_RECEIPT_FRAME = PREALLOC_RECEIVE_FRAME(
 b"external_receipt",13,14,14*CMSG_SPACE(sizeof_int),RECEIPT_QUARANTINE_13,
)
REFUSAL_FRAME = PREALLOC_RECEIVE_FRAME(
 b"refusal",4,5,5*CMSG_SPACE(sizeof_int),REFUSAL_QUARANTINE_4,
)
WATCHDOG_WRAPPER_FALLBACK = PREALLOC_WRAPPER_CELL()
WATCHDOG_ACQUISITION_EPOCH = False

def watchdog_enter_acquisition_epoch():
 require(not WATCHDOG_ACQUISITION_EPOCH)
 require(rlimit_hard_nofile() >= 256)
 set_rlimit_soft_nofile(256)
 require(rlimit_soft_nofile() == 256)
 require(sum_fixed(WATCHDOG_HIGH_WATER_COMPONENTS) == 112)
 require(max_phase_live_records(WATCHDOG_PHASE_HIGH_WATER) == 112)
 WATCHDOG_ACQUISITION_EPOCH = True

def watchdog_record_begin(record, semantic_role, provenance):
 require(WATCHDOG_ACQUISITION_EPOCH)
 require(record.state == b"CLOSED")
 record.state = b"ACQUIRING"
 record.semantic_role = semantic_role
 record.raw_fd = -1
 record.identity.known = False
 record.access = b"UNKNOWN"
 record.leaf_identity = b"UNKNOWN"
 record.provenance = provenance
 record.endpoint_state = b"NO_WRAPPER"
 record.wrapper_ref = NONE
 record.detached_raw_fd = -1

def watchdog_raw_begin(cell, record):
 require(cell.state in (b"EMPTY",b"DISARMED"))
 require(record.state == b"ACQUIRING" and record.raw_fd == -1)
 cell.state = b"EMPTY"
 cell.raw_fd = -1
 cell.record_id = record.record_id

def watchdog_capture_scalar_first(cell, record, raw_fd):
 cell.raw_fd = raw_fd
 cell.state = b"LOCAL_RAW"
 require(record.state == b"ACQUIRING" and record.raw_fd == -1)
 require(0 <= raw_fd <= 255)
 record.raw_fd = raw_fd
 cell.state = b"SHADOW_OF_RECORD"

def watchdog_identity_revalidate_into(record):
 C_FSTAT_INTO_PREALLOCATED(record.raw_fd,record.identity)
 C_FCNTL_ACCESS_INTO_PREALLOCATED(record.raw_fd,record.identity)
 require(record.identity.known)
 record.access = record.identity.access

def watchdog_finish_adoption(cell, record):
 require(record.state == b"ACQUIRING")
 require(cell.state == b"SHADOW_OF_RECORD" and cell.raw_fd == record.raw_fd)
 watchdog_identity_revalidate_into(record)
 require(global_live_owner_count(record.raw_fd,record.record_id) == 0)
 record.state = b"OWNED"
 cell.raw_fd = -1
 cell.state = b"DISARMED"
 bounded_journal_write_noalloc(record.record_id,b"OWNED")
 return record.raw_fd

def watchdog_resolve_raw_finally(cell, record):
 if cell.state == b"LOCAL_RAW":
  STRICT_CLOSE_RAW_RETRY_SAME_NUMBER(cell)
  cell.raw_fd = -1
  cell.state = b"DISARMED"
 if cell.state == b"SHADOW_OF_RECORD":
  require(cell.raw_fd == record.raw_fd)
  if record.state == b"ACQUIRING":
   watchdog_physical_close(record)
  cell.raw_fd = -1
  cell.state = b"DISARMED"

def watchdog_adopt_inherited(record, cell, semantic_role, raw_fd, provenance):
 watchdog_record_begin(record,semantic_role,provenance)
 watchdog_raw_begin(cell,record)
 try:
  watchdog_capture_scalar_first(cell,record,raw_fd)
  return watchdog_finish_adoption(cell,record)
 finally:
  watchdog_resolve_raw_finally(cell,record)

def watchdog_acquire_open(record, cell, path, flags, mode, dir_fd, semantic_role, provenance):
 watchdog_record_begin(record,semantic_role,provenance)
 watchdog_raw_begin(cell,record)
 try:
  raw_fd = OS_OPEN_SCALAR(path,flags,mode,dir_fd)
  watchdog_capture_scalar_first(cell,record,raw_fd)
  return watchdog_finish_adoption(cell,record)
 finally:
  watchdog_resolve_raw_finally(cell,record)

def watchdog_acquire_memfd(record, cell, label, flags, semantic_role, provenance):
 watchdog_record_begin(record,semantic_role,provenance)
 watchdog_raw_begin(cell,record)
 try:
  raw_fd = OS_MEMFD_CREATE_SCALAR(label,flags)
  watchdog_capture_scalar_first(cell,record,raw_fd)
  return watchdog_finish_adoption(cell,record)
 finally:
  watchdog_resolve_raw_finally(cell,record)

def watchdog_acquire_dup(record, cell, source, semantic_role, provenance):
 watchdog_record_begin(record,semantic_role,provenance)
 watchdog_raw_begin(cell,record)
 try:
  raw_fd = OS_DUP_SCALAR(source)
  watchdog_capture_scalar_first(cell,record,raw_fd)
  return watchdog_finish_adoption(cell,record)
 finally:
  watchdog_resolve_raw_finally(cell,record)

def watchdog_adopt_socket_wrapper(record, endpoint_cell):
 require(record.state == b"OWNED")
 require(record.endpoint_state == b"NO_WRAPPER")
 endpoint_cell.record_id = record.record_id
 endpoint_cell.raw_fd = record.raw_fd
 endpoint_cell.state = b"NO_WRAPPER"
 endpoint_cell.wrapper_ref = NONE
 try:
  endpoint_cell.wrapper_ref = SOCKET_WRAPPER_CONSTRUCT_PROTECTED(record.raw_fd)
  require(endpoint_cell.wrapper_ref.fileno() == record.raw_fd)
  record.wrapper_ref = endpoint_cell.wrapper_ref
  record.endpoint_state = b"ATTACHED"
  endpoint_cell.wrapper_ref = NONE
  endpoint_cell.state = b"ATTACHED"
  return record.wrapper_ref
 except BaseFailure:
  if endpoint_cell.wrapper_ref is not NONE:
   observed = endpoint_cell.wrapper_ref.fileno()
   if observed == record.raw_fd:
    detached = endpoint_cell.wrapper_ref.detach()
    require(detached == record.raw_fd)
   elif observed != -1:
    fault(b"WRAPPER_IDENTITY_MISMATCH")
   endpoint_cell.wrapper_ref = NONE
  if record.state != b"CLOSED":
   watchdog_physical_close(record)
  raise
 finally:
  if endpoint_cell.wrapper_ref is not NONE:
   observed = endpoint_cell.wrapper_ref.fileno()
   if observed == record.raw_fd:
    detached = endpoint_cell.wrapper_ref.detach()
    require(detached == record.raw_fd)
   elif observed != -1:
    fault(b"WRAPPER_IDENTITY_MISMATCH")
   endpoint_cell.wrapper_ref = NONE

def watchdog_promote_in_place(record, new_role, expected_identity, expected_access, provenance):
 require(record.state == b"OWNED")
 require(record.semantic_role == b"QUARANTINE")
 watchdog_identity_revalidate_into(record)
 require(identity_equal(record.identity,expected_identity))
 require(record.access == expected_access)
 require(global_live_owner_count(record.raw_fd,record.record_id) == 0)
 require(global_semantic_role_owner_count(new_role) == 0)
 require(poller_cells_consistent_for_record(record.record_id))
 record.provenance = provenance
 record.semantic_role = new_role
 bounded_journal_write_noalloc(record.record_id,b"PROMOTED")
 return record.raw_fd

def register_poller_by_record_id(poller_cell, poller_ref, record, mask):
 require(not poller_cell.active)
 require(record.state == b"OWNED" and is_pidfd_role(record.semantic_role))
 poller_cell.record_id = record.record_id
 poller_cell.poller_ref = poller_ref
 poller_cell.mask = mask
 POLLER_REGISTER_NOALLOC(poller_ref,record.raw_fd,mask)
 poller_cell.active = True

def reconcile_pollers_by_record_id(record):
 index = 0
 while index < PREALLOC_POLLER_CELL_COUNT:
  cell = WATCHDOG_POLLER_CELLS[index]
  if cell.active and cell.record_id == record.record_id:
   POLLER_UNREGISTER_REPAIRABLE(cell.poller_ref,record.raw_fd)
   cell.active = False
   cell.poller_ref = NONE
   cell.record_id = -1
  index += 1

def pidfd_ready_event(mask):
 if mask & POLLNVAL:
  raise FaultSet(b"PIDFD_BINDING")
 return bool(mask & (POLLIN|POLLHUP|POLLERR))

def watchdog_endpoint_detach_repair(record):
 if record.endpoint_state == b"ATTACHED":
  record.endpoint_state = b"DETACH_REQUESTED"
 if record.endpoint_state == b"DETACH_REQUESTED":
  observed = record.wrapper_ref.fileno()
  if observed == -1:
   record.detached_raw_fd = record.raw_fd
   record.wrapper_ref = NONE
   record.endpoint_state = b"DETACHED"
  else:
   detached = record.wrapper_ref.detach()
   require(detached == record.raw_fd)
   record.detached_raw_fd = detached
   record.wrapper_ref = NONE
   record.endpoint_state = b"DETACHED"
 require(record.endpoint_state in (b"NO_WRAPPER",b"DETACHED"))

def watchdog_physical_close(record):
 if record.state == b"CLOSED":
  return b"CLOSED"
 require(record.state in (b"ACQUIRING",b"OWNED",b"CLOSE_RETRY"))
 record.state = b"CLOSE_RETRY"
 result = C_FSTAT_REVALIDATE_OR_EBADF(record.raw_fd,record.identity)
 if result == b"EBADF":
  reconcile_pollers_by_record_id(record)
  if record.endpoint_state in (b"ATTACHED",b"DETACH_REQUESTED"):
   require(record.wrapper_ref.fileno() == -1)
   record.detached_raw_fd = record.raw_fd
   record.wrapper_ref = NONE
   record.endpoint_state = b"DETACHED"
  record.raw_fd = -1
  record.endpoint_state = b"PROVED_CLOSED"
  record.state = b"CLOSED"
  return b"CLOSED"
 require(result == b"SAME_IDENTITY")
 require(global_live_owner_count(record.raw_fd,record.record_id) == 0)
 reconcile_pollers_by_record_id(record)
 watchdog_endpoint_detach_repair(record)
 result = C_CLOSE_SAME_NUMBER(record.raw_fd)
 if result == b"RETURNED" or C_FSTAT_PROVES_EBADF(record.raw_fd):
  record.raw_fd = -1
  record.endpoint_state = b"PROVED_CLOSED"
  record.state = b"CLOSED"
  bounded_journal_write_noalloc(record.record_id,b"CLOSED")
  return b"CLOSED"
 require(C_FSTAT_IDENTITY_EQUALS(record.raw_fd,record.identity))
 record.state = b"CLOSE_RETRY"
 raise RetryPhysicalClose(record.record_id)

def capture_rights_first(frame):
 C_CAPTURE_ALL_RIGHTS_TO_RAW_CELLS_NOFAIL(
  frame.msghdr,frame.capture_raw_cells,frame.installed_capacity,
 )
 frame.installed_count = frame.capture_raw_cells.installed_count
 frame.bad_header = frame.capture_raw_cells.bad_header
 frame.capture_complete = True
 frame.capture_fault = b"NONE"
 index = 0
 while index < min_noalloc(frame.installed_count,frame.semantic_capacity):
  record = frame.quarantine_records[index]
  cell = frame.capture_raw_cells[index]
  frame.history_cells[index].raw_fd = cell.raw_fd
  frame.history_cells[index].state = b"INSTALLED_RAW_CAPTURED"
  try:
   require(cell.state == b"LOCAL_RAW")
   watchdog_record_begin(record,b"QUARANTINE",b"SCM_RIGHTS")
   record.raw_fd = cell.raw_fd
   cell.record_id = record.record_id
   cell.state = b"SHADOW_OF_RECORD"
   watchdog_finish_adoption(cell,record)
   frame.history_cells[index].state = b"INSTALLED_QUARANTINED"
  except BaseFailure:
   frame.capture_fault = b"QUARANTINE_ADOPTION_FAULT"
  index += 1
 frame.overflow_raw_cell = frame.capture_raw_cells[frame.semantic_capacity]
 if frame.installed_count > frame.semantic_capacity:
  frame.history_cells[frame.semantic_capacity].raw_fd = frame.overflow_raw_cell.raw_fd
  frame.history_cells[frame.semantic_capacity].state = b"INSTALLED_OVERFLOW_RAW_CAPTURED"
 if frame.capture_fault != b"NONE":
  raise CaptureFaultAfterAllRightsAccounted()

def reconcile_receive_frame(frame):
 index = 0
 while index < frame.semantic_capacity:
  record = frame.quarantine_records[index]
  if record.state != b"CLOSED":
   watchdog_physical_close(record)
   frame.history_cells[index].state = b"INSTALLED_THEN_CLOSED"
  index += 1
 index = 0
 while index < frame.installed_capacity:
  cell = frame.capture_raw_cells[index]
  if cell.state == b"LOCAL_RAW":
   STRICT_CLOSE_RAW_RETRY_SAME_NUMBER(cell)
   cell.state = b"DISARMED"
   cell.raw_fd = -1
   frame.history_cells[index].state = b"INSTALLED_THEN_CLOSED"
  elif cell.state == b"SHADOW_OF_RECORD":
   record = record_by_id(cell.record_id)
   if record.state != b"CLOSED":
    watchdog_physical_close(record)
   require(record.state == b"CLOSED")
   cell.state = b"DISARMED"
   cell.raw_fd = -1
   frame.history_cells[index].state = b"INSTALLED_THEN_CLOSED"
  index += 1

def prepare_receive_frame_before_syscall(frame):
 receive_frame_reset_preallocated(frame)
 require(frame.capture_complete is False)

def configure_monitored_frame_noalloc(frame, caller):
 require(frame.site == b"monitored" and frame.semantic_capacity == 4)
 if caller == b"stream_arm":
  frame.quarantine_records[0] = record_by_home_slot(b"out_fd")
  frame.quarantine_records[1] = record_by_home_slot(b"err_fd")
  frame.quarantine_records[2] = record_by_home_slot(b"events_fd")
  frame.quarantine_records[3] = record_by_home_slot(b"unexpected_control_right_0")
 elif caller == b"pidfd_arm":
  frame.quarantine_records[0] = record_by_home_slot(b"outer_pidfd")
  frame.quarantine_records[1] = record_by_home_slot(b"unexpected_control_right_0")
  frame.quarantine_records[2] = record_by_home_slot(b"unexpected_control_right_1")
  frame.quarantine_records[3] = record_by_home_slot(b"unexpected_control_right_2")
 elif caller == b"stage_bind":
  frame.quarantine_records[0] = record_by_home_slot(b"stage_fd")
  frame.quarantine_records[1] = record_by_home_slot(b"unexpected_control_right_0")
  frame.quarantine_records[2] = record_by_home_slot(b"unexpected_control_right_1")
  frame.quarantine_records[3] = record_by_home_slot(b"unexpected_control_right_2")
 elif caller == b"containment_bind":
  frame.quarantine_records[0] = record_by_home_slot(b"cgfd")
  frame.quarantine_records[1] = record_by_home_slot(b"unexpected_control_right_0")
  frame.quarantine_records[2] = record_by_home_slot(b"unexpected_control_right_1")
  frame.quarantine_records[3] = record_by_home_slot(b"unexpected_control_right_2")
 else:
  require(caller == b"control_only")
  frame.quarantine_records[0] = record_by_home_slot(b"unexpected_control_right_0")
  frame.quarantine_records[1] = record_by_home_slot(b"unexpected_control_right_1")
  frame.quarantine_records[2] = record_by_home_slot(b"unexpected_control_right_2")
  frame.quarantine_records[3] = record_by_home_slot(b"unexpected_control_right_3")
 require(all_configured_records_are_closed(frame))

def validate_frame_common_after_capture(frame, deadline, expected_rights):
 require(frame.capture_complete)
 checkpoint_after_capture(deadline)
 require(not frame.msg_flags & (MSG_TRUNC|MSG_CTRUNC))
 require(not frame.bad_header)
 require(frame.installed_count == expected_rights)
 require(frame.payload_count > 0 and frame.peer_address_empty)

def validate_right_record_nonsemantic(record, expected):
 require(record.state == b"OWNED")
 require(record.semantic_role == b"QUARANTINE")
 watchdog_identity_revalidate_into(record)
 validate_expected_number_order(record,expected)
 validate_expected_identity(record,expected)
 validate_expected_type(record,expected)
 validate_expected_access(record,expected)
 validate_expected_inode(record,expected)
 validate_expected_cgroup(record,expected)
 validate_expected_stream(record,expected)
 require(record.semantic_role == b"QUARANTINE")

def promote_monitored_after_full_validation(frame, caller, expected):
 require(frame.validation_complete)
 if caller == b"stream_arm":
  require(frame.installed_count == 3)
  watchdog_promote_in_place(frame.quarantine_records[0],b"OUT_FD",expected[0].identity,expected[0].access,b"STREAM_ARM")
  watchdog_promote_in_place(frame.quarantine_records[1],b"ERR_FD",expected[1].identity,expected[1].access,b"STREAM_ARM")
  watchdog_promote_in_place(frame.quarantine_records[2],b"EVENTS_FD",expected[2].identity,expected[2].access,b"STREAM_ARM")
 elif caller == b"pidfd_arm":
  require(frame.installed_count == 1)
  watchdog_promote_in_place(frame.quarantine_records[0],b"OUTER_PIDFD",expected[0].identity,expected[0].access,b"PIDFD_ARM")
 elif caller == b"stage_bind":
  require(frame.installed_count == 1)
  watchdog_promote_in_place(frame.quarantine_records[0],b"STAGE_DIRFD",expected[0].identity,expected[0].access,b"STAGE_BIND")
 elif caller == b"containment_bind":
  require(frame.installed_count == 1)
  watchdog_promote_in_place(frame.quarantine_records[0],b"CGROUP_DIRFD",expected[0].identity,expected[0].access,b"CONTAINMENT_BIND")
 else:
  require(frame.installed_count == 0)

def recv_monitored(control_record, actor_pidfd_record, deadline, caller, expected):
 frame = MONITORED_FRAME
 while True:
  cmask,amask = positive_poll_control_and_pidfd(control_record,actor_pidfd_record,deadline)
  if cmask & POLLIN:
   try:
    prepare_receive_frame_before_syscall(frame)
    configure_monitored_frame_noalloc(frame,caller)
    C_RECVMSG_INTO_PREALLOCATED(
     control_record.raw_fd,frame.msghdr,MSG_CMSG_CLOEXEC,
    )
    capture_rights_first(frame)
    validate_frame_common_after_capture(frame,deadline,expected.count)
    validate_packet_framing_deadline_count_order(frame,expected,deadline)
    index = 0
    while index < expected.count:
     validate_right_record_nonsemantic(frame.quarantine_records[index],expected[index])
     index += 1
    frame.validation_complete = True
    promote_monitored_after_full_validation(frame,caller,expected)
    return frame.payload_65536,frame.payload_count
   except WouldBlock:
    reconcile_receive_frame(frame)
    continue
   except BaseFailure:
    reconcile_receive_frame(frame)
    raise
  if pidfd_ready_event(amask):
   raise ActorLost()
  if cmask & (POLLHUP|POLLERR):
   drain_control_before_declaring_loss(control_record,actor_pidfd_record,deadline)

def recv_external_control(transfer_record, deadline, expected):
 frame = EXTERNAL_CONTROL_FRAME
 while True:
 positive_poll_record(transfer_record,deadline)
 try:
   prepare_receive_frame_before_syscall(frame)
   C_RECVMSG_INTO_PREALLOCATED(
    transfer_record.raw_fd,frame.msghdr,MSG_CMSG_CLOEXEC,
   )
   capture_rights_first(frame)
   validate_frame_common_after_capture(frame,deadline,expected.count)
   validate_external_packet_complete(frame,expected,deadline)
   validate_all_external_rights_nonsemantic(frame,expected)
   frame.validation_complete = True
   commit_receiver_installed_history_before_close(frame)
   reconcile_receive_frame(frame)
   return frame.payload_65536,frame.payload_count
  except WouldBlock:
   reconcile_receive_frame(frame)
   continue
  except BaseFailure:
   reconcile_receive_frame(frame)
   raise

def recv_external_receipt(transfer_record, deadline, expected):
 frame = EXTERNAL_RECEIPT_FRAME
 while True:
 positive_poll_record(transfer_record,deadline)
 try:
   prepare_receive_frame_before_syscall(frame)
   C_RECVMSG_INTO_PREALLOCATED(
    transfer_record.raw_fd,frame.msghdr,MSG_CMSG_CLOEXEC,
   )
   capture_rights_first(frame)
   checkpoint_after_capture(deadline)
   validate_frame_common_after_capture(frame,deadline,expected.count)
   validate_external_receipt_packet(frame,expected,deadline)
   validate_receipt_carriers_nonsemantic(frame,expected)
   frame.validation_complete = True
   bind_validated_receipt_view_noalloc(frame.validated_view,frame,expected)
   commit_receiver_installed_history_before_close(frame)
   reconcile_receive_frame(frame)
   require(all_receipt_carrier_records_closed(frame))
   return frame.validated_view
  except WouldBlock:
   reconcile_receive_frame(frame)
   continue
  except BaseFailure:
   reconcile_receive_frame(frame)
   raise

def recv_refusal(actor_control_record, actor_pidfd_record, deadline, expected):
 frame = REFUSAL_FRAME
 while True:
  cmask,amask = positive_poll_control_and_pidfd(actor_control_record,actor_pidfd_record,deadline)
 if cmask & POLLIN:
  try:
    prepare_receive_frame_before_syscall(frame)
    C_RECVMSG_INTO_PREALLOCATED(
     actor_control_record.raw_fd,frame.msghdr,MSG_CMSG_CLOEXEC,
    )
    capture_rights_first(frame)
    validate_frame_common_after_capture(frame,deadline,expected.count)
    validate_refusal_candidate_nonpoisoning(frame,expected,deadline)
    require(expected.count == 0)
    frame.validation_complete = True
    return frame.payload_65536,frame.payload_count
   except WouldBlock:
    reconcile_receive_frame(frame)
    continue
   except CandidateReject:
    record_bounded_nonauthoritative_fault_digest(frame)
    reconcile_receive_frame(frame)
    continue
   except BaseFailure:
    reconcile_receive_frame(frame)
    raise
  if pidfd_ready_event(amask):
   require(drain_actor_control_to_exact_eof(actor_control_record))
   return b"ACTOR_LOSS_DRAINED",len(b"ACTOR_LOSS_DRAINED")

def monitored_callsites(control_record, actor_pidfd_record, deadlines, expected):
 recv_monitored(control_record,actor_pidfd_record,deadlines.stream,b"stream_arm",expected.stream_three)
 recv_monitored(control_record,actor_pidfd_record,deadlines.pidfd,b"pidfd_arm",expected.pidfd_one)
 recv_monitored(control_record,actor_pidfd_record,deadlines.stage,b"stage_bind",expected.stage_one)
 recv_monitored(control_record,actor_pidfd_record,deadlines.containment,b"containment_bind",expected.containment_one)
 recv_monitored(control_record,actor_pidfd_record,deadlines.control,b"control_only",expected.zero)

def full_live_census_into(snapshot):
 snapshot.reset_preallocated()
 record_index = 0
 while record_index < 97:
  record = WATCHDOG_RECORDS[record_index]
  if record.state == b"ACQUIRING":
   snapshot.add_record_noalloc(record,b"ACQUIRING_BLOCK")
  elif record.state in (b"OWNED",b"CLOSE_RETRY"):
   snapshot.add_record_noalloc(record,b"LIVE")
  record_index += 1
 raw_index = 0
 while raw_index < WATCHDOG_RAW_CELL_COUNT:
  raw = WATCHDOG_RAW_CELLS[raw_index]
  if raw.state == b"LOCAL_RAW":
   snapshot.add_raw_noalloc(raw,b"LIVE_LOCAL_RAW_BLOCK")
  raw_index += 1
 snapshot.seal_noalloc()
 return snapshot

def classify_generic_offer_into(snapshot, offered_out, safe_out):
 require(snapshot.sealed)
 index = 0
 while index < snapshot.record_count:
  record = snapshot.records[index]
  require(record.identity.known and record.access != b"UNKNOWN")
  require(record.state == b"OWNED")
  if record.slot in OFFERED_13:
   require(record.semantic_role == external_role_for_slot(record.slot))
   offered_out.add_noalloc(record.record_id,record.slot,record.raw_fd,record.identity,record.access)
  elif record.slot in SAFE_LOCAL_12:
   safe_out.add_noalloc(record.record_id,record.slot,record.raw_fd,record.identity,record.access)
  else:
   require(record.slot in BLOCKING_72)
   raise OfferBlocked(record.record_id)
  index += 1
 require(snapshot.raw_count == 0)
 require(offered_out.slots_are_subset_of(OFFERED_13))
 require(safe_out.slots_are_subset_of(SAFE_LOCAL_12))
 return offered_out,safe_out

def freeze_generic_offer(context):
 require(context.offer_cache is NONE)
 full_live_census_into(context.current_live)
 classify_generic_offer_into(context.current_live,context.current_offered,context.current_safe)
 validate_unique_kill_scan(context,required=context.containment_bound)
 prepare_outer_offer_identity_before_freeze(context)
 final_zero_time_combined_readiness_snapshot(context)
 if context.outer_state == b"POST_READY_OMITTED":
  discard_unactivated_candidate_without_sequence_consumption(context)
  return freeze_generic_offer(context)
 context.outer_state = b"PRE_READY_OFFER_FROZEN"
 serialize_offer_once_into_preallocated_cache(
  context.offer_cache,context.current_live,context.current_offered,
  context.current_safe,context.outer_frozen_identity,
 )
 context.offer_frozen_live_digest = context.current_live.digest
 context.offer_frozen_offered_digest = context.current_offered.digest
 context.offer_frozen_safe_digest = context.current_safe.digest
 context.offer_possible_send = False
 context.offer_state = b"FROZEN_NOT_SENT"

def assert_frozen_generic_offer(context, stage):
 full_live_census_into(context.current_live)
 classify_generic_offer_into(context.current_live,context.current_offered,context.current_safe)
 require(context.current_live.digest == context.offer_frozen_live_digest)
 require(context.current_offered.digest == context.offer_frozen_offered_digest)
 require(context.current_safe.digest == context.offer_frozen_safe_digest)
 require(context.offer_cache.bytes_immutable)
 require(context.outer_frozen_identity == context.offer_cache.outer_identity)
 require(context.outer_state in (b"PRE_READY_OFFER_FROZEN",b"POST_OFFER_READY_RETAINED"))
 validate_unique_kill_scan(context,required=context.containment_bound)
 bounded_journal_write_noalloc(stage,b"OFFER_SET_REVALIDATED")

def refusal_offer_guard(context):
 require(context.refusal_slot_locked)
 require(context.refusal_finality_state in (b"RECEIPT_VERIFIED",b"ACTOR_LOSS_DRAINED"))
 require(context.refusal_close_state in (b"CLOSED_NO_CONSUME",b"CLOSE_EFFECT_UNKNOWN_RETAINED"))
 require(context.refusal_ack_cache_is_exact)
 require(context.refusal_offer_cache is NONE or context.refusal_offer_cache.bytes_immutable)
 require(all_blocking_72_closed())
 require(all_generic_offered_records_closed_except_optional_actor_control())
 require(all_raw_cells_resolved())
 require(context.refusal_offered_rights.count == 0)
 return b"EXACT_EMPTY_RIGHTS"

def freeze_refusal_offer(context):
 refusal_offer_guard(context)
 serialize_refusal_offer_once_with_empty_rights(context.refusal_offer_cache)
 require(context.refusal_offer_cache.rights_count == 0)
 context.refusal_possible_send = False
 context.refusal_offer_state = b"FROZEN_EMPTY_RIGHTS_NOT_SENT"

def scan_actual_writable_kill_into(context, census):
 census.reset_preallocated()
 index = 0
 while index < 97:
  record = WATCHDOG_RECORDS[index]
  if record.state in (b"ACQUIRING",b"OWNED",b"CLOSE_RETRY") and record.raw_fd >= 0:
   require(record.identity.known)
   require(record.access != b"UNKNOWN")
   require(record.leaf_identity != b"UNKNOWN")
   if record.leaf_identity == context.bound_leaf_identity and record.access in (O_WRONLY,O_RDWR):
    census.add_noalloc(record.record_id,record.raw_fd,record.access,record.leaf_identity)
  index += 1
 return census

def validate_unique_kill_scan(context, required):
 scan_actual_writable_kill_into(context,context.kill_census)
 expected = 1 if required else 0
 require(context.kill_census.count == expected)
 if expected == 1:
  require(context.kill_census.entries[0].raw_fd == context.root_kill_record.raw_fd)
 return context.kill_census.digest

def validate_postrelease_zero_kill(context):
 require(WATCHDOG_CLOSURE.phase == b"RELEASED")
 return validate_unique_kill_scan(context,required=False)

def observe_outer_readiness(context, mask, before_freeze):
 ready = pidfd_ready_event(mask)
 if not ready:
  return
 if before_freeze:
  require(context.outer_state == b"PRE_READY")
  context.outer_state = b"POST_READY_OMITTED"
  watchdog_physical_close(context.outer_pidfd_record)
  record_outer_received_then_closed_history(context)
  discard_unactivated_candidate_without_sequence_consumption(context)
 else:
  require(context.outer_state == b"PRE_READY_OFFER_FROZEN")
  context.outer_state = b"POST_OFFER_READY_RETAINED"
  require(context.offer_cache.bytes_immutable)
  require(context.offer_cache.sequence == context.frozen_sequence)
  require(context.offer_cache.predecessor == context.frozen_predecessor)
  require(context.offer_cache.outer_identity == context.outer_frozen_identity)
  require(context.offer_resend_count == 0)

def external_identity_for_outer(context, record):
 require(record.record_id == context.outer_pidfd_record.record_id)
 require(record.state == b"OWNED")
 require(context.outer_state in (b"PRE_READY_OFFER_FROZEN",b"POST_OFFER_READY_RETAINED"))
 watchdog_identity_revalidate_into(record)
 require(identity_equal(record.identity,context.outer_frozen_identity.physical_identity))
 require(record.raw_fd == context.outer_frozen_identity.raw_fd)
 return context.outer_frozen_identity.serialized_bytes

def acceptance_commit_once(context, receipt):
 require(WATCHDOG_ACCEPTANCE.state == b"EMPTY")
 assert_frozen_generic_offer(context,b"ACCEPTANCE")
 verify_durable_receipt_signature_no_replay(receipt)
 verify_receiver_pid_starttime(receipt)
 verify_exhaustive_receiver_installed_history(receipt)
 require(receipt.full_live_digest == context.offer_frozen_live_digest)
 require(receipt.kill_census_digest == context.kill_census.digest)
 require(receipt.outer_frozen_identity == context.outer_frozen_identity.serialized_bytes)
 require(receipt.outer_readiness == context.outer_state)
 WATCHDOG_ACCEPTANCE.offer_sha256 = context.offer_cache.sha256
 WATCHDOG_ACCEPTANCE.sequence = context.offer_cache.sequence
 WATCHDOG_ACCEPTANCE.predecessor = context.offer_cache.predecessor
 WATCHDOG_ACCEPTANCE.frozen_outer_identity = context.outer_frozen_identity.serialized_bytes
 WATCHDOG_ACCEPTANCE.outer_readiness = context.outer_state
 WATCHDOG_ACCEPTANCE.installed_history_digest = receipt.installed_history_digest
 WATCHDOG_ACCEPTANCE.full_live_digest = receipt.full_live_digest
 WATCHDOG_ACCEPTANCE.kill_census_digest = receipt.kill_census_digest
 WATCHDOG_ACCEPTANCE.durable_receipt_sha256 = receipt.sha256
 WATCHDOG_ACCEPTANCE.issuer_result = b"VERIFIED"
 WATCHDOG_ACCEPTANCE.no_replay = True
 WATCHDOG_ACCEPTANCE.receiver_pid = receipt.receiver_pid
 WATCHDOG_ACCEPTANCE.receiver_starttime = receipt.receiver_starttime
 WATCHDOG_ACCEPTANCE.state = b"COMMITTED"
 if context.outer_state == b"POST_OFFER_READY_RETAINED":
  record_outer_received_then_closed_history(context)
 return b"COMMITTED"

def closure_plan_install_noalloc(context, mode):
 cell = WATCHDOG_CLOSURE
 require(cell.phase == b"NOT_STARTED")
 require(mode in CLOSURE_MODES)
 require(all_nonownership_checks_complete(context,mode))
 require(no_pending_checkpoint_or_deadline(context))
 require(no_pending_offer_receive_send(context))
 build_exact_record_id_plan_into_preallocated(context,cell.plan_record_ids)
 cell.plan_length = exact_plan_length(context)
 cell.cursor = 0
 cell.current_record_id = -1
 cell.retry_wait_ms = 10
 cell.timing_overrun = False
 cell.mode = mode
 cell.phase = b"ACTIVE"

def closure_retry_wait_positive(cell):
 require(cell.phase == b"ACTIVE")
 if cell.retry_wait_ms < 10:
  cell.retry_wait_ms = 10
 if cell.retry_wait_ms > 50:
  cell.retry_wait_ms = 50
 POSITIVE_MONOTONIC_WAIT_MS(cell.retry_wait_ms)
 if cell.retry_wait_ms < 50:
  cell.retry_wait_ms = min_noalloc(50,cell.retry_wait_ms+10)

def closure_no_return_driver(context):
 cell = WATCHDOG_CLOSURE
 require(cell.phase == b"ACTIVE")
 while True:
  if cell.cursor < cell.plan_length:
   record_id = cell.plan_record_ids[cell.cursor]
   cell.current_record_id = record_id
   record = record_by_id(record_id)
   try:
    watchdog_physical_close(record)
    require(record.state == b"CLOSED")
    cell.cursor += 1
    cell.current_record_id = -1
    cell.retry_wait_ms = 10
   except RetryPhysicalClose:
    closure_retry_wait_positive(cell)
   except PersistentCloseFault:
    cell.timing_overrun = True
    closure_retry_wait_positive(cell)
   continue
  if cell.phase == b"ACTIVE":
   require(all_97_records_closed())
   require(all_raw_cells_resolved())
   require(all_poller_cells_inactive())
   require(all_endpoints_no_wrapper_or_proved_closed())
   cell.phase = b"CLOSED"
  if cell.phase == b"CLOSED":
   require(cell.mode in CLOSURE_MODES)
   require(WATCHDOG_ACCEPTANCE.state == b"COMMITTED" or cell.mode == b"DIRECT")
   require(local_actual_writable_kill_count() == 0)
   cell.phase = b"RELEASED"
  if cell.phase == b"RELEASED":
   close_probe(context)
   NO_RETURN_RELEASE_HANDOFF(context)
   continue

def start_generic_accepted_closure(context):
 require(WATCHDOG_ACCEPTANCE.state == b"COMMITTED")
 require(context.offer_send_count == 1)
 require(context.offer_resend_count == 0)
 closure_plan_install_noalloc(context,b"GENERIC_ACCEPTED")
 closure_no_return_driver(context)
 unreachable()

def start_refusal_accepted_closure(context):
 require(context.refusal_acceptance_state == b"COMMITTED")
 require(context.refusal_offer_cache.rights_count == 0)
 require(context.refusal_send_count == 1)
 require(context.refusal_resend_count == 0)
 closure_plan_install_noalloc(context,b"REFUSAL_ACCEPTED")
 closure_no_return_driver(context)
 unreachable()

def start_direct_closure(context):
 require(context.direct_terminal_durable)
 closure_plan_install_noalloc(context,b"DIRECT")
 closure_no_return_driver(context)
 unreachable()

def close_probe(context):
 if WATCHDOG_CLOSURE.phase != b"RELEASED":
  raise ClosureNotReleased()
 require(all_97_records_closed())
 require(all_raw_cells_empty_or_disarmed())
 require(all_poller_cells_inactive())
 require(all_endpoints_no_wrapper_or_proved_closed())
 require(local_actual_writable_kill_count() == 0)
 return b"POSTRELEASE_IDEMPOTENT_ZERO_KILL"

def drain(record, stream_cell):
 require(stream_cell.record_id == record.record_id)
 while True:
  try:
   count = C_READ_INTO_PREALLOCATED_SCRATCH(record.raw_fd,stream_cell.scratch)
  except WouldBlock:
   return stream_cell.overflow,stream_cell.eof
  except Interrupted:
   continue
  except BaseFailure:
   raise FaultSet(b"CAPTURE_IO")
  if count == 0:
   stream_cell.eof = True
   return stream_cell.overflow,stream_cell.eof
  room = STREAM_CAP - stream_cell.used
  if count > room:
   stream_cell.overflow = True
  copied = min_noalloc(count,max_noalloc(room,0))
  COPY_BYTES_NOALLOC(
   stream_cell.buffer,stream_cell.used,stream_cell.scratch,0,copied,
  )
  stream_cell.used += copied

def refusal_finality_surface(context):
 require(context.refusal_slot_locked implies context.refusal_slot_nonnull)
 require(context.refusal_state_was_open_at_validation())
 require(context.ack_constructed_and_cached_before_close())
 require(context.close_no_consume_never_precedes_ack_cache())
 require(context.authoritative_receipt_candidate_is_nonpoisoning())
 require(context.recovery_resamples_clock_at_each_checkpoint())
 require(context.finality_deadline_offset_ns == 80000000)
 require(context.closure_deadline_offset_ns == 210000000)
 require(context.nonborrowable_tail_ns == 130000000)
 require(context.actor_loss_finality_requires_pidfd_and_drained_eof())
 require(context.late_exact_receipt_cannot_mutate_after_finality())
 require(context.refusal_offer_rights_count == 0)
 require(context.RefusalFinalityPending_routes_to_same_locked_slot())
 require(context.RefusalFinalityPending_never_enters_generic_offer())

def transfer_surface(context):
 require(context.offer_bytes_frozen_before_possible_send())
 require(context.offer_send_count <= 1)
 require(context.offer_resend_count == 0)
 require(context.uncertain_send_retains_all_capabilities())
 require(context.acceptance_uncertainty_retains_frozen_offer())
 require(context.receiver_history_is_exhaustive())
 require(context.receiver_history_includes_received_then_closed_outer_pidfd())
 require(context.acceptance_uses_one_commit_object())
 require(context.committed_has_no_downgrade())

def durable_surface(context):
 require(context.carrier_complete_before_o_excl_reservation())
 require(context.semantic_delta_kind_count == 17)
 require(context.report_union_candidate_keys == 26)
 require(context.report_union_final_keys == 34)
 require(context.durability_reconciliation_exact())
 require(context.publication_verified())
 require(context.kill_ticket_count <= 1)
 require(context.kill_call_count <= 1)
 require(context.pass_state_is_sticky())
 require(context.terminal_durable_order_exact())

def watchdog_main_static_transition(context):
 watchdog_enter_acquisition_epoch()
 watchdog_bootstrap_all_inherited_through_watchdog_adopt_inherited()
 watchdog_verify_entry_dependency_identity_and_six_external_gate_receipts()
 refusal_finality_surface(context)
 monitored_callsites(context.actor_control,context.actor_pidfd,context.deadlines,context.expected)
 drain(context.out_record,WATCHDOG_STREAMS.out)
 drain(context.err_record,WATCHDOG_STREAMS.err)
 durable_surface(context)
 if context.generic_transfer_required:
  freeze_generic_offer(context)
  assert_frozen_generic_offer(context,b"PRE_SEND")
  send_offer_once_mark_possible_before_send(context)
  receipt = recv_external_receipt(context.transfer_control,context.transfer_deadline,context.expected_receipt)
  acceptance_commit_once(context,receipt)
  start_generic_accepted_closure(context)
 if context.refusal_transfer_required:
  recv_refusal(context.actor_control,context.actor_pidfd,context.refusal_finality_deadline,context.expected_refusal)
  freeze_refusal_offer(context)
  send_refusal_offer_once_mark_possible_before_send(context)
  receive_and_commit_refusal_acceptance(context)
  start_refusal_accepted_closure(context)
 start_direct_closure(context)
 unreachable()
P27 RUNNER V16 WATCHDOG SOURCE END 91BE16D4

## 13. Exact raw-span census

All six delimiter lines must be unique exact full lines. The actor raw span
contains the embedded-validator delimiters and raw span. The two outer spans
are separated by exactly one blank line. Each raw span ends in LF and consists
only of printable ASCII or LF.

- Actor begin delimiter: line 246.
- Actor raw span: lines 247 through 1062 inclusive; 35125 bytes; 816 LF;
  SHA256 8f43d97b03bf1f98684829b80f5bf4d1d9140ff2b4cf7a0d72fedd1fd2b872a2.
- Embedded-validator begin delimiter: line 887.
- Embedded-validator raw span: lines 888 through 1010 inclusive; 5378
  bytes; 123 LF; SHA256
  b6a9c63c0a5dcb19271778f1c999bb903ad9b227c959633d0195198906897d8a.
- Embedded-validator end delimiter: line 1011.
- Actor end delimiter: line 1063.
- Watchdog begin delimiter: line 1065.
- Watchdog raw span: lines 1066 through 2176 inclusive; 49185 bytes; 1111
  LF; SHA256
  6fcfe7c4efa70f0f76c17b141f5d2d93083187f568b251115b26aa282baa0291.
- Watchdog end delimiter: line 2177.

## 14. Static source and transition census

This is a raw-text responsibility statement, not a parse, compilation,
validator run, microtest, or executability claim.

- Physical states are exactly CLOSED, ACQUIRING, OWNED, CLOSE_RETRY; no
  independent owns authority exists. ACQUIRING with a nonnegative fd is live.
- Raw fallback states are exactly EMPTY, LOCAL_RAW, SHADOW_OF_RECORD,
  DISARMED. Each producer begins protection before its syscall.
- Actor producers are open, dup, F_DUPFD_CLOEXEC, dup2, memfd, pipe2,
  socketpair, pidfd_open, and clone3 pidfd. Watchdog producers are open,
  memfd, and dup. Inherited and received adoption use the same discipline.
- Five receive boundaries have installed capacities 5, 5, 14, 14, and 5.
  Every buffer includes one overflow capture and uses MSG_CMSG_CLOEXEC.
- The first post-recvmsg transition is fixed capture. Promotion occurs only
  after full validation and only in place on one physical record.
- The watchdog registry is exactly 13 offered plus 12 unconditional
  safe-local plus 72 blocking records, totaling 97. Refusal is an independent
  empty-rights special case.
- Unique kill scans full live identity and actual access. Unknown facts block.
- One ClosureCell has four phases and three modes. ACTIVE has no return edge.
  Retry waits are positive and bounded from 10 through 50 ms.
- Outer frozen identity accepts PRE_READY_OFFER_FROZEN and
  POST_OFFER_READY_RETAINED without byte or sequence mutation.
- Drain has no post-loop chunk or room read; overflow and eof are sticky.
- The control table has 40 V16 rows. There are 17 semantic delta kinds.
  Terminal, refusal, and transfer timing arithmetic is unchanged.
- The exact six unresolved external gates remain unchanged and unresolved.

## 15. Author-stop boundary

The final whole-file identity is necessarily reported externally rather than
self-hashed. A whole-file self-hash would be cyclic. The final marker grants
no manifest, prebind, formal review, test, execution, or downstream authority.

BATCH07_P27_E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V16_AUTHOR_STOP
