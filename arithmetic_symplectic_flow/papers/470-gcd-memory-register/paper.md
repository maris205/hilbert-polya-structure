# Delayed gcd memory creates two primitive log-two packets

Candidate ID: `ANG-20260925-GMR01`.
Outcome: OWNED MEMORY CLOCK; DUPLICATE PRIME-2 FIXED PACKETS — STOP / FORK

Paper470: `470-gcd-memory-register`; version1, 2026-09-25.
Batch `SYMBOLIC-RETURN-20260925-Y`, round1/5, exactly470–474.
Type: ANG measured Borel history owner with counting × area, not an ASFS suspension.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal coordinates UNASSIGNED; Route B NOT INVOKED.
AI-assisted same-model/shared-history work is NOT_CALIBRATED; no human, external or cross-family verification is certified.

## Abstract

The frozen owner couples an integer memory to two real coordinates: the present geometric digit becomes the next memory, while the previous memory enters both a gcd divisor and an additive feedback. We prove the complete inverse atlas and its every-point original counting × Lebesgue IMAGE, including all half-open cell faces. The resulting full-history clocks are logarithms of ratios of finite products of actual division factors; all incoming, kernels, entire isotropy-clock images and phases are retained. The global fixed set of MAIN consists of a zero-clock continuous family and two isolated states \(P_\pm=(\pm2,\pm2,\pm2)\). Each isolated state has only itself as a predecessor at every depth, and each owns a primitive \(\log2\). They are distinct full source orbits, so the one-packet-per-prime requirement is refuted. The three controls are audited separately: content-OFF has identically zero clock; additive-memory-OFF has only zero-clock fixed families; delayed-memory-OFF reproduces MAIN's fixed cores but has different incoming. No higher-period census, sign deletion, memory quotient or changed measure is used.

## 1. Full frozen owner and arithmetic lineage

Every owner has
\[
Y=\mathbb Z\times\mathbb R^2,\qquad
\mu=\#_{\mathbb Z}\otimes dx\,dy,
\]
with discrete/product Borel structure and original, unnormalized counting × area. For \(z=(m,x,y)\), let
\[
n=\lfloor x\rfloor,\qquad
\Gamma(m,n)=
\begin{cases}\gcd(|m|,|n|),&(m,n)\ne(0,0),\\1,&(m,n)=(0,0),\end{cases}
\quad g=\Gamma(m,n),\quad g_0(n)=\Gamma(n,n). \tag{1}
\]
All these factors are positive integers, including on the zero and unit states. The four TOTAL maps, with the labels of the actual frozen card, are
\[
\begin{array}{c|c}
M\text{ MAIN}&(n,y,(x+m)/g)\\
C\text{ content-OFF}&(n,y,x+m)\\
K\text{ additive-memory-OFF}&(n,y,x/g)\\
R\text{ delayed-memory-OFF}&(n,y,(x+n)/g_0(n)).
\end{array} \tag{2}
\]
Every successor is reread. No state is terminal; all negative memories, units, zero memory, axes, cuts and real coordinates remain. A point without a predecessor still has its specified outgoing step. In R, the old \(m\) remains an actual source field even though the continuous formula ignores it. Different memories are never discarded as redundant labels.

For integers \(1<D<N\), sources \((D,N+\alpha,y)\), \(0\le\alpha<1\), have \(\Gamma(D,N)=D\) iff \(D\mid N\). The comparison controls actual division, while the stored integer also translates geometry; the geometric update regenerates memory. Nondivisible sources execute their own gcd rule. This is bidirectional discrete/geometric feedback, not an external fixed integer parameter or prime-selected subsystem. It is a declared deformation, not a proved natural prime generator, conservative realization or Logistic/Hénon conjugacy.

The single return gate is the complete fixed set of every owner on all of \(Y\). The target requires nonempty positive packets, every primitive \(\log p\) for an ordinary prime, and at most one full packet per prime; all-prime coverage is additional. One actual duplicate MAIN packet suffices to stop the uniqueness condition. No second-period or bounded-label test is appended.

## 2. Complete inverse atlas and every-point original IMAGE

