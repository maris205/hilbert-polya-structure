# Final QA — P140 random majority-of-three contraction

**Date:** 2026-09-01 UTC.  **Result:** **PASS AFTER REPAIR**.  **Internal
status:** **GO_INTERNAL**.  **External status:** **HOLD_EXTERNAL**.

## 1. Final payload and review closure

The anonymous manuscript, verified bibliography, paper-local verifier and
canonical transcript, evidence ledgers, two independent hostile reviews, and
three immutable round PDFs are present.  Review A reported one major boundary
scope defect and no critical defect.  The repair was implemented before Round
B, which returned critical 0, major 0, minor 0.

The original `main_round0_original.pdf` is preserved at 259,329 bytes and
SHA-256
`2b151d0916d8d43d26988f3f70a25885fdf8e71255657dc1486bc300e070aa99`.
The repaired `main.pdf`, `main_round1.pdf`, and `main_round2.pdf` are
byte-identical at 260,643 bytes, four A4 pages, SHA-256
`a04683cd14c2ac0ecea73ae6baf98f17ef1a0c947ba712f25529b0087d839c18`.

## 2. Mathematical gate

Both reviewers reconstructed the exact two-run transition kernel, terminal
endpoint and complete-history counts, cross-boundary generating polynomial,
its support and one-cross atom, and the continuous-time odd-rate clock law.
The Round-A defect is closed as follows:

- at `n=1`, both embedded vectors are empty and `tau_1=0` almost surely;
- the Laplace empty product equals one and the moment empty sums equal zero;
- `e^{-2 tau_n} ~ Beta(1/2,m)` is stated only for `n=2m+1>=3`, `m>=1`;
- the Gamma limit is explicitly along odd lengths with `m -> infinity`.

Review B's standalone enumeration checked 818 exact conditions through the
sharp small boundaries without importing the canonical verifier.

## 3. Exact and build replay

The canonical transcript replays byte for byte with
`exact_assertions=190740` and `status=PASS`.  A fresh isolated four-stage
build from only `main.tex` and `references.bib` reproduces the repaired PDF
byte for byte.  Settled LaTeX and BibTeX logs contain no warning, error,
undefined citation/reference, bad box, or rerun request.

## 4. PDF, sources, and anonymity

All 22 font rows are embedded, subsetted, and Unicode-mapped.  The PDF is A4,
rotation zero, unencrypted, form-free, JavaScript-free, searchable, and has
blank identifying metadata.  All four pages were rasterized and inspected;
no clipping, overlap, malformed glyph, or identity leak was found.  The
visible author is `Anonymous`.  Both bibliography entries are cited and
resolved.

Fixed-carrier majority systems, generic exponential races, and generic
Beta/Gamma identities remain zero-credit background.  The residual is the
shrinking current-window process, its two-run/history/crossing atlas, and its
whole-history clock theorem.  The owner and internal collision gates passed.

## 5. Decision

**PASS AFTER REPAIR / GO_INTERNAL.**  The only major review finding is closed,
and the final theorem/artifact package is coherent and reproducible.
**HOLD_EXTERNAL.**  Bounded owner non-hits and internal review do not authorize
novelty, priority, authorship, posting, submission, specialist contact, or
release.
