# Paper 27 successor build-validator lock

## 1. Authority, source identity, and scope

This is the sole validator-lock artifact for the current Paper 27 successor
corrective gate.  It binds, but does not execute, the exact validator source
`notes/BUILD_VALIDATOR_SUCCESSOR.py`.  The source is a strict UTF-8/LF,
no-BOM, no-CR, no-NUL, exactly-one-terminal-LF regular mode-0644 link-one
file.  The following is the sole machine-consumed identity frame:

```text
BATCH07_VALIDATOR_IDENTITY_BEGIN
bytes=398248
LF=9360
mode=0644
nlink=1
sha256=27c8f1e6535602f3cdc734eb8bf89ad28889493532d9628c31d9d95e78faffc1
terminal=# BATCH07_P27_BUILD_VALIDATOR_SUCCESSOR_AUTHOR_STOP
BATCH07_VALIDATOR_IDENTITY_END
```

The program is not a builder and has no filesystem repair, deletion, rollback,
compiler, BibTeX, external PDF-tool invocation, shell, subprocess, network, or
release branch.
Its sole filesystem payload creations are the exact exclusive snapshot and
root-manifest destinations in Section 5.  Every report path may also write
the wrapper-precreated stdout receipt on file descriptor 1; it neither writes
stderr nor creates a status receipt.  Descriptor and memory release is the
only cleanup.  This lock grants no execution or build authority.

Every validator PASS is conditional on an external trust root that this pure
Python program neither creates nor authenticates.  The externally sealed
launcher/build capsule is the trust root for process creation, the Python
loader, every standard-library module and shared object already loaded before
`main`, and the pre-`main` interpreter, validator-source, evidence-copy, and
validator-lock namespace.  The source-level import allowlist and the runtime
image, source/copy, and lock checks below therefore make no self-authentication
claim about code, bytes, path bindings, or namespace state selected, loaded,
or executed before `main`.

The same external capsule must provide one immutable no-concurrent-writer
namespace for the frozen validator source and evidence copy, this lock, all
frozen controls, the source trio, tools, dependency targets, and governed
parent directories over the complete span of process creation and every
separately executed compiler, BibTeX, PDF-tool, and validator interval.
Validator-held inode, digest, directory, symlink, absence, universe, and
receipt checks establish only the admitted state observed from `main` onward
during that single invocation.  They neither establish cross-process
continuity nor replace the external premise.  Both external conditions are
additional to, and never substitute for, any validator predicate; a PASS is
admissible only when both conditions hold.

On a complete successful guarded invocation, the program parses this frame and
binds the mode-0644 source and mode-0500 evidence copy before the handler, after
the handler and before PASS, and again after PASS emission.  Every check
requires exact bytes/LF/hash/terminal and source/copy byte equality.  A
mode-wide identity pool also holds the lock, source, and copy descriptors
across the handler and emission, repeatedly rehashes them, and rebinds their
pathname identities before close.  There is no claim that a pre-guard failure
can run these checks or that a universal `finally` reparses the frame.

## 2. Frozen upstream controls and runtime bootstrap

The validator hard-codes these exact regular mode-0644 link-one controls:

| Exact path relative to the Paper 27 project | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `notes/BUILD_PROFILE_SUCCESSOR.md` | 45,627 | 816 | `2e608faaa05e3063352c193869b92d5a305cc3de956ad18624d457b303787bec` |
| `notes/DEPENDENCY_LOCK_SUCCESSOR.md` | 30,145 | 215 | `66c96cc6b40658370cc129e3bf828bcd08a7e69f7f2462ebea084cc77ce6ed17` |
| `notes/INDEPENDENT_DEPENDENCY_LOCK_SUCCESSOR_REVIEW.md` | 12,687 | 231 | `b37e361c1cb8e7340c7a2e4af5b207de40df935ced707043c63c1e0f7017df35` |
| `notes/INDEPENDENT_BUILD_PROFILE_SUCCESSOR_SYMLINK_POLICY_REVISION_REVIEW.md` | 19,942 | 353 | `d8f8c82c722d00dcf419e6878cbcda3b3f784ed734ebb91dc33502271ceb2893` |
| `notes/INDEPENDENT_STATIC_SOURCE_SUCCESSOR_REVIEW.md` | 31,760 | 704 | `7745af4b80e4e5ff35134e9279b7d2493f9b063bac0110bab115199bae3114ae` |

It hard-codes this exact source trio, each regular mode 0644 and link one:

| Relative source | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 55,063 | 1,681 | `d60ec6611683cafdf822b4cb493040258dc1dd29502363d493f52c3e2deeed3e` |
| `paper/math_commands.tex` | 601 | 17 | `34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957` |
| `paper/references.bib` | 6,610 | 217 | `a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5` |

Every invocation is exactly

```text
/root/miniconda3/bin/python3 -S -B -P /root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/build/successor-d60ec6611683-evidence/BUILD_VALIDATOR_SUCCESSOR.py MODE ARGS...
```

The script requires its own `argv[0]` to equal the absolute evidence-copy
path above.  `-S` disables `site`, `-B` prohibits bytecode writes, and `-P`
removes the unsafe script-directory prefix.  The exact invocation symlink is
10 bytes, mode 0777, link one, raw target `python3.12`; the exact regular
target `/root/miniconda3/bin/python3.12` is 30,626,264 bytes, mode 0755,
link one, SHA-256
`9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101`.

The exact complete child-environment key/value mapping is:

```text
LANG=C
LC_ALL=C
PATH=/usr/bin:/bin
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
PYTHONIOENCODING=UTF-8:strict
PYTHONNOUSERSITE=1
PYTHONSAFEPATH=1
PYTHONUTF8=1
TZ=UTC
```

After the exact argv row has matched and the receipt guard, launch-FD census,
and identity pool have opened, the runtime check requires Python 3.12,
`dont_write_bytecode=1`, `no_site=1`, `no_user_site=1`, `safe_path=1`,
`utf8_mode=1`, and `hash_randomization=0`.  It also binds `sys.argv`,
`sys.orig_argv`, `sys.executable`, `__file__`, `__name__`, `__spec__`, and
`__package__` to the exact launch.  On that complete-success path, the check
runs before the handler, before PASS, and after PASS; all three returned
vectors must match.

The only imports, in source order, are the explicit standard-library allowlist
`fcntl`, `hashlib`, `math`, `os`, `re`, `resource`, `stat`, `sys`, and `zlib`.
There is no `ImportFrom`, dynamic import, `eval`, built-in `exec`, built-in
`compile`, import-by-name, user/site code, environment-selected path,
locale-selected parse, randomness, clock read, or filesystem bytecode or
cache-file write.

The soft `RLIMIT_NOFILE` must be finite and between 1,024 and 4,096.  After
the receipt guard opens, the program directly opens `/proc/self/fd`, rewinds
and lists that descriptor twice, and requires both live-FD sets to equal
exactly descriptors 0/1/2, the stage and guard read descriptors, every held
stage-chain descriptor, and the scan descriptor itself.  Any inherited FD
fails.  The interpreter target is component-anchored and held; direct
`/proc/self/exe` fstat must equal it, and a chunked read must reproduce exactly
30,626,264 bytes and the frozen digest before terminal target rebind and close.

## 3. Toolchain and complete dependency constants

Every `REPLAY` and `ABSENT` rebinds all tool paths without following the
invocation symlink and hashes each regular target:

