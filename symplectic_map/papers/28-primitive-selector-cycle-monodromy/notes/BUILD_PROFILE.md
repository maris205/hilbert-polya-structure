# Paper 28 deterministic build profile — revision R1

## Authority, revision disposition, and effect boundary

Candidate: `primitive_selector_cycle_monodromy_v1`  
Controlling revision authority: `B07-E0209-P28-BUILD-PROFILE-REVISION-R1-AUTHORIZATION`  
Consumed failed-review marker: `BATCH07_PAPER28_BUILD_PROFILE_REVIEW_R1_FAILED_WRITE_NOTHING`  
Profile role: `batch07-p28-build-profile-revision-author-r1`  
Profile-time compiler, BibTeX, cache, PDF, or scientific execution: none  
Profile-time build/future-path probe: none  
External effect: none

This revision replaces the earlier protocol at this exact path.  It closes the
two Blockers, three Majors, one Minor, and one Ambiguity recorded in E0208.
It is a protocol only: it creates no build parent, evidence path, discovery
root, certified root, dependency byte, auxiliary file, PDF, release copy, or
external effect.  None of the future paths named below was listed, lstat'ed,
tested for existence, entered, created, or otherwise probed while this
revision was written.

A wholly fresh R2 reviewer must return an unconditional all-zero
`BATCH07_PAPER28_BUILD_PROFILE_PASS` before any executable build action or
future-path observation is authorized.  This profile never grants build,
finalization, release, upload, submission, hosting, messaging, or identity-
disclosure authority by itself.

## One literal workspace and complete absolute path map

There is exactly one administrative working directory:

```text
/root/autodl-tmp/symplectic_map
```

Every administrative capsule below first changes to that literal directory.
No relative project, source, build-parent, root, dependency-list, evidence,
or inspection path is used.  The complete future path map is:

| Role | Literal absolute path | Required type/mode |
|---|---|---|
| workspace cwd | `/root/autodl-tmp/symplectic_map` | pre-existing directory; separately bound by the build gate |
| project | `/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy` | pre-existing directory |
| live main source | `/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/main.tex` | regular 0644, link one |
| live macro source | `/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/math_commands.tex` | regular 0644, link one |
| live bibliography | `/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/references.bib` | regular 0644, link one |
| build parent | `/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build` | created once as directory 0755 |
| durable evidence root | `/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831` | created once as directory 0700 |
| non-release dependency-discovery root | `/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/dependency-discovery-r1-20260831` | created once as directory 0700 |
| certified root 0 | `/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831` | created once as directory 0700 |
| certified root 1 | `/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831` | created once as directory 0700 |

The discovery root is not either certified root, is never copied into a
certified root, and can never supply a PDF for release.  The two certified
roots are fresh isolated siblings and receive independent copies from the
live trio.  Root 1 is not copied from root 0.  No replacement root exists.

The build parent and evidence root are bootstrap objects.  A later explicit
dependency-discovery authorization must first perform a no-follow absence
check on the exact build-parent path.  If it is present in any form, the
action history fails; there is no cleanup or reuse.  On absence, the exact
parent-creation command is:

```text
/usr/bin/mkdir -m 0755 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build
```

Its status must be zero, its combined stdout/stderr must be the zero-byte
string, and its immediate no-follow result must be one directory of mode
0755.  The next exact command is:

```text
/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831
```

