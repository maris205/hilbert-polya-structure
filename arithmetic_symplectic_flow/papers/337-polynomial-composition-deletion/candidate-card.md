# Frozen candidate — right-composition quotient and factor deletion

Candidate ID: `ANG-20260920-PCD01`.
Paper ID: `337-polynomial-composition-deletion`. Date: 2026-09-20.
Version:1. Initial status: `OPEN — FULL POLYNOMIAL WORD AND COMPOSITION CLOCK`.

## 1. Entire word carrier and right-composition procedure

Let A=Z[X], X formal, discrete alphabet, and Y=A^(N_0) with full
product topology/Borel structure. Retain ALL zero polynomials, signed constants, degrees,
units and infinite tails. Finite words are not objects. No restriction to
linear, monic, irreducible, prime-accepted or selected recurrent words.

Define R_Q(P), an integral RIGHT-composition quotient procedure, exactly as follows.

1. If Q is constant, including0,+/-1, FAIL.
2. Otherwise set m=deg(Q)>=1, R=P and V=0.
3. While R!=0 and deg(R)>=m: if deg(R) is not a multiple
   of m, FAIL. Set k=deg(R)/m and c=lc(R)/lc(Q)^k. If
   c is not an integer, FAIL. Otherwise set V:=V+c X^k
   and R:=R-c Q^k and repeat.
4. After exit, if R is nonconstant, FAIL. Otherwise set V:=V+R.
5. Verify P=V composed with Q; FAIL if not, output V if so.

P=0 and constant P use the same final constant-remainder rule; no selected
quotient is supplied. Termination, correspondence with ALL integral right-composition factors,
uniqueness and boundary correctness must be proved, not assumed from the algorithm.

## 2. Actual map, terminal states and every inverse

For FULL source(P,Q,U,eta), where eta is the infinite tail, ONLY if
R_Q(P) succeeds with V, define

    B=U composed with Q;
    T(P,Q,U,eta)=(B,V,eta).

Delete the actual old factor Q; the actual quotient is the new
second letter and the full tail stays. Every failed source is terminal
with T^0 and all actual incoming, no reset, absorbing loop or deletion
of the object. Target failure at its NEXT step does not remove the target.

For EVERY nonconstant Q and EVERY U in A specify

    E_(Q,U)={(B,V,eta):B=U composed with Q,
                      R_Q(V composed with Q) succeeds and returns V};
    h_(Q,U)(B,V,eta)=(V composed with Q,Q,U,eta).

Retain ALL admissible labels and decompositions; never choose a representative factor.
If labels give the same actual predecessor, it is one predecessor, not
extra free-label isotropy. Equivalently use all admissible source three-letter cylinders.
Prove exhaustive image, both inverse identities, enumeration equivalence and all boundaries.

## 3. Explicit design probability and all-point IMAGE

Re-declare the following alphabet law, numerically equal to303's but inheriting
NO normalization, IMAGE, clock or return theorem:

    rho(0)=1/2;
    rho(a)=1/(4 abs(a)(abs(a)+1)) for a in Z nonzero;
    sigma(a)=1/(2 abs(a)(abs(a)+1)) for a in Z nonzero;
    lambda_d=1/((d+1)(d+2)), d>=0;
    pi(0)=1/2.

For nonzero P=sum_(i=0)^d a_i X^i, a_d!=0, prescribe

    pi(P)=(1/2) lambda_d sigma(a_d) product_(0<=i<d) rho(a_i);
    mu=pi^(N_0).

Normalization, existence, support and atomic status belong to this audit. No
canonical or invariant measure is presumed. For the actual inverse from target
cylinder[B,V] to admissible source cylinder[P,Q,U] prescribe on its WHOLE domain

    j_theta=pi(P)pi(Q)pi(U)/(pi(B)pi(V)).

This is a full-point version, including every zero-measure infinite word. No
value is precomputed. Prove positivity/finite values and mu(theta E)=integral_E
j_theta dmu for EVERY Borel E in the actual target cylinder,
plus inverse and legal finite-composition versions. Cylinder ratios alone do not
replace that proof. Do not modify null-periodic values by a.e. equivalence.

## 4. Retained-lag clock, all incoming and whole packets

Define G={(z,m-n,w):T^m z=T^n w,m,n>=0}, requiring BOTH full
histories legal, source w, range z, inherited Borel structure in Y x Z
x Y. Equal actual triples give one arrow. No free composition-word,
arbitrary prefix-swap or unrelated shift arrow is inserted.

For every legal source and ACTUAL successor inverse B_z:Tz->z set

    kappa(z)=-log j_(B_z)(Tz);
    S_m(z)=sum_(0<=i<m) kappa(T^i z), S_0=0;
    c(z,m-n,w)=S_m(z)-S_n(w).

