# Test report — C125

- producer: `C125_PREFREEZE_G3_PASS`;
- independent checker: `C125_CHECK_PASS` for twelve replay rows, all-order
  formulas, the zeta, Koopman obstruction, and all controls;
- separate SymPy reconstruction:
  `C125_SYMPY_PASS 238 exact symbolic checks`;
- canonical replay: `C125_REPLAY_PASS` through period twelve;
- hostile mutation audit: `C125_MUTATION_PASS 23 / 23`;
- Route-A YAML: canonical tuple and `route_b_invocation_allowed=false` checked
  against the evidence and source text;
- paper: two isolated fixed-date builds are byte-identical to each other and
  to the checked-in PDF;
- PDF: two pages, all fonts embedded, no unresolved reference/citation,
  overfull/underfull box, undefined label, or material package warning;
- raster inspection: both pages pass with no clipping, collision, truncation,
  or blank content;
- release manifest: all 27 included artifacts hash-close after the final
  paper build.

The checker imports no producer code.  Exact rows are derived from integer
matrix arithmetic; no tolerance or random seed is used.

## Final integrity and seven-mode audit

All seven ARS failure modes are `CLEAR` for the declared exact-theorem scope:

1. **implementation bug passing self-review:** independently written checker,
   SymPy reconstruction, replay, and 23 mutations all agree;
2. **hallucinated citation:** the package makes no external literature or
   novelty claim and contains no bibliography;
3. **hallucinated result:** every displayed count, coefficient, matrix action,
   and control is present in the canonical evidence and executable replay;
4. **shortcut reliance:** the orbit claims are all-order theorems, while the
   finite period/modulus tables are explicitly subordinate sentinels and
   controls;
5. **bug reframed as insight:** no failed assertion, compiler warning, or
   anomalous run is used as a theorem; the Koopman obstruction is proved from
   an explicit orthonormal sequence;
6. **methodology fabrication:** every declared method maps to a named script
   and successful command above; no unrun experiment, fit, or random seed is
   described;
7. **frame-lock:** the paper retains both the positive orbit-zeta theorem and
   the negative natural-owner result, rather than forcing determinant
   compatibility, and three structurally different controls test the frame.

The claim registry is the finite set of headline statements in
`THEOREM_PACKAGE.md`; coverage is complete for those declared claims.  This
does not certify literature novelty or any unregistered semantic claim.
