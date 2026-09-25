# SPR01 — independent card-only derivation

Candidate ID: ANG-AUDIT-20260924-SPR01.
Date label: 2026-09-24; batch RECURRENCE-ADMISSION-20260924-W, round5/5.
Reviewer: /root/pcr01_independent_review, separate from author and helper.

## 0. Frozen inputs and release boundary

The sole newly read scientific input is candidate-card.md, amended118 lines,
SHA256 bbefea1f80acb342a9e5f49f03a7f4b11666543e0674b184c6aab235e123545f.
The original107-line prefix has SHA256
d0ea8d7a2786717a65af42cfac64e2b4d9e507bd4f527e228b611899a59f70f8.
The initial CP1 version-choice issue was resolved before any science release.
CP1 scope-review.md has180 lines and SHA256
47cd414189b228ba538c5c40e08c030b7aa88d6e23c39ddda6d7e462292b84b4.
Root FULL read CP1, then separately released this RAW stage.
The complete amended card was reread through EOF for this derivation.

No464 author paper, README, ledger, helper answer or current peer answer
has been read. No old proof/card has been reopened. This file is the only
RAW-stage write. No scientific code, numerics, network, Git or PDF is used.
Inherited443/448/454/459 review history and the old overview exposure
disclosed in CP1 remain. Same-model shared-history checking is NOT_CALIBRATED,
not blind, human, external or cross-model validation. ARS supplied bounded
proof and disclosure discipline. All mathematics below is freshly worked
from the frozen SPR01 contract, not credited from an earlier theorem.
This raw must freeze before root FULL read and DISTINCT PAPER UNLOCK.

## 1. Actual restricted inverse atlas and owned all-point clock

For each parent source piece D_i put \(D_i^E=D_i\cap E\). These pieces
form a complete disjoint countable Borel partition of E. Let
\[
 Y_i^E=\{y\in\operatorname{dom}\theta_i:\theta_i(y)\in E\},\qquad
 \theta_i^E=\theta_i|_{Y_i^E},\qquad J_i^E=J_i|_{Y_i^E}.
\]
The first set is Borel, is exactly T(D_i^E), and theta_i^E is the actual
inverse of Q on D_i^E. Both inverse identities follow from the parent
identities and the source permission test. No requirement y in E is made.
Every Q predecessor appears on its parent's unique source piece and is
retained precisely when its source is in E.

For every Borel B contained in Y_i^E, the parent every-Borel identity gives
\[
 \mu(\theta_i^E B)=\mu(\theta_i B)
       =\int_B J_i\,d\mu=\int_B J_i^E\,d\mu.
\]
This proves the new owner's own IMAGE identity for the original measure.
Its frozen all-point version is exactly the displayed restriction; hence
\[
 \kappa_Q(x)=-\log J_i^E(Qx)=\kappa_T(x)\qquad(x\in D_i^E).
\]
There is no Q outgoing clock at x outside E. Incoming arrows and units
remain there. No value is reset to zero or multiplied at a permission cut.
The every-Borel identity alone does not uniquely select null-point values;
the stipulated versions, including the clarified control versions, are
separate data and are used pointwise.

For n>=0, Q^n x exists exactly when T^n x exists and
\[
 T^j x\in E\qquad(0\le j<n).
\]
At n=0 this is vacuous at every object. The endpoint T^n x may be outside E.
On a legal Q history, Q^n x=T^n x and S_n^Q(x)=S_n^T(x).
For any target y and depth n, the complete inverse sources are therefore
\[
 (Q^n)^{-1}(y)=
 \{x:T^nx=y\text{ legally},\ T^jx\in E\ (0\le j<n)\}.
\]
Repeated actual restricted inverse branches enumerate all these sources;
all compatible sequences give the infinite backward histories. A terminal
target is allowed to have arbitrarily deep or infinite backward histories.

## 2. Both actual groupoids, clocks and exact embedding

