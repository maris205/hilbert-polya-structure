# Build record — P126 round 2 final freeze

## Manuscript

- Date: 2026-08-30 UTC.
- Pipeline: `pdflatex -> bibtex -> pdflatex -> pdflatex`.
- Result: **PASS**.
- Final log: 0 errors, 0 undefined citations/references, 0 warning hits,
  0 overfull/underfull boxes.
- Bibliography: 9/9 cited owner/interface sources.
- PDF: 4 A4 pages, 319,631 bytes.
- PDF SHA-256:
  `e5d7ab3986a635a490804a8a81d7b3873b5c8403456fccf138af30315751ed3e`.
- `main_round1.pdf`, support-only `main_round2.pdf`, and current
  `main.pdf` are byte-identical.
- Immutable `main_round0_original.pdf` is preserved at
  `d48125fc509fc972b2b705226c33d7915a529523917fd786a5eda2190106ca1e`.
- Fonts: all listed fonts embedded and carry Unicode maps.
- Metadata: author/title/subject fields blank; creation/modification dates
  omitted; no JavaScript or encryption.
- Visual inspection: all four pages inspected; no clipping, overlap,
  malformed formula, bad link, missing glyph, or orphaned heading found.

## Exact control

- Verifier result: PASS, **8,756,710 assertions**.
- Fresh stdout versus canonical transcript: byte-identical.
- `code/verify.py` SHA-256:
  `5f58da9c3418502d64cd2fc7e3918c9a8bb464c456bc936539bb2afc7ee83ef0`.
- Canonical transcript SHA-256:
  `978191ccbc9a120ca34a298ab79f828175a069b7574388823885fb5712bd2090`.

## Source freeze

- `main.tex` SHA-256:
  `c93d504af40fbf6e162db4cf3b996457bb7d892ea1ab3e2c8ef89dd7273fd270`.
- `references.bib` SHA-256:
  `4272430bd26581c7c6aead83f7ae2cacab37f5177d551e293447a0e071105292`.
- Status: anonymous internal round-2; Review-A re-entry and independent
  Review B both **GO_INTERNAL**; novelty, priority, and external release
  **HOLD**.

## Review-A rewrite boundary

The theorem contract and exact verifier are unchanged.  Round 1 adds the
primary-owner subtraction and mandatory internal firewall, corrects
length/weight terminology, spells out empty/identity boundaries, expands the
terminal-marker induction, and restores the proof-spike provenance hashes.
All four pages were re-inspected after the rewrite; all listed fonts remain
embedded, subsetted, and Unicode-mapped, and anonymous metadata remains clean.

Review-A re-entry and Review B independently reproduced the same four-page
PDF, reran the exact controls, and closed every owner, scope, boundary, and
provenance item.  Round two changes support status only; the round-one
manuscript bytes remain frozen.