For a fixed owner write its continuous update as \((y,(x+b_{mn})/a_{mn})\) on source cell \(\{m\}\times[n,n+1)\times\mathbb R\), where
\[
\begin{array}{c|cc}
U&a_{mn}&b_{mn}\\ \hline
M&\Gamma(m,n)&m\\
C&1&m\\
K&\Gamma(m,n)&0\\
R&g_0(n)&n .
\end{array} \tag{3}
\]
For target \((n,u,v)\), every integer old memory \(m\) supplies the candidate
\[
\theta^U_{mn}(n,u,v)=(m,a_{mn}v-b_{mn},u).
\]
Its exact actual domain is
\[
\Omega^U_{mn}=
\{(n,u,v):n\le a_{mn}v-b_{mn}<n+1,\ u,v\in\mathbb R\}. \tag{4}
\]
These are Borel half-open strips in the target component. The source readout is \(n\), the reconstructed coefficient is (3), and forward substitution gives the target. Conversely every actual predecessor has one old memory \(m\), must solve the displayed affine equation, and satisfies (4). Hence all predecessors of every target are listed, including at boundaries and when the list is empty. There is no bound on \(m\).

Each \(\theta^U_{mn}\) is injective on its domain. Even when two branches have the same continuous formula, their different old-memory components are different actual source objects. No extra free label is introduced. The upper endpoint in (4) is excluded exactly because it has a different floor; the lower endpoint is included.

**Proposition 1.** The frozen every-point branch density and legal-source clock are
\[
J^U_{mn}(n,u,v)=a_{mn},\qquad
\begin{array}{ll}
\kappa_M(m,x,y)=\kappa_K(m,x,y)=-\log\Gamma(m,\lfloor x\rfloor),\\
\kappa_C(m,x,y)=0,\qquad
\kappa_R(m,x,y)=-\log g_0(\lfloor x\rfloor).
\end{array} \tag{5}
\]
For every Borel \(E\subset\Omega^U_{mn}\),
\[
\mu(\theta^U_{mn}E)=\int_E a_{mn}\,d\mu. \tag{6}
\]

**Proof.** Between these fixed counting components, the continuous inverse germ is affine with derivative
\[
\begin{pmatrix}0&a_{mn}\\1&0\end{pmatrix},
\]
whose determinant is \(-a_{mn}\). The source and target singleton labels each have counting mass one. The two-dimensional affine change-of-variables formula gives (6), also for infinite-measure Borel sets as an equality of nonnegative extended integrals. Restricting to the half-open strip preserves that identity. Every finite integer label gives \(1\le a_{mn}<\infty\), so the prescribed analytic-germ value is positive finite at EVERY actual point, including null cut faces. No ratio of zero set masses or arbitrary a.e. completion is used.

The forward fixed-cell determinant is \(-1/a_{mn}\). Thus \(-\log J_{\rm actual}(T_Uz)\) is exactly (5); signs and zero are retained. Differentiating the integer memory as if \(Y\) were \(\mathbb R^3\) would be the wrong measure and carrier. These are genuinely two-dimensional branch determinants with counting transport, not an added roof. \(\square\)

## 3. Actual histories and complete kernel formulas

Fix one owner at a time. All its iterates exist. Put
\[
A_0(z)=1,\quad A_r(z)=\prod_{i=0}^{r-1}a(T^iz),\qquad
S_r(z)=-\log A_r(z),
\]
where \(a(z)\) is that owner's factor from (3). Every \(A_r\) is a positive integer. Retain the Borel groupoid
\[
\mathcal G=\{(z,r-s,w):T^rz=T^sw,\ r,s\ge0\},\quad
c(z,r-s,w)=S_r(z)-S_s(w)=\log\frac{A_s(w)}{A_r(z)}. \tag{7}
\]
Source is \(w\), range is \(z\); inverse swaps endpoints and reverses lag. Equal actual triples are identified, with integer lag retained. It is a Borel subset of \(Y\times\mathbb Z\times Y\), a countable union of finite-iterate equality sets. Formula (4) makes every finite inverse fibre countable, so all source/range fibres are countable.

To check descent, two witnesses with the same lag differ by a common number of iterations. Their added factors at the common future coincide and cancel in (7). To compose arrows, extend their finite witnesses to the same iterate of the shared endpoint. All maps are total, so these extensions are actual; the middle sums cancel. This proves closure, lag addition and cocycle additivity. In particular
\[
c(Tz,-1,z)=-\kappa(z). \tag{8}
\]
For actual finite path branches, the history-pair map
\[
\psi=(T^r|_B)^{-1}\circ T^s|_D:\ w\longmapsto z
\]
has, by successive applications of (6),
\[
J_\psi(w)=\frac{A_r(z)}{A_s(w)}
=e^{-c(z,r-s,w)},\qquad
\mu(\psi E)=\int_E e^{-c(\psi w,r-s,w)}\,d\mu(w). \tag{9}
\]
Its domain requires every source-cell test along both paths. Countably many such branch words cover all arrows; their fixed-component affine germs give the same pointwise chain rule at cuts. This is the IMAGE direction from \(w\) to \(z\), not its reciprocal.

