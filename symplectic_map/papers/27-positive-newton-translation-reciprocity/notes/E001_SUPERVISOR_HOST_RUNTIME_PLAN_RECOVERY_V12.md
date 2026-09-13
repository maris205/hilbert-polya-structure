# Paper 27 E001 supervisor host runtime plan recovery V12

Status: AUTHOR-STOP CANDIDATE ONLY; NO EXECUTION AUTHORITY

## 1. Authority and effect boundary

This document is the sole Runner V12 author artifact opened by authoritative event E0375. The opening ledger terminal is:

BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V11_SUPERVISOR_PREBIND_FAIL_AND_RUNNER_V12_AUTHOR_OPEN_NO_EXECUTION

E0375 authorizes only construction of this exact plan file. It does not authorize importing, tokenizing, parsing as a programming language, compiling, evaluating, launching, testing, validating, probing, building, retrying, consuming a reservation, creating evidence, changing a manifest, or changing any other file. The two embedded programs and the embedded transcript validator are inert ASCII source text in this artifact.

The intended future operation is one no-build, one-shot Host V15 probe. This plan is not that operation. Every launcher, issuer, environment, kernel, filesystem, timing, external-owner, and reconciliation premise below must be independently established after author stop. Failure to establish any premise is a closed, no-execution result.

Author-stop is not a claim that the source is executable. No source in this file was imported, tokenized, language-parsed, compiled, evaluated, executed, launched, or microtested during authorship.

## 2. Frozen normative carriers

A future prebind review must authenticate all of these as held carriers, not as path names:

- E0366 snapshot: 2303269 bytes, 23672 LF, SHA256 0ea4f324c5175ec196b8118e551a429a6207cd57bacfdaa9903a109046daab92, with its exact unique terminal bound in both programs.
- Host Probe Recovery V15: 228310 bytes, 4622 LF, SHA256 a27eb1bb5540c18b57094ee26724be75a0c431b3c523385fe1271fb02378b845, final-LF ASCII, and its exact unique V15 author-stop terminal.
- Normative Host Probe V8 digest: 72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf.
- Frozen Runner V4 historical input: 248620 bytes, 3422 LF, SHA256 a11d80da1d5cffa2ac973cfe13d39340c587c87bbddaaa4d3d46640350e5ef83.
- Frozen actor source below: 144471 bytes, 1692 LF, SHA256 bf2e61290cae71f5191b73331d342cd29ae7577efc4f759ffd8021554a218202.
- Frozen watchdog source below: 274030 bytes, 3042 LF, SHA256 204f9b1aee30c301635fb459356c62778bfaa51f736425890c6ec3fc20299dd7.
- Frozen embedded validator inside the actor source: 10195 bytes, 102 LF, SHA256 7414e09dcdd09463f900a24dc19af9d3ecc9528c44895541fba7739fd7af9a89.
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
- 103 sealed complete V12 plan.
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
- 7 certificate; 8 final envelope; 9 E0366 snapshot; 10 V12 plan; 11 actor source; 12 linked frozen O_RDONLY/nlink-one Host V15; 13 reservation.
- 14 external-owner control; 15 external-owner pidfd; 16 external-owner manifest.
- 100 sealed watchdog source.

Any extra descriptor, wrong access mode, wrong owner/type/nlink/seal, wrong size/hash, nonempty stdin, wrong cwd, wrong environment, or carrier mismatch is a pre-action closed failure. Mutation-capable bases are individually owned and either closed or explicitly transferred; parent exceptions after fork retain and exactly reap or durably transfer watchdog ownership.

## 5. Acyclic issuer construction

The issuer construction is deliberately one-way and has no whole-hash fixed point.

1. Build the canonical detached envelope-context payload from the 15 ENVELOPE_CONTEXT_KEYS plus its exact end line. It excludes certificate bytes, certificate digest, every signature and signature-preimage hash, the issuer receipt, final-envelope digest, reservation bytes, and session AUTH. Its preimage is exactly `P27E001_V12_DETACHED_ENVELOPE_CONTEXT || NUL || ENVELOPE_CONTEXT_RAW=<decimal byte length> || LF || payload`; its SHA256 is ISSUER_CONTEXT_SHA256 in the certificate.
2. Construct the certificate once. It contains no later-object hash, signature, receipt, self-hash, final-envelope digest, reservation digest, or AUTH. CERTIFICATE_DIGEST_SHA256 is exactly SHA256 of `P27E001_V12_CERTIFICATE_DIGEST || NUL || CERTIFICATE_RAW=<decimal byte length> || LF || certificate bytes`.
3. Form the final-envelope TBS payload from the detached context plus ENVELOPE_CONTEXT_SHA256, CERTIFICATE_DIGEST_SHA256, SIGNATURE_ALGORITHM, and its exact end line. First wrap that payload as `P27E001_V12_ENVELOPE_TBS || NUL || ENVELOPE_TBS_RAW=<length> || LF || payload`. Then form the issuer-signature payload from separately length-framed CERTIFICATE_RAW and ENVELOPE_TBS plus its end line, and wrap the whole payload as `P27E001_V12_ISSUER_SIGNATURE_PREIMAGE || NUL || ISSUER_SIGNATURE_TBS_RAW=<length> || LF || payload`.
4. Append SIGNATURE_PREIMAGE_SHA256, SIGNATURE_ALGORITHM, and SIGNATURE_HEX. The issuer receipt is one `ISSUER_RECEIPT_TBS_RAW` length frame under the P27E001_V12_ISSUER_RECEIPT NUL domain and binds the exact context digest, certificate digest, signature-preimage digest, algorithm, signature, and end line. Append ISSUER_RECEIPT_SHA256. FINAL_ENVELOPE_DIGEST_SHA256 is exactly SHA256 of the P27E001_V12_FINAL_ENVELOPE NUL domain followed by one `FINAL_ENVELOPE_RAW` length frame containing every final-envelope byte.
5. Construct the ordered 10-field reservation payload from issuer identity/key/serial, certificate digest, final-envelope digest, validity interval, reserved=1, consumed=0, and Ed25519. Wrap it as one `RESERVATION_TBS_RAW` length frame under the P27E001_V12_RESERVATION_TBS NUL domain. The reservation signature and receipt each use their own NUL domain plus exactly one outer length frame; the signature payload contains the nested RESERVATION_TBS frame, and the receipt payload binds that TBS, signature-preimage hash, algorithm, signature, and exact end line. Only then append RESERVATION_DIGEST_SHA256.
6. Compute session AUTH only after all three immutable carriers exist. Its payload is the ordered concatenation of `CERTIFICATE_RAW`, `FINAL_ENVELOPE_RAW`, and `RESERVATION_RAW` length frames; AUTH is SHA256 of `P27E001_V12_SESSION_AUTH || NUL || AUTH_TBS_RAW=<payload length> || LF || payload`. Labels, decimal lengths, NUL domains, order, and end lines are part of the bytes and admit no implicit concatenation.

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

Ancillary data is closed before any malformed result is reported. Wrong rights count/type, truncation, control bytes, sequence, sender, receiver state, slot, probe, effect, deadline, or packet digest is CONTROL_MALFORMED before action. CONTROL_LOST is only channel state. SEND_EFFECT_UNKNOWN is only send state. PIDFD_ACTOR_LOST is only actor state and can be established only from fd 4 readiness. POLLIN is drained before HUP/ERR classification. Control loss never proves actor loss and never satisfies owner-release predicates.

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

The watchdog owns cgroup and payload lifetime. cgroup descriptors for type, controllers, subtree_control, events, kill, and root are immediately registered in exhaustive cleanup scopes. Containment is not considered bound until exact identity, access, cgroup topology, singleton population, pidfd/starttime, stopped state, and actor/control acknowledgements agree.

The suite is exactly 15 slots in this order:

P00, P01D, P01C, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12, P13

P00 reconstructs its synthetic transcript bytes exactly before checking SHA256. P01D yields exactly 13 fields and P01C receives the exact relation, including index 9. P05 uses pidfd plus stable starttime and rejects PID reuse. Topology claims are limited to complete transcript observations and do not claim unobserved global process ancestry.

For each slot, stream rights and pidfd rights enter exhaustive local owner scopes immediately and transfer individually only at commit. Release requires the durable release record, exact packet binding, cgroup membership, stopped observation, pidfd/starttime relation, and boundary checks before and after SIGCONT. The release record and reply use the one carried origin; release cannot be retried.

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

All resource acquisitions occur inside immediate typed owner stacks. On possible payload release, the first failure consumes the sole safe kill authority even when an instantaneous population observation is empty. The kill ticket, cgroup.kill call, return, and postcheck all fit within one inherited cleanup cap with resampled clocks. There is at most one kill ticket and one kill call; no retry exists.

The watchdog runs one terminal_owner_loop. It continuously polls actor pidfd, actor control, containment, and pending terminal packets; drains POLLIN before HUP; and retains every owner descriptor through success, failure, send uncertainty, control loss, and actor loss. No generic finally releases owner descriptors.

The loop exits only through one of these exact predicates:

- complete durable terminal-seen, report, PASS if applicable, ACK, actor receipt, no-replay reconciliation, OWNER_CLOSURE, closure packet, safe containment, and watchdog exit handshake;
- pidfd-proved actor loss plus durable outcome, safe containment, durable no-replay ACK-receipt/reconciliation/OWNER_CLOSURE chain; or
- the frozen external transfer protocol below.

Post-deadline observation is outside certified effects. It cannot create a record, issue kill, accept PASS, infer empty, or release ownership. It can terminate only through a real prebound external transfer.

## 15. External owner transfer

External transfer is not a Boolean escape hatch. Before entry, the certificate binds an independently alive owner PID, stable starttime, uid/gid, pidfd, SOCK_SEQPACKET endpoint, manifest size/hash, maximum packet, rights types, signature policy, and monotone receipt service.

A transfer offer binds AUTH, sequence, predecessor, reason, current terminal subject, chain head, outcome durability, actor/control/send states, attempt/collision/base-closed/commit/intent facts, exact rights count, and a manifest of each fstat/access identity. If a record remains pending, the offer additionally binds its exact sequence, predecessor, entry name, expected byte length, expected raw SHA256, and the complete length-framed typed semantic delta with its SHA256; the expected raw bytes travel only in an anonymous O_RDWR, nlink-zero, exactly sealed carrier whose identity also binds the delta digest. SCM_RIGHTS may include only the enumerated attempt, attempt-base, stage, cgroup, stream, events, kill, outer-pidfd, cgroup-base, actor-control, and pending-expected-raw capabilities. Each local right remains owned until exact ACCEPTED.

Acceptance must bind the offer SHA256, exact sequence and predecessor, durable receipt SHA256, issuer signature, no-replay flag, receiver PID/starttime, receiver liveness, and independent carrier identity. Only then may rights transfer individually and local ownership close. An unknown offer/acceptance effect remains owned and cannot release resources.

The dedicated refusal slot, not an external offer, is installed before the first post-validation fallible action. REFUSAL_CLOSE_OFFER remains nonexistent until the same slot reaches exact receipt finality or pidfd-loss/control-EOF finality. The receipt-final branch also requires known CLOSED_NO_CONSUME with a cached ACK; the loss/EOF branch retains the exact earlier ACK/close variant without fabrication. Its immutable contract covers the sequence, predecessor, exact request, close state, schedule, deadline, ACK bytes and sequence (including exact empty/zero), final authoritative receipt state, finality evidence, and final slot digest. Fallible contract and offer construction may be repeated only while no offer exists and always reserve the same external sequence; once exact offer bytes are frozen neither slot nor offer can change. The possible-send flag is set before activating that reserved packet, so there is at most one possible external send and never a resend. All post-lock recovery, including late actor receipt capture, remains on this slot; OWNER_POLL cannot consume it as an unrelated packet, generic TRANSFER_OFFER is unreachable, and external acceptance rechecks finality before release.

Collision uses the same exact transfer machinery or a separately durable independent receipt; there is no dead collision grammar. Refusal uses a dedicated durable issuer receipt and closure chain. Actor-loss also produces durable no-replay reconciliation and OWNER_CLOSURE. There is no replay after any uncertain effect.

## 16. Outer launcher obligations

The embedded sources cannot establish their own initial authority. A future outer launcher must, before any source interpretation:

- obtain explicit ledger authority naming this exact final V12 identity;
- verify author-stop, both separated formal reviews, all six gates, issuer key/serial/expiry, and one-shot reservation freshness;
- construct every sealed carrier without path substitution and authenticate every fd;
- establish clean argv, env, cwd, umask, signal, timer, FD, namespace, mount, cgroup, and no-mutator state;
- start a new process group/session or stronger containment that covers all descendants;
- retain pidfds/cgroup kill and external-owner capabilities, independently drain both output streams, and use one absolute watchdog deadline;
- distinguish pre-send, send-effect-unknown, consumed, terminal, reconciled, and owner-closed states;
- never kill only the top process, truncate output, infer timeout from missing text, retry after uncertain effect, or touch any build/evidence/root.

These are outer-launcher obligations, not intrinsic V15 guarantees. Intrinsic V15 guarantees are limited to the exact behavior proved from its frozen source and complete transcript under its stated inputs. Containment, carrier creation, issuer authority, clean entry, durable records, deadlines, drainage, descendant cleanup, reconciliation, and no replay are supplied by this Runner protocol and its future launcher.

## 17. Review separation and manifest eligibility

After this author stop, one fresh supervisor-prebind review must first check exact bytes, line counts, hashes, delimiters, source/prose agreement, certificate constructibility, unresolved gates, and the no-execution boundary. Its prospective ledger outcomes are:

- pass/open: BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V12_SUPERVISOR_PREBIND_PASS_AND_DUAL_FORMAL_REVIEW_OPEN_NO_EXECUTION
- fail/closed: BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V12_SUPERVISOR_PREBIND_FAIL_NO_EXECUTION

Only a prebind pass may open two separated formal scopes, performed by fresh reviewers not involved in V12 authorship or prebind:

- Source/certificate/parser formal scope: extraction and seals; one-way issuer construction; certificate/envelope/reservation/AUTH; fd and ancillary grammar; P00/P01D/P01C/P05; RESULT; complete transcript; report/candidate/source/prose census.
- Lifecycle/containment/durability formal scope: fork ownership; control/actor/send orthogonality; refusal; carried consumption/release horizons; cgroup and pidfd/starttime; cleanup and one-kill lane; all absolute schedules; terminal owner loop; reconciliation; external transfer; no replay.

The two reports must be separately sealed and cannot substitute for each other. The prospective combined ledger outcomes are:

- pass/closed: BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V12_DUAL_FORMAL_REVIEW_PASS_NO_EXECUTION
- fail/closed: BATCH07_P27_PROBE_RECOVERY_E001_HOST_V15_RUNNER_V12_DUAL_FORMAL_REVIEW_FAIL_NO_EXECUTION

Even a dual pass grants no execution. Manifest eligibility remains false until the exact final V12 identity, prebind pass, both formal passes, all six current gate receipts, issuer materials, external owner, outer reconciler, and a later explicit immutable ledger event independently grant manifest binding and execution. No event in this file can self-authorize that transition.

## 18. Embedded source boundaries

The next outer span is the frozen actor source. It contains the frozen validator as an inner raw span. The later outer span is the frozen watchdog source. Exact boundary lines and source census are recorded after both spans. The bytes between boundaries are inert raw text.
P27 RUNNER V12 ACTOR SOURCE BEGIN C5A91E34
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
CONTEXT_DOMAIN=b"P27E001_V12_DETACHED_ENVELOPE_CONTEXT\x00"
CERTIFICATE_DOMAIN=b"P27E001_V12_CERTIFICATE_DIGEST\x00"
ENVELOPE_TBS_DOMAIN=b"P27E001_V12_ENVELOPE_TBS\x00"
SIGNATURE_DOMAIN=b"P27E001_V12_ISSUER_SIGNATURE_PREIMAGE\x00"
RECEIPT_DOMAIN=b"P27E001_V12_ISSUER_RECEIPT\x00"
RESERVATION_TBS_DOMAIN=b"P27E001_V12_RESERVATION_TBS\x00"
RESERVATION_SIGNATURE_DOMAIN=b"P27E001_V12_RESERVATION_SIGNATURE\x00"
RESERVATION_RECEIPT_DOMAIN=b"P27E001_V12_RESERVATION_RECEIPT\x00"
FINAL_ENVELOPE_DOMAIN=b"P27E001_V12_FINAL_ENVELOPE\x00"
AUTH_DOMAIN=b"P27E001_V12_SESSION_AUTH\x00"
EXTERNAL_ACCEPTANCE_DOMAIN=b"P27E001_V12_EXTERNAL_ACCEPTANCE\x00"
ISSUER_KEY_BIND_DOMAIN=b"P27E001_V12_ISSUER_KEY_BIND\x00"
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
  current=os.open(b"/",O_DIR)
  for part in path.split(b"/")[1:]:
   need(part not in (b"",b".",b".."))
   following=os.open(part,O_DIR,dir_fd=current);os.close(current);current=following;following=-1
  held=os.fstat(current)
  need(stat.S_ISDIR(held.st_mode) and held.st_uid==held.st_gid==0 and held.st_mode&0o022==0)
  result=current;current=-1;return result
 finally:close_numbers(tuple(x for x in (following,current) if x>=0))

def open_under(rootfd,path):
 need(path.startswith(b"/") and b"\x00" not in path)
 parts=path.split(b"/")[1:];need(parts and all(x not in (b"",b".",b"..") for x in parts))
 current=following=-1
 try:
  current=os.dup(rootfd)
  for part in parts[:-1]:
   following=os.open(part,O_DIR,dir_fd=current);os.close(current);current=following;following=-1
  return os.open(parts[-1],os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=current)
 finally:close_numbers(tuple(x for x in (following,current) if x>=0))

def mount_id(number):
 info=-1
 try:
  info=os.open(b"/proc/self/fdinfo/"+str(number).encode(),os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=read_all(info,4096)
 finally:close_numbers(tuple(x for x in (info,) if x>=0))
 values=[x[7:] for x in raw.splitlines() if x.startswith(b"mnt_id:\t")]
 need(len(values)==1);return udec(values[0],1)

def mount_line(number):
 wanted=mount_id(number);info=-1
 try:
  info=os.open(b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(info,1048576),1048576)
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
  number=os.open(name,os.O_RDWR|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC|os.O_NOFOLLOW,0o400,dir_fd=directory)
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
  number=os.open(name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=directory)
  progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS));held=os.fstat(number);again=read_all(number,identity[0])
  need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_nlink==1 and held.st_uid==held.st_gid==0)
  need(meta(again)==identity);progress(CERT,deadline,horizon_needed(deadline,POST_STAGE_REMAIN_NS))
 finally:close_numbers(tuple(x for x in (number,) if x>=0))

def memfd(raw,label):
 number=-1
 try:
  number=os.memfd_create(label,os.MFD_CLOEXEC|os.MFD_ALLOW_SEALING)
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
 body=b"P27E001_ISSUER_CONTEXT_V12\n"
 for key in ENVELOPE_CONTEXT_KEYS:body+=key+b"="+values[key]+b"\n"
 return domain_frame(CONTEXT_DOMAIN,b"ENVELOPE_CONTEXT_RAW",body+b"CONTEXT_END=1\n")

def envelope_tbs(values,certificate_digest):
 body=b"P27E001_ISSUER_ENVELOPE_TBS_V12\n"
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
 values=parse_fixed(raw,b"P27E001_ISSUER_ENVELOPE_V12",ENVELOPE_KEYS,b"ENVELOPE_END=1")
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V12",b"E0366_SNAPSHOT_BYTES":str(SNAPSHOT_EXPECT[0]).encode(),b"E0366_SNAPSHOT_LF":str(SNAPSHOT_EXPECT[1]).encode(),b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"V15_SHA256":WHOLE_V15[8],b"ONE_SHOT_RESERVED_BY_ISSUER":b"1",b"ONE_SHOT_CONSUMED_BY_ISSUER":b"0",b"SIGNATURE_ALGORITHM":b"ED25519_EXTERNAL_GATE_V12"}
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
 body=b"P27E001_ISSUER_RESERVATION_TBS_V12\n"
 for key in RESERVATION_TBS_KEYS:body+=key+b"="+values[key]+b"\n"
 return domain_frame(RESERVATION_TBS_DOMAIN,b"RESERVATION_TBS_RAW",body+b"RESERVATION_TBS_END=1\n")

def reservation_signature_preimage(tbs):
 payload=length_frame(b"RESERVATION_TBS",tbs)+b"RESERVATION_SIGNATURE_PREIMAGE_END=1\n"
 return domain_frame(RESERVATION_SIGNATURE_DOMAIN,b"RESERVATION_SIGNATURE_TBS_RAW",payload)

def reservation_receipt_preimage(tbs,signature_digest,algorithm,signature):
 payload=length_frame(b"RESERVATION_TBS",tbs)+b"SIGNATURE_PREIMAGE_SHA256="+signature_digest+b"\nSIGNATURE_ALGORITHM="+algorithm+b"\nSIGNATURE_HEX="+signature+b"\nRESERVATION_RECEIPT_END=1\n"
 return domain_frame(RESERVATION_RECEIPT_DOMAIN,b"RESERVATION_RECEIPT_TBS_RAW",payload)

def parse_reservation(raw):
 values=parse_fixed(raw,b"P27E001_ISSUER_RESERVATION_V12",RESERVATION_KEYS,b"RESERVATION_END=1")
 need(values[b"ISSUER_ID"]==b"P27_HOST_PREMISE_ISSUER_V12" and values[b"ONE_SHOT_RESERVED_BY_ISSUER"]==b"1" and values[b"ONE_SHOT_CONSUMED_BY_ISSUER"]==b"0",Refuse)
 need(values[b"SIGNATURE_ALGORITHM"]==b"ED25519_EXTERNAL_GATE_V12",Refuse)
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
 need(lines and lines[0]==b"P27E001_PREMISE_CERTIFICATE_V12" and lines[-1]==b"CERTIFICATE_END=1",Refuse)
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
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V12",b"ARCH":b"x86_64",b"ABSOLUTE_LIFETIME_NS":b"360000000000",b"REALTIME_MONOTONIC_MAX_DRIFT_NS":b"1000000",b"E0366_SNAPSHOT_BYTES":b"2303269",b"E0366_SNAPSHOT_LF":b"23672",b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"HISTORICAL_SNAPSHOT_SEALED":b"1",b"V15_SHA256":WHOLE_V15[8],b"V8_SHA256":V8_SHA,b"ACTOR_ENTRY_CAPS":b"00000000000401c0",b"ACTOR_ENTRY_NNP":b"0",b"ACTOR_ENTRY_SECUREBITS":b"12",b"PAYLOAD_FINAL_CAPS":b"0000000000000000",b"PAYLOAD_FINAL_NNP":b"1",b"PAYLOAD_FINAL_SECUREBITS":b"15",b"ATTEMPT_BASE_MODE":b"40700",b"ATTEMPT_BASE_UID":b"0",b"ATTEMPT_BASE_GID":b"0",b"CGROUP2_FS_MAGIC":b"63677270",b"CGROUP_BASE_UID":b"0",b"CGROUP_BASE_GID":b"0",b"CGROUP_NO_EXTERNAL_MUTATOR":b"1",b"CGROUP_CHILD_MODE":b"40700",b"CGROUP_CHILD_UID":b"0",b"CGROUP_CHILD_GID":b"0",b"CGROUP_CHILD_TYPE_HEX":b"646f6d61696e0a",b"RUNTIME_ROOT_UID":b"0",b"RUNTIME_ROOT_GID":b"0",b"SAFE_BIND_MODE":b"40700",b"SAFE_BIND_UID":b"0",b"SAFE_BIND_GID":b"0",b"SAFE_BIND_NOEXEC":b"1",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT":b"1",b"KEEPER_BYTES":b"4216",b"KEEPER_LF":b"128",b"KEEPER_SHA256":b"e3bf14ddde012be70a0ec40ac9373c055d2fd79d3ea30aa5e64450174f057716",b"LAUNCHER_BYTES":b"4218",b"LAUNCHER_LF":b"128",b"LAUNCHER_SHA256":b"e9d5eb3544dfddd7251279294e113f053165c2d446dd4517fbcdc6927a8618d5",b"MARKER_BYTES":b"75094",b"MARKER_LF":b"1479",b"MARKER_SHA256":b"b06ceed041004279e9df73cc9cc3c2d73ec07d8f71a9345f451a32e93b7a955d",b"CHILD_BYTES":b"19746",b"CHILD_LF":b"452",b"CHILD_SHA256":b"1d20310b965ff9df9351cbc3ca07aebb15e8cbacf74a8058782c085fde0780bf",b"PYTHON_IMAGE_SHA256":PY_SHA,b"PYTHON_IMAGE_BYTES":b"30626264",b"PYTHON_IMAGE_UID":b"0",b"PYTHON_IMAGE_GID":b"0",b"LIBC_UID":b"0",b"LIBC_GID":b"0",b"PRECONSUMPTION_CAP_NS":b"10000000000",b"CONSUMPTION_PROGRESS_NS":b"250000000",b"ATTEMPT_DIRFD_PROGRESS_NS":b"100000000",b"STAGING_CAP_NS":b"10000000000",b"RELEASE_PROGRESS_NS":b"1000000000",b"RELEASE_RECORD_ABSOLUTE_OFFSET_NS":b"800000000",b"RELEASE_REPLY_ABSOLUTE_OFFSET_NS":b"900000000",b"SIGCONT_CALL_RETURN_NS":b"5000000",b"DURABLE_RECORD_PROGRESS_NS":b"100000000",b"WATCHDOG_ARM_PROGRESS_NS":b"1000000000",b"WATCHDOG_ACK_PROGRESS_NS":b"500000000",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT":b"1",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY":b"1",b"CGROUP_KILL_WRITE_RETURN_NS":b"5000000",b"CGROUP_KILL_TO_EMPTY_NS":b"2000000000",b"FINAL_REPORT_PROGRESS_NS":b"1000000000",b"FINAL_PASS_COMMIT_PROGRESS_NS":b"100000000",b"FINAL_PASS_MARGIN_NS":b"10000000",b"TERMINAL_HANDSHAKE_PROGRESS_NS":b"500000000",b"A_RECEIPT_PROGRESS_NS":b"100000000",b"B_CLOSURE_PROGRESS_NS":b"500000000",b"TERMINAL_CANDIDATE_RECORD_NS":b"100000000",b"TERMINAL_NOTICE_PROGRESS_NS":b"100000000",b"TERMINAL_SEEN_RECORD_NS":b"100000000",b"TERMINAL_ACK_RECEIPT_RECORD_NS":b"100000000",b"TERMINAL_RECONCILIATION_RECORD_NS":b"100000000",b"TERMINAL_OWNER_CLOSURE_RECORD_NS":b"100000000",b"TERMINAL_CLOSURE_PACKET_NS":b"100000000",b"TERMINAL_B_EXIT_NS":b"100000000",b"FAILURE_OVERALL_PROGRESS_NS":b"5210000000",b"FAILURE_CLEANUP_EFFECT_PROGRESS_NS":b"2600000000",b"FAILURE_TAIL_RESERVE_NS":b"2610000000",b"REFUSAL_RECORD_PROGRESS_NS":b"20000000",b"REFUSAL_ACK_PROGRESS_NS":b"20000000",b"REFUSAL_RECEIPT_WAIT_PROGRESS_NS":b"30000000",b"REFUSAL_FINALITY_COMMIT_PROGRESS_NS":b"10000000",b"REFUSAL_FINALITY_DEADLINE_PROGRESS_NS":b"80000000",b"REFUSAL_OFFER_BUILD_PROGRESS_NS":b"10000000",b"REFUSAL_OFFER_SEND_PROGRESS_NS":b"20000000",b"REFUSAL_ACCEPTANCE_RECV_PROGRESS_NS":b"30000000",b"REFUSAL_ACCEPTANCE_VERIFY_PROGRESS_NS":b"20000000",b"REFUSAL_ACCEPTANCE_COMMIT_PROGRESS_NS":b"10000000",b"REFUSAL_ACTOR_CLOSURE_PROGRESS_NS":b"20000000",b"REFUSAL_CAPABILITY_CLOSE_PROGRESS_NS":b"10000000",b"REFUSAL_OWNER_RELEASE_PROGRESS_NS":b"10000000",b"REFUSAL_CLOSURE_TAIL_NS":b"130000000",b"REFUSAL_CLOSURE_DEADLINE_PROGRESS_NS":b"210000000",b"FINAL_TERMINAL_TOTAL_NS":b"2510000000",b"ENTRY_MIN_REMAINING_NS":b"295482000000",b"CONSUMPTION_MIN_REMAINING_NS":b"285482000000",b"PRE_STAGE_MIN_REMAINING_NS":b"285232000000",b"POST_STAGE_MIN_REMAINING_NS":b"275232000000",b"POST_CONTAIN_MIN_REMAINING_NS":b"274732000000",b"ACTOR_RELEASE_DISABLE_PROGRESS_NS":b"500000000",b"EXTERNAL_OWNER_UID":b"0",b"EXTERNAL_OWNER_GID":b"0",b"CLONE3_CPYTHON_GATE_PASS":b"1",b"DELETED_CGROUP_FD_GATE_PASS":b"1",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_PASS":b"1",b"EXTERNAL_SURVIVAL_GATE_PASS":b"1",b"OUTER_RECONCILER_GATE_PASS":b"1",b"ISSUER_CRYPTOGRAPHY_GATE_PASS":b"1"}
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
  boot=os.open(b"/proc/sys/kernel/random/boot_id",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);boot_raw=read_all(boot,128)
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
  current=os.dup(rootfd)
  for part in parts[:-1]:
   following=os.open(part,O_DIR,dir_fd=current);os.close(current);current=following;following=-1
  if role==b"PYTHON_LINK":
   held=os.stat(parts[-1],dir_fd=current,follow_symlinks=False);need(stat.S_ISLNK(held.st_mode),Refuse)
   target=os.readlink(parts[-1],dir_fd=current);size=len(target);digest=sha(target)
  else:
   number=os.open(parts[-1],os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=current)
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

