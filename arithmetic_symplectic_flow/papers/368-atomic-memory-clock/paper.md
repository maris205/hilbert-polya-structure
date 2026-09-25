# Countable reset memory: atomic IMAGE clocks have zero return image

**Paper:** `368-atomic-memory-clock`; **candidate:** `ANG-AUDIT-20260921-AMC01`.
**Date/status:** 2026-09-21; exact conditional theorem, negative return gate.
**Decision:** CONDITIONAL ATOMIC CLOCK FILTER — STOP / FORK UNDER HYPOTHESES.
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

For one full countable state set with strictly positive finite atom masses,
every-Borel IMAGE determines the clock of every actual groupoid arrow,
including all retained isotropy labels. It is the difference of endpoint
log-masses. Consequently every entire isotropy group has zero clock image,
even if the source has many reset cycles. We determine the full kernels,
extension isotropy and physical phases. Weighted transport, a retained loop
group, and a separately measured nonatomic binary-prefix source test the
distinctions between nonzero arrow clocks, source cycles and positive physical
periods. This is a conditional filter for countable memory repairs, not a
constructed arithmetic candidate or a no-go for nonatomic history spaces.

## 1. Same-object ledger and precise question

All definitions are those of the [69-line card](candidate-card.md), SHA256
`7b8cac9a4941a415d0edd74f263977df5b739a43513adf8b25ac03f247f30fa4`.
Fix ONE countable X, masses0<m(x)<infinity, counting-weighted measure mu,
ONE countable discrete groupoid G with unit set X, and a fixed homomorphism
ell:G->Z. Every actual arrow and label is retained. The question is whether
an owned IMAGE clock can give positive return times after symbolic histories
have been reset into this exact countable memory carrier.

| Field | Frozen owner | Boundary |
| --- | --- | --- |
| Carrier / arithmetic link | Complete countable retained/reset symbolic states | No new arithmetic realization constructed |
| Measure | mu({x})=m(x)>0, finite at every state | Sigma-finite, not assumed invariant |
| Evolution | Actual G and its bisections | Arbitrary isotropy retained |
| Clock | Negative logarithm of actual IMAGE | Derived below, not supplied roof |
| Time | Translation on full real-extension orbit set | Set claim only |
| Symplectic map / suspension | None | NOT APPLICABLE |
| Trace / operator | None | T3 NOT AUDITED |

The exact lineage under test is divisor-symbolic history -> countable exact
memory/reset -> its own actual inverse/history law. Arithmetic is not used
in the theorem: the PROVES_TOO_MUCH warning is a scope fact, not evidence of
prime specificity. A nonatomic path completion is a different owner.

## 2. Unique all-point IMAGE and complete clock

**Theorem.** On every actual arrow g:x->y the only every-Borel IMAGE version is

    J(g)=m(y)/m(x),       c(g)=log m(x)-log m(y).                 (1)

Indeed the singleton bisection {g} transports {x} to {y}. Its IMAGE identity
requires m(y)=J(g)m(x), with a positive finite denominator. The same argument
on any larger bisection fixes its value at every source point, not merely
almost everywhere. Conversely, for any bisection B and every subset E of
its source, injectivity gives

    mu(theta_B E)=sum_(x in E)m(theta_B x)
                 =integral_E [m(theta_B x)/m(x)] dmu(x).

Countable sums are legitimate even when infinite. This proves the required
identity on EVERY Borel subset, cross-chart consistency and uniqueness on all
labels with the same endpoints. Sigma-finiteness follows by covering X by its
finite-mass singletons. No null state was discarded: none is in the hypothesis.

For g:x->y and h:y->z, J(hg)=J(h)J(g); logarithms give
c(hg)=c(h)+c(g), and inversion changes the sign. This owns one real cocycle
on the entire groupoid. Different loop labels remain different arrows even
though their J and c coincide. There is no assumption that ell measures time.

## 3. Full kernels, arbitrary isotropy and all physical phases

The complete arrow kernels, not just their isotropy restrictions, are

    ker c = {g:x->y : m(x)=m(y)},
    ker ell = {g : ell(g)=0},
    ker c intersect ker ell = {g:x->y : m(x)=m(y), ell(g)=0}.

For every x the source isotropy is its FULL given group I_x=G_x^x, with no
cyclicity/effectiveness assumption. Equation(1) is zero on every element,
so H_x=c(I_x)={0}. In the real extension an arrow is
(x,h)->(y,h+c(g)); its isotropy at (x,h) is still the entire I_x. No loop
label was removed to reach a zero-time conclusion.

All incoming states are exactly the actual orbit O_x={y:there is g:x->y};
all the corresponding arrows remain. Endpoint-dependent clocks imply that

    a(x,h)=h+log m(x)

