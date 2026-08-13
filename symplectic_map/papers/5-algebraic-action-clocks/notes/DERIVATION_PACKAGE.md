# Derivation Package

## Target

Derive an all-period, data-free certificate for the proposal that a periodic
generating-function action of an algebraic exact-symplectic map might itself
provide the arithmetic clock

$$
T_{\gamma_p}=\log p.
$$

The immediate objective is to determine whether the normalized closed action
can equal $\log p$, not whether some nonalgebraic function of the action can
do so.

## Status

`COHERENT AFTER REFRAMING / EXTRA ASSUMPTION`

The coherent invariant is not an unnormalized action value.  A potential is
defined only up to an additive constant, which shifts a period-$n$ action by
$nC$.  The source-locked object is therefore the action of a **frozen
algebraic representative**, or equivalently its algebraicity class under
algebraic gauge and algebraic constant changes.  Under that reframe, the
prime-logarithm obstruction is exact.

## Invariant Object

The organizing object is the one-traversal discrete action cocycle

$$
\mathcal A_G(P)=\sum_{j=0}^{n-1}G(F^jP)
$$

for a frozen exact potential $G$.  The robust arithmetic invariant is

$$
\mathcal A_G(P)\in\overline{\mathbb Q},
$$

not the numerical value modulo arbitrary constants.  Under a zero-constant
exact algebraic gauge, the numerical action is also invariant.

## Assumptions

- $F$, $\theta$, $G$, and every admitted gauge $\chi$ are single-valued
  rational algebraic data over $\overline{\mathbb Q}$; logarithmic and other
  analytic multivalued gauges are excluded.
- $F^*\theta-\theta=dG$ on the orbit domain.
- The periodic orbit is algebraic; each $P_{j+1}=F_j(P_j)$ is formed only
  after checking $F_j$ at $P_j$, and every potential, gauge, endpoint, or
  transition value is checked separately for a pole before evaluation.
- $G$ is single-valued on the orbit domain.
- Every additive normalization, including a local or step-dependent
  constant $C_j$, and every actual endpoint or transition contribution is
  frozen before evaluation and is algebraic.
- Equality is exact and dimensionless; any overall scale is a fixed nonzero
  algebraic number.
- For the Hénon specialization, $a$ is algebraic.  The stronger integrality
  line starts with $a\in\mathcal O_{K_0,S_0}$, then passes to an orbit field
  $K/K_0$ and extends $S_0$ to the places $S$ of $K$ above it.

## Notation

- $P_j=F^j(P)$, with $P_n=P_0$.
- $n$ is the one-traversal period; $r$ is a repetition number.
- $\mathcal A_G(P)$ is the action in the potential convention
  $F^*\theta-\theta=dG$.
- $\mathcal A_L=\sum_jL(q_j,q_{j+1})$ is the type-1 convention for Hénon and
  equals $-\mathcal A_G$.
- $S$ is a finite set of places containing the archimedean places.

## Derivation Strategy

Start from the exactness cocycle rather than from a fitted clock.  Separate
three layers:

1. an **algebraic-evaluation layer**, which puts every closed action in
   $\overline{\mathbb Q}$;
2. a **transcendence layer**, which separates algebraic actions from every
   branch of $\log p$;
3. a **normalization layer**, which identifies exactly which gauge changes
   preserve the value and which constants merely preserve algebraicity.

Then specialize to the polynomial Hénon automorphism, where the primitive,
potential, generating function, periodic-coordinate algebraicity, and
$S$-integral refinement can all be displayed without approximation.

## Derivation Map

1. `Definition`: $F^*\theta-\theta=dG$ and
   $\mathcal A_G=\sum_jG(P_j)$.
2. `Proposition`: regular evaluation of $G\in\overline{\mathbb Q}(X)$ at
   $P_j\in X(\overline{\mathbb Q})$ is algebraic.
3. `Proposition`: the finite action sum is algebraic.
4. `Named theorem`: Hermite--Lindemann makes every nonzero logarithm of a
   nontrivial algebraic number transcendental.
5. `Corollary`: $\mathcal A_G\ne\log p$, including repetitions and
   algebraically scaled variants.
6. `Identity`: an exact gauge changes the potential by
   $\chi\circ F-\chi+C$.
7. `Identity`: the gauge difference telescopes and the constant contributes
   $nC$ in the autonomous closed case; in general the shift is
   $\chi_n(P_n)-\chi_0(P_0)+\sum_jC_j$.
8. `Counterexample`: a transcendental constant potential for the identity
   map can inject $\log 2$.
9. `Hénon identity`: $G=2q^3/3-pq$ and
   $L_a=q^3/3-aq-qQ$.