def cap_status():
 number=-1
 try:
  number=os.open(b"/proc/self/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(number,65536),65536)
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
  root=os.open(b"/",O_DIR)
  tmp=os.open(b"tmp",O_DIR,dir_fd=root);base=os.open(b"p27-e001-host-v15",O_DIR,dir_fd=tmp)
  cwd=os.dup(base) if cwd_name is None else os.open(cwd_name,O_DIR,dir_fd=base)
  held=os.fstat(cwd);need((held.st_dev,held.st_ino,held.st_uid,held.st_gid,stat.S_IMODE(held.st_mode))==(safe_dev,safe_ino,0,0,0o700))
  os.fchdir(cwd)
 finally:
  for number in (locals().get("cwd",-1),locals().get("base",-1),locals().get("tmp",-1),root):
   if number>=0:
    try:os.close(number)
    except OSError:pass
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
  for source,target in mapping:
   number=fcntl.fcntl(source,fcntl.F_DUPFD_CLOEXEC,200)
   need(number>=200 and number not in targets and number not in [x[0] for x in parked])
   parked.append((number,target));number=-1
  for held,target in parked:os.dup2(held,target,inheritable=True)
 finally:
  close_numbers(tuple(x for x in (number,) if x>=0))
  for held,target in parked:
   try:os.close(held)
   except OSError:pass

# P27 RUNNER V12 EMBEDDED VALIDATOR BEGIN D5B40A72
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
# P27 RUNNER V12 EMBEDDED VALIDATOR END D5B40A72

CONTROL_SPEC={
 b"V12_ABORT":(b"ABORTING",b"*",b"ABORT_NOTICE",b"control_deadline_ns"),
 b"V12_READY":(b"READY",b"WAIT_READY",b"NO_EFFECT",b"ready_deadline_ns"),
 b"V12_REFUSE_PREBEGIN":(b"REFUSE_PREBEGIN",b"WAIT_BEGIN",b"NO_CONSUME_REFUSAL",b"consume_deadline_ns"),
 b"V12_REFUSE_POSTARM":(b"REFUSE_POSTARM",b"WAIT_COMMIT",b"NO_CONSUME_REFUSAL",b"consume_deadline_ns"),
 b"V12_REFUSE_ACK":(b"REFUSAL_CLOSED_NO_CONSUME",b"WAIT_REFUSAL_ACK",b"REFUSAL_ACK_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V12_REFUSE_ACK_RECEIPT":(b"REFUSAL_ACK_RECEIVED",b"WAIT_REFUSAL_RECEIPT",b"NO_REPLAY_RECEIPT",b"consume_deadline_ns"),
 b"V12_REFUSAL_CLOSED":(b"REFUSAL_DURABLY_CLOSED",b"WAIT_REFUSAL_CLOSED",b"OWNER_CLOSURE",b"consume_deadline_ns"),
 b"V12_CONSUME_BEGIN":(b"CONSUME_BEGIN",b"WAIT_BEGIN",b"BEGIN_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V12_CONSUME_ARMED":(b"CONSUME_ARMED",b"WAIT_ARM",b"ARM_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V12_CONSUME_COMMIT":(b"CONSUME_COMMIT",b"WAIT_COMMIT",b"COMMIT_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V12_CONSUMED_DURABLE":(b"CONSUMED_DURABLE",b"WAIT_CONSUMED",b"INTENT_DURABLE",b"consume_deadline_ns"),
 b"V12_STAGE_DURABLE":(b"STAGE_DURABLE",b"WAIT_STAGE",b"FD_TRANSFER",b"stage_deadline_ns"),
 b"V12_STAGE_ACK":(b"STAGE_BOUND",b"WAIT_STAGE_ACK",b"STAGE_VERIFIED",b"stage_deadline_ns"),
 b"V12_CONTAINMENT":(b"CONTAINMENT_CANDIDATE",b"WAIT_CONTAINMENT",b"FD_TRANSFER",b"contain_deadline_ns"),
 b"V12_CONTAINMENT_ACK":(b"CONTAINMENT_BOUND",b"WAIT_CONTAINMENT_ACK",b"CONTAINMENT_VERIFIED",b"contain_deadline_ns"),
 b"V12_STREAM_ARM":(b"STREAM_ARM",b"WAIT_STREAM_ARM",b"FD_TRANSFER",b"launch_deadline_ns"),
 b"V12_STREAMS_ARMED":(b"STREAMS_ARMED",b"WAIT_STREAMS_ARMED",b"FD_VERIFIED",b"launch_deadline_ns"),
 b"V12_PIDFD_ARM":(b"PIDFD_ARM",b"WAIT_PIDFD_ARM",b"FD_TRANSFER",b"launch_deadline_ns"),
 b"V12_PIDFD_ARMED":(b"PIDFD_ARMED",b"WAIT_PIDFD_ARMED",b"PIDFD_VERIFIED",b"launch_deadline_ns"),
 b"V12_RELEASE_CANDIDATE":(b"RELEASE_CANDIDATE",b"WAIT_RELEASE",b"RELEASE_AUTHORIZATION",b"launch_deadline_ns"),
 b"V12_RELEASE_DURABLE":(b"RELEASE_DURABLE",b"WAIT_RELEASE_DURABLE",b"RELEASE_RECORD_DURABLE",b"launch_deadline_ns"),
 b"V12_RESULT":(b"RESULT",b"WAIT_RESULT",b"RESULT_NOTICE",b"result_deadline_ns"),
 b"V12_RESULT_FRAME":(b"RESULT_FRAME",b"WAIT_RESULT_FRAME",b"RESULT_FRAME",b"result_deadline_ns"),
 b"V12_RESULT_END":(b"RESULT_END",b"WAIT_RESULT_END",b"RESULT_COMPLETE",b"result_deadline_ns"),
 b"V12_VALIDATED_CANDIDATE":(b"VALIDATED_CANDIDATE",b"WAIT_VALIDATED",b"VALIDATION_NOTICE",b"ack_deadline_ns"),
 b"V12_VALIDATED_DURABLE":(b"VALIDATED_DURABLE",b"WAIT_VALIDATED_DURABLE",b"VALIDATED_RECORD_DURABLE",b"ack_deadline_ns"),
 b"V12_ACK_COMMIT_INTENT":(b"ACK_COMMIT_INTENT",b"WAIT_ACK_INTENT",b"ACK_COMMIT",b"ack_deadline_ns"),
 b"V12_COMMITTED":(b"COMMITTED",b"WAIT_COMMITTED",b"COMMIT_RECORD_DURABLE",b"ack_deadline_ns"),
 b"V12_COMMITTED_SEEN":(b"COMMITTED_SEEN",b"WAIT_COMMITTED_SEEN",b"ACK_RECEIPT",b"ack_deadline_ns"),
 b"V12_EMPTY_FINAL_QUERY":(b"EMPTY_FINAL_QUERY",b"WAIT_EMPTY_QUERY",b"REMOVE_QUERY",b"remove_deadline_ns"),
 b"V12_EMPTY_FINAL_CONFIRMED":(b"EMPTY_FINAL_CONFIRMED",b"WAIT_EMPTY_CONFIRMED",b"EMPTY_OBSERVED",b"remove_deadline_ns"),
 b"V12_CGROUP_REMOVED":(b"CGROUP_REMOVED",b"WAIT_REMOVED",b"REMOVE_EFFECT",b"remove_deadline_ns"),
 b"V12_REMOVE_ACK":(b"REMOVE_ACK",b"WAIT_REMOVE_ACK",b"REMOVAL_VERIFIED",b"remove_deadline_ns"),
 b"V12_FINALIZE_CANDIDATE":(b"FINALIZE_CANDIDATE",b"WAIT_FINALIZE",b"FINALIZE_NOTICE",b"candidate_deadline_ns"),
 b"V12_TERMINAL_CANDIDATE_DURABLE":(b"TERMINAL_CANDIDATE_DURABLE",b"WAIT_TERMINAL_CANDIDATE",b"CANDIDATE_DURABLE",b"candidate_deadline_ns"),
 b"V12_TERMINAL_FAILURE_DURABLE":(b"TERMINAL_FAILURE_DURABLE",b"WAIT_TERMINAL_FAILURE",b"FAILURE_REPORT_DURABLE",b"candidate_deadline_ns"),
 b"V12_TERMINAL_SEEN":(b"TERMINAL_SEEN",b"WAIT_TERMINAL_SEEN",b"TERMINAL_SEEN",b"seen_deadline_ns"),
 b"V12_TERMINAL_ACK":(b"TERMINAL_ACK",b"WAIT_TERMINAL_ACK",b"ACK_SEND_EFFECT_UNKNOWN",b"ack_deadline_ns"),
 b"V12_TERMINAL_ACK_RECEIPT":(b"ACK_RECEIVED_NO_REPLAY",b"WAIT_ACK_RECEIPT",b"NO_REPLAY_RECEIPT",b"receipt_deadline_ns"),
 b"V12_TERMINAL_CLOSED":(b"OWNER_CLOSED",b"WAIT_OWNER_CLOSED",b"OWNER_CLOSURE",b"closure_deadline_ns")
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
 if kind==b"V12_ABORT":need(state==spec_state and effect==spec_effect and receiver not in (b"",b"*"))
 else:need((state,receiver,effect)==(spec_state,spec_receiver,spec_effect) and state!=b"*" and receiver!=b"*" and effect!=b"*")
 ordinal=provided.pop(b"ordinal");probe=provided.pop(b"probe")
 if b"auth_id" in provided:need(provided.pop(b"auth_id")==AUTH_ID)
 if b"sender" in provided:need(provided.pop(b"sender")==b"A")
 need(deadline_key in provided);deadline=provided.pop(deadline_key);udec(deadline,1)
 need(not any(key in CONTROL_RESERVED for key in provided))
 CONTROL_SEND_SEQ+=1
 transition=state+b"->"+receiver+b":"+effect
 body=(kind+b"|protocol_version=12|session_id="+AUTH_ID+b"|message_seq="+str(CONTROL_SEND_SEQ).encode()+b"|message_sender="+b"A"+b"|transition_id="+transition+b"|sender_state="+state+b"|expected_receiver_state="+receiver+b"|slot_ordinal="+ordinal+b"|slot_probe="+probe+b"|effect_state="+effect+b"|deadline_name="+deadline_key+b"|absolute_deadline_ns="+deadline)
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
 if kind!=b"V12_ABORT" and raw.startswith(b"V12_ABORT|"):
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
 need(common[b"protocol_version"]==b"12" and common[b"session_id"]==AUTH_ID and common[b"message_sender"]==b"B")
 need(common[b"transition_id"]==common[b"sender_state"]+b"->"+common[b"expected_receiver_state"]+b":"+common[b"effect_state"])
 if kind==b"V12_ABORT":need(common[b"sender_state"]==spec_state and common[b"effect_state"]==spec_effect and common[b"expected_receiver_state"] not in (b"",b"*"))
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
 values=parse_packet(raw,b"V12_ABORT",keys,binding)
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
  try:os.close(number)
  except OSError:pass

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
    for level,kind,data in ancillary:
     if level==socket.SOL_SOCKET and kind==socket.SCM_RIGHTS:
      cells=array.array("i");whole=len(data)-(len(data)%cells.itemsize)
      if whole:cells.frombytes(data[:whole]);installed.extend(cells)
      if whole!=len(data):bad=True
     else:bad=True
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
  info=os.open(b"/proc/self/fdinfo/"+str(number).encode(),os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(info,4096),4096)
 finally:close_numbers(tuple(x for x in (info,) if x>=0))
 values=[x[5:] for x in raw.splitlines() if x.startswith(b"Pid:\t")];need(len(values)==1,Refuse);return udec(values[0],1)

def proc_starttime(pid,kind=Refuse):
 number=-1
 try:
  number=os.open(b"/proc/"+str(pid).encode()+b"/stat",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(number,4096),4096)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))
 cut=raw.rfind(b") ");need(cut>0,kind);fields=raw[cut+2:].strip().split();need(len(fields)>=20,kind)
 return udec(fields[19],1)

EXTERNAL_MANIFEST_KEYS=(b"VERSION",b"SESSION_AUTH_POLICY",b"OWNER_PID",b"OWNER_STARTTIME",b"OWNER_UID",b"OWNER_GID",b"ENDPOINT_TYPE",b"PIDFD_REQUIRED",b"MAX_PACKET_BYTES",b"RIGHTS_TYPES",b"REFUSAL_RECEIPT_PROTOCOL",b"TRANSFER_PROTOCOL",b"NO_REPLAY")
EXTERNAL_RIGHTS_TYPES=b"ATTEMPT_DIRFD,ATTEMPT_BASE_DIRFD,STAGE_DIRFD,CGROUP_DIRFD,OUT_FD,ERR_FD,EVENTS_FD,KILL_FD,OUTER_PIDFD,CGROUP_BASE_DIRFD,ACTOR_CONTROL_FD,PENDING_EXPECTED_RAW_FD"

def parse_external_manifest(raw,cert):
 values=parse_fixed(raw,b"P27E001_EXTERNAL_OWNER_MANIFEST_V12",EXTERNAL_MANIFEST_KEYS,b"MANIFEST_END=1")
 exact={b"VERSION":b"12",b"SESSION_AUTH_POLICY":b"AUTH_V12_LENGTH_FRAMED",b"OWNER_PID":cert[b"EXTERNAL_OWNER_PID"],b"OWNER_STARTTIME":cert[b"EXTERNAL_OWNER_STARTTIME"],b"OWNER_UID":cert[b"EXTERNAL_OWNER_UID"],b"OWNER_GID":cert[b"EXTERNAL_OWNER_GID"],b"ENDPOINT_TYPE":b"SOCK_SEQPACKET",b"PIDFD_REQUIRED":b"1",b"MAX_PACKET_BYTES":b"65536",b"RIGHTS_TYPES":EXTERNAL_RIGHTS_TYPES,b"REFUSAL_RECEIPT_PROTOCOL":b"MONOTONE_O_EXCL_ISSUER_V12",b"TRANSFER_PROTOCOL":b"OFFER_ACCEPTED_DURABLE_V12",b"NO_REPLAY":b"1"}
 for key,value in exact.items():need(values[key]==value,Refuse)
 return values

def verify_external_inputs(cert):
 pid=udec(cert[b"EXTERNAL_OWNER_PID"],2);start=udec(cert[b"EXTERNAL_OWNER_STARTTIME"],1)
 fd_access(108,os.O_RDWR);fd_access(109,os.O_RDWR);need(pidfd_pid(109)==pid,Refuse)
 watcher=select.poll();watcher.register(109,select.POLLIN|select.POLLHUP|select.POLLERR);need(watcher.poll(0)==[],Refuse)
 duplicate=socket.fromfd(108,socket.AF_UNIX,socket.SOCK_SEQPACKET)
 try:
  need(duplicate.getsockopt(socket.SOL_SOCKET,socket.SO_TYPE)==socket.SOCK_SEQPACKET,Refuse)
  need(fcntl.fcntl(108,fcntl.F_GETFL)&os.O_NONBLOCK,Refuse)
  peer=struct.unpack("3i",duplicate.getsockopt(socket.SOL_SOCKET,socket.SO_PEERCRED,12))
  need(peer==(pid,udec(cert[b"EXTERNAL_OWNER_UID"]),udec(cert[b"EXTERNAL_OWNER_GID"])),Refuse)
 finally:duplicate.close()
 need(proc_starttime(pid)==start and pidfd_pid(109)==pid and proc_starttime(pid)==start and watcher.poll(0)==[],Refuse)

def cgroup_populated(number):
 os.lseek(number,0,os.SEEK_SET);raw=os.read(number,4096)
 matches=[line for line in raw.splitlines() if line.startswith(b"populated ")]
 need(len(matches)==1 and matches[0] in (b"populated 0",b"populated 1"),ConsumedIndeterminate)
 return matches[0]==b"populated 1"

def cgroup_empty(cgfd):
 number=-1
 try:
  number=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd);return not cgroup_populated(number)
 finally:close_numbers(tuple(x for x in (number,) if x>=0))

def exact_child_cgroup(cgfd,pid):
 number=-1
 try:
  number=os.open(b"cgroup.procs",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd);need(read_all(number,64)==str(pid).encode()+b"\n",ConsumedIndeterminate)
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
  rootfd=open_dir(RUNTIME_ROOT);number=open_under(rootfd,path);held=os.fstat(number);raw=read_all(number,held.st_size);os.close(number);number=-1
  py=open_under(rootfd,PYIMAGE);pyheld=os.fstat(py);pyraw=read_all(py,30626264);os.close(py);py=-1
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
  empty_r,empty_w=os.pipe2(os.O_CLOEXEC);os.close(empty_w);empty_w=-1
  left,right=socket.socketpair(socket.AF_UNIX,socket.SOCK_SEQPACKET|socket.SOCK_CLOEXEC|socket.SOCK_NONBLOCK)
  actor_pid=os.getpid();actor_starttime=proc_starttime(actor_pid);actor_pidfd=os.pidfd_open(actor_pid,0);need(pidfd_pid(actor_pidfd)==actor_pid and proc_starttime(actor_pid)==actor_starttime,Refuse);pid=os.fork()
  if pid>0:
   B_CHILD_PID=pid;B_CONTROL=left;left=None
  if pid==0:
   try:
    left.close();left=None
    mapping=((empty_r,0),(right.fileno(),3),(actor_pidfd,4),(base_stats[b"attempt_fd"],5),(base_stats[b"cgroup_fd"],6),(104,7),(105,8),(101,9),(103,10),(100,11),(102,12),(107,13),(108,14),(109,15),(110,16),(106,100))
    preserved_map(mapping);os.close(1);os.close(2)
    close_range(17,99);close_range(101,UINT_MAX)
    child_context(None,base_stats[b"safe"].st_dev,base_stats[b"safe"].st_ino);scrub_exact({0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,100})
    argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"/proc/self/fd/100",b"RECOVER_V12",AUTH_ID,str(actor_pid).encode(),str(actor_starttime).encode(),cert[b"PLAN_SHA256"],cert[b"RECOVERY_SHA256"],str(base_stats[b"safe"].st_dev).encode(),str(base_stats[b"safe"].st_ino).encode())
    os.execve(PYTHON,argv,ENV)
   except BaseException:os._exit(97)
  right.close();right=None;os.close(empty_r);empty_r=-1;os.close(actor_pidfd);actor_pidfd=-1
  result=B_CONTROL;need(B_CHILD_PID==pid and result is not None,Refuse);return pid,result
 finally:
  close_numbers(tuple(x for x in (empty_r,empty_w,actor_pidfd) if x>=0))
  for endpoint in (left,right):
   if endpoint is not None:
    try:endpoint.close()
    except BaseException:pass

def launch_outer(outer_fd,in_r,out_w,err_w,safe,argv,cgfd):
 pidfd_cell=ctypes.c_int(-1);args=CloneArgs();args.flags=CLONE_PIDFD|CLONE_INTO_CGROUP
 args.pidfd=ctypes.addressof(pidfd_cell);args.exit_signal=int(signal.SIGCHLD);args.cgroup=cgfd
 pid=LIBC.syscall(SYS_CLONE3,ctypes.byref(args),ctypes.sizeof(args))
 if pid<0:raise ConsumedIndeterminate("clone-return")
 if pid==0:
  try:
   os.kill(os.getpid(),signal.SIGSTOP)
   preserved_map(((in_r,0),(out_w,1),(err_w,2),(outer_fd,100)))
   close_range(3,99);close_range(101,UINT_MAX)
   child_context(AUTH_ID,safe.st_dev,safe.st_ino);scrub_exact({0,1,2,100})
   os.execve(PYTHON,tuple(argv),ENV)
  except BaseException:os._exit(98)
 need(pid>=2 and pidfd_cell.value>=0,ConsumedIndeterminate)
 return pid,pidfd_cell.value

def recv_result(control,deadline,ordinal,probe,pid):
 raw=recv_control(control,deadline)
 keys=(b"ordinal",b"probe",b"outer_pid",b"pidfd_bound",b"pidfd_exit_ready_observed",b"stdout_len",b"stdout_sha256",b"stdout_eof",b"stdout_frames",b"stderr_len",b"stderr_sha256",b"stderr_eof",b"stderr_frames",b"cgroup_empty",b"fault_set",b"capture_done_ns")
 values=parse_packet(raw,b"V12_RESULT",keys,receiver_binding(b"WAIT_RESULT",str(ordinal).encode(),probe,deadline))
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
   fields=parse_packet(header,b"V12_RESULT_FRAME",(b"ordinal",b"probe",b"stream",b"index",b"bytes",b"sha256"),receiver_binding(b"WAIT_RESULT_FRAME",str(ordinal).encode(),probe,deadline))
   need(udec(fields[b"ordinal"],0,14)==ordinal and fields[b"probe"]==probe and fields[b"stream"]==stream)
   need(udec(fields[b"index"])==index and udec(fields[b"bytes"],1,65000)==len(payload) and sha(payload)==fields[b"sha256"])
   target.extend(payload)
 end=parse_packet(recv_control(control,deadline),b"V12_RESULT_END",(b"state",b"ordinal",b"probe"),receiver_binding(b"WAIT_RESULT_END",str(ordinal).encode(),probe,deadline))
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
 raw=packet(b"V12_ABORT",((b"sender",b"A"),(b"state",b"ABORTING"),(b"expected_state",receiver_state),(b"ordinal",b"NONE" if ordinal is None else str(ordinal).encode()),(b"probe",probe),(b"effect_state",b"ABORT_NOTICE"),(b"causal_state",state),(b"causal_effect",effect),(b"stage_present",b"1" if STAGE_PRESENT else b"0"),(b"release_disabled",b"1"),(b"terminal_deadline_ns",str(terminal_deadline).encode()),(b"fault_set",fault_csv(faults)),(b"control_deadline_ns",str(deadline).encode())))
 send_plain(control,raw,deadline)

def run_probe(control,ordinal,probe,cgfd,safefd,safe,outer_source,ctx,p01c,cert):
 phase=b"STREAM_ARM";release_origin=time.monotonic_ns();launch_deadline=release_origin+LAUNCH_NS
 peer_pre_state=b"WAIT_STREAM_ARM";peer_deadline=launch_deadline
 in_r=in_w=out_r=out_w=err_r=err_w=outer_fd=events=kill=pidfd=-1;pid=-1;outer_starttime=0;direct_wait_entered=False
 try:
  checkpoint(cert,horizon_needed(release_origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ConsumedIndeterminate,launch_deadline)
  in_r,in_w=os.pipe2(os.O_CLOEXEC);os.close(in_w);in_w=-1;need(os.read(in_r,1)==b"")
  out_r,out_w=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK);err_r,err_w=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK)
  need(os.fstat(out_r).st_ino!=os.fstat(err_r).st_ino);outer_fd=memfd(outer_source,"p27-v15-outer-v5")
  events=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
  kill=os.open(b"cgroup.kill",os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
  stream=packet(b"V12_STREAM_ARM",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"release_origin_ns",str(release_origin).encode()),(b"launch_deadline_ns",str(launch_deadline).encode()),(b"stdout_dev",str(os.fstat(out_r).st_dev).encode()),(b"stdout_ino",str(os.fstat(out_r).st_ino).encode()),(b"stderr_dev",str(os.fstat(err_r).st_dev).encode()),(b"stderr_ino",str(os.fstat(err_r).st_ino).encode()),(b"events_dev",str(os.fstat(events).st_dev).encode()),(b"events_ino",str(os.fstat(events).st_ino).encode()),(b"kill_dev",str(os.fstat(kill).st_dev).encode()),(b"kill_ino",str(os.fstat(kill).st_ino).encode())))
  send_rights(control,stream,(out_r,err_r,events,kill),launch_deadline)
  close_numbers((out_r,err_r,events,kill));out_r=err_r=events=kill=-1
  armed=parse_packet(recv_control(control,launch_deadline),b"V12_STREAMS_ARMED",(b"ordinal",b"probe"),receiver_binding(b"WAIT_STREAMS_ARMED",str(ordinal).encode(),probe,launch_deadline))
  need(udec(armed[b"ordinal"],0,14)==ordinal and armed[b"probe"]==probe);progress(cert,launch_deadline,horizon_needed(release_origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS))
  peer_pre_state=b"WAIT_PIDFD_ARM"
  phase=b"CLONE";argv=source_argv(probe,safe,p01c);pid,pidfd=launch_outer(outer_fd,in_r,out_w,err_w,safe,argv,cgfd)
  outer_starttime=proc_starttime(pid);need(pidfd_pid(pidfd)==pid and proc_starttime(pid)==outer_starttime,ConsumedIndeterminate)
  close_numbers((in_r,out_w,err_w,outer_fd));in_r=out_w=err_w=outer_fd=-1
  phase=b"STOP";stopped=wait_status(pid,os.WUNTRACED,launch_deadline,b"STOP_WAIT_UNKNOWN")
  need(os.WIFSTOPPED(stopped) and os.WSTOPSIG(stopped)==signal.SIGSTOP and pidfd_pid(pidfd)==pid and proc_starttime(pid)==outer_starttime,ConsumedIndeterminate)
  exact_child_cgroup(cgfd,pid);need(not cgroup_empty(cgfd),ConsumedIndeterminate)
  phase=b"PIDFD_ARM";arm=packet(b"V12_PIDFD_ARM",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"outer_pid",str(pid).encode()),(b"outer_starttime",str(outer_starttime).encode()),(b"stopped_raw_status",str(stopped).encode()),(b"cgroup_member",b"1"),(b"pidfd_bound",b"1"),(b"launch_deadline_ns",str(launch_deadline).encode())))
  send_rights(control,arm,(pidfd,),launch_deadline);os.close(pidfd);pidfd=-1
  armed=parse_packet(recv_control(control,launch_deadline),b"V12_PIDFD_ARMED",(b"ordinal",b"probe",b"pidfd_bound",b"outer_pid",b"outer_starttime"),receiver_binding(b"WAIT_PIDFD_ARMED",str(ordinal).encode(),probe,launch_deadline))
  need(udec(armed[b"ordinal"],0,14)==ordinal and armed[b"probe"]==probe and armed[b"pidfd_bound"]==b"1" and udec(armed[b"outer_pid"],2)==pid and udec(armed[b"outer_starttime"],1)==outer_starttime)
  peer_pre_state=b"WAIT_RELEASE"
  outer_pid=pid;cg=os.fstat(cgfd)
  phase=b"RELEASE_RECORD";release_record_deadline=release_origin+RELEASE_RECORD_OFFSET_NS;release_reply_deadline=release_origin+RELEASE_REPLY_OFFSET_NS
  need(release_record_deadline<release_reply_deadline<launch_deadline,ConsumedIndeterminate)
  release=packet(b"V12_RELEASE_CANDIDATE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"outer_pid",str(pid).encode()),(b"outer_starttime",str(outer_starttime).encode()),(b"pidfd_bound",b"1"),(b"stopped_raw_status",str(stopped).encode()),(b"cgroup_member",b"1"),(b"cgroup_dev",str(cg.st_dev).encode()),(b"cgroup_ino",str(cg.st_ino).encode()),(b"cgroup_mode",format(cg.st_mode,"o").encode()),(b"cgroup_nlink",str(cg.st_nlink).encode()),(b"cgroup_uid",str(cg.st_uid).encode()),(b"cgroup_gid",str(cg.st_gid).encode()),(b"argv_sha256",sha(b"\x00".join(argv))),(b"env_sha256",sha(b"\x00".join(x+b"="+ENV[x] for x in sorted(ENV)))),(b"release_origin_ns",str(release_origin).encode()),(b"launch_overall_deadline_ns",str(launch_deadline).encode()),(b"release_record_deadline_ns",str(release_record_deadline).encode()),(b"release_reply_deadline_ns",str(release_reply_deadline).encode()),(b"launch_deadline_ns",str(release_record_deadline).encode())))
  send_plain(control,release,release_record_deadline)
  released=parse_packet(recv_control(control,release_reply_deadline),b"V12_RELEASE_DURABLE",(b"ordinal",b"probe",b"release_sha256",b"launch_overall_deadline_ns",b"release_record_deadline_ns",b"release_reply_deadline_ns"),receiver_binding(b"WAIT_RELEASE_DURABLE",str(ordinal).encode(),probe,release_reply_deadline))
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
  phase=b"RECEIPT";peer_pre_state=b"WAIT_VALIDATED";peer_deadline=ack_deadline;candidate=packet(b"V12_VALIDATED_CANDIDATE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"release_record_sha256",release_sha),(b"release_origin_ns",str(release_origin).encode()),(b"release_return_ns",str(release_return).encode()),(b"host_complete_ns",str(host_complete).encode()),(b"capture_done_ns",str(done).encode()),(b"direct_wait_state",b"COMPLETE"),(b"outer_raw_status",str(raw).encode()),(b"pidfd_bound",b"1"),(b"pidfd_exit_ready_observed",b"1"),(b"stdout_len",str(len(stdout)).encode()),(b"stdout_sha256",sha(stdout)),(b"stdout_eof",b"1"),(b"stdout_overflow",b"0"),(b"stderr_len",str(len(stderr)).encode()),(b"stderr_sha256",EMPTY_SHA),(b"stderr_eof",b"1"),(b"stderr_overflow",b"0"),(b"cgroup_empty",b"1"),(b"parser_language",b"ACCEPTED"),(b"parser_structure",b"ACCEPTED"),(b"parser_semantics",b"ACCEPTED"),(b"candidate",b"ACCEPTED"),(b"terminal",b"ACCEPTED"),(b"certificate_expiry_realtime_ns",cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"]),(b"ack_deadline_ns",str(ack_deadline).encode())))
  send_plain(control,candidate,ack_deadline)
  validated=parse_packet(recv_control(control,ack_deadline),b"V12_VALIDATED_DURABLE",(b"ordinal",b"probe",b"validated_sha256"),receiver_binding(b"WAIT_VALIDATED_DURABLE",str(ordinal).encode(),probe,ack_deadline))
  need(udec(validated[b"ordinal"],0,14)==ordinal and validated[b"probe"]==probe);validated_sha=h64(validated[b"validated_sha256"])
  peer_pre_state=b"WAIT_ACK_INTENT"
  checkpoint(cert,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ConsumedIndeterminate,ack_deadline)
  actor_ack=time.monotonic_ns();need(actor_ack-host_complete<=ACK_NS,ConsumedIndeterminate)
  intent=packet(b"V12_ACK_COMMIT_INTENT",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"validated_sha256",validated_sha),(b"host_complete_ns",str(host_complete).encode()),(b"ack_deadline_ns",str(ack_deadline).encode()),(b"actor_ack_intent_ns",str(actor_ack).encode())))
  send_plain(control,intent,ack_deadline)
  committed_raw=recv_control(control,ack_deadline);committed=parse_packet(committed_raw,b"V12_COMMITTED",(b"ordinal",b"probe",b"ack_sha256",b"commit_record_seq",b"committed_count"),receiver_binding(b"WAIT_COMMITTED",str(ordinal).encode(),probe,ack_deadline))
  need(udec(committed[b"ordinal"],0,14)==ordinal and committed[b"probe"]==probe);ack_sha=h64(committed[b"ack_sha256"])
  peer_pre_state=b"WAIT_COMMITTED_SEEN"
  need(udec(committed[b"commit_record_seq"],1)>0 and udec(committed[b"committed_count"],1,15)==ordinal+1);committed_packet_sha=sha(committed_raw)
  checkpoint(cert,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ConsumedIndeterminate,ack_deadline)
  seen=packet(b"V12_COMMITTED_SEEN",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"ack_sha256",ack_sha),(b"committed_packet_sha256",committed_packet_sha),(b"committed_count",committed[b"committed_count"]),(b"host_complete_ns",str(host_complete).encode()),(b"ack_deadline_ns",str(ack_deadline).encode())))
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
  close_numbers(tuple(number for number in (in_r,in_w,out_r,out_w,err_r,err_w,outer_fd,events,kill,pidfd) if number>=0))

def mount_semantics(line,fstype,required,forbidden):
 pieces=line[:-1].split(b" - ");need(len(pieces)==2)
 left=pieces[0].split(b" ");right=pieces[1].split(b" ");need(len(left)>=6 and len(right)>=3 and right[0]==fstype)
 options=set(left[5].split(b","))|set(right[2].split(b","))
 need(required<=options and not (forbidden&options),Refuse)

def mount_graph(cert):
 number=-1
 try:
  number=os.open(b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(number,1048576),1048576)
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
  kind=b"V12_REFUSE_PREBEGIN";cross_state=b"ARM_NOT_ENTERED";origin=time.monotonic_ns();closure_deadline=origin+REFUSAL_TOTAL_NS
 elif (begin_state,arm_state)==(b"BEGIN_SENT",b"ARMED_CONFIRMED"):
  kind=b"V12_REFUSE_POSTARM";cross_state=b"REFUSAL_CLOSED_NO_CONSUME";closure_deadline=inherited_deadline;origin=closure_deadline-REFUSAL_TOTAL_NS
 else:raise ConsumedIndeterminate("refusal-cross-map")
 need(time.monotonic_ns()<=origin+REFUSAL_RECORD_NS and closure_deadline<=inherited_deadline,ConsumedIndeterminate)
 schedule=exact_schedule(origin,closure_deadline,REFUSAL_PHASE_SPEC);request_deadline=schedule[b"REFUSAL_RECORD"]
 finality_deadline=schedule[b"REFUSAL_FINALITY"]
 need(finality_deadline==origin+REFUSAL_FINALITY_NS and closure_deadline==schedule[b"REFUSAL_CLOSURE"] and finality_deadline<closure_deadline and closure_deadline-finality_deadline==REFUSAL_CLOSURE_TAIL_NS,ConsumedIndeterminate)
 raw=packet(kind,((b"state",b"REFUSE_PREBEGIN" if kind==b"V12_REFUSE_PREBEGIN" else b"REFUSE_POSTARM"),(b"expected_state",b"WAIT_BEGIN" if kind==b"V12_REFUSE_PREBEGIN" else b"WAIT_COMMIT"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH_ID),(b"a_begin_state",begin_state),(b"a_arm_state",arm_state),(b"cross_map_state",cross_state),(b"reason",reason),(b"refusal_origin_ns",str(origin).encode()),(b"refusal_finality_deadline_ns",str(finality_deadline).encode()),(b"refusal_closure_deadline_ns",str(closure_deadline).encode()),(b"refusal_schedule_hex",schedule_hex(schedule,REFUSAL_PHASE_SPEC)),(b"consume_deadline_ns",str(request_deadline).encode())))
 request_send_state=b"REFUSAL_REQUEST_EFFECT_UNKNOWN"
 try:send_plain(control,raw,request_deadline);request_send_state=b"REFUSAL_REQUEST_SENT"
 except SendEffectUnknown:request_send_state=b"REFUSAL_REQUEST_EFFECT_UNKNOWN"
 ack_deadline=schedule[b"REFUSAL_ACK"]
 ack_raw=recv_control(control,ack_deadline)
 ack=parse_packet(ack_raw,b"V12_REFUSE_ACK",(b"state",b"ordinal",b"probe",b"auth_id",b"a_begin_state",b"a_arm_state",b"cross_map_state",b"request_packet_sha256",b"request_message_seq",b"commit_count",b"attempt_state",b"intent_count",b"disposition",b"refusal_origin_ns",b"refusal_finality_deadline_ns",b"refusal_closure_deadline_ns",b"refusal_schedule_hex",b"consume_deadline_ns"),receiver_binding(b"WAIT_REFUSAL_ACK",b"NONE",b"NONE",ack_deadline))
 need(ack[b"state"]==b"REFUSAL_CLOSED_NO_CONSUME" and ack[b"expected_state"]==b"WAIT_REFUSAL_ACK" and ack[b"effect_state"]==b"REFUSAL_ACK_SEND_EFFECT_UNKNOWN",ConsumedIndeterminate)
 need(ack[b"ordinal"]==ack[b"probe"]==b"NONE" and ack[b"auth_id"]==AUTH_ID and ack[b"a_begin_state"]==begin_state and ack[b"a_arm_state"]==arm_state,ConsumedIndeterminate)
 need(ack[b"cross_map_state"]==cross_state and ack[b"request_packet_sha256"]==sha(raw) and ack[b"request_message_seq"]==str(CONTROL_SEND_SEQ).encode(),ConsumedIndeterminate)
 need(ack[b"commit_count"]==b"0" and ack[b"attempt_state"]==b"ABSENT_KNOWN" and ack[b"intent_count"]==b"0" and ack[b"disposition"]==b"UNCONSUMED",ConsumedIndeterminate)
 need(udec(ack[b"refusal_origin_ns"])==origin and udec(ack[b"refusal_finality_deadline_ns"])==finality_deadline and udec(ack[b"refusal_closure_deadline_ns"])==closure_deadline and ack[b"refusal_schedule_hex"]==schedule_hex(schedule,REFUSAL_PHASE_SPEC),ConsumedIndeterminate)
 receipt_deadline=finality_deadline
 receipt=packet(b"V12_REFUSE_ACK_RECEIPT",((b"state",b"REFUSAL_ACK_RECEIVED"),(b"expected_state",b"WAIT_REFUSAL_RECEIPT"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"ack_packet_sha256",sha(ack_raw)),(b"ack_message_seq",ack[b"message_seq"]),(b"request_packet_sha256",sha(raw)),(b"cross_map_state",cross_state),(b"no_replay",b"1"),(b"refusal_finality_deadline_ns",str(finality_deadline).encode()),(b"refusal_closure_deadline_ns",str(closure_deadline).encode()),(b"refusal_schedule_hex",schedule_hex(schedule,REFUSAL_PHASE_SPEC)),(b"consume_deadline_ns",str(receipt_deadline).encode())))
 receipt_send_state=b"REFUSAL_RECEIPT_EFFECT_UNKNOWN"
 try:send_plain(control,receipt,receipt_deadline);receipt_send_state=b"REFUSAL_RECEIPT_SENT"
 except SendEffectUnknown:receipt_send_state=b"REFUSAL_RECEIPT_EFFECT_UNKNOWN"
 actor_closure_deadline=schedule[b"REFUSAL_ACTOR_CLOSURE"];closed_raw=recv_control(control,actor_closure_deadline)
 closed=parse_packet(closed_raw,b"V12_REFUSAL_CLOSED",(b"state",b"ordinal",b"probe",b"ack_packet_sha256",b"receipt_packet_sha256",b"cross_map_state",b"issuer_closure_sha256",b"issuer_record_seq",b"issuer_predecessor_sha256",b"no_replay",b"refusal_finality_deadline_ns",b"refusal_closure_deadline_ns",b"refusal_schedule_hex",b"consume_deadline_ns"),receiver_binding(b"WAIT_REFUSAL_CLOSED",b"NONE",b"NONE",actor_closure_deadline))
 need(closed[b"state"]==b"REFUSAL_DURABLY_CLOSED" and closed[b"expected_state"]==b"WAIT_REFUSAL_CLOSED" and closed[b"effect_state"]==b"OWNER_CLOSURE",ConsumedIndeterminate)
 need(closed[b"ordinal"]==closed[b"probe"]==b"NONE" and closed[b"ack_packet_sha256"]==sha(ack_raw) and closed[b"receipt_packet_sha256"]==sha(receipt),ConsumedIndeterminate)
 need(closed[b"cross_map_state"]==cross_state and h64(closed[b"issuer_closure_sha256"])!=b"0"*64 and udec(closed[b"issuer_record_seq"],1)>=1 and h64(closed[b"issuer_predecessor_sha256"])!=b"0"*64,ConsumedIndeterminate)
 need(closed[b"no_replay"]==b"1" and udec(closed[b"refusal_finality_deadline_ns"])==finality_deadline and udec(closed[b"refusal_closure_deadline_ns"])==closure_deadline and closed[b"refusal_schedule_hex"]==schedule_hex(schedule,REFUSAL_PHASE_SPEC),ConsumedIndeterminate)
 return {b"request_raw":raw,b"ack_raw":ack_raw,b"receipt_raw":receipt,b"closed_raw":closed_raw,b"cross_state":cross_state,b"request_send_state":request_send_state,b"receipt_send_state":receipt_send_state,b"refusal_finality_deadline":finality_deadline,b"refusal_closure_deadline":closure_deadline}

