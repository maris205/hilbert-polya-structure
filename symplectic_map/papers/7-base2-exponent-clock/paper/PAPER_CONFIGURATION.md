# Paper Configuration

- Project: `pcf_quadratic_exact_2adic_boundary_v1`
- Format: anonymous specialist arithmetic-dynamics article (`article`, 11 pt,
  single column); no conference style or venue-specific page claim is made.
- Working title: *Exact 2-Adic Valuation of Higher-Period Multipliers for a
  Frozen PCF Quadratic*.
- Document date: 2026-08-14.
- Length: 11 pages total.  The revised main text through Section 8 ends on
  page 9; references begin on page 9 and appendices occupy pages 10--11.
- Bibliography: numerical `natbib`, 12 cited entries and 12 verified entries,
  with no missing or unused key.  Metadata remain bound to
  `notes/CITATION_VERIFICATION.md`.
- Figures: three frozen-data vector PDF masters with SVG and 300 dpi PNG
  companions.  The manuscript displays all three and preserves their planned
  semantic order: boundary map, finite ledger, Frobenius filter.
- Build: `paper/build.sh` fixes `SOURCE_DATE_EPOCH`, `FORCE_SOURCE_DATE`, and
  `TZ`; it uses `latexmk` when available and the deterministic
  `pdflatex -> bibtex -> pdflatex x3` fallback in this environment.
- Pre-review PDF: `paper/paper_pre_review.pdf`, SHA-256
  `36cf7d4f50ef712e3208565d081a57dd5602a828c3eedc5ad50e4386603bf8be`.
- Round-1 revision PDF: `paper/paper_round1_revision.pdf`, SHA-256
  `fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf`.
- Final PDF: `paper/paper_final.pdf`, SHA-256
  `fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf`;
  it is byte-identical to the independently approved Round-1 revision PDF.
- Review policy: independent Round 1 returned `PASS_WITH_MINORS`; independent
  Round 2 returned `PASS / MAY_FINALIZE`, review SHA-256
  `f9a9937fd439bd5a91df1b45709775615fc1fe7920777488d72e8d1e6cfb62d6`.
  The local manuscript status is `COMPLETE_LOCAL_FINAL_REVIEW_PASS`.

## Scientific boundary

The all-period theorem is the exact local identity
`w(Lambda_C)=n*w(2)` for exact `n>=2`, and its rational corollary is
`Lambda_C=2^n*m` with `m` odd.  Equality is proved absent at periods two and
three by the local coefficient obstruction and is reproduced as absent over
the development-seen finite set `n=2,...,7`.  No uniform exclusion for every
`n>=4` is proved; the status remains `OPEN_FOR_N_GE_4`.

The manuscript does not decide complex-modulus equality without rationality
or characteristic-exponent equality.  It makes no general PCF rigidity,
prime-orbit, zeta-zero, quantization, or downstream route claim.  Route A is
not advanced and Route B is not opened.

## Review and finalization boundary

The revision is limited to four changes requested in
`paper/reviews/round1_review.md`: the finite cycle-field and valuation domain
in Theorem 4.1, the `d | n` Hensel-uniqueness bridge in Proposition 5.1, the
explicit modulo-two quotient-ring calculation in Section 6, and calibration
of gcd/resultant evidence as separately implemented but algebraically
equivalent exact certificates.  No theorem conclusion, frozen input, result,
figure, bibliography entry, registered period, or route status changed.  The
bounded response is `paper/reviews/round1_response.md`; fresh independent
Round 2 verified all four repairs and the complete regression package with no
residual blocker.  Finalization was purely mechanical: the accepted source was
not altered, two isolated deterministic builds reproduced the approved PDF,
and that byte-identical artifact was copied to `paper/paper_final.pdf`.
Repository synchronization remains deferred to the Session batch rule.