No nonempty illegal terminal sum. Descent, cocycle and same-owner IMAGE meaning
are audit obligations. Keep ALL Y x R_h, arrows(w,h)->(z,h+c),
and time translation h->h+t. No unit roof, algorithm-cost clock or manually
specified log p. No prime table, zero data, Mangoldt or per-prime parameter.

Retain ENTIRE source isotropy, clock kernel, extension fixed-object isotropy, every
incoming history, terminal/nonperiodic word and height phase. Positive primitive requires
ENTIRE H_z=c(G_z^z)=LZ with least L>0; repetitions belong to the
SAME whole packet. Equal degree, weight, composition value or time never
merges classes. Local compactness, regular coarse quotient and embedded circles are
not pre-supplied. Classical symplectic form/base/roof/suspension and A0/A1/A2 NOT
APPLICABLE; T0–T3 owner labels only; T3 NOT SUPPLIED; formal UNASSIGNED;
B NOT INVOKED. No later Hamiltonian/contact/quantum/trace/zeta/operator owner supplied.

## 5. Three controls with separate complete owners

Each keeps full Y,mu but owns its map, source/target domains, full-point
IMAGE, retained lag/clock/kernel and entire incoming/packet/phase convention.

A — EXACT-MULTIPLICATION: if Q!=0 and P=VQ with V in Z[X],
set T_A(P,Q,U,eta)=(UQ,V,eta). For operational clarity, ordinary Q[X]
long division succeeds here ONLY if remainder0 and every coefficient of V
is integral. All other sources remain terminal, including Q=0. Nonzero constant
Q is NOT automatically terminal as it is in main.

Enumerate ALL Q!=0,U with B=UQ and source(VQ,Q,U,eta) passing its
OWN exact-division rule; inverse returns(VQ,Q,U,eta). No main composition permission.

B — RECONSTRUCTION-ORDER-REVERSED: keep main quotient permission, but

    T_B(P,Q,U,eta)=(Q composed with U,V,eta).

Enumerate ALL nonconstant Q,U satisfying B=Q composed with U and
R_Q(V composed with Q)=V; return(V composed with Q,Q,U,eta).
Do NOT assume U uniquely determined by B,Q; keep all actual predecessors.

C — NO-DELETION: keep main permission but

    T_C(P,Q,U,eta)=(U composed with Q,Q,V,eta).

For target(B,Q,V,eta), enumerate all U with Q nonconstant, B=U composed
with Q and R_Q(V composed with Q)=V; return(V composed with Q,Q,U,eta).
The middle Q is ACTUALLY retained, not a freely replaced inverse label.

A/B prescribe their OWN three-letter-source/two-letter-target mass ratios; C its
OWN three-letter-source/three-letter-target ratio, on whole actual target cylinders.
No main/control IMAGE, inverse or period conclusion transfers without its proof.

## 6. Exact lineage and prebounded full-fixed-word gate

On the integer-linear sector P=nX,Q=dX,U=uX,d!=0, the proposed
right-composition permission realizes d divides n and the actual reassembly and
quotient enter the successor. Verify this interface, rather than adding a primality
flag. Proper-divisor scope n>=2,1<d<n is an observable, not the carrier.

Proposed arrow: divisor-symbolic integral-factor permission -> actual current polynomial
RIGHT-composition factor test -> reassembly/quotient/deletion -> new source admissibility.
All constant, zero, unit and higher-degree states remain. Right direction, old-
factor deletion, prefix lengths and the alphabet law are explicit design choices.
Strong naturalness/prime meaning and arbitrary countable-algebra/weight risks remain OPEN.
This is a broadened symbolic replacement, not a completed Logistic/Henon geometric lift.

First prove quotient procedure, ALL inverse domains and full-point every-Borel IMAGE.
Then inspect ALL FIXED FULL WORDS of main and ALL controls, not
preselected constant/linear tails. Retain complete inverse excursions, source/kernel,
packet identity and multiplicity. A decisive surplus unit/composite packet, wrong
native prime time or multiplicity stops target advancement. No deletion of tails,
measure tuning, equal-time quotient or parameter adjustment. If undecided, bounded
OPEN and stop/fork, not a high-period census or T3 campaign.

Frozen one-step checks: all-zero word; all-X word; first two letters(nX,dX)
with(n,d)=(6,2),(5,2),(0,1),(1,0), keeping ALL U,eta; and
(P,Q,U)=(X^2+X,X^2,X+1), with arbitrary infinite tail. No test result
is precomputed. Root clarifies before freeze: direct inverse/one-step identities may
describe full incoming/source/kernel/phase; unknown higher-period realizations stay OPEN.
Do not replace these ledgers by a fixed representative or chosen inverse path.

## 7. Provenance and staged first-lock review

