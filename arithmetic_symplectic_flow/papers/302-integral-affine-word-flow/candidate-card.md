# Frozen candidate — finite integral-affine word refactorization

Candidate ID: `ANG-20260920-IAW01`.
Paper ID: `302-integral-affine-word-flow`. Date: 2026-09-20.
Version: 1. Initial status: `OPEN — INTEGRAL WORD OWNER, IMAGE ORIENTATION AND FULL SINGLETON RETURNS`.

## 1. All words, exact partial action and proposed inverse

A letter is f(t)=a*t+b with a>=1 and b in Z. Let W contain
ALL finite ordered words of letters, including the empty word.
Words are literal ordered tuples, not cyclic classes or affine maps
identified by their total product. Retain every unit slope and
negative translation. The carrier is Y=coproduct_(w in W) {w} x R,
discrete word roots and ordinary real fibres. On every fibre use
the SAME Lebesgue measure, with counting over roots, no root weight.

Composition is (f circ g)(t)=f(g(t)). For nonempty w=(f_1,...,f_k),
write f_1(t)=a*t+b and P=f_2 circ ... circ f_k=A*t+B.
For k=1 set P=id, A=1,B=0. Domain D is precisely those nonempty
root fibres with A dividing b+(a-1)B. On D define

    beta=(b+(a-1)B)/A,     g(t)=a*t+beta,
    H(w)=(f_2,...,f_k,g),  T(w,x)=(H(w),(x-b)/a).

Keep the empty fibre and every integrality-failing fibre as terminal
objects, with no forward step or added loop. Retain their actual
incoming arrows if any. At k=1 use the exact formula, without any
prime exception. For a=1 the domain is A divides b, last letter
is t+b/A and seed becomes x-b. No slope, word length or seed is
deleted to enforce a target. The intended P circ g=f_1 circ P
relation, arithmetic closure and action ownership are obligations.

For a nonempty target v=(h_1,...,h_k), write last letter
h_k(t)=a*t+beta and Q=h_1 circ ... circ h_(k-1)=A*t+B,
with Q=id when k=1. The proposed predecessor is

    b=A*beta-(a-1)B,      f(t)=a*t+b,
    I(v,z)=((f,h_1,...,h_(k-1)), a*z+b), z in R.

Its proposed domain is EVERY nonempty target fibre, with no inverse
at the empty word. Prove all inverse-domain, uniqueness and image
claims, and whether T is injective or surjective onto that portion.
Keep whole terminal fibres even if they lie in the image. Do not
confuse partial-map domain with its range. The pair word
(t+1,2t) is a frozen integrality-failure boundary test; assess its
actual predecessors rather than declaring it isolated by convention.

## 2. Full owner, actual IMAGE clock and time

