# 416 — card-only independent derivation

Candidate: ANG-20260923-DQS01. Date: 2026-09-23.
Batch SYNCHRONOUS-FEEDBACK-20260923-N; same-model shared-history NOT_CALIBRATED.
Root reported reading all 88 lines of CP1 and separately released raw mathematics.
Sole scientific input: original candidate-card.md lines 1–88, completely reread.
Original candidate-card.md — 88 lines; SHA256 bd5a2b43e45860c63ba40bce0ce311828837257f0917422a112d126f6b75a11c
Frozen scope-review.md — 88 lines; SHA256 6d6a7fa31adee66f96f155917d3d4f9d225bb4610e54573bf0a9e8d139b9f341
No author paper, README, ledger, outcome append, peer, sibling or old scientific
package was read. Prior shared history remains exposed, not blind or calibrated.
The full ARS router/workflow/role/reference/runtime instruction reads recorded
in CP1 are retained; they are not represented as newly read during this release.
AI supplied this derivation and checking. No mathematical code, numerical
experiment, external source, helper agent, Git action or extended census was used.

## 1. Full objects and actual inverse branches

Each owner keeps all \(X=\mathbb R^2\), \(\mu=dx\,dy\).
For y nonzero write \(a=\lfloor x/y\rfloor,b=\lfloor y\rfloor,r=y-bx\).
MAIN has \(D=\{y\ne0,r\ne0,a\ne0,a\mid b\}\) and
\(T(x,y)=(x/y-a,y-bx)\).
G has only y,r nonzero and the same successor formula.
P has D and \(1-ab\ne0\), with successor \((x-ay,y-bx)\).
S has y nonzero, a nonzero and a dividing b, with successor \((x/y-a,y)\);
its domain does NOT require r nonzero.
Every domain and partial map is Borel, since the floors and each branch are Borel.
The complement remains in X, with identity and all actual incoming but no step.
Undefined digits at y=0 and terminal-step clocks are not assigned artificial values.

For MAIN/G fix any integers a,b and write
\[
L=1-b(a+u),\qquad
\theta_{ab}(u,v)=\left(\frac{(a+u)v}{L},\frac vL\right).
\]
An actual source mapping to (u,v) has \(x=(a+u)y\) and \(v=Ly\).
Because y and v=r are nonzero, L is nonzero, and the displayed inverse follows.
The fractional quotient gives \(0\le u<1\).
Conversely impose these target conditions and all reconstructed own source,
floor and forward tests; substitution then gives exactly the actual predecessor.
This proves exhaustion over ALL integer a,b, including signed digits and zero
digits allowed by G. MAIN additionally keeps its a-nonzero/divisibility test.
No legal predecessor can have missing L=0 or v=0.

For P the two branch equations have coefficient matrix
\(\begin{pmatrix}1&-a\\-b&1\end{pmatrix}\), whose determinant is \(1-ab\ne0\).
Its inverse is precisely
\[
\theta^P_{ab}(u,v)
=\left(\frac{u+av}{1-ab},\frac{bu+v}{1-ab}\right).
\]
All a nonzero dividing b with this determinant condition are enumerated.
Testing the reconstructed D_P, both actual floors and the forward equation is
necessary and sufficient. There is no quotient-strip restriction on u for P.
For S, v=y and \(x=(a+u)v\); thus
\(\theta^S_a(u,v)=((a+u)v,v)\), for \(0\le u<1,v\ne0\),
with all own source and actual-digit checks. The integer b is then floor v;
it is not an extra inverse label. All nonzero a are tested.

Each displayed branch is injective: composing with its frozen branch forward
formula recovers (u,v). Its actual domain is a Borel subset of its analytic
denominator domain. Every actual source has unique actual digits, so equivalent
descriptions are identified and distinct labels cannot duplicate that source.
Targets need not be legal sources for the next step.
Each point has at most countably many predecessors in each owner.
No assertion of global injectivity is made.

## 2. Every-point analytic IMAGE and each own clock

