# Paper 27 probe-recovery deterministic build profile

## 1. Status, authority, and source binding

This is the separate probe-recovery profile authorized by E0298 after the
E0297 read-only namespace-enumeration stop.  E0299 authorizes this file alone.
At authoring open, `BATCH_07_STATUS.md` is 1,534,289 bytes, 18,166 LF, mode
0644, link one, SHA-256
`f14050ca7ed1daccedf46f2e0b336388dd780d249cd23399fa5c7f48fc9662a4`,
ending in
`BATCH07_P27_PROBE_RECOVERY_MANIFEST_AND_DESIGN_PASS_PROFILE_AUTHORIZED`.

The direct profile predecessor is the immutable
`notes/BUILD_PROFILE_POSTFAIL.md`, 53,878 bytes, 963 LF, mode 0644, link one,
SHA-256
`f4829e21e4626b372a05e646f34d29f0ea306b653d23d6dd924d1fc54161687e`.
This file preserves its complete source, toolchain, dependency, root,
publication, PDF, comparison, evidence, and first-failure semantics, except
for the fresh recovery names and the explicit noncircular first-evidence-touch
protocol printed in Section 4.  No predecessor file is edited or reused as a
runtime input.

### Immutable history; never an active runtime namespace

E0282 permanently preserves the first validator failure
`FAIL predicate=RESULT_SELF_UNVALIDATED_root`; E001 and E010 succeeded, R000
never ran, and no certified root was created.  E0297 permanently stops the
later postfail regime after a read-only directory-entry enumeration; it
created no build object.  The labels `successor-d60ec6611683`,
`postfail-d60ec6611683`, `r0-20260829`, `r0-rev1-20260830`,
`r1-rev1-20260830`, and `BOOTSTRAP_FIRST_TOUCH_POSTFAIL.md` occur here only as
historical provenance.  No later actor may list, glob, stat, read, execute,
copy, clean, rename, delete, or reuse any corresponding build path or stopped
control.  The deactivated supplemental control is preserved at 9,990 bytes,
194 LF, mode 0644, link one, SHA-256
`1df8823ac6665eed26590aa2384aefef605418d7c1276b108a609f347fce0910`;
it has no recovery authority.

This profile is a local control record and grants no path probe, directory
creation, compiler, BibTeX, PDF, cleanup, release, submission, upload,
later-paper, network, or external-effect authority.  The future recovery
validator retains every frozen executable predicate of
`BUILD_VALIDATOR_POSTFAIL.py`, including its six corrected total result-field
branches and all Type1/PDFRAW, object/resource, semantic-token, `/Contents`,
xref, receipt, runtime, and trust-boundary checks.  Only exact recovery
path/control identities may differ.

The profile is bound to the following exact passed anonymous source trio.
Each path is a regular mode-0644, link-one, strict UTF-8/LF file with no BOM,
CR, or NUL byte and exactly one terminal LF.

| Source path | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 55,063 | 1,681 | `d60ec6611683cafdf822b4cb493040258dc1dd29502363d493f52c3e2deeed3e` |
| `paper/math_commands.tex` | 601 | 17 | `34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957` |
| `paper/references.bib` | 6,610 | 217 | `a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5` |

The controlling static-source review is
`notes/INDEPENDENT_STATIC_SOURCE_SUCCESSOR_REVIEW.md`, 31,760 bytes, 704
LF, mode 0644, link one, SHA-256
`7745af4b80e4e5ff35134e9279b7d2493f9b063bac0110bab115199bae3114ae`,
ending in `BATCH07_P27_STATIC_SOURCE_SUCCESSOR_REVIEW_PASS`.  Its census is
Blocker=0, Major=0, Minor=0, Ambiguity=0.  The canonical manifest after that
review has 90 sorted rows, 13,690 framing bytes, 90 LF bytes, and SHA-256
`4aa9ae32bbe2ff02b8d611a4deeb90fc2d4c743f301216ea3d5890a4e86113ba`;
the ledger is self-excluded and every build subtree is excluded.

No source file may be repaired, formatted, regenerated, or changed during a
build.  The three installed copies in each root must be byte-identical to
the above files both immediately before the first command and after the last
inspection.  A mismatch is a terminal build failure.

## 2. Fixed compiler and bibliography toolchain

The complete dependency authority is already frozen and reviewed; this regime
does not reopen candidate discovery, path-chain discovery, content hashing, or
dependency-lock authorship.  The inherited
`notes/DEPENDENCY_LOCK_SUCCESSOR.md` is 30,145 bytes, 215 LF, mode 0644,
link one, SHA-256
`66c96cc6b40658370cc129e3bf828bcd08a7e69f7f2462ebea084cc77ce6ed17`.
Its independent review at
`notes/INDEPENDENT_DEPENDENCY_LOCK_SUCCESSOR_REVIEW.md` is 12,687 bytes,
231 LF, mode 0644, link one, SHA-256
`b37e361c1cb8e7340c7a2e4af5b207de40df935ced707043c63c1e0f7017df35`,
and ends in `BATCH07_P27_DEPENDENCY_LOCK_SUCCESSOR_REVIEW_PASS`.  The new
profile reviewers must independently prove that the following 87 candidate
strings, 86 final regular targets, chain rules, and per-command rebind rules
are unchanged; the historical review is not represented as a review of this
new profile.

The only permitted compiler invocation is `/usr/bin/pdflatex`.  It is an
invocation symlink with lstat mode 0777, link count one, byte length 6, and
literal target `pdftex`.  Its required resolved regular target is
`/usr/bin/pdftex`, with 1,802,504 bytes, mode 0755, link count one, and
SHA-256
`01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9`.

The only permitted bibliography invocation is `/usr/bin/bibtex`.  It is an
invocation symlink with lstat mode 0777, link count one, byte length 24, and
literal target `/etc/alternatives/bibtex`.  The separately reviewed fixed
toolchain requires `/etc/alternatives/bibtex` itself to be a symlink with
lstat mode 0777, link count one, byte length 24, and literal target
`/usr/bin/bibtex.original`.  The chain resolves to the required regular target
`/usr/bin/bibtex.original`, with 117,128 bytes, mode 0755, link count one,
and SHA-256
`c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f`.
Before any future build command, the separately authorized builder must
directly verify every stated lstat field and literal target with no-follow
`lstat` and `readlink`; resolving only the final regular target is
insufficient.

The following eight exact regular system package files are fixed anchor
identities.  They must have mode 0644, link count one, the stated byte length,
and the stated SHA-256.  They do not purport to be the complete TeX input
closure; the complete 87-path candidate universe and its separate lock gate
are defined immediately after this table.