| Path / role | Frozen identity |
|---|---|
| `/usr/bin/pdflatex` | symlink: bytes 6, 0777, link 1, raw `pdftex`, lexical target `/usr/bin/pdftex` |
| `/usr/bin/pdftex` | 1,802,504 bytes; 0755; link 1; `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` |
| `/usr/bin/bibtex` | symlink: bytes 24, 0777, link 1, raw `/etc/alternatives/bibtex` |
| `/etc/alternatives/bibtex` | symlink: bytes 24, 0777, link 1, raw `/usr/bin/bibtex.original` |
| `/usr/bin/bibtex.original` | 117,128 bytes; 0755; link 1; `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |
| `/usr/bin/env` | 43,976 bytes; 0755; link 1; `85036540673319c6c2f54233fd2b9e45a8a71246b51cc96c4e6ab8ee6c419eb0` |
| `/usr/bin/bash` | 1,396,520 bytes; 0755; link 1; `59474588a312b6b6e73e5a42a59bf71e62b55416b6c9d5e4a6e1c630c2a9ecd4` |
| `/usr/bin/mkdir` | 68,104 bytes; 0755; link 1; `bd2f081ac37d653181332bd27f35a6041dbf215a7957f65838a9cbec9e64928b` |
| `/usr/bin/install` | 145,944 bytes; 0755; link 1; `519a00d199d07da6028ec5a9800d92c562934582a2ea1793b2cbc378a85c1439` |
| `/usr/bin/cmp` | 43,408 bytes; 0755; link 1; `b355472d3c90ea94d11ebb8b750e6946ccd348edc6fca4aefc1235c3994ef791` |
| `/usr/bin/pdfinfo` | 59,928 bytes; 0755; link 1; `8ca6e6d0b2e6b3f135a82feb07b3d5750498eb77e6f66412803f425eb8471a8e` |
| `/usr/bin/pdftotext` | 43,544 bytes; 0755; link 1; `7de929ce0686af5dbf76975ad08bbff93526b3d9028035176a4ca89d9d19c27d` |

The embedded dependency row stream is byte-for-byte equal to Section 4 of
`DEPENDENCY_LOCK_SUCCESSOR.md`: 87 rows, 23,408 bytes, 87 LF bytes,
SHA-256
`2855b5fe4a859552fc581eb3c06b11c68008b8eb67351d37f2a44c57a91adf87`.
It yields 87 logical paths and 86 distinct final regular targets.  The two
nonzero-hop rows are hard-coded with these raw bindings:

```text
/usr/share/texmf/web2c/texmf.cnf	bytes=40	mode=0777	nlink=1	raw=../../texlive/texmf-dist/web2c/texmf.cnf	final=/usr/share/texlive/texmf-dist/web2c/texmf.cnf
/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map	bytes=15	mode=0777	nlink=1	raw=pdftex_dl14.map	final=/var/lib/texmf/fonts/map/pdftex/updmap/pdftex_dl14.map
```

For every dependency pass, all 87 logical roles are lstat'ed, both raw symlink
bytes and lexical canonical targets are reproduced, and all 86 unique finals
are opened with `O_RDONLY|O_NOFOLLOW|O_CLOEXEC`; the shared final is hashed
once.  Identity-only reads keep an anchored held FD, use positional chunks of
at most 1 MiB through the frozen size, perform a one-byte EOF probe, then
stream the held bytes again while rebinding FD and pathname stat before close.
Every byte count, mode, link count, and digest is required.  A recorder
external-input set is nonempty and may be a strict subset of the frozen
logical/final union; no unlisted external path is admitted.

The mode-wide identity pool for every mode holds 12 regular files, the Python
symlink, and 12 shared-prefix directory FDs, for 25 descriptors.  `ABSENT` and
`REPLAY` extend that plan to 107 distinct regular files, six symlinks, and 68
prefix-directory FDs, for 181 descriptors, below the static ceiling of 512.
The base plan is the lock/source/copy, five controls, three paper sources,
Python target, and Python symlink; the extended plan adds every tool,
dependency final, and tool/dependency symlink.  It spans the handler and PASS
emission and is rehashed/rebound at all three hold checkpoints.

## 4. Exact roots, stages, directory enumeration, and I/O discipline

The exact aliases used only to compact the tables below are literal:

```text
P=/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity
E=P/build/successor-d60ec6611683-evidence
R0=P/build/successor-d60ec6611683-r0
R1=P/build/successor-d60ec6611683-r1
S0=E/r0
S1=E/r1
X=E/cross-root
```

They are explanatory aliases only.  The Python constants contain the full
absolute strings; no environment, prefix scan, directory content, or user
argument expands an alias.

Every configured project, build, tool, and dependency path is reached through
a held no-follow descriptor for `/` and per-component
`O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC` descriptors, or through the
equivalent mode-wide shared-prefix identity pool.  Entry/fstat identity is
bound at each step.  An explicitly walked component chain stays open through
the leaf operation and is rebound on close; the mode-wide pool is rebound at
the terminal checkpoint immediately before close.  The only literal direct
proc opens are
`/proc/self/fd` for the launch-FD census and `/proc/self/exe` for the running
image.  No path is derived from environment, user text, or enumeration
results; parent components and basenames are derived only from frozen exact
constants and validated exact argv rows.

Ordinary payload reads use no-follow leaf stat/open, one positional
`pread(st_size+1, 0)`, and exact-length enforcement.  A short read or extra
byte fails closed and is not retried under a possibly changed file version.
Pre/post FD and pathname stat keys, mode/link/size, full-payload SHA-256, and
the exact per-file and aggregate caps below are required.  Identity-only reads
instead use the held chunked streaming/EOF-probe discipline in Section 3.
There is no glob, `os.walk`, filesystem recursion, `realpath`, `resolve`,
shell, or subprocess.

### Exact filesystem and text resource ceilings

All KiB and MiB quantities in this lock are binary multiples of 1,024.  Every
ceiling below is inclusive: a size or count fails only when it exceeds the
stated value.  The generic dynamic-read ceiling is 64 MiB, but every governed
root, stage, evidence, receipt, and parser role is further restricted as
follows.  Exact-name universes and argv maps are checked before these cap
functions, so a numeric cap never admits an otherwise unknown basename.

The direct regular-file caps in either build root are:

| Exact root basename | Maximum bytes |
|---|---:|
| `main.tex` | 256 KiB |
| `math_commands.tex` | 64 KiB |
| `references.bib` | 256 KiB |
| `main.log` | 8 MiB |
| `main.aux` | 4 MiB |
| `main.fls` | 8 MiB |
| `main.pdf` | 64 MiB |
| `main.bbl` | 2 MiB |
| `main.blg` | 512 KiB |

For the next table, `V` is exactly this 36-ID set and is only an explanatory
alias:

```text
A000 R009 V020P V020Q R021 R022 R023 C023 R024
V030P V030Q R031 R032 B032 L033 R033
V040P V040Q R041 R042 R043 C043 R044
V050P V050Q R051 R052 R053 C053 R054
F055 F061 F063 F064 F065 I066
```

The exact stage/evidence regular-file role caps are:

| Admitted exact role or receipt ID | Maximum bytes |
|---|---:|
| Every admitted `*.status` | 2 bytes |
| Every admitted `*.stderr` | 0 |
| `R009`, `R024`, `R033`, `R044`, or `R054` root manifest | 256 KiB |
| `R021`/`R041`/`R051` `main.log` snapshot | 8 MiB |
| `R022`/`R042`/`R052` `main.aux` snapshot | 4 MiB |
| `R023`/`R043`/`R053` `main.fls` snapshot | 8 MiB |
| `R031` `main.bbl` snapshot | 2 MiB |
| `R032` `main.blg` snapshot | 512 KiB |
| `R000`--`R008`, `X001`--`X008`, or `E001 E010 E011 E012` stdout | 0 |
| `R020 R030 R040 R050` stdout | 4 MiB |
| `R060` pdfinfo stdout | 64 KiB |
| `R062` PDF-text stdout | 8 MiB |
| Every `V` stdout and `X009`/`X010` stdout | 1 MiB |
| Evidence-root `BUILD_VALIDATOR_SUCCESSOR.py` | 1 MiB |

The evidence validator copy is mode 0500.  Every other direct evidence-root
regular is mode 0600 and uses the same exact receipt-role cap above; the
`r0`, `r1`, and `cross-root` entries are child directories and do not pass
through a regular-file cap function.

The four complete direct-regular aggregate ceilings are:

| Governed container | Maximum sum of actual direct-regular sizes |
|---|---:|
| Each held `R0` or `R1` root universe | 96 MiB |
| Each held `S0` or `S1` stage universe, and each `_inventory_stage` preflight | 128 MiB |
| Held `X` for `CROSS`/`X009` or `EVIDENCE`/`X010` | 4 MiB |
| Held evidence root `E` for `ABSENT`, `REPLAY`, or `EVIDENCE` | 2 MiB |

For each aggregate, every direct non-directory regular first satisfies its
role cap, then its actual `st_size` is added.  Direct child directories are
skipped before the sum: the five cache children do not count toward 96 MiB,
and `E/r0`, `E/r1`, and `E/cross-root` and their contents do not count toward
2 MiB.  Those stage/cross contents receive their own independent 128-MiB or
4-MiB universe/inventory bounds when governed.  The 128-MiB stage cap covers
the completed `S0` additionally held for root-1 `ABSENT`/`REPLAY`, both root
stages held by `CROSS`/`EVIDENCE`, the selected `STAGEINV` stage, and every
`_inventory_stage` preflight over its completed names plus any supplied
in-flight streams.  These are not recursive tree quotas.

Mutable in-flight stdout/stderr must be empty when a held universe opens and
therefore enter that opening aggregate as zero bytes.  The same held universe
does not recompute its aggregate after report emission; a later exact
`_inventory_stage` whose completed-name set contains that receipt recomputes
the actual stage sizes under the 128-MiB ceiling.  This timing does not weaken
the separate content, offset, identity, and exact-name rechecks around
emission.

The following byte/LF/physical-line limits govern accepted inputs.  For every
listed role except `R060` PDFINFO, they are enforced before subsequent
line-list materialization.  PDFINFO first enforces its 64-KiB total-byte and
framing bounds, then performs a byte-bounded LF split; its 4,096-byte
physical-line ceiling and unique closed 18--22-line schema are enforced while
consuming that materialized list.  Per-line byte counts exclude their
terminating LF unless a qualification below states otherwise.

| Text role | Byte ceiling | LF/line ceiling | Physical-line ceiling | Terminal rule |
|---|---:|---:|---:|---|
| Validator lock | 1 MiB | 10,000 LF | 64 KiB | terminal LF required |
| Validator source | 1 MiB | 100,000 LF | 64 KiB | terminal LF required |
| Root manifest | 256 KiB | 1,024 LF | 16 KiB | terminal LF required |
| Recorder | 8 MiB | 200,000 LF | 16 KiB | terminal LF required |
| AUX | 4 MiB | 100,000 LF | 16 KiB | terminal LF required |
| BBL | 2 MiB | 50,000 LF | 16 KiB | terminal LF required |
| BLG | 512 KiB | 1,024 LF | 4,096 bytes | terminal LF required |
| Log | 8 MiB | 200,000 LF | 4,096 bytes | terminal LF required |
| `R060` PDFINFO | 64 KiB | closed 18--22-line schema | 4,096 bytes | exactly one terminal LF |
| `R062` PDFTEXT | 8 MiB | 200,000 LF bytes | 64 KiB per LF-delimited segment | terminal LF not required |

The evidence copy is not line-split a second time, but it must be byte-equal
to the source that passed the 1-MiB/100,000-LF/64-KiB source preflight, and its
evidence role and identity-pool reads are independently capped at 1 MiB.  The
identity-frame `bytes` decimal first has the generic 64-MiB parse ceiling, but
a complete successful path is still limited to the 1-MiB source/copy role.
The frozen root manifests contain only the exact state rows; 1,024 is a parser
resource ceiling, not an expected census.

AUX active lines remain within 100,000; one multiline longtable record is at
most 4,096 lines and 256 KiB including its inserted LF separators.  BBL active
lines remain within 50,000; one bibitem content is at most 4,096 lines and
256 KiB counting one LF per line, with at most six `newblock` controls.  After
its resource preflight, BLG has exactly 46 closed-schema lines.  PDFINFO has no
separate generic line-count constant: its unique closed schema derives the
18--22 range.  PDFTEXT counts LF bytes, so an input without a terminal LF may
have 200,001 physical segments; form feeds do not reset the 64-KiB
LF-delimited-segment ceiling.

The pure-underfull warning set has at most 4,096 lines and its reconstructed
frame has at most 256 KiB.  Each retained original UTF-8 physical line receives
one LF, and that LF counts toward the frame ceiling; a 4,097th line or a frame
larger than 256 KiB fails before hexadecimal expansion.

Ordinary finite directory census has exactly one `os.scandir(fd)` call site.
It rewinds a held exact directory FD, converts only `entry.name` with
UTF-8/surrogateescape, rejects an unknown or over-255-byte name immediately,
and checks duplicate, missing, and exact-set closure.  It never forms a path
from a returned name.  The only `os.listdir` call is the two-pass numeric
`/proc/self/fd` census in Section 2.  Artifact census applies only to held
descriptors for the exact roots, their five cache children, the evidence root,
the two root stages, or the cross stage.

Root states have these exact complete name sets:

| State | Exact names in addition to the five empty directories and three sources |
|---|---|
| `SETUP` | none |
| `TEX1` | `main.aux`, `main.fls`, `main.log`, `main.pdf` |
| `BIB` | the `TEX1` set plus `main.bbl`, `main.blg` |
| `TEX2` | exactly the `BIB` set |
| `FINAL` | exactly the `BIB` set |

The root itself is mode 0700, link seven; each of the five enumerated empty
directories is mode 0700, link two; source copies are exact regular mode-0644
link-one bytes; every generated top-level file is regular mode 0600, link
one.  Raw manifest rows are
`relative<TAB>type<TAB>bytes<TAB>LF<TAB>mode<TAB>nlink<TAB>sha256<LF>`;
directories use `-` for bytes/LF/hash.  Rows are distinct and byte-sorted.
All five cache-directory descriptors remain open while the root frame is
read; each is initially empty, relisted empty at the end, rebound against its
parent entry and original identity, and only then closed.  The root itself is
also relisted/rebound before release.  Every regular child is held open with
its frozen stat/size/LF/digest, then streamed again from the held FD and
rebound to the pathname before close.  No full child payload cache is needed
to prevent an in-place rewrite from leaving a stale manifest row.

The complete 74-element exact argv set must match before mode-specific
filesystem inspection.  The receipt guard then requires the current
`.stdout` and `.stderr` to preexist as distinct empty regular mode-0600
link-one files, their process descriptors to be write-only, non-append and at
offset zero, and the matching `.status` to be absent.  It holds the stage and
both read descriptors across the handler and report emission.  Exact mode
universes, pre/post-handler regular holds, the ABSENT root hold, and the
identity pool are checked before and after emission.

`SNAPSHOT` and `MANIFEST` are the only new filesystem payloads.  Their exact
stage and literal basename are component-anchored and required absent;
creation uses `O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC`, mode 0600,
chunked writes, file-FD `fsync`, post-write fstat/stat, close/reopen, and full
reread/hash.  The parent directory is not claimed crash-fsynced.  There is no
rename, remove, unlink, truncate, overwrite, recreation or retry after a failed
creation or write, or partial-file cleanup.
After a snapshot is reread, its live source must reproduce the original
bytes/size/LF/hash before PASS.  After a manifest is reread, the entire root
frame is regenerated and must equal it.  Terminal recomputation and the
post-handler held FD bind the created destination through report emission.

## 5. Exhaustive modes and argv rows

There are exactly 15 mode names and 74 accepted argv rows after the absolute
script path.  The arities below exclude the mode token.  Every unlisted mode,
row, alias spelling, relative path, missing/extra argument, or alternate
destination raises exit-2 usage failure before the receipt guard, identity
pool, or any mode-specific filesystem inspection is opened; as specified in
Section 8, that pre-guard path may still attempt to write its one failure
diagnostic to the already supplied file descriptor 1.

| Mode | Arity | Exact row count |
|---|---:|---:|
| `ABSENT` | 2 | 2 |
| `REPLAY` | 2 | 16 |
| `SNAPSHOT` | 4 | 22 |
| `MANIFEST` | 3 | 10 |
| `RECORDER` | 3 | 6 |
| `R033LIVE` | 3 | 2 |
| `BIB` | 5 | 2 |
| `LOGBIB` | 7 | 2 |
| `PDFINFO` | 3 | 2 |
| `PDFTEXT` | 3 | 2 |
| `PDFRAW` | 2 | 2 |
| `SOURCEFINAL` | 1 | 2 |
| `CROSS` | 1 | 1 |
| `STAGEINV` | 2 | 2 |
| `EVIDENCE` | 2 | 1 |

The two `ABSENT` rows are exactly:

```text
ABSENT R0 S0
ABSENT R1 S1
```

For each literal root/stage pair `(R0,S0)` and `(R1,S1)`, the eight exact
`REPLAY` rows are:

```text
REPLAY Rn R020-pre
REPLAY Rn R020-post
REPLAY Rn R030-pre
REPLAY Rn R030-post
REPLAY Rn R040-pre
REPLAY Rn R040-post
REPLAY Rn R050-pre
REPLAY Rn R050-post
```

The state map is respectively `SETUP`, `TEX1`, `TEX1`, `BIB`, `BIB`,
`TEX2`, `TEX2`, `FINAL`.  Each replay rebinds controls, tools, all 87/86
dependencies, the validator source/copy equality, live sources/root copies,
and the exact root universe.

For each literal pair `(Rn,Sn)` the eleven exact `SNAPSHOT` rows are:

```text
SNAPSHOT Rn R021 Rn/main.log Sn/R021--main.log.snapshot
SNAPSHOT Rn R022 Rn/main.aux Sn/R022--main.aux.snapshot
SNAPSHOT Rn R023 Rn/main.fls Sn/R023--main.fls.snapshot
SNAPSHOT Rn R031 Rn/main.bbl Sn/R031--main.bbl.snapshot
SNAPSHOT Rn R032 Rn/main.blg Sn/R032--main.blg.snapshot
SNAPSHOT Rn R041 Rn/main.log Sn/R041--main.log.snapshot
SNAPSHOT Rn R042 Rn/main.aux Sn/R042--main.aux.snapshot
SNAPSHOT Rn R043 Rn/main.fls Sn/R043--main.fls.snapshot
SNAPSHOT Rn R051 Rn/main.log Sn/R051--main.log.snapshot
SNAPSHOT Rn R052 Rn/main.aux Sn/R052--main.aux.snapshot
SNAPSHOT Rn R053 Rn/main.fls Sn/R053--main.fls.snapshot
```

For each literal pair `(Rn,Sn)` the five exact `MANIFEST` rows are:

```text
MANIFEST Rn R009 Sn/R009--root.manifest
MANIFEST Rn R024 Sn/R024--root.manifest
MANIFEST Rn R033 Sn/R033--root.manifest
MANIFEST Rn R044 Sn/R044--root.manifest
MANIFEST Rn R054 Sn/R054--root.manifest
```

They bind states `SETUP`, `TEX1`, `BIB`, `TEX2`, and `FINAL`.  The transition
checker requires R024 to preserve setup rows and add exactly four files;
R033 to preserve every R024 row and add exactly `main.bbl`/`main.blg`; and
R044/R054 to preserve root/directories/sources/bbl/blg exactly.

For each literal pair `(Rn,Sn)` the three exact `RECORDER` rows are:

```text
RECORDER Rn R023 Sn/R023--main.fls.snapshot
RECORDER Rn R043 Sn/R043--main.fls.snapshot
RECORDER Rn R053 Sn/R053--main.fls.snapshot
```

The two rows for each remaining root-local mode are exactly:

```text
R033LIVE Rn Rn/main.fls Sn/R023--main.fls.snapshot
BIB Rn Rn/main.bbl Rn/main.blg Sn/R031--main.bbl.snapshot Sn/R032--main.blg.snapshot
LOGBIB Rn Rn/main.log Rn/main.aux Rn/main.bbl Rn/main.blg Rn/main.pdf Sn/R060.stdout
PDFINFO Rn Rn/main.pdf Sn/R060.stdout
PDFTEXT Rn Sn/R060.stdout Sn/R062.stdout
PDFRAW Rn Rn/main.pdf
SOURCEFINAL Rn
```

Here, and only here, `n=0` means the literal `(R0,S0)` pair and `n=1` means
the literal `(R1,S1)` pair.  This defines 2 rows for each displayed mode,
not a runtime placeholder grammar.

The remaining exact rows are:

```text
CROSS X
STAGEINV S0 r0-pre-I066
STAGEINV S1 r1-pre-I066
EVIDENCE E X
```

`EXACT_ARGV_ROWS` is the 74-element `frozenset` of expanded absolute tuples
formed from the frozen root/state/maps above and the literal
`CROSS`/`STAGEINV`/`EVIDENCE` rows.  The aliases in this document admit no
third root, stage, or substitution.  `REPLAY` verifies tools and dependencies
inside its handler and again after PASS emission; the receipt guard, root
universe, and mode-wide identity pool remain held through those checks.

## 6. Receipt, snapshot, manifest, and evidence-stage basenames

For every completed ID below the three exact basenames are the Cartesian suffixes
`ID.stdout`, `ID.stderr`, and `ID.status`; there is no other suffix.  Each is
regular mode 0600, link one.  Status is exactly `0<LF>` and stderr is empty.
Silent-command stdout is empty; publication/PDF-tool stdout obeys its bound
text grammar.  Every root-stage validator receipt is additionally bound by
ID to its exact mode and leading field sequence: `PASS MODE root=r0|r1 `,
except `I066`, which is `PASS STAGEINV stage=r0|r1 `.  Replay receipts also
bind their exact `checkpoint=R0x0-pre|post`; snapshot and manifest receipts
bind their same-numbered `id=R...`; and C023/C043/C053 bind respectively
`id=R023/R043/R053`.  Cross receipt `X009` begins exactly
`PASS CROSS raw_pairs=8 `.  All are single ASCII lines; no generic `PASS `
substitute is accepted.

Each root stage has these 50 pre-inventory IDs:

```text
R000 R001 R002 R003 R004 R005 R006 R007 R008
R020 R030 R040 R050
A000 R009 V020P V020Q R021 R022 R023 C023 R024
V030P V030Q R031 R032 B032 L033 R033
V040P V040Q R041 R042 R043 C043 R044
V050P V050Q R051 R052 R053 C053 R054
F055 F061 F063 F064 F065
R060 R062
```

`R000`--`R008` are silent initialization commands; `R020`, `R030`, `R040`,
and `R050` are publication-text commands; `R060` is pdfinfo text; `R062` is
pdftotext UTF-8/form-feed text; all remaining IDs above are validator modes.
After `STAGEINV`, the only added receipt ID is validator ID `I066`.

The exact validator-receipt ID-to-mode map, applied independently within each
root stage, is:

```text
A000=ABSENT R009=MANIFEST
V020P=REPLAY V020Q=REPLAY R021=SNAPSHOT R022=SNAPSHOT R023=SNAPSHOT C023=RECORDER R024=MANIFEST
V030P=REPLAY V030Q=REPLAY R031=SNAPSHOT R032=SNAPSHOT B032=BIB L033=R033LIVE R033=MANIFEST
V040P=REPLAY V040Q=REPLAY R041=SNAPSHOT R042=SNAPSHOT R043=SNAPSHOT C043=RECORDER R044=MANIFEST
V050P=REPLAY V050Q=REPLAY R051=SNAPSHOT R052=SNAPSHOT R053=SNAPSHOT C053=RECORDER R054=MANIFEST
F055=SOURCEFINAL F061=PDFINFO F063=PDFTEXT F064=PDFRAW F065=LOGBIB I066=STAGEINV
```

The exact 51-ID root-stage timeline is:

```text
A000 R000 R001 R002 R003 R004 R005 R006 R007 R008
R009 V020P R020 V020Q R021 R022 R023 C023 R024
V030P R030 V030Q R031 R032 B032 L033 R033
V040P R040 V040Q R041 R042 R043 C043 R044
V050P R050 V050Q R051 R052 R053 C053 R054
F055 R060 F061 R062 F063 F064 F065 I066
```

The only handler-created stage payloads are the eleven snapshots and five
manifests listed below, each at its same-numbered handler.  At receipt-guard
open, the exact stage set is the completed-name prefix plus the current
`ID.stdout` and `ID.stderr`; both streams are empty regular mode-0600 link-one
files and `ID.status` is absent.  After a successful SNAPSHOT or MANIFEST
handler, its one frozen current destination basename is the sole additional
stage payload admitted before emission; no other mode adds a stage payload.
Every later success check uses that terminal exact set.  At receipt-guard open,
file descriptors 1 and 2 are write-only, non-append, offset-zero bindings to
the two distinct streams.  Each later check requires each descriptor offset to
equal the complete currently expected stream length: both are zero before
emission; after emission fd1 equals the exact stdout byte length and fd2 remains
zero.  Before and after emission the guard rechecks names, held identities,
complete stdout bytes, empty stderr, and absent status.  The wrapper alone adds
`ID.status` with `0<LF>` after a successful validator return.

The eleven exact snapshot basenames are:

```text
R021--main.log.snapshot
R022--main.aux.snapshot
R023--main.fls.snapshot
R031--main.bbl.snapshot
R032--main.blg.snapshot
R041--main.log.snapshot
R042--main.aux.snapshot
R043--main.fls.snapshot
R051--main.log.snapshot
R052--main.aux.snapshot
R053--main.fls.snapshot
```

The five exact manifest basenames are:

```text
R009--root.manifest
R024--root.manifest
R033--root.manifest
R044--root.manifest
R054--root.manifest
```

Thus each root stage's pre-`I066` complete-name frame has 166 names, 2,188
bytes and SHA-256
`978bc704ad9d6aa48dedccc799d540c5266902c48c5dde89f41579a92d7b158a`;
the `STAGEINV` call adds empty `I066.stdout`/`.stderr` while status remains
absent, giving 168 names, 2,212 bytes and SHA-256
`3b8e6e3c8967800e227ee9894250c9938e81739074997bfb857d59efd4a30225`.
The completed post-`I066` frame has 169 names, 2,224 bytes and SHA-256
`ff59cd1d01a709db334b2c631509cd781315e1538ee210ed4b00f217c8682c87`.
All frames are sorted `basename<LF>`.

The exact evidence-root receipt IDs are `E001 E010 E011 E012`; their twelve
suffix-expanded receipt basenames, `BUILD_VALIDATOR_SUCCESSOR.py`, and stage
names `r0`, `r1`, `cross-root` form the final 16-name, 190-byte sorted frame
with SHA-256
`fdf7265843cb9d94f1d40636fa7d97fcdd9ed7813f2f0addd0675cd64c452cc3`.
At root-0 `ABSENT`, the exact evidence set is only validator copy, `r0`, and
the six E001/E010 receipts: 8 names, 104 bytes, SHA-256
`fcfb786df5f7515f180712ab94df53b53528c980b7ecaaad75df8e554ef15231`.
At root-1 `ABSENT`, it is validator copy, `r0`, `r1`, and the nine
E001/E010/E011 receipts: 12 names, 143 bytes, SHA-256
`c1233539586dab7650ecc67a650f58a8b727be4d943af64474b71295f37861c8`.

The cross stage first has completed silent cmp receipt IDs `X001`--`X008`:
24 names, 288 bytes, SHA-256
`f7955686bbf2ec63609cb2f62ff3232c8d1124eeedced5c9ccc3dac16b409dae`.
The `CROSS` call adds empty `X009.stdout`/`.stderr` with absent status, giving
26 names, 312 bytes and SHA-256
`c2336c6ccdee97ad87e6e900d78cea7c13c44dda2e2af010e19d26736e938db1`.
Its completed receipt gives the pre-evidence 27-name, 324-byte frame with
SHA-256
`5a555210ef205d8abe3802f360d1a8ab3bdeeaf409e8a20fa5b1d1e467d9c7a9`.
The `EVIDENCE` call sees those 27 completed names plus empty
`X010.stdout`/`.stderr` and absent `X010.status`, exactly the 29-name,
348-byte frame with SHA-256
`030998e8dedc74d1707d23265d532c639ca42eae31e03fe03d32e811cb7b7902`.
It preserves those in-flight files empty throughout its handler; after it
returns, main emits and rechecks complete X010 stdout while status is still
absent.  The wrapper's final `X010.status` is the sole later addition, yielding
the 30-name, 360-byte final frame with SHA-256
`b4eb3603cba6c9260db671175c0c549a25dfd8fde928f1d40f4da32ca629ae64`.

Validator stdout is not accepted by a prefix-only test.  Each of the fifteen
modes has one exact ordered field-name tuple; the parser requires a single
printable-ASCII LF-terminated line, exactly the mode's complete token census,
canonical decimal and SHA-256 grammars, and field-specific enumerations.  It
rejects missing, extra, reordered, duplicate, empty, control-byte, or
noncanonical fields.  The exact ordered tuples are:

```text
ABSENT root absent stage_empty dependencies
REPLAY root checkpoint root_rows root_sha256 dependencies
SNAPSHOT root id bytes LF sha256
MANIFEST root id rows bytes sha256
RECORDER root id bytes LF sha256 normalized_sha256 local_inputs local_outputs external_unique
R033LIVE root bytes LF sha256
BIB root items bbl_sha256 blg_sha256
LOGBIB root sentinel pages warnings warning_sha256 disposition warning_bytes_hex log_sha256 aux_sha256 bbl_sha256 blg_sha256 pdf_sha256
PDFINFO root pages bytes pdf_sha256
PDFTEXT root pages reference_page text_sha256 pre_reference_sha256
PDFRAW root pages fonts descriptors font_streams streams bytes sha256
SOURCEFINAL root source_files root_rows manifest_sha256
CROSS raw_pairs recorder_pairs manifest_pairs projected_fields recorder_sha256 manifest_sha256 sentinel pages warnings aggregate_sha256
STAGEINV stage items framing_bytes inventory_sha256 root_manifest_sha256
EVIDENCE pre_X010 root_entries r0_items r1_items cross_items inventory_sha256
```

Each `_inventory_stage` call preflights all completed names and, when
`inflight_ident` is supplied, the two corresponding in-flight streams;
supplied in-flight streams must be empty.  It reads each completed regular
file once into a content cache and separately records
size/LF/stat-key/hash in an identity cache.  Receipt, snapshot, manifest,
recorder, bibliography, replay, final-source, and parsed-validator bindings
use cached stage bytes.  Final semantic recomputation consumes only cached
R060/R062 receipts while reading the held live FINAL-root products and binding
them to cached R054.  Each completed stage file is then reopened and streamed
under a held no-follow FD, must reproduce the cached identity, exact names are
relisted, and any supplied in-flight streams are rechecked empty before close;
outer receipt, universe, and identity holds remain in force.

## 7. Semantic predicate binding

`RECORDER` accepts only `PWD`, `INPUT`, and `OUTPUT` rows.  PWD is exactly the
selected root; the strict UTF-8/LF recorder is capped at 8 MiB, 200,000 lines,
and 16 KiB per line.  Root-local input basenames are `main.tex`,
`math_commands.tex`, optional/required `main.aux` by pass, and required
`main.bbl` on R043/R053.  The exact output set is `main.aux`, `main.fls`,
`main.log`, `main.pdf`.  Every external input is in the frozen logical/final
dependency union and the external set must be nonempty.  R023/R043/R053
root-prefix replacement by the literal
`<ROOT>` is the sole content normalization.

`BIB` and `LOGBIB` bind the exact twenty-key set:

```text
abboud_xie_2026 bedford_kim_2008 berger_turaev_2025 bianchi_dinh_rakhimov_2024
blanc_van_santen_2022 cheng_wang_yu_1994 dang_favre_2021 deserti_2018
el_hilany_2024 favre_wulcan_2012 fordy_hone_2011 gomez_meiss_2004
grigoriev_containment hasselblatt_propp_2007 janeczko_jelonek_2008
koch_lomeli_2014 nisse_2026 shafikov_wolf_2003 shao_sun_2025 takenawa_2026
```

The source cite set, BibTeX entries, final aux citations, aux bibcite keys and
labels 1--20, and bbl items each equal it with census 20 and no duplicate.
The ordered closed `plain.bst` BBL item at position `i` must have the same key
as the unique aux `\bibcite{key}{i}` row; a permuted key/label map fails even
when all unordered sets agree.  The AUX parser has a closed control allowlist,
rejects dynamic controls, binds `@abspage@last` to the PDF page count, and
admits only the bounded frozen TOC/LOF/LOT/newlabel/longtable surfaces.  The
BLG parser requires the exact frozen BibTeX version/capacity/top-aux/style/
database/20-entry line schema, the fixed ordered built-in counter rows, a
closed counter total, and `warning$=0`.  `BIB` also requires live BBL/BLG bytes
to equal their R031/R032 snapshots.

The final log has exactly one positive output line and exactly one
`BATCH07_REFERENCE_START_PAGE=N`; `N-1` is 24--28, log pages/bytes equal
pdfinfo/raw PDF, and total pages are at least N.  It rejects the complete
profile list of errors, undefined labels/citations, multiply-defined labels,
missing characters, emergency/fatal stops, overfull boxes, rerun requests,
destination collisions, PDF-string tokens, font substitution, and any
shell-escape/write18-enabled evidence.  Any
remaining warning that is not a pure underfull line fails.  Pure underfull
lines are emitted in the single receipt line as a count/hash and reversible
exact-byte hexadecimal frame, with the explicit `benign-underfull-only`
disposition, and must agree across roots.

`PDFINFO` requires unencrypted PDF 1.5, positive pages/size, size equal raw
bytes, letter `612 x 792` portrait, rotation zero, creator `TeX`, producer
`pdfTeX-1.40.22`, both dates `D:19700101000000Z`, and negative custom-
metadata, metadata-stream, user-property, suspect, form, and JavaScript
flags.  `Tagged` and `Optimized` are `no`; Subject and Keywords are empty.
Title is empty or the exact article title; Author is empty or `Anonymous`.
The printable-ASCII, LF-only, no-tab/no-trailing-space field sequence is
closed and ordered.  Title, Subject, Keywords, and Author are optional and
their absence is treated as the empty value for the allowed-value checks.
BOM, CR, NUL, duplicate fields, a missing required field, an extra field, or
a schema-order violation fails.

`PDFTEXT` splits only at form feeds and removes only one final empty segment.
It requires exact form-feed/page census, strict UTF-8, bounded physical lines,
and rejects BOM, replacement characters, C1 controls, Unicode line separators,
and invalid controls.  It binds reference-page index N, forbids a blank
proof-content page, and requires page-one title/Anonymous/Abstract.  Its
collapse operation recognizes only the frozen ASCII whitespace set.  Before N
it requires the exact eight headings in their tuple order and, independently,
the exact six module anchors in their tuple order.  It also requires all five
theorem clauses, fixture IDs `P1 P2 P3 Q1 Q2 Q3`, all seven boundary names,
and the exact conclusion anchor, without imposing an additional relative order
on those latter anchors.  None of any of these anchors may occur in the
reference suffix.  The suffix has exactly whitespace-followed labels
`[1]`--`[20]` and
rejects every other leading bracketed decimal.  Frozen provenance/path tokens
and a case-insensitive email grammar fail everywhere.

`PDFRAW` reads one regular mode-0600 link-one PDF capped at 64 MiB and
requires the exact PDF-1.5 header, including one four-byte binary-comment
line, followed only by PDF layout bytes before the first direct object.
Direct objects have unique positive bounded object numbers, generation zero,
line-anchored `obj`/`endobj` frames, layout-only inter-object gaps, and an
exact census bounded by 100,000 objects.  A same-length mutable structural
copy masks comments, literal and hex-string contents, and every stream
payload.  Its full-document keyword census is online, admits at most
2,000,000 tokens, and does not materialize a full-document token tuple.
Parsed object-graph tokens have a separate aggregate 2,000,000-token budget;
atoms and names are at most 4,096 bytes, decoded literal/hex strings at most
64 KiB, and object containers at most depth 64.  Structural object,
stream-prefix, compressed-object, and trailer names containing `#` fail.

