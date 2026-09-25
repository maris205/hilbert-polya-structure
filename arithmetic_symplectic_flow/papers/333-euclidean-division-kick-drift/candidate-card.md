# Frozen candidate — Euclidean-division kick–drift

Candidate ID: `ANG-20260920-EKD01`.
Paper ID: `333-euclidean-division-kick-drift`. Date: 2026-09-20.
Version:1. Initial status: `OPEN — FULL TRANSPORT AND IMAGE CLOCK`.

## 1. Entire carrier and actual arithmetic action

Take X=R2_q x R2_p, its usual Borel structure, and mu=Leb4.
This is a Borel piecewise-affine/groupoid proposal, not a claimed globally
C^r symplectic map, Hamiltonian flow or classical ASFS suspension.

For q=(q1,q2) put a=floor(q1), b=floor(q2) and define

    if b!=0: s=floor(a/|b|), r=a-|b|s;
    if b=0: s=0, r=a;
    K_(a,b)=(r,s);
    p*=p+K_(a,b);
    T(q,p)=(q+p*,p*).

The full quotient and remainder change actual momentum. The new position
determines the next integer readout. All negative, zero, unit and noninteger
coordinates, arbitrary real momenta and exact integer boundaries remain. There are
no terminals, absorbing states, preferred sections or deleted nonwitnesses. Zero divisor
is NOT an admissible divisor: chi(q)=1_(b!=0 and r=0).

All unit coefficients, floor readout, coordinate order (r,s), zero-divisor rule
and unweighted measure are fixed design inputs, not fitted parameters. Prime
tables, log p, Mangoldt weights, zeros and per-prime choices are prohibited.

## 2. Complete inverse prescription and full-point IMAGE

Write I_(a,b)=[a,a+1) x [b,b+1), B_(a,b)=I_(a,b) x R2.
At target (u,v) the proposed inverse is

    q=u-v; (a,b)=floor(q); p=v-K_(a,b).

The branch target domain and inverse are exactly

    E_(a,b)={(u,v):u-v in I_(a,b)};
    theta_(a,b)(u,v)=(u-v,v-K_(a,b)).

Every cut belongs to the lower endpoint's half-open cell. No extra
boundary predecessor or free history label is inserted. Prove full coverage,
uniqueness, both inverse identities and Borel ownership; formulas alone are not
proofs. A branch has the displayed full-space affine extension theta^aff.
Prescribe j_theta(z)=|det D theta^aff| on ALL of its own E.
This is not the derivative of a globally smooth map. Prove
finite positivity and mu(theta A)=integral_A j_theta dmu for EVERY Borel
A subset E, including null/cut states, plus actual compositions and inverses.
No a.e. modification, density change or extra atomic weight is permitted.

## 3. Actual lag groupoid, clock and complete packets

Prescribe G={(x,m-n,y):T^m x=T^n y, m,n>=0}, source y,
range x, inherited Borel structure in X x Z x X.
Identical triples are identical arrows, even with different m,n witnesses.
Use actual compositions and inverses; branch names add no isotropy.

Let B_x:Tx->x be the actual successor inverse branch and prescribe

    kappa(x)=-log j_(B_x)(Tx);
    S_m(x)=sum_(0<=i<m) kappa(T^i x), S_0=0;
    c(x,m-n,y)=S_m(x)-S_n(y).

Representation independence, additivity and same-owner IMAGE meaning require audit.
Keep all X x R_h with arrows (y,h)->(x,h+c), and height
translation h->h+t. This is an IMAGE extension, NOT mechanical elapsed
time for kick–drift and NOT a unit-roof suspension. Iteration count is
not relabelled physical time.

Retain entire source isotropy, its clock kernel, extension fixed-object isotropy,
and H_x=c(G_x^x). A positive primitive requires ENTIRE H_x=LZ with
least L>0; repetitions are rL in the same oriented full packet.
Packets retain all actual incoming objects and height phases. Equal cells,
symbols, periods or coordinate translations do not identify distinct packets. All
nonperiodic and null sources and zero-clock lags remain. No coarse smooth
quotient or measurable global transversal is presumed. T3 analytic owner NOT SUPPLIED.

## 4. Three controls, each with its own entire owner

All use full X, mu, the same floor/boundary conventions, and their
OWN action, complete inverses, affine IMAGE versions, lag/clock/kernel and packets.

DIVISION-OFF (A): K^A_(a,b)=(a,b),

    T_A(q,p)=(q+p+K^A,p+K^A);
    E^A_(a,b)={(u,v):u-v in I_(a,b)};
    theta^A_(a,b)(u,v)=(u-v,v-K^A).

QUOTIENT-OFF (B): retain the full main r,s convention but K^B=(r,0),

    T_B(q,p)=(q+p+K^B,p+K^B);
    E^B_(a,b)={(u,v):u-v in I_(a,b)};
    theta^B_(a,b)(u,v)=(u-v,v-K^B).

DRIFT-OFF (C): retain main K, but

    T_C(q,p)=(q,p+K);
    E^C_(a,b)={(u,v):u in I_(a,b)};
    theta^C_(a,b)(u,v)=(u,v-K).

C uses u, NOT u-v, for its inverse domain/readout. Each j
is the absolute determinant of its OWN displayed affine inverse extension
on its entire own domain. No determinant value or return is given
as a frozen input result. No control clock repairs main.

## 5. Specific prior-work arrow and limits

At native seeds q=(n,d), ALL real p, d!=0, the current
readout executes Euclidean division. Restricting the observable, not the carrier,
to n>=2 and1<d<n makes chi the proper-divisor witness. The arrow is

    proper-divisor/prime-composite symbol -> current full quotient/remainder
      -> momentum kick -> real-position drift -> next arithmetic readout.

