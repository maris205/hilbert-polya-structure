# P213 minimal observer — source contract, not acceptance

Status: SOURCE_PREPARATION_ONLY / BINDING_UNRESOLVED / CAPTURE_DISABLED.
Author: /root/round211_functional_surgery_residual, 2026-09-09 UTC.
The governing originals are the accepted design, root receipt and independent
design audit pinned in INPUTS.sha256. This author is not the source auditor
or an independent receiver of future runtime output. No operation is granted.

## Binding and ordinary trust

observe.py has BINDING = None and exits before importing sys or observing
anything. BINDING.disabled.json is a schema-shaped documentary placeholder,
not a runtime input. An eventual enabled observer must be a separately
reviewed new source with the complete literal binding embedded before its
first import. No config/JSON file is read, parsed or imported to discover it.
The source path printed in the placeholder is this existing disabled source,
not a preselected future launch source. A new binding must name its own exact
reviewed observer path and retain provenance to this frozen predecessor.

The accepted premise is ordinary trusted product/Bash/env/CPython/kernel/
filesystem bootstrap. The small capture proposal additionally names one
ordinary trusted mkdir executable for exclusive, nonrecursive output-directory
allocation; its exact path is unresolved and must be accepted in the capture
source/binding review. This is not an attestation of these tool binaries or
pre-env process state. No recursive observer, P212 statx/birth-time/ancestor
device closure, cancellation supervisor, sandbox or ELF/NSS/config crawl
is introduced. Neither source has been run, parsed, imported or compiled.

