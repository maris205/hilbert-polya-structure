# VSA01 — independent card-only mathematical derivation

Candidate ID: ANG-AUDIT-20260924-VSA01.
Date label: 2026-09-24; batch RECURRENCE-OWNER-20260924-V, round5/5.
Reviewer: /root/pcr01_independent_review, separate from the author.

## 0. Input, release and evidence boundary

Sole newly read scientific input: the frozen95-line candidate-card.md,
SHA256 72facc556a4e30cebffd6970541b5b33a8748f5064445ec5faa7eb7906507c13.
It was FULL read through EOF at CP1 and reread through EOF for this raw.
CP1 scope-review.md has169 lines and SHA256
bd29c80d52760b2f9205a715358dda00ddc897a7e2b7ce24f8a3dd8e55715b8b.
Root separately released this derivation after its FULL CP1 read.
No459 author paper, README, ledger, helper result or current peer answer
has been read. No old proof/card was reopened. No scientific code, numerics,
network or Git was used. This file is the only write in the RAW stage.

The inherited443/448/454 review history and old overview exposure disclosed
at CP1 remain; this is not a memory-free or blind review. Same-model
shared-history checking is NOT_CALIBRATED, not human/external/cross-model
verification. ARS supplies bounded proof and disclosure discipline, not
an external certificate or authority to enlarge the frozen task.
All arguments below are exact symbolic arguments on the frozen class.
This raw must freeze before root FULL read and distinct PAPER UNLOCK.

## 1. Complete legal words and the new owner's IMAGE

Let D_n consist of points with a legal T-history of n steps, D_0=X.
An endpoint of an n-step history need not have an additional outgoing step.
The V domain is exactly the disjoint union
\[
 D_V=\bigcup_{n\ge1}\bigl(D_n\cap\{r=n\}\bigr).
\]
It is Borel. V is partial on the full X; every point outside D_V remains
an object with its unit and every actual incoming arrow.

For a length-n parent word \(\mathbf i=(i_0,\ldots,i_{n-1})\), define
\[
 Q_{\mathbf i,n}=\{x:r(x)=n,\ T^j x\in P_{i_j}\ (0\le j<n)\}.
\]
All stated iterates must be legal. These Borel pieces form a complete
countable disjoint partition of D_V: each legal source has one value of r
and exactly one parent source piece at each step of its requested word.
The restriction of T^n to each piece is injective.

Its inverse is reconstructed backwards. Set \(x_n=y\) and
\(x_j=I_{i_j}(x_{j+1})\) for j=n-1 down to0. Every inverse must be on its
actual image, and the reconstructed initial source must satisfy r(x_0)=n.
These tests define the actual Borel target image; the inverse is y to x_0.
No schedule test r(x_j) is imposed for 0<j<n. No outgoing permission at y
is imposed. The two inverse identities follow by the actual T identities.

On this branch prescribe the all-point version
\[
 J_{\mathbf i,n}(y)=\prod_{j=0}^{n-1}J_{i_j}(x_{j+1}).
\]
It is positive, finite and Borel at every actual target. For any Borel
subset B of the branch image, repeated inverse IMAGE identities give
\[
 \mu(I_{i_0}\cdots I_{i_{n-1}}B)
       =\int_B J_{\mathbf i,n}(y)\,d\mu(y).
\]
For completeness, the induction uses the parent identity extended from
indicator functions to nonnegative Borel functions: integration over an
inverse image is integration over its target with the appropriate J factor.
Apply it successively to the backward reconstructed coordinates, restricting
to B so every domain and source-schedule test is already satisfied. This
proves every-Borel IMAGE, including sets of infinite measure.

Therefore the prescribed version yields, at every legal V source,
\[
 \kappa_V(x)=-\log J_{\mathbf i,r(x)}(Vx)
       =\sum_{j=0}^{r(x)-1}\kappa_T(T^jx)=S_{r(x)}^T(x).
\]
This is an owned clock identity, not a division by r or an inserted roof.
The measure identity alone does not uniquely fix values on null sets;
the all-point prescription is a separate frozen input retained here.

## 2. General actual partial-map groupoid and physical phases

All assertions in this section apply separately to U=T and U=V with their
own actual domains and clocks. Write S_n only on legal histories and S_0=0.
An arrow \((z,m-n,w)\) has legal meeting \(U^mz=U^nw\); source is w,
range z, and equal triples, not labelled witnesses, are identified.

