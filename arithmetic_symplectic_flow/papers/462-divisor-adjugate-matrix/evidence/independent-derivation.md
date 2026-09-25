# DAM01 — card-only independent raw derivation

Date: 2026-09-24. Candidate: `ANG-20260924-DAM01`.
Batch: `RECURRENCE-ADMISSION-20260924-W`, round 3/5, exactly 460–464.
Reviewer: `/root/algebraic_henon_author`, separate from author/helper.
Internal same-model/shared-history AI work: **NOT_CALIBRATED**.

## 1. Release, exact inputs and conclusion

Root separately released mathematics after reporting its full 118-line CP1
read. I then reread the original scientific card prefix, lines 1–100 through
its explicit EOF, and remeasured that exact prefix using head/sha256sum.
candidate-card.md original prefix — 100 lines — SHA256 b4e6f17686ee716eb16b218515f5d0ef10343410dee41fa089dc95ba7fbe9331.
scope-review.md — 118 lines — SHA256 b097eaabef5a831675d31049a82722a4f49f3b14c95816ac950ee51d172d0a63.
Only this frozen card supplied current science. No author paper, README,
ledger, outcome append, helper/peer output, sibling paper or old proof was
read. The personally refreshed ARS instructions and retained local guidance
are documented exactly in CP1. Historical/shared exposure remains disclosed;
this is neither blind prediction nor external/human/cross-model validation.

The full determinant of each adjugate branch is 2(det A)^3; L separately
has determinant 1. The complete fixed sets in W are MAIN/G each {phi I},
L empty, and Q {I}, where phi=(1+sqrt(5))/2. Entire incoming basins of the
tested cores are respectively {phi I,-phi I} and {I,-I}, not selected centers.
MAIN/G's positive primitive is log(76+34sqrt(5)); its exponential is
irrational, not an ordinary integer or prime.
Q independently has one tested prime-2 packet. MAIN stops on its own result.

## 2. Full nine-dimensional derivative and own domains

Throughout, I=I_3, X=M_3(R), mu is original Lebesgue9, and D=det A.
Laplace expansion gives A adj(A)=adj(A)A=D I. For invertible A this is
adj(A)=D A^{-1}. Expanding det(I+tX)=1+t tr X+O(t²) and
(I+tX)^{-1}=I-tX+O(t²) gives the full Fréchet derivative

    D adj_A[H] = D[tr(A^{-1}H) A^{-1}-A^{-1}H A^{-1}].   (1)

This differentiates the full cofactor polynomial, not a diagonal restriction.
Put X_0=A^{-1}H. Formula (1) factors into

    H -> X_0 -> tr(X_0)I-X_0 -> D(tr(X_0)I-X_0)A^{-1}.

The first map has determinant D^{-3}: left multiplication acts on each of
three columns. The middle map is multiplication by 2 on the scalar line
and by -1 on the eight-dimensional traceless space, so its determinant
is 2. The last scalar/right-multiplication map has determinant D^9 D^{-3}.
Therefore, in all nine original coordinates,

    det_R9 D adj_A = 2D³.                              (2)

Both sides of (2) are polynomials in the entries of A. They agree on the
dense open invertible matrices, so (2) also holds at every singular matrix.
Translation by -qI does not affect the fixed-label derivative. MAIN/G/Q
thus have own regularity exactly D!=0; their singular objects are retained
terminals, not deleted from X. L's fixed-label derivative is the identity
on all M_3(R), with determinant 1, including singular and zero-q sources.

For cells C_mn={floor A11=m, floor A22=n}, MAIN's legal q source is
the union of C_m,qm over integers m!=0, intersected with {D!=0}.
G takes all C_mn with m!=0, floor(n/m)=q, and for q=0 also the m=0
cells, again intersected with {D!=0}. Q uses MAIN's arithmetic union and
{D!=0}, but just its one adjugate map. L uses the arithmetic union alone.
These are Borel sets. Actual quotients for M/G/L are unique wherever used;
Q's unused quotient does not multiply its map or roots. All excluded objects
still have their units and every actual incoming arrow, without an outgoing
step, absorbing loop or next-step clock. No target permission is imposed.

