# Same-reviewer D01-F01 cancellation delta acceptance

2026-09-09 UTC. **D01_F01_CLOSED_FOR_EXACT_SOURCE / ROOT_RECEPTION_PENDING**.
SOURCE_ACCEPTABLE_WITH_DECLARED_LIMITS. D01/D02 and checkpoint operations
remain ungranted by this review; HOLD_OPERATIONAL / HOLD_EXTERNAL.

D01-F01 is closed only for the complete 347-line / 18,364-byte launch.py:
SHA256 fa765db377179ad10770fa981f93b6fcc76e1adc49f79825d1631c90b5e29d96.
No new blocking source finding was established. This is source acceptance,
not an executed cancellation test, native-closure result or diagnostic grant.

## Independence, preservation and exact delta

Reviewer: /root/round211_functional_surgery_residual/fresh08_shift_source,
the author of the independent original D01-F01 finding. I proposed the
correction requirement but authored neither D01 implementation. The code
author remains /root/round211_finite_matching_scout. The older-protocol
author parent did not contribute substantive review or repair here.

The old 327-line source, original Major/open report and FINDINGS.json are
unchanged. Their open status remains historically correct. This separate
delta closes that finding only for the full successor key above; it does
not edit, relabel or accept the old source.

The complete author packet is 9 payloads / 10 files / 157,301 bytes, with seal
dbe83bea29b244561b420624064d2771f114ef8354e17d9a6fa179b057a80fc3.
The exact independent native diff (9c01f9, expected exit 1) is 6,356 bytes,
SHA256 a2cbcc47bdd08456724b8b14593bf7503ec2789efb8709ba47a2ef7a16b35478.
It equals both the author's EXACT_DELTA.patch and final archived diff output
fde668, byte for byte. INDEPENDENT_DELTA.patch is the raw independent output,
not a hand-written patch or a source execution.

All four diff hunks have been reviewed. The first changes only SELF to the
new packet. The other three change capture. The complete prefix outside SELF
and the complete main/entry-point suffix are byte-identical to the old source:
imports, direct SSH argv, environment and historical keys, grant and file
helpers, owned_signal predicate, private output and endpoint gates are intact.

## Why the original finding is closed

The original counterexample was one caught cancellation outside communicate,
after proc and origin existed, followed only by poll and pipe close.
New source lines below refer to the exact 347-line successor.

| Invariant | Source-level evidence and conclusion |
|---|---|
| Same-child recovery before pipe close | Lines 204–212 set permanent failure, retain the private traceback and call the same handle_remaining when proc and origin exist; finally closes pipes only afterwards. The original bypass through only poll/close is removed. |
| Persistent phase cursor | Lines 147–149 initialize one cursor and four phases before spawn. Lines 166/183 advance only after an exhausted or timed-out phase; line 174 finishes at 4. Recovery records the current cursor and never assigns it back to zero. |
| No renewed budget | The only acquisition of origin is line 195. Both handler entries use remaining=origin+offset−monotonic at line 162 and the original +20 outer cutoff at line 155; offsets remain +14/+17/+19/+20. An exhausted phase can obtain no new interval. |
| At-most-once signal opportunity | Lines 158–161 claim the named TERM/KILL phase before dispatch; the claim list persists across recovery. A claimed phase is never dispatched again. The unchanged owned_signal still requires an unreaped direct child and observed pid=pgid=sid. |
| Same cumulative capture state | stdout/stderr are nonlocal handler variables, initialized once and never cleared on recovery. Timeout outputs replace them with available cumulative data; a completed communicate supplies the complete streams. |
| Permanent failure and finite recovery | The outer catch sets cancelled_or_exception before recovery. A second recovery failure is separately retained at lines 213–216. Lines 224–225 cannot report success after that first caught exception. There is no automatic third handler entry or extra child. |

For the exact former trace, interrupt the new deadline calculation at line
155 or 162 after valid proc/origin. The outer catch retains failure and
re-enters handle_remaining with the same current phase, time origin, child,
claims, bytes and events. Under the original ordinary API/scheduling premises,
the remaining finite phases are processed before pipe close. That is the
required correction, rather than merely a new failure label.

An interrupt adjacent to cursor advancement leaves either the old phase or
its successor. Both are safe with respect to time: an old exhausted phase
recomputes a nonpositive remaining interval and advances; a successor is
already the next unconsumed phase. If successful communication completed
before the interrupt, EOF/data survive and recovery either returns at cursor
4 or resumes the same already-completed child; failure still cannot clear.

A signal claim is deliberately a reservation, **not proof of delivery**.
An interruption after reservation but before dispatch/event recording leaves
an ambiguous attempt. It will not be repeated. In particular, a reserved but
unconfirmed KILL is not converted into a delivered KILL or successful closure.
Later available phases continue and unknown closure remains failure. This
conservative at-most-once boundary is explicitly disclosed in the technical
response; it is not an at-least-once or exactly-once delivery guarantee.