Here are exact full-source kernel membership formulas, with the indicated common future \(t\) ranging over all \(Y\):
\[
\begin{array}{ll}
\ker(\mathrm{lag}) &: (z,0,w),\ T^rz=T^rw=t\text{ for some }r,\\
\ker c &: (z,r-s,w),\ T^rz=T^sw=t,\ A_r(z)=A_s(w),\\
\ker(\mathrm{lag},c)&:\text{both conditions, with }r=s.
\end{array} \tag{10}
\]
Thus C has \(c\equiv0\) on its entire groupoid, not only on its fixed set; its clock kernel is the whole groupoid and its joint kernel is its lag kernel. Other owners retain the product equality in (10), not C's normalization.

The extension keeps all \(Y\times\mathbb R_h\) and arrows
\[
(w,h)\longmapsto(z,h+c(z,k,w)). \tag{11}
\]
Height translation acts on the set-level orbit space. There is no asserted regular quotient, chosen section, physical Hamiltonian realization or unit-time suspension.

## 4. All incoming histories, entire isotropy and phases

For each owner independently, let
\[
P_0(t)=\{t\},\qquad
P_{j+1}(t)=\bigcup_{v\in P_j(t)}
\{\theta_{mn}(v):v\in\Omega_{mn},\ m,n\in\mathbb Z\}. \tag{12}
\]
The first coordinate of \(v\) fixes \(n\). Completeness of (4) and induction show
\[
P_j(t)=\{z:T^jz=t\}\quad\text{for EVERY }j\ge0.
\]
Consequently ALL arrows incoming to range \(t\) are
\[
\{(t,r-j,z):r,j\ge0,\ z\in P_j(T^rt)\}. \tag{13}
\]
Every arrow's finite witness appears, and every listed triple is actual. Inverting these arrows gives all outgoing arrows. Compatible infinite incoming histories are exactly the sequences \(z_0=t,Tz_{j+1}=z_j\); (12) retains all such compatible choices. Neither surjectivity nor a selected infinite continuation is assumed.

Two sources are in the same orbit iff they have a common finite future. Two extended points \((z,h_z)\), \((w,h_w)\) are in the same orbit iff, for some such \(r,s\),
\[
h_z-h_w=S_r(z)-S_s(w).
\tag{14}
\]
These unrestricted recursion and equality tests retain the whole basins and all phase offsets.

A nonzero source-isotropy lag is equivalent to eventual entry into a finite cycle: an equality \(T^rz=T^sz\), \(r>s\), exhibits that cycle, and conversely cycling after entry supplies nonzero lags. If the eventual core has least period \(p\) and product
\[
Q=\prod_{i=0}^{p-1}a(T^iP)\in\mathbb N_{\ge1},\qquad \ell=-\log Q,
\]
then exactly
\[
I_z=p\mathbb Z,\quad c(z,kp,z)=k\ell,\quad H_z=\ell\mathbb Z. \tag{15}
\]
Every return difference is divisible by the least period; all multiples occur, and the transient products cancel. Otherwise \(I_z=H_z=\{0\}\). Extension isotropy is the zero-clock part: trivial if \(Q>1\), and all \(p\mathbb Z\) if \(Q=1\).

Over a full source orbit, phases are \(\mathbb R/H_z\), with offsets determined by (14). If \(Q>1\), the primitive is \(\log Q\) and repeats are its positive integer multiples. Factoring \(Q\) does not create shorter primitive loops. If \(Q=1\), all ineffective isotropy and real phases remain, but there is no positive primitive. These are structural formulas for all actual sources, not an enumeration of higher cycles. In particular C has an empty positive-clock ledger globally because its owned clock is identically zero; no C cycle census is needed.

## 5. Global fixed-set classification of all four owners

Define \(F_I=\{(\lfloor t\rfloor,t,t):t\in I\}\) and \(P_\pm=(\pm2,\pm2,\pm2)\).

