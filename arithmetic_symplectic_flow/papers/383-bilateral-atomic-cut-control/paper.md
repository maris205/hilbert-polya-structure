# Bilateral cut transport: dense atoms and zero return time

**Candidate:** `ANG-CONTROL-20260922-BAC01`; paper `383-bilateral-atomic-cut-control`.<br>
**Date / portfolio:** 2026-09-22; **CONTROL STOP / FORK**.<br>
Outcome: `ATOMIC TRANSPORT OWNED / ZERO RETURNS — CONTROL STOP / FORK`
**Type:** Borel labelled path groupoid and real-height orbit SET, not a classical suspension.<br>
Strong naturalness OPEN; T3 NOT AUDITED; classical NOT APPLICABLE;
formal UNASSIGNED; Route B NOT INVOKED. No formal Route coordinate is assigned.

## Abstract

The frozen bilateral hard-gap source retains all configurations, including
its infinite-one null states. Shift and legal insertion/deletion generate a
well-defined reduced-label groupoid. An edit-address test and a spanning-tree
description determine every actual incoming arrow and the entire labelled
isotropy, including nonabelian groups. A dense, saturated countable set of
finite-one configurations carries the prescribed probability. Direct atomic
summation proves every-Borel IMAGE with the frozen positive finite all-point
density. Its logarithm is an endpoint potential on the WHOLE carrier, hence
every isotropy clock vanishes and every physical return group is {0}.
The three own controls retain this zero-return conclusion with their stated,
different source and isotropy ledgers. This is an atomic boundary control,
not a construction or impossibility theorem for a nonatomic arithmetic flow.

## 1. Frozen identity, question and arithmetic source

The [original 59-line card](candidate-card.md) is the sole scientific input.
Write S(x)={i in Z:x_i=1}. A completed gap is v-u for consecutive u<v in S(x).
Let Gamma(x) be the set of these positive integer values. The full source X
requires that distinct d,e in Gamma(x) satisfy d not dividing e and e not
dividing d. Repeated equal values are allowed; zero is never a gap value.
The all-zero state, finite/one-sided-infinite/two-sided-infinite supports,
and every null point remain. A violation has two finite witnessed gaps, so
X is closed in the compact binary product. Use its inherited Borel structure.

The preserved lineage is proper-divisor witnesses -> nonlocal complete-gap
admissibility -> actual two-sided cut transport. The question is whether this
specific atomic law and its prescribed all-point version supply positive
physical returns, not whether every measure on this source has the same clock.
No prime table, roof, operator, geometric section or old theorem is imported.

## 2. All actual branches and their arithmetic domains

Let t=T, u_a=I_a, a=0,1; their inverse symbols name their actual inverses.
T sends support S to S-1, T^-1 to S+1, and both preserve all gap values.
For insertion set L=S intersect(-infinity,0), R=S intersect[0,infinity):
I_a sends S to L union(R+1), additionally adjoining {0} exactly when a=1.
Its domain D_a consists of those x whose displayed output belongs to X.
Deletion d_a requires x_0=a and sends S to
(S intersect(-infinity,0)) union((S intersect[1,infinity))-1),
provided this output belongs to X. This is precisely I_a's range and inverse.
All-zero and empty-side cuts use these same formulas, without exceptional arrows.

Here is an explicit arithmetic domain test, keeping GAP OCCURRENCES until the
update is complete. For insertion let l=max L and r=min R when they exist.
Keep every gap internal to L or R; replace the old crossing gap r-l, if present,
by r+1-l for I_0, or by -l and r+1 for I_1, omitting terms with missing endpoints.
For deletion keep gaps internal to the strict negative and strict positive
sides, remove all old gaps incident across/at0, and add r-1-l if both sides
have a nearest occupied point. Check the new gaps against each other and ALL
untouched gap values. Do not remove a value that still occurs at another pair.
These tests are necessary and sufficient because no other gap changes.

The insertion maps are continuous on the ambient product; deletion is continuous
on its bit cylinder. Their domains and ranges above are closed and the maps
are mutually inverse homeomorphisms of those closed subspaces. Closed does not
mean open: no local-homeomorphism, etaleness or global free action is assumed.
There are no terminal states since both shifts are always allowed.

## 3. Reduced paths and a structural test for every label

