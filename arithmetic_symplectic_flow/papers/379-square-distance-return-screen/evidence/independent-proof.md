# Independent raw proof — square-distance source screen

Screen `ANG-SCREEN-20260922-SDC01`; round5/5, `HARD-NONLOCAL-20260922-F`.
Reviewer `/root/nonlocal_source_review`; date2026-09-22.
Input: all82lines of [frozen card](../candidate-card.md), SHA256
`111aeaa1b7599fa9ac05367b1b020865084a104d99a31114ec13ea40fc87afdb`.
Root explicitly released mathematical work after reading CP1. No manuscript,
peer proof or other375–379 paper was read. Shared-history internal review is
`NOT_CALIBRATED`, not blind, cross-model or external peer review. Exact proofs
below are primary evidence; no numerical experiment or external priority claim.

## 1. One full source for each distance set

For any fixed D subset of the positive integers, put A={2,3,...} and
X_D={x in A^N0:gcd(x_i,x_(i+d))=1 for all i>=0,d in D}.
Every individual constraint is clopen in the discrete product topology;
X_D is closed. Left shift T is continuous and total because shifting replaces
i by i+1 in the same constraints. No surjectivity assertion is needed below.

Set F_i=2^(2^i)+1. The elementary factorization
product_(j<i) F_j=2^(2^i)-1=F_i-2 follows inductively from
(v-1)(v+1)=v^2-1, including the empty product at i=0.
For j>i, F_j is 2 modulo F_i. Both are odd, so gcd(F_i,F_j)=1.
Thus (F_0,F_1,...) belongs to X_D for EVERY such D. This proves all four
carriers nonempty without asserting primality of any F_i.

The complete one-letter inverse relation is
I_a(y)=ay, E_a={y in X_D:gcd(a,y_(d-1))=1 for every d in D}.
Indeed only pairs involving the new index0 add constraints. Every preimage
has a unique first letter, so these are ALL branches, not chosen branches.
E_a is closed, but need not be treated as open; I_a is a homeomorphism onto
X_D intersect [a] with its subspace topology. No etale claim follows.

For u=(u_0,...,u_(m-1)), its full prefix domain E_u consists of y in X_D with
(i) gcd(u_i,u_j)=1 whenever 0<=i<j<m and j-i in D, and
(ii) gcd(u_i,y_t)=1 whenever i<m,t>=0 and m+t-i in D.
Internal failure makes E_u empty; otherwise these are all crossing tests.
The empty word has E_empty=X_D. Consequently T^m preimages are exactly uy
with y in E_u, retaining every finite legal prefix and the entire tail.

## 2. Actual arrows, incoming relation and lag kernel

G_D={(z,m-n,y):m,n>=0,T^m z=T^n y}, with equal triples identified.
Source is y, range z, inverse reverses endpoints and lag; composition adds
lags. To check closure, align the two equal-tail equations by applying the
additional powers n or p, yielding T^(m+p)z=T^(n+q)w for composable witnesses.
This is a countable Borel groupoid, without requiring local homeomorphisms.

For fixed y, ALL arrows with source y have the description
(u T^n y,m-n,y), n,m>=0, u in A^m, T^n y in E_u.
Duplicates are identified only when endpoint and lag agree. Their endpoints
form exactly [y]_G. ALL arrows with range y are their inverses. This formula
also lists every permitted prehistory; it does not discard eventual prefixes.
The complete lag kernel is {(z,0,y):T^m z=T^m y for some m>=0}.
It is not generally just units: (2,F_0,F_1,...) and (4,F_0,F_1,...) are
different admissible points for every D here, with equal first shifts.

Entire source isotropy at y, identified by its lag, is
I_y={k in Z:(y,k,y) in G_D}. It is {0} unless y is eventually periodic.
If its eventual tail has least word period l, then I_y=l Z. A nonzero equal-
tail lag is precisely an eventual period. Conversely each eventual period
gives such an arrow. For a periodic tail, reduction of any other period modulo
l gives a period of its cyclic word; minimality forces that residue to be0.
Hence this statement includes every eventually periodic point, not only a
selected pure cycle. The abstract lag generator need not be a physical time.

## 3. Exact universal cyclic-word criterion

For l>=1 let R_D(l)={d mod l:d in D}. A word w in A^l gives an admissible
periodic sequence if and only if
gcd(w_i,w_((i+r) mod l))=1 for every i mod l and every r in R_D(l).       (1)
Necessity applies each actual distance to the periodic sequence; sufficiency
reduces every actual distance modulo l. This uses the COMPLETE residue set.
The word is primitive precisely when its least cyclic word period is l.

There exists an admissible sequence of least period l exactly when
0 is NOT in R_D(l). If0 is present, (1) requires gcd(w_i,w_i)=1, impossible
in A. If0 is absent, choose w=(F_0,...,F_(l-1)). Its distinct entries make
its least period l, and pairwise coprimality verifies every nonzero residue.
The construction includes l=1 when the residue set is empty. This proves
sufficiency, not just an exclusion test on potential periods.

