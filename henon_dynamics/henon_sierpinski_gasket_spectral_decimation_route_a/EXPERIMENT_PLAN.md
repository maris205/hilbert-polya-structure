# C184 exact validation plan

## Claims under test

1. For the Dirichlet matrix \(L_m\), restriction and local extension are
   governed away from exceptional values by
   \(R(\lambda)=\lambda(5-\lambda)\) and its two inverse branches.
2. The complete spectrum consists of the 2-, 5-, and 6-series.  A 6-series
   born at level \(j\) has seed 6 and, if continued, must next take the
   allowed preimage 3; the preimage 2 is forbidden at that step.
3. The birth multiplicities are respectively \(1\),
   \((3^{j-1}+3)/2\), and \((3^j-3)/2\), and their weighted lineage sum is
   \(N_m=(3^{m+1}-3)/2\).
4. The characteristic recurrence has an exact exceptional-factor
   cancellation, and its evaluation at zero yields the closed determinant.
5. Heat and finite-zeta formulas are exact finite spectral consequences,
   not claims about the limiting fractal spectral zeta.
6. The level inverse-branch tree is not physical time and cannot be relabeled
   as an intrinsic primitive-orbit clock.

## Independent validation paths

- The producer constructs pre-gasket graphs by recursive triangle
  refinement, emits the all-level formula ledger, builds exact integer
  characteristic polynomials through level five, and uses numerical graph
  diagonalization only as a regression control.
- The checker imports no producer code.  It constructs the graph by
  independent iterated edge copies, reconstructs polynomials by a different
  convolution/substitution path, uses fraction-free Bareiss determinants,
  tests characteristic values directly, and independently enumerates all
  lineages.
- The SymPy path directly forms graph matrices and characteristic
  polynomials through level four, rebuilds the recurrence through level
  five, and checks the dimension and determinant exponent formulas far
  beyond the released graph cutoff.
- Replay regenerates the evidence byte for byte.
- Seventy repaired-hash semantic mutations and one stale-hash mutation
  attack identity, every source-lock field, exceptional branches,
  coefficients, lineages, Route-A gates, scope, citation metadata,
  integrity modes, and nonclaims.

The finite ledger covers \(1\le m\le5\), 103 lineage rows, 542 exact
coefficient cells, and 537 numerically diagonalized eigenvalue cells.  These
rows are regression sentinels.  The all-level conclusion rests on the
spectral-decimation, kernel-count, and algebraic proofs in
`THEOREM_PACKAGE.md` and the manuscript.
