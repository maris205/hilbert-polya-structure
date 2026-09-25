# Integer-part/remainder matrix division: full fixed locus and a noninteger-log primitive

Candidate ID: `ANG-20260920-MRD01`.
Status: `OWNED MATRIX CLOCK; NONINTEGER-LOG FIXED PRIMITIVE — STOP / FORK`.
Date: 2026-09-20. Exact Markdown research record, not a publication.

## Abstract

We audit the partial autonomous map T(M)=R(M)^(-1)A(M)
on ALL signed real 2x2 matrices, where A is the
entrywise floor and R the remainder. Admissibility requires a nonzero
11-pivot dividing the nonzero integer determinant and a nonsingular
remainder. All terminals and boundaries remain. Complete inverse branches
and ordinary four-volume supply a strictly positive inverse-arrow clock.
We resolve the complete fixed-locus equation by an explicit rational
parameterization in the full remainder cube, and classify every fixed
core's complete time group, extension kernel and actual finite-tail packet.
The fixed matrix phi*I, phi=(1+sqrt5)/2, has least
positive time 8 log phi, not the logarithm of any
integer. Three separately owned controls retain the same wrong-time witness
under their OWN IMAGE laws. This decisively stops the prime-time
target without a higher-period census or a formal Route evaluation.

## 1. Frozen owner, question and lineage

The [original card](candidate-card.md), first 186 lines, SHA-256
`e12798b416c0109b50e96f18be02f7c74830e805a6136d5a432072e47bc863ea`,
precedes this audit. The carrier is Y=M_2(R) with ordinary
Borel structure and four-dimensional Lebesgue measure. There are no atoms,
integer-root fibres, similarity identifications, selected centres or added density.
Put entrywise

    A=floor(M), R=M-A in [0,1)^4,
    Aset={A in M_2(Z): A11!=0, det A!=0, A11|det A}.
    T(M)=R^(-1)A when A in Aset and det R!=0.       (1)

Every other state is terminal: T^0 remains, with all actual
incoming histories, but no added forward step or absorbing loop.
Negative floors, all cell faces, pivots +/-1 and unit factors
use the same law. Singular M is NOT excluded by
an extra condition; only A and R determine forward permission.
Matrix order is R^(-1)A, not A R^(-1).

For A_(d,n)=[[d,-n],[1,0]], d,n>=1, its determinant
is n and its 11-entry d; the permission is exactly
d|n. Proper-divisor symbols occur at 1<d<n. The complete
corresponding real cells are retained, alongside ALL other cells. The
arrow is divisor-symbolic admissibility -> integer quotient det A/A11
-> actual integer-dividend/remainder division -> new real floors. It
is not a prime predicate or a selected divisor-labelled orbit.

The question is whether this same owner supplies the required primitive
clock, first at the complete fixed locus. Fixed coordinates,
pivot, floors, matrix order, nonsingular integer dividend and Lebesgue
measure remain DECLARED DESIGN; stronger naturalness is OPEN. No
Logistic/Henon conjugacy or conservative/symplectic lift is claimed. The
[source record](evidence/scout-record.md) preserves bounded input access; old
owners, clocks and conclusions do not supply any proof below.

## 2. Exact inverse/image owner and four-dimensional IMAGE

For EVERY A in Aset define

    U_A={A+R:R in [0,1)^4, det R!=0},
    V_A={X:det X!=0, A X^(-1) in [0,1)^4},
    I_A(X)=A+A X^(-1).                           (2)

For M=A+R in U_A, its image X=R^(-1)A is
nonsingular and A X^(-1)=R. Conversely X in V_A gives
an invertible R=A X^(-1), since both A and X are
invertible. The entries of R put I_A(X) in the
correct half-open floor cell, and (1) maps it back to
X. Thus these are exactly ALL inverse branches with no
missing singular target or selected matrix label. Distinct A give
distinct predecessors because their entrywise floors differ.

The complete image and finite predecessor count admit an explicit
target-wise enumeration. For nonsingular X put

    L_X={a in Z^2: a X^(-1) in [0,1)^2}.
    C_X={A: both rows lie in L_X, A in Aset}.   (3)

Then X has a preimage iff C_X is nonempty; its
predecessors are exactly I_A(X), A in C_X. Each coordinate
of a=rX, r in [0,1)^2, satisfies

    |a_j| <= |X_(1j)|+|X_(2j)|.                  (4)

Hence L_X and C_X are finite, providing a COMPLETE
finite integer-box enumeration for every given finite target, not a
chosen numerical cutoff. Membership uses the exact half-open inequalities;
the loose box bound is only an enumeration envelope. Singular
X has no incoming branch, but stays in Y with
its own unchanged forward permission. Even some nonsingular targets are
missing: X=(1/2)I forces A=0 in (2), which is
inadmissible. The partial map is nononto and finite-to-one.