For MAIN/G, differentiation on \(L\ne0,v\ne0\) gives
\[
D\theta_{ab}=
\begin{pmatrix}
v/L^2&(a+u)/L\\
bv/L^2&1/L
\end{pmatrix},\qquad
\det D\theta_{ab}=v/L^2.
\]
This is nonzero at every admitted point. The inverse branch is an analytic
local diffeomorphism, and injectivity makes it a diffeomorphism onto its image.
The direct branch derivative also gives
\(\det DT=(y-bx)/y^2=r/y^2\), consistently with the inverse formula.
For P the determinant of its linear inverse is \(1/(1-ab)\);
for S the determinant of its displayed inverse is v.
Consequently the prescribed full-point densities and positive forward factors are
\[
\begin{array}{c|c|c|c}
O&J_O(u,v)&B_O(x,y)=J_{\theta_{(x,y)}}(T_O(x,y))^{-1}&\kappa_O\\ \hline
\mathrm{MAIN},G&|v|/L^2&|y-bx|/y^2&\log|y-bx|-2\log|y|\\
P&1/|1-ab|&|1-ab|&\log|1-ab|\\
S&|v|&1/|y|&-\log|y|
\end{array}
\]
These values use the actual owner's reconstructed source and branch.
The J and B entries are positive finite on ALL admitted points, including
every floor face. The logarithmic clocks may have either sign or be zero.
Same-source descriptions have the same actual digits and analytic formula,
so no overlap has inconsistent J. S never imports MAIN's residual condition.

For every Borel E in an actual inverse domain, ordinary analytic change of
variables, restricted to that Borel set, gives
\[
\mu(\theta E)=\int_E J_O\,d\mu .
\]
If necessary use a countable local-diffeomorphism cover and disjoint Borel
pieces; injectivity keeps their images disjoint. Null faces are included.
The displayed analytic extension fixes J at those points; IMAGE alone would
not uniquely prescribe arbitrary null-set values. No such reassignment is made.
Floors need not make the global partial map differentiable across a face.
Every measure and coordinate convention remains the frozen one.

## 3. All legal histories, kernels and clocks

All definitions below use each owner's own map and full inverse atlas.
For a legal j-step history set
\[
R_j(z)=\prod_{i=0}^{j-1}B_O(T_O^iz),\quad R_0=1,\quad S_j=\log R_j.
\]
The full groupoid is
\[
G_O=\{(z,r-s,w):T_O^rz=T_O^sw,\ r,s\ge0,\ \text{both histories legal}\}.
\]
It is Borel by the countable union of Borel equal-iterate relations.
Its source and range fibres are countable by the countable inverse atlas.
Equal triples are identified; distinct integer lags remain.
Two presentations of the same triple differ by appending a common legal tail;
its equal product on both sides cancels. Therefore
\[
c(z,r-s,w)=\log\frac{R_r(z)}{R_s(w)}
\]
descends. To compose arrows, align the middle histories along their longer
already existing legal history; the middle products cancel. This proves closure
and additivity without extending a terminal. Inversion negates c.
The forward arrow \((T_Oz,-1,z)\) has clock \(-\kappa_O(z)\), as frozen.
Finite inverse-history densities multiply; a source-to-range history chart
has density \(R_s(w)/R_r(z)=e^{-c}\) by the all-point chain rule and IMAGE.

The COMPLETE kernels, on all actual triples, are
\[
\begin{aligned}
\ker\ell&=\{(z,0,w):T_O^rz=T_O^rw\text{ for some legal }r\},\\
\ker c&=\{(z,r-s,w)\in G_O:R_r(z)=R_s(w)\},\\
\ker\ell\cap\ker c
&=\{(z,0,w):T_O^rz=T_O^rw,\ R_r(z)=R_r(w)
                    \text{ for some legal }r\}.
\end{aligned}
\]
These are exact presentation-independent sets, not a unit-kernel assumption.
For all FOUR owners, take \(z=(1/4,1/4)\), \(w=(1/2,1/4)\).
Their own digits are respectively (1,0),(2,0), both sources are legal, and
both images are (0,1/4). Their factors are both 4 for MAIN/G/S and both 1 for P.
Thus \((z,0,w)\) is a nonunit arrow in both kernels and their intersection.
This collision is not a closed primitive and uses no outside-cell fixed census.

For S every history preserves y. At any actual arrow with y nonzero,
\[
c(z,k,w)=-k\log|y|,\qquad y(z)=y(w).
\]
Thus its full clock kernel there consists of k=0 or \(|y|=1\), intersected
with actual arrows; its lag/clock intersection is its full lag kernel.
At y=0 only identities exist and their empty-history clock is zero,
without defining a nonexistent step clock.
For MAIN/G, a legal r-step history with coordinates \(y_0,\ldots,y_r\)
has \(R_r=|y_r|/(|y_0|^2\prod_{i=1}^{r-1}|y_i|)\) for r>=1.
In particular a legal cycle has one-cycle clock \(-\sum_{i=0}^{r-1}\log|y_i|\).
For P the products use exactly the own integer factors \(|1-a_i b_i|\).
These are conditional full-history identities, not an extended cycle census.

## 4. Entire isotropy, incoming and every phase