def failure_recv(control,deadline,actual_pre_state,stop_probe):
 while True:
  raw=recv_control(control,deadline)
  if not raw.startswith(b"V12_ABORT|"):return raw
  try:
   binding=received_binding(raw,actual_pre_state,b"NONE",stop_probe,b"control_deadline_ns",deadline)
   values,faults=parse_abort(raw,b"B",binding);need(values[b"causal_state"]==b"CLEANUP_RELEASE_DISABLE")
   remote_deadline=udec(values[b"terminal_deadline_ns"],1);response_deadline=udec(values[b"control_deadline_ns"],1)
   need(time.monotonic_ns()<=response_deadline<=remote_deadline<=deadline)
   send_abort(control,b"CLEANUP_RELEASE_DISABLED",b"WAIT_RELEASE_DISABLE_ACK",None,values[b"probe"],faults,response_deadline,remote_deadline)
  except FaultSet:raise

def await_failure_terminal(control,outer_deadline,stop_probe):
 notice_raw=failure_recv(control,outer_deadline,b"WAIT_TERMINAL_FAILURE",stop_probe)
 values=parse_packet(notice_raw,b"V12_TERMINAL_FAILURE_DURABLE",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"chain_head_sha256",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"candidate_deadline_ns",b"disposition"),received_binding(notice_raw,b"WAIT_TERMINAL_FAILURE",b"NONE",b"NONE",b"candidate_deadline_ns",outer_deadline))
 subject=h64(values[b"subject_sha256"]);origin=udec(values[b"terminal_origin_ns"],1);deadline=udec(values[b"terminal_deadline_ns"],1)
 need(values[b"state"]==b"TERMINAL_FAILURE_DURABLE" and values[b"expected_state"]==b"WAIT_TERMINAL_FAILURE" and values[b"effect_state"]==b"FAILURE_REPORT_DURABLE")
 need(values[b"ordinal"]==values[b"probe"]==b"NONE" and values[b"kind"]==b"FAILURE_CANDIDATE" and values[b"disposition"] in (b"CONSUMED_FAIL",b"CONSUMED_INDETERMINATE"))
 need(time.monotonic_ns()<=deadline<=outer_deadline and deadline==origin+FINAL_TOTAL_NS);schedule=check_schedule_hex(values[b"terminal_schedule_hex"],origin,deadline,TERMINAL_PHASE_SPEC)
 need(udec(values[b"candidate_deadline_ns"])==schedule[b"NOTICE"])
 seen_deadline=schedule[b"TERMINAL_SEEN_RECORD"]
 seen=packet(b"V12_TERMINAL_SEEN",((b"state",b"TERMINAL_SEEN"),(b"expected_state",b"WAIT_TERMINAL_SEEN"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",b"FAILURE_CANDIDATE"),(b"subject_sha256",subject),(b"notice_packet_sha256",sha(notice_raw)),(b"terminal_origin_ns",str(origin).encode()),(b"terminal_deadline_ns",str(deadline).encode()),(b"terminal_schedule_hex",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"seen_deadline_ns",str(seen_deadline).encode())))
 send_plain(control,seen,seen_deadline)
 ack_deadline=schedule[b"ACK"];ack_raw=failure_recv(control,ack_deadline,b"WAIT_TERMINAL_ACK",stop_probe)
 ack=parse_packet(ack_raw,b"V12_TERMINAL_ACK",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"terminal_seen_sha256",b"report_sha256",b"pass_sha256",b"reconciliation_token",b"ack_state",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"ack_deadline_ns"),receiver_binding(b"WAIT_TERMINAL_ACK",b"NONE",b"NONE",ack_deadline))
 need(ack[b"state"]==b"TERMINAL_ACK" and ack[b"expected_state"]==b"WAIT_TERMINAL_ACK" and ack[b"ordinal"]==ack[b"probe"]==b"NONE" and ack[b"kind"]==b"FAILURE_CANDIDATE" and ack[b"subject_sha256"]==subject)
 report_sha=h64(ack[b"report_sha256"]);need(ack[b"pass_sha256"]==ack[b"reconciliation_token"]==b"NONE" and ack[b"ack_state"]==b"FAILURE_DURABLE")
 need(udec(ack[b"terminal_origin_ns"])==origin and udec(ack[b"terminal_deadline_ns"])==deadline and ack[b"terminal_schedule_hex"]==schedule_hex(schedule,TERMINAL_PHASE_SPEC))
 receipt_deadline=schedule[b"A_RECEIPT"];receipt_ns=time.monotonic_ns()
 receipt=packet(b"V12_TERMINAL_ACK_RECEIPT",((b"state",b"ACK_RECEIVED_NO_REPLAY"),(b"expected_state",b"WAIT_ACK_RECEIPT"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",b"FAILURE_CANDIDATE"),(b"subject_sha256",subject),(b"ack_packet_sha256",sha(ack_raw)),(b"report_sha256",report_sha),(b"pass_sha256",b"NONE"),(b"reconciliation_token",b"NONE"),(b"actor_receipt_ns",str(receipt_ns).encode()),(b"terminal_origin_ns",str(origin).encode()),(b"terminal_deadline_ns",str(deadline).encode()),(b"terminal_schedule_hex",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"receipt_deadline_ns",str(receipt_deadline).encode())))
 send_plain(control,receipt,receipt_deadline)
 closure_deadline=schedule[b"CLOSURE_PACKET"];closed=parse_packet(failure_recv(control,closure_deadline,b"WAIT_OWNER_CLOSED",stop_probe),b"V12_TERMINAL_CLOSED",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"report_sha256",b"pass_sha256",b"ack_receipt_sha256",b"reconciliation_sha256",b"closure_sha256",b"owner",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"closure_deadline_ns"),receiver_binding(b"WAIT_OWNER_CLOSED",b"NONE",b"NONE",closure_deadline))
 need(closed[b"state"]==b"OWNER_CLOSED" and closed[b"expected_state"]==b"WAIT_OWNER_CLOSED" and closed[b"ordinal"]==closed[b"probe"]==b"NONE" and closed[b"kind"]==b"FAILURE_CANDIDATE")
 need(closed[b"subject_sha256"]==subject and closed[b"report_sha256"]==report_sha and closed[b"pass_sha256"]==b"NONE" and closed[b"owner"]==b"B")
 for key in (b"ack_receipt_sha256",b"reconciliation_sha256",b"closure_sha256"):need(h64(closed[key])!=b"0"*64)
 need(udec(closed[b"terminal_origin_ns"])==origin and udec(closed[b"terminal_deadline_ns"])==deadline and closed[b"terminal_schedule_hex"]==schedule_hex(schedule,TERMINAL_PHASE_SPEC))
 return values[b"disposition"],deadline

def main():
 global AUTH_ID,PREFLIGHT,CERT,STAGE_PRESENT,B_CHILD_PID,B_CONTROL
 entry_mono=time.monotonic_ns();state=b"INPUT";consumed=False;commit_edge=False;peer_pre_state=b"WAIT_BEGIN";peer_deadline=entry_mono+PRECONSUME_NS
 begin_effect_possible=False;begin_state=b"BEGIN_NOT_ENTERED";arm_state=b"ARM_NOT_OBSERVED";refusal_acked=False
 pass_may_be_committed=False;pass_authoritative=False;receipt_effect_unknown=False;terminal_deadline=0;failure_terminal_deadline=0
 bpid=-1;control=None;runtime=attempt_base=stage_base=cgroup_base=safefd=cgfd=-1
 need(type(sys.argv)is list and len(sys.argv)==3 and sys.argv[0]=="/proc/self/fd/100" and sys.argv[1]=="RUN_V12",Refuse)
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
 need(envelope[b"E0366_SNAPSHOT_SHA256"]==CERT[b"E0366_SNAPSHOT_SHA256"]==sha(snapshot),Refuse)
 need(envelope[b"E0366_SNAPSHOT_BYTES"]==CERT[b"E0366_SNAPSHOT_BYTES"]==b"2303269" and envelope[b"E0366_SNAPSHOT_LF"]==CERT[b"E0366_SNAPSHOT_LF"]==b"23672",Refuse)
 need(envelope[b"E0366_SNAPSHOT_TERMINAL_HEX"]==CERT[b"E0366_SNAPSHOT_TERMINAL_HEX"]==SNAPSHOT_TERMINAL_HEX,Refuse)
 not_before=udec(CERT[b"NOT_BEFORE_REALTIME_NS"]);expiry=udec(CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"])
 need(expiry-not_before==CERT_LIFE_NS and udec(envelope[b"NOT_BEFORE_REALTIME_NS"])<=not_before<expiry<=udec(envelope[b"NOT_AFTER_REALTIME_NS"]),Refuse)
 checkpoint(CERT,horizon_needed(entry_mono+PRECONSUME_NS,CONSUME_REMAIN_NS),Refuse,entry_mono+PRECONSUME_NS);verify_platform(CERT);signal_snapshot(CERT)
 ab=b"P27 RUNNER V12 ACTOR SOURCE "+b"BEGIN C5A91E34";ae=b"P27 RUNNER V12 ACTOR SOURCE "+b"END C5A91E34"
 bb=b"P27 RUNNER V12 WATCHDOG SOURCE "+b"BEGIN F5C2189D";be=b"P27 RUNNER V12 WATCHDOG SOURCE "+b"END F5C2189D"
 need(extract_one(plan,ab,ae)==actor_raw and extract_one(plan,bb,be)==b_raw,Refuse)
 sources=v15_sources(v15)
 state=b"ENTRY"
 try:
  runtime=open_dir(RUNTIME_ROOT);attempt_base=open_dir(ATTEMPT_BASE);stage_base=open_dir(STAGE_BASE);cgroup_base=open_dir(CGROUP_BASE)
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
   base_type=os.open(b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgroup_base)
   base_controllers=os.open(b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgroup_base)
   base_subtree=os.open(b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgroup_base)
   need(read_all(base_type,128).hex().encode()==CERT[b"CGROUP_BASE_TYPE_HEX"],Refuse)
   need(read_all(base_controllers,4096).hex().encode()==CERT[b"CGROUP_BASE_CONTROLLERS_HEX"],Refuse)
   need(read_all(base_subtree,4096).hex().encode()==CERT[b"CGROUP_BASE_SUBTREE_CONTROL_HEX"],Refuse)
  finally:close_numbers((base_type,base_controllers,base_subtree))
  need(runtime_mid!=stage_mid,Refuse);mount_graph(CERT)
  absent(attempt_base,AUTH_ID,Refuse);absent(stage_base,AUTH_ID,Refuse);absent(cgroup_base,AUTH_ID,Refuse)
  need(time.monotonic_ns()-entry_mono<=PRECONSUME_NS,Refuse)
  bases={b"attempt_fd":attempt_base,b"cgroup_fd":cgroup_base,b"safe":stage_stat}
  state=b"B_BOOT";bpid,control=launch_b(CERT,bases);need(B_CHILD_PID==bpid and B_CONTROL is control and fcntl.fcntl(control.fileno(),fcntl.F_GETFL)&os.O_NONBLOCK,Refuse)
  os.close(attempt_base);attempt_base=-1
  ready_deadline=entry_mono+PRECONSUME_NS;peer_pre_state=b"WAIT_BEGIN";peer_deadline=ready_deadline
  ready_raw=recv_control(control,ready_deadline)
  ready=parse_packet(ready_raw,b"V12_READY",(b"state",b"ordinal",b"probe"),received_binding(ready_raw,b"WAIT_READY",b"NONE",b"NONE",b"ready_deadline_ns",ready_deadline))
  need(ready[b"state"]==b"READY" and ready[b"ordinal"]==ready[b"probe"]==b"NONE",Refuse)
  checkpoint(CERT,CONSUME_REMAIN_NS,Refuse,ready_deadline)
  consume_origin=time.monotonic_ns();consume_deadline=consume_origin+CONSUMPTION_NS
  checkpoint(CERT,CONSUME_REMAIN_NS,Refuse,consume_deadline)
  state=b"BEGIN_SEND_EFFECT_UNKNOWN";begin_state=b"BEGIN_SEND_EFFECT_UNKNOWN";begin_effect_possible=True
  begin=packet(b"V12_CONSUME_BEGIN",((b"state",b"CONSUME_BEGIN"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH_ID),(b"a_begin_state",begin_state),(b"a_arm_state",arm_state),(b"consume_origin_ns",str(consume_origin).encode()),(b"consume_deadline_ns",str(consume_deadline).encode())))
  b_send(control,begin,consume_deadline);begin_state=b"BEGIN_SENT";state=b"BEGIN_SENT"
  arm_state=b"ARM_RECEIVE_EFFECT_UNKNOWN";state=b"ARM_RECEIVE_EFFECT_UNKNOWN"
  armed=parse_packet(recv_control(control,consume_deadline),b"V12_CONSUME_ARMED",(b"state",b"ordinal",b"probe",b"auth_id",b"a_begin_state",b"b_arm_state",b"consume_origin_ns",b"consume_deadline_ns"),receiver_binding(b"WAIT_ARM",b"NONE",b"NONE",consume_deadline))
  need(armed[b"state"]==b"CONSUME_ARMED" and armed[b"ordinal"]==armed[b"probe"]==b"NONE" and armed[b"auth_id"]==AUTH_ID)
  need(armed[b"a_begin_state"]==b"BEGIN_SEND_EFFECT_UNKNOWN" and armed[b"b_arm_state"]==b"ARM_SEND_EFFECT_UNKNOWN")
  need(udec(armed[b"consume_origin_ns"])==consume_origin and udec(armed[b"consume_deadline_ns"])==consume_deadline)
  arm_state=b"ARMED_CONFIRMED";state=b"ARMED_CONFIRMED";peer_pre_state=b"WAIT_COMMIT";peer_deadline=consume_deadline
  commit_edge=True;consumed=True;PREFLIGHT=False;state=b"COMMIT_SEND_EFFECT_UNKNOWN"
  commit=packet(b"V12_CONSUME_COMMIT",((b"state",b"CONSUME_COMMIT"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH_ID),(b"a_begin_state",begin_state),(b"a_arm_state",arm_state),(b"a_commit_state",b"COMMIT_SEND_EFFECT_UNKNOWN"),(b"consume_origin_ns",str(consume_origin).encode()),(b"consume_deadline_ns",str(consume_deadline).encode())))
  b_send(control,commit,consume_deadline);state=b"COMMIT_SENT";peer_pre_state=b"WAIT_STAGE"
  consumed_msg=parse_packet(recv_control(control,consume_deadline),b"V12_CONSUMED_DURABLE",(b"state",b"ordinal",b"probe",b"auth_id",b"intent_sha256",b"consume_origin_ns",b"consume_deadline_ns",b"attempt_fd_state"),receiver_binding(b"WAIT_CONSUMED",b"NONE",b"NONE",consume_deadline))
  need(consumed_msg[b"state"]==b"CONSUMED_DURABLE" and consumed_msg[b"ordinal"]==consumed_msg[b"probe"]==b"NONE" and consumed_msg[b"auth_id"]==AUTH_ID)
  need(udec(consumed_msg[b"consume_origin_ns"])==consume_origin and udec(consumed_msg[b"consume_deadline_ns"])==consume_deadline and consumed_msg[b"attempt_fd_state"]==b"PUBLISHED")
  chain_sha=h64(consumed_msg[b"intent_sha256"]);checkpoint(CERT,PRE_STAGE_REMAIN_NS,ConsumedIndeterminate,consume_deadline)
  state=b"STAGE";stage_origin=time.monotonic_ns();stage_deadline=stage_origin+STAGE_NS;peer_pre_state=b"WAIT_STAGE";peer_deadline=stage_deadline
  checkpoint(CERT,PRE_STAGE_REMAIN_NS,ConsumedIndeterminate,stage_deadline)
  os.mkdir(AUTH_ID,0o700,dir_fd=stage_base);progress(CERT,stage_deadline,horizon_needed(stage_deadline,POST_STAGE_REMAIN_NS));os.fsync(stage_base);progress(CERT,stage_deadline,horizon_needed(stage_deadline,POST_STAGE_REMAIN_NS))
  safefd=os.open(AUTH_ID,O_DIR,dir_fd=stage_base);progress(CERT,stage_deadline,horizon_needed(stage_deadline,POST_STAGE_REMAIN_NS));safe=os.fstat(safefd)
  need((safe.st_uid,safe.st_gid,stat.S_IMODE(safe.st_mode),safe.st_nlink)==(0,0,0o700,2),ConsumedIndeterminate)
  named=os.stat(AUTH_ID,dir_fd=stage_base,follow_symlinks=False)
  need((named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid)==(safe.st_dev,safe.st_ino,safe.st_mode,safe.st_nlink,safe.st_uid,safe.st_gid),ConsumedIndeterminate)
  for name in (b"target",b"a",b"b"):absent(safefd,name)
  for name,body,identity in zip(SOURCE_NAMES,sources[1:],SOURCE_META[1:]):stage_leaf(safefd,name,body,identity,stage_deadline)
  os.fsync(safefd);progress(CERT,stage_deadline,POST_STAGE_REMAIN_NS)
  STAGE_PRESENT=True
  staged=packet(b"V12_STAGE_DURABLE",((b"state",b"STAGE_DURABLE"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"stage_origin_ns",str(stage_origin).encode()),(b"stage_deadline_ns",str(stage_deadline).encode()),(b"stage_return_ns",str(time.monotonic_ns()).encode()),(b"safe_dev",str(safe.st_dev).encode()),(b"safe_ino",str(safe.st_ino).encode()),(b"safe_mode",format(safe.st_mode,"o").encode()),(b"safe_nlink",str(safe.st_nlink).encode()),(b"safe_uid",str(safe.st_uid).encode()),(b"safe_gid",str(safe.st_gid).encode()),(b"keeper_sha256",CERT[b"KEEPER_SHA256"]),(b"launcher_sha256",CERT[b"LAUNCHER_SHA256"]),(b"marker_sha256",CERT[b"MARKER_SHA256"]),(b"child_sha256",CERT[b"CHILD_SHA256"])))
  send_rights(control,staged,(safefd,),stage_deadline)
  stage_ack=parse_packet(recv_control(control,stage_deadline),b"V12_STAGE_ACK",(b"state",b"ordinal",b"probe",b"stage_deadline_ns",b"safe_dev",b"safe_ino"),receiver_binding(b"WAIT_STAGE_ACK",b"NONE",b"NONE",stage_deadline))
  need(stage_ack[b"state"]==b"STAGE_BOUND" and stage_ack[b"ordinal"]==stage_ack[b"probe"]==b"NONE")
  need(udec(stage_ack[b"stage_deadline_ns"])==stage_deadline and (udec(stage_ack[b"safe_dev"]),udec(stage_ack[b"safe_ino"]))==(safe.st_dev,safe.st_ino))
  progress(CERT,stage_deadline,POST_STAGE_REMAIN_NS)
  state=b"CONTAIN";contain_origin=time.monotonic_ns();contain_deadline=contain_origin+ACK_NS;peer_pre_state=b"WAIT_CONTAINMENT";peer_deadline=contain_deadline
  os.mkdir(AUTH_ID,0o700,dir_fd=cgroup_base);progress(CERT,contain_deadline,horizon_needed(contain_deadline,POST_CONTAIN_REMAIN_NS))
  cgfd=os.open(AUTH_ID,O_DIR,dir_fd=cgroup_base);progress(CERT,contain_deadline,horizon_needed(contain_deadline,POST_CONTAIN_REMAIN_NS));cgchild=os.fstat(cgfd)
  need((format(cgchild.st_mode,"o").encode(),cgchild.st_uid,cgchild.st_gid,cgchild.st_nlink)==(CERT[b"CGROUP_CHILD_MODE"],0,0,2),ConsumedIndeterminate)
  need(cgroup_empty(cgfd),ConsumedIndeterminate)
  ctype=controllers=subtree=-1
  try:
   ctype=os.open(b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
   controllers=os.open(b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
   subtree=os.open(b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=cgfd)
   type_raw=read_all(ctype,128);controllers_raw=read_all(controllers,4096);subtree_raw=read_all(subtree,4096)
   need(type_raw.hex().encode()==CERT[b"CGROUP_CHILD_TYPE_HEX"],ConsumedIndeterminate)
   need(controllers_raw.hex().encode()==CERT[b"CGROUP_CHILD_CONTROLLERS_HEX"],ConsumedIndeterminate)
   need(subtree_raw.hex().encode()==CERT[b"CGROUP_CHILD_SUBTREE_CONTROL_HEX"],ConsumedIndeterminate)
  finally:close_numbers(tuple(x for x in (ctype,controllers,subtree) if x>=0))
  cgbase=os.fstat(cgroup_base);cg_mid,cg_line=mount_line(cgfd)
  containment=packet(b"V12_CONTAINMENT",((b"state",b"CONTAINMENT_CANDIDATE"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"contain_origin_ns",str(contain_origin).encode()),(b"contain_deadline_ns",str(contain_deadline).encode()),(b"dev",str(cgchild.st_dev).encode()),(b"ino",str(cgchild.st_ino).encode()),(b"mode",format(cgchild.st_mode,"o").encode()),(b"nlink",str(cgchild.st_nlink).encode()),(b"uid",str(cgchild.st_uid).encode()),(b"gid",str(cgchild.st_gid).encode()),(b"base_dev",str(cgbase.st_dev).encode()),(b"base_ino",str(cgbase.st_ino).encode()),(b"mount_id",str(cg_mid).encode()),(b"mountinfo_sha256",sha(cg_line)),(b"type_hex",type_raw.hex().encode()),(b"controllers_hex",controllers_raw.hex().encode()),(b"subtree_control_hex",subtree_raw.hex().encode())))
  send_rights(control,containment,(cgfd,),contain_deadline)
  contain_ack=parse_packet(recv_control(control,contain_deadline),b"V12_CONTAINMENT_ACK",(b"state",b"ordinal",b"probe",b"contain_deadline_ns",b"dev",b"ino"),receiver_binding(b"WAIT_CONTAINMENT_ACK",b"NONE",b"NONE",contain_deadline))
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
  query=packet(b"V12_EMPTY_FINAL_QUERY",((b"state",b"EMPTY_FINAL_QUERY"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"chain_head_sha256",chain_sha),(b"remove_origin_ns",str(remove_origin).encode()),(b"remove_deadline_ns",str(remove_deadline).encode())))
  b_send(control,query,remove_deadline)
  confirmed=parse_packet(recv_control(control,remove_deadline),b"V12_EMPTY_FINAL_CONFIRMED",(b"state",b"ordinal",b"probe",b"chain_head_sha256",b"remove_deadline_ns"),receiver_binding(b"WAIT_EMPTY_CONFIRMED",b"NONE",b"NONE",remove_deadline))
  need(confirmed[b"state"]==b"EMPTY_FINAL_CONFIRMED" and confirmed[b"ordinal"]==confirmed[b"probe"]==b"NONE" and h64(confirmed[b"chain_head_sha256"]) and udec(confirmed[b"remove_deadline_ns"])==remove_deadline)
  chain_sha=confirmed[b"chain_head_sha256"];peer_pre_state=b"WAIT_REMOVE_ACK"
  os.close(cgfd);cgfd=-1;os.rmdir(AUTH_ID,dir_fd=cgroup_base)
  try:os.stat(AUTH_ID,dir_fd=cgroup_base,follow_symlinks=False);need(False,ConsumedIndeterminate)
  except FileNotFoundError:pass
  progress(CERT,remove_deadline,FINAL_TOTAL_NS)
  removed=packet(b"V12_CGROUP_REMOVED",((b"state",b"CGROUP_REMOVED"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"chain_head_sha256",chain_sha),(b"remove_deadline_ns",str(remove_deadline).encode())))
  b_send(control,removed,remove_deadline)
  removed_ack=parse_packet(recv_control(control,remove_deadline),b"V12_REMOVE_ACK",(b"state",b"ordinal",b"probe",b"chain_head_sha256",b"remove_deadline_ns"),receiver_binding(b"WAIT_REMOVE_ACK",b"NONE",b"NONE",remove_deadline))
  need(removed_ack[b"state"]==b"REMOVE_ACK" and removed_ack[b"ordinal"]==removed_ack[b"probe"]==b"NONE" and removed_ack[b"chain_head_sha256"]==chain_sha and udec(removed_ack[b"remove_deadline_ns"])==remove_deadline)
  state=b"FINAL";terminal_origin=time.monotonic_ns();terminal_deadline=terminal_origin+FINAL_TOTAL_NS;schedule=exact_schedule(terminal_origin,terminal_deadline,TERMINAL_PHASE_SPEC);peer_pre_state=b"WAIT_FINALIZE";peer_deadline=schedule[b"CANDIDATE_RECORD"]
  checkpoint(CERT,FINAL_TOTAL_NS,ConsumedIndeterminate,schedule[b"CANDIDATE_RECORD"])
  finalize=packet(b"V12_FINALIZE_CANDIDATE",((b"state",b"FINALIZE_CANDIDATE"),(b"expected_state",b"WAIT_FINALIZE"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"chain_head_sha256",chain_sha),(b"terminal_origin_ns",str(terminal_origin).encode()),(b"terminal_deadline_ns",str(terminal_deadline).encode()),(b"terminal_schedule_hex",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"candidate_deadline_ns",str(schedule[b"CANDIDATE_RECORD"]).encode())))
  b_send(control,finalize,schedule[b"CANDIDATE_RECORD"])
  notice_deadline=schedule[b"NOTICE"];notice_raw=recv_control(control,notice_deadline)
  candidate=parse_packet(notice_raw,b"V12_TERMINAL_CANDIDATE_DURABLE",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"chain_head_sha256",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"candidate_deadline_ns"),receiver_binding(b"WAIT_TERMINAL_CANDIDATE",b"NONE",b"NONE",notice_deadline))
  candidate_sha=h64(candidate[b"subject_sha256"])
  need(candidate[b"state"]==b"TERMINAL_CANDIDATE_DURABLE" and candidate[b"expected_state"]==b"WAIT_TERMINAL_CANDIDATE" and candidate[b"kind"]==b"SUCCESS_CANDIDATE" and candidate[b"ordinal"]==candidate[b"probe"]==b"NONE")
  need(udec(candidate[b"terminal_origin_ns"])==terminal_origin and udec(candidate[b"terminal_deadline_ns"])==terminal_deadline and candidate[b"terminal_schedule_hex"]==schedule_hex(schedule,TERMINAL_PHASE_SPEC))
  seen_deadline=schedule[b"TERMINAL_SEEN_RECORD"];peer_pre_state=b"WAIT_TERMINAL_SEEN";peer_deadline=seen_deadline
  seen=packet(b"V12_TERMINAL_SEEN",((b"state",b"TERMINAL_SEEN"),(b"expected_state",b"WAIT_TERMINAL_SEEN"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",b"SUCCESS_CANDIDATE"),(b"subject_sha256",candidate_sha),(b"notice_packet_sha256",sha(notice_raw)),(b"terminal_origin_ns",str(terminal_origin).encode()),(b"terminal_deadline_ns",str(terminal_deadline).encode()),(b"terminal_schedule_hex",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"seen_deadline_ns",str(seen_deadline).encode())))
  pass_may_be_committed=True;state=b"TERMINAL_SEEN_SEND_EFFECT_UNKNOWN";b_send(control,seen,seen_deadline);state=b"TERMINAL_SEEN_SENT"
  ack_deadline=schedule[b"ACK"];ack_raw=recv_control(control,ack_deadline)
  terminal=parse_packet(ack_raw,b"V12_TERMINAL_ACK",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"terminal_seen_sha256",b"report_sha256",b"pass_sha256",b"reconciliation_token",b"ack_state",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"ack_deadline_ns"),receiver_binding(b"WAIT_TERMINAL_ACK",b"NONE",b"NONE",ack_deadline))
  need(terminal[b"state"]==b"TERMINAL_ACK" and terminal[b"expected_state"]==b"WAIT_TERMINAL_ACK" and terminal[b"ordinal"]==terminal[b"probe"]==b"NONE" and terminal[b"kind"]==b"SUCCESS_CANDIDATE")
  need(terminal[b"subject_sha256"]==candidate_sha and terminal[b"ack_state"]==b"PASS_COMMITTED_NO_DOWNGRADE")
  need(udec(terminal[b"terminal_origin_ns"])==terminal_origin and udec(terminal[b"terminal_deadline_ns"])==terminal_deadline and terminal[b"terminal_schedule_hex"]==schedule_hex(schedule,TERMINAL_PHASE_SPEC))
  terminal_seen_sha=h64(terminal[b"terminal_seen_sha256"]);report_sha=h64(terminal[b"report_sha256"]);pass_sha=h64(terminal[b"pass_sha256"]);reconciliation_token=h64(terminal[b"reconciliation_token"])
  pass_authoritative=True;receipt_deadline=schedule[b"A_RECEIPT"];receipt_ns=time.monotonic_ns();peer_pre_state=b"WAIT_ACK_RECEIPT";peer_deadline=receipt_deadline
  receipt=packet(b"V12_TERMINAL_ACK_RECEIPT",((b"state",b"ACK_RECEIVED_NO_REPLAY"),(b"expected_state",b"WAIT_ACK_RECEIPT"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",b"SUCCESS_CANDIDATE"),(b"subject_sha256",candidate_sha),(b"ack_packet_sha256",sha(ack_raw)),(b"report_sha256",report_sha),(b"pass_sha256",pass_sha),(b"reconciliation_token",reconciliation_token),(b"actor_receipt_ns",str(receipt_ns).encode()),(b"terminal_origin_ns",str(terminal_origin).encode()),(b"terminal_deadline_ns",str(terminal_deadline).encode()),(b"terminal_schedule_hex",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"receipt_deadline_ns",str(receipt_deadline).encode())))
  receipt_effect_unknown=True;state=b"ACK_RECEIPT_SEND_EFFECT_UNKNOWN";b_send(control,receipt,receipt_deadline);receipt_effect_unknown=False;state=b"ACK_RECEIPT_SENT"
  closure_deadline=schedule[b"CLOSURE_PACKET"];closed=parse_packet(recv_control(control,closure_deadline),b"V12_TERMINAL_CLOSED",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"report_sha256",b"pass_sha256",b"ack_receipt_sha256",b"reconciliation_sha256",b"closure_sha256",b"owner",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"closure_deadline_ns"),receiver_binding(b"WAIT_OWNER_CLOSED",b"NONE",b"NONE",closure_deadline))
  need(closed[b"state"]==b"OWNER_CLOSED" and closed[b"expected_state"]==b"WAIT_OWNER_CLOSED" and closed[b"ordinal"]==closed[b"probe"]==b"NONE" and closed[b"kind"]==b"SUCCESS_CANDIDATE")
  need(closed[b"subject_sha256"]==candidate_sha and closed[b"report_sha256"]==report_sha and closed[b"pass_sha256"]==pass_sha and closed[b"owner"]==b"B")
  for key in (b"ack_receipt_sha256",b"reconciliation_sha256",b"closure_sha256"):need(h64(closed[key])!=b"0"*64)
  need(udec(closed[b"terminal_origin_ns"])==terminal_origin and udec(closed[b"terminal_deadline_ns"])==terminal_deadline and closed[b"terminal_schedule_hex"]==schedule_hex(schedule,TERMINAL_PHASE_SPEC))
  control.close();control=None
  braw=wait_status(bpid,0,schedule[b"B_EXIT"],b"PIDFD_ACTOR_LOST");bpid=-1;B_CHILD_PID=-1;B_CONTROL=None
  need(os.WIFEXITED(braw) and os.WEXITSTATUS(braw)==0,ConsumedIndeterminate)
  result=(b"P27E001_RUNNER_V12|AUTH_ID="+AUTH_ID+b"|entered=15|committed=15|candidate_sha256="+candidate_sha+b"|terminal_seen_sha256="+terminal_seen_sha+b"|report_sha256="+report_sha+b"|pass_sha256="+pass_sha+b"|ack_receipt_sha256="+closed[b"ack_receipt_sha256"]+b"|reconciliation_sha256="+closed[b"reconciliation_sha256"]+b"|owner_closure_sha256="+closed[b"closure_sha256"]+b"|owner_closed=1|retry_allowed=0\n")
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
   try:control.close()
   except BaseException:pass
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
  close_numbers(tuple(number for number in (cgfd,safefd,runtime,attempt_base,stage_base,cgroup_base) if number>=0))

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
P27 RUNNER V12 ACTOR SOURCE END C5A91E34

P27 RUNNER V12 WATCHDOG SOURCE BEGIN F5C2189D
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
CONTEXT_DOMAIN=b"P27E001_V12_DETACHED_ENVELOPE_CONTEXT\x00"
CERTIFICATE_DOMAIN=b"P27E001_V12_CERTIFICATE_DIGEST\x00"
ENVELOPE_TBS_DOMAIN=b"P27E001_V12_ENVELOPE_TBS\x00"
SIGNATURE_DOMAIN=b"P27E001_V12_ISSUER_SIGNATURE_PREIMAGE\x00"
RECEIPT_DOMAIN=b"P27E001_V12_ISSUER_RECEIPT\x00"
RESERVATION_TBS_DOMAIN=b"P27E001_V12_RESERVATION_TBS\x00"
RESERVATION_SIGNATURE_DOMAIN=b"P27E001_V12_RESERVATION_SIGNATURE\x00"
RESERVATION_RECEIPT_DOMAIN=b"P27E001_V12_RESERVATION_RECEIPT\x00"
FINAL_ENVELOPE_DOMAIN=b"P27E001_V12_FINAL_ENVELOPE\x00"
AUTH_DOMAIN=b"P27E001_V12_SESSION_AUTH\x00"
EXTERNAL_ACCEPTANCE_DOMAIN=b"P27E001_V12_EXTERNAL_ACCEPTANCE\x00"
ISSUER_KEY_BIND_DOMAIN=b"P27E001_V12_ISSUER_KEY_BIND\x00"
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
 b"V12_ABORT":(b"ABORTING",b"*",b"ABORT_NOTICE",b"control_deadline_ns"),
 b"V12_READY":(b"READY",b"WAIT_READY",b"NO_EFFECT",b"ready_deadline_ns"),
 b"V12_REFUSE_PREBEGIN":(b"REFUSE_PREBEGIN",b"WAIT_BEGIN",b"NO_CONSUME_REFUSAL",b"consume_deadline_ns"),
 b"V12_REFUSE_POSTARM":(b"REFUSE_POSTARM",b"WAIT_COMMIT",b"NO_CONSUME_REFUSAL",b"consume_deadline_ns"),
 b"V12_REFUSE_ACK":(b"REFUSAL_CLOSED_NO_CONSUME",b"WAIT_REFUSAL_ACK",b"REFUSAL_ACK_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V12_REFUSE_ACK_RECEIPT":(b"REFUSAL_ACK_RECEIVED",b"WAIT_REFUSAL_RECEIPT",b"NO_REPLAY_RECEIPT",b"consume_deadline_ns"),
 b"V12_REFUSAL_CLOSED":(b"REFUSAL_DURABLY_CLOSED",b"WAIT_REFUSAL_CLOSED",b"OWNER_CLOSURE",b"consume_deadline_ns"),
 b"V12_CONSUME_BEGIN":(b"CONSUME_BEGIN",b"WAIT_BEGIN",b"BEGIN_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V12_CONSUME_ARMED":(b"CONSUME_ARMED",b"WAIT_ARM",b"ARM_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V12_CONSUME_COMMIT":(b"CONSUME_COMMIT",b"WAIT_COMMIT",b"COMMIT_SEND_EFFECT_UNKNOWN",b"consume_deadline_ns"),
 b"V12_CONSUMED_DURABLE":(b"CONSUMED_DURABLE",b"WAIT_CONSUMED",b"INTENT_DURABLE",b"consume_deadline_ns"),
 b"V12_STAGE_DURABLE":(b"STAGE_DURABLE",b"WAIT_STAGE",b"FD_TRANSFER",b"stage_deadline_ns"),
 b"V12_STAGE_ACK":(b"STAGE_BOUND",b"WAIT_STAGE_ACK",b"STAGE_VERIFIED",b"stage_deadline_ns"),
 b"V12_CONTAINMENT":(b"CONTAINMENT_CANDIDATE",b"WAIT_CONTAINMENT",b"FD_TRANSFER",b"contain_deadline_ns"),
 b"V12_CONTAINMENT_ACK":(b"CONTAINMENT_BOUND",b"WAIT_CONTAINMENT_ACK",b"CONTAINMENT_VERIFIED",b"contain_deadline_ns"),
 b"V12_STREAM_ARM":(b"STREAM_ARM",b"WAIT_STREAM_ARM",b"FD_TRANSFER",b"launch_deadline_ns"),
 b"V12_STREAMS_ARMED":(b"STREAMS_ARMED",b"WAIT_STREAMS_ARMED",b"FD_VERIFIED",b"launch_deadline_ns"),
 b"V12_PIDFD_ARM":(b"PIDFD_ARM",b"WAIT_PIDFD_ARM",b"FD_TRANSFER",b"launch_deadline_ns"),
 b"V12_PIDFD_ARMED":(b"PIDFD_ARMED",b"WAIT_PIDFD_ARMED",b"PIDFD_VERIFIED",b"launch_deadline_ns"),
 b"V12_RELEASE_CANDIDATE":(b"RELEASE_CANDIDATE",b"WAIT_RELEASE",b"RELEASE_AUTHORIZATION",b"launch_deadline_ns"),
 b"V12_RELEASE_DURABLE":(b"RELEASE_DURABLE",b"WAIT_RELEASE_DURABLE",b"RELEASE_RECORD_DURABLE",b"launch_deadline_ns"),
 b"V12_RESULT":(b"RESULT",b"WAIT_RESULT",b"RESULT_NOTICE",b"result_deadline_ns"),
 b"V12_RESULT_FRAME":(b"RESULT_FRAME",b"WAIT_RESULT_FRAME",b"RESULT_FRAME",b"result_deadline_ns"),
 b"V12_RESULT_END":(b"RESULT_END",b"WAIT_RESULT_END",b"RESULT_COMPLETE",b"result_deadline_ns"),
 b"V12_VALIDATED_CANDIDATE":(b"VALIDATED_CANDIDATE",b"WAIT_VALIDATED",b"VALIDATION_NOTICE",b"ack_deadline_ns"),
 b"V12_VALIDATED_DURABLE":(b"VALIDATED_DURABLE",b"WAIT_VALIDATED_DURABLE",b"VALIDATED_RECORD_DURABLE",b"ack_deadline_ns"),
 b"V12_ACK_COMMIT_INTENT":(b"ACK_COMMIT_INTENT",b"WAIT_ACK_INTENT",b"ACK_COMMIT",b"ack_deadline_ns"),
 b"V12_COMMITTED":(b"COMMITTED",b"WAIT_COMMITTED",b"COMMIT_RECORD_DURABLE",b"ack_deadline_ns"),
 b"V12_COMMITTED_SEEN":(b"COMMITTED_SEEN",b"WAIT_COMMITTED_SEEN",b"ACK_RECEIPT",b"ack_deadline_ns"),
 b"V12_EMPTY_FINAL_QUERY":(b"EMPTY_FINAL_QUERY",b"WAIT_EMPTY_QUERY",b"REMOVE_QUERY",b"remove_deadline_ns"),
 b"V12_EMPTY_FINAL_CONFIRMED":(b"EMPTY_FINAL_CONFIRMED",b"WAIT_EMPTY_CONFIRMED",b"EMPTY_OBSERVED",b"remove_deadline_ns"),
 b"V12_CGROUP_REMOVED":(b"CGROUP_REMOVED",b"WAIT_REMOVED",b"REMOVE_EFFECT",b"remove_deadline_ns"),
 b"V12_REMOVE_ACK":(b"REMOVE_ACK",b"WAIT_REMOVE_ACK",b"REMOVAL_VERIFIED",b"remove_deadline_ns"),
 b"V12_FINALIZE_CANDIDATE":(b"FINALIZE_CANDIDATE",b"WAIT_FINALIZE",b"FINALIZE_NOTICE",b"candidate_deadline_ns"),
 b"V12_TERMINAL_CANDIDATE_DURABLE":(b"TERMINAL_CANDIDATE_DURABLE",b"WAIT_TERMINAL_CANDIDATE",b"CANDIDATE_DURABLE",b"candidate_deadline_ns"),
 b"V12_TERMINAL_FAILURE_DURABLE":(b"TERMINAL_FAILURE_DURABLE",b"WAIT_TERMINAL_FAILURE",b"FAILURE_REPORT_DURABLE",b"candidate_deadline_ns"),
 b"V12_TERMINAL_SEEN":(b"TERMINAL_SEEN",b"WAIT_TERMINAL_SEEN",b"TERMINAL_SEEN",b"seen_deadline_ns"),
 b"V12_TERMINAL_ACK":(b"TERMINAL_ACK",b"WAIT_TERMINAL_ACK",b"ACK_SEND_EFFECT_UNKNOWN",b"ack_deadline_ns"),
 b"V12_TERMINAL_ACK_RECEIPT":(b"ACK_RECEIVED_NO_REPLAY",b"WAIT_ACK_RECEIPT",b"NO_REPLAY_RECEIPT",b"receipt_deadline_ns"),
 b"V12_TERMINAL_CLOSED":(b"OWNER_CLOSED",b"WAIT_OWNER_CLOSED",b"OWNER_CLOSURE",b"closure_deadline_ns")
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
 if kind==b"V12_ABORT":need(state==spec_state and effect==spec_effect and receiver not in (b"",b"*"))
 else:need((state,receiver,effect)==(spec_state,spec_receiver,spec_effect) and state!=b"*" and receiver!=b"*" and effect!=b"*")
 ordinal=provided.pop(b"ordinal");probe=provided.pop(b"probe")
 if b"auth_id" in provided:need(provided.pop(b"auth_id")==AUTH)
 if b"sender" in provided:need(provided.pop(b"sender")==b"B")
 need(deadline_key in provided);deadline=provided.pop(deadline_key);udec(deadline,1)
 need(not any(key in CONTROL_RESERVED for key in provided))
 CONTROL_SEND_SEQ+=1
 transition=state+b"->"+receiver+b":"+effect
 body=(kind+b"|protocol_version=12|session_id="+AUTH+b"|message_seq="+str(CONTROL_SEND_SEQ).encode()+b"|message_sender="+b"B"+b"|transition_id="+transition+b"|sender_state="+state+b"|expected_receiver_state="+receiver+b"|slot_ordinal="+ordinal+b"|slot_probe="+probe+b"|effect_state="+effect+b"|deadline_name="+deadline_key+b"|absolute_deadline_ns="+deadline)
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
 if kind!=b"V12_ABORT" and raw.startswith(b"V12_ABORT|"):
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
 need(common[b"protocol_version"]==b"12" and common[b"session_id"]==AUTH and common[b"message_sender"]==b"A")
 need(common[b"transition_id"]==common[b"sender_state"]+b"->"+common[b"expected_receiver_state"]+b":"+common[b"effect_state"])
 if kind==b"V12_ABORT":need(common[b"sender_state"]==spec_state and common[b"effect_state"]==spec_effect and common[b"expected_receiver_state"] not in (b"",b"*"))
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
 values=parse_packet(raw,b"V12_ABORT",keys,binding)
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
 body=b"P27E001_ISSUER_CONTEXT_V12\n"
 for key in ENVELOPE_CONTEXT_KEYS:body+=key+b"="+values[key]+b"\n"
 return domain_frame(CONTEXT_DOMAIN,b"ENVELOPE_CONTEXT_RAW",body+b"CONTEXT_END=1\n")

def envelope_tbs(values,certificate_digest):
 body=b"P27E001_ISSUER_ENVELOPE_TBS_V12\n"
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
 values=parse_fixed(raw,b"P27E001_ISSUER_ENVELOPE_V12",ENVELOPE_KEYS,b"ENVELOPE_END=1")
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V12",b"E0366_SNAPSHOT_BYTES":str(SNAPSHOT_EXPECT[0]).encode(),b"E0366_SNAPSHOT_LF":str(SNAPSHOT_EXPECT[1]).encode(),b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"V15_SHA256":V15_SHA,b"ONE_SHOT_RESERVED_BY_ISSUER":b"1",b"ONE_SHOT_CONSUMED_BY_ISSUER":b"0",b"SIGNATURE_ALGORITHM":b"ED25519_EXTERNAL_GATE_V12"}
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
 body=b"P27E001_ISSUER_RESERVATION_TBS_V12\n"
 for key in RESERVATION_TBS_KEYS:body+=key+b"="+values[key]+b"\n"
 return domain_frame(RESERVATION_TBS_DOMAIN,b"RESERVATION_TBS_RAW",body+b"RESERVATION_TBS_END=1\n")

def reservation_signature_preimage(tbs):
 payload=length_frame(b"RESERVATION_TBS",tbs)+b"RESERVATION_SIGNATURE_PREIMAGE_END=1\n"
 return domain_frame(RESERVATION_SIGNATURE_DOMAIN,b"RESERVATION_SIGNATURE_TBS_RAW",payload)

def reservation_receipt_preimage(tbs,signature_digest,algorithm,signature):
 payload=length_frame(b"RESERVATION_TBS",tbs)+b"SIGNATURE_PREIMAGE_SHA256="+signature_digest+b"\nSIGNATURE_ALGORITHM="+algorithm+b"\nSIGNATURE_HEX="+signature+b"\nRESERVATION_RECEIPT_END=1\n"
 return domain_frame(RESERVATION_RECEIPT_DOMAIN,b"RESERVATION_RECEIPT_TBS_RAW",payload)

def parse_reservation(raw):
 values=parse_fixed(raw,b"P27E001_ISSUER_RESERVATION_V12",RESERVATION_KEYS,b"RESERVATION_END=1")
 need(values[b"ISSUER_ID"]==b"P27_HOST_PREMISE_ISSUER_V12" and values[b"ONE_SHOT_RESERVED_BY_ISSUER"]==b"1" and values[b"ONE_SHOT_CONSUMED_BY_ISSUER"]==b"0")
 need(values[b"SIGNATURE_ALGORITHM"]==b"ED25519_EXTERNAL_GATE_V12")
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
 need(lines and lines[0]==b"P27E001_PREMISE_CERTIFICATE_V12" and lines[-1]==b"CERTIFICATE_END=1")
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
 exact={b"ISSUER_ID":b"P27_HOST_PREMISE_ISSUER_V12",b"ARCH":b"x86_64",b"ABSOLUTE_LIFETIME_NS":b"360000000000",b"REALTIME_MONOTONIC_MAX_DRIFT_NS":b"1000000",b"E0366_SNAPSHOT_BYTES":b"2303269",b"E0366_SNAPSHOT_LF":b"23672",b"E0366_SNAPSHOT_SHA256":SNAPSHOT_EXPECT[2],b"E0366_SNAPSHOT_TERMINAL_HEX":SNAPSHOT_TERMINAL_HEX,b"HISTORICAL_SNAPSHOT_SEALED":b"1",b"V15_SHA256":V15_SHA,b"V8_SHA256":V8_SHA,b"ACTOR_ENTRY_CAPS":b"00000000000401c0",b"ACTOR_ENTRY_NNP":b"0",b"ACTOR_ENTRY_SECUREBITS":b"12",b"PAYLOAD_FINAL_CAPS":b"0000000000000000",b"PAYLOAD_FINAL_NNP":b"1",b"PAYLOAD_FINAL_SECUREBITS":b"15",b"ATTEMPT_BASE_MODE":b"40700",b"ATTEMPT_BASE_UID":b"0",b"ATTEMPT_BASE_GID":b"0",b"CGROUP2_FS_MAGIC":b"63677270",b"CGROUP_BASE_UID":b"0",b"CGROUP_BASE_GID":b"0",b"CGROUP_NO_EXTERNAL_MUTATOR":b"1",b"CGROUP_CHILD_MODE":b"40700",b"CGROUP_CHILD_UID":b"0",b"CGROUP_CHILD_GID":b"0",b"CGROUP_CHILD_TYPE_HEX":b"646f6d61696e0a",b"RUNTIME_ROOT_UID":b"0",b"RUNTIME_ROOT_GID":b"0",b"SAFE_BIND_MODE":b"40700",b"SAFE_BIND_UID":b"0",b"SAFE_BIND_GID":b"0",b"SAFE_BIND_NOEXEC":b"1",b"SAFE_BIND_WRITABLE_DESCENDANT_COUNT":b"1",b"KEEPER_BYTES":b"4216",b"KEEPER_LF":b"128",b"KEEPER_SHA256":b"e3bf14ddde012be70a0ec40ac9373c055d2fd79d3ea30aa5e64450174f057716",b"LAUNCHER_BYTES":b"4218",b"LAUNCHER_LF":b"128",b"LAUNCHER_SHA256":b"e9d5eb3544dfddd7251279294e113f053165c2d446dd4517fbcdc6927a8618d5",b"MARKER_BYTES":b"75094",b"MARKER_LF":b"1479",b"MARKER_SHA256":b"b06ceed041004279e9df73cc9cc3c2d73ec07d8f71a9345f451a32e93b7a955d",b"CHILD_BYTES":b"19746",b"CHILD_LF":b"452",b"CHILD_SHA256":b"1d20310b965ff9df9351cbc3ca07aebb15e8cbacf74a8058782c085fde0780bf",b"PYTHON_IMAGE_SHA256":PY_SHA,b"PYTHON_IMAGE_BYTES":b"30626264",b"PYTHON_IMAGE_UID":b"0",b"PYTHON_IMAGE_GID":b"0",b"LIBC_UID":b"0",b"LIBC_GID":b"0",b"PRECONSUMPTION_CAP_NS":b"10000000000",b"CONSUMPTION_PROGRESS_NS":b"250000000",b"ATTEMPT_DIRFD_PROGRESS_NS":b"100000000",b"STAGING_CAP_NS":b"10000000000",b"RELEASE_PROGRESS_NS":b"1000000000",b"RELEASE_RECORD_ABSOLUTE_OFFSET_NS":b"800000000",b"RELEASE_REPLY_ABSOLUTE_OFFSET_NS":b"900000000",b"SIGCONT_CALL_RETURN_NS":b"5000000",b"DURABLE_RECORD_PROGRESS_NS":b"100000000",b"WATCHDOG_ARM_PROGRESS_NS":b"1000000000",b"WATCHDOG_ACK_PROGRESS_NS":b"500000000",b"WATCHDOG_SURVIVES_CONSUME_TO_REPORT":b"1",b"WATCHDOG_SURVIVES_KILL_TO_EMPTY":b"1",b"CGROUP_KILL_WRITE_RETURN_NS":b"5000000",b"CGROUP_KILL_TO_EMPTY_NS":b"2000000000",b"FINAL_REPORT_PROGRESS_NS":b"1000000000",b"FINAL_PASS_COMMIT_PROGRESS_NS":b"100000000",b"FINAL_PASS_MARGIN_NS":b"10000000",b"TERMINAL_HANDSHAKE_PROGRESS_NS":b"500000000",b"A_RECEIPT_PROGRESS_NS":b"100000000",b"B_CLOSURE_PROGRESS_NS":b"500000000",b"TERMINAL_CANDIDATE_RECORD_NS":b"100000000",b"TERMINAL_NOTICE_PROGRESS_NS":b"100000000",b"TERMINAL_SEEN_RECORD_NS":b"100000000",b"TERMINAL_ACK_RECEIPT_RECORD_NS":b"100000000",b"TERMINAL_RECONCILIATION_RECORD_NS":b"100000000",b"TERMINAL_OWNER_CLOSURE_RECORD_NS":b"100000000",b"TERMINAL_CLOSURE_PACKET_NS":b"100000000",b"TERMINAL_B_EXIT_NS":b"100000000",b"FAILURE_OVERALL_PROGRESS_NS":b"5210000000",b"FAILURE_CLEANUP_EFFECT_PROGRESS_NS":b"2600000000",b"FAILURE_TAIL_RESERVE_NS":b"2610000000",b"REFUSAL_RECORD_PROGRESS_NS":b"20000000",b"REFUSAL_ACK_PROGRESS_NS":b"20000000",b"REFUSAL_RECEIPT_WAIT_PROGRESS_NS":b"30000000",b"REFUSAL_FINALITY_COMMIT_PROGRESS_NS":b"10000000",b"REFUSAL_FINALITY_DEADLINE_PROGRESS_NS":b"80000000",b"REFUSAL_OFFER_BUILD_PROGRESS_NS":b"10000000",b"REFUSAL_OFFER_SEND_PROGRESS_NS":b"20000000",b"REFUSAL_ACCEPTANCE_RECV_PROGRESS_NS":b"30000000",b"REFUSAL_ACCEPTANCE_VERIFY_PROGRESS_NS":b"20000000",b"REFUSAL_ACCEPTANCE_COMMIT_PROGRESS_NS":b"10000000",b"REFUSAL_ACTOR_CLOSURE_PROGRESS_NS":b"20000000",b"REFUSAL_CAPABILITY_CLOSE_PROGRESS_NS":b"10000000",b"REFUSAL_OWNER_RELEASE_PROGRESS_NS":b"10000000",b"REFUSAL_CLOSURE_TAIL_NS":b"130000000",b"REFUSAL_CLOSURE_DEADLINE_PROGRESS_NS":b"210000000",b"FINAL_TERMINAL_TOTAL_NS":b"2510000000",b"ENTRY_MIN_REMAINING_NS":b"295482000000",b"CONSUMPTION_MIN_REMAINING_NS":b"285482000000",b"PRE_STAGE_MIN_REMAINING_NS":b"285232000000",b"POST_STAGE_MIN_REMAINING_NS":b"275232000000",b"POST_CONTAIN_MIN_REMAINING_NS":b"274732000000",b"ACTOR_RELEASE_DISABLE_PROGRESS_NS":b"500000000",b"EXTERNAL_OWNER_UID":b"0",b"EXTERNAL_OWNER_GID":b"0",b"CLONE3_CPYTHON_GATE_PASS":b"1",b"DELETED_CGROUP_FD_GATE_PASS":b"1",b"SEALED_SNAPSHOT_CONSTRUCTION_GATE_PASS":b"1",b"EXTERNAL_SURVIVAL_GATE_PASS":b"1",b"OUTER_RECONCILER_GATE_PASS":b"1",b"ISSUER_CRYPTOGRAPHY_GATE_PASS":b"1"}
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
  number=os.open(b"/proc/self/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(number,65536),65536)
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
 for key,value in limit_vector():need(resource.getrlimit(key)==value)
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
  info=os.open(b"/proc/self/fdinfo/"+str(number).encode(),os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(info,4096),4096)
 finally:close_numbers(tuple(x for x in (info,) if x>=0))
 values=[x[5:] for x in raw.splitlines() if x.startswith(b"Pid:\t")];need(len(values)==1)
 return udec(values[0],1)

def proc_starttime(pid):
 number=-1
 try:
  number=os.open(b"/proc/"+str(pid).encode()+b"/stat",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(number,4096),4096)
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
  info=os.open(b"/proc/self/fdinfo/"+str(number).encode(),os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(info,4096),4096)
 finally:close_numbers(tuple(x for x in (info,) if x>=0))
 mids=[x[7:] for x in raw.splitlines() if x.startswith(b"mnt_id:\t")];need(len(mids)==1);mid=udec(mids[0],1);table=-1
 try:
  table=os.open(b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);rows=ascii_file(read_all(table,1048576),1048576)
 finally:close_numbers(tuple(x for x in (table,) if x>=0))
 matches=[line+b"\n" for line in rows.splitlines() if line.split(b" ",1)[0]==str(mid).encode()]
 need(len(matches)==1);return mid,matches[0]

def verify_platform(cert):
 boot=-1
 try:
  boot=os.open(b"/proc/sys/kernel/random/boot_id",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);boot_raw=read_all(boot,128)
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
  number=os.open(b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=ascii_file(read_all(number,1048576),1048576)
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
  rootfd=os.open(b"/",O_DIR);current=os.dup(rootfd)
  for part in parts[:-1]:
   following=os.open(part,O_DIR,dir_fd=current);os.close(current);current=following;following=-1
  if role==b"PYTHON_LINK":
   held=os.stat(parts[-1],dir_fd=current,follow_symlinks=False);need(stat.S_ISLNK(held.st_mode))
   target=os.readlink(parts[-1],dir_fd=current);size=len(target);digest=sha(target)
  else:
   number=os.open(parts[-1],os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=current)
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
 poller=select.poll();poller.register(4,select.POLLIN|select.POLLHUP|select.POLLERR)
 control=context.get(b"actor_control")
 if control is not None and context.get(b"control_state")==b"CONNECTED":poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR)
 amask=cmask=0
 for number,event in poller.poll(0):
  if number==4:amask|=event
  elif control is not None and number==control.fileno():cmask|=event
 if amask:
  context[b"actor_state"]=b"PIDFD_ACTOR_LOST";context[b"actor_lost"]=True;raise PidfdActorLost("certified-boundary")
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
 return b"P27E001_RECORD_SEMANTIC_DELTA_V12\n"+b"".join(b"ITEM="+str(len(item)).encode()+b":"+item+b"\n" for item in delta)+b"DELTA_END=1\n"

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
 if carrier>=0:
  try:os.close(carrier)
  except OSError:pass
  context[b"pending_expected_raw_fd"]=-1
 context[b"record_seq"]=seq;context[b"record_pending"]=None;context[b"record_sequence_frozen"]=False;context[b"uncertain_record"]=None;context[b"carrier_pre_effect_state"]=b"DELTA_APPLIED_SUCCESSOR_OPEN"

def construct_pending_expected_raw_carrier_before_reservation(context,raw,deadline,require_live,needed_after):
 need(context.get(b"record_pending") is None and not context.get(b"record_sequence_frozen") and context.get(b"record_draft") is not None)
 number=-1;existing=context.get(b"pending_expected_raw_fd",-1)
 if existing>=0:
  need(sealed_carrier(existing,len(raw))==raw);os.lseek(existing,0,os.SEEK_SET);return existing
 try:
  record_boundary(context,deadline,require_live,needed_after);number=os.memfd_create("p27-e001-pending-raw-v12",os.MFD_CLOEXEC|os.MFD_ALLOW_SEALING)
  write_all(number,raw,context,deadline,require_live,needed_after);os.lseek(number,0,os.SEEK_SET)
  fcntl.fcntl(number,fcntl.F_ADD_SEALS,EXACT_SEALS);record_boundary(context,deadline,require_live,needed_after)
  need(sealed_carrier(number,len(raw))==raw);os.lseek(number,0,os.SEEK_SET)
  context[b"pending_expected_raw_fd"]=number;number=-1;return context[b"pending_expected_raw_fd"]
 finally:
  if number>=0:
   try:os.close(number)
   except OSError:pass

def reconcile_pending_record(context,deadline,require_live=False,needed_after=0):
 pending=context.get(b"record_pending");need(context.get(b"record_sequence_frozen") and pending is not None)
 seq,predecessor,name,digest,semantic_delta=pending;semantic_delta_bytes(semantic_delta);raw=context[b"durability_raw"][name];number=-1
 try:
  record_boundary(context,deadline,require_live,needed_after)
  try:number=os.open(name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"attempt"])
  except FileNotFoundError:
   record_boundary(context,deadline,require_live,needed_after);os.fsync(context[b"attempt"]);record_boundary(context,deadline,require_live,needed_after)
   try:number=os.open(name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"attempt"])
   except FileNotFoundError:
    state=b"ABSENT_RECONCILED_SAME_RESERVATION";context[b"durability"][name]=state;return state,digest
   else:raise FaultSet({b"RECONCILIATION_UNKNOWN"})
  opened=os.fstat(number);named=os.stat(name,dir_fd=context[b"attempt"],follow_symlinks=False);again=read_all(number,len(raw))
  need((opened.st_dev,opened.st_ino,opened.st_mode,opened.st_nlink,opened.st_uid,opened.st_gid,opened.st_size)==(named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid,named.st_size))
  need(stat.S_ISREG(opened.st_mode) and stat.S_IMODE(opened.st_mode)==0o400 and opened.st_nlink==1 and opened.st_uid==opened.st_gid==0 and again==raw and sha(again)==digest)
  os.close(number);number=-1;record_boundary(context,deadline,require_live,needed_after);os.fsync(context[b"attempt"]);record_boundary(context,deadline,require_live,needed_after)
  context[b"durability"][name]=b"DIR_FSYNC_VERIFIED_DELTA_PENDING";commit_record_reservation(context,name,digest);return DURABLE_VERIFIED,digest
 except BaseException:
  context[b"record_sequence_frozen"]=True;context[b"faults"].add(b"RECONCILIATION_UNKNOWN");raise FaultSet({b"RECONCILIATION_UNKNOWN"})
 finally:
  if number>=0:
   try:os.close(number)
   except OSError:pass

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
  if carrier>=0:
   try:os.close(carrier)
   except OSError:pass
  context[b"pending_expected_raw_fd"]=-1;context[b"record_draft"]=None;context[b"record_pending"]=None;context[b"record_sequence_frozen"]=False;context[b"uncertain_record"]=None
  return b"CARRIER_FAILED_NON_PENDING_PRE_EFFECT",digest
 state=b"ABSENT_KNOWN";context[b"durability"][name]=state;context[b"durability_digest"][name]=digest;context[b"durability_raw"][name]=raw;context[b"durability_faults"][name]=set();number=reopened=-1;created=None
 try:
  freeze_record_reservation(context,name,digest)
  record_boundary(context,deadline,require_live,needed_after)
  state=b"OPEN_EFFECT_UNKNOWN";context[b"durability"][name]=state
  number=os.open(name,os.O_RDWR|os.O_CREAT|os.O_EXCL|os.O_CLOEXEC|os.O_NOFOLLOW,0o400,dir_fd=context[b"attempt"])
  record_boundary(context,deadline,require_live,needed_after);state=b"FD_HELD";context[b"durability"][name]=state
  state=b"WRITE_EFFECT_UNKNOWN";context[b"durability"][name]=state
  write_all(number,raw,context,deadline,require_live,needed_after)
  state=b"FILE_FSYNC_EFFECT_UNKNOWN";context[b"durability"][name]=state
  record_boundary(context,deadline,require_live,needed_after);os.fsync(number);record_boundary(context,deadline,require_live,needed_after)
  held=os.fstat(number);record_boundary(context,deadline,require_live,needed_after)
  need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o400 and held.st_uid==held.st_gid==0 and held.st_nlink==1 and held.st_size==len(raw))
  created=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,held.st_size)
  os.close(number);number=-1;state=b"CREATED_FD_CLOSED";context[b"durability"][name]=state
  state=b"NAMED_REOPEN_EFFECT_UNKNOWN";context[b"durability"][name]=state
  reopened=os.open(name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"attempt"]);record_boundary(context,deadline,require_live,needed_after)
  opened=os.fstat(reopened);named=os.stat(name,dir_fd=context[b"attempt"],follow_symlinks=False)
  reopened_identity=(opened.st_dev,opened.st_ino,opened.st_mode,opened.st_nlink,opened.st_uid,opened.st_gid,opened.st_size);named_identity=(named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid,named.st_size)
  need(created==reopened_identity==named_identity and read_all(reopened,len(raw))==raw);record_boundary(context,deadline,require_live,needed_after)
  os.close(reopened);reopened=-1;state=b"NAMED_ENTRY_REREAD_VERIFIED";context[b"durability"][name]=state
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
  for held_number in (number,reopened):
   if held_number>=0:
    try:os.close(held_number)
    except OSError:pass
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
  try:os.close(number)
  except OSError:pass

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
 return (b"P27E001_ATTEMPT_INTENT_V12\nAUTH_ID="+auth+b"\nNONCE="+auth+b"\nRECORD_SEQ=1\nPREDECESSOR_SHA256=NONE\nISSUER_FINAL_ENVELOPE_SHA256="+sha(envelope_raw)+b"\nCERTIFICATE_SHA256="+sha(cert_raw)+b"\nPLAN_SHA256="+cert[b"PLAN_SHA256"]+b"\nRUNNER_SHA256="+cert[b"RUNNER_SHA256"]+b"\nRECOVERY_SHA256="+sha(source_raw)+b"\nE0366_SNAPSHOT_BYTES=2303269\nE0366_SNAPSHOT_LF=23672\nE0366_SNAPSHOT_SHA256="+SNAPSHOT_EXPECT[2]+b"\nE0366_SNAPSHOT_TERMINAL_HEX="+SNAPSHOT_TERMINAL_HEX+b"\nV15_SHA256="+cert[b"V15_SHA256"]+b"\nSUITE="+b",".join(PROBES)+b"\nATTEMPT_PATH_HEX="+(b"/var/lib/p27-e001-host-v15/attempts/"+auth).hex().encode()+b"\nSTAGE_PATH_HEX="+(b"/tmp/p27-e001-host-v15/"+auth).hex().encode()+b"\nCGROUP_PATH_HEX="+(b"/sys/fs/cgroup/p27-e001-host-v15/"+auth).hex().encode()+b"\nACTOR_ENTRY_CAPS=00000000000401c0\nPAYLOAD_FINAL_CAPS=0000000000000000\nABSOLUTE_EXPIRY_REALTIME_NS="+cert[b"ABSOLUTE_EXPIRY_REALTIME_NS"]+b"\nCONSUMED_OR_EFFECT_UNKNOWN=1\nRETRY_ALLOWED=0\nINTENT_END=1\n")

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
   os.close(context[b"attempt_base_fd"]);context[b"attempt_base_fd"]=-1;context[b"attempt_base_closed_on_collision"]=True;context[b"attempt_state"]=b"COLLISION_CLOSED"
  except BaseException:
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
  number=os.open(AUTH,os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=5)
  post_deadline(deadline);checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
  verify_attempt_fd(number);context[b"local_fd_state"]=b"LOCAL_VERIFIED";checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
  context[b"attempt"]=number;number=-1;context[b"local_fd_state"]=b"LOCAL_VERIFIED_HELD";context[b"attempt_state"]=b"LOCAL_VERIFIED_HELD";context[b"consumption_state"]=b"DIRFD_HELD_VERIFIED"
 except CertificateExpired:
  context[b"consumption_state"]=b"DIRFD_EFFECT_UNKNOWN";context[b"faults"].update((b"CERTIFICATE_EXPIRED",b"ATTEMPT_DIRFD_UNKNOWN"))
  raise
 except BaseException as error:
  context[b"consumption_state"]=b"DIRFD_EFFECT_UNKNOWN";context[b"faults"].add(b"ATTEMPT_DIRFD_UNKNOWN")
  raise FaultSet(set(context[b"faults"])) from error
 finally:
  if number>=0:
   try:os.close(number)
   except OSError:pass
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
 os.close(context[b"attempt_base_fd"]);context[b"attempt_base_fd"]=-1
 return digest

def release_record(context,values):
 seq=next_record(context);predecessor=context[b"chain_sha"];origin=time.monotonic_ns();deadline=udec(values[b"release_record_deadline_ns"]);need(origin<=deadline and deadline==udec(values[b"release_origin_ns"])+RELEASE_RECORD_OFFSET_NS)
 body=(b"P27E001_RELEASE_STATE_V12\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+predecessor+b"\nORDINAL="+values[b"ordinal"]+b"\nPROBE="+values[b"probe"]+b"\nOUTER_PID="+values[b"outer_pid"]+b"\nOUTER_STARTTIME="+values[b"outer_starttime"]+b"\nPIDFD_BOUND="+values[b"pidfd_bound"]+b"\nPIDFD_EXIT_READY_OBSERVED=0\nSTOPPED_RAW_STATUS="+values[b"stopped_raw_status"]+b"\nCGROUP_MEMBER="+values[b"cgroup_member"]+b"\nCGROUP_DEV="+values[b"cgroup_dev"]+b"\nCGROUP_INO="+values[b"cgroup_ino"]+b"\nCGROUP_MODE="+values[b"cgroup_mode"]+b"\nCGROUP_NLINK="+values[b"cgroup_nlink"]+b"\nCGROUP_UID="+values[b"cgroup_uid"]+b"\nCGROUP_GID="+values[b"cgroup_gid"]+b"\nARGV_SHA256="+values[b"argv_sha256"]+b"\nENV_SHA256="+values[b"env_sha256"]+b"\nRELEASE_ORIGIN_NS="+values[b"release_origin_ns"]+b"\nLAUNCH_OVERALL_DEADLINE_NS="+values[b"launch_overall_deadline_ns"]+b"\nRELEASE_RECORD_DEADLINE_NS="+values[b"release_record_deadline_ns"]+b"\nRELEASE_REPLY_DEADLINE_NS="+values[b"release_reply_deadline_ns"]+b"\nB_RECORD_ORIGIN_NS="+str(origin).encode()+b"\nB_RECORD_DEADLINE_NS="+str(deadline).encode()+b"\nCERTIFICATE_EXPIRY_REALTIME_NS="+CERT[b"ABSOLUTE_EXPIRY_REALTIME_NS"]+b"\nSTATE=RELEASE_AUTHORIZED\nRELEASE_END=1\n")
 state,digest=durable_once(context,b"release-"+values[b"probe"]+b".v5",body,deadline,True,udec(values[b"launch_overall_deadline_ns"])-deadline,(b"RELEASE",values[b"probe"]))
 if state!=DURABLE_VERIFIED:raise FaultSet({b"RELEASE_RECORD_DURABILITY_UNKNOWN"})
 context[b"chain_sha"]=digest;context[b"release_sha"]=digest;return digest

CANDIDATE_KEYS=(b"ordinal",b"probe",b"release_record_sha256",b"release_origin_ns",b"release_return_ns",b"host_complete_ns",b"capture_done_ns",b"direct_wait_state",b"outer_raw_status",b"pidfd_bound",b"pidfd_exit_ready_observed",b"stdout_len",b"stdout_sha256",b"stdout_eof",b"stdout_overflow",b"stderr_len",b"stderr_sha256",b"stderr_eof",b"stderr_overflow",b"cgroup_empty",b"parser_language",b"parser_structure",b"parser_semantics",b"candidate",b"terminal",b"certificate_expiry_realtime_ns")
FINAL_REPORT_KEYS=(b"AUTH_ID",b"RECORD_SEQ",b"PREDECESSOR_SHA256",b"OUTCOME_KIND",b"SUITE",b"ENTERED_COUNT",b"COMMITTED_COUNT",b"REAPED_COUNT",b"STOPPED_COUNT",b"STOP_ORDINAL",b"STOP_PROBE",b"STAGE_STATE",b"ATTEMPT_STATE",b"CONTAINMENT_STATE",b"EMPTY_STATE",b"REMOVAL_STATE",b"PRIMARY",b"FAULT_SET",b"CHAIN_BEFORE_REPORT_SHA256",b"KILL_CALL_COUNT",b"KILL_STATE",b"KILL_TICKET_STATE",b"ACK_STATE",b"RECONCILIATION_STATE",b"OWNER_CLOSURE_STATE",b"FAILURE_ORIGIN_NS",b"CLEANUP_EFFECT_DEADLINE_NS",b"TERMINAL_ORIGIN_NS",b"TERMINAL_DEADLINE_NS",b"TERMINAL_SCHEDULE_HEX",b"CERTIFICATE_LIVE_AT_REPORT",b"RETRY_ALLOWED",b"DISPOSITION",b"PHASE_DEADLINE_NS")

def forensic_body(values):
 return (b"RELEASE_ORIGIN_NS="+values[b"release_origin_ns"]+b"\nRELEASE_RETURN_NS="+values[b"release_return_ns"]+b"\nHOST_COMPLETE_NS="+values[b"host_complete_ns"]+b"\nCAPTURE_DONE_NS="+values[b"capture_done_ns"]+b"\nDIRECT_WAIT="+values[b"direct_wait_state"]+b"\nOUTER_RAW_STATUS="+values[b"outer_raw_status"]+b"\nPIDFD_BOUND="+values[b"pidfd_bound"]+b"\nPIDFD_EXIT_READY_OBSERVED="+values[b"pidfd_exit_ready_observed"]+b"\nSTDOUT_BYTES="+values[b"stdout_len"]+b"\nSTDOUT_SHA256="+values[b"stdout_sha256"]+b"\nSTDOUT_EOF="+values[b"stdout_eof"]+b"\nSTDOUT_OVERFLOW="+values[b"stdout_overflow"]+b"\nSTDERR_BYTES="+values[b"stderr_len"]+b"\nSTDERR_SHA256="+values[b"stderr_sha256"]+b"\nSTDERR_EOF="+values[b"stderr_eof"]+b"\nSTDERR_OVERFLOW="+values[b"stderr_overflow"]+b"\nCGROUP_EMPTY="+values[b"cgroup_empty"]+b"\nPARSER_LANGUAGE="+values[b"parser_language"]+b"\nPARSER_STRUCTURE="+values[b"parser_structure"]+b"\nPARSER_SEMANTICS="+values[b"parser_semantics"]+b"\nCANDIDATE="+values[b"candidate"]+b"\nTERMINAL="+values[b"terminal"]+b"\nCERTIFICATE_EXPIRY_REALTIME_NS="+values[b"certificate_expiry_realtime_ns"]+b"\nTOPOLOGY=V15_INTERNAL_VALIDATION_REPORTED_BY_COMPLETE_TRANSCRIPT\nEXTERNAL_TOPOLOGY_RECONSTRUCTION=UNAVAILABLE\n")

def validated_record(context,values,ack_deadline):
 seq=next_record(context);origin=time.monotonic_ns();deadline=min(ack_deadline,origin+RECORD_NS);need(origin+RECORD_NS<=ack_deadline)
 body=(b"P27E001_PROBE_STATE_V12\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+context[b"chain_sha"]+b"\nORDINAL="+values[b"ordinal"]+b"\nPROBE="+values[b"probe"]+b"\nSTATE=VALIDATED_CANDIDATE\n"+forensic_body(values)+b"B_RECORD_ORIGIN_NS="+str(origin).encode()+b"\nB_RECORD_DEADLINE_NS="+str(deadline).encode()+b"\nRECORD_END=1\n")
 state,digest=durable_once(context,b"receipt-"+values[b"probe"]+b"-validated.v5",body,deadline,True,0,(b"VALIDATED",values[b"probe"])+tuple(values[key] for key in CANDIDATE_KEYS))
 if state!=DURABLE_VERIFIED:raise FaultSet({b"VALIDATED_DURABILITY_UNKNOWN"})
 context[b"chain_sha"]=digest;context[b"validated_sha"]=digest;context[b"validated_values"]=dict(values);return digest

def ack_intent_record(context,ordinal,probe,actor_ack,received,ack_deadline):
 values=context[b"validated_values"];seq=next_record(context);origin=time.monotonic_ns();deadline=min(ack_deadline,origin+RECORD_NS);need(origin+RECORD_NS<=ack_deadline)
 body=(b"P27E001_PROBE_STATE_V12\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+context[b"chain_sha"]+b"\nORDINAL="+str(ordinal).encode()+b"\nPROBE="+probe+b"\nSTATE=ACK_COMMIT_INTENT\n"+forensic_body(values)+b"ACTOR_ACK_INTENT_NS="+str(actor_ack).encode()+b"\nB_ACK_RECEIVED_NS="+str(received).encode()+b"\nB_RECORD_ORIGIN_NS="+str(origin).encode()+b"\nB_RECORD_DEADLINE_NS="+str(deadline).encode()+b"\nRECORD_END=1\n")
 state,digest=durable_once(context,b"receipt-"+probe+b"-ack-intent.v5",body,deadline,True,0,(b"ACK_INTENT",probe))
 if state!=DURABLE_VERIFIED:raise FaultSet({b"ACK_DURABILITY_UNKNOWN"})
 context[b"chain_sha"]=digest;return digest

def committed_record(context,ordinal,probe,ack_sha,committed_raw,reserved_control_seq,final_count,ack_deadline):
 need(context[b"chain_sha"]==ack_sha and final_count==sum(context[b"committed"])+1==ordinal+1)
 seq=next_record(context);origin=time.monotonic_ns();deadline=min(ack_deadline,origin+RECORD_NS);need(origin+RECORD_NS<=ack_deadline)
 body=(b"P27E001_PROBE_STATE_V12\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+ack_sha+b"\nORDINAL="+str(ordinal).encode()+b"\nPROBE="+probe+b"\nSTATE=COMMITTED\nACK_SHA256="+ack_sha+b"\nCOMMITTED_PACKET_SHA256="+sha(committed_raw)+b"\nCOMMITTED_PACKET_MESSAGE_SEQ="+str(reserved_control_seq).encode()+b"\nCOMMITTED_COUNT="+str(final_count).encode()+b"\nDIRECT_REAP_COUNT="+str(final_count).encode()+b"\nACK_DEADLINE_NS="+str(ack_deadline).encode()+b"\nB_RECORD_ORIGIN_NS="+str(origin).encode()+b"\nB_RECORD_DEADLINE_NS="+str(deadline).encode()+b"\nRECORD_END=1\n")
 state,digest=durable_once(context,b"receipt-"+probe+b"-committed.v12",body,deadline,True,0,(b"COMMITTED",str(ordinal).encode(),probe,sha(committed_raw),str(final_count).encode(),str(reserved_control_seq).encode()))
 if state!=DURABLE_VERIFIED:raise FaultSet({b"ACK_DURABILITY_UNKNOWN"})
 context[b"chain_sha"]=digest;context[b"last_committed_record_sha"]=digest;context[b"last_committed_packet_sha"]=sha(committed_raw);return digest

def committed_seen_record(context,ordinal,probe,seen_raw,committed_raw,commit_sha,ack_sha,final_count,host_complete,ack_deadline):
 need(time.monotonic_ns()<=ack_deadline and time.monotonic_ns()-host_complete<=ACK_NS)
 seq=next_record(context);predecessor=context[b"chain_sha"];need(predecessor==commit_sha)
 body=(b"P27E001_PROBE_STATE_V12\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+predecessor+b"\nORDINAL="+str(ordinal).encode()+b"\nPROBE="+probe+b"\nSTATE=COMMITTED_SEEN\nACK_SHA256="+ack_sha+b"\nCOMMIT_RECORD_SHA256="+commit_sha+b"\nCOMMITTED_PACKET_SHA256="+sha(committed_raw)+b"\nCOMMITTED_COUNT="+str(final_count).encode()+b"\nACTOR_SEEN_PACKET_SHA256="+sha(seen_raw)+b"\nACTOR_SEEN_MESSAGE_SEQ="+str(CONTROL_RECV_SEQ).encode()+b"\nHOST_COMPLETE_NS="+str(host_complete).encode()+b"\nACK_DEADLINE_NS="+str(ack_deadline).encode()+b"\nRECORD_END=1\n")
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

def recv_monitored(control,actor_pidfd,deadline,rights,actual_pre_state,ordinal,probe):
 receiver_binding(actual_pre_state,ordinal,probe,deadline)
 checkpoint(CERT,0,deadline)
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR);poller.register(actor_pidfd,select.POLLIN|select.POLLHUP|select.POLLERR)
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
   installed=[];bad=False
   try:
    raw,ancillary,flags,address=control.recvmsg(65536,socket.CMSG_SPACE(MAX_RIGHTS*array.array("i").itemsize))
    for level,kind,data in ancillary:
     if level==socket.SOL_SOCKET and kind==socket.SCM_RIGHTS:
      cells=array.array("i");whole=len(data)-(len(data)%cells.itemsize)
      if whole:cells.frombytes(data[:whole]);installed.extend(cells)
      if whole!=len(data):bad=True
     else:bad=True
    checkpoint(CERT,0,deadline)
    if time.monotonic_ns()>deadline:raise FaultSet({b"CONTROL_TIMEOUT"})
    if flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC):raise FaultSet({b"CONTROL_TRUNCATION"})
    if address is not None or not raw:raise FaultSet({b"CONTROL_MALFORMED"})
    if bad:raise FaultSet({b"FD_TRANSFER"})
    if raw.startswith(b"V12_ABORT|"):
     binding=received_binding(raw,actual_pre_state,ordinal,probe,b"control_deadline_ns",deadline)
     values,faults=parse_abort(raw,b"A",binding)
     if installed or ancillary:faults.add(b"FD_TRANSFER")
     error=RemoteAbort(faults);error.values=values;raise error
    if rights==0:
     if installed or ancillary:raise FaultSet({b"FD_TRANSFER"})
    elif len(ancillary)!=1 or len(installed)!=rights:raise FaultSet({b"FD_TRANSFER"})
    return raw,tuple(installed)
   except BlockingIOError:
    close_numbers(installed);continue
   except BaseException:
    close_numbers(installed);raise
  if amask:raise PidfdActorLost("pidfd-ready")
  if cmask&(select.POLLHUP|select.POLLERR):raise ControlLost("control-hup")

def wait_sendable(control,deadline):
 poller=select.poll();poller.register(control.fileno(),select.POLLOUT|select.POLLHUP|select.POLLERR);poller.register(4,select.POLLIN|select.POLLHUP|select.POLLERR)
 while True:
  checkpoint(CERT,0,deadline);remaining=deadline-time.monotonic_ns()
  if remaining<=0:raise FaultSet({b"CONTROL_TIMEOUT"})
  try:events=poller.poll(max(1,min(50,(remaining+999999)//1000000)))
  except InterruptedError:continue
  cmask=amask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   elif number==4:amask|=event
  if amask:raise PidfdActorLost("pidfd-ready")
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

EXTERNAL_MAX_RIGHTS=12
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
 body=(b"P27E001_EXTERNAL_CONTROL_V12|kind="+kind+b"|protocol_version=12|session_id="+AUTH+b"|tx_sequence="+str(EXTERNAL_SEND_SEQ).encode()+b"|sender=B|sender_state="+state+b"|expected_receiver_state="+receiver+b"|effect_state="+effect+b"|absolute_deadline_ns="+str(deadline).encode())
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
 fields=raw[:-1].split(b"|");need(fields[0]==b"P27E001_EXTERNAL_CONTROL_V12" and len(fields)==1+len(common)+len(keys))
 values={}
 for key,item in zip(common+keys,fields[1:]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and parts[1] and key not in values);values[key]=parts[1]
 need(values[b"kind"]==kind and values[b"protocol_version"]==b"12" and values[b"session_id"]==AUTH and values[b"sender"]==b"ISSUER")
 need(values[b"sender_state"]==EXTERNAL_SPEC[kind][0] and values[b"expected_receiver_state"]==EXTERNAL_SPEC[kind][1] and values[b"effect_state"]==EXTERNAL_SPEC[kind][2])
 sequence=udec(values[b"tx_sequence"],1);need(sequence==expected_sequence and sequence==EXTERNAL_RECV_SEQ+1)
 need(udec(values[b"absolute_deadline_ns"],1)==deadline);return values

def commit_external_receive(sequence):
 global EXTERNAL_RECV_SEQ
 need(sequence==EXTERNAL_RECV_SEQ+1);EXTERNAL_RECV_SEQ=sequence

def external_send(control,raw,deadline,rights=()):
 need(len(rights)<=EXTERNAL_MAX_RIGHTS and len(set(rights))==len(rights) and all(type(x)is int and x>=0 for x in rights))
 ancillary=[] if not rights else [(socket.SOL_SOCKET,socket.SCM_RIGHTS,array.array("i",rights))]
 while True:
  checkpoint(CERT,0,deadline);now=time.monotonic_ns();need(now<=deadline)
  poller=select.poll();poller.register(control.fileno(),select.POLLOUT|select.POLLHUP|select.POLLERR);poller.register(15,select.POLLIN|select.POLLHUP|select.POLLERR)
  try:events=poller.poll(max(1,min(50,(deadline-now+999999)//1000000)))
  except InterruptedError:continue
  cmask=omask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   elif number==15:omask|=event
  if omask:raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})
  if cmask&select.POLLOUT:
   try:count=control.sendmsg((raw,),ancillary)
   except BlockingIOError:continue
   except BaseException as error:raise SendEffectUnknown("external-send") from error
   if count!=len(raw):raise SendEffectUnknown("external-short-send")
   checkpoint(CERT,0,deadline);need(time.monotonic_ns()<=deadline);return
  if cmask&(select.POLLHUP|select.POLLERR):raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})

def external_recv(control,kind,keys,expected_sequence,deadline):
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR);poller.register(15,select.POLLIN|select.POLLHUP|select.POLLERR)
 while True:
  checkpoint(CERT,0,deadline);now=time.monotonic_ns();need(now<=deadline)
  try:events=poller.poll(max(1,min(50,(deadline-now+999999)//1000000)))
  except InterruptedError:continue
  cmask=omask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   elif number==15:omask|=event
  if omask:raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})
  if cmask&select.POLLIN:
   installed=[]
   try:
    raw,ancillary,flags,address=control.recvmsg(65536,socket.CMSG_SPACE(EXTERNAL_MAX_RIGHTS*array.array("i").itemsize))
    for level,ctype,data in ancillary:
     if level==socket.SOL_SOCKET and ctype==socket.SCM_RIGHTS:
      cells=array.array("i");whole=len(data)-(len(data)%cells.itemsize)
      if whole:cells.frombytes(data[:whole]);installed.extend(cells)
    need(not installed and not ancillary and not flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC) and address is None)
    return parse_external(raw,kind,keys,expected_sequence,deadline)
   finally:close_numbers(installed)
  if cmask&(select.POLLHUP|select.POLLERR):raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})

EXTERNAL_RECEIPT_KEYS=(b"RECEIPT_KIND",b"OFFER_SHA256",b"RECORD_SEQ",b"PREDECESSOR_SHA256",b"RIGHTS_MANIFEST_SHA256",b"FINALITY_DEADLINE_NS",b"CLOSURE_DEADLINE_NS",b"RECEIVER_PID",b"RECEIVER_STARTTIME",b"NO_REPLAY")

def external_recv_receipt(control,kind,keys,expected_sequence,deadline):
 poller=select.poll();poller.register(control.fileno(),select.POLLIN|select.POLLHUP|select.POLLERR);poller.register(15,select.POLLIN|select.POLLHUP|select.POLLERR)
 while True:
  checkpoint(CERT,0,deadline);now=time.monotonic_ns();need(now<=deadline)
  try:events=poller.poll(max(1,min(50,(deadline-now+999999)//1000000)))
  except InterruptedError:continue
  cmask=omask=0
  for number,event in events:
   if number==control.fileno():cmask|=event
   elif number==15:omask|=event
  if omask:raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})
  if cmask&select.POLLIN:
   installed=[]
   try:
    raw,ancillary,flags,address=control.recvmsg(65536,socket.CMSG_SPACE(array.array("i").itemsize))
    checkpoint(CERT,0,deadline);need(time.monotonic_ns()<=deadline)
    for level,ctype,data in ancillary:
     if level==socket.SOL_SOCKET and ctype==socket.SCM_RIGHTS:
      cells=array.array("i");whole=len(data)-(len(data)%cells.itemsize)
      if whole:cells.frombytes(data[:whole]);installed.extend(cells)
    need(len(installed)==1 and len(ancillary)==1 and not flags&(socket.MSG_TRUNC|socket.MSG_CTRUNC) and address is None)
    receipt_raw=sealed_carrier(installed[0],65536);checkpoint(CERT,0,deadline);need(time.monotonic_ns()<=deadline)
    values=parse_external(raw,kind,keys,expected_sequence,deadline);checkpoint(CERT,0,deadline);need(time.monotonic_ns()<=deadline);return values,receipt_raw
   finally:close_numbers(installed)
  if cmask&(select.POLLHUP|select.POLLERR):raise FaultSet({b"TRANSFER_PROTOCOL_UNKNOWN"})

def verify_external_acceptance(receipt_kind,offer,receipt_raw,values,sequence,predecessor,manifest_sha,finality_deadline,closure_deadline,verify_deadline):
 receipt=parse_fixed(receipt_raw,b"P27E001_EXTERNAL_DURABLE_RECEIPT_V12",EXTERNAL_RECEIPT_KEYS,b"RECEIPT_END=1")
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
 need(kind in (b"ATTEMPT_DIRFD",b"ATTEMPT_BASE_DIRFD",b"STAGE_DIRFD",b"CGROUP_DIRFD",b"OUT_FD",b"ERR_FD",b"EVENTS_FD",b"KILL_FD",b"OUTER_PIDFD",b"CGROUP_BASE_DIRFD",b"ACTOR_CONTROL_FD",b"PENDING_EXPECTED_RAW_FD"))
 access=fcntl.fcntl(number,fcntl.F_GETFL)&os.O_ACCMODE
 if kind==b"PENDING_EXPECTED_RAW_FD":
  pending=context.get(b"record_pending");need(pending is not None and context.get(b"record_sequence_frozen"))
  expected=context[b"durability_raw"][pending[2]];again=sealed_carrier(number,len(expected));delta_raw=semantic_delta_bytes(pending[4]);need(again==expected and sha(again)==pending[3] and access==os.O_RDWR)
  os.lseek(number,0,os.SEEK_SET);return kind+b":"+str(held.st_dev).encode()+b":"+str(held.st_ino).encode()+b":"+format(held.st_mode,"o").encode()+b":"+str(held.st_nlink).encode()+b":"+str(held.st_uid).encode()+b":"+str(held.st_gid).encode()+b":ACCESS="+str(access).encode()+b":SEALED="+str(EXACT_SEALS).encode()+b":BYTES="+str(len(expected)).encode()+b":SHA256="+pending[3]+b":SEMANTIC_DELTA_SHA256="+sha(delta_raw)
 if kind==b"OUTER_PIDFD":
  pid=pidfd_pid(number);start=proc_starttime(pid)
  return kind+b":"+str(pid).encode()+b":"+str(start).encode()+b":PIDFD:ACCESS="+str(access).encode()
 if kind==b"ACTOR_CONTROL_FD":
  flags=fcntl.fcntl(number,fcntl.F_GETFL);need(stat.S_ISSOCK(held.st_mode) and flags&os.O_NONBLOCK)
  return kind+b":"+str(held.st_dev).encode()+b":"+str(held.st_ino).encode()+b":SOCK_SEQPACKET:ACCESS="+str(access).encode()+b":NONBLOCK=1"
 return kind+b":"+str(held.st_dev).encode()+b":"+str(held.st_ino).encode()+b":"+format(held.st_mode,"o").encode()+b":"+str(held.st_nlink).encode()+b":"+str(held.st_uid).encode()+b":"+str(held.st_gid).encode()+b":ACCESS="+str(access).encode()

def external_capabilities(control,context):
 slots=((b"ATTEMPT_DIRFD",b"attempt"),(b"ATTEMPT_BASE_DIRFD",b"attempt_base_fd"),(b"STAGE_DIRFD",b"stage_fd"),(b"CGROUP_DIRFD",b"cgfd"),(b"OUT_FD",b"out_fd"),(b"ERR_FD",b"err_fd"),(b"EVENTS_FD",b"events_fd"),(b"KILL_FD",b"kill_fd"),(b"OUTER_PIDFD",b"outer_pidfd"),(b"CGROUP_BASE_DIRFD",b"cgroup_base_fd"),(b"PENDING_EXPECTED_RAW_FD",b"pending_expected_raw_fd"))
 result=[]
 for kind,key in slots:
  number=context.get(key,-1)
  if number>=0:result.append((kind,key,number,external_identity(kind,number,context)))
 if control is not None:result.append((b"ACTOR_CONTROL_FD",b"actor_control",control.fileno(),external_identity(b"ACTOR_CONTROL_FD",control.fileno(),context)))
 if context.get(b"record_pending") is not None:need(any(item[0]==b"PENDING_EXPECTED_RAW_FD" for item in result))
 need(result and len(result)<=EXTERNAL_MAX_RIGHTS);return tuple(result)

def pending_transfer_manifest(context):
 pending=context.get(b"record_pending")
 if pending is None:return b"NOT_APPLICABLE"
 seq,predecessor,name,digest,semantic_delta=pending;raw=context[b"durability_raw"][name];delta_raw=semantic_delta_bytes(semantic_delta)
 need(context.get(b"record_sequence_frozen") and context.get(b"pending_expected_raw_fd",-1)>=0 and sha(raw)==digest)
 return (b"P27E001_PENDING_RECORD_MANIFEST_V12\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+str(seq).encode()+b"\nPREDECESSOR_SHA256="+predecessor+b"\nENTRY_NAME_HEX="+name.hex().encode()+b"\nEXPECTED_RAW_BYTES="+str(len(raw)).encode()+b"\nEXPECTED_RAW_SHA256="+digest+b"\nSEMANTIC_DELTA_BYTES="+str(len(delta_raw)).encode()+b"\nSEMANTIC_DELTA_SHA256="+sha(delta_raw)+b"\nSEMANTIC_DELTA_HEX="+delta_raw.hex().encode()+b"\nCARRIER_RIGHT=PENDING_EXPECTED_RAW_FD\nCARRIER_CONTRACT=ANONYMOUS_SEALED_O_RDWR_NLINK0\nNO_SUCCESSOR=1\nPENDING_END=1\n")

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
 need(request_kind in (b"V12_REFUSE_PREBEGIN",b"V12_REFUSE_POSTARM") and type(claims)is tuple and len(claims)==9 and all(type(item)is bytes and item for item in claims))
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
 state_payload=(b"P27E001_REFUSAL_SLOT_STATE_V12\nRECORD_SEQ="+str(seq).encode()+b"\nPREDECESSOR_SHA256="+predecessor+b"\nREQUEST_KIND="+request_kind+b"\nREQUEST_SHA256="+request_sha+b"\nREQUEST_MESSAGE_SEQ="+request_sequence+b"\nA_BEGIN_STATE="+a_begin+b"\nA_ARM_STATE="+a_arm+b"\nCROSS_MAP_STATE="+cross_map+b"\nREFUSAL_ORIGIN_NS="+origin_raw+b"\nREFUSAL_FINALITY_DEADLINE_NS="+finality_raw+b"\nREFUSAL_CLOSURE_DEADLINE_NS="+closure_raw+b"\nREFUSAL_CLOSURE_TAIL_NS="+str(REFUSAL_CLOSURE_TAIL_NS).encode()+b"\nREFUSAL_SCHEDULE_HEX="+schedule_claim+b"\nCLOSE_STATE="+close_state+b"\nSLOT_VARIANT="+variant+b"\nACK_SEQUENCE="+str(ack_sequence).encode()+b"\nACK_BYTES="+str(len(ack_raw)).encode()+b"\nACK_SHA256="+(sha(ack_raw) if ack_raw else EMPTY_SHA)+b"\nRECEIPT_SEQUENCE="+str(receipt_sequence).encode()+b"\nRECEIPT_BYTES="+str(len(receipt_raw)).encode()+b"\nRECEIPT_SHA256="+(sha(receipt_raw) if receipt_raw else EMPTY_SHA)+b"\nFINALITY_STATE="+finality_state+b"\nFINALITY_EVIDENCE_BYTES="+str(len(finality_evidence)).encode()+b"\nFINALITY_EVIDENCE_SHA256="+(sha(finality_evidence) if finality_evidence else EMPTY_SHA)+b"\n"+length_frame(b"REQUEST_RAW",request_raw)+length_frame(b"ACK_RAW",ack_raw)+length_frame(b"AUTHORITATIVE_RECEIPT_RAW",receipt_raw)+length_frame(b"FINALITY_EVIDENCE_RAW",finality_evidence)+b"STATE_END=1\n")
 return (b"REFUSAL_SLOT_V12",core,variant,close_state,ack_raw,ack_sequence,receipt_raw,receipt_sequence,finality_state,finality_evidence,offer,sha(offer) if offer else EMPTY_SHA,contract,sha(contract) if contract else EMPTY_SHA,offer_send_sequence,sha(state_payload))

def refusal_slot(context):
 cached=context.get(b"refusal_offer_cache");need(context.get(b"refusal_slot_locked",False) and cached is not None and type(cached)is tuple and len(cached)==16 and cached[0]==b"REFUSAL_SLOT_V12")
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
 digest=sha(b"P27E001_REFUSAL_CANDIDATE_FAULT_V12\x00"+reason+b"\x00"+str(len(raw)).encode()+b"\x00"+raw)
 evidence=context[b"refusal_candidate_fault_evidence"]
 if len(evidence)<REFUSAL_CANDIDATE_EVIDENCE_MAX:context[b"refusal_candidate_fault_evidence"]=evidence+(digest,)
 else:context[b"refusal_candidate_fault_overflow"]+=1
 return digest

def refusal_candidate_fault_digest(context):
 evidence=context[b"refusal_candidate_fault_evidence"];overflow=context[b"refusal_candidate_fault_overflow"]
 raw=b"P27E001_REFUSAL_CANDIDATE_EVIDENCE_V12\nCOUNT="+str(len(evidence)).encode()+b"\nOVERFLOW="+str(overflow).encode()+b"\n"+b"".join(b"EVIDENCE_SHA256="+item+b"\n" for item in evidence)+b"EVIDENCE_END=1\n"
 return sha(raw)

def parse_refusal_receipt_candidate(context,receipt_raw):
 cached=refusal_slot(context);need(cached[2] in (b"ACK_EFFECT_UNKNOWN",b"WAITING_RECEIPT") and cached[4] and cached[6]==b"" and cached[8]==b"OPEN" and cached[10]==b"")
 core=cached[1];ack_raw=cached[4];ack_sequence=cached[5];seq,predecessor,request_raw,request_kind,claims,schedule_items,finality_deadline,closure_deadline=core
 request_sha,request_sequence,a_begin,a_arm,cross_map,origin_raw,finality_raw,closure_raw,schedule_claim=claims;schedule={name:value for name,value in schedule_items};receipt_deadline=finality_deadline
 checkpoint(CERT,0,finality_deadline);need(time.monotonic_ns()<=finality_deadline)
 need(type(receipt_raw)is bytes and receipt_raw.endswith(b"\n") and receipt_raw.count(b"\n")==1 and all(x==10 or 32<=x<=126 for x in receipt_raw))
 common_keys=(b"protocol_version",b"session_id",b"message_seq",b"message_sender",b"transition_id",b"sender_state",b"expected_receiver_state",b"slot_ordinal",b"slot_probe",b"effect_state",b"deadline_name",b"absolute_deadline_ns")
 physical=tuple(key for key in REFUSAL_RECEIPT_KEYS if key not in CONTROL_RESERVED)
 fields=receipt_raw[:-1].split(b"|");need(fields[0]==b"V12_REFUSE_ACK_RECEIPT" and len(fields)==1+len(common_keys)+len(physical))
 common={};result={}
 for key,item in zip(common_keys,fields[1:1+len(common_keys)]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and parts[1] and key not in common);common[key]=parts[1]
 for key,item in zip(physical,fields[1+len(common_keys):]):
  parts=item.split(b"=",1);need(len(parts)==2 and parts[0]==key and parts[1] and key not in result and key not in common);result[key]=parts[1]
 spec_state,spec_receiver,spec_effect,deadline_key=CONTROL_SPEC[b"V12_REFUSE_ACK_RECEIPT"]
 need(common[b"protocol_version"]==b"12" and common[b"session_id"]==AUTH and common[b"message_sender"]==b"A")
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
 evidence=(b"P27E001_REFUSAL_RECEIPT_FINALITY_V12\nRECEIPT_SEQUENCE="+str(sequence).encode()+b"\nRECEIPT_BYTES="+str(len(receipt_raw)).encode()+b"\nRECEIPT_SHA256="+sha(receipt_raw)+b"\nCANDIDATE_FAULT_EVIDENCE_SHA256="+refusal_candidate_fault_digest(context)+b"\nFINALITY_DEADLINE_NS="+str(finality_deadline).encode()+b"\nCLOSURE_DEADLINE_NS="+str(cached[1][7]).encode()+b"\nFINALITY_END=1\n")
 updated=refusal_slot_update(context,b"RECEIPT_VERIFIED",receipt_raw=receipt_raw,receipt_sequence=sequence,finality_state=b"RECEIPT_VERIFIED_FINAL",finality_evidence=evidence);evidence_sha=sha(evidence)
 need(updated[6]==receipt_raw and updated[7]==sequence and updated[8]==b"RECEIPT_VERIFIED_FINAL" and updated[10]==b"" and sequence==CONTROL_RECV_SEQ+1)
 need(refusal_slot(context)==cached and sequence==CONTROL_RECV_SEQ+1);checkpoint(CERT,0,finality_deadline);need(time.monotonic_ns()<=finality_deadline)
 CONTROL_RECV_SEQ,context[b"refusal_offer_cache"],context[b"refusal_finality_state"],context[b"refusal_finality_evidence_sha"]=(sequence,updated,b"RECEIPT_VERIFIED_FINAL",evidence_sha)
 return updated

def receive_refusal_candidate_once(control,context):
 installed=[];raw=b"";finality_deadline=refusal_slot(context)[1][6]
 try:
  try:
   raw,ancillary,flags,address=control.recvmsg(65536,socket.CMSG_SPACE(MAX_RIGHTS*array.array("i").itemsize));bad=False
   for level,kind,data in ancillary:
    if level==socket.SOL_SOCKET and kind==socket.SCM_RIGHTS:
     cells=array.array("i");whole=len(data)-(len(data)%cells.itemsize)
     if whole:cells.frombytes(data[:whole]);installed.extend(cells)
     if whole!=len(data):bad=True
    else:bad=True
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
 finally:close_numbers(installed)

def finalize_refusal_actor_loss(context):
 cached=refusal_slot(context);finality_deadline=cached[1][6]
 need(cached[8]==b"OPEN" and cached[10]==b"" and context[b"refusal_actor_loss_seen"] and context[b"refusal_control_eof"] and pidfd_pid(4)==ACTOR_PID)
 evidence=(b"P27E001_REFUSAL_ACTOR_LOSS_FINALITY_V12\nACTOR_PID="+str(ACTOR_PID).encode()+b"\nACTOR_STARTTIME="+str(ACTOR_STARTTIME).encode()+b"\nPIDFD_READY=1\nACTOR_CONTROL_EOF=1\nCONTROL_RECV_SEQ_AT_EOF="+str(CONTROL_RECV_SEQ).encode()+b"\nCANDIDATE_FAULT_EVIDENCE_SHA256="+refusal_candidate_fault_digest(context)+b"\nFINALITY_DEADLINE_NS="+str(finality_deadline).encode()+b"\nCLOSURE_DEADLINE_NS="+str(cached[1][7]).encode()+b"\nFINALITY_END=1\n")
 updated=refusal_slot_update(context,b"ACTOR_LOSS_DRAINED",finality_state=b"ACTOR_LOSS_CONTROL_EOF_FINAL",finality_evidence=evidence);evidence_sha=sha(evidence)
 need(refusal_slot(context)==cached);checkpoint(CERT,0,finality_deadline);need(time.monotonic_ns()<=finality_deadline)
 context[b"refusal_offer_cache"],context[b"refusal_finality_state"],context[b"refusal_finality_evidence_sha"],context[b"refusal_offer_state"]=(updated,b"ACTOR_LOSS_CONTROL_EOF_FINAL",evidence_sha,b"ACTOR_LOSS_CONTROL_EOF_FINAL_NO_OFFER")
 return updated

def finalize_refusal_cap_hold(context):
 cached=refusal_slot(context)
 if cached[8]!=b"OPEN":return cached
 need(cached[10]==b"");finality_deadline=cached[1][6]
 evidence=(b"P27E001_REFUSAL_FINALITY_CAP_HOLD_V12\nFINALITY_DEADLINE_NS="+str(finality_deadline).encode()+b"\nCLOSURE_DEADLINE_NS="+str(cached[1][7]).encode()+b"\nCONTROL_RECV_SEQ="+str(CONTROL_RECV_SEQ).encode()+b"\nACTOR_LOSS_SEEN="+(b"1" if context[b"refusal_actor_loss_seen"] else b"0")+b"\nACTOR_CONTROL_EOF="+(b"1" if context[b"refusal_control_eof"] else b"0")+b"\nCANDIDATE_FAULT_EVIDENCE_SHA256="+refusal_candidate_fault_digest(context)+b"\nOFFER_ALLOWED=0\nFINALITY_END=1\n")
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
   try:poller.register(4,select.POLLIN|select.POLLHUP|select.POLLERR);actor_registered=True
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
  if amask:
   try:need(pidfd_pid(4)==ACTOR_PID)
   except BaseException:context[b"faults"].add(b"RECONCILIATION_UNKNOWN")
   else:context[b"refusal_actor_loss_seen"]=True;mark_actor_pidfd_lost(context)
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
 return (b"P27E001_REFUSAL_RECEIPT_CONTRACT_V12\nAUTH_ID="+AUTH+b"\nRECEIPT_KIND=REFUSAL_CLOSE\nRECORD_SEQ="+str(seq).encode()+b"\nPREDECESSOR_SHA256="+predecessor+b"\nREQUEST_KIND="+request_kind+b"\nREQUEST_BYTES="+str(len(request_raw)).encode()+b"\nREQUEST_SHA256="+sha(request_raw)+b"\nCLOSE_STATE="+close_state+b"\nSLOT_VARIANT="+variant+b"\nFINAL_SLOT_SHA256="+state_digest+b"\nACK_SEQUENCE="+str(ack_sequence).encode()+b"\nACK_BYTES="+str(len(ack_raw)).encode()+b"\nACK_SHA256="+sha(ack_raw)+b"\nACTOR_RECEIPT_SEQUENCE="+str(receipt_sequence).encode()+b"\nACTOR_RECEIPT_BYTES="+str(len(receipt_raw)).encode()+b"\nACTOR_RECEIPT_SHA256="+(sha(receipt_raw) if receipt_raw else EMPTY_SHA)+b"\nFINALITY_STATE="+finality_state+b"\nFINALITY_EVIDENCE_BYTES="+str(len(finality_evidence)).encode()+b"\nFINALITY_EVIDENCE_SHA256="+sha(finality_evidence)+b"\nREFUSAL_FINALITY_DEADLINE_NS="+str(finality_deadline).encode()+b"\nREFUSAL_CLOSURE_DEADLINE_NS="+str(closure_deadline).encode()+b"\nREFUSAL_CLOSURE_TAIL_NS="+str(REFUSAL_CLOSURE_TAIL_NS).encode()+b"\nREFUSAL_SCHEDULE_HEX="+schedule_hex(schedule,REFUSAL_PHASE_SPEC)+b"\nRIGHTS_MANIFEST_SHA256="+EMPTY_SHA+b"\nISSUER_KEY_ID="+ISSUER_KEY_ID+b"\nOWNER_PID="+CERT[b"EXTERNAL_OWNER_PID"]+b"\nOWNER_STARTTIME="+CERT[b"EXTERNAL_OWNER_STARTTIME"]+b"\nEFFECT=DEDICATED_REFUSAL_RECONCILIATION\nABSOLUTE_FINALITY_DEADLINE_NS="+str(finality_deadline).encode()+b"\nABSOLUTE_CLOSURE_DEADLINE_NS="+str(closure_deadline).encode()+b"\nNO_SUCCESSOR=1\nNO_REPLAY=1\nCONTRACT_END=1\n")

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
    activate_reserved_external_packet(offer,offer_send_sequence);external_send(context[b"transfer_control"],offer,send_deadline)
    context[b"refusal_offer_state"]=b"SENT_ONCE_WAITING_ACCEPTANCE";context[b"external_send_state"]=b"REFUSAL_OFFER_SENT"
   except BaseException:
    context[b"refusal_offer_state"]=b"EFFECT_UNKNOWN_NO_RESEND_WAITING_ACCEPTANCE";context[b"external_send_state"]=b"REFUSAL_OFFER_EFFECT_UNKNOWN"
  recv_deadline,recv_latest_start,recv_reserve_after=refusal_stage_window(context,b"REFUSAL_ACCEPTANCE_RECV")
  keys=(b"offer_sha256",b"record_seq",b"predecessor_sha256",b"refusal_finality_deadline_ns",b"refusal_closure_deadline_ns",b"refusal_schedule_hex",b"durable_receipt_bytes",b"durable_receipt_sha256",b"acceptance_preimage_sha256",b"issuer_key_id",b"issuer_public_key_hex",b"issuer_signature_hex",b"owner_pid",b"owner_starttime",b"no_replay")
  values,issuer_receipt_raw=external_recv_receipt(context[b"transfer_control"],b"REFUSAL_CLOSE_ACCEPTED",keys,seq,recv_deadline)
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
   closed=packet(b"V12_REFUSAL_CLOSED",((b"state",b"REFUSAL_DURABLY_CLOSED"),(b"expected_state",b"WAIT_REFUSAL_CLOSED"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"ack_packet_sha256",sha(cached[4])),(b"receipt_packet_sha256",sha(cached[6])),(b"cross_map_state",cross_map),(b"issuer_closure_sha256",context[b"refusal_closure_sha"]),(b"issuer_record_seq",str(core[0]).encode()),(b"issuer_predecessor_sha256",core[1]),(b"no_replay",b"1"),(b"refusal_finality_deadline_ns",str(finality_deadline).encode()),(b"refusal_closure_deadline_ns",str(closure_deadline).encode()),(b"refusal_schedule_hex",schedule_claim),(b"consume_deadline_ns",str(actor_close_deadline).encode())))
   checkpoint(CERT,0,actor_close_deadline);need(time.monotonic_ns()<=actor_close_deadline)
   context[b"send_state"]=b"REFUSAL_CLOSURE_SEND_EFFECT_UNKNOWN"
   try:send_exact(control,closed,actor_close_deadline);context[b"send_state"]=b"REFUSAL_CLOSURE_SENT";context[b"refusal_actor_closure_state"]=b"SENT"
   except BaseException:context[b"send_state"]=b"REFUSAL_CLOSURE_SEND_EFFECT_UNKNOWN";context[b"refusal_actor_closure_state"]=b"EFFECT_UNKNOWN_AFTER_DURABLE_ACCEPTANCE"
  else:context[b"refusal_actor_closure_state"]=b"ACTOR_LOSS_OR_CONTROL_UNAVAILABLE_AFTER_DURABLE_ACCEPTANCE"
  context[b"refusal_actor_closure_complete"]=True
 if not context[b"refusal_capabilities_closed"]:
  try:cap_deadline,cap_latest_start,cap_reserve_after=refusal_stage_window(context,b"REFUSAL_CAPABILITY_CLOSE")
  except BaseException:refusal_closure_hold(context,b"CAPABILITY_CLOSE_LATEST_SAFE_START_MISSED")
  numbers=[]
  for key in (b"attempt",b"attempt_base_fd",b"cgroup_base_fd",b"pending_expected_raw_fd"):
   number=context.get(key,-1)
   if number>=0:numbers.append((key,number))
  for key,number in numbers:
   checkpoint(CERT,0,cap_deadline);need(time.monotonic_ns()<=cap_deadline);os.close(number);context[key]=-1
  for key in (b"actor_control",b"transfer_control"):
   endpoint=context.get(key)
   if endpoint is not None:
    checkpoint(CERT,0,cap_deadline);need(time.monotonic_ns()<=cap_deadline);endpoint.close();context[key]=None
  checkpoint(CERT,0,cap_deadline);need(time.monotonic_ns()<=cap_deadline);context[b"refusal_capabilities_closed"]=True
 try:release_deadline,release_latest_start,release_reserve_after=refusal_stage_window(context,b"REFUSAL_CLOSURE")
 except BaseException:refusal_closure_hold(context,b"OWNER_RELEASE_LATEST_SAFE_START_MISSED")
 need(context[b"refusal_capabilities_closed"] and context[b"refusal_actor_closure_complete"] and context[b"refusal_acceptance_state"]==b"COMMITTED" and refusal_slot(context)[10]==cached[10])
 checkpoint(CERT,0,release_deadline);need(time.monotonic_ns()<=release_deadline and not context[b"owner_released"])
 context[b"owner_released"]=True;context[b"refusal_offer_state"]=b"OWNER_RELEASED_AFTER_DURABLE_ACCEPTANCE_AND_CAPABILITY_CLOSE";return context[b"refusal_closure_sha"]

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
 offer,caps,manifest,seq,predecessor,schedule_items,finality_deadline,closure_deadline,reason,reserved_sequence,state_digest=cache
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
 if reason==b"STAGE_NOT_STARTED":context[b"transfer_acceptance_state"]=b"TRANSFER_STAGE_NOT_STARTED_HOLD"
 elif reason==b"ACCEPTANCE_EFFECT_UNKNOWN":context[b"transfer_acceptance_state"]=b"TRANSFER_ACCEPTANCE_EFFECT_UNKNOWN_HOLD"
 else:context[b"transfer_acceptance_state"]=b"TRANSFER_CLOSURE_CAP_HOLD"
 context[b"transfer_state"]=context[b"transfer_acceptance_state"]+b"_NO_RESEND_NO_OWNER_RELEASE";raise RefusalFinalityPending("generic-transfer-held")

def complete_generic_transfer_closure(context):
 cache=context[b"transfer_offer_cache"];offer,caps,manifest,seq,predecessor,schedule_items,finality_deadline,closure_deadline,reason,reserved_sequence,state_digest=cache
 need(context[b"transfer_acceptance_state"]==b"COMMITTED" and context[b"transfer_receipt_sha"]!=b"0"*64)
 if not context[b"transfer_capabilities_closed"]:
  try:cap_deadline,cap_latest_start,cap_reserve_after=transfer_stage_window(context,b"TRANSFER_CAPABILITY_CLOSE")
  except BaseException:generic_transfer_hold(context,b"CLOSURE_CAP_EXPIRED")
  try:
   for kind,key,number,identity in caps:
    if key==b"actor_control":
     endpoint=context.get(b"actor_control");need(endpoint is not None and endpoint.fileno()==number);checkpoint(CERT,0,cap_deadline);need(time.monotonic_ns()<=cap_deadline);endpoint.close();context[b"actor_control"]=None
    else:
     need(context.get(key,-1)==number);checkpoint(CERT,0,cap_deadline);need(time.monotonic_ns()<=cap_deadline);os.close(number);context[key]=-1
   endpoint=context.get(b"transfer_control")
   if endpoint is not None:
    checkpoint(CERT,0,cap_deadline);need(time.monotonic_ns()<=cap_deadline);endpoint.close();context[b"transfer_control"]=None
   checkpoint(CERT,0,cap_deadline);need(time.monotonic_ns()<=cap_deadline);context[b"transfer_capabilities_closed"]=True
  except BaseException:generic_transfer_hold(context,b"CLOSURE_CAP_EXPIRED")
 try:release_deadline,release_latest_start,release_reserve_after=transfer_stage_window(context,b"TRANSFER_CLOSURE")
 except BaseException:generic_transfer_hold(context,b"CLOSURE_CAP_EXPIRED")
 checkpoint(CERT,0,release_deadline);need(time.monotonic_ns()<=release_deadline and context[b"transfer_capabilities_closed"] and not context[b"owner_released"])
 context[b"owner_released"]=True;context[b"transfer_state"]=b"TRANSFER_ACCEPTED_CAPABILITIES_CLOSED_OWNER_RELEASED";return context[b"transfer_receipt_sha"]

def external_transfer(control,context,reason):
 need((context[b"consumed"] or context.get(b"refusal_closed",False) or context.get(b"refusal_slot_locked",False)) and not context[b"owner_released"] and reason in FAULT_ORDER)
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
 if context[b"transfer_acceptance_state"] in (b"TRANSFER_STAGE_NOT_STARTED_HOLD",b"TRANSFER_ACCEPTANCE_EFFECT_UNKNOWN_HOLD",b"TRANSFER_CLOSURE_CAP_HOLD"):raise RefusalFinalityPending("generic-transfer-held")
 if context[b"transfer_acceptance_state"]==b"COMMITTED":return complete_generic_transfer_closure(context)
 if context.get(b"transfer_offer_cache") is None:
  origin=time.monotonic_ns();closure_deadline=origin+TRANSFER_TOTAL_NS;need(closure_deadline<=certificate_mono_expiry(CERT))
  schedule=exact_schedule(origin,closure_deadline,TRANSFER_PHASE_SPEC);finality_deadline=schedule[b"TRANSFER_ACCEPTANCE_COMMIT"]
  caps=external_capabilities(control,context);manifest=b";".join(item[3] for item in caps);pending_manifest=pending_transfer_manifest(context)
  seq=context[b"external_record_seq"]+1;predecessor=context[b"external_chain_sha"];schedule_items=tuple((name,schedule[name]) for name,cap in TRANSFER_PHASE_SPEC)
  state_payload=(b"P27E001_GENERIC_TRANSFER_STATE_V12\nRECORD_SEQ="+str(seq).encode()+b"\nPREDECESSOR_SHA256="+predecessor+b"\nREASON="+reason+b"\nRIGHTS_MANIFEST_SHA256="+sha(manifest)+b"\nFINALITY_DEADLINE_NS="+str(finality_deadline).encode()+b"\nCLOSURE_DEADLINE_NS="+str(closure_deadline).encode()+b"\nTRANSFER_SCHEDULE_HEX="+schedule_hex(schedule,TRANSFER_PHASE_SPEC)+b"\nSTATE_END=1\n");state_digest=sha(state_payload)
  body=((b"record_seq",str(seq).encode()),(b"predecessor_sha256",predecessor),(b"reason",reason),(b"rights_count",str(len(caps)).encode()),(b"rights_manifest_hex",manifest.hex().encode()),(b"rights_manifest_sha256",sha(manifest)),(b"pending_record_manifest_hex",pending_manifest.hex().encode()),(b"pending_record_manifest_sha256",sha(pending_manifest)),(b"pending_expected_raw_carrier",b"PENDING_EXPECTED_RAW_FD" if context.get(b"record_pending") is not None else b"NOT_APPLICABLE"),(b"actor_pid",str(ACTOR_PID).encode()),(b"actor_starttime",str(ACTOR_STARTTIME).encode()),(b"owner_pid",CERT[b"EXTERNAL_OWNER_PID"]),(b"owner_starttime",CERT[b"EXTERNAL_OWNER_STARTTIME"]),(b"terminal_phase",context.get(b"terminal_phase",b"NOT_STARTED")),(b"terminal_subject_sha256",context.get(b"terminal_subject",context.get(b"collision_transfer_claim_sha",b"0"*64))),(b"chain_head_sha256",context[b"chain_sha"]),(b"outcome_durable",b"1" if context[b"outcome_durable"] else b"0"),(b"control_state",context[b"control_state"]),(b"actor_state",context[b"actor_state"]),(b"send_state",context[b"send_state"]),(b"attempt_state",context[b"attempt_state"]),(b"collision_closed",b"1" if context[b"collision"] else b"0"),(b"attempt_base_closed",b"1" if context.get(b"attempt_base_fd",-1)<0 else b"0"),(b"commit_count",str(context[b"commit_count"]).encode()),(b"intent_count",str(context[b"intent_count"]).encode()),(b"last_committed_record_sha256",context.get(b"last_committed_record_sha",b"0"*64)),(b"last_committed_packet_sha256",context.get(b"last_committed_packet_sha",b"0"*64)),(b"committed_send_state",context.get(b"committed_send_state",b"NOT_STARTED")),(b"transfer_finality_deadline_ns",str(finality_deadline).encode()),(b"transfer_closure_deadline_ns",str(closure_deadline).encode()),(b"transfer_schedule_hex",schedule_hex(schedule,TRANSFER_PHASE_SPEC)),(b"frozen_state_sha256",state_digest),(b"no_replay",b"1"))
  offer,reserved_sequence=reserve_external_packet(b"TRANSFER_OFFER",b"FROZEN_EXTERNAL_TRANSFER",b"ISSUER_WAIT_TRANSFER",b"SCM_RIGHTS_TRANSFER",schedule[b"TRANSFER_OFFER_SEND"],body);need(reserved_sequence==seq)
  candidate=(offer,caps,manifest,seq,predecessor,schedule_items,finality_deadline,closure_deadline,reason,reserved_sequence,state_digest)
  need(context[b"transfer_offer_cache"] is None);checkpoint(CERT,0,schedule[b"TRANSFER_OFFER_BUILD"]);need(time.monotonic_ns()<=schedule[b"TRANSFER_OFFER_BUILD"])
  context[b"transfer_offer_cache"]=candidate;context[b"frozen_transfer_reason"]=reason;context[b"offer_delivery_possible"]=False;context[b"transfer_state"]=b"OFFER_FROZEN_NOT_SENT"
 else:
  offer,caps,manifest,seq,predecessor,schedule_items,finality_deadline,closure_deadline,frozen_reason,reserved_sequence,state_digest=context[b"transfer_offer_cache"];need(reason==frozen_reason==context[b"frozen_transfer_reason"])
 cache=context[b"transfer_offer_cache"];offer,caps,manifest,seq,predecessor,schedule_items,finality_deadline,closure_deadline,frozen_reason,reserved_sequence,state_digest=cache;schedule=transfer_schedule_from_cache(cache)
 try:
  send_deadline,send_latest_start,send_reserve_after=transfer_stage_window(context,b"TRANSFER_OFFER_SEND")
  if not context[b"offer_delivery_possible"]:
   context[b"offer_delivery_possible"]=True;context[b"transfer_state"]=b"OFFER_DELIVERY_POSSIBLE_NO_RESEND"
   try:activate_reserved_external_packet(offer,reserved_sequence);external_send(context[b"transfer_control"],offer,send_deadline,tuple(item[2] for item in caps));context[b"transfer_state"]=b"OFFER_SENT_ONCE_WAITING_RECEIPT"
   except BaseException:context[b"transfer_state"]=b"OFFER_EFFECT_UNKNOWN_NO_RESEND_WAITING_RECEIPT"
  recv_deadline,recv_latest_start,recv_reserve_after=transfer_stage_window(context,b"TRANSFER_ACCEPTANCE_RECV")
  keys=(b"offer_sha256",b"record_seq",b"predecessor_sha256",b"held_manifest_sha256",b"transfer_finality_deadline_ns",b"transfer_closure_deadline_ns",b"transfer_schedule_hex",b"durable_receipt_bytes",b"durable_receipt_sha256",b"acceptance_preimage_sha256",b"issuer_key_id",b"issuer_public_key_hex",b"issuer_signature_hex",b"receiver_pid",b"receiver_starttime",b"no_replay")
  values,receipt_raw=external_recv_receipt(context[b"transfer_control"],b"TRANSFER_ACCEPTED",keys,seq,recv_deadline)
  need(values[b"offer_sha256"]==sha(offer) and udec(values[b"record_seq"],1)==seq and values[b"predecessor_sha256"]==predecessor and values[b"held_manifest_sha256"]==sha(manifest))
  need(udec(values[b"transfer_finality_deadline_ns"])==finality_deadline and udec(values[b"transfer_closure_deadline_ns"])==closure_deadline and values[b"transfer_schedule_hex"]==schedule_hex(schedule,TRANSFER_PHASE_SPEC))
  verify_deadline,verify_latest_start,verify_reserve_after=transfer_stage_window(context,b"TRANSFER_ACCEPTANCE_VERIFY")
  digest=verify_external_acceptance(b"TRANSFER_ACCEPTED",offer,receipt_raw,values,seq,predecessor,sha(manifest),finality_deadline,closure_deadline,verify_deadline)
  need(values[b"receiver_pid"]==CERT[b"EXTERNAL_OWNER_PID"] and values[b"receiver_starttime"]==CERT[b"EXTERNAL_OWNER_STARTTIME"] and values[b"no_replay"]==b"1")
  owner_pid=udec(CERT[b"EXTERNAL_OWNER_PID"],2);need(pidfd_pid(15)==owner_pid and proc_starttime(owner_pid)==udec(CERT[b"EXTERNAL_OWNER_STARTTIME"],1))
  checkpoint(CERT,0,verify_deadline);need(time.monotonic_ns()<=verify_deadline)
  commit_deadline,commit_latest_start,commit_reserve_after=transfer_stage_window(context,b"TRANSFER_ACCEPTANCE_COMMIT")
  need(context[b"transfer_offer_cache"]==cache and EXTERNAL_RECV_SEQ+1==seq);checkpoint(CERT,0,commit_deadline);need(time.monotonic_ns()<=commit_deadline)
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

def kill_once(context,reason):
 if context[b"kill_call_attempted"]:return
 need(context[b"kill_authority_consumed"]);context[b"kill_call_attempted"]=True;context[b"kill_state"]=b"TICKET_COMMITTING"
 freeze_failure_deadlines(context);ticket_deadline=context[b"failure_origin"]+KILL_TICKET_NS;cleanup_deadline=context[b"cleanup_effect_deadline"]
 if time.monotonic_ns()>ticket_deadline:
  context[b"kill_state"]=b"DEADLINE_PRECLUDED";context[b"faults"].add(b"KILL_TICKET_DURABILITY_UNKNOWN");return
 seq=next_record(context);predecessor=context[b"chain_sha"]
 ticket=(b"P27E001_KILL_TICKET_V12\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+predecessor+b"\nPRIMARY="+reason+b"\nFAILURE_ORIGIN_NS="+str(context[b"failure_origin"]).encode()+b"\nCLEANUP_EFFECT_DEADLINE_NS="+str(cleanup_deadline).encode()+b"\nTICKET_DEADLINE_NS="+str(ticket_deadline).encode()+b"\nKILL_CALL_COUNT_BEFORE=0\nWRITE_BYTES_HEX=310a\nRETRY_ALLOWED=0\nTICKET_END=1\n")
 state,digest=durable_once(context,b"kill-ticket.v5",ticket,ticket_deadline,False,cleanup_deadline-ticket_deadline,(b"KILL_TICKET",))
 context[b"kill_ticket_state"]=state
 if state!=DURABLE_VERIFIED:
  context[b"kill_state"]=b"TICKET_DURABILITY_UNKNOWN";context[b"faults"].add(b"KILL_TICKET_DURABILITY_UNKNOWN");return
 context[b"chain_sha"]=digest;context[b"kill_state"]=b"CALL_RESERVED";number=context.get(b"kill_fd",-1)
 if number<0:number=context.get(b"root_kill_fd",-1)
 if number<0:
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
 body=(b"P27E001_RETAINED_STATE_V12\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+predecessor+b"\nSTOP_PROBE="+stop+b"\nPRIMARY="+primary(context[b"faults"])+b"\nFAULT_SET="+fault_csv(context[b"faults"])+b"\nFAILURE_ORIGIN_NS="+str(context[b"failure_origin"]).encode()+b"\nCLEANUP_EFFECT_DEADLINE_NS="+str(deadline).encode()+b"\nKILL_CALL_COUNT="+str(context[b"kill_call_count"]).encode()+b"\nKILL_STATE="+context[b"kill_state"]+b"\nRETRY_ALLOWED=0\nRETAINED_END=1\n")
 state,digest=durable_once(context,b"retained.v5",body,deadline,False,FAILURE_TAIL_NS,(b"RETAINED",));context[b"retained_state"]=state
 if state==DURABLE_VERIFIED:context[b"chain_sha"]=digest
 else:context[b"faults"].add(b"RETAINED_DURABILITY_UNKNOWN")

def mark_actor_pidfd_lost(context):
 context[b"actor_state"]=b"PIDFD_ACTOR_LOST";context[b"actor_lost"]=True;context[b"release_disabled"]=True;context[b"faults"].add(b"PIDFD_ACTOR_LOST")

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
  try:poller.register(4,select.POLLIN|select.POLLHUP|select.POLLERR);actor_registered=True
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
  if amask:
   try:need(pidfd_pid(4)==ACTOR_PID)
   except BaseException:context[b"faults"].add(b"RECONCILIATION_UNKNOWN")
   else:context[b"refusal_actor_loss_seen"]=True;mark_actor_pidfd_lost(context)
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
  try:need(pidfd_pid(4)==ACTOR_PID)
  except BaseException:context[b"faults"].add(b"RECONCILIATION_UNKNOWN")
  else:mark_actor_pidfd_lost(context)
 if cmask&select.POLLIN:
  if not locked:
   try:
    raw,fds=recv_monitored(control,4,min(until,time.monotonic_ns()+ACK_NS),0,b"OWNER_POLL",b"NONE",b"NONE");need(fds==())
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
 body=(b"P27E001_RECOVERY_STATE_V12\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+predecessor+b"\nSTOP_PROBE="+stop+b"\nPRIMARY="+primary(context[b"faults"])+b"\nFAULT_SET="+fault_csv(context[b"faults"])+b"\nINTENT_DURABLE="+(b"1" if context[b"intent_durable"] else b"0")+b"\nCONSUMPTION_STATE="+context[b"consumption_state"]+b"\nSTAGE_STATE="+context[b"stage_state"]+b"\nCONTAINMENT_STATE="+(b"BOUND" if context[b"containment_bound"] else b"NOT_APPLICABLE")+b"\nEMPTY_STATE="+(b"EMPTY" if population is False else b"NOT_APPLICABLE")+b"\nSTOPPED_COUNT="+str(context[b"stopped_count"]).encode()+b"\nDIRECT_REAP="+direct+b"\nSTDOUT_EOF="+(b"1" if context[b"last_out_eof"] else b"0")+b"\nSTDERR_EOF="+(b"1" if context[b"last_err_eof"] else b"0")+b"\nKILL_CALL_COUNT="+str(context[b"kill_call_count"]).encode()+b"\nKILL_STATE="+context[b"kill_state"]+b"\nKILL_TICKET_STATE="+context[b"kill_ticket_state"]+b"\nFAILURE_ORIGIN_NS="+str(context[b"failure_origin"]).encode()+b"\nCLEANUP_EFFECT_DEADLINE_NS="+str(context[b"cleanup_effect_deadline"]).encode()+b"\nRECOVERY_DEADLINE_NS="+str(deadline).encode()+b"\nTERMINAL_DEADLINE_NS="+str(context[b"terminal_deadline"]).encode()+b"\nRETRY_ALLOWED=0\nDISPOSITION="+disposition(context[b"faults"])+b"\nRECOVERY_END=1\n")
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
 values=parse_fixed(raw,b"P27E001_FINAL_REPORT_V12",FINAL_REPORT_KEYS,b"RECORD_END=1")
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
 body=b"P27E001_FINAL_REPORT_V12\nAUTH_ID="+AUTH+b"\nRECORD_SEQ="+seq+b"\nPREDECESSOR_SHA256="+predecessor+b"\n"+b"".join(key+b"="+value+b"\n" for key,value in lines)+b"PHASE_DEADLINE_NS="+str(deadline).encode()+b"\nRECORD_END=1\n"
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
 body,digest=chained_record(context,b"terminal-candidate.v5" if mode==b"SUCCESS" else b"failure-candidate.v5",b"P27E001_TERMINAL_CANDIDATE_V12",lines,deadline,mode==b"SUCCESS",context[b"terminal_deadline"]-deadline,(b"TERMINAL_CANDIDATE",))
 context[b"candidate_sha"]=digest;return digest

def terminal_seen_record(context,mode,candidate_sha,notice_raw,seen_raw,schedule):
 deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"TERMINAL_SEEN_RECORD",context[b"terminal_deadline"],mode==b"SUCCESS")
 lines=((b"OUTCOME_KIND",b"SUCCESS" if mode==b"SUCCESS" else b"FAILURE"),(b"CANDIDATE_SHA256",candidate_sha),(b"NOTICE_PACKET_SHA256",sha(notice_raw)),(b"ACTOR_SEEN_PACKET_SHA256",sha(seen_raw)),(b"ACTOR_SEEN_MESSAGE_SEQ",str(CONTROL_RECV_SEQ).encode()),(b"TERMINAL_SCHEDULE_HEX",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"NO_REPLAY",b"1"))
 body,digest=chained_record(context,b"terminal-seen.v5",b"P27E001_TERMINAL_SEEN_V12",lines,deadline,mode==b"SUCCESS",context[b"terminal_deadline"]-deadline,(b"TERMINAL_SEEN",))
 context[b"terminal_seen_sha"]=digest;return digest

def success_report_and_pass(context,schedule):
 report_deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"REPORT_RECORD",context[b"terminal_deadline"],True)
 body,report_sha=durable_prevalidated_report(context,b"NONE",b"SUCCESS",schedule,report_deadline,True,context[b"terminal_deadline"]-report_deadline,b"SUCCESS_REPORT")
 context[b"report_state"]=DURABLE_VERIFIED;context[b"report_sha"]=report_sha
 pass_deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"PASS_COMMIT",context[b"terminal_deadline"],True)
 token=sha(b"P27E001V12_RECONCILE\x00"+AUTH+b"\x00"+report_sha+b"\x00"+context[b"terminal_seen_sha"]+b"\x00"+schedule_hex(schedule,TERMINAL_PHASE_SPEC))
 context[b"pass_effect_possible"]=True
 lines=((b"OUTCOME_KIND",b"PASS"),(b"REPORT_SHA256",report_sha),(b"TERMINAL_SEEN_SHA256",context[b"terminal_seen_sha"]),(b"RECONCILIATION_TOKEN",token),(b"PASS",b"1"),(b"PASS_DEADLINE_NS",str(pass_deadline).encode()),(b"TERMINAL_SCHEDULE_HEX",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"RETRY_ALLOWED",b"0"))
 body,pass_sha=chained_record(context,b"pass-commit.v5",b"P27E001_PASS_COMMIT_V12",lines,pass_deadline,True,context[b"terminal_deadline"]-pass_deadline,(b"PASS_COMMIT",token))
 context[b"pass_committed"]=True;context[b"outcome_durable"]=True;context[b"pass_sha"]=pass_sha;context[b"reconciliation_token"]=token
 margin_deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"PASS_MARGIN",context[b"terminal_deadline"],True)
 while time.monotonic_ns()<margin_deadline:owner_poll(context.get(b"actor_control"),context,margin_deadline)
 need(time.monotonic_ns()<=margin_deadline);return report_sha,pass_sha,token

def ack_receipt_record(context,mode,receipt_raw,schedule,actor_lost=False):
 deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"ACK_RECEIPT_RECORD",context[b"terminal_deadline"],False)
 state=b"PIDFD_ACTOR_LOST_NO_REPLAY" if actor_lost else b"ACTOR_ACK_RECEIPT"
 packet_sha=b"NONE" if actor_lost else sha(receipt_raw)
 lines=((b"OUTCOME_KIND",mode),(b"ACK_RECEIPT_STATE",state),(b"ACTOR_RECEIPT_PACKET_SHA256",packet_sha),(b"REPORT_SHA256",context[b"report_sha"]),(b"PASS_SHA256",context.get(b"pass_sha",b"NONE")),(b"RECONCILIATION_TOKEN",context.get(b"reconciliation_token",b"NONE")),(b"NO_REPLAY",b"1"),(b"TERMINAL_SCHEDULE_HEX",schedule_hex(schedule,TERMINAL_PHASE_SPEC)))
 body,digest=chained_record(context,b"ack-receipt.v5",b"P27E001_ACK_RECEIPT_V12",lines,deadline,False,context[b"terminal_deadline"]-deadline,(b"ACK_RECEIPT",));context[b"ack_receipt_sha"]=digest;return digest

def reconciliation_record(context,mode,schedule):
 deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"RECONCILIATION_RECORD",context[b"terminal_deadline"],False)
 lines=((b"OUTCOME_KIND",mode),(b"ACK_RECEIPT_SHA256",context[b"ack_receipt_sha"]),(b"REPORT_SHA256",context[b"report_sha"]),(b"RECONCILIATION_TOKEN",context.get(b"reconciliation_token",b"NONE")),(b"NO_REPLAY",b"1"),(b"TERMINAL_SCHEDULE_HEX",schedule_hex(schedule,TERMINAL_PHASE_SPEC)))
 body,digest=chained_record(context,b"reconciliation.v5",b"P27E001_RECONCILIATION_V12",lines,deadline,False,context[b"terminal_deadline"]-deadline,(b"RECONCILIATION",));context[b"reconciliation_sha"]=digest;return digest

def owner_closure_record(context,mode,schedule):
 deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"OWNER_CLOSURE_RECORD",context[b"terminal_deadline"],False)
 safe=terminal_safe(context);need(safe)
 lines=((b"OUTCOME_KIND",mode),(b"RECONCILIATION_SHA256",context[b"reconciliation_sha"]),(b"REPORT_SHA256",context[b"report_sha"]),(b"CONTAINMENT_SAFE",b"1"),(b"CONTROL_STATE",context[b"control_state"]),(b"ACTOR_STATE",context[b"actor_state"]),(b"OWNER_STATE",b"OWNER_CLOSED_DURABLE"),(b"NO_REPLAY",b"1"),(b"TERMINAL_SCHEDULE_HEX",schedule_hex(schedule,TERMINAL_PHASE_SPEC)))
 body,digest=chained_record(context,b"owner-closure.v5",b"P27E001_OWNER_CLOSURE_V12",lines,deadline,False,context[b"terminal_deadline"]-deadline,(b"OWNER_CLOSURE",));context[b"owner_closure_sha"]=digest;return digest

def send_result(control,ordinal,probe,pid,context,stdout,stderr,out_eof,err_eof,out_over,err_over,empty,faults,done):
 deadline=context[b"origin"]+HOST_NS;out_frames=(len(stdout)+64999)//65000;err_frames=(len(stderr)+64999)//65000
 header=packet(b"V12_RESULT",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"outer_pid",str(pid).encode()),(b"pidfd_bound",b"1" if context[b"pidfd_bound"] else b"0"),(b"pidfd_exit_ready_observed",b"1" if context[b"pidfd_exit_ready_observed"] else b"0"),(b"stdout_len",str(len(stdout)).encode()),(b"stdout_sha256",sha(stdout)),(b"stdout_eof",b"1" if out_eof else b"0"),(b"stdout_frames",str(out_frames).encode()),(b"stderr_len",str(len(stderr)).encode()),(b"stderr_sha256",sha(stderr)),(b"stderr_eof",b"1" if err_eof else b"0"),(b"stderr_frames",str(err_frames).encode()),(b"cgroup_empty",b"1" if empty else b"0"),(b"fault_set",fault_csv(faults)),(b"capture_done_ns",str(done).encode()),(b"result_deadline_ns",str(deadline).encode())))
 send_exact(control,header,deadline)
 for stream,raw in ((b"STDOUT",stdout),(b"STDERR",stderr)):
  for index,start in enumerate(range(0,len(raw),65000)):
   payload=raw[start:start+65000]
   frame=packet(b"V12_RESULT_FRAME",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"stream",stream),(b"index",str(index).encode()),(b"bytes",str(len(payload)).encode()),(b"sha256",sha(payload)),(b"result_deadline_ns",str(deadline).encode())))+payload
   send_exact(control,frame,deadline)
 end=packet(b"V12_RESULT_END",((b"state",b"RESULT_END"),(b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"result_deadline_ns",str(deadline).encode())));send_exact(control,end,deadline)

def set_actor_receive(context,state,ordinal,probe,deadline):
 receiver_binding(state,ordinal,probe,deadline)
 context[b"actor_receive_state"]=state;context[b"actor_receive_ordinal"]=ordinal;context[b"actor_receive_probe"]=probe;context[b"actor_receive_deadline"]=deadline

def stream_arm(control,context,ordinal,probe):
 keys=(b"ordinal",b"probe",b"release_origin_ns",b"launch_deadline_ns",b"stdout_dev",b"stdout_ino",b"stderr_dev",b"stderr_ino",b"events_dev",b"events_ino",b"kill_dev",b"kill_ino")
 fds=();out=err=events=kill=own_events=own_kill=-1
 try:
  receive_ceiling=time.monotonic_ns()+ACK_NS;set_actor_receive(context,b"WAIT_STREAMS_ARMED",str(ordinal).encode(),probe,receive_ceiling)
  raw,fds=recv_monitored(control,4,receive_ceiling,4,b"WAIT_STREAM_ARM",str(ordinal).encode(),probe);need(len(fds)==4)
  out,err,events,kill=fds;fds=()
  values=parse_packet(raw,b"V12_STREAM_ARM",keys,received_binding(raw,b"WAIT_STREAM_ARM",str(ordinal).encode(),probe,b"launch_deadline_ns",receive_ceiling))
  need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe)
  origin=udec(values[b"release_origin_ns"],1);launch=udec(values[b"launch_deadline_ns"],1);need(origin<launch==origin+1000000000)
  post_deadline(launch);checkpoint(CERT,horizon_needed(origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),launch)
  fd_access(out,os.O_RDONLY);fd_access(err,os.O_RDONLY);fd_access(events,os.O_RDONLY);fd_access(kill,os.O_WRONLY)
  need(fcntl.fcntl(out,fcntl.F_GETFL)&os.O_NONBLOCK and fcntl.fcntl(err,fcntl.F_GETFL)&os.O_NONBLOCK)
  outs=os.fstat(out);errs=os.fstat(err);eventss=os.fstat(events);kills=os.fstat(kill)
  need(stat.S_ISFIFO(outs.st_mode) and stat.S_ISFIFO(errs.st_mode) and (outs.st_dev,outs.st_ino)!=(errs.st_dev,errs.st_ino))
  need((outs.st_dev,outs.st_ino)==(udec(values[b"stdout_dev"],1),udec(values[b"stdout_ino"],1)))
  need((errs.st_dev,errs.st_ino)==(udec(values[b"stderr_dev"],1),udec(values[b"stderr_ino"],1)))
  need((eventss.st_dev,eventss.st_ino)==(udec(values[b"events_dev"],1),udec(values[b"events_ino"],1)))
  need((kills.st_dev,kills.st_ino)==(udec(values[b"kill_dev"],1),udec(values[b"kill_ino"],1)))
  own_events=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"cgfd"])
  own_kill=os.open(b"cgroup.kill",os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"cgfd"])
  fd_access(own_events,os.O_RDONLY);fd_access(own_kill,os.O_WRONLY)
  a=os.fstat(own_events);bb=os.fstat(own_kill)
  need((a.st_dev,a.st_ino)==(eventss.st_dev,eventss.st_ino) and (bb.st_dev,bb.st_ino)==(kills.st_dev,kills.st_ino))
  context.update({b"out_fd":out,b"err_fd":err,b"events_fd":events,b"kill_fd":kill,b"origin":origin,b"launch":launch,b"pidfd_bound":False,b"pidfd_exit_ready_observed":False})
  out=err=events=kill=-1
  reply=packet(b"V12_STREAMS_ARMED",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"launch_deadline_ns",str(launch).encode())))
  send_exact(control,reply,launch);checkpoint(CERT,horizon_needed(origin+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),launch)
 finally:
  close_numbers(tuple(fds)+tuple(x for x in (out,err,events,kill,own_events,own_kill) if x>=0))

