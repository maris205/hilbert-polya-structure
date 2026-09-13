# Paper 23 — Deterministic R0 Repair-Build Blocker

Date: 2026-08-25 UTC  
Stage: one-shot deterministic R0 repair build  
Disposition: blocked after authority consumption; zero success paths persisted

## Decisive result

The one authorized repair-build invocation failed one hard PDF-metadata
conjunct.  Both fresh deterministic PDFs omit the raw `/CreationDate` and
`/ModDate` keys.  The governing authorization requires each raw value to be
exactly `D:20260825000000Z`.  An absent key is not that required value, and
the contract permits no waiver, retry, replacement root pair, source edit, or
partial success persistence.

The failure is reproducible from the frozen source.  Lines 1--3 of
`paper/main.tex` are

```tex
\ifdefined\pdfinfoomitdate
  \pdfinfoomitdate=1
\fi
```

so pdfTeX is explicitly instructed to omit its automatically generated PDF
date information.  The builder did not modify this or any other source.

## Opening preflight and consumed authority

Before either build root was created, a read-only preflight passed every
opening condition:

- `BATCH_06_STATUS.md` was SHA-256
  `bee1840d89e9319a81983d6f32f69010f82958763c6aedf55dfd0de27d43d437`,
  82,037 bytes / 1,211 LF / mode 0644 / root:root / link count one.  Its
  final nonempty line was `  root hashes below, not either diagnostic
  pre-correction hash.`
- `BATCH_06_IDEA_REPORT.md` was SHA-256
  `a1dea9ce6a0938a79b818fe4a813b9f23554b06559a0cc35252085c33e8db361`,
  130,521 bytes / 2,505 LF / mode 0644 / root:root / link count one.  Its
  final nonempty line was `identity disclosure, and every external effect
  remain unauthorized.`
- `BATCH_06_PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTION.md` was SHA-256
  `27615c425261aa72caa4c880b6bc7f54ecfa98c99399a2d7efc78ed19d8282c4`,
  8,524 bytes / 245 LF / mode 0644 / root:root / link count one, ending
  uniquely with `PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTED_PASS`.
- The live gate was exactly
  `PAPER23_DETERMINISTIC_R0_REPAIR_BUILD_OPEN`, and the Paper-23 queue was
  exactly `R0_REPAIR_BUILD_AUTHORIZED`.
- Both root ledgers bound the final authorization at
  `notes/BUILD_AUTHORIZATION_R0_REPAIR.md`, SHA-256
  `d2af138c12d3abc59dce9d7950a7e53113e2b1f8c1b312a1d4803c3b5cc8d207`,
  25,966 bytes / 428 LF / mode 0644 / root:root / link count one, with its
  required unique terminal.
- The complete 28-row issuance ledger matched byte-for-byte and the
  authorization-added opening inventory was exactly 29 regular files, four
  directories, zero symlinks, and zero other objects.  The project and its
  four child directories were ordinary mode-0755 root:root directories.
- `notes/BUILD_R0_REPAIR_BLOCKER.md` and all nine authorized success paths
  were absent under both existence and symlink checks.
- The old diagnostic roots `/tmp/paper23-r0-A.DyWKGR` and
  `/tmp/paper23-r0-B.dsQvTx` were not read, reused, copied, linked, cached, or
  written.

The authority was consumed by the first fresh-root creation.  The two roots
were created atomically and independently by distinct `mktemp -d` templates:

| Root | Canonical path | Mode / owner | Device / inode |
|---|---|---|---|
| A | `/tmp/paper23-r0-repair-A.BzlBNd` | 0700 / root:root | 149 / 6981313815 |
| B | `/tmp/paper23-r0-repair-B.TVRci7` | 0700 / root:root | 149 / 7517921828 |

Each initial root contained exactly the three mode-0644, link-count-one
source copies below and no other object.  Every root copy had an inode
distinct from the project copy and the corresponding copy in the other root.

