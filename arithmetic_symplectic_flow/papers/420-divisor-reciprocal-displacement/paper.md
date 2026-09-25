# Divisor reciprocal displacement: two distinct prime-2 return packets

Candidate ID: `ANG-20260923-DRD01`  
Session date: 2026-09-23. Carrier: arithmetic Borel source groupoid with an IMAGE-clock extension.
Outcome: `OWNED POSITIVE CLOCK; DUPLICATE PRIME-2 PACKETS — STOP / FORK`

## Abstract

A current integer divisibility test permits a nonlinear reciprocal displacement of a full real two-coordinate source. We admit its prescribed positive finite all-point inverse-IMAGE clock and those of three separately owned controls. The maps need not be injective: all actual algebraic inverse branches, terminal targets, coalescing histories and clock kernels are retained. In the six frozen floor rectangles MAIN has two fixed cores, $(-\sqrt3,-\sqrt3)$ and $(\sqrt2,\sqrt2)$. Each full source packet, including every incoming depth and height phase, has entire clock isotropy $(\log2)\mathbb Z$. Their basins cannot meet, so they are distinct packets for the same ordinary prime. This disproves the necessary uniqueness condition despite a nonempty, owned positive clock. The prescribed two-step cell word and its rotation have no actual two-cycles. No other cells or higher periods are classified.

## 1. Contract, arithmetic source and target

The [candidate card](candidate-card.md), original lines 1–88 through its frozen EOF, has SHA-256 `31ea137041ecd06bee01bbaa421251517285d7c28db722240a1d4145104da88e`. Root released author mathematics after reading the complete CP1 scope review. This author read the card, not that review, any raw proof or any peer manuscript.

Each owner separately uses full $X=\mathbb R^2$, ordinary Borel sets and $\mu=dx\,dy$. At its current point set
$$
n=\lfloor x\rfloor,\quad m=\lfloor y\rfloor,\quad d=|m|,
\quad g=\gcd(|n|,d),\qquad \gcd(0,0)=0,
$$
$$
r(n,m)=
\begin{cases}
n-d\lfloor n/d\rfloor,&d>0,\\
n,&d=0.
\end{cases}
$$
The permission $r=0$ includes $0\mid0$ but excludes $0\mid n\ne0$. All floor cells are half-open. No signs, axes, units, cuts, null points or failed-permission states are removed.

At an integer seed $(n,d)$ with $n\ge2$ and $2\le d<n$, the geometric condition $x\ne0$ holds and $r=0$ is exactly $d\mid n$. Thus the prior-work arrow is proper-divisor symbolic admissibility $\longrightarrow$ current-step permission and gcd displacement $\longrightarrow$ actual geometry regenerating the next digits. No restriction to these integer seeds is made. The gate and the coefficient $1+g$ are designed choices; this verifies an interface, not strong arithmetic naturalness or a prime-only subsystem.

The necessary target requires a nonempty positive primitive ledger, every positive primitive to be $\log p$ for an ordinary integer prime, and at most one source packet per prime. All-prime coverage is additional. A MAIN ownership failure, wrong primitive or duplicate prime packet stops the target; a control failure does not decide MAIN. No prime table, inserted prime roof or externally supplied symbolic path is used.

## 2. Four actual maps and the complete inverse atlas

Write $F_O(x,y)=(y,x+\delta_Oy-a_O/x)$. The four owners are:

| Owner | Own legal source domain | $a_O(n,m)$ | $\delta_O$ |
|---|---|---|---|
| MAIN | $x\ne0,\ r(n,m)=0$ | $1+g$ | $1$ |
| P: PERMISSION-OFF | $x\ne0$ | $1+g$ | $1$ |
| C: CONTENT-OFF | $x\ne0,\ r(n,m)=0$ | $1$ | $1$ |
| D: DRIFT-OFF | $x\ne0,\ r(n,m)=0$ | $1+g$ | $0$ |

All illegal sources are forward terminals, retaining identities and all incoming arrows. They have no artificial absorbing step, reset or continuation across $x=0$. In particular $y=0$ is not a blanket terminal rule; its actual digits and permission decide legality. Every legal output recomputes all digits from the new real coordinates. Each displayed update is one source step, not a unit roof.