Every stream is located outside comments and strings and bound to the most
recent real line-anchored generation-zero object header.  The bytes between
that header and `stream` are capped at 256 KiB and must parse as one dictionary
containing one direct canonical nonnegative `/Length`.  Payload extent,
required LF or CRLF framing, `endstream`, enclosing `endobj`, and layout-only
gaps are rebound exactly.  Indirect lengths, duplicate keys, ambiguous
dictionaries, overlapping objects, unbound markers, and lone-CR structural
line endings fail closed.

The complete raw-byte complement of verified font-program payload ranges,
including compressed nonfont payloads, is checked for `/Encrypt`, the frozen
active-content tokens, and every frozen internal provenance, path, host,
lock, role, and candidate token.  The same forbidden set is checked in raw
and semantically decoded literal strings, hex strings, and escaped names in
every direct nonstream object, stream dictionary prefix, decompressed
object-stream member, and traditional trailer.  Comments cannot hide a raw
forbidden sequence.  Parsed dictionaries reject resolved `/Type /Action` and
every `/S` value in the frozen action-name set.  Content-stream names are not
subject to the structural blanket `#` rejection; every `#xx` escape is
instead decoded before its forbidden-token check.

Direct objects and Flate-only object streams are reconstructed.  An ObjStm
dictionary has exactly `/Type`, `/Length`, `/Filter`, `/N`, and `/First`;
`/Filter` is `/FlateDecode`, while DecodeParms, Extends, nested ObjStm
members, stream members, duplicate IDs, noncanonical indexes, nonzero first
member offsets, unordered/overlapping extents, or trailing Flate data fail.
Each object stream is capped at 16 MiB decoded and their PDF-wide total at
32 MiB.  Each decoded block is structurally masked and parsed in place, one
object stream at a time.

