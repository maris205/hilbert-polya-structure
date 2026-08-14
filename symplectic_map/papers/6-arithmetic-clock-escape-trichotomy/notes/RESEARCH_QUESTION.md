# Research Question: Finite Arithmetic Capacity under Additive Readouts

**Candidate ID:** `additive_finite_arithmetic_capacity_v2`  
**Safe working title:** *Finite Arithmetic Capacity under Additive Locally
Constant, Good-Reduction Multiplier, and Algebraic-Action Readouts*  
**Design state:** repaired theory source lock; formal candidate execution is
forbidden until independent code review passes  
**Date:** 2026-08-14

## Motivation

The preceding projects isolate three exact periodic-orbit obstructions:

1. finite-memory locally constant lengths occupy one finite-dimensional
   rational space;
2. good-reduction Hénon return-modulus squares are units outside one fixed
   finite rational-prime support; and
3. safely evaluated algebraic actions, including their allowed algebraic
   transforms, remain algebraic.

Treating these as a selector-only union gives a correct but weak bookkeeping
statement.  This project asks the stronger question identified by the
independent proof attack: what remains possible when the three contributions
are genuinely **added** in one fixed readout?

## Exact additive design class

Fix once and for all:

- a finite-dimensional vector space $V\subset\mathbb R$ over $\mathbb Q$;
- a finite set $S_{\mathbb Q}$ of rational primes; and
- all maps, coefficients, rational weights, normalizations, and assembly
  operations independently of the prime later declared as a target.

An in-scope periodic-orbit readout must have the canonical form

$$
L=v+\log q+\alpha,                                      \tag{1}
$$

where

$$
v\in V,\qquad
q\in\overline{\mathbb Q}\cap\mathbb R_{>0},\qquad
q^2\text{ is an }S_{\mathbb Q}\text{-unit},\qquad
\alpha\in\overline{\mathbb Q}\cap\mathbb R.
$$

Here an algebraic number is an $S_{\mathbb Q}$-unit when it has valuation
zero at every finite place away from primes in $S_{\mathbb Q}$, in any number
field containing it after the exceptional places are saturated above
$S_{\mathbb Q}$.  This condition is invariant under finite field extension,
multiplication, and inversion.

### What (1) permits

- finite rational sums, differences, repetitions, and rational scalings of
  locally constant lengths, all of which remain in the same $V$;
- finite rational sums of multiplier-modulus logarithms: after adjoining the
  required positive algebraic roots they combine as $\log q$, and $q^2$
  remains an $S_{\mathbb Q}$-unit;
- finite sums and algebraic scalings of safely evaluated algebraic-action
  terms, which remain real algebraic after taking any declared real-valued
  transform.

Negative powers are admitted because $q>0$ and the unit group is closed under
inversion.  Rational powers are taken as the unique positive real algebraic
roots in a finite extension.  The logarithm is always the real logarithm.

### What (1) excludes

- an algebraic irrational coefficient multiplying a multiplier logarithm;
- an arbitrary nonlinear function or lookup table applied after assembly;
- a target-dependent coefficient, normalization, bad support, or choice of
  architecture;
- a logarithm applied after an algebraic action;
- point-dependent roofs not known to occupy one common finite-rank $V$; and
- approximate equality, tolerance matching, or prime relabeling.

## Primary question and source-locked answer

Let $\mathcal P_{\rm hit}$ be the set of **distinct** positive rational primes
$p$ for which at least one orbit has an in-scope certificate

$$
\log p=v_p+\log q_p+\alpha_p.                           \tag{2}
$$

Can a fixed additive architecture realize infinitely many such targets?

No.  The main theorem proves

$$
\boxed{
\#\mathcal P_{\rm hit}
\leq \dim_{\mathbb Q}V+|S_{\mathbb Q}|.}
$$

For primes outside $S_{\mathbb Q}$, any rational dependence among the chosen
$v_p$ terms would yield an identity $\log R=\beta$ with $R>0$ algebraic and
$\beta$ real algebraic.  Hermite--Lindemann forces $\beta=0$ and $R=1$.
After squaring, valuations at the distinct outside primes force every
coefficient in the relation to vanish.  Thus the $v_p$ terms are rationally
independent, so there are at most $\dim_{\mathbb Q}V$ outside hits; at most
$|S_{\mathbb Q}|$ further primes lie inside the bad support.