Given a target $(u,v)$, enumerate every $(n,m,\sigma)\in\mathbb Z^2\times\{-1,+1\}$, require $m\le u<m+1$, and put
$$
b=v-\delta_Ou,\qquad a=a_O(n,m)\ge1,\qquad
\xi_\sigma=\frac{b+\sigma\sqrt{b^2+4a}}2,\qquad
\theta^O_{n,m,\sigma}(u,v)=(\xi_\sigma,u).
$$
Its actual domain requires $\xi_\sigma\ne0$, $n\le\xi_\sigma<n+1$, agreement of all reconstructed digits, $g,r$, the owner's own permission, and exact own forward equality. Target next-step legality is not required. There is no index cutoff or positive-root selection; duplicate actual sources do not create duplicate arrows.

Indeed every predecessor has $y=u$ and solves $x^2-bx-a=0$. Since $a>0$, its two algebraic roots are distinct, nonzero and of opposite signs. The actual source determines $n,m$ and its root sign uniquely, so the enumeration is exhaustive. Conversely each passing root reconstructs a legal source and returns the target. A fixed branch is injective because its second output coordinate recovers $u$ and its first recovers $b=\xi-a/\xi$, hence $v$. Distinct branches may supply distinct predecessors of one target; this is not global injectivity.

All domains and maps are Borel, by the countable floor partition and the displayed continuous root formulas. For MAIN and D the inverse search simplifies without discarding a branch: permission with $d>0$ forces $g=d$, while permission with $d=0$ forces $n=0,g=0$. Thus for a target $m=\lfloor u\rfloor$ their two candidate roots use $a=1+|m|$, followed by the actual permission and floor checks. C uses $a=1$ followed by those checks. P retains the full integer-index enumeration because its coefficient is not subject to permission.

## 3. Own all-point IMAGE and positive source clocks

Freeze $n,m,\sigma$ on an inverse branch. For its root define
$$
q=\frac{\partial\xi_\sigma}{\partial b}
=\frac12\left(1+\frac{\sigma b}{\sqrt{b^2+4a}}\right)
=\frac{\xi_\sigma^2}{\xi_\sigma^2+a}\in(0,1).
$$
The last equality follows by differentiating $\xi-a/\xi=b$; its denominator never vanishes. The actual analytic inverse germ has
$$
D\theta=
\begin{pmatrix}-\delta_Oq&q\\1&0\end{pmatrix},
\qquad J_\theta=|\det D\theta|=q.
$$
This proves strict positivity and finiteness at every actual point, including floor boundaries with their assigned integer labels.

For fixed $a>0$, the function $x-a/x$ is an increasing analytic bijection from each open sign half-line onto $\mathbb R$: its derivative is $1+a/x^2>0$ and its endpoint limits are opposite infinities. Hence each displayed unrestricted root map is an analytic diffeomorphism from the target plane onto its source sign half-plane. Ordinary change of variables, restricted to any Borel subset of the actual checked domain, gives
$$
\mu(\theta E)=\int_EJ_\theta\,d\mu
$$
for every such $E$, also allowing infinite nonnegative integrals. Actual labels and root signs are unique for a source, establishing atlas compatibility. Floor-cut null subsets keep the specified analytic-germ value; there is no a.e. reassignment. A terminal target can have a legal inverse germ, while a missing forward step has no next-step clock.

All four owners therefore pass their own IMAGE admission. At a legal source,
$$
j_O(x,y):=J_{\theta_{(x,y)}}(F_O(x,y))
=\frac{x^2}{x^2+a_O(n,m)},\qquad
\kappa_O(x,y)=-\log j_O(x,y)
=\log\left(1+\frac{a_O(n,m)}{x^2}\right)>0.
$$
The selected inverse is the one returning that actual source, not an arbitrary incoming branch. The terminal next clock is NOT DEFINED, not zero. These are geometric IMAGE clocks, not an assertion of a classical conservative, symplectic or physical flight-time model.

## 4. Full actual groupoid, kernels and return groups

