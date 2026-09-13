# Paper 21 Final Manuscript Integrity Review

Date: 2026-08-22 UTC

Verdict: PASS. The frozen manuscript is confirmed as a local anonymous release
candidate. This determination grants no submission, upload, transport,
repository push, public hosting, external messaging, or identity disclosure.

## Independence, authority, and write discipline

I acted as the fresh sole terminal-integrity reviewer. I authored none of the
57-file `Q57` universe and am distinct from the finalization-governance author,
the independent finalization reviewer, the release-candidate author, and the
terminal-build evidence author. I performed no source edit, rebuild, BibTeX
run, CAS or numerical experiment, network access, or external action.

Before cleanup I read, enumerated, and rehashed exact `Q57` and both live
terminal roots. I also directly audited all six historical build roots. Until
every content, build, PDF, visual, governance, and root check passed,
`paper/reviews` was absent and I wrote nothing inside the project. The only
regular-file project write of this review is this file; its parent directory is
the sole added directory.

## Exact Q57 universe and canonical JSON

The pre-review project universe was exactly 57 regular files in the four
project-relative directories `experiments`, `notes`, `paper`, and
`refine-logs`, with zero symlinks and zero other entries. A complete snapshot
recorded the root and directory modes plus, for every regular file, its path,
mode, owner, size, and SHA-256. The snapshot was 6,577 bytes/62 LF and had
SHA-256
`9d9cc97c764a93f811248f535474414b5039e0a53d1b6bab1241df37ebdd2477`.
It was byte-identical immediately before cleanup and immediately after cleanup.

The controlling terminal identities were:

| Artifact | Bytes | LF | SHA-256 / status |
|---|---:|---:|---|
| `paper/TERMINAL_REBUILD_RECEIPT.json` | 24,430 | 1 | `935e434e8329489fdb6edd2f27323200e0af42c6819dcbc227bba7041140896a`; `TERMINAL_REBUILD_PASS_PENDING_INDEPENDENT_ROOT_AUDIT` |
| `paper/FINAL_RELEASE_MANIFEST.json` | 12,141 | 1 | `1acf1f482673e8f7e6ea64d98cccf205a11c153ef29d6fc9c4f029bb2708a661` |
| `paper/main_release_candidate.pdf` | 465,922 | 2,539 | `b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3` |
| `paper/main.tex` | 84,917 | 1,990 | `34074c5965086d79145bf2b273398c4c17fdc264b6f5e3555fd1b9a2bd27c7b2` |
| `paper/math_commands.tex` | 981 | 33 | `05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a` |
| `paper/references.bib` | 675 | 19 | `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8` |

I strictly decoded all ten JSON files in `Q57` as UTF-8 with duplicate keys,
`NaN`, `Infinity`, `-Infinity`, and all other nonfinite values rejected. Each
object reproduced its exact input bytes under recursive Unicode key ordering,
compact `,`/`:` separators, and one terminal LF. The result was 10/10 strict
canonical round trips.

I independently rehashed every declared binding rather than trusting a summary:

- the finalization lock's frozen `F51` universe passed 51/51;
- the release manifest's non-self binding set passed 55/55;
- the terminal receipt's exact `R56` universe passed 56/56;
- the manifest was present as an independently rehashed `R56` member;
- the manifest excluded its own byte count and digest, and the receipt excluded
  its own byte count and digest; and
- all binding paths were unique, byte-sorted, safe project-relative paths.

The manifest's 55 bindings are exactly current `Q57` minus the manifest and
terminal receipt; the receipt's 56 bindings are exactly current `Q57` minus
the receipt. There is no unbound non-self regular file in either universe.

## Authoritative source, build, and governance lineage

The complete proof-first lineage rehashes and is internally consistent.

1. The source and publication locks are SHA-256
   `41f350ca31fc06cf0eae3412419fa6d4615f9670a5d2150b04d7e59f9986b202`
   and
   `14966ffc04e0ce68eed83688bfaf871aa02422ba2564532d0f6fff5a7071e114`.
   Their independent reviews end `SOURCE_LOCK_PASS` and
   `PUBLICATION_LOCK_PASS`.
