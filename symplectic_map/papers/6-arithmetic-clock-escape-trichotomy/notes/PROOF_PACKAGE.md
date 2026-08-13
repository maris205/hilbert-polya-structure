# Proof Package: Additive Finite Arithmetic Capacity

**Candidate:** `additive_finite_arithmetic_capacity_v2`  
**Status:** `PROVABLE AS STATED`  
**Source lock:** version 2, repaired after the independent pre-execution proof
and novelty audit

## Claim

### Theorem A (additive finite arithmetic-capacity bound)

Let $V\subset\mathbb R$ be a finite-dimensional vector space over
$\mathbb Q$, and let $S_{\mathbb Q}$ be a fixed finite set of rational
primes.  Suppose that every distinct positive rational prime $p$ realized by
a fixed architecture has at least one representation

$$
\log p=v_p+\log q_p+\alpha_p,                           \tag{A.1}
$$

where

$$
v_p\in V,\qquad
q_p\in\overline{\mathbb Q}\cap\mathbb R_{>0},\qquad
q_p^2\text{ is an }S_{\mathbb Q}\text{-unit},\qquad
\alpha_p\in\overline{\mathbb Q}\cap\mathbb R.
$$

All architecture data, coefficients, and allowed operations are fixed
independently of $p$.  Then

$$
\boxed{
\#\mathcal P_{\rm hit}
\leq \dim_{\mathbb Q}V+|S_{\mathbb Q}|.}               \tag{A.2}
$$

## Status

`PROVABLE AS STATED` under the explicit assumptions below.  No weakening is
needed after replacing the version-1 selector theorem by the additive normal
form (A.1).  The selector theorem survives as Corollary B.

## Assumptions

1. $V$ is one fixed finite-dimensional $\mathbb Q$-subspace of $\mathbb R$
   for the whole architecture.
2. $S_{\mathbb Q}$ is one fixed finite set of rational primes for the whole
   architecture.
3. For an algebraic $x\ne0$, ``$S_{\mathbb Q}$-unit'' means that in a number
   field containing $x$, the valuation of $x$ is zero at every finite place
   not above $S_{\mathbb Q}$.  The definition is unchanged after finite field
   extension.
4. Every $q_p$ is a positive real algebraic number.  The certified unit is
   $q_p^2$; $q_p$ itself need not be certified as a unit in the original
   field.
5. Every $\alpha_p$ is real algebraic.
6. Equality is exact.  There is no tolerance, numerical fitting, prime
   relabeling, or target-dependent choice of coefficients or support.
7. Rational, including negative, coefficients on multiplier logarithms are
   allowed.  Algebraic irrational coefficients are not covered.
8. The logarithm is the single-valued real logarithm on
   $\mathbb R_{>0}$.

## Notation

- $\mathcal P_{\rm hit}$ is a set of distinct primes, not a multiset of
  orbit hits.
- $\mathcal P_0=\mathcal P_{\rm hit}\setminus S_{\mathbb Q}$.
- $v_w$ is an additive valuation at a finite place $w$ of a number field.
- A representation is selected once for each distinct prime before any
  finite rational relation is considered.

## Proof strategy

We prove that the selected vectors $\{v_p:p\in\mathcal P_0\}$ are linearly
independent over $\mathbb Q$.  A hypothetical rational relation becomes
$\log R=\beta$ with $R>0$ algebraic and $\beta$ real algebraic.
Hermite--Lindemann forces $\beta=0$ and $R=1$.  Squaring removes the only
possible modulus-square-root issue.  Valuations at the distinct outside
primes then force every relation coefficient to vanish.

## Dependency map

1. Theorem A depends on Lemma 1 (extension-invariant units), Lemma 2
   (rational closure of multiplier logs), Hermite--Lindemann, and the
   outside-prime valuation argument.
2. Lemma 2 depends on positivity, algebraicity of rational powers, the real
   logarithm law, and Lemma 1.
3. The class-M certificate depends on separate-degree homogenization, the
   projective-affine dimension lemma, the nonarchimedean maximum argument,
   determinant one, and a normal extension saturated above
   $S_{\mathbb Q}$.
4. The class-L certificate depends on higher-block recoding and finite
   rational rank.
5. The class-A certificate depends on regular algebraic evaluation and
   distinguishes algebraicity from canonical gauge invariance.
6. Corollary B embeds selector outputs into (A.1); it is not used to prove
   Theorem A.

## Preliminary lemmas

### Lemma 1 (extension invariance of the unit certificate)

Let $E/K$ be a finite extension of number fields and let $x\in K^\times$.
If $v(x)=0$ at every finite place $v$ of $K$ not above
$S_{\mathbb Q}$, then $w(x)=0$ at every finite place $w$ of $E$ not above
$S_{\mathbb Q}$.

