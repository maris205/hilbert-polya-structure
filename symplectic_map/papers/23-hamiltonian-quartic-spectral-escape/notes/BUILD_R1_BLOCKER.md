# Paper 23 — Deterministic R1 Build Blocker

Date: 2026-08-25 UTC  
Stage: post-root deterministic R1 no-op build failure  
Disposition: build authority consumed; no success persistence; no retry

## 1. Binding authority and frozen opening state

The parent consumed the R1 authorization before this builder acted.  The
builder-opening gate was exactly
`PAPER23_DETERMINISTIC_R1_BUILD_OPEN`, and the Paper 23 queue was exactly
`R1_BUILD_AUTHORIZED`.  The post-consumption governance roots read through
EOF and frozen by the builder were:

| Root | SHA-256 | Bytes / LF | Device / inode | Mode / owner / links | Final nonempty line |
|---|---|---:|---:|---|---|
| `BATCH_06_STATUS.md` | `987f976b520d8b8b59b557030aa453db40d7f33b1d22b039f82cb359db6dd712` | 105,855 / 1,553 | 2431 / 12439253850 | 0644 / root:root / 1 | `finalization, release, Paper 24, and every external effect remain closed.` |
| `BATCH_06_IDEA_REPORT.md` | `2f043ae80524511f2d7805b343615026dfb2260fc4b3bd24ed577e4405e4bfd3` | 173,800 / 3,246 | 2431 / 12439253853 | 0644 / root:root / 1 | `work, network action, or external effect is authorized.` |
| `BATCH_06_PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTION.md` | `27615c425261aa72caa4c880b6bc7f54ecfa98c99399a2d7efc78ed19d8282c4` | 8,524 / 245 | 2431 / 12439253857 | 0644 / root:root / 1 | `PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTED_PASS` |

The governing authorization was
`notes/BUILD_AUTHORIZATION_R1.md`, SHA-256
`156605ab96edba550af97f61e3f2484d9aca63743ec1ed570dd594c7cc310924`,
48,400 bytes and 749 LF, ordinary root-owned mode 0644 with link count one,
ending exactly `BUILD_AUTHORIZATION_R1`.  It expressly makes every clause a
hard conjunct and forbids a clean or byte-identical PDF from compensating for
one false date-omission clause.

The complete builder-opening project universe was exactly 48 ordinary
regular files, four child directories, zero symlinks, zero other objects,
and 2,012,029 regular-file bytes.  Its nine-field manifest was 6,709 bytes
and 48 LF with SHA-256
`86b420dda8fcbf637ecfb85e535de554208d5740b7ece46a735e3af2c12a3272`.
Every opening path remained byte- and inode-stable up to this failure
disposition.  Before root creation and again immediately before this blocker,
all four downstream paths were absent:

- `paper/main_round1.pdf`;
- `paper/BUILD_METADATA_R1.json`;
- `paper/BUILD_RECEIPT_R1.json`;
- `notes/BUILD_R1_BLOCKER.md`.

## 2. Authority consumption and retained fresh roots

Pre-root preflight passed.  It independently reproduced the 48-file
manifest, the governance roots, gate and queue, authorization identity,
frozen source trio, no-op source receipt, all four downstream absences, and
three-way live executable identities.  It created no root and performed no
project write.

Authority was then consumed irrevocably by creation of fresh root A.  The two
independently allocated retained roots are:

| Root | Canonical path | Mode / owner | Device / inode | Links |
|---|---|---|---:|---:|
| A | `/tmp/paper23-r1-noop-A.e2oejfix` | 0700 / root:root | 149 / 5905639316 | 3 at failure evidence checkpoint |
| B | `/tmp/paper23-r1-noop-B.xc72gwxv` | 0700 / root:root | 149 / 6445715778 | 2 at failure evidence checkpoint |

Each root began with exactly three independently copied ordinary mode-0644,
link-count-one source files, with inodes distinct from the project and the
other root.  Each of the eight build child processes received an empty
environment populated with exactly:

```text
PATH=/usr/bin:/bin
SOURCE_DATE_EPOCH=1787616000
FORCE_SOURCE_DATE=1
TZ=UTC
LC_ALL=C
LANG=C
```

