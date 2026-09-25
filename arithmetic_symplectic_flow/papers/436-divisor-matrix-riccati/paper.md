# A nonprime fixed return in divisor-matrix Riccati transport

Candidate ID: ANG-20260923-DMR01.
Outcome: OWNED RICCATI IMAGE CLOCK; NONPRIME FIXED RETURN — STOP / FORK
Date: 2026-09-23. Batch NONHOMOGENEOUS-FEEDBACK-20260923-R, round 436.
Type: ANG partial Borel transport with its retained-lag IMAGE extension.
Classical fields NOT APPLICABLE; T3 NOT AUDITED; formal Route UNASSIGNED.
Route B NOT INVOKED. Strong naturalness remains OPEN.

## Abstract

We study the frozen full four-entry real matrix map with current-entry
divisibility, a nonlinear inverse-matrix term and a fixed displacement.
We prove its complete countable actual inverse atlas, its prescribed
every-point/every-Borel IMAGE law and the complete history convention.
MAIN and its permission-off control each have exactly one fixed point,
\(A_*=\left(\begin{smallmatrix}0&2\\4&0\end{smallmatrix}\right)\).
The full four-dimensional forward determinant there is \(49/64\).
Consequently the entire return subgroup is \(\log(49/64)\mathbb Z\);
its least positive generator is \(\log(64/49)\), not an ordinary-prime log.
The drift-off control instead has an explicitly classified continuum of
zero-clock fixed cores. Unrestricted inverse recursion retains every incoming
point and phase, including terminal targets, and gives the whole fixed-core
packets. The MAIN obstruction is decisive without any higher-period census.

## 1. Frozen object, lineage and separate controls

The input is the original 104-line [candidate card](candidate-card.md), SHA256
c289e5e336174545441971d2773d2612e95035be135f21fc129997781429daac.
Take \(X=M_2(\mathbb R)\), ordinary Borel structure, original-entry Lebesgue4,
\[
 C=\begin{pmatrix}1&0\\0&2\end{pmatrix},\quad
 J=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
 m=\lfloor A_{12}\rfloor,\quad n=\lfloor A_{21}\rfloor.
\]
For a fixed integer \(q\), put
\[
 f_{q,\varepsilon}(A)=A+qA^{-1}C-\varepsilon J,\qquad
 {\cal L}_{q,A}(H)=H-qA^{-1}HA^{-1}C,\quad
 \Delta(q,A)=\det_{\mathbb R^4}{\cal L}_{q,A}.                \tag{1}
\]
Only invertible \(A\) is used in (1). Define the open geometric set
\(R_q=\{A:\det A\ne0,\Delta(q,A)\ne0\}\).
The three owners use these separate laws and actual domains:

| Owner | Arithmetic reading and permission | Actual map and domain |
| --- | --- | --- |
| MAIN \(T\) | \(m\ne0,m\mid n,\ q=n/m\) | \(f_{q,1}\), with \(A\in R_q\) |
| \(G\), permission-off | \(q=\lfloor n/m\rfloor\) if \(m\ne0\), otherwise \(0\) | \(f_{q,1}\), with \(A\in R_q\); no divisibility gate |
| \(D\), drift-off | MAIN permission and quotient | \(f_{q,0}\), with \(A\in R_q\) |

Every other state remains a forward terminal, with identity and all incoming.
No singular matrix, critical source, sign, unit, zero quotient or assigned
floor boundary is discarded. No absorbing loop is added. A legal target may
be terminal; target-next-step regularity is never an inverse condition.
The full matrix space is not restricted to symmetric or diagonalizable matrices.

