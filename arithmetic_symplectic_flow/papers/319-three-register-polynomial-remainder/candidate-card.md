# Frozen candidate — three-register polynomial integer-remainder feedback

Candidate ID: `ANG-20260920-PRF01`.
Paper ID: `319-three-register-polynomial-remainder`. Date: 2026-09-20.
Version: 1. Initial status: `OPEN — FULL POLYNOMIAL OWNER AND FIXED-CELL GATE`.

## 1. Entire carrier, arithmetic and actual update

Freeze X=R^3, usual Borel structure and ordinary Lebesgue volume.
Every signed coordinate, axis, integer cut and origin remains. Read

    A=floor(x), B=floor(y), C=floor(z), h(t)=t^3+t,
    N=h(A)+C=A^3+A+C.

For B!=0 set R=N mod |B|, the unique nonnegative residue
0<=R<|B|, and q=(N-R)/B. For B=0 set q=0,
R=N: explicit totalization, not ordinary division. Units B=+/-1
use the same rule; no selected root, atom, passive scale or deletion.
The entire autonomous update is

    T(x,y,z)=(y,z,h(x)+z-q*y).

Every step rereads the new actual real cell, numerator and quotient.
All three registers participate. No terminal, reset, overflow or infinity point.
At integer inputs the intended arithmetic register law is
(A,B,C)->(B,C,N-qB); prove it rather than using a label
as substitute for the actual source. Cubic real interpolation is design.

## 2. Symbolic lineage and exact definition access

The actual quotient/remainder digit retains B|N iff R=0 when
B!=0. On the FULL cell (A,B,C)=(0,d,n), d,n>=1,
N=n, giving precisely d|n and proper-divisor symbols at 1<d<n.
All three fractional coordinates and failed-divisibility states remain; this is
an inspection interface, not a prime-only acceptance/deletion gate.
The arrow is divisor-symbolic observation -> current Euclidean quotient/remainder
constraint -> quotient participating in real transport -> new arithmetic input.
No prime/factor table, zero data, per-prime parameter or time schedule.
Cubic h, third-register addition, B=0 totalization and volume are DECLARED
DESIGN; stronger naturalness and prime recurrence OPEN. No conservative/symplectic
lift, Logistic/Henon conjugacy or previous owner's credit is asserted.

Input: [318 source/frontier](../318-polynomial-quotient-remainder-register/evidence/scout-record.md),
all 199 lines read by root, SHA-256
`7c7dcb9609bfa92d79e56c392211369becd73a441a66a9ae2a65752133bf5e6c`.
Original author read 299-card lines 1–96/192 and 303-card lines
1–115/202, neither EOF nor appended outcome. Old history inherited.
During original delivery it read no 318 material/result, current 317
scout or peer tuple. Later definition-only transcription QA read then-318-scout
Section 3 lines 48–182, not other sections/files/results. No proof,
inverse/IMAGE/return evaluation or numeric calculation accompanied the tuple.
No global novelty/nonconjugacy follows from this bounded historical comparison.

## 3. ALL inverse specifications and own full-point IMAGE

For every gamma=(A,B,C) in Z^3, retain
D_gamma=[A,A+1) x [B,B+1) x [C,C+1) with own q_gamma.
Specify real cube roots in

    sigma(a)=cbrt(a/2+sqrt(a^2/4+1/27))
             +cbrt(a/2-sqrt(a^2/4+1/27)).

For target w=(u,v,w3), the proposed inverse and FULL domain are

    theta_gamma(w)=(sigma(w3-v+q_gamma*u),u,v),
    E_gamma={A<=sigma(w3-v+q_gamma*u)<A+1,
             B<=u<B+1, C<=v<C+1}.

Prove sigma's actual inverse property, positivity/smoothness needed below,
every inverse identity, exact image and exhaustive predecessor enumeration.
Count ALL gamma, actual overlaps and predecessors without integer cutoff.
An exact countable target-wise enumeration is acceptable; if cardinalities
are unresolved, say so rather than assume onto or finite-to-one.
A target without predecessors still belongs to the full total source.

For each actual inverse and finite branch pair derive

    mu(theta E)=integral_E J_theta dmu, J_theta=abs(det D theta),

on every Borel subset of the actual domain. The FULL-POINT version
uses its own explicit analytic branch at cuts/axes, without extending
the actual domain or claiming a.e. uniqueness. Prove finite positive IMAGE,
substitution and composition; do not preassign a prime clock or atom.

Use only the actual retained-lag groupoid

    G={(z,k-l,w):T^k z=T^l w, k,l>=0}, source w, range z,

with inherited Borel structure in X x Z x X. Equal triples
are one arrow, not quotient words, ambient polynomial maps or germs.
For the actual inverse B_z from Tz to z define

    kappa(z)=-log J_(B_z)(Tz),
    c(z,k-l,w)=sum_(0<=i<k)kappa(T^i z)
               -sum_(0<=i<l)kappa(T^i w).

Prove pointwise presentation independence/cocycle. Keep ALL X x R_h,
arrows (w,h)->(z,h+c), all R-translations and complete actual packet
identity. Volume times dh is only reference measure, not presumed invariant.
Only a Borel/set quotient is proposed, not a smooth/etale flow.

## 4. Fast fixed-cell discriminator and exact packet obligation

After full ownership, solve ALL full-state fixed points within the three
preselected COMPLETE cells D_(0,0,0), D_(1,1,1), D_(2,2,2).
These are a counterexample-first test, NOT a restricted carrier or a
global fixed census. Keep all cuts and the zero/unit cases. If
the same short algebra closes all fixed cells without a campaign,
record that stronger exact classification with its sign/range proof; otherwise
preserve remaining fixed states OPEN. No selected favourable line counts as
full fixedness or supplies the full incoming packet.

