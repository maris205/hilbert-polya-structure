# 436 — card-only independent derivation

Candidate: ANG-20260923-DMR01. Date: 2026-09-23.
Batch NONHOMOGENEOUS-FEEDBACK-20260923-R; round2/5,435–439 only.
Root reported its complete 98-line CP1 read and distinctly released raw math.
Sole scientific input: original candidate-card.md lines 1–104, completely
reread after release; no later append or author surface was read.
candidate-card.md original prefix — 104 lines; SHA256 c289e5e336174545441971d2773d2612e95035be135f21fc129997781429daac
Frozen scope-review.md — 98 lines; SHA256 f3cca63fbea50ff93e3c94a6d28abe2f85c09a284131e994eb7b383dc26818b8
No author paper/README/ledger, helper, peer, sibling or old science was read.
The card disclosed informal design hand algebra and its predeclared A*;
this proof is card-only but not blind or independent of shared history.
ARS instructions retained from earlier complete reads govern this stage;
they are not claimed as freshly reread. AI supplied the derivation/checks.
Same-model internal NOT_CALIBRATED; no external, human or cross-model review.
No auxiliary agent, scientific code/numerics, literature, Git, publication
or two-step/higher-period census was used.

## 1. Whole owners, actual derivative and exact interface

Each owner separately retains \(X=M_2(\mathbb R)\), its Borel structure,
and \(\mu=\mathrm{Leb}_4\) on the four original entries. The fixed matrices are
\[
C=\begin{pmatrix}1&0\\0&2\end{pmatrix},\qquad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
For a fixed integer q and \(\det A\ne0\), write
\[
f_q(A)=A+qA^{-1}C-J,\qquad g_q(A)=A+qA^{-1}C.
\]
Differentiating \(A A^{-1}=I\) in direction H gives
\(D(A^{-1})[H]=-A^{-1}HA^{-1}\). Hence the ACTUAL derivatives of
both analytic formulas on the full four-entry space are
\[
Df_q(A)[H]=Dg_q(A)[H]=L_{q,A}(H)
=H-qA^{-1}HA^{-1}C.
\]
The disappearance of the constant drift in the derivative has been proved,
not used to borrow a control's domain or clock.
Put \(\delta_q(A)=\det_{\mathbb R^4}L_{q,A}\) and
\(R_q=\{A:\det A\ne0,\delta_q(A)\ne0\}\), an open set.

Throughout each owner's definitions, \(m=\lfloor A_{12}\rfloor\) and
\(n=\lfloor A_{21}\rfloor\). MAIN's actual legal q-source set is
\[
D_{{\rm M},q}=\{A\in R_q:m=\lfloor A_{12}\rfloor\ne0,\
                n=\lfloor A_{21}\rfloor,\ m\mid n,\ n/m=q\}.
\]
G has
\[
D_{G,q}=\{A\in R_q:q_G(m,n)=q\},\quad
q_G(m,n)=
\begin{cases}\lfloor n/m\rfloor&m\ne0,\\0&m=0.\end{cases}
\]
D has \(D_{D,q}=D_{{\rm M},q}\) as its own declared domain, but uses \(g_q\).
MAIN and G use \(f_q\). These Borel sets partition each owner's legal source
by its actual exponent; no formal branch with an incorrect q is admitted.
Their union is the actual legal domain. All remaining matrices stay terminal,
with \(T^0\), identities and every actual incoming arrow but no next step.
There is no absorbing loop or next-step clock assigned to a terminal.

At \(A_{Nd}\), \(\det A_{Nd}=Nd+1-dN=1\), \(m=d,n=N\).
Thus the arithmetic permission is exactly \(d\mid N\), with q=N/d when
permitted. Actual transport uses that quotient and recomputes the readouts
from its output, not an independent integer memory. The additional
\(\delta_q(A_{Nd})\ne0\) condition is not assumed universally.
This verifies the specified arithmetic interface, not a naturalness theorem,
invariant interface, prime classifier or conservative/symplectic lift.

## 2. ALL real inverse solutions and the complete countable atlas

For MAIN/G the fixed-q equation \(f_q(A)=B\), with \(\det A\ne0\), is
equivalent to
\[
A^2-A(B+J)+qC=0 .
\]
Indeed multiply the forward equation on the LEFT by A; conversely left
multiply this polynomial equation by \(A^{-1}\). No factors are commuted.
For D the corresponding equivalence is
\[
g_q(A)=B\quad\Longleftrightarrow\quad A^2-AB+qC=0 .
\]
For each owner enumerate ALL integer source labels permitted by its own
rule and ALL real matrix solutions of the corresponding equation.
Keeping exactly \(A\in D_{O,q}\) and its actual forward equality is
necessary and sufficient for being an actual predecessor.
No positivity, symmetry, spectrum or invertibility of target B is imposed.
The root equation before permission/regularity need not have finitely many
solutions; no such finite-root assertion is used here.

Here is the exact realization by the card's rational balls.
Fix any one countable enumeration of all open balls with rational centres
and positive rational radii in the four-entry space. For each owner and q,
retain precisely those balls V with \(\overline V\subset R_q\) on which
its own fixed-q formula \(F_{O,q}\) is injective; \(F_{O,q}\) is f_q or g_q.
Each point of \(R_q\) has an analytic inverse-function neighborhood,
since its derivative L is invertible. A smaller rational ball containing
that point, with closure inside that neighborhood, is retained.
Thus the retained balls cover \(R_q\), and in particular \(D_{O,q}\).
Their selection need not be an effective finite test for the exact
countable definition and coverage proof to hold.

Order the retained balls by the frozen enumeration, writing them \(V_j\),
and define actual source pieces
\[
S_{O,q,j}=(V_j\cap D_{O,q})\setminus
               \bigcup_{i<j}(V_i\cap D_{O,q}).
\]
They are Borel, disjoint and cover \(D_{O,q}\). The least containing index
exists for each legal point. Removing earlier pieces does not remove
any legal source from the atlas; other points remain objects of X.
Across q the actual source sets are already disjoint.

On \(V_j\), \(F_{O,q}\) is an injective analytic local diffeomorphism,
hence a diffeomorphism onto its OPEN image: local inverses cover and agree
by injectivity. Its inverse is analytic on that entire image.
The actual target set \(E_{O,q,j}=F_{O,q}(S_{O,q,j})\) is Borel, because
the open-set diffeomorphism and its inverse are continuous.
Restrict its analytic inverse to E; this is the card's actual inverse chart.

Every actual predecessor belongs to exactly one source piece and supplies
one such chart. Conversely every chart point is a legal source and maps
to its stated target. This proves BOTH inverse identities and completeness
of the all-real-root prescription on the entire X.
For a fixed target each injective chart supplies at most one predecessor;
the countable set of q,j therefore proves countability of actual inverses,
not their finiteness. Target-terminal and integer-face points are included.
Changing the once-fixed ball order only changes the partition descriptions,
not the set of actual sources, predecessors or retained triples.

## 3. Own four-dimensional IMAGE and pointwise clocks

At an actual inverse point \(A=\theta(B)\), the inverse derivative is
\[
D\theta(B)=L_{q,A}^{-1},\qquad
J_\theta(B)=\frac{1}{|\delta_q(A)|}>0 .
\]
It is finite at every admitted point by its OWN regularity.
Any two chart germs at the same actual source use its unique actual q
and the same derivative of the same fixed-q owner. They consequently
give the identical inverse derivative and J, including null floor faces.
There is no dependence of the actual point clock on chart order.
This applies separately to MAIN's q, G's q_G and D's g_q inverse.

For every Borel subset E of any actual target piece, change of variables
on the full open chart, restricted to E, gives
\[
\mu(\theta(E))=\int_E|\det D\theta(B)|\,d\mu(B)
              =\int_EJ_\theta(B)\,d\mu(B).
\]
Unbounded sets are covered by countable restrictions and nonnegative
integrals. Null sets and assigned integer cuts are not exceptions.
The analytic germ supplies the frozen point version; it is not a claim
that a.e. measure uniqueness determines arbitrary null-point values.
Thus every owner has exactly its own legal clock
\[
\kappa_O(A)=\log d_O(A),\qquad
d_O(A)=|\delta_{q_O(A)}(A)|>0 .
\]
No clock is defined at a terminal next step. Signed and zero legal clocks
are allowed; no positive roof or physical-time normalization is inserted.

For clarity, an explicit FULL-entry formula is available without any
eigenbasis. Write \(A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\),
\(\Delta=ad-bc\ne0\), and order H's entries as 11,12,21,22.
Direct left/right multiplication gives
\[
\delta_q(A)=\det\!\left(I_4-\frac{q}{\Delta^2}
\begin{pmatrix}
d^2&-cd&-bd&bc\\
-2bd&2ad&2b^2&-2ab\\
-cd&c^2&ad&-ac\\
2bc&-2ac&-2ab&2a^2
\end{pmatrix}\right).
\]
This is the full native four-dimensional determinant, not the determinant
of a selected scalar, symmetric, unstable or eigendirection component.

## 4. Entire history, kernels, isotropy and generic incoming

For each owner let \(P_O(B)\) contain ALL retained inverse solutions from
Section 2, with identical points identified, and recursively define
\[
P_O^0(B)=\{B\},\qquad
P_O^{j+1}(B)=\bigcup_{A\in P_O^j(B)}P_O(A).
\]
The inverse identities prove by induction that this is precisely every
legal j-step starting point into B. All q, real roots, source pieces and
depths remain. This is an exact unrestricted recursion, not a finite census.
It applies to singular/critical/terminal targets as well as legal targets.

On legal finite histories define
\[
M_r(A)=\prod_{i=0}^{r-1}d_O(T_O^iA),\quad S_r=\log M_r,\quad M_0=1 .
\]
All products are positive finite. The actual retained-lag groupoid is
\[
\mathscr G_O=\{(A,r-s,B):T_O^rA=T_O^sB,\ r,s\ge0
                                  \text{ both histories legal}\}.
\]
It is a countable Borel groupoid: equal-iterate relations are Borel,
integer lags form a countable set and the complete inverse atlas gives
countable source/range fibres.
Equal triples, not extra history labels, are identified.
If two witnesses have the same r-s, the longer adds an equal legal tail
at their common endpoint. Its identical clock products cancel. Therefore
\[
c_O(A,r-s,B)=\log\frac{M_r(A)}{M_s(B)}
\]
descends to the actual triple. For composable witnesses, advance the shorter
middle history to the longer already legal one. Middle products then
cancel and lags add, proving additivity without any terminal continuation.
Inversion negates c; the forward arrow \((T_OA,-1,A)\) has clock \(-\kappa_O(A)\).
The density of a source-to-range finite history chart is
\(M_s(B)/M_r(A)=e^{-c_O}\), by composition of its own IMAGE charts.
Countable disjoint restrictions give the same every-Borel history identity.

The COMPLETE kernels are
\[
\begin{aligned}
\ker\ell&=\{(A,0,B):T_O^rA=T_O^rB\text{ for some legal }r\},\\
\ker c&=\{(A,r-s,B)\in\mathscr G_O:M_r(A)=M_s(B)\},\\
\ker\ell\cap\ker c
 &=\{(A,0,B):T_O^rA=T_O^rB,\ M_r(A)=M_r(B)
                                          \text{ for some legal }r\}.
\end{aligned}
\]
All coalescences and all distinct equal-level inverse points remain.
No globally injective map or unit lag kernel is assumed for any owner.

All incoming arrows at range A are exactly
\[
(A,r-s,B),\qquad r\text{ legal at }A,\quad s\ge0,\quad
B\in P_O^s(T_O^rA).
\]
At range height h the source height is \(h-c_O(A,r-s,B)\).
At a terminal only r=0 is allowed; all backward words and its identity
still remain. There is no floor, root, phase or depth cutoff.

Nonzero source isotropy is equivalent to an eventually periodic legal
future: unequal-time equalities produce a legal cycle, and conversely an
eventual cycle supplies equalities. If its least source period is p,
advancing any equality into the core forces its lag into pZ, while all
signed multiples are realized by sufficiently late times.
If K is the clock sum on one least core traversal, the entire groups are
\[
\mathscr G_{O,A}^{A}=p\mathbb Z,\qquad H_A=K\mathbb Z .
\]
Entrance products cancel. Finite-terminal and non-eventually-periodic
futures have trivial source isotropy and H=0.
The full \(X\times\mathbb R\) extension has isotropy \(\{kp:kK=0\}\):
it keeps all pZ when K=0 and is trivial otherwise.
For a packet choose an actual arrow \(g_A:A\to b\). Its phase is
\(h+c(g_A)\) modulo \(H_b\). Changing that arrow changes the phase only by H.
Height translation on the orbit SET has stabilizer exactly H; no nice
quotient is needed. For K nonzero its least positive time is |K| and
repetitions are \(j|K|\); for H=0 every real phase remains and no positive
time exists, even if source isotropy is nontrivial.

## 5. ENTIRE fixed sets on the whole source

For MAIN or G, a legal fixed point satisfies
\(qA^{-1}C=J\). q=0 cannot satisfy this equation. Left multiplying by A
and using \(J^2=I\) gives
\[
A=qCJ=\begin{pmatrix}0&q\\2q&0\end{pmatrix},\qquad q\in\mathbb Z\setminus\{0\}.
\]
Its ACTUAL floors, for every signed integer q, are m=q and n=2q.
For MAIN the arithmetic permission holds, but the actual quotient is 2;
for G its actual floor quotient is also 2. Hence in either own map the
fixed equation forces q=2 and leaves only
\[
A_*=2CJ=\begin{pmatrix}0&2\\4&0\end{pmatrix}.
\]
This exhausts the entire real carrier, not just a box, diagonal sector or
the integer seed. Legality and regularity of this remaining point must
still be checked; that check is performed below.

For D, the fixed equation is \(qA^{-1}C=0\).
Since A and C are invertible at a legal source, it is equivalent to q=0.
The entire candidate fixed set is therefore
\[
\mathcal F_D=\{A:\det A\ne0,\ \lfloor A_{12}\rfloor\ne0,\
                                \lfloor A_{21}\rfloor=0\}.
\]
Every such point indeed has own q=0, \(L_{0,A}=I_4\), determinant one,
and \(T_D(A)=A\). Thus every listed point is regular and legal, proving
\(\operatorname{Fix}(T_D)=\mathcal F_D\) exactly.
All signs allowed by these floors and their exact endpoints remain.
Every core in this full family has its own step clock zero.
It is not asserted that D's clocks or cocycle vanish outside those cores.

## 6. A* legality and its FULL four-dimensional clock

At A*, \(m=2,n=4\); MAIN has \(2\mid4\) and actual q=2.
G independently has its own quotient \(\lfloor4/2\rfloor=2\).
Also \(\det A_*=-8\ne0\), and
\[
A_*^{-1}=\begin{pmatrix}0&1/4\\1/2&0\end{pmatrix},\qquad
A_*^{-1}C=\tfrac12J.
\]
It follows that \(f_2(A_*)=A_*+J-J=A_*\), in each own map.
For \(H=\begin{pmatrix}x&y\\z&w\end{pmatrix}\), the full derivative is
\[
L_{2,A_*}(H)=H-A_*^{-1}HJ
=\begin{pmatrix}x-w/4&y-z/4\\z-y/2&w-x/2\end{pmatrix}.
\]
Simultaneously ordering input and output coordinates as (x,w,y,z)
gives TWO blocks \(\begin{pmatrix}1&-1/4\\-1/2&1\end{pmatrix}\).
Each has determinant \(1-1/8=7/8\), so the FULL determinant is
\[
\delta_2(A_*)=(7/8)^2=49/64\ne0,\qquad
J_{\rm actual}(A_*)=64/49,\qquad K_*=\kappa(A_*)=\log(49/64).
\]
This proves actual regularity, not merely formal fixedness, and completes
\[
\operatorname{Fix}(T_{\rm M})=\operatorname{Fix}(T_G)=\{A_*\}.
\]
The two owners reach this result with their own permissions/inverses.
Both factors of the four-entry volume are mandatory; using only one block
would change the frozen IMAGE clock, not normalize this same object.

## 7. EVERY fixed-core incoming, entire packet and phase

For each owner's every found fixed core F, define the EXACT entire basin
\[
\mathcal B_O(F)=\bigcup_{j\ge0}P_O^j(F).
\]
The recursion is the complete all-real Riccati-root/chart construction of
Sections 2 and 4, with the owner's own polynomial and source tests at
EVERY step. Equivalently it consists of all starts of all finite legal
sequences ending at F. Every actual branch remains; repeated descriptions
of the same point or triple do not add multiplicity.
This specifies the full incoming set at every depth; no singleton,
finite-basin, cardinality cutoff or closed-form root selection is claimed.
An arrow relating a source to a fixed core exists exactly when the source
eventually reaches it, since the core's entire forward tail is constant.
Thus this basin is the whole source packet, not a selected invariant subset.
Distinct fixed cores cannot share a packet.

Let d(A) be first arrival at F, \(\eta(A)=S_{d(A)}(A)\),
\(K=\kappa_O(F)\), and \(v(A)=\eta(A)-d(A)K\).
For ANY A,B in this basin and EVERY integer k, sufficiently late arrival
times give an actual arrow (A,k,B), and its value is exactly
\[
c_O(A,k,B)=v(A)-v(B)+kK .
\]
Indeed at time r>=d(A), \(S_r(A)=v(A)+rK\); the corresponding expression
for B gives the formula at every common meeting after arrival, and
representation independence proves it for all witnesses.
Therefore, on the WHOLE basin,
\[
\begin{aligned}
\ker\ell&=\{(A,0,B):A,B\in\mathcal B_O(F)\},\\
\ker c&=\{(A,k,B):v(A)-v(B)+kK=0\},\\
\ker\ell\cap\ker c&=\{(A,0,B):v(A)=v(B)\}.
\end{aligned}
\]
Every basin source has source isotropy Z and ENTIRE \(H=K\mathbb Z\),
regardless of the number or clocks of entrance paths.
Extension isotropy is \(\{k:kK=0\}\).
Its complete fixed-reference phase is \(h-\eta(A)\) modulo KZ,
equivalently \(h-v(A)\). At (F,h), ALL incoming source heights from A are
\(h+v(A)-kK\), with every integer k and every basin A retained.

For MAIN and G, take F=A* and K=log(49/64), separately for each owner.
Their basins need not be equal; neither is replaced by its fixed centre.
Each own whole packet has
\[
H=(\log(64/49))\mathbb Z,\quad
\text{source isotropy }\mathbb Z,\quad
\text{extension isotropy }\{0\},\quad
\text{all phases }\mathbb R/(\log(64/49))\mathbb Z .
\]
Thus its genuine primitive is \(\log(64/49)\), not a selected repetition,
half-clock or entrance-clock value. All positive repetitions are its
positive integer multiples.

For EACH \(F\in\mathcal F_D\), K=0 and v(A)=eta(A) in its OWN full basin.
All those basin sources have H=0, source and extension isotropy Z, and
full real phase \(h-\eta(A)\). The clock kernel is exactly
\(\eta(A)=\eta(B)\), with every lag; it is not asserted to be the entire
basin groupoid. Entrance clocks can enter the phase offset and must not
be reset merely because the fixed core's clock is zero.
No positive primitive exists on any of these D fixed packets.
Distinct F remain distinct packets, and no assertion is made about
unclassified higher-period D cores or the global vanishing of D's cocycle.

## 8. Decisive gate, controls and limits

Exactly \(1<64/49<2\), since \(49<64<98\). Hence
\[
0<\log(64/49)<\log2 .
\]
No ordinary integer prime p can have this logarithm: every such p is at
least 2. MAIN has a genuinely owned positive primitive with this wrong
value in its COMPLETE A* packet. This is an actual necessary-target
failure, so the frozen disposition is STOP / FORK.
It is not an empty-ledger argument, a numerical approximation, or evidence
that a longer census might restore purity. Further source cycles could
not remove this retained wrong packet.

G independently retains the same wrong fixed-core clock without MAIN's
arithmetic permission: it provides no arithmetic credit for that clock.
D independently has the complete zero-clock fixed family, with all
incoming/ineffective isotropy retained. Its control does not imply a
global zero-clock theorem for all D periods.
These control results expose the PROVES_TOO_MUCH risk of treating a
nonlinear derivative factor as intrinsically prime-selected.
Selecting one derivative block, renormalizing time, choosing a root,
deleting the packet or changing C,J/measure would define a different owner.

The same-object ledger is intact throughout: full source, three own laws,
native four-entry measure, all actual roots, point version, whole history,
all heights and repetitions were retained. Strong naturalness is OPEN;
arithmetic T1 NOT PASSED; T3 NOT AUDITED; classical NOT APPLICABLE;
formal Route UNASSIGNED; B NOT INVOKED.
The decisive result was sent to root before this report was written.
No higher-period census, scientific numerical run or manuscript access occurred.
EOF — freeze after full self-read; HOLD for root's full read and distinct PAPER UNLOCK.
