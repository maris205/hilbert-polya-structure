# Frozen candidate — polynomial quotient/remainder register

Candidate ID: `ANG-20260920-PQR01`.
Paper ID: `318-polynomial-quotient-remainder-register`. Date: 2026-09-20.
Version: 1. Initial status: `OPEN — FULL REGISTER OWNER AND ONE/TWO-STEP GATE`.

## 1. Entire source and actual polynomial division

Freeze Y=R^2, its usual Borel structure and ordinary Lebesgue area.
All signed coordinates, axes, integer cuts and half-open cells remain.
For z=(x,y), put a=floor(x), b=floor(y). The actual
step is permitted exactly when b!=0 and b divides a,
using ordinary signed integer divisibility, and is

    P_z(xi)=x*xi+y, D_b(xi)=b*xi+1,
    q=x/b, r=y-x/b, P_z=q*D_b+r,
    T(x,y)=(r,q)=(y-x/b,x/b).

The constant polynomial remainder r has no Euclidean interval constraint.
The next dividend and divisor are read from the new REAL registers;
there is no carried digit label or time-dependent fitting schedule.
Every other state is terminal, retaining T^0, itself and ALL legal
incoming histories. No absorbing self-loop, reset, overflow or infinity point.
In particular the whole strip 0<=y<1 is terminal. Units b=+/-1,
a=0, negative/zero quotients and all cut endpoints remain under one rule.
No extra scale, root fibre, atom, integer-only restriction or selected centre.

## 2. Precise symbolic lineage and source access

At the actual integer register (n,d), n,d>=1, the permission is
d|n and the output is (d-n/d,n/d). The proper-divisor
symbols 1<d<n are retained inspection data, not a prime-only subsystem.
All other real/signed/unit states also belong to the same owner.
The arrow is floor-integer quotient permission -> actual real polynomial
division -> quotient/remainder registers -> next current admissibility test.
This is a stated deformation of divisor-symbolic dynamics, not merely
a generic plane map labelled arithmetic. b=floor(y), the divisor's
constant 1, register order and measure are DECLARED DESIGN. Stronger
naturalness, prime selectivity and a conservative or symplectic realization OPEN.
No Logistic/Henon conjugacy is asserted.

Input: [317 source/frontier](../317-noncommutative-central-carry-flow/evidence/scout-record.md),
all 206 lines read by root; SHA-256
`ee6989b090c666066d50efe511aa9f8be23112fd026053f382dfc7fc96059957`.
Original tuple author read 303-card lines 1–105 and 299-card
lines 1–88, not EOF/appended outcomes (the last line was
a next-audit heading). Old history was inherited. It read no
317 material/result/peer answer in original delivery; later author transcription
QA read only then-317-scout Section 3 lines 49–188.
Borel structure and zero-based sums were made explicit without changing
the tuple. No proof, inverse/image computation, clock result or
return calculation was supplied with it. Root does not assert global
novelty or nonconjugacy from a limited definition comparison.

## 3. Full inverse specification and actual clock owner

For EVERY integer pair a,b with b!=0 and b|a,
write U_ab=[a,a+1) x [b,b+1). Specify the inverse

    I_b(s,t)=(b*t,s+t),
    V_ab={b<=s+t<b+1, a<=b*t<a+1}.

ALL these actual domains and distinct predecessors must be counted;
equivalently enumerate every nonzero integer b with b<=s+t<b+1
and b|floor(b*t). Prove exact inverse identities, image and
boundary membership; do not assume bijectivity or onto. A target
without predecessors is not thereby terminal: its own next-step permission
uses its own second register. The zero-step object is never deleted.

For every actual inverse and Borel subset E of its actual domain,
derive from this affine map and area

    mu(I_b(E))=integral_E J_(I_b) dmu,
    J_(I_b)=abs(det D I_b).

The analytic determinant of the actual branch specifies the FULL-POINT
version also on every retained null face/axis/cut. No a.e.-uniqueness
claim, atomic ratio or invented boundary inverse. Establish finite branch-pair
IMAGE, positivity and composition; no log-prime clock is preassigned.

Only the full actual retained-lag groupoid is permitted:

    G={(z,k-l,w):T^k z=T^l w, k,l>=0, all steps legal},
    source w, range z; inherited Borel structure in Y x Z x Y.

Equal triples are one arrow, not words, germs or arbitrary affine arrows.
For each legal z and its actual inverse B_z=I_floor(y), set

    kappa(z)=-log J_(B_z)(Tz),
    c(z,k-l,w)=sum_(0<=i<k)kappa(T^i z)
               -sum_(0<=i<l)kappa(T^i w).

Prove presentation independence and cocycle law; terminal length-zero sums
are zero without evaluating a nonexistent terminal step. Keep ALL Y x R_h,
arrows (w,h)->(z,h+c) and full R-translation. Only a Borel/set
quotient is proposed, not a smooth/etale flow or invariant area-times-dh.
No roof, runtime cost, selected section or transported prime table.

## 4. Bounded return and whole-clock audit

First establish full ownership. Then solve ALL full-real one-step and
two-step returns, including every signed/unit cell, axis, cut and terminal
case. Both steps of T^2 must actually be legal. Exact branch-root
parameterization is permitted only with explicit exhaustive membership tests.
Simple algebra/sign/range constraints may close the test, not sample seeds.

For every discovered periodic core keep every actual finite predecessor;
prove full packet identity/phases. Distinguish least source period P,
source isotropy PZ, its ENTIRE time image H and extension kernel.
A positive primitive exists only when H=LZ has least L>0;
repetition rL belongs to the SAME packet. Equal labels/times do
not identify different packets. Preserve zero-time source/extension isotropy.

