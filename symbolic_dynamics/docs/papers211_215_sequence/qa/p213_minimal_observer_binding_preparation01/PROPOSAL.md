# P213 finite collection-policy proposal — source preparation only

2026-09-10 UTC. Author: /root/round211_functional_surgery_residual.
Status: FINITE_PROPOSAL / NO_CURRENT_RUNTIME_FACTS / NO_IMPLEMENTATION_HERE.
This packet is not an enabled binding, independent source audit or runtime
reception. It changes no frozen source, accepted design, audit or central index.

## Decision and narrow scope

The root's exact selected child01 RUNTIME_BEFORE.json is historical P211
data, not a current P213 snapshot. ARCHIVE_FILTER.json gives a disposition
and reason for all 57 old file-backed module names and all 11 old mapped
names. Retain 32 module candidates; reject 25 old wrapper/paper facilities.
Retain nine native-map candidate names; reject the two old C.UTF-8/gconv
names. These are permissions proposed for review, never observed identities.

POLICY.proposed.json is deliberately incompatible with the frozen exact-row
binding. It has enabled=false and no full expected/observed launch or module
rows. It proposes 62 exact module names: 32 file-backed, 26 builtin-only,
three frozen-only, and one distinct new direct-script __main__. Only 23
names are admissible before helpers. Membership is a finite upper frontier,
not a claim that every name occurs; required cores are separately explicit.
No general builtin-membership, filename-prefix or class-name wildcard exists.

The direct observer remains limited to import sys, then os/hashlib/json
after its earliest and second snapshots. The new proposal must not import
argparse, AST, pathlib, subprocess, locale, sysconfig or its own helper module.
Builtin names are qualified by observed builtin membership AND exact builtin
loader/origin rules. A compiled fallback installed as an unlisted extension
is unsupported, even if its short module name is permitted as builtin.

## Provenance of the finite import frontier

The static support scope is CPython 3.10.12 final on Linux, chosen as a NEW
admissibility predicate matching the archived release line and the tagged
public source consulted. No installed version was queried. A changed release,
layout, packaging, optional-module mechanism or import footprint is HOLD.
This is a justified conservative support proposal, not a proof that every
possible patched binary or failure path stays in the proposed frontier.