It has the same zero-status/zero-console requirement and an immediate
directory-mode-0700 check.  Because no evidence directory can exist before
these two commands, their sole durable receipt is the exact physical ledger
event that authorized them: it must record command IDs `BOOT-000` and
`BOOT-001`, the literal command bytes, empty-console SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`,
console bytes zero, raw status zero, post-lstat fields, and the parent-ledger
hash.  This named ledger receipt is the only bootstrap exception.  If either
command emits one byte, exits nonzero, or cannot be fully recorded, the
stage stops before any root and no later receipt may backfill it.

All later durable receipts live below the evidence root and outside every
discovery/certified root.  The whole `build/` subtree remains excluded from
the canonical source/control manifest and is bound only by the build-evidence
manifests defined here.

## Immutable live source and terminal rebinding

The sole scientific inputs are:

| Literal path | Bytes | LF | Mode | Links | SHA-256 |
|---|---:|---:|---:|---:|---|
| `/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/main.tex` | 73,733 | 1,605 | 0644 | 1 | `bdc7a1edc06b3f8cfc75c6b47a8c24180883d24eef878c70d857588d19f1762e` |
| `/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/math_commands.tex` | 444 | 14 | 0644 | 1 | `16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5` |
| `/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/references.bib` | 6,104 | 204 | 0644 | 1 | `e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e` |

Each is a regular non-symlink, strict-UTF-8/LF file with no BOM, CR, or NUL
and exactly one terminal LF.  The controlling fresh source review is
`/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/notes/INDEPENDENT_SOURCE_REVIEW.md`,
25,100 bytes, 531 LF, SHA-256
`bfa264202de33ae63c0910eeafe4c90968f85515179456ab44b10fcf91dfe750`.

The live trio is lstat'ed and rehashed at six mandatory boundaries: before
the discovery copies, after dependency discovery, before root-0 copies,
after root 0, before root-1 copies, and after every root-1 command and final
inspection has completed.  The last of these is the terminal live-source
census and occurs before cross-root acceptance.  Every census must reproduce
all fields above.  A changed byte, mode, link count, type, encoding, or line
ending is terminal; later PDF equality cannot cure it.

## Fully bound administrative and publication toolchain

E0209 authorized only read-only administrative discovery.  The resulting
invocation paths, symlink chains, resolved regular targets, and target
identities are frozen below.  A regular invocation path is its own target.
All modes are octal and every resolved target has link count one.

| Program role | Absolute invocation and lstat chain | Final regular target; bytes; mode; SHA-256 | Exact version identity |
|---|---|---|---|
| empty environment | `/usr/bin/env` regular | `/usr/bin/env`; 43,976; 0755; `85036540673319c6c2f54233fd2b9e45a8a71246b51cc96c4e6ab8ee6c419eb0` | GNU coreutils 8.32 |
| administrative shell | `/usr/bin/bash` regular | `/usr/bin/bash`; 1,396,520; 0755; `59474588a312b6b6e73e5a42a59bf71e62b55416b6c9d5e4a6e1c630c2a9ecd4` | GNU bash 5.1.16(1)-release, x86_64-pc-linux-gnu |
| directory creation | `/usr/bin/mkdir` regular | `/usr/bin/mkdir`; 68,104; 0755; `bd2f081ac37d653181332bd27f35a6041dbf215a7957f65838a9cbec9e64928b` | GNU coreutils 8.32 |
| byte copy with mode | `/usr/bin/install` regular | `/usr/bin/install`; 145,944; 0755; `519a00d199d07da6028ec5a9800d92c562934582a2ea1793b2cbc378a85c1439` | GNU coreutils 8.32 |
| administrative validator | `/root/miniconda3/bin/python3` symlink of 10 bytes to `python3.12` | `/root/miniconda3/bin/python3.12`; 30,626,264; 0755; `9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101` | Python 3.12.3 |
| metadata | `/usr/bin/stat` regular | `/usr/bin/stat`; 80,400; 0755; `9b571b54bd2f17f5fbb841e1886c2d364f5138a02533f4ac3dbfbdaf4dddbea3` | GNU coreutils 8.32 |
| hashing | `/usr/bin/sha256sum` regular | `/usr/bin/sha256sum`; 51,624; 0755; `7645c8e76d75515ccb75c9086bdcf0d4071f2985f380f249253ead7d7c6810b3` | GNU coreutils 8.32 |
| raw comparison | `/usr/bin/cmp` regular | `/usr/bin/cmp`; 43,408; 0755; `b355472d3c90ea94d11ebb8b750e6946ccd348edc6fca4aefc1235c3994ef791` | GNU diffutils 3.8 |
| pdfLaTeX | `/usr/bin/pdflatex` symlink of 6 bytes to `pdftex` | `/usr/bin/pdftex`; 1,802,504; 0755; `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` | pdfTeX 3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian; kpathsea 6.3.4/dev; libpng 1.6.37; zlib 1.2.11; xpdf 4.03 |
| BibTeX | `/usr/bin/bibtex` symlink of 24 bytes to `/etc/alternatives/bibtex`, itself a 24-byte symlink to `/usr/bin/bibtex.original` | `/usr/bin/bibtex.original`; 117,128; 0755; `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` | BibTeX 0.99d, TeX Live 2022/dev/Debian; kpathsea 6.3.4/dev |
| TeX lookup | `/usr/bin/kpsewhich` regular | `/usr/bin/kpsewhich`; 27,960; 0755; `ae30057832d4870b13d3abcbf10187b538dc3439afff15d624a65b920dc7911b` | kpathsea 6.3.4/dev |
| PDF metadata | `/usr/bin/pdfinfo` regular | `/usr/bin/pdfinfo`; 59,928; 0755; `8ca6e6d0b2e6b3f135a82feb07b3d5750498eb77e6f66412803f425eb8471a8e` | Poppler pdfinfo 22.02.0 |
| PDF text | `/usr/bin/pdftotext` regular | `/usr/bin/pdftotext`; 43,544; 0755; `7de929ce0686af5dbf76975ad08bbff93526b3d9028035176a4ca89d9d19c27d` | Poppler pdftotext 22.02.0 |

The invocation symlink metadata and every resolved target are rebound before
their first use in each stage.  Version stdout/stderr is captured in that
stage.  `/usr/bin/sha256sum` and Python `hashlib.sha256` cross-check each
other against the frozen hashes; their circular observation is anchored by
the E0209 discovery record.  Drift in path, chain, type, bytes, mode, link
count, target, hash, or complete version bytes aborts.  No PATH-selected or
similar-version substitute is allowed.  `latexmk`, `qpdf`, `fc-match`,
`readlink`, `realpath`, `find`, `tar`, `cp`, `tee`, `grep`, `sed`, `awk`,
`perl`, `openssl`, and every other executable are forbidden.

## Literal empty-environment execution capsule

Every external program, including mkdir, install, stat, hash, compare,
Python, TeX lookup, compiler, BibTeX, and PDF inspection, is launched through
the following mechanism.  It is a printed protocol, not an implied wrapper.
For each command row below, `CWD`, `CONSOLE`, `STATUS`, the environment rows,
the absolute program, and every argument are replaced only by the literal
values in that row; no shell expansion chooses a path.

```text
/usr/bin/env -i /usr/bin/bash --noprofile --norc -c '
set -C
umask 077
cd -- LITERAL_CWD || exit 125
/usr/bin/env -i LITERAL_ENV_ROWS LITERAL_ABSOLUTE_PROGRAM LITERAL_ARGUMENTS > LITERAL_CONSOLE 2>&1
rc=$?
printf "%s\n" "$rc" > LITERAL_STATUS || exit 126
exit "$rc"
'
```

The outer `/usr/bin/env -i` gives Bash an empty inherited environment.  Bash
reads no profile or rc file, sets umask 077, and changes to the one literal
workspace cwd or the one literal selected root.  The inner `/usr/bin/env -i`
removes Bash-created variables before the target program and supplies only
the listed rows.  `set -C` makes both receipt redirections fail rather than
overwrite.  The status file grammar is exactly one ASCII decimal integer in
`0..255` followed by LF.  A console file is the unmodified interleaving of
the target's stdout and stderr created by `> LITERAL_CONSOLE 2>&1`.  Both are regular
mode-0600 link-one files.  A failure to create either receipt is itself an
unreceipted-command failure and stops the lifecycle.

For non-TeX administrative commands the exact environment is:

```text
PATH=/usr/bin:/bin
SOURCE_DATE_EPOCH=0
FORCE_SOURCE_DATE=1
TZ=UTC
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
```

TeX, BibTeX, kpsewhich, and root-specific validators receive the preceding
seven rows plus exactly one of the following already expanded five-row sets.
The discovery-root set is:

```text
TEXMFVAR=/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/dependency-discovery-r1-20260831/texmf-var
TEXMFCONFIG=/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/dependency-discovery-r1-20260831/texmf-config
TEXMFHOME=/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/dependency-discovery-r1-20260831/texmf-home
XDG_CACHE_HOME=/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/dependency-discovery-r1-20260831/xdg-cache
TMPDIR=/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/dependency-discovery-r1-20260831/tmp
```

The certified-root-0 set is:

```text
TEXMFVAR=/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/texmf-var
TEXMFCONFIG=/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/texmf-config
TEXMFHOME=/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/texmf-home
XDG_CACHE_HOME=/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/xdg-cache
TMPDIR=/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/tmp
```

The certified-root-1 set is:

```text
TEXMFVAR=/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/texmf-var
TEXMFCONFIG=/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/texmf-config
TEXMFHOME=/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/texmf-home
XDG_CACHE_HOME=/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/xdg-cache
TMPDIR=/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/tmp
```

There is no HOME, USER, LOGNAME, HOSTNAME, PWD, OLDPWD, SHLVL, `_`, proxy,
TeX search-path override, BibTeX search-path override, shell-startup variable,
or inherited entry in the target process.  PATH is present only because some
TeX internals require a conventional value; every program named by this
profile is nevertheless invoked absolutely.  The capsule itself is repeated
verbatim for every command.  An export, parent-shell umask, implicit cd,
pipeline, command substitution, alias, function, here-document not printed in
the build authorization, or unstated orchestrator is forbidden.

## Durable evidence grammar and overwrite prevention

Each stage first creates exactly one fresh mode-0700 evidence directory:

```text
/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/discovery
/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/dependency-binding
/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/certified-r0
/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/certified-r1
/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/cross-root
/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/final
```

They are created only when their stage is authorized; no later-stage path is
probed early.  Because a stage directory cannot contain the receipt for its
own creation, those six creation commands have the following unique receipt
pairs directly in the already-created evidence root:

```text
D001.console / D001.status
B000.console / B000.status
R0E000.console / R0E000.status
R1E000.console / R1E000.status
C000.console / C000.status
F000.console / F000.status
```

Each line means the literal prefix
`/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/`
followed by the printed filename.  The six commands respectively create the
six directories in the printed order above; each console is required empty
and each status is `0\n`.  This mapping is exhaustive and contains no runtime
path choice.

After a stage directory exists, command ID `ID` has the exact suffixes
`/ID.console` and `/ID.status` under its one printed stage path.  A named
snapshot has suffix `/ID--NAME.snapshot`, a canonical table
`/ID--NAME.tsv`, and a stage seal `/ID--stage-seal.tsv`.  The stage-to-ID
tables below are exhaustive; concatenating the already printed literal stage
path and literal suffix is the sole filename grammar.  There is no unnamed
receipt.

Before every command, a no-follow Python `lstat` checks that its console,
status, snapshots, canonical tables, and seal destinations are absent.  The
evidence stage directory must itself have an opening manifest containing no
entry before its first stage-local receipt.  Snapshot creation uses `os.open` with
`O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW`, mode 0600, binary 1,048,576-byte chunks,
`fsync`, close, then byte/hash comparison with the still-openable source.
No snapshot is made with an overwrite-capable operation.  Console/status use
the capsule's noclobber redirections.  Evidence is never written inside a
discovery or certified root.

Every stage seal enumerates its two evidence-root creation receipts plus all
stage-local evidence paths, bytewise-sorted by UTF-8 path bytes, with exact
framing

```text
relative_path<TAB>type<TAB>bytes<TAB>LF-or--<TAB>mode<TAB>nlink<TAB>sha256-or--<LF>
```

where files use `file`, directories use `dir`, binary LF is still the raw
0x0a count, modes are four octal digits, hashes are lowercase hexadecimal,
and directory bytes/LF/hash are `-`.  It records row count, framing byte/LF
count, and aggregate SHA-256.  The stage seal is created with O_EXCL, then a
physical ledger STOP binds its bytes/hash and every preceding console/status.
After that STOP the entire stage directory is immutable evidence.  Missing,
duplicate, overwritten, late-created, or unsealed evidence is terminal.

## Governance-safe dependency-discovery lifecycle

No certified build may discover its dependency universe as it runs.  The
following separate non-release stage is mandatory after profile R2 PASS.

### Discovery-stage authorization and exact initialization

The dependency-discovery authorization may create only the build parent,
evidence root, the literal evidence `discovery` directory printed above, and
the discovery root.  It must not probe either
certified root.  After `BOOT-000` and `BOOT-001`, the exact initialization
commands, each through its own receipt capsule, are:

| ID | Exact operation |
|---|---|
| `D001` | `/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/discovery` |
| `D002` | `/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/dependency-discovery-r1-20260831` |
| `D003` | `/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/dependency-discovery-r1-20260831/texmf-var` |
| `D004` | `/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/dependency-discovery-r1-20260831/texmf-config` |
| `D005` | `/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/dependency-discovery-r1-20260831/texmf-home` |
| `D006` | `/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/dependency-discovery-r1-20260831/xdg-cache` |
| `D007` | `/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/dependency-discovery-r1-20260831/tmp` |
| `D008` | `/usr/bin/install -m 0644 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/main.tex /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/dependency-discovery-r1-20260831/main.tex` |
| `D009` | `/usr/bin/install -m 0644 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/math_commands.tex /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/dependency-discovery-r1-20260831/math_commands.tex` |
| `D010` | `/usr/bin/install -m 0644 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/references.bib /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/dependency-discovery-r1-20260831/references.bib` |
| `D011` | validator `SOURCE_AND_OPENING_MANIFEST` on the live trio and discovery root |
| `D012` | one `/usr/bin/kpsewhich` invocation with the nineteen literal names below, in table order |

Every initialization command above is already a complete literal command.
No downstream expansion, path variable, shorthand, or inferred prefix is
permitted.

The nineteen D012 arguments and required output lines are:

| Argument | Required literal output |
|---|---|
| `article.cls` | `/usr/share/texlive/texmf-dist/tex/latex/base/article.cls` |
| `fontenc.sty` | `/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty` |
| `inputenc.sty` | `/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty` |
| `lmodern.sty` | `/usr/share/texmf/tex/latex/lm/lmodern.sty` |
| `geometry.sty` | `/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty` |
| `microtype.sty` | `/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty` |
| `amsmath.sty` | `/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty` |
| `amssymb.sty` | `/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty` |
| `amsthm.sty` | `/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty` |
| `mathtools.sty` | `/usr/share/texlive/texmf-dist/tex/latex/mathtools/mathtools.sty` |
| `bm.sty` | `/usr/share/texlive/texmf-dist/tex/latex/tools/bm.sty` |
| `booktabs.sty` | `/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty` |
| `array.sty` | `/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty` |
| `tabularx.sty` | `/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty` |
| `enumitem.sty` | `/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty` |
| `natbib.sty` | `/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty` |
| `xurl.sty` | `/usr/share/texlive/texmf-dist/tex/latex/xurl/xurl.sty` |
| `hyperref.sty` | `/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty` |
| `plainnat.bst` | `/usr/share/texlive/texmf-dist/bibtex/bst/natbib/plainnat.bst` |

D012 only records names returned by the bound lookup executable.  Neither its
orchestrator nor its validator may lstat, resolve, open, hash, or read any
returned system path at this stage.

### Non-release preflight exception and one-shot discovery commands

The discovery TeX/BibTeX processes are untrusted non-release preflights.  A
separate ledger authorization may allow those processes internally, through
kpathsea, to read root-local files and system files under exactly these four
lexical prefixes:

```text
/usr/share/texlive/texmf-dist/
/usr/share/texmf/
/var/lib/texmf/
/etc/texmf/
```

This is the sole prefix-limited read exception.  It does not authorize the
administrative actor or validator to directly open a newly reported system
path, does not certify the discovery output, and cannot support release.  A
recorder input outside the discovery root or those four prefixes is an
immediate failure.  Network access, package installation, shell escape, a
home tree, `/tmp`, any other project file, and every other prefix remain
forbidden.

From the discovery root, run exactly:

```text
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder -jobname=main '\pdfinfoomitdate=1\relax\pdftrailerid{}\pdfsuppressptexinfo=15\relax\pdfcompresslevel=0\relax\pdfobjcompresslevel=0\relax\pdfminorversion=5\relax\input{main.tex}'
/usr/bin/bibtex main
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder -jobname=main '\pdfinfoomitdate=1\relax\pdftrailerid{}\pdfsuppressptexinfo=15\relax\pdfcompresslevel=0\relax\pdfobjcompresslevel=0\relax\pdfminorversion=5\relax\input{main.tex}'
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder -jobname=main '\pdfinfoomitdate=1\relax\pdftrailerid{}\pdfsuppressptexinfo=15\relax\pdfcompresslevel=0\relax\pdfobjcompresslevel=0\relax\pdfminorversion=5\relax\input{main.tex}'
```

Their IDs are `D020`, `D030`, `D040`, and `D050`.  All statuses must be zero.
Before each next command overwrites a file, the exact snapshots are:

| Completed command | Snapshot IDs and bytes copied outside the root |
|---|---|
| `D020` | `D021--main.log`, `D022--main.aux`, `D023--main.out`, `D024--main.fls` |
| `D030` | `D031--main.blg`, `D032--main.bbl` |
| `D040` | `D041--main.log`, `D042--main.aux`, `D043--main.out`, `D044--main.fls` |
| `D050` | `D051--main.log`, `D052--main.aux`, `D053--main.out`, `D054--main.fls` |

Each listed base name becomes the literal discovery-evidence prefix
`/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/discovery/`
followed by `ID--NAME.snapshot`; each snapshot operation has its own
`ID.console` and `ID.status`.  `D060` creates the
closing discovery-root manifest.  `D061` runs the dependency-list extractor.
`D062` creates the discovery stage seal.

### Exact dependency-candidate extraction and mandatory STOP

The D061 validator reads only D012 console bytes and the three snapshotted
`.fls` files.  It never opens a path named inside them.  It accepts only LF
lines without NUL, CR, tab, or non-UTF-8 bytes.  From each `.fls`, it takes
exactly the bytes after the ASCII prefix `INPUT `; from D012 it takes exactly
the nineteen nonempty output lines.  A path is normalized lexically by
splitting on `/`, rejecting an empty interior component, `.` or `..`, and
rejoining unchanged components with one `/`; no filesystem resolution is
performed.  Root-local paths are recorded separately.  Every external path
must be absolute and begin byte-for-byte with one of the four system prefixes.

The external union is bytewise sorted and deduplicated.  D061 writes exactly
`/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/discovery/D061--dependency-candidates.tsv`,
one row per path:

```text
absolute_path<TAB>source-bitmask<TAB>UNBOUND<LF>
```

The bitmask is a four-character ASCII binary string in the order D012,
D024, D044, D054; a bit is one iff that source named the path.  The file has
one terminal LF unless the union is empty; an empty union is a failure.  Its
row count, byte count, LF count, and SHA-256 enter D062.

After D062 there is a mandatory physical ledger transition
`P28_DEPENDENCY_DISCOVERY_STOP`.  It embeds the complete candidate table as a
literal fenced byte block and binds D001--D062, the discovery-root closing
manifest, and the evidence stage seal.  No system candidate is lstat'ed,
resolved, opened, or hashed before that STOP.  The discovery root is then
permanent evidence-only and its PDF, if any, is noncertified and forbidden
for release.

### Symlink-safe exact-path authorization and content binding

A new ledger event first runs command `B000`,
`/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/dependency-binding`,
using the evidence-root receipt pair frozen above; it then seals an empty
opening manifest for that directory.  The same event may authorize no-follow
lstat only for the literal
candidate paths embedded at the discovery STOP.  For each regular file it
records type/mode/link count but does not read content.  For each symlink it
records only the literal link bytes supplied by lstat.  A relative target is
joined lexically to the symlink's parent and normalized by the same no-dot
grammar; an absolute target is normalized directly.  The newly obtained
target paths are not lstat'ed in that event.  They are written to the exact
path formed by the literal dependency-binding evidence prefix
`/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/dependency-binding/`
and the literal filename `LNN--next-hop.tsv`, sealed, and frozen at a physical
`P28_DEPENDENCY_SYMLINK_STOP_NN`.

A fresh ledger authorization naming every literal next-hop path is required
before its lstat.  The cycle repeats, one physical STOP per hop, with a hard
maximum of eight hops per candidate.  A cycle, dangling target, nonregular
terminal object, device, socket, FIFO, directory-as-input, path outside the
four prefixes, mode with any write bit, or hop nine aborts.  At no point may a
newly discovered target be probed in the same event that discovered it.

Only after all chains terminate in regular files may a new
`P28_DEPENDENCY_CONTENT_HASH_AUTHORIZATION` name every logical path, every
symlink hop, and every final regular target and authorize direct reads of
those exact regular targets.  The binding validator then hashes them and
writes `/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/dependency-binding/B100--dependency-binding.tsv`
with bytewise-
sorted rows:

```text
logical_path<TAB>chain-with-=>TAB>target_path<TAB>bytes<TAB>mode<TAB>nlink<TAB>sha256<LF>
```

`chain-with-=>` is the literal sequence of absolute hop paths separated by
the two ASCII bytes `=>`; it contains no whitespace.  Modes are four octal
digits and hashes lowercase hex.  The table, every lstat console/status, and
the binding-stage seal are frozen in a final physical
`P28_DEPENDENCY_CONTENT_BINDING_STOP`.  A fresh independent binding review
must pass before either certified root.  This staged lifecycle is mandatory;
the discovery STOP cannot be collapsed into content hashing.

## Two fresh certified roots

Only after profile R2 PASS, discovery STOP, every required symlink STOP,
content-binding STOP, and fresh dependency-binding PASS may one exact build
authorization open the certified stage.  Root 0 completes and seals before
root 1 is even checked for absence.  A root-0 failure means root 1 is never
probed or created.

### Literal initialization for each certified root

For root 0, command `R0E000` creates
`/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/certified-r0`
mode 0700 using its evidence-root receipt pair.  Then, and only then, the
literal root-0 path is checked absent.  Root-0 initialization IDs `R000`
through `R008` are the following complete commands in order:

```text
/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831
/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/texmf-var
/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/texmf-config
/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/texmf-home
/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/xdg-cache
/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/tmp
/usr/bin/install -m 0644 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/main.tex /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/main.tex
/usr/bin/install -m 0644 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/math_commands.tex /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/math_commands.tex
/usr/bin/install -m 0644 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/references.bib /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/references.bib
```

Only after root 0 passes and seals, command `R1E000` creates
`/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/certified-r1`
mode 0700 using its evidence-root receipt pair; root 1 had not been probed
earlier.  Root-1 initialization IDs `R000` through `R008` are:

```text
/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831
/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/texmf-var
/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/texmf-config
/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/texmf-home
/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/xdg-cache
/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/tmp
/usr/bin/install -m 0644 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/main.tex /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/main.tex
/usr/bin/install -m 0644 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/math_commands.tex /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/math_commands.tex
/usr/bin/install -m 0644 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/paper/references.bib /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/references.bib
```

The opening validator is `R009` within each root's own evidence stage.  It
requires the root itself
mode 0700/link one; five empty mode-0700 directories; three regular mode-0644
link-one copies exactly equal to the live frozen hashes; and no other entry.
No hard-link alias, symlink, hidden file, special file, nested entry, cache
byte, or receipt is allowed.

### Invocation-time dependency and tool binding

Before and after every one of the four publication commands, validator
`DEPENDENCY_BIND_NOW` reads the immutable B100 table and performs no-follow
lstat of every logical path and hop, then opens and hashes only each listed
final regular target.  Every field must equal B100.  It also rebinds the
invoked executable and both env/bash capsule executables.  The eight receipts
are IDs `R019/R021`, `R029/R031`, `R039/R041`, and `R049/R051`, respectively
before/after TeX 1, BibTeX, TeX 2, and TeX 3.  A dependency change between
pre- and post-checks is terminal.  A later recorder equality never backfills
a missing invocation-time check.

Immediately before each command, the root source copies are also lstat'ed
and rehashed, and the five cache/tmp directories must be empty.  Immediately
after each command, the root is checked for writes outside its permitted
universe and those directories are checked again.  No system path absent
from B100 may be opened by an administrative validator.  If a certified
`.fls` names an extra external path, the validator records only its literal
bytes, does not probe it, and aborts permanently.

### Exact publication sequence and snapshots

Each certified root runs the same four commands through the literal empty-
environment capsule:

```text
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder -jobname=main '\pdfinfoomitdate=1\relax\pdftrailerid{}\pdfsuppressptexinfo=15\relax\pdfcompresslevel=0\relax\pdfobjcompresslevel=0\relax\pdfminorversion=5\relax\input{main.tex}'
/usr/bin/bibtex main
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder -jobname=main '\pdfinfoomitdate=1\relax\pdftrailerid{}\pdfsuppressptexinfo=15\relax\pdfcompresslevel=0\relax\pdfobjcompresslevel=0\relax\pdfminorversion=5\relax\input{main.tex}'
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder -jobname=main '\pdfinfoomitdate=1\relax\pdftrailerid{}\pdfsuppressptexinfo=15\relax\pdfcompresslevel=0\relax\pdfobjcompresslevel=0\relax\pdfminorversion=5\relax\input{main.tex}'
```

Command IDs are `R020`, `R030`, `R040`, and `R050`.  All raw statuses are
zero.  Snapshots are identical in name and timing to discovery, with R IDs:
`R022`--`R025` copy log/aux/out/fls after TeX 1; `R032`--`R033` copy blg/bbl
after BibTeX; `R042`--`R045` copy log/aux/out/fls after TeX 2; and
`R052`--`R055` copy log/aux/out/fls after TeX 3.  Every snapshot is outside
the root and precedes any overwriting command.

There is one BibTeX pass and exactly three TeX passes.  There is no retry,
extra pass, alternate engine, interactive input, shell escape, package
installation, network access, source mutation, qpdf, latexmk, PDF rewrite,
normalization, repair, cleanup, or root reuse.  A nonzero command or receipt
status is terminal.

## Root universes and root-manifest grammar

Before TeX 1, each certified root contains exactly:

```text
texmf-var/
texmf-config/
texmf-home/
xdg-cache/
tmp/
main.tex
math_commands.tex
references.bib
```

After TeX 3, the only additional regular files are:

```text
main.aux
main.bbl
main.blg
main.fls
main.log
main.out
main.pdf
```

The three source files remain 0644/link one.  Every generated file is
0600/link one under umask 077.  The five cache/tmp directories remain empty
0700 directories.  The root remains 0700.  No `.toc`, `.dvi`, `.synctex`,
`.fdb_latexmk`, `missfont.log`, bytecode, `__pycache__`, hidden path,
temporary, backup, lock, socket, FIFO, device, symlink, hard-link alias, or
nested entry is allowed.

The root validator uses only `os.scandir` with `follow_symlinks=False` from
the exact authorized root.  It rejects a name containing slash, NUL, tab,
CR, LF, `.` or `..`, non-UTF-8 bytes, or a component outside the exact
allowlist above.  Rows are bytewise sorted and framed:

```text
relative_path<TAB>type<TAB>bytes<TAB>LF-or--<TAB>mode<TAB>nlink<TAB>sha256-or--<LF>
```

The root itself is separately bound by literal path, no-follow type, mode,
link count, device, and inode.  Opening and closing manifests record row/LF
count, framing bytes, and aggregate SHA-256.  Root 0 and root 1 never enter
the source/control manifest.

## Frozen administrative validators and exit semantics

All validators run only as fresh
`/root/miniconda3/bin/python3 - MODE literal-absolute-path-list` stdin
processes through the capsule.  They import only `sys`, `os`, `stat`,
`hashlib`, `re`, `struct`, and `posixpath`; write no script, module, bytecode,
cache, or transformed PDF; and read only paths explicitly authorized for
that stage.  The algorithms in this section are normative byte-state
machines bound by the hash of this profile.  A later build authorization must
embed the exact stdin implementing these ordered steps and its SHA-256; it
may not add a predicate, fallback, repair, or discretionary branch.  Every
mode exits 0 only after printing exactly `MODE<TAB>PASS<LF>`; any failed
predicate prints exactly `MODE<TAB>FAIL<TAB>code<LF>` and exits 1.  An
exception exits 2.  No warning is success.

### `SOURCE_AND_OPENING_MANIFEST`

For every named text file: no-follow lstat; require regular, expected mode and
link one; read bytes once; require no BOM `efbbbf`, NUL `00`, CR `0d`, or
invalid UTF-8; require nonempty bytes ending in exactly one LF (last byte LF,
penultimate byte not LF); count raw LF; compare byte count and SHA-256 to the
frozen row.  Root traversal and framing then follow the preceding exact
grammar.

### `DEPENDENCY_LIST` and `DEPENDENCY_BIND_NOW`

`DEPENDENCY_LIST` is exactly the D061 extraction algorithm already printed.
`DEPENDENCY_BIND_NOW` parses B100 by splitting LF then TAB into exactly seven
fields, rejects duplicate/unsorted paths and malformed decimal/octal/hex,
replays every no-follow symlink hop, requires the final regular identity, and
hashes it in 1,048,576-byte chunks.  It rejects any field difference.  It
never follows or opens a path not literally present in B100.

### `FINAL_LOG`

The final `main.log` must be UTF-8/LF without CR or NUL.  It contains exactly
one line matching the ASCII regular expression

```text
^Output written on main\.pdf \(([1-9][0-9]*) pages?, ([1-9][0-9]*) bytes\)\.$
```

under multiline mode.  Captured group 1 equals the later pdfinfo page count
and group 2 equals the raw PDF bytes.  It contains none of the following
case-insensitive byte regular expression:

```text
(^!|warning|error|undefined|multiply defined|missing character|emergency stop|fatal|overfull|underfull|rerun|label\(s\) may have changed|destination with the same identifier|token not allowed in a pdf string|font shape.*substitut)
```

The intermediate logs are evidence only; they must contain the positive
output-written line and none of `^!`, `Emergency stop`, or `Fatal error`, but
first-pass undefined-citation messages are neither erased nor used as final
success.  This grammar replaces “normal completion,” “other warning,” and
all subjective log judgments.

### `BIBLIOGRAPHY_CLOSURE`

The exact key set is:

```text
AkianGaubertLemmensNussbaum2006
BedfordKim2008
BellonViallet1999
BlancVanSanten2022
FordyHone2011
FordyHone2014
FriedlandMilnor1989
Gunawardena2003
HasselblattPropp2007
HasselblattProppCorrigendum2007
HoneRagniscoZullo2016
IshibashiKano2021
JaneczkoJelonek2008
Kim2026
MeunierPreliminary
OhmoriYamazaki2024
ShaoSun2025
ZorzenonKomendaRaisch2024
```

The source parser accepts only `\citep{K(,K)*}` citation commands and rejects
any unconsumed `\cite` token.  The BibTeX parser accepts entry starts matching
`^@[A-Za-z]+\{([A-Za-z0-9]+),$`.  The aux parser accepts only keys from
`^\\citation\{([A-Za-z0-9]+(?:,[A-Za-z0-9]+)*)\}$`.  The bbl parser takes
keys from `^\\bibitem(?:\[[^\]\r\n]*\])?\{([A-Za-z0-9]+)\}$`.  Each of the
four distinct sets must equal the exact eighteen-key set; duplicates in BibTeX
or bbl are failures.  `main.blg` must contain exactly once each of
`The style file: plainnat.bst` and `Database file #1: references.bib`, no
other `Database file #`, and no case-insensitive `warning`, `error`, or
`undefined`.  The original and corrigendum must co-occur in every source
citation command containing either key.

