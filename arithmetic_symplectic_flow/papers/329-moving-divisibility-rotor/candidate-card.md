# Frozen candidate — moving divisibility rotor field

Candidate ID: `ANG-20260920-MRF01`.
Paper ID: `329-moving-divisibility-rotor`. Date: 2026-09-20.
Version: 1. Initial status: `OPEN — FULL ROTOR OWNER AND RETURN CLOCK`.

## 1. Entire field source and actual motion

Let P=Z^2, V={(1,0),(0,1),(-1,0),(0,-1)}, Omega={0,1}^{Z^2},
and X=P x V x Omega. Use discrete P,V and the full
product topology/Borel on Omega. State x=(p,v,eta) includes integer test
position p=(n,d), direction v and ALL rotor bits eta_q. No
translation quotient, omitted unvisited tail, selected configuration or null-set deletion.

    chi(n,d)=1 if d!=0 and d divides n; otherwise0.
    R(v_1,v_2)=(-v_2,v_1).
    epsilon(p,b)=(2 chi(p)-1)(1-2b).
    eta^p flips only the bit at p.
    v_* = R^(epsilon(p,eta_p)) v.
    T(p,v,eta)=(p+v_*,v_*,eta^p).

The turn uses local divisibility AND local memory; the hit bit changes,
then the new position supplies the next test. All X has a
proposed successor. Keep d=0, n=0, negative coordinates, units and every
infinite field under the same rule. No terminal, reset, boundary overflow,
fixed-n scan or prescribed prime subsystem is introduced.

## 2. Full inverse and exact branch specification

At ANY target (p',v',eta') prescribe the candidate inverse

    p=p'-v'; b=1-eta'_p;
    v=R^(-epsilon(p,b)) v'; eta=(eta')^p.

Prove both inverse identities, full domain/image and uniqueness; do not assume
bijection from the formal expression. For p,v,b let

    B_(p,v,b)={(p,v,eta):eta_p=b};
    v_b=R^(epsilon(p,b))v;
    C_(p,v,b)={(p+v_b,v_b,eta'):eta'_p=1-b}.

The proposed actual inverse theta:C->B is the above inverse restricted
to that ENTIRE cylinder. Verify all source/target partitions, including all
integer boundaries and null configurations. Do not add free-history arrows.

## 3. Declared measure and fixed all-point IMAGE

Freeze mu=count_P x uniform_V x pi^(Z^2), with uniform_V(v)=1/4,
pi(0)=2/3 and pi(1)=1/3. This biased field law is DESIGN,
not a claimed natural, conserved or divisibility-forced probability. Establish its
full Borel law, sigma-finiteness, support/atom status and actual nonsingularity.

For theta:C_(p,v,b)->B_(p,v,b), prescribe the candidate version

    j_theta(z)=mu(B_(p,v,b))/mu(C_(p,v,b)), every z in C.

Prove mu(theta E)=integral_E j_theta dmu for EVERY Borel E
in C, not just a cylinder ratio, and prove all finite
actual-composition/prefix-pair IMAGE laws. Retain this full-point constant version on
null returning fields. No branch value is precomputed or supplied by
another owner, no a.e.-version change after locating a return.

## 4. Entire lag, time image, kernel and packet convention

Freeze G={(x,m-n,y):T^m x=T^n y,m,n>=0}, Borel from
X x Z x X, source y and range x. Equal triples
are one arrow. Define B_x:Tx->x as the actual inverse branch,

    kappa(x)=-log j_Bx(Tx);
    S_m(x)=sum_(0<=i<m)kappa(T^i x), S_0=0;
    c(x,m-n,y)=S_m(x)-S_n(y).

Prove descent, additivity, correct direction and owned IMAGE. Keep ALL
X x R_h with arrows (y,h)->(x,h+c) and all translations
h->h+t. No positive roof or operation-count time is inserted. Only
set/Borel quotient claims initially; no Hausdorff/smooth coarse flow, invariant
mu dh, embedded circle or analytic operator is presumed.

Use ENTIRE source isotropy G_x^x, H_x=c(G_x^x) and extension
kernel. A positive primitive requires the entire H_x=LZ with LEAST
L>0; repetitions stay in that same full packet. Full-field equality,
not particle position/direction closure, defines a source return. Keep every
incoming object, phase, untouched field, zero-clock lag and nonperiodic trajectory.
Equal times/position paths or finite-difference fields alone do not identify packets.

## 5. Three controls with their own complete owners

Each uses declared X,mu but reconstructs its OWN action, inverse cylinders,
all-point IMAGE, lag, source/time/kernel groups and packet/phase convention.

ARITHMETIC-OFF: set chi identically0, still turn/flip/move. Use its
own epsilon, v_b, and full inverse p=p'-v', b=1-eta'_p,
v=R^(-epsilon(p,b))v', eta=(eta')^p. Its branch target has
its own p+v_b,v_b and old-hit bit1-b.