If two witnesses have the same lag, their two depths differ by the same
integer. Order them so the second depths are larger. The added legal
history starts at the same meeting point, and contributes the same clock
to both sums. Thus
\[
 c_U(z,m-n,w)=S_m^U(z)-S_n^U(w)
\]
is well defined. For composition, extend the shorter middle history to the
longer middle depth; the known longer history supplies precisely the legal
extension needed. Middle clock sums cancel. This proves additivity and
negation under inverses without adding a step at a terminal.
The forward arrow \((Uz,-1,z)\) has clock \(-\kappa_U(z)\).

The complete kernels are
\[
 K_{\rm lag}^U=\{(z,0,w):U^nz=U^nw\text{ legally for some }n\},
\quad K_c^U=\{g\in G_U:c_U(g)=0\},
\quad K_{\rm joint}^U=K_{\rm lag}^U\cap K_c^U.
\]
These include every actual merging arrow; zero lag need not mean a unit.
The full source packet of w is
\[
 [w]_U=\bigcup_{n\ {\rm legal\ at}\ w}\ \bigcup_{m\ge0}
             (U^m)^{-1}(\{U^nw\}),
\]
where inverse images use only legal histories. All finite predecessor
histories arise by repeated actual inverses; all compatible infinite
sequences give the infinite backward histories. No branch-name duplicates
are extra arrows.

A source has a nonzero-lag loop exactly when its forward path is eventually
periodic. Indeed unequal depths meeting along the same path give a repeated
state and hence an actual cycle; every such cycle supplies loops after entry.
If its eventual core has least U period ell and signed cycle sum W, then
\[
 \operatorname{Iso}_{G_U}(z)=\ell\mathbb Z,\qquad
 c_U(z,t\ell,z)=tW,\qquad H_z=W\mathbb Z.
\]
Both statements hold at every transient source feeding that core, not just
at periodic points. A transient point having groupoid isotropy is not itself
thereby a periodic point. Extension isotropy is ell Z if W=0, and zero
otherwise. A terminal or infinite non-eventual source has all isotropy and
H equal to zero.

Retain all of X times R, with arrows \((w,h)\mapsto(z,h+c_U(g))\).
Within one source packet choose a reference p and actual arrows \(g_z:p\to z\).
Put \(a_z=c_U(g_z)\). The full phases are
\[
 [h-a_z]\in\mathbb R/H_p.
\]
Changing a reference arrow changes a_z by H_p; changing reference translates
the coordinate. No global measurable selector or good quotient topology is
claimed. Vertical translation on the orbit set has exactly stabilizer H_p:
a translation t identifies the same extended orbit precisely via a source
loop with clock t. If W is nonzero, the least positive period is abs(W),
and every positive return is a positive integer multiple. If H=0 there is
no positive return, and phase is a full real coordinate.

For an eventual core, fix one of its points p. For each incoming z choose
any actual depth d_z with U^{d_z}z=p and put \(a_z=S_{d_z}^U(z)\).
All arrows in the entire incoming packet are exactly
\[
 (z,d_z-d_w+t\ell,w),\qquad
 c_U=a_z-a_w+tW,\qquad t\in\mathbb Z.
\]
Any meeting can be extended legally to p; conversely sufficiently large
added core turns realize every indicated lag. Consequently the full lag
kernel imposes d_z-d_w+t ell=0, the clock kernel imposes a_z-a_w+tW=0,
and the joint kernel imposes both. The full phase is h-a_z modulo WZ.
If W=0, incoming a_z may still differ; the whole clock need not be zero.

For a terminal packet with endpoint p, d_z is the unique remaining depth
to p. The analogous formula has no t term: its sole arrow from w to z
has lag d_z-d_w and clock a_z-a_w. Kernels impose equality of these depth
and/or clock labels, and phase is h-a_z in R.

For an infinite non-eventual packet, there is at most one arrow between
given endpoints, since two would yield a nonzero-lag loop. With any packet
reference choose its unique arrows, and denote their lags l_z and clocks
a_z. All arrows then have lag l_z-l_w and clock a_z-a_w. The three kernels
are their exact equality predicates, H and both isotropies vanish, and
phase is h-a_z in R. This is a packetwise description, not a chosen global
selector or an assertion that all parent packets remain whole under V.

