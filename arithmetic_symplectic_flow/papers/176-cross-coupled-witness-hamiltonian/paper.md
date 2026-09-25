# A complete cross-coupled witness Hamiltonian with prime packets and a changed Floquet law

**Paper ID:** 176-cross-coupled-witness-hamiltonian  
**Candidate ID:** ASFS-20260915-XWH01  
**Date:** 2026-09-15  
**Status:** ADVANCE — COMPLETE CROSS-COUPLED PRIME PACKETS AND CHANGED FLOQUET LAW; NATURALNESS OPEN.  
**Route:** Owner-level audit only; formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

The frozen full Hamiltonian adds a position-dependent transverse coupling
to the rational divisor-witness construction. Its entire energy 1 is regular
and its ambient flow complete. Its actual maximal bi-return section is a
positive-dimensional symplectic domain, with a narrower invariant-product
interval than its uncoupled antecedent. The full energy still has exactly
one primitive closed orbit per prime, not a selected central subsystem.
The actual primitive periods remain those of the antecedent rational well,
T_p=2 sqrt(2) log p+O(1), while the transverse Floquet exponent changes to
Lambda_p=3 sqrt(2) log p+O(1). The roof and exponent are different actual
integrals. The composition changes both the force away from the axis and
the transverse growth along it; this is not a new primitive clock, an
irreducibility theorem or a naturalness result. The ordinary full-orbit
product retains its precise absolute-convergence boundary. No trace,
Fredholm representation or target-divisor claim is supplied.

## 1. Identity, lineage and construction question

The [version-1 card](candidate-card.md) predates the proof and fixes the
complete generator, energy, section and time units under
[180 Lane H](../180-constructive-coupling-frontier/candidate-card.md).
The nearest antecedent is [171](../171-separatrix-witness-hamiltonian-clock/paper.md).
Its generator is not this generator; its return-domain or stability
statements are not inherited. An axis equality proved below explains
the unchanged primitive times without identifying the full flows.

The exact [prime-symbolic lineage](../../docs/prior_work/README.md) is
prime/composite divisor symbols -> their full witness-exclusion constraint
-> conservative scalar well/escape deformation -> a coupled four-dimensional
Hamiltonian and its actual two-dimensional Poincare map. For all 2<=d<n,
w(n,d)=1_{d divides n}; their zero-count condition is the retained arithmetic
observable. The ODE uses the static full count, not a chronological sieve,
and n remains an invariant component. No conjugacy to a historical Logistic
or Henon map is claimed. The design is not a generic arithmetic-space seed.

The bounded question is whether the prescribed cross term can be retained
in one complete owner, with every periodic state and the actual coupling
accounted for. Naturalness is OPEN, not an automatic rejection of a valid
construction and not an unproved premise of it.

| Item | Exact owner / limitation |
| --- | --- |
| Full carrier | Every real state on every integer component of the canonical four-manifold, followed by its entire preselected energy 1 |
| Flow | The autonomous coupled equations (2), in their original time units |
| Base | Actual first return on the maximal bi-return domain (7), with induced dQ wedge dP |
| Roof | Actual elapsed period tau_n(I), not the transverse exponent Lambda_n(I) |
| Full periodic ledger | Derived from all full-energy periodic equations, including all nonreturning states |
| Ordinary zeta | Complete unweighted primitive-orbit product with these same periods |
| Absent owners | Transfer space, trace, Fredholm determinant, contact and quantum construction NOT SUPPLIED |

## 2. Frozen generator and complete dynamics

For n>=2 write a=a(n), c=c_n, and set

\[
a(n)=\sum_{2\le d<n}\mathbf1_{\{d\mid n\}},\quad c_n=1+n^{-2},\quad
W(q)=\frac{4q^2}{(1+q^2)^2},\quad b(q)=1+\frac{W(q)}2,
\]
\[
\mathcal X=\coprod_{n\ge2}\mathbb R^4_{q,p,Q,P},\quad
\Omega=dq\wedge dp+dQ\wedge dP,
\]
\[
H_n=\frac{p^2}{2}+(1-a)cW(q)+8aq+b(q)QP,
\qquad \mathcal E=\coprod_{n\ge2}H_n^{-1}(1).
\tag{1}
\]