### `RECORDER_CLOSURE`

Each certified `.fls` is parsed by the same line grammar as discovery.
Root-local INPUT paths are exactly the three source copies plus later-pass
reads of `main.aux`, `main.out`, and `main.bbl`.  OUTPUT paths are exactly the
seven generated files.  Every external INPUT logical path must be a B100
logical path, and every B100 logical path must occur in the union of the
three certified snapshots plus the nineteen frozen top-level resolutions.
An extra path is reported as literal text only and is never probed.  There is
no shell command, pipe, URL fetch, graphic, fourth source, or write outside
the selected root.

### `EXTRACTED_TEXT_AND_PAGES`

Run the following literal root-0 commands, with their own receipts and stdout
captured in the certified-r0 evidence directory:

```text
/usr/bin/pdfinfo -rawdates /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/main.pdf
/usr/bin/pdfinfo -meta /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/main.pdf
/usr/bin/pdftotext -layout -enc UTF-8 /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/main.pdf -
```

Run the following literal root-1 commands in its distinct stage:

```text
/usr/bin/pdfinfo -rawdates /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/main.pdf
/usr/bin/pdfinfo -meta /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/main.pdf
/usr/bin/pdftotext -layout -enc UTF-8 /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/main.pdf -
```

Their IDs are `R060`, `R061`, and `R062`.  All statuses are zero.  The
pdftotext console bytes are the text evidence; stderr must be empty because
stdout/stderr are combined and any Poppler diagnostic is rejected by UTF-8
page grammar.  Split raw bytes at form feed `0c`, removing exactly one final
empty segment and no other segment.  Each page must decode strict UTF-8.
Within a page, split at LF; a blank line contains only space, tab, vertical
tab, or CR.  The unique page whose first nonblank line after removing only
those four byte classes from both ends is exactly `References` has one-based
index `RREF`.