A nonzero self-lag exists iff the deterministic forward history eventually
reaches a legal periodic core: two equal distinct-time iterates give such a
core, while every eventual cycle gives repeated equalities.
If its least source period is r, all self-lags are exactly rZ.
Let C be its least-core clock sum. Entrance sums cancel, so
\[
G_z^z=r\mathbb Z,\qquad H_z=C\mathbb Z.
\]
All integer multiples are realized after reaching the core; no proper subset
of loops is used. At non-eventually-periodic or terminal histories both are zero.
The full extension keeps every (z,h), with \((w,h)\mapsto(z,h+c)\).
Its isotropy at an eventual core class is \(\{kr:kC=0\}\); thus rZ is retained
if C=0 and it is trivial otherwise. Non-eventual extension isotropy is trivial.

For any source class, choose a reference b and any actual arrow \(g_z:z\to b\).
The phase of (z,h) is \(h+c(g_z)\) modulo \(H_b\).
Different choices differ by exactly a self-arrow clock at b.
Therefore height translation on the orbit SET has stabilizer precisely H.
If C differs from zero, the primitive is \(|C|\), with repetitions \(k|C|\),
k positive integer. If H=0 there is a free real phase line and no positive
primitive, even when ineffective source/extension isotropy remains.
No smooth or Hausdorff quotient, classical positive roof or physical ODE is claimed.

For ANY target z, enumerate every legal r and every length-s inverse word from
\(T_O^rz\) using Section 1. Its start w gives ALL incoming arrows
\((z,r-s,w)\), with source height \(h-c(z,r-s,w)\) for target height h.
This is an exact, all-depth, all-integer prescription. At a terminal only r=0
is allowed, but every actual backward word remains.

For later use define \(\mathcal P_O(z)\) by that complete own inverse atlas,
\(\mathcal P_O^0(z)=\{z\}\), and
\(\mathcal P_O^{j+1}(z)=\bigcup_{w\in\mathcal P_O^j(z)}\mathcal P_O(w)\).
Induction proves that these are exactly the starts of all legal j-step histories.
For an actual fixed core F its entire source packet is
\[
\mathcal B_O(F)=\bigcup_{j\ge0}\mathcal P_O^j(F).
\]
Indeed an arrow to F requires precisely eventual arrival at F.
Two different fixed cores cannot share a packet because their constant forward
tails cannot meet. A packet is countable; the set of different cores need not be.

Let d(z) be the first arrival time at F, \(K=\kappa_O(F)\),
\(\eta(z)=S_{d(z)}(z)\), and \(v(z)=\eta(z)-d(z)K\).
For ANY z,w in this basin and EVERY integer k, an arrow (z,k,w) exists by
choosing sufficiently long meeting times after both arrivals. Its clock is
\[
c(z,k,w)=v(z)-v(w)+kK.
\]
Thus source isotropy is all Z, entire H is KZ, and the basin clock kernel is
the displayed equality to zero. Its lag kernel has all (z,0,w); the intersection
adds \(v(z)=v(w)\). These statements retain all incoming coalescences.
At target (F,h), all incoming heights from z are \(h+v(z)-kK\).
The phase of (z,h) is \(h-\eta(z)\) modulo KZ, equivalently \(h-v(z)\).
Transient entrance clocks cannot reduce KZ to a smaller return-time group.

## 5. The TWO COMPLETE source-cell fixed tests

These are complete tests only inside the frozen C_10 and C_11, not globally.
In C_10, b=0 and y nonzero imply \(0<y<1\); a=1 means \(1\le x/y<2\).
MAIN and G fixedness imposes \(x=x/y-1\), with the second coordinate already y.
Hence \(x=y/(1-y)\). Its actual a=1 condition becomes
\(1\le1/(1-y)<2\), equivalent here to \(0<y<1/2\).
Every such point has r=y nonzero and MAIN's divisor permission, so conversely
each is a legal fixed source. S has the identical first-coordinate equation
and its own permitted source, hence gives exactly the same complete set.
Denote it by
\[
F_t=\left(\frac{t}{1-t},t\right),\qquad 0<t<1/2.
\]
Neither endpoint is silently omitted: t=0 violates the source and t=1/2
changes the actual quotient digit to 2, outside the tested cell.
For P in C_10 its first-coordinate fixed equation is x-y=x, impossible for
the required y nonzero. This control has no fixed point in that entire cell.

In C_11 one has \(1\le y<2\) and \(x\ge y>0\).
MAIN/G fixedness of y-bx with b=1 would force x=0, impossible.
For P the entire intersection with its own source is empty because 1-ab=0.
For S the first-coordinate equation is \(x(1-y)=y\).
At y=1 it is impossible, and for y>1 it would require x negative, contradicting
x positive. Therefore S also has no fixed point in the entire C_11.

