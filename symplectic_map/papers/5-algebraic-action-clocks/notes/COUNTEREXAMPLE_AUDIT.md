# Counterexample Audit

**Candidate:** `algebraic_exact_action_clock_obstruction_v1`  
**Audit mode:** adversarial reconstruction from the frozen statement after
the proof package was written  
**Current independence level:** separate internal proof pass completed;
second-agent cross-check returned `REPAIR` on 2026-08-14 and its mandatory
repairs were incorporated into source-lock v3 before candidate execution  
**Candidate orbit data used:** none  
**Prime or zero data used:** none

## Verdict

`PASS FOR THE NARROW FROZEN THEOREM; FAIL FOR THE BROAD UNNORMALIZED CLAIM`

No counterexample found satisfies all frozen hypotheses.  One decisive
counterexample breaks the informal map-only version: an exact potential is
defined up to a constant, and a transcendental constant can insert
$\log p$ directly.  The valid theorem is therefore about a single-valued
algebraic potential with an algebraic additive normalization, evaluated on
an algebraic orbit away from poles.

The audit also found several tempting but invalid overextensions.  In
particular, the theorem says nothing about $\log|\mathcal A|$, multiplier
logarithms, multivalued potentials, or arbitrary changes of primitive.

## Frozen claim under attack

Let $F$, $\theta$, and $G$ be algebraic rational data over
$\overline{\mathbb Q}$ with

$$
F^*\theta-\theta=dG,
$$

where $G$ is single-valued and its additive constant is frozen in
$\overline{\mathbb Q}$.  Let $P\in X(\overline{\mathbb Q})$ satisfy
$F^n(P)=P$, and suppose the full orbit is regular for every evaluated datum.
Then

$$
\mathcal A_G(P)=\sum_{j=0}^{n-1}G(F^jP)
\in\overline{\mathbb Q},
$$

so it cannot be a logarithm of a nontrivial algebraic number.

## Audit matrix

| Attack | Does it break the frozen theorem? | Result |
|---|---|---|
| Transcendental additive constant | No; violates algebraic normalization. | Valid counterexample to the broader map-only claim. |
| Orbit-dependent target shift | No; violates frozen, target-independent normalization. | Valid leakage example. |
| Algebraic additive constant | No. | Action shifts by $nC$ but remains algebraic. |
| Distinct algebraic step constants $C_j$ | No, when all step and endpoint values are defined and algebraic. | Full shift is $\chi_n(P_n)-\chi_0(P_0)+\sum_jC_j$; compatibility removes the endpoint term. |
| Single-valued exact algebraic gauge | No. | Gauge terms telescope exactly. |
| Closed non-exact primitive change | Outside hypotheses. | Can carry nontrivial periods; no invariance claim is allowed. |
| Multivalued logarithmic gauge | Outside hypotheses. | Branch monodromy can survive the closed sum. |
| Orbit through a pole | Outside hypotheses. | Action is undefined or requires an extra regularization. |
| Complex logarithm branch | No. | Exponentiating removes the branch ambiguity. |
| Real part, imaginary part, or modulus | No. | Each remains algebraic. |
| Logarithm applied after the action | Outside conclusion. | $\log|\mathcal A|$ may equal $\log p$ if $|\mathcal A|=p$. |
| Algebraic but non-$S$-integral parameter | No for algebraicity. | Only the stronger $S$-integral conclusion is unavailable. |
| Hénon sign convention | No. | Type-1 action is exactly the negative of the exact-potential action. |
| Hénon denominator 3 | No. | It forces the statement $3\mathcal A$ is $S$-integral, not necessarily $\mathcal A$. |

## Attack 1: exploit the additive constant

Take $X=\mathbb A^2$, $F=\mathrm{id}$, and $\theta=p\,dq$.  Then

$$
F^*\theta-\theta=0.
$$

Every constant is a potential.  Choosing

$$
G\equiv\log 2
$$

makes every point a fixed point with action $\log 2$.  The map and primitive
are algebraic, and the orbit can even be algebraic, but the normalization of
$G$ is not algebraic.  Therefore:

- “algebraic exact-symplectic map implies algebraic absolute action” is
  false;
- “algebraic map, primitive, potential including its constant, and orbit
  imply algebraic action” survives;
- exactness alone never chooses the constant.

For a period-$n$ orbit with initial action $A$, the still sharper target
injection is

$$
C=\frac{\log p-A}{n}.
$$

It produces $A+nC=\log p$.  This is not a dynamical mechanism: it selects a
constant using both the orbit and the desired target.  The source lock
forbids it.

## Attack 2: hide the constant inside a gauge

Let

$$
\theta'=\theta+d\chi,
\qquad
G'=G+\chi\circ F-\chi+C.
$$

Direct cyclic summation gives

