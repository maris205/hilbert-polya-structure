# Small exact checks for the two-clock candidate

2026-09-06. Supporting sanity checks only. The general convergence,
continuation, polar-divisor and natural-boundary assertions rest on
`RECTANGULAR_RETURN_PROOF.md`, not on finite computation.

Run `python rectangular_exact_checks.py` in this directory. The script
uses the Python standard library and writes no files.

The actual run passed:

- 784 explicit intersections of finite rational-point circle kernels,
  for $2\leq a,b\leq8$ and $1\leq n,m\leq4$;
- 24,624 dependent-branch coefficient comparisons, for
  $2\leq c\leq5$, coprime $1\leq r,s\leq5$ and
  $1\leq n,m\leq18$, including the identity
  $h_{i,j}=\gcd(r,j)\gcd(s,i)\mid rs$ and primitive-ray coefficients;
- the exact four-component intersection at
  $c=2,r=s=1,x_0=y_0=2^{-1/5}$, whose slice residue factor is
  $1+1/2+1/3+1/4=25/12$, so the residue is $-25x_0/12$.

There was no large search, asymptotic fit, floating-point pole test,
Diophantine-bound inference, or attempt to validate an infinite
natural-boundary statement by sampling. These tests do not certify
novelty or independent-contract substance.