For an explicit singular source with a legal outgoing step, take
A=[[-1,2],[-1,1]] and R=[[1/2,0],[5/8,1/2]]. Then
det A=1, pivot -1 passes divisibility, det R=1/4,
and floor(A+R)=A, yet det(A+R)=0. Thus "no incoming
branch" really cannot be replaced by "terminal" for singular objects.

It is Borel, not generally continuous even on its actual
domain. For M_t=[[t,1/2],[1/2,3/2]], t<2 sufficiently
close to 2, T(M_t) tends to [[2,-2],[-2,4]].
At t=2 both permission and remainder invertibility still hold,
but T(M_2)=[[-4,2],[4,0]]. No etale or smooth
global source has been inferred from its analytic branches.

For a perturbation H, differentiation of (2) gives

    D I_A(X)[H]=-A X^(-1) H X^(-1).

On the FOUR-dimensional space of 2x2 matrices, left multiplication
by P has determinant (det P)^2 (it acts on two
columns); right multiplication by Q has determinant (det Q)^2
(two rows). Consequently the actual inverse IMAGE is

    J_A(X)=|det A|^2 / |det X|^4,
    mu(I_A E)=integral_E J_A dmu                 (5)

for every Borel E in V_A. This follows from the
analytic bijection on invertible matrices restricted to the actual cell
domain. The frozen version uses the SAME positive finite formula
at all retained null faces and cuts inside V_A. No
value is assigned at a singular target outside that domain;
no terminal is differentiated. A.e. IMAGE alone does not fix
null values, and predecessor counts are not an IMAGE substitute.

At a legal forward state, det T=det A/det R,
so the frozen inverse-arrow clock is

    kappa(M)=-log J_A(T(M))
            =2 log|det A|-4 log|det R| > 0.    (6)

Indeed |det A|>=1, whereas for R=[[a,b],[c,d]] in
[0,1)^4, det R=ad-bc lies strictly between -1 and
1; its nonzero absolute value is strictly below 1.
The sign is proved, not imposed as a positive roof.

For a legal k-step history let K_k(z)=sum_(i<k)kappa(T^i z).
The actual forward Jacobian is exp(K_k(z)). A branch pair
with T^k z=T^l w, directed w->z, has

    J_g=exp(K_l(w)-K_k(z)),
    c(g)=-log J_g=K_k(z)-K_l(w).                 (7)

Two legal presentations of the same retained-lag triple have a
common extension; their shared future increments cancel pointwise. Aligning
middle histories proves composition. Actual finite analytic branch pairs
give IMAGE on their Borel domains with the stated all-point
versions. The partial countable Borel groupoid includes all triples
(z,k-l,w) with legal common futures and T^0 at every
terminal, not arbitrary matrix actions or free branch histories.

Its real extension has all objects (z,h), arrows
(w,h)->(z,h+c), and all translations h->h+t. An
actual forward step z->Tz has lag -1 and time
-kappa(z). This sign does not remove the positive generator
of a two-sided loop time group. Only a Borel/set-level
quotient is claimed, not a smooth suspension or Hausdorff coarse space.

## 3. COMPLETE fixed locus, not only a diagonal slice

A legal fixed point M=A+R must satisfy

    R(A+R)=A, hence (I-R)A=R^2.                  (8)

I-R is necessarily invertible. If a nonzero row v satisfied
v(I-R)=0, then vR=v and multiplying (8) by v
would give 0=vR^2=v, a contradiction. Therefore every fixed
point is supplied by the following explicit rational parameterization:

    R in [0,1)^4, det R!=0, det(I-R)!=0,
    A_R=(I-R)^(-1)R^2 is an INTEGER matrix in Aset,
    F_R=(I-R)^(-1)R.                            (9)

Conversely ANY R passing exactly these tests gives F_R=A_R+R,
so its entrywise floor is A_R and it is a legal
state. Since R commutes with I-R and its inverse,
R F_R=A_R; hence (1) fixes F_R. This proves
necessity and sufficiency on the FULL four-entry remainder cube.
The parameterization eliminates the unknown fixed matrix and resolves its
equation rationally; it is not a restatement of T(M)=M.
Integer membership and the stated pivot divisibility are explicit tests,
not a finite classification of all admissible integer cells. Distinct
accepted R give distinct F_R, by uniqueness of fractional parts.
No positivity, symmetry, diagonalizability or commutation of a general
source point was assumed; commutation here is a CONSEQUENCE of (8).

