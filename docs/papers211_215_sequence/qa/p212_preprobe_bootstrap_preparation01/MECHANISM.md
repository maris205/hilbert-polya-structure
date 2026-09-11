# New bounded native observer: exact claims and limits

Source-only author design. It has not been imported, compiled, parsed as
Python, syntax-checked, tested or executed. Source review and later actual
tool behavior must be independently received. The new code is not the
previous private-Git ten-field observer and does not inherit its acceptance.

## Native field semantics

The observer imports ctypes, hashlib.sha256, json, os, stat and sys under the
explicit ordinary observer-bootstrap assumption. Only after an exact enabled
observation-only canonical argument does it initialize libc.statx.
It never imports the author probe, driver, outer supervisor or Node preload.

The independently expressed ctypes.Structure has the fixed 256-byte statx
envelope, signed 64-bit seconds, unsigned 32-bit nanoseconds, and an
uninterpreted 112-byte tail beginning at offset 144. It checks little-endian
Linux, LP64 int/long/pointer sizes and all used offsets before any target stat.
It requests basic fields plus birthtime (0xFFF), retains the actual return,
errno, returned mask and complete post-call buffer, and decodes no fields
unless every requested bit is present. Buffers after failed syscalls are
failure evidence only, not returned valid stat fields. No zero/ctime fallback
is installed. Unsupported symbol, ABI, masks or nanoseconds remain HOLD.
The fixed layout and mask distinction follow the primary Linux UAPI.
[Linux v6.8 stat.h](https://github.com/torvalds/linux/blob/v6.8/include/uapi/linux/stat.h).

The fourteen decimal-string fields are dev, ino, mode, nlink, uid, gid, rdev,
size, blksize, blocks, atimeNs, mtimeNs, ctimeNs and birthtimeNs. Device IDs use
the observed major/minor values through ordinary os.makedev. This common
Python/libc dependency is disclosed; a different Structure expression is not
a claim of independent toolchain or hostile-platform verification.

AT_NO_AUTOMOUNT is requested throughout. Lexical component observations use
AT_SYMLINK_NOFOLLOW; same-handle observations use AT_EMPTY_PATH. A final
resolved-path stat is retained separately. Individual statx fields may reflect
different instants; this is discrete observation, not an atomic filesystem
snapshot or race exclusion.

Node's BigInt field names alone are insufficient for native birthtime support.
In the tagged libuv source, Linux statx can fall back to ordinary stat/lstat/
fstat, whose conversion may use ctime as birthtime; the public returned Stats
does not expose the required native mask. Nonzero values or inequality with
ctime do not prove support. This is why no Node-only fourteen-name result is
adopted as this masked native key.
[libuv Unix fs.c](https://raw.githubusercontent.com/nodejs/node/v22.22.2/deps/uv/src/unix/fs.c),
[libuv Linux conversion](https://raw.githubusercontent.com/nodejs/node/v22.22.2/deps/uv/src/unix/linux.c).

## Read, alias and membership semantics

All control paths are fixed source constants, whole pinned regular files and
physical component chains. Root source receipt, trust receipt and frontier
are distinct roles. Controls are keyed both before and, only if all targets
succeed, after the finite target passes. The current source does not pretend
to inspect its own interpreter history or require a bootstrap receipt for itself.

Target paths and allowed components are exact literal lists. Traversal checks
each next component against that set before statx. It records each link's
exact text before checking that the referent and all ancestors are approved.
Unknown referents stop before dereference. Dot/dot-dot, repeated/empty link
components, more than 40 symlinks or 1024 component steps require HOLD;
there is no silently normalized dot-dot alias. The mechanism may be amended
later if an actual finite in-scope alias requires it.

Each whole file is opened O_RDONLY|O_NOFOLLOW|O_NONBLOCK only after bounded
resolution. Native same-fd before/after keys bracket 64-KiB reads and whole
SHA256; metadata must match the resolved-path observation. The byte count
must match observed file size. No FIFO/device content is read. /dev/null is
metadata-only and must be a character device.

The exact lexical lstat (including a terminal symlink), resolved-path stat,
component-chain records, actual fd statx and full byte key remain separate.
All applicable fields except atime must match for leaves and symlinks.
For intermediate directories only dev/ino/mode/uid/gid/rdev/birthtime identity
is compared; size/link-count/timestamps are retained but not treated as an
assertion that unrelated directory membership is frozen. Target directory
leaves and the explicitly scoped memberships use full stable fields except
atime. This is an explicit ancestor-identity policy, not a hidden omission.

Membership uses bounded os.scandir iteration and entry.name only: no
DirEntry.stat/is_dir, unknown member body, child directory or recursive walk.
Every name and ordinal is preserved before an unknown-name/ceiling failure.
A selected name guard is compared exactly in both planned passes. Internal
directory buffering is ordinary libc/Python behavior, not a whole-host scan
or a hard per-syscall byte proof. No Node getDirent fallback is used.

The two passes are planned finite observations, not a retry policy. The first
failure stops all further targets and suppresses the second pass/closing
controls. Successful rows and raw native/path events already obtained remain
in the result. No retry, signal, cleanup or failure-to-success relabel occurs.

## Explicit ceilings

At most 384 targets and 768 literal components are accepted; this initial
frontier uses 164 and 204. Native statx calls are capped at 60,000.
Each path/link has a 4096-byte bound. Member names have 255-byte bounds;
directory ceilings are 32 or 320 for the five selected scopes, with at most
one overflow sentinel name observed. File limits are individually literal:
128 MiB for Node, 16 MiB for selected executable/library files, and 1 MiB for
source/configuration/raw-ELF captures. Reads use a 64-KiB buffer and a
512-MiB total byte ceiling, plus at most one failure sentinel byte.
Captured raw file bodies are capped at 1 MiB each and 8 MiB in aggregate.
Whole-key-only binary bytes are hashed completely but not embedded as hex.

Output is capped at 128 MiB after serialization. An output-size violation is
a failed capture with no successful result; it is not truncated-and-sealed
evidence. Root must retain actual transport returns and any process handle.
This in-process bound is not a hard time or peak-memory interrupt. Blocking
OS calls, transport truncation, failed stdout/close or an external timeout
cannot be converted into a completed observation. There is no automatic kill.

## Output is not an operational binding

The result always fixes observer_bootstrap_attested=false,
author_probe_executed=false and closure_certified=false. Even an exit-0,
two-pass result says only FINITE_OBSERVATION_ONLY_ROOT_RECEPTION_AND_CLOSURE_PENDING.
The output has its own schema, not the outer contract's descriptor schema.

Root may later derive explicit path/role/kind/comparison/lstat/stat/resolved/
symlink_target/content/members descriptors from the originals, with named
ancestor and alias roles, only after static follow-through. It must not rename
this initial result a complete operational key. The author's later statx
sample comparison, native ABI/runtime reception and subreaper gate remain
distinct, and no support is certified by these source-only instructions.
