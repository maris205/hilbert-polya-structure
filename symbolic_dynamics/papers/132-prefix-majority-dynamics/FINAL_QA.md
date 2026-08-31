# Final QA — P132 synchronous prefix-majority dynamics

**Date:** 2026-09-01 UTC.  **Result:** **PASS**.  **Internal status:**
**GO_INTERNAL**.  **External status:** **HOLD_EXTERNAL**.

## 1. Final payload

- `main.tex` SHA-256:
  `a26bee914dd2909c825a7c1d3e2a012c09b2def816b14db85ab27c40b60bddaf`.
- `main.pdf` and `main_round2.pdf`: 326,101 bytes, three A4 pages, SHA-256
  `dcfd7eddb0cb85a197f0ae875af97fd353f50070317ca4ec6f8de0ad5a74527e`.
- `main_round1.pdf` is byte-identical to the final PDF.
- `main_round0_original.pdf` remains distinct and immutable at SHA-256
  `f6329905059f20811380dcfe1163d9cd908a592e428a358ec1f9461d55140679`.
- Exact paper-local assertions: **524,452**.

## 2. Fresh verifier replay

The terminal run in `/tmp/p132-136-terminal-verifiers.TCvHXQ` reproduced
`code/verification_output.txt` byte for byte (`cmp=0`).  Fresh and canonical
stdout are 1,160 bytes with SHA-256
`f52d769cd0831772458e700db189722bf745b8e74c4aca2c3539dcfea8a0f442`;
the terminal line is `STATUS=PASS`.  The verifier source SHA-256 is
`50ff5f13d47c01b679a9158f79ce5aa20333f43c374d133c31ff46712882604d`.
The finite run is counterexample pressure, not an all-length proof or novelty
certificate.

## 3. Isolated build

Only `main.tex` and `references.bib` were copied to
`/tmp/p132-136-final-builds.RetOwU/132-prefix-majority-dynamics`.  The sequence
`pdflatex -> bibtex -> pdflatex -> pdflatex` exited zero and reproduced both
final PDF copies byte for byte.  The settled LaTeX/BibTeX logs contain no
error, warning, undefined citation/reference, multiply defined label,
overfull/underfull box, or rerun request.

## 4. PDF, bibliography, and anonymity

The PDF is version 1.5, A4, rotation zero, unencrypted, form-free,
JavaScript-free, and has no metadata stream, embedded raster image, or file
attachment.  Title, Author, Subject, and Keywords metadata are blank; the
visible author is `Anonymous`.  All **25/25** font rows are embedded,
subsetted, and Unicode-mapped.  All **5/5** bibliography entries are cited and
resolved.  Extracted text is searchable, every page is nonempty, and scans
found no unresolved-reference, placeholder, TODO/FIXME, verification, tool,
path, email, or personal-identity leak.

## 5. Three-page visual audit

- Page 1: title, anonymous byline, abstract, literal map, owner subtraction,
  fixed-language theorem, and corrected exponents are clean.
- Page 2: amplifier, sharp clock, constant fibres, and excursion product are
  aligned and legible; no literal `qquad` remains.
- Page 3: image/extremal theorem, exact-control boundary, external hold, and
  all five references are complete without clipping or overlap.

## 6. Review closure and decision

All four Review-A minors are closed.  Review B independently reconstructed
the theorem package and its sole provenance minor is closed by the corrected
Round-0 digest.  Final review severity is critical 0, major 0, minor 0.

**PASS / GO_INTERNAL.**  The anonymous internal theorem package is coherent
and reproducible.  **HOLD_EXTERNAL.**  Novelty, priority, authorship, posting,
submission, specialist contact, and every release action require a separate
authorized decision.
