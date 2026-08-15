# Author Response to Independent Round 1

**Review verdict:** `PASS_WITH_MINORS`  
**Review SHA-256:**
`b4b571cdcaf5aab6825235e2012fedf7e64b3434a14b17064f5d3d5a5b1a31a5`  
**Revision date:** 2026-08-14  
**Status:** all four required minors implemented; author-side verification
only, not an independent Round-2 review

## M1 — finite cycle field and valuation domain

**Response: accepted and repaired.** Theorem 4.1 now starts with a finite
extension `L/K` containing the cycle coordinates and explicitly takes `w` to
be an additive non-Archimedean valuation of `L` above the unique valuation of
`K` over two. The theorem and proof conclusions are unchanged.

## M2 — the Hensel bridge for `d | n`

**Response: accepted and repaired.** The proof of Proposition 5.1 now names
the unique lift `y` of `alpha` solving `g^d(y)=y` in
`K_{u,d} \subset K_{u,n}`. It states that `d | n` makes `y` a root of
`g^n-X`, after which uniqueness in the residue class identifies
`y=z_alpha`; reduction then excludes any smaller positive period.

## M3 — self-contained coefficient comparison modulo two

**Response: accepted and repaired.** Section 6 now identifies
`(2)=(u^3)` and
`O_{K_{u,n}}/(2) \simeq F_{2^n}[\bar u]/(\bar u^3)`, including the basis
`1,\bar u,\bar u^2`. It records that the square's cross terms carry a factor
two and vanish modulo `u^3`. With `t=u+u^2`, it then writes
`t^2=u^2`, `t^3=0`, `e_n=1`, and `e_k in F_2` before displaying the norm
expansion and comparing its two nilpotent coefficients.

## M4 — certificate independence class

**Response: accepted and calibrated.** The abstract, contribution list,
Figure 2 caption, registered-audit section, Appendix B certificate display,
and raw-ledger commentary now describe gcd and resultant/field norm as
separately implemented but algebraically equivalent exact certificates.
The wording no longer suggests logically or statistically independent target
evidence. The independent result-integrity audit remains labeled independent
because that is a distinct reviewed artifact.

## Revision verification

- revised source SHA-256:
  `60a9868f92b2d34e9ae140cebc534118225d05fe647530df1341c5ad0cc96974`;
- revised PDF SHA-256:
  `fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf`;
- revised PDF: 11 pages; the discussion ends and references begin on page 9;
- two consecutive deterministic builds have the same revised-PDF hash;
- final log: zero errors, warnings, undefined citations/references, or box
  warnings; all 33 fonts are embedded and subset;
- all 11 revised pages passed author-side visual inspection;
- safe tests: 38 passed; the strict 12-file result manifest and 32-path figure
  manifest both close under their recorded hashes; all nine frozen figure
  outputs retain their byte-reproducibility record;
- citations remain closed at 12 cited and 12 verified BibTeX entries, with no
  missing or unused key;
- the original pre-review PDF remains immutable at
  `36cf7d4f50ef712e3208565d081a57dd5602a828c3eedc5ad50e4386603bf8be`;
- the paper plan, source lock, proof package, official result, result manifest,
  bibliography, and all frozen figure outputs are unchanged.

No candidate was rerun or extended, no new citation or datum was added, and no
optional presentation change was made. The all-period equality question
remains `OPEN_FOR_N_GE_4`; Route A is not advanced and Route B is not opened.
A fresh reviewer must perform Round 2. This response is not an independent
acceptance decision.