**Theorem 2.** The complete fixed sets, over every integer memory and every real coordinate, are
\[
\operatorname{Fix}(M)=\operatorname{Fix}(R)=F_{[0,1)}\cup\{P_+,P_-\},\qquad
\operatorname{Fix}(C)=F_{[0,1)},\qquad
\operatorname{Fix}(K)=F_{[-1,2)}. \tag{16}
\]

**Proof.** For any of the four owners, equality of the first and second coordinates of source and target forces
\[
m=\lfloor x\rfloor,\qquad x=y=t.
\tag{17}
\]
No diagonality or integer restriction on \(t\) is assumed beforehand.

For MAIN, put \(h=\Gamma(m,m)\), equal to \(|m|\) when \(m\ne0\) and to one when \(m=0\). The last coordinate requires
\[
(h-1)t=m,\qquad m\le t<m+1. \tag{18}
\]
If \(m=0\), this gives every \(t\in[0,1)\). If \(m=1\) or \(-1\), the equation \(0=m\) has no solution. If \(m\ge2\), it forces \(t=m/(m-1)\); \(m=2\) gives \(t=2\), while \(m\ge3\) gives \(t\le3/2<m\). If \(m=-k\le-2\), it forces \(t=-k/(k-1)\); \(k=2\) gives \(t=-2\), while \(k\ge3\) gives \(t>-2\ge m+1\). Thus all \(k\ge3\) violate the half-open floor cell. This proves MAIN's full list.

For R, (17) makes its OWN \(n=m\), \(g_0(n)=h\), and additive term \(n=m\). Its own fixed equation is therefore exactly (18), giving the same list without identifying the maps away from fixed states.

For C, the own last coordinate says \(t=t+m\), so \(m=0\); (17) then gives precisely \(F_{[0,1)}\). Its coefficient was one from the outset.

For K, the own equation is \((h-1)t=0\). If \(|m|\le1\), then \(h=1\) and every \(t\in[m,m+1)\) works, giving \(F_{[-1,2)}\). If \(|m|\ge2\), it forces \(t=0\), contradicting \(\lfloor t\rfloor=m\). All signs, zero and unit memories, axes and integer endpoints have been included. \(\square\)

In M/R, every point of \(F_{[0,1)}\) has \(\kappa=0\), while both \(P_\pm\) have \(\kappa=-\log2\). All fixed states of C/K have clock zero. The fixed families include their left endpoints and exclude the stated right endpoints; \(P_\pm\) lie on retained null integer faces with the prescribed branch version.

## 6. Whole incoming packets for every fixed core

**Proposition 3.** Every MAIN fixed state, and every C fixed state, has only itself as a one-step predecessor. Consequently its entire incoming basin is a singleton, with only the constant compatible infinite ancestry.

**Proof for MAIN's zero family.** For target \(P=(0,t,t)\), \(0\le t<1\), an old memory \(m=0\) reconstructs \(x=t\). If \(m>0\), its factor is \(m\) and the reconstruction is \(m(t-1)<0\). If \(m=-k<0\), it is \(k(t+1)\ge1\). The latter two fail \(0\le x<1\). Thus only \(P\) remains.

**Proof for MAIN's signed cores.** At \(P_+\), every candidate factor \(g=\Gamma(m,2)\) is one or two. The reconstructed \(x=2g-m\) is an integer, so the cell condition \(2\le x<3\) forces \(m=2g-2\). For \(g=1\), this gives \(m=0\), whose actual gcd with two is two, not one. For \(g=2\), it gives \(m=2\), the actual source \(P_+\). At \(P_-\), the integer reconstruction \(-2g-m\) must equal \(-2\), hence \(m=2-2g\). The \(g=1\) candidate again has the wrong gcd; \(g=2\) gives exactly \(P_-\). No other integer memory is available.

**Own proof for C.** At \(P=(0,t,t)\), its reconstruction is \(x=t-m\). Since \(m\) is integral and \(0\le t<1\), \(\lfloor t-m\rfloor=-m\), so the target digit zero requires \(m=0\). In each case the all-depth conclusion follows from (12) by induction. \(\square\)

