# Methodology blueprint

## Mathematical route

1. Freeze the six ordered variables and the closing coefficient \(\rho\).
2. Count radial roots on the four \((\mathcal C,\mathcal Q)\) strata.
3. Count the split quadric by its even--odd bilinear form.
4. Count the Fermat cubic by cubic characters and Gauss/Jacobi sums.
5. Prove characteristic-zero smoothness of \(X=S\cap Q\), then use openness
   for the theorem-level finite-exception statement.
6. Compute \(K_X\), \(H^3\), the Chern class, \(b_3\), and Frobenius weights.
7. Substitute point counts before applying any asymptotic estimate.
8. Divide by the real cyclotomic degree \(d_p\) only at the final step.
9. Recompute all four convergence thresholds and the semifinite ideal order.

## Exact computational route

The producer must implement two independent paths:

* chronological dynamic programming for \(Z_{p,3}\), preserving endpoint
  and phase residue;
* projective point counts of (S,Q,X) on disjoint normalization charts.

The checker must independently verify:

* the recurrence singular ideal;
* the degree-21 elimination polynomial (R(t));
* the rational resultant \(2^{21}3^{12}23^3\);
* every split divisor of the projection denominator;
* the exact identity \(Z=p^5-p^2-A-pB\);
* rational, rather than rounded, \(C_{p,3}\).

## Promotion rules

* Small-prime smoothness scans are controls, not a proof.
* \(B_p/p\in\mathbf Z\) may be promoted because Chevalley--Warning proves it.
* The Jacobi formula for \(A_p\) may be promoted because the six-variable
  character calculation is included in `PROOF_PACKAGE.md`.
* Any finer law for \(b_p\) remains `OBSERVED` until a geometric
  correspondence is proved.
* The all-split smoothness sentence remains gated until exact independent
  replay of the leading-coefficient primes.
