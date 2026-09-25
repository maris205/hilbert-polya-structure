# Ordered physical return blocks with complete symplectic seams

**Paper ID:** 177-ordered-physical-segment-gluing  
**Candidate ID:** ALF-20260915-PSG01  
**Date:** 2026-09-15  
**Status:** ADVANCE — COMPLETE PHYSICAL RETURN-BLOCK COMPOSITION; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

We construct one event-glued physical flow over the entire bilateral
weakly ordered divisibility-cover source. A fixed smooth symplectic
transport identifies one full reference strip with every physical
return strip of a rational-barrier oscillator and hyperbolic plane.
Successive cut blocks are joined by the induced whole-section transport,
including the scalar entrance momentum. The complete flow is Hausdorff,
smooth along its three-dimensional leaves and non-Zeno in both directions.
Its return base is leafwise symplectic and its roof is exactly elapsed
Hamiltonian time inside the blocks. Every primitive closed orbit is the
single central oval over one constant cover-atom history. The actual
periods satisfy T_p=2 sqrt(2) log p+O(1); their positive repeats and
transverse monodromies are complete. The source and every allowed strip
state remain present. This is an explicit composition theorem, not the
entire energy surface of an older Hamiltonian, a classical manifold,
a global Hamiltonian across reset events, or a natural-A0 theorem.

## 1. Question, identity and precise lineage

The [version-1 card](candidate-card.md) freezes the physical blocks,
all histories, the reference and physical strips, the uniform transport,
and the seam before this proof. The research question is whether these
particular pieces form one complete owner with genuine elapsed timing
and the full intended periodic ledger. They are not conclusions assembled
after examining separate candidates.

The [prior-work lineage](../../docs/prior_work/README.md) realized here is
divisor exclusion -> multiplicative cover atoms -> ordered symbolic
admissibility -> actual sequential physical blocks -> conservative
section geometry. This is a defined deformation/lift of the project's
prime-symbolic source, not a claimed conjugacy to a Logistic or Henon map.
The chronological evolution is fully specified on all bilateral histories;
it is not a schedule fitted to observations or Riemann-zero data.

| Item | This candidate's owner | Limitation |
| --- | --- | --- |
| Source | All ordered rational cover chains Y and their normalized shift F | Chosen admissibility, not a primality-enumeration algorithm |
| Return geometry | M=Y times U*, area dQ wedge dP on each full strip | No transverse derivatives or locally compact transverse assumption |
| Physical dynamics | Every inner-return state of the displayed rational well and hyperbolic plane, cut at its actual section | This building-block contract is not the full 171 energy surface |
| Interface | Full symplectic S_n and S_b S_n^-1 section seam | The original ambient physical coordinates reset at an event |
| Clock and flow | Actual block Hamiltonian time and the complete glued flow | No assigned logarithmic roof or time rescaling |
| Primitive and repeat ledger | Every closed orbit in that complete quotient | No selected centres or periodic subsystem as carrier |
| Analytic consequence | Ordinary unweighted orbit product Z in Section 7 | No trace, operator or Fredholm claim |
| Measure and later geometry | Invariant leafwise section-time volume | No transverse probability, global Hamiltonian, contact or quantum owner |

[163](../163-ordered-cover-scale-suspension/paper.md) supplies the exact
symbolic antecedent but has a different multiplicative-scale clock.
[169](../169-ordered-cover-leafwise-symplectic-lift/paper.md) uses that
scale clock and full planes; its globally hyperbolic-product construction
is not this physical block system. The rational well is an explicit
building-block dependency on
[171](../171-separatrix-witness-hamiltonian-clock/paper.md), not a
transfer of its full energy-space or composite-exclusion theorem.
Here a mixed allowed source history changes wells at its actual section
events. Such trajectories are not trajectories of one fixed component
of 171. These comparisons are not a global novelty claim.

## 2. Entire source and its topology

Let x <=_D z mean z/x is a positive integer. A strict cover x prec z
has no intermediate positive rational in that order. Define

