# DVC01 — frozen-card independent derivation

Candidate `ANG-20260925-DVC01`; paper 467; date 2026-09-25.
Batch `ADMISSION-CORE-20260925-X`, round 3/5; no paper 470.
Reviewer `/root/algebraic_henon_author`; same-model/shared-history
`NOT_CALIBRATED`, not blind, external, human or cross-model verification.

## 0. Inputs, release and scope

Sole candidate scientific input: candidate-card.md, full original lines
1–115 through explicit EOF, re-read after DISTINCT RAW RELEASE; SHA256
`ed66e9258ce953584e9bd57c2dac7ea00bac740d8133ebcf3be579f60a89a658`.
The card was unchanged from CP1. Root reported its FULL read of the
125-line scope-review.md before this separate mathematical release.
The scope receipt is
`ebb7e056c09ad31be4a6058aff0960ee3fa03030b361f05e76091025ff6f0a8f`.
ARS router/workflow/runtime/DA/fallacies/anti-leakage and local AGENTS/plan
were personally refreshed at CP1; exact ranges are recorded there.
Those are retained instructions, not independent mathematical evidence.
No current author manuscript/README/ledger, helper/peer answer, old proof
or old outcome file was read. Embedded card provenance and inherited
participation remain exposed; no sealed-prediction claim is made.
No scientific code, numerical census, network, Git, PDF or helper was used.
Only this raw file is written. It is frozen after complete self-read and
receipt; no author comparison occurs before a distinct PAPER UNLOCK.

All calculations below concern the original X=R3×R3 and Lebesgue6.
M denotes MAIN, G permission-OFF, C cross-product-OFF, and D drift-OFF.
Write z=(u,v), a=e3, b=e1, m=floor(u1), n=floor(u2).
Arithmetic permission means m!=0 and n/m is an integer, with actual
q=n/m. G instead uses q=floor(n/m) if m!=0, otherwise q=0.
Fixed-label differentiation never differentiates the floor function.

## 1. Full six-dimensional derivative and the actual domains

For s in R3, let K_s w=s×w. In the original ordered (u,v) coordinates,
the derivative of M/G/D's fixed-label map is

    [ I          I   ]
    [ qI-K_v     K_u ].

Eliminating its lower-left block gives

    Delta_q(z)=det(K_(u+v)-qI)=-q(q^2+|u+v|^2).              (1)

Here K_s s=0 and K_s^2=ss^t-|s|^2 I. For s!=0, its action on s-perp
in an oriented orthonormal basis is a two-dimensional skew block of
square -|s|^2 I; hence det(qI-K_s)=q(q^2+|s|^2).
For s=0 the same identity follows from qI. This establishes (1) for
all real q and ALL six coordinates, including collinear/null states.
The sign comes from det(K_s-qI) in dimension three; it is not dropped
until forming the absolute measure modulus.

C has derivative blocks [I,I; qI,0], so independently

    Delta_q^C=-q^3.                                         (2)

Thus EVERY owner's own full derivative guard is exactly q!=0, although
their maps, derivative values and clocks are not identical. In particular
C obtains this guard from (2), not by inheriting a removed cross term.

For M/C/D, define E_(U,q)={z: m!=0, n=qm}, q in Z\{0}.
For G, define E_(G,q)={z: q_G(z)=q}, q in Z\{0}.
These are disjoint Borel sets; their unions are the respective legal
domains. All excluded objects remain in X as terminals, including q=0
and failed arithmetic states. No outgoing terminal step is manufactured.
This does not remove their possible incoming arrows.

At the frozen seed u=(d,N,0), v=e3, an admitted MAIN quotient is q=N/d>1.
Formula (1) is -q(q^2+d^2+N^2+1), hence nonzero. Thus full MAIN admission
there is exactly d|N, not merely an unverified arithmetic subtest.
C has nonzero (2) on admitted seeds, and D has nonzero (1).
G's quotient floor(N/d)>=1 gives a legal geometric source even without
divisibility. This is an own-rule comparison, not MAIN arithmetic credit.

