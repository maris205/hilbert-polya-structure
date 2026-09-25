# Rational barrier heights produce physical logarithmic prime periods in a complete Hamiltonian return owner

**Paper ID:** 171-separatrix-witness-hamiltonian-clock  
**Candidate ID:** ASFS-20260915-SWH01  
**Date:** 2026-09-15  
**Status:** ADVANCE — COMPLETE PRIME-ONLY HAMILTONIAN PACKETS AND PHYSICAL LOGARITHMIC CLOCK; NATURALNESS OPEN.  
**Route:** Owner-level construction audit only; formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

A single all-integer rule defines a countable, disconnected four-dimensional
Hamiltonian manifold. Divisor witnesses distinguish a confining inner well
from a monotone escape potential; a hyperbolic transverse Hamiltonian pair
removes all noncentral periodic states without deleting them from the carrier.
The entire energy surface H=1 is fixed before the audit. A uniform rational
barrier excess n^-2 makes the actual inner-well period grow as
2 sqrt(2) log n+O(1), by an explicit near-separatrix integral estimate.
There is exactly one primitive closed orbit per prime and none for composites.
The genuine first-return map is symplectic on its full maximal bi-return
domain, its actual roof is uniformly positive, and all omitted energy states
are nonclosed. The ordinary unweighted orbit zeta has logarithmic-series
absolute-convergence abscissa 1/(2 sqrt(2)). These are owned construction
results, not a naturalness claim: the rational size dependence, potential and
energy remain declared designs. No logarithmic roof is inserted, no operator
is borrowed, and no exact log-p clock or Riemann determinant is asserted.

## 1. Identity, question and source lineage

The [version-1 card](candidate-card.md) was frozen before this proof, under
Lane S of [175](../175-six-lane-geometric-source-frontier/candidate-card.md).
This is a new generator, not a repair or retrospective continuation of
[164](../164-witness-hamiltonian-return-clock/paper.md).

The precise [prior-work arrow](../../docs/prior_work/README.md) is
prime/composite divisor symbols -> full finite witness-exclusion constraint
-> conservative scalar well/escape deformation -> positive-dimensional
Hamiltonian/Poincare geometry. For 2<=d<n the symbol is
w(n,d)=1_{d divides n}; the displayed potential uses their full count.
This preserves an arithmetic admissibility mechanism, not a conjugacy to
the historical Logistic/Henon maps. The continuous trajectory does not
execute trial divisions chronologically, and n is an invariant component
label rather than an advancing sequential-sieve clock.

The question is whether a prespecified, uniform rational dependence on
integer size can generate a physical logarithmic period through a complete
Hamiltonian return mechanism. Naturalness of that design is a separate
OPEN obligation, not a premise of the construction theorem.

| Item | Same-object owner / boundary |
| --- | --- |
| Full geometry | All integer components of the canonical real four-dimensional manifold in (1), and their entire H=1 energy surface |
| Actual flow | Autonomous Hamiltonian equations (2), with unmodified time units |
| Base and form | Genuine first return on the maximal bi-return section M in Proposition 2; full positive-dimensional dQ wedge dP domain |
| Roof and suspension | Actual inner-well return time T_n(1-QP), endpoint gluing by that same return map, exact return-saturation conjugacy |
| Full ledger | All energy-surface closed orbits, including a proof that its nonreturning complement contains none |
| Ordinary analytic object | Unweighted complete primitive-orbit product with the same physical periods; no normalization to make the leading coefficient 1 |
| Operator and later structures | Transfer space, trace, Fredholm determinant, contact and quantum construction NOT SUPPLIED |

## 2. Frozen data and full geometry

For every n>=2 let

\[
a(n)=\sum_{2\le d<n}\mathbf1_{\{d\mid n\}},\quad
c_n=1+n^{-2},\quad W(q)=\frac{4q^2}{(1+q^2)^2},
\]
\[
V_{n,a}(q)=(1-a)c_nW(q)+8a q,\quad
\mathcal X=\coprod_{n\ge2}\mathbb R^4_{q,p,Q,P},\quad
\Omega=dq\wedge dp+dQ\wedge dP,
\]
\[
H_n=\frac{p^2}{2}+V_{n,a(n)}(q)+QP,\qquad
\mathcal E=\coprod_{n\ge2}H_n^{-1}(1).
\tag{1}
\]

