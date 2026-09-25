# 421 — card-only independent derivation

Candidate: ANG-20260923-DBF01. Date: 2026-09-23.
Batch QUOTIENT-FEEDBACK-20260923-O; shared-history same-model NOT_CALIBRATED.
Root reported its full CP1 read and separately released this raw derivation.
Sole scientific input: clarified candidate-card.md, complete original lines 1–99.
candidate-card.md prefix — 99 lines; SHA256 f34fe85bdb784b9a2215c650ef5e11974825861ecb53c740213a1884ad220a5d
Frozen scope-review.md — 104 lines; SHA256 f4ad4b673bd6ec286facace5efa9f472a036ab3b866ea4475c362b16f1675d14
The card was completely reread after release; no author paper, README, ledger,
outcome, peer, sibling or old scientific file was accessed.
ARS instructions recorded in CP1 are retained, not represented as newly read.
Prior shared history and card-attributed scouting exposure remain disclosed;
this is neither blind, human, external nor cross-model verification.
AI supplied the derivation/checking. No helper, mathematical code, numerical
experiment, literature, external API, Git action or extended census was used.

## 1. Full four-owner definitions and exhaustive actual inverses

Every owner retains all \(X=\mathbb R^5\) and its own native Lebesgue5 measure.
Write \(z=(a,b,c,d,e)\), \(N=ac+bd\), \(m=\lfloor e\rfloor,n=\lfloor N\rfloor\).
MAIN requires \(m\ne0,m\mid n,c\ne0,e+qc\ne0\), with q=n/m, and maps
\[
Tz=(b,c,d,e,N/(e+qc)).
\]
G uses the same form with \(q_G=\lfloor n/m\rfloor\) if m is nonzero,
and q_G=0 otherwise, requiring only \(c\ne0,e+q_Gc\ne0\).
Q requires MAIN's arithmetic permission and \(c\ne0,e\ne0\), and maps
\(T_Qz=(b,c,d,e,N/e)\).
B retains MAIN's exact readout, quotient and domain, but maps
\(T_Bz=(b,c,d,e,ac/(e+qc))\).
All domains and maps are Borel. No illegal point is deleted: it has identity,
all actual incoming and no next step. Its nonexistent next clock is undefined.

Fix a target \(y=(u,v,w,s,t)\). Any predecessor has the first four recovered
source coordinates after its first entry equal to (u,v,w,s).
For MAIN/G put \(D_q=s+qv\). The last forward equation gives necessarily
\[
A_q=\frac{D_qt-uw}{v},\qquad
\theta(y)=(A_q,u,v,w,s).
\]
Its complete geometric tests are \(v\ne0,D_q\ne0\).
MAIN enumerates every \(m\ne0,n\) with m dividing n and q=n/m;
G enumerates every integer m,n with its own stated q_G rule.
In both cases require \(\lfloor s\rfloor=m\) and
\[
\lfloor A_qv+uw\rfloor=n .
\]
These checks recover precisely the actual own digits, permission and denominator.
Conversely every accepted source has numerator \(A_qv+uw=D_qt\), so
its actual forward image is exactly y. Any actual predecessor supplied those
same labels and formula. This proves necessity, sufficiency and exhaustion,
including G's m=0 branch and every signed/zero numerator allowed by an owner.

For B use MAIN's label set and geometric tests, but the actual inverse is
\[
A_q^B=D_qt/v,\qquad \theta^B(y)=(A_q^B,u,v,w,s).
\]
The source arithmetic numerator is STILL \(A_q^Bv+uw=D_qt+uw\),
not merely its transported product \(A_q^Bv\). The required floor test is
\(\lfloor D_qt+uw\rfloor=n\), together with floor s=m.
Then the owned transport numerator \(A_q^Bv=D_qt\) proves the inverse identity.
Conversely every actual B predecessor has exactly this formula and these tests.