def pidfd_arm(control,context,ordinal,probe):
 fds=();number=procs=status=-1
 try:
  set_actor_receive(context,b"WAIT_PIDFD_ARMED",str(ordinal).encode(),probe,context[b"launch"])
  raw,fds=recv_monitored(control,4,context[b"launch"],1,b"WAIT_PIDFD_ARM",str(ordinal).encode(),probe);need(len(fds)==1)
  number=fds[0];fds=()
  values=parse_packet(raw,b"V12_PIDFD_ARM",(b"ordinal",b"probe",b"outer_pid",b"outer_starttime",b"stopped_raw_status",b"cgroup_member",b"pidfd_bound"),receiver_binding(b"WAIT_PIDFD_ARM",str(ordinal).encode(),probe,context[b"launch"]))
  need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe)
  pid=udec(values[b"outer_pid"],2);starttime=udec(values[b"outer_starttime"],1);stopped=udec(values[b"stopped_raw_status"],1)
  need(os.WIFSTOPPED(stopped) and os.WSTOPSIG(stopped)==signal.SIGSTOP and values[b"cgroup_member"]==values[b"pidfd_bound"]==b"1")
  fd_access(number,os.O_RDWR);need(pidfd_pid(number)==pid and proc_starttime(pid)==starttime)
  watcher=select.poll();watcher.register(number,select.POLLIN|select.POLLHUP|select.POLLERR);need(watcher.poll(0)==[])
  procs=os.open(b"cgroup.procs",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=context[b"cgfd"])
  status=os.open(b"/proc/"+str(pid).encode()+b"/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
  need(read_all(procs,64)==str(pid).encode()+b"\n")
  state=[x for x in ascii_file(read_all(status,65536),65536).splitlines() if x.startswith(b"State:\t")]
  need(len(state)==1 and state[0].startswith(b"State:\tT") and watcher.poll(0)==[])
  need(pidfd_pid(number)==pid and proc_starttime(pid)==starttime and read_all(procs,64)==str(pid).encode()+b"\n")
  context[b"outer_pidfd"]=number;number=-1;context[b"outer_pid"]=pid;context[b"outer_starttime"]=starttime
  context[b"pidfd_bound"]=True;context[b"pidfd_exit_ready_observed"]=False;context[b"stopped_count"]+=1
  reply=packet(b"V12_PIDFD_ARMED",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"pidfd_bound",b"1"),(b"outer_pid",str(pid).encode()),(b"outer_starttime",str(starttime).encode()),(b"launch_deadline_ns",str(context[b"launch"]).encode())))
  send_exact(control,reply,context[b"launch"]);checkpoint(CERT,horizon_needed(context[b"origin"]+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),context[b"launch"])
 finally:
  close_numbers(tuple(fds)+tuple(x for x in (number,procs,status) if x>=0))