For integers \(N\ge2,1<d<N\), the declared interface
\(A_{N,d}=\left(\begin{smallmatrix}1&d\\N&Nd+1\end{smallmatrix}\right)\)
has determinant one and readings \(m=d,n=N\). Its arithmetic permission
is exactly \(d\mid N\); when permitted, full legality additionally requires
\(\Delta(N/d,A_{N,d})\ne0\).
We do not assert that the entire interface is legal or invariant.
For \(A=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) and
\(t=\det A\), the displaced off-diagonal outputs are
\(b(1-2q/t)-1\) and \(c(1-q/t)-1\).
Thus current arithmetic participates in actual transport, and actual geometry
determines the next arithmetic reading. This is a precise deformation of
proper-divisor symbolic permission, not an external prime label.
The universal matrices, readout and measure are design choices, not a proved
natural arithmetic construction. No prime table, selected roof or zero data enters.

## 2. Complete inverse atlas and full-dimensional IMAGE

Write \(\varepsilon_T=\varepsilon_G=1,\varepsilon_D=0\).
For target \(B\) and a candidate integer \(q\), the inverse equation is
\[
             A^2-A(B+\varepsilon_OJ)+qC=0.                 \tag{2}
\]
For MAIN and \(D\), enumerate every integer pair \(m\ne0,n\) with \(m\mid n\);
for \(G\), enumerate every pair \(m,n\in\mathbb Z\).
Use each owner's own quotient rule, and take ALL real matrix solutions of (2).
Keep exactly those in \(R_q\) whose actual floors, own permission and own quotient
agree with the label. Multiplying the forward equation on the left by \(A\)
gives (2); conversely invertibility allows multiplication by \(A^{-1}\) to
recover the exact forward equation. This proves both directions of the recipe.
There are no omitted spectral, nonsymmetric or nonpositive roots.
The actual floors fix an actual predecessor's labels, so repeated descriptions
are identified without deleting distinct predecessors.

Differentiating \(AA^{-1}=I\) gives \(D(A^{-1})[H]=-A^{-1}HA^{-1}\).
For each fixed integer branch the actual derivative is therefore exactly
\({\cal L}_{q,A}\) from (1), for each owner's own displacement.
It is invertible precisely on \(R_q\).
By the real-analytic inverse function theorem, every point of \(R_q\) has
a neighborhood on which its fixed-\(q\) map is analytically invertible.
Inside that neighborhood choose a rational ball containing the point whose
closure still lies inside it. Thus the card's eligible rational balls cover \(R_q\).

For each owner and \(q\), keep the once-enumerated eligible balls, intersect them
with its actual arithmetic \(q\)-source, and remove earlier source pieces.
Different actual \(q\)-sources are disjoint; this is a countable Borel partition
of the entire legal domain. On a ball \(U\), the fixed-\(q\) map is an analytic
diffeomorphism onto its open image. Hence the actual target of a Borel source
piece is Borel, and its inverse is the restriction of that analytic inverse.
Every source point, including a legal floor face, lies in one of these pieces.
Every actual predecessor is obtained by this atlas and the complete equation (2).
There are at most countably many actual predecessors, because every injective
source piece contributes at most one to a fixed target. We do not assert finiteness.

With column-stacked matrix coordinates, the full determinant has the exact form
\[
 \Delta(q,A)=\det\!\left(I_4-q\big((A^{-1}C)^{\mathsf T}\otimes A^{-1}\big)\right).
                                                               \tag{3}
\]
Changing between this ordering and the original four entries is just a
coordinate permutation. No eigenbasis, commuting slice or selected direction
is substituted for the full determinant.
At an actual inverse \(\theta\), with \(A=\theta(B)\), differentiation of the
inverse identity and change of variables give, respectively,
\[
 J_\theta(B)=|\det D\theta(B)|=\frac1{|\Delta(q,A)|},\qquad
 \mu(\theta E)=\int_E J_\theta(B)\,d\mu(B)                    \tag{4}
\]
for EVERY Borel subset \(E\) of its actual target domain.
These values are positive and finite by the declared source regularity.
At a floor cut the analytic germ on its covering ball provides the same formula.
Two overlapping germs returning the same actual source have derivative
\({\cal L}_{q,A}^{-1}\); the actual quotient is fixed by that source.
Thus their density agrees at every point, independent of the ball enumeration.
This is the prescribed germ version, not a measure-theoretic uniqueness claim
for arbitrary values on null sets.

