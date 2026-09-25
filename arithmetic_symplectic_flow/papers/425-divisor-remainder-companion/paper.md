# Scaled divisor-remainder companion: an owned clock and a prime-2 fixed packet

Candidate ID: ANG-20260923-DRC01. Date: 2026-09-23.
Outcome: `OWNED CLOCK; PRIME-2 FIXED PACKET — BOUNDED OPEN / FORK`

This is the first round of the authorized 425–429 batch, not authorization for a sixth round.
The [frozen card](candidate-card.md) defines the object; the [claim ledger](claim-ledger.md) and [package entry](README.md) summarize this proof.
AI agents supplied design, mathematical derivation, drafting and internal workflow review. The author and its bounded author helper share model/history; this is NOT_CALIBRATED, not blind or external peer review, and no human/external verification is certified.

## 1. Contract, arithmetic origin and exact scope

Each owner has $X=\mathbb R^3$, its ordinary Borel structure and three-dimensional Lebesgue measure $\mu$.
At $s=(x,y,z)$ read
$$
n=\lfloor x\rfloor,\qquad m=\lfloor y\rfloor,\qquad d=|m|,\qquad
q=\begin{cases}\lfloor n/d\rfloor,&d>0,\\0,&d=0,\end{cases}
\qquad r=n-dq.
$$
The three separate partial maps are
$$
F(s)=(y,z,xy-qz),\quad D_F=\{y\ne0\};\qquad
F_Q(s)=(y,z,xy),\quad D_Q=\{y\ne0\};\qquad
F_L(s)=(y,z,x-qz),\quad D_L=X.
$$
For MAIN and Q the whole plane $y=0$ is forward terminal, with identities and all actual incoming arrows, not an absorbing fixed plane.
The strip $0<y<1$, every floor face, all signs, coordinate axes and failed divisibility states remain in their specified owners. L has no forward terminals.

For integers $n\ge2$ and $2\le d<n$, the actual seed $s=(n,d,d^2)$ gives
$$
F(n,d,d^2)=(d,d^2,d[n-d\lfloor n/d\rfloor]).
$$
Thus $d\mid n$ is exactly zero third output on this interface; nondivisors execute a nonzero remainder instead.
That output enters the subsequent coordinate readouts. The seed is not a selected invariant source or a permission to discard other points.
The lineage is proper-divisor/prime-composite admissibility $\to$ scaled Euclidean remainder execution $\to$ nonlinear autonomous geometric feedback.
The embedding, readout, bilinear law and reference measure are design choices. Strong naturalness remains OPEN; no Logistic/Hénon conjugacy or conservative lift is asserted.

We prove the full branch and history ledger, all global fixed states, and only the specified two-step floor word and its rotation.
No higher-period census is performed. The global target concerns every positive primitive packet, uniqueness per ordinary prime and ultimately all-prime coverage; one good fixed packet cannot settle it.

## 2. All inverse branches and their actual domains

Write a target as $t=(u,v,w)$. For MAIN, each integer pair $(n,m)$ with its prescribed $q$ supplies
$$
\theta_{nm}(t)=\left(\frac{w+qv}{u},u,v\right).
$$
Its exact domain is $u\ne0$, $m\le u<m+1$, and $n\le (w+qv)/u<n+1$, with the source readouts above and actual forward equality.
These are Borel domains, including their assigned half-open faces. No legality condition is imposed on the target's next step.
Indeed the first two forward coordinates force $y=u,z=v$; the third then forces the displayed $x$. Conversely these checks give precisely that source and target.
Consequently enumeration over all integers is complete. Repeated actual points/triples are counted once, not as artificial branch multiplicity.

Q has the sole inverse $\theta_Q(t)=(w/u,u,v)$ on $u\ne0$, without fabricated integer labels.
It is a partial bijection from $D_Q$ onto $\{u\ne0\}$, even when the target has $v=0$ and is forward terminal.
L has
$$
\theta^L_{nm}(t)=(w+qv,u,v),
$$
on exactly the reconstructed floor conditions $m\le u<m+1$, $n\le w+qv<n+1$, and its prescribed source quotient.
The same coordinate argument proves completeness. In particular $u=0$ is allowed, with $m=q=0$.
This accounts for all zero and unit readouts without borrowing MAIN's domain for L.

