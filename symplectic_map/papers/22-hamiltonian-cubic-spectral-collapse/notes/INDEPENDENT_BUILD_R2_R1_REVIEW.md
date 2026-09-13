# Paper 22 — Independent R2 Review of the Deterministic R1 No-Op Build

Date: 2026-08-24 UTC  
Stage: fresh post-R1 build review  
Reviewer role: independent of the source, repair, authorization, build, and
R1 revision roles  
Disposition: PASS with zero required findings and zero cosmetic findings

## Review boundary and opening freeze

I performed a read-only review of the accepted R0 and R1 build evidence.  I
did not invoke TeX, BibTeX, `latexmk`, a source generator, a scientific/CAS
program, or a network service.  The only temporary writes were reviewer-owned
PNG renders in a new private scratch directory.  Those files were removed by
explicit no-follow checks and unlinks after all visual observations and
identities had been recorded.  The only project write is this review.

The opening parent state independently matched the authorization given to
this reviewer:

| Opening artifact or state | Independently observed value |
|---|---|
| `BATCH_06_STATUS.md` | SHA-256 `dc6e616fd011b6d719a028dcd80440520bd7960a60f37df213a5702dcf0e16fd`; 37,114 bytes; 575 LF |
| current gate | `PAPER22_R1_BUILD_R2_REVIEW_OPEN` |
| Paper 22 queue | `R1_BUILD_PASS_PENDING_INDEPENDENT_R2_REVIEW` |
| `BATCH_06_IDEA_REPORT.md` | SHA-256 `b99cb2c10c14cd075a28f75877a5b9ae894a10794b04baf6ccc91c495db7e862`; 47,307 bytes; 929 LF |
| Paper 22 project | exactly 44 regular files, four direct child directories, zero symlinks |
| optional R1 blocker | absent |
| this review path | absent |

The exact 44-entry opening project manifest had SHA-256
`5f5f91744b77209910294be4acd5d1665d806019bf7b0bd58b2a3530333f9587`
under the reviewer framing `relative-path TAB sha256 TAB bytes TAB LF LF`; it
was 4,604 bytes and 44 LF.  All 44 opening project files had distinct
device/inode pairs.  None was hard-linked to a retained build-root file.
The two parent ledgers remained byte-identical to these opening values through
the final pre-write checkpoint.

The R1 JSONs bind the actual build-time parent ledgers separately from the
authorization author's earlier issuance ledgers.  The current append-only
`BATCH_06_IDEA_REPORT.md` prefix of 45,285 bytes and 894 LF independently
reproduces the recorded R1 build-time SHA-256
`c538e9a04d7a986c97d7478c8928eb2741f293050151e5729a9dedb30387c682`
and its recorded terminal line.  `BATCH_06_STATUS.md` is intentionally a
mutable gate/queue ledger: its header and queue row have since been changed
to this R2-review state and its R1-PASS activity appended.  Its current bytes
therefore properly differ from the historical build-time identity
`8c3139f7e7a47cc1c90bfd8e489d4ac6a21c53eb3ec26f71c520dbc76cab4ff9`
/ 35,209 bytes / 547 LF.  The current status activity and both R1 JSONs
agree on that historical build-open gate, queue, authorization binding, and
41-file pre-persistence state.  No issuance-time hash was incorrectly used
as a future build-time condition.

## Upstream lineage and frozen source

I rehashed the complete source/build lineage rather than relying on the
current PDF alone.  The relevant immutable terminals and identities are:

| Artifact | SHA-256 | Bytes | LF | Terminal/status |
|---|---|---:|---:|---|
| `experiments/source_lock.json` | `6f79231121f78e1c6b55da148c5710c2005e0ae36f92b0771740d127a253ad88` | 32,258 | 1 | schema version `paper22.source_lock.v1` |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `1fa152bdf1cf83a852b7e585e1e3aac402d06534c447a881e7506f082594846f` | 16,605 | 521 | `SOURCE_LOCK_PASS` |
| `experiments/publication_lock.json` | `3d7eb3c7ef143a17c1ccdb82ece985a05c916b78c1ebe0591bca8af3c05ce6cd` | 34,222 | 1 | schema version `paper22.publication_lock.v1` |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `65bfe3d7e24c6f9f4ec6a826f2d29a387c0105e208f4990226a4d22242f24512` | 16,536 | 388 | `PUBLICATION_STAGE_PASS` |
| `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md` | `21a35057011098de88b03518cbb4e24a27ee1cb998303e526fcd128188c99fa8` | 17,031 | 350 | `PUBLICATION_LOCK_PASS` |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | `20c7e7b49a2f698b509026bd025e5dd3ebf000ff6d3fa343466867e755d3951c` | 10,683 | 248 | `PAPER_PLAN_PASS` |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md` | `d38343539db88d1eeda555c464657e408df6ab58aa6ad7a811cd262f53038750` | 17,056 | 424 | `PAPER_SOURCE_R1_PASS` |
| `notes/BUILD_R0_BLOCKER.md` | `5242052c625add4ba084d5542faae221e6b1a1cb6d81b773b9295d968afbc7fd` | 5,873 | 145 | exact historical terminal `R0_BLOCKED` |
| `notes/R0_HYPERREF_SOURCE_REPAIR.md` | `0587269d6e5fcd4461a4749b6846d459c096d698dd460d2f4abf291463934ed5` | 7,553 | 189 | `SOURCE_REPAIR_FROZEN_DUAL_REVIEW_REQUIRED` |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_R0_REPAIR_REVIEW.md` | `6c02368dd361192628d4b79898b0a5fd9b273344d56e60179f52cb66dcc6d925` | 21,489 | 582 | `PAPER_SOURCE_R1_R0_REPAIR_PASS` |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_R0_REPAIR_REVIEW.md` | `8699472ce07744617c7407d051f84c2cca577c4d5e4ad4f9a0aa6f911ca1b0d5` | 26,796 | 891 | `PAPER_SOURCE_R2_R0_REPAIR_PASS` |
| `notes/BUILD_AUTHORIZATION_R0_REPAIR.md` | `8095586065f3f997125b29231ffcff28be1d099ecd01bedc22eb75b7809ee6ca` | 21,642 | 389 | `BUILD_AUTHORIZATION_R0_REPAIR` |
| `paper/BUILD_METADATA_R0.json` | `10797a9079fea64629a852dbf6644302a35ef2a96e8b05573eae9799f865345c` | 65,981 | 1 | `BUILD_METADATA_R0_REPAIR` |
| `paper/BUILD_RECEIPT_R0.json` | `4e7810b9ac2ad628503634539f0997a418aa4f583c9557ef6a5c41146b95dcec` | 66,318 | 1 | `BUILD_R0_REPAIR_PASS` |
| `notes/INDEPENDENT_BUILD_R1_R0_REPAIR_REVIEW.md` | `cc1d6f222ab500c10040c28f24bf3207fe5b0d645dc7a695e1406eb997e5f868` | 24,176 | 195 | `BUILD_R1_R0_REPAIR_PASS` |
| `notes/R1_REVISION_WINDOW_NO_CHANGE.md` | `4da8ff908be280bb9140eaf23ab60a726794ca9d6e2b95a4b2356fda8d350df3` | 2,729 | 68 | `R1_REVISION_WINDOW_NO_CHANGE` |
| `paper/SOURCE_REVISION_RECEIPT_R1.json` | `a77154a2150e74af115cb2ced4767f9617bafdb22267373b8128ebed09c3208d` | 3,967 | 1 | schema `PAPER22_SOURCE_REVISION_RECEIPT_R1_NO_OP_V1`; status `R1_NO_OP_REVISION_PASS` |
| `notes/BUILD_AUTHORIZATION_R1.md` | `cc64d8e294dce01d0e2e4dbc24a15007222dde04998c5598fee0eb5e35f7a634` | 19,746 | 353 | `BUILD_AUTHORIZATION_R1` |
| `paper/BUILD_METADATA_R1.json` | `ba621d379d805d4f7d9aae9b4233a02c79cf578605ad2a2d498d8b3613037af3` | 75,469 | 1 | schema `PAPER22_BUILD_METADATA_R1_NO_OP_V1`; status `BUILD_METADATA_R1_NO_OP` |
| `paper/BUILD_RECEIPT_R1.json` | `1a84c8af9e1f5ce74c0a7fb0a40c765885da43578561c78b0dc21c88790db966` | 75,628 | 1 | schema `PAPER22_BUILD_RECEIPT_R1_NO_OP_V1`; status `BUILD_R1_NO_OP_PASS` |

The only build source is still the exact repaired trio:

| Source | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `paper/main.tex` | `926c6fd083ee532b6ca5dde1a366e6c2cb93d0bfec855ac38944bcbac7fcc0a1` | 69,241 | 1,921 |
| `paper/math_commands.tex` | `544a046194ef6b0326609b79275f5f04595519354b11a9fb0a91356cacdb612c` | 330 | 11 |
| `paper/references.bib` | `50f8ed9f1f415bc53a32c39a437b35fb1a4cff066efb44e681804e293dd6a53d` | 1,928 | 55 |

The repair is exactly the intended source line 1,754 form
`\texorpdfstring{\(g=2r\)}{g=2r}`.  No other source identity changed.  The
no-op source receipt records one authorized and consumed revision window,
zero remaining windows, empty changed paths, and zero changed
paths/hunks/bytes/theorem/proof/title/citation/anonymity/anti-claim counts.
Its before and after source identities are equal to the table above.

## Retained roots, inventories, and byte determinism

All four accepted roots exist at their exact canonical paths and are
ordinary non-symlink directories of mode `0700`:

| Root | Device | Inode | Live nlink | Direct inventory |
|---|---:|---:|---:|---|
| `/tmp/paper22-r0-repair-A.0zGVu9` | 149 | 548226305 | 2 | 13 regular files, zero directories, zero symlinks |
| `/tmp/paper22-r0-repair-B.FwYPpz` | 149 | 1073892550 | 2 | 13 regular files, zero directories, zero symlinks |
| `/tmp/paper22-r1-noop-A.JMXTHF` | 149 | 13421874566 | 2 | 13 regular files, zero directories, zero symlinks |
| `/tmp/paper22-r1-noop-B.lEctAm` | 149 | 13959694139 | 2 | 13 regular files, zero directories, zero symlinks |

Every one of the 52 root files is regular, mode `0644`, and link count one;
all 52 device/inode pairs are distinct.  The R1 root-A directory's recorded
temporal nlink of three was observed while its builder-owned staging
subdirectory existed.  Its documented post-cleanup inventory is 13/0/0 and
its live nlink is now two, so there is no directory-state contradiction.
No staging or render residue remains in either R1 root.

The three sources, four command logs, and six outputs are byte-identical
between the two R1 roots.  Every corresponding R1 file is also byte-identical
to both accepted R0 roots.  The six current project outputs equal every root
copy.  The paired log identities are:

| Log | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `command-1.log` | `1775b04cad10c07ae781f497ffea53bb3e1a8d03dfaacf9ee2f313300fc5fe41` | 16,779 | 552 |
| `command-2.log` | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` | 158 | 4 |
| `command-3.log` | `7418c3d6b43f0c109246fe2bfdd39ec19e07a6c93e43ce55924f93bb44b2f9b7` | 8,372 | 156 |
| `command-4.log` | `0de737419e403fbfcca1c53d69ac98dbe55297e63de51697d8bca064d4c198c6` | 7,642 | 123 |

