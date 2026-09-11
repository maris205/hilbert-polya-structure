# Independent D01 source audit 01

2026-09-09 UTC. **SOURCE_CHANGE_REQUIRED / ONE_BLOCKING_SOURCE_FINDING**.
D01 and D02 remain disabled; HOLD_OPERATIONAL / HOLD_EXTERNAL.

The exact proposed launcher is not recommended for a diagnostic grant yet.
One caught post-spawn cancellation path bypasses the remaining owned-child
handling. It correctly prevents success; this is not a false-success finding
and no runtime incident was observed. A narrowly scoped successor source is
needed, preserving this original packet and review.

## Independence and exact intake

Reviewer: /root/round211_functional_surgery_residual/fresh08_shift_source.
I have authored or repaired no D01 launcher, proposal or protocol. My earlier
finite-system compression source contribution is unrelated. The new launcher
author is /root/round211_finite_matching_scout. My parent authored an older D01
plan and was excluded from this audit's substance. Root assigned this review
directly; no part was delegated to that parent. An accidentally delivered P213
bibliography assignment was declined without P213 reading, searching or writing.

The project research skill and linked WORKFLOW were read in full. They required
source-first reception, explicit independence and preservation, not execution.
The current recovery/batch orientation was read only to establish this task's
scope: P213 retained, three retained / one complete / two open / 50 closed;
neither this audit nor the historical diagnostic documents changes that count.

The entire input packet has 13 payloads / 14 files / 159,985 bytes.
Its nonself SHA256SUMS hash is
bc61e43e136281c0ea4e55809d26d0e34e92a9e88dd6bd4d1a06e1157e5d82ee.
The fully read launch.py is 327 lines / 17,513 bytes, SHA256
b1b39b9ce36f9c7ace171229c6e69ba236e888bf2664e81eab9d557fd69468ce.

## Finding D01-F01 — caught cancellation can abandon the owned child

Severity: Major / blocking source correction. Location: launch.py 160–171
and 194–203; interaction with the catches at 156–159 and 179–189.

A concrete source-level trace suffices, without running or instrumenting code:

1. Popen has returned; proc, native pid and origin have all been assigned.
   The same direct child is still running, with time remaining before origin+20.
2. One KeyboardInterrupt occurs while evaluating the loop's outer deadline
   check at line 162 or remaining-time calculation at line 167, outside the
   communicate try suite that starts at line 172.
3. The outer catch at lines 194–198 marks failure and polls the child. It does
   not call owned_signal or resume any remaining communication phase.
4. The finally suite only closes the pipe objects. There is no owned TERM,
   KILL or remaining drain attempt. The function can return with returncode
   None and pipes_eof false while the previously owned child is still alive.