2. The authoritative repaired-source R1 and R2 reviews are
   `07114e0da0eb41ed827f86064186639ffed49c2be2db97bf3e016d7390fface0`
   and
   `3b606a9481811d795dd7fe5ebb16bf280898f56748e61045f8b802de0b063a3a`;
   they end `PAPER_SOURCE_R1_R0_REPAIR_PASS` and
   `PAPER_SOURCE_R2_R0_REPAIR_PASS` and bind the current source trio.
3. The historical first R0 attempt bound source
   `c3d34411f3012a446238c098a10e1f76258236a5d0b6da91f7b01475633c1e86`
   and PDF
   `b004e961ea4184b222c98bbafff217fbff78b5e95c7b2a359757ee67b665a100`.
   The two roots agreed on their stable outputs, but direct reinspection found
   21 pages, two underfull boxes, and the two recorded overfull boxes of
   0.4714 pt and 26.77045 pt. The bound blocker note is
   `6b97f1203541b254cd1b0a60c7ed29978e2a500286c0ba1b72dad0712276fada`
   and ends `R0_BLOCKED`.
4. The proof-first repair ledger
   `4c8ec1258876305cd447bdf175b5a88fe801f69fdfd78d0ee956ae7463171a12`
   records the bounded expansion from that baseline to current
   `main.tex` `34074c59...`. It correctly treats the superseded source reviews
   and the intermediate `910086eb...` PAGEFIX reviews as non-authoritative.
5. The repaired deterministic R0 receipt is
   `3899ee597562861623bd161a00063fc683f5f998499c677fd7e85e842f1a6e96`
   and has status `BUILD_R0_REPAIR_PASS`. The first build review
   `90d4c0ac6aa682dbd1ca0df5d1a3d75c42ba56d2a4df341643db888bf753be1c`
   blocked solely on the receipt's declared canonical key ordering. I
   independently reconstructed the old 7,339-byte serialization in memory:
   it hashes to
   `48e61f31636c3e70f26da61b74fa9655c22a3ac954b9ae56b877cdebedcd5537`
   and decodes to the same JSON value as the current receipt. The repair ledger
   `fefe63317ca10890ba6763bc1fc0dcd3a8c92497caed3ebc454d2704f841e510`
   changes only the final four `checks` key positions. The replacement review
   `62511dd572fa14bdea670df85eb6a48fc54e081a916af5935fdca8f870531bdd`
   ends `BUILD_R1_R0_REPAIR_REPLACEMENT_PASS`.
6. The sole revision window is a true no-op. Receipt
   `441c1cc5e7b3372bbe1d7f05e34ac19461f109bcb0de1e9f7cd4e23db6ba8d42`
   has status `R1_NO_OP_REVISION_PASS`, zero changed paths, zero required or
   cosmetic findings, identical before/after source bindings, one window
   consumed, and zero remaining.
7. The deterministic R1 receipt
   `fa0a511a3391135db75b6eaef03e83fa90930219ddacb8aeaf4713d2aff0bada`
   has status `BUILD_R1_NO_OP_PASS`; R0 and R1 persisted generated outputs are
   byte-identical. The fresh R2 review
   `69f0c560443edbf3f718e47507081525ddd1f2caa383f6bfbd1ec9378cf6070a`
   ends `BUILD_R2_R1_PASS`.

The recovered finalization lock is
`f8a71bdcddb77c19618c02b61c2a503d46d6a719de60c9bf467c57af98be17ab`.
Its sole recovery changes the false authoritative-chain terminal value
`BUILD_R0_BLOCKED` to the actual `R0_BLOCKED`; all 51 `F51` bytes remain
unchanged, the failed review wrote no project file, and a fresh reviewer was
required. The current scope
`1c2b5e6dfe0a355ad839bf3a3b303c3f0258372f0f1c677b440478899f49d01a`
and fresh finalization review
`d489295621cf42a1595d419bea33d63fe98c5d4a95078ffe2500165b12433fd3`
bind this recovery; the latter ends `FINALIZATION_STAGE_PASS`.

## Release manifest, provenance, DAG, and firewall