For the integer seed diag(d,N,1), det A=dN!=0, so the full adjugate guard
is nonzero. L's own guard is also nonzero. Thus MAIN and Q have exactly
the stated d|N admission at proper-divisor seeds, and L retains it as well;
G removes that arithmetic condition. No prime list or target clock was used.
This verifies the concrete interface, not strong naturalness of the design.

## 3. Exhaustive inverse sheets, including own L and Q

Consider adj(A)=Y on the legal adjugate source. Invertibility of A implies

    det Y=D²>0,        A=D Y^{-1}.

Conversely, if det Y>0, for either epsilon=+1 or -1 put

    D_epsilon=epsilon sqrt(det Y),
    A_epsilon(Y)=epsilon sqrt(det Y) Y^{-1}.           (3)

Its determinant is D_epsilon³/det Y=D_epsilon, so its adjugate is exactly
Y. Thus (3) is all and only the legal full-matrix inverse candidates, one
of each determinant sign. If det Y<=0 there is no regular-source inverse.
For det Y=0 this does not deny singular algebraic roots; (2) proves why
every such source is rejected by the relevant own guard.

For M/G enumerate every integer q, set Y=B+qI, use both branches (3) when
det Y>0, and retain the exact actual floor/quotient/permission and forward
checks. Every actual predecessor supplies its own q and its own determinant
sign, proving completeness. No finite q cutoff, chosen sign, eigenbasis,
or target-next-step requirement is permitted. Q uses Y=B just once, with
its own arithmetic guard. In particular a Q singular target has no actual
incoming step, while such a target for M/G must still be tested at every q.

L independently has candidates A=B+qI for every integer q, with its own
source checks and no adjugate guard. These can equivalently be stated
without an infinite label search. Put b=floor B11, c=floor B22; the
candidate has source floors b+q,c+q. Its actual quotient equals q exactly
when

    q in Z,  b+q!=0,  q²+(b-1)q-c=0.                 (4)

The last equation says q(b+q)=c+q and itself ensures divisibility.
Thus (4) gives every L predecessor and at most two; it excludes no singular
matrix merely for its determinant. Identical actual source descriptions
are identified, not counted repeatedly. Write P_O(B) for each complete
actual predecessor relation, O=M,G,L,Q.

The formulas also prove a complete analytic atlas directly. For fixed q,
adj(A)-qI maps each open set {epsilon det A>0} analytically and bijectively
onto {B:det(B+qI)>0}, with analytic inverse (3); Q is the q=0 unshifted
case. L's fixed-label translation is an analytic diffeomorphism on all X.
Restrict these sheets to actual Borel source-label sets. They form disjoint
countable Borel sources, have Borel images by the ambient homeomorphism,
and have precisely the inverses just established. Q uses two sign sheets,
not an additional copy for every unused quotient.

This explicit atlas is an allowed replacement for the card's rational-ball
atlas. To compare them, every legal source has an open analytic inverse
neighborhood on its sheet, containing an eligible rational ball with closure
inside that neighborhood. First-eligible subtraction covers the same actual
source without omission or duplication, and both inverses agree by (3)/(4).
No unproved root-count or local-injectivity assertion is doing the work.

## 4. Every-point IMAGE and the original-volume clock

For a shifted adjugate branch at target B, put Y=B+qI. The inverse
derivative from (2) gives the prescribed every-point value

    J(B)=1/[2(det Y)^(3/2)] > 0.                     (5)

Both signs in (3) have this same absolute determinant. Q uses (5) with
Y=B; L has J=1 on each actual inverse branch. These are analytic ambient
germ values, finite and positive at every actual image point. Refining to
rational balls leaves them unchanged. Assigned floor faces use the unique
active source label, not a limit from a neighboring arithmetic cell.

For every Borel E in any actual inverse image domain, ordinary change of
variables on the ambient analytic diffeomorphism, restricted to E, proves

    mu(theta E)=integral_E J dmu.                     (6)

Extended integrals are allowed. A null-set density class alone would not
determine periodic null-point values; the frozen analytic version does.
Countable inverse branches and (6) imply nonsingularity of each partial T.
No global injectivity, invariant measure or conservative theorem is inferred.

The own legal clocks are therefore

    kappa_M(A)=kappa_G(A)=kappa_Q(A)=log 2+3log|det A|,
    kappa_L(A)=0,                                     (7)

