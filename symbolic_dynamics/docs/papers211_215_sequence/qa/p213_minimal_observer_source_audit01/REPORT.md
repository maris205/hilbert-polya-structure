# P213 minimal observer/capture — independent source-only audit

Verdict: HOLD_SOURCE_TWO_OPEN_FINDINGS_BINDING_UNRESOLVED.
Finding census: 0 Critical, 2 Major/open, 0 Minor; none closed.
2026-09-10 UTC. Reviewer: /root/round211_finite_matching_scout.

This is an independent review of the exact disabled algorithm and capture
proposal, not a probe, a completed binding, runtime acceptance, scientific
source/parameter reopening, manuscript review or paper/batch completion.

## Exact object and independence

The complete observer is 438 lines/21,437 bytes, SHA-256
97198b16d87c504a2574a773133f8a4574d01f1751d810146b1237bb6359e65b.
The complete capture is 40 lines/1,734 bytes, SHA-256
1591b239781196ef8e31db64f17cfe51d3c707d1297f6756f0d072acb8aec1d2.
Their frozen [source packet](../p213_minimal_observer_source01/HANDOFF.md)
has exactly 23 payloads/24 files/421,765 bytes and nonself seal
5517fa99464c02c5d21170a133b0f5a6d540f18ca549dd6296503f2fc0d29d55.
Nothing in that packet was edited.

The observer/capture author is /root/round211_functional_surgery_residual.
The design author is its different child fresh08_shift_source. I previously
authored the independent design audit and reviewed P213 scientific-source/
parameter/title evidence; I did not author the design, this implementation,
or P213's mathematical proof/verifier. My design acceptance criteria and
review familiarity are disclosed, not called blind or external review.
No inherited observer/capture implementation contribution was found in the
actual source contract, read scope, seven construction patches and prior
design provenance. The distinct P212 baseline contribution restriction does
not turn this P213 authored implementation into my own source.

The project research skill/workflow required recovery of actual accepted
design evidence, preservation of failure/provenance and reviewer separation.
I read the whole selected instruction files, accepted design receipt,
235-line design and independent report/seven obligations, both whole
programs, CONTRACT, BINDING_FORMAT, both disabled JSON documents, selection
request, handoff/read scope, nine declared input documents and complete
source packet inventory. Early orientation previews are not claimed to be
complete readings of every historical central-index paragraph.

## Findings requiring a new-only source delta

### P213-MOS-F01 — Major/open: validate proc target before following it

[observe.py](../p213_minimal_observer_source01/observe.py) lines 335–345
first save cwd and the own-process cwd/exe links. Line 339 then calls
os.stat("/proc/self/exe") and captures ten fields. The cwd test and exact
interpreter-final-path test occur only at lines 340–342. This helper is used
at the beginning, after all keys and at closing.

