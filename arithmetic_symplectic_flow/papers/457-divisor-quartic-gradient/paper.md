# An owned quartic-interaction clock with a composite two-step packet

Candidate ID: ANG-20260924-DQG01. Paper 457, version 1.
Outcome: OWNED QUARTIC IMAGE; COMPOSITE TWO-STEP RETURN — STOP / FORK
Date: 2026-09-24. Batch RECURRENCE-OWNER-20260924-V, round 3/5.
Type: measured Borel partial map, retained-lag groupoid and real cocycle extension.
Classical symplectic/suspension fields: NOT APPLICABLE. T3: NOT AUDITED.
Formal Route coordinates: UNASSIGNED. Route B: NOT INVOKED.

## Abstract

We audit a synchronous quartic-interaction map whose current divisibility
quotient changes both real coordinates. On the complete plane with its
original area measure we construct every actual inverse, its analytic
pointwise IMAGE version, and the full history cocycle. In the frozen square,
MAIN has no fixed points, permission-OFF has one zero-clock fixed point, and
interaction-OFF has one fixed point with primitive time \(\log35\).
The separately prelisted word is an actual least-period-two MAIN orbit.
Each of its steps has full area multiplier \(5\), but its entire isotropy
clock group is \((\log25)\mathbb Z\), not \((\log5)\mathbb Z\).
All incoming roots, phases, and repetitions are retained. Its composite
primitive \(\log25\) stops MAIN without extending the return search.

## 1. Frozen ownership and arithmetic source

The governing [candidate card](candidate-card.md) is the original 92-line
prefix through its EOF marker, SHA256
a47a223d611a59ba999d10664b2262f7eac8c012bbd32539843fafff4f85771a.
The [claim ledger](claim-ledger.md) records scoped results and limits.
The root-managed [review record](evidence/review.md) is not an author input.

Every owner has \(X=\mathbb R^2\), its usual Borel structure, and original
Lebesgue area \(\mu=dx\,dy\). At a source \(z=(x,y)\) read
\[
m=\lfloor x\rfloor,\qquad n=\lfloor y\rfloor.
\]
MAIN requires \(m\ne0,\ m\mid n\), and uses the signed integer \(q=n/m\).
For a fixed integer label define
\[
V_q=\frac{x^4+y^4}{4}+\frac q2x^2y^2+xy,\qquad
F_q(x,y)=(x^3+qxy^2+y,\ y^3+qx^2y+x).                 \tag{1}
\]
The actual MAIN map \(T_M\) uses \(F_q\) only where its own complete
two-dimensional derivative is nondegenerate.
The permission-OFF owner G uses the same polynomial family with
\[
q_G=\begin{cases}\lfloor n/m\rfloor,&m\ne0,\\0,&m=0,\end{cases}
\]
and only its own derivative guard, not MAIN's divisibility condition.
The interaction-OFF owner Q retains MAIN arithmetic permission but always
uses \(F_0=(x^3+y,y^3+x)\), with its own \(DF_0\) guard.
The unused arithmetic quotient does not label extra Q inverse branches.

All signs, axes, units, zero quotients, integer cuts and critical points
remain objects in \(X\). An illegal source has its unit and every incoming
arrow but no next step or next-step clock. It is not an absorbing fixed point.
A target need not itself permit an outgoing step.
Although \(F_q=\nabla V_q\) at fixed \(q\), no global smooth gradient across
readout cuts, symplectic map or Hamiltonian time-flow is asserted.

For integers \(N,d\) with \(N\ge2,\ 1<d<N\), the source \((d,N)\) has
MAIN arithmetic permission exactly when \(d\mid N\). The geometric guard is
checked in §2. Thus the exact interface is proper-divisor symbolic admission,
current quotient in synchronous quartic interaction, real transport of both
coordinates, and fresh arithmetic readout. There is no independent integer
register, selected prime set, external clock or per-prime parameter.
Formula/readout naturalness remains a separate OPEN question.

