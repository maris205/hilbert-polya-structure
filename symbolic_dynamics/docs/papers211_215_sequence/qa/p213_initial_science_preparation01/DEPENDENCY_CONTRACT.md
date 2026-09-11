# P213 changed dependency and own-process control contract — proposed only

This is a new disabled source contract, not a runtime acceptance or grant.
Read it with SOURCE_DELTA.md and the exact source/capture/request bytes.

## Finite permissions and immutable observations

The inherited literal retains exactly 62 permitted module names: 26 builtin,
three frozen, 32 file-backed names and one direct-script role. Early allows
23 names; helper/closing each allow the same 62. Required names, qualified
loader identities, exact source/cache/package/origin rules, os.path alias
consistency and all launch/flag/encoding requirements remain unchanged,
except that the direct script and argv/orig_argv now name this new wrapper.
The nine file-map candidates, six special maps and 29 distinct matching
source / 29 nonoptimized cache candidates are unchanged permissions.

The old observer source role is replaced by the exact future wrapper path;
one mandatory no-link regular verify.py scientific_source_exact_bytes role
is added. There are 70 candidates, each lexical=final, links=[], with the
old optional/ENOENT and required startup-zip absence rules. The new science
entry is not a module origin or mapped-file permission. No runtime role is
given to the parameters JSON, output schema, proof, candidate/gate programs,
old raw output or canonical: these are documentary dependencies accepted
externally and never read by the scientific process.

The actual launch and module rows remain immutable copied/tagged data;
no historical row is inserted, predicted inventory substituted, or unknown
name/path inspected to fill an omission. The actual runtime key must be
collected in each new process. Unknown observed modules/maps cause HOLD
at their validation step, with no adaptive path/content investigation.

The reused complete file key is EOF, actual byte count, SHA256, actual
integer st_dev/st_ino/st_mode/st_nlink/st_uid/st_gid/st_rdev/st_size/
st_mtime_ns/st_ctime_ns, one no-follow/nonblocking regular fd, before/after
fstat and endpoint agreement, and successful close. Neither atime nor
birth time is used. Native nanoseconds are not invented precision.
Optional absence requires actual literal-path lstat ENOENT and is never
content-key evidence. Existing matching-source/cache ambiguity and frozen
nominal-filename exclusions remain exactly as in the accepted policy.

## Before/after key and source-load delta

The old observer performed one fixed file pass. This wrapper proposes two,
both in identical binding order: before and after the scientific body.
All present candidates are fully read/hashed on each pass; optional
absences are independently observed. Equality is type-preserving across
the complete before/after records before closing fields are appended.
For later documentary reception, strip only the after-record's additional
closing member when checking that equality; all other members must agree.
Those closing observations must separately equal the respective begin.

A third, special source-only read retains the exact verifier bytes to
compile. load_science keeps partial/failure/close evidence, uses the same
ten-field endpoint/fd protocol, enforces the exact 17,539-byte size and
accepted SHA256, and compares every complete source-load key field to the
first-pass key before returning bytes. The stored bytes are compiled only
after successful close. No earlier archived bytes or cache bytes are
compiled. This change is a new source/collection review obligation.

The source-load read and both full passes share the same 64 MiB total
successful-read limit; inherited per-file limit remains 8 MiB. A failing
sentinel can consume one byte beyond a limit and is retained, without
retry. The science source-load own limit is exactly 17,539 bytes. File
candidate capacity changes only from 69 to 70. No claim is made that the
old observed byte totals predict a future process or guarantee completion.

Early/helper maps and roles are checked against the newly collected keys.
Actual pre-science, post-science and closing boundaries each receive full
copied modules, launch, maps, own cwd/proc-cwd/proc-exe/executable metadata,
cached environment equality and output-descriptor metadata. The existing
closing module permission category is used at all three new boundaries;
their snapshot labels remain the actual distinct phases. No source load,
file role or content key is created to repair a late unknown.

After science, full module rows, launch record and process points must
equal pre-science; the exact file-backed map-path set must also agree.
Each individual map still has device/inode agreement to a complete key.
Addresses, anonymous allocations and heap shape are not required equal.
After the second key pass, closing uses those after keys; the complete
pre/post key equality binds the samples together. Final endpoint/absence,
module/launch/environment/output checks follow, but no later key_file call.

## Globals, cache and failures

The builtin compile/exec transition is explicitly new. Exact bytes are
compiled with an absolute filename and flags=0/dont_inherit=True/optimize=0.
One new globals/locals dictionary has __name__="__main__", the exact source
__file__, null package/spec/cache/loader, and the actual shared builtin
module. __builtins__ identity is checked; no custom builtin mapping,
function replacement or stdout proxy is supplied. sys.argv, orig_argv
and sys.modules continue to describe the wrapper. This is not represented
as a direct script run or separately imported scientific module.