For each discovered core retain EVERY actual finite predecessor and full
tail class. Distinguish source isotropy, its ENTIRE time image H and
extension kernel. Positive primitive requires H=LZ with least L>0;
repetitions rL belong to that SAME packet. Equal periods/labels do not
merge distinct packets. Retain zero-time source/extension isotropy and phases.

Ownership failure, wrong/nonprime primitive time or excess multiplicity gives
STOP / FORK. No higher-period census after a decisive fixed witness.
If tests are inconclusive, keep OPEN and stop the bounded round, not
tune source, clock, measure or selected cells. A short whole-clock identity
may bound other periods but must not be mistaken for their existence.
Higher source periods remain UNCLASSIFIED unless explicitly proved otherwise.

## 5. Controls with OWN sources/inverses/clocks

All keep entire X, volume, cuts/units, actual-lag and complete packet
convention. Each owns its full image/IMAGE, fixed-cell and phase audit.

DIVISION-OFF: q=0 globally, T_0=(y,z,h(x)+z), proposed inverse
(sigma(w3-v),u,v) on ALL X. Cell decomposition only restricts the
inverse point to D_gamma; it creates no extra arrow labels. Audit
all fixed points if the direct equation closes them, not only units.

POLYNOMIAL-OFF: h(x) becomes x AND integer N becomes A+C.
Recompute own q,R with the same B=0 convention. Its action
is T_lin=(y,z,x+z-q*y), inverse (w3-v+q_gamma*u,u,v)
on exactly those targets for which this point lies in D_gamma.
Audit complete image/IMAGE, the same three fixed cells, all other
fixed cells if the same short equation closes them, and whole-clock scope.

THIRD-NUMERATOR-OFF: remove C from N and z from the real
numerator, but retain all three cyclic registers. Own N=h(A), own
q,R and B=0 rule; T_nc=(y,z,h(x)-q*y). Proposed inverse
(sigma(w3+q_gamma*u),u,v) on exactly its own D_gamma membership
domain. Audit its own image/IMAGE and fixed/packet gates as above.

No control supplies a main orbit or time group. No scientific numerics,
prime/zero data, external literature campaign or operator construction planned.

## 6. Review, verification and authority

Root owns all files except evidence/independent-review.md. ARS original-card,
synthesis and final-adverse checkpoints use inherited-model/shared-history internal AI,
NOT_CALIBRATED, not external peer review, cross-model or independent-error evidence.
Main reviewer completes ALL main/control raw results before paper/peer release;
no auxiliary delegation. Record actual access, hashes, sequence and influences.

T0--T3 are broadened owner labels only. Stronger naturalness OPEN;
T3 NOT SUPPLIED. Classical symplectic base, roof/mapping torus and
A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
Markdown only, no PDF/LaTeX, upload/publication or Git staging/commit.
Positive 304 and older packages unchanged; 241/242 paused; goal active.
Verify links, candidate/status, frozen prefix/proof/review/input locks and scope.

## 7. Appended outcome — original definition unchanged

Candidate ID: `ANG-20260920-PRF01`.
Status: `OWNED POLYNOMIAL CLOCK; COMPOSITE FIXED PRIMITIVE — STOP / FORK`.
The original first 165 lines remain byte-preserved, SHA-256
`8f7138b4f3478df3072c6fcf87f20620fcf72c7662505ec149fec042ed461d09`.

The [paper](paper.md) proves the root inverse, complete cell inverses,
exact target-wise image/predecessor enumeration and actual volume IMAGE.
B=floor(u)=0 gives one predecessor; outside that strip noninteger u
has finitely many (possibly zero), while nonzero integer u has zero
or countably infinitely many under an explicit residue-minimum image test.
Target (1,0,-1) is missing; (1,0,0) has exactly all
(A,1,0), A integer, as predecessors. The total source is
not onto or globally finite-to-one; every target object remains.

Owned full-point inverse IMAGE is 1/(1+3x^2) at its actual
predecessor x, so kappa=log(1+3x^2). Finite branch pairs and
common-future cancellation give the full retained-lag cocycle; forward-arrow
time is -kappa, inverse-arrow time +kappa. No prime clock inserted.

The same short signed-cell equation closes ALL fixed points: origin,
and g_n=diag(sqrt(n^2+1)) for every integer n>=1. Origin
has only itself as predecessor and source/extension Z with H0.
Every positive fixed core has its full countable actual incoming basin,
source Z, ENTIRE H=log(3n^2+4)Z, extension kernel0 and
prefix-adjusted real phase. Different basins cannot merge. Thus n=1
has primitive log7, but n=2 has genuine primitive log16. This
composite least time violates the prime-only target, not a selected
repetition of another packet. STOP / FORK; no higher-cycle census.

DIVISION-OFF owns a global smooth inverse and only origin fixed.
POLYNOMIAL-OFF owns its changed exact image/multiplicity, globally zero
clock, and only origin fixed. THIRD-NUMERATOR-OFF owns its changed
inverse/image and the same complete fixed family including its own
primitive log16; its basins use its OWN inverse chains. No control
membership or clock is transferred. Higher source cycles remain UNCLASSIFIED;
conditional cycle-clock formulae are not existence theorems.

Same-object ledger intact; T0/owned T1 established; stronger naturalness
OPEN; T2 prime target FAILS at the fixed-packet gate; T3 NOT
SUPPLIED / NOT PURSUED. Classical A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED. See [ledger](claim-ledger.md),
[evidence](evidence/README.md), [review](evidence/independent-review.md),
[source/frontier](evidence/scout-record.md) and [index](README.md).
Positive 304 and older packages unchanged; 241/242 paused; goal active.
