# Evidence — `AFC-20260914-PGS01`

The primorial gap cycles, their span `P_k`, and the exact recursion are sourced
as in [028](../../028-primorial-wheel-fibre-carrier/evidence/README.md), citing
Fred B. Holt, [*Discrete dynamics of Eratosthenes sieve*](https://arxiv.org/abs/2608.26384).

The roof calculation is elementary: the cyclic gaps between all consecutive
reduced residues mod `P_k` partition one period, so their sum is `P_k`. The
zeta convergence is recorded only for `Re(s)>0`: `P_k>=2^k`, hence
`sum_k exp(-sigma P_k)<infinity` for every `sigma>0`, so the logarithmic Euler
series converges absolutely. No continuation, divisor comparison, trace formula,
or Riemann identification is claimed.