def release_phase(control,context,ordinal,probe):
 set_actor_receive(context,b"WAIT_RELEASE_DURABLE",str(ordinal).encode(),probe,context[b"launch"])
 raw,fds=recv_monitored(control,4,context[b"launch"],0,b"WAIT_RELEASE",str(ordinal).encode(),probe);need(fds==())
 keys=(b"ordinal",b"probe",b"outer_pid",b"outer_starttime",b"pidfd_bound",b"stopped_raw_status",b"cgroup_member",b"cgroup_dev",b"cgroup_ino",b"cgroup_mode",b"cgroup_nlink",b"cgroup_uid",b"cgroup_gid",b"argv_sha256",b"env_sha256",b"release_origin_ns",b"launch_overall_deadline_ns",b"release_record_deadline_ns",b"release_reply_deadline_ns",b"launch_deadline_ns")
 values=parse_packet(raw,b"V12_RELEASE_CANDIDATE",keys,receiver_binding(b"WAIT_RELEASE",str(ordinal).encode(),probe,context[b"launch"]))
 need(udec(values[b"ordinal"],0,14)==ordinal and values[b"probe"]==probe and udec(values[b"outer_pid"],2)==context[b"outer_pid"] and udec(values[b"outer_starttime"],1)==context[b"outer_starttime"] and values[b"pidfd_bound"]==values[b"cgroup_member"]==b"1")
 h64(values[b"argv_sha256"]);h64(values[b"env_sha256"]);need(udec(values[b"release_origin_ns"])==context[b"origin"] and udec(values[b"launch_overall_deadline_ns"])==context[b"launch"])
 record_deadline=udec(values[b"release_record_deadline_ns"]);reply_deadline=udec(values[b"release_reply_deadline_ns"])
 set_actor_receive(context,b"WAIT_RELEASE_DURABLE",str(ordinal).encode(),probe,reply_deadline)
 need(record_deadline==context[b"origin"]+RELEASE_RECORD_OFFSET_NS and reply_deadline==context[b"origin"]+RELEASE_REPLY_OFFSET_NS and udec(values[b"launch_deadline_ns"])==record_deadline and time.monotonic_ns()<=record_deadline)
 cg=os.fstat(context[b"cgfd"]);observed=(cg.st_dev,cg.st_ino,format(cg.st_mode,"o").encode(),cg.st_nlink,cg.st_uid,cg.st_gid)
 supplied=(udec(values[b"cgroup_dev"],1),udec(values[b"cgroup_ino"],1),values[b"cgroup_mode"],udec(values[b"cgroup_nlink"],1),udec(values[b"cgroup_uid"]),udec(values[b"cgroup_gid"]))
 need(observed==supplied)
 checkpoint(CERT,horizon_needed(context[b"origin"]+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),record_deadline);digest=release_record(context,values)
 context[b"payload_release_possible"]=True;context[b"release_send_state"]=b"RELEASE_DURABLE_SEND_EFFECT_UNKNOWN"
 reply=packet(b"V12_RELEASE_DURABLE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"release_sha256",digest),(b"launch_overall_deadline_ns",str(context[b"launch"]).encode()),(b"release_record_deadline_ns",str(record_deadline).encode()),(b"release_reply_deadline_ns",str(reply_deadline).encode()),(b"launch_deadline_ns",str(reply_deadline).encode())))
 send_exact(control,reply,reply_deadline);context[b"release_send_state"]=b"RELEASE_DURABLE_SENT";checkpoint(CERT,horizon_needed(context[b"origin"]+TOTAL_NS,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),context[b"launch"])

def monitor_probe(control,context,ordinal,probe):
 stdout=bytearray();stderr=bytearray();out_eof=err_eof=out_over=err_over=False;faults=set();actor_lost=False
 deadline=context[b"origin"]+HOST_NS;set_actor_receive(context,b"WAIT_RESULT",str(ordinal).encode(),probe,deadline);poller=select.poll()
 for number in (context[b"out_fd"],context[b"err_fd"],context[b"events_fd"],context[b"outer_pidfd"],4,control.fileno()):poller.register(number,select.POLLIN|select.POLLHUP|select.POLLERR)
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
    raw,fds=recv_monitored(control,4,min(deadline,time.monotonic_ns()+ACK_NS),0,b"MONITOR_PROBE",str(ordinal).encode(),probe)
    faults.add(b"CONTROL_MALFORMED")
   except RemoteAbort as error:faults.update(error.faults)
   except PidfdActorLost:actor_lost=True;faults.add(b"PIDFD_ACTOR_LOST")
   except FaultSet as error:faults.update(error.faults)
  elif cmask&(select.POLLHUP|select.POLLERR):
   context[b"control_state"]=b"CONTROL_LOST";faults.add(b"CONTROL_LOST")
  if amask:
   actor_lost=True;context[b"actor_state"]=b"PIDFD_ACTOR_LOST";faults.add(b"PIDFD_ACTOR_LOST")
  for number,event in events:
   if number==context[b"out_fd"]:
    try:
     overflow,eof=drain(number,stdout);out_over|=overflow;out_eof|=eof
    except FaultSet as error:faults.update(error.faults)
   elif number==context[b"err_fd"]:
    try:
     overflow,eof=drain(number,stderr);err_over|=overflow;err_eof|=eof
    except FaultSet as error:faults.update(error.faults)
   elif number==context[b"outer_pidfd"] and event&(select.POLLIN|select.POLLHUP|select.POLLERR):
    context[b"pidfd_exit_ready_observed"]=True
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
 for key in (b"out_fd",b"err_fd",b"events_fd",b"kill_fd",b"outer_pidfd"):
  number=context.get(key,-1)
  if number>=0:
   try:os.close(number)
   except OSError:pass
  context[key]=-1
 context[b"pidfd_bound"]=False;context[b"pidfd_exit_ready_observed"]=False

def request_release_disable(control,context,stop):
 if context[b"release_disabled"] or context[b"actor_lost"]:return
 actual_state=context[b"actor_receive_state"];actual_ordinal=context[b"actor_receive_ordinal"];actual_probe=context[b"actor_receive_probe"]
 if actual_state in (b"NONE",b"UNKNOWN_SEND_EFFECT"):
  context[b"faults"].add(b"RECONCILIATION_UNKNOWN");return
 need(actual_probe==stop or stop==b"NONE")
 deadline=min(context[b"failure_origin"]+ACTOR_DISABLE_NS,context[b"actor_receive_deadline"])
 if time.monotonic_ns()>deadline:context[b"faults"].add(b"DEADLINE_EXPIRED");return
 notice=packet(b"V12_ABORT",((b"sender",b"B"),(b"state",b"ABORTING"),(b"expected_state",actual_state),(b"ordinal",actual_ordinal),(b"probe",actual_probe),(b"effect_state",b"ABORT_NOTICE"),(b"causal_state",b"CLEANUP_RELEASE_DISABLE"),(b"causal_effect",b"CONSUMED"),(b"stage_present",b"1" if context[b"stage_present"] else b"0"),(b"release_disabled",b"0"),(b"terminal_deadline_ns",str(context[b"cleanup_effect_deadline"]).encode()),(b"fault_set",fault_csv(context[b"faults"])),(b"control_deadline_ns",str(deadline).encode())))
 try:
  send_exact(control,notice,deadline)
  raw,fds=recv_monitored(control,4,deadline,0,b"WAIT_RELEASE_DISABLE_ACK",actual_ordinal,actual_probe);need(fds==())
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
 context[b"terminal_phase"]=b"ACTOR_LOSS_DURABLE_NO_REPLAY_OWNER_CLOSED";context[b"owner_released"]=True

def transfer_or_hold(control,context,reason,record_fault=True):
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
 if mode==b"SUCCESS":notice=packet(b"V12_TERMINAL_CANDIDATE_DURABLE",common)
 else:notice=packet(b"V12_TERMINAL_FAILURE_DURABLE",common+((b"disposition",disp),))
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
   raw,fds=recv_monitored(control,4,phase_deadline,0,phase,b"NONE",b"NONE");need(fds==())
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
   values=parse_packet(raw,b"V12_TERMINAL_SEEN",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"notice_packet_sha256",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"seen_deadline_ns"),receiver_binding(b"WAIT_TERMINAL_SEEN",b"NONE",b"NONE",phase_deadline))
   need(values[b"state"]==b"TERMINAL_SEEN" and values[b"expected_state"]==b"WAIT_TERMINAL_SEEN" and values[b"effect_state"]==b"TERMINAL_SEEN")
   need(values[b"ordinal"]==values[b"probe"]==b"NONE" and values[b"kind"]==kind and values[b"subject_sha256"]==subject and values[b"notice_packet_sha256"]==sha(notice))
   need(udec(values[b"terminal_origin_ns"])==context[b"terminal_origin"] and udec(values[b"terminal_deadline_ns"])==deadline and values[b"terminal_schedule_hex"]==schedule_hex(schedule,TERMINAL_PHASE_SPEC))
   terminal_seen_record(context,mode,subject,notice,raw,schedule)
   if mode==b"SUCCESS":report_sha,pass_sha,token=success_report_and_pass(context,schedule);ack_state=b"PASS_COMMITTED_NO_DOWNGRADE"
   else:report_sha=failure_report(context,context[b"stop_probe"],schedule);pass_sha=b"NONE";token=b"NONE";context[b"outcome_durable"]=True;ack_state=b"FAILURE_DURABLE"
   ack_deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"ACK",deadline,False)
   ack=packet(b"V12_TERMINAL_ACK",((b"state",b"TERMINAL_ACK"),(b"expected_state",b"WAIT_TERMINAL_ACK"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",kind),(b"subject_sha256",subject),(b"terminal_seen_sha256",context[b"terminal_seen_sha"]),(b"report_sha256",report_sha),(b"pass_sha256",pass_sha),(b"reconciliation_token",token),(b"ack_state",ack_state),(b"terminal_origin_ns",str(context[b"terminal_origin"]).encode()),(b"terminal_deadline_ns",str(deadline).encode()),(b"terminal_schedule_hex",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"ack_deadline_ns",str(ack_deadline).encode())))
   context[b"terminal_ack_raw"]=ack;context[b"ack_state"]=b"ACK_SEND_EFFECT_UNKNOWN";context[b"send_state"]=b"ACK_SEND_EFFECT_UNKNOWN";context[b"terminal_phase"]=b"ACK_SEND_EFFECT_UNKNOWN"
   try:send_exact(control,ack,ack_deadline);context[b"ack_state"]=b"ACK_SENT";context[b"send_state"]=b"ACK_SENT"
   except SendEffectUnknown:context[b"ack_effect_unknown"]=True;context[b"faults"].add(b"ACK_EFFECT_UNKNOWN");context[b"send_state"]=b"ACK_SEND_EFFECT_UNKNOWN"
   context[b"terminal_phase"]=b"WAIT_ACK_RECEIPT"
  elif phase==b"WAIT_ACK_RECEIPT":
   values=parse_packet(raw,b"V12_TERMINAL_ACK_RECEIPT",(b"state",b"ordinal",b"probe",b"kind",b"subject_sha256",b"ack_packet_sha256",b"report_sha256",b"pass_sha256",b"reconciliation_token",b"actor_receipt_ns",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"receipt_deadline_ns"),receiver_binding(b"WAIT_ACK_RECEIPT",b"NONE",b"NONE",phase_deadline))
   need(values[b"state"]==b"ACK_RECEIVED_NO_REPLAY" and values[b"expected_state"]==b"WAIT_ACK_RECEIPT" and values[b"effect_state"]==b"NO_REPLAY_RECEIPT")
   need(values[b"ordinal"]==values[b"probe"]==b"NONE" and values[b"kind"]==kind and values[b"subject_sha256"]==subject and values[b"ack_packet_sha256"]==sha(context[b"terminal_ack_raw"]))
   need(values[b"report_sha256"]==context[b"report_sha"] and values[b"pass_sha256"]==context.get(b"pass_sha",b"NONE") and values[b"reconciliation_token"]==context.get(b"reconciliation_token",b"NONE"))
   need(udec(values[b"actor_receipt_ns"],1)<=time.monotonic_ns() and udec(values[b"terminal_origin_ns"])==context[b"terminal_origin"] and udec(values[b"terminal_deadline_ns"])==deadline)
   need(values[b"terminal_schedule_hex"]==schedule_hex(schedule,TERMINAL_PHASE_SPEC))
   ack_receipt_record(context,mode,raw,schedule,False);reconciliation_record(context,mode,schedule);closure_sha=owner_closure_record(context,mode,schedule)
   closure_deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"CLOSURE_PACKET",deadline,False)
   closed_packet=packet(b"V12_TERMINAL_CLOSED",((b"state",b"OWNER_CLOSED"),(b"expected_state",b"WAIT_OWNER_CLOSED"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"kind",kind),(b"subject_sha256",subject),(b"report_sha256",context[b"report_sha"]),(b"pass_sha256",context.get(b"pass_sha",b"NONE")),(b"ack_receipt_sha256",context[b"ack_receipt_sha"]),(b"reconciliation_sha256",context[b"reconciliation_sha"]),(b"closure_sha256",closure_sha),(b"owner",b"B"),(b"terminal_origin_ns",str(context[b"terminal_origin"]).encode()),(b"terminal_deadline_ns",str(deadline).encode()),(b"terminal_schedule_hex",schedule_hex(schedule,TERMINAL_PHASE_SPEC)),(b"closure_deadline_ns",str(closure_deadline).encode())))
   context[b"terminal_phase"]=b"OWNER_CLOSE_SEND_EFFECT_UNKNOWN";context[b"send_state"]=b"OWNER_CLOSE_SEND_EFFECT_UNKNOWN"
   try:
    send_exact(control,closed_packet,closure_deadline);context[b"terminal_phase"]=b"OWNER_CLOSED";context[b"send_state"]=b"OWNER_CLOSED_SENT"
    exit_deadline=phase_boundary(context,schedule,TERMINAL_PHASE_SPEC,b"B_EXIT",deadline,False);need(time.monotonic_ns()<=exit_deadline and terminal_safe(context));context[b"owner_released"]=True;return
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
  try:os.close(context[b"attempt_base_fd"])
  except OSError:context[b"faults"].add(b"ATTEMPT_DIRFD_UNKNOWN")
  else:
   context[b"attempt_base_fd"]=-1
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
  context[b"collision_transfer_claim_sha"]=sha(b"P27E001_COLLISION_V12\x00"+AUTH+b"\x00"+fault_csv(context[b"faults"])+b"\x00"+str(context[b"failure_origin"]).encode()+b"\x00"+mutation_state+b"\x00"+(b"1" if context[b"attempt_base_fd"]<0 else b"0"))
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
 raw,fds=recv_monitored(control,4,context[b"origin"]+TOTAL_NS,0,b"WAIT_VALIDATED",str(ordinal).encode(),probe);need(fds==())
 candidate_binding=received_binding(raw,b"WAIT_VALIDATED",str(ordinal).encode(),probe,b"ack_deadline_ns",context[b"origin"]+TOTAL_NS)
 values=parse_packet(raw,b"V12_VALIDATED_CANDIDATE",CANDIDATE_KEYS,candidate_binding)
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
 reply=packet(b"V12_VALIDATED_DURABLE",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"validated_sha256",validated_sha),(b"ack_deadline_ns",str(ack_deadline).encode())))
 send_exact(control,reply,ack_deadline)
 raw,fds=recv_monitored(control,4,ack_deadline,0,b"WAIT_ACK_INTENT",str(ordinal).encode(),probe);need(fds==())
 intent=parse_packet(raw,b"V12_ACK_COMMIT_INTENT",(b"ordinal",b"probe",b"validated_sha256",b"host_complete_ns",b"ack_deadline_ns",b"actor_ack_intent_ns"),receiver_binding(b"WAIT_ACK_INTENT",str(ordinal).encode(),probe,ack_deadline))
 set_actor_receive(context,b"WAIT_COMMITTED",str(ordinal).encode(),probe,ack_deadline)
 need(udec(intent[b"ordinal"],0,14)==ordinal and intent[b"probe"]==probe and intent[b"validated_sha256"]==validated_sha)
 actor_ack=udec(intent[b"actor_ack_intent_ns"]);received=time.monotonic_ns();ack_deadline=udec(intent[b"ack_deadline_ns"],1)
 need(udec(intent[b"host_complete_ns"])==host_complete and ack_deadline==min(context[b"origin"]+TOTAL_NS,host_complete+ACK_NS))
 need(host_complete<=actor_ack<=received<=ack_deadline and actor_ack-host_complete<=ACK_NS)
 checkpoint(CERT,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ack_deadline)
 ack_sha=ack_intent_record(context,ordinal,probe,actor_ack,received,ack_deadline)
 checkpoint(CERT,horizon_needed(ack_deadline,(14-ordinal)*TOTAL_NS+REPORT_NS+FINAL_TOTAL_NS),ack_deadline)
 final_count=sum(context[b"committed"])+1;commit_record_seq=context[b"record_seq"]+1
 committed,reserved_control_seq=reserve_packet(b"V12_COMMITTED",((b"ordinal",str(ordinal).encode()),(b"probe",probe),(b"ack_sha256",ack_sha),(b"commit_record_seq",str(commit_record_seq).encode()),(b"committed_count",str(final_count).encode()),(b"ack_deadline_ns",str(ack_deadline).encode())))
 commit_sha=committed_record(context,ordinal,probe,ack_sha,committed,reserved_control_seq,final_count,ack_deadline)
 activate_reserved_packet(committed,reserved_control_seq)
 need(context[b"committed"][ordinal] and context[b"direct_reaps"]==final_count and context[b"direct_reap_state"]==b"COMPLETE")
 need(context[b"last_committed_record_sha"]==commit_sha and context[b"last_committed_packet_sha"]==sha(committed) and context[b"last_committed_packet_message_seq"]==reserved_control_seq)
 need(context[b"committed_send_state"]==b"COMMITTED_SEND_EFFECT_UNKNOWN" and context.get(b"committed_seen_sha",b"0"*64)!=commit_sha)
 send_exact(control,committed,ack_deadline);context[b"committed_send_state"]=b"COMMITTED_SENT"
 raw,fds=recv_monitored(control,4,ack_deadline,0,b"WAIT_COMMITTED_SEEN",str(ordinal).encode(),probe);need(fds==())
 seen=parse_packet(raw,b"V12_COMMITTED_SEEN",(b"ordinal",b"probe",b"ack_sha256",b"committed_packet_sha256",b"committed_count",b"host_complete_ns",b"ack_deadline_ns"),receiver_binding(b"WAIT_COMMITTED_SEEN",str(ordinal).encode(),probe,ack_deadline))
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
  base=os.open(b".",O_DIR);base_check(base,CERT,b"SAFE_BIND");base_mid,base_line=mount_binding(base)
  record_boundary(context,deadline,False,FAILURE_TAIL_NS)
  need(base_mid==udec(CERT[b"SAFE_BIND_MOUNT_ID"],1) and sha(base_line)==CERT[b"SAFE_BIND_MOUNTINFO_SHA256"])
  named=os.stat(AUTH,dir_fd=base,follow_symlinks=False);number=os.open(AUTH,O_DIR,dir_fd=base);held=os.fstat(number)
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
   leaf=os.open(name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number);body=read_all(leaf,udec(CERT[bkey],1));st=os.fstat(leaf)
   need(stat.S_ISREG(st.st_mode) and (st.st_uid,st.st_gid,stat.S_IMODE(st.st_mode),st.st_nlink)==(0,0,0o400,1))
   need((len(body),body.count(b"\n"),sha(body))==(udec(CERT[bkey],1),udec(CERT[lkey]),CERT[hkey]))
   record_boundary(context,deadline,False,FAILURE_TAIL_NS);os.close(leaf);leaf=-1
  again=os.stat(AUTH,dir_fd=base,follow_symlinks=False);need(identity==(again.st_dev,again.st_ino,again.st_mode,again.st_nlink,again.st_uid,again.st_gid))
  record_boundary(context,deadline,False,FAILURE_TAIL_NS)
  verified_identity=identity;verified=True
 except FileNotFoundError:
  context[b"stage_state"]=b"ABSENT_KNOWN"
 except FaultSet as error:
  context[b"stage_state"]=b"UNKNOWN";context[b"faults"].update(error.faults);context[b"faults"].add(b"STAGING_FAULT")
 except BaseException:
  context[b"stage_state"]=b"UNKNOWN";context[b"faults"].add(b"STAGING_FAULT")
 finally:close_numbers(tuple(x for x in (leaf,base) if x>=0))
 if verified:
  context[b"stage_fd"]=number;number=-1;context[b"stage_identity"]=verified_identity;context[b"stage_present"]=True;context[b"stage_state"]=b"VERIFIED_PRESENT"
 else:
  close_numbers(tuple(x for x in (number,) if x>=0));context[b"stage_fd"]=-1;context[b"stage_present"]=False

