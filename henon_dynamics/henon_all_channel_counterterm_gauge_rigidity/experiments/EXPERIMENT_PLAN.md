# Experiment plan

1. Hash-lock the P72 and P73 proof packages, executable certificates, and
   compiled PDFs.
2. Replay the exact coefficient identity
   `c_m=m^(-1)sum_(d|m,d odd)d mu(d)` against the odd-radical Euler product
   for at least 149 channels in tests.
3. Check the weighted `2m`-root filter and the first several source
   coefficients of every pole orbit.
4. Compare, through degree 96 in the certificate and degree 179 in tests,
   the relative channel log with:
   - the genus `m-1` multiplier, whose residual must be zero;
   - the genus `m` multiplier, whose residual must be `-2c_m t^m`.
5. Independently reconstruct the degree-96 coefficient ledger without
   importing the producer.
6. Verify the exact source ledger and forced pair `(a,beta)=(3/4,1/2)`.
7. Construct gauge witnesses preserving every jet of order zero through 12
   in the certificate and through 19 in tests.
8. Run 16 unit tests under normal and optimized Python.
9. Reject mutations that flip the multiplier sign, forge a unique gauge,
   alter the source pair, promote an operator/arithmetic claim, or authorize
   Route B.

Finite computation audits signs and artifact integrity.  It does not prove
normal convergence or infinite coefficient rigidity; those proofs are in
the proof package and manuscript.