For explicit incoming enumeration, when $d=|\lfloor u\rfloor|>0$ the identity
$\lfloor\lfloor x\rfloor/d\rfloor=\lfloor x/d\rfloor$ follows because the endpoints $qd$ are integers.
MAIN's full predecessor list can therefore be written
$$
P_F(u,v,w)=
\left\{\left(A+qB,u,v\right):q\in\mathbb Z,\ 0\le A+q(B-d)<d\right\},
\qquad A=w/u,\quad B=v/u,
$$
provided $u\ne0$. The old integer $n$ is recovered as $\lfloor A+qB\rfloor$, not discarded from the check.
If $d=0$ and $u\ne0$, necessarily $0<u<1$ and $P_F=\{(w/u,u,v)\}$; if $u=0$, $P_F=\varnothing$.
For L, if $d>0$ its full list is
$$
P_L(u,v,w)=\{(w+qv,u,v):q\in\mathbb Z,\ 0\le w+q(v-d)<d\};
$$
if $d=0$ it is $\{(w,u,v)\}$, including $u=0$. For Q it is the sole inverse above or the empty set.
These are exact all-integer prescriptions, not bounded searches. A resonant inequality may admit all integer labels; it must not be replaced by a finite or principal selection.

## 3. The owned all-point IMAGE clock

Hold the assigned integer label fixed when differentiating its analytic inverse germ. MAIN and Q have
$$
D\theta=
\begin{pmatrix}
-(w+qv)/u^2&q/u&1/u\\
1&0&0\\0&1&0
\end{pmatrix},
\qquad J(t)=|\det D\theta(t)|=1/|u|,
$$
where Q uses $q=0$. L has
$$
D\theta^L=
\begin{pmatrix}0&q&1\\1&0&0\\0&1&0\end{pmatrix},
\qquad J_L(t)=1.
$$
The fixed-label MAIN/Q map is a smooth diffeomorphism on $u\ne0$ onto $y\ne0$; L's fixed-label germ is an affine diffeomorphism of $\mathbb R^3$.
Ordinary change of variables restricted to any Borel subset $E$ of the actual branch domain therefore gives
$$
\mu(\theta E)=\int_E J(t)\,d\mu(t).
$$
This holds for every such Borel set, including sets supported on floor faces. On null faces the displayed germ, rather than the integral alone, fixes the finite positive pointwise version.
The same prescribed source has one assigned label; there is no arbitrary periodic-point completion.
Thus on every legal source
$$
\kappa_F(x,y,z)=\kappa_Q(x,y,z)=\log|y|,\qquad \kappa_L=0.
$$
The clock of a nonexistent terminal next step is NOT DEFINED. Negative and zero legal clocks are retained.
For L the branch IMAGE density being one does not assert global measure preservation of the possibly many-to-one map.
These are geometric IMAGE clocks, not supplied positive roofs or a claimed classical physical suspension.

## 4. Full actual histories, kernels, isotropy and phases

Fix one owner $O\in\{F,Q,L\}$. Every iterate below must be legal.
Set $W_0=1$ and, for MAIN/Q,
$$
W_a(s)=\prod_{0\le i<a}|\operatorname{second}(F_O^i s)|,\qquad S_a(s)=\log W_a(s).
$$
For L set $W_a=1,S_a=0$. All products are finite and strictly positive; no infinite energy or infinite product is introduced.
The actual groupoid is
$$
G_O=\{(z,a-b,w):F_O^a z=F_O^b w,\ a,b\ge0\},
\qquad s(z,k,w)=w,\quad r(z,k,w)=z.
$$
Equal actual triples, and only equal triples, are identified. Inversion reverses endpoints and lag; composition adds lags.
The groupoid inherits the Borel structure of $X\times\mathbb Z\times X$: legal iterate domains are Borel, and its defining equality sets form a countable union of Borel sets.
To compose two witnesses, align their common middle trajectory at the longer of its already existing legal lengths. The required shorter continuation of the other witness then exists; no continuation through a terminal is invented.

If two witnesses give the same lag, their lengths differ by a common integer. Extending the shorter common future to the longer one adds the same clock sum to both sides.
Hence the following is well defined and additive:
$$
c(z,a-b,w)=S_a(z)-S_b(w)=\log\frac{W_a(z)}{W_b(w)}.
$$
For example, if the second composable witness is $F_O^d w=F_O^e v$ with $d\ge b$, the composite witness is $F_O^{a+d-b}z=F_O^e v$; the identity $S_{a+d-b}(z)=S_a(z)+S_d(w)-S_b(w)$ proves additivity. The other inequality is symmetric.
In particular $(F_Os,-1,s)$ has clock $-\kappa_O(s)$.
An actual arrow germ, using its specified forward and inverse histories, has IMAGE factor $W_b(w)/W_a(z)=e^{-c}$.
This also makes the germ version compatible with common-future changes of witness.