def stage_bind(control,context):
 fds=();number=base=leaf=-1
 keys=(b"state",b"ordinal",b"probe",b"stage_origin_ns",b"stage_deadline_ns",b"stage_return_ns",b"safe_dev",b"safe_ino",b"safe_mode",b"safe_nlink",b"safe_uid",b"safe_gid",b"keeper_sha256",b"launcher_sha256",b"marker_sha256",b"child_sha256")
 try:
  boot=time.monotonic_ns()+STAGE_NS;set_actor_receive(context,b"WAIT_STAGE_ACK",b"NONE",b"NONE",boot)
  raw,fds=recv_monitored(control,4,boot,1,b"WAIT_STAGE",b"NONE",b"NONE");need(len(fds)==1)
  number=fds[0];fds=()
  values=parse_packet(raw,b"V12_STAGE_DURABLE",keys,received_binding(raw,b"WAIT_STAGE",b"NONE",b"NONE",b"stage_deadline_ns",boot))
  need(values[b"state"]==b"STAGE_DURABLE" and values[b"ordinal"]==values[b"probe"]==b"NONE")
  origin=udec(values[b"stage_origin_ns"],1);deadline=udec(values[b"stage_deadline_ns"],1)
  need(deadline==origin+STAGE_NS and udec(values[b"stage_return_ns"],origin,deadline)<=time.monotonic_ns()<=deadline)
  checkpoint(CERT,POST_STAGE_REMAIN_NS,deadline);fd_access(number,os.O_RDONLY)
  held=os.fstat(number);supplied=(udec(values[b"safe_dev"],1),udec(values[b"safe_ino"],1),octal(values[b"safe_mode"]),udec(values[b"safe_nlink"],1),udec(values[b"safe_uid"]),udec(values[b"safe_gid"]))
  need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)==supplied)
  need(stat.S_ISDIR(held.st_mode) and stat.S_IMODE(held.st_mode)==0o700 and held.st_uid==held.st_gid==0 and held.st_nlink==2)
  base=os.open(b".",O_DIR);base_check(base,CERT,b"SAFE_BIND")
  named=os.stat(AUTH,dir_fd=base,follow_symlinks=False)
  need((named.st_dev,named.st_ino,named.st_mode,named.st_nlink,named.st_uid,named.st_gid)==(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid))
  specs=((b"keeper.py",b"KEEPER_BYTES",b"KEEPER_LF",b"KEEPER_SHA256",b"keeper_sha256"),(b"launcher.py",b"LAUNCHER_BYTES",b"LAUNCHER_LF",b"LAUNCHER_SHA256",b"launcher_sha256"),(b"marker.py",b"MARKER_BYTES",b"MARKER_LF",b"MARKER_SHA256",b"marker_sha256"),(b"child.py",b"CHILD_BYTES",b"CHILD_LF",b"CHILD_SHA256",b"child_sha256"))
  for name,bkey,lkey,hkey,pkey in specs:
   try:
    leaf=os.open(name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number);fd_access(leaf,os.O_RDONLY)
    body=read_all(leaf,udec(CERT[bkey],1));st=os.fstat(leaf)
    need(stat.S_ISREG(st.st_mode) and (st.st_uid,st.st_gid,stat.S_IMODE(st.st_mode),st.st_nlink)==(0,0,0o400,1))
    need((len(body),body.count(b"\n"),sha(body))==(udec(CERT[bkey],1),udec(CERT[lkey]),CERT[hkey]))
    need(values[pkey]==CERT[hkey])
   finally:close_numbers(tuple(x for x in (leaf,) if x>=0));leaf=-1
  again=os.stat(AUTH,dir_fd=base,follow_symlinks=False);base_check(base,CERT,b"SAFE_BIND");fd_access(number,os.O_RDONLY)
  need((again.st_dev,again.st_ino,again.st_mode,again.st_nlink,again.st_uid,again.st_gid)==(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid))
  checkpoint(CERT,POST_STAGE_REMAIN_NS,deadline)
  context[b"stage_fd"]=number;number=-1;context[b"stage_identity"]=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)
  context[b"stage_present"]=True;context[b"stage_state"]=b"VERIFIED_PRESENT";context[b"stage_deadline"]=deadline
  reply=packet(b"V12_STAGE_ACK",((b"state",b"STAGE_BOUND"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"stage_deadline_ns",str(deadline).encode()),(b"safe_dev",str(held.st_dev).encode()),(b"safe_ino",str(held.st_ino).encode())))
  send_exact(control,reply,deadline);checkpoint(CERT,POST_STAGE_REMAIN_NS,deadline)
 finally:
  close_numbers(tuple(fds)+tuple(x for x in (leaf,number,base) if x>=0))