| Source | SHA-256 | Bytes / LF | Root-A inode | Root-B inode |
|---|---|---:|---:|---:|
| `main.tex` | `1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0` | 67,408 / 1,776 | 6981313816 | 7517921829 |
| `math_commands.tex` | `a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d` | 420 / 13 | 6981313817 | 7517921830 |
| `references.bib` | `ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782` | 2,812 / 99 | 6981313818 | 7517921831 |

## Exact execution evidence

`pdflatex` resolved through `/usr/bin/pdflatex -> pdftex` to
`/usr/bin/pdftex`, SHA-256
`01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9`,
1,802,504 bytes.  `bibtex` resolved through `/usr/bin/bibtex` and the Debian
alternative to `/usr/bin/bibtex.original`, SHA-256
`c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f`,
117,128 bytes.

Every one of the eight build child processes received exactly this six-pair
environment and no other variable:

```text
PATH=/usr/bin:/bin
SOURCE_DATE_EPOCH=1787616000
FORCE_SOURCE_DATE=1
TZ=UTC
LC_ALL=C
LANG=C
```

With each fresh root as its exact working directory, the builder ran exactly
once and in order, without retry or fifth command:

1. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
2. `bibtex main`
3. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
4. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`

Both exit vectors were exactly `0,0,0,0`.  Captured merged streams were
pairwise byte-identical by command index:

| Stream | SHA-256 | Bytes / LF |
|---|---|---:|
| `command-1.log` | `1fcbc0319012bbeb4fd526dad9eef6a0ca9e86474e9c092ae766a70a4ef466ce` | 18,124 / 597 |
| `command-2.log` | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` | 158 / 4 |
| `command-3.log` | `cba30ead0e25a854366d5bf7e9156ffadfb713fd4de7097a43b6f284e1d2db72` | 8,363 / 158 |
| `command-4.log` | `ad3eb1bf23dd06e82b1683ccb3e66c34b142303fa24685f56f268f58368612b0` | 7,254 / 112 |

The final six outputs were also pairwise byte-identical and remained stable
through the final checkpoint:

| Output | SHA-256 | Bytes / LF |
|---|---|---:|
| `main.aux` | `2748935c255778a4e40227c008adeb8c361a3933a9ff5f545407f04ae48c8eeb` | 14,072 / 165 |
| `main.bbl` | `baa229dd7d35d96b27d7dfb18a844db73c98b752df3be4c008d748636f199cf9` | 2,881 / 73 |
| `main.blg` | `be7e80a71c65ef8bbfcc2e43c3aadcc0b89cb8216e61a785ca24403ec6c04c34` | 900 / 46 |
| `main.log` | `ab451da731a6ef13c7f1f83e9de463b4b2d71b0cb255e10b2d831a235aaa13f6` | 27,628 / 700 |
| `main.out` | `14be6d78b541eb75e29cec5bf18d1e9a26bfb0c128ddaa5f4c26ab00d315bb94` | 6,226 / 28 |
| `main.pdf` | `ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37` | 492,452 / 2,724 |

The three project sources and both copied trios retained their exact frozen
identities at the final checkpoint.  All paired sources, four logs, and six
outputs were directly byte-compared equal.  No hard link or symlink was used.

## Successful diagnostic observations before the hard failure

These facts do not waive or compensate for the failed metadata conjunct:

- Every command log had zero fatal error.  Command 1 recorded expected
  convergence warnings (118 LaTeX warnings and 11 package warnings), and
  command 3 recorded 11 expected natbib convergence warnings.  Command 4 and
  final `main.log` each had zero LaTeX warning, package warning, hyperref
  PDF-string warning, undefined citation/reference warning,
  multiply-defined-label warning, changed-label/rerun warning, overfull box,
  and underfull box.  Both BibTeX streams and final `main.blg` had zero BibTeX
  error and zero BibTeX warning.
