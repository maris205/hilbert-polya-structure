# TR8 nonauthor coordinator review

2026-09-08 UTC. Internal model review of the actual 451-line
[author proof](PROOF_PACKAGE.md), its complete
[source audit](SOURCE_AUDIT.md) and [freeze](FROZEN_ATTEMPT.md).
The coordinator did not author that proof and rederived the arguments
below. The coordinator had suggested testing a fixed-kick construction
before the author worked out the proof: this is not a blind review or
an independent discovery of the idea. It is not human peer review.

## Verdict and retained scope

**PASS for the three stated helper results**, with the external
height/equidistribution inputs stated in the proof. No mandatory
mathematical correction was found in those scopes.

- For every rational $c\le-16$, the exact witness algorithm terminates
  and returns distinct nonperiodic totally-real points with positive
  total canonical height at most the requested $2^{-j}$.
- For every rational $c>1$, the explicit rational lower bound applies
  to every totally-real algebraic point, with arbitrary degree and
  denominator.
- For each fixed rational $c$, a zero nonperiodic height infimum implies
  Zariski density of all small sublevel sets and full real support of
  the equilibrium measure. This implication is qualitative.

**Original TR7: NOT CLOSED.** The interval $-16<c\le1$, the full
decision procedure and a general effective positive bound remain
unproved. This review does not admit a smaller replacement contract,
clear worldwide novelty, or create a fourth/fifth paper.

## 1. Independent root count and native-clock check

For $a=-c\ge16$, setting $B=\sqrt a+2$ gives
$a-2B\ge4$ and $a+2B+1<B^2$. The sign-specific square-root map
therefore preserves the cube and has sup-norm Lipschitz constant
at most $1/2$. Different sign vectors give different nonzero-coordinate
solutions.

The finite algebra argument is stronger than numerical branch finding:
quadratic-to-linear reduction spans the quotient by $2^N$ squarefree
monomials. Evaluation at the $2^N$ already constructed solutions is
surjective by the Chinese remainder theorem. The matching upper/lower
dimension proves reducedness and exhausts every complex root. Rational
coefficients then make every conjugate real. No irreducibility or
single-Galois-orbit assumption is present.

I checked the sign of the closing perturbation directly. Native
recurrence at indices $1,\ldots,N-1$ gives $x_N=x_0$, while the
forced index-zero equation gives
$x_0^2-a-x_{N-1}=x_1+1$. Thus
$F_c^N(x_0,x_1)=(x_0,x_1+1)$, with the plus sign claimed.
$N\ge3$ avoids a doubled-neighbour ambiguity.

## 2. All-place bound and midpoint decay

At a finite place, a maximal coordinate in the cyclic system satisfies
$M_v^2\le\max(|a|_v,M_v,1)$. If
$M_v>\max(1,|a|_v^{1/2})$, every quantity on the right is strictly
smaller than $M_v^2$, a contradiction. The integral kick changes
no finite-place bound. Since $a=A/D$ is reduced,
the weighted finite-place contribution is at most $\frac12\log D$,
independently of the field degree. Each real conjugate and the kicked
endpoint are bounded by $B+1$.

The elementary inequality
$h(F_c^{\pm1}R)\le2h(R)+h(c)+\log3$ follows place by place.
Summing its geometric recurrence gives (2.1), without assuming a
lower comparison with naive height.

For $m=\lfloor N/2\rfloor$, the forward term at $Q_N=F_c^mP_N$
is bounded from the right endpoint with factor $2^{-(N-m)}$;
the backward term is bounded from the left endpoint with factor
$2^{-m}$. Both exponents in (4.3) are correct.
The integer $K_a=3A+D+10$ dominates the displayed logarithmic
constant using $A\ge16D$. All inequalities used to certify
$H_c(Q_N)\le2^{-j}$ are effective.

## 3. Nonperiodicity, positive height and distinctness

The positive fixed solution lies at or above
$\alpha=1+\sqrt{a+1}$, with $x_0>\alpha$. Its maximal displacement
$M$ satisfies $M(2\alpha+M-2)\le1$, so every coordinate is
strictly below $\alpha+1$. At the kicked endpoint,
$v=x_1+1>u=x_0>\alpha$. The recurrence gives
$w=v^2-a-u>v$ and retains this ordering. A finite increasing limit
would solve $L^2-2L-a=0$ with $L>\alpha$, which is impossible.
Hence the selected embedding escapes and the algebraic point is
not periodic.

Once a coordinate exceeds $\max(4,2\sqrt a)$, the forward escape
estimate is at least quadratic growth divided by two. This gives
a strictly positive forward Green function at that iterate, hence
at the initial point and midpoint by scaling. A positive contribution
at one actual embedding has positive global weight; no uniform
lower bound on that weight is needed for this positivity assertion.

