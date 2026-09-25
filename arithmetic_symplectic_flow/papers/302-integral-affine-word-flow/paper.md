# Integral affine words own a real clock but retain infinitely many singleton packets

Paper ID: `302-integral-affine-word-flow`.
Candidate ID: `ANG-20260920-IAW01`. Date: 2026-09-20.
Status: `OWNED REAL IMAGE CLOCK; INFINITE SINGLETON PACKET MULTIPLICITY — STOP / FORK`.
Route state: broadened owner audit; classical A0/A1/A2 NOT APPLICABLE;
formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

All finite words of positive-slope integral affine letters, including
units and the empty word, carry full real seed fibres. A partial
integral refactorization cycles the first letter past the remaining
composition while transporting the seed by its inverse. The entire
partial map has a unique predecessor on every nonempty target fibre,
including terminal targets. Counting-root Lebesgue measure gives
inverse IMAGE factor a, not the profinite factor 1/a, and yields
a complete continuous real-time extension of the full tail groupoid.
Nevertheless each singleton letter a*t+b, a>=2, has one positive
primitive packet of least time log a, for EVERY b in Z. Different
letters cannot be merged by the actual arrows. Already a=2 has
infinitely many prime-time packets; a=4 gives separate composite
primitives. The frozen mixed-slope two-letter control gives an
additional length-two log-6 packet, not a singleton identification.
The candidate stops without an all-word return census or T3 rescue.

## 1. Identity, question and claim boundary

The [original card](candidate-card.md) freezes the object before
this proof. The question is whether integral word admissibility,
an exact divisor-symbolic deformation, produces an owned clock
and the desired full primitive ledger without prime-only selection.

| Field | Same frozen owner | Scope |
| --- | --- | --- |
| Carrier | Y=coproduct of ALL finite integral-affine words w with real fibre R | ANG track, not a classical symplectic lift |
| Action | Integral refactorization H and inverse first-letter seed transport | Partial, full terminal fibres retained |
| Arithmetic | Integral composition and divisibility of translation expressions | No prime predicate, table or per-prime input |
| Measure | Same Lebesgue measure on every discrete word root | No fitted weights |
| Clock | Negative logarithm of actual IMAGE density | Derived below; no separate roof |
| Arrows and packets | Full retained-lag tail groupoid, real phases, complete isotropy image | No free split, conjugacy or cyclic quotient |
| Classical base / mapping torus / Hamiltonian owner | NOT APPLICABLE / NOT SUPPLIED | No Logistic/Henon conjugacy asserted |
| Trace / zeta / determinant / operator / quantum owner | NOT SUPPLIED / NOT PURSUED | No later-route credit |

All translations b and all real seeds are retained. Strong
naturalness of the real transport and the source replacement is
OPEN. An integral formula alone is not prime selectivity. This
bounded negative result neither classifies all multiword returns
nor claims a natural conservative geometric realization.

## 2. Full action, integrality and inverse ownership

A letter is f(t)=a*t+b with a>=1 and b in Z. Words are
literal ordered tuples, not total affine maps or cyclic classes.
Composition means (f circ g)(t)=f(g(t)). For a nonempty
w=(f_1,...,f_k), write f_1(t)=a*t+b and

    P=f_2 circ ... circ f_k=A*t+B,

where A>=1 and B is integral. For k=1, P=id, A=1,B=0.
Let D be the union of precisely those nonempty root fibres with
A dividing b+(a-1)B. On D define

    beta=(b+(a-1)B)/A,        g(t)=a*t+beta,
    H(w)=(f_2,...,f_k,g),     T(w,x)=(H(w),(x-b)/a).

The identity P circ g=f_1 circ P holds because the slopes are
both aA and the translations satisfy A*beta+B=aB+b.
Conversely that identity forces this beta. Thus the divisibility
condition is exactly the condition that this refactored letter
remain integral, not a test added after selecting a periodic word.