Put Delta=det(I-R). At a fixed point (9),

    det A_R=(det R)^2/Delta, det F_R=det R/Delta,
    J_(A_R)(F_R)=Delta^2,
    a_R=kappa(F_R)=-2 log|Delta|.                (10)

There are no zero-clock fixed cores. To see this without
restricting to diagonal R, write

    Delta=(1-a)(1-d)-bc, 0<=a,b,c,d<1.

The first term is positive and at most 1; bc<1,
so Delta>-1 and Delta<=1. Equality Delta=1 would force
a=d=0 and bc=0, contradicting det R!=0. Thus
0<|Delta|<1 throughout (9), and a_R is strictly positive.
Every such core has least SOURCE period one, full source
isotropy Z, ENTIRE H=a_R Z and trivial extension kernel.

## 4. Full finite-tail packets and the decisive exact witness

For EACH accepted fixed core F define its complete basin

    B_F=union_(d>=0){z:T^d z=F with every step legal}. (11)

The inverse list (2)–(4) enumerates all finite predecessors at
each depth, with no depth cutoff; the basin is at
most countable. Repeated presentations of one state do not add
new source objects. No terminal can make a positive forward
step into F, and no incoming branch can be deleted.

For z in B_F let d(z) be its least entry
depth and S(z)=K_(d(z))(z). All integer lags between
z,w in B_F occur by extending their paths along the
fixed core. Writing a=kappa(F)>0, equation (7) gives

    c(z,ell,w)=S(z)-S(w)+(ell-d(z)+d(w))*a.     (12)

Thus source isotropy is Z at every basin point, the
FULL time image is aZ, and the extension kernel is
zero. The complete extension-object invariant is

    h-S(z) modulo a.                            (13)

Equality of (13) is equivalent to an actual arrow because
every integer lag is available. Translation on R/aZ is transitive
with least positive time a. The entire basin contributes ONE
primitive packet and repeats ra, r=1,2,..., not one
packet per inverse word, predecessor or phase. Two different fixed
cores cannot have a common future; their packets do not
merge even if their matrices, determinants or times have related
values. This is a complete FIXED-packet account. Source isotropy
at higher periodic cores elsewhere remains UNCLASSIFIED; none can shorten
or merge one of these already determined full-tail packets.

An exact witness is obtained WITHOUT inserting a logarithm:

    phi=(1+sqrt5)/2, r=1/phi=phi-1,
    r^2+r=1, A=I, R=rI, F=phi I.              (14)

Here 0<r<1, the floor is I, and the unit pivot
passes the original permission 1|1. Both matrices are invertible,
so F is an actual full-source fixed point. Equation (5)
or (10), independently evaluated at this point, gives

    J_I(F)=phi^(-8), H_F=(8 log phi) Z,
    least positive primitive time L=8 log phi.    (15)

The number exp L=phi^8=(47+21 sqrt5)/2 is irrational,
so L is not log N for ANY integer N, let
alone log p for a prime. This is an exact
algebraic obstruction, not a decimal fit. Its least SOURCE period
is one but its positive time is (15); those are
different notions. A prime packet elsewhere cannot turn F into
its repeat, by the complete H and actual-tail separation above.

The witness is not retained by selecting a diagonal subsystem.
Its direct predecessors are exactly phi A for the four matrices

    [[1,0],[0,1]], [[1,0],[1,1]],
    [[1,1],[0,1]], [[1,1],[1,0]].                (16)

Indeed at X=phi I, condition (2) forces every entry
of A to be 0 or 1; A11=1 and det
A!=0 leave precisely (16), all satisfying divisibility. The
full deeper basin is still (11), not just these four
points. All other real source states and terminals also remain.
The wrong-time primitive is therefore decisive: STOP / FORK.

## 5. Separately owned gate controls

SCHUR-OFF uses the same transport but admissible list

    Aset_off={A integer:A11!=0,det A!=0}.

SCHUR-SHIFT instead uses

    Aset_shift={A integer:A11!=0,det A!=0,A11|(det A+1)}.

For EACH list the inverse identities (2) follow anew by
solving R X=A, and (3) uses that list to
give its OWN exact finite image/predecessor enumeration. Formula (5)
is its actual four-dimensional IMAGE and (6) its positive
clock; no equality of source domains is asserted. All rejected
states remain terminal under that control's own permission.

Its complete fixed locus is (9) with A_R tested against
that control's list, proved from its OWN equation (8).
The bound 0<|Delta|<1 and formula (10) classify ALL
its fixed source/time/kernel groups. Its own inverse basins and
prefix sums give (11)–(13), not imported main basins.
Both lists admit I, so each OWN fixed packet at
phi I has primitive 8 log phi. This conclusion does
not depend on borrowing an orbit from the main or deleting
the unit cell. The gate modifications do not remove the
wrong-time witness. Higher control periods are UNCLASSIFIED.

