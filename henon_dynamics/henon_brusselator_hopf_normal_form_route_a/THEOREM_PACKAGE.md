# Brusselator complete local Hopf theorem

For `A>0`, `B>=0`, the nonnegative quadrant is forward invariant and every
solution is global because `(x+y)'=A-x<=A`.  Its unique nonnegative
equilibrium is `(A,B/A)`.

Writing `tau=B-1-A^2`, the equilibrium Jacobian has trace `tau` and
determinant `A^2`.  Thus the exact sequence as `B` increases is:

- stable node for `B<(A-1)^2` (within `B>=0`);
- defective stable node at `B=(A-1)^2`;
- stable focus until `B=1+A^2`;
- Hopf at `B=1+A^2`, with frequency `A`;
- unstable focus until `B=(A+1)^2`;
- defective unstable node there; and
- unstable node above it.

At Hopf, fix

`q=(1,-1+i/A)` and `p=((1+iA)/2,iA/2)`, so `<p,q>=1`.  The standard
multilinear formula gives

\[
G_{21}=-\left(1+\frac2{A^2}\right)
-i\frac{4A^4-7A^2+4}{3A^3},\qquad
\ell_1=\frac{\Re G_{21}}{2A}
=-\frac{A^2+2}{2A^3}<0.
\]

Hence the Hopf is transverse and supercritical.  For
`mu=B-(1+A^2)>0`, the unique small local periodic branch is stable and, in
the declared complex coordinate,

\[
r^2=\frac{A^2}{A^2+2}\mu+O(\mu^2).
\]

The first harmonic of `x-A` has amplitude
`2A sqrt(mu/(A^2+2))`, and the angular frequency is

\[
A-\frac{4A^4-7A^2+4}{6A(A^2+2)}\mu+O(\mu^2).
\]

The exact Route-A tuple is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A is rejected and Route B
is locked.
