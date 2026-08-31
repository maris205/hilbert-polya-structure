# Final QA — P133 totient-complement Pratt dynamics

**Date:** 2026-09-01 UTC.  **Result:** **PASS**.  **Internal status:**
**GO_INTERNAL**.  **External status:** **HOLD_EXTERNAL**.

## 1. Final payload

- `main.tex` SHA-256:
  `3f62efbd5a23a5a0a811e92f4f975ba643cd4262b958c6c6ab0804920f602835`.
- `main.pdf`, `main_round0_original.pdf`, `main_round1.pdf`, and
  `main_round2.pdf` are byte-identical: 346,509 bytes, three A4 pages,
  SHA-256
  `bbb869d485230bc0165bbe49ff43929de61700c1e0acc960a541b64b23651d7b`.
- Exact paper-local assertions: **4,774**.

## 2. Fresh verifier replay

The terminal run in `/tmp/p132-136-terminal-verifiers.TCvHXQ` reproduced the
canonical stdout byte for byte (`cmp=0`).  Both copies are 730 bytes with
SHA-256
`1c90aea14a3c45d084ec9cd6d86e951d3508494d94fa04afa6bd6ec12692b99d`;
the terminal line is `STATUS=PASS`.  The verifier source SHA-256 is
`841ed6f77091e0d0e6721c24dc334891f8bc3b54701717153da49ecbb391262a`.
The four exact boxes are falsification controls, not an all-prime-set proof or
novelty certificate.

## 3. Isolated build

Only `main.tex` and `references.bib` were copied to
`/tmp/p132-136-final-builds.RetOwU/133-totient-complement-pratt-dynamics`.
The four-stage LaTeX/BibTeX sequence exited zero and reproduced the frozen PDF
byte for byte.  Settled logs contain no error, warning, undefined citation or
reference, multiply defined label, bad box, or rerun request.

## 4. PDF, bibliography, and anonymity

The PDF is version 1.5, A4, rotation zero, unencrypted, form-free,
JavaScript-free, and has no metadata stream, raster image, or attachment.
Identifying metadata fields are blank and the visible author is `Anonymous`.
All **28/28** font rows are embedded, subsetted, and Unicode-mapped.  All
**3/3** bibliography entries are cited and resolved.  Extracted text is
searchable on every page and contains no unresolved marker, placeholder,
TODO/FIXME, tool/path/email string, or identity leak.

## 5. Three-page visual audit

- Page 1: title, abstract, support graph, main theorem, and all-target formula
  are clean.
- Page 2: support conjugacy, phase decoder, erasure identity, and entry proof
  are complete and aligned.
- Page 3: recurrent census, inclusion--exclusion fibre proof, control table,
  owner boundary, external hold, and all references are legible.

## 6. Review closure and decision

Review A's sole locator minor is closed.  Independent Review B reconstructed
the support law, source phases, simultaneous `h+1` entrance, census, and every
target fibre and returned critical 0, major 0, minor 0.

**PASS / GO_INTERNAL.**  The anonymous internal theorem package is coherent
and reproducible.  **HOLD_EXTERNAL.**  Novelty, priority, authorship, posting,
submission, specialist contact, and every release action remain unauthorized.