Fix any one owner and suppress $O$. For every legal finite forward history define
$$
Q_a(z)=\prod_{i=0}^{a-1}\left(1+\frac{a_O(n_i,m_i)}{x_i^2}\right),
\qquad S_a(z)=\log Q_a(z),\qquad Q_0=1,\ S_0=0,
$$
where $(x_i,y_i)=F^iz$. Every nonempty product is greater than $1$. The full Borel groupoid is
$$
G=\{(z,a-b,w):F^az=F^bw,\ a,b\ge0,\ \text{all steps legal}\},
\qquad s(z,k,w)=w,\ r(z,k,w)=z .
$$
Only identical actual triples are identified, not different lags; multiplication adds lags and inversion negates them. To compose two common-future presentations, extend the shorter middle forward history along the longer already-legal one. This supplies a common future without crossing a terminal, and proves closure. Countably many finite checked inverse words supply a Borel branch atlas.

The prescribed clock is
$$
c(z,a-b,w)=S_a(z)-S_b(w)=\log\frac{Q_a(z)}{Q_b(w)}.
$$
Two presentations of the same triple have lengths differing by a common integer. Extending the shorter presentation multiplies its two products by the same future factors, proving descent. The same cancellation after aligning common futures proves additivity and the inverse sign. In particular the forward arrow $(Fz,-1,z)$ has $c=-\kappa(z)$.

On a source-to-range branch, forward steps contribute IMAGE factor $Q_b(w)$ and inverse steps contribute $Q_a(z)^{-1}$. Thus its factor is $e^{-c}$. Finite change of variables proves the every-Borel identity for these compositions, and their prescribed germs agree pointwise under common extensions.

Unlike a partial bijection, equal lag does not cancel coalescing histories. The complete kernel membership criteria are
$$
\ker k=\{(z,0,w):\exists r\ge0,\ F^rz=F^rw\text{ legally}\},
$$
$$
\ker c=\{(z,a-b,w)\in G:Q_a(z)=Q_b(w)\},
$$
$$
\ker k\cap\ker c=
\{(z,0,w):\exists r\ge0,\ F^rz=F^rw,\ Q_r(z)=Q_r(w)\}.
$$
These are full-source exact criteria using finite arithmetic histories, not an enumeration of all their solutions. Section 7 exhibits nonunit members of the joint kernel.

For completeness, all incoming histories are constructively specified by the inverse roots. Let $\mathcal P_O(v)$ be the complete passing-root set of Section 2, and define
$$
B_0(v)=\{v\},\qquad B_{r+1}(v)=\bigcup_{w\in B_r(v)}\mathcal P_O(w).
$$
Induction proves $B_r(v)=\{w:F^rw=v\text{ legally}\}$, including every integer inverse branch, every depth and terminal target. Therefore all arrows incoming to range $z$ are exactly
$$
\bigcup_{\substack{a,b\ge0\\F^az\ {\rm legal}}}
\{(z,a-b,w):w\in B_b(F^az)\}.
$$
This is an untruncated root-and-source-check construction, not a restriction to the fixed-state window.

Nonzero source isotropy occurs exactly at eventually periodic points. Indeed $F^{b+k}z=F^bz$ for $k>0$ is an eventual return; conversely every eventual cycle supplies such presentations. If its least cycle period is $p$, all return differences are multiples of $p$, by division with remainder after reaching the cycle. Thus
$$
I_z=
\begin{cases}
p\mathbb Z,&z\text{ eventually reaches a least-period }p\text{ cycle},\\
\{0\},&z\text{ has no eventual cycle}.
\end{cases}
$$
For an eventual cycle reached after $\tau$ steps put
$$
L_z=\sum_{i=0}^{p-1}\kappa(F^{\tau+i}z)>0.
$$
Moving both isotropy presentations beyond the transient gives $c(z,kp,z)=kL_z$ and the entire $H_z=L_z\mathbb Z$. Otherwise $H_z=\{0\}$. This is a structural conditional formula, not a census of cycles elsewhere.

The extension has every object $(z,h)\in X\times\mathbb R$, product Borel structure, and arrows $(w,h)\mapsto(z,h+c)$. Its isotropy is the source isotropy intersected with the clock kernel. It is trivial for every source here: the cycle sum is strictly positive when isotropy exists. Nonunit clock-kernel arrows between different objects are nevertheless retained.