on their respective, generally different legal domains. All signs and
zero values remain. There is no clock at a terminal and no new positive roof.

## 5. Whole histories, full kernels and every incoming depth

Fix an owner O and abbreviate its partial map to U. Let D_r be the domain
of r legal steps, D_0=X, S_0=0, S_r(A)=sum_{j<r} kappa_O(U^j A), and
M_r(A)=exp S_r(A), with M_0=1. For adjugate owners,

    M_r(A)=2^r product_{j<r}|det(U^j A)|³;             (8)

for L, M_r=1 and S_r=0. All nonempty expressions are confined to their
actual legal domains. The owner retains exactly the triples
G_O={(A,r-s,B):U^r A=U^s B legally}, with source B/range A and lag kept.
For each lag this is a countable union of Borel equality sets. Inversion
swaps the endpoints and negates lag. To compose witnesses (r,s) and (u,v),
advance the middle histories to ell=max(s,u); the resulting witness
(r+ell-s,v+ell-u) is legal because the longer middle history already exists.

Define on every actual triple

    c(A,r-s,B)=S_r(A)-S_s(B)=log(M_r(A)/M_s(B)).        (9)

Two witnesses of the same lag differ by equal additions to both lengths;
the common endpoint's added sums cancel, proving descent. The same middle
alignment proves additivity. The forward arrow (UA,-1,A) has clock
-kappa_O(A). Refinement into the analytic atlas makes an actual arrow
branch locally (U^r)^(-1)U^s with full modulus M_s(B)/M_r(A)=exp(-c).
Chain rule and change of variables on actual Borel pieces prove its own
every-Borel IMAGE, with the inherited all-point germ prescription.

The complete kernels, without a unit-only simplification, are

    K_lag={(A,0,B) in G_O},
    K_c={(A,r-s,B) in G_O:M_r(A)=M_s(B)},
    K_joint=K_lag intersect K_c.                     (10)

In particular K_c=G_L and K_joint=K_lag for L. The extension is on the
whole X×R, g:B->A sending (B,h) to (A,h+c(g)); height-preserving arrows
lift K_c and lag-zero arrows lift K_lag, with both conditions for the joint.

For every B in X, define P_O^0(B)={B} and
P_O^(j+1)(B)=union_{Y in P_O^j(B)} P_O(Y). Induction proves this is
exactly every depth-j predecessor, with all integers/signs/own permissions
already checked. Targets can be terminal, critical or on null cuts, and no
source is restricted to W. Infinite ancestral histories, if any, are just
compatible sequences of this relation, not new objects or free arrows.

For a terminal E, its complete source orbit is union_j P_O^j(E).
Every point A in it has a unique terminal hitting depth d(A). Any pair
A,B has exactly lag d(A)-d(B) and clock S_{d(A)}(A)-S_{d(B)}(B), since
an earlier common endpoint can be advanced to E. The three kernels impose
equal depths, equal entry sums, or both, respectively. Its isotropy is
trivial and its complete extension phase is h-S_{d(A)}(A) in R.

## 6. Entire isotropy and phases, not just a displayed subgroup

Nonzero isotropy for a deterministic partial map is equivalent to equality
of unequal legal iterates, hence to an eventually periodic forward history.
For eventual least source period p, every lag is a multiple of p after
advancing into the core, and every such multiple occurs. If the signed
least-cycle sum is C, incoming sums cancel and the full groups are

    Iso_G(A)=pZ,       c(kp)=kC,       H_A=CZ.         (11)

Identified actual triples do not acquire extra isotropy from inverse labels.
Extension isotropy is pZ when C=0 and trivial when C!=0. Non-eventually-
periodic orbits, including terminal-ending ones, have trivial source and
extension isotropy and H={0}; their inter-object clocks may still be nonzero.