For either U=T,Q, use legal meeting triples (z,m-n,w), source w and
range z, identifying equal triples. Set
\[
 c_U(z,m-n,w)=S_m^U(z)-S_n^U(w).
\]
Two witnesses of the same triple shift both depths by the same integer.
After ordering those depths, the extra legal history begins at the common
meeting and contributes an identical sum to both terms. Thus c descends.
For composition, extend the shorter middle history to the longer one,
using that longer actual history to justify the extension. The middle
sums cancel, proving additivity and negation under inverse. This does
not complete a terminal by an extra step. The forward arrow
(Uz,-1,z) has clock minus kappa_U(z).

Every Q witness is a T witness, so
\[
 \iota:G_Q\longrightarrow G_T,\qquad(z,k,w)\longmapsto(z,k,w)
\]
is injective on actual triples, preserves composition, inverse and units,
and is the identity on the full object set X. On its arrows
\[
 c_Q=c_T\circ\iota.
\]
The image is exactly, not just contained in,
\[
 \{(z,k,w)\in G_T:\exists m,n\ge0,\ m-n=k,\ T^mz=T^nw,
       \ T^jz\in E\ (j<m),\ T^jw\in E\ (j<n)\}.
\]
The forward implication is the legal-history criterion in Section1;
conversely the stated witness is an actual Q witness. The common endpoint
does not have to lie in E. Testing an arbitrary displayed parent witness
is not equivalent to testing this existential condition.

For an equivalent precise decision rule define the first forbidden depth
\[
 \tau(x)=\min\{n\ge0:T^nx\text{ exists and }T^nx\notin E\},
\]
with tau=infinity when the parent path stays in E forever. Because E is
contained in the parent domain, a parent terminal is itself outside E,
so a finite parent path always has such an endpoint. Legal Q depths are
exactly 0<=n<=tau(x).

Given one parent arrow (z,k,w), its witnesses have a least second depth
n_0 and first depth m_0=n_0+k. All other witnesses of that same triple
are (m_0+d,n_0+d) with d>=0 and the shared parent tail legal.
This follows from determinism and the ordering of integer depths.
Consequently the arrow is in the image iff
\[
 m_0\le\tau(z),\qquad n_0\le\tau(w).
\]
If any later witness is legal for Q, its shorter prefixes are legal too.
Conversely these inequalities make the least witness legal. A later
parent witness may pass a forbidden source even though the least witness
does not; that does not remove the arrow.

The complete kernels for U are
\[
 K_{\rm lag}^U=\{(z,0,w):U^nz=U^nw\text{ legally for some }n\},
\quad K_c^U=\{g\in G_U:c_U(g)=0\},
\quad K_{\rm joint}^U=K_{\rm lag}^U\cap K_c^U.
\]
Since both lag and clock are preserved here, their exact relation is
\[
 K_{\rm lag}^Q=G_Q\cap K_{\rm lag}^T,\qquad
 K_c^Q=G_Q\cap K_c^T,\qquad
 K_{\rm joint}^Q=G_Q\cap K_{\rm joint}^T,
\]
where G_Q is identified with its proven image. This retains all actual
nonunit merges and all possible clock cancellation arrows; they need
not be units or equal to one another.

## 3. Complete source classes, isotropy and phase classification

The full packet of w for either owner is the union of every legal inverse
depth of every legal forward U^n w. Equivalently z and w are in the same
packet exactly when some legal forward histories meet. This includes all
incoming roots, not a chosen branch or a selected recurrent section.

A deterministic partial map has a nonzero-lag source loop exactly when
the source is eventually periodic: unequal depths meeting on its one
forward path give an actual repeated state, and conversely any eventual
cycle supplies loop witnesses after entry. For a least-q eventual core
of signed clock C, the entire source isotropy, its clock character and H are
\[
 \operatorname{Iso}(z)=q\mathbb Z,\qquad
 c(z,tq,z)=tC,\qquad H_z=C\mathbb Z.
\]
Necessity uses the least cycle period; sufficiency uses sufficiently late
core witnesses. These are true at transient incoming sources too.
Extension isotropy is qZ if C=0 and zero otherwise. Terminal and infinite
non-eventual sources have zero source/extension isotropy and H.