Q has just one candidate
\[
\theta^Q(y)=((st-uw)/v,u,v,w,s).
\]
Its conditions are \(v\ne0,s\ne0\) and the reconstructed own arithmetic
permission: \(\lfloor s\rfloor\ne0\) and \(\lfloor s\rfloor\mid\lfloor st\rfloor\).
Indeed its reconstructed numerator is st, and dividing by the actual e=s
gives t. These conditions are both necessary and sufficient.
There is no extra quotient-indexed copy of this inverse.
In particular Q is globally injective as a partial map.

All actual inverse domains are Borel restrictions of the stated rational domains.
No target-next-step test is imposed. Targets may be terminals.
Each fixed-label inverse branch is injective: its last four outputs recover
(u,v,w,s), and its first output is affine in t with nonzero coefficient
\(D_q/v\) or s/v. Thus it also recovers t.
If two descriptions name one actual source, its own floors m,n and quotient
are unique. Equivalent descriptions are identified, not counted as new arrows.
Each target has at most countably many predecessors; no global injectivity is
claimed for MAIN/G/B.

## 2. Every-point rational IMAGE and the four own clocks

The derivative of \(\theta=(A,u,v,w,s)\) has its last four rows equal to
the first four coordinate rows. Expanding its determinant in the last column
gives \(+\partial A/\partial t\); the sign is positive after four transpositions.
Therefore
\[
J_{\mathrm{MAIN}/G/B}(y)=\left|\frac{s+qv}{v}\right|,
\qquad J_Q(y)=\left|\frac sv\right|,
\]
where q is the actual owner's accepted quotient.
These are strictly positive and finite everywhere on the admitted domain,
including its null floor faces. Their rational extensions are analytic with
nonsingular derivative on the open sets \(vD_q\ne0\), or \(vs\ne0\) for Q.
Injectivity makes each branch a diffeomorphism onto its image.
Same-source descriptions have the same actual q and therefore the same J.

For every Borel E in an actual inverse domain, analytic change of variables gives
\[
\mu(\theta E)=\int_EJ_\theta\,d\mu.
\]
One may partition E into disjoint Borel pieces subordinate to a countable local
diffeomorphism cover; injectivity keeps the image pieces disjoint.
Thus no openness of the floor-restricted domain, or removal of null faces,
is required. The analytic prescription fixes the point version there;
the measure identity alone is not claimed to determine arbitrary null values.
No measure replacement, null-point patch or omitted singular fibre occurs.

Let \(D_O(z)=J_{\theta_z}(T_Oz)^{-1}\) denote the own positive forward factor.
The exact legal-step factors and clocks are
\[
\begin{array}{c|c|c}
O&D_O(z)&\kappa_O(z)\\ \hline
\mathrm{MAIN}&|c/(e+qc)|&\log|c|-\log|e+qc|\\
G&|c/(e+q_Gc)|&\log|c|-\log|e+q_Gc|\\
Q&|c/e|&\log|c|-\log|e|\\
B&|c/(e+qc)|&\log|c|-\log|e+qc|
\end{array}
\]
Identical local expressions do not identify owners: B's actual successor and
future readouts differ from MAIN, and G has its own permission and q.
Positive density/factor does not mean positive clock. No independent roof,
classical conservative map or ordinary suspension is supplied.

## 3. Whole actual groupoid, kernels and compatible history densities

For each owner and legal j-step history set
\[
R_j(z)=\prod_{i=0}^{j-1}D_O(T_O^iz),\quad R_0=1,\quad S_j=\log R_j.
\]
Keep all actual triples
\[
G_O=\{(z,r-s,w):T_O^rz=T_O^sw,\ r,s\ge0,\ \text{both histories legal}\}.
\]
This is a countable union of Borel equal-iterate relations; source/range fibres
are countable by the complete inverse atlas. Equal triples are identified,
but lag is retained. Two presentations of the same triple differ by a common
legal tail. The equal tail products cancel, proving representation independence of
\[
c_O(z,r-s,w)=\log\frac{R_r(z)}{R_s(w)}.
\]
To compose arrows, align the middle histories using the longer already legal
history; the matching factors cancel. Closure and additivity follow without
continuing a terminal. Inversion changes the clock sign.
In particular \((T_Oz,-1,z)\) has clock \(-\kappa_O(z)\).
Finite inverse-word densities multiply by the all-point chain rule; on a
source-to-range history chart the density is \(R_s(w)/R_r(z)=e^{-c_O}\).
Every-Borel IMAGE therefore extends to those actual history restrictions.

