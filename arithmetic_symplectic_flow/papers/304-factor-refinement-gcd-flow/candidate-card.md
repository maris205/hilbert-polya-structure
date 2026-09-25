# Frozen candidate — finite factor refinement and gcd coalescence

Candidate ID: `ANG-20260920-FGC01`.
Paper ID: `304-factor-refinement-gcd-flow`. Date: 2026-09-20.
Version: 1. Initial status: `OPEN — FULL WORD BASINS, REAL IMAGE CLOCK AND PRIMITIVE PACKETS`.

## 1. Complete arithmetic source and full real fibres

Let W be ALL finite ordered words of positive integers, including
the empty word, every unit entry, composite entry, repeated factor
and every order. Words are literal tuples, not products or unordered
factorizations. Give W the discrete topology. In the divisibility
order define a cover atom p by p>1 and no 1<d<p dividing p.
For n>=2 let fct(n) be the complete ASCENDING word of these
atoms with product n, retaining every multiplicity. Set fct(1)=empty.
Prove existence/uniqueness from integer arithmetic; do not input
a prime table or regard factorization cost as physical time.

For each nonempty w=(a_1,...,a_k), define the actual next word

    k=1: C(w)=fct(a_1),
    k>=2: C(w)=(gcd(a_1,a_2),a_3,...,a_k).

This length-dependent composition law is a declared design. No
separate accepted-set bit, terminal completion or free rewrite is
added. Empty has no forward step. In particular (1)->empty,
and a gcd equal to 1 remains an entry rather than being erased.

The ENTIRE carrier is Y=coproduct_(w in W) {w} x R with usual
real topology in each fibre. Mu is counting over word roots times
Lebesgue, density one on EVERY fibre. No finite probability or
T-invariance is assumed. On precisely the nonempty root fibres set

    T(w,x)=(C(w),x/a_1).

All real x, including zero and both signs, remain. The empty real
fibre is terminal, not removed or given a loop. Source C has no
real-coordinate feedback; the first-letter transport is a declared
geometric design, not a derived Hamiltonian or clock formula.

## 2. All inverse branches and actual measured time

The proposed inverse families at target (v,y) are:

    for every n>=1 with fct(n)=v:
        I_n(v,y)=((n),n*y), y in R;
    for nonempty v=(g,tail), every a,b>=1 with gcd(a,b)=g:
        I_(a,b)(v,y)=((a,b,tail),a*y), y in R.

Keep all pairs and both families whenever their targets coincide.
Distinct predecessors are not merged by gcd or product. The branch
n=1 enters the empty terminal; retain it. Verify every domain,
completeness, local inverse, full image and topological property.
Neither branch labels nor all abstract split/merge moves become
extra arrows beyond this exact deterministic partial map.