On the whole X times R the extension acts by
\[
 (w,h)\longmapsto(z,h+c_U(g)).
\]
Within one packet choose a reference p and actual arrows g_z:p to z,
and let a_z=c_U(g_z). The full phase set is
\[
 [h-a_z]\in\mathbb R/H_p.
\]
Another choice of g_z changes a_z by H_p. A different packet reference
translates the coordinate. No global measurable choice or regular quotient
is claimed. Translation on this orbit set has exactly stabilizer H_p:
its displacement must and can be supplied by a source loop clock.
For C nonzero its primitive is abs(C) and every positive return is
n abs(C), n>=1. For H=0 there is no positive return and all real phases stay.

For a full incoming periodic packet choose p on its core, d_z with
U^{d_z}z=p, and a_z=S_{d_z}^U(z). Its complete arrows are
\[
 (z,d_z-d_w+tq,w),\qquad c_U=a_z-a_w+tC,\qquad t\in\mathbb Z.
\]
Extend any meeting to p for necessity; sufficiently many extra core turns
realize every indicated lag for sufficiency. The lag kernel sets the
displayed lag to zero, the clock kernel sets its clock to zero, and
the joint kernel imposes both. Phase is h-a_z modulo CZ, including C=0.
Zero cycle clock does not require all incoming a_z to be equal.

For Q define \(X_\infty=\{x:\tau(x)=\infty\}\).
Every source outside X_infinity has actual Q endpoint
\[
 e(x)=T^{\tau(x)}x\in X\setminus E.
\]
Two such sources are in the same Q packet iff their endpoints agree:
a legal meeting forces the same later first forbidden source, and an
equal endpoint supplies a legal meeting. No finite-ending source can
share a Q packet with an infinite one. Thus every terminal Q packet is
exactly one nonempty fibre of e, including e itself with depth0.
This classifies cut points on old cycles as well as original terminals.

For z in the endpoint-e packet put d_z=tau(z) and a_z=S_{d_z}^T(z).
All its Q arrows, with no further loop term, are
\[
 (z,d_z-d_w,w),\qquad c_Q=a_z-a_w.
\]
The source/extension isotropy and H vanish; full phase is h-a_z in R.
All three kernels are the exact depth/clock equality predicates. These
formulas include arbitrary incoming depths and nonunit merges at equal
depth, where they really exist.

For points of X_infinity every parent forward history is also a Q history.
Hence on this set G_Q is the full restriction of G_T: any parent meeting
witness between its points is legal for Q. Each parent source packet has
at most one nonempty infinite Q packet, its intersection with X_infinity.
No assumption about injectivity of T is used. This describes all infinite
non-eventual classes as well as surviving eventual-periodic classes.

For a non-eventual infinite packet, there is only one arrow between given
endpoints, since two would yield nonzero source isotropy. Taking its
unique arrows from a packet reference gives integer labels l_z and clocks
a_z. All arrows have lag l_z-l_w and clock a_z-a_w. The kernels impose
the corresponding equalities, H and both isotropies are zero, and phase
is h-a_z in R. Exact common legal tails and the inverse recursion provide
complete tests even when no simpler closed parametrization is available.

Every Q source is in one of the above terminal fibres or infinite
intersections. Distinct parent packets cannot merge under Q, because
every Q meeting is already a parent meeting. A parent packet can split
into many endpoint packets and at most one infinite packet; none of its
objects is removed in that split.

## 4. Extension relation inclusion is not phase injectivity

The clock-compatible inclusion also embeds the full extension arrow
groupoid by keeping objects (x,h) and arrows. Its orbit equivalence
relation is a subrelation of the parent's. Therefore the natural map
\[
 (X\times\mathbb R)/G_Q^c\ \longrightarrow\
 (X\times\mathbb R)/G_T^c
\]
is surjective as a map of orbit SETS and commutes with height translation.
It need not be injective. Keeping all extended objects does not keep all
extended equivalences.

