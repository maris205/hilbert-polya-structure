# Final QA — P139 Lyndon-factor-start feedback

**Date:** 2026-09-01 UTC.  **Result:** **PASS AFTER OWNER REPAIR**.
**Internal status:** **GO_INTERNAL**.  **External status:**
**HOLD_EXTERNAL**.

## 1. Final payload and review closure

The anonymous manuscript, five-entry verified bibliography, paper-local
verifier and canonical transcript, plans/evidence ledgers, two hostile reviews,
the final batch owner audit, a documented owner repair, an independent repair
review, and four immutable round PDFs are present.

The pre-repair `main_round0_original.pdf`, `main_round1.pdf`, and
`main_round2.pdf` are byte-identical: 324,120 bytes, SHA-256
`3d41d36820b33b2b4f9215dd55d8b9d620d7c39ae0f65c5512426c8d7b79acf0`.
The repaired `main.pdf` and `main_round3.pdf` are byte-identical: 326,430
bytes, four A4 pages, SHA-256
`3c4b474a05290223a1ea70a050cab1b7b46043b0ca3c67f88327d9f71ceb76e3`.

## 2. Mathematical gate

Independent reviewers reconstructed the leading-one amplifier, unique
recurrent state `1^n`, exact maximum depth `n`, uniqueness of the alternating
deepest source, and the target-wise fibre bijection with nonincreasing chains
of binary Lyndon words.  The matrix product and special target cells were
attacked separately.  A post-repair standalone checker reconfirmed all
dynamics through length 8 and the hostile outside-image mask `10110` without
importing the canonical verifier.

## 3. Owner gate

Mantaci--Restivo--Rosone--Sciortino (2014), Theorem 2.2, is now the controlling
owner for the factor-start/suffix-record equivalence.  That proposition, its
reproduced proof, and the ordered-tail comparison are explicitly owned static
input with zero contribution credit.  CFL factorization, Duval algorithms,
Lyndon arrays/trees, the binary Lyndon census, Möbius inversion, and generic
matrix multiplication are also subtracted.

The surviving residual is limited to repeated start-mask dynamics, the unique
sharp clock, and the ordered-Lyndon inverse atlas.  The independent repair
review found no remaining attribution overclaim.

## 4. Exact, build, PDF, and anonymity gates

The canonical transcript replays byte for byte with
`EXACT_ASSERTIONS=2654300` and `STATUS=PASS`; it exhausts functional graphs
through length 18 and ordered fibres through length 14.  A source-only
four-stage isolated build reproduces the repaired PDF byte for byte.  Settled
logs contain no warning, error, undefined citation/reference, bad box, or
rerun request.

All 25 font rows are embedded, subsetted, and Unicode-mapped.  The PDF is A4,
rotation zero, unencrypted, form-free, JavaScript-free, searchable, and has
blank identifying metadata.  All four pages were rasterized and inspected;
no clipping, overlap, malformed glyph, or identity leak was found.  The
visible author is `Anonymous`.

## 5. Decision

**PASS AFTER OWNER REPAIR / GO_INTERNAL.**  The theorem package survives and
the missing static owner is now fully subtracted.  **HOLD_EXTERNAL.**  Bounded
owner non-hits and internal review do not authorize novelty, priority,
authorship, posting, submission, specialist contact, or release.