Each owner separately has its signed step clock
\[
                    \kappa_O(A)=\log|\Delta(q_O(A),A)|.     \tag{5}
\]
No next-step clock is assigned at a terminal. A terminal's identity is still
present. Different inverse branches of one target need not have the same
density; (4) always uses the branch returning the specified source.
Unions of overlapping images are not summed as if disjoint.

## 3. Entire fixed sets and their actual clocks

For either displaced owner, fixedness requires \(qA^{-1}C=J\).
Since \(J\ne0\), \(q\ne0\); multiplying on the left by \(A\) and on the right
by \(J\) gives
\[
               A=qCJ=\begin{pmatrix}0&q\\2q&0\end{pmatrix}. \tag{6}
\]
Here the readings are exactly \(m=q,n=2q\). MAIN's actual quotient is \(2\),
and \(G\)'s actual floor quotient is also \(2\). In either case self-consistency
forces \(q=2\). Conversely \(A_*=2CJ\) has these readings, determinant \(-8\),
and satisfies \(f_{2,1}(A_*)=A_*\). It remains to check full regularity.

At this actual point, \(A_*^{-1}=\left(\begin{smallmatrix}0&1/4\\1/2&0\end{smallmatrix}\right)\)
and \(qA_*^{-1}C=J\). Hence
\({\cal L}_{2,A_*}(H)=H-A_*^{-1}HJ\).
In the coordinate pairs \((h_{11},h_{22})\) and \((h_{12},h_{21})\),
each of its two blocks is
\[
 \begin{pmatrix}1&-1/4\\-1/2&1\end{pmatrix},\qquad
 \Delta(2,A_*)=(7/8)^2=49/64\ne0.                          \tag{7}
\]
This uses all four real directions. Thus each displaced owner has ENTIRE
fixed set \(\{A_*\}\), actual inverse density \(64/49\) at that fixed branch,
and fixed clock \(C_*=\log(49/64)<0\). MAIN and \(G\) are distinct owners;
their common fixed matrix does not identify their incoming packets.

For \(D\), fixedness instead requires \(qA^{-1}C=0\), hence exactly \(q=0\).
Its permission then gives \(n=0,m\ne0\). Conversely those conditions and
invertibility give \({\cal L}_{0,A}=I_4\) and a legal fixed point. Its ENTIRE
fixed set is consequently
\[
 {\cal F}_D=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}:
       ad-bc\ne0,\ (b<0\text{ or }b\ge1),\ 0\le c<1\right\}. \tag{8}
\]
All endpoints are as written; arbitrary \(a,d\), negative \(b\), and \(c=0\)
remain subject only to invertibility. Every such core has \(J_\theta(Y)=1,\kappa_D=0\).
This does not assert zero clock on other legal \(D\) sources or exclude
higher-period \(D\) cores.

## 4. Full histories, kernels and unrestricted incoming

For each actual owner \(F\), let \(D_F^{(r)}\) mean that \(r\) steps are legal,
with \(D_F^{(0)}=X\). Define
\[
 M_r(A)=\prod_{j=0}^{r-1}|\Delta(q_F(F^jA),F^jA)|,\quad
 M_0=1,\quad S_r=\log M_r,
\quad {\cal G}_F=\{(A,r-s,B):F^rA=F^sB\text{ legally}\}.     \tag{9}
\]
All these domains and equalities are Borel. Equal triples are identified,
but integer lag is retained; source is \(B\), range is \(A\).
Composition aligns two equalities at the larger time on their common middle
trajectory. Every needed advance is already a legal part of that trajectory;
no continuation past a terminal is invented.
For the same triple, two pairs of witnesses differ by a common time advance.
Their two clock sums acquire the identical tail sum at their common endpoint,
which cancels. The same alignment proves additivity. Thus the full cocycle is
\[
 c_F(A,r-s,B)=S_r(A)-S_s(B)=\log\frac{M_r(A)}{M_s(B)}.        \tag{10}
\]
Inversion negates it. The forward arrow \((FA,-1,A)\) has clock \(-\kappa_F(A)\).
On every finite actual history chart, composition of (4) gives IMAGE density
\(M_s(B)/M_r(A)=e^{-c_F}\) in this source-to-range direction, including every
assigned cut. These countably many charts cover all arrows, not just loops.