10. `Hénon proposition`: the cyclic recurrence has no projective
    solution at infinity, so all finite periodic coordinates are algebraic.
11. `Hénon specialization`: the action is an explicit algebraic sum.
12. `$S$-integral proposition`: a non-archimedean maximum argument gives
    $3\mathcal A_G$ integral outside $S$.

No approximation enters this derivation.

## Main Derivation

### Step 1: close the exactness cocycle around an orbit

The defining one-step object is the exact potential $G$ in

$$
F^*\theta-\theta=dG.
$$

The $n$-step pullback telescopes at the level of one-forms:

$$
(F^n)^*\theta-\theta
=d\left(\sum_{j=0}^{n-1}G\circ F^j\right).
$$

At a period-$n$ point, the scalar value of the sum is the closed action

$$
\mathcal A_G(P)=\sum_{j=0}^{n-1}G(P_j).
$$

This is an exact identity.  It explains why the same potential used to
define one step supplies the full periodic action.

### Step 2: freeze the arithmetic type of the action

Every $G(P_j)$ is algebraic because $G$ has algebraic coefficients, $P_j$
has algebraic coordinates, and no denominator vanishes at $P_j$.  Therefore

$$
\mathcal A_G(P)\in\overline{\mathbb Q}.
$$

This is a proposition, not a statistical observation.  The argument is
uniform in $n$.

### Step 3: compare algebraic action with the proposed logarithmic clock

Hermite--Lindemann gives

$$
0\ne\alpha\in\overline{\mathbb Q}
\quad\Longrightarrow\quad
e^\alpha\notin\overline{\mathbb Q}.
$$

If an algebraic action $A$ were any branch of $\log p$, then
$e^A=p$ would be algebraic.  The value $A$ is nonzero because $p\ne1$,
contradicting the theorem.  Hence

$$
\mathcal A_G(P)\ne\log p.
$$

More generally, for $\beta\in\overline{\mathbb Q}^{\times}$ the only
algebraic solution of $e^A=\beta$ is the trivial case $A=0,\beta=1$.
There is no complex logarithm of $\beta=0$.

For an $r$-fold repetition,

$$
\mathcal A_G(P^{\times r})=r\mathcal A_G(P)
\in\overline{\mathbb Q},
$$

whereas

$$
\log(p^r)=r\log p
$$

is transcendental.  Repetition does not repair the mismatch.

If a fixed nonzero algebraic scale $c$ is introduced, then
$c\log p$ remains transcendental; otherwise dividing by $c$ would make
$\log p$ algebraic.  Thus an algebraic unit conversion or algebraic
semiclassical scale does not change the conclusion.

### Step 4: separate gauge invariance from normalization dependence

Under

$$
\theta'=\theta+d\chi,
$$

the exact potential can be chosen as

$$
G'=G+\chi\circ F-\chi+C.
$$

The closed sum is