os.stat normally follows a symlink, while the proc exe endpoint is a link
to this process's executable. Thus the exact local order follows the target
for metadata before deciding that the observed target is the approved
interpreter target. [Python stat contract](https://docs.python.org/3/library/os.html#os.stat),
[kernel proc endpoint contract](https://www.kernel.org/doc/html/latest/filesystems/proc.html).

This fails the accepted design/CONTRACT promise to reject unknown symlink
targets before a new unapproved explicit path/metadata read. Early map
allowlisting may reject some mismatches first; it does not itself implement
the executable-link comparison or establish that every later proc endpoint
can be followed without checking its role. This finding requests the narrow
ordering guarantee, not hermetic startup or atomic race immunity. I did not
observe an unexpected target or an actual out-of-scope read; this program
is disabled and was not executed.

Required resolution: in a new commissioned copy, retain the observed
readlink/cwd evidence, reject unapproved values before following executable
metadata, then keep all existing complete-key and pointwise comparisons.
Do not broaden the finite frontier, silently weaken the promise or alter
this frozen source. Root and the same reviewer must receive the exact delta.

### P213-MOS-F02 — Major/open: exception class does not identify code origin

At lines 109–113, failure(exc) exports exc.args[0] for every exception whose
exact type is RuntimeError. The helper is called from handlers covering
the observer's own checks and helper/import/file/runtime operations.
The type test does not establish that need() or another reviewed internal
failure site created that particular exception.

A RuntimeError from another covered operation carrying a message will have
that first argument copied into the emitted "code" field. This is a direct
branch implication, not an executed fault-injection test. Exception args
are constructor-supplied associated values, not an internal-code provenance
marker. [Python exception data](https://docs.python.org/3/library/exceptions.html#BaseException.args).

Consequently the source comment and CONTRACT assertion that arbitrary
exception text is not exported are too strong for this implementation.
No actual sensitive value, helper failure or disclosure is asserted.
Empty args would also make this indexing fail, but the accepted design
already disclaims a guaranteed receipt; that is not a new liveness finding.

Required resolution: distinguish observer-owned bounded internal codes from
generic runtime exceptions in the new source. Only reviewed finite codes
and appropriate non-sensitive class/errno information should be emitted;
do not forward arbitrary args merely because their exception class matches.
Retain complete captured failed evidence and the existing no-guaranteed-
receipt boundary. No source implementation change was made in this audit.

## Assessment of the seven accepted obligations

| Obligation | Static source assessment and remaining limit |
|---|---|
| Immutable early facts | Lines 25–86 copy supported scalar/sequence facts into tagged tuples, including tuple subclasses. Completed rows retain no module/spec/loader objects; partial row prefixes are retained separately. Missing and null are distinct. Direct-script null-main classification and qualified class-valued loader handling are present. |
| Concrete launch/trust | Lines 76–86 and 360–373 save/compare launch data and enforce the literal CPython/Linux flags/argv. os.environ is accurately labelled as the cached Python mapping; only match booleans and the two expected literals are emitted. Exact paths, implementation/flag fields, encodings and full expected record remain unresolved. F02 affects failure-text scope. |
| Mechanism/source/cache phases | Early raw maps and second snapshots precede os/hashlib/json imports. Helper/closing rows/maps/deltas stay distinct; removed/changed facts HOLD. Ordinary/direct origins need content keys; caches/eligible matching sources require independent binding review. Nominal frozen filenames do not become executed text automatically. |
| Finite frontier | All file/module/loader/map lists and bounds are literal future binding inputs. Module/map checks precede ordinary file acquisition; all file-backed mappings are included regardless of execute permission. No discovery import/frontier expansion exists. F01 leaves the proc-exe endpoint ordering unresolved. |
| Full keys and absence | Lines 159–232 check declared links/final types; open final files nonblocking/nofollow; fstat before content; hash through EOF on one fd; check byte count and ten exact integer fields at descriptor/path endpoints. Closing rechecks include every named optional path. ENOENT with no link chain is distinct from other errors; late actual content must already have a complete key. F01 concerns the separate process endpoint. |
| Capture and reception | The 40-line proposal gates before allocation; its body uses one nonrecursive exclusive mkdir, private fixed separate files and one foreground env/interpreter invocation. Partial artifacts are retained, no retries/controller/cleanup guarantee exists. Exact request, Bash/env/mkdir/source paths, output budget and one-probe grant remain separate; F02 affects observer failure output. |
| Later science | The observer never parses/imports/executes verify.py and no scientific file role is authorized here. Successful output still says runtime_accepted=false and pending independent reception. Initial science, canonical adoption, strict pair, build/views/rounds/A/B remain separate. |

The module-registry copy avoids dictionary-size iteration problems, but
only the additional scalar copying makes saved facts immutable; it is not
an atomic hostile-runtime snapshot. [Official sys semantics](https://docs.python.org/3/library/sys.html#sys.modules).
Direct source-file execution gives __main__.__spec__=None, and builtin/
frozen importers are class-based; the implementation preserves those cases.
[Direct-main semantics](https://docs.python.org/3/reference/import.html#main-spec),
[loader classes](https://docs.python.org/3/library/importlib.html#importlib.machinery.BuiltinImporter).

The raw maps buffers keep bytes as lossless hex, byte count and EOF before
parsing, including failure prefixes. Map parsing is deliberately restricted
to approved ASCII forms and rejects deleted/unsupported/unapproved entries.
Kernel documentation warns about partial-read races; no startup history,
atomic process map or later scientific-process equivalence is inferred.
[Kernel maps observation limits](https://www.kernel.org/doc/html/latest/filesystems/proc.html).

Same-fd hashing uses one sentinel byte to detect a bound overrun, which the
contract discloses. O_NONBLOCK plus the pre-content regular-file check is
not a hard deadline for filesystem operations. Optional absence records
remain incomplete content keys; only optional eligibility roles can accept
actual absence. Present source/cache candidates are fully read; -B is not
used to infer absence or establish which bytes executed. Ordinary parent
traversal, kernel/CPython and helper-import internals remain trusted.

Capture redirections duplicate fds 3/4 to distinct child stdout/stderr before
closing those extra child fds. Exclusive fresh directory allocation and
trusted ownership, not noclobber on arbitrary preexisting objects, support
the proposed separation. Every native/session return and both full files
must still be received later, including unexpected bytes or failure.
[GNU redirection semantics](https://www.gnu.org/s/bash/manual/html_node/Redirections.html),
[GNU directory creation](https://www.gnu.org/s/coreutils/manual/html_node/mkdir-invocation.html).
Direct GNU opens failed; the preserved narrowed primary GNU search results,
not unrelated incidental search results, supplied these semantic references.

## Binding sufficiency and the smallest honest next preparation

BINDING=None and capture's unconditional exit are intentional safeguards,
not additional findings. The disabled JSON is not consumed by the observer.
I do not accept nonexistent launch paths, numeric bounds, module records,
cache eligibility, symlink targets, file keys, absence facts or a runnable
request by accepting their schema.

The current algorithm requires exact complete phase module-name equality
and every expected eight-field module row (lines 253–257), plus the entire
launch_snapshot record (line 361). The accepted design and nine inputs do
not provide those values. In particular, a selected P211 archival inventory
can suggest finite historical names; it does not establish exact P213
early/helper/closing rows, the new __main__ observer path, complete launch
representation or present state. That archive was not a selected input
read by this audit, and no assertion about its exact contents is made.

The smallest honest immediate deliverable is therefore still a disabled,
source-only proposal with per-field provenance: literal choices made by
root, finite archival name candidates, proposed supported mechanisms/roles,
and justified numeric bounds. Mark unavailable whole-row values unresolved.
Historical guesses or proposed comparison targets must not be labelled
observed facts, and a placeholder cannot be enabled in the current algorithm.

If independent documentary evidence cannot supply justified exact expected
rows, a separately commissioned design/source delta may use reviewed finite
permission allowlists while collecting the full immutable observed rows
for independent reception. It must still check chosen launch invariants,
supported loader/mechanism/path rules, exact approved file/symlink roles,
bounds, early/helper/closing separation and all unknown-path HOLD rules.
It must not simply drop source/cache eligibility, accept arbitrary modules
or backfill missing keys. This is an explicit proposed adjustment of the
exact-comparison contract, not permission inferred from the old design.

Root's later documentary archive selection and source-only proposal are
outside this frozen audit input selection. No host scan, version query,
probe, source change or allocation was performed to make the binding fit.
A new exact source/binding/capture review and one-probe grant remain
necessary, followed by independent complete runtime reception.

## Actual documentary verification, not program execution

CHECK01_NATIVE records native 325ce1: 3,420 checks, 33 complete document
keys, all 23 source payloads/24 physical files and all nine input pins.
The keys include SHA-256, byte length and the ten integer non-atime fields
with descriptor/path endpoint comparisons and a second full document read.
The first key round followed initial textual reading; no claim of keys
taken before the first orientation read or continuous stability is made.
All 19 author-check and 22 author-closing complete historical keys match.

Nineteen archived full-body native returns match current files as raw UTF-8
bytes, totaling 107,836 bytes: nine inputs, seven final source/interfaces,
two author report bodies and one documentary-checker source. Twenty-eight
selected documentary native records total 166,059 output bytes, including
the preserved wrong-filename exit 2. The 898-line/46,256-byte seven-body wc
table is checked against actual newlines/bytes. All seven authored patch
records and their targets, the earlier 20,267-byte observer read, and all
four primary-access request/returns are retained and structurally received.
I do not claim that a text-token check proves Python/Bash semantics or that
the entire older design/audit/root seals were newly reviewed by this packet.

After reading all of its source, I actually ran the existing author
CHECK_DOCUMENTS.cjs as a bounded document/JSON/string checker. Native 728134
returned 2,189 checks, not a Python/observer/capture execution. The raw
comparison and closing evidence are recorded separately below in the
handoff and closing result. The observer/capture were never executed,
syntax-checked, AST-parsed, compiled, imported or used for runtime tests.

The first native-structure display accidentally included large nested
bodies and was truly truncated. STRUCTURE_NATIVE preserves that exact
return and the later compact structural reread; no missing preview was
reconstructed. Full selected bodies are independently covered by the raw
comparisons above. Three direct GNU public-document opens returned errors;
those exact requests/returns remain in PRIMARY_ACCESS. Early combined
orientation previews were also limited; selected skill/workflow/design
instructions and both complete programs were separately read.

## Handoff

Receive this original report and its two open source findings before any
new-only repair. The author may propose a delta; the same independent
reviewer must assess its exact bytes and root must receive the originals.
This is neither source acceptance nor any observation/data-reception grant.
No central index, historic manuscript, accepted review/seal, failed evidence,
runtime setting or program was changed. No host/private/proc/config/env
observation, science/build/view, Git/SSH, external upload or specialist
contact occurred. Root owns batch-first integration. HOLD_EXTERNAL.