PDF page 1 through `RREF-1` are content pages.  Require
`22 <= RREF-1 <= 30`, total pages at least RREF, and total pages equal both
the page-segment count and pdfinfo.  The whitespace-collapsed page-1 text
must contain the exact public title, `Anonymous`, `Abstract`, and
`1 Introduction and bounded positioning`.  The exact sentence fragment
`contained in the main text.` occurs on page `RREF-1` and not page `RREF`.
The frozen source contains exactly one literal `\clearpage`, immediately
before `\bibliographystyle{plainnat}` and `\bibliography{references}`.

Collapse maximal ASCII whitespace runs to one space only for anchor checks.
The full collapsed content contains, in order, these exact headings:

```text
1 Introduction and bounded positioning
2 Symplectic family and exact weighted-degree transport
3 Normal-fan iff
4 Incidence realization of primitive words
5 Strict carries and leading forms
6 Ordered monodromy and decoding
7 Least periods, scalar boundaries, and counterexamples
8 Limitations and conclusion
```

It also contains exactly once `Family-wise realization, classification, and
monodromy` and all three captions `Established ingredients and the separation
used here.`, `Notation used in the construction and its consequences.`, and
`Exact side-information ladder for monodromy decoding.`.  These exact anchors
replace subjective “surrounding prose” and semantic-presence judgments.