For ANY nonempty target v=(h_1,...,h_k), put

    h_k(t)=a*t+beta,   Q=h_1 circ ... circ h_(k-1)=A*t+B,
    b=A*beta-(a-1)B,  f(t)=a*t+b,
    I(v,z)=((f,h_1,...,h_(k-1)), a*z+b).

The length-one convention is again Q=id. This predecessor has
integral coefficients and satisfies the domain test, since
b+(a-1)B=A*beta. Substitution shows T I(v,z)=(v,z).
Conversely H(w) determines the former tail and the new last
letter; these determine a,b uniquely by the displayed equation.
The real seed is likewise uniquely recovered. Thus I T=id on D,
and T is a homeomorphism from D onto Y_*, the union of ALL
nonempty fibres. Both are clopen in the countable coproduct Y.
Each branch is an affine homeomorphism of a whole real fibre.
Y is locally compact, second-countable and Hausdorff.

The empty fibre has no incoming or outgoing nonidentity step.
Every failed nonempty root is terminal but DOES have a predecessor.
For example v=(t+1,2t) fails its 2-divides-1 domain condition,
yet

    I(v,z)=((2t-1,t+1),2z-1)

is defined for every real z and maps back to that terminal fibre.
A terminal is not deleted or declared isolated merely because its
forward domain is empty. All unit slopes and negative translations
remain; for a=1 the domain is A divides b and seed update x-b.

Word length is preserved in BOTH directions. The slope list rotates
under H, but changes of translation coefficients still govern later
admissibility. Neither a finite slope list nor preservation of a
field is treated as a proof of full-word periodicity.

## 3. The actual real IMAGE clock and time owner

On every root use ordinary Lebesgue measure, counting over roots.
This measure mu is sigma-finite, locally finite and full support;
individual points have zero mass. For every Borel E in a target
fibre, its inverse I has the real affine form z->a*z+b, so

    mu(I(E))=a*mu(E),       J_I=a,       c(I)=-log a.

The IMAGE orientation is target to predecessor. The forward arrow
has the reciprocal density and opposite clock. Replacing a by
1/a in this inverse formula would import a different measure from
the profinite setting; it is not the clock of the frozen object.

Retain the entire partial-map tail groupoid

    G_T={(z,m-n,w): T^m z=T^n w, m,n>=0},

with all iterates actually defined, source w, range z. Finite
actual branch pairs over common open terminal domains, refined by
intervals, give its topology. They give local source and range
homeomorphisms; intersections refine by aligning existing histories.
Composition aligns the middle histories, using only extensions
already justified by the defining equalities. It does not assume
that a terminal has a future step. Compact interval restrictions
give local compactness; range, source and integer lag separate
distinct triples, giving a Hausdorff etale groupoid.

Let R_m(z) be the product of the first-letter slopes during the
ACTUAL first m steps from z; R_0=1. The terminal-to-z inverse
of that history scales Lebesgue measure by R_m(z). Thus a branch
pair from w to z has

    J=R_m(z)/R_n(w),
    c(z,m-n,w)=log R_n(w)-log R_m(z).

Two valid presentations of the same lag differ by extending both
histories along their already-defined common tail. Equal terminal
products cancel. This proves presentation independence; aligning
middle histories proves cocycle additivity. Factors are locally
constant on root-history charts and continuous on every interval
refinement. Full support uniquely fixes this continuous version
from its almost-everywhere density, INCLUDING all null fixed seeds.
The assigned measure, not a later choice of fixed-point clock,
therefore owns the result.

Use all extension objects Y x R with arrows

    (w,s)->(z,s+c(g)).

Translation (z,s)->(z,s+t) for all real t commutes with the
arrows and is jointly continuous and two-sided complete. The
extension groupoid is etale, hence its orbit projection is open;
the resulting quotient time action is continuous as well. Coarse
Hausdorffness and embedded-circle statements remain OPEN.

For every tested z use H_z=c(G_z^z). A least positive generator
T_z of H_z defines a primitive time packet; the sign of a
particular arrow generator is irrelevant to that subgroup. Fixed-
object extension isotropy is the kernel of c on source isotropy.
Repetition is ell traversals of the SAME packet, never an equality
of numerical lengths between unrelated cores.