## 6. INTEGER-DIVIDEND-OFF — different image and infinite predecessors

This control retains ALL main permission but acts by T_0(M)=R^(-1).
Its complete inverse branches are

    I^0_A(X)=A+X^(-1), A in Aset,
    V_0={X:det X!=0, X^(-1) in [0,1)^4}.      (17)

Necessity and sufficiency follow directly from R=X^(-1); its
invertibility and floor-cell membership give the legal predecessor A+R.
The image is EXACTLY V_0, and EVERY image target has
countably infinitely many predecessors, one for every A in Aset.
The list is infinite, for example A=diag(n,1), n>=1,
and distinct A have distinct floors. The main finite-to-one
image and AX^(-1) test cannot be transferred to this control.

Differentiating THIS inverse gives H->-X^(-1)H X^(-1), so

    J^0_A(X)=|det X|^(-4),
    kappa_0(M)=-4 log|det R| >0.                (18)

The same all-Borel analytic substitution and explicit null-face version
apply on V_0, not outside it. Its OWN actual
finite-branch pairs supply its groupoid/cocycle. Countably infinite branching
does not justify truncation or assigning equal labels to predecessors.

Its COMPLETE fixed-locus equation resolves differently:

    R in [0,1)^4, det R!=0,
    A_R^0=R^(-1)-R is an integer matrix in Aset,
    F_R^0=R^(-1).                               (19)

Necessity follows from A+R=R^(-1); conversely the displayed
integer/floor test makes that equation an actual legal fixed point.
The parameterization covers the full remainder cube, including all negative
integer dividends it permits. ALL these cores have source Z,
H=(-4 log|det R|)Z with positive generator and extension
kernel zero. Every actual finite predecessor is retained by its
own analogue of (11); the source/phase proof (12)–(13)
uses its OWN increments and cores. It gives one packet
per fixed core, without claiming to classify other cycles.

At R=rI from (14), R^(-1)-R=I, so this owner
also has F=phi I, now by (19), with its OWN
J^0(F)=phi^(-8) and primitive 8 log phi. Its immediate
predecessors are ALL A+rI, A in Aset, not the
four main predecessors in (16). The equal witness clock is
independently derived; the full orbit owners are different. This control
also fails the prime-time fixed gate. Higher periods UNCLASSIFIED.

## 7. Gate synthesis, adverse limits and decision

The four-dimensional carrier, transport, every arithmetic permission, inverse
branch, IMAGE and retained-lag packet convention belong to the same
frozen main owner. T0 and the owned part of T1
are established; the arithmetic clock is a real determinant calculation,
not an inserted log-prime roof. Stronger naturalness remains OPEN.

The COMPLETE fixed-locus and fixed-packet classification (9)–(13) is
established, including all zero-time tests and finite predecessors. This
is not a classification of all higher returns, which remain
UNCLASSIFIED. Nevertheless the exact positive primitive (15) decides the
T2 prime-time target negatively. Keeping the unit cell and full
packet prevents a selected-subsystem or repetition-label rescue. Three controls
show that merely shifting/removing this divisibility filter, or removing
the integer dividend from transport, does not remove their OWN
wrong-time fixed witnesses. No universal matrix-dynamics impossibility is claimed.

The witnesses lie on null off-diagonal cell faces. Their IMAGE
clock uses the frozen analytic full-point version, not uniqueness from
a.e. measure data. These pointwise conventions are part of the
owner, not evidence that its time is uniquely forced by arithmetic.
No singular target is assigned a clock or terminal given a loop.
The quotient circle is an abstract phase model, not an embedded
periodic curve or a proved Hausdorff coarse topology.

Portfolio: STOP positive-prime-time promotion; retain the exact owner and
fixed-packet negative; FORK to a separately defined/frozen architecture.
T3 NOT SUPPLIED / NOT PURSUED. Classical symplectic base,
positive-roof mapping torus and A0/A1/A2 NOT APPLICABLE;
formal coordinates UNASSIGNED; Route B NOT INVOKED. No borrowed
operator, trace, determinant/zeta identity or RH statement follows.

The [claim ledger](claim-ledger.md), [evidence](evidence/README.md) and
[internal review](evidence/independent-review.md) record bounded verification and
all three ARS checkpoints. Review is inherited-model/shared-history internal
AI scrutiny, NOT_CALIBRATED, not external peer review or formal
proof. No scientific numerics, prime tables, precision cutoff or
external literature campaign was used. Positive 304 and older packages
remain unchanged; 241/242 paused; programme goal active. Markdown
only; no publication, upload, PDF/LaTeX or Git commit.