### `PDFINFO_GRAMMAR`

Parse each `pdfinfo -rawdates` line at its first colon.  The only permitted
keys are `Title`, `Subject`, `Keywords`, `Author`, `Creator`, `Producer`,
`CreationDate`, `ModDate`, `Custom Metadata`, `Metadata Stream`, `Tagged`,
`UserProperties`, `Suspects`, `Form`, `JavaScript`, `Pages`, `Encrypted`,
`Page size`, `Page rot`, `File size`, `Optimized`, and `PDF version`; duplicate
or unknown keys fail.  Title is the exact public title and Author is
`Anonymous`.  Subject, Keywords, Creator, Producer, CreationDate, and ModDate
are absent or have an empty value.  Required exact values are `Custom
Metadata: no`, `Metadata Stream: no`, `UserProperties: no`, `Suspects: no`,
`Form: none`, `JavaScript: no`, `Encrypted: no`, `Page size: 612 x 792 pts
(letter)`, `Page rot: 0`, and `PDF version: 1.5`.  Pages and File size are
positive decimal values matching direct observations.  Tagged and Optimized,
if present, are each exactly `yes` or `no`.  `pdfinfo -meta` stdout is exactly
zero bytes.

### `RAW_PDF_SECURITY_FONT_ANONYMITY`

