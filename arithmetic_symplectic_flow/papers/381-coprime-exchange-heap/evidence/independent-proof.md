# Card-only independent proof — ANG-20260922-CEH01

2026-09-22; batch `FULL-TRANSPORT-20260922-G`, round 2/5.
Verdict: `STOP — COMPOSITE PRIMITIVE CLOCKS; ALL FOUR OWNERS AUDITED`.
Internal shared-history evidence: `NOT_CALIBRATED`, not external peer review.

## 0. Release, input and method

Root explicitly released mathematics after its full CP1 read.
Sole scientific input: original `candidate-card.md`, lines 1–61 through EOF,
read again after release; SHA256
`02da94469ed3289591c192ad93e7f5080ad67b843da9f7f1bc175c0562504136`.
Scope receipt: `scope-review.md`, 74 lines, SHA256
`d7be72329d182920dcc3b39d212b31e10c36ce81b27cf29ad5ce29ff26e563cb`.
No main manuscript, peer, scout, other scientific package, external source,
numerical experiment, auxiliary agent or model change was used.
Prior project authorship/history is shared; independence is from the current
unread manuscript, not a claim of blindness or independently distributed errors.
ARS instruction reads are recorded in CP1; only first-principles finite-word,
probability and groupoid arguments are used below. The decisive result was
sent to root before this report was written.

## 1. Quotients, cancellation and exact enumeration

Work separately with each symmetric, irreflexive exchange relation I:
MAIN: gcd(a,b)=1; FREE-WORD: none; COMMUTATIVE: a!=b;
NONCOPRIME: a!=b and gcd(a,b)>1. Let D be its complementary dependence relation,
including all equal-letter pairs. All statements in this section apply to each
own quotient; they do not identify its classes with another control's classes.

For a word w label each occurrence by (a,r), its letter and its occurrence rank
among that letter. Put a directed relation from each earlier to each later
occurrence with dependent labels, and take transitive closure. This is a finite
labelled poset P(w). Adjacent independent exchanges preserve it: their mutual
edge is absent and every other occurrence remains before or after both.
Conversely, linear extensions of P(w) give precisely the equivalent words.
Indeed w is one extension. To transform one extension into another, move the
first desired vertex left across the preceding vertices. It is incomparable
with each crossed vertex, since the desired extension places it first.
Incomparable vertices have independent labels; these are allowed exchanges.
Remove that first vertex and induct. Equal-labelled vertices form a chain, so
their ranks remain fixed and distinct extensions give distinct label words.
Thus P(w), with occurrence names, is a complete invariant, not an assumed
normal-form theorem. Word length and each letter count descend to the quotient.

Minimal vertices are exactly possible first letters of representatives;
maximal vertices are exactly possible last letters. At most one minimal or
maximal vertex has any given label. Deleting a minimal/maximal vertex yields
the residual heap: such a vertex cannot be an intermediate vertex of a path
between surviving vertices, so induced order equals the residual dependence
poset. Different deleted labels give different residual count vectors.
Consequently L(h) and R(h) are finite, nonempty for h!=e, and enumerated exactly
by minimal and maximal vertices respectively, without multiplicity labels.
For h=e both are empty. Write ell(h)=|L(h)| for nonempty h.

Left multiplication by [a] adds the distinguished first a-occurrence; deleting
it from equality [a]g=[a]g' recovers equal residual posets, hence g=g'.
Right multiplication is cancellative by the last a-occurrence argument.
Successively cancelling letters proves cancellation by any fixed finite heap.
Different appended/prepended letters give different targets by count vectors.
There are countably many heaps. A finite explicit enumeration for any given
heap uses all linear extensions of its finite poset. Let N(h) be their number;
N(e)=1 and N(h)=sum_{g in L(h)}N(g), also with R in place of L.
The recursions count first/last letters disjointly and terminate by length.

## 2. Own initial laws and actual transition probabilities

Let n=|h| and m_a(h) be its multiplicities. In each own quotient,

    pi(h)=2^(-n-1) N(h) product_a rho(a)^m_a(h),  rho(a)=1/[a(a-1)].

All representative words have the same product weight; the N(h) distinct
representatives are exactly the disjoint events being pushed forward.
The telescoping sum of rho over a>=2 is 1. Summing over all heaps at length n
recovers total word mass 2^(-n-1), and summing n gives 1. Every pi(h)>0.
All these values are finite positive rationals. No finite heap is discarded.

Put b(e)=1, b(h)=1/2 for h!=e. The complete, already-merged matrix is

    P(h,h[a])=b(h)rho(a);
    P(h,g)=1/[2 ell(h)] if g in L(h), h!=e;
    P(h,g)=0 otherwise.

Growth/deletion target sets have different lengths. Each growth target has a
unique letter and each deletion target a unique removed label, as proved above.
Thus no further hidden-edge multiplicity is left in this formula. Its rows sum
to 1 and every positive entry is <=1/2. Its reciprocal d(h,g)=1/P(h,g) is an
integer >=2: a(a-1), 2a(a-1), or 2ell(h), according to the transition type.