Also state what the derived clock implies CONDITIONALLY for an arbitrary
actual cycle; do not turn a cycle-product formula into existence or
absence of higher cycles. No unbounded higher-period census is authorized
by this card. A short exact structural identity is allowed if decisive.
If the one/two-step and own-clock tests remain inconclusive at higher
periods, retain that OPEN scope and stop this bounded round / fork.
Wrong primitive time, excess multiplicity or ownership failure is a stop.
Do not tune registers, permission, measure or clock to retain this ID.

## 5. Three separately owned controls

All controls keep Y, area, all boundaries/terminal histories and full
actual-lag/packet convention. Derive their OWN images, IMAGE and clocks.

DIVISIBILITY-OFF: permission only b!=0, same T and I_b;
its own target domain b<=s+t<b+1 has NO floor(b*t) filter.
Audit all one/two-step returns and full discovered packet groups.

DIVISIBILITY-SHIFT: permission b!=0 and b|(a+1), same T
and I_b; own target domain b<=s+t<b+1 and b|(floor(b*t)+1).
Audit all one/two-step returns and full discovered packet groups.

DIVISOR-CONSTANT-OFF: change the actual polynomial divisor to D_b^0=b*xi,
keeping the MAIN permission and the SAME (remainder,quotient) register order.
Thus T_0(x,y)=(y,x/b), NOT removal of the unit-integer branch.
Its own inverse is I_b^0(s,t)=(b*t,s), on the entire
domain b<=s<b+1, b!=0, b|floor(b*t). Audit complete
image/IMAGE, ALL fixed and two-step returns and their full basins,
isotropy, time groups and phases. Higher periods may remain OPEN.

Control evidence never supplies a missing main orbit or clock.
No scientific numerics, coefficient cutoff, prime/zero data, external literature
campaign or operator construction is planned. Finite checks prove no
infinite claim; exact full-state one/two-step proofs are not all-period proofs.

## 6. Review, scope and authority

Root owns all files except evidence/independent-review.md. ARS original-card,
synthesis and final-adverse checkpoints use inherited-model/shared-history internal AI,
NOT_CALIBRATED, not external peer review, cross-model verification or independent
error evidence. Main reviewer completes ALL main/control raw findings before
manuscript/peer release, without auxiliary delegation. Record exact read ranges,
hashes, access order and any later influence on root's manuscript.

T0--T3 are broadened owner labels, not formal Route coordinates.
Stronger naturalness OPEN; T3 NOT SUPPLIED. Classical symplectic base,
positive-roof mapping torus and A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED;
B NOT INVOKED. Markdown only, no PDF/LaTeX, publication/upload, Git
staging or commit. Positive 304, 317 and older packages unchanged;
241/242 paused; programme goal active. Verify Markdown links, candidate/status
consistency, frozen prefix/proof/review/input locks and exact claim scope.

## 7. Appended outcome — original definition unchanged

Candidate ID: `ANG-20260920-PQR01`.
Status: `OWNED REGISTER CLOCK; ONE/TWO-STEP RETURNS ABSENT — STOP / FORK`.
The original first 164 lines remain byte-preserved, SHA-256
`ab764785594498f289f04c026d3ee38de66a1ba3a6585236f8fe41389d4ce099`.

The [paper](paper.md) proves exact polynomial division, complete inverse/image
and actual area IMAGE |b|, hence full-point kappa=-log|b|.
For target (s,t), the only possible inverse uses B=floor(s+t);
it exists iff B!=0 and B|floor(B*t). The full source
is a partial injection, not onto; terminality is its own forward
permission, not absence of incoming branches. All cuts and histories remain.

ALL main fixed points and two-step returns are absent. The fixed
equations force an illegal zero divisor. Two-step return equations force
(b-1)(d-1)=1, hence b=d=2, incompatible with q=-y and
both current floors equal to 2. This exhaustive short-return result
does NOT rule out higher periods. Positive higher-cycle existence, prime
selectivity and multiplicity remain OPEN / UNCLASSIFIED.

For any actual least-P cycle, conditionally N=product |b_i|>=1
is integer: source isotropy PZ; if N=1, H0 and kernel
PZ; otherwise entire H=log(N)Z and kernel0. The least
positive time, if it exists, is log N. Partial injectivity proves
no external finite tail enters any cycle. The complete discovered
packets, terminal histories and real phases use actual arrows, not labels.

DIVISIBILITY-OFF and DIVISIBILITY-SHIFT have their own exact images,
inverses and |b| IMAGE; ALL their one/two-step returns are also
absent. Higher returns remain OPEN. DIVISOR-CONSTANT-OFF has its own
inverse (bt,s), and exactly [1,2)^2 as the full two-step
return locus, with diagonal fixed cores and off-diagonal swap pairs.
Every such packet has zero time, source/extension Z or 2Z,
and no external incoming tails. An exact whole-cycle product identity
proves ALL this control's time groups zero. A unit-boundary period-three
cycle also exists; the complete higher source classification is UNCLASSIFIED.
No control result transfers to the main owner.

Portfolio STOP / FORK only at the precommitted bounded gate,
not a global target-impossibility verdict. Same-object ledger intact; T0/owned
T1 established; stronger naturalness OPEN; T2 higher prime-packet target OPEN;
T3 NOT SUPPLIED / NOT PURSUED. Classical A0/A1/A2 NOT
APPLICABLE; formal UNASSIGNED; B NOT INVOKED. See [ledger](claim-ledger.md),
[evidence](evidence/README.md), [review](evidence/independent-review.md),
[source/frontier](evidence/scout-record.md) and [index](README.md).
Positive 304 and older packages unchanged; 241/242 paused; goal active.