def containment_bind(control,context):
 fds=();number=root_events=root_kill=ctype=controllers=subtree=-1
 try:
  boot=time.monotonic_ns()+ACK_NS;set_actor_receive(context,b"WAIT_CONTAINMENT_ACK",b"NONE",b"NONE",boot)
  raw,fds=recv_monitored(control,4,boot,1,b"WAIT_CONTAINMENT",b"NONE",b"NONE");need(len(fds)==1)
  number=fds[0];fds=()
  keys=(b"state",b"ordinal",b"probe",b"contain_origin_ns",b"contain_deadline_ns",b"dev",b"ino",b"mode",b"nlink",b"uid",b"gid",b"base_dev",b"base_ino",b"mount_id",b"mountinfo_sha256",b"type_hex",b"controllers_hex",b"subtree_control_hex")
  values=parse_packet(raw,b"V12_CONTAINMENT",keys,received_binding(raw,b"WAIT_CONTAINMENT",b"NONE",b"NONE",b"contain_deadline_ns",boot))
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
  ctype=os.open(b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  controllers=os.open(b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  subtree=os.open(b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  root_events=os.open(b"cgroup.events",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  root_kill=os.open(b"cgroup.kill",os.O_WRONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=number)
  fd_access(ctype,os.O_RDONLY);fd_access(controllers,os.O_RDONLY);fd_access(subtree,os.O_RDONLY);fd_access(root_events,os.O_RDONLY);fd_access(root_kill,os.O_WRONLY)
  type_raw=read_all(ctype,128);controllers_raw=read_all(controllers,4096);subtree_raw=read_all(subtree,4096)
  need(type_raw.hex().encode()==values[b"type_hex"]==CERT[b"CGROUP_CHILD_TYPE_HEX"])
  need(controllers_raw.hex().encode()==values[b"controllers_hex"]==CERT[b"CGROUP_CHILD_CONTROLLERS_HEX"])
  need(subtree_raw.hex().encode()==values[b"subtree_control_hex"]==CERT[b"CGROUP_CHILD_SUBTREE_CONTROL_HEX"])
  need(not populated(root_events));checkpoint(CERT,POST_CONTAIN_REMAIN_NS,deadline)
  context[b"cgfd"]=number;number=-1;context[b"root_events_fd"]=root_events;root_events=-1
  context[b"root_kill_fd"]=root_kill;root_kill=-1;context[b"containment_bound"]=True;context[b"contain_deadline"]=deadline
  context[b"cgroup_identity"]=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid)
  reply=packet(b"V12_CONTAINMENT_ACK",((b"state",b"CONTAINMENT_BOUND"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"contain_deadline_ns",str(deadline).encode()),(b"dev",str(held.st_dev).encode()),(b"ino",str(held.st_ino).encode())))
  send_exact(control,reply,deadline);checkpoint(CERT,POST_CONTAIN_REMAIN_NS,deadline)
 finally:
  close_numbers(tuple(fds)+tuple(x for x in (number,root_events,root_kill,ctype,controllers,subtree) if x>=0))

def acquire_control(actor_pid):
 control=None
 try:
  control=socket.socket(fileno=3)
  need(control.getsockopt(socket.SOL_SOCKET,socket.SO_TYPE)==socket.SOCK_SEQPACKET);fd_access(3,os.O_RDWR)
  need(fcntl.fcntl(3,fcntl.F_GETFL)&os.O_NONBLOCK)
  peer=struct.unpack("3i",control.getsockopt(socket.SOL_SOCKET,socket.SO_PEERCRED,12));need(peer==(actor_pid,0,0))
  result=control;control=None;return result
 finally:
  if control is not None:
   try:control.close()
   except BaseException:pass

EXTERNAL_MANIFEST_KEYS=(b"VERSION",b"SESSION_AUTH_POLICY",b"OWNER_PID",b"OWNER_STARTTIME",b"OWNER_UID",b"OWNER_GID",b"ENDPOINT_TYPE",b"PIDFD_REQUIRED",b"MAX_PACKET_BYTES",b"RIGHTS_TYPES",b"REFUSAL_RECEIPT_PROTOCOL",b"TRANSFER_PROTOCOL",b"NO_REPLAY")
EXTERNAL_RIGHTS_TYPES=b"ATTEMPT_DIRFD,ATTEMPT_BASE_DIRFD,STAGE_DIRFD,CGROUP_DIRFD,OUT_FD,ERR_FD,EVENTS_FD,KILL_FD,OUTER_PIDFD,CGROUP_BASE_DIRFD,ACTOR_CONTROL_FD,PENDING_EXPECTED_RAW_FD"

def parse_external_manifest(raw,cert):
 values=parse_fixed(raw,b"P27E001_EXTERNAL_OWNER_MANIFEST_V12",EXTERNAL_MANIFEST_KEYS,b"MANIFEST_END=1")
 exact={b"VERSION":b"12",b"SESSION_AUTH_POLICY":b"AUTH_V12_LENGTH_FRAMED",b"OWNER_PID":cert[b"EXTERNAL_OWNER_PID"],b"OWNER_STARTTIME":cert[b"EXTERNAL_OWNER_STARTTIME"],b"OWNER_UID":cert[b"EXTERNAL_OWNER_UID"],b"OWNER_GID":cert[b"EXTERNAL_OWNER_GID"],b"ENDPOINT_TYPE":b"SOCK_SEQPACKET",b"PIDFD_REQUIRED":b"1",b"MAX_PACKET_BYTES":b"65536",b"RIGHTS_TYPES":EXTERNAL_RIGHTS_TYPES,b"REFUSAL_RECEIPT_PROTOCOL":b"MONOTONE_O_EXCL_ISSUER_V12",b"TRANSFER_PROTOCOL":b"OFFER_ACCEPTED_DURABLE_V12",b"NO_REPLAY":b"1"}
 for key,value in exact.items():need(values[key]==value)
 return values

def acquire_external_owner():
 pid=udec(CERT[b"EXTERNAL_OWNER_PID"],2);start=udec(CERT[b"EXTERNAL_OWNER_STARTTIME"],1)
 fd_access(14,os.O_RDWR);fd_access(15,os.O_RDWR);need(pidfd_pid(15)==pid)
 watcher=select.poll();watcher.register(15,select.POLLIN|select.POLLHUP|select.POLLERR);need(watcher.poll(0)==[])
 external=socket.socket(fileno=14)
 try:
  need(external.getsockopt(socket.SOL_SOCKET,socket.SO_TYPE)==socket.SOCK_SEQPACKET and fcntl.fcntl(14,fcntl.F_GETFL)&os.O_NONBLOCK)
  peer=struct.unpack("3i",external.getsockopt(socket.SOL_SOCKET,socket.SO_PEERCRED,12));need(peer==(pid,udec(CERT[b"EXTERNAL_OWNER_UID"]),udec(CERT[b"EXTERNAL_OWNER_GID"])))
  need(proc_starttime(pid)==start and pidfd_pid(15)==pid and proc_starttime(pid)==start and watcher.poll(0)==[])
  result=external;external=None;return result
 finally:
  if external is not None:external.close()

def static_inputs():
 global AUTH,CERT,DEPS,RESERVATION_DIGEST,ACTOR_PID,ACTOR_STARTTIME,ISSUER_KEY_ID
 need(type(sys.argv)is list and len(sys.argv)==9 and sys.argv[0]=="/proc/self/fd/100" and sys.argv[1]=="RECOVER_V12")
 supplied=h64(sys.argv[2].encode("ascii"));actor_pid=udec(sys.argv[3].encode("ascii"),2);actor_starttime=udec(sys.argv[4].encode("ascii"),1)
 plan_sha=h64(sys.argv[5].encode("ascii"));source_sha=h64(sys.argv[6].encode("ascii"))
 safe_dev=udec(sys.argv[7].encode("ascii"),1);safe_ino=udec(sys.argv[8].encode("ascii"),1)
 ACTOR_PID=actor_pid;ACTOR_STARTTIME=actor_starttime
 need(os.read(0,1)==b"");fd_access(0,os.O_RDONLY);need(stat.S_ISFIFO(os.fstat(0).st_mode));closed(1);closed(2)
 fd_access(4,os.O_RDWR);need(pidfd_pid(4)==actor_pid and proc_starttime(actor_pid)==actor_starttime)
 actor_watcher=select.poll();actor_watcher.register(4,select.POLLIN|select.POLLHUP|select.POLLERR);need(actor_watcher.poll(0)==[] and pidfd_pid(4)==actor_pid and proc_starttime(actor_pid)==actor_starttime)
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
 need(extract_one(plan_raw,b"P27 RUNNER V12 ACTOR SOURCE BEGIN C5A91E34",b"P27 RUNNER V12 ACTOR SOURCE END C5A91E34")==actor_raw)
 need(extract_one(plan_raw,b"P27 RUNNER V12 WATCHDOG SOURCE BEGIN F5C2189D",b"P27 RUNNER V12 WATCHDOG SOURCE END F5C2189D")==source_raw)
 need(issued[b"E0366_SNAPSHOT_SHA256"]==CERT[b"E0366_SNAPSHOT_SHA256"]==sha(snapshot_raw)==SNAPSHOT_EXPECT[2])
 need(issued[b"E0366_SNAPSHOT_BYTES"]==CERT[b"E0366_SNAPSHOT_BYTES"]==b"2303269" and issued[b"E0366_SNAPSHOT_LF"]==CERT[b"E0366_SNAPSHOT_LF"]==b"23672")
 need(issued[b"E0366_SNAPSHOT_TERMINAL_HEX"]==CERT[b"E0366_SNAPSHOT_TERMINAL_HEX"]==SNAPSHOT_TERMINAL_HEX)
 need(issued[b"V15_SHA256"]==CERT[b"V15_SHA256"]==V15_SHA)
 need((len(transfer_manifest_raw),sha(transfer_manifest_raw))==(udec(CERT[b"EXTERNAL_TRANSFER_MANIFEST_BYTES"],1),CERT[b"EXTERNAL_TRANSFER_MANIFEST_SHA256"]));parse_external_manifest(transfer_manifest_raw,CERT)
 need(reservation[b"NOT_BEFORE_REALTIME_NS"]==issued[b"NOT_BEFORE_REALTIME_NS"] and reservation[b"NOT_AFTER_REALTIME_NS"]==issued[b"NOT_AFTER_REALTIME_NS"])
 base_check(5,CERT,b"ATTEMPT_BASE");base_check(6,CERT,b"CGROUP_BASE")
 rootfd=safebase=-1
 try:
  rootfd=os.open(b"/",O_DIR);safebase=os.open(b".",O_DIR)
  base_check(rootfd,CERT,b"RUNTIME_ROOT");base_check(safebase,CERT,b"SAFE_BIND")
  root_mid,root_line=mount_binding(rootfd);safe_mid,safe_line=mount_binding(safebase)
  need(root_mid==udec(CERT[b"RUNTIME_ROOT_MOUNT_ID"],1) and sha(root_line)==CERT[b"RUNTIME_ROOT_MOUNTINFO_SHA256"])
  need(safe_mid==udec(CERT[b"SAFE_BIND_MOUNT_ID"],1) and sha(safe_line)==CERT[b"SAFE_BIND_MOUNTINFO_SHA256"] and root_mid!=safe_mid)
  mount_semantics(root_line,even_hex(CERT[b"RUNTIME_ROOT_FSTYPE_HEX"]),{b"ro",b"nosuid",b"nodev"},{b"rw"})
  mount_semantics(safe_line,even_hex(CERT[b"SAFE_BIND_FSTYPE_HEX"]),{b"rw",b"nosuid",b"nodev",b"noexec"},{b"ro"})
  mount_graph(CERT)
 finally:close_numbers(tuple(x for x in (rootfd,safebase) if x>=0))
 attempt_mid,attempt_line=mount_binding(5)
 need(attempt_mid==udec(CERT[b"ATTEMPT_BASE_MOUNT_ID"],1) and sha(attempt_line)==CERT[b"ATTEMPT_BASE_MOUNTINFO_SHA256"])
 mount_semantics(attempt_line,even_hex(CERT[b"ATTEMPT_BASE_FSTYPE_HEX"]),{b"rw",b"nosuid",b"nodev"},{b"ro"})
 cgroup_mid,cgroup_line=mount_binding(6)
 need(statfs_magic(6)==int(CERT[b"CGROUP2_FS_MAGIC"],16) and cgroup_mid==udec(CERT[b"CGROUP2_MOUNT_ID"],1) and sha(cgroup_line)==CERT[b"CGROUP2_MOUNTINFO_SHA256"])
 mount_semantics(cgroup_line,b"cgroup2",{b"rw"},{b"ro"})
 base_type=base_controllers=base_subtree=-1
 try:
  base_type=os.open(b"cgroup.type",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=6)
  base_controllers=os.open(b"cgroup.controllers",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=6)
  base_subtree=os.open(b"cgroup.subtree_control",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=6)
  need(read_all(base_type,128).hex().encode()==CERT[b"CGROUP_BASE_TYPE_HEX"])
  need(read_all(base_controllers,4096).hex().encode()==CERT[b"CGROUP_BASE_CONTROLLERS_HEX"])
  need(read_all(base_subtree,4096).hex().encode()==CERT[b"CGROUP_BASE_SUBTREE_CONTROL_HEX"])
 finally:close_numbers((base_type,base_controllers,base_subtree))
 need((safe_dev,safe_ino)==(udec(CERT[b"SAFE_BIND_DEV"],1),udec(CERT[b"SAFE_BIND_INO"],1)))
 final_context(safe_dev,safe_ino);scrub_exact({0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,100});checkpoint(CERT,ENTRY_REMAIN_NS)
 return acquire_control(actor_pid),acquire_external_owner(),cert_raw,envelope_raw,reservation_raw,source_raw

def minimal_context():
 return {
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
  b"cgfd":-1,b"root_events_fd":-1,b"root_kill_fd":-1,b"events_fd":-1,b"kill_fd":-1,b"out_fd":-1,b"err_fd":-1,
  b"outer_pidfd":-1,b"pidfd_bound":False,b"pidfd_exit_ready_observed":False,b"outer_pid":-1,b"outer_starttime":0,b"removed":False,
  b"report_state":b"ABSENT_KNOWN",b"report_sha":b"0"*64,b"retained_state":b"ABSENT_KNOWN",
  b"candidate_sha":b"0"*64,b"terminal_seen_sha":b"0"*64,b"reconciliation_token":b"0"*64,b"reconciliation_sha":b"0"*64,
  b"terminal_origin":0,b"terminal_deadline":0,b"terminal_mode":b"NONE",b"terminal_kind":b"NONE",b"terminal_subject":b"0"*64,
  b"terminal_phase":b"NOT_STARTED",b"ack_state":b"NOT_SENT",b"ack_effect_unknown":False,b"pass_effect_possible":False,b"pass_committed":False,
  b"control_state":b"CONNECTED",b"actor_state":b"ALIVE_PIDFD_NOT_READY",b"send_state":b"IDLE",
  b"actor_receive_state":b"NONE",b"actor_receive_ordinal":b"NONE",b"actor_receive_probe":b"NONE",b"actor_receive_deadline":1,
  b"transfer_control":None,b"actor_control":None,b"external_record_seq":0,b"external_chain_sha":RESERVATION_DIGEST,b"external_send_state":b"IDLE",b"transfer_state":b"NOT_OFFERED",b"transfer_offer_cache":None,b"frozen_transfer_reason":None,b"offer_delivery_possible":False,b"transfer_receipt_sha":b"0"*64,b"transfer_acceptance_state":b"NOT_STARTED",b"transfer_capabilities_closed":False,b"refusal_closure_sha":b"0"*64,
  b"refusal_prevalidation_state":b"NOT_SEEN",b"refusal_slot_locked":False,b"refusal_offer_cache":None,b"refusal_close_state":b"CLOSE_NOT_ATTEMPTED",b"refusal_finality_state":b"OPEN",b"refusal_control_eof":False,b"refusal_actor_loss_seen":False,b"refusal_candidate_fault_evidence":(),b"refusal_candidate_fault_overflow":0,b"refusal_finality_evidence_sha":EMPTY_SHA,b"refusal_finality_timeout_observed":False,b"refusal_frozen_state_sha":EMPTY_SHA,b"refusal_offer_delivery_possible":False,b"refusal_offer_complete":False,b"refusal_offer_state":b"NOT_STARTED",b"refusal_offer_receipt_sha":b"0"*64,b"refusal_acceptance_state":b"NOT_STARTED",b"refusal_acceptance_hold_reason":b"NONE",b"refusal_actor_closure_complete":False,b"refusal_actor_closure_state":b"NOT_STARTED",b"refusal_capabilities_closed":False,b"refusal_closure_hold_state":b"NONE",
  b"outcome_durable":False,b"owner_released":False
 }

def ambiguous_consumption(control,context,cert_raw,envelope_raw,source_raw,error):
 context[b"consumed"]=True;context[b"consumption_state"]=b"CONSUME_EDGE_UNKNOWN";context[b"faults"].add(b"CONSUME_EDGE_UNKNOWN")
 if isinstance(error,RemoteAbort):
  context[b"faults"].update(error.faults);context[b"release_disabled"]=True
 elif isinstance(error,FaultSet):context[b"faults"].update(error.faults)
 elif isinstance(error,PidfdActorLost):
  context[b"faults"].add(b"PIDFD_ACTOR_LOST");context[b"actor_lost"]=True;context[b"release_disabled"]=True
 try:consume_attempt(context,cert_raw,envelope_raw,source_raw,context[b"consume_deadline"])
 except CertificateExpired:context[b"faults"].add(b"CERTIFICATE_EXPIRED")
 except FaultSet as attempt_error:context[b"faults"].update(attempt_error.faults)
 terminal_failure(control,context,b"NONE",set(context[b"faults"]),isinstance(error,PidfdActorLost))

def refusal_values(raw,kind):
 need(kind in (b"V12_REFUSE_PREBEGIN",b"V12_REFUSE_POSTARM"))
 keys=(b"state",b"ordinal",b"probe",b"auth_id",b"a_begin_state",b"a_arm_state",b"cross_map_state",b"reason",b"refusal_origin_ns",b"refusal_finality_deadline_ns",b"refusal_closure_deadline_ns",b"refusal_schedule_hex",b"consume_deadline_ns")
 actual_pre_state=b"WAIT_BEGIN" if kind==b"V12_REFUSE_PREBEGIN" else b"WAIT_COMMIT"
 values=parse_packet(raw,kind,keys,received_binding(raw,actual_pre_state,b"NONE",b"NONE",b"consume_deadline_ns",certificate_mono_expiry(CERT)))
 if kind==b"V12_REFUSE_PREBEGIN":
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
  os.close(context[b"attempt_base_fd"]);context[b"attempt_base_fd"]=-1
 if context.get(b"cgroup_base_fd",6)>=0:
  os.close(context[b"cgroup_base_fd"]);context[b"cgroup_base_fd"]=-1
 os.chdir(b"/");rootfd=os.open(b".",O_DIR)
 try:base_check(rootfd,CERT,b"RUNTIME_ROOT");fd_access(rootfd,os.O_RDONLY)
 finally:os.close(rootfd)
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
  ack,reserved_ack_sequence=reserve_packet(b"V12_REFUSE_ACK",((b"state",b"REFUSAL_CLOSED_NO_CONSUME"),(b"expected_state",b"WAIT_REFUSAL_ACK"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH),(b"a_begin_state",values[b"a_begin_state"]),(b"a_arm_state",values[b"a_arm_state"]),(b"cross_map_state",values[b"cross_map_state"]),(b"request_packet_sha256",values[b"packet_sha256"]),(b"request_message_seq",values[b"message_seq"]),(b"commit_count",b"0"),(b"attempt_state",b"ABSENT_KNOWN"),(b"intent_count",b"0"),(b"disposition",b"UNCONSUMED"),(b"refusal_origin_ns",values[b"refusal_origin_ns"]),(b"refusal_finality_deadline_ns",values[b"refusal_finality_deadline_ns"]),(b"refusal_closure_deadline_ns",values[b"refusal_closure_deadline_ns"]),(b"refusal_schedule_hex",values[b"refusal_schedule_hex"]),(b"consume_deadline_ns",str(ack_deadline).encode())))
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
 context=minimal_context();control=transfer_control=None
 try:
  control,transfer_control,cert_raw,envelope_raw,reservation_raw,source_raw=static_inputs();context[b"transfer_control"]=transfer_control;context[b"actor_control"]=control;context[b"external_chain_sha"]=RESERVATION_DIGEST
  ready_deadline=time.monotonic_ns()+10000000000
  ready=packet(b"V12_READY",((b"state",b"READY"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"ready_deadline_ns",str(ready_deadline).encode())))
  send_exact(control,ready,ready_deadline)
  raw,fds=recv_monitored(control,4,ready_deadline,0,b"WAIT_BEGIN",b"NONE",b"NONE");need(fds==())
  if raw.startswith(b"V12_REFUSE_PREBEGIN|"):
   refusal_session(control,context,raw,b"V12_REFUSE_PREBEGIN");return
  begin=parse_packet(raw,b"V12_CONSUME_BEGIN",(b"state",b"ordinal",b"probe",b"auth_id",b"a_begin_state",b"a_arm_state",b"consume_origin_ns",b"consume_deadline_ns"),received_binding(raw,b"WAIT_BEGIN",b"NONE",b"NONE",b"consume_deadline_ns",ready_deadline))
  need(begin[b"state"]==b"CONSUME_BEGIN" and begin[b"ordinal"]==begin[b"probe"]==b"NONE" and begin[b"auth_id"]==AUTH)
  need(begin[b"a_begin_state"]==b"BEGIN_SEND_EFFECT_UNKNOWN" and begin[b"a_arm_state"]==b"ARM_NOT_OBSERVED")
  origin=udec(begin[b"consume_origin_ns"],1);deadline=udec(begin[b"consume_deadline_ns"],1)
  need(deadline==origin+CONSUMPTION_NS and time.monotonic_ns()<=deadline);checkpoint(CERT,horizon_needed(deadline,PRE_STAGE_REMAIN_NS),deadline)
  context[b"begin_observed"]=True;context[b"consume_origin"]=origin;context[b"consume_deadline"]=deadline
  need(time.monotonic_ns()<=deadline-REFUSAL_TOTAL_NS)
  context[b"consumption_state"]=b"ARM_SEND_EFFECT_UNKNOWN";context[b"arm_effect_possible"]=True;context[b"send_state"]=b"ARM_SEND_EFFECT_UNKNOWN"
  armed=packet(b"V12_CONSUME_ARMED",((b"state",b"CONSUME_ARMED"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH),(b"a_begin_state",b"BEGIN_SEND_EFFECT_UNKNOWN"),(b"b_arm_state",b"ARM_SEND_EFFECT_UNKNOWN"),(b"consume_origin_ns",str(origin).encode()),(b"consume_deadline_ns",str(deadline).encode())))
  send_exact(control,armed,deadline);context[b"consumption_state"]=b"ARM_SENT";context[b"send_state"]=b"ARM_SENT"
  try:
   raw,fds=recv_monitored(control,4,deadline,0,b"WAIT_COMMIT",b"NONE",b"NONE");need(fds==())
   if raw.startswith(b"V12_REFUSE_POSTARM|"):
    refusal_session(control,context,raw,b"V12_REFUSE_POSTARM");return
   commit=parse_packet(raw,b"V12_CONSUME_COMMIT",(b"state",b"ordinal",b"probe",b"auth_id",b"a_begin_state",b"a_arm_state",b"a_commit_state",b"consume_origin_ns",b"consume_deadline_ns"),receiver_binding(b"WAIT_COMMIT",b"NONE",b"NONE",deadline))
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
  consumed=packet(b"V12_CONSUMED_DURABLE",((b"state",b"CONSUMED_DURABLE"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"auth_id",AUTH),(b"intent_sha256",intent_sha),(b"consume_origin_ns",str(origin).encode()),(b"consume_deadline_ns",str(deadline).encode()),(b"attempt_fd_state",context[b"local_fd_state"])))
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
  preterminal_arrival_deadline=context[b"origin"]+TOTAL_NS;raw,fds=recv_monitored(control,4,preterminal_arrival_deadline,0,b"WAIT_EMPTY_QUERY",b"NONE",b"NONE");need(fds==())
  query=parse_packet(raw,b"V12_EMPTY_FINAL_QUERY",(b"state",b"ordinal",b"probe",b"chain_head_sha256",b"remove_origin_ns",b"remove_deadline_ns"),received_binding(raw,b"WAIT_EMPTY_QUERY",b"NONE",b"NONE",b"remove_deadline_ns",preterminal_arrival_deadline+REPORT_NS))
  remove_origin=udec(query[b"remove_origin_ns"],1);remove_deadline=udec(query[b"remove_deadline_ns"],1)
  need(query[b"state"]==b"EMPTY_FINAL_QUERY" and query[b"ordinal"]==query[b"probe"]==b"NONE" and query[b"chain_head_sha256"]==context[b"actor_known_chain_sha"])
  need(remove_deadline==remove_origin+REPORT_NS and remove_origin<=time.monotonic_ns()<=remove_deadline)
  checkpoint(CERT,horizon_needed(remove_deadline,FINAL_TOTAL_NS),remove_deadline);need(observe_population(context) is False)
  confirmed=packet(b"V12_EMPTY_FINAL_CONFIRMED",((b"state",b"EMPTY_FINAL_CONFIRMED"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"chain_head_sha256",context[b"chain_sha"]),(b"remove_deadline_ns",str(remove_deadline).encode())))
  send_exact(control,confirmed,remove_deadline)
  raw,fds=recv_monitored(control,4,remove_deadline,0,b"WAIT_REMOVED",b"NONE",b"NONE");need(fds==())
  removed=parse_packet(raw,b"V12_CGROUP_REMOVED",(b"state",b"ordinal",b"probe",b"chain_head_sha256",b"remove_deadline_ns"),receiver_binding(b"WAIT_REMOVED",b"NONE",b"NONE",remove_deadline))
  need(removed[b"state"]==b"CGROUP_REMOVED" and removed[b"ordinal"]==removed[b"probe"]==b"NONE" and removed[b"chain_head_sha256"]==context[b"chain_sha"] and udec(removed[b"remove_deadline_ns"])==remove_deadline)
  try:os.stat(AUTH,dir_fd=6,follow_symlinks=False);need(False)
  except FileNotFoundError:pass
  context[b"removed"]=True;checkpoint(CERT,horizon_needed(remove_deadline,FINAL_TOTAL_NS),remove_deadline)
  ack=packet(b"V12_REMOVE_ACK",((b"state",b"REMOVE_ACK"),(b"ordinal",b"NONE"),(b"probe",b"NONE"),(b"chain_head_sha256",context[b"chain_sha"]),(b"remove_deadline_ns",str(remove_deadline).encode())))
  send_exact(control,ack,remove_deadline)
  raw,fds=recv_monitored(control,4,remove_deadline,0,b"WAIT_FINALIZE",b"NONE",b"NONE");need(fds==())
  finalize=parse_packet(raw,b"V12_FINALIZE_CANDIDATE",(b"state",b"ordinal",b"probe",b"chain_head_sha256",b"terminal_origin_ns",b"terminal_deadline_ns",b"terminal_schedule_hex",b"candidate_deadline_ns"),received_binding(raw,b"WAIT_FINALIZE",b"NONE",b"NONE",b"candidate_deadline_ns",remove_deadline+FINAL_TOTAL_NS))
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
   close_probe(context)
   close_numbers(tuple(context.get(key,-1) for key in (b"root_events_fd",b"root_kill_fd",b"cgfd",b"cgroup_base_fd",b"stage_fd",b"attempt",b"attempt_base_fd") if context.get(key,-1)>=0))
   for endpoint in (control,transfer_control):
    if endpoint is not None:
     try:endpoint.close()
     except BaseException:pass

try:
 main()
except BaseException:
 raise SystemExit(96)
raise SystemExit(0)
P27 RUNNER V12 WATCHDOG SOURCE END F5C2189D
## 19. Exact raw-span census

Outer and inner delimiter lines are unique exact full lines. No delimiter is repeated as a full line; source literals that name an extraction boundary are not delimiter lines.

- Actor begin delimiter: line 244.
- Actor raw bytes: lines 245 through 1936 inclusive; 144471 bytes; 1692 LF; SHA256 bf2e61290cae71f5191b73331d342cd29ae7577efc4f759ffd8021554a218202.
- Actor end delimiter: line 1937.
- Embedded-validator begin delimiter inside actor: line 966.
- Embedded-validator raw bytes: lines 967 through 1068 inclusive; 10195 bytes; 102 LF; SHA256 7414e09dcdd09463f900a24dc19af9d3ecc9528c44895541fba7739fd7af9a89.
- Embedded-validator end delimiter: line 1069.
- Watchdog begin delimiter: line 1939.
- Watchdog raw bytes: lines 1940 through 4981 inclusive; 274030 bytes; 3042 LF; SHA256 204f9b1aee30c301635fb459356c62778bfaa51f736425890c6ec3fc20299dd7.
- Watchdog end delimiter: line 4982.

Each raw span ends with LF and contains only LF or printable ASCII bytes. The two outer spans are separated by exactly one blank line. Raw extraction excludes the delimiter lines and preserves every byte between them. A future extractor must require exactly one begin, exactly one later end, exact adjacency semantics, the identities above, and no trailing or alternate match.

## 20. Frozen source and callsite closure census

This census is raw textual evidence only. It is not a parse, compile, validator run, or executability claim.

- Actor top-level function-definition lines: 123; duplicate definition names: 0.
- Watchdog top-level function-definition lines: 201; duplicate definition names: 0.
- CERT_KEYS: 192 literal keys on each side; the two literal tuples are identical.
- Detached context fields: 15; final envelope fields: 21; reservation TBS fields: 10; final reservation fields: 13.
- CONTROL_SPEC rows: 40 on each side; every literal row occurs once per side and the two tables are identical.
- Domain constants: 12 on each side, including the explicit envelope-TBS, external-acceptance, and issuer-key-bind domains; the two literal sets are identical. The complete 13-line domain-plus-EMPTY_SHA block is 776 bytes/13 LF/SHA256 73be9b6207975cea482a15729236e9a5dbbcc96b38bd9dca9c9c42d27304ce28 on each side, and EMPTY_SHA has its canonical value exactly once per span.
- EXTERNAL_RIGHTS_TYPES: 12 comma-separated types on each side; the literal values are identical and include ATTEMPT_BASE_DIRFD and PENDING_EXPECTED_RAW_FD.
- RELEASE_RECORD_OFFSET_NS is defined as 800000000 in both spans and occurs actor 2/watchdog 3 times; RELEASE_REPLY_OFFSET_NS is defined as 900000000 in both spans and occurs actor 2/watchdog 2 times.
- Suite slots: 15, with one P01D immediately followed by one P01C.
- FAULT_ORDER entries: 55 on each side.
- Terminal phase ceilings: 13 on each side and total exactly 2510000000 ns. Refusal phase ceilings: 12 on each side, with finality at 80000000 ns, closure at 210000000 ns, and an exact 130000000 ns positive tail. The watchdog-only generic-transfer schedule has 7 positive phases totaling 240000000 ns.
- Candidate fields: 26.
- Final report fields: 34.
- Exact standalone packet identifier occurrences, definition included: actor 21; watchdog 22.
- parse_packet literal name occurrences, definition included: actor 25; watchdog 18.
- Actor recv_result/send_abort/parse_abort occurrences, definitions included: 2/5/3; watchdog send_result/set_actor_receive/request_release_disable/validated_exchange/parse_abort occurrences: 2/11/2/2/3.
- Watchdog validate_report_union occurrences, definition included: 3, exactly one constructor call and one parser call.
- Watchdog validate_report_constructor_context/parse_final_report/durable_prevalidated_report occurrences, definitions included: 2/3/3. The two parse_final_report calls in durable_prevalidated_report are respectively the mandatory pre-durability validation and equality-only post-write recheck; its other two occurrences are the failure and success callsites.
- Watchdog durable_once occurrences, definition included: 13.
- Watchdog chained_record occurrences, definition included: 7; neither final-report path uses it.
- Watchdog failure_report occurrences, definition included: 2.
- Watchdog success_report_and_pass occurrences, definition included: 2.
- Watchdog committed_seen_record occurrences, definition included: 2.
- Watchdog ack_receipt_record occurrences, definition included: 3.
- Watchdog reconciliation_record occurrences, definition included: 3.
- Watchdog owner_closure_record occurrences, definition included: 3.
- Watchdog external_transfer occurrences, definition included: 2.
- Watchdog kill_once occurrences, definition included: 3.
- Watchdog consume_attempt occurrences, definition included: 3.
- Watchdog refusal_session occurrences, definition included: 3.
- Watchdog ambiguous_consumption occurrences, definition included: 7; refusal paths are textually disjoint and never call it after REFUSAL_CLOSED_NO_CONSUME.
- Watchdog prepare_first_intent_draft/construct_pending_expected_raw_carrier_before_reservation/activate_record_reservation_after_carrier/freeze_record_reservation/reconcile_pending_record/resolve_pending_before_successor occurrences, definitions included: 2/2/2/3/2/2; next_record/commit_record_reservation occurrences: 10/3.
- RECORD_DELTA_KINDS has 17 literal kinds; apply_record_delta has 17 corresponding explicit kind branches. semantic_delta_bytes/apply_record_delta occurrences, definitions included: 10/2.
- Watchdog pending_transfer_manifest/verify_external_acceptance/external_send/external_recv_receipt occurrences, definitions included: 2/3/3/3.
- Watchdog reserve_packet/activate_reserved_packet/reserve_external_packet/activate_reserved_external_packet occurrences, definitions included: 3/3/3/3. refusal_slot_pack/refusal_slot/refusal_lock_invariant/stage_refusal_slot/refusal_slot_update/refusal_slot_transition/refusal_schedule_from_core/refusal_stage_window occurrences are 4/33/15/2/6/6/6/9.
- Refusal candidate/finality helper occurrences, definitions included: refusal_candidate_fault/refusal_candidate_fault_digest/parse_refusal_receipt_candidate/commit_refusal_receipt/receive_refusal_candidate_once/finalize_refusal_actor_loss/finalize_refusal_cap_hold/refusal_receipt_final/refusal_offer_eligible/await_refusal_finality are 6/4/2/2/4/3/5/4/11/3.
- Refusal closure/driver helper occurrences, definitions included: refusal_receipt_contract/materialize_cached_refusal_offer/refusal_acceptance_hold/drive_cached_refusal_offer/refusal_closure_hold/complete_refusal_closure/issuer_refusal_close/note_locked_refusal_error/route_locked_refusal/read_late_refusal_candidate/owner_poll/external_transfer/transfer_or_hold/refusal_session are 2/2/3/3/4/4/2/3/2/3/9/2/29/3. Generic transfer_schedule_from_cache/transfer_stage_window/generic_transfer_hold/complete_generic_transfer_closure occurrences are 3/7/5/3. REFUSAL_CLOSE_OFFER and generic TRANSFER_OFFER each have one construction site and one possible-send site; the sole true refusal-lock write is the same update that installs the non-null cache.
- Refusal helper definition arities, read directly from the 32 unique definition headers, are: refusal_slot_pack/refusal_slot/refusal_lock_invariant/stage_refusal_slot/refusal_slot_update/refusal_slot_transition/refusal_schedule_from_core/refusal_stage_window = 12/1/1/5/12/12/1/2; refusal_candidate_fault/refusal_candidate_fault_digest/parse_refusal_receipt_candidate/commit_refusal_receipt/receive_refusal_candidate_once/finalize_refusal_actor_loss/finalize_refusal_cap_hold/refusal_receipt_final/refusal_offer_eligible/await_refusal_finality = 3/1/2/3/2/1/1/1/1/2; refusal_receipt_contract/materialize_cached_refusal_offer/refusal_acceptance_hold/drive_cached_refusal_offer/refusal_closure_hold/complete_refusal_closure/issuer_refusal_close/note_locked_refusal_error/route_locked_refusal/read_late_refusal_candidate/owner_poll/external_transfer/transfer_or_hold/refusal_session = 1/1/2/1/2/2/1/3/3/2/3/3/4/4. Generic transfer_schedule_from_cache/transfer_stage_window/generic_transfer_hold/complete_generic_transfer_closure are 1/2/2/1; external_recv_receipt and verify_external_acceptance are 5 and 10.
- owner_poll has one definition and eight direct callsites. Its 68-line raw body has two one-space `if locked:` guards, one two-space locked `if amask:`, one two-space locked return, and one later one-space unlocked `if amask:`. The unlocked actor branch verifies the pidfd identity and marks actor loss before control POLLIN parsing; its tail has zero finality_deadline, refusal-finality-timeout, refusal-offer, or locked-only references and two mark_actor_pidfd_lost callsites including the receive exception. Locked POLLIN precedes HUP/EOF draining, finality resolution, and return.
- The eight owner_poll callers use only finite absolute phase/cleanup/recovery/margin cutoffs or the explicit 50000000 ns post-final hold cutoff. Known actor/control loss descriptors are not re-registered, and poll waits retain a positive one-millisecond floor, so persistent settled holds do not zero-spin while capabilities remain retained.
- Only an OPEN refusal finality is clamped or transitioned to FINALITY_CAP_EXPIRED_HOLD. Settled receipt/loss/cap finality is polled under the caller cutoff without rewriting finality, eligibility, offer identity, acceptance hold, or closure-hold reason. Empty drained recvmsg is recognized before the finality checkpoint; post-cutoff nonempty packets remain bounded non-authoritative evidence.
- RefusalFinalityPending is caught before broad exception handling, is a strict no-op in note_locked_refusal_error, and enters the four-argument transfer_or_hold path with record_fault false and its exact exception reason. recovery_record has arity two and one callsite; after all owner polling it derives actor_lost from current actor_state immediately before direct_reap_value and requires the durable PIDFD_ACTOR_LOST fault classification to agree.
- The ACK-before-close textual order has one ACK_NOT_CONSTRUCTED assertion, one ACK_CACHED_PRE_CLOSE transition, then the sole CLOSE_EFFECT_UNKNOWN transition and sole close_no_consume call, followed by the sole refusal-ACK activation. The temporary receipt parser has no receive-sequence assignment; the sole refusal-specific CONTROL_RECV_SEQ assignment is the tuple commit beside authoritative receipt installation. The sole refusal-offer installation is finality-gated and preceded by a fresh offer-build checkpoint. The frozen slot digest is rechecked before the sole refusal external receive-sequence commit. Every refusal closure phase has one latest-safe-start/reserve-after derivation, and direct locked-path owner release occurs only in complete_refusal_closure after capability closure.

The frozen sources contain no Runner V4 token, no lowercase runner-v4 token, no legacy REFUSED_NOT_ARMED token, no legacy REFUSED_POST_ARM token, and no author-stop terminal for an earlier runtime-plan version. Sections 2, 19, and 20 retain no superseded V11 Runner source identity, boundary, definition count, helper name, or callsite count; the separately named normative Host Probe V8 digest remains intentional. All certificate domain constants, envelope/reservation layouts, common control fields, transition rows, phase tables, suite order, source identities, snapshot identities, V15 identities, and external-manifest rights agree across the two source spans.

Source/prose responsibility is exact: the sources implement only the in-process protocol after authenticated entry; Sections 3, 4, 15, 16, and 17 retain issuer, gate, launcher, external-owner, reconciliation, review, manifest, and execution authority outside the source. No literal source field turns an unresolved external premise into evidence.

## 21. Author-stop boundary

The complete-file byte count, LF count, SHA256, stat identity, strict byte class, final LF, delimiter uniqueness, and terminal uniqueness are reported externally after the terminal is appended. They are not embedded as a self-hash, because a whole-file self-hash would be cyclic.

The final line is an author-stop marker only. It grants no manifest mutation, formal-review result, test, validator, build, evidence creation, reservation consumption, retry, probe, or execution authority.

BATCH07_P27_E001_SUPERVISOR_HOST_RUNTIME_PLAN_RECOVERY_V12_AUTHOR_STOP