The complete kernels, not just isotropy kernels, are
$$
\ker k=\{(z,0,w):F_O^r z=F_O^r w\text{ for some legal }r\ge0\},
$$
$$
\ker c=\{(z,a-b,w)\in G_O:W_a(z)=W_b(w)\},\qquad
\ker k\cap\ker c=\{(z,0,w):F_O^r z=F_O^r w,\ W_r(z)=W_r(w)\}.
$$
For Q, injectivity of every legal iterate makes $\ker k$ and the joint kernel precisely the units.
For L, $\ker c=G_L$ and the joint kernel is $\ker k$; zero clock does not erase integer lag or nontrivial source arrows.

Here is a constructive full-source incoming prescription, including null and terminal objects.
For any target $v$, put $B_0(v)=\{v\}$ and $B_{b+1}(v)=\bigcup_{w\in B_b(v)}P_O(w)$, with the complete predecessor lists of §2.
Induction on $b$ shows that $B_b(v)$ is exactly the set of legal depth-$b$ predecessors.
All arrows incoming to a fixed range $z$ are exactly
$$
\bigcup_{\substack{a,b\ge0\\F_O^a z\ {\rm legal}}}
\{(z,a-b,w):w\in B_b(F_O^a z)\}.
$$
Thus all labels and depths are retained; this is not a finite-difference quotient or a restriction to the fixed-point window.

For an arbitrary source point, nonzero isotropy is equivalent to an actual eventual cycle: a repeated forward state gives a cycle, and a cycle supplies repeated witnesses.
If no eventual cycle exists, $I_z=\{0\}$ and $H_z=c(G_z^z)=\{0\}$.
If its eventual cycle has least source period $p$, then $I_z=p\mathbb Z$. Write $C$ for the sum of $\kappa_O$ once around that cycle.
Cancellation of the identical preperiodic segment gives
$$
c(z,kp,z)=kC,\qquad H_z=C\mathbb Z.
$$
These statements are exact for every source, not a claim to have enumerated all cycles. Terminal histories have no eventual cycle.

The full extension has objects $(z,h)\in X\times\mathbb R$ and arrows $(w,h)\mapsto(z,h+c)$.
Its isotropy is $I_z\cap\ker c$: it is trivial when $C\ne0$, and is the whole $p\mathbb Z$ when $C=0$.
Height translation on the set-level orbit space has entire stabilizer $H_z$; over a chosen source orbit its phases are $\mathbb R/H_z$.
If $H_z=C\mathbb Z\ne0$, the positive primitive is $|C|$ and repetitions are $j|C|$, $j\ge1$.
If $H_z=\{0\}$ there is no positive primitive. Equal lengths do not identify different actual source orbits.
No smooth quotient, symplectic suspension or conservative physical flow is claimed.

For Q, its entire return-clock ledger simplifies without a further period census.
On any legal Q cycle, every $y_i\ne0$, and the two shift equations show that every $x_i,z_i$ is also nonzero.
Let $P_x,P_y,P_z$ be the products of their absolute values once around that finite cycle.
The shifts give $P_x=P_y=P_z$, while the third equation gives $P_z=P_xP_y$. Positivity forces $P_y=1$, so $C=\log P_y=0$.
Consequently $H_z=\{0\}$ for every Q source, including non-eventual and terminal histories; all source isotropy survives in the extension.
This does not assert $\kappa_Q=0$ on each step: Q has a nonconstant one-step clock whose cycle sums cancel.
L instead has identically zero one-step and arrow clocks, hence $H_z=\{0\}$ everywhere for the stronger direct reason.

## 5. Complete global fixed states

