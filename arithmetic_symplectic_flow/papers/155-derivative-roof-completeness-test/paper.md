# Derivative-generated time and a finite-time escape obstruction

**Paper ID:** 155-derivative-roof-completeness-test  
**Candidate ID:** ASFS-20260915-DRC01  
**Date:** 2026-09-15  
**Status:** STOP — POSITIVE DERIVATIVE ROOF HAS FINITE-TIME ESCAPE.

**Route state:** P0 clock/completeness screen only; A0--A2 are not advanced.
Formal Route coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

The logarithm of a configuration derivative is an intrinsic observable,
but need not define a complete suspension clock. We freeze that proposed
roof over an all-integer divisor-witness cotangent map. It is smooth and
strictly positive on the entire real carrier. In the n=2 fibre, however,
positive configuration states grow at least linearly while their roof
values decay at least exponentially. The sum of all forward return times
is finite. An explicitly defined continuous observable on the glued space
diverges along the trajectory, excluding an endpoint or continuous
extension within that space. The prime central cycles retain well-defined
finite roof sums, but this partial observation cannot supply the required
full-state complete flow. The candidate stops at P0 without analytic or
Route credit.

## 1. Frozen identity and same-object ledger

The [version-1 card](candidate-card.md) was frozen before this audit.
For every n>=2 set

\[
K_n=\max(1,\lfloor\log_2(n-1)\rfloor),\qquad
b(n,k)=\sum_{\substack{2^k\le d<2^{k+1}\\d<n}}1_{\{d\mid n\}},
\quad 1\le k\le K_n.
\tag{1}
\]

Let k^+ denote the cyclic successor, and take the full carrier

\[
M=\coprod_{\substack{n\ge2\\1\le k\le K_n}}\mathbb R^2_{n,k},
\qquad \omega|_{M_{n,k}}=dq\wedge dp.
\]

The map and the new roof are