The only return window is complete fixed-point classification in
\(W=[-2,2]^2\), including its cuts and boundary, followed by the prelisted
word at \(P=(1,-1)\), \(Q_0=(-1,1)\). The whole plane remains the carrier;
all incoming histories range outside \(W\) without cutoff.

## 2. Full derivative, exact inverses and the IMAGE atlas

Differentiate at fixed \(q\), without differentiating floors:
\[
DF_q(x,y)=
\begin{pmatrix}
3x^2+qy^2&1+2qxy\\
1+2qxy&3y^2+qx^2
\end{pmatrix},\qquad
\Delta_q=(3x^2+qy^2)(3y^2+qx^2)-(1+2qxy)^2.           \tag{2}
\]
This determinant uses both original coordinates. For Q, its own determinant
is \(\Delta_0=9x^2y^2-1\), regardless of its unused arithmetic quotient.
Each owner's domain is its arithmetic/quotient domain intersected with its
actual polynomial regular locus, a Borel set.

At an admitted integer seed \(x=d,\ y=N=qd\), one has \(q,d\ge1\), and
expanding (2) gives
\[
\Delta_q(d,qd)
=3q(q^4-q^3+3q+1)d^4-4q^2d^2-1
>q^2d^2(9d^2-4)-1>0.                                \tag{3}
\]
Here \(q^4-q^3\ge0\), and the omitted \(3q\) contribution is strictly
positive; the last bound follows already from \(q,d\ge1\).
Thus actual MAIN admission on the stated proper-divisor interface is
exactly \(d\mid N\), with no hidden geometric exception. Q's own guard there
is also nonzero because \(9d^2N^2-1>0\).

For MAIN/G target \((u,v)\), enumerate every integer \(q\) and every real
solution of
\[
x^3+qxy^2+y=u,\qquad y^3+qx^2y+x=v.                   \tag{4}
\]
Retain precisely its actual source floors, own quotient/permission,
\(\Delta_q\ne0\), and forward equality. This is necessary for an actual
predecessor by (1), and sufficient by substitution; no preferred root or
target-next-step check is included.
For Q solve instead all real roots
\[
(u-x^3)^3+x-v=0,\qquad y=u-x^3,                       \tag{5}
\]
and retain its own arithmetic and \(\Delta_0\ne0\) checks.
Elimination of \(y\) proves (5) is equivalent to \(F_0(x,y)=(u,v)\).
It is solved only once, not once per unused label.
Identical actual points are deduplicated. Write \(\mathcal P_O(u,v)\) for
the resulting full predecessor set for owner \(O=M,G,Q\).

For each fixed-label polynomial use the card's ordered rational open balls
with closure in its regular locus and injective analytic extension.
The inverse function theorem gives such a neighborhood at every regular
point; a sufficiently small rational ball containing the point has closure
inside it. Hence the eligible balls cover, without asserting an effective
algorithm for their injectivity predicate.
Intersect these balls with the owner's actual source-label sets and subtract
earlier pieces. Unique actual labels give a countable disjoint Borel source
partition. For Q only its single map \(F_0\) is used in this step.

On an eligible ball the fixed-label map is an analytic diffeomorphism onto
an open image. Its restricted source piece \(E_\alpha\) therefore has Borel
image \(B_\alpha\) and actual inverse \(\theta_\alpha\) from that analytic
inverse. Equations (4)–(5) and this atlas produce identical predecessor sets.
Every actual inverse fibre is at most countable, since each source piece
is injective and the partition countable; no finite inverse cutoff is used.

Smooth change of variables on the ambient ball, restricted to any Borel
\(E\subseteq B_\alpha\), proves
\[
\mu(\theta_\alpha E)=\int_E J_\alpha(w)\,d\mu(w),\qquad
J_\alpha(w)=\frac1{|\Delta_O(\theta_\alpha w)|}.        \tag{6}
\]
Here \(\Delta_O\) is the actual \(\Delta_q\) for M/G and \(\Delta_0\) for Q.
The displayed value is finite and positive at every actual inverse point;
extended integrals handle sets of infinite measure.
Overlapping inverse germs through the same actual source agree locally by
uniqueness, and thus have identical pointwise derivatives.
At an assigned floor face the frozen label's analytic germ gives the value.
This is not a claim that an a.e. density alone determines a null-point clock,
nor that the actual map is globally continuous across its cuts.