The output's second active vector affects the next first vector and
therefore subsequent integer readouts. This is the specified exact
divisor-symbolic deformation; it proves no strong-naturalness theorem.

## 2. All real inverse solutions, including zero-label degeneracies

For q!=0 define the globally analytic map

    R_q(s,t)=[q t+s×t+s(s·t)/q]/(q^2+|s|^2).                (3)

Indeed (qI-K_s)(qI+K_s+ss^t/q)=(q^2+|s|^2)I, so R_q is the
unique solution u of u×s+q u=t. The denominator is everywhere positive;
no direction, eigenline or root selection has been made.

The complete nonzero-label inverse maps at target w=(x,y) are

    theta_(M/G,q)(w)=(R_q(x+a,y-b), x+a-R_q(x+a,y-b));
    theta_(C,q)(w)=((y-b)/q, x+a-(y-b)/q);
    theta_(D,q)(w)=(R_q(x,y), x-R_q(x,y)).                 (4)

Substitution into the first component gives the required sum. In the
cross cases, u×v=u×(s-u)=u×s, so (3) gives the second component.
Conversely any preimage has that sum and must solve the same linear
equation, proving that (4) exhausts every nonzero-label real solution.

Zero labels are handled BEFORE excluding them by the own regularity guard.
For the equation u×s=t at q=0:

- If s=0 and t=0, every u in R3 is a solution.
- If s=0 and t!=0, there is no solution.
- If s!=0, existence is equivalent to s·t=0; all solutions are
  u=(s×t)/|s|^2+alpha s, alpha in R.

Necessity follows by dotting with s. The displayed solution follows from
the vector triple-product identity, and the difference of two solutions
is parallel to s. This covers all M/G and D zero-label possibilities
with their respective (s,t) substitutions. For C at q=0, t=y-b must
vanish, in which case every u is a solution; otherwise there is none.
In every zero-label case, (1) or (2) vanishes. Consequently none is an
actual legal incoming source, but all such points remain physical objects.

The actual predecessor relation for EVERY target w in X is therefore

    Pre_U(w)={theta_(U,q)(w): q in Z\{0},
                             theta_(U,q)(w) in E_(U,q)}.   (5)

Membership uses exact original floors, the owner's quotient/permission,
and its proven guard. Each candidate already has exact forward equality
by (4). No outgoing permission on w is tested. Actual labels are unique,
so two different retained labels cannot describe the same legal source.
All integer labels are retained; (5) has no finite cutoff.

## 3. Complete atlas, every-point IMAGE and each owner's clock

For each fixed q!=0, (4) is a global analytic inverse to its fixed-label
map on R6. Thus the maps are global analytic diffeomorphisms on ambient
R6, even though the actual dynamics use only their Borel source pieces.
The restrictions theta_(U,q):B_(U,q)->E_(U,q), where
B_(U,q)=F_(U,q)(E_(U,q)), give complete disjoint SOURCE charts.
B_(U,q) is Borel because it is the image of a Borel set under an ambient
homeomorphism. Target domains may overlap, recording distinct incoming
sources; they are not incorrectly disjointized by deleting sources.

This is the card's permitted explicit atlas. It is equivalent to the
rational-ball prescription: each regular fixed-label germ is the same
global diffeomorphism; rational balls cover its domain, and first-index
subtraction only assigns one chart, never changes the actual germ.

At EVERY target in an assigned inverse domain, set

    J_(M/G,q)(x,y)=1/[|q|(q^2+|x+a|^2)],
    J_(C,q)(x,y)=|q|^(-3),
    J_(D,q)(x,y)=1/[|q|(q^2+|x|^2)].                       (6)

These are positive, finite full-six-dimensional inverse determinants
from (1)–(4). They also prescribe actual null-floor-face values through
the ambient analytic germ. A point with a fixed actual label has the
same value in every permitted refinement; no arbitrary a.e. modification
or new measure is introduced. For any Borel A subset B_(U,q), ordinary
analytic change of variables on the ambient diffeomorphism yields

    mu(theta_(U,q)(A))=integral_A J_(U,q)(w) dmu(w).         (7)