## 3. Accumulated parent time and the exact arrow embedding

For every legal V history put
\[
 R_m(x)=\sum_{j=0}^{m-1}r(V^jx),\quad R_0=0.
\]
Induction and Section1 give
\[
 V^mx=T^{R_m(x)}x,\qquad
 S_m^V(x)=S_{R_m(x)}^T(x),\qquad
 R_{m+d}(x)=R_m(x)+R_d(V^mx)
\]
whenever the histories are legal. The sequence R_m is strictly increasing
because every r is a positive integer.

Define on a witnessed V arrow
\[
 \Phi(z,m-n,w)=(z,R_m(z)-R_n(w),w).
\]
It is an actual T arrow by the iterate identity. For another witness of
the SAME V triple, both macro depths are shifted equally. Their added
V history starts at the common meeting, hence their added R values agree.
Their difference is unchanged. This proves well-definedness.

The same legal middle-depth alignment used for composition in Section2,
now with the additive R identity, proves that Phi preserves composition
and inverse. Units and objects are unchanged. Its clock compatibility is
\[
 c_V(g)=c_T(\Phi(g)).
\]
In particular the forward V arrow maps to \((Vx,-r(x),x)\), with clock
minus the entire requested legal T-block sum.

Phi is injective, and positivity of r is essential to this argument.
If two V arrows with the same endpoints have the same image, their
composition with one inverse is a V loop mapped to a zero-lag T loop,
which is a unit triple. A nonzero-lag V loop has a witness with unequal
depths m,n at the SAME source z; strict increase of R at z gives
R_m(z)-R_n(z) nonzero. Thus a loop mapped to a unit has zero macro lag
and is itself a unit. The original two arrows are equal.
This establishes a groupoid embedding at the level of actual arrow sets,
not a topological/properness claim.

Here is its exact image, not just an inclusion. For each x let
\(\mathcal A_x=\{R_m(x):m\text{ is a legal V depth}\}\), retaining0.
Then
\[
 \operatorname{im}\Phi=
 \{(z,a-b,w)\in G_T:
       a\in\mathcal A_z,\ b\in\mathcal A_w,\ T^az=T^bw\}.
\]
The forward inclusion uses a V witness. Conversely the unique sampled
depth indices of a,b supply a V witness and the displayed image.
This may be a proper subgroupoid on the full object set.

An equivalent test works with any given T arrow (z,L,w). Its witnesses
have a least second depth n_0, with first depth m_0=n_0+L. All witnesses
are exactly (m_0+d,n_0+d) for nonnegative legal depths d on the common
parent tail: once two states meet, all their legal common extensions meet.
Thus the arrow is in the image iff
\[
 \exists d\ge0:\quad
 m_0+d\in\mathcal A_z,\quad n_0+d\in\mathcal A_w,
\]
with that shared parent-tail depth legal. This statement does not presume
that some such sampled time exists.

The complete V kernels can now be written without a constant-time error:
\[
 K_{\rm lag}^V=\{(z,0,w):
    T^{R_m(z)}z=T^{R_m(w)}w\text{ for some legal }m\},
\]
\[
 K_c^V=\{(z,m-n,w)\in G_V:
 S_{R_m(z)}^T(z)=S_{R_n(w)}^T(w)\},
\qquad K_{\rm joint}^V=K_{\rm lag}^V\cap K_c^V.
\]
Clock-zero is the pullback of parent clock-zero, but the macro lag-zero
predicate is equality of macro depths, not equality of R values.
The base-lag-zero pullback instead imposes R_m(z)=R_n(w).
Keep these distinct predicates even in controls where their kernels happen
to coincide. All actual merging arrows satisfying them remain.

## 4. Full weighted functional graphs over every parent core

Fix a least-q parent core \(x_j=T^jx_0\), j modulo q, and let
\[
 C=\sum_{j=0}^{q-1}\kappa_T(x_j),\qquad
 r_j=r(x_j),\qquad f(j)=j+r_j\pmod q.
\]
All q vertices remain, with the positive integer weight r_j on their one
outgoing edge. Every vertex of this finite functional graph eventually
enters a unique directed cycle; its complete basin includes all transients.
This is generally a function, not an assumed permutation.