Use the disjoint-union smooth topology. It is a second-countable smooth
four-manifold; connectedness or compactness is not claimed. Every n and
every real state is included before fixing the same energy 1. Ordinary
divisibility, the fixed rational formulas and the number 8 are the only
inputs. In particular a(n)=0 precisely when n is prime. No prime list,
prime-selected parameter, zero data or externally declared orbit length
is used. The choice c_n-1=n^-2 is explicit engineering data on every
integer, not an arithmetic theorem forcing that barrier.

With i_X Omega=dH, the equations and conserved quantities are

\[
\dot q=p,\quad \dot p=-V'_{n,a}(q),\quad
\dot Q=Q,\quad\dot P=-P;\qquad
E=\tfrac12p^2+V_{n,a}(q),\quad I=QP,\quad E+I=1.
\tag{2}
\]

### Proposition 1. Complete ambient flow and regular full energy

The flow is complete in both time directions. Every level H_n=1 is
regular. The full transverse section Sigma={H=1,q=0,p>0} on every
integer component is parametrized by

\[
U=\{(Q,P):QP<1\},\qquad
(Q,P)\longmapsto(0,\sqrt{2(1-QP)},Q,P),
\tag{3}
\]

and its induced symplectic form is dQ wedge dP.

**Proof.** Direct differentiation gives

\[
W'(q)=\frac{8q(1-q^2)}{(1+q^2)^3},\qquad
|W'(q)|\le4,
\tag{4}
\]

using |1-q^2|<=1+q^2 and 2|q|<=1+q^2. Since c_n<=5/4,
the force is bounded on each fixed component by
5|1-a|+8a. Momentum grows at most linearly and position at most
quadratically on finite time intervals, while Q(t)=e^t Q(0) and
P(t)=e^-t P(0). No finite-time escape is possible. Smooth local ODE
solutions therefore extend for all real time. No uniform bound in n or
a is needed for this statement: trajectories never change components.

If a>=1 then

\[
V'_{n,a}(q)=8a-(a-1)c_nW'(q)
\ge8a-5(a-1)=3a+5\ge8.
\tag{5}
\]

Thus composite components have no critical point of H. For a=0 its
only critical points have p=Q=P=0 and q=0 or +/-1. Their energies
are 0 or c_n>1, not 1. This proves full-energy regularity. At the
section V(0)=0, giving (3), and qdot=p>0 proves transversality.
Pullback of Omega is dQ wedge dP. The Hamiltonian flow preserves
Omega because the Lie derivative is d(i_X Omega)=d(dH)=0. ∎

## 3. Exact return domain and all omitted energy states

M is defined operationally as the maximal bi-return domain of Sigma,
not by specifying primes or selecting closed centres. For a component
with a=0 and 0<E<c_n, write A_n(E) in (0,1) for the unique inner
positive turning point c_n W(A_n(E))=E, and define the actual period

\[
T_n(E)=4\int_0^{A_n(E)}
\frac{dq}{\sqrt{2(E-c_nW(q))}}.
\tag{6}
\]

### Proposition 2. Maximal bi-return and the full complement

The actual M is precisely the union, over the zero-witness components,
of the entire open domains

\[
U_n^{\rm ret}=\{(Q,P):1-c_n<QP<1\}.
\tag{7}
\]

Its return-saturation consists of the inner scalar oscillations
0<E<c_n, |q|<1 on these components, with every compatible transverse
state. T_n is smooth on (0,c_n), and uniformly on all M,

\[
\tau(n,Q,P)=T_n(1-QP)\ge\pi/5>0.
\tag{8}
\]

All other full-energy states are retained in the primary energy owner
and are nonclosed.

**Proof.** On composite components (5) gives pdot<=-8, which forbids
every positive-time closed orbit. Moreover q is strictly concave, so
there cannot be two crossings q=0,p>0 on the same trajectory. These
components have no bi-return states, irrespective of the sign of E.

