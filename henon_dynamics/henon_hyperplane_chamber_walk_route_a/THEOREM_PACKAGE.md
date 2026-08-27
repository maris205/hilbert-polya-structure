# Theorem package

## Domain and product

Let `A` be an arbitrary finite real hyperplane arrangement in `V`, including
affine arrangements.  Encode each face by its signs relative to the
hyperplanes.  The face product is

`(FG)_H = F_H` if `F_H != 0`, and `(FG)_H = G_H` otherwise.

Faces form a left-regular-band semigroup and act on the chambers.  For a
probability measure `w` on the faces, the chamber transition matrix is

`K(C,C') = sum_{F: FC=C'} w(F)`.

## Source-owned all-family theorem

Brown--Diaconis Theorem 1 states that `K` is diagonalizable.  For every flat
`W` in the intersection poset,

`lambda_W = sum_{F subset W} w(F)`,
`m_W = |mu(W,V)|`.

The flat-indexed factorization remains valid when several flats give the same
numeric eigenvalue; their exponents then add.  Therefore, by finite-dimensional
linear algebra,

`chi_K(x) = product_W (x-lambda_W)^{m_W}`,
`det(I-zK) = product_W (1-z lambda_W)^{m_W}`,
`tr(K^ell) = sum_W m_W lambda_W^ell`.

The operator corollaries are deductions from the source theorem, not new
spectral theorems.

## Stationarity and stopping sampler

The measure `w` is separating when, for every hyperplane `H`, at least one
positive-weight face is not contained in `H`.  Brown--Diaconis Theorem 2 says
this is equivalent to unique stationarity.  Under separation, order all
positive-weight faces by weighted sampling without replacement; their product
is a chamber with the stationary law.

Equivalently, sample faces with replacement and stop when the product becomes a
chamber; deleting repeated ineffective factors recovers the without-replacement
law.  Theorem 3 and Section 4 yield the coupling estimate.  C192 calls this a
stationary stopping sampler, not a strict strong stationary time: the source
does not state, and the general model does not supply, independence of the
output from the stopping time.

For every initial chamber and integer `ell >= 0`, Section 4B gives

`||K_C^ell-pi||_TV <= -sum_{W != V} mu(W,V) lambda_W^ell`

and the right side is at most `sum_{H in A} lambda_H^ell`.

## Nonseparating boundary

Let `A0` consist of all hyperplanes containing every positive-weight face.  The
`A0`-chambers index closed communicating components.  Each component has one
stationary law, and every stationary law is a convex combination of these
component laws.  Thus the stationary set is exactly the simplex with one vertex
per `A0`-chamber.  This is stronger and more accurate than merely saying
“stationarity is nonunique.”

## Oriented-matroid ceiling

Brown--Diaconis Section 6 states that Theorems 1 and 2 carry over to the covector
face semigroup of an oriented matroid, including nonrealizable examples.  C192
imports only that stated extension.  It makes no broader realization theorem,
no unrestricted affine-oriented-matroid claim, and no new topological result.

## Regression and nonclaims

The exact program checks eight coordinate/braid fixtures: six separating and
two nonseparating.  This is a regression census, not a proof by enumeration.
Tsetlin, coordinate, and braid examples remain examples of the one theorem.

No claim is made about local factors, Euler factors, root numbers, automorphy,
target zeros, a target functional equation, a target counting law, a
Hilbert--Pólya operator, global novelty, or external review.
