# Full factor refinement and gcd dynamics own one log-prime packet per prime

Paper ID: `304-factor-refinement-gcd-flow`.
Candidate ID: `ANG-20260920-FGC01`. Date: 2026-09-20.
Status: `ADVANCE — FULL SOURCE/CLOCK/PRIME-PACKET THEOREM; NATURALNESS OPEN`.
Route state: broadened owner audit; classical A0/A1/A2 NOT APPLICABLE;
formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

All finite positive-integer words, including composite and unit entries
and the empty word, carry full real fibres. A singleton is replaced
by its complete factor word; a longer word coalesces its first
two entries by gcd. The first entry divides the real seed at each
step. The full partial-tail groupoid owns a counting-Lebesgue IMAGE
clock and complete continuous time. Every nonempty word either reaches
a singleton prime or terminates at the empty word. Full-state returns
occur precisely at zero seeds in the prime-reaching basins, giving
exactly one primitive time packet per prime, with least time log p
and all repeats retained. This is an all-state theorem, not a
selected-prime or selected-centre construction. Factor removal, identity
transport, radial reweighting and factor-order reversal distinguish
arithmetic selection, clock dependence and ordering robustness. The
source scheduling and geometric/measure choices remain declared designs;
the positive owner theorem does not establish natural A0 or a Route pass.

## 1. Exact identity and claim boundary

The [original card](candidate-card.md) freezes the entire construction
before this proof. The question is whether actual factor composition,
rather than an independent accepted-set scan switch, can coexist with
an owned clock and an intrinsic complete primitive ledger.

| Field | Same frozen owner | Scope |
| --- | --- | --- |
| Carrier | Discrete ALL finite ordered positive-integer words, each with full R | Empty, units, composites and both real signs retained |
| Source | Singleton complete ascending factor refinement; longer-word first-pair gcd coalescence | Autonomous arithmetic word law C |
| Full action | T(w,x)=(C(w),x/a_1) on nonempty words | Empty fibre retained as terminal |
| Measure | Counting roots times Lebesgue, density one on every fibre | Locally finite, not finite or T-invariant |
| Time owner | Full retained-lag groupoid, actual IMAGE cocycle, real extension | No roof or algorithm-runtime time |
| Packets | Full isotropy image and actual tail/time equivalence | Every positive primitive and repetition classified |
| Symplectic base / mapping torus / Hamiltonian/contact owner | NOT APPLICABLE / NOT SUPPLIED | No Logistic/Henon conjugacy asserted |
| Trace / zeta / determinant / operator / quantum owner | NOT SUPPLIED / NOT PURSUED | No T3 or formal Route credit |

The complete factorization operation, length-based schedule, gcd choice,
first-entry transport and Lebesgue structure are explicit designs.
No real-coordinate feedback into the word rule is present. Their
stronger arithmetic/geometric naturalness remains OPEN, not proved
by correctly counting the resulting packets.

## 2. Arithmetic construction and full local owner

### 2.1 Cover factors from divisibility

A cover atom p in the positive-integer divisibility order satisfies
p>1 and has no divisor strictly between 1 and p; these are
the ordinary primes. Factorization can be constructed without a
prime table: take the least divisor d>1 of n>1, divide by d,
and repeat on the smaller quotient. The least d must be a cover
atom, since a proper nonunit factor of d would be a smaller
divisor of n. The quotient decreases until it is one, so this
gives a finite atom factorization.

For uniqueness, a cover atom p has gcd(p,a)=1 whenever p does
not divide a. The Euclidean algorithm supplies Bezout coefficients;
multiplying their identity by b shows p|ab implies p|a or p|b.
Repeated application matches and cancels atoms in any two factorizations.
Sorting therefore gives a unique ascending word fct(n), with all
multiplicities retained. Set fct(1)=empty. This establishes the
arithmetic definition, not a constant-cost factorization claim.

Let W contain ALL finite ordered positive-integer words, empty included.
On w=(a_1,...,a_k) with k>=1 define

    k=1: C(w)=fct(a_1),
    k>=2: C(w)=(gcd(a_1,a_2),a_3,...,a_k).

The word (1) goes to empty; gcd=1 remains a literal entry.
There is no additional accept/reject bit or completion loop. For
Y=coproduct_w {w} x R define T(w,x)=(C(w),x/a_1) on
nonempty roots. Empty has no forward step at any real seed.