| Exact package path | Bytes | SHA-256 |
|---|---:|---|
| `/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty` | 87,648 | `027b292408d989f370f160c9b5f5b89641f69cd19027b0342beb022dd74d7c83` |
| `/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty` | 13,829 | `70838b061b56569dd3ed9f339b1bdd1c78ba185de49f27ceae331c97f48b5986` |
| `/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty` | 12,594 | `8d5e2bdb117297385971927b14fe4804314133dc0027b3171249a08280894626` |
| `/usr/share/texlive/texmf-dist/tex/latex/mathtools/mathtools.sty` | 59,397 | `e6bb70c66ffccc39e0ce8786d3dfca962a473339008a5a51ffae09075b74f5a7` |
| `/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty` | 6,078 | `3fe694a5406f84847143e56ba1841385364277cfe7694a9f4bc0072ca8656abc` |
| `/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty` | 12,694 | `1518422cc09b174c47105e41e3606260714b8f99049e3005a87f3c2ce034d157` |
| `/usr/share/texlive/texmf-dist/tex/latex/tools/longtable.sty` | 12,892 | `196f2a7038e1727c4088a015bf11cac88abfedc5b7ee5eca65f44ab91dbac415` |
| `/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty` | 51,697 | `a217353d233e54e8c0944d87ea2924ec1f20d849a35b749698df03884856e5e3` |

The builder must record all lstat/stat/link targets, bytes, modes, link
counts, and hashes immediately before each root's first command.  Any
identity discrepancy stops before compiler execution.  No alternate engine,
bibliography processor, package installation, `kpsewhich`, formatter, custom
style, or fallback toolchain is permitted.

### 2.1 Predeclared complete dependency-candidate universe

No successor compiler or BibTeX process may discover an unlisted system path.
The candidate universe is derived without executing a program or opening a
system candidate: it is the byte-sorted union of the literal external
`INPUT ` strings in the two immutable historical recorder files
`build/r0-rev1-20260830/main.fls` and
`build/r1-rev1-20260830/main.fls`, plus one author-predeclared absolute
candidate for the BibTeX style basename confirmed by both historical
`main.blg` files.  The recorder files are respectively
23,262 bytes, 355 LF, SHA-256
`573ac913b7ffaadb0fb58d02dff8832664c82b54f45f996606c6136c1dfc20cd`
and 23,262 bytes, 355 LF, SHA-256
`46ede3c9acb4d81854a9c85734ac31d9d77bc7d9aeacdd546ec266633cc62353`.
Their 86-element external sets are equal.  Both 906-byte, 46-LF BibTeX logs
have SHA-256
`76792d7f67dc314358a53f43894e619c7da0a51af611ecb3e7ba161b38ee2f92`
and state exactly `The style file: plain.bst` and
`Database file #1: references.bib`.  Those lines prove the basename and
database only; they did not prove an absolute style path.  Before the already
consumed exact dependency-lock derivation, the frozen
`/usr/share/texlive/texmf-dist/bibtex/bst/base/plain.bst` string below was a
literal prospective declaration inferred from the fixed TeX Live layout.
Its existence, type, chain, and bytes remained unclaimed until those consumed
events opened and froze that predeclared path in the exact passed lock and
review bound at the start of this section.  No new candidate or target read is
opened here.

The historical and successor source prefixes before `\\title{` are
byte-identical: 549 bytes with SHA-256
`ea61ad1f6c60bb78ee880a1cd0ebffc6b56e6712a9c8ab7fb5df4beeec0b1f52`.
Thus the class, 11-point option, all eight packages, layout lengths, theorem
environments, and command input are identical.  The command and bibliography
files are byte-identical.  The successor's explicit font-family demands are
roman, italic/emphasis, bold section/theorem furniture, mathematical italic,
calligraphic, blackboard bold, symbol, and operator roman; every family,
series, shape, and size is already represented in the historical recorder
closure.  The successor is ASCII-only, whereas the historical source also
exercised UTF-8 input.  This conservative comparison may justify using the
predeclared superset; it never authorizes a path outside it.

The exact 87 candidate strings are:

```text
/etc/texmf/web2c/texmf.cnf
/usr/share/texlive/texmf-dist/bibtex/bst/base/plain.bst
/usr/share/texlive/texmf-dist/fonts/map/fontname/texfonts.map
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex7.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex8.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam10.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam5.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam7.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm10.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm5.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm7.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx10.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx12.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx5.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx6.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx7.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx8.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmex10.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi10.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi12.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi6.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi8.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr10.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr12.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr17.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr6.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr8.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmss10.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmss8.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy10.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy6.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy8.tfm
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmti10.tfm
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss8.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex8.pfb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb
/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty
/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty
/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd
/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo
/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty
/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty
/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg
/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def
/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty
/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty
/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def
/usr/share/texlive/texmf-dist/tex/latex/mathtools/mathtools.sty
/usr/share/texlive/texmf-dist/tex/latex/mathtools/mhsetup.sty
/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty
/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty
/usr/share/texlive/texmf-dist/tex/latex/tools/longtable.sty
/usr/share/texlive/texmf-dist/web2c/texmf.cnf
/usr/share/texmf/web2c/texmf.cnf
/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map
/var/lib/texmf/web2c/pdftex/pdflatex.fmt
```

The list above freezes path strings, not a new observation of current
filesystem content.  This profile opens no candidate.  The following chain
rules record the already consumed dependency-lock derivation and remain the
mandatory future rebind semantics; they grant no new candidate observation.
Every historically recorded raw target is preserved exactly as bytes,
hexadecimal, and strict UTF-8 literal text.  An empty target, invalid UTF-8,
NUL, CR, LF, or tab fails before any separately authorized target-role
rebind.

The canonical hop is computed without any filesystem operation by this exact
POSIX component algorithm.  For an absolute raw target the component
accumulator starts empty; for a relative target it starts with the components
of the absolute logical symlink parent.  Split the raw target on `/`, ignore
empty components and `.`, pop exactly one accumulated component for each
`..`, failing on an attempted pop of the empty accumulator, and append every
other component literally.  Emit `/` followed by the accumulated components
joined with single `/` bytes.  The result must be an absolute strict
descendant of exactly one of `/etc/texmf/`,
`/usr/share/texlive/texmf-dist/`, `/usr/share/texmf/`, or
`/var/lib/texmf/`.  No `realpath`, stat-follow, directory traversal, prefix
scan, existence inference, or content access is part of this calculation.
The raw target and canonical hop must be frozen together in a physical ledger
STOP before a later event may perform a target-role no-follow `lstat` or
`readlink` on that exact canonical hop.

Logical-role and target-role authority are distinct.  If a canonical hop is
also one of the 87 predeclared logical strings, a separately authorized
same-stage observation of that path in its logical role does not resolve,
validate, or supply the newly learned chain edge.  No observation is made
because of the returned target in the event that learns it, and no
logical-role result is reused for the chain.  Only after the physical STOP
may another event authorize a fresh target-role no-follow observation of the
exact canonical hop.  A repeated canonical path already present in that
chain is a cycle and fails.  At most eight symlink edges are permitted;
encountering a ninth symlink, a dangling target, directory, special file, or
terminal mode other than the exact later-frozen regular-file mode fails
closed.

The consumed derivation terminated every chain in an exact regular path and
predeclared every logical path, hop, and final target before content hashing.
Its sole resulting control artifact remains
`notes/DEPENDENCY_LOCK_SUCCESSOR.md`, with byte-sorted rows

```text
logical_path<TAB>chain-with-=><TAB>target_path<TAB>bytes<TAB>mode<TAB>nlink<TAB>sha256<LF>
```