The intended child environment is literally LANG=C and LC_ALL=C under
env -i. The source compares os.environ's cached Python mapping without
reloading it, changing it, or exporting any unexpected key/value. Matching
this mapping does not attest continuously refreshed C or parent environment.
See the [official os.environ semantics](https://docs.python.org/3/library/os.html#os.environ).
The exact interpreter argv is interpreter, -I, -S, -B, observer and nothing
else; argv, selected flags, CPython/Linux and sys.executable are checked.
The entire immutable launch record must also match the eventual binding.
The version, paths and encodings in public documentation are not installed
facts. No local executable or live process was inspected to fill them.

## Observation phases and immutable facts

After the disabled gate, the first import is access to initialized sys.
The source then takes an immutable module snapshot and immutable launch
snapshot, reads bounded raw /proc/self/maps through builtin binary I/O,
and takes the second module/launch snapshot before helper imports. The
declared helpers are exactly os, hashlib and json. No discovery helper,
find_spec, recursive import, science wrapper or subprocess is used.

Each completed module row is a tuple of name, registry presence, builtin
membership, spec facts, module loader identity, file, cache and package paths.
The spec tuple separately records origin, loader, has_location and search
locations. Scalars carry explicit missing/null/value/sequence tags. Module,
spec or loader objects are not saved in completed rows; tuple subclasses
such as sys.version_info are copied elementwise. Partial immutable rows
remain in module_snapshots if a later row cannot be represented.

A class-valued loader records class plus its actual __module__/__qualname__,
not type(loader) = type. An instance records its qualified concrete class.
__main__ with a null spec is the known direct-script case, not a missing or
unknown spec. The binding must approve actual qualified IDs, including
module/spec loader distinctions, and complete exact module facts.
See [direct-script spec semantics](https://docs.python.org/3/reference/import.html#main-spec)
and [loader mechanisms](https://docs.python.org/3/library/importlib.html#importlib.machinery.BuiltinImporter).

Helper and closing snapshots are distinct from early facts. Explicit
module added/removed/changed lists and newly observed mapped-file paths
identify late observations. Removal or changed early/helper facts is HOLD;
known additions have separately labelled roles. No late observation is
backfilled as startup evidence, and no added-path list proves causation.
The final module check is another point check, not continuous surveillance.

The three maps records retain raw byte counts, EOF status and lossless hex,
then parsed address/perms/offset/device/inode/path records. All regular
file-backed mappings, including non-executable ones, require approved roles.
Anonymous/kernel-special names require exact approved strings. The proposed
parser deliberately supports only printable ASCII lexical file paths without
backslash escapes, no deleted suffix and no normalization ambiguity.
Unsupported encodings/forms cause HOLD; the raw bytes remain evidence.
Partial map reads are not atomic runtime snapshots or startup history.
See the [kernel maps/race contract](https://www.kernel.org/doc/html/latest/filesystems/proc.html).

## Finite path, key and absence rules

The exact finite binding must contain all module names/facts, class IDs,
ordinary origin/cache/matching-source roles, optional zip/cache paths,
approved lexical symlink chains and final files, and every numeric bound.
The observer never expands this set. Unknown observed paths are rejected
before any new unapproved explicit path/content read. This is not a sandbox
around already-trusted interpreter/helper import internals. Frozen nominal
filenames remain nominal, never automatically executed-text dependencies.
The binding auditor must independently receive eligible matching-source/cache
roles for the selected version. -B is not an absence or cache-read proof.

All approved file entries are keyed once, including finite explicitly
preapproved optional/closing candidates; this is no discovery/hash loop.
The observer source and selected interpreter are mandatory file roles.
Each approved link hop has exact lexical path, literal readlink and next
path. A surprise link, chain target, nonregular final file or new path is
HOLD. Ordinary traversal of unkeyed parent directories is trusted; there
is no ancestor scan or continuous symlink-race immunity claim.

One O_RDONLY|O_NONBLOCK|O_NOFOLLOW|O_CLOEXEC fd opens each final regular
file. It is checked by fstat before any content read. Full file bytes are
hashed through EOF on that fd; byte count must equal size. Before/after
fstat and lexical/final endpoint observations must agree. Fields are exactly
st_dev, st_ino, st_mode, st_nlink, st_uid, st_gid, st_rdev, st_size,
st_mtime_ns and st_ctime_ns, all actual integers. SHA-256 describes every
byte actually read. It is a complete key only with complete=true, EOF,
all comparisons and successful close; an empty/partial digest is not a
whole-file key. Nanoseconds are integer accessors, not claimed precision
or creation time. [Metadata and open interfaces](https://docs.python.org/3/library/os.html#os.stat_result).

Per-file and total accepted read bounds apply to successful reads. A failed
overflow detection can consume one sentinel byte beyond the relevant bound;
that count/digest is retained and no retry occurs. Partial endpoint records,
exception class/errno, internal failure code and close errors are retained.
Arbitrary exception text is not exported. Nonblocking open plus pre-read
type checks avoid treating a surprise FIFO/device as a blocking content
stream; this is not a hard deadline for ordinary filesystem operations.

Optional absence is only the authorized literal path's actual lstat ENOENT
(Linux errno 2) with no approved link chain. ENOTDIR, permission failure,
dangling links and other failures are not absence. Every accepted optional
role receives opening and closing point evidence; appearance/disappearance
is HOLD. Present eligible caches are fully keyed even if their role is only
eligibility. An absent optional eligibility candidate is not a loaded-file
dependency; actual module origins and file-backed maps require complete keys.
Closing loaded dependencies must already have complete approved keys; no
new key is acquired to repair a late observation. File keys are not mapped
memory attestation or evidence of the next scientific process's runtime.

Only own-process maps/exe/cwd proc roles are named. Cwd/proc-cwd/proc-exe
and the interpreter's ten-field identity are checked at beginning, after
key collection and closing points. Named file/map identities are compared
by device/inode against complete keys. No other-process proc, environment
file, /dev/null, directory recursion, ldd, network or scientific file read
is included. verify.py is not a file role of this observer.

## Failure, capture and independent reception

capture.disabled.sh has an unconditional exit before directory changes,
output allocation or env/interpreter invocation. Its proposed body is a
single foreground invocation, not a controller. A reviewed absolute mkdir
creates one new 0700 directory without -p; existing paths fail. Fixed
stdout.bin/stderr.bin in that fresh directory are allocated under 077
umask and noclobber. This relies on trusted ownership/filesystem behavior;
noclobber alone on an arbitrary preexisting device is not the argument.
No partial artifact is deleted. No stdin is opened or inspected: inherited
trusted native stdin is unused by both programs. No hard deadline, process-
group cleanup, cancellation receipt or total liveness guarantee is offered.

Preserve complete separate raw stdout/stderr plus every actual native/session
return and exact request. A merged preview, missing continuation, nonzero
exit, truncated transfer or missing stream is failed/incomplete evidence.
Only the exact fully bound separately reviewed capture may receive a single
operation grant. Files and directories named by the disabled request have
not been created; their paths are unresolved, not reserved.

An early/helper-import error can emit a builtin ASCII-repr failed envelope
without importing a new serializer; do not eval/exec that output. After
helpers, the ordinary result is one ASCII JSON document. A source output
budget/serialization/stream failure exits 79 and may leave no complete
envelope; preserve the actual streams, never reconstruct missing maps or
claim a guaranteed final receipt. The enabled binding's output budget must
be independently justified from its finite rows and bounds. Exit 78 means
HOLD when the source reaches that handling; any other exception/fatal exit
also fails. A successful document explicitly says runtime_accepted=false
and OBSERVED_PENDING_INDEPENDENT_RECEPTION. Exit 0 is not acceptance.

An independent agent must receive all exact source/binding/capture pins,
full raw streams, native returns, phases, complete keys/absences and source
limits. This author cannot independently audit its own source or runtime.
Later initial science, canonical adoption, strict replay pair, before/after
refresh, build/page views/physical rounds and manuscript reviews each stay
separate. No parameter expansion or canonical fabrication is permitted.
OWNER_AMBER / HOLD_EXTERNAL.