\[
Y=\{y\in(\mathbb Q_{>0})^{\mathbb Z}:y_0=1,
y_j\prec y_{j+1},\ a_j\le a_{j+1}\ \forall j\},\qquad
a_j=y_{j+1}/y_j,\qquad F(y)_j=y_{j+1}/y_1.
\tag{1}
\]

Rational coordinates are discrete; Y has the product-subspace topology.
All negative and positive coordinates are included.

**Source lemma.** Covers have exactly prime ratios. Ratio coordinates
identify Y homeomorphically with all nondecreasing bilateral sequences
of these derived atoms. F is the bilateral left shift, hence a
homeomorphism. Its only periodic histories are the constant atom histories.
Y is totally disconnected and nowhere locally compact.

**Proof.** A divisible integer ratio n is reducible precisely when
n=ab with a,b>=2, which gives the intermediate ax; conversely an
intermediate supplies those two integer factors. Thus the no-intermediate
condition derives primes without a supplied prime table. The inverse
ratio-coordinate map is y_j=product_(0<=i<j) a_i for j>0 and
y_j=(product_(j<=i<0) a_i)^-1 for j<0. Every coordinate in both
directions depends on finitely many discrete coordinates, proving the
homeomorphism. The inverse of F shifts ratios right. A nondecreasing
m-periodic sequence must be constant, since a_j<=...<=a_(j+m)=a_j.

Clopen coordinate sets separate any two histories. A neighborhood of
any history contains a cylinder fixing a finite interval [-N,N]. Keep
the old left history through N and choose a_(N+1) to be any sufficiently
large prime, constant thereafter. These histories lie in that cylinder
and their ratio-coordinate a_(N+1) takes infinitely many discrete values. No
compact neighborhood can contain the cylinder, since a compact set's
image in a discrete coordinate is finite. This proves the topology claim.
The history with ratios 2 for j<0 and 3 for j>=0 is one retained
nonperiodic example. QED.

## 3. One full symplectic transport for every physical section

Let I=QP and define the full open strips

\[
U_* =\{(Q,P):-1<I<1\},\qquad
U_n=\{(Q,P):-n^{-2}<I<1\}\quad(n\ge2).
\tag{2}
\]

These are the entire reference and physical section domains. Neither is
silently called all of R^2; no claim concerns omitted points outside
the frozen strips. All axes, quadrants and noncentral states inside them
are retained. Set eta(t)=exp(-1/t) for t>0 and zero otherwise, and

\[
\chi(t)=\frac{\eta(t)}{\eta(t)+\eta(1-t)},\quad
\delta_n=\frac1{4n^2},\quad \epsilon_n=\frac5{8n^2-3},
\]
\[
g_n(u)=\epsilon_n+(1-\epsilon_n)
\chi\bigl((u+2\delta_n)/\delta_n\bigr),\qquad
f_n(I)=\int_0^I g_n(u)\,du.
\tag{3}
\]

**Proposition 1.** Each f_n is a smooth increasing diffeomorphism
(-1,1) -> (-n^-2,1), equals I on I>=-delta_n, and induces a
global smooth symplectomorphism S_n:U* -> U_n by

\[
Q'=\operatorname{sgn}(Q)\exp\bigl(\log|Q|/f_n'(I)\bigr),
\qquad P'=f_n(I)/Q'\quad(Q\ne0),
\tag{4}
\]

with S_n(0,P)=(0,P).

**Proof.** The denominator defining chi never vanishes. The usual
flat extension of exp(-1/t) has every derivative zero at zero, so chi
is smooth, is zero for t<=0 and one for t>=1. Its exact symmetry
chi(t)+chi(1-t)=1 gives integral_0^1 chi=1/2. Since
0<epsilon_n<1, g_n is positive and at most one. It equals epsilon_n
on u<=-2delta_n and equals one on u>=-delta_n. Thus

\[
\int_{-1}^0g_n(u)du
=\epsilon_n(1-2\delta_n)
+\tfrac{\delta_n}{2}(1+\epsilon_n)+\delta_n
=\epsilon_n(1-3\delta_n/2)+3\delta_n/2=n^{-2}.
\tag{5}
\]

