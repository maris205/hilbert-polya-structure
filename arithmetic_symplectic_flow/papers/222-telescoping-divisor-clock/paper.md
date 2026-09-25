# A divisor-scan roof stops at an exact logarithmic offset

**Paper ID:** 222-telescoping-divisor-clock  
**Candidate ID:** ASFS-20260918-TDC01  
**Date / status:** 2026-09-18; STOP — TELESCOPING ROOF HAS THE OFFSET log 2; NO PRIME-LOG CLOCK.  
**Route state:** Exact owner-level geometry, complete periodic ledger and clock
audit only; formal Route coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

We freeze an all-integer Hénon-form symplectic map whose cyclic phase executes
one proper-divisor test per step. A nonnegative cycle-sum identity proves that
its complete periodic set consists of one primitive orbit per prime and no
composite orbits. The universal adjacent-integer roof
\(\tau(n,d)=\log((d+1)/d)\) is positive and gives a complete suspension on the
full retained carrier. However, the frozen scan starts at \(d=2\), not at 1.
For every prime \(p\ge3\), its actual roof sum is \(\log(p/2)\), not
\(\log p\). The \(n=2\) empty-scan sentinel has time \(\log2\), so it does not
remove this offset. The initially hoped-for exact prime clock is therefore
refuted without changing the card. The ordinary orbit product is recorded
only as a direct ledger control and is not the prime Euler product.
The analogous adjacent-ratio timing with an initialization interval is already
an engineered-clock control in package 160; neither that result nor its clock
can be transferred here. All surviving monodromies are unipotent, so no
nondegenerate periodic-point trace formula is supplied.

## 1. Frozen identity and same-object ledger

The [version-1 card](candidate-card.md) froze
\[
D_2=\{1\},\qquad D_n=\{2,3,\ldots,n-1\}\quad(n\ge3),
\]
with cyclic successor \(d^+\). For \(n=2\), \(d=1\) is an empty-scan sentinel,
not a divisor test. Put
\[
h(n,d)=\mathbf1_{\{2\le d<n,\ d\mid n\}},
\qquad \tau(n,d,q,p)=\log\frac{d+1}{d}.
\tag{1}
\]
The complete carrier and map are
\[
M=\coprod_{n\ge2,\ d\in D_n}\mathbb R^2_{n,d},\qquad
\omega|_{\mathbb R^2_{n,d}}=dq\wedge dp,
\]
\[
F(n,d,q,p)=\bigl(n,d^+,p,\;2p-q+(p-1)^2+h(n,d)\bigr).
\tag{2}
\]
The flow is the translation suspension on
\[
X_\tau=\{(z,t):z\in M,\ 0\le t\le\tau(z)\}/
((z,\tau(z))\sim(Fz,0)).
\tag{3}
\]

| Item | Owner in ASFS-20260918-TDC01 | Status / boundary |
| --- | --- | --- |
| Phase space | Full countable union of all integer/phase real planes | Frozen; disconnected and noncompact |
| Base map | Exact polynomial map (2) | Global symplectomorphism proved below |
| Arithmetic action | One local proper-divisor witness per phase | Same map executes every witness; no prime table |
| Source lineage | Prime/composite exclusion -> sequential scan -> Hénon-form lift | Constraint deformation, not a causal-sieve conjugacy |
| Roof / flow | Exact ratio (1), endpoint-glued flow (3) | Complete; actual prime times below |
| Primitive ledger | All real periodic states modulo cyclic phase | Complete classification; no centre selection |
| Stability | Derivative of (2) on those states | Unipotent; all repeated trace denominators vanish |
| Scalar product | Ordinary unweighted product from the actual lengths | Local control only; no Euler-product identity |
| Measure | Componentwise symplectic area | No finite trace normalization |
| Operator / later owner | No transfer, Hilbert, Hamiltonian/contact or quantum object | NOT SUPPLIED / DEFERRED |