All real height translations commute with the arrows. On the extension's orbit set their full stabilizer at $[z,h]$ is precisely $H_z$, because equality after translation requires an actual source-isotropy arrow with that clock. Each actual source orbit carries every phase in $\mathbb R/H_z$, with $\mathbb R$ when $H_z=0$. No nice topological quotient is asserted. Only a least positive generator $L$ of the entire $H_z=L\mathbb Z$ defines a primitive; repetitions are $rL$, $r\ge1$. Distinct source orbits remain distinct packets, even with equal $L$.

## 5. Complete fixed sets in the six frozen full rectangles

A fixed point must have $x=y=t\ne0$. Write $k=\lfloor t\rfloor$. The MAIN/C/D permission always passes on this diagonal, including $k=0$, by the stated zero convention. MAIN and P have $a=1+|k|$, C has $a=1$. Their $\delta=1$ fixed equation is
$$
t^2=a.
$$
D instead requires $t=t-a/t$, which contradicts $a>0$. Retaining the full half-open cells gives:

| $(\lfloor x\rfloor,\lfloor y\rfloor)$ | MAIN | P | C | D |
|---|---|---|---|---|
| $(-2,-2)$ | $\{(-\sqrt3,-\sqrt3)\}$ | $\{(-\sqrt3,-\sqrt3)\}$ | $\varnothing$ | $\varnothing$ |
| $(-1,-1)$ | $\varnothing$ | $\varnothing$ | $\{(-1,-1)\}$ | $\varnothing$ |
| $(0,0)$ | $\varnothing$ | $\varnothing$ | $\varnothing$ | $\varnothing$ |
| $(1,1)$ | $\{(\sqrt2,\sqrt2)\}$ | $\{(\sqrt2,\sqrt2)\}$ | $\{(1,1)\}$ | $\varnothing$ |
| $(2,2)$ | $\varnothing$ | $\varnothing$ | $\varnothing$ | $\varnothing$ |
| $(4,2)$ | $\varnothing$ | $\varnothing$ | $\varnothing$ | $\varnothing$ |

For MAIN/P, the five diagonal integers $k=-2,-1,0,1,2$ require respectively $t^2=3,2,1,2,3$. Only $-\sqrt3\in[-2,-1)$ and $\sqrt2\in[1,2)$ meet their own digit assignments. The other signs or roots lie outside the required interval. C has only $t=\pm1$: both are retained lower endpoints of their displayed cells, not points in the adjacent cell below. In particular $1$ is excluded from $[0,1)$ and $-1$ from $[-2,-1)$. The off-diagonal cell cannot contain $x=y$. These arguments exhaust every real point and boundary in the frozen rectangles.

At every displayed fixed core, $t^2=a$, so its own density and clock are
$$
j=1/2,\qquad \kappa=\ell:=\log2>0.
$$
The all-point assignment matters for C's two integer-boundary fixed points. No measure-zero core is discarded or assigned a different version.

## 6. Only the prescribed two-step word and its rotation

For MAIN, C and D the whole cell $(n,m)=(2,4)$ fails permission, since $4\nmid2$. Thus the word $((4,2),(2,4))$ has an illegal second source, and its rotation an illegal first source. Neither is an actual two-cycle in those owners.

P has $a=1+\gcd(4,2)=3$ in each of the two specified cells. If a point $(x,y)\in[4,5)\times[2,3)$ had the specified two-step return, the first coordinate shift forces
$$
F_P(x,y)=(y,x),\qquad x+y-\frac3x=x,\qquad xy=3 .
$$
But $xy\ge8$. The rotated word gives the same product contradiction. Consequently P has no such return either. The two cells are disjoint, so no period-one point could be mislabeled an exact-two packet. No other two-step itinerary or higher period is inspected.

## 7. Complete incoming of the discovered cores and their packet identity

The passing-root atlas gives the following full direct-predecessor lists, not just predecessors inside the six rectangles:

| Owner and fixed core $p$ | Complete $\mathcal P_O(p)$ |
|---|---|
| MAIN $p_-=(-\sqrt3,-\sqrt3)$ | $\{p_-\}$ |
| MAIN $p_+=(\sqrt2,\sqrt2)$ | $\{p_+,(-\sqrt2,\sqrt2)\}$ |
| P $p_-$ | $\{p_-,(\sqrt2,-\sqrt3)\}$ |
| P $p_+$ | $\{p_+,(-\sqrt2,\sqrt2)\}$ |
| C $p_t=(t,t)$, $t=\pm1$ | $\{p_t,(-t,t)\}$ |

For MAIN at $p_-$, $m=-2$ makes the permitted coefficient $3$. Its roots are $\pm\sqrt3$, but the positive root has floor $1$ and fails $2\mid1$. Thus only the negative root survives. At $p_+$, $m=1$ permits both roots $\pm\sqrt2$.

Let $q_+=(-\sqrt2,\sqrt2)$, the other MAIN predecessor of $p_+$. Its own possible predecessors have $m=-2$, $a=3$, $b=2\sqrt2$, and first coordinates $\sqrt2\pm\sqrt5$. The positive root lies in $(3,4)$: it exceeds $1+2$, and is below $3/2+5/2$. The negative root lies in $(-1,0)$, since $\sqrt2<\sqrt5<\sqrt2+1$ and $(\sqrt2+1)^2=3+2\sqrt2>5$. Their floors are $3,-1$, both failing divisibility by $2$. Thus $q_+$ has no one-step $F$-predecessor. It still has a legal forward step and groupoid incoming arrows; it is not a forward terminal.

For P at $p_-$, $m=-2$ makes $a=3$ for even $n$ and $a=2$ for odd $n$. At this fixed target $b=0$, so the candidates are $\pm\sqrt a$. Checking their actual floors leaves exactly $-\sqrt3$ with even floor $-2$ and $\sqrt2$ with odd floor $1$. This exhausts all integer labels because these are the only possible coefficient values. P at $p_+$ has $a=2$ for every $n$, giving its stated two roots. C always has $a=1$ and both roots $\pm1$ pass the unit-divisor permission at either core.

For each such core use the exact Section 4 recursion and set
$$
B(p)=\bigcup_{r\ge0}B_r(p).
$$
Since $p$ is fixed, the levels are nested. They retain every actual predecessor at every depth, including points outside the window. The complete MAIN basins are $B(p_-)=\{p_-\}$ and $B(p_+)=\{p_+,q_+\}$: their predecessor lists have now closed exactly. P/C retain their full recursive root trees without a branch count, depth cutoff or canonical-tail selection. This is a proof of the complete incoming prescription at every depth, not a finite tree sample.

This recursion is also a complete source-orbit identification: $z$ shares a future with fixed $p$ exactly when some legal iterate of $z$ equals $p$. Thus its orbit is exactly $B(p)$, not merely the displayed core. Two different fixed cores have disjoint basins: once a deterministic forward orbit reaches one fixed point, it cannot reach another.

For $z\in B(p)$ let $h_p(z)$ be its least depth to $p$ and set
$$
\beta_p(z)=S_{h_p(z)}(z)-h_p(z)\ell .
$$
The full restricted groupoid and clock have the explicit form
$$
G|_{B(p)}=B(p)\times\mathbb Z\times B(p),\qquad
c(z,k,w)=k\ell+\beta_p(z)-\beta_p(w).
$$
To prove every integer lag is present, advance each endpoint to $p$ and then take sufficiently many fixed steps to realize their prescribed length difference. For an existing arrow, any earlier common future may likewise be extended to $p$; for $a\ge h_p(z)$, $S_a(z)=\beta_p(z)+a\ell$, which proves the formula independently of the presentation.

This provides all incoming arrows to every basin point, not just to its root. Source isotropy at each point is $\mathbb Z$, and its entire clock image is $\ell\mathbb Z$. Extension isotropy is trivial. On each basin the lag kernel is all $(z,0,w)$; the clock kernel consists exactly of triples satisfying $k\ell=\beta_p(w)-\beta_p(z)$; their intersection requires $k=0$ and $\beta_p(z)=\beta_p(w)$.