Choose a reference E in one source orbit and an actual arrow a_A:A->E.
Its complete extension phase is h+c(a_A) modulo H_E. Another arrow
changes the coordinate by an isotropy clock; conversely equality modulo H_E
supplies an isotropy arrow, proving completeness. This is orbitwise, with
no global selector or regular quotient assertion. Height translation has
stabilizer exactly H_E. For C!=0 it yields one closed packet over that
source orbit, least positive time |C| and repeats j|C|, j>=1; negative/zero
group elements and source isotropy are retained. For C=0 there is no
positive return, though source/extension isotropy may be nontrivial.
Different source orbits remain different packets even if their times agree.
For L, c is identically zero on the WHOLE groupoid, so H={0} everywhere
and no positive height period exists. This follows from its clock, not a
higher-period census of its underlying arithmetic map.

## 7. Complete fixed matrices in the frozen W

The window has 1<=A11<2 and 1<=A22<2, all other seven entries in [-2,2].
Thus m=n=1 throughout W. MAIN, G and L all use actual q=1 there;
Q retains its arithmetic permission but no quotient shift. All remaining
matrix entries are unrestricted except for the seven stated closed bounds.

We use two full-matrix polynomial identities, not an eigenvalue ansatz:

    adj(adj A)=(det A)A,
    adj(A+tI)=adj A+t[(tr A)I-A]+t²I.                (12)

For invertible A the first follows from adj A=D A^{-1}, det(adj A)=D²;
polynomial continuation proves it for every A. The second follows by
expanding each two-by-two cofactor: diagonal entries gain t times the other
two diagonal entries plus t²; off-diagonal adjugate entries gain -t A_ij.
Thus (12) also includes every nonsymmetric or nondiagonal real matrix.

A MAIN/G fixed matrix in W is regular and satisfies adj A=A+I. Applying
(12) and the fixed equation yields

    D A=adj(A+I)=adj A+(tr A)I-A+I=(tr A+2)I.         (13)

Since D!=0 by the proved full guard, (13) forces A=aI. Scalarity has been
derived, not imposed on the carrier. Its equation is a²-a-1=0, so the
two formal scalars are phi=(1+sqrt(5))/2 and psi=(1-sqrt(5))/2.
Since 1<phi<2 and psi<0, only phi I lies in W. It satisfies all nine-entry
bounds, actual quotient/permission and full guard. Consequently

    Fix_W(M)=Fix_W(G)={phi I}.                        (14)

L would require A-I=A throughout W, which is impossible. Thus Fix_W(L)
is empty; this is not a statement about fixed matrices outside W.

For Q, a fixed regular A satisfies adj A=A. The first identity of (12)
then gives D A=A, hence D=1 since A is invertible. Laplace identity gives
A²=I. Conversely A²=I and det A=1 imply adj A=A.
The complementary projections (I+A)/2 and (I-A)/2 decompose the real
space into the +1 and -1 eigenspaces, so no Jordan or nonnormal case is
missing. If the -1 eigenspace has dimension r, det A=(-1)^r=1 forces
r=0 or 2, with trace 3-2r equal to 3 or -1. But W has tr A>=1+1-2=0,
excluding r=2. Hence A=I. This point is legal, regular and lies in W:

    Fix_W(Q)={I}.                                    (15)

This is a complete classification in the stated half-open/closed window,
not a new global fixed-set or higher-period census.

## 8. Unrestricted incoming basins of every found core

For any tested core E, the unrestricted recursion from §5 gives its entire
basin union_j P_O^j(E), not just its W part. Here the inverse formulas let
us evaluate those basins exactly without truncating labels or real roots.

For M/G target bI, every regular predecessor at label q must come from
Y=(b+q)I. Formula (3) requires b+q>0 and gives A=tI with
t=+sqrt(b+q) or -sqrt(b+q). There are no hidden nonscalar roots: (3)
exhausts the full legal nine-dimensional source. At a scalar tI, equal
floors force MAIN's q=1 whenever legal; G also uses q=1 for nonzero floor,
while floor t=0 gives G's q=0.

At b=phi, q=1 produces t=±phi since phi²=phi+1. Both are legal for M/G:
their floor pairs are (1,1) and (-2,-2), with nonzero determinants.
For G, the possible q=0 source would have 0<=t<1 and hence t²<1,
so it cannot produce phi>1. All other q fail the reconstructed scalar
source law. Thus P_M(phi I)=P_G(phi I)={phi I,-phi I}.
At b=-phi, q=1 would require t²=1-phi<0 and G's q=0 would require
t²=-phi<0. There is therefore no legal predecessor of -phi I in either
owner. The negative point itself is legal and maps to phi I; it is an
incoming leaf, not a terminal or a second fixed core. The full basins are

    B_M(phi I)=B_G(phi I)={phi I,-phi I}.              (16)

