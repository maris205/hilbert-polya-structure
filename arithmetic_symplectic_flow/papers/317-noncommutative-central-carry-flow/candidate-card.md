# Frozen candidate — noncommutative central-carry feedback

Candidate ID: `ANG-20260920-CCF01`.
Paper ID: `317-noncommutative-central-carry-flow`. Date: 2026-09-20.
Version: 1. Initial status: `OPEN — FULL CENTRAL-CARRY OWNER AND FIXED/TIME GATE`.

## 1. Entire source, cell law and actual feedback

Freeze X=R^3, usual Borel structure and ordinary Lebesgue volume.
All signed coordinates, axes, cuts and origin remain. No integer
root fibre, extra scale, atom, selected centre or prime subsystem.
Specify

    (a,b,c)*(r,s,t)=(a+r,b+s,c+t+a*s),
    delta_m(a,b,c)=(m*a,m*b,m^2*c).

For every g=(x,y,z), use the actual coordinate readout

    A=floor(x), B=floor(y), r=x-A, s=y-B,
    C=floor(z-A*s), t=z-A*s-C,
    gamma=(A,B,C), f=(r,s,t) in [0,1)^3,
    D_gamma={A<=x<A+1,B<=y<B+1,C<=z-A*(y-B)<C+1}.

Set m=1+|C|. Residues are the standard NONNEGATIVE representatives,
also for negative integers. Freeze the digits/quotients

    j1=A mod m, a=(A-j1)/m,
    j2=B mod m, b=(B-j2)/m,
    j3=(C-j1*m*b) mod m^2,
    c=(C-j1*m*b-j3)/m^2,
    d=(j1,j2,j3), eta=(a,b,c).

The central borrow j1*m*b belongs to this actual arithmetic
step. Freeze the feedback and complete action

    F(x,y,z)=(y,z,x+y*z), F_inverse(u,v,w)=(w-u*v,u,v),
    d^(-1)=(-j1,-j2,-j3+j1*j2),
    T(g)=F(delta_m^(-1)(d^(-1)*g)).

The next digits come from the new REAL point, not a
carried label or external schedule. At C=0, m=1 and
all digits vanish under the SAME rule. Every coordinate cut
uses its actual half-open branch; no reset, terminal, overflow,
infinity point or deleted state. Prove actual totality and all
stated cell/quotient identities rather than assuming group terminology suffices.

## 2. Precise symbolic lineage and input access

The actual digit j1 retains m|A iff j1=0.
The FULL cell gamma=(n,0,d0-1), n,d0>=1,
has m=d0 and displays d0|n, including proper-divisor symbols
at 1<d0<n. This is an inspection interface, not an
acceptance gate or carrier restriction. Any factor-set observation is derived
read-only data, not additional transport input, clock or branch selector.

The arrow is divisor-symbolic readout -> finite current remainders ->
noncommutative quotient/borrow -> real feedback generating the next cell.
Multiplication, m=1+|C|, dilation powers, feedback and measure
are DECLARED DESIGN. Stronger naturalness and prime selectivity OPEN;
no canonical A0, Logistic/Henon conjugacy, conservative realization or
classical symplectic structure follows from the three-dimensional coordinates.

Input: [316 source/frontier](../316-integer-remainder-matrix-division/evidence/scout-record.md),
all 225 lines read by root, SHA-256
`38c76ad0c810f5922b768d9386b840449cdb02878820d3e6e50e2a9385c5aa7a`.
Original author directly read 283-card lines 1–94/164 and
301-card lines 1–96/196, not EOF/outcomes, but inherited
old results. It read no 315 frontier or 316
file/result/review during delivery. Later definition-only transcription QA read
then-316-scout Section 3 lines 49–209. Explicit Borel/integral-
IMAGE/direction fields and zero lower summation bounds were documented
without changing any action. No inverse, clock or return theorem
came with the tuple. No old-owner credit transfers.

## 3. ALL inverse branches, full-point IMAGE and lag

For EVERY gamma in Z^3 with its own m,d, specify

    theta_gamma(w)=d*delta_m(F_inverse(w)), w=(u,v,w3),
    X_gamma=j1+m*(w3-u*v),
    Y_gamma=j2+m*u,
    Z_gamma=j3+m^2*v+j1*m*u.