X is the full legal path subspace of the discrete countable-state product,
with its Borel sigma algebra. The prescribed cylinder masses are consistent
probabilities and define mu: for example, sampling h_0 with pi and then using
independent uniform variables to sample each countable row constructs this law.
Every nonempty legal cylinder has positive mass, proving full topological
support. Every n-step cylinder has mass <=2^(-n), so each point has mass zero.
This keeps, rather than removes, all periodic and other null paths.
No stationarity is used: in fact (pi P)(e)=sum_a pi([a])/2=1/8 != pi(e)=1/2.

## 3. Entire inverse atlas and all-Borel IMAGE

If c can precede h, its step was either growth (c in R(h)) or deletion
(c=[a]h). Conversely every member of these two sets has the required positive
transition. The union is disjoint by lengths; within {[a]h} count vectors
distinguish letters, and R(h) already consists of actual distinct states.
This proves the proposed exact atlas, including h=e. It is countably infinite
at every h. There are no terminal paths, no missing predecessors, and T is onto.
The chart theta_c:X_h -> X_(c,h) prepends c and is a Borel homeomorphism onto
its cylinder. On every point of X_h freeze

    j_c=pi(c)P(c,h)/pi(h)>0.

On every cylinder B in X_h the defining path law gives
mu(theta_c B)=j_c mu(B); agreement of finite measures extends this to every
Borel B by the monotone-class argument. The chart law therefore includes every
null subset; no a.s. replacement or conull restriction is made. Countably many
positive-density inverse charts also prove T is nonsingular in both measure
class directions. The sum of j_c at fixed h is (pi P)(h)/pi(h), not generally 1.
In particular it is 1/4 at e, so these are not inverse transition probabilities.

For own quotient counts the formulas can also be written

    j_h at h[a] = 2 b(h) N(h)/N(h[a]);
    j_h at g, h=[a]g = N(h)rho(a)/[4 ell(h)N(g)].

Both follow by substituting the own pi, not by borrowing MAIN's counts.
The first gives j_e=2, hence local kappa=-log 2. A positive classical roof is
not obtained. All-point versions here are the versions explicitly frozen.

## 4. Finite histories, full kernels and incoming classes

For z=(h_0,h_1,...) put D_m(z)=product_{i<m}d(h_i,h_(i+1)), D_0=1,
W_m(z)=pi(h_0)/D_m(z), and A_m(z)=sum_{i<m}kappa(T^i z). Telescoping gives

    A_m(z)=log[pi(h_m)D_m(z)/pi(h_0)].

If T^m z=T^n y, then on g=(z,m-n,y) the frozen clock is exactly

    c(g)=log[W_n(y)/W_m(z)]
        =log[pi(y_0)D_m(z)/(pi(z_0)D_n(y))].

Two representatives of the same arrow have both m,n shifted by the same
integer. Extending to the larger pair adds the identical common-tail finite
sum to both A's; hence c descends. Aligning the common tails of composable
arrows proves additivity; inverse arrows negate c. This covers all signed lags
using finite products only. No infinite clock sum or stationary law is needed.
The complete kernels, with the shared-tail condition always retained, are

    ker c = {g: pi(y_0)D_m(z)=pi(z_0)D_n(y)};
    ker lag = {(z,0,y): T^m z=T^m y for some m};
    ker c intersect ker lag = the same equality with m=n.

These are explicit rational finite-history tests on every actual arrow, not
only descriptions on periodic points. They include all exceptional/null paths.
They are genuinely different kernels. Prepending [2] to a path starting [22]
has j=1, giving a zero-clock arrow of lag 1 in every owner. Paths starting
([2],e,...) and ([3],e,...) with the same subsequent tail give lag 0 and
clock -log 3. Prefixes (e,[2],e,[3],e) and (e,[3],e,[2],e) with the same tail
give a nonidentity arrow in their intersection, since the transition products
agree. None of these arrows is removed by a choice of representatives.

All incoming finite histories of y are precisely all finite legal state paths
ending at y_0, with that endpoint identified with the start of y. Its full
source orbit allows the same construction at every T^n y, n>=0. This is both
necessary and sufficient by the definition of G. At state level every heap
can be deleted to e and built from e by a representative word, so there is one
communicating state component; this does not identify its many tail orbits.
Closed walks avoiding e remain present, for example [2],[22],[2].

## 5. Entire isotropy, physical phases and primitive packet ledger