For a directed cycle O of length ell, define
\[
 N_O=\sum_{j\in O}r_j,\qquad b_O=N_O/q.
\]
Closing the phase walk proves N_O is divisible by q; positivity gives the
integer b_O>=1. This is a winding count of actual parent time, not the
macro period ell and not the number of distinct parent phases visited.

Exactly the points x_j for j in O form one actual V core, with least
V period ell, accumulated parent time N_O=q b_O, and signed V clock
\[
 W_O=b_OC.
\]
Least macro period is ell because the ell phase vertices are distinct.
The clock identity follows by concatenating its legal T blocks: together
they traverse N_O consecutive parent steps, or b_O complete parent turns.
Each complete parent turn has signed sum C regardless of initial phase.

Conversely a V-periodic point satisfies T^N x=x for a positive accumulated
time N, so it is itself on a parent periodic core. Its V core is precisely
a cycle of that core's f. Distinct f cycles have distinct V cores, and
transient graph vertices supply no further cores. This proves both
coverage and multiplicity across all parent cores and all q phases.

For O the entire incoming V packet has source isotropy ell Z, extension
isotropy ell Z if b_OC=0 and zero otherwise, and
\[
 H_O=b_OC\,\mathbb Z.
\]
If C is nonzero the primitive is b_O abs(C), with all positive integer
repetitions, not ell abs(C) or a clock divided by a source period.
If C=0 all the source isotropy remains, H=0 and every real phase remains.

For any parent incoming x, let d be its first T arrival at this parent
core, at phase j. Its T future is infinite, so every V step is legal,
R_m is unbounded, and there is a least M with R_M(x)>=d. The first sampled
core phase is
\[
 j_x=j+R_M(x)-d\pmod q.
\]
This handles an overshoot past the first T arrival. After that sample,
the phase follows f exactly. Thus x lies in the full V packet of O iff
j_x is in the complete f basin of O. Every such source eventually reaches
that actual V core; every predecessor of the core satisfies this test.
This includes every parent backward branch and every graph transient.
Different eventual V cores cannot share a source or a full source packet.

For sharper arrow accounting in this packet choose a core point p. Set
d_z to any legal V depth with V^{d_z}z=p, \(B_z=R_{d_z}(z)\), and
\(A_z=S_{B_z}^T(z)\). Then all its arrows and images are
\[
 (z,d_z-d_w+t\ell,w)
   \ \stackrel{\Phi}{\longmapsto}\
 (z,B_z-B_w+tN_O,w),\qquad
 c=A_z-A_w+t b_OC,\quad t\in\mathbb Z.
\]
The phase is h-A_z modulo b_OC Z. The full lag/clock/joint kernels impose,
respectively, zero macro lag, zero displayed clock, or both.
The parent arrows between the same endpoints instead have all lags
B_z-B_w+tq. Thus at source loops the embedded V lag subgroup is
N_O Z inside qZ, of index b_O, even when C=0 makes both clock images zero.
No inference of full parent-arrow coverage follows merely from full X.

Changing the reference parent phase just relabels all q actual points.
If new label u denotes old label u+h, its graph is
\(f'(u)=f(u+h)-h\pmod q\) and weight \(r'_u=r_{u+h}\).
This is an isomorphism of the ENTIRE weighted graph, including transients.
It is not the noninjective fibre transport from a different lift problem.
The actual V cores, winding counts, incoming packets, clocks and phases
therefore do not depend on the reference label.

## 5. Terminal and infinite non-eventual parent classes

Suppose x has exactly N_T(x) legal parent steps until its terminal e_T.
Compute samples recursively from R_0=0. At sampled state T^{R_m}x a next
macro step exists iff
\[
 R_m+r(T^{R_m}x)\le N_T(x).
\]
If so add that positive integer; otherwise stop. The finite sequence has
a last index M(x), with R_M<=N_T(x), and its V endpoint is
\[
 e_V(x)=T^{R_M(x)}x.
\]
It is an actual V terminal, which need not be a T terminal. Positivity
ensures termination in at most N_T(x) macro steps. At a parent terminal
M=0, and no fictive successor is introduced.