and its own framing row/byte/LF/hash totals.  The exact independent review
identified at the start of this section already returned an all-zero census.
A later probe-recovery build authorization must reproduce the entire reviewed
table literally in its exact-path read authority.  Immediately before and
after each of the four
publication commands, every logical path and hop is rebound without
following, and every final regular target is rehashed.  Any drift is
terminal.  Each of the three time-indexed certified recorder snapshots must
name no external input outside the reviewed lock.  Their actual external
union may be a strict subset of the conservative lock and is recorded
exactly; no locked-but-unused candidate is required to be read.  The BibTeX
log must name only `plain.bst` and `references.bib`, and the sole system
style candidate must be the reviewed plain-style row.  A prospective extra
dependency is a failure; it is never opened, probed, added, or repaired.

## 3. Exact environment and process discipline

Every executable used by the later build is absolute and independently
rebound before use.  In addition to the TeX pair in Section 2, the required
administrative targets are:

| Role and invocation | Required resolved regular target identity |
|---|---|
| empty environment `/usr/bin/env` | 43,976 bytes; 0755; link one; `85036540673319c6c2f54233fd2b9e45a8a71246b51cc96c4e6ab8ee6c419eb0` |
| capsule shell `/usr/bin/bash` | 1,396,520 bytes; 0755; link one; `59474588a312b6b6e73e5a42a59bf71e62b55416b6c9d5e4a6e1c630c2a9ecd4` |
| directory creation `/usr/bin/mkdir` | 68,104 bytes; 0755; link one; `bd2f081ac37d653181332bd27f35a6041dbf215a7957f65838a9cbec9e64928b` |
| source copy `/usr/bin/install` | 145,944 bytes; 0755; link one; `519a00d199d07da6028ec5a9800d92c562934582a2ea1793b2cbc378a85c1439` |
| validator `/root/miniconda3/bin/python3` | symlink of 10 bytes to `python3.12`; target `/root/miniconda3/bin/python3.12`, 30,626,264 bytes, 0755, link one, `9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101` |
| raw compare `/usr/bin/cmp` | 43,408 bytes; 0755; link one; `b355472d3c90ea94d11ebb8b750e6946ccd348edc6fca4aefc1235c3994ef791` |
| PDF metadata `/usr/bin/pdfinfo` | 59,928 bytes; 0755; link one; `8ca6e6d0b2e6b3f135a82feb07b3d5750498eb77e6f66412803f425eb8471a8e` |
| PDF text `/usr/bin/pdftotext` | 43,544 bytes; 0755; link one; `7de929ce0686af5dbf76975ad08bbff93526b3d9028035176a4ca89d9d19c27d` |

The independent profile review must directly verify these expected
identities; inheriting them from the local protocol reference is not enough.
No `find`, `realpath`, `readlink` executable, `kpsewhich`, `latexmk`, `qpdf`,
formatter, package manager, network client, or PATH-selected substitute is
used.  No-follow metadata and literal symlink reads are performed only by the
bound validator on paths already named by the controlling ledger event.

Except for the single receipt-free first-evidence-touch process defined
exhaustively in Section 4, every external command is launched by the following
literal capsule.  Beginning with `E001`, the later authorization substitutes
only an already printed literal absolute `CWD`, program, argument vector,
three receipt paths, and environment rows:

```text
/usr/bin/env -i /usr/bin/bash --noprofile --norc -c '
set -C
umask 077
cd -- LITERAL_ABSOLUTE_CWD || exit 125
/usr/bin/env -i LITERAL_ENV_ROWS LITERAL_ABSOLUTE_PROGRAM LITERAL_ARGUMENTS > LITERAL_STDOUT 2> LITERAL_STDERR
rc=$?
printf "%s\n" "$rc" > LITERAL_STATUS || exit 126
exit "$rc"
'
```

Each governed process is wrapped outside that row script by the exact E0280
liveness/FD-scrub process argv.  Its argv0 label deliberately retains the
already audited successor literal; changing it would define a new launcher:

```text
/usr/bin/env -i /usr/bin/bash --noprofile --norc -c LITERAL_LIVENESS_CORRECTED_LAUNCHER_SCRIPT batch07-p27-successor-liveness-fd-scrub-launcher LITERAL_SECTION3_ROW_SCRIPT
```

`LITERAL_LIVENESS_CORRECTED_LAUNCHER_SCRIPT` is exactly these thirteen lines:

```text
[ "$#" -eq 1 ] || exit 127
batch07_p27_inner=$1
[[ -e /proc/self/fd/0 && -e /proc/self/fd/1 && -e /proc/self/fd/2 ]] || exit 127
for batch07_p27_fd_path in /proc/self/fd/*; do
  batch07_p27_fd=${batch07_p27_fd_path##*/}
  case $batch07_p27_fd in
    0|1|2) ;;
    ''|*[!0-9]*) exit 127 ;;
    *) exec {batch07_p27_fd}>&- || exit 127 ;;
  esac
done
ulimit -Sn 4096 || exit 127
exec /usr/bin/env -i /usr/bin/bash --noprofile --norc -c "$batch07_p27_inner"
```

The initial and exec-boundary `env -i` calls eliminate inherited environment,
not inherited file descriptors.  The literal standard-FD guard and scrub loop
prove descriptors 0/1/2 live and close every other live decimal descriptor
before the unchanged row script begins; `ulimit -Sn` changes only the soft
`RLIMIT_NOFILE` to 4096.  The four E0280 launcher microtests and their two
all-zero audits are consumed historical evidence and may not be repeated.
Bash reads no startup file; `set -C` prevents receipt overwrite.  For every
`E001`-and-later row, each stdout, stderr, and status path is prechecked absent
without following a symlink.  A status file
is one decimal integer in 0--255 plus LF.  All three receipts are regular
mode-0600, link-one files.  Every `E001`-and-later command gets its own receipt triple; a
missing receipt, nonzero status, unexpected stdout byte for a silent
administrative command, nonempty stderr where the command grammar requires
zero bytes, or pre-existing destination stops the lifecycle.  The sole
validator program is the exact separately reviewed file required by Section
10, copied byte-for-byte into the evidence root before first use.  It executes
with `PYTHONDONTWRITEBYTECODE=1`, imports only the modules permitted by its
reviewed validator lock, writes no code or cache, and has no discretionary
repair branch.

For command or validator ID `ID`, the three literal receipt basenames are
`ID.stdout`, `ID.stderr`, and `ID.status` in its already-created exact
evidence stage.  Snapshot and manifest destinations use only the additional
literal basenames printed in Sections 5--6.  There is no suffix inference at
runtime: the build authorization must print every absolute receipt and
destination path.

Every inner program receives exactly one of the following three mutually
exclusive environment tables and no inherited variable outside its selected
table.  Rows are shown in their required byte order and are passed in that
same order as literal `name=value` arguments to the inner `/usr/bin/env -i`.
The outer `/usr/bin/env -i` supplies the capsule shell with the empty
environment; `set`, `umask`, `cd`, assignment to `rc`, and `printf` are Bash
builtins, as is each displayed `exit`; they do not create a fourth
external-command environment.

`PUBLICATION_ENV(<root>)` is used only for `/usr/bin/pdflatex` and
`/usr/bin/bibtex`:

```text
FORCE_SOURCE_DATE=1
LANG=C
LC_ALL=C
PATH=/usr/bin:/bin
SOURCE_DATE_EPOCH=0
TEXMFCONFIG=<root>/texmf-config
TEXMFHOME=<root>/texmf-home
TEXMFVAR=<root>/texmf-var
TMPDIR=<root>/tmp
TZ=UTC
XDG_CACHE_HOME=<root>/xdg-cache
```

`ADMIN_ENV` is used only for `/usr/bin/mkdir`, `/usr/bin/install`,
`/usr/bin/cmp`, `/usr/bin/pdfinfo`, and `/usr/bin/pdftotext`:

```text
LANG=C
LC_ALL=C
PATH=/usr/bin:/bin
TZ=UTC
```

`VALIDATOR_ENV` is used only for the single Section 4 first-touch Python
harness and every mode of the separately reviewed validator, each invoked
through `/root/miniconda3/bin/python3`:

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

`<root>` is replaced by the exact absolute selected-root path before the
publication table is printed.  The build authorization must bind every
literal program invocation to exactly one named table and record the exact
ordered table presented to the child.  The five ordinary administrative
programs may not receive `PUBLICATION_ENV` or `VALIDATOR_ENV`; the validator
and first-touch harness may not receive either other table; no other inner
executable is permitted.
There is no `HOME`, `USER`, `LOGNAME`, `HOSTNAME`, `PWD`, proxy, TeX search
override, BibTeX search override, shell-startup, or unspecified Python
variable.  Shell escape, network access, inherited caches, retries,
interactive recovery, post-command edits, and source or output copying
between roots are forbidden.

## 4. Reserved evidence and certified roots

The exact existing build parent is
`/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/build`.
It is not listed or traversed by this profile.  The only new direct children
ever permitted by this probe-recovery regime are:

```text
/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/build/recovery-6103a9df0c3d-evidence
/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/build/recovery-6103a9df0c3d-r0
/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/build/recovery-6103a9df0c3d-r1
```

The only later stage paths permitted, in their gated order, are:

```text
/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/build/recovery-6103a9df0c3d-evidence/r0
/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/build/recovery-6103a9df0c3d-evidence/r1
/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/build/recovery-6103a9df0c3d-evidence/cross-root
```

This profile probes none of the six paths.  The inherited dependency lock is
already PASS.  Only after this profile, its two-review aggregate, the new
validator/lock, their independent review, and a separately authorized runtime
microtest all pass may a dual-reviewed first-touch plan be bound and executed.

### Exact noncircular first-evidence-touch protocol

For exactly one operation—the first creation of
`recovery-6103a9df0c3d-evidence`—this subsection is the sole authority and
supersedes the otherwise universal Sections 3 and 10 requirements for an
on-disk receipt triple and an already-installed evidence-validator copy.
Those objects cannot exist before their own directory.  This narrow
precedence expires permanently when the physical bootstrap result is bound in
the next ledger event.  Beginning with `E001`, every Section 3 and Section 10
receipt, capsule, copy, and validator requirement resumes without exception.

The first-touch process uses the exact E0280 outer launcher already printed in
Section 3, including its frozen argv0
`batch07-p27-successor-liveness-fd-scrub-launcher`.  Its literal inner script
is exactly:

```text
set -C
umask 077
cd -- /root/autodl-tmp/symplectic_map || exit 125
exec /usr/bin/env -i LANG=C LC_ALL=C PATH=/usr/bin:/bin PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 PYTHONIOENCODING=UTF-8:strict PYTHONNOUSERSITE=1 PYTHONSAFEPATH=1 PYTHONUTF8=1 TZ=UTC /root/miniconda3/bin/python3 -S -B -P -c LITERAL_RECOVERY_FIRST_TOUCH_HARNESS
```

`LITERAL_RECOVERY_FIRST_TOUCH_HARNESS` is exactly the byte substring after
the following BEGIN line's LF and before the LF preceding the END line.  It
has no runtime dependency on any stopped supplemental control.

BATCH07_P27_RECOVERY_FIRST_TOUCH_HARNESS_BEGIN
import errno
import os
import stat
import sys

COMPONENTS = (
    "root",
    "autodl-tmp",
    "symplectic_map",
    "papers",
    "27-positive-newton-translation-reciprocity",
    "build",
)
LEAF = "recovery-6103a9df0c3d-evidence"
EXPECTED_CWD = "/root/autodl-tmp/symplectic_map"
EXPECTED_ENV = {
    "LANG": "C",
    "LC_ALL": "C",
    "PATH": "/usr/bin:/bin",
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONHASHSEED": "0",
    "PYTHONIOENCODING": "UTF-8:strict",
    "PYTHONNOUSERSITE": "1",
    "PYTHONSAFEPATH": "1",
    "PYTHONUTF8": "1",
    "TZ": "UTC",
}

def fail(predicate):
    print("FAIL BOOTSTRAP predicate=" + predicate)
    raise SystemExit(1)

if sys.argv != ["-c"]:
    fail("ARGV")
if os.getcwd() != EXPECTED_CWD:
    fail("CWD")
if dict(os.environ) != EXPECTED_ENV:
    fail("ENV")
old_umask = os.umask(0o077)
if old_umask != 0o077:
    fail("UMASK")

flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC
directory_fields = ("st_dev", "st_ino", "st_mode", "st_uid", "st_gid")
leaf_fields = directory_fields + ("st_nlink",)
held_fds = []

def same_fields(left, right, names):
    return all(getattr(left, name) == getattr(right, name) for name in names)

def rewalk_chain():
    fresh_fds = []
    try:
        fresh_fds.append(os.open("/", flags))
        if not same_fields(os.fstat(fresh_fds[0]), os.fstat(held_fds[0]), directory_fields):
            fail("REWALK_ROOT")
        for component, held_fd in zip(COMPONENTS, held_fds[1:]):
            fresh_fds.append(os.open(component, flags, dir_fd=fresh_fds[-1]))
            if not same_fields(os.fstat(fresh_fds[-1]), os.fstat(held_fd), directory_fields):
                fail("REWALK_ANCESTOR")
        return fresh_fds
    except BaseException:
        for fresh_fd in reversed(fresh_fds):
            os.close(fresh_fd)
        raise