R and K must not inherit this predecessor conclusion. For ANY fixed \(P=(n,t,t)\) of R, its fixed equation gives \(g_0(n)t-n=t\), so
\[
P_1^R(P)=\{(m,t,t):m\in\mathbb Z\}. \tag{19}
\]
All these sources pass the same cell test and are different actual objects. For a fixed point of K, \(n=\lfloor t\rfloor\in\{-1,0,1\}\), its exact first predecessor set is
\[
P_1^K(P)=
\{(m,\Gamma(m,n)t,t):m\in\mathbb Z,\
\lfloor\Gamma(m,n)t\rfloor=n\}. \tag{20}
\]
For \(n=\pm1\) this includes every old memory, with continuous coordinates \((t,t)\). For \(n=0\) it retains the literal condition \(0\le\Gamma(m,0)t<1\), including every old memory at \(t=0\). Further levels for both controls are exactly (12), with all-depth coverage proved above, not a finite-tree approximation.

Here is an explicit full-basin clock and phase test for EVERY fixed core of EVERY owner. Set
\[
B_U(P)=\bigcup_{N\ge0}P_N^U(P),\qquad
\ell_P=\kappa_U(P),\qquad
\beta_U(z)=S_N^U(z)-N\ell_P\quad(U^Nz=P).
\tag{21}
\]
The value \(\beta_U\) is independent of the chosen entry depth, since additional fixed steps add \(\ell_P\). Any arrow meeting \(P\)'s source orbit has a common future equal to \(P\), so the orbit is exactly \(B_U(P)\). For any two sources in this basin and any integer lag \(k\), choose sufficiently large \(r,s\) with \(r-s=k\) after both have entered \(P\). Thus its complete restriction is
\[
\mathcal G_U|_{B_U(P)}
=B_U(P)\times\mathbb Z\times B_U(P),\qquad
c_U(z,k,w)=\beta_U(z)-\beta_U(w)+k\ell_P.
\tag{22}
\]
The lag kernel is \(k=0\); the clock kernel is exactly the vanishing of the right-hand expression; the joint kernel imposes both. At every point of the basin the source isotropy is \(\mathbb Z\), its clock homomorphism is \(k\mapsto k\ell_P\), and its ENTIRE image is \(H=\ell_P\mathbb Z\). The phase coordinate is
\[
[h-\beta_U(z)]\in\mathbb R/(\ell_P\mathbb Z). \tag{23}
\]
If \(\ell_P=0\), extension isotropy is \(\mathbb Z\), phases are all real numbers and there is no positive primitive. If \(\ell_P=-\log2\), extension isotropy is trivial, and one whole-basin closed height orbit has primitive \(\log2\) and repeats \(j\log2\), \(j\ge1\). The negative step clock has not been replaced: its forward-arrow clock is positive by (8).

Different fixed cores cannot share a source orbit, since their constant forward histories have no common future. Therefore all continuous zero-clock fixed families remain distinct source orbits with their full phases, not deleted null representatives. For M/C, Proposition 3 makes their fixed-core offsets \(\beta=0\). For K/R, (12), (20)–(23) supply their own unrestricted basins and offsets. Coincident M/R core sets do not identify their groupoids; (19) already shows different incoming.

The global kernel of height translation is the intersection \(\bigcap_{z\in Y}H_z\). Each owner contains the actual zero-clock fixed state \((0,0,0)\), whose entire \(H\) is zero by (22). Hence the global height-action kernel is zero for all four owners, even though their zero-clock source isotropy is retained.

## 7. Decisive MAIN duplicate and control limits

MAIN has two distinct source orbits \(\{P_+\}\) and \(\{P_-\}\), each with
\[
I=\mathbb Z,\quad c(k)=-k\log2,\quad H=(\log2)\mathbb Z,\quad
\text{phase }\mathbb R/((\log2)\mathbb Z).
\tag{24}
\]
Their complete primitive length is \(\log2\), not a proper fraction: (24) computes the entire isotropy-clock image. There are exactly two positive packets arising from MAIN's GLOBAL fixed set, with all their repeats. They are not two phases of one packet and cannot be merged by sign, equal length, a memory quotient or choice of representative. Thus the at-most-one-packet-per-prime requirement is REFUTED for the full MAIN owner, regardless of any higher cycles.

| Owner | Complete global fixed set | Own fixed-packet conclusion |
| --- | --- | --- |
| M | \(F_{[0,1)}\cup\{P_+,P_-\}\) | Two distinct primitive \(\log2\) packets; all zero-clock family retained |
| C | \(F_{[0,1)}\) | Zero-clock fixed family; its full positive ledger is empty because \(c\equiv0\) |
| K | \(F_{[-1,2)}\) | Only zero-clock fixed families; higher-cycle positive packets not classified |
| R | Same core set as M | Two own primitive \(\log2\) packets, with different unrestricted incoming |