This follows the documented Python signal-exception model: a default SIGINT
may produce KeyboardInterrupt at an arbitrary Python instruction, not only
inside communicate. No hostile interpreter or special monkeypatch is needed.
[Python 3.10 signal semantics](https://docs.python.org/3.10/library/signal.html#note-on-signal-handlers-and-exceptions).

The finding concerns a single exception which the launcher **catches**, after
proc and origin are already valid. It does not require atomic Popen startup,
a response to SIGKILL, guaranteed handling through repeated cancellation,
a hard whole-launch SLA, continuous identity tracing, or a new observer.
The contract's allowance for unhandled outer termination and partial
filesystem evidence does not describe this caught, still-running-controller
path. Nor does correctly setting failure replace the promised bounded
owned-child handling. Closing local pipe readers is not proof of child exit.

The normal timeout path and the explicit SPAWN-write-failure catch do enter
the finite phase loop. The defect is the other caught post-spawn path.
All success flags stay false in the demonstrated trace; no root acceptance,
D02 or checkpoint successor is created.

### Minimal exact repair boundary

Make a new source revision, not an edit of the frozen preparation01 packet.
Change the capture control-flow boundary around lines 150–203 so a caught
post-spawn failure with a valid proc and established origin reaches the same
finite owned-child cleanup/communication path **before** closing its pipes.
Keep explicit phase progress so TERM/KILL are attempted at most once and
already consumed time is not reset. Reuse the same absolute deadlines
origin+14, +17, +19 and +20 and the existing live-direct-child / pid=pgid=sid
ownership predicate. Preserve accumulated raw data, failure flags and actual
signal/wait outcomes. If ownership, remaining budget or completion cannot be
established, retain failure/unclosed rather than inventing closure.

A new unbounded wait, direct broad kill, process search, restarted 20-second
budget, additional child, runtime probe or diagnostic retry is not a repair.
This review supplies a correction requirement, not an authored replacement
implementation. Root must receive the whole new source/hash and changed
control flow independently before considering a separate D01 grant.

## Remaining reviewed boundaries

| Boundary | Source-level conclusion |
|---|---|
| Direct child | Exactly ['/usr/bin/ssh', '-V']; shell=False, EOF stdin, binary stdout/stderr, close_fds and a new session. No target, D02 or Git branch. |
| Environment | Only genuine present ENV5 values, preserving absences, plus fixed PATH/LANG/LC_ALL/TZ; equality to the private root selection before and after. No invented private value. |
| Grant | Exact external hash, constrained token/path, fifteen top-level keys, duplicate JSON-key refusal, enabled/trust/diagnostic checks and exact source/argv/budget. Disabled template cannot select a run. |
| Receipt references | Shape-checked and recorded, deliberately not followed or self-certified. Genuine source/runtime receipt selection remains root's obligation. |
| Private evidence | Exclusive new 0700 directory under checked private parent; exclusive directory-relative 0600 files; raw files and ATTEMPT precede spawning; no old output reuse or overwrite. |
| Finite input keys | Source, grant, SSH and resolved Python whole reads, lexical/opened/end checks and same-descriptor endpoint rereads; separate exact python3 alias; historical content/OID/mode plus complete selected ten-field metadata. |
| Ordinary timeout path | Finite absolute normal/TERM/KILL/drain deadlines and owned-session predicate are present. D01-F01 is the cancellation bypass, not a claim that timeout handling is absent. |
| Success and authority | Requires zero return code, EOF, no timeout/cancellation/exception and endpoint equality. Only native-closed/root-reception-pending; outer acceptance remains false and successors disabled. |
| Privacy | Environment map, output and failure traceback remain private. Public success/failure exposes only safe status, keys/counts; no new secret export was found. |

Published subprocess semantics support the binary communication, finite
timeout, output-resumption and new-session interpretation. communicate can
buffer output in memory; the small-banner assumption is therefore a real
declared premise, not an independently established byte or RAM bound.
[Python 3.10 subprocess](https://docs.python.org/3.10/library/subprocess.html#subprocess.Popen.communicate).
These are public API semantics, not installed-vendor correspondence.

The ordinary trusted product/shell/Python bootstrap, imports, filesystem,
kernel and tool premises remain accepted review limits. Internal checks occur
after imports and do not attest startup closure or hostile concurrency.
The public OpenSSH 8.9 discussion in the accepted prior package is not evidence
of the installed executable's option semantics. A future version banner would
not establish such correspondence either. Missing evidence is not a pass.

## Documentary evidence and exact read scope

All thirteen input payloads and the seal were read as data. launch.py,
CONTRACT and HANDOFF were read completely. SOURCE_READS_NATIVE,
INPUT_CHECKS_NATIVE and CLOSING_NATIVE were read completely; the ten complete
DOCUMENT_READS_NATIVE records were displayed in nonoverlapping 0–2, 3–5 and
6–9 groups, each bound to its whole 70,170-byte file key.

The complete accepted executor_ssh_root04 RECEPTION, delta04 SOURCE_CONTRACT
and audit04 REPORT were directly read. The archival native bodies additionally
contain the relevant older command/runtime protocol, disabled proposals,
historical role records and observer source/root receipts. Their recorded
commands were not executed. Other author input-pin files were whole-byte/key
dependencies only, not blanket rereviews of their historical packages.

INPUT_BEFORE_NATIVE (chunk e5d6b4) and INPUT_AFTER_NATIVE (chunk b94aa5) are
actual successful documentary inventories. They verify exact 14-file input
membership, all 13 payload hashes, root's expected source/seal/counts, all 14
historical input pins and four explicit contextual keys. All 31 distinct
whole-file non-atime keys are identical at the two inventory endpoints.
The first inventory followed initial orientation/core reads; no claim is made
that it preceded every preliminary read.

VERIFICATION_NATIVE records actual chunk ec3160, exit 0: 273 documentary
checks over those 31 complete inputs, a fresh complete-key reread, 30 exact
author/reviewer sed-output equalities and all ten archival-record selections.
This is documentary equality, not source execution or a technical PASS.
Nonsed and out-of-pinned-scope records are expressly listed as unclaimed slice
equalities rather than replayed. Commands embedded in outputs are inert data.

DOCUMENTARY_NATIVE retains 23 actual selected requests and full return objects;
SOURCE_NATIVE_REREAD preserves the separate full source-native read at chunk
8b8a36. PRIMARY_NATIVE retains actual independent public Python requests.
The author's PRIMARY_REQUESTS is an authored source-use account, not a raw
web transcript; it was not promoted into one.

Some combined orchestration displays were clipped. Complete underlying
command return objects remain attached; substantive bodies were separately
reread as stated. Two successful structural lookups initially used the wrong
result-property spelling, yielding null summary fields; those lookups are
retained and were superseded by complete exact archival record display.
No failed operational run exists because none was authorized or attempted.

Only this new audit directory was written. No launcher import, AST/syntax
parse, test or execution; no SSH/Git command; no private original, environment,
configuration, tool-binary, runtime, host or agent observation; no science,
paper, central index, historical packet, setting or external release change.

## Root handoff

Finding census: Critical 0 / Major 1 / Minor 0. D01-F01 remains open.
The packet's complete nonself SHA256SUMS covers every other file in this
directory. Root should preserve this rejected source-boundary result,
receive a narrowly revised source and then make any later diagnostic decision
separately. This review grants no diagnostic or checkpoint operation.