- The source contained exactly nine citation commands and exactly the nine
  authorized distinct keys.  Final AUX citation and bibcite sets and the nine
  nonduplicate BBL items were exactly closed; the bibliography contained
  exactly those nine cited entries, with `plainnat` and `references` recorded
  in the AUX.  All citations remained in the bounded related-work passage.
- Final `main.out` had 28 readable bookmarks.  It contained plain safe `g=9`
  text and the exact bookmark `The restricted boundary at g=9`, with no raw
  math shift, `texorpdfstring` token, unresolved token, or governance text.
- The PDFs were byte-identical, readable by Poppler, PyMuPDF, and Ghostscript,
  unencrypted, 23 pages, US Letter on every page, and rotation zero.  Poppler
  reported no form and no JavaScript; `pdfdetach` reported zero embedded
  files; `pdfimages -list` reported zero image objects.  PyMuPDF found zero
  widgets, ordinary internal GoTo navigation, one visible arXiv URI, and none
  of the prohibited JavaScript, Launch, SubmitForm, ImportData, embedded-file,
  AcroForm, XFA, or rich-media keys.
- `pdffonts` reported 31 nonzero font rows, every one embedded, subsetted, and
  Unicode mapped.
- The decoded title was exactly `Four-Mode Hamiltonian Product Shears Beyond
  Cubic Collapse: Exact Degree Growth and Quartic Perron Subfamilies`; visible
  author text was exactly `Anonymous`; decoded `Author`, `Creator`, and
  `Producer` were empty.  No visible document date or private governance text
  was present.
- Fresh extracted-text and visual checks located Abstract on page 1, the
  repaired boundary subsection and Section 9 on page 20, Conclusion entirely
  on page 22, and References on page 23, with no appendix.  The substantive
  span was pages 1--22: hard band true, preferred band false, and planning
  target false.  All 23 pages were rendered at 160 dpi (1360 by 1760 pixels)
  and inspected at readable scale.  No page was blank, corrupt, clipped, or
  beyond its boundary; all three tables on pages 7, 10, and 15 were readable,
  and the visible repaired heading rendered mathematically as `g=9`.

## Exact failed metadata evidence

The date failure was observed independently in both byte-identical PDFs:

1. `pdfinfo -rawdates main.pdf` printed no `CreationDate` line and no
   `ModDate` line.
2. PyMuPDF 1.27.2.3 decoded both `metadata.creationDate` and
   `metadata.modDate` as the empty string.
3. An exhaustive PyMuPDF scan of all 639 nonzero xrefs found zero occurrence
   of `/CreationDate`, zero occurrence of `/ModDate`, and zero occurrence of
   `D:20260825000000Z`.
4. The actual Info dictionary at xref 638 contained the exact title, empty
   Author/Subject/Creator/Producer/Keywords, and `/Trapped /False`, but no
   creation or modification date key.  The PDF had no metadata stream.

The required fields are therefore absent, not merely formatted differently.
This single false hard conjunct fixes the invocation disposition as failure.

## Failure persistence and final immutability

No success JSON candidate was constructed or validated, no private or project
`main_round0.pdf` was created, and none of the nine success paths was staged
or persisted.  Immediately before this blocker was written, all nine remained
absent under existence and symlink checks and the project remained 29/4/0/0.
This blocker is the sole authorized new project path, making the expected
post-blocker inventory 30 regular files, four directories, zero symlinks, and
zero other objects.

At the final pre-blocker checkpoint the status root, idea root, correction
root, authorization, complete 28-file issuance ledger, old blocker, repair
receipt, both repaired-source reviews, and frozen source trio were unchanged.
Both fresh roots are retained for independent forensic inspection.  Root B
retains its exact 13 post-command files.  Root A additionally retains only
private read-only validation derivatives created after command 4, including
page renders and per-page structural probes; these are outside the project,
are not a third build root, and never entered either build.

Authority was consumed and cannot be resumed.  This record authorizes no
source repair, second root pair, retry, R1 action, release, Paper-24 action,
submission, upload, transport, or external effect.

R0_REPAIR_BUILD_BLOCKED