MEMORY-WRITE-OFF: main turn/move, but eta'=eta. Inverse p=p'-v',
b=eta'_p, v=R^(-epsilon(p,b))v', eta=eta'. Branch target has
p+v_b,v_b and old-hit bit b, NOT main's flipped-bit cylinder.

TURN-OFF: T_0(p,v,eta)=(p+v,v,eta^p). Inverse p=p'-v',
v=v', eta=(eta')^p. Branch target has p+v,v and old-hit
bit1-b. There is no residual arithmetic turn or fixed-position substitute.

Each candidate j is its OWN source-cylinder mass/target-cylinder mass, fixed
on that full target; prove the Borel law and complete versions.
Equal declared measure/carrier does not transfer any result across controls.

## 6. Specific lineage and classical limits

At every full field/direction, the actual turn at (n,d) uses
d|n. For n>=2,1<d<n this is the original proper-divisor
admissibility observable. The arrow is divisor/prime-composite symbol -> local
scattering -> memory update and integer-position feedback -> next divisibility readout.
Existence of a proper divisor is a derived observable, not an
additional primality input. No prime table, GPF schedule, per-prime period,
external scale, log-prime roof or zero data. This is a declared
autonomous symbolic deformation, not a proven Logistic/Henon conjugacy or conservative
geometric lift. Stronger naturalness OPEN. Classical symplectic base, mapping torus
and positive classical roof NOT APPLICABLE; T3 operator/trace NOT SUPPLIED.

## 7. Fast gate and precommitted ownership controls

First establish the complete owner and all-point IMAGE. Then ask whether
requiring an actual finite history to return the ENTIRE source forces
its finite-write cylinder-mass ledger, and hence return clock, to cancel.
This is OPEN, not an assumed answer. If it excludes all
positive primitive times, stop target promotion before any general cycle census.
Do not change bit weights, choose a field tail or add a roof.

Root adds these finite ownership tests BEFORE freeze, supplementing the original
author's quick question without changing the object. Let q_0=(2,2),
q_1=(2,3), q_2=(1,3), q_3=(1,2), initial direction e=(1,0).
For main and MEMORY-WRITE-OFF use ALL fields with bits (0,1,1,1)
at (q_0,q_1,q_2,q_3), every other bit arbitrary. Test the proposed
four moves q_0->q_1->q_2->q_3->q_0, including actual directions, COMPLETE
final field, clock and full return status. For ARITHMETIC-OFF use
its OWN input family with bits (1,1,1,1) there, arbitrary elsewhere,
and test the same proposed path. TURN-OFF requires its own actual
trajectory, not this prescribed word. First verify legality; position closure is
not a return claim. If a test gives genuine periodic sources,
record their full isotropy, every incoming object, all unvisited-field multiplicity
and height phase, without selecting a representative field. Otherwise retain the
actual nonclosing arrow and do not label its clock a return time.
Also retain both local hit-bit cases b=0,1 as own IMAGE controls.

Generic exact full-source isotropy/phase rules are allowed, but unknown realization
or multiplicity outside these tests stays OPEN after a decisive fast gate.
Root owns all files except evidence/independent-review.md. Reviewer reads ONLY
this original card, personally derives main+ALL controls, sends metadata-only ALL
RAW READY and holds ALL mathematical output until root's first-paper lock
and explicit RAW RELEASE. ALL raw through FINAL precedes separate PAPER
UNLOCK, manuscript synthesis and adverse audit. Same-runtime/shared-history ARS three
checkpoints are NOT_CALIBRATED internal scrutiny, not external peer review or
independent-error evidence. No auxiliary, scientific numerics or external search in review.