Every V-terminal point is in a parent terminal class: if the requested
finite T block is illegal, the parent forward path stops before its end.
Hence the full terminal V packets are exactly the nonempty fibres of the
actual endpoint function e_V. A parent terminal packet can split into
several of these packets; no endpoint is discarded.
For a V endpoint e, all its actual incoming depths are exactly the z with
V^{M(z)}z=e. Put \(A_z=S_{R_{M(z)}(z)}^T(z)\). All arrows in that packet
have macro lag M(z)-M(w), parent lag R_{M(z)}(z)-R_{M(w)}(w), and clock
A_z-A_w. Source/extension isotropy and H are zero; phase is h-A_z.
The full three kernels are the exact depth/clock equality conditions.
On each such packet Phi includes every parent arrow between its endpoints,
since that parent arrow is unique; arrows joining different V endpoints
within one parent terminal packet are omitted.
All backward histories are the actual inverse-word recursion of Section1.

Now let the parent path be infinite and not eventually periodic. Every
requested finite block is legal, so the V forward path is infinite and
R_m tends to infinity. A V repetition would be a positive-time T repetition
by strict increase of R, which is impossible. Thus there are no V source
loops, positive packets or extension isotropy above such parent sources.

For z,w in the same such parent packet, there is one parent arrow and a
least meeting pair (a_0,b_0). The exact common sampled-tail condition is
\[
 \{R_m(z)-a_0:R_m(z)\ge a_0\}
 \ \cap\
 \{R_n(w)-b_0:R_n(w)\ge b_0\}\ne\varnothing.
\]
The common parent tail never repeats, so equality of these offsets is
equivalent to equality of the sampled actual states. This condition is
necessary and sufficient for a V arrow; no automatic synchronization is
assumed. Once a sampled meeting occurs, deterministic V continuation has
the same subsequent schedule on both sides. All its later witnesses
therefore have the same macro lag and the same clock.

This sampled-tail relation partitions each non-eventual parent packet into
the complete V packets. In each use the unique-reference-arrow formula
of Section2 to obtain all lag/clock/joint kernels and all real phases.
Nonunit merges at equal macro depth, if present, remain actual arrows;
lack of source isotropy does not remove them. All finite and infinite
incoming histories remain the actual inverse-word recursion. On a fixed
V packet Phi maps onto all parent arrows between its endpoints, but it
omits parent arrows between different sampled-tail classes.

The three parent cases above exhaust all sources: a deterministic partial
forward path either terminates, repeats eventually, or is infinite without
eventual repetition. Thus no unexamined source stratum can add a positive
V packet to the periodic ledger of Section4.

## 6. Exact prime benchmark and rational boundary

Index distinct parent periodic cores by Gamma, counted once modulo phase.
For each nonzero signed parent sum C_Gamma and each cycle O of its complete
weighted phase graph, retain the full V packet with primitive
\[
 L_{\Gamma,O}=b_{\Gamma,O}|C_\Gamma|,\qquad
 b_{\Gamma,O}=\frac1{q_\Gamma}\sum_{j\in O}r(x_j)\in\mathbb N_{\ge1}.
\]
This is the complete positive ledger, with multiplicities. Distinct pairs
remain distinct packets even if their primitive lengths are equal.
Every finite graph has a cycle. Therefore this ledger is nonempty iff
some parent core has nonzero C. Zero-clock cores and non-eventual/terminal
parent packets cannot contribute a positive primitive.

Without rationality the exact prime-only test is
\[
 \exp(|C_\Gamma|)^{b_{\Gamma,O}}\text{ is an ordinary prime for every pair}.
\]
Prime uniqueness means at most one pair yields each prime. These are
necessary and sufficient directly from the full ledger.

Under the card's hypothesis \(M_\Gamma=\exp(|C_\Gamma|)>1\) rational,
write M=u/v in lowest positive terms. If M^b=p prime, then
u^b=p v^b forces v=1 by coprimality, and unique integer factorization
forces b=1 and u=p. Conversely M=p and b=1 give the prime p.
Thus the nonempty, prime-only, prime-unique benchmark holds exactly when:

1. Some parent core has nonzero C.
2. Every nonzero parent multiplier is an ordinary prime.
3. Different nonzero parent cores have different prime multipliers.
4. Each nonzero parent's full weighted graph has exactly one cycle, and
   that cycle has winding count b=1, equivalently its edge weights sum to q.

Necessity of the last uniqueness condition uses that a finite graph has
at least one cycle; two winding-one cycles above one prime parent duplicate
that prime. Sufficiency follows by listing the one retained packet from
each distinct parent prime. All other phase vertices may be transient,
and their incoming source states stay in the packet. No permutation or
constant-step assumption is silently added.

