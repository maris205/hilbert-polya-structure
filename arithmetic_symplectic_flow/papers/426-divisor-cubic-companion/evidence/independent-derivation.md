# 426 — card-only independent derivation

Candidate: ANG-20260923-DCC01. Date: 2026-09-23.
Batch SYMMETRY-FEEDBACK-20260923-P; same-model shared-history NOT_CALIBRATED.
Root reported its full CP1 read and separately released this raw mathematics.
Sole scientific input: candidate-card.md, original lines 1–99, completely
reread after release; only that prefix was read, not any possible later append.
candidate-card.md prefix — 99 lines; SHA256 d69f92855c83ca9fc9e73cb02e4839fe85079f22c51bb823abefa84441c268b4
Frozen scope-review.md — 91 lines; SHA256 b9a85b8af7aedb41900c637d814078d6a41611775957a9fda203f0387e0ce49e
No author paper, README, ledger, outcome, peer, sibling or old scientific
artifact was read. Prior shared history remains exposed, not blind.
ARS instructions recorded in CP1 are retained, not claimed as freshly read.
AI supplied this derivation and checking; no helper, mathematical code,
scientific numerics, literature/API call, Git action or higher-period search.
This is internal work, not external/human/cross-model verification.

## 1. Every owner and ALL signed-q cubic components

All three owners retain \(X=\mathbb R^3\), its Borel structure and Lebesgue3.
At \(z=(a,b,c)\), let \(m=\lfloor a\rfloor,n=\lfloor bc\rfloor\).
MAIN has \(m\ne0,m\mid n,q=n/m,\Delta=3a^2+q\ne0\) and
\(Tz=(b,c,a^3+qa)\).
G uses \(q_G=\lfloor n/m\rfloor\) if m is nonzero and q_G=0 otherwise,
with only \(3a^2+q_G\ne0\) required, and the corresponding cubic successor.
L has MAIN arithmetic permission and q nonzero, with
\(T_Lz=(b,c,qa)\); the cubic Delta condition is NOT its source test.
Every domain and map is Borel. Illegal and critical sources remain objects
with identities and all incoming, but no next step or next-step clock.

For any integer q put \(P_q(r)=r^3+qr\). Its regular components and FULL images are:

| q | Ordered regular components I | Corresponding images P_q(I) |
| --- | --- | --- |
| q>0 | \(\mathbb R\) | \(\mathbb R\) |
| q=0 | \((-\infty,0),(0,\infty)\) | \((-\infty,0),(0,\infty)\) |
| q<0 | \((-\infty,-h),(-h,h),(h,\infty)\) | \((-\infty,V),(-V,V),(-V,\infty)\) |