A fixed state for any owner must be $(t,t,t)$. Its quotient is $-1$ for $t<0$, $0$ for $0\le t<1$, and $1$ for $t\ge1$.
For MAIN, legality requires $t\ne0$, and the remaining equation is $t^2-qt=t$, or $t=q+1$.
The negative case would give the illegal $t=0$; the middle case gives $t=1$ outside that half-open case; the positive case gives
$$
\operatorname{Fix}(F)=\{p\},\qquad p=(2,2,2),\qquad \kappa_F(p)=\log2.
$$
For Q the equation is $t^2=t$ with $t\ne0$, so
$$
\operatorname{Fix}(F_Q)=\{(1,1,1)\},\qquad \kappa_Q(1,1,1)=0.
$$
For L it is $qt=0$, with no deleted zero plane:
$$
\operatorname{Fix}(F_L)=\{p_t=(t,t,t):0\le t<1\},\qquad \kappa_L(p_t)=0.
$$
The origin is an L fixed state and a MAIN/Q terminal state. The endpoint $t=1$ is not an L fixed state.
These are all fixed points on the entire real carrier, not only selected positive cells.

## 6. The prescribed two-step word and its rotation

Let $A=[4,5)\times[2,3)\times[4,5)$ and $B=[2,3)\times[4,5)\times[2,3)$.
The quotient is $2$ throughout $A$ and $0$ throughout $B$, including assigned faces.
For a MAIN two-cycle with its first state in $A$, closure of the two shift coordinates forces states $(x,y,x)$ and $(y,x,y)$.
The second step, whose quotient is zero, then forces $xy=x$. Since $x\ge4$, this gives $y=1$, incompatible with $y\in[2,3)$.
Thus MAIN has no such closed word. A cycle with the rotated word shifts one legal step to the excluded word, so it is excluded too.

For Q, either first transition has third coordinate $xy\ge8$, outside the required target third interval, $[2,3)$ or $[4,5)$.
For L, an $A$ source has third output $x-2z<5-8=-3$, incompatible with $B$; a $B$ source has third output $x\in[2,3)$, incompatible with $A$.
Hence both words are empty separately for each control as well.
The cells are disjoint, so a repeated fixed state could not satisfy this word; no least-period-two packet is hidden by a fixed-repeat identification.
This conclusion concerns exactly these whole half-open cells, not all period-two trajectories.

## 7. Full incoming completion of the MAIN fixed packet

Put $a=(1,2,2)$, $b=(-2,1,2)$, $c_*=(-1/2,-2,1)$ and $\ell=\log2$.
The all-integer inverse inequality of §2 gives the following complete lists:

| Target | $d$ | $A=w/u$ | $B-d=v/u-d$ | Allowed $q$ | All predecessors |
|---|---:|---:|---:|---|---|
| $p$ | $2$ | $1$ | $-1$ | $0,1$ | $a,p$ |
| $a$ | $1$ | $2$ | $1$ | $-2$ | $b$ |
| $b$ | $2$ | $-1$ | $-5/2$ | $-1$ | $c_*$ |
| $c_*$ | $1$ | $-2$ | $3$ | none | none |

For clarity the four integer conditions are $-1<q\le1$, $-2\le q<-1$, $-6/5<q\le-2/5$, and $2/3\le q<1$, respectively.
Substitution recovers the displayed source coordinates and their original floor labels. This is an exhaustive inverse calculation, with no integer cutoff.
Therefore the entire source orbit of the fixed point is
$$
\mathcal B=\{p,a,b,c_*\},\qquad c_*\longrightarrow b\longrightarrow a\longrightarrow p\longrightarrow p.
$$
Every source joining this fixed orbit must be one of its finite-depth predecessors, and the table is closed under all predecessors.
The point $c_*$ has no predecessor but has a legal forward step; it is not a forward terminal and its groupoid incoming arrows are not empty.

The step clocks at $(p,a,b,c_*)$ are $(\ell,\ell,0,\ell)$.
Their least arrival depths at $p$ are $(0,1,2,3)$ and their arrival sums are $(0,\ell,\ell,2\ell)$.
Define $\beta(z)=S_{r(z)}(z)-r(z)\ell$, giving values $(0,0,-\ell,-\ell)$ in that order.
Extending any common future to $p$, and then using its fixed loop, yields the full restriction
$$
G_F|_{\mathcal B}=\mathcal B\times\mathbb Z\times\mathcal B,\qquad
c(z,k,w)=k\ell+\beta(z)-\beta(w).
$$
Every integer lag is realizable by advancing both endpoints sufficiently far; no earlier common future is discarded by this description.
Thus each point has source isotropy $\mathbb Z$, entire $H_z=\ell\mathbb Z$, trivial extension isotropy and positive primitive $\ell$, with repetitions $j\ell$.
All incoming arrows to any of the four points have all four possible source points and every integer lag.
The lag kernel is the complete zero-lag pair relation. The clock kernel has, for each pair, the unique lag $k=(\beta(w)-\beta(z))/\ell$.
Their intersection is the zero-lag pair relation within $\{p,a\}$ and within $\{b,c_*\}$.
In particular nonunit joint-kernel arrows are retained; so is the zero-clock forward arrow $(a,-1,b)$.
The full height phases are $h-\beta(z)$ modulo $\ell\mathbb Z$.
These four source points constitute one actual packet with all its tails and phases, not four equal-length packets or a selected representative.