A path is a finite sequence of legal generator steps. In products the rightmost
letter acts first. An adjacent inverse pair returns to the very same intermediate
state; removing it leaves a legal path with unchanged endpoints. The usual
stack cancellation gives a unique free reduced word w in F(t,u_0,u_1).
From a fixed source, a fixed reduced word has at most one path, since each step
is a partial function. Every unreduced path reduces to that legal path. Thus
G={(theta_w x,w,x):x in D_w} is well-defined, with identity (x,e,x), reversed
path inverse, and concatenation followed by cancellation as multiplication.
Associativity follows from free-word reduction and the unchanged endpoints.
The reduced chart can have a larger domain than one unreduced spelling, but
it agrees on every source where that spelling is legal; no domain is inferred
from an illegal spelling. Countably many closed chart graphs give G a Borel
structure inherited from X times the discrete free group times X.

The following edit-address procedure describes D_w and all endpoints directly.
Start an address tape A(j)=j, where integer j reads x_j and marked constants
underline0,underline1 read the indicated fixed bits. Apply to A each generator's
coordinate formula from the card; deletion first tests the evaluated A(0)=a.
At each step perform the gap-occurrence test in section2. Shift reindexes A;
insertion writes a marked constant; deletion removes one entry. Each finite
word yields a finite piecewise-translation table with finitely many constants.
Induction on the word gives computable R and offsets

    A_w(j)=j+alpha_- for j<-R;  A_w(j)=j+alpha_+ for j>R,
    alpha_-=n_t(w),            alpha_+=n_t(w)-n_I(w),

where n_t counts t minus t^-1 and n_I counts both insertions minus deletions.
The finite center is the remaining address/constant table. These assertions
follow at each step because a far negative insertion/deletion changes no
address, a far positive insertion subtracts1, a deletion adds1, and t adds1.
Choose R large enough for all previous cut positions as well as the final table.

Consequently (z,w,x) is an incoming arrow EXACTLY when all the finite sequence
of bit/domain tests succeeds, z_j=x_(j+alpha_-) for j<-R,
z_j=x_(j+alpha_+) for j>R, and every center entry agrees with its address or
constant. Isotropy replaces z by x in these explicit conditions. In particular
nonzero tail offsets require the corresponding semi-infinite tail periodicity;
zero offsets impose no tail condition. This is a full-label criterion, not just
the equation theta_w x=x or a list of short loops. Global untouched-gap tests
and tail equalities remain genuine infinite-state conditions; the claim is
not finite-time decidability from a bounded sample of an arbitrary input.

## 4. Complete isotropy structure and the named source tests

For an additional group-level description, form the actual orbit graph of x:
vertices are all endpoints of the preceding test, edges are each legal named
generator step, paired only with its named inverse. Keep parallel edges and
self-loops. Order the six symbols once and choose for every vertex its first
shortest path from x. Prefixes are first shortest paths too (otherwise replacing
a prefix shortens or lexicographically improves the whole path), so these paths
form a spanning tree. Choose ONE orientation per inverse-paired non-tree edge;
go from x along the tree to its source, traverse it, then return along the
target's reversed tree path. A loop edge is retained, not placed in the tree.

These loops form a free basis of Iso_G(x). Indeed insert tree paths at every
vertex of a closed path; tree traversals cancel, leaving the ordered non-tree
edge word. Conversely a nonempty reduced word in these basis loops cannot
cancel its last remaining non-tree edge. This proves generation and no further
relations. It constructs the ENTIRE group from actual source-checked edges,
not from a presumed global action; the group has at most countable rank.

Let D be all finite-one states in X and N=X\D. All generators preserve D and N.
Every D-state reaches0^Z: shift its leftmost1 to0 and delete that1; this removes
only the first gap, translates the remaining support, and stays legal. Repeat
finitely, then reverse paths for arbitrary incoming states. Hence O(0^Z)=D.
At each singleton support {-m}, m>=1, insertion0 is a self-loop. These infinitely
many non-tree edges show Iso_G(0^Z), and every finite-state isotropy, is free of
countably infinite rank. In particular the t and u_0 loops are both retained.

At1^Z, shifts and insertion/deletion1 fix the state. Insertion0 creates gap2
beside existing gap1 and is illegal; deletion0 fails its bit test. Thus its
whole orbit is a singleton and its ENTIRE isotropy is F(t,u_1), of rank2.
For x=(10)^Z with x_0=1, the complete section3 test simplifies to even n_t,
even n_I, all center entries matching alternating parity, and all intermediate
gap/bit tests. This is necessary and sufficient, since both tails have period2.
It includes t^2 and u_1 u_0: insertion0 first makes the single crossing gap3
among gap2 values, and insertion1 then restores the alternating state. Alternating
nonzero powers of these two words cannot cancel in the disjoint t/cut alphabets,
so they generate a free rank2 subgroup; section3 and the tree basis retain all
additional labels, not merely that subgroup. The three tests are not a census.