Consequently each legal step has the owned clock
\[
\kappa_O(z)=-\log J_{\alpha(z)}(T_Oz)=\log|\Delta_O(z)|. \tag{7}
\]
All signs and legal zero clocks remain. Terminals have no assigned next-step
clock, and no different measure or positive roof has been introduced.

## 3. Complete retained-lag histories, kernels and height action

Fix one owner \(O\) at a time and abbreviate its map to \(T\).
Let \(D_r\) be the Borel domain of \(r\) legal steps, \(D_0=X\), and define
\[
S_0=0,\quad S_r(z)=\sum_{j=0}^{r-1}\kappa_O(T^jz),\qquad
M_r(z)=e^{S_r(z)}
=\prod_{j=0}^{r-1}|\Delta_O(T^jz)|,\quad M_0=1.        \tag{8}
\]
Nonempty sums and products are used only on their actual domains.
Keep all actual triples
\[
\mathcal G_O=\{(z,r-s,w):z\in D_r,\ w\in D_s,\ T^rz=T^sw\},
\quad r,s\ge0.
\]
Source is \(w\), range \(z\); equal triples are identified with lag retained.
For each lag the relation is a countable union of Borel equality sets.
Multiplication adds lags, inversion swaps the endpoints and negates the lag.
The common-iterate property makes these operations well-defined.

The full clock is
\[
c_O(z,r-s,w)=S_r(z)-S_s(w)
           =\log\frac{M_r(z)}{M_s(w)}.                 \tag{9}
\]
Two representations of one triple differ by a common number of iterations
after their common endpoint, and the additional sums cancel.
For composition align the two middle histories to the longer middle length,
which is legal by hypothesis; cancellation of that middle sum proves
additivity. In particular the actual forward arrow \((Tz,-1,z)\) has
clock \(-\kappa_O(z)\), and inverse arrows have opposite clocks.

Refinement of finite histories into the countable atlas gives actual
injective arrow pieces \(w\mapsto (T^r)^{-1}(T^sw)=z\).
Chain rule on their smooth extensions gives full area modulus
\(M_s(w)/M_r(z)=e^{-c_O(z,r-s,w)}\).
Change of variables restricted to the actual Borel pieces proves their
every-Borel IMAGE formulas. Thus the cocycle belongs to the actual
transport, not to an independently chosen word clock.
The complete kernels are
\[
\begin{split}
K_{\rm lag}&=\{(z,0,w)\in\mathcal G_O\},\\
K_c&=\{(z,r-s,w)\in\mathcal G_O:M_r(z)=M_s(w)\},\\
K_{\rm joint}&=K_{\rm lag}\cap K_c.
\end{split}                                           \tag{10}
\]
All witnesses and all retained objects are included; no kernel is presumed
to contain only units.

An arrow \(g:w\to z\) acts on the whole \(X\times\mathbb R\) by
\((w,h)\mapsto(z,h+c_O(g))\).
Height translations act on the complete orbit SET, without a regular
topological quotient or global measurable selector assumption.
For a reference object \(b\) in one source orbit put
\(H_b=c_O(\operatorname{Iso}_{\mathcal G_O}(b))\).
An actual arrow \(g_z:z\to b\) supplies the complete extension-orbit phase
\[
h+c_O(g_z)\pmod{H_b}.                                 \tag{11}
\]
Changing the arrow changes this expression by an isotropy clock; conversely
an equality modulo \(H_b\) supplies the required isotropy arrow.