Restriction to actual Borel pieces preserves (7), including null pieces;
extended integrals are permitted. Countable completeness gives a
nonsingular measured-history owner, not measure invariance or symplecticity.

At every legal source the OWN clock is

    kappa_M/G/D(u,v)=log[|q|(q^2+|u+v|^2)],
    kappa_C(u,v)=3 log|q|.                                (8)

This is exactly -log J_actual(Tz). Since q is a nonzero integer, these
clocks are nonnegative. Cross-owner zero clock is possible only when
|q|=1 and u+v=0; C has zero clock whenever |q|=1. Strict positivity is
not imposed by definition, and no terminal receives a step clock.

## 4. Every incoming history and full history-pair IMAGE

For each U separately, let D_r be its r-legal-step domain, D_0=X,
T^0 the identity, S_0=0, and

    S_r(z)=sum_(j=0)^(r-1) kappa_U(T^j z),  M_r(z)=exp S_r(z).

For M/G/D this is the product of |q_j|(q_j^2+|u_j+v_j|^2);
for C it is the product of |q_j|^3. Empty products equal one.
Every legal finite label word defines a Borel source piece on which
T^r is the restriction of a composition of global diffeomorphisms.
All words form a countable complete source partition for D_r, with
Borel images and all-point absolute determinant M_r(z).

For arbitrary w define P_U^0(w)={w} and recursively

    P_U^(j+1)(w)=union_(t in P_U^j(w)) Pre_U(t).            (9)

Induction using (5) proves P_U^j(w)={z in D_j:T^j z=w} for EVERY j.
No target-domain guard, prescribed eigenline, finite label truncation or
window condition occurs. All compatible infinite incoming histories are
the sequences w_0=w, w_(j+1) in Pre_U(w_j) for every j>=0.
They are retained as histories of existing objects, not added physical
completion points. Formulae (3)–(5),(9) are an unrestricted explicit
inverse recursion for the entire original X, including terminal targets.

Let G_U contain all actual (z,r-s,w) with z in D_r, w in D_s and
T^r z=T^s w. Equal triples, not equal endpoints alone, are identified.
The source is w and range z. This is a countable Borel groupoid: each
pair of finite branch words supplies a Borel partial-bijection graph,
and a countable union covers every triple while retaining its lag.

Define c(z,r-s,w)=S_r(z)-S_s(w). For two witnesses of the same lag,
r'-r=s'-s. If this common difference is nonnegative, both sums append
exactly the same legal orbit segment after their common endpoint.
It cancels. The opposite difference is treated by interchanging witnesses.
Hence c descends to actual triples, including those with terminal ends.

For composable witnesses (z,r-s,w) and (w,p-t,v), take ell=max(s,p).
The composite has witness (r+ell-s,t+ell-p). Each extension is legal
because its continuation is an already existing segment of w's orbit.
The common intermediate sums cancel, proving cocycle additivity.
Units have c=0, inverses reverse c, and (Tz,-1,z) has c=-kappa_U(z).

On actual word pieces the arrow map w->z is
(T^r|_alpha)^(-1) composed with (T^s|_beta). Its absolute full6D Jacobian
is M_s(w)/M_r(z)=exp[-c(z,r-s,w)]. Change of variables proves its
every-Borel IMAGE formula. Different witnesses agree by descent;
every-point branch values, including all assigned cuts, are preserved.

## 5. Full kernels, isotropy and physical phase test

All three global kernels, for each owner, are exactly

    K_lag={(z,0,w): some r has T^r z=T^r w legally};
    K_clock={(z,r-s,w) in G_U: M_r(z)=M_s(w)};
    K_joint=K_lag intersect K_clock.                      (10)

These are complete actual equal-lag/equal-product tests. They are not
restricted to units; a zero-lag arrow need not have zero clock.
In particular C's clock uses its own products of |q|^3, not automatically
zero on its whole groupoid merely because some labels have zero clock.

Nonzero source isotropy is equivalent to eventual legal periodicity.
Indeed r>s and T^r z=T^s z force a repeat of an already legal segment;
that segment can be iterated forever. Conversely an eventual cycle gives
such witnesses. If its least period is p, every repeat difference is a
multiple of p: division by p leaves a smaller return if the remainder
were nonzero. Every integer multiple is realized by sufficiently late
witnesses. Thus source isotropy is pZ, not merely a subgroup containing it.