$$
\sum_{j=0}^{n-1}
\bigl(\chi(P_{j+1})-\chi(P_j)\bigr)=0,
$$

but the constant contributes $nC$.  Thus an exact gauge with $C=0$ cannot
hide a target.  An algebraic $C$ changes the numerical value but not its
arithmetic type.  A transcendental $C$ is exactly Attack 1 in different
notation.

This calculation uses a single-valued $\chi$ regular on the orbit.  If
$\chi=\log q$ is treated as multivalued, then $d\chi=dq/q$ may be algebraic
as a one-form even though branch continuation of $\chi$ acquires a multiple
of $2\pi i$.  Such monodromy is not a telescoping rational-function gauge
and is outside the frozen theorem.

Likewise, replacing $\theta$ by $\theta+\eta$ for a closed non-exact
one-form $\eta$ is not covered by $\eta=d\chi$.  Its periods require a
separate topological ledger.

For local or time-dependent one-step data,

$$
G'_j=G_j+\chi_{j+1}\circ F_j-\chi_j+C_j
$$

gives, before imposing endpoint compatibility,

$$
\sum_jG'_j(P_j)=\sum_jG_j(P_j)
+\chi_n(P_n)-\chi_0(P_0)+\sum_jC_j
$$

with no endpoint assumption.  When endpoint gauges match, the endpoint term
vanishes; the common formula $nC$ is the autonomous special case
$C_j=C$.  A defined algebraic endpoint mismatch and a collection of frozen
algebraic $C_j$ preserve algebraicity.  An undefined value, pole,
multivalued branch jump, or transcendental endpoint contribution stops the
absolute-action certificate.  A target-dependent collection whose total
shift is $\log p-A$ is the distributed form of target injection.

## Attack 3: use a pole, indeterminacy, or regularization

If $G=A/B$ and $B(P_j)=0$, the elementary evaluation proof cannot be
applied.  Assigning a principal value, subtracting a divergence, or choosing
a local branch introduces new analytic and normalization data.  This is not
a counterexample because regularity at every evaluated orbit point is a
frozen hypothesis.

The algebraicity of the periodic orbit is a sufficient assumption, not a
claim of necessity.  The audit does not infer a transcendental action merely
from a nonalgebraic point on a positive-dimensional periodic locus; exactness
may impose additional constancy there.

## Attack 4: exploit a complex branch or the modulus

Suppose an algebraic action $A$ equals a complex logarithm of an algebraic
$\beta\in\overline{\mathbb Q}^{\times}\setminus\{1\}$.  Every branch
satisfies $e^A=\beta$.  Since $A\ne0$,
Hermite--Lindemann makes $e^A$ transcendental, a contradiction.  The proof
does not choose a principal branch.

For $\beta=1$, the only algebraic logarithm is the trivial value $A=0$;
for $\beta=0$, no complex logarithm exists.

For $A\in\overline{\mathbb Q}$,

$$
\operatorname{Re}A=\frac{A+\overline A}{2},
\qquad
\operatorname{Im}A=\frac{A-\overline A}{2i},
\qquad
|A|^2=A\overline A.
$$

All three displayed real quantities are algebraic; the positive square root
defining $|A|$ is also algebraic.  None can equal the transcendental real
number $\log p$.

This does **not** show that $\arg A$ or $\log|A|$ is algebraic.  Indeed, if
an action happened to equal a positive rational prime, then
$\log|A|=\log p$.  The candidate tests the action itself, not a logarithm
applied after it.

## Attack 5: scale, average, or repeat the orbit

If $c\ne0$ is algebraic and $A=c\log p$, then
$\log p=A/c$ would be algebraic.  Thus algebraic scaling cannot evade the
obstruction.  The average $A/n$ and repetition $rA$ are also algebraic.
Comparing $rA$ with

$$
\log(p^r)=r\log p
$$

does not help.

A transcendental physical unit conversion is different: it lies outside
the algebraic normalization and scale hypothesis and must be treated as a
new source of the clock.

## Attack 6: break the Hénon formulas

For

$$
(Q,P)=H_a(q,p)=(q^2-a-p,q),
$$

the pullback calculation is

$$
H_a^*(p\,dq)=P\,dQ
=q(2q\,dq-dp),
$$

so

$$
H_a^*(p\,dq)-p\,dq
=(2q^2-p)\,dq-q\,dp
=d\left(\frac23q^3-pq\right).
$$

For

$$
L_a(q,Q)=\frac13q^3-aq-qQ,
$$

one obtains

$$
\partial_qL_a=q^2-a-Q=p,
\qquad
-\partial_QL_a=q=P.
$$

Substituting $Q=q^2-a-p$ gives

$$
L_a=pq-\frac23q^3=-G.
$$

