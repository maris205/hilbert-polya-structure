# A complete witness Hamiltonian has an owned return clock but infinitely many common-time prime packets

**Paper ID:** 164-witness-hamiltonian-return-clock  
**Candidate ID:** ASFS-20260915-WHR01  
**Date:** 2026-09-15  
**Status:** STOP — COMPLETE HAMILTONIAN RETURN OWNER; INFINITE COMMON-TIME PRIME PACKETS.  
**Route:** Owner-level audit only; formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

On the disjoint union of all integer-labelled real four-dimensional
components, one autonomous Hamiltonian combines a finite divisor-witness
potential with a hyperbolic transverse pair. Its complete energy surface
H=1 is fixed before the audit. The actual section q=0,p>0 has a
positive-dimensional maximal bi-return domain. We prove that its genuine
first-return map is symplectic and its positive roof is uniformly at least
2 pi. The resulting complete suspension is exactly the return-saturated
part of the energy surface, not the entire surface. Classification of the
omitted states proves that no closed orbit is lost: there is exactly one
primitive closed orbit per prime, none for composite labels, and every
transverse repetition is hyperbolic. However, all prime orbits have the
same actual Hamiltonian period. Their infinite common-time multiplicity
prevents the ordinary unweighted orbit product on every right half-plane.
The genuine Hamiltonian clock is retained as a construction result, not
promoted to a logarithmic or source-natural arithmetic clock. No parameter
or energy adjustment is made after this decisive failure.

## 1. Identity, lineage and claim boundary

The [version-1 card](candidate-card.md) fixes the full Hamiltonian,
uniform energy level, actual first-return convention and stop tests before
the proof. This is Lane H of the
[168 scope](../168-source-return-breadth-frontier/candidate-card.md), not a
repair of [160](../160-source-geometric-return-clock/paper.md).

The [prior-work lineage](../../docs/prior_work/README.md) is used in the
following exact, limited sense:

\[
\text{prime/composite divisor symbols}
\longrightarrow\text{finite witness-exclusion constraint}
\longrightarrow\text{conservative oscillator/escape deformation}
\longrightarrow\text{positive-dimensional symplectic return map}.
\]

The witness symbols are \(w(n,d)=\mathbf1_{\{d\mid n\}}\) for
\(2\le d<n\); their complete count is the coefficient of the displayed
potential. This is a conservative geometric deformation of that source
constraint, not a conjugacy to the historical Logistic or Hénon map.
The count is computed by one finite trial-divisor formula on every
integer component. The continuous motion does not execute the tests in
chronological order, and n is invariant, not a sequential sieve clock.

| Item | Exact owner and evidence boundary |
| --- | --- |
| Ambient phase space | All n>=2 and all real q,p,Q,P in the Hamiltonian manifold X below |
| Primary flow | The displayed Hamiltonian flow on the entire pre-fixed regular energy Ecal=H inverse(1) |
| Base map and form | Actual first return on maximal bi-return section M, with dQ wedge dP; not a map on the nonreturning part of Sigma |
| Roof and suspension | Actual elapsed return time T(1-QP), endpoint gluing by the same F, and the explicit flow embedding in Proposition 3 |
| Full closed-orbit ledger | Every energy-surface closed orbit, with no lost orbit in the nonreturning complement; exactly the full suspension ledger |
| Analytic diagnostic | Ordinary unweighted complete orbit Z; its convergence fails, so no operator, trace or determinant is introduced |
| Further ownership | Hamiltonian owner explicitly constructed; no contact, quantum, Fredholm or formal Route claim |

The positive result is an exact full-energy/Poincare construction. It does
not assert that a three-dimensional energy surface or mapping torus is
itself symplectic. The symplectic objects here are the four-dimensional
ambient phase space and two-dimensional section/base.

## 2. Frozen definitions and permitted inputs

For every integer n>=2 set

