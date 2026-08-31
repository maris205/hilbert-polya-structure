# Final QA — P136 random sunflower transversal laws

**Date:** 2026-09-01 UTC.  **Result:** **PASS**.  **Internal status:**
**GO_INTERNAL**.  **External status:** **HOLD_EXTERNAL**.

## 1. Final payload

- `main.tex` SHA-256:
  `39724907724bf2f0bcc2e03b0dd5fb74aefeff8fb9f9d9c4bdea1edf00131170`.
- `main.pdf`, `main_round1.pdf`, and `main_round2.pdf`: 265,938 bytes,
  four A4 pages, SHA-256
  `3cf06ca9b8b5cd829e20e99d6eafe32d45150b9eae2b60c61a1082e391f2be04`.
- `main_round0_original.pdf` remains immutable at SHA-256
  `0668f9b434aad2747a3d887d0a8fa6f6e36885a41b9f27f6182ee2d6a15192ef`.
- Exact paper-local assertions: **174,170** over 5,812 parameter inputs.

## 2. Fresh verifier replay

The terminal run in `/tmp/p132-136-terminal-verifiers.TCvHXQ` reproduced the
428-byte canonical stdout byte for byte (`cmp=0`), with SHA-256
`5553c8c797bc4b577a6252959471f1e556e850cafcdf96d8a74b39353491271c`
and terminal line `status=PASS`.  The verifier source SHA-256 is
`0285c2c7f82540d421888f37bad0302a3a3fd106e916c1ad590018e927b51913`.
The finite grids are exact falsification controls, not proofs of arbitrary
positive-rate claims or novelty.

## 3. Isolated stable build

Only `main.tex` and `references.bib` were copied to
`/tmp/p132-136-final-builds.RetOwU/136-random-sunflower-transversal-laws`.
The stable sequence `pdflatex -> bibtex -> pdflatex -> pdflatex -> pdflatex`
exited zero and reproduced the final PDF byte for byte.  The final log has no
error, warning, undefined citation/reference, bad box, label-change warning,
or rerun request; BibTeX has no warning.

## 4. PDF, bibliography, and anonymity

The PDF is version 1.5, A4, rotation zero, unencrypted, form-free,
JavaScript-free, and has no metadata stream, image, or attachment.  Identifying
metadata is blank and the visible author is `Anonymous`.  All **18/18** fonts
are embedded, subsetted, and Unicode-mapped.  All **6/6** bibliography entries
are cited and resolved.  Every page has searchable text; marker, placeholder,
tool/path/email, and identity-leak scans are clean.

## 5. Four-page visual audit

- Page 1: process ownership, endpoint definition, and rate notation are clean.
- Page 2: weighted endpoint integral and actual-vertex sigma-field refinement
  are aligned and legible.
- Page 3: `T` is visibly defined as discrete selection count; top atom, PGF,
  moments, and forest factorization are complete.
- Page 4: continuous elapsed completion is explicitly a maximum rather than a
  convolution; exact controls, limitations, conclusion, and six references
  are complete.

## 6. Review closure and decision

Review A's count/time major and both finite-grid/conditioning minors are
closed.  Review B's clean-build and stale-prose minors are closed by the
five-stage protocol and strict reader-facing terminology audit.  Final
severity is critical 0, major 0, minor 0.

**PASS / GO_INTERNAL.**  The anonymous internal theorem package is coherent
and reproducible.  **HOLD_EXTERNAL.**  The owned covering process and bounded
owner search authorize no novelty, priority, authorship, posting, submission,
specialist contact, or release action.
