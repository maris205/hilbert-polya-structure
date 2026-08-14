# Research Question: Algebraic Periodic Actions versus Prime Logarithms

**Candidate ID:** `algebraic_exact_action_clock_obstruction_v1`  
**Design state:** source-locked; no candidate experiment has been executed  
**Date:** 2026-08-13

## Exact object

Let $X$ be an algebraic symplectic phase space over
$\overline{\mathbb Q}$, let $\theta$ be a single-valued algebraic Liouville
primitive on the domain under consideration, and let $F$ be an algebraic
exact-symplectic map.  The exactness data are frozen as an algebraic
potential $G$ satisfying

$$
F^*\theta-\theta=dG.
$$

For an algebraic period-$n$ point $P$, construct each iterate
$P_{j+1}=F_j(P_j)$ only after checking that $F_j$ is defined at $P_j$.
Before evaluation, check each potential, gauge, endpoint, and transition
separately for poles at the required point.  Then define the closed discrete
action

$$
\mathcal A_G(P)=\sum_{j=0}^{n-1}G(F^jP).
$$

The additive constant in $G$ is part of the candidate definition.  It must
be fixed before any orbit is evaluated and must be algebraic.  A change of
Liouville primitive is admitted only through a single-valued
$\overline{\mathbb Q}$-rational gauge
$\theta\mapsto\theta+d\chi$, with all orbit points avoiding the poles of
$\chi$.  If local charts or a time-dependent presentation use separate
one-step constants $C_j$, every $C_j$ must likewise be frozen and algebraic.

## Primary research question

Can such a normalized algebraic closed-orbit action intrinsically realize the
prime clock required by the arithmetic trace-formula analogy,

$$
\mathcal A_G(P)=\log p,
$$

for any positive rational prime $p$?

## Frozen answer to prove and audit

No.  Every summand is the value of an algebraic rational function at an
algebraic point, so

$$
\mathcal A_G(P)\in\overline{\mathbb Q}.
$$

Hermite--Lindemann says that $e^\alpha$ is transcendental for every nonzero
algebraic $\alpha$.  Consequently every complex logarithm of an algebraic
number $\beta\in\overline{\mathbb Q}^{\times}\setminus\{1\}$ is
transcendental; the only algebraic exception to $e^A=\beta$ is
$A=0,\beta=1$, and $\beta=0$ has no complex logarithm.  In particular, no branch of
$\log p$ can equal $\mathcal A_G(P)$.  The same exclusion holds for

- a nonzero algebraic multiple $c\log p$;
- the average action $\mathcal A_G(P)/n$;
- any repetition value $r\mathcal A_G(P)$ versus
  $\log(p^r)=r\log p$;
- $\operatorname{Re}\mathcal A_G(P)$,
  $\operatorname{Im}\mathcal A_G(P)$, or
  $|\mathcal A_G(P)|$ versus the real number $\log p$;
- an equality $e^{\mathcal A_G(P)}=p$.

This is an all-period arithmetic statement.  It is not inferred from a
finite periodic-orbit ledger.

## Gauge and normalization boundary

For an algebraic gauge $\chi$ and a constant $C$, the compatible potential
is

$$
G'=G+\chi\circ F-\chi+C.
$$

On a period-$n$ orbit,

