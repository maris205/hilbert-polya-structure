# Proof Package

## Claim

### Theorem A (algebraic closed-action certificate)

Let $X$ be an algebraic variety over $\overline{\mathbb Q}$ and let $U$ be
a Zariski-open subset.  Let $F:U\dashrightarrow X$ be an algebraic rational
map, let $\theta$ be an algebraic rational one-form, and let $G$ be an
algebraic rational function such that

$$
F^*\theta-\theta=dG
$$

where both sides are defined.  Starting from
$P_0=P\in X(\overline{\mathbb Q})$, require recursively that $F$ is defined
at $P_j$ and put $P_{j+1}=F(P_j)$; assume $P_n=P_0$.  Before evaluating the
$j$th summand, require separately that $G$ is regular at $P_j$.  Any use of
$\theta$, a gauge, or a transition function additionally requires that datum
to be defined and pole-free at the precise point where it is evaluated.
Then

$$
\mathcal A_G(P):=\sum_{j=0}^{n-1}G(P_j)
\in\overline{\mathbb Q}.
$$

Exact symplecticity explains why this sum is a closed-orbit action, but the
arithmetic conclusion uses only that $G$ and the orbit are algebraic and
regular at the evaluation points.

### Corollary B (prime-logarithm obstruction)

Under Theorem A, for every positive rational prime $p$, every integer
$r\ge1$, and every nonzero algebraic number $c$,

$$
\mathcal A_G(P)\ne c\log p,
\qquad
r\mathcal A_G(P)\ne c\log(p^r),
$$

where $\log p$ denotes the positive real logarithm.  More generally, if
$\beta\in\overline{\mathbb Q}^{\times}$ and
$e^{\mathcal A_G(P)}=\beta$, then the only algebraic possibility is
$\mathcal A_G(P)=0$ and $\beta=1$.  Thus $\mathcal A_G(P)$ is not any
complex logarithm of an algebraic number
$\beta\in\overline{\mathbb Q}^{\times}\setminus\{1\}$.  The value
$\beta=0$ has no complex logarithm.  Also,

$$
e^{\mathcal A_G(P)}\ne\beta
$$

for algebraic $\beta$ whenever $\mathcal A_G(P)\ne0$.

The real numbers

$$
\operatorname{Re}\mathcal A_G(P),\quad
\operatorname{Im}\mathcal A_G(P),\quad
|\mathcal A_G(P)|
$$

are algebraic, so none can equal $\log p$.

### Proposition C (exact algebraic gauge and additive normalization)

Let $\chi$ be a single-valued algebraic rational function regular on the
orbit, put

$$
\theta'=\theta+d\chi,
$$

and choose

$$
G'=G+\chi\circ F-\chi+C
$$

with a constant $C$.  Then $F^*\theta'-\theta'=dG'$ and

