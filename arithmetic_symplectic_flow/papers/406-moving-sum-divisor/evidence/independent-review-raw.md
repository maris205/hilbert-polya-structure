# 406 — frozen card-only independent raw derivation

Candidate: ANG-20260923-MSD01. Date: 2026-09-23.
Batch: NONLINEAR-PACKET-20260923-L. Internal shared-history NOT_CALIBRATED.
Root reported reading the complete CP1 report and explicitly released this bounded mathematical derivation.
Sole current scientific input: candidate-card.md, complete lines 1–93 through its final blank line and actual EOF.
candidate-card.md: 93 lines; SHA256 ef460079eb0f5f604822611f93e09382fcd688a4e3d49f037e07ac04ffaba80c
Frozen CP1 scope-review.md: 77 lines; SHA256 9fc2d3de746334bbf9cdd63f4902cadc754c4bc88c7468d8c3e53396fce63b32
The card was reread completely after release and both receipts were checked.
No manuscript, README, ledger, author/peer result, old card or other new scientific package was read.
Earlier project history, including 401 review, remains exposed; independence here means card-only derivation before current manuscript access, not blind, external or cross-model review.
The ARS academic-research-suite SKILL.md was fully reread at CP1; its complete retained workflow, role, runtime and logical-fallacies instructions continue to govern this stage.
AI supplies this mathematical derivation and internal checking; no human or external verification is certified.
No scientific code, numerical experiment, literature search, auxiliary agent, operator or higher-period census was used.

## 1. Exact four-owner notation and whole sources

Each owner has its OWN full $X=\mathbb R^3$ and three-dimensional Lebesgue measure.
For compact notation write
\[
r(x,y)=x+\varepsilon y,\qquad M(y,z)=K(y,z).
\]
The exact frozen choices are:

| Owner | $\varepsilon$ | $K(u,v)$ | Actual source permission |
| --- | --- | --- | --- |
| MAIN | $1$ | $uv+1$ | $rM\ne0$, $a=\lfloor r\rfloor\ne0$, $a\mid\nu=\lfloor M\rfloor$ |
| D | $1$ | $uv+1$ | $rM\ne0$, with no floor restriction |
| S | $0$ | $uv+1$ | $rM\ne0$, $a=\lfloor r\rfloor\ne0$, $a\mid\nu=\lfloor M\rfloor$ |
| A | $1$ | $u+v+1$ | $rM\ne0$, $a=\lfloor r\rfloor\ne0$, $a\mid\nu=\lfloor M\rfloor$ |

Here divisibility is integer divisibility with signed nonzero divisor; every such divisor divides zero.
The owner law is exactly
\[
T(x,y,z)=(y,z,M(y,z)/r(x,y)).
\]
No coordinate is changed before evaluating its numerator and divisor.
All floor digits are recomputed from the current real state on the next step, not stored external labels.
Each legal domain is Borel by continuous arithmetic, Borel floor and a countable integer divisibility test.
Every point outside that owner's domain remains a terminal with its identity arrow and all actual incoming; it has no fictitious forward self-loop.

## 2. Complete inverse domains and genuine partial bijections

For arbitrary target $q=(u,v,w)$ put $K=K(u,v)$ with the owner's numerator.
On the open set $E_0=\{wK\ne0\}$ define
\[
\Theta(q)=(K/w-\varepsilon u,\ u,\ v).
\]
The reconstructed real divisor and numerator are exactly $r=K/w$ and $M=K$.
Consequently, the actual inverse domain for MAIN/S/A is
\[
E=\{wK\ne0,\ \lfloor K/w\rfloor\ne0,
             \lfloor K/w\rfloor\mid\lfloor K\rfloor\};
\]
for D it is the whole $E_0$.
Equivalently MAIN/S/A enumerate every integer pair $a\ne0,\nu$ with $a\mid\nu$ and
\[
a\le K/w<a+1,\qquad \nu\le K<\nu+1.
\]
These half-open cells are Borel and disjoint; no integer cutoff or deletion of $\nu=0$ is imposed.
They are restrictions of ONE reconstructed inverse point, not additional source fibres or multiple arrow labels.
There is no permission check for the target's next forward step.

