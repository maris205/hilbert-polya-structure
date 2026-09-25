# Reversible factor redistribution and unwanted relative-return packets

**Paper ID:** `269-factor-redistribution-lattice`  
**Candidate ID:** `ANG-20260919-FRL01`  
**Date:** 2026-09-19. **Evidence:** exact construction and negative proof.  
**Status:** `FULL REVERSIBLE OWNER; ALL-INTEGER TRANSPORT PACKETS — STOP / FORK`.  
**Formal coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

The frozen source redistributes each adjacent pair of positive integers
cyclically through all ordered factorizations of its product, with even
and odd layers. All finite non-vacuum configurations are retained. The
map is a bijection, conserves total product and descends to the entire
quotient by even spatial translations. Its unit suspension is a complete
flow with the stated primitive/repetition convention. However, every
configuration supported on even sites, with arbitrary integer contents,
translates right by two sites at every step. Each therefore gives a
time-1 primitive circle in the quotient. This includes all composite
singletons and infinitely many distinct packets at a fixed product p².
The complete prime-product sector has exactly two primitive circles per
prime, both of time 1. Actual neighboring factor redistribution occurs
elsewhere, but does not exclude these transport packets. The candidate
stops without retiming, deleting states or classifying its remaining
periodic orbits. No classical symplectic lift or analytic owner is supplied.

## 1. Question, identity and lineage

Can reversible local factor interactions turn prime/composite
admissibility into useful intrinsic closed packets, rather than merely
generate generic transport? The [version-1 card](candidate-card.md) fixed
the complete source, spatial quotient and clock before this audit.

The precise lineage is the prior-work prime/composite observable and
symbolic admissibility arrow, replaced here by all-integer factor
redistribution and reversible neighboring updates. This is a stated
symbolic deformation, not a conjugacy to a Logistic or Hénon map. No
positive-dimensional conservative or symplectic lift has been established.
The [prior-work guide](../../docs/prior_work/README.md) motivates the
question; no theorem is imported from its papers.

| Same-object field | Frozen owner retained here |
| --- | --- |
| Source | All finite nonempty nonunit configurations W on Z, with discrete topology |
| Arithmetic update | Cyclic successor among all positive divisors of the current pair product |
| Chronology | Even layer E followed by odd layer O; F=O E |
| Main carrier | The entire Q=W/⟨S²⟩, not a chosen set of gliders |
| Physical clock | The unit suspension of Fbar on Q |
| Packets | All primitive Fbar-orbits, with actual suspension phase identification only |
| Conserved charge | P(w)=product of all nonunit entries, derived below |
| Later owners | No symplectic/contact lift, transfer operator, zeta or quantum object supplied |

Divisor order, layer chronology, the spatial quotient and the macroclock
are explicit design choices. No table of primes or per-prime clock is
used, but this absence is not a naturalness theorem. The full integer
product P is an invariant charge, not a dynamically changing prime label.

## 2. Exact definitions and comparisons

Let

    W={w in N_{>=1}^Z : 0<|supp(w−1)|<infinity},
    (S w)_j=w_(j−1).

For a,b>=1 let 1=d_0<...<d_k=ab be the full increasing divisor list.
If a=d_i, the local map is

    C(a,b)=(d_(i+1 mod (k+1)), ab/d_(i+1 mod (k+1))).

E applies C on (2j,2j+1); O applies C on (2j+1,2j+2); F=O E.
The main map is Fbar[w]=[Fw] on Q=W/⟨S²⟩. Its flow is

    M=(Q x R)/((q,u+1)~(Fbar(q),u)),
    Phi^t[q,u]=[q,u+t].

All integer values, supports and translation classes occur in these
definitions. The spatial quotient is part of the original card, not a
repair after finding a nonreturning orbit. It is nevertheless a material
change of owner from W: quotient returns are only relative returns upstairs.

The nearest local comparison [232](../232-source-feedback-frontier/candidate-card.md)
also has alternating pair layers, but starts with an atom alphabet,
redistributes pair sums and uses a different direction/scale flow.
[136](../136-factorization-nonbacktracking-flow/README.md),
[217](../217-divisor-scattering-return/README.md) and
[225](../225-euclid-edge-scattering/README.md) instead use factorization
graphs or ordered ports. Their packet and clock statements are not used
as proof inputs. No external novelty claim is made.

## 3. Full action and flow ownership

### Proposition 1 — reversible arithmetic action

C is a bijection on positive integer pairs. E, O and F are bijections
of W, preserve P(w)=∏_j w_j and commute with S². Consequently Fbar is
a bijection of the full discrete, countable quotient Q.

**Proof.** At a fixed product N, ordered pairs are in bijection with its
finite positive divisor list by d↦(d,N/d). C is exactly a cyclic
permutation of this list. The inverse takes its cyclic predecessor. At
N=1 the unique pair (1,1) stays fixed. Thus the inverse of F is
E^{-1} O^{-1}, not the layers in the forward order.

