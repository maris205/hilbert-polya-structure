# C134 narrative report

C129 attached one fifth-root phase to each integer branch translation.  That
phase made the determinant position-sensitive, but only modulo five.  C134
asks whether the kernel can be removed without changing the dynamics or the
global Hardy--Fredholm owner.

The replacement is the full labelled character torus of the integer lattice,
represented exactly by `Q[X,X^(-1)]`.  In the scaled separated family, every
`k>=1` uses the bidisc of radius `3k` and any branch permutation of
`(-2k,0,2k)`.  Scaling preserves the rational contraction and separation
proofs: the exact image radii are `21k/32` and `3k/4`, with gap `11k/16`.

The determinant contains more than qualitative phase sensitivity.  Its first
three normalized logarithmic jets give the first three power traces of the
three-state character matrix.  Newton identities convert them into monomials
with exponents `t0`, `t0+t1`, and `t0+t1+t2`; differences recover the labelled
triple.  The theorem is all-period and uses the original infinite-dimensional
Hardy owner, not a finite surrogate.

The exact anchor `q=(3+4i)/5` has infinite order and lives in Gaussian
rationals.  The `k=1` and `k=6` models are identical under every mod-five
phase, yet `q^(-2)` and `q^(-12)` differ.  This supplies both a negative
finite-quotient control and a positive faithful-character control.

The evidence has 284 rooted words, 40 primitive cycles, twelve permutation
recoveries, Laurent traces and coefficients through order eight, 71
independent checker assertions, 64 SymPy checks, byte replay, and 48 hostile
mutations: 47 with repaired payload hashes plus one stale-hash case.

The claim remains narrow.  Parameter orientation is labelled; exact
injectivity is not finite-precision stability; only integer x-translations in
the frozen `A,B,c` family are recovered.  No target divisor, arithmetic/local
data, Hilbert--Polya operator, or Route-B authorization is asserted.