For an exact phase test in an endpoint-e Q packet, choose a parent packet
reference p and a parent arrow p to e of clock beta_e. The Q phase
v=h-a_z in R maps to the parent phase
\[
 [v-\beta_e]\in\mathbb R/H_T.
\]
Indeed composing that parent arrow with the Q arrow e to z has clock
beta_e+a_z. Thus different endpoint packets can give distinct real phase
families over the same parent phase family. If H_T is nonzero, even one
such R family maps by a noninjective reduction modulo H_T.

In the infinite intersection packet, the full parent restriction retains
the same isotropy and clock arrows, so a permitted reference gives its
phase coordinate bijectively with the parent's R/H_T, up to translation.
Together these statements describe every phase contribution from every
cut incoming path, including a cut source before a surviving parent core.
They assert no global quotient topology or measurable selector.

## 5. Surviving cores and exact positive benchmark

A parent least-q core Gamma survives as a Q core iff EVERY point of Gamma
lies in E. The forward direction tests each actual outgoing edge around
a Q cycle. Conversely permission at every phase permits exactly the old
cycle, with its old least period q and signed sum C. A smaller Q period
would already be a smaller parent period. Every Q cycle is a parent
cycle because Q steps are unchanged T steps. Thus coverage and converse
are exact: no new core, no absorbing fixed point at a cut, and no duplicate
copy of a surviving core.

For a surviving core, its complete Q incoming packet consists of the
parent incoming sources whose entire path to that core is permitted.
Equivalently it is the parent core packet intersected with X_infinity.
If a source encounters a forbidden source before core arrival it instead
belongs to that forbidden endpoint's terminal packet, even though the core
it would later reach under T survives. Every allowed parent inverse branch
is retained by the actual recursion, so this is not a finite-basin claim.
Its source isotropy remains qZ, entire H remains CZ, extension isotropy
is qZ when C=0 and zero otherwise, and all phases/repetitions are those
of Section3. For a cut core there is no eventual Q core above it; all its
parent incoming sources terminate at their first forbidden source.

Consequently the complete positive Q ledger, with multiplicity, is
\[
 \{(\Gamma,|C_\Gamma|):
       \Gamma\text{ a distinct parent core},\
       \Gamma\subset E,\ C_\Gamma\ne0\}.
\]
Each such core is counted once modulo phase. Equal positive times of
different cores remain different packets. Zero-clock surviving cores
retain all their source isotropy but add no positive primitive.

The exact necessary and sufficient benchmark is:

1. At least one retained parent core has nonzero C.
2. For every retained nonzero core, exp(abs(C)) is an ordinary prime.
3. No two distinct retained nonzero cores have the same such prime.

All-prime coverage is the additional requirement that these retained
primes exhaust the ordinary primes. No rational-exponential assumption
is needed: this is the unchanged-clock survival ledger itself.
Necessity and sufficiency both follow by listing exactly the proven cores;
no terminal or infinite non-eventual packet has hidden positive H.

Permission restriction cannot turn one core's nonprime primitive into a
prime primitive, or manufacture a new core. It can cut unwanted cores
and hence alter which old data remain. Choosing E externally to retain
desirable data is not an endogenous arithmetic discovery. The conditional
survival criterion supplies no intrinsic sieve law or naturalness of E.

## 6. Parents A and B, each owned separately

For each control the parent is T(x)=2x on full R, with Lebesgue measure.
Its actual inverse is y/2 on all R. The frozen geometric every-point
Jacobian is1/2, including y=0, and for every Borel B
\[
 \mu(B/2)=\int_B(1/2)\,dy.
\]
Thus its own kappa_T=L=log2 at every source.
All signed iterates are 2^n x, all histories bilateral with one inverse
at every depth, and its complete arrows are
\[
 (2^{-k}y,k,y),\qquad c_T=kL,\qquad k\in\mathbb Z.
\]
Lag, clock and joint kernels are all units.

The zero singleton is the only periodic core and its entire incoming
packet. It has source isotropy Z, H=LZ, extension isotropy0, all phases
h modulo L and positive returns mL, m>=1.
Every nonzero state has a unique form epsilon 2^n u with epsilon=+/-,
u in[1,2), n in Z. For each fixed (epsilon,u) these states form one
complete bilateral parent packet, with zero source/extension isotropy
and H. Its full real phase is h+nL. Both signs and all real states
are covered. No nonzero state enters the zero packet.