For every permitted target, substituting $r=K/w$ proves $T\Theta(q)=q$.
For every legal source, its image has $w=M/r\ne0$ and target numerator $K=M\ne0$; then
\[
\Theta T(x,y,z)=(M/(M/r)-\varepsilon y,y,z)=(x,y,z).
\]
These identities prove both source/target exhaustion and all stated forward checks.
They also prove GLOBAL partial injectivity: every target has at most one actual predecessor in that owner.
No previous candidate's injectivity conclusion is used; it follows from these four current rational reconstructions.
All actual inverse histories are obtained by repeated application of this inverse, checking its actual domain at every step.
Signed coordinates, axes, unit floors, zero integer numerator and singular permissions remain exactly as frozen.

## 3. Every-Borel IMAGE and all-point analytic version

The unrestricted rational law is an analytic diffeomorphism from the open set $\{rM\ne0\}$ onto $E_0$, with the displayed inverse.
Its derivative matrix on $E_0$ is
\[
D\Theta=
\begin{pmatrix}
K_u/w-\varepsilon&K_v/w&-K/w^2\\
1&0&0\\
0&1&0
\end{pmatrix},
\qquad \det D\Theta=-K/w^2.
\]
Thus the frozen inverse IMAGE version for EACH owner is
\[
J(q)=|K(u,v)|/w^2,\qquad q\in E.
\]
It is finite and strictly positive at every actual target, including integer cuts and null restrictions.
Change of variables for the displayed analytic diffeomorphism, restricted to any Borel $B\subseteq E$, proves
\[
\mu(\Theta B)=\int_B |K(u,v)|/w^2\,d\mu(q).
\]
Both sides may be infinite; this does not affect the identity.
The source measure is unchanged three-dimensional Lebesgue measure.
The analytic extension fixes this all-point version; the integral identity alone would not determine arbitrary values on null subsets.
No extra counting factor arises: all three coordinates are real and the integer digits only describe the same actual restrictions.
Source and image Borel restrictions are nonsingular in both directions under the actual partial bijection.

At a legal source the inverse density and the owned clock are therefore
\[
J(Tp)=r(p)^2/|M(p)|,\qquad
f(p)=|M(p)|/r(p)^2>0,\qquad \kappa(p)=\log f(p).
\]
In particular MAIN/D use $f=|yz+1|/(x+y)^2$; S uses $f=|yz+1|/x^2$; A uses $f=|y+z+1|/(x+y)^2$.
These are each owner's own formulas, not a clock copied from a different transport.
Local clock may have either sign or vanish; it is not a positive suspension roof.
At a terminal there is no legal-step clock to assign.

## 4. Generic complete actual histories, cocycle and kernels

This section applies separately to each of the four proved partial bijections.
For every legal finite history define
\[
R_m(p)=\prod_{i=0}^{m-1}f(T^ip)>0,\qquad R_0(p)=1,\qquad S_m(p)=\log R_m(p).
\]
All points have the length-zero history; positive histories require the actual intermediate permissions.
The frozen actual arrow set is
\[
G=\{(p,m-n,q):T^mp=T^nq,\ m,n\ge0,\ \text{both histories legal}\},
\]
with source $q$ and range $p$, integer lag retained, and equal triples identified.
It is Borel as a countable union of legal-iterate equality sets.
Each source/range fibre is countable because each iterate and each actual inverse iterate is single-valued.
Set
\[
c(p,m-n,q)=\log\bigl(R_m(p)/R_n(q)\bigr).
\]
For two witnesses of the same triple, both indices change by the same integer.
Taking the longer existing witness appends the identical legal common tail to the two products, so that tail cancels.
This proves all-point descent without continuing through a terminal.
To compose arrows, align the two meetings on their common middle history at its larger already-valid index.
The same cancellation proves additivity; inversion changes the sign.
Finite inverse-history IMAGE factors are $R_m^{-1}$; the source-to-range map of a pair of inverse histories has factor $R_n(q)/R_m(p)=e^{-c}$ on every Borel restriction.
The chain rule inherits the same all-point versions on cuts, and descent makes different actual-arrow presentations consistent.

Injectivity gives the useful exact cancellation of histories:
\[
\begin{cases}
T^jp=q,&(p,j,q)\in G,\ j\ge0,\\
p=T^{-j}q,&(p,j,q)\in G,\ j<0.
\end{cases}
\]
Only nonnegative iterates are used on the right; these equations also suffice for membership when their histories are legal.
Indeed cancel the common shorter iterate using its injectivity.
It follows that the ENTIRE lag kernel consists of units, not an unproved quotient:
\[
\ker\ell=\{(p,0,p):p\in X\}.
\]
The ENTIRE clock kernel and intersection are
\[
\ker c=\{(p,m-n,q)\in G:R_m(p)=R_n(q)\},\qquad
\ker\ell\cap\ker c=\{(p,0,p):p\in X\}.
\]
This product-equality description includes all off-diagonal zero-clock arrows, not just isotropy.
In reduced form a positive lag $j$ has $c=S_j(p)$, while a negative lag $j$ has $c=-S_{-j}(q)$.
No complete clock kernel is replaced by a sign assumption on one local factor.

