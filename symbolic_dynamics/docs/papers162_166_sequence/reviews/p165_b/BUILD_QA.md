# P165 Review B — replay, source-only build, and PDF QA

**Date:** 2026-09-03  
**Reviewed PDF:** `papers/165-low-weight-support-shortening/main_round1.pdf`  
**Lifecycle:** `HOLD_EXTERNAL`

## 1. Frozen Round-1 identity

```text
main.pdf                    f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a
main_round0_original.pdf    f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a
main_round1.pdf             f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a
bytes                       288,837
byte comparison             all three equal
```

Review A returned `0C/0M/0m` and requested no source change.  Therefore the
Round-1 no-op freeze is coherent: the source/PDF is supposed to be identical
to Round 0, and it is.  `PINNED_INPUTS.sha256` records the source,
bibliography, frozen PDFs, author verifier/canonical, Review-A report, and
principal author evidence files before this review wrote any output.

## 2. Fresh executable replays

### Author verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 papers/165-low-weight-support-shortening/code/verify.py
verifier SHA-256:  391c47dd3be9931c4b525025722ade224bd3b583c75d5da8564f6b75f347bcaf
canonical SHA-256: 0fc0aac73b62b039fb9e82918a141927b33fb2aecb8b1f28ae3940c1481590bd
fresh replay 1:    0fc0aac73b62b039fb9e82918a141927b33fb2aecb8b1f28ae3940c1481590bd
fresh replay 2:    0fc0aac73b62b039fb9e82918a141927b33fb2aecb8b1f28ae3940c1481590bd
result:             2/2 byte-identical to canonical; PASS
author assertions:  605,733
```

### Review-A independent verifier

```text
verifier SHA-256:  f6399e25007c147f78f83799f825c14fb19419b1ad4a0467ea17618ea592e27f
canonical SHA-256: 66de01f2399047e6a32d9b22d508be9eab56fd14b62b3e766991d0b28d5b25e7
fresh replay 1:    66de01f2399047e6a32d9b22d508be9eab56fd14b62b3e766991d0b28d5b25e7
fresh replay 2:    66de01f2399047e6a32d9b22d508be9eab56fd14b62b3e766991d0b28d5b25e7
result:             2/2 byte-identical to canonical; PASS
Review-A assertions: 1,574,098
```

### Review-B independent verifier

The Review-B implementation imports neither author nor Review-A code.  It
enumerates unique RREF subspaces and constructs the literal map from all
codewords.  Its true nonprime field is
`GF(4)=GF(2)[a]/(a^2+a+1)`, with the field laws and `a^2=a+1`, `a^3=1`
checked directly.

```text
verifier SHA-256:  987e913be21a91d7f612bf158f14d84c0b597950e215a870c4d0405280685b54
canonical SHA-256: 3a593364f3a30a18bf76fe1611dad2a8330a57772cd466afd8d672cda238da04
fresh replay 1:    3a593364f3a30a18bf76fe1611dad2a8330a57772cd466afd8d672cda238da04
fresh replay 2:    3a593364f3a30a18bf76fe1611dad2a8330a57772cd466afd8d672cda238da04
result:             2/2 byte-identical to canonical; PASS
assertions:         1,220,460
code states:        37,193
target-time interfaces checked: 215,030
transition digest:  26f9a5289fff65e701ecfc0c18cb1d91271b652ca8f1067263497db1374ae8b7
```

Complete boxes are `F2, 0<=n<=7`; `F3, 0<=n<=5`; `F4, 0<=n<=4`; and
`F5, 0<=n<=4`.  Every box checks Gaussian totals, literal transitions,
strict descent, doubling, depths and sharp height, all tested times and
targets, the image iff, both lower bounds, the actual-versus-constructed
simultaneous-extremizer sets, their closed count, exact-depth zero-target
minimizers, time zero, the empty ambient space, full-support holes,
post-cap times, and a strict-versus-weak cutoff sentinel.

## 3. Two source-only cold builds

Two new directories received only byte copies of `main.tex` and
`references.bib`; no `.aux`, `.bbl`, log, PDF, or repository build artifact
was imported.  Each ran

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

with `SOURCE_DATE_EPOCH=0` and `TZ=UTC`.

```text
toolchain: pdfTeX 3.141592653-2.6-1.40.22; BibTeX 0.99d
build 1 PDF: f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a
build 2 PDF: f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a
canonical Round-1 PDF: same
build 1/2 PDF byte match: YES
each PDF bytes: 288,837
build 1/2 settled main.bbl SHA-256:
  d892ae169e3f71ea608f0c1312ec1b6b79e84be0295816fafd4d507dd4f88d59
build 1/2 settled main.log SHA-256:
  df87a2e1c3d32737b04813f950874453632ebb9cfbf6cef3d40c80653bdd2b6e
```

The two settled logs and `.bbl` files are pairwise byte-identical.  A
diagnostic scan found zero LaTeX/class/package warnings, fatal errors,
undefined citations/references/control sequences, rerun requests,
multiply-defined labels, duplicate destinations, overfull boxes, or
underfull boxes.  BibTeX used all three entries and emitted zero warnings.
Package filenames containing the strings `warning` or `rerun` were not
miscounted as diagnostics.

## 4. PDF structure, fonts, metadata, and anonymity

```text
pages:                    4/4
page size:                595.276 x 841.89 pt (A4)
page rotation:            0
PDF version:              1.5
encrypted:                no
forms:                    none
JavaScript:               no
custom metadata:          no
metadata stream:          no
user properties:          no
suspects flag:            no
embedded attachments:     0
digital signatures:       0
font rows:                23
embedded/subset/Unicode:  23/23, 23/23, 23/23
references rendered:      3/3
```

Title, subject, keywords, author, creator, and producer metadata fields are
empty.  Extracted text contains the visible byline/running head `ANONYMOUS`
and the intended visible `HOLD_EXTERNAL` lifecycle marker.  It contains no
email address, ORCID, affiliation, institution, department, acknowledgement,
funding identifier, local path, TODO/FIXME token, or nonanonymous byline.

## 5. Page-by-page 150-dpi visual inspection

- **Page 1:** title/byline, abstract, map definition, owner subtraction, and
  the first theorem portion are sharp and inside the page box.  No collision,
  clipping, missing glyph, or formula overflow.
- **Page 2:** the extremal formula, dyadic clock proof, and image proof render
  cleanly.  Equation labels and hyperlinks are legible; no bad break or
  margin intrusion.
- **Page 3:** equality proof, count, boundary audit, lifecycle statement, and
  first reference are complete and legible.  No orphaned heading or clipped
  text.
- **Page 4:** references 2 and 3 render correctly.  The remaining white area
  is the natural end of a four-page note, not missing content.

All four pages passed visual inspection.  Successful independent raster
rendering also provided parser pressure on the PDF in addition to
`pdfinfo`, `pdffonts`, `pdftotext`, `pdfimages`, `pdfsig`, and `pdfdetach`.

## 6. QA result

All replay, build, metadata, font, reference, anonymity, lifecycle, and
visual checks pass.  No artifact repair is requested.
