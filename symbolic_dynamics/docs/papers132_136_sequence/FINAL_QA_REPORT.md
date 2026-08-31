# Final QA report — P132–P136

**Checkpoint:** 2026-09-01 UTC.  
**Result:** **5/5 PASS INTERNAL; FINAL FREEZE; EXTERNAL HOLD**.

| paper | pages | bytes | exact control | independent gate | fonts | visual pages |
|---:|---:|---:|---:|---|---:|---:|
| P132 | 3 | 326,101 | 524,452 | `GO_INTERNAL` | 25/25 | 3/3 |
| P133 | 3 | 346,509 | 4,774 | `GO_INTERNAL` | 28/28 | 3/3 |
| P134 | 5 | 323,103 | 1,694,506 | `GO_INTERNAL` | 24/24 | 5/5 |
| P135 | 5 | 395,335 | 7,130,840 | `GO_INTERNAL` | 31/31 | 5/5 |
| P136 | 4 | 265,938 | 174,170 | `GO_INTERNAL` | 18/18 | 4/4 |
| **total** | **20** | **1,656,986** | **9,528,742** | **5/5** | **126/126** | **20/20** |

## Control and build replay

After every Review-B repair, all five paper-local verifiers ran in fresh
Python processes with bytecode disabled.  Each raw stdout matched its frozen
transcript byte for byte.  The canonical transcript digests are:

| paper | transcript SHA-256 |
|---:|---|
| P132 | `f52d769cd0831772458e700db189722bf745b8e74c4aca2c3539dcfea8a0f442` |
| P133 | `1c90aea14a3c45d084ec9cd6d86e951d3508494d94fa04afa6bd6ec12692b99d` |
| P134 | `cce8c343276f5a299cb2c723e8b1957020749f74ff36a9aeb8462253c4b34d3e` |
| P135 | `be50b73c6c3c17c6378d141bc6c594388512241b8acb9b6e7b877b470070ba90` |
| P136 | `5553c8c797bc4b577a6252959471f1e556e850cafcdf96d8a74b39353491271c` |

The terminal verifier directory is
`/tmp/p132-136-terminal-verifiers.TCvHXQ`.  These heterogeneous counts are
finite counterexample pressure and must not be compared as paper-quality,
proof-strength, novelty, or owner-clearance scores.

All five manuscripts were also built from only `main.tex` and
`references.bib` under `/tmp/p132-136-final-builds.RetOwU`.  P132--P135 use
`pdflatex -> bibtex -> pdflatex -> pdflatex`; P136 uses one additional final
`pdflatex` pass to settle clean-directory page labels.  Every command exited
zero, every final log is warning/error/undefined-reference/bad-box/rerun free,
and every isolated PDF reproduced `main.pdf` and `main_round2.pdf` byte for
byte.

## Bibliography, PDF, text, and visual gates

The bibliography closures are 5/5, 3/3, 4/4, 4/4, and 6/6: **22/22** entries
are cited and resolved.  All PDFs are A4, rotation zero, version 1.5,
unencrypted, form-free, JavaScript-free, and have empty Title, Author, Subject,
and Keywords metadata fields.  No PDF contains a raster image, metadata
stream, or attached file.  Every visible byline is `Anonymous`.

All **126/126** font rows are embedded, subsetted, and Unicode-mapped.  Fresh
layout-preserving text extraction contains **85,637 bytes** in **1,133 lines**;
all 20 pages have nonempty searchable text.  Scans found no unresolved
reference, placeholder, TODO/FIXME, verification marker, local filesystem
path, tool/debug name, email address, or personal-identity leak.  Each
manuscript visibly retains its external-hold boundary.

All **20/20** final pages were rasterized at 160 dpi and inspected one by one.
Titles, anonymous bylines, abstracts, theorem statements, proofs, equations,
tables, owner boundaries, limitations, conclusions, and references are
legible.  No page has clipping, overlap, missing glyphs, malformed display,
unintended blank content, or rotation.  P134 and P135 have deliberately sparse
last reference pages; both contain complete legible content and are not blank.

## Integrity gate

Each paper-local `SHA256SUMS` covers 19 frozen evidence artifacts and passes
entry by entry.  The manifests themselves have digests:

| paper | entries | manifest SHA-256 |
|---:|---:|---|
| P132 | 19 | `7762d66e40bc7597e336e9b8172626246abc0b233ef8bfa0812c1bc2ccd4877c` |
| P133 | 19 | `58d94070683f340817e9722418a27fbfeca48f0ce5c750a0455b7d1fba07b9df` |
| P134 | 19 | `419438a9f906ee94ca1469ccffc505626a6b8a7ddd62779dd64fecc6bde7b7cb` |
| P135 | 19 | `20390cef348f1267e0a91ef2b517659b5c022c104dfba76cd9c4f04a96bc17ec` |
| P136 | 19 | `16c19647f72ca0b0b3bdf7e72e02bf25a36f096cf317893b4342079418c25a8f` |

The five canonical PDF digests are frozen in
`CANONICAL_PDF_MANIFEST.sha256`; it passes 5/5 and has SHA-256
`4b3e138953d661d1282b52d8253940c8ab9867cb199f54ea00bcfe929e81f6c1`.

This report certifies internal theorem-package consistency, reproducibility,
and artifact mechanics only.  External release, novelty, priority, authorship,
posting, submission, specialist contact, and every other external action
remain **HOLD**.