Use ONLY the full retained-lag tail groupoid of this partial T:

    G_T={(z,m-n,z'): T^m z=T^n z', m,n>=0},

where every iterate must be defined, source z', range z. Use all
actual finite branch pairs over common open terminal domains and
all interval refinements. Retain lag, not free affine or Hurwitz
labels. No split/merge, arbitrary translation, cyclic quotient,
selected stabilizer or germ quotient is added. Prove topology,
composition and all-point owner with terminals included.

Use the measure above with the IMAGE convention

    mu(theta E)=integral_E J_theta dmu,    c=-log J_theta.

For I the direction is target to predecessor. Derive its factor;
do NOT import a profinite Haar 1/a rule into the real Lebesgue
fibre. Neither J_I nor a sign of log a is presumed here.
Derive every branch-pair factor and verify presentation independence
and additivity, aligning only already-defined common histories.
Use a proved full-support continuous all-point version, retaining
null fixed seeds. No arbitrary assignment at a recurrent point.

Use ALL extension objects Y x R and arrows (z',s)->(z,s+c(g)).
Physical time is s->s+t for all real t. Prove joint continuity
and two-sided completeness; no independent roof or counting runtime.
Coarse Hausdorffness and embedded-circle language remain OPEN.

For every tested full state compute G_z^z, its full time group
H_z=c(G_z^z), and extension fixed-object isotropy ker c. A positive
primitive requires H_z=T_z Z with a least T_z>0, irrespective of
the sign of a selected generating arrow. Packet identity is actual
full tail equivalence and time phase, not equal periods, affine
conjugacy, equal total products or a selected representative seed.
Repetition traverses the SAME packet ell times.

## 3. Exact lineage and decisive gates

The [prior-work](../../docs/prior_work/README.md) interface to verify is,
for 1<d<a and f(t)=a*t+b,

    d|a iff f=(t->d*t+b) circ (t->(a/d)*t)
             with integral slopes.

The proposal deforms divisor-symbolic factor admissibility into
integral affine-word refactorization. Prove its actual relation;
split symbols express lineage but are NOT automatically arrows.
Strong naturalness and sufficiency of this replacement remain OPEN.
This is the ANG track, not a Logistic/Henon conjugacy or classical
symplectic lift. No prime table, witness-selected return component,
per-prime parameter, von Mangoldt or zero data is supplied.

After owner and clock, audit ALL source periods and time groups
on ALL single-letter roots f(t)=a*t+b, a>=1,b in Z, every real
seed. Include identity, nonzero translations, prime/composite slopes,
all translations b and null fixed points. Test whether other word
lengths or inverse excursions can identify distinct tested packets.
Retain a=2 and a=4 as prime/composite controls without selecting b.

One excess prime packet or composite primitive decisively STOPS
target promotion. Afterward finish only the following frozen
boundaries/controls; no all-word period census, trace, determinant,
measure fit or deletion of singleton/composite roots is authorized.

Bounded length-two ownership test: literal word ((2,0),(3,0))
and its actual word successors, ALL real seeds. Determine its
least source return and full time group, not just total slope.
This one precommitted mixed-slope test is not an all-two-letter
classification or a reason to postpone a singleton stop.
Keep the empty/failing-domain boundary and actual incoming arrows.

## 4. Changed-source controls with their own measures

REFACTOR-OFF: for every nonempty word use plain cyclic rotation
H_0(f_1,...,f_k)=(f_2,...,f_k,f_1), without the integrality
domain or changed last translation. Keep T_0(w,x)=(H_0(w),(x-b)/a)
and the same full Y/counting-Lebesgue measure. Empty word remains
terminal. Derive its OWN inverse IMAGE law; test only ALL
single-letter roots and the same frozen mixed-slope two-letter word.

UNIT-TRANSPORT: keep the main partial root action H and its domain,
but set T_u(w,x)=(H(w),x). Keep full Y and the same measure.
Derive its OWN branch law and ALL time groups. Classify source/
extension isotropy only for all singleton and terminal states, plus
the frozen mixed-slope two-letter word. Do not attach the main
affine slope clock to this changed identity fibre action.

## 5. Provenance, limits and authority

Definition-only input: [301 scout record](../301-sublattice-intersection-digit-flow/evidence/scout-record.md),
SHA-256 `6a6dbada5ea261d6cd46604e79b096bb7612adfb38de0dbba5e8cbe023edeb17`.
Root read it before freeze, along with [225's word-port card](../225-euclid-edge-scattering/candidate-card.md)
and [275's full rational-affine Haar card](../275-rational-affine-residue-flow/candidate-card.md).
Those sources differ in actual arrows, real/profinite carrier and
measure; their clocks or returns do not transfer. Bounded comparison
is not novelty certification. Definition-stage awareness informed
the decisive singleton test; no blind candidate-selection claim.

All claims are exact-proof obligations; no scientific computation,
cutoff, precision parameter, external literature campaign or new
analytic object is planned. T0--T3 are broadened owner labels only.
Classical A0/A1/A2 NOT APPLICABLE; formal coordinates UNASSIGNED;
Route B NOT INVOKED. T3 / Hamiltonian / quantum NOT SUPPLIED.
Root owns integration and all files except reviewer-owned
evidence/independent-review.md. ARS raw-card, manuscript and final
adverse checkpoints use inherited-model/shared-context internal
review, not peer review or independent-error evidence. Old packages
and mirrors unchanged; 241/242 paused; programme goal active.
Markdown only; no PDF/LaTeX, staging, commit, upload or publication.

## 6. Appended outcome — original definition unchanged

Status: `OWNED REAL IMAGE CLOCK; INFINITE SINGLETON PACKET MULTIPLICITY — STOP / FORK`.
The original preceding 158 lines remain byte-preserved, SHA-256
`90e4085eee115f406f050eb47540aabfe9179556c15f61edd9ee70eaabda12dc`.

The [paper](paper.md) proves exact integral refactorization and a
unique inverse on EVERY nonempty target, including terminal roots.
T:D->Y_nonempty is a homeomorphism. The empty root has no incoming
step; the frozen failed root (t+1,2t) does, from (2t-1,t+1).
Real counting-Lebesgue inverse IMAGE is a and its clock is -log a.
The full partial-tail cocycle and complete continuous real extension
are owned on all points, including null fixed seeds.

ALL positive singleton returns at a>=2 occur at -b/(a-1).
Each literal letter has one primitive packet with H=(log a)Z,
source isotropy Z and zero extension fixed-object isotropy. EVERY
b in Z gives a different packet; full arrows preserve each
singleton root and word length. Therefore a=2 already has infinite
prime-time multiplicity and a=4 has separate composite primitives.
Unit identities have source/extension isotropy Z but H=0 at all
seeds; nonzero unit translations have no returns. Other a>1 seeds
have no periodic/eventual returns.

The frozen (2t,3t) pair has only its zero-seed two-phase packet,
with least source period 2 and time log 6, distinct from a
singleton 6t packet. Empty/terminal states have trivial isotropy;
actual incoming arrows are retained. REFACTOR-OFF owns its clock
and keeps both tested surplus families. UNIT-TRANSPORT owns IMAGE
1, all H=0, with singleton isotropy Z and mixed-pair isotropy 2Z
at EVERY real seed; terminal isotropy remains trivial.

Portfolio: **stop target promotion / fork**. Other multiword
returns, coarse topology and stronger naturalness OPEN / NOT
PURSUED. T0/scoped measured T1/tested-family T2 established; T3
NOT SUPPLIED / NOT PURSUED. Classical A0/A1/A2 NOT APPLICABLE;
formal coordinates UNASSIGNED; Route B NOT INVOKED.
The same-object ledger is intact. Separate definition gaps are
not extra candidates or impossibility results. See the
[claim ledger](claim-ledger.md) and [evidence](evidence/README.md).