Only finitely many pairs in either layer meet the finite nonunit support;
all other pairs remain (1,1). Each output pair has its original product.
Hence the output still has finite support, and its total product remains
P(w)>1. It cannot become the excluded all-vacuum state. The same argument
applies to the inverse layers, proving surjectivity on the whole W as
well as injectivity. Every layer's pairing is preserved by translation
through two sites, giving commutation with S². This proves descent and
the inverse on Q, and shows that P also descends to Q.

There are countably many finite integer configurations. Since W is
discrete, every subset of Q has an open preimage and Q is discrete and
countable. A nonzero translation cannot fix a finite nonempty support:
iterating it would produce infinitely many support sites. In particular,
no additional spatial stabilizer is hidden in the quotient. ∎

### Proposition 2 — complete flow and primitive convention

M is a disjoint union of circles and lines, with a complete continuous
translation flow and no stationary point. A least-period-m Fbar-orbit
gives exactly one circle of least physical time m, with repetitions r m.
An infinite Fbar-orbit gives a line with no positive return.

**Proof.** Decompose the discrete Q into its orbits under the bijection
Fbar. An orbit of m points is identified cyclically by the unit endpoint
relation and yields R/mZ. An infinite orbit is indexed by all integers;
concatenating its unit intervals gives R. These components are open and
closed because Q is discrete, so this also proves that the complete
quotient is Hausdorff. Translation exists for every real t on each
component. There is no Zeno accumulation because each crossing costs
one unit. No point is fixed by all real t. A positive return in the
section must cross an integer number of intervals, so the least circle
time is the least base period, not a chosen divisor of it. ∎

Equivalently, a base return is exactly

    F^m w=S^(2k) w for some integer k and m>=1.                 (1)

An ordinary upstairs return additionally needs k=0. No argument below
forgets this distinction.

## 4. Decisive transport packets

### Proposition 3 — arbitrary even-site contents return in the quotient

If w is supported entirely on even sites, with any integer contents
greater than 1, then Fw=S²w. Thus every such spatial class gives a
primitive circle of time 1 in the frozen flow.

**Proof.** For every a>=1, the final divisor a of a has successor 1,
including the singleton list at a=1. Therefore

    C(a,1)=(1,a).                                            (2)

An even-site configuration is a disjoint array of pairs (a,1). E moves
each content to the odd site on its right. At the start of O, every
active pair again has the form (a,1), because all even sites are empty.
Equation (2) moves each content one more site to the right, proving the
identity. No neighboring token overlaps another in either layer, even
when occupied even sites are only two sites apart.

In Q, S²w and w define the same point. Its least positive integer period
is therefore 1. Proposition 2 gives a genuine primitive time-1 circle,
not a stationary flow point. ∎

This is an infinite exact family of ALL-INTEGER returns, not finite
numerical evidence. For every N>=2, the singleton N at site 0 provides
such a primitive. In particular N=4 and N=6 are composite counterexamples.

### Proposition 4 — complete prime-charge sector

For each prime p, all states with P(w)=p are singletons p. In Q there
are exactly two such states, distinguished by site parity. Both are
fixed by Fbar and give two distinct primitive time-1 circles.

**Proof.** A product of positive integers equals p only if exactly one
nonunit factor equals p. Even spatial translations identify precisely
the even singletons with one another and the odd singletons with one
another; they do not identify the two parities.

The even state is covered by Proposition 3. The divisor list of p is
(1,p), so C(1,p)=(p,1) as well as C(p,1)=(1,p). For an odd singleton,
E moves p one site left and O moves it one more site left. More generally,
any configuration of prime contents on odd sites obeys Fw=S^{-2}w.
Its quotient point is fixed. These are all the prime-charge states, and
the two resulting circles cannot be identified by time translation
because their fixed base points differ. ∎

The prime clock is exactly 1 for every prime, not a quantity growing
like log p. Keeping two distinct parities is compulsory under the card.
The prime-charge classification is complete; the full periodic ledger
over all charges is not claimed to be classified.

### Proposition 5 — infinite multiplicity even at a fixed composite charge

Fix a prime p. For each d>=1 put p at sites 0 and 2d and put 1 elsewhere.
These configurations all have product p², and give pairwise distinct
primitive time-1 circles of FRL01.

**Proof.** Proposition 3 supplies the return for each configuration.
Even translations preserve the support gap 2d, so different d cannot
represent the same point of Q. Since these are fixed points of Fbar,
cyclic time phase identifies none of them with another. Moreover, P is
invariant along the full suspension: an endpoint crossing preserves it.
Their charge p² differs from the charge p of a prime-sector circle.
They are not repetitions of that circle; even their least time is 1,
whereas its twice-traversed time is 2. ∎

There is likewise an infinite mixed-charge family with distinct primes
p and q at 0 and 2d. Matching clock values never changes packet identity.
These families suffice to trigger the frozen stop. No classification of
all colliding, mixed-parity or higher-period configurations is needed.

## 5. Controls and adverse evidence

All unspecified sites in the following exact controls equal 1. They
are direct arithmetic evaluations, not a numerical orbit search.