A deterministic partial map has nonzero source isotropy precisely when its
forward orbit is eventually periodic: unequal legal iterates that coincide
give a periodic tail, and a periodic tail supplies such coincidences.
If its least period is \(p\) and its signed least-cycle clock is \(C_\gamma\),
then the entire groups are
\[
\operatorname{Iso}_{\mathcal G_O}(z)=p\mathbb Z,\qquad
c_O(kp)=kC_\gamma,\qquad H_z=C_\gamma\mathbb Z.          \tag{12}
\]
Incoming-path sums cancel, and no inverse-word multiplicity is added to
actual retained triples. Extension isotropy is all \(p\mathbb Z\) when
\(C_\gamma=0\), and trivial otherwise.
Non-eventually-periodic and terminal-ending source orbits have trivial
source/extension isotropy and \(H_z=\{0\}\); their inter-object clocks need
not vanish. A nonzero \(C_\gamma\) gives one height circle over the source
orbit with primitive \(|C_\gamma|\) and all positive integer repetitions.
A zero \(C_\gamma\) retains zero-clock source isotropy but gives a height
line, not a positive closed orbit. Equal lengths do not merge distinct
source orbits. These are structural formulas, not a higher-period census.

For every target \(Y\), the recursion
\(\mathcal P_O^0(Y)=\{Y\}\),
\(\mathcal P_O^{j+1}(Y)=\bigcup_{Z\in\mathcal P_O^j(Y)}\mathcal P_O(Z)\)
enumerates exactly all actual finite incoming depths by induction.
Infinite incoming histories are all compatible chains of this same
predecessor relation, with no added history objects or free arrows.
This prescription applies to every null, cut or terminal target as well.

## 4. Complete fixed-point classification in the frozen square

In \(W=[-2,2]^2\), both floors lie in \(\{-2,-1,0,1,2\}\).
Every MAIN-admitted quotient and every G quotient therefore lies in
\(\{-2,-1,0,1,2\}\), including all boundary cases.
For fixed \(q\), addition and subtraction of \(F_q(x,y)=(x,y)\) give the
equivalent equations
\[
(x+y)\bigl(x^2+y^2+(q-1)xy\bigr)=0,
\quad
(x-y)\bigl(x^2+y^2+(1-q)xy-2\bigr)=0.                 \tag{13}
\]
The origin is a formal solution for every label.
On \(x=y=t\), nonzero solutions require \(q=-1\) and then every \(t\) works.
On \(x=-y=t\), nonzero solutions require \((q+1)t^2=2\).
If both \(x+y\) and \(x-y\) are nonzero, their remaining factors imply
\[
x^2+y^2=1,\qquad xy=\frac1{1-q}.
\]
Among the five possible labels only \(q=-2\) yields such genuinely
off-diagonal solutions; \(q=-1\) collapses back to the diagonal.
Indeed \(|xy|\le(x^2+y^2)/2\) rules out the others, including the
inconsistent \(q=1\) equations.

Put
\[
a=\frac{\sqrt5+1}{2\sqrt3},\quad
b=\frac{\sqrt5-1}{2\sqrt3},\quad
\alpha=\sqrt{2/3}.
\]
Then \(0<b<a<1\) and \(0<\alpha<1\).
For example \((\sqrt5+1)^2=6+2\sqrt5<12\) proves \(a<1\).
The entire nonzero formal fixed list in \(W\) is:

| Fixed label | All nonzero formal solutions in \(W\) |
| --- | --- |
| \(-2\) | \((a,b),(b,a),(-a,-b),(-b,-a)\) |
| \(-1\) | \((t,t)\), \(0<\lvert t\rvert\le2\) |
| \(0\) | \((\sqrt2,-\sqrt2),(-\sqrt2,\sqrt2)\) |
| \(1\) | \((1,-1),(-1,1)\) |
| \(2\) | \((\alpha,-\alpha),(-\alpha,\alpha)\) |

Their actual source checks eliminate every nonzero MAIN/G candidate:

| Formal family | Actual floors or quotient | Reason for rejection |
| --- | --- | --- |
| Positive \(q=-2\) pair | \((m,n)=(0,0)\) | MAIN illegal; G assigns \(0\) |
| Negative \(q=-2\) pair | \((m,n)=(-1,-1)\) | Both assign \(1\) |
| \(q=-1\) diagonal | \(m=n\) | MAIN illegal when \(m=0\), otherwise \(q=1\); G gives \(0\) or \(1\) |
| \((\sqrt2,-\sqrt2)\) for \(q=0\) | \((1,-2)\) | Both assign \(-2\) |
| \((-\sqrt2,\sqrt2)\) for \(q=0\) | \((-2,1)\) | MAIN fails divisibility; G assigns \(-1\) |
| \(q=1\) antidiagonal | \((1,-1)\) or \((-1,1)\) | Both assign \(-1\) |
| \((\alpha,-\alpha)\) for \(q=2\) | \((0,-1)\) | MAIN illegal; G assigns \(0\) |
| \((-\alpha,\alpha)\) for \(q=2\) | \((-1,0)\) | Both assign \(0\) |

At \(o=(0,0)\), MAIN is illegal, while G assigns \(q_G=0\) and has
\(\Delta_0(o)=-1\), hence an actual fixed point with clock zero.
Every other formal candidate already failed its own source label, so
there is no unresolved guard exception among actual candidates.
We have proved
\[
\operatorname{Fix}(T_M)\cap W=\varnothing,\qquad
\operatorname{Fix}(T_G)\cap W=\{o\}.                   \tag{14}
\]

Q uses \(F_0\) alone. Its formal fixed candidates are \(o\) and the two
\(\sqrt2\)-antidiagonal points from (13), regardless of unused arithmetic
quotients. The origin fails \(m\ne0\), and the negative-first point has
\((-2,1)\), which fails divisibility. The positive-first point
\[
R=(\sqrt2,-\sqrt2)
\]
has floors \((1,-2)\), is arithmetically admitted, and has its own
\[
DF_0(R)=\begin{pmatrix}6&1\\1&6\end{pmatrix},
\qquad \Delta_0(R)=35.
\]
Thus
\(\operatorname{Fix}(T_Q)\cap W=\{R\}\), with own clock \(\log35\).
The unused arithmetic quotient \(-2\) does not replace Q's \(DF_0\).
This completes exactly the fixed window, not a global MAIN/G census.

## 5. The prelisted word and its own-control checks

At both \(P=(1,-1)\) and \(Q_0=(-1,1)\), MAIN permission holds and its
actual quotient is \(-1\). G independently assigns the same quotient.
Exact substitution gives
\[
F_{-1}(P)=Q_0,\qquad F_{-1}(Q_0)=P,\qquad
DF_{-1}(P)=DF_{-1}(Q_0)=\begin{pmatrix}2&3\\3&2\end{pmatrix}.
\]
Thus both steps are legal for M and G, with determinant \(-5\),
inverse IMAGE density \(1/5\) and own clock
\[
\lambda=\log5.
\]
Since \(P\ne Q_0\), the least source period is two; these are not fixed
points omitted from §4. Their signed least-cycle clock is
\[
C_\Gamma=2\lambda=\log25,\qquad \Gamma=\{P,Q_0\}.      \tag{15}
\]
Assigned integer faces use exactly these fixed-label analytic values.

For Q, its own map instead gives
\[
F_0(P)=F_0(Q_0)=o,\qquad \Delta_0(P)=\Delta_0(Q_0)=8.
\]
Both source points satisfy Q arithmetic permission and its own regularity,
but \(o\) is a Q terminal because its first floor is zero.
Therefore the prelisted two-step word does not exist in Q.
Its legal incoming steps to that terminal have clock \(\log8\); they are
not a closed packet and cannot inherit MAIN's word or its derivative.
All these points and incoming arrows remain in their respective owners.

## 6. Entire incoming basins, kernels, and phase conventions

For each tested fixed core \(F\) in its own owner, set
\[
\mathcal B_0=\{F\},\qquad
\mathcal B_{j+1}=\bigcup_{Y\in\mathcal B_j}\mathcal P_O(Y),\qquad
\mathcal B=\bigcup_{j\ge0}\mathcal B_j.                \tag{16}
\]
For a tested cycle use \(\mathcal B_0=\Gamma\) in the same recursion.
Induction proves these are exactly the points reaching the specified core
set after the stated number of legal steps. The sets are nested because
the core sets map onto themselves. All are at most countable, by the complete
inverse atlas. Every equation (4)–(5), actual label, real root and depth is
included, without restricting incoming points to \(W\).
These are exact basin characterizations, not finite basin enumerations.
Each such basin is the full source orbit of its fixed core or cycle.

