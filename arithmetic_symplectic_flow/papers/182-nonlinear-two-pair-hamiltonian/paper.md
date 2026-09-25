# Complete prime packets in a nonlinear two-pair Hamiltonian

**Paper ID:** 182-nonlinear-two-pair-hamiltonian  
**Candidate ID:** ASFS-20260915-NHC01  
**Date / evidence:** 2026-09-15; theorem-level construction with stated OPEN ownership fields.  
**Status:** ADVANCE — COMPLETE NONLINEAR TWO-PAIR HAMILTONIAN PACKETS; GLOBAL RETURN OWNER OPEN; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

A fixed bounded nonlinear interaction joins two hyperbolic canonical pairs
to the proper-divisor witness oscillator on the entire energy 1 of a
six-dimensional Hamiltonian. The full ambient flow is complete, its energy
is regular, and a strict global transverse Lyapunov inequality forces every
closed trajectory onto the invariant oscillator axis. The complete energy
therefore has exactly one primitive oriented closed orbit per prime, no
composite closed orbit and no off-axis periodic continuum. The original
Hamiltonian time satisfies T_p = 2 sqrt(2) log p + O(1), and all repeated
transverse multipliers are two copies of exp(plus or minus r T_p).
The interaction changes actual off-axis forces and destroys the individual
transverse product integrals of the uncoupled comparator; it does not change
the primitive clock or its linear Floquet law. An explicit escaping section
point prevents the entire section from being a return base. The global
positive-dimensional invariant return domain and ASFS suspension P0 remain
OPEN. The result is a complete Hamiltonian closed-ledger construction, not
a completed suspension, natural arithmetic mechanism, trace theorem or
formal Route pass.

## 1. Exact identity and question

The [version-1 card](candidate-card.md) froze the following full object
before this audit. For every integer n >= 2 put

\[
a=a(n)=\sum_{2\le d<n}\mathbf1_{\{d\mid n\}},\quad
c=c_n=1+n^{-2},\quad W(q)=\frac{4q^2}{(1+q^2)^2},\quad
\epsilon=\frac1{100},
\]
\[
\Psi=\tanh Q_1\tanh P_1\tanh Q_2\tanh P_2,\qquad
V_{n,a}(q)=(1-a)cW(q)+8aq,
\]
\[
\mathcal X=\coprod_{n\ge2}\mathbb R^6_{q,p,Q_1,P_1,Q_2,P_2},\qquad
\Omega=dq\wedge dp+dQ_1\wedge dP_1+dQ_2\wedge dP_2,
\]
\[
H_n=\frac{p^2}{2}+V_{n,a}(q)+Q_1P_1+Q_2P_2+\epsilon W(q)\Psi,
\qquad \mathcal E=\coprod_{n\ge2}H_n^{-1}(1).
\tag{1}
\]

Use the disjoint-union smooth topology, the convention
\(\iota_X\Omega=dH\), and unmodified Hamiltonian time. The carrier is a
second-countable smooth six-manifold, not a connected or compact one.
Every integer and every real state are present. The main owner is the
**entire** energy, not its axis, a chosen strip, a local section or a
symbolic replacement.

| Ledger item | Owner and actual scope |
| --- | --- |
| Arithmetic data | a(n) from every proper divisibility test, and the uniform rational rule c_n; no prime list, zero data or logarithmic roof is an input |
| Dynamics and clock | Exactly (1), energy 1, and its physical flow; no reparametrization |
| Complete carrier | Entire regular five-dimensional energy in the six-dimensional ambient symplectic manifold, proved below |
| Symbolic lineage | The zero set of the complete proper-divisor witness observable is preserved by the well/escape deformation and the nonlinear conservative lift |
| Closed ledger | All full-energy nonconstant closed trajectories, modulo oriented time translation; multiplicity and repetitions derived below |
| Section and local map | Full section and prime-packet Poincare germs derived in Section 5; not an invariant global base |
| Global symplectic base, roof and suspension | OPEN; no full strip or return formula borrowed from 171 or 176 |
| Analytic / later owner | Transfer operator, analytic zeta theorem, Fredholm determinant, trace, contact and quantum constructions NOT SUPPLIED |