Use the FULL retained-lag partial-tail groupoid

    G={(z,m-n,z'):T^m z=T^n z',m,n>=0}, source z', range z,

with all iterates actually defined. Topology uses actual finite
branch pairs on common open terminal domains and interval refinements.
Keep lag, not a free path group or germ quotient. Include every
transient, terminal and null fixed point. Prove the full owner.

For each actual local inverse theta derive the Borel IMAGE factor
from THIS counting-Lebesgue measure:

    mu(theta E)=integral_E J_theta dmu,     c=-log J_theta.

Inverse direction is target -> predecessor. No J or log-slope
formula is assumed or inherited. Derive all branch-pair factors,
presentation independence and additivity using only valid histories.
Use the unique continuous all-point version determined by full
support, not a freely chosen value on zero-seed returning states.

The extension objects are ALL Y x R; arrows shift the last
coordinate by c and physical time translates it by every real t.
Prove jointly continuous two-sided complete time. No extra roof,
algorithm runtime, conull replacement or chosen return section.
Coarse Hausdorffness and embedded-circle statements remain OPEN.

## 3. Exact lineage and ALL-state packet audit

The [prior-work](../../docs/prior_work/README.md) interface is proper-
divisor / cover-atom admissibility -> full finite factor words ->
actual factor refinement and common-divisor coalescence -> the same
measured real action. Specify what is retained or replaced. This
is not a direct prime-subshift input or the algebraic I/I^2 quotient:
all composite and unit word states remain. It is an ANG symbolic
deformation, NOT a Logistic/Henon conjugacy or symplectic lift.

After owner and clock, determine the full forward word behaviour
for EVERY finite word, including empty, all units, mixed factors,
repetitions and arbitrary orders. Then classify ALL periodic and
eventually periodic FULL states (w,x), ALL source isotropy groups,
H_z=c(G_z^z), extension fixed-object isotropy and actual packet
equivalence. No zero-seed or prime-word ansatz may replace that
classification. Test whether finite preimages or other word lengths
merge distinct recurrent cores or multiply a packet's count.

A positive primitive requires H_z=T_z Z with least T_z>0.
Its r-fold repetition traverses the SAME packet with time r*T_z.
Do not infer repetition from equal numerical lengths or interpret
prime powers in a source label as flow repetition without proof.
Retain nonreturning real states even when their roots recur.

A failed owner or decisive extra/missing primitive stops target
promotion. A positive full packet result is retained as an owner-
level theorem, NOT automatically natural A0. Finish the controls
below either way. No trace, zeta, determinant, operator, quantization
or T3 is supplied by this bounded source/clock/packet contract.

## 4. Independently owned adverse and robustness controls

FACTOR-OFF: replace only the singleton rule by C_0((n))=(n)
for EVERY n>=1. Keep gcd coalescence on longer words, the full
carrier, empty terminal, real transport x/a_1 and measure. Derive
its OWN inverse IMAGE law and full state/time/packet classification.
Do not delete composite or unit singleton roots.

UNIT-TRANSPORT: keep the exact main C/domain and full carrier,
but transport the real seed identically. Derive its OWN IMAGE law,
all time groups and source/extension isotropy on ALL states. A
zero clock is not a license to erase nontrivial source isotropy.

RADIAL-WEIGHT: keep the ENTIRE main T but change measure on
EVERY real fibre to |x| dx, with the same root normalization.
Prove full support/local finiteness and its OWN Borel IMAGE law,
continuous version at x=0 and complete return-time ledger. This
is a different measured owner, not a retiming of the main result.
Distinguish failure of translation invariance of this comparator
from ambiguity of an already frozen Lebesgue clock.

ORDER: replace ascending fct by descending fct, preserving all
factor multiplicities and every other rule. Derive its own branch
laws and decide whether complete root basins/primitive ledger change.
This checks ordering robustness, not arbitrary-alphabet universality.

Explicitly report what these controls do and do not establish about
factorization macro-operations, length-based scheduling, choice of
gcd, first-letter real transport and measure naturalness. Do not
claim arbitrary accepted-set encodability without an actual defined
comparator preserving the alleged source constraints. A prime-only
ledger alone is not a naturalness theorem or formal Route pass.

## 5. Provenance, review and authority

Definition-only input: [303 scout record](../303-polynomial-quotient-deletion-flow/evidence/scout-record.md),
SHA-256 `a6e6f815f79baea9634879334e547fbaabfb948b4ba8a78aad67703ee1b505e1`.
Root read it before freeze. Its narrow comparisons with
[298](../298-subtract-factor-word-flow/candidate-card.md),
[294](../294-gcd-product-residue-flow/candidate-card.md) and
[193](../193-indecomposable-radial-quotient/candidate-card.md) distinguish
infinite subtract-prefix words, two-root residue feedback and a
direct indecomposable cone quotient. No old theorem, clock, source
lock or Route result transfers. No global novelty claim.

No scientific numerics, cutoff, precision parameter, prime/zero data
or external literature campaign is planned. T0--T3 are broadened
owner labels; classical A0/A1/A2 NOT APPLICABLE; formal coordinates
UNASSIGNED; Route B NOT INVOKED. Strong source/geometry naturalness
OPEN. Root owns all files except evidence/independent-review.md.
ARS raw-card, manuscript and adverse checkpoints use inherited-model/
shared-context internal review, not peer review or independent-error
evidence. Old packages/mirrors unchanged; 241/242 paused; goal active.
Markdown only; no PDF/LaTeX, staging, commit, upload or publication.

## 6. Appended outcome — original definition above unchanged

Candidate ID: `ANG-20260920-FGC01`.
Status: `ADVANCE — FULL SOURCE/CLOCK/PRIME-PACKET THEOREM; NATURALNESS OPEN`.
The original 167-line prefix remains byte-preserved, SHA-256
`bc61a77df8ff6f0ac216bebc55a0e12b65532889a36f8e4f092c36ca715fdeb4`.
This appendix reports results, not a new source or changed measure.

The [full paper](paper.md) establishes both inverse families, full
LCH etale retained-lag owner, own Borel IMAGE factor a_1 and complete
continuous real time. Every nonempty word reaches singleton p iff
its total gcd is p^e, e>=1; otherwise it reaches empty. ONLY
((p),0) are periodic full states. Their entire zero-seed basins
have source isotropy Z and H=(log p)Z; all other states have
trivial source isotropy/H. Extension fixed-object isotropy is trivial
everywhere. Each prime-reaching basin is one actual packet, distinct
from every other prime's basin: the complete positive primitive
ledger is ONE packet per prime, least time log p, repeats r log p.
No full carrier state or predecessor was removed.

FACTOR-OFF has one positive packet per integer >1 and a zero-time
recurrent unit family. UNIT-TRANSPORT has all H=0 and retains
source/extension Z on prime-reaching basins at EVERY seed.
RADIAL-WEIGHT owns the same packet identities at times 2 log p;
it fails additive translation invariance and does not make the
fixed Lebesgue clock ambiguous. ORDER preserves the entire packet
ledger; no equality of transient orbit relations is asserted.

T0 and complete T2 established; T1 is a scoped engineering advance,
with stronger naturalness OPEN. Scheduling, factorization macro-steps,
gcd, passive real transport and measure geometry remain designs.
T3 NOT PURSUED; classical A0/A1/A2 NOT APPLICABLE; formal coordinates
UNASSIGNED; Route B NOT INVOKED. Portfolio: **advance scoped theorem;
stop natural-A0 promotion; fork source/geometric justification**.

See [claim ledger](claim-ledger.md), [evidence](evidence/README.md),
[internal review](evidence/independent-review.md), [package index](README.md)
and [source/frontier record](evidence/scout-record.md). The separate
future real–profinite definition has no ID, audit or result here.
Same-object ledger intact; old packages/mirrors unchanged; 241/242
paused; programme goal active. Markdown only; no publication/commit.