## 5. Generic entire isotropy, incoming and phases

An equality $T^mp=T^np$ with $m>n$ cancels to $T^{m-n}p=p$.
Thus nonzero source isotropy occurs exactly at an actual periodic point, not at an extra preperiodic incoming tail.
If its least period is $r$, its entire source isotropy is $r\mathbb Z$: every self-lag is divisible by $r$, and every multiple is realized.
Define on that actual least cycle
\[
C=\sum_{i=0}^{r-1}\kappa(T^ip)=\log R_r(p).
\]
Then $c(kr)=kC$ and the ENTIRE clock subgroup is $H_p=C\mathbb Z$.
Global partial injectivity prevents any extra state from entering a periodic cycle: a cycle point already has its unique cycle predecessor.
Therefore its full source class is exactly its cycle, not a selected core from a larger basin.
At every nonperiodic state source isotropy and $H_p$ are both zero, including terminals.
These are generic conditional statements; no higher-period solution is asserted or enumerated.

The extension keeps every $(p,h)\in X\times\mathbb R$, with $(q,h)\mapsto(p,h+c)$ for every actual arrow.
Its lag/clock kernels are the full lifts of the preceding kernels, with all heights.
Its isotropy at a periodic state is $\{kr:kC=0\}$: all $r\mathbb Z$ if $C=0$, and trivial if $C\ne0$.
At a nonperiodic state it is trivial.
All extension-orbit phases over a source class are $\mathbb R/H_p$: transporting to a reference point gives this quotient, and two choices differ exactly by a self-arrow clock.
Vertical height translation has stabilizer $H_p$ on that orbit SET.
If $C\ne0$, the least positive time is $L=|C|$, repetitions are $kL$ for positive integers $k$, and all phases of this physical orbit are retained.
If $H_p=0$, there is no positive time; phases form a free real translation line, even when zero-clock source isotropy survives in the extension.
No smooth global flow, positive roof or regular quotient topology is claimed.
Different source classes never merge because their times happen to coincide.

For an exhaustive incoming prescription at arbitrary $p$, take any legal $m\ge0$, then every legal inverse history of length $n\ge0$ from $T^mp$.
Its initial state $q$ gives the actual arrow $(p,m-n,q)$; deduplicate only identical triples.
The source height for an arrow ending at $(p,h)$ is $h-c(p,m-n,q)$.
Unique inverse reconstruction makes this completely specified, including all terminal incoming; for a terminal only $m=0$ is available.
Equivalently, partial-injective source classes are their full finite chains, one- or two-sided chains, or finite cycles, with every permitted endpoint retained.
No completion through a failed permission or infinite-history source enlargement is used.

## 6. COMPLETE fixed sets, with every formal root source-checked

Fixedness of any of the four shift maps first forces $x=y=z=t$.
For MAIN and D, the real nonzero conditions imply $t\ne0$, and
\[
t=(t^2+1)/(2t)\quad\Longleftrightarrow\quad t^2=1.
\]
Both $t=1$ and $t=-1$ are legal for D by its own nonzero conditions.
For MAIN, their divisor floors are respectively $2,-2$, their numerator floor is $2$, and each signed divisor divides $2$.
Thus the COMPLETE fixed sets of these two distinct owners are
\[
\operatorname{Fix}(T_{\rm MAIN})=\{(1,1,1),(-1,-1,-1)\}
=\operatorname{Fix}(T_D).
\]
For S, legal diagonal points have $t\ne0$; fixedness would require
\[
t=(t^2+1)/t,\qquad t^2=t^2+1,
\]
which has no real solution. Hence $\operatorname{Fix}(T_S)=\varnothing$ on its entire legal domain.

