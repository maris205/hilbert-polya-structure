# HCS-C48 derivation package

## Chronology to geometry

The ordered four-step phase is retained verbatim.  Splitting it into its
homogeneous cubic and quadratic pieces is a projective-direction
stratification, not a change of dynamics.  On each direction, the radial
equation has one ordinary nonzero solution, no nonzero solution, or all
(p-1) nonzero solutions according to the vanishing of the two homogeneous
pieces.  This gives

\[
Z=1+\#\mathbf P^3-\#S-\#R+p\#(S\cap R).
\]

The split quadric parametrization converts the intersection into the explicit
\((3,3)\) equation in the theorem package.  The derivative argument separates
the cases \(rs\ne0\), \(r=0\), and \(s=0\), proving smoothness uniformly in all
allowed characteristics.

More precisely, the construction is defined over
\(\mathbf Z[\rho,1/6]/(\rho^2+\rho+1)\).  The only denominator in the
quadric coordinates is \(\rho-1\), whose norm is three.  On the four standard
affine charts of \(\mathbf P^1\times\mathbf P^1\), the singularity equations
have no solution in any characteristic other than two and three.  Thus the
finite controls do not stand in for an all-prime Jacobian argument.

## Frobenius normalization

The convention inherited from C45 is

\[
C_{p,2}=2Z/p-2p^2,\qquad c_{p,2}=2C_{p,2}/(p-1).
\]

The Tate pieces in the cubic surface, split quadric, and ambient projective
space cancel exactly, leaving

\[
C_{p,2}=-14-2a_p(X).
\]

This identity explains why finite controls are irregular but only of size
(O(\sqrt p)\) before field-degree normalization.

## Analytic consequence

The logarithm of the normalized product is

\[
-\sum_p\sum_{n\ge1}c_{p,n}p^{-ns}/n.
\]

The \(n=1\) series converges for \(\Re s>0\); the genus-four estimate makes the
\(n=2\) series converge for \(\Re s>1/4\); and the generic \(n\ge3\) majorant
converges for \(\Re s>1/3\).  The first active wall is therefore \(n=3\).

The same decomposition yields the exact sixth-order determinant formula in
the normalized semifinite category: the \(L^6(\mathcal M,\tau)\) tail starts
at \(n=6\), while the first five chronological moments remain explicit
counterterms.  No coefficient has been fitted or rounded.

For completeness, local normal convergence uses two majorants.  On a compact
set with \(\Re s\ge\sigma_0>1/3\), the bound
\(|c_{p,n}|\le4\cdot4^n\) sums the \(n\ge3\) tail after all sufficiently large
primes are chosen so that \(4p^{-\sigma_0}\le1/2\).  The remaining finite set
of primes is handled by the unitary-block estimate
\(|c_{p,n}|\le\tau_p(I)\) and \(p^{-\sigma_0}<1\).  This finite-prime split is
essential to the stated proof, even though it does not change the abscissa.

## Two trace categories

The inherited positive trace is the field-degree-normalized semifinite trace.
For \(\sigma=\Re s\),

\[
\tau(|X_s|^q)
=\sum_{p\equiv1(3)}\frac{8p+4}{3}p^{-q\sigma},
\qquad
X_s\in L^q(\mathcal M,\tau)\iff q\sigma>2.
\]

Thus \(X_s\) is \(\tau\)-trace class exactly for \(\sigma>2\); only there
does the unregularized \(\tau\)-associated analytic graded determinant exist.
The sixth-order determinant on \(\sigma>1/3\) is a regularized
\(\tau\)-determinant with the first five moments disclosed.

The same block matrices act on the ordinary Hilbert direct sum, but its trace
does not contain the factor \(d_p^{-1}\).  Since

\[
\dim\mathcal H_p
=d_p\tau_p(I)
=\frac{(p-1)(4p+2)}3,
\]

one has

\[
\operatorname{Tr}_{\mathcal H}(|X_s|^q)
=\sum_{p\equiv1(3)}\frac{(p-1)(4p+2)}3p^{-q\sigma},
\qquad
X_s\in S^q(\mathcal H)\iff q\sigma>3.
\]

Consequently classical Hilbert trace class begins only at \(\sigma>3\).
Moreover

\[
\operatorname{Str}_{\mathcal H_p}(W_p^n)
=d_pc_{p,n}=C_{p,n},
\qquad
\exp\operatorname{Str}_{\mathcal H_p}\Log_0(I-zW_p)
=G_p(z)^{d_p}=N_p(z).
\]

The classical determinant therefore realizes the ordinary Galois norm, not
the normalized local root studied here.

## Reproducible controls

The checker must independently reconstruct:

1. split-prime and order-three-element conventions;
2. the four-variable chronological zero count;
3. the projective curve count from the explicit \((3,3)\) polynomial;
4. \(C_{p,2}=-14-2a_p\);
5. the Hasse--Weil bound;
6. the prime-series thresholds (0,1/4,1/3);
7. the normalized semifinite \(L^6(\mathcal M,\tau)\), unregularized
   \(\tau\)-trace-class, and classical \(S^q(\mathcal H)\) thresholds;
8. Route-A and scope fields with strict JSON types.