Root read336's COMPLETE223-line frontier, not303/302 cards or proofs. The
definition author previously participated in303. New reads were303 original1–121/202
and302 original1–120/199, neither EOF, with outcome TITLES165/160 exposed
by heading scans, not bodies. The shared303 full-word/product-law template
is acknowledged; replacing ordinary multiplication/remainder by right composition is a
displayed definition difference, not blind discovery or a global novelty/nonconjugacy claim.
No third card, current336/335 science/peer, old paper/review, web, scientific
calculation, auxiliary or write entered delivery. Later source-only QA read336
frontier26–207, NOT EOF, no extra files/headings/hash/metadata measurement, and
confirmed faithful transcription. Its name-only336 clock-result reference was new QA
metadata, not original input or a mathematical value/conclusion/proof.

Root's operational A-division spelling and full-ledger scope clarification are pre-freeze
wording, not changes to the declared action, measure or clock. Reviewer reads
ONLY this original card, personally derives main and ALL controls, sends metadata
ALL RAW READY and holds ALL mathematics. Root FIRST-paper hash lock AND
explicit RAW RELEASE precede every raw result; ALL RAW FINAL precedes separate
PAPER UNLOCK and manuscript/adverse review. Root owns all new package paths
except evidence/independent-review.md. No review auxiliary/web/scientific numerics. Shared
model/history NOT_CALIBRATED, not peer review or independent-error evidence. Markdown
only, no PDF/LaTeX/publication/upload/staging/commit, model or old-package changes.
241/242 paused; programme goal active. Preserve this complete original prefix.

## 8. Appended outcome — original194-line definition unchanged

Final status: `OWNED COMPOSITION CLOCK; ALL PRIMITIVES COMPOSITE — STOP / FORK`.
Read [paper](paper.md), [claim ledger](claim-ledger.md) and [evidence](evidence/README.md).

The quotient procedure terminates and succeeds EXACTLY on integral right factors,
with unique quotient for every nonconstant Q. Main/B own all source-checked
predecessors, countably infinitely many at EVERY target; A is onto with its
full exact-factor enumeration. C has image exactly its own legal D and
is an involution there; outside-D C terminals are isolated. Other owners'
terminal incoming are not deleted. Full-support nonatomic mu and EVERY-Borel,
full-cylinder IMAGE versions, finite legal compositions and retained-lag clock are proved.

Main's COMPLETE fixed words are(Q(Q),Q,Q,...), Q nonconstant. A's are
(Q^2,Q,Q,...), Q!=0. B's are(Q(Q),Q,U,U,...), with U=Q,
or the proved integral reflection U=b-Q where deg(Q)=m is even,
b=-2a_(m-1)/(m a_m) is integral and Q(b-X)=Q(X). No
other polynomial tail solutions exist. C's full fixed set is(U(Q),Q,U,eta),
Q nonconstant, arbitrary U and ENTIRE arbitrary tail; no constant-tail selection.

Every deletion fixed core owns its WHOLE countable infinite inverse basin, sourceZ,
H=LZ, zero source-clock/extension kernel, and phase h-S_r modulo L at
each ancestor. Main/A have L=-log pi(Q); B L=-log pi(U).
Different fixed cores remain different complete packets. Main/A/B fixed-basin unions
are null; C fixed cylinders have positive measure but each word is null.
C has H0 everywhere, source/kernelZ or2Z on its one/two-word legal
orbits,0 at isolated terminals, real phase h+sum_(i=0)^2 log pi(a_i).

The finite-history IMAGE identity proves that any actual least-d cycle for
main/A/B has ENTIRE primitive L=-sum_(i=2)^(d+1)log pi(a_i)>0;
transient ancestors have the SAME H and zero source-clock kernel. All alphabet
weights are reciprocal integers N(a)>=2; nonzero letters have composite N,
and all fixed deleted letters are nonzero. Thus EVERY positive primitive
is log of a composite integer: no log-prime primitive anywhere. This is
a direct identity/conditional period law, not a high-period realization census.

Positive examples include main's composition-unit log96, A's multiplication-unit log16,
and two distinct B reflection packets of length log384. Frozen one-step
tests keep all U/tails; all-X is NOT fixed for A and all-zero
is terminal, with incoming for deletion owners. No prime or zero data inserted.

Same-object ledger intact; strong naturalness and higher source-period realization OPEN.
T0/declared clock ownership established; prime-time target FAILS; T3 NOT SUPPLIED /
NOT PURSUED. Classical ASFS A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED;
B NOT INVOKED. Portfolio stop / fork, without density/tail/permission repair.
Next-definition screen is Pre-P0 NONE for an old-definition collision, not a
new frozen object or universal no-go. Earlier packages unchanged; goal active.