The release candidate is an exact raw-byte copy of `paper/main_round1.pdf`.
It is byte-identical to `paper/main.pdf`, `paper/main_round0.pdf`, and
`paper/main_round1.pdf`; no compile, transform, render, metadata rewrite,
signature, or optimization intervened. The manifest self-exclusion is sound,
and the terminal receipt independently binds the resulting manifest.

The dependency DAG is exactly
`F51 -> G53 -> P54 -> R56 -> Q57 -> T58`, with regular-file counts
51, 53, 54, 56, 57, and 58. The role fences and sole-write paths are distinct
and ordered. At the `R56` author stop, the receipt, `paper/reviews`, and this
review path were required to be absent; the terminal receipt records that
precondition. At the start of this review exact `Q57` contained the receipt
but still contained neither review directory nor review file.

Every external-effect field in the manifest and terminal receipt is false.
The candidate remains inside the local anonymous boundary; no external release
event has occurred.

## Direct live-root audit

Before cleanup, each of the following eight literal paths was a real,
non-symlink, root-owned mode-0700 directory whose real parent was exactly
`/tmp`. Every direct child was a root-owned regular non-symlink file; there
were no child directories or other entry types.

- `/tmp/paper21-r0-a.pDEi2V`: 19 direct files;
- `/tmp/paper21-r0-b.QB6qsy`: 13 direct files;
- `/tmp/paper21-r0-repair-a.rai5wu`: 16 direct files;
- `/tmp/paper21-r0-repair-b.WlpPpd`: 13 direct files;
- `/tmp/paper21-r1-a.cMLvZF`: 13 direct files;
- `/tmp/paper21-r1-b.2D6a87`: 13 direct files;
- `/tmp/paper21-terminal-a.yWwPV7`: 13 direct files; and
- `/tmp/paper21-terminal-b.dhlc6k`: 13 direct files.

The blocked-R0 roots shared `bibtex.stdout`, the six stable `main.*` outputs,
the source trio, and `pass1.stdout` through `pass3.stdout`; root A additionally
held `main.txt` and `page-17.pdf` through `page-21.pdf`. The repaired-R0 roots
shared the four `command-*.log` files, six stable outputs, and source trio;
root A additionally held `main.txt`, `page-01.png`, and `page-27.png`. Both R1
roots and both terminal roots each contained the expected 13-file build
inventory. I opened every child with no-follow semantics and rehashed its
complete bytes before cleanup.

The two terminal root inventories were equal entry for entry:

