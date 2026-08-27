# Results

- Canonical evidence: `c206_couette_evidence.json`.
- 675 exact Fourier cells and 54 exact composition cells.
- Exact rational exponents are retained; 1,350 exponential fields are computed
  at 100 working decimal digits and serialized to 82 significant digits.
- Exact formula and sharp sector norm hold for every declared continuous
  parameter by proof. The norm is not attained by a nonzero `L2` vector when
  `nu*t>0`, is approached by frequency-localized packets, and is attained on
  every nonzero vector at the unitary boundary `nu*t=0`.
- Independent checker, SymPy reconstruction, byte replay, and hostile mutation tests pass.
- Strict tuple: `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
- Overall: `ROUTE_A_REJECTED`; `route_b_invocation_allowed=false`.

Finite cells are regression sentinels, not the authority for the theorem.