The endpoint-forgetting functor q:G->R has kernel the whole isotropy bundle.
This is not a claim that every such label acts identically on its whole domain:
t fixes constants but moves a singleton. Nor is it the kernel of the label
map lambda:G->F(t,u_0,u_1), which contains only identity arrows. No germ quotient
or global partial-action effectiveness theorem is silently substituted.

## 5. Dense atomic probability and every-Borel all-point IMAGE

The frozen e:Z->N_0 is a bijection. Binary expansion makes
code(F)=sum_(i in F)2^e(i) injective on finite subsets, taking values in N_0.
Therefore 1<B=sum_(1_F in D)2^(-code(F))<=sum_(n>=0)2^(-n)=2.
The strict lower bound uses the empty set and any singleton. The normalized
weights b(1_F)=2^(-code(F))/B define a probability on FULL X; its atoms are
exactly D. It has full support: for any nonempty cylinder choose x in it and
truncate S(x) to a finite interval containing its specified coordinates. The
retained gaps are a subset of the old gaps, so this truncation lies in D and
has positive mass. N is retained with measure0, not deleted or given an atom.

The specified function b is these positive masses on D and1 on N; it is Borel,
finite and strictly positive everywhere. Every actual word is a bijection
between its source-checked domain and range and preserves D/N, by finite edits
and shifts. For ANY Borel E subset D_w, including arbitrary null restrictions,

    mu(theta_w E)=sum_(x in E intersect D) b(theta_w x)
                 =integral_E [b(theta_w x)/b(x)] dmu(x).

Images are Borel because each chart is a homeomorphism of its closed domain
and range. The atomic sum proves IMAGE in the forward source-to-image direction;
no ratio of possibly zero set masses is taken. The frozen J_w is positive
finite at every point, equals1 on N, and its inverse version is reciprocal at
the actual target. Composition telescopes the b ratios; cancellation and any
two charts with the same endpoints give the same ratio wherever both apply.
Thus full-point consistency and the every-history IMAGE identity are proved.
On N, every-Borel equality alone would not select this version: b=1 there is
part of this CONTROL's frozen prescription, not a uniqueness/naturalness theorem.

## 6. Exact clock, all kernels, full return groups and phases

Only now define V=-log b, c(z,w,x)=V(z)-V(x)=-log J_w(x), and the actual extension
(x,h)->(z,h+c). All quantities are finite at every point; no infinite energy
sum or unit roof is introduced. If x=1_F,z=1_E, then
c=(code(E)-code(F))log2. On N every arrow has c=0. For example insertion1 at
0^Z has c=log2, but its inverse has -log2; that edge is not a positive return.

Codes and hence atomic masses are distinct, while every atomic b<1 and b=1 on N.
Together with D/N saturation this gives the COMPLETE clock kernel

    ker c = { (x,w,x):x in D, w in Iso_G(x) } union G|N.

The retained full-label kernel ker lambda consists only of identity arrows,
and its intersection with ker c is the same unit set. The endpoint kernel
ker q is ALL source isotropy, on both D and N. At every source point and height,
extension isotropy is exactly Iso_G(x), because every loop has c=0. Therefore

    H_x={c(g):g in Iso_G(x)}={0}  for EVERY x in X.

This includes all tree-basis labels, all null-state loops and their conjugates;
the conclusion does not rest on the three named tests. All incoming lifted
arrows are precisely (x,h)->(theta_w x,h+V(theta_w x)-V(x)) with the section3
source checks, retaining every label. The invariant phase is s=h-V(x)=h+log b(x).
Two lifted points are equivalent exactly when their sources share an actual
orbit and these real phases agree. Hence the orbit SET is (X/G) times R with
time translation s->s+t. No manifold, separation or classical suspension claim
is made. Each physical orbit is a real line with stabilizer{0}; there are no
positive primitive physical packets or positive repetitions. Source loops and
nonabelian label multiplicity survive but are not positive-time repetitions.

## 7. Three independently owned controls

### 7.1 SHIFT-ONLY

Its whole carrier is X, its actual arrows are (T^k x,k,x), k in Z, with global
inverse T^-k. Its own finite-one sum uses the same legal subsets and therefore
the same B; the truncation proof gives its own full support. Shifts preserve
finite/infinite support, so the atomic sum of section5 directly proves its own
all-point J_k=b(T^k x)/b(x), not a borrowed cut version. Full incoming points
are exactly T^k x. Isotropy is pZ when x is globally periodic with least p,
and{0} otherwise: a nonzero stabilizing shift is exactly a bilateral period,
and the subgroup's least positive element generates all periods by division.
Nonempty finite supports have no such shift (use their minimum);0^Z and1^Z
have p=1, the alternating points p=2. Eventual periodicity alone does not suffice.
Clock kernel consists of finite-state isotropy plus ALL arrows on N; integer
lag kernel and its intersection are units. Extension isotropy is the full
source group, H={0} everywhere, incoming heights have the same potential
difference, and phase s=h+log b(x) parametrizes a free real line over each actual
SHIFT orbit. There are no positive packets; distinct shift orbits are not merged.

