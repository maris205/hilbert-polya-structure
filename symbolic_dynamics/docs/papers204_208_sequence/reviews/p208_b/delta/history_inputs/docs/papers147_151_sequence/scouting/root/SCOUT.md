# Root scout: two exact finite dynamical systems

This scout contributes two literal self-maps to the P147--P151 breadth gate.  The
computation is a falsifier for the formulas below, not a proof and not an
ownership certificate.  Both candidates remain `HOLD_EXTERNAL`.

## XPF: codimension-one exterior powers of abelian p-groups

Fix a prime, a rank `r >= 3`, and an exponent ceiling `e`.  Write a group type
as

\[
  \lambda=(\lambda_1\geq\cdots\geq\lambda_r\geq1),\qquad
  G_\lambda=\bigoplus_{i=1}^r C_{p^{\lambda_i}}.
\]

The literal type dynamics induced by `G -> exterior^(r-1) G` is

\[
  W_r(\lambda)=(\lambda_{r-1},\lambda_r,\ldots,\lambda_r).
\]

The classical exterior-power type identity is zero-credit input.  The proposed
dynamical increment is the simultaneous package below.

- `W_r^2(lambda)` is homocyclic and `W_r^3=W_r^2`; every tail is 0, 1, or 2.
- There are `e` fixed types, `binom(e+r-2,r-1)-e` tail-one types, and
  `binom(e+r-2,r)` tail-two types.
- The image has `e(e+1)/2` elements.
- For a target `(b,a,...,a)` with `b >= a`, the one-step fibre has size
  `binom(e-b+r-2,r-2)`; every other target has empty fibre.
- The full basin of the fixed type `(a,...,a)` has size
  `binom(e-a+r-1,r-1)`.

This is a strict strengthening of the internally rejected rank-three
exterior-square reserve: arbitrary rank, exact depth strata, all one-step
fibres, and all terminal basins are now included.  It is nevertheless
owner-heavy, so it may re-enter only if direct subtraction leaves a
paper-sized dynamical theorem rather than a reformulation of the classical
type formula.

## EQC: equal-cardinality coarsening of labelled set partitions

For a set partition `pi` of `[n]`, simultaneously merge all blocks having the
same cardinality.  Denote the resulting labelled partition by `C(pi)`.  This is
a literal self-map of the Bell set, with labels retained throughout.

- A state is fixed exactly when its block sizes are pairwise distinct.
- Every nonfixed step strictly lowers the number of blocks, and the sharp
  universal clock is `tau(pi) <= floor(log_2 n)`.
- Equality is attained for every `n=2^t` by the cascade with block sizes
  `(2^(t-1),2^(t-2),...,2,1,1)`.
- The number of fixed labelled partitions is
  `n! [z^n] prod_(s>=1) (1+z^s/s!)`.

There is also a complete every-target fibre formula.  If the target has
labelled blocks `B_i` of sizes `b_i`, assign pairwise distinct divisors
`s_i | b_i`.  For each assignment, split `B_i` into `b_i/s_i` unlabelled
blocks of common size `s_i`.  Hence

\[
 |C^{-1}(B_1|\cdots|B_k)|=
 \sum_{\substack{s_i\mid b_i\\s_i\text{ pairwise distinct}}}
 \prod_i \frac{b_i!}{(s_i!)^{b_i/s_i}(b_i/s_i)!}.
\]

In particular, positivity of this sum is an exact image test, equivalently a
distinct-representatives condition for the divisor sets of the target block
sizes.  The sharp logarithmic cascade plus the complete divisor-injection
inverse is the proposed increment.

The nearest direct primary-source neighbour currently located is Dougherty and
McCammond's definition of a partition's shape/multiset of block
multiplicities.  That static statistic receives zero credit; the present
candidate still requires a direct search for prior iteration, clocks, and
fibres before selection.

## Exact replay

`verify_root_scout.py` checks XPF for ranks 3--8 and exponent ceilings 1--12,
covering 293,475 group types.  It checks EQC on every labelled partition of
sizes 1--9, including every target fibre, and checks sharp cascades through
`n=512`.  The canonical run records 3,416,699 exact passing assertions.

Status: **XPF conditional re-entry; EQC strong owner-search finalist;
HOLD_EXTERNAL**.
