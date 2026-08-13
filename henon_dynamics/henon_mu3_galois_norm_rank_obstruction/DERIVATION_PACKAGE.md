# HCS-C45 derivation package

## The descent trilemma

C44 forces any source-native paired Hénon coefficient field to grow like the
maximal real cyclotomic field.  Three canonical responses remain:

1. additive Galois trace;
2. multiplicative Galois norm;
3. normalized logarithmic norm.

The first collapses the first moment to \(-6\).  The second restores rational
local factors but forces virtual degree \(2(p-1)\).  The third preserves the
average chronological trace and produces a new analytic half-plane.

## Ordinary norm

The paired determinant \(E_p=D_{p,\psi}^{\rm aug}D_{p,\bar\psi}^{\rm aug}\)
has coefficients in \(L_p=\mathbf Q(\zeta_p)^+\) and virtual degree four.
Taking the norm over all \(d_p=(p-1)/2\) embeddings gives a rational function
of virtual degree \(4d_p=2(p-1)\).  This cannot be cured by a rational
prefactor of uniformly bounded degree.  Rational descent therefore succeeds
only by turning a bounded virtual augmentation into a growing-rank object.

## Normalized norm

On \(|z|<1\), the local unitary sector determinants are zero-free, so their
origin-normalized logarithms are unambiguous.  Divide the norm logarithm by
the field degree:

\[
\log G_p(z)=\frac1{d_p}\operatorname{Tr}_{L_p/\mathbf Q}\log E_p(z).
\]

At first order, C44 gives
\(c_{p,1}=-12/(p-1)\), an extra factor \(p^{-1}\) over the naive prime
sum.  At orders \(n\ge2\), the smooth-cubic Deligne bound gives a uniform
exponential bound \(4\cdot4^n\).  Consequently the first-order prime series
converges for \(\Re s>0\), while the higher-order series converge together
for \(2\Re s>1\).  Their intersection is exactly \(\Re s>1/2\).

This is a structural gain: the Galois average removes the first-order trace
field obstruction strongly enough for the canonical Euler germ to reach the
Riemann critical abscissa from the right.  Here the canonical clock is
\(z=p^{-s}\), whose unit-circle local divisors lie on \(\Re s=0\).  If one
instead uses the optional divisor display \(z=p^{1/2-s}\), the current
higher-order bound proves convergence only on \(\Re s>1\).  These two
coordinate statements must not be conflated.

## Why this is not yet a Fredholm determinant

The logarithmic average assigns divisor multiplicity \(1/d_p\) to each
Galois-conjugate local channel.  Such dimensions are natural for normalized or
semifinite traces, but not for an ordinary finite-dimensional determinant.
An ordinary rational root exists only if every divisor multiplicity of the
norm is divisible by \(d_p\).  C46 tests this exact perfect-power and local
branch condition at the first split prime.

## Falsification boundary

No claim is made that \(\Re s=1/2\) is a natural boundary.  No zero or pole of
\(\zeta\) is used.  The theorem supplies a half-plane germ and a precise
operator-category question; it does not provide analytic continuation or the
Riemann functional equation.
