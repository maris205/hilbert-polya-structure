# Derivation package

## 1. Reversible map and exact-period cover

Work with

\[
H_A(x,y)=(A-x^2-y,x),\qquad R(x,y)=(y,x).
\]

Direct substitution gives

\[
R^2=1,\qquad RH_AR=H_A^{-1}.
\]

For fixed \(n\), the universal fixed scheme has generic rank \(2^n\) over the
parameter line.  Remove parameters at which a lower-period branch collides,
the fixed scheme is non-reduced, or the relevant discriminant vanishes.  On
the resulting open set \(U_n\), the exact-period locus
\(\pi_n:\mathcal P_n\to U_n\) is a finite étale cover of degree

\[
\nu(n)=\sum_{d\mid n}\mu(n/d)2^d.
\]

The generator \(H_A\) acts freely on exact-period points and, together with
\(R\), defines a fiberwise \(D_n\)-action.  These statements are made only on
\(U_n\); no global finite-flat exact-period claim is needed at bad parameters
or in characteristics dividing \(n\).

## 2. Orbit counts

The cyclic-orbit count is \(M_n=\nu(n)/n\).  Reversible half-orbit boundary
conditions give the all-period fixed-axis counts

\[
\#(\operatorname{Fix}R\cap\operatorname{Fix}H^n)
=2^{\lfloor(n+1)/2\rfloor},
\]

\[
\#(\operatorname{Fix}(HR)\cap\operatorname{Fix}H^n)
=2^{\lfloor(n+2)/2\rfloor}.
\]

Möbius inversion yields \(A_n,Q_n\) as recorded in the README.  For odd
period, every self-conjugate orbit meets the diagonal and there is no
non-diagonal class.  For even period, an axial orbit contributes two axial
points, and a non-diagonal self-conjugate orbit contributes two points on the
other reversor axes.  Hence

\[
D_n=\begin{cases}A_n,&n\text{ odd},\\A_n/2,&n\text{ even},\end{cases}
\quad
N_n=\begin{cases}0,&n\text{ odd},\\Q_n/2,&n\text{ even}.\end{cases}
\]

The remaining \(C_n=M_n-D_n-N_n\) cyclic orbits occur in reversal pairs.
Therefore the number of coarse dihedral orbits is

\[
D_n+N_n+C_n/2=\frac{M_n+D_n+N_n}{2}.
\]

This derivation reproduces Gallas (2007); it is included to make the audit
executable, not as a new counting theorem.

## 3. Invariant-sector projection

Let

\[
\mathscr V_n=(\pi_n)_*\mathbb Q_\ell,
\]

with \(\ell\nmid 2n\).  Fiberwise, \(\mathscr V_n\) is the vector space of
functions on the finite exact-period set.  Functions on the orbit set
\(\mathcal P_n/D_n\) are precisely the invariant functions, so

\[
(\mathcal P_n/D_n\to U_n)_*\mathbb Q_\ell
\simeq \mathscr V_n^{D_n}.
\]

### Proposition (only the trivial isotypic sector descends)

The chronological generator \(H\) acts identically on
\(\mathscr V_n^{D_n}\).  If a Frobenius operator \(F^r\) commutes with the
\(D_n\)-action, then

\[
\operatorname{Tr}(F^r\mid\mathscr V_n^{D_n})
=\frac1{2n}\sum_{g\in D_n}
\operatorname{Tr}(F^rg\mid\mathscr V_n).
\]

### Proof

Every invariant vector is fixed by every group element, in particular by
\(H\).  Since \(2n\) is invertible in \(\mathbb Q_\ell\), the projector onto
the invariant sector is

\[
P_{\mathrm{inv}}=\frac1{2n}\sum_{g\in D_n}g.
\]

Commutation with \(F^r\) gives

\[
\operatorname{Tr}(F^r\mid\mathscr V_n^{D_n})
=\operatorname{Tr}(F^rP_{\mathrm{inv}}\mid\mathscr V_n),
\]

which is the displayed average. \(\square\)

Thus the quotient retains only a group average of joint traces.  It discards a
marked phase, reversal orientation, all non-trivial dihedral representations,
and the unaveraged joint Frobenius--Hénon data.

For an autonomous scalar dynamical zeta, quotienting a periodic orbit by its
cyclic choice of starting point is standard and legitimate; the external
period label \(n\) is not erased.  The proposition is therefore not a generic
no-go for orbit zeta functions.  It prevents the coarse quotient from being
used as if it still carried a non-trivial chronological generator or the full
equivariant Frobenius--Hénon representation.  In contrast, replacing an
ordered non-autonomous cocycle by a group average would genuinely destroy its
time ordering.

A quotient stack with constant characteristic-zero coefficients does not
recover the omitted isotypic data: averaging kills higher finite-group
cohomology and again selects the invariant sector.  One must explicitly use
non-trivial representation coefficients or retain the equivariant cover
itself if those sectors are part of the proposed mechanism.

## 4. Period-six normalization

The squarefree period-six orbit-marker curve has components \(C_6,D_6,N_6\)
listed in the source audit.

- \(C_6=0\) is the parameter line \(\sigma=2\).
- \(D_6=0\) has \(A=(\sigma^2+4\sigma)/4\), hence rational function field
  \(\mathbb Q(\sigma)\).
- Regard \(N_6\) as \(c_2(\sigma)A^2+c_1(\sigma)A+c_0(\sigma)\).  Exact
  expansion gives
  \[
  \operatorname{Disc}_A(N_6)
  =16(\sigma-6)(\sigma+2)(3\sigma^2-8\sigma-12)^2.
  \]

On the generic locus, set

\[
Y=\frac{2c_2(\sigma)A+c_1(\sigma)}
{4(3\sigma^2-8\sigma-12)}.
\]

The equation \(N_6=0\) becomes

\[
Y^2=(\sigma-6)(\sigma+2).
\]

This conic has the rational parametrization

\[
\sigma=2+2(t+t^{-1}),\qquad Y=2(t-t^{-1}).
\]

Consequently every smooth projective component has genus zero and
\(\dim H^1=0\).  Singular gluing of rational components may create
dual-graph weight-zero cohomology, but not the proposed weight-one curve
spectrum.

## 5. Scope of the obstruction

The proof does not say that all Hénon period-cover cohomology vanishes or that
unmarked autonomous cycle zeta functions are invalid.  It says that the
registered **coarse dihedral quotient** collides with prior work and contains
only trivial-isotypic joint action.  A Route-A revival must define a global
determinant across periods, supply a prime-like clock and target divisor, and,
if non-trivial joint action is claimed, retain the relevant equivariant
coefficient systems.
