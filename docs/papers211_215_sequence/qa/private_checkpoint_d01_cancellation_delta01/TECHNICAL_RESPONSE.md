# Technical response to D01-F01

2026-09-09 UTC. CORRECTION_PROPOSED / SAME_REVIEWER_ACCEPTANCE_PENDING.
Author: /root/round211_finite_matching_scout. The original Major/open finding
and its frozen source/audit remain unchanged. This is my correction proposal,
not an independent opinion, executed cancellation test or diagnostic grant.

## Exact inherited input and correction

The original fully read source is 327 lines / 17,513 bytes, SHA256
b1b39b9ce36f9c7ace171229c6e69ba236e888bf2664e81eab9d557fd69468ce.
The new whole source is 347 lines / 18,364 bytes, SHA256
fa765db377179ad10770fa981f93b6fcc76e1adc49f79825d1631c90b5e29d96.

The actual native EXACT_DELTA.patch has four hunks: SELF relocates to this
new packet; the remaining three hunks change only capture. All imports,
fixed argv/environment/budget/historical role constants, file/grant helpers,
the entire owned_signal ownership predicate, main and the entry point are
otherwise byte-identical. The preceding 345-line author draft and its actual
read/diff are retained in NATIVE_READS.json as pre-refinement, not final input.
The final two added private cursor observations were followed by another
complete source read and actual whole old/new diff.

D01-F01's trace is valid: the old catch could receive KeyboardInterrupt
outside communicate after proc and origin existed, set failure, then reach
only poll and pipe close. Python documents that such exceptions can interrupt
ordinary execution outside the selected inner try. This supports the finding,
not an installed-interpreter attestation.
[Python 3.10 signal semantics](https://docs.python.org/3.10/library/signal.html#note-on-signal-handlers-and-exceptions).

## One handler and persistent progress

The original four-phase body is now the nested handle_remaining function.
Its same closure retains proc, origin, stdout, stderr, phase_index, signal
claims and native events. Initial execution calls it once. The outer catch
first permanently sets cancellation/failure and records the original private
traceback; when both proc and origin are established it re-enters this exact
handler before the existing finally closes pipe objects. It does not spawn,
reset a deadline, reconstruct a child, clear buffers or invent success.

The cursor advances only after an exhausted phase or completed communication.
A first exception between clock checks, remaining-time calculation, event
recording or cursor advancement therefore returns to the current unconsumed
phase or the already advanced next phase. It never starts the normal budget
again. The unchanged absolute limits are origin+14, +17, +19 and +20, with
remaining time recomputed against the same origin. Normal timeouts still
preserve cumulative TimeoutExpired bytes and proceed through the same phases.
A completed communication sets the cursor to the terminal value 4.

Before dispatching TERM or KILL, the handler records a conservative phase
claim. Re-entry never dispatches a claimed phase again. The unchanged
owned_signal function still requires an unreaped direct child and observed
pid=pgid=sid before killpg. A claim is not proof that a signal was delivered:
interruption after reservation but before the call or its event append can
leave an ambiguous attempt. It is retained as ambiguous, not replayed.
Later still-available phases proceed; no process search or group inference
from a reaped leader is introduced.

| First caught exception location | Source-level recovery |
|---|---|
| After origin acquisition, before first handler call | Cursor remains 0; the original native envelope is entered. |
| Normal clock check or remaining-time calculation | Re-enters the same cursor; uses only time left before the original +14 deadline, then later phases if needed. |
| During a claimed TERM/KILL phase | Retains claim and existing signal events; does not redispatch that signal, but resumes bounded communication and later phases. |
| After TimeoutExpired, around cursor advancement | Cursor is either the exhausted phase or its successor; an exhausted deadline cannot obtain new time. |
| After communication already completed | Preserves bytes/EOF; any exception still permanently prevents success. |

Recovery-entry cursor and, if reached, final cursor are written to the private
native object. A second failure during recovery records its private traceback
and unclosed cursor. It cannot make native_closed_success true because the
first exception already set cancelled_or_exception. The demonstrated repair
covers the review's single caught exception after valid proc/origin; it does
not promise survival through repeated cancellation or broken ordinary APIs.

## Unchanged bounds and authority

The original CONTRACT.md remains the inherited contract except for this new
source identity and the corrected caught-post-spawn flow described above.
This correction does not strengthen it into atomic Popen/origin acquisition,
SIGKILL handling, an arbitrary-output/RAM limit, a hard whole-launch SLA,
hostile-race proof or ELF/NSS/import/observer provenance chain. The ordinary
trusted bootstrap, small-banner capture and filesystem/scheduling limitations
remain. A remaining-budget or ownership failure stays failure/unclosed.

The command is still exactly ['/usr/bin/ssh', '-V']; no target, D02, Git action,
extra observation, changed ENV5 role, diagnostic retry or successor exists.
Raw output/environment/failure details still stay private. The grant format,
fifteen keys, old historical binary keys, private path constraints, endpoint
checks and root-only receipt obligations are unchanged.

The old disabled grant/prospective request still identify the rejected old
source. They are archival format references, not selections for this delta.
Any later root grant and outer request must freshly name this new source path
and full SHA256 after the same independent reviewer has accepted the actual
delta and root has received it. No new operative grant or private value was
created here. D01-F01 remains independently open pending that decision.