All primitive source cycles are EXACTLY the primitive words satisfying(1),
modulo cyclic rotation. Rotations lie in one G_D orbit; two periodic tails in
the same G_D orbit agree after shifts and therefore have the same primitive
necklace. The whole class attached to a representative w^infinity consists
of all u T^n(w^infinity) with T^n(w^infinity) in E_u. These are precisely the
legal eventual prefixes/phases, not extra primitive necklaces. Repeating the
word r times does not create a new primitive cycle; its loop lag is r*l.
Non-eventually-periodic source orbits remain present with zero isotropy.

## 4. MAIN: every square distance

Here R_D(l)={r^2 mod l:0<=r<l}. Every positive l has0 in this set, since the
ACTUAL allowed distance l^2 is divisible by l. Thus no period l is legal.
Directly, if x becomes l-periodic after N, then x_(N+l^2)=x_N, whereas the
distance-l^2 rule requires gcd(x_N,x_N)=1, a contradiction. This proof treats
all positive l at once and every coordinate after the preperiod.
Therefore MAIN has no eventually periodic points: I_x={0} for EVERY x.
Its inverse domains, all arrows/incoming and nontrivial lag kernel remain
those of §§1–2; its source is nonempty, not an empty-carrier obstruction.

## 5. Three complete source-only controls

ODD-SQUARE has R_odd(l)={r^2 mod l:1<=r<2l,r odd}. Reduction modulo2l
preserves parity and square residue, so this is exact for all odd squares.
If l is odd, the allowed distance l^2 gives residue0. If l is even, no odd
square is divisible by l, hence0 is absent. Possible least periods are thus
EXACTLY all positive even integers, each realized by its distinct-Fermat word.
Its exact primitive words are(1) with this R_odd, not merely alternating
examples. E_a tests y_((2n+1)^2-1) for every n>=0; E_u uses the same D_odd
in both tests of §1. §§2–3 give all incoming, lag kernel, eventual classes
and I_y=l Z for a least eventual even l, otherwise I_y={0}.

FINITE-SQUARE has R_fin(l)={1 mod l,4 mod l}. Its self-residue obstruction
occurs exactly at l=1,2,4; ALL l=3 and l>=5 occur by the same explicit distinct-
Fermat construction. Primitive words are exactly the least-period words
satisfying gcd(w_i,w_(i+1))=gcd(w_i,w_(i+4))=1 with cyclic indices.
E_a={y:gcd(a,y_0)=gcd(a,y_3)=1}; E_u retains both internal and crossing
distance1/4 tests. §§2–3 give every arrow, incoming, lag kernel and eventual
prefix class; I_y=l Z precisely for a least eventual admissible l, else{0}.
This control is a separate finite-distance source, not a truncation proof
that MAIN possesses any period.

INTERACTION-OFF has X=A^N0 and empty residue sets; every E_a and E_u is all X.
Every primitive cyclic word is legal, and all least periods l>=1 occur.
Every constant a is a distinct least-period1 source cycle. The arrow/orbit and
lag-kernel descriptions of §2 apply without admissibility exclusions; entire
source isotropy is l Z at any eventually l-periodic point, and{0} otherwise.

All three carriers also contain the nonperiodic increasing Fermat sequence.
Their source multiplicities are the full necklace lists above, without
choosing one necklace, phase or prefix representative as the whole owner.

## 6. Conditional height extension — no clock has been constructed

Suppose, ONLY conditionally, a real additive cocycle c on the actual G_D is
given. Its extension arrows are (y,h)->(z,h+c(z,k,y)); all X_D times R stays.
Let Q be their orbit SET, and let height translation send [y,h] to[y,h+t].
An equality [y,h+t]=[y,h] holds exactly when an isotropy arrow (y,k,y) has
c(y,k,y)=t: any finite arrow chain composes to one such arrow, and conversely
that arrow proves equality. Therefore the stabilizer is exactly c(I_y).
Extension isotropy at(y,h) is ker(c restricted to I_y). Every source arrow
also fixes the full height relation between its endpoints; none is omitted.

Conditionally, I_y={0} implies stabilizer{0} and trivial extension isotropy.
If I_y=l Z and alpha=c(y,l,y), the stabilizer is alpha Z, and extension
isotropy is l Z when alpha=0, otherwise{0}. A nonzero alpha would give least
positive time |alpha|, but source l supplies no value or sign of alpha.
For controls, these are formulas in an UNASSIGNED cocycle, not assigned H
values, IMAGE laws, clocks or target verdicts. The clock kernel, if c is later
supplied, is {g:c(g)=0}; without c there is no actual clock kernel to evaluate.

In particular ANY such conditional MAIN extension has no positive time
stabilizer, because MAIN's entire source isotropy is trivial. This is a
universal conditional obstruction, not an actual construction with a zero
clock. The present screen's physical clock, H and packet ledger are undefined.
Neither probabilities nor their nonexistence follow from the argument.

## 7. Scoped disposition

STOP before measured P0: MAIN's hard square schedule forbids every genuine
source return, even though the full carrier and inverse relation are nonempty.
The three controls show the exact dependence on distance/period resonance;
they do not license changing MAIN or importing their source cycles or clocks.
No invariant-probability claim, physical time, operator, formal Route label
or global no-go beyond these hypotheses is proved. T1 measure/clock and T3
NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
The same-object source ledger remains intact; round5 ends at batch handoff.

EOF — raw complete source proof; await explicit PAPER UNLOCK before peer access.