The exact [prior-work lineage](../../docs/prior_work/README.md) is
proper-divisor/cover admissibility -> full factor words -> factor
refinement and common-divisor coalescence -> the same measured action.
Arithmetic changes actual word length, entries and the next operation.
No composite word is removed by an indecomposable quotient, and
no separate prime subshift supplies the clock. This is a stated
ANG deformation, not a conservative geometric lift theorem.

### 2.2 Every inverse, including the empty target

For a singleton predecessor n with fct(n)=v, the inverse is

    I_n(v,y)=((n),n*y), y in R.

For nonempty target v=(g,tail), every a,b>=1 with gcd(a,b)=g
gives the inverse

    I_(a,b)(v,y)=((a,b,tail),a*y), y in R.

Substitution verifies both; any predecessor has either one letter
or at least two, so these exhaust all inverses. Different pairs
retain their different actual root words. Both families can share
a target without becoming one predecessor or free path labels.
Every nonempty target has a predecessor (g,g,tail); every empty
target has predecessor (1). Thus T maps its proper nonempty
domain ONTO Y, including terminals, and is a local homeomorphism
on every full real root fibre. It is not globally injective.

Y is a countable coproduct of real lines, hence locally compact,
Hausdorff and second countable. Its nonempty-root domain is clopen.
Mu, counting over roots times Lebesgue with density one on each,
is sigma-finite, locally finite and full support, with singleton
points of zero mass. A terminal has real incoming arrows but
no outgoing iterate; these are separate ownership facts.

## 3. Actual IMAGE law, full cocycle and real time

An inverse on a predecessor with first letter a_1 is y->a_1*y.
For EVERY Borel target set E, Lebesgue scaling gives

    mu(I(E))=a_1*mu(E),     J_I=a_1,     c(I)=-log a_1.

This is the inverse direction target -> predecessor. The forward
branch has factor 1/a_1 and clock +log a_1. Neither a roof
nor a profinite Haar inverse factor is substituted. Unit leading
entries give zero step clock but are not assigned return loops.

Retain the full partial-tail groupoid

    G={(z,m-n,w):T^m z=T^n w, m,n>=0},

source w, range z, with all iterates defined and lag retained.
All actual finite branch pairs on common open terminal domains,
with interval refinements, give local source/range homeomorphisms.
Their histories align for multiplication using only steps already
known to exist; no terminal future is invented. These charts give
a locally compact, Hausdorff, second-countable etale owner: compact
interval restrictions give local compactness, and range/source/lag
separate distinct triples. No free split/merge or germ quotient enters.

Let A_m(z) be the product of first entries along the actual m
steps from z, A_0=1. Inverse composition from a common terminal
state to z has IMAGE A_m(z). Consequently

    J_(z,m-n,w)=A_m(z)/A_n(w),
    c(z,m-n,w)=log A_n(w)-log A_m(z).

Two valid presentations of the same lag extend both histories
along an identical existing common tail; its factors cancel.
Alignment also proves additivity. Factors are locally constant on
root-history charts. Full support uniquely determines the continuous
all-point version from its almost-everywhere density, including the
zero-seed recurrent points. Their clocks are not independently assigned.

On all extension objects Y x R, use arrows
(w,s)->(z,s+c(g)). Translation (z,s)->(z,s+t) for every real
t is jointly continuous, two-sided complete and commutes with all
arrows. The etale orbit projection is open, so the quotient time
action is continuous in its quotient topology. Coarse Hausdorffness,
embedded classical circles and a mapping-torus realization are not
claimed by this bounded contract.

For every state z, define H_z=c(G_z^z). A positive primitive
packet requires H_z=T_z Z with least T_z>0. Extension fixed-
object isotropy is ker c on source isotropy, not H_z. Equal
numerical times do not identify different packets.

## 4. ALL word basins and ALL full-state returns

### 4.1 Exhaustive word dynamics

For nonempty w let g(w)=gcd(a_1,...,a_k). Its first k-1
coalescences reduce the word to the singleton (g(w)), since each
step lowers length by one and preserves the gcd of all entries.
This includes k=1 with zero preliminary steps.

If g=1, the next word is empty. If g is a cover atom p,
the singleton is fixed. Otherwise fct(g) has at least two atoms.
If all are the same p, then g=p^e and their successive gcds
reduce to (p). If at least two different atoms occur, their total
gcd is one, so coalescence reaches (1), then empty. Therefore:

    g(w)=p^e, p prime, e>=1: reaches (p) in finitely many steps;
    all other nonempty words: reaches empty in finitely many steps.