## 4. Exact divisor-symbolic lineage

The [prior-work interface](../../docs/prior_work/README.md) is the
proper-divisor symbol on a letter's slope. For 1<d<a,

    d divides a iff f=(t->d*t+b) circ (t->(a/d)*t)
                    with both slopes integral.

Indeed the displayed composition is a*t+b, and its second slope
is integral exactly when d divides a. The new root dynamics
replaces these elementary factor-admissibility relations with the
integral refactorization P circ g=f_1 circ P proved in Section 2.
The translation congruence really affects the evolving root domain.
This is a mathematically specified divisor-symbolic -> affine-word
admissibility deformation, not merely the label 'arithmetic'.

Those split relations are NOT arrows of G_T. Adding free split,
merge, affine conjugacy or cyclic-word identifications would change
the owner and its packet ledger. No chronological sieve equivalence,
Logistic/Henon lift or prime-only return property is inferred.
The adequacy and stronger naturalness of this source replacement
remain OPEN. The lineage relation does not force nonprime slopes
to leave the recurrent set.

## 5. All singleton returns and decisive packet surplus

For each singleton f(t)=a*t+b the root domain always holds,
H((f))=(f), and the entire real-fibre action is S(x)=(x-b)/a.
Its inverse remains on that SAME literal letter. No root of another
length or another singleton letter is connected to it by a tail
arrow: length is preserved, and singleton roots never change.

For a>1 put r=-b/(a-1). Then

    S(x)-r=(x-r)/a,     S^m(x)-r=a^(-m)*(x-r).

Consequently ALL positive-period real seeds are exactly x=r,
and they are fixed. Equality S^m(x)=S^n(x) with m>n also
forces x=r, so there is no additional eventual-return seed.
At that fixed core the complete source isotropy is Z and

    c(ell)=-ell log a,   H=(log a)Z,
    fixed-object extension isotropy=0.

The primitive least positive time is log a, despite the negative
clock of the chosen inverse generator. All nonfixed seeds have
trivial source and extension isotropy and H=0.

For a=1,b=0 the entire real fibre is fixed: source and extension
isotropy are Z, while H=0. For a=1,b!=0, S^m(x)=x-m*b
has no nonzero return at any seed; both isotropies and H are
trivial. Thus unit identity and unit translation boundaries are
different; a zero clock alone never determines their isotropy.

Different b values give different singleton roots and constant
fixed tails. Their cores cannot be merged by any actual tail
arrow, any longer-word excursion or a real time phase. There is
exactly ONE positive primitive packet in each a>1 singleton fibre,
but countably infinitely many such distinct packets for EVERY
fixed a>=2 as b ranges through Z. These are family counts, not
a complete enumeration of packets at that time in the full carrier.

Already a=2 violates the desired finite prime-packet multiplicity.
Each a=4 core is independently primitive of time log 4, not a
repeat of an a=2 packet even though log 4=2 log 2. Selecting
b=0, identifying affine-conjugate fixed points, deleting composites
or adjoining factor-split arrows would change the frozen object.
The fixed points are Lebesgue null but retained under the proved
continuous clock. Target promotion therefore STOPS here.

## 6. Precommitted boundaries and separately owned controls

### The literal mixed-slope word

The frozen w_0=(2t,3t) is admissible, H(w_0)=w_1=(3t,2t),
and H(w_1)=w_0. The real updates are x/2 and then x/3,
so T^2(w_0,x)=(w_0,x/6). The two literal roots differ, excluding
odd returns. Hence x=0 is the ONLY periodic seed on these
two fibres. Its least source period is 2, source isotropy is 2Z,
and c(2*ell)=-ell log 6. Thus H=(log 6)Z and extension
fixed-object isotropy is zero. The two phases form one primitive
packet. All nonzero seeds have trivial isotropy and time groups.
No word-length-preserving arrow identifies it with the singleton
6t packet. This is the specified two-letter ownership test only.

