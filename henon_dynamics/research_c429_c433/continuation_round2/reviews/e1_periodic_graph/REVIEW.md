# Round 2 E1 — independent periodic-transfer graph review

2026-09-09 UTC. Current-session nonauthor internal review at the assigned
model/reasoning setting. This is not human peer review or paper admission.

## Verdict

**PROVABLE AS STATED. Mathematical/source must-fixes: 0.**

The native-periodic complexity theorem in
[A2's report](../../a2_algebraic_transfer/REPORT.md), lines 80–95 and
proof lines 118–219, is correct. For the stated finite graph over ordinary
periodic points, a non-coboundary modulo constants satisfies

$$N\le D+d_TD^3.$$

The strict converse threshold forces $h=\Delta Q+\beta$; the original
all-ordinary-cycle condition forces $\beta=0$. The claimed sufficient
growth condition $D_j=o(N_j^{1/3})$ is therefore valid for fixed $f,h$.
It has **not** been deduced from ordinary cycle vanishing. PC424-L remains
open exactly as the author reports. This is a complete quantitative
auxiliary improvement to the same A1/A2 question, not a second paper or a
completion of the finite-transfer existence bridge.

Numbered must-fix list: **none**. In particular, no finite test, rank
calculation, or speculative construction is needed to validate the bound.
The application boundaries in Sections 5–6 below must remain attached to
it; the inspected report already respects them.

## Actual inspection and dependency boundary

Read the entire 301-line Round 2 author report, including its frozen
question, complete proof, growth criterion, source subtraction and handoff.
Also read the actual relevant source statements/proofs:

- [First-pass A2 supplement](../../../lanes/a2_transfer_bridge/PROOF_SUPPLEMENT.md),
  Section 3, its assumptions and Section 4: the old threshold
  $N>2^D d_TD^4$, finite-fiber loss, periodic-component extraction, and
  one-step constant removal.
- [R6 descent](../../../../research_c424_c428/continuation_round6/positive_characteristic/PROOF_AND_GAPS.md),
  exact theorem and Sections 1–7: degree prime to the characteristic,
  finite compatible field embedding, rational-pole removal, separable and
  purely inseparable descent. This remains an imported proved theorem;
  its application is checked here, not claimed as new.
- [First-pass A1 report](../../../lanes/a1_periodic_coboundary/REPORT.md),
  Section C: finite-field coefficient descent, interpolation, and its
  explicit failure to supply a uniform degree bound.
- [First-pass E4 review](../../../reviews/e4_covers/REVIEW.md), A2 audit,
  and [first-pass disposition](../../../FIRST_PASS_DECISION.md): ownership
  and the prior open-existence boundary, not substitutes for the actual
  proof passages above.
- Author-hosted [Milne, Algebraic Geometry, Theorem 6.37](https://www.jmilne.org/math/CourseNotes/AG.pdf),
  printed pages 152–153 (PDF pages 151–152, zero-based), statement and
  displayed proof. Its relevant input is the classical product-of-degrees
  upper bound on distinct affine intersections of curves without a common
  component. It is valid in the positive characteristic used here.

The updated Hénon guidance and `CONTINUOUS_RUN.md` were read. The
research-review and proof-writer skills supplied independent checking,
explicit hypotheses and honest open/proved separation. Their older external
model default is superseded here by the authorized current-session internal
review, with no external upload. All first-pass sources remained read-only.

## 1. The finite graph really is a permutation

Locator: author proof §1, lines 120–125.

Let $S$ be a finite union of ordinary primitive $f$-orbits. The restriction
$f|_S$ is a permutation, including when a primitive length is divisible by
$p$. The single-valued graph projection
$\Gamma\to S$, $(a,U(a))\mapsto a$, is a bijection. The assumed identity
$U(f(a))-U(a)=h(a)$ makes this projection conjugate $T|_\Gamma$ to
$f|_S$. Thus $T|_\Gamma$ is a permutation and, for every finite subset
$A\subseteq\Gamma$ and every $r\ge0$,

$$|T^r(A)|=|A|.$$

This does not assert that $T$ is globally injective; it usually has two
geometric preimages. Nor does it infer injectivity from forward invariance
alone. It uses precisely the periodic-base hypothesis absent from the
first-pass general finite-functional-graph theorem.

When $h\in K_c$, the existence of $U$ on each selected ordinary orbit is
the old cumulative-sum construction: choose an initial value and add the
successive $h$-values. Vanishing of the sum makes the assignment close up.
There is no division by the orbit length, so wild lengths cause no problem.
For the auxiliary theorem itself, $U$ is an explicit hypothesis; full
membership $h\in K_c$ is not needed until the constant-removal step.

## 2. Components, vertical exceptions and the directed graph

Locator: author proof §1, lines 127–141, and §2, lines 165–168.

Replacing $P$ by its squarefree product preserves its zero set and cannot
increase degree. Over the algebraically closed field, a vertical
irreducible plane-curve component is a line $X=a$. It contains at most
one point of the single-valued graph $\Gamma$. Hence at most $D$ graph
points need be charged to all vertical components, even if some are also
on nonvertical components.

For a nonvertical irreducible component $C_i$, the restriction of $X$ is
nonconstant. Its image under the first coordinate $f(X)$ is still
nonconstant: otherwise the function $X$ would be algebraic over $k$ and
hence constant. Thus $T(C_i)$ is not a point or a subset of a vertical
line. Its closure is one irreducible nonvertical curve. If its image were
contained in two distinct components of $Z(P)$, that curve would lie in
their finite intersection, a contradiction. Therefore the containment
graph has outdegree at most one.

The absence of a containment edge does **not** assert that no individual
graph point maps into another component. Such exceptional pointwise
transitions are precisely what the terminal Bézout argument counts.
If the finite directed graph has no cycle, following the unique outgoing
edge, when present, reaches a terminal vertex in finitely many steps.
No disjointness of components, uniqueness of a component containing a
graph point, or injectivity of the component map is assumed.

## 3. A directed cycle gives the R6 input with the right native equation

Locator: author proof §2, lines 145–163.

A directed cycle gives a nonvertical irreducible curve $C$ and a dominant
self-map $T^r:C\to C$, for some $r\ge1$. Nonverticality makes $k(C)$ a
finite extension of $k(x)$: its transcendence degree is one, and the
remaining coordinate is algebraic over $k(x)$. Dominance gives an
injective pullback fixing $k$, with

$$\tau(x)=f^r(x),\qquad \tau(y)-y=S_rh(x).$$

This is an actual compatible finite field object, not a relation on
unrelated fibers. Singularities of $C$ do not prevent the function-field
construction. The extension need not be separable; R6 includes that case.
Its base degree is $2^r$, prime to the odd characteristic, regardless of
whether $p$ divides $r$. All R6 hypotheses match.

R6 gives $y=Q(x)$, $Q\in k[x]$, and
$\Delta_{f^r}Q=S_rh$. Applying $\Delta_f$ and using commuting pullbacks
gives

$$\Delta_{f^r}(h-\Delta_fQ)=0.$$

A nonconstant polynomial cannot be invariant under $f^r$, since its
degree would be multiplied by $2^r>1$. Thus $h-\Delta_fQ=\beta\in k$.
There is no division by $r$. In fact $r\beta=0$ also follows from the
summed equation, but when $p\mid r$ this does not remove $\beta$ and
must not replace the fixed-point argument.

Under $h\in K_c$, choose a root $a$ of $f(X)-X$ in $k$. Its ordinary
orbit has length one, even if that root is scheme-theoretically multiple.
Then $0=h(a)=\beta$. This restores the original one-step transfer, not a
changed clock or an averaged iterate equation.

## 4. Terminal Bézout count and overlap-safe summation

Locator: author proof §§3–4, lines 172–214.

For a terminal component $C_t$, every $z\in\Gamma\cap C_t$ satisfies
$P(Tz)=0$. The polynomial $P\circ T$ is nonzero because $T$ is dominant:
over $k$, solve $x^2+c=a$ and then $y=b-h(x)$ for any target $(a,b)$.
Also $\deg(P\circ T)\le d_TD$, with the stated convention $d_T=2$
for zero or constant $h$.

If $P\circ T$ vanished identically on $C_t$, the irreducible nonconstant
image would lie in one component of $Z(P)$. That component cannot be
vertical, and a nonvertical target would give an outgoing edge. This
contradicts terminality. Therefore $C_t$ and $Z(P\circ T)$ have no
common curve component, and the classical distinct-point Bézout bound is

$$M_t:=|\Gamma\cap C_t|\le d_t\deg(P\circ T)\le d_t d_TD.$$

Projective closure does not introduce a common curve at infinity: the
closure of the affine irreducible $C_t$ is not the line at infinity.
Repeated factors, nonreduced intersections and critical points can only
increase intersection multiplicities; counting distinct affine points
still gives the claimed upper bound.

For each nonvertical $C_i$, its containment path of length $r_i$ sends
$\Gamma\cap C_i$ into $\Gamma\cap C_{t(i)}$. The permutation property
preserves the cardinality of this image, so
$|\Gamma\cap C_i|\le M_{t(i)}$ without the old exponential fiber loss.
Now use $s\le D$ and $d_t\le D$:

$$
N\le D+\sum_{i=1}^s|\Gamma\cap C_i|
 \le D+d_TD\sum_{i=1}^s d_{t(i)}
 \le D+d_TD(sD)
 \le D+d_TD^3.
$$

Different starting components can reach the same terminal component, and
different components can share graph points. Both phenomena only overcount
the union in this inequality. The proof never claims disjointness or
replaces the sum by an unjustified exact equality. The constant is coarse,
not claimed sharp; its strict-threshold contrapositive is valid as written.

## 5. Degenerate cases and a discriminating exact boundary example

- $N=0$ is harmless. A nonzero constant polynomial can vanish on $\Gamma$
  only in this case. Its empty factor list causes no issue for the bound.
- The theorem states $D\ge1$. If one separately allows $D=0$, the only
  admissible nonzero equation is constant and forces $N=0$; there is no
  positive-graph conclusion. The zero polynomial must remain excluded.
- If there are no nonvertical components, all graph points are already
  covered by at most $D$ vertical lines. The empty DAG and empty sum are
  valid.
- A component already terminal has path length zero. A self-edge is a
  directed cycle and is handled by R6, not by terminal counting.
- $h=0$ is already a coboundary. Nonzero constant $h$ belongs to $B_c+k$
  but not to $B_c$; the auxiliary conclusion is deliberately only modulo
  constants without the full orbit hypothesis.

The last distinction has an exact unbounded-graph control, requiring no
program. Fix an odd $p$, let $f=x^2$ and $h=1$. For $r\ge1$, choose a
primitive $(2^{p^r}-1)$st root of unity $\zeta\in k$. This exists because
$2^{p^r}-1\equiv1\pmod p$. The $f$-orbit of $\zeta$ has least period
$p^r$: for $0<j<p^r$, the positive integer $2^j-1$ is smaller than
$2^{p^r}-1$ and cannot be divisible by it.

On this orbit define $U(\zeta^{2^j})=j\bmod p$. It satisfies the
one-step equation, including the closing step, and its graph lies on
$Y^p-Y=0$, of total degree $D=p$. Thus $N=p^r$ becomes arbitrarily
large while $D$ stays fixed, but $h=1$ is not a polynomial coboundary:
the difference of a nonconstant polynomial has positive degree, and a
constant has difference zero. This example confirms why the theorem's
$+\beta$ is necessary and why a cyclic component need not be one-step
stable. It is **not** a PC424-L counterexample, since every fixed point
has orbit sum $1\ne0$.

## 6. The growth criterion is sufficient, but its existence is still missing

Locator: author report lines 221–258 and 282–287.

For fixed $f,h$, $d_T$ is fixed. If the selected graphs have
$N_j\to\infty$ and equations with $D_j=o(N_j^{1/3})$, then

$$\frac{D_j+d_TD_j^3}{N_j}\longrightarrow0.$$

Hence one sufficiently large graph satisfies the strict theorem threshold.
For $h\in K_c$ it supplies an actual polynomial $Q$, and then the fixed
relation $Y-Q(X)=0$ is available for suitably chosen subsequent transfers.
No limit of the equations $P_j$, compatibility of the graphs $U_j$, or
stabilization of their coefficients is required.

The numerical growth requirement on a *selected sequence* permits
unbounded $D_j$, unlike an advance uniform bound. Under the orbit
hypothesis, however, existence of some such successful sequence and
existence of a polynomial transfer are equivalent via the proved theorem;
the report does not exhibit a new class of solutions strictly between
those alternatives. Its phrase “weaker sufficient regularity condition”
should be read in this numerical-input sense, not as an unproved strict
logical separation of the existential properties.

For a hypothetical defect $h\in K_c\setminus B_c$, the contrapositive
applies to **every** selected finite union, every transfer and every
nonzero relation. Since $D\le D^3$ for $D\ge1$,

$$D\ge\left(\frac{N}{d_T+1}\right)^{1/3}.$$

General bivariate interpolation is compatible with this obstruction:
the vector space of polynomials of degree at most $D$ has dimension
$(D+1)(D+2)/2$, so elementary dimension counting only guarantees a
nonzero relation after this exceeds $N$, at order $N^{1/2}$, not
$o(N^{1/3})$. Degree one in $Y$ alone does not control total degree.

An important domain boundary is that **$N$ is the number of actual ordinary
periodic points in the chosen base set**. A full finite field generally
contains preperiodic tails. One cannot simply put $N=q^r$ in the new bound
because the first-pass theorem allowed the entire functional graph on
$\mathbb F_{q^r}$. Restrict to genuine cycles and use their actual
cardinality. The author explicitly uses growing finite unions of cycles,
so no correction is needed on this point.

## 7. Source subtraction and allowed handoff

The genuine new deduction is the use of the finite periodic graph's
permutation structure together with the terminal-component DAG to improve
the first-pass exponential threshold to a cubic one on this domain.
Bézout, irreducible-component arguments and R6's periodic-curve-to-polynomial
descent are inherited. The new theorem should not replace the old theorem
on arbitrary finite forward-invariant sets without its extra periodicity
hypothesis.

Finite-field coefficient descent is already in A1 Section C. The associated
coherent reduced-profinite construction is a compactness consequence of
the same old input: each finite solution set is nonempty and finite; for
finitely many compatibility constraints, choose a common multiple of the
extension degrees and restrict a solution there. This gives the finite
intersection property, even when individual restriction maps are not
surjective. It produces an inverse-limit element, not a finite extension
of $k(x)$, a low-degree algebraic relation, or the embedding required by
PC424-L. The author correctly subtracts this route.

Allowed output: the exact finite threshold and its contrapositive;
the sufficient sub-cube-root criterion for fixed $f,h$; the resulting
polynomial transfer **conditional on an actual qualifying graph equation**.
Not allowed: asserting that ordinary cycle sums, coefficient-field descent,
finite degree slices, compactness, or a relation of bounded $Y$-degree
already furnish that equation. No such missing existence theorem or
all-orbit counterexample is supplied in the inspected report.

**Disposition:** accept the bound as an independently checked auxiliary
interface for the unchanged PC424-L investigation. Keep original
$K_c=B_c$ and finite-algebraic-transfer existence **OPEN**. No independent
paper, target Euler factor, root number, automorphy, zero correspondence,
or Hilbert–Pólya conclusion follows.

Execution/write receipt: no mathematical program, old certificate rerun,
PDF/build, author/shared/evaluator modification, Git action, external model
call or nested agent. The only new write is this assigned Round 2 review
file. First-pass files and earlier reviews were not modified.