is constant along extension arrows. On a fixed source orbit it is a COMPLETE
orbit-set coordinate: two heights with the same a are connected by every
actual arrow with those endpoints. Thus the quotient as a SET consists of
one real line of phases for each actual source orbit. Translation acts by
a->a+t; its stabilizer is H_x=0. No positive primitive time or repetition
packet exists. This does not kill source cycles, their multiplicity or their
possibly noncyclic isotropy. No global Borel transversal or coarse topology
is claimed.

## 4. Own controls and hypothesis boundary

### WEIGHTED-LINE

Here sum_(n in Z)2^(-|n|)=3, so m(n)=2^(-|n|)/3 is a probability.
The actual bijection F(n)=n+1 has inverse n-1; all histories n->n+k are
retained with ell=k. For every subset E, the direct sum change of variable
gives its OWN IMAGE and clock

    J_k(n)=2^(|n|-|n+k|),   c_k(n)=(|n+k|-|n|)log2.

Full clock kernel is |n+k|=|n|, allowing k=-2n as well as0; lag kernel
and the intersection are k=0. Source and extension isotropy are trivial;
H=0. All integers are incoming in one actual orbit, with every phase
h-|n|log2-log3. The clock on 0->1 is nonzero but is not a return clock.

### FIXED-LOOP

The sole state has mass1; each retained integer loop induces the identity
on its singleton. Its own every-Borel IMAGE is1 and c=0. Source and
extension isotropy are the entire Z, not trivial; H=0. Clock kernel is ALL
arrows, lag kernel and intersection are only the zero label. There is one
incoming state with ALL integer incoming arrows, and every real height is
a separate phase. Source periodicity and label multiplicity do not create
a physical circle or a branch-entropy clock.

### NONATOMIC-BINARY

Use the full one-sided binary product space with fair Bernoulli law. Both
prefix maps theta_a(w)=aw are actual inverses of its shift. Independence
gives mu(theta_a E)=mu(E)/2 for EVERY Borel E. Freeze that same full-point
version on null paths. Prefixing length m gives IMAGE2^(-m); replacing a
length-n prefix by length m has IMAGE2^(n-m), on every Borel chart domain.
Actual triples (z,k,w) with T^m z=T^n w, k=m-n, identify equal triples only.
The owned c=k log2 is witness-independent and additive, with no free labels.

The full clock and lag kernels coincide with synchronized equal-depth tail
equivalence. Unequal shift equality occurs exactly at eventually periodic
sources; if the eventual tail has least period l, ENTIRE source isotropy
is lZ and H=l log2 Z. Otherwise both are0. Extension isotropy is always
trivial because c is injective on source isotropy. Primitive words modulo
cyclic rotation give ALL positive packets, each least time l log2; powers
give only repetitions r*l log2. Distinct primitive necklaces cannot acquire
a common tail, so their packets never merge. If P_l is the number of
primitive length-l binary words, 2^n=sum_(l|n)P_l gives exactly P_l/l packets.

For a periodic core eta of least l, every incoming state is u T^j eta,
0<=j<l, with arbitrary finite binary u. Its phase relative to eta is
h-(|u|-j)log2 modulo l log2; differing representations change this by H.
For an aperiodic-tail orbit anchored at a, all incoming are all prefixes of
all T^n a. Its actual lag to a is unique, and phase is h-k log2 in R.
All prefixes, null periodic paths, rotations, heights and repetitions remain.
In particular the two constant words yield distinct log2 packets. They have
zero singleton mass, so the atomic singleton division in(1) is unavailable.
This is a genuine boundary control, not a changed version on MAIN's states.

## 5. Gate, adverse findings and decision

T0/T1 are exact CONDITIONAL owner statements on the frozen class. The entire
T2 positive-return target fails there: H=0 for every state, even with source
cycles. This does not construct an arithmetic owner, prove canonical measure
selection or exclude arbitrary long-memory/non-atomic laws. T3 NOT AUDITED;
classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
The same-object ledger remains intact. Stop countable positive-atom reset
repairs as a route to positive IMAGE periods; a new measured owner requires
a fresh card. The next separately frozen test keeps full product memory and
finite rewrites, rather than treating its points as positive atoms.

## Reproducibility and evidence

Exact inputs and method: the frozen card and proofs by singleton IMAGE,
countable sums, endpoint cancellation and full product-prefix identities.
No finite numerical sample, external literature or novelty claim is used.
Root wrote this proof before reading the independent derivation. ARS CP1
released analysis only after the scope report was read; the separate raw-card
proof and CP2/CP3 are internal shared-history NOT_CALIBRATED, not peer review.
[Claims](claim-ledger.md), [scope](evidence/scope-review.md),
[independent proof](evidence/independent-proof.md), [review](evidence/review.md).