The parameter $a$ cancels from the graph substitution; this is not an
omission.  Adding a constant to $L_a$ would restore the already audited
per-step normalization shift.

The cyclic indexing also survives the small-period edge cases.  For $n=1$,
$q_{j+1}$ and $q_{j-1}$ are both $q_j$, so the fixed-point equation is
$q^2-a-2q=0$.  For $n=2$, both neighbors of $q_0$ are $q_1$ and conversely,
so the recurrence correctly contains a coefficient two.  These are two
argument slots with equal values, not a set of neighbors to deduplicate.
The repeated indices do not affect the point-at-infinity argument.

## Attack 7: find a transcendental finite Hénon periodic point

The cyclic equations are

$$
q_j^2-a-q_{j+1}-q_{j-1}=0.
$$

Their projective homogenizations are

$$
Q_j^2-aZ^2-Q_{j+1}Z-Q_{j-1}Z=0.
$$

At $Z=0$, every $Q_j^2$ vanishes, forcing all projective coordinates to
zero.  Hence the projective solution set has no point at infinity.  A
positive-dimensional projective component not contained in the hyperplane
$Z=0$ must intersect that hyperplane by the projective dimension theorem.
Therefore the projective solution set is zero-dimensional.  Since it is
defined over $\mathbb Q(a)$ and $a$ is algebraic, every closed point has
algebraic coordinates.

This rules out the proposed attack for every finite periodic orbit.  It does
not classify periodic points at an indeterminacy of a compactification, and
none is used in the affine action certificate.

## Attack 8: break the $S$-integral refinement

Let $a\in\mathcal O_{K_0,S_0}$ and pass to a finite orbit field $K/K_0$
containing every coordinate.  Extend $S_0$ to all places $S$ of $K$ above
it.  At a non-archimedean place outside $S$, set

$$
R=\max_j|q_j|.
$$

If $R>1$ and $|q_j|=R$, then $|a|\le1$ implies

$$
|q_j^2-a|=R^2.
$$

The recurrence gives the contradictory upper bound

$$
|q_j^2-a|=|q_{j+1}+q_{j-1}|\le R.
$$

Thus all periodic coordinates are integral outside $S$.  However,

$$
\mathcal A_G
=\sum_j\left(\frac23q_j^3-q_{j-1}q_j\right)
$$

contains $1/3$.  The proof certifies only

$$
3\mathcal A_G
=\sum_j(2q_j^3-3q_{j-1}q_j)
$$

as $S$-integral.  The denominator at places above the rational prime 3 is a
real boundary, not a counterexample.  If $a$ is merely algebraic, the
algebraic-action theorem still holds but this valuation statement is not
asserted.

## Surviving theorem and rejected variants

### Survives

> A frozen single-valued algebraic rational potential, including its
> algebraic additive constant, has algebraic closed action on every
> algebraic periodic orbit where it is regular; hence that action cannot be
> any branch of the logarithm of a nontrivial algebraic number.

### Rejected or outside scope

- algebraic map alone canonically determines an algebraic absolute action;
- arbitrary analytic normalizations preserve the obstruction;
- all primitive changes telescope;
- multivalued logarithmic potentials are covered;
- the result excludes $\log|\mathcal A|$, multiplier logs, or return times;
- the Hénon action itself is always integral rather than integral after
  multiplication by 3;
- a finite low-period computation is evidence for the all-period claim.

## Explicit stop conditions

1. **Normalization stop:** do not compare an absolute action with $\log p$
   until every global, local, or step constant is frozen and algebraic.
2. **Primitive stop:** a primitive change known only to be closed is not an
   exact gauge; stop telescoping and record its period class separately.
3. **Branch stop:** a multivalued potential or gauge requires a branch and
   monodromy ledger.  Without one, the absolute action is not certified.
4. **Complex-observable stop:** algebraicity covers $\operatorname{Re}A$,
   $\operatorname{Im}A$, and $|A|$ themselves.  Stop before transferring the
   conclusion to $\arg A$ or $\log|A|$.
5. **Integrality stop:** for the frozen Hénon primitive, stop at
   $3\mathcal A_G$ being $S$-integral unless a separate divisibility proof
   removes the places above 3.
6. **Execution stop:** no candidate orbit or action is evaluated during the
   source-lock and counterexample-audit stage.

## Independence note and remaining gate

This document is a deliberately separate adversarial reconstruction, but it
was produced in the same source-lock workstream as the proof package.  It is
not represented as an external or second-person review.  A different agent
subsequently received only the frozen theorem, assumptions, and attack
checklist; its `REPAIR` report is preserved in
`notes/INDEPENDENT_COUNTEREXAMPLE_REVIEW.md`.  Source-lock v3 incorporates
those repairs before any candidate periodic point or action was computed.
