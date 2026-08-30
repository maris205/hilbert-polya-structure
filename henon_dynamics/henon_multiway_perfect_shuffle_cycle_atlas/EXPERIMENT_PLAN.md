# Experiment and validation plan

1. Freeze the Ellis--Fan--Shallit multiway convention
   \\(\\rho_{k,n}(i)=ki\\bmod (kn+1)\\) on nonzero residue positions, the
   evaluator authority, source baseline `489506cf92bfed721f94f22dd0444a60427f90a5`,
   and the `NO_BAD_EULER_OR_ROOT_NUMBER` firewall.
2. Generate the cross-parameter grid `2<=k<=6, 1<=n<=10`, with exact integer
   fixed counts, least periods, cycle counts, gcd strata, and direct cycle
   representatives.
3. Reconstruct every formula in a producer-independent checker.  The checker
   independently enumerates the finite permutation and verifies the
   \\(\\gcd\\), order, and Möbius identities rather than importing producer code.
4. Check the source-local zeta factorization
   \\(\\prod_r(1-z^r)^{-C_r}\\) and the finite Koopman characteristic factors
   \\(\\prod_r(\\lambda^r-1)^{C_r}\\), including exact zeta-denominator and
   Koopman-polynomial coefficient rows for small
   moduli.
5. Run independent SymPy congruence, polynomial, and permutation-matrix
   checks; then replay the producer in a clean temporary directory byte-for-byte.
6. Run the 44-case hostile suite, including repaired-payload-hash mutations
   of numerical rows, cycle order, theorem text, citation metadata, route and
   scope flags, unknown keys, and missing rows.
7. Build three substantive paper rounds.  Every round is compiled twice in
   fresh directories with LuaLaTeX, `SOURCE_DATE_EPOCH=1788048000`, embedded
   subset fonts, and settled-log scans for errors, references, boxes and
   missing characters.
8. Close the self-excluded 27-payload/28-physical-file release manifest and
   retain the three distinct round PDFs as revision evidence.