The COMPLETE kernel sets are
\[
\begin{aligned}
\ker\ell&=\{(z,0,w):T_O^rz=T_O^rw\text{ for some legal }r\},\\
\ker c_O&=\{(z,r-s,w)\in G_O:R_r(z)=R_s(w)\},\\
\ker\ell\cap\ker c_O
&=\{(z,0,w):T_O^rz=T_O^rw,\ R_r(z)=R_r(w)
                         \text{ for some legal }r\}.
\end{aligned}
\]
Descent makes these presentation independent. For Q, injectivity of every legal
iterate implies \(\ker\ell\) and its intersection with the clock kernel are
exactly units. This conclusion is NOT transferred to MAIN/G/B.

Indeed put \(z_+=(1/4,0,2,0,1)\) and \(z_-=(-1/4,0,2,0,1)\).
For MAIN/G/B their actual (m,n,q) are (1,0,0) and (1,-1,-1).
Both are legal and map to \((0,2,0,1,1/2)\); both forward factors equal 2.
Thus \((z_+,0,z_-)\) is a genuine nonunit arrow in both kernels and their
intersection for these three owners. Q instead has the single inverse.
This exact collision check does not classify any extra periodic window.

## 4. Entire isotropy, phase and untruncated incoming

For any deterministic partial map, nonzero self-lag exists exactly when the
forward history eventually reaches a legal periodic core.
Equal distinct-time iterates give a periodic tail; conversely an eventual
period gives all its repeated self-equalities.
For least core period p, all self-lags are precisely pZ. If C is the
least-core sum of kappa, entrance sums cancel and every multiple is realized:
\[
G_z^z=p\mathbb Z,\qquad H_z=c_O(G_z^z)=C\mathbb Z .
\]
If there is no eventual legal period, source isotropy and H are both zero.
The full extension contains every \((z,h)\in X\times\mathbb R\), with
\((w,h)\mapsto(z,h+c_O)\). Its isotropy at an eventual-periodic object is
\(\{kp:kC=0\}\), namely pZ if C=0 and trivial otherwise.
Non-eventual extension isotropy is trivial.
Thus H=0 does not justify deleting nontrivial zero-clock isotropy.

For each source class choose a reference b and an actual arrow \(g_z:z\to b\).
The phase of (z,h) is \(h+c_O(g_z)\) modulo \(H_b\); different transports
differ by a loop at b. Height translation on the orbit SET has stabilizer
exactly H. For C nonzero its least positive generator is \(|C|\), with
repetitions \(k|C|\), k positive integer. If H=0 the phase is a free real line
and no positive primitive exists. No quotient manifold or regular topology
is inferred. Distinct source packets are not merged by equal clocks.

Define \(\mathcal P_O(y)\) using every actual inverse in Section 1 and recurse
\[
\mathcal P_O^0(y)=\{y\},\qquad
\mathcal P_O^{j+1}(y)=\bigcup_{v\in\mathcal P_O^j(y)}\mathcal P_O(v).
\]
Necessity and sufficiency of the one-step atlas prove by induction that these
are exactly the starts of legal j-step histories into y.
At any target z, ALL incoming arrows arise by choosing every legal r and
every \(w\in\mathcal P_O^s(T_O^rz)\), for every s>=0, with lag r-s.
For target height h their source height is \(h-c_O(z,r-s,w)\).
At a terminal r=0 only, but all actual backward words remain.
No integer/depth cutoff or window restriction appears in this prescription.

