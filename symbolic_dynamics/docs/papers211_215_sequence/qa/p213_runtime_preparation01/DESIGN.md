# P213 minimal runtime gate — design only

Status: `DESIGN_COMPLETE / SOURCE_AND_RUNTIME_ACCEPTANCE_PENDING`.
2026-09-09 UTC. This packet contains no observer, launcher or controller
source and authorizes no execution. Root agreed the overview direction and
requested this design be sealed before commissioning any observer source.

## Purpose and explicit trust boundary

The paper declares one zero-import, builtin-only scientific script. Its
documentary parameters are n=1..6 and mass=0..4, 30 carriers and 461 states;
these are declarations, not results reproduced here. The paper seal lists
verify.py as a01d3d93619cea90adfc2e5be1bdfd8089d7eae6fcaae153b4fb4af398fc1812.
This design neither independently verifies that script nor receives its
mathematics, source, parameters, output or complete manuscript seal.

Root preselected ordinary trusted product/Bash/env/CPython/kernel/filesystem
bootstrap. The future observation is a bounded record within that assumption,
not proof of hermetic startup, ELF/NSS/configuration closure, continuous
immutability, kernel correctness, absence of hidden hooks or exact loaded
memory bytes. It does not satisfy or replace P212's different old gates.
No birth-time/statx requirement, fourteen-field key, ancestor-device closure,
recursive observer or process supervisor is proposed.

## Launch contract to bind later

Use one source-reviewed independent observer in its own process, never an
import/runpy/exec wrapper around verify.py. No scientific source is parsed,
compiled, imported or run by the observer. A Linux CPython implementation
supporting sys.orig_argv is proposed; its actual path, version and identities
remain unresolved. Published 3.14 documentation and the 3.11.13 source example
below are semantic references, not an installed-version attestation.

The later binding must provide exact absolute paths for the trusted env
program, selected interpreter, observer and controlled working directory;
it must not search PATH or silently choose another interpreter. Use the
same cwd and interpreter/flags for later authorized science, changing only
the script argument. The observer and scientific program are still different
processes: equal launch settings do not prove identical startup state.

Proposed child environment, set by env -i after the trusted shell bootstrap,
is exactly LANG=C and LC_ALL=C, with no other entries. The observer checks
that finite child environment against this literal map; an unexpected entry
causes HOLD without dumping its name/value. No parent/shell environment,
credentials, SSH/Git configuration or general /proc environment is inspected.
This is not a claim about the environment before env executed.