The exact full lag kernel has \(r=s\) in (9); the exact clock kernel has
\(M_r(A)=M_s(B)\); their intersection has both conditions.
These describe all kernels, not just their isotropy and not just unit arrows.
Let \(P^F_1(B)\) be every actual predecessor from (2) and its own checks.
Set \(P^F_0(B)=\{B\}\) and
\[
       P^F_{j+1}(B)=\bigcup_{Y\in P^F_j(B)}P^F_1(Y).         \tag{11}
\]
Splitting the first step proves inductively
\(P^F_j(B)=\{A:F^jA=B\text{ through }j\text{ legal steps}\}\).
There is no integer, root or depth cutoff, even if \(B\) is terminal.
For any range \(A\), all arrows are obtained by taking legal \(F^rA\),
any \(s\ge0\), and every \(B\in P^F_s(F^rA)\), with retained lag \(r-s\).
This gives every source orbit and every finite history; all compatible
infinite inverse histories remain. Different written witnesses of the same
triple are not extra arrows or extra packet labels.

If \(A\) is eventually on a least \(p\)-cycle, any isotropy equality can be
advanced to that cycle, so its lag is divisible by \(p\). Conversely all such
multiples occur by comparing late iterates. Its source isotropy is \(p\mathbb Z\).
Writing \(C_\gamma\) for the actual clock sum once around that cycle,
its ENTIRE clock image is \(H_A=C_\gamma\mathbb Z\); the preperiod cancels.
If \(A\) is not eventually periodic, its source isotropy and \(H_A\) are trivial:
a repeated legal iterate would itself force an indefinitely repeating cycle.
This includes terminals and eventually terminating points, without classifying
the existence of any higher cycle in the present maps.

On the complete extension \((B,h)\mapsto(A,h+c_F)\), isotropy is precisely
the zero-clock part of source isotropy: \(kp\) survives iff \(kC_\gamma=0\).
All real heights remain. Source orbits have physical phases \(\mathbb R/H_A\)
and height translation on the orbit SET, with return group exactly \(H_A\).
For an actual arrow \(g_A:A\to b\), the transported phase is
\(h+c_F(g_A)\bmod H_b\); two choices differ by a full isotropy value.
No topological or regular measurable quotient is assumed.

## 5. Complete fixed-core packets and decisive MAIN failure

For every fixed core \(Y\) in Section 3 its FULL source packet is exactly
\({\cal B}_Y=\bigcup_{j\ge0}P^F_j(Y)\): tail equality with the fixed point
is equivalent to actual eventual entry. Distinct fixed points have disjoint
basins by determinism. Equation (11), with the complete polynomial roots
and regularity checks, is an exact unrestricted incoming description, not
a finite census or a claim that only the fixed point belongs to its basin.
For MAIN/\(G\), substitute \(B=Y=A_*\) in (2); for \(D\), use every \(Y\)
in (8). All subsequent inverse depths again use the owner's full (2).
Neither the fixed-point ansatz (6) nor \(q=0\) from (8) is imposed on incoming
sources: their own arbitrary quotients and all regular roots remain in (11).

