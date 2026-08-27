# Research question

For a finite real hyperplane arrangement `A`, let `F` be its face semigroup,
`C` its chambers, and `w` any probability measure on `F`.  A step sends chamber
`C` to `FC`, where `F` is sampled from `w`.

The mathematical question is whether this entire family admits a single exact
description of:

1. the spectrum and algebraic multiplicities of its transition operator;
2. its characteristic polynomial, finite determinant, and power traces;
3. the precise uniqueness condition and a constructive stationary sampler;
4. a computable total-variation bound; and
5. the full nonseparating stationary-simplex boundary.

The answer is yes by the classical Brown--Diaconis theorem package.  C192 tests
whether this exact operator family advances Route A.  It does not: the operator
has no intrinsic target-prime/zero index, recovers no target arithmetic data,
gives no target functional equation or counting law, and identifies no target
divisor.  Its finite determinant earns only `A4_FORMAL_HINT`.

The finite computation asks a narrower regression question: do independent
sign-vector, lattice/Möbius, exact-matrix, and symbolic-algebra implementations
agree on coordinate and braid fixtures, including separating and nonseparating
cases?  These checks support implementation integrity only.