For A, legal diagonal fixedness requires $t\ne0$ and
\[
2t^2=2t+1,\qquad t_\pm=(1\pm\sqrt3)/2.
\]
Both formal roots meet the real nonzero conditions; they still require A's OWN floor permission.
Using $1<\sqrt3<2$, the positive root has
\[
2t_+=1+\sqrt3\in(2,3),\qquad 2t_++1=2+\sqrt3\in(3,4).
\]
Its floor divisor is $2$ and numerator floor is $3$, so it is NOT legal.
The negative root instead has
\[
2t_-=1-\sqrt3\in(-1,0),\qquad 2t_-+1=2-\sqrt3\in(0,1).
\]
Its floor divisor is $-1$ and numerator floor is zero; $-1\mid0$ is legal, while the real numerator is strictly positive.
Therefore
\[
\operatorname{Fix}(T_A)=\{(t_-,t_-,t_-)\}.
\]
The rejected positive formal root remains an actual terminal state, not a deleted point.
Its unique analytic predecessor is itself and fails the source permission, so it has no actual incoming other than its identity; its $H=0$ and phases are $\mathbb R$.
Its formal derivative is not a legal-step clock or a positive packet.

## 7. Entire ledger of every actual fixed core and the decisive MAIN gate

For each MAIN fixed point, its OWN target inverse density is $J=(t^2+1)/t^2=2$.
The same direct calculation applies to each D fixed point under D's own inverse.
For A's single admitted root, its fixed equation gives $2t_-+1=2t_-^2$, so its OWN $J=(2t_-+1)/t_-^2=2$.
Thus every actual fixed core listed above has $\kappa=-\log2$, not a manually assigned roof.

For each such core $p$, its full source class is the singleton $\{p\}$ by Section 5's proved partial injectivity.
ALL its incoming arrows are $(p,j,p)$ for $j\in\mathbb Z$, and
\[
c(p,j,p)=-j\log2,\quad
G_p^p=\mathbb Z,\quad H_p=(\log2)\mathbb Z,\quad
\operatorname{Iso}_{G^c}(p,h)=0.
\]
At target height $h$ the source height of this arrow is $h+j\log2$.
All phases are $\mathbb R/(\log2)\mathbb Z$; the least positive time is $\log2$, and repetitions are exactly $k\log2$.
The fixed-core lag kernel, clock kernel and intersection are all its identity arrow; no other source or height is selected out.
This is the ENTIRE subgroup and incoming structure, not one return whose primitive might later shrink.

MAIN consequently has TWO distinct actual fixed-core packets with the same ordinary-prime primitive time $\log2$.
They cannot be connected by an incoming history, and equal time does not identify their two source classes.
This violates the frozen “at most one actual packet per prime” requirement and is a decisive STOP / FORK.
The nonempty positive-ledger requirement is witnessed, but uniqueness fails; this is not an empty-window inference.
No claim is made that these are MAIN's only positive packets or that all its higher periods have prime times.

D separately has its own two fixed-core packets, so its fixed window also exhibits duplicate $\log2$ packets.
S has an empty fixed window, with its full generic ledger still given by Sections 4–5; this is not a theorem that its global positive ledger is empty.
A has exactly one $\log2$ packet in its fixed window and the rejected positive root retained as a terminal; this is not a global uniqueness, coverage or target pass.
No control conclusion repairs or automatically condemns MAIN; its own two retained fixed points already decide its necessary gate.

## 8. Exact prime-symbolic interface and final scope

For integers $1<d<n$, the frozen source $(d-n+1,n-1,1)$ has real divisor $s=d$ and numerator $N=n$.
Its floors are those same integers, so its MAIN permission is EXACTLY $d\mid n$.
For an admitted witness, the actual image is $(n-1,1,n/d)$.
This proves the proposed proper-divisor-symbolic interface and the real-quotient feedback, without replacing the whole real source by the slice.
Negative first coordinates and the negative MAIN fixed point remain; no positivity truncation is licensed.
This exact interface does not establish stronger naturalness or exclude arbitrary-encoding risks.

T0: each complete partial Borel owner, inverse/IMAGE and retained-lag extension is established.
T1: the prescribed all-point analytic-volume clock belongs to the same transport; stronger naturalness remains OPEN.
T2: full fixed-core packets are established, and MAIN's necessary uniqueness target FAILS by two $\log2$ packets.
The generic ledger elsewhere is complete as a conditional prescription; higher-period existence and locations remain unclassified.
Classical NOT APPLICABLE; T3 NOT AUDITED; formal Route UNASSIGNED; Route B NOT INVOKED.
Decision: STOP / FORK within the frozen short gate. No higher-period census, source deletion, domain repair or clock tuning follows.
The decisive fixed-core result was sent to root before writing this raw report.
This raw now freezes for root's full read; all author-surface access still awaits separate PAPER UNLOCK.

EOF — card-only independent raw, exact bounded fixed-window result.
