# HCS-C276 — uniform random mapping functional graphs

This package proves and independently certifies a complete finite/asymptotic
closure for the functional graph of a uniform random function `f:[n]->[n]`.
For `C_n` cyclic vertices, `K_n` weak components, and a marked orbit with tail
`mu`, cycle length `lambda`, and collision length `R_n=mu+lambda`, it gives:

- the exact joint count
  `binom(n,k)c(k,r) k n^(n-k-1)`, including the empty-forest face `k=n`;
- `P(C_n=k)=(n)_k k/n^(k+1)` and
  `E[# ell-cycles]=(n)_ell/(ell n^ell)`;
- `P(mu=u,lambda=l)=(n-1)_(u+l-1)/n^(u+l)` and the exact identity
  `C_n =_d R_n`;
- Rayleigh limits for `C_n/sqrt(n)` and `R_n/sqrt(n)`, and joint limiting
  density `exp(-(x+y)^2/2)` for `(mu,lambda)/sqrt(n)`.

The status is **PROVABLE AS STATED**.  Exhaustive enumeration of all 873,612
maps for `1<=n<=7` is regression evidence, not the all-`n` proof.  The proof is
in [THEOREM_PACKAGE.md](THEOREM_PACKAGE.md), executable receipts are under
`results/`, and the compiled article is `paper/main.pdf`.

The strict Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, the verdict is
`ROUTE_A_REJECTED`, and Route B is disabled.  Under
`NO_BAD_EULER_OR_ROOT_NUMBER`, an ensemble probability generating function is
not renamed as an arithmetic zeta function, target determinant, or spectral
operator.