**Proof.**  If $w$ lies above $v$, the normalized additive valuations satisfy
$w(x)=e(w/v)v(x)$ up to the common positive normalization convention.  A
place $w$ not above $S_{\mathbb Q}$ lies over a place $v$ not above
$S_{\mathbb Q}$, so $v(x)=0$ and hence $w(x)=0$.  Multiplication and
inversion preserve zero valuations. $\square$

### Lemma 2 (rational closure of multiplier-log terms)

Let $q_1,\ldots,q_t$ be positive real algebraic numbers such that each
$q_j^2$ is an $S_{\mathbb Q}$-unit, and let
$c_1,\ldots,c_t\in\mathbb Q$.  There is a positive real algebraic number
$q$ such that

$$
\sum_{j=1}^t c_j\log q_j=\log q
$$

and $q^2$ is an $S_{\mathbb Q}$-unit.

**Proof.**  Choose $D\ge1$ clearing the denominators and put
$m_j=Dc_j\in\mathbb Z$.  In a finite extension containing the unique
positive real $D$-th root, define

$$
q=\prod_{j=1}^t q_j^{m_j/D}>0.
$$

This number is algebraic.  The real logarithm law gives the asserted sum.
Moreover

$$
(q^2)^D=\prod_{j=1}^t(q_j^2)^{m_j}.
$$

At every finite place outside $S_{\mathbb Q}$, the right side has valuation
zero.  Therefore $D v_w(q^2)=0$, so $v_w(q^2)=0$.  Negative $m_j$ cause no
problem because the unit group is closed under inversion. $\square$

## Proof of Theorem A

**Step 1: select certificates without counting repetitions.**  For each
$p\in\mathcal P_0$, select one representation (A.1).  If several orbits or
several representations realize the same $p$, they still contribute one
element to $\mathcal P_0$.  The proof below works for every such selection.

**Step 2: assume a finite rational relation.**  Take distinct primes
$p_1,\ldots,p_k\in\mathcal P_0$ and suppose

$$
\sum_{i=1}^k c_i v_{p_i}=0,
\qquad c_i\in\mathbb Q.
$$

After clearing denominators there are integers $m_i$, not all zero, such
that

$$
\sum_{i=1}^k m_i v_{p_i}=0.                            \tag{A.3}
$$

**Step 3: reduce the relation to an algebraic exponential identity.**
Rearranging (A.1) and using (A.3) gives

$$
\log R=\beta,                                           \tag{A.4}
$$

where

$$
R=
\frac{\prod_{i=1}^k p_i^{m_i}}
     {\prod_{i=1}^k q_{p_i}^{m_i}}
\in\overline{\mathbb Q}\cap\mathbb R_{>0},
\qquad
\beta=\sum_{i=1}^k m_i\alpha_{p_i}
\in\overline{\mathbb Q}\cap\mathbb R.
$$

Positivity of every factor makes the real-log addition law valid even when
some $m_i$ are negative.

**Step 4: use Hermite--Lindemann.**  If $\beta\ne0$, then
Hermite--Lindemann says that $e^\beta$ is transcendental.  Equation (A.4)
instead gives $e^\beta=R$, which is algebraic.  Hence $\beta=0$.  Since the
real exponential is injective, $R=1$.

**Step 5: square before taking valuations.**  The identity $R=1$ yields

$$
\prod_{i=1}^k p_i^{2m_i}
=\prod_{i=1}^k(q_{p_i}^2)^{m_i}.                        \tag{A.5}
$$

Put the finitely many algebraic numbers in (A.5) into one number field $E$.
Lemma 1 preserves the $S_{\mathbb Q}$-unit property after this extension.

**Step 6: isolate each outside prime.**  Fix $i$ and choose a finite place
$w$ of $E$ above $p_i$.  Since $p_i\notin S_{\mathbb Q}$, every factor on
the right of (A.5) has $w$-valuation zero.  Distinct rational primes generate
coprime ideals, so $v_w(p_j)=0$ for $j\ne i$, while
$v_w(p_i)>0$.  Taking $w$-valuations gives

$$
2m_i v_w(p_i)=0,
$$

and therefore $m_i=0$.  This holds for each $i$, contradicting the assumed
nonzero relation.

**Step 7: count.**  Thus every finite subset of
$\{v_p:p\in\mathcal P_0\}$ is rationally independent.  A vector space of
dimension $r=\dim_{\mathbb Q}V$ contains no linearly independent subset of
size $r+1$, so

$$
|\mathcal P_0|\le r.
$$

At most $|S_{\mathbb Q}|$ distinct rational primes lie in the complementary
part $\mathcal P_{\rm hit}\cap S_{\mathbb Q}$.  This proves (A.2).
$\square$

## Source-class certificates

### Class L: finite memory becomes finite rank

