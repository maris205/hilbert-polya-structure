# Assumptions and conventions

- `n>=3` unless a finite evidence range is explicitly stated.
- `m=2^n`, `alpha_n=2^(1/m)`, and `zeta_m` is a fixed primitive
  `m`-th root of unity.
- `R_n={zeta_m^j alpha_n: j in Z/m}` and
  `K_n=Q(alpha_n,zeta_m)`.
- `(2/a)=(-1)^((a^2-1)/8)` is the conductor-eight quadratic character
  for odd `a`.
- A pair `(a,b)` acts on root indices by `j -> a*j+b (mod m)`; composition
  is `(a,b)(c,d)=(ac,a*d+b)`.
- Arithmetic Frobenius is used.  Geometric Frobenius is its inverse and
  has the same number of fixed roots.
- Only the prime `2` is excluded from Frobenius density statements.  It is
  the unique prime that can ramify in the splitting field of `x^m-2`.
- Natural density follows from Chebotarev for the conjugacy-stable fixed-
  point subsets of the finite Galois group.
- The finite range `3<=n<=12`, `p<=100000` is a deterministic regression
  range, not an assumption behind the theorem.