Exactly one current cross-reference source is admitted: either one
traditional xref table with no compressed objects or one terminal XRef stream
at the exact `startxref` offset.  Trailer and XRef-stream dictionaries have
closed key sets, so `/Prev` and `/XRefStm` are not admitted.  `/Size`, every
direct offset, every compressed container/index pair, every free entry,
object zero, and the complete free chain are closed against the parsed object
set.  There is one structural `startxref`, one exact terminal
`startxref`/`%%EOF` grammar, and exactly one `%%EOF` in the nonfont raw
complement at that terminal position.

The sole Root resolves to the sole Catalog, whose dictionary is exactly
`/Type` and `/Pages`.  Catalog/Info reachability plus physical ObjStm and XRef
roots partitions the complete object set: every semantic object is reachable,
every compressed object is semantically reachable, and no physical container
is semantically reachable.  Closed Page/Pages dictionaries form one bounded
acyclic tree with unique children, exact parent backreferences and `/Count`,
equality between all Page/Pages objects and their reachable sets, and page
census equality with PDFINFO.  Every page inherits at least one exact rational
`[0 0 612 792]` MediaBox; every present Rotate is exact rational zero; every
selected Resources value is an indirect nonstream dictionary; and every page
has exactly one nonempty indirect content-stream reference.  The last rule is
a conservative fail-closed acceptance condition, not a claim that an upstream
contract preproved the cardinality.