The bounded inference about cancellation uses the same published Python
signal model already independently read for audit01, not an installed-runtime
observation. The documentation allows signal-raised exceptions at arbitrary
instruction boundaries; it does not make the revised operations atomic.
[Python 3.10 signal exceptions](https://docs.python.org/3.10/library/signal.html#note-on-signal-handlers-and-exceptions).

## Limits and unchanged authority

The acceptance covers the original single caught post-spawn exception with
valid proc and origin. It does not add atomic Popen/origin acquisition,
survival through repeated cancellation or broken APIs, SIGKILL handling,
continuous process/file identity, hostile-race isolation, arbitrary-output
memory bounds, a hard full-launch SLA or an observer-of-observer chain.
If the available budget expires or recovery/ownership remains unknown,
the result remains failed/unclosed. These limits were not silently relaxed.

The original ordinary trusted product/shell/Python/import/platform and
small-banner premises remain. Filesystem writes/fsync, startup and scheduling
are not claimed to fit a hard 20-second whole-launch deadline. The original
finite input/private-output and independent root-reception contract is reused,
with only the new SELF/hash and reviewed capture correction.

The one direct child remains ['/usr/bin/ssh', '-V'] with EOF input, exact
ENV5-plus-fixed environment, private raw capture and no target/D02/Git branch.
Public OpenSSH 8.9 source discussion is not installed semantics. A later
version banner cannot certify vendor-source correspondence, option/default
policy, authentication or absence of all startup effects.

The old disabled grant/prospective request still point to the rejected old
source and cannot select this successor. Root must separately receive this
whole new source and exact delta, select genuine private role/receipt data,
and make any new exact diagnostic request. No operational authority follows
from the source verdict, author packet, signal claims or an eventual exit 0.

## Complete evidence, draft separation and read scope

The project skill and WORKFLOW were read completely again; current STATE
and the linked batch's current tail were orientation only. Their source-first,
changed-dependency and preservation rules kept the review inside this
single correction. No P212/P213 science, manuscript or central index was edited.

All ten author files were read as data, including the complete new source,
TECHNICAL_RESPONSE, HANDOFF, EXACT_DELTA and both full native collections.
The 19 preparation records were displayed in adjacent groups 0–3, 4–10,
11–14 and 15–18; all eight closing records were displayed together.
Each group was bound to the complete input file key. No contained command
was dispatched. The complete old source/contract/report/finding were reread
through their archived actual outputs and checked against the originals.

NATIVE_READS records 10–14 are the earlier draft/diff, not final evidence.
Their adjacent source reads reconstruct 345 lines / 18,241 bytes, SHA256
a462ea8b4ab9c4bc3b271eb3dc21b75af4b81bfc8c4f9aeda7c0ac4cfda1ff6e.
Record 15 is the complete final 347-line source, and 16 its complete final
diff. The two versions are kept distinct; no mixed-source equality is used.
CLOSING_NATIVE record 1 is earlier 1,986-byte handoff wording; record 7 is
the final 2,050-byte handoff. The earlier record remains intact and is excluded
from final-original slice equality.

INPUT_BEFORE_NATIVE (0a9aad) and INPUT_AFTER_NATIVE (37aeb0) both returned 0.
They verify exact 10-file membership, all nine author payload hashes, the
root-selected source/seal and all nine historical input pins. All 19 complete
non-atime keys agree at both endpoints. The first inventory preceded the
substantive new source/native reads, but followed orientation and pin-list reads.

CHECKS_NATIVE records actual bce9ac, exit 0, with 210 documentary checks.
It freshly rereads the 19 complete keys, checks 17 exact author/reviewer sed
outputs, the raw three-way final diff, all five complete archival-record
groups, old-source reconstruction, final-source equality and distinct draft.
It also confirms that the old FINDINGS.json still says open.
Literal source censuses and byte equalities support the manual argument;
they are not compilation, AST interpretation, a test or an executed trace.

READS_NATIVE preserves 24 actual selected requests and complete return objects,
not an exhaustive hidden-product transcript. DIFF_NATIVE, input inventories,
CHECKS_NATIVE and CLOSING_NATIVE preserve their separately identified actual
requests/returns. The author's PRIMARY_REQUESTS explicitly is an authored
public-source-use record; it is not presented as a raw web transcript.
No new independent public retrieval or installed-provenance claim is made here.

One independent documentary reader failed (90d21a, exit 1): it expected the
usual records property, while NATIVE_READS uses
all_preparation_workspace_native_records. The original read_native.cjs and
complete failure diagnostic are preserved. A new read_native02.cjs adapter
accepts exactly the two documented collection fields and checks the same
whole-byte keys; it subsequently read every record successfully. No author
file or original failure was altered to make this pass. The incidental
trusted-helper error output is not used as a runtime or bootstrap receipt.

Only this new audit directory was written with apply_patch. No submitted
source import, AST/syntax/compile/test/execution; no SSH/Git, private-original,
environment/configuration/tool-binary/host/runtime probe; no new grant,
science, manuscript, historical packet, central state or external action.

## Finding census and handoff

Current exact-source open findings: Critical 0 / Major 0 / Minor 0.
D01-F01: closed only for fa765db377179ad10770fa981f93b6fcc76e1adc49f79825d1631c90b5e29d96.
The rejected source and original open record remain unchanged.

The complete nonself SHA256SUMS covers every other file in this new directory,
including the failed documentary helper and its retained failure record.
Root reception and any diagnostic grant remain separate next decisions.