A function depending on $m$ consecutive symbols on a finite-state shift can
be recoded on the finite graph of admissible $(m-1)$-blocks.  Its periodic
sum becomes a sum of finitely many edge values.  Thus all L-readouts in a
finite architecture occupy one finite-dimensional rational space $V$.
This statement does not cover arbitrary point-dependent Hölder roofs.

### Class M: why squared moduli have fixed support

For a finite composition of monic generalized Hénon factors, expand a
periodic orbit into the cyclic recurrence

$$
z_{j+1}+z_{j-1}=p_{i_j}(z_j).
$$

Indices are cyclic and neighbor occurrences retain their multiplicity.  Thus
for a one-step cycle the left side is $2z_0$; no duplicate neighbor is silently
collapsed in periods one or two.

Homogenize the $j$-th equation to its own degree $d_{i_j}$.  On the common
hyperplane at infinity, monicity leaves $z_j^{d_{i_j}}=0$ for every $j$, so
there is no projective solution at infinity.  A positive-dimensional
projective variety cannot be contained in an affine chart: a projective
variety that is also affine has only zero-dimensional complete irreducible
components.  Hence the cyclic solution set is zero-dimensional and its
coordinates are algebraic.

At a finite place of good reduction, let $R>1$ be the maximum norm of the
cyclic coordinates and choose an index attaining it.  The monic leading term
is uniquely dominant, so $|p_{i_j}(z_j)|=R^{d_{i_j}}>R$, whereas the
recurrence gives $|p_{i_j}(z_j)|\le R$, a contradiction.  Every periodic
coordinate is integral outside the fixed bad set.

Derivative factors and their inverses lie in $\mathrm{SL}_2$ of the integral
closure, so both return eigenvalues are units away from the bad places.  Put
the orbit and eigenvalue in one normal extension and saturate the exceptional
set to all places above $S_{\mathbb Q}$.  Complex conjugation preserves its
complement, hence for $q=|\lambda|>0$,

$$
q^2=\lambda\overline\lambda
$$

is an $S_{\mathbb Q}$-unit.  This does not identify
$\overline\lambda$ with $\lambda^{-1}$.

### Class A: algebraicity versus gauge invariance

For algebraic orbit points at which all rational functions are regular, each
potential value and every finite action sum is algebraic.  Algebraic scales,
averages, repetitions, real and imaginary parts, and moduli preserve
algebraicity.  A general algebraic primitive change contributes

$$
\chi_n(P_n)-\chi_0(P_0)+\sum_j C_j.
$$

This remains algebraic without endpoint cancellation.  Endpoint
compatibility is required only to call the closed action canonically gauge
invariant.  Closed non-exact changes, multivalued logarithmic gauges, poles,
transcendental constants, and logarithmic postprocessing lie outside the
certificate.

## Corollary B (selector/union architecture)

Suppose each realized target is supplied by one L-, M-, or A-component.  An L
hit embeds as $(v,q,\alpha)=(\ell_L,1,0)$, an M hit as
$(0,|\lambda|,0)$, and an A hit as $(0,1,\mathcal A)$.  Therefore the same
bound (A.2) applies.  In particular, the version-1 selector theorem is a
corollary of Theorem A.

## Corollary C (necessary certificate escapes)

An exact all-prime construction cannot retain all assumptions of (A.1): it
must lose the common finite-rank $V$, the fixed finite support
$S_{\mathbb Q}$, the real-algebraic action term, or the rational additive
normal form.  This is contraposition inside the declared certificate.  The
failures are neither mutually exclusive nor jointly exhaustive for arbitrary
dynamics, and none is sufficient for arithmetic correspondence.

## Boundary controls

1. A rank-$r$ finite graph can realize $r$ deliberately inserted independent
   target lengths.  This proves abstract sharpness only.
2. For $H_{-15/16}$, the fixed point $(5/4,5/4)$ has characteristic
   polynomial
   $T^2-(5/2)T+1=(T-2)(T-1/2)$; the displayed prime is already in the
   denominator support.
3. On $\mathbb A^2$ with $\theta=p\,dq$, the identity map satisfies
   $F^*\theta-\theta=0=dG$ for the constant $G=\log 2$, and its fixed-point
   action is $\log 2$.  This is a positive-dimensional but forbidden
   transcendental target injection.

## Corrections or missing assumptions

- Version 1 treated only a selector union.  Version 2 makes the additive
  normal form the main claim and explicitly limits multiplier-log
  coefficients to $\mathbb Q$.
- Version 1's point-phase-space action control has been replaced by the
  identity exact map on $\mathbb A^2$.
- No further missing assumption is known after the independent audit.

## Open risks

- Novelty is moderate synthesis/certificate novelty, not component-theorem
  novelty; the manuscript must keep that positioning.
- The class-M algebraicity/finiteness lemma should receive a full conventional
  citation or appendix treatment in the manuscript even though it is explicit
  here.
- The theorem gives exact equality only and has no quantitative stability
  analogue for approximate matching.
