# Independent class proof — reversible uniform inverse-limit clocks

Audit: `ANG-AUDIT-20260921-RUI01`; not a new Hénon candidate.
Standing: the full specified reversible uniform clock is identically zero;
positive primitive time is absent for this clock class. Three controls owned.
Internal proof: `NOT_CALIBRATED`, not external peer review or novelty evidence.

## 1. Exact input, exposure and scope

I personally read candidate-card.md lines 1–116 through authorized EOF,
including the uniform-measure clarification, and measured SHA-256
`3db55fb8bbb9b89882c54ba893f06232dd6977aadcd5370be725cc932baed568`.
It was the sole new scientific input. No author manuscript, peer, scout,
old283 or other historical scientific file was read. No network, scientific
code, numerical experiment, auxiliary agent or model change was used.
ARS router/DA/runtime/workflow guidance is retained from prior complete reads.
Shared history and the card's explicit prior-mechanism disclosure prevent
blindness or independent-error claims. I sent the mathematical conclusions
to root before writing. No unread manuscript review is claimed here.
The following proves the abstract class and its controls directly; the named
Hénon example is not represented as a newly discovered mechanism.

## 2. The complete inverse system and its own measure

Give each finite X_l the discrete topology. The inverse limit is the closed
compatibility subset of the countable compact product, hence compact and
metrizable. Surjective bonding maps give every finite coordinate a compatible
extension. If r_l is the common fibre size, |X_(l+1)|=r_l |X_l|, and
the uniform mass above an atom of X_l is r_l/|X_(l+1)|=1/|X_l|.
For an explicit probability construction, partition [0,1) into |X_1| equal
half-open intervals, then partition each parent interval into r_l equal
children labelled by its bonding fibre. Each parameter determines a full
compatible path; the coordinate maps are measurable. The pushforward of
Lebesgue probability assigns each level-l cylinder mass 1/|X_l|.

The level-cylinder atoms, with empty set and X, are a pi-system: cylinders
from different levels are disjoint or their intersection is the deeper one.
They generate the full Borel sigma-algebra. Thus the probability is unique,
and every nonempty open set has positive measure. A point has mass
lim_l 1/|X_l|; null points are retained when that limit is zero.
This is UNIFORM inverse-limit measure, not automatically Haar on a set.
If the finite sets are compatible groups and the bonding maps are group
homomorphisms, cylinder translations preserve it; it is then normalized Haar
on the resulting compact group. No group structure is invented otherwise.

Compatibility and bijectivity imply
pi_l F_(l+1)^(-1)=F_l^(-1) pi_l. Hence F and its coordinatewise inverse
are full homeomorphisms of X, with all signed iterates defined everywhere.
For every integer n, F^n C_l(x)=C_l(F^n x), not merely a containment.
Every prescribed finite-level IMAGE ratio is therefore exactly 1. The limit
J_n(x)=1 exists at EVERY x, including null periodic or fixed points.
The finite measures E->mu(F^n E) and mu agree on the generating pi-system,
so mu(F^n E)=mu(E)=integral_E J_n dmu for EVERY Borel E.
Composition and inverse coherence are exact; c(n,x)=0 on ALL arrows.

## 3. All source groups, incoming and physical time in the class

Let q_l(x) be the least period of x_l under its finite permutation F_l.
Then q_l divides q_(l+1), and the ENTIRE source isotropy is
Iso_x=intersection_l q_l Z.
If these integers are bounded they stabilize at q and Iso_x=q Z; otherwise
Iso_x={0}. This characterizes every point without a high-period census.
The full clock kernel is the entire retained Z-action groupoid. Every H_x
is {0}, and extension isotropy equals Iso_x, not necessarily the identity.
All incoming arrows to x have sources F^(-n)x, for all integers n. Each
source orbit retains exactly its two-sided iterate orbit and its actual lag
labels. Extension classes over it have the unchanged real height as phase.
Height translation is complete and commutes with every extension arrow;
no nonzero translation returns a class. Source cycles are not positive
physical cycles. No unit roof or deletion of ineffective isotropy is allowed.

## 4. SCALAR-INDEX: own partial action and complete ledger

Multiplication by a nonzero integer is injective on K: dx=0 modulo dN
implies x=0 modulo N for every N. Thus all stated divisions by 6^m exist
uniquely on 6^m K. The arrows are the full reduction to K of the ambient
integer-power action; composition is (j,6^k x) after (k,x) -> (j+k,x)
when both arrows are legal, and inverse is (-k,6^k x). No intervening
illegal step is silently added. Positive k need not give an onto map of K.

For x in D_k, C_l(x) intersect D_k is x+L K, where L=l! for k>=0 and
L=lcm(l!,6^{-k}) for k<0. Its image is 6^k x+(6^k L)K. Both moduli here
are positive integers. The masses are 1/L and 1/(6^k L), so their ratio
is 6^{-k} for EVERY l, before taking any limit. Integer subgroup indices
and uniqueness of Haar on the subgroup also give
h(6^k E)=6^{-k}h(E) for every Borel E subset D_k.
Consequently its own all-point J_k=6^{-k}, c(k,x)=k log 6; the inverse
and composition laws agree. The full clock kernel has only k=0 identities.