The positive MAIN cores have active gcd two but equal stored/current digits \(m=n=\pm2\). They do not prove delayed-memory necessity or recurrence in a proper-divisor interface with \(1<D<N\). R reproduces these cores precisely because fixed states satisfy \(m=n\). Content and additive feedback matter to this fixed gate, but that fact is not an endogenous prime-uniqueness mechanism.

No MAIN nonprime primitive is claimed: the positive fixed primitives are prime logarithms. Global prime-only purity and all-prime coverage remain OPEN; the necessary uniqueness condition already fails. The integer-product formula (15) does not turn an arbitrary composite cycle product into repetitions of a prime packet.

## 8. Decision, access and declarations

T0 and the all-point original-measure history obligations are established for each owner. T1 arithmetic prime-packet success is NOT PASSED: MAIN's uniqueness condition is refuted by its own full fixed packets. Complete packet/repetition accounting is not target T2 success. Strong naturalness and PROVES_TOO_MUCH remain OPEN. T3 is NOT AUDITED; classical fields NOT APPLICABLE; formal coordinates UNASSIGNED; Route B NOT INVOKED.

Decision: **STOP / FORK** without changing this owner. All signed states, cells, measures, inverse germs, lags and incoming remain intact. No extra period gate, prime table, roof fitting, operator, density replacement or round475 is introduced.

The sole new scientific input was the [frozen card](candidate-card.md), personally read at lines1–111 through measured EOF, SHA-256 `6dee0423864ea121b7b475c302e1f3dd7fa06f4c9e5c953ab7e53bdc771b0f50`. Root supplied full-CP1 PASS and DISTINCT AUTHOR RELEASE; the CP1 file, reviewer raw, peer proofs and helper proofs were not read. The actual card's C/K/R names govern this paper. No helper was used. All proofs above were derived locally after release.

Design collision reads were [343 card](../343-gcd-square-register-flow/candidate-card.md) lines1–56, non-EOF, prefix SHA-256 `3ae5df72de30ee2e76de282c7a97abe747d7a107b3f82749e953d7f3a0f3ecef`, and [469 card](../469-divisor-normalized-register/candidate-card.md) lines1–51, non-EOF, prefix SHA-256 `eaff5d061194520e1acd08089ded301bfd94379506ddfe9727077957d8f9c78b`. Heading discovery exposed their Outcome titles, not bodies. 343's integer triple evolves independently of its geometric fibre;469 uses a purely real three-coordinate sum-readout permission. This is a mixed delayed-digit feedback definition, not a claimed nonconjugacy or global novelty theorem. No old proof is imported.

The [X summary](../465-gcd-hyperbolic-exchange/batch-summary.md) was read at lines1–68 through EOF, SHA-256 `4bb9ff20fd084a963f1a7eb31832a2ff6350042f22d853fe9736720ecad342a4`; root readme lines1–35 additionally exposed X/W summary outcomes, not their proofs. Prior authorship and shared history are retained. Root and scout had informal inverse/fixed-equation design algebra before freeze; this was not blind or outcome-sealed preregistration. Those exposures are not independent validation.

ARS supplies bounded scoping, proof/evidence separation, drafting and disclosure discipline; the applicable instructions and local template were retained from their complete readings. The frozen card and current release control scope. All new science is exact symbolic derivation and all-integer case analysis, not a numerical experiment. Only paper.md, README.md and claim-ledger.md are author writes; root owns card outcome and integration.

Evidence: [card](candidate-card.md), [claim ledger](claim-ledger.md), [overview](README.md). Reading/check methods are filename/heading `rg`, `nl -ba`, `sed`, `wc -l`, SHA-256 hashing and final text/link/identity checks with full EOF self-reading. No scientific code, web/API, network upload, Git mutation, old-file edit or PDF was used.

Data availability: frozen local definitions and exact proofs, no empirical dataset. Ethics: no human participants, personal data or animal subjects. Contributions: AI agents supplied design, mathematical derivation and drafting; root coordinates separate internal review. Same-model/shared-history work is NOT_CALIBRATED; no human, external or cross-family verification is certified. Funding/conflict information was not supplied and is not invented. No external submission or publication is claimed.