Let \(d(A)\) be the first entry time of \(A\in{\cal B}_Y\), let
\(C_Y=\kappa_F(Y)\), and put \(\beta(A)=S_{d(A)}(A)-d(A)C_Y\).
For \(r\ge d(A)\), \(S_r(A)=\beta(A)+rC_Y\). All pairs of basin points admit
every integer lag by choosing sufficiently late iterates at \(Y\).
Thus on this WHOLE fixed basin,
\[
 c_F(A,k,B)=\beta(A)-\beta(B)+kC_Y,\qquad
 {\cal G}_{F,A}^{A}\simeq\mathbb Z,\quad H_A=C_Y\mathbb Z.    \tag{12}
\]
The basin lag kernel is \(k=0\); its clock kernel is
\(\beta(A)-\beta(B)+kC_Y=0\); the joint kernel is \(k=0,\beta(A)=\beta(B)\).
Extension isotropy is the subgroup of integers with \(kC_Y=0\).
An incoming height has phase
\(h-S_{d(A)}(A)\bmod C_Y\mathbb Z\), equivalently \(h-\beta(A)\) modulo that
same ENTIRE group. These are all phases, not selected centres or branches.

For MAIN and \(G\), (7) gives \(C_Y=C_*<0\), so the full extension isotropy
is trivial, phases are \(\mathbb R/\log(64/49)\mathbb Z\), and the positive
primitive is
\[
                 L_*=-C_*=\log(64/49)>0.                   \tag{13}
\]
The entire source isotropy is \(\mathbb Z\), whose image is exactly
\(C_*\mathbb Z\); no unseen incoming path can reduce this generator.
Every repetition and both orientations are included. Since \(64/49\) is
strictly between \(1\) and \(2\), it is not an ordinary integer prime.
MAIN therefore has a nonempty positive ledger containing a forbidden
primitive. Selecting one block of (7), taking half the clock, or replacing
the density with another directional quantity would change the owner.

For each \(D\) core in (8), \(C_Y=0\): source and extension isotropy are
\(\mathbb Z\), the entire \(H\) is zero, phases are \(\mathbb R\), and that
fixed packet has no positive primitive. Incoming clocks need not be zero;
their exact values and kernels remain in (10)–(12).
No merging of different \(D\) cores or deletion of zero-clock isotropy occurs.
All higher-period orbits, additional positive packets and all-prime coverage
outside the fixed window remain UNCLASSIFIED; they cannot remove (13).

## 6. Gates, methods and limits

T0 inverse/Borel/IMAGE/history ownership is established on the frozen full
carrier. The proper-divisor reading is exact, but strong naturalness remains
OPEN and arithmetic T1 is NOT PASSED. T2's complete packet convention
exhibits a MAIN violation of prime purity, so the decision is STOP / FORK.
The permission-off fixed obstruction shows that this local return is not a
certificate of prime-selective arithmetic. Drift-off has its own different
fixed ledger, not a rescue clock. This is the relevant PROVES_TOO_MUCH warning.
Classical fields NOT APPLICABLE, T3 NOT AUDITED, formal Route UNASSIGNED,
Route B NOT INVOKED. No universal no-go for all matrix/Riccati sources is claimed.

Method: exact matrix substitution, analytic inverse function/change-of-variables
arguments, a complete four-coordinate determinant at the fixed core, and
partial-map history algebra. No numerical experiment, higher-period table,
new literature claim, external data, operator, PDF or Git action was used.
The author fully read the frozen card before proof. An author-side helper
read only that original 104-line card to check the \(G,D\) fixed calculations
and immediate predecessor constraints; the author independently verified
the fixed results and integrated no independent-review evidence.
The general atlas, MAIN proof and whole-history derivation are author work.

Before freeze the no-displacement draft was explicitly changed to the present
MAIN, with the old draft retained as control \(D\). Informal fixed-equation
and derivative-factor algebra informed \(A_*\); this was not sealed or blind
discovery. Scout reads were 430 summary 1–110 EOF, 420 card 1–69 and 411 card
1–64 non-EOF; their exact prefix locks and outcome-heading exposure are in
the frozen card. Retained prior authorship of 411/431 and shared history
remain disclosed. No current raw, scope-review or peer science was read.
AI agents supplied mathematical derivation, drafting and internal checking;
same-model shared-history work is NOT_CALIBRATED. No human or external
verification or independent peer validation is certified.

The [claim ledger](claim-ledger.md) and [README](README.md) summarize this
proof; root owns the card's outcome append and separate review integration.
No formula, measure, terminal rule or clock was repaired after freeze.
