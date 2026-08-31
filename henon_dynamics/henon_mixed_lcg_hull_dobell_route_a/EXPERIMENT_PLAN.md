# Exact verification plan

1. Freeze m at every integer from 2 through 96 and enumerate all m squared
   residue pairs (a,c).
2. Starting at zero, compute the exact orbit and compare full-cycle status
   against the three Hull--Dobell conditions.
3. Independently reconstruct the factorization, condition modulus, Euler
   totient, predicted admissible-pair count, and accumulated orbit work.
4. On six composite and prime-power controls, verify every fixed count through
   time 2m, the unique primitive cycle, source zeta, and Koopman polynomial.
5. Check odd and dyadic return-gap valuations without importing the producer.
6. Use SymPy for affine iterates, cycle determinants, and unitarity.
7. Require byte-identical replay and rejection of at least twenty repaired-hash
   semantic mutations.

The finite census is only a regression oracle.  The all-modulus conclusion is
carried by the prime-power valuation proof and CRT.