For a fixed core with signed clock \(C\), let \(a(z)\) be the first entry
time and \(\beta(z)=S_{a(z)}(z)-a(z)C\).
Every integer lag occurs between any two basin points, by advancing beyond
their entry times. The entire basin cocycle is
\[
c(z,k,w)=\beta(z)-\beta(w)+kC.                         \tag{17}
\]
Hence its lag kernel has exactly \(k=0\), its clock kernel imposes the
displayed expression equal to zero, and the joint kernel imposes both.
Source isotropy at every basin point is \(\mathbb Z\), with entire
clock image \(C\mathbb Z\). The phase at the reference fixed core is
\[
h-S_{a(z)}(z)\pmod{C\mathbb Z}
=h-\beta(z)\pmod{C\mathbb Z}.                         \tag{18}
\]
The transporting forward arrow has lag \(-a(z)\) and clock \(-S_{a(z)}(z)\).

For G's core \(o\), \(C=0\): its full source isotropy remains \(\mathbb Z\),
extension isotropy also remains \(\mathbb Z\), and \(H_o=\{0\}\).
Every real phase in (18) is retained, with free height translation and no
positive primitive. This zero-clock fixed point is not a nonempty positive
ledger. For Q's core \(R\), \(C=\log35\), entire \(H_R=(\log35)\mathbb Z\),
extension isotropy is trivial, and the primitive is \(\log35\), with every
positive integer repetition. Both use their own unrestricted basins (16).

Now fix either M or G's actual two-cycle basin and choose reference \(P\).
Let \(t(z)\) be the first time \(T^{t(z)}z=P\); it exists for every point
reaching \(\Gamma\), since \(Q_0\) next maps to \(P\).
Put
\[
\beta_\Gamma(z)=S_{t(z)}(z)-t(z)\lambda .
\]
Every later visit to \(P\) is an even number of steps later and yields the
same value. Once at the core, each further step has clock \(\lambda\).
Two basin histories can meet exactly when their core phases match, so the
complete set of available arrows and their clocks is
\[
k\equiv t(z)-t(w)\pmod2,\qquad
c(z,k,w)=\beta_\Gamma(z)-\beta_\Gamma(w)+k\lambda.      \tag{19}
\]
Necessity follows by advancing any common endpoint into the cycle.
Conversely, for any lag satisfying the congruence, take both histories
sufficiently long beyond their first visits to \(P\); their parity makes
the endpoints equal. This proves all arrows, not only the displayed word.

On this basin the lag kernel consists exactly of \(k=0\) arrows between
points with equal \(t\)-parity. The clock kernel imposes the zero-clock
equation in (19) together with its lag congruence; the joint kernel imposes
both this equation and \(k=0\). At each object the entire isotropy is
\[
2\mathbb Z,\qquad
c(2j)=2j\lambda,\qquad
H=(2\lambda)\mathbb Z=(\log25)\mathbb Z.               \tag{20}
\]
Its extension isotropy is trivial. No additional root or entry path adds
an odd isotropy lag to this deterministic least-period-two core.
The complete phase at reference \(P\) is
\[
h-S_{t(z)}(z)\pmod{(\log25)\mathbb Z}
=h-\beta_\Gamma(z)-t(z)\lambda
   \pmod{(\log25)\mathbb Z}.                          \tag{21}
\]
The parity-dependent last term must not be silently dropped.
Changing reference to \(Q_0\) shifts the phase origin, not the period group.
All phases form one height circle over this full source orbit; cyclic
rotations of the core are not separate packets.