Also f_n(1)=1. Positivity, these endpoint limits and the inverse
function theorem give the claimed diffeomorphism; f_n(I)=I for
I>=-delta_n follows directly by integration.

On each half-plane Q!=0, coordinates s=log|Q| and I=QP have
dQ wedge dP=ds wedge dI. Formula (4) becomes

\[
(s,I)\longmapsto (s/f_n'(I),f_n(I)).
\tag{6}
\]

Its wedge pullback is ds wedge dI. Its inverse is
I=f_n^-1(I'), s=f_n'(I)s'; all quadrants are mapped onto their
counterparts since f_n is increasing and f_n(0)=0. On the open band
abs(I)<delta_n, formula (4) is exactly the identity. Every point of
either axis has a neighborhood in this band. Therefore there is no
axis singularity from log|Q|, and the extensions and inverse are smooth
there. This proves a whole-strip symplectomorphism, not just a quadrant
coordinate calculation. QED.

## 4. Actual physical blocks and the complete seam

For all n>=2 use the single uniform family

\[
c_n=1+n^{-2},\quad W(q)=\frac{4q^2}{(1+q^2)^2},\quad
H_n=\tfrac12p^2+c_nW(q)+QP,
\quad\Omega=dq\wedge dp+dQ\wedge dP.
\tag{7}
\]

With i_X Omega=dH, its equations are
qdot=p, pdot=-c_n W'(q), Qdot=Q, Pdot=-P.
They are complete: abs(W')<=4 bounds scalar acceleration, and
Q(t)=e^t Q(0), P(t)=e^-t P(0) have no finite-time escape.

The declared block is the entire inner return-saturation on H_n=1:
0<E=p^2/2+c_nW(q)<c_n and abs(q)<1, with every compatible
transverse state. It is not an assertion about all of H_n=1. In
particular the outer scattering branches, separatrices, and scalar
equilibrium do not belong to the building-block definition. This scope
was fixed before selecting periodic points. Cut this entire saturation
at q=0,p>0, with entrance

\[
\iota_n(w)=\bigl(0,\sqrt{2(1-QP)},Q,P\bigr),\quad w=(Q,P)\in U_n.
\tag{8}
\]

**Proposition 2.** The first same-oriented physical return on every
point of U_n has time and map

\[
T_n(E)=4\int_0^{A_n(E)}\frac{dq}{\sqrt{2(E-c_nW(q))}},\quad
t_n(w)=T_n(1-QP),
\]
\[
R_n(w)=(e^{t_n(w)}Q,e^{-t_n(w)}P),\qquad
T_n(E)\ge\pi/5>0\quad(0<E<c_n).
\tag{9}
\]

T_n is smooth and R_n is a smooth symplectomorphism of all U_n.
Here A_n(E) is the unique turning point in (0,1).

**Proof.** W increases strictly from 0 to 1 on (0,1), is even,
and has a strict maximum at each of +/-1. For each 0<E<c_n
the inner level is one regular oval, with one positive-momentum crossing
of q=0. Its four quarter-oscillations give exactly the integral in (9);
the simple turning singularity is integrable. Smooth dependence of the
ODE and the transverse next crossing give smooth T_n on the open
energy interval. Conservation E+QP=1 produces precisely U_n.
All points of every inner oval and every compatible transverse state
are reached from (8), with a unique elapsed phase in [0,T_n(E)).

On this nonzero oscillator oval the clockwise angle satisfies

\[
0<\dot\theta=\frac{p^2+c_nqW'(q)}{q^2+p^2}\le10,
\tag{10}
\]

because 0<=c_n qW'(q)<=10q^2 for abs(q)<1. One full oval
turns once, so 2pi<=10T_n(E). The actual transverse solutions
give R_n. This map preserves J=QP and its whole allowed interval;
its inverse has the opposite exponent. In s=log|Q|, J coordinates
it is (s,J)->(s+T_n(1-J),J), preserving ds wedge dJ. Its smooth
formula on the full strip extends the same area identity over the axes.
This proves (9) directly for these blocks; 171's full-energy theorem is
not being presumed. QED.

For y in Y let n=a_0(y), b=a_1(y). Use every segment
Psi_n^u(iota_n(S_n z)), z in U*, 0<=u<=t_n(S_n z).
The two cut faces are distinct labelled faces before gluing, including
when a central closed oval has equal physical endpoint coordinates.
At the outgoing point w_end=R_n S_n z glue by

\[
(y,\iota_n(w_{\rm end}))\longmapsto
\bigl(Fy,\iota_b(S_b S_n^{-1}w_{\rm end})\bigr).
\tag{11}
\]

This maps the whole outgoing U_n onto the whole incoming U_b.
The scalar momentum is reset to sqrt(2(1-Q_new P_new)) as in (8);
it is not incorrectly held fixed while QP changes. The inverse uses
the previous symbol a_-1 and S_n S_b^-1 on these respective sections.
There is no time penalty at a seam. The restricted ambient form on
each section is dQ wedge dP, and (11) preserves it by Proposition 1.

## 5. Full glued owner, inverse, smooth leaves and completeness

Write reference I=QP and define

\[
\tau(y,z)=T_{a_0}(1-f_{a_0}(I)),\qquad
h_n(I)=f_n'(I)T_n(1-f_n(I))>0.
\tag{12}
\]

**Proposition 3.** The actual section return of (11) is the single
leafwise symplectic homeomorphism

\[
B(y,Q,P)=\bigl(Fy,e^{h_{a_0}(I)}Q,e^{-h_{a_0}(I)}P\bigr)
=\bigl(Fy,S_{a_0}^{-1}R_{a_0}S_{a_0}z\bigr).
\tag{13}
\]

Its actual roof is (12), bounded below by pi/5. Its endpoint-glued
suspension is Hausdorff, complete in both time directions, and conjugate
with unchanged time to the entire cut-block composition. It has smooth
three-dimensional leaf charts and invariant leafwise section-time volume.

**Proof.** In (6), the physical return translates s' by
T_n(1-f_n(I)); conjugating back translates s by f_n'(I) times
that actual time. Formula (13) follows away from Q=0 and extends
to both axes by the smooth identities already proved. In particular I
is invariant under B. The inverse uses y^-=F^-1 y and n=a_-1(y),
then multiplies Q by exp(-h_n(I)) and P by exp(h_n(I)). All
integer iterates exist and stay in U*. Since a_0 is a discrete
continuous coordinate, B, its inverse and tau are jointly continuous
and smooth along each entire strip. Each return is symplectic by
conjugation, or by the area calculation for (s,I)->(s+h_n(I),I).

The physical endpoint in (11) is iota_b(S_b z') with
z'=S_n^-1 R_n S_n z. Therefore both the reference return and the
elapsed roof follow from the actual physical segment and its full seam;
no detached clock has been substituted. The unique phase statement
in Proposition 2 identifies every cut-block point with its elapsed
coordinate (y,z,u). Inverse local coordinates are obtained by the
last transverse crossing and the physical flow. Near each cut face
these are physical flow-box coordinates, with the whole-section seam
(11) supplying the transition. Thus the quotient is exactly

\[
\mathcal Q=\{(x,u):x\in M=Y\times U_*,\ 0\le u\le\tau(x)\}
/((x,\tau(x))\sim(Bx,0)).
\tag{14}
\]

For a direct topology and completeness proof, equivalently use M times
R with the full integer deck action generated by

\[
D(x,u)=(Bx,u-\tau(x)),\qquad
D^{-1}(x,u)=(B^{-1}x,u+\tau(B^{-1}x)).
\tag{15}
\]

Each positive iterate decreases u by at least m pi/5; each negative
iterate increases it by at least abs(m) pi/5. Consequently only
finitely many deck translates can connect two bounded time intervals,
uniformly over their base points. The action is free. For two distinct
orbits, first bound their time neighborhoods and then separate the
finitely many possible translates by Hausdorff neighborhoods in M times
R, shrinking those neighborhoods simultaneously. Their saturated images
are disjoint open quotient neighborhoods. Hence the quotient is
Hausdorff without invoking local compactness of Y.

An interval in u of width less than pi/5 has no overlap with its
nonidentity deck translates. Projection restricted to M times this
interval is injective and open onto its image. Together with local
strip charts this gives the stated topological-transverse/smooth-leaf
atlas; transition functions are the smooth finite iterates of (15)
on each leaf. Translation u->u+t commutes with D, so it induces a
jointly continuous complete real flow, smooth in the leaf charts.
The lower bound prevents infinitely many physical seams in finite
positive or negative time, even for histories with unbounded atoms.
The embedded section u=0 has first return precisely tau and B, since
the intervening partial elapsed segment has no further section crossing.

Finally D pulls dQ wedge dP wedge du back to itself: B preserves
section area, while the extra d tau term vanishes against its top-degree
two-dimensional area. The resulting leafwise volume is flow invariant.
No transverse measure is needed for this claim. QED.

The physical ambient coordinates need not have matching derivatives
across (11); smoothness is in the specified flow-box atlas. No global
four-dimensional Hamiltonian extension across these resets has been
constructed. The three-dimensional flow carrier is not symplectic.
It is also not a classical manifold or a locally compact lamination:
its local transverse factor is the actual nowhere locally compact Y.

This construction has a transparent simplification, not an irreducibility
claim: it is the skew suspension (12)--(14) with globally conserved
reference I. The discrete source return F is independent of transverse
state. The elapsed roof depends on I and the current atom, and physical
QP changes at a mixed-symbol seam through f_b composed with f_n^-1.
No theorem of nontrivial cocycle class, impossibility of further coordinate
trivialization, or feedback into the source is asserted.

## 6. Every closed orbit and its actual logarithmic-size clock

**Proposition 4.** The complete Q has exactly one oriented primitive
closed orbit per cover atom, hence per prime p. Its least period is
T_p=T_p(1). Every positive repeat has time r T_p and transverse
Poincare monodromy

\[
DB^r|_{(y^{(p)},0,0)}
=\operatorname{diag}(e^{rT_p},e^{-rT_p}),\qquad
\det(I-DB^r)=2-e^{rT_p}-e^{-rT_p}<0.
\tag{16}
\]

There are no other periodic points, continuous primitive families,
equilibria or unclassified source packets.

**Proof.** Every orbit meets the section in finite future and past time
by its finite segment length and the complete construction. A positive
closed orbit therefore yields B^m(y,z)=(y,z) for some m>=1.
The source lemma forces all ratios of y to be the same atom p.
On such a source fibre, I remains invariant and B^m multiplies Q,P
by exp(+-m h_p(I)), with h_p(I)>0. Thus Q=P=0 is necessary
and sufficient. No centre restriction was imposed to obtain this
conclusion: all states of U* were tested. At the origin S_p is the
identity and f_p(0)=0, so the actual physical segment is the whole
energy-1 inner oval with time T_p(1). Its source point has least
map period one and there is no earlier same-oriented crossing. The
opposite-momentum crossing and other elapsed phases are the same
oriented flow orbit, not new packets. The local flow direction is
nonzero, excluding equilibria. Because dI vanishes at the origin,
differentiating (13) yields (16); its neutral flow direction is not
part of the two-dimensional transverse matrix. QED.

**Proposition 5.** In the frozen physical time units, uniformly for
all integers n>=2 in the building-block formula,

\[
T_n(1)=2\sqrt2\log n+O(1).
\tag{17}
\]

**Proof.** This is the same scalar integral as the explicitly identified
rational-well lemma of 171, but it is already the actual period of the
present closed packet by Proposition 4. We give the calculation to fix
its coefficient and ownership. Put c=1+n^-2,
d=1/sqrt(n^2+1) and v=(1-q^2)/(1+q^2). Since
1-W(q)=v^2 and -dq/dv=(1+v)^(-3/2)(1-v)^(-1/2)=k(v),
the quarter-period substitution gives

\[
T_n(1)=\frac4{\sqrt{2c}}
\int_d^1\frac{k(v)}{\sqrt{v^2-d^2}}\,dv.
\tag{18}
\]

On [0,1/2], k(0)=1 and abs(k(v)-1)<=L v for a fixed L.
The resulting integral error on [d,1/2] is at most L/2.
On [1/2,1), v^2-d^2>=1/20 for all n>=2, and k is
integrable at 1, so that contribution is uniformly bounded. The
remaining integral is arcosh(1/(2d))=log(1/d)+O(1), uniformly
for 0<d<=1/sqrt5. Thus
T_n(1)=(2sqrt(2)/sqrt(c))log(1/d)+O(1).
Use log(1/d)=log n+(1/2)log c and the boundedness of
n^-2 log n to obtain (17). QED.

The logarithm comes from elapsed motion near the rational well's
nondegenerate barriers, with the predeclared gap c_n-1=n^-2.
That gap remains engineering data, applied to every integer by the same
formula. No T_p=log p equality, global time rescaling, per-prime fit,
canonical barrier choice or arithmetic naturalness follows from (17).

## 7. Ordinary product belonging to this full ledger

The sole analytic object frozen for this candidate is

\[
\log Z_{177}(s)=\sum_{p\ \mathrm{prime}}\sum_{r\ge1}
\frac{e^{-srT_p}}r,\qquad
Z_{177}(s)=\prod_p(1-e^{-sT_p})^{-1}.
\tag{19}
\]

Each multiplicity is one; r is actual positive traversal of that same
flow orbit. No transverse stability weight is inserted.

**Corollary 6.** The logarithmic series converges absolutely and
locally uniformly precisely on Re s>1/(2sqrt(2)); it defines a
nonzero holomorphic ordinary product there. Every finite physical-time
window contains finitely many primitive packets and repeats.

**Proof.** With C=2sqrt(2), Proposition 5 gives
abs(T_p-C log p)<=K for a fixed K, and T_p>=pi/5.
For sigma>0 the repeat sum is at most
exp(-sigma T_p)/(1-exp(-sigma pi/5)). If C sigma>1,
comparison with sum_(n>=2) n^(-C sigma) proves convergence,
also uniformly on compact sub-half-planes. If 0<sigma<=1/C,
its r=1 terms dominate a positive constant times sum_p 1/p.
The latter diverges: otherwise the finite Euler products at exponent
one would be bounded using -log(1-1/p)<=2/p, whereas their
positive geometric expansions and unique factorization dominate
sum_(m<=N)1/m when all primes <=N are included. For sigma<=0,
one prime's repeats already fail absolute convergence. Finally
T_p<=R implies p<=exp((R+K)/C), and rT_p<=R implies
r<=5R/pi. QED.

Equality of these period numbers with the zero-witness packets of 171
is proved at the block level; it does not identify the full flows.
Equation (19) is not a Fredholm determinant, a trace formula, a
Riemann-zeta identity or an analytic continuation. No analytic operator
from 174 or any concurrent package is assigned to 177.

## 8. Controls, adverse boundaries and owner-level assessment

| Control / objection | Exact consequence and disposition |
| --- | --- |
| Identity seam between unequal physical strips | For n<b, U_n is larger than U_b: identity is not defined as a map into U_b on all outgoing U_n states, and the inverse cannot cover the larger strip. The frozen S_b S_n^-1 transports the whole domains |
| Remove weak ordering while retaining cover ratios | Alternating 2,3 histories become least-period-two sources; the origin supplies a mixed primitive packet with time T_2+T_3. Ordering is operative design |
| Remove the cover requirement but keep integer divisible ratios | Constant composite ratio 4 becomes a source history with an actual central packet T_4(1). Cover indecomposability is operative |
| Replace transverse hyperbolicity by identity on the same strips | Every z over a constant source becomes a periodic section point; continuous primitive families appear. The central ledger is a full-state consequence of hyperbolicity |
| Keep only Q=P=0 at definition | Would evade whole-strip transport and full-state ownership. The present proofs explicitly retain and test every allowed noncentral state |
| Scalar barrier comparison: replace c_n by a constant | The central E=1 scalar period becomes common for c>1; at c=1 it becomes a separatrix, not a finite closed oval. This is only a scalar-period control: the altered full return strips and seams would need a new contract |
| Arbitrary arithmetic labels or a density-matched alphabet | The assembly would still work if its source and barrier rules were changed. This PROVES_TOO_MUCH risk prevents a claim of canonical arithmetic naturalness |
| Borrow the global 171 energy theorem or the 174 determinant | Neither is an owner theorem for the mixed-history event-glued flow. Such promotion is expressly excluded |
| Finite numerical or truncated history tests | None used. All claims above are exact arguments on entire strips, all integer times and all Y histories |

An explicit clock-substitution control distinguishes tau from h. At
reference I=-1/2, every n>=2 lies on the constant-g_n plateau:
g_n=epsilon_n and f_n(-1/2)=epsilon_n/2-n^-2. Its physical scalar
energy is therefore c_n-epsilon_n/2. Repeating substitution (18) with
d=sqrt(epsilon_n/(2c_n)), which is bounded above and below by positive
constants times 1/n, gives tau_n=2sqrt(2)log n+O(1).
Thus h_n=epsilon_n tau_n=O(log n/n^2). Take an allowed history
constant 2 in the past and passing through the increasing primes in
the future. The actual forward time sum diverges, whereas sum h_n
converges by comparison with sum_(n>=2) log n/n^2. Consequently
replacing tau by the section's logarithmic stretch h would introduce
finite-time seam accumulation on the full carrier. This is a control
against that specific incorrect clock replacement, not a change to the
frozen object or a theorem excluding all coordinate conjugacies.

The arithmetic input is divisibility and cover exclusion, not a supplied
prime table. However its equivalence to primality is explicit, the weak
ordering is selected admissibility, and the rational barrier rule is
selected engineering. Nonuniqueness alone is not a mathematical failure
of this construction; neither is construction success a natural-A0 pass.

| Audit item | Established for ALF-20260915-PSG01 | Boundary |
| --- | --- | --- |
| T0 carrier and ownership | Entire source, global whole-strip transports, physical blocks and seams, complete Hausdorff flow | Topological-transverse/smooth-leaf category only |
| T1 arithmetic and clock | Cover atoms derived internally; the actual central block periods have logarithmic size | Naturalness OPEN; no exact log p or prime-enumeration claim |
| T2 full periodic data | Exactly one primitive circle per prime, positive repeats and complete transverse monodromy | No independent phase packet or noncentral continuum |
| T3 ordinary analytic consequence | Own ordinary product on its exact absolute-convergence half-plane | Operator / trace / Fredholm / continuation NOT SUPPLIED |
| Classical finite-dimensional A0--A2 | NOT APPLICABLE to this carrier type | Not silently fulfilled by the broadened owner-level result |
| Formal Route coordinates | UNASSIGNED | No formal target/divisor protocol was evaluated |
| Route B | NOT INVOKED | No later-route rescue or spectral claim |

## 9. Decision and reproducibility

Decision: advance the explicit composition as a complete engineered
owner with naturalness OPEN. The decisive positive fact is whole-strip
physical compatibility: the same actual blocks and symplectic seams
produce the return map, roof and every periodic packet. There is no
unresolved seam repair or proposed substitution to keep this candidate
alive. Any new barrier, source rule, roof, global Hamiltonian extension
or operator requires its own explicit owner contract before further claims.

The proof inputs and limits are recorded in the
[candidate card](candidate-card.md), [claim ledger](claim-ledger.md)
and [evidence index](evidence/README.md). No numerical dataset, fitted
parameter, finite orbit enumeration, script, external model/API call,
PDF or publication artifact was produced. This is an AI-authored local
research note, with a separate actual model invocation performing
mathematical review; its provenance and limitations are in the evidence
record. It is not human peer review, a human-read attestation, a
submission-readiness certificate or a claim of independent reviewer errors.