If a path is not eventually periodic, its source isotropy is {0}, by the
shared-tail definition. Otherwise its possible integer lags form a nonzero
subgroup dZ of Z; its least positive generator d is the least eventual state
period. A tail beyond the finite stem is a primitive closed state walk
C=(h_0,...,h_d=h_0), unique up to cyclic rotation. Its primitive property is
as a state sequence, not as a word representative of any individual heap.
Conversely each such primitive closed walk, repeated indefinitely, and every
finite incoming stem yield exactly this source-orbit type. Two eventual cycles
belong to the same tail orbit iff their primitive state words are cyclic
rotations: equality of tails gives equality of the repeated state words.

Write D(C)=product_{i<d}d(h_i,h_(i+1)) and L(C)=log D(C)>0. For any incoming
stem the source isotropy element kd has clock kL(C): the common stem cancels
and one cycle telescopes pi back to itself. Thus the complete clock subgroup
H_z=c(Iso_G(z)) is {0} in the nonperiodic case and L(C)Z otherwise.
No other clock periods arise from lag-zero arrows between different paths.

For definiteness let g=(z,k,y) carry (y,t) to (z,t+c(g)). This convention gives
the stated quotient X times R/G; reversing the convention only reverses time.
Extension isotropy is Iso_G(z) intersect ker c, which is trivial everywhere,
although periodic source isotropy dZ is retained and is not itself discarded.
For each full source orbit, all physical phases are R/H_z: transported phase
differences between two choices of incoming arrow are exactly H_z. Vertical
translation has one closed packet of least positive period L(C) for each
primitive closed-state-walk necklace, and no closed packet on any other orbit.
Repetitions have times kL(C), k>=1. All incoming stems and phases belong to this
same packet, not extra selected orbits. This classifies the full countable
closed packet set, including all walks avoiding e and all null periodic paths.
No smooth, Hausdorff or standard-Borel regularity of the orbit quotient, nor
classical suspension, Hamiltonian owner or trace object, is inferred.

## 6. Decisive clocks and independent own controls

Every closed walk has length at least 2: heap length changes by exactly +1 or
-1 at each step. In fact its length is even. Every factor d(h,g) is an integer
>=2, so every primitive D(C) is composite. Thus no owner in this frozen family
has even one positive primitive log-prime packet. This conclusion concerns
these specified probabilities, not all heap, Markov or non-Markov clocks.

First required test: C_a=(e,[a],e) is primitive of state period 2 and has
D(C_a)=2a(a-1). In particular C_2 has least physical period log 4 in all four
owners. It is not a repetition of an absent log 2 packet. The e-avoiding
primitive cycle ([2],[22],[2]) has D=8 and is also retained in every owner.

For distinct a,b the legal state walk C_ab=(e,[a],[ab],[b],e) has unique e,
hence is primitive. Its reversed-letter counterpart C_ba is a different
necklace: unique e fixes the rotation and the next state differs. Put
ell_ab=2 when the letters exchange in that owner and ell_ab=1 otherwise.
The poset proof gives N([ab])=ell_ab and

    D(C_ab)=D(C_ba)=8 ell_ab a(a-1)b(b-1).

MAIN therefore has the required actual commuting [23]=[32] pair of distinct
packets, each of time log 192; their shared heap is an actual quotient state.
The complete control comparison (displaying D, not log D) is

| Own owner | Exchange rule | D(C_23) | D(C_24) | D(C_2) |
|---|---|---:|---:|---:|
| MAIN | gcd=1 | 192 | 192 | 4 |
| FREE-WORD | none | 96 | 192 | 4 |
| COMMUTATIVE | all distinct | 192 | 384 | 4 |
| NONCOPRIME | distinct, gcd>1 | 96 | 384 | 4 |

FREE-WORD has its own word states, N=1, ell=1, and first/last-letter L/R.
COMMUTATIVE has own finite-multiset states, N=n!/product_a m_a!, and L=R
given by removing one of its distinct present labels, so ell is support size.
NONCOPRIME uses the dependence-poset proof with its own opposite arithmetic
exchange relation; its N,L,R are independently enumerated by that poset.
Substituting each into Sections 2–5 supplies its own normalized pi, P, full X,
nonatomic full-support law, every-Borel IMAGE, all signed history kernels,
isotropy, incoming histories, H, primitive necklaces, phases and repetitions.
In particular the universal formulas quantify over each own state graph and
retain every own closed walk; the table is not substituted for those ledgers.

## 7. Bounded disposition

T0 is an explicit same-object Borel/groupoid construction. The arithmetic
exchange rule really changes old-symbol deletability and the own transition
counts, as the control comparison verifies. The clock is exactly that owner's
IMAGE cocycle; no prime-dependent roof or external labels were inserted.
These facts do not settle strong arithmetic naturalness, which remains OPEN.
T2 has a complete ledger and fails the stated prime-only target decisively;
the construction is a countable Markov lift, not an escape from splicing.
Portfolio: STOP, with no probability tuning or source restriction authorized.
T3 NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE; formal Route UNASSIGNED;
B NOT INVOKED. This raw report now awaits root read/freeze and explicit
manuscript unlock before any CP2/CP3 or main/peer access.