The theorem needs no prior finiteness assumption on $\mathcal P_{\rm hit}$:
any $\dim_{\mathbb Q}V+1$ outside primes would already contradict finite
dimension.

## How the three source classes enter

### Class L: locally constant terms

A finite directed graph, or a fixed finite-memory observable after
higher-block recoding, has finitely many edge lengths.  Every periodic sum is
an integer combination of them and hence belongs to the common space $V$.
The edge lengths need not be algebraic.

### Class M: good-reduction multiplier terms

A finite composition of monic generalized Hénon factors over an
$S$-integer ring has algebraic periodic coordinates and monodromy in
$\mathrm{SL}_2$ of the integral closure outside $S$.  After passing to a
normal extension and saturating all places above $S_{\mathbb Q}$, both a
return eigenvalue and its complex conjugate are units away from that support.
For $q=|\lambda|>0$,

$$
q^2=\lambda\overline\lambda
$$

is therefore an $S_{\mathbb Q}$-unit.  No claim is made that $q$ or
$\log q$ is algebraic merely because it is a modulus; algebraicity of $q$ is
part of the canonical certificate and follows here from
$q^2\in\overline{\mathbb Q}_{>0}$.

### Class A: algebraic-action terms

Regular evaluation of a $\overline{\mathbb Q}$-rational exact potential on
an algebraic periodic orbit produces an algebraic action.  Algebraic sums,
scales, averages, repetitions, real parts, imaginary parts, and moduli remain
algebraic.  Algebraic endpoint and gauge shifts preserve algebraicity even
when they do not cancel; endpoint compatibility is needed for canonical
gauge invariance, not for the arithmetic conclusion.

## Selector/union corollary

The earlier selector architecture is a special case of (1):

- an L hit uses $(v,q,\alpha)=(\ell_L,1,0)$;
- an M hit uses $(v,q,\alpha)=(0,|\lambda|,0)$; and
- an A hit uses $(v,q,\alpha)=(0,1,\mathcal A)$.

Hence the same numerical bound holds when one component supplies the whole
target.  This selector statement is a corollary, not the paper's principal
result.

## Certified escape map

An exact all-prime construction cannot keep all hypotheses of the canonical
certificate.  It must lose at least one of the following applicable
conditions:

1. a common finite-rank locally constant space $V$;
2. a fixed finite bad-prime support $S_{\mathbb Q}$ for the squared modulus;
3. algebraic and target-independent action evaluation/normalization; or
4. the rational additive normal form (1).

These are necessary failures of the declared certificate only.  They are not
mutually exclusive, not exhaustive across all dynamics, and not sufficient
for arithmetic correspondence.  A fourth observable class is permitted only
after a new source lock and its own provenance theorem.

## Boundary controls

- The rank bound is abstractly sharp: inserting $r$ chosen independent target
  lengths into $r$ loops realizes $r$ targets.  This is target injection, not
  arithmetic emergence.
- For $H_a(X,Y)=(X^2-a-Y,X)$ with $a=-15/16$, the fixed point
  $(5/4,5/4)$ has return eigenvalues $2$ and $1/2$.  The only displayed prime
  already occurs in the coefficient denominator support.
- On $\mathbb A^2$ with its standard exact symplectic form, the identity map
  and constant potential $G=\log 2$ give a fixed-point action $\log 2$.
  This deliberately violates algebraic normalization and demonstrates target
  injection in a conventional positive-dimensional phase space.
- Deninger and Connes--Consani arithmetic/adelic constructions with
  prime-labelled lengths lie outside the declared finite certificate and are
  positive boundary architectures, not support for a universal obstruction.

## Explicit nonclaims

This project does not prove a universal no-go theorem for smooth or
finite-dimensional symplectic dynamics, a complete escape trichotomy, a
classification of irrational multiplier moduli, finite rational rank for
general Hölder roofs, sufficiency of any escape gate, or any Riemann-zero,
determinant, quantization, or Route-B statement.  It makes no historical-first
claim.  Its defensible contribution is a scoped mixed-class capacity
certificate and an auditable assumption ledger.