The output identities in the project and every retained root are:

| Output | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `main.aux` | `22a3bcd35b0aa9b87d6a4e40fe9f0cdc422fee366cf72e848be149486e5bcfb2` | 17,245 | 191 |
| `main.bbl` | `13faf55051bd94bf0cacdf4cae3b6476b77c417657bd8184b6f2446b1c28c3aa` | 1,738 | 45 |
| `main.blg` | `911285900fa9c373c657edd562d9cc284cd702194ab99094be5870613ef15f92` | 896 | 46 |
| `main.log` | `3f8a5951bda82725d0731f0fd17d4e6b506ed2084e48bb7a9663b69ab5924cb0` | 27,869 | 712 |
| `main.out` | `c732b3ddb9511976c30b5b00e10709c77c022636e419de173c10db9ce172093a` | 8,604 | 36 |
| `main.pdf` | `5316843486e1cdf68e9193bf6ad5efe3820543135e27ca6ee64d3a9579e488a7` | 471,647 | 2,649 |

Direct byte comparisons also prove
`paper/main.pdf == paper/main_round0.pdf == paper/main_round1.pdf`, each
with the PDF identity above.  The R1 receipt's complete 41-entry
pre-persistence manifest matches every still-live opening path; the only
three later paths are the authorized R1 metadata, receipt, and round-one PDF.