try:
    held_fds.append(os.open("/", flags))
    for component in COMPONENTS:
        held_fds.append(os.open(component, flags, dir_fd=held_fds[-1]))
    parent_fd = held_fds[-1]
    parent_before = os.fstat(parent_fd)
    if not stat.S_ISDIR(parent_before.st_mode):
        fail("PARENT_TYPE")
    opening_rewalk = rewalk_chain()
    try:
        pass
    finally:
        for fresh_fd in reversed(opening_rewalk):
            os.close(fresh_fd)
    try:
        os.stat(LEAF, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError as error:
        if error.errno != errno.ENOENT:
            fail("LEAF_ABSENCE_ERRNO")
    else:
        fail("LEAF_PRESENT")
    os.mkdir(LEAF, 0o700, dir_fd=parent_fd)
    child_fd = os.open(LEAF, flags, dir_fd=parent_fd)
    final_rewalk = []
    final_leaf_fd = None
    try:
        child_info = os.fstat(child_fd)
        leaf_info = os.stat(LEAF, dir_fd=parent_fd, follow_symlinks=False)
        if not same_fields(child_info, leaf_info, leaf_fields):
            fail("LEAF_REBIND")
        if not stat.S_ISDIR(child_info.st_mode):
            fail("LEAF_TYPE")
        if stat.S_IMODE(child_info.st_mode) != 0o700:
            fail("LEAF_MODE")
        if child_info.st_nlink != 2:
            fail("LEAF_NLINK")
        if child_info.st_uid != os.geteuid() or child_info.st_gid != os.getegid():
            fail("LEAF_OWNER")
        if os.listdir(child_fd) != []:
            fail("LEAF_NONEMPTY")
        os.fsync(child_fd)
        os.fsync(parent_fd)
        child_after = os.fstat(child_fd)
        parent_after = os.fstat(parent_fd)
        if not same_fields(child_info, child_after, leaf_fields):
            fail("LEAF_DRIFT")
        if not same_fields(parent_before, parent_after, directory_fields):
            fail("PARENT_DRIFT")
        if os.listdir(child_fd) != []:
            fail("LEAF_POSTSYNC_NONEMPTY")
        final_rewalk = rewalk_chain()
        final_parent_fd = final_rewalk[-1]
        if not same_fields(os.fstat(final_parent_fd), parent_after, directory_fields):
            fail("FINAL_PARENT_REBIND")
        final_leaf_info = os.stat(LEAF, dir_fd=final_parent_fd, follow_symlinks=False)
        final_leaf_fd = os.open(LEAF, flags, dir_fd=final_parent_fd)
        final_open_info = os.fstat(final_leaf_fd)
        if (not same_fields(final_leaf_info, child_after, leaf_fields) or
                not same_fields(final_open_info, child_after, leaf_fields)):
            fail("FINAL_LEAF_REBIND")
        if os.listdir(final_leaf_fd) != []:
            fail("FINAL_LEAF_NONEMPTY")
        print(
            "PASS BOOTSTRAP"
            + " parent_dev=" + str(parent_after.st_dev)
            + " parent_ino=" + str(parent_after.st_ino)
            + " evidence=" + LEAF
            + " dev=" + str(child_after.st_dev)
            + " ino=" + str(child_after.st_ino)
            + " bytes=" + str(child_after.st_size)
            + " mode=0700 nlink=2"
            + " uid=" + str(child_after.st_uid)
            + " gid=" + str(child_after.st_gid)
            + " entries=0"
        )
    finally:
        if final_leaf_fd is not None:
            os.close(final_leaf_fd)
        for fresh_fd in reversed(final_rewalk):
            os.close(fresh_fd)
        os.close(child_fd)
finally:
    for held_fd in reversed(held_fds):
        os.close(held_fd)
BATCH07_P27_RECOVERY_FIRST_TOUCH_HARNESS_END

The harness imports only `errno`, `os`, `stat`, and `sys`; it does not import
or execute `BUILD_VALIDATOR_RECOVERY.py`.  It opens `/` and each literal
ancestor through `O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC` and retains the complete
descriptor chain through success emission.  A fresh no-follow absolute rewalk
immediately before the absence check must match every retained ancestor by
device, inode, type/mode, uid, and gid.  The harness then inspects only the
exact evidence leaf with `follow_symlinks=False`, accepts only `ENOENT`, and
performs exactly one `os.mkdir` relative to the held build-parent descriptor.
It reopens no-follow, matches fstat/lstat identity, requires directory mode
0700, link count two, process owner, and an empty inventory, and fsyncs child
and parent.  Before success it performs a second complete absolute rewalk,
requires the rewalked build descriptor to match the retained parent, re-lstats
and reopens the literal leaf through that rewalked descriptor, requires both
to match the retained created child, and rechecks empty inventory.  It closes
only process-local descriptors.  It contains no cleanup, retry, fallback,
rename, chmod, stage/root creation, or old namespace.  Any failure after
`os.mkdir` preserves the new directory and stops permanently.

The first-touch authorization must freeze an explicit single-writer premise
from its final source/control/tool preflight through the physical ledger
post-binding: the one governed launcher chain is the only actor authorized to
mutate, rename, unlink, mount over, or replace any literal ancestor, build
parent, or recovery leaf entry.  Reviewers and all other agents remain
zero-write and build-blind.  Any contrary external namespace mutation
invalidates the run and is permanent failure.  Retained descriptors plus the
terminal full rewalk detect namespace changes before the final check; this
single-writer premise closes the unavoidable interval after that check without
claiming that an advisory directory lock can prevent a hostile writer.

Success is one printable-ASCII LF-terminated line in this exact positional
grammar:

```text
PASS BOOTSTRAP parent_dev=D parent_ino=I evidence=recovery-6103a9df0c3d-evidence dev=D ino=I bytes=B mode=0700 nlink=2 uid=U gid=G entries=0
```

Each `D`, `I`, `B`, `U`, or `G` is replaced by canonical decimal
`0|[1-9][0-9]*`; the two device values must agree.  The controlling shell uses
one in-memory non-newline status sentinel, requires status zero and empty
stderr, positionally validates the complete line, and re-emits only the exact
accepted stdout.  It creates no temporary file and no receipt.  The next
physical ledger event must bind the authorizer, profile/validator/tool
identities, exact argv/environment/cwd, stdout bytes/LF/SHA-256, empty stderr,
status, parent fields, new-directory fields, and empty inventory.  No later
receipt may backfill this action.  Any precheck, path, process, grammar,
status, stderr, postcheck, or write mismatch is permanent failure with no
second process, absence check, mkdir, cleanup, or repair.

All later stdout/stderr/status receipts and immutable snapshots live under the
evidence root, never in a certified root.  It has the only two mode-0700 stage
children `r0` and `r1`, plus `cross-root` after both roots pass.  Creation of
each stage is receipted in the already-existing evidence root.  Only after
the corresponding stage exists is its certified root checked absent and
created mode 0700 with receipts in that stage.  Root 1 is neither probed nor
created until root 0 has completed, been validated, and had its evidence
inventory bound in the ledger.  A pre-existing path fails closed without
read, delete, rename, or reuse.  Neither root is seeded from a historical or
other successor root.

All evidence is preserved.  No root, cache, auxiliary file, failed output,
receipt, or log may be cleaned, truncated, overwritten by a retry, or removed.

## 5. Exact root initialization and four-command sequence

The absolute project directory is
`/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity`.
For root suffix `r0` or `r1`, after the ordered absence and parent checks, the
only initialization operations are the following absolute-path operations,
each through the Section 3 capsule and its own receipt ID `R000`--`R008`:

```text
/usr/bin/mkdir -m 0700 -- <root>
/usr/bin/mkdir -m 0700 -- <root>/texmf-var
/usr/bin/mkdir -m 0700 -- <root>/texmf-config
/usr/bin/mkdir -m 0700 -- <root>/texmf-home
/usr/bin/mkdir -m 0700 -- <root>/xdg-cache
/usr/bin/mkdir -m 0700 -- <root>/tmp
/usr/bin/install -m 0644 -- /root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/paper/main.tex <root>/main.tex
/usr/bin/install -m 0644 -- /root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/paper/math_commands.tex <root>/math_commands.tex
/usr/bin/install -m 0644 -- /root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/paper/references.bib <root>/references.bib
```

`R009` freezes the opening root manifest and exact installed-copy equality.
Immediately before and after every publication command, a distinct validator
replays the complete reviewed dependency lock, the invoked executable chain,
the capsule tools, the live source trio, the three root copies, and the root
universe.  It exits zero only on exact equality.  The four publication command
IDs are `R020`, `R030`, `R040`, and `R050`; from absolute `<root>` cwd they run
exactly once, in this order:

```text
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder main.tex
/usr/bin/bibtex main
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder main.tex
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder main.tex
```

After `R020`, before BibTeX can overwrite anything, the exact `main.log`,
`main.aux`, and `main.fls` are copied with an embedded validator using
`os.open(O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW,0600)`, binary chunks, `fsync`,
and a post-copy byte/hash comparison into `R021--main.log.snapshot`,
`R022--main.aux.snapshot`, and `R023--main.fls.snapshot` in the root's
evidence stage.  After `R030`, `main.bbl` and `main.blg` are similarly frozen
as `R031` and `R032`.  After `R040`, the second `main.log`, `main.aux`, and
`main.fls` are frozen as `R041`--`R043`; after `R050`, the final three are
frozen as `R051`--`R053`.  A complete no-follow root manifest is frozen after
each publication command as `R024`, `R033`, `R044`, and `R054`.  Snapshot
source and destination names are literal in the build authorization; no
runtime filename construction or overwrite is allowed.

Every command and snapshot has a separate stdout/stderr/status receipt.  Raw argv,
environment, cwd, start/end observation, status, both stream identities,
pre/post dependency census, and root-manifest identity are recorded.  A
nonzero status or failed predicate stops immediately.  There is no retry or
fifth pass.  If root 0 fails, root 1 is never probed.  If root 1 fails, both
roots and all evidence are preserved and no release gate opens.

## 6. Root-local products and filesystem containment

Before TeX 1, each root contains exactly five empty mode-0700 directories
`texmf-var`, `texmf-config`, `texmf-home`, `xdg-cache`, and `tmp`, followed by
the three mode-0644, link-one source copies.  After TeX 3, the only additional
regular mode-0600, link-one top-level files are exactly:

```text
main.aux
main.bbl
main.blg
main.fls
main.log
main.pdf
```

No `main.out`, `main.toc`, hidden file, temporary, backup, script, bytecode,
symlink, socket, device, FIFO, hard-link alias, or nested entry is accepted.
The five cache/tmp directories must remain empty.  The builder manifests the
root itself and every allowed child after setup and after each command with
literal relative path, type, bytes, raw LF, four-digit mode, link count, and
raw SHA-256 for every regular file; rows are byte-sorted and framed with one
terminal LF.  These five root-local manifests are immutable raw evidence.
Their bytes are never edited or called normalized.  Section 9 defines the
separate field-aware comparison projection and the exact recorder snapshot
to which each raw `main.fls` row must rebind.

The three recorder snapshots must show root-local INPUT paths drawn only from
`main.tex`, `math_commands.tex`, `main.aux`, and `main.bbl` as appropriate to
the pass, root-local OUTPUT paths drawn only from `main.aux`, `main.log`,
`main.fls`, and `main.pdf`, and external inputs exactly within the reviewed
dependency lock.  BibTeX alone may read root-local `main.aux`,
`references.bib`, and the locked `plain.bst` and write only `main.bbl` and
`main.blg`.

The phrase “no write outside the chosen root” applies to the publication
processes.  The exhaustive administrative exceptions are: metadata changes
to the exact build parent caused by creating the evidence and two certified
children; stdout/stderr/status/snapshot/manifest bytes below the exact evidence
root; the append-only ledger events; and, only after both roots stop, the sole
authorized `notes/BUILD_EVIDENCE_RECOVERY.md`.  No other outside-root write
is permitted.  The empty inherited environment, root-local cwd/TEXMF/cache/
TMP paths, per-command receipts, time-indexed recorder snapshots, and
post-command root manifests are the mandatory containment evidence; final
`main.fls` alone is never treated as proof of all four commands.

## 7. Log, bibliography, sentinel, and page acceptance

For each successful root, the final `main.log`, `main.blg`, `main.aux`, and
`main.bbl` must establish all of the following:

1. exactly one complete log line has the form
   `BATCH07_REFERENCE_START_PAGE=N`, where `N` is a positive decimal integer;
2. the proof-content page count is exactly `N-1` and lies in the inclusive
   interval 24--28;
3. bibliography processing completed with all and only the frozen twenty
   citation keys, with twenty bibliography items and no missing, duplicate,
   undefined, or unused-key anomaly caused by the build;
4. every citation and cross-reference is resolved after the final pass;
5. there is no `Overfull \\hbox` or `Overfull \\vbox` line;
6. there is no TeX error, emergency stop, fatal error, missing character,
   multiply defined label, undefined reference, undefined citation, rerun
   request, font substitution/fallback warning, destination collision,
   shell-escape evidence, or package/file-not-found warning;
7. every remaining warning, including each underfull box if any, is listed
   verbatim by class and line/page locus, has the same census in both roots,
   and receives an explicit benign/non-padding disposition before review.

The exact bibliography-key set is:

```text
abboud_xie_2026
bedford_kim_2008
berger_turaev_2025
bianchi_dinh_rakhimov_2024
blanc_van_santen_2022
cheng_wang_yu_1994
dang_favre_2021
deserti_2018
el_hilany_2024
favre_wulcan_2012
fordy_hone_2011
gomez_meiss_2004
grigoriev_containment
hasselblatt_propp_2007
janeczko_jelonek_2008
koch_lomeli_2014
nisse_2026
shafikov_wolf_2003
shao_sun_2025
takenawa_2026
```

The source `\cite{...}` union, BibTeX entry keys, final aux `\citation`
union, and final bbl `\bibitem` keys must each equal this set, with no
duplicate entry or item.  `main.blg` must contain exactly once each of
`The style file: plain.bst` and `Database file #1: references.bib`, no other
database line, and no case-insensitive `warning`, `error`, or `undefined`.

The final-log validator reads strict UTF-8/LF bytes with no NUL or CR.  It
requires exactly one line matching
`^Output written on main\.pdf \(([1-9][0-9]*) pages?, ([1-9][0-9]*) bytes\)\.$`,
whose groups equal direct PDF observations, and exactly one sentinel line
matching `^BATCH07_REFERENCE_START_PAGE=([1-9][0-9]*)$`.  It rejects the
case-insensitive classes `^!`, `error`, `undefined`, `multiply defined`,
`missing character`, `emergency stop`, `fatal`, `overfull`, `rerun`,
`label(s) may have changed`, `destination with the same identifier`,
`token not allowed in a pdf string`, and `font shape.*substitut`.  Every line
containing `warning` or `underfull` not already rejected is emitted verbatim
to the evidence census; omission or an unexplained line fails.

The last condition is not a waiver for unresolved semantic or layout
warnings.  A warning that may affect mathematics, citations, anonymity,
pagination, table fit, glyphs, or deterministic output is a failure.

The final PDF page count must be at least `N`, and the bibliography must
begin on page `N` with no theorem, proof, fixture, boundary, conclusion, or
other proof content after the sentinel.  The source-level 11-point portrait,
normal-spacing, normal-size, no-padding contract remains binding.  The build
must not introduce blank proof-content pages, clipped material, rotated or
landscape pages, or table overflow.

## 8. PDF integrity and anonymous publication checks

After the final root-local command and dependency rebind, each root runs only
these two already bound read-only inspection invocations, with its literal
absolute PDF path substituted and its stdout/stderr/status captured in that root's
evidence stage:

```text
/usr/bin/pdfinfo -rawdates <root>/main.pdf
/usr/bin/pdftotext -layout -enc UTF-8 <root>/main.pdf -
```

Both statuses must be zero and each separately captured stderr file must be
exactly zero bytes.
The PDF-info parser requires an unencrypted PDF 1.5, positive total page and
file-size fields equal to raw observations, letter portrait media boxes with
zero rotation, no JavaScript, form, user-property, suspect, metadata-stream,
or custom-metadata flag, creator `TeX`, producer `pdfTeX-1.40.22`, and epoch
CreationDate/ModDate corresponding to `1970-01-01T00:00:00Z`.  An absent or
empty Title/Author metadata field is permitted because visible authorship is
checked from extracted page 1; any nonempty Author other than `Anonymous`
fails.

The exact extracted-text stdout is split at form-feed bytes, removing only
one final empty segment.  Every page must be strict UTF-8 and contain no
replacement character.  The unique page whose first nonblank trimmed line is
`References` has one-based index `RREF`; `RREF` must equal the log sentinel
`N`, so pages 1 through `N-1` are exactly the 24--28 proof-content pages.
Total pages must equal both pdfinfo and the page-segment count and be at least
`N`.  Whitespace-collapsed page 1 must contain the exact title, `Anonymous`,
and `Abstract`.  The collapsed pre-reference text must contain, in order,
the exact eight headings `1 Introduction`, `2 Collision positioning`,
`3 Typed cells and main theorem`, `4 Positive-face survival`,
`5 Translation, envelopes, equality, and tail`,
`6 Full spans and literal reciprocity`,
`7 One-step radius and complete fixture`, and
`8 Boundaries and conclusion`; it must also contain the exact five theorem
clause names `Typed survival`, `Translation and transience`,
`Equality and tail`, `Literal word reciprocity`, and `One-step radius`, the
six fixture IDs `P1`, `P2`, `P3`, `Q1`, `Q2`, and `Q3`, the seven boundary
row names `Characteristic zero`, `Positive coordinates`,
`Coordinate lower bound and strictness`, `Complete row family`,
`First carry`, `Literal reflected label`, and
`Positive-support cancellation control`, and the conclusion.  None may
first occur on or after `RREF`.

The exact conclusion anchor is `Larger typed fan systems and perturbations
of the row data would require new hypotheses and proofs; they are directions
beyond the present result.` after ASCII-whitespace collapse.  In the
extracted reference-page suffix, multiline matching must find exactly one
leading numeric label for each integer 1 through 20 by
`^[ \t]*\[([1-9]|1[0-9]|20)\][ \t]+`, and no other leading bracketed
decimal label.  This visible census must equal the twenty bbl items.

The raw-PDF validator requires prefix `%PDF-1.5`, one terminal `%%EOF`, no
encryption dictionary, no `/Subtype /Type3`, and for every visible font
descriptor at least one nonempty `/FontFile`, `/FontFile2`, or `/FontFile3`
reference.  It rejects `/JavaScript`, `/JS`, `/Launch`, `/EmbeddedFile`,
`/Filespec`, `/RichMedia`, `/SubmitForm`, `/ImportData`, and the exact byte
tokens `BATCH07`, `B07-`, `SOURCE_LOCK`, `PUBLICATION_LOCK`,
`reviewer_role`, `candidate_id`, `/root/`, `/home/`, `autodl-tmp`,
`symplectic_map`, `localhost`, `127.0.0.1`, and `::1` outside embedded font
program streams.  Decoded text is rejected by the same provenance/path
tokens and by a case-insensitive email-address grammar.  These checks and
successful full-text extraction are the fixed embedded-font, glyph,
security, and anonymity evidence; no subjective visual waiver is allowed.

Acceptance requires an unencrypted readable PDF, uniform portrait pages,
embedded usable fonts, no personal author name or internal path/hash/event,
reviewer/agent, recovery, repository, or build-governance narrative, and
visible preservation of the five theorem clauses, all six proof modules,
six-pair fixture, seven boundaries, conclusion, and twenty-item references.
PDF metadata may identify only the fixed TeX producer/creator and the
anonymous article title; filesystem paths and personal identity are
forbidden.

## 9. Cross-root determinism

After both roots independently pass Sections 5--8 and the terminal live
source trio has been rehashed, create the exact `cross-root` evidence stage.
Using the bound `/usr/bin/cmp` with separate receipts, require byte-for-byte
identity and equal SHA-256 for `main.tex`, `math_commands.tex`,
`references.bib`, `main.pdf`, `main.aux`, `main.bbl`, `main.blg`, and
`main.log`.

The three aligned time-indexed `.fls` snapshot pairs, `R023`, `R043`, and
`R053`, are compared after only the mechanical replacement, in the bytes of
each snapshot itself, of that snapshot's exact absolute root prefix by the
literal token `<ROOT>`.  The normalized snapshot bytes and SHA-256 values
must match.  Raw root-bearing recorder snapshots are not required to match.

Root manifests are compared in the five exact aligned pairs `R009/R009`,
`R024/R024`, `R033/R033`, `R044/R044`, and `R054/R054`, where the left and
right member names live in the `r0` and `r1` evidence stages respectively.
The setup manifests `R009/R009` contain no recorder and must be byte-identical
as raw framed files.  For each later pair, the validator strictly parses both
immutable raw manifests and requires identical row paths and types.  Every
row other than the row whose literal relative path is `main.fls` must be
byte-identical, including its raw identity fields.  The two `main.fls` rows
must have identical path, type, raw-byte-count, raw-LF, mode, and link-count
fields; their raw SHA-256 fields may differ only as described next.

For `R024` and `R033`, each raw `main.fls` row must rebind exactly to that
root's preserved `R023--main.fls.snapshot`; BibTeX must not have changed the
live recorder between those manifests.  For `R044` it must rebind to
`R043--main.fls.snapshot`, and for `R054` it must rebind to
`R053--main.fls.snapshot`.  Rebinding means that the snapshot's raw bytes,
raw LF, mode, link count, and raw SHA-256 equal the corresponding manifest
row.  For `R024`, `R044`, and `R054`, the snapshot receipt must already bind
those fields to the recorder immediately copied from the live root.  Before
freezing `R033`, a distinct validator invocation must also require the still
live `main.fls` to equal `R023--main.fls.snapshot` byte-for-byte and in every
identity field.  The validator then forms an in-memory
canonical comparison projection by copying every raw manifest byte except
that it replaces the 64 lowercase hexadecimal raw-SHA field of the sole
`main.fls` row with the SHA-256 of the corresponding recorder snapshot after
the sole root-prefix substitution above.  It emits the two projection
SHA-256 values and the compared field census in its already required
cross-root stdout receipt; it creates no projection file.  The two projected
manifest byte streams and hashes must match.  This field substitution is not
a second content normalization: the only transformed content is the
preserved recorder byte stream, and all raw manifests remain untouched.

No other normalization, field substitution, line deletion, semantic-log
sorting, PDF rewriting, metadata stripping, or tolerance is allowed.  The
sentinel value, total page count, warning census, font census, PDF metadata
census, and decoded-text hash must also agree exactly.  No other evidence
file is normalized or projected.

Any difference in the raw PDFs, required auxiliaries, normalized recorder
evidence, pages, sentinel, warnings,
fonts, metadata, or decoded text is a deterministic-build failure.  Equality
cannot cure a missing pre-command identity or a root-local acceptance
failure.

## 10. Evidence, review, and fail-closed handoff

A later build-author event may open only after this profile has its required
two separated all-zero reports, the aggregate review artifact has passed, and
the unchanged complete dependency lock and its historical all-zero review
have been identity-bound again.  The two profile reviewers must each return
Blocker=0, Major=0, Minor=0, Ambiguity=0; the sole
`notes/INDEPENDENT_BUILD_PROFILE_RECOVERY_REVIEW.md` must bind both complete
separated reports rather than reduce them to one review.  Only a later
build-author ledger event, after that aggregate PASS, the new validator/lock
independent review, and the separately authorized runtime microtest all pass,
may separately authorize the exact evidence-root bootstrap, ordered two-root
mutations, receipts, and
exactly one local probe-recovery build-evidence record at the reserved path
`notes/BUILD_EVIDENCE_RECOVERY.md`.  This profile reserves that path but
grants no authority to create it.  That record must bind:

- the opening ledger and reviewed profile identities;
- immediate root-absence and parent-component checks;
- source, toolchain, administrative-tool, complete dependency-lock,
  environment, and installed-copy pre/post checks for every command;
- every command's timestamp, argv, status, and transcript identity;
- bootstrap ledger receipt, every stdout/stderr/status path, every pre-overwrite
  snapshot, and every after-command root manifest;
- complete opening/final root manifests and exact write-containment evidence;
- all required product identities;
- log, bibliography, sentinel, page, warning, layout, PDF, font, metadata,
  anonymity, and decoded-content checks;
- raw and normalized cross-root comparisons; and
- the precise terminal disposition without cleanup or repair.

Before cross-root comparison, the live source trio is lstat'ed and rehashed
one final time against Section 1.  Missing evidence, an incomplete check, a
tool or dependency identity not separately bound, a pre-existing path, an
unlisted input/output, or any discrepancy is terminal failure and opens no
PDF/release/later-paper authority.

Validator implementation is a separate pre-build lock, never an
implementation invented in the build authorization.  After the profile's
two-review aggregate PASS and re-binding the already passed dependency lock,
a bounded author gate must create exactly
`notes/BUILD_VALIDATOR_RECOVERY.py` and
`notes/VALIDATOR_LOCK_RECOVERY.md`.  The Python file must completely
implement the no-follow identity/root-manifest, exclusive snapshot,
dependency rebind, final log/bibliography/recorder, PDF-info/text/raw-PDF,
and cross-root modes specified here, with an exhaustive argv/path grammar,
deterministic PASS/FAIL stdout, zero diagnostic stderr on success, and exit
codes 0/1/2.  The lock must bind its bytes, LF, mode, link count, SHA-256,
allowed imports, every exact mode/argv row, every expected receipt basename,
and every read/write path class.  A wholly fresh reviewer must create the
sole all-zero artifact
`notes/INDEPENDENT_VALIDATOR_RECOVERY_REVIEW.md`, ending in
`BATCH07_P27_VALIDATOR_RECOVERY_REVIEW_PASS`.  Any code ambiguity,
unbound runtime input, unsafe path operation, incomplete predicate, or
profile mismatch is FAIL_WRITE_NOTHING.

The probe-recovery validator must be derived from the preserved predecessor
bytes without editing that predecessor.  It must update every evidence,
stage, root, copy, profile, lock, review, and terminal identity to this
regime.  In `_parse_validator_stdout`, every field name in all fifteen
`VALIDATOR_RESULT_FIELDS` rows must enter exactly one total validation branch.
In particular, `root`, `stage`, `checkpoint`, `id`, `dependencies`, and
`disposition` branches must accept their exact valid grammar and reject every
other value; they may not use an invalid-only conditional that lets a valid
value fall through to `UNVALIDATED`.  Decimal, hash, warning-hex, recorder and
cross-manifest fields retain their predecessor predicates.  Static review
must construct a canonical valid detail string for all fifteen modes and an
invalid mutation for each symbolic field before any separately authorized
runtime microtest or build.

The one Section 4 receipt-free first-touch process and every `E001`-and-later
validator/nonvalidator row are wrapped by the exact liveness/FD-scrub launcher
printed in Section 3 and proved under E0280.  The first-touch launcher execs
the Section 4 literal harness inner script; every later launcher execs the
unchanged Section 3 receipt capsule.  In both cases an empty-environment
noninteractive frozen Bash first
requires `/proc/self/fd/0`, `1`, and `2` to exist, enumerates its own
`/proc/self/fd/*`, closes every decimal descriptor other than 0/1/2, lowers
only soft `RLIMIT_NOFILE` to 4096, and execs its already selected literal
Section 3 or Section 4 inner script through a second absolute `env -i` and
noninteractive Bash.  Any arity,
standard-FD, descriptor-close, or limit failure exits 127 before a governed
receipt or payload opens.  No inherited environment, extra descriptor,
temporary launcher file, PATH-selected executable, retry, or repair is
admitted.  This explicit split is the sole bootstrap exception; it grants no
receipt exception to `E001` or any later row.

Only after that review may the build event name the already reviewed
validator-file identity and copy those exact bytes once, mode 0500, to the
evidence root using the bound install tool.  Every validator invocation uses
that immutable evidence copy with its printed mode and absolute arguments;
its hash is rebound before and after every use.  The build event may not
embed, edit, parameterize, or replace validator code.  Thus the profile
review audits this required lock architecture, the later validator review
audits the exact executable bytes, and no validator semantics are deferred
to build execution.

After the author stop, the complete evidence root and both preserved roots
are opened to a wholly fresh independent build reviewer.  Only its single
all-zero PASS artifact at
`notes/INDEPENDENT_BUILD_RECOVERY_REVIEW.md`, ending in
`BATCH07_P27_BUILD_RECOVERY_REVIEW_PASS`, may open a separately authored and
independently reviewed release-integrity gate.  The build-review path is only
reserved here; creation authority remains none until the future evidence
author stop.  Release-integrity artifact names and exact checks must be frozen
by their own future author gate and review; none is silently inherited from
the failed regime.  Paper 28 remains closed until that new release-integrity
PASS.  Any release is local only.  No publication or external effect is ever
implied.

BATCH07_P27_BUILD_PROFILE_RECOVERY_AUTHOR_STOP