$$
\begin{aligned}
\mathcal A_{G'}(P)
&=\mathcal A_G(P)
 +\sum_{j=0}^{n-1}
   \bigl(\chi(P_{j+1})-\chi(P_j)\bigr)
 +nC\\
&=\mathcal A_G(P)+nC.
\end{aligned}
$$

The telescoping part is a gauge identity.  The $nC$ term is a normalization
effect.  An algebraic $C$ preserves the arithmetic type but not the value.
An arbitrary transcendental $C$ destroys the obstruction and can insert a
target by hand.  Therefore the meaningful certificate is:

> algebraic representatives produce only algebraic closed actions, even
> though their raw numerical spectra shift under algebraic per-step
> constants.

For a time-dependent or chartwise presentation, let

$$
G'_j=G_j+\chi_{j+1}\circ F_j-\chi_j+C_j.
$$

Without imposing endpoint compatibility, direct telescoping gives

$$
\sum_jG'_j(P_j)=\sum_jG_j(P_j)
+\chi_n(P_n)-\chi_0(P_0)+\sum_jC_j.
$$

Compatible endpoint gauges make the endpoint term vanish.  An incompatible
but defined algebraic endpoint mismatch remains inside the algebraic source
lock, although the shorter $\sum_jC_j$ formula must stop.  An undefined
endpoint, a pole, a multivalued branch jump, or a transcendental mismatch
stops the absolute-action certificate.  Thus separately chosen algebraic
step constants preserve algebraicity even though they need not produce the
uniform shift $nC$.

### Step 5: derive the Hénon exact potential

For

$$
(Q,P)=H_a(q,p)=(q^2-a-p,q),
$$

and $\theta=p\,dq$,

$$
\begin{aligned}
H_a^*\theta-\theta
&=q\,d(q^2-a-p)-p\,dq\\
&=(2q^2-p)\,dq-q\,dp\\
&=d\left(\frac23q^3-pq\right).
\end{aligned}
$$

Thus the frozen zero-constant potential is

$$
G(q,p)=\frac23q^3-pq.
$$

The type-1 function

$$
L_a(q,Q)=\frac13q^3-aq-qQ
$$

obeys

$$
p=\partial_qL_a,
\qquad
P=-\partial_QL_a.
$$

On the graph of the map,

$$
L_a(q,Q)=-G(q,p).
$$

These are exact identities.  The sign is a convention and does not affect
algebraicity or the transcendence comparison.

### Step 6: derive the Hénon periodic action

On a periodic orbit, $p_j=q_{j-1}$ and

$$
q_{j+1}+q_{j-1}=q_j^2-a.
$$

Cyclic neighbor slots are counted with multiplicity: $n=1$ gives
$2q_0=q_0^2-a$, and $n=2$ gives
$2q_1=q_0^2-a$, $2q_0=q_1^2-a$.

Homogenizing the cyclic equations shows that the projective closure has no
point with homogenizing coordinate zero: at infinity the equations force
every homogeneous $q_j$ coordinate to vanish.  Hence the periodic solution
set is zero-dimensional and every finite periodic coordinate is algebraic
when $a$ is algebraic.

Substitution into $G$ gives

$$
\mathcal A_G(P)
=\sum_{j=0}^{n-1}
 \left(\frac23q_j^3-q_{j-1}q_j\right)
\in\overline{\mathbb Q}.
$$

The type-1 action is

$$
\mathcal A_L(P)
=\sum_{j=0}^{n-1}L_a(q_j,q_{j+1})
=-\mathcal A_G(P).
$$

Both are therefore excluded as exact prime logarithms.

### Step 7: refine from algebraic to $S$-integral provenance

Let $a\in\mathcal O_{K_0,S_0}$, adjoin every orbit coordinate to a finite
number field $K/K_0$, and extend $S_0$ to all places $S$ of $K$ above it.
At a finite place of $K$ outside $S$, let
$R=\max_j|q_j|_v$.  If $R>1$, monicity gives

$$
|q_j^2-a|_v=R^2
$$

at a maximizing index, whereas the recurrence bounds the same quantity by
$R$.  This contradiction yields $R\le1$ and makes every $q_j$ integral
outside $S$.

Therefore

$$
3\mathcal A_G(P)
=\sum_j\left(2q_j^3-3q_{j-1}q_j\right)
$$

is $S$-integral.  The canonical rational coefficient $1/3$ is the only new
denominator outside $S$.  This refinement is an arithmetic provenance
record, not a stronger transcendence theorem.

## Remarks and Interpretation

- The obstruction identifies where a successful exact prime-logarithm clock
  must leave this algebraic class: transcendental normalization,
  transcendental parameters, a logarithmic observable, multivalued
  monodromy, or a different non-action clock.
- Exact symplecticity supplies a canonical cocycle structure, but it does not
  choose the additive constant.  The constant is mathematical data, not an
  innocuous reporting convention when absolute action values are compared.
- Algebraic Hénon actions may still be dynamically rich and need not be
  rational or integral.  The theorem only separates them from logarithms of
  nontrivial algebraic numbers.
- The same logic applies to any nontrivial algebraic target $\beta$, not only
  rational primes: an algebraic action cannot be a logarithm of $\beta$.

## Boundaries and Non-Claims

- No claim about $\log|\mathcal A_G|$ or $\arg\mathcal A_G$; the valid
  inequality $|\mathcal A_G|\ne\log p$ does not imply any inequality after
  applying a logarithm to $|\mathcal A_G|$.
- No claim that $\mathcal A_G$ cannot equal a rational prime.
- No claim about return periods, multiplier logarithms, Lyapunov exponents,
  or $\partial_E\mathcal A$.
- No claim about transcendental parameters or transcendental physical unit
  conversions.
- No claim about local multivalued generating functions whose transition
  periods are not algebraic.
- No approximate, asymptotic, density, or near-collision statement.
- No prime table, zeta-zero table, determinant fit, or quantization is used.

## Open Risks

- The contribution is easy to compress to one sentence; standalone novelty
  is fragile.
- A reviewer may object that action spectra are usually considered only up
  to normalization.  The response is to foreground the algebraicity class
  and state absolute-value comparisons only after freezing the constant.
- A logarithmic post-processing step is a genuine loophole, not a technical
  defect.  It must remain explicit rather than being rhetorically folded
  into the theorem.
- The Hénon derivation inherits the noncompactness and lack of a proved
  arithmetic orbit labelling from the broader program; neither affects this
  local certificate.