Consequently the primitive height time is exactly \(\log25\), and the
positive repetition list is \(j\log25,\ j=1,2,\ldots\).
A one-step arrow with clock magnitude \(\log5\) connects different core
objects; it is not isotropy at either one. It cannot be used to halve the
primitive in (20). M and G have their own complete basins and packets;
their shared core formulas do not identify their global histories.

Q's two prelisted incoming points instead belong to the terminal-ending
source orbit of \(o\). By §3 it has trivial isotropy and \(H=\{0\}\),
with all other incoming depths still given by (4)–(5); its inter-object
clock need not be zero. It supplies no positive period.

## 7. Scoped decision and evidence limits

MAIN's fully owned primitive is \(\log25\). If it were \(\log p\) for an
ordinary prime, injectivity of the real logarithm would force \(p=25\),
which is composite. Thus MAIN fails the necessary prime-packet target.
Its empty fixed window did not decide the target; the independently
precommitted actual two-step test did. Q's \(\log35\) and G's zero-clock
fixed core are separately owned controls, not substitutes for this proof.

| Obligation | Same-object evidence | Status |
| --- | --- | --- |
| Divisor-symbolic source | Integer seed and full guard (3) | Established; strong naturalness OPEN |
| Full area/IMAGE owner | All roots, atlas and analytic cut values (2)–(7) | Established |
| Whole histories | (8)–(12), full kernels/isotropy and all incoming | Established structural ledger |
| Complete fixed window | MAIN empty; G only \(o\); Q only \(R\) | Complete in \(W\), not global MAIN/G |
| Listed word | M/G actual least period two; Q terminates at \(o\) | Exact own-control comparison |
| Entire MAIN packet | (19)–(21), primitive \(\log25\) | Adverse composite; STOP / FORK |
| Other returns/coverage | No higher-period or outside-window census | OPEN; no further search here |
| Classical / formal Routes | No symplectic suspension, operator or formal evaluation | N/A; T3 NOT AUDITED; UNASSIGNED; B NOT INVOKED |

The same-object ledger stayed intact. G's same two-cycle is a PROVES_TOO_MUCH
warning, not a theorem of global equivalence. Prime uniqueness/coverage,
canonical formula choice and a positive classical roof are not established.
No label, root, incoming history, null point or zero-clock isotropy was
deleted to improve the target. The candidate stops without coefficient,
readout, measure or time normalization repair.

## 8. Provenance, assistance and reproducibility

The author read the original card's complete 1–92 through EOF and used the
previously read local paper template. Informal substitution motivated the
prelisted word before freeze; that design exposure is in the card and is
not presented as a sealed prediction. No old result was imported.
Current CP1, raw review, final review and sibling scientific outputs were
not author inputs. Root owns the card, outcome append and review integration.

The only pre-freeze scientific collision prefixes were the 426 card 1–48
and 342 card 1–59, both non-EOF, with hashes recorded in the governing card.
Heading metadata exposed their outcome titles at 426:101 and 342:195, not
their appended bodies. No full-card hashes or totals were claimed.
Shared prior participation and historical exposure remain; the bounded
comparisons give no global novelty or nonconjugacy claim.

Same-author helper /root/arithmetic_feedback_scout/dss_g_fixed_author read only
this original card 1–92 through EOF and independently measured the same
prefix hash, for exact fixed-window and source-guard checks.
It performed no listed-word analysis and wrote no manuscript file; it was
not an independent reviewer. The author owns the integrated proof.
AI agents supplied mathematical derivation, drafting and internal checking;
no human or external verification is certified. Same-model/shared-history
execution is NOT_CALIBRATED, not cross-model validation.
ARS supplied bounded card-first and evidence-isolation discipline, not
mathematical certification or publication authority.

The scientific method was exact polynomial differentiation/factorization,
integer-floor case analysis, analytic local inversion/change of variables
and deterministic history identities. No scientific program, numerical
census, network, Git operation, PDF, operator or external publication was used.
Mechanical UTF-8, link, identity and hash checks verify artifacts only.
The [claim ledger](claim-ledger.md) and [package overview](README.md) carry
the identical outcome and its limits.