Interpreter flags are exactly -I -S -B, no -O/-OO/-X and no arguments after
the script. -I isolates Python path/environment processing, -S skips site,
and -B disables bytecode writes, not all startup support or cache reads.
Do not add PYTHONHASHSEED and claim fixed hashing under -I. Assert execution
and output ordering remain the separate scientific source gate's obligation.
See the [official command-line contract](https://docs.python.org/3/using/cmdline.html).

Record actual sys.executable, sys.orig_argv, sys.argv, sys.flags,
sys.implementation, sys.version, sys.path and prefix/base-prefix values,
bytecode-cache settings, stdout/stderr encoding/error modes and actual cwd.
Compare them against the eventual binding rather than accepting a banner.
The interpreter executable readlink and file key must agree with the selected
path at the observation points; an empty/unresolved sys.executable is HOLD.
Only the observer's own /proc/self/exe and /proc/self/cwd are proposed here.
No interpreter path or host value is supplied by this design.

## Earliest snapshot and helper separation

The observer's first import is access to CPython's already-initialized sys.
That access is explicitly part of the trusted observer bootstrap, not a
claim of literally zero executed import statements. In the published
[CPython 3.11.13 initialization source](https://raw.githubusercontent.com/python/cpython/v3.11.13/Python/pylifecycle.c),
sys is created and registered during core initialization; encodings and
standard streams are initialized before ordinary script execution. Confirm
the applicable contract for the interpreter eventually selected.

The future source must perform this small, explicit sequence:

1. Immediately copy startup module facts into immutable scalar tuples,
   not retained module/spec objects. For each name record presence, builtin
   membership, spec origin, loader type name, has_location, __file__,
   __cached__ and package search paths where present. Save the relevant sys
   launch facts in immutable scalar form as well.
2. Before os/hashlib/json or any other helper import, read the raw bytes of
   /proc/self/maps using builtin binary file I/O, subject to a fixed byte
   limit. Preserve bytes unchanged in memory for later lossless emission.
   No parsing result can replace the original bytes. Take a second small
   pre-helper module snapshot to expose any change caused by observation.
3. Only then import the source-declared helpers, initially proposed as
   os, hashlib and json. Record the full post-helper module snapshot and
   raw maps separately, plus the later closing snapshot after collection.
   Explicitly list observer-added modules/native files; never relabel them
   startup dependencies. No discovery import or find_spec search is allowed.
4. Emit the saved early immutable data, late data and their separate file
   roles. Early data must not be reconstructed from mutated module/spec
   objects at serialization time. Missing, changed or unknown mechanism
   classifications are HOLD, not silently downgraded to builtin/frozen.

sys.modules is a mutable registry of loaded modules; copying it avoids
iteration races but a shallow copy alone does not freeze module attributes.
sys.orig_argv includes interpreter-consumed arguments unlike sys.argv.
Those published facts motivate the immutable capture and comparison design;
they do not certify a hostile runtime. See [sys documentation](https://docs.python.org/3/library/sys.html).

/proc/self/maps is a current mapping observation. Its complete raw bytes and
parsed address/perms/offset/device/inode/path records are preserved, including
anonymous and kernel-special entries. It is not a startup history, an atomic
whole-process snapshot, or evidence of every file ever opened. Partial-read
races are documented; the bounded read is explicitly a finite observation.
Do not deduce the future scientific process's complete native set from it.
See the [kernel proc documentation](https://www.kernel.org/doc/html/latest/filesystems/proc.html).

## Finite observation frontier and file keys

Before any probe, root must receive a finite observation binding with exact
approved paths/roles, supported module/loader classes and numeric bounds
for module count, maps bytes, regular-file count, bytes per file and total
bytes. None is presently resolved; this is a design prerequisite, not an
invitation to broad discovery. Proposed regular-file roles are limited to:

- The selected interpreter, observer source and explicitly approved lexical
  symlink targets for those paths.
- Ordinary-file module origins actually in the early snapshot; matching
  source/cache roles; and separately the same roles for declared helpers.
- Regular file-backed paths from the early maps and, separately, additions
  from helper/closing maps. Include all approved file-backed mappings, not
  only executable ones. Check map device/inode against the opened file key.
- Explicitly approved startup search candidates needed for the chosen
  CPython path arrangement, such as its zip-path candidate and exact cache
  candidates. These are finite named roles, not directory walks. Any cfg
  role would need to be individually approved; no configuration crawl or
  claim of exhaustive loader/config closure is made.

A snapshot supplies a role/path observation, not permission to open any
arbitrary named path. Unknown path, symlink target, loader, malformed map,
deleted mapping, non-regular file, unsupported encoding or bound exhaustion
is preserved and causes HOLD before a new out-of-allowlist content read.
This limit governs the observer's explicit path/metadata/hash reads; it is
not a sandbox around the already-trusted interpreter/helper import internals.
A later mismatch does not prove an earlier internal import was prevented.
Any late file dependency lacking an already complete approved key is HOLD;
there is no recursive discover/import/hash loop to force closure.
No recursive scanning, filesystem ancestor key, /dev/null content read,
other-process /proc access, ldd command, subprocess or network operation is
part of the observer. Ordinary directory traversal remains trusted.

Classify builtin and frozen origins by actual recorded spec/loader mechanism.
A frozen module can have a nominal __file__; its text file cannot be called
the executed source merely because that string exists. Any such nominal
role remains explicit and distinct. Unknown mechanisms are not guessed.
The import system's [module-spec and cache semantics](https://docs.python.org/3/reference/import.html)
also mean a source/cache existence record is not a trace proving which one
supplied the executed code. Existing ordinary source and eligible cache
files must both be fully keyed within the approved finite roles.

For each approved necessary regular file, open one bounded read-only fd,
verify its regular-file type, save fstat before reading, hash every byte up
to the accepted bound through EOF, and save fstat again on that same fd.
Require equal full keys, exact byte count equal to size, and agreement with
the path/lstat or map identity at the observation points. If it changes,
retain the failure and do not reopen/retry to obtain a matching read.
The eventual source must prevent a surprise FIFO/device from becoming a
blocking content read and check lexical symlink targets against the binding.

The exact ten non-atime integer fields are:

    st_dev, st_ino, st_mode, st_nlink, st_uid, st_gid,
    st_rdev, st_size, st_mtime_ns, st_ctime_ns

Add full-file SHA-256 and byte count. No timestamp float conversions,
missing-field zeros or ctime-as-creation-time substitution are allowed.
Record a present symlink's lstat key and literal readlink separately from
its final regular target. Point checks do not prove continuous immutability
or that the on-disk file equals already-relocated mapped memory. Integer
nanosecond accessors and file metadata meanings are documented in
[os.stat_result](https://docs.python.org/3/library/os.html#os.stat_result).

Every named optional role must receive an actual existence result. An absent
cache/zip role is accepted only from the precise authorized path's actual
not-found result; permission errors, dangling links, ENOTDIR and skipped
reads are distinct, not absence. Record both opening and closing point
checks for these finite roles. A sys.path string can name a zip that does
not exist; this behavior is documented in [path initialization](https://docs.python.org/3/library/sys_path_init.html).
Do not fabricate absence from -B, -S, a missing __cached__, another paper or
the present lack of observation.

## Capture, acceptance and later science

Use a single separately authorized native invocation, with exact request,
cwd, literal env/argv and transport settings recorded. Preserve separate
complete stdout/stderr bytes and every actual native return (including
any continuation/session return); a merged preview alone is not separate
stream evidence. Allocate new exclusive artifact paths. No overwrite,
reconstruction of truncated output, automatic restart or retry is allowed.
Lossless hex encoding of saved maps bytes inside the observer stdout is
acceptable if the receiver checks exact decoding and full byte counts.

An incomplete/error/truncated transport or nonzero exit is failed evidence,
not runtime acceptance, even if the observer emitted a final-looking record.
Conversely, exit 0 alone is insufficient: a different agent must receive
the complete raw streams, source/binding pins, early/late separation, all
required file keys/absences and complete native records. The design/source
author may explain them but cannot act as their independent runtime auditor.
This design promises no hard wall-time bound, hostile cancellation cleanup
or guaranteed final receipt under process/product/kernel failure. A later
capture mechanism must be separately source-reviewed, not expanded here
into a controller or copied from unrelated D01/P212 machinery.

Required sequence, with no implicit operation authority:

    source/parameter acceptance + root reception of this design
      -> separately commissioned minimal observer source and binding
      -> independent source acceptance + single-probe authorization
      -> actual bounded probe + independent runtime acceptance
      -> separately authorized scientific initial run and full reception
      -> separately authorized exact canonical adoption
      -> separately authorized strict author replay pair and raw comparisons

For later science, refresh the accepted finite source/runtime keys at the
agreed before/after points under the same trust boundary. A dependency
change reopens the affected gate; an identical key is not proof that a
different process had an identical complete runtime. The initial result
is neither replay. Actual accepted stdout, never inferred tables or an old
candidate result, supplies canonical bytes. This design neither fixes the
scientific output capture budget nor accepts a result; those belong to the
source/output and later launch gates. No enlarged parameter box is allowed.
TeX/BibTeX/font/build/page-view/Round0 and manuscript reviews remain separate.

## Deliverable boundary

Only this new preparation directory was written. No observer source exists
in it. No Python/Node interpreter, AST/compile/import, scientific test,
runtime probe, host/environment/configuration/proc observation, build,
Git/SSH operation or external manuscript action was performed. Ordinary
workspace documentary reads/hashes and public primary-document access are
recorded separately. All old papers, packets and failed evidence stay intact.
This is the requested design overview, not SOURCE_PASS, RUNTIME_PASS,
manuscript acceptance or batch completion. `OWNER_AMBER / HOLD_EXTERNAL`.
