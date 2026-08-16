# Hostile review round 1

**Attack:** P72 already proves normal convergence of the channel-grouped
series, so individual pole ordering should be harmless.

**Resolution:** grouping hides a real conditional cancellation.  At `t=0`,
the absolute mass of the `2m` raw poles is `sqrt(2)|c_m|`; odd prime levels
alone make the sum diverge.  The raw double series cannot be reordered.

**Attack:** subtracting Taylor polynomials changes the target.

**Resolution:** for `0<=j<m`, the signed `2m`-root sum is exactly zero.  Each
level therefore retains the exact rational channel after genus-`m-1`
regularization.

**Attack:** compact convergence is inferred from finite numerics.

**Resolution:** the proof bounds the complete level by
`sqrt(2)|c_m|q^m/(1-q)` for a compact-dependent `q<1`; computation only
checks the implementation.