All streams are partitioned without collision or remainder into content,
embedded FontFile, ObjStm, and the optional XRef stream.  Parsed inbound
multiplicity to each content stream equals its Page `/Contents` edges;
multiplicity to each font stream equals its descriptor `/FontFile` edges;
ObjStm and XRef streams have no semantic inbound edge.  XObjects, metadata,
ToUnicode, images, embedded files, and every other unclassified stream role
therefore fail the frozen closure.

Each content-stream dictionary has exactly `/Length` and optional `/Filter`;
the only filter is `/FlateDecode`, with no DecodeParms.  Each decoded stream
is capped at 16 MiB, the unique-stream decoded total at 64 MiB, and aggregate
lexical work at 2,000,000 tokens.  The scanner validates balanced arrays and
dictionaries to depth 64, 4,096-byte atoms/decoded names, and 64-KiB decoded
literal/hex strings.  It checks raw bytes and decoded strings/names against
the full forbidden set, rejects a top-level inline-image `BI`, and carries a
rolling forbidden-token match across all string operands of a top-level `TJ`
array, including strings separated by numeric adjustments.

The frozen font scope is exactly all `/Type /Font` objects reachable through
selected page-resource Font dictionaries.  Every resource Font entry is an
indirect reference; every Font object is subtype `Type1`, has a bounded
BaseFont name, has no DescendantFonts, and has one indirect FontDescriptor.
Every FontDescriptor object is in that closure, its FontName equals each bound
BaseFont name, and among `/FontFile`, `/FontFile2`, and `/FontFile3` it has
exactly one nonempty `/FontFile`.  The FontFile stream dictionary contains
exactly `/Length`, `/Length1`, `/Length2`, `/Length3`, and optional `/Filter`;
the only filter is `/FlateDecode`, DecodeParms is absent, and stream `/Subtype`
is absent.  A shared stream is admitted only when every descriptor gives the
same `(FontFile, Type1, FontName)` binding, and each unique stream is validated
once.  Embedded Type1 FontName must equal descriptor and BaseFont names.

