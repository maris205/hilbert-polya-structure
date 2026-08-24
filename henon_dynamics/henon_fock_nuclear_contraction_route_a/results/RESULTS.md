# Results — C119

- Matrix eigenvalues: `1/2,1/4`; determinant: `1/8`.
- Squared singular values: `(7±3*sqrt(5))/16`, both in `(0,1)`.
- `Gamma(A)` is trace class with
  `||Gamma(A)||_1=1/((1-s_1)(1-s_2))`.
- Trace prefix `n=1..8`:
  `8/3, 64/45, 512/441, 4096/3825, 32768/31713, 262144/257985, 2097152/2080641, 16777216/16711425`.
- Fredholm Taylor coefficients `d_0..d_8` are recorded exactly in the evidence.
- Zeros: `2^k` with multiplicity `floor(k/2)+1`, for every `k>=0`.
- Strict Route-A verdict: `A1_FAIL`, `A2_FAIL`, `A3_FAIL`, `A4_FAIL`,
  overall `ROUTE_A_EXPLORATORY`.  The exact source-owned Fock determinant is
  structural evidence, not an orbit-zeta/target-divisor certificate.
