# Exact-computation plan

1. Freeze thirteen rational parameter rows: five positive-pressure collapse
   cases, two zero-pressure equilibria, three negative-pressure expansion
   controls, and three `R0=0` boundary cases.
2. Serialize the exact first-integral parameters, Beta clock, collapse and
   expansion samples, terminal coefficient, energy, volume coefficient, and
   boundary nulls at 90 working digits and 54 displayed significant digits.
3. Use an independent checker: reconstruct rational inputs, evaluate the
   positive clock through a hypergeometric primitive, evaluate the expansion
   clock through its independent hypergeometric branch, and test monotonicity,
   energy, volume, and all sign faces.
4. Use SymPy for the first integral, Euler--Lagrange residual, Beta substitution,
   endpoint Puiseux coefficients, volume exponents, energy ledger, and `L^p`
   thresholds.  Replay bytes and run repaired-hash, stale-hash, unknown-key,
   route, scope, sign, and boundary mutations.
5. Compile three substantive LuaLaTeX revisions at
   `SOURCE_DATE_EPOCH=1787875200`; remove build sidecars and close the
   self-excluded 27-payload manifest only after two clean round-2 rebuilds.