Each decoded Type1 program is capped at 16 MiB and the PDF-wide unique-program
decoded-byte budget is 64 MiB.  Length1 cleartext is at most 1 MiB, Length2
eexec at most 16 MiB, and Length3 tail at most 64 KiB.  PFA lengths partition
the payload exactly; PFB admits only exact type-1/type-2 with optional final
type-1 segment and one terminal type-3 marker, with segment lengths rebound to
Length1/2/3.  Cleartext has the admitted Type1 signature and closed font,
FontInfo, Encoding, matrix, box, and field productions.  Binary or ASCII-hex
eexec is decrypted while discarding the first four decrypted eexec bytes and
has exact Private/CharStrings closure, one admitted RD/ND/NP or `-|`/`|-`/`|`
macro family, the frozen
OtherSubrs template, bounded allocation operands, and only closed PostScript
names/productions.  Dynamic `cvx`, `cvn`, `token`, `run`, and unapproved
`exec` contexts fail.  Raw cleartext, decrypted nonbinary eexec spans, and
tail are checked for forbidden semantic tokens; every PostScript literal and
hex string is decoded before that check.  Binary Subr/CharString spans are
claimed exactly once and decoded under lenIV in the closed Type1 charstring
grammar rather than treated as text.

PDF-wide Type1 budgets are 4,000,000 lexical tokens, 2,000,000 CharString
tokens, 4,000,000 concrete steps, and 4,000,000 abstract steps.  A font has
at most 512 Subrs and 4,096 glyphs, exactly one `.notdef`, and at most 16 MiB
of Subr-plus-glyph bytes.  Every stored glyph is concretely executed with a
24-value operand stack, call depth at most 16, at most 100,000 steps, one
initial width operator, exact arities, approved OtherSubrs/pop flow, and a
role-correct terminal.  Every recursively reachable Subr receives those
concrete checks.  Every Subr has lexical closure; an unreachable Subr is inert
data and is admitted only when the bounded abstract fixpoint finds at least
one stack-I/O contract.  The local fixpoint is capped at 2,000,000 steps and
4,096 states in addition to the PDF-wide aggregate.