## 7. Control A: remove only the zero outgoing permission

Here E=R without{0}. The actual Q inverse is y/2 on R without{0};
source restriction excludes only y=0. Its own every-Borel IMAGE is still
1/2 on that actual image, and its all-point clock is L at x nonzero.
The object0 remains but has no outgoing step and no incoming predecessor.

Every nonzero parent packet, arrow and bilateral history is unchanged.
The zero Q packet is a terminal singleton with only its unit. Thus the
exact arrow image consists of every parent arrow with nonzero endpoints
and the zero unit (0,0,0), but none of the nonzero-lag zero loops.
All three kernels are units. Every source/extension isotropy and H for
Q is zero. Nonzero packet phases are h+nL; the zero phase is h in R.
Positive-depth inverse histories of0 are empty, while all nonzero targets
retain their unique inverse at every depth.

The parent zero phase circle R/LZ has split into real Q phases, with the
natural map h to h modulo L. Full object retention has not preserved the
parent phase identifications. Q's complete positive ledger is empty,
so the nonemptiness part of the necessary benchmark fails.

## 8. Control B: a cut in one nonperiodic parent packet

Here E=R without{1}. The actual Q inverse is y/2 exactly for y not equal
to2, because only the predecessor1 loses permission. In particular target1
is retained with predecessor1/2 although it is itself a Q terminal.
The own every-Borel IMAGE is1/2 on that actual image, and kappa_Q=L at
every legal source x not equal to1.

All parent packets except the positive powers-of-two packet are unchanged.
In that packet write x_i=2^i, i in Z. The missing edge is x_0 to x_1.
The complete Q packets are
\[
 B_-=\{2^i:i\le0\},\qquad B_+=\{2^i:i\ge1\}.
\]
B_- ends at1 and has an infinite backward history; a state2^i with i<=0
has exactly -i remaining forward steps. Every depth of backward history
exists uniquely there. B_+ is a one-sided infinite forward chain beginning
at2, which has no Q predecessor; the backward depth at2^i is at most i-1.
Every other nonzero packet retains its bilateral history.
The parent zero fixed point remains a Q fixed point with all inverse depths.

Within either B_- or B_+, all arrows between x_i and x_j are
\[
 (2^i,j-i,2^j),\qquad c_Q=(j-i)L.
\]
There are no Q arrows crossing the two sets. Thus the exact parent image
omits precisely those crossing arrows in this one parent packet.
At every other parent packet its arrows are unchanged.
All three kernels are units. Each exceptional packet has zero source/
extension isotropy and H and full phase h+iL in R. The two phase families
are distinct Q families even where they map to the same parent real phase.

The zero packet still has source isotropy Z, H=LZ, extension isotropy0,
phase h modulo L and returns mL. It is the only positive Q packet.
Thus B satisfies the necessary one-log2 nonempty prime-only prime-unique
benchmark, but provides no all-prime coverage or arithmetic mechanism.

## 9. Control C: cut one outgoing edge on a two-cycle

Put s=sqrt2, a=log s and L=2a=log2. The parent on full R times Z/2 is
\[
 T(x,j)=(sx,j+1\bmod2).
\]
Its actual inverse is (y,f) to(y/s,f+1); geometric J=1/s at every point,
with sheet counting factor1. Scaling on each sheet proves every-Borel
IMAGE for this parent's Lebesgue-times-counting measure, so kappa_T=a.
All signed iterates are(s^n x,j+n mod2), and all arrows are
\[
 ((s^{-k}y,f+k\bmod2),k,(y,f)),\qquad c_T=ka,\quad k\in\mathbb Z.
\]
All three parent kernels are units. Every history is bilateral.