Let C_z be the sum of the OWN clock once around that least cycle.
The transient sums cancel in loop witnesses, so c(z,kp,z)=k C_z and

    ENTIRE H_z=c(G_z^z)=C_z Z.                            (11)

If z is not eventually periodic, source isotropy and H_z are both {0}.
The complete X×R extension has arrows (w,h)->(z,h+c).
Its isotropy is {k in source isotropy:c(z,k,z)=0}: it is all pZ when
C_z=0, and {0} when C_z!=0. Zero-clock isotropy is never removed.

Two extended points (w,h_w),(z,h_z) are equivalent exactly when some
legal r,s have T^r z=T^s w and h_z-h_w=S_r(z)-S_s(w).
This exact test covers every pair without presuming a quotient topology.
Within a source orbit choose any reference z_0 and any actual arrow
g:z->z_0. The complete phase is h+c(g) modulo H_(z_0). Different choices
differ by full isotropy; conversely a congruence is realized by composing
with an actual isotropy arrow. Thus the phase test is sufficient as well
as necessary, without a global selector or a regular coarse quotient.

Height translation is well-defined on the orbit SET because it commutes
with every extension arrow. Its stabilizer on the orbit represented by
z is exactly H_z. If C_z!=0, its primitive is |C_z| and its positive
repetitions are j|C_z|, j>=1; all signed integer repeats are retained.
If H_z={0}, there is no positive closed height packet, even when the
source has nontrivial zero-clock isotropy. Distinct source orbits are
not merged merely because their periods agree.

For completeness, if e is terminal, its source orbit is precisely
union_j P_U^j(e). Each z there has a unique depth d(z) to e, since e
cannot be legally advanced. Put sigma(z)=S_(d(z))(z). The only arrow
between z,w has lag d(z)-d(w) and clock sigma(z)-sigma(w): any common
endpoint can be advanced to e, and conversely those terminal arrivals
provide a witness. The lag, clock and joint kernels mean respectively
equal depths, equal sigmas, and both. All isotropy is trivial; the full
phase is h-sigma(z) in R, with no positive return and no absorbing loop.
For non-eventual infinite histories, (9)–(11) and the common-future
phase test remain exact; no empty or periodic completion is appended.

## 6. Exhaustive fixed states in the frozen W

In W, both readout floors are -1. Thus all four owners have their actual
q=1 and arithmetic permission there. Equations (1)–(2) show nonzero
own guards throughout W, without restricting the other coordinates.

For M/G, the first fixed equation forces v=a. The second becomes

    u×a+u+b=a.

Writing u=(x,y,z), u×a=(y,-x,0), so

    x+y=-1,  y-x=0,  z=1.

These full coordinate equations have the unique solution

    u_*=(-1/2,-1/2,1), v_*=a; denote P=(u_*,a).           (12)

It lies in W, including all actual half-open/closed tests, and has
floors -1,-1 and actual q=1 for BOTH owners. Its sum has squared norm
|u_*+a|^2=9/2; therefore Delta_1(P)=-11/2 is the original full6D
determinant. These calculations check the own legal guard and forward
equations, not a scalar or planar reduced owner.

For C, the first fixed equation again forces v=a. The second forces
u=a-b=(-1,0,1). Its second coordinate is the EXCLUDED upper readout
boundary 0, so it is not in W. There is no other formal solution.
For D, the first fixed equation forces v=0, and the second forces u=0.
This fails both readout bounds of W. Hence, exhaustively,

    Fix_W(M)=Fix_W(G)={P};  Fix_W(C)=Fix_W(D)=empty.        (13)

No unrestricted fixed-state or higher-period classification is inferred.
In particular the empty C/D windows do not imply empty global ledgers.

## 7. FULL incoming and complete packet for each discovered core

For U=M and separately U=G, use its OWN predecessor tests in (5) to set

    B_U=union_(j>=0) P_U^j(P).                            (14)