The prior-work connection is the local prime/composite admissibility
constraint, as described in the [lineage guide](../../docs/prior_work/README.md).
Every proper-divisor test affects the same conservative recurrence. No
phase-space component is prefiltered by primality. This is a separate object
from [145's dyadic-batch map](../145-convex-witness-henon-sieve/paper.md):
the serial phase set and variable roof have changed, so its proof obligations
are proved afresh.

## 2. Question, strongest claim, and decisive stop

The question is whether the frozen serial scan and adjacent-ratio roof supply
an exact prime-log suspension clock. The answer is **no**: the telescoping
normalization is
\[
\prod_{d=2}^{p-1}\frac{d+1}{d}=\frac p2.
\tag{4}
\]
The initial audit draft incorrectly wrote \(p\) on the right. The readback
audit caught the missing lower-end factor; this package preserves the
unchanged object and records the correction as a decisive clock stop.

The strongest positive result is a complete two-dimensional symplectic base,
complete three-dimensional suspension, and prime-only full periodic ledger
with exact lengths \(T_2=\log2\) and \(T_p=\log(p/2)\) for \(p\ge3\).
The flow is not itself claimed symplectic or Hamiltonian. Natural arithmetic
timing, an operator trace, a determinant, target-divisor evidence and formal
Route coordinates are not established.

## 3. Geometry and non-Zeno proof

### Proposition 1 — Full global symplectic diffeomorphism

The map (2) is a smooth symplectomorphism of the full carrier.

**Proof.** A countable disjoint union of planes is a Hausdorff second-countable
smooth two-manifold. Given \((n,d',Q,P)\), let \(d\) be the cyclic predecessor
of \(d'\). The inverse is
\[
F^{-1}(n,d',Q,P)
=\bigl(n,d,\;2Q+(Q-1)^2+h(n,d)-P,\;Q\bigr).
\tag{5}
\]
Both directions are polynomial on each component. With
\(Q=p,\ P=2p-q+(p-1)^2+h(n,d)\),
\[
dQ\wedge dP=dp\wedge(-dq+2p\,dp)=dq\wedge dp.
\]
The component permutation preserves this equality globally. QED.

### Proposition 2 — Complete variable-roof flow

The flow (3) is defined for every real time on every full state.

**Proof.** The label \(n\) is conserved. For \(n=2\), every roof is \(\log2\).
For \(n\ge3\),
\[
\tau(n,d)\ge\log\frac n{n-1}>0.
\tag{6}
\]
Hence the sum over \(N\) forward or backward crossings is bounded below by a
fixed positive multiple of \(N\) along each orbit. Finite elapsed time uses
only finitely many globally defined iterates of \(F\) or \(F^{-1}\).
Unbounded continuous coordinates do not cause finite-time escape because
the roof depends only on the finite phase set for that conserved \(n\).
The roof is smooth componentwise; gluing its endpoint collars gives the
usual smooth suspension. QED.

The global infimum of the roof over all \(n\) is zero, but this does not create
Zeno behavior along a fixed orbit. This distinguishes the present object from
[155's state-dependent derivative-roof stop](../155-derivative-roof-completeness-test/README.md).

## 4. Full intrinsic periodic ledger and actual clock

### Proposition 3 — Exactly one primitive packet per prime

The complete periodic set is
\[
\operatorname{Per}(F)=\{(2,1,1,1)\}\cup
\{(p,d,1,1):p\ge3\text{ prime},\ d\in D_p\}.
\tag{7}
\]
For \(p\ge3\), the least base period is \(p-2\), and the \(p-2\) phase points
form one primitive orbit. For \(p=2\), there is one fixed point. No composite
or other real state is periodic.

**Proof.** Along a period-\(m\) orbit, write the position coordinates as
\(q_t=x_t\), so the second coordinate is \(p_t=x_{t+1}\). Equation (2) gives
\[
x_{t+2}-2x_{t+1}+x_t=(x_{t+1}-1)^2+h(n,d_t).
\]
Summing around the cycle yields
\[
0=\sum_{t=0}^{m-1}(x_{t+1}-1)^2+\sum_{t=0}^{m-1}h(n,d_t).
\tag{8}
\]
Every term is nonnegative, so all \(x_t=1\) and every visited witness
vanishes. A return of the phase forces \(m\) to be a multiple of \(|D_n|\);
therefore the whole phase set is visited. For \(n\ge3\), witness vanishing
is precisely absence of proper divisors \(2\le d<n\), equivalent to \(n\)
prime. For \(n=2\), the sentinel has no witness. Conversely the states in
(7) follow the cyclic phase and return. The phase itself excludes a shorter
period. This examines every real coordinate and every momentum, rather than
choosing centres from a larger periodic set. QED.

### Proposition 4 — Offset clock and repetitions

There is one oriented primitive closed flow orbit \(\gamma_p\) per prime,
and its actual lengths are
\[
T_2=\log2,\qquad T_p=\log(p/2)\quad(p\ge3).
\tag{9}
\]
Its \(r\)-fold repetition has length \(rT_p\), with no additional packet
multiplicity.

**Proof.** The complete base ledger and the complete positive-roof suspension
give the usual correspondence between primitive base cycles modulo cyclic
phase and oriented primitive flow orbits. Reversal is not a second orbit
of this fixed oriented flow. For \(p\ge3\),
\[
T_p=\sum_{d=2}^{p-1}\log\frac{d+1}{d}
=\log\frac32+\log\frac43+\cdots+\log\frac p{p-1}
=\log\frac p2.
\]
For \(p=2\), the frozen singleton roof is \(\log2\).
Repeated traversal of the same primitive cycle repeats the roof sum, proving
\(T_{\gamma_p^r}=rT_p\). QED.

The difference \(T_p-\log p=-\log2\) persists for all odd primes. No fixed
positive time rescaling makes these lengths exactly \(\log p\): the ratio
\(T_p/\log p\) tends to 1, forcing such a rescaling to equal 1, which leaves
the nonzero offset. This disproves the exact clock target, not logarithmic
asymptotic order. Adding the absent \(d=1\) phase would define another object.

### Proposition 5 — Degenerate monodromy

At each periodic state, the derivative is
\[
A=\begin{pmatrix}0&1\\-1&2\end{pmatrix}=I+N,\qquad N^2=0.
\]
Writing \(L_2=1,\ L_p=p-2\) for \(p\ge3\), the primitive monodromy and its
repetitions are \(P_p=I+L_pN\) and \(P_p^r=I+rL_pN\). Hence
\[
\det(I-P_p^r)=0
\]
for every prime and positive repetition. These formulas follow directly from
the derivative of (2); they are not borrowed from 145. The usual
nondegenerate periodic-point flat-trace denominator is therefore unavailable.
This is a scoped obstruction to that formula, not a no-go for every
distributional or regularized trace construction.

## 5. Scalar product as an actual-clock control

The ordinary unweighted product associated with (9), if recorded as a direct
ledger consequence, is
\[
Z_{222}(s)=(1-2^{-s})^{-1}
\prod_{\substack{p\ {\rm prime}\\p\ge3}}
\left(1-(p/2)^{-s}\right)^{-1},\qquad \Re s>1.
\tag{10}
\]
Its logarithmic series converges absolutely and normally there. No function
space, transfer operator, trace, Fredholm determinant or analytic continuation
is supplied. Equation (10) is not the prime Euler product and is not used to
advance A2 after the clock stop.

## 6. Controls, prior collision, and naturalness boundary

| Control | Exact observation | Consequence |
| --- | --- | --- |
| Remove every witness \(h\) | Every integer has a central phase cycle | Divisibility affects the intrinsic return ledger |
| Shift the test to \(\mathbf1_{d\mid n+1}\) | For \(n\ge3\), cycles select \(n+1\) prime | Arithmetic relation is a design choice, not uniquely forced geometry |
| Unit roof on the same base | Prime times become \(p-2\) for \(p\ge3\) | No old unit-clock conclusion transfers |
| Exact lower-end roof audit | Product of ratios is \(p/2\), not \(p\) | Decisive exact-clock stop; no added phase |
| Every noncentral state retained | Equation (8) forces the complete periodic set | No centre selection or omitted periodic family |
| Same derivative owner | Every repeated monodromy has eigenvalue 1 | No nondegenerate trace formula credit |

The closest clock control is
[160 — source-geometric return clock](../160-source-geometric-return-clock/README.md).
It already includes \(d=1,\ldots,n-1\), uses the same adjacent-ratio roof
with an explicit dilation/reset assumption, and obtains exact \(\log n\) scan
times on a different cotangent map. Its source-clock naturalness is explicitly
OPEN and promotion is stopped. Neither its extra phase nor its exact clock is
borrowed here.

For \(n\ge3\), put \(H(n,d)=\log d\). Then on every serial phase edge
\[
\tau(z)=H(Fz)-H(z)+\mathbf1_{\{d=n-1\}}\log(n/2).
\tag{11}
\]
Thus the chosen positive timing can be concentrated at the reset edge; local
ratios alone do not derive a natural arithmetic clock.

## 7. Gate assessment and decision

| Gate | Exact evidence | Status / boundary |
| --- | --- | --- |
| P0 | Global inverse, symplectic form, full carrier and complete positive roof | Geometry/flow established |
| A0 | Local divisor witnesses alter recurrence; no prime-selected domain | Bounded arithmetic mechanism; source-clock naturalness OPEN |
| A1 | Complete prime-only packets and repetitions | Owner-level ledger established; exact prime-log clock SCOPED FAIL |
| A2 | Actual-clock scalar product only | NOT ADVANCED; no operator/trace owner |
| Formal Route / B | No formal target/divisor evaluation | UNASSIGNED / NOT INVOKED |

**Portfolio: stop / fork.** The decisive gate is the exact clock offset in
(9); the frozen object remains unchanged. Retain the geometry and complete
ledger as reusable controls. A future \(d=1\) initialization proposal needs
a new candidate and must confront the naturalness boundary in 160.

## Reproducibility and evidence

All proofs are exact full-state arguments, not finite numerical evidence.
See the [card](candidate-card.md), [claim ledger](claim-ledger.md), and
[evidence record](evidence/README.md). No numerical run or GPU use was needed.
