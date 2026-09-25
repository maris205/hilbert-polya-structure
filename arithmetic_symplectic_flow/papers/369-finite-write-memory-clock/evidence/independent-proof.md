# Independent raw-card proof — finite-write product-memory clocks

Candidate `ANG-AUDIT-20260921-FWM01`; 2026-09-21; fifth round.
Author `/root/algebraic_henon_author`; internal AI, `NOT_CALIBRATED`.
Sole scientific input: [card](../candidate-card.md), all 81 lines through EOF,
SHA-256 `8ca58d59d6498503a344e749c96bd28201e7c0684d3ad8022ce823bad3ce64a5`,
checked at CP1 and read completely again after root's explicit mathematics release.
No main manuscript, peer/scout evidence, other new science, web or numerics read.
Previously fully read ARS instructions reused; shared history and the card's
disclosed anticipation preclude a blindness or discovery-priority claim.

## 1. Complete owner and every-Borel finite-write IMAGE

The countable discrete factors make Omega and X standard Borel spaces.
The full product probability exists; mu is sigma-finite since each q-fibre has
finite mass m(q). No nonatomicity assumption is needed or inferred for this class.
Existence of the actual bijection and both complete chart partitions is a
hypothesis, not a conclusion from a guessed inverse. Its inverse is Borel:
on each specified image piece it swaps (r,b,eta) back to (q,a,eta).

For a chart D,a,b, write P_D(a)=product_(s in D) pi_s(a_s), and similarly
for b. For EVERY Borel E in that chart, its outside-tail image C is Borel,
and product disintegration gives

    mu(E)=m(q) P_D(a) nu_(D^c)(C),
    mu(F E)=m(r) P_D(b) nu_(D^c)(C).

Thus J=m(r)P_D(b)/(m(q)P_D(a)) is strictly positive and finite and
mu(F E)=integral_E J dmu. The calculation applies when C is null; it never
divides by its measure. Countably summing over the source partition, whose
images are disjoint, proves this identity for every Borel E subset X.
The same proof on the inverse partition gives its own IMAGE J(F^-1 x)^(-1).
All specified chart values remain assigned at every point, not merely a.e.

## 2. Finite relative products, repeated writes and every integer history

For x=(q,omega), y=(r,eta) differing at only finitely many sites, define

    R(x,y)=m(r)/m(q) * product_(s:omega_s!=eta_s) pi_s(eta_s)/pi_s(omega_s).

This is a finite relative product, not a quotient of infinite configuration
weights. Adding unchanged sites to its product contributes only factors one.
For three finite-difference configurations, take the finite union of their
changed sites; coordinatewise cancellation proves R(x,z)=R(x,y)R(y,z).
The actual chart prescription above equals R(x,Fx), including any superfluous
written sites whose final symbol equals their initial symbol.

Every finite positive or negative history changes only the finite union of
the sites actually written in its steps. Define J_0=1; products of the forward
or inverse chart factors therefore give, for EVERY k in Z and every x,

    J_k(x)=R(x,F^k x),
    J_(k+l)(x)=J_k(x) J_l(F^k x),       c_k(x)=-log J_k(x).             (1)

Repeated writes cancel site by site, even when intermediate symbols differ
and the update rule inspects all untouched memory. This proves chart and
history consistency at all points. All these functions are Borel from their
countable chart construction and finite composition. The one-step IMAGE law
extends to integration of nonnegative Borel functions by simple approximation;
composition and the inverse law then prove

    mu(F^k E)=integral_E J_k dmu                         for every Borel E. (2)

No infinite energy, infinite-time update or configuration-measure ratio was used.

## 3. Full action kernels, isotropy, incoming histories and real phase

Keep action arrows (x,k): x->F^k x, with actual labels k. Then exactly

    ker c = { (x,k): R(x,F^k x)=1 };
    ker lag = { (x,0): x in X };
    ker c intersect ker lag = ker lag.                              (3)

The first set contains only actual iterates; equal relative weights or finite
configuration difference do not create an arrow between different F-orbits.
Let Gamma_x={k:F^k x=x}. Either Gamma_x={0}, or Gamma_x=pZ for the least
positive source period p. Equation (1) gives J_k=1 and c_k=0 for EVERY
k in Gamma_x. Consequently H_x={0} everywhere. Source cycles need not vanish.
Extension isotropy at each (x,h) is the WHOLE Gamma_x, since all its clocks
are zero; no effective or germ quotient may discard these loop labels.

Every source has the unique incoming n-step history F^-n x for every n>=0,
with no terminal or missing branch. All integer arrows and all real heights
remain. Translation stabilizer at an extension orbit [x,h] is H_x: equality
after a height translation is exactly an isotropy arrow with that clock.
Thus each actual F-orbit supplies one physical orbit set-theoretically R,
and there are NO positive packets or positive primitive/repetition times.
Explicitly, choose x_0 in one actual orbit; at x=F^k x_0 the coordinate
h-c_k(x_0) is independent of the chosen k because every return clock is zero.
This retains every height and source isotropy, without asserting manifold
topology or combining distinct finite-difference classes into physical orbits.

