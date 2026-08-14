# HCS-C50 methodology blueprint

## Mathematical route

1. Freeze the C48 affine curve and verify every proposed automorphism in its
   function field.
2. Use quotient genera and the rational character table, rather than
   finite-prime fitting, to determine the differential representation.
3. Construct rational idempotents and identify their connected Jacobian
   images.
4. Match the first logarithmic coefficient at both degree-one primes over
   each split rational prime.
5. Put every denominator correction, higher Euler power, inert prime, and
   bad local factor into an explicit residual logarithm.
6. Keep all eight chronological variables and the \(\rho x_7x_0\) closing
   edge in the fourth moment.
7. Count radial roots on the four \((\mathcal C,\mathcal Q)\)-strata.
8. Prove characteristic-zero smoothness by exact elimination, then use
   openness only to obtain a finite exceptional set.
9. Compute middle Betti ranks from Chern classes and weak Lefschetz, apply
   Deligne at good primes, and normalize only at the final step.
10. Recompute every moment threshold and both operator-ideal thresholds.

## Reproducibility route

The theorem-bearing producer should certify:

- the rational identities for \(T,f,h\) modulo \(\rho^2+\rho+1\);
- all group relations and rational idempotent identities;
- the second-logarithm coefficient \(14+2a_p\);
- the eight-step projective direction identity;
- the split-quadric matrix and determinant;
- the Chern coefficients and ranks \(86,168\);
- the \(p=181\) recurrence, \(\mathcal C=0\), and \(\mathcal Q=0\);
- the exact fourth-moment substitutions and convergence inequalities; and
- the \(\tau\)-versus-classical ideal thresholds.

The checker must recompute these from frozen source data and reject schema
omissions. A finite point-count ledger is validation, not a proof of the
\(K\)-isogeny, smoothness outside finitely many primes, or analytic
continuation.

## Promotion and kill gates

- **GO:** rational identities and quotient genera force two standard blocks.
- **STOP:** a finite factorization pattern alone cannot prove a Jacobian
  decomposition.
- **GO:** the split-prime coefficient is an integer combination of
  \(\zeta_K\) and the curve \(L\)-function.
- **STOP:** any fractional global \(L\)-root reintroduces a branch
  obstruction.
- **GO:** the characteristic-zero recurrence ideal contains all coordinates.
- **STOP:** a finite smooth-prime scan cannot justify a cofinite theorem.
- **GO:** after normalization, the fourth moment is \(O(p^{-1/2})\).
- **STOP:** if a weight-six trace survived with coefficient \(p^{-2}\), the
  quarter wall would remain.
- **GO:** normal convergence starts with \(n=5\), giving \(\Re s>1/5\).
- **STOP:** do not call this a full functional equation or a zero-free
  continuation.
