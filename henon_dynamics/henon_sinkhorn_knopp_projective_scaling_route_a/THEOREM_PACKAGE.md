# C191 theorem package

## 1. Frozen dynamics

Let `A` be an `n x n` nonnegative matrix with no zero row or column.  For a
matrix `B`, let `R(B)` divide each row by its row sum and let `C(B)` divide each
column by its column sum.  One clock step is

\[
  \mathcal S(B)=C(R(B)).
\]

The zero pattern is invariant at every finite step.  A **positive diagonal**
is a permutation `pi` with `prod_i a_(i,pi(i))>0`.  The matrix has **support**
if one exists and **total support** if every positive entry belongs to one.
It is **fully indecomposable** if no independent row and column permutations
put a zero `r x (n-r)` rectangle in a corner for `1<=r<n`.

## 2. Boundary-complete scaling theorem

### Theorem 1 (source-locked Sinkhorn--Knopp classification)

For every frozen `A`:

1. `S^k(A)` converges to a doubly stochastic matrix if and only if `A` has
   support.
2. A doubly stochastic limit has the form `D_1 A D_2` with finite positive
   diagonal factors if and only if `A` has total support.
3. The doubly stochastic matrix in a diagonal-equivalence class is unique.
4. When `A` has total support, the factors are unique up to
   `(D_1,D_2) -> (c D_1,c^{-1}D_2)` exactly when `A` is fully
   indecomposable.  In general the total-support pattern splits into fully
   indecomposable blocks and carries one gauge per block.

Items 1--2 are the theorem of Sinkhorn and Knopp in the present clock
convention.  Item 4 is the Brualdi--Parter--Schneider uniqueness boundary.
The limit for support without total support can contain zeros at locations
where `A` was positive; it therefore cannot be represented by finite positive
diagonal factors.

### Proof boundary

The all-matrix statements are classical source theorems.  The executable
enumeration of all declared order-two and order-three zero patterns verifies
the combinatorial predicates and limiting sentinels, but it is not used as an
inductive proof.

## 3. Positive projective dynamics

Assume now that `A>0`.  On positive column rays define

\[
  T_A(x)=\left[A^T\left((Ax)^{-1}\right)\right]^{-1},
\]

where inverses are componentwise.  Diagonal rescaling of `x` describes one
full row/column step.  Hilbert distance

\[
 d_H(x,y)=\log\frac{\max_i x_i/y_i}{\min_i x_i/y_i}
\]

is unchanged by componentwise inversion.  Put

\[
 \Theta(A)=\max_{i,j,k,l}\frac{a_{ik}a_{jl}}{a_{il}a_{jk}},
 \qquad
 \kappa(A)=\frac{\sqrt{\Theta(A)}-1}{\sqrt{\Theta(A)}+1}.
\]

Birkhoff contraction applied to `A` and `A^T` gives

\[
 d_H(T_Ax,T_Ay)\le \kappa(A)^2 d_H(x,y).
\]

Thus the positive scaling ray converges geometrically.  The coefficient is
data-dependent.  As the projective diameter tends to infinity,
`kappa(A)->1`; no dimension-only rate follows.

## 4. Exact local rate

Let `S>0` be the doubly stochastic limit.  Choose logarithmic column-scaling
coordinates `u`, and quotient the gauge line spanned by the all-ones vector.
The full-cycle map is

\[
 F(u)=-\log\left(S^T\exp[-\log(S\exp u)]\right).
\]

Direct differentiation at `u=0` yields

\[
  DF(0)=S^T S.
\]

The gauge eigenvalue is one.  On its orthogonal quotient the spectral radius
is

\[
  \rho_{\rm loc}=\sigma_2(S)^2<1,
\]

the square of the second singular value.  This is a local asymptotic rate,
not a global equality at every iterate.  The exact two- and three-dimensional
oracles reconstruct both the characteristic polynomial and the quotient
rate.

## 5. Recurrence and Route-A stop

Every orbit in the support stratum converges.  Therefore an orbit of the
full-cycle map that is exactly periodic is constant: a nonconstant periodic
sequence cannot also have a single limit.  The resulting fixed point is an
algorithmic normalization target, not a primitive periodic orbit carrying an
arithmetic clock.

Support matchings, cross-ratios and singular values have no intrinsic
rational-prime or prime-power semantics.  There is no natural `log p` clock,
target divisor, target functional equation, Weil compression or source-native
self-adjoint Hilbert-space quantization.  Hence

```text
(A0,A1,A2,A3,A4)=(FAIL,FAIL,FAIL,FAIL,FAIL)
overall ROUTE_A_REJECTED
Route B false
scope NO_BAD_EULER_OR_ROOT_NUMBER
```

No coordinate is borrowed from another candidate.