## 4. TOGGLE — complete own ledger

The two singleton charts 0->1 and 1->0 partition both full source and image;
the inverse is the same toggle. Its own masses are 2/3,1/3, hence IMAGE
J(0)=1/2 and J(1)=2 on every Borel subset, including the empty set.
For any integer k, even k has J_k=1,c_k=0; odd k has c_k(0)=log2 and
c_k(1)=-log2. Thus full ker c consists of all even-lag arrows, ker lag
and the intersection are identities. Each source has Gamma=2Z, H=0 and
extension isotropy 2Z at every height. All incoming histories alternate the
two states. Their ONE physical line has coordinate h at state 0 and h-log2
at state 1. The actual two-cycle and every labelled repetition remain, but
their return clock is zero, so there is no positive primitive packet.

## 5. MOVING-WRITE — complete own ledger

For each n and bit a, the chart has source token n, D={n}, specified bit a,
and ALL outside configurations. Its image has token n+1 and bit 1-a at n;
these countably many pieces partition both source and image. The full inverse
is (n,eta)->(n-1,eta with bit n-1 flipped). Its own product measure gives
J(n,eta)=2^(2 eta_n-1) on every chart and every Borel subset.

For k>0 put I(n,k)={n,...,n+k-1}; for k<0 put I(n,k)={n+k,...,n-1};
I(n,0) is empty. F^k moves the token to n+k and flips exactly these sites once.
The forward or inverse product law gives, for every configuration and k,

    J_k=2^[sum_(s in I(n,k)) (2 eta_s-1)],
    c_k=[sum_(s in I(n,k)) (1-2 eta_s)] log2.                        (4)

Full ker c comprises exactly the arrows whose indicated interval has equal
numbers of zeros and ones, including the empty interval. Nonzero balanced
histories are genuine zero-clock arrows, not returns: the token has moved.
Ker lag and the intersection are identities. The token forces Gamma={0},
so extension isotropy is trivial and H=0 everywhere. Every positive incoming
depth exists by the displayed inverse, with all untouched memory retained.
Each actual orbit has exactly one token-zero representative (0,xi), namely
F^-n(n,eta). Therefore all source orbits are parametrized by the FULL Omega;
each supplies one physical line with coordinate h-c_n(0,xi). The physical
orbit set is set-theoretically Omega times R. No finite-difference quotient,
memory deletion, positive packet or unowned extra clock is involved.

## 6. NONATOMIC-PREFIX — complete own boundary ledger

Its own full binary product gives each length-m cylinder mass 2^-m and each
individual infinite path mass zero. Both prefix maps are defined on the entire
space and have every-Borel IMAGE 1/2, by product independence and measure
uniqueness from cylinders. Replacement v eta->u eta has every-Borel IMAGE
2^(|v|-|u|), so the all-point clock on actual lag triples is c=k log2.
Therefore full ker c=ker lag is the entire synchronized-tail zero-lag relation;
their intersection is the same relation, not merely identities.

A nonzero isotropy lag exists exactly when the source tail is eventually
periodic. Its least eventual edge period l generates all source isotropy lZ;
the period lags form a subgroup of Z with least positive element l.
Then H=l log2 Z and extension isotropy is trivial. Aperiodic sources have
trivial source/extension isotropy and H=0. Every source orbit contains exactly
all legal finite prefixes of all its forward tails. For periodic sources,
two such orbits agree iff their primitive period words agree up to rotation,
as follows by aligning their common infinite periodic tails.
Thus EVERY primitive binary necklace gives one physical packet of least time
l log2, with powers only repetitions r*l log2; all incoming prefixes, null
periodic paths and real phases remain. Aperiodic source orbits give lines.
Each positive packet retains the complete phase set R/(l log2)Z.
The two constants give two log2 packets; for each l>=2 the word a^(l-1)b
is primitive because b occurs once, and gives composite index 2^l.
This owner is outside the theorem's class: its shift is not bijective and
prefix branches reindex the full tail, not finitely many fixed memory sites.

## 7. Scoped stop

The conditional full finite-write owner has exact IMAGE and clock, but H=0
at every entire-source return. STOP target promotion for this class. This does
not construct an arithmetic candidate, classify all source cycles, assume all
product owners nonatomic, or exclude different long-memory measured owners.
Strong naturalness OPEN; T3 NOT AUDITED; classical NOT APPLICABLE; formal
UNASSIGNED; B NOT INVOKED. Fifth-round receipt only; no sixth-round work.