## 8. Source provenance and authority

Root read the complete237-line328 frontier containing this proposal and later
source-author QA. The author read217 original1–73/101, not EOF;
headings1,9,38,74,84 exposed outcome TITLE84, not body. Card103
only heading1 and total11, no body/EOF and no adequate collision
definition. No old paper/review, current327/328 science/scout/peer, web,
calculation, write or auxiliary entered original delivery. Later limited QA read
ONLY then-328-frontier89–215, not EOF; total224 was ROOT metadata.
It confirmed faithful rules and access boundaries, no new mathematics. Root
has not independently reopened217/103. This definition distinction from fixed-n
cover scattering is not a nonconjugacy or global novelty theorem. Shared
history remains; earlier factor/coefficient NONE is only a definition-level screen.

T0--T3 are owner labels, formal UNASSIGNED; B NOT INVOKED.
Markdown only; no PDF/LaTeX, publication/upload or Git staging/commit.
Positive304, partial-positive320 and older packages unchanged;241/242 paused;
programme goal active. Preserve the original card prefix and scoped findings.

## Appended outcome — original173 lines above unchanged

Candidate ID: `ANG-20260920-MRF01`.
Status: `OWNED ROTOR CLOCK; ALL RETURN TIMES ZERO — STOP / FORK`.
Portfolio decision: **stop / fork**. Original measure/rule/source unchanged.

The complete moving-field map is a global homeomorphism with the prescribed
unique inverse and exact source/target cylinder partitions. All integer boundaries
and all rotor fields remain. Its fixed product measure is sigma-finite,
full-support and nonatomic; every-Borel inverse IMAGE gives the frozen version
j2 at old bit0 and j1/2 at old bit1. The
signed step clock is -log2/+log2, not a positive roof. Main
mu is nonsingular but not conserved; declared design is not canonical A0.

Every finite-history clock sum is its FINITE relative field-weight difference,
with all repeated writes telescoped site by site. Every actual arrow
has c=D(eta_source,eta_range), so the ENTIRE time group of EVERY
source is H0. There is no positive primitive time anywhere. This
is not a main no-source-period theorem or a numerical search result.

Full source isotropy/kernel is qZ at actual least-period-q states, otherwise0.
Bijectivity retains exactly the complete bilateral base orbit, with no extra
preperiodic ancestors. All real phases are h plus a finite relative-
field offset on the SAME actual base orbit. No global infinite
field energy, Borel transversal or collapse of finite-difference fields is presumed.

Main's frozen square has S4=log4 and closes particle position/direction,
but flips the four hit bits: it is NOT a full
source return. Arithmetic-off independently has its own nonclosing square S4=log16.
Memory-write-off has J1/c0 globally and genuine least-period4 square sources,
one four-state orbit per full exterior field: continuum many distinct zero-time
packets, each null, while the whole four-phase family has mass2/81.
Turn-off has no source period anywhere. Every control owns its inverse,
IMAGE, source/kernel and entire incoming/phase ledger. Neither a nonclosing
clock nor a control source cycle becomes a main positive primitive.

T0 / declared owned T1 established; stronger naturalness OPEN. T2 positive-
time target FAILS; T3 NOT SUPPLIED / NOT PURSUED. Classical
A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
Main/arithmetic-off source-period realization outside frozen tests and geometric realization
remain OPEN. No general census or revised weight/roof after this gate.

See the [paper](paper.md), [ledger](claim-ledger.md), [evidence](evidence/README.md),
[review](evidence/independent-review.md) and [frontier](evidence/scout-record.md).
A complete first-order divisibility-exchange geometric-feedback tuple is pending, without
next ID/freeze/audit or transferred result. Positive304, partial-positive320 and
older packages unchanged;241/242 paused; programme goal active. Markdown only.