The empty root is already terminal. The ONLY periodic word roots
are the singleton atoms (p); there are no longer cycles hidden
in a factor-refinement/coalescence excursion. A root label p^e
is generally a transient, not a prime-power primitive orbit.

### 4.2 Real seeds and the complete isotropy table

For every valid j-step history,

    T^j(w,x)=(C^j(w),x/A_j(w)),    A_j(w)>0.

Suppose the root reaches (p) at step h. Thereafter the real
seed is (x/A_h)/p^r after r further steps. A nonzero x never
becomes zero and has no return under these strict scalings.
Thus the ONLY full periodic states are z_p=((p),0), each fixed.
The FULL eventually periodic locus is

    R_p={(w,0): w nonempty and g(w)=p^e for some e>=1},
    R=disjoint-union over primes p of R_p.

For z in R_p, every integer lag is represented by two sufficiently
late iterates at z_p, so G_z^z=Z. Common transient products cancel
from the cocycle, giving c(ell)=-ell log p. For any other full
state, a nonzero isotropy lag would give equality of two distinct
valid iterates and hence an eventual periodic state, which the
classification has excluded. This proves the all-state table:

| Full state | Source isotropy | Time group H | Extension fixed-object isotropy |
| --- | --- | --- | --- |
| z in R_p | Z | (log p)Z | 0 |
| Every other z, including nonzero real seeds and terminal basins | 0 | 0 | 0 |

In particular extension fixed-object isotropy is trivial everywhere.
Transient R_p points have source isotropy through eventual equality;
they are not falsely called periodic points of T itself.

### 4.3 Exactly one primitive packet per prime

Any two states of R_p have actual finite tails ending at the
SAME z_p, so an arrow relates them. The cocycle merely changes
the real time phase of that relation. All phases at z_p belong
to one time orbit with stabilizer (log p)Z. Thus R_p contributes
exactly ONE positive primitive packet, of least time log p.
Distinct p cores have different constant T-tails, so no full
arrow or inverse excursion merges their packets. Since R is the
entire nontrivial-isotropy locus, there are no other positive packets.

The r-fold repetition is the same packet's isotropy lag r and
has positive elapsed time r log p, using the appropriate arrow
orientation. For example a source word (p^e) reaches the p core;
it is not an extra primitive of time log(p^e), nor does its
finite root itinerary itself count as e traversals. Repetition
comes from the full cyclic time group, not the source label.

Zero seeds were selected by the solved return equation, not by
restriction of the carrier. All nonzero states, composite roots,
empty/unit fibres and null points remain. This proves the complete
abstract packet ledger of the frozen groupoid/time owner, not a
finite-dimensional symplectic closed-orbit theorem.

## 5. Independently owned controls

### FACTOR-OFF: arithmetic selection is substantive

Replace the singleton rule by C_0((n))=(n) for every n>=1.
Longer words still coalesce to (g(w)); empty remains terminal.
Inverses now consist of each singleton self-root inverse y->n*y
and the unchanged complete gcd-pair inverses. Empty has no incoming
branch in this comparator. Its OWN Lebesgue IMAGE law is a_1,
with the same valid-history derivation, not transferred packets.

Every nonempty word reaches the fixed singleton g. For g>1,
exactly x=0 gives eventual full returns: source isotropy Z,
H=(log g)Z and extension isotropy zero. There is one distinct
positive packet for EACH integer g>1, including composites.
For g=1, EVERY real seed eventually reaches an identity singleton;
source and extension isotropy are Z, but H=0. For g>1,x!=0
and for empty-root states both isotropies and H are trivial.
The actual factor refinement therefore removes composite primitives
and the recurrent unit family; it is not an inactive label.

### UNIT-TRANSPORT: source recurrence is not physical time

Keep main C but send (w,x) to (C(w),x). Every inverse has
identity seed transport and hence its OWN IMAGE factor 1. Its
full cocycle is zero and every time group H is zero.
For g(w)=p^e, EVERY real seed eventually reaches ((p),x),
so source AND extension isotropy are Z; the periodic points
themselves are all ((p),x). In all terminal basins and the empty
fibre these groups are trivial. The global zero-time claim follows
from the actual IMAGE law, not from erasing root recurrence.

### RADIAL-WEIGHT: same action, different declared measure

Keep the entire main T but put mu_r=|x| dx on every fibre.
It is locally finite, sigma-finite and full support: every nonempty
open interval has positive integral, including those containing zero.
For every Borel E and a>=1, substitution x=a*y gives

    mu_r(aE)=a^2*mu_r(E).

