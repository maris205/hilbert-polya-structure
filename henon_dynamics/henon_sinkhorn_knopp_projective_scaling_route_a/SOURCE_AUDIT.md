# C191 source audit

All bibliographic metadata below was checked against publisher or author-hosted
records.  The package claims a reproducible synthesis and derived convention
ledger, not priority for the classical theorems.

## Source-locked results

1. R. Sinkhorn and P. Knopp, “Concerning nonnegative matrices and doubly
   stochastic matrices,” *Pacific Journal of Mathematics* 21(2) (1967),
   343--348, DOI `10.2140/pjm.1967.21.343`.

   This is the authority for the alternating-normalization convergence
   criterion, the support/total-support distinction, and the fact that an
   entry outside every positive diagonal vanishes in the limiting process.

2. R. A. Brualdi, S. V. Parter and H. Schneider, “The diagonal equivalence of
   a nonnegative matrix to a stochastic matrix,” *Journal of Mathematical
   Analysis and Applications* 16(1) (1966), 31--50, DOI
   `10.1016/0022-247X(66)90184-3`.

   This is the primary full-indecomposability/factor-uniqueness source.  Its
   theorem is not presented as new here.

3. J. Franklin and J. Lorenz, “On the scaling of multidimensional matrices,”
   *Linear Algebra and its Applications* 114--115 (1989), 717--735, DOI
   `10.1016/0024-3795(89)90490-4`.

   This supplies the Hilbert-projective proof of geometric convergence and a
   data-dependent ratio.  It does not supply a dimension-only uniform rate.

4. P. A. Knight, “The Sinkhorn--Knopp algorithm: convergence and
   applications,” *SIAM Journal on Matrix Analysis and Applications* 30(1)
   (2008), 261--275, DOI `10.1137/060659624`.

   This supports the convergence synthesis and the local asymptotic rate in
   terms of the second singular value of the doubly stochastic limit.

## Package-owned derivations

The package fixes one row-then-column clock, writes its positive scaling-vector
map explicitly, differentiates it in logarithmic coordinates to obtain
`S^T S`, and places the support, total-support, gauge, contraction, local-rate
and recurrence boundaries in one theorem ledger.  It also supplies two
independent zero-pattern algorithms, exact rational scaling oracles, a
separate SymPy reconstruction, byte replay and semantic mutation tests.

## Citation and claim firewall

- No source is cited for a stronger claim than it contains.
- Strict positivity is not silently extended across zeros in the Hilbert
  contraction formula.
- The full-cycle local rate is not advertised as a global uniform rate.
- The finite census is not treated as proof of convergence for arbitrary
  matrices.
- No prime table, zero table, local arithmetic datum, Euler factor, root
  number, automorphy object, target divisor or Route-B input appears.