Equivalently the parent itself must satisfy the necessary nonempty
prime-only prime-unique benchmark, and every nonzero weighted graph must
have exactly one winding-one cycle. Arbitrary zero-clock graphs are
unrestricted by this positive-ledger condition. All-prime coverage is the
additional requirement that the set of these parent primes is all primes.
In particular rational nonprime parent multipliers cannot be repaired by
positive finite advancement, and parent duplicate primes cannot be removed
by dropping their mandatory nonempty return graphs.

The rational step does not extend to irrational multipliers. Algebraically,
M=p^(1/b) with b>1 is compatible with M^b=p, so only the general power
criterion is asserted there. This identifies the boundary of the implication;
it is not a new external control or a construction of an arithmetic source.
Zero C, negative C and all signed isotropy-clock multiples are retained;
only the least positive generator uses absolute value.

## 7. Parents of A, B and C: complete own measured accounting

For each control separately put \(s=\sqrt2\), \(a=\log s\), \(L=2a=\log2\).
Its full owner is R times Z/2 with Lebesgue times counting, and
\[
 T(x,j)=(sx,j+1).
\]
The actual inverse at target (y,f) is (y/s,f+1). For every Borel target
set on that sheet, its inverse measure is 1/s times its measure.
Thus own geometric all-point J=1/s and kappa_T=a, including x=0.
This argument applies independently to each of the three specified owners.

All signed iterates are \(T^n(x,j)=(s^nx,j+n\bmod2)\). All arrows are
\[
 ((s^{-k}y,f+k\bmod2),k,(y,f)),\qquad c_T=ka,\quad k\in\mathbb Z.
\]
All three kernels are units. Every point has its unique bilateral history;
there are no terminals or additional backward branches.

At x=0 the sole full parent packet is its two-cycle. Source isotropy is
2Z at either point, H=2a Z=LZ, extension isotropy is zero, and the full
phase coordinate is h+j a modulo2a. Its positive returns are mL, m>=1.
No nonzero real point can enter it.

For x nonzero write uniquely \(x=\epsilon s^n\rho\), epsilon in {-,+},
rho in [1,s), n in Z. Existence and uniqueness follow by the unique integer
n with s^n<=abs(x)<s^(n+1). A full parent nonzero packet fixes
(epsilon,rho,b), b=j-n modulo2, and consists of
\[
 (\epsilon s^n\rho,b+n\bmod2),\quad n\in\mathbb Z.
\]
This includes both signs and exhausts every nonzero state. Source and
extension isotropy and H are zero, and all phases are h+n a in R.
These formulas also enumerate every incoming depth by negative iterates.

## 8. Control A: schedules (1,1)

Here V=T on the entire two-sheet space. Its actual inverses, own every-Borel
IMAGE and all-point clock are exactly the formulas just derived, since
the requested legal word has length1 on each source.
All histories, arrows, unit kernels and phases are precisely those of
Section7, without any omitted source or extra branch multiplicity.
Phi is the identity on arrows.

The zero parent phase graph is the two-cycle with both edge weights1:
least V period2, N=2, winding1, cycle clock L, H=LZ and extension
isotropy zero. The entire incoming packet is the same two zero states,
with phase h+j a modulo L and repetitions mL.
All nonzero packets remain the bilateral (epsilon,rho,b) packets of Section7
and have no positive return. No terminals exist.
The complete positive V ledger has exactly one log2 packet.
A satisfies the necessary nonempty prime-only prime-unique benchmark,
but neither all-prime coverage nor endogenous arithmetic is supplied.

## 9. Control B: schedules (2,2)

Here V(x,j)=(2x,j), total and bijective. Its actual inverse is (y/2,j)
on each target sheet. Each own every-Borel inverse IMAGE is1/2, equal to
the product of the two parent factors, and kappa_V=L everywhere.
All signed iterates are \(V^n(x,j)=(2^nx,j)\), giving
\[
 ((2^{-k}y,f),k,(y,f)),\qquad c_V=kL,\qquad
 \Phi\text{ has parent lag }2k.
\]
All three kernels are units; all histories are unique and bilateral.
This is a proper subgroupoid of the parent's arrow set despite full X.