$$
\mathcal A_{G'}(P)=\mathcal A_G(P)+nC.
$$

If $C=0$, the action is invariant under the gauge.  If
$C\in\overline{\mathbb Q}$, the numerical value changes but remains
algebraic, so Corollary B survives.  If arbitrary transcendental $C$ is
allowed, no such conclusion follows.

More generally, if a time-dependent presentation or a sequence of local
charts uses one-step representatives

$$
G'_j=G_j+\chi_{j+1}\circ F_j-\chi_j+C_j,
$$

where every $\chi_j$ is single-valued and
$\overline{\mathbb Q}$-rational, then the general action shift is

$$
\chi_n(P_n)-\chi_0(P_0)+\sum_{j=0}^{n-1}C_j.
$$

Endpoint compatibility removes the first two terms.  Without compatibility,
the shorter formula must not be used; nevertheless the arithmetic
certificate remains valid if both endpoint values and all $C_j$ are defined
and algebraic.  Multivalued transitions, untracked monodromy, and any
transcendental endpoint contribution remain outside the proposition.

### Theorem D (algebraic Hénon action)

Let $a\in\overline{\mathbb Q}$ and

$$
H_a(q,p)=(q^2-a-p,q).
$$

Every finite complex periodic point of $H_a$ has algebraic coordinates.  For
$\theta=p\,dq$, the zero-constant polynomial

$$
G(q,p)=\frac23q^3-pq
$$

satisfies $H_a^*\theta-\theta=dG$.  Hence the closed action of every finite
periodic orbit is algebraic and cannot equal $\log p_0$ for any positive
rational prime $p_0$.

The type-1 generating function

$$
L_a(q,Q)=\frac13q^3-aq-qQ
$$

satisfies $p=\partial_qL_a$, $P=-\partial_QL_a$, and
$L_a=-G$ on the graph of $H_a$.  Its periodic discrete action is therefore
the negative of $\mathcal A_G$ and obeys the same exclusion.

### Corollary E ($S$-integral refinement for Hénon actions)

Let $K_0$ be a number field, let $S_0$ contain its archimedean places, and
let $a\in\mathcal O_{K_0,S_0}$.  For a finite periodic point of $H_a$, let
$K/K_0$ be a finite number field containing every orbit coordinate and let
$S$ contain all places of $K$ above $S_0$.  Then its coordinates lie in
$\mathcal O_{K,S}$ and

$$
3\mathcal A_G(P)
$$

lies in $\mathcal O_{K,S}$.  Equivalently,
$\mathcal A_G(P)$ is integral outside $S$ and the places of $K$ above the
rational prime $3$.

## Status

`PROVABLE AFTER SOURCE-LOCK V3 REPAIR`

The claim survives under the source-lock-v3 meaning of "algebraic exact
potential": a single-valued rational function over
$\overline{\mathbb Q}$, including an algebraic additive normalization, and
an algebraic orbit avoiding all poles and indeterminacies.  Without the
algebraic normalization condition the broad claim is false; the explicit
counterexample appears in Step 9.

## Assumptions

- "Algebraic map/form/function" means rational algebraic data defined over
  a number field contained in $\overline{\mathbb Q}$.
- The orbit is constructed step by step: $F_j$ is defined at $P_j$ before
  $P_{j+1}$ is formed; formal cancellation in a composite is not enough.
- Every actually evaluated $G_j$, $\theta_j$, $\chi_j$, endpoint gauge, and
  transition is checked separately for a pole at its evaluation point.
- The potential is single-valued on the orbit domain.
- Every admitted gauge is a single-valued
  $\overline{\mathbb Q}$-rational function; a logarithmic or analytic
  multivalued primitive is not an admitted gauge.
- Every additive constant, including a chart- or step-dependent constant,
  and every endpoint or transition contribution is frozen before orbit
  evaluation and belongs to $\overline{\mathbb Q}$.
- Equality to $\log p$ is exact, after a fixed dimensionless normalization.
  Numerical proximity and asymptotic scaling are outside the theorem.
- The theorem concerns the action itself and the explicitly listed algebraic
  transforms.  It does not cover a logarithm applied after the action.

## Notation

- $\overline{\mathbb Q}$ is the field of algebraic numbers in $\mathbb C$.
- $P_j=F^j(P)$, with indices read modulo $n$ on a period-$n$ orbit.
- $\mathcal A_G(P)$ is the one-traversal action associated with the frozen
  potential $G$.
- $\log p$ is the positive real logarithm; a "complex logarithm" of
  $\beta$ is any $z\in\mathbb C$ satisfying $e^z=\beta$.
- For the Hénon map, $(Q,P)=H_a(q,p)$; the capital $P$ in that coordinate
  formula is not the periodic point used elsewhere.

## Proof Strategy

Evaluate the algebraic potential at algebraic orbit points and use closure of
$\overline{\mathbb Q}$ under finite sums.  Apply the
Hermite--Lindemann theorem to separate these algebraic values from logarithms
of nontrivial algebraic numbers.  Audit the gauge formula by direct
differentiation and a telescoping sum.  For the Hénon family, first prove
periodic-coordinate algebraicity from the projective closure of the cyclic
recurrence, then derive the exact potential and type-1 generating function
directly.  Finally, apply a non-archimedean maximum argument for the
$S$-integral refinement.

## Dependency Map

1. Theorem A depends on regular evaluation of rational functions at
   $\overline{\mathbb Q}$-points and closure of
   $\overline{\mathbb Q}$ under addition.
2. Corollary B depends on Hermite--Lindemann:
   $\alpha\in\overline{\mathbb Q}\setminus\{0\}$ implies
   $e^\alpha$ is transcendental.
3. The real-part, imaginary-part, and modulus statements additionally use
   stability of $\overline{\mathbb Q}$ under complex conjugation and square
   roots.
4. Proposition C depends on the pullback identity
   $F^*(d\chi)=d(\chi\circ F)$ and telescoping around a closed orbit; the
   general local/time-dependent formula retains the endpoint mismatch, and
   compatibility is required only to delete it.
5. Theorem D's coordinate claim depends on the cyclic Hénon equations
   having no projective solution at infinity.
6. Its exactness and generating-function claims are direct differential
   identities.
7. Corollary E depends on monicity of the quadratic term and the
   ultrametric maximum principle at finite places outside $S$.

## Auditable proof contract (version 3)

The following unique JSON block is the machine-readable semantic interface
for the static checker.  JSON indentation is nonsemantic, while IDs,
dependencies, and tagged equations are exact.  The prose below remains the
mathematical proof and does not replace this fail-closed interface.

<!-- BEGIN AC_PROOF_CONTRACT_V3 -->
```json
{
  "schema": "AC_PROOF_CONTRACT",
  "version": 3,
  "contracts": [
    {
      "id": "AC-DOMAIN-v3",
      "kind": "dependency",
      "requires": [
        "each_map_step_defined_before_evaluation",
        "each_potential_value_defined_and_pole_free",
        "each_gauge_endpoint_and_transition_defined_and_pole_free"
      ]
    },
    {
      "id": "AC-EVAL-v3",
      "kind": "equation",
      "requires": [
        "single_valued_qbar_rational_potential",
        "algebraic_periodic_orbit",
        "finite_sum_closed_in_qbar"
      ]
    },
    {
      "id": "AC-HL-v3",
      "kind": "equation",
      "requires": [
        "beta_zero_has_no_complex_logarithm",
        "beta_one_retains_exactly_the_algebraic_exception_A_zero",
        "nonzero_algebraic_A_has_transcendental_exponential"
      ]
    },
    {
      "id": "AC-GAUGE-v3",
      "kind": "equation",
      "requires": [
        "retain_chi_n_at_P_n",
        "retain_minus_chi_0_at_P_0",
        "retain_every_step_constant_C_j",
        "endpoint_compatibility_only_removes_endpoint_difference"
      ]
    },
    {
      "id": "AC-OBS-v3",
      "kind": "dependency",
      "requires": [
        "action_real_part_imaginary_part_and_modulus_are_covered",
        "log_modulus_and_argument_are_nonclaims"
      ]
    },
    {
      "id": "AC-HENON-v3",
      "kind": "equation",
      "requires": [
        "period_one_counts_two_neighbor_slots",
        "period_two_counts_two_neighbor_slots"
      ]
    },
    {
      "id": "AC-GEOM-v3",
      "kind": "dependency",
      "requires": [
        "homogenized_cyclic_system_has_no_projective_point_at_infinity",
        "positive_dimensional_projective_component_would_meet_infinity"
      ]
    },
    {
      "id": "AC-SINT-v3",
      "kind": "equation",
      "requires": [
        "orbit_field_is_finite_extension_K_over_K0",
        "S_contains_places_above_S0",
        "only_three_times_action_is_certified_S_integral"
      ]
    },
    {
      "id": "AC-ROLE-v3",
      "kind": "dependency",
      "requires": [
        "static_computation_is_implementation_audit_only",
        "all_period_conclusion_is_deductive"
      ]
    }
  ]
}
```
<!-- END AC_PROOF_CONTRACT_V3 -->

The stable equations used by this contract are

$$
P_{j+1}=F_j(P_j),\qquad G_j(P_j)\in\overline{\mathbb Q}
\tag{AC-EVAL-v3}
$$

$$
A'-A=\chi_n(P_n)-\chi_0(P_0)+\sum_{j=0}^{n-1}C_j
\tag{AC-GAUGE-v3}
$$

$$
A\in\overline{\mathbb Q},\quad
\beta\in\overline{\mathbb Q}^{\times},\quad e^A=\beta
\quad\Longrightarrow\quad (A,\beta)=(0,1)
\tag{AC-HL-v3}
$$

$$
n=1:\ 2q_0=q_0^2-a;\qquad
n=2:\ 2q_1=q_0^2-a,\quad 2q_0=q_1^2-a
\tag{AC-HENON-v3}
$$

$$
a\in\mathcal O_{K_0,S_0},\quad K/K_0\text{ contains the orbit},
\quad S=\{v:v\mid S_0\}
\quad\Longrightarrow\quad 3\mathcal A_G\in\mathcal O_{K,S}
\tag{AC-SINT-v3}
$$

## Proof

### Step 1: algebraic evaluation of the potential

Choose a number field $K$ over which $F$, $G$, and the finite orbit are
defined.  This is possible because the coefficients of the algebraic data
and the finitely many coordinates of the orbit are algebraic.

Write $G=A/B$ on an affine chart containing an orbit point, with
$A,B\in K[x_1,\ldots,x_m]$.  The no-pole assumption gives $B(P_j)\ne0$.
Since the coordinates of $P_j$ are algebraic,
$A(P_j),B(P_j)\in\overline{\mathbb Q}$ and therefore

$$
G(P_j)=\frac{A(P_j)}{B(P_j)}\in\overline{\mathbb Q}.
$$

This applies at each of the finitely many orbit points, using finitely many
charts if necessary.  The field of algebraic numbers is closed under finite
sums, so

$$
\mathcal A_G(P)=\sum_{j=0}^{n-1}G(P_j)
\in\overline{\mathbb Q}.
$$

This proves Theorem A. $\square$

### Step 2: exclude every logarithm of a nontrivial algebraic number

Let $\beta\in\overline{\mathbb Q}^{\times}\setminus\{1\}$ and suppose that
$\mathcal A_G(P)$ were a complex logarithm of $\beta$.  Then

$$
e^{\mathcal A_G(P)}=\beta.
$$

The value $\mathcal A_G(P)$ cannot be zero because $e^0=1\ne\beta$.
By Theorem A it is algebraic.  Hermite--Lindemann then states that its
exponential is transcendental, contradicting the algebraicity of $\beta$.
For $\beta=1$, the value $A=0$ is the unique algebraic solution of
$e^A=1$; the nonzero branches $2\pi i k$ are not algebraic.  The target
$\beta=0$ has no complex logarithm because the complex exponential never
vanishes.

Taking $\beta=p$ proves the unscaled prime-logarithm statement for every
complex branch.  If $c\in\overline{\mathbb Q}^{\times}$ and
$\mathcal A_G(P)=c\log p$, then
$\log p=\mathcal A_G(P)/c$ would be algebraic, contradicting the case just
proved.  Division by $n$ and multiplication by a repetition number $r$ keep
the action algebraic.  Since $\log(p^r)=r\log p$ is transcendental, the
average and repetition conclusions follow.  This proves the first part of
Corollary B.

If $\mathcal A_G(P)\ne0$, the same Hermite--Lindemann statement makes
$e^{\mathcal A_G(P)}$ transcendental, so it cannot equal any algebraic
$\beta$.  This proves the exponential formulation. $\square$

### Step 3: real part, imaginary part, and modulus

Complex conjugation maps algebraic numbers to algebraic numbers.  Hence, for
$A=\mathcal A_G(P)\in\overline{\mathbb Q}$,

$$
\operatorname{Re}A=\frac{A+\overline A}{2},
\qquad
\operatorname{Im}A=\frac{A-\overline A}{2i}
$$

are algebraic.  Also $A\overline A$ is algebraic, and $|A|$ is a root of

$$
T^2-A\overline A=0.
$$

Thus $|A|$ is algebraic.  The positive real number $\log p$ is
transcendental by Step 2, so it cannot equal any of these three algebraic
numbers.

This argument makes no assertion about $\arg A$ or $\log|A|$; those are not
algebraic operations on $A$ in general.

### Step 4: exact algebraic gauge transformation

Set $\theta'=\theta+d\chi$.  Pullback commutes with the exterior derivative,
so

$$
\begin{aligned}
F^*\theta'-\theta'
&=F^*\theta-\theta+F^*(d\chi)-d\chi\\
&=dG+d(\chi\circ F)-d\chi\\
&=d\bigl(G+\chi\circ F-\chi+C\bigr)\\
&=dG'.
\end{aligned}
$$

On the periodic orbit,

$$
\begin{aligned}
\mathcal A_{G'}(P)
&=\sum_{j=0}^{n-1}
  \bigl(G(P_j)+\chi(P_{j+1})-\chi(P_j)+C\bigr)\\
&=\mathcal A_G(P)+nC,
\end{aligned}
$$

because $P_n=P_0$.  When $C=0$ the action is gauge invariant.  When $C$ is
algebraic, Theorem A and Corollary B apply to the shifted action.  This proves
the autonomous part of Proposition C.

For a sequence of maps or local representatives, first construct every
$P_{j+1}=F_j(P_j)$ only after checking that $F_j$ is defined at $P_j$.
Then check separately that $G_j(P_j)$, $\chi_j(P_j)$,
$\chi_{j+1}(P_{j+1})$, and any transition value are finite before
evaluating

$$
G'_j=G_j+\chi_{j+1}\circ F_j-\chi_j+C_j
$$

at $P_{j+1}=F_j(P_j)$.  The interior gauge differences telescope without
any endpoint assumption:

$$
\sum_{j=0}^{n-1}G'_j(P_j)
=\sum_{j=0}^{n-1}G_j(P_j)
 +\chi_n(P_n)-\chi_0(P_0)+\sum_{j=0}^{n-1}C_j.
$$

If endpoint gauges agree under the closed-orbit identification, the endpoint
term vanishes.  If they do not agree but both endpoint values and every
$C_j$ are algebraic, the numerical shift includes the algebraic mismatch and
the source lock survives.  An undefined value, a pole, an unfrozen branch
jump, or a transcendental mismatch stops the absolute-action certificate.
This completes Proposition C. $\square$

The calculation requires $\chi$ to be single-valued and regular at each
orbit point.  A closed but non-exact change of primitive or a multivalued
gauge can contribute monodromy and is not represented by this telescoping
formula.

### Step 5: exactness and generating data for $H_a$

Put

$$
(Q,P)=H_a(q,p)=(q^2-a-p,q),
\qquad \theta=p\,dq.
$$

Then

$$
H_a^*\theta=P\,dQ
=q\,d(q^2-a-p)
=2q^2\,dq-q\,dp.
$$

Therefore

$$
H_a^*\theta-\theta
=(2q^2-p)\,dq-q\,dp
=d\left(\frac23q^3-pq\right).
$$

This proves the exactness identity with the frozen zero-constant polynomial
$G(q,p)=2q^3/3-pq$.

For

$$
L_a(q,Q)=\frac13q^3-aq-qQ,
$$

we have

$$
\partial_qL_a=q^2-a-Q=p,
\qquad
-\partial_QL_a=q=P.
$$

Thus $L_a$ is a type-1 generating function in the stated sign convention.
On the graph, $Q=q^2-a-p$, and substitution gives

$$
L_a(q,Q)
=\frac13q^3-aq-q(q^2-a-p)
=pq-\frac23q^3
=-G(q,p).
$$

### Step 6: every finite periodic point of $H_a$ is algebraic

Let $(q_j,p_j)$ be a period-$n$ orbit.  The second component of the map gives
$p_j=q_{j-1}$, while the first gives the cyclic recurrence

$$
q_{j+1}+q_{j-1}=q_j^2-a,
\qquad j\in\mathbb Z/n\mathbb Z.
$$

The two cyclic neighbor slots retain their multiplicity.  Thus $n=1$ gives
$2q_0=q_0^2-a$, while $n=2$ gives
$2q_1=q_0^2-a$ and $2q_0=q_1^2-a$; equal neighbors are never deduplicated.

Consider the $n$ affine equations

$$
q_j^2-a-q_{j+1}-q_{j-1}=0.
$$

Homogenize them in projective coordinates
$[Q_0:\cdots:Q_{n-1}:Z]$:

$$
Q_j^2-aZ^2-Q_{j+1}Z-Q_{j-1}Z=0.
$$

On the hyperplane $Z=0$, every equation becomes $Q_j^2=0$.  Hence every
$Q_j$ would be zero, which is not a projective point.  The projective zero
set therefore has no point at infinity.

If this projective zero set had a positive-dimensional irreducible
component, that component would meet every hyperplane, in particular
$Z=0$.  This contradicts the preceding paragraph.  The zero set is thus
zero-dimensional.  It is defined over the number field $\mathbb Q(a)$, so
the coordinates of each of its points are algebraic over $\mathbb Q(a)$ and
therefore algebraic over $\mathbb Q$.  Since $p_j=q_{j-1}$, all phase-space
coordinates are algebraic.

### Step 7: formula and algebraicity of the Hénon action

Using $p_j=q_{j-1}$ in the potential gives

$$
\mathcal A_G(P)
=\sum_{j=0}^{n-1}
 \left(\frac23q_j^3-q_{j-1}q_j\right).
$$

Every $q_j$ is algebraic by Step 6, so the sum is algebraic.  Step 5 gives

$$
\sum_{j=0}^{n-1}L_a(q_j,q_{j+1})=-\mathcal A_G(P).
$$

Step 2 now excludes $\log p_0$ for every rational prime $p_0$ under either
sign convention.  This proves Theorem D. $\square$

### Step 8: $S$-integrality and the denominator $3$

Let $a\in\mathcal O_{K_0,S_0}$ and choose a finite extension $K/K_0$
containing all coordinates of the periodic orbit.  Let $S$ be the set of
places of $K$ above $S_0$, together with all archimedean places.  Fix a
non-archimedean place $w$ of $K$ outside $S$.
Suppose

$$
R=\max_j|q_j|_w>1
$$

and choose an index $j$ attaining the maximum.  Since $|a|_w\le1$,

$$
|q_j^2-a|_w=|q_j|_w^2=R^2.
$$

The recurrence, however, gives

$$
|q_j^2-a|_w
=|q_{j+1}+q_{j-1}|_w
\le\max(|q_{j+1}|_w,|q_{j-1}|_w)
\le R,
$$

contradicting $R^2>R$.  Hence every $|q_j|_w\le1$ at every place outside
$S$, so every periodic coordinate is integral over $\mathcal O_{K,S}$.

Finally,

$$
3\mathcal A_G(P)
=\sum_{j=0}^{n-1}
 \left(2q_j^3-3q_{j-1}q_j\right)
$$

is a polynomial with integer coefficients in these $S$-integral
coordinates.  It is integral over $\mathcal O_{K,S}$.  Dividing by $3$ can
introduce only places above the rational prime $3$.  This proves Corollary E.
$\square$

### Step 9: necessity of algebraic normalization

Let $X=\mathbb A^2$, let $F$ be the identity map, and take
$\theta=p\,dq$.  Then

$$
F^*\theta-\theta=0.
$$

Every constant function is an exact potential because its differential is
zero.  If arbitrary analytic constants are allowed, choose

$$
G\equiv\log 2.
$$

Every point is fixed and its one-step action is $\log 2$.  The map and
Liouville primitive are algebraic, but the potential's normalization
constant is transcendental.  Thus algebraicity of the map alone cannot
prove the action obstruction, and exactness does not remove the additive
constant ambiguity.

More generally, for any selected period-$n$ orbit with initial action
$\mathcal A$, the constant

$$
C=\frac{\log p-\mathcal A}{n}
$$

forces the shifted action to equal $\log p$.  Such a constant depends on the
target and orbit and is forbidden by the source lock.  This is target
injection, not an intrinsic arithmetic mechanism.

The same attack can be distributed over steps: any constants $C_j$ with
$\sum_jC_j=\log p-\mathcal A$ force the target.  Requiring each $C_j$ to be
algebraic blocks this attack because their finite sum is algebraic.

## Corrections or Missing Assumptions

- The phrase "algebraic exact-symplectic map" is insufficient by itself.
  The potential, its additive constant, and the evaluated orbit must also be
  algebraic.
- A global or orbitwise single-valued potential is required.  Local or
  time-dependent generating functions retain the general endpoint mismatch;
  compatibility is needed only for the shorter formula, while every
  endpoint value, transition, and step constant must be defined, frozen, and
  algebraic for the source lock to survive.
- Pole avoidance is necessary for the action to be a finite algebraic
  number.
- An arbitrary change of primitive by a closed non-exact form is outside the
  exact-gauge formula and must be audited separately.

## Open Risks

- The general arithmetic statement is an elementary evaluation lemma plus a
  classical transcendence theorem.  It must be presented as a design
  certificate, not as a new action-spectrum theory.
- Action normalization is convention-dependent.  Only the algebraicity class
  is stable under algebraic per-step constants; the numerical values are not.
- The result does not obstruct $\log|\mathcal A_G|$.  If an algebraic action
  itself equals a prime, logarithmic post-processing can produce $\log p$.
- In particular, $|\mathcal A_G|\ne\log p$ must never be rewritten as
  $\log|\mathcal A_G|\ne\log p$; these are different claims, and the latter
  may fail when $|\mathcal A_G|=p$.
- The result does not constrain return times or derivatives of action with
  respect to energy.
- The Hénon $S$-integral refinement is stated only after adjoining the orbit
  coordinates and extending $S$ to their number field.  It contains an
  unavoidable denominator $3$
  for the canonical primitive and chosen normalization; it must not be
  misstated as integral action.
