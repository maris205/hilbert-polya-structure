# Paper Configuration

- Candidate: `cat_torsion_primitive_divisor_capacity_v1`.
- Format: anonymous specialist mathematical technical note (`article`, 11 pt,
  single column); no venue-specific page or acceptance claim is made.
- Title: *A Primitive-Divisor Audit of Prime-Order Torsion Periods for
  Hyperbolic Toral Automorphisms*.
- Document date: 2026-08-14.
- Length: 12 pages total, including three appendices and 14 references.
- Bibliography: numerical `natbib`; 14 cited keys and the same 14 verified
  BibTeX entries, with zero missing or unused key. Metadata and permitted
  citation roles remain bound to `notes/CITATION_VERIFICATION.md`.
- Figures: three manifest-bound vector PDF masters, each with selectable-text
  SVG and 300 dpi PNG companions. All three are included with semantic
  captions in the order arithmetic bridge, standard-cat boundary, and
  capacity-versus-specificity obstruction.
- Build: `paper/build.sh` fixes `SOURCE_DATE_EPOCH`, `FORCE_SOURCE_DATE`, and
  `TZ`; in this environment it uses the deterministic
  `pdflatex -> bibtex -> pdflatex x2` fallback.
- Pre-review PDF: `paper/paper_pre_review.pdf`, SHA-256
  `9b7594015e3e6eb3db759ea1eea27a2249c513368ce9c063382be76e041357f8`.
- Round-1 revision PDF: `paper/paper_round1_revision.pdf`, SHA-256
  `5ff37aca10905bd7fd84f25a81e47601ed9883259519b02e2809f77485770d98`.
- Independent Round-2 review: `paper/reviews/round2_review.md`, SHA-256
  `4f0da5c2174b6185a743e8834fa2a3c73b72fc4afa09b811cd730f3ad95f5d95`,
  verdict `PASS -- MAY FINALIZE`, score `9.2/10`, with zero Critical,
  Major, or Minor finding.
- Final PDF: `paper/paper_final.pdf`, SHA-256
  `5ff37aca10905bd7fd84f25a81e47601ed9883259519b02e2809f77485770d98`.
  It is byte-identical to the independently approved Round-1 revision PDF.
- Revised source: `paper/manuscript.tex`, SHA-256
  `95ebccff1eb5f2b939be92c9a8b7020b625d4b8056cc5b6bda3b3814fcae580c`.
- Plan authority: `PAPER_PLAN.md`, SHA-256
  `6d87e00c8cf5b21c021dfe38b572ec16d5551f576615fced4abdc72f6f70a885`.
- Independent plan/figure/citation gate:
  `notes/INDEPENDENT_PLAN_FIGURE_REVIEW.md`, SHA-256
  `a5e2eab53b97765bee6cedc004f4e77a29c0647c5a0186c2cd8eda7bc8262655`,
  verdict `PAPER8_PLAN_FIGURE_CITATION_PASS` for the pre-review package.
- Round-1 review: `paper/reviews/round1_review.md`, SHA-256
  `bb64f75c96ca0b3d2e78a3b295a1d1b8321ea2143f4612e08b316594991e5ac5`,
  verdict `MINOR REVISION` with three bounded items.
- Round-1 response: `paper/reviews/round1_response.md`, SHA-256
  `85b618e7a0cbd28ac4bed4cea93e3cdc7a0593a1ba7357fc9f1944650c0950eb`,
  status `3/3 IMPLEMENTED; AUTHOR VERIFIED`.
- Review state: `COMPLETE_LOCAL_FINAL_REVIEW_PASS`. Independent Round 2
  authorized finalization; terminal finalization was mechanical and changed
  no manuscript source, scientific content, reference, figure, source-lock,
  code, or result artifact.

## Scientific boundary

The note derives a prime-additive-order exact-period carrier for every
hyperbolic matrix in `SL_2(Z)` and every integer period above 12. The direct
Flatters corollary is restricted to positive trace; negative trace is covered
by the separately proved odd / divisible-by-four / half-index parity split.
For the standard cat matrix, a carrier exists exactly outside
`{1,6,12}`, with period 10 supplied by the ramified modulo-five Jordan
calculation rather than a primitive divisor.

The torsion-order label certifies intrinsic all-order capacity but fails prime
specificity and regularity. The frozen classification is
`INTRINSIC_TORSION_CAPACITY_CERTIFIED / A0_FAIL_PROVES_TOO_MUCH`, with Route A
status `A0_FAIL_PROVES_TOO_MUCH_NO_A1_TO_A4` and Route B `NOT_OPENED`.

## Evidence and release boundary

The sole registered exact audit covers only periods 1 through 12. It supports
the finite ledger, finite-field profiles, and falsification controls; it does
not support the infinite tail, which is theorem-only. No candidate numerical
run, tail-period computation, external prime table, Riemann-zero data,
floating match, transfer/Fredholm construction, quantization, or priority
claim was introduced during manuscript production or bounded revision.
`paper_round1_revision.pdf` is the immutable Round-2 review artifact; the
original `paper_pre_review.pdf` also remains immutable. `paper_final.pdf` is
an exact byte-for-byte copy of the approved revision artifact. Two isolated
clean builds independently reproduced the same final digest. The terminal
release status is `COMPLETE_LOCAL_FINAL_REVIEW_PASS`.