Every main terminal state has trivial source isotropy, since no
positive iterate from it exists. Its H and extension isotropy
are also trivial, regardless of actual incoming arrows. The empty
fibre is included, without an artificial identity-time loop.

### REFACTOR-OFF

Use plain cyclic rotation on every nonempty word and the same
inverse first-letter seed transport. This changed root map is
invertible on nonempty words; its inverse moves the last letter
a*t+b to the front and sends the seed to a*z+b. Under its OWN
counting-Lebesgue measure this has IMAGE a and clock -log a.
Actual branch products give its own full continuous cocycle.

For singletons its exact map is again (x-b)/a. Thus the complete
singleton analysis in Section 5 applies by direct equality of
these control branches: one log-a primitive per a>1,b, identity
unit isotropy Z/H=0, and no translated-unit returns. The frozen
(2t,3t) pair likewise rotates and has the same explicitly checked
two-step seed x/6, with one log-6 packet at zero. No other control
words are classified. Removing refactorization does not remove
the tested surplus; the main integrality condition did not select it.

### UNIT-TRANSPORT

Keep the main partial word action and domain, but transport x
identically. Its inverse has the same word predecessor and the
identity real seed map. Equal root-fibre Lebesgue measures give
IMAGE 1, so c=0 and EVERY time group H is zero. The main
log-slope clock must not be attached to this changed action.

For every singleton letter and EVERY real x, the root and seed
are fixed, giving source and extension isotropy Z. Terminal
states have both isotropies trivial. On the frozen mixed-slope
pair every x has least source period 2 and source/extension
isotropy 2Z, but still H=0. Other root isotropies remain unclassified;
the global zero-time conclusion follows from the global IMAGE law,
not from a partial return census.

The realised PROVES_TOO_MUCH risk is integer-slope primitives
with unbounded translation-labelled multiplicity. Natural root
refactorization and an owned clock alone do not impose the desired
prime ledger. Units, terminals, null cores and inverse directions
are ownership controls, not disposable exceptions.

## 7. Gate assessment and portfolio decision

| Gate | Same-object evidence | Status / limit |
| --- | --- | --- |
| T0 | Full word partial homeomorphism, inverse domains, terminals and retained-lag owner | ESTABLISHED |
| T1 | Exact divisor-symbolic relation and real IMAGE clock | SCOPED MEASURED RESULT; stronger naturalness OPEN |
| T2 | ALL singleton returns, full H, packet nonmerging and frozen two-letter test | ESTABLISHED TESTED FAMILIES; target multiplicity/composite requirement FAILS |
| T3 | No trace, zeta, determinant or operator | NOT SUPPLIED / NOT PURSUED |
| Classical A0/A1/A2 | No finite-dimensional symplectic realization | NOT APPLICABLE; formal coordinates UNASSIGNED |
| Route B | No formal readiness or evaluation | NOT INVOKED |

Portfolio: **stop target promotion / fork**. Infinitely many
different log-2 singleton primitives are decisive without a general
multiword census. Composite and mixed-word controls reinforce, not
repair, that failure. The same-object ledger stayed intact.
Other multiword returns, coarse topology and naturalness remain
OPEN / NOT PURSUED. Further source proposals belong only to the
separate [definition/admission record](evidence/scout-record.md);
none changes this candidate or inherits its clock or Route credit.

## Reproducibility and internal review

This is an exact proof for arbitrary singleton a,b and EVERY
real seed, plus the named boundary and two-letter tests. There
is no finite cutoff, numerical precision or scientific computation.
[Evidence](evidence/README.md) records provenance, hashes, methods
and document QA; see the [claim ledger](claim-ledger.md),
[package index](README.md) and [internal review](evidence/independent-review.md).
ARS supplies raw-card, manuscript and final adverse checkpoints,
using inherited-model/shared-context execution, not external peer
review or independent-error evidence. No external literature lemma
or manuscript upload is used. Historical packages/mirrors remain
unchanged; 241/242 paused; programme goal active. Markdown only.