Let z_0=(0,0), z_1=(0,1). Their parent packet is the two-cycle with
source isotropy2Z, H=2a Z, extension isotropy0, phase h+ja modulo2a
and primitive L with all returns mL. No nonzero point enters it.
All nonzero parent packets, each counted once, are
\[
 \{(\epsilon2^n u,0),(\epsilon s2^n u,1):n\in\mathbb Z\},
 \qquad \epsilon=+/- ,\quad u\in[1,2).
\]
The unique sheet0 scale representative proves exhaustive, disjoint
coverage of both sheets and signs. Their isotropy and H are zero,
their histories bilateral, and a full phase is h+log(abs(x)) in R.

Q removes only the outgoing permission at z_1. Its actual inverse keeps
every parent target except z_0: on target sheet1 it is always(y/s,0);
on target sheet0 it is(y/s,1) only when y is nonzero.
The own IMAGE is1/s on each actual target domain, and kappa_Q=a at all
legal Q sources. The two zero objects now form the complete chain
\[
 z_0\longrightarrow z_1,
\]
with no predecessor at z_0, exactly z_0 as depth1 predecessor of z_1,
and no positive-depth history beyond that. The target z_1 needs no
outgoing permission to be retained as an actual image.

The complete zero arrows are the two units and
\[
 (z_0,1,z_1)\text{ with clock }a,\qquad
 (z_1,-1,z_0)\text{ with clock }-a.
\]
All other zero parent arrows, including every nonzero loop, are removed.
For example the first displayed arrow has the legal witness(m,n)=(1,0);
its parent witness(3,2) is forbidden under Q. The longer witness's failure
does not remove the arrow, illustrating why existence of a legal witness
is the exact criterion.

All nonzero parent arrows, packets and bilateral histories are unchanged.
The full Q lag/clock/joint kernels are units; every Q source/extension
isotropy and H is zero. The zero packet has full real phase h+ja, not
that coordinate reduced modulo2a. This agrees with the actual forward
clock subtraction at z_0 and projects to the parent's phase modulo2a.
Every nonzero packet keeps h+log(abs(x)) in R.
The entire positive Q ledger is empty; no absorbing core is created.

## 10. Control D: own inverse germs and complete parent source packets

Write \(f(x)=x^2+2\). The parent is f on R without{0}, on the full measured
object set R. Its two actual inverse germs are
\[
 \theta_+(y)=\sqrt{y-2},\qquad
 \theta_-(y)=-\sqrt{y-2},\qquad y>2.
\]
Their geometric all-point IMAGE versions are separately
\[
 J_+(y)=J_-(y)=\frac1{2\sqrt{y-2}},
\]
by the absolute derivative of each inverse. Ordinary one-dimensional
change of variables proves every-Borel IMAGE on either germ, with its
own orientation handled by the absolute derivative. These two densities
are not summed to define a source clock. They give
\[
 \kappa_T(x)=\log(2|x|)\qquad(x\ne0).
\]
Target2 is not in the inverse image domain, because its sole algebraic
preimage0 is an excluded source. The object2 is nevertheless a legal
forward source. Object0 is a terminal with no incoming branch.

On the positive half-line f is strictly increasing and maps (0,infinity)
onto(2,infinity). Also
\[
 f(x)-x=(x-\tfrac12)^2+\tfrac74>0.
\]
Every positive forward path is strictly increasing and tends to infinity.
Every negative source enters that positive region in one step.
Thus the parent has no periodic or eventual-periodic source and no
positive packet; this conclusion will not be inferred from a finite scan.

Every positive y has a unique finite backward chain by the positive germ
until a unique value u in(0,2] is reached. Indeed when a positive inverse
exists it decreases the coordinate by at least7/4, so it cannot continue
indefinitely. Its first point with no positive predecessor lies in(0,2].
Conversely f maps each u forward uniquely. Define
\[
 x_n=f^n(u),\quad n\ge0,\quad u\in(0,2].
\]
These positive sequences form a disjoint exhaustive partition of the
positive half-line into its positive-germ forward chains.

The complete NONZERO parent packet associated with u is
\[
 P_u=\{+x_n,-x_n:n\ge0\}.
\]
Its positive backbone is x_0 to x_1 to x_2 and so on. At every level n
there is a negative leaf -x_n whose sole outgoing step goes to x_{n+1}.
Negative states have no incoming, since the parent image is(2,infinity).
Both signs at level0 have no predecessor. At positive x_n, n>=1, the
two predecessors are exactly plus/minus x_{n-1}. These statements prove
coverage and disjointness of all P_u: absolute value belongs to exactly
one positive chain, and any signed orbit merges with that chain.
The only remaining parent packet is the terminal singleton{0}.