This is an autonomous conservative-style two-stage deformation of the sieve-symbolic
seed, with the second-order/shear geometry motivated by the Logistic/Henon bridge.
It is not a proved conjugacy, globally smooth symplectic lift, finite-
packet-preserving geometric realization, or natural prime selector. Actual volume ownership,
arithmetic relevance beyond this interface and primitive selection are OPEN. Arbitrary
cell rules in this template are an explicit PROVES_TOO_MUCH risk.

Classical base form/F/positive roof/mapping torus and classical A0/A1/A2 are
NOT APPLICABLE, not passed. Use owner T0–T3 only; formal UNASSIGNED;
B NOT INVOKED. No future Hamiltonian/contact/quantum owner is supplied.

## 6. Precommitted fast tests and bounded stop

First prove all-symbol inverse/IMAGE ownership and actual full-point compositions. Ask
whether that fixed unweighted IMAGE clock permits ANY positive primitive time.
If already excluded at this gate, stop without a long periodic census.
Do not change measure, add a roof or select cells to rescue it.

The bounded direct transport check covers each owner's first TWO steps
and inverse recovery for p=(0,0) and all five seeds

    q=(6,2), (5,2), (0,0), (-5,-2), (5,-1),

plus the ENTIRE half-open-boundary family

    q=(2-epsilon,2), p=(epsilon,0), 0<epsilon<1.

These are not precomputed orbits, and finite checks do not prove global
ownership. Root adds before freeze: describe all actual incoming orbits and
full source/kernel groups using actual least map periods, retaining any unknown
period-realization problem; zero IMAGE time is not absence of map cycles.
If the bounded owner/clock tests leave no credible same-object arithmetic/primitive
chain, record bounded OPEN and stop/fork; no long census or T3 rescue.

## 7. Definition provenance and review boundary

The definition-only author used filename searches then133 headings1,33 and original
body1–32/39, and134 headings1,29 and original body1–28/48, neither EOF.
Only the appended-outcome TITLES33/29 were exposed, not bodies. It contrasts
133's fixed finite divisor-polynomial/equilibrium source and134's fixed2,3,4 residual-potential/
unit-roof source with this moving full division readout; shared shear ancestry
remains. Root did not reopen those cards. No global novelty/nonconjugacy claim.
No third card, old paper/review, current332 science/peer, web, scientific calculation,
auxiliary or author write entered delivery. Shared history remains NOT_CALIBRATED.

Root owns all new package files except evidence/independent-review.md. Reviewer reads
ONLY this original card and personally derives main and ALL controls. It
sends metadata-only ALL RAW READY, holding ALL mathematics until root's first
paper is hash-locked AND explicit RAW RELEASE is received. ALL RAW FINAL
must precede a separate PAPER UNLOCK. Three ARS scrutiny checkpoints are
internal, shared-model/history NOT_CALIBRATED, not peer review or independent-error evidence.
No auxiliary/web/scientific numerics in review. Markdown only; no PDF/LaTeX,
publication/upload, staging/commit or model change. Earlier packages remain unchanged;
241/242 paused; programme goal active. Preserve this original prefix.

## 8. Version-1 outcome — appended after first manuscript lock

Final status: `OWNED DIVISION TRANSPORT; ALL IMAGE TIMES ZERO — STOP / FORK`.
Candidate ID remains `ANG-20260920-EKD01`. Original170 lines are unchanged.
No action, measure, clock, normalization, control or packet convention was altered.

Main/A/B own their complete inverse using SOURCE q=u-v and half-open
source cells; C owns the different u-based inverse. Each is a global
Borel bijection preserving Leb4, with its prescribed all-point affine inverse IMAGE
j=1 and every-Borel identity, including cuts and null states. All finite
compositions/inverses own the same value. Main is not globally continuous, so
this is not a smooth classical symplectic realization.

For each owner the whole lag groupoid has x=T^(-k)y. All kappa,
S_m and c vanish on EVERY arrow. Entire source isotropy is actual
least-map-period dZ or0; the kernel and extension fixed-object isotropy retain
that full source group. ENTIRE H_z={0} for every source. Thus no
positive primitive time exists in the frozen extension, although map cycles exist.

All incoming objects are the exact orbit T^Zz; no extra eventually-periodic
ancestors. Height phase remains all R for each orbit; no height translation
has a nonzero return. Main's entire fixed family is a=0,p=0;
A's is q in[0,1)^2,p=0; B's is r=0,p=0, with its
explicit zero-divisor rule. These continuum families are null, their individual incoming
orbits singletons. C is fully classified: a=0 gives fixed states for
all p, a positive-infinite-volume family; otherwise the whole incoming orbit is
(q,p+jK), j in Z, with source0. Higher main/A/B map periods
remain UNCLASSIFIED, not absent. All sources and lags remain in the object.

All five frozen seeds and the entire0<epsilon<1 boundary family have exact
two-step/inverse checks for each owner. They supplement, not replace, the global
proof. Arbitrary cell kicks admit the same volume/clock mechanism; this is
a PROVES_TOO_MUCH warning, not a claim of identical dynamics. The actual
division-to-motion interface is established, stronger prime naturalness OPEN. Portfolio **stop /
fork** at the global time obstruction; no density/roof repair or long census.

T3 NOT SUPPLIED / NOT PURSUED; classical ASFS A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED. Same-object ledger intact. A different complete
physical-flight billiard definition is pending without ID/freeze/audit or transferred credit.
See [paper](paper.md), [ledger](claim-ledger.md), [evidence](evidence/README.md),
[review](evidence/independent-review.md) and [frontier](evidence/scout-record.md). Goal active.