The [prior-work guide](../../docs/prior_work/README.md) motivates the arrow
from prime/composite symbols through conservative dimensional lifts. Here
the exact retained source is a(n)=0 if and only if n is prime. It is a
static arithmetic coefficient, not a claim that the ODE executes trial
divisions or moves between integers. There is no claimed conjugacy to a
historical Logistic or Henon map. The rational near-barrier choice and
bounded interaction are declared designs; source-naturalness remains OPEN.

The bounded question is whether a genuine nonlinear two-pair interaction
can preserve a complete prime-only Hamiltonian ledger without discarding
off-axis states. A new primitive clock, nonintegrability, chaos and a
global suspension are not presumed.

## 2. Full equations and a global escape inequality

Hamilton's equations on every real state are

\[
\dot q=p,\quad
\dot p=-V'_{n,a}(q)-\epsilon W'(q)\Psi,
\]
\[
\dot Q_j=Q_j+\epsilon W(q)\Psi_{P_j},\qquad
\dot P_j=-P_j-\epsilon W(q)\Psi_{Q_j},\qquad j=1,2.
\tag{2}
\]

Elementary differentiation gives

\[
0\le W\le1,\qquad
W'(q)=\frac{8q(1-q^2)}{(1+q^2)^3},\qquad |W'|\le4,
\tag{3}
\]

using \(|1-q^2|\le1+q^2\) and \(2|q|\le1+q^2\).
Also \(|\Psi|\le1\) and each of its four first partial derivatives
has absolute value at most 1.

### Proposition 1. Strict full-state transverse growth

Set

\[
S=Q_1^2+Q_2^2+P_1^2+P_2^2,\qquad
L=Q_1^2+Q_2^2-P_1^2-P_2^2.
\]

On the entire ambient space, at every energy and every integer,

\[
\dot L\ge2(1-\epsilon W)S\ge\frac{99}{50}S.
\tag{4}
\]

**Proof.** Equation (2) gives

\[
\dot L=2S+2\epsilon W
\sum_{j=1}^2\left(Q_j\Psi_{P_j}+P_j\Psi_{Q_j}\right).
\]

For example

\[
|Q_1\Psi_{P_1}|=
|Q_1\tanh Q_1|\,\operatorname{sech}^2P_1
|\tanh Q_2\tanh P_2|\le Q_1^2.
\]

The other three terms are bounded respectively by Q_2^2, P_1^2
and P_2^2 because \(|x\tanh x|\le x^2\). Their sum has absolute
value at most S. Since W is nonnegative, (4) follows. No invariant
product, small initial state, energy restriction or sign of a was used. ∎

If a full trajectory closes after time T > 0, integration of (4) over
one period gives \(0\ge(99/50)\int_0^T S(t)dt\). Continuity and
nonnegativity imply S(t)=0 identically. Thus **every** closed trajectory
lies on the axis Q_1=P_1=Q_2=P_2=0. This is a consequence for the full
carrier, not the definition of a reduced carrier. L is signed: (4)
does not assert that S is increasing or that every off-axis state
escapes in forward time. Stable directions may decay forward in time.

### Proposition 2. Complete ambient flow and regular energy

The flow of (1) exists for every real time from every real initial state.
Every component of H=1 is regular. For composites the stronger global
estimate

\[
\dot p\le-(3a+5)+4\epsilon\le-\frac{199}{25}<0
\qquad(a\ge1)
\tag{5}
\]

holds on all energies and all transverse states.

**Proof.** On a fixed integer component, c <= 5/4 and (2)--(3) imply

\[
|\dot p|\le5|1-a|+8a+4\epsilon=:C_n,
\qquad |\dot Q_j|\le|Q_j|+\epsilon,
\qquad |\dot P_j|\le|P_j|+\epsilon.
\tag{6}
\]