For any actual periodic core, cyclic rotations lie in the same source packet.
Every point in that packet is an actual eventual arrival at that core, and
conversely. Distinct periodic cycles, not cyclic rotations of one cycle,
cannot share a packet.
Choosing a reference phase on such a core and transporting by the displayed
clock determines every incoming phase; entrance factors cannot enlarge H.
A fixed core F would have phase \(h-S_a(z)\) modulo \(\kappa_O(F)\mathbb Z\)
when \(T_O^az=F\). This is conditional bookkeeping, not an assertion that
the prescribed window contains a core.

## 5. Two full-owner control identities: H_Q=H_B=0

On a legal period-p core, write its cyclic register sequence as \(x_i\),
with state i equal to \((x_i,x_{i+1},x_{i+2},x_{i+3},x_{i+4})\).
Indices are modulo p. Every legal state requires \(c=x_{i+2}\ne0\);
as i runs over the core, every cyclic register is nonzero.
This argument concerns actual periodic cores, not deletion of any zero-coordinate
source from the full owner.

For Q its core clock is
\[
C_Q=\sum_{i=0}^{p-1}\bigl(\log|x_{i+2}|-\log|x_{i+4}|\bigr)=0,
\]
since the two index shifts permute the same cyclic sequence.
For B the ACTUAL recurrence is
\[
x_{i+5}=\frac{x_ix_{i+2}}{x_{i+4}+q_ix_{i+2}}.
\]
All registers on this core are nonzero, so its OWN factor equals
\[
D_B(T_B^iz)=\left|\frac{x_{i+5}}{x_i}\right|.
\]
The product over a full core is one, hence C_B=0 as well.
The source-isotropy theorem now gives H_Q=H_B=0 at every source point:
eventual cores have zero cycle sum, and non-eventual histories have no self-lag.
All possible source isotropy survives in the extension; all phase lines are free.
This proves absence of positive clock primitives for these TWO controls only,
not absence of their source cycles and not a MAIN or G result.

Neither full clock cocycle is identically zero. For example
\(z=(0,0,1,0,2)\) is legal for both controls, with actual n=0,m=2,q=0 where used.
Its factor is 1/2, so its legal forward arrow has clock log2.
Its image \((0,1,0,2,0)\) is terminal because c=0.
Thus one cannot replace the full clock kernel by the entire groupoid, or assign
a zero next-step clock to that terminal. In particular the B factor ratio
\(|x_{i+5}/x_i|\) above is a core identity, not a formula dividing by zero
at arbitrary sources with a=0.

## 6. COMPLETE fixed sets inside the frozen union window

Let \(C_\pm=\{\lfloor e\rfloor=\pm1,\ \lfloor ac+bd\rfloor=2\}\)
and \(W=C_+\cup C_-\), with each owner's own legal-source tests.
A fixed point of ANY of these five-register shifts must have
\[
(a,b,c,d,e)=(t,t,t,t,t).
\]
The window then requires floor t equal to 1 or -1 and \(2\le2t^2<3\).
The complete possible diagonal parameters before the fixed equation are
\[
t\in[1,\sqrt{3/2})\quad\text{or}\quad t=-1 .
\]
All are nonzero. Here n=2, q=2 for floor t=1 and q=-2 for floor t=-1,
also for G, whose own rule agrees at these unit divisor labels.
MAIN/G/B denominators are \((1+q)t\ne0\); Q's is t.
Thus no remaining diagonal parameter is discarded by an unmentioned domain test.

For MAIN/G the final-coordinate fixed equation is \(t=2t/(1+q)\),
requiring q=1, contrary to q=2 or -2.
For Q it is t=2t, impossible for nonzero t.
For B it is \(t=t/(1+q)\), requiring q=0, again impossible.
Therefore all FOUR complete fixed intersections with W are empty.
Terminals in W remain objects, not additional fixed self-loops.

## 7. ALL four ordered length-two cell itineraries