| Initial nonunit sites | After E | After O, hence after F |
| --- | --- | --- |
| 4 at 0 | 4 at 1 | 4 at 2 |
| 6 at 0 | 6 at 1 | 6 at 2 |
| 2 at both 0 and 1 | 4 at 0 | 2 at both −1 and 0 |
| 4 at 1 | 2 at both 0 and 1 | 2 at both −1 and 2 |
| 6 at 1 | 2 at 0 and 3 at 1 | 2 at −1 and 3 at 2 |

For the first two rows, C(4,1)=(1,4) and C(6,1)=(1,6) explain both
layers. The third row uses C(2,2)=(4,1), followed on sites (−1,0) by
C(1,4)=(2,2). This merge/split is genuine current-neighbor arithmetic
feedback; it is not a frozen prime label. It does not remove the
noninteracting transport family proved above.

The last two rows are instances of an exact parity contrast. For any
composite N at odd site 1, let ell be its least prime factor. The first
divisor after 1 is ell, so E gives ell at 0 and N/ell at 1. The next
layer gives ell at −1 and N/ell at 2. Both are nonunit. Subsequently the
left odd prime travels left and the right even integer travels right;
their layers never meet. At macrostep m>=1 their sites are 1−2m and 2m,
with gap 4m−1. Neither this growing gap nor the change from one to two
sites can be removed by spatial translation. Thus the odd composite
singleton has no positive quotient return, unlike the even singleton
of the same N. Arithmetic can distinguish a channel, but the full frozen
owner retains both channels; selecting the odd one would change it.

For the distinct swap-only control C_swap(a,b)=(b,a), retain the same
layers, state space, spatial quotient and unit clock. All even-site
configurations have the same right transport as in Proposition 3, and
all odd-site configurations have left transport regardless of their
integer contents. The first two table rows (isolated 4 and 6 at even
site 0) are unchanged.
But the adjacent-2 input stays at (0,1) after E and ends at (−1,2) after
O, unlike FRL01's adjacent pair at (−1,0). Thus arithmetic changes the
interaction, while the unwanted return mechanism already exists in a
nonarithmetic swap rule. This is the decisive PROVES_TOO_MUCH control.

For the unquotiented comparison, all Proposition 3 configurations satisfy
F^m w=S^{2m}w. Finite nonempty support excludes F^m w=w for every m>0.
Their ordinary unit suspensions upstairs are lines, not circles. The
odd-prime family similarly travels by −2m. Quotienting is responsible
for these relative-return circles; it is not evidence of spatially
closed motion in the original lattice. Conversely, the frozen quotient
really does own its circles: the stop is not a claim they are fictitious.

There are no cutoff or floating-point precision assumptions. Infinite
families are proved by (2), not inferred from the finite table. A full
periodic census, physical operation-cost model and geometric lift remain
absent. Altering the quotient, clock, ordering or allowed states would
require a new card and would not repair FRL01 under its old identity.

## 6. Gate assessment and decision

| Gate or obligation | Evidence and disposition |
| --- | --- |
| T0 full owner | Established: bijections, full quotient, Hausdorff complete flow and repetitions |
| T1 executed arithmetic | Exact neighboring factor redistribution established; naturalness OPEN |
| T1 prime/clock target | Scoped FAIL: all integers have transport packets and all prime times equal 1 |
| T2 prime subledger | Complete: exactly two circles per prime charge, one for each parity |
| T2 full-target dictionary | Scoped FAIL: composite primitives and infinite fixed-charge multiplicity |
| Remaining periodic classification | OPEN; deliberately not pursued after decisive failure |
| T3 | NOT SUPPLIED / NOT ADVANCED |
| Classical A0/A1/A2 | NOT APPLICABLE; no classical symplectic lift supplied |
| Formal Route coordinates | UNASSIGNED / NOT EVALUATED |
| Route B | NOT INVOKED |

**Portfolio: stop this candidate's target promotion and fork.** The
decisive reason is that coherent all-integer transport, converted into
returns by the declared quotient, survives the arithmetic interaction.
It supplies composite primitives and uncontrolled packet multiplicity
before any hoped-for prime clock can be derived. Neither the complete
prime-charge classification nor the real local interaction establishes
natural A0 or a later Route result.

The reusable design constraint is specific: a neighboring arithmetic
rule needs to distinguish the complete transported configurations, not
only exhibit an interesting collision. No impossibility theorem for all
reversible arithmetic lattices, spatial quotients or conservative lifts
has been proved. This result does not justify deleting separated tokens
or putting a logarithmic roof on them.

## Reproducibility, review and disclosure

Definitions and stop rules are in the [frozen card](candidate-card.md);
claim scopes are in the [ledger](claim-ledger.md). The
[evidence index](evidence/README.md) records source comparisons, exact
controls, review and document checks. All mathematical inputs are the
displayed elementary definitions; no external theorem or finite census
is used to prove the infinite statements.

This is AI-assisted construction and proof checking. Root independently
derived the propositions; a bounded scout supplied the first three local
control rows; a separate native worker reviewed the raw card before
seeing the paper and supplied the general odd-composite contrast, which
root checked and integrated. Same-family model review is not external peer review
or evidence of independent error processes. The package is Markdown-only;
no publication, formal Route evaluation or restart of paused 241/242
was undertaken. The broader search goal remains active.