This countable disjoint union is a second-countable smooth four-manifold.
No connectedness or compactness is asserted. All trial divisors, the uniform
rational rule c_n, the fixed numbers 8 and 1/2 and energy 1 are design inputs.
There is no prime list, zero data, assigned logarithmic period, prime-specific
choice or post-proof coefficient change. Ordinary divisibility gives
a(n)=0 exactly on primes, with no dynamical naturalness conclusion attached.

Using i_X Omega=dH gives the coupled equations

\[
\dot q=p,\qquad
\dot p=-\left((1-a)c+\frac{QP}{2}\right)W'(q)-8a,
\qquad \dot Q=b(q)Q,\quad\dot P=-b(q)P.
\tag{2}
\]

Consequently I=QP is conserved. With the constant-on-orbit notation

\[
B=(1-a)c+I/2,\quad U_I(q)=BW(q)+8aq,\quad E=1-I,
\]
\[
\frac{p^2}{2}+U_I(q)=E\quad\hbox{on }\mathcal E.
\tag{3}
\]

The original scalar energy from 171 is generally not conserved here;
the invariant reduction (3) includes the interaction. In particular
pdot has a genuine I-dependent term and transverse growth depends on q.

### Proposition 1. Full completeness and regular energy

The entire ambient flow is complete in both time directions, every energy
1 component is regular, and the full transverse section is

\[
\Sigma=\{H=1,q=0,p>0\}
\simeq\coprod_{n\ge2}\{(Q,P):QP<1\},\quad
p=\sqrt{2(1-QP)},\quad\omega_\Sigma=dQ\wedge dP.
\tag{4}
\]

**Proof.** Direct differentiation gives

\[
0\le W\le1,\qquad 1\le b\le3/2,\qquad
W'(q)=\frac{8q(1-q^2)}{(1+q^2)^3},\qquad |W'|\le4.
\tag{5}
\]

On any fixed trajectory, a,c,I and hence B are fixed. Its acceleration
is bounded by 4 abs(B)+8a. Thus p and q cannot escape in finite time.
If K(t)=integral_0^t b(q(u)) du, then Q(t)=e^{K(t)}Q(0) and
P(t)=e^{-K(t)}P(0), with abs(K(t))<=3 abs(t)/2. These coordinates
also remain bounded on finite time intervals. Smooth local existence
therefore extends in both directions. The bound need not be uniform in
n or I: trajectories do not switch components or invariant products.

At a critical point of H, positivity of b forces Q=P=0 and hence I=0;
also p=0. On a composite component,

\[
\partial_qH\big|_{I=0}=8a-(a-1)cW'
\ge8a-5(a-1)=3a+5>0,
\tag{6}
\]

using c<=5/4. A prime component has only q=0 or q=+/-1 as its
remaining critical candidates, at energies 0 or c>1. None lies on
energy 1. At q=0, W=0 and b=1, proving (4); qdot=p>0 makes
the section transverse. Pullback of Omega gives the displayed form. ∎

The estimate (6) is asserted only at I=0. It is not a global composite
force estimate for the coupled generator.

## 3. Actual maximal return, with no states discarded

For a prime label and I in the open interval below, put
E=1-I, B=c+I/2 and let A_n(I) in (0,1) solve BW(A_n(I))=E.
Define two different actual orbit integrals:

\[
M=\coprod_{n:\,a(n)=0}
\left\{(Q,P):-\frac{2}{3n^2}<I=QP<1\right\},
\tag{7}
\]
\[
\tau_n(I)=4\int_0^{A_n(I)}\frac{dq}{\sqrt{2(E-BW(q))}},
\qquad
\Lambda_n(I)=4\int_0^{A_n(I)}
\frac{b(q)\,dq}{\sqrt{2(E-BW(q))}}.
\tag{8}
\]

### Proposition 2. Exact return domain and uniform non-Zeno roof

The set (7) is exactly the operational maximal bi-return domain of the
full section (4). Its saturation consists precisely of the prime inner
scalar ovals 0<E<B, with all compatible transverse states. Both integrals
in (8) are smooth on their stated interval, and uniformly on M,

