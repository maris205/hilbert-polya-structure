# Final QA — P135 derived-centralizer orbit partitions

**Date:** 2026-09-01 UTC.  **Result:** **PASS**.  **Internal status:**
**GO_INTERNAL**.  **External status:** **HOLD_EXTERNAL**.

## 1. Final payload

- `main.tex` SHA-256:
  `cd8ea8a0d077b9619adf8b8d7e172757a5262d2f24a9060c98c92f0ad87ae149`.
- `main.pdf`, `main_round1.pdf`, and `main_round2.pdf`: 395,335 bytes,
  five A4 pages, SHA-256
  `dbf3a7ff19d1ddd2bcde59b35287835ffa8dec3b4244c53e65e87fc14a2b1b94`.
- `main_round0_original.pdf` remains immutable at SHA-256
  `7cd8a811a9d879e303c3d7a0b1bd6631aa24d9fc64704df62b4a369ce327505b`.
- Exact paper-local assertions: **7,130,840**.

## 2. Fresh verifier replay

The terminal run in `/tmp/p132-136-terminal-verifiers.TCvHXQ` reproduced the
463-byte canonical stdout byte for byte (`cmp=0`), with SHA-256
`be50b73c6c3c17c6378d141bc6c594388512241b8acb9b6e7b877b470070ba90`
and terminal line `STATUS=PASS`.  The verifier source SHA-256 is
`26b87846c87dd671f709f90e9945f5724b3f6deac959f2619a73078721f0313a`.
Its bounded partition, tagged-state, and literal-wreath checks are falsifiers,
not an all-weight proof or owner clearance.

## 3. Isolated build

Only `main.tex` and `references.bib` were copied to
`/tmp/p132-136-final-builds.RetOwU/135-derived-centralizer-orbit-partitions`.
The four-stage build exited zero and reproduced the final PDF byte for byte.
Settled logs contain no error, warning, undefined citation/reference, bad box,
multiply defined label, or rerun request.

## 4. PDF, bibliography, and anonymity

The PDF is version 1.5, A4, rotation zero, unencrypted, form-free,
JavaScript-free, and has no metadata stream, image, or attachment.  Identifying
metadata is blank and the visible author is `Anonymous`.  All **31/31** fonts
are embedded, subsetted, and Unicode-mapped.  All **4/4** bibliography entries
are cited and resolved.  Every page has searchable text and the marker,
placeholder, identity, tool, path, and email scans are clean.

## 5. Five-page visual audit

- Page 1: abstract, local rule, recurrence/tail definitions, and main theorem
  are clean.
- Page 2: `f_0=1,c_0=0`, OGFs, fibre formula, and derived-wreath thresholds are
  legible.
- Page 3: reachable-tag invariants and two-clean proof fit without collision.
- Page 4: recurrent decoder, generating functions, fibre proof, and ownership
  paragraph are complete.
- Page 5: the ownership paragraph finishes before the table; the table and all
  four references are legible.  Residual whitespace is intentional.

## 6. Review closure and decision

All Review-A definition, locator, and layout minors are closed.  Review B
reconstructed the whole theorem package; its sole historical-hash-label minor
is closed by separate Round-0/current pins and an independent hash check.
Final severity is critical 0, major 0, minor 0.

**PASS / GO_INTERNAL.**  The anonymous internal theorem package is coherent
and reproducible.  **HOLD_EXTERNAL.**  No novelty, priority, authorship,
posting, submission, specialist contact, or release action is authorized.