The algebraic solution procedure is terminating at each $N$:
a separating rational linear form exists for a finite reduced
characteristic-zero algebra, and exact algebraic sign/equality
tests are decidable. Repeated points cannot block the outer
enumeration forever: each previously selected point has strictly
positive height and the uniform candidate upper bound tends to zero.
No computation of an exact canonical height is required by the
duplicate filter. This is an effective existence algorithm, not
a claim of practical running time.

## 4. The entire positive-parameter region

For $c>1$, the chosen
$R=2\lceil c\rceil+4$ satisfies $R\ge4$ and $R\ge2\sqrt c$.
If a complex pair has norm $T\ge R$, one of the forward/backward
dominant coordinates has next modulus at least
$T^2-T-c\ge T^2/2$. Iteration proves the Green lower estimate
$\log(T/2)$ in the appropriate direction, including tied coordinates.

If the real total local Green function were below
$2^{-M}\log(R/2)$, all states with $|n|\le M$ would have norm below
$R$. The identity
$$
x_M+x_{-M}-2x_0
=\sum_{i=-M+1}^{M-1}(M-|i|)\Delta^2x_i
$$
has weight sum $M^2$, and $\Delta^2x_i=(x_i-1)^2+c-1\ge c-1$.
The defining strict inequality $(c-1)M^2>4R$ contradicts the
coordinate bound. Averaging over all real conjugates retains the
same bound because the archimedean weights sum to one. The rational
choice $2^{-(M+1)}$ is smaller since $\log(R/2)>\frac12$.
There is no hidden degree or integrality restriction.

## 5. Exceptional-curve saturation and source applicability

The descending Zariski closures of the small sublevel sets stabilize
because affine space is Noetherian. The one-step inequalities in
both time directions show that the stable closure is invariant.
Its one-dimensional components, if any, would be permuted and
yield an invariant curve for a positive iterate. The no-invariant-curve
theorem applies to each Hénon-type iterate. A proper invariant
zero-dimensional closure is finite and consists of periodic points,
contradicting the nonperiodic sublevel set it contains. Thus density
is proved for every sublevel set, not assumed for the sequence.

The max/sum comparison
$h_{G_c}\le H_c\le2h_{G_c}$ is pointwise and has no additive
constant. The regular pair has degree two in each direction and
disjoint indeterminacy points. Finiteness in Lee's Definition 1.1
also follows directly from the inverse polynomial height estimate:
$h(P)\le2h(F_cP)+C_c$, and the analogous inverse inequality.
Thus its height-ratio limsup is at most two; Lemma 7.3 gives the
regular-automorphism formulation as well.

The source's zero variety height makes the extracted generic
sequence small for the adelic metric, rather than merely bounded.
Weak limits of Galois measures supported on the closed real
projective plane remain supported there. The identified equilibrium
measure has no mass at infinity. This proves the claimed implication,
but no converse or effective support test.

## 6. Primary-source checks actually performed

The coordinator opened the three cited primary PDF bodies and checked
the affected theorem statements/normalizations:

- [Ingram](https://arxiv.org/pdf/1111.3609), section 2 and Lemma 2.1:
  arbitrary nonzero coefficient, local limits and scaling.
  The explicit conjugacy $L F_c L=(-y,x+y^2+c)$ has coefficient
  $-1$ and preserves the height; no coefficient-$+1$-only arithmetic
  conclusion is imported.
- [Dujardin–Favre](https://arxiv.org/pdf/1405.1377), Propositions
  1.6–1.7: local Green functions and the no-invariant-curve statement.
  The Bedford–Smillie original proof is credited through this
  primary paper, not separately claimed as read.
- [Lee](https://arxiv.org/pdf/1203.1224), Definition 1.1, Theorem B,
  Theorem 6.5 and its sup-norm construction, Lemma 7.3, Corollary
  7.5, and the final archimedean measure identification.
  This verifies generic small-point applicability, not only
  periodic-point equidistribution.

No full-paper reading or new novelty search is claimed for this helper
review. Direct opens/finds are not additional search-query submissions.
The classical dependencies remain external theorem inputs, not
reproved general results.

## 7. Final boundaries

Mathematical executions and old reruns: **0**. This review used
hand derivations and source reading, not finite-height or finite-period
certification. The witness algorithm has not been implemented/run.
No new correction to the author proof was necessary.

The prospective review/source requirements were applied via
research-review with the repository-authorized current-team fallback;
the unavailable external GPT-5.4 MCP workflow did not run.
The batch skill retains the whole TR7 contract. No paper/PDF,
formal evaluation, target Euler factor or A2 advancement follows
from this helper PASS. NO_BAD_EULER_OR_ROOT_NUMBER.