At the parent zero two-cycle the phase graph has two fixed vertices,
each edge of weight2. Each gives one zero singleton V packet: least
V period1, N=2, winding1, source isotropy Z, H=LZ, extension isotropy0,
phase h modulo L and every positive return mL. There is no other incoming
state to either zero singleton.

Every nonzero state belongs uniquely to a packet
\[
 \{(\epsilon2^n\rho,j):n\in\mathbb Z\},
 \quad\epsilon\in\{-,+\},\quad\rho\in[1,2),\quad j\in\mathbb Z/2.
\]
Source and extension isotropy and H vanish; phase is h+nL in R.
In the parent's (epsilon,rho,b) indexing from Section7, each nonzero
parent packet splits into the two parity classes of its index n.
This also explicitly shows nonsynchronizing parent histories under V.
There are no merging branches or terminal histories.
The full positive V ledger has TWO log2 packets, so prime uniqueness fails.

## 10. Control C: schedules (1,3)

On the entire space,
\[
 V(x,0)=(sx,1),\qquad V(x,1)=(s^3x,0),\qquad V^2(x,j)=(4x,j).
\]
The actual inverse at target sheet1 is (y/s,0), with own IMAGE1/s;
at target sheet0 it is (y/s^3,1), with own IMAGE1/s^3.
These are every-Borel change-of-scale identities, also on sets containing0.
Thus kappa_V(x,0)=a and kappa_V(x,1)=3a at every source.
V is total and bijective, with exactly one inverse history at every depth.

Here is a complete signed-iterate and arrow formula, including negative
indices without a parity ambiguity. For n=2t+delta, delta in {0,1},
t an arbitrary integer, put
\[
 B_n(j)=4t+\delta(1+2j).
\]
Then \(V^n(x,j)=(s^{B_n(j)}x,j+n\bmod2)\). The formula agrees with
both actual inverse branches and with V squared, so holds for every n in Z.
For a target sheet f and macro lag k define \(A_k(f)=-B_{-k}(f)\);
explicitly
\[
 A_{2t}(f)=4t,\qquad A_{2t+1}(f)=4t+3-2f.
\]
The complete arrows and clocks are
\[
 ((s^{-A_k(f)}y,f-k\bmod2),k,(y,f)),\qquad
 c_V=a A_k(f),\qquad \Phi\text{ has parent lag }A_k(f).
\]
The formula derives by taking V^{-k} of the target and summing its signed
legal parent time. For macro lag1 the parent lag is3 at target sheet0
and1 at target sheet1, so no constant multiplier of macro lag describes
this embedding. A_k(f)=0 iff k=0; all three kernels are units.

The zero phase graph is one two-cycle, with weights1 and3. Its least
V period is2, accumulated parent time4, winding2 and cycle clock4a=2L.
Its full incoming packet is both zero states and nothing else. Source
isotropy is2Z, H=4a Z, extension isotropy is zero, and every phase is
h+j a modulo4a. Indeed the sheet0 step subtracts a and advances j;
the sheet1 step subtracts3a, consistent modulo4a with returning to j=0.
The primitive is4a=log4, with positive returns4ma, not log2.
The embedded parent isotropy is4Z inside the parent's2Z.

Every nonzero V packet has unique labels (epsilon,rho), rho in [1,4),
by choosing its sheet0 scale representative, and consists of
\[
 z_{2t}=(\epsilon4^t\rho,0),\qquad
 z_{2t+1}=(\epsilon s4^t\rho,1),\qquad t\in\mathbb Z.
\]
For a given sheet1 state divide its real coordinate by s before taking
the unique factor4 representative. Thus this list covers all real nonzero
states, both signs and both sheets, with no selected section as an owner.
Its source/extension isotropy and H vanish, and its full real phase is
h+(4t+delta)a at z_{2t+delta}. Both transition clocks preserve it.
Every history is bilateral; inverse depths are exactly the signed iterates.

In a fixed nonzero parent packet, sheet0 indices have one parity and two
residue classes modulo4. Each residue class produces the pair of sampled
residues n_0+4t at sheet0 and n_0+4t+1 at sheet1. Therefore each such
parent packet splits into exactly two V packets, not into a single parent
packet by assumed synchronization. No extra merging or terminal branch exists.
The complete positive V ledger is one log4 packet; prime-only support fails.

