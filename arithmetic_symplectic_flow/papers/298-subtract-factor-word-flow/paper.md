# Subtract-and-factor words: an owned image clock with composite primitive times

Candidate ID: `ANG-20260920-SFW01`.
Paper ID: `298-subtract-factor-word-flow`. Date: 2026-09-20.
Status: `OWNED WORD IMAGE CLOCK; COMPOSITE FIXED-CORE TIMES — STOP / FORK`.
Result type: exact measured-owner construction and decisive fixed-family audit.

## Abstract

On all infinite words of integers at least two, replace the first pair
by the complete ordered factor word of their difference, with a stated
equal-input convention. The full product measure assigns n probability
1/[n(n-1)]. The resulting surjective local homeomorphism has an owned,
continuous full-point IMAGE clock and a complete real time action.
The first frozen fixed-core family already fails the target: its cores
are p^infinity and (p,2p,2p,...), for primes p, with least times
log[p(p-1)] and log[2p(2p-1)] respectively. In particular log 6 is
primitive, not a repeat inferred from a factorization of 6. Turning
factorization off adds integer-indexed cores; changing the full measure
changes actual packet times without identifying packets. We stop here,
preserving all states and leaving other returns unclassified.

## 1. Frozen object and lineage

The original [card](candidate-card.md) has SHA-256

    10b23181087e28469c7490e4dc3ae5cc018eb274ed4684a7482d3d0add762ecd