Each extra direct predecessor $q$ in the table satisfies its own $x^2=a$, hence $S_1(q)=\ell$, $h_p(q)=1$ and $\beta_p(q)=0=\beta_p(p)$. Therefore $(p,0,q)$ is a nonunit member of the joint kernel. The source is genuinely many-to-one; the units-only kernels of an injective comparator would be wrong here.

For MAIN this specializes further: $\beta_p=0$ everywhere on both complete basins. On its two-point basin of $p_+$ the lag, clock and joint kernels all equal the full zero-lag pair relation; on its singleton basin of $p_-$ they are only the unit. These are full packet-level statements, not assumptions about kernels elsewhere in $X$.

The extension phases on this entire packet are exactly
$$
h_{\rm height}-\beta_p(z)\pmod{\ell\mathbb Z}.
$$
Indeed an arrow changes this expression by $k\ell$, and any such change is realized by the full groupoid just proved. Thus all phases $\mathbb R/(\log2)\mathbb Z$ remain, with primitive $\log2$ and repetitions $r\log2$. No representative incoming tail or single height phase is selected.

## 8. Decision, limits and research integrity

MAIN has at least the two distinct source packets $B(p_-)$ and $B(p_+)$, each with positive primitive $\log2$. The integer $2$ is an ordinary prime, but the necessary at-most-one-packet-per-prime condition fails. This is a full-source counterexample: the exact incoming construction and deterministic disjointness show that omitted tails cannot merge these two packets or change their entire isotropy groups.

P and C each have their own two such fixed-core packets; these are controls, not evidence substituted for MAIN. D has no fixed point in the tested cells, and all four owners have empty prescribed two-step returns. These bounded emptiness results are not global no-cycle claims. Other-cell positive times, the EVERY-prime-time condition over the remaining ledger, and all-prime coverage are not classified. The conjunctive target is already stopped without further census or changing the map, measure, null version or arithmetic permission.

T0 ownership and the geometric clock are established. Arithmetic T1 is NOT PASSED: the designed divisor interface is exact but stronger naturalness is OPEN. T2 has the stated bounded counterexample; T3 is NOT AUDITED. Classical conservative/symplectic/suspension fields are NOT APPLICABLE; formal Route coordinates are UNASSIGNED and Route B is NOT INVOKED. The portfolio decision is STOP / FORK.

Methods were exact quadratic inversion, change of variables, floor checks and finite algebraic return equations. No scientific numerical run, external data, literature search, enlarged window, higher-cycle census, Git operation, PDF, operator or publication was used. The author read the original card lines 1–88 through EOF using `nl -ba`/`sed` and measured its line count and SHA-256. Final checks of the three author surfaces are mechanical text/link/identity/count/hash checks.

The definition scout read only old card 400 lines 1–24 and 405 lines 1–27, neither through EOF; heading searches exposed their outcome titles at 86/103, not bodies. Their full lengths and hashes were not measured in that scout. Additional discovery was filename-only and entry-heading metadata, not a third old card body. Previous authorship and shared history of those owners are disclosed. The present quadratic-root displacement is definitionally different from their displayed fractional-linear or affine inverses and does not execute 415's divisor word; no global novelty or nonconjugacy claim follows.

Quadratic inverse and possible fixed-equation reasoning informed pre-freeze design expectations. This was not blind or sealed preregistration, nor a certified pre-freeze result. Formal proof followed root's CP1 release. One bounded AUTHOR helper, `drd_pc_author`, read only the same original 88-line card and supplied P/C inverse-IMAGE, fixed-window, specified-word and incoming-tree derivations. It wrote no files and read no peer science; it is author assistance, not an independent review seat. The main author derived MAIN/D and the full general ledger and integrated the control proofs.

AI agents supplied design, mathematical derivation, drafting and internal workflow assistance, including root-managed scope review. Same-model shared-history assistance is `NOT_CALIBRATED`, not external peer review; no human or external verification is certified. There are no human subjects or private data. No funding or conflict declaration was supplied. Data availability: the exact formulas, proofs and [frozen card](candidate-card.md), [claim ledger](claim-ledger.md) and [summary](README.md) constitute the record; no numerical dataset exists.