| Direct child in each terminal root | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `command-1.log` | 13,647 | 394 | `8e4b9c79ab49094bd267319a588882c92af64f9616af07629de7c6efaa92a0f0` |
| `command-2.log` | 158 | 4 | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` |
| `command-3.log` | 8,237 | 149 | `0b64bafc42c7ee9efee43856a97ec811b510206d52a7f7ed2bbfb7bb57084cc6` |
| `command-4.log` | 7,881 | 131 | `f6559cc9b105e42330b3d32c6e9f425dd9a0d71027126b51b623a3d54c28312d` |
| `main.aux` | 12,760 | 113 | `f203a377a6752a16ae22b61dd9c241a638081da2b7d54141ac62a2ab785d18c6` |
| `main.bbl` | 731 | 20 | `1be6c9b14cae6da54ed8ab04d9739d0bb02ccc363f52ac6ad69b2c2dcf19a1de` |
| `main.blg` | 885 | 46 | `4ef0e5c28c45d31e9cd0f4459679b0a06bfaa2555498a2f87c6b6e68f588d804` |
| `main.log` | 28,677 | 731 | `16fd0f29941ecb708e247d64db4fa7fdfdb00c8222804f09d1058054d2daef0e` |
| `main.out` | 4,090 | 16 | `25820119b32d0994e23555952047c4fe7ddce7a140420b21a1817b9e9141208c` |
| `main.pdf` | 465,922 | 2,539 | `b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3` |
| `main.tex` | 84,917 | 1,990 | `34074c5965086d79145bf2b273398c4c17fdc264b6f5e3555fd1b9a2bd27c7b2` |
| `math_commands.tex` | 981 | 33 | `05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a` |
| `references.bib` | 675 | 19 | `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8` |

All 13 A/B pairs were byte-identical and matched both receipt snapshots. The
three source copies matched the frozen project source. The two terminal PDFs,
the three persisted round PDFs, and the release candidate formed the required
six-way byte-equality set at 465,922 bytes and SHA-256 `b02785a0...`.

## Terminal build protocol and final diagnostics

Both terminal roots used an environment cleared before exact assignment of:

```text
SOURCE_DATE_EPOCH=1787356800
FORCE_SOURCE_DATE=1
TZ=UTC
LC_ALL=C
LANG=C
PATH=/usr/bin:/bin
```

Each root ran, in its own exact working directory:

```text
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
/usr/bin/bibtex main
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
```

The receipt binds all eight combined stdout/stderr logs, all four commands per
root, and eight zero exit codes. Direct log inspection confirmed pdfTeX
1.40.22, BibTeX 0.99d, a complete 27-page output on every LaTeX pass, and a
final 465,922-byte PDF. Fresh-root first- and third-pass citation/reference
warnings were ordinary convergence diagnostics and were byte-identical across
the two roots; they were absent from the fourth pass. In the receipt's declared
diagnostic scope of final `main.log` plus `main.blg`, each root had:

- zero fatal errors and emergency stops;
- zero undefined references and citations;
- zero LaTeX, package, pdfTeX, or BibTeX warnings (`warning$ -- 0` is a BibTeX
  function-count line, not a warning);
- zero overfull boxes;
- exactly seven authorized, nonblocking underfull boxes, at source lines 191,
  199, and 345--349; and
- zero `??`, `[?]`, `TODO`, `FIXME`, `TBD`, or `VERIFY` markers.

## PDF, page contract, security, anonymity, and visual audit

Direct Poppler and Ghostscript inspection of both terminal PDFs passed. The
PDF is version 1.5, unencrypted, 27 pages of 612-by-792-point letter paper, and
all 27 pages have rotation zero. Section 8 begins on page 26; conclusion text
continues and ends on page 27; `References` begins later on page 27. The body
through conclusion therefore occupies page 27 and satisfies the locked 24--29
substantive-page band.

The metadata is exactly:

- title `Three-Mode Hamiltonian Shears in A6: Exact Degree Growth and Cubic Perron Subfamilies`;
- author `Anonymous Authors`;
- creator `LaTeX with hyperref`;
- producer `pdfTeX-1.40.22`;
- empty subject and keywords; and
- raw creation and modification dates `D:20260822000000Z`, decoded as
  `2026-08-22T00:00:00Z`.

All 25 font rows are embedded, subsetted, and Unicode mapped. `pdfimages`
listed zero images, `pdfdetach` listed zero embedded files, `Form` is `none`,
JavaScript is absent, encryption is absent, and no `AcroForm`, XFA, launch,
rich-media, collection, or embedded-file object was found. Ghostscript
`nullpage` parsing returned zero for both PDFs. The only URL annotations are
the two locked arXiv URLs on page 27.

Rendered text and raw PDF strings contain no local path, digest, build receipt,
manifest, review filename, model/provider name, email, ORCID, affiliation,
acknowledgment, funding statement, workflow marker, or private identity. The
title page and metadata both use `Anonymous Authors`.

I rendered all 27 pages at low detail and inspected three nine-page contact
sheets. I then inspected pages 1, 13, 18, 25, and 27 at high detail, covering
the title/theorem opening, selector/cone ledger, six-coordinate phase table,
mod-five table and characteristic-polynomial proof, and conclusion/references.
There is no blank or duplicated page, clipping, crop loss, overlap, missing
glyph, broken table rule, bad rotation, or anonymity leak. The intentionally
short final reference page is clean. All temporary text, raster, and contact-
sheet inspection files were removed before this review was written.

## Citations and theorem-critical mathematics

The source has exactly two citation commands, for
`BlancVanSanten2019` and `ShaoSun2025`; the auxiliary file has exactly those
two citation and bibcite keys, the bibliography has two entries, and the BBL
has two bibitems. The rendered references are Jérémy Blanc--Immanuel van
Santen and Enbo Shao--Xiaosong Sun. Both citations remain contextual and are
not used to prove symplecticity, selection, recurrence, visibility,
irreducibility, priority, or firstness.

I independently checked the theorem-critical identities from the displayed
source, without CAS or numerical sampling:

- the potentials are
  `V=q1^2 q2^2 q3^2+q1^g` and `W=p1^2 p2^2 p3^2+p3^g`, over an algebraically
  closed characteristic-zero field with integer `g>=8`;
- the six gradient support rows give
  `A=((g-1,0,0),(2,1,2),(2,2,1))` and
  `B=((1,2,2),(2,1,2),(0,0,g-1))`;
- row-by-row multiplication gives
  `C=BA=((g+7,6,6),(2g+4,5,4),(2(g-1),2(g-1),g-1))`;
- the strict cone is `x,y>=1`, `x+y<(g-3)/2`;
- direct score subtraction gives
  `M_S=(g-2)-2x-2y` and, only after `v=A u`,
  `M_T=(2g-6)x+(g-6)y-6`; all other support rows are singletons;
- with `h=g-3-2x-2y`, the exact facial identities are
  `M_S=1+h` and `X'-1=(x+h)/D`; the `Y'-1` numerator is bounded below by
  `4g-24`;
- the height numerator is
  `Q=g^2-4g-25+2(g-12)x+4(g-6)y`. For `8<=g<=11`, substituting the upper
  cone face gives `Q>2g^2-17g+11=3+(g-8)(2g-1)`; for `g>=12`, lower faces
  give `Q>=g^2+2g-73=95+(g-12)(g+14)`;
- the phase convention is exactly `v_(n+1)=A u_n`,
  `u_(n+1)=C u_n`. The T carry is `(C-I)u_n>0`, including the seed, and the
  S carry is `A(u_n-u_(n-1))>0`. Positive support coefficients survive in
  characteristic zero;
- `C-A` is entrywise positive, while the two internal q-row differences are
  `-6+(2g-7)x+(g-5)y` and `g-9+(2g-8)x+(g-7)y`. Thus the third q-coordinate
  is uniquely visible and
  `deg(F_g^n)=e_3^T C^n 1` for every `n>=0`, with
  `lambda_1(F_g)=rho(C)`;
- trace `2g+11`, principal-minor sum `g^2-16g+19`, and determinant
  `9(g-1)^2` give
  `t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2`; and
- modulo five, the classes 2, 3, and 4 give respectively
  `t^3+t+1`, `t^3-2t^2-1`, and `t^3+t^2+t-1`, with displayed value rows
  `(1,3,1,1,4)`, `(4,3,4,3,1)`, and `(4,2,3,3,3)`. None has an F5 root.

The manuscript keeps the `g=7` seed on the strict-cone boundary with
`M_S=1`, not at a selector tie. It states no generic Newton-fan theorem,
classification of arbitrary symplectic or affine-triangular automorphisms,
entropy, periodic-point, torus, conjugacy, absolute novelty, priority,
firstness, or CAS/numerical proof claim. The mod-five result is explicitly
one-sided and makes no assertion that the omitted residue classes are
reducible.

## Safe governed-root cleanup and final state

Only after every preceding audit passed, I revalidated all eight literal roots
and performed the cleanup authorized to the sole terminal-integrity reviewer.
For each root I opened the directory with no-follow semantics, enumerated only
its direct children, revalidated every child as a regular non-symlink file,
opened and rehashed it with no-follow semantics, unlinked each enumerated child
relative to the open directory, verified the directory was empty, revalidated
the directory inode, and called `rmdir` on the exact literal root. No recursive
delete, glob, wildcard, unresolved environment variable, or symlink traversal
was used.

Exactly 113 direct regular files were unlinked across the eight governed roots.
All eight roots and every enumerated child are absent. The complete project
snapshot remained byte-identical at SHA-256 `9d9cc9...`; `Q57` still had
57 regular files, four directories, and zero symlinks after cleanup. The
inspection temporaries were then removed, and no `/tmp/paper21-*` entry
remained.

Adding only the `paper/reviews` directory and this sole review advances exact
`Q57` to `T58`: 58 regular files, five project-relative directories, zero
symlinks, and zero other entries. The release candidate remains local,
anonymous, byte-frozen, and unchanged.

FINAL_INTEGRITY_PASS
RELEASE_CONFIRMED