$$
\mathcal A_{G'}(P)=\mathcal A_G(P)+nC.
$$

For local or time-dependent representatives

$$
G'_j=G_j+\chi_{j+1}\circ F_j-\chi_j+C_j,
$$

the same cyclic calculation gives the general shift

$$
\chi_n(P_n)-\chi_0(P_0)+\sum_jC_j.
$$

Compatibility of endpoint gauges deletes only the endpoint mismatch.  Thus:

1. the exact gauge term telescopes and does not change the closed action;
2. the additive constant changes the numerical action and prevents an
   unnormalized action from being intrinsic;
3. if $C$ is algebraic, the new action remains algebraic and the
   prime-logarithm exclusion survives;
4. an incompatible but algebraic, pole-free endpoint mismatch preserves
   algebraicity, although the shorter $\sum_jC_j$ formula is invalid;
5. if transcendental constants or endpoint contributions are allowed, the claim is false: for the
   identity map one may take the constant potential $G=\log 2$ and obtain a
   fixed-point action $\log 2$.

The corresponding statements for compatible step gauges replace $nC$ by
$\sum_jC_j$.  Multivalued monodromy and unfrozen branch jumps lie outside
this algebraic-gauge rule.

The theorem is therefore a certificate for **algebraically normalized**
actions, not for arbitrary analytic representatives of an exactness class.

## Hénon specialization

For

$$
H_a(q,p)=(Q,P)=(q^2-a-p,q),
\qquad a\in\overline{\mathbb Q},
$$

take $\theta=p\,dq$.  Direct differentiation gives

$$
H_a^*\theta-\theta
=(2q^2-p)\,dq-q\,dp
=d\left(\frac23q^3-pq\right).
$$

The zero-constant algebraic potential and the corresponding type-1
generating function are therefore

$$
G(q,p)=\frac23q^3-pq,
\qquad
L_a(q,Q)=\frac13q^3-aq-qQ,
$$

with

$$
p=\partial_qL_a,
\qquad
P=-\partial_QL_a,
\qquad
L_a(q,Q)=-G(q,p)
$$

on the graph of $H_a$.  Every finite periodic orbit of $H_a$ is algebraic
when $a$ is algebraic.  If its cyclic coordinates satisfy

$$
q_{j+1}+q_{j-1}=q_j^2-a,
$$

Here the two neighbor slots retain multiplicity: $n=1$ gives
$2q_0=q_0^2-a$, while $n=2$ gives
$2q_1=q_0^2-a$ and $2q_0=q_1^2-a$.

With this convention,

$$
\mathcal A_G
=\sum_{j=0}^{n-1}
 \left(\frac23q_j^3-q_{j-1}q_j\right)
\in\overline{\mathbb Q},
$$

and the type-1 action $\sum_jL_a(q_j,q_{j+1})$ is its negative.  Hence
neither sign convention can equal $\log p$.

The inherited candidate $a=u$, where

$$
u^3-2u^2+2u-2=0,
$$

is a frozen special case; the conclusion does not use any multiplier,
prime, or zero data.

## $S$-integral refinement

If $a\in\mathcal O_{K_0,S_0}$, adjoin all periodic coordinates to an orbit
field $K/K_0$ and extend $S_0$ to the places $S$ of $K$ above it.  The
non-archimedean maximum argument from the preceding Hénon project gives
$S$-integral periodic coordinates.  Therefore

$$
3\mathcal A_G
=\sum_j\left(2q_j^3-3q_{j-1}q_j\right)
$$

is integral over $\mathcal O_{K,S}$, while $\mathcal A_G$ is integral away
from $S$ and the places above $3$.  This strengthens the arithmetic
provenance statement but is not needed for the Hermite--Lindemann
obstruction.  For merely algebraic $a$, algebraicity still holds even when
integrality does not.

## Scope boundary

The source-locked theorem does **not** exclude:

- return times that are not algebraic evaluations of the frozen potential;
- multiplier clocks such as $\log|\lambda|$;
- a logarithm applied after the action, for example $\log|\mathcal A_G|$;
  in particular, $|\mathcal A_G|\ne\log p$ does not imply a claim about
  $\log|\mathcal A_G|$;
- an action that itself equals a rational prime or another algebraic number;
- derivatives with respect to an energy or parameter, unless their
  algebraicity is proved separately;
- transcendental parameters, transcendental unit conversions, or
  transcendental normalizing constants;
- multivalued logarithmic generating functions, branch monodromy, or
  non-exact changes of Liouville primitive;
- an orbit meeting a pole or an indeterminacy;
- approximate or asymptotic relations to $\log p$;
- a prime-orbit correspondence, a dynamical determinant, a quantization, or
  a Riemann-zero comparison.

In particular, this result closes only the proposal
"use a normalized algebraic periodic action itself as the exact prime
logarithm clock."  It is not a no-go theorem for all symplectic clocks.

## FINER assessment

| Criterion | Score | Reason |
|---|---:|---|
| Feasible | 5/5 | The core proof is exact and reduces to algebraic evaluation plus Hermite--Lindemann. |
| Interesting | 4/5 | It directly tests the roadmap's action-clock route and exposes a normalization trap. |
| Novel | 2/5 | Each ingredient is standard; only the candidate-specific design-certificate packaging appears unrecorded. |
| Ethical | 5/5 | No human data, target table, or dual-use issue is present. |
| Relevant | 4/5 | It removes one natural-looking arithmetic clock before expensive orbit or quantization work. |
| **Average** | **4.0/5** | Proceed only with narrow positioning. |

## Decision value

This candidate follows the multiplier obstructions by testing a genuinely
different symplectic observable: the periodic generating-function action.
The outcome is again negative, but for a new reason.  Algebraic state and
algebraic exactness data can generate rich algebraic action spectra, yet an
exact prime logarithm requires a transcendental ingredient somewhere in the
clock.  The useful conclusion is a provenance requirement, not a new theory
of action spectra.