This validator reads `main.pdf` without changing it.  Its parser is fixed:

1. Require prefix `%PDF-1.5` followed by CR, LF, or CRLF; locate the last
   `startxref` and require one traditional xref table.  Parse fixed-width xref
   entries, require every in-use offset to begin the matching decimal object
   and generation header, and require one terminal `%%EOF` followed only by
   bytes `00`, `09`, `0a`, `0c`, `0d`, or `20`.
2. Tokenize PDF whitespace, `%` comments, names with `#HH` decoding, integers,
   `obj/endobj`, dictionaries, arrays, references, literal strings with exact
   PDF backslash/octal/line-continuation decoding, and even-length hex strings.
   Reject malformed nesting, duplicate object numbers, an unresolved
   reference, an object stream, xref stream, linearization dictionary, or
   incremental update.
3. For every stream, resolve `/Length` as a direct nonnegative integer or one
   indirect integer object, require exact stream boundaries, and reject a
   `/Filter` on every non-font stream.  `/Metadata` and `/EmbeddedFile`
   streams are forbidden.
4. Locate every `/Type /Font` dictionary.  Reject `/Subtype /Type3`.  Follow
   every `/DescendantFonts` reference and require every terminal simple or CID
   font to have a `/FontDescriptor`.  That descriptor has exactly one present
   nonempty `/FontFile`, `/FontFile2`, or `/FontFile3` stream reference.  Its
   `/BaseFont` name matches `^[A-Z]{6}\+[A-Za-z0-9_.-]+$`.  Only the byte spans
   of those referenced font-program streams are excluded from content scans.
