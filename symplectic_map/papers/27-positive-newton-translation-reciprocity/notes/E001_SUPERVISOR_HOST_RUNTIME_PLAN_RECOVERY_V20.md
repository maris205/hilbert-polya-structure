# Paper 27 E001 supervisor host runtime plan recovery V20

Status: AUTHOR-STOP CANDIDATE ONLY; NO EXECUTION AUTHORITY

## 1. Authority and effect boundary

This document is the sole Runner V20 author artifact opened by authoritative event E0385. The opening ledger terminal is:

BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V19_DUAL_SUPERVISOR_PREBIND_FAIL_AND_RUNNER_V20_AUTHOR_OPEN_NO_EXECUTION

E0385 authorizes only construction of this exact fresh V20 plan file from the complete frozen V19 carrier. It does not authorize importing, tokenizing, parsing as a programming language, compiling, evaluating, launching, testing, validating, probing, building, retrying, consuming a reservation, creating evidence, changing a manifest, or changing any other file. The two embedded programs and embedded validator remain inert ASCII source text in this artifact.

The intended future operation is one no-build, one-shot Host V15 probe. This plan is not that operation. Every launcher, issuer, environment, kernel, filesystem, timing, external-owner, and reconciliation premise below must be independently established after author stop. Failure to establish any premise is a closed, no-execution result.

Author-stop is not a claim that the source is executable. No source in this file was imported, tokenized, language-parsed, compiled, evaluated, executed, launched, or microtested during authorship.

## 2. Frozen normative carriers

A future prebind review must authenticate all of these as held carriers, not as path names:

- E0366 snapshot: 2303269 bytes, 23672 LF, SHA256 0ea4f324c5175ec196b8118e551a429a6207cd57bacfdaa9903a109046daab92, with its exact unique terminal bound in both programs.
- Host Probe Recovery V15: 228310 bytes, 4622 LF, SHA256 a27eb1bb5540c18b57094ee26724be75a0c431b3c523385fe1271fb02378b845, final-LF ASCII, and its exact unique V15 author-stop terminal.
- Normative Host Probe V8 digest: 72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf.
- Frozen Runner V4 historical input: 248620 bytes, 3422 LF, SHA256 a11d80da1d5cffa2ac973cfe13d39340c587c87bbddaaa4d3d46640350e5ef83.
- Frozen complete Runner V19 baseline: dev 2431, ino 5916037043, mode 0644, nlink 1, uid 0, gid 0, 689599 bytes, 8469 LF, SHA256 17f6d4f3bed2a01d83ed3ae9f1b4466c060d06e3d6438085aa1ebb9f4d6073d6, with terminal BATCH07_P27_E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V19_AUTHOR_STOP.
- Frozen actor source below: 232821 bytes, 3123 LF, SHA256 c3fcb0e2b7e05b88178e74152b4abfb01de86642679796712c96978b0393296e.
- Frozen watchdog source below: 432198 bytes, 5426 LF, SHA256 37d93ca0c0a9fcb34d7f3f5010b741893b1b41aacec6950add7d57a4613b8843.
- Frozen embedded validator inside the actor source: 38275 bytes, 410 LF, SHA256 51462a4f424667121a9b571919cc4314d2bb3400585ec92af5a180c87a0ad0b3.
- Dedicated Python image: /root/miniconda3/bin/python3.12, exact certificate identity and SHA256 9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101.

Every anonymous input carrier is required to be a root-owned regular file with nlink zero, O_RDWR access, exact WRITE/GROW/SHRINK/SEAL seals, exact size, and exact SHA256. The frozen Host V15 is deliberately not such a carrier: actor fd 102 and watchdog fd 12 are duplicates of one linked, root-owned, nlink-one, O_RDONLY open description with the exact frozen dev/ino/mode/size/LF/SHA/terminal identity. No descriptor is ever checked under both contracts. Each side reads its own held carriers and recomputes identities. Actor assertions are not evidence for the watchdog.

## 3. Six unresolved external gates

All six gates remain unresolved by this author artifact. Their certificate PASS fields and nonzero gate identifiers are future issuer facts, not author claims:

1. CLONE3_CPYTHON: the exact CPython image and host must have a separately reviewed clone3/CLONE_INTO_CGROUP/CLONE_PIDFD construction premise.
2. DELETED_CGROUP_FD: held descriptors, cgroup.kill behavior, empty observation, and removal behavior after namespace unlink must have a separately reviewed kernel premise.
3. SEALED_SNAPSHOT_CONSTRUCTION: the exact E0366 snapshot must be constructed and sealed by an authorized procedure without evidence-root contact.
4. EXTERNAL_SURVIVAL: the external owner, endpoint, pidfd/starttime identity, SCM_RIGHTS transfer, and durable takeover protocol must be established before entry.
5. OUTER_RECONCILER: an independent durable reconciliation service must exist for uncertain terminal sends and actor loss.
6. ISSUER_CRYPTOGRAPHY: issuer key control, Ed25519 verification, serial allocation, expiry, reservation, signature, receipt, and replay prevention must be established.

Until all six are independently evidenced, current, mutually consistent, and formally accepted, this plan is non-executable. A literal PASS value in a hypothetical packet cannot substitute for the external evidence.

## 4. One-shot input and descriptor contract

The future outer launcher must begin from a clean absolute cwd, a fixed umask, the exact ENV map in both sources, no inherited signals or timers, no tracing/profile/audit hook, no concurrent mutator, no ambient authority, no writable workspace reachability, and no reachable build/evidence/root. It must use an empty stdin, independently drained stdout and stderr, an external pidfd, a prebound SOCK_SEQPACKET owner channel, and no shell.

Actor inherited descriptors are exactly:

- 0 empty read-only stdin; 1 stdout; 2 stderr.
- 100 sealed actor source.
- 101 sealed E0366 snapshot.
- 102 linked frozen O_RDONLY/nlink-one Host V15.
- 103 sealed complete V15 plan.
- 104 sealed certificate.
- 105 sealed final issuer envelope.
- 106 sealed watchdog source.
- 107 sealed reservation.
- 108 prebound external-owner control.
- 109 prebound external-owner pidfd.
- 110 sealed external-owner manifest.

Watchdog inherited descriptors are exactly:

- 0 an EOF stdin; 1 and 2 closed.
- 3 actor control SOCK_SEQPACKET; 4 actor pidfd.
- 5 attempt base; 6 cgroup base.
- 7 certificate; 8 final envelope; 9 E0366 snapshot; 10 V15 plan; 11 actor source; 12 linked frozen O_RDONLY/nlink-one Host V15; 13 reservation.
- 14 external-owner control; 15 external-owner pidfd; 16 external-owner manifest.
- 100 sealed watchdog source.

Any extra descriptor, wrong access mode, wrong owner/type/nlink/seal, wrong size/hash, nonempty stdin, wrong cwd, wrong environment, or carrier mismatch is a pre-action closed failure. Mutation-capable bases are individually owned and either closed or explicitly transferred; parent exceptions after fork retain and exactly reap or durably transfer watchdog ownership.

## 5. Acyclic issuer construction

The issuer construction is deliberately one-way and has no whole-hash fixed point.

1. Build the canonical detached envelope-context payload from the 15 ENVELOPE_CONTEXT_KEYS plus its exact end line. It excludes certificate bytes, certificate digest, every signature and signature-preimage hash, the issuer receipt, final-envelope digest, reservation bytes, and session AUTH. Its preimage is exactly `P27E001_V15_DETACHED_ENVELOPE_CONTEXT || NUL || ENVELOPE_CONTEXT_RAW=<decimal byte length> || LF || payload`; its SHA256 is ISSUER_CONTEXT_SHA256 in the certificate.
2. Construct the certificate once. It contains no later-object hash, signature, receipt, self-hash, final-envelope digest, reservation digest, or AUTH. CERTIFICATE_DIGEST_SHA256 is exactly SHA256 of `P27E001_V15_CERTIFICATE_DIGEST || NUL || CERTIFICATE_RAW=<decimal byte length> || LF || certificate bytes`.
3. Form the final-envelope TBS payload from the detached context plus ENVELOPE_CONTEXT_SHA256, CERTIFICATE_DIGEST_SHA256, SIGNATURE_ALGORITHM, and its exact end line. First wrap that payload as `P27E001_V15_ENVELOPE_TBS || NUL || ENVELOPE_TBS_RAW=<length> || LF || payload`. Then form the issuer-signature payload from separately length-framed CERTIFICATE_RAW and ENVELOPE_TBS plus its end line, and wrap the whole payload as `P27E001_V15_ISSUER_SIGNATURE_PREIMAGE || NUL || ISSUER_SIGNATURE_TBS_RAW=<length> || LF || payload`.
4. Append SIGNATURE_PREIMAGE_SHA256, SIGNATURE_ALGORITHM, and SIGNATURE_HEX. The issuer receipt is one `ISSUER_RECEIPT_TBS_RAW` length frame under the P27E001_V15_ISSUER_RECEIPT NUL domain and binds the exact context digest, certificate digest, signature-preimage digest, algorithm, signature, and end line. Append ISSUER_RECEIPT_SHA256. FINAL_ENVELOPE_DIGEST_SHA256 is exactly SHA256 of the P27E001_V15_FINAL_ENVELOPE NUL domain followed by one `FINAL_ENVELOPE_RAW` length frame containing every final-envelope byte.
5. Construct the ordered 10-field reservation payload from issuer identity/key/serial, certificate digest, final-envelope digest, validity interval, reserved=1, consumed=0, and Ed25519. Wrap it as one `RESERVATION_TBS_RAW` length frame under the P27E001_V15_RESERVATION_TBS NUL domain. The reservation signature and receipt each use their own NUL domain plus exactly one outer length frame; the signature payload contains the nested RESERVATION_TBS frame, and the receipt payload binds that TBS, signature-preimage hash, algorithm, signature, and exact end line. Only then append RESERVATION_DIGEST_SHA256.
6. Compute session AUTH only after all three immutable carriers exist. Its payload is the ordered concatenation of `CERTIFICATE_RAW`, `FINAL_ENVELOPE_RAW`, and `RESERVATION_RAW` length frames; AUTH is SHA256 of `P27E001_V15_SESSION_AUTH || NUL || AUTH_TBS_RAW=<payload length> || LF || payload`. Labels, decimal lengths, NUL domains, order, and end lines are part of the bytes and admit no implicit concatenation.

A later consumed/released state is a new monotone chained receipt. No carrier above is mutated. Both programs independently recompute the same domain/length preimages, exclusions, cross-carrier digests, signature-preimage digests, receipt digests, time fields, plan/source/V15/snapshot bindings, and reservation relations from held bytes. Actual issuer-signature validity remains a required external ISSUER_CRYPTOGRAPHY gate; this author artifact does not convert that unresolved gate into a local proof.

## 6. Entry identity and dependency closure

Both programs bind boot ID, platform identity, architecture, kernel release, exact mountinfo identities, filesystem types, base dev/ino/mode/nlink/uid/gid, safe-bind noexec and writable-descendant count, cgroup v2 magic and topology, controllers/subtree_control/type, runtime root, no-external-mutator premise, and access modes.

The watchdog independently holds and checks plan, both sources, V15, snapshot, certificate, envelope, reservation, manifest, attempt base, cgroup base, external owner, and its own image. It does not trust actor hashes. Python is accepted only when the executable identity equals the dedicated PYTHON_IMAGE dependency entry. LIBC identity includes path, dev, ino, mode, nlink, uid, gid, size, hash, and confstr relation. All singleton dependencies, gates, credentials, and graph edges are cardinality-checked.

The actor and watchdog bind pidfd fdinfo PID to the same PID, bind stable /proc stat field 22 starttime by repeated observation, bind stopped state from /proc status, and bind exact cgroup membership. PID alone is never an identity and cannot authorize action after reuse.

## 7. Clock and deadline discipline

The certificate binds realtime and monotonic clocks with at most 1000000 ns drift and a 360000000000 ns lifetime. Every certified boundary performs pre/post clock, expiry, actor-state, control-state, and relevant containment checks. CLOCK_DRIFT, CERTIFICATE_EXPIRED, DEADLINE_EXPIRED, CONTROL_LOST, SEND_EFFECT_UNKNOWN, and PIDFD_ACTOR_LOST remain distinct causal faults.

All caps are cumulative absolute phase deadlines derived from one origin. No retry, helper restart, borrowing, or deadline restart is permitted. Every effect uses the minimum inherited bound while preserving the precomputed remaining tail.

Normal release uses one origin and fixed absolute offsets: durable release record by origin+800000000 ns and reply by origin+900000000 ns inside the 1000000000 ns launch cap.

At first failure the watchdog freezes one immutable overall deadline at origin+5210000000 ns and an earlier cleanup-effect deadline at origin+2600000000 ns. The remaining 2610000000 ns is reserved for the 100000000 ns recovery record and the complete 2510000000 ns terminal chain. No cleanup effect or retained/late-empty record begins after its cap.

The terminal chain has one common absolute deadline and these 13 cumulative phase ceilings, in order: candidate record 100 ms, notice 100 ms, terminal-seen record 100 ms, report record 1000 ms, PASS commit 100 ms, PASS margin 10 ms, ACK 500 ms, actor ACK receipt 100 ms, ACK-receipt record 100 ms, reconciliation record 100 ms, owner-closure record 100 ms, closure packet 100 ms, watchdog exit 100 ms. Total: 2510 ms. The host-complete-to-ACK bound is independently enforced at no more than 500 ms where applicable.

Refusal has one 210 ms cumulative schedule. Its authoritative-finality deadline is origin+80 ms after 20 ms record, 20 ms ACK, 30 ms receipt-wait, and 10 ms finality-commit phases. Its distinct closure deadline is origin+210 ms, leaving a certified positive 130 ms nonborrowable tail partitioned into 10/20/30/20/10/20/10/10 ms offer-build, one-send, acceptance-receive, acceptance-verify, acceptance-commit, actor-closure, capability-close, and owner-release phases. The consumption cap is 250 ms so post-ARM refusal retains the complete 210 ms schedule after its fixed 40 ms prefix.

## 8. Control language and state machine

There is one control-envelope language, one frozen 40-row transition table, and no broad or wildcard state map. Each packet has exactly one final LF, printable ASCII only, a size cap, canonical field order, no duplicate/reserved extension, and an authenticated digest. Common fields bind protocol version, session AUTH, direction, transaction sequence, transition ID, sender state, required receiver state, current ordinal, current probe, effect state, and the exact phase deadline.

Every recvmsg installs each kernel-created descriptor immediately into a bounded preallocated typed quarantine record before framing or semantic validation. Malformed ancillary bytes, excess rights, wrong counts or types, truncation, packet rejection, and exceptions proved-close or retain every quarantined descriptor; validated rights promote in place to their preallocated semantic records. Wrong control bytes, sequence, sender, receiver state, slot, probe, effect, deadline, or packet digest is CONTROL_MALFORMED before action. CONTROL_LOST is only channel state. SEND_EFFECT_UNKNOWN is only send state. PIDFD_ACTOR_LOST is only actor state and can be established only from fd 4 readiness. POLLIN is drained before HUP/ERR classification. Control loss never proves actor loss and never satisfies owner-release predicates.

## 9. Refusal and consumption edge

Before every BEGIN send, the actor irreversibly records BEGIN_SEND_EFFECT_UNKNOWN. Before every ARMED send, the watchdog irreversibly records ARM_SEND_EFFECT_UNKNOWN and armed_possible. Any unproved send outcome remains effect-unknown.

There are exactly two no-consume cross-map rows:

- BEGIN_NOT_ENTERED plus ARM_NOT_OBSERVED maps only to ARM_NOT_ENTERED.
- BEGIN_SENT plus ARMED_CONFIRMED maps only to REFUSAL_CLOSED_NO_CONSUME.

A refusal request is fully parsed and semantically checked while the dedicated refusal slot remains unlocked; rejection records REJECTED_UNLOCKED_NONCONSUMING, returns on its explicit non-consuming branch, and performs no refusal close, ACK construction, refusal-slot allocation, or reservation consumption. If BEGIN was already observed, ordinary unlocked owner-transfer rules still retain or transfer that pre-existing ownership. After validation and before any fallible close, ACK construction, ACK possible effect, receipt wait, or receipt parsing, the watchdog installs one non-null staged immutable slot and then locks out the generic transfer path. Its invariant is refusal_slot_locked implies refusal_offer_cache is non-null.

That one slot permanently binds the external sequence and predecessor, exact request bytes and digest, request message sequence, cross-map facts, the complete refusal schedule, the absolute refusal_finality_deadline, and the strictly later absolute refusal_closure_deadline. The request, staged core, ACK, actor receipt, one-off offer, issuer contract, acceptance, durable receipt, and actor-closure packet all bind both values and the exact schedule. While its close state is still CLOSE_NOT_ATTEMPTED, the watchdog constructs and reserves the exact ACK, atomically installs its bytes and sequence as ACK_CACHED_PRE_CLOSE, and only then may enter CLOSE_EFFECT_UNKNOWN or call close_no_consume. ACK construction or reservation failure therefore leaves the same locked slot in the exact ACK_NOT_CONSTRUCTED/CLOSE_NOT_ATTEMPTED state; no ACK identity is invented. ACK activation and its first possible send occur only after CLOSED_NO_CONSUME is known. The later monotone variants distinguish ACK_READY_CLOSED, ACK_EFFECT_UNKNOWN, WAITING_RECEIPT, RECEIPT_VERIFIED, ACTOR_LOSS_DRAINED, and FINALITY_CAP_EXPIRED_HOLD without allocating a successor.

Each actor-receipt candidate is received into temporary state and completely checked for envelope, expected sequence, exact ACK and request hashes, cross-map, both absolute deadlines, schedule, certificate liveness, and receipt-state facts before either authoritative field changes. Fresh finality-deadline checkpoints occur after recvmsg, after parse, and immediately before the atomic receipt-plus-sequence commit. Rejected candidates affect only a separate bounded fault-evidence digest: they never become authoritative receipt bytes and never advance CONTROL_RECV_SEQ, so a later exact candidate remains admissible. At or after the finality cap, packets can add only bounded non-authoritative evidence; they cannot mutate receipt bytes, sequence, finality, or offer eligibility. Close or packet construction failure, ACK uncertainty, receipt timeout or malformed bytes, StaticReject, certificate/issuer failure, actor or control loss, closure-send uncertainty, and every late exact receipt remain on the same dedicated slot; OWNER_POLL never routes them through generic transfer.

No refusal offer exists while a late actor receipt is still possible. Until refusal_finality_deadline the watchdog multiplexes actor control with the actor pidfd, drains readable control before HUP/ERR, and can finalize only an exact fully validated receipt or pidfd-proved actor loss plus fully drained actor-control EOF. A cap race that cannot commit by that deadline enters FINALITY_CAP_EXPIRED_HOLD or the explicit no-authoritative-mutation equivalent, retains ownership, and permits neither offer nor release. Only then may closure-tail work start, and each stage has an explicit latest-safe-start ceiling plus exact reserve-after value. Offer construction is temporary until a fresh pre-install checkpoint; the single possible send is never retried. Receipt carrier read, envelope parse, signature verification, pidfd/starttime verification, external-receipt commit, actor closure, each capability close, and owner release have fresh phase checkpoints. If a possibly effective offer cannot be fully verified and committed, immutable ACCEPTANCE_EFFECT_UNKNOWN_HOLD preserves the frozen slot, all local capabilities, no resend, and no owner release. Generic rights transfer uses the same build/send/receive/verify/commit/close/release discipline. The frozen refusal slot never mutates behind an offer, and release occurs only after durable cryptographic acceptance, the reserved actor-closure phase, local capability closure, and a final owner-release checkpoint.

All other BEGIN/ARM/control loss combinations become CONSUME_EDGE_UNKNOWN. One actor-derived consumption deadline is carried unchanged through BEGIN, ARM, COMMIT, mkdir, open, verify, publish, fsync, intent, and ACK. No helper restart or replay is allowed.

## 10. Attempt and recovered-stage publication

Attempt publication is verify-before-publish. A local descriptor progresses LOCAL_UNVERIFIED to LOCAL_VERIFIED to PUBLISHED only after fstat, named-entry, base identity, owner, mode, nlink, access, collision, and durability checks. A collision namespace retains no mutation-capable base; it can report only through a separately certified independent base/control and, if ownership cannot close, the exact external transfer protocol.

Recovered-stage handling keeps the stage descriptor, named-entry descriptor, base descriptor, identities, and all four leaf descriptors local until all named-entry/base/access checks and all four exact leaf size/LF/SHA identities pass. Only then can the immutable stage capability be published. Any failure closes locals and reports ABSENT_KNOWN or UNKNOWN as justified; it never reports retained=1.

The runtime root and safe bind are checked independently at every relevant boundary. No source path is read after sealing. No build step exists.

## 11. Containment, release, and probe topology

The watchdog owns cgroup and payload lifetime. cgroup descriptors for type, controllers, subtree_control, events, kill, and root are immediately registered in exhaustive cleanup scopes. The long-lived root cgroup.events and cgroup.kill descriptors are distinct ROOT_EVENTS_FD and ROOT_KILL_FD ownership capabilities: whenever live they occur in the canonical external-right order, and every accepted or direct terminal closure closes each local descriptor, writes its slot to -1, and rechecks the exhaustive ownership set before logical release. Containment is not considered bound until exact identity, access, cgroup topology, singleton population, pidfd/starttime, stopped state, and actor/control acknowledgements agree.

The suite is exactly 15 slots in this order:

P00, P01D, P01C, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12, P13

P00 reconstructs its synthetic transcript bytes exactly before checking SHA256. P01D yields exactly 13 fields and P01C receives the exact relation, including index 9. P05 uses pidfd plus stable starttime and rejects PID reuse. Topology claims are limited to complete transcript observations and do not claim unobserved global process ancestry.

For each slot, stream rights and pidfd rights enter exhaustive local owner scopes immediately and transfer individually only at commit. Actor PID/starttime and each outer PID/starttime are cached as immutable provenance while their exact pidfds are known not ready. Actor-pidfd readiness directly establishes actor loss without any later positive fdinfo PID or live /proc lookup. Release requires the durable release record, exact packet binding, cgroup membership, stopped observation, cached pidfd/starttime relation, and boundary checks before and after SIGCONT. The release record and reply use the one carried origin; release cannot be retried.

## 12. Transcript and result discipline

stdout and stderr are independently nonblocking-drained until exact EOF while the watchdog monitors actor pidfd, payload pidfd, control, cgroup events, and absolute deadlines. stdout is capped at 3145728 bytes; overflow is terminal. stderr must be empty and at EOF. No wait status, transcript, or topology result is accepted from a partial stream.

The transcript validator has three disjoint stages:

1. Byte language: exact ASCII/control-byte, LF, size, and terminal framing.
2. Structural grammar: exact line and field cardinality, canonical decimal/hex forms, slot order, packet boundaries, and complete consumption.
3. Semantics: exact probe relations, P00 reconstruction, P01D to P01C relation, P05 identity, candidate claims, and cross-slot constraints.

The RESULT protocol is complete and framed: exact RESULT notice, bounded frame sequence, exact final frame cardinality and digest, RESULT_END, and independent watchdog reconstruction. SCM_RIGHTS packets bind the exact packet digest, rights manifest, local fstat/access facts, pidfd PID/starttime, cgroup facts, and current slot/deadline. Every local descriptor is closed on every reject path.

## 13. Durable records and report union

Every durable record is created O_EXCL, written completely, fsynced, closed, reopened without following symlinks, byte-verified, and directory-fsynced within its phase deadline. Before freezing any reservation, B constructs an anonymous expected-raw carrier, writes it completely, applies the exact seals, rereads it, and verifies exact bytes and digest. Carrier failure closes the anonymous fd and clears the draft as a typed non-pending pre-effect result; no O_EXCL is then reachable. Only after carrier verification does B immutably bind sequence, predecessor, exact entry name, raw digest, and one typed idempotent semantic delta and close the successor gate before the first possibly effective O_EXCL. While that reservation is pending, every recovery, terminal, or other chain allocation is rejected, and the verified carrier supplies the exact authenticated external fallback. After named-byte and directory-fsync verification, both the nominal path and reconciliation apply that same delta before marking the record durable or clearing the gate; a post-directory-fsync delta fault therefore remains `DIR_FSYNC_VERIFIED_DELTA_PENDING` with the original carrier and reservation. The COMMITTED delta restores the exact slot bit, direct-reap count, committed-record and packet hashes, packet message sequence, and `COMMITTED_SEND_EFFECT_UNKNOWN`; only the later COMMITTED_SEEN delta may claim actor observation. Reconciliation never allocates a successor to explain uncertainty. durable_once carries partial state, digest, typed causal fault, and effect state. Each chain member has RECORD_SEQ and PREDECESSOR_SHA256.

The chain covers intent, release, validated result, ACK-commit intent, COMMITTED, COMMITTED_SEEN, terminal candidate, terminal seen, report, PASS when eligible, ACK receipt/no-replay, reconciliation, and OWNER_CLOSURE. Success and failure use the same monotone terminal-seen through owner-closure discipline. Volatile OWNER_CLOSED is sent only after durable closure.

The 34-field final report is a discriminated union. OUTCOME_KIND determines exact applicability of attempt, stage, containment, empty, removal, kill, stop-probe, reap, ACK, reconciliation, closure, failure-origin, cleanup deadline, terminal deadline, and disposition fields. NOT_APPLICABLE is distinct from empty or absent. B first derives every field from the live constructor state, assembles the complete final bytes with the prospective sequence and predecessor without allocating a draft, and runs the same exhaustive parse_final_report/validate_report_union path used for reread acceptance. Only successful prevalidation may create the draft and enter durable_once; the post-write parse is an equality recheck and adds no acceptance condition. Every constructible final report represents a consumed, durable, published attempt. BOUND additionally requires the reachable verified stage state, its retained identity, and the actual consumed/published attempt state; field tuples that cannot be produced from those live facts are rejected. It enforces:

0 <= COMMITTED_COUNT <= REAPED_COUNT <= STOPPED_COUNT <= ENTERED_COUNT <= 15

STOP_ORDINAL and STOP_PROBE have one exact relation to the suite. Absent containment is not empty. A no-payload path may use ABSENT_KNOWN only with the corresponding zero counts and no-release facts. Candidate claims must match literal RESULT/transcript fields and the complete B-held record chain.

PASS is eligible only after the exact success report and durable PASS record within the pass margin. PASS or ACK send-effect unknown is sticky and cannot be downgraded to a conflicting ABORT. A missing ACK never authorizes replay; it requires durable reconciliation and owner closure.

## 14. Cleanup, kill, and terminal ownership

Both spans preallocate fixed typed lifecycle records before fd-producing work. A producer first marks its reserved record ACQUIRING, stores the returned raw number in that same record before identity, validation, journaling, or other fallible work, and either finishes adoption or strictly reconciles that exact number. Promotion is an in-place preallocated alias swap; proved-close state is authoritative before optional audit journaling; each retry revalidates the stored identity and global live-fd-number uniqueness. On possible payload release, the first failure consumes the sole safe ROOT_KILL_FD authority even when an instantaneous population observation is empty. The actor never opens or transfers cgroup.kill. The kill ticket, watchdog cgroup.kill call, return, and postcheck all fit within one inherited cleanup cap with resampled clocks. There is at most one kill ticket and one kill call; no retry exists.

The watchdog runs one terminal_owner_loop. It continuously polls actor pidfd, actor control, containment, and pending terminal packets; drains POLLIN before HUP; and retains every owner descriptor through success, failure, send uncertainty, control loss, and actor loss. Every one of the four logical owner-release assignments follows real exhaustive local capability closure, including both root descriptors, both nontransferable lifecycle pidfds, every carrier, and both control endpoints; the generic finally only asserts the already-monotone exhaustive predicate and never establishes ownership release.

The loop exits only through one of these exact predicates:

- complete durable terminal-seen, report, PASS if applicable, ACK, actor receipt, no-replay reconciliation, OWNER_CLOSURE, closure packet, safe containment, and watchdog exit handshake;
- pidfd-proved actor loss plus durable outcome, safe containment, durable no-replay ACK-receipt/reconciliation/OWNER_CLOSURE chain; or
- the frozen external transfer protocol below.

Post-deadline observation is outside certified effects. It cannot create a record, issue kill, accept PASS, infer empty, or release ownership. It can terminate only through a real prebound external transfer.

## 15. External owner transfer

External transfer is not a Boolean escape hatch. Before entry, the certificate binds an independently alive owner PID, stable starttime, uid/gid, pidfd, SOCK_SEQPACKET endpoint, manifest size/hash, maximum packet, rights types, signature policy, and monotone receipt service.

A transfer offer derives its exact transferable set from every live registry record marked transferable, sorts by the canonical 13-kind order, rejects duplicate kinds, slots, or numbers, and compares the byte-exact registry set at freeze, immediately before the one possible send, and again at acceptance. It binds AUTH, sequence, predecessor, reason, current terminal subject, chain head, outcome durability, actor/control/send states, attempt/collision/base-closed/commit/intent facts, exact rights count, the sole ROOT_KILL_FD authority, and each fstat/access identity. If a record remains pending, the offer additionally binds its exact sequence, predecessor, entry name, expected byte length, expected raw SHA256, and the complete length-framed typed semantic delta with its SHA256; the expected raw bytes travel only in an anonymous O_RDWR, nlink-zero, exactly sealed carrier whose identity also binds the delta digest. Actor pidfd and external-owner pidfd are typed nontransferable lifecycle slots and are closed locally before release. Each live root capability is mandatory in the offer. Each local right remains owned until exact ACCEPTED.

Outer pidfd transfer has exactly two offer-freeze states. Its PID/starttime provenance is authenticated and cached before readiness. Offer material is tentative until a final zero-time combined actor/outer readiness snapshot; no fallible, blocking, allocating, or identity-building operation occurs between an unchanged snapshot and immutable cache assignment. A changed snapshot discards the unactivated candidate without sequence consumption, applies the cached-provenance post-ready close/omit transition, and rebuilds monotonically. Once readiness is observed, no new fdinfo PID or live /proc lookup is permitted: before offer freeze the watchdog proved-closes and omits the local outer pidfd and binds cached PID/starttime, exit-ready state, and the exact durable release-record digest/ordinal/probe. Acceptance echoes this state, the external-owner cached provenance, and the OUTER_PIDFD-right-present bit, and safely promotes readiness first observed after cache installation without mutating or resending the frozen offer.

Acceptance must bind the offer SHA256, exact sequence and predecessor, durable receipt SHA256, issuer signature, no-replay flag, receiver PID/starttime, independently sealed receipt carrier, cached actor/external-owner/outer provenance and snapshot fields, release-record identity, sole-kill identity, and the byte-exact dynamic registry set. COMMITTED is immutable. Before the first irreversible local close, all nonownership checks complete and one immutable close plan plus cursor is installed. Accepted and direct closure resume that same cursor through every exception; no later deadline, offer, resend, sequence change, generic fallback, or state downgrade may abandon it. Non-endpoints close first and the ownership endpoints are the final journaled phase. Each slot becomes closed only after close return or immediate same-fd EBADF reconciliation; a live matching identity remains registered and retryable, and mismatch or unclassified effect is a retained HOLD. Exhaustive proved closure permits owner release even if later nonownership reporting fails.

The dedicated refusal slot, not an external offer, is installed before the first post-validation fallible action. REFUSAL_CLOSE_OFFER remains nonexistent until the same slot reaches exact receipt finality or pidfd-loss/control-EOF finality. The receipt-final branch also requires known CLOSED_NO_CONSUME with a cached ACK; the loss/EOF branch retains the exact earlier ACK/close variant without fabrication. Its immutable contract covers the sequence, predecessor, exact request, close state, schedule, deadline, ACK bytes and sequence (including exact empty/zero), final authoritative receipt state, finality evidence, and final slot digest. Fallible contract and offer construction may be repeated only while no offer exists and always reserve the same external sequence; once exact offer bytes are frozen neither slot nor offer can change. The possible-send flag is set before activating that reserved packet, so there is at most one possible external send and never a resend. All post-lock recovery, including late actor receipt capture, remains on this slot; OWNER_POLL cannot consume it as an unrelated packet, generic TRANSFER_OFFER is unreachable, and external acceptance rechecks finality before release.

Collision uses the same exact transfer machinery or a separately durable independent receipt; there is no dead collision grammar. Refusal uses a dedicated durable issuer receipt and closure chain. Actor-loss also produces durable no-replay reconciliation and OWNER_CLOSURE. There is no replay after any uncertain effect.

## 16. Outer launcher obligations

The embedded sources cannot establish their own initial authority. A future outer launcher must, before any source interpretation:

- obtain explicit ledger authority naming this exact final V20 control identity and its frozen V19 and V15 carrier baselines;
- verify author-stop, both separated formal reviews, all six gates, issuer key/serial/expiry, and one-shot reservation freshness;
- construct every sealed carrier without path substitution and authenticate every fd;
- establish clean argv, env, cwd, umask, signal, timer, FD, namespace, mount, cgroup, and no-mutator state;
- start a new process group/session or stronger containment that covers all descendants;
- retain pidfds/cgroup kill and external-owner capabilities, independently drain both output streams, and use one absolute watchdog deadline;
- distinguish pre-send, send-effect-unknown, consumed, terminal, reconciled, and owner-closed states;
- never kill only the top process, truncate output, infer timeout from missing text, retry after uncertain effect, or touch any build/evidence/root.

These are outer-launcher obligations, not intrinsic V20 guarantees. Intrinsic V20 guarantees are limited to the complete V19 carrier, the retained V15 wire protocol, and the reachable E0385 transition corrections frozen in the two source spans under their stated inputs. Containment, carrier creation, issuer authority, clean entry, durable records, deadlines, drainage, descendant cleanup, reconciliation, and no replay are supplied by this Runner protocol and its future launcher.

## 17. Review separation and manifest eligibility

After this author stop, two fresh separated supervisor-prebind reviews must independently check source/constructibility and lifecycle/ownership, including exact bytes, line counts, hashes, delimiters, source/prose agreement, certificate constructibility, unresolved gates, and the no-execution boundary. Their prospective combined ledger outcomes are:

- pass/open: BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V20_DUAL_SUPERVISOR_PREBIND_PASS_AND_FORMAL_REVIEW_OPEN_NO_EXECUTION
- fail/closed: BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V20_DUAL_SUPERVISOR_PREBIND_FAIL_NO_EXECUTION

Only a dual prebind pass may open two separated formal scopes, performed by fresh reviewers not involved in V20 authorship or prebind and not involved in failed V19 authorship or reviews:

- Source/certificate/parser formal scope: extraction and seals; one-way issuer construction; certificate/envelope/reservation/AUTH; fd and ancillary grammar; P00/P01D/P01C/P05; RESULT; complete transcript; report/candidate/source/prose census.
- Lifecycle/containment/durability formal scope: fork ownership; control/actor/send orthogonality; refusal; carried consumption/release horizons; cgroup and pidfd/starttime; cleanup and one-kill lane; all absolute schedules; terminal owner loop; reconciliation; external transfer; no replay.

The two reports must be separately sealed and cannot substitute for each other. The prospective combined ledger outcomes are:

- pass/closed: BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V20_DUAL_FORMAL_REVIEW_PASS_NO_EXECUTION
- fail/closed: BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V20_DUAL_FORMAL_REVIEW_FAIL_NO_EXECUTION

Even a dual pass grants no execution. Manifest eligibility remains false until the exact final V20 identity, both prebind passes, both formal passes, all six current gate receipts, issuer materials, external owner, outer reconciler, and a later explicit immutable ledger event independently grant manifest binding and execution. V13 through V19 remain immutable nonmanifest failure history. No event in this file can self-authorize that transition.

## 18. Embedded source boundaries

The next outer span is the frozen actor source. It contains the frozen validator as an inner raw span. The later outer span is the frozen watchdog source. Exact boundary lines and source census are recorded after both spans. The bytes between boundaries are inert raw text.

### 18A. V20 correction authority and completeness rule

Sections 2 through 17 preserve the complete V19 carrier, complete V15 protocol,
and frozen carrier contract. V20 changes no V15 wire tag, carrier manifest version, issuer domain,
certificate field, envelope field, reservation field, session-AUTH construction,
control transition, durable-record grammar, report union, or terminal-owner
ordering. The V15 actor and watchdog programs below remain the completeness
baseline. Their later V19 and V20 definitions intentionally shadow only descriptor
acquisition, receive quarantine, promotion, poller, wrapper, offer census,
readiness, acceptance, kill-census, stream-drain, and ownership-closure
mechanics. Every concrete V15 bootstrap, 40-row handshake, refusal, ACK,
generic transfer, one-kill, 17-delta durability, O_EXCL carrier-before-
reservation, reconciliation, report-union, transcript, and terminal path is
retained. A V20 override is valid only when it has a reachable call from the
preserved main path and every name it calls has a compatible definition.

The exact six and only six unresolved external gates remain CLONE3_CPYTHON,
DELETED_CGROUP_FD, SEALED_SNAPSHOT_CONSTRUCTION, EXTERNAL_SURVIVAL,
OUTER_RECONCILER, and ISSUER_CRYPTOGRAPHY. The retained small-descriptor proof is a
mandatory conjunct of CLONE3_CPYTHON, not a seventh gate: the immutable
launcher-entry pair 1048576/1048576 is captured first and soft RLIMIT_NOFILE
is lowered once to current 256/1048576 immediately before bootstrap. Every
descriptor target and successful result is in 0 through 255. Explicit
simultaneous-role sets derive actor high-water 211+5+3=219 and watchdog
high-water 97+14+1=112, both below 256; the frozen CPython image supplies
cached scalar objects for 0 through 255 and statically nonfailing preallocated
ctypes result stores under that same gate.

### 18B. One physical-record authority and producer boundary

Each side preallocates one fixed PhysicalRecord for every record_id. Its only
physical states are CLOSED, ACQUIRING, OWNED, and CLOSE_RETRY. A record carries
one raw_fd, immutable record_id and provenance origin, mutable semantic_role,
full physical identity (dev, ino, mode, nlink, uid, gid, access), separately
verified kill-leaf identity, actual access, endpoint phase, and wrapper strong
reference. Generic identity revalidation never overwrites kill-leaf identity.
There is no owns bit and no independent EndpointCell
ownership authority. ACQUIRING with a nonnegative raw_fd is live. CLOSED is the
only proof that a physical descriptor is absent.

Every scalar open, dup, F_DUPFD_CLOEXEC, dup2, memfd, pidfd_open, inherited
descriptor, pipe2 pair, socketpair pair, clone3 pidfd, and recvmsg producer is
prearmed with a fixed RawCell before the producing boundary. Scalar boundaries
write their result directly into that cell. pipe2 and socketpair write two
preallocated C integer cells. clone3 writes its pidfd into a preallocated C
integer cell whose PhysicalRecord is already ACQUIRING. A protected finally
rescans every output cell: each nonnegative value is adopted by its already
reserved record or remains CLOSE_RETRY, and ACQUIRING/-1 repairs to CLOSED.
Pair outputs are independently adopted and independently reconciled. No
post-syscall statement can erase or precede the retained output cell.

Wrapper construction begins after raw adoption but inside the same protected
primitive. The already-owning record receives the first strong reference.
Constructor, fileno, binding, detach, and bookkeeping failures enter nested
repair. DETACH_REQUESTED is monotone; fileno==-1 proves a completed detach and
repairs DETACHED from the recorded raw number without a second detach.
Destructor behavior is never ownership or close evidence.

### 18C. Five fixed receive sites and deferred semantics

There are exactly five reachable libc recvmsg site wrappers. Their visible
installed-right cell counts are actor-control 5, watchdog monitored-control 5,
external-control 14, external-receipt 14, and refusal-control 5. The semantic
caps are respectively 4, 4, 13, 13, and 4, with one overflow-visible cell.
Each frame owns a fixed payload buffer, msghdr, iovec, ancillary buffer of at
least installed_capacity*CMSG_SPACE(sizeof(int)), fixed RawCells, fixed
quarantine record_ids, count/flags/result cells, and one capture epoch.
MSG_CMSG_CLOEXEC is mandatory.

One exception-total primitive prearms the frame, invokes libc recvmsg, and as
its first return action scans the retained msghdr/control buffer into the fixed
raw and quarantine cells. Its finally rescans authoritative retained control
bytes from offset zero, resynchronizes after malformed headers, and captures
every complete visible right. Rejection cleanup retains a frame cursor, visits
every record even when an earlier close is retryable, and completes before
frame reuse or receive-loop continuation;
MSG_TRUNC, MSG_CTRUNC, malformed CMSG, count overflow, framing failure,
deadline failure, or caller failure cannot abandon a later cell.

Every received right remains semantic_role=QUARANTINE through packet framing,
deadline, count/order, identity, type, access, inode, cgroup, stream, and
provenance validation. Only then does the same PhysicalRecord promote in
place. The exact caller map is stream_arm to OUT_FD/ERR_FD/EVENTS_FD,
pidfd_arm to OUTER_PIDFD, stage_bind to STAGE_DIRFD, and containment_bind to
CGROUP_DIRFD. The external receipt carrier is temporary, enters quarantine
before exactly one immediate post-quarantine deadline checkpoint and before
payload copying, flag/count validation, carrier inspection, local-history
mutation, or parsing. It is then included in local carrier history and closed
without permanent promotion; fresh later verification and precommit checks
remain.

### 18D. Promotion, pollers, close, and sticky streams

Promotion revalidates the same record_id, raw_fd, full identity, leaf identity,
actual access, and global uniqueness, then performs one semantic_role write in
place. It allocates no destination record, journal entry, collection, cache,
or poller object. PollerCell states are FREE, REGISTERING, ACTIVE,
UNREGISTER_RETRY, and INACTIVE and identify only record_id. REGISTERING is set
only after poller, record_id, raw_fd, and mask metadata are installed, and
immediately before the registration effect. Any effect-unknown path
unregisters or retains UNREGISTER_RETRY. Every event mask passes through pidfd_ready_event and
POLLNVAL is a fault.

Physical close enters CLOSE_RETRY before identity, poller, endpoint, wrapper,
or close work. It exhaustively reconciles every poller naming record_id,
performs the monotone wrapper detach repair, and treats EBADF only after same-
record identity and endpoint reconciliation. Optional journal/cache repair is
after CLOSED and cannot revoke it.

Each output stream has one preallocated StreamCell with fixed buffer, cap,
used, scratch, sticky overflow, and sticky eof. room is computed only after a
successful nonempty read. EAGAIN and EOF return directly, never inspect stale
chunk or room values, and EOF cannot clear an earlier overflow.

### 18E. Exhaustive offer and kill proof

The watchdog domain is exactly 97 PhysicalRecords. The generic partition is
exactly 13 offered permanent records, 12 unconditional safe-local records, and
72 blocking records. Offered records are attempt, attempt_base_fd, stage_fd,
cgfd, root_events_fd, root_kill_fd, out_fd, err_fd, events_fd, outer_pidfd,
cgroup_base_fd, actor_control_fd, and pending_expected_raw_fd. Safe-local
records are transfer_control_fd, actor_pidfd_fd, external_owner_pidfd_fd, and
the certificate, envelope, snapshot, plan, actor-source, host-source,
reservation, external-manifest, and watchdog-source carriers. Every other
fixed record is blocking. Refusal has one separately guarded actor-control
case with exactly zero offered rights; it does not alter the 13/12/72 generic
partition.

Preallocated Census objects and a distinct OfferCache storage object use
EMPTY, nonauthoritative CENSUS_PREPARED, and authoritative FROZEN states with
an epoch. Census preparation does not advance the boundary. Manifest,
payload, packet bytes, digest, reserved sequence, record-id sets, epoch, and
boundary one are assembled off-side and installed by one immutable FROZEN
authority assignment. A preassignment fault discards preparation without
sequence consumption; a postassignment fault restores mirrors from that
authority and resumes only PRE_SEND or acceptance with no resend. Freeze,
immediately pre-send, and acceptance compare exact record-id sets, epochs,
identities, actual accesses, and digests. ACQUIRING, LOCAL_RAW, quarantine,
unknown identity/access, CLOSE_RETRY, duplicate record_id, stale cache, or any
live blocking record rejects both generic and refusal release. Authenticated
receiver evidence separately binds installed history, current-retained rights,
receiver kill census, outer disposition, and four domain-separated digests.
It is never synthesized from watchdog-local receipt-carrier history and is
compared with the frozen offered and full-live sender censuses. A received-
then-closed outer pidfd remains in installed history but not current-retained
state.

Leaf identity and actual access are bound at adoption and revalidated at ARM,
kill, freeze, pre-send, acceptance, close, and post-release. Unique kill scans
every live PhysicalRecord rather than semantic labels. Unknown values block.
When containment failure requires kill, exact cardinality one is mandatory,
one durable ticket precedes exactly one cgroup.kill write call, retry is
forbidden, and post-release local writable-kill cardinality is exactly zero.
Legitimate ticket-durability, deadline, unavailable-call, and retained-tail
outcomes before call-possible preserve zero calls; cardinality one is required
only once the call boundary has become possible.

### 18F. Frozen outer identity, atomic acceptance, and no-return close

Freeze, pre-send, and acceptance invoke a live comparator over the same
record_id, raw_fd, full identity, leaf identity, actual access, and frozen
serialized bytes. Outer readiness is polled in every relevant wait. Before
freeze, readiness omits and rebuilds the candidate. After freeze,
PRE_READY_OFFER_FROZEN changes only to POST_OFFER_READY_RETAINED: offer bytes,
registry identity, sequence, predecessor, and possible-send state do not
change and no resend is reachable. Acceptance prepares exhaustive installed
history, current-retained set, kill census, and retained-versus-received-then-
closed disposition before one immutable candidate is prepared off-side. The
actual offered outer pidfd and external-owner pidfd are both registered in
receipt waits and the final readiness snapshot. One COMMITTED authority
assignment atomically binds that candidate and final snapshot; sequence and
generic/refusal mirrors derive from it without changing frozen offer bytes.

One reentrant ClosureCell is the sole aggregate authority. Its phases are
NOT_STARTED, ACTIVE, CLOSED, and RELEASED; modes are GENERIC_ACCEPTED,
REFUSAL_ACCEPTED, and DIRECT. It holds one immutable mode-specific commit
predicate, fixed close plan, cursor, current record_id, retry delay, and timing
overrun observation. Every fallible lookup, identity check, poller repair,
wrapper repair, close, journal mirror, invariant, and handoff fault remains in
one no-return driver. Retry waits are positive and bounded from 10 through 50
ms. ACTIVE and CLOSED reentry resume the same cell. Once ACTIVE, only the already-bound refusal preclose deadline checkpoint and sole latched send may occur; no offer build, receive, resend, caller return, main return,
state downgrade, or alternate release path is reachable. The only process
termination is the RELEASED handoff performed inside the same catch-all loop.
Safety continues even when the earlier timely tail can no longer be certified.
Before that handoff, the CLOSED invariant requires all records CLOSED, all
RawCells EMPTY or DISARMED, all pollers FREE or INACTIVE, all wrappers
NO_WRAPPER or PROVED_CLOSED, completed receive cleanup cursors, and zero local
writable-kill rights. Every caller tail-enters the driver; close_probe may
return only while the cell is still NOT_STARTED.

V12 finality remains OPEN-only with bounded positive polling, actor mark
ordering, RefusalFinalityPending routing, recovery resampling, 80 ms finality,
and a nonborrowable 130 ms closure tail totaling 210 ms. Generic transfer
remains 240 ms and terminal order remains 2510 ms. ACK-before-close,
no-consume close uncertainty, nonpoison receipt, actor-loss plus drained EOF,
one-send immutable offers, unresolved holds, sticky PASS, durable terminal
ordering, and no replay remain unchanged.
### 18G. V20 final-entry correction closure

V20 retains the complete V19 carrier and changes only E0385 U01, U03, U04, U05, and M01. Actor and watchdog acquisition enter their catch-all boundary before reset, prearm, raw-cell, or record mutation; a partial begin repairs the same reserved record to CLOSED/no-effect or CLOSE_RETRY/sole-authority-retained before propagation. Pair and clone C outputs remain authoritative until their reserved PhysicalRecords adopt or retain them. Wrapper construction, fileno observation, detach, effect-unknown postcondition observation, one bounded detach retry, and retained-no-retry are explicit monotone states with the strong wrapper reference and raw fallback continuously bound to the same record.

The preserved final-snapshot caller now treats only a post-FROZEN outer late-ready transition as admissible. It retains the identical outer_offer_binding object, OfferCache authority, sequence, packet bytes, ordered offered/full census, and live outer PhysicalRecord; it assigns POST_OFFER_READY_RETAINED and continues into the existing one-send and authenticated-acceptance path without clearing, closing, rebuilding, or recursively calling external_transfer. Generic capabilities and the physical offered census use one immutable 13-role semantic order, with actor_control_fd immediately before pending_expected_raw_fd. The 13-index wire rows remain free of record ids. Refusal remains distinct ZERO_RIGHTS with empty offered/installed/retained/kill wire sets and actor_control_fd safe-local only under the locked refusal guard.

For REFUSAL_ACCEPTED, every fallible sequence check, immutable packet construction, digest, deadline, closure plan, and latch candidate completes while ClosureCell remains NOT_STARTED and without changing CONTROL_SEND_SEQ or an installed cell. One contiguous assignment-only commit installs the complete candidate, records the packet's exact next actor-control message sequence, advances CONTROL_SEND_SEQ once, and enters ACTIVE. Preparation failure propagates with NOT_STARTED, sequence, and installed candidate unchanged. ACTIVE admits only NOT_ATTEMPTED, POSSIBLE, EFFECT_UNKNOWN, and CONFIRMED; the deadline checkpoint is immediately before POSSIBLE, the latch precedes the sole bounded send_exact call, and POSSIBLE reentry never rebuilds, increments, or resends.

The final embedded raw validator selects the actual final definitions and the preserved mismatch caller, compares the two canonical producers and all freeze/pre-send/acceptance order surfaces, and rejects every E0385-listed V19 defect. Its independent negative and positive byte fixtures exercise begin fencing, wrapper postcondition repair, frozen readiness retention, actor-before-pending order, and candidate-before-sequence commit. It remains inert source text here and was not run.

P27 RUNNER V20 ACTOR SOURCE BEGIN 6C20A4F1
import array
import ctypes
import errno
import fcntl
import hashlib
import os
import resource
import select
import signal
import socket
import stat
import struct
import sys
import time

TAG=b"P27E001V15"
PYTHON=b"/root/miniconda3/bin/python3"
PYIMAGE=b"/root/miniconda3/bin/python3.12"
RUNTIME_ROOT=b"/var/lib/p27-e001-host-v15/runtime-root"
ATTEMPT_BASE=b"/var/lib/p27-e001-host-v15/attempts"
STAGE_BASE=b"/tmp/p27-e001-host-v15"
CGROUP_BASE=b"/sys/fs/cgroup/p27-e001-host-v15"
ENV={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
SUITE=(b"P00",b"P01D",b"P01C",b"P02",b"P03",b"P04",b"P05",b"P06",b"P07",b"P08",b"P09",b"P10",b"P11",b"P12",b"P13")
SOURCE_NAMES=(b"keeper.py",b"launcher.py",b"marker.py",b"child.py")
SOURCE_META=((87151,1840,b"cfa1d88b312b7f4425778018be39cf7628568c9ddb39c697ff12b8b0f1c8be1a"),(4216,128,b"e3bf14ddde012be70a0ec40ac9373c055d2fd79d3ea30aa5e64450174f057716"),(4218,128,b"e9d5eb3544dfddd7251279294e113f053165c2d446dd4517fbcdc6927a8618d5"),(75094,1479,b"b06ceed041004279e9df73cc9cc3c2d73ec07d8f71a9345f451a32e93b7a955d"),(19746,452,b"1d20310b965ff9df9351cbc3ca07aebb15e8cbacf74a8058782c085fde0780bf"))
SNAPSHOT_EXPECT=(2303269,23672,b"0ea4f324c5175ec196b8118e551a429a6207cd57bacfdaa9903a109046daab92")
SNAPSHOT_TERMINAL=b"BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V2_SUPERVISOR_PREBIND_FAIL_AND_RUNNER_V3_AUTHOR_OPEN_NO_EXECUTION"
SNAPSHOT_TERMINAL_HEX=SNAPSHOT_TERMINAL.hex().encode("ascii")
WHOLE_V15=(2431,5916064615,0o100644,1,0,0,228310,4622,b"a27eb1bb5540c18b57094ee26724be75a0c431b3c523385fe1271fb02378b845")
V15_TERMINAL=b"BATCH07_P27_E001_SUPERVISOR_HOST_PROBE_RECOVERY_V15_AUTHOR_STOP"
V8_SHA=b"72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf"
PY_SHA=b"9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"
CONTEXT_DOMAIN=b"P27E001_V15_DETACHED_ENVELOPE_CONTEXT\x00"
CERTIFICATE_DOMAIN=b"P27E001_V15_CERTIFICATE_DIGEST\x00"
ENVELOPE_TBS_DOMAIN=b"P27E001_V15_ENVELOPE_TBS\x00"
SIGNATURE_DOMAIN=b"P27E001_V15_ISSUER_SIGNATURE_PREIMAGE\x00"
RECEIPT_DOMAIN=b"P27E001_V15_ISSUER_RECEIPT\x00"
RESERVATION_TBS_DOMAIN=b"P27E001_V15_RESERVATION_TBS\x00"
RESERVATION_SIGNATURE_DOMAIN=b"P27E001_V15_RESERVATION_SIGNATURE\x00"
RESERVATION_RECEIPT_DOMAIN=b"P27E001_V15_RESERVATION_RECEIPT\x00"
FINAL_ENVELOPE_DOMAIN=b"P27E001_V15_FINAL_ENVELOPE\x00"
AUTH_DOMAIN=b"P27E001_V15_SESSION_AUTH\x00"
EXTERNAL_ACCEPTANCE_DOMAIN=b"P27E001_V15_EXTERNAL_ACCEPTANCE\x00"
ISSUER_KEY_BIND_DOMAIN=b"P27E001_V15_ISSUER_KEY_BIND\x00"
EMPTY_SHA=b"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
OP_NS=15000000000
LAUNCH_NS=1000000000
RELEASE_RECORD_OFFSET_NS=800000000
RELEASE_REPLY_OFFSET_NS=900000000
POST_NS=1664800000
HOST_NS=17664800000
TOTAL_NS=18164800000
CLEANUP_NS=2000000000
SIGCONT_NS=5000000
PRECONSUME_NS=10000000000
CONSUMPTION_NS=250000000
ATTEMPT_DIRFD_NS=100000000
STAGE_NS=10000000000
REPORT_NS=1000000000
RECORD_NS=100000000
CANDIDATE_RECORD_NS=100000000
NOTICE_NS=100000000
SEEN_RECORD_NS=100000000
REPORT_RECORD_NS=1000000000
PASS_COMMIT_NS=100000000
PASS_MARGIN_NS=10000000
ACK_NS=500000000
A_RECEIPT_NS=100000000
ACK_RECEIPT_RECORD_NS=100000000
RECONCILIATION_RECORD_NS=100000000
OWNER_CLOSURE_RECORD_NS=100000000
CLOSURE_PACKET_NS=100000000
B_EXIT_NS=100000000
FINAL_TOTAL_NS=2510000000
KILL_TICKET_NS=100000000
RECOVERY_RECORD_NS=100000000
CLEANUP_EFFECT_NS=2600000000
FAILURE_TAIL_NS=2610000000
FAILURE_TOTAL_NS=5210000000
REFUSAL_RECORD_NS=20000000
REFUSAL_ACK_NS=20000000
REFUSAL_RECEIPT_WAIT_NS=30000000
REFUSAL_FINALITY_COMMIT_NS=10000000
REFUSAL_OFFER_BUILD_NS=10000000
REFUSAL_OFFER_SEND_NS=20000000
REFUSAL_ACCEPTANCE_RECV_NS=30000000
REFUSAL_ACCEPTANCE_VERIFY_NS=20000000
REFUSAL_ACCEPTANCE_COMMIT_NS=10000000
REFUSAL_ACTOR_CLOSURE_NS=20000000
REFUSAL_CAPABILITY_CLOSE_NS=10000000
REFUSAL_OWNER_RELEASE_NS=10000000
REFUSAL_FINALITY_NS=80000000
REFUSAL_CLOSURE_TAIL_NS=130000000
REFUSAL_TOTAL_NS=210000000
REFUSAL_PHASE_SPEC=((b"REFUSAL_RECORD",REFUSAL_RECORD_NS),(b"REFUSAL_ACK",REFUSAL_ACK_NS),(b"REFUSAL_RECEIPT_WAIT",REFUSAL_RECEIPT_WAIT_NS),(b"REFUSAL_FINALITY",REFUSAL_FINALITY_COMMIT_NS),(b"REFUSAL_OFFER_BUILD",REFUSAL_OFFER_BUILD_NS),(b"REFUSAL_OFFER_SEND",REFUSAL_OFFER_SEND_NS),(b"REFUSAL_ACCEPTANCE_RECV",REFUSAL_ACCEPTANCE_RECV_NS),(b"REFUSAL_ACCEPTANCE_VERIFY",REFUSAL_ACCEPTANCE_VERIFY_NS),(b"REFUSAL_ACCEPTANCE_COMMIT",REFUSAL_ACCEPTANCE_COMMIT_NS),(b"REFUSAL_ACTOR_CLOSURE",REFUSAL_ACTOR_CLOSURE_NS),(b"REFUSAL_CAPABILITY_CLOSE",REFUSAL_CAPABILITY_CLOSE_NS),(b"REFUSAL_CLOSURE",REFUSAL_OWNER_RELEASE_NS))
ACTOR_DISABLE_NS=500000000
TERMINAL_PHASE_SPEC=((b"CANDIDATE_RECORD",CANDIDATE_RECORD_NS),(b"NOTICE",NOTICE_NS),(b"TERMINAL_SEEN_RECORD",SEEN_RECORD_NS),(b"REPORT_RECORD",REPORT_RECORD_NS),(b"PASS_COMMIT",PASS_COMMIT_NS),(b"PASS_MARGIN",PASS_MARGIN_NS),(b"ACK",ACK_NS),(b"A_RECEIPT",A_RECEIPT_NS),(b"ACK_RECEIPT_RECORD",ACK_RECEIPT_RECORD_NS),(b"RECONCILIATION_RECORD",RECONCILIATION_RECORD_NS),(b"OWNER_CLOSURE_RECORD",OWNER_CLOSURE_RECORD_NS),(b"CLOSURE_PACKET",CLOSURE_PACKET_NS),(b"B_EXIT",B_EXIT_NS))
TERMINAL_BIND_KEYS=tuple(b"bound_"+name.lower()+b"_deadline_ns" for name,cap in TERMINAL_PHASE_SPEC)
CERT_LIFE_NS=360000000000
ENTRY_REMAIN_NS=295482000000
CONSUME_REMAIN_NS=285482000000
PRE_STAGE_REMAIN_NS=285232000000
POST_STAGE_REMAIN_NS=275232000000
POST_CONTAIN_REMAIN_NS=274732000000
STREAM_CAP=3145728
MAX_FILE=16777216
MAX_U63=(1<<63)-1
UINT_MAX=(1<<32)-1
MAX_RIGHTS=4
EXACT_SEALS=fcntl.F_SEAL_WRITE|fcntl.F_SEAL_GROW|fcntl.F_SEAL_SHRINK|fcntl.F_SEAL_SEAL
O_DIR=os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW
LIBC=ctypes.CDLL(None,use_errno=True)
LIBC.syscall.restype=ctypes.c_long
SYS_CLONE3=435
CLONE_PIDFD=0x00001000
CLONE_INTO_CGROUP=0x200000000
CGROUP2_MAGIC=0x63677270
PREFLIGHT=True
STAGE_PRESENT=False
CONTROL_SEND_SEQ=0
CONTROL_RECV_SEQ=0
CONTROL_SEND_STATE=b"IDLE"
B_CHILD_PID=-1
B_CONTROL=None

FAULT_ORDER=(b"INPUT_AUTH",b"ENTRY_CONTEXT",b"CERTIFICATE_INVALID",b"PRECONSUMPTION_DEADLINE",b"CONSUME_EDGE_UNKNOWN",b"ATTEMPT_COLLISION",b"ATTEMPT_NAMESPACE_UNKNOWN",b"ATTEMPT_DIRFD_UNKNOWN",b"ATTEMPT_BASE_DURABILITY_UNKNOWN",b"INTENT_DURABILITY_UNKNOWN",b"CERTIFICATE_EXPIRED",b"CLOCK_DRIFT",b"DEADLINE_EXPIRED",b"CONTROL_MALFORMED",b"CONTROL_TIMEOUT",b"CONTROL_TRUNCATION",b"CONTROL_LOST",b"SEND_EFFECT_UNKNOWN",b"PIDFD_ACTOR_LOST",b"FD_TRANSFER",b"STAGING_FAULT",b"STAGING_DEADLINE",b"CONTAINMENT_FAULT",b"STOP_WAIT_UNKNOWN",b"PIDFD_BINDING",b"LAUNCH_DEADLINE",b"RELEASE_RECORD_DURABILITY_UNKNOWN",b"RELEASE_EFFECT_UNKNOWN",b"SYSCALL_EFFECT_UNKNOWN",b"WATCHDOG_DEADLINE",b"KILL_TICKET_DURABILITY_UNKNOWN",b"KILL_EFFECT_UNKNOWN",b"CAPTURE_IO",b"CAPTURE_OVERFLOW",b"STDERR_NONEMPTY",b"DIRECT_WAIT_UNKNOWN",b"OUTER_STATUS",b"TRANSCRIPT_LANGUAGE",b"TRANSCRIPT_STRUCTURE",b"TRANSCRIPT_SEMANTICS",b"VALIDATED_DURABILITY_UNKNOWN",b"ACK_DURABILITY_UNKNOWN",b"CONTAINMENT_OBSERVATION_UNKNOWN",b"CONTAINMENT_NOT_EMPTY",b"RECOVERY_DURABILITY_UNKNOWN",b"RETAINED_DURABILITY_UNKNOWN",b"REPORT_CANDIDATE_DURABILITY_UNKNOWN",b"TERMINAL_SEEN_DURABILITY_UNKNOWN",b"REPORT_DURABILITY_UNKNOWN",b"ACK_EFFECT_UNKNOWN",b"RECONCILIATION_UNKNOWN",b"OWNER_CLOSURE_DURABILITY_UNKNOWN",b"TRANSFER_PROTOCOL_UNKNOWN",b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED",b"INTERNAL_INVARIANT")

class Refuse(Exception):
 pass

class ConsumedFail(Exception):
 pass

class ConsumedIndeterminate(Exception):
 pass

class CertificateExpired(ConsumedIndeterminate):
 pass

class FaultSet(ConsumedIndeterminate):
 def __init__(self,faults):
  self.faults=set(faults)
  super().__init__("fault-set")

class RemoteAbort(FaultSet):
 pass

class ControlLost(FaultSet):
 def __init__(self,label):
  super().__init__({b"CONTROL_LOST"})

class SendEffectUnknown(FaultSet):
 def __init__(self,label):
  super().__init__({b"SEND_EFFECT_UNKNOWN"})

def need(value,kind=None):
 if not value:
  selected=(Refuse if PREFLIGHT else ConsumedFail) if kind is None else kind
  raise selected("closed")

def udec(raw,low=0,high=MAX_U63):
 need(type(raw)is bytes and raw and raw.isdigit() and (len(raw)==1 or raw[0]!=48))
 value=int(raw);need(low<=value<=high and str(value).encode()==raw)
 return value

def sdec(raw,low=-MAX_U63,high=MAX_U63):
 need(type(raw)is bytes and raw)
 if raw.startswith(b"-"):need(len(raw)>1 and raw[1:].isdigit() and raw[1]!=48)
 else:need(raw.isdigit() and (len(raw)==1 or raw[0]!=48))
 value=int(raw);need(low<=value<=high and str(value).encode()==raw)
 return value

def h64(raw):
 need(type(raw)is bytes and len(raw)==64 and all(x in b"0123456789abcdef" for x in raw))
 return raw

def even_hex(raw,cap=MAX_FILE):
 need(type(raw)is bytes and len(raw)%2==0 and len(raw)<=2*cap)
 need(all(x in b"0123456789abcdef" for x in raw))
 result=bytes.fromhex(raw.decode("ascii"))
 need(result.hex().encode()==raw)
 return result

def octal(raw):
 need(raw and all(x in b"01234567" for x in raw))
 value=int(raw,8);need(format(value,"o").encode()==raw)
 return value

def ascii_file(raw,cap=MAX_FILE):
 need(type(raw)is bytes and 0<len(raw)<=cap and raw.endswith(b"\n"))
 need(all(x==10 or 32<=x<=126 for x in raw))
 return raw

def sha(raw):
 return hashlib.sha256(raw).hexdigest().encode("ascii")

ED_Q=(1<<255)-19
ED_L=(1<<252)+27742317777372353535851937790883648493
ED_D=(-121665*pow(121666,ED_Q-2,ED_Q))%ED_Q
ED_I=pow(2,(ED_Q-1)//4,ED_Q)

def ed_xrecover(y):
 xx=(y*y-1)*pow(ED_D*y*y+1,ED_Q-2,ED_Q)%ED_Q;x=pow(xx,(ED_Q+3)//8,ED_Q)
 if (x*x-xx)%ED_Q:x=x*ED_I%ED_Q
 need((x*x-xx)%ED_Q==0);return x

def ed_decode(raw):
 need(type(raw)is bytes and len(raw)==32);y=int.from_bytes(raw,"little")&((1<<255)-1);sign=raw[31]>>7;need(y<ED_Q);x=ed_xrecover(y)
 if (x&1)!=sign:x=ED_Q-x
 need((-x*x+y*y-1-ED_D*x*x*y*y)%ED_Q==0);return (x,y,1,x*y%ED_Q)

def ed_add(p,q):
 x1,y1,z1,t1=p;x2,y2,z2,t2=q;a=(y1-x1)*(y2-x2)%ED_Q;b=(y1+x1)*(y2+x2)%ED_Q;c=2*ED_D*t1*t2%ED_Q;d=2*z1*z2%ED_Q
 e=(b-a)%ED_Q;f=(d-c)%ED_Q;g=(d+c)%ED_Q;h=(b+a)%ED_Q;return (e*f%ED_Q,g*h%ED_Q,f*g%ED_Q,e*h%ED_Q)

def ed_scalar(point,scalar):
 result=(0,1,1,0);current=point
 while scalar:
  if scalar&1:result=ed_add(result,current)
  current=ed_add(current,current);scalar>>=1
 return result

def ed_encode(point):
 x,y,z,t=point;inverse=pow(z,ED_Q-2,ED_Q);x=x*inverse%ED_Q;y=y*inverse%ED_Q;encoded=bytearray(y.to_bytes(32,"little"));encoded[31]|=(x&1)<<7;return bytes(encoded)

def verify_ed25519(public_key,message,signature):
 need(len(public_key)==32 and len(signature)==64);r=signature[:32];s=int.from_bytes(signature[32:],"little");need(s<ED_L)
 public=ed_decode(public_key);ed_decode(r);base_y=4*pow(5,ED_Q-2,ED_Q)%ED_Q;base_x=ed_xrecover(base_y)
 if base_x&1:base_x=ED_Q-base_x
 base=(base_x,base_y,1,base_x*base_y%ED_Q);challenge=int.from_bytes(hashlib.sha512(r+public_key+message).digest(),"little")%ED_L
 need(ed_encode(ed_scalar(base,s))==ed_encode(ed_add(ed_decode(r),ed_scalar(public,challenge))));return True

def read_all(number,cap=MAX_FILE):
 os.lseek(number,0,os.SEEK_SET);parts=[];total=0
 while True:
  chunk=os.read(number,min(1048576,cap-total+1))
  if not chunk:break
  total+=len(chunk);need(total<=cap);parts.append(chunk)
 return b"".join(parts)

def write_all(number,raw,kind=ConsumedIndeterminate):
 offset=0
 while offset<len(raw):
  try:count=os.write(number,raw[offset:])
  except InterruptedError:continue
  need(count>0,kind);offset+=count

def fd_tuple(number,body):
 held=os.fstat(number)
 return (held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,held.st_size,body.count(b"\n"),sha(body))

def exact_whole(number,expected,terminal):
 fd_access(number,os.O_RDONLY)
 raw=read_all(number,expected[6]);need(fd_tuple(number,raw)==expected,Refuse)
 lines=raw[:-1].split(b"\n");need(lines and lines[-1]==terminal and lines.count(terminal)==1,Refuse)
 return raw

def exact_snapshot(number):
 seals(number);fd_access(number,os.O_RDWR)
 raw=read_all(number,SNAPSHOT_EXPECT[0]);held=os.fstat(number)
 need(stat.S_ISREG(held.st_mode) and held.st_nlink==0 and held.st_uid==held.st_gid==0,Refuse)
 need((held.st_size,raw.count(b"\n"),sha(raw))==SNAPSHOT_EXPECT and raw.endswith(b"\n"),Refuse)
 lines=raw[:-1].split(b"\n")
 need(lines and lines[-1]==SNAPSHOT_TERMINAL and lines.count(SNAPSHOT_TERMINAL)==1,Refuse)
 return raw

def seals(number):
 need(fcntl.fcntl(number,fcntl.F_GET_SEALS)==EXACT_SEALS,Refuse)

def sealed_carrier(number,cap):
 seals(number);fd_access(number,os.O_RDWR);held=os.fstat(number)
 need(stat.S_ISREG(held.st_mode) and held.st_nlink==0 and held.st_uid==held.st_gid==0,Refuse)
 raw=read_all(number,cap);need(held.st_size==len(raw) and len(raw)<=cap,Refuse)
 return raw

def extract_one(raw,begin,end):
 lead=begin+b"\n";tail=end+b"\n"
 need(raw.count(lead)==1 and raw.count(tail)==1)
 start=raw.index(lead)+len(lead);stop=raw.index(tail,start)
 return raw[start:stop]

def meta(raw):
 return (len(raw),raw.count(b"\n"),sha(raw))

def open_dir(path):
 need(type(path)is bytes and path.startswith(b"/") and b"\x00" not in path)
 current=following=-1
 try:
  current=actor_acquire_open_pool(True,b"/",O_DIR)
  for part in path.split(b"/")[1:]:
   need(part not in (b"",b".",b".."))
   following=actor_acquire_open_pool(True,part,O_DIR,dir_fd=current);close_numbers((current,));current=following;following=-1
  held=os.fstat(current)
  need(stat.S_ISDIR(held.st_mode) and held.st_uid==held.st_gid==0 and held.st_mode&0o022==0)
  result=current;current=-1;return result
 finally:close_numbers(tuple(x for x in (following,current) if x>=0))

def open_under(rootfd,path):
 need(path.startswith(b"/") and b"\x00" not in path)
 parts=path.split(b"/")[1:];need(parts and all(x not in (b"",b".",b"..") for x in parts))
 current=following=-1
 try:
  current=actor_acquire_dup(b"open_under_current_fd",b"OPEN_UNDER_CURRENT_FD",rootfd)
  for part in parts[:-1]:
   following=actor_acquire_open(b"open_under_following_fd",b"OPEN_UNDER_FOLLOWING_FD",part,O_DIR,dir_fd=current);close_numbers((current,));actor_promote_record(b"open_under_following_fd",b"open_under_current_fd");current=following;following=-1
  return actor_acquire_open_pool(False,parts[-1],os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=current)
 finally:close_numbers(tuple(x for x in (following,current) if x>=0))

def mount_id(number):
 info=-1
 try:
  info=actor_acquire_open(b"mount_fdinfo_fd",b"MOUNT_FDINFO_OBSERVATION_FD",b"/proc/self/fdinfo/"+str(number).encode(),os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=read_all(info,4096)
 finally:close_numbers(tuple(x for x in (info,) if x>=0))
 values=[x[7:] for x in raw.splitlines() if x.startswith(b"mnt_id:\t")]
 need(len(values)==1);return udec(values[0],1)

def mount_line(number):
 wanted=mount_id(number);info=-1
 try:
  info=actor_acquire_open(b"mount_table_fd",b"MOUNT_TABLE_OBSERVATION_FD",b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(info,1048576),1048576)
 finally:close_numbers(tuple(x for x in (info,) if x>=0))
 matches=[]
 for line in raw.splitlines():
  parts=line.split(b" ")
  if parts and parts[0]==str(wanted).encode():matches.append(line+b"\n")
 need(len(matches)==1);return wanted,matches[0]

class StatFS(ctypes.Structure):
 _fields_=(("f_type",ctypes.c_long),("f_bsize",ctypes.c_long),("rest",ctypes.c_byte*240))

def statfs_magic(number):
 cell=StatFS();need(LIBC.fstatfs(number,ctypes.byref(cell))==0)
 return cell.f_type&0xffffffff

def absent(directory,name,kind=ConsumedFail):
 try:os.stat(name,dir_fd=directory,follow_symlinks=False)
 except FileNotFoundError:return
 raise kind("present")

def durable_leaf(directory,name,raw,deadline,kind=ConsumedIndeterminate):
 number=-1
 try:
  progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS),kind)
  number=actor_acquire_open(b"durable_leaf_fd",b"DURABLE_LEAF_FD",name,os.O_RDWR|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC|os.O_NOFOLLOW,0o400,directory)
  progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS),kind);write_all(number,raw,kind);progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS),kind)
  os.fsync(number);progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS),kind);held=os.fstat(number)
  need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_uid==held.st_gid==0 and held.st_nlink==1 and held.st_size==len(raw),kind)
  need(read_all(number,len(raw))==raw,kind);progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS),kind)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))
 os.fsync(directory);progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS),kind)

def stage_leaf(directory,name,raw,identity,deadline):
 number=-1
 try:
  durable_leaf(directory,name,raw,deadline)
  number=actor_acquire_open(b"stage_leaf_fd",b"STAGE_LEAF_VERIFY_FD",name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=directory)
  progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS));held=os.fstat(number);again=read_all(number,identity[0])
  need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_nlink==1 and held.st_uid==held.st_gid==0)
  need(meta(again)==identity);progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS))
 finally:close_numbers(tuple(x for x in (number,) if x>=0))

def memfd(raw,label):
 number=-1
 try:
  number=actor_acquire_memfd(b"memfd_fd",b"SEALED_MEMFD",label)
  write_all(number,raw);os.lseek(number,0,os.SEEK_SET)
  fcntl.fcntl(number,fcntl.F_ADD_SEALS,EXACT_SEALS);seals(number)
  need(read_all(number,len(raw))==raw);os.lseek(number,0,os.SEEK_SET)
  result=number;number=-1;return result
 finally:close_numbers(tuple(x for x in (number,) if x>=0))

def close_range(first,last):
 need(0<=first<=last<=UINT_MAX)
 need(LIBC.close_range(ctypes.c_uint(first),ctypes.c_uint(last),ctypes.c_uint(0))==0)

def parse_fixed(raw,header,keys,end):
 ascii_file(raw);lines=raw[:-1].split(b"\n")
 need(len(lines)==len(keys)+2 and lines[0]==header and lines[-1]==end)
 result={}
 for key,line in zip(keys,lines[1:-1]):
  parts=line.split(b"=",1);need(len(parts)==2 and parts[0]==key and key not in result)
  result[key]=parts[1]
 return result

ENVELOPE_CONTEXT_KEYS=(b"ISSUER_ID",b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0366_SNAPSHOT_BYTES",b"E0366_SNAPSHOT_LF",b"E0366_SNAPSHOT_SHA256",b"E0366_SNAPSHOT_TERMINAL_HEX",b"V15_SHA256",b"NOT_BEFORE_REALTIME_NS",b"NOT_AFTER_REALTIME_NS",b"ONE_SHOT_RESERVED_BY_ISSUER",b"ONE_SHOT_CONSUMED_BY_ISSUER")
ENVELOPE_KEYS=ENVELOPE_CONTEXT_KEYS+(b"ENVELOPE_CONTEXT_SHA256",b"CERTIFICATE_DIGEST_SHA256",b"SIGNATURE_PREIMAGE_SHA256",b"SIGNATURE_ALGORITHM",b"SIGNATURE_HEX",b"ISSUER_RECEIPT_SHA256")
RESERVATION_TBS_KEYS=(b"ISSUER_ID",b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"CERTIFICATE_DIGEST_SHA256",b"FINAL_ENVELOPE_DIGEST_SHA256",b"NOT_BEFORE_REALTIME_NS",b"NOT_AFTER_REALTIME_NS",b"ONE_SHOT_RESERVED_BY_ISSUER",b"ONE_SHOT_CONSUMED_BY_ISSUER",b"SIGNATURE_ALGORITHM")
RESERVATION_KEYS=RESERVATION_TBS_KEYS+(b"SIGNATURE_PREIMAGE_SHA256",b"SIGNATURE_HEX",b"RESERVATION_DIGEST_SHA256")

CERT_KEYS=(b"ISSUER_ID",b"ISSUER_CONTEXT_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"ARCH",b"KERNEL_RELEASE_HEX",b"NOT_BEFORE_REALTIME_NS",b"ABSOLUTE_EXPIRY_REALTIME_NS",b"ABSOLUTE_LIFETIME_NS",b"REALTIME_BIND_NS",b"MONOTONIC_BIND_NS",b"REALTIME_MONOTONIC_MAX_DRIFT_NS",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0366_SNAPSHOT_BYTES",b"E0366_SNAPSHOT_LF",b"E0366_SNAPSHOT_SHA256",b"E0366_SNAPSHOT_TERMINAL_HEX",b"HISTORICAL_SNAPSHOT_SEALED",b"V15_SHA256",b"V8_SHA256",b"ACTOR_ENTRY_CAPS",b"ACTOR_ENTRY_NNP",b"ACTOR_ENTRY_SECUREBITS",b"PAYLOAD_FINAL_CAPS",b"PAYLOAD_FINAL_NNP",b"PAYLOAD_FINAL_SECUREBITS",b"ATTEMPT_BASE_DEV",b"ATTEMPT_BASE_INO",b"ATTEMPT_BASE_MODE",b"ATTEMPT_BASE_NLINK",b"ATTEMPT_BASE_UID",b"ATTEMPT_BASE_GID",b"ATTEMPT_BASE_MOUNT_ID",b"ATTEMPT_BASE_MOUNTINFO_SHA256",b"ATTEMPT_BASE_FSTYPE_HEX",b"CGROUP2_FS_MAGIC",b"CGROUP2_MOUNT_ID",b"CGROUP2_MOUNTINFO_SHA256",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO",b"CGROUP_BASE_MODE",b"CGROUP_BASE_NLINK",b"CGROUP_BASE_UID",b"CGROUP_BASE_GID",b"CGROUP_BASE_TYPE_HEX",b"CGROUP_BASE_CONTROLLERS_HEX",b"CGROUP_BASE_SUBTREE_CONTROL_HEX",b"CGROUP_NO_EXTERNAL_MUTATOR",b"CGROUP_CHILD_MODE",b"CGROUP_CHILD_UID",b"CGROUP_CHILD_GID",b"CGROUP_CHILD_TYPE_HEX",b"CGROUP_CHILD_CONTROLLERS_HEX",b"CGROUP_CHILD_SUBTREE_CONTROL_HEX",b"RUNTIME_ROOT_DEV",b"RUNTIME_ROOT_INO",b"RUNTIME_ROOT_MODE",b"RUNTIME_ROOT_NLINK",b"RUNTIME_ROOT_UID",b"RUNTIME_ROOT_GID",b"RUNTIME_ROOT_MOUNT_ID",b"RUNTIME_ROOT_MOUNTINFO_SHA256",b"RUNTIME_ROOT_FSTYPE_HEX",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"SAFE_BIND_MODE",b"SAFE_BIND_NLINK",b"SAFE_BIND_UID",b"SAFE_BIND_GID",b"SAFE_BIND_MOUNT_ID",b"SAFE_BIND_MOUNTINFO_SHA256",b"SAFE_BIND_FSTYPE_HEX",b"SAFE_BIND_NOEXEC",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT",b"KEEPER_BYTES",b"KEEPER_LF",b"KEEPER_SHA256",b"LAUNCHER_BYTES",b"LAUNCHER_LF",b"LAUNCHER_SHA256",b"MARKER_BYTES",b"MARKER_LF",b"MARKER_SHA256",b"CHILD_BYTES",b"CHILD_LF",b"CHILD_SHA256",b"PYTHON_IMAGE_SHA256",b"PYTHON_IMAGE_BYTES",b"PYTHON_IMAGE_DEV",b"PYTHON_IMAGE_INO",b"PYTHON_IMAGE_MODE",b"PYTHON_IMAGE_NLINK",b"PYTHON_IMAGE_UID",b"PYTHON_IMAGE_GID",b"LIBC_PATH_HEX",b"LIBC_DEV",b"LIBC_INO",b"LIBC_MODE",b"LIBC_NLINK",b"LIBC_UID",b"LIBC_GID",b"LIBC_BYTES",b"LIBC_SHA256",b"LIBC_CONFSTR_HEX",b"VALID_SIGNAL_COUNT",b"DEFAULT_SIGNAL_COUNT",b"DEFAULTS_SHA256",b"PRECONSUMPTION_CAP_NS",b"CONSUMPTION_PROGRESS_NS",b"ATTEMPT_DIRFD_PROGRESS_NS",b"STAGING_CAP_NS",b"RELEASE_PROGRESS_NS",b"RELEASE_RECORD_ABSOLUTE_OFFSET_NS",b"RELEASE_REPLY_ABSOLUTE_OFFSET_NS",b"SIGCONT_CALL_RETURN_NS",b"DURABLE_RECORD_PROGRESS_NS",b"WATCHDOG_ARM_PROGRESS_NS",b"WATCHDOG_ACK_PROGRESS_NS",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY",b"CGROUP_KILL_WRITE_RETURN_NS",b"CGROUP_KILL_TO_EMPTY_NS",b"FINAL_REPORT_PROGRESS_NS",b"FINAL_PASS_COMMIT_PROGRESS_NS",b"FINAL_PASS_MARGIN_NS",b"TERMINAL_HANDSHAKE_PROGRESS_NS",b"A_RECEIPT_PROGRESS_NS",b"B_CLOSURE_PROGRESS_NS",b"TERMINAL_CANDIDATE_RECORD_NS",b"TERMINAL_NOTICE_PROGRESS_NS",b"TERMINAL_SEEN_RECORD_NS",b"TERMINAL_ACK_RECEIPT_RECORD_NS",b"TERMINAL_RECONCILIATION_RECORD_NS",b"TERMINAL_OWNER_CLOSURE_RECORD_NS",b"TERMINAL_CLOSURE_PACKET_NS",b"TERMINAL_B_EXIT_NS",b"FAILURE_OVERALL_PROGRESS_NS",b"FAILURE_CLEANUP_EFFECT_PROGRESS_NS",b"FAILURE_TAIL_RESERVE_NS",b"REFUSAL_RECORD_PROGRESS_NS",b"REFUSAL_ACK_PROGRESS_NS",b"REFUSAL_RECEIPT_WAIT_PROGRESS_NS",b"REFUSAL_FINALITY_COMMIT_PROGRESS_NS",b"REFUSAL_FINALITY_DEADLINE_PROGRESS_NS",b"REFUSAL_OFFER_BUILD_PROGRESS_NS",b"REFUSAL_OFFER_SEND_PROGRESS_NS",b"REFUSAL_ACCEPTANCE_RECV_PROGRESS_NS",b"REFUSAL_ACCEPTANCE_VERIFY_PROGRESS_NS",b"REFUSAL_ACCEPTANCE_COMMIT_PROGRESS_NS",b"REFUSAL_ACTOR_CLOSURE_PROGRESS_NS",b"REFUSAL_CAPABILITY_CLOSE_PROGRESS_NS",b"REFUSAL_OWNER_RELEASE_PROGRESS_NS",b"REFUSAL_CLOSURE_TAIL_NS",b"REFUSAL_CLOSURE_DEADLINE_PROGRESS_NS",b"FINAL_TERMINAL_TOTAL_NS",b"ENTRY_MIN_REMAINING_NS",b"CONSUMPTION_MIN_REMAINING_NS",b"PRE_STAGE_MIN_REMAINING_NS",b"POST_STAGE_MIN_REMAINING_NS",b"POST_CONTAIN_MIN_REMAINING_NS",b"ACTOR_RELEASE_DISABLE_PROGRESS_NS",b"EXTERNAL_OWNER_PID",b"EXTERNAL_OWNER_STARTTIME",b"EXTERNAL_OWNER_UID",b"EXTERNAL_OWNER_GID",b"EXTERNAL_TRANSFER_MANIFEST_BYTES",b"EXTERNAL_TRANSFER_MANIFEST_SHA256",b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE",b"CLONE3_CPYTHON_GATE_ID",b"CLONE3_CPYTHON_GATE_PASS",b"DELETED_CGROUP_FD_GATE_ID",b"DELETED_CGROUP_FD_GATE_PASS",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_ID",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_PASS",b"EXTERNAL_SURVIVAL_GATE_ID",b"EXTERNAL_SURVIVAL_GATE_PASS",b"OUTER_RECONCILER_GATE_ID",b"OUTER_RECONCILER_GATE_PASS",b"ISSUER_CRYPTOGRAPHY_GATE_ID",b"ISSUER_CRYPTOGRAPHY_GATE_PASS",b"DEP_COUNT")

def canonical_envelope_context(values):
 body=b"P27E001_ISSUER_CONTEXT_V15\n"
 for key in ENVELOPE_CONTEXT_KEYS:body+=key+b"="+values[key]+b"\n"
 return domain_frame(CONTEXT_DOMAIN,b"ENVELOPE_CONTEXT_RAW",body+b"CONTEXT_END=1\n")

def envelope_tbs(values,certificate_digest):
 body=b"P27E001_ISSUER_ENVELOPE_TBS_V15\n"
 for key in ENVELOPE_CONTEXT_KEYS:body+=key+b"="+values[key]+b"\n"
 body+=b"ENVELOPE_CONTEXT_SHA256="+values[b"ENVELOPE_CONTEXT_SHA256"]+b"\nCERTIFICATE_DIGEST_SHA256="+certificate_digest+b"\nSIGNATURE_ALGORITHM="+values[b"SIGNATURE_ALGORITHM"]+b"\nENVELOPE_TBS_END=1\n"
 return domain_frame(ENVELOPE_TBS_DOMAIN,b"ENVELOPE_TBS_RAW",body)

def issuer_signature_preimage(cert_raw,env_tbs):
 payload=length_frame(b"CERTIFICATE_RAW",cert_raw)+length_frame(b"ENVELOPE_TBS",env_tbs)+b"SIGNATURE_PREIMAGE_END=1\n"
 return domain_frame(SIGNATURE_DOMAIN,b"ISSUER_SIGNATURE_TBS_RAW",payload)

def issuer_receipt_preimage(context_digest,certificate_digest,signature_digest,algorithm,signature):
 payload=(b"ENVELOPE_CONTEXT_SHA256="+context_digest+b"\nCERTIFICATE_DIGEST_SHA256="+certificate_digest+b"\nSIGNATURE_PREIMAGE_SHA256="+signature_digest+b"\nSIGNATURE_ALGORITHM="+algorithm+b"\nSIGNATURE_HEX="+signature+b"\nISSUER_RECEIPT_END=1\n")
 return domain_frame(RECEIPT_DOMAIN,b"ISSUER_RECEIPT_TBS_RAW",payload)

def parse_envelope(raw):
 values=parse_fixed(raw,b"P27E001_ISSUER_ENVELOPE_V15",ENVELOPE_KEYS,b"ENVELOPE_END=1")
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V15",b"E0366_SNAPSHOT_BYTES":str(SNAPSHOT_EXPECT[0]).encode(),b"E0366_SNAPSHOT_LF":str(SNAPSHOT_EXPECT[1]).encode(),b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"V15_SHA256":WHOLE_V15[8],b"ONE_SHOT_RESERVED_BY_ISSUER":b"1",b"ONE_SHOT_CONSUMED_BY_ISSUER":b"0",b"SIGNATURE_ALGORITHM":b"ED25519_EXTERNAL_GATE_V15"}
 for key,value in exact.items():need(values[key]==value,Refuse)
 for key in (b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"ENVELOPE_CONTEXT_SHA256",b"CERTIFICATE_DIGEST_SHA256",b"SIGNATURE_PREIMAGE_SHA256",b"ISSUER_RECEIPT_SHA256"):h64(values[key])
 sig=values[b"SIGNATURE_HEX"];need(len(sig)==128 and all(x in b"0123456789abcdef" for x in sig),Refuse)
 before=udec(values[b"NOT_BEFORE_REALTIME_NS"]);after=udec(values[b"NOT_AFTER_REALTIME_NS"]);need(before<after,Refuse)
 context_digest=sha(canonical_envelope_context(values));need(values[b"ENVELOPE_CONTEXT_SHA256"]==context_digest,Refuse)
 return values

def verify_issuer_order(values,cert_raw,cert_values):
 context=canonical_envelope_context(values);context_digest=sha(context);certificate_digest=digest_certificate(cert_raw)
 need(cert_values[b"ISSUER_CONTEXT_SHA256"]==context_digest,Refuse)
 need(values[b"ENVELOPE_CONTEXT_SHA256"]==context_digest and values[b"CERTIFICATE_DIGEST_SHA256"]==certificate_digest,Refuse)
 for key in (b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256"):need(values[key]==cert_values[key],Refuse)
 need(values[b"NOT_BEFORE_REALTIME_NS"]==cert_values[b"NOT_BEFORE_REALTIME_NS"] and values[b"NOT_AFTER_REALTIME_NS"]==cert_values[b"ABSOLUTE_EXPIRY_REALTIME_NS"],Refuse)
 tbs=envelope_tbs(values,certificate_digest);signature_preimage=issuer_signature_preimage(cert_raw,tbs);signature_digest=sha(signature_preimage)
 receipt_preimage=issuer_receipt_preimage(context_digest,certificate_digest,signature_digest,values[b"SIGNATURE_ALGORITHM"],values[b"SIGNATURE_HEX"]);receipt_digest=sha(receipt_preimage)
 need(values[b"SIGNATURE_PREIMAGE_SHA256"]==signature_digest and values[b"ISSUER_RECEIPT_SHA256"]==receipt_digest,Refuse)
 need(cert_values[b"ISSUER_CRYPTOGRAPHY_GATE_PASS"]==b"1" and cert_values[b"ISSUER_CRYPTOGRAPHY_GATE_ID"]!=b"0"*64,Refuse)
 return context_digest,certificate_digest,receipt_digest

def length_frame(label,raw):
 need(type(label)is bytes and label and b"=" not in label and b"\n" not in label and type(raw)is bytes)
 return label+b"="+str(len(raw)).encode()+b"\n"+raw

def domain_frame(domain,label,raw):
 need(type(domain)is bytes and domain.endswith(b"\x00"))
 return domain+length_frame(label,raw)

def digest_certificate(cert_raw):
 return sha(domain_frame(CERTIFICATE_DOMAIN,b"CERTIFICATE_RAW",cert_raw))

def digest_final_envelope(envelope_raw):
 return sha(domain_frame(FINAL_ENVELOPE_DOMAIN,b"FINAL_ENVELOPE_RAW",envelope_raw))

def reservation_tbs(values):
 body=b"P27E001_ISSUER_RESERVATION_TBS_V15\n"
 for key in RESERVATION_TBS_KEYS:body+=key+b"="+values[key]+b"\n"
 return domain_frame(RESERVATION_TBS_DOMAIN,b"RESERVATION_TBS_RAW",body+b"RESERVATION_TBS_END=1\n")

def reservation_signature_preimage(tbs):
 payload=length_frame(b"RESERVATION_TBS",tbs)+b"RESERVATION_SIGNATURE_PREIMAGE_END=1\n"
 return domain_frame(RESERVATION_SIGNATURE_DOMAIN,b"RESERVATION_SIGNATURE_TBS_RAW",payload)

def reservation_receipt_preimage(tbs,signature_digest,algorithm,signature):
 payload=length_frame(b"RESERVATION_TBS",tbs)+b"SIGNATURE_PREIMAGE_SHA256="+signature_digest+b"\nSIGNATURE_ALGORITHM="+algorithm+b"\nSIGNATURE_HEX="+signature+b"\nRESERVATION_RECEIPT_END=1\n"
 return domain_frame(RESERVATION_RECEIPT_DOMAIN,b"RESERVATION_RECEIPT_TBS_RAW",payload)

def parse_reservation(raw):
 values=parse_fixed(raw,b"P27E001_ISSUER_RESERVATION_V15",RESERVATION_KEYS,b"RESERVATION_END=1")
 need(values[b"ISSUER_ID"]==b"P27_HOST_PREMISE_ISSUER_V15" and values[b"ONE_SHOT_RESERVED_BY_ISSUER"]==b"1" and values[b"ONE_SHOT_CONSUMED_BY_ISSUER"]==b"0",Refuse)
 need(values[b"SIGNATURE_ALGORITHM"]==b"ED25519_EXTERNAL_GATE_V15",Refuse)
 for key in (b"AUTHORIZATION_SERIAL",b"CERTIFICATE_DIGEST_SHA256",b"FINAL_ENVELOPE_DIGEST_SHA256",b"SIGNATURE_PREIMAGE_SHA256",b"RESERVATION_DIGEST_SHA256"):h64(values[key])
 sig=values[b"SIGNATURE_HEX"];need(len(sig)==128 and all(x in b"0123456789abcdef" for x in sig),Refuse)
 before=udec(values[b"NOT_BEFORE_REALTIME_NS"]);after=udec(values[b"NOT_AFTER_REALTIME_NS"]);need(before<after,Refuse)
 return values

def verify_reservation_order(values,cert_raw,envelope_raw,envelope_values):
 cert_digest=digest_certificate(cert_raw);envelope_digest=digest_final_envelope(envelope_raw)
 tbs=reservation_tbs(values);signature_preimage=reservation_signature_preimage(tbs);signature_digest=sha(signature_preimage)
 receipt_preimage=reservation_receipt_preimage(tbs,signature_digest,values[b"SIGNATURE_ALGORITHM"],values[b"SIGNATURE_HEX"]);receipt_digest=sha(receipt_preimage)
 need(values[b"CERTIFICATE_DIGEST_SHA256"]==cert_digest and values[b"FINAL_ENVELOPE_DIGEST_SHA256"]==envelope_digest,Refuse)
 need(values[b"SIGNATURE_PREIMAGE_SHA256"]==signature_digest and values[b"RESERVATION_DIGEST_SHA256"]==receipt_digest,Refuse)
 for key in (b"ISSUER_ID",b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"NOT_BEFORE_REALTIME_NS",b"NOT_AFTER_REALTIME_NS",b"ONE_SHOT_RESERVED_BY_ISSUER",b"ONE_SHOT_CONSUMED_BY_ISSUER"):need(values[key]==envelope_values[key],Refuse)
 return receipt_digest

def session_auth(cert_raw,envelope_raw,reservation_raw):
 payload=length_frame(b"CERTIFICATE_RAW",cert_raw)+length_frame(b"FINAL_ENVELOPE_RAW",envelope_raw)+length_frame(b"RESERVATION_RAW",reservation_raw)
 return sha(domain_frame(AUTH_DOMAIN,b"AUTH_TBS_RAW",payload))

def parse_cert(raw):
 ascii_file(raw);lines=raw[:-1].split(b"\n")
 need(lines and lines[0]==b"P27E001_PREMISE_CERTIFICATE_V15" and lines[-1]==b"CERTIFICATE_END=1",Refuse)
 fixed=lines[1:1+len(CERT_KEYS)];need(len(fixed)==len(CERT_KEYS),Refuse);values={}
 for key,line in zip(CERT_KEYS,fixed):
  parts=line.split(b"=",1);need(len(parts)==2 and parts[0]==key and key not in values,Refuse);values[key]=parts[1]
 count=udec(values[b"DEP_COUNT"],1,256);dep_lines=lines[1+len(CERT_KEYS):-1];need(len(dep_lines)==count,Refuse)
 roles={b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC",b"PYTHON_STDLIB",b"PYTHON_EXTENSION",b"NSS_DEPENDENCY",b"RUNTIME_DEPENDENCY"}
 deps=[]
 for index,line in enumerate(dep_lines):
  prefix=b"DEP[%04d]="%index;need(line.startswith(prefix),Refuse);fields=line[len(prefix):].split(b",")
  need(len(fields)==10 and fields[0] in roles,Refuse);path=even_hex(fields[1]);need(path.startswith(b"/") and b"\x00" not in path,Refuse)
  ident=(udec(fields[2],1),udec(fields[3],1),octal(fields[4]),udec(fields[5],1),udec(fields[6]),udec(fields[7]),udec(fields[8]),h64(fields[9]))
  deps.append((fields[0],path,ident))
 need(len(set((x[0],x[1]) for x in deps))==len(deps),Refuse)
 for role in (b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC"):need(sum(x[0]==role for x in deps)==1,Refuse)
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V15",b"ARCH":b"x86_64",b"ABSOLUTE_LIFETIME_NS":b"360000000000",b"REALTIME_MONOTONIC_MAX_DRIFT_NS":b"1000000",b"E0366_SNAPSHOT_BYTES":b"2303269",b"E0366_SNAPSHOT_LF":b"23672",b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"HISTORICAL_SNAPSHOT_SEALED":b"1",b"V15_SHA256":WHOLE_V15[8],b"V8_SHA256":V8_SHA,b"ACTOR_ENTRY_CAPS":b"00000000000401c0",b"ACTOR_ENTRY_NNP":b"0",b"ACTOR_ENTRY_SECUREBITS":b"12",b"PAYLOAD_FINAL_CAPS":b"0000000000000000",b"PAYLOAD_FINAL_NNP":b"1",b"PAYLOAD_FINAL_SECUREBITS":b"15",b"ATTEMPT_BASE_MODE":b"40700",b"ATTEMPT_BASE_UID":b"0",b"ATTEMPT_BASE_GID":b"0",b"CGROUP2_FS_MAGIC":b"63677270",b"CGROUP_BASE_UID":b"0",b"CGROUP_BASE_GID":b"0",b"CGROUP_NO_EXTERNAL_MUTATOR":b"1",b"CGROUP_CHILD_MODE":b"40700",b"CGROUP_CHILD_UID":b"0",b"CGROUP_CHILD_GID":b"0",b"CGROUP_CHILD_TYPE_HEX":b"646f6d61696e0a",b"RUNTIME_ROOT_UID":b"0",b"RUNTIME_ROOT_GID":b"0",b"SAFE_BIND_MODE":b"40700",b"SAFE_BIND_UID":b"0",b"SAFE_BIND_GID":b"0",b"SAFE_BIND_NOEXEC":b"1",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT":b"1",b"KEEPER_BYTES":b"4216",b"KEEPER_LF":b"128",b"KEEPER_SHA256":b"e3bf14ddde012be70a0ec40ac9373c055d2fd79d3ea30aa5e64450174f057716",b"LAUNCHER_BYTES":b"4218",b"LAUNCHER_LF":b"128",b"LAUNCHER_SHA256":b"e9d5eb3544dfddd7251279294e113f053165c2d446dd4517fbcdc6927a8618d5",b"MARKER_BYTES":b"75094",b"MARKER_LF":b"1479",b"MARKER_SHA256":b"b06ceed041004279e9df73cc9cc3c2d73ec07d8f71a9345f451a32e93b7a955d",b"CHILD_BYTES":b"19746",b"CHILD_LF":b"452",b"CHILD_SHA256":b"1d20310b965ff9df9351cbc3ca07aebb15e8cbacf74a8058782c085fde0780bf",b"PYTHON_IMAGE_SHA256":PY_SHA,b"PYTHON_IMAGE_BYTES":b"30626264",b"PYTHON_IMAGE_UID":b"0",b"PYTHON_IMAGE_GID":b"0",b"LIBC_UID":b"0",b"LIBC_GID":b"0",b"PRECONSUMPTION_CAP_NS":b"10000000000",b"CONSUMPTION_PROGRESS_NS":b"250000000",b"ATTEMPT_DIRFD_PROGRESS_NS":b"100000000",b"STAGING_CAP_NS":b"10000000000",b"RELEASE_PROGRESS_NS":b"1000000000",b"RELEASE_RECORD_ABSOLUTE_OFFSET_NS":b"800000000",b"RELEASE_REPLY_ABSOLUTE_OFFSET_NS":b"900000000",b"SIGCONT_CALL_RETURN_NS":b"5000000",b"DURABLE_RECORD_PROGRESS_NS":b"100000000",b"WATCHDOG_ARM_PROGRESS_NS":b"1000000000",b"WATCHDOG_ACK_PROGRESS_NS":b"500000000",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT":b"1",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY":b"1",b"CGROUP_KILL_WRITE_RETURN_NS":b"5000000",b"CGROUP_KILL_TO_EMPTY_NS":b"2000000000",b"FINAL_REPORT_PROGRESS_NS":b"1000000000",b"FINAL_PASS_COMMIT_PROGRESS_NS":b"100000000",b"FINAL_PASS_MARGIN_NS":b"10000000",b"TERMINAL_HANDSHAKE_PROGRESS_NS":b"500000000",b"A_RECEIPT_PROGRESS_NS":b"100000000",b"B_CLOSURE_PROGRESS_NS":b"500000000",b"TERMINAL_CANDIDATE_RECORD_NS":b"100000000",b"TERMINAL_NOTICE_PROGRESS_NS":b"100000000",b"TERMINAL_SEEN_RECORD_NS":b"100000000",b"TERMINAL_ACK_RECEIPT_RECORD_NS":b"100000000",b"TERMINAL_RECONCILIATION_RECORD_NS":b"100000000",b"TERMINAL_OWNER_CLOSURE_RECORD_NS":b"100000000",b"TERMINAL_CLOSURE_PACKET_NS":b"100000000",b"TERMINAL_B_EXIT_NS":b"100000000",b"FAILURE_OVERALL_PROGRESS_NS":b"5210000000",b"FAILURE_CLEANUP_EFFECT_PROGRESS_NS":b"2600000000",b"FAILURE_TAIL_RESERVE_NS":b"2610000000",b"REFUSAL_RECORD_PROGRESS_NS":b"20000000",b"REFUSAL_ACK_PROGRESS_NS":b"20000000",b"REFUSAL_RECEIPT_WAIT_PROGRESS_NS":b"30000000",b"REFUSAL_FINALITY_COMMIT_PROGRESS_NS":b"10000000",b"REFUSAL_FINALITY_DEADLINE_PROGRESS_NS":b"80000000",b"REFUSAL_OFFER_BUILD_PROGRESS_NS":b"10000000",b"REFUSAL_OFFER_SEND_PROGRESS_NS":b"20000000",b"REFUSAL_ACCEPTANCE_RECV_PROGRESS_NS":b"30000000",b"REFUSAL_ACCEPTANCE_VERIFY_PROGRESS_NS":b"20000000",b"REFUSAL_ACCEPTANCE_COMMIT_PROGRESS_NS":b"10000000",b"REFUSAL_ACTOR_CLOSURE_PROGRESS_NS":b"20000000",b"REFUSAL_CAPABILITY_CLOSE_PROGRESS_NS":b"10000000",b"REFUSAL_OWNER_RELEASE_PROGRESS_NS":b"10000000",b"REFUSAL_CLOSURE_TAIL_NS":b"130000000",b"REFUSAL_CLOSURE_DEADLINE_PROGRESS_NS":b"210000000",b"FINAL_TERMINAL_TOTAL_NS":b"2510000000",b"ENTRY_MIN_REMAINING_NS":b"295482000000",b"CONSUMPTION_MIN_REMAINING_NS":b"285482000000",b"PRE_STAGE_MIN_REMAINING_NS":b"285232000000",b"POST_STAGE_MIN_REMAINING_NS":b"275232000000",b"POST_CONTAIN_MIN_REMAINING_NS":b"274732000000",b"ACTOR_RELEASE_DISABLE_PROGRESS_NS":b"500000000",b"EXTERNAL_OWNER_UID":b"0",b"EXTERNAL_OWNER_GID":b"0",b"CLONE3_CPYTHON_GATE_PASS":b"1",b"DELETED_CGROUP_FD_GATE_PASS":b"1",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_PASS":b"1",b"EXTERNAL_SURVIVAL_GATE_PASS":b"1",b"OUTER_RECONCILER_GATE_PASS":b"1",b"ISSUER_CRYPTOGRAPHY_GATE_PASS":b"1"}
 for key,value in exact.items():need(values[key]==value,Refuse)
 for key in (b"ISSUER_CONTEXT_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"ATTEMPT_BASE_MOUNTINFO_SHA256",b"CGROUP2_MOUNTINFO_SHA256",b"RUNTIME_ROOT_MOUNTINFO_SHA256",b"SAFE_BIND_MOUNTINFO_SHA256",b"KEEPER_SHA256",b"LAUNCHER_SHA256",b"MARKER_SHA256",b"CHILD_SHA256",b"LIBC_SHA256",b"DEFAULTS_SHA256",b"EXTERNAL_TRANSFER_MANIFEST_SHA256",b"CLONE3_CPYTHON_GATE_ID",b"DELETED_CGROUP_FD_GATE_ID",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_ID",b"EXTERNAL_SURVIVAL_GATE_ID",b"OUTER_RECONCILER_GATE_ID",b"ISSUER_CRYPTOGRAPHY_GATE_ID"):h64(values[key])
 need(values[b"CLONE3_CPYTHON_GATE_ID"]!=b"0"*64 and values[b"DELETED_CGROUP_FD_GATE_ID"]!=b"0"*64 and values[b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_ID"]!=b"0"*64 and values[b"EXTERNAL_SURVIVAL_GATE_ID"]!=b"0"*64 and values[b"OUTER_RECONCILER_GATE_ID"]!=b"0"*64 and values[b"ISSUER_CRYPTOGRAPHY_GATE_ID"]!=b"0"*64,Refuse)
 for key in (b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE"):need(values[key]==b"1",Refuse)
 for key in (b"KERNEL_RELEASE_HEX",b"E0366_SNAPSHOT_TERMINAL_HEX",b"ATTEMPT_BASE_FSTYPE_HEX",b"CGROUP_BASE_TYPE_HEX",b"CGROUP_BASE_CONTROLLERS_HEX",b"CGROUP_BASE_SUBTREE_CONTROL_HEX",b"CGROUP_CHILD_TYPE_HEX",b"CGROUP_CHILD_CONTROLLERS_HEX",b"CGROUP_CHILD_SUBTREE_CONTROL_HEX",b"RUNTIME_ROOT_FSTYPE_HEX",b"SAFE_BIND_FSTYPE_HEX",b"LIBC_PATH_HEX",b"LIBC_CONFSTR_HEX"):even_hex(values[key])
 for key in (b"ATTEMPT_BASE_MODE",b"CGROUP_BASE_MODE",b"CGROUP_CHILD_MODE",b"RUNTIME_ROOT_MODE",b"SAFE_BIND_MODE",b"PYTHON_IMAGE_MODE",b"LIBC_MODE"):octal(values[key])
 for key in (b"NOT_BEFORE_REALTIME_NS",b"ABSOLUTE_EXPIRY_REALTIME_NS",b"REALTIME_BIND_NS",b"MONOTONIC_BIND_NS",b"ATTEMPT_BASE_DEV",b"ATTEMPT_BASE_INO",b"ATTEMPT_BASE_NLINK",b"ATTEMPT_BASE_MOUNT_ID",b"CGROUP2_MOUNT_ID",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO",b"CGROUP_BASE_NLINK",b"RUNTIME_ROOT_DEV",b"RUNTIME_ROOT_INO",b"RUNTIME_ROOT_NLINK",b"RUNTIME_ROOT_MOUNT_ID",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"SAFE_BIND_NLINK",b"SAFE_BIND_MOUNT_ID",b"KEEPER_BYTES",b"KEEPER_LF",b"LAUNCHER_BYTES",b"LAUNCHER_LF",b"MARKER_BYTES",b"MARKER_LF",b"CHILD_BYTES",b"CHILD_LF",b"PYTHON_IMAGE_DEV",b"PYTHON_IMAGE_INO",b"PYTHON_IMAGE_NLINK",b"PYTHON_IMAGE_UID",b"PYTHON_IMAGE_GID",b"LIBC_DEV",b"LIBC_INO",b"LIBC_NLINK",b"LIBC_BYTES",b"VALID_SIGNAL_COUNT",b"DEFAULT_SIGNAL_COUNT",b"EXTERNAL_OWNER_PID",b"EXTERNAL_OWNER_STARTTIME",b"EXTERNAL_OWNER_UID",b"EXTERNAL_OWNER_GID",b"EXTERNAL_TRANSFER_MANIFEST_BYTES"):udec(values[key])
 by_role={role:next(x for x in deps if x[0]==role) for role in (b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC")}
 need(by_role[b"PYTHON_LINK"][1]==PYTHON and by_role[b"PYTHON_IMAGE"][1]==PYIMAGE and by_role[b"ENV_EXEC"][1]==b"/usr/bin/env" and by_role[b"BASH_EXEC"][1]==b"/usr/bin/bash",Refuse)
 libc=(udec(values[b"LIBC_DEV"],1),udec(values[b"LIBC_INO"],1),octal(values[b"LIBC_MODE"]),udec(values[b"LIBC_NLINK"],1),0,0,udec(values[b"LIBC_BYTES"],1),values[b"LIBC_SHA256"])
 python_image=(udec(values[b"PYTHON_IMAGE_DEV"],1),udec(values[b"PYTHON_IMAGE_INO"],1),octal(values[b"PYTHON_IMAGE_MODE"]),udec(values[b"PYTHON_IMAGE_NLINK"],1),udec(values[b"PYTHON_IMAGE_UID"]),udec(values[b"PYTHON_IMAGE_GID"]),udec(values[b"PYTHON_IMAGE_BYTES"],1),values[b"PYTHON_IMAGE_SHA256"])
 need(by_role[b"PYTHON_IMAGE"][1]==PYIMAGE and by_role[b"PYTHON_IMAGE"][2]==python_image,Refuse)
 need(by_role[b"LIBC"][1]==even_hex(values[b"LIBC_PATH_HEX"]) and by_role[b"LIBC"][2]==libc,Refuse)
 return values,tuple(deps)

def time_fault(kind,fault,label):
 if kind is Refuse:raise Refuse(label)
 raise FaultSet({fault})

def checkpoint(cert,needed,kind=ConsumedIndeterminate,deadline=None):
 m0=time.monotonic_ns();real=time.time_ns();m1=time.monotonic_ns()
 before=udec(cert[b"NOT_BEFORE_REALTIME_NS"]);expiry=udec(cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 if not (before<=real<expiry and expiry-real>=needed):
  if kind is Refuse:raise Refuse("certificate-life")
  raise CertificateExpired("certificate-life")
 base_r=udec(cert[b"REALTIME_BIND_NS"]);base_m=udec(cert[b"MONOTONIC_BIND_NS"])
 if not base_m<=m0<=m1:time_fault(kind,b"CLOCK_DRIFT","monotonic-binding")
 drift=udec(cert[b"REALTIME_MONOTONIC_MAX_DRIFT_NS"]);low=base_r+(m0-base_m);high=base_r+(m1-base_m)
 if not low-drift<=real<=high+drift:time_fault(kind,b"CLOCK_DRIFT","realtime-monotonic-drift")
 if deadline is not None and m1>deadline:time_fault(kind,b"DEADLINE_EXPIRED","absolute-deadline")
 return real,m1

def cert_live(cert,needed,kind=ConsumedIndeterminate):
 return checkpoint(cert,needed,kind)

def verify_platform(cert):
 boot=-1
 try:
  boot=actor_acquire_open(b"boot_id_fd",b"BOOT_ID_OBSERVATION_FD",b"/proc/sys/kernel/random/boot_id",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);boot_raw=read_all(boot,128)
 finally:close_numbers(tuple(x for x in (boot,) if x>=0))
 need(boot_raw.endswith(b"\n") and sha(boot_raw)==cert[b"BOOT_ID_SHA256"],Refuse)
 u=os.uname();parts=(u.sysname,u.release,u.version,u.machine)
 encoded=tuple(x.encode("ascii","strict") for x in parts)
 raw=b"SYSNAME="+encoded[0]+b"\nRELEASE="+encoded[1]+b"\nVERSION="+encoded[2]+b"\nMACHINE="+encoded[3]+b"\n"
 need(encoded[3]==b"x86_64" and encoded[1].hex().encode()==cert[b"KERNEL_RELEASE_HEX"] and sha(raw)==cert[b"PLATFORM_ID_SHA256"],Refuse)

def verify_dependency(rootfd,entry):
 role,path,identity=entry;parts=path.split(b"/")[1:];need(parts and all(x not in (b"",b".",b"..") for x in parts),Refuse)
 current=number=following=-1
 try:
  current=actor_acquire_dup(b"dependency_current_fd",b"DEPENDENCY_CURRENT_FD",rootfd)
  for part in parts[:-1]:
   following=actor_acquire_open(b"dependency_following_fd",b"DEPENDENCY_FOLLOWING_FD",part,O_DIR,dir_fd=current);actor_close_number(current);current=actor_promote_record(b"dependency_following_fd",b"dependency_current_fd");following=-1
  if role==b"PYTHON_LINK":
   held=os.stat(parts[-1],dir_fd=current,follow_symlinks=False);need(stat.S_ISLNK(held.st_mode),Refuse)
   target=os.readlink(parts[-1],dir_fd=current);size=len(target);digest=sha(target)
  else:
   number=actor_acquire_open(b"dependency_leaf_fd",b"DEPENDENCY_LEAF_FD",parts[-1],os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=current)
   held=os.fstat(number);body=read_all(number,identity[6]);size=len(body);digest=sha(body)
  need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,size,digest)==identity,Refuse)
 finally:close_numbers(tuple(x for x in (number,following,current) if x>=0))

def verify_mount(number,cert,prefix,want_magic=None):
 held=os.fstat(number);mode=octal(cert[prefix+b"_MODE"])
 need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==(udec(cert[prefix+b"_DEV"],1),udec(cert[prefix+b"_INO"],1),mode,udec(cert[prefix+b"_NLINK"],1),udec(cert[prefix+b"_UID"]),udec(cert[prefix+b"_GID"])),Refuse)
 mid,line=mount_line(number);need(mid==udec(cert[prefix+b"_MOUNT_ID"],1) and sha(line)==cert[prefix+b"_MOUNTINFO_SHA256"],Refuse)
 if want_magic is not None:need(statfs_magic(number)==want_magic,Refuse)
 return line

def v15_sources(raw):
 result=[]
 for label,expected in zip((b"OUTER",b"KEEPER",b"LAUNCHER",b"MARKER",b"CHILD"),SOURCE_META):
  begin=(b"UNIFIED "+label+b" V15 SOURCE BEGIN") if label!=b"CHILD" else b"NESTED CHILD V15 SOURCE BEGIN"
  end=(b"UNIFIED "+label+b" V15 SOURCE END") if label!=b"CHILD" else b"NESTED CHILD V15 SOURCE END"
  span=extract_one(raw,begin,end);need(meta(span)==expected,Refuse);result.append(span)
 need(extract_one(result[3],b"CHILD_SOURCE=b'''\\",b"'''")==result[4],Refuse)
 return tuple(result)

def clock_binding(cert,kind=ConsumedIndeterminate):
 checkpoint(cert,0,kind)

def progress(cert,deadline,needed=0,kind=ConsumedIndeterminate):
 if time.monotonic_ns()>deadline:time_fault(kind,b"DEADLINE_EXPIRED","absolute-deadline")
 return checkpoint(cert,needed,kind,deadline)


def horizon_needed(deadline,tail):
 return tail+max(0,deadline-time.monotonic_ns())

def exact_schedule(origin,overall,spec,kind=ConsumedIndeterminate):
 need(type(origin)is int and type(overall)is int and origin>0 and overall==origin+sum(cap for name,cap in spec),kind)
 cursor=origin;result={}
 for name,cap in spec:
  need(name not in result and cap>0,kind);cursor+=cap;result[name]=cursor
 need(cursor==overall,kind);return result

def schedule_raw(schedule,spec):
 need(tuple(schedule)==tuple(name for name,cap in spec))
 return b";".join(name+b"="+str(schedule[name]).encode() for name,cap in spec)

def schedule_hex(schedule,spec):
 return schedule_raw(schedule,spec).hex().encode("ascii")

def check_schedule_hex(raw,origin,overall,spec,kind=ConsumedIndeterminate):
 need(type(raw)is bytes and raw and len(raw)%2==0 and all(x in b"0123456789abcdef" for x in raw),kind)
 expected=exact_schedule(origin,overall,spec,kind)
 need(bytes.fromhex(raw.decode("ascii"))==schedule_raw(expected,spec),kind);return expected

def phase_boundary(cert,schedule,spec,name,overall,kind=ConsumedIndeterminate):
 need(name in schedule and schedule==exact_schedule(overall-sum(cap for key,cap in spec),overall,spec,kind),kind)
 deadline=schedule[name];reserve_after=overall-deadline;now=time.monotonic_ns()
 need(now<=deadline,kind);checkpoint(cert,reserve_after,kind,deadline)
 need(time.monotonic_ns()<=deadline,kind);return deadline

def certificate_mono_expiry(cert):
 return udec(cert[b"MONOTONIC_BIND_NS"],1)+udec(cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"])-udec(cert[b"REALTIME_BIND_NS"])-udec(cert[b"REALTIME_MONOTONIC_MAX_DRIFT_NS"])

ACTOR_FD_ROLE_SPEC=(
 (b"stdin_fd",b"STDIN_FD"),(b"stdout_fd",b"STDOUT_FD"),(b"stderr_fd",b"STDERR_FD"),(b"actor_source_carrier_fd",b"ACTOR_SOURCE_CARRIER_FD"),(b"snapshot_carrier_fd",b"SNAPSHOT_CARRIER_FD"),(b"v15_carrier_fd",b"V15_CARRIER_FD"),(b"plan_carrier_fd",b"PLAN_CARRIER_FD"),(b"certificate_carrier_fd",b"CERTIFICATE_CARRIER_FD"),(b"envelope_carrier_fd",b"ENVELOPE_CARRIER_FD"),(b"watchdog_source_carrier_fd",b"WATCHDOG_SOURCE_CARRIER_FD"),(b"reservation_carrier_fd",b"RESERVATION_CARRIER_FD"),(b"external_owner_control_carrier_fd",b"EXTERNAL_OWNER_CONTROL_FD"),(b"external_owner_pidfd_carrier_fd",b"EXTERNAL_OWNER_PIDFD"),(b"external_manifest_carrier_fd",b"EXTERNAL_MANIFEST_CARRIER_FD"),
 (b"open_dir_current_fd",b"OPEN_DIR_CURRENT_FD"),(b"open_dir_following_fd",b"OPEN_DIR_FOLLOWING_FD"),(b"open_under_current_fd",b"OPEN_UNDER_CURRENT_FD"),(b"open_under_following_fd",b"OPEN_UNDER_FOLLOWING_FD"),(b"open_under_leaf_fd",b"OPEN_UNDER_LEAF_FD"),(b"mount_fdinfo_fd",b"MOUNT_FDINFO_OBSERVATION_FD"),(b"mount_table_fd",b"MOUNT_TABLE_OBSERVATION_FD"),(b"durable_leaf_fd",b"DURABLE_LEAF_FD"),(b"stage_leaf_fd",b"STAGE_LEAF_VERIFY_FD"),(b"memfd_fd",b"SEALED_MEMFD"),(b"boot_id_fd",b"BOOT_ID_OBSERVATION_FD"),(b"dependency_current_fd",b"DEPENDENCY_CURRENT_FD"),(b"dependency_following_fd",b"DEPENDENCY_FOLLOWING_FD"),(b"dependency_leaf_fd",b"DEPENDENCY_LEAF_FD"),(b"cap_status_fd",b"PROC_STATUS_OBSERVATION_FD"),(b"pidfd_info_fd",b"PIDFD_INFO_OBSERVATION_FD"),(b"proc_starttime_fd",b"PROC_STARTTIME_OBSERVATION_FD"),(b"cgroup_events_observation_fd",b"CGROUP_EVENTS_OBSERVATION_FD"),(b"cgroup_procs_observation_fd",b"CGROUP_PROCS_OBSERVATION_FD"),
 (b"runtime_root_fd",b"RUNTIME_ROOT_DIRFD"),(b"runtime_tmp_fd",b"RUNTIME_TMP_DIRFD"),(b"runtime_base_fd",b"RUNTIME_BASE_DIRFD"),(b"runtime_cwd_fd",b"RUNTIME_CWD_DIRFD"),(b"runtime_attempt_base_fd",b"RUNTIME_ATTEMPT_BASE_DIRFD"),(b"runtime_stage_base_fd",b"RUNTIME_STAGE_BASE_DIRFD"),(b"runtime_cgroup_base_fd",b"RUNTIME_CGROUP_BASE_DIRFD"),(b"launch_empty_r_fd",b"LAUNCH_EMPTY_R_FD"),(b"launch_empty_w_fd",b"LAUNCH_EMPTY_W_FD"),(b"launch_left_fd",b"LAUNCH_CONTROL_LEFT_FD"),(b"launch_right_fd",b"LAUNCH_CONTROL_RIGHT_FD"),(b"launch_actor_pidfd",b"LAUNCH_ACTOR_PIDFD"),
 (b"probe_in_r_fd",b"PROBE_IN_R_FD"),(b"probe_in_w_fd",b"PROBE_IN_W_FD"),(b"probe_out_r_fd",b"PROBE_OUT_R_FD"),(b"probe_out_w_fd",b"PROBE_OUT_W_FD"),(b"probe_err_r_fd",b"PROBE_ERR_R_FD"),(b"probe_err_w_fd",b"PROBE_ERR_W_FD"),(b"probe_outer_memfd",b"PROBE_OUTER_MEMFD"),(b"probe_events_fd",b"PROBE_EVENTS_FD"),(b"probe_outer_pidfd",b"PROBE_OUTER_PIDFD"),(b"outer_mountinfo_fd",b"OUTER_MOUNTINFO_OBSERVATION_FD"),
 (b"base_type_fd",b"BASE_TYPE_OBSERVATION_FD"),(b"base_controllers_fd",b"BASE_CONTROLLERS_OBSERVATION_FD"),(b"base_subtree_fd",b"BASE_SUBTREE_OBSERVATION_FD"),(b"stage_safe_fd",b"STAGE_SAFE_DIRFD"),(b"containment_cgroup_fd",b"CONTAINMENT_CGROUP_DIRFD"),(b"containment_type_fd",b"CONTAINMENT_TYPE_OBSERVATION_FD"),(b"containment_controllers_fd",b"CONTAINMENT_CONTROLLERS_OBSERVATION_FD"),(b"containment_subtree_fd",b"CONTAINMENT_SUBTREE_OBSERVATION_FD")
)+tuple((b"actor_dir_pool_"+str(index).encode(),b"DYNAMIC_DIR_FD") for index in range(32))+tuple((b"actor_file_pool_"+str(index).encode(),b"DYNAMIC_FILE_FD") for index in range(64))+tuple((b"actor_quarantine_"+str(index).encode(),b"SCM_RIGHTS_QUARANTINE_FD") for index in range(4))+tuple((b"actor_mapping_park_"+str(index).encode(),b"MAPPING_PARK_FD") for index in range(24))+tuple((b"actor_mapping_target_"+str(index).encode(),b"MAPPING_TARGET_FD") for index in range(24))
ACTOR_FD_ROLE_MAP={role:kind for role,kind in ACTOR_FD_ROLE_SPEC}
ACTOR_FD_REGISTRY={role:[kind,b"RESERVED",-1,None,False,None] for role,kind in ACTOR_FD_ROLE_SPEC}
ACTOR_FD_JOURNAL=[]

def actor_fd_identity(number):
 held=os.fstat(number);access=fcntl.fcntl(number,fcntl.F_GETFL)&os.O_ACCMODE
 return (held.st_dev,held.st_ino,held.st_mode,held.st_uid,held.st_gid,access)

def actor_live_owner(number,exclude=None):
 owner=None
 for role,record in ACTOR_FD_REGISTRY.items():
  if role!=exclude and record[4] and record[2]==number:need(owner is None);owner=role
 return owner

def actor_audit(role):
 try:ACTOR_FD_JOURNAL.append((role,)+tuple(ACTOR_FD_REGISTRY[role][:5]))
 except BaseException:pass

def actor_begin_acquisition(role,kind):
 need(role in ACTOR_FD_ROLE_MAP and ACTOR_FD_ROLE_MAP[role]==kind);record=ACTOR_FD_REGISTRY[role];need(not record[4] and record[1]!=b"ACQUIRING")
 record[0]=kind;record[1]=b"ACQUIRING";record[2]=-1;record[3]=None;record[4]=False;record[5]=None;return record

def actor_finish_adoption(role):
 record=ACTOR_FD_REGISTRY[role];number=record[2];need(record[4] and number>=0 and actor_live_owner(number,role) is None)
 try:identity=actor_fd_identity(number)
 except BaseException:record[1]=b"ADOPTED_RAW_CLOSE_REQUIRED";actor_close_record(role);raise
 record[3]=identity;record[1]=b"OPEN_PROVED";actor_audit(role);return number

def actor_adopt_raw(role,kind,number,endpoint=None):
 record=actor_begin_acquisition(role,kind);need(type(number)is int and number>=0);record[2]=number;record[1]=b"ADOPTED_RAW";record[4]=True;record[5]=endpoint
 try:return actor_finish_adoption(role)
 except BaseException:actor_close_record(role);raise

def register_runtime_fd(slot,kind,number):
 return actor_adopt_raw(slot,kind,number)

def actor_acquire_open(role,kind,path,flags,mode=0o777,dir_fd=None):
 record=actor_begin_acquisition(role,kind)
 try:
  number=os.open(path,flags,mode,dir_fd=dir_fd);record[2]=number;record[1]=b"ADOPTED_RAW";record[4]=True
  return actor_finish_adoption(role)
 except BaseException:
  if record[4]:actor_close_record(role)
  else:record[1]=b"ACQUIRE_FAILED_NO_FD"
  raise

def actor_acquire_open_pool(directory,path,flags,mode=0o777,dir_fd=None):
 prefix=b"actor_dir_pool_" if directory else b"actor_file_pool_";kind=b"DYNAMIC_DIR_FD" if directory else b"DYNAMIC_FILE_FD";role=None
 for candidate,record in ACTOR_FD_REGISTRY.items():
  if candidate.startswith(prefix) and not record[4] and record[1]!=b"ACQUIRING":role=candidate;break
 need(role is not None);return actor_acquire_open(role,kind,path,flags,mode,dir_fd)

def actor_acquire_dup(role,kind,source):
 record=actor_begin_acquisition(role,kind)
 try:
  number=os.dup(source);record[2]=number;record[1]=b"ADOPTED_RAW";record[4]=True
  return actor_finish_adoption(role)
 except BaseException:
  if record[4]:actor_close_record(role)
  else:record[1]=b"ACQUIRE_FAILED_NO_FD"
  raise

def actor_acquire_dup_pool(directory,source):
 prefix=b"actor_dir_pool_" if directory else b"actor_file_pool_";kind=b"DYNAMIC_DIR_FD" if directory else b"DYNAMIC_FILE_FD";role=None
 for candidate,record in ACTOR_FD_REGISTRY.items():
  if candidate.startswith(prefix) and not record[4] and record[1]!=b"ACQUIRING":role=candidate;break
 need(role is not None);return actor_acquire_dup(role,kind,source)

def actor_acquire_mapping_park(index,source):
 role=b"actor_mapping_park_"+str(index).encode();record=actor_begin_acquisition(role,b"MAPPING_PARK_FD")
 try:
  number=fcntl.fcntl(source,fcntl.F_DUPFD_CLOEXEC,200);record[2]=number;record[1]=b"ADOPTED_RAW";record[4]=True
  return actor_finish_adoption(role)
 except BaseException:
  if record[4]:actor_close_record(role)
  raise

def actor_dup2_mapping_target(index,source,target):
 role=b"actor_mapping_target_"+str(index).encode();owner=actor_live_owner(target)
 if owner is not None:actor_close_record(owner)
 record=actor_begin_acquisition(role,b"MAPPING_TARGET_FD")
 try:
  number=os.dup2(source,target,inheritable=True);record[2]=number;record[1]=b"ADOPTED_RAW";record[4]=True
  return actor_finish_adoption(role)
 except BaseException:
  if record[4]:actor_close_record(role)
  raise

def actor_close_registered_range(first,last):
 for role,record in ACTOR_FD_REGISTRY.items():
  if record[4] and first<=record[2]<=last:actor_close_record(role)
 return True

def actor_acquire_memfd(role,kind,label):
 record=actor_begin_acquisition(role,kind)
 try:
  number=os.memfd_create(label,os.MFD_CLOEXEC|os.MFD_ALLOW_SEALING);record[2]=number;record[1]=b"ADOPTED_RAW";record[4]=True
  return actor_finish_adoption(role)
 except BaseException:
  if record[4]:actor_close_record(role)
  else:record[1]=b"ACQUIRE_FAILED_NO_FD"
  raise

def actor_acquire_pipe2(read_role,write_role,flags):
 read=actor_begin_acquisition(read_role,ACTOR_FD_ROLE_MAP[read_role]);write=actor_begin_acquisition(write_role,ACTOR_FD_ROLE_MAP[write_role])
 try:
  read_number,write_number=os.pipe2(flags);read[2]=read_number;read[1]=b"ADOPTED_RAW";read[4]=True;write[2]=write_number;write[1]=b"ADOPTED_RAW";write[4]=True
  return actor_finish_adoption(read_role),actor_finish_adoption(write_role)
 except BaseException:
  if read[4]:actor_close_record(read_role)
  if write[4]:actor_close_record(write_role)
  raise

def actor_acquire_socketpair(left_role,right_role):
 left_record=actor_begin_acquisition(left_role,ACTOR_FD_ROLE_MAP[left_role]);right_record=actor_begin_acquisition(right_role,ACTOR_FD_ROLE_MAP[right_role])
 try:
  left,right=socket.socketpair(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC|socket.SOCK_NONBLOCK);left_record[2]=left.fileno();left_record[1]=b"ADOPTED_RAW";left_record[4]=True;left_record[5]=left;right_record[2]=right.fileno();right_record[1]=b"ADOPTED_RAW";right_record[4]=True;right_record[5]=right
  actor_finish_adoption(left_role);actor_finish_adoption(right_role);return left,right
 except BaseException:
  if left_record[4]:actor_close_record(left_role)
  if right_record[4]:actor_close_record(right_role)
  raise

def actor_acquire_pidfd(role,pid):
 record=actor_begin_acquisition(role,ACTOR_FD_ROLE_MAP[role])
 try:
  number=os.pidfd_open(pid,0);record[2]=number;record[1]=b"ADOPTED_RAW";record[4]=True
  return actor_finish_adoption(role)
 except BaseException:
  if record[4]:actor_close_record(role)
  raise

def actor_promote_record(old_role,new_role):
 source=ACTOR_FD_REGISTRY[old_role];destination=ACTOR_FD_REGISTRY[new_role];need(source[4] and not destination[4]);number=source[2]
 destination[0]=ACTOR_FD_ROLE_MAP[new_role];destination[1]=b"OPEN_PROVED";destination[2]=number;destination[3]=source[3];destination[5]=source[5];destination[4]=True
 source[4]=False;source[2]=-1;source[1]=b"PROMOTED_ALIAS_CLEARED";source[5]=None;actor_audit(old_role);actor_audit(new_role);return number

def actor_close_record(role):
 record=ACTOR_FD_REGISTRY[role]
 if not record[4]:return True
 number=record[2];identity=record[3];need(actor_live_owner(number,role) is None)
 if identity is not None:
  try:observed=actor_fd_identity(number)
  except OSError as probe:
   if probe.errno==errno.EBADF:record[2]=-1;record[1]=b"PROVED_CLOSED_BEFORE_RETRY_EBADF";record[4]=False;record[5]=None;actor_audit(role);return True
   record[1]=b"PRE_CLOSE_REVALIDATION_HOLD";raise
  need(observed==identity)
 endpoint=record[5]
 if endpoint is not None:detached=endpoint.detach();need(detached==number);record[5]=None
 try:os.close(number)
 except OSError:
  try:observed=actor_fd_identity(number)
  except OSError as probe:
   if probe.errno==errno.EBADF:record[2]=-1;record[1]=b"PROVED_CLOSED_AFTER_EBADF";record[4]=False;record[5]=None;actor_audit(role);return True
   record[1]=b"CLOSE_RECONCILIATION_HOLD";raise
  if identity is not None and observed==identity:record[1]=b"OPEN_RETRYABLE_AFTER_CLOSE_ERROR";raise
  record[1]=b"CLOSE_IDENTITY_MISMATCH_HOLD";raise
 record[2]=-1;record[1]=b"PROVED_CLOSED_BY_RETURN";record[4]=False;record[5]=None;actor_audit(role);return True

def actor_close_number(number):
 role=actor_live_owner(number)
 if role is not None:return actor_close_record(role)
 try:os.close(number)
 except OSError:
  try:os.fstat(number)
  except OSError as probe:need(probe.errno==errno.EBADF);return True
 raise
 return True

def actor_quarantine_rights(ancillary):
 installed=[];bad=False
 try:
  for level,kind,data in ancillary:
   if level!=socket.SOL_SOCKET or kind!=socket.SCM_RIGHTS:bad=True;continue
   cells=array.array("i");whole=len(data)-(len(data)%cells.itemsize)
   if whole:cells.frombytes(data[:whole])
   if whole!=len(data):bad=True
   for number in cells:
    role=None
    for candidate,record in ACTOR_FD_REGISTRY.items():
     if candidate.startswith(b"actor_quarantine_") and not record[4] and record[1]!=b"ACQUIRING":role=candidate;break
    if role is None:
     actor_close_number(number);bad=True;continue
    actor_adopt_raw(role,b"SCM_RIGHTS_QUARANTINE_FD",number);installed.append(number)
  return installed,bad
 except BaseException:
  close_numbers(tuple(installed));raise

def actor_bootstrap_registry():
 for role,kind,number in ((b"stdin_fd",b"STDIN_FD",0),(b"stdout_fd",b"STDOUT_FD",1),(b"stderr_fd",b"STDERR_FD",2),(b"actor_source_carrier_fd",b"ACTOR_SOURCE_CARRIER_FD",100),(b"snapshot_carrier_fd",b"SNAPSHOT_CARRIER_FD",101),(b"v15_carrier_fd",b"V15_CARRIER_FD",102),(b"plan_carrier_fd",b"PLAN_CARRIER_FD",103),(b"certificate_carrier_fd",b"CERTIFICATE_CARRIER_FD",104),(b"envelope_carrier_fd",b"ENVELOPE_CARRIER_FD",105),(b"watchdog_source_carrier_fd",b"WATCHDOG_SOURCE_CARRIER_FD",106),(b"reservation_carrier_fd",b"RESERVATION_CARRIER_FD",107),(b"external_owner_control_carrier_fd",b"EXTERNAL_OWNER_CONTROL_FD",108),(b"external_owner_pidfd_carrier_fd",b"EXTERNAL_OWNER_PIDFD",109),(b"external_manifest_carrier_fd",b"EXTERNAL_MANIFEST_CARRIER_FD",110)):actor_adopt_raw(role,kind,number)
 return True

def actor_close_all():
 for role,record in ACTOR_FD_REGISTRY.items():
  if record[4]:actor_close_record(role)
 return True

def cap_status():
 number=-1
 try:
  number=actor_acquire_open(b"cap_status_fd",b"PROC_STATUS_OBSERVATION_FD",b"/proc/self/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(number,65536),65536)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))
 keys=(b"CapInh",b"CapPrm",b"CapEff",b"CapBnd",b"CapAmb",b"NoNewPrivs")
 values={}
 for line in raw.splitlines():
  for key in keys:
   prefix=key+b":"
   if line.startswith(prefix):
    need(key not in values);values[key]=line[len(prefix):].strip()
 need(set(values)==set(keys))
 return values

def securebits():
 result=LIBC.prctl(27,0,0,0,0);need(result>=0)
 return result

def verify_creds(final):
 values=cap_status();zero=b"0000000000000000"
 need(os.getresuid()==(0,0,0) and os.getresgid()==(0,0,0) and os.getgroups()==[])
 if final:
  need(all(values[x]==zero for x in (b"CapInh",b"CapPrm",b"CapEff",b"CapBnd",b"CapAmb")))
  need(values[b"NoNewPrivs"]==b"1" and securebits()==15)
 else:
  need(values[b"CapInh"]==zero and values[b"CapAmb"]==zero)
  need(all(values[x]==b"00000000000401c0" for x in (b"CapPrm",b"CapEff",b"CapBnd")))
  need(values[b"NoNewPrivs"]==b"0" and securebits()==12,Refuse)

def normalize_limits():
 inf=resource.RLIM_INFINITY
 fixed=((resource.RLIMIT_AS,(inf,inf)),(resource.RLIMIT_CORE,(0,0)),(resource.RLIMIT_CPU,(inf,inf)),(resource.RLIMIT_DATA,(inf,inf)),(resource.RLIMIT_FSIZE,(inf,inf)),(resource.RLIMIT_MEMLOCK,(8388608,8388608)),(resource.RLIMIT_MSGQUEUE,(819200,819200)),(resource.RLIMIT_NICE,(0,0)),(resource.RLIMIT_NOFILE,(1048576,1048576)),(resource.RLIMIT_NPROC,(1048576,1048576)),(resource.RLIMIT_RSS,(inf,inf)),(resource.RLIMIT_RTPRIO,(0,0)),(resource.RLIMIT_RTTIME,(inf,inf)),(resource.RLIMIT_SIGPENDING,(515199,515199)),(resource.RLIMIT_STACK,(8388608,inf)))
 for key,value in fixed:resource.setrlimit(key,value)
 for key,value in fixed:need(resource.getrlimit(key)==value)

def normalize_signals():
 for which in (signal.ITIMER_REAL,signal.ITIMER_VIRTUAL,signal.ITIMER_PROF):signal.setitimer(which,0.0,0.0)
 valid=signal.valid_signals();catchable=tuple(sorted(int(x) for x in valid if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP))))
 signal.pthread_sigmask(signal.SIG_SETMASK,set())
 for number in catchable:signal.signal(number,signal.SIG_DFL)
 need(signal.sigpending()==set())

class CapHeader(ctypes.Structure):
 _fields_=(("version",ctypes.c_uint32),("pid",ctypes.c_int))

class CapData(ctypes.Structure):
 _fields_=(("effective",ctypes.c_uint32),("permitted",ctypes.c_uint32),("inheritable",ctypes.c_uint32))

class CloneArgs(ctypes.Structure):
 _fields_=(("flags",ctypes.c_uint64),("pidfd",ctypes.c_uint64),("child_tid",ctypes.c_uint64),("parent_tid",ctypes.c_uint64),("exit_signal",ctypes.c_uint64),("stack",ctypes.c_uint64),("stack_size",ctypes.c_uint64),("tls",ctypes.c_uint64),("set_tid",ctypes.c_uint64),("set_tid_size",ctypes.c_uint64),("cgroup",ctypes.c_uint64))

def final_drop():
 need(LIBC.prctl(28,15,0,0,0)==0)
 for bit in range(64):
  result=LIBC.prctl(24,bit,0,0,0)
  if result!=0:need(ctypes.get_errno()==errno.EINVAL)
 header=CapHeader(0x20080522,0);data=(CapData*2)()
 need(LIBC.capset(ctypes.byref(header),ctypes.byref(data))==0)
 need(LIBC.prctl(47,4,0,0,0)==0 and LIBC.prctl(38,1,0,0,0)==0)

def child_context(cwd_name,safe_dev,safe_ino):
 root=-1;os.chroot(RUNTIME_ROOT)
 try:
  root=actor_acquire_open_pool(True,b"/",O_DIR)
  tmp=actor_acquire_open_pool(True,b"tmp",O_DIR,dir_fd=root);base=actor_acquire_open_pool(True,b"p27-e001-host-v15",O_DIR,dir_fd=tmp)
  cwd=actor_acquire_dup_pool(True,base) if cwd_name is None else actor_acquire_open_pool(True,cwd_name,O_DIR,dir_fd=base)
  held=os.fstat(cwd);need((held.st_dev,held.st_ino,held.st_uid,held.st_gid,stat.S_IMODE(held.st_mode))==(safe_dev,safe_ino,0,0,0o700))
  os.fchdir(cwd)
 finally:
  for number in (locals().get("cwd",-1),locals().get("base",-1),locals().get("tmp",-1),root):
   if number>=0:
    actor_close_number(number)
 os.setgroups([]);os.setresgid(0,0,0);os.setresuid(0,0,0);os.umask(0o077)
 normalize_limits();normalize_signals();final_drop();verify_creds(True)

def fd_access(number,mode):
 need(fcntl.fcntl(number,fcntl.F_GETFL)&os.O_ACCMODE==mode)

def scrub_exact(expected):
 seen=set()
 for item in os.listdir(b"/proc/self/fd"):
  if item.isdigit():
   number=int(item)
   try:os.fstat(number)
   except OSError as error:
    need(error.errno==errno.EBADF);continue
   seen.add(number)
 need(seen==expected)

def preserved_map(mapping):
 parked=[];number=-1;targets={target for source,target in mapping}
 try:
  for index,(source,target) in enumerate(mapping):
   number=actor_acquire_mapping_park(index,source)
   need(number>=200 and number not in targets and number not in [x[0] for x in parked])
   parked.append((number,target));number=-1
  for index,(held,target) in enumerate(parked):actor_dup2_mapping_target(index,held,target)
 finally:
  close_numbers(tuple(x for x in (number,) if x>=0))
  for held,target in parked:
   actor_close_number(held)

# P27 RUNNER V20 EMBEDDED VALIDATOR BEGIN 8E20B7D2
COMMON=(b"marker_image_dev",b"marker_image_ino",b"marker_image_sha256",b"probe_start_ns",b"probe_finish_ns",b"probe_elapsed_ns",b"probe_bound_ns",b"primary_failure",b"cleanup_failure",b"result")
PREFIX={b"P00":(b"source_item_bytes",b"source_item_accounted_bytes",b"broker_spawned",b"broker_payload_hex"),b"P01D":(b"python_image_dev",b"python_image_ino",b"python_image_bytes",b"python_image_sha256",b"libc_confstr_hex",b"libc_path_hex",b"libc_bytes",b"libc_sha256",b"backend_surface",b"spawn_premise_satisfied"),b"P01C":(b"libc_path_hex",b"libc_sha256",b"libc_confstr_hex",b"child_pids",b"child_statuses",b"child_raw_hex",b"spawn_premise_satisfied"),b"P02":(b"fds",b"environment_count",b"cwd_hex",b"flags"),b"P03":(b"soft_before",b"hard_before",b"soft_test",b"opened_fds",b"emfile"),b"P04":(b"valid_signal_count",b"default_signal_count",b"defaults_sha256",b"mask_empty"),b"P05":(b"wnohang_zero",b"eintr",b"echild",b"child_pids",b"raw_statuses",b"term_signal",b"broker_payload_hex"),b"P06":(b"monotonic",b"observed_min_delta_ns",b"start_ns",b"end_ns",b"deadline_checked"),b"P07":(b"empty_eagain",b"eof_before_last_writer",b"eof_after_last_writer"),b"P08":(b"child_pids",b"raw_statuses",b"same_session_group",b"post_pid_esrch",b"broker_payload_hex"),b"P09":(b"child_pids",b"raw_statuses",b"signal",b"reap_start_ns",b"reap_end_ns",b"reaped"),b"P10":(b"sample_count",b"pids",b"statuses",b"pid_duplicates",b"group_is_single_owned_launcher_group",b"reuse_proof"),b"P11":(b"open_result",b"atime_unchanged",b"cleanup_unlinked",b"cleanup_identity_observed",b"atomic_unlink_proof",b"scope_single_inode"),b"P12":(b"child_pids",b"raw_statuses",b"environment_count",b"underscore_absent",b"real_payload_invoked",b"broker_payload_hex"),b"P13":(b"file_fsync_returned",b"hardlink_noreplace_returned",b"inode_preserved",b"dir_fsync_returned",b"post_unlink_absent",b"cleanup_unlinked",b"durability_proof",b"rename_atomicity_proof")}

def csv_values(raw,signed=False,count=None):
 parts=raw.split(b",");need(parts and (count is None or len(parts)==count))
 return tuple(sdec(x) if signed else udec(x,1) for x in parts)

def child_observation(raw,mode,pid,source_sha,cwd_hex,phase):
 need(raw.endswith(b"\n") and raw.count(b"\n")==1)
 fields=raw[:-1].split(b"|");need(len(fields)==11 and fields[0]==TAG and fields[1]==b"child=observation")
 need(fields[2]==b"mode="+mode and fields[3]==b"pid="+str(pid).encode())
 need(fields[4].startswith(b"sid=") and udec(fields[4][4:],1)>0)
 need(fields[5].startswith(b"pgid=") and udec(fields[5][5:],1)>0)
 need(tuple(fields[6:])==(b"image_sha="+PY_SHA,b"source_sha="+source_sha,b"cwd_hex="+cwd_hex,b"phase="+phase,b"result=PASS"))

def payload_item(raw,prefix):
 lead=prefix+b":";need(raw.startswith(lead));return even_hex(raw[len(lead):])

def parse_outer(line,probe,terminal):
 fields=line.split(b"|")
 if terminal:need(len(fields)==8 and fields[0]==TAG and fields[1]==b"outer=terminal" and fields[2]==b"probe="+probe and fields[3]==b"all_reaped=1" and fields[5]==b"frame_complete=1" and fields[6]==b"fatal=0" and fields[7]==b"result=PASS")
 else:need(len(fields)==8 and fields[0]==TAG and fields[1]==b"outer=candidate" and fields[2]==b"probe="+probe and fields[3]==b"slots=4" and fields[4]==b"all_reaped=1" and fields[6]==b"fatal=0" and fields[7]==b"result=PASS")
 role_field=fields[4] if terminal else fields[5];need(role_field.startswith(b"role_statuses="))
 roles=role_field[14:].split(b",");need(len(roles)==4);result={}
 for expected,item in zip((b"launcher",b"keeper",b"marker",b"child"),roles):
  pieces=item.split(b":",1);need(len(pieces)==2 and pieces[0]==expected);result[expected]=sdec(pieces[1])
 return result

def validate_probe(rows,probe,ctx):
 if probe==b"P00":
  need(rows[b"source_item_bytes"]==b"251414" and rows[b"source_item_accounted_bytes"]==b"251415")
  child=ctx[b"child_source"];need((len(child),child.count(b"\n"),sha(child))==SOURCE_META[4])
  padding=251414-len(child)-2;need(padding>=0)
  synthetic=child+b"\n#"+b"x"*padding
  need(len(synthetic)==251414 and synthetic[:len(child)]==child and synthetic[len(child):len(child)+2]==b"\n#");synthetic_sha=sha(synthetic)
  spawned=udec(rows[b"broker_spawned"],0,1);items=even_hex(rows[b"broker_payload_hex"]).split(b";")
  if spawned==0:
   need(len(items)==1 and items[0]==b"source_bytes=251414,returned=0,e2big=1,sha="+synthetic_sha)
  else:
   need(len(items)==2 and items[1]==b"source_bytes=251414,returned=1,e2big=0,sha="+synthetic_sha)
   observation=payload_item(items[0],b"INFO");fields=observation.split(b"|");need(len(fields)==11 and fields[3].startswith(b"pid="))
   child_observation(observation,b"INFO",udec(fields[3][4:],1),synthetic_sha,ctx[b"cwd_hex"],b"terminal")
 elif probe==b"P01D":
  need(udec(rows[b"python_image_dev"],1)==ctx[b"python_dev"] and udec(rows[b"python_image_ino"],1)==ctx[b"python_ino"])
  need(rows[b"python_image_bytes"]==b"30626264" and rows[b"python_image_sha256"]==PY_SHA)
  need(rows[b"libc_path_hex"]==ctx[b"libc_path_hex"] and rows[b"libc_confstr_hex"]==ctx[b"libc_confstr_hex"])
  need(udec(rows[b"libc_bytes"],1)==ctx[b"libc_bytes"] and rows[b"libc_sha256"]==ctx[b"libc_sha"])
  need(rows[b"backend_surface"]==b"posix-posix_spawn" and rows[b"spawn_premise_satisfied"]==b"0")
 elif probe==b"P01C":
  prior=ctx[b"p01d"];need(rows[b"libc_path_hex"]==prior[b"libc_path_hex"] and rows[b"libc_sha256"]==prior[b"libc_sha256"] and rows[b"libc_confstr_hex"]==prior[b"libc_confstr_hex"] and rows[b"spawn_premise_satisfied"]==b"1")
  pids=csv_values(rows[b"child_pids"],False,1);need(csv_values(rows[b"child_statuses"],True,1)==(0,))
  child_observation(payload_item(even_hex(rows[b"child_raw_hex"]),b"INFO"),b"INFO",pids[0],SOURCE_META[4][2],ctx[b"cwd_hex"],b"terminal")
 elif probe==b"P02":need(tuple(rows[x] for x in PREFIX[probe])==(b"0,1,2,5,6",b"10",ctx[b"cwd_hex"],b"isolated:1,ignore_environment:1,no_site:1,no_user_site:1,dont_write_bytecode:1,safe_path:1,utf8_mode:1,hash_randomization:1"))
 elif probe==b"P03":need(tuple(rows[x] for x in PREFIX[probe])==(b"4096",b"1048576",b"64",b"59",b"1"))
 elif probe==b"P04":need(udec(rows[b"valid_signal_count"])==ctx[b"valid_signals"] and udec(rows[b"default_signal_count"])==ctx[b"default_signals"] and rows[b"defaults_sha256"]==ctx[b"defaults_sha"] and rows[b"mask_empty"]==b"1")
 elif probe==b"P05":
  need(rows[b"wnohang_zero"]==rows[b"eintr"]==rows[b"echild"]==b"1" and rows[b"term_signal"]==b"15")
  pids=csv_values(rows[b"child_pids"],False,2);statuses=csv_values(rows[b"raw_statuses"],True,2);need(statuses==(23<<8,15))
  parts=payload_item(even_hex(rows[b"broker_payload_hex"]),b"P05").splitlines(True);need(len(parts)==2)
  child_observation(parts[0],b"EXIT23",pids[0],SOURCE_META[4][2],ctx[b"cwd_hex"],b"ready")
  child_observation(parts[1],b"TERM",pids[1],SOURCE_META[4][2],ctx[b"cwd_hex"],b"ready")
 elif probe==b"P06":need(rows[b"monotonic"]==b"1" and udec(rows[b"observed_min_delta_ns"],1)>0 and udec(rows[b"start_ns"])<=udec(rows[b"end_ns"]) and rows[b"deadline_checked"]==b"1")
 elif probe==b"P07":need(tuple(rows[x] for x in PREFIX[probe])==(b"1",b"0",b"1"))
 elif probe==b"P08":
  pids=csv_values(rows[b"child_pids"],False,1);need(csv_values(rows[b"raw_statuses"],True,1)==(0,) and rows[b"same_session_group"]==rows[b"post_pid_esrch"]==b"1")
  child_observation(payload_item(even_hex(rows[b"broker_payload_hex"]),b"P08"),b"BLOCK0",pids[0],SOURCE_META[4][2],ctx[b"cwd_hex"],b"ready")
 elif probe==b"P09":
  csv_values(rows[b"child_pids"],False,1);need(csv_values(rows[b"raw_statuses"],True,1)==(9,) and rows[b"signal"]==b"9" and rows[b"reaped"]==b"1")
  start=udec(rows[b"reap_start_ns"]);finish=udec(rows[b"reap_end_ns"]);need(start<=finish and finish-start<=100000000)
 elif probe==b"P10":
  pids=csv_values(rows[b"pids"],False,16);need(rows[b"sample_count"]==b"16" and csv_values(rows[b"statuses"],True,16)==(0,)*16)
  need(udec(rows[b"pid_duplicates"])==16-len(set(pids)) and rows[b"group_is_single_owned_launcher_group"]==b"1" and rows[b"reuse_proof"]==b"0")
 elif probe==b"P11":need(tuple(rows[x] for x in PREFIX[probe])==(b"OK",b"1",b"1",b"1",b"0",b"1"))
 elif probe==b"P12":
  pids=csv_values(rows[b"child_pids"],False,1);need(csv_values(rows[b"raw_statuses"],True,1)==(0,) and rows[b"environment_count"]==b"10" and rows[b"underscore_absent"]==b"1" and rows[b"real_payload_invoked"]==b"0")
  child_observation(payload_item(even_hex(rows[b"broker_payload_hex"]),b"CHAIN"),b"CHAIN",pids[0],SOURCE_META[4][2],ctx[b"cwd_hex"],b"terminal")
 elif probe==b"P13":need(tuple(rows[x] for x in PREFIX[probe])==(b"1",b"1",b"1",b"1",b"1",b"1",b"0",b"0"))
 else:need(False)

def transcript_structure(raw,probe):
 ascii_file(raw,STREAM_CAP);lines=raw[:-1].split(b"\n")
 need(lines and all(lines) and lines[0]==TAG+b"|marker=report|schema=15|probe="+probe)
 keys=PREFIX[probe]+COMMON;need(len(lines)==len(keys)+4);rows={}
 for key,line in zip(keys,lines[1:1+len(keys)]):
  prefix=TAG+b"|probe="+probe+b"|"+key+b"=";need(line.startswith(prefix) and key not in rows)
  value=line[len(prefix):];need(value and b"|" not in value and b"=" not in value);rows[key]=value
 need(lines[1+len(keys)]==TAG+b"|probe="+probe+b"|result=PASS")
 candidate=parse_outer(lines[2+len(keys)],probe,False);terminal=parse_outer(lines[3+len(keys)],probe,True)
 need(candidate==terminal);return rows,candidate

def transcript_semantics(rows,candidate,probe,ctx):
 need(candidate[b"launcher"]==15 and candidate[b"keeper"]==15 and candidate[b"marker"]==0)
 start=udec(rows[b"probe_start_ns"]);finish=udec(rows[b"probe_finish_ns"]);elapsed=udec(rows[b"probe_elapsed_ns"])
 need(start<=finish and finish-start==elapsed and elapsed<=OP_NS and rows[b"probe_bound_ns"]==b"15000000000")
 need(rows[b"primary_failure"]==b"none" and rows[b"cleanup_failure"]==b"none" and rows[b"result"]==b"PASS")
 need(udec(rows[b"marker_image_dev"],1)==ctx[b"python_dev"] and udec(rows[b"marker_image_ino"],1)==ctx[b"python_ino"] and rows[b"marker_image_sha256"]==PY_SHA)
 validate_probe(rows,probe,ctx);expected=-1
 if probe==b"P00":expected=-1 if rows[b"broker_spawned"]==b"0" else 0
 elif probe in (b"P01C",b"P08",b"P10",b"P12"):expected=0
 elif probe==b"P05":expected=15
 elif probe==b"P09":expected=9
 need(candidate[b"child"]==expected);return rows

V19_EXTERNAL_GATES=(
 b"CLONE3_CPYTHON",b"DELETED_CGROUP_FD",
 b"SEALED_SNAPSHOT_CONSTRUCTION",b"EXTERNAL_SURVIVAL",
 b"OUTER_RECONCILER",b"ISSUER_CRYPTOGRAPHY",
)
V19_PHYSICAL_STATES=(b"CLOSED",b"ACQUIRING",b"OWNED",b"CLOSE_RETRY")
V19_RAW_STATES=(b"EMPTY",b"LOCAL_RAW",b"SHADOW_OF_RECORD",b"DISARMED")
V19_ENDPOINT_STATES=(b"NO_WRAPPER",b"ATTACHED",b"DETACH_REQUESTED",b"DETACHED",b"PROVED_CLOSED")
V19_POLLER_STATES=(b"FREE",b"REGISTERING",b"ACTIVE",b"UNREGISTER_RETRY",b"INACTIVE")
V19_CLOSURE_PHASES=(b"NOT_STARTED",b"ACTIVE",b"CLOSED",b"RELEASED")
V19_CLOSURE_MODES=(b"GENERIC_ACCEPTED",b"REFUSAL_ACCEPTED",b"DIRECT")
V19_OUTER_STATES=(b"PRE_READY",b"PRE_READY_OFFER_FROZEN",b"POST_OFFER_READY_RETAINED",b"ACCEPTED_RETAINED",b"ACCEPTED_RECEIVED_THEN_CLOSED",b"CLOSED_OMITTED")
V19_RECEIVE_SITE_SPEC=(
 (b"ACTOR_CONTROL",4,5),(b"WATCHDOG_MONITORED",4,5),
 (b"EXTERNAL_CONTROL",13,14),(b"EXTERNAL_RECEIPT",13,14),
 (b"REFUSAL_CONTROL",4,5),
)
V19_OFFERED_SLOTS=(
 b"attempt",b"attempt_base_fd",b"stage_fd",b"cgfd",b"root_events_fd",
 b"root_kill_fd",b"out_fd",b"err_fd",b"events_fd",b"outer_pidfd",
 b"cgroup_base_fd",b"actor_control_fd",b"pending_expected_raw_fd",
)
V19_SAFE_LOCAL_SLOTS=(
 b"transfer_control_fd",b"actor_pidfd_fd",b"external_owner_pidfd_fd",
 b"certificate_carrier_fd",b"envelope_carrier_fd",b"snapshot_carrier_fd",
 b"plan_carrier_fd",b"actor_source_carrier_fd",b"host_source_carrier_fd",
 b"reservation_carrier_fd",b"external_manifest_carrier_fd",
 b"watchdog_source_carrier_fd",
)
V19_RECORD_DELTA_KINDS=(
 b"INTENT",b"RELEASE",b"VALIDATED",b"ACK_INTENT",b"COMMITTED",
 b"COMMITTED_SEEN",b"KILL_TICKET",b"RETAINED",b"RECOVERY",
 b"FAILURE_REPORT",b"TERMINAL_CANDIDATE",b"TERMINAL_SEEN",
 b"SUCCESS_REPORT",b"PASS_COMMIT",b"ACK_RECEIPT",b"RECONCILIATION",
 b"OWNER_CLOSURE",
)
V19_RECORD_DELTA_GRAMMAR_RAW=b'RECORD_DELTA_KINDS=(b"INTENT",b"RELEASE",b"VALIDATED",b"ACK_INTENT",b"COMMITTED",b"COMMITTED_SEEN",b"KILL_TICKET",b"RETAINED",b"RECOVERY",b"FAILURE_REPORT",b"TERMINAL_CANDIDATE",b"TERMINAL_SEEN",b"SUCCESS_REPORT",b"PASS_COMMIT",b"ACK_RECEIPT",b"RECONCILIATION",b"OWNER_CLOSURE")'
V19_PHYSICAL_RECORD_FIELDS=(
 "record_id","home_role","state","semantic_role","raw_fd","identity","physical_identity","leaf_identity","verified_kill_leaf_identity",
 "access","provenance","endpoint_state","wrapper_ref","detached_raw_fd",
 "wrapper_phase","wrapper_local_fallback","wrapper_probe_done","wrapper_detach_attempted","raw_cell","epoch",
)
V19_RAW_CELL_FIELDS=("cell_id","state","c_value","record_id","epoch")
V19_POLLER_CELL_FIELDS=("cell_id","state","poller","record_id","raw_fd","mask","epoch")
V19_ACTOR_RECEIVE_FRAME_FIELDS=(
 "site","semantic_capacity","installed_capacity","ancillary_bytes","kernel_control_bytes",
 "payload","control","iov","hdr","header_views","int_views","raw_cells",
 "quarantine_records","provenances","installed_count","payload_count","msg_flags",
 "capture_complete","validation_complete","capture_fault","cleanup_cursor","cleanup_pending","original_fault","epoch",
)

def v19_raw_slice_v19(raw,start,end):
 need(raw.count(start)==1 and raw.count(end)==1)
 left,tail=raw.split(start);body,right=tail.split(end)
 need(left is not None and body and right is not None);return body

def v19_raw_order_v19(raw,pieces):
 cursor=-1
 for piece in pieces:
  need(type(piece)is bytes and raw.count(piece)>=1)
  position=raw.index(piece,cursor+1);need(position>cursor);cursor=position
 return True

def v19_validate_raw_contract(actor_raw,watchdog_raw):
 need(type(actor_raw)is bytes and type(watchdog_raw)is bytes)
 validator_begin=b"# P27 RUNNER V20 EMBEDDED "+b"VALIDATOR BEGIN 8E20B7D2\n"
 validator_end=b"# P27 RUNNER V20 EMBEDDED "+b"VALIDATOR END 8E20B7D2\n"
 need(actor_raw.count(validator_begin)==actor_raw.count(validator_end)==1)
 actor_prefix,actor_tail=actor_raw.split(validator_begin);validator_body,actor_suffix=actor_tail.split(validator_end)
 need(validator_body and actor_prefix and actor_suffix);actor_surface=actor_prefix+actor_suffix
 actor_marker=b"# P27 RUNNER V19 ACTOR FINAL ENTRY BEGIN 19A0C701\n"
 watch_marker=b"# P27 RUNNER V19 WATCHDOG FINAL ENTRY BEGIN 19B0C702\n"
 need(actor_surface.count(actor_marker)==1 and watchdog_raw.count(watch_marker)==1)
 actor_entry=actor_surface.split(actor_marker)[1];watch_entry=watchdog_raw.split(watch_marker)[1]
 for forbidden in (b".logical_role",b".logical_slot",b"record.transferable",b"source.transferable",b"record.transfer_order",b"source.transfer_order"):
  need(forbidden not in actor_entry and forbidden not in watch_entry)
 need(actor_entry.count(b"def actor_begin_acquisition(role,kind):")==1)
 actor_begin=v19_raw_slice_v19(actor_entry,b"def actor_begin_acquisition(role,kind):\n",b"def actor_capture_cell_v19")
 v19_raw_order_v19(actor_begin,(b"record.state=b\"ACQUIRING\"",b"actor_raw_prearm_v19",b"except BaseException:",b"actor_record_reset_closed_v19(record)",b"raise"))
 need(actor_begin.count(b"except BaseException:")==1)
 pair=v19_raw_slice_v19(actor_entry,b"def actor_capture_authoritative_c_v19",b"def actor_wrapper_adopt_v19")
 need(pair.count(b"def actor_capture_authoritative_c_v19")==1 and pair.count(b"actor_capture_authoritative_c_v19(")==3)
 need(b"left_cell.c_value" not in pair and b"right_cell.c_value" not in pair and b"actor_pair_scan" not in pair)
 v19_raw_order_v19(pair,(b"record.raw_fd=number;record.state=b\"ACQUIRING\"",b"shadow=record.raw_cell",b"finally:actor_reconcile_pair_outputs_v19(left,right,cells)"))
 clone=v19_raw_slice_v19(actor_entry,b"def actor_clone3_boundary_v19",b"def launch_outer")
 need(b"finally:actor_capture_authoritative_c_v19(record,ACTOR_CLONE3_PIDFD_OUT_V19)" in clone)
 need(b"cell.c_value.value=ACTOR_CLONE3_PIDFD_OUT_V19.value" not in clone)
 actor_wrapper=v19_raw_slice_v19(actor_entry,b"def actor_wrapper_adopt_v19",b"def actor_role_for_record_v19")
 v19_raw_order_v19(actor_wrapper,(b"wrapper=socket.socket.__new__(socket.socket)",b"record.wrapper_ref=wrapper",b"socket.socket.__init__(wrapper,fileno=record.raw_fd)"))
 actor_repair=v19_raw_slice_v19(actor_entry,b"def actor_reconcile_wrapper_v19",b"def actor_close_record")
 need(actor_repair.count(b"wrapper.fileno()")==1 and actor_repair.count(b"wrapper.detach()")==1)
 actor_promote=v19_raw_slice_v19(actor_entry,b"def actor_promote_record",b"def actor_reconcile_pollers_v19")
 need(actor_promote.count(b"source.semantic_role=new_role")==1)
 v19_raw_order_v19(actor_promote,(b"prepared_provenance=",b"actor_identity_revalidate_v19(source)",b"source.provenance=prepared_provenance",b"source.semantic_role=new_role",b"source.state=b\"OWNED\""))
 actor_boot=v19_raw_slice_v19(actor_entry,b"def actor_bootstrap_registry",b"def actor_close_all")
 v19_raw_order_v19(actor_boot,(b"actor_capture_cell_v19",b"actor_finish_adoption(role)",b"record.physical_identity is not None"))
 need(b"record.state=b\"OWNED\"" not in actor_boot.split(b"actor_finish_adoption(role)")[0])
 watch_begin=v19_raw_slice_v19(watch_entry,b"def lifecycle_begin_acquisition(context,slot,kind,transferable,provenance):\n",b"def lifecycle_capture_cell_v19")
 v19_raw_order_v19(watch_begin,(b"record.state=b\"ACQUIRING\"",b"cell.c_value.value=-1",b"except BaseException:",b"watchdog_record_reset_v19(record)",b"raise"))
 watch_wrapper=v19_raw_slice_v19(watch_entry,b"def watchdog_wrapper_adopt_v19",b"def bind_lifecycle_endpoint")
 v19_raw_order_v19(watch_wrapper,(b"wrapper=socket.socket.__new__(socket.socket)",b"record.wrapper_ref=wrapper",b"socket.socket.__init__(wrapper,fileno=record.raw_fd)"))
 watch_repair=v19_raw_slice_v19(watch_entry,b"def watchdog_endpoint_repair_v19",b"def lifecycle_mark_closed_v19")
 need(watch_repair.count(b"wrapper.fileno()")==1 and watch_repair.count(b"wrapper.detach()")==1)
 watch_promote=v19_raw_slice_v19(watch_entry,b"def promote_lifecycle_fd",b"def register_lifecycle_poller")
 need(watch_promote.count(b"source.semantic_role=new_slot")==1)
 v19_raw_order_v19(watch_promote,(b"frame_binding=",b"prepared_provenance=",b"lifecycle_bind_identity_v19(source)",b"source.provenance=",b"source.semantic_role=new_slot",b"source.state=b\"OWNED\""))
 watch_boot=v19_raw_slice_v19(watch_entry,b"def bootstrap_lifecycle_registry",b"def watchdog_entry_limit_transition_v19")
 v19_raw_order_v19(watch_boot,(b"lifecycle_capture_cell_v19",b"lifecycle_finish_adoption(context,slot)",b"record.physical_identity is not None"))
 need(b"record.state=b\"OWNED\"" not in watch_boot.split(b"lifecycle_finish_adoption(context,slot)")[0])
 need(watch_entry.count(b"V19_WIRE_ROLE_SPEC=tuple(")==1 and watch_entry.count(b"def v19_wire_row_v19")==1)
 wire=v19_raw_slice_v19(watch_entry,b"def v19_wire_row_v19",b"def v19_parse_wire_row_v19")
 need(b"record_id" not in wire)
 for field in (b"b\"I=\"",b"b\".R=\"",b"b\".K=\"",b"b\".H=\"",b"b\".A=\"",b"b\".D=\""):
  need(field in wire)
 receiver=v19_raw_slice_v19(watch_entry,b"def v19_receiver_proof_v19",b"V19_WATCHDOG_MINIMAL_CONTEXT_STAGE3")
 need(receiver.count(b"v19_receiver_wire_set_v19")==3)
 census=v19_raw_slice_v19(watch_entry,b"def v19_populate_census",b"def v19_copy_ids")
 need(b"mode=b\"ZERO_RIGHTS\" if refusal else b\"GENERIC_13\"" in census)
 need(b"if refusal:" in census and b"census.offered.count==0" in census)
 boundary=v19_raw_slice_v19(watch_entry,b"def v19_offer_census_boundary",b"def unique_kill_authority")
 need(b"wire_rows=v19_wire_rows_from_caps_v19(caps)" in boundary)
 need(b"cache.frozen_wire_rows=wire_rows" in boundary and b"wire_rows==cache.frozen_wire_rows" in boundary)
 need(b"cap_record_ids" in boundary and b"record_id" not in v19_raw_slice_v19(watch_entry,b"def v19_wire_row_v19",b"def v19_receiver_wire_set_v19"))
 ready=v19_raw_slice_v19(watch_entry,b"def apply_offer_readiness",b"def promote_later_offer_readiness")
 frozen=ready.split(b"if cache.state==b\"FROZEN\" and cache.atomic_authority is not None:")[1].split(b"need(cache.atomic_authority is None")[0]
 for forbidden in (b"close_lifecycle_fd",b"discard_unactivated",b"prepared_sequence",b"store_offer",b"v19_offer_census_boundary"):
  need(forbidden not in frozen)
 need(b"context[b\"outer_pidfd_offer_state\"]=b\"POST_OFFER_READY_RETAINED\"" in frozen)
 later=v19_raw_slice_v19(watch_entry,b"def promote_later_offer_readiness",b"def prepare_outer_pidfd_offer_binding")
 need(b"close_lifecycle_fd" not in later and b"discard_unactivated" not in later)
 acceptance=v19_raw_slice_v19(watch_entry,b"def v19_prepare_acceptance_v19",b"V15_VERIFY_EXTERNAL_ACCEPTANCE_V19")
 need(b"frozen_wire=cache.frozen_wire_rows" in acceptance)
 need(b"frozen_wire==installed==current_retained==receiver_kill==()" in acceptance)
 builder=v19_raw_slice_v19(watch_entry,b"def v19_build_refusal_preclose_v19",b"def v19_refusal_preclose_once_v19")
 v19_raw_order_v19(builder,(b"immutable_packet=packet(",b"cell.preclose_packet=immutable_packet",b"cell.preclose_sequence=core[0]",b"cell.preclose_deadline=actor_close_deadline"))
 preclose=v19_raw_slice_v19(watch_entry,b"def v19_refusal_preclose_once_v19",b"def v19_closure_driver")
 need(preclose.count(b"send_exact(")==1)
 v19_raw_order_v19(preclose,(b"checkpoint(CERT,0,cell.preclose_deadline)",b"cell.preclose_state=b\"POSSIBLE\"",b"cell.preclose_send_latch=True",b"send_exact(control,cell.preclose_packet,cell.preclose_deadline)"))
 driver=v19_raw_slice_v19(watch_entry,b"def v19_closure_driver",b"def close_ownership_capabilities")
 v19_raw_order_v19(driver,(b"if cell.mode==b\"REFUSAL_ACCEPTED\":v19_build_refusal_preclose_v19(context,cell)",b"cell.phase=b\"ACTIVE\"",b"if cell.phase==b\"ACTIVE\":"))
 active=driver.split(b"if cell.phase==b\"ACTIVE\":")[1].split(b"if cell.phase==b\"CLOSED\":")[0]
 need(b"packet(" not in active and b"preclose_sequence=" not in active and b"EXTERNAL_RECV_SEQ=" not in active)
 need(active.count(b"v19_refusal_preclose_once_v19(context,cell)")==1)
 for function_name in (b"actor_begin_acquisition",b"actor_promote_record",b"actor_clone3_boundary_v19"):
  need(actor_entry.count(b"def "+function_name+b"(")==1)
 for function_name in (b"lifecycle_begin_acquisition",b"promote_lifecycle_fd",b"apply_offer_readiness",b"v19_prepare_acceptance_v19",b"v19_closure_driver"):
  need(watch_entry.count(b"def "+function_name+b"(")==1)
 need(actor_entry.count(b"v19_validate_actor_control_surface()")==1)
 need(watch_entry.count(b"\n v19_validate_watchdog_control_surface()\n")==1)
 need(actor_entry.count(b"ACTOR_SIMULTANEOUS_LIVE_ROLE_SET_V19=ACTOR_SIMULTANEOUS_RECORD_ROLES_V19+ACTOR_SIMULTANEOUS_INTAKE_ROLES_V19+ACTOR_SIMULTANEOUS_C_OUTPUT_ROLES_V19")==1)
 need(watch_entry.count(b"WATCHDOG_SIMULTANEOUS_LIVE_ROLE_SET_V19=WATCHDOG_SIMULTANEOUS_RECORD_ROLES_V19+WATCHDOG_SIMULTANEOUS_MAX_INTAKE_ROLES_V19+WATCHDOG_SIMULTANEOUS_WRAPPER_FALLBACK_V19")==1)
 need(watchdog_raw.count(V19_RECORD_DELTA_GRAMMAR_RAW)==1)
 need(V19_RECORD_DELTA_KINDS==(b"INTENT",b"RELEASE",b"VALIDATED",b"ACK_INTENT",b"COMMITTED",b"COMMITTED_SEEN",b"KILL_TICKET",b"RETAINED",b"RECOVERY",b"FAILURE_REPORT",b"TERMINAL_CANDIDATE",b"TERMINAL_SEEN",b"SUCCESS_REPORT",b"PASS_COMMIT",b"ACK_RECEIPT",b"RECONCILIATION",b"OWNER_CLOSURE"))
 return True

V20_NEGATIVE_RAW_FIXTURES=(
 (b"BEGIN",b"actor_record_reset_closed_v19(record)\ntry:\nrecord.state=b\"ACQUIRING\""),
 (b"WRAPPER",b"phase=b\"DETACH_EFFECT_UNKNOWN\"\nwrapper.detach()"),
 (b"FROZEN",b"state=b\"FROZEN\"\ncontext[b\"outer_offer_binding\"]=None\nreturn external_transfer(control,context,reason)"),
 (b"ORDER",b"pending_expected_raw_fd\nactor_control_fd"),
 (b"SEQUENCE",b"immutable_packet=packet(\npreclose_sequence=core[0]\ncell.phase=b\"ACTIVE\""),
)
V20_POSITIVE_RAW_FIXTURES=(
 (b"BEGIN",b"try:\nactor_record_reset_closed_v19(record)\nrecord.state=b\"ACQUIRING\"\nexcept BaseException:\nactor_partial_begin_reconcile_v20(record,role)"),
 (b"WRAPPER",b"phase==b\"DETACH_EFFECT_UNKNOWN\"\nDETACH_POSTCONDITION_POSSIBLE\nwrapper.fileno()\nDETACH_OBSERVED_ATTACHED\nDETACH_RETRY_IN_PROGRESS"),
 (b"FROZEN",b"state==b\"FROZEN\"\nv20_frozen_binding=context[b\"outer_offer_binding\"]\napply_offer_readiness\ncontext[b\"outer_offer_binding\"] is v20_frozen_binding"),
 (b"ORDER",b"actor_control_fd\npending_expected_raw_fd"),
 (b"SEQUENCE",b"next_control_sequence=CONTROL_SEND_SEQ+1\nv20_packet_without_sequence_commit\ncell.preclose_sequence=preclose_sequence\nCONTROL_SEND_SEQ=next_control_sequence\ncell.phase=b\"ACTIVE\""),
)

def v20_fixture_accepts_v20(kind,raw):
 need(type(kind)is bytes and type(raw)is bytes)
 if kind==b"BEGIN":
  return b"try:" in raw and raw.index(b"try:")<raw.index(b"actor_record_reset_closed_v19(record)")<raw.index(b"record.state=b\"ACQUIRING\"") and b"actor_partial_begin_reconcile_v20" in raw
 if kind==b"WRAPPER":
  return b"DETACH_POSTCONDITION_POSSIBLE" in raw and b"wrapper.fileno()" in raw and b"DETACH_RETRY_IN_PROGRESS" in raw and raw.index(b"DETACH_POSTCONDITION_POSSIBLE")<raw.index(b"wrapper.fileno()")<raw.index(b"DETACH_RETRY_IN_PROGRESS")
 if kind==b"FROZEN":
  return b"state==b\"FROZEN\"" in raw and b"v20_frozen_binding" in raw and b"apply_offer_readiness" in raw and b"outer_offer_binding\"]=None" not in raw and b"return external_transfer" not in raw
 if kind==b"ORDER":
  return b"actor_control_fd" in raw and b"pending_expected_raw_fd" in raw and raw.index(b"actor_control_fd")<raw.index(b"pending_expected_raw_fd")
 if kind==b"SEQUENCE":
  return b"next_control_sequence=CONTROL_SEND_SEQ+1" in raw and b"v20_packet_without_sequence_commit" in raw and b"preclose_sequence=core[0]" not in raw and b"CONTROL_SEND_SEQ=next_control_sequence" in raw
 need(False)

def v20_raw_last_between_v20(raw,start,end):
 need(type(raw)is bytes and raw.count(start)>=1)
 tail=raw.rsplit(start,1)[1];need(end in tail)
 body=tail.split(end,1)[0];need(body)
 return body

def v19_validate_raw_contract(actor_raw,watchdog_raw):
 need(type(actor_raw)is bytes and type(watchdog_raw)is bytes)
 validator_begin=b"# P27 RUNNER V20 EMBEDDED VALIDATOR BEGIN 8E20B7D2\n"
 validator_end=b"# P27 RUNNER V20 EMBEDDED VALIDATOR END 8E20B7D2\n"
 need(actor_raw.count(validator_begin)==actor_raw.count(validator_end)==1)
 actor_prefix,actor_tail=actor_raw.split(validator_begin);validator_body,actor_suffix=actor_tail.split(validator_end)
 need(validator_body and actor_prefix and actor_suffix);actor_surface=actor_prefix+actor_suffix
 for kind,raw in V20_NEGATIVE_RAW_FIXTURES:need(not v20_fixture_accepts_v20(kind,raw))
 for kind,raw in V20_POSITIVE_RAW_FIXTURES:need(v20_fixture_accepts_v20(kind,raw))

 actor_begin=v20_raw_last_between_v20(actor_surface,b"def actor_begin_acquisition(role,kind):\n",b"def actor_pair_boundary_v19")
 v19_raw_order_v19(actor_begin,(b"record=None\n try:",b"actor_record_reset_closed_v19(record)",b"record.state=b\"ACQUIRING\"",b"actor_raw_prearm_v19",b"except BaseException:",b"actor_partial_begin_reconcile_v20(record,role)",b"raise"))
 need(b"actor_record_reset_closed_v19(record)\n try:" not in actor_begin)
 pair=v20_raw_last_between_v20(actor_surface,b"def actor_pair_boundary_v19",b"def actor_wrapper_observe_v20")
 v19_raw_order_v19(pair,(b"try:",b"cells[0]=-1;cells[1]=-1",b"left=actor_begin_acquisition",b"right=actor_begin_acquisition",b"finally:",b"actor_reconcile_pair_outputs_v19(left,right,cells)"))
 clone=v20_raw_last_between_v20(actor_surface,b"def actor_clone3_boundary_v19",b"\ntry:\n main()")
 v19_raw_order_v19(clone,(b"try:",b"ACTOR_CLONE3_PIDFD_OUT_V19.value=-1",b"record=actor_begin_acquisition",b"LIBC.syscall",b"finally:",b"actor_capture_authoritative_c_v19(record,ACTOR_CLONE3_PIDFD_OUT_V19)"))
 actor_repair=v20_raw_last_between_v20(actor_surface,b"def actor_reconcile_wrapper_v19",b"def actor_wrapper_adopt_v19")
 need(b"if phase==b\"DETACH_EFFECT_UNKNOWN\":" in actor_repair and b"if phase==b\"DETACH_RETRY_EFFECT_UNKNOWN\":" in actor_repair)
 v19_raw_order_v19(actor_repair,(b"if phase==b\"DETACH_EFFECT_UNKNOWN\":",b"DETACH_POSTCONDITION_POSSIBLE",b"DETACH_OBSERVED_ATTACHED",b"actor_wrapper_detach_attempt_v20(record,wrapper,True)"))
 need(b"RETAINED_ATTACHED_NO_RETRY" in actor_repair and b"sole-authority-retained-no-uncontrolled-retry" in actor_repair)
 actor_wrapper=v20_raw_last_between_v20(actor_surface,b"def actor_wrapper_adopt_v19",b"def actor_clone3_boundary_v19")
 v19_raw_order_v19(actor_wrapper,(b"wrapper=socket.socket.__new__",b"record.wrapper_ref=wrapper",b"CONSTRUCTOR_IN_PROGRESS",b"socket.socket.__init__",b"ATTACH_VERIFY_POSSIBLE",b"observed=wrapper.fileno()"))
 need(b"ATTACH_VERIFY_UNKNOWN" in actor_wrapper and b"CONSTRUCTOR_EFFECT_UNKNOWN" in actor_wrapper)

 watch_begin=v20_raw_last_between_v20(watchdog_raw,b"def lifecycle_begin_acquisition(context,slot,kind,transferable,provenance):\n",b"def watchdog_wrapper_observe_v20")
 v19_raw_order_v19(watch_begin,(b"record=None\n try:",b"watchdog_record_reset_v19(record)",b"record.state=b\"ACQUIRING\"",b"cell.state=b\"EMPTY\"",b"except BaseException:",b"watchdog_partial_begin_reconcile_v20(record,slot)",b"raise"))
 need(b"watchdog_record_reset_v19(record)\n try:" not in watch_begin)
 watch_repair=v20_raw_last_between_v20(watchdog_raw,b"def watchdog_endpoint_repair_v19",b"def watchdog_wrapper_adopt_v19")
 v19_raw_order_v19(watch_repair,(b"if phase==b\"DETACH_EFFECT_UNKNOWN\":",b"DETACH_POSTCONDITION_POSSIBLE",b"DETACH_OBSERVED_ATTACHED",b"watchdog_wrapper_detach_attempt_v20(record,wrapper,True)"))
 need(b"DETACH_RETRY_POSTCONDITION_POSSIBLE" in watch_repair and b"RETAINED_ATTACHED_NO_RETRY" in watch_repair)
 watch_wrapper=v20_raw_last_between_v20(watchdog_raw,b"def watchdog_wrapper_adopt_v19",b"def v20_live_canonical_offered_slots")
 v19_raw_order_v19(watch_wrapper,(b"wrapper=socket.socket.__new__",b"record.wrapper_ref=wrapper",b"CONSTRUCTOR_IN_PROGRESS",b"socket.socket.__init__",b"ATTACH_VERIFY_POSSIBLE",b"observed=wrapper.fileno()"))

 transfer_parts=watchdog_raw.split(b"def external_transfer(control,context,reason):\n")
 need(len(transfer_parts)==3)
 frozen_caller=transfer_parts[1].split(b"def freeze_failure_deadlines",1)[0]
 mismatch=frozen_caller.split(b"if final_snapshot!=expected_snapshot:",1)[1].split(b"  else:\n   context[b\"transfer_offer_cache\"]",1)[0]
 for forbidden in (b"context[b\"outer_offer_binding\"]=None",b"return external_transfer(control,context,reason)",b"discard_unactivated",b"close_lifecycle_fd"):
  need(forbidden not in mismatch)
 v19_raw_order_v19(mismatch,(b"v20_frozen_cache.state==b\"FROZEN\"",b"v20_frozen_binding=context[b\"outer_offer_binding\"]",b"v20_frozen_full=",b"v20_frozen_offered=",b"apply_offer_readiness",b"context[b\"outer_offer_binding\"] is v20_frozen_binding",b"POST_OFFER_READY_RETAINED",b"v20_frozen_cache.prepared_sequence==v20_frozen_sequence"))

 role_order=v20_raw_last_between_v20(watchdog_raw,b"WATCHDOG_CANONICAL_OFFERED_ROLE_ORDER_V20=(",b")\nWATCHDOG_WRAPPER_MONOTONE_PHASES_V20")
 need(role_order.index(b"actor_control_fd")<role_order.index(b"pending_expected_raw_fd"))
 ownership=v20_raw_last_between_v20(watchdog_raw,b"def ownership_transfer_keys(context):\n",b"def external_capabilities")
 v19_raw_order_v19(ownership,(b"for slot in v20_live_canonical_offered_slots(context):",b"rows.append",b"tuple(row[1] for row in rows)==v20_live_canonical_offered_slots(context)",b"return tuple(rows)"))
 need(b"rows.sort" not in ownership and b"EXTERNAL_RIGHTS_ORDER.index" not in ownership)
 census=v20_raw_last_between_v20(watchdog_raw,b"def v19_populate_census(context,census,phase,refusal=False):\n",b"\ntry:\n main()")
 need(b"mode=b\"ZERO_RIGHTS\" if refusal else b\"GENERIC_13\"" in census)
 need(b"if role==b\"actor_control_fd\":" in census and b"if refusal_guard:census.safe_local.add(record.record_id)" in census and b"else:census.blocking.add(record.record_id)" in census)
 v19_raw_order_v19(census,(b"if not refusal:",b"for role in v20_live_canonical_offered_slots(context):",b"census.offered.add",b"census.offered.exact_tuple()==tuple"))
 boundary=v20_raw_last_between_v20(watchdog_raw,b"def v19_offer_census_boundary",b"def unique_kill_authority")
 need(b"cap_record_ids==census.offered.exact_tuple()" in boundary and b"wire_rows==cache.frozen_wire_rows" in boundary)
 wire=v19_raw_slice_v19(watchdog_raw,b"def v19_wire_row_v19",b"def v19_parse_wire_row_v19")
 need(b"record_id" not in wire and all(field in wire for field in (b"b\"I=\"",b"b\".R=\"",b"b\".K=\"",b"b\".H=\"",b"b\".A=\"",b"b\".D=\"")))

 packet_candidate=v19_raw_slice_v19(watchdog_raw,b"def v20_packet_without_sequence_commit",b"def v20_prepare_closure_candidate")
 need(b"global CONTROL_SEND_SEQ" not in packet_candidate and b"CONTROL_SEND_SEQ+=" not in packet_candidate)
 need(b"message_sequence==CONTROL_SEND_SEQ+1" in packet_candidate and b"message_seq=" in packet_candidate)
 prepare=v19_raw_slice_v19(watchdog_raw,b"def v20_prepare_closure_candidate",b"def v20_install_closure_candidate")
 need(b"preclose_sequence=core[0]" not in prepare and b"immutable_packet=packet(" not in prepare)
 v19_raw_order_v19(prepare,(b"plan_ids=[]",b"next_control_sequence=CONTROL_SEND_SEQ+1",b"v20_packet_without_sequence_commit",b"preclose_packet_sha=sha(preclose_packet)",b"preclose_sequence=next_control_sequence",b"latch_candidate=",b"return (b\"V20_COMPLETE_IMMUTABLE_CLOSURE_CANDIDATE\""))
 install=v19_raw_slice_v19(watchdog_raw,b"def v20_install_closure_candidate",b"def v19_build_refusal_preclose_v19")
 need(b"packet(" not in install and b"checkpoint(" not in install and b"need(" not in install)
 v19_raw_order_v19(install,(b"cell.plan=plan",b"cell.preclose_packet=preclose_packet",b"cell.preclose_sequence=preclose_sequence",b"CONTROL_SEND_SEQ=next_control_sequence",b"cell.phase=b\"ACTIVE\""))
 driver=v20_raw_last_between_v20(watchdog_raw,b"def v19_closure_driver",b"def close_ownership_capabilities")
 not_started=driver.split(b"if cell.phase==b\"NOT_STARTED\":",1)[1].split(b"if cell.phase==b\"ACTIVE\":",1)[0]
 need(b"v20_prepare_closure_candidate" in not_started and b"v20_install_closure_candidate" in not_started)
 for forbidden in (b"packet(",b"CONTROL_SEND_SEQ=",b"preclose_sequence=core[0]",b"v19_build_refusal_preclose_v19"):
  need(forbidden not in not_started)
 need(b"if repair_cell.phase==b\"NOT_STARTED\":raise" in driver)
 preclose=v19_raw_slice_v19(watchdog_raw,b"def v19_refusal_preclose_once_v19",b"def v19_closure_driver")
 need(preclose.count(b"send_exact(")==1)
 v19_raw_order_v19(preclose,(b"CONTROL_SEND_SEQ==cell.preclose_sequence",b"checkpoint(CERT,0,cell.preclose_deadline)",b"cell.preclose_state=b\"POSSIBLE\"",b"cell.preclose_send_latch=True",b"send_exact(control,cell.preclose_packet,cell.preclose_deadline)"))
 need(watchdog_raw.count(V19_RECORD_DELTA_GRAMMAR_RAW)==1)
 need(V19_RECORD_DELTA_KINDS==(b"INTENT",b"RELEASE",b"VALIDATED",b"ACK_INTENT",b"COMMITTED",b"COMMITTED_SEEN",b"KILL_TICKET",b"RETAINED",b"RECOVERY",b"FAILURE_REPORT",b"TERMINAL_CANDIDATE",b"TERMINAL_SEEN",b"SUCCESS_REPORT",b"PASS_COMMIT",b"ACK_RECEIPT",b"RECONCILIATION",b"OWNER_CLOSURE"))
 return True

def v19_validate_actor_control_surface():
 need(len(V19_EXTERNAL_GATES)==6 and len(set(V19_EXTERNAL_GATES))==6)
 need(V19_PHYSICAL_STATES==(b"CLOSED",b"ACQUIRING",b"OWNED",b"CLOSE_RETRY"))
 need(len(V19_RECEIVE_SITE_SPEC)==5 and tuple(row[2] for row in V19_RECEIVE_SITE_SPEC)==(5,5,14,14,5))
 need(tuple(row[1]+1 for row in V19_RECEIVE_SITE_SPEC)==tuple(row[2] for row in V19_RECEIVE_SITE_SPEC))
 need(len(V19_OFFERED_SLOTS)==13 and len(V19_SAFE_LOCAL_SLOTS)==12 and not set(V19_OFFERED_SLOTS)&set(V19_SAFE_LOCAL_SLOTS))
 need(len(V19_RECORD_DELTA_KINDS)==17 and len(set(V19_RECORD_DELTA_KINDS))==17)
 need(len(CONTROL_SPEC)==40 and all(key.startswith(b"V15_") for key in CONTROL_SPEC))
 need(CONTEXT_DOMAIN==b"P27E001_V15_DETACHED_ENVELOPE_CONTEXT\x00")
 need(CERTIFICATE_DOMAIN==b"P27E001_V15_CERTIFICATE_DIGEST\x00")
 need(ENVELOPE_TBS_DOMAIN==b"P27E001_V15_ENVELOPE_TBS\x00")
 need(AUTH_DOMAIN==b"P27E001_V15_SESSION_AUTH\x00")
 need(REFUSAL_FINALITY_NS==80000000 and REFUSAL_CLOSURE_TAIL_NS==130000000)
 need(REFUSAL_TOTAL_NS==210000000 and FINAL_TOTAL_NS==2510000000)
 need(ACTOR_RECORD_COUNT_V19==211 and ACTOR_LIVE_HIGH_WATER_V19==219)
 need(resource.getrlimit(resource.RLIMIT_NOFILE)[0]==256)
 need(ACTOR_CONTROL_FRAME_V19.semantic_capacity==4 and ACTOR_CONTROL_FRAME_V19.installed_capacity==5)
 need(ACTOR_CONTROL_FRAME_V19.ancillary_bytes>=5*socket.CMSG_SPACE(ctypes.sizeof(ctypes.c_int)))
 need(ACTOR_CONTROL_FRAME_V19.kernel_control_bytes==5*socket.CMSG_SPACE(ctypes.sizeof(ctypes.c_int)))
 need(len(ACTOR_PHYSICAL_RECORDS_V19)==211 and len(ACTOR_RAW_CELLS_V19)==ACTOR_RAW_CELL_COUNT_V19)
 need(PhysicalRecordV19.__slots__==V19_PHYSICAL_RECORD_FIELDS and "owns" not in PhysicalRecordV19.__slots__)
 need("logical_role" not in PhysicalRecordV19.__slots__ and "transferable" not in PhysicalRecordV19.__slots__ and "transfer_order" not in PhysicalRecordV19.__slots__)
 need(RawCellV19.__slots__==V19_RAW_CELL_FIELDS and PollerCellV19.__slots__==V19_POLLER_CELL_FIELDS)
 need(ReceiveFrameV19.__slots__==V19_ACTOR_RECEIVE_FRAME_FIELDS)
 need(tuple(record.record_id for record in ACTOR_PHYSICAL_RECORDS_V19)==tuple(range(211)))
 need(len(ACTOR_CONTROL_FRAME_V19.raw_cells)==5 and len(ACTOR_CONTROL_FRAME_V19.quarantine_records)==5)
 need(all(record.state in V19_PHYSICAL_STATES for record in ACTOR_PHYSICAL_RECORDS_V19))
 need(all(cell.state in V19_RAW_STATES for cell in ACTOR_RAW_CELLS_V19))
 need(ACTOR_ENTRY_LIMIT_CERTIFIED_V19 and ACTOR_CURRENT_LOW_LIMIT_VECTOR_V19==(256,ACTOR_ENTRY_LIMIT_VECTOR_V19[1]))
 need(ACTOR_LIVE_HIGH_WATER_V19==len(ACTOR_SIMULTANEOUS_LIVE_ROLE_SET_V19)==219<256)
 inherited_roles=tuple(row[0] for row in ACTOR_INHERITED_FIXED_SPEC_V19)
 need(len(inherited_roles)==14 and len(set(inherited_roles))==14)
 for record in ACTOR_PHYSICAL_RECORDS_V19:
  if record.semantic_role in inherited_roles:
   expected=next(row for row in ACTOR_INHERITED_FIXED_SPEC_V19 if row[0]==record.semantic_role)
   need(record.state==b"OWNED" and record.raw_fd==expected[2] and record.physical_identity is not None and len(record.physical_identity)==7 and record.access!=b"UNKNOWN")
  else:need(record.state==b"CLOSED" and record.raw_fd==-1 and record.semantic_role is None)
 need(sum(1 for record in ACTOR_PHYSICAL_RECORDS_V19 if record.semantic_role in inherited_roles)==14)
 return True
# P27 RUNNER V20 EMBEDDED VALIDATOR END 8E20B7D2

CONTROL_SPEC={
 b"V15_ABORT":(b"ABORTING",b"*",b"ABORT_NOTICE",b"control_deadline_ns"),
 b"V15_READY":(b"READY",b"WAIT_READY",b"NO_EFFECT",b"ready_deadline_ns"),
 b"V15_REFUSE_PREBEGIN":(b"REFUSE_PREBEGIN",b"WAIT_BEGIN",b"NO_CONSUME_REFUSAL",b"consume_deadline_ns"),
 b"V15_REFUSE_POSTARM":(b"REFUSE_POSTARM",b"WAIT_COMMIT",b"NO_CONSUME_REFUSAL",b"consume_deadline_ns"),
 b"V15_REFUSE_ACK":(b"REFUSAL_CLOSED_NO_CONSUME",b"WAIT_REFUSAL_ACK",b"REFUSAL_ACK_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V15_REFUSE_ACK_RECEIPT":(b"REFUSAL_ACK_RECEIVED",b"WAIT_REFUSAL_RECEIPT",b"NO_REPLAY_RECEIPT",b"consume_deadline_ns"),
 b"V15_REFUSAL_CLOSED":(b"REFUSAL_DURABLY_CLOSED",b"WAIT_REFUSAL_CLOSED",b"OWNER_CLOSURE",b"consume_deadline_ns"),
 b"V15_CONSUME_BEGIN":(b"CONSUME_BEGIN",b"WAIT_BEGIN",b"BEGIN_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V15_CONSUME_ARMED":(b"CONSUME_ARMED",b"WAIT_ARM",b"ARM_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V15_CONSUME_COMMIT":(b"CONSUME_COMMIT",b"WAIT_COMMIT",b"COMMIT_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V15_CONSUMED_DURABLE":(b"CONSUMED_DURABLE",b"WAIT_CONSUMED",b"INTENT_DURABLE",b"consume_deadline_ns"),
 b"V15_STAGE_DURABLE":(b"STAGE_DURABLE",b"WAIT_STAGE",b"FD_TRANSFER",b"stage_deadline_ns"),
 b"V15_STAGE_ACK":(b"STAGE_BOUND",b"WAIT_STAGE_ACK",b"STAGE_VERIFIED",b"stage_deadline_ns"),
 b"V15_CONTAINMENT":(b"CONTAINMENT_CANDIDATE",b"WAIT_CONTAINMENT",b"FD_TRANSFER",b"contain_deadline_ns"),
 b"V15_CONTAINMENT_ACK":(b"CONTAINMENT_BOUND",b"WAIT_CONTAINMENT_ACK",b"CONTAINMENT_VERIFIED",b"contain_deadline_ns"),
 b"V15_STREAM_ARM":(b"STREAM_ARM",b"WAIT_STREAM_ARM",b"FD_TRANSFER",b"launch_deadline_ns"),
 b"V15_STREAMS_ARMED":(b"STREAMS_ARMED",b"WAIT_STREAMS_ARMED",b"FD_VERIFIED",b"launch_deadline_ns"),
 b"V15_PIDFD_ARM":(b"PIDFD_ARM",b"WAIT_PIDFD_ARM",b"FD_TRANSFER",b"launch_deadline_ns"),
 b"V15_PIDFD_ARMED":(b"PIDFD_ARMED",b"WAIT_PIDFD_ARMED",b"PIDFD_VERIFIED",b"launch_deadline_ns"),
 b"V15_RELEASE_CANDIDATE":(b"RELEASE_CANDIDATE",b"WAIT_RELEASE",b"RELEASE_AUTHORIZATION",b"launch_deadline_ns"),
 b"V15_RELEASE_DURABLE":(b"RELEASE_DURABLE",b"WAIT_RELEASE_DURABLE",b"RELEASE_RECORD_DURABLE",b"launch_deadline_ns"),
 b"V15_RESULT":(b"RESULT",b"WAIT_RESULT",b"RESULT_NOTICE",b"result_deadline_ns"),
 b"V15_RESULT_FRAME":(b"RESULT_FRAME",b"WAIT_RESULT_FRAME",b"RESULT_FRAME",b"result_deadline_ns"),
 b"V15_RESULT_END":(b"RESULT_END",b"WAIT_RESULT_END",b"RESULT_COMPLETE",b"result_deadline_ns"),
 b"V15_VALIDATED_CANDIDATE":(b"VALIDATED_CANDIDATE",b"WAIT_VALIDATED",b"VALIDATION_NOTICE",b"ack_deadline_ns"),
 b"V15_VALIDATED_DURABLE":(b"VALIDATED_DURABLE",b"WAIT_VALIDATED_DURABLE",b"VALIDATED_RECORD_DURABLE",b"ack_deadline_ns"),
 b"V15_ACK_COMMIT_INTENT":(b"ACK_COMMIT_INTENT",b"WAIT_ACK_INTENT",b"ACK_COMMIT",b"ack_deadline_ns"),
 b"V15_COMMITTED":(b"COMMITTED",b"WAIT_COMMITTED",b"COMMIT_RECORD_DURABLE",b"ack_deadline_ns"),
 b"V15_COMMITTED_SEEN":(b"COMMITTED_SEEN",b"WAIT_COMMITTED_SEEN",b"ACK_RECEIPT",b"ack_deadline_ns"),
 b"V15_EMPTY_FINAL_QUERY":(b"EMPTY_FINAL_QUERY",b"WAIT_EMPTY_QUERY",b"REMOVE_QUERY",b"remove_deadline_ns"),
 b"V15_EMPTY_FINAL_CONFIRMED":(b"EMPTY_FINAL_CONFIRMED",b"WAIT_EMPTY_CONFIRMED",b"EMPTY_OBSERVED",b"remove_deadline_ns"),
 b"V15_CGROUP_REMOVED":(b"CGROUP_REMOVED",b"WAIT_REMOVED",b"REMOVE_EFFECT",b"remove_deadline_ns"),
 b"V15_REMOVE_ACK":(b"REMOVE_ACK",b"WAIT_REMOVE_ACK",b"REMOVAL_VERIFIED",b"remove_deadline_ns"),
 b"V15_FINALIZE_CANDIDATE":(b"FINALIZE_CANDIDATE",b"WAIT_FINALIZE",b"FINALIZE_NOTICE",b"candidate_deadline_ns"),
 b"V15_TERMINAL_CANDIDATE_DURABLE":(b"TERMINAL_CANDIDATE_DURABLE",b"WAIT_TERMINAL_CANDIDATE",b"CANDIDATE_DURABLE",b"candidate_deadline_ns"),
 b"V15_TERMINAL_FAILURE_DURABLE":(b"TERMINAL_FAILURE_DURABLE",b"WAIT_TERMINAL_FAILURE",b"FAILURE_REPORT_DURABLE",b"candidate_deadline_ns"),
 b"V15_TERMINAL_SEEN":(b"TERMINAL_SEEN",b"WAIT_TERMINAL_SEEN",b"TERMINAL_SEEN",b"seen_deadline_ns"),
 b"V15_TERMINAL_ACK":(b"TERMINAL_ACK",b"WAIT_TERMINAL_ACK",b"ACK_SEND_EFFECT_UNKNOWN",b"ack_deadline_ns"),
 b"V15_TERMINAL_ACK_RECEIPT":(b"ACK_RECEIVED_NO_REPLAY",b"WAIT_ACK_RECEIPT",b"NO_REPLAY_RECEIPT",b"receipt_deadline_ns"),
 b"V15_TERMINAL_CLOSED":(b"OWNER_CLOSED",b"WAIT_OWNER_CLOSED",b"OWNER_CLOSURE",b"closure_deadline_ns")
}
CONTROL_DEADLINE_KEYS=(b"ready_deadline_ns",b"control_deadline_ns",b"consume_deadline_ns",b"stage_deadline_ns",b"contain_deadline_ns",b"launch_deadline_ns",b"result_deadline_ns",b"ack_deadline_ns",b"remove_deadline_ns",b"candidate_deadline_ns",b"seen_deadline_ns",b"pass_deadline_ns",b"margin_deadline_ns",b"receipt_deadline_ns",b"closure_deadline_ns",b"transfer_deadline_ns",b"terminal_deadline_ns")
CONTROL_RESERVED={b"state",b"expected_state",b"ordinal",b"probe",b"auth_id",b"sender",b"effect_state"}|set(CONTROL_DEADLINE_KEYS)

def packet(kind,pairs):
 global CONTROL_SEND_SEQ
 need(kind in CONTROL_SPEC and b"|" not in kind and b"\n" not in kind)
 provided={}
 for key,value in pairs:
  need(key and value and b"|" not in key+value and b"\n" not in key+value and b"=" not in key+value and key not in provided)
  provided[key]=value
 spec_state,spec_receiver,spec_effect,deadline_key=CONTROL_SPEC[kind]
 state=provided.pop(b"state",spec_state);receiver=provided.pop(b"expected_state",spec_receiver);effect=provided.pop(b"effect_state",spec_effect)
 if kind==b"V15_ABORT":need(state==spec_state and effect==spec_effect and receiver not in (b"",b"*"))
 else:need((state,receiver,effect)==(spec_state,spec_receiver,spec_effect) and state!=b"*" and receiver!=b"*" and effect!=b"*")
 ordinal=provided.pop(b"ordinal");probe=provided.pop(b"probe")
 if b"auth_id" in provided:need(provided.pop(b"auth_id")==AUTH_ID)
 if b"sender" in provided:need(provided.pop(b"sender")==b"A")
 need(deadline_key in provided);deadline=provided.pop(deadline_key);udec(deadline,1)
 need(not any(key in CONTROL_RESERVED for key in provided))
 CONTROL_SEND_SEQ+=1
 transition=state+b"->"+receiver+b":"+effect
 body=(kind+b"|protocol_version=14|session_id="+AUTH_ID+b"|message_seq="+str(CONTROL_SEND_SEQ).encode()+b"|message_sender="+b"A"+b"|transition_id="+transition+b"|sender_state="+state+b"|expected_receiver_state="+receiver+b"|slot_ordinal="+ordinal+b"|slot_probe="+probe+b"|effect_state="+effect+b"|deadline_name="+deadline_key+b"|absolute_deadline_ns="+deadline)
 for key,value in pairs:
  if key not in CONTROL_RESERVED:body+=b"|"+key+b"="+value
 return body+b"\n"

def receiver_binding(actual_pre_state,ordinal,probe,inherited_deadline):
 need(type(actual_pre_state)is bytes and actual_pre_state and type(ordinal)is bytes and ordinal and type(probe)is bytes and probe and type(inherited_deadline)is int and inherited_deadline>0)
 return (actual_pre_state,ordinal,probe,inherited_deadline)

def received_binding(raw,actual_pre_state,ordinal,probe,deadline_name,local_ceiling):
 need(type(raw)is bytes and type(deadline_name)is bytes and deadline_name in CONTROL_DEADLINE_KEYS and type(local_ceiling)is int and local_ceiling>0)
 fields=raw[:-1].split(b"|") if raw.endswith(b"\n") else ()
 names=[item.split(b"=",1)[1] for item in fields if item.startswith(b"deadline_name=")]
 absolutes=[item.split(b"=",1)[1] for item in fields if item.startswith(b"absolute_deadline_ns=")]
 need(len(names)==len(absolutes)==1 and names[0]==deadline_name)
 inherited=udec(absolutes[0],1);need(inherited<=local_ceiling)
 return receiver_binding(actual_pre_state,ordinal,probe,inherited)

def parse_packet(raw,kind,keys,binding):
 global CONTROL_RECV_SEQ
 if kind!=b"V15_ABORT" and raw.startswith(b"V15_ABORT|"):
  actual_pre_state,actual_ordinal,actual_probe,local_ceiling=binding
  abort_binding=received_binding(raw,actual_pre_state,actual_ordinal,actual_probe,b"control_deadline_ns",local_ceiling)
  values,faults=parse_abort(raw,b"B",abort_binding);error=RemoteAbort(faults);error.values=values;raise error
 need(type(raw)is bytes and raw.endswith(b"\n") and raw.count(b"\n")==1 and all(x==10 or 32<=x<=126 for x in raw))
 common_keys=(b"protocol_version",b"session_id",b"message_seq",b"message_sender",b"transition_id",b"sender_state",b"expected_receiver_state",b"slot_ordinal",b"slot_probe",b"effect_state",b"deadline_name",b"absolute_deadline_ns")
 physical=tuple(key for key in keys if key not in CONTROL_RESERVED)
 fields=raw[:-1].split(b"|");need(fields[0]==kind and len(fields)==1+len(common_keys)+len(physical))
 common={}
 for key,item in zip(common_keys,fields[1:1+len(common_keys)]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and parts[1] and key not in common);common[key]=parts[1]
 result={}
 for key,item in zip(physical,fields[1+len(common_keys):]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and parts[1] and key not in result and key not in common);result[key]=parts[1]
 spec_state,spec_receiver,spec_effect,deadline_key=CONTROL_SPEC[kind]
 need(common[b"protocol_version"]==b"14" and common[b"session_id"]==AUTH_ID and common[b"message_sender"]==b"B")
 need(common[b"transition_id"]==common[b"sender_state"]+b"->"+common[b"expected_receiver_state"]+b":"+common[b"effect_state"])
 if kind==b"V15_ABORT":need(common[b"sender_state"]==spec_state and common[b"effect_state"]==spec_effect and common[b"expected_receiver_state"] not in (b"",b"*"))
 else:need((common[b"sender_state"],common[b"expected_receiver_state"],common[b"effect_state"])==(spec_state,spec_receiver,spec_effect))
 need(common[b"deadline_name"]==deadline_key);deadline=udec(common[b"absolute_deadline_ns"],1)
 actual_pre_state,actual_ordinal,actual_probe,inherited_deadline=binding
 need((actual_pre_state,actual_ordinal,actual_probe,inherited_deadline)==(common[b"expected_receiver_state"],common[b"slot_ordinal"],common[b"slot_probe"],deadline))
 sequence=udec(common[b"message_seq"],1);need(sequence==CONTROL_RECV_SEQ+1);CONTROL_RECV_SEQ=sequence
 result.update({b"state":common[b"sender_state"],b"expected_state":common[b"expected_receiver_state"],b"ordinal":common[b"slot_ordinal"],b"probe":common[b"slot_probe"],b"auth_id":common[b"session_id"],b"sender":common[b"message_sender"],b"effect_state":common[b"effect_state"],deadline_key:str(deadline).encode(),b"message_seq":str(sequence).encode(),b"packet_sha256":sha(raw)})
 return result

def fault_csv(faults):
 ordered=tuple(x for x in FAULT_ORDER if x in faults)
 need(len(ordered)==len(faults))
 return b"NONE" if not ordered else b",".join(ordered)

def parse_fault_csv(raw,allow_none):
 if raw==b"NONE":
  need(allow_none);return set()
 parts=raw.split(b",");need(parts and all(x in FAULT_ORDER for x in parts))
 need(len(parts)==len(set(parts)) and tuple(x for x in FAULT_ORDER if x in set(parts))==tuple(parts))
 return set(parts)

def parse_abort(raw,want_sender,binding):
 keys=(b"state",b"ordinal",b"probe",b"effect_state",b"causal_state",b"causal_effect",b"stage_present",b"release_disabled",b"terminal_deadline_ns",b"fault_set",b"control_deadline_ns")
 values=parse_packet(raw,b"V15_ABORT",keys,binding)
 need(values[b"sender"]==want_sender and values[b"state"]==b"ABORTING" and values[b"expected_state"]==binding[0] and values[b"effect_state"]==b"ABORT_NOTICE")
 causal_effects=(b"PREBEGIN",b"BEGIN_SEND_EFFECT_UNKNOWN",b"ARM_SEND_EFFECT_UNKNOWN",b"COMMIT_SEND_EFFECT_UNKNOWN",b"CONSUMED",b"PASS_COMMITTED",b"ACK_SEND_EFFECT_UNKNOWN",b"OWNER_CLOSED")
 need(values[b"causal_state"] and values[b"causal_effect"] in causal_effects and values[b"ordinal"] and values[b"probe"])
 need(values[b"stage_present"] in (b"0",b"1") and values[b"release_disabled"] in (b"0",b"1"))
 if want_sender==b"A":need(values[b"release_disabled"]==b"1")
 if want_sender==b"B" and values[b"causal_state"]==b"CLEANUP_RELEASE_DISABLE":need(values[b"release_disabled"]==b"0")
 deadline=udec(values[b"terminal_deadline_ns"])
 if values[b"causal_effect"] in (b"PASS_COMMITTED",b"ACK_SEND_EFFECT_UNKNOWN",b"OWNER_CLOSED"):need(deadline>0)
 faults=parse_fault_csv(values[b"fault_set"],False);return values,faults

def close_numbers(numbers):
 for number in numbers:
  actor_close_number(number)

def wait_sendable(control,deadline):
 poller=select.poll();poller.register(control.fileno(),select.POLLOUT|select.POLLHUP|select.POLLERR)
 while True:
  checkpoint(CERT,0,ConsumedIndeterminate,deadline);remaining=deadline-time.monotonic_ns()
  if remaining<=0:raise FaultSet({b"CONTROL_TIMEOUT"})
  try:events=poller.poll(max(1,min(50,(remaining+999999)//1000000)))
  except InterruptedError:continue
  mask=0
  for number,event in events:
   if number==control.fileno():mask|=event
  if mask&select.POLLOUT:return
  if mask&(select.POLLHUP|select.POLLERR):raise ControlLost("control-hup")

def send_plain(control,raw,deadline):
 global CONTROL_SEND_STATE
 while True:
  wait_sendable(control,deadline);CONTROL_SEND_STATE=b"SEND_EFFECT_UNKNOWN"
  try:count=control.send(raw)
  except BlockingIOError:continue
  except BaseException as error:raise SendEffectUnknown("send") from error
  if count!=len(raw):raise SendEffectUnknown("short-send")
  checkpoint(CERT,0,ConsumedIndeterminate,deadline)
  if time.monotonic_ns()>deadline:raise SendEffectUnknown("post-send-deadline")
  CONTROL_SEND_STATE=b"SENT";return

def send_rights(control,raw,numbers,deadline):
 global CONTROL_SEND_STATE
 cells=array.array("i",numbers)
 while True:
  wait_sendable(control,deadline);CONTROL_SEND_STATE=b"SEND_EFFECT_UNKNOWN"
  try:count=control.sendmsg([raw],[(socket.SOL_SOCKET,socket.SCM_RIGHTS,cells.tobytes())])
  except BlockingIOError:continue
  except BaseException as error:raise FaultSet({b"FD_TRANSFER",b"SEND_EFFECT_UNKNOWN"}) from error
  if count!=len(raw):raise FaultSet({b"FD_TRANSFER",b"SEND_EFFECT_UNKNOWN"})
  checkpoint(CERT,0,ConsumedIndeterminate,deadline)
  if time.monotonic_ns()>deadline:raise FaultSet({b"FD_TRANSFER",b"SEND_EFFECT_UNKNOWN"})
  CONTROL_SEND_STATE=b"SENT";return

def recv_control(control,deadline,cap=65536):
 checkpoint(CERT,0,ConsumedIndeterminate,deadline)
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR)
 while True:
  checkpoint(CERT,0,ConsumedIndeterminate,deadline);remaining=deadline-time.monotonic_ns()
  if remaining<=0:raise FaultSet({b"CONTROL_TIMEOUT"})
  try:events=poller.poll(max(1,min(50,(remaining+999999)//1000000)))
  except InterruptedError:continue
  mask=0
  for number,event in events:
   if number==control.fileno():mask|=event
  if mask&select.POLLIN:
   installed=[];bad=False
   try:
    raw,ancillary,flags,address=control.recvmsg(cap,socket.CMSG_SPACE(MAX_RIGHTS*array.array("i").itemsize))
    installed,bad=actor_quarantine_rights(ancillary)
    checkpoint(CERT,0,ConsumedIndeterminate,deadline)
    if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})
    if flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC):raise FaultSet({b"CONTROL_TRUNCATION"})
    if bad or installed or ancillary:raise FaultSet({b"FD_TRANSFER"})
    if address is not None or not raw:raise FaultSet({b"CONTROL_MALFORMED"})
    return raw
   except BlockingIOError:
    close_numbers(installed);continue
   except BaseException:
    close_numbers(installed);raise
  if mask&(select.POLLHUP|select.POLLERR):raise ControlLost("control-hup")

def wait_exact(control,deadline,expected):
 raw=recv_control(control,deadline)
 if raw!=expected:raise FaultSet({b"CONTROL_MALFORMED"})

def pidfd_pid(number):
 link=os.readlink(b"/proc/self/fd/"+str(number).encode());need(link==b"anon_inode:[pidfd]",Refuse);info=-1
 try:
  info=actor_acquire_open(b"pidfd_info_fd",b"PIDFD_INFO_OBSERVATION_FD",b"/proc/self/fdinfo/"+str(number).encode(),os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(info,4096),4096)
 finally:close_numbers(tuple(x for x in (info,) if x>=0))
 values=[x[5:] for x in raw.splitlines() if x.startswith(b"Pid:\t")];need(len(values)==1,Refuse);return udec(values[0],1)

def proc_starttime(pid,kind=Refuse):
 number=-1
 try:
  number=actor_acquire_open(b"proc_starttime_fd",b"PROC_STARTTIME_OBSERVATION_FD",b"/proc/"+str(pid).encode()+b"/stat",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(number,4096),4096)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))
 cut=raw.rfind(b") ");need(cut>0,kind);fields=raw[cut+2:].strip().split();need(len(fields)>=20,kind)
 return udec(fields[19],1)

EXTERNAL_MANIFEST_KEYS=(b"VERSION",b"SESSION_AUTH_POLICY",b"OWNER_PID",b"OWNER_STARTTIME",b"OWNER_UID",b"OWNER_GID",b"ENDPOINT_TYPE",b"PIDFD_REQUIRED",b"MAX_PACKET_BYTES",b"RIGHTS_TYPES",b"REFUSAL_RECEIPT_PROTOCOL",b"TRANSFER_PROTOCOL",b"NO_REPLAY")
EXTERNAL_RIGHTS_TYPES=b"ATTEMPT_DIRFD,ATTEMPT_BASE_DIRFD,STAGE_DIRFD,CGROUP_DIRFD,ROOT_EVENTS_FD,ROOT_KILL_FD,OUT_FD,ERR_FD,EVENTS_FD,OUTER_PIDFD,CGROUP_BASE_DIRFD,ACTOR_CONTROL_FD,PENDING_EXPECTED_RAW_FD"

def parse_external_manifest(raw,cert):
 values=parse_fixed(raw,b"P27E001_EXTERNAL_OWNER_MANIFEST_V15",EXTERNAL_MANIFEST_KEYS,b"MANIFEST_END=1")
 exact={b"VERSION":b"14",b"SESSION_AUTH_POLICY":b"AUTH_V15_LENGTH_FRAMED",b"OWNER_PID":cert[b"EXTERNAL_OWNER_PID"],b"OWNER_STARTTIME":cert[b"EXTERNAL_OWNER_STARTTIME"],b"OWNER_UID":cert[b"EXTERNAL_OWNER_UID"],b"OWNER_GID":cert[b"EXTERNAL_OWNER_GID"],b"ENDPOINT_TYPE":b"SOCK_SEQPACKET",b"PIDFD_REQUIRED":b"1",b"MAX_PACKET_BYTES":b"65536",b"RIGHTS_TYPES":EXTERNAL_RIGHTS_TYPES,b"REFUSAL_RECEIPT_PROTOCOL":b"MONOTONE_O_EXCL_ISSUER_V15",b"TRANSFER_PROTOCOL":b"OFFER_ACCEPTED_DURABLE_V15",b"NO_REPLAY":b"1"}
 for key,value in exact.items():need(values[key]==value,Refuse)
 return values

def verify_external_inputs(cert):
 pid=udec(cert[b"EXTERNAL_OWNER_PID"],2);start=udec(cert[b"EXTERNAL_OWNER_STARTTIME"],1)
 fd_access(108,os.O_RDWR);fd_access(109,os.O_RDWR);need(pidfd_pid(109)==pid,Refuse)
 watcher=select.poll();watcher.register(109,select.POLLIN|select.POLLHUP|select.POLLERR);need(watcher.poll(0)==[],Refuse)
 duplicate=socket.socket(fileno=108)
 try:
  need(duplicate.getsockopt(socket.SOL_SOCKET,socket.SO_TYPE)==socket.SOCK_SEQPACKET,Refuse)
  need(fcntl.fcntl(108,fcntl.F_GETFL)&os.O_NONBLOCK,Refuse)
  peer=struct.unpack("3i",duplicate.getsockopt(socket.SOL_SOCKET,socket.SO_PEERCRED,12))
  need(peer==(pid,udec(cert[b"EXTERNAL_OWNER_UID"]),udec(cert[b"EXTERNAL_OWNER_GID"])),Refuse)
 finally:need(duplicate.detach()==108,Refuse)
 need(proc_starttime(pid)==start and pidfd_pid(109)==pid and proc_starttime(pid)==start and watcher.poll(0)==[],Refuse)

def cgroup_populated(number):
 os.lseek(number,0,os.SEEK_SET);raw=os.read(number,4096)
 matches=[line for line in raw.splitlines() if line.startswith(b"populated ")]
 need(len(matches)==1 and matches[0] in (b"populated 0",b"populated 1"),ConsumedIndeterminate)
 return matches[0]==b"populated 1"

def cgroup_empty(cgfd):
 number=-1
 try:
  number=actor_acquire_open(b"cgroup_events_observation_fd",b"CGROUP_EVENTS_OBSERVATION_FD",b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd);return not cgroup_populated(number)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))

def exact_child_cgroup(cgfd,pid):
 number=-1
 try:
  number=actor_acquire_open(b"cgroup_procs_observation_fd",b"CGROUP_PROCS_OBSERVATION_FD",b"cgroup.procs",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd);need(read_all(number,64)==str(pid).encode()+b"\n",ConsumedIndeterminate)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))

def wait_status(pid,flags,deadline,unknown_fault):
 while True:
  checkpoint(CERT,0,ConsumedIndeterminate,deadline)
  if time.monotonic_ns()>deadline:raise FaultSet({unknown_fault})
  try:waited,raw=os.waitpid(pid,flags|os.WNOHANG)
  except InterruptedError:
   checkpoint(CERT,0,ConsumedIndeterminate,deadline);continue
  except BaseException as error:raise FaultSet({unknown_fault}) from error
  checkpoint(CERT,0,ConsumedIndeterminate,deadline)
  if time.monotonic_ns()>deadline:raise FaultSet({unknown_fault})
  if waited not in (0,pid):raise FaultSet({unknown_fault})
  if waited==pid:return raw
  try:select.poll().poll(1)
  except InterruptedError:pass

def source_argv(probe,safe,p01c):
 app=[b"/proc/self/fd/100",probe,AUTH_ID,b"15000000000",b"5000000",b"2000000",b"20000000",b"100000000",b"100000000",b"500000000",b"NO_ASYNC_TRANSFER_THROUGH_FIXED_FD_PROCESS_WAIT_AND_CLOSE_COMMIT_V15",b"OWNER_SURVIVAL_PROGRESS_SINGLE_FRAME_V15",b"ROOT_OWNED_0700_STABLE_NONCE_NO_CONCURRENT_MUTATOR_V15",str(safe.st_dev).encode(),str(safe.st_ino).encode()]
 for identity in SOURCE_META:app.append(str(identity[0]).encode()+b","+str(identity[1]).encode()+b","+identity[2])
 app.extend(p01c);need(len(app)==20 or (probe==b"P01C" and len(app)==33))
 return [PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8"]+app

def derive_p01c(prior,cert):
 need(prior is not None)
 path=even_hex(prior[b"libc_path_hex"]);conf_bytes=even_hex(prior[b"libc_confstr_hex"])
 conf_text=conf_bytes.decode("ascii","strict");need(conf_text.encode("ascii","strict")==conf_bytes and conf_bytes.hex().encode()==prior[b"libc_confstr_hex"])
 need(prior[b"libc_path_hex"]==cert[b"LIBC_PATH_HEX"] and prior[b"libc_confstr_hex"]==cert[b"LIBC_CONFSTR_HEX"] and prior[b"libc_sha256"]==cert[b"LIBC_SHA256"])
 rootfd=number=py=-1
 try:
  rootfd=open_dir(RUNTIME_ROOT);number=open_under(rootfd,path);held=os.fstat(number);raw=read_all(number,held.st_size);actor_close_number(number);number=-1
  py=open_under(rootfd,PYIMAGE);pyheld=os.fstat(py);pyraw=read_all(py,30626264);actor_close_number(py);py=-1
 finally:close_numbers(tuple(x for x in (number,py,rootfd) if x>=0))
 observed=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,held.st_size,sha(raw))
 certified=(udec(cert[b"LIBC_DEV"],1),udec(cert[b"LIBC_INO"],1),octal(cert[b"LIBC_MODE"]),udec(cert[b"LIBC_NLINK"],1),udec(cert[b"LIBC_UID"]),udec(cert[b"LIBC_GID"]),udec(cert[b"LIBC_BYTES"],1),cert[b"LIBC_SHA256"])
 need(observed==certified and held.st_size==udec(prior[b"libc_bytes"]) and sha(raw)==prior[b"libc_sha256"])
 py_observed=(pyheld.st_dev,pyheld.st_ino,pyheld.st_mode,pyheld.st_nlink,pyheld.st_uid,pyheld.st_gid,len(pyraw),sha(pyraw))
 py_certified=(udec(cert[b"PYTHON_IMAGE_DEV"],1),udec(cert[b"PYTHON_IMAGE_INO"],1),octal(cert[b"PYTHON_IMAGE_MODE"]),udec(cert[b"PYTHON_IMAGE_NLINK"],1),udec(cert[b"PYTHON_IMAGE_UID"]),udec(cert[b"PYTHON_IMAGE_GID"]),udec(cert[b"PYTHON_IMAGE_BYTES"],1),cert[b"PYTHON_IMAGE_SHA256"])
 need(py_observed==py_certified and str(pyheld.st_dev).encode()==prior[b"python_image_dev"] and str(pyheld.st_ino).encode()==prior[b"python_image_ino"])
 result=(prior[b"libc_path_hex"],str(held.st_dev).encode(),str(held.st_ino).encode(),format(held.st_mode,"o").encode(),str(held.st_nlink).encode(),str(held.st_uid).encode(),str(held.st_gid).encode(),str(held.st_size).encode(),prior[b"libc_sha256"],prior[b"libc_confstr_hex"],prior[b"python_image_dev"],prior[b"python_image_ino"],prior[b"python_image_sha256"])
 need(len(result)==13 and result[9]==prior[b"libc_confstr_hex"] and result[5]==cert[b"LIBC_UID"] and result[6]==cert[b"LIBC_GID"]);return result

def launch_b(cert,base_stats):
 global B_CHILD_PID,B_CONTROL
 empty_r=empty_w=actor_pidfd=-1;left=right=None;pid=-1
 try:
  empty_r,empty_w=actor_acquire_pipe2(b"launch_empty_r_fd",b"launch_empty_w_fd",os.O_CLOEXEC);actor_close_number(empty_w);empty_w=-1
  left,right=actor_acquire_socketpair(b"launch_left_fd",b"launch_right_fd")
  actor_pid=os.getpid();actor_starttime=proc_starttime(actor_pid);actor_pidfd=actor_acquire_pidfd(b"launch_actor_pidfd",actor_pid);need(pidfd_pid(actor_pidfd)==actor_pid and proc_starttime(actor_pid)==actor_starttime,Refuse);pid=os.fork()
  if pid>0:
   B_CHILD_PID=pid;B_CONTROL=left;left=None
  if pid==0:
   try:
    actor_close_number(left.fileno());left=None
    mapping=((empty_r,0),(right.fileno(),3),(actor_pidfd,4),(base_stats[b"attempt_fd"],5),(base_stats[b"cgroup_fd"],6),(104,7),(105,8),(101,9),(103,10),(100,11),(102,12),(107,13),(108,14),(109,15),(110,16),(106,100))
    preserved_map(mapping);actor_close_number(1);actor_close_number(2)
    actor_close_registered_range(17,99);close_range(17,99);actor_close_registered_range(101,UINT_MAX);close_range(101,UINT_MAX)
    child_context(None,base_stats[b"safe"].st_dev,base_stats[b"safe"].st_ino);scrub_exact({0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,100})
    argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"/proc/self/fd/100",b"RECOVER_V19",AUTH_ID,str(actor_pid).encode(),str(actor_starttime).encode(),cert[b"PLAN_SHA256"],cert[b"RECOVERY_SHA256"],str(base_stats[b"safe"].st_dev).encode(),str(base_stats[b"safe"].st_ino).encode())
    os.execve(PYTHON,argv,ENV)
   except BaseException:os._exit(97)
  actor_close_number(right.fileno());right=None;actor_close_number(empty_r);empty_r=-1;actor_close_number(actor_pidfd);actor_pidfd=-1
  result=B_CONTROL;need(B_CHILD_PID==pid and result is not None,Refuse);return pid,result
 finally:
  close_numbers(tuple(x for x in (empty_r,empty_w,actor_pidfd) if x>=0))
  for endpoint in (left,right):
   if endpoint is not None:
    actor_close_number(endpoint.fileno())

def launch_outer(outer_fd,in_r,out_w,err_w,safe,argv,cgfd):
 pidfd_cell=ctypes.c_int(-1);args=CloneArgs();args.flags=CLONE_PIDFD|CLONE_INTO_CGROUP
 args.pidfd=ctypes.addressof(pidfd_cell);args.exit_signal=int(signal.SIGCHLD);args.cgroup=cgfd
 pid=LIBC.syscall(SYS_CLONE3,ctypes.byref(args),ctypes.sizeof(args))
 if pid<0:
  if pidfd_cell.value>=0:actor_adopt_raw(b"probe_outer_pidfd",b"PROBE_OUTER_PIDFD",pidfd_cell.value);actor_close_record(b"probe_outer_pidfd")
  raise ConsumedIndeterminate("clone-return")
 if pid==0:
  try:
   os.kill(os.getpid(),signal.SIGSTOP)
   preserved_map(((in_r,0),(out_w,1),(err_w,2),(outer_fd,100)))
   actor_close_registered_range(3,99);close_range(3,99);actor_close_registered_range(101,UINT_MAX);close_range(101,UINT_MAX)
   child_context(AUTH_ID,safe.st_dev,safe.st_ino);scrub_exact({0,1,2,100})
   os.execve(PYTHON,tuple(argv),ENV)
  except BaseException:os._exit(98)
 if not (pid>=2 and pidfd_cell.value>=0):
  if pidfd_cell.value>=0:actor_adopt_raw(b"probe_outer_pidfd",b"PROBE_OUTER_PIDFD",pidfd_cell.value);actor_close_record(b"probe_outer_pidfd")
  raise ConsumedIndeterminate("clone-identity")
 actor_adopt_raw(b"probe_outer_pidfd",b"PROBE_OUTER_PIDFD",pidfd_cell.value)
 return pid,pidfd_cell.value

def recv_result(control,deadline,ordinal,probe,pid):
 raw=recv_control(control,deadline)
 keys=(b"ordinal",b"probe",b"outer_pid",b"pidfd_bound",b"pidfd_exit_ready_observed",b"stdout_len",b"stdout_sha256",b"stdout_eof",b"stdout_frames",b"stderr_len",b"stderr_sha256",b"stderr_eof",b"stderr_frames",b"cgroup_empty",b"fault_set",b"capture_done_ns")
 values=parse_packet(raw,b"V15_RESULT",keys,receiver_binding(b"WAIT_RESULT",str(ordinal).encode(),probe,deadline))
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe and udec(values[b"outer_pid"],2)==pid)
 out_need=udec(values[b"stdout_len"],0,STREAM_CAP);err_need=udec(values[b"stderr_len"],0,STREAM_CAP)
 out_frames=udec(values[b"stdout_frames"],0,49);err_frames=udec(values[b"stderr_frames"],0,49)
 need(out_frames==(out_need+64999)//65000 and err_frames==(err_need+64999)//65000)
 h64(values[b"stdout_sha256"]);h64(values[b"stderr_sha256"]);parse_fault_csv(values[b"fault_set"],True)
 out=bytearray();err=bytearray()
 for stream,total,target in ((b"STDOUT",out_frames,out),(b"STDERR",err_frames,err)):
  for index in range(total):
   frame=recv_control(control,deadline,65536)
   cut=frame.find(b"\n");need(cut>0)
   header=frame[:cut+1];payload=frame[cut+1:]
   fields=parse_packet(header,b"V15_RESULT_FRAME",(b"ordinal",b"probe",b"stream",b"index",b"bytes",b"sha256"),receiver_binding(b"WAIT_RESULT_FRAME",str(ordinal).encode(),probe,deadline))
   need(udec(fields[b"ordinal"],0,14)==ordinal and fields[b"probe"]==probe and fields[b"stream"]==stream)
   need(udec(fields[b"index"])==index and udec(fields[b"bytes"],1,65000)==len(payload) and sha(payload)==fields[b"sha256"])
   target.extend(payload)
 end=parse_packet(recv_control(control,deadline),b"V15_RESULT_END",(b"state",b"ordinal",b"probe"),receiver_binding(b"WAIT_RESULT_END",str(ordinal).encode(),probe,deadline))
 need(end[b"state"]==b"RESULT_END" and udec(end[b"ordinal"],0,14)==ordinal and end[b"probe"]==probe)
 need(len(out)==out_need and len(err)==err_need and sha(out)==values[b"stdout_sha256"] and sha(err)==values[b"stderr_sha256"])
 return values,bytes(out),bytes(err)

def transcript_language(raw):
 if not (type(raw)is bytes and 0<len(raw)<=STREAM_CAP and raw.endswith(b"\n")):raise FaultSet({b"TRANSCRIPT_LANGUAGE"})
 if not all(x==10 or 32<=x<=126 for x in raw):raise FaultSet({b"TRANSCRIPT_LANGUAGE"})
 lines=raw[:-1].split(b"\n")
 if not lines or not all(lines):raise FaultSet({b"TRANSCRIPT_LANGUAGE"})

PHASE_FAULT={b"STAGE":b"STAGING_FAULT",b"CONTAIN":b"CONTAINMENT_FAULT",b"STREAM_ARM":b"FD_TRANSFER",b"CLONE":b"RELEASE_EFFECT_UNKNOWN",b"STOP":b"STOP_WAIT_UNKNOWN",b"PIDFD_ARM":b"PIDFD_BINDING",b"RELEASE_RECORD":b"RELEASE_RECORD_DURABILITY_UNKNOWN",b"SIGCONT":b"RELEASE_EFFECT_UNKNOWN",b"WAIT":b"DIRECT_WAIT_UNKNOWN",b"RESULT":b"CAPTURE_IO",b"LANGUAGE":b"TRANSCRIPT_LANGUAGE",b"STRUCTURE":b"TRANSCRIPT_STRUCTURE",b"SEMANTICS":b"TRANSCRIPT_SEMANTICS",b"RECEIPT":b"ACK_DURABILITY_UNKNOWN",b"REMOVE":b"CONTAINMENT_NOT_EMPTY",b"FINAL":b"REPORT_DURABILITY_UNKNOWN"}

def error_faults(error,phase):
 if isinstance(error,RemoteAbort):return set(error.faults)
 if isinstance(error,FaultSet):return set(error.faults)
 if isinstance(error,CertificateExpired):return {b"CERTIFICATE_EXPIRED"}
 if isinstance(error,(ConsumedFail,ConsumedIndeterminate)) and phase in PHASE_FAULT:return {PHASE_FAULT[phase]}
 return {b"INTERNAL_INVARIANT"}

def send_abort(control,state,receiver_state,ordinal,probe,faults,deadline,terminal_deadline=0):
 effect=b"PREBEGIN" if PREFLIGHT else b"CONSUMED"
 need(receiver_state not in (b"",b"*"))
 raw=packet(b"V15_ABORT",((b"sender",b"A"),(b"state",b"ABORTING"),(b"expected_state",receiver_state),(b"ordinal",b"NONE" if ordinal is None else str(ordinal).encode()),(b"probe",probe),(b"effect_state",b"ABORT_NOTICE"),(b"causal_state",state),(b"causal_effect",effect),(b"stage_present",b"1" if STAGE_PRESENT else b"0"),(b"release_disabled",b"1"),(b"terminal_deadline_ns",str(terminal_deadline).encode()),(b"fault_set",fault_csv(faults)),(b"control_deadline_ns",str(deadline).encode())))
 send_plain(control,raw,deadline)

def run_probe(control,ordinal,probe,cgfd,safefd,safe,outer_source,ctx,p01c,cert):
 phase=b"STREAM_ARM";release_origin=time.monotonic_ns();launch_deadline=release_origin+LAUNCH_NS
 peer_pre_state=b"WAIT_STREAM_ARM";peer_deadline=launch_deadline
 in_r=in_w=out_r=out_w=err_r=err_w=outer_fd=events=pidfd=-1;pid=-1;outer_starttime=0;direct_wait_entered=False
 try:
  checkpoint(cert,horizon_needed(release_origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ConsumedIndeterminate,launch_deadline)
  in_r,in_w=actor_acquire_pipe2(b"probe_in_r_fd",b"probe_in_w_fd",os.O_CLOEXEC);actor_close_number(in_w);in_w=-1;need(os.read(in_r,1)==b"")
  out_r,out_w=actor_acquire_pipe2(b"probe_out_r_fd",b"probe_out_w_fd",os.O_CLOEXEC|os.O_NONBLOCK);err_r,err_w=actor_acquire_pipe2(b"probe_err_r_fd",b"probe_err_w_fd",os.O_CLOEXEC|os.O_NONBLOCK)
  need(os.fstat(out_r).st_ino!=os.fstat(err_r).st_ino);outer_fd=memfd(outer_source,"p27-v15-outer-v5")
  events=actor_acquire_open(b"probe_events_fd",b"PROBE_EVENTS_FD",b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
  cg_identity=os.fstat(cgfd);event_identity=os.fstat(events);leaf_identity=sha(str(cg_identity.st_dev).encode()+b":"+str(cg_identity.st_ino).encode()+b":"+str(event_identity.st_dev).encode()+b":"+str(event_identity.st_ino).encode())
  stream=packet(b"V15_STREAM_ARM",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"release_origin_ns",str(release_origin).encode()),(b"launch_deadline_ns",str(launch_deadline).encode()),(b"stdout_dev",str(os.fstat(out_r).st_dev).encode()),(b"stdout_ino",str(os.fstat(out_r).st_ino).encode()),(b"stderr_dev",str(os.fstat(err_r).st_dev).encode()),(b"stderr_ino",str(os.fstat(err_r).st_ino).encode()),(b"events_dev",str(event_identity.st_dev).encode()),(b"events_ino",str(event_identity.st_ino).encode()),(b"leaf_identity_sha256",leaf_identity),(b"kill_authority_source",b"WATCHDOG_ROOT_KILL_FD_ONLY")))
  send_rights(control,stream,(out_r,err_r,events),launch_deadline)
  close_numbers((out_r,err_r,events));out_r=err_r=events=-1
  armed=parse_packet(recv_control(control,launch_deadline),b"V15_STREAMS_ARMED",(b"ordinal",b"probe",b"sole_kill_capability"),receiver_binding(b"WAIT_STREAMS_ARMED",str(ordinal).encode(),probe,launch_deadline))
  need(udec(armed[b"ordinal"],0,14)==ordinal and armed[b"probe"]==probe and armed[b"sole_kill_capability"]==b"ROOT_KILL_FD");progress(cert,launch_deadline,horizon_needed(release_origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS))
  peer_pre_state=b"WAIT_PIDFD_ARM"
  phase=b"CLONE";argv=source_argv(probe,safe,p01c);pid,pidfd=launch_outer(outer_fd,in_r,out_w,err_w,safe,argv,cgfd)
  outer_starttime=proc_starttime(pid);need(pidfd_pid(pidfd)==pid and proc_starttime(pid)==outer_starttime,ConsumedIndeterminate)
  close_numbers((in_r,out_w,err_w,outer_fd));in_r=out_w=err_w=outer_fd=-1
  phase=b"STOP";stopped=wait_status(pid,os.WUNTRACED,launch_deadline,b"STOP_WAIT_UNKNOWN")
  need(os.WIFSTOPPED(stopped) and os.WSTOPSIG(stopped)==signal.SIGSTOP and pidfd_pid(pidfd)==pid and proc_starttime(pid)==outer_starttime,ConsumedIndeterminate)
  exact_child_cgroup(cgfd,pid);need(not cgroup_empty(cgfd),ConsumedIndeterminate)
  phase=b"PIDFD_ARM";arm=packet(b"V15_PIDFD_ARM",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"outer_pid",str(pid).encode()),(b"outer_starttime",str(outer_starttime).encode()),(b"stopped_raw_status",str(stopped).encode()),(b"cgroup_member",b"1"),(b"pidfd_bound",b"1"),(b"launch_deadline_ns",str(launch_deadline).encode())))
  send_rights(control,arm,(pidfd,),launch_deadline);actor_close_number(pidfd);pidfd=-1
  armed=parse_packet(recv_control(control,launch_deadline),b"V15_PIDFD_ARMED",(b"ordinal",b"probe",b"pidfd_bound",b"outer_pid",b"outer_starttime"),receiver_binding(b"WAIT_PIDFD_ARMED",str(ordinal).encode(),probe,launch_deadline))
  need(udec(armed[b"ordinal"],0,14)==ordinal and armed[b"probe"]==probe and armed[b"pidfd_bound"]==b"1" and udec(armed[b"outer_pid"],2)==pid and udec(armed[b"outer_starttime"],1)==outer_starttime)
  peer_pre_state=b"WAIT_RELEASE"
  outer_pid=pid;cg=os.fstat(cgfd)
  phase=b"RELEASE_RECORD";release_record_deadline=release_origin+RELEASE_RECORD_OFFSET_NS;release_reply_deadline=release_origin+RELEASE_REPLY_OFFSET_NS
  need(release_record_deadline<release_reply_deadline<launch_deadline,ConsumedIndeterminate)
  release=packet(b"V15_RELEASE_CANDIDATE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"outer_pid",str(pid).encode()),(b"outer_starttime",str(outer_starttime).encode()),(b"pidfd_bound",b"1"),(b"stopped_raw_status",str(stopped).encode()),(b"cgroup_member",b"1"),(b"cgroup_dev",str(cg.st_dev).encode()),(b"cgroup_ino",str(cg.st_ino).encode()),(b"cgroup_mode",format(cg.st_mode,"o").encode()),(b"cgroup_nlink",str(cg.st_nlink).encode()),(b"cgroup_uid",str(cg.st_uid).encode()),(b"cgroup_gid",str(cg.st_gid).encode()),(b"argv_sha256",sha(b"\x00".join(argv))),(b"env_sha256",sha(b"\x00".join(x+b"="+ENV[x] for x in sorted(ENV)))),(b"release_origin_ns",str(release_origin).encode()),(b"launch_overall_deadline_ns",str(launch_deadline).encode()),(b"release_record_deadline_ns",str(release_record_deadline).encode()),(b"release_reply_deadline_ns",str(release_reply_deadline).encode()),(b"launch_deadline_ns",str(release_record_deadline).encode())))
  send_plain(control,release,release_record_deadline)
  released=parse_packet(recv_control(control,release_reply_deadline),b"V15_RELEASE_DURABLE",(b"ordinal",b"probe",b"release_sha256",b"launch_overall_deadline_ns",b"release_record_deadline_ns",b"release_reply_deadline_ns"),receiver_binding(b"WAIT_RELEASE_DURABLE",str(ordinal).encode(),probe,release_reply_deadline))
  need(udec(released[b"ordinal"],0,14)==ordinal and released[b"probe"]==probe and udec(released[b"launch_overall_deadline_ns"])==launch_deadline and udec(released[b"release_record_deadline_ns"])==release_record_deadline and udec(released[b"release_reply_deadline_ns"])==release_reply_deadline);release_sha=h64(released[b"release_sha256"])
  peer_pre_state=b"MONITOR_PROBE";peer_deadline=release_origin+TOTAL_NS
  phase=b"SIGCONT";checkpoint(cert,horizon_needed(release_origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ConsumedIndeterminate,launch_deadline)
  call_entry=time.monotonic_ns();need(call_entry+SIGCONT_NS<=launch_deadline,ConsumedIndeterminate)
  os.kill(pid,signal.SIGCONT);release_return=time.monotonic_ns()
  need(release_return<=call_entry+SIGCONT_NS and release_return<=launch_deadline,ConsumedIndeterminate)
  checkpoint(cert,horizon_needed(release_origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ConsumedIndeterminate,launch_deadline)
  phase=b"WAIT";direct_wait_entered=True
  raw=wait_status(pid,0,release_origin+HOST_NS,b"DIRECT_WAIT_UNKNOWN");pid=-1;direct_done=time.monotonic_ns()
  phase=b"RESULT";values,stdout,stderr=recv_result(control,release_origin+HOST_NS,ordinal,probe,outer_pid)
  peer_pre_state=b"WAIT_VALIDATED";peer_deadline=release_origin+TOTAL_NS
  done=udec(values[b"capture_done_ns"]);host_complete=max(direct_done,done);ack_deadline=min(release_origin+TOTAL_NS,host_complete+ACK_NS)
  peer_deadline=ack_deadline
  need(time.monotonic_ns()<=ack_deadline and ack_deadline-host_complete<=ACK_NS,ConsumedIndeterminate)
  faults=parse_fault_csv(values[b"fault_set"],True)
  if values[b"pidfd_bound"]!=b"1" or values[b"pidfd_exit_ready_observed"]!=b"1":faults.add(b"PIDFD_BINDING")
  if values[b"stdout_eof"]!=b"1" or values[b"stderr_eof"]!=b"1":faults.add(b"CAPTURE_IO")
  if values[b"cgroup_empty"]!=b"1":faults.add(b"CONTAINMENT_NOT_EMPTY")
  if stderr:faults.add(b"STDERR_NONEMPTY")
  if raw!=0:faults.add(b"OUTER_STATUS")
  if host_complete>release_origin+HOST_NS:faults.add(b"WATCHDOG_DEADLINE")
  if faults:raise FaultSet(faults)
  try:
   if not cgroup_empty(cgfd):raise FaultSet({b"CONTAINMENT_NOT_EMPTY"})
  except FaultSet:raise
  except BaseException as error:raise FaultSet({b"CONTAINMENT_OBSERVATION_UNKNOWN"}) from error
  phase=b"LANGUAGE";transcript_language(stdout)
  phase=b"STRUCTURE"
  try:rows,outer_claims=transcript_structure(stdout,probe)
  except BaseException as error:raise FaultSet({b"TRANSCRIPT_STRUCTURE"}) from error
  phase=b"SEMANTICS"
  try:rows=transcript_semantics(rows,outer_claims,probe,ctx)
  except FaultSet:raise
  except BaseException as error:raise FaultSet({b"TRANSCRIPT_SEMANTICS"}) from error
  phase=b"RECEIPT";peer_pre_state=b"WAIT_VALIDATED";peer_deadline=ack_deadline;candidate=packet(b"V15_VALIDATED_CANDIDATE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"release_record_sha256",release_sha),(b"release_origin_ns",str(release_origin).encode()),(b"release_return_ns",str(release_return).encode()),(b"host_complete_ns",str(host_complete).encode()),(b"capture_done_ns",str(done).encode()),(b"direct_wait_state",b"COMPLETE"),(b"outer_raw_status",str(raw).encode()),(b"pidfd_bound",b"1"),(b"pidfd_exit_ready_observed",b"1"),(b"stdout_len",str(len(stdout)).encode()),(b"stdout_sha256",sha(stdout)),(b"stdout_eof",b"1"),(b"stdout_overflow",b"0"),(b"stderr_len",str(len(stderr)).encode()),(b"stderr_sha256",EMPTY_SHA),(b"stderr_eof",b"1"),(b"stderr_overflow",b"0"),(b"cgroup_empty",b"1"),(b"parser_language",b"ACCEPTED"),(b"parser_structure",b"ACCEPTED"),(b"parser_semantics",b"ACCEPTED"),(b"candidate",b"ACCEPTED"),(b"terminal",b"ACCEPTED"),(b"certificate_expiry_realtime_ns",cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"]),(b"ack_deadline_ns",str(ack_deadline).encode())))
  send_plain(control,candidate,ack_deadline)
  validated=parse_packet(recv_control(control,ack_deadline),b"V15_VALIDATED_DURABLE",(b"ordinal",b"probe",b"validated_sha256"),receiver_binding(b"WAIT_VALIDATED_DURABLE",str(ordinal).encode(),probe,ack_deadline))
  need(udec(validated[b"ordinal"],0,14)==ordinal and validated[b"probe"]==probe);validated_sha=h64(validated[b"validated_sha256"])
  peer_pre_state=b"WAIT_ACK_INTENT"
  checkpoint(cert,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ConsumedIndeterminate,ack_deadline)
  actor_ack=time.monotonic_ns();need(actor_ack-host_complete<=ACK_NS,ConsumedIndeterminate)
  intent=packet(b"V15_ACK_COMMIT_INTENT",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"validated_sha256",validated_sha),(b"host_complete_ns",str(host_complete).encode()),(b"ack_deadline_ns",str(ack_deadline).encode()),(b"actor_ack_intent_ns",str(actor_ack).encode())))
  send_plain(control,intent,ack_deadline)
  committed_raw=recv_control(control,ack_deadline);committed=parse_packet(committed_raw,b"V15_COMMITTED",(b"ordinal",b"probe",b"ack_sha256",b"commit_record_seq",b"committed_count"),receiver_binding(b"WAIT_COMMITTED",str(ordinal).encode(),probe,ack_deadline))
  need(udec(committed[b"ordinal"],0,14)==ordinal and committed[b"probe"]==probe);ack_sha=h64(committed[b"ack_sha256"])
  peer_pre_state=b"WAIT_COMMITTED_SEEN"
  need(udec(committed[b"commit_record_seq"],1)>0 and udec(committed[b"committed_count"],1,15)==ordinal+1);committed_packet_sha=sha(committed_raw)
  checkpoint(cert,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ConsumedIndeterminate,ack_deadline)
  seen=packet(b"V15_COMMITTED_SEEN",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"ack_sha256",ack_sha),(b"committed_packet_sha256",committed_packet_sha),(b"committed_count",committed[b"committed_count"]),(b"host_complete_ns",str(host_complete).encode()),(b"ack_deadline_ns",str(ack_deadline).encode())))
  send_plain(control,seen,ack_deadline);need(time.monotonic_ns()-host_complete<=ACK_NS,ConsumedIndeterminate);return rows,ack_sha
 except BaseException as error:
  faults=error_faults(error,phase)
  if isinstance(error,RemoteAbort):
   remote=error.values;response_deadline=udec(remote[b"control_deadline_ns"],1);remote_terminal=udec(remote[b"terminal_deadline_ns"])
   reply_state=b"WAIT_RELEASE_DISABLE_ACK";reply_ordinal=ordinal;reply_probe=probe
  else:
   response_deadline=min(peer_deadline,time.monotonic_ns()+ACK_NS);remote_terminal=0
   reply_state=peer_pre_state;reply_ordinal=ordinal;reply_probe=probe
  try:send_abort(control,phase,reply_state,reply_ordinal,reply_probe,faults,response_deadline,remote_terminal)
  except BaseException as send_error:faults.update(error_faults(send_error,phase))
  if pid>=0 and not direct_wait_entered:
   direct_wait_entered=True
   try:wait_status(pid,0,release_origin+TOTAL_NS,b"DIRECT_WAIT_UNKNOWN");pid=-1
   except FaultSet as wait_error:faults.update(wait_error.faults)
  raised=FaultSet(faults);setattr(raised,"p27_abort_sent",True);setattr(raised,"p27_phase",phase);raise raised
 finally:
  close_numbers(tuple(number for number in (in_r,in_w,out_r,out_w,err_r,err_w,outer_fd,events,pidfd) if number>=0))

def mount_semantics(line,fstype,required,forbidden):
 pieces=line[:-1].split(b" - ");need(len(pieces)==2)
 left=pieces[0].split(b" ");right=pieces[1].split(b" ");need(len(left)>=6 and len(right)>=3 and right[0]==fstype)
 options=set(left[5].split(b","))|set(right[2].split(b","))
 need(required<=options and not (forbidden&options),Refuse)

def mount_graph(cert):
 number=-1
 try:
  number=actor_acquire_open(b"outer_mountinfo_fd",b"OUTER_MOUNTINFO_OBSERVATION_FD",b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(number,1048576),1048576)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))
 rows={}
 for line in raw.splitlines():
  left,right=line.split(b" - ",1);fields=left.split(b" ");need(len(fields)>=6,Refuse)
  mid=udec(fields[0],1);parent=udec(fields[1],1);options=set(fields[5].split(b","))
  need(mid not in rows,Refuse);rows[mid]=(parent,options)
 runtime=udec(cert[b"RUNTIME_ROOT_MOUNT_ID"],1);safe=udec(cert[b"SAFE_BIND_MOUNT_ID"],1)
 need(runtime in rows and safe in rows and runtime!=safe,Refuse)
 def descends(mid,ancestor):
  seen=set()
  while mid in rows and mid not in seen:
   if mid==ancestor:return True
   seen.add(mid);mid=rows[mid][0]
  return False
 writable=[mid for mid,(parent,options) in rows.items() if mid!=runtime and descends(mid,runtime) and b"rw" in options]
 need(writable==[safe] and cert[b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT"]==b"1",Refuse)

def base_identity(number,cert,prefix):
 held=os.fstat(number)
 expected=(udec(cert[prefix+b"_DEV"],1),udec(cert[prefix+b"_INO"],1),octal(cert[prefix+b"_MODE"]),udec(cert[prefix+b"_NLINK"],1),udec(cert[prefix+b"_UID"]),udec(cert[prefix+b"_GID"]))
 need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==expected,Refuse)
 return held

def signal_snapshot(cert):
 need(all(signal.getitimer(which)==(0.0,0.0) for which in (signal.ITIMER_REAL,signal.ITIMER_VIRTUAL,signal.ITIMER_PROF)),Refuse)
 previous=signal.pthread_sigmask(signal.SIG_BLOCK,set());need(previous==set(),Refuse)
 valid=tuple(sorted(int(x) for x in signal.valid_signals()))
 catchable=tuple(x for x in valid if x not in (int(signal.SIGKILL),int(signal.SIGSTOP)))
 defaults=[]
 for number in catchable:
  need(signal.getsignal(number)==signal.SIG_DFL,Refuse);defaults.append(str(number).encode()+b":DFL\n")
 need(len(valid)==udec(cert[b"VALID_SIGNAL_COUNT"]) and len(defaults)==udec(cert[b"DEFAULT_SIGNAL_COUNT"]),Refuse)
 need(sha(b"".join(defaults))==cert[b"DEFAULTS_SHA256"],Refuse)

def b_send(control,raw,deadline):
 send_plain(control,raw,deadline)

def request_refusal(control,begin_state,arm_state,reason,inherited_deadline):
 if (begin_state,arm_state)==(b"BEGIN_NOT_ENTERED",b"ARM_NOT_OBSERVED"):
  kind=b"V15_REFUSE_PREBEGIN";cross_state=b"ARM_NOT_ENTERED";origin=time.monotonic_ns();closure_deadline=origin+REFUSAL_TOTAL_NS
 elif (begin_state,arm_state)==(b"BEGIN_SENT",b"ARMED_CONFIRMED"):
  kind=b"V15_REFUSE_POSTARM";cross_state=b"REFUSAL_CLOSED_NO_CONSUME";closure_deadline=inherited_deadline;origin=closure_deadline-REFUSAL_TOTAL_NS
 else:raise ConsumedIndeterminate("refusal-cross-map")
 need(time.monotonic_ns()<=origin+REFUSAL_RECORD_NS and closure_deadline<=inherited_deadline,ConsumedIndeterminate)
 schedule=exact_schedule(origin,closure_deadline,REFUSAL_PHASE_SPEC);request_deadline=schedule[b"REFUSAL_RECORD"]
 finality_deadline=schedule[b"REFUSAL_FINALITY"]
 need(finality_deadline==origin+REFUSAL_FINALITY_NS and closure_deadline==schedule[b"REFUSAL_CLOSURE"] and finality_deadline<closure_deadline and closure_deadline-finality_deadline==REFUSAL_CLOSURE_TAIL_NS,ConsumedIndeterminate)
 raw=packet(kind,((b"state",b"REFUSE_PREBEGIN" if kind==b"V15_REFUSE_PREBEGIN" else b"REFUSE_POSTARM"),(b"expected_state",b"WAIT_BEGIN" if kind==b"V15_REFUSE_PREBEGIN" else b"WAIT_COMMIT"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH_ID),(b"a_begin_state",begin_state),(b"a_arm_state",arm_state),(b"cross_map_state",cross_state),(b"reason",reason),(b"refusal_origin_ns",str(origin).encode()),(b"refusal_finality_deadline_ns",str(finality_deadline).encode()),(b"refusal_closure_deadline_ns",str(closure_deadline).encode()),(b"refusal_schedule_hex",schedule_hex(schedule,REFUSAL_PHASE_SPEC)),(b"consume_deadline_ns",str(request_deadline).encode())))
 request_send_state=b"REFUSAL_REQUEST_EFFECT_UNKNOWN"
 try:send_plain(control,raw,request_deadline);request_send_state=b"REFUSAL_REQUEST_SENT"
 except SendEffectUnknown:request_send_state=b"REFUSAL_REQUEST_EFFECT_UNKNOWN"
 ack_deadline=schedule[b"REFUSAL_ACK"]
 ack_raw=recv_control(control,ack_deadline)
 ack=parse_packet(ack_raw,b"V15_REFUSE_ACK",(b"state",b"ordinal",b"probe",b"auth_id",b"a_begin_state",b"a_arm_state",b"cross_map_state",b"request_packet_sha256",b"request_message_seq",b"commit_count",b"attempt_state",b"intent_count",b"disposition",b"refusal_origin_ns",b"refusal_finality_deadline_ns",b"refusal_closure_deadline_ns",b"refusal_schedule_hex",b"consume_deadline_ns"),receiver_binding(b"WAIT_REFUSAL_ACK",b"NONE",b"NONE",ack_deadline))
 need(ack[b"state"]==b"REFUSAL_CLOSED_NO_CONSUME" and ack[b"expected_state"]==b"WAIT_REFUSAL_ACK" and ack[b"effect_state"]==b"REFUSAL_ACK_SEND_EFFECT_UNKNOWN",ConsumedIndeterminate)
 need(ack[b"ordinal"]==ack[b"probe"]==b"NONE" and ack[b"auth_id"]==AUTH_ID and ack[b"a_begin_state"]==begin_state and ack[b"a_arm_state"]==arm_state,ConsumedIndeterminate)
 need(ack[b"cross_map_state"]==cross_state and ack[b"request_packet_sha256"]==sha(raw) and ack[b"request_message_seq"]==str(CONTROL_SEND_SEQ).encode(),ConsumedIndeterminate)
 need(ack[b"commit_count"]==b"0" and ack[b"attempt_state"]==b"ABSENT_KNOWN" and ack[b"intent_count"]==b"0" and ack[b"disposition"]==b"UNCONSUMED",ConsumedIndeterminate)
 need(udec(ack[b"refusal_origin_ns"])==origin and udec(ack[b"refusal_finality_deadline_ns"])==finality_deadline and udec(ack[b"refusal_closure_deadline_ns"])==closure_deadline and ack[b"refusal_schedule_hex"]==schedule_hex(schedule,REFUSAL_PHASE_SPEC),ConsumedIndeterminate)
 receipt_deadline=finality_deadline
 receipt=packet(b"V15_REFUSE_ACK_RECEIPT",((b"state",b"REFUSAL_ACK_RECEIVED"),(b"expected_state",b"WAIT_REFUSAL_RECEIPT"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"ack_packet_sha256",sha(ack_raw)),(b"ack_message_seq",ack[b"message_seq"]),(b"request_packet_sha256",sha(raw)),(b"cross_map_state",cross_state),(b"no_replay",b"1"),(b"refusal_finality_deadline_ns",str(finality_deadline).encode()),(b"refusal_closure_deadline_ns",str(closure_deadline).encode()),(b"refusal_schedule_hex",schedule_hex(schedule,REFUSAL_PHASE_SPEC)),(b"consume_deadline_ns",str(receipt_deadline).encode())))
 receipt_send_state=b"REFUSAL_RECEIPT_EFFECT_UNKNOWN"
 try:send_plain(control,receipt,receipt_deadline);receipt_send_state=b"REFUSAL_RECEIPT_SENT"
 except SendEffectUnknown:receipt_send_state=b"REFUSAL_RECEIPT_EFFECT_UNKNOWN"
 actor_closure_deadline=schedule[b"REFUSAL_ACTOR_CLOSURE"];closed_raw=recv_control(control,actor_closure_deadline)
 closed=parse_packet(closed_raw,b"V15_REFUSAL_CLOSED",(b"state",b"ordinal",b"probe",b"ack_packet_sha256",b"receipt_packet_sha256",b"cross_map_state",b"issuer_closure_sha256",b"issuer_record_seq",b"issuer_predecessor_sha256",b"no_replay",b"refusal_finality_deadline_ns",b"refusal_closure_deadline_ns",b"refusal_schedule_hex",b"consume_deadline_ns"),receiver_binding(b"WAIT_REFUSAL_CLOSED",b"NONE",b"NONE",actor_closure_deadline))
 need(closed[b"state"]==b"REFUSAL_DURABLY_CLOSED" and closed[b"expected_state"]==b"WAIT_REFUSAL_CLOSED" and closed[b"effect_state"]==b"OWNER_CLOSURE",ConsumedIndeterminate)
 need(closed[b"ordinal"]==closed[b"probe"]==b"NONE" and closed[b"ack_packet_sha256"]==sha(ack_raw) and closed[b"receipt_packet_sha256"]==sha(receipt),ConsumedIndeterminate)
 need(closed[b"cross_map_state"]==cross_state and h64(closed[b"issuer_closure_sha256"])!=b"0"*64 and udec(closed[b"issuer_record_seq"],1)>=1 and h64(closed[b"issuer_predecessor_sha256"])!=b"0"*64,ConsumedIndeterminate)
 need(closed[b"no_replay"]==b"1" and udec(closed[b"refusal_finality_deadline_ns"])==finality_deadline and udec(closed[b"refusal_closure_deadline_ns"])==closure_deadline and closed[b"refusal_schedule_hex"]==schedule_hex(schedule,REFUSAL_PHASE_SPEC),ConsumedIndeterminate)
 return {b"request_raw":raw,b"ack_raw":ack_raw,b"receipt_raw":receipt,b"closed_raw":closed_raw,b"cross_state":cross_state,b"request_send_state":request_send_state,b"receipt_send_state":receipt_send_state,b"refusal_finality_deadline":finality_deadline,b"refusal_closure_deadline":closure_deadline}

def failure_recv(control,deadline,actual_pre_state,stop_probe):
 while True:
  raw=recv_control(control,deadline)
  if not raw.startswith(b"V15_ABORT|"):return raw
  try:
   binding=received_binding(raw,actual_pre_state,b"NONE",stop_probe,b"control_deadline_ns",deadline)
   values,faults=parse_abort(raw,b"B",binding);need(values[b"causal_state"]==b"CLEANUP_RELEASE_DISABLE")
   remote_deadline=udec(values[b"terminal_deadline_ns"],1);response_deadline=udec(values[b"control_deadline_ns"],1)
   need(time.monotonic_ns()<=response_deadline<=remote_deadline<=deadline)
   send_abort(control,b"CLEANUP_RELEASE_DISABLED",b"WAIT_RELEASE_DISABLE_ACK",None,values[b"probe"],faults,response_deadline,remote_deadline)
  except FaultSet:raise

def await_failure_terminal(control,outer_deadline,stop_probe):
 notice_raw=failure_recv(control,outer_deadline,b"WAIT_TERMINAL_FAILURE",stop_probe)
 values=parse_packet(notice_raw,b"V15_TERMINAL_FAILURE_DURABLE",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"chain_head_sha256",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"candidate_deadline_ns",b"disposition"),received_binding(notice_raw,b"WAIT_TERMINAL_FAILURE",b"NONE",b"NONE",b"candidate_deadline_ns",outer_deadline))
 subject=h64(values[b"subject_sha256"]);origin=udec(values[b"terminal_origin_ns"],1);deadline=udec(values[b"terminal_deadline_ns"],1)
 need(values[b"state"]==b"TERMINAL_FAILURE_DURABLE" and values[b"expected_state"]==b"WAIT_TERMINAL_FAILURE" and values[b"effect_state"]==b"FAILURE_REPORT_DURABLE")
 need(values[b"ordinal"]==values[b"probe"]==b"NONE" and values[b"kind"]==b"FAILURE_CANDIDATE" and values[b"disposition"] in (b"CONSUMED_FAIL",b"CONSUMED_INDETERMINATE"))
 need(time.monotonic_ns()<=deadline<=outer_deadline and deadline==origin+FINAL_TOTAL_NS);schedule=check_schedule_hex(values[b"terminal_schedule_hex"],origin,deadline,TERMINAL_PHASE_SPEC)
 need(udec(values[b"candidate_deadline_ns"])==schedule[b"NOTICE"])
 seen_deadline=schedule[b"TERMINAL_SEEN_RECORD"]
 seen=packet(b"V15_TERMINAL_SEEN",((b"state",b"TERMINAL_SEEN"),(b"expected_state",b"WAIT_TERMINAL_SEEN"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",b"FAILURE_CANDIDATE"),(b"subject_sha256",subject),(b"notice_packet_sha256",sha(notice_raw)),(b"terminal_origin_ns",str(origin).encode()),(b"terminal_deadline_ns",str(deadline).encode()),(b"terminal_schedule_hex",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"seen_deadline_ns",str(seen_deadline).encode())))
 send_plain(control,seen,seen_deadline)
 ack_deadline=schedule[b"ACK"];ack_raw=failure_recv(control,ack_deadline,b"WAIT_TERMINAL_ACK",stop_probe)
 ack=parse_packet(ack_raw,b"V15_TERMINAL_ACK",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"terminal_seen_sha256",b"report_sha256",b"pass_sha256",b"reconciliation_token",b"ack_state",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"ack_deadline_ns"),receiver_binding(b"WAIT_TERMINAL_ACK",b"NONE",b"NONE",ack_deadline))
 need(ack[b"state"]==b"TERMINAL_ACK" and ack[b"expected_state"]==b"WAIT_TERMINAL_ACK" and ack[b"ordinal"]==ack[b"probe"]==b"NONE" and ack[b"kind"]==b"FAILURE_CANDIDATE" and ack[b"subject_sha256"]==subject)
 report_sha=h64(ack[b"report_sha256"]);need(ack[b"pass_sha256"]==ack[b"reconciliation_token"]==b"NONE" and ack[b"ack_state"]==b"FAILURE_DURABLE")
 need(udec(ack[b"terminal_origin_ns"])==origin and udec(ack[b"terminal_deadline_ns"])==deadline and ack[b"terminal_schedule_hex"]==schedule_hex(schedule,TERMINAL_PHASE_SPEC))
 receipt_deadline=schedule[b"A_RECEIPT"];receipt_ns=time.monotonic_ns()
 receipt=packet(b"V15_TERMINAL_ACK_RECEIPT",((b"state",b"ACK_RECEIVED_NO_REPLAY"),(b"expected_state",b"WAIT_ACK_RECEIPT"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",b"FAILURE_CANDIDATE"),(b"subject_sha256",subject),(b"ack_packet_sha256",sha(ack_raw)),(b"report_sha256",report_sha),(b"pass_sha256",b"NONE"),(b"reconciliation_token",b"NONE"),(b"actor_receipt_ns",str(receipt_ns).encode()),(b"terminal_origin_ns",str(origin).encode()),(b"terminal_deadline_ns",str(deadline).encode()),(b"terminal_schedule_hex",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"receipt_deadline_ns",str(receipt_deadline).encode())))
 send_plain(control,receipt,receipt_deadline)
 closure_deadline=schedule[b"CLOSURE_PACKET"];closed=parse_packet(failure_recv(control,closure_deadline,b"WAIT_OWNER_CLOSED",stop_probe),b"V15_TERMINAL_CLOSED",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"report_sha256",b"pass_sha256",b"ack_receipt_sha256",b"reconciliation_sha256",b"closure_sha256",b"owner",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"closure_deadline_ns"),receiver_binding(b"WAIT_OWNER_CLOSED",b"NONE",b"NONE",closure_deadline))
 need(closed[b"state"]==b"OWNER_CLOSED" and closed[b"expected_state"]==b"WAIT_OWNER_CLOSED" and closed[b"ordinal"]==closed[b"probe"]==b"NONE" and closed[b"kind"]==b"FAILURE_CANDIDATE")
 need(closed[b"subject_sha256"]==subject and closed[b"report_sha256"]==report_sha and closed[b"pass_sha256"]==b"NONE" and closed[b"owner"]==b"B")
 for key in (b"ack_receipt_sha256",b"reconciliation_sha256",b"closure_sha256"):need(h64(closed[key])!=b"0"*64)
 need(udec(closed[b"terminal_origin_ns"])==origin and udec(closed[b"terminal_deadline_ns"])==deadline and closed[b"terminal_schedule_hex"]==schedule_hex(schedule,TERMINAL_PHASE_SPEC))
 return values[b"disposition"],deadline

def main():
 global AUTH_ID,PREFLIGHT,CERT,STAGE_PRESENT,B_CHILD_PID,B_CONTROL
 actor_bootstrap_registry()
 entry_mono=time.monotonic_ns();state=b"INPUT";consumed=False;commit_edge=False;peer_pre_state=b"WAIT_BEGIN";peer_deadline=entry_mono+PRECONSUME_NS
 begin_effect_possible=False;begin_state=b"BEGIN_NOT_ENTERED";arm_state=b"ARM_NOT_OBSERVED";refusal_acked=False
 pass_may_be_committed=False;pass_authoritative=False;receipt_effect_unknown=False;terminal_deadline=0;failure_terminal_deadline=0
 bpid=-1;control=None;runtime=attempt_base=stage_base=cgroup_base=safefd=cgfd=-1
 need(type(sys.argv)is list and len(sys.argv)==3 and sys.argv[0]=="/proc/self/fd/100" and sys.argv[1]=="RUN_V19",Refuse)
 supplied=h64(sys.argv[2].encode("ascii"))
 need(os.environb==ENV and os.read(0,1)==b"" and sys.gettrace() is None and sys.getprofile() is None,Refuse)
 verify_creds(False);need(os.umask(0o077)==0o077,Refuse)
 fd0=os.fstat(0);fd1=os.fstat(1);fd2=os.fstat(2)
 need(stat.S_ISFIFO(fd0.st_mode) and stat.S_ISFIFO(fd1.st_mode) and stat.S_ISFIFO(fd2.st_mode),Refuse)
 fd_access(0,os.O_RDONLY);fd_access(1,os.O_WRONLY);fd_access(2,os.O_WRONLY)
 need((fd1.st_dev,fd1.st_ino)!=(fd2.st_dev,fd2.st_ino),Refuse)
 close_range(3,99);close_range(111,UINT_MAX);scrub_exact({0,1,2,100,101,102,103,104,105,106,107,108,109,110})
 fd_access(102,os.O_RDONLY)
 actor_raw=sealed_carrier(100,MAX_FILE);snapshot=exact_snapshot(101)
 v15=exact_whole(102,WHOLE_V15,V15_TERMINAL);plan=sealed_carrier(103,MAX_FILE)
 cert_raw=sealed_carrier(104,MAX_FILE);envelope_raw=sealed_carrier(105,MAX_FILE);b_raw=sealed_carrier(106,MAX_FILE);reservation_raw=sealed_carrier(107,MAX_FILE);transfer_manifest_raw=sealed_carrier(110,MAX_FILE)
 state=b"CERT";envelope=parse_envelope(envelope_raw);CERT,deps=parse_cert(cert_raw);reservation=parse_reservation(reservation_raw)
 context_digest,certificate_digest,receipt_digest=verify_issuer_order(envelope,cert_raw,CERT);reservation_digest=verify_reservation_order(reservation,cert_raw,envelope_raw,envelope)
 AUTH_ID=session_auth(cert_raw,envelope_raw,reservation_raw);need(AUTH_ID==supplied,Refuse)
 need(envelope[b"PLAN_SHA256"]==CERT[b"PLAN_SHA256"] and envelope[b"RUNNER_SHA256"]==CERT[b"RUNNER_SHA256"] and envelope[b"RECOVERY_SHA256"]==CERT[b"RECOVERY_SHA256"],Refuse)
 need((len(transfer_manifest_raw),sha(transfer_manifest_raw))==(udec(CERT[b"EXTERNAL_TRANSFER_MANIFEST_BYTES"],1),CERT[b"EXTERNAL_TRANSFER_MANIFEST_SHA256"]),Refuse)
 parse_external_manifest(transfer_manifest_raw,CERT);verify_external_inputs(CERT)
 need(reservation[b"NOT_BEFORE_REALTIME_NS"]==envelope[b"NOT_BEFORE_REALTIME_NS"] and reservation[b"NOT_AFTER_REALTIME_NS"]==envelope[b"NOT_AFTER_REALTIME_NS"],Refuse)
 need(sha(plan)==CERT[b"PLAN_SHA256"] and sha(actor_raw)==CERT[b"RUNNER_SHA256"] and sha(b_raw)==CERT[b"RECOVERY_SHA256"],Refuse)
 v19_validate_raw_contract(actor_raw,b_raw)
 need(envelope[b"E0366_SNAPSHOT_SHA256"]==CERT[b"E0366_SNAPSHOT_SHA256"]==sha(snapshot),Refuse)
 need(envelope[b"E0366_SNAPSHOT_BYTES"]==CERT[b"E0366_SNAPSHOT_BYTES"]==b"2303269" and envelope[b"E0366_SNAPSHOT_LF"]==CERT[b"E0366_SNAPSHOT_LF"]==b"23672",Refuse)
 need(envelope[b"E0366_SNAPSHOT_TERMINAL_HEX"]==CERT[b"E0366_SNAPSHOT_TERMINAL_HEX"]==SNAPSHOT_TERMINAL_HEX,Refuse)
 not_before=udec(CERT[b"NOT_BEFORE_REALTIME_NS"]);expiry=udec(CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 need(expiry-not_before==CERT_LIFE_NS and udec(envelope[b"NOT_BEFORE_REALTIME_NS"])<=not_before<expiry<=udec(envelope[b"NOT_AFTER_REALTIME_NS"]),Refuse)
 checkpoint(CERT,horizon_needed(entry_mono+PRECONSUME_NS,CONSUME_REMAIN_NS),Refuse,entry_mono+PRECONSUME_NS);verify_platform(CERT);signal_snapshot(CERT)
 ab=b"P27 RUNNER V20 ACTOR SOURCE "+b"BEGIN 6C20A4F1";ae=b"P27 RUNNER V20 ACTOR SOURCE "+b"END 6C20A4F1"
 bb=b"P27 RUNNER V20 WATCHDOG SOURCE "+b"BEGIN 9F20C6A3";be=b"P27 RUNNER V20 WATCHDOG SOURCE "+b"END 9F20C6A3"
 need(extract_one(plan,ab,ae)==actor_raw and extract_one(plan,bb,be)==b_raw,Refuse)
 sources=v15_sources(v15)
 state=b"ENTRY"
 try:
  runtime=open_dir(RUNTIME_ROOT);actor_promote_record(actor_live_owner(runtime),b"runtime_root_fd")
  attempt_base=open_dir(ATTEMPT_BASE);actor_promote_record(actor_live_owner(attempt_base),b"runtime_attempt_base_fd")
  stage_base=open_dir(STAGE_BASE);actor_promote_record(actor_live_owner(stage_base),b"runtime_stage_base_fd")
  cgroup_base=open_dir(CGROUP_BASE);actor_promote_record(actor_live_owner(cgroup_base),b"runtime_cgroup_base_fd")
  runtime_stat=base_identity(runtime,CERT,b"RUNTIME_ROOT");runtime_mid,runtime_line=mount_line(runtime)
  need(runtime_mid==udec(CERT[b"RUNTIME_ROOT_MOUNT_ID"],1) and sha(runtime_line)==CERT[b"RUNTIME_ROOT_MOUNTINFO_SHA256"],Refuse)
  mount_semantics(runtime_line,even_hex(CERT[b"RUNTIME_ROOT_FSTYPE_HEX"]),{b"ro",b"nosuid",b"nodev"},{b"rw"})
  for entry in deps:verify_dependency(runtime,entry)
  attempt_stat=base_identity(attempt_base,CERT,b"ATTEMPT_BASE");attempt_mid,attempt_line=mount_line(attempt_base)
  need(attempt_mid==udec(CERT[b"ATTEMPT_BASE_MOUNT_ID"],1) and sha(attempt_line)==CERT[b"ATTEMPT_BASE_MOUNTINFO_SHA256"],Refuse)
  mount_semantics(attempt_line,even_hex(CERT[b"ATTEMPT_BASE_FSTYPE_HEX"]),{b"rw",b"nosuid",b"nodev"},{b"ro"})
  stage_stat=base_identity(stage_base,CERT,b"SAFE_BIND");stage_mid,stage_line=mount_line(stage_base)
  need(stage_mid==udec(CERT[b"SAFE_BIND_MOUNT_ID"],1) and sha(stage_line)==CERT[b"SAFE_BIND_MOUNTINFO_SHA256"],Refuse)
  mount_semantics(stage_line,even_hex(CERT[b"SAFE_BIND_FSTYPE_HEX"]),{b"rw",b"nosuid",b"nodev",b"noexec"},{b"ro"})
  cgroup_stat=base_identity(cgroup_base,CERT,b"CGROUP_BASE");cg_mid,cg_line=mount_line(cgroup_base)
  need(statfs_magic(cgroup_base)==CGROUP2_MAGIC and cg_mid==udec(CERT[b"CGROUP2_MOUNT_ID"],1) and sha(cg_line)==CERT[b"CGROUP2_MOUNTINFO_SHA256"],Refuse)
  mount_semantics(cg_line,b"cgroup2",{b"rw"},{b"ro"})
  base_type=base_controllers=base_subtree=-1
  try:
   base_type=actor_acquire_open(b"base_type_fd",b"BASE_TYPE_OBSERVATION_FD",b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgroup_base)
   base_controllers=actor_acquire_open(b"base_controllers_fd",b"BASE_CONTROLLERS_OBSERVATION_FD",b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgroup_base)
   base_subtree=actor_acquire_open(b"base_subtree_fd",b"BASE_SUBTREE_OBSERVATION_FD",b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgroup_base)
   need(read_all(base_type,128).hex().encode()==CERT[b"CGROUP_BASE_TYPE_HEX"],Refuse)
   need(read_all(base_controllers,4096).hex().encode()==CERT[b"CGROUP_BASE_CONTROLLERS_HEX"],Refuse)
   need(read_all(base_subtree,4096).hex().encode()==CERT[b"CGROUP_BASE_SUBTREE_CONTROL_HEX"],Refuse)
  finally:close_numbers((base_type,base_controllers,base_subtree))
  need(runtime_mid!=stage_mid,Refuse);mount_graph(CERT)
  absent(attempt_base,AUTH_ID,Refuse);absent(stage_base,AUTH_ID,Refuse);absent(cgroup_base,AUTH_ID,Refuse)
  need(time.monotonic_ns()-entry_mono<=PRECONSUME_NS,Refuse)
  bases={b"attempt_fd":attempt_base,b"cgroup_fd":cgroup_base,b"safe":stage_stat}
  state=b"B_BOOT";bpid,control=launch_b(CERT,bases);need(B_CHILD_PID==bpid and B_CONTROL is control and fcntl.fcntl(control.fileno(),fcntl.F_GETFL)&os.O_NONBLOCK,Refuse)
  actor_close_number(attempt_base);attempt_base=-1
  ready_deadline=entry_mono+PRECONSUME_NS;peer_pre_state=b"WAIT_BEGIN";peer_deadline=ready_deadline
  ready_raw=recv_control(control,ready_deadline)
  ready=parse_packet(ready_raw,b"V15_READY",(b"state",b"ordinal",b"probe"),received_binding(ready_raw,b"WAIT_READY",b"NONE",b"NONE",b"ready_deadline_ns",ready_deadline))
  need(ready[b"state"]==b"READY" and ready[b"ordinal"]==ready[b"probe"]==b"NONE",Refuse)
  checkpoint(CERT,CONSUME_REMAIN_NS,Refuse,ready_deadline)
  consume_origin=time.monotonic_ns();consume_deadline=consume_origin+CONSUMPTION_NS
  checkpoint(CERT,CONSUME_REMAIN_NS,Refuse,consume_deadline)
  state=b"BEGIN_SEND_EFFECT_UNKNOWN";begin_state=b"BEGIN_SEND_EFFECT_UNKNOWN";begin_effect_possible=True
  begin=packet(b"V15_CONSUME_BEGIN",((b"state",b"CONSUME_BEGIN"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH_ID),(b"a_begin_state",begin_state),(b"a_arm_state",arm_state),(b"consume_origin_ns",str(consume_origin).encode()),(b"consume_deadline_ns",str(consume_deadline).encode())))
  b_send(control,begin,consume_deadline);begin_state=b"BEGIN_SENT";state=b"BEGIN_SENT"
  arm_state=b"ARM_RECEIVE_EFFECT_UNKNOWN";state=b"ARM_RECEIVE_EFFECT_UNKNOWN"
  armed=parse_packet(recv_control(control,consume_deadline),b"V15_CONSUME_ARMED",(b"state",b"ordinal",b"probe",b"auth_id",b"a_begin_state",b"b_arm_state",b"consume_origin_ns",b"consume_deadline_ns"),receiver_binding(b"WAIT_ARM",b"NONE",b"NONE",consume_deadline))
  need(armed[b"state"]==b"CONSUME_ARMED" and armed[b"ordinal"]==armed[b"probe"]==b"NONE" and armed[b"auth_id"]==AUTH_ID)
  need(armed[b"a_begin_state"]==b"BEGIN_SEND_EFFECT_UNKNOWN" and armed[b"b_arm_state"]==b"ARM_SEND_EFFECT_UNKNOWN")
  need(udec(armed[b"consume_origin_ns"])==consume_origin and udec(armed[b"consume_deadline_ns"])==consume_deadline)
  arm_state=b"ARMED_CONFIRMED";state=b"ARMED_CONFIRMED";peer_pre_state=b"WAIT_COMMIT";peer_deadline=consume_deadline
  commit_edge=True;consumed=True;PREFLIGHT=False;state=b"COMMIT_SEND_EFFECT_UNKNOWN"
  commit=packet(b"V15_CONSUME_COMMIT",((b"state",b"CONSUME_COMMIT"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH_ID),(b"a_begin_state",begin_state),(b"a_arm_state",arm_state),(b"a_commit_state",b"COMMIT_SEND_EFFECT_UNKNOWN"),(b"consume_origin_ns",str(consume_origin).encode()),(b"consume_deadline_ns",str(consume_deadline).encode())))
  b_send(control,commit,consume_deadline);state=b"COMMIT_SENT";peer_pre_state=b"WAIT_STAGE"
  consumed_msg=parse_packet(recv_control(control,consume_deadline),b"V15_CONSUMED_DURABLE",(b"state",b"ordinal",b"probe",b"auth_id",b"intent_sha256",b"consume_origin_ns",b"consume_deadline_ns",b"attempt_fd_state"),receiver_binding(b"WAIT_CONSUMED",b"NONE",b"NONE",consume_deadline))
  need(consumed_msg[b"state"]==b"CONSUMED_DURABLE" and consumed_msg[b"ordinal"]==consumed_msg[b"probe"]==b"NONE" and consumed_msg[b"auth_id"]==AUTH_ID)
  need(udec(consumed_msg[b"consume_origin_ns"])==consume_origin and udec(consumed_msg[b"consume_deadline_ns"])==consume_deadline and consumed_msg[b"attempt_fd_state"]==b"PUBLISHED")
  chain_sha=h64(consumed_msg[b"intent_sha256"]);checkpoint(CERT,PRE_STAGE_REMAIN_NS,ConsumedIndeterminate,consume_deadline)
  state=b"STAGE";stage_origin=time.monotonic_ns();stage_deadline=stage_origin+STAGE_NS;peer_pre_state=b"WAIT_STAGE";peer_deadline=stage_deadline
  checkpoint(CERT,PRE_STAGE_REMAIN_NS,ConsumedIndeterminate,stage_deadline)
  os.mkdir(AUTH_ID,0o700,dir_fd=stage_base);progress(CERT,stage_deadline,horizon_needed(stage_deadline,POST_STAGE_REMAIN_NS));os.fsync(stage_base);progress(CERT,stage_deadline,horizon_needed(stage_deadline,POST_STAGE_REMAIN_NS))
  safefd=actor_acquire_open(b"stage_safe_fd",b"STAGE_SAFE_DIRFD",AUTH_ID,O_DIR,dir_fd=stage_base);progress(CERT,stage_deadline,horizon_needed(stage_deadline,POST_STAGE_REMAIN_NS));safe=os.fstat(safefd)
  need((safe.st_uid,safe.st_gid,stat.S_IMODE(safe.st_mode),safe.st_nlink)==(0,0,0o700,2),ConsumedIndeterminate)
  named=os.stat(AUTH_ID,dir_fd=stage_base,follow_symlinks=False)
  need((named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid)==(safe.st_dev,safe.st_ino,safe.st_mode,safe.st_nlink,safe.st_uid,safe.st_gid),ConsumedIndeterminate)
  for name in (b"target",b"a",b"b"):absent(safefd,name)
  for name,body,identity in zip(SOURCE_NAMES,sources[1:],SOURCE_META[1:]):stage_leaf(safefd,name,body,identity,stage_deadline)
  os.fsync(safefd);progress(CERT,stage_deadline,POST_STAGE_REMAIN_NS)
  STAGE_PRESENT=True
  staged=packet(b"V15_STAGE_DURABLE",((b"state",b"STAGE_DURABLE"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"stage_origin_ns",str(stage_origin).encode()),(b"stage_deadline_ns",str(stage_deadline).encode()),(b"stage_return_ns",str(time.monotonic_ns()).encode()),(b"safe_dev",str(safe.st_dev).encode()),(b"safe_ino",str(safe.st_ino).encode()),(b"safe_mode",format(safe.st_mode,"o").encode()),(b"safe_nlink",str(safe.st_nlink).encode()),(b"safe_uid",str(safe.st_uid).encode()),(b"safe_gid",str(safe.st_gid).encode()),(b"keeper_sha256",CERT[b"KEEPER_SHA256"]),(b"launcher_sha256",CERT[b"LAUNCHER_SHA256"]),(b"marker_sha256",CERT[b"MARKER_SHA256"]),(b"child_sha256",CERT[b"CHILD_SHA256"])))
  send_rights(control,staged,(safefd,),stage_deadline)
  stage_ack=parse_packet(recv_control(control,stage_deadline),b"V15_STAGE_ACK",(b"state",b"ordinal",b"probe",b"stage_deadline_ns",b"safe_dev",b"safe_ino"),receiver_binding(b"WAIT_STAGE_ACK",b"NONE",b"NONE",stage_deadline))
  need(stage_ack[b"state"]==b"STAGE_BOUND" and stage_ack[b"ordinal"]==stage_ack[b"probe"]==b"NONE")
  need(udec(stage_ack[b"stage_deadline_ns"])==stage_deadline and (udec(stage_ack[b"safe_dev"]),udec(stage_ack[b"safe_ino"]))==(safe.st_dev,safe.st_ino))
  progress(CERT,stage_deadline,POST_STAGE_REMAIN_NS)
  state=b"CONTAIN";contain_origin=time.monotonic_ns();contain_deadline=contain_origin+ACK_NS;peer_pre_state=b"WAIT_CONTAINMENT";peer_deadline=contain_deadline
  os.mkdir(AUTH_ID,0o700,dir_fd=cgroup_base);progress(CERT,contain_deadline,horizon_needed(contain_deadline,POST_CONTAIN_REMAIN_NS))
  cgfd=actor_acquire_open(b"containment_cgroup_fd",b"CONTAINMENT_CGROUP_DIRFD",AUTH_ID,O_DIR,dir_fd=cgroup_base);progress(CERT,contain_deadline,horizon_needed(contain_deadline,POST_CONTAIN_REMAIN_NS));cgchild=os.fstat(cgfd)
  need((format(cgchild.st_mode,"o").encode(),cgchild.st_uid,cgchild.st_gid,cgchild.st_nlink)==(CERT[b"CGROUP_CHILD_MODE"],0,0,2),ConsumedIndeterminate)
  need(cgroup_empty(cgfd),ConsumedIndeterminate)
  ctype=controllers=subtree=-1
  try:
   ctype=actor_acquire_open(b"containment_type_fd",b"CONTAINMENT_TYPE_OBSERVATION_FD",b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
   controllers=actor_acquire_open(b"containment_controllers_fd",b"CONTAINMENT_CONTROLLERS_OBSERVATION_FD",b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
   subtree=actor_acquire_open(b"containment_subtree_fd",b"CONTAINMENT_SUBTREE_OBSERVATION_FD",b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
   type_raw=read_all(ctype,128);controllers_raw=read_all(controllers,4096);subtree_raw=read_all(subtree,4096)
   need(type_raw.hex().encode()==CERT[b"CGROUP_CHILD_TYPE_HEX"],ConsumedIndeterminate)
   need(controllers_raw.hex().encode()==CERT[b"CGROUP_CHILD_CONTROLLERS_HEX"],ConsumedIndeterminate)
   need(subtree_raw.hex().encode()==CERT[b"CGROUP_CHILD_SUBTREE_CONTROL_HEX"],ConsumedIndeterminate)
  finally:close_numbers(tuple(x for x in (ctype,controllers,subtree) if x>=0))
  cgbase=os.fstat(cgroup_base);cg_mid,cg_line=mount_line(cgfd)
  containment=packet(b"V15_CONTAINMENT",((b"state",b"CONTAINMENT_CANDIDATE"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"contain_origin_ns",str(contain_origin).encode()),(b"contain_deadline_ns",str(contain_deadline).encode()),(b"dev",str(cgchild.st_dev).encode()),(b"ino",str(cgchild.st_ino).encode()),(b"mode",format(cgchild.st_mode,"o").encode()),(b"nlink",str(cgchild.st_nlink).encode()),(b"uid",str(cgchild.st_uid).encode()),(b"gid",str(cgchild.st_gid).encode()),(b"base_dev",str(cgbase.st_dev).encode()),(b"base_ino",str(cgbase.st_ino).encode()),(b"mount_id",str(cg_mid).encode()),(b"mountinfo_sha256",sha(cg_line)),(b"type_hex",type_raw.hex().encode()),(b"controllers_hex",controllers_raw.hex().encode()),(b"subtree_control_hex",subtree_raw.hex().encode())))
  send_rights(control,containment,(cgfd,),contain_deadline)
  contain_ack=parse_packet(recv_control(control,contain_deadline),b"V15_CONTAINMENT_ACK",(b"state",b"ordinal",b"probe",b"contain_deadline_ns",b"dev",b"ino"),receiver_binding(b"WAIT_CONTAINMENT_ACK",b"NONE",b"NONE",contain_deadline))
  need(contain_ack[b"state"]==b"CONTAINMENT_BOUND" and contain_ack[b"ordinal"]==contain_ack[b"probe"]==b"NONE")
  need(udec(contain_ack[b"contain_deadline_ns"])==contain_deadline and (udec(contain_ack[b"dev"]),udec(contain_ack[b"ino"]))==(cgchild.st_dev,cgchild.st_ino))
  progress(CERT,contain_deadline,POST_CONTAIN_REMAIN_NS)
  safe_path=STAGE_BASE+b"/"+AUTH_ID
  ctx={b"cwd_hex":safe_path.hex().encode(),b"python_dev":udec(CERT[b"PYTHON_IMAGE_DEV"],1),b"python_ino":udec(CERT[b"PYTHON_IMAGE_INO"],1),b"libc_path_hex":CERT[b"LIBC_PATH_HEX"],b"libc_confstr_hex":CERT[b"LIBC_CONFSTR_HEX"],b"libc_bytes":udec(CERT[b"LIBC_BYTES"],1),b"libc_sha":CERT[b"LIBC_SHA256"],b"valid_signals":udec(CERT[b"VALID_SIGNAL_COUNT"]),b"default_signals":udec(CERT[b"DEFAULT_SIGNAL_COUNT"]),b"defaults_sha":CERT[b"DEFAULTS_SHA256"],b"child_source":sources[4]}
  prior=None
  for ordinal,probe in enumerate(SUITE):
   checkpoint(CERT,(15-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS)
   p01c=derive_p01c(prior,CERT) if probe==b"P01C" else ()
   rows,chain_sha=run_probe(control,ordinal,probe,cgfd,safefd,safe,sources[0],ctx,p01c,CERT)
   if probe==b"P01D":prior=rows;ctx[b"p01d"]=rows
  state=b"REMOVE";remove_origin=time.monotonic_ns();remove_deadline=remove_origin+REPORT_NS;peer_pre_state=b"WAIT_EMPTY_QUERY";peer_deadline=remove_deadline
  checkpoint(CERT,REPORT_NS+FINAL_TOTAL_NS,ConsumedIndeterminate,remove_deadline);need(cgroup_empty(cgfd),ConsumedIndeterminate)
  query=packet(b"V15_EMPTY_FINAL_QUERY",((b"state",b"EMPTY_FINAL_QUERY"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"chain_head_sha256",chain_sha),(b"remove_origin_ns",str(remove_origin).encode()),(b"remove_deadline_ns",str(remove_deadline).encode())))
  b_send(control,query,remove_deadline)
  confirmed=parse_packet(recv_control(control,remove_deadline),b"V15_EMPTY_FINAL_CONFIRMED",(b"state",b"ordinal",b"probe",b"chain_head_sha256",b"remove_deadline_ns"),receiver_binding(b"WAIT_EMPTY_CONFIRMED",b"NONE",b"NONE",remove_deadline))
  need(confirmed[b"state"]==b"EMPTY_FINAL_CONFIRMED" and confirmed[b"ordinal"]==confirmed[b"probe"]==b"NONE" and h64(confirmed[b"chain_head_sha256"]) and udec(confirmed[b"remove_deadline_ns"])==remove_deadline)
  chain_sha=confirmed[b"chain_head_sha256"];peer_pre_state=b"WAIT_REMOVE_ACK"
  actor_close_number(cgfd);cgfd=-1;os.rmdir(AUTH_ID,dir_fd=cgroup_base)
  try:os.stat(AUTH_ID,dir_fd=cgroup_base,follow_symlinks=False);need(False,ConsumedIndeterminate)
  except FileNotFoundError:pass
  progress(CERT,remove_deadline,FINAL_TOTAL_NS)
  removed=packet(b"V15_CGROUP_REMOVED",((b"state",b"CGROUP_REMOVED"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"chain_head_sha256",chain_sha),(b"remove_deadline_ns",str(remove_deadline).encode())))
  b_send(control,removed,remove_deadline)
  removed_ack=parse_packet(recv_control(control,remove_deadline),b"V15_REMOVE_ACK",(b"state",b"ordinal",b"probe",b"chain_head_sha256",b"remove_deadline_ns"),receiver_binding(b"WAIT_REMOVE_ACK",b"NONE",b"NONE",remove_deadline))
  need(removed_ack[b"state"]==b"REMOVE_ACK" and removed_ack[b"ordinal"]==removed_ack[b"probe"]==b"NONE" and removed_ack[b"chain_head_sha256"]==chain_sha and udec(removed_ack[b"remove_deadline_ns"])==remove_deadline)
  state=b"FINAL";terminal_origin=time.monotonic_ns();terminal_deadline=terminal_origin+FINAL_TOTAL_NS;schedule=exact_schedule(terminal_origin,terminal_deadline,TERMINAL_PHASE_SPEC);peer_pre_state=b"WAIT_FINALIZE";peer_deadline=schedule[b"CANDIDATE_RECORD"]
  checkpoint(CERT,FINAL_TOTAL_NS,ConsumedIndeterminate,schedule[b"CANDIDATE_RECORD"])
  finalize=packet(b"V15_FINALIZE_CANDIDATE",((b"state",b"FINALIZE_CANDIDATE"),(b"expected_state",b"WAIT_FINALIZE"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"chain_head_sha256",chain_sha),(b"terminal_origin_ns",str(terminal_origin).encode()),(b"terminal_deadline_ns",str(terminal_deadline).encode()),(b"terminal_schedule_hex",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"candidate_deadline_ns",str(schedule[b"CANDIDATE_RECORD"]).encode())))
  b_send(control,finalize,schedule[b"CANDIDATE_RECORD"])
  notice_deadline=schedule[b"NOTICE"];notice_raw=recv_control(control,notice_deadline)
  candidate=parse_packet(notice_raw,b"V15_TERMINAL_CANDIDATE_DURABLE",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"chain_head_sha256",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"candidate_deadline_ns"),receiver_binding(b"WAIT_TERMINAL_CANDIDATE",b"NONE",b"NONE",notice_deadline))
  candidate_sha=h64(candidate[b"subject_sha256"])
  need(candidate[b"state"]==b"TERMINAL_CANDIDATE_DURABLE" and candidate[b"expected_state"]==b"WAIT_TERMINAL_CANDIDATE" and candidate[b"kind"]==b"SUCCESS_CANDIDATE" and candidate[b"ordinal"]==candidate[b"probe"]==b"NONE")
  need(udec(candidate[b"terminal_origin_ns"])==terminal_origin and udec(candidate[b"terminal_deadline_ns"])==terminal_deadline and candidate[b"terminal_schedule_hex"]==schedule_hex(schedule,TERMINAL_PHASE_SPEC))
  seen_deadline=schedule[b"TERMINAL_SEEN_RECORD"];peer_pre_state=b"WAIT_TERMINAL_SEEN";peer_deadline=seen_deadline
  seen=packet(b"V15_TERMINAL_SEEN",((b"state",b"TERMINAL_SEEN"),(b"expected_state",b"WAIT_TERMINAL_SEEN"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",b"SUCCESS_CANDIDATE"),(b"subject_sha256",candidate_sha),(b"notice_packet_sha256",sha(notice_raw)),(b"terminal_origin_ns",str(terminal_origin).encode()),(b"terminal_deadline_ns",str(terminal_deadline).encode()),(b"terminal_schedule_hex",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"seen_deadline_ns",str(seen_deadline).encode())))
  pass_may_be_committed=True;state=b"TERMINAL_SEEN_SEND_EFFECT_UNKNOWN";b_send(control,seen,seen_deadline);state=b"TERMINAL_SEEN_SENT"
  ack_deadline=schedule[b"ACK"];ack_raw=recv_control(control,ack_deadline)
  terminal=parse_packet(ack_raw,b"V15_TERMINAL_ACK",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"terminal_seen_sha256",b"report_sha256",b"pass_sha256",b"reconciliation_token",b"ack_state",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"ack_deadline_ns"),receiver_binding(b"WAIT_TERMINAL_ACK",b"NONE",b"NONE",ack_deadline))
  need(terminal[b"state"]==b"TERMINAL_ACK" and terminal[b"expected_state"]==b"WAIT_TERMINAL_ACK" and terminal[b"ordinal"]==terminal[b"probe"]==b"NONE" and terminal[b"kind"]==b"SUCCESS_CANDIDATE")
  need(terminal[b"subject_sha256"]==candidate_sha and terminal[b"ack_state"]==b"PASS_COMMITTED_NO_DOWNGRADE")
  need(udec(terminal[b"terminal_origin_ns"])==terminal_origin and udec(terminal[b"terminal_deadline_ns"])==terminal_deadline and terminal[b"terminal_schedule_hex"]==schedule_hex(schedule,TERMINAL_PHASE_SPEC))
  terminal_seen_sha=h64(terminal[b"terminal_seen_sha256"]);report_sha=h64(terminal[b"report_sha256"]);pass_sha=h64(terminal[b"pass_sha256"]);reconciliation_token=h64(terminal[b"reconciliation_token"])
  pass_authoritative=True;receipt_deadline=schedule[b"A_RECEIPT"];receipt_ns=time.monotonic_ns();peer_pre_state=b"WAIT_ACK_RECEIPT";peer_deadline=receipt_deadline
  receipt=packet(b"V15_TERMINAL_ACK_RECEIPT",((b"state",b"ACK_RECEIVED_NO_REPLAY"),(b"expected_state",b"WAIT_ACK_RECEIPT"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",b"SUCCESS_CANDIDATE"),(b"subject_sha256",candidate_sha),(b"ack_packet_sha256",sha(ack_raw)),(b"report_sha256",report_sha),(b"pass_sha256",pass_sha),(b"reconciliation_token",reconciliation_token),(b"actor_receipt_ns",str(receipt_ns).encode()),(b"terminal_origin_ns",str(terminal_origin).encode()),(b"terminal_deadline_ns",str(terminal_deadline).encode()),(b"terminal_schedule_hex",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"receipt_deadline_ns",str(receipt_deadline).encode())))
  receipt_effect_unknown=True;state=b"ACK_RECEIPT_SEND_EFFECT_UNKNOWN";b_send(control,receipt,receipt_deadline);receipt_effect_unknown=False;state=b"ACK_RECEIPT_SENT"
  closure_deadline=schedule[b"CLOSURE_PACKET"];closed=parse_packet(recv_control(control,closure_deadline),b"V15_TERMINAL_CLOSED",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"report_sha256",b"pass_sha256",b"ack_receipt_sha256",b"reconciliation_sha256",b"closure_sha256",b"owner",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"closure_deadline_ns"),receiver_binding(b"WAIT_OWNER_CLOSED",b"NONE",b"NONE",closure_deadline))
  need(closed[b"state"]==b"OWNER_CLOSED" and closed[b"expected_state"]==b"WAIT_OWNER_CLOSED" and closed[b"ordinal"]==closed[b"probe"]==b"NONE" and closed[b"kind"]==b"SUCCESS_CANDIDATE")
  need(closed[b"subject_sha256"]==candidate_sha and closed[b"report_sha256"]==report_sha and closed[b"pass_sha256"]==pass_sha and closed[b"owner"]==b"B")
  for key in (b"ack_receipt_sha256",b"reconciliation_sha256",b"closure_sha256"):need(h64(closed[key])!=b"0"*64)
  need(udec(closed[b"terminal_origin_ns"])==terminal_origin and udec(closed[b"terminal_deadline_ns"])==terminal_deadline and closed[b"terminal_schedule_hex"]==schedule_hex(schedule,TERMINAL_PHASE_SPEC))
  actor_close_number(control.fileno());control=None
  braw=wait_status(bpid,0,schedule[b"B_EXIT"],b"PIDFD_ACTOR_LOST");bpid=-1;B_CHILD_PID=-1;B_CONTROL=None
  need(os.WIFEXITED(braw) and os.WEXITSTATUS(braw)==0,ConsumedIndeterminate)
  result=(b"P27E001_RUNNER_V15|AUTH_ID="+AUTH_ID+b"|entered=15|committed=15|candidate_sha256="+candidate_sha+b"|terminal_seen_sha256="+terminal_seen_sha+b"|report_sha256="+report_sha+b"|pass_sha256="+pass_sha+b"|ack_receipt_sha256="+closed[b"ack_receipt_sha256"]+b"|reconciliation_sha256="+closed[b"reconciliation_sha256"]+b"|owner_closure_sha256="+closed[b"closure_sha256"]+b"|owner_closed=1|retry_allowed=0\n")
  write_all(1,result)
 except BaseException as error:
  if control is None and B_CONTROL is not None:control=B_CONTROL;bpid=B_CHILD_PID
  phase=getattr(error,"p27_phase",state);faults=error_faults(error,phase);disposition=None;clean_refusal=False
  failure_stop_probe=locals().get("probe",b"NONE")
  if isinstance(error,RemoteAbort) and control is not None:
   remote=error.values;response_deadline=udec(remote[b"control_deadline_ns"],1);remote_terminal=udec(remote[b"terminal_deadline_ns"])
   response_ordinal=None if remote[b"ordinal"]==b"NONE" else udec(remote[b"ordinal"],0,14);failure_stop_probe=remote[b"probe"]
   try:
    send_abort(control,phase,b"WAIT_RELEASE_DISABLE_ACK",response_ordinal,failure_stop_probe,faults,response_deadline,remote_terminal)
    setattr(error,"p27_abort_sent",True)
   except BaseException as response_error:faults.update(error_faults(response_error,phase))
  if not begin_effect_possible:
   if control is None:clean_refusal=True
   else:
    try:
     deadline=locals().get("ready_deadline",entry_mono+PRECONSUME_NS)
     clean_refusal=request_refusal(control,b"BEGIN_NOT_ENTERED",b"ARM_NOT_OBSERVED",b"PREBEGIN_CLOSED",deadline)
    except BaseException:clean_refusal=False
  elif not commit_edge:
   try:
    refusal_acked=request_refusal(control,begin_state,arm_state,b"BEGIN_OR_ARM_CLOSED",consume_deadline);clean_refusal=refusal_acked
   except BaseException:clean_refusal=False
  elif pass_may_be_committed or pass_authoritative:
   disposition=None
  else:
   if control is not None:
    try:
     if not getattr(error,"p27_abort_sent",False):
      abort_ceiling=terminal_deadline if terminal_deadline and time.monotonic_ns()<=terminal_deadline else time.monotonic_ns()+ACK_NS
      abort_deadline=min(peer_deadline,abort_ceiling,time.monotonic_ns()+ACK_NS)
      send_abort(control,phase,peer_pre_state,None,b"NONE",faults,abort_deadline,terminal_deadline)
     outer_deadline=terminal_deadline if terminal_deadline else certificate_mono_expiry(CERT)
     disposition,failure_terminal_deadline=await_failure_terminal(control,outer_deadline,failure_stop_probe)
    except BaseException:disposition=None
  if control is not None:
   actor_close_number(control.fileno())
   control=None
  if bpid>=0 and (clean_refusal or disposition is not None):
   shutdown_deadline=failure_terminal_deadline if disposition is not None else locals().get("consume_deadline",locals().get("ready_deadline",entry_mono+PRECONSUME_NS))
   try:
    shutdown_raw=wait_status(bpid,0,shutdown_deadline,b"PIDFD_ACTOR_LOST");bpid=-1;B_CHILD_PID=-1;B_CONTROL=None
    if not (os.WIFEXITED(shutdown_raw) and os.WEXITSTATUS(shutdown_raw)==0):clean_refusal=False;disposition=None
   except BaseException:
    clean_refusal=False;disposition=None
  if clean_refusal and (refusal_acked or not begin_effect_possible):raise Refuse("exact-refusal-ack") from error
  if disposition==b"CONSUMED_FAIL":raise ConsumedFail("reported-fail") from error
 raise ConsumedIndeterminate("consumed-or-effect-unknown-no-replay") from error
 finally:
  close_numbers(tuple(number for number in (cgfd,safefd,runtime,attempt_base,stage_base,cgroup_base) if number>=0));actor_close_all()

# P27 RUNNER V19 ACTOR FINAL ENTRY BEGIN 19A0C701
RUNNER_INTERNAL_REVISION_V19=b"V19"
ACTOR_RECORD_COUNT_V19=211
ACTOR_RAW_CELL_COUNT_V19=216
V19_AT_FDCWD=-100
V19_F_DUPFD_CLOEXEC=1030
V19_SYS_PIDFD_OPEN=434
V19_MSG_CMSG_CLOEXEC=0x40000000
V19_PHYSICAL_LIVE_STATES=(b"ACQUIRING",b"OWNED",b"CLOSE_RETRY")

ACTOR_ENTRY_LIMIT_VECTOR_V19=(1048576,1048576)
ACTOR_CURRENT_LOW_LIMIT_VECTOR_V19=None
ACTOR_ENTRY_LIMIT_CERTIFIED_V19=False
ACTOR_BOOTSTRAP_INSTALLED_V19=False
ACTOR_SIMULTANEOUS_RECORD_ROLES_V19=tuple(role for role,kind in ACTOR_FD_ROLE_SPEC)
ACTOR_SIMULTANEOUS_INTAKE_ROLES_V19=tuple(b"ACTOR_CONTROL_VISIBLE_RIGHT_"+str(index).encode() for index in range(5))
ACTOR_SIMULTANEOUS_C_OUTPUT_ROLES_V19=(b"PIPE_OR_SOCKET_C_LEFT",b"PIPE_OR_SOCKET_C_RIGHT",b"CLONE3_PIDFD_C_OUT")
ACTOR_SIMULTANEOUS_LIVE_ROLE_SET_V19=ACTOR_SIMULTANEOUS_RECORD_ROLES_V19+ACTOR_SIMULTANEOUS_INTAKE_ROLES_V19+ACTOR_SIMULTANEOUS_C_OUTPUT_ROLES_V19
ACTOR_LIVE_HIGH_WATER_V19=len(ACTOR_SIMULTANEOUS_LIVE_ROLE_SET_V19)
ACTOR_CLONE3_CPYTHON_SUBCONDITIONS_V19=(
 b"FROZEN_ENTRY_RLIMIT_NOFILE_1048576_1048576",
 b"CURRENT_RLIMIT_NOFILE_256_SAME_HARD",
 b"ACTOR_SIMULTANEOUS_LIVE_ROLE_SET_219_LT_256",
 b"FD_TARGET_AND_RESULT_RANGE_0_THROUGH_255",
 b"FROZEN_CPYTHON_CACHED_SMALL_INT_0_THROUGH_255",
 b"CTYPES_C_INT_RESULT_STORE_STATICALLY_NONFAILING",
)
ACTOR_INHERITED_FIXED_SPEC_V19=(
 (b"stdin_fd",b"STDIN_FD",0),(b"stdout_fd",b"STDOUT_FD",1),(b"stderr_fd",b"STDERR_FD",2),
 (b"actor_source_carrier_fd",b"ACTOR_SOURCE_CARRIER_FD",100),(b"snapshot_carrier_fd",b"SNAPSHOT_CARRIER_FD",101),
 (b"v15_carrier_fd",b"V15_CARRIER_FD",102),(b"plan_carrier_fd",b"PLAN_CARRIER_FD",103),
 (b"certificate_carrier_fd",b"CERTIFICATE_CARRIER_FD",104),(b"envelope_carrier_fd",b"ENVELOPE_CARRIER_FD",105),
 (b"watchdog_source_carrier_fd",b"WATCHDOG_SOURCE_CARRIER_FD",106),(b"reservation_carrier_fd",b"RESERVATION_CARRIER_FD",107),
 (b"external_owner_control_carrier_fd",b"EXTERNAL_OWNER_CONTROL_FD",108),(b"external_owner_pidfd_carrier_fd",b"EXTERNAL_OWNER_PIDFD",109),
 (b"external_manifest_carrier_fd",b"EXTERNAL_MANIFEST_CARRIER_FD",110),
)

class PhysicalRecordV19:
 __slots__=(
  "record_id","home_role","state","semantic_role","raw_fd","identity","physical_identity","leaf_identity","verified_kill_leaf_identity",
  "access","provenance","endpoint_state","wrapper_ref","detached_raw_fd",
  "wrapper_phase","wrapper_local_fallback","wrapper_probe_done","wrapper_detach_attempted","raw_cell","epoch",
 )
 def __init__(self,record_id,home_role,raw_cell):
  self.record_id=record_id;self.home_role=home_role;self.state=b"CLOSED";self.semantic_role=None
  self.raw_fd=-1;self.identity=None;self.physical_identity=None;self.leaf_identity=None;self.verified_kill_leaf_identity=None;self.access=b"UNKNOWN"
  self.provenance=None;self.endpoint_state=b"NO_WRAPPER";self.wrapper_ref=None
  self.detached_raw_fd=-1;self.wrapper_phase=b"NO_CONSTRUCTOR";self.wrapper_local_fallback=-1
  self.wrapper_probe_done=False;self.wrapper_detach_attempted=False;self.raw_cell=raw_cell;self.epoch=0

class RawCellV19:
 __slots__=("cell_id","state","c_value","record_id","epoch")
 def __init__(self,cell_id):
  self.cell_id=cell_id;self.state=b"EMPTY";self.c_value=ctypes.c_int(-1)
  self.record_id=-1;self.epoch=0

class PollerCellV19:
 __slots__=("cell_id","state","poller","record_id","raw_fd","mask","epoch")
 def __init__(self,cell_id):
  self.cell_id=cell_id;self.state=b"FREE";self.poller=None;self.record_id=-1
  self.raw_fd=-1;self.mask=0;self.epoch=0

class PairResultV19:
 __slots__=("left","right")
 def __init__(self):
  self.left=None;self.right=None
 def __iter__(self):
  yield self.left
  yield self.right

class IovecV19(ctypes.Structure):
 _fields_=(("iov_base",ctypes.c_void_p),("iov_len",ctypes.c_size_t))

class MsghdrV19(ctypes.Structure):
 _fields_=(
  ("msg_name",ctypes.c_void_p),("msg_namelen",ctypes.c_uint),
  ("msg_iov",ctypes.POINTER(IovecV19)),("msg_iovlen",ctypes.c_size_t),
  ("msg_control",ctypes.c_void_p),("msg_controllen",ctypes.c_size_t),
  ("msg_flags",ctypes.c_int),
 )

class CmsghdrV19(ctypes.Structure):
 _fields_=(("cmsg_len",ctypes.c_size_t),("cmsg_level",ctypes.c_int),("cmsg_type",ctypes.c_int))

def cmsg_align_v19(value):
 alignment=ctypes.sizeof(ctypes.c_size_t)
 return (value+alignment-1)&~(alignment-1)

class ReceiveFrameV19:
 __slots__=(
  "site","semantic_capacity","installed_capacity","ancillary_bytes","kernel_control_bytes",
  "payload","control","iov","hdr","header_views","int_views","raw_cells",
  "quarantine_records","provenances","installed_count","payload_count","msg_flags",
  "capture_complete","validation_complete","capture_fault","cleanup_cursor","cleanup_pending","original_fault","epoch",
 )
 def __init__(self,site,semantic_capacity,installed_capacity,records,raw_cells):
  self.site=site;self.semantic_capacity=semantic_capacity
  self.installed_capacity=installed_capacity
  self.ancillary_bytes=installed_capacity*socket.CMSG_SPACE(ctypes.sizeof(ctypes.c_int))
  self.kernel_control_bytes=installed_capacity*socket.CMSG_SPACE(ctypes.sizeof(ctypes.c_int))
  self.payload=(ctypes.c_ubyte*65536)()
  self.control=(ctypes.c_ubyte*self.ancillary_bytes)()
  self.iov=IovecV19(ctypes.addressof(self.payload),65536)
  self.hdr=MsghdrV19()
  self.hdr.msg_name=None;self.hdr.msg_namelen=0
  self.hdr.msg_iov=ctypes.pointer(self.iov);self.hdr.msg_iovlen=1
  self.hdr.msg_control=ctypes.addressof(self.control)
  self.hdr.msg_controllen=self.kernel_control_bytes;self.hdr.msg_flags=0
  step=ctypes.sizeof(ctypes.c_size_t)
  self.header_views=tuple(CmsghdrV19.from_buffer(self.control,offset) for offset in range(0,self.ancillary_bytes-ctypes.sizeof(CmsghdrV19)+1,step))
  self.int_views=tuple(ctypes.c_int.from_buffer(self.control,offset) for offset in range(0,self.ancillary_bytes-ctypes.sizeof(ctypes.c_int)+1))
  need(len(records)==installed_capacity and len(raw_cells)==installed_capacity)
  self.raw_cells=raw_cells;self.quarantine_records=records
  self.provenances=tuple((b"RECVMSG",site,index) for index in range(installed_capacity))
  self.installed_count=0;self.payload_count=0;self.msg_flags=0
  self.capture_complete=False;self.validation_complete=False
  self.capture_fault=b"NONE";self.cleanup_cursor=0;self.cleanup_pending=False
  self.original_fault=None;self.epoch=0

ACTOR_RAW_CELLS_V19=tuple(RawCellV19(b"actor_record_raw_"+str(index).encode()) for index in range(ACTOR_RECORD_COUNT_V19))
ACTOR_PHYSICAL_RECORDS_V19=tuple(
 PhysicalRecordV19(index,ACTOR_FD_ROLE_SPEC[index][0],ACTOR_RAW_CELLS_V19[index])
 for index in range(ACTOR_RECORD_COUNT_V19)
)
ACTOR_RECORD_BY_ROLE_V19={
 role:ACTOR_PHYSICAL_RECORDS_V19[index] for index,(role,kind) in enumerate(ACTOR_FD_ROLE_SPEC)
}
ACTOR_FD_REGISTRY=ACTOR_RECORD_BY_ROLE_V19
ACTOR_EXTRA_RECEIVE_RAW_CELLS_V19=tuple(RawCellV19(b"actor_receive_raw_"+str(index).encode()) for index in range(5))
ACTOR_RAW_CELLS_V19=ACTOR_RAW_CELLS_V19+ACTOR_EXTRA_RECEIVE_RAW_CELLS_V19
ACTOR_POLLER_CELLS_V19=tuple(PollerCellV19(index) for index in range(8))
ACTOR_PIPE2_OUT_V19=(ctypes.c_int*2)(-1,-1)
ACTOR_SOCKETPAIR_OUT_V19=(ctypes.c_int*2)(-1,-1)
ACTOR_CLONE3_PIDFD_OUT_V19=ctypes.c_int(-1)
ACTOR_CLONE3_ARGS_V19=CloneArgs()
ACTOR_PIPE_RETURN_V19=PairResultV19()
ACTOR_SOCKET_RETURN_V19=PairResultV19()
ACTOR_CLONE_RETURN_V19=PairResultV19()
ACTOR_PAIR_RECORD_RETURN_V19=PairResultV19()
ACTOR_CLONE_RECORD_RETURN_V19=PairResultV19()
ACTOR_ROLE_ORDER_V19=tuple(role for role,kind in ACTOR_FD_ROLE_SPEC)
ACTOR_CONTROL_QUARANTINE_V19=(
 ACTOR_RECORD_BY_ROLE_V19[b"actor_quarantine_0"],
 ACTOR_RECORD_BY_ROLE_V19[b"actor_quarantine_1"],
 ACTOR_RECORD_BY_ROLE_V19[b"actor_quarantine_2"],
 ACTOR_RECORD_BY_ROLE_V19[b"actor_quarantine_3"],
 ACTOR_RECORD_BY_ROLE_V19[b"actor_file_pool_63"],
)
ACTOR_CONTROL_FRAME_V19=ReceiveFrameV19(b"ACTOR_CONTROL",4,5,ACTOR_CONTROL_QUARANTINE_V19,ACTOR_EXTRA_RECEIVE_RAW_CELLS_V19)
ACTOR_RECEIVE_CLEANUP_WAIT_V19=select.poll()

class ActorRegistryViewV19:
 __slots__=("home",)
 def __init__(self,home):self.home=home
 def __iter__(self):return iter(ACTOR_ROLE_ORDER_V19)
 def __contains__(self,role):return role in self.home
 def __getitem__(self,role):
  need(role in self.home)
  for record in ACTOR_PHYSICAL_RECORDS_V19:
   if record.state in V19_PHYSICAL_LIVE_STATES and record.semantic_role==role:return record
  home=self.home[role]
  if home.state==b"CLOSED":return home
  for record in ACTOR_PHYSICAL_RECORDS_V19:
   if record.state==b"CLOSED" and record.semantic_role is None:return record
  need(False)
 def get(self,role,default=None):return self[role] if role in self.home else default
 def items(self):
  for role in ACTOR_ROLE_ORDER_V19:yield role,self[role]
 def __setitem__(self,role,record):raise ConsumedIndeterminate("actor-derived-registry-is-not-mutable")

ACTOR_FD_REGISTRY=ActorRegistryViewV19(ACTOR_RECORD_BY_ROLE_V19)

def actor_record_live_v19(record):
 return record.state in V19_PHYSICAL_LIVE_STATES and record.raw_fd>=0

def actor_record_reset_closed_v19(record):
 cell=record.raw_cell;cell.state=b"EMPTY";cell.c_value.value=-1
 cell.record_id=record.record_id;cell.epoch=record.epoch
 record.state=b"CLOSED";record.semantic_role=None;record.raw_fd=-1;record.identity=None
 record.physical_identity=None;record.leaf_identity=None;record.verified_kill_leaf_identity=None
 record.access=b"UNKNOWN";record.provenance=None
 record.endpoint_state=b"NO_WRAPPER";record.wrapper_ref=None
 record.detached_raw_fd=-1;record.wrapper_phase=b"NO_CONSTRUCTOR"
 record.wrapper_local_fallback=-1;record.wrapper_probe_done=False;record.wrapper_detach_attempted=False

def actor_raw_prearm_v19(cell,record):
 need(record.state==b"ACQUIRING" and record.raw_fd==-1)
 need(cell.state in (b"EMPTY",b"DISARMED") and cell.c_value.value<0)
 cell.state=b"EMPTY";cell.c_value.value=-1;cell.record_id=record.record_id
 cell.epoch=record.epoch

def actor_begin_acquisition(role,kind):
 need(role in ACTOR_FD_ROLE_MAP and ACTOR_FD_ROLE_MAP[role]==kind)
 record=ACTOR_FD_REGISTRY[role];need(record.state==b"CLOSED" and record.raw_fd==-1)
 actor_record_reset_closed_v19(record)
 try:
  record.epoch+=1;record.semantic_role=role;record.state=b"ACQUIRING"
  record.identity=None;record.physical_identity=None;record.leaf_identity=None
  record.verified_kill_leaf_identity=None;record.access=b"UNKNOWN"
  record.provenance=(b"ACTOR_PRODUCER",role,record.epoch)
  record.endpoint_state=b"NO_WRAPPER";record.wrapper_ref=None
  record.detached_raw_fd=-1;actor_raw_prearm_v19(record.raw_cell,record)
  return record
 except BaseException:
  if record.raw_fd>=0:record.state=b"CLOSE_RETRY"
  else:actor_record_reset_closed_v19(record)
  raise

def actor_capture_cell_v19(cell,record):
 number=cell.c_value.value
 if number>=0:
  if record.raw_fd<0:record.raw_fd=number;record.state=b"ACQUIRING"
  else:need(record.raw_fd==number)
  cell.record_id=record.record_id;cell.epoch=record.epoch;cell.state=b"SHADOW_OF_RECORD"
  if number>255:
   record.state=b"CLOSE_RETRY";raise ConsumedIndeterminate("actor-fd-above-cached-bound")
 elif record.state==b"ACQUIRING" and record.raw_fd<0:
  actor_record_reset_closed_v19(record);cell.state=b"DISARMED"
 return number

def actor_identity_revalidate_v19(record):
 need(actor_record_live_v19(record))
 held=os.fstat(record.raw_fd);access=fcntl.fcntl(record.raw_fd,fcntl.F_GETFL)&os.O_ACCMODE
 observed=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,access)
 if record.physical_identity is not None:need(observed==record.physical_identity)
 record.physical_identity=observed;record.identity=observed
 if record.leaf_identity is None:record.leaf_identity=(b"PHYSICAL",held.st_dev,held.st_ino)
 record.access=access;return observed

def actor_finish_adoption(role):
 record=ACTOR_FD_REGISTRY[role];need(actor_record_live_v19(record))
 need(record.semantic_role==role and actor_live_owner(record.raw_fd,role) is None)
 try:
  actor_identity_revalidate_v19(record)
  need(record.physical_identity is not None and len(record.physical_identity)==7 and record.access!=b"UNKNOWN")
  record.state=b"OWNED"
 except BaseException:
  record.state=b"CLOSE_RETRY"
  try:actor_close_record(role)
  except BaseException:pass
  raise
 return record.raw_fd

def actor_scalar_boundary_v19(role,kind,operation,arg0=None,arg1=None,arg2=None,arg3=None):
 record=None;cell=None;result=-1;saved=0
 try:
  record=actor_begin_acquisition(role,kind);cell=record.raw_cell
  if operation==b"OPENAT":
   directory=V19_AT_FDCWD if arg3 is None else arg3
   result=LIBC.openat(directory,arg0,arg1,arg2)
  elif operation==b"DUP":
   result=LIBC.dup(arg0)
  elif operation==b"F_DUPFD_CLOEXEC":
   result=LIBC.fcntl(arg0,V19_F_DUPFD_CLOEXEC,arg1)
  elif operation==b"DUP2":
   result=LIBC.dup2(arg0,arg1)
  elif operation==b"MEMFD":
   result=LIBC.memfd_create(arg0,arg1)
  elif operation==b"PIDFD_OPEN":
   result=LIBC.syscall(V19_SYS_PIDFD_OPEN,arg0,0)
  else:need(False)
  cell.c_value.value=result
  saved=ctypes.get_errno()
 finally:
  if record is not None:
   actor_capture_cell_v19(record.raw_cell,record)
 if result<0:
  need(record.state==b"CLOSED")
  raise OSError(saved,os.strerror(saved))
 return actor_finish_adoption(role)

def actor_capture_authoritative_c_v19(record,c_cell):
 number=c_cell.value
 if record is None:
  need(number<0);return number
 if number>=0:
  if record.raw_fd<0:record.raw_fd=number;record.state=b"ACQUIRING"
  else:need(record.raw_fd==number)
  shadow=record.raw_cell;shadow.c_value.value=number;shadow.record_id=record.record_id
  shadow.epoch=record.epoch;shadow.state=b"SHADOW_OF_RECORD"
  if number>255:
   record.state=b"CLOSE_RETRY";raise ConsumedIndeterminate("actor-c-output-above-cached-bound")
 elif record.state==b"ACQUIRING" and record.raw_fd<0:
  actor_record_reset_closed_v19(record);record.raw_cell.state=b"DISARMED"
 return number

def actor_reconcile_pair_outputs_v19(left,right,cells):
 first=None
 try:actor_capture_authoritative_c_v19(left,cells[0])
 except BaseException as error:first=error
 try:actor_capture_authoritative_c_v19(right,cells[1])
 except BaseException as error:
  if first is None:first=error
 if first is not None:raise first

def actor_pair_boundary_v19(left_role,right_role,operation,flags=0):
 left=right=None
 cells=ACTOR_PIPE2_OUT_V19 if operation==b"PIPE2" else ACTOR_SOCKETPAIR_OUT_V19
 cells[0]=-1;cells[1]=-1;result=-1;saved=0
 try:
  left=actor_begin_acquisition(left_role,ACTOR_FD_ROLE_MAP[left_role])
  right=actor_begin_acquisition(right_role,ACTOR_FD_ROLE_MAP[right_role])
  if operation==b"PIPE2":result=LIBC.pipe2(cells,flags)
  else:result=LIBC.socketpair(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC|socket.SOCK_NONBLOCK,0,cells)
  saved=ctypes.get_errno()
 finally:actor_reconcile_pair_outputs_v19(left,right,cells)
 if result<0:
  for role in (left_role,right_role):
   if actor_record_live_v19(ACTOR_FD_REGISTRY[role]):
    try:actor_close_record(role)
    except BaseException:pass
  raise OSError(saved,os.strerror(saved))
 first=None
 try:actor_finish_adoption(left_role)
 except BaseException as error:first=error
 try:actor_finish_adoption(right_role)
 except BaseException as error:
  if first is None:first=error
 if first is not None:
  for role in (left_role,right_role):
   if actor_record_live_v19(ACTOR_FD_REGISTRY[role]):
    try:actor_close_record(role)
    except BaseException:pass
  raise first
 ACTOR_PAIR_RECORD_RETURN_V19.left=left;ACTOR_PAIR_RECORD_RETURN_V19.right=right
 return ACTOR_PAIR_RECORD_RETURN_V19

def actor_wrapper_adopt_v19(record):
 need(record.state==b"OWNED" and record.raw_fd>=0 and record.wrapper_ref is None)
 record.endpoint_state=b"NO_WRAPPER";record.wrapper_phase=b"CONSTRUCTOR_ARMED"
 record.wrapper_local_fallback=record.raw_fd;record.wrapper_probe_done=False;record.wrapper_detach_attempted=False
 wrapper=socket.socket.__new__(socket.socket)
 record.wrapper_ref=wrapper;record.wrapper_phase=b"LOCAL_STRONG_REFERENCE"
 try:
  socket.socket.__init__(wrapper,fileno=record.raw_fd)
  record.wrapper_phase=b"ATTACH_CONFIRMED";record.endpoint_state=b"ATTACHED"
  need(wrapper.fileno()==record.raw_fd);return wrapper
 except BaseException:
  record.state=b"CLOSE_RETRY"
  try:actor_reconcile_wrapper_v19(record)
  except BaseException:pass
  if record.endpoint_state==b"DETACHED":
   try:actor_close_record(actor_role_for_record_v19(record))
   except BaseException:pass
  raise

def actor_role_for_record_v19(record):
 need(record.semantic_role in ACTOR_FD_ROLE_MAP);return record.semantic_role

def actor_live_owner(number,exclude=None):
 owner=None
 for role,record in ACTOR_FD_REGISTRY.items():
  if role!=exclude and actor_record_live_v19(record) and record.raw_fd==number:
   need(owner is None);owner=role
 return owner

def actor_audit(role,record=None):
 if record is None:record=ACTOR_FD_REGISTRY[role]
 derived_kind=ACTOR_FD_ROLE_MAP[role]
 try:ACTOR_FD_JOURNAL.append((role,record.record_id,record.state,derived_kind,record.raw_fd,record.identity,record.access))
 except BaseException:pass

def actor_adopt_raw(role,kind,number,endpoint=None):
 record=None
 try:
  record=actor_begin_acquisition(role,kind)
  record.raw_cell.c_value.value=number
 finally:
  if record is not None:actor_capture_cell_v19(record.raw_cell,record)
 result=actor_finish_adoption(role)
 if endpoint is not None:
  record.wrapper_ref=endpoint;record.endpoint_state=b"ATTACHED"
  try:need(endpoint.fileno()==result)
  except BaseException:
   record.state=b"CLOSE_RETRY";actor_close_record(role);raise
 return result

def register_runtime_fd(slot,kind,number):
 return actor_adopt_raw(slot,kind,number)

def actor_acquire_open(role,kind,path,flags,mode=0o777,dir_fd=None):
 return actor_scalar_boundary_v19(role,kind,b"OPENAT",path,flags,mode,dir_fd)

def actor_acquire_open_pool(directory,path,flags,mode=0o777,dir_fd=None):
 prefix=b"actor_dir_pool_" if directory else b"actor_file_pool_"
 kind=b"DYNAMIC_DIR_FD" if directory else b"DYNAMIC_FILE_FD";role=None
 for candidate in ACTOR_FD_REGISTRY:
  record=ACTOR_FD_REGISTRY[candidate]
  if candidate.startswith(prefix) and candidate!=b"actor_file_pool_63" and record.state==b"CLOSED":role=candidate;break
 need(role is not None);return actor_acquire_open(role,kind,path,flags,mode,dir_fd)

def actor_acquire_dup(role,kind,source):
 return actor_scalar_boundary_v19(role,kind,b"DUP",source)

def actor_acquire_dup_pool(directory,source):
 prefix=b"actor_dir_pool_" if directory else b"actor_file_pool_"
 kind=b"DYNAMIC_DIR_FD" if directory else b"DYNAMIC_FILE_FD";role=None
 for candidate in ACTOR_FD_REGISTRY:
  if candidate.startswith(prefix) and candidate!=b"actor_file_pool_63" and ACTOR_FD_REGISTRY[candidate].state==b"CLOSED":role=candidate;break
 need(role is not None);return actor_acquire_dup(role,kind,source)

def actor_acquire_mapping_park(index,source):
 return actor_scalar_boundary_v19(b"actor_mapping_park_"+str(index).encode(),b"MAPPING_PARK_FD",b"F_DUPFD_CLOEXEC",source,200)

def actor_dup2_mapping_target(index,source,target):
 role=b"actor_mapping_target_"+str(index).encode();owner=actor_live_owner(target)
 if owner is not None:actor_close_record(owner)
 return actor_scalar_boundary_v19(role,b"MAPPING_TARGET_FD",b"DUP2",source,target)

def actor_acquire_memfd(role,kind,label):
 return actor_scalar_boundary_v19(role,kind,b"MEMFD",label,os.MFD_CLOEXEC|os.MFD_ALLOW_SEALING)

def actor_acquire_pipe2(read_role,write_role,flags):
 left,right=actor_pair_boundary_v19(read_role,write_role,b"PIPE2",flags)
 ACTOR_PIPE_RETURN_V19.left=left.raw_fd;ACTOR_PIPE_RETURN_V19.right=right.raw_fd
 return ACTOR_PIPE_RETURN_V19

def actor_acquire_socketpair(left_role,right_role):
 left,right=actor_pair_boundary_v19(left_role,right_role,b"SOCKETPAIR")
 ACTOR_SOCKET_RETURN_V19.left=actor_wrapper_adopt_v19(left)
 ACTOR_SOCKET_RETURN_V19.right=actor_wrapper_adopt_v19(right)
 return ACTOR_SOCKET_RETURN_V19

def actor_acquire_pidfd(role,pid):
 return actor_scalar_boundary_v19(role,ACTOR_FD_ROLE_MAP[role],b"PIDFD_OPEN",pid)

def actor_promote_record(old_role,new_role):
 source=ACTOR_FD_REGISTRY[old_role];need(actor_record_live_v19(source))
 need(not any(actor_record_live_v19(record) and record.semantic_role==new_role for record in ACTOR_PHYSICAL_RECORDS_V19))
 prepared_provenance=(b"ACTOR_PROMOTION",old_role,new_role,source.provenance,source.epoch)
 actor_identity_revalidate_v19(source);need(actor_live_owner(source.raw_fd,old_role) is None)
 for record in ACTOR_PHYSICAL_RECORDS_V19:
  if record is not source and actor_record_live_v19(record):need(record.raw_fd!=source.raw_fd)
 source.provenance=prepared_provenance
 source.semantic_role=new_role
 source.state=b"OWNED";return source.raw_fd

def actor_reconcile_pollers_v19(record):
 pending=False
 for cell in ACTOR_POLLER_CELLS_V19:
  if cell.record_id==record.record_id and cell.state in (b"REGISTERING",b"ACTIVE",b"UNREGISTER_RETRY"):
   cell.state=b"UNREGISTER_RETRY"
   try:cell.poller.unregister(record.raw_fd)
   except KeyError:pass
   except BaseException:pending=True;continue
   cell.state=b"INACTIVE";cell.poller=None;cell.raw_fd=-1;cell.mask=0
 if pending:raise ConsumedIndeterminate("actor-poller-unregister-retry")

def actor_reconcile_wrapper_v19(record):
 wrapper=record.wrapper_ref
 if wrapper is None:
  if record.endpoint_state not in (b"NO_WRAPPER",b"DETACHED",b"PROVED_CLOSED"):record.endpoint_state=b"NO_WRAPPER"
  return
 record.endpoint_state=b"DETACH_REQUESTED"
 if not record.wrapper_probe_done:
  observed=wrapper.fileno();record.wrapper_probe_done=True
  if observed==-1:
   record.detached_raw_fd=record.raw_fd;record.endpoint_state=b"DETACHED"
   record.wrapper_phase=b"DETACH_CONFIRMED";record.wrapper_ref=None;return
  need(observed==record.raw_fd)
 if record.wrapper_detach_attempted:raise ConsumedIndeterminate("actor-wrapper-detach-effect-unknown-no-repeat")
 record.wrapper_detach_attempted=True;record.wrapper_phase=b"DETACH_POSSIBLE"
 try:detached=wrapper.detach()
 except BaseException as error:raise ConsumedIndeterminate("actor-wrapper-detach-effect-unknown-no-repeat") from error
 need(detached==record.raw_fd)
 record.detached_raw_fd=detached;record.endpoint_state=b"DETACHED"
 record.wrapper_phase=b"DETACH_CONFIRMED";record.wrapper_ref=None

def actor_close_record(role):
 record=ACTOR_FD_REGISTRY[role]
 if record.state==b"CLOSED":return True
 need(record.raw_fd>=0);number=record.raw_fd;record.state=b"CLOSE_RETRY"
 actor_reconcile_pollers_v19(record);actor_reconcile_wrapper_v19(record)
 if record.identity is not None:
  try:actor_identity_revalidate_v19(record)
  except OSError as probe:
   if probe.errno==errno.EBADF:
    record.endpoint_state=b"PROVED_CLOSED";record.raw_cell.state=b"DISARMED"
    actor_record_reset_closed_v19(record);actor_audit(role,record);return True
   raise
 try:os.close(number)
 except OSError:
  try:actor_identity_revalidate_v19(record)
  except OSError as probe:
   if probe.errno==errno.EBADF:
    record.endpoint_state=b"PROVED_CLOSED";record.raw_cell.state=b"DISARMED"
    actor_record_reset_closed_v19(record);actor_audit(role,record);return True
   raise
  record.state=b"CLOSE_RETRY";raise
 record.endpoint_state=b"PROVED_CLOSED";record.raw_cell.state=b"DISARMED"
 actor_record_reset_closed_v19(record);actor_audit(role,record);return True

def actor_close_number(number):
 role=actor_live_owner(number)
 if role is not None:return actor_close_record(role)
 try:os.close(number)
 except OSError as error:
  if error.errno!=errno.EBADF:raise
 return True

def actor_close_registered_range(first,last):
 for role in ACTOR_ROLE_ORDER_V19:
  record=ACTOR_FD_REGISTRY[role]
  if actor_record_live_v19(record) and first<=record.raw_fd<=last:actor_close_record(role)
 return True

def actor_bootstrap_registry():
 global ACTOR_BOOTSTRAP_INSTALLED_V19
 if ACTOR_BOOTSTRAP_INSTALLED_V19:return True
 for role,kind,number in ACTOR_INHERITED_FIXED_SPEC_V19:
  record=actor_begin_acquisition(role,kind);record.raw_cell.c_value.value=number
  actor_capture_cell_v19(record.raw_cell,record);actor_finish_adoption(role)
  need(record.state==b"OWNED" and record.raw_fd==number and record.physical_identity is not None and record.access!=b"UNKNOWN")
 ACTOR_BOOTSTRAP_INSTALLED_V19=True;return True

def actor_close_all():
 first=None
 for role in ACTOR_ROLE_ORDER_V19:
  if actor_record_live_v19(ACTOR_FD_REGISTRY[role]):
   try:actor_close_record(role)
   except BaseException as error:
    if first is None:first=error
 if first is not None:raise first
 return True

def actor_receive_prearm_v19(frame):
 need(frame.cleanup_cursor==0 and not frame.cleanup_pending)
 frame.epoch+=1;frame.installed_count=0;frame.payload_count=0
 frame.msg_flags=0;frame.capture_complete=False;frame.validation_complete=False
 frame.capture_fault=b"NONE";frame.original_fault=None
 frame.hdr.msg_controllen=frame.kernel_control_bytes;frame.hdr.msg_flags=0
 ctypes.memset(ctypes.addressof(frame.control),0,frame.ancillary_bytes)
 for index in range(frame.installed_capacity):
  record=frame.quarantine_records[index];need(record.state==b"CLOSED")
  actor_record_reset_closed_v19(record);record.epoch+=1
  record.semantic_role=record.home_role;record.state=b"ACQUIRING"
  record.raw_fd=-1;record.identity=None;record.physical_identity=None
  record.leaf_identity=None;record.verified_kill_leaf_identity=None
  record.access=b"UNKNOWN";record.provenance=frame.provenances[index]
  record.endpoint_state=b"NO_WRAPPER";record.wrapper_ref=None
  cell=frame.raw_cells[index];cell.state=b"EMPTY";cell.c_value.value=-1
  cell.record_id=record.record_id;cell.epoch=record.epoch

def actor_receive_capture_one_v19(frame,index,number):
 if index>=frame.installed_capacity:
  frame.capture_fault=b"RIGHTS_OVERFLOW";return
 cell=frame.raw_cells[index];record=frame.quarantine_records[index];cell.c_value.value=number
 if number<0:
  frame.capture_fault=b"NEGATIVE_INSTALLED_RIGHT";return
 if record.raw_fd<0:record.raw_fd=number;record.state=b"ACQUIRING";cell.state=b"SHADOW_OF_RECORD"
 elif record.raw_fd!=number:frame.capture_fault=b"CAPTURE_IDENTITY_CONFLICT"
 if number>255:record.state=b"CLOSE_RETRY";frame.capture_fault=b"FD_ABOVE_CACHED_BOUND"
 if index+1>frame.installed_count:frame.installed_count=index+1

def actor_receive_scan_v19(frame,count):
 frame.payload_count=count;frame.msg_flags=frame.hdr.msg_flags
 offset=0;visible=0;limit=min(frame.hdr.msg_controllen,frame.ancillary_bytes)
 while offset+ctypes.sizeof(CmsghdrV19)<=limit:
  header=frame.header_views[offset//ctypes.sizeof(ctypes.c_size_t)]
  length=header.cmsg_len
  if length<ctypes.sizeof(CmsghdrV19) or offset+length>limit:
   frame.capture_fault=b"MALFORMED_CMSG";offset+=ctypes.sizeof(ctypes.c_size_t);continue
  data_offset=offset+cmsg_align_v19(ctypes.sizeof(CmsghdrV19))
  if header.cmsg_level==socket.SOL_SOCKET and header.cmsg_type==socket.SCM_RIGHTS:
   data_bytes=length-cmsg_align_v19(ctypes.sizeof(CmsghdrV19))
   if data_bytes%ctypes.sizeof(ctypes.c_int):frame.capture_fault=b"MALFORMED_RIGHTS"
   rights=data_bytes//ctypes.sizeof(ctypes.c_int)
   for item in range(rights):
    position=data_offset+item*ctypes.sizeof(ctypes.c_int)
    if visible<frame.installed_capacity:
     actor_receive_capture_one_v19(frame,visible,frame.int_views[position].value)
    else:frame.capture_fault=b"RIGHTS_OVERFLOW"
    visible+=1
  else:frame.capture_fault=b"UNEXPECTED_CMSG"
  offset+=max(ctypes.sizeof(ctypes.c_size_t),cmsg_align_v19(length))
 for index in range(frame.installed_capacity):
  record=frame.quarantine_records[index]
  if record.state==b"ACQUIRING" and record.raw_fd<0:
   actor_record_reset_closed_v19(record);frame.raw_cells[index].state=b"DISARMED"
 frame.capture_complete=True

def actor_receive_rescan_v19(frame):
 actor_receive_scan_v19(frame,frame.payload_count)
 for index in range(frame.installed_capacity):
  cell=frame.raw_cells[index];record=frame.quarantine_records[index]
  if record.state==b"ACQUIRING":actor_capture_cell_v19(cell,record)

def actor_receive_cleanup_v19(frame):
 while True:
  frame.cleanup_pending=False
  while frame.cleanup_cursor<frame.installed_capacity:
   index=frame.cleanup_cursor;record=frame.quarantine_records[index]
   if actor_record_live_v19(record):
    try:actor_close_record(actor_role_for_record_v19(record))
    except BaseException:
     record.state=b"CLOSE_RETRY";frame.cleanup_pending=True
   if record.state==b"CLOSED":frame.raw_cells[index].state=b"EMPTY";frame.raw_cells[index].c_value.value=-1
   frame.cleanup_cursor+=1
  if not frame.cleanup_pending:
   frame.cleanup_cursor=0;return True
  frame.cleanup_cursor=0
  try:ACTOR_RECEIVE_CLEANUP_WAIT_V19.poll(10)
  except BaseException:pass

def actor_recvmsg_primitive_v19(control,frame):
 result=-1;failure=None
 try:
  try:
   actor_receive_prearm_v19(frame)
   result=LIBC.recvmsg(control.fileno(),ctypes.byref(frame.hdr),V19_MSG_CMSG_CLOEXEC)
   actor_receive_scan_v19(frame,result)
  except BaseException as error:failure=error
 finally:
  try:actor_receive_rescan_v19(frame)
  except BaseException as error:
   if failure is None:failure=error
 if result<0 and failure is None:
  saved=ctypes.get_errno()
  failure=BlockingIOError(saved,os.strerror(saved)) if saved in (errno.EAGAIN,errno.EWOULDBLOCK) else OSError(saved,os.strerror(saved))
 if failure is not None:
  frame.original_fault=failure;actor_receive_cleanup_v19(frame)
  raise failure
 return frame

def actor_recvmsg_site_v19(control):
 return actor_recvmsg_primitive_v19(control,ACTOR_CONTROL_FRAME_V19)

def recv_control(control,deadline,cap=65536):
 need(cap<=65536);checkpoint(CERT,0,ConsumedIndeterminate,deadline)
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 while True:
  checkpoint(CERT,0,ConsumedIndeterminate,deadline);remaining=deadline-time.monotonic_ns()
  if remaining<=0:raise FaultSet({b"CONTROL_TIMEOUT"})
  try:events=poller.poll(max(1,min(50,(remaining+999999)//1000000)))
  except InterruptedError:continue
  mask=0
  for number,event in events:
   if number==control.fileno():mask|=event
  if mask&select.POLLNVAL:raise ControlLost("control-nval")
  if mask&select.POLLIN:
   frame=None
   try:
    frame=actor_recvmsg_site_v19(control)
    raw=bytes(frame.payload[:frame.payload_count])
    checkpoint(CERT,0,ConsumedIndeterminate,deadline)
    if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})
    if frame.msg_flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC):raise FaultSet({b"CONTROL_TRUNCATION"})
    if frame.capture_fault!=b"NONE" or frame.installed_count!=0:raise FaultSet({b"FD_TRANSFER"})
    if not raw:raise FaultSet({b"CONTROL_MALFORMED"})
    frame.validation_complete=True;return raw
   except BlockingIOError:
    if frame is not None:actor_receive_cleanup_v19(frame)
    continue
   finally:
    if frame is not None:actor_receive_cleanup_v19(frame)
  if mask&(select.POLLHUP|select.POLLERR):raise ControlLost("control-hup")

def actor_clone3_boundary_v19(cgfd):
 record=None;ACTOR_CLONE3_PIDFD_OUT_V19.value=-1
 args=ACTOR_CLONE3_ARGS_V19;args.flags=CLONE_PIDFD|CLONE_INTO_CGROUP
 args.pidfd=ctypes.addressof(ACTOR_CLONE3_PIDFD_OUT_V19)
 args.exit_signal=int(signal.SIGCHLD);args.cgroup=cgfd;pid=-1
 try:
  record=actor_begin_acquisition(b"probe_outer_pidfd",b"PROBE_OUTER_PIDFD")
  pid=LIBC.syscall(SYS_CLONE3,ctypes.byref(args),ctypes.sizeof(args))
 finally:actor_capture_authoritative_c_v19(record,ACTOR_CLONE3_PIDFD_OUT_V19)
 if pid<0:
  if record is not None and actor_record_live_v19(record):
   try:actor_close_record(b"probe_outer_pidfd")
   except BaseException:pass
  raise ConsumedIndeterminate("clone-return")
 if pid>0:actor_finish_adoption(b"probe_outer_pidfd")
 ACTOR_CLONE_RECORD_RETURN_V19.left=pid;ACTOR_CLONE_RECORD_RETURN_V19.right=record
 return ACTOR_CLONE_RECORD_RETURN_V19

def launch_outer(outer_fd,in_r,out_w,err_w,safe,argv,cgfd):
 pid,record=actor_clone3_boundary_v19(cgfd)
 if pid==0:
  try:
   os.kill(os.getpid(),signal.SIGSTOP)
   preserved_map(((in_r,0),(out_w,1),(err_w,2),(outer_fd,100)))
   actor_close_registered_range(3,99);close_range(3,99)
   actor_close_registered_range(101,UINT_MAX);close_range(101,UINT_MAX)
   child_context(AUTH_ID,safe.st_dev,safe.st_ino);scrub_exact({0,1,2,100})
   os.execve(PYTHON,tuple(argv),ENV)
  except BaseException:os._exit(98)
 need(pid>=2 and actor_record_live_v19(record) and record.raw_fd>=0)
 ACTOR_CLONE_RETURN_V19.left=pid;ACTOR_CLONE_RETURN_V19.right=record.raw_fd
 return ACTOR_CLONE_RETURN_V19

def verify_platform_v15_baseline_v19(cert):
 return V15_ACTOR_VERIFY_PLATFORM(cert)

V15_ACTOR_VERIFY_PLATFORM=verify_platform
def verify_platform(cert):
 result=V15_ACTOR_VERIFY_PLATFORM(cert)
 need(cert[b"CLONE3_CPYTHON_GATE_PASS"]==b"1" and cert[b"CLONE3_CPYTHON_GATE_ID"]!=b"0"*64,Refuse)
 soft,hard=resource.getrlimit(resource.RLIMIT_NOFILE)
 need(soft==256 and hard>=256 and ACTOR_LIVE_HIGH_WATER_V19==219,Refuse)
 for value in range(256):need(int(str(value)) is value,Refuse)
 return result

def verify_external_inputs(cert):
 pid=udec(cert[b"EXTERNAL_OWNER_PID"],2);start=udec(cert[b"EXTERNAL_OWNER_STARTTIME"],1)
 fd_access(108,os.O_RDWR);fd_access(109,os.O_RDWR);need(pidfd_pid(109)==pid,Refuse)
 watcher=select.poll();watcher.register(109,select.POLLIN|select.POLLHUP|select.POLLERR);need(watcher.poll(0)==[],Refuse)
 record=ACTOR_FD_REGISTRY[b"external_owner_control_carrier_fd"]
 need(record.state==b"OWNED" and record.raw_fd==108,Refuse)
 duplicate=actor_wrapper_adopt_v19(record)
 try:
  need(duplicate.getsockopt(socket.SOL_SOCKET,socket.SO_TYPE)==socket.SOCK_SEQPACKET,Refuse)
  need(fcntl.fcntl(108,fcntl.F_GETFL)&os.O_NONBLOCK,Refuse)
  peer=struct.unpack("3i",duplicate.getsockopt(socket.SOL_SOCKET,socket.SO_PEERCRED,12))
  need(peer==(pid,udec(cert[b"EXTERNAL_OWNER_UID"]),udec(cert[b"EXTERNAL_OWNER_GID"])),Refuse)
 finally:actor_reconcile_wrapper_v19(record)
 need(record.state==b"OWNED" and record.raw_fd==108 and record.endpoint_state==b"DETACHED",Refuse)
 need(proc_starttime(pid)==start and pidfd_pid(109)==pid and proc_starttime(pid)==start and watcher.poll(0)==[],Refuse)

V15_ACTOR_MAIN_V19=main
def actor_entry_limit_transition_v19():
 global ACTOR_ENTRY_LIMIT_CERTIFIED_V19,ACTOR_CURRENT_LOW_LIMIT_VECTOR_V19
 need(not ACTOR_ENTRY_LIMIT_CERTIFIED_V19,Refuse)
 entry_limit_vector=resource.getrlimit(resource.RLIMIT_NOFILE)
 need(entry_limit_vector==ACTOR_ENTRY_LIMIT_VECTOR_V19,Refuse)
 ACTOR_ENTRY_LIMIT_CERTIFIED_V19=True
 resource.setrlimit(resource.RLIMIT_NOFILE,(256,entry_limit_vector[1]))
 current_low_limit_vector=resource.getrlimit(resource.RLIMIT_NOFILE)
 need(current_low_limit_vector==(256,entry_limit_vector[1]),Refuse)
 ACTOR_CURRENT_LOW_LIMIT_VECTOR_V19=current_low_limit_vector
 need(len(ACTOR_SIMULTANEOUS_LIVE_ROLE_SET_V19)==len(set(ACTOR_SIMULTANEOUS_LIVE_ROLE_SET_V19))==219,Refuse)
 need(ACTOR_LIVE_HIGH_WATER_V19==219<256 and len(ACTOR_CLONE3_CPYTHON_SUBCONDITIONS_V19)==6,Refuse)
 return entry_limit_vector,current_low_limit_vector

def main():
 actor_entry_limit_transition_v19()
 actor_bootstrap_registry()
 v19_validate_actor_control_surface()
 return V15_ACTOR_MAIN_V19()

# P27 RUNNER V20 ACTOR FINAL ENTRY BEGIN 20A0C801
RUNNER_INTERNAL_REVISION_V20=b"V20"
ACTOR_WRAPPER_MONOTONE_PHASES_V20=(
 b"NO_CONSTRUCTOR",b"CONSTRUCTOR_ALLOCATION_POSSIBLE",b"LOCAL_STRONG_REFERENCE",
 b"CONSTRUCTOR_IN_PROGRESS",b"CONSTRUCTOR_EFFECT_UNKNOWN",b"ATTACH_VERIFY_POSSIBLE",
 b"ATTACH_VERIFY_UNKNOWN",b"FILENO_INITIAL_POSSIBLE",b"FILENO_INITIAL_UNKNOWN",
 b"FILENO_REPAIR_POSSIBLE",b"FILENO_REPAIR_UNKNOWN",b"FILENO_OBSERVED_ATTACHED",
 b"FILENO_OBSERVED_DETACHED",b"DETACH_IN_PROGRESS",b"DETACH_EFFECT_UNKNOWN",
 b"DETACH_POSTCONDITION_POSSIBLE",b"DETACH_POSTCONDITION_UNKNOWN",
 b"DETACH_OBSERVED_ATTACHED",b"DETACH_RETRY_IN_PROGRESS",b"DETACH_RETRY_EFFECT_UNKNOWN",
 b"DETACH_RETRY_POSTCONDITION_POSSIBLE",b"DETACH_RETRY_POSTCONDITION_UNKNOWN",
 b"RETAINED_ATTACHED_NO_RETRY",b"DETACH_CONFIRMED",b"PROVED_CLOSED",
)

def actor_partial_begin_reconcile_v20(record,role):
 number=record.raw_fd
 if number>=0:
  record.semantic_role=role;record.state=b"CLOSE_RETRY"
  cell=record.raw_cell;cell.c_value.value=number;cell.record_id=record.record_id
  cell.epoch=record.epoch;cell.state=b"SHADOW_OF_RECORD"
  need(record.raw_fd==number and record.state==b"CLOSE_RETRY")
  return b"SOLE_RECORD_AUTHORITY_RETAINED"
 actor_record_reset_closed_v19(record)
 need(record.state==b"CLOSED" and record.raw_fd==-1 and record.raw_cell.c_value.value==-1)
 return b"CLOSED_NO_EFFECT"

def actor_begin_acquisition(role,kind):
 record=None
 try:
  need(role in ACTOR_FD_ROLE_MAP and ACTOR_FD_ROLE_MAP[role]==kind)
  record=ACTOR_FD_REGISTRY[role]
  need(record.state==b"CLOSED" and record.raw_fd==-1)
  actor_record_reset_closed_v19(record)
  record.epoch+=1;record.semantic_role=role;record.state=b"ACQUIRING"
  record.identity=None;record.physical_identity=None;record.leaf_identity=None
  record.verified_kill_leaf_identity=None;record.access=b"UNKNOWN"
  record.provenance=(b"ACTOR_PRODUCER_V20",role,record.epoch)
  record.endpoint_state=b"NO_WRAPPER";record.wrapper_ref=None
  record.detached_raw_fd=-1;record.wrapper_phase=b"NO_CONSTRUCTOR"
  record.wrapper_local_fallback=-1;record.wrapper_probe_done=False
  record.wrapper_detach_attempted=False
  actor_raw_prearm_v19(record.raw_cell,record)
  return record
 except BaseException:
  if record is not None:actor_partial_begin_reconcile_v20(record,role)
  raise

def actor_pair_boundary_v19(left_role,right_role,operation,flags=0):
 left=right=None;cells=None;result=-1;saved=0
 try:
  cells=ACTOR_PIPE2_OUT_V19 if operation==b"PIPE2" else ACTOR_SOCKETPAIR_OUT_V19
  cells[0]=-1;cells[1]=-1
  left=actor_begin_acquisition(left_role,ACTOR_FD_ROLE_MAP[left_role])
  right=actor_begin_acquisition(right_role,ACTOR_FD_ROLE_MAP[right_role])
  if operation==b"PIPE2":result=LIBC.pipe2(cells,flags)
  else:result=LIBC.socketpair(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC|socket.SOCK_NONBLOCK,0,cells)
  saved=ctypes.get_errno()
 finally:
  if cells is not None:actor_reconcile_pair_outputs_v19(left,right,cells)
 if result<0:
  for role in (left_role,right_role):
   if actor_record_live_v19(ACTOR_FD_REGISTRY[role]):
    try:actor_close_record(role)
    except BaseException:pass
  raise OSError(saved,os.strerror(saved))
 first=None
 try:actor_finish_adoption(left_role)
 except BaseException as error:first=error
 try:actor_finish_adoption(right_role)
 except BaseException as error:
  if first is None:first=error
 if first is not None:
  for role in (left_role,right_role):
   if actor_record_live_v19(ACTOR_FD_REGISTRY[role]):
    try:actor_close_record(role)
    except BaseException:pass
  raise first
 ACTOR_PAIR_RECORD_RETURN_V19.left=left;ACTOR_PAIR_RECORD_RETURN_V19.right=right
 return ACTOR_PAIR_RECORD_RETURN_V19

def actor_wrapper_observe_v20(record,wrapper,possible,unknown):
 record.wrapper_phase=possible
 try:observed=wrapper.fileno()
 except BaseException as error:
  record.wrapper_phase=unknown
  raise ConsumedIndeterminate("actor-wrapper-fileno-effect-unknown-retained") from error
 if observed==-1:
  record.detached_raw_fd=record.raw_fd;record.endpoint_state=b"DETACHED"
  record.wrapper_phase=b"FILENO_OBSERVED_DETACHED";record.wrapper_ref=None
  return -1
 need(observed==record.raw_fd)
 record.endpoint_state=b"ATTACHED";record.wrapper_phase=b"FILENO_OBSERVED_ATTACHED"
 return observed

def actor_wrapper_detach_attempt_v20(record,wrapper,retry=False):
 record.wrapper_phase=b"DETACH_RETRY_IN_PROGRESS" if retry else b"DETACH_IN_PROGRESS"
 try:detached=wrapper.detach()
 except BaseException as error:
  record.wrapper_phase=b"DETACH_RETRY_EFFECT_UNKNOWN" if retry else b"DETACH_EFFECT_UNKNOWN"
  raise ConsumedIndeterminate("actor-wrapper-detach-effect-unknown-retained") from error
 need(detached==record.raw_fd)
 record.detached_raw_fd=detached;record.endpoint_state=b"DETACHED"
 record.wrapper_phase=b"DETACH_CONFIRMED";record.wrapper_ref=None
 return True

def actor_reconcile_wrapper_v19(record):
 wrapper=record.wrapper_ref
 if wrapper is None:
  if record.endpoint_state in (b"DETACHED",b"PROVED_CLOSED"):return True
  record.endpoint_state=b"NO_WRAPPER";return True
 phase=record.wrapper_phase
 if phase in (b"FILENO_REPAIR_UNKNOWN",b"DETACH_POSTCONDITION_UNKNOWN",b"DETACH_RETRY_POSTCONDITION_UNKNOWN",b"RETAINED_ATTACHED_NO_RETRY"):
  record.state=b"CLOSE_RETRY"
  raise ConsumedIndeterminate("actor-wrapper-sole-authority-retained-no-uncontrolled-retry")
 if phase==b"DETACH_EFFECT_UNKNOWN":
  try:observed=actor_wrapper_observe_v20(record,wrapper,b"DETACH_POSTCONDITION_POSSIBLE",b"DETACH_POSTCONDITION_UNKNOWN")
  except BaseException:raise
  if observed==-1:return True
  record.wrapper_phase=b"DETACH_OBSERVED_ATTACHED"
  return actor_wrapper_detach_attempt_v20(record,wrapper,True)
 if phase==b"DETACH_RETRY_EFFECT_UNKNOWN":
  try:observed=actor_wrapper_observe_v20(record,wrapper,b"DETACH_RETRY_POSTCONDITION_POSSIBLE",b"DETACH_RETRY_POSTCONDITION_UNKNOWN")
  except BaseException:raise
  if observed==-1:return True
  record.wrapper_phase=b"RETAINED_ATTACHED_NO_RETRY";record.state=b"CLOSE_RETRY"
  raise ConsumedIndeterminate("actor-wrapper-second-detach-observed-attached-retained")
 if phase in (b"CONSTRUCTOR_EFFECT_UNKNOWN",b"ATTACH_VERIFY_UNKNOWN",b"FILENO_INITIAL_UNKNOWN"):
  observed=actor_wrapper_observe_v20(record,wrapper,b"FILENO_REPAIR_POSSIBLE",b"FILENO_REPAIR_UNKNOWN")
 else:
  observed=actor_wrapper_observe_v20(record,wrapper,b"FILENO_INITIAL_POSSIBLE",b"FILENO_INITIAL_UNKNOWN")
 if observed==-1:return True
 return actor_wrapper_detach_attempt_v20(record,wrapper,False)

def actor_wrapper_adopt_v19(record):
 need(record.state==b"OWNED" and record.raw_fd>=0 and record.wrapper_ref is None)
 wrapper=None;record.endpoint_state=b"NO_WRAPPER"
 record.wrapper_local_fallback=record.raw_fd;record.wrapper_phase=b"CONSTRUCTOR_ALLOCATION_POSSIBLE"
 try:
  wrapper=socket.socket.__new__(socket.socket)
  record.wrapper_ref=wrapper;record.wrapper_phase=b"LOCAL_STRONG_REFERENCE"
  record.wrapper_phase=b"CONSTRUCTOR_IN_PROGRESS"
  socket.socket.__init__(wrapper,fileno=record.raw_fd)
  record.endpoint_state=b"ATTACHED";record.wrapper_phase=b"ATTACH_VERIFY_POSSIBLE"
  observed=wrapper.fileno()
  need(observed==record.raw_fd)
  record.wrapper_phase=b"FILENO_OBSERVED_ATTACHED";return wrapper
 except BaseException:
  record.state=b"CLOSE_RETRY"
  if wrapper is None:
   record.wrapper_phase=b"NO_CONSTRUCTOR";record.wrapper_ref=None
  else:
   if record.wrapper_phase==b"CONSTRUCTOR_IN_PROGRESS":record.wrapper_phase=b"CONSTRUCTOR_EFFECT_UNKNOWN"
   elif record.wrapper_phase==b"ATTACH_VERIFY_POSSIBLE":record.wrapper_phase=b"ATTACH_VERIFY_UNKNOWN"
   try:actor_reconcile_wrapper_v19(record)
   except BaseException:pass
  if record.endpoint_state==b"DETACHED":
   try:actor_close_record(actor_role_for_record_v19(record))
   except BaseException:pass
  raise

def actor_clone3_boundary_v19(cgfd):
 record=None;pid=-1
 try:
  ACTOR_CLONE3_PIDFD_OUT_V19.value=-1
  args=ACTOR_CLONE3_ARGS_V19;args.flags=CLONE_PIDFD|CLONE_INTO_CGROUP
  args.pidfd=ctypes.addressof(ACTOR_CLONE3_PIDFD_OUT_V19)
  args.exit_signal=int(signal.SIGCHLD);args.cgroup=cgfd
  record=actor_begin_acquisition(b"probe_outer_pidfd",b"PROBE_OUTER_PIDFD")
  pid=LIBC.syscall(SYS_CLONE3,ctypes.byref(args),ctypes.sizeof(args))
 finally:
  actor_capture_authoritative_c_v19(record,ACTOR_CLONE3_PIDFD_OUT_V19)
 if pid<0:
  if record is not None and actor_record_live_v19(record):
   try:actor_close_record(b"probe_outer_pidfd")
   except BaseException:pass
  raise ConsumedIndeterminate("clone-return")
 if pid>0:actor_finish_adoption(b"probe_outer_pidfd")
 ACTOR_CLONE_RECORD_RETURN_V19.left=pid;ACTOR_CLONE_RECORD_RETURN_V19.right=record
 return ACTOR_CLONE_RECORD_RETURN_V19

try:
 main()
except Refuse:
 raise SystemExit(80)
except ConsumedFail:
 raise SystemExit(81)
except ConsumedIndeterminate:
 raise SystemExit(82)
except BaseException:
 raise SystemExit(83)
raise SystemExit(0)
P27 RUNNER V20 ACTOR SOURCE END 6C20A4F1

P27 RUNNER V20 WATCHDOG SOURCE BEGIN 9F20C6A3
import array
import ctypes
import errno
import fcntl
import hashlib
import os
import resource
import select
import signal
import socket
import stat
import struct
import sys
import time

PROBES=(b"P00",b"P01D",b"P01C",b"P02",b"P03",b"P04",b"P05",b"P06",b"P07",b"P08",b"P09",b"P10",b"P11",b"P12",b"P13")
FAULT_ORDER=(b"INPUT_AUTH",b"ENTRY_CONTEXT",b"CERTIFICATE_INVALID",b"PRECONSUMPTION_DEADLINE",b"CONSUME_EDGE_UNKNOWN",b"ATTEMPT_COLLISION",b"ATTEMPT_NAMESPACE_UNKNOWN",b"ATTEMPT_DIRFD_UNKNOWN",b"ATTEMPT_BASE_DURABILITY_UNKNOWN",b"INTENT_DURABILITY_UNKNOWN",b"CERTIFICATE_EXPIRED",b"CLOCK_DRIFT",b"DEADLINE_EXPIRED",b"CONTROL_MALFORMED",b"CONTROL_TIMEOUT",b"CONTROL_TRUNCATION",b"CONTROL_LOST",b"SEND_EFFECT_UNKNOWN",b"PIDFD_ACTOR_LOST",b"FD_TRANSFER",b"STAGING_FAULT",b"STAGING_DEADLINE",b"CONTAINMENT_FAULT",b"STOP_WAIT_UNKNOWN",b"PIDFD_BINDING",b"LAUNCH_DEADLINE",b"RELEASE_RECORD_DURABILITY_UNKNOWN",b"RELEASE_EFFECT_UNKNOWN",b"SYSCALL_EFFECT_UNKNOWN",b"WATCHDOG_DEADLINE",b"KILL_TICKET_DURABILITY_UNKNOWN",b"KILL_EFFECT_UNKNOWN",b"CAPTURE_IO",b"CAPTURE_OVERFLOW",b"STDERR_NONEMPTY",b"DIRECT_WAIT_UNKNOWN",b"OUTER_STATUS",b"TRANSCRIPT_LANGUAGE",b"TRANSCRIPT_STRUCTURE",b"TRANSCRIPT_SEMANTICS",b"VALIDATED_DURABILITY_UNKNOWN",b"ACK_DURABILITY_UNKNOWN",b"CONTAINMENT_OBSERVATION_UNKNOWN",b"CONTAINMENT_NOT_EMPTY",b"RECOVERY_DURABILITY_UNKNOWN",b"RETAINED_DURABILITY_UNKNOWN",b"REPORT_CANDIDATE_DURABILITY_UNKNOWN",b"TERMINAL_SEEN_DURABILITY_UNKNOWN",b"REPORT_DURABILITY_UNKNOWN",b"ACK_EFFECT_UNKNOWN",b"RECONCILIATION_UNKNOWN",b"OWNER_CLOSURE_DURABILITY_UNKNOWN",b"TRANSFER_PROTOCOL_UNKNOWN",b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED",b"INTERNAL_INVARIANT")
KNOWN_FAIL={b"CAPTURE_OVERFLOW",b"STDERR_NONEMPTY",b"OUTER_STATUS",b"TRANSCRIPT_LANGUAGE",b"TRANSCRIPT_STRUCTURE",b"TRANSCRIPT_SEMANTICS"}
INDETERMINATE=set(FAULT_ORDER)-KNOWN_FAIL
ENV={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
PYTHON=b"/root/miniconda3/bin/python3"
PYIMAGE=b"/root/miniconda3/bin/python3.12"
SNAPSHOT_EXPECT=(2303269,23672,b"0ea4f324c5175ec196b8118e551a429a6207cd57bacfdaa9903a109046daab92")
SNAPSHOT_TERMINAL=b"BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V2_SUPERVISOR_PREBIND_FAIL_AND_RUNNER_V3_AUTHOR_OPEN_NO_EXECUTION"
SNAPSHOT_TERMINAL_HEX=SNAPSHOT_TERMINAL.hex().encode("ascii")
V15_SHA=b"a27eb1bb5540c18b57094ee26724be75a0c431b3c523385fe1271fb02378b845"
V15_BYTES=228310
V15_LF=4622
V15_TERMINAL=b"BATCH07_P27_E001_SUPERVISOR_HOST_PROBE_RECOVERY_V15_AUTHOR_STOP"
V15_LINKED_EXPECT=(2431,5916064615,0o100644,1,0,0,V15_BYTES,V15_LF,V15_SHA)
V8_SHA=b"72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf"
PY_SHA=b"9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"
CONTEXT_DOMAIN=b"P27E001_V15_DETACHED_ENVELOPE_CONTEXT\x00"
CERTIFICATE_DOMAIN=b"P27E001_V15_CERTIFICATE_DIGEST\x00"
ENVELOPE_TBS_DOMAIN=b"P27E001_V15_ENVELOPE_TBS\x00"
SIGNATURE_DOMAIN=b"P27E001_V15_ISSUER_SIGNATURE_PREIMAGE\x00"
RECEIPT_DOMAIN=b"P27E001_V15_ISSUER_RECEIPT\x00"
RESERVATION_TBS_DOMAIN=b"P27E001_V15_RESERVATION_TBS\x00"
RESERVATION_SIGNATURE_DOMAIN=b"P27E001_V15_RESERVATION_SIGNATURE\x00"
RESERVATION_RECEIPT_DOMAIN=b"P27E001_V15_RESERVATION_RECEIPT\x00"
FINAL_ENVELOPE_DOMAIN=b"P27E001_V15_FINAL_ENVELOPE\x00"
AUTH_DOMAIN=b"P27E001_V15_SESSION_AUTH\x00"
EXTERNAL_ACCEPTANCE_DOMAIN=b"P27E001_V15_EXTERNAL_ACCEPTANCE\x00"
ISSUER_KEY_BIND_DOMAIN=b"P27E001_V15_ISSUER_KEY_BIND\x00"
EMPTY_SHA=b"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
EXACT_SEALS=fcntl.F_SEAL_WRITE|fcntl.F_SEAL_GROW|fcntl.F_SEAL_SHRINK|fcntl.F_SEAL_SEAL
MAX_U63=(1<<63)-1
MAX_FILE=16777216
STREAM_CAP=3145728
TOTAL_NS=18164800000
HOST_NS=17664800000
RELEASE_RECORD_OFFSET_NS=800000000
RELEASE_REPLY_OFFSET_NS=900000000
CLEANUP_NS=2000000000
REPORT_NS=1000000000
RECORD_NS=100000000
CONSUMPTION_NS=250000000
CANDIDATE_RECORD_NS=100000000
NOTICE_NS=100000000
SEEN_RECORD_NS=100000000
REPORT_RECORD_NS=1000000000
PASS_COMMIT_NS=100000000
PASS_MARGIN_NS=10000000
ACK_NS=500000000
A_RECEIPT_NS=100000000
ACK_RECEIPT_RECORD_NS=100000000
RECONCILIATION_RECORD_NS=100000000
OWNER_CLOSURE_RECORD_NS=100000000
CLOSURE_PACKET_NS=100000000
B_EXIT_NS=100000000
FINAL_TOTAL_NS=2510000000
KILL_TICKET_NS=100000000
RECOVERY_RECORD_NS=100000000
CLEANUP_EFFECT_NS=2600000000
FAILURE_TAIL_NS=2610000000
FAILURE_TOTAL_NS=5210000000
REFUSAL_RECORD_NS=20000000
REFUSAL_ACK_NS=20000000
REFUSAL_RECEIPT_WAIT_NS=30000000
REFUSAL_FINALITY_COMMIT_NS=10000000
REFUSAL_OFFER_BUILD_NS=10000000
REFUSAL_OFFER_SEND_NS=20000000
REFUSAL_ACCEPTANCE_RECV_NS=30000000
REFUSAL_ACCEPTANCE_VERIFY_NS=20000000
REFUSAL_ACCEPTANCE_COMMIT_NS=10000000
REFUSAL_ACTOR_CLOSURE_NS=20000000
REFUSAL_CAPABILITY_CLOSE_NS=10000000
REFUSAL_OWNER_RELEASE_NS=10000000
REFUSAL_FINALITY_NS=80000000
REFUSAL_CLOSURE_TAIL_NS=130000000
REFUSAL_TOTAL_NS=210000000
REFUSAL_PHASE_SPEC=((b"REFUSAL_RECORD",REFUSAL_RECORD_NS),(b"REFUSAL_ACK",REFUSAL_ACK_NS),(b"REFUSAL_RECEIPT_WAIT",REFUSAL_RECEIPT_WAIT_NS),(b"REFUSAL_FINALITY",REFUSAL_FINALITY_COMMIT_NS),(b"REFUSAL_OFFER_BUILD",REFUSAL_OFFER_BUILD_NS),(b"REFUSAL_OFFER_SEND",REFUSAL_OFFER_SEND_NS),(b"REFUSAL_ACCEPTANCE_RECV",REFUSAL_ACCEPTANCE_RECV_NS),(b"REFUSAL_ACCEPTANCE_VERIFY",REFUSAL_ACCEPTANCE_VERIFY_NS),(b"REFUSAL_ACCEPTANCE_COMMIT",REFUSAL_ACCEPTANCE_COMMIT_NS),(b"REFUSAL_ACTOR_CLOSURE",REFUSAL_ACTOR_CLOSURE_NS),(b"REFUSAL_CAPABILITY_CLOSE",REFUSAL_CAPABILITY_CLOSE_NS),(b"REFUSAL_CLOSURE",REFUSAL_OWNER_RELEASE_NS))
ACTOR_DISABLE_NS=500000000
TERMINAL_PHASE_SPEC=((b"CANDIDATE_RECORD",CANDIDATE_RECORD_NS),(b"NOTICE",NOTICE_NS),(b"TERMINAL_SEEN_RECORD",SEEN_RECORD_NS),(b"REPORT_RECORD",REPORT_RECORD_NS),(b"PASS_COMMIT",PASS_COMMIT_NS),(b"PASS_MARGIN",PASS_MARGIN_NS),(b"ACK",ACK_NS),(b"A_RECEIPT",A_RECEIPT_NS),(b"ACK_RECEIPT_RECORD",ACK_RECEIPT_RECORD_NS),(b"RECONCILIATION_RECORD",RECONCILIATION_RECORD_NS),(b"OWNER_CLOSURE_RECORD",OWNER_CLOSURE_RECORD_NS),(b"CLOSURE_PACKET",CLOSURE_PACKET_NS),(b"B_EXIT",B_EXIT_NS))
TERMINAL_BIND_KEYS=tuple(b"bound_"+name.lower()+b"_deadline_ns" for name,cap in TERMINAL_PHASE_SPEC)
STAGE_NS=10000000000
CERT_LIFE_NS=360000000000
ENTRY_REMAIN_NS=295482000000
CONSUME_REMAIN_NS=285482000000
PRE_STAGE_REMAIN_NS=285232000000
POST_STAGE_REMAIN_NS=275232000000
POST_CONTAIN_REMAIN_NS=274732000000
KILL_RETURN_NS=5000000
TRANSFER_OFFER_BUILD_NS=20000000
TRANSFER_OFFER_SEND_NS=40000000
TRANSFER_ACCEPTANCE_RECV_NS=80000000
TRANSFER_ACCEPTANCE_VERIFY_NS=40000000
TRANSFER_ACCEPTANCE_COMMIT_NS=20000000
TRANSFER_CAPABILITY_CLOSE_NS=20000000
TRANSFER_OWNER_RELEASE_NS=20000000
TRANSFER_TOTAL_NS=240000000
TRANSFER_PHASE_SPEC=((b"TRANSFER_OFFER_BUILD",TRANSFER_OFFER_BUILD_NS),(b"TRANSFER_OFFER_SEND",TRANSFER_OFFER_SEND_NS),(b"TRANSFER_ACCEPTANCE_RECV",TRANSFER_ACCEPTANCE_RECV_NS),(b"TRANSFER_ACCEPTANCE_VERIFY",TRANSFER_ACCEPTANCE_VERIFY_NS),(b"TRANSFER_ACCEPTANCE_COMMIT",TRANSFER_ACCEPTANCE_COMMIT_NS),(b"TRANSFER_CAPABILITY_CLOSE",TRANSFER_CAPABILITY_CLOSE_NS),(b"TRANSFER_CLOSURE",TRANSFER_OWNER_RELEASE_NS))
MAX_RIGHTS=4
UINT_MAX=(1<<32)-1
DURABLE_VERIFIED=b"DURABLE_VERIFIED"
O_DIR=os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW
AUTH=b""
CERT={}
DEPS=()
ISSUER_KEY_ID=b""
CONTROL_SEND_SEQ=0
CONTROL_RECV_SEQ=0
CONTROL_SEND_STATE=b"IDLE"
EXTERNAL_SEND_SEQ=0
EXTERNAL_RECV_SEQ=0
RESERVATION_DIGEST=b""
ACTOR_PID=0
ACTOR_STARTTIME=0
ENVELOPE_CONTEXT_KEYS=(b"ISSUER_ID",b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0366_SNAPSHOT_BYTES",b"E0366_SNAPSHOT_LF",b"E0366_SNAPSHOT_SHA256",b"E0366_SNAPSHOT_TERMINAL_HEX",b"V15_SHA256",b"NOT_BEFORE_REALTIME_NS",b"NOT_AFTER_REALTIME_NS",b"ONE_SHOT_RESERVED_BY_ISSUER",b"ONE_SHOT_CONSUMED_BY_ISSUER")
ENVELOPE_KEYS=ENVELOPE_CONTEXT_KEYS+(b"ENVELOPE_CONTEXT_SHA256",b"CERTIFICATE_DIGEST_SHA256",b"SIGNATURE_PREIMAGE_SHA256",b"SIGNATURE_ALGORITHM",b"SIGNATURE_HEX",b"ISSUER_RECEIPT_SHA256")
RESERVATION_TBS_KEYS=(b"ISSUER_ID",b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"CERTIFICATE_DIGEST_SHA256",b"FINAL_ENVELOPE_DIGEST_SHA256",b"NOT_BEFORE_REALTIME_NS",b"NOT_AFTER_REALTIME_NS",b"ONE_SHOT_RESERVED_BY_ISSUER",b"ONE_SHOT_CONSUMED_BY_ISSUER",b"SIGNATURE_ALGORITHM")
RESERVATION_KEYS=RESERVATION_TBS_KEYS+(b"SIGNATURE_PREIMAGE_SHA256",b"SIGNATURE_HEX",b"RESERVATION_DIGEST_SHA256")
CERT_KEYS=(b"ISSUER_ID",b"ISSUER_CONTEXT_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"ARCH",b"KERNEL_RELEASE_HEX",b"NOT_BEFORE_REALTIME_NS",b"ABSOLUTE_EXPIRY_REALTIME_NS",b"ABSOLUTE_LIFETIME_NS",b"REALTIME_BIND_NS",b"MONOTONIC_BIND_NS",b"REALTIME_MONOTONIC_MAX_DRIFT_NS",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"E0366_SNAPSHOT_BYTES",b"E0366_SNAPSHOT_LF",b"E0366_SNAPSHOT_SHA256",b"E0366_SNAPSHOT_TERMINAL_HEX",b"HISTORICAL_SNAPSHOT_SEALED",b"V15_SHA256",b"V8_SHA256",b"ACTOR_ENTRY_CAPS",b"ACTOR_ENTRY_NNP",b"ACTOR_ENTRY_SECUREBITS",b"PAYLOAD_FINAL_CAPS",b"PAYLOAD_FINAL_NNP",b"PAYLOAD_FINAL_SECUREBITS",b"ATTEMPT_BASE_DEV",b"ATTEMPT_BASE_INO",b"ATTEMPT_BASE_MODE",b"ATTEMPT_BASE_NLINK",b"ATTEMPT_BASE_UID",b"ATTEMPT_BASE_GID",b"ATTEMPT_BASE_MOUNT_ID",b"ATTEMPT_BASE_MOUNTINFO_SHA256",b"ATTEMPT_BASE_FSTYPE_HEX",b"CGROUP2_FS_MAGIC",b"CGROUP2_MOUNT_ID",b"CGROUP2_MOUNTINFO_SHA256",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO",b"CGROUP_BASE_MODE",b"CGROUP_BASE_NLINK",b"CGROUP_BASE_UID",b"CGROUP_BASE_GID",b"CGROUP_BASE_TYPE_HEX",b"CGROUP_BASE_CONTROLLERS_HEX",b"CGROUP_BASE_SUBTREE_CONTROL_HEX",b"CGROUP_NO_EXTERNAL_MUTATOR",b"CGROUP_CHILD_MODE",b"CGROUP_CHILD_UID",b"CGROUP_CHILD_GID",b"CGROUP_CHILD_TYPE_HEX",b"CGROUP_CHILD_CONTROLLERS_HEX",b"CGROUP_CHILD_SUBTREE_CONTROL_HEX",b"RUNTIME_ROOT_DEV",b"RUNTIME_ROOT_INO",b"RUNTIME_ROOT_MODE",b"RUNTIME_ROOT_NLINK",b"RUNTIME_ROOT_UID",b"RUNTIME_ROOT_GID",b"RUNTIME_ROOT_MOUNT_ID",b"RUNTIME_ROOT_MOUNTINFO_SHA256",b"RUNTIME_ROOT_FSTYPE_HEX",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"SAFE_BIND_MODE",b"SAFE_BIND_NLINK",b"SAFE_BIND_UID",b"SAFE_BIND_GID",b"SAFE_BIND_MOUNT_ID",b"SAFE_BIND_MOUNTINFO_SHA256",b"SAFE_BIND_FSTYPE_HEX",b"SAFE_BIND_NOEXEC",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT",b"KEEPER_BYTES",b"KEEPER_LF",b"KEEPER_SHA256",b"LAUNCHER_BYTES",b"LAUNCHER_LF",b"LAUNCHER_SHA256",b"MARKER_BYTES",b"MARKER_LF",b"MARKER_SHA256",b"CHILD_BYTES",b"CHILD_LF",b"CHILD_SHA256",b"PYTHON_IMAGE_SHA256",b"PYTHON_IMAGE_BYTES",b"PYTHON_IMAGE_DEV",b"PYTHON_IMAGE_INO",b"PYTHON_IMAGE_MODE",b"PYTHON_IMAGE_NLINK",b"PYTHON_IMAGE_UID",b"PYTHON_IMAGE_GID",b"LIBC_PATH_HEX",b"LIBC_DEV",b"LIBC_INO",b"LIBC_MODE",b"LIBC_NLINK",b"LIBC_UID",b"LIBC_GID",b"LIBC_BYTES",b"LIBC_SHA256",b"LIBC_CONFSTR_HEX",b"VALID_SIGNAL_COUNT",b"DEFAULT_SIGNAL_COUNT",b"DEFAULTS_SHA256",b"PRECONSUMPTION_CAP_NS",b"CONSUMPTION_PROGRESS_NS",b"ATTEMPT_DIRFD_PROGRESS_NS",b"STAGING_CAP_NS",b"RELEASE_PROGRESS_NS",b"RELEASE_RECORD_ABSOLUTE_OFFSET_NS",b"RELEASE_REPLY_ABSOLUTE_OFFSET_NS",b"SIGCONT_CALL_RETURN_NS",b"DURABLE_RECORD_PROGRESS_NS",b"WATCHDOG_ARM_PROGRESS_NS",b"WATCHDOG_ACK_PROGRESS_NS",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY",b"CGROUP_KILL_WRITE_RETURN_NS",b"CGROUP_KILL_TO_EMPTY_NS",b"FINAL_REPORT_PROGRESS_NS",b"FINAL_PASS_COMMIT_PROGRESS_NS",b"FINAL_PASS_MARGIN_NS",b"TERMINAL_HANDSHAKE_PROGRESS_NS",b"A_RECEIPT_PROGRESS_NS",b"B_CLOSURE_PROGRESS_NS",b"TERMINAL_CANDIDATE_RECORD_NS",b"TERMINAL_NOTICE_PROGRESS_NS",b"TERMINAL_SEEN_RECORD_NS",b"TERMINAL_ACK_RECEIPT_RECORD_NS",b"TERMINAL_RECONCILIATION_RECORD_NS",b"TERMINAL_OWNER_CLOSURE_RECORD_NS",b"TERMINAL_CLOSURE_PACKET_NS",b"TERMINAL_B_EXIT_NS",b"FAILURE_OVERALL_PROGRESS_NS",b"FAILURE_CLEANUP_EFFECT_PROGRESS_NS",b"FAILURE_TAIL_RESERVE_NS",b"REFUSAL_RECORD_PROGRESS_NS",b"REFUSAL_ACK_PROGRESS_NS",b"REFUSAL_RECEIPT_WAIT_PROGRESS_NS",b"REFUSAL_FINALITY_COMMIT_PROGRESS_NS",b"REFUSAL_FINALITY_DEADLINE_PROGRESS_NS",b"REFUSAL_OFFER_BUILD_PROGRESS_NS",b"REFUSAL_OFFER_SEND_PROGRESS_NS",b"REFUSAL_ACCEPTANCE_RECV_PROGRESS_NS",b"REFUSAL_ACCEPTANCE_VERIFY_PROGRESS_NS",b"REFUSAL_ACCEPTANCE_COMMIT_PROGRESS_NS",b"REFUSAL_ACTOR_CLOSURE_PROGRESS_NS",b"REFUSAL_CAPABILITY_CLOSE_PROGRESS_NS",b"REFUSAL_OWNER_RELEASE_PROGRESS_NS",b"REFUSAL_CLOSURE_TAIL_NS",b"REFUSAL_CLOSURE_DEADLINE_PROGRESS_NS",b"FINAL_TERMINAL_TOTAL_NS",b"ENTRY_MIN_REMAINING_NS",b"CONSUMPTION_MIN_REMAINING_NS",b"PRE_STAGE_MIN_REMAINING_NS",b"POST_STAGE_MIN_REMAINING_NS",b"POST_CONTAIN_MIN_REMAINING_NS",b"ACTOR_RELEASE_DISABLE_PROGRESS_NS",b"EXTERNAL_OWNER_PID",b"EXTERNAL_OWNER_STARTTIME",b"EXTERNAL_OWNER_UID",b"EXTERNAL_OWNER_GID",b"EXTERNAL_TRANSFER_MANIFEST_BYTES",b"EXTERNAL_TRANSFER_MANIFEST_SHA256",b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE",b"CLONE3_CPYTHON_GATE_ID",b"CLONE3_CPYTHON_GATE_PASS",b"DELETED_CGROUP_FD_GATE_ID",b"DELETED_CGROUP_FD_GATE_PASS",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_ID",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_PASS",b"EXTERNAL_SURVIVAL_GATE_ID",b"EXTERNAL_SURVIVAL_GATE_PASS",b"OUTER_RECONCILER_GATE_ID",b"OUTER_RECONCILER_GATE_PASS",b"ISSUER_CRYPTOGRAPHY_GATE_ID",b"ISSUER_CRYPTOGRAPHY_GATE_PASS",b"DEP_COUNT")

class StaticReject(Exception):
 pass

class CertificateExpired(StaticReject):
 pass

class FaultSet(StaticReject):
 def __init__(self,faults):
  self.faults=set(faults)
  super().__init__("fault-set")

class RemoteAbort(FaultSet):
 pass

class ControlLost(FaultSet):
 def __init__(self,label):
  super().__init__({b"CONTROL_LOST"})

class SendEffectUnknown(FaultSet):
 def __init__(self,label):
  super().__init__({b"SEND_EFFECT_UNKNOWN"})

class PidfdActorLost(FaultSet):
 def __init__(self,label):
  super().__init__({b"PIDFD_ACTOR_LOST"})

class RefusalFinalityPending(Exception):
 pass

def need(value):
 if not value:raise StaticReject("static-reject")

def udec(raw,low=0,high=MAX_U63):
 need(type(raw)is bytes and raw and raw.isdigit() and (len(raw)==1 or raw[0]!=48))
 value=int(raw);need(low<=value<=high and str(value).encode()==raw);return value

def h64(raw):
 need(type(raw)is bytes and len(raw)==64 and all(x in b"0123456789abcdef" for x in raw));return raw

def even_hex(raw,cap=MAX_FILE):
 need(type(raw)is bytes and len(raw)%2==0 and len(raw)<=2*cap)
 need(all(x in b"0123456789abcdef" for x in raw))
 result=bytes.fromhex(raw.decode("ascii"));need(result.hex().encode()==raw);return result

def octal(raw):
 need(raw and all(x in b"01234567" for x in raw));value=int(raw,8);need(format(value,"o").encode()==raw);return value

def sha(raw):
 return hashlib.sha256(raw).hexdigest().encode("ascii")

ED_Q=(1<<255)-19
ED_L=(1<<252)+27742317777372353535851937790883648493
ED_D=(-121665*pow(121666,ED_Q-2,ED_Q))%ED_Q
ED_I=pow(2,(ED_Q-1)//4,ED_Q)

def ed_xrecover(y):
 xx=(y*y-1)*pow(ED_D*y*y+1,ED_Q-2,ED_Q)%ED_Q;x=pow(xx,(ED_Q+3)//8,ED_Q)
 if (x*x-xx)%ED_Q:x=x*ED_I%ED_Q
 need((x*x-xx)%ED_Q==0);return x

def ed_decode(raw):
 need(type(raw)is bytes and len(raw)==32);y=int.from_bytes(raw,"little")&((1<<255)-1);sign=raw[31]>>7;need(y<ED_Q);x=ed_xrecover(y)
 if (x&1)!=sign:x=ED_Q-x
 need((-x*x+y*y-1-ED_D*x*x*y*y)%ED_Q==0);return (x,y,1,x*y%ED_Q)

def ed_add(p,q):
 x1,y1,z1,t1=p;x2,y2,z2,t2=q;a=(y1-x1)*(y2-x2)%ED_Q;b=(y1+x1)*(y2+x2)%ED_Q;c=2*ED_D*t1*t2%ED_Q;d=2*z1*z2%ED_Q
 e=(b-a)%ED_Q;f=(d-c)%ED_Q;g=(d+c)%ED_Q;h=(b+a)%ED_Q;return (e*f%ED_Q,g*h%ED_Q,f*g%ED_Q,e*h%ED_Q)

def ed_scalar(point,scalar):
 result=(0,1,1,0);current=point
 while scalar:
  if scalar&1:result=ed_add(result,current)
  current=ed_add(current,current);scalar>>=1
 return result

def ed_encode(point):
 x,y,z,t=point;inverse=pow(z,ED_Q-2,ED_Q);x=x*inverse%ED_Q;y=y*inverse%ED_Q;encoded=bytearray(y.to_bytes(32,"little"));encoded[31]|=(x&1)<<7;return bytes(encoded)

def verify_ed25519(public_key,message,signature):
 need(len(public_key)==32 and len(signature)==64);r=signature[:32];s=int.from_bytes(signature[32:],"little");need(s<ED_L)
 public=ed_decode(public_key);ed_decode(r);base_y=4*pow(5,ED_Q-2,ED_Q)%ED_Q;base_x=ed_xrecover(base_y)
 if base_x&1:base_x=ED_Q-base_x
 base=(base_x,base_y,1,base_x*base_y%ED_Q);challenge=int.from_bytes(hashlib.sha512(r+public_key+message).digest(),"little")%ED_L
 need(ed_encode(ed_scalar(base,s))==ed_encode(ed_add(ed_decode(r),ed_scalar(public,challenge))));return True

def read_all(number,cap=16777216):
 os.lseek(number,0,os.SEEK_SET);parts=[];total=0
 while True:
  chunk=os.read(number,min(1048576,cap-total+1))
  if not chunk:break
  total+=len(chunk);need(total<=cap);parts.append(chunk)
 return b"".join(parts)

def exact_text(raw,size,lf,digest,terminal):
 ascii_file(raw,size);need((len(raw),raw.count(b"\n"),sha(raw))==(size,lf,digest))
 lines=raw[:-1].split(b"\n");need(lines and lines[-1]==terminal and lines.count(terminal)==1);return raw

def extract_one(raw,begin,end):
 lead=begin+b"\n";tail=end+b"\n";need(raw.count(lead)==1 and raw.count(tail)==1)
 start=raw.index(lead)+len(lead);stop=raw.index(tail,start);return raw[start:stop]

def ascii_file(raw,cap=16777216):
 need(type(raw)is bytes and 0<len(raw)<=cap and raw.endswith(b"\n"))
 need(all(x==10 or 32<=x<=126 for x in raw));return raw

def seals(number):
 need(fcntl.fcntl(number,fcntl.F_GET_SEALS)==EXACT_SEALS)

def fd_access(number,mode):
 need(fcntl.fcntl(number,fcntl.F_GETFL)&os.O_ACCMODE==mode)

def sealed_carrier(number,cap):
 seals(number);fd_access(number,os.O_RDWR);held=os.fstat(number)
 need(stat.S_ISREG(held.st_mode) and held.st_nlink==0 and held.st_uid==held.st_gid==0)
 raw=read_all(number,cap);need(held.st_size==len(raw) and len(raw)<=cap)
 return raw

def linked_frozen_carrier(number,expected,terminal):
 fd_access(number,os.O_RDONLY);held=os.fstat(number);raw=read_all(number,expected[6])
 need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,held.st_size,raw.count(b"\n"),sha(raw))==expected)
 exact_text(raw,expected[6],expected[7],expected[8],terminal);return raw


CONTROL_SPEC={
 b"V15_ABORT":(b"ABORTING",b"*",b"ABORT_NOTICE",b"control_deadline_ns"),
 b"V15_READY":(b"READY",b"WAIT_READY",b"NO_EFFECT",b"ready_deadline_ns"),
 b"V15_REFUSE_PREBEGIN":(b"REFUSE_PREBEGIN",b"WAIT_BEGIN",b"NO_CONSUME_REFUSAL",b"consume_deadline_ns"),
 b"V15_REFUSE_POSTARM":(b"REFUSE_POSTARM",b"WAIT_COMMIT",b"NO_CONSUME_REFUSAL",b"consume_deadline_ns"),
 b"V15_REFUSE_ACK":(b"REFUSAL_CLOSED_NO_CONSUME",b"WAIT_REFUSAL_ACK",b"REFUSAL_ACK_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V15_REFUSE_ACK_RECEIPT":(b"REFUSAL_ACK_RECEIVED",b"WAIT_REFUSAL_RECEIPT",b"NO_REPLAY_RECEIPT",b"consume_deadline_ns"),
 b"V15_REFUSAL_CLOSED":(b"REFUSAL_DURABLY_CLOSED",b"WAIT_REFUSAL_CLOSED",b"OWNER_CLOSURE",b"consume_deadline_ns"),
 b"V15_CONSUME_BEGIN":(b"CONSUME_BEGIN",b"WAIT_BEGIN",b"BEGIN_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V15_CONSUME_ARMED":(b"CONSUME_ARMED",b"WAIT_ARM",b"ARM_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V15_CONSUME_COMMIT":(b"CONSUME_COMMIT",b"WAIT_COMMIT",b"COMMIT_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V15_CONSUMED_DURABLE":(b"CONSUMED_DURABLE",b"WAIT_CONSUMED",b"INTENT_DURABLE",b"consume_deadline_ns"),
 b"V15_STAGE_DURABLE":(b"STAGE_DURABLE",b"WAIT_STAGE",b"FD_TRANSFER",b"stage_deadline_ns"),
 b"V15_STAGE_ACK":(b"STAGE_BOUND",b"WAIT_STAGE_ACK",b"STAGE_VERIFIED",b"stage_deadline_ns"),
 b"V15_CONTAINMENT":(b"CONTAINMENT_CANDIDATE",b"WAIT_CONTAINMENT",b"FD_TRANSFER",b"contain_deadline_ns"),
 b"V15_CONTAINMENT_ACK":(b"CONTAINMENT_BOUND",b"WAIT_CONTAINMENT_ACK",b"CONTAINMENT_VERIFIED",b"contain_deadline_ns"),
 b"V15_STREAM_ARM":(b"STREAM_ARM",b"WAIT_STREAM_ARM",b"FD_TRANSFER",b"launch_deadline_ns"),
 b"V15_STREAMS_ARMED":(b"STREAMS_ARMED",b"WAIT_STREAMS_ARMED",b"FD_VERIFIED",b"launch_deadline_ns"),
 b"V15_PIDFD_ARM":(b"PIDFD_ARM",b"WAIT_PIDFD_ARM",b"FD_TRANSFER",b"launch_deadline_ns"),
 b"V15_PIDFD_ARMED":(b"PIDFD_ARMED",b"WAIT_PIDFD_ARMED",b"PIDFD_VERIFIED",b"launch_deadline_ns"),
 b"V15_RELEASE_CANDIDATE":(b"RELEASE_CANDIDATE",b"WAIT_RELEASE",b"RELEASE_AUTHORIZATION",b"launch_deadline_ns"),
 b"V15_RELEASE_DURABLE":(b"RELEASE_DURABLE",b"WAIT_RELEASE_DURABLE",b"RELEASE_RECORD_DURABLE",b"launch_deadline_ns"),
 b"V15_RESULT":(b"RESULT",b"WAIT_RESULT",b"RESULT_NOTICE",b"result_deadline_ns"),
 b"V15_RESULT_FRAME":(b"RESULT_FRAME",b"WAIT_RESULT_FRAME",b"RESULT_FRAME",b"result_deadline_ns"),
 b"V15_RESULT_END":(b"RESULT_END",b"WAIT_RESULT_END",b"RESULT_COMPLETE",b"result_deadline_ns"),
 b"V15_VALIDATED_CANDIDATE":(b"VALIDATED_CANDIDATE",b"WAIT_VALIDATED",b"VALIDATION_NOTICE",b"ack_deadline_ns"),
 b"V15_VALIDATED_DURABLE":(b"VALIDATED_DURABLE",b"WAIT_VALIDATED_DURABLE",b"VALIDATED_RECORD_DURABLE",b"ack_deadline_ns"),
 b"V15_ACK_COMMIT_INTENT":(b"ACK_COMMIT_INTENT",b"WAIT_ACK_INTENT",b"ACK_COMMIT",b"ack_deadline_ns"),
 b"V15_COMMITTED":(b"COMMITTED",b"WAIT_COMMITTED",b"COMMIT_RECORD_DURABLE",b"ack_deadline_ns"),
 b"V15_COMMITTED_SEEN":(b"COMMITTED_SEEN",b"WAIT_COMMITTED_SEEN",b"ACK_RECEIPT",b"ack_deadline_ns"),
 b"V15_EMPTY_FINAL_QUERY":(b"EMPTY_FINAL_QUERY",b"WAIT_EMPTY_QUERY",b"REMOVE_QUERY",b"remove_deadline_ns"),
 b"V15_EMPTY_FINAL_CONFIRMED":(b"EMPTY_FINAL_CONFIRMED",b"WAIT_EMPTY_CONFIRMED",b"EMPTY_OBSERVED",b"remove_deadline_ns"),
 b"V15_CGROUP_REMOVED":(b"CGROUP_REMOVED",b"WAIT_REMOVED",b"REMOVE_EFFECT",b"remove_deadline_ns"),
 b"V15_REMOVE_ACK":(b"REMOVE_ACK",b"WAIT_REMOVE_ACK",b"REMOVAL_VERIFIED",b"remove_deadline_ns"),
 b"V15_FINALIZE_CANDIDATE":(b"FINALIZE_CANDIDATE",b"WAIT_FINALIZE",b"FINALIZE_NOTICE",b"candidate_deadline_ns"),
 b"V15_TERMINAL_CANDIDATE_DURABLE":(b"TERMINAL_CANDIDATE_DURABLE",b"WAIT_TERMINAL_CANDIDATE",b"CANDIDATE_DURABLE",b"candidate_deadline_ns"),
 b"V15_TERMINAL_FAILURE_DURABLE":(b"TERMINAL_FAILURE_DURABLE",b"WAIT_TERMINAL_FAILURE",b"FAILURE_REPORT_DURABLE",b"candidate_deadline_ns"),
 b"V15_TERMINAL_SEEN":(b"TERMINAL_SEEN",b"WAIT_TERMINAL_SEEN",b"TERMINAL_SEEN",b"seen_deadline_ns"),
 b"V15_TERMINAL_ACK":(b"TERMINAL_ACK",b"WAIT_TERMINAL_ACK",b"ACK_SEND_EFFECT_UNKNOWN",b"ack_deadline_ns"),
 b"V15_TERMINAL_ACK_RECEIPT":(b"ACK_RECEIVED_NO_REPLAY",b"WAIT_ACK_RECEIPT",b"NO_REPLAY_RECEIPT",b"receipt_deadline_ns"),
 b"V15_TERMINAL_CLOSED":(b"OWNER_CLOSED",b"WAIT_OWNER_CLOSED",b"OWNER_CLOSURE",b"closure_deadline_ns")
}
CONTROL_DEADLINE_KEYS=(b"ready_deadline_ns",b"control_deadline_ns",b"consume_deadline_ns",b"stage_deadline_ns",b"contain_deadline_ns",b"launch_deadline_ns",b"result_deadline_ns",b"ack_deadline_ns",b"remove_deadline_ns",b"candidate_deadline_ns",b"seen_deadline_ns",b"pass_deadline_ns",b"margin_deadline_ns",b"receipt_deadline_ns",b"closure_deadline_ns",b"transfer_deadline_ns",b"terminal_deadline_ns")
CONTROL_RESERVED={b"state",b"expected_state",b"ordinal",b"probe",b"auth_id",b"sender",b"effect_state"}|set(CONTROL_DEADLINE_KEYS)

def packet(kind,pairs):
 global CONTROL_SEND_SEQ
 need(kind in CONTROL_SPEC and b"|" not in kind and b"\n" not in kind)
 provided={}
 for key,value in pairs:
  need(key and value and b"|" not in key+value and b"\n" not in key+value and b"=" not in key+value and key not in provided)
  provided[key]=value
 spec_state,spec_receiver,spec_effect,deadline_key=CONTROL_SPEC[kind]
 state=provided.pop(b"state",spec_state);receiver=provided.pop(b"expected_state",spec_receiver);effect=provided.pop(b"effect_state",spec_effect)
 if kind==b"V15_ABORT":need(state==spec_state and effect==spec_effect and receiver not in (b"",b"*"))
 else:need((state,receiver,effect)==(spec_state,spec_receiver,spec_effect) and state!=b"*" and receiver!=b"*" and effect!=b"*")
 ordinal=provided.pop(b"ordinal");probe=provided.pop(b"probe")
 if b"auth_id" in provided:need(provided.pop(b"auth_id")==AUTH)
 if b"sender" in provided:need(provided.pop(b"sender")==b"B")
 need(deadline_key in provided);deadline=provided.pop(deadline_key);udec(deadline,1)
 need(not any(key in CONTROL_RESERVED for key in provided))
 CONTROL_SEND_SEQ+=1
 transition=state+b"->"+receiver+b":"+effect
 body=(kind+b"|protocol_version=14|session_id="+AUTH+b"|message_seq="+str(CONTROL_SEND_SEQ).encode()+b"|message_sender="+b"B"+b"|transition_id="+transition+b"|sender_state="+state+b"|expected_receiver_state="+receiver+b"|slot_ordinal="+ordinal+b"|slot_probe="+probe+b"|effect_state="+effect+b"|deadline_name="+deadline_key+b"|absolute_deadline_ns="+deadline)
 for key,value in pairs:
  if key not in CONTROL_RESERVED:body+=b"|"+key+b"="+value
 return body+b"\n"

def reserve_packet(kind,pairs):
 global CONTROL_SEND_SEQ
 before=CONTROL_SEND_SEQ
 try:
  raw=packet(kind,pairs);reserved=CONTROL_SEND_SEQ;need(reserved==before+1);return raw,reserved
 finally:
  if CONTROL_SEND_SEQ==before+1:CONTROL_SEND_SEQ=before

def activate_reserved_packet(raw,reserved):
 global CONTROL_SEND_SEQ
 need(type(raw)is bytes and reserved==CONTROL_SEND_SEQ+1);CONTROL_SEND_SEQ=reserved;return raw

def receiver_binding(actual_pre_state,ordinal,probe,inherited_deadline):
 need(type(actual_pre_state)is bytes and actual_pre_state and type(ordinal)is bytes and ordinal and type(probe)is bytes and probe and type(inherited_deadline)is int and inherited_deadline>0)
 return (actual_pre_state,ordinal,probe,inherited_deadline)

def received_binding(raw,actual_pre_state,ordinal,probe,deadline_name,local_ceiling):
 need(type(raw)is bytes and type(deadline_name)is bytes and deadline_name in CONTROL_DEADLINE_KEYS and type(local_ceiling)is int and local_ceiling>0)
 fields=raw[:-1].split(b"|") if raw.endswith(b"\n") else ()
 names=[item.split(b"=",1)[1] for item in fields if item.startswith(b"deadline_name=")]
 absolutes=[item.split(b"=",1)[1] for item in fields if item.startswith(b"absolute_deadline_ns=")]
 need(len(names)==len(absolutes)==1 and names[0]==deadline_name)
 inherited=udec(absolutes[0],1);need(inherited<=local_ceiling)
 return receiver_binding(actual_pre_state,ordinal,probe,inherited)

def parse_packet(raw,kind,keys,binding):
 global CONTROL_RECV_SEQ
 if kind!=b"V15_ABORT" and raw.startswith(b"V15_ABORT|"):
  actual_pre_state,actual_ordinal,actual_probe,local_ceiling=binding
  abort_binding=received_binding(raw,actual_pre_state,actual_ordinal,actual_probe,b"control_deadline_ns",local_ceiling)
  values,faults=parse_abort(raw,b"A",abort_binding);error=RemoteAbort(faults);error.values=values;raise error
 need(type(raw)is bytes and raw.endswith(b"\n") and raw.count(b"\n")==1 and all(x==10 or 32<=x<=126 for x in raw))
 common_keys=(b"protocol_version",b"session_id",b"message_seq",b"message_sender",b"transition_id",b"sender_state",b"expected_receiver_state",b"slot_ordinal",b"slot_probe",b"effect_state",b"deadline_name",b"absolute_deadline_ns")
 physical=tuple(key for key in keys if key not in CONTROL_RESERVED)
 fields=raw[:-1].split(b"|");need(fields[0]==kind and len(fields)==1+len(common_keys)+len(physical))
 common={}
 for key,item in zip(common_keys,fields[1:1+len(common_keys)]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and parts[1] and key not in common);common[key]=parts[1]
 result={}
 for key,item in zip(physical,fields[1+len(common_keys):]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and parts[1] and key not in result and key not in common);result[key]=parts[1]
 spec_state,spec_receiver,spec_effect,deadline_key=CONTROL_SPEC[kind]
 need(common[b"protocol_version"]==b"14" and common[b"session_id"]==AUTH and common[b"message_sender"]==b"A")
 need(common[b"transition_id"]==common[b"sender_state"]+b"->"+common[b"expected_receiver_state"]+b":"+common[b"effect_state"])
 if kind==b"V15_ABORT":need(common[b"sender_state"]==spec_state and common[b"effect_state"]==spec_effect and common[b"expected_receiver_state"] not in (b"",b"*"))
 else:need((common[b"sender_state"],common[b"expected_receiver_state"],common[b"effect_state"])==(spec_state,spec_receiver,spec_effect))
 need(common[b"deadline_name"]==deadline_key);deadline=udec(common[b"absolute_deadline_ns"],1)
 actual_pre_state,actual_ordinal,actual_probe,inherited_deadline=binding
 need((actual_pre_state,actual_ordinal,actual_probe,inherited_deadline)==(common[b"expected_receiver_state"],common[b"slot_ordinal"],common[b"slot_probe"],deadline))
 sequence=udec(common[b"message_seq"],1);need(sequence==CONTROL_RECV_SEQ+1);CONTROL_RECV_SEQ=sequence
 result.update({b"state":common[b"sender_state"],b"expected_state":common[b"expected_receiver_state"],b"ordinal":common[b"slot_ordinal"],b"probe":common[b"slot_probe"],b"auth_id":common[b"session_id"],b"sender":common[b"message_sender"],b"effect_state":common[b"effect_state"],deadline_key:str(deadline).encode(),b"message_seq":str(sequence).encode(),b"packet_sha256":sha(raw)})
 return result

def parse_fixed(raw,header,keys,end):
 ascii_file(raw);lines=raw[:-1].split(b"\n")
 need(len(lines)==len(keys)+2 and lines[0]==header and lines[-1]==end);result={}
 for key,line in zip(keys,lines[1:-1]):
  parts=line.split(b"=",1);need(len(parts)==2 and parts[0]==key and key not in result);result[key]=parts[1]
 return result

def fault_csv(faults):
 ordered=tuple(x for x in FAULT_ORDER if x in faults);need(len(ordered)==len(faults))
 return b"NONE" if not ordered else b",".join(ordered)

def parse_fault_csv(raw,allow_none):
 if raw==b"NONE":need(allow_none);return set()
 parts=raw.split(b",");need(parts and all(x in FAULT_ORDER for x in parts))
 need(len(parts)==len(set(parts)) and tuple(x for x in FAULT_ORDER if x in set(parts))==tuple(parts))
 return set(parts)

def parse_abort(raw,want_sender,binding):
 keys=(b"state",b"ordinal",b"probe",b"effect_state",b"causal_state",b"causal_effect",b"stage_present",b"release_disabled",b"terminal_deadline_ns",b"fault_set",b"control_deadline_ns")
 values=parse_packet(raw,b"V15_ABORT",keys,binding)
 need(values[b"sender"]==want_sender and values[b"state"]==b"ABORTING" and values[b"expected_state"]==binding[0] and values[b"effect_state"]==b"ABORT_NOTICE")
 causal_effects=(b"PREBEGIN",b"BEGIN_SEND_EFFECT_UNKNOWN",b"ARM_SEND_EFFECT_UNKNOWN",b"COMMIT_SEND_EFFECT_UNKNOWN",b"CONSUMED",b"PASS_COMMITTED",b"ACK_SEND_EFFECT_UNKNOWN",b"OWNER_CLOSED")
 need(values[b"causal_state"] and values[b"causal_effect"] in causal_effects and values[b"ordinal"] and values[b"probe"])
 need(values[b"stage_present"] in (b"0",b"1") and values[b"release_disabled"] in (b"0",b"1"))
 if want_sender==b"A":need(values[b"release_disabled"]==b"1")
 if want_sender==b"B" and values[b"causal_state"]==b"CLEANUP_RELEASE_DISABLE":need(values[b"release_disabled"]==b"0")
 deadline=udec(values[b"terminal_deadline_ns"])
 if values[b"causal_effect"] in (b"PASS_COMMITTED",b"ACK_SEND_EFFECT_UNKNOWN",b"OWNER_CLOSED"):need(deadline>0)
 faults=parse_fault_csv(values[b"fault_set"],False);return values,faults

def canonical_envelope_context(values):
 body=b"P27E001_ISSUER_CONTEXT_V15\n"
 for key in ENVELOPE_CONTEXT_KEYS:body+=key+b"="+values[key]+b"\n"
 return domain_frame(CONTEXT_DOMAIN,b"ENVELOPE_CONTEXT_RAW",body+b"CONTEXT_END=1\n")

def envelope_tbs(values,certificate_digest):
 body=b"P27E001_ISSUER_ENVELOPE_TBS_V15\n"
 for key in ENVELOPE_CONTEXT_KEYS:body+=key+b"="+values[key]+b"\n"
 body+=b"ENVELOPE_CONTEXT_SHA256="+values[b"ENVELOPE_CONTEXT_SHA256"]+b"\nCERTIFICATE_DIGEST_SHA256="+certificate_digest+b"\nSIGNATURE_ALGORITHM="+values[b"SIGNATURE_ALGORITHM"]+b"\nENVELOPE_TBS_END=1\n"
 return domain_frame(ENVELOPE_TBS_DOMAIN,b"ENVELOPE_TBS_RAW",body)

def issuer_signature_preimage(cert_raw,env_tbs):
 payload=length_frame(b"CERTIFICATE_RAW",cert_raw)+length_frame(b"ENVELOPE_TBS",env_tbs)+b"SIGNATURE_PREIMAGE_END=1\n"
 return domain_frame(SIGNATURE_DOMAIN,b"ISSUER_SIGNATURE_TBS_RAW",payload)

def issuer_receipt_preimage(context_digest,certificate_digest,signature_digest,algorithm,signature):
 payload=(b"ENVELOPE_CONTEXT_SHA256="+context_digest+b"\nCERTIFICATE_DIGEST_SHA256="+certificate_digest+b"\nSIGNATURE_PREIMAGE_SHA256="+signature_digest+b"\nSIGNATURE_ALGORITHM="+algorithm+b"\nSIGNATURE_HEX="+signature+b"\nISSUER_RECEIPT_END=1\n")
 return domain_frame(RECEIPT_DOMAIN,b"ISSUER_RECEIPT_TBS_RAW",payload)

def envelope(raw):
 values=parse_fixed(raw,b"P27E001_ISSUER_ENVELOPE_V15",ENVELOPE_KEYS,b"ENVELOPE_END=1")
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V15",b"E0366_SNAPSHOT_BYTES":str(SNAPSHOT_EXPECT[0]).encode(),b"E0366_SNAPSHOT_LF":str(SNAPSHOT_EXPECT[1]).encode(),b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"V15_SHA256":V15_SHA,b"ONE_SHOT_RESERVED_BY_ISSUER":b"1",b"ONE_SHOT_CONSUMED_BY_ISSUER":b"0",b"SIGNATURE_ALGORITHM":b"ED25519_EXTERNAL_GATE_V15"}
 for key,value in exact.items():need(values[key]==value)
 for key in (b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"ENVELOPE_CONTEXT_SHA256",b"CERTIFICATE_DIGEST_SHA256",b"SIGNATURE_PREIMAGE_SHA256",b"ISSUER_RECEIPT_SHA256"):h64(values[key])
 sig=values[b"SIGNATURE_HEX"];need(len(sig)==128 and all(x in b"0123456789abcdef" for x in sig))
 before=udec(values[b"NOT_BEFORE_REALTIME_NS"]);after=udec(values[b"NOT_AFTER_REALTIME_NS"]);need(before<after)
 need(values[b"ENVELOPE_CONTEXT_SHA256"]==sha(canonical_envelope_context(values)))
 return values

def verify_issuer_order(values,cert_raw,cert_values):
 context=canonical_envelope_context(values);context_digest=sha(context);certificate_digest=digest_certificate(cert_raw)
 need(cert_values[b"ISSUER_CONTEXT_SHA256"]==context_digest)
 need(values[b"ENVELOPE_CONTEXT_SHA256"]==context_digest and values[b"CERTIFICATE_DIGEST_SHA256"]==certificate_digest)
 for key in (b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256"):need(values[key]==cert_values[key])
 need(values[b"NOT_BEFORE_REALTIME_NS"]==cert_values[b"NOT_BEFORE_REALTIME_NS"] and values[b"NOT_AFTER_REALTIME_NS"]==cert_values[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 tbs=envelope_tbs(values,certificate_digest);signature_preimage=issuer_signature_preimage(cert_raw,tbs);signature_digest=sha(signature_preimage)
 receipt_preimage=issuer_receipt_preimage(context_digest,certificate_digest,signature_digest,values[b"SIGNATURE_ALGORITHM"],values[b"SIGNATURE_HEX"]);receipt_digest=sha(receipt_preimage)
 need(values[b"SIGNATURE_PREIMAGE_SHA256"]==signature_digest and values[b"ISSUER_RECEIPT_SHA256"]==receipt_digest)
 need(cert_values[b"ISSUER_CRYPTOGRAPHY_GATE_PASS"]==b"1" and cert_values[b"ISSUER_CRYPTOGRAPHY_GATE_ID"]!=b"0"*64)
 return context_digest,certificate_digest,receipt_digest

def length_frame(label,raw):
 need(type(label)is bytes and label and b"=" not in label and b"\n" not in label and type(raw)is bytes)
 return label+b"="+str(len(raw)).encode()+b"\n"+raw

def domain_frame(domain,label,raw):
 need(type(domain)is bytes and domain.endswith(b"\x00"))
 return domain+length_frame(label,raw)

def digest_certificate(cert_raw):
 return sha(domain_frame(CERTIFICATE_DOMAIN,b"CERTIFICATE_RAW",cert_raw))

def digest_final_envelope(envelope_raw):
 return sha(domain_frame(FINAL_ENVELOPE_DOMAIN,b"FINAL_ENVELOPE_RAW",envelope_raw))

def reservation_tbs(values):
 body=b"P27E001_ISSUER_RESERVATION_TBS_V15\n"
 for key in RESERVATION_TBS_KEYS:body+=key+b"="+values[key]+b"\n"
 return domain_frame(RESERVATION_TBS_DOMAIN,b"RESERVATION_TBS_RAW",body+b"RESERVATION_TBS_END=1\n")

def reservation_signature_preimage(tbs):
 payload=length_frame(b"RESERVATION_TBS",tbs)+b"RESERVATION_SIGNATURE_PREIMAGE_END=1\n"
 return domain_frame(RESERVATION_SIGNATURE_DOMAIN,b"RESERVATION_SIGNATURE_TBS_RAW",payload)

def reservation_receipt_preimage(tbs,signature_digest,algorithm,signature):
 payload=length_frame(b"RESERVATION_TBS",tbs)+b"SIGNATURE_PREIMAGE_SHA256="+signature_digest+b"\nSIGNATURE_ALGORITHM="+algorithm+b"\nSIGNATURE_HEX="+signature+b"\nRESERVATION_RECEIPT_END=1\n"
 return domain_frame(RESERVATION_RECEIPT_DOMAIN,b"RESERVATION_RECEIPT_TBS_RAW",payload)

def parse_reservation(raw):
 values=parse_fixed(raw,b"P27E001_ISSUER_RESERVATION_V15",RESERVATION_KEYS,b"RESERVATION_END=1")
 need(values[b"ISSUER_ID"]==b"P27_HOST_PREMISE_ISSUER_V15" and values[b"ONE_SHOT_RESERVED_BY_ISSUER"]==b"1" and values[b"ONE_SHOT_CONSUMED_BY_ISSUER"]==b"0")
 need(values[b"SIGNATURE_ALGORITHM"]==b"ED25519_EXTERNAL_GATE_V15")
 for key in (b"AUTHORIZATION_SERIAL",b"CERTIFICATE_DIGEST_SHA256",b"FINAL_ENVELOPE_DIGEST_SHA256",b"SIGNATURE_PREIMAGE_SHA256",b"RESERVATION_DIGEST_SHA256"):h64(values[key])
 sig=values[b"SIGNATURE_HEX"];need(len(sig)==128 and all(x in b"0123456789abcdef" for x in sig))
 before=udec(values[b"NOT_BEFORE_REALTIME_NS"]);after=udec(values[b"NOT_AFTER_REALTIME_NS"]);need(before<after)
 return values

def verify_reservation_order(values,cert_raw,envelope_raw,envelope_values):
 cert_digest=digest_certificate(cert_raw);envelope_digest=digest_final_envelope(envelope_raw)
 tbs=reservation_tbs(values);signature_preimage=reservation_signature_preimage(tbs);signature_digest=sha(signature_preimage)
 receipt_preimage=reservation_receipt_preimage(tbs,signature_digest,values[b"SIGNATURE_ALGORITHM"],values[b"SIGNATURE_HEX"]);receipt_digest=sha(receipt_preimage)
 need(values[b"CERTIFICATE_DIGEST_SHA256"]==cert_digest and values[b"FINAL_ENVELOPE_DIGEST_SHA256"]==envelope_digest)
 need(values[b"SIGNATURE_PREIMAGE_SHA256"]==signature_digest and values[b"RESERVATION_DIGEST_SHA256"]==receipt_digest)
 for key in (b"ISSUER_ID",b"ISSUER_KEY_ID",b"AUTHORIZATION_SERIAL",b"NOT_BEFORE_REALTIME_NS",b"NOT_AFTER_REALTIME_NS",b"ONE_SHOT_RESERVED_BY_ISSUER",b"ONE_SHOT_CONSUMED_BY_ISSUER"):need(values[key]==envelope_values[key])
 return receipt_digest

def session_auth(cert_raw,envelope_raw,reservation_raw):
 payload=length_frame(b"CERTIFICATE_RAW",cert_raw)+length_frame(b"FINAL_ENVELOPE_RAW",envelope_raw)+length_frame(b"RESERVATION_RAW",reservation_raw)
 return sha(domain_frame(AUTH_DOMAIN,b"AUTH_TBS_RAW",payload))

def contract(raw):
 ascii_file(raw);lines=raw[:-1].split(b"\n")
 need(lines and lines[0]==b"P27E001_PREMISE_CERTIFICATE_V15" and lines[-1]==b"CERTIFICATE_END=1")
 fixed=lines[1:1+len(CERT_KEYS)];need(len(fixed)==len(CERT_KEYS));values={}
 for key,line in zip(CERT_KEYS,fixed):
  parts=line.split(b"=",1);need(len(parts)==2 and parts[0]==key and key not in values);values[key]=parts[1]
 count=udec(values[b"DEP_COUNT"],1,256);dep_lines=lines[1+len(CERT_KEYS):-1];need(len(dep_lines)==count)
 roles={b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC",b"PYTHON_STDLIB",b"PYTHON_EXTENSION",b"NSS_DEPENDENCY",b"RUNTIME_DEPENDENCY"}
 deps=[]
 for index,line in enumerate(dep_lines):
  prefix=b"DEP[%04d]="%index;need(line.startswith(prefix));fields=line[len(prefix):].split(b",")
  need(len(fields)==10 and fields[0] in roles);path=even_hex(fields[1]);need(path.startswith(b"/") and b"\x00" not in path)
  ident=(udec(fields[2],1),udec(fields[3],1),octal(fields[4]),udec(fields[5],1),udec(fields[6]),udec(fields[7]),udec(fields[8]),h64(fields[9]))
  deps.append((fields[0],path,ident))
 need(len(set((x[0],x[1]) for x in deps))==len(deps))
 for role in (b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC"):need(sum(x[0]==role for x in deps)==1)
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V15",b"ARCH":b"x86_64",b"ABSOLUTE_LIFETIME_NS":b"360000000000",b"REALTIME_MONOTONIC_MAX_DRIFT_NS":b"1000000",b"E0366_SNAPSHOT_BYTES":b"2303269",b"E0366_SNAPSHOT_LF":b"23672",b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"HISTORICAL_SNAPSHOT_SEALED":b"1",b"V15_SHA256":V15_SHA,b"V8_SHA256":V8_SHA,b"ACTOR_ENTRY_CAPS":b"00000000000401c0",b"ACTOR_ENTRY_NNP":b"0",b"ACTOR_ENTRY_SECUREBITS":b"12",b"PAYLOAD_FINAL_CAPS":b"0000000000000000",b"PAYLOAD_FINAL_NNP":b"1",b"PAYLOAD_FINAL_SECUREBITS":b"15",b"ATTEMPT_BASE_MODE":b"40700",b"ATTEMPT_BASE_UID":b"0",b"ATTEMPT_BASE_GID":b"0",b"CGROUP2_FS_MAGIC":b"63677270",b"CGROUP_BASE_UID":b"0",b"CGROUP_BASE_GID":b"0",b"CGROUP_NO_EXTERNAL_MUTATOR":b"1",b"CGROUP_CHILD_MODE":b"40700",b"CGROUP_CHILD_UID":b"0",b"CGROUP_CHILD_GID":b"0",b"CGROUP_CHILD_TYPE_HEX":b"646f6d61696e0a",b"RUNTIME_ROOT_UID":b"0",b"RUNTIME_ROOT_GID":b"0",b"SAFE_BIND_MODE":b"40700",b"SAFE_BIND_UID":b"0",b"SAFE_BIND_GID":b"0",b"SAFE_BIND_NOEXEC":b"1",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT":b"1",b"KEEPER_BYTES":b"4216",b"KEEPER_LF":b"128",b"KEEPER_SHA256":b"e3bf14ddde012be70a0ec40ac9373c055d2fd79d3ea30aa5e64450174f057716",b"LAUNCHER_BYTES":b"4218",b"LAUNCHER_LF":b"128",b"LAUNCHER_SHA256":b"e9d5eb3544dfddd7251279294e113f053165c2d446dd4517fbcdc6927a8618d5",b"MARKER_BYTES":b"75094",b"MARKER_LF":b"1479",b"MARKER_SHA256":b"b06ceed041004279e9df73cc9cc3c2d73ec07d8f71a9345f451a32e93b7a955d",b"CHILD_BYTES":b"19746",b"CHILD_LF":b"452",b"CHILD_SHA256":b"1d20310b965ff9df9351cbc3ca07aebb15e8cbacf74a8058782c085fde0780bf",b"PYTHON_IMAGE_SHA256":PY_SHA,b"PYTHON_IMAGE_BYTES":b"30626264",b"PYTHON_IMAGE_UID":b"0",b"PYTHON_IMAGE_GID":b"0",b"LIBC_UID":b"0",b"LIBC_GID":b"0",b"PRECONSUMPTION_CAP_NS":b"10000000000",b"CONSUMPTION_PROGRESS_NS":b"250000000",b"ATTEMPT_DIRFD_PROGRESS_NS":b"100000000",b"STAGING_CAP_NS":b"10000000000",b"RELEASE_PROGRESS_NS":b"1000000000",b"RELEASE_RECORD_ABSOLUTE_OFFSET_NS":b"800000000",b"RELEASE_REPLY_ABSOLUTE_OFFSET_NS":b"900000000",b"SIGCONT_CALL_RETURN_NS":b"5000000",b"DURABLE_RECORD_PROGRESS_NS":b"100000000",b"WATCHDOG_ARM_PROGRESS_NS":b"1000000000",b"WATCHDOG_ACK_PROGRESS_NS":b"500000000",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT":b"1",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY":b"1",b"CGROUP_KILL_WRITE_RETURN_NS":b"5000000",b"CGROUP_KILL_TO_EMPTY_NS":b"2000000000",b"FINAL_REPORT_PROGRESS_NS":b"1000000000",b"FINAL_PASS_COMMIT_PROGRESS_NS":b"100000000",b"FINAL_PASS_MARGIN_NS":b"10000000",b"TERMINAL_HANDSHAKE_PROGRESS_NS":b"500000000",b"A_RECEIPT_PROGRESS_NS":b"100000000",b"B_CLOSURE_PROGRESS_NS":b"500000000",b"TERMINAL_CANDIDATE_RECORD_NS":b"100000000",b"TERMINAL_NOTICE_PROGRESS_NS":b"100000000",b"TERMINAL_SEEN_RECORD_NS":b"100000000",b"TERMINAL_ACK_RECEIPT_RECORD_NS":b"100000000",b"TERMINAL_RECONCILIATION_RECORD_NS":b"100000000",b"TERMINAL_OWNER_CLOSURE_RECORD_NS":b"100000000",b"TERMINAL_CLOSURE_PACKET_NS":b"100000000",b"TERMINAL_B_EXIT_NS":b"100000000",b"FAILURE_OVERALL_PROGRESS_NS":b"5210000000",b"FAILURE_CLEANUP_EFFECT_PROGRESS_NS":b"2600000000",b"FAILURE_TAIL_RESERVE_NS":b"2610000000",b"REFUSAL_RECORD_PROGRESS_NS":b"20000000",b"REFUSAL_ACK_PROGRESS_NS":b"20000000",b"REFUSAL_RECEIPT_WAIT_PROGRESS_NS":b"30000000",b"REFUSAL_FINALITY_COMMIT_PROGRESS_NS":b"10000000",b"REFUSAL_FINALITY_DEADLINE_PROGRESS_NS":b"80000000",b"REFUSAL_OFFER_BUILD_PROGRESS_NS":b"10000000",b"REFUSAL_OFFER_SEND_PROGRESS_NS":b"20000000",b"REFUSAL_ACCEPTANCE_RECV_PROGRESS_NS":b"30000000",b"REFUSAL_ACCEPTANCE_VERIFY_PROGRESS_NS":b"20000000",b"REFUSAL_ACCEPTANCE_COMMIT_PROGRESS_NS":b"10000000",b"REFUSAL_ACTOR_CLOSURE_PROGRESS_NS":b"20000000",b"REFUSAL_CAPABILITY_CLOSE_PROGRESS_NS":b"10000000",b"REFUSAL_OWNER_RELEASE_PROGRESS_NS":b"10000000",b"REFUSAL_CLOSURE_TAIL_NS":b"130000000",b"REFUSAL_CLOSURE_DEADLINE_PROGRESS_NS":b"210000000",b"FINAL_TERMINAL_TOTAL_NS":b"2510000000",b"ENTRY_MIN_REMAINING_NS":b"295482000000",b"CONSUMPTION_MIN_REMAINING_NS":b"285482000000",b"PRE_STAGE_MIN_REMAINING_NS":b"285232000000",b"POST_STAGE_MIN_REMAINING_NS":b"275232000000",b"POST_CONTAIN_MIN_REMAINING_NS":b"274732000000",b"ACTOR_RELEASE_DISABLE_PROGRESS_NS":b"500000000",b"EXTERNAL_OWNER_UID":b"0",b"EXTERNAL_OWNER_GID":b"0",b"CLONE3_CPYTHON_GATE_PASS":b"1",b"DELETED_CGROUP_FD_GATE_PASS":b"1",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_PASS":b"1",b"EXTERNAL_SURVIVAL_GATE_PASS":b"1",b"OUTER_RECONCILER_GATE_PASS":b"1",b"ISSUER_CRYPTOGRAPHY_GATE_PASS":b"1"}
 for key,value in exact.items():need(values[key]==value)
 for key in (b"ISSUER_CONTEXT_SHA256",b"BOOT_ID_SHA256",b"PLATFORM_ID_SHA256",b"PLAN_SHA256",b"RUNNER_SHA256",b"RECOVERY_SHA256",b"ATTEMPT_BASE_MOUNTINFO_SHA256",b"CGROUP2_MOUNTINFO_SHA256",b"RUNTIME_ROOT_MOUNTINFO_SHA256",b"SAFE_BIND_MOUNTINFO_SHA256",b"KEEPER_SHA256",b"LAUNCHER_SHA256",b"MARKER_SHA256",b"CHILD_SHA256",b"LIBC_SHA256",b"DEFAULTS_SHA256",b"EXTERNAL_TRANSFER_MANIFEST_SHA256",b"CLONE3_CPYTHON_GATE_ID",b"DELETED_CGROUP_FD_GATE_ID",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_ID",b"EXTERNAL_SURVIVAL_GATE_ID",b"OUTER_RECONCILER_GATE_ID",b"ISSUER_CRYPTOGRAPHY_GATE_ID"):h64(values[key])
 need(values[b"CLONE3_CPYTHON_GATE_ID"]!=b"0"*64 and values[b"DELETED_CGROUP_FD_GATE_ID"]!=b"0"*64 and values[b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_ID"]!=b"0"*64 and values[b"EXTERNAL_SURVIVAL_GATE_ID"]!=b"0"*64 and values[b"OUTER_RECONCILER_GATE_ID"]!=b"0"*64 and values[b"ISSUER_CRYPTOGRAPHY_GATE_ID"]!=b"0"*64)
 for key in (b"NO_ASYNC_TRANSFER",b"NO_SIGNAL_DELIVERY",b"NO_TIMER_DELIVERY",b"NO_TRACE_PROFILE_AUDIT_HOOK",b"NO_CONCURRENT_MUTATOR",b"DEPENDENCY_CLOSURE_COMPLETE",b"RUNTIME_ROOT_WORKSPACE_ABSENT",b"BUILD_EVIDENCE_ROOT_UNREACHABLE",b"CLOSE_RANGE_COMPLETE",b"FSYNC_DURABILITY_PREMISE"):need(values[key]==b"1")
 for key in (b"KERNEL_RELEASE_HEX",b"E0366_SNAPSHOT_TERMINAL_HEX",b"ATTEMPT_BASE_FSTYPE_HEX",b"CGROUP_BASE_TYPE_HEX",b"CGROUP_BASE_CONTROLLERS_HEX",b"CGROUP_BASE_SUBTREE_CONTROL_HEX",b"CGROUP_CHILD_TYPE_HEX",b"CGROUP_CHILD_CONTROLLERS_HEX",b"CGROUP_CHILD_SUBTREE_CONTROL_HEX",b"RUNTIME_ROOT_FSTYPE_HEX",b"SAFE_BIND_FSTYPE_HEX",b"LIBC_PATH_HEX",b"LIBC_CONFSTR_HEX"):even_hex(values[key])
 for key in (b"ATTEMPT_BASE_MODE",b"CGROUP_BASE_MODE",b"CGROUP_CHILD_MODE",b"RUNTIME_ROOT_MODE",b"SAFE_BIND_MODE",b"PYTHON_IMAGE_MODE",b"LIBC_MODE"):octal(values[key])
 for key in (b"NOT_BEFORE_REALTIME_NS",b"ABSOLUTE_EXPIRY_REALTIME_NS",b"REALTIME_BIND_NS",b"MONOTONIC_BIND_NS",b"ATTEMPT_BASE_DEV",b"ATTEMPT_BASE_INO",b"ATTEMPT_BASE_NLINK",b"ATTEMPT_BASE_MOUNT_ID",b"CGROUP2_MOUNT_ID",b"CGROUP_BASE_DEV",b"CGROUP_BASE_INO",b"CGROUP_BASE_NLINK",b"RUNTIME_ROOT_DEV",b"RUNTIME_ROOT_INO",b"RUNTIME_ROOT_NLINK",b"RUNTIME_ROOT_MOUNT_ID",b"SAFE_BIND_DEV",b"SAFE_BIND_INO",b"SAFE_BIND_NLINK",b"SAFE_BIND_MOUNT_ID",b"KEEPER_BYTES",b"KEEPER_LF",b"LAUNCHER_BYTES",b"LAUNCHER_LF",b"MARKER_BYTES",b"MARKER_LF",b"CHILD_BYTES",b"CHILD_LF",b"PYTHON_IMAGE_DEV",b"PYTHON_IMAGE_INO",b"PYTHON_IMAGE_NLINK",b"PYTHON_IMAGE_UID",b"PYTHON_IMAGE_GID",b"LIBC_DEV",b"LIBC_INO",b"LIBC_NLINK",b"LIBC_BYTES",b"VALID_SIGNAL_COUNT",b"DEFAULT_SIGNAL_COUNT",b"EXTERNAL_OWNER_PID",b"EXTERNAL_OWNER_STARTTIME",b"EXTERNAL_OWNER_UID",b"EXTERNAL_OWNER_GID",b"EXTERNAL_TRANSFER_MANIFEST_BYTES"):udec(values[key])
 by_role={role:next(x for x in deps if x[0]==role) for role in (b"PYTHON_LINK",b"PYTHON_IMAGE",b"ENV_EXEC",b"BASH_EXEC",b"DYNAMIC_LOADER",b"LIBC")}
 need(by_role[b"PYTHON_LINK"][1]==PYTHON and by_role[b"PYTHON_IMAGE"][1]==PYIMAGE and by_role[b"ENV_EXEC"][1]==b"/usr/bin/env" and by_role[b"BASH_EXEC"][1]==b"/usr/bin/bash")
 libc=(udec(values[b"LIBC_DEV"],1),udec(values[b"LIBC_INO"],1),octal(values[b"LIBC_MODE"]),udec(values[b"LIBC_NLINK"],1),0,0,udec(values[b"LIBC_BYTES"],1),values[b"LIBC_SHA256"])
 python_image=(udec(values[b"PYTHON_IMAGE_DEV"],1),udec(values[b"PYTHON_IMAGE_INO"],1),octal(values[b"PYTHON_IMAGE_MODE"]),udec(values[b"PYTHON_IMAGE_NLINK"],1),udec(values[b"PYTHON_IMAGE_UID"]),udec(values[b"PYTHON_IMAGE_GID"]),udec(values[b"PYTHON_IMAGE_BYTES"],1),values[b"PYTHON_IMAGE_SHA256"])
 need(by_role[b"PYTHON_IMAGE"][1]==PYIMAGE and by_role[b"PYTHON_IMAGE"][2]==python_image)
 need(by_role[b"LIBC"][1]==even_hex(values[b"LIBC_PATH_HEX"]) and by_role[b"LIBC"][2]==libc)
 return values,tuple(deps)

def checkpoint(cert,needed=0,deadline=None):
 m0=time.monotonic_ns();real=time.time_ns();m1=time.monotonic_ns()
 before=udec(cert[b"NOT_BEFORE_REALTIME_NS"]);expiry=udec(cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 if not (before<=real<expiry and expiry-real>=needed):raise CertificateExpired("certificate-life")
 base_r=udec(cert[b"REALTIME_BIND_NS"]);base_m=udec(cert[b"MONOTONIC_BIND_NS"])
 if not base_m<=m0<=m1:raise FaultSet({b"CLOCK_DRIFT"})
 drift=udec(cert[b"REALTIME_MONOTONIC_MAX_DRIFT_NS"]);low=base_r+(m0-base_m);high=base_r+(m1-base_m)
 if not low-drift<=real<=high+drift:raise FaultSet({b"CLOCK_DRIFT"})
 if deadline is not None and m1>deadline:raise FaultSet({b"DEADLINE_EXPIRED"})
 return real,m1


def horizon_needed(deadline,tail):
 return tail+max(0,deadline-time.monotonic_ns())

def exact_schedule(origin,overall,spec):
 need(type(origin)is int and type(overall)is int and origin>0 and overall==origin+sum(cap for name,cap in spec))
 cursor=origin;result={}
 for name,cap in spec:
  need(name not in result and cap>0);cursor+=cap;result[name]=cursor
 need(cursor==overall);return result

def schedule_raw(schedule,spec):
 need(tuple(schedule)==tuple(name for name,cap in spec))
 return b";".join(name+b"="+str(schedule[name]).encode() for name,cap in spec)

def schedule_hex(schedule,spec):
 return schedule_raw(schedule,spec).hex().encode("ascii")

def check_schedule_hex(raw,origin,overall,spec):
 need(type(raw)is bytes and raw and len(raw)%2==0 and all(x in b"0123456789abcdef" for x in raw))
 expected=exact_schedule(origin,overall,spec)
 need(bytes.fromhex(raw.decode("ascii"))==schedule_raw(expected,spec));return expected

def phase_boundary(context,schedule,spec,name,overall,require_live=True):
 origin=overall-sum(cap for key,cap in spec);need(name in schedule and schedule==exact_schedule(origin,overall,spec))
 names=tuple(key for key,cap in spec);index=names.index(name);start=origin if index==0 else schedule[names[index-1]];deadline=schedule[name];reserve_after=overall-deadline
 while time.monotonic_ns()<start:
  owner_poll(context.get(b"actor_control"),context,start)
  if require_live and context.get(b"actor_state")==b"PIDFD_ACTOR_LOST":raise PidfdActorLost("phase-start")
  if require_live and context.get(b"control_state")==b"CONTROL_LOST":raise ControlLost("phase-start")
 need(start<=time.monotonic_ns()<=deadline);record_boundary(context,deadline,require_live,reserve_after)
 need(time.monotonic_ns()<=deadline);return deadline

def certificate_mono_expiry(cert):
 return udec(cert[b"MONOTONIC_BIND_NS"],1)+udec(cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"])-udec(cert[b"REALTIME_BIND_NS"])-udec(cert[b"REALTIME_MONOTONIC_MAX_DRIFT_NS"])

def cert_live(cert,needed=0):
 return checkpoint(cert,needed)

def cap_status():
 number=-1
 try:
  number=acquire_lifecycle_open(ACTIVE_LIFECYCLE_CONTEXT,b"cap_status_fd",b"PROC_STATUS_OBSERVATION_FD",b"/proc/self/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(number,65536),65536)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))
 values={}
 for line in raw.splitlines():
  for key in (b"CapInh",b"CapPrm",b"CapEff",b"CapBnd",b"CapAmb",b"NoNewPrivs"):
   if line.startswith(key+b":"):need(key not in values);values[key]=line.split(b":",1)[1].strip()
 need(set(values)=={b"CapInh",b"CapPrm",b"CapEff",b"CapBnd",b"CapAmb",b"NoNewPrivs"});return values

def limit_vector():
 inf=resource.RLIM_INFINITY
 return ((resource.RLIMIT_AS,(inf,inf)),(resource.RLIMIT_CORE,(0,0)),(resource.RLIMIT_CPU,(inf,inf)),(resource.RLIMIT_DATA,(inf,inf)),(resource.RLIMIT_FSIZE,(inf,inf)),(resource.RLIMIT_MEMLOCK,(8388608,8388608)),(resource.RLIMIT_MSGQUEUE,(819200,819200)),(resource.RLIMIT_NICE,(0,0)),(resource.RLIMIT_NOFILE,(1048576,1048576)),(resource.RLIMIT_NPROC,(1048576,1048576)),(resource.RLIMIT_RSS,(inf,inf)),(resource.RLIMIT_RTPRIO,(0,0)),(resource.RLIMIT_RTTIME,(inf,inf)),(resource.RLIMIT_SIGPENDING,(515199,515199)),(resource.RLIMIT_STACK,(8388608,inf)))

def final_context(safe_dev,safe_ino):
 values=cap_status();zero=b"0000000000000000"
 need(os.getresuid()==(0,0,0) and os.getresgid()==(0,0,0) and os.getgroups()==[])
 need(all(values[x]==zero for x in (b"CapInh",b"CapPrm",b"CapEff",b"CapBnd",b"CapAmb")) and values[b"NoNewPrivs"]==b"1")
 libc=ctypes.CDLL(None,use_errno=True);need(libc.prctl(27,0,0,0,0)==15)
 held=os.stat(b".",follow_symlinks=False);need((held.st_dev,held.st_ino,held.st_uid,held.st_gid,stat.S_IMODE(held.st_mode))==(safe_dev,safe_ino,0,0,0o700))
 need(os.umask(0o077)==0o077 and all(signal.getitimer(x)==(0.0,0.0) for x in (signal.ITIMER_REAL,signal.ITIMER_VIRTUAL,signal.ITIMER_PROF)))
 need(signal.pthread_sigmask(signal.SIG_BLOCK,set())==set() and all(signal.getsignal(x)==signal.SIG_DFL for x in signal.valid_signals() if x not in (signal.SIGKILL,signal.SIGSTOP)))
 for key,value in limit_vector():
  if key==resource.RLIMIT_NOFILE:
   need(value==WATCHDOG_ENTRY_LIMIT_VECTOR_V19)
   need(WATCHDOG_ENTRY_LIMIT_CERTIFIED_V19 and WATCHDOG_CURRENT_LOW_LIMIT_VECTOR_V19==(256,value[1]))
   need(resource.getrlimit(key)==WATCHDOG_CURRENT_LOW_LIMIT_VECTOR_V19)
  else:need(resource.getrlimit(key)==value)
 need(sys.gettrace() is None and sys.getprofile() is None and os.environb==ENV)

def scrub_exact(expected):
 seen=set()
 for item in os.listdir(b"/proc/self/fd"):
  if item.isdigit():
   number=int(item)
   try:os.fstat(number)
   except OSError as error:need(error.errno==errno.EBADF);continue
   seen.add(number)
 need(seen==expected)

def pidfd_pid(number):
 link=os.readlink(b"/proc/self/fd/"+str(number).encode());need(link==b"anon_inode:[pidfd]");info=-1
 try:
  info=acquire_lifecycle_open(ACTIVE_LIFECYCLE_CONTEXT,b"mount_fdinfo_fd",b"MOUNT_FDINFO_OBSERVATION_FD",b"/proc/self/fdinfo/"+str(number).encode(),os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(info,4096),4096)
 finally:close_numbers(tuple(x for x in (info,) if x>=0))
 values=[x[5:] for x in raw.splitlines() if x.startswith(b"Pid:\t")];need(len(values)==1)
 return udec(values[0],1)

def proc_starttime(pid):
 number=-1
 try:
  number=acquire_lifecycle_open(ACTIVE_LIFECYCLE_CONTEXT,b"proc_starttime_fd",b"PROC_STARTTIME_OBSERVATION_FD",b"/proc/"+str(pid).encode()+b"/stat",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(number,4096),4096)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))
 cut=raw.rfind(b") ");need(cut>0);fields=raw[cut+2:].strip().split();need(len(fields)>=20);return udec(fields[19],1)

def closed(number):
 try:os.fstat(number)
 except OSError as error:need(error.errno==errno.EBADF);return
 need(False)

def whole_snapshot():
 seals(9);fd_access(9,os.O_RDWR);raw=read_all(9,SNAPSHOT_EXPECT[0]);held=os.fstat(9)
 need(stat.S_ISREG(held.st_mode) and held.st_nlink==0 and held.st_uid==held.st_gid==0)
 need((held.st_size,raw.count(b"\n"),sha(raw))==SNAPSHOT_EXPECT and raw.endswith(b"\n"))
 lines=raw[:-1].split(b"\n");need(lines[-1]==SNAPSHOT_TERMINAL and lines.count(SNAPSHOT_TERMINAL)==1)
 return raw

class StatFS(ctypes.Structure):
 _fields_=(("f_type",ctypes.c_long),("f_bsize",ctypes.c_long),("rest",ctypes.c_byte*240))

def statfs_magic(number):
 cell=StatFS();libc=ctypes.CDLL(None,use_errno=True);need(libc.fstatfs(number,ctypes.byref(cell))==0)
 return cell.f_type&0xffffffff

def mount_binding(number):
 info=-1
 try:
  info=acquire_lifecycle_open(ACTIVE_LIFECYCLE_CONTEXT,b"mount_fdinfo_fd",b"MOUNT_FDINFO_OBSERVATION_FD",b"/proc/self/fdinfo/"+str(number).encode(),os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(info,4096),4096)
 finally:close_numbers(tuple(x for x in (info,) if x>=0))
 mids=[x[7:] for x in raw.splitlines() if x.startswith(b"mnt_id:\t")];need(len(mids)==1);mid=udec(mids[0],1);table=-1
 try:
  table=acquire_lifecycle_open(ACTIVE_LIFECYCLE_CONTEXT,b"mount_table_fd",b"MOUNT_TABLE_OBSERVATION_FD",b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);rows=ascii_file(read_all(table,1048576),1048576)
 finally:close_numbers(tuple(x for x in (table,) if x>=0))
 matches=[line+b"\n" for line in rows.splitlines() if line.split(b" ",1)[0]==str(mid).encode()]
 need(len(matches)==1);return mid,matches[0]

def verify_platform(cert):
 boot=-1
 try:
  boot=acquire_lifecycle_open(ACTIVE_LIFECYCLE_CONTEXT,b"boot_id_fd",b"BOOT_ID_OBSERVATION_FD",b"/proc/sys/kernel/random/boot_id",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);boot_raw=read_all(boot,128)
 finally:close_numbers(tuple(x for x in (boot,) if x>=0))
 need(boot_raw.endswith(b"\n") and sha(boot_raw)==cert[b"BOOT_ID_SHA256"])
 u=os.uname();encoded=tuple(x.encode("ascii","strict") for x in (u.sysname,u.release,u.version,u.machine))
 raw=b"SYSNAME="+encoded[0]+b"\nRELEASE="+encoded[1]+b"\nVERSION="+encoded[2]+b"\nMACHINE="+encoded[3]+b"\n"
 need(encoded[3]==b"x86_64" and encoded[1].hex().encode()==cert[b"KERNEL_RELEASE_HEX"] and sha(raw)==cert[b"PLATFORM_ID_SHA256"])

def mount_semantics(line,fstype,required,forbidden):
 pieces=line[:-1].split(b" - ");need(len(pieces)==2)
 left=pieces[0].split(b" ");right=pieces[1].split(b" ");need(len(left)>=6 and len(right)>=3 and right[0]==fstype)
 options=set(left[5].split(b","))|set(right[2].split(b","));need(required<=options and not (forbidden&options))

def mount_graph(cert):
 number=-1
 try:
  number=acquire_lifecycle_open(ACTIVE_LIFECYCLE_CONTEXT,b"mount_graph_fd",b"MOUNT_GRAPH_OBSERVATION_FD",b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(number,1048576),1048576)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))
 rows={}
 for line in raw.splitlines():
  left,right=line.split(b" - ",1);fields=left.split(b" ");need(len(fields)>=6)
  mid=udec(fields[0],1);parent=udec(fields[1],1);options=set(fields[5].split(b","));need(mid not in rows);rows[mid]=(parent,options)
 runtime=udec(cert[b"RUNTIME_ROOT_MOUNT_ID"],1);safe=udec(cert[b"SAFE_BIND_MOUNT_ID"],1);need(runtime in rows and safe in rows and runtime!=safe)
 def descends(mid,ancestor):
  seen=set()
  while mid in rows and mid not in seen:
   if mid==ancestor:return True
   seen.add(mid);mid=rows[mid][0]
  return False
 writable=[mid for mid,(parent,options) in rows.items() if mid!=runtime and descends(mid,runtime) and b"rw" in options]
 need(writable==[safe] and cert[b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT"]==b"1")

def base_check(number,cert,prefix):
 held=os.fstat(number);need(stat.S_ISDIR(held.st_mode));fd_access(number,os.O_RDONLY)
 expected=(udec(cert[prefix+b"_DEV"],1),udec(cert[prefix+b"_INO"],1),octal(cert[prefix+b"_MODE"]),udec(cert[prefix+b"_NLINK"],1),udec(cert[prefix+b"_UID"]),udec(cert[prefix+b"_GID"]))
 need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==expected)
 return held

def verify_dependency(entry):
 role,path,identity=entry;parts=path.split(b"/")[1:];need(parts and all(x not in (b"",b".",b"..") for x in parts))
 rootfd=current=number=following=-1
 try:
  rootfd=acquire_lifecycle_open(ACTIVE_LIFECYCLE_CONTEXT,b"dependency_root_fd",b"DEPENDENCY_ROOT_DIRFD",b"/",O_DIR);current=acquire_lifecycle_dup(ACTIVE_LIFECYCLE_CONTEXT,b"dependency_current_fd",b"DEPENDENCY_CURRENT_DIRFD",rootfd)
  for part in parts[:-1]:
   following=acquire_lifecycle_open(ACTIVE_LIFECYCLE_CONTEXT,b"dependency_following_fd",b"DEPENDENCY_FOLLOWING_DIRFD",part,O_DIR,dir_fd=current);close_numbers((current,));promote_lifecycle_fd(ACTIVE_LIFECYCLE_CONTEXT,b"dependency_following_fd",b"dependency_current_fd",b"DEPENDENCY_CURRENT_DIRFD",False);current=following;following=-1
  if role==b"PYTHON_LINK":
   held=os.stat(parts[-1],dir_fd=current,follow_symlinks=False);need(stat.S_ISLNK(held.st_mode))
   target=os.readlink(parts[-1],dir_fd=current);size=len(target);digest=sha(target)
  else:
   number=acquire_lifecycle_open(ACTIVE_LIFECYCLE_CONTEXT,b"dependency_leaf_fd",b"DEPENDENCY_LEAF_VERIFY_FD",parts[-1],os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=current)
   held=os.fstat(number);body=read_all(number,identity[6]);size=len(body);digest=sha(body)
  need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,size,digest)==identity)
 finally:
  close_numbers(tuple(x for x in (number,following,current,rootfd) if x>=0))

def write_all(number,raw,context,deadline,require_live,needed):
 offset=0
 while offset<len(raw):
  record_boundary(context,deadline,require_live,needed)
  try:count=os.write(number,raw[offset:])
  except InterruptedError:
   record_boundary(context,deadline,require_live,needed);continue
  record_boundary(context,deadline,require_live,needed);need(count>0);offset+=count

def post_deadline(deadline):
 if time.monotonic_ns()>deadline:raise FaultSet({b"DEADLINE_EXPIRED"})

def boundary_liveness(context):
 poller=select.poll();register_lifecycle_poller(context,poller,b"actor_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 control=context.get(b"actor_control")
 if control is not None and context.get(b"control_state")==b"CONNECTED":poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR)
 amask=cmask=0
 for number,event in poller.poll(0):
  if number==4:amask|=event
  elif control is not None and number==control.fileno():cmask|=event
 if pidfd_ready_event(amask):
  mark_actor_pidfd_lost(context);raise PidfdActorLost("certified-boundary")
 if cmask&(select.POLLHUP|select.POLLERR) and not cmask&select.POLLIN:
  context[b"control_state"]=b"CONTROL_LOST";raise ControlLost("certified-boundary")

def record_boundary(context,deadline,require_live,needed):
 if require_live:boundary_liveness(context)
 post_deadline(deadline)
 try:checkpoint(CERT,needed,deadline)
 except CertificateExpired:
  context[b"faults"].add(b"CERTIFICATE_EXPIRED")
  if require_live:raise
 except FaultSet as error:
  context[b"faults"].update(error.faults)
  if require_live:raise
 except StaticReject:
  context[b"faults"].add(b"CERTIFICATE_INVALID")
  if require_live:raise
 if require_live:boundary_liveness(context)

RECORD_DELTA_KINDS=(b"INTENT",b"RELEASE",b"VALIDATED",b"ACK_INTENT",b"COMMITTED",b"COMMITTED_SEEN",b"KILL_TICKET",b"RETAINED",b"RECOVERY",b"FAILURE_REPORT",b"TERMINAL_CANDIDATE",b"TERMINAL_SEEN",b"SUCCESS_REPORT",b"PASS_COMMIT",b"ACK_RECEIPT",b"RECONCILIATION",b"OWNER_CLOSURE")

def semantic_delta_bytes(delta):
 need(type(delta)is tuple and delta and delta[0] in RECORD_DELTA_KINDS and all(type(item)is bytes for item in delta))
 return b"P27E001_RECORD_SEMANTIC_DELTA_V15\n"+b"".join(b"ITEM="+str(len(item)).encode()+b":"+item+b"\n" for item in delta)+b"DELTA_END=1\n"

def apply_record_delta(context,delta,seq,predecessor,name,digest):
 semantic_delta_bytes(delta);kind=delta[0];before=b"0"*64 if predecessor==b"NONE" else predecessor
 need(context[b"chain_sha"] in (before,digest))
 if kind==b"INTENT":
  need(len(delta)==1 and seq==1 and predecessor==b"NONE" and name==b"intent.v5")
  need(context[b"intent_count"] in (0,1) and context[b"commit_count"] in (0,1))
  context[b"intent_durable"]=True;context[b"intent_count"]=1;context[b"commit_count"]=1
  context[b"local_fd_state"]=b"PUBLISHED";context[b"attempt_state"]=b"PUBLISHED";context[b"consumption_state"]=b"INTENT_DURABLE_DIRFD_PUBLISHED"
 elif kind==b"RELEASE":
  need(len(delta)==2 and delta[1] in PROBES);context[b"release_sha"]=digest
 elif kind==b"VALIDATED":
  need(len(delta)==2+len(CANDIDATE_KEYS) and delta[1] in PROBES)
  values=dict(zip(CANDIDATE_KEYS,delta[2:]));need(values[b"probe"]==delta[1]);context[b"validated_sha"]=digest;context[b"validated_values"]=values
 elif kind==b"ACK_INTENT":need(len(delta)==2 and delta[1] in PROBES)
 elif kind==b"COMMITTED":
  need(len(delta)==6);ordinal=udec(delta[1],0,14);probe=delta[2];packet_sha=h64(delta[3]);final_count=udec(delta[4],1,15);message_seq=udec(delta[5],1)
  need(PROBES[ordinal]==probe and final_count==ordinal+1 and context[b"direct_reaps"] in (final_count-1,final_count))
  context[b"committed"][ordinal]=True;context[b"direct_reaps"]=final_count;context[b"direct_reap_state"]=b"COMPLETE"
  context[b"last_committed_record_sha"]=digest;context[b"last_committed_packet_sha"]=packet_sha;context[b"last_committed_packet_message_seq"]=message_seq
  if context[b"committed_send_state"]!=b"COMMITTED_SENT":context[b"committed_send_state"]=b"COMMITTED_SEND_EFFECT_UNKNOWN"
 elif kind==b"COMMITTED_SEEN":
  need(len(delta)==5);ordinal=udec(delta[1],0,14);need(PROBES[ordinal]==delta[2] and h64(delta[3])==context[b"last_committed_packet_sha"] and udec(delta[4],1,15)==ordinal+1)
  need(context[b"committed"][ordinal] and context[b"direct_reaps"]==ordinal+1);context[b"committed_seen_sha"]=digest;context[b"committed_send_state"]=b"COMMITTED_SENT"
 elif kind==b"KILL_TICKET":
  need(len(delta)==1);context[b"kill_ticket_state"]=DURABLE_VERIFIED;context[b"kill_state"]=b"CALL_RESERVED"
 elif kind==b"RETAINED":need(len(delta)==1);context[b"retained_state"]=DURABLE_VERIFIED
 elif kind==b"RECOVERY":need(len(delta)==1);context[b"recovery_state"]=DURABLE_VERIFIED;context[b"recovery_sha"]=digest
 else:
  need(len(delta)>=2);deadline=udec(delta[-1],1);record=(seq,name,predecessor,digest,deadline)
  existing=[item for item in context[b"chain_records"] if item[0]==seq]
  need(not existing or existing==[record])
  if not existing:context[b"chain_records"].append(record)
  if kind==b"FAILURE_REPORT":need(len(delta)==2);context[b"report_state"]=DURABLE_VERIFIED;context[b"report_sha"]=digest;context[b"outcome_durable"]=True
  elif kind==b"TERMINAL_CANDIDATE":need(len(delta)==2);context[b"candidate_sha"]=digest
  elif kind==b"TERMINAL_SEEN":need(len(delta)==2);context[b"terminal_seen_sha"]=digest
  elif kind==b"SUCCESS_REPORT":need(len(delta)==2);context[b"report_state"]=DURABLE_VERIFIED;context[b"report_sha"]=digest
  elif kind==b"PASS_COMMIT":need(len(delta)==3);context[b"pass_committed"]=True;context[b"outcome_durable"]=True;context[b"pass_sha"]=digest;context[b"reconciliation_token"]=h64(delta[1])
  elif kind==b"ACK_RECEIPT":need(len(delta)==2);context[b"ack_receipt_sha"]=digest
  elif kind==b"RECONCILIATION":need(len(delta)==2);context[b"reconciliation_sha"]=digest
  elif kind==b"OWNER_CLOSURE":need(len(delta)==2);context[b"owner_closure_sha"]=digest
  else:need(False)
 context[b"chain_sha"]=digest;context[b"last_applied_record_delta_sha"]=sha(semantic_delta_bytes(delta))

def activate_record_reservation_after_carrier(context,name,raw,digest,semantic_delta):
 need(context.get(b"record_pending") is None and not context.get(b"record_sequence_frozen") and context.get(b"pending_expected_raw_fd",-1)>=0)
 draft=context.get(b"record_draft");need(draft is not None)
 seq,predecessor,pending_name,pending_digest=draft;need(pending_name in (None,name) and pending_digest in (None,digest))
 need(raw.count(b"RECORD_SEQ="+str(seq).encode()+b"\n")==1 and raw.count(b"PREDECESSOR_SHA256="+predecessor+b"\n")==1)
 semantic_delta_bytes(semantic_delta)
 need(sealed_carrier(context[b"pending_expected_raw_fd"],len(raw))==raw);os.lseek(context[b"pending_expected_raw_fd"],0,os.SEEK_SET)
 context[b"record_pending"]=(seq,predecessor,name,digest,semantic_delta);context[b"record_draft"]=None;context[b"record_sequence_frozen"]=True
 context[b"uncertain_record"]=(seq,predecessor,name,digest,semantic_delta);context[b"carrier_pre_effect_state"]=b"CARRIER_VERIFIED_RESERVATION_FROZEN"

def prepare_first_intent_draft(context,name,raw):
 need(name==b"intent.v5" and context[b"record_seq"]==0 and context[b"chain_sha"]==b"0"*64)
 need(context.get(b"record_pending") is None and context.get(b"record_draft") is None and not context.get(b"record_sequence_frozen"))
 digest=sha(raw);need(raw.count(b"RECORD_SEQ=1\n")==1 and raw.count(b"PREDECESSOR_SHA256=NONE\n")==1)
 context[b"record_draft"]=(1,b"NONE",name,digest);context[b"carrier_pre_effect_state"]=b"DRAFT_NON_PENDING_PRE_EFFECT";return digest

def freeze_record_reservation(context,name,digest):
 pending=context.get(b"record_pending")
 if pending is not None:
  seq,predecessor,pending_name,pending_digest,semantic_delta=pending;need((pending_name,pending_digest)==(name,digest));semantic_delta_bytes(semantic_delta)
  context[b"record_sequence_frozen"]=True;context[b"uncertain_record"]=pending

def commit_record_reservation(context,name,digest):
 pending=context.get(b"record_pending")
 if pending is None:return
 seq,predecessor,pending_name,pending_digest,semantic_delta=pending;need((pending_name,pending_digest)==(name,digest) and seq==context[b"record_seq"]+1)
 apply_record_delta(context,semantic_delta,seq,predecessor,name,digest);context[b"durability"][name]=DURABLE_VERIFIED
 carrier=context.get(b"pending_expected_raw_fd",-1)
 if carrier>=0:close_lifecycle_fd(context,b"pending_expected_raw_fd")
 need(context.get(b"pending_expected_raw_fd",-1)<0)
 context[b"record_seq"]=seq;context[b"record_pending"]=None;context[b"record_sequence_frozen"]=False;context[b"uncertain_record"]=None;context[b"carrier_pre_effect_state"]=b"DELTA_APPLIED_SUCCESSOR_OPEN"

def construct_pending_expected_raw_carrier_before_reservation(context,raw,deadline,require_live,needed_after):
 need(context.get(b"record_pending") is None and not context.get(b"record_sequence_frozen") and context.get(b"record_draft") is not None)
 number=-1;existing=context.get(b"pending_expected_raw_fd",-1)
 if existing>=0:
  need(sealed_carrier(existing,len(raw))==raw);os.lseek(existing,0,os.SEEK_SET);return existing
 try:
  record_boundary(context,deadline,require_live,needed_after);number=acquire_lifecycle_memfd(context,b"pending_expected_raw_fd",b"PENDING_EXPECTED_RAW_FD","p27-e001-pending-raw-v15",os.MFD_CLOEXEC|os.MFD_ALLOW_SEALING,True)
  write_all(number,raw,context,deadline,require_live,needed_after);os.lseek(number,0,os.SEEK_SET)
  fcntl.fcntl(number,fcntl.F_ADD_SEALS,EXACT_SEALS);record_boundary(context,deadline,require_live,needed_after)
  need(sealed_carrier(number,len(raw))==raw);os.lseek(number,0,os.SEEK_SET)
  number=-1;return context[b"pending_expected_raw_fd"]
 finally:
  if number>=0:close_lifecycle_fd(context,b"pending_expected_raw_fd")

def reconcile_pending_record(context,deadline,require_live=False,needed_after=0):
 pending=context.get(b"record_pending");need(context.get(b"record_sequence_frozen") and pending is not None)
 seq,predecessor,name,digest,semantic_delta=pending;semantic_delta_bytes(semantic_delta);raw=context[b"durability_raw"][name];number=-1
 try:
  record_boundary(context,deadline,require_live,needed_after)
  try:number=acquire_lifecycle_open(context,b"reconcile_record_fd",b"DURABLE_RECORD_RECONCILE_FD",name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"attempt"])
  except FileNotFoundError:
   record_boundary(context,deadline,require_live,needed_after);os.fsync(context[b"attempt"]);record_boundary(context,deadline,require_live,needed_after)
   try:number=acquire_lifecycle_open(context,b"reconcile_record_fd",b"DURABLE_RECORD_RECONCILE_FD",name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"attempt"])
   except FileNotFoundError:
    state=b"ABSENT_RECONCILED_SAME_RESERVATION";context[b"durability"][name]=state;return state,digest
   else:raise FaultSet({b"RECONCILIATION_UNKNOWN"})
  opened=os.fstat(number);named=os.stat(name,dir_fd=context[b"attempt"],follow_symlinks=False);again=read_all(number,len(raw))
  need((opened.st_dev,opened.st_ino,opened.st_mode,opened.st_nlink,opened.st_uid,opened.st_gid,opened.st_size)==(named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid,named.st_size))
  need(stat.S_ISREG(opened.st_mode) and stat.S_IMODE(opened.st_mode)==0o400 and opened.st_nlink==1 and opened.st_uid==opened.st_gid==0 and again==raw and sha(again)==digest)
  close_lifecycle_fd(context,b"reconcile_record_fd");number=-1;record_boundary(context,deadline,require_live,needed_after);os.fsync(context[b"attempt"]);record_boundary(context,deadline,require_live,needed_after)
  context[b"durability"][name]=b"DIR_FSYNC_VERIFIED_DELTA_PENDING";commit_record_reservation(context,name,digest);return DURABLE_VERIFIED,digest
 except BaseException:
  context[b"record_sequence_frozen"]=True;context[b"faults"].add(b"RECONCILIATION_UNKNOWN");raise FaultSet({b"RECONCILIATION_UNKNOWN"})
 finally:
  if number>=0:close_lifecycle_fd(context,b"reconcile_record_fd")

def durable_once(context,name,raw,deadline,require_live=True,needed_after=0,semantic_delta=None):
 digest=sha(raw)
 if name in context[b"durability"]:
  if context[b"durability_digest"].get(name)!=digest:raise FaultSet({b"INTERNAL_INVARIANT"})
  pending=context.get(b"record_pending")
  if pending is not None:
   need(pending[2:4]==(name,digest));semantic_delta=pending[4] if semantic_delta is None else semantic_delta;need(semantic_delta==pending[4])
  if context[b"durability"][name]!=DURABLE_VERIFIED and context.get(b"record_sequence_frozen"):
   reconciled,_=reconcile_pending_record(context,deadline,require_live,needed_after)
   if reconciled==DURABLE_VERIFIED:return reconciled,digest
   need(reconciled==b"ABSENT_RECONCILED_SAME_RESERVATION")
  else:return context[b"durability"][name],digest
 need(context.get(b"record_pending") is None and context.get(b"record_draft") is not None and not context.get(b"record_sequence_frozen") and semantic_delta is not None);semantic_delta_bytes(semantic_delta)
 try:
  construct_pending_expected_raw_carrier_before_reservation(context,raw,deadline,require_live,needed_after)
  activate_record_reservation_after_carrier(context,name,raw,digest,semantic_delta)
 except CertificateExpired:
  context[b"faults"].add(b"CERTIFICATE_EXPIRED");context[b"carrier_pre_effect_state"]=b"CARRIER_FAILED_NON_PENDING_PRE_EFFECT"
 except FaultSet as error:
  context[b"faults"].update(error.faults);context[b"carrier_pre_effect_state"]=b"CARRIER_FAILED_NON_PENDING_PRE_EFFECT"
 except StaticReject:
  context[b"faults"].add(b"CERTIFICATE_INVALID");context[b"carrier_pre_effect_state"]=b"CARRIER_FAILED_NON_PENDING_PRE_EFFECT"
 except BaseException:
  context[b"faults"].add(b"INTERNAL_INVARIANT");context[b"carrier_pre_effect_state"]=b"CARRIER_FAILED_NON_PENDING_PRE_EFFECT"
 if context[b"carrier_pre_effect_state"]==b"CARRIER_FAILED_NON_PENDING_PRE_EFFECT":
  carrier=context.get(b"pending_expected_raw_fd",-1)
  if carrier>=0:close_lifecycle_fd(context,b"pending_expected_raw_fd")
  need(context.get(b"pending_expected_raw_fd",-1)<0);context[b"record_draft"]=None;context[b"record_pending"]=None;context[b"record_sequence_frozen"]=False;context[b"uncertain_record"]=None
  return b"CARRIER_FAILED_NON_PENDING_PRE_EFFECT",digest
 state=b"ABSENT_KNOWN";context[b"durability"][name]=state;context[b"durability_digest"][name]=digest;context[b"durability_raw"][name]=raw;context[b"durability_faults"][name]=set();number=reopened=-1;created=None
 try:
  freeze_record_reservation(context,name,digest)
  record_boundary(context,deadline,require_live,needed_after)
  state=b"OPEN_EFFECT_UNKNOWN";context[b"durability"][name]=state
  number=acquire_lifecycle_open(context,b"record_create_fd",b"DURABLE_RECORD_CREATE_FD",name,os.O_RDWR|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC|os.O_NOFOLLOW,0o400,context[b"attempt"])
  record_boundary(context,deadline,require_live,needed_after);state=b"FD_HELD";context[b"durability"][name]=state
  state=b"WRITE_EFFECT_UNKNOWN";context[b"durability"][name]=state
  write_all(number,raw,context,deadline,require_live,needed_after)
  state=b"FILE_FSYNC_EFFECT_UNKNOWN";context[b"durability"][name]=state
  record_boundary(context,deadline,require_live,needed_after);os.fsync(number);record_boundary(context,deadline,require_live,needed_after)
  held=os.fstat(number);record_boundary(context,deadline,require_live,needed_after)
  need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_uid==held.st_gid==0 and held.st_nlink==1 and held.st_size==len(raw))
  created=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,held.st_size)
  close_lifecycle_fd(context,b"record_create_fd");number=-1;state=b"CREATED_FD_CLOSED";context[b"durability"][name]=state
  state=b"NAMED_REOPEN_EFFECT_UNKNOWN";context[b"durability"][name]=state
  reopened=acquire_lifecycle_open(context,b"record_reopen_fd",b"DURABLE_RECORD_REOPEN_FD",name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"attempt"]);record_boundary(context,deadline,require_live,needed_after)
  opened=os.fstat(reopened);named=os.stat(name,dir_fd=context[b"attempt"],follow_symlinks=False)
  reopened_identity=(opened.st_dev,opened.st_ino,opened.st_mode,opened.st_nlink,opened.st_uid,opened.st_gid,opened.st_size);named_identity=(named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid,named.st_size)
  need(created==reopened_identity==named_identity and read_all(reopened,len(raw))==raw);record_boundary(context,deadline,require_live,needed_after)
  close_lifecycle_fd(context,b"record_reopen_fd");reopened=-1;state=b"NAMED_ENTRY_REREAD_VERIFIED";context[b"durability"][name]=state
  state=b"DIR_FSYNC_EFFECT_UNKNOWN";context[b"durability"][name]=state
  record_boundary(context,deadline,require_live,needed_after);os.fsync(context[b"attempt"]);record_boundary(context,deadline,require_live,needed_after)
  state=b"DIR_FSYNC_VERIFIED_DELTA_PENDING";context[b"durability"][name]=state;commit_record_reservation(context,name,digest);state=DURABLE_VERIFIED
 except CertificateExpired:
  context[b"faults"].add(b"CERTIFICATE_EXPIRED");context[b"durability_faults"][name].add(b"CERTIFICATE_EXPIRED");context[b"durability"][name]=state
 except FaultSet as error:
  context[b"faults"].update(error.faults);context[b"durability_faults"][name].update(error.faults);context[b"durability"][name]=state
 except StaticReject:
  context[b"faults"].add(b"CERTIFICATE_INVALID");context[b"durability_faults"][name].add(b"CERTIFICATE_INVALID");context[b"durability"][name]=state
 except BaseException:
  context[b"faults"].add(b"INTERNAL_INVARIANT");context[b"durability_faults"][name].add(b"INTERNAL_INVARIANT");context[b"durability"][name]=state
 finally:
  if number>=0:close_lifecycle_fd(context,b"record_create_fd")
  if reopened>=0:close_lifecycle_fd(context,b"record_reopen_fd")
 if state!=DURABLE_VERIFIED:freeze_record_reservation(context,name,digest)
 return context[b"durability"][name],digest

def resolve_pending_before_successor(context,deadline):
 if not context.get(b"record_sequence_frozen"):return True
 pending=context.get(b"record_pending");need(pending is not None and context.get(b"attempt",-1)>=0)
 seq,predecessor,name,digest,semantic_delta=pending;raw=context[b"durability_raw"][name]
 state,verified_digest=durable_once(context,name,raw,deadline,False,FAILURE_TAIL_NS,semantic_delta)
 if state!=DURABLE_VERIFIED:return False
 need(verified_digest==digest and context[b"record_seq"]==seq and context[b"record_pending"] is None and not context[b"record_sequence_frozen"])
 need(context[b"chain_sha"]==digest and context[b"last_applied_record_delta_sha"]==sha(semantic_delta_bytes(semantic_delta)))
 return True

def primary(faults):
 ordered=tuple(x for x in FAULT_ORDER if x in faults);need(faults and len(ordered)==len(faults))
 return ordered[0]

def disposition(faults):
 need(faults)
 return b"CONSUMED_INDETERMINATE" if any(x in INDETERMINATE for x in faults) else b"CONSUMED_FAIL"

def close_numbers(numbers):
 for number in numbers:
  context=ACTIVE_LIFECYCLE_CONTEXT
  if context is not None:
   slot=lifecycle_live_number_owner(context,number)
   if slot is not None:close_lifecycle_fd(context,slot);continue
  strict_close_unadopted(number)

class OwnershipClosePending(RefusalFinalityPending):pass

ACTIVE_LIFECYCLE_CONTEXT=None

def register_runtime_fd(slot,kind,number):
 need(ACTIVE_LIFECYCLE_CONTEXT is not None);return register_lifecycle_fd(ACTIVE_LIFECYCLE_CONTEXT,slot,kind,number,False)

LIFECYCLE_ENDPOINTS={b"actor_control_fd":b"actor_control",b"transfer_control_fd":b"transfer_control"}
LIFECYCLE_PERMANENT_SLOTS=(b"attempt",b"attempt_base_fd",b"stage_fd",b"cgfd",b"root_events_fd",b"root_kill_fd",b"out_fd",b"err_fd",b"events_fd",b"outer_pidfd",b"cgroup_base_fd",b"pending_expected_raw_fd",b"actor_control_fd",b"transfer_control_fd",b"actor_pidfd_fd",b"external_owner_pidfd_fd")
LIFECYCLE_TRANSFER_ORDER={b"ATTEMPT_DIRFD":0,b"ATTEMPT_BASE_DIRFD":1,b"STAGE_DIRFD":2,b"CGROUP_DIRFD":3,b"ROOT_EVENTS_FD":4,b"ROOT_KILL_FD":5,b"OUT_FD":6,b"ERR_FD":7,b"EVENTS_FD":8,b"OUTER_PIDFD":9,b"CGROUP_BASE_DIRFD":10,b"ACTOR_CONTROL_FD":11,b"PENDING_EXPECTED_RAW_FD":12}
LIFECYCLE_SLOT_SPEC=(
 (b"attempt",b"ATTEMPT_DIRFD",True),(b"attempt_base_fd",b"ATTEMPT_BASE_DIRFD",True),(b"stage_fd",b"STAGE_DIRFD",True),(b"cgfd",b"CGROUP_DIRFD",True),(b"root_events_fd",b"ROOT_EVENTS_FD",True),(b"root_kill_fd",b"ROOT_KILL_FD",True),(b"out_fd",b"OUT_FD",True),(b"err_fd",b"ERR_FD",True),(b"events_fd",b"EVENTS_FD",True),(b"outer_pidfd",b"OUTER_PIDFD",True),(b"cgroup_base_fd",b"CGROUP_BASE_DIRFD",True),(b"pending_expected_raw_fd",b"PENDING_EXPECTED_RAW_FD",True),(b"actor_control_fd",b"ACTOR_CONTROL_FD",True),(b"transfer_control_fd",b"EXTERNAL_CONTROL_FD_NONTRANSFERABLE",False),(b"actor_pidfd_fd",b"ACTOR_PIDFD_NONTRANSFERABLE",False),(b"external_owner_pidfd_fd",b"EXTERNAL_OWNER_PIDFD_NONTRANSFERABLE",False),
 (b"certificate_carrier_fd",b"CERTIFICATE_CARRIER_FD",False),(b"envelope_carrier_fd",b"ENVELOPE_CARRIER_FD",False),(b"snapshot_carrier_fd",b"SNAPSHOT_CARRIER_FD",False),(b"plan_carrier_fd",b"PLAN_CARRIER_FD",False),(b"actor_source_carrier_fd",b"ACTOR_SOURCE_CARRIER_FD",False),(b"host_source_carrier_fd",b"HOST_SOURCE_CARRIER_FD",False),(b"reservation_carrier_fd",b"RESERVATION_CARRIER_FD",False),(b"external_manifest_carrier_fd",b"EXTERNAL_MANIFEST_CARRIER_FD",False),(b"watchdog_source_carrier_fd",b"WATCHDOG_SOURCE_CARRIER_FD",False),
 (b"cap_status_fd",b"PROC_STATUS_OBSERVATION_FD",False),(b"proc_starttime_fd",b"PROC_STARTTIME_OBSERVATION_FD",False),(b"mount_fdinfo_fd",b"MOUNT_FDINFO_OBSERVATION_FD",False),(b"mount_table_fd",b"MOUNT_TABLE_OBSERVATION_FD",False),(b"boot_id_fd",b"BOOT_ID_OBSERVATION_FD",False),(b"mount_graph_fd",b"MOUNT_GRAPH_OBSERVATION_FD",False),(b"dependency_root_fd",b"DEPENDENCY_ROOT_DIRFD",False),(b"dependency_current_fd",b"DEPENDENCY_CURRENT_DIRFD",False),(b"dependency_following_fd",b"DEPENDENCY_FOLLOWING_DIRFD",False),(b"dependency_leaf_fd",b"DEPENDENCY_LEAF_VERIFY_FD",False),
 (b"reconcile_record_fd",b"DURABLE_RECORD_RECONCILE_FD",False),(b"record_create_fd",b"DURABLE_RECORD_CREATE_FD",False),(b"record_reopen_fd",b"DURABLE_RECORD_REOPEN_FD",False),(b"attempt_received",b"ATTEMPT_DIRFD",True),(b"pidfd_arm_procs_fd",b"CGROUP_PROCS_OBSERVATION_FD",False),(b"pidfd_arm_status_fd",b"PROC_STATUS_OBSERVATION_FD",False),
 (b"recovery_stage_base_fd",b"STAGE_RECOVERY_BASE_DIRFD",False),(b"recovery_stage_received",b"STAGE_DIRFD",True),(b"recovery_stage_leaf_fd",b"STAGE_LEAF_VERIFY_FD",False),(b"stage_base_verify_fd",b"STAGE_BASE_VERIFY_DIRFD",False),(b"stage_received",b"STAGE_DIRFD",True),(b"stage_leaf_verify_fd",b"STAGE_LEAF_VERIFY_FD",False),
 (b"containment_received",b"CGROUP_DIRFD",True),(b"containment_type_fd",b"CGROUP_TYPE_VERIFY_FD",False),(b"containment_controllers_fd",b"CGROUP_CONTROLLERS_VERIFY_FD",False),(b"containment_subtree_fd",b"CGROUP_SUBTREE_VERIFY_FD",False),(b"containment_root_events_received",b"ROOT_EVENTS_FD",True),(b"containment_root_kill_received",b"ROOT_KILL_FD",True),
 (b"stream_out_received",b"OUT_FD",True),(b"stream_err_received",b"ERR_FD",True),(b"stream_events_received",b"EVENTS_FD",True),(b"outer_pidfd_received",b"OUTER_PIDFD",True),
 (b"static_runtime_root_fd",b"RUNTIME_ROOT_VERIFY_DIRFD",False),(b"static_safe_base_fd",b"SAFE_BASE_VERIFY_DIRFD",False),(b"static_cgroup_type_fd",b"CGROUP_TYPE_VERIFY_FD",False),(b"static_cgroup_controllers_fd",b"CGROUP_CONTROLLERS_VERIFY_FD",False),(b"static_cgroup_subtree_fd",b"CGROUP_SUBTREE_VERIFY_FD",False),(b"refusal_runtime_root_fd",b"RUNTIME_ROOT_VERIFY_DIRFD",False)
)+tuple((b"unexpected_control_right_"+str(index).encode(),b"UNEXPECTED_CONTROL_RIGHT",False) for index in range(4))+tuple((b"external_unexpected_right_"+str(index).encode(),b"UNEXPECTED_EXTERNAL_RIGHT",False) for index in range(13))+tuple((b"external_receipt_carrier_"+str(index).encode(),b"EXTERNAL_RECEIPT_SEALED_CARRIER_FD",False) for index in range(13))+tuple((b"refusal_unexpected_right_"+str(index).encode(),b"UNEXPECTED_REFUSAL_RIGHT",False) for index in range(4))
LIFECYCLE_SLOT_SPEC_MAP={slot:(kind,transferable) for slot,kind,transferable in LIFECYCLE_SLOT_SPEC}
PIDFD_LIFECYCLE_SLOTS=(b"actor_pidfd_fd",b"external_owner_pidfd_fd",b"outer_pidfd",b"outer_pidfd_received")

def new_lifecycle_registry():
 return {slot:[kind,-1,None,b"RESERVED",transferable,None,False,LIFECYCLE_TRANSFER_ORDER.get(kind,-1)] for slot,kind,transferable in LIFECYCLE_SLOT_SPEC}

def new_pidfd_poller_records():
 return [[None,None,-1,False] for index in range(2048)]

def lifecycle_identity(number):
 held=os.fstat(number);access=fcntl.fcntl(number,fcntl.F_GETFL)&os.O_ACCMODE
 return (held.st_dev,held.st_ino,held.st_mode,held.st_uid,held.st_gid,access)

def lifecycle_audit(context,slot):
 entry=context[b"fd_registry"][slot]
 try:context[b"fd_close_journal"].append((slot,)+tuple(entry))
 except BaseException:context[b"fd_journal_complete"]=False

def lifecycle_live_number_owner(context,number,exclude=None):
 owner=None
 for slot,entry in context[b"fd_registry"].items():
  if slot!=exclude and entry[6] and entry[1]==number:
   need(owner is None);owner=slot
 return owner

def lifecycle_begin_acquisition(context,slot,kind,transferable,provenance):
 need(slot in LIFECYCLE_SLOT_SPEC_MAP and LIFECYCLE_SLOT_SPEC_MAP[slot][0]==kind and bool(transferable)==LIFECYCLE_SLOT_SPEC_MAP[slot][1])
 entry=context[b"fd_registry"][slot];need(not entry[6] and entry[3] not in (b"ACQUIRING",b"ADOPTED_RAW"))
 entry[0]=kind;entry[1]=-1;entry[2]=None;entry[3]=b"ACQUIRING";entry[4]=transferable;entry[5]=provenance;entry[6]=False;entry[7]=LIFECYCLE_TRANSFER_ORDER.get(kind,-1)
 return entry

def lifecycle_finish_adoption(context,slot):
 entry=context[b"fd_registry"][slot];number=entry[1];need(entry[6] and number>=0 and lifecycle_live_number_owner(context,number,slot) is None)
 try:identity=lifecycle_identity(number)
 except BaseException:
  entry[3]=b"ADOPTED_RAW_CLOSE_REQUIRED";raise
 entry[2]=identity;entry[3]=b"OPEN_PROVED";context[slot]=number;lifecycle_audit(context,slot);return number

def lifecycle_adopt_raw(context,slot,kind,number,transferable=False,provenance=None):
 entry=lifecycle_begin_acquisition(context,slot,kind,transferable,provenance)
 need(type(number)is int and number>=0)
 entry[1]=number;entry[3]=b"ADOPTED_RAW";entry[6]=True
 try:return lifecycle_finish_adoption(context,slot)
 except BaseException:close_lifecycle_fd(context,slot);raise

def register_lifecycle_fd(context,slot,kind,number,transferable=False,provenance=None):
 return lifecycle_adopt_raw(context,slot,kind,number,transferable,provenance)

def acquire_lifecycle_open(context,slot,kind,path,flags,mode=0o777,dir_fd=None,transferable=False,provenance=None):
 entry=lifecycle_begin_acquisition(context,slot,kind,transferable,provenance);number=-1
 try:
  number=os.open(path,flags,mode,dir_fd=dir_fd)
  entry[1]=number;entry[3]=b"ADOPTED_RAW";entry[6]=True
  return lifecycle_finish_adoption(context,slot)
 except BaseException:
  if entry[6]:close_lifecycle_fd(context,slot)
  else:entry[3]=b"ACQUIRE_FAILED_NO_FD"
  raise

def acquire_lifecycle_memfd(context,slot,kind,label,flags,transferable=False,provenance=None):
 entry=lifecycle_begin_acquisition(context,slot,kind,transferable,provenance);number=-1
 try:
  number=os.memfd_create(label,flags)
  entry[1]=number;entry[3]=b"ADOPTED_RAW";entry[6]=True
  return lifecycle_finish_adoption(context,slot)
 except BaseException:
  if entry[6]:close_lifecycle_fd(context,slot)
  else:entry[3]=b"ACQUIRE_FAILED_NO_FD"
  raise

def acquire_lifecycle_dup(context,slot,kind,source,transferable=False,provenance=None):
 entry=lifecycle_begin_acquisition(context,slot,kind,transferable,provenance);number=-1
 try:
  number=os.dup(source)
  entry[1]=number;entry[3]=b"ADOPTED_RAW";entry[6]=True
  return lifecycle_finish_adoption(context,slot)
 except BaseException:
  if entry[6]:close_lifecycle_fd(context,slot)
  else:entry[3]=b"ACQUIRE_FAILED_NO_FD"
  raise

def bind_lifecycle_provenance(context,slot,provenance):
 entry=context[b"fd_registry"][slot];need(entry[6] and entry[3] in (b"OPEN_PROVED",b"OPEN_RETRYABLE_AFTER_CLOSE_ERROR") and provenance is not None)
 entry[5]=provenance;lifecycle_audit(context,slot);return provenance

def bind_lifecycle_endpoint(context,slot,endpoint_key,endpoint):
 entry=context[b"fd_registry"][slot];need(entry[6] and endpoint.fileno()==entry[1] and LIFECYCLE_ENDPOINTS[slot]==endpoint_key)
 context[endpoint_key]=endpoint;return endpoint

def promote_lifecycle_fd(context,old_slot,new_slot,new_kind,transferable=False,provenance=None):
 source=context[b"fd_registry"][old_slot];destination=context[b"fd_registry"][new_slot]
 need(source[6] and source[3]==b"OPEN_PROVED" and not destination[6] and LIFECYCLE_SLOT_SPEC_MAP[new_slot]==(new_kind,bool(transferable)))
 number=source[1];identity=source[2];bound_provenance=source[5] if provenance is None else provenance
 destination[0]=new_kind;destination[1]=number;destination[2]=identity;destination[3]=b"OPEN_PROVED";destination[4]=transferable;destination[5]=bound_provenance;destination[7]=LIFECYCLE_TRANSFER_ORDER.get(new_kind,-1)
 destination[6]=True
 for cell in context[b"pidfd_poller_records"]:
  if cell[3] and cell[1]==old_slot and cell[2]==number:cell[1]=new_slot
 source[6]=False;source[1]=-1;source[3]=b"PROMOTED_ALIAS_CLEARED"
 context[new_slot]=number;context[old_slot]=-1;lifecycle_audit(context,old_slot);lifecycle_audit(context,new_slot);return number

def lifecycle_mark_closed(context,slot,entry,state):
 number=entry[1];entry[1]=-1;entry[3]=state;entry[6]=False
 if context.get(slot)==number:context[slot]=-1
 endpoint_key=LIFECYCLE_ENDPOINTS.get(slot)
 if endpoint_key is not None:context[endpoint_key]=None
 lifecycle_audit(context,slot);return True

def register_lifecycle_poller(context,poller,slot,mask):
 entry=context[b"fd_registry"][slot];need(entry[6] and entry[1]>=0 and slot in PIDFD_LIFECYCLE_SLOTS)
 cell=None
 for candidate in context[b"pidfd_poller_records"]:
  if not candidate[3]:cell=candidate;break
 need(cell is not None);cell[0]=poller;cell[1]=slot;cell[2]=entry[1];cell[3]=True
 try:poller.register(entry[1],mask)
 except BaseException:cell[0]=None;cell[1]=None;cell[2]=-1;cell[3]=False;raise
 return entry[1]

def unregister_lifecycle_pollers(context,slot,number):
 for cell in context[b"pidfd_poller_records"]:
  if cell[3] and cell[1]==slot and cell[2]==number:
   try:cell[0].unregister(number)
   except KeyError:pass
   except BaseException:raise OwnershipClosePending("pidfd-poller-unregister")
   cell[0]=None;cell[1]=None;cell[2]=-1;cell[3]=False
 return True

def pidfd_ready_event(event):
 if event&select.POLLNVAL:raise FaultSet({b"PIDFD_BINDING"})
 return bool(event&(select.POLLIN|select.POLLHUP|select.POLLERR))

def strict_close_unadopted(number):
 need(type(number)is int and number>=0)
 try:os.close(number)
 except OSError:
  try:os.fstat(number)
  except OSError as probe:
   need(probe.errno==errno.EBADF);return True
  raise OwnershipClosePending("unadopted-raw-close-live")
 return True

def close_lifecycle_fd(context,slot):
 entry=context[b"fd_registry"].get(slot)
 if entry is None or not entry[6]:return True
 kind,number,identity,state,transferable,provenance,owns,order=entry;endpoint_key=LIFECYCLE_ENDPOINTS.get(slot);endpoint=context.get(endpoint_key) if endpoint_key is not None else None
 need(lifecycle_live_number_owner(context,number,slot) is None)
 if identity is not None:
  try:observed=lifecycle_identity(number)
  except OSError as probe:
   if probe.errno==errno.EBADF:return lifecycle_mark_closed(context,slot,entry,b"PROVED_CLOSED_BEFORE_RETRY_EBADF")
   entry[3]=b"PRE_CLOSE_REVALIDATION_UNKNOWN_HOLD";raise OwnershipClosePending("pre-close-revalidation")
  if observed!=identity:entry[3]=b"PRE_CLOSE_IDENTITY_REUSE_HOLD";raise OwnershipClosePending("pre-close-identity-reuse")
 if slot in PIDFD_LIFECYCLE_SLOTS:unregister_lifecycle_pollers(context,slot,number)
 if endpoint is not None:
  try:detached=endpoint.detach()
  except BaseException:entry[3]=b"ENDPOINT_DETACH_HOLD";raise OwnershipClosePending("endpoint-detach")
  need(detached==number);context[endpoint_key]=None
 try:
  os.close(number)
 except OSError:
  try:observed=lifecycle_identity(number)
  except OSError as probe:
   if probe.errno==errno.EBADF:return lifecycle_mark_closed(context,slot,entry,b"PROVED_CLOSED_AFTER_EBADF_RECONCILIATION")
   entry[3]=b"CLOSE_RECONCILIATION_UNKNOWN_HOLD";raise OwnershipClosePending("close-probe-unknown")
  if identity is not None and observed==identity:
   entry[3]=b"OPEN_RETRYABLE_AFTER_CLOSE_ERROR";raise OwnershipClosePending("close-live-retryable")
  entry[3]=b"CLOSE_IDENTITY_MISMATCH_HOLD";raise OwnershipClosePending("close-identity-mismatch")
 return lifecycle_mark_closed(context,slot,entry,b"PROVED_CLOSED_BY_CLOSE_RETURN")

def close_lifecycle_slots(context,slots):
 for slot in slots:close_lifecycle_fd(context,slot)
 return True

def bootstrap_lifecycle_registry(context):
 register_lifecycle_fd(context,b"actor_control_fd",b"ACTOR_CONTROL_FD",3,True)
 register_lifecycle_fd(context,b"actor_pidfd_fd",b"ACTOR_PIDFD_NONTRANSFERABLE",4,False)
 register_lifecycle_fd(context,b"attempt_base_fd",b"ATTEMPT_BASE_DIRFD",5,True)
 register_lifecycle_fd(context,b"cgroup_base_fd",b"CGROUP_BASE_DIRFD",6,True)
 register_lifecycle_fd(context,b"transfer_control_fd",b"EXTERNAL_CONTROL_FD_NONTRANSFERABLE",14,False)
 register_lifecycle_fd(context,b"external_owner_pidfd_fd",b"EXTERNAL_OWNER_PIDFD_NONTRANSFERABLE",15,False)
 for slot,kind,number in ((b"certificate_carrier_fd",b"CERTIFICATE_CARRIER_FD",7),(b"envelope_carrier_fd",b"ENVELOPE_CARRIER_FD",8),(b"snapshot_carrier_fd",b"SNAPSHOT_CARRIER_FD",9),(b"plan_carrier_fd",b"PLAN_CARRIER_FD",10),(b"actor_source_carrier_fd",b"ACTOR_SOURCE_CARRIER_FD",11),(b"host_source_carrier_fd",b"HOST_SOURCE_CARRIER_FD",12),(b"reservation_carrier_fd",b"RESERVATION_CARRIER_FD",13),(b"external_manifest_carrier_fd",b"EXTERNAL_MANIFEST_CARRIER_FD",16),(b"watchdog_source_carrier_fd",b"WATCHDOG_SOURCE_CARRIER_FD",100)):register_lifecycle_fd(context,slot,kind,number,False)
 snapshot=select.poll();register_lifecycle_poller(context,snapshot,b"actor_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL);register_lifecycle_poller(context,snapshot,b"external_owner_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL);context[b"offer_snapshot_poller"]=snapshot
 return True

def next_record(context):
 need(not context.get(b"record_sequence_frozen") and context.get(b"record_pending") is None and context.get(b"record_draft") is None)
 seq=context[b"record_seq"]+1;context[b"record_draft"]=(seq,context[b"chain_sha"],None,None);context[b"carrier_pre_effect_state"]=b"DRAFT_NON_PENDING_PRE_EFFECT";return str(seq).encode()

def chained_record(context,name,tag,lines,deadline,require_live,reserve_after,semantic_delta):
 need(type(name)is bytes and type(tag)is bytes and type(lines)is tuple and time.monotonic_ns()<=deadline)
 seq=next_record(context);predecessor=context[b"chain_sha"]
 body=tag+b"\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+predecessor+b"\n"+b"".join(key+b"="+value+b"\n" for key,value in lines)+b"PHASE_DEADLINE_NS="+str(deadline).encode()+b"\nRECORD_END=1\n"
 state,digest=durable_once(context,name,body,deadline,require_live,reserve_after,semantic_delta+(str(deadline).encode(),))
 if state!=DURABLE_VERIFIED:raise FaultSet({b"REPORT_DURABILITY_UNKNOWN"})
 need(context[b"chain_sha"]==digest);return body,digest


def attempt_intent(auth,cert,cert_raw,envelope_raw,source_raw):
 return (b"P27E001_ATTEMPT_INTENT_V15\nAUTH_ID="+auth+b"\nNONCE="+auth+b"\nRECORD_SEQ=1\nPREDECESSOR_SHA256=NONE\nISSUER_FINAL_ENVELOPE_SHA256="+sha(envelope_raw)+b"\nCERTIFICATE_SHA256="+sha(cert_raw)+b"\nPLAN_SHA256="+cert[b"PLAN_SHA256"]+b"\nRUNNER_SHA256="+cert[b"RUNNER_SHA256"]+b"\nRECOVERY_SHA256="+sha(source_raw)+b"\nE0366_SNAPSHOT_BYTES=2303269\nE0366_SNAPSHOT_LF=23672\nE0366_SNAPSHOT_SHA256="+SNAPSHOT_EXPECT[2]+b"\nE0366_SNAPSHOT_TERMINAL_HEX="+SNAPSHOT_TERMINAL_HEX+b"\nV15_SHA256="+cert[b"V15_SHA256"]+b"\nSUITE="+b",".join(PROBES)+b"\nATTEMPT_PATH_HEX="+(b"/var/lib/p27-e001-host-v15/attempts/"+auth).hex().encode()+b"\nSTAGE_PATH_HEX="+(b"/tmp/p27-e001-host-v15/"+auth).hex().encode()+b"\nCGROUP_PATH_HEX="+(b"/sys/fs/cgroup/p27-e001-host-v15/"+auth).hex().encode()+b"\nACTOR_ENTRY_CAPS=00000000000401c0\nPAYLOAD_FINAL_CAPS=0000000000000000\nABSOLUTE_EXPIRY_REALTIME_NS="+cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"]+b"\nCONSUMED_OR_EFFECT_UNKNOWN=1\nRETRY_ALLOWED=0\nINTENT_END=1\n")

def verify_attempt_fd(number):
 held=os.fstat(number);fd_access(number,os.O_RDONLY);named=os.stat(AUTH,dir_fd=5,follow_symlinks=False)
 need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==(named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid))
 need(stat.S_ISDIR(held.st_mode) and held.st_uid==held.st_gid==0 and stat.S_IMODE(held.st_mode)==0o700 and held.st_nlink==2)
 base_check(5,CERT,b"ATTEMPT_BASE");return held

def retain_attempt_dirfd(context):
 context[b"faults"].update((b"ATTEMPT_DIRFD_UNKNOWN",b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED"))
 context[b"consumption_state"]=b"DIRFD_HORIZON_CLOSED_NO_REOPEN"
 return False

def consume_attempt(context,cert_raw,envelope_raw,source_raw,deadline):
 context[b"consume_deadline"]=deadline;context[b"consumption_state"]=b"MKDIR_CALL_ENTERED";context[b"mkdir_created"]=False
 try:
  checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
  os.mkdir(AUTH,0o700,dir_fd=5)
  context[b"mkdir_created"]=True;context[b"consumption_state"]=b"MKDIR_RETURNED_CREATED";context[b"attempt_state"]=b"CREATED_BASE_HELD";context[b"local_fd_state"]=b"LOCAL_UNVERIFIED"
  post_deadline(deadline);checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
 except FileExistsError as error:
  context[b"consumption_state"]=b"COLLISION";context[b"collision"]=True;context[b"attempt_state"]=b"COLLISION_DETECTED";context[b"faults"].add(b"ATTEMPT_COLLISION")
  context[b"collision_identity"]=(0,0,0,0,0,0)
  try:
   close_lifecycle_fd(context,b"attempt_base_fd");context[b"attempt_base_closed_on_collision"]=True;context[b"attempt_state"]=b"COLLISION_CLOSED"
  except OwnershipClosePending:
   context[b"attempt_state"]=b"COLLISION_BASE_HELD_FOR_TRANSFER";context[b"faults"].add(b"ATTEMPT_DIRFD_UNKNOWN")
  raise FaultSet(set(context[b"faults"])) from error
 except CertificateExpired:
  if context[b"mkdir_created"]:context[b"consumption_state"]=b"MKDIR_CREATED_BASE_HELD";context[b"attempt_state"]=b"CREATED_BASE_HELD";context[b"faults"].update((b"CERTIFICATE_EXPIRED",b"ATTEMPT_DIRFD_UNKNOWN"))
  else:context[b"consumption_state"]=b"MKDIR_EFFECT_UNKNOWN";context[b"faults"].update((b"CERTIFICATE_EXPIRED",b"ATTEMPT_NAMESPACE_UNKNOWN"))
  raise
 except BaseException as error:
  if context[b"mkdir_created"]:context[b"consumption_state"]=b"MKDIR_CREATED_BASE_HELD";context[b"attempt_state"]=b"CREATED_BASE_HELD";context[b"faults"].add(b"ATTEMPT_DIRFD_UNKNOWN")
  else:context[b"consumption_state"]=b"MKDIR_EFFECT_UNKNOWN";context[b"faults"].add(b"ATTEMPT_NAMESPACE_UNKNOWN")
  raise FaultSet(set(context[b"faults"])) from error
 number=-1
 try:
  context[b"consumption_state"]=b"IMMEDIATE_DIRFD_CALL_ENTERED"
  checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
  number=acquire_lifecycle_open(context,b"attempt_received",b"ATTEMPT_DIRFD",AUTH,os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=5,transferable=True)
  post_deadline(deadline);checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
  verify_attempt_fd(number);context[b"local_fd_state"]=b"LOCAL_VERIFIED";checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
  promote_lifecycle_fd(context,b"attempt_received",b"attempt",b"ATTEMPT_DIRFD",True);number=-1;context[b"local_fd_state"]=b"LOCAL_VERIFIED_HELD";context[b"attempt_state"]=b"LOCAL_VERIFIED_HELD";context[b"consumption_state"]=b"DIRFD_HELD_VERIFIED"
 except CertificateExpired:
  context[b"consumption_state"]=b"DIRFD_EFFECT_UNKNOWN";context[b"faults"].update((b"CERTIFICATE_EXPIRED",b"ATTEMPT_DIRFD_UNKNOWN"))
  raise
 except BaseException as error:
  context[b"consumption_state"]=b"DIRFD_EFFECT_UNKNOWN";context[b"faults"].add(b"ATTEMPT_DIRFD_UNKNOWN")
  raise FaultSet(set(context[b"faults"])) from error
 finally:
  if number>=0:close_lifecycle_fd(context,b"attempt_received")
 context[b"consumption_state"]=b"BASE_FSYNC_EFFECT_UNKNOWN"
 try:
  checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline);os.fsync(5);post_deadline(deadline);checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
 except CertificateExpired:
  context[b"faults"].update((b"CERTIFICATE_EXPIRED",b"ATTEMPT_BASE_DURABILITY_UNKNOWN"));raise
 except BaseException as error:
  context[b"faults"].add(b"ATTEMPT_BASE_DURABILITY_UNKNOWN");raise FaultSet(set(context[b"faults"])) from error
 context[b"consumption_state"]=b"BASE_DURABLE"
 body=attempt_intent(AUTH,CERT,cert_raw,envelope_raw,source_raw)
 reserved_digest=prepare_first_intent_draft(context,b"intent.v5",body);need(reserved_digest==sha(body))
 state,digest=durable_once(context,b"intent.v5",body,deadline,True,PRE_STAGE_REMAIN_NS,(b"INTENT",))
 if state!=DURABLE_VERIFIED:
  context[b"faults"].add(b"INTENT_DURABILITY_UNKNOWN");raise FaultSet(set(context[b"faults"]))
 context[b"intent_durable"]=True;context[b"intent_count"]=1;context[b"commit_count"]=1;context[b"chain_sha"]=digest;need(context[b"record_seq"]==1 and context[b"record_pending"] is None and not context[b"record_sequence_frozen"])
 context[b"local_fd_state"]=b"PUBLISHED";context[b"attempt_state"]=b"PUBLISHED";context[b"consumption_state"]=b"INTENT_DURABLE_DIRFD_PUBLISHED"
 close_lifecycle_fd(context,b"attempt_base_fd")
 return digest

def release_record(context,values):
 seq=next_record(context);predecessor=context[b"chain_sha"];origin=time.monotonic_ns();deadline=udec(values[b"release_record_deadline_ns"]);need(origin<=deadline and deadline==udec(values[b"release_origin_ns"])+RELEASE_RECORD_OFFSET_NS)
 body=(b"P27E001_RELEASE_STATE_V15\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+predecessor+b"\nORDINAL="+values[b"ordinal"]+b"\nPROBE="+values[b"probe"]+b"\nOUTER_PID="+values[b"outer_pid"]+b"\nOUTER_STARTTIME="+values[b"outer_starttime"]+b"\nPIDFD_BOUND="+values[b"pidfd_bound"]+b"\nPIDFD_EXIT_READY_OBSERVED=0\nSTOPPED_RAW_STATUS="+values[b"stopped_raw_status"]+b"\nCGROUP_MEMBER="+values[b"cgroup_member"]+b"\nCGROUP_DEV="+values[b"cgroup_dev"]+b"\nCGROUP_INO="+values[b"cgroup_ino"]+b"\nCGROUP_MODE="+values[b"cgroup_mode"]+b"\nCGROUP_NLINK="+values[b"cgroup_nlink"]+b"\nCGROUP_UID="+values[b"cgroup_uid"]+b"\nCGROUP_GID="+values[b"cgroup_gid"]+b"\nARGV_SHA256="+values[b"argv_sha256"]+b"\nENV_SHA256="+values[b"env_sha256"]+b"\nRELEASE_ORIGIN_NS="+values[b"release_origin_ns"]+b"\nLAUNCH_OVERALL_DEADLINE_NS="+values[b"launch_overall_deadline_ns"]+b"\nRELEASE_RECORD_DEADLINE_NS="+values[b"release_record_deadline_ns"]+b"\nRELEASE_REPLY_DEADLINE_NS="+values[b"release_reply_deadline_ns"]+b"\nB_RECORD_ORIGIN_NS="+str(origin).encode()+b"\nB_RECORD_DEADLINE_NS="+str(deadline).encode()+b"\nCERTIFICATE_EXPIRY_REALTIME_NS="+CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"]+b"\nSTATE=RELEASE_AUTHORIZED\nRELEASE_END=1\n")
 state,digest=durable_once(context,b"release-"+values[b"probe"]+b".v5",body,deadline,True,udec(values[b"launch_overall_deadline_ns"])-deadline,(b"RELEASE",values[b"probe"]))
 if state!=DURABLE_VERIFIED:raise FaultSet({b"RELEASE_RECORD_DURABILITY_UNKNOWN"})
 context[b"chain_sha"]=digest;context[b"release_sha"]=digest;return digest

CANDIDATE_KEYS=(b"ordinal",b"probe",b"release_record_sha256",b"release_origin_ns",b"release_return_ns",b"host_complete_ns",b"capture_done_ns",b"direct_wait_state",b"outer_raw_status",b"pidfd_bound",b"pidfd_exit_ready_observed",b"stdout_len",b"stdout_sha256",b"stdout_eof",b"stdout_overflow",b"stderr_len",b"stderr_sha256",b"stderr_eof",b"stderr_overflow",b"cgroup_empty",b"parser_language",b"parser_structure",b"parser_semantics",b"candidate",b"terminal",b"certificate_expiry_realtime_ns")
FINAL_REPORT_KEYS=(b"AUTH_ID",b"RECORD_SEQ",b"PREDECESSOR_SHA256",b"OUTCOME_KIND",b"SUITE",b"ENTERED_COUNT",b"COMMITTED_COUNT",b"REAPED_COUNT",b"STOPPED_COUNT",b"STOP_ORDINAL",b"STOP_PROBE",b"STAGE_STATE",b"ATTEMPT_STATE",b"CONTAINMENT_STATE",b"EMPTY_STATE",b"REMOVAL_STATE",b"PRIMARY",b"FAULT_SET",b"CHAIN_BEFORE_REPORT_SHA256",b"KILL_CALL_COUNT",b"KILL_STATE",b"KILL_TICKET_STATE",b"ACK_STATE",b"RECONCILIATION_STATE",b"OWNER_CLOSURE_STATE",b"FAILURE_ORIGIN_NS",b"CLEANUP_EFFECT_DEADLINE_NS",b"TERMINAL_ORIGIN_NS",b"TERMINAL_DEADLINE_NS",b"TERMINAL_SCHEDULE_HEX",b"CERTIFICATE_LIVE_AT_REPORT",b"RETRY_ALLOWED",b"DISPOSITION",b"PHASE_DEADLINE_NS")

def forensic_body(values):
 return (b"RELEASE_ORIGIN_NS="+values[b"release_origin_ns"]+b"\nRELEASE_RETURN_NS="+values[b"release_return_ns"]+b"\nHOST_COMPLETE_NS="+values[b"host_complete_ns"]+b"\nCAPTURE_DONE_NS="+values[b"capture_done_ns"]+b"\nDIRECT_WAIT="+values[b"direct_wait_state"]+b"\nOUTER_RAW_STATUS="+values[b"outer_raw_status"]+b"\nPIDFD_BOUND="+values[b"pidfd_bound"]+b"\nPIDFD_EXIT_READY_OBSERVED="+values[b"pidfd_exit_ready_observed"]+b"\nSTDOUT_BYTES="+values[b"stdout_len"]+b"\nSTDOUT_SHA256="+values[b"stdout_sha256"]+b"\nSTDOUT_EOF="+values[b"stdout_eof"]+b"\nSTDOUT_OVERFLOW="+values[b"stdout_overflow"]+b"\nSTDERR_BYTES="+values[b"stderr_len"]+b"\nSTDERR_SHA256="+values[b"stderr_sha256"]+b"\nSTDERR_EOF="+values[b"stderr_eof"]+b"\nSTDERR_OVERFLOW="+values[b"stderr_overflow"]+b"\nCGROUP_EMPTY="+values[b"cgroup_empty"]+b"\nPARSER_LANGUAGE="+values[b"parser_language"]+b"\nPARSER_STRUCTURE="+values[b"parser_structure"]+b"\nPARSER_SEMANTICS="+values[b"parser_semantics"]+b"\nCANDIDATE="+values[b"candidate"]+b"\nTERMINAL="+values[b"terminal"]+b"\nCERTIFICATE_EXPIRY_REALTIME_NS="+values[b"certificate_expiry_realtime_ns"]+b"\nTOPOLOGY=V15_INTERNAL_VALIDATION_REPORTED_BY_COMPLETE_TRANSCRIPT\nEXTERNAL_TOPOLOGY_RECONSTRUCTION=UNAVAILABLE\n")

def validated_record(context,values,ack_deadline):
 seq=next_record(context);origin=time.monotonic_ns();deadline=min(ack_deadline,origin+RECORD_NS);need(origin+RECORD_NS<=ack_deadline)
 body=(b"P27E001_PROBE_STATE_V15\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+context[b"chain_sha"]+b"\nORDINAL="+values[b"ordinal"]+b"\nPROBE="+values[b"probe"]+b"\nSTATE=VALIDATED_CANDIDATE\n"+forensic_body(values)+b"B_RECORD_ORIGIN_NS="+str(origin).encode()+b"\nB_RECORD_DEADLINE_NS="+str(deadline).encode()+b"\nRECORD_END=1\n")
 state,digest=durable_once(context,b"receipt-"+values[b"probe"]+b"-validated.v5",body,deadline,True,0,(b"VALIDATED",values[b"probe"])+tuple(values[key] for key in CANDIDATE_KEYS))
 if state!=DURABLE_VERIFIED:raise FaultSet({b"VALIDATED_DURABILITY_UNKNOWN"})
 context[b"chain_sha"]=digest;context[b"validated_sha"]=digest;context[b"validated_values"]=dict(values);return digest

def ack_intent_record(context,ordinal,probe,actor_ack,received,ack_deadline):
 values=context[b"validated_values"];seq=next_record(context);origin=time.monotonic_ns();deadline=min(ack_deadline,origin+RECORD_NS);need(origin+RECORD_NS<=ack_deadline)
 body=(b"P27E001_PROBE_STATE_V15\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+context[b"chain_sha"]+b"\nORDINAL="+str(ordinal).encode()+b"\nPROBE="+probe+b"\nSTATE=ACK_COMMIT_INTENT\n"+forensic_body(values)+b"ACTOR_ACK_INTENT_NS="+str(actor_ack).encode()+b"\nB_ACK_RECEIVED_NS="+str(received).encode()+b"\nB_RECORD_ORIGIN_NS="+str(origin).encode()+b"\nB_RECORD_DEADLINE_NS="+str(deadline).encode()+b"\nRECORD_END=1\n")
 state,digest=durable_once(context,b"receipt-"+probe+b"-ack-intent.v5",body,deadline,True,0,(b"ACK_INTENT",probe))
 if state!=DURABLE_VERIFIED:raise FaultSet({b"ACK_DURABILITY_UNKNOWN"})
 context[b"chain_sha"]=digest;return digest

def committed_record(context,ordinal,probe,ack_sha,committed_raw,reserved_control_seq,final_count,ack_deadline):
 need(context[b"chain_sha"]==ack_sha and final_count==sum(context[b"committed"])+1==ordinal+1)
 seq=next_record(context);origin=time.monotonic_ns();deadline=min(ack_deadline,origin+RECORD_NS);need(origin+RECORD_NS<=ack_deadline)
 body=(b"P27E001_PROBE_STATE_V15\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+ack_sha+b"\nORDINAL="+str(ordinal).encode()+b"\nPROBE="+probe+b"\nSTATE=COMMITTED\nACK_SHA256="+ack_sha+b"\nCOMMITTED_PACKET_SHA256="+sha(committed_raw)+b"\nCOMMITTED_PACKET_MESSAGE_SEQ="+str(reserved_control_seq).encode()+b"\nCOMMITTED_COUNT="+str(final_count).encode()+b"\nDIRECT_REAP_COUNT="+str(final_count).encode()+b"\nACK_DEADLINE_NS="+str(ack_deadline).encode()+b"\nB_RECORD_ORIGIN_NS="+str(origin).encode()+b"\nB_RECORD_DEADLINE_NS="+str(deadline).encode()+b"\nRECORD_END=1\n")
 state,digest=durable_once(context,b"receipt-"+probe+b"-committed.v15",body,deadline,True,0,(b"COMMITTED",str(ordinal).encode(),probe,sha(committed_raw),str(final_count).encode(),str(reserved_control_seq).encode()))
 if state!=DURABLE_VERIFIED:raise FaultSet({b"ACK_DURABILITY_UNKNOWN"})
 context[b"chain_sha"]=digest;context[b"last_committed_record_sha"]=digest;context[b"last_committed_packet_sha"]=sha(committed_raw);return digest

def committed_seen_record(context,ordinal,probe,seen_raw,committed_raw,commit_sha,ack_sha,final_count,host_complete,ack_deadline):
 need(time.monotonic_ns()<=ack_deadline and time.monotonic_ns()-host_complete<=ACK_NS)
 seq=next_record(context);predecessor=context[b"chain_sha"];need(predecessor==commit_sha)
 body=(b"P27E001_PROBE_STATE_V15\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+predecessor+b"\nORDINAL="+str(ordinal).encode()+b"\nPROBE="+probe+b"\nSTATE=COMMITTED_SEEN\nACK_SHA256="+ack_sha+b"\nCOMMIT_RECORD_SHA256="+commit_sha+b"\nCOMMITTED_PACKET_SHA256="+sha(committed_raw)+b"\nCOMMITTED_COUNT="+str(final_count).encode()+b"\nACTOR_SEEN_PACKET_SHA256="+sha(seen_raw)+b"\nACTOR_SEEN_MESSAGE_SEQ="+str(CONTROL_RECV_SEQ).encode()+b"\nHOST_COMPLETE_NS="+str(host_complete).encode()+b"\nACK_DEADLINE_NS="+str(ack_deadline).encode()+b"\nRECORD_END=1\n")
 state,digest=durable_once(context,b"receipt-"+probe+b"-committed-seen.v5",body,ack_deadline,True,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS,(b"COMMITTED_SEEN",str(ordinal).encode(),probe,sha(committed_raw),str(final_count).encode()))
 if state!=DURABLE_VERIFIED:raise FaultSet({b"ACK_DURABILITY_UNKNOWN"})
 context[b"chain_sha"]=digest;context[b"committed_seen_sha"]=digest;return digest

def populated(number):
 os.lseek(number,0,os.SEEK_SET);raw=os.read(number,4096)
 values=[x for x in raw.splitlines() if x.startswith(b"populated ")]
 need(len(values)==1 and values[0] in (b"populated 0",b"populated 1"));return values[0]==b"populated 1"

def observe_population(context):
 number=context.get(b"events_fd",-1)
 if number<0:number=context.get(b"root_events_fd",-1)
 if number<0:return False
 try:return populated(number)
 except BaseException:
  context[b"faults"].add(b"CONTAINMENT_OBSERVATION_UNKNOWN");return None

def drain(number,target):
 overflow=False;eof=False
 while True:
  try:chunk=os.read(number,65536)
  except BlockingIOError:break
  except InterruptedError:continue
  except BaseException as error:raise FaultSet({b"CAPTURE_IO"}) from error
  if chunk==b"":eof=True;break
  room=STREAM_CAP-len(target)
  if room>0:target.extend(chunk[:room])
 if len(chunk)>room:overflow=True
 return overflow,eof

def quarantine_scm_rights(context,ancillary,prefix,kind,limit):
 slots=[];numbers=[];bad=False
 try:
  for level,ctype,data in ancillary:
   if level!=socket.SOL_SOCKET or ctype!=socket.SCM_RIGHTS:bad=True;continue
   cells=array.array("i");whole=len(data)-(len(data)%cells.itemsize)
   if whole:cells.frombytes(data[:whole])
   if whole!=len(data):bad=True
   for number in cells:
    if len(slots)>=limit:
     strict_close_unadopted(number);bad=True;continue
    slot=prefix+str(len(slots)).encode();lifecycle_adopt_raw(context,slot,kind,number,False,(b"SCM_RIGHTS_QUARANTINE",prefix));slots.append(slot);numbers.append(number)
  return tuple(slots),tuple(numbers),bad
 except BaseException:
  close_lifecycle_slots(context,tuple(slots));raise

def recv_monitored(control,context,actor_pidfd,deadline,rights,actual_pre_state,ordinal,probe,received_slots=()):
 receiver_binding(actual_pre_state,ordinal,probe,deadline)
 need(type(received_slots)is tuple and len(received_slots)==rights and all(type(slot)is tuple and len(slot)==3 for slot in received_slots))
 checkpoint(CERT,0,deadline)
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR);need(actor_pidfd==context[b"actor_pidfd_fd"]);register_lifecycle_poller(context,poller,b"actor_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 while True:
  checkpoint(CERT,0,deadline);remaining=deadline-time.monotonic_ns()
  if remaining<=0:raise FaultSet({b"CONTROL_TIMEOUT"})
  try:events=poller.poll(max(1,min(50,(remaining+999999)//1000000)))
  except InterruptedError:continue
  cmask=0;amask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   if number==actor_pidfd:amask|=event
  if cmask&select.POLLIN:
   installed=();quarantine_slots=();promoted_slots=[];bad=False
   try:
    raw,ancillary,flags,address=control.recvmsg(65536,socket.CMSG_SPACE(MAX_RIGHTS*array.array("i").itemsize))
    quarantine_slots,installed,bad=quarantine_scm_rights(context,ancillary,b"unexpected_control_right_",b"UNEXPECTED_CONTROL_RIGHT",MAX_RIGHTS)
    checkpoint(CERT,0,deadline)
    if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})
    if flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC):raise FaultSet({b"CONTROL_TRUNCATION"})
    if address is not None or not raw:raise FaultSet({b"CONTROL_MALFORMED"})
    if bad:raise FaultSet({b"FD_TRANSFER"})
    if raw.startswith(b"V15_ABORT|"):
     binding=received_binding(raw,actual_pre_state,ordinal,probe,b"control_deadline_ns",deadline)
     values,faults=parse_abort(raw,b"A",binding)
     if installed or ancillary:faults.add(b"FD_TRANSFER")
     error=RemoteAbort(faults);error.values=values;raise error
    if rights==0:
     if installed or ancillary:raise FaultSet({b"FD_TRANSFER"})
    elif len(ancillary)!=1 or len(installed)!=rights:raise FaultSet({b"FD_TRANSFER"})
    if rights:
     for quarantine_slot,(slot,fd_kind,transferable) in zip(quarantine_slots,received_slots):
      promote_lifecycle_fd(context,quarantine_slot,slot,fd_kind,transferable,(b"SCM_RIGHTS_VALIDATED",actual_pre_state));promoted_slots.append(slot)
   return raw,tuple(installed)
   except BlockingIOError:
    close_lifecycle_slots(context,tuple(promoted_slots)+tuple(quarantine_slots))
    continue
   except BaseException:
    close_lifecycle_slots(context,tuple(promoted_slots)+tuple(quarantine_slots))
    raise
  if pidfd_ready_event(amask):raise PidfdActorLost("pidfd-ready")
  if cmask&(select.POLLHUP|select.POLLERR):raise ControlLost("control-hup")

def wait_sendable(control,deadline):
 context=ACTIVE_LIFECYCLE_CONTEXT;need(context is not None);poller=select.poll();poller.register(control.fileno(),select.POLLOUT|select.POLLHUP|select.POLLERR);register_lifecycle_poller(context,poller,b"actor_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 while True:
  checkpoint(CERT,0,deadline);remaining=deadline-time.monotonic_ns()
  if remaining<=0:raise FaultSet({b"CONTROL_TIMEOUT"})
  try:events=poller.poll(max(1,min(50,(remaining+999999)//1000000)))
  except InterruptedError:continue
  cmask=amask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   elif number==4:amask|=event
  if pidfd_ready_event(amask):raise PidfdActorLost("pidfd-ready")
  if cmask&select.POLLOUT:return
  if cmask&(select.POLLHUP|select.POLLERR):raise ControlLost("control-hup")

def send_exact(control,raw,deadline):
 global CONTROL_SEND_STATE
 while True:
  wait_sendable(control,deadline);CONTROL_SEND_STATE=b"SEND_EFFECT_UNKNOWN"
  try:count=control.send(raw)
  except BlockingIOError:continue
  except BaseException as error:raise SendEffectUnknown("send") from error
  if count!=len(raw):raise SendEffectUnknown("short-send")
  checkpoint(CERT,0,deadline)
  if time.monotonic_ns()>deadline:raise SendEffectUnknown("post-send-deadline")
  CONTROL_SEND_STATE=b"SENT";return

EXTERNAL_MAX_RIGHTS=13
EXTERNAL_RIGHTS_ORDER=(b"ATTEMPT_DIRFD",b"ATTEMPT_BASE_DIRFD",b"STAGE_DIRFD",b"CGROUP_DIRFD",b"ROOT_EVENTS_FD",b"ROOT_KILL_FD",b"OUT_FD",b"ERR_FD",b"EVENTS_FD",b"OUTER_PIDFD",b"CGROUP_BASE_DIRFD",b"ACTOR_CONTROL_FD",b"PENDING_EXPECTED_RAW_FD")
EXTERNAL_SLOT_ORDER=((b"ATTEMPT_DIRFD",b"attempt"),(b"ATTEMPT_BASE_DIRFD",b"attempt_base_fd"),(b"STAGE_DIRFD",b"stage_fd"),(b"CGROUP_DIRFD",b"cgfd"),(b"ROOT_EVENTS_FD",b"root_events_fd"),(b"ROOT_KILL_FD",b"root_kill_fd"),(b"OUT_FD",b"out_fd"),(b"ERR_FD",b"err_fd"),(b"EVENTS_FD",b"events_fd"),(b"OUTER_PIDFD",b"outer_pidfd"),(b"CGROUP_BASE_DIRFD",b"cgroup_base_fd"),(b"PENDING_EXPECTED_RAW_FD",b"pending_expected_raw_fd"))
OWNERSHIP_FD_KEYS=tuple(key for kind,key in EXTERNAL_SLOT_ORDER)
EXTERNAL_SPEC={
 b"REFUSAL_CLOSE_OFFER":(b"REFUSAL_SLOT_LOCKED",b"ISSUER_WAIT_REFUSAL",b"DEDICATED_REFUSAL_RECONCILIATION"),
 b"REFUSAL_CLOSE_ACCEPTED":(b"ISSUER_REFUSAL_DURABLE",b"B_WAIT_REFUSAL_ACCEPTED",b"DURABLE_NO_REPLAY_RECEIPT"),
 b"TRANSFER_OFFER":(b"FROZEN_EXTERNAL_TRANSFER",b"ISSUER_WAIT_TRANSFER",b"SCM_RIGHTS_TRANSFER"),
 b"TRANSFER_ACCEPTED":(b"ISSUER_OWNERSHIP_DURABLE",b"B_WAIT_TRANSFER_ACCEPTED",b"DURABLE_OWNERSHIP_RECEIPT")
}

def external_packet(kind,state,receiver,effect,deadline,pairs):
 global EXTERNAL_SEND_SEQ
 need(kind in EXTERNAL_SPEC and EXTERNAL_SPEC[kind]==(state,receiver,effect))
 values={}
 for key,value in pairs:
  need(key and value and key not in values and all(x not in key+value for x in (10,61,124)));values[key]=value
 EXTERNAL_SEND_SEQ+=1
 body=(b"P27E001_EXTERNAL_CONTROL_V15|kind="+kind+b"|protocol_version=14|session_id="+AUTH+b"|tx_sequence="+str(EXTERNAL_SEND_SEQ).encode()+b"|sender=B|sender_state="+state+b"|expected_receiver_state="+receiver+b"|effect_state="+effect+b"|absolute_deadline_ns="+str(deadline).encode())
 for key,value in pairs:body+=b"|"+key+b"="+value
 need(len(body)<65536);return body+b"\n"

def reserve_external_packet(kind,state,receiver,effect,deadline,pairs):
 global EXTERNAL_SEND_SEQ
 before=EXTERNAL_SEND_SEQ
 try:
  raw=external_packet(kind,state,receiver,effect,deadline,pairs);reserved=EXTERNAL_SEND_SEQ;need(reserved==before+1);return raw,reserved
 finally:
  if EXTERNAL_SEND_SEQ==before+1:EXTERNAL_SEND_SEQ=before

def activate_reserved_external_packet(raw,reserved):
 global EXTERNAL_SEND_SEQ
 need(type(raw)is bytes and raw.endswith(b"\n") and reserved==EXTERNAL_SEND_SEQ+1);EXTERNAL_SEND_SEQ=reserved;return raw

def parse_external(raw,kind,keys,expected_sequence,deadline):
 global EXTERNAL_RECV_SEQ
 need(type(raw)is bytes and raw.endswith(b"\n") and raw.count(b"\n")==1 and len(raw)<65536 and all(x==10 or 32<=x<=126 for x in raw))
 common=(b"kind",b"protocol_version",b"session_id",b"tx_sequence",b"sender",b"sender_state",b"expected_receiver_state",b"effect_state",b"absolute_deadline_ns")
 fields=raw[:-1].split(b"|");need(fields[0]==b"P27E001_EXTERNAL_CONTROL_V15" and len(fields)==1+len(common)+len(keys))
 values={}
 for key,item in zip(common+keys,fields[1:]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and parts[1] and key not in values);values[key]=parts[1]
 need(values[b"kind"]==kind and values[b"protocol_version"]==b"14" and values[b"session_id"]==AUTH and values[b"sender"]==b"ISSUER")
 need(values[b"sender_state"]==EXTERNAL_SPEC[kind][0] and values[b"expected_receiver_state"]==EXTERNAL_SPEC[kind][1] and values[b"effect_state"]==EXTERNAL_SPEC[kind][2])
 sequence=udec(values[b"tx_sequence"],1);need(sequence==expected_sequence and sequence==EXTERNAL_RECV_SEQ+1)
 need(udec(values[b"absolute_deadline_ns"],1)==deadline);return values

def commit_external_receive(sequence):
 global EXTERNAL_RECV_SEQ
 need(sequence==EXTERNAL_RECV_SEQ+1);EXTERNAL_RECV_SEQ=sequence

def external_send(control,context,raw,deadline,rights=()):
 need(len(rights)<=EXTERNAL_MAX_RIGHTS and len(set(rights))==len(rights) and all(type(x)is int and x>=0 for x in rights))
 ancillary=[] if not rights else [(socket.SOL_SOCKET,socket.SCM_RIGHTS,array.array("i",rights))]
 while True:
  checkpoint(CERT,0,deadline);now=time.monotonic_ns();need(now<=deadline)
  poller=select.poll();poller.register(control.fileno(),select.POLLOUT|select.POLLHUP|select.POLLERR);register_lifecycle_poller(context,poller,b"external_owner_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
  try:events=poller.poll(max(1,min(50,(deadline-now+999999)//1000000)))
  except InterruptedError:continue
  cmask=omask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   elif number==15:omask|=event
  if pidfd_ready_event(omask):context[b"external_owner_pidfd_exit_ready_observed"]=True;raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})
  if cmask&select.POLLOUT:
   try:count=control.sendmsg((raw,),ancillary)
   except BlockingIOError:continue
   except BaseException as error:raise SendEffectUnknown("external-send") from error
   if count!=len(raw):raise SendEffectUnknown("external-short-send")
   checkpoint(CERT,0,deadline);need(time.monotonic_ns()<=deadline);return
  if cmask&(select.POLLHUP|select.POLLERR):raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})

def external_recv(control,context,kind,keys,expected_sequence,deadline):
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR);register_lifecycle_poller(context,poller,b"external_owner_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 while True:
  checkpoint(CERT,0,deadline);now=time.monotonic_ns();need(now<=deadline)
  try:events=poller.poll(max(1,min(50,(deadline-now+999999)//1000000)))
  except InterruptedError:continue
  cmask=omask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   elif number==15:omask|=event
  if pidfd_ready_event(omask):context[b"external_owner_pidfd_exit_ready_observed"]=True;raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})
  if cmask&select.POLLIN:
   installed=();installed_slots=()
   try:
    raw,ancillary,flags,address=control.recvmsg(65536,socket.CMSG_SPACE(EXTERNAL_MAX_RIGHTS*array.array("i").itemsize))
    installed_slots,installed,bad=quarantine_scm_rights(context,ancillary,b"external_unexpected_right_",b"UNEXPECTED_EXTERNAL_RIGHT",EXTERNAL_MAX_RIGHTS)
    need(not bad and not installed and not ancillary and not flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC) and address is None)
    return parse_external(raw,kind,keys,expected_sequence,deadline)
   finally:close_lifecycle_slots(context,tuple(installed_slots))
  if cmask&(select.POLLHUP|select.POLLERR):raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})

EXTERNAL_RECEIPT_KEYS=(b"RECEIPT_KIND",b"OFFER_SHA256",b"RECORD_SEQ",b"PREDECESSOR_SHA256",b"RIGHTS_MANIFEST_SHA256",b"FINALITY_DEADLINE_NS",b"CLOSURE_DEADLINE_NS",b"RECEIVER_PID",b"RECEIVER_STARTTIME",b"NO_REPLAY")

def external_recv_receipt(control,context,kind,keys,expected_sequence,deadline):
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR);register_lifecycle_poller(context,poller,b"external_owner_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 while True:
  checkpoint(CERT,0,deadline);now=time.monotonic_ns();need(now<=deadline)
  try:events=poller.poll(max(1,min(50,(deadline-now+999999)//1000000)))
  except InterruptedError:continue
  cmask=omask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   elif number==15:omask|=event
  if pidfd_ready_event(omask):context[b"external_owner_pidfd_exit_ready_observed"]=True;raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})
  if cmask&select.POLLIN:
   installed=();installed_slots=()
   try:
    raw,ancillary,flags,address=control.recvmsg(65536,socket.CMSG_SPACE(array.array("i").itemsize))
    checkpoint(CERT,0,deadline);need(time.monotonic_ns()<=deadline)
    installed_slots,installed,bad=quarantine_scm_rights(context,ancillary,b"external_receipt_carrier_",b"EXTERNAL_RECEIPT_SEALED_CARRIER_FD",EXTERNAL_MAX_RIGHTS)
    need(not bad and len(installed)==1 and len(ancillary)==1 and not flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC) and address is None)
    receipt_raw=sealed_carrier(installed[0],65536);checkpoint(CERT,0,deadline);need(time.monotonic_ns()<=deadline)
    values=parse_external(raw,kind,keys,expected_sequence,deadline);checkpoint(CERT,0,deadline);need(time.monotonic_ns()<=deadline);return values,receipt_raw
   finally:close_lifecycle_slots(context,tuple(installed_slots))
  if cmask&(select.POLLHUP|select.POLLERR):raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})

def verify_external_acceptance(receipt_kind,offer,receipt_raw,values,sequence,predecessor,manifest_sha,finality_deadline,closure_deadline,verify_deadline):
 receipt=parse_fixed(receipt_raw,b"P27E001_EXTERNAL_DURABLE_RECEIPT_V15",EXTERNAL_RECEIPT_KEYS,b"RECEIPT_END=1")
 checkpoint(CERT,0,verify_deadline);need(time.monotonic_ns()<=verify_deadline)
 need(receipt[b"RECEIPT_KIND"]==receipt_kind and receipt[b"OFFER_SHA256"]==sha(offer) and udec(receipt[b"RECORD_SEQ"],1)==sequence)
 need(receipt[b"PREDECESSOR_SHA256"]==predecessor and receipt[b"RIGHTS_MANIFEST_SHA256"]==manifest_sha)
 need(udec(receipt[b"FINALITY_DEADLINE_NS"])==finality_deadline and udec(receipt[b"CLOSURE_DEADLINE_NS"])==closure_deadline and finality_deadline<closure_deadline)
 need(receipt[b"RECEIVER_PID"]==CERT[b"EXTERNAL_OWNER_PID"] and receipt[b"RECEIVER_STARTTIME"]==CERT[b"EXTERNAL_OWNER_STARTTIME"] and receipt[b"NO_REPLAY"]==b"1")
 need(udec(values[b"durable_receipt_bytes"],1)==len(receipt_raw) and values[b"durable_receipt_sha256"]==sha(receipt_raw))
 key_id=h64(values[b"issuer_key_id"]);need(key_id==ISSUER_KEY_ID);public_key=even_hex(values[b"issuer_public_key_hex"],32);need(len(public_key)==32)
 need(key_id==sha(ISSUER_KEY_BIND_DOMAIN+length_frame(b"ISSUER_PUBLIC_KEY",public_key)))
 checkpoint(CERT,0,verify_deadline);need(time.monotonic_ns()<=verify_deadline)
 preimage=EXTERNAL_ACCEPTANCE_DOMAIN+length_frame(b"OFFER_RAW",offer)+length_frame(b"DURABLE_RECEIPT_RAW",receipt_raw)+length_frame(b"ISSUER_KEY_ID",key_id)
 need(values[b"acceptance_preimage_sha256"]==sha(preimage));signature=even_hex(values[b"issuer_signature_hex"],64);need(len(signature)==64 and verify_ed25519(public_key,preimage,signature))
 checkpoint(CERT,0,verify_deadline);need(time.monotonic_ns()<=verify_deadline)
 return sha(receipt_raw)

def external_identity(kind,number,context):
 held=os.fstat(number)
 need(kind in EXTERNAL_RIGHTS_ORDER)
 access=fcntl.fcntl(number,fcntl.F_GETFL)&os.O_ACCMODE
 if kind==b"PENDING_EXPECTED_RAW_FD":
  pending=context.get(b"record_pending");need(pending is not None and context.get(b"record_sequence_frozen"))
  expected=context[b"durability_raw"][pending[2]];again=sealed_carrier(number,len(expected));delta_raw=semantic_delta_bytes(pending[4]);need(again==expected and sha(again)==pending[3] and access==os.O_RDWR)
  os.lseek(number,0,os.SEEK_SET);return kind+b":"+str(held.st_dev).encode()+b":"+str(held.st_ino).encode()+b":"+format(held.st_mode,"o").encode()+b":"+str(held.st_nlink).encode()+b":"+str(held.st_uid).encode()+b":"+str(held.st_gid).encode()+b":ACCESS="+str(access).encode()+b":SEALED="+str(EXACT_SEALS).encode()+b":BYTES="+str(len(expected)).encode()+b":SHA256="+pending[3]+b":SEMANTIC_DELTA_SHA256="+sha(delta_raw)
 if kind==b"OUTER_PIDFD":
  provenance=context.get(b"outer_pidfd_provenance");need(type(provenance)is tuple and len(provenance)==3 and provenance==(number,context[b"outer_pid"],context[b"outer_starttime"]))
  need(context.get(b"outer_pidfd_offer_state")==b"PRE_READY_CACHED_PROVENANCE_MATCHED")
  return kind+b":"+str(provenance[1]).encode()+b":"+str(provenance[2]).encode()+b":PIDFD:ACCESS="+str(access).encode()+b":PROVENANCE=PRE_EXIT_IMMUTABLE:EXIT_READY=0"
 if kind==b"ACTOR_CONTROL_FD":
  flags=fcntl.fcntl(number,fcntl.F_GETFL);need(stat.S_ISSOCK(held.st_mode) and flags&os.O_NONBLOCK)
  return kind+b":"+str(held.st_dev).encode()+b":"+str(held.st_ino).encode()+b":SOCK_SEQPACKET:ACCESS="+str(access).encode()+b":NONBLOCK=1"
 return kind+b":"+str(held.st_dev).encode()+b":"+str(held.st_ino).encode()+b":"+format(held.st_mode,"o").encode()+b":"+str(held.st_nlink).encode()+b":"+str(held.st_uid).encode()+b":"+str(held.st_gid).encode()+b":ACCESS="+str(access).encode()

def external_capabilities(control,context):
 result=ownership_transfer_keys(context);kinds=tuple(item[0] for item in result);slots=tuple(item[1] for item in result)
 need(result and len(result)<=EXTERNAL_MAX_RIGHTS and len(set(kinds))==len(kinds)==len(set(slots)))
 need(tuple(EXTERNAL_RIGHTS_ORDER.index(kind) for kind in kinds)==tuple(sorted(EXTERNAL_RIGHTS_ORDER.index(kind) for kind in kinds)))
 actor=tuple(item for item in result if item[0]==b"ACTOR_CONTROL_FD")
 if actor:need(len(actor)==1 and control is not None and control.fileno()==actor[0][2])
 if context.get(b"record_pending") is not None:need(any(item[0]==b"PENDING_EXPECTED_RAW_FD" for item in result))
 required=bool(context.get(b"containment_bound"));need(sum(1 for item in result if item[0]==b"ROOT_KILL_FD")== (1 if required else 0) and unique_kill_authority(context,required))
 return result

def registry_transfer_set_bytes(caps):
 need(type(caps)is tuple)
 return b"".join(b"KIND="+kind+b";SLOT="+slot+b";IDENTITY_SHA256="+sha(identity)+b"\n" for kind,slot,number,identity in caps)

def assert_registry_transfer_set(context,caps):
 current=ownership_transfer_keys(context);need(current==caps and registry_transfer_set_bytes(current)==registry_transfer_set_bytes(caps));unique_kill_authority(context,bool(context.get(b"containment_bound")));return current

def actor_pidfd_provenance(context):
 provenance=context.get(b"actor_pidfd_provenance")
 need(type(provenance)is tuple and len(provenance)==3 and provenance==(4,ACTOR_PID,ACTOR_STARTTIME) and ACTOR_PID>=2 and ACTOR_STARTTIME>=1)
 return provenance

def offer_readiness_snapshot(context):
 actor=actor_pidfd_provenance(context);external=context.get(b"external_owner_pidfd_provenance");need(type(external)is tuple and len(external)==3 and external[0]==15)
 actor_ready=bool(context.get(b"actor_pidfd_exit_ready_observed"));outer_ready=bool(context.get(b"pidfd_exit_ready_observed"));external_ready=bool(context.get(b"external_owner_pidfd_exit_ready_observed"))
 outer_number=context.get(b"outer_pidfd",-1)
 for number,event in context[b"offer_snapshot_poller"].poll(0):
  need(not event&select.POLLNVAL)
  if number==actor[0]:actor_ready=True
  elif number==external[0]:external_ready=True
  elif outer_number>=0 and number==outer_number:outer_ready=True
 return actor_ready,outer_ready,external_ready

def apply_offer_readiness(context,snapshot,deadline):
 actor_ready,outer_ready,external_ready=snapshot
 if actor_ready and not context.get(b"actor_pidfd_exit_ready_observed"):mark_actor_pidfd_lost(context)
 if external_ready:
  context[b"external_owner_pidfd_exit_ready_observed"]=True;raise RefusalFinalityPending("external-owner-pidfd-ready-no-takeover")
 number=context.get(b"outer_pidfd",-1)
 if outer_ready and number>=0:
  provenance=context.get(b"outer_pidfd_provenance");release_identity=context.get(b"outer_release_record_identity")
  need(provenance==(number,context[b"outer_pid"],context[b"outer_starttime"]) and type(release_identity)is tuple and len(release_identity)==3 and h64(release_identity[0])==release_identity[0] and release_identity[0]!=EMPTY_SHA)
  context[b"pidfd_exit_ready_observed"]=True;context[b"outer_pidfd_offer_state"]=b"POST_READY_CACHED_PROVENANCE";checkpoint(CERT,0,deadline);need(time.monotonic_ns()<=deadline)
  if context.get(b"offer_snapshot_outer_fd")==number:context[b"offer_snapshot_poller"].unregister(number);context[b"offer_snapshot_outer_fd"]=-1
  context[b"outer_pidfd_close_state"]=b"CLOSE_EFFECT_UNKNOWN"
  try:close_lifecycle_fd(context,b"outer_pidfd")
  except OwnershipClosePending:
   context[b"outer_pidfd_close_state"]=b"CLOSE_RECONCILIATION_HOLD";raise
  context[b"outer_pidfd_close_state"]=b"OMITTED_EXIT_READY_LOCAL_CLOSED"
 return True

def promote_later_offer_readiness(context,snapshot):
 actor_ready,outer_ready,external_ready=snapshot
 if actor_ready and not context.get(b"actor_pidfd_exit_ready_observed"):mark_actor_pidfd_lost(context)
 if outer_ready and context.get(b"outer_pidfd",-1)>=0:
  context[b"pidfd_exit_ready_observed"]=True;context[b"outer_pidfd_offer_state"]=b"POST_OFFER_READY_LOCAL_RETAINED_UNTIL_ACCEPTED_CLOSE"
 if external_ready:
  context[b"external_owner_pidfd_exit_ready_observed"]=True;raise RefusalFinalityPending("external-owner-pidfd-ready-before-acceptance-commit")
 return True

def prepare_outer_pidfd_offer_binding(context,deadline):
 need(context.get(b"transfer_offer_cache") is None and time.monotonic_ns()<=deadline);actor=actor_pidfd_provenance(context);external=context.get(b"external_owner_pidfd_provenance");need(type(external)is tuple and len(external)==3 and external[0]==15)
 number=context.get(b"outer_pidfd",-1);pid=context.get(b"outer_pid",-1);start=context.get(b"outer_starttime",0);release_identity=context.get(b"outer_release_record_identity")
 if number<0:
  need(context.get(b"outer_pidfd_close_state") in (b"NOT_BOUND",b"CLOSED_NORMAL",b"OMITTED_EXIT_READY_LOCAL_CLOSED"))
  if context.get(b"outer_pidfd_close_state")==b"OMITTED_EXIT_READY_LOCAL_CLOSED":
   need(context.get(b"pidfd_exit_ready_observed") and type(release_identity)is tuple and len(release_identity)==3 and h64(release_identity[0])==release_identity[0])
   state=b"POST_READY_OMITTED_LOCAL_CLOSED";right_present=b"0"
  else:state=b"NOT_BOUND";right_present=b"0";pid=-1;start=0;release_identity=(EMPTY_SHA,b"NONE",b"NONE")
 else:
  provenance=context.get(b"outer_pidfd_provenance");need(provenance==(number,pid,start) and pid>=2 and start>=1)
  need(not context[b"pidfd_exit_ready_observed"]);context[b"outer_pidfd_offer_state"]=b"PRE_READY_CACHED_PROVENANCE_MATCHED";state=b"PRE_READY_CACHED_PROVENANCE_MATCHED";right_present=b"1"
  if release_identity is None:release_identity=(EMPTY_SHA,b"NONE",b"NONE")
 need(type(release_identity)is tuple and len(release_identity)==3)
 binding=(str(actor[1]).encode(),str(actor[2]).encode(),b"1" if context.get(b"actor_pidfd_exit_ready_observed") else b"0",str(external[1]).encode(),str(external[2]).encode(),b"1" if context.get(b"external_owner_pidfd_exit_ready_observed") else b"0",str(pid).encode(),str(start).encode(),state,b"1" if context.get(b"pidfd_exit_ready_observed") else b"0",release_identity[0],release_identity[1],release_identity[2],right_present)
 context[b"outer_pidfd_offer_state"]=state;context[b"outer_offer_binding"]=binding;return binding

def ownership_transfer_keys(context):
 rows=[];seen=set()
 for slot,entry in context[b"fd_registry"].items():
  if entry[6] and entry[4]:
   need(entry[0] in LIFECYCLE_TRANSFER_ORDER and entry[7]==LIFECYCLE_TRANSFER_ORDER[entry[0]] and entry[0] not in seen);seen.add(entry[0]);rows.append((entry[7],entry[0],slot,entry[1],external_identity(entry[0],entry[1],context)))
 rows.sort();need(tuple(row[0] for row in rows)==tuple(sorted(row[0] for row in rows)))
 return tuple((kind,slot,number,identity) for order,kind,slot,number,identity in rows)

def ownership_capabilities_closed(context):
 if context[b"ownership_closed_monotone"]:return True
 closed=all(not entry[6] for entry in context[b"fd_registry"].values())
 if closed:context[b"ownership_closed_monotone"]=True;context[b"ownership_close_complete"]=True
 return closed

def close_ownership_capabilities(context,deadline,offered=None):
 mode=b"GENERIC_ACCEPTED" if offered is not None else (b"REFUSAL_ACCEPTED" if context.get(b"refusal_acceptance_state")==b"COMMITTED" else b"DIRECT_TERMINAL")
 if not context[b"ownership_close_started"]:
  if offered is not None:
   frozen=tuple((kind,key,number,identity) for kind,key,number,identity in offered);need(frozen==ownership_transfer_keys(context));context[b"ownership_closure_offer"]=frozen
  else:
   need(context.get(b"record_pending") is None and not context.get(b"record_sequence_frozen") and context.get(b"pending_expected_raw_fd",-1)<0);context[b"ownership_closure_offer"]=()
  if deadline is not None:checkpoint(CERT,0,deadline);need(time.monotonic_ns()<=deadline)
  non_endpoints=tuple(slot for slot,entry in context[b"fd_registry"].items() if entry[6] and slot not in (b"actor_control_fd",b"transfer_control_fd"))
  endpoints=tuple(slot for slot in (b"actor_control_fd",b"transfer_control_fd") if context[b"fd_registry"][slot][6])
  context[b"ownership_close_plan"]=non_endpoints+endpoints;context[b"ownership_close_cursor"]=0;context[b"ownership_close_mode"]=mode;context[b"ownership_close_started"]=True
 else:
  need(context[b"ownership_close_mode"]==mode or offered is None)
  if offered is not None:need(context[b"ownership_closure_offer"]==tuple((kind,key,number,identity) for kind,key,number,identity in offered))
 plan=context[b"ownership_close_plan"]
 while context[b"ownership_close_cursor"]<len(plan):
  index=context[b"ownership_close_cursor"];slot=plan[index];entry=context[b"fd_registry"][slot]
  if entry[6]:close_lifecycle_fd(context,slot)
  need(not context[b"fd_registry"][slot][6]);context[b"ownership_close_cursor"]=index+1
 need(context[b"ownership_close_cursor"]==len(plan) and ownership_capabilities_closed(context));return True

def complete_started_ownership_close(context):
 need(context[b"ownership_close_started"] and not context[b"owner_released"])
 close_ownership_capabilities(context,None)
 need(context[b"ownership_close_complete"] and ownership_capabilities_closed(context))
 mode=context[b"ownership_close_mode"]
 if mode==b"GENERIC_ACCEPTED":need(context[b"transfer_acceptance_state"]==b"COMMITTED");context[b"transfer_capabilities_closed"]=True;context[b"transfer_state"]=b"TRANSFER_ACCEPTED_CAPABILITIES_CLOSED_OWNER_RELEASED"
 elif mode==b"REFUSAL_ACCEPTED":need(context[b"refusal_acceptance_state"]==b"COMMITTED");context[b"refusal_capabilities_closed"]=True;context[b"refusal_offer_state"]=b"OWNER_RELEASED_AFTER_DURABLE_ACCEPTANCE_AND_CAPABILITY_CLOSE"
 else:context[b"terminal_phase"]=b"DIRECT_CURSOR_CAPABILITIES_CLOSED_OWNER_RELEASED"
 context[b"owner_released"]=True;return True

def pending_transfer_manifest(context):
 pending=context.get(b"record_pending")
 if pending is None:return b"NOT_APPLICABLE"
 seq,predecessor,name,digest,semantic_delta=pending;raw=context[b"durability_raw"][name];delta_raw=semantic_delta_bytes(semantic_delta)
 need(context.get(b"record_sequence_frozen") and context.get(b"pending_expected_raw_fd",-1)>=0 and sha(raw)==digest)
 return (b"P27E001_PENDING_RECORD_MANIFEST_V15\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+str(seq).encode()+b"\nPREDECESSOR_SHA256="+predecessor+b"\nENTRY_NAME_HEX="+name.hex().encode()+b"\nEXPECTED_RAW_BYTES="+str(len(raw)).encode()+b"\nEXPECTED_RAW_SHA256="+digest+b"\nSEMANTIC_DELTA_BYTES="+str(len(delta_raw)).encode()+b"\nSEMANTIC_DELTA_SHA256="+sha(delta_raw)+b"\nSEMANTIC_DELTA_HEX="+delta_raw.hex().encode()+b"\nCARRIER_RIGHT=PENDING_EXPECTED_RAW_FD\nCARRIER_CONTRACT=ANONYMOUS_SEALED_O_RDWR_NLINK0\nNO_SUCCESSOR=1\nPENDING_END=1\n")

REFUSAL_SLOT_VARIANTS=(b"ACK_NOT_CONSTRUCTED",b"ACK_CACHED_PRE_CLOSE",b"CLOSE_EFFECT_UNKNOWN",b"ACK_READY_CLOSED",b"ACK_EFFECT_UNKNOWN",b"WAITING_RECEIPT",b"RECEIPT_VERIFIED",b"ACTOR_LOSS_DRAINED",b"FINALITY_CAP_EXPIRED_HOLD")
REFUSAL_CLOSE_STATES=(b"CLOSE_NOT_ATTEMPTED",b"CLOSE_EFFECT_UNKNOWN",b"CLOSED_NO_CONSUME")
REFUSAL_FINALITY_STATES=(b"OPEN",b"RECEIPT_VERIFIED_FINAL",b"ACTOR_LOSS_CONTROL_EOF_FINAL",b"CAP_EXPIRED_HOLD")
REFUSAL_RECEIPT_KEYS=(b"state",b"ordinal",b"probe",b"ack_packet_sha256",b"ack_message_seq",b"request_packet_sha256",b"cross_map_state",b"no_replay",b"refusal_finality_deadline_ns",b"refusal_closure_deadline_ns",b"refusal_schedule_hex",b"consume_deadline_ns")
REFUSAL_CANDIDATE_EVIDENCE_MAX=8
REFUSAL_CLOSURE_PHASES=(b"REFUSAL_OFFER_BUILD",b"REFUSAL_OFFER_SEND",b"REFUSAL_ACCEPTANCE_RECV",b"REFUSAL_ACCEPTANCE_VERIFY",b"REFUSAL_ACCEPTANCE_COMMIT",b"REFUSAL_ACTOR_CLOSURE",b"REFUSAL_CAPABILITY_CLOSE",b"REFUSAL_CLOSURE")

def refusal_slot_pack(core,variant,close_state,ack_raw=b"",ack_sequence=0,receipt_raw=b"",receipt_sequence=0,finality_state=b"OPEN",finality_evidence=b"",offer=b"",contract=b"",offer_send_sequence=0):
 need(type(core)is tuple and len(core)==8 and variant in REFUSAL_SLOT_VARIANTS and close_state in REFUSAL_CLOSE_STATES and finality_state in REFUSAL_FINALITY_STATES)
 seq,predecessor,request_raw,request_kind,claims,schedule_items,finality_deadline,closure_deadline=core
 need(type(seq)is int and seq>=1 and h64(predecessor)==predecessor and type(request_raw)is bytes and request_raw.endswith(b"\n"))
 need(request_kind in (b"V15_REFUSE_PREBEGIN",b"V15_REFUSE_POSTARM") and type(claims)is tuple and len(claims)==9 and all(type(item)is bytes and item for item in claims))
 request_sha,request_sequence,a_begin,a_arm,cross_map,origin_raw,finality_raw,closure_raw,schedule_claim=claims
 need(request_sha==sha(request_raw));udec(request_sequence,1);origin=udec(origin_raw,1)
 need(udec(finality_raw,1)==finality_deadline and udec(closure_raw,1)==closure_deadline and finality_deadline<closure_deadline)
 need(type(schedule_items)is tuple and len(schedule_items)==len(REFUSAL_PHASE_SPEC) and all(type(name)is bytes and type(value)is int for name,value in schedule_items))
 schedule={name:value for name,value in schedule_items};need(schedule_items==tuple((name,schedule[name]) for name,cap in REFUSAL_PHASE_SPEC))
 need(schedule==exact_schedule(origin,closure_deadline,REFUSAL_PHASE_SPEC) and finality_deadline==schedule[b"REFUSAL_FINALITY"]==origin+REFUSAL_FINALITY_NS)
 need(closure_deadline==schedule[b"REFUSAL_CLOSURE"] and closure_deadline-finality_deadline==REFUSAL_CLOSURE_TAIL_NS and schedule_claim==schedule_hex(schedule,REFUSAL_PHASE_SPEC))
 if ack_raw==b"":
  need(ack_sequence==0 and close_state==b"CLOSE_NOT_ATTEMPTED" and variant in (b"ACK_NOT_CONSTRUCTED",b"ACTOR_LOSS_DRAINED",b"FINALITY_CAP_EXPIRED_HOLD"))
 else:
  need(type(ack_raw)is bytes and ack_raw.endswith(b"\n") and type(ack_sequence)is int and ack_sequence>=1 and variant!=b"ACK_NOT_CONSTRUCTED")
 if variant==b"ACK_CACHED_PRE_CLOSE":need(close_state==b"CLOSE_NOT_ATTEMPTED")
 if variant==b"CLOSE_EFFECT_UNKNOWN":need(close_state==b"CLOSE_EFFECT_UNKNOWN")
 if variant in (b"ACK_READY_CLOSED",b"ACK_EFFECT_UNKNOWN",b"WAITING_RECEIPT",b"RECEIPT_VERIFIED"):need(close_state==b"CLOSED_NO_CONSUME")
 need(type(receipt_sequence)is int and receipt_sequence>=0 and type(finality_evidence)is bytes)
 if finality_state==b"OPEN":
  need(receipt_raw==b"" and receipt_sequence==0 and finality_evidence==b"" and variant not in (b"RECEIPT_VERIFIED",b"ACTOR_LOSS_DRAINED",b"FINALITY_CAP_EXPIRED_HOLD"))
 elif finality_state==b"RECEIPT_VERIFIED_FINAL":
  need(variant==b"RECEIPT_VERIFIED" and type(receipt_raw)is bytes and receipt_raw.endswith(b"\n") and receipt_sequence>=1 and finality_evidence.endswith(b"\n"))
 elif finality_state==b"ACTOR_LOSS_CONTROL_EOF_FINAL":
  need(variant==b"ACTOR_LOSS_DRAINED" and receipt_raw==b"" and receipt_sequence==0 and finality_evidence.endswith(b"\n"))
 else:
  need(variant==b"FINALITY_CAP_EXPIRED_HOLD" and receipt_raw==b"" and receipt_sequence==0 and finality_evidence.endswith(b"\n"))
 empty_offer=offer==b"" and contract==b"" and offer_send_sequence==0
 full_offer=type(offer)is bytes and offer.endswith(b"\n") and type(contract)is bytes and contract.endswith(b"\n") and type(offer_send_sequence)is int and offer_send_sequence>=1
 need(empty_offer or full_offer)
 if full_offer:
  need(finality_state in (b"RECEIPT_VERIFIED_FINAL",b"ACTOR_LOSS_CONTROL_EOF_FINAL"))
  if finality_state==b"RECEIPT_VERIFIED_FINAL":need(close_state==b"CLOSED_NO_CONSUME" and ack_raw)
 state_payload=(b"P27E001_REFUSAL_SLOT_STATE_V15\nRECORD_SEQ="+str(seq).encode()+b"\nPREDECESSOR_SHA256="+predecessor+b"\nREQUEST_KIND="+request_kind+b"\nREQUEST_SHA256="+request_sha+b"\nREQUEST_MESSAGE_SEQ="+request_sequence+b"\nA_BEGIN_STATE="+a_begin+b"\nA_ARM_STATE="+a_arm+b"\nCROSS_MAP_STATE="+cross_map+b"\nREFUSAL_ORIGIN_NS="+origin_raw+b"\nREFUSAL_FINALITY_DEADLINE_NS="+finality_raw+b"\nREFUSAL_CLOSURE_DEADLINE_NS="+closure_raw+b"\nREFUSAL_CLOSURE_TAIL_NS="+str(REFUSAL_CLOSURE_TAIL_NS).encode()+b"\nREFUSAL_SCHEDULE_HEX="+schedule_claim+b"\nCLOSE_STATE="+close_state+b"\nSLOT_VARIANT="+variant+b"\nACK_SEQUENCE="+str(ack_sequence).encode()+b"\nACK_BYTES="+str(len(ack_raw)).encode()+b"\nACK_SHA256="+(sha(ack_raw) if ack_raw else EMPTY_SHA)+b"\nRECEIPT_SEQUENCE="+str(receipt_sequence).encode()+b"\nRECEIPT_BYTES="+str(len(receipt_raw)).encode()+b"\nRECEIPT_SHA256="+(sha(receipt_raw) if receipt_raw else EMPTY_SHA)+b"\nFINALITY_STATE="+finality_state+b"\nFINALITY_EVIDENCE_BYTES="+str(len(finality_evidence)).encode()+b"\nFINALITY_EVIDENCE_SHA256="+(sha(finality_evidence) if finality_evidence else EMPTY_SHA)+b"\n"+length_frame(b"REQUEST_RAW",request_raw)+length_frame(b"ACK_RAW",ack_raw)+length_frame(b"AUTHORITATIVE_RECEIPT_RAW",receipt_raw)+length_frame(b"FINALITY_EVIDENCE_RAW",finality_evidence)+b"STATE_END=1\n")
 return (b"REFUSAL_SLOT_V15",core,variant,close_state,ack_raw,ack_sequence,receipt_raw,receipt_sequence,finality_state,finality_evidence,offer,sha(offer) if offer else EMPTY_SHA,contract,sha(contract) if contract else EMPTY_SHA,offer_send_sequence,sha(state_payload))

def refusal_slot(context):
 cached=context.get(b"refusal_offer_cache");need(context.get(b"refusal_slot_locked",False) and cached is not None and type(cached)is tuple and len(cached)==16 and cached[0]==b"REFUSAL_SLOT_V15")
 tag,core,variant,close_state,ack_raw,ack_sequence,receipt_raw,receipt_sequence,finality_state,finality_evidence,offer,offer_sha,contract,contract_sha,offer_send_sequence,state_digest=cached
 need(refusal_slot_pack(core,variant,close_state,ack_raw,ack_sequence,receipt_raw,receipt_sequence,finality_state,finality_evidence,offer,contract,offer_send_sequence)==cached)
 need(context[b"refusal_close_state"]==close_state and context[b"refusal_finality_state"]==finality_state)
 if offer:need(offer_sha==sha(offer) and contract_sha==sha(contract))
 return cached

def refusal_lock_invariant(context):
 locked=context.get(b"refusal_slot_locked",False);cached=context.get(b"refusal_offer_cache")
 need((locked and cached is not None) or (not locked and cached is None))
 if locked:refusal_slot(context)
 return locked

def stage_refusal_slot(context,request_raw,request_kind,values,refusal_schedule):
 need(not refusal_lock_invariant(context) and context[b"transfer_offer_cache"] is None)
 seq=context[b"external_record_seq"]+1;predecessor=context[b"external_chain_sha"]
 finality_deadline=refusal_schedule[b"REFUSAL_FINALITY"];closure_deadline=refusal_schedule[b"REFUSAL_CLOSURE"]
 claims=(values[b"packet_sha256"],values[b"message_seq"],values[b"a_begin_state"],values[b"a_arm_state"],values[b"cross_map_state"],values[b"refusal_origin_ns"],values[b"refusal_finality_deadline_ns"],values[b"refusal_closure_deadline_ns"],values[b"refusal_schedule_hex"])
 schedule_items=tuple((name,refusal_schedule[name]) for name,cap in REFUSAL_PHASE_SPEC)
 core=(seq,predecessor,request_raw,request_kind,claims,schedule_items,finality_deadline,closure_deadline)
 staged=refusal_slot_pack(core,b"ACK_NOT_CONSTRUCTED",b"CLOSE_NOT_ATTEMPTED")
 context.update({b"refusal_offer_cache":staged,b"refusal_slot_locked":True,b"refusal_close_state":b"CLOSE_NOT_ATTEMPTED",b"refusal_finality_state":b"OPEN",b"refusal_offer_state":b"STAGED_ACK_NOT_CONSTRUCTED_NO_CLOSE_NO_GENERIC"})
 refusal_lock_invariant(context);return staged

def refusal_slot_update(context,variant=None,close_state=None,ack_raw=None,ack_sequence=None,receipt_raw=None,receipt_sequence=None,finality_state=None,finality_evidence=None,offer=None,contract=None,offer_send_sequence=None):
 cached=refusal_slot(context);tag,core,old_variant,old_close,old_ack,old_ack_sequence,old_receipt,old_receipt_sequence,old_finality,old_evidence,old_offer,old_offer_sha,old_contract,old_contract_sha,old_offer_sequence,state_digest=cached
 allowed={
  b"ACK_NOT_CONSTRUCTED":(b"ACK_NOT_CONSTRUCTED",b"ACK_CACHED_PRE_CLOSE",b"ACTOR_LOSS_DRAINED",b"FINALITY_CAP_EXPIRED_HOLD"),
  b"ACK_CACHED_PRE_CLOSE":(b"ACK_CACHED_PRE_CLOSE",b"CLOSE_EFFECT_UNKNOWN",b"ACTOR_LOSS_DRAINED",b"FINALITY_CAP_EXPIRED_HOLD"),
  b"CLOSE_EFFECT_UNKNOWN":(b"CLOSE_EFFECT_UNKNOWN",b"ACK_READY_CLOSED",b"ACTOR_LOSS_DRAINED",b"FINALITY_CAP_EXPIRED_HOLD"),
  b"ACK_READY_CLOSED":(b"ACK_READY_CLOSED",b"ACK_EFFECT_UNKNOWN",b"ACTOR_LOSS_DRAINED",b"FINALITY_CAP_EXPIRED_HOLD"),
  b"ACK_EFFECT_UNKNOWN":(b"ACK_EFFECT_UNKNOWN",b"WAITING_RECEIPT",b"RECEIPT_VERIFIED",b"ACTOR_LOSS_DRAINED",b"FINALITY_CAP_EXPIRED_HOLD"),
  b"WAITING_RECEIPT":(b"WAITING_RECEIPT",b"RECEIPT_VERIFIED",b"ACTOR_LOSS_DRAINED",b"FINALITY_CAP_EXPIRED_HOLD"),
  b"RECEIPT_VERIFIED":(b"RECEIPT_VERIFIED",),
  b"ACTOR_LOSS_DRAINED":(b"ACTOR_LOSS_DRAINED",),
  b"FINALITY_CAP_EXPIRED_HOLD":(b"FINALITY_CAP_EXPIRED_HOLD",)
 }
 new_variant=old_variant if variant is None else variant;need(new_variant in allowed[old_variant])
 new_close=old_close if close_state is None else close_state
 need((old_close,new_close) in ((b"CLOSE_NOT_ATTEMPTED",b"CLOSE_NOT_ATTEMPTED"),(b"CLOSE_NOT_ATTEMPTED",b"CLOSE_EFFECT_UNKNOWN"),(b"CLOSE_EFFECT_UNKNOWN",b"CLOSE_EFFECT_UNKNOWN"),(b"CLOSE_EFFECT_UNKNOWN",b"CLOSED_NO_CONSUME"),(b"CLOSED_NO_CONSUME",b"CLOSED_NO_CONSUME")))
 new_ack=old_ack if ack_raw is None else ack_raw;new_ack_sequence=old_ack_sequence if ack_sequence is None else ack_sequence
 if old_ack:need((new_ack,new_ack_sequence)==(old_ack,old_ack_sequence))
 new_receipt=old_receipt if receipt_raw is None else receipt_raw;new_receipt_sequence=old_receipt_sequence if receipt_sequence is None else receipt_sequence
 if old_receipt:need((new_receipt,new_receipt_sequence)==(old_receipt,old_receipt_sequence))
 new_finality=old_finality if finality_state is None else finality_state;new_evidence=old_evidence if finality_evidence is None else finality_evidence
 need((old_finality==b"OPEN" and new_finality in REFUSAL_FINALITY_STATES) or (old_finality==new_finality and old_evidence==new_evidence))
 new_offer=old_offer if offer is None else offer;new_contract=old_contract if contract is None else contract;new_offer_sequence=old_offer_sequence if offer_send_sequence is None else offer_send_sequence
 if old_offer:
  need((new_variant,new_close,new_ack,new_ack_sequence,new_receipt,new_receipt_sequence,new_finality,new_evidence)==(old_variant,old_close,old_ack,old_ack_sequence,old_receipt,old_receipt_sequence,old_finality,old_evidence))
  need((new_offer,new_contract,new_offer_sequence)==(old_offer,old_contract,old_offer_sequence))
 return refusal_slot_pack(core,new_variant,new_close,new_ack,new_ack_sequence,new_receipt,new_receipt_sequence,new_finality,new_evidence,new_offer,new_contract,new_offer_sequence)

def refusal_slot_transition(context,variant=None,close_state=None,ack_raw=None,ack_sequence=None,receipt_raw=None,receipt_sequence=None,finality_state=None,finality_evidence=None,offer=None,contract=None,offer_send_sequence=None):
 updated=refusal_slot_update(context,variant,close_state,ack_raw,ack_sequence,receipt_raw,receipt_sequence,finality_state,finality_evidence,offer,contract,offer_send_sequence)
 context.update({b"refusal_offer_cache":updated,b"refusal_close_state":updated[3],b"refusal_finality_state":updated[8]})
 refusal_lock_invariant(context);return updated

def refusal_schedule_from_core(core):
 schedule={name:value for name,value in core[5]}
 need(schedule[b"REFUSAL_FINALITY"]==core[6] and schedule[b"REFUSAL_CLOSURE"]==core[7] and core[7]-core[6]==REFUSAL_CLOSURE_TAIL_NS)
 return schedule

def refusal_stage_window(context,name):
 cached=refusal_slot(context);need(name in REFUSAL_CLOSURE_PHASES);core=cached[1];schedule=refusal_schedule_from_core(core)
 names=tuple(item[0] for item in REFUSAL_PHASE_SPEC);index=names.index(name);cap=REFUSAL_PHASE_SPEC[index][1]
 stage_deadline=schedule[name];latest_safe_start=stage_deadline-cap;reserve_after=core[7]-stage_deadline
 need(cap>0 and reserve_after==sum(item[1] for item in REFUSAL_PHASE_SPEC[index+1:]) and time.monotonic_ns()<=latest_safe_start)
 checkpoint(CERT,0,stage_deadline);need(time.monotonic_ns()<=stage_deadline)
 return stage_deadline,latest_safe_start,reserve_after

def refusal_candidate_fault(context,raw,reason):
 need(type(raw)is bytes and reason in (b"TRANSPORT_REJECTED",b"SEMANTIC_REJECTED",b"POST_FINAL_REPLAY",b"POST_FINALITY_NONAUTHORITATIVE"))
 digest=sha(b"P27E001_REFUSAL_CANDIDATE_FAULT_V15\x00"+reason+b"\x00"+str(len(raw)).encode()+b"\x00"+raw)
 evidence=context[b"refusal_candidate_fault_evidence"]
 if len(evidence)<REFUSAL_CANDIDATE_EVIDENCE_MAX:context[b"refusal_candidate_fault_evidence"]=evidence+(digest,)
 else:context[b"refusal_candidate_fault_overflow"]+=1
 return digest

def refusal_candidate_fault_digest(context):
 evidence=context[b"refusal_candidate_fault_evidence"];overflow=context[b"refusal_candidate_fault_overflow"]
 raw=b"P27E001_REFUSAL_CANDIDATE_EVIDENCE_V15\nCOUNT="+str(len(evidence)).encode()+b"\nOVERFLOW="+str(overflow).encode()+b"\n"+b"".join(b"EVIDENCE_SHA256="+item+b"\n" for item in evidence)+b"EVIDENCE_END=1\n"
 return sha(raw)

def parse_refusal_receipt_candidate(context,receipt_raw):
 cached=refusal_slot(context);need(cached[2] in (b"ACK_EFFECT_UNKNOWN",b"WAITING_RECEIPT") and cached[4] and cached[6]==b"" and cached[8]==b"OPEN" and cached[10]==b"")
 core=cached[1];ack_raw=cached[4];ack_sequence=cached[5];seq,predecessor,request_raw,request_kind,claims,schedule_items,finality_deadline,closure_deadline=core
 request_sha,request_sequence,a_begin,a_arm,cross_map,origin_raw,finality_raw,closure_raw,schedule_claim=claims;schedule={name:value for name,value in schedule_items};receipt_deadline=finality_deadline
 checkpoint(CERT,0,finality_deadline);need(time.monotonic_ns()<=finality_deadline)
 need(type(receipt_raw)is bytes and receipt_raw.endswith(b"\n") and receipt_raw.count(b"\n")==1 and all(x==10 or 32<=x<=126 for x in receipt_raw))
 common_keys=(b"protocol_version",b"session_id",b"message_seq",b"message_sender",b"transition_id",b"sender_state",b"expected_receiver_state",b"slot_ordinal",b"slot_probe",b"effect_state",b"deadline_name",b"absolute_deadline_ns")
 physical=tuple(key for key in REFUSAL_RECEIPT_KEYS if key not in CONTROL_RESERVED)
 fields=receipt_raw[:-1].split(b"|");need(fields[0]==b"V15_REFUSE_ACK_RECEIPT" and len(fields)==1+len(common_keys)+len(physical))
 common={};result={}
 for key,item in zip(common_keys,fields[1:1+len(common_keys)]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and parts[1] and key not in common);common[key]=parts[1]
 for key,item in zip(physical,fields[1+len(common_keys):]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and parts[1] and key not in result and key not in common);result[key]=parts[1]
 spec_state,spec_receiver,spec_effect,deadline_key=CONTROL_SPEC[b"V15_REFUSE_ACK_RECEIPT"]
 need(common[b"protocol_version"]==b"14" and common[b"session_id"]==AUTH and common[b"message_sender"]==b"A")
 need(common[b"transition_id"]==common[b"sender_state"]+b"->"+common[b"expected_receiver_state"]+b":"+common[b"effect_state"])
 need((common[b"sender_state"],common[b"expected_receiver_state"],common[b"effect_state"])==(spec_state,spec_receiver,spec_effect))
 need(common[b"deadline_name"]==deadline_key and udec(common[b"absolute_deadline_ns"],1)==receipt_deadline)
 need((common[b"expected_receiver_state"],common[b"slot_ordinal"],common[b"slot_probe"])==(b"WAIT_REFUSAL_RECEIPT",b"NONE",b"NONE"))
 sequence=udec(common[b"message_seq"],1);need(sequence==CONTROL_RECV_SEQ+1)
 result.update({b"state":common[b"sender_state"],b"expected_state":common[b"expected_receiver_state"],b"ordinal":common[b"slot_ordinal"],b"probe":common[b"slot_probe"],b"auth_id":common[b"session_id"],b"sender":common[b"message_sender"],b"effect_state":common[b"effect_state"],deadline_key:str(receipt_deadline).encode(),b"message_seq":str(sequence).encode(),b"packet_sha256":sha(receipt_raw)})
 need(result[b"state"]==b"REFUSAL_ACK_RECEIVED" and result[b"expected_state"]==b"WAIT_REFUSAL_RECEIPT" and result[b"effect_state"]==b"NO_REPLAY_RECEIPT")
 need(result[b"ordinal"]==result[b"probe"]==b"NONE" and result[b"ack_packet_sha256"]==sha(ack_raw) and udec(result[b"ack_message_seq"],1)==ack_sequence)
 need(result[b"request_packet_sha256"]==request_sha and result[b"cross_map_state"]==cross_map and result[b"no_replay"]==b"1")
 need(udec(result[b"refusal_finality_deadline_ns"])==finality_deadline and udec(result[b"refusal_closure_deadline_ns"])==closure_deadline and result[b"refusal_schedule_hex"]==schedule_claim and udec(result[b"consume_deadline_ns"])==receipt_deadline)
 checkpoint(CERT,0,finality_deadline);need(time.monotonic_ns()<=finality_deadline and sequence==CONTROL_RECV_SEQ+1)
 return result,sequence

def commit_refusal_receipt(context,receipt_raw,sequence):
 global CONTROL_RECV_SEQ
 cached=refusal_slot(context);finality_deadline=cached[1][6];need(sequence==CONTROL_RECV_SEQ+1 and cached[8]==b"OPEN" and cached[10]==b"")
 evidence=(b"P27E001_REFUSAL_RECEIPT_FINALITY_V15\nRECEIPT_SEQUENCE="+str(sequence).encode()+b"\nRECEIPT_BYTES="+str(len(receipt_raw)).encode()+b"\nRECEIPT_SHA256="+sha(receipt_raw)+b"\nCANDIDATE_FAULT_EVIDENCE_SHA256="+refusal_candidate_fault_digest(context)+b"\nFINALITY_DEADLINE_NS="+str(finality_deadline).encode()+b"\nCLOSURE_DEADLINE_NS="+str(cached[1][7]).encode()+b"\nFINALITY_END=1\n")
 updated=refusal_slot_update(context,b"RECEIPT_VERIFIED",receipt_raw=receipt_raw,receipt_sequence=sequence,finality_state=b"RECEIPT_VERIFIED_FINAL",finality_evidence=evidence);evidence_sha=sha(evidence)
 need(updated[6]==receipt_raw and updated[7]==sequence and updated[8]==b"RECEIPT_VERIFIED_FINAL" and updated[10]==b"" and sequence==CONTROL_RECV_SEQ+1)
 need(refusal_slot(context)==cached and sequence==CONTROL_RECV_SEQ+1);checkpoint(CERT,0,finality_deadline);need(time.monotonic_ns()<=finality_deadline)
 CONTROL_RECV_SEQ,context[b"refusal_offer_cache"],context[b"refusal_finality_state"],context[b"refusal_finality_evidence_sha"]=(sequence,updated,b"RECEIPT_VERIFIED_FINAL",evidence_sha)
 return updated

def receive_refusal_candidate_once(control,context):
 installed=();installed_slots=();raw=b"";finality_deadline=refusal_slot(context)[1][6]
 try:
  try:
   raw,ancillary,flags,address=control.recvmsg(65536,socket.CMSG_SPACE(MAX_RIGHTS*array.array("i").itemsize));bad=False
   installed_slots,installed,bad=quarantine_scm_rights(context,ancillary,b"refusal_unexpected_right_",b"UNEXPECTED_REFUSAL_RIGHT",MAX_RIGHTS)
  except BlockingIOError:return b"NO_DATA"
  except BaseException:
   refusal_candidate_fault(context,raw,b"TRANSPORT_REJECTED");return b"REJECTED"
  if raw==b"" and not bad and not installed and not ancillary and not flags and address is None:
   context[b"refusal_control_eof"]=True;return b"EOF"
  try:checkpoint(CERT,0,finality_deadline);need(time.monotonic_ns()<=finality_deadline)
  except BaseException:
   refusal_candidate_fault(context,raw,b"POST_FINALITY_NONAUTHORITATIVE");return b"LATE_NONAUTHORITATIVE"
  if not raw or bad or installed or ancillary or flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC) or address is not None:
   refusal_candidate_fault(context,raw,b"TRANSPORT_REJECTED");return b"REJECTED"
  if context[b"refusal_finality_state"]!=b"OPEN":
   refusal_candidate_fault(context,raw,b"POST_FINAL_REPLAY");return b"REJECTED"
  try:receipt,sequence=parse_refusal_receipt_candidate(context,raw)
  except BaseException:refusal_candidate_fault(context,raw,b"SEMANTIC_REJECTED");return b"REJECTED"
  commit_refusal_receipt(context,raw,sequence);return b"VERIFIED"
 finally:close_lifecycle_slots(context,tuple(installed_slots))

def finalize_refusal_actor_loss(context):
 cached=refusal_slot(context);finality_deadline=cached[1][6]
 actor_pidfd_provenance(context);need(cached[8]==b"OPEN" and cached[10]==b"" and context[b"refusal_actor_loss_seen"] and context[b"refusal_control_eof"] and context[b"actor_pidfd_exit_ready_observed"])
 evidence=(b"P27E001_REFUSAL_ACTOR_LOSS_FINALITY_V15\nACTOR_PID="+str(ACTOR_PID).encode()+b"\nACTOR_STARTTIME="+str(ACTOR_STARTTIME).encode()+b"\nPIDFD_READY=1\nACTOR_CONTROL_EOF=1\nCONTROL_RECV_SEQ_AT_EOF="+str(CONTROL_RECV_SEQ).encode()+b"\nCANDIDATE_FAULT_EVIDENCE_SHA256="+refusal_candidate_fault_digest(context)+b"\nFINALITY_DEADLINE_NS="+str(finality_deadline).encode()+b"\nCLOSURE_DEADLINE_NS="+str(cached[1][7]).encode()+b"\nFINALITY_END=1\n")
 updated=refusal_slot_update(context,b"ACTOR_LOSS_DRAINED",finality_state=b"ACTOR_LOSS_CONTROL_EOF_FINAL",finality_evidence=evidence);evidence_sha=sha(evidence)
 need(refusal_slot(context)==cached);checkpoint(CERT,0,finality_deadline);need(time.monotonic_ns()<=finality_deadline)
 context[b"refusal_offer_cache"],context[b"refusal_finality_state"],context[b"refusal_finality_evidence_sha"],context[b"refusal_offer_state"]=(updated,b"ACTOR_LOSS_CONTROL_EOF_FINAL",evidence_sha,b"ACTOR_LOSS_CONTROL_EOF_FINAL_NO_OFFER")
 return updated

def finalize_refusal_cap_hold(context):
 cached=refusal_slot(context)
 if cached[8]!=b"OPEN":return cached
 need(cached[10]==b"");finality_deadline=cached[1][6]
 evidence=(b"P27E001_REFUSAL_FINALITY_CAP_HOLD_V15\nFINALITY_DEADLINE_NS="+str(finality_deadline).encode()+b"\nCLOSURE_DEADLINE_NS="+str(cached[1][7]).encode()+b"\nCONTROL_RECV_SEQ="+str(CONTROL_RECV_SEQ).encode()+b"\nACTOR_LOSS_SEEN="+(b"1" if context[b"refusal_actor_loss_seen"] else b"0")+b"\nACTOR_CONTROL_EOF="+(b"1" if context[b"refusal_control_eof"] else b"0")+b"\nCANDIDATE_FAULT_EVIDENCE_SHA256="+refusal_candidate_fault_digest(context)+b"\nOFFER_ALLOWED=0\nFINALITY_END=1\n")
 updated=refusal_slot_update(context,b"FINALITY_CAP_EXPIRED_HOLD",finality_state=b"CAP_EXPIRED_HOLD",finality_evidence=evidence);evidence_sha=sha(evidence)
 need(refusal_slot(context)==cached and time.monotonic_ns()>=finality_deadline)
 context[b"refusal_offer_cache"],context[b"refusal_finality_state"],context[b"refusal_finality_evidence_sha"],context[b"refusal_offer_state"]=(updated,b"CAP_EXPIRED_HOLD",evidence_sha,b"FINALITY_CAP_EXPIRED_HOLD_NO_OFFER")
 context[b"refusal_finality_timeout_observed"]=True
 return updated

def refusal_receipt_final(context):
 state=refusal_slot(context)[8];return state in (b"RECEIPT_VERIFIED_FINAL",b"ACTOR_LOSS_CONTROL_EOF_FINAL")

def refusal_offer_eligible(context):
 cached=refusal_slot(context)
 if cached[8]==b"RECEIPT_VERIFIED_FINAL":return cached[3]==b"CLOSED_NO_CONSUME" and bool(cached[4]) and context[b"refusal_closed"]
 if cached[8]==b"ACTOR_LOSS_CONTROL_EOF_FINAL":return context[b"refusal_actor_loss_seen"] and context[b"refusal_control_eof"] and not context[b"consumed"]
 return False

def await_refusal_finality(control,context):
 cached=refusal_slot(context);finality_deadline=cached[1][6]
 if refusal_receipt_final(context):return True
 if cached[8]==b"CAP_EXPIRED_HOLD":return False
 while True:
  now=time.monotonic_ns()
  if now>=finality_deadline:
   try:finalize_refusal_cap_hold(context)
   except BaseException:
    context[b"refusal_finality_timeout_observed"]=True;context[b"faults"].add(b"RECONCILIATION_UNKNOWN")
   return False
  poller=select.poll();actor_registered=False;control_fd=-1
  if not context[b"refusal_actor_loss_seen"]:
   try:register_lifecycle_poller(context,poller,b"actor_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL);actor_registered=True
   except BaseException:context[b"faults"].add(b"RECONCILIATION_UNKNOWN")
  if control is not None and not context[b"refusal_control_eof"]:
   try:control_fd=control.fileno();need(control_fd>=0);poller.register(control_fd,select.POLLIN|select.POLLHUP|select.POLLERR)
   except BaseException:control_fd=-1;mark_control_lost(context)
  try:events=poller.poll(max(1,min(10,(finality_deadline-now+999999)//1000000)))
  except InterruptedError:continue
  except BaseException:continue
  cmask=amask=0
  for number,event in events:
   if actor_registered and number==4:amask|=event
   elif control_fd>=0 and number==control_fd:cmask|=event
  if pidfd_ready_event(amask):
   context[b"refusal_actor_loss_seen"]=True;mark_actor_pidfd_lost(context)
  if cmask&select.POLLIN:
   result=receive_refusal_candidate_once(control,context)
   if result==b"VERIFIED":return True
  if cmask&(select.POLLHUP|select.POLLERR):
   if not context[b"refusal_control_eof"]:receive_refusal_candidate_once(control,context)
   if context[b"refusal_control_eof"]:mark_control_lost(context)
  if refusal_receipt_final(context):return True
  if refusal_slot(context)[8]==b"OPEN" and context[b"refusal_actor_loss_seen"] and context[b"refusal_control_eof"] and time.monotonic_ns()<=finality_deadline:
   try:finalize_refusal_actor_loss(context);return True
   except BaseException:context[b"faults"].add(b"RECONCILIATION_UNKNOWN")
  if refusal_slot(context)[8]==b"OPEN" and time.monotonic_ns()>=finality_deadline:
   try:finalize_refusal_cap_hold(context)
   except BaseException:
    context[b"refusal_finality_timeout_observed"]=True;context[b"faults"].add(b"RECONCILIATION_UNKNOWN")
   return False

def refusal_receipt_contract(context):
 cached=refusal_slot(context);need(refusal_offer_eligible(context) and cached[10]==b"")
 tag,core,variant,close_state,ack_raw,ack_sequence,receipt_raw,receipt_sequence,finality_state,finality_evidence,offer,offer_sha,contract,contract_sha,offer_send_sequence,state_digest=cached
 seq,predecessor,request_raw,request_kind,claims,schedule_items,finality_deadline,closure_deadline=core;schedule=refusal_schedule_from_core(core)
 return (b"P27E001_REFUSAL_RECEIPT_CONTRACT_V15\nAUTH_ID="+AUTH+b"\nRECEIPT_KIND=REFUSAL_CLOSE\nRECORD_SEQ="+str(seq).encode()+b"\nPREDECESSOR_SHA256="+predecessor+b"\nREQUEST_KIND="+request_kind+b"\nREQUEST_BYTES="+str(len(request_raw)).encode()+b"\nREQUEST_SHA256="+sha(request_raw)+b"\nCLOSE_STATE="+close_state+b"\nSLOT_VARIANT="+variant+b"\nFINAL_SLOT_SHA256="+state_digest+b"\nACK_SEQUENCE="+str(ack_sequence).encode()+b"\nACK_BYTES="+str(len(ack_raw)).encode()+b"\nACK_SHA256="+sha(ack_raw)+b"\nACTOR_RECEIPT_SEQUENCE="+str(receipt_sequence).encode()+b"\nACTOR_RECEIPT_BYTES="+str(len(receipt_raw)).encode()+b"\nACTOR_RECEIPT_SHA256="+(sha(receipt_raw) if receipt_raw else EMPTY_SHA)+b"\nFINALITY_STATE="+finality_state+b"\nFINALITY_EVIDENCE_BYTES="+str(len(finality_evidence)).encode()+b"\nFINALITY_EVIDENCE_SHA256="+sha(finality_evidence)+b"\nREFUSAL_FINALITY_DEADLINE_NS="+str(finality_deadline).encode()+b"\nREFUSAL_CLOSURE_DEADLINE_NS="+str(closure_deadline).encode()+b"\nREFUSAL_CLOSURE_TAIL_NS="+str(REFUSAL_CLOSURE_TAIL_NS).encode()+b"\nREFUSAL_SCHEDULE_HEX="+schedule_hex(schedule,REFUSAL_PHASE_SPEC)+b"\nRIGHTS_MANIFEST_SHA256="+EMPTY_SHA+b"\nISSUER_KEY_ID="+ISSUER_KEY_ID+b"\nOWNER_PID="+CERT[b"EXTERNAL_OWNER_PID"]+b"\nOWNER_STARTTIME="+CERT[b"EXTERNAL_OWNER_STARTTIME"]+b"\nEFFECT=DEDICATED_REFUSAL_RECONCILIATION\nABSOLUTE_FINALITY_DEADLINE_NS="+str(finality_deadline).encode()+b"\nABSOLUTE_CLOSURE_DEADLINE_NS="+str(closure_deadline).encode()+b"\nNO_SUCCESSOR=1\nNO_REPLAY=1\nCONTRACT_END=1\n")

def materialize_cached_refusal_offer(context):
 cached=refusal_slot(context);need(refusal_offer_eligible(context))
 if cached[10]:return cached
 offer_build_deadline,offer_latest_start,offer_reserve_after=refusal_stage_window(context,b"REFUSAL_OFFER_BUILD")
 tag,core,variant,close_state,ack_raw,ack_sequence,receipt_raw,receipt_sequence,finality_state,finality_evidence,old_offer,old_offer_sha,old_contract,old_contract_sha,old_offer_sequence,state_digest=cached
 seq,predecessor,request_raw,request_kind,claims,schedule_items,finality_deadline,closure_deadline=core;schedule=refusal_schedule_from_core(core)
 contract=refusal_receipt_contract(context);schedule_raw=schedule_hex(schedule,REFUSAL_PHASE_SPEC);offer_send_deadline=schedule[b"REFUSAL_OFFER_SEND"]
 body=((b"record_seq",str(seq).encode()),(b"predecessor_sha256",predecessor),(b"request_kind",request_kind),(b"request_bytes",str(len(request_raw)).encode()),(b"request_packet_sha256",sha(request_raw)),(b"close_state",close_state),(b"slot_variant",variant),(b"final_slot_sha256",state_digest),(b"refusal_ack_sequence",str(ack_sequence).encode()),(b"refusal_ack_bytes",str(len(ack_raw)).encode()),(b"refusal_ack_sha256",sha(ack_raw)),(b"actor_receipt_sequence",str(receipt_sequence).encode()),(b"actor_receipt_bytes",str(len(receipt_raw)).encode()),(b"actor_receipt_sha256",sha(receipt_raw) if receipt_raw else EMPTY_SHA),(b"finality_state",finality_state),(b"finality_evidence_bytes",str(len(finality_evidence)).encode()),(b"finality_evidence_sha256",sha(finality_evidence)),(b"refusal_finality_deadline_ns",str(finality_deadline).encode()),(b"refusal_closure_deadline_ns",str(closure_deadline).encode()),(b"refusal_closure_tail_ns",str(REFUSAL_CLOSURE_TAIL_NS).encode()),(b"refusal_schedule_hex",schedule_raw),(b"offer_latest_safe_start_ns",str(offer_latest_start).encode()),(b"offer_reserve_after_ns",str(offer_reserve_after).encode()),(b"receipt_contract_bytes",str(len(contract)).encode()),(b"receipt_contract_sha256",sha(contract)),(b"effect_contract",b"DEDICATED_REFUSAL_RECONCILIATION"),(b"commit_count",b"0"),(b"attempt_state",b"ABSENT_KNOWN"),(b"intent_count",b"0"),(b"receipt_possibility_closed",b"1"),(b"no_successor",b"1"),(b"no_replay",b"1"))
 offer,reserved_send_sequence=reserve_external_packet(b"REFUSAL_CLOSE_OFFER",b"REFUSAL_SLOT_LOCKED",b"ISSUER_WAIT_REFUSAL",b"DEDICATED_REFUSAL_RECONCILIATION",offer_send_deadline,body);need(reserved_send_sequence==seq)
 updated=refusal_slot_update(context,offer=offer,contract=contract,offer_send_sequence=reserved_send_sequence)
 need(updated[15]==state_digest and updated[11]==sha(offer) and updated[13]==sha(contract))
 need(refusal_slot(context)==cached and refusal_offer_eligible(context));checkpoint(CERT,0,offer_build_deadline);need(time.monotonic_ns()<=offer_build_deadline)
 context[b"refusal_offer_cache"]=updated;context[b"refusal_offer_delivery_possible"]=False;context[b"refusal_frozen_state_sha"]=state_digest;context[b"refusal_offer_state"]=b"FINALITY_BOUND_OFFER_FROZEN_NOT_SENT"
 refusal_lock_invariant(context);return updated

def refusal_acceptance_hold(context,reason):
 need(reason in (b"STAGE_LATEST_SAFE_START_MISSED",b"SEND_OR_ACCEPTANCE_EFFECT_UNKNOWN",b"ACCEPTANCE_VERIFY_OR_COMMIT_CAP_EXPIRED"))
 if context[b"refusal_acceptance_state"]!=b"COMMITTED":
  if reason==b"STAGE_LATEST_SAFE_START_MISSED" and not context[b"refusal_offer_delivery_possible"]:
   context[b"refusal_acceptance_state"]=b"CLOSURE_STAGE_NOT_STARTED_HOLD";context[b"refusal_offer_state"]=b"STAGE_LATEST_SAFE_START_MISSED_NO_NEW_EFFECT_RETAIN_OWNER"
  else:
   context[b"refusal_acceptance_state"]=b"ACCEPTANCE_EFFECT_UNKNOWN_HOLD";context[b"refusal_offer_state"]=b"ACCEPTANCE_EFFECT_UNKNOWN_HOLD_NO_RESEND_NO_CLOSE_NO_RELEASE"
  context[b"refusal_acceptance_hold_reason"]=reason
 raise RefusalFinalityPending("refusal-acceptance-effect-unknown-hold")

def drive_cached_refusal_offer(context):
 refusal_lock_invariant(context);need(refusal_offer_eligible(context))
 if context[b"refusal_offer_complete"]:
  cached=refusal_slot(context);need(cached[10] and cached[15]==context[b"refusal_frozen_state_sha"] and context[b"refusal_acceptance_state"]==b"COMMITTED");return context[b"refusal_closure_sha"]
 if context[b"refusal_acceptance_state"] in (b"CLOSURE_STAGE_NOT_STARTED_HOLD",b"ACCEPTANCE_EFFECT_UNKNOWN_HOLD"):raise RefusalFinalityPending("refusal-acceptance-held")
 try:cached=materialize_cached_refusal_offer(context)
 except BaseException:refusal_acceptance_hold(context,b"STAGE_LATEST_SAFE_START_MISSED")
 tag,core,variant,close_state,ack_raw,ack_sequence,receipt_raw,receipt_sequence,finality_state,finality_evidence,offer,offer_sha,contract,contract_sha,offer_send_sequence,state_digest=cached
 seq,predecessor,request_raw,request_kind,claims,schedule_items,finality_deadline,closure_deadline=core;schedule=refusal_schedule_from_core(core)
 need(offer and contract and offer_sha==sha(offer) and contract_sha==sha(contract) and sha(contract) in offer and context[b"transfer_offer_cache"] is None and refusal_offer_eligible(context))
 try:
  send_deadline,send_latest_start,send_reserve_after=refusal_stage_window(context,b"REFUSAL_OFFER_SEND")
  if not context[b"refusal_offer_delivery_possible"]:
   context[b"refusal_offer_delivery_possible"]=True;context[b"refusal_offer_state"]=b"DELIVERY_POSSIBLE_NO_RESEND";context[b"external_send_state"]=b"REFUSAL_OFFER_SEND_EFFECT_UNKNOWN"
   try:
    activate_reserved_external_packet(offer,offer_send_sequence);external_send(context[b"transfer_control"],context,offer,send_deadline)
    context[b"refusal_offer_state"]=b"SENT_ONCE_WAITING_ACCEPTANCE";context[b"external_send_state"]=b"REFUSAL_OFFER_SENT"
   except BaseException:
    context[b"refusal_offer_state"]=b"EFFECT_UNKNOWN_NO_RESEND_WAITING_ACCEPTANCE";context[b"external_send_state"]=b"REFUSAL_OFFER_EFFECT_UNKNOWN"
  recv_deadline,recv_latest_start,recv_reserve_after=refusal_stage_window(context,b"REFUSAL_ACCEPTANCE_RECV")
  keys=(b"offer_sha256",b"record_seq",b"predecessor_sha256",b"refusal_finality_deadline_ns",b"refusal_closure_deadline_ns",b"refusal_schedule_hex",b"durable_receipt_bytes",b"durable_receipt_sha256",b"acceptance_preimage_sha256",b"issuer_key_id",b"issuer_public_key_hex",b"issuer_signature_hex",b"owner_pid",b"owner_starttime",b"no_replay")
  values,issuer_receipt_raw=external_recv_receipt(context[b"transfer_control"],context,b"REFUSAL_CLOSE_ACCEPTED",keys,seq,recv_deadline)
  need(values[b"offer_sha256"]==sha(offer) and udec(values[b"record_seq"],1)==seq and values[b"predecessor_sha256"]==predecessor)
  need(udec(values[b"refusal_finality_deadline_ns"])==finality_deadline and udec(values[b"refusal_closure_deadline_ns"])==closure_deadline and values[b"refusal_schedule_hex"]==schedule_hex(schedule,REFUSAL_PHASE_SPEC))
  verify_deadline,verify_latest_start,verify_reserve_after=refusal_stage_window(context,b"REFUSAL_ACCEPTANCE_VERIFY")
  digest=verify_external_acceptance(b"REFUSAL_CLOSE",offer,issuer_receipt_raw,values,seq,predecessor,EMPTY_SHA,finality_deadline,closure_deadline,verify_deadline)
  need(values[b"owner_pid"]==CERT[b"EXTERNAL_OWNER_PID"] and values[b"owner_starttime"]==CERT[b"EXTERNAL_OWNER_STARTTIME"] and values[b"no_replay"]==b"1")
  owner_pid=udec(CERT[b"EXTERNAL_OWNER_PID"],2);need(pidfd_pid(15)==owner_pid and proc_starttime(owner_pid)==udec(CERT[b"EXTERNAL_OWNER_STARTTIME"],1))
  checkpoint(CERT,0,verify_deadline);need(time.monotonic_ns()<=verify_deadline)
  commit_deadline,commit_latest_start,commit_reserve_after=refusal_stage_window(context,b"REFUSAL_ACCEPTANCE_COMMIT")
  current=refusal_slot(context);need(refusal_offer_eligible(context) and current[10]==offer and current[11]==offer_sha and current[12]==contract and current[13]==contract_sha and current[15]==state_digest==context[b"refusal_frozen_state_sha"])
  new_external_state=(seq,digest)
  need(refusal_slot(context)==current and EXTERNAL_RECV_SEQ+1==seq);checkpoint(CERT,0,commit_deadline);need(time.monotonic_ns()<=commit_deadline)
  commit_external_receive(seq);context[b"external_record_seq"],context[b"external_chain_sha"]=new_external_state;context[b"refusal_closure_sha"]=digest
  context[b"refusal_offer_receipt_sha"]=digest;context[b"refusal_offer_complete"]=True;context[b"refusal_acceptance_state"]=b"COMMITTED";context[b"refusal_offer_state"]=b"ACCEPTED_CRYPTOGRAPHIC_DURABLE_FINALITY_RECHECKED";return digest
 except RefusalFinalityPending:raise
 except BaseException:
  refusal_acceptance_hold(context,b"ACCEPTANCE_VERIFY_OR_COMMIT_CAP_EXPIRED" if context[b"refusal_offer_delivery_possible"] else b"STAGE_LATEST_SAFE_START_MISSED")

def refusal_closure_hold(context,reason):
 context[b"refusal_closure_hold_state"]=reason;context[b"refusal_offer_state"]=b"CLOSURE_CAP_HOLD_RETAIN_CAPABILITIES_NO_OWNER_RELEASE"
 raise RefusalFinalityPending("refusal-closure-cap-hold")

def complete_refusal_closure(control,context):
 cached=refusal_slot(context);need(context[b"refusal_offer_complete"] and context[b"refusal_acceptance_state"]==b"COMMITTED" and cached[10] and cached[15]==context[b"refusal_frozen_state_sha"])
 core=cached[1];schedule=refusal_schedule_from_core(core);finality_deadline=core[6];closure_deadline=core[7]
 if not context[b"refusal_actor_closure_complete"]:
  try:actor_close_deadline,actor_close_latest_start,actor_close_reserve_after=refusal_stage_window(context,b"REFUSAL_ACTOR_CLOSURE")
  except BaseException:refusal_closure_hold(context,b"ACTOR_CLOSURE_LATEST_SAFE_START_MISSED")
  if cached[8]==b"RECEIPT_VERIFIED_FINAL" and control is not None:
   request_sha,request_sequence,a_begin,a_arm,cross_map,origin_raw,finality_raw,closure_raw,schedule_claim=core[4]
   closed=packet(b"V15_REFUSAL_CLOSED",((b"state",b"REFUSAL_DURABLY_CLOSED"),(b"expected_state",b"WAIT_REFUSAL_CLOSED"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"ack_packet_sha256",sha(cached[4])),(b"receipt_packet_sha256",sha(cached[6])),(b"cross_map_state",cross_map),(b"issuer_closure_sha256",context[b"refusal_closure_sha"]),(b"issuer_record_seq",str(core[0]).encode()),(b"issuer_predecessor_sha256",core[1]),(b"no_replay",b"1"),(b"refusal_finality_deadline_ns",str(finality_deadline).encode()),(b"refusal_closure_deadline_ns",str(closure_deadline).encode()),(b"refusal_schedule_hex",schedule_claim),(b"consume_deadline_ns",str(actor_close_deadline).encode())))
   checkpoint(CERT,0,actor_close_deadline);need(time.monotonic_ns()<=actor_close_deadline)
   context[b"send_state"]=b"REFUSAL_CLOSURE_SEND_EFFECT_UNKNOWN"
   try:send_exact(control,closed,actor_close_deadline);context[b"send_state"]=b"REFUSAL_CLOSURE_SENT";context[b"refusal_actor_closure_state"]=b"SENT"
   except BaseException:context[b"send_state"]=b"REFUSAL_CLOSURE_SEND_EFFECT_UNKNOWN";context[b"refusal_actor_closure_state"]=b"EFFECT_UNKNOWN_AFTER_DURABLE_ACCEPTANCE"
  else:context[b"refusal_actor_closure_state"]=b"ACTOR_LOSS_OR_CONTROL_UNAVAILABLE_AFTER_DURABLE_ACCEPTANCE"
  context[b"refusal_actor_closure_complete"]=True
 if not context[b"refusal_capabilities_closed"]:
  if not context[b"ownership_close_started"]:
   try:
    cap_deadline,cap_latest_start,cap_reserve_after=refusal_stage_window(context,b"REFUSAL_CAPABILITY_CLOSE")
    release_deadline,release_latest_start,release_reserve_after=refusal_stage_window(context,b"REFUSAL_CLOSURE")
   except BaseException:refusal_closure_hold(context,b"CAPABILITY_OR_RELEASE_LATEST_SAFE_START_MISSED")
  else:cap_deadline=None
  try:close_ownership_capabilities(context,cap_deadline);context[b"refusal_capabilities_closed"]=True
  except OwnershipClosePending:refusal_closure_hold(context,b"CAPABILITY_CLOSE_RECONCILIATION_RETRYABLE")
 need(context[b"refusal_capabilities_closed"] and ownership_capabilities_closed(context) and context[b"refusal_actor_closure_complete"] and context[b"refusal_acceptance_state"]==b"COMMITTED" and refusal_slot(context)[10]==cached[10])
 need(not context[b"owner_released"])
 complete_started_ownership_close(context);return context[b"refusal_closure_sha"]

def issuer_refusal_close(context):
 refusal_lock_invariant(context);need(refusal_offer_eligible(context));return drive_cached_refusal_offer(context)

def note_locked_refusal_error(context,error,external=False):
 if isinstance(error,RefusalFinalityPending):
  refusal_lock_invariant(context);return
 refusal_lock_invariant(context)
 if isinstance(error,RemoteAbort):context[b"faults"].update(error.faults)
 elif isinstance(error,PidfdActorLost):context[b"refusal_actor_loss_seen"]=True;mark_actor_pidfd_lost(context)
 elif isinstance(error,ControlLost):mark_control_lost(context)
 elif isinstance(error,CertificateExpired):context[b"faults"].add(b"CERTIFICATE_EXPIRED")
 elif isinstance(error,SendEffectUnknown):context[b"faults"].add(b"SEND_EFFECT_UNKNOWN")
 elif isinstance(error,FaultSet):context[b"faults"].update(error.faults)
 elif isinstance(error,StaticReject):context[b"faults"].add(b"TRANSFER_PROTOCOL_UNKNOWN" if external else b"CONTROL_MALFORMED")
 else:context[b"faults"].add(b"INTERNAL_INVARIANT")
 context[b"faults"].add(b"RECONCILIATION_UNKNOWN");context[b"refusal_offer_state"]=b"POST_LOCK_FAULT_SAME_SLOT";refusal_lock_invariant(context)

def route_locked_refusal(control,context,error):
 if isinstance(error,RefusalFinalityPending):
  reason=error.args[0].encode("ascii") if len(error.args)==1 and type(error.args[0]) is str else b"REFUSAL_FINALITY_PENDING"
  transfer_or_hold(control,context,reason,False);return
 note_locked_refusal_error(context,error);transfer_or_hold(control,context,b"RECONCILIATION_UNKNOWN")

def transfer_schedule_from_cache(cache):
 offer,caps,manifest,seq,predecessor,schedule_items,finality_deadline,closure_deadline,reason,reserved_sequence,state_digest,provenance_binding=cache
 schedule={name:value for name,value in schedule_items};need(schedule_items==tuple((name,schedule[name]) for name,cap in TRANSFER_PHASE_SPEC))
 origin=schedule[b"TRANSFER_OFFER_BUILD"]-TRANSFER_OFFER_BUILD_NS
 need(schedule==exact_schedule(origin,closure_deadline,TRANSFER_PHASE_SPEC) and finality_deadline==schedule[b"TRANSFER_ACCEPTANCE_COMMIT"]<closure_deadline)
 return schedule

def transfer_stage_window(context,name):
 cache=context[b"transfer_offer_cache"];schedule=transfer_schedule_from_cache(cache);names=tuple(item[0] for item in TRANSFER_PHASE_SPEC);index=names.index(name);cap=TRANSFER_PHASE_SPEC[index][1]
 stage_deadline=schedule[name];latest_safe_start=stage_deadline-cap;reserve_after=cache[7]-stage_deadline
 need(cap>0 and reserve_after==sum(item[1] for item in TRANSFER_PHASE_SPEC[index+1:]) and time.monotonic_ns()<=latest_safe_start)
 checkpoint(CERT,0,stage_deadline);need(time.monotonic_ns()<=stage_deadline);return stage_deadline,latest_safe_start,reserve_after

def generic_transfer_hold(context,reason):
 need(reason in (b"STAGE_NOT_STARTED",b"ACCEPTANCE_EFFECT_UNKNOWN",b"CLOSURE_CAP_EXPIRED"))
 if context[b"transfer_acceptance_state"]==b"COMMITTED":
  context[b"transfer_state"]=b"COMMITTED_IMMUTABLE_CLOSE_CURSOR_RETRYABLE_NO_RESEND";raise RefusalFinalityPending("generic-committed-close-retry")
 if reason==b"STAGE_NOT_STARTED":context[b"transfer_acceptance_state"]=b"TRANSFER_STAGE_NOT_STARTED_HOLD"
 elif reason==b"ACCEPTANCE_EFFECT_UNKNOWN":context[b"transfer_acceptance_state"]=b"TRANSFER_ACCEPTANCE_EFFECT_UNKNOWN_HOLD"
 else:context[b"transfer_acceptance_state"]=b"TRANSFER_CLOSURE_CAP_HOLD"
 context[b"transfer_state"]=context[b"transfer_acceptance_state"]+b"_NO_RESEND_NO_OWNER_RELEASE";raise RefusalFinalityPending("generic-transfer-held")

def complete_generic_transfer_closure(context):
 cache=context[b"transfer_offer_cache"];offer,caps,manifest,seq,predecessor,schedule_items,finality_deadline,closure_deadline,reason,reserved_sequence,state_digest,provenance_binding=cache
 need(context[b"transfer_acceptance_state"]==b"COMMITTED" and context[b"transfer_receipt_sha"]!=b"0"*64)
 if not context[b"transfer_capabilities_closed"]:
  if not context[b"ownership_close_started"]:
   try:
    cap_deadline,cap_latest_start,cap_reserve_after=transfer_stage_window(context,b"TRANSFER_CAPABILITY_CLOSE")
    release_deadline,release_latest_start,release_reserve_after=transfer_stage_window(context,b"TRANSFER_CLOSURE")
   except BaseException:generic_transfer_hold(context,b"CLOSURE_CAP_EXPIRED")
  else:cap_deadline=None
  try:
   need(context.get(b"outer_offer_binding")==provenance_binding);close_ownership_capabilities(context,cap_deadline,caps);context[b"transfer_capabilities_closed"]=True
  except OwnershipClosePending:
   context[b"transfer_state"]=b"COMMITTED_IMMUTABLE_LOCAL_CLOSE_CURSOR_RETRYABLE_NO_RESEND";raise
  except BaseException:
   if context[b"ownership_close_started"]:context[b"transfer_state"]=b"COMMITTED_IMMUTABLE_LOCAL_CLOSE_CURSOR_FAULT_RETAINED_NO_RESEND";raise
   generic_transfer_hold(context,b"CLOSURE_CAP_EXPIRED")
 need(context[b"transfer_capabilities_closed"] and ownership_capabilities_closed(context) and not context[b"owner_released"])
 complete_started_ownership_close(context);return context[b"transfer_receipt_sha"]

def external_transfer(control,context,reason):
 need((context[b"consumed"] or context.get(b"refusal_closed",False) or context.get(b"refusal_slot_locked",False)) and not context[b"owner_released"] and reason in FAULT_ORDER)
 if context[b"ownership_close_started"]:
  complete_started_ownership_close(context);return context.get(b"transfer_receipt_sha",context.get(b"refusal_closure_sha",b"0"*64))
 locked=refusal_lock_invariant(context)
 if locked:
  if not refusal_receipt_final(context):await_refusal_finality(control,context)
  if not refusal_offer_eligible(context):raise RefusalFinalityPending("refusal-finality-or-close-not-established")
  if context.get(b"refusal_offer_complete",False):
   cached=refusal_slot(context);need(cached[10] and cached[15]==context[b"refusal_frozen_state_sha"] and refusal_offer_eligible(context))
   return complete_refusal_closure(control,context)
  digest=drive_cached_refusal_offer(context)
  cached=refusal_slot(context);need(context[b"refusal_offer_complete"] and digest==context[b"refusal_closure_sha"] and cached[10] and cached[15]==context[b"refusal_frozen_state_sha"] and refusal_offer_eligible(context))
  return complete_refusal_closure(control,context)
 if context[b"transfer_acceptance_state"]==b"COMMITTED":return complete_generic_transfer_closure(context)
 if context[b"transfer_acceptance_state"] in (b"TRANSFER_STAGE_NOT_STARTED_HOLD",b"TRANSFER_ACCEPTANCE_EFFECT_UNKNOWN_HOLD",b"TRANSFER_CLOSURE_CAP_HOLD"):raise RefusalFinalityPending("generic-transfer-held")
 if context.get(b"transfer_offer_cache") is None:
  origin=time.monotonic_ns();closure_deadline=origin+TRANSFER_TOTAL_NS;need(closure_deadline<=certificate_mono_expiry(CERT))
  schedule=exact_schedule(origin,closure_deadline,TRANSFER_PHASE_SPEC);finality_deadline=schedule[b"TRANSFER_ACCEPTANCE_COMMIT"]
  apply_offer_readiness(context,offer_readiness_snapshot(context),schedule[b"TRANSFER_OFFER_BUILD"])
  provenance_binding=prepare_outer_pidfd_offer_binding(context,schedule[b"TRANSFER_OFFER_BUILD"])
  caps=external_capabilities(control,context);assert_registry_transfer_set(context,caps);transfer_set=registry_transfer_set_bytes(caps);manifest=b";".join(item[3] for item in caps);pending_manifest=pending_transfer_manifest(context)
  need((context.get(b"root_events_fd",-1)>=0)==any(item[0]==b"ROOT_EVENTS_FD" for item in caps) and (context.get(b"root_kill_fd",-1)>=0)==any(item[0]==b"ROOT_KILL_FD" for item in caps))
  seq=context[b"external_record_seq"]+1;predecessor=context[b"external_chain_sha"];schedule_items=tuple((name,schedule[name]) for name,cap in TRANSFER_PHASE_SPEC)
  actor_pid_raw,actor_start_raw,actor_ready_raw,external_pid_raw,external_start_raw,external_ready_raw,outer_pid_raw,outer_start_raw,outer_state,outer_ready_raw,outer_release_sha,outer_release_ordinal,outer_release_probe,outer_right_raw=provenance_binding
  state_payload=(b"P27E001_GENERIC_TRANSFER_STATE_V15\nRECORD_SEQ="+str(seq).encode()+b"\nPREDECESSOR_SHA256="+predecessor+b"\nREASON="+reason+b"\nRIGHTS_MANIFEST_SHA256="+sha(manifest)+b"\nREGISTRY_TRANSFER_SET_SHA256="+sha(transfer_set)+b"\nSOLE_KILL_CAPABILITY=ROOT_KILL_FD\nACTOR_PID="+actor_pid_raw+b"\nACTOR_STARTTIME="+actor_start_raw+b"\nACTOR_PIDFD_EXIT_READY="+actor_ready_raw+b"\nEXTERNAL_OWNER_PID="+external_pid_raw+b"\nEXTERNAL_OWNER_STARTTIME="+external_start_raw+b"\nEXTERNAL_OWNER_PIDFD_EXIT_READY="+external_ready_raw+b"\nOUTER_PID="+outer_pid_raw+b"\nOUTER_STARTTIME="+outer_start_raw+b"\nOUTER_PIDFD_STATE="+outer_state+b"\nOUTER_PIDFD_EXIT_READY="+outer_ready_raw+b"\nOUTER_RELEASE_RECORD_SHA256="+outer_release_sha+b"\nOUTER_RELEASE_ORDINAL="+outer_release_ordinal+b"\nOUTER_RELEASE_PROBE="+outer_release_probe+b"\nOUTER_PIDFD_RIGHT_PRESENT="+outer_right_raw+b"\nFINALITY_DEADLINE_NS="+str(finality_deadline).encode()+b"\nCLOSURE_DEADLINE_NS="+str(closure_deadline).encode()+b"\nTRANSFER_SCHEDULE_HEX="+schedule_hex(schedule,TRANSFER_PHASE_SPEC)+b"\nSTATE_END=1\n");state_digest=sha(state_payload)
  body=((b"record_seq",str(seq).encode()),(b"predecessor_sha256",predecessor),(b"reason",reason),(b"rights_count",str(len(caps)).encode()),(b"rights_manifest_hex",manifest.hex().encode()),(b"rights_manifest_sha256",sha(manifest)),(b"registry_transfer_set_hex",transfer_set.hex().encode()),(b"registry_transfer_set_sha256",sha(transfer_set)),(b"sole_kill_capability",b"ROOT_KILL_FD"),(b"pending_record_manifest_hex",pending_manifest.hex().encode()),(b"pending_record_manifest_sha256",sha(pending_manifest)),(b"pending_expected_raw_carrier",b"PENDING_EXPECTED_RAW_FD" if context.get(b"record_pending") is not None else b"NOT_APPLICABLE"),(b"actor_pid",actor_pid_raw),(b"actor_starttime",actor_start_raw),(b"actor_pidfd_exit_ready",actor_ready_raw),(b"external_owner_pid",external_pid_raw),(b"external_owner_starttime",external_start_raw),(b"external_owner_pidfd_exit_ready",external_ready_raw),(b"outer_pid",outer_pid_raw),(b"outer_starttime",outer_start_raw),(b"outer_pidfd_state",outer_state),(b"outer_pidfd_exit_ready",outer_ready_raw),(b"outer_release_record_sha256",outer_release_sha),(b"outer_release_ordinal",outer_release_ordinal),(b"outer_release_probe",outer_release_probe),(b"outer_pidfd_right_present",outer_right_raw),(b"owner_pid",CERT[b"EXTERNAL_OWNER_PID"]),(b"owner_starttime",CERT[b"EXTERNAL_OWNER_STARTTIME"]),(b"terminal_phase",context.get(b"terminal_phase",b"NOT_STARTED")),(b"terminal_subject_sha256",context.get(b"terminal_subject",context.get(b"collision_transfer_claim_sha",b"0"*64))),(b"chain_head_sha256",context[b"chain_sha"]),(b"outcome_durable",b"1" if context[b"outcome_durable"] else b"0"),(b"control_state",context[b"control_state"]),(b"actor_state",context[b"actor_state"]),(b"send_state",context[b"send_state"]),(b"attempt_state",context[b"attempt_state"]),(b"collision_closed",b"1" if context[b"collision"] else b"0"),(b"attempt_base_closed",b"1" if context.get(b"attempt_base_fd",-1)<0 else b"0"),(b"commit_count",str(context[b"commit_count"]).encode()),(b"intent_count",str(context[b"intent_count"]).encode()),(b"last_committed_record_sha256",context.get(b"last_committed_record_sha",b"0"*64)),(b"last_committed_packet_sha256",context.get(b"last_committed_packet_sha",b"0"*64)),(b"committed_send_state",context.get(b"committed_send_state",b"NOT_STARTED")),(b"transfer_finality_deadline_ns",str(finality_deadline).encode()),(b"transfer_closure_deadline_ns",str(closure_deadline).encode()),(b"transfer_schedule_hex",schedule_hex(schedule,TRANSFER_PHASE_SPEC)),(b"frozen_state_sha256",state_digest),(b"no_replay",b"1"))
  offer,reserved_sequence=reserve_external_packet(b"TRANSFER_OFFER",b"FROZEN_EXTERNAL_TRANSFER",b"ISSUER_WAIT_TRANSFER",b"SCM_RIGHTS_TRANSFER",schedule[b"TRANSFER_OFFER_SEND"],body);need(reserved_sequence==seq)
  candidate=(offer,caps,manifest,seq,predecessor,schedule_items,finality_deadline,closure_deadline,reason,reserved_sequence,state_digest,provenance_binding)
  need(context[b"transfer_offer_cache"] is None);checkpoint(CERT,0,schedule[b"TRANSFER_OFFER_BUILD"]);need(time.monotonic_ns()<=schedule[b"TRANSFER_OFFER_BUILD"])
  expected_snapshot=(actor_ready_raw==b"1",outer_ready_raw==b"1",external_ready_raw==b"1");final_snapshot=offer_readiness_snapshot(context)
  if final_snapshot!=expected_snapshot:
   v20_frozen_cache=context[b"v19_generic_offer_cache"]
   need(v20_frozen_cache.state==b"FROZEN" and v20_frozen_cache.atomic_authority is not None)
   need(v20_frozen_cache.atomic_authority[1]==offer and v20_frozen_cache.frozen_wire_rows==v19_wire_rows_from_caps_v19(caps))
   need(final_snapshot[0]==expected_snapshot[0] and final_snapshot[2]==expected_snapshot[2])
   need(final_snapshot[1] and not expected_snapshot[1])
   v20_frozen_binding=context[b"outer_offer_binding"]
   v20_frozen_outer_record_id=v20_frozen_cache.outer_record_id
   v20_frozen_sequence=v20_frozen_cache.prepared_sequence
   v20_frozen_full=v20_frozen_cache.frozen_full.exact_tuple()
   v20_frozen_offered=v20_frozen_cache.frozen_offered.exact_tuple()
   context[b"transfer_offer_cache"]=candidate;context[b"frozen_transfer_reason"]=reason
   context[b"offer_delivery_possible"]=False;context[b"transfer_state"]=b"OFFER_FROZEN_NOT_SENT"
   apply_offer_readiness(context,final_snapshot,schedule[b"TRANSFER_OFFER_BUILD"])
   need(context[b"outer_offer_binding"] is v20_frozen_binding and v20_frozen_binding is provenance_binding)
   need(context[b"outer_pidfd_offer_state"]==b"POST_OFFER_READY_RETAINED")
   need(v20_frozen_cache.outer_record_id==v20_frozen_outer_record_id and v20_frozen_cache.prepared_sequence==v20_frozen_sequence)
   need(v20_frozen_cache.frozen_full.exact_tuple()==v20_frozen_full and v20_frozen_cache.frozen_offered.exact_tuple()==v20_frozen_offered)
  else:
   context[b"transfer_offer_cache"]=candidate;context[b"frozen_transfer_reason"]=reason
   context[b"offer_delivery_possible"]=False;context[b"transfer_state"]=b"OFFER_FROZEN_NOT_SENT"
 else:
  offer,caps,manifest,seq,predecessor,schedule_items,finality_deadline,closure_deadline,frozen_reason,reserved_sequence,state_digest,provenance_binding=context[b"transfer_offer_cache"];need(reason==frozen_reason==context[b"frozen_transfer_reason"])
 cache=context[b"transfer_offer_cache"];offer,caps,manifest,seq,predecessor,schedule_items,finality_deadline,closure_deadline,frozen_reason,reserved_sequence,state_digest,provenance_binding=cache;schedule=transfer_schedule_from_cache(cache)
 try:
  send_deadline,send_latest_start,send_reserve_after=transfer_stage_window(context,b"TRANSFER_OFFER_SEND")
  if not context[b"offer_delivery_possible"]:
   context[b"offer_delivery_possible"]=True;context[b"transfer_state"]=b"OFFER_DELIVERY_POSSIBLE_NO_RESEND"
   try:assert_registry_transfer_set(context,caps);unique_kill_authority(context,bool(context.get(b"containment_bound")));activate_reserved_external_packet(offer,reserved_sequence);external_send(context[b"transfer_control"],context,offer,send_deadline,tuple(item[2] for item in caps));context[b"transfer_state"]=b"OFFER_SENT_ONCE_WAITING_RECEIPT"
   except BaseException:context[b"transfer_state"]=b"OFFER_EFFECT_UNKNOWN_NO_RESEND_WAITING_RECEIPT"
  recv_deadline,recv_latest_start,recv_reserve_after=transfer_stage_window(context,b"TRANSFER_ACCEPTANCE_RECV")
  keys=(b"offer_sha256",b"record_seq",b"predecessor_sha256",b"held_manifest_sha256",b"registry_transfer_set_hex",b"registry_transfer_set_sha256",b"sole_kill_capability",b"actor_pid",b"actor_starttime",b"actor_pidfd_exit_ready",b"external_owner_pid",b"external_owner_starttime",b"external_owner_pidfd_exit_ready",b"outer_pid",b"outer_starttime",b"outer_pidfd_state",b"outer_pidfd_exit_ready",b"outer_release_record_sha256",b"outer_release_ordinal",b"outer_release_probe",b"outer_pidfd_right_present",b"transfer_finality_deadline_ns",b"transfer_closure_deadline_ns",b"transfer_schedule_hex",b"durable_receipt_bytes",b"durable_receipt_sha256",b"acceptance_preimage_sha256",b"issuer_key_id",b"issuer_public_key_hex",b"issuer_signature_hex",b"receiver_pid",b"receiver_starttime",b"no_replay")
  values,receipt_raw=external_recv_receipt(context[b"transfer_control"],context,b"TRANSFER_ACCEPTED",keys,seq,recv_deadline)
  need(values[b"offer_sha256"]==sha(offer) and udec(values[b"record_seq"],1)==seq and values[b"predecessor_sha256"]==predecessor and values[b"held_manifest_sha256"]==sha(manifest));transfer_set=registry_transfer_set_bytes(caps);need(values[b"registry_transfer_set_hex"]==transfer_set.hex().encode() and values[b"registry_transfer_set_sha256"]==sha(transfer_set))
  need(values[b"sole_kill_capability"]==b"ROOT_KILL_FD");echoed=(values[b"actor_pid"],values[b"actor_starttime"],values[b"actor_pidfd_exit_ready"],values[b"external_owner_pid"],values[b"external_owner_starttime"],values[b"external_owner_pidfd_exit_ready"],values[b"outer_pid"],values[b"outer_starttime"],values[b"outer_pidfd_state"],values[b"outer_pidfd_exit_ready"],values[b"outer_release_record_sha256"],values[b"outer_release_ordinal"],values[b"outer_release_probe"],values[b"outer_pidfd_right_present"]);need(echoed==provenance_binding)
  need((values[b"outer_pidfd_right_present"]==b"1")==any(item[0]==b"OUTER_PIDFD" for item in caps))
  need(udec(values[b"transfer_finality_deadline_ns"])==finality_deadline and udec(values[b"transfer_closure_deadline_ns"])==closure_deadline and values[b"transfer_schedule_hex"]==schedule_hex(schedule,TRANSFER_PHASE_SPEC))
  verify_deadline,verify_latest_start,verify_reserve_after=transfer_stage_window(context,b"TRANSFER_ACCEPTANCE_VERIFY")
  digest=verify_external_acceptance(b"TRANSFER_ACCEPTED",offer,receipt_raw,values,seq,predecessor,sha(manifest),finality_deadline,closure_deadline,verify_deadline)
  need(values[b"receiver_pid"]==CERT[b"EXTERNAL_OWNER_PID"] and values[b"receiver_starttime"]==CERT[b"EXTERNAL_OWNER_STARTTIME"] and values[b"no_replay"]==b"1")
  owner_pid=udec(CERT[b"EXTERNAL_OWNER_PID"],2);need(context.get(b"external_owner_pidfd_provenance")== (15,owner_pid,udec(CERT[b"EXTERNAL_OWNER_STARTTIME"],1)) and not context.get(b"external_owner_pidfd_exit_ready_observed"))
  checkpoint(CERT,0,verify_deadline);need(time.monotonic_ns()<=verify_deadline)
  commit_deadline,commit_latest_start,commit_reserve_after=transfer_stage_window(context,b"TRANSFER_ACCEPTANCE_COMMIT")
  promote_later_offer_readiness(context,offer_readiness_snapshot(context));assert_registry_transfer_set(context,caps);unique_kill_authority(context,bool(context.get(b"containment_bound")));need(context[b"transfer_offer_cache"]==cache and context.get(b"outer_offer_binding")==provenance_binding and EXTERNAL_RECV_SEQ+1==seq);checkpoint(CERT,0,commit_deadline);need(time.monotonic_ns()<=commit_deadline)
  commit_external_receive(seq);context[b"external_record_seq"]=seq;context[b"external_chain_sha"]=digest;context[b"transfer_receipt_sha"]=digest;context[b"transfer_acceptance_state"]=b"COMMITTED";context[b"transfer_state"]=b"TRANSFER_ACCEPTED_CRYPTOGRAPHIC_DURABLE"
 except RefusalFinalityPending:raise
 except BaseException:generic_transfer_hold(context,b"ACCEPTANCE_EFFECT_UNKNOWN" if context[b"offer_delivery_possible"] else b"STAGE_NOT_STARTED")
 return complete_generic_transfer_closure(context)
def freeze_failure_deadlines(context):
 if context.get(b"failure_origin") is None:
  origin=time.monotonic_ns();overall=origin+FAILURE_TOTAL_NS;cleanup=origin+CLEANUP_EFFECT_NS;recovery=cleanup+RECOVERY_RECORD_NS
  need(overall-recovery==FINAL_TOTAL_NS and cleanup==overall-FAILURE_TAIL_NS)
  context[b"failure_origin"]=origin;context[b"failure_overall_deadline"]=overall;context[b"cleanup_effect_deadline"]=cleanup;context[b"recovery_deadline"]=recovery
  context[b"terminal_origin"]=recovery;context[b"terminal_deadline"]=overall;context[b"terminal_schedule"]=exact_schedule(recovery,overall,TERMINAL_PHASE_SPEC)
 else:
  need(context[b"failure_overall_deadline"]==context[b"failure_origin"]+FAILURE_TOTAL_NS)
 return context[b"failure_overall_deadline"]

def unique_kill_authority(context,required=True):
 writable=tuple((slot,entry[1]) for slot,entry in context[b"fd_registry"].items() if entry[6] and entry[0]==b"ROOT_KILL_FD")
 need(len(writable)==(1 if required else 0))
 if required:need(writable[0][0]==b"root_kill_fd" and context.get(b"root_kill_fd",-1)==writable[0][1] and context[b"fd_registry"][b"root_kill_fd"][4])
 return bool(writable)

def kill_once(context,reason):
 if context[b"kill_call_attempted"]:return
 need(context[b"kill_authority_consumed"]);context[b"kill_call_attempted"]=True;context[b"kill_state"]=b"TICKET_COMMITTING"
 freeze_failure_deadlines(context);ticket_deadline=context[b"failure_origin"]+KILL_TICKET_NS;cleanup_deadline=context[b"cleanup_effect_deadline"]
 if time.monotonic_ns()>ticket_deadline:
  context[b"kill_state"]=b"DEADLINE_PRECLUDED";context[b"faults"].add(b"KILL_TICKET_DURABILITY_UNKNOWN");return
 seq=next_record(context);predecessor=context[b"chain_sha"]
 ticket=(b"P27E001_KILL_TICKET_V15\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+predecessor+b"\nPRIMARY="+reason+b"\nFAILURE_ORIGIN_NS="+str(context[b"failure_origin"]).encode()+b"\nCLEANUP_EFFECT_DEADLINE_NS="+str(cleanup_deadline).encode()+b"\nTICKET_DEADLINE_NS="+str(ticket_deadline).encode()+b"\nKILL_CALL_COUNT_BEFORE=0\nWRITE_BYTES_HEX=310a\nRETRY_ALLOWED=0\nTICKET_END=1\n")
 state,digest=durable_once(context,b"kill-ticket.v5",ticket,ticket_deadline,False,cleanup_deadline-ticket_deadline,(b"KILL_TICKET",))
 context[b"kill_ticket_state"]=state
 if state!=DURABLE_VERIFIED:
  context[b"kill_state"]=b"TICKET_DURABILITY_UNKNOWN";context[b"faults"].add(b"KILL_TICKET_DURABILITY_UNKNOWN");return
 context[b"chain_sha"]=digest;context[b"kill_state"]=b"CALL_RESERVED";number=context.get(b"root_kill_fd",-1)
 if not unique_kill_authority(context,True) or number<0:
  context[b"kill_state"]=b"CALL_UNAVAILABLE";context[b"faults"].add(b"KILL_EFFECT_UNKNOWN");return
 if time.monotonic_ns()+KILL_RETURN_NS>cleanup_deadline:
  context[b"kill_state"]=b"DEADLINE_PRECLUDED";context[b"faults"].add(b"KILL_EFFECT_UNKNOWN");return
 context[b"kill_call_count"]=1;context[b"kill_state"]=b"CALL_ENTERED"
 try:
  record_boundary(context,cleanup_deadline,False,FAILURE_TAIL_NS);before=time.monotonic_ns()
  returned=os.write(number,b"1\n");after=time.monotonic_ns()
  record_boundary(context,cleanup_deadline,False,FAILURE_TAIL_NS)
  need(after-before<=KILL_RETURN_NS and after<=cleanup_deadline)
 except BaseException:
  context[b"kill_state"]=b"RETURN_UNKNOWN";context[b"faults"].add(b"KILL_EFFECT_UNKNOWN");return
 if returned!=2:
  context[b"kill_state"]=b"SHORT_OR_UNKNOWN";context[b"faults"].add(b"KILL_EFFECT_UNKNOWN")
 else:context[b"kill_state"]=b"RETURNED_2"
 while time.monotonic_ns()<=cleanup_deadline:
  record_boundary(context,cleanup_deadline,False,FAILURE_TAIL_NS)
  state=observe_population(context);context[b"last_population"]=state
  if state is False:
   if returned==2:context[b"kill_state"]=b"RETURNED_2_EMPTY_CONFIRMED"
   return
  owner_poll(context.get(b"actor_control"),context,cleanup_deadline)
 context[b"faults"].add(b"CONTAINMENT_OBSERVATION_UNKNOWN")
 if context[b"kill_state"]==b"RETURNED_2":context[b"kill_state"]=b"RETURNED_2_POSTCHECK_UNKNOWN"

def begin_cleanup(context):
 freeze_failure_deadlines(context)
 if context[b"cleanup_origin"] is None:context[b"cleanup_origin"]=context[b"failure_origin"];context[b"cleanup_deadline"]=context[b"cleanup_effect_deadline"]
 state=observe_population(context);context[b"last_population"]=state
 if context.get(b"payload_release_possible",False) and not context[b"kill_authority_consumed"]:
  context[b"kill_authority_consumed"]=True;context[b"kill_state"]=b"AUTHORITY_RESERVED"
 need(context[b"kill_authority_consumed"] or not context.get(b"payload_release_possible",False))

def retained_record(context,stop):
 if context[b"attempt"]<0 or context[b"collision"]:return
 deadline=context[b"cleanup_effect_deadline"]
 if time.monotonic_ns()>deadline:
  context[b"retained_state"]=b"NOT_WRITTEN_CAP_EXPIRED";context[b"faults"].add(b"RETAINED_DURABILITY_UNKNOWN");return
 seq=next_record(context);predecessor=context[b"chain_sha"]
 body=(b"P27E001_RETAINED_STATE_V15\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+predecessor+b"\nSTOP_PROBE="+stop+b"\nPRIMARY="+primary(context[b"faults"])+b"\nFAULT_SET="+fault_csv(context[b"faults"])+b"\nFAILURE_ORIGIN_NS="+str(context[b"failure_origin"]).encode()+b"\nCLEANUP_EFFECT_DEADLINE_NS="+str(deadline).encode()+b"\nKILL_CALL_COUNT="+str(context[b"kill_call_count"]).encode()+b"\nKILL_STATE="+context[b"kill_state"]+b"\nRETRY_ALLOWED=0\nRETAINED_END=1\n")
 state,digest=durable_once(context,b"retained.v5",body,deadline,False,FAILURE_TAIL_NS,(b"RETAINED",));context[b"retained_state"]=state
 if state==DURABLE_VERIFIED:context[b"chain_sha"]=digest
 else:context[b"faults"].add(b"RETAINED_DURABILITY_UNKNOWN")

def mark_actor_pidfd_lost(context):
 actor_pidfd_provenance(context);context[b"actor_pidfd_exit_ready_observed"]=True
 context[b"actor_state"]=b"PIDFD_ACTOR_LOST";context[b"actor_lost"]=True;context[b"release_disabled"]=True;context[b"faults"].add(b"PIDFD_ACTOR_LOST")

def mark_outer_pidfd_ready(context):
 number=context.get(b"outer_pidfd",-1);provenance=context.get(b"outer_pidfd_provenance")
 need(number>=0 and provenance==(number,context[b"outer_pid"],context[b"outer_starttime"]))
 context[b"pidfd_exit_ready_observed"]=True;context[b"outer_pidfd_offer_state"]=b"POST_READY_CACHED_PROVENANCE"

def mark_control_lost(context):
 context[b"control_state"]=b"CONTROL_LOST";context[b"release_disabled"]=True;context[b"faults"].add(b"CONTROL_LOST")

def read_late_refusal_candidate(control,context):
 refusal_lock_invariant(context)
 return receive_refusal_candidate_once(control,context)

def owner_poll(control,context,until):
 locked=refusal_lock_invariant(context)
 finality_deadline=0
 if locked:
  cached=refusal_slot(context)
  if cached[8]==b"OPEN":
   finality_deadline=cached[1][6];now=time.monotonic_ns()
   if now>=finality_deadline:
    try:finalize_refusal_cap_hold(context)
    except BaseException:
     context[b"refusal_finality_timeout_observed"]=True;context[b"faults"].add(b"RECONCILIATION_UNKNOWN")
   else:until=min(until,finality_deadline)
 need(type(until)is int and until>0)
 poller=select.poll();actor_registered=False;control_fd=-1
 if context.get(b"actor_state")!=b"PIDFD_ACTOR_LOST":
  try:register_lifecycle_poller(context,poller,b"actor_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL);actor_registered=True
  except BaseException:
   if locked:context[b"faults"].add(b"RECONCILIATION_UNKNOWN")
 if control is not None and context[b"control_state"]!=b"CONTROL_LOST":
  try:control_fd=control.fileno();need(control_fd>=0);poller.register(control_fd,select.POLLIN|select.POLLHUP|select.POLLERR)
  except BaseException:
   control_fd=-1;mark_control_lost(context)
 try:events=poller.poll(max(1,min(50,max(1,(until-time.monotonic_ns()+999999)//1000000))))
 except InterruptedError:return
 except BaseException:
  if locked:context[b"faults"].add(b"RECONCILIATION_UNKNOWN")
  return
 cmask=amask=0
 for number,event in events:
  if actor_registered and number==4:amask|=event
  elif control_fd>=0 and number==control_fd:cmask|=event
 if locked:
  if cmask&select.POLLIN:read_late_refusal_candidate(control,context)
  if pidfd_ready_event(amask):
   context[b"refusal_actor_loss_seen"]=True;mark_actor_pidfd_lost(context)
  if cmask&(select.POLLHUP|select.POLLERR):
   if not context[b"refusal_control_eof"]:read_late_refusal_candidate(control,context)
   if context[b"refusal_control_eof"]:mark_control_lost(context)
  cached=refusal_slot(context)
  if cached[8]==b"OPEN":
   finality_deadline=cached[1][6]
   if context[b"refusal_actor_loss_seen"] and context[b"refusal_control_eof"] and time.monotonic_ns()<=finality_deadline:
    try:finalize_refusal_actor_loss(context)
    except BaseException:context[b"faults"].add(b"RECONCILIATION_UNKNOWN")
   cached=refusal_slot(context)
   if cached[8]==b"OPEN" and time.monotonic_ns()>=finality_deadline:
    try:finalize_refusal_cap_hold(context)
    except BaseException:
     context[b"refusal_finality_timeout_observed"]=True;context[b"faults"].add(b"RECONCILIATION_UNKNOWN")
  refusal_lock_invariant(context);return
 if amask:
  mark_actor_pidfd_lost(context)
 if cmask&select.POLLIN:
  if not locked:
   try:
    raw,fds=recv_monitored(control,context,4,min(until,time.monotonic_ns()+ACK_NS),0,b"OWNER_POLL",b"NONE",b"NONE");need(fds==())
    context[b"faults"].add(b"CONTROL_MALFORMED")
   except RemoteAbort as error:
    values=error.values;context[b"faults"].update(error.faults);context[b"release_disabled"]=values[b"release_disabled"]==b"1";context[b"stage_present"]=values[b"stage_present"]==b"1"
   except PidfdActorLost:mark_actor_pidfd_lost(context)
   except ControlLost:mark_control_lost(context)
   except FaultSet as error:context[b"faults"].update(error.faults)
 if cmask&(select.POLLHUP|select.POLLERR) and not cmask&select.POLLIN:mark_control_lost(context)

def retained_until_empty(control,context,stop):
 if time.monotonic_ns()<=context[b"cleanup_effect_deadline"]:retained_record(context,stop)
 while time.monotonic_ns()<=context[b"cleanup_effect_deadline"]:
  for key in (b"out_fd",b"err_fd"):
   number=context.get(key,-1)
   if number>=0:
    try:drain(number,bytearray())
    except FaultSet as error:context[b"faults"].update(error.faults)
  owner_poll(control,context,context[b"cleanup_effect_deadline"]);state=observe_population(context);context[b"last_population"]=state
  if state is False:return True
 return False

def direct_reap_value(context,actor_lost):
 if context[b"direct_reaps"]==context[b"entered"] and context[b"entered"]>0:return b"COMPLETE"
 if b"DIRECT_WAIT_UNKNOWN" in context[b"faults"]:return b"UNKNOWN"
 if actor_lost:return b"UNAVAILABLE_ACTOR_LOST"
 return b"UNKNOWN"

def recovery_record(context,stop):
 freeze_failure_deadlines(context);start=context[b"cleanup_effect_deadline"];deadline=context[b"recovery_deadline"]
 while time.monotonic_ns()<start:owner_poll(context.get(b"actor_control"),context,start)
 need(start<=time.monotonic_ns()<=deadline)
 population=observe_population(context);context[b"last_population"]=population
 need(not context[b"payload_release_possible"] or population is False)
 actor_lost=context[b"actor_state"]==b"PIDFD_ACTOR_LOST"
 if actor_lost:context[b"faults"].add(b"PIDFD_ACTOR_LOST")
 need(actor_lost==(b"PIDFD_ACTOR_LOST" in context[b"faults"]))
 direct=direct_reap_value(context,actor_lost)
 seq=next_record(context);predecessor=context[b"chain_sha"]
 body=(b"P27E001_RECOVERY_STATE_V15\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+predecessor+b"\nSTOP_PROBE="+stop+b"\nPRIMARY="+primary(context[b"faults"])+b"\nFAULT_SET="+fault_csv(context[b"faults"])+b"\nINTENT_DURABLE="+(b"1" if context[b"intent_durable"] else b"0")+b"\nCONSUMPTION_STATE="+context[b"consumption_state"]+b"\nSTAGE_STATE="+context[b"stage_state"]+b"\nCONTAINMENT_STATE="+(b"BOUND" if context[b"containment_bound"] else b"NOT_APPLICABLE")+b"\nEMPTY_STATE="+(b"EMPTY" if population is False else b"NOT_APPLICABLE")+b"\nSTOPPED_COUNT="+str(context[b"stopped_count"]).encode()+b"\nDIRECT_REAP="+direct+b"\nSTDOUT_EOF="+(b"1" if context[b"last_out_eof"] else b"0")+b"\nSTDERR_EOF="+(b"1" if context[b"last_err_eof"] else b"0")+b"\nKILL_CALL_COUNT="+str(context[b"kill_call_count"]).encode()+b"\nKILL_STATE="+context[b"kill_state"]+b"\nKILL_TICKET_STATE="+context[b"kill_ticket_state"]+b"\nFAILURE_ORIGIN_NS="+str(context[b"failure_origin"]).encode()+b"\nCLEANUP_EFFECT_DEADLINE_NS="+str(context[b"cleanup_effect_deadline"]).encode()+b"\nRECOVERY_DEADLINE_NS="+str(deadline).encode()+b"\nTERMINAL_DEADLINE_NS="+str(context[b"terminal_deadline"]).encode()+b"\nRETRY_ALLOWED=0\nDISPOSITION="+disposition(context[b"faults"])+b"\nRECOVERY_END=1\n")
 state,digest=durable_once(context,b"recovery.v5",body,deadline,False,FINAL_TOTAL_NS,(b"RECOVERY",));context[b"recovery_state"]=state
 if state==DURABLE_VERIFIED:context[b"chain_sha"]=digest;context[b"recovery_sha"]=digest
 else:context[b"faults"].add(b"RECOVERY_DURABILITY_UNKNOWN")
 return state,digest

def validate_report_union(outcome,entered,stage,attempt,containment,empty,removal):
 need(outcome in (b"SUCCESS",b"FAILURE_CONTAINED",b"FAILURE_NO_PAYLOAD"))
 need(stage in (b"ABSENT_KNOWN",b"VERIFIED_PRESENT",b"UNKNOWN") and attempt==b"PUBLISHED")
 need(containment in (b"NOT_APPLICABLE",b"BOUND") and empty in (b"NOT_APPLICABLE",b"EMPTY") and removal in (b"NOT_APPLICABLE",b"REMOVED",b"RETAINED"))
 if containment==b"BOUND":need(stage==b"VERIFIED_PRESENT" and attempt==b"PUBLISHED" and empty==b"EMPTY" and removal in (b"REMOVED",b"RETAINED"))
 else:need(entered==0 and empty==removal==b"NOT_APPLICABLE")
 if outcome==b"SUCCESS":need(entered==15 and stage==b"VERIFIED_PRESENT" and attempt==b"PUBLISHED" and containment==b"BOUND" and empty==b"EMPTY" and removal==b"REMOVED")
 elif outcome==b"FAILURE_CONTAINED":need(containment==b"BOUND" and empty==b"EMPTY" and removal in (b"REMOVED",b"RETAINED"))
 else:need(entered==0 and containment==empty==removal==b"NOT_APPLICABLE")
 return True

def parse_final_report(raw):
 values=parse_fixed(raw,b"P27E001_FINAL_REPORT_V15",FINAL_REPORT_KEYS,b"RECORD_END=1")
 need(values[b"AUTH_ID"]==AUTH and values[b"SUITE"]==b",".join(PROBES));udec(values[b"RECORD_SEQ"],1);h64(values[b"PREDECESSOR_SHA256"])
 entered=udec(values[b"ENTERED_COUNT"],0,15);committed=udec(values[b"COMMITTED_COUNT"],0,15);reaped=udec(values[b"REAPED_COUNT"],0,15);stopped=udec(values[b"STOPPED_COUNT"],0,15)
 need(0<=committed<=reaped<=stopped<=entered<=15)
 ordinal=values[b"STOP_ORDINAL"];probe=values[b"STOP_PROBE"]
 if ordinal==b"NONE":need(probe==b"NONE")
 else:
  index=udec(ordinal,0,14);need(probe==PROBES[index] and index<entered)
 need(values[b"STAGE_STATE"] in (b"NOT_APPLICABLE",b"ABSENT_KNOWN",b"VERIFIED_PRESENT",b"UNKNOWN"))
 need(values[b"ATTEMPT_STATE"] in (b"NOT_APPLICABLE",b"ABSENT_KNOWN",b"PUBLISHED",b"RETAINED",b"COLLISION_CLOSED",b"UNKNOWN"))
 containment=values[b"CONTAINMENT_STATE"];empty=values[b"EMPTY_STATE"];removal=values[b"REMOVAL_STATE"]
 need(containment in (b"NOT_APPLICABLE",b"BOUND",b"UNKNOWN") and empty in (b"NOT_APPLICABLE",b"EMPTY",b"NONEMPTY",b"UNKNOWN") and removal in (b"NOT_APPLICABLE",b"REMOVED",b"RETAINED",b"UNKNOWN"))
 if containment==b"NOT_APPLICABLE":need(empty==removal==b"NOT_APPLICABLE" and entered==0)
 if containment==b"BOUND" and empty==b"EMPTY":need(removal in (b"REMOVED",b"RETAINED"))
 if empty==b"NONEMPTY":need(removal!=b"REMOVED")
 kill_count=udec(values[b"KILL_CALL_COUNT"],0,1);kill_state=values[b"KILL_STATE"];ticket=values[b"KILL_TICKET_STATE"]
 if kill_count==0:need(kill_state in (b"NOT_RESERVED",b"AUTHORITY_RESERVED",b"TICKET_COMMITTING",b"TICKET_DURABILITY_UNKNOWN",b"CALL_RESERVED",b"CALL_UNAVAILABLE",b"DEADLINE_PRECLUDED"))
 else:need(kill_state in (b"CALL_ENTERED",b"RETURN_UNKNOWN",b"SHORT_OR_UNKNOWN",b"RETURNED_2",b"RETURNED_2_EMPTY_CONFIRMED",b"RETURNED_2_POSTCHECK_UNKNOWN"))
 need(ticket in (b"ABSENT_KNOWN",DURABLE_VERIFIED,b"CARRIER_FAILED_NON_PENDING_PRE_EFFECT",b"OPEN_EFFECT_UNKNOWN",b"FD_HELD",b"WRITE_EFFECT_UNKNOWN",b"FILE_FSYNC_EFFECT_UNKNOWN",b"CREATED_FD_CLOSED",b"NAMED_REOPEN_EFFECT_UNKNOWN",b"NAMED_ENTRY_REREAD_VERIFIED",b"DIR_FSYNC_EFFECT_UNKNOWN"))
 h64(values[b"CHAIN_BEFORE_REPORT_SHA256"]);need(values[b"PREDECESSOR_SHA256"]==values[b"CHAIN_BEFORE_REPORT_SHA256"]);terminal_origin=udec(values[b"TERMINAL_ORIGIN_NS"],1);terminal_deadline=udec(values[b"TERMINAL_DEADLINE_NS"],1)
 schedule=check_schedule_hex(values[b"TERMINAL_SCHEDULE_HEX"],terminal_origin,terminal_deadline,TERMINAL_PHASE_SPEC);need(udec(values[b"PHASE_DEADLINE_NS"])==schedule[b"REPORT_RECORD"])
 need(values[b"ACK_STATE"]==b"AWAITING_TERMINAL_ACK" and values[b"RECONCILIATION_STATE"]==b"NOT_STARTED" and values[b"OWNER_CLOSURE_STATE"]==b"NOT_STARTED" and values[b"RETRY_ALLOWED"]==b"0")
 outcome=values[b"OUTCOME_KIND"]
 validate_report_union(outcome,entered,values[b"STAGE_STATE"],values[b"ATTEMPT_STATE"],containment,empty,removal)
 if outcome==b"SUCCESS":
  need(entered==committed==reaped==stopped==15 and ordinal==probe==b"NONE")
  need(values[b"STAGE_STATE"]==b"VERIFIED_PRESENT" and values[b"ATTEMPT_STATE"]==b"PUBLISHED" and containment==b"BOUND" and empty==b"EMPTY" and removal==b"REMOVED")
  need(values[b"PRIMARY"]==values[b"FAULT_SET"]==b"NONE" and kill_count==0 and kill_state==b"NOT_RESERVED" and ticket==b"ABSENT_KNOWN")
  need(values[b"FAILURE_ORIGIN_NS"]==values[b"CLEANUP_EFFECT_DEADLINE_NS"]==b"0" and values[b"CERTIFICATE_LIVE_AT_REPORT"]==b"1" and values[b"DISPOSITION"]==b"PASS_PENDING_COMMIT");return values
 need(outcome in (b"FAILURE_CONTAINED",b"FAILURE_NO_PAYLOAD"))
 faults=parse_fault_csv(values[b"FAULT_SET"],False);need(values[b"PRIMARY"]==primary(faults) and values[b"DISPOSITION"]==disposition(faults))
 failure_origin=udec(values[b"FAILURE_ORIGIN_NS"],1);cleanup=udec(values[b"CLEANUP_EFFECT_DEADLINE_NS"],1)
 need(cleanup==failure_origin+CLEANUP_EFFECT_NS and terminal_deadline==failure_origin+FAILURE_TOTAL_NS and terminal_origin==cleanup+RECOVERY_RECORD_NS)
 if outcome==b"FAILURE_CONTAINED":need(containment==b"BOUND" and empty==b"EMPTY")
 else:need(entered==0 and containment==empty==removal==b"NOT_APPLICABLE")
 need(values[b"CERTIFICATE_LIVE_AT_REPORT"] in (b"0",b"1"));return values

def validate_report_constructor_context(context,outcome,stage,attempt,containment,empty,removal):
 need(context[b"consumed"] and context[b"intent_durable"] and context[b"commit_count"]==context[b"intent_count"]==1)
 need(context[b"attempt"]>=0 and context[b"local_fd_state"]==context[b"attempt_state"]==attempt==b"PUBLISHED")
 if stage==b"VERIFIED_PRESENT":need(context[b"stage_present"] and type(context[b"stage_identity"]) is tuple and len(context[b"stage_identity"])==6)
 else:need(not context[b"stage_present"] and context[b"stage_identity"] is None)
 if containment==b"BOUND":
  need(context[b"containment_bound"] and context[b"consumed"] and context[b"stage_state"]==b"VERIFIED_PRESENT" and context[b"stage_present"])
  need(type(context.get(b"cgroup_identity")) is tuple and len(context[b"cgroup_identity"])==6 and empty==b"EMPTY" and context[b"last_population"] is False)
 else:need(not context[b"containment_bound"] and not context[b"payload_release_possible"] and empty==removal==b"NOT_APPLICABLE")
 if outcome==b"SUCCESS":need(not context[b"faults"] and context[b"removed"] and removal==b"REMOVED")
 elif outcome==b"FAILURE_CONTAINED":need(context[b"faults"] and containment==b"BOUND")
 else:need(context[b"faults"] and context[b"entered"]==0 and not context[b"payload_release_possible"] and containment==b"NOT_APPLICABLE")
 return True

def report_common(context,stop,outcome,schedule):
 entered=context[b"entered"];committed=sum(context[b"committed"]);reaped=context[b"direct_reaps"];stopped=context[b"stopped_count"];need(0<=committed<=reaped<=stopped<=entered<=15)
 stop_ordinal=b"NONE" if stop==b"NONE" else str(PROBES.index(stop)).encode()
 stage=context.get(b"stage_state",b"UNKNOWN");attempt=context.get(b"attempt_state",context.get(b"local_fd_state",b"UNKNOWN"))
 population=context.get(b"last_population")
 if not context[b"containment_bound"]:containment=b"NOT_APPLICABLE";empty=b"NOT_APPLICABLE";removal=b"NOT_APPLICABLE"
 else:
  containment=b"BOUND";empty=b"EMPTY" if population is False else (b"NONEMPTY" if population is True else b"UNKNOWN")
  removal=b"REMOVED" if context[b"removed"] else (b"RETAINED" if empty==b"EMPTY" else b"UNKNOWN")
 faults=context[b"faults"];certificate_live=b"1"
 try:checkpoint(CERT,0,schedule[b"REPORT_RECORD"])
 except BaseException:certificate_live=b"0"
 predecessor=context[b"chain_sha"]
 rows=((b"OUTCOME_KIND",outcome),(b"SUITE",b",".join(PROBES)),(b"ENTERED_COUNT",str(entered).encode()),(b"COMMITTED_COUNT",str(committed).encode()),(b"REAPED_COUNT",str(reaped).encode()),(b"STOPPED_COUNT",str(stopped).encode()),(b"STOP_ORDINAL",stop_ordinal),(b"STOP_PROBE",stop),(b"STAGE_STATE",stage),(b"ATTEMPT_STATE",attempt),(b"CONTAINMENT_STATE",containment),(b"EMPTY_STATE",empty),(b"REMOVAL_STATE",removal),(b"PRIMARY",b"NONE" if not faults else primary(faults)),(b"FAULT_SET",b"NONE" if not faults else fault_csv(faults)),(b"CHAIN_BEFORE_REPORT_SHA256",predecessor),(b"KILL_CALL_COUNT",str(context[b"kill_call_count"]).encode()),(b"KILL_STATE",context[b"kill_state"]),(b"KILL_TICKET_STATE",context[b"kill_ticket_state"]),(b"ACK_STATE",b"AWAITING_TERMINAL_ACK"),(b"RECONCILIATION_STATE",b"NOT_STARTED"),(b"OWNER_CLOSURE_STATE",b"NOT_STARTED"),(b"FAILURE_ORIGIN_NS",b"0" if outcome==b"SUCCESS" else str(context[b"failure_origin"]).encode()),(b"CLEANUP_EFFECT_DEADLINE_NS",b"0" if outcome==b"SUCCESS" else str(context[b"cleanup_effect_deadline"]).encode()),(b"TERMINAL_ORIGIN_NS",str(context[b"terminal_origin"]).encode()),(b"TERMINAL_DEADLINE_NS",str(context[b"terminal_deadline"]).encode()),(b"TERMINAL_SCHEDULE_HEX",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"CERTIFICATE_LIVE_AT_REPORT",certificate_live),(b"RETRY_ALLOWED",b"0"),(b"DISPOSITION",b"PASS_PENDING_COMMIT" if outcome==b"SUCCESS" else disposition(faults)))
 validate_report_constructor_context(context,outcome,stage,attempt,containment,empty,removal)
 validate_report_union(outcome,entered,stage,attempt,containment,empty,removal);return rows

def durable_prevalidated_report(context,stop,outcome,schedule,deadline,require_live,reserve_after,delta_kind):
 need(delta_kind in (b"FAILURE_REPORT",b"SUCCESS_REPORT") and time.monotonic_ns()<=deadline)
 need(not context.get(b"record_sequence_frozen") and context.get(b"record_pending") is None and context.get(b"record_draft") is None)
 lines=report_common(context,stop,outcome,schedule);seq_number=context[b"record_seq"]+1;seq=str(seq_number).encode();predecessor=context[b"chain_sha"]
 body=b"P27E001_FINAL_REPORT_V15\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+predecessor+b"\n"+b"".join(key+b"="+value+b"\n" for key,value in lines)+b"PHASE_DEADLINE_NS="+str(deadline).encode()+b"\nRECORD_END=1\n"
 prevalidated=parse_final_report(body)
 need(prevalidated[b"RECORD_SEQ"]==seq and prevalidated[b"PREDECESSOR_SHA256"]==predecessor and context[b"record_seq"]+1==seq_number and context[b"chain_sha"]==predecessor)
 need(not context.get(b"record_sequence_frozen") and context.get(b"record_pending") is None and context.get(b"record_draft") is None)
 context[b"record_draft"]=(seq_number,predecessor,None,None);context[b"carrier_pre_effect_state"]=b"DRAFT_NON_PENDING_PRE_EFFECT"
 state,digest=durable_once(context,b"report.v5",body,deadline,require_live,reserve_after,(delta_kind,str(deadline).encode()))
 if state!=DURABLE_VERIFIED:raise FaultSet({b"REPORT_DURABILITY_UNKNOWN"})
 postvalidated=parse_final_report(body);need(postvalidated==prevalidated and context[b"chain_sha"]==digest)
 return body,digest

def failure_report(context,stop,schedule):
 outcome=b"FAILURE_CONTAINED" if context[b"containment_bound"] else b"FAILURE_NO_PAYLOAD"
 if outcome==b"FAILURE_CONTAINED":need(context[b"last_population"] is False)
 else:need(not context[b"payload_release_possible"] and context[b"entered"]==0)
 deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"REPORT_RECORD",context[b"terminal_deadline"],False)
 body,digest=durable_prevalidated_report(context,stop,outcome,schedule,deadline,False,context[b"terminal_deadline"]-deadline,b"FAILURE_REPORT")
 context[b"report_state"]=DURABLE_VERIFIED;context[b"report_sha"]=digest;context[b"outcome_durable"]=True;return digest

def terminal_candidate_record(context,mode,stop,schedule):
 need(mode in (b"SUCCESS",b"FAILURE"));deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"CANDIDATE_RECORD",context[b"terminal_deadline"],mode==b"SUCCESS")
 if mode==b"SUCCESS":
  need(context[b"entered"]==sum(context[b"committed"])==context[b"direct_reaps"]==context[b"stopped_count"]==15)
  need(context[b"stage_state"]==b"VERIFIED_PRESENT" and context[b"containment_bound"] and context[b"last_population"] is False and context[b"removed"] and not context[b"faults"])
  claim=b"SUCCESS_ELIGIBLE_NOT_PASS";outcome=b"SUCCESS_CANDIDATE"
 else:
  claim=b"FAILURE_DURABLE_PENDING_SEEN";outcome=b"FAILURE_CANDIDATE"
 predecessor=context[b"chain_sha"];lines=((b"OUTCOME_KIND",outcome),(b"CANDIDATE_CLAIM",claim),(b"STOP_PROBE",stop),(b"ENTERED_COUNT",str(context[b"entered"]).encode()),(b"COMMITTED_COUNT",str(sum(context[b"committed"])).encode()),(b"REAPED_COUNT",str(context[b"direct_reaps"]).encode()),(b"STOPPED_COUNT",str(context[b"stopped_count"]).encode()),(b"STAGE_STATE",context[b"stage_state"]),(b"CONTAINMENT_STATE",b"BOUND" if context[b"containment_bound"] else b"NOT_APPLICABLE"),(b"EMPTY_STATE",b"EMPTY" if context[b"last_population"] is False else b"NOT_APPLICABLE"),(b"REMOVAL_STATE",b"REMOVED" if context[b"removed"] else b"NOT_APPLICABLE"),(b"KILL_CALL_COUNT",str(context[b"kill_call_count"]).encode()),(b"KILL_STATE",context[b"kill_state"]),(b"CHAIN_BEFORE_CANDIDATE_SHA256",predecessor),(b"TERMINAL_ORIGIN_NS",str(context[b"terminal_origin"]).encode()),(b"TERMINAL_DEADLINE_NS",str(context[b"terminal_deadline"]).encode()),(b"TERMINAL_SCHEDULE_HEX",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"RETRY_ALLOWED",b"0"))
 body,digest=chained_record(context,b"terminal-candidate.v5" if mode==b"SUCCESS" else b"failure-candidate.v5",b"P27E001_TERMINAL_CANDIDATE_V15",lines,deadline,mode==b"SUCCESS",context[b"terminal_deadline"]-deadline,(b"TERMINAL_CANDIDATE",))
 context[b"candidate_sha"]=digest;return digest

def terminal_seen_record(context,mode,candidate_sha,notice_raw,seen_raw,schedule):
 deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"TERMINAL_SEEN_RECORD",context[b"terminal_deadline"],mode==b"SUCCESS")
 lines=((b"OUTCOME_KIND",b"SUCCESS" if mode==b"SUCCESS" else b"FAILURE"),(b"CANDIDATE_SHA256",candidate_sha),(b"NOTICE_PACKET_SHA256",sha(notice_raw)),(b"ACTOR_SEEN_PACKET_SHA256",sha(seen_raw)),(b"ACTOR_SEEN_MESSAGE_SEQ",str(CONTROL_RECV_SEQ).encode()),(b"TERMINAL_SCHEDULE_HEX",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"NO_REPLAY",b"1"))
 body,digest=chained_record(context,b"terminal-seen.v5",b"P27E001_TERMINAL_SEEN_V15",lines,deadline,mode==b"SUCCESS",context[b"terminal_deadline"]-deadline,(b"TERMINAL_SEEN",))
 context[b"terminal_seen_sha"]=digest;return digest

def success_report_and_pass(context,schedule):
 report_deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"REPORT_RECORD",context[b"terminal_deadline"],True)
 body,report_sha=durable_prevalidated_report(context,b"NONE",b"SUCCESS",schedule,report_deadline,True,context[b"terminal_deadline"]-report_deadline,b"SUCCESS_REPORT")
 context[b"report_state"]=DURABLE_VERIFIED;context[b"report_sha"]=report_sha
 pass_deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"PASS_COMMIT",context[b"terminal_deadline"],True)
 token=sha(b"P27E001V15_RECONCILE\x00"+AUTH+b"\x00"+report_sha+b"\x00"+context[b"terminal_seen_sha"]+b"\x00"+schedule_hex(schedule,TERMINAL_PHASE_SPEC))
 context[b"pass_effect_possible"]=True
 lines=((b"OUTCOME_KIND",b"PASS"),(b"REPORT_SHA256",report_sha),(b"TERMINAL_SEEN_SHA256",context[b"terminal_seen_sha"]),(b"RECONCILIATION_TOKEN",token),(b"PASS",b"1"),(b"PASS_DEADLINE_NS",str(pass_deadline).encode()),(b"TERMINAL_SCHEDULE_HEX",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"RETRY_ALLOWED",b"0"))
 body,pass_sha=chained_record(context,b"pass-commit.v5",b"P27E001_PASS_COMMIT_V15",lines,pass_deadline,True,context[b"terminal_deadline"]-pass_deadline,(b"PASS_COMMIT",token))
 context[b"pass_committed"]=True;context[b"outcome_durable"]=True;context[b"pass_sha"]=pass_sha;context[b"reconciliation_token"]=token
 margin_deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"PASS_MARGIN",context[b"terminal_deadline"],True)
 while time.monotonic_ns()<margin_deadline:owner_poll(context.get(b"actor_control"),context,margin_deadline)
 need(time.monotonic_ns()<=margin_deadline);return report_sha,pass_sha,token

def ack_receipt_record(context,mode,receipt_raw,schedule,actor_lost=False):
 deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"ACK_RECEIPT_RECORD",context[b"terminal_deadline"],False)
 state=b"PIDFD_ACTOR_LOST_NO_REPLAY" if actor_lost else b"ACTOR_ACK_RECEIPT"
 packet_sha=b"NONE" if actor_lost else sha(receipt_raw)
 lines=((b"OUTCOME_KIND",mode),(b"ACK_RECEIPT_STATE",state),(b"ACTOR_RECEIPT_PACKET_SHA256",packet_sha),(b"REPORT_SHA256",context[b"report_sha"]),(b"PASS_SHA256",context.get(b"pass_sha",b"NONE")),(b"RECONCILIATION_TOKEN",context.get(b"reconciliation_token",b"NONE")),(b"NO_REPLAY",b"1"),(b"TERMINAL_SCHEDULE_HEX",schedule_hex(schedule,TERMINAL_PHASE_SPEC)))
 body,digest=chained_record(context,b"ack-receipt.v5",b"P27E001_ACK_RECEIPT_V15",lines,deadline,False,context[b"terminal_deadline"]-deadline,(b"ACK_RECEIPT",));context[b"ack_receipt_sha"]=digest;return digest

def reconciliation_record(context,mode,schedule):
 deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"RECONCILIATION_RECORD",context[b"terminal_deadline"],False)
 lines=((b"OUTCOME_KIND",mode),(b"ACK_RECEIPT_SHA256",context[b"ack_receipt_sha"]),(b"REPORT_SHA256",context[b"report_sha"]),(b"RECONCILIATION_TOKEN",context.get(b"reconciliation_token",b"NONE")),(b"NO_REPLAY",b"1"),(b"TERMINAL_SCHEDULE_HEX",schedule_hex(schedule,TERMINAL_PHASE_SPEC)))
 body,digest=chained_record(context,b"reconciliation.v5",b"P27E001_RECONCILIATION_V15",lines,deadline,False,context[b"terminal_deadline"]-deadline,(b"RECONCILIATION",));context[b"reconciliation_sha"]=digest;return digest

def owner_closure_record(context,mode,schedule):
 deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"OWNER_CLOSURE_RECORD",context[b"terminal_deadline"],False)
 safe=terminal_safe(context);need(safe)
 lines=((b"OUTCOME_KIND",mode),(b"RECONCILIATION_SHA256",context[b"reconciliation_sha"]),(b"REPORT_SHA256",context[b"report_sha"]),(b"CONTAINMENT_SAFE",b"1"),(b"CONTROL_STATE",context[b"control_state"]),(b"ACTOR_STATE",context[b"actor_state"]),(b"OWNER_STATE",b"OWNER_CLOSED_DURABLE"),(b"NO_REPLAY",b"1"),(b"TERMINAL_SCHEDULE_HEX",schedule_hex(schedule,TERMINAL_PHASE_SPEC)))
 body,digest=chained_record(context,b"owner-closure.v5",b"P27E001_OWNER_CLOSURE_V15",lines,deadline,False,context[b"terminal_deadline"]-deadline,(b"OWNER_CLOSURE",));context[b"owner_closure_sha"]=digest;return digest

def send_result(control,ordinal,probe,pid,context,stdout,stderr,out_eof,err_eof,out_over,err_over,empty,faults,done):
 deadline=context[b"origin"]+HOST_NS;out_frames=(len(stdout)+64999)//65000;err_frames=(len(stderr)+64999)//65000
 header=packet(b"V15_RESULT",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"outer_pid",str(pid).encode()),(b"pidfd_bound",b"1" if context[b"pidfd_bound"] else b"0"),(b"pidfd_exit_ready_observed",b"1" if context[b"pidfd_exit_ready_observed"] else b"0"),(b"stdout_len",str(len(stdout)).encode()),(b"stdout_sha256",sha(stdout)),(b"stdout_eof",b"1" if out_eof else b"0"),(b"stdout_frames",str(out_frames).encode()),(b"stderr_len",str(len(stderr)).encode()),(b"stderr_sha256",sha(stderr)),(b"stderr_eof",b"1" if err_eof else b"0"),(b"stderr_frames",str(err_frames).encode()),(b"cgroup_empty",b"1" if empty else b"0"),(b"fault_set",fault_csv(faults)),(b"capture_done_ns",str(done).encode()),(b"result_deadline_ns",str(deadline).encode())))
 send_exact(control,header,deadline)
 for stream,raw in ((b"STDOUT",stdout),(b"STDERR",stderr)):
  for index,start in enumerate(range(0,len(raw),65000)):
   payload=raw[start:start+65000]
   frame=packet(b"V15_RESULT_FRAME",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"stream",stream),(b"index",str(index).encode()),(b"bytes",str(len(payload)).encode()),(b"sha256",sha(payload)),(b"result_deadline_ns",str(deadline).encode())))+payload
   send_exact(control,frame,deadline)
 end=packet(b"V15_RESULT_END",((b"state",b"RESULT_END"),(b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"result_deadline_ns",str(deadline).encode())));send_exact(control,end,deadline)

def set_actor_receive(context,state,ordinal,probe,deadline):
 receiver_binding(state,ordinal,probe,deadline)
 context[b"actor_receive_state"]=state;context[b"actor_receive_ordinal"]=ordinal;context[b"actor_receive_probe"]=probe;context[b"actor_receive_deadline"]=deadline

def stream_arm(control,context,ordinal,probe):
 keys=(b"ordinal",b"probe",b"release_origin_ns",b"launch_deadline_ns",b"stdout_dev",b"stdout_ino",b"stderr_dev",b"stderr_ino",b"events_dev",b"events_ino",b"leaf_identity_sha256",b"kill_authority_source")
 fds=();out=err=events=-1
 try:
  receive_ceiling=time.monotonic_ns()+ACK_NS;set_actor_receive(context,b"WAIT_STREAMS_ARMED",str(ordinal).encode(),probe,receive_ceiling)
  stream_slots=((b"stream_out_received",b"OUT_FD",True),(b"stream_err_received",b"ERR_FD",True),(b"stream_events_received",b"EVENTS_FD",True))
  raw,fds=recv_monitored(control,context,4,receive_ceiling,3,b"WAIT_STREAM_ARM",str(ordinal).encode(),probe,stream_slots);need(len(fds)==3)
  out,err,events=fds;fds=()
  values=parse_packet(raw,b"V15_STREAM_ARM",keys,received_binding(raw,b"WAIT_STREAM_ARM",str(ordinal).encode(),probe,b"launch_deadline_ns",receive_ceiling))
  need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe and values[b"kill_authority_source"]==b"WATCHDOG_ROOT_KILL_FD_ONLY")
  origin=udec(values[b"release_origin_ns"],1);launch=udec(values[b"launch_deadline_ns"],1);need(origin<launch==origin+1000000000)
  post_deadline(launch);checkpoint(CERT,horizon_needed(origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),launch)
  fd_access(out,os.O_RDONLY);fd_access(err,os.O_RDONLY);fd_access(events,os.O_RDONLY)
  need(fcntl.fcntl(out,fcntl.F_GETFL)&os.O_NONBLOCK and fcntl.fcntl(err,fcntl.F_GETFL)&os.O_NONBLOCK)
  outs=os.fstat(out);errs=os.fstat(err);eventss=os.fstat(events)
  need(stat.S_ISFIFO(outs.st_mode) and stat.S_ISFIFO(errs.st_mode) and (outs.st_dev,outs.st_ino)!=(errs.st_dev,errs.st_ino))
  need((outs.st_dev,outs.st_ino)==(udec(values[b"stdout_dev"],1),udec(values[b"stdout_ino"],1)))
  need((errs.st_dev,errs.st_ino)==(udec(values[b"stderr_dev"],1),udec(values[b"stderr_ino"],1)))
  need((eventss.st_dev,eventss.st_ino)==(udec(values[b"events_dev"],1),udec(values[b"events_ino"],1)))
  a=os.fstat(context[b"root_events_fd"]);cg=os.fstat(context[b"cgfd"]);need((a.st_dev,a.st_ino)==(eventss.st_dev,eventss.st_ino))
  leaf_identity=sha(str(cg.st_dev).encode()+b":"+str(cg.st_ino).encode()+b":"+str(eventss.st_dev).encode()+b":"+str(eventss.st_ino).encode());need(values[b"leaf_identity_sha256"]==leaf_identity);unique_kill_authority(context,True)
  promote_lifecycle_fd(context,b"stream_out_received",b"out_fd",b"OUT_FD",True);promote_lifecycle_fd(context,b"stream_err_received",b"err_fd",b"ERR_FD",True);promote_lifecycle_fd(context,b"stream_events_received",b"events_fd",b"EVENTS_FD",True)
  context.update({b"origin":origin,b"launch":launch,b"pidfd_bound":False,b"pidfd_exit_ready_observed":False})
  out=err=events=-1
  reply=packet(b"V15_STREAMS_ARMED",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"sole_kill_capability",b"ROOT_KILL_FD"),(b"launch_deadline_ns",str(launch).encode())))
  send_exact(control,reply,launch);checkpoint(CERT,horizon_needed(origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),launch)
 finally:
  close_lifecycle_slots(context,(b"stream_out_received",b"stream_err_received",b"stream_events_received"))

def pidfd_arm(control,context,ordinal,probe):
 fds=();number=procs=status=-1
 try:
  set_actor_receive(context,b"WAIT_PIDFD_ARMED",str(ordinal).encode(),probe,context[b"launch"])
  raw,fds=recv_monitored(control,context,4,context[b"launch"],1,b"WAIT_PIDFD_ARM",str(ordinal).encode(),probe,((b"outer_pidfd_received",b"OUTER_PIDFD",True),));need(len(fds)==1)
  number=fds[0];fds=()
  values=parse_packet(raw,b"V15_PIDFD_ARM",(b"ordinal",b"probe",b"outer_pid",b"outer_starttime",b"stopped_raw_status",b"cgroup_member",b"pidfd_bound"),receiver_binding(b"WAIT_PIDFD_ARM",str(ordinal).encode(),probe,context[b"launch"]))
  need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe)
  pid=udec(values[b"outer_pid"],2);starttime=udec(values[b"outer_starttime"],1);stopped=udec(values[b"stopped_raw_status"],1)
  need(os.WIFSTOPPED(stopped) and os.WSTOPSIG(stopped)==signal.SIGSTOP and values[b"cgroup_member"]==values[b"pidfd_bound"]==b"1")
  fd_access(number,os.O_RDWR);need(pidfd_pid(number)==pid and proc_starttime(pid)==starttime)
  watcher=select.poll();register_lifecycle_poller(context,watcher,b"outer_pidfd_received",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL);need(watcher.poll(0)==[])
  procs=acquire_lifecycle_open(context,b"pidfd_arm_procs_fd",b"CGROUP_PROCS_OBSERVATION_FD",b"cgroup.procs",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"cgfd"])
  status=acquire_lifecycle_open(context,b"pidfd_arm_status_fd",b"PROC_STATUS_OBSERVATION_FD",b"/proc/"+str(pid).encode()+b"/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
  need(read_all(procs,64)==str(pid).encode()+b"\n")
  state=[x for x in ascii_file(read_all(status,65536),65536).splitlines() if x.startswith(b"State:\t")]
  need(len(state)==1 and state[0].startswith(b"State:\tT") and watcher.poll(0)==[])
  need(pidfd_pid(number)==pid and proc_starttime(pid)==starttime and read_all(procs,64)==str(pid).encode()+b"\n")
  need(context.get(b"outer_pidfd",-1)<0)
  prior_provenance=context.get(b"outer_pidfd_provenance");prior_facts=context.get(b"last_outer_pidfd_causal_facts")
  if prior_provenance is not None:need(type(prior_facts)is tuple and len(prior_facts)==5 and prior_facts[0]==prior_provenance)
  provenance=(number,pid,starttime);promote_lifecycle_fd(context,b"outer_pidfd_received",b"outer_pidfd",b"OUTER_PIDFD",True,provenance);number=-1;context[b"outer_pid"]=pid;context[b"outer_starttime"]=starttime;context[b"outer_pidfd_provenance"]=provenance
  register_lifecycle_poller(context,context[b"offer_snapshot_poller"],b"outer_pidfd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL);context[b"offer_snapshot_outer_fd"]=context[b"outer_pidfd"]
  context[b"pidfd_bound"]=True;context[b"pidfd_exit_ready_observed"]=False;context[b"outer_pidfd_close_state"]=b"LIVE_PRE_READY";context[b"outer_pidfd_offer_state"]=b"NOT_FROZEN";context[b"outer_release_record_identity"]=None;context[b"outer_offer_binding"]=None;context[b"stopped_count"]+=1
  reply=packet(b"V15_PIDFD_ARMED",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"pidfd_bound",b"1"),(b"outer_pid",str(pid).encode()),(b"outer_starttime",str(starttime).encode()),(b"launch_deadline_ns",str(context[b"launch"]).encode())))
  send_exact(control,reply,context[b"launch"]);checkpoint(CERT,horizon_needed(context[b"origin"]+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),context[b"launch"])
 finally:
  close_lifecycle_slots(context,(b"outer_pidfd_received",b"pidfd_arm_procs_fd",b"pidfd_arm_status_fd"))

def release_phase(control,context,ordinal,probe):
 set_actor_receive(context,b"WAIT_RELEASE_DURABLE",str(ordinal).encode(),probe,context[b"launch"])
 raw,fds=recv_monitored(control,context,4,context[b"launch"],0,b"WAIT_RELEASE",str(ordinal).encode(),probe);need(fds==())
 keys=(b"ordinal",b"probe",b"outer_pid",b"outer_starttime",b"pidfd_bound",b"stopped_raw_status",b"cgroup_member",b"cgroup_dev",b"cgroup_ino",b"cgroup_mode",b"cgroup_nlink",b"cgroup_uid",b"cgroup_gid",b"argv_sha256",b"env_sha256",b"release_origin_ns",b"launch_overall_deadline_ns",b"release_record_deadline_ns",b"release_reply_deadline_ns",b"launch_deadline_ns")
 values=parse_packet(raw,b"V15_RELEASE_CANDIDATE",keys,receiver_binding(b"WAIT_RELEASE",str(ordinal).encode(),probe,context[b"launch"]))
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe and udec(values[b"outer_pid"],2)==context[b"outer_pid"] and udec(values[b"outer_starttime"],1)==context[b"outer_starttime"] and values[b"pidfd_bound"]==values[b"cgroup_member"]==b"1")
 h64(values[b"argv_sha256"]);h64(values[b"env_sha256"]);need(udec(values[b"release_origin_ns"])==context[b"origin"] and udec(values[b"launch_overall_deadline_ns"])==context[b"launch"])
 record_deadline=udec(values[b"release_record_deadline_ns"]);reply_deadline=udec(values[b"release_reply_deadline_ns"])
 set_actor_receive(context,b"WAIT_RELEASE_DURABLE",str(ordinal).encode(),probe,reply_deadline)
 need(record_deadline==context[b"origin"]+RELEASE_RECORD_OFFSET_NS and reply_deadline==context[b"origin"]+RELEASE_REPLY_OFFSET_NS and udec(values[b"launch_deadline_ns"])==record_deadline and time.monotonic_ns()<=record_deadline)
 cg=os.fstat(context[b"cgfd"]);observed=(cg.st_dev,cg.st_ino,format(cg.st_mode,"o").encode(),cg.st_nlink,cg.st_uid,cg.st_gid)
 supplied=(udec(values[b"cgroup_dev"],1),udec(values[b"cgroup_ino"],1),values[b"cgroup_mode"],udec(values[b"cgroup_nlink"],1),udec(values[b"cgroup_uid"]),udec(values[b"cgroup_gid"]))
 need(observed==supplied)
 checkpoint(CERT,horizon_needed(context[b"origin"]+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),record_deadline);digest=release_record(context,values)
 need(context.get(b"outer_release_record_identity") is None);context[b"outer_release_record_identity"]=(digest,str(ordinal).encode(),probe)
 context[b"payload_release_possible"]=True;context[b"release_send_state"]=b"RELEASE_DURABLE_SEND_EFFECT_UNKNOWN"
 reply=packet(b"V15_RELEASE_DURABLE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"release_sha256",digest),(b"launch_overall_deadline_ns",str(context[b"launch"]).encode()),(b"release_record_deadline_ns",str(record_deadline).encode()),(b"release_reply_deadline_ns",str(reply_deadline).encode()),(b"launch_deadline_ns",str(reply_deadline).encode())))
 send_exact(control,reply,reply_deadline);context[b"release_send_state"]=b"RELEASE_DURABLE_SENT";checkpoint(CERT,horizon_needed(context[b"origin"]+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),context[b"launch"])

def monitor_probe(control,context,ordinal,probe):
 stdout=bytearray();stderr=bytearray();out_eof=err_eof=out_over=err_over=False;faults=set();actor_lost=False
 deadline=context[b"origin"]+HOST_NS;set_actor_receive(context,b"WAIT_RESULT",str(ordinal).encode(),probe,deadline);poller=select.poll()
 for number in (context[b"out_fd"],context[b"err_fd"],context[b"events_fd"],control.fileno()):poller.register(number,select.POLLIN|select.POLLHUP|select.POLLERR)
 register_lifecycle_poller(context,poller,b"outer_pidfd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL);register_lifecycle_poller(context,poller,b"actor_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 while True:
  checkpoint(CERT,horizon_needed(context[b"origin"]+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),deadline)
  now=time.monotonic_ns()
  try:events=poller.poll(10)
  except InterruptedError:events=[]
  cmask=0;amask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   if number==4:amask|=event
  if cmask&select.POLLIN:
   try:
    raw,fds=recv_monitored(control,context,4,min(deadline,time.monotonic_ns()+ACK_NS),0,b"MONITOR_PROBE",str(ordinal).encode(),probe)
    faults.add(b"CONTROL_MALFORMED")
   except RemoteAbort as error:faults.update(error.faults)
   except PidfdActorLost:mark_actor_pidfd_lost(context);actor_lost=True;faults.add(b"PIDFD_ACTOR_LOST")
   except FaultSet as error:faults.update(error.faults)
  elif cmask&(select.POLLHUP|select.POLLERR):
   context[b"control_state"]=b"CONTROL_LOST";faults.add(b"CONTROL_LOST")
  if pidfd_ready_event(amask):
   actor_lost=True;mark_actor_pidfd_lost(context);faults.add(b"PIDFD_ACTOR_LOST")
  for number,event in events:
   if number==context[b"out_fd"]:
    try:
     overflow,eof=drain(number,stdout);out_over|=overflow;out_eof|=eof
    except FaultSet as error:faults.update(error.faults)
   elif number==context[b"err_fd"]:
    try:
     overflow,eof=drain(number,stderr);err_over|=overflow;err_eof|=eof
    except FaultSet as error:faults.update(error.faults)
   elif number==context[b"outer_pidfd"] and pidfd_ready_event(event):mark_outer_pidfd_ready(context)
  if not out_eof:
   try:
    overflow,eof=drain(context[b"out_fd"],stdout);out_over|=overflow;out_eof|=eof
   except FaultSet as error:faults.update(error.faults)
  if not err_eof:
   try:
    overflow,eof=drain(context[b"err_fd"],stderr);err_over|=overflow;err_eof|=eof
   except FaultSet as error:faults.update(error.faults)
  if out_over or err_over:faults.add(b"CAPTURE_OVERFLOW")
  if stderr:faults.add(b"STDERR_NONEMPTY")
  empty_state=observe_population(context)
  if empty_state is None:faults.add(b"CONTAINMENT_OBSERVATION_UNKNOWN")
  if not faults and now>deadline:faults.add(b"WATCHDOG_DEADLINE")
  if faults:
   context[b"faults"].update(faults);begin_cleanup(context)
   deadline=min(deadline,context[b"cleanup_effect_deadline"])
   if empty_state is True and context[b"kill_authority_consumed"] and not context[b"kill_call_attempted"] and now<context[b"cleanup_deadline"]:kill_once(context,primary(context[b"faults"]))
  if not faults and out_eof and err_eof and empty_state is False and context[b"pidfd_bound"] and context[b"pidfd_exit_ready_observed"]:break
  if faults and context[b"cleanup_deadline"] is not None and now>=context[b"cleanup_deadline"]:break
  if actor_lost and context[b"cleanup_deadline"] is not None and now>=context[b"cleanup_deadline"]:break
 if not context[b"faults"]:checkpoint(CERT,horizon_needed(context[b"origin"]+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),deadline)
 done=time.monotonic_ns();empty_state=observe_population(context);empty=empty_state is False
 context[b"last_out_eof"]=out_eof;context[b"last_err_eof"]=err_eof
 result_complete=False
 if not actor_lost and context[b"control_state"]==b"CONNECTED" and time.monotonic_ns()<=context[b"origin"]+HOST_NS:
  try:
   send_result(control,ordinal,probe,context[b"outer_pid"],context,bytes(stdout),bytes(stderr),out_eof,err_eof,out_over,err_over,empty,set(context[b"faults"]),done)
   set_actor_receive(context,b"WAIT_VALIDATED",str(ordinal).encode(),probe,context[b"origin"]+TOTAL_NS);result_complete=True
  except PidfdActorLost:mark_actor_pidfd_lost(context);actor_lost=True
  except ControlLost:mark_control_lost(context)
  except FaultSet as error:context[b"faults"].update(error.faults);context[b"actor_receive_state"]=b"UNKNOWN_SEND_EFFECT"
  except SendEffectUnknown:context[b"faults"].add(b"SEND_EFFECT_UNKNOWN");context[b"actor_receive_state"]=b"UNKNOWN_SEND_EFFECT"
 return actor_lost,set(context[b"faults"]),empty,bytes(stdout),bytes(stderr),result_complete

def close_probe(context):
 number=context.get(b"outer_pidfd",-1)
 if number>=0 and context.get(b"offer_snapshot_outer_fd")==number:
  context[b"offer_snapshot_poller"].unregister(number);context[b"offer_snapshot_outer_fd"]=-1
 context[b"last_outer_pidfd_causal_facts"]=(context.get(b"outer_pidfd_provenance"),context.get(b"pidfd_exit_ready_observed"),context.get(b"outer_release_record_identity"),context.get(b"outer_pid"),context.get(b"outer_starttime"))
 close_lifecycle_slots(context,(b"out_fd",b"err_fd",b"events_fd",b"outer_pidfd"))
 unique_kill_authority(context,bool(context.get(b"containment_bound")))
 context[b"pidfd_bound"]=False;context[b"outer_pidfd_close_state"]=b"CLOSED_NORMAL";context[b"outer_pidfd_offer_state"]=b"NOT_BOUND";context[b"outer_offer_binding"]=None

def request_release_disable(control,context,stop):
 if context[b"release_disabled"] or context[b"actor_lost"]:return
 actual_state=context[b"actor_receive_state"];actual_ordinal=context[b"actor_receive_ordinal"];actual_probe=context[b"actor_receive_probe"]
 if actual_state in (b"NONE",b"UNKNOWN_SEND_EFFECT"):
  context[b"faults"].add(b"RECONCILIATION_UNKNOWN");return
 need(actual_probe==stop or stop==b"NONE")
 deadline=min(context[b"failure_origin"]+ACTOR_DISABLE_NS,context[b"actor_receive_deadline"])
 if time.monotonic_ns()>deadline:context[b"faults"].add(b"DEADLINE_EXPIRED");return
 notice=packet(b"V15_ABORT",((b"sender",b"B"),(b"state",b"ABORTING"),(b"expected_state",actual_state),(b"ordinal",actual_ordinal),(b"probe",actual_probe),(b"effect_state",b"ABORT_NOTICE"),(b"causal_state",b"CLEANUP_RELEASE_DISABLE"),(b"causal_effect",b"CONSUMED"),(b"stage_present",b"1" if context[b"stage_present"] else b"0"),(b"release_disabled",b"0"),(b"terminal_deadline_ns",str(context[b"cleanup_effect_deadline"]).encode()),(b"fault_set",fault_csv(context[b"faults"])),(b"control_deadline_ns",str(deadline).encode())))
 try:
  send_exact(control,notice,deadline)
  raw,fds=recv_monitored(control,context,4,deadline,0,b"WAIT_RELEASE_DISABLE_ACK",actual_ordinal,actual_probe);need(fds==())
  context[b"faults"].add(b"CONTROL_MALFORMED")
 except RemoteAbort as error:
  values=error.values;context[b"faults"].update(error.faults);need(values[b"release_disabled"]==b"1");context[b"release_disabled"]=True
 except PidfdActorLost:mark_actor_pidfd_lost(context)
 except ControlLost:mark_control_lost(context)
 except FaultSet as error:context[b"faults"].update(error.faults)
 except BaseException:context[b"faults"].add(b"CONTROL_MALFORMED")
 if not context[b"release_disabled"]:
  context[b"faults"].add(b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED")

def pass_locked(context):
 return context[b"pass_effect_possible"] or context[b"pass_committed"]

def terminal_safe(context):
 state=observe_population(context);context[b"last_population"]=state
 if context[b"containment_bound"]:return state is False
 return not context[b"payload_release_possible"] and context[b"stopped_count"]==0

def finish_actor_loss_chain(context,mode,schedule):
 need(context[b"actor_state"]==b"PIDFD_ACTOR_LOST" and context[b"outcome_durable"] and terminal_safe(context))
 ack_receipt_record(context,mode,b"",schedule,True);reconciliation_record(context,mode,schedule);owner_closure_record(context,mode,schedule)
 release_deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"B_EXIT",context[b"terminal_deadline"],False)
 close_ownership_capabilities(context,release_deadline);need(ownership_capabilities_closed(context))
 complete_started_ownership_close(context);context[b"terminal_phase"]=b"ACTOR_LOSS_DURABLE_NO_REPLAY_CAPABILITIES_CLOSED_OWNER_CLOSED"

def transfer_or_hold(control,context,reason,record_fault=True):
 if context[b"ownership_close_started"]:
  try:complete_started_ownership_close(context)
  except OwnershipClosePending:context[b"terminal_phase"]=b"OWNERSHIP_CLOSE_CURSOR_RETRYABLE_RETAINED"
  return
 context[b"terminal_phase"]=b"FROZEN_EXTERNAL_TRANSFER"
 if record_fault:context[b"faults"].add(reason)
 driver_reason=reason if reason in FAULT_ORDER else b"RECONCILIATION_UNKNOWN"
 while not context[b"owner_released"]:
  try:external_transfer(control,context,driver_reason)
  except RefusalFinalityPending:
   owner_poll(control,context,time.monotonic_ns()+50000000);continue
  except BaseException as error:
   locked=context.get(b"refusal_slot_locked",False)
   if locked:note_locked_refusal_error(context,error,True)
   owner_poll(control,context,time.monotonic_ns()+50000000)
   if not locked and context[b"actor_state"]==b"PIDFD_ACTOR_LOST" and context[b"outcome_durable"] and terminal_safe(context) and context.get(b"terminal_schedule") is not None:
    try:finish_actor_loss_chain(context,context[b"terminal_mode"],context[b"terminal_schedule"]);return
    except BaseException:pass
 return

def terminal_owner_loop(control,context,mode,kind,subject,disp,deadline):
 need(mode in (b"SUCCESS",b"FAILURE") and deadline==context[b"terminal_deadline"]);schedule=context[b"terminal_schedule"]
 need(schedule==exact_schedule(context[b"terminal_origin"],deadline,TERMINAL_PHASE_SPEC))
 context[b"terminal_mode"]=mode;context[b"terminal_kind"]=kind;context[b"terminal_subject"]=subject
 notice_deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"NOTICE",deadline,mode==b"SUCCESS")
 common=((b"state",b"TERMINAL_CANDIDATE_DURABLE" if mode==b"SUCCESS" else b"TERMINAL_FAILURE_DURABLE"),(b"expected_state",b"WAIT_TERMINAL_CANDIDATE" if mode==b"SUCCESS" else b"WAIT_TERMINAL_FAILURE"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",kind),(b"subject_sha256",subject),(b"chain_head_sha256",context[b"chain_sha"]),(b"terminal_origin_ns",str(context[b"terminal_origin"]).encode()),(b"terminal_deadline_ns",str(deadline).encode()),(b"terminal_schedule_hex",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"candidate_deadline_ns",str(notice_deadline).encode()))
 if mode==b"SUCCESS":notice=packet(b"V15_TERMINAL_CANDIDATE_DURABLE",common)
 else:notice=packet(b"V15_TERMINAL_FAILURE_DURABLE",common+((b"disposition",disp),))
 context[b"terminal_notice_raw"]=notice;context[b"terminal_phase"]=b"NOTICE_SEND_EFFECT_UNKNOWN";context[b"send_state"]=b"NOTICE_SEND_EFFECT_UNKNOWN"
 try:send_exact(control,notice,notice_deadline);context[b"terminal_phase"]=b"WAIT_TERMINAL_SEEN";context[b"send_state"]=b"NOTICE_SENT"
 except SendEffectUnknown:context[b"send_state"]=b"NOTICE_SEND_EFFECT_UNKNOWN";context[b"terminal_phase"]=b"WAIT_TERMINAL_SEEN"
 while not context[b"owner_released"]:
  now=time.monotonic_ns()
  if context[b"actor_state"]==b"PIDFD_ACTOR_LOST":
   if context[b"outcome_durable"] and context[b"terminal_seen_sha"]!=b"0"*64 and terminal_safe(context):
    try:finish_actor_loss_chain(context,mode,schedule);return
    except BaseException:transfer_or_hold(control,context,b"RECONCILIATION_UNKNOWN");return
   transfer_or_hold(control,context,b"PIDFD_ACTOR_LOST");return
  if now>deadline:
   transfer_or_hold(control,context,b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED");return
  phase=context[b"terminal_phase"]
  phase_deadline=schedule[b"TERMINAL_SEEN_RECORD"] if phase==b"WAIT_TERMINAL_SEEN" else (schedule[b"A_RECEIPT"] if phase==b"WAIT_ACK_RECEIPT" else deadline)
  try:
   raw,fds=recv_monitored(control,context,4,phase_deadline,0,phase,b"NONE",b"NONE");need(fds==())
  except PidfdActorLost:
   mark_actor_pidfd_lost(context);continue
  except ControlLost:
   mark_control_lost(context);transfer_or_hold(control,context,b"CONTROL_LOST");return
  except SendEffectUnknown:
   context[b"send_state"]=b"SEND_EFFECT_UNKNOWN";continue
  except RemoteAbort as error:
   context[b"faults"].update(error.faults)
   if pass_locked(context):context[b"faults"].add(b"ACK_EFFECT_UNKNOWN")
   transfer_or_hold(control,context,b"RECONCILIATION_UNKNOWN");return
  except FaultSet as error:
   context[b"faults"].update(error.faults);transfer_or_hold(control,context,b"RECONCILIATION_UNKNOWN");return
  if phase==b"WAIT_TERMINAL_SEEN":
   values=parse_packet(raw,b"V15_TERMINAL_SEEN",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"notice_packet_sha256",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"seen_deadline_ns"),receiver_binding(b"WAIT_TERMINAL_SEEN",b"NONE",b"NONE",phase_deadline))
   need(values[b"state"]==b"TERMINAL_SEEN" and values[b"expected_state"]==b"WAIT_TERMINAL_SEEN" and values[b"effect_state"]==b"TERMINAL_SEEN")
   need(values[b"ordinal"]==values[b"probe"]==b"NONE" and values[b"kind"]==kind and values[b"subject_sha256"]==subject and values[b"notice_packet_sha256"]==sha(notice))
   need(udec(values[b"terminal_origin_ns"])==context[b"terminal_origin"] and udec(values[b"terminal_deadline_ns"])==deadline and values[b"terminal_schedule_hex"]==schedule_hex(schedule,TERMINAL_PHASE_SPEC))
   terminal_seen_record(context,mode,subject,notice,raw,schedule)
   if mode==b"SUCCESS":report_sha,pass_sha,token=success_report_and_pass(context,schedule);ack_state=b"PASS_COMMITTED_NO_DOWNGRADE"
   else:report_sha=failure_report(context,context[b"stop_probe"],schedule);pass_sha=b"NONE";token=b"NONE";context[b"outcome_durable"]=True;ack_state=b"FAILURE_DURABLE"
   ack_deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"ACK",deadline,False)
   ack=packet(b"V15_TERMINAL_ACK",((b"state",b"TERMINAL_ACK"),(b"expected_state",b"WAIT_TERMINAL_ACK"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",kind),(b"subject_sha256",subject),(b"terminal_seen_sha256",context[b"terminal_seen_sha"]),(b"report_sha256",report_sha),(b"pass_sha256",pass_sha),(b"reconciliation_token",token),(b"ack_state",ack_state),(b"terminal_origin_ns",str(context[b"terminal_origin"]).encode()),(b"terminal_deadline_ns",str(deadline).encode()),(b"terminal_schedule_hex",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"ack_deadline_ns",str(ack_deadline).encode())))
   context[b"terminal_ack_raw"]=ack;context[b"ack_state"]=b"ACK_SEND_EFFECT_UNKNOWN";context[b"send_state"]=b"ACK_SEND_EFFECT_UNKNOWN";context[b"terminal_phase"]=b"ACK_SEND_EFFECT_UNKNOWN"
   try:send_exact(control,ack,ack_deadline);context[b"ack_state"]=b"ACK_SENT";context[b"send_state"]=b"ACK_SENT"
   except SendEffectUnknown:context[b"ack_effect_unknown"]=True;context[b"faults"].add(b"ACK_EFFECT_UNKNOWN");context[b"send_state"]=b"ACK_SEND_EFFECT_UNKNOWN"
   context[b"terminal_phase"]=b"WAIT_ACK_RECEIPT"
  elif phase==b"WAIT_ACK_RECEIPT":
   values=parse_packet(raw,b"V15_TERMINAL_ACK_RECEIPT",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"ack_packet_sha256",b"report_sha256",b"pass_sha256",b"reconciliation_token",b"actor_receipt_ns",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"receipt_deadline_ns"),receiver_binding(b"WAIT_ACK_RECEIPT",b"NONE",b"NONE",phase_deadline))
   need(values[b"state"]==b"ACK_RECEIVED_NO_REPLAY" and values[b"expected_state"]==b"WAIT_ACK_RECEIPT" and values[b"effect_state"]==b"NO_REPLAY_RECEIPT")
   need(values[b"ordinal"]==values[b"probe"]==b"NONE" and values[b"kind"]==kind and values[b"subject_sha256"]==subject and values[b"ack_packet_sha256"]==sha(context[b"terminal_ack_raw"]))
   need(values[b"report_sha256"]==context[b"report_sha"] and values[b"pass_sha256"]==context.get(b"pass_sha",b"NONE") and values[b"reconciliation_token"]==context.get(b"reconciliation_token",b"NONE"))
   need(udec(values[b"actor_receipt_ns"],1)<=time.monotonic_ns() and udec(values[b"terminal_origin_ns"])==context[b"terminal_origin"] and udec(values[b"terminal_deadline_ns"])==deadline)
   need(values[b"terminal_schedule_hex"]==schedule_hex(schedule,TERMINAL_PHASE_SPEC))
   ack_receipt_record(context,mode,raw,schedule,False);reconciliation_record(context,mode,schedule);closure_sha=owner_closure_record(context,mode,schedule)
   closure_deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"CLOSURE_PACKET",deadline,False)
   closed_packet=packet(b"V15_TERMINAL_CLOSED",((b"state",b"OWNER_CLOSED"),(b"expected_state",b"WAIT_OWNER_CLOSED"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",kind),(b"subject_sha256",subject),(b"report_sha256",context[b"report_sha"]),(b"pass_sha256",context.get(b"pass_sha",b"NONE")),(b"ack_receipt_sha256",context[b"ack_receipt_sha"]),(b"reconciliation_sha256",context[b"reconciliation_sha"]),(b"closure_sha256",closure_sha),(b"owner",b"B"),(b"terminal_origin_ns",str(context[b"terminal_origin"]).encode()),(b"terminal_deadline_ns",str(deadline).encode()),(b"terminal_schedule_hex",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"closure_deadline_ns",str(closure_deadline).encode())))
   context[b"terminal_phase"]=b"OWNER_CLOSE_SEND_EFFECT_UNKNOWN";context[b"send_state"]=b"OWNER_CLOSE_SEND_EFFECT_UNKNOWN"
   try:
    send_exact(control,closed_packet,closure_deadline);context[b"terminal_phase"]=b"OWNER_CLOSED";context[b"send_state"]=b"OWNER_CLOSED_SENT"
    exit_deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"B_EXIT",deadline,False);need(time.monotonic_ns()<=exit_deadline and terminal_safe(context))
    close_ownership_capabilities(context,exit_deadline);need(ownership_capabilities_closed(context));complete_started_ownership_close(context);return
   except SendEffectUnknown:
    context[b"send_state"]=b"OWNER_CLOSE_SEND_EFFECT_UNKNOWN";transfer_or_hold(control,context,b"SEND_EFFECT_UNKNOWN");return
  else:
   context[b"faults"].add(b"CONTROL_MALFORMED");transfer_or_hold(control,context,b"CONTROL_MALFORMED");return

def terminal_failure(control,context,stop,faults,actor_lost):
 need(not pass_locked(context));context[b"faults"].update(faults);context[b"stop_probe"]=stop
 if actor_lost:mark_actor_pidfd_lost(context)
 if not context[b"faults"]:context[b"faults"].add(b"INTERNAL_INVARIANT")
 freeze_failure_deadlines(context)
 if context.get(b"record_sequence_frozen"):
  try:resolved=resolve_pending_before_successor(context,context[b"cleanup_effect_deadline"])
  except (FaultSet,CertificateExpired):resolved=False
  if not resolved:
   context[b"faults"].add(b"RECONCILIATION_UNKNOWN");transfer_or_hold(control,context,b"RECONCILIATION_UNKNOWN");return disposition(context[b"faults"])
 if context.get(b"attempt_base_fd",-1)>=0 and (context.get(b"attempt",-1)>=0 or context[b"collision"]):
  try:close_lifecycle_fd(context,b"attempt_base_fd")
  except OwnershipClosePending:context[b"faults"].add(b"ATTEMPT_DIRFD_UNKNOWN")
  else:
   if context[b"collision"]:context[b"attempt_base_closed_on_collision"]=True;context[b"attempt_state"]=b"COLLISION_CLOSED"
 begin_cleanup(context)
 if context[b"payload_release_possible"]:kill_once(context,primary(context[b"faults"]))
 if context[b"payload_release_possible"] and context[b"control_state"]!=b"CONTROL_LOST":
  try:request_release_disable(control,context,stop)
  except PidfdActorLost:mark_actor_pidfd_lost(context)
  except ControlLost:mark_control_lost(context)
  except FaultSet as error:context[b"faults"].update(error.faults)
 begin_cleanup(context);recover_stage_presence(context,context[b"cleanup_effect_deadline"])
 if context[b"collision"]:
  mutation_state=b"COLLISION_CLOSED" if context[b"attempt_base_fd"]<0 and context[b"attempt_base_closed_on_collision"] else b"COLLISION_BASE_HELD_FOR_EXACT_TRANSFER"
  context[b"attempt_state"]=mutation_state
  context[b"collision_transfer_claim_sha"]=sha(b"P27E001_COLLISION_V15\x00"+AUTH+b"\x00"+fault_csv(context[b"faults"])+b"\x00"+str(context[b"failure_origin"]).encode()+b"\x00"+mutation_state+b"\x00"+(b"1" if context[b"attempt_base_fd"]<0 else b"0"))
  transfer_or_hold(control,context,b"ATTEMPT_COLLISION");return disposition(context[b"faults"])
 if context[b"attempt"]<0:
  context[b"faults"].add(b"ATTEMPT_DIRFD_UNKNOWN");transfer_or_hold(control,context,b"ATTEMPT_DIRFD_UNKNOWN");return disposition(context[b"faults"])
 while time.monotonic_ns()<=context[b"cleanup_effect_deadline"]:
  owner_poll(control,context,context[b"cleanup_effect_deadline"]);state=observe_population(context);context[b"last_population"]=state
  if not context[b"payload_release_possible"] or state is False:break
 if context[b"payload_release_possible"] and context[b"last_population"] is not False:
  if not retained_until_empty(control,context,stop):
   context[b"faults"].add(b"CONTAINMENT_NOT_EMPTY");transfer_or_hold(control,context,b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED");return disposition(context[b"faults"])
 state,digest=recovery_record(context,stop)
 if state!=DURABLE_VERIFIED:
  transfer_or_hold(control,context,b"RECOVERY_DURABILITY_UNKNOWN");return disposition(context[b"faults"])
 context[b"terminal_schedule"]=exact_schedule(context[b"terminal_origin"],context[b"terminal_deadline"],TERMINAL_PHASE_SPEC)
 subject=terminal_candidate_record(context,b"FAILURE",stop,context[b"terminal_schedule"])
 terminal_owner_loop(control,context,b"FAILURE",b"FAILURE_CANDIDATE",subject,disposition(context[b"faults"]),context[b"terminal_deadline"]);return disposition(context[b"faults"])

def validated_exchange(control,context,ordinal,probe,stdout,stderr,expected_faults):
 raw,fds=recv_monitored(control,context,4,context[b"origin"]+TOTAL_NS,0,b"WAIT_VALIDATED",str(ordinal).encode(),probe);need(fds==())
 candidate_binding=received_binding(raw,b"WAIT_VALIDATED",str(ordinal).encode(),probe,b"ack_deadline_ns",context[b"origin"]+TOTAL_NS)
 values=parse_packet(raw,b"V15_VALIDATED_CANDIDATE",CANDIDATE_KEYS,candidate_binding)
 set_actor_receive(context,b"WAIT_VALIDATED_DURABLE",str(ordinal).encode(),probe,candidate_binding[3])
 if expected_faults:raise FaultSet({b"CONTROL_MALFORMED"})
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe)
 need(values[b"release_record_sha256"]==context[b"release_sha"] and udec(values[b"release_origin_ns"])==context[b"origin"])
 release_return=udec(values[b"release_return_ns"]);host_complete=udec(values[b"host_complete_ns"]);capture_done=udec(values[b"capture_done_ns"])
 need(context[b"origin"]<release_return<=context[b"launch"] and capture_done<=host_complete<=context[b"origin"]+HOST_NS)
 need(values[b"direct_wait_state"]==b"COMPLETE" and values[b"outer_raw_status"]==b"0")
 need(values[b"pidfd_bound"]==values[b"pidfd_exit_ready_observed"]==b"1")
 need(udec(values[b"stdout_len"])==len(stdout) and values[b"stdout_sha256"]==sha(stdout) and values[b"stdout_eof"]==b"1" and values[b"stdout_overflow"]==b"0")
 need(udec(values[b"stderr_len"])==len(stderr)==0 and values[b"stderr_sha256"]==sha(stderr) and values[b"stderr_eof"]==b"1" and values[b"stderr_overflow"]==b"0")
 need(values[b"cgroup_empty"]==b"1" and values[b"parser_language"]==values[b"parser_structure"]==values[b"parser_semantics"]==values[b"candidate"]==values[b"terminal"]==b"ACCEPTED")
 need(values[b"certificate_expiry_realtime_ns"]==CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 h64(values[b"stdout_sha256"]);h64(values[b"stderr_sha256"])
 ack_deadline=min(context[b"origin"]+TOTAL_NS,host_complete+ACK_NS);need(ack_deadline==candidate_binding[3] and time.monotonic_ns()+4*RECORD_NS<=ack_deadline)
 checkpoint(CERT,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ack_deadline);validated_sha=validated_record(context,values,ack_deadline)
 reply=packet(b"V15_VALIDATED_DURABLE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"validated_sha256",validated_sha),(b"ack_deadline_ns",str(ack_deadline).encode())))
 send_exact(control,reply,ack_deadline)
 raw,fds=recv_monitored(control,context,4,ack_deadline,0,b"WAIT_ACK_INTENT",str(ordinal).encode(),probe);need(fds==())
 intent=parse_packet(raw,b"V15_ACK_COMMIT_INTENT",(b"ordinal",b"probe",b"validated_sha256",b"host_complete_ns",b"ack_deadline_ns",b"actor_ack_intent_ns"),receiver_binding(b"WAIT_ACK_INTENT",str(ordinal).encode(),probe,ack_deadline))
 set_actor_receive(context,b"WAIT_COMMITTED",str(ordinal).encode(),probe,ack_deadline)
 need(udec(intent[b"ordinal"],0,14)==ordinal and intent[b"probe"]==probe and intent[b"validated_sha256"]==validated_sha)
 actor_ack=udec(intent[b"actor_ack_intent_ns"]);received=time.monotonic_ns();ack_deadline=udec(intent[b"ack_deadline_ns"],1)
 need(udec(intent[b"host_complete_ns"])==host_complete and ack_deadline==min(context[b"origin"]+TOTAL_NS,host_complete+ACK_NS))
 need(host_complete<=actor_ack<=received<=ack_deadline and actor_ack-host_complete<=ACK_NS)
 checkpoint(CERT,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ack_deadline)
 ack_sha=ack_intent_record(context,ordinal,probe,actor_ack,received,ack_deadline)
 checkpoint(CERT,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ack_deadline)
 final_count=sum(context[b"committed"])+1;commit_record_seq=context[b"record_seq"]+1
 committed,reserved_control_seq=reserve_packet(b"V15_COMMITTED",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"ack_sha256",ack_sha),(b"commit_record_seq",str(commit_record_seq).encode()),(b"committed_count",str(final_count).encode()),(b"ack_deadline_ns",str(ack_deadline).encode())))
 commit_sha=committed_record(context,ordinal,probe,ack_sha,committed,reserved_control_seq,final_count,ack_deadline)
 activate_reserved_packet(committed,reserved_control_seq)
 need(context[b"committed"][ordinal] and context[b"direct_reaps"]==final_count and context[b"direct_reap_state"]==b"COMPLETE")
 need(context[b"last_committed_record_sha"]==commit_sha and context[b"last_committed_packet_sha"]==sha(committed) and context[b"last_committed_packet_message_seq"]==reserved_control_seq)
 need(context[b"committed_send_state"]==b"COMMITTED_SEND_EFFECT_UNKNOWN" and context.get(b"committed_seen_sha",b"0"*64)!=commit_sha)
 send_exact(control,committed,ack_deadline);context[b"committed_send_state"]=b"COMMITTED_SENT"
 raw,fds=recv_monitored(control,context,4,ack_deadline,0,b"WAIT_COMMITTED_SEEN",str(ordinal).encode(),probe);need(fds==())
 seen=parse_packet(raw,b"V15_COMMITTED_SEEN",(b"ordinal",b"probe",b"ack_sha256",b"committed_packet_sha256",b"committed_count",b"host_complete_ns",b"ack_deadline_ns"),receiver_binding(b"WAIT_COMMITTED_SEEN",str(ordinal).encode(),probe,ack_deadline))
 need(udec(seen[b"ordinal"],0,14)==ordinal and seen[b"probe"]==probe and seen[b"ack_sha256"]==ack_sha)
 need(seen[b"committed_packet_sha256"]==sha(committed) and udec(seen[b"committed_count"],1,15)==final_count)
 need(udec(seen[b"host_complete_ns"])==host_complete and udec(seen[b"ack_deadline_ns"])==ack_deadline and time.monotonic_ns()-host_complete<=ACK_NS)
 committed_seen_record(context,ordinal,probe,raw,committed,commit_sha,ack_sha,final_count,host_complete,ack_deadline);context[b"actor_known_chain_sha"]=ack_sha
 checkpoint(CERT,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ack_deadline);return ack_sha

def recover_stage_presence(context,deadline):
 if context[b"stage_present"] and context[b"stage_state"]==b"VERIFIED_PRESENT":return
 base=number=leaf=-1;verified_identity=None;verified=False
 try:
  record_boundary(context,deadline,False,FAILURE_TAIL_NS)
  base=acquire_lifecycle_open(context,b"recovery_stage_base_fd",b"STAGE_RECOVERY_BASE_DIRFD",b".",O_DIR);base_check(base,CERT,b"SAFE_BIND");base_mid,base_line=mount_binding(base)
  record_boundary(context,deadline,False,FAILURE_TAIL_NS)
  need(base_mid==udec(CERT[b"SAFE_BIND_MOUNT_ID"],1) and sha(base_line)==CERT[b"SAFE_BIND_MOUNTINFO_SHA256"])
  named=os.stat(AUTH,dir_fd=base,follow_symlinks=False);number=acquire_lifecycle_open(context,b"recovery_stage_received",b"STAGE_DIRFD",AUTH,O_DIR,dir_fd=base,transferable=True);held=os.fstat(number)
  identity=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)
  need(identity==(named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid))
  need(stat.S_ISDIR(held.st_mode) and stat.S_IMODE(held.st_mode)==0o700 and held.st_uid==held.st_gid==0 and held.st_nlink==2)
  fd_access(number,os.O_RDONLY);record_boundary(context,deadline,False,FAILURE_TAIL_NS)
  for absent_name in (b"target",b"a",b"b"):
   try:os.stat(absent_name,dir_fd=number,follow_symlinks=False);need(False)
   except FileNotFoundError:pass
  specs=((b"keeper.py",b"KEEPER_BYTES",b"KEEPER_LF",b"KEEPER_SHA256"),(b"launcher.py",b"LAUNCHER_BYTES",b"LAUNCHER_LF",b"LAUNCHER_SHA256"),(b"marker.py",b"MARKER_BYTES",b"MARKER_LF",b"MARKER_SHA256"),(b"child.py",b"CHILD_BYTES",b"CHILD_LF",b"CHILD_SHA256"))
  for name,bkey,lkey,hkey in specs:
   record_boundary(context,deadline,False,FAILURE_TAIL_NS)
   leaf=acquire_lifecycle_open(context,b"recovery_stage_leaf_fd",b"STAGE_LEAF_VERIFY_FD",name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number);body=read_all(leaf,udec(CERT[bkey],1));st=os.fstat(leaf)
   need(stat.S_ISREG(st.st_mode) and (st.st_uid,st.st_gid,stat.S_IMODE(st.st_mode),st.st_nlink)==(0,0,0o400,1))
   need((len(body),body.count(b"\n"),sha(body))==(udec(CERT[bkey],1),udec(CERT[lkey]),CERT[hkey]))
   record_boundary(context,deadline,False,FAILURE_TAIL_NS);close_lifecycle_fd(context,b"recovery_stage_leaf_fd");leaf=-1
  again=os.stat(AUTH,dir_fd=base,follow_symlinks=False);need(identity==(again.st_dev,again.st_ino,again.st_mode,again.st_nlink,again.st_uid,again.st_gid))
  record_boundary(context,deadline,False,FAILURE_TAIL_NS)
  verified_identity=identity;verified=True
 except FileNotFoundError:
  context[b"stage_state"]=b"ABSENT_KNOWN"
 except FaultSet as error:
  context[b"stage_state"]=b"UNKNOWN";context[b"faults"].update(error.faults);context[b"faults"].add(b"STAGING_FAULT")
 except BaseException:
  context[b"stage_state"]=b"UNKNOWN";context[b"faults"].add(b"STAGING_FAULT")
 finally:close_lifecycle_slots(context,(b"recovery_stage_leaf_fd",b"recovery_stage_base_fd"))
 if verified:
  promote_lifecycle_fd(context,b"recovery_stage_received",b"stage_fd",b"STAGE_DIRFD",True);number=-1;context[b"stage_identity"]=verified_identity;context[b"stage_present"]=True;context[b"stage_state"]=b"VERIFIED_PRESENT"
 else:
  close_lifecycle_fd(context,b"recovery_stage_received");context[b"stage_present"]=False

def stage_bind(control,context):
 fds=();number=base=leaf=-1
 keys=(b"state",b"ordinal",b"probe",b"stage_origin_ns",b"stage_deadline_ns",b"stage_return_ns",b"safe_dev",b"safe_ino",b"safe_mode",b"safe_nlink",b"safe_uid",b"safe_gid",b"keeper_sha256",b"launcher_sha256",b"marker_sha256",b"child_sha256")
 try:
  boot=time.monotonic_ns()+STAGE_NS;set_actor_receive(context,b"WAIT_STAGE_ACK",b"NONE",b"NONE",boot)
  raw,fds=recv_monitored(control,context,4,boot,1,b"WAIT_STAGE",b"NONE",b"NONE",((b"stage_received",b"STAGE_DIRFD",True),));need(len(fds)==1)
  number=fds[0];fds=()
  values=parse_packet(raw,b"V15_STAGE_DURABLE",keys,received_binding(raw,b"WAIT_STAGE",b"NONE",b"NONE",b"stage_deadline_ns",boot))
  need(values[b"state"]==b"STAGE_DURABLE" and values[b"ordinal"]==values[b"probe"]==b"NONE")
  origin=udec(values[b"stage_origin_ns"],1);deadline=udec(values[b"stage_deadline_ns"],1)
  need(deadline==origin+STAGE_NS and udec(values[b"stage_return_ns"],origin,deadline)<=time.monotonic_ns()<=deadline)
  checkpoint(CERT,POST_STAGE_REMAIN_NS,deadline);fd_access(number,os.O_RDONLY)
  held=os.fstat(number);supplied=(udec(values[b"safe_dev"],1),udec(values[b"safe_ino"],1),octal(values[b"safe_mode"]),udec(values[b"safe_nlink"],1),udec(values[b"safe_uid"]),udec(values[b"safe_gid"]))
  need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==supplied)
  need(stat.S_ISDIR(held.st_mode) and stat.S_IMODE(held.st_mode)==0o700 and held.st_uid==held.st_gid==0 and held.st_nlink==2)
  base=acquire_lifecycle_open(context,b"stage_base_verify_fd",b"STAGE_BASE_VERIFY_DIRFD",b".",O_DIR);base_check(base,CERT,b"SAFE_BIND")
  named=os.stat(AUTH,dir_fd=base,follow_symlinks=False)
  need((named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid)==(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid))
  specs=((b"keeper.py",b"KEEPER_BYTES",b"KEEPER_LF",b"KEEPER_SHA256",b"keeper_sha256"),(b"launcher.py",b"LAUNCHER_BYTES",b"LAUNCHER_LF",b"LAUNCHER_SHA256",b"launcher_sha256"),(b"marker.py",b"MARKER_BYTES",b"MARKER_LF",b"MARKER_SHA256",b"marker_sha256"),(b"child.py",b"CHILD_BYTES",b"CHILD_LF",b"CHILD_SHA256",b"child_sha256"))
  for name,bkey,lkey,hkey,pkey in specs:
   try:
    leaf=acquire_lifecycle_open(context,b"stage_leaf_verify_fd",b"STAGE_LEAF_VERIFY_FD",name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number);fd_access(leaf,os.O_RDONLY)
    body=read_all(leaf,udec(CERT[bkey],1));st=os.fstat(leaf)
    need(stat.S_ISREG(st.st_mode) and (st.st_uid,st.st_gid,stat.S_IMODE(st.st_mode),st.st_nlink)==(0,0,0o400,1))
    need((len(body),body.count(b"\n"),sha(body))==(udec(CERT[bkey],1),udec(CERT[lkey]),CERT[hkey]))
    need(values[pkey]==CERT[hkey])
   finally:close_lifecycle_fd(context,b"stage_leaf_verify_fd");leaf=-1
  again=os.stat(AUTH,dir_fd=base,follow_symlinks=False);base_check(base,CERT,b"SAFE_BIND");fd_access(number,os.O_RDONLY)
  need((again.st_dev,again.st_ino,again.st_mode,again.st_nlink,again.st_uid,again.st_gid)==(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid))
  checkpoint(CERT,POST_STAGE_REMAIN_NS,deadline)
  promote_lifecycle_fd(context,b"stage_received",b"stage_fd",b"STAGE_DIRFD",True);number=-1;context[b"stage_identity"]=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)
  context[b"stage_present"]=True;context[b"stage_state"]=b"VERIFIED_PRESENT";context[b"stage_deadline"]=deadline
  reply=packet(b"V15_STAGE_ACK",((b"state",b"STAGE_BOUND"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"stage_deadline_ns",str(deadline).encode()),(b"safe_dev",str(held.st_dev).encode()),(b"safe_ino",str(held.st_ino).encode())))
  send_exact(control,reply,deadline);checkpoint(CERT,POST_STAGE_REMAIN_NS,deadline)
 finally:
  close_lifecycle_slots(context,(b"stage_received",b"stage_leaf_verify_fd",b"stage_base_verify_fd"))

def containment_bind(control,context):
 fds=();number=root_events=root_kill=ctype=controllers=subtree=-1
 try:
  boot=time.monotonic_ns()+ACK_NS;set_actor_receive(context,b"WAIT_CONTAINMENT_ACK",b"NONE",b"NONE",boot)
  raw,fds=recv_monitored(control,context,4,boot,1,b"WAIT_CONTAINMENT",b"NONE",b"NONE",((b"containment_received",b"CGROUP_DIRFD",True),));need(len(fds)==1)
  number=fds[0];fds=()
  keys=(b"state",b"ordinal",b"probe",b"contain_origin_ns",b"contain_deadline_ns",b"dev",b"ino",b"mode",b"nlink",b"uid",b"gid",b"base_dev",b"base_ino",b"mount_id",b"mountinfo_sha256",b"type_hex",b"controllers_hex",b"subtree_control_hex")
  values=parse_packet(raw,b"V15_CONTAINMENT",keys,received_binding(raw,b"WAIT_CONTAINMENT",b"NONE",b"NONE",b"contain_deadline_ns",boot))
  need(values[b"state"]==b"CONTAINMENT_CANDIDATE" and values[b"ordinal"]==values[b"probe"]==b"NONE" and context[b"stage_present"])
  origin=udec(values[b"contain_origin_ns"],1);deadline=udec(values[b"contain_deadline_ns"],1);need(deadline==origin+ACK_NS and time.monotonic_ns()<=deadline)
  checkpoint(CERT,POST_CONTAIN_REMAIN_NS,deadline);fd_access(number,os.O_RDONLY)
  held=os.fstat(number);need(stat.S_ISDIR(held.st_mode))
  supplied=(udec(values[b"dev"],1),udec(values[b"ino"],1),octal(values[b"mode"]),udec(values[b"nlink"],1),udec(values[b"uid"]),udec(values[b"gid"]))
  need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==supplied)
  need(values[b"mode"]==CERT[b"CGROUP_CHILD_MODE"] and values[b"uid"]==CERT[b"CGROUP_CHILD_UID"] and values[b"gid"]==CERT[b"CGROUP_CHILD_GID"] and values[b"nlink"]==b"2")
  base_check(6,CERT,b"CGROUP_BASE");base=os.fstat(6)
  need((udec(values[b"base_dev"],1),udec(values[b"base_ino"],1))==(base.st_dev,base.st_ino))
  named=os.stat(AUTH,dir_fd=6,follow_symlinks=False)
  need((named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid)==(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid))
  mid,line=mount_binding(number);need(mid==udec(values[b"mount_id"],1)==udec(CERT[b"CGROUP2_MOUNT_ID"],1))
  need(sha(line)==values[b"mountinfo_sha256"]==CERT[b"CGROUP2_MOUNTINFO_SHA256"] and statfs_magic(number)==int(CERT[b"CGROUP2_FS_MAGIC"],16))
  ctype=acquire_lifecycle_open(context,b"containment_type_fd",b"CGROUP_TYPE_VERIFY_FD",b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  controllers=acquire_lifecycle_open(context,b"containment_controllers_fd",b"CGROUP_CONTROLLERS_VERIFY_FD",b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  subtree=acquire_lifecycle_open(context,b"containment_subtree_fd",b"CGROUP_SUBTREE_VERIFY_FD",b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  root_events=acquire_lifecycle_open(context,b"containment_root_events_received",b"ROOT_EVENTS_FD",b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number,transferable=True)
  root_kill=acquire_lifecycle_open(context,b"containment_root_kill_received",b"ROOT_KILL_FD",b"cgroup.kill",os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number,transferable=True)
  fd_access(ctype,os.O_RDONLY);fd_access(controllers,os.O_RDONLY);fd_access(subtree,os.O_RDONLY);fd_access(root_events,os.O_RDONLY);fd_access(root_kill,os.O_WRONLY)
  type_raw=read_all(ctype,128);controllers_raw=read_all(controllers,4096);subtree_raw=read_all(subtree,4096)
  need(type_raw.hex().encode()==values[b"type_hex"]==CERT[b"CGROUP_CHILD_TYPE_HEX"])
  need(controllers_raw.hex().encode()==values[b"controllers_hex"]==CERT[b"CGROUP_CHILD_CONTROLLERS_HEX"])
  need(subtree_raw.hex().encode()==values[b"subtree_control_hex"]==CERT[b"CGROUP_CHILD_SUBTREE_CONTROL_HEX"])
  need(not populated(root_events));checkpoint(CERT,POST_CONTAIN_REMAIN_NS,deadline)
  promote_lifecycle_fd(context,b"containment_received",b"cgfd",b"CGROUP_DIRFD",True);number=-1;promote_lifecycle_fd(context,b"containment_root_events_received",b"root_events_fd",b"ROOT_EVENTS_FD",True);root_events=-1
  promote_lifecycle_fd(context,b"containment_root_kill_received",b"root_kill_fd",b"ROOT_KILL_FD",True);root_kill=-1;context[b"containment_bound"]=True;context[b"contain_deadline"]=deadline;unique_kill_authority(context,True)
  context[b"cgroup_identity"]=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)
  reply=packet(b"V15_CONTAINMENT_ACK",((b"state",b"CONTAINMENT_BOUND"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"contain_deadline_ns",str(deadline).encode()),(b"dev",str(held.st_dev).encode()),(b"ino",str(held.st_ino).encode())))
  send_exact(control,reply,deadline);checkpoint(CERT,POST_CONTAIN_REMAIN_NS,deadline)
 finally:
  close_lifecycle_slots(context,(b"containment_received",b"containment_root_events_received",b"containment_root_kill_received",b"containment_type_fd",b"containment_controllers_fd",b"containment_subtree_fd"))

def acquire_control(context,actor_pid):
 control=socket.socket(fileno=context[b"actor_control_fd"]);bind_lifecycle_endpoint(context,b"actor_control_fd",b"actor_control",control)
 try:
  need(control.getsockopt(socket.SOL_SOCKET,socket.SO_TYPE)==socket.SOCK_SEQPACKET);fd_access(context[b"actor_control_fd"],os.O_RDWR)
  need(fcntl.fcntl(context[b"actor_control_fd"],fcntl.F_GETFL)&os.O_NONBLOCK)
  peer=struct.unpack("3i",control.getsockopt(socket.SOL_SOCKET,socket.SO_PEERCRED,12));need(peer==(actor_pid,0,0))
  return control
 except BaseException:
  close_lifecycle_fd(context,b"actor_control_fd");raise

EXTERNAL_MANIFEST_KEYS=(b"VERSION",b"SESSION_AUTH_POLICY",b"OWNER_PID",b"OWNER_STARTTIME",b"OWNER_UID",b"OWNER_GID",b"ENDPOINT_TYPE",b"PIDFD_REQUIRED",b"MAX_PACKET_BYTES",b"RIGHTS_TYPES",b"REFUSAL_RECEIPT_PROTOCOL",b"TRANSFER_PROTOCOL",b"NO_REPLAY")
EXTERNAL_RIGHTS_TYPES=b"ATTEMPT_DIRFD,ATTEMPT_BASE_DIRFD,STAGE_DIRFD,CGROUP_DIRFD,ROOT_EVENTS_FD,ROOT_KILL_FD,OUT_FD,ERR_FD,EVENTS_FD,OUTER_PIDFD,CGROUP_BASE_DIRFD,ACTOR_CONTROL_FD,PENDING_EXPECTED_RAW_FD"

def parse_external_manifest(raw,cert):
 values=parse_fixed(raw,b"P27E001_EXTERNAL_OWNER_MANIFEST_V15",EXTERNAL_MANIFEST_KEYS,b"MANIFEST_END=1")
 exact={b"VERSION":b"14",b"SESSION_AUTH_POLICY":b"AUTH_V15_LENGTH_FRAMED",b"OWNER_PID":cert[b"EXTERNAL_OWNER_PID"],b"OWNER_STARTTIME":cert[b"EXTERNAL_OWNER_STARTTIME"],b"OWNER_UID":cert[b"EXTERNAL_OWNER_UID"],b"OWNER_GID":cert[b"EXTERNAL_OWNER_GID"],b"ENDPOINT_TYPE":b"SOCK_SEQPACKET",b"PIDFD_REQUIRED":b"1",b"MAX_PACKET_BYTES":b"65536",b"RIGHTS_TYPES":EXTERNAL_RIGHTS_TYPES,b"REFUSAL_RECEIPT_PROTOCOL":b"MONOTONE_O_EXCL_ISSUER_V15",b"TRANSFER_PROTOCOL":b"OFFER_ACCEPTED_DURABLE_V15",b"NO_REPLAY":b"1"}
 for key,value in exact.items():need(values[key]==value)
 return values

def acquire_external_owner(context):
 pid=udec(CERT[b"EXTERNAL_OWNER_PID"],2);start=udec(CERT[b"EXTERNAL_OWNER_STARTTIME"],1)
 fd_access(context[b"transfer_control_fd"],os.O_RDWR);fd_access(context[b"external_owner_pidfd_fd"],os.O_RDWR);need(pidfd_pid(context[b"external_owner_pidfd_fd"])==pid)
 watcher=select.poll();register_lifecycle_poller(context,watcher,b"external_owner_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL);need(watcher.poll(0)==[])
 external=socket.socket(fileno=context[b"transfer_control_fd"]);bind_lifecycle_endpoint(context,b"transfer_control_fd",b"transfer_control",external)
 try:
  need(external.getsockopt(socket.SOL_SOCKET,socket.SO_TYPE)==socket.SOCK_SEQPACKET and fcntl.fcntl(context[b"transfer_control_fd"],fcntl.F_GETFL)&os.O_NONBLOCK)
  peer=struct.unpack("3i",external.getsockopt(socket.SOL_SOCKET,socket.SO_PEERCRED,12));need(peer==(pid,udec(CERT[b"EXTERNAL_OWNER_UID"]),udec(CERT[b"EXTERNAL_OWNER_GID"])))
  need(proc_starttime(pid)==start and pidfd_pid(context[b"external_owner_pidfd_fd"])==pid and proc_starttime(pid)==start and watcher.poll(0)==[])
  return external
 except BaseException:
  close_lifecycle_fd(context,b"transfer_control_fd");raise

def static_inputs(context):
 global AUTH,CERT,DEPS,RESERVATION_DIGEST,ACTOR_PID,ACTOR_STARTTIME,ISSUER_KEY_ID
 need(type(sys.argv)is list and len(sys.argv)==9 and sys.argv[0]=="/proc/self/fd/100" and sys.argv[1]=="RECOVER_V19")
 supplied=h64(sys.argv[2].encode("ascii"));actor_pid=udec(sys.argv[3].encode("ascii"),2);actor_starttime=udec(sys.argv[4].encode("ascii"),1)
 plan_sha=h64(sys.argv[5].encode("ascii"));source_sha=h64(sys.argv[6].encode("ascii"))
 safe_dev=udec(sys.argv[7].encode("ascii"),1);safe_ino=udec(sys.argv[8].encode("ascii"),1)
 ACTOR_PID=actor_pid;ACTOR_STARTTIME=actor_starttime
 need(os.read(0,1)==b"");fd_access(0,os.O_RDONLY);need(stat.S_ISFIFO(os.fstat(0).st_mode));closed(1);closed(2)
 fd_access(4,os.O_RDWR);need(pidfd_pid(4)==actor_pid and proc_starttime(actor_pid)==actor_starttime)
 actor_watcher=select.poll();register_lifecycle_poller(context,actor_watcher,b"actor_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL);need(actor_watcher.poll(0)==[] and pidfd_pid(4)==actor_pid and proc_starttime(actor_pid)==actor_starttime)
 snapshot_raw=whole_snapshot();cert_raw=sealed_carrier(7,MAX_FILE);envelope_raw=sealed_carrier(8,MAX_FILE);plan_raw=sealed_carrier(10,MAX_FILE);actor_raw=sealed_carrier(11,MAX_FILE);v15_raw=linked_frozen_carrier(12,V15_LINKED_EXPECT,V15_TERMINAL);reservation_raw=sealed_carrier(13,MAX_FILE);transfer_manifest_raw=sealed_carrier(16,MAX_FILE);source_raw=sealed_carrier(100,MAX_FILE)
 CERT,DEPS=contract(cert_raw);issued=envelope(envelope_raw);ISSUER_KEY_ID=issued[b"ISSUER_KEY_ID"];reservation=parse_reservation(reservation_raw)
 context_digest,certificate_digest,receipt_digest=verify_issuer_order(issued,cert_raw,CERT);reservation_digest=verify_reservation_order(reservation,cert_raw,envelope_raw,issued);RESERVATION_DIGEST=reservation_digest
 exact_text(v15_raw,V15_BYTES,V15_LF,V15_SHA,V15_TERMINAL)
 not_before=udec(CERT[b"NOT_BEFORE_REALTIME_NS"]);expiry=udec(CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 need(expiry-not_before==CERT_LIFE_NS and udec(issued[b"NOT_BEFORE_REALTIME_NS"])<=not_before<expiry<=udec(issued[b"NOT_AFTER_REALTIME_NS"]))
 verify_platform(CERT)
 for entry in DEPS:verify_dependency(entry)
 AUTH=session_auth(cert_raw,envelope_raw,reservation_raw);need(AUTH==supplied)
 need(plan_sha==sha(plan_raw)==CERT[b"PLAN_SHA256"]==issued[b"PLAN_SHA256"])
 need(sha(actor_raw)==issued[b"RUNNER_SHA256"]==CERT[b"RUNNER_SHA256"])
 need(source_sha==sha(source_raw)==CERT[b"RECOVERY_SHA256"]==issued[b"RECOVERY_SHA256"])
 need(extract_one(plan_raw,b"P27 RUNNER V20 ACTOR SOURCE BEGIN 6C20A4F1",b"P27 RUNNER V20 ACTOR SOURCE END 6C20A4F1")==actor_raw)
 need(extract_one(plan_raw,b"P27 RUNNER V20 WATCHDOG SOURCE BEGIN 9F20C6A3",b"P27 RUNNER V20 WATCHDOG SOURCE END 9F20C6A3")==source_raw)
 need(issued[b"E0366_SNAPSHOT_SHA256"]==CERT[b"E0366_SNAPSHOT_SHA256"]==sha(snapshot_raw)==SNAPSHOT_EXPECT[2])
 need(issued[b"E0366_SNAPSHOT_BYTES"]==CERT[b"E0366_SNAPSHOT_BYTES"]==b"2303269" and issued[b"E0366_SNAPSHOT_LF"]==CERT[b"E0366_SNAPSHOT_LF"]==b"23672")
 need(issued[b"E0366_SNAPSHOT_TERMINAL_HEX"]==CERT[b"E0366_SNAPSHOT_TERMINAL_HEX"]==SNAPSHOT_TERMINAL_HEX)
 need(issued[b"V15_SHA256"]==CERT[b"V15_SHA256"]==V15_SHA)
 need((len(transfer_manifest_raw),sha(transfer_manifest_raw))==(udec(CERT[b"EXTERNAL_TRANSFER_MANIFEST_BYTES"],1),CERT[b"EXTERNAL_TRANSFER_MANIFEST_SHA256"]));parse_external_manifest(transfer_manifest_raw,CERT)
 need(reservation[b"NOT_BEFORE_REALTIME_NS"]==issued[b"NOT_BEFORE_REALTIME_NS"] and reservation[b"NOT_AFTER_REALTIME_NS"]==issued[b"NOT_AFTER_REALTIME_NS"])
 base_check(5,CERT,b"ATTEMPT_BASE");base_check(6,CERT,b"CGROUP_BASE")
 rootfd=safebase=-1
 try:
  rootfd=acquire_lifecycle_open(context,b"static_runtime_root_fd",b"RUNTIME_ROOT_VERIFY_DIRFD",b"/",O_DIR);safebase=acquire_lifecycle_open(context,b"static_safe_base_fd",b"SAFE_BASE_VERIFY_DIRFD",b".",O_DIR)
  base_check(rootfd,CERT,b"RUNTIME_ROOT");base_check(safebase,CERT,b"SAFE_BIND")
  root_mid,root_line=mount_binding(rootfd);safe_mid,safe_line=mount_binding(safebase)
  need(root_mid==udec(CERT[b"RUNTIME_ROOT_MOUNT_ID"],1) and sha(root_line)==CERT[b"RUNTIME_ROOT_MOUNTINFO_SHA256"])
  need(safe_mid==udec(CERT[b"SAFE_BIND_MOUNT_ID"],1) and sha(safe_line)==CERT[b"SAFE_BIND_MOUNTINFO_SHA256"] and root_mid!=safe_mid)
  mount_semantics(root_line,even_hex(CERT[b"RUNTIME_ROOT_FSTYPE_HEX"]),{b"ro",b"nosuid",b"nodev"},{b"rw"})
  mount_semantics(safe_line,even_hex(CERT[b"SAFE_BIND_FSTYPE_HEX"]),{b"rw",b"nosuid",b"nodev",b"noexec"},{b"ro"})
  mount_graph(CERT)
 finally:close_lifecycle_slots(context,(b"static_runtime_root_fd",b"static_safe_base_fd"))
 attempt_mid,attempt_line=mount_binding(5)
 need(attempt_mid==udec(CERT[b"ATTEMPT_BASE_MOUNT_ID"],1) and sha(attempt_line)==CERT[b"ATTEMPT_BASE_MOUNTINFO_SHA256"])
 mount_semantics(attempt_line,even_hex(CERT[b"ATTEMPT_BASE_FSTYPE_HEX"]),{b"rw",b"nosuid",b"nodev"},{b"ro"})
 cgroup_mid,cgroup_line=mount_binding(6)
 need(statfs_magic(6)==int(CERT[b"CGROUP2_FS_MAGIC"],16) and cgroup_mid==udec(CERT[b"CGROUP2_MOUNT_ID"],1) and sha(cgroup_line)==CERT[b"CGROUP2_MOUNTINFO_SHA256"])
 mount_semantics(cgroup_line,b"cgroup2",{b"rw"},{b"ro"})
 base_type=base_controllers=base_subtree=-1
 try:
  base_type=acquire_lifecycle_open(context,b"static_cgroup_type_fd",b"CGROUP_TYPE_VERIFY_FD",b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=6)
  base_controllers=acquire_lifecycle_open(context,b"static_cgroup_controllers_fd",b"CGROUP_CONTROLLERS_VERIFY_FD",b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=6)
  base_subtree=acquire_lifecycle_open(context,b"static_cgroup_subtree_fd",b"CGROUP_SUBTREE_VERIFY_FD",b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=6)
  need(read_all(base_type,128).hex().encode()==CERT[b"CGROUP_BASE_TYPE_HEX"])
  need(read_all(base_controllers,4096).hex().encode()==CERT[b"CGROUP_BASE_CONTROLLERS_HEX"])
  need(read_all(base_subtree,4096).hex().encode()==CERT[b"CGROUP_BASE_SUBTREE_CONTROL_HEX"])
 finally:close_lifecycle_slots(context,(b"static_cgroup_type_fd",b"static_cgroup_controllers_fd",b"static_cgroup_subtree_fd"))
 need((safe_dev,safe_ino)==(udec(CERT[b"SAFE_BIND_DEV"],1),udec(CERT[b"SAFE_BIND_INO"],1)))
 final_context(safe_dev,safe_ino);scrub_exact({0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,100});checkpoint(CERT,ENTRY_REMAIN_NS)
 control=acquire_control(context,actor_pid)
 try:external=acquire_external_owner(context)
 except BaseException:
  close_lifecycle_fd(context,b"actor_control_fd");raise
 return control,external,cert_raw,envelope_raw,reservation_raw,source_raw

def minimal_context():
 return {
  b"fd_registry":new_lifecycle_registry(),b"fd_close_journal":[],b"fd_journal_complete":True,b"pidfd_poller_records":new_pidfd_poller_records(),b"ownership_closed_monotone":False,b"ownership_close_started":False,b"ownership_close_mode":b"NOT_STARTED",b"ownership_close_plan":(),b"ownership_close_cursor":0,b"ownership_close_complete":False,b"ownership_closure_offer":None,b"offer_snapshot_poller":None,b"offer_snapshot_outer_fd":-1,
  b"attempt":-1,b"attempt_base_fd":5,b"cgroup_base_fd":6,b"local_fd_state":b"ABSENT",b"attempt_base_closed_on_collision":False,b"mkdir_created":False,
  b"consumed":False,b"consumption_state":b"PREARMED",b"consume_origin":0,b"consume_deadline":0,b"arm_effect_possible":False,b"refusal_closed":False,
  b"commit_count":0,b"attempt_state":b"ABSENT_KNOWN",b"intent_count":0,
  b"intent_durable":False,b"collision":False,b"collision_identity":(0,0,0,0,0,0),
  b"faults":set(),b"durability":{},b"durability_digest":{},b"durability_raw":{},b"durability_faults":{},b"record_seq":0,b"record_draft":None,b"record_pending":None,b"record_sequence_frozen":False,b"uncertain_record":None,b"pending_expected_raw_fd":-1,b"carrier_pre_effect_state":b"NO_DRAFT",b"last_applied_record_delta_sha":b"0"*64,b"chain_sha":b"0"*64,b"actor_known_chain_sha":b"0"*64,b"chain_records":[],b"committed":[False]*15,b"entered":0,b"stopped_count":0,b"last_committed_record_sha":b"0"*64,b"last_committed_packet_sha":b"0"*64,b"last_committed_packet_message_seq":0,b"committed_seen_sha":b"0"*64,b"committed_send_state":b"NOT_STARTED",
  b"direct_reaps":0,b"direct_reap_state":b"UNAVAILABLE",
  b"stage_present":False,b"stage_state":b"ABSENT_KNOWN",b"stage_fd":-1,b"stage_identity":None,b"stage_deadline":0,
  b"containment_bound":False,b"contain_deadline":0,b"actor_lost":False,b"release_disabled":False,
  b"kill_call_count":0,b"kill_state":b"NOT_RESERVED",b"kill_ticket_state":b"ABSENT_KNOWN",
  b"failure_origin":None,b"failure_overall_deadline":None,b"cleanup_effect_deadline":None,b"recovery_deadline":None,b"cleanup_origin":None,b"cleanup_deadline":None,b"terminal_schedule":None,
  b"payload_release_possible":False,b"kill_authority_consumed":False,b"kill_call_attempted":False,b"last_population":None,b"last_out_eof":False,b"last_err_eof":False,
  b"cgfd":-1,b"root_events_fd":-1,b"root_kill_fd":-1,b"events_fd":-1,b"out_fd":-1,b"err_fd":-1,
  b"outer_pidfd":-1,b"pidfd_bound":False,b"pidfd_exit_ready_observed":False,b"outer_pid":-1,b"outer_starttime":0,b"outer_pidfd_provenance":None,b"outer_pidfd_close_state":b"NOT_BOUND",b"outer_pidfd_offer_state":b"NOT_BOUND",b"outer_release_record_identity":None,b"outer_offer_binding":None,b"removed":False,
  b"report_state":b"ABSENT_KNOWN",b"report_sha":b"0"*64,b"retained_state":b"ABSENT_KNOWN",
  b"candidate_sha":b"0"*64,b"terminal_seen_sha":b"0"*64,b"reconciliation_token":b"0"*64,b"reconciliation_sha":b"0"*64,
  b"terminal_origin":0,b"terminal_deadline":0,b"terminal_mode":b"NONE",b"terminal_kind":b"NONE",b"terminal_subject":b"0"*64,
  b"terminal_phase":b"NOT_STARTED",b"ack_state":b"NOT_SENT",b"ack_effect_unknown":False,b"pass_effect_possible":False,b"pass_committed":False,
  b"control_state":b"CONNECTED",b"actor_state":b"ALIVE_PIDFD_NOT_READY",b"actor_control_fd":3,b"actor_pidfd_fd":4,b"actor_pidfd_provenance":None,b"actor_pidfd_exit_ready_observed":False,b"send_state":b"IDLE",
  b"actor_receive_state":b"NONE",b"actor_receive_ordinal":b"NONE",b"actor_receive_probe":b"NONE",b"actor_receive_deadline":1,
  b"transfer_control":None,b"transfer_control_fd":14,b"actor_control":None,b"external_owner_pidfd_fd":15,b"external_owner_pidfd_provenance":None,b"external_owner_pidfd_exit_ready_observed":False,b"external_record_seq":0,b"external_chain_sha":RESERVATION_DIGEST,b"external_send_state":b"IDLE",b"transfer_state":b"NOT_OFFERED",b"transfer_offer_cache":None,b"frozen_transfer_reason":None,b"offer_delivery_possible":False,b"transfer_receipt_sha":b"0"*64,b"transfer_acceptance_state":b"NOT_STARTED",b"transfer_capabilities_closed":False,b"refusal_closure_sha":b"0"*64,
  b"refusal_prevalidation_state":b"NOT_SEEN",b"refusal_slot_locked":False,b"refusal_offer_cache":None,b"refusal_close_state":b"CLOSE_NOT_ATTEMPTED",b"refusal_finality_state":b"OPEN",b"refusal_control_eof":False,b"refusal_actor_loss_seen":False,b"refusal_candidate_fault_evidence":(),b"refusal_candidate_fault_overflow":0,b"refusal_finality_evidence_sha":EMPTY_SHA,b"refusal_finality_timeout_observed":False,b"refusal_frozen_state_sha":EMPTY_SHA,b"refusal_offer_delivery_possible":False,b"refusal_offer_complete":False,b"refusal_offer_state":b"NOT_STARTED",b"refusal_offer_receipt_sha":b"0"*64,b"refusal_acceptance_state":b"NOT_STARTED",b"refusal_acceptance_hold_reason":b"NONE",b"refusal_actor_closure_complete":False,b"refusal_actor_closure_state":b"NOT_STARTED",b"refusal_capabilities_closed":False,b"refusal_closure_hold_state":b"NONE",
  b"outcome_durable":False,b"owner_released":False
 }

def ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,error):
 context[b"consumed"]=True;context[b"consumption_state"]=b"CONSUME_EDGE_UNKNOWN";context[b"faults"].add(b"CONSUME_EDGE_UNKNOWN")
 if isinstance(error,RemoteAbort):
  context[b"faults"].update(error.faults);context[b"release_disabled"]=True
 elif isinstance(error,PidfdActorLost):
  mark_actor_pidfd_lost(context)
 elif isinstance(error,FaultSet):context[b"faults"].update(error.faults)
 try:consume_attempt(context,cert_raw,envelope_raw,source_raw,context[b"consume_deadline"])
 except CertificateExpired:context[b"faults"].add(b"CERTIFICATE_EXPIRED")
 except FaultSet as attempt_error:context[b"faults"].update(attempt_error.faults)
 terminal_failure(control,context,b"NONE",set(context[b"faults"]),isinstance(error,PidfdActorLost))

def refusal_values(raw,kind):
 need(kind in (b"V15_REFUSE_PREBEGIN",b"V15_REFUSE_POSTARM"))
 keys=(b"state",b"ordinal",b"probe",b"auth_id",b"a_begin_state",b"a_arm_state",b"cross_map_state",b"reason",b"refusal_origin_ns",b"refusal_finality_deadline_ns",b"refusal_closure_deadline_ns",b"refusal_schedule_hex",b"consume_deadline_ns")
 actual_pre_state=b"WAIT_BEGIN" if kind==b"V15_REFUSE_PREBEGIN" else b"WAIT_COMMIT"
 values=parse_packet(raw,kind,keys,received_binding(raw,actual_pre_state,b"NONE",b"NONE",b"consume_deadline_ns",certificate_mono_expiry(CERT)))
 if kind==b"V15_REFUSE_PREBEGIN":
  need(values[b"state"]==b"REFUSE_PREBEGIN" and values[b"expected_state"]==b"WAIT_BEGIN")
  need((values[b"a_begin_state"],values[b"a_arm_state"],values[b"cross_map_state"])==(b"BEGIN_NOT_ENTERED",b"ARM_NOT_OBSERVED",b"ARM_NOT_ENTERED"))
 else:
  need(values[b"state"]==b"REFUSE_POSTARM" and values[b"expected_state"]==b"WAIT_COMMIT")
  need((values[b"a_begin_state"],values[b"a_arm_state"],values[b"cross_map_state"])==(b"BEGIN_SENT",b"ARMED_CONFIRMED",b"REFUSAL_CLOSED_NO_CONSUME"))
 need(values[b"ordinal"]==values[b"probe"]==b"NONE" and values[b"auth_id"]==AUTH and values[b"reason"])
 origin=udec(values[b"refusal_origin_ns"],1);finality_deadline=udec(values[b"refusal_finality_deadline_ns"],1);closure_deadline=udec(values[b"refusal_closure_deadline_ns"],1)
 schedule=check_schedule_hex(values[b"refusal_schedule_hex"],origin,closure_deadline,REFUSAL_PHASE_SPEC)
 need(finality_deadline==schedule[b"REFUSAL_FINALITY"]==origin+REFUSAL_FINALITY_NS and closure_deadline==schedule[b"REFUSAL_CLOSURE"])
 need(closure_deadline-finality_deadline==REFUSAL_CLOSURE_TAIL_NS and closure_deadline<=certificate_mono_expiry(CERT))
 need(udec(values[b"consume_deadline_ns"])==schedule[b"REFUSAL_RECORD"] and time.monotonic_ns()<=schedule[b"REFUSAL_RECORD"])
 return values,schedule

def close_no_consume(context):
 need(not context[b"consumed"] and context[b"record_seq"]==0 and not context[b"intent_durable"] and context[b"attempt"]<0)
 if context.get(b"attempt_base_fd",5)>=0:
  close_lifecycle_fd(context,b"attempt_base_fd")
 if context.get(b"cgroup_base_fd",6)>=0:
  close_lifecycle_fd(context,b"cgroup_base_fd")
 os.chdir(b"/");rootfd=acquire_lifecycle_open(context,b"refusal_runtime_root_fd",b"RUNTIME_ROOT_VERIFY_DIRFD",b".",O_DIR)
 try:base_check(rootfd,CERT,b"RUNTIME_ROOT");fd_access(rootfd,os.O_RDONLY)
 finally:close_lifecycle_fd(context,b"refusal_runtime_root_fd")
 context[b"consumption_state"]=b"REFUSAL_CLOSED_NO_CONSUME";context[b"refusal_closed"]=True
 context[b"commit_count"]=0;context[b"attempt_state"]=b"ABSENT_KNOWN";context[b"intent_count"]=0
 need(context[b"attempt_base_fd"]<0 and context[b"commit_count"]==context[b"intent_count"]==0 and context[b"attempt_state"]==b"ABSENT_KNOWN")

def refusal_session(control,context,raw,kind):
 need(not refusal_lock_invariant(context) and not context[b"consumed"])
 try:values,schedule=refusal_values(raw,kind)
 except StaticReject:
  context[b"refusal_prevalidation_state"]=b"REJECTED_UNLOCKED_NONCONSUMING"
  need(not context[b"refusal_slot_locked"] and context[b"refusal_offer_cache"] is None and not context[b"consumed"]);return
 context[b"refusal_prevalidation_state"]=b"VALIDATED_UNLOCKED_NONCONSUMING"
 try:
  stage_refusal_slot(context,raw,kind,values,schedule)
  ack_deadline=schedule[b"REFUSAL_ACK"];finality_deadline=schedule[b"REFUSAL_FINALITY"];closure_deadline=schedule[b"REFUSAL_CLOSURE"]
  cached=refusal_slot(context);need(cached[2]==b"ACK_NOT_CONSTRUCTED" and cached[3]==b"CLOSE_NOT_ATTEMPTED" and cached[4]==b"" and cached[5]==0)
  ack,reserved_ack_sequence=reserve_packet(b"V15_REFUSE_ACK",((b"state",b"REFUSAL_CLOSED_NO_CONSUME"),(b"expected_state",b"WAIT_REFUSAL_ACK"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH),(b"a_begin_state",values[b"a_begin_state"]),(b"a_arm_state",values[b"a_arm_state"]),(b"cross_map_state",values[b"cross_map_state"]),(b"request_packet_sha256",values[b"packet_sha256"]),(b"request_message_seq",values[b"message_seq"]),(b"commit_count",b"0"),(b"attempt_state",b"ABSENT_KNOWN"),(b"intent_count",b"0"),(b"disposition",b"UNCONSUMED"),(b"refusal_origin_ns",values[b"refusal_origin_ns"]),(b"refusal_finality_deadline_ns",values[b"refusal_finality_deadline_ns"]),(b"refusal_closure_deadline_ns",values[b"refusal_closure_deadline_ns"]),(b"refusal_schedule_hex",values[b"refusal_schedule_hex"]),(b"consume_deadline_ns",str(ack_deadline).encode())))
  cached=refusal_slot_transition(context,b"ACK_CACHED_PRE_CLOSE",ack_raw=ack,ack_sequence=reserved_ack_sequence)
  need(cached[2]==b"ACK_CACHED_PRE_CLOSE" and cached[3]==b"CLOSE_NOT_ATTEMPTED" and cached[4]==ack and cached[5]==reserved_ack_sequence and not context[b"refusal_closed"])
  context[b"refusal_ack_raw"]=ack;context[b"refusal_offer_state"]=b"EXACT_ACK_CACHED_PRE_CLOSE"
  refusal_slot_transition(context,b"CLOSE_EFFECT_UNKNOWN",close_state=b"CLOSE_EFFECT_UNKNOWN")
  close_no_consume(context)
  cached=refusal_slot_transition(context,b"ACK_READY_CLOSED",close_state=b"CLOSED_NO_CONSUME")
  need(cached[4]==ack and cached[5]==reserved_ack_sequence and cached[3]==b"CLOSED_NO_CONSUME" and context[b"refusal_closed"])
  activate_reserved_packet(ack,reserved_ack_sequence);refusal_slot_transition(context,b"ACK_EFFECT_UNKNOWN")
  context[b"send_state"]=b"REFUSAL_ACK_SEND_EFFECT_UNKNOWN"
  try:
   send_exact(control,ack,ack_deadline);context[b"send_state"]=b"REFUSAL_ACK_SENT";refusal_slot_transition(context,b"WAITING_RECEIPT")
  except SendEffectUnknown:context[b"send_state"]=b"REFUSAL_ACK_SEND_EFFECT_UNKNOWN"
  if not await_refusal_finality(control,context):
   transfer_or_hold(control,context,b"RECONCILIATION_UNKNOWN");return
  closure=issuer_refusal_close(context);need(context[b"refusal_offer_complete"] and closure==context[b"refusal_closure_sha"])
  complete_refusal_closure(control,context);return
 except BaseException as error:
  if context.get(b"refusal_slot_locked",False):
   route_locked_refusal(control,context,error);return
  context[b"refusal_prevalidation_state"]=b"STAGING_REJECTED_UNLOCKED_NONCONSUMING"
  need(context[b"refusal_offer_cache"] is None and not context[b"consumed"]);raise
def main():
 global ACTIVE_LIFECYCLE_CONTEXT
 context=minimal_context();ACTIVE_LIFECYCLE_CONTEXT=context;control=transfer_control=None
 try:
  bootstrap_lifecycle_registry(context)
  control,transfer_control,cert_raw,envelope_raw,reservation_raw,source_raw=static_inputs(context);context[b"external_chain_sha"]=RESERVATION_DIGEST
  context[b"actor_pidfd_provenance"]=(4,ACTOR_PID,ACTOR_STARTTIME);bind_lifecycle_provenance(context,b"actor_pidfd_fd",context[b"actor_pidfd_provenance"]);actor_pidfd_provenance(context)
  external_pid=udec(CERT[b"EXTERNAL_OWNER_PID"],2);external_start=udec(CERT[b"EXTERNAL_OWNER_STARTTIME"],1);context[b"external_owner_pidfd_provenance"]=(15,external_pid,external_start);bind_lifecycle_provenance(context,b"external_owner_pidfd_fd",context[b"external_owner_pidfd_provenance"])
  ready_deadline=time.monotonic_ns()+10000000000
  ready=packet(b"V15_READY",((b"state",b"READY"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"ready_deadline_ns",str(ready_deadline).encode())))
  send_exact(control,ready,ready_deadline)
  raw,fds=recv_monitored(control,context,4,ready_deadline,0,b"WAIT_BEGIN",b"NONE",b"NONE");need(fds==())
  if raw.startswith(b"V15_REFUSE_PREBEGIN|"):
   refusal_session(control,context,raw,b"V15_REFUSE_PREBEGIN");return
  begin=parse_packet(raw,b"V15_CONSUME_BEGIN",(b"state",b"ordinal",b"probe",b"auth_id",b"a_begin_state",b"a_arm_state",b"consume_origin_ns",b"consume_deadline_ns"),received_binding(raw,b"WAIT_BEGIN",b"NONE",b"NONE",b"consume_deadline_ns",ready_deadline))
  need(begin[b"state"]==b"CONSUME_BEGIN" and begin[b"ordinal"]==begin[b"probe"]==b"NONE" and begin[b"auth_id"]==AUTH)
  need(begin[b"a_begin_state"]==b"BEGIN_SEND_EFFECT_UNKNOWN" and begin[b"a_arm_state"]==b"ARM_NOT_OBSERVED")
  origin=udec(begin[b"consume_origin_ns"],1);deadline=udec(begin[b"consume_deadline_ns"],1)
  need(deadline==origin+CONSUMPTION_NS and time.monotonic_ns()<=deadline);checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
  context[b"begin_observed"]=True;context[b"consume_origin"]=origin;context[b"consume_deadline"]=deadline
  need(time.monotonic_ns()<=deadline-REFUSAL_TOTAL_NS)
  context[b"consumption_state"]=b"ARM_SEND_EFFECT_UNKNOWN";context[b"arm_effect_possible"]=True;context[b"send_state"]=b"ARM_SEND_EFFECT_UNKNOWN"
  armed=packet(b"V15_CONSUME_ARMED",((b"state",b"CONSUME_ARMED"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH),(b"a_begin_state",b"BEGIN_SEND_EFFECT_UNKNOWN"),(b"b_arm_state",b"ARM_SEND_EFFECT_UNKNOWN"),(b"consume_origin_ns",str(origin).encode()),(b"consume_deadline_ns",str(deadline).encode())))
  send_exact(control,armed,deadline);context[b"consumption_state"]=b"ARM_SENT";context[b"send_state"]=b"ARM_SENT"
  try:
   raw,fds=recv_monitored(control,context,4,deadline,0,b"WAIT_COMMIT",b"NONE",b"NONE");need(fds==())
   if raw.startswith(b"V15_REFUSE_POSTARM|"):
    refusal_session(control,context,raw,b"V15_REFUSE_POSTARM");return
   commit=parse_packet(raw,b"V15_CONSUME_COMMIT",(b"state",b"ordinal",b"probe",b"auth_id",b"a_begin_state",b"a_arm_state",b"a_commit_state",b"consume_origin_ns",b"consume_deadline_ns"),receiver_binding(b"WAIT_COMMIT",b"NONE",b"NONE",deadline))
   need(commit[b"state"]==b"CONSUME_COMMIT" and commit[b"ordinal"]==commit[b"probe"]==b"NONE" and commit[b"auth_id"]==AUTH)
   need(commit[b"a_begin_state"]==b"BEGIN_SENT" and commit[b"a_arm_state"]==b"ARMED_CONFIRMED" and commit[b"a_commit_state"]==b"COMMIT_SEND_EFFECT_UNKNOWN")
   need(udec(commit[b"consume_origin_ns"])==origin and udec(commit[b"consume_deadline_ns"])==deadline)
  except (PidfdActorLost,RemoteAbort,CertificateExpired,FaultSet) as error:
   ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,error);return
  context[b"consumed"]=True;context[b"consumption_state"]=b"COMMIT_RECEIVED"
  try:intent_sha=consume_attempt(context,cert_raw,envelope_raw,source_raw,deadline)
  except (CertificateExpired,FaultSet) as error:
   context[b"faults"].update(error.faults if isinstance(error,FaultSet) else {b"CERTIFICATE_EXPIRED"})
   terminal_failure(control,context,b"NONE",set(context[b"faults"]),False);return
  checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
  consumed=packet(b"V15_CONSUMED_DURABLE",((b"state",b"CONSUMED_DURABLE"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH),(b"intent_sha256",intent_sha),(b"consume_origin_ns",str(origin).encode()),(b"consume_deadline_ns",str(deadline).encode()),(b"attempt_fd_state",context[b"local_fd_state"])))
  send_exact(control,consumed,deadline)
  stage_bind(control,context);containment_bind(control,context)
  for ordinal,probe in enumerate(PROBES):
   context[b"entered"]=ordinal+1;checkpoint(CERT,(15-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS)
   try:
    stream_arm(control,context,ordinal,probe);pidfd_arm(control,context,ordinal,probe);release_phase(control,context,ordinal,probe)
    actor_lost,faults,empty,stdout,stderr,result_complete=monitor_probe(control,context,ordinal,probe)
    if actor_lost:raise PidfdActorLost("probe")
    if result_complete:validated_exchange(control,context,ordinal,probe,stdout,stderr,faults)
    elif faults:raise FaultSet(faults)
    close_probe(context);checkpoint(CERT,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS)
   except RemoteAbort as error:
    context[b"faults"].update(error.faults);context[b"release_disabled"]=error.values[b"release_disabled"]==b"1";context[b"stage_present"]=error.values[b"stage_present"]==b"1"
    terminal_failure(control,context,probe,set(context[b"faults"]),False);return
   except PidfdActorLost:
    context[b"faults"].add(b"PIDFD_ACTOR_LOST");terminal_failure(control,context,probe,set(context[b"faults"]),True);return
   except CertificateExpired:
    context[b"faults"].add(b"CERTIFICATE_EXPIRED");terminal_failure(control,context,probe,set(context[b"faults"]),False);return
   except FaultSet as error:
    context[b"faults"].update(error.faults);terminal_failure(control,context,probe,set(context[b"faults"]),False);return
  preterminal_arrival_deadline=context[b"origin"]+TOTAL_NS;raw,fds=recv_monitored(control,context,4,preterminal_arrival_deadline,0,b"WAIT_EMPTY_QUERY",b"NONE",b"NONE");need(fds==())
  query=parse_packet(raw,b"V15_EMPTY_FINAL_QUERY",(b"state",b"ordinal",b"probe",b"chain_head_sha256",b"remove_origin_ns",b"remove_deadline_ns"),received_binding(raw,b"WAIT_EMPTY_QUERY",b"NONE",b"NONE",b"remove_deadline_ns",preterminal_arrival_deadline+REPORT_NS))
  remove_origin=udec(query[b"remove_origin_ns"],1);remove_deadline=udec(query[b"remove_deadline_ns"],1)
  need(query[b"state"]==b"EMPTY_FINAL_QUERY" and query[b"ordinal"]==query[b"probe"]==b"NONE" and query[b"chain_head_sha256"]==context[b"actor_known_chain_sha"])
  need(remove_deadline==remove_origin+REPORT_NS and remove_origin<=time.monotonic_ns()<=remove_deadline)
  checkpoint(CERT,horizon_needed(remove_deadline,FINAL_TOTAL_NS),remove_deadline);need(observe_population(context) is False)
  confirmed=packet(b"V15_EMPTY_FINAL_CONFIRMED",((b"state",b"EMPTY_FINAL_CONFIRMED"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"chain_head_sha256",context[b"chain_sha"]),(b"remove_deadline_ns",str(remove_deadline).encode())))
  send_exact(control,confirmed,remove_deadline)
  raw,fds=recv_monitored(control,context,4,remove_deadline,0,b"WAIT_REMOVED",b"NONE",b"NONE");need(fds==())
  removed=parse_packet(raw,b"V15_CGROUP_REMOVED",(b"state",b"ordinal",b"probe",b"chain_head_sha256",b"remove_deadline_ns"),receiver_binding(b"WAIT_REMOVED",b"NONE",b"NONE",remove_deadline))
  need(removed[b"state"]==b"CGROUP_REMOVED" and removed[b"ordinal"]==removed[b"probe"]==b"NONE" and removed[b"chain_head_sha256"]==context[b"chain_sha"] and udec(removed[b"remove_deadline_ns"])==remove_deadline)
  try:os.stat(AUTH,dir_fd=6,follow_symlinks=False);need(False)
  except FileNotFoundError:pass
  context[b"removed"]=True;checkpoint(CERT,horizon_needed(remove_deadline,FINAL_TOTAL_NS),remove_deadline)
  ack=packet(b"V15_REMOVE_ACK",((b"state",b"REMOVE_ACK"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"chain_head_sha256",context[b"chain_sha"]),(b"remove_deadline_ns",str(remove_deadline).encode())))
  send_exact(control,ack,remove_deadline)
  raw,fds=recv_monitored(control,context,4,remove_deadline,0,b"WAIT_FINALIZE",b"NONE",b"NONE");need(fds==())
  finalize=parse_packet(raw,b"V15_FINALIZE_CANDIDATE",(b"state",b"ordinal",b"probe",b"chain_head_sha256",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"candidate_deadline_ns"),received_binding(raw,b"WAIT_FINALIZE",b"NONE",b"NONE",b"candidate_deadline_ns",remove_deadline+FINAL_TOTAL_NS))
  terminal_origin=udec(finalize[b"terminal_origin_ns"],1);terminal_deadline=udec(finalize[b"terminal_deadline_ns"],1)
  need(finalize[b"state"]==b"FINALIZE_CANDIDATE" and finalize[b"expected_state"]==b"WAIT_FINALIZE" and finalize[b"ordinal"]==finalize[b"probe"]==b"NONE" and finalize[b"chain_head_sha256"]==context[b"chain_sha"])
  need(terminal_deadline==terminal_origin+FINAL_TOTAL_NS and terminal_origin<=time.monotonic_ns()<=terminal_deadline)
  schedule=check_schedule_hex(finalize[b"terminal_schedule_hex"],terminal_origin,terminal_deadline,TERMINAL_PHASE_SPEC)
  need(udec(finalize[b"candidate_deadline_ns"])==schedule[b"CANDIDATE_RECORD"])
  context[b"terminal_origin"]=terminal_origin;context[b"terminal_deadline"]=terminal_deadline;context[b"terminal_schedule"]=schedule;context[b"last_population"]=observe_population(context)
  checkpoint(CERT,horizon_needed(terminal_deadline,0),terminal_deadline)
  need(context[b"entered"]==sum(context[b"committed"])==context[b"direct_reaps"]==context[b"stopped_count"]==15)
  need(context[b"stage_state"]==b"VERIFIED_PRESENT" and context[b"containment_bound"] and context[b"removed"] and context[b"last_population"] is False and not context[b"faults"] and context[b"kill_call_count"]==0 and context[b"kill_state"]==b"NOT_RESERVED")
  candidate_sha=terminal_candidate_record(context,b"SUCCESS",b"NONE",schedule)
  terminal_owner_loop(control,context,b"SUCCESS",b"SUCCESS_CANDIDATE",candidate_sha,b"PASS",terminal_deadline)
 except RemoteAbort as error:
  context[b"faults"].update(error.faults);context[b"release_disabled"]=error.values[b"release_disabled"]==b"1";context[b"stage_present"]=error.values[b"stage_present"]==b"1"
  if context[b"refusal_slot_locked"]:
   if not context[b"owner_released"]:transfer_or_hold(control,context,b"RECONCILIATION_UNKNOWN")
  elif pass_locked(context):
   context[b"faults"].add(b"ACK_EFFECT_UNKNOWN");transfer_or_hold(control,context,b"RECONCILIATION_UNKNOWN")
  elif context[b"arm_effect_possible"] and not context[b"consumed"]:
   ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,error)
  elif context[b"consumed"]:terminal_failure(control,context,b"NONE",set(context[b"faults"]),False)
  else:raise
 except PidfdActorLost as error:
  mark_actor_pidfd_lost(context)
  if context[b"refusal_slot_locked"]:
   if not context[b"owner_released"]:transfer_or_hold(control,context,b"PIDFD_ACTOR_LOST")
  elif pass_locked(context):
   context[b"faults"].add(b"ACK_EFFECT_UNKNOWN")
   if context[b"outcome_durable"] and context.get(b"terminal_schedule") is not None and terminal_safe(context):
    try:finish_actor_loss_chain(context,context[b"terminal_mode"],context[b"terminal_schedule"])
    except BaseException:transfer_or_hold(control,context,b"RECONCILIATION_UNKNOWN")
   else:transfer_or_hold(control,context,b"PIDFD_ACTOR_LOST")
  elif context[b"arm_effect_possible"] and not context[b"consumed"]:ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,error)
  elif context[b"consumed"]:terminal_failure(control,context,b"NONE",set(context[b"faults"]),True)
  else:raise
 except CertificateExpired as error:
  context[b"faults"].add(b"CERTIFICATE_EXPIRED")
  if context[b"refusal_slot_locked"]:
   if not context[b"owner_released"]:transfer_or_hold(control,context,b"RECONCILIATION_UNKNOWN")
  elif pass_locked(context):context[b"faults"].add(b"ACK_EFFECT_UNKNOWN");transfer_or_hold(control,context,b"RECONCILIATION_UNKNOWN")
  elif context[b"arm_effect_possible"] and not context[b"consumed"]:ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,error)
  elif context[b"consumed"]:terminal_failure(control,context,b"NONE",set(context[b"faults"]),False)
  else:raise
 except FaultSet as error:
  context[b"faults"].update(error.faults)
  if context[b"refusal_slot_locked"]:
   if not context[b"owner_released"]:transfer_or_hold(control,context,b"RECONCILIATION_UNKNOWN")
  elif pass_locked(context):context[b"faults"].add(b"ACK_EFFECT_UNKNOWN");transfer_or_hold(control,context,b"RECONCILIATION_UNKNOWN")
  elif context[b"arm_effect_possible"] and not context[b"consumed"]:ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,error)
  elif context[b"consumed"]:terminal_failure(control,context,b"NONE",set(context[b"faults"]),False)
  else:raise
 except BaseException as error:
  context[b"faults"].add(b"INTERNAL_INVARIANT")
  typed=FaultSet({b"INTERNAL_INVARIANT"})
  if context[b"refusal_slot_locked"]:
   if not context[b"owner_released"]:transfer_or_hold(control,context,b"INTERNAL_INVARIANT")
  elif pass_locked(context):context[b"faults"].add(b"ACK_EFFECT_UNKNOWN");transfer_or_hold(control,context,b"INTERNAL_INVARIANT")
  elif context[b"arm_effect_possible"] and not context[b"consumed"]:ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,typed)
  elif context[b"consumed"]:terminal_failure(control,context,b"NONE",set(context[b"faults"]),False)
  else:raise
 finally:
  if (context.get(b"begin_observed",False) or context[b"consumed"] or context[b"refusal_closed"] or context[b"refusal_slot_locked"]) and not context[b"owner_released"]:
   transfer_or_hold(control,context,b"EXTERNAL_SURVIVAL_TRANSFER_REQUIRED")
 if context[b"owner_released"]:
  need(ownership_capabilities_closed(context));close_probe(context);need(ownership_capabilities_closed(context))

# P27 RUNNER V19 WATCHDOG FINAL ENTRY BEGIN 19B0C702
WATCHDOG_INTERNAL_REVISION_V19=b"V19"
WATCHDOG_RECORD_COUNT_V19=97
WATCHDOG_LIBC_V19=ctypes.CDLL(None,use_errno=True)
WATCHDOG_AT_FDCWD_V19=-100
WATCHDOG_MSG_CMSG_CLOEXEC_V19=0x40000000
WATCHDOG_LIVE_STATES_V19=(b"ACQUIRING",b"OWNED",b"CLOSE_RETRY")
WATCHDOG_ENTRY_LIMIT_VECTOR_V19=(1048576,1048576)
WATCHDOG_CURRENT_LOW_LIMIT_VECTOR_V19=None
WATCHDOG_ENTRY_LIMIT_CERTIFIED_V19=False
WATCHDOG_SIMULTANEOUS_RECORD_ROLES_V19=tuple(slot for slot,kind,transferable in LIFECYCLE_SLOT_SPEC)
WATCHDOG_SIMULTANEOUS_MAX_INTAKE_ROLES_V19=tuple(b"MAX_VISIBLE_EXTERNAL_RIGHT_"+str(index).encode() for index in range(14))
WATCHDOG_SIMULTANEOUS_WRAPPER_FALLBACK_V19=(b"CONSTRUCTOR_LOCAL_STRONG_REFERENCE",)
WATCHDOG_SIMULTANEOUS_LIVE_ROLE_SET_V19=WATCHDOG_SIMULTANEOUS_RECORD_ROLES_V19+WATCHDOG_SIMULTANEOUS_MAX_INTAKE_ROLES_V19+WATCHDOG_SIMULTANEOUS_WRAPPER_FALLBACK_V19
WATCHDOG_LIVE_HIGH_WATER_V19=len(WATCHDOG_SIMULTANEOUS_LIVE_ROLE_SET_V19)
WATCHDOG_CLONE3_CPYTHON_SUBCONDITIONS_V19=(
 b"FROZEN_ENTRY_RLIMIT_NOFILE_1048576_1048576",
 b"CURRENT_RLIMIT_NOFILE_256_SAME_HARD",
 b"WATCHDOG_SIMULTANEOUS_LIVE_ROLE_SET_112_LT_256",
 b"FD_TARGET_AND_RESULT_RANGE_0_THROUGH_255",
 b"FROZEN_CPYTHON_CACHED_SMALL_INT_0_THROUGH_255",
 b"CTYPES_C_INT_RESULT_STORE_STATICALLY_NONFAILING",
)
WATCHDOG_INHERITED_FIXED_SPEC_V19=(
 (b"actor_control_fd",b"ACTOR_CONTROL_FD",3,True),(b"actor_pidfd_fd",b"ACTOR_PIDFD_NONTRANSFERABLE",4,False),
 (b"attempt_base_fd",b"ATTEMPT_BASE_DIRFD",5,True),(b"cgroup_base_fd",b"CGROUP_BASE_DIRFD",6,True),
 (b"certificate_carrier_fd",b"CERTIFICATE_CARRIER_FD",7,False),(b"envelope_carrier_fd",b"ENVELOPE_CARRIER_FD",8,False),
 (b"snapshot_carrier_fd",b"SNAPSHOT_CARRIER_FD",9,False),(b"plan_carrier_fd",b"PLAN_CARRIER_FD",10,False),
 (b"actor_source_carrier_fd",b"ACTOR_SOURCE_CARRIER_FD",11,False),(b"host_source_carrier_fd",b"HOST_SOURCE_CARRIER_FD",12,False),
 (b"reservation_carrier_fd",b"RESERVATION_CARRIER_FD",13,False),(b"transfer_control_fd",b"EXTERNAL_CONTROL_FD_NONTRANSFERABLE",14,False),
 (b"external_owner_pidfd_fd",b"EXTERNAL_OWNER_PIDFD_NONTRANSFERABLE",15,False),(b"external_manifest_carrier_fd",b"EXTERNAL_MANIFEST_CARRIER_FD",16,False),
 (b"watchdog_source_carrier_fd",b"WATCHDOG_SOURCE_CARRIER_FD",100,False),
)
WATCHDOG_OFFERED_SLOTS_V19=(
 b"attempt",b"attempt_base_fd",b"stage_fd",b"cgfd",b"root_events_fd",
 b"root_kill_fd",b"out_fd",b"err_fd",b"events_fd",b"outer_pidfd",
 b"cgroup_base_fd",b"actor_control_fd",b"pending_expected_raw_fd",
)
WATCHDOG_SAFE_LOCAL_SLOTS_V19=(
 b"transfer_control_fd",b"actor_pidfd_fd",b"external_owner_pidfd_fd",
 b"certificate_carrier_fd",b"envelope_carrier_fd",b"snapshot_carrier_fd",
 b"plan_carrier_fd",b"actor_source_carrier_fd",b"host_source_carrier_fd",
 b"reservation_carrier_fd",b"external_manifest_carrier_fd",
 b"watchdog_source_carrier_fd",
)
WATCHDOG_BLOCKING_FIXED_V19=(
 b"cap_status_fd",b"proc_starttime_fd",b"mount_fdinfo_fd",b"mount_table_fd",
 b"boot_id_fd",b"mount_graph_fd",b"dependency_root_fd",b"dependency_current_fd",
 b"dependency_following_fd",b"dependency_leaf_fd",b"reconcile_record_fd",
 b"record_create_fd",b"record_reopen_fd",b"attempt_received",
 b"pidfd_arm_procs_fd",b"pidfd_arm_status_fd",b"recovery_stage_base_fd",
 b"recovery_stage_received",b"recovery_stage_leaf_fd",b"stage_base_verify_fd",
 b"stage_received",b"stage_leaf_verify_fd",b"containment_received",
 b"containment_type_fd",b"containment_controllers_fd",b"containment_subtree_fd",
 b"containment_root_events_received",b"containment_root_kill_received",
 b"stream_out_received",b"stream_err_received",b"stream_events_received",
 b"outer_pidfd_received",b"static_runtime_root_fd",b"static_safe_base_fd",
 b"static_cgroup_type_fd",b"static_cgroup_controllers_fd",
 b"static_cgroup_subtree_fd",b"refusal_runtime_root_fd",
)+tuple(b"unexpected_control_right_"+str(index).encode() for index in range(4))+tuple(b"external_unexpected_right_"+str(index).encode() for index in range(13))+tuple(b"external_receipt_carrier_"+str(index).encode() for index in range(13))+tuple(b"refusal_unexpected_right_"+str(index).encode() for index in range(4))
WATCHDOG_IMMUTABLE_ROLE_SPEC_V19=tuple(
 (slot,kind,bool(transferable),LIFECYCLE_TRANSFER_ORDER.get(kind,-1))
 for slot,kind,transferable in LIFECYCLE_SLOT_SPEC
)
def watchdog_role_spec_v19(slot):
 for row in WATCHDOG_IMMUTABLE_ROLE_SPEC_V19:
  if row[0]==slot:return row
 need(False)

WATCHDOG_PHYSICAL_RECORD_FIELDS_V19=(
 "record_id","home_slot","state","semantic_role","raw_fd","identity","physical_identity",
 "leaf_identity","verified_kill_leaf_identity","access","provenance",
 "endpoint_state","wrapper_ref","detached_raw_fd","raw_cell","epoch",
 "wrapper_phase","wrapper_local_fallback","wrapper_probe_done","wrapper_detach_attempted",
)
WATCHDOG_RAW_CELL_FIELDS_V19=("cell_id","state","c_value","record_id","epoch")
WATCHDOG_POLLER_CELL_FIELDS_V19=("cell_id","state","poller","record_id","raw_fd","mask","epoch")
WATCHDOG_RECEIVE_FRAME_FIELDS_V19=(
 "site","semantic_capacity","installed_capacity","ancillary_bytes","kernel_control_bytes",
 "payload","control","iov","hdr","header_views","int_views","raw_cells",
 "records","expected_slots","promoted","provenances","installed_count","payload_count",
 "msg_flags","capture_complete","validation_complete","capture_fault","cleanup_cursor","cleanup_pending","original_fault","immediate_checkpoint_done","epoch",
)
WATCHDOG_CENSUS_FIELDS_V19=("epoch","phase","mode","full_live","offered","safe_local","blocking","kill","raw","digest")
WATCHDOG_CACHE_FIELDS_V19=(
 "kind","state","epoch","boundary","storage","length","offer_sha",
 "frozen_full","frozen_offered","frozen_safe","frozen_kill","frozen_raw",
 "frozen_census_sha","capability_sha","identity_sha","outer_record_id",
 "outer_state","mode","frozen_wire_rows","wire_sha","possible_send","sent_once","atomic_authority","prepared_sequence",
)
WATCHDOG_ACCEPTANCE_FIELDS_V19=(
 "state","mode","offer_sha","record_seq","predecessor","receipt_sha",
 "frozen_census_sha","current_census_sha","installed_history",
 "current_retained","kill_census","outer_record_id","outer_disposition",
 "no_replay","commit_epoch","candidate","authority",
)
WATCHDOG_CLOSURE_FIELDS_V19=(
 "phase","mode","plan","plan_count","cursor","current_record_id",
 "retry_ms","timing_overrun","commit_state","commit_offer_sha","epoch",
 "acceptance_authority","preclose_done","preclose_state","preclose_packet","preclose_packet_sha",
 "preclose_sequence","preclose_deadline","preclose_send_latch","retained_fault","release_handoff",
)

class WatchRawCellV19:
 __slots__=("cell_id","state","c_value","record_id","epoch")
 def __init__(self,cell_id):
  self.cell_id=cell_id;self.state=b"EMPTY";self.c_value=ctypes.c_int(-1)
  self.record_id=-1;self.epoch=0

class WatchPhysicalRecordV19:
 __slots__=(
  "record_id","home_slot","state","semantic_role","raw_fd","identity","physical_identity",
  "leaf_identity","verified_kill_leaf_identity","access","provenance",
  "endpoint_state","wrapper_ref","detached_raw_fd","raw_cell","epoch",
  "wrapper_phase","wrapper_local_fallback","wrapper_probe_done","wrapper_detach_attempted",
 )
 def __init__(self,record_id,slot,kind,transferable,raw_cell):
  spec=watchdog_role_spec_v19(slot);need(spec[1]==kind and spec[2]==bool(transferable))
  self.record_id=record_id;self.home_slot=slot;self.state=b"CLOSED";self.semantic_role=None
  self.raw_fd=-1;self.identity=None;self.physical_identity=None
  self.leaf_identity=None;self.verified_kill_leaf_identity=None;self.access=b"UNKNOWN";self.provenance=None
  self.endpoint_state=b"NO_WRAPPER";self.wrapper_ref=None
  self.detached_raw_fd=-1;self.raw_cell=raw_cell;self.epoch=0
  self.wrapper_phase=b"NO_CONSTRUCTOR";self.wrapper_local_fallback=-1
  self.wrapper_probe_done=False;self.wrapper_detach_attempted=False
 def __getitem__(self,index):
  spec=(b"QUARANTINE",b"QUARANTINE",False,-1) if self.semantic_role is None else watchdog_role_spec_v19(self.semantic_role)
  if index==0:return spec[1]
  if index==1:return self.raw_fd
  if index==2:return self.identity
  if index==3:return self.state
  if index==4:return spec[2]
  if index==5:return self.provenance
  if index==6:return self.state in WATCHDOG_LIVE_STATES_V19 and self.raw_fd>=0
  if index==7:return spec[3]
  raise IndexError(index)
 def __setitem__(self,index,value):
  if index==1:self.raw_fd=value
  elif index==2:self.identity=value
  elif index==3:self.state=value
  elif index==5:self.provenance=value
  elif index==6:need(bool(value)==(self.state in WATCHDOG_LIVE_STATES_V19 and self.raw_fd>=0))
  elif index in (0,4,7):need(value==self[index])
  else:raise IndexError(index)
 def __iter__(self):
  for index in range(8):yield self[index]

class WatchPollerCellV19:
 __slots__=("cell_id","state","poller","record_id","raw_fd","mask","epoch")
 def __init__(self,cell_id):
  self.cell_id=cell_id;self.state=b"FREE";self.poller=None
  self.record_id=-1;self.raw_fd=-1;self.mask=0;self.epoch=0

WATCHDOG_RECORD_RAW_CELLS_V19=tuple(WatchRawCellV19(b"watch_record_raw_"+str(index).encode()) for index in range(WATCHDOG_RECORD_COUNT_V19))
WATCHDOG_PHYSICAL_RECORDS_V19=tuple(
 WatchPhysicalRecordV19(index,slot,kind,transferable,WATCHDOG_RECORD_RAW_CELLS_V19[index])
 for index,(slot,kind,transferable) in enumerate(LIFECYCLE_SLOT_SPEC)
)
WATCHDOG_RECORD_BY_HOME_V19={
 slot:WATCHDOG_PHYSICAL_RECORDS_V19[index]
 for index,(slot,kind,transferable) in enumerate(LIFECYCLE_SLOT_SPEC)
}
WATCHDOG_POLLER_CELLS_V19=tuple(WatchPollerCellV19(index) for index in range(2048))

class WatchRegistryViewV19:
 __slots__=("home",)
 def __init__(self,home):self.home=home
 def __contains__(self,slot):return slot in self.home
 def __getitem__(self,slot):
  need(slot in self.home)
  for record in WATCHDOG_PHYSICAL_RECORDS_V19:
   if record.state in WATCHDOG_LIVE_STATES_V19 and record.semantic_role==slot:return record
  home=self.home[slot]
  if home.state==b"CLOSED":return home
  for record in WATCHDOG_PHYSICAL_RECORDS_V19:
   if record.state==b"CLOSED" and record.semantic_role is None:return record
  need(False)
 def get(self,slot,default=None):return self[slot] if slot in self.home else default
 def items(self):
  for slot,kind,transferable in LIFECYCLE_SLOT_SPEC:yield slot,self[slot]
 def __setitem__(self,slot,record):raise OwnershipClosePending("derived-watchdog-registry-is-not-mutable")

WATCHDOG_DERIVED_REGISTRY_V19=WatchRegistryViewV19(WATCHDOG_RECORD_BY_HOME_V19)

class LifecycleContextV19(dict):
 def __getitem__(self,key):
  if key in LIFECYCLE_SLOT_SPEC_MAP and dict.__contains__(self,b"fd_registry"):
   return dict.__getitem__(self,b"fd_registry")[key].raw_fd
  return dict.__getitem__(self,key)
 def get(self,key,default=None):
  if key in LIFECYCLE_SLOT_SPEC_MAP and dict.__contains__(self,b"fd_registry"):
   value=dict.__getitem__(self,b"fd_registry")[key].raw_fd
   return default if value is None else value
  return dict.get(self,key,default)
 def __setitem__(self,key,value):
  if key in LIFECYCLE_SLOT_SPEC_MAP and dict.__contains__(self,b"fd_registry"):
   record=dict.__getitem__(self,b"fd_registry")[key]
   need(value in (-1,record.raw_fd))
   return
  dict.__setitem__(self,key,value)

def watchdog_record_live_v19(record):
 return record.state in WATCHDOG_LIVE_STATES_V19 and record.raw_fd>=0

def watchdog_record_reset_v19(record):
 cell=record.raw_cell;cell.state=b"EMPTY";cell.c_value.value=-1
 cell.record_id=record.record_id;cell.epoch=record.epoch
 record.state=b"CLOSED";record.semantic_role=None;record.raw_fd=-1;record.identity=None
 record.physical_identity=None;record.leaf_identity=None;record.verified_kill_leaf_identity=None
 record.access=b"UNKNOWN";record.provenance=None
 record.endpoint_state=b"NO_WRAPPER";record.wrapper_ref=None;record.detached_raw_fd=-1
 record.wrapper_phase=b"NO_CONSTRUCTOR";record.wrapper_local_fallback=-1
 record.wrapper_probe_done=False;record.wrapper_detach_attempted=False

def watchdog_registry_slot_v19(context,record):
 role=record.semantic_role if record.semantic_role is not None else record.home_slot
 need(role in LIFECYCLE_SLOT_SPEC_MAP);return role

def new_lifecycle_registry():
 for record in WATCHDOG_PHYSICAL_RECORDS_V19:
  need(record.state==b"CLOSED" and record.raw_fd==-1)
 return WATCHDOG_DERIVED_REGISTRY_V19

def new_pidfd_poller_records():
 for cell in WATCHDOG_POLLER_CELLS_V19:
  cell.state=b"FREE";cell.poller=None;cell.record_id=-1;cell.raw_fd=-1
  cell.mask=0;cell.epoch=0
 return WATCHDOG_POLLER_CELLS_V19

def lifecycle_live_number_owner(context,number,exclude=None):
 owner=None
 for slot,record in context[b"fd_registry"].items():
  if slot!=exclude and watchdog_record_live_v19(record) and record.raw_fd==number:
   need(owner is None);owner=slot
 return owner

def lifecycle_identity(number):
 held=os.fstat(number);access=fcntl.fcntl(number,fcntl.F_GETFL)&os.O_ACCMODE
 return (held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,access)

def lifecycle_bind_identity_v19(record):
 need(watchdog_record_live_v19(record))
 observed=lifecycle_identity(record.raw_fd)
 if record.physical_identity is not None:need(observed==record.physical_identity)
 record.physical_identity=observed;record.identity=observed
 if record.leaf_identity is None:record.leaf_identity=(b"PHYSICAL",observed[0],observed[1])
 record.access=observed[6];return observed

def lifecycle_audit(context,slot,record=None):
 if record is None:record=context[b"fd_registry"][slot]
 spec=watchdog_role_spec_v19(slot)
 try:context[b"fd_close_journal"].append((slot,record.record_id,record.state,spec[1],record.raw_fd,record.identity,record.access,record.endpoint_state))
 except BaseException:context[b"fd_journal_complete"]=False

def lifecycle_begin_acquisition(context,slot,kind,transferable,provenance):
 spec=watchdog_role_spec_v19(slot);need(spec[1]==kind and spec[2]==bool(transferable))
 record=context[b"fd_registry"][slot];need(record.state==b"CLOSED" and record.raw_fd==-1)
 watchdog_record_reset_v19(record)
 try:
  record.epoch+=1;record.semantic_role=slot;record.state=b"ACQUIRING"
  record.identity=None;record.physical_identity=None;record.leaf_identity=None
  record.verified_kill_leaf_identity=None;record.access=b"UNKNOWN";record.provenance=provenance
  record.endpoint_state=b"NO_WRAPPER";record.wrapper_ref=None;record.detached_raw_fd=-1
  cell=record.raw_cell;need(cell.state in (b"EMPTY",b"DISARMED"))
  cell.state=b"EMPTY";cell.c_value.value=-1;cell.record_id=record.record_id;cell.epoch=record.epoch
  return record
 except BaseException:
  if record.raw_fd>=0:record.state=b"CLOSE_RETRY"
  else:watchdog_record_reset_v19(record)
  raise

def lifecycle_capture_cell_v19(record,cell):
 number=cell.c_value.value
 if number>=0:
  if record.raw_fd<0:record.raw_fd=number;record.state=b"ACQUIRING"
  else:need(record.raw_fd==number)
  cell.record_id=record.record_id;cell.epoch=record.epoch;cell.state=b"SHADOW_OF_RECORD"
  if number>255:record.state=b"CLOSE_RETRY";raise OwnershipClosePending("watchdog-fd-above-cached-bound")
 elif record.state==b"ACQUIRING" and record.raw_fd<0:
  watchdog_record_reset_v19(record);cell.state=b"DISARMED"
 return number

def lifecycle_finish_adoption(context,slot):
 record=context[b"fd_registry"][slot];need(watchdog_record_live_v19(record))
 need(record.semantic_role==slot and lifecycle_live_number_owner(context,record.raw_fd,slot) is None)
 try:
  lifecycle_bind_identity_v19(record)
  need(record.physical_identity is not None and len(record.physical_identity)==7 and record.access!=b"UNKNOWN")
  record.state=b"OWNED"
 except BaseException:
  record.state=b"CLOSE_RETRY"
  try:close_lifecycle_fd(context,slot)
  except BaseException:pass
  raise
 context[slot]=record.raw_fd;return record.raw_fd

def lifecycle_adopt_raw(context,slot,kind,number,transferable=False,provenance=None):
 record=None
 try:
  record=lifecycle_begin_acquisition(context,slot,kind,transferable,provenance)
  record.raw_cell.c_value.value=number
 finally:
  if record is not None:lifecycle_capture_cell_v19(record,record.raw_cell)
 if record.raw_fd<0:raise OwnershipClosePending("inherited-adoption-no-fd")
 return lifecycle_finish_adoption(context,slot)

def register_lifecycle_fd(context,slot,kind,number,transferable=False,provenance=None):
 return lifecycle_adopt_raw(context,slot,kind,number,transferable,provenance)

def lifecycle_scalar_boundary_v19(context,slot,kind,operation,arg0,arg1=0,arg2=0,arg3=None,transferable=False,provenance=None):
 record=None;cell=None;result=-1;saved=0
 try:
  record=lifecycle_begin_acquisition(context,slot,kind,transferable,provenance);cell=record.raw_cell
  if operation==b"OPENAT":
   directory=WATCHDOG_AT_FDCWD_V19 if arg3 is None else arg3
   result=WATCHDOG_LIBC_V19.openat(directory,arg0,arg1,arg2)
  elif operation==b"DUP":result=WATCHDOG_LIBC_V19.dup(arg0)
  elif operation==b"MEMFD":result=WATCHDOG_LIBC_V19.memfd_create(arg0,arg1)
  else:need(False)
  cell.c_value.value=result;saved=ctypes.get_errno()
 finally:
  if record is not None:lifecycle_capture_cell_v19(record,record.raw_cell)
 if result<0:
  need(record.state==b"CLOSED")
  raise OSError(saved,os.strerror(saved))
 return lifecycle_finish_adoption(context,slot)

def acquire_lifecycle_open(context,slot,kind,path,flags,mode=0o777,dir_fd=None,transferable=False,provenance=None):
 return lifecycle_scalar_boundary_v19(context,slot,kind,b"OPENAT",path,flags,mode,dir_fd,transferable,provenance)

def acquire_lifecycle_memfd(context,slot,kind,label,flags,transferable=False,provenance=None):
 return lifecycle_scalar_boundary_v19(context,slot,kind,b"MEMFD",label,flags,0,None,transferable,provenance)

def acquire_lifecycle_dup(context,slot,kind,source,transferable=False,provenance=None):
 return lifecycle_scalar_boundary_v19(context,slot,kind,b"DUP",source,0,0,None,transferable,provenance)

def bind_lifecycle_provenance(context,slot,provenance):
 record=context[b"fd_registry"][slot];need(watchdog_record_live_v19(record) and provenance is not None)
 lifecycle_bind_identity_v19(record);record.provenance=provenance;lifecycle_audit(context,slot);return provenance

def watchdog_wrapper_adopt_v19(context,slot):
 record=context[b"fd_registry"][slot];need(record.state==b"OWNED" and record.raw_fd>=0)
 record.endpoint_state=b"NO_WRAPPER";record.wrapper_phase=b"CONSTRUCTOR_ARMED"
 record.wrapper_local_fallback=record.raw_fd;record.wrapper_probe_done=False;record.wrapper_detach_attempted=False
 wrapper=socket.socket.__new__(socket.socket)
 record.wrapper_ref=wrapper;record.wrapper_phase=b"LOCAL_STRONG_REFERENCE"
 try:
  socket.socket.__init__(wrapper,fileno=record.raw_fd)
  record.wrapper_phase=b"ATTACH_CONFIRMED";record.endpoint_state=b"ATTACHED"
  need(wrapper.fileno()==record.raw_fd);return wrapper
 except BaseException:
  record.state=b"CLOSE_RETRY"
  try:watchdog_endpoint_repair_v19(record)
  except BaseException:pass
  if record.endpoint_state==b"DETACHED":
   try:close_lifecycle_fd(context,slot)
   except BaseException:pass
  raise

def bind_lifecycle_endpoint(context,slot,endpoint_key,endpoint):
 record=context[b"fd_registry"][slot]
 need(watchdog_record_live_v19(record) and LIFECYCLE_ENDPOINTS[slot]==endpoint_key)
 need(record.wrapper_ref is endpoint and record.endpoint_state==b"ATTACHED")
 need(endpoint.fileno()==record.raw_fd);context[endpoint_key]=endpoint;return endpoint

def promote_lifecycle_fd(context,old_slot,new_slot,new_kind,transferable=False,provenance=None):
 frame=context.get(b"v19_pending_receive_frame");source=context[b"fd_registry"][old_slot]
 if not watchdog_record_live_v19(source) and frame is not None:source=frame.record_for_expected(old_slot)
 spec=watchdog_role_spec_v19(new_slot)
 need(watchdog_record_live_v19(source) and spec[1]==new_kind and spec[2]==bool(transferable))
 need(source.semantic_role==old_slot)
 need(not any(record is not source and watchdog_record_live_v19(record) and record.semantic_role==new_slot for record in WATCHDOG_PHYSICAL_RECORDS_V19))
 frame_binding=None
 if frame is not None and frame.record_for_expected(old_slot,required=False) is source:
  frame_binding=(frame.site,frame.epoch,old_slot,source.record_id)
 prepared_provenance=provenance if provenance is not None else source.provenance
 need(prepared_provenance is not None)
 lifecycle_bind_identity_v19(source);need(lifecycle_live_number_owner(context,source.raw_fd,old_slot) in (None,old_slot))
 for record in WATCHDOG_PHYSICAL_RECORDS_V19:
  if record is not source and watchdog_record_live_v19(record):need(record.raw_fd!=source.raw_fd)
 source.provenance=(b"PROMOTED",prepared_provenance,frame_binding,source.epoch)
 source.semantic_role=new_slot
 source.state=b"OWNED"
 if frame_binding is not None:frame.mark_promoted(old_slot,source.record_id)
 return source.raw_fd

def register_lifecycle_poller(context,poller,slot,mask):
 record=context[b"fd_registry"][slot];need(watchdog_record_live_v19(record) and slot in PIDFD_LIFECYCLE_SLOTS)
 cell=None
 for candidate in WATCHDOG_POLLER_CELLS_V19:
  if candidate.state in (b"FREE",b"INACTIVE"):cell=candidate;break
 need(cell is not None);cell.epoch+=1
 cell.poller=poller;cell.record_id=record.record_id;cell.raw_fd=record.raw_fd;cell.mask=mask
 cell.state=b"REGISTERING"
 try:poller.register(record.raw_fd,mask)
 except BaseException:
  cell.state=b"UNREGISTER_RETRY"
  try:poller.unregister(record.raw_fd)
  except KeyError:pass
  except BaseException:raise OwnershipClosePending("poller-register-effect-unknown")
  cell.state=b"INACTIVE";cell.poller=None;cell.raw_fd=-1;cell.mask=0;raise
 cell.state=b"ACTIVE";return record.raw_fd

def unregister_lifecycle_pollers_record_v19(record):
 pending=False
 for cell in WATCHDOG_POLLER_CELLS_V19:
  if cell.record_id==record.record_id and cell.state in (b"REGISTERING",b"ACTIVE",b"UNREGISTER_RETRY"):
   cell.state=b"UNREGISTER_RETRY"
   try:cell.poller.unregister(record.raw_fd)
   except KeyError:pass
   except BaseException:pending=True;continue
   cell.state=b"INACTIVE";cell.poller=None;cell.raw_fd=-1;cell.mask=0
 if pending:raise OwnershipClosePending("poller-unregister-retry")

def unregister_lifecycle_pollers(context,slot,number):
 record=context[b"fd_registry"][slot];need(record.raw_fd==number)
 return unregister_lifecycle_pollers_record_v19(record)

def pidfd_ready_event(event):
 if event&select.POLLNVAL:raise FaultSet({b"PIDFD_BINDING"})
 return bool(event&(select.POLLIN|select.POLLHUP|select.POLLERR))

def watchdog_endpoint_repair_v19(record):
 wrapper=record.wrapper_ref
 if wrapper is None:
  if record.endpoint_state not in (b"NO_WRAPPER",b"DETACHED",b"PROVED_CLOSED"):record.endpoint_state=b"NO_WRAPPER"
  return
 record.endpoint_state=b"DETACH_REQUESTED"
 if not record.wrapper_probe_done:
  observed=wrapper.fileno();record.wrapper_probe_done=True
  if observed==-1:
   record.detached_raw_fd=record.raw_fd;record.endpoint_state=b"DETACHED"
   record.wrapper_phase=b"DETACH_CONFIRMED";record.wrapper_ref=None;return
  need(observed==record.raw_fd)
 if record.wrapper_detach_attempted:raise OwnershipClosePending("endpoint-detach-effect-unknown-no-repeat")
 record.wrapper_detach_attempted=True;record.wrapper_phase=b"DETACH_POSSIBLE"
 try:detached=wrapper.detach()
 except BaseException as error:raise OwnershipClosePending("endpoint-detach-effect-unknown-no-repeat") from error
 need(detached==record.raw_fd)
 record.detached_raw_fd=detached;record.endpoint_state=b"DETACHED"
 record.wrapper_phase=b"DETACH_CONFIRMED";record.wrapper_ref=None

def lifecycle_mark_closed_v19(context,record):
 number=record.raw_fd;slot=watchdog_registry_slot_v19(context,record)
 record.endpoint_state=b"PROVED_CLOSED";record.raw_cell.state=b"DISARMED"
 for frame in (WATCHDOG_MONITORED_FRAME_V19,WATCHDOG_EXTERNAL_CONTROL_FRAME_V19,WATCHDOG_EXTERNAL_RECEIPT_FRAME_V19,WATCHDOG_REFUSAL_FRAME_V19):
  for index in range(frame.installed_capacity):
   if frame.raw_cells[index].record_id==record.record_id:frame.raw_cells[index].state=b"DISARMED"
 watchdog_record_reset_v19(record)
 if context.get(slot)==number:context[slot]=-1
 endpoint_key=LIFECYCLE_ENDPOINTS.get(slot)
 if endpoint_key is not None:context[endpoint_key]=None
 lifecycle_audit(context,slot,record);return True

def close_lifecycle_record_v19(context,record):
 if record.state==b"CLOSED":return True
 need(record.raw_fd>=0);record.state=b"CLOSE_RETRY";number=record.raw_fd
 unregister_lifecycle_pollers_record_v19(record);watchdog_endpoint_repair_v19(record)
 if record.identity is not None:
  try:lifecycle_bind_identity_v19(record)
  except OSError as probe:
   if probe.errno==errno.EBADF:return lifecycle_mark_closed_v19(context,record)
   raise OwnershipClosePending("pre-close-revalidate") from probe
 try:os.close(number)
 except OSError:
  try:lifecycle_bind_identity_v19(record)
  except OSError as probe:
   if probe.errno==errno.EBADF:return lifecycle_mark_closed_v19(context,record)
   raise OwnershipClosePending("close-probe-unknown") from probe
  record.state=b"CLOSE_RETRY";raise OwnershipClosePending("close-live-retry")
 return lifecycle_mark_closed_v19(context,record)

def close_lifecycle_fd(context,slot):
 record=context[b"fd_registry"].get(slot)
 if record is None or record.state==b"CLOSED":
  frame=context.get(b"v19_pending_receive_frame")
  if frame is not None:
   pending=frame.record_for_expected(slot,required=False)
   if pending is not None and not frame.promoted[next(index for index in range(frame.installed_capacity) if frame.records[index] is pending)]:
    return close_lifecycle_record_v19(context,pending)
  return True
 return close_lifecycle_record_v19(context,record)

def close_lifecycle_slots(context,slots):
 first=None
 for slot in slots:
  try:close_lifecycle_fd(context,slot)
  except BaseException as error:
   if first is None:first=error
 frame=context.get(b"v19_pending_receive_frame")
 touches=False
 if frame is not None:
  for slot in slots:
   if frame.record_for_expected(slot,required=False) is not None:touches=True
  if touches and not frame.validation_complete:
   for index in range(frame.installed_capacity):
    record=frame.records[index]
    if record is not None and watchdog_record_live_v19(record):
     try:close_lifecycle_record_v19(context,record)
     except BaseException as error:
      record.state=b"CLOSE_RETRY"
      if first is None:first=error
  if frame.all_expected_resolved():context[b"v19_pending_receive_frame"]=None
 if first is not None:raise first
 return True

V15_WATCHDOG_MINIMAL_CONTEXT_V19=minimal_context
def minimal_context():
 context=V15_WATCHDOG_MINIMAL_CONTEXT_V19()
 context[b"physical_records_v19"]=WATCHDOG_PHYSICAL_RECORDS_V19
 context[b"v19_pending_receive_frame"]=None
 context[b"v19_offer_boundary_index"]=0
 context[b"v19_refusal_boundary_index"]=0
 context[b"v19_installed_history_epoch"]=0
 return context

def acquire_control(context,actor_pid):
 control=watchdog_wrapper_adopt_v19(context,b"actor_control_fd")
 bind_lifecycle_endpoint(context,b"actor_control_fd",b"actor_control",control)
 try:
  need(control.getsockopt(socket.SOL_SOCKET,socket.SO_TYPE)==socket.SOCK_SEQPACKET)
  fd_access(context[b"actor_control_fd"],os.O_RDWR)
  need(fcntl.fcntl(context[b"actor_control_fd"],fcntl.F_GETFL)&os.O_NONBLOCK)
  peer=struct.unpack("3i",control.getsockopt(socket.SOL_SOCKET,socket.SO_PEERCRED,12))
  need(peer==(actor_pid,0,0));return control
 except BaseException:close_lifecycle_fd(context,b"actor_control_fd");raise

def acquire_external_owner(context):
 pid=udec(CERT[b"EXTERNAL_OWNER_PID"],2);start=udec(CERT[b"EXTERNAL_OWNER_STARTTIME"],1)
 fd_access(context[b"transfer_control_fd"],os.O_RDWR)
 fd_access(context[b"external_owner_pidfd_fd"],os.O_RDWR)
 need(pidfd_pid(context[b"external_owner_pidfd_fd"])==pid)
 watcher=select.poll();register_lifecycle_poller(context,watcher,b"external_owner_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 need(watcher.poll(0)==[])
 external=watchdog_wrapper_adopt_v19(context,b"transfer_control_fd")
 bind_lifecycle_endpoint(context,b"transfer_control_fd",b"transfer_control",external)
 try:
  need(external.getsockopt(socket.SOL_SOCKET,socket.SO_TYPE)==socket.SOCK_SEQPACKET)
  need(fcntl.fcntl(context[b"transfer_control_fd"],fcntl.F_GETFL)&os.O_NONBLOCK)
  peer=struct.unpack("3i",external.getsockopt(socket.SOL_SOCKET,socket.SO_PEERCRED,12))
  need(peer==(pid,udec(CERT[b"EXTERNAL_OWNER_UID"]),udec(CERT[b"EXTERNAL_OWNER_GID"])))
  need(proc_starttime(pid)==start and pidfd_pid(context[b"external_owner_pidfd_fd"])==pid)
  need(proc_starttime(pid)==start and watcher.poll(0)==[]);return external
 except BaseException:close_lifecycle_fd(context,b"transfer_control_fd");raise

class WatchIovecV19(ctypes.Structure):
 _fields_=(("iov_base",ctypes.c_void_p),("iov_len",ctypes.c_size_t))

class WatchMsghdrV19(ctypes.Structure):
 _fields_=(
  ("msg_name",ctypes.c_void_p),("msg_namelen",ctypes.c_uint),
  ("msg_iov",ctypes.POINTER(WatchIovecV19)),("msg_iovlen",ctypes.c_size_t),
  ("msg_control",ctypes.c_void_p),("msg_controllen",ctypes.c_size_t),
  ("msg_flags",ctypes.c_int),
 )

class WatchCmsghdrV19(ctypes.Structure):
 _fields_=(("cmsg_len",ctypes.c_size_t),("cmsg_level",ctypes.c_int),("cmsg_type",ctypes.c_int))

def watch_cmsg_align_v19(value):
 alignment=ctypes.sizeof(ctypes.c_size_t)
 return (value+alignment-1)&~(alignment-1)

class WatchReceiveFrameV19:
 __slots__=(
  "site","semantic_capacity","installed_capacity","ancillary_bytes","kernel_control_bytes",
  "payload","control","iov","hdr","header_views","int_views","raw_cells",
  "records","expected_slots","promoted","provenances","installed_count","payload_count",
  "msg_flags","capture_complete","validation_complete","capture_fault","cleanup_cursor","cleanup_pending","original_fault","immediate_checkpoint_done","epoch",
 )
 def __init__(self,site,semantic_capacity,installed_capacity):
  self.site=site;self.semantic_capacity=semantic_capacity
  self.installed_capacity=installed_capacity
  self.ancillary_bytes=installed_capacity*socket.CMSG_SPACE(ctypes.sizeof(ctypes.c_int))
  self.kernel_control_bytes=installed_capacity*socket.CMSG_SPACE(ctypes.sizeof(ctypes.c_int))
  self.payload=(ctypes.c_ubyte*65536)()
  self.control=(ctypes.c_ubyte*self.ancillary_bytes)()
  self.iov=WatchIovecV19(ctypes.addressof(self.payload),65536)
  self.hdr=WatchMsghdrV19();self.hdr.msg_name=None;self.hdr.msg_namelen=0
  self.hdr.msg_iov=ctypes.pointer(self.iov);self.hdr.msg_iovlen=1
  self.hdr.msg_control=ctypes.addressof(self.control)
  self.hdr.msg_controllen=self.kernel_control_bytes;self.hdr.msg_flags=0
  step=ctypes.sizeof(ctypes.c_size_t)
  self.header_views=tuple(WatchCmsghdrV19.from_buffer(self.control,offset) for offset in range(0,self.ancillary_bytes-ctypes.sizeof(WatchCmsghdrV19)+1,step))
  self.int_views=tuple(ctypes.c_int.from_buffer(self.control,offset) for offset in range(0,self.ancillary_bytes-ctypes.sizeof(ctypes.c_int)+1))
  self.raw_cells=tuple(WatchRawCellV19(site+b"_raw_"+str(index).encode()) for index in range(installed_capacity))
  self.records=[None]*installed_capacity;self.expected_slots=[None]*installed_capacity
  self.promoted=[False]*installed_capacity
  self.provenances=tuple((b"RECVMSG",site,index) for index in range(installed_capacity))
  self.installed_count=0
  self.payload_count=0;self.msg_flags=0;self.capture_complete=False
  self.validation_complete=False;self.capture_fault=b"NONE"
  self.cleanup_cursor=0;self.cleanup_pending=False;self.original_fault=None
  self.immediate_checkpoint_done=False;self.epoch=0
 def record_for_expected(self,slot,required=True):
  found=None
  for index in range(self.installed_capacity):
   if self.expected_slots[index]==slot:
    need(found is None);found=self.records[index]
  if required:need(found is not None)
  return found
 def mark_promoted(self,slot,record_id):
  for index in range(self.installed_capacity):
   if self.expected_slots[index]==slot:
    need(self.records[index].record_id==record_id);self.promoted[index]=True
    complete=True
    for cursor in range(self.installed_capacity):
     if self.expected_slots[cursor] is not None and not self.promoted[cursor]:complete=False
    if complete:self.validation_complete=True
    return
  need(False)
 def all_expected_resolved(self):
  for index in range(self.installed_capacity):
   if self.expected_slots[index] is not None and not self.promoted[index]:
    record=self.records[index]
    if record is not None and watchdog_record_live_v19(record):return False
  return True

WATCHDOG_MONITORED_FRAME_V19=WatchReceiveFrameV19(b"WATCHDOG_MONITORED",4,5)
WATCHDOG_EXTERNAL_CONTROL_FRAME_V19=WatchReceiveFrameV19(b"EXTERNAL_CONTROL",13,14)
WATCHDOG_EXTERNAL_RECEIPT_FRAME_V19=WatchReceiveFrameV19(b"EXTERNAL_RECEIPT",13,14)
WATCHDOG_REFUSAL_FRAME_V19=WatchReceiveFrameV19(b"REFUSAL_CONTROL",4,5)
WATCHDOG_RECEIVE_CLEANUP_WAIT_V19=select.poll()
WATCHDOG_ALL_RAW_CELLS_V19=(
 WATCHDOG_RECORD_RAW_CELLS_V19+WATCHDOG_MONITORED_FRAME_V19.raw_cells+
 WATCHDOG_EXTERNAL_CONTROL_FRAME_V19.raw_cells+WATCHDOG_EXTERNAL_RECEIPT_FRAME_V19.raw_cells+
 WATCHDOG_REFUSAL_FRAME_V19.raw_cells
)
WATCHDOG_MONITORED_QUARANTINE_SLOTS_V19=tuple(b"unexpected_control_right_"+str(index).encode() for index in range(4))+(b"cap_status_fd",)
WATCHDOG_EXTERNAL_CONTROL_QUARANTINE_SLOTS_V19=tuple(b"external_unexpected_right_"+str(index).encode() for index in range(13))+(b"mount_graph_fd",)
WATCHDOG_EXTERNAL_RECEIPT_QUARANTINE_SLOTS_V19=tuple(b"external_receipt_carrier_"+str(index).encode() for index in range(13))+(b"boot_id_fd",)
WATCHDOG_REFUSAL_QUARANTINE_SLOTS_V19=tuple(b"refusal_unexpected_right_"+str(index).encode() for index in range(4))+(b"refusal_runtime_root_fd",)

def watch_receive_prearm_v19(context,frame,received_slots,quarantine_slots):
 need(context.get(b"v19_pending_receive_frame") is None)
 need(frame.cleanup_cursor==0 and not frame.cleanup_pending)
 need(len(received_slots)<=frame.semantic_capacity and len(quarantine_slots)==frame.installed_capacity)
 frame.epoch+=1;frame.installed_count=0;frame.payload_count=0
 frame.msg_flags=0;frame.capture_complete=False;frame.validation_complete=False
 frame.capture_fault=b"NONE";frame.original_fault=None;frame.immediate_checkpoint_done=False
 frame.hdr.msg_controllen=frame.kernel_control_bytes;frame.hdr.msg_flags=0
 ctypes.memset(ctypes.addressof(frame.control),0,frame.ancillary_bytes)
 for index in range(frame.installed_capacity):
  if index<len(received_slots):slot=received_slots[index][0];expected=slot
  else:slot=quarantine_slots[index-len(received_slots)];expected=None
  record=context[b"fd_registry"][slot];need(record.state==b"CLOSED")
  watchdog_record_reset_v19(record);record.epoch+=1
  record.semantic_role=slot;record.state=b"ACQUIRING";record.raw_fd=-1
  record.identity=None;record.physical_identity=None;record.leaf_identity=None
  record.verified_kill_leaf_identity=None;record.access=b"UNKNOWN";record.provenance=frame.provenances[index]
  record.endpoint_state=b"NO_WRAPPER";record.wrapper_ref=None
  frame.records[index]=record;frame.expected_slots[index]=expected;frame.promoted[index]=False
  cell=frame.raw_cells[index];cell.state=b"EMPTY";cell.c_value.value=-1
  cell.record_id=record.record_id;cell.epoch=record.epoch

def watch_receive_capture_one_v19(frame,index,number):
 if index>=frame.installed_capacity:
  frame.capture_fault=b"RIGHTS_OVERFLOW";return
 record=frame.records[index];cell=frame.raw_cells[index];cell.c_value.value=number
 if number<0:
  frame.capture_fault=b"NEGATIVE_INSTALLED_RIGHT";return
 if record.raw_fd<0:record.raw_fd=number;record.state=b"ACQUIRING";cell.state=b"SHADOW_OF_RECORD"
 elif record.raw_fd!=number:frame.capture_fault=b"CAPTURE_IDENTITY_CONFLICT"
 if number>255:record.state=b"CLOSE_RETRY";frame.capture_fault=b"FD_ABOVE_CACHED_BOUND"
 if index+1>frame.installed_count:frame.installed_count=index+1

def watch_receive_scan_v19(frame,count):
 frame.payload_count=count;frame.msg_flags=frame.hdr.msg_flags
 offset=0;visible=0;limit=min(frame.hdr.msg_controllen,frame.ancillary_bytes)
 while offset+ctypes.sizeof(WatchCmsghdrV19)<=limit:
  header=frame.header_views[offset//ctypes.sizeof(ctypes.c_size_t)]
  length=header.cmsg_len
  if length<ctypes.sizeof(WatchCmsghdrV19) or offset+length>limit:
   frame.capture_fault=b"MALFORMED_CMSG";offset+=ctypes.sizeof(ctypes.c_size_t);continue
  data_offset=offset+watch_cmsg_align_v19(ctypes.sizeof(WatchCmsghdrV19))
  if header.cmsg_level==socket.SOL_SOCKET and header.cmsg_type==socket.SCM_RIGHTS:
   data_bytes=length-watch_cmsg_align_v19(ctypes.sizeof(WatchCmsghdrV19))
   if data_bytes%ctypes.sizeof(ctypes.c_int):frame.capture_fault=b"MALFORMED_RIGHTS"
   rights=data_bytes//ctypes.sizeof(ctypes.c_int)
   for item in range(rights):
    position=data_offset+item*ctypes.sizeof(ctypes.c_int)
    if visible<frame.installed_capacity:
     watch_receive_capture_one_v19(frame,visible,frame.int_views[position].value)
    else:frame.capture_fault=b"RIGHTS_OVERFLOW"
    visible+=1
  else:frame.capture_fault=b"UNEXPECTED_CMSG"
  offset+=max(ctypes.sizeof(ctypes.c_size_t),watch_cmsg_align_v19(length))
 for index in range(frame.installed_capacity):
  record=frame.records[index]
  if record.state==b"ACQUIRING" and record.raw_fd<0:
   watchdog_record_reset_v19(record);frame.raw_cells[index].state=b"DISARMED"
 frame.capture_complete=True

def watch_receive_rescan_v19(frame):
 watch_receive_scan_v19(frame,frame.payload_count)
 for index in range(frame.installed_capacity):
  record=frame.records[index];cell=frame.raw_cells[index]
  if record is not None and record.state==b"ACQUIRING":
   lifecycle_capture_cell_v19(record,cell)

def watch_receive_cleanup_v19(context,frame):
 while True:
  frame.cleanup_pending=False
  while frame.cleanup_cursor<frame.installed_capacity:
   index=frame.cleanup_cursor;record=frame.records[index]
   if record is not None and watchdog_record_live_v19(record) and not frame.promoted[index]:
    try:close_lifecycle_record_v19(context,record)
    except BaseException:record.state=b"CLOSE_RETRY";frame.cleanup_pending=True
   if record is not None and record.state==b"CLOSED":
    frame.raw_cells[index].state=b"EMPTY";frame.raw_cells[index].c_value.value=-1
   frame.cleanup_cursor+=1
  if not frame.cleanup_pending:
   frame.cleanup_cursor=0;return True
  frame.cleanup_cursor=0
  try:WATCHDOG_RECEIVE_CLEANUP_WAIT_V19.poll(10)
  except BaseException:pass

def watch_recvmsg_primitive_v19(control,context,frame,received_slots,quarantine_slots):
 result=-1;failure=None
 try:
  try:
   watch_receive_prearm_v19(context,frame,received_slots,quarantine_slots)
   result=WATCHDOG_LIBC_V19.recvmsg(control.fileno(),ctypes.byref(frame.hdr),WATCHDOG_MSG_CMSG_CLOEXEC_V19)
   watch_receive_scan_v19(frame,result)
  except BaseException as error:failure=error
 finally:
  try:watch_receive_rescan_v19(frame)
  except BaseException as error:
   if failure is None:failure=error
 if result<0 and failure is None:
  saved=ctypes.get_errno()
  failure=BlockingIOError(saved,os.strerror(saved)) if saved in (errno.EAGAIN,errno.EWOULDBLOCK) else OSError(saved,os.strerror(saved))
 if failure is not None:
  frame.original_fault=failure;watch_receive_cleanup_v19(context,frame)
  raise failure
 return frame

def watchdog_monitored_recvmsg_site_v19(control,context,received_slots):
 return watch_recvmsg_primitive_v19(control,context,WATCHDOG_MONITORED_FRAME_V19,received_slots,WATCHDOG_MONITORED_QUARANTINE_SLOTS_V19)

def external_control_recvmsg_site_v19(control,context):
 return watch_recvmsg_primitive_v19(control,context,WATCHDOG_EXTERNAL_CONTROL_FRAME_V19,(),WATCHDOG_EXTERNAL_CONTROL_QUARANTINE_SLOTS_V19)

def external_receipt_recvmsg_site_v19(control,context):
 return watch_recvmsg_primitive_v19(control,context,WATCHDOG_EXTERNAL_RECEIPT_FRAME_V19,(),WATCHDOG_EXTERNAL_RECEIPT_QUARANTINE_SLOTS_V19)

def refusal_recvmsg_site_v19(control,context):
 return watch_recvmsg_primitive_v19(control,context,WATCHDOG_REFUSAL_FRAME_V19,(),WATCHDOG_REFUSAL_QUARANTINE_SLOTS_V19)

def watch_poll_outer_readiness_v19(context,events):
 outer=context.get(b"outer_pidfd",-1)
 if outer<0:return False
 ready=False
 for number,event in events:
  if number==outer and pidfd_ready_event(event):ready=True
 if ready:
  context[b"pidfd_exit_ready_observed"]=True
  if context.get(b"outer_pidfd_offer_state") in (b"PRE_READY_OFFER_FROZEN",b"POST_OFFER_READY_RETAINED"):
   context[b"outer_pidfd_offer_state"]=b"POST_OFFER_READY_RETAINED"
 return ready

def recv_monitored(control,context,actor_pidfd,deadline,rights,actual_pre_state,ordinal,probe,received_slots=()):
 receiver_binding(actual_pre_state,ordinal,probe,deadline)
 need(type(received_slots)is tuple and len(received_slots)==rights)
 need(rights<=4 and actor_pidfd==context[b"actor_pidfd_fd"])
 checkpoint(CERT,0,deadline)
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 register_lifecycle_poller(context,poller,b"actor_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 outer=context.get(b"outer_pidfd",-1)
 if outer>=0:register_lifecycle_poller(context,poller,b"outer_pidfd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 while True:
  checkpoint(CERT,0,deadline);remaining=deadline-time.monotonic_ns()
  if remaining<=0:raise FaultSet({b"CONTROL_TIMEOUT"})
  try:events=poller.poll(max(1,min(50,(remaining+999999)//1000000)))
  except InterruptedError:continue
  cmask=amask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   elif number==actor_pidfd:amask|=event
  watch_poll_outer_readiness_v19(context,events)
  if cmask&select.POLLNVAL:raise ControlLost("control-nval")
  if cmask&select.POLLIN:
   frame=None;keep=False
   try:
    frame=watchdog_monitored_recvmsg_site_v19(control,context,received_slots)
    raw=bytes(frame.payload[:frame.payload_count])
    checkpoint(CERT,0,deadline)
    if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})
    if frame.msg_flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC):raise FaultSet({b"CONTROL_TRUNCATION"})
    if frame.capture_fault!=b"NONE" or not raw:raise FaultSet({b"CONTROL_MALFORMED"})
    if raw.startswith(b"V15_ABORT|"):
     binding=received_binding(raw,actual_pre_state,ordinal,probe,b"control_deadline_ns",deadline)
     values,faults=parse_abort(raw,b"A",binding)
     if frame.installed_count:faults.add(b"FD_TRANSFER")
     error=RemoteAbort(faults);error.values=values;raise error
    need(frame.installed_count==rights)
    installed=tuple(frame.records[index].raw_fd for index in range(rights))
    if rights:
     context[b"v19_pending_receive_frame"]=frame;keep=True
    else:frame.validation_complete=True
    return raw,installed
   except BlockingIOError:
    if frame is not None:watch_receive_cleanup_v19(context,frame)
    continue
   finally:
    if frame is not None and not keep:watch_receive_cleanup_v19(context,frame)
  if pidfd_ready_event(amask):raise PidfdActorLost("pidfd-ready")
  if cmask&(select.POLLHUP|select.POLLERR):raise ControlLost("control-hup")

def external_recv(control,context,kind,keys,expected_sequence,deadline):
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 register_lifecycle_poller(context,poller,b"external_owner_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 if context.get(b"outer_pidfd",-1)>=0:register_lifecycle_poller(context,poller,b"outer_pidfd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 while True:
  checkpoint(CERT,0,deadline);now=time.monotonic_ns();need(now<=deadline)
  try:events=poller.poll(max(1,min(50,(deadline-now+999999)//1000000)))
  except InterruptedError:continue
  cmask=omask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   elif number==15:omask|=event
  watch_poll_outer_readiness_v19(context,events)
  if pidfd_ready_event(omask):
   context[b"external_owner_pidfd_exit_ready_observed"]=True
   raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})
  if cmask&select.POLLNVAL:raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})
  if cmask&select.POLLIN:
   frame=None
   try:
    frame=external_control_recvmsg_site_v19(control,context)
    raw=bytes(frame.payload[:frame.payload_count])
    need(frame.capture_fault==b"NONE" and frame.installed_count==0)
    need(not frame.msg_flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC) and raw)
    frame.validation_complete=True;return parse_external(raw,kind,keys,expected_sequence,deadline)
   finally:
    if frame is not None:watch_receive_cleanup_v19(context,frame)
  if cmask&(select.POLLHUP|select.POLLERR):raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})

def external_recv_receipt(control,context,kind,keys,expected_sequence,deadline):
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 register_lifecycle_poller(context,poller,b"external_owner_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 if context.get(b"outer_pidfd",-1)>=0:register_lifecycle_poller(context,poller,b"outer_pidfd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 while True:
  checkpoint(CERT,0,deadline);now=time.monotonic_ns();need(now<=deadline)
  try:events=poller.poll(max(1,min(50,(deadline-now+999999)//1000000)))
  except InterruptedError:continue
  cmask=omask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   elif number==15:omask|=event
  watch_poll_outer_readiness_v19(context,events)
  if pidfd_ready_event(omask):
   context[b"external_owner_pidfd_exit_ready_observed"]=True
   raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})
  if cmask&select.POLLNVAL:raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})
  if cmask&select.POLLIN:
   frame=None
   try:
    frame=external_receipt_recvmsg_site_v19(control,context)
    checkpoint(CERT,0,deadline);need(time.monotonic_ns()<=deadline)
    frame.immediate_checkpoint_done=True
    raw=bytes(frame.payload[:frame.payload_count])
    need(frame.capture_fault==b"NONE" and frame.installed_count==1)
    need(not frame.msg_flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC) and raw)
    carrier=frame.records[0];need(carrier.state==b"ACQUIRING" and carrier.provenance[0]==b"RECVMSG")
    receipt_raw=sealed_carrier(carrier.raw_fd,65536)
    v19_record_installed_history(context,frame)
    values=parse_external(raw,kind,keys,expected_sequence,deadline)
    checkpoint(CERT,0,deadline);need(time.monotonic_ns()<=deadline)
    frame.validation_complete=True;return values,receipt_raw
   finally:
    if frame is not None:watch_receive_cleanup_v19(context,frame)
  if cmask&(select.POLLHUP|select.POLLERR):raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})

def receive_refusal_candidate_once(control,context):
 raw=b"";frame=None;finality_deadline=refusal_slot(context)[1][6]
 try:
  try:
   frame=refusal_recvmsg_site_v19(control,context)
   raw=bytes(frame.payload[:frame.payload_count])
  except BlockingIOError:return b"NO_DATA"
  except BaseException:
   refusal_candidate_fault(context,raw,b"TRANSPORT_REJECTED");return b"REJECTED"
  if raw==b"" and frame.capture_fault==b"NONE" and frame.installed_count==0 and not frame.msg_flags:
   context[b"refusal_control_eof"]=True;return b"EOF"
  try:checkpoint(CERT,0,finality_deadline);need(time.monotonic_ns()<=finality_deadline)
  except BaseException:
   refusal_candidate_fault(context,raw,b"POST_FINALITY_NONAUTHORITATIVE");return b"LATE_NONAUTHORITATIVE"
  if not raw or frame.capture_fault!=b"NONE" or frame.installed_count or frame.msg_flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC):
   refusal_candidate_fault(context,raw,b"TRANSPORT_REJECTED");return b"REJECTED"
  if context[b"refusal_finality_state"]!=b"OPEN":
   refusal_candidate_fault(context,raw,b"POST_FINAL_REPLAY");return b"REJECTED"
  try:receipt,sequence=parse_refusal_receipt_candidate(context,raw)
  except BaseException:refusal_candidate_fault(context,raw,b"SEMANTIC_REJECTED");return b"REJECTED"
  frame.validation_complete=True;commit_refusal_receipt(context,raw,sequence);return b"VERIFIED"
 finally:
  if frame is not None:watch_receive_cleanup_v19(context,frame)

class StreamCellV19:
 __slots__=("role","buffer","cap","used","scratch","overflow","eof","epoch")
 def __init__(self,role):
  self.role=role;self.buffer=bytearray(STREAM_CAP);self.cap=STREAM_CAP
  self.used=0;self.scratch=b"";self.overflow=False;self.eof=False;self.epoch=0
 def reset(self):
  self.used=0;self.scratch=b"";self.overflow=False;self.eof=False;self.epoch+=1

WATCHDOG_OUT_STREAM_V19=StreamCellV19(b"OUT_FD")
WATCHDOG_ERR_STREAM_V19=StreamCellV19(b"ERR_FD")

def stream_cell_for_number_v19(number):
 context=ACTIVE_LIFECYCLE_CONTEXT;need(context is not None)
 slot=lifecycle_live_number_owner(context,number)
 need(slot in (b"out_fd",b"err_fd"))
 return WATCHDOG_OUT_STREAM_V19 if slot==b"out_fd" else WATCHDOG_ERR_STREAM_V19

def drain(number,target):
 cell=stream_cell_for_number_v19(number)
 while True:
  try:chunk=os.read(number,65536)
  except BlockingIOError:return cell.overflow,cell.eof
  except InterruptedError:continue
  except BaseException as error:raise FaultSet({b"CAPTURE_IO"}) from error
  if chunk==b"":
   cell.eof=True;return cell.overflow,cell.eof
  cell.scratch=chunk;room=cell.cap-cell.used
  if len(chunk)>room:cell.overflow=True
  copied=min(room,len(chunk))
  if copied>0:
   cell.buffer[cell.used:cell.used+copied]=chunk[:copied]
   cell.used+=copied;target.extend(chunk[:copied])

class FixedIdVectorV19:
 __slots__=("capacity","values","count","epoch")
 def __init__(self,capacity):
  self.capacity=capacity;self.values=(ctypes.c_int*capacity)(*([-1]*capacity))
  self.count=0;self.epoch=0
 def reset(self,epoch):
  self.count=0;self.epoch=epoch
  for index in range(self.capacity):self.values[index]=-1
 def add(self,record_id):
  need(self.count<self.capacity)
  for index in range(self.count):need(self.values[index]!=record_id)
  self.values[self.count]=record_id;self.count+=1
 def contains(self,record_id):
  for index in range(self.count):
   if self.values[index]==record_id:return True
  return False
 def exact_tuple(self):
  return tuple(self.values[index] for index in range(self.count))

class CensusV19:
 __slots__=("epoch","phase","mode","full_live","offered","safe_local","blocking","kill","raw","digest")
 def __init__(self):
  self.epoch=0;self.phase=b"EMPTY";self.mode=b"UNBOUND";self.full_live=FixedIdVectorV19(97)
  self.offered=FixedIdVectorV19(13);self.safe_local=FixedIdVectorV19(97)
  self.blocking=FixedIdVectorV19(97);self.kill=FixedIdVectorV19(97)
  self.raw=FixedIdVectorV19(135);self.digest=EMPTY_SHA
 def reset(self,epoch,phase,mode):
  self.epoch=epoch;self.phase=phase;self.mode=mode
  self.full_live.reset(epoch);self.offered.reset(epoch);self.safe_local.reset(epoch)
  self.blocking.reset(epoch);self.kill.reset(epoch);self.raw.reset(epoch);self.digest=EMPTY_SHA

class OfferCacheV19:
 __slots__=(
  "kind","state","epoch","boundary","storage","length","offer_sha",
  "frozen_full","frozen_offered","frozen_safe","frozen_kill","frozen_raw",
  "frozen_census_sha","capability_sha","identity_sha","outer_record_id",
  "outer_state","mode","frozen_wire_rows","wire_sha","possible_send","sent_once","atomic_authority","prepared_sequence",
 )
 def __init__(self,kind):
  self.kind=kind;self.state=b"EMPTY";self.epoch=0;self.boundary=0
  self.storage=bytearray(65536);self.length=0;self.offer_sha=EMPTY_SHA
  self.frozen_full=FixedIdVectorV19(97);self.frozen_offered=FixedIdVectorV19(13)
  self.frozen_safe=FixedIdVectorV19(97);self.frozen_kill=FixedIdVectorV19(97)
  self.frozen_raw=FixedIdVectorV19(135);self.frozen_census_sha=EMPTY_SHA
  self.capability_sha=EMPTY_SHA;self.identity_sha=EMPTY_SHA
  self.outer_record_id=-1;self.outer_state=b"NOT_BOUND"
  self.mode=b"ZERO_RIGHTS" if kind==b"REFUSAL" else b"GENERIC_13"
  self.frozen_wire_rows=();self.wire_sha=EMPTY_SHA
  self.possible_send=False;self.sent_once=False;self.atomic_authority=None;self.prepared_sequence=0
 def store_offer(self,raw,sequence):
  need(self.state==b"CENSUS_PREPARED" and self.atomic_authority is None)
  need(type(raw)is bytes and 0<len(raw)<=len(self.storage))
  digest=sha(raw);self.storage[:len(raw)]=raw
  candidate=(b"FROZEN",raw,digest,self.epoch,sequence,1,
   self.frozen_full.exact_tuple(),self.frozen_offered.exact_tuple(),
   self.frozen_safe.exact_tuple(),self.frozen_kill.exact_tuple(),
   self.frozen_raw.exact_tuple(),self.frozen_census_sha,
   self.capability_sha,self.identity_sha,self.outer_record_id,self.outer_state,
   self.mode,self.frozen_wire_rows,self.wire_sha)
  self.atomic_authority=candidate;self.restore_authority()
 def restore_authority(self):
  authority=self.atomic_authority;need(authority is not None and authority[0]==b"FROZEN" and len(authority)==19)
  self.length=len(authority[1]);self.offer_sha=authority[2];self.epoch=authority[3]
  self.prepared_sequence=authority[4];self.boundary=authority[5];self.state=authority[0]
  self.frozen_census_sha=authority[11];self.capability_sha=authority[12]
  self.identity_sha=authority[13];self.outer_record_id=authority[14];self.outer_state=authority[15]
  self.mode=authority[16];self.frozen_wire_rows=authority[17];self.wire_sha=authority[18]
 def raw(self):
  need(self.atomic_authority is not None and self.atomic_authority[0]==b"FROZEN")
  return self.atomic_authority[1]
 def discard_unactivated(self):
  need(not self.possible_send and not self.sent_once)
  self.state=b"EMPTY";self.boundary=0;self.length=0;self.offer_sha=EMPTY_SHA
  self.frozen_census_sha=EMPTY_SHA;self.capability_sha=EMPTY_SHA
  self.identity_sha=EMPTY_SHA;self.outer_record_id=-1;self.outer_state=b"NOT_BOUND"
  self.frozen_wire_rows=();self.wire_sha=EMPTY_SHA
  self.atomic_authority=None;self.prepared_sequence=0

class AcceptanceCommitV19:
 __slots__=(
  "state","mode","offer_sha","record_seq","predecessor","receipt_sha",
  "frozen_census_sha","current_census_sha","installed_history",
  "current_retained","kill_census","outer_record_id","outer_disposition",
  "no_replay","commit_epoch","candidate","authority",
 )
 def __init__(self):
  self.state=b"EMPTY";self.mode=b"DIRECT";self.offer_sha=EMPTY_SHA
  self.record_seq=0;self.predecessor=EMPTY_SHA;self.receipt_sha=EMPTY_SHA
  self.frozen_census_sha=EMPTY_SHA;self.current_census_sha=EMPTY_SHA
  self.installed_history=FixedIdVectorV19(97)
  self.current_retained=FixedIdVectorV19(97);self.kill_census=FixedIdVectorV19(97)
  self.outer_record_id=-1;self.outer_disposition=b"NOT_BOUND"
  self.no_replay=False;self.commit_epoch=0;self.candidate=None;self.authority=None

class ClosureCellV19:
 __slots__=(
  "phase","mode","plan","plan_count","cursor","current_record_id",
  "retry_ms","timing_overrun","commit_state","commit_offer_sha","epoch",
  "acceptance_authority","preclose_done","preclose_state","preclose_packet","preclose_packet_sha",
  "preclose_sequence","preclose_deadline","preclose_send_latch","retained_fault","release_handoff",
 )
 def __init__(self):
  self.phase=b"NOT_STARTED";self.mode=b"DIRECT"
  self.plan=(ctypes.c_int*97)(*([-1]*97));self.plan_count=0
  self.cursor=0;self.current_record_id=-1;self.retry_ms=10
  self.timing_overrun=False;self.commit_state=b"EMPTY"
  self.commit_offer_sha=EMPTY_SHA;self.epoch=0;self.acceptance_authority=None
  self.preclose_done=False;self.preclose_state=b"NOT_ATTEMPTED"
  self.preclose_packet=b"";self.preclose_packet_sha=EMPTY_SHA
  self.preclose_sequence=0;self.preclose_deadline=0;self.preclose_send_latch=False
  self.retained_fault=False;self.release_handoff=b"NONE"

WATCHDOG_GENERIC_CENSUS_V19=CensusV19()
WATCHDOG_REFUSAL_CENSUS_V19=CensusV19()
WATCHDOG_GENERIC_OFFER_CACHE_V19=OfferCacheV19(b"GENERIC")
WATCHDOG_REFUSAL_OFFER_CACHE_V19=OfferCacheV19(b"REFUSAL")
WATCHDOG_ACCEPTANCE_COMMIT_V19=AcceptanceCommitV19()
WATCHDOG_ACCEPTANCE_AUTHORITY_V19=None
WATCHDOG_CLOSURE_CELL_V19=ClosureCellV19()
WATCHDOG_CLOSURE_WAIT_V19=select.poll()
WATCHDOG_LAST_INSTALLED_HISTORY_V19=FixedIdVectorV19(97)
WATCHDOG_CENSUS_SEEN_V19=FixedIdVectorV19(97)

V19_RECEIVER_PROOF_KEYS=(
 b"RECEIVER_INSTALLED_HISTORY",b"RECEIVER_INSTALLED_HISTORY_SHA256",
 b"RECEIVER_CURRENT_RETAINED_SET",b"RECEIVER_CURRENT_RETAINED_SET_SHA256",
 b"RECEIVER_KILL_CENSUS",b"RECEIVER_KILL_CENSUS_SHA256",
 b"RECEIVER_OUTER_DISPOSITION",b"RECEIVER_OUTER_DISPOSITION_SHA256",
)
EXTERNAL_RECEIPT_KEYS=EXTERNAL_RECEIPT_KEYS+V19_RECEIVER_PROOF_KEYS
V19_RECEIVER_PROOF_DOMAIN=b"P27E001_V15_RECEIVER_INSTALLATION_PROOF\x00"
V19_WIRE_ROW_DOMAIN=b"P27E001_V19_CANONICAL_EXTERNAL_WIRE_ROW\x00"
V19_WIRE_ROLE_SPEC=tuple(
 (index,slot,LIFECYCLE_SLOT_SPEC_MAP[slot][0])
 for index,slot in enumerate(WATCHDOG_OFFERED_SLOTS_V19)
)

def v19_wire_row_v19(index,slot,kind,number,identity):
 need(type(index)is int and 0<=index<13 and V19_WIRE_ROLE_SPEC[index]==(index,slot,kind))
 need(type(identity)is bytes and identity and type(number)is int and number>=0)
 access=fcntl.fcntl(number,fcntl.F_GETFL)&os.O_ACCMODE
 core=(b"I="+str(index).encode()+b".R="+slot+b".K="+kind+b".H="+sha(identity)+b".A="+str(access).encode())
 return core+b".D="+sha(V19_WIRE_ROW_DOMAIN+core)

def v19_parse_wire_row_v19(row):
 need(type(row)is bytes and row and row.count(b".")==5)
 fields=row.split(b".");need(len(fields)==6)
 need(fields[0].startswith(b"I=") and fields[1].startswith(b"R=") and fields[2].startswith(b"K="))
 need(fields[3].startswith(b"H=") and fields[4].startswith(b"A=") and fields[5].startswith(b"D="))
 index=udec(fields[0][2:],0,12);slot=fields[1][2:];kind=fields[2][2:]
 need(V19_WIRE_ROLE_SPEC[index]==(index,slot,kind))
 h64(fields[3][2:]);access=udec(fields[4][2:],0,2);h64(fields[5][2:])
 core=b".".join(fields[:5]);need(fields[5][2:]==sha(V19_WIRE_ROW_DOMAIN+core))
 return index,slot,kind,fields[3][2:],access,fields[5][2:]

def v19_wire_rows_from_caps_v19(caps):
 need(type(caps)is tuple)
 rows=[]
 for kind,slot,number,identity in caps:
  matches=tuple(row for row in V19_WIRE_ROLE_SPEC if row[1]==slot)
  need(len(matches)==1 and matches[0][2]==kind)
  rows.append(v19_wire_row_v19(matches[0][0],slot,kind,number,identity))
 parsed=tuple(v19_parse_wire_row_v19(row) for row in rows)
 need(tuple(item[0] for item in parsed)==tuple(sorted(item[0] for item in parsed)))
 return tuple(rows)

def registry_transfer_set_bytes(caps):
 rows=v19_wire_rows_from_caps_v19(caps)
 return b"".join(b"WIRE_ROW="+row+b"\n" for row in rows)

def v19_receiver_wire_set_v19(raw):
 need(type(raw)is bytes)
 if raw==b"NONE":return ()
 rows=tuple(raw.split(b","))
 parsed=tuple(v19_parse_wire_row_v19(row) for row in rows)
 need(len(rows)==len(set(rows)) and tuple(item[0] for item in parsed)==tuple(sorted(item[0] for item in parsed)))
 return rows

def v19_receiver_proof_v19(receipt):
 installed=v19_receiver_wire_set_v19(receipt[b"RECEIVER_INSTALLED_HISTORY"])
 retained=v19_receiver_wire_set_v19(receipt[b"RECEIVER_CURRENT_RETAINED_SET"])
 kill=v19_receiver_wire_set_v19(receipt[b"RECEIVER_KILL_CENSUS"])
 disposition=receipt[b"RECEIVER_OUTER_DISPOSITION"]
 need(disposition in (b"ACCEPTED_RETAINED",b"ACCEPTED_RECEIVED_THEN_CLOSED",b"CLOSED_OMITTED"))
 rows=((b"RECEIVER_INSTALLED_HISTORY",receipt[b"RECEIVER_INSTALLED_HISTORY"]),(b"RECEIVER_CURRENT_RETAINED_SET",receipt[b"RECEIVER_CURRENT_RETAINED_SET"]),(b"RECEIVER_KILL_CENSUS",receipt[b"RECEIVER_KILL_CENSUS"]),(b"RECEIVER_OUTER_DISPOSITION",disposition))
 digests=tuple(sha(V19_RECEIVER_PROOF_DOMAIN+key+b"="+value+b"\n") for key,value in rows)
 need(receipt[b"RECEIVER_INSTALLED_HISTORY_SHA256"]==digests[0])
 need(receipt[b"RECEIVER_CURRENT_RETAINED_SET_SHA256"]==digests[1])
 need(receipt[b"RECEIVER_KILL_CENSUS_SHA256"]==digests[2])
 need(receipt[b"RECEIVER_OUTER_DISPOSITION_SHA256"]==digests[3])
 return installed,retained,kill,disposition,digests

V19_WATCHDOG_MINIMAL_CONTEXT_STAGE3=minimal_context
def minimal_context():
 context=LifecycleContextV19(V19_WATCHDOG_MINIMAL_CONTEXT_STAGE3())
 context[b"v19_generic_census"]=WATCHDOG_GENERIC_CENSUS_V19
 context[b"v19_refusal_census"]=WATCHDOG_REFUSAL_CENSUS_V19
 context[b"v19_generic_offer_cache"]=WATCHDOG_GENERIC_OFFER_CACHE_V19
 context[b"v19_refusal_offer_cache"]=WATCHDOG_REFUSAL_OFFER_CACHE_V19
 context[b"v19_acceptance_commit"]=WATCHDOG_ACCEPTANCE_COMMIT_V19
 context[b"v19_closure_cell"]=WATCHDOG_CLOSURE_CELL_V19
 context[b"v19_last_installed_history"]=WATCHDOG_LAST_INSTALLED_HISTORY_V19
 context[b"v19_pending_receiver_proof"]=None
 context[b"v19_pending_acceptance_candidate"]=None
 context[b"v19_pending_acceptance_verify_deadline"]=0
 context[b"v19_offer_outer_poller_record_id"]=-1
 WATCHDOG_LAST_INSTALLED_HISTORY_V19.reset(0)
 return context

def v19_record_installed_history(context,frame):
 history=context[b"v19_last_installed_history"]
 context[b"v19_installed_history_epoch"]+=1
 history.epoch=context[b"v19_installed_history_epoch"]
 for index in range(frame.installed_count):
  record_id=frame.records[index].record_id
  if not history.contains(record_id):history.add(record_id)
 return history

def v19_census_digest(census):
 raw=(b"EPOCH="+str(census.epoch).encode()+b"\nMODE="+census.mode+b"\nFULL="+b",".join(str(item).encode() for item in census.full_live.exact_tuple())+b"\nOFFERED="+b",".join(str(item).encode() for item in census.offered.exact_tuple())+b"\nSAFE="+b",".join(str(item).encode() for item in census.safe_local.exact_tuple())+b"\nBLOCKING="+b",".join(str(item).encode() for item in census.blocking.exact_tuple())+b"\nKILL="+b",".join(str(item).encode() for item in census.kill.exact_tuple())+b"\nRAW="+b",".join(str(item).encode() for item in census.raw.exact_tuple())+b"\n")
 census.digest=sha(raw);return census.digest

def v19_bind_leaf_for_kill_v19(context):
 number=context.get(b"cgfd",-1)
 leaf=None
 if number>=0:
  held=os.fstat(number);leaf=(b"VERIFIED_CGROUP_LEAF",held.st_dev,held.st_ino)
 else:held=None
 if context.get(b"cgroup_identity") is None:
  if held is not None:context[b"cgroup_identity"]=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)
 leaf_records=()
 if leaf is not None:
  leaf_records=(context[b"fd_registry"][b"cgfd"],context[b"fd_registry"][b"root_events_fd"],context[b"fd_registry"][b"root_kill_fd"])
 for record in WATCHDOG_PHYSICAL_RECORDS_V19:
  if watchdog_record_live_v19(record):
   lifecycle_bind_identity_v19(record)
   candidate=leaf if any(record is item for item in leaf_records) else (b"VERIFIED_NON_KILL_PHYSICAL",)+record.physical_identity
   if record.verified_kill_leaf_identity is None:record.verified_kill_leaf_identity=candidate
   else:need(record.verified_kill_leaf_identity==candidate)
 return leaf

def v19_populate_census(context,census,phase,refusal=False):
 cache=context[b"v19_refusal_offer_cache"] if refusal else context[b"v19_generic_offer_cache"]
 mode=b"ZERO_RIGHTS" if refusal else b"GENERIC_13"
 epoch=cache.epoch;census.reset(epoch,phase,mode);leaf=v19_bind_leaf_for_kill_v19(context)
 seen=WATCHDOG_CENSUS_SEEN_V19;seen.reset(epoch)
 for record in WATCHDOG_PHYSICAL_RECORDS_V19:seen.add(record.record_id)
 need(seen.count==97)
 refusal_guard=bool(context.get(b"refusal_slot_locked") and context.get(b"actor_control_fd",-1)>=0)
 for record in WATCHDOG_PHYSICAL_RECORDS_V19:
  if record.state in (b"ACQUIRING",b"CLOSE_RETRY"):need(False)
  if watchdog_record_live_v19(record):
   lifecycle_bind_identity_v19(record)
   need(record.identity is not None and record.physical_identity is not None and record.verified_kill_leaf_identity is not None and record.access!=b"UNKNOWN")
   census.full_live.add(record.record_id);role=watchdog_registry_slot_v19(context,record)
   if refusal:
    if role==b"actor_control_fd" and not refusal_guard:census.blocking.add(record.record_id)
    elif role in WATCHDOG_OFFERED_SLOTS_V19 or role in WATCHDOG_SAFE_LOCAL_SLOTS_V19:census.safe_local.add(record.record_id)
    else:census.blocking.add(record.record_id)
   else:
    if role in WATCHDOG_OFFERED_SLOTS_V19:census.offered.add(record.record_id)
    elif role in WATCHDOG_SAFE_LOCAL_SLOTS_V19:census.safe_local.add(record.record_id)
    else:census.blocking.add(record.record_id)
   if leaf is not None and record.verified_kill_leaf_identity==leaf and record.access in (os.O_WRONLY,os.O_RDWR):census.kill.add(record.record_id)
  if record.raw_cell.state==b"LOCAL_RAW":census.raw.add(record.record_id)
 for frame in (WATCHDOG_MONITORED_FRAME_V19,WATCHDOG_EXTERNAL_CONTROL_FRAME_V19,WATCHDOG_EXTERNAL_RECEIPT_FRAME_V19,WATCHDOG_REFUSAL_FRAME_V19):
  for cell in frame.raw_cells:
   if cell.state==b"LOCAL_RAW":census.raw.add(cell.record_id)
 need(census.blocking.count==0 and census.raw.count==0)
 if refusal:
  need(refusal_guard and census.offered.count==0 and census.safe_local.count<=25)
 else:
  need(census.offered.count<=13 and census.safe_local.count<=12)
  need(census.kill.count==(1 if context.get(b"containment_bound") else 0))
 v19_census_digest(census);return census

def v19_copy_ids(target,source):
 target.reset(source.epoch)
 for record_id in source.exact_tuple():target.add(record_id)

def v19_offer_census_boundary(context,phase,refusal=False,caps=()):
 cache=context[b"v19_refusal_offer_cache"] if refusal else context[b"v19_generic_offer_cache"]
 census=context[b"v19_refusal_census"] if refusal else context[b"v19_generic_census"]
 if phase==b"FREEZE":
  need(cache.state==b"EMPTY" and cache.atomic_authority is None);cache.epoch+=1;cache.boundary=0
 else:need(cache.state==b"FROZEN" and cache.atomic_authority is not None)
 v19_populate_census(context,census,phase,refusal)
 wire_rows=v19_wire_rows_from_caps_v19(caps)
 cap_record_ids=tuple(context[b"fd_registry"][slot].record_id for kind,slot,number,identity in caps)
 identity_raw=b"".join(watchdog_registry_slot_v19(context,record)+b":"+str(record.raw_fd).encode()+b":"+str(record.epoch).encode()+b":"+sha(repr((record.identity,record.leaf_identity,record.access)).encode())+b"\n" for record in WATCHDOG_PHYSICAL_RECORDS_V19 if watchdog_record_live_v19(record))
 if refusal:
  need(cache.mode==b"ZERO_RIGHTS" and caps==() and wire_rows==() and cap_record_ids==() and census.offered.count==0)
 else:
  need(cache.mode==b"GENERIC_13" and cap_record_ids==census.offered.exact_tuple() and len(wire_rows)==len(caps)<=13)
 if phase==b"FREEZE":
  v19_copy_ids(cache.frozen_full,census.full_live);v19_copy_ids(cache.frozen_offered,census.offered)
  v19_copy_ids(cache.frozen_safe,census.safe_local);v19_copy_ids(cache.frozen_kill,census.kill)
  v19_copy_ids(cache.frozen_raw,census.raw)
  cache.frozen_census_sha=census.digest;cache.capability_sha=sha(registry_transfer_set_bytes(caps))
  cache.identity_sha=sha(identity_raw);cache.frozen_wire_rows=wire_rows
  cache.wire_sha=sha(registry_transfer_set_bytes(caps));cache.state=b"CENSUS_PREPARED"
  outer=-1 if refusal else context.get(b"outer_pidfd",-1)
  cache.outer_record_id=context[b"fd_registry"][b"outer_pidfd"].record_id if outer>=0 else -1
  cache.outer_state=context.get(b"outer_pidfd_offer_state",b"NOT_BOUND") if outer>=0 else b"NOT_BOUND"
 else:
  need(census.mode==cache.mode and census.full_live.exact_tuple()==cache.frozen_full.exact_tuple())
  need(census.offered.exact_tuple()==cache.frozen_offered.exact_tuple())
  need(census.safe_local.exact_tuple()==cache.frozen_safe.exact_tuple())
  need(census.kill.exact_tuple()==cache.frozen_kill.exact_tuple())
  need(census.raw.exact_tuple()==cache.frozen_raw.exact_tuple())
  need(census.digest==cache.frozen_census_sha and sha(identity_raw)==cache.identity_sha)
  need(wire_rows==cache.frozen_wire_rows and sha(registry_transfer_set_bytes(caps))==cache.wire_sha==cache.capability_sha)
  need(cache.offer_sha==sha(cache.raw()))
  current_outer=context.get(b"outer_pidfd",-1);need((current_outer>=0)==(cache.outer_record_id>=0))
  if current_outer>=0:
   need(context[b"fd_registry"][b"outer_pidfd"].record_id==cache.outer_record_id)
   current_outer_state=context.get(b"outer_pidfd_offer_state",b"NOT_BOUND")
   if cache.outer_state==b"PRE_READY_OFFER_FROZEN":need(current_outer_state in (b"PRE_READY_OFFER_FROZEN",b"POST_OFFER_READY_RETAINED"))
   else:need(current_outer_state==cache.outer_state)
 if phase!=b"FREEZE":
  cache.boundary+=1;context[b"v19_refusal_boundary_index" if refusal else b"v19_offer_boundary_index"]=cache.boundary
 return census

def unique_kill_authority(context,required=True):
 leaf=v19_bind_leaf_for_kill_v19(context);count=0;selected=None
 for record in WATCHDOG_PHYSICAL_RECORDS_V19:
  if watchdog_record_live_v19(record):
   lifecycle_bind_identity_v19(record)
   need(record.physical_identity is not None and record.verified_kill_leaf_identity is not None and record.access!=b"UNKNOWN")
   if leaf is not None and record.verified_kill_leaf_identity==leaf and record.access in (os.O_WRONLY,os.O_RDWR):
    count+=1;selected=record
 need(count==(1 if required else 0))
 if required:
  need(selected.semantic_role==b"root_kill_fd" and watchdog_role_spec_v19(selected.semantic_role)[1]==b"ROOT_KILL_FD")
  need(selected is context[b"fd_registry"][b"root_kill_fd"])
 return count==1

V15_KILL_ONCE_V19=kill_once
def kill_once(context,reason):
 before=context[b"kill_call_count"]
 if context.get(b"containment_bound") and context.get(b"payload_release_possible"):
  unique_kill_authority(context,True)
 result=V15_KILL_ONCE_V19(context,reason)
 after=context[b"kill_call_count"]
 pre_call=(b"NOT_RESERVED",b"AUTHORITY_RESERVED",b"TICKET_COMMITTING",b"TICKET_DURABILITY_UNKNOWN",b"CALL_RESERVED",b"CALL_UNAVAILABLE",b"DEADLINE_PRECLUDED")
 post_call=(b"CALL_ENTERED",b"RETURN_UNKNOWN",b"SHORT_OR_UNKNOWN",b"RETURNED_2",b"RETURNED_2_EMPTY_CONFIRMED",b"RETURNED_2_POSTCHECK_UNKNOWN")
 need(before in (0,1) and after in (0,1) and after>=before)
 if after==0:need(before==0 and context[b"kill_state"] in pre_call)
 else:need(context[b"kill_state"] in post_call and context.get(b"kill_authority_consumed") and context.get(b"kill_call_attempted"))
 return result

def external_identity(kind,number,context):
 record=context[b"fd_registry"][next(slot for slot,entry in context[b"fd_registry"].items() if watchdog_record_live_v19(entry) and entry.raw_fd==number)]
 lifecycle_bind_identity_v19(record);need(watchdog_role_spec_v19(record.semantic_role)[1]==kind)
 held=os.fstat(number);access=record.access
 if kind==b"PENDING_EXPECTED_RAW_FD":
  pending=context.get(b"record_pending");need(pending is not None and context.get(b"record_sequence_frozen"))
  expected=context[b"durability_raw"][pending[2]];again=sealed_carrier(number,len(expected))
  delta_raw=semantic_delta_bytes(pending[4]);need(again==expected and sha(again)==pending[3] and access==os.O_RDWR)
  os.lseek(number,0,os.SEEK_SET)
  return kind+b":"+str(held.st_dev).encode()+b":"+str(held.st_ino).encode()+b":"+format(held.st_mode,"o").encode()+b":"+str(held.st_nlink).encode()+b":"+str(held.st_uid).encode()+b":"+str(held.st_gid).encode()+b":ACCESS="+str(access).encode()+b":SEALED="+str(EXACT_SEALS).encode()+b":BYTES="+str(len(expected)).encode()+b":SHA256="+pending[3]+b":SEMANTIC_DELTA_SHA256="+sha(delta_raw)
 if kind==b"OUTER_PIDFD":
  provenance=context.get(b"outer_pidfd_provenance")
  need(provenance==(number,context[b"outer_pid"],context[b"outer_starttime"]))
  need(context.get(b"outer_pidfd_offer_state") in (b"PRE_READY_CACHED_PROVENANCE_MATCHED",b"PRE_READY_OFFER_FROZEN",b"POST_OFFER_READY_RETAINED"))
  return kind+b":"+str(provenance[1]).encode()+b":"+str(provenance[2]).encode()+b":PIDFD:ACCESS="+str(access).encode()+b":PROVENANCE=PRE_EXIT_IMMUTABLE:EXIT_READY=0"
 if kind==b"ACTOR_CONTROL_FD":
  flags=fcntl.fcntl(number,fcntl.F_GETFL);need(stat.S_ISSOCK(held.st_mode) and flags&os.O_NONBLOCK)
  return kind+b":"+str(held.st_dev).encode()+b":"+str(held.st_ino).encode()+b":SOCK_SEQPACKET:ACCESS="+str(access).encode()+b":NONBLOCK=1"
 return kind+b":"+str(held.st_dev).encode()+b":"+str(held.st_ino).encode()+b":"+format(held.st_mode,"o").encode()+b":"+str(held.st_nlink).encode()+b":"+str(held.st_uid).encode()+b":"+str(held.st_gid).encode()+b":ACCESS="+str(access).encode()

def external_capabilities(control,context):
 result=ownership_transfer_keys(context)
 need(len(result)<=13 and tuple(item[0] for item in result)==tuple(sorted((item[0] for item in result),key=EXTERNAL_RIGHTS_ORDER.index)))
 actor=tuple(item for item in result if item[0]==b"ACTOR_CONTROL_FD")
 if actor:need(len(actor)==1 and control is not None and control.fileno()==actor[0][2])
 if context.get(b"record_pending") is not None:need(any(item[0]==b"PENDING_EXPECTED_RAW_FD" for item in result))
 unique_kill_authority(context,bool(context.get(b"containment_bound")));return result

def assert_registry_transfer_set(context,caps):
 current=ownership_transfer_keys(context)
 need(current==caps and registry_transfer_set_bytes(current)==registry_transfer_set_bytes(caps))
 cache=context[b"v19_generic_offer_cache"];index=cache.boundary
 need(index<3);phase=(b"FREEZE",b"PRE_SEND",b"ACCEPT")[index]
 census=v19_offer_census_boundary(context,phase,False,caps)
 if phase==b"ACCEPT":v19_prepare_acceptance_v19(context,b"GENERIC_ACCEPTED",context[b"v19_generic_offer_cache"],census)
 return current

V15_RESERVE_EXTERNAL_PACKET_V19=reserve_external_packet
def reserve_external_packet(kind,state,receiver,effect,deadline,pairs):
 context=ACTIVE_LIFECYCLE_CONTEXT;need(context is not None)
 cache=context[b"v19_refusal_offer_cache"] if kind==b"REFUSAL_CLOSE_OFFER" else context[b"v19_generic_offer_cache"]
 if cache.atomic_authority is not None:
  cache.restore_authority()
  boundary_key=b"v19_refusal_boundary_index" if kind==b"REFUSAL_CLOSE_OFFER" else b"v19_offer_boundary_index"
  context[boundary_key]=cache.atomic_authority[5]
  return cache.raw(),cache.prepared_sequence
 if kind==b"REFUSAL_CLOSE_OFFER" and cache.state==b"EMPTY":v19_offer_census_boundary(context,b"FREEZE",True,())
 try:
  result=V15_RESERVE_EXTERNAL_PACKET_V19(kind,state,receiver,effect,deadline,pairs)
  cache.store_offer(result[0],result[1])
  boundary_key=b"v19_refusal_boundary_index" if kind==b"REFUSAL_CLOSE_OFFER" else b"v19_offer_boundary_index"
  context[boundary_key]=cache.atomic_authority[5]
  return result
 except BaseException:
  if cache.atomic_authority is None:cache.discard_unactivated()
  raise

V15_EXTERNAL_TRANSFER_V19=external_transfer
def external_transfer(control,context,reason):
 try:return V15_EXTERNAL_TRANSFER_V19(control,context,reason)
 except BaseException:
  cache=context[b"v19_generic_offer_cache"]
  if cache.state==b"CENSUS_PREPARED" and cache.atomic_authority is None and not cache.possible_send:
   cache.discard_unactivated();context[b"v19_offer_boundary_index"]=0
  raise

V15_MATERIALIZE_REFUSAL_OFFER_V19=materialize_cached_refusal_offer
def materialize_cached_refusal_offer(context):
 result=V15_MATERIALIZE_REFUSAL_OFFER_V19(context)
 need(context[b"v19_refusal_offer_cache"].state==b"FROZEN" and context[b"v19_refusal_offer_cache"].boundary==1)
 return result

V15_EXTERNAL_SEND_V19=external_send
def external_send(control,context,raw,deadline,rights=()):
 refusal=b"|kind=REFUSAL_CLOSE_OFFER|" in raw
 generic=b"|kind=TRANSFER_OFFER|" in raw
 if refusal:
  need(rights==())
  v19_offer_census_boundary(context,b"PRE_SEND",True,())
  context[b"v19_refusal_boundary_index"]=2
 if refusal or generic:
  cache=context[b"v19_refusal_offer_cache"] if refusal else context[b"v19_generic_offer_cache"]
  need(not cache.possible_send);cache.possible_send=True
 result=V15_EXTERNAL_SEND_V19(control,context,raw,deadline,rights)
 if refusal or generic:
  need(not cache.sent_once);cache.sent_once=True
 return result

def offer_readiness_snapshot(context):
 actor=actor_pidfd_provenance(context);external=context.get(b"external_owner_pidfd_provenance")
 need(type(external)is tuple and len(external)==3 and external[0]==15)
 actor_ready=bool(context.get(b"actor_pidfd_exit_ready_observed"))
 outer_ready=bool(context.get(b"pidfd_exit_ready_observed"))
 external_ready=bool(context.get(b"external_owner_pidfd_exit_ready_observed"))
 outer=context.get(b"outer_pidfd",-1);snapshot_poller=context[b"offer_snapshot_poller"]
 if outer>=0:
  outer_record=context[b"fd_registry"][b"outer_pidfd"]
  if context.get(b"v19_offer_outer_poller_record_id",-1)!=outer_record.record_id:
   cache=context[b"v19_generic_offer_cache"]
   need(cache.state not in (b"FROZEN",) and cache.atomic_authority is None)
   register_lifecycle_poller(context,snapshot_poller,b"outer_pidfd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
   context[b"v19_offer_outer_poller_record_id"]=outer_record.record_id
 events=snapshot_poller.poll(0)
 for number,event in events:
  ready=pidfd_ready_event(event)
  if number==actor[0] and ready:actor_ready=True
  elif number==external[0] and ready:external_ready=True
  elif outer>=0 and number==outer and ready:outer_ready=True
 watch_poll_outer_readiness_v19(context,events)
 return actor_ready,outer_ready,external_ready

def apply_offer_readiness(context,snapshot,deadline):
 cache=context[b"v19_generic_offer_cache"];actor_ready,outer_ready,external_ready=snapshot
 if actor_ready and not context.get(b"actor_pidfd_exit_ready_observed"):mark_actor_pidfd_lost(context)
 if external_ready:
  context[b"external_owner_pidfd_exit_ready_observed"]=True
  raise RefusalFinalityPending("external-owner-pidfd-ready-no-takeover")
 number=context.get(b"outer_pidfd",-1)
 if outer_ready and number>=0:
  provenance=context.get(b"outer_pidfd_provenance")
  need(provenance==(number,context[b"outer_pid"],context[b"outer_starttime"]))
  if cache.state==b"FROZEN" and cache.atomic_authority is not None:
   need(cache.outer_record_id==context[b"fd_registry"][b"outer_pidfd"].record_id)
   need(context.get(b"outer_pidfd_offer_state") in (b"PRE_READY_OFFER_FROZEN",b"POST_OFFER_READY_RETAINED"))
   context[b"pidfd_exit_ready_observed"]=True
   context[b"outer_pidfd_offer_state"]=b"POST_OFFER_READY_RETAINED"
   return True
  need(cache.atomic_authority is None and not cache.possible_send)
  if cache.state==b"CENSUS_PREPARED":
   cache.discard_unactivated();context[b"v19_offer_boundary_index"]=0
  release_identity=context.get(b"outer_release_record_identity")
  need(type(release_identity)is tuple and len(release_identity)==3 and release_identity[0]!=EMPTY_SHA)
  context[b"pidfd_exit_ready_observed"]=True;context[b"outer_pidfd_offer_state"]=b"POST_READY_CACHED_PROVENANCE"
  checkpoint(CERT,0,deadline);need(time.monotonic_ns()<=deadline)
  close_lifecycle_fd(context,b"outer_pidfd")
  context[b"outer_pidfd_close_state"]=b"OMITTED_EXIT_READY_LOCAL_CLOSED"
 return True

def promote_later_offer_readiness(context,snapshot):
 actor_ready,outer_ready,external_ready=snapshot
 if actor_ready and not context.get(b"actor_pidfd_exit_ready_observed"):mark_actor_pidfd_lost(context)
 if outer_ready and context.get(b"outer_pidfd",-1)>=0:
  cache=context[b"v19_generic_offer_cache"]
  need(cache.state==b"FROZEN" and cache.atomic_authority is not None)
  need(cache.outer_record_id==context[b"fd_registry"][b"outer_pidfd"].record_id)
  context[b"pidfd_exit_ready_observed"]=True
  context[b"outer_pidfd_offer_state"]=b"POST_OFFER_READY_RETAINED"
 if external_ready:
  context[b"external_owner_pidfd_exit_ready_observed"]=True
  raise RefusalFinalityPending("external-owner-pidfd-ready-before-acceptance-commit")
 return True

def prepare_outer_pidfd_offer_binding(context,deadline):
 need(context.get(b"transfer_offer_cache") is None and time.monotonic_ns()<=deadline)
 actor=actor_pidfd_provenance(context);external=context.get(b"external_owner_pidfd_provenance")
 need(type(external)is tuple and len(external)==3 and external[0]==15)
 number=context.get(b"outer_pidfd",-1);pid=context.get(b"outer_pid",-1)
 start=context.get(b"outer_starttime",0);release=context.get(b"outer_release_record_identity")
 if number<0:
  if context.get(b"outer_pidfd_close_state")==b"OMITTED_EXIT_READY_LOCAL_CLOSED":
   need(context.get(b"pidfd_exit_ready_observed") and type(release)is tuple)
   wire_state=b"POST_READY_OMITTED_LOCAL_CLOSED";right=b"0"
  else:wire_state=b"NOT_BOUND";right=b"0";pid=-1;start=0;release=(EMPTY_SHA,b"NONE",b"NONE")
 else:
  provenance=context.get(b"outer_pidfd_provenance");need(provenance==(number,pid,start))
  need(not context[b"pidfd_exit_ready_observed"]);wire_state=b"PRE_READY_CACHED_PROVENANCE_MATCHED"
  context[b"outer_pidfd_offer_state"]=b"PRE_READY_OFFER_FROZEN";right=b"1"
  if release is None:release=(EMPTY_SHA,b"NONE",b"NONE")
 binding=(str(actor[1]).encode(),str(actor[2]).encode(),b"1" if context.get(b"actor_pidfd_exit_ready_observed") else b"0",str(external[1]).encode(),str(external[2]).encode(),b"1" if context.get(b"external_owner_pidfd_exit_ready_observed") else b"0",str(pid).encode(),str(start).encode(),wire_state,b"1" if context.get(b"pidfd_exit_ready_observed") else b"0",release[0],release[1],release[2],right)
 context[b"outer_offer_binding"]=binding;return binding

def v19_prepare_acceptance_v19(context,mode,cache,census):
 commit=context[b"v19_acceptance_commit"];need(commit.state in (b"EMPTY",b"PREPARED"))
 need(cache.state==b"FROZEN" and cache.boundary==3 and cache.possible_send)
 need(cache.atomic_authority is not None and cache.atomic_authority[0]==b"FROZEN" and len(cache.atomic_authority)==19)
 need(cache.offer_sha==sha(cache.raw()) and census.epoch==cache.epoch and census.mode==cache.mode)
 need(census.digest==cache.frozen_census_sha and cache.wire_sha==sha(registry_transfer_set_bytes(()) if cache.mode==b"ZERO_RIGHTS" else b"".join(b"WIRE_ROW="+row+b"\n" for row in cache.frozen_wire_rows)))
 proof=context.get(b"v19_pending_receiver_proof");need(type(proof)is tuple and len(proof)==5)
 installed,current_retained,receiver_kill,outer_disposition,proof_digests=proof
 frozen_wire=cache.frozen_wire_rows
 need(installed==frozen_wire and len(installed)==len(set(installed)))
 expected_kill=()
 if cache.mode==b"GENERIC_13":
  root_record=context[b"fd_registry"][b"root_kill_fd"]
  if cache.frozen_kill.contains(root_record.record_id):
   expected_kill=tuple(row for row in frozen_wire if v19_parse_wire_row_v19(row)[1]==b"root_kill_fd")
 need(receiver_kill==expected_kill)
 for record_id in census.full_live.exact_tuple():lifecycle_bind_identity_v19(WATCHDOG_PHYSICAL_RECORDS_V19[record_id])
 outer_rows=tuple(row for row in frozen_wire if v19_parse_wire_row_v19(row)[1]==b"outer_pidfd")
 if cache.outer_record_id>=0:
  need(len(outer_rows)==1)
  outer_row=outer_rows[0]
  if outer_disposition==b"ACCEPTED_RECEIVED_THEN_CLOSED":
   need(outer_row not in current_retained);expected_retained=tuple(row for row in installed if row!=outer_row)
  else:
   need(outer_disposition==b"ACCEPTED_RETAINED" and outer_row in current_retained);expected_retained=installed
 else:
  need(outer_rows==() and outer_disposition==b"CLOSED_OMITTED");expected_retained=installed
 need(current_retained==expected_retained)
 if cache.mode==b"ZERO_RIGHTS":
  need(mode==b"REFUSAL_ACCEPTED" and frozen_wire==installed==current_retained==receiver_kill==())
 else:need(mode==b"GENERIC_ACCEPTED")
 sequence=context[b"v19_pending_acceptance_sequence"];predecessor=context[b"v19_pending_acceptance_predecessor"]
 receipt_sha=context[b"v19_pending_acceptance_digest"]
 candidate=(b"COMPLETE_IMMUTABLE_CANDIDATE",mode,cache.offer_sha,sequence,predecessor,receipt_sha,cache.frozen_census_sha,census.digest,installed,current_retained,receiver_kill,cache.outer_record_id,outer_disposition,True,cache.epoch,proof_digests,cache.atomic_authority)
 commit.candidate=candidate;commit.state=b"PREPARED";context[b"v19_pending_acceptance_candidate"]=candidate
 return commit

V15_VERIFY_EXTERNAL_ACCEPTANCE_V19=verify_external_acceptance
def verify_external_acceptance(receipt_kind,offer,receipt_raw,values,sequence,predecessor,manifest_sha,finality_deadline,closure_deadline,verify_deadline):
 digest=V15_VERIFY_EXTERNAL_ACCEPTANCE_V19(receipt_kind,offer,receipt_raw,values,sequence,predecessor,manifest_sha,finality_deadline,closure_deadline,verify_deadline)
 context=ACTIVE_LIFECYCLE_CONTEXT;need(context is not None)
 checkpoint(CERT,0,verify_deadline);need(time.monotonic_ns()<=verify_deadline)
 signed_receipt=parse_fixed(receipt_raw,b"P27E001_EXTERNAL_DURABLE_RECEIPT_V15",EXTERNAL_RECEIPT_KEYS,b"RECEIPT_END=1")
 context[b"v19_pending_receiver_proof"]=v19_receiver_proof_v19(signed_receipt)
 context[b"v19_pending_acceptance_digest"]=digest
 context[b"v19_pending_acceptance_sequence"]=sequence
 context[b"v19_pending_acceptance_predecessor"]=predecessor
 context[b"v19_pending_acceptance_verify_deadline"]=verify_deadline
 if receipt_kind==b"REFUSAL_CLOSE":
  census=v19_offer_census_boundary(context,b"ACCEPT",True,())
  context[b"v19_refusal_boundary_index"]=3
  v19_prepare_acceptance_v19(context,b"REFUSAL_ACCEPTED",context[b"v19_refusal_offer_cache"],census)
 return digest

V15_COMMIT_EXTERNAL_RECEIVE_V19=commit_external_receive
def commit_external_receive(sequence):
 global WATCHDOG_ACCEPTANCE_AUTHORITY_V19
 context=ACTIVE_LIFECYCLE_CONTEXT;need(context is not None)
 commit=context[b"v19_acceptance_commit"];candidate=commit.candidate
 need(commit.state==b"PREPARED" and WATCHDOG_ACCEPTANCE_AUTHORITY_V19 is None)
 need(candidate is context[b"v19_pending_acceptance_candidate"] and candidate[0]==b"COMPLETE_IMMUTABLE_CANDIDATE")
 need(candidate[3]==sequence==context[b"v19_pending_acceptance_sequence"])
 need(sequence==EXTERNAL_RECV_SEQ+1 and candidate[16][0]==b"FROZEN")
 need(candidate[1] in (b"GENERIC_ACCEPTED",b"REFUSAL_ACCEPTED"))
 need(candidate[4]==context[b"external_chain_sha"] and candidate[16][2]==candidate[2])
 cache=context[b"v19_generic_offer_cache"] if candidate[1]==b"GENERIC_ACCEPTED" else context[b"v19_refusal_offer_cache"]
 need(cache.atomic_authority is candidate[16] and cache.state==b"FROZEN" and cache.boundary==3 and cache.raw()==candidate[16][1])
 commit_deadline=(transfer_stage_window(context,b"TRANSFER_ACCEPTANCE_COMMIT")[0] if candidate[1]==b"GENERIC_ACCEPTED" else refusal_stage_window(context,b"REFUSAL_ACCEPTANCE_COMMIT")[0])
 checkpoint(CERT,0,commit_deadline);need(time.monotonic_ns()<=commit_deadline)
 final_readiness=offer_readiness_snapshot(context)
 need(not final_readiness[2])
 if final_readiness[1] and candidate[11]>=0:context[b"outer_pidfd_offer_state"]=b"POST_OFFER_READY_RETAINED"
 authority=(b"COMMITTED",)+candidate[1:]+(final_readiness,)
 WATCHDOG_ACCEPTANCE_AUTHORITY_V19=authority
 return v19_closure_driver(context,authority,None,None)

def ownership_capabilities_closed(context):
 return all(record.state==b"CLOSED" for record in WATCHDOG_PHYSICAL_RECORDS_V19)

def v19_closure_commit_valid(context,cell):
 if cell.mode in (b"GENERIC_ACCEPTED",b"REFUSAL_ACCEPTED"):
  authority=cell.acceptance_authority
  return authority is WATCHDOG_ACCEPTANCE_AUTHORITY_V19 and authority[0]==b"COMMITTED" and authority[1]==cell.mode and authority[2]==cell.commit_offer_sha
 return cell.commit_state==b"DIRECT_DURABLE"

def v19_closure_wait(cell):
 delay=max(10,min(50,cell.retry_ms))
 try:WATCHDOG_CLOSURE_WAIT_V19.poll(delay)
 except BaseException:pass
 cell.retry_ms=min(50,delay+10);cell.timing_overrun=True

def v20_packet_without_sequence_commit(kind,pairs,message_sequence):
 need(type(message_sequence)is int and message_sequence==CONTROL_SEND_SEQ+1)
 need(kind in CONTROL_SPEC and b"|" not in kind and b"\n" not in kind)
 provided={}
 for key,value in pairs:
  need(key and value and b"|" not in key+value and b"\n" not in key+value and b"=" not in key+value and key not in provided)
  provided[key]=value
 spec_state,spec_receiver,spec_effect,deadline_key=CONTROL_SPEC[kind]
 state=provided.pop(b"state",spec_state);receiver=provided.pop(b"expected_state",spec_receiver)
 effect=provided.pop(b"effect_state",spec_effect)
 if kind==b"V15_ABORT":need(state==spec_state and effect==spec_effect and receiver not in (b"",b"*"))
 else:need((state,receiver,effect)==(spec_state,spec_receiver,spec_effect) and state!=b"*" and receiver!=b"*" and effect!=b"*")
 ordinal=provided.pop(b"ordinal");probe=provided.pop(b"probe")
 if b"auth_id" in provided:need(provided.pop(b"auth_id")==AUTH)
 if b"sender" in provided:need(provided.pop(b"sender")==b"B")
 need(deadline_key in provided);deadline_raw=provided.pop(deadline_key);udec(deadline_raw,1)
 need(not any(key in CONTROL_RESERVED for key in provided))
 transition=state+b"->"+receiver+b":"+effect
 body=(kind+b"|protocol_version=14|session_id="+AUTH+b"|message_seq="+str(message_sequence).encode()+b"|message_sender=B|transition_id="+transition+b"|sender_state="+state+b"|expected_receiver_state="+receiver+b"|slot_ordinal="+ordinal+b"|slot_probe="+probe+b"|effect_state="+effect+b"|deadline_name="+deadline_key+b"|absolute_deadline_ns="+deadline_raw)
 for key,value in pairs:
  if key not in CONTROL_RESERVED:body+=b"|"+key+b"="+value
 raw=body+b"\n"
 need(b"|message_seq="+str(message_sequence).encode()+b"|" in raw)
 return raw

def v20_prepare_closure_candidate(context,acceptance_authority,deadline,offered):
 cell=context[b"v19_closure_cell"]
 need(cell.phase==b"NOT_STARTED")
 if deadline is not None:checkpoint(CERT,0,deadline);need(time.monotonic_ns()<=deadline)
 if acceptance_authority is not None:
  need(acceptance_authority is WATCHDOG_ACCEPTANCE_AUTHORITY_V19 and acceptance_authority[0]==b"COMMITTED")
  mode=acceptance_authority[1];commit_state=b"COMMITTED";commit_offer_sha=acceptance_authority[2]
  external_recv_sequence=acceptance_authority[3]
 else:
  mode=b"GENERIC_ACCEPTED" if offered is not None else b"DIRECT"
  commit_state=b"DIRECT_DURABLE";commit_offer_sha=EMPTY_SHA;external_recv_sequence=EXTERNAL_RECV_SEQ
 plan_ids=[]
 for endpoint_pass in (False,True):
  for record in WATCHDOG_PHYSICAL_RECORDS_V19:
   if record.state!=b"CLOSED":
    endpoint=record.semantic_role in (b"actor_control_fd",b"transfer_control_fd")
    if endpoint==endpoint_pass:plan_ids.append(record.record_id)
 need(len(plan_ids)<=97 and len(plan_ids)==len(set(plan_ids)))
 plan=(ctypes.c_int*97)(*(tuple(plan_ids)+tuple(-1 for unused in range(97-len(plan_ids)))))
 preclose_done=mode!=b"REFUSAL_ACCEPTED";preclose_state=b"NOT_ATTEMPTED"
 preclose_packet=b"";preclose_packet_sha=EMPTY_SHA;preclose_sequence=0
 preclose_deadline=0;preclose_send_latch=False;next_control_sequence=CONTROL_SEND_SEQ
 if mode==b"REFUSAL_ACCEPTED":
  need(acceptance_authority is not None)
  cached=refusal_slot(context);core=cached[1];schedule=refusal_schedule_from_core(core)
  request_sha,request_sequence,a_begin,a_arm,cross_map,origin_raw,finality_raw,closure_raw,schedule_claim=core[4]
  preclose_deadline=schedule[b"REFUSAL_ACTOR_CLOSURE"]
  next_control_sequence=CONTROL_SEND_SEQ+1
  pairs=((b"state",b"REFUSAL_DURABLY_CLOSED"),(b"expected_state",b"WAIT_REFUSAL_CLOSED"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"ack_packet_sha256",sha(cached[4])),(b"receipt_packet_sha256",sha(cached[6])),(b"cross_map_state",cross_map),(b"issuer_closure_sha256",acceptance_authority[5]),(b"issuer_record_seq",str(core[0]).encode()),(b"issuer_predecessor_sha256",core[1]),(b"no_replay",b"1"),(b"refusal_finality_deadline_ns",str(core[6]).encode()),(b"refusal_closure_deadline_ns",str(core[7]).encode()),(b"refusal_schedule_hex",schedule_claim),(b"consume_deadline_ns",str(preclose_deadline).encode()))
  preclose_packet=v20_packet_without_sequence_commit(b"V15_REFUSAL_CLOSED",pairs,next_control_sequence)
  preclose_packet_sha=sha(preclose_packet);preclose_sequence=next_control_sequence
  need(preclose_packet_sha!=EMPTY_SHA and preclose_deadline>0)
  need(b"|message_seq="+str(preclose_sequence).encode()+b"|" in preclose_packet)
 latch_candidate=(preclose_state,preclose_send_latch,preclose_packet,preclose_packet_sha,preclose_sequence,preclose_deadline)
 need(latch_candidate[0]==b"NOT_ATTEMPTED" and not latch_candidate[1])
 return (b"V20_COMPLETE_IMMUTABLE_CLOSURE_CANDIDATE",mode,commit_state,commit_offer_sha,
  acceptance_authority,external_recv_sequence,plan,len(plan_ids),preclose_done,latch_candidate,
  next_control_sequence,cell.epoch+1,b"PROCESS_EXIT_AFTER_OWNER_RELEASE")

def v20_install_closure_candidate(context,cell,candidate):
 global CONTROL_SEND_SEQ,EXTERNAL_RECV_SEQ
 tag,mode,commit_state,commit_offer_sha,authority,external_recv_sequence,plan,plan_count,preclose_done,latch_candidate,next_control_sequence,next_epoch,release_handoff=candidate
 preclose_state,preclose_send_latch,preclose_packet,preclose_packet_sha,preclose_sequence,preclose_deadline=latch_candidate
 if authority is not None:
  commit=context[b"v19_acceptance_commit"]
  EXTERNAL_RECV_SEQ=external_recv_sequence
  commit.authority=authority;commit.state=b"COMMITTED";commit.mode=authority[1]
  commit.offer_sha=authority[2];commit.record_seq=authority[3];commit.predecessor=authority[4]
  commit.receipt_sha=authority[5];commit.frozen_census_sha=authority[6]
  commit.current_census_sha=authority[7];commit.outer_record_id=authority[11]
  commit.outer_disposition=authority[12];commit.no_replay=authority[13];commit.commit_epoch=authority[14]
  context[b"external_record_seq"]=authority[3];context[b"external_chain_sha"]=authority[5]
  if mode==b"GENERIC_ACCEPTED":
   context[b"transfer_receipt_sha"]=authority[5];context[b"transfer_acceptance_state"]=b"COMMITTED"
  else:
   context[b"refusal_closure_sha"]=authority[5];context[b"refusal_offer_receipt_sha"]=authority[5]
   context[b"refusal_acceptance_state"]=b"COMMITTED"
 cell.mode=mode;cell.commit_state=commit_state;cell.commit_offer_sha=commit_offer_sha
 cell.acceptance_authority=authority;cell.epoch=next_epoch;cell.plan=plan;cell.plan_count=plan_count
 cell.cursor=0;cell.current_record_id=-1;cell.preclose_done=preclose_done
 cell.preclose_state=preclose_state;cell.preclose_packet=preclose_packet
 cell.preclose_packet_sha=preclose_packet_sha;cell.preclose_sequence=preclose_sequence
 cell.preclose_deadline=preclose_deadline;cell.preclose_send_latch=preclose_send_latch
 cell.release_handoff=release_handoff;context[b"ownership_close_started"]=True
 context[b"ownership_close_mode"]=mode;CONTROL_SEND_SEQ=next_control_sequence
 cell.phase=b"ACTIVE"
 return True

def v19_build_refusal_preclose_v19(context,cell):
 raise OwnershipClosePending("v19-preclose-builder-retired-by-v20-atomic-candidate")

def v19_refusal_preclose_once_v19(context,cell):
 need(cell.phase==b"ACTIVE" and cell.mode==b"REFUSAL_ACCEPTED")
 need(cell.preclose_packet and cell.preclose_packet_sha==sha(cell.preclose_packet))
 need(cell.preclose_sequence>=1 and cell.preclose_deadline>0)
 need(CONTROL_SEND_SEQ==cell.preclose_sequence)
 need(b"|message_seq="+str(cell.preclose_sequence).encode()+b"|" in cell.preclose_packet)
 if cell.preclose_state==b"POSSIBLE":
  cell.preclose_state=b"EFFECT_UNKNOWN";cell.preclose_done=True
  context[b"send_state"]=b"REFUSAL_CLOSURE_SEND_EFFECT_UNKNOWN";return True
 if cell.preclose_state in (b"EFFECT_UNKNOWN",b"CONFIRMED"):
  cell.preclose_done=True;return True
 need(cell.preclose_state==b"NOT_ATTEMPTED" and not cell.preclose_send_latch)
 cached=refusal_slot(context);control=context.get(b"actor_control")
 if cached[8]!=b"RECEIPT_VERIFIED_FINAL" or control is None:
  context[b"refusal_actor_closure_state"]=b"ACTOR_LOSS_OR_CONTROL_UNAVAILABLE_AFTER_DURABLE_ACCEPTANCE"
  cell.preclose_done=True;return True
 checkpoint(CERT,0,cell.preclose_deadline);need(time.monotonic_ns()<=cell.preclose_deadline)
 cell.preclose_state=b"POSSIBLE"
 cell.preclose_send_latch=True;context[b"send_state"]=b"REFUSAL_CLOSURE_SEND_EFFECT_UNKNOWN"
 try:
  send_exact(control,cell.preclose_packet,cell.preclose_deadline)
  cell.preclose_state=b"CONFIRMED";context[b"send_state"]=b"REFUSAL_CLOSURE_SENT"
  context[b"refusal_actor_closure_state"]=b"SENT"
 except BaseException:
  cell.preclose_state=b"EFFECT_UNKNOWN";context[b"send_state"]=b"REFUSAL_CLOSURE_SEND_EFFECT_UNKNOWN"
  context[b"refusal_actor_closure_state"]=b"EFFECT_UNKNOWN_NO_RESEND_HOLD"
 context[b"refusal_actor_closure_complete"]=True;cell.preclose_done=True;return True

def v19_closure_driver(context,acceptance_authority=None,deadline=None,offered=None,probe_only=False):
 global EXTERNAL_RECV_SEQ
 while True:
  preactive_probe=False
  try:
   cell=context[b"v19_closure_cell"]
   if cell.phase==b"RELEASED":os._exit(0)
   if cell.phase==b"NOT_STARTED" and probe_only:
    preactive_probe=True
    close_lifecycle_slots(context,(b"out_fd",b"err_fd",b"events_fd",b"outer_pidfd"))
    WATCHDOG_OUT_STREAM_V19.reset();WATCHDOG_ERR_STREAM_V19.reset()
    unique_kill_authority(context,bool(context.get(b"containment_bound")))
    context[b"pidfd_bound"]=False;context[b"outer_pidfd_close_state"]=b"CLOSED_NORMAL"
   context[b"outer_pidfd_offer_state"]=b"NOT_BOUND";context[b"outer_offer_binding"]=None
   return True
   if cell.phase==b"NOT_STARTED":
    v20_candidate=v20_prepare_closure_candidate(context,acceptance_authority,deadline,offered)
    v20_install_closure_candidate(context,cell,v20_candidate)
    continue
   if cell.phase==b"ACTIVE":
    need(v19_closure_commit_valid(context,cell))
    if not cell.preclose_done:v19_refusal_preclose_once_v19(context,cell)
    if cell.cursor<cell.plan_count:
     record_id=cell.plan[cell.cursor];cell.current_record_id=record_id
     record=WATCHDOG_PHYSICAL_RECORDS_V19[record_id]
     if record.state==b"ACQUIRING" and record.raw_fd<0:watchdog_record_reset_v19(record)
     elif record.state!=b"CLOSED":close_lifecycle_record_v19(context,record)
     need(record.state==b"CLOSED");cell.cursor+=1;cell.retry_ms=10;continue
    for frame in (WATCHDOG_MONITORED_FRAME_V19,WATCHDOG_EXTERNAL_CONTROL_FRAME_V19,WATCHDOG_EXTERNAL_RECEIPT_FRAME_V19,WATCHDOG_REFUSAL_FRAME_V19):
     watch_receive_cleanup_v19(context,frame)
    context[b"v19_pending_receive_frame"]=None
    cell.phase=b"CLOSED";cell.current_record_id=-1;continue
   if cell.phase==b"CLOSED":
    need(v19_closure_commit_valid(context,cell) and ownership_capabilities_closed(context))
    need(cell.preclose_state in (b"NOT_ATTEMPTED",b"EFFECT_UNKNOWN",b"CONFIRMED"))
    need(not (cell.preclose_state in (b"EFFECT_UNKNOWN",b"CONFIRMED") and not cell.preclose_send_latch))
    for record in WATCHDOG_PHYSICAL_RECORDS_V19:
     need(record.state==b"CLOSED" and record.raw_cell.state in (b"EMPTY",b"DISARMED"))
     need(record.endpoint_state in (b"NO_WRAPPER",b"PROVED_CLOSED") and record.wrapper_ref is None)
    for frame in (WATCHDOG_MONITORED_FRAME_V19,WATCHDOG_EXTERNAL_CONTROL_FRAME_V19,WATCHDOG_EXTERNAL_RECEIPT_FRAME_V19,WATCHDOG_REFUSAL_FRAME_V19):
     for raw_cell in frame.raw_cells:need(raw_cell.state in (b"EMPTY",b"DISARMED"))
    need(all(poller_cell.state in (b"FREE",b"INACTIVE") for poller_cell in WATCHDOG_POLLER_CELLS_V19))
    unique_kill_authority(context,False)
    context[b"ownership_closed_monotone"]=True;context[b"ownership_close_complete"]=True
    context[b"owner_released"]=True;cell.phase=b"RELEASED";cell.retry_ms=10;continue
   need(False)
  except BaseException:
   if preactive_probe:raise
   repair_cell=context.get(b"v19_closure_cell",WATCHDOG_CLOSURE_CELL_V19)
   if repair_cell.phase==b"NOT_STARTED":raise
   try:
    repair_cell.retained_fault=True;v19_closure_wait(repair_cell)
   except BaseException:
    try:WATCHDOG_CLOSURE_WAIT_V19.poll(10)
    except BaseException:pass

def close_ownership_capabilities(context,deadline,offered=None):
 return v19_closure_driver(context,None,deadline,offered)

def complete_started_ownership_close(context):
 return v19_closure_driver(context,None,None,None)

def close_probe(context):
 return v19_closure_driver(context,None,None,None,True)

def v19_validate_watchdog_control_surface():
 need(len(LIFECYCLE_SLOT_SPEC)==97 and len(WATCHDOG_PHYSICAL_RECORDS_V19)==97)
 need(len(WATCHDOG_IMMUTABLE_ROLE_SPEC_V19)==97 and len({row[0] for row in WATCHDOG_IMMUTABLE_ROLE_SPEC_V19})==97)
 need(WatchPhysicalRecordV19.__slots__==WATCHDOG_PHYSICAL_RECORD_FIELDS_V19 and "owns" not in WatchPhysicalRecordV19.__slots__)
 need("logical_slot" not in WatchPhysicalRecordV19.__slots__ and "transferable" not in WatchPhysicalRecordV19.__slots__ and "transfer_order" not in WatchPhysicalRecordV19.__slots__)
 need(WatchRawCellV19.__slots__==WATCHDOG_RAW_CELL_FIELDS_V19)
 need(WatchPollerCellV19.__slots__==WATCHDOG_POLLER_CELL_FIELDS_V19)
 need(WatchReceiveFrameV19.__slots__==WATCHDOG_RECEIVE_FRAME_FIELDS_V19)
 need(CensusV19.__slots__==WATCHDOG_CENSUS_FIELDS_V19 and OfferCacheV19.__slots__==WATCHDOG_CACHE_FIELDS_V19)
 need(AcceptanceCommitV19.__slots__==WATCHDOG_ACCEPTANCE_FIELDS_V19 and ClosureCellV19.__slots__==WATCHDOG_CLOSURE_FIELDS_V19)
 need(tuple(record.record_id for record in WATCHDOG_PHYSICAL_RECORDS_V19)==tuple(range(97)))
 inherited_slots=tuple(row[0] for row in WATCHDOG_INHERITED_FIXED_SPEC_V19)
 need(len(inherited_slots)==15 and len(set(inherited_slots))==15)
 for record in WATCHDOG_PHYSICAL_RECORDS_V19:
  if record.semantic_role in inherited_slots:
   expected=next(row for row in WATCHDOG_INHERITED_FIXED_SPEC_V19 if row[0]==record.semantic_role)
   need(record.state==b"OWNED" and record.raw_fd==expected[2] and record.physical_identity is not None and len(record.physical_identity)==7 and record.access!=b"UNKNOWN")
  else:need(record.state==b"CLOSED" and record.raw_fd==-1 and record.semantic_role is None)
 need(len(WATCHDOG_OFFERED_SLOTS_V19)==13 and len(WATCHDOG_SAFE_LOCAL_SLOTS_V19)==12 and len(WATCHDOG_BLOCKING_FIXED_V19)==72)
 need(len(set(WATCHDOG_OFFERED_SLOTS_V19+WATCHDOG_SAFE_LOCAL_SLOTS_V19+WATCHDOG_BLOCKING_FIXED_V19))==97)
 need(set(WATCHDOG_OFFERED_SLOTS_V19)|set(WATCHDOG_SAFE_LOCAL_SLOTS_V19)|set(WATCHDOG_BLOCKING_FIXED_V19)==set(slot for slot,kind,transferable in LIFECYCLE_SLOT_SPEC))
 need(tuple(frame.installed_capacity for frame in (WATCHDOG_MONITORED_FRAME_V19,WATCHDOG_EXTERNAL_CONTROL_FRAME_V19,WATCHDOG_EXTERNAL_RECEIPT_FRAME_V19,WATCHDOG_REFUSAL_FRAME_V19))==(5,14,14,5))
 need(tuple(frame.semantic_capacity for frame in (WATCHDOG_MONITORED_FRAME_V19,WATCHDOG_EXTERNAL_CONTROL_FRAME_V19,WATCHDOG_EXTERNAL_RECEIPT_FRAME_V19,WATCHDOG_REFUSAL_FRAME_V19))==(4,13,13,4))
 need(len(WATCHDOG_ALL_RAW_CELLS_V19)==135 and len({id(cell) for cell in WATCHDOG_ALL_RAW_CELLS_V19})==135)
 need(tuple(frame.kernel_control_bytes for frame in (WATCHDOG_MONITORED_FRAME_V19,WATCHDOG_EXTERNAL_CONTROL_FRAME_V19,WATCHDOG_EXTERNAL_RECEIPT_FRAME_V19,WATCHDOG_REFUSAL_FRAME_V19))==tuple(count*socket.CMSG_SPACE(ctypes.sizeof(ctypes.c_int)) for count in (5,14,14,5)))
 need(WATCHDOG_GENERIC_CENSUS_V19.phase==b"EMPTY" and WATCHDOG_REFUSAL_CENSUS_V19.phase==b"EMPTY")
 need(WATCHDOG_GENERIC_OFFER_CACHE_V19.state==b"EMPTY" and WATCHDOG_GENERIC_OFFER_CACHE_V19.mode==b"GENERIC_13")
 need(WATCHDOG_REFUSAL_OFFER_CACHE_V19.state==b"EMPTY" and WATCHDOG_REFUSAL_OFFER_CACHE_V19.mode==b"ZERO_RIGHTS")
 need(WATCHDOG_REFUSAL_OFFER_CACHE_V19.frozen_wire_rows==())
 need(WATCHDOG_ACCEPTANCE_COMMIT_V19.state==b"EMPTY" and WATCHDOG_CLOSURE_CELL_V19.phase==b"NOT_STARTED")
 need(WATCHDOG_CLOSURE_CELL_V19.preclose_state==b"NOT_ATTEMPTED" and not WATCHDOG_CLOSURE_CELL_V19.preclose_send_latch)
 need(len(V19_WIRE_ROLE_SPEC)==13 and tuple(row[0] for row in V19_WIRE_ROLE_SPEC)==tuple(range(13)))
 need(len(WATCHDOG_POLLER_CELLS_V19)==2048 and all(cell.state==b"FREE" for cell in WATCHDOG_POLLER_CELLS_V19))
 need(len(CONTROL_SPEC)==40 and len(RECORD_DELTA_KINDS)==17)
 need(REFUSAL_FINALITY_NS==80000000 and REFUSAL_CLOSURE_TAIL_NS==130000000)
 need(REFUSAL_TOTAL_NS==210000000 and TRANSFER_TOTAL_NS==240000000 and FINAL_TOTAL_NS==2510000000)
 need(CONTEXT_DOMAIN==b"P27E001_V15_DETACHED_ENVELOPE_CONTEXT\x00" and AUTH_DOMAIN==b"P27E001_V15_SESSION_AUTH\x00")
 need(WATCHDOG_ENTRY_LIMIT_CERTIFIED_V19 and WATCHDOG_CURRENT_LOW_LIMIT_VECTOR_V19==(256,WATCHDOG_ENTRY_LIMIT_VECTOR_V19[1]))
 need(WATCHDOG_LIVE_HIGH_WATER_V19==len(WATCHDOG_SIMULTANEOUS_LIVE_ROLE_SET_V19)==112<256)
 need(len(WATCHDOG_CLONE3_CPYTHON_SUBCONDITIONS_V19)==6)
 soft,hard=resource.getrlimit(resource.RLIMIT_NOFILE);need((soft,hard)==WATCHDOG_CURRENT_LOW_LIMIT_VECTOR_V19)
 need(all(record.physical_identity is None or len(record.physical_identity)==7 for record in WATCHDOG_PHYSICAL_RECORDS_V19))
 need(all(record.verified_kill_leaf_identity is None or len(record.verified_kill_leaf_identity)>=7 for record in WATCHDOG_PHYSICAL_RECORDS_V19))
 return True

V15_WATCHDOG_VERIFY_PLATFORM_V19=verify_platform
def verify_platform(cert):
 result=V15_WATCHDOG_VERIFY_PLATFORM_V19(cert)
 need(cert[b"CLONE3_CPYTHON_GATE_PASS"]==b"1" and cert[b"CLONE3_CPYTHON_GATE_ID"]!=b"0"*64)
 soft,hard=resource.getrlimit(resource.RLIMIT_NOFILE)
 need(soft==256 and hard>=256 and WATCHDOG_LIVE_HIGH_WATER_V19==112)
 for value in range(256):need(int(str(value)) is value)
 return result

V15_WATCHDOG_MAIN_V19=main
def bootstrap_lifecycle_registry(context):
 for slot,kind,number,transferable in WATCHDOG_INHERITED_FIXED_SPEC_V19:
  record=lifecycle_begin_acquisition(context,slot,kind,transferable,(b"INHERITED_FIXED",number))
  record.raw_cell.c_value.value=number;lifecycle_capture_cell_v19(record,record.raw_cell)
  lifecycle_finish_adoption(context,slot)
  need(record.state==b"OWNED" and record.raw_fd==number and record.physical_identity is not None and record.access!=b"UNKNOWN")
 v19_validate_watchdog_control_surface()
 snapshot=select.poll()
 register_lifecycle_poller(context,snapshot,b"actor_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 register_lifecycle_poller(context,snapshot,b"external_owner_pidfd_fd",select.POLLIN|select.POLLHUP|select.POLLERR|select.POLLNVAL)
 context[b"offer_snapshot_poller"]=snapshot;return True

def watchdog_entry_limit_transition_v19():
 global WATCHDOG_ENTRY_LIMIT_CERTIFIED_V19,WATCHDOG_CURRENT_LOW_LIMIT_VECTOR_V19
 need(not WATCHDOG_ENTRY_LIMIT_CERTIFIED_V19)
 entry_limit_vector=resource.getrlimit(resource.RLIMIT_NOFILE)
 need(entry_limit_vector==WATCHDOG_ENTRY_LIMIT_VECTOR_V19)
 WATCHDOG_ENTRY_LIMIT_CERTIFIED_V19=True
 resource.setrlimit(resource.RLIMIT_NOFILE,(256,entry_limit_vector[1]))
 current_low_limit_vector=resource.getrlimit(resource.RLIMIT_NOFILE)
 need(current_low_limit_vector==(256,entry_limit_vector[1]))
 WATCHDOG_CURRENT_LOW_LIMIT_VECTOR_V19=current_low_limit_vector
 need(len(WATCHDOG_SIMULTANEOUS_LIVE_ROLE_SET_V19)==len(set(WATCHDOG_SIMULTANEOUS_LIVE_ROLE_SET_V19))==112)
 need(WATCHDOG_LIVE_HIGH_WATER_V19==112<256 and len(WATCHDOG_CLONE3_CPYTHON_SUBCONDITIONS_V19)==6)
 return entry_limit_vector,current_low_limit_vector

def main():
 watchdog_entry_limit_transition_v19()
 return V15_WATCHDOG_MAIN_V19()

# P27 RUNNER V20 WATCHDOG FINAL ENTRY BEGIN 20B0C802
WATCHDOG_INTERNAL_REVISION_V20=b"V20"
WATCHDOG_CANONICAL_OFFERED_ROLE_ORDER_V20=(
 b"attempt",b"attempt_base_fd",b"stage_fd",b"cgfd",b"root_events_fd",
 b"root_kill_fd",b"out_fd",b"err_fd",b"events_fd",b"outer_pidfd",
 b"cgroup_base_fd",b"actor_control_fd",b"pending_expected_raw_fd",
)
WATCHDOG_WRAPPER_MONOTONE_PHASES_V20=(
 b"NO_CONSTRUCTOR",b"CONSTRUCTOR_ALLOCATION_POSSIBLE",b"LOCAL_STRONG_REFERENCE",
 b"CONSTRUCTOR_IN_PROGRESS",b"CONSTRUCTOR_EFFECT_UNKNOWN",b"ATTACH_VERIFY_POSSIBLE",
 b"ATTACH_VERIFY_UNKNOWN",b"FILENO_INITIAL_POSSIBLE",b"FILENO_INITIAL_UNKNOWN",
 b"FILENO_REPAIR_POSSIBLE",b"FILENO_REPAIR_UNKNOWN",b"FILENO_OBSERVED_ATTACHED",
 b"FILENO_OBSERVED_DETACHED",b"DETACH_IN_PROGRESS",b"DETACH_EFFECT_UNKNOWN",
 b"DETACH_POSTCONDITION_POSSIBLE",b"DETACH_POSTCONDITION_UNKNOWN",
 b"DETACH_OBSERVED_ATTACHED",b"DETACH_RETRY_IN_PROGRESS",b"DETACH_RETRY_EFFECT_UNKNOWN",
 b"DETACH_RETRY_POSTCONDITION_POSSIBLE",b"DETACH_RETRY_POSTCONDITION_UNKNOWN",
 b"RETAINED_ATTACHED_NO_RETRY",b"DETACH_CONFIRMED",b"PROVED_CLOSED",
)

def watchdog_partial_begin_reconcile_v20(record,slot):
 number=record.raw_fd
 if number>=0:
  record.semantic_role=slot;record.state=b"CLOSE_RETRY"
  cell=record.raw_cell;cell.c_value.value=number;cell.record_id=record.record_id
  cell.epoch=record.epoch;cell.state=b"SHADOW_OF_RECORD"
  need(record.raw_fd==number and record.state==b"CLOSE_RETRY")
  return b"SOLE_RECORD_AUTHORITY_RETAINED"
 watchdog_record_reset_v19(record)
 need(record.state==b"CLOSED" and record.raw_fd==-1 and record.raw_cell.c_value.value==-1)
 return b"CLOSED_NO_EFFECT"

def lifecycle_begin_acquisition(context,slot,kind,transferable,provenance):
 record=None
 try:
  spec=watchdog_role_spec_v19(slot)
  need(spec[1]==kind and spec[2]==bool(transferable))
  record=context[b"fd_registry"][slot]
  need(record.state==b"CLOSED" and record.raw_fd==-1)
  watchdog_record_reset_v19(record)
  record.epoch+=1;record.semantic_role=slot;record.state=b"ACQUIRING"
  record.identity=None;record.physical_identity=None;record.leaf_identity=None
  record.verified_kill_leaf_identity=None;record.access=b"UNKNOWN"
  record.provenance=provenance;record.endpoint_state=b"NO_WRAPPER"
  record.wrapper_ref=None;record.detached_raw_fd=-1;record.wrapper_phase=b"NO_CONSTRUCTOR"
  record.wrapper_local_fallback=-1;record.wrapper_probe_done=False
  record.wrapper_detach_attempted=False
  cell=record.raw_cell
  need(cell.state in (b"EMPTY",b"DISARMED"))
  cell.state=b"EMPTY";cell.c_value.value=-1;cell.record_id=record.record_id;cell.epoch=record.epoch
  return record
 except BaseException:
  if record is not None:watchdog_partial_begin_reconcile_v20(record,slot)
  raise

def watchdog_wrapper_observe_v20(record,wrapper,possible,unknown):
 record.wrapper_phase=possible
 try:observed=wrapper.fileno()
 except BaseException as error:
  record.wrapper_phase=unknown
  raise OwnershipClosePending("watchdog-wrapper-fileno-effect-unknown-retained") from error
 if observed==-1:
  record.detached_raw_fd=record.raw_fd;record.endpoint_state=b"DETACHED"
  record.wrapper_phase=b"FILENO_OBSERVED_DETACHED";record.wrapper_ref=None
  return -1
 need(observed==record.raw_fd)
 record.endpoint_state=b"ATTACHED";record.wrapper_phase=b"FILENO_OBSERVED_ATTACHED"
 return observed

def watchdog_wrapper_detach_attempt_v20(record,wrapper,retry=False):
 record.wrapper_phase=b"DETACH_RETRY_IN_PROGRESS" if retry else b"DETACH_IN_PROGRESS"
 try:detached=wrapper.detach()
 except BaseException as error:
  record.wrapper_phase=b"DETACH_RETRY_EFFECT_UNKNOWN" if retry else b"DETACH_EFFECT_UNKNOWN"
  raise OwnershipClosePending("watchdog-wrapper-detach-effect-unknown-retained") from error
 need(detached==record.raw_fd)
 record.detached_raw_fd=detached;record.endpoint_state=b"DETACHED"
 record.wrapper_phase=b"DETACH_CONFIRMED";record.wrapper_ref=None
 return True

def watchdog_endpoint_repair_v19(record):
 wrapper=record.wrapper_ref
 if wrapper is None:
  if record.endpoint_state in (b"DETACHED",b"PROVED_CLOSED"):return True
  record.endpoint_state=b"NO_WRAPPER";return True
 phase=record.wrapper_phase
 if phase in (b"FILENO_REPAIR_UNKNOWN",b"DETACH_POSTCONDITION_UNKNOWN",b"DETACH_RETRY_POSTCONDITION_UNKNOWN",b"RETAINED_ATTACHED_NO_RETRY"):
  record.state=b"CLOSE_RETRY"
  raise OwnershipClosePending("watchdog-wrapper-sole-authority-retained-no-uncontrolled-retry")
 if phase==b"DETACH_EFFECT_UNKNOWN":
  observed=watchdog_wrapper_observe_v20(record,wrapper,b"DETACH_POSTCONDITION_POSSIBLE",b"DETACH_POSTCONDITION_UNKNOWN")
  if observed==-1:return True
  record.wrapper_phase=b"DETACH_OBSERVED_ATTACHED"
  return watchdog_wrapper_detach_attempt_v20(record,wrapper,True)
 if phase==b"DETACH_RETRY_EFFECT_UNKNOWN":
  observed=watchdog_wrapper_observe_v20(record,wrapper,b"DETACH_RETRY_POSTCONDITION_POSSIBLE",b"DETACH_RETRY_POSTCONDITION_UNKNOWN")
  if observed==-1:return True
  record.wrapper_phase=b"RETAINED_ATTACHED_NO_RETRY";record.state=b"CLOSE_RETRY"
  raise OwnershipClosePending("watchdog-wrapper-second-detach-observed-attached-retained")
 if phase in (b"CONSTRUCTOR_EFFECT_UNKNOWN",b"ATTACH_VERIFY_UNKNOWN",b"FILENO_INITIAL_UNKNOWN"):
  observed=watchdog_wrapper_observe_v20(record,wrapper,b"FILENO_REPAIR_POSSIBLE",b"FILENO_REPAIR_UNKNOWN")
 else:
  observed=watchdog_wrapper_observe_v20(record,wrapper,b"FILENO_INITIAL_POSSIBLE",b"FILENO_INITIAL_UNKNOWN")
 if observed==-1:return True
 return watchdog_wrapper_detach_attempt_v20(record,wrapper,False)

def watchdog_wrapper_adopt_v19(context,slot):
 record=context[b"fd_registry"][slot]
 need(record.state==b"OWNED" and record.raw_fd>=0 and record.wrapper_ref is None)
 wrapper=None;record.endpoint_state=b"NO_WRAPPER"
 record.wrapper_local_fallback=record.raw_fd;record.wrapper_phase=b"CONSTRUCTOR_ALLOCATION_POSSIBLE"
 try:
  wrapper=socket.socket.__new__(socket.socket)
  record.wrapper_ref=wrapper;record.wrapper_phase=b"LOCAL_STRONG_REFERENCE"
  record.wrapper_phase=b"CONSTRUCTOR_IN_PROGRESS"
  socket.socket.__init__(wrapper,fileno=record.raw_fd)
  record.endpoint_state=b"ATTACHED";record.wrapper_phase=b"ATTACH_VERIFY_POSSIBLE"
  observed=wrapper.fileno();need(observed==record.raw_fd)
  record.wrapper_phase=b"FILENO_OBSERVED_ATTACHED";return wrapper
 except BaseException:
  record.state=b"CLOSE_RETRY"
  if wrapper is None:
   record.wrapper_phase=b"NO_CONSTRUCTOR";record.wrapper_ref=None
  else:
   if record.wrapper_phase==b"CONSTRUCTOR_IN_PROGRESS":record.wrapper_phase=b"CONSTRUCTOR_EFFECT_UNKNOWN"
   elif record.wrapper_phase==b"ATTACH_VERIFY_POSSIBLE":record.wrapper_phase=b"ATTACH_VERIFY_UNKNOWN"
   try:watchdog_endpoint_repair_v19(record)
   except BaseException:pass
  if record.endpoint_state==b"DETACHED":
   try:close_lifecycle_fd(context,slot)
   except BaseException:pass
  raise

def v20_live_canonical_offered_slots(context):
 need(WATCHDOG_CANONICAL_OFFERED_ROLE_ORDER_V20==WATCHDOG_OFFERED_SLOTS_V19)
 result=[]
 for slot in WATCHDOG_CANONICAL_OFFERED_ROLE_ORDER_V20:
  record=context[b"fd_registry"][slot]
  if watchdog_record_live_v19(record):
   spec=watchdog_role_spec_v19(slot);need(spec[2])
   result.append(slot)
 for record in WATCHDOG_PHYSICAL_RECORDS_V19:
  if watchdog_record_live_v19(record):
   slot=watchdog_registry_slot_v19(context,record);spec=watchdog_role_spec_v19(slot)
   if spec[2]:need(slot in WATCHDOG_CANONICAL_OFFERED_ROLE_ORDER_V20)
 return tuple(result)

def ownership_transfer_keys(context):
 rows=[]
 for slot in v20_live_canonical_offered_slots(context):
  record=context[b"fd_registry"][slot]
  kind=watchdog_role_spec_v19(slot)[1]
  rows.append((kind,slot,record.raw_fd,external_identity(kind,record.raw_fd,context)))
 need(tuple(row[1] for row in rows)==v20_live_canonical_offered_slots(context))
 return tuple(rows)

def external_capabilities(control,context):
 result=ownership_transfer_keys(context)
 need(len(result)<=13)
 need(tuple(item[1] for item in result)==v20_live_canonical_offered_slots(context))
 actor=tuple(item for item in result if item[1]==b"actor_control_fd")
 pending=tuple(item for item in result if item[1]==b"pending_expected_raw_fd")
 if actor:need(len(actor)==1 and control is not None and control.fileno()==actor[0][2])
 if pending:need(actor==() or result.index(actor[0])<result.index(pending[0]))
 if context.get(b"record_pending") is not None:need(len(pending)==1)
 unique_kill_authority(context,bool(context.get(b"containment_bound")))
 return result

def v19_populate_census(context,census,phase,refusal=False):
 cache=context[b"v19_refusal_offer_cache"] if refusal else context[b"v19_generic_offer_cache"]
 mode=b"ZERO_RIGHTS" if refusal else b"GENERIC_13"
 epoch=cache.epoch;census.reset(epoch,phase,mode);leaf=v19_bind_leaf_for_kill_v19(context)
 seen=WATCHDOG_CENSUS_SEEN_V19;seen.reset(epoch)
 for record in WATCHDOG_PHYSICAL_RECORDS_V19:seen.add(record.record_id)
 need(seen.count==97)
 refusal_guard=bool(context.get(b"refusal_slot_locked") and context.get(b"actor_control_fd",-1)>=0)
 for record in WATCHDOG_PHYSICAL_RECORDS_V19:
  if record.state in (b"ACQUIRING",b"CLOSE_RETRY"):need(False)
  if watchdog_record_live_v19(record):
   lifecycle_bind_identity_v19(record)
   need(record.identity is not None and record.physical_identity is not None and record.verified_kill_leaf_identity is not None and record.access!=b"UNKNOWN")
   census.full_live.add(record.record_id);role=watchdog_registry_slot_v19(context,record)
   if refusal:
    if role==b"actor_control_fd":
     if refusal_guard:census.safe_local.add(record.record_id)
     else:census.blocking.add(record.record_id)
    elif role in WATCHDOG_OFFERED_SLOTS_V19 or role in WATCHDOG_SAFE_LOCAL_SLOTS_V19:census.safe_local.add(record.record_id)
    else:census.blocking.add(record.record_id)
   else:
    if role in WATCHDOG_OFFERED_SLOTS_V19:pass
    elif role in WATCHDOG_SAFE_LOCAL_SLOTS_V19:census.safe_local.add(record.record_id)
    else:census.blocking.add(record.record_id)
   if leaf is not None and record.verified_kill_leaf_identity==leaf and record.access in (os.O_WRONLY,os.O_RDWR):census.kill.add(record.record_id)
  if record.raw_cell.state==b"LOCAL_RAW":census.raw.add(record.record_id)
 if not refusal:
  for role in v20_live_canonical_offered_slots(context):
   census.offered.add(context[b"fd_registry"][role].record_id)
 for frame in (WATCHDOG_MONITORED_FRAME_V19,WATCHDOG_EXTERNAL_CONTROL_FRAME_V19,WATCHDOG_EXTERNAL_RECEIPT_FRAME_V19,WATCHDOG_REFUSAL_FRAME_V19):
  for cell in frame.raw_cells:
   if cell.state==b"LOCAL_RAW":census.raw.add(cell.record_id)
 need(census.blocking.count==0 and census.raw.count==0)
 if refusal:
  need(refusal_guard and census.offered.exact_tuple()==() and census.safe_local.count<=25)
 else:
  need(census.offered.exact_tuple()==tuple(context[b"fd_registry"][slot].record_id for slot in v20_live_canonical_offered_slots(context)))
  need(census.offered.count<=13 and census.safe_local.count<=12)
  need(census.kill.count==(1 if context.get(b"containment_bound") else 0))
 v19_census_digest(census);return census

try:
 main()
except BaseException:
 raise SystemExit(96)
raise SystemExit(0)
P27 RUNNER V20 WATCHDOG SOURCE END 9F20C6A3
## 19. Exact raw-span census

All six delimiter lines are unique exact full lines. Boundary-name literals inside the source are not full delimiter lines.

- Actor begin delimiter: line 455.
- Actor raw bytes: lines 456 through 3578 inclusive; 232821 bytes; 3123 LF; SHA256 c3fcb0e2b7e05b88178e74152b4abfb01de86642679796712c96978b0393296e.
- Actor end delimiter: line 3579.
- Embedded-validator begin delimiter: line 1379.
- Embedded-validator raw bytes: lines 1380 through 1789 inclusive; 38275 bytes; 410 LF; SHA256 51462a4f424667121a9b571919cc4314d2bb3400585ec92af5a180c87a0ad0b3.
- Embedded-validator end delimiter: line 1790.
- Watchdog begin delimiter: line 3581.
- Watchdog raw bytes: lines 3582 through 9007 inclusive; 432198 bytes; 5426 LF; SHA256 37d93ca0c0a9fcb34d7f3f5010b741893b1b41aacec6950add7d57a4613b8843.
- Watchdog end delimiter: line 9008.

Each raw span ends with LF and contains only LF or printable ASCII bytes. The two outer spans are separated by exactly one blank line. Extraction excludes delimiter lines and preserves every intervening byte.

## 20. Frozen source and callsite closure census

This is a raw textual census, not a parse, compile, validator run, microtest, or executability claim.

- The raw source preserves every V19 definition and adds narrowly scoped V20 last bindings or direct caller corrections. Mechanical raw-order checks bind each V20 acquisition, wrapper, canonical-order, and closure helper before its preserved main-path use. Duplicate historical definitions remain inert under ordinary final-name binding; the final raw validator selects the last definition or the exact preserved caller explicitly rather than treating function-name counts as proof.
- `v19_validate_raw_contract` deliberately has the retained V19 definition followed by one V20 final definition and one preserved actor-bootstrap call after the two raw-source hash checks. The final definition removes its own validator span before inspecting actor source, selects the actual last actor/watchdog definitions, isolates the first preserved external-transfer caller, and checks ordered structures rather than callable or count-only proxies. `v19_validate_actor_control_surface` and `v19_validate_watchdog_control_surface` retain their reachable bootstrap calls and unchanged domain/capacity checks. None was run here.
- Exactly five reachable libc receive-site wrappers have semantic/installed capacities `actor_recvmsg_site_v19` 4/5, `watchdog_monitored_recvmsg_site_v19` 4/5, `external_control_recvmsg_site_v19` 13/14, `external_receipt_recvmsg_site_v19` 13/14, and `refusal_recvmsg_site_v19` 4/5; hence the installed capacities are exactly 5/5/14/14/5. The actor wrapper reaches the actor primitive and the four watchdog wrappers reach the watchdog primitive. Each primitive begins its one try before prearm, owns syscall, first scan, and final authoritative control-byte rescan from offset zero, and completes exhaustive frame-cursor cleanup before reuse. The external-receipt path has exactly one immediate post-quarantine checkpoint before payload copy, flags, counts, carrier/history, or parse, plus later fresh precommit checks.
- The watchdog record domain is exactly 97 record ids partitioned into 13 offered permanent records, 12 unconditional safe-local records, and 72 blocking records; the three disjoint sets cover all 97 ids exactly. Its raw-cell aggregate is exactly 135: 97 record cells plus installed receive cells 5/14/14/5. The actor retains its 211-record domain plus five installed intake cells and three C-output cells. The exact simultaneous-live role derivations are actor 211+5+3=219 and watchdog 97+14+1=112, both strictly below the current soft RLIMIT_NOFILE 256; the frozen entry pair 1048576/1048576 is certified before the first descriptor producer and thereafter checked separately from current 256/1048576. These derivations and the frozen CPython cached-small-int 0 through 255 contract are CLONE3_CPYTHON subconditions and do not create a seventh gate.
- The source retains the concrete 40-row control handshake, refusal/ACK/generic-transfer/kill paths, the byte-equal 17-kind record-delta grammar, durable O_EXCL and reconciliation/report-union paths, transcript validation, and terminal-owner paths. The raw capacity/partition/census audit confirms the 13/12/72 partition and every five-site capacity. Refusal finality remains 80 ms; its nonborrowable 130 ms tail yields 210 ms total; generic transfer remains 240 ms; terminal handling remains 2510 ms.
- The only gates are CLONE3_CPYTHON, DELETED_CGROUP_FD, SEALED_SNAPSHOT_CONSTRUCTION, EXTERNAL_SURVIVAL, OUTER_RECONCILER, and ISSUER_CRYPTOGRAPHY. The complete candidate, final readiness snapshot, one atomic COMMITTED authority assignment, derived receiver-sequence mirrors, and tail-entry to the one outer no-return closure driver preserve the six-gate boundary; no seventh gate or ordinary post-ACTIVE return exists.
- Frozen authorship inputs remain exact: opening E0385 ledger dev 2431/ino 12439253869/mode 0644/nlink 1/uid 0/gid 0, 2610713 bytes/25673 LF/SHA256 3b6d0afdc98fe06abe10d4ad184d31b6557fc0097496c00d379e8ad901bf5e53; mandatory complete V19 baseline dev 2431/ino 5916037043/mode 0644/nlink 1/uid 0/gid 0, 689599 bytes/8469 LF/SHA256 17f6d4f3bed2a01d83ed3ae9f1b4466c060d06e3d6438085aa1ebb9f4d6073d6. V19 remains the immutable failed predecessor and complete V20 construction baseline.

Source/prose responsibility remains exact: the sources specify only the in-process protocol after authenticated entry. Issuer, launcher, gate, external-owner, outer-reconciler, review, manifest, and execution authority remain external and unresolved.

## 21. Author-stop boundary

The complete-file byte count, LF count, SHA256, stat identity, strict byte class, final LF, delimiter uniqueness, and terminal uniqueness are reported externally after the terminal is appended. They are not embedded as a self-hash, because a whole-file self-hash would be cyclic.

The final line is an author-stop marker only. It grants no manifest mutation, formal-review result, test, validator, build, evidence creation, reservation consumption, retry, probe, or execution authority.

BATCH07_P27_E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V20_AUTHOR_STOP