On a prime component, c_n W is even and nonnegative, vanishes only
at q=0, increases strictly on (0,1) to its maximum c_n, decreases
strictly on (1,infinity) to 0, and has the same shape on the negative
side. The following list exhausts all scalar energy branches:

| Scalar energy / branch | Actual dynamics and section behavior |
| --- | --- |
| E<0 | No real state exists |
| E=0 | Only q=p=0; then QP=1, so the full transverse motion is nonclosed |
| 0<E<c_n, inner component | One bounded energy oval between +/-A_n(E); it has exactly one q=0,p>0 crossing per full period |
| 0<E<c_n, two outer components | Allowed abs(q)>=B_n(E)=1/A_n(E)>1; each has one simple turning point and escapes toward the same spatial infinity in the two time directions; none hits q=0 |
| E=c_n | Equilibria q=+/-1,p=0 and separatrix branches, including the inner heteroclinic branches; no nonconstant periodic orbit and no repeated positive section crossing |
| E>c_n | p never vanishes, so q is strictly monotone; scattering branches are nonperiodic and have at most one section crossing |

At E=c_n, the identity

\[
1-W(q)=\left(\frac{1-q^2}{1+q^2}\right)^2
\tag{9}
\]

shows a double zero of E-c_n W at either barrier. The elapsed
approach integral diverges logarithmically, so separatrix trajectories
do not cross a saddle in finite time. At the scalar equilibria the
full-energy relation gives QP=1-c_n!=0; hence their full trajectories
are not fixed or periodic. Outer turning points for 0<E<c_n are
simple because W'(B_n(E))!=0. The kinetic energy tends to E at
infinity, so escape takes infinite time, consistently with Proposition 1.

Only the inner ovals cross the section repeatedly. Each crossing is
transverse, and its return integral (6) has an integrable inverse-square-
root endpoint singularity. The ODE and return transversality imply
smooth local dependence of the first return time on E by the implicit
function theorem. This proves smooth T_n throughout (0,c_n).
Conservation of E=1-QP gives exactly (7), in both time directions.

For the non-Zeno bound use the clockwise angle of the nonzero inner
oscillator point (q,p). On |q|<1,