In the last row \(h=\sqrt{-q/3}>0\), \(V=2h^3\).
Indeed \(P_q'=3r^2+q\). It is strictly positive for q>0;
for q=0 its only zero is zero; for q<0 its zeros are \(\pm h\),
with positive, negative, positive signs on the three listed intervals.
Limits at infinity and \(P_q(-h)=V,P_q(h)=-V\) give all the image endpoints.
Thus each restriction is one-to-one onto its stated open interval.
The inverse function theorem gives a real-analytic inverse \(\rho_{q,j}\)
at every point of that full image, since its derivative never vanishes.

Every regular real solution of \(P_q(r)=w\) lies in exactly one component,
and that component supplies exactly its inverse value. This proves geometric
root exhaustion, including all signed q, not selection of one real root.
At w=V or -V for q<0, the critical endpoint root is excluded as a legal
source, but the regular root 2h or -2h lies in the opposite outer component
and is still enumerated. Its actual arithmetic permission must then be tested.
Hence a critical VALUE is not used to delete an entire target fibre.
Critical source points themselves stay in X as frozen terminals.

## 2. Actual atlas, own source checks and all-point IMAGE

At target \(y=(u,v,w)\), every predecessor has the form \((r,u,v)\).
For MAIN enumerate ALL \(m\ne0,n\) with m dividing n, q=n/m, and each j.
Retain \(r=\rho_{q,j}(w)\) iff w is in the stated component image,
\(\lfloor r\rfloor=m,\lfloor uv\rfloor=n\), and the own legal tests hold.
Then \(P_q(r)=w\) proves the exact forward identity.
Conversely any actual predecessor supplies precisely its own m,n,q and
regular component, so this procedure exhausts all actual predecessors.
For G perform the identical component construction using all integer m,n
and its own q_G, including m=0, without importing MAIN's divisibility.
Its reconstructed floor tests again supply precisely the actual own source.

L enumerates MAIN's labels with q nonzero, sets
\(\theta^L_{m,n}(u,v,w)=(w/q,u,v)\), and checks the two source floors.
This is necessary and sufficient for its actual linear law.
It imposes neither a cubic branch index nor the unused Delta condition.
In every owner the target may itself be terminal: only the reconstructed
source is tested for the step under consideration.
An actual source fixes its floors and its own q uniquely; a regular cubic
source lies in only one component. Duplicate names never add arrows.
All actual inverse domains are Borel and the countable atlas has no cutoff.
Every target has at most countably many actual predecessors.

Each cubic inverse branch is \(\theta(u,v,w)=(\rho_{q,j}(w),u,v)\).
Its derivative determinant is \(\rho_{q,j}'(w)\), since the coordinate
cycle has positive sign. Differentiating \(P_q(\rho(w))=w\) gives
\[
J_{\rm MAIN}=J_G=\frac{1}{|3\rho(w)^2+q|}.
\]
L's own derivative gives \(J_L=1/|q|\).
All are positive finite at EVERY admitted point; no uniform bound near a
critical endpoint is claimed or needed. These formulas extend analytically
on each full geometric branch domain, before floor restrictions.
The branch is injective, with analytic inverse \((r,b,c)\mapsto(b,c,P_q(r))\),
or its linear counterpart for L. Same-source descriptions have the same
actual q/component and hence consistent derivative and J.

For every Borel E in the actual inverse domain, analytic change of variables
restricted to that Borel subset proves
\[
\mu(\theta E)=\int_EJ_\theta\,d\mu.
\]
If local charts are used, take a countable cover and disjoint Borel pieces;
injectivity keeps the image pieces disjoint. All null floor faces are included.
Their point version is fixed by the analytic prescription, not by claiming
that an almost-everywhere density uniquely determines null-point values.
The native measure is unchanged; no periodic-point repair occurs.

The own positive factors and legal clocks are therefore
\[
D_{\rm MAIN}=|3a^2+q|,\quad D_G=|3a^2+q_G|,\quad D_L=|q|,
\qquad \kappa_O=\log D_O .
\]
The cubic clocks can be signed or zero. L's is nonnegative because its own
nonzero q is an integer, but it need not vanish. These are not inserted roofs.
For example (1,-3,1) has m=1,n=-3,q=-3: L is legal with its own factor 3,
whereas the cubic Delta is zero. Keeping this L step is required, not a repair.

## 3. Complete actual history, kernels and extension

For each owner define on legal histories
\[
R_j(z)=\prod_{i=0}^{j-1}D_O(T_O^iz),\quad R_0=1,\quad S_j=\log R_j .
\]
The entire retained-lag groupoid is
\[
G_O=\{(z,r-s,w):T_O^rz=T_O^sw,\ r,s\ge0,\ \text{both histories legal}\}.
\]
It is Borel as the countable union of legal equal-iterate relations, and its
source/range fibres are countable by the full inverse atlas.
Equal triples, not extra history labels, are identified.
Two presentations of one triple append the same legal common tail;
its matching products cancel. Therefore
\[
c_O(z,r-s,w)=\log(R_r(z)/R_s(w))
\]
is well-defined. Aligning the middle histories on their longer existing
legal history proves closure and additivity without continuing a terminal.
Inversion negates c. The actual forward arrow \((T_Oz,-1,z)\) has
clock \(-\kappa_O(z)\).
All finite inverse-history densities multiply, and a source-to-range history
chart has density \(R_s(w)/R_r(z)=e^{-c_O}\) by the chain rule and IMAGE.

The COMPLETE kernels are the following sets of actual triples:
\[
\begin{aligned}
\ker\ell&=\{(z,0,w):T_O^rz=T_O^rw\text{ for some legal }r\},\\
\ker c_O&=\{(z,r-s,w)\in G_O:R_r(z)=R_s(w)\},\\
\ker\ell\cap\ker c_O
&=\{(z,0,w):T_O^rz=T_O^rw,\ R_r(z)=R_r(w)
                          \text{ for some legal }r\}.
\end{aligned}
\]
They retain all branch coalescences; no globally unit lag kernel is assumed.
Below L's fixed-core basin gives an explicit nonunit member of the intersection.

A nonzero self-lag exists exactly for an eventually periodic legal future.
Equal distinct-time iterates produce that periodic tail, and every eventual
cycle produces repeated equalities. If its least source period is p and
least-core clock sum is C, all self-lags are precisely pZ and
\[
G_z^z=p\mathbb Z,\qquad H_z=C\mathbb Z .
\]
All multiples are realized and prefix sums cancel. A non-eventually-periodic
or finite-terminal history has trivial source isotropy and H=0.
In the full \(X\times\mathbb R\) extension, \((w,h)\mapsto(z,h+c_O)\);
its isotropy is \(\{kp:kC=0\}\), all pZ if C=0 and trivial otherwise.
Non-eventual sources have trivial extension isotropy.
Thus zero clock retains, rather than deletes, ineffective source isotropy.

For a source class choose a reference b and an actual arrow \(g_z:z\to b\).
The phase of (z,h) is \(h+c_O(g_z)\) modulo \(H_b\).
Changing the transport adds exactly an element of H; height translation on
the orbit SET has stabilizer exactly H. When C is nonzero the primitive is
\(|C|\), with positive repetitions \(k|C|\). H=0 has no positive primitive
and gives a free real phase line, whether or not source isotropy is ineffective.
No regular topological or manifold quotient is inferred.

## 4. Every incoming history and full fixed-core formulas

Let \(\mathcal P_O(y)\) be ALL accepted inverse points from Section 2, and set
\[
\mathcal P_O^0(y)=\{y\},\qquad
\mathcal P_O^{j+1}(y)=\bigcup_{v\in\mathcal P_O^j(y)}\mathcal P_O(v).
\]
The one-step inverse identities prove by induction that these are exactly all
starts of legal j-step histories into y. At a generic target z, all incoming
arrows are obtained by every legal r and every \(w\in\mathcal P_O^s(T_O^rz)\),
s>=0, with lag r-s. For target height h, the source height is h-c_O.
At a terminal only r=0 is legal; every actual backward word still remains.
This prescription has no floor, branch, depth or cube cutoff.

For an actual fixed core F its entire source packet is
\(\mathcal B_O(F)=\bigcup_{j\ge0}\mathcal P_O^j(F)\):
an arrow to its constant future is precisely eventual arrival at F.
Different fixed cores cannot share a packet.
Let d(z) be the first arrival time, \(K=\kappa_O(F)\),
\(\eta(z)=S_{d(z)}(z)\), and \(v(z)=\eta(z)-d(z)K\).
For any z,w in this basin and EVERY integer k, sufficiently late common
meeting times after arrival give an arrow (z,k,w), with
\[
c_O(z,k,w)=v(z)-v(w)+kK .
\]
Thus the basin lag kernel consists of all (z,0,w); its clock intersection
adds v(z)=v(w), and its full clock kernel is the displayed equality to zero.
Entire H at every incoming point is KZ, not enlarged by entrance clocks.
The fixed-reference phase is \(h-\eta(z)\) modulo KZ, equivalently h-v(z).
At (F,h), all incoming source heights from z are \(h+v(z)-kK\).
These formulas also apply when K=0, retaining every lag and real phase.

## 5. COMPLETE MAIN/G fixed sets in the CLOSED cube

Write \(\mathcal C=[-2,2]^3\). A fixed source of either cubic shift must be
\((t,t,t)\), with \(t=t^3+qt\). At t=0, MAIN fails m nonzero;
G uses q=0 but fails Delta nonzero. Thus the origin is not a legal fixed point.
For t nonzero the fixed equation requires \(q=1-t^2\).
Both own q rules are integer-valued, so \(k=t^2\) is a positive integer.
The CLOSED cube bound gives exactly k=1,2,3,4; all signs must be tested.

| t | m | n | MAIN q | G q | Required 1-k | Actual fixed owners |
| --- | --- | --- | --- | --- | --- | --- |
| -2 | -2 | 4 | -2 | -2 | -3 | neither |
| \(-\sqrt3\) | -2 | 3 | not permitted | -2 | -2 | G |
| \(-\sqrt2\) | -2 | 2 | -1 | -1 | -1 | MAIN and G |
| -1 | -1 | 1 | -1 | -1 | 0 | neither |
| 1 | 1 | 1 | 1 | 1 | 0 | neither |
| \(\sqrt2\) | 1 | 2 | 2 | 2 | -1 | neither |
| \(\sqrt3\) | 1 | 3 | 3 | 3 | -2 | neither |
| 2 | 2 | 4 | 2 | 2 | -3 | neither |

The floor signs in the negative rows are ordinary signed floors, not truncation.
In particular MAIN never receives G's q at the nondivisible (-2,3) label.
The actual surviving derivatives are \(3(2)-1=5\) and \(3(3)-2=7\);
both are legal. This proves the complete intersections
\[
\operatorname{Fix}(T_{\rm MAIN})\cap\mathcal C=\{F_2\},\quad
\operatorname{Fix}(T_G)\cap\mathcal C=\{F_2,F_3\},\qquad
F_k=(-\sqrt k,-\sqrt k,-\sqrt k).
\]
Every continuous possibility was reduced by its actual fixed equation;
no floor face or outer cube endpoint is omitted.

## 6. COMPLETE L fixed set and its own full control clock

A fixed L source is again (t,t,t). Since m is nonzero, t is nonzero.
Fixedness requires q=1, hence \(n=m\).
As n=floor(t²) is nonnegative and m is nonzero, m must be positive.
In the cube, t>=1 and t<=2. For m=1 the condition n=1 gives
\(1\le t<\sqrt2\); at t=2, m=2 but n=4 and the condition fails.
No negative t can have n=m. Therefore
\[
\operatorname{Fix}(T_L)\cap\mathcal C
=\{E_t=(t,t,t):1\le t<\sqrt2\}.
\]
Each actual source has q=1 and its OWN factor 1, so its clock is zero.
The included t=1 and excluded t=sqrt2 are consequences of the exact floors,
not endpoint deletions. The unused cubic Delta never enters this classification.

In fact the full L control has H=0 at EVERY source, without a period census.
For any legal cyclic register sequence x_i of source period p,
every x_i is nonzero because floor of the first coordinate must be nonzero.
Its actual recurrence is \(x_{i+3}=q_i x_i\), hence
\(\prod_i|q_i|=\prod_i|x_{i+3}/x_i|=1\).
The complete cycle sum is zero. The generic isotropy theorem then gives
H=0 also for incoming tails and for non-eventually-periodic/terminal objects.
All possible source isotropy remains in the extension; no positive clock
primitive exists for L. This is not absence of L source cycles.
Nor is its full cocycle zero: for example (1,2,1) has q=2 and clock log2
on its legal step. No such control identity is transferred to MAIN or G.

## 7. FULL unrestricted incoming of EVERY found core

At target F_2, the source product readout n=floor(uv)=2 is fixed.
For MAIN its possible m are the ALL signed divisors 1,2,-1,-2.
For positive m the reconstructed a is positive and q positive, so
\(a^3+qa>0\), inconsistent with the negative target.
For m=-1, a lies in [-1,0), q=-2 and \(a^3-2a>0\).
For m=-2, a lies in [-2,-1), q=-1. The function \(a^3-a\) is strictly
increasing there, and a=-sqrt2 supplies the unique required value.
Thus \(\mathcal P_{\rm MAIN}(F_2)=\{F_2\}\), and its full basin is singleton.

For G at F_2 ALL m>=0 again give nonnegative output (including m=0,q=0).
The m=-1 case has the same positive output as above.
Every m<=-2 has q_G=-1 and a<-1; \(a^3-a\) is strictly increasing
on this entire unbounded interval. Its unique target solution is -sqrt2.
Thus \(\mathcal P_G(F_2)=\{F_2\}\), with singleton full basin.

At F_3 for G, n=3. ALL m>=0 give nonnegative output.
For m=-1, q_G=-3 and \(a^3-3a>0\) on [-1,0).
For m=-2, q_G=-2 and \(a^3-2a\) is strictly increasing on [-2,-1);
a=-sqrt3 supplies its unique target value.
Every m<=-3 has q_G=-1 and a<-2, so \(a^3-a<-6<-\sqrt3\).
Consequently \(\mathcal P_G(F_3)=\{F_3\}\) and the full basin is singleton.
These are unrestricted source checks, not inverse searches truncated to the cube.

For any L fixed E_t, \(1\le t<\sqrt2\), the target has n=1.
ALL permitted m are 1 or -1. With m=1,q=1 the source a=t is legal.
With m=-1,q=-1 the source is a=-t; its floor is -1 exactly when t=1.
Therefore the full first predecessor set is \(\{E_t\}\) for t>1, and
\(\{E_1,U\}\) for t=1, where \(U=(-1,1,1)\).
At target U one has n=floor((-1)1)=-1.
For m=1,q=-1 the proposed a=-1 has the wrong floor; for m=-1,q=1
the proposed a=1 has the wrong floor. These are all signed divisors of -1.
Thus U has no predecessors, proving the ENTIRE basins
\[
\mathcal B_L(E_t)=\{E_t\}\ (1<t<\sqrt2),\qquad
\mathcal B_L(E_1)=\{E_1,U\}.
\]
The legal U-to-E_1 clock is log|-1|=0. All basins above have therefore been
exhausted at every depth, including the extra endpoint source and empty predecessor ends.

## 8. Complete packet clocks, phases and bounded decision

MAIN F_2 and G F_2 each have, in their OWN singleton basin, source isotropy Z,
entire \(H=(\log5)\mathbb Z\), trivial extension isotropy and phase circle
\(\mathbb R/(\log5)\mathbb Z\). G F_3 has the corresponding group and circle
with log7. Their positive primitives are log5 and log7, with integer repetitions.
The whole H, not just one loop, was computed; no shorter prime-power clock is
inserted. Both 5 and 7 are ordinary primes. The G packet is not MAIN evidence.

Every L fixed basin has source and extension isotropy Z and H=0.
All its arrow clocks are zero within that basin, by its just-proved incoming
description; every real phase remains. At E_1 the distinct U point is retained,
and \((E_1,0,U)\) is a nonunit arrow in both kernels and their intersection.
For the singleton cubic basins the clock and lag kernels restrict to units.
For L's fixed basins the full clock kernel is the whole basin groupoid,
while the lag and joint kernels contain all actual zero-lag pairs.
Different t give different source packets despite their identical zero clocks.
These exact basin statements do not replace the generic whole-source kernels.

At the integer interface (d,N,1), actual m=d,n=N give arithmetic permission
exactly d dividing N. When it holds, \(q=N/d>0\) and
\(\Delta=3d^2+N/d>0\), so the geometric gate also holds there.
This verifies the stated proper-divisor interface and actual nonlinear feedback,
not strong naturalness of the readout, polynomial, measure or critical termination.

MAIN has a genuinely owned log5 primitive, so its positive ledger is NONEMPTY.
Its complete fixed window has no wrong-prime or duplicate prime packet.
This does NOT establish global prime purity, uniqueness of the log5 packet
outside the window, or all-prime coverage. No other fixed region, period-two
or higher search was performed. L's zero-H control does not condemn MAIN,
and G's log7 packet cannot be borrowed into it.
The precommitted disposition is therefore BOUNDED OPEN / FORK with an owned
prime witness, not a global target pass, wrong-prime STOP or automatic advance.

Same-object source, native measure, analytic clock and full packet ledger remain
intact. Geometric ownership is established; arithmetic T1 NOT PASSED and
strong naturalness/PROVES_TOO_MUCH remain OPEN; T3 NOT AUDITED;
classical NOT APPLICABLE; formal UNASSIGNED; Route B NOT INVOKED.
The decisive result was sent to root before this report was written.

EOF — card-only raw derivation; HOLD for root's full read and PAPER UNLOCK.