Only the exact source's own __name__ branch starts main. Its source
constants, deterministic output ordering and assertions remain unchanged.
No return value or reconstructed output is substituted for its print.
An exception from source loading, compile, exec, stdout flush or a control
check means HOLD. The old finite class/errno/owned-code mechanism is reused
with 26 new literal wrapper codes; no exception text/args, arbitrary class
metadata, traceback formatting or new failure import is exported. An
unlisted exception class becomes other_exception/operation_failed.

Failure before helper availability uses an ASCII repr envelope on stderr
and native nonzero status; it is not JSON to eval or scientific output.
After helpers, the best-effort control record retains partial phases and
complete actual integer values. Science progress fields are set only as
their steps return; compile_completed is not science acceptance, and a
returned body without a successful flush is incomplete.

## Descriptor and capture lifetime

Each separately granted capture would create one fresh 0700 directory
nonrecursively under umask 077 and noclobber. It opens parent FDs 3, 4, 5
for fixed stdout.bin, stderr.bin, runtime_control.bin, preserving partial
allocations on failure. No target directory currently exists by claim or
observation. Bash/env/mkdir, interpreter bootstrap, ordinary ancestor
traversal, output-directory ownership and filesystem behavior stay the
explicit trusted boundary; no new host-tool attestation is claimed.

The single foreground invocation redirects in this exact order:

    child FD 1 <- parent FD 3 (science stdout)
    child FD 2 <- parent FD 4 (stderr)
    child FD 3 <- parent FD 5 (runtime control)
    child FDs 4 and 5 closed

The parent retains its own 3/4/5 until the native invocation returns, then
closes them and prints only P213_SCIENCE_NATIVE_EXIT=<actual status>.
Inherited trusted native stdin is unused and never opened or inspected.
The source launches no descendant, network operation or controller.
There is no hard timeout, process-group cleanup, storage reservation,
hostile-parent protection or liveness guarantee.

Before any science, the three child descriptors must be distinct regular
files with nlink=1 and size=0; none may have the device/inode of a complete
input key. The before/after identity projection is exactly the first
seven stat fields. stderr and control must keep all ten fields unchanged
through science. stdout is the original ordinary sys.stdout object;
its object identity and stderr identity are checked after exec, then both
streams are flushed. Its whole file size must be positive and at most
64 MiB. After that flush, all ten stdout fields must remain unchanged
through final output checks. Python does not read/hash stdout back.

Control is written only if the initial three-FD validation completed and
FD 3 still has its exact original ten-field empty-file record. Otherwise
native exit 79 may leave no control. One ASCII JSON+LF buffer, at most
16 MiB, is written with explicit positive-progress os.write accounting;
partial writes continue, zero/error fails, and a successful close is
required before native zero. This is not self-hashed output attestation.
External reception must key all three closed raw artifacts and reconcile
stdout length/descriptor identity with the reported point data, plus
capture/native return and all continuations.

Control serialization, its write/close, and interpreter/native shutdown
occur after the final point controls. They rely on the reviewed collector
and ordinary runtime boundary, not on a claim that snapshots attest every
instruction. Serialization/output failure exits 79; normal recorded HOLD
exits 78; only a complete pending-reception document followed by native
zero is a candidate for later independent reception. Even then all four
acceptance/adoption/pair flags remain false in this author-produced record.

## Output capacity and acceptance

Scientific framing remains OUTPUT_SCHEMA V1. Source-only arithmetic gives
17,990 WORD lines, 461 TARGET, 30 CARRIER and four header/trailer lines:
18,485 total. These are framing obligations, not observed numerical data.
A site vector has at most 11 characters, and a full carrier/vector list
has at most 126 entries, hence at most 1,511 characters. Carrier/target
fields plus bounded counters fit a 2,048-byte line envelope; WORD lists
are also subsets of a 126-state carrier after the source assertions.
Its at most two long-ascent interval tuples and other fixed fields fit
that envelope. Thus the complete successful declared output is below
18,485 * 2,048 = 37,857,280 bytes, within the chosen 64 MiB cap.
This is not a claim that any scientific assertions have passed.

The 16 MiB control capacity and 64 KiB-per-maps-read cap are fail-closed
limits, not predicted actual sizes or guarantees that every hypothetical
bounded module/implementation structure serializes within them. The wrapper
can fail on bounds or resources. The original science buffers output and
has no hard memory/wall-time guard; this proposal does not add one silently.

A future receiver must obtain complete raw bytes, exact native request/
return/continuations, empty stderr, complete valid control and every ordered
scientific record/assertion result. It must preserve every failure rather
than reconstruct a missing suffix or infer acceptance from counts/hash/PASS.
Canonical adoption and two new strict replay receipts remain separately
gated. No source, policy, runtime-key, wrapper/capture, parameter, schema
or canonical change is waived merely because stdout happens to match.