## 8. Incoming completion of the control fixed cores

Q's sole inverse sends $(1,1,1)$ to itself, so its full source orbit is that singleton.
For each L fixed point $p_t$, $0\le t<1$, its target first coordinate forces $m=q=0$ on every inverse label; then $x=t$ and $n=0$.
It too has only itself as predecessor at every depth. Different $t$ cannot acquire a common future because both are fixed.
At each of these control cores, $G|_{\{p\}}=\{(p,k,p):k\in\mathbb Z\}$, $I_p=\mathbb Z$, $c=0$, and $H_p=\{0\}$.
The clock kernel is the whole restricted groupoid, the lag and joint kernels are the units, and extension isotropy remains $\mathbb Z$.
All phases are the unreduced real line, with no positive primitive. The uncountably many L fixed cores, including null individual points and the origin, are not deleted or collapsed.
Outside these cores the all-source formulas and incoming construction in §4 remain in force for each control.

## 9. Gate decision, reproducibility and limits

MAIN has an owned positive primitive $\log2$ at its unique global fixed core, with the complete packet and incoming multiplicity proved above.
The only prescribed two-step words are empty. No wrong prime length, duplicate positive packet or ownership failure was found in this window.
The result is therefore BOUNDED OPEN / FORK, not a global prime-only, global uniqueness or all-prime-coverage theorem.
The controls' zero return-clock ledgers do not decide MAIN by proxy; MAIN's other eventual cycles remain governed by the exact conditional ledger, not by a census.
The same candidate supplies its source, inverse IMAGE, clock, histories and packet. T0 owner bookkeeping is established; arithmetic T1 is NOT PASSED, and the global T2 prime target remains OPEN.
Strong naturalness is OPEN. T3 is NOT AUDITED; classical symplectic/suspension fields are NOT APPLICABLE, formal Route coordinates UNASSIGNED, and Route B NOT INVOKED.

The author personally read the frozen original card lines 1–93 through its then-measured EOF, SHA256 `d51292ce726c02338670acb5ad7da4bc2b28f115522f3dd1da855097d3b0fb46`, and reread only that prefix during drafting.
The retained paper template and ARS instructions govern the scope/provenance record; no review, raw proof or sibling manuscript was read for this authorship.
Definition-stage inputs were 318/card lines 1–27 and 343/card lines 1–56, neither to EOF. Their prefix hashes are recorded in the frozen card.
Only outcome headings at 318:166 and 343:185 were exposed, not their outcome bodies; original total lengths and full hashes were not measured then.
318's two-real-register permitted division and 343's discrete gcd-root driving a real quadratic fibre were definition comparisons, not imported results.
Root disclosed 426's cubic companion formula by message only. It shares the companion family but not the present scaled-remainder execution; no global novelty or nonconjugacy is claimed.
Informal inverse, seed and fixed-feasibility algebra informed design before freezing; this was not blind or sealed preregistration.

One bounded author helper, `drd_pc_author`, read only the same 93-line card and derived Q/L inverse, IMAGE, fixed, word and incoming ledgers.
That agent was reused from earlier author assistance and shares history; it was not an independent reviewer. The main author checked and integrated its control derivations.
The Q all-cycle product identity was accepted by root as a direct full-ledger identity within the frozen obligation, not an expanded period census.
Proof methods are exact coordinate inversion, Borel change of variables, finite product cancellation and integer inequalities; no scientific numerics, prime tables, fitted roofs, external literature or code-generated orbit tests were used.
Read commands used `sed -n '1,93p'` / numbered prefix reads; mechanical EOF, hash, Markdown-link and control-character checks concern artifacts only.
No cutoff or precision extrapolation is present. The next decision is a different authorized architecture, or a separately frozen justified scope, not retuning this clock or silently widening its cycle window.