The preceding predicates are a structural and bounded-execution boundary, not
a font-provenance proof.  Subject to the external premises in Section 1,
PDFRAW establishes for each root the closed PDF/Type1 structure, the
fail-closed finite execution profiles for admitted Type1 programs, and
embedded FontName/BaseFont/FontDescriptor name consistency.  CROSS separately
establishes raw two-root PDF equality and equality of the complete recomputed
semantic summaries.  Neither PDFRAW nor CROSS compares an embedded
`/FontFile` program or its glyph outlines with any particular dependency-lock
`.pfb` input; matching names and two-root equality do not establish that
lineage.

Glyph-outline provenance from the exact frozen dependency `.pfb` bytes through
the build into the embedded Type1 programs is supplied externally by the
frozen dependency capsule together with the deterministic two-root build and
the cross-process continuity premise.  It is not inferred from structural
Type1 parsing, bounded execution, name consistency, or output equality.

The live-buffer discipline is algorithmic, not an operating-system RSS limit.
Raw analysis holds at most the 64-MiB PDF and one same-size structural copy
while constructing the graph; the structural copy is released before content
and font validation.  Stream-dictionary copies are at most 256 KiB.  ObjStm
blocks are decoded/mutated in place one at a time; content and unique Type1
programs are decoded one at a time.  The raw complement is range-scanned, so
no third whole-PDF font-masked copy exists.  In stage inventory, the bulk
cache is discarded after receipt/binding checks; only R060/R062 survives into
the final summary, both are consumed there, and PDFTEXT/bibliography buffers
are released before raw PDF input.  CROSS releases each recorder/normalized
pair per iteration; EVIDENCE retains only its separately bounded evidence and
cross caches while stage inventories run serially.