5. Outside those font-program spans, reject the exact PDF names
   `/CreationDate`, `/ModDate`, `/ID`, `/PTEX.Fullbanner`, `/JavaScript`,
   `/JS`, `/Launch`, `/EmbeddedFile`, `/Filespec`, `/RichMedia`, `/SubmitForm`,
   `/ImportData`, and `/AA`.  If `/OpenAction` exists, it must occur exactly
   once in the Catalog and resolve only to a page-destination array whose last
   name is `/Fit`, `/FitH`, `/FitV`, `/FitR`, `/FitB`, `/FitBH`, or `/FitBV`;
   an action dictionary is forbidden there.  Reject any non-font stream with
   a nonempty binary byte outside tab/LF/CR and bytes 0x20--0x7e.
6. Decode every literal and hex string and scan it, every non-font stream, and
   `main.out` for the exact forbidden byte tokens listed below.  Matching is
   ASCII case-sensitive except where a regex explicitly says insensitive.

The forbidden token list is:

```text
BATCH07
B07-
PAPER28
primitive_selector_cycle_monodromy_v1
SOURCE_LOCK
PUBLICATION_LOCK
reviewer_role
candidate_id
/root/
/home/
/tmp/
autodl-tmp
symplectic_map
localhost
127.0.0.1
::1
file:
ssh:
smb:
javascript:
```

Do not reject a raw `@` byte.  Contact data is rejected only by this
case-insensitive email regex, applied to decoded strings and extracted text:

```text
[A-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Z0-9.-]+\.[A-Z]{2,}
```

Thus a binary or bibliographic raw-at byte is not a false positive.

Every URI action must be exactly `/S /URI` followed by one decoded `/URI`
string in this public allowlist and no other URI is permitted:

```text
https://www.math.univ-toulouse.fr/~imeunier/
https://www.math.univ-toulouse.fr/~imeunier/pub/Minimal_weighted_degrees_and_algebraic_stability_of_tame_automorphisms.pdf
```

Outside a recognized allowlisted URI, reject any decoded-string match of
`(?<![A-Za-z0-9:])/(?:[A-Za-z0-9._~+%-]+/){2,}[A-Za-z0-9._~+%=-]+`.
This exact string-level rule replaces an undefined “absolute-path pattern”
without treating PDF names or the `https://` separator as paths.  Reject IPv4
hosts in 10/8, 127/8, 169.254/16, 172.16/12, or 192.168/16 and any hostname
ending `.local`.  The visible/extracted author token is exactly `Anonymous`;
no author identity is inferred from public bibliographic author names.

## Per-root acceptance and page/anonymity ceiling

After R052--R055, each root uses this exhaustive ID map; there are no unused
or later-defined slots:

| ID | Exact operation |
|---|---|
| `R056` | `FINAL_LOG` on that root's literal `main.log` and `main.pdf` |
| `R057` | `BIBLIOGRAPHY_CLOSURE` on the three root source copies plus literal `main.aux`, `main.bbl`, and `main.blg` |
| `R058` | `RECORDER_CLOSURE` on the three time-indexed fls snapshots, B100, and that root path |
| `R059` | closing root-universe and five-empty-directory preinspection census |
| `R060` | the literal root-specific `/usr/bin/pdfinfo -rawdates` command printed above |
| `R061` | the literal root-specific `/usr/bin/pdfinfo -meta` command printed above |
| `R062` | the corresponding complete root-specific pdftotext command printed in `EXTRACTED_TEXT_AND_PAGES` above |
| `R063` | `PDFINFO_GRAMMAR` on R060 and R061 console bytes plus direct PDF bytes |
| `R064` | `EXTRACTED_TEXT_AND_PAGES` on R062 console bytes, R063 page count, and the frozen main-source copy |
| `R065` | `RAW_PDF_SECURITY_FONT_ANONYMITY` on literal `main.pdf`, `main.out`, and R062 console bytes |
| `R066` | exact static census: eight sections, thirty-two subsections, forty-three display groups, three tables, zero figures, seventy-one unique labels, and eighteen keys |
| `R067` | root-copy and live-trio lstat/hash equality census |
| `R068` | completeness check for every command, console, status, snapshot, validator result, and stage-local path R000--R067 |
| `R069` | conjunctive per-root acceptance aggregation; it passes only if every preceding status and predicate is zero/PASS |
| `R070` | closing root manifest under the frozen framing |
| `R071` | root-stage evidence seal |

