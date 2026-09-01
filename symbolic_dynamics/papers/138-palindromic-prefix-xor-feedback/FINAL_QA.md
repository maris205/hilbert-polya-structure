# Final QA — P138 palindromic-prefix XOR feedback

**Date:** 2026-09-01 UTC.  **Result:** **PASS**.  **Internal status:**
**GO_INTERNAL**.  **External status:** **HOLD_EXTERNAL**.

## 1. Final payload and review closure

The anonymous manuscript, verified bibliography, paper-local verifier and
canonical transcript, plans/evidence ledgers, two independent hostile reviews,
and three immutable round PDFs are present.  Review A and Review B each
returned critical 0, major 0, repair-level minor 0.  No theorem or source
repair was required.

`main.pdf`, `main_round0_original.pdf`, `main_round1.pdf`, and
`main_round2.pdf` are byte-identical: 279,050 bytes, three A4 pages, SHA-256
`6c2114456c77df71516e4d9b2573907a1633cedeb9e77890c3cdcca318828942`.

## 2. Mathematical gate

Both reviewers independently reconstructed the complement quotient, the
one-step reset and leading-zero amplifier, the unique original strict
two-cycle `0^n <-> 1^n`, and the exact maximum-tail profile

```text
0, 1, n-2  for n=1, n=2, n>=3.
```

They also attacked the mod-four sharp witness and independently recovered its
complete palindromic-prefix set.  The left-to-right decoder was proved both
necessary and sufficient for every normalized target, including the unique
original-phase lift and targets outside the image.

## 3. Exact and build replay

The canonical paper-local run replays byte for byte with
`EXACT_ASSERTIONS=3870590` and `STATUS=PASS`.  It exhausts all words through
length 18, the decoder through length 15, and the sharp family through length
64.  An isolated four-stage build from only `main.tex` and `references.bib`
reproduces the final PDF byte for byte.  The settled logs contain no warning,
error, undefined citation/reference, bad box, or rerun request.

## 4. PDF, sources, and anonymity

All 21 font rows are embedded, subsetted, and Unicode-mapped.  The PDF is A4,
rotation zero, unencrypted, form-free, JavaScript-free, searchable, and has
blank identifying metadata.  Every page was rasterized and inspected; no
clipping, overlap, malformed glyph, or identity leak was found.  The visible
author is `Anonymous`.

Static palindrome recognition, storage, generation, and prefix encoding are
explicit zero-credit inputs.  The residual contribution is the repeated XOR
feedback dynamics, its quotient clock, and its target-wise inverse decoder.
The P134 whole-border-array firewall passed.

## 5. Decision

**PASS / GO_INTERNAL.**  The theorem and artifact package is coherent and
reproducible.  **HOLD_EXTERNAL.**  Bounded owner non-hits and internal review
do not authorize novelty, priority, authorship, posting, submission,
specialist contact, or release.