\[
f_{n,k}(q)=q+\tfrac12\tanh q+K_nb(n,k),
\]
\[
F(n,k,q,p)=
\left(n,k^+,f_{n,k}(q),\frac{p}{f'_{n,k}(q)}\right),
\qquad
\tau(n,k,q,p)=\log f'_{n,k}(q)
=\log\left(1+\tfrac12\operatorname{sech}^2q\right).
\tag{2}
\]

| Item | Owner in ASFS-20260915-DRC01 | Scope |
| --- | --- | --- |
| Carrier and base map | Full M, omega and (2) | No selected periodic centres or removed escaping states |
| Arithmetic source | Local proper-divisor witnesses in (1) | All n and ordinary divisibility permitted; no prime table |
| Symbolic lineage | Divisor-exclusion constraints -> cyclic witness action -> cotangent geometric lift | A constraint realization, not a conjugacy to the original causal sieve |
| Clock | The displayed log derivative of this same configuration map | Positive pointwise; no positive uniform lower bound |
| Proposed flow space | The endpoint-glued variable-roof space in (3) below | Locally defined suspension dynamics; global completeness fails |
| Coding and periodic data | Full integer/phase/configuration/momentum states | Only a central-cycle control is needed before the stop |
| Measure | Componentwise symplectic area | No finite probability or trace normalization |
| Zeta, transfer operator and trace | NOT EVALUATED | Nothing transfers from a different roof |
| Later owner | Hamiltonian, contact and quantum constructions NOT SUPPLIED | No Route-B statement |

The comparison with [147](../147-saturated-drift-cotangent-sieve/paper.md)
is exact but limited: the base map is the same displayed formula, while
the roof is different. Thus the proposed suspension is a new frozen
candidate. Neither 147's completeness proof nor its zeta belongs to (2).
No claim identifies the odd-dimensional suspension with a symplectic or
Hamiltonian flow.

## 2. Question, inputs and claim boundary

Does the intrinsically defined positive derivative observable in (2)
provide a complete clock on the full frozen carrier? The answer is no:
a single explicit family of full-state trajectories has finite total
forward time and no endpoint in the proposed flow space.

The [prior-work lineage](../../docs/prior_work/README.md) is retained
through the same local prime/composite exclusion witnesses and their
one-dimensional-to-conservative lift. The new hypothesis concerns elapsed
time, not a new arithmetic selector. No numerical prime list, zero data,
fitted logarithmic prime roof, cutoff or parameter search is used.

The strongest claim is an exact scoped negative result. It is not a
no-go theorem for every derivative roof, every cotangent map, or every
possible compactification. Positive closed cycles in an incomplete local
flow are not denied. A full A1 classification and an A2 construction are
not needed after this P0 failure and are not undertaken.

## 3. Geometry and the precise clock proposal

On each component f' lies in (1,3/2]. The bounded tanh term implies that
f_{n,k}(q) tends to the corresponding infinity as q does. Thus f_{n,k}
is a smooth increasing onto diffeomorphism of the line. The inverse of F
uses the preceding phase, q=f_{n,k}^{-1}(Q) and p=P f'_{n,k}(q).
Moreover P dQ=p dq, so dQ wedge dP=dq wedge dp. The full countable
union is a Hausdorff second-countable smooth symplectic surface, and
F is a globally defined symplectomorphism.

The roof is smooth and positive at every finite q, with

\[
0<\tau(q)\le\log(3/2),\qquad
\lim_{|q|\to\infty}\tau(q)=0.
\]

The proposed flow space is the endpoint-glued space

\[
X_\tau=
\{(z,t):z\in M,\ 0\le t\le\tau(z)\}/
\bigl((z,\tau(z))\sim(Fz,0)\bigr).
\tag{3}
\]

Translation in t, with the specified gluing at crossings, defines the
usual local suspension dynamics. Pointwise roof positivity permits local
crossing charts. It does not prove that infinitely many crossings cannot
occur in a bounded elapsed time. That is the independent obligation tested
next.

## 4. Exact full-state finite-time escape

### Proposition — A positive roof with a finite forward return-time sum

Choose n=2, its unique phase k=1, any real initial momentum p_0, and any
q_0>0. Let z_j=F^j(2,1,q_0,p_0) and let q_j be its configuration.
Then q_j tends to positive infinity and

\[
S:=\sum_{j=0}^{\infty}\tau(z_j)<\infty.
\tag{4}
\]

The corresponding trajectory has no endpoint in X_tau at time S and
does not extend continuously there.

**Proof.** The n=2 block is empty, so b(2,1)=0 and

\[
q_{j+1}=q_j+\tfrac12\tanh q_j.
\]

The sequence is positive and strictly increasing. Put
c=(1/2)tanh q_0>0. Monotonicity of tanh gives by induction

\[
q_j\ge q_0+cj.
\tag{5}
\]

For x>=0, log(1+x)<=x. For q>=0, cosh q>=e^q/2. Consequently

\[
0<\tau(z_j)
\le\tfrac12\operatorname{sech}^2q_j
\le2e^{-2q_j}
\le2e^{-2q_0}e^{-2cj}.
\]

Summing the geometric majorant yields the explicit finite bound

\[
0<S\le
\frac{2e^{-2q_0}}{1-e^{-2c}}<\infty.
\tag{6}
\]

Momentum does not enter either q's recurrence or the roof, so the
argument applies to every p_0.

It remains to check that finite accumulated time is genuine incompleteness,
not merely a bad choice of coordinates at a removable endpoint. On the
pre-quotient of (3), define

\[
\mathcal Q(z,t)
=q+\frac{t}{\tau(z)}\bigl(f_{n,k}(q)-q\bigr).
\tag{7}
\]

This is continuous for every finite state. At the upper endpoint it equals
f_{n,k}(q), exactly the configuration of the next section representative
(Fz,0). Therefore it descends to a well-defined continuous real-valued
function on X_tau.

Put s_j=sum_{i=0}^{j-1}tau(z_i). The trajectory on the j-th segment,
with elapsed time in [s_j,s_{j+1}], has
mathcal Q between q_j and q_{j+1}, because those coordinates increase.
Since s_j increases to S and q_j tends to infinity by (5),

\[
\mathcal Q(\varphi^t[z_0,0])\longrightarrow+\infty
\qquad(t\uparrow S).
\tag{8}
\]

Every point of X_tau has a finite value of the continuous function
mathcal Q. Thus the trajectory cannot converge to any point there.
Any continuous flow extension to time S would supply such a limit and
contradict (8). No endpoint or infinity compactification is present in
the frozen carrier. QED.

This proof uses the actual glued space, not an assertion that the raw
coordinate q is globally invariant under gluing. It also concerns the
full real trajectory, not a finite simulation of shrinking return times.
One failing forward trajectory already disproves the required all-state,
both-time-direction completeness.

## 5. Positive local control and adverse comparisons

For a prime label ell, every witness b(ell,k) vanishes. Direct substitution
into (2) shows that (ell,k,0,0) advances through the cyclic phases and
returns after K_ell steps. The roof at those states is log(3/2).
Thus these explicitly displayed central cycles have roof sums

\[
T_\ell=K_\ell\log(3/2),\qquad
T_{\ell,r}=rK_\ell\log(3/2).
\tag{9}
\]

These cycles admit continuation for all times within their own closed
trajectories. Equation (9) is a partial control, not an A1 award for the
full candidate and not exact log ell. It does not remove the noncentral
states used in the escape proposition.

| Control | Result | Consequence |
| --- | --- | --- |
| Same global base map with roof 1 | Any finite elapsed time makes only finitely many global iterates | A separate complete comparator; its clock and analytic data cannot transfer |
| Prime central states | Explicit cycles have the positive sums (9) | Closed packets do not imply full-state completeness |
| Noncentral n=2 states | Equations (5)--(8) give finite-time escape for every q_0>0 | One allowed fibre is sufficient for the P0 stop |
| Pointwise versus uniform positivity | tau>0 everywhere but inf tau=0 | Smooth positive roofs require a separate non-Zeno test |
| Momentum variation | The same escape proof holds for all p_0 | No hidden momentum restriction generates the failure |
| No arithmetic complexity | The n=2 witness block is empty | The clock failure already occurs in the simplest retained source fibre |
| PROVES_TOO_MUCH risk | A positive log derivative alone is not a general completeness criterion | No blanket conversion of expansion observables into complete time |

A positive roof floor, a selected trapped set or an added endpoint at
infinity would alter the frozen object. None is introduced. Broader
arithmetic label controls and analytic numerical checks are not pursued:
they cannot remove this explicit full-state clock counterexample.

## 6. Gate assessment

| Gate | Evidence for ASFS-20260915-DRC01 | Result / boundary |
| --- | --- | --- |
| P0 geometry | Exact global cotangent symplectomorphism | ESTABLISHED for the base only |
| P0 clock / completeness | Finite accumulated time and no endpoint, (5)--(8) | SCOPED FAIL; candidate stops |
| A0 | Derivative-generated clock hypothesis fails the prior completeness obligation | NOT ADVANCED; no arithmetic result transferred from 147 |
| A1 | Central cycles recorded solely as a control | NOT EVALUATED as a full owner-level gate |
| A2 | No complete candidate flow admitted | NOT EVALUATED; no operator, trace or zeta supplied |
| Formal Route A | No protocol evaluation | UNASSIGNED |
| Route B | No readiness or separate invocation | NOT INVOKED |

## 7. Conclusion and portfolio decision

**Stop.** ASFS-20260915-DRC01 does not provide the required complete
full-state suspension, despite a global symplectic base and a smooth
strictly positive roof. The decisive reason is summable return times
along an escaping allowed trajectory.

The same-object ledger remains intact: the negative result is for the
displayed derivative roof, and no unit-roof conclusion is reassigned
to it. The next admissible clock architecture must prove non-Zeno
completeness on its full carrier. Any roof alteration or new endpoint
would require a separate frozen card, with no automatic credit from
the present stop.

Here the roof measures accumulated configuration expansion:
sum_j tau(z_j)=log product_j f'(q_j), with a finite limiting sum along
the escaping orbit. That observable does not supply a complete traversal
time for this particular map. This diagnosis is not a universal rejection
of derivative-generated or geometric clocks.

## Reproducibility and evidence

The proof uses exact inequalities for every q_0>0 and every initial
momentum, with no finite cutoff, numerical precision or external theorem.
See the [card](candidate-card.md), [claim ledger](claim-ledger.md),
[evidence record](evidence/README.md), [independent model review](evidence/review.md),
and [summary](README.md).
