# Evidence — `AFC-20260914-PWF01`

Primary source: Fred B. Holt, [*Discrete dynamics of Eratosthenes
sieve*](https://arxiv.org/abs/2608.26384), arXiv:2608.26384 (v2, 2026).
The source states that each stage has a gap cycle of length `phi(p#)` and span
`p#`, and gives the recursion between successive primorial cycles.  The
internal-next-prime reading `p_(k+1)=g_1+1` is preserved from the prior local
[019 control](../../019-primorial-gap-recursion-control/paper.md).

The finite permutation `next_k` is a definition of this package: order the
reduced residue classes cyclically and take the next one.  It validates packet
closure and repetitions only; it does not import a physical time, logarithmic
roof, determinant, or symplectic structure.
