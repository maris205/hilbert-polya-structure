# Research Question: Rational-Modulus Prime Support of Periodic Hénon Multipliers

**Candidate ID:** `integral_area_henon_multiplier_support_v1`  
**Design state:** source-lock v2; no candidate experiment has been executed  
**Date:** 2026-08-13

## Exact frozen map

Let

$$
P(U)=U^3-2U^2+2U-2
$$

and let $u$ be its unique real root in
$$(3859/2500,15437/10000).$$
The parameter is inherited from Papers 1--2 and is an algebraic integer because
$P$ is monic.  The new candidate is the globally polynomial, area-preserving
Hénon automorphism

$$
H_u(X,Y)=(X^2-u-Y,X),
\qquad
H_u^{-1}(X,Y)=(Y,Y^2-u-X).
$$

Its derivative is

$$
DH_u(X,Y)=
\begin{pmatrix}2X&-1\\1&0\end{pmatrix},
\qquad \det DH_u=1.
$$

Thus this is a genuine global polynomial symplectic map of the affine plane,
not the singular branchwise cotangent construction used only as a bridge in
Paper 2.

## Primary question

Can a finite complex periodic orbit of $H_u$ have a multiplier of **exact
rational-prime modulus**,

$$
|\lambda|=p,
$$

where $p$ is a positive rational prime and $\lambda$ is an eigenvalue of the
periodic return derivative in the fixed embedding into $\mathbb C$?  No
rationality assumption is made on $\lambda$ itself.

## Frozen answer to prove and audit

No.  The intended proof has three arithmetic layers.

1. Homogenizing the finite cyclic recurrence shows first that every complex
   periodic coordinate is algebraic.  At every non-archimedean place, the
   recurrence

   $$
   x_{j+1}+x_{j-1}=x_j^2-u
   $$

   and the ultrametric maximum principle force every coordinate of every
   periodic point to be integral.  This is an all-period statement, not a
   conclusion inferred from a finite orbit search.
2. The entries of the periodic monodromy are consequently algebraic
   integers.  Its determinant is one, so its characteristic polynomial is
   $T^2-tT+1$ with algebraic-integer trace $t$.  Each multiplier and its
   reciprocal are algebraic integers: they are algebraic units.
3. Complex conjugation preserves algebraic units.  Hence

   $$
   |\lambda|^2=\lambda\overline\lambda
   $$

   is an algebraic unit.  If $|\lambda|=q\in\mathbb Q_{>0}$, then $q^2$ is
   a rational algebraic unit, so $q=1$.

Therefore no multiplier of $H_u$ has rational modulus other than $1$.  In
particular, no rational prime $p>1$ occurs as an exact multiplier modulus.
More strongly, no positive rational integer greater than one, nor any
positive rational number other than one, occurs as an exact modulus.
The former statement that a rational multiplier can only be $+1$ or $-1$
remains a strict special case.

## Publishable-strength extension and its boundary

For a finite composition of monic area-preserving generalized Hénon factors

$$
H_i(X,Y)=(p_i(X)-Y,X),
\qquad p_i\in\mathcal O_{K,S}[X]\ \text{monic},
$$

the same argument at every finite place outside $S$ shows:

- periodic coordinates are integral outside $S$;
- periodic monodromies lie in
  $\mathrm{SL}_2$ of the integral closure of $\mathcal O_{K,S}$;
- both multipliers are $S$-units;
- if a multiplier has exact rational modulus $q$, every rational prime in
  the numerator or denominator of $q$ lies in the rational prime support of
  $S$.

For the conjugation step, pass to a finite Galois extension $M/\mathbb Q$
containing the orbit and multipliers and enlarge the places to all places of
$M$ above the rational primes $S_{\mathbb Q}$.  This larger set is stable
under complex conjugation and has exactly the same rational-prime support.
Thus both $\lambda$ and $\overline\lambda$ are units outside it.  No
unstated conjugation-stability assumption on the original pair $(K,S)$ is
needed.

This **rational-modulus prime-support certificate** is the strongest safe
statement.  The elementary unit argument is not presented as a new general
theory of Hénon
maps; its contribution is a concrete all-period design filter for exact
rational-modulus clocks in a nonlinear polynomial symplectic family.

## Sharp control and necessity of good reduction

For the same convention $H_a(X,Y)=(X^2-a-Y,X)$, the rational parameter

$$
a=-\frac{15}{16}
$$

has the fixed point $(5/4,5/4)$.  Its return derivative has trace $5/2$ and
characteristic polynomial

$$
T^2-\frac52T+1=(T-2)(T-1/2).
$$

Thus the multipliers are exactly $2$ and $1/2$.  The denominator of $a$ is
supported at $2$, exactly as the $S$-unit theorem permits.  This control shows
that area preservation alone does not exclude rational-prime modulus and
that the coefficient-integrality/good-reduction hypothesis is essential.

## Explicit scope boundary

The theorem now includes the exact rationality of $|\lambda|$: if that
modulus is rational, its prime support is certified.  In the determinant-one
two-dimensional setting, the same is true of an exactly rational spectral
radius, because the spectral radius is the larger multiplier modulus.  It
does not give

- a size bound or an obstruction to instability when $|\lambda|$ is
  irrational;
- a classification of nonrational algebraic moduli or spectral radii;
- singular values or Lyapunov exponents;
- approximate, near-rational, or near-prime multipliers;
- primes appearing in reductions modulo finite places;
- prime orbit labels, Riemann zeros, zeta fitting, or quantization.

In particular, a real saddle can have an algebraic-unit unstable multiplier
of irrational absolute value greater than one.  For a nonreal algebraic
multiplier, $|\lambda|$ is algebraic because
$|\lambda|^2=\lambda\overline\lambda$, but it need not be rational; only the
exact rational case is controlled here.

## Decision value

The candidate advances the sequence from Paper 2's singular branchwise lift
to a global nonlinear symplectic polynomial automorphism.  If the exact proof
and controls pass, the conclusion is nevertheless another obstruction:
good-reduction Hénon maps cannot implement an exact rational-prime-modulus
clock unless the desired primes have already been placed in the finite bad
prime set.  This remains true even when the eigenvalue itself is nonrational.
That closes this design class without opening any target-data stage.