The whole target domain E_gamma is

    A<=X_gamma<A+1, B<=Y_gamma<B+1,
    C<=Z_gamma-A*(Y_gamma-B)<C+1.

Prove inverse identities, exact union image and complete predecessor
enumeration. Keep all gamma, overlaps and distinct preimages; do
not presume onto/finite-to-one/continuity/etale or truncate integer labels.
An exact countable enumeration with stated unresolved cardinality is allowed;
a point outside the image still remains an object of X.

For each actual inverse and finite branch pair establish

    mu(theta E)=integral_E J_theta dmu,
    J_theta=abs(det D theta).

Use the analytic formula of the actual half-open branch on
ALL retained cuts/axes, not conull deletion or atom ratios.
Prove positivity, actual substitution and consistent finite composition. A.e.
IMAGE alone does not fix null values; no constant determinant
value or arithmetic logarithm is imposed before the derivation.

Only the full actual retained-lag groupoid is permitted:

    G={(z,k-l,w):T^k z=T^l w, k,l>=0}, source w, range z,

with inherited Borel structure in X x Z x X.
Equal triples are one arrow, not ambient multiplication arrows, free
digit words or germs. For the actual inverse B_z at Tz,

    kappa(z)=-log J_(B_z)(Tz),
    c(z,k-l,w)=sum_(0<=i<k)kappa(T^i z)
               -sum_(0<=i<l)kappa(T^i w).

Prove presentation independence and the cocycle law pointwise. Keep ALL
X x R_h, arrows (w,h)->(z,h+c) and full
translation h->h+time. Lebesgue times dh may be a reference
measure, not presumed invariant. No roof, runtime cost or
label-selected time. Only a Borel/set quotient is proposed.

## 4. Bounded fixed and whole-clock discriminators

First classify ALL full-state fixed points, including C=0, negative
cells, axes and cuts. Solve their coordinate equations and
cell self-consistency, not a selected prime fibre. An exact
exhaustive branch-root parameterization is acceptable if all membership tests
are explicit; do not restate T(g)=g as a result.
Use elementary sign/range constraints to close it further if decisive.

Keep every actual finite predecessor and prove full fixed-basin packet
identity/phases. Distinguish source isotropy, its ENTIRE time image H,
and extension kernel. Positive primitive means H=L Z with least
L>0; repetitions rL are of the SAME packet, not
equal labels/times or a preferred loop. Preserve zero-time isotropy.

Also test the derived whole-clock multiplication law on arbitrary source
cycles: does it itself force or exclude admissible prime primitive
times? Such a universal algebraic obstruction may decide the target
without a higher-period census. If positive higher returns are not
proved or excluded, say OPEN; never turn a conditional time
formula into existence or no-cycle theorem. A first finite-iterate
identity may be used if sufficient, not an unbounded campaign.

Ownership failure, wrong primitive time/multiplicity or absence of target
times gives STOP / FORK. After the decisive gate finish
only the specified controls and review. Do not rescale the
clock, change measure/dilation, delete units, add a roof or
construct T3 to rescue this frozen owner. Inconclusive fixed tests
are preserved with their exact OPEN scope, not endless tuning.

## 5. Three controls with their OWN owners

All controls keep the entire X, same measure/boundaries and full
actual-tail/packet convention, deriving OWN inverse domains, IMAGE and clock.

COMMUTATOR-OFF: multiplication becomes vector addition, C=floor(z), ordinary
unit-cube cells. Keep m=1+|C|, delta_m and F, with
j1=A mod m, j2=B mod m, j3=C mod m^2.
Set T_ab=F(delta_m^(-1)(g-d)). Inverse d+delta_m(F_inverse(w)),
on exactly those targets whose inverse is in that original
ordinary cell. Nonlinear F remains. Audit complete inverse/image,
all fixed cells and full time/isotropy, plus the same
whole-clock discriminator, without borrowing the main cell identity.