The article must have exactly eighteen bibliography keys, exactly three
tables, zero figures, eight numbered sections, references on a fresh physical
page, and an inclusive integer content span in `[22,30]`.  The page gate may
not be achieved by source changes, font/margin changes, table scaling,
negative spacing, proof removal, an appendix, or PDF postprocessing.

Failure of a log, citation, dependency, page, text, metadata, font, security,
URL, path, or anonymity predicate preserves the root and opens no repair or
release authority.

## Cross-root reproducibility and terminal live-source census

After root 1 has passed R071, `F000` runs the exact command
`/usr/bin/mkdir -m 0700 -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/final`
using the evidence-root receipt pair.  `F001` then runs the terminal live-trio
lstat/hash census and must equal the frozen source table; `F002` seals the
final stage.  This is the required post-second-root observation.  Only then
does `C000` create
`/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/evidence-r1-20260831/cross-root`
using its evidence-root receipt pair.

The literal cross-root commands `C001`--`C009` are, in order:

```text
/usr/bin/cmp -s -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/main.tex /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/main.tex
/usr/bin/cmp -s -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/math_commands.tex /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/math_commands.tex
/usr/bin/cmp -s -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/references.bib /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/references.bib
/usr/bin/cmp -s -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/main.aux /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/main.aux
/usr/bin/cmp -s -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/main.bbl /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/main.bbl
/usr/bin/cmp -s -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/main.blg /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/main.blg
/usr/bin/cmp -s -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/main.log /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/main.log
/usr/bin/cmp -s -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/main.out /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/main.out
/usr/bin/cmp -s -- /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r0-r1-20260831/main.pdf /root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy/build/certified-r1-r1-20260831/main.pdf
```

All statuses are zero and all consoles empty.  `C010` independently compares
byte counts and SHA-256 values.  The raw PDFs must be byte-for-byte identical;
visual equivalence or normalized equality is insufficient.

`main.fls` is the sole root-dependent file.  Normalize a copy in memory only
by replacing every exact byte occurrence of that file's own literal root
prefix with the seven bytes `<ROOT>`; require at least one replacement.  No
other replacement, deletion, sorting, canonicalization, timestamp removal,
or whitespace change is permitted.  The normalized bytes must match.  Both
certified recorder unions must also equal the B100 dependency universe.

`C011` performs the sole `.fls` normalization and comparison.  The closing
relative-path/type/mode/nlink/byte/LF/hash manifests are compared by `C012` and must agree,
except for the raw `.fls` hash which is compared only after that one allowed
prefix substitution.  The two cache/tmp censuses, command statuses,
time-indexed snapshots, pdfinfo bytes, extracted page segments, reference
index, content-page count, raw-object census, font census, security census,
URI census, and anonymity census must agree exactly.  `C013` compares every
per-root semantic and evidence census; `C014` creates the cross-root stage
seal and freezes all comparisons at a physical ledger STOP.

## Terminal abort and no-release rules

The lifecycle is an irreversible one-shot failure, preserving every realized
byte and opening no release authority, if any of the following occurs:

1. a live source, root copy, source-review binding, workspace/cwd, executable,
   symlink chain, version, hash, environment, umask, command, or receipt differs;
2. a future path is probed early, a build/evidence path pre-exists, a root is
   reused, a receipt is missing/overwritten, or a stage is not physically
   sealed before the next authorization;
3. discovery directly opens a newly reported system path, a symlink hop is
   followed before its next STOP/authorization, dependency content is hashed
   before content-hash authority, or a certified command lacks its immediate
   pre/post dependency binding;
4. a command is added, omitted, reordered, retried, substituted, given a
   different argument/environment/cwd/umask, exits nonzero, requests input,
   invokes shell escape, downloads, accesses a network, or writes outside its root;
5. a root has an unexpected entry, cache byte, unsafe name, symlink, alias,
   special file, unlisted input/output, unrecorded status, or invalid manifest;
6. final log, bibliography, recorder, page, reference-start, extracted-text,
   metadata, PDF syntax, security, font embedding, public-URL allowlist, path,
   or anonymity validation fails;
7. the two raw PDFs or any required raw file differ, normalized `.fls` differs,
   dependency universes differ, evidence is incomplete, or the terminal live
   trio no longer matches; or
8. compliance would require source mutation, another root/pass/tool,
   dependency-list repair, evidence backfill, cleanup, normalization, PDF
   rewriting, proof compression, or any external effect.

An abort grants no retry, source edit, replacement root, finalization,
release, copy, upload, submission, hosting, message, or identity disclosure.
Any necessary repair requires a new exact ledger transition and fresh
independent review; a missing time-indexed fact can never be reconstructed
from later equality.

## Closure matrix for the E0208 findings

| E0208 finding | Exact closure in this revision |
|---|---|
| Blocker 1: inconsistent cwd and missing parent mkdir | one literal absolute workspace cwd; every path absolute; `BOOT-000` freezes mode-0755 parent creation and receipt |
| Blocker 2: declarative environment/umask | printed outer env-i/Bash/umask/cd/inner env-i capsule for every child, with exact variables and receipts |
| Major 1: unbound helpers | absolute paths, symlink chains, bytes, modes, hashes, and versions for env/bash/mkdir/install/Python/stat/hash/cmp/TeX/BibTeX/kpsewhich/pdfinfo/pdftotext |
| Major 2: unnamed/overwritten evidence | exact root-external filename grammar, complete command IDs, per-command console/status, time-indexed snapshots, O_EXCL/noclobber, stage manifests and seals |
| Major 3: post-hoc transitive dependencies | distinct non-release discovery root, candidate-list STOP, hop-by-hop symlink STOPs, content-binding authorization/PASS, then two fresh certified roots with every-command pre/post binding |
| Minor 1: no terminal source rehash | `F001` lstat/hash after root-1 seal and before cross-root acceptance |
| Ambiguity 1: subjective validators | exact log/bib/recorder/text/page/pdfinfo/PDF-object/font/security/URL/path/email grammars and exit semantics |

No acceptance gate from the earlier profile is weakened: source hashes,
three-TeX/one-BibTeX order, no retry or source mutation, exact root universes,
eighteen-key closure, inclusive `[22,30]` content pages, fresh References
page, raw certified-PDF equality, sole `.fls` root-prefix normalization,
metadata/font/security/anonymity inspection, and all no-release effects remain
mandatory.

BATCH07_PAPER28_BUILD_PROFILE_FROZEN
