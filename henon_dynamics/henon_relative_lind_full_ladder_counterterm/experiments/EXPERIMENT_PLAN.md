# Experiment plan

1. Lock the P71 and P72 proof packages, certificates, and PDFs by six exact
   SHA-256 dependencies.
2. Reconstruct all `2m` complex roots and principal coefficients for levels
   `2<=m<=12` in the main certificate.
3. Compare the primitive/repetition tail with the scalar-channel expansion
   through degree 96 in the certificate and degree 120 in tests.
4. Verify all genus-`m-1` Taylor cancellations through level 79 and audit an
   exact geometric normal-convergence majorant.
5. Independently reconstruct regularized partial fractions through level 64
   at three complex sample points; samples diagnose the implementation and
   do not prove the theorem.
6. Run eight tests under normal and optimized Python and reject 25 mutations,
   including false operator, arithmetic, and Route-B promotions.