Equations (3)–(5),(9) explicitly determine EVERY branch at every depth
over full X; they do not confine u,v to W. Induction already proves that
(14) is precisely every source eventually hitting P. It is also exactly
P's full groupoid source orbit: an arrow to P equates an iterate of the
source to an iterate of the fixed P, hence to P itself. Conversely each
finite hitting history gives that arrow. No claim B_M=B_G is needed or
made; identical fixed maps at P do not equate their global source tests.

Put K=log(11/2)>0. This is the OWN value from (6),(8) at P for each
of these owners. For z in B_U define the least hitting depth ell(z),
sigma(z)=S_(ell(z))(z), and E(z)=sigma(z)-ell(z)K.
These are exact actual-history quantities; sigma includes every incoming
step and is not artificially replaced by ell K.

For any z,w in B_U and every integer k, choose a,b>=0 with
k=ell(z)-ell(w)+a-b. The witnesses r=ell(z)+a, s=ell(w)+b meet at P,
and their clock is E(z)-E(w)+kK. Any other witness can be extended to P
and gives the same value. Therefore the ENTIRE basin restriction is

    G_U|B_U={(z,k,w):z,w in B_U, k in Z},
    c(z,k,w)=E(z)-E(w)+kK.                               (15)

This retains every incoming branch and lag rather than listing only
the fixed-point loop. Its complete three kernels are

    K_lag|B_U={(z,0,w):z,w in B_U};
    K_clock|B_U={(z,k,w):E(z)-E(w)+kK=0};
    K_joint|B_U={(z,0,w):E(z)=E(w)}.                      (16)

At every z in B_U, source isotropy is all Z and c(z,k,z)=kK.
Thus ENTIRE H_z=K Z and extension isotropy is trivial. There is no
smaller generator hidden in the incoming tree or a different phase.
The actual forward hitting arrow (P,-ell(z),z) has clock -sigma(z),
so the complete physical phase is

    h-sigma(z) modulo K Z = h-E(z) modulo K Z.             (17)

Equation (15) proves that this phase equality is exactly extension-orbit
equality on the basin, in both directions. All real h are retained.
Height translation gives one whole circle R/(K Z) and exactly ONE
closed packet over this source orbit, with primitive K and repetitions
jK. Incoming leaves and distinct phase representatives do not add
packets or justify dividing K. Each owner has this conclusion separately.
C and D have no W core, but their full-X inverse/history/kernel/phase
contracts remain those proved in Sections 1–5, not empty-owner claims.

## 8. Decisive necessary-target result and limitations

For MAIN the primitive in Section 7 has exponential 11/2, which is >1
and is not an integer, hence not an ordinary prime. Injectivity of the
real logarithm proves that K is not log p for ANY ordinary prime.
This is an owned positive primitive using the full6D measure, whole H,
full incoming source orbit and all phases/repetitions. It is not merely
a local Jacobian value, an eigenline time or a selected subpacket.

Therefore MAIN's universal ordinary-prime-only purity is REFUTED and the
frozen necessary target fails: **STOP / FORK**. Its positive ledger is
nonempty. Global coverage, global multiplicity, untested fixed states and
higher cycles are not classified and remain OPEN, without continuation
on this candidate. The adverse witness needs no additional census.

G reproduces this fixed packet under its own rules: a PROVES_TOO_MUCH
warning, not a proof of global equivalence. C and D's empty fixed windows
neither rescue MAIN nor refute all of their possible positive packets.
Strong naturalness remains OPEN. No repaired constants, roof, density,
parameter, source restriction or new window is proposed.

The same-object ledger is intact for each measured-history owner.
Classical symplectic/suspension fields are NOT APPLICABLE; arithmetic T1
is NOT PASSED; T3 NOT AUDITED; formal coordinates UNASSIGNED;
Route B NOT INVOKED. No trace, operator, zeta or novelty claim is made.
AI supplied this independent raw mathematical derivation and checking;
ARS supplies staging discipline, not calibration or correctness credit.
After full self-read and hash freeze, HOLD for root's full raw read and
DISTINCT PAPER UNLOCK. No author material was used to construct this raw.
