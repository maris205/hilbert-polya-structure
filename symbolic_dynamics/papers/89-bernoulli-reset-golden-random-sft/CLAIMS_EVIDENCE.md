# Claims–Evidence Map

| Claim | Proof location | Independent control |
|---|---|---|
| `N_n = 1^T M_0 ... M_(n-1) 1` counts all fibre paths | Equation (2.3), definition | Direct enumeration of every binary state path for all environments through `n=9` |
| `E A^k E = F_(k+2) E` for every `k>=0` | Lemma 3.1 | Integer matrix powers through `k=50` |
| Every environment product factors into boundary terms and Fibonacci gap gains | Lemma 3.1 | All binary environments through `n=15` |
| Boundary terms are `O(log n)` almost surely | Theorem 3.2 proof | Union bound and Borel--Cantelli; finite enumeration is not used as proof |
| Exact quenched entropy series | Theorem 3.2 | Renewal factorization plus exact geometric mass/moment checks |
| Endpoint values `h_q(0)=log(phi)` and `h_q(1)=0` | Theorem 3.2 | Direct powers of `A` and idempotence of `E` |
| `E[N_n] = 1^T ((1-p)A+pE)^n 1` exactly at finite `n` | Equation (4.1) | Full environment enumeration at three rational `p` values through `n=16` |
| Exact annealed exponent | Theorem 4.1 | Characteristic polynomial `t^2-t-(1-p)` and rational finite-time checks |
| Strict quenched--annealed gap for `0<p<1` | Theorem 4.1 | Exact rational reduction of `E[Z]=1` and nonconstancy witness; decimals are diagnostic only |
| Renewal CLT for `log N_n` | Theorem 5.1 | Classical delayed regenerative CLT with explicit first-reset clock and geometric moments; script checks the exact cycle ledger but is not a proof of convergence in distribution |
| Explicit variance series and strict positivity | Theorem 5.1 | Independent numeric evaluations at five `p` values; positivity is proved from the `K=0,1` cycles |
| Owner and release scope | Introduction and Section 6 | Source-verified bibliography plus bounded collision search; external release remains HOLD |

The program is a regression control, not a replacement for the almost-sure
limit, strict Jensen, or regenerative CLT arguments.  The iid Bernoulli
assumption and the exact two matrices are essential to the stated theorem
package.
