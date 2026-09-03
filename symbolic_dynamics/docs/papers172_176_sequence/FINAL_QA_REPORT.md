# Final QA report — P172–P176

**Audit record:** 2026-09-03.  **Scope:** exactly the five final Round-2
packages, with prior round PDFs preserved.  **Decision:**
`PASS_INTERNAL / HOLD_EXTERNAL`.

## Exact paper-local replay

Each final paper-local control was run afresh with Python bytecode disabled.
Every stdout stream matched its retained canonical file byte for byte.

| paper | control | assertions | canonical transcript SHA-256 | replay |
|---:|---|---:|---|---|
| P172 | `verify_p172.py` | 48,575 | `a279b8841d9d3d05055520fe4a49998c078c16d9156d1a5ed1354a3d81cd0756` | exact match / PASS |
| P173 | `verify_p173.py` | 13,307 | `b32f20b843b22d719633620971f12cdc67a1e3ca02003aff41ea3b15261421d0` | exact match / PASS |
| P174 | `verify_p174.py` | 131,018,555 | `1faac49f7cb9cdfb7be13caf1a533f36a07851cdff1a9a955b85a3ec593e0646` | exact match / PASS |
| P175 | `verify_p175.py` | 2,111,465 | `f9169bb2d6ccfb304dee28409c3ed07e86ba597cc1862524bcc7f29d5a34eb25` | exact match / PASS |
| P176 | `code/verify_p176.py` | 2,828,503 | `3d0947a4df32f8e583e28d1964a52523602d61c64dde7b259bfdd15e71e4003b` | exact match / PASS; explicitly scout-derived |

Total: **136,020,405 exact paper-local assertions** and five of five
canonical transcript matches.  Reviewer-owned lanes are reported separately.

## Ten deterministic source-only builds

Two fresh directories per paper were initialized with only `main.tex` and
`references.bib`.  Each completed `pdflatex / bibtex / pdflatex / pdflatex`
with halt-on-error.  Every cold pair matched internally and every output
matched its live `main.pdf` byte for byte.

| paper | pages | bytes | final PDF SHA-256 | font rows | isolated builds |
|---:|---:|---:|---|---:|---|
| P172 | 4 | 274,791 | `91e8cc76f007eafba48a343aae116eeda03daa8bf3e1bcdbe50d2fc2e2013c83` | 22 | 2/2 exact |
| P173 | 4 | 333,340 | `01235b8279d922b0d120f869f32ef8be1ee6aea105dafbc5ea25155be1ef039c` | 24 | 2/2 exact |
| P174 | 4 | 321,776 | `b428c24be406d8c2cef9c1d6fc5a2630495f2eed54473ed1dec7b1120444ff7f` | 25 | 2/2 exact |
| P175 | 4 | 328,780 | `321d59b8b66cc2aef22296f214ee0d0072652c86d53293714599b0e07ee4b703` | 27 | 2/2 exact |
| P176 | 4 | 397,525 | `c13ca3f5e3673bb5dd9c01bdf7c8913f78425cdbfeb2a52e2d9b096a34122db4` | 31 | 2/2 exact |

Total: **10/10 source-only builds**, **20 A4 pages**, **1,656,212 bytes**,
and **129/129 font rows** embedded, subsetted, and Unicode mapped.  Settled
LaTeX/BibTeX logs contain no genuine warning, error, undefined citation or
reference, rerun request, or bad box.

## Preserved PDF rounds

| paper | Round 0 SHA-256 | Round 1 SHA-256 | Round 2/current SHA-256 |
|---:|---|---|---|
| P172 | `ac16b12438b1c2db313cc55af630887112ce53833cb7afb76deb656329164ecb` | `ef34c142ea0350d86501d04cc829b8ba8a5e87ea21970b6f180e4bcd7276e62b` | `91e8cc76f007eafba48a343aae116eeda03daa8bf3e1bcdbe50d2fc2e2013c83` |
| P173 | `d876f022bdc1e04ec57b0f9438db78b1f84abb1691c61dbd78d53083df48d359` | `1a66075c7d64ae943cbbd42503b81964ea7fabe85e2ee7515001a052aa5cce22` | `01235b8279d922b0d120f869f32ef8be1ee6aea105dafbc5ea25155be1ef039c` |
| P174 | `c1865f487b633477b41ffda5a6a03c0974516c3cea0f30160077e93c3157ec58` | `c1865f487b633477b41ffda5a6a03c0974516c3cea0f30160077e93c3157ec58` | `b428c24be406d8c2cef9c1d6fc5a2630495f2eed54473ed1dec7b1120444ff7f` |
| P175 | `32f296a1519fd598f0ef4c88bdbd0d655ff930b94e97eec42bd6f2b9ba1d1eba` | `32f296a1519fd598f0ef4c88bdbd0d655ff930b94e97eec42bd6f2b9ba1d1eba` | `321d59b8b66cc2aef22296f214ee0d0072652c86d53293714599b0e07ee4b703` |
| P176 | `5a8977524f5f7f5f654442bb3ac98cf74872de297277e9ffb0ff5c23878e69ba` | `5a8977524f5f7f5f654442bb3ac98cf74872de297277e9ffb0ff5c23878e69ba` | `c13ca3f5e3673bb5dd9c01bdf7c8913f78425cdbfeb2a52e2d9b096a34122db4` |

For all five papers, `main.pdf` and `main_round2.pdf` are byte-identical.
Earlier PDFs remain immutable repair receipts.

## PDF, visual, anonymity, and lifecycle QA

All 20 final pages were rasterized and inspected.  No clipping, overlap,
missing glyph, malformed display, illegible table/reference, margin
excursion, orphaned heading, or page-boundary defect was found.  Batch checks
also confirmed:

- A4 media boxes of `595.276 x 841.89 pt` for all five PDFs;
- blank title, author, subject, keyword, creator, and producer metadata;
- no encryption, interactive form, or JavaScript;
- exactly one anonymous visible byline and no identifying author material;
- no email, affiliation, ORCID, personal acknowledgement, username, or
  workspace path;
- at least one visibly extractable `HOLD_EXTERNAL` token in every PDF; and
- complete text extraction with no unresolved citation/reference marker.

## Review closure

| review lane | raw Critical | raw Major | raw Minor | assertions | closure |
|---|---:|---:|---:|---:|---|
| Hostile Review A | 0 | 2 | 5 | 15,037,657 | all findings repaired and delta-accepted |
| Hostile Review B | 0 | 6 | 9 | 37,087,856 | all findings repaired and delta-accepted |

No paper has an unresolved review finding.  The reviewer lanes total
**52,125,513 independent exact assertions** and remain separate from the
paper-local count.

## Integrity and manifest closure

The five final paper-local `SHA256SUMS` files contain respectively **46, 53,
43, 42, and 46** non-self entries and pass **230/230**.  Nineteen supporting
scouting/reviewer manifests cover **112** declared entries and pass
**112/112**.  The batch `CANONICAL_PDF_MANIFEST.sha256` covers exactly
P172–P176 and passes **5/5**.

No historical `PINNED_INPUTS.sha256` exists in this batch.  The explicit
Round-0/1/2 PDFs and current manifests preserve the relevant provenance.

## Release boundary

Final QA establishes internal theorem-package and artifact integrity only.
It does not establish novelty, priority, ownership completeness, freedom to
operate, or external readiness.  No upload, posting, circulation, contact,
or submission is authorized.  All five manuscripts remain anonymous internal
accepts under `HOLD_EXTERNAL`.