\[
\tau_n(I)\ge\pi/7>0,\qquad
\tau_n(I)<\Lambda_n(I)<\tfrac32\tau_n(I).
\tag{9}
\]

**Proof.** For all composite energy states, not just section states, set

\[
J_a(q)=\frac{1+(a-1)cW(q)-8aq}{b(q)}.
\]

The exact energy equation is p^2/2=b(q)(J_a(q)-I). Differentiation gives

\[
b^2J_a'=((a-1)c-1/2)W'+4a(qW'-W-2).
\]

For a>=1, abs((a-1)c-1/2)<=5a/4. Writing t=q^2 gives
qW'-W=4t(1-3t)/(1+t)^3<=1/3: for t>=1/3 it is nonpositive,
and otherwise 4t(1-3t)<=1/3. With (5) this proves
b^2 J_a'<=5a-20a/3=-5a/3<0. Also J_a(0)=1 and J_a tends
to minus/plus infinity as q tends to plus/minus infinity. Thus every
real I has exactly one turning position q_I=J_a^{-1}(I), and the
whole allowed scalar region is q<=q_I. At the turning point,
U_I'(q_I)=-b(q_I)J_a'(q_I)>0, so it is simple and reached in finite
time from any nearby allowed point. Every scalar energy branch turns
once and escapes left in both time directions; no bounded oval or
saddle is hidden. For section states I<1, q_I>0. The trajectory
returns through q=0 with negative momentum and never again with positive
momentum. Therefore no composite state belongs to M. This proves the
claim without assuming global monotonicity of the coupled momentum.

For primes, B=c+I/2. If I>1 then E<0 and B>0, so no real energy
state exists. If I=1 the only scalar state is q=p=0 and QP=1.
For I<1 one has E>0. If B<=0, p never vanishes and q is monotone.
If B>0 the even rational potential has maxima B at q=+/-1 and tends
to 0 at either infinity. It gives the exhaustive branch list:

| Prime reduced branch | Full-state retention and section behavior |
| --- | --- |
| 0<E<B, inner component | One oval between +/-A_n(I), with one positive section crossing per period |
| 0<E<B, outer components | abs(q)>=1/A_n(I)>1; simple turning and escape, no section hit |
| E=B | Scalar saddles and separatrix branches; no finite repeated positive section hit |
| E>B or B<=0 | Nonvanishing p and monotone scattering; at most one section hit |
| I=1, E=0 | Scalar equilibrium q=p=0 with nonconstant transverse motion |
| I>1 | No real prime energy state |

The identity 1-W(q)=((1-q^2)/(1+q^2))^2 gives a double energy
zero at the saddles when E=B; their approach time is infinite.
The condition 0<E<B is precisely -2(c-1)/3<I<1. Only its inner
component returns. This proves (7), including both time directions.

The oval has a transverse positive section hit, so smooth dependence of
the ODE and the implicit return equation proves smooth tau. Integrating
the smooth b along that smoothly varying orbit proves smooth Lambda.
For a uniform period bound take the clockwise angle of (q,p) on its
inner oval. There B>0, abs(q)<1 and B<c+1/2<=7/4. Thus

\[
0\le BqW'(q)\le14q^2,\quad
0<\dot\theta=\frac{p^2+BqW'(q)}{q^2+p^2}\le14.
\tag{10}
\]

The angle advances by 2 pi per period, so tau>=pi/7. On an inner
oval, b>=1 with strict inequality except at isolated q=0 crossings;
b<3/2 throughout because abs(q)<1. Integration gives (9). ∎

The composite monotonicity assertion is about the energy-coordinate
function J_a, not the force U_I'. It accounts for every real I on the
entire fixed energy; Section 5 also supplies a direct all-state closure
test. No scalar potential or energy branch is removed.

### Proposition 3. Symplectic return and exact suspension owner

On the entire domain (7), the genuine return is

\[
F(n,Q,P)=(n,e^{\Lambda_n(I)}Q,e^{-\Lambda_n(I)}P),\qquad I=QP.
\tag{11}
\]

It is a smooth symplectomorphism, with roof tau_n(I), and its complete
endpoint-glued suspension is smoothly conjugate to exactly the return-
saturation in Proposition 2, in unchanged physical time.

**Proof.** The scalar oval and Q,P solutions give (11). Since I is
preserved, the inverse replaces Lambda by -Lambda, on the same domain.
For l(I)=Lambda_n(I), dI=P dQ+Q dP gives

\[
d(e^lQ)\wedge d(e^{-l}P)
=dQ\wedge dP-Pl' dQ\wedge dI+Ql'dI\wedge dP
=dQ\wedge dP.
\tag{12}
\]

The map [z,t] -> Phi^t(z) respects (z,tau(z))~(Fz,0). Every
saturated state has a unique elapsed representative 0<=t<tau(z)
from its last positive section crossing. Flow-box charts and transverse
smooth returns give local smooth inverses, including at the seam.
It is therefore a flow conjugacy onto that saturation. The bound (9)
prevents infinitely many positive or negative hits in finite time.
Equivalently, along each fixed I all its return times are identical
and positive. The complementary energy states are not deleted or
identified with this suspension. ∎

Canonical ambient volume and section area are preserved; the suspension
has its corresponding area-times-time volume. No finite normalization
of these volumes or any trace normalization is supplied. The energy and
suspension are three-dimensional, not symplectic manifolds; the ambient
four-manifold and section two-manifold are symplectic.

## 4. Interaction versus an inherited clock

The cross term changes actual dynamics: at q=1/2 and I!=0 the additional
force is -I W'(1/2)/2!=0. At the same points the transverse rate is
b(1/2)=1+8/25=33/25, not 1. Thus in the declared physical coordinates
both the scalar force and the transverse rate interact. I remains an
integral, so this observation is not a claim of chaotic feedback or
nonintegrability. The admissible return interval really changes from
171's -n^-2<I<1 to (7), which is a stricter interval.

The invariant axis Q=P=0 has I=0, and there (1) restricts exactly to
p^2/2+(1-a)cW+8aq. Its physical orbit and clock agree with that
scalar restriction of 171. That equality is a derived restriction of
the new generator, not a transfer of the entire old return owner.

## 5. Complete primitive ledger and transverse Floquet law

### Proposition 4. One primitive orbit per prime, with changed stability

Every full-energy closed orbit lies on Q=P=0. There is exactly one
primitive oriented flow orbit gamma_p for each prime p and none for
composites. Set

\[
T_p=\tau_p(0),\qquad L_p=\Lambda_p(0).
\tag{13}
\]

Its least map period is one, its r-fold repetition has time r T_p,
and its transverse monodromy is

\[
DF^r(0,0)=\operatorname{diag}(e^{rL_p},e^{-rL_p}),\quad
\det(I-DF^r)=2-e^{rL_p}-e^{-rL_p}<0.
\tag{14}
\]

**Proof.** For any positive time t, K(t)=integral_0^t b(q(u))du>=t.
If a full state closes, Q=e^{K(t)}Q and P=e^{-K(t)}P force Q=P=0.
This argument applies to every real state of the entire energy, not
only its returning portion. Then I=0 and the scalar energy is 1.
On composites (6) makes pdot strictly negative. On primes 0<1<c_p,
so there is exactly one inner closed oval; the two outer branches are
not closed. Its negative-momentum half is not a second oriented packet.
Every full closed orbit has consequently been counted.

On M, I invariance gives F^r(Q,P)=(e^{rLambda_n(I)}Q,
e^{-rLambda_n(I)}P). Since Lambda>0, only Q=P=0 is periodic.
At the origin dI=0, so differentiation proves (14). The neutral
autonomous time/energy directions have not been mistaken for transverse
Poincare degeneracy. ∎

In particular, nonreturning scalar equilibria, scattering or separatrix
states cannot supply hidden closed full orbits: if their transverse pair
is nonzero, K>0 excludes closure, and the entire remaining I=0 axis
was classified in the proof. This is complete periodic accounting
without restricting the full carrier to selected centres.

### Proposition 5. Physical time and Floquet exponent have different logarithmic coefficients

Uniformly along prime packets,

\[
T_p=2\sqrt2\log p+O(1),\qquad
L_p=3\sqrt2\log p+O(1),\qquad T_p<L_p<3T_p/2.
\tag{15}
\]

The first law is unchanged from the corresponding scalar restriction of
171. The second is the new actual transverse law, not a rescaled roof.

**Proof.** For any integer n>=2 use the well-only comparison integral
at E=1,B=c_n (only prime labels give actual closed orbits). Put
delta=1/sqrt(n^2+1) and y=(1-q^2)/(1+q^2). If A solves cW(A)=1,
then y runs from 1 to delta and

\[
f(y)=-\frac{dq}{dy}=(1+y)^{-3/2}(1-y)^{-1/2},\quad
T_n=\frac4{\sqrt{2c}}\int_\delta^1
\frac{f(y)}{\sqrt{y^2-\delta^2}}\,dy.
\tag{16}
\]

Here f(0)=1 and abs(f(y)-1)<=C_0 y on [0,1/2]. Since
delta<=1/sqrt5<1/2, the replacement of f by 1 on [delta,1/2]
costs at most C_0 sqrt(1/4-delta^2)<=C_0/2. On [1/2,1), the
denominator is at least sqrt(1/20) and f is integrable. Thus

\[
\int_\delta^1\frac{f(y)}{\sqrt{y^2-\delta^2}}\,dy
=\operatorname{arcosh}(1/(2\delta))+O(1)
=\log(1/\delta)+O(1).
\tag{17}
\]

All errors are uniform. Now log(1/delta)=log n+(log c)/2 and
abs((c^{-1/2}-1)log n)<=n^{-2}log n is bounded. Equations
(16)--(17) yield T_n=2 sqrt2 log n+O(1).

Because b=3/2-(1-W)/2 and 1-W=y^2, the actual exponent is

\[
L_n=\tfrac32 T_n-\tfrac12 R_n,\qquad
R_n=\frac4{\sqrt{2c}}\int_\delta^1
\frac{y^2f(y)}{\sqrt{y^2-\delta^2}}\,dy>0.
\tag{18}
\]

The upper-half contribution is uniformly bounded as above. On
[delta,1/2], f is bounded and y^2<=y/2, so its contribution is
bounded by a constant times integral_delta^{1/2}
y/sqrt(y^2-delta^2)dy=sqrt(1/4-delta^2). Hence R_n=O(1)
uniformly. Substitution proves the second asymptotic in (15).
The two strict inequalities are the I=0 case of (9). ∎

The different transverse multipliers exclude a C^1 time-preserving
flow conjugacy to 171 that maps a given gamma_p to its corresponding
prime packet: such a conjugacy conjugates the Poincare derivatives,
whereas here e^{L_p}!=e^{T_p}. This is a specified obstruction only.
No assertion is made against arbitrary orbit equivalence, a time change,
different packet assignments or every possible smooth coordinate scheme.

## 6. Owned ordinary orbit product

The sole analytic object is the full unweighted product

\[
\log Z(s)=\sum_{p\ {\rm prime}}\sum_{r\ge1}\frac{e^{-srT_p}}r,
\qquad Z(s)=\prod_p(1-e^{-sT_p})^{-1}.
\tag{19}
\]

It uses physical T_p, not L_p and not an assigned log-p roof. There
are no stability or von Mangoldt weights.

### Corollary 6. Exact absolute logarithmic-series abscissa

The logarithmic series is absolutely and locally uniformly convergent
on Re s>1/(2 sqrt2), defining nonzero holomorphic Z there, and fails
absolute convergence for Re s<=1/(2 sqrt2). Every finite physical
time window contains finitely many primitive packets and repetitions.

**Proof.** Let C=2 sqrt2. By (15), abs(T_p-C log p)<=B_0 for
a fixed constant, while (9) gives T_p>=pi/7. For sigma>0,

\[
\sum_{r\ge1}\frac{e^{-\sigma rT_p}}r
\le\frac{e^{-\sigma T_p}}{1-e^{-\sigma\pi/7}}.
\tag{20}
\]

When C sigma>1 this is summable by comparison with all integers to
the power -C sigma, also locally uniformly. When 0<C sigma<=1,
the r=1 terms dominate a positive multiple of 1/p. The divergence
of sum_p 1/p follows without a prime-number theorem: if it converged,
the finite Euler products product_{p<=N}(1-1/p)^{-1} would be
bounded, since -log(1-1/p)<=2/p. Unique factorization makes each
such product at least sum_{m<=N}1/m, a contradiction. For sigma<=0
the repetitions of any single prime already diverge absolutely.
The uniform log-size estimate and positive period bound give the finite
time-window assertion. These are ordinary product facts, not an operator
or continuation theorem. ∎

## 7. Controls, limits and gate assessment

| Control or objection | Exact response and boundary |
| --- | --- |
| Composite force inherited from 171 | Rejected: n=4, a=1, q=1/2, Q=1, P=-100 and p=sqrt(258) give H=1 but pdot=344/5>0. Proposition 2 uses the monotone energy-coordinate J_a, not globally monotone momentum |
| Remove cross term WQP/2 | Recovers 171's distinct generator, its wider return strip and transverse exponent T; demonstrates a real interaction effect, not a new primitive clock |
| Remove the entire transverse term bQP | Q,P become constant and prime ovals have continuously many full closed copies; finite multiplicity is enforced dynamically here |
| Remove witness count | Every integer acquires the same kind of inner packet; arithmetic exclusion genuinely uses the divisor symbols |
| Replace count by any nonnegative integer constraint | The I=0 full closed-orbit proof retains its zero set; PROVES_TOO_MUCH for a claim that geometry canonically singles out primes |
| Retain all ambient energies | At Q=P=0 a prime has inner ovals for every energy between 0 and c_p; the packet theorem is about the entire energy 1 fixed before proof |
| Treat Lambda as roof | Would change physical time and the zeta owner; not performed |
| Identify suspension with entire energy | False: outer, separatrix and other nonreturning states are retained separately; all were covered by the full closure test |
| Replace rational barrier by constant c>1 | The same axis gives common periods; logarithmic growth depends on the declared size rule, not canonical arithmetic necessity |
| Import 174 or 179 transfer data | Different source/flow owners; not done, and no same-object trace or determinant is supplied |

The construction uses finitely many smooth ingredients with every interaction
written explicitly. It supplies no infinite-layer convergence claim. The
source is static and componentwise, the potential and energy engineered,
and arithmetic naturalness remains OPEN. No prime-table or zero-data fit
has been run. This is not a literature novelty or uniqueness assertion.

| Gate / field | Result for ASFS-20260915-XWH01 |
| --- | --- |
| P0 owner | ESTABLISHED: complete full Hamiltonian, regular energy, exact maximal symplectic return and actual non-Zeno suspension owner |
| Owner-level A0 relevance | CONSTRUCTION POSITIVE: derived prime support and physical logarithmic size; naturalness OPEN, not formal A0 PASS |
| Owner-level A1 | ESTABLISHED: full primitive multiplicity, orientation, repeats and changed Floquet integrals |
| Owner-level ordinary A2 consequence | ESTABLISHED only for (19) and its precise convergence region; operator/trace/continuation NOT SUPPLIED |
| Formal Route coordinates | UNASSIGNED; no target/divisor evaluation |
| Route B | NOT INVOKED |

**Decision: advance the frozen coupled construction.** The decisive result
is complete same-object interaction and periodic ownership with a changed
transverse law. It is explicitly not another new primitive clock. This
bounded lane ends here; stronger operator, naturalness or irreducibility
claims require their own evidence, and any object change a new card.

## Reproducibility and disclosure

The proof consists of exact ODE, energy, return and integral estimates
(1)--(20), not finite numerical observations. No integrator, prime table,
cutoff, precision-fit, external-model upload, script, TeX or PDF artifact
is used. The [evidence index](evidence/README.md),
[claim ledger](claim-ledger.md) and actual different-invocation
[mathematical review](evidence/review.md) record evidence and limits.
ARS was used solely for bounded claim/evidence/reasoning and counterargument
discipline under the approved construction question, not a publication
workflow or venue-fit claim. Model-assisted authoring and review are not
human peer review or an independent-error certificate. There are no
human-subject data or external-funding claims.