The two recorded exit vectors are `0,0,0,0`.  The bound command sequence is
exactly `pdflatex -interaction=nonstopmode -halt-on-error main.tex`,
`bibtex main`, followed by the same `pdflatex` command twice.  The bound
empty inherited environment contains exactly `PATH=/usr/bin:/bin`,
`SOURCE_DATE_EPOCH=1787529600`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`,
`LC_ALL=C`, and `LANG=C`.  The current executable checks independently give
`/usr/bin/pdflatex -> /usr/bin/pdftex`, SHA-256
`01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9`,
and `/usr/bin/bibtex -> /usr/bin/bibtex.original`, SHA-256
`c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f`.
No fifth pass, retry, replacement root pair, shell-escape argument, or
source-side shell command is present.

## Independent strict audit of all seven JSON artifacts

I treated all seven JSON files as untrusted bytes.  The first implementation
used CPython 3.12.3 with duplicate-rejecting pair construction at every
depth, nonfinite rejection, strict UTF-8 decoding, recursive code-point key
order, and a handwritten compact encoder.  The second used Node v22.22.2
with a separate handwritten recursive-descent tokenizer/parser, surrogate
handling, duplicate-key sets, numeric canonicalizer, code-point comparator,
and encoder.  It did not use `JSON.parse` or `JSON.stringify` for the value
tree.

Both implementations independently established zero BOM, CR, NUL, invalid
UTF-8, insignificant whitespace, duplicate key, unsorted object, nonfinite
number, and trailing content; exactly one terminal LF; and byte-exact
canonical round trips with the live hashes.  Both rejected adversarial
top-level and nested duplicates, `NaN`, positive and negative infinity,
trailing content, BOM, CR, internal LF, NUL, malformed UTF-8, and unsorted
objects.  Their structural counts agreed:

| JSON | Objects | Objects below `checks` | Arrays | Integers | Floats |
|---|---:|---:|---:|---:|---:|
| `source_lock.json` | 72 | 0 | 32 | 47 | 0 |
| `publication_lock.json` | 77 | 0 | 37 | 109 | 1 |
| `BUILD_METADATA_R0.json` | 391 | 199 | 57 | 1,311 | 0 |
| `BUILD_RECEIPT_R0.json` | 393 | 199 | 57 | 1,315 | 0 |
| `SOURCE_REVISION_RECEIPT_R1.json` | 27 | 0 | 3 | 49 | 0 |
| `BUILD_METADATA_R1.json` | 441 | 207 | 59 | 1,448 | 0 |
| `BUILD_RECEIPT_R1.json` | 442 | 207 | 59 | 1,450 | 0 |

The one finite float is the authorized publication target `26.5`.  The two
historical R0 build JSONs intentionally have no top-level `schema` key; their
required statuses are exact.  Every lock self-exclusion and every receipt or
build self identity has `bytes:null` and `sha256:null` (with the required
path/reason fields where applicable).  The R1 metadata and receipt differ
only at their artifact path, schema, status, self path, receipt-only metadata
external identity, and the consequent object-count fields.  The receipt
binds the finalized metadata exactly as SHA-256
`ba621d379d805d4f7d9aae9b4233a02c79cf578605ad2a2d498d8b3613037af3`,
75,469 bytes, one LF, path `paper/BUILD_METADATA_R1.json`.

A recursive live-identity audit found that every currently addressable
identity object matches its file.  The only non-live identities are
explicitly historical builder render files documented as removed.  The only
live paths whose current full bytes properly differ from recorded identities
are the explicitly temporal root-ledger snapshots after later parent
transitions.  This distinction is recorded in both R1 JSONs and is not a
waiver of an artifact mismatch.

## Diagnostics and reference closure

I parsed warning starts and semantic events directly in both roots.  Since
all paired logs are byte-identical, the following counts hold independently
for A and B:

| Surface | Fatal | LaTeX warnings | Package warnings | Undefined citations | Undefined references | Changed/rerun | Overfull | Underfull |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| command 1 | 0 | 100 | 8 | 7 | 99 | 2 | 0 | 3 |
| command 2 / BibTeX | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| command 3 | 0 | 0 | 8 | 7 | 0 | 1 | 0 | 3 |
| command 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| final `main.log` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| final `main.blg` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

The first-pass totals are transparent semantic counts: six individual
undefined-citation messages plus one plural summary line give seven, and 98
individual undefined-reference messages plus one plural summary line give
99.  The underlying command-1 bytes are identical to both accepted R0
command-1 logs.  Command 3 has the same six individual citation messages
plus one summary, followed by the citation-change event.  All convergence
messages are absent from command 4 and the final state.

The only final diagnostics are exactly three underfull `hbox` events, all at
source line 944 with badness sequence `6316,10000,6316`.  Their log-line
positions are command 1 lines 239/243/250, command 3 lines 114/118/121,
command 4 lines 90/94/97, and final `main.log` lines 648/654/659.  Event-
specific parsing avoids mistaking the `infwarerr` package description
“error messages” for an actual error.  Detailed visual review confirms that
the associated Table 2 cells wrap completely and legibly.

The final AUX has exactly four citation commands, six distinct keys, 121
new labels, six `bibcite` keys, one `plainnat` style, one `references`
bibliography, and absolute last page 26.  Source scanning finds 121 unique
labels and 98 `ref`/`eqref` uses, with zero missing labels.  The BBL declares
six items and contains exactly six unique `bibitem`s; the BLG reports six
used entries and zero warning/error.  The bibliography source contains the
same six entries and no seventh entry.

The four source citation commands occur at lines 276, 283, 290, and 296 and
use exactly `BlancVanSanten2021`, `ShaoSun2025`, `Deserti2016`,
`DangFavre2021`, `Rangarajan2002`, and
`FujiokaKogawaLiShudo2023`.  They provide bounded context for adjacent
literature, not proof transfer for any selector, cone, carry, leading-form,
matrix, visibility, cubic, multiplicity, boundary, coefficient, or threshold
claim.

The OUT has 36 syntactically readable UTF-16BE bookmarks and the PDF outline
has the same 36 resolved destinations.  Bookmark 32 decodes exactly as
`The g=2r seed/selected-face boundary`.  There is no raw failed math token,
unresolved destination, or private provenance.

## PDF structure, safety, identity, and boundaries

Independent `pdfinfo`, `pdffonts`, `pdfimages`, `pdfdetach`, `pdfsig`,
Ghostscript, Poppler text extraction, and PyMuPDF 1.27.2.3 checks agree:

- the file is valid PDF 1.5, 471,647 bytes, 26 pages, unencrypted, and needs
  no password; Ghostscript `-dSAFER` null-page processing succeeds for both
  R1 roots through page 26;
- every page and every Media/Crop/Bleed/Trim/Art box is exactly US Letter
  `612 x 792` points with rotation zero; all pages have positive text, and
  no extracted word box lies outside its page;
- `pdffonts` reports exactly 28 nonzero font rows, all embedded, subsetted,
  and Unicode mapped; PyMuPDF independently finds 28 page font xrefs;
- `pdfimages` and page inspection find zero image objects and zero page
  images; there are zero embedded files, attachments, widgets, forms,
  AcroForms, XFA, signatures, multimedia objects, or encryption;
- object dictionaries contain zero JavaScript, launch, submit/import,
  external-GoTo, embedded-file, signature, rich-media, movie, sound, or
  file-spec action.  Catalog xref 712 has one safe OpenAction, xref 146,
  exactly `/S /GoTo` to page 1 with `/Fit`;
- there are exactly 148 ordinary GoTo action dictionaries: 111 page links,
  36 outline entries, and the one OpenAction.  Eight ordinary URI action
  dictionaries account for 16 raw `/URI` literals and point only to the six
  displayed bibliography destinations.  No dangerous action is hidden by
  the raw-token count;
- the title is exactly “Cubic Spectral Collapse for Endpoint-Spiked
  Hamiltonian Product Shears: Sharp Selector Thresholds in Arbitrary Mode
  Number”; the visible author is exactly `Anonymous`, once; PDF Author,
  Creator, Producer, Subject, and Keywords are empty;
- `1787529600` converts to `2026-08-24T00:00:00Z`; raw CreationDate and
  ModDate are each exactly `D:20260824000000Z`.  The custom PTEX full-banner
  is the standard deterministic pdfTeX compiler banner, not private author,
  reviewer, model, workspace, or governance provenance;
- Poppler and PyMuPDF extract nonempty text on all 26 pages.  Abstract begins
  on page 1; Section 8 begins on page 24; Limitations and Conclusion begin on
  page 26; Conclusion ends before References; References begins and ends on
  page 26; there is no appendix.  The 26-page physical body preserves the
  recorded 26.5-page target convention, lies in the preferred 24–28 band,
  and lies in the hard 22–30 band.

Independent scans of Poppler text, PyMuPDF text, metadata, bookmarks, and
object dictionaries found zero `TODO`, `TBD`, `FIXME`, `VERIFY`, citation-
needed, placeholder, `??`, or `[?]` marker.  They also found zero root or
project path, ledger gate/queue, command-log name, build/review token,
agent/model identity, known private hash, or other private governance text.

## Mathematical and anti-claim fidelity

I compared the repaired source, extracted text, detailed renders, source and
publication locks, and the proof lineage.  The rendered main theorem retains
all critical conjuncts:

- characteristic zero, `r >= 4`, `g >= 2r+1`, `h=g-1`, `m=r-2`, the fixed
  word `F=T` after `S`, and `C=BA`;
- `M=2 11^T-I`, first-row replacement for `A`, last-row replacement for
  `B`, the explicit cone `x_i>=1` and `sigma<(h-1)/2`, both strict phase
  selectors, and actual recurrences `v_(n+1)=Au_n`, `u_(n+1)=Cu_n`;
- separate carried-coordinate gaps and leading-form survival in a polynomial
  domain, without a coefficient-positivity assumption;
- strict last-coordinate visibility only for `n>=1`, with the tied `n=0`
  case handled separately, followed by the exact degree and algebraic
  Perron-radius identities;
- the invariant direct sum `K^r=U+E`, exact `(r-3)`-dimensional semisimple
  unit sector, the fixed equal-middle convention, and the displayed matrix
  `Q_(m,h)`;
- the characteristic factor `(t-1)^(r-3) P_(m,h)(t)`, the exact cubic
  coefficients, `P_(m,h)(1)=-4m(m+1)(h+1)^2`, and exact algebraic and
  geometric unit multiplicity `r-3` with no quotient unit mode;
- the scalar recurrence with the displayed `T_0,S_0,D_0` and initial values
  `d_0=1`, `d_1=h(2m+3)`;
- the `g=2r` ordinary-seed/selected-face boundary, formal `r=3`
  consistency only, and the four arbitrary nonzero coefficients on the same
  fixed supports.

The rendered qualifications are equally intact.  The cone is sufficient,
not claimed maximal, necessary, unique, exact, or classificatory.  The cubic
is an annihilator, not uniformly minimal or irreducible.  No uniform
algebraic-degree-three claim is made for the Perron root.  The boundary is
not a global failure theorem and does not analyze all dynamics at or below
`g=2r`.  The formal low-mode substitution proves no `r=3` theorem.  The
result fixes the supports and phase word and makes no arbitrary-Hamiltonian,
positive-characteristic, topological, metric, arithmetic, entropy, or
hyperbolicity claim.

## Fresh reviewer visual audit and scratch cleanup

I created `/tmp/paper22-r2-review-render.W0WPDx` by a fresh `mktemp -d`
invocation.  Its canonical path equaled its literal path; it was a
non-symlink directory on device 149, inode 3759170818, mode `0700`, initially
empty.  I rendered every page at 120 dpi, composed seven chronological
two-by-two contact sheets, and rendered pages 1, 8, 13, 22, 24, and 26
separately at 200 dpi.  The contact-sheet identities, in order, were:

| Pages | SHA-256 | Bytes |
|---|---|---:|
| 01–04 | `22f0251e54c983e2a89385f6f27b698f7913e74de59252223d1517016dd06008` | 957,402 |
| 05–08 | `c840dc7e2386fdf3353c998cac3d4371412ca1bd999cdc39161648ee9eb65980` | 833,382 |
| 09–12 | `88fd4b184adfe413012303abb35840c4d161c1851b138625f429205d9d73ec38` | 686,216 |
| 13–16 | `84c12ba8be330ea094500124ba86fff3f86423e312b14421633429a6c929de6a` | 932,577 |
| 17–20 | `da9511100383d02a3df464cb6aaa2b232b305db029bc79f7aec734199965b6da` | 798,883 |
| 21–24 | `8442b172d708fc917b1db1dbfd8db8a0fe350c83ae04a69f4c48338fae9ca7be` | 783,132 |
| 25–26 | `c346008fe018cb8b130eb00fbcd6ea2d6b0b1fe1507187ecf95909504b7e9637` | 490,569 |

The detailed page hashes for pages 1, 8, 13, 22, 24, and 26 were,
respectively,
`7f89a208097621128c93f63a1d727bab266dcef34aa7258b45aed233edd8d190`,
`635cc38eed36eae8d633451bf68a8a7c5ebb13c147d606167d67dd6286a7ca2e`,
`65ab2be7498742c0952cd53796c11c99ed36bbaafcef6fe7ad95af2cbb50a9b3`,
`10edda68cb1bf495328c3f773c5f7dc1f86a0779368eab29bab112a2ae33985b`,
`2611606f467d3650850e12daf7ddc92ec5dce25e56befcd4a5769512399f6ad2`,
and `ffc2f3eae2af4f51de828caa00e51a4ac000bef16be5760cd3bb7dba6301eca2`.

All 26 pages are present, chronological, numbered, nonblank, sharp, and
readable.  There is zero corruption, clipping, crop loss, overlap, margin
overflow, table overflow, or unintended blank page.  Detailed page 1
confirms title, Anonymous, Abstract, and the start of Section 1.  Page 8
confirms complete Table 1 and the selector cone.  Page 13 confirms complete,
legible Table 2 despite its three logged underfull cells.  Page 22 confirms
complete Table 3 and the exact-unit-multiplicity theorem.  Page 24 confirms
the Section 8 heading and safely rendered `g=2r` boundary heading.  Page 26
confirms Limitations, Conclusion, and all six References in the required
order and boundaries.

The scratch held exactly 39 regular, link-count-one PNG files and no
subdirectory or symlink.  After inspection I reopened the directory with
`O_DIRECTORY|O_NOFOLLOW`, revalidated every child with no-follow `lstat`,
unlinked exactly those 39 reviewer-created files by directory descriptor,
verified the directory empty, and removed it.  The scratch path is now
absent.  No retained build or validation root was modified or cleaned.

## Final disposition and bounded effect

Immediately before this sole write I rehashed both parent ledgers, the exact
44-file project manifest, all 52 retained-root files, all three project/root
source copies, all paired command logs, all outputs, and the three equal
PDFs.  Every opening identity remained unchanged.  Creation of this review
alone changes the Paper 22 inventory from 44 to 45 regular files; the four
direct child directories and zero-symlink counts remain unchanged.  The
review's non-circular SHA-256, byte count, and LF count are to be computed
externally after persistence.

Every required R2 conjunct passes.  There is no scientific, source,
bibliographic, build, JSON, citation, mathematical, rendering, anonymity,
metadata, security, private-provenance, permission, required, or cosmetic
finding.  This review authorizes no source edit, rebuild, overwrite, release,
finalization, publication, submission, upload, transport, repository action,
messaging, identity disclosure, Paper 23 work, network access, or external
effect.  It supplies only the independent R2-PASS evidence required for a
separately governed Paper 22 finalization transition.

BUILD_R2_R1_PASS