All incoming depths are explicit. At a positive target x_n and a depth
1<=m<=n, the initial predecessors are exactly plus/minus x_{n-m}, with
every intermediate state after the initial step positive. At m>n there
are none. A negative target has no positive-depth predecessor.
Thus there are no infinite backward histories anywhere; every nonzero
source has a one-sided infinite forward history, with the finite backward
extensions just listed. Choosing signs independently at intermediate
depths would invent histories; only the earliest source may be negative.

## 11. Control D: all parent arrows and all cancellation kernels

For its fixed u define
\[
 K_n(u)=\log(2x_n),\qquad
 A_0(u)=0,\qquad A_n(u)=\sum_{j=0}^{n-1}K_j(u)\quad(n\ge1).
\]
For either sign at level i, the legal n-step clock sum is
A_{i+n}-A_i. All arrows in P_u are exactly
\[
 (\epsilon x_i,j-i,\delta x_j),\qquad
 c_T=A_j-A_i,\qquad i,j\ge0,\quad\epsilon,\delta\in\{+,-\}.
\]
To see existence, let both signed states take positive numbers of forward
steps to a common sufficiently high positive level. This gives the stated
lag and clock. Necessity follows because once a nonzero state advances it
is on that same strictly increasing positive backbone. Two possible lags
would alternatively create an impossible nonzero source loop.
All different u packets have no arrows between them;0 has only its unit.

Consequently the full parent lag kernel is
\[
 \{(\epsilon x_i,0,\delta x_i):u\in(0,2],\ i\ge0,\
       \epsilon,\delta\in\{+,-\}\}\ \cup\{(0,0,0)\}.
\]
Its nonunit sign-merging arrows have zero clock. The joint kernel equals
this whole lag kernel. The CLOCK kernel is larger at exactly the following
exceptional roots, so it must not be identified globally with the lag kernel.

For n>=1 put
\[
 P_n(u)=\prod_{j=0}^{n-1}2f^j(u)=\exp(A_n(u)).
\]
It is continuous and strictly increasing in u>0. For each fixed n its
limit at u down to0 is0, because its first factor tends to0 and all
remaining finitely many factors have finite positive limits.
For n=1 it equals1 exactly at u_1=1/2. For n>=2 its value at1/2 is
strictly greater than1, since all the later x_j exceed2. The intermediate
value theorem and strict increase give a unique
\[
 u_n\in(0,1/2)\quad(n\ge2),\qquad P_n(u_n)=1.
\]
These are exact definitions, not numerical estimates. They satisfy
u_{n+1}<u_n: at u_n the next extra factor2x_n is greater than1.
Their limit is0, since for every fixed u>0 the products tend to infinity
as n increases, so eventually their roots are smaller than u.

For any fixed u, K_n>0 for n>=1. Hence A_n is strictly increasing on
n>=1, and equality of A_i,A_j with i!=j can only involve i=0 or j=0.
It occurs exactly for u=u_n and the other index n. Thus the complete
clock kernel consists of the lag kernel above and, for every n>=1,
every sign choice of the arrows
\[
 (\epsilon u_n,n,\delta f^n(u_n)),\qquad
 (\delta f^n(u_n),-n,\epsilon u_n).
\]
There are no other clock cancellations. In particular a zero-clock
nonzero-lag arrow between distinct states is not an isotropy loop and
does not create a physical period.

All parent source/extension isotropy and entire H are zero, including
at the exceptional u_n packets. For P_u the complete real phase is
\[
 h+A_i(u)\quad\hbox{at either sign of }x_i.
\]
An arrow from level j to level i changes height by A_j-A_i and preserves
that coordinate. It captures the zero-clock sign merges and exceptional
cross-level cancellations. The phase at the singleton0 is h in R.
There is no positive repetition at any source.