The first six file candidates cover I/O and UTF-8 startup: abc, codecs,
encodings, encodings.aliases, encodings.utf_8 and io. The os branch adds
stat, _collections_abc, posixpath, its os.path registry alias, and genericpath.
The json branch adds decoder/encoder/scanner and re; re adds enum,
sre_compile/sre_parse/sre_constants, functools and copyreg. functools and
collections account for types, reprlib, keyword and operator. These edges
are visible in the tagged primary sources, not inferred from the old 57
names alone. See [os](https://raw.githubusercontent.com/python/cpython/v3.10.12/Lib/os.py),
[json](https://raw.githubusercontent.com/python/cpython/v3.10.12/Lib/json/__init__.py),
[re](https://raw.githubusercontent.com/python/cpython/v3.10.12/Lib/re.py),
[functools](https://raw.githubusercontent.com/python/cpython/v3.10.12/Lib/functools.py)
and [collections](https://raw.githubusercontent.com/python/cpython/v3.10.12/Lib/collections/__init__.py).

hashlib attempts _hashlib, initializes supported algorithms and can call
six builtin constructors; the PBKDF2 fallback imports warnings. Thus those
six builtin-only names and warnings initialization have stated roles.
Logging after a failed algorithm constructor, warning formatting/linecache,
Unicode-name regex lookup/unicodedata and general resource-reader imports
remain outside support; their occurrence causes HOLD when next observable.
No observer uses those operations deliberately. This limitation follows the
actual conditional branches in [hashlib](https://raw.githubusercontent.com/python/cpython/v3.10.12/Lib/hashlib.py),
[sre_parse](https://raw.githubusercontent.com/python/cpython/v3.10.12/Lib/sre_parse.py)
and [warnings](https://raw.githubusercontent.com/python/cpython/v3.10.12/Lib/warnings.py).

The 13 early builtin candidates implement core sys/builtins, imports, bytes,
codec/I/O, POSIX, signal/thread/weakref/warnings and time bootstrap. The seven
helper builtin candidates come from stat, re, collections, operator and
functools imports. These are a finite mechanism proposal; the archive has
no builtin inventory and supplies none of their actual membership facts.
The three frozen names are expressly listed by
[CPython frozen.c](https://raw.githubusercontent.com/python/cpython/v3.10.12/Python/frozen.c).
No __hello__ test entry or importlib alias is admitted merely because the
upstream frozen table or a nominal filename mentions it.

## Structural module and loader predicates

Every actual row remains the original complete eight-field immutable row:
registry name/presence, builtin membership, spec, module loader, file,
cached and package paths. Spec retains origin, qualified loader, location
flag and search paths. Missing and null remain distinct tagged facts.
No copying of proposed rows into actual output is permitted.

Both spec and module loaders must match the exact qualified permission
record for their mechanism, including class versus instance. Builtin and
frozen loaders are classes _frozen_importlib.BuiltinImporter/FrozenImporter;
ordinary sources and extensions use instances of
_frozen_importlib_external.SourceFileLoader/ExtensionFileLoader.
These permission records are not observations. The ordinary implementations
and class-valued loaders are documented in
[importlib](https://docs.python.org/3.10/library/importlib.html#importlib.machinery).

Builtin rows require origin built-in and true builtin membership. Frozen
rows require origin frozen and false builtin membership. For these nonpackage
mechanisms, has_location is false, search paths are null, and package paths
are missing or null. Builtin file/cache fields are missing or null. A frozen
file may additionally equal only its explicitly listed NOMINAL path; that
path is never read or labelled executed-source evidence. Frozen cache is
missing or null. A missing/null spec outside __main__ is unsupported.

Ordinary rows require nonbuiltin membership, exact selected file=origin,
has_location=true, and exact package directory for encodings, json or
collections (null spec search paths and missing/null __path__ otherwise).
A source module's cached field must equal its exact proposed cache spelling;
an extension's cached field is missing or null. No namespace, zip loader,
sourceless bytecode-origin loader, alternative suffix or arbitrary alias
mechanism is supported. Both os.path and posixpath use the same exact
posixpath source/cache entries, and their structural facts must agree.

Direct-script __main__ requires the new proposed observer path, false builtin
membership, null (not missing) spec, null cached field, missing/null package
path, and the stated SourceFileLoader instance. The primary
[direct-file runner](https://raw.githubusercontent.com/python/cpython/v3.10.12/Python/pythonrun.c)
sets that loader and null cache. The
[import reference](https://docs.python.org/3.10/reference/import.html#main-spec)
documents its null spec. No old P211 wrapper or compile/exec identity is reused.

## Launch, cache and file permissions

Root selected /usr/bin/python3.10, /bin/bash, /usr/bin/env, /usr/bin/mkdir,
workspace cwd, env -i LANG=C LC_ALL=C and exactly -I -S -B direct-script
arguments. These lexical selections do not attest any installed tools.
The new observer/capture/probe paths are explicit proposals only; no such
source or runtime path was inspected or created by this packet.

The proposed three sys.path strings are taken as NEW exact constraints from
the archival names; four prefixes must be /usr and pycache_prefix must be
null. Version_info must be (3,10,12,final,0); implementation/cache tag and
Linux platform are constrained. Full sys.version, implementation scalar
dictionary, builtin-module-name tuple, all 17 named sys.flags plus its full
string, byteorder, abiflags, maxsize and encoding facts remain collected.
Cross-phase launch equality is retained. Recorded ancillary scalars are
bounded observations, not preclaimed historical values. The full 17-field
flag layout is in [sysmodule.c](https://raw.githubusercontent.com/python/cpython/v3.10.12/Python/sysmodule.c);
the proposal does not drop inconvenient applicable flags.

LC_ALL=C gives a proposed UTF-8-mode predicate, unlike the archived ENV4
C.UTF-8 run. UTF-8 filesystem/stdout/stderr encodings, surrogateescape for
filesystem/stdout, and backslashreplace for stderr are constrained according
to [Python UTF-8 mode](https://docs.python.org/3.10/library/os.html#python-utf-8-mode).
Only the cached os.environ mapping is compared with the two literal entries;
no environment reload, locale query or unexpected name/value dump is added.

There are 29 distinct .py paths (os.path is a shared alias) and 29 exact
nonoptimized __pycache__/NAME.cpython-310.pyc candidates. These spellings
are derived statically under cache_tag=cpython-310, optimize=0 and no cache
prefix, following [cache_from_source](https://raw.githubusercontent.com/python/cpython/v3.10.12/Lib/importlib/_bootstrap_external.py).
No Python cache function was called. -B prevents writes; it does not prove
preexisting bytecode absent or unused. SourceFileLoader can execute eligible
bytecode while reporting a .py origin. Consequently source OR matching-source
and eligible cache are both keyed when present; the packet never identifies
which bytes were actually executed. No extra matching-source discovery exists:
sourceless bytecode-origin loading is excluded outright.

The 69 unique candidate file paths are 29 sources + 29 caches + nine native
paths (including the two extensions) + one new observer + one zip eligibility
path. All are leaf-no-symlink permissions: final must equal lexical, with no
approved links. This is an observed-condition test, not an assertion that the
selected leaves are currently regular. Unknown links stop before following.
Trusted ancestor resolution is not an ancestor-scan or hostile-race guarantee.

The startup path /usr/lib/python310.zip is proposed MUST_BE_ABSENT at its
two required points, using genuine ENOENT only. If present, even an empty
zip is unsupported; it is not opened for exploration. Source/cache/native
candidates can be absent only while no actual content or map role requires
them. The observer and interpreter are mandatory. Eager preclosing keying of
the small finite eligible set is deliberate: it supports already-permitted
conditional/closing roles without inventing a late new-key operation.
Optional presence still requires a complete regular-file key; optional is
not permission to ignore permission errors, bad types, partial reads or
changed identity. Successful absent roles never count as loaded-code keys.

## Maps and numeric budget

Nine exact archived native path names are candidate permissions, including
six interpreter-process linkage candidates and three helper-time candidates
(_hashlib, _json, libcrypto). This is not a current ELF dependency proof.
No whole /usr/lib or extension-directory permission is inferred. All
file-backed maps count, including non-executable mappings. Special names
are exactly empty, [heap], [stack], [vvar], [vdso], [vsyscall]; every other
special/deleted/escaped/unknown path is unsupported. Ranges/addresses are
volatile samples; no historical address or inode is an expected current fact.

The proposed limits are: 62 module rows, 69 candidate files, 64 KiB per
raw maps snapshot, 8 MiB per ordinary file, 64 MiB aggregate file bytes,
1,024 characters per scalar, 128 sequence members and 16 MiB stdout.
The inherited positive link_hops bound is 1 for interface compatibility,
but every permitted chain is empty, so it grants no one-hop alias.
The selected old maps string has 6,692 bytes, and nine retained historical
native file lengths total 14,212,024 bytes; the largest is 5,937,704 bytes.
These measurements justify finite headroom, not a claim current sizes fit.
The stdout ceiling allows three hex map records, five module-snapshot
records and separate actual rows, roles, full keys and launch snapshots.
It is a conservative capture ceiling, not a formal promise that arbitrary
failure objects, huge ancillary scalars or I/O failure yield a complete
envelope. Overflow retains the failed scope; no limit is silently raised.
No deadline, supervisor, startup attestation or continuous syscall trace
is claimed. The one-byte overrun sentinel and whole-EOF requirements remain.

## Smallest honest source-contract delta and remaining gates

The frozen observer's exact full pre-observation launch/row requirements
cannot be filled from this archive. A new reviewed source must replace
only those expected-fact equalities with these explicit structural/invariant
permission predicates while retaining ALL actual immutable rows, actual
full launch records, before/after exact comparisons and separate late deltas.
Do not backfill an early row from a helper or closing snapshot.

Validate early names/mechanisms/paths before helper imports; validate
helper and closing records before further explicit candidate accesses.
Unknowns mean HOLD, not adaptive discovery. Ordinary trusted bootstrap and
helper imports are not instrumented: they may perform implicit reads before
the next snapshot. This boundary promise concerns further explicit observer
accesses after detection, not a syscall sandbox or retroactive denial of
already executed startup code.

Every accepted actual module content/map dependency must have a prior full
EOF hash plus ten integer metadata fields, stable fd/path observations,
map device/inode match and closing checks. No new file key after closing,
automatic retry, source/capture execution or probe is authorized here.

Root communicated two source findings (F01 process-exe order, F02 finite
error ownership). This proposal neither independently receives nor closes
them and implements no fix. Any exact new source delta must receive the
frozen audit, preserve those findings, and undergo the same separate reviewer.
Source/policy/capture acceptance and a distinct one-probe grant still precede
a single actual observation; independent full raw-output reception precedes
later scientific work. No missing generic host-discovery request is needed.