`CROSS` first rebinds controls, validator source/copy equality, and both root
source-copy trios.  It requires raw equality of the source trio, PDF, aux,
bbl, blg, and log;
normalized equality of R023/R043/R053; and the five manifest pairs.  R009 is
raw-equal.  In each later pair only the raw SHA field of `main.fls` may differ;
the snapshot rebinds bytes/LF/mode/link/hash, its sole root-prefix-normalized
hash replaces that one field in memory, and the projected frames match.  No
projection file is written.  Its one-line receipt directly prints both-root
hash pairs for all three normalized recorders and all five raw/projected
manifest pairs, and the aggregate covers the eight raw comparisons, both
members of all recorder pairs, and both members of all manifest pairs.  Final
sentinel/pages/warnings and warning frame, every PDFINFO field, the PDFRAW
five-count tuple, decoded/pre-reference text hashes, receipt hashes, final
identity rows, and all raw product hashes match.
Before returning its detail, CROSS relists both root stages and the cross
stage, repeats all eight raw pairs, all three recorder pairs, all five
manifest projections and row counts, both final-root/R054 frames, both full
semantic summaries, and all eight cmp receipt triplets; every terminal value
must equal its first captured version.

`SOURCEFINAL` rehashes controls, validator source/copy equality, live
source/root copies, exact final-root universe, and R054 binding.  `STAGEINV`
enumerates and hashes every exact pre-I066 receipt/snapshot/manifest and
validates all receipt grammars.  After cache-level binding it retains only
R060/R062; final semantic recomputation consumes those receipts while reading
the held live final log/aux/bbl/blg/PDF and binding every product identity
directly to R054.
Both SOURCEFINAL and STAGEINV repeat their live final-root/R054 comparison
after intervening manifest or inventory work and require the terminal bytes
to equal the initial frame.

`EVIDENCE` checks control/source and validator source/copy equality, both
live final-root/R054 rebindings, exact evidence/stage name sets and every
evidence-root receipt identity, receipt grammars, both post-I066 root-stage
inventories, and the 27 completed plus two empty in-flight pre-X010 cross
files.  X009 stdout must equal the fresh, exact `_cross_analysis` result
byte-for-byte, not merely its prefix.  Initial, terminal, and ultimate
checkpoints repeat both complete stage inventories, the whole pre-X010 cross
cache, and all evidence-root regular/child identities.  Initial and terminal
checkpoints separately regenerate both live final-root frames, reread both
R054 manifests, and require each pair and both versions to agree.  The outer
held root and stage universes then preserve those identities through the
ultimate checks, terminal recomputation, report emission, and final hold
rebind.  X010 stdout/stderr remain empty throughout the handler.  Every
terminal value must equal the first cached version before PASS; no evidence
path is discovered from an enumeration result.

## 8. Result grammar, exit codes, and author static audit

Immediately before PASS encoding, `_terminal_recompute` runs under all held
universes and identities.  SNAPSHOT is terminally rebound by rereading its live
source and created destination and reproducing the exact detail; MANIFEST
regenerates the root frame, rereads the destination, repeats the transition
check and destination version check, and reproduces the exact detail.  Each of
the other thirteen modes invokes its complete handler a second time.  In every
mode the terminal detail must equal the first detail exactly before PASS can be
encoded.

A complete successful invocation writes and fsyncs exactly one printable-ASCII
LF-terminated `PASS MODE fields...` line, preserves empty stderr, passes every
post-emission runtime/identity/control/hold/receipt check, and returns 0.
`CheckFail` returns 1; `UsageFail` and caught `Exception` contract failures
return 2.  Before PASS, a guarded failure is a fully validated guarded FAIL
receipt only when its complete `FAIL predicate=`, `FAIL usage=`, or
`FAIL internal=` line, empty receipts, write, two-FD fsync, and readback all
succeed; complete bytes may already have been written if a later validation
step fails.  Before a guard is expected, a usage or internal failure makes one
unguarded `_write_stdout` attempt, without fsync or readback; complete, partial,
or zero stdout may result, always with nonzero exit.  Failure while opening an
expected guard may likewise return nonzero with zero stdout.  Failure after a
complete PASS emission can leave PASS bytes but returns nonzero; it is not
success.  Therefore, conditional on the external trust-root and cross-process
continuity premises in Section 1, validator-invocation acceptance is the
conjunction of exit/status 0, exact mode stdout, empty stderr, and all receipt
bindings, never stdout text alone.  This invocation-level conjunction does not
discharge the external font-provenance obligation in Section 7.  An incomplete
stdout emission, a zero/negative `os.write` result, or an `OSError` encountered
by `_write_stdout` cannot return 0; positive short writes are continued until
the complete frame is written.

The author performed zero-execution byte, text, and AST checks; no validator
import, built-in compile, or invocation was used.  `ast.parse` succeeded.  The
source has 267 top-level functions, ten nested helpers (277 functions total),
two exception classes, and nine lambdas.  Imports are exactly the nine modules
listed in Section 2.  `MODE_ARITY`, `MODE_HANDLERS`, and
`VALIDATOR_RESULT_FIELDS` have the same 15 keys; `EXACT_ARGV_ROWS` has 74
members and the root-stage timeline has 51 IDs.  Map censuses are snapshot
22, manifest 10, recorder 6, R033-live 2, bibliography 2, final-root 2, and
replay-checkpoint 8.  The 36-entry receipt-mode map covers 35 pre-inventory
validator IDs plus `I066`; its 27-entry second-field map covers eight replay,
eleven snapshot, five manifest, and three recorder receipts.

The dependency literal independently reproduces the 87-row, 23,408-byte,
87-LF frame and its frozen hash.  Source/BibTeX controls yield 20 distinct
expected cite keys and 20 matching entries.  AST inspection finds no bare
`eval`, built-in `exec`, built-in `compile`, `__import__`, subprocess, glob,
`os.walk`, `os.path.realpath`, `os.remove`, `os.unlink`, `os.rename`,
`os.replace`, or `os.truncate`.  There is one reviewed `os.scandir` artifact
census and one reviewed `/proc/self/fd` `os.listdir` census.  The two ordinary
`replace` calls are recorder-root normalization and diagnostic space mapping;
the one `remove` spelling is a set method, not a filesystem operation.  Direct
absolute `os.open` literals are the two `/` anchors and the two reviewed proc
paths; relative leaves use frozen basenames and held directory FDs.  The exact
standalone terminal marker occurs once and is the final source line.

The frozen source identity in Section 1 received three independent final
static reviews with zero Blocker, Major, Minor, or Ambiguity findings.  Those
reviews did not execute, import, compile, or mutate the validator.

Any independent finding, runtime drift, unsafe operation, omitted predicate,
path or basename not bound here, lock/source mismatch, or ambiguity is
`FAIL_WRITE_NOTHING`.  No validator execution, build/evidence mutation, PDF
release, later-paper action, network access, or external effect follows from
this author lock.

BATCH07_P27_VALIDATOR_LOCK_SUCCESSOR_AUTHOR_STOP
