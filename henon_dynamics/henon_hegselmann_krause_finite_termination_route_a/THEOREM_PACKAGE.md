# One-dimensional HK finite-termination theorem

Let

\[
x_i(t+1)=\frac1{|N_i(t)|}\sum_{j\in N_i(t)}x_j(t),\qquad
N_i(t)=\{j:|x_j(t)-x_i(t)|\le\varepsilon\},
\]

with `epsilon>0` and ordered initial opinions.

## Theorem

- Order, coincident-agent blocks, and the global convex hull are preserved.
- Any consecutive gap greater than `epsilon` persists and splits the system
  into independent subsystems.
- The system reaches an exact fixed configuration in at most
  `4 n^3 + 2 n + 2` synchronous updates.
- Fixed configurations are exactly equal-position clusters whose distinct
  positions are separated by gaps strictly greater than `epsilon`.
- On every open cell with fixed strict neighbor relations, the update is
  `x -> A_G x`, where row `i` is uniform on `N_i`; `A_G` is row-stochastic
  and rational, but need not be doubly stochastic.
- Translation and common positive scaling of opinions and radius are
  covariant.  The arithmetic mean is not generally invariant: for
  `epsilon=1`, `(0,1/2,7/5)` maps to `(1/4,19/30,19/20)`, changing the mean
  from `19/30` to `11/18`.

The time proof uses the leftmost nonfrozen block.  Within two updates it
gains multiplicity, freezes, or moves right by at least
`epsilon/(2n^2)`.  Permanent-gap decomposition and convex-hull width then
give the displayed cubic bound.

The exact Route-A tuple is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`;
finite termination leaves no nontrivial primitive cycles.