It freezes the definition supplied without results in
[297's scout record](../297-real-feedback-scale-flow/evidence/scout-record.md).
Let X={2,3,...}^(N_0) with its full product topology. Define

    q(a,b)=a if a=b, and abs(a-b) otherwise,
    T(a,b,eta)=fct(q(a,b)) concatenated with eta,
    nu(n)=1/[n(n-1)], mu=nu^(N_0).

Here fct(d) is the complete ascending divisibility-atom factor word,
with multiplicities, and fct(1) is empty. All source symbols, words,
empty-output branches and infinite tails remain. The equality rule,
factor ordering and product measure are declared design choices.

| Same-object item | Frozen owner | Boundary |
|---|---|---|
| Arithmetic source | Current-pair subtraction and factor-word replacement on ALL X | No prime alphabet restriction or fixed integer component |
| Measure | Full all-integer product law mu | Not claimed invariant or uniquely natural |
| Arrows | Entire retained-lag tail groupoid of T | No free prefix arrows, swaps or selected histories |
| Clock | Negative log of this measure's actual IMAGE derivative | Not a supplied log-prime roof |
| Packets | Full time stabilizers and actual tail/time equivalence | Same length or integer factorization does not merge packets |
| Analytic / classical geometry | NOT SUPPLIED / NOT APPLICABLE | Non-locally-compact symbolic owner, not a symplectic suspension |

The [prior-work](../../docs/prior_work/README.md) arrow is divisor/factor
observables -> current integer subtraction -> variable-length symbolic
rewriting -> that same source's measured time. This is a stated
symbolic deformation, not a Logistic/Henon conjugacy or conservative
lift. [225](../225-euclid-edge-scattering/candidate-card.md) has a finite-word
graph/port owner, [269](../269-factor-redistribution-lattice/candidate-card.md)
a product-preserving lattice action, and
[296](../296-factor-compare-remove-flow/candidate-card.md) a different
comparison/removal action and declared unmeasured scale. No old clock,
packet theorem, source lock or Route result transfers.

No prime table, per-prime choice, Mangoldt weight, Riemann-zero data
or supplied return length enters. Factoring cost is not identified
with elapsed physical time. Naturalness of these designs stays OPEN.

## 2. Full source, branches and measure

**Proposition 1.** The arithmetic rule is defined on all X. X is
Hausdorff and nowhere locally compact. T is a surjective local
homeomorphism with exactly the displayed inverse branch on each
first-pair cylinder. The measure mu is a full-support, nonatomic
probability measure with the prescribed finite-prefix weights.

*Proof.* A divisibility atom at 1 is exactly an integer with no
proper nontrivial divisor. For any d>=2, repeatedly divide by the
least divisor greater than one. Each chosen divisor is an atom;
the positive quotient decreases until it is one. A smaller atom
cannot appear at a later step, since it would already divide the
earlier integer. This constructs the finite ascending factor word,
whose product is d. All its entries lie in the source alphabet.
Uniqueness follows from the elementary prime-divisor lemma: if p
does not divide a, the Euclidean algorithm gives up+va=1, so
p|ab implies p|b. Cancel common prime factors inductively and
then sort to obtain the same word.
For a!=b, q>=1; for a=b, q=a>=2. Thus the frozen operation,
including its empty-output case, is everywhere defined.

Every finite cylinder in X is clopen and projects onto the full
infinite discrete alphabet at an unused coordinate, so it is not
compact. A compact neighbourhood would contain a cylinder closed
inside it, a contradiction. Hausdorffness follows from the discrete
product. No finite alphabet is substituted.

On C(a,b), let w=fct(q(a,b)). Deleting the first two symbols
and adjoining w is a homeomorphism onto the clopen C(w); the
inverse deletes that precise w prefix and adjoins (a,b). This is
also valid when w is empty and C(w)=X. The (2,3) branch has
q=1 and maps onto all X, proving surjectivity.

Since nu(n)=1/(n-1)-1/n, its sum over n>=2 equals one.
The countable product probability has cylinder weights
mu(C(v))=product_(d in v)nu(d). Every nonempty open set contains
a positive-weight cylinder, proving full support. Each nu(n)<=1/2,
so any length-L cylinder has mass at most 2^(-L). Nested prefixes
therefore give zero mass to every singleton. QED.

In particular the returning words below are null points, not omitted
states. Nonatomicity is distinct from lack of full support.

## 3. Actual Borel IMAGE law and full time owner

Write v(w)=product_(d in w)nu(d), with v(empty)=1. For a
single actual inverse branch h_(a,b):C(w)->C(a,b) set

    R(a,b)=nu(a)*nu(b)/v(w),
    L(x)=-log R(a,b), x in C(a,b),
    L_m(x)=sum_(0<=i<m)L(T^i x), L_0=0.

**Proposition 2.** For every Borel E subset C(w),

    mu(h_(a,b)(E))=R(a,b)*mu(E).

The full retained-lag topological groupoid has the unique continuous
full-point IMAGE version

    J(x,m-k,y)=exp(-L_m(x)+L_k(y)),
    c=-log J=L_m(x)-L_k(y).

Its extension owns a jointly continuous complete real-time action.

*Proof.* Adjoining a finite word v to an arbitrary Borel tail set
A multiplies its product measure by v(v). Apply this with prefixes
w and (a,b) to obtain the displayed identity. Equivalently it
holds on cylinders and extends to all Borel sets by finite-measure
uniqueness. This is an INVERSE image factor; the forward branch
factor is its reciprocal, not R.

T's actual local inverses and their finite compositions supply
open inverse-branch-pair charts for G_T={(x,m-k,y):T^m x=T^k y}.
When chart presentations overlap at equal lag, extending both
iterate counts together along the same terminal word gives compatible
refinements. Composition aligns intermediate counts; inversion reverses
the branches. Source and range are local homeomorphisms. This uses
no local compactness or locally compact analytic groupoid theorem.

Composing the proved Borel branch identities on these charts gives
J=exp(-L_m(x)+L_k(y)) for the map y->x. For two presentations
of the SAME arrow, the longer one adds identical common terminal
factors to both sides, which cancel. The same alignment argument
under composition proves multiplicativity of J and additivity of c.
L depends only on the first pair and is locally constant. Each
finite L_m is locally constant, so the chart function c is continuous.

On a chart, two continuous versions of the IMAGE derivative must
coincide: a nonzero difference at a point persists on a nonempty
open source subset, which has positive mu by full support, contrary
to equality of the Borel measure identities. This owns the clock
at EVERY arrow, including arrows through singleton-null fixed words.

The extended chart (y,u)->(x,u+c) is a homeomorphism between
open subsets of X x R. Saturations of open sets are open, so
the orbit projection is open. Real translations commute with all
arrows; the product of this open quotient map with the identity
is quotient. Hence the descended time action is jointly continuous,
and every real t is allowed, giving completeness. QED.

The sign convention can also be checked directly: the derived map
T_tilde(x,u)=(Tx,u-L(x)) has m-th iterate
(T^m x,u-L_m(x)). Equality of two such iterates is exactly base
tail equality and u=v+L_m(x)-L_k(y), the SAME extended arrows
including lag. No second clock has been attached.

There is a useful global positivity check. Put
K(d)=product_(p in fct(d))p(p-1), K(1)=1. For d>=2,
K(d)<=d(d-1), since product_(p in fct(d))(p-1) is a positive
integer strictly less than d. With A=min(a,b), B=max(a,b),
one has q<=B and K(q)<=B(B-1), also when q=1. Therefore

    R(a,b)=K(q)/[a(a-1)b(b-1)] <= 1/[A(A-1)] <= 1/2,
    L(x)>=log 2.

This proves a uniform positive branch clock, not a classical
symplectic roof or a Hausdorff/embedded-circle theorem for the quotient.

## 4. The frozen fixed head/constant-tail family

Let x_(a,b)=(a,b,b,...) for a,b>=2.

**Theorem 3.** Its fixed members are precisely

    x_(p,p)=p^infinity and x_(p,2p)=(p,2p,2p,...), p prime.

At each such member the full source isotropy is the lag Z,
fixed-object extension isotropy is trivial, and

    H_(p,b) = log[b(b-1)] Z, b=p or 2p.

All these fixed cores represent different primitive time packets.

*Proof.* Write w=fct(q(a,b)). The fixed equation is
w concatenated with b^infinity = a concatenated with b^infinity.
If w is empty, it requires a=b, but empty output has q=1 and
a!=b. If w is nonempty, its first letter is a, forcing a to
be an atom, hence a prime p. If w had length at least two,
its second letter would be b, so q=product(w)>=ab>max(a,b).
This contradicts the actual q rule. Thus w=(p) and q=p.
The solutions are b=p from equality or b=2p from |p-b|=p;
the other algebraic solution b=0 is outside the frozen alphabet.
Both displayed families do satisfy the fixed equation.

At either fixed core, w=(p), so R(p,b)=nu(b). Every integer
lag occurs, and every equal-tail presentation gives
c=(m-k)*log[b(b-1)]. This is the ENTIRE time group, not one
chosen loop. Its least positive element is log[b(b-1)], and
repeats have ell times this same period. Injectivity of this clock
on the lag Z gives trivial fixed-object extension isotropy.

Different fixed words never have a common forward tail. Determinism
also prevents any finite preimage from joining distinct fixed cores;
the full groupoid is already exactly the common-tail relation.
Real-time translation changes no base word. Thus distinct listed
cores remain distinct packets; all real phases of a given core
belong to that one packet. QED.

The constant p=2 core has least time log 2, but the constant
p=3 core has least time log 6. It is an independent primitive,
not a repeat produced by multiplying labels 2 and 3. More generally
p(p-1) is composite for p>=3. The (2,4,4,...) core has least
time log 12, and every 2p(2p-1) is composite. These are exact
primitive obstructions to the ordinary-prime-time target.

We STOP target promotion here. This theorem classifies only the
fixed members of the frozen family and their complete isotropy;
it does NOT classify nonfixed family members, eventual returns,
other fixed words, higher periods or the full returning locus.
No claim that a particular prime time is globally absent is needed.

## 5. Precommitted controls and ownership checks

**FACTORIZATION-OFF.** Replace
fct(q) by (q) for q>=2 and by the empty word for q=1, using
the SAME full X and mu. Each branch is again an actual prefix
homeomorphism. Its OWN inverse IMAGE factor is nu(a)nu(b)/nu(q)
when q>=2 and nu(a)nu(b) when q=1. The same finite-branch
proof establishes its full clock/time owner; no main J is borrowed.

Its fixed head/constant-tail members are exactly (a,a,a,...)
and (a,2a,2a,...) for every integer a>=2: nonempty fixed output
must be the single symbol a, so q=a, and the empty case still
fails. Each has H=log[b(b-1)]Z and all different fixed cores
remain different packets. In particular constant 4 and (2,4,4,...)
are TWO different least-log-12 primitives in this comparator.
This is not a complete comparator return census.

**MEASURE-CHANGE.** Keep the main T but set nu_0(n)=2^(1-n).
Its sum is one; all cylinder weights are positive and each symbol
mass is at most 1/2, proving full support and zero singleton mass.
The SAME product-prefix argument, now for mu_0, gives its own
R_0=nu_0(a)nu_0(b)/product_(d in w)nu_0(d) and continuous
full-point clock. The fixed cores are unchanged because T is.
There R_0(p,b)=nu_0(b), so their least times are (b-1)log 2.
In particular the constant-3 primitive has time 2 log 2 but is
NOT the second traversal of the distinct constant-2 packet. A
change of full measure changes the time action, not the tail identity.

**Empty and composite branch controls.** The main (2,3) inverse
chart inserts that pair into any word, with J=1/12; its positive
clock is log 12. This chart identity alone is not a periodic-orbit
claim. At input (4,4), the main output prefix (2,2) gives J=1/36,
whereas FACTORIZATION-OFF's output (4) gives J=1/12. Neither
main clock value is silently turned into a return of constant 4.
The main (2,2) chart has J=1/2, agreeing with the independently
proved fixed constant-2 period.

| Control | Exact finding | Limit |
|---|---|---|
| Main constant-prime cores | log[p(p-1)] primitives | Prime symbols do not imply prime times |
| Main (p,2p,2p,...) | log[2p(2p-1)] primitives | Composite tail symbols and full core identity retained |
| FACTORIZATION-OFF | Integer-indexed fixed families, including two log-12 cores | Own branch clock; no full comparator return classification |
| MEASURE-CHANGE | Same fixed cores, least times (b-1)log 2 | Coincident repeat lengths do not merge packets |
| Empty-output and composite charts | Correct own IMAGE factors on all Borel subsets | Branch lengths are not automatically periods |
| Singleton-null fixed words | Unique continuous clock follows from full support | No atom-mass or conull deletion argument |

The demonstrated PROVES_TOO_MUCH issue is extra composite primitive
times and their survival under factorization removal, not arbitrary
data universality. Source, equality convention, factor ordering and
measure naturalness remain OPEN. No measure is retuned after failure.

## 6. Gate decision and reproducibility

T0 and the full measured-clock ownership part of T1 are established,
with a nowhere locally compact source and complete continuous time.
T2 establishes the exact frozen fixed family and repetitions, but
the prime-time target FAILS by composite primitives. The remaining
return ledger and coarse quotient topology are OPEN / NOT PURSUED.
Stronger naturalness is NOT ESTABLISHED. T3 NOT SUPPLIED / NOT
PURSUED; classical A0/A1/A2 NOT APPLICABLE; formal coordinates
UNASSIGNED; Route B NOT INVOKED.

Portfolio: **stop target promotion / fork search**. The same-object
ledger is intact: all words, measure, empty branches, clocks and
packet identifications remain unchanged. No higher-period search,
prime-only restriction, alternate measure adoption or analytic rescue
follows this decisive test. A different architecture needs a fresh card.

The [claims](claim-ledger.md), [evidence](evidence/README.md),
[internal review](evidence/independent-review.md) and
[definition provenance](evidence/scout-record.md) record exact inputs
and boundaries. Proofs use integer divisibility, product measures,
actual local charts and exact word equations, with no scientific
numerical run, cutoff, fitting or external literature campaign.
ARS/AI-assisted same-model internal review is not external peer review,
formal verification or independent-error evidence. Old packages and
mirrors unchanged; 241/242 paused; programme goal remains active.