\[
a(n)=\sum_{2\le d<n}\mathbf1_{\{d\mid n\}},\qquad
V_a(q)=(1-a)\log\cosh q+a q,
\tag{1}
\]
\[
\mathcal X=\coprod_{n\ge2}\mathbb R^4_{q,p,Q,P},\qquad
\Omega=dq\wedge dp+dQ\wedge dP,
\]
\[
H_n(q,p,Q,P)=\frac{p^2}{2}+V_{a(n)}(q)+QP,
\qquad \mathcal E=\coprod_{n\ge2}H_n^{-1}(1).
\tag{2}
\]

Use the disjoint-union smooth topology. All components have dimension
four, and no labels are selected using a prime list. The only arithmetic
input is ordinary divisibility; the empty count at n=2 is zero. By the
definition of primality, a(n)=0 exactly for prime n; otherwise a(n) is
an integer at least one. The fixed functions, all coefficients and energy
1 are design choices. No prime-specific energy or period is supplied.

With \(\iota_{X_H}\Omega=dH\), the equations are

\[
\dot q=p,\qquad
\dot p=-\bigl((1-a)\tanh q+a\bigr),\qquad
\dot Q=Q,\qquad \dot P=-P.
\tag{3}
\]

Both the oscillator energy
\(E=p^2/2+V_a(q)\) and \(I=QP\) are conserved, with E+I=1
on the full energy surface. The full section is

\[
\Sigma=\{z\in\mathcal E:q=0, p>0\}.
\tag{4}
\]

Before classification, M means its maximal bi-return domain as defined
in the card. It is not defined by retaining primes or periodic centres.
Every first-return and omission statement below follows from (3).

## 3. Full geometry and actual return domain

### Proposition 1. Complete flow and regular energy

The flow of (3) is complete in both time directions on every ambient
component. The energy surface H=1 is regular for every n. The section
Sigma is transverse and is parameterized on each integer component by

\[
\mathcal U=\{(Q,P)\in\mathbb R^2:QP<1\},\qquad
(Q,P)\longmapsto(0,\sqrt{2(1-QP)},Q,P).
\tag{5}
\]

Its induced two-form is dQ wedge dP.