For Q, formula (3) at I gives exactly ±I. Both satisfy Q permission with
floor pairs (1,1) and (-1,-1), and both are regular. At -I, det(-I)<0
gives no legal predecessor. Since adj(-I)=I, the complete basin is

    B_Q(I)={I,-I}.                                   (17)

These incoming negative matrices lie outside the test window but were
neither deleted nor counted as additional fixed packets. L has no tested
fixed core; its all-target incoming relation (4) and histories remain complete.

## 9. Full tested-basin kernels, ENTIRE H, phases and repeats

In either basin {aI,-aI}, where a=phi for M/G or a=1 for Q, every legal
step has the same positive own clock

    K_a=log(2a^9).                                   (18)

This includes the negative incoming point: (2) there is negative, but its
absolute nine-dimensional multiplier is the same 2a^9. Both points map
to the fixed positive core. For any pair A,B in the basin and any integer
k, choose r,s>=1 with r-s=k. Their endpoints coincide, so every triple
(A,k,B) exists. All its witnesses have clock

    c(A,k,B)=kK_a.                                   (19)

Indeed every sum S_r on these two points is rK_a, including S_0=0.
This proves the ENTIRE restricted groupoid and clock, not a selected loop.
Its lag, clock and joint kernels all consist of every (A,0,B), including
non-unit arrows between the two points. At each point source isotropy is
all Z, its complete image is K_a Z, and extension isotropy is trivial.
In particular the non-fixed incoming point has eventual fixed isotropy,
not the trivial isotropy of a non-eventually-periodic history.

The complete phase can be written h mod K_a Z at either point. Transport
from the negative point to the positive core subtracts K_a, leaving the
same class. All real phases are retained, and one height circle over this
whole source orbit is one primitive packet, not one packet per sign/height.
The primitive is K_a, with positive repeats jK_a and all signed isotropy
elements retained. M and G are different owners even where (16) agrees.
Q's full tested packet has K_1=log 2, with no duplicate from its -I predecessor.

For MAIN/G, phi²=phi+1 gives phi³=2phi+1, phi^6=8phi+5 and
phi^9=34phi+21. Therefore

    exp K_phi=2phi^9=76+34sqrt(5).                    (20)

The square root of 5 is irrational: a lowest-terms rational square root
would force both numerator and denominator divisible by 5. Hence (20)
is irrational and cannot be any ordinary integer or prime. K_phi>0 since
phi>1. The primitive is not rescued by a negative source determinant,
a one-dimensional derivative, choosing the other inverse sign, or deleting
the incoming leaf; all of those full-owner data have been retained.

## 10. Scoped verdict and reproducibility boundary

MAIN has an owned positive primitive whose exponential is irrational,
so it fails the necessary prime-log target. This is STOP / FORK for this
candidate, independent of control-to-MAIN transfer. G separately shares
the adverse tested packet. Q separately supplies the prime-2 fixed packet,
which gives no credit to MAIN and no global prime-purity/coverage claim
for Q. L's wholly zero clock supplies no positive height period at all.

The full nine-dimensional source, original measure, actual inverse germs,
all-point clock, full histories, kernels, incoming states and entire
isotropy/phase conventions stay on the frozen owners. T0 ownership is
established here; the necessary arithmetic target fails. Strong naturalness,
untested returns and prime coverage remain OPEN; T1 NOT PASSED;
T3 NOT AUDITED; classical NOT APPLICABLE; formal Routes UNASSIGNED;
Route B NOT INVOKED. No later owner or work on 465 is started.

Methods were exact cofactor/derivative identities, full-dimensional linear
determinants, actual integer-floor source checks, analytic change of variables
and deterministic history arguments. No numerical evaluation, scientific
program, higher-period search, network, Git, PDF or old-file write occurred.
Only this raw report was written. Its original card and CP1 remain unchanged.
After full self-read and measured hash, freeze these bytes and HOLD for root's
full raw read and a distinct PAPER UNLOCK before any author comparison.