### 7.2 HARD-OFF

Its own source is Y={0,1}^Z. Insertions have whole domain; deletion of a requires
only the bit a. The address and reduced-graph proofs apply with all gap tests
removed, so they give its complete domains, incoming arrows and entire tree
basis isotropy. All finite subsets are allowed; binary coding is now onto N_0,
so B_off=2 and b_off(1_F)=2^(-code(F)-1), with b_off=1 on infinite supports.
Its dense atomic probability and every-Borel IMAGE follow directly by summing
these own weights over each bijective chart. Its specified c_off is again the
endpoint potential; clock kernel is finite-state isotropy union the entire
infinite-state restriction, label kernel/intersection are units, extension
isotropy is its entire source group, and H={0} at ALL points.

Source groups are not imported from MAIN:0^Z has the all-finite orbit and free
countably infinite rank;1^Z now has the whole cofinite-one orbit. Delete its
finitely many zeros to reach1^Z; conversely finite edits cannot leave this orbit.
The states with one zero at -m supply infinitely many insertion1 self-loops,
so its isotropy has countably infinite rank, rather than MAIN's rank2.
The alternating full-label test keeps the even-tail and center tests but drops
intermediate arithmetic exclusions. For every source, the tree basis remains
the complete description. Phase is h+log b_off(x); all incoming words remain;
each physical orbit is a free line and no positive primitive/repeated packet exists.

### 7.3 ENDPOINT

This independently defined control is R={(z,x):some actual MAIN path joins x,z},
a countable Borel equivalence-relation groupoid. It is NOT a germ groupoid.
Its own measure is the same finite-one recipe on FULL X. Each graph chart
theta_w has the atomic IMAGE identity, and J(z,x)=b(z)/b(x) is independent
of the word representation, so both density and potential clock descend.
Any Borel bijective chart of R can be partitioned by its first word representation;
the same atomic sum proves IMAGE on that chart as well, including null restrictions.
Incoming sources/ranges are all actual MAIN orbit points, now with one arrow
per endpoint pair. Source and extension isotropy are trivial at every point.
Clock kernel is the diagonal on D union R|N. There is no retained free-word
lag in this control (that kernel field is NOT APPLICABLE), and its endpoint
functor is the identity. H={0}; phase h+log b(x) and the full real-line physical
orbits remain, with no positive packets. Forgetting labels changes the object
and source multiplicity; it does not manufacture returns or repair MAIN.

## 8. Decision, reproducibility and disclosure

The CONTROL owns its complete Borel source/action, probability, every-history
positive finite all-point IMAGE and real-height extension. Its full H is zero,
so the positive prime-packet target stops. This conclusion concerns precisely
the frozen atomic law and null-state version; no nonatomic or general groupoid
no-go follows. Strong naturalness OPEN; T3 NOT AUDITED; classical NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED. A different law/version/quotient requires a
new freeze, not an overwrite or inherited credit.

Scientific input personally read: candidate-card.md1–59 through actual EOF,
SHA256 d9f5a9215dc603ab848a67900f8ca6cde9b751f5cb302fb2e693fbf9bf9ffe25,
using `nl -ba`, `wc -l`, `sha256sum`; paper-template.md was read fully.
Root reported CP1 acceptance and explicitly released this independent author
derivation. No scope/raw/peer evidence or other new manuscript was read.
Earlier definition work supplied the cut architecture, not this root-frozen
atomic law; no nonatomic status was established for the unadopted measure idea.
Shared prior history includes378 authorship and375 batch-summary1–73, not a
blind discovery or globally novel claim. ARS writing guidance was read; internal
model work is NOT_CALIBRATED and is not external peer review.

All results above are exact arguments, without scientific code, numerical
census, external retrieval or Git changes. Metadata commands and Markdown
editing are not experiments. Data availability: the card and displayed formulas
are the complete inputs. Contributions: root chose/froze this CONTROL; this
author derived and wrote the manuscript and support ledger; review is separate.
No human-subject or private-data study occurs. No external funding or competing
interest information was supplied; no claim of an independently verified
disclosure is made. AI-assisted authorship is explicit. See the [claim ledger](claim-ledger.md).
