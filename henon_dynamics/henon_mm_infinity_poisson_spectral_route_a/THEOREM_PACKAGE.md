# C233 theorem package

For `lambda,mu>0`, set `rho=lambda/mu` and `a_t=exp(-mu t)`.

1. The unique reversible invariant law is `pi_n=exp(-rho)rho^n/n!`.
2. Conditional on `X_0=n`, `X_t` is the sum of an independent
   `Binomial(n,a_t)` survivor count and `Poisson(rho(1-a_t))` immigration.
3. Charlier polynomials defined by
   `sum_k C_k(n;rho) z^k/k! = exp(-rho z)(1+z)^n` satisfy
   `Q C_k=-mu*k C_k` and are orthogonal with norm `k!rho^k`.
4. Hence the normalized modes diagonalize the semigroup, the gap is `mu`,
   and for every `t>0` the trace is `(1-exp(-mu t))^{-1}` with source product
   `prod_{k>=0}(1-z exp(-k mu t))`.
5. Shared immigration gives
   `TV(P_t(n,.),P_t(m,.)) <= min(1,exp(-mu t)|n-m|)` and comparison with a
   stationary Poisson initial state gives `min(1,exp(-mu t)(n+rho))`.
6. The pure-death, pure-birth, identity, small-rho, small-mu and long-time
   faces are separate boundary statements.

The finite PMF and mode rows are deterministic regression oracles; they do not
stand in for the all-state polynomial and semigroup proof.
