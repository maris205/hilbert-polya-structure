# Final QA — P124 round 2

Status: **ROUND2 GO_INTERNAL / EXTERNAL HOLD**.

QA date: 2026-08-30.

## Immutable core

Round 2 did not modify the manuscript, bibliography, either verifier, either
canonical transcript, or any pre-existing PDF.

| Artifact | SHA-256 |
|---|---|
| `main.tex` | `a34a431f1e048e3d43871b630dbfee63ac31097a7eff45c134455e80f415ac56` |
| `references.bib` | `74d639b81e6914f2da781682e02df99800f3186f95e9e364028037466dea9e89` |
| `code/verify_alg_cross_colon.py` | `950953523155868efec1491e69038b1d30c33249b1df2daa7881c74012242cbf` |
| `code/verify_alg_cross_colon_basins.py` | `51ca13655933b869ce8e4b12c868d550a107496c013136e2e5fa18ad9b481f22` |
| `code/ALG_CROSS_COLON_CANONICAL.txt` | `b924e05c5e9ac71a25fb668d5bc2033f6ab58c325c7c73642a4dd0b096d67deb` |
| `code/ALG_CROSS_COLON_BASINS_CANONICAL.txt` | `bdfd3e041b9f641101436c40918adbba59fd14b1f1381d77fa943ce00c0c76ff` |

## Exact-control QA

| Check | Result |
|---|---|
| fresh core verifier | PASS, 1,469,669 assertions |
| core stdout versus canonical | byte-identical, `cmp` exit 0 |
| fresh basin verifier | PASS, 265,987 assertions |
| basin stdout versus canonical | byte-identical, `cmp` exit 0 |
| combined assertion accounting | **1,735,656** |
| network, randomness, floating point | none in either verifier |

## Isolated build QA

Only `main.tex` and `references.bib` were copied to a fresh temporary
directory.  The following four stages all exited 0:

1. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`;
2. `bibtex main`;
3. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`;
4. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`.

The final log has zero effective LaTeX/package/class warnings, zero undefined
citations or references, zero overfull/underfull boxes, zero rerun requests,
and zero errors.  BibTeX resolves 9/9 entries without warning or error.

## PDF archive QA

| Artifact | Pages | Bytes | SHA-256 | Byte relation |
|---|---:|---:|---|---|
| `main_round0_original.pdf` | 5 | 293,617 | `3dd3316a0abbc504a65c6214bc52d4a439a4e16f8290ca655b7fcece2b501f81` | frozen original |
| `main_round1.pdf` | 5 | 293,617 | `3dd3316a0abbc504a65c6214bc52d4a439a4e16f8290ca655b7fcece2b501f81` | identical to round 0 |
| `main.pdf` | 5 | 293,617 | `3dd3316a0abbc504a65c6214bc52d4a439a4e16f8290ca655b7fcece2b501f81` | identical to round 0 |
| `main_round2.pdf` | 5 | 293,617 | `3dd3316a0abbc504a65c6214bc52d4a439a4e16f8290ca655b7fcece2b501f81` | direct copy of current |

The isolated-build PDF has the same hash, page count, and byte count.

## Visual, font, and anonymity QA

All five pages were rendered and inspected:

| Page | Content | Result |
|---:|---|---|
| 1 | anonymous title/abstract, scope, operator, start of coordinates | clean |
| 2 | local rule, diagonal bands, path lemma, checker definition | clean |
| 3 | recurrent/depth theorem and complete basin theorem | clean |
| 4 | four-state transfer, reflection proof, complexity, example | clean |
| 5 | basin table, exact controls, conclusion, nine references | clean |

There is no clipping, overlap, malformed formula, broken glyph, unreadable
table entry, blank page, or unresolved marker.  The page-4 discussion and
page-5 Table 1 float remain unambiguous.

- format: A4 portrait, 5 pages, PDF 1.5, unencrypted;
- fonts: 23/23 rows embedded, subsetted, and Unicode-mapped;
- visible author: Anonymous;
- metadata Author, Title, Subject, and Keywords: blank;
- metadata stream and custom metadata: absent;
- filesystem paths, usernames, email, affiliation, ORCID, dates, TODO/DRAFT
  markers: absent;
- embedded files, forms, JavaScript, signatures, and raster images: absent.

## Review and ownership QA

- Review A: `0 CRITICAL / 0 MAJOR / 2 MINOR`; both support findings closed.
- Review B: `0 CRITICAL / 0 MAJOR / 0 MINOR`; `GO_INTERNAL`.
- corrected anchors: Theorem 3.2 and Theorem 5.1.
- P107/P104 firewall: explicit and independently confirmed.
- generic-method owner subtraction: retained.
- bounded direct-owner non-hit: not treated as novelty evidence.
- external novelty, priority, posting, submission, and release: **HOLD**.

## Manifest QA

`SHA256SUMS` covers the frozen sources, verifier/canonical pairs, support
records, review records, and all four PDFs.  The manifest intentionally does
not hash itself.  From this directory:

```bash
sha256sum -c SHA256SUMS
```

must report `OK` for every listed artifact.

## Final result

**All authorized round-2 mechanical QA checks pass.  GO_INTERNAL; EXTERNAL
HOLD remains in force.**