\[
0\le c_nqW'(q)\le10q^2,\qquad
0<\dot\theta=\frac{p^2+c_nqW'(q)}{q^2+p^2}\le10.
\tag{10}
\]

At q=0, p!=0; at a turning point q!=0 the numerator is positive.
The inner oval turns once around the origin, so 2 pi<=10 T_n(E),
proving (8). The estimate is deliberately coarse but uniform. The
table includes every omitted energy state, and its scalar nonclosed
branches cannot become full closed orbits by adjoining Q,P. ∎

In particular, merely specifying 0<E<c_n without the inner-component
condition would be wrong: the same energies have outer escaping states.
These states are not deleted from the full energy owner or called part
of the return suspension.

### Proposition 3. Full symplectic first return and its exact flow owner

On all of M the return map is

\[
F(n,Q,P)=\bigl(n,e^{T_n(1-QP)}Q,e^{-T_n(1-QP)}P\bigr).
\tag{11}
\]

It is a smooth symplectomorphism of M. Its actual-roof suspension is
complete and smoothly conjugate to precisely the return-saturation in
Proposition 2, with unchanged Hamiltonian time.

**Proof.** The transverse solutions and first scalar return give (11).
Write t(I)=T_n(1-I). The map preserves I and the whole open interval
1-c_n<I<1, and its inverse replaces t by -t. Since dI=P dQ+Q dP,

\[
d(e^{t(I)}Q)\wedge d(e^{-t(I)}P)
=dQ\wedge dP-Pt'(I)dQ\wedge dI+Qt'(I)dI\wedge dP
=dQ\wedge dP.
\tag{12}
\]

Define the endpoint-glued M_tau using the card's convention and send
[z,u] to Phi^u(z). The endpoint equality is the actual return identity.
Every saturated state has a unique elapsed phase 0<=u<T_n(E) from
its last section crossing. This proves bijection after endpoint gluing;
flow-box charts and transverse smooth returns give smooth local inverse
coordinates, including at seams. The map intertwines both flows. The
uniform bound (8) forbids infinitely many crossings in finite positive
or negative time. Alternatively E is conserved and each orbit has the
same positive spacing at every crossing. The suspension is not claimed
to be all of mathcal E; Proposition 2 accounts for the whole complement. ∎

The componentwise section area and time volume dQ dP du descend across
the seams and are flow invariant; the extra d tau term vanishes when
wedged with the top-degree section area. No finite total probability
measure is asserted. The ambient four-manifold and the two-dimensional
base are symplectic; their three-dimensional energy/suspension spaces
are not called symplectic manifolds.

## 4. Full primitive packets, repeats and stability

### Proposition 4. Exactly one primitive packet per prime

The entire fixed energy flow has one primitive closed orbit on every
prime component and none on composite components. Its actual period is
T_p=T_p(1) from (6). It corresponds to the unique periodic section
point Q=P=0, with least map period one. Every r-fold repetition has
time r T_p and transverse monodromy

\[
DF^r(0,0)=\operatorname{diag}(e^{rT_p},e^{-rT_p}),\qquad
\det(I-DF^r)=2-e^{rT_p}-e^{-rT_p}<0.
\tag{13}
\]

**Proof.** For any positive-time full closed orbit, the transverse
equations force Q=e^t Q and P=e^-t P, hence Q=P=0. This conclusion
is derived on the whole energy surface, not imposed as a carrier
restriction. Therefore E=1. Composite components cannot close by (5).
For a prime, 0<1<c_p, and the unique inner energy-1 oval is closed;
the two outer branches at E=1 are not closed. One oval is one oriented
flow orbit; the negative-momentum crossing is not a second packet.

On M, conservation of I gives F^r(Q,P)=(e^{rt(I)}Q,e^{-rt(I)}P).
Positivity of t likewise forces every periodic section point to be the
origin. At the origin dI=0, so differentiation gives (13). No higher
least-map-period packet or noncentral continuum is hidden. The statement
is transverse Poincare hyperbolicity, not a denial of the usual neutral
time/energy directions of an autonomous Hamiltonian. ∎

## 5. Physical period asymptotics without a logarithmic roof

### Proposition 5. Uniform logarithmic-size estimate

For the inner energy-1 period of the rational well at every integer
n>=2 (and thus for every actual prime packet),

\[
T_n(1)=2\sqrt2\log n+O(1),
\tag{14}
\]

where the bound is uniform in n. For composite labels the well-only
quantity in this statement is a comparison integral, not their actual
Hamiltonian period. Their actual flow has no closed orbit.

**Proof.** Set c=1+n^-2 and delta=sqrt((c-1)/c)=1/sqrt(n^2+1).
For 0<=q<=A_n(1), use y=(1-q^2)/(1+q^2). The endpoint changes
from y=1 to y=delta, and

\[
q=\sqrt{\frac{1-y}{1+y}},\qquad
-\frac{dq}{dy}=f(y)=\frac1{(1+y)^{3/2}(1-y)^{1/2}}.
\]

Identity (9) then gives the exact elapsed-time formula

\[
T_n(1)=\frac4{\sqrt{2c}}
\int_\delta^1\frac{f(y)}{\sqrt{y^2-\delta^2}}\,dy.
\tag{15}
\]

Here f(0)=1 and f is continuously differentiable on [0,1/2].
Choose a finite constant L with |f(y)-1|<=L y on that interval.
Because delta<=1/sqrt5<1/2,

\[
\left|\int_\delta^{1/2}
\frac{f(y)-1}{\sqrt{y^2-\delta^2}}\,dy\right|
\le L\sqrt{1/4-\delta^2}\le L/2.
\tag{16}
\]

On [1/2,1), y^2-delta^2>=1/20, while f is integrable up to 1.
Thus that entire upper contribution is bounded uniformly in n. The
remaining integral is

\[
\int_\delta^{1/2}\frac{dy}{\sqrt{y^2-\delta^2}}
=\operatorname{arcosh}\frac1{2\delta}
=\log(1/\delta)+O(1).
\tag{17}
\]

The final O(1) is uniform for the stated delta interval (use the
explicit arcosh logarithm). Therefore (15) is
(2 sqrt2/sqrt c) log(1/delta)+O(1). Now
log(1/delta)=log n+(1/2)log c, and
|(1/sqrt c-1)log n|<=n^-2 log n, uniformly bounded. This proves
(14), with its n-independent coefficient 2 sqrt2. ∎

The maxima are nondegenerate: (9) gives W(1+x)=1-x^2+O(x^3),
and likewise at -1. Formula (15), not an assigned roof, is why the
distance c_n-1=n^-2 from the barrier converts to a logarithm in
physical time. Time has not been divided by 2 sqrt2. No equality
T_p=log p, no canonical choice of c_n, and no explicit-formula
weight are concluded from this asymptotic.

## 6. Ordinary same-object product: a bounded analytic consequence

Put C=2 sqrt2. The sole analytic object considered is

\[
\log Z(s)=\sum_{p\,\mathrm{prime}}\sum_{r\ge1}
\frac{e^{-srT_p}}r,\qquad
Z(s)=\prod_{p\,\mathrm{prime}}(1-e^{-sT_p})^{-1}.
\tag{18}
\]

All primitive multiplicities are one, and r is the repetition of the
same Hamiltonian orbit. There are no added stability weights.

### Corollary 6. Exact logarithmic-series absolute abscissa

The series in (18) converges absolutely and locally uniformly for
Re(s)>1/C and defines a holomorphic nonzero Z there. It fails absolute
convergence for every Re(s)<=1/C. In particular finite physical-time
windows contain only finitely many primitive packets and repetitions.

**Proof.** Proposition 5 gives |T_p-C log p|<=B for one finite B,
and Proposition 2 gives T_p>=pi/5. For sigma=Re(s)>0,

\[
\sum_{r\ge1}\frac{e^{-\sigma rT_p}}r
\le\frac{e^{-\sigma T_p}}{1-e^{-\sigma\pi/5}}.
\tag{19}
\]

If C sigma>1, summing the bound by e^{sigma B} p^{-C sigma}
and then by all integers proves absolute convergence. The same estimate
with the minimum real part of a compact subset proves normal convergence.
Exponentiation gives the nonzero holomorphic product.

For 0<sigma<=1/C, the r=1 sum dominates a constant times
sum_p p^{-C sigma}, hence sum_p 1/p. For completeness, divergence
of the latter follows elementarily: if it converged then the finite
Euler products product_{p<=N}(1-1/p)^-1 would be uniformly bounded,
since -log(1-1/p)<=2/p. Expanding a finite product by geometric
series and unique factorization shows it is at least sum_{m<=N}1/m,
which is unbounded. For sigma<=0 even the repetitions of a single
prime fail absolute convergence. This proves the exact abscissa without
using a prime-number asymptotic. Finally T_p<=R implies
p<=exp((R+B)/C), and r T_p<=R implies r<=5R/pi. ∎

This is an ordinary owned orbit product, not an equality with the
Riemann zeta function, a Fredholm determinant or an analytic continuation.
No transfer space, trace kernel, target divisor or quantization is
constructed or borrowed. Those remain separate OPEN / NOT SUPPLIED fields.

## 7. Controls and naturalness boundary

These comparisons are not changes to the frozen candidate.

| Control | Exact consequence | Scope |
| --- | --- | --- |
| Set every witness count to zero | Every integer has the same kind of unique inner energy-1 packet, with its own rational-barrier period | The exclusion of composites is genuinely due to the divisor witness |
| Composite-only full-energy diagnostic | pdot<=-8 everywhere | No composite packet is hidden in an unexamined energy branch |
| Replace a(n) by an arbitrary nonnegative integer constraint | The proof retains exactly its zero set | PROVES_TOO_MUCH for claiming that conservative geometry uniquely privileges primality |
| Remove QP from H | Q and P are constant; each prime inner oval has a continuum of full closed copies | The transverse dynamics, not centre selection, enforces finite multiplicity |
| Do not fix the energy beforehand | Each prime has closed inner ovals for every scalar 0<E<c_p at Q=P=0 | The theorem is about the entire energy 1 fixed before proof, not all ambient energies |
| Set c_n=1 for all n | The fixed energy 1 reaches the separatrix, whose nonconstant branches never close in finite time; scalar saddles have energy 1 | Positive barrier excess is necessary for this chosen nonconstant-packet mechanism; this comparator has critical energy and is not the candidate |
| Set a constant c_n=c>1 | Every prime has the same inner period | Size dependence, absent in 164, is necessary for the new logarithmic-scale clock |
| Replace n^-2 by n^-beta for fixed beta>0 | The same integral estimate has leading sqrt2 beta log n | The power and resulting time coefficient are engineered, not uniquely source-forced; this is a symbolic formula comparison, not an executed parameter search |
| Retain outer and saddle states | Proposition 2 accounts for them outside the return-saturation; none contributes an omitted closed orbit | The return suspension is not misidentified with the full energy surface |
| Use an assigned log-p roof or import 153's trace | Would change the frozen time or analytic owner | Not performed; it would require a different contract |

Thus a real physical logarithmic-size mechanism has been proved, while
the stronger claim that the original prime-symbolic source canonically
selects this Hamiltonian has not. The latter remains OPEN. Declared design
choices do not erase the full-state construction; successful engineering
does not establish natural A0.

## 8. Gate assessment and decision

| Gate / field | Evidence for this exact candidate | Outcome |
| --- | --- | --- |
| P0 geometry / clock owner | Propositions 1--3 give complete ambient dynamics, regular full energy, exact positive-dimensional symplectic return and uniform non-Zeno actual roof | ESTABLISHED with the precise return-saturation relation |
| Owner-level A0 relevance | Same all-integer divisor mechanism derives prime support; rational barrier gives physical logarithmic size through Proposition 5 | CONSTRUCTION POSITIVE; naturalness OPEN, not formal A0 PASS |
| Owner-level A1 | Proposition 4 exhausts full energy and suspension packets, orientation, multiplicity and repeats | ESTABLISHED; one primitive packet per prime |
| Owner-level ordinary A2 consequence | Corollary 6 proves full unweighted product and exact absolute abscissa | ESTABLISHED only for this ordinary product; operator and continuation NOT SUPPLIED |
| Formal Route coordinates | No target/divisor audit performed | UNASSIGNED |
| Route B | No formal invocation or candidate-specific readiness | NOT INVOKED |

**Portfolio decision: advance within the frozen engineering contract.**
The decisive positive difference from 164 is an actually derived,
unbounded logarithmic-size Hamiltonian clock, with the full geometry and
periodic ledger intact. Unlike [160](../160-source-geometric-return-clock/paper.md),
the logarithm comes from a nondegenerate-barrier transit integral, not a
dilation/reset timing prescription. Unlike
[155](../155-derivative-roof-completeness-test/paper.md), both ambient
completeness and non-Zeno return time are proved on the full relevant states.
No old result or formal coordinate transfers through these comparisons.

The bounded lane stops work here with its positive record. Any further
operator construction, change of barrier or clock, or stronger naturalness
claim needs its own explicit evidence and, when it changes the object,
a new contract. No exact log-p or Riemann-target matching is pursued.

## Reproducibility and disclosure

All results are exact derivations from (1)--(19), not finite observations.
There was no integrator, prime table, period-fitting run, numerical cutoff,
precision claim, external-model upload or publication artifact. The
[evidence index](evidence/README.md) records checks and the actual
different-invocation [mathematical review](evidence/review.md).
The [claim ledger](claim-ledger.md) separates constructed facts from OPEN
claims. ARS was used only for bounded claim/evidence/counterargument
discipline; no full manuscript pipeline or journal-fit claim was invoked.
Model-assisted authoring and review are not human peer review or a proof
certificate. No human-subject data or external funding claim is involved.