Assume a legal two-step closed word z,w=T_Oz with both z,w in W.
The shift coordinates alone force
\[
z=(x,y,x,y,x),\qquad w=(y,x,y,x,y).
\]
This reduction is necessary for every real solution, not a selected ansatz.
The full common arithmetic readout is
\[
S=x^2+y^2\in[2,3),\qquad m_x=\lfloor x\rfloor,\ 
m_y=\lfloor y\rfloor,\qquad m_x,m_y\in\{1,-1\}.
\]
Thus x,y are nonzero; if their label is + they lie in [1,2), and if -
they lie in [-1,0). Arithmetic reads S also for B: it is NOT changed to x².
Set \(A_+=3,A_-=-1\). Then \(1+q_x=A_{m_x}\) and
\(1+q_y=A_{m_y}\) for MAIN/G/B.
All the reconstructed c and denominators for these hypothetical states are
nonzero, and unit divisibility is automatic. Own source tests are retained.

MAIN and G require, separately using their actual coincident window quotients,
\[
S=A_{m_x}xy=A_{m_y}xy.
\]
For +- or -+, the two A values differ; since xy is nonzero this is impossible.
For --, xy is positive and the right side is -xy<0, contrary to S>=2.
For ++, x,y>=1 gives S=3xy>=3, contrary to the STRICT window bound S<3.
This treats the included lower faces as well as all continuous interiors.
Consequently neither MAIN nor G has any of the four two-step words.

Q would require \(S=xy\). But
\[
x^2-xy+y^2=(x-y/2)^2+3y^2/4>0
\]
for the allowed nonzero y, so this is impossible for every sign itinerary.
No quotient label is inserted into Q's equation.

B instead requires
\[
y=x/A_{m_x},\qquad x=y/A_{m_y},
\]
since its transported numerator is x² or y², while the readout remains S.
Thus \(A_{m_x}A_{m_y}=1\).
The products are 9 for ++, -3 for either mixed word, and 1 only for --.
In the last case y=-x, impossible when x,y are both in [-1,0).
This exhausts B's entire two-step window.

Therefore for EVERY owner
\[
\{z:T_Oz\in W,\ z\in W,\ T_O^2z=z,\ \text{both steps legal}\}=\varnothing.
\]
Length-two closures would include repeated fixed points, but none occurs here.
No least-period-two core or primitive packet is invented from a solution of
an unchecked polynomial equation. Cyclic rotation and repetition conventions
are consequently vacuous in this window, not silently relaxed.
There is no found core whose incoming multiplicity could be selectively omitted;
the full incoming/phase prescription for all objects remains Section 4.

## 8. Lineage and the precise bounded disposition

For the frozen integers N0>=2 and 1<d0<N0, the source
\((N0-1,1,1,1,d0)\) has N=N0, c=1 and the readouts (n,m)=(N0,d0).
If d0 divides N0 its MAIN denominator is \(d0+N0/d0>0\);
otherwise the arithmetic permission fails. Thus the stated proper-divisor
interface is exact, and current digits actually alter the next geometric value.
All five shifted coordinates feed later readouts. This does not establish
strong naturalness, prime recurrence, or replace the full space by the interface.

All four owners pass the stated inverse/analytic IMAGE ownership check.
Their complete fixed and length-two probe is EMPTY, across ALL four itineraries.
An empty finite window neither violates MAIN's global nonempty positive-ledger
target nor proves that target, prime support, multiplicity or coverage.
Accordingly the precommitted decision is BOUNDED OPEN / FORK.
It is not a MAIN wrong-prime STOP and not an advance based on empty evidence.
Q/B's proved zero-H identities are owned control results, not a substitute
for a MAIN or G verdict. No other cell or longer-period census was performed.

Same-object source, measure, pointwise clock and full packet conventions remain
intact. T0 and the geometric-clock component are established; arithmetic
T1 NOT PASSED; MAIN T2 unresolved beyond this exact bounded empty window;
T3 NOT AUDITED; classical NOT APPLICABLE; formal UNASSIGNED; Route B NOT INVOKED.
No tuning, local repair, operator or new architecture is proposed in this record.
The decisive bounded result was sent to root before writing this report.

EOF — card-only raw derivation; preserve and HOLD for root read/PAPER UNLOCK.