Thus its OWN inverse factor is a_1^2, its full continuous cocycle
is twice the main one, and its complete time groups are
H_r=(2 log p)Z on R_p and zero elsewhere. Source isotropy
and the full state/packet identities are unchanged; extension isotropy
is still trivial everywhere. Null zero seeds are retained under
the unique continuous version, not assigned a value by hand.

This does NOT make the frozen Lebesgue clock ambiguous. The
comparator violates additive translation invariance: its masses of
[0,1] and [1,2] are 1/2 and 3/2. On a real fibre a locally
finite translation-invariant measure is a constant multiple of
Lebesgue: interval additivity and monotonicity give that formula
first at rational lengths, then at all lengths. The declared
unit density fixes this constant. Radial reweighting instead shows
that the symbolic source alone, without the extra measure structure,
does not force the logarithmic time normalization.

### ORDER: factor sorting is not responsible for prime selection

Replace ascending factor words by descending words with the same
multiplicities. Singleton inverse targets change accordingly, but
each actual inverse still scales its real fibre by its own first
entry and hence has its OWN Lebesgue IMAGE factor a_1. Gcd of
all factors is independent of their order, so the exhaustive root
classification is unchanged. Finite transient scaling products may
change, but each recurrent singleton remains p with seed update x/p.
The full R_p, isotropy, one-packet-per-prime and repetition results
are therefore unchanged under this comparator. No arbitrary ordering
quotient or identification of transients was introduced.

## 6. What is established and what remains a design choice

The source itself executes factor refinement and common-divisor
coalescence on all words; the complete classification proves prime
specificity, and FACTOR-OFF detects its loss. The clock follows
from the same action and measure, and ORDER checks a genuine
robustness direction. No arbitrary accepted-set oracle or prime
table was supplied to the main owner.

These facts do not derive the necessity of complete factorization
as one operation, scheduling it at length one, using gcd for
coalescence, selecting x/a_1 as the geometric transport, or choosing
the real additive-measure structure. UNIT-TRANSPORT and RADIAL-WEIGHT
show that an unchanged arithmetic word rule is not by itself a
physical clock. The real coordinate remains passive with respect
to C, and the action is not a symplectic conservative lift.
No arbitrary-set universality or general impossibility follows from
these controls; neither was proved. Strong naturalness remains OPEN.

## 7. Gate assessment and portfolio decision

| Gate | Evidence for this exact owner | Status / limit |
| --- | --- | --- |
| T0 | Full carrier, both inverse families, terminals and LCH etale tail owner | ESTABLISHED |
| T1 | Executed factor/gcd source and its actual real IMAGE clock | SCOPED ENGINEERING ADVANCE; stronger naturalness OPEN |
| T2 | ALL state basins/isotropy; exactly one least-log-p packet per prime and all repeats | ESTABLISHED complete abstract packet theorem |
| T3 | No trace, zeta, determinant or operator supplied | NOT PURSUED under this bounded contract |
| Classical A0/A1/A2 | No finite-dimensional symplectic suspension | NOT APPLICABLE; no natural-A0 promotion |
| Formal Route A / B | No formal evaluation | UNASSIGNED / NOT INVOKED |

Portfolio: **advance the scoped source/clock/packet construction;
stop natural-A0 promotion; fork the search for arithmetic/geometric
justification of the declared transport and source choices**. A
positive packet theorem is preserved, not collapsed into a failure
or enlarged into a Route result. No object, measure or packet
convention changed. A later analytic or geometric proposal requires
its own explicit contract and ownership proof; none is appended here.
See the [source/frontier record](evidence/scout-record.md) for provenance
and any separately unadmitted follow-up definition.

## Reproducibility and internal review

The proof covers all finite word lengths, integer entries and real
seeds, with no cutoff, precision choice or scientific computation.
All transient products are exact, and finite examples do not stand
in for the all-state argument. [Evidence](evidence/README.md) binds
the original card, final paper, [claim ledger](claim-ledger.md),
[internal review](evidence/independent-review.md) and document checks;
the [package index](README.md) summarizes the scoped decision.
ARS uses raw-card, manuscript and adverse checkpoints with inherited-
model/shared-context limits, not external peer review or independent-
error evidence. Old packages/mirrors unchanged; 241/242 paused;
programme goal active. Markdown only; no publication or Git commit.