**Proof.** For each fixed finite a,
\(\lvert V'_a(q)\rvert\le\lvert1-a\rvert+a\).
Thus p grows at most linearly and q at most quadratically on any bounded
time interval. Meanwhile \(Q(t)=e^tQ(0)\) and
\(P(t)=e^{-t}P(0)\). No coordinate can escape to infinity in finite
time; smooth local ODE solutions therefore extend to all real times.
No uniform bound in n is needed, because n never changes along a flow
line. The Hamiltonian is conserved and its flow preserves Omega.

For a=0, the only critical point of H is q=p=Q=P=0, at energy 0.
For every integer a>=1,

\[
V'_a(q)=a-(a-1)\tanh q\ge1,
\tag{6}
\]

so H has no critical point. This proves regularity at energy 1.
Since V_a(0)=0, (5) follows from the energy equation. At the section,
\(\dot q=p>0\), giving transversality. Pulling back Omega to (5)
removes the dq wedge dp term and leaves the nondegenerate form
dQ wedge dP. ∎

### Proposition 2. Exact returns and the full omitted-state classification

The operational maximal bi-return domain M is exactly the union of the
whole U section components for which a(n)=0. On this domain,

\[
F(n,Q,P)=\bigl(n,e^{T(1-QP)}Q,e^{-T(1-QP)}P\bigr),
\qquad \tau(n,Q,P)=T(1-QP),
\tag{7}
\]

where, for E>0,

\[
A(E)=\operatorname{arcosh}(e^E),\qquad
T(E)=4\int_0^{A(E)}\frac{dq}{\sqrt{2(E-\log\cosh q)}}.
\tag{8}
\]

T is smooth and positive on E>0, and T(E)>=2 pi. The Hamiltonian
return-saturation is exactly the a(n)=0 part with oscillator energy E>0.
The complementary full-energy states consist of all composite components
and, on prime components, the states q=p=0, QP=1. None is closed.

**Proof.** For a>=1, (6) gives
\(p(t_2)\le p(t_1)-(t_2-t_1)\) when t_2>t_1.
The momentum is strictly decreasing. In particular q is strictly
concave along each trajectory. There cannot be two section hits with
q=0 and p>0: before p changes sign q is increasing, and after its
sign change q cannot return with positive momentum. Thus these section
components have no first positive return and no point in M. The same
strict momentum inequality excludes a positive-time closed orbit
anywhere on the entire composite energy surface, including states that
never hit Sigma. Oscillator energies E of any sign are possible here;
the monotonicity proof does not exclude them from the primary carrier.

For a=0, the oscillator energy is
\(E=p^2/2+\log\cosh q\ge0\). No prime full-energy state with
E<0 exists. For E=0 necessarily q=p=0 and I=QP=1. Such a state
never reaches Sigma, and Q,P are both nonzero, so their exponential
motion cannot close.

For E>0, the scalar potential is even, strictly increasing on q>0,
and tends to infinity as |q| tends to infinity. The oscillator traverses
its single energy oval between the two turning points +/-A(E). The
integral in (8) is finite: near a turning point V'(A)>0 and the
integrand has only an inverse-square-root endpoint singularity. Each
period has exactly one crossing q=0,p>0, so T(E) is the least such
return time, not a half-period. Smooth dependence of the ODE and the
nonzero return crossing speed give smooth T(E) locally at every E>0
by the implicit function theorem. These local periods agree with (8).

The oscillator never reaches the origin for E>0. Its clockwise angle
has derivative

\[
\dot\theta=\frac{p^2+q\tanh q}{q^2+p^2},
\qquad 0<\dot\theta\le1.
\tag{9}
\]

Indeed 0<q tanh q<=q^2 for q nonzero, and at q=0 the numerator
and denominator both equal p^2>0. One traversal of the energy oval
makes one full angular turn, so
\(2\pi=\int_0^{T(E)}\dot\theta\,dt\le T(E)\).
The transverse equations in (3) then give (7), because E=1-QP is
constant along the trajectory. All forward and backward section hits
exist with this same positive spacing, proving the exact domain claim.
Every E>0 prime state lies on such a section-saturated trajectory.
The classifications above exhaust the full energy surface. ∎

The result describes M using primality only **after** the full operational
return calculation. The initial Hamiltonian, energy and section included
all integers. Moreover M contains every point of the two-dimensional
open U for each admitted component, not merely the periodic centre.

### Proposition 3. Symplectic return and exact suspension ownership

The map F in (7) is a smooth symplectomorphism of all M. Its roofed
suspension is a complete flow and is smoothly conjugate to the actual
Hamiltonian flow on the return-saturation described in Proposition 2.
This saturation is generally a proper subset of the full energy surface.

**Proof.** Write I=QP and t(I)=T(1-I). Formula (7) preserves I,
and its inverse is
\((Q,P)\mapsto(e^{-t(I)}Q,e^{t(I)}P)\). The inequalities I<1
and all real transverse states in U are preserved. Direct differentiation
gives

\[
d(e^{t(I)}Q)\wedge d(e^{-t(I)}P)
=dQ\wedge dP
-P t'(I)dQ\wedge dI+Q t'(I)dI\wedge dP
=dQ\wedge dP.
\tag{10}
\]

The last cancellation uses dI=P dQ+Q dP. Thus the return map is
symplectic on its full positive-dimensional domain.

Define

\[
M_\tau=\{(z,u):z\in M,0\le u\le\tau(z)\}/
((z,\tau(z))\sim(Fz,0)),
\qquad \Psi[z,u]=\Phi^u(z).
\tag{11}
\]

The equality at each gluing seam is exactly the first-return equation.
Each saturated Hamiltonian state has a unique last positive-crossing
section hit and an elapsed phase in [0,T(E)); hence Psi is bijective
onto that saturation, with the seam equivalence precisely removing the
endpoint duplication. Transversality and smooth first-return times give
smooth local inverse coordinates, including flow-box charts across each
seam. Psi intertwines translation in u with the original Hamiltonian
time, without reparameterization or reset. The uniform bound tau>=2 pi
proves two-sided non-Zeno completeness directly; equivalently every
orbit has conserved E and constant roof spacing T(E)>0.

No conjugacy to the entire energy surface is asserted: its omitted
components and boundary states were explicitly retained and shown to
have no closed orbit in Proposition 2. ∎

## 4. Complete primitive ledger and the decisive clock failure

### Proposition 4. One hyperbolic packet per prime, all at the same time

For every prime label there is exactly one primitive closed orbit on the
entire H=1 energy surface, and there are none for composite labels.
Its transverse section point is Q=P=0, its least map period is one,
and its actual primitive flow time is the same constant

\[
T_* = T(1)
=4\int_0^{\operatorname{arcosh}(e)}
\frac{dq}{\sqrt{2(1-\log\cosh q)}}>0
\tag{12}
\]

for every prime. Its r-fold repetition has time r T_* and transverse
Poincare monodromy

\[
D F^r(0,0)=\begin{pmatrix}e^{rT_*}&0\\0&e^{-rT_*}\end{pmatrix},
\qquad
\det(I-D F^r)=2-e^{rT_*}-e^{-rT_*}<0.
\tag{13}
\]

**Proof.** Every full Hamiltonian closed orbit of positive time t must
satisfy Q=e^t Q and P=e^{-t}P; hence Q=P=0. This is a consequence
of the full periodic equations, not a restriction on the initial carrier.
The energy then forces oscillator energy E=1. Composite orbits cannot
close by Proposition 2. On a prime component the unique energy-1
oscillator oval is a single oriented flow orbit with least period (12).
The other sign at q=0 is a point on the same orbit, not a second packet.

Equivalently, on all of M the conserved I gives
\(F^r(Q,P)=(e^{rT(1-I)}Q,e^{-rT(1-I)}P)\).
Since the time is positive, any periodic section state has Q=P=0.
Thus there are no omitted noncentral or higher-period packets. At the
origin dI=0; differentiating gives (13). The two nontrivial transverse
multipliers are hyperbolic, and no repeat has a transverse multiplier 1.
This is a statement about the two-dimensional Poincare monodromy, not
a denial of the usual time/energy directions in the full autonomous
flow linearization. Proposition 2 proves that the suspension's ledger
also exhausts all closed orbits of the full energy owner. ∎

### Corollary 5. The ordinary unweighted zeta stops at convergence

There are infinitely many primitive packets at the bounded time T_*.
The proposed complete ordinary repetition series would be

\[
\log Z(s)=\sum_{p\ \mathrm{prime}}\sum_{r\ge1}
\frac{e^{-srT_*}}{r}.
\tag{14}
\]

It has no absolute convergence point at any finite s: already the
r=1 terms have the same nonzero absolute value for infinitely many
primes. Consequently there is no right half-plane on which the full
ordinary unweighted orbit product is defined by its usual convergent
logarithmic series. For positive real s, even its finite prime-cutoff
products grow without bound. No ordering or enumeration convention
removes this actual common-time multiplicity.

This uses only the infinitude of primes and the exact full ledger, not
a finite numerical census or a prime-number asymptotic. It does not
exclude an independently defined weighted or regularized object, none
of which is part of this frozen contract. No analytic continuation is
claimed for an ordinary product that lacks an initial convergence domain.

The actual clock also cannot be the prime-log clock: T_2=T_3=T_*,
whereas log 2 differs from log 3. Since primes are unbounded, T_p/log p
tends to zero along primes. The Hamiltonian is identical on every zero-
witness component, so its primitive timing contains no remaining
prime-size information. This is the decisive source-clock discrimination,
not a failure to construct a physical clock.

## 5. Controls and adverse findings

All control changes below are comparators, not alterations of (1)--(3).

| Control | Exact finding | Meaning |
| --- | --- | --- |
| Remove all witnesses: a(n)=0 | Every integer component has the same single energy-1 closed oscillator orbit | Arithmetic exclusion is caused by the witness coefficient, not generic conservative geometry |
| Composite-only ledger diagnostic | Full momentum is strictly decreasing on every retained component | No composite closed orbit is concealed in the nonreturning domain |
| Replace a(n) by another nonnegative integer constraint count | The same proof admits exactly its zero set; a=1 outside any prescribed set realizes that set as a control | PROVES_TOO_MUCH for any claim that this interpolation alone makes the arithmetic source privileged |
| Remove the transverse QP term | Q and P become constant; each prime energy-1 oval then gives a continuum of closed orbits indexed by all real (Q,P) | The full transverse Hamiltonian pair, not post hoc centre selection, makes the candidate's packet multiplicity finite per label |
| Do not pre-fix energy | Q=P=0 supports a different closed oval for every E>0 on each prime component | The unrestricted ambient flow has continuum orbit families; the stated result is for H=1 fixed before any audit, not secretly for all energies |
| Retain the entire section U | Nonzero Q or P returns to Sigma but never periodically returns to the same full state | Section recurrence does not imply a continuum of periodic packets |
| Retain the full-energy complement | Composite components and prime E=0 states are complete and nonclosed; prime E<0 has no state | The exact saturation relation accounts for all closed orbits without identifying two different carriers |
| Compare two prime labels or enlarge the prime cutoff | Every prime time remains T_*; at cutoff N packets the product is (1-e^{-sT_*})^{-N} | The infinite common-time failure is exact and cannot be fixed by higher numerical precision |

The fixed energy choice is legitimate construction data. Its legitimacy
does not assert that the integer source singles it out. Likewise the
oscillator/escape interpolation supplies an internal divisibility-based
constraint, but it is not a chronological primality-generating trajectory.
These limitations do not invalidate the complete Hamiltonian geometry.
They prevent promotion to a natural prime-log A0 result.

## 6. History collision and gate assessment

The direct full-state construction addresses the obligation in
[038](../038-hamiltonian-periodic-ledger-obligation/paper.md), rather than
borrowing its closed-surface comparator theorems. Its open noncompact
section is not in those closed-surface hypotheses.
[152](../152-coupled-witness-henon-escape/paper.md) is a discrete
full-count Hénon antecedent, not this Hamiltonian generator.
[155](../155-derivative-roof-completeness-test/paper.md) shows that a
positive roof alone need not be complete; (9)--(11) settle this candidate
directly. Unlike [160](../160-source-geometric-return-clock/paper.md),
there is no prescribed dilation transit or log-n reset seam here.
That geometric difference does not force arithmetic timing: the actual
Hamiltonian period is constant across the desired labels.

| Gate | Exact evidence | Status / limitation |
| --- | --- | --- |
| P0 geometry and clock ownership | Propositions 1--3: complete regular full energy, exact bi-return domain, symplectic positive-dimensional base and actual uniformly positive roof | ESTABLISHED in the stated full-energy/return-saturation relation |
| Owner-level A0 source | Finite proper-divisor count and oscillator/escape dichotomy are explicit and survive composite controls | Scoped arithmetic relevance; source-naturalness OPEN; prime-log timing fails |
| Owner-level A1 ledger | Proposition 4 characterizes every closed orbit and repetition of the full energy and suspension owners | Exact ledger ESTABLISHED; infinite bounded-time multiplicity is an adverse finding, not an omitted family |
| Owner-level A2 minimum test | Corollary 5 rules out an ordinary convergent full unweighted product on any right half-plane | STOP; no operator, trace, Fredholm or continuation work advanced |
| Formal Route coordinates | No target/divisor evaluation performed | UNASSIGNED |
| Route B | No same-candidate Route-A readiness or formal invocation | NOT INVOKED |

## 7. Decision and reproducibility

**Portfolio decision: stop.** Retain the complete full-energy/Poincare
construction and its exact arithmetic support as a geometric control.
Do not tune an n-dependent energy or alter the oscillator in order to
save its failed common-time clock. Any changed generator, energy, time
law or analytic owner requires a new frozen contract; no such fork is
executed in this package.

Every result above follows from the displayed equations on all real
states. No ODE integrator, period fit, numerical cutoff or precision
claim is used. The endpoint integral is an exact definition, not a
numerical estimate. The [evidence index](evidence/README.md) records the
actual proof checks, bounded history inspection and review provenance.
The [claim ledger](claim-ledger.md) and [candidate card](candidate-card.md)
retain the same ID, tuple and scoped stop. Independent model review is
not human peer review or proof certification.
