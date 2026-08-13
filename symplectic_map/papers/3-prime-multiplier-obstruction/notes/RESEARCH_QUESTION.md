# Research Question: Prime Multipliers in the Frozen PCF Quadratic

**Candidate ID:** `pcf_quadratic_prime_multiplier_obstruction_v1`  
**Design state:** source-locked; no candidate experiment has been executed  
**Date:** 2026-08-13

## Exact object

Let

$$
P(U)=U^3-2U^2+2U-2
$$

and let $u$ be its unique real root.  The inherited quadratic map is

$$
f_u(x)=1-u x^2.
$$

The linear change of coordinate $\phi(x)=-ux$ conjugates it to the monic
quadratic

$$
g(z)=z^2-u,
\qquad
\phi\circ f_u=g\circ\phi.
$$

Because $P$ is monic, $u$ is an algebraic integer.  Period and multiplier are
unchanged by the conjugacy.

## Primary question

Can any finite periodic orbit of $f_u$ (equivalently, of $g$) have a **raw
rational-prime multiplier**,

$$
\lambda=(g^{\circ n})'(z)\in\mathbb Q,
\qquad |\lambda|=p,
$$

where $n$ is the exact period and $p$ is a positive rational prime?

## Frozen answer to prove and audit

No.  More generally, if $F\in\mathcal O_K[X]$ is monic and
$F'=mH$ with $m\ge 2$ an integer and $H\in\mathcal O_K[X]$, then every
rational multiplier at a finite point fixed by $F^{\circ n}$ lies in
$m^n\mathbb Z$.  For $g(z)=z^2-u$, this gives

$$
\lambda\in\mathbb Q \Longrightarrow \lambda\in 2^n\mathbb Z.
$$

For $n\ge2$ this excludes $|\lambda|=p$ immediately.  For $n=1$, the only
remaining possibility is $|\lambda|=2$; the fixed-point equation excludes
both multipliers $2$ and $-2$ because they would force $u=0$ or $u=2$.

The proof is exact and all-period.  Low-period calculations are therefore
audits of the algebra and implementation, not empirical evidence from which
the theorem is inferred.

## Separate target that remains open

The **exponent-prime** target is different:

$$
\lambda\in\mathbb Q,
\qquad |\lambda|=p^n.
$$

The divisibility theorem excludes every odd $p$.  It does **not** exclude
$p=2$, since $2^n\in2^n\mathbb Z$.  The $p=2$ exponent-prime case for
periods $n\ge2$ remains open at source lock.  Also, for complex periodic
orbits, the weaker condition $|\lambda|=p^n$ without assuming
$\lambda\in\mathbb Q$ is outside the arithmetic theorem.

## Symplectic relevance and its strict boundary

On either real branch $q>0$ or $q<0$, the regular cotangent lift

$$
\widehat g(q,p)=\left(g(q),\frac{p}{g'(q)}\right)
                 =\left(q^2-u,\frac{p}{2q}\right)
$$

satisfies $\widehat g^*(P\,dQ)=p\,dq$.  Along the zero section over a
regular period-$n$ orbit, its linearized return has reciprocal eigenvalues
$\lambda$ and $\lambda^{-1}$.  This is only a classical bridge from the
one-dimensional derivative clock to a branchwise exact-symplectic local
map.  It is undefined at $q=0$, two-to-one globally, noncompact, and not a
global symplectomorphism.  No novelty is claimed for this lift.

## Decision value

This candidate is the first nonlinear derivative-clock follow-up to the
finite-memory obstruction.  It escapes finite-rank locally constant clocks,
but the arithmetic integrality of its derivative imposes a stronger exact
obstruction to raw rational-prime multipliers.  A successful audit therefore
closes this particular nonlinear carrier rather than opening a prime/zero
matching stage.