The complete prescribed results are consequently
\[
\begin{array}{c|c|c}
O&\operatorname{Fix}(T_O)\cap C_{10}&\operatorname{Fix}(T_O)\cap C_{11}\\ \hline
\mathrm{MAIN}&\{F_t:0<t<1/2\}&\varnothing\\
G&\{F_t:0<t<1/2\}&\varnothing\\
P&\varnothing&\varnothing\\
S&\{F_t:0<t<1/2\}&\varnothing
\end{array}
\]
In particular P's empty own-domain intersection is not a MAIN result.

## 6. Whole incoming packets and primitive clocks of every found core

For MAIN, G and S, their separately computed own factors at F_t are all 1/t.
Put \(K_t=\log(1/t)>0\). Section 4 proves ENTIRE \(H=K_t\mathbb Z\) at each
core and every incoming point, source isotropy Z, trivial extension isotropy,
full phase circle \(\mathbb R/K_t\mathbb Z\), and primitive \(L=K_t\).
Positive repetitions are kK_t. These are not unverified one-loop lengths.

All incoming basins are the exact recursive sets \(\mathcal B_O(F_t)\) above,
using the DIFFERENT complete own atlases. In particular incoming sources are
not restricted to C_10 or C_11. To make their first layer explicit, put
\(u_t=t/(1-t)\in(0,1)\) and \(L_{ab}=1-b(a+u_t)\).
For MAIN its complete immediate predecessors are
\[
\left\{\left(\frac{(a+u_t)t}{L_{ab}},\frac t{L_{ab}}\right):
a,b\in\mathbb Z,\ a\ne0,\ a\mid b,\ L_{ab}\ne0,\
b\le t/L_{ab}<b+1\right\}.
\]
For G delete exactly the a-nonzero/divisibility restriction from this formula.
The quotient floor is a automatically because \(u_t\in(0,1)\);
r=t is nonzero, and the last inequalities impose precisely the other floor.
Necessity/sufficiency follows from Section 1, so no signed branch is omitted.
Every subsequent predecessor layer uses that full atlas at its own actual
target, not this first-layer simplification beyond its valid target.

For S its complete first layer is
\(\{((a+u_t)t,t):a\in\mathbb Z\setminus\{0\}\}\).
Here b=0 and every nonzero signed a divides zero.
All of its basin has y=t, so \(\eta(z)=d(z)K_t\) and v(z)=0.
Thus every basin arrow has c=kK_t; its clock kernel is exactly its lag kernel,
including all nonunit equal-lag coalescences. Its phase is h modulo K_t.
For MAIN/G the general v-difference formula retains all possibly different
entrance clocks rather than imposing S's simplification.
Each basin is countably infinite: the b=0 first layer already has infinitely
many distinct sources, and the complete finite-word atlas gives countability.
There are continuum many distinct fixed-core packets in each of these owners.
Equal source cores across DIFFERENT controls are never pooled into one owner.
Within each displayed family t determines K_t injectively; neither this fact
nor the two-cell calculation asserts global multiplicity outside the window.

## 7. Lineage, exact counterexample and disposition

At the frozen integer interface (dN,N), the actual digits are (d,N) and
\(r=N(1-dN)\ne0\). Thus MAIN's permission there is exactly d dividing N.
The current digits change the actual successor, whose geometry supplies the
next digits. This verifies the specified proper-divisor symbolic deformation,
not strong naturalness and not replacement of the full plane by this slice.
The inverse/J construction inserts no prime-dependent data or external roof.

Take t=1/4, so \(F_t=(1/3,1/4)\). Its actual digits are (1,0), it is legal
for MAIN, and direct substitution fixes it. Its OWN entire H is
\((\log4)\mathbb Z\), so its primitive is log4, not log of an ordinary prime.
The necessary target therefore FAILS already for this single complete packet.
The continuous family yields still more times; no extension of the cell or
higher-period census is needed or performed.
G and S have their independently owned same tested fixed clocks; P's empty
two-cell window gives no claim of global absence of periods or positive packets.

Same-object source/measure/clock/history conventions are intact for all four.
T0 and the specified analytic IMAGE clock ownership are established;
the necessary MAIN T2 prime-time condition fails. Strong naturalness and
PROVES_TOO_MUCH remain OPEN; untested fixed cells and higher cycles unclassified.
Classical NOT APPLICABLE; T3 NOT AUDITED; formal Route UNASSIGNED;
Route B NOT INVOKED. Candidate disposition: STOP / FORK, no local repair.
The decisive result was sent to root before this report was written.

EOF — frozen-card derivation only; full prescribed window, then HOLD for root read.