## 11. Control D: partial translation and early macro stopping

The parent is T(x)=x+1 exactly on (-2,0), with full object set R and
Lebesgue measure. Its actual inverse is y-1 exactly on image(-1,1).
Translation gives own every-Borel IMAGE J=1 and all-point kappa_T=0.
Parent terminal points are (-infinity,-2] union [0,infinity), not absorbing
fixed points.

The full parent packets and their finite histories are:

- For t in(0,1), the three-point chain t-2 -> t-1 -> t.
- The two-point chain -1 -> 0.
- A singleton at every terminal t<=-2 or t>=1.

These sets exhaust R, including -2,-1,0,1. The interior of(-2,-1)
has two legal parent steps, the interval[-1,0) has one, and all other
points have zero. Every backward history is a truncation of these displayed
chains; none is infinite and none has an omitted predecessor.

For a chain with endpoint t, write its states t-i for the available depths
i. All parent arrows are
\[
 (t-i,i-j,t-j),\qquad c_T=0
\]
for all its available i,j; singleton packets have just a unit.
The lag kernel and joint kernel are units because each chain has one point
at each depth; the clock kernel is the entire groupoid. Source and extension
isotropy and H are zero everywhere. Each packet's full phase is h in R,
and there is no positive primitive or positive repetition.

Now r(x)=1 for x<-1 and r(x)=2 for x>=-1, on ALL R.
For sources x<-1 a legal V word exists exactly at x in(-2,-1).
For sources x>=-1 the requested two parent steps are never both legal:
the two-step parent domain is(-2,-1), disjoint from those sources.
Consequently
\[
 D_V=(-2,-1),\qquad V(x)=x+1,\qquad V(D_V)=(-1,0).
\]
Its sole actual inverse is y-1 on(-1,0), with own every-Borel IMAGE1
and kappa_V=0. There is no source using the length2 branch, and no next-step
test removes the target(-1,0) from this length1 image.

The full V packets are the two-point chains
\[
 u-1\longrightarrow u,\qquad u\in(-1,0),
\]
and singleton objects at every x<=-2, at x=-1, and at every x>=0.
This exhausts all of R. Its parent triples for t in(0,1) split into
the V pair {t-2,t-1} and singleton {t}; the parent pair {-1,0} splits
into two singletons. The V endpoint t-1 in(-1,0) still has a legal parent
step, but its requested length2 V step is illegal. No endpoint is removed.

For each pair, all arrows are its units and
\[
 (u-1,1,u),\qquad (u,-1,u-1),
\]
all with zero clock. These are the full incoming histories of length1;
there are no positive-depth histories at the singleton objects and no
infinite histories. The lag and joint kernels are units, the clock kernel
is the whole V groupoid, and all isotropy and H vanish. Every phase is
h in R, with no positive return. Phi is the inclusion of these arrows
in the parent groupoid, with the same lag on actual legal words; it omits
the parent links from u to u+1 and from -1 to0 and their composites.
Both parent and V fail nonemptiness of the positive benchmark.

## 12. Bounded conclusion and freeze boundary

The variable-step class owns every inverse-word IMAGE and its accumulated
clock. The proposed Phi is a well-defined injective, clock-compatible
actual groupoid map with the exact sampled-time image above, not generally
the whole parent arrow set or a constant scaling of lag.
Every parent cycle contributes all cycles of its entire weighted phase
graph; their winding counts, not their macro lengths alone, determine
physical primitives. All graph transients, terminal classes and sampled
non-eventual classes have been retained with full kernels and phases.
The rational benchmark has the necessary and sufficient conditions of
Section6. Controls A/B/C/D respectively give one log2 packet, duplicate
log2 packets, one log4 packet, and no positive packet.

These are conditional transport laws and complete EXTERNAL controls, not
a prime-symbolic source or arithmetic admission. Same-object accounting
remains intact for each owner. Strong naturalness and PROVES_TOO_MUCH
remain OPEN. Classical fields are NOT APPLICABLE, arithmetic T1 NOT PASSED,
T3 NOT AUDITED, formal coordinates UNASSIGNED, and Route B NOT INVOKED.
No operator, zero work, scientific census or460 has been undertaken.
Freeze this raw after FULL self-read; send only its receipt and HOLD
until root FULL read and a separate PAPER UNLOCK.