Each root ran exactly once, in order, with no retry or substitute:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Both exit vectors are exactly `[0,0,0,0]`.  Dynamic observations at pre-root
and every command boundary repeatedly resolved `/usr/bin/pdflatex` to
`/usr/bin/pdftex`, SHA-256
`01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9`,
1,802,504 bytes and 4,629 LF, and `/usr/bin/bibtex` through
`/etc/alternatives/bibtex` to `/usr/bin/bibtex.original`, SHA-256
`c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f`,
117,128 bytes and 393 LF.  Python streaming, GNU `sha256sum`, and OpenSSL
SHA-256 agreed at every recorded boundary.  These clean facts do not
compensate for the date blocker below.

## 3. Noncompensatory equality, diagnostics, structure, and visual facts

The corresponding source trio, four command logs, and six final outputs were
directly byte-identical across fresh roots A and B and both permitted
corrected-R0 comparator roots.  Their common identities are:

| Object | SHA-256 | Bytes / LF |
|---|---|---:|
| `main.tex` | `1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0` | 67,408 / 1,776 |
| `math_commands.tex` | `a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d` | 420 / 13 |
| `references.bib` | `ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782` | 2,812 / 99 |
| `command-1.log` | `1fcbc0319012bbeb4fd526dad9eef6a0ca9e86474e9c092ae766a70a4ef466ce` | 18,124 / 597 |
| `command-2.log` | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` | 158 / 4 |
| `command-3.log` | `cba30ead0e25a854366d5bf7e9156ffadfb713fd4de7097a43b6f284e1d2db72` | 8,363 / 158 |
| `command-4.log` | `ad3eb1bf23dd06e82b1683ccb3e66c34b142303fa24685f56f268f58368612b0` | 7,254 / 112 |
| `main.aux` | `2748935c255778a4e40227c008adeb8c361a3933a9ff5f545407f04ae48c8eeb` | 14,072 / 165 |
| `main.bbl` | `baa229dd7d35d96b27d7dfb18a844db73c98b752df3be4c008d748636f199cf9` | 2,881 / 73 |
| `main.blg` | `be7e80a71c65ef8bbfcc2e43c3aadcc0b89cb8216e61a785ca24403ec6c04c34` | 900 / 46 |
| `main.log` | `ab451da731a6ef13c7f1f83e9de463b4b2d71b0cb255e10b2d831a235aaa13f6` | 27,628 / 700 |
| `main.out` | `14be6d78b541eb75e29cec5bf18d1e9a26bfb0c128ddaa5f4c26ab00d315bb94` | 6,226 / 28 |
| `main.pdf` | `ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37` | 492,452 / 2,724 |

Both fresh PDFs are also directly byte-identical to immutable project
`paper/main.pdf` and `paper/main_round0.pdf`.  The diagnostic progression is
exactly `118/11`, `0/0`, `0/11`, `0/0`; final logs converge; closure checks
reproduce nine citations, nine `bibcite` entries, nine BBL items, 95 labels,
116 resolved references, and 28 bookmarks.  Structural inspection reports
PDF 1.5, 23 nonblank US Letter pages, xref length 640, 86 streams, 31 fully
embedded/subsetted/Unicode-mapped font rows, 135 internal links plus one safe
URI, and no dangerous PDF action.

Exactly 23 fresh 200-dpi page images were individually inspected at original
resolution.  The selector and cone pages, carry and survival arguments,
visibility, principal minors, quartic and recurrence, modulo-five proof,
`g=9` boundary, shifted kernels, limitations, three tables, and bibliography
were visually clear.  There was no clipping, overlap, bad glyph, missing or
duplicate page, citation artifact, or anonymity leak.  This visual PASS is a
true but noncompensatory observation.

## 4. Hard decoded-stream date blocker

Authorization Section 9.3 requires `CreationDate` and `ModDate` keys and
values to occur zero times in every decoded stream, and Section 9 makes that
date-omission rule a hard conjunct.  Fresh PyMuPDF 1.27.2.3 traversal of all
root-A xrefs called `xref_stream(xref)` and found the exact token
`CreationDate` 25 times in 25 distinct decompressed embedded Type1
font-program streams.  The exact xrefs are:

```text
520, 522, 524, 526, 528, 530, 532, 534, 536, 538, 540, 542, 544,
546, 548, 550, 552, 554, 556, 558, 560, 562, 564, 566, 568
```

The decoded lines are instances of:

```text
%%CreationDate: 7th October 2009
%%CreationDate: 16th September 2009
%%CreationDate: Mon Jul 13 16:17:00 2009
```

Root B independently reproduces the same 25 xrefs, decoded-stream hashes,
and lines because its PDF bytes are identical.  The full xref-by-xref ledger
is retained read-only at
`/tmp/paper23-r1-noop-A.e2oejfix/r1-validation-staging/DECODED_STREAM_DATE_BLOCKER_EVIDENCE.md`,
SHA-256
`89f6543c77bbbd0bea80289154a2379a53c00eac763d935e9d0ce91bb9d276e3`,
5,049 bytes and 71 LF, ordinary root-owned mode 0444 with link count one,
ending `DECODED_STREAM_DATE_BLOCKER_REPRODUCED`.

The compressed raw PDF contains zero `CreationDate`, zero `ModDate`, and
zero `D:` plus 14 digits plus `Z`.  `pdfinfo -rawdates` reports neither date
row, and xref 638 `/Info` has no `/CreationDate` or `/ModDate` dictionary
key.  Those metadata/raw zeros are not the required decoded-stream zero and
cannot compensate for 25 decoded occurrences.

The prior corrected-R0 direct review,
`notes/INDEPENDENT_BUILD_R1_R0_REPAIR_CORRECTION_REVIEW.md`, SHA-256
`98e709908c44f6a62dc11520649134be2c6b2830e2aecf6bbf6743a9889e6089`,
39,959 bytes and 702 LF, states at lines 579–581 that it searched all decoded
streams and that CreationDate and alternative date markers were absent in
every layer.  The fresh xref-level evidence directly falsifies that date
conclusion.  That review remains immutable historical bytes but is no longer
credited for its decoded-stream date claim.

Because the required count is zero and the observed count is 25, the R1
acceptance conjunction is false.  Equality, convergence, PDF safety, fonts,
and visual quality cannot change this result.

## 5. Candidate and persistence disposition

The parent hard-blocker instruction interrupted a generator tool call.  The
in-flight process had already completed two private root-A staging
candidates before the interruption became visible to the builder:

| Private retained non-artifact | SHA-256 | Bytes / LF |
|---|---|---:|
| `r1-validation-staging/BUILD_METADATA_R1.candidate.json` | `c5cfbaff5b3e3362c9daccfa76d2ef0c79a104bd90083c614ec41a1d4154b031` | 189,974 / 1 |
| `r1-validation-staging/BUILD_RECEIPT_R1.candidate.json` | `d0f7bd4e5e198bd032078a5116315aaa29ef551087be427d419938264d6e0e3d` | 38,858 / 1 |

They were never syntax-validated, never semantic-validated, never accepted,
and never persisted.  They are not project success artifacts and confer no
PASS meaning.  After blocker recognition they were neither patched nor
removed; they remain only as private failure evidence inside the retained
root.  No further candidate was generated.

The three project success paths never existed, so bounded rollback removed
nothing.  Immediately before this blocker was exclusively created, all three
were confirmed absent under no-follow checks:

- `paper/main_round1.pdf`;
- `paper/BUILD_METADATA_R1.json`;
- `paper/BUILD_RECEIPT_R1.json`.

This blocker is the sole project write of the failure branch.  It does not
authorize or perform a source edit, fifth TeX pass, second BibTeX run, retry,
replacement roots, cleanup, new builder, self-review, R2 review,
finalization, release, Paper 24 work, network action, or external effect.
Authority remains consumed.  Both fresh roots and all their evidence are
retained unchanged for later parent governance.  The failure project state
is exactly 49 regular files, four child directories, zero symlinks, and zero
other objects, with all three success paths absent.

R1_BUILD_BLOCKED
