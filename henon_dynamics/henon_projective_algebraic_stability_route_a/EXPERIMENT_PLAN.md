# Experiment plan — C121

## Frozen objects

- family: \(H_c(x,y)=(x^2+c-y,x)\);
- release parameter: \(c=-4\);
- forward projective coordinates:
  \([X^2-4Z^2-YZ:XZ:Z^2]\);
- inverse projective coordinates:
  \([YZ:Y^2-4Z^2-XZ:Z^2]\);
- recurrence: \(p_{-1}=y,p_0=x,p_n=p_{n-1}^2-4-p_{n-2}\);
- replay range: \(1\leq n\leq8\);
- control parameters: \(c=-3,-5\);
- release scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Gates

1. Verify both affine inverse compositions exactly.
2. Solve the forward and inverse projective base loci and identify the image
   and forward orbit of the exceptional line.
3. Prove by recurrence that the coordinate degrees are
   \((2^n,2^{n-1})\) and that the homogenized triple has no common factor.
4. Store an exact recursive DAG hash, sparse leading certificate, and exact
   integer probes for \(n=1,\ldots,8\), without full degree-256 expansion.
5. Certify both fixed points and the primitive real two-cycle with its exact
   tangent monodromy and determinant polynomial.
6. Show that the same proposed cycle fails at \(c=-3,-5\).
7. Run a producer, independent checker, fresh SymPy reconstruction, canonical
   replay, and at least ten hostile mutations.
8. Compile the paper in two isolated fixed-date directories, compare bytes,
   inspect fonts and logs, and close a content-addressed manifest.
9. Apply only the canonical labels from the repository Route-A evaluator:
   exact structural evidence without a prime-like correspondence is A1 weak;
   absent determinant/divisor and analytic-bridge objects force A2 and A3
   fail, respectively.

## Failure conditions

- a hidden common factor in an iterate homogenization;
- confusing the forward and inverse indeterminacy points;
- using expanded degree-256 algebra as the sole replay mechanism;
- failing to distinguish a primitive cycle from a repeated fixed point;
- presenting a parameter control as preserving the frozen witness;
- upgrading algebraic dynamical degree to an entropy identity;
- upgrading a tangent matrix to a transfer or Fredholm operator;
- upgrading one primitive cycle to a prime-like target correspondence;
- hiding the missing target divisor or analytic bridge behind a noncanonical
  “not addressed” verdict;
- accepted hostile mutation, nondeterministic PDF, unembedded font, unresolved
  reference, layout warning, or manifest mismatch.