At zero the entire source isotropy is Z and H_0=log 6 Z. The least positive
time is log 6, with repetitions k log 6, and extension isotropy is zero.
At nonzero x, an equation 6^k x=x for k!=0 would imply
(6^{|k|}-1)x=0 after clearing division, impossible by integer injectivity.
Thus all nonzero source isotropy and H are zero, not just on integer seeds.
All incoming to x are (k,6^{-k}x) whenever 6^{-k}x is integral. Negative
powers from x are allowed through depth min(v_2(x),v_3(x)), possibly infinity;
zero components and noninteger states are therefore included exactly.
For a nonzero orbit anchor a, every object is uniquely 6^n a when integral,
and the complete phase is h-n log 6. For the zero orbit it is h mod log 6.
Zero has no nonzero incoming object. This null source's positive clock is
fixed by its cylinder ratios, not reassigned. The control lacks the class's
global bijective finite permutations and does not contradict the theorem.

## 5. BINARY-SHIFT: actual prefix clocks and all eventual cores

Both prefix maps eta->0eta and eta->1eta are complete inverse branches.
For arbitrary finite words u,v the replacement v eta -> u eta has ratio
2^{|v|-|u|} at every cylinder depth. For every Borel tail set E, the product
measure identity mu(wE)=2^{-|w|}mu(E) proves the corresponding EVERY-Borel
law, including null subsets. Its actual arrow is (u eta,|u|-|v|,v eta),
so c=lag times log 2. Any two presentations of the same triple have the
same lag; composition adds lags, proving all-point descent and coherence.
All arrows are covered by these prefix charts with their actual common tails.
One cannot put one IMAGE multiplier on the noninjective shift on every set:
the mass ratio is 2 on a one-letter cylinder but 1 on the whole space.

The FULL c-kernel is the nontrivial synchronized-tail relation
{(x,0,y): sigma^m x=sigma^m y for some m}, not merely identities.
An eventual tail with least period q has entire source isotropy q Z and
H=q log 2 Z. A noneventually-periodic point has both groups zero. Indeed
a nonzero isotropy lag is exactly an eventual periodicity relation, and
the least tail period divides every such lag and realizes all its multiples.
Extension isotropy is zero everywhere, since the character is injective on
isotropy. Thus the positive primitive is q log 2, not the length of a
nonprimitive repeated word or of an arbitrary preperiodic prefix.

Choose a primitive periodic representative eta of least period q. Its ENTIRE
source orbit consists of all u sigma^j eta, with finite u and 0<=j<q.
Their complete phase is h-(|u|-j)log 2 modulo q log 2; different choices
change it by exactly that lattice. Distinct primitive necklaces never share
a tail and never merge. Noneventual source orbits are all finite prefixes
of all forward tails of an anchor a; the unique lag in an arrow (x,k,a)
gives the real phase h-k log 2. These formulas include all incoming.

Let P_q count binary words of least period q. Then
2^q=sum_{d|q} P_d, so P_q=2^q-sum_{d|q,d<q}P_d.
There are exactly P_q/q primitive packets of time q log 2, because each
least-period necklace contains q words. In particular q=1 gives two distinct
log 2 packets, not one. All eventually periodic sources form a countable
Bernoulli-null set; none is discarded or assigned a different clock.

## 6. HENON-EXAMPLE: own full inverse and zero physical time

Over K and over EVERY ring Z/l!Z, substituting the two polynomial formulas
gives H^{-1}H=HH^{-1}=identity, where H^{-1}(u,v)=(u^2+1-v,u).
Reduction commutes with both formulas; thus each finite H_l is a permutation
and the projections have equal fibres of size (l+1)^2. Their uniform limit
is product additive Haar, identified by translation-invariant cylinders.
Its own two-coordinate cylinder IMAGE ratios are exactly 1 at every depth,
and the generating-class argument gives its EVERY-Borel Haar law. Hence
J_n=1, c=0, all H_x=0, the full kernel is all arrows, and extension isotropy
is the full source isotropy, computed by intersection of its finite-period
lattices as in section 3. All incoming are H^{-n}x and phase is height.
For example (1,1) is fixed, with source isotropy Z but physical H=0.
No longer-period enumeration, source conjugacy or new prime-generator claim
is needed or inferred. This is an owned example of the previously identified
mechanism, not a first discovery of the283 result or a reuse of an unread proof.

## 7. Adverse scope and stopping decision

The theorem stops the specified full uniform inverse-limit IMAGE clock,
not reversible dynamics equipped with other physical clocks. Missing an
all-level bijection, compatibility or the frozen uniform measure puts an
application outside the theorem; a finite-depth check cannot supply it.
Scalar and binary controls demonstrate the necessity of distinguishing
onto reversibility, partial invertibility, branch laws and whole-map laws.
No claim is made about358's different content-division source. The class is
a conditional lineage filter, not automatically prime admissibility, T3 or
a conservative geometric lift. Strong naturalness remains OPEN; classical
A0/A1/A2 are not applicable, formal Route unassigned and B not invoked.

EOF — full class and three controls; independent report frozen.