## 12. Control D: full Q owner after negative permission is removed

Here E=(0,infinity). The actual Q inverse atlas keeps only theta_+ on
y>2, with its own every-Borel IMAGE1/(2sqrt(y-2)) and all-point clock
\[
 \kappa_Q(x)=\log(2x)\qquad(x>0).
\]
It does not average, double or renormalize the two parent branches.
All x<=0 remain Q-terminal objects and have no incoming, since Q's image
is(2,infinity). They are singleton packets, not removed negative states.
There is no outgoing Q clock to assign at them.

Each parent's nonzero packet P_u splits into exactly one positive packet
\[
 P_u^+=\{x_n:n\ge0\}
\]
and the separate negative singleton packets{-x_n}, n>=0. The0 singleton
is unchanged. The positive packet is a one-sided infinite chain from u.
At x_n it has one predecessor of depth m exactly for0<=m<=n, namely
x_{n-m}; there is none at larger depth. Negative and zero singleton
objects have no positive-depth histories. No bilateral or infinite
backward history has appeared.

The complete positive-packet arrows are
\[
 (x_i,j-i,x_j),\qquad c_Q=A_j-A_i.
\]
Every negative/zero singleton has only a unit, and there are no other
Q arrows. This is precisely the legal-witness image in the parent:
all positive-positive parent arrows remain, all nonunit arrows involving
a negative leaf are lost. The lost negative sign-merging arrows are not
replaced by arrows between terminal singleton packets.

Q is injective on its source domain, so its lag and joint kernels are
units at EVERY object. Its clock kernel consists of all units plus,
at each exceptional u_n from Section11, exactly
\[
 (u_n,n,f^n(u_n)),\qquad(f^n(u_n),-n,u_n).
\]
These positive-state cancellation arrows remain actual Q arrows even
though the parent sign-merging arrows do not. Thus a claim that the
clock kernel is entirely units would be false for this control.

Every Q source/extension isotropy and entire H is zero. The phase on
P_u^+ is h+A_i at x_i. The phase on each negative singleton is its
unrestricted h, and at0 it is h. Under the natural map to parent phases,
the singleton{-x_i} coordinate h maps to h+A_i in the parent P_u;
the positive packet phase maps identically. This exhibits the full
additional phase splitting despite unchanged parent clocks on E.
Neither parent nor Q has a positive ledger. Both fail nonemptiness of
the necessary benchmark; no arithmetic source is supplied by this cut.

## 13. Bounded result and freeze

The restriction owns its complete source-filtered inverse atlas and
every-Borel IMAGE, with exactly the fixed parent all-point version on
actual restricted domains. Its clock and lag both embed without change,
but only the proved existential legal-witness parent arrows are retained.
Every terminal fibre, infinite intersection, kernel, isotropy group and
phase family is accounted for; relation inclusion is not phase injectivity.
The complete positive ledger consists exactly of parent cores whose
every phase is permitted, with unchanged least periods, signed sums,
entire H and packet multiplicity. The exact benchmark requires only
the three retained-core conditions above, not a rationality assumption.

The complete external controls show:

- A cuts the zero core while retaining0 as a terminal real-phase object.
- B cuts one nonperiodic packet into two, retaining the one log2 core.
- C turns the zero two-cycle into its complete terminal chain and removes
  its positive period without deleting either zero object.
- D retains a positive one-sided chain and all terminal negative leaves;
  its nonunit sign merges are removed but exact positive clock-cancellation
  arrows remain at the explicitly defined u_n. Both positive ledgers are empty.

These are conditional ownership/survival results, not endogenous discovery
of E. Same-object accounting remains intact for each parent/restriction
pair; source naturalness and PROVES_TOO_MUCH are not established.
Arithmetic T1 remains NOT PASSED, T3 NOT AUDITED, classical fields NOT
APPLICABLE, formal coordinates UNASSIGNED and Route B NOT INVOKED.
No operator, scientific census, old edit or465 work was undertaken.
After FULL self-read, freeze and return the receipt; HOLD for root FULL
raw read and a separate PAPER UNLOCK. No post-manuscript raw backfill.