FEEDBACK-OFF: set F=id only; retain main cell/digit/multiplication laws.
Inverse theta_gamma(w)=d*delta_m(w) on exactly theta_gamma(w) in D_gamma.
Audit complete inverse/image, ALL fixed points (including any full
unit-cell region), all fixed-core/finite-tail groups and whole-clock discriminator.

UNIT-DILATION: set m=1 globally, recompute the same residues
(all zero). The action is F, inverse F_inverse on
ALL X, not a chosen C=0 subsystem. Audit its
own IMAGE, ALL fixed points and global time groups; higher
source periods may remain UNCLASSIFIED even if all times are decided.

No scientific numerics, coefficient cutoff, prime data, external literature
campaign or operator construction is planned. Any global impossibility claim
must follow from this actual clock/source, not a finite check.

## 6. Review, scope and authority

Root owns all files except evidence/independent-review.md. ARS original-card,
synthesis and final-adverse checkpoints use inherited-model/shared-history internal AI,
NOT_CALIBRATED; no external peer review, cross-model verification or
independent-error guarantee. Complete raw results before manuscript/peer release.
Record exact inputs, read ranges, hashes and later influences.

T0--T3 are broadened owner labels. Stronger naturalness OPEN;
T3 NOT SUPPLIED. Classical symplectic base, positive-roof mapping torus
and A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
Markdown only; no PDF/LaTeX, publication, upload, staging or
Git commit. Positive 304, 316 and older packages unchanged;
241/242 paused; programme goal active. Verify links, candidate/status
consistency, frozen prefix/proof/review/input locks and exact claim scope.

## 7. Appended outcome — original definition unchanged

Candidate ID: `ANG-20260920-CCF01`.
Status: `OWNED CENTRAL-CARRY CLOCK; PRIME TIMES EXCLUDED — STOP / FORK`.
The original first 197 lines remain byte-preserved, SHA-256
`301ff3423c91673e6baae9e2287579059465b7b46eaee5e2a97a0cd7c5af1054`.

The [paper](paper.md) proves all cell/quotient identities, inverse branches
and exact target-wise predecessor enumeration. Noninteger targets have finitely
many predecessors; origin has countably infinitely many, all retained.
Target (0,1,0) is not in the image. The total
Borel source is nononto and not globally finite-to-one.

Actual volume IMAGE is J=m^4 on every inverse branch,
with kappa=-4log m and the frozen analytic full-point version.
Finite branch-pair products and common-future cancellation define the full
retained-lag cocycle. No borrowed prime clock or multiplicity measure.

At ANY eventually periodic state with least source period P,
let N be the product of m around its actual cycle.
Source isotropy is PZ. If N=1 then H=0 and
extension kernel PZ; if N>=2 then ENTIRE H=(4log N)Z
and extension kernel zero. Non-eventual states have all groups zero.
Thus every possible positive primitive is log(N^4), never log
of a prime. This is a GLOBAL target-time obstruction,
NOT proof of existence or absence of positive higher cycles.
Their existence and full source classification remain OPEN / UNCLASSIFIED.

The complete main fixed locus is only origin, proved by
exhaustive signed-cell inequalities. Its full finite predecessor basin retains
source/extension Z and zero H, with real prefix-adjusted phase.
No positive fixed packet exists, but higher periods are not erased.

COMMUTATOR-OFF has exactly origin and one other fixed core,
the latter of primitive log16. FEEDBACK-OFF has the full
C=0 zero-time fixed region and precisely three additional positive
fixed cores, each primitive log16 with distinct full basins.
UNIT-DILATION owns a global zero clock and only origin as
a fixed point. Each control has its OWN inverse/image/IMAGE
and prefix phases; untested higher source periods stay UNCLASSIFIED.

Portfolio STOP / FORK. Same-object ledger intact; T0/owned
T1 established; stronger naturalness OPEN; T2 prime-time target FAILS
at all periods; T3 NOT SUPPLIED / NOT PURSUED.
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
See [ledger](claim-ledger.md), [evidence](evidence/README.md),
[review](evidence/independent-review.md), [source/frontier](evidence/scout-record.md)
and [index](README.md). Positive 304 and older packages unchanged;
241/242 paused; goal active. Markdown only; no Git commit/publication.