For |t| <= R, integration bounds |p(t)| by |p(0)|+C_n R and
|q(t)| by |q(0)|+|p(0)|R+C_n R^2/2. Each transverse coordinate
x satisfies \(|x(t)|\le(|x(0)|+\epsilon)e^R-\epsilon\), by the
integral inequality in either time direction. Thus no coordinate can
escape on a finite interval. Smooth local ODE existence extends globally.
No bound uniform in n is needed: a trajectory never changes component.
Hamiltonian conservation follows from dH(X)=Omega(X,X)=0.

At a critical point of H its vector field vanishes, so (4) forces S=0.
The interaction and its first derivatives then vanish, and p=0. If
a >= 1,

\[
V'_{n,a}(q)=8a-(a-1)cW'(q)
\ge8a-5(a-1)=3a+5.
\]

There is no critical point on any composite component. If a=0, the
remaining candidates are q=0 or q=plus or minus 1, with energies 0
or c>1. None is on H=1. This proves regularity. Applying the same
force bound without setting S=0, and using |epsilon W' Psi| <=
4 epsilon, proves (5). ∎

This bounded interaction avoids the large-invariant force reversal that
required a different full-energy argument in [176, Section 3](../176-cross-coupled-witness-hamiltonian/paper.md#3-actual-maximal-return-with-no-states-discarded).
That comparison is not an inheritance of its conserved I or return domain.

## 3. Complete primitive ledger and actual physical periods

### Proposition 3. Exactly one primitive packet per prime

The complete energy \(\mathcal E\) has precisely one nonconstant
primitive oriented closed orbit gamma_p on each prime component p, and
none on composite components. There are no off-axis closed packets,
continuous periodic families or additional higher-primitive-period packets.

**Proof.** Proposition 1 forces any closed trajectory onto the whole
transverse-zero axis. That axis is invariant by (2), because Psi and all
its first partial derivatives vanish there. The restricted physical
Hamiltonian is exactly

\[
h_{n,a}(q,p)=\tfrac12p^2+(1-a)c_nW(q)+8aq,
\qquad h_{n,a}=1.
\tag{7}
\]

For composites (5) precludes closure. For a prime, W is even, increases
strictly from 0 to 1 on 0<q<1 and decreases strictly from 1 to 0 on
q>1. Since 0<1<c, the equation cW(q)=1 has four simple roots
\(-B,-A,A,B\), where 0<A<1<B and B=1/A. The scalar energy set
is one bounded inner oval over [-A,A], plus an unbounded left branch
over q<=-B and an unbounded right branch over q>=B. Each outer
branch has only one turning point and escapes; neither closes.
The inner oval has no equilibrium, is traversed as a single periodic
orbit, and has finite period because its turning roots are simple.

Every full-energy closed trajectory has already been reduced by (4) to
this complete scalar classification. Nonreturning or scattering off-axis
states cannot create an omitted orbit. The negative-momentum half of the
oval belongs to the same oriented trajectory, not a second primitive
packet. Its first positive-momentum crossing of q=0 after time 0 is
exactly one full traversal. ∎

Write T_p for the time of that traversal. Its r-fold repetition has time
r T_p, for every positive integer r. This is the repetition of the same
physical orbit, not an independent composite component indexed by p^r.
Composite labels, including p^r for r>=2, still have no primitive packet.

### Proposition 4. Identified axis clock, not a new clock

Uniformly along prime packets,

\[
T_p=2\sqrt2\log p+O(1).
\tag{8}
\]

**Proof and dependency boundary.** The restriction (7), with a=0,
is literally the same scalar equation with the same energy and time as
[171, Proposition 5](../171-separatrix-witness-hamiltonian-clock/paper.md#proposition-5-uniform-logarithmic-size-estimate).
Only that scalar restriction is identified. Its actual integral is

\[
T_n=4\int_0^{A_n}\frac{dq}{\sqrt{2(1-c_nW(q))}},
\qquad c_nW(A_n)=1,\quad 0<A_n<1.
\tag{9}
\]

For completeness, put delta=1/sqrt(n^2+1) and
y=(1-q^2)/(1+q^2). Then 1-W=y^2 and

\[
f(y)=-\frac{dq}{dy}=(1+y)^{-3/2}(1-y)^{-1/2},\qquad
T_n=\frac4{\sqrt{2c_n}}\int_\delta^1
\frac{f(y)}{\sqrt{y^2-\delta^2}}\,dy.
\tag{10}
\]

On [0,1/2], f(0)=1 and |f(y)-1|<=C y. Replacing f by 1
on [delta,1/2] therefore costs at most C/2. On [1/2,1), the
denominator is at least sqrt(1/20), since delta^2<=1/5; f is
integrable there. All errors are uniform. The remaining integral is
arcosh(1/(2 delta))=log(1/delta)+O(1). Consequently

\[
T_n=\frac{2\sqrt2}{\sqrt{c_n}}\log(1/\delta)+O(1)
=2\sqrt2\log n+O(1),
\]

because log(1/delta)=log n+(log c_n)/2 and
\(|(c_n^{-1/2}-1)\log n|\le n^{-2}\log n\) is bounded.
For composites (9) is only a well-only comparison integral; their actual
Hamiltonian includes the witness force and has no period. ∎

Thus the nonlinear lift retains, rather than improves, the axis clock.
The logarithm is obtained from a mechanical near-separatrix integral;
it was not inserted as a roof. This does not make the rational choice
c_n-1=n^-2 arithmetically canonical or produce exact T_p=log p.

## 4. Actual nonlinear feedback and its limits

The interaction is not a function only of I_1=Q_1P_1 and I_2=Q_2P_2.
Equation (2) gives

\[
\dot I_1=\epsilon W\tanh Q_2\tanh P_2
\left(P_1\tanh Q_1\operatorname{sech}^2P_1
      -Q_1\operatorname{sech}^2Q_1\tanh P_1\right).
\tag{11}
\]

This is genuinely nonzero at a real energy-1 point, not merely at an
unattainable coordinate tuple. Take n=2, q=1/2,
Q_1=1/2, P_1=Q_2=P_2=1/4 and

\[
\Psi_* =\tanh(1/2)\tanh^3(1/4),\qquad
p=\sqrt{2\left(\frac1{80}-\frac4{625}\Psi_*\right)}.
\tag{12}
\]

Here c_2 W(1/2)=4/5, I_1+I_2=3/16, and
epsilon W(1/2)=4/625. The quantity under the inner parentheses is
at least 1/80-4/625=61/10000>0, and direct substitution gives H=1.
For t>0, k(t)=2t/sinh(2t) is strictly decreasing, because
sinh(2t)-2t cosh(2t)<0. The bracket in (11) equals
\(\tanh Q_1\tanh P_1[k(P_1)-k(Q_1)]\), which is positive at
(12). Thus I_1 is not conserved. Its force on the oscillator also
changes by

\[
-\epsilon W'(1/2)\Psi_*=-\frac{48}{3125}\Psi_*\ne0.
\tag{13}
\]

The feedback between pairs is explicit as well:

\[
\partial_{Q_2}\dot Q_1
=\epsilon W\tanh Q_1\operatorname{sech}^2P_1
\operatorname{sech}^2Q_2\tanh P_2>0
\]

at (12). These are trajectory changes in the declared physical
coordinates. They do not prove nonintegrability, chaos, irreducibility
or impossibility of a different canonical conjugacy. No such theorem
is asserted. In particular a nonlinear interaction can be substantial
away from the axis while invisible to the linearized periodic data.

## 5. Local return geometry, stability and the global-base gap

The full transverse section has the exact coordinates

\[
\Sigma=\{H=1,q=0,p>0\}\simeq
\coprod_{n\ge2}\{(Q_1,P_1,Q_2,P_2):I_1+I_2<1\},
\]
\[
p=\sqrt{2(1-I_1-I_2)},\qquad
\omega_\Sigma=dQ_1\wedge dP_1+dQ_2\wedge dP_2.
\tag{14}
\]

Indeed W(0)=0 and qdot=p>0; pullback of Omega gives the displayed
nondegenerate four-dimensional form. Near each prime packet's section
origin, smooth ODE dependence and the transverse crossing at time T_p
give a smooth local first-return map germ fixing that origin. Along the
reference oval the only intermediate crossing has p<0; compactness of
the remaining orbit segments and transversality preserve this first-
return convention for sufficiently close initial points. The variable-
time Hamiltonian map preserves the section form: its extra time-vector
terms vanish on energy tangents because i_X Omega=dH.

Since Psi is fourth order in the transverse coordinates, its Hessian
there vanishes on the axis. The transverse linearized equations along
the prime orbit are exactly
\(\delta\dot Q_j=\delta Q_j\),
\(\delta\dot P_j=-\delta P_j\). The section energy correction
in p is second order, and the base transverse coordinates vanish on
the orbit, so the first-order return-time correction does not change
the transverse derivative. Hence the r-fold local Poincare germ has

\[
DF_p^r(0)=\operatorname{diag}
(e^{rT_p},e^{-rT_p},e^{rT_p},e^{-rT_p}),
\]
\[
\det(I-DF_p^r(0))=
\left(2-e^{rT_p}-e^{-rT_p}\right)^2>0.
\tag{15}
\]

These are nondegenerate transverse hyperbolic packets; the ordinary
neutral time/energy directions of an autonomous Hamiltonian are not
counted as transverse eigenvalues. Unlike 176's changed exponent,
this model has the same linear exponent T_p as two uncoupled pairs.

The entire section (14) is **not** a self-returning base. For example,
on n=2 take

\[
(q,p,Q_1,P_1,Q_2,P_2)=(0,2,1,-1,0,0).
\tag{16}
\]

It lies on H=1. The subspace Q_2=P_2=0 is invariant and there
the interaction and all its first derivatives vanish. The first pair
has I_1=-1 and the scalar motion has energy 2. Since c_2W<=5/4,
p stays positive with p>=sqrt(3/2), so q is strictly increasing and
there is no later section hit. This point and its full trajectory remain
in the owner.

The theorem neither identifies the maximal recurrent subset of (14)
nor proves it an open invariant symplectic manifold. A local map germ
or a formal set of all bi-infinite hits is not a supplied global
self-map F:M->M. Thus full return-domain geometry, its actual roof and
non-Zeno condition, the suspension identification and original ASFS
suspension P0 remain OPEN. Ambient physical completeness in Proposition 2
does not by itself close those return-specific obligations. This is the
declared stopping boundary for the current bounded lane.

## 6. Controls, negative results and naturalness

The following are diagnostic comparators, not retuned versions of (1).
The frozen candidate and all its proven fields remain unchanged.

| Control | Exact consequence and boundary |
| --- | --- |
| Composite-only labels | All real composite states satisfy (5), so there is no omitted composite periodic packet, not merely no axial one |
| Remove the witness by replacing a(n) with 0 on every integer | The same full-state escape proof leaves one inner primitive oval on every integer; the geometric shell is not intrinsically prime-selective |
| Replace a(n) by an arbitrary nonnegative integer-valued coefficient b(n) | The same estimates with a=b(n) produce precisely one primitive packet on each b(n)=0 component and none on b(n)>=1. This is an explicit PROVES_TOO_MUCH control on source-naturalness, not authorization to insert an arbitrary target into the main candidate |
| Set epsilon=0 | Two independent hyperbolic pairs give the same full closed ledger, axis periods and linear multipliers. What the nonzero frozen interaction adds is the actual nonlinear feedback (11)--(13), not new periodic data |
| Remove both quadratic hyperbolic terms while retaining the displayed interaction | On Q_2=P_2=0 the interaction gradient vanishes, so every constant (Q_1,P_1) accompanies a prime scalar oval. This comparator contains a continuum of closed trajectories; merely selecting transverse centres would lose multiplicity |
| Replace c_n by the constant 5/4 | The growth and composite estimates still apply, but all prime axis periods are the same constant. Thus arithmetic packet selection alone does not explain logarithmic time |
| Replace c_n by 1 | Prime energy 1 reaches the barrier: the inner periodic oval is lost and q=plus or minus 1 on the transverse-zero axis gives critical energy points. This different comparator does not inherit regularity or the period theorem |
| Keep every section point | Point (16) prevents an assertion that the full section is a return base. No escaping state is removed from the Hamiltonian ledger |
| Borrow a roof or operator | No unit roof, log-p roof, 171/176 global return strip or 179 scale-clock transfer is assigned to this Hamiltonian |

There is no finite orbit cutoff, fitted dataset, floating-point period
calculation or parameter optimization in this proof. All n and all real
states are covered by the displayed estimates; the asymptotic error in
(8) is uniform. This is not a claim that any finite check proves an
infinite statement. The witnesses, all-integer near-barrier rule, fixed
energy and chosen coupling remain engineered inputs. Mathematical
construction succeeds within its stated owner; naturalness remains OPEN
rather than being silently passed or treated as a refutation of the proof.

## 7. Gate assessment and bounded decision

| Question / gate | Exact evidence for ASFS-20260915-NHC01 | Status and limit |
| --- | --- | --- |
| Hamiltonian-level identity and full owner | Frozen (1), Propositions 1--2, no off-axis deletion | ESTABLISHED as an engineering construction |
| Original ASFS suspension P0 | Full section and local map germs only; explicit nonreturning point | OPEN: invariant positive-dimensional global base and suspension not supplied |
| A0-related arithmetic relevance | Full witness zero set selects the primitive Hamiltonian packets; rational physical logarithmic time derived | Construction evidence positive; source-naturalness OPEN; no formal A0 pass |
| A1-related Hamiltonian ledger | Entire energy, one oriented primitive per prime, all repetitions, full transverse monodromy | ESTABLISHED for this Hamiltonian; no inherited suspension A1 coordinate |
| A2 / analytic owner | No operator, trace, analytic zeta theorem or Fredholm construction in this lane | NOT SUPPLIED; formal coordinates UNASSIGNED |
| Route B | No formal Route-A readiness or separate evaluation | NOT INVOKED |

Decision: **advance** the complete nonlinear Hamiltonian construction as
a new geometric owner with a full periodic ledger. The decisive positive
fact is (4): the true coupled dynamics retain exact full-state packet
multiplicity without selecting an axis as the carrier. The decisive
limitation is also explicit: no global return owner has been established.
This bounded lane ends here; it does not repair the OPEN global base with
an unlimited local analysis or label unchanged clock/Floquet data as a new
clock. Any later return construction must use this same fixed generator
and actual time, or be a new candidate.

## Evidence and disclosure

The [candidate card](candidate-card.md), [claim ledger](claim-ledger.md)
and [evidence index](evidence/README.md) record the exact freeze, proof
dependencies and separate model-review provenance. The scalar period
restriction of 171 is identified in (7)--(10); its full return geometry
is not used. The relation to 176 is a comparison of generators and
linear stability, not credit transfer. No external literature expansion
or new empirical dataset was required for these self-contained estimates.

The controller proposed the bounded architecture; the author agent wrote
and derived this package. Separate invocations check the global estimate
and the finished manuscript, with proposal visibility and inherited
model/context disclosed in the evidence index. These are nonblind model
checks, not human peer review or independent-error certificates. There
are no human-subject data, publication claims, external uploads, code
experiments, or asserted funding/author declarations beyond those facts.
