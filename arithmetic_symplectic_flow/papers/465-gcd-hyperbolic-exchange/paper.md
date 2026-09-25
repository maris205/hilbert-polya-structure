# Active gcd feedback produces a nonprime fixed packet

Candidate ID: `ANG-20260925-GHE01`.
Outcome: OWNED ACTIVE-GCD CLOCK; NONPRIME FIXED PACKET — STOP / FORK

Paper465: `465-gcd-hyperbolic-exchange`; version1, 2026-09-25.
Batch `ADMISSION-CORE-20260925-X`, round1/5, exactly465–469.
Type: measured Borel geometric-history owner (ANG), not a symplectic suspension.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal coordinates UNASSIGNED; Route B NOT INVOKED.
AI-assisted same-model/shared-history work is NOT_CALIBRATED; no human, external or cross-model verification is certified.

## Abstract

We audit the frozen current-gcd hyperbolic exchange on the entire real plane with its original area. Its complete inverse atlas determines a positive finite, every-point IMAGE density on every actual branch, including assigned integer faces. We prove the corresponding full-history cocycle, unrestricted incoming recursion, kernels, source and extension isotropy, and complete phase convention for MAIN and three separately owned controls. In the sole return window \([2,3)^2\), MAIN has exactly one fixed point \(P=(\alpha,\alpha)\), where \(\cosh\alpha=2\alpha\). Its actual gcd is two. The full two-dimensional primitive multiplier is \(\lambda=\alpha^2-1/4\), and exact series inequalities give \(4<\lambda<5\). Its whole source basin therefore owns a positive primitive \(\log\lambda\) that is not the logarithm of any ordinary prime. Content-OFF and cosh-fold-OFF have no fixed points in this window; exchange-OFF reproduces \(P\) and its own multiplier. This MAIN witness stops the universal prime-only target. No other window, higher-period census, density repair or source selection is used.

## 1. Frozen full sources and question

Every owner has \(X=\mathbb R^2\), its usual Borel structure, and original unnormalized Lebesgue area \(\mu=dx\,dy\). At each source define
\[
a=\lfloor x\rfloor,\quad b=\lfloor y\rfloor,\qquad
\gamma(x,y)=\Gamma(a,b)=
\begin{cases}\gcd(|a|,|b|),&(a,b)\ne(0,0),\\1,&(a,b)=(0,0).\end{cases}
\tag{1}
\]
Always \(\gamma\ge1\). MAIN, cosh-fold-OFF, and exchange-OFF read it once per whole step, then recompute it at the actual successor.

| Owner | Actual map | Own legal domain |
| --- | --- | --- |
| M, MAIN | \((\cosh y/\gamma,\cosh x/\gamma)\) | \(xy\ne0\) |
| G, content-OFF | \((\cosh y,\cosh x)\) | \(xy\ne0\), no unused cell labels |
| E, cosh-fold-OFF | \((e^y/\gamma,e^x/\gamma)\) | All \(X\), including both axes |
| S, exchange-OFF | \((\cosh x/\gamma,\cosh y/\gamma)\) | \(xy\ne0\) |

Illegal points remain objects with units and every actual incoming arrow, not absorbing loops. Negative coordinates, zeros, integer cuts and all null points remain. An inverse target need not permit a further forward step. Each owner keeps its own measure, atlas, clock and histories; sharing a formula at a point is not an identification of owners.

For integers \(1<D<N\), the full positive cell \([N,N+1)\times[D,D+1)\) has \(\Gamma(N,D)=D\) exactly when \(D\mid N\). This same readout changes both nonlinear output coordinates. Nondivisor cells execute their own gcd rather than being deleted. Thus the precise lineage is proper-divisor observable \(\to\) current gcd symbol \(\to\) geometric normalization \(\to\) new current readout. This is a designed deformation, not a proof of strong naturalness, Logistic/Hénon conjugacy or symplecticity.

The only return gate is the exhaustive actual fixed set of each owner in
\[
W=[2,3)\times[2,3). \tag{2}
\]
It is not a restricted carrier or a forward-invariant assumption. The necessary target is a nonempty positive ledger with EVERY primitive equal to \(\log p\) for an ordinary prime and at most one full packet per prime; all-prime coverage is additional. A single owned MAIN nonprime witness suffices to refute the universal purity condition.

## 2. Complete actual inverse atlases

Write \(C_{ab}=[a,a+1)\times[b,b+1)\), \(g=\Gamma(a,b)\). For each target \(w=(u,v)\), enumerate all \(a,b\in\mathbb Z\) and, where specified, all independent signs \(\epsilon,\eta\in\{-1,1\}\):
\[
\begin{array}{c|c|c}
U&\theta_\alpha(u,v)&\text{ambient target domain}\\ \hline
M&(\epsilon\operatorname{arcosh}(gv),\eta\operatorname{arcosh}(gu))&gu>1,\ gv>1\\
G&(\epsilon\operatorname{arcosh}v,\eta\operatorname{arcosh}u)&u>1,\ v>1\\
E&(\log(gv),\log(gu))&u>0,\ v>0\\
S&(\epsilon\operatorname{arcosh}(gu),\eta\operatorname{arcosh}(gv))&gu>1,\ gv>1 .
\end{array} \tag{3}
\]
G has no cell indices. Define each actual domain \(\Omega_\alpha^U\) by retaining exactly the ambient targets whose reconstruction lies in the named cell when applicable, satisfies that owner's legal guard, and obeys \(T_U\theta_\alpha^U(w)=w\). These are Borel conditions. Identical actual sources are deduplicated, never genuinely different predecessors or integer lags.

**Proposition 1.** Formula (3), with these checks, lists every actual predecessor of every target for each owner.

**Proof.** On either open half-line, \(\cosh\) is one-to-one onto \((1,\infty)\); its two inverse values are \(\pm\operatorname{arcosh}\). The guards for M/G/S exclude precisely the zero inputs of either coordinate. Applying these scalar inverses in the map's actual coordinate order gives (3). Every legal source supplies its unique floor cell and nonzero coordinate signs, so appears; every retained reconstruction passes the original forward equality and is a genuine source.

For E, \(\exp:\mathbb R\to(0,\infty)\) is bijective. Taking both logarithms in the correct exchanged order gives its displayed inverse and includes zero coordinates whenever the logarithm is zero. The cell check recovers exactly its actual coefficient. No fold guard belongs to E. At a cosh threshold \(gu=1\) or \(gv=1\), a zero reconstructed coordinate would be illegal for that owner; it is not a missing legal branch. The corresponding plane objects are nevertheless retained. Targets outside an ambient domain simply have no predecessor on that branch. \(\square\)

The fixed-cell, fixed-sign formula in (3) is an analytic inverse germ on its indicated open target domain, even when its actual restriction lands on a half-open cell face. The full piecewise map need not be a global continuous local homeomorphism. The assigned germ, not a derivative of the floor function, specifies the all-point version.

## 3. Owned all-point IMAGE and step clocks

**Proposition 2.** Every actual inverse has the prescribed positive finite density
\[
J^{M/S}_{g}(u,v)=
\frac{g^2}{\sqrt{(gu)^2-1}\sqrt{(gv)^2-1}},\qquad
J^G(u,v)=\frac1{\sqrt{u^2-1}\sqrt{v^2-1}},\qquad
J^E_g(u,v)=\frac1{uv}. \tag{4}
\]
For every Borel \(B\subset\Omega_\alpha^U\),
\[
\mu(\theta_\alpha^U B)=\int_BJ_\alpha^U\,d\mu. \tag{5}
\]

**Proof.** The derivative of \(\operatorname{arcosh}(gs)\) is \(g/\sqrt{(gs)^2-1}\). Multiplying the two absolute scalar derivatives, in either exchanged or direct order, gives (4). E has scalar derivatives \(1/v\) and \(1/u\); its coefficient cancels in the inverse derivatives but still defines the source and its actual domain. Strict ambient inequalities make every value positive and finite.

For each fixed \(g\) and each sign quadrant, the ambient scalar product or exchanged product is an analytic diffeomorphism onto its indicated target rectangle. The ordinary two-dimensional change-of-variables formula therefore gives (5) on every Borel subset of that rectangle's actual branch restriction. This includes subsets confined to integer faces: no division by their zero area is made. The assigned analytic expression at every such point fixes the null-point value as part of the frozen owner. \(\square\)

At every legal source, the resulting clocks are
\[
\begin{aligned}
\kappa_M(x,y)=\kappa_S(x,y)
 &=\log\frac{|\sinh x\,\sinh y|}{\gamma(x,y)^2},\\
\kappa_G(x,y)&=\log|\sinh x\,\sinh y|,\\
\kappa_E(x,y)&=x+y-2\log\gamma(x,y).
\end{aligned} \tag{6}
\]
These are \(-\log J_{\rm actual}(T_Uz)\), with signs and zero retained. M and S have equal displayed source functions but distinct transports and hence distinct histories. Terminals have no outgoing step clock. There is no altered density, positive roof, unit-time identification or a.e. replacement.

## 4. Full histories, cocycle and history-pair IMAGE

Fix any one of the four owners for this section. Put \(D_0=X\) and let \(D_r\) be the set of sources permitting all \(r\) steps. Let \(S_0=0\) and \(S_r(z)=\sum_{i=0}^{r-1}\kappa(T^iz)\) on \(D_r\). Retain
\[
\mathcal G=\{(z,r-s,w):r,s\ge0,\ z\in D_r,\ w\in D_s,\
T^rz=T^sw\},\quad c=S_r(z)-S_s(w). \tag{7}
\]
The source is \(w\), range is \(z\), inverse interchanges endpoints and negates lag. Only identical actual triples are identified. The carrier is Borel in \(X\times\mathbb Z\times X\), since it is the countable union of the Borel finite-history equality sets; the atlases make every source and range fibre countable.

If two witnesses have the same endpoints and lag, their iteration pairs differ by a common integer. Advancing the shorter pair to the longer adds the same clock sum at their common future, so cancels in (7). Thus \(c\) descends. To compose two arrows, advance their two witnesses at the shared endpoint to the larger legal iteration depth. Both other endpoints can advance equally through the same future, and the middle clock sums cancel. This proves closure, lag addition and cocycle additivity even with partial domains. No terminal continuation is inserted. In particular
\[
c(Tz,-1,z)=-\kappa(z). \tag{8}
\]

Every finite legal path admits the branch decomposition supplied by (3). On such a path the absolute forward determinant is \(\exp S_r(z)\), by (4)–(6) and the chain rule for its assigned germs. For two path branches \(A,B\), form the actual history-pair map
\[
\psi=(T^r|_A)^{-1}\circ T^s|_B,\qquad w\longmapsto z.
\]
Its Borel domain contains precisely the sources for which both path branches and the common future are actual. Successive change of variables gives
\[
J_\psi(w)=e^{-S_r(z)+S_s(w)}=e^{-c(z,r-s,w)},\qquad
\mu(\psi E)=\int_E e^{-c(\psi w,r-s,w)}\,d\mu(w). \tag{9}
\]
This is an IMAGE identity, not the density in the opposite pushforward direction. Countably many finite branch words cover every arrow. Formula (9) also holds at the prescribed null-point versions by the product of their own assigned germs; the measure identity on null subsets is not used to invent those values.

The extension retains all \((z,h)\in X\times\mathbb R\), with
\[
(w,h)\longmapsto(z,h+c(z,k,w)).
\tag{10}
\]
Height translation acts on its orbit SET. No regular quotient topology, physical Hamiltonian flow, selected section or new roof is asserted.

## 5. All incoming, kernels, isotropy and phases

For each owner independently, define an unrestricted inverse recursion
\[
P_0(t)=\{t\},\qquad
P_{j+1}(t)=
\bigcup_{v\in P_j(t)}\{\theta_\alpha(v):v\in\Omega_\alpha\}. \tag{11}
\]
Proposition 1 and induction give \(P_j(t)=\{z\in D_j:T^jz=t\}\) for EVERY finite \(j\). Therefore the entire incoming set at range \(t\) is
\[
\{(t,r-j,z):t\in D_r,\ j\ge0,\ z\in P_j(T^rt)\}. \tag{12}
\]
Every incoming arrow has exactly such a finite witness, proving coverage; taking inverses gives every outgoing arrow. A terminal allows \(r=0\) but retains all actual \(P_j(t)\). Compatible infinite incoming histories are exactly all sequences \((z_0,z_1,\ldots)\) with \(z_0=t\) and \(Tz_{j+1}=z_j\) legally. Equation (11), without a depth cutoff or a representative selection, supplies all of them.

For a complete kernel description put \(Q_r(z)=e^{S_r(z)}>0\). Among the actual triples (7),
\[
\begin{array}{ll}
\ker(\mathrm{lag}):&r=s,\quad z,w\in P_r(t)\text{ for some }r,t,\\
\ker c:&z\in P_r(t),\ w\in P_s(t),\quad Q_r(z)=Q_s(w),\\
\ker(\mathrm{lag},c):&r=s\text{ and the same product equality}.
\end{array} \tag{13}
\]
These are exact all-source membership tests, including all cells, signs and depths, rather than a finite tree.

The source orbit relation is common legal future. The exact extension-orbit test is that such \(r,s\) exist and \(h_z-h_w=S_r(z)-S_s(w)\). A source \(z\) has nonzero isotropy lag iff its forward orbit eventually enters a legal finite cycle: an equality \(T^rz=T^sz\) with \(r>s\) proves one direction, and advancing around the cycle proves the other. If its eventual cycle has least period \(p\) and own signed cycle sum \(C\), then
\[
I_z=p\mathbb Z,\qquad c(z,jp,z)=jC,\qquad H_z=C\mathbb Z. \tag{14}
\]
Every return lag is divisible by the least period, and all its multiples occur after reaching the core; the transient sums cancel. Otherwise \(I_z=H_z=\{0\}\), including terminating sources. This is a structural characterization, not a new census.

Extension isotropy is \(I_z\cap\ker c\): it is trivial when \(C\ne0\), and all \(p\mathbb Z\) when \(C=0\). Over each full source orbit, choosing any reference point identifies phases with \(\mathbb R/H_z\); the exact test above determines all cross-point offsets. The global height-action kernel is \(\bigcap_{z\in X}H_z\), not the clock group at a selected core. M/G/S have terminal objects with \(H=0\), so that global kernel is zero for them. E retains the same exact intersection test without a further global return classification.

A nonzero \(C\) gives primitive \(|C|\) and all positive integer repeats. A zero \(C\) retains ineffective source isotropy and real phases, but supplies no positive primitive. Each periodic core and all its finite entrants constitute exactly one source orbit: any arrow to the core has a common future on it, while different cycles cannot have a common future. Thus one such core gives one whole positive closed height-translation orbit when \(C\ne0\). Distinct cores are not merged merely because their times agree.

## 6. Exhaustive four-owner fixed gate

Throughout \(W\), the actual floors are \(a=b=2\), so M/E/S have \(g=2\). Every point in \(W\) is legal for all four owners. This identifies the branch on the frozen window only; it does not fix \(g\) globally.

**Lemma 3.** The equation \(\cosh s=2s\) has exactly one solution \(\alpha\) in \([2,3)\), and
\[
\frac{21}{10}<\alpha<\frac94,\qquad
4<\alpha^2-\frac14<5. \tag{15}
\]

**Proof.** For \(h(s)=\cosh s-2s\), \(h'(s)=\sinh s-2>0\) on \([2,3]\): the positive power series gives \(\sinh s\ge s+s^3/6>2\).
Here are exact rational endpoint certificates, not decimal approximations. At \(t=21/10\), write \(A_k=t^{2k}/(2k)!\). Direct rational comparisons give
\[
A_1<\frac{221}{100},\quad A_2<\frac{41}{50},\quad
A_3<\frac3{25},\quad A_4<\frac1{100},\quad
\frac{A_{k+1}}{A_k}
=\frac{441}{100(2k+2)(2k+1)}<\frac1{20}\quad(k\ge4).
\]
Consequently \(\sum_{k\ge4}A_k<1/95<1/50\), and
\[
\cosh(21/10)<1+\frac{221}{100}+\frac{41}{50}+\frac3{25}+\frac1{50}
=\frac{417}{100}<\frac{21}{5}.
\]
At \(t=9/4\), the first three positive terms alone give
\[
\cosh(9/4)>1+\frac{81}{32}+\frac{6561}{6144}
=\frac{28257}{6144}>\frac92.
\]
Continuity and strict monotonicity prove existence, uniqueness and the strict bracket in (15), including the window boundaries. Squaring the positive bracket yields
\[
\alpha^2-\tfrac14>\tfrac{104}{25}>4,\qquad
\alpha^2-\tfrac14<\tfrac{77}{16}<5.
\]
This proves the last assertion. \(\square\)

**Theorem 4.** The entire fixed sets in the frozen window are
\[
\operatorname{Fix}(T_M)\cap W=\operatorname{Fix}(T_S)\cap W
=\{P\},\quad P=(\alpha,\alpha),\qquad
\operatorname{Fix}(T_G)\cap W=\operatorname{Fix}(T_E)\cap W=\varnothing.
\tag{16}
\]

**Proof for MAIN.** The equations are \(2x=\cosh y\), \(2y=\cosh x\). If \(x>y\), strict increase of \(\cosh\) on the positive half-line makes the first right side smaller than the second, contradicting \(2x>2y\). The reverse inequality is likewise impossible. Thus diagonality is proved, not assumed. Lemma 3 gives exactly \(P\). It is internal to \(W\), legal, and has its actual current gcd equal to two.

**Own proof for G.** The same comparison first forces \(x=y=s\). But \(\cosh s\ge1+s^2/2>s\) for \(s\in[2,3)\), since \(1+s^2/2-s=((s-1)^2+1)/2>0\). Hence its own fixed equation has no root in \(W\).

**Own proof for E.** Its equations \(2x=e^y\), \(2y=e^x\) similarly force \(x=y=s\). The positive series gives \(e^s>1+s+s^2/2>2s\) on \([2,3)\), since \(1-s+s^2/2>0\). Thus its own fixed set in \(W\) is empty. No cosh critical guard is imposed on E.

**Own proof for S.** Its two independent fixed equations are \(2x=\cosh x\), \(2y=\cosh y\). Lemma 3 forces both coordinates to be \(\alpha\); there are no additional off-diagonal choices. Its own actual gcd is again two. \(\square\)

## 7. The whole MAIN witness packet and control comparison

At \(P\), both M and S have the OWN step clock
\[
C=\kappa_U(P)=\log\lambda,\qquad
\lambda=\frac{\sinh^2\alpha}{4}
=\alpha^2-\frac14,\qquad 4<\lambda<5. \tag{17}
\]
The hyperbolic identity and \(\cosh\alpha=2\alpha\) give the middle equality. The signed determinant is \(-\lambda\) for M and \(+\lambda\) for S; the clock uses the absolute value of the full two-dimensional determinant, not one eigenvalue, its square root, or a chosen coordinate.

For either owner separately, let
\[
B_U(P)=\bigcup_{N\ge0}P_N^U(P).
\tag{18}
\]
This is its complete full-\(X\) source orbit, not a selected point or a window-restricted basin. Equations (3), (11) enumerate it at every finite depth and retain every compatible infinite ancestry. For \(z\in B_U(P)\), choose any \(N\) with \(U^Nz=P\), and put
\[
\beta_U(z)=S_N^U(z)-NC.
\]
It is independent of that choice, since any further steps are fixed steps with clock \(C\). For any \(z,w\) in this basin, EVERY integer lag \(k\) occurs: choose \(r,s\) sufficiently large with \(r-s=k\), after both endpoints have reached \(P\). Conversely an arrow meeting the basin stays in that same source orbit. Therefore its complete arrow and clock descriptions are
\[
\mathcal G_U|_{B_U(P)}=B_U(P)\times\mathbb Z\times B_U(P),\qquad
c_U(z,k,w)=\beta_U(z)-\beta_U(w)+kC. \tag{19}
\]
Equal actual triples remain identified; no additional free labels are introduced. Its lag kernel is \(k=0\); its clock kernel is the exact equality \(\beta_U(z)-\beta_U(w)+kC=0\); the joint kernel requires both. At every such source \(I_z=\mathbb Z\), the clock map is \(k\mapsto kC\), and the ENTIRE \(H_z=C\mathbb Z\). Extension isotropy is trivial because \(C>0\).

The exact phase coordinate is \([h-\beta_U(z)]\in\mathbb R/(C\mathbb Z)\). Thus this whole basin contributes one closed height-translation orbit with primitive \(C\) and all repeats \(nC\), \(n\ge1\). Extra incoming branches cannot add a fractional lag or shorten \(C\); (19) computes the entire isotropy, not a selected subgroup. The M and S basins and offsets remain separately owned; equality of the core and \(C\) proves no global groupoid equality.

Since no integer, and hence no ordinary prime, lies strictly between four and five, (17) is an owned MAIN positive primitive that is not \(\log p\). This refutes the universal prime-only condition regardless of any other source cycles. It is not an empty-ledger obstruction: the positive packet exists with genuinely active current gcd two.

| Owner | Exhaustive fixed evidence in \(W\) | Its own packet conclusion |
| --- | --- | --- |
| M | Exactly \(P\), actual gcd two | One whole-basin nonprime primitive \(C\) |
| G | Empty | No fixed packet from \(W\); other windows and periods unclassified |
| E | Empty, using its total map | Same bounded limitation, not a global empty-ledger claim |
| S | Exactly \(P\), actual gcd two | Its own whole-basin primitive \(C\); exchange is not needed for this witness |

The controls isolate this scoped mechanism: the MAIN fixed witness is absent in the content-OFF and exponential controls within \(W\), while exchange-OFF reproduces it. The core has equal floor labels \((2,2)\): it witnesses active gcd normalization, not recurrence in a proper-divisor cell with \(N>D\). These controls do not establish that the general formula or measure is naturally forced, nor that all M/S returns agree.

## 8. Decision, limitations and provenance

T0 and the all-point measured-history ownership obligations are established for every frozen owner. The gcd readout actually participates at the MAIN witness, but arithmetic prime-clock T1 is NOT PASSED: universal purity is REFUTED by (17). The full-source packet and repetition convention is proved, not target T2 success. Strong naturalness and PROVES_TOO_MUCH remain explicit OPEN obligations. T3 is NOT AUDITED; classical fields NOT APPLICABLE; formal coordinates UNASSIGNED; Route B NOT INVOKED.

Decision: **STOP / FORK for this unchanged MAIN owner**. No higher-period or outside-window classification is claimed. Global uniqueness per prime and all-prime coverage are not settled separately; they cannot repair the necessary purity failure. The source, original measure, germs, terminal rules and entire histories remain intact. No density adjustment, selected representative, new roof, operator or round470 is introduced.

The sole new scientific input was the [frozen card](candidate-card.md), personally read at lines1–108 through measured EOF, SHA-256 `fc7698d40f559138a7ec6cb49172dcdd28c5af125dc29a2719ca8eb58ca87a25`. Root supplied its CP1 PASS and DISTINCT AUTHOR RELEASE; this author did not read the CP1 file, reviewer raw, peer answers or helper proofs. All proofs above were derived locally after release; no author helper was used. After the draft existed, root reported raw-result agreement without supplying a derivation; no raw text was opened.

During design, the exact old definition reads were [446 card](../446-divisor-cosine-companion/candidate-card.md) lines1–39, non-EOF, prefix SHA-256 `2a1418fa29868855a58cf0a44033a79b81af4a0b493ae9afa966b66917f667f9`, and [456 card](../456-gcd-oblique-fold/candidate-card.md) lines1–44, non-EOF, prefix SHA-256 `0f9ac6ef529d8266d5bfa81165f69eb89b93fc920e54c84159a7103f6178f191`. Heading discovery exposed their appended Outcome titles, not bodies. 446 is a hard-divisor cosine companion;456 is oblique mixing with a one-coordinate bounded rational fold. Those are exact definition differences, not novelty or nonconjugacy theorems, and no old result is imported into this proof.

Prior446/456/460 authorship and shared history remain known. Informal source/inverse feasibility and scalar-return expectations influenced design and window choice, so this was not blind or outcome-sealed preregistration. During governance refresh, root readme lines1–35 exposed preceding batch summaries. During author preparation, papers/README.md lines1–100 additionally exposed historical registry summaries/titles; neither read reached EOF and no linked proof or peer file was opened. These summary exposures are disclosed, not counted as independent scientific validation.

ARS was used for bounded scoping, drafting, evidence discipline and disclosure. Its router, deep-research workflow, runtime policy, architect role, local AGENTS and plan were refreshed in full during design; the academic-paper workflow and draft-writer instructions were refreshed for authorship, including completion of initially truncated instruction reads. The local paper template and relevant writing diagnostics were read. The card, not a generic workflow, fixed scientific and file scope.

Methods: exact symbolic differentiation, change of variables, finite-history arguments and rational power-series inequalities. No numerical search, scientific program, external literature/API, network, Git mutation, old-file edit or PDF was used. Reading/check commands were `rg`, `nl -ba`, `sed`, `wc -l` and SHA-256 hashing; final author verification is full EOF rereading plus text, identity and local-link checks. Only paper.md, README.md and claim-ledger.md are author writes; root owns card outcome and review integration.

Evidence navigation: [card](candidate-card.md), [claim ledger](claim-ledger.md), [overview](README.md). Data availability: the frozen definition, exact proof and access receipts are local; no empirical dataset exists. Ethics: no human participants, personal data or animal subjects. Contributions: AI agents supplied design, mathematical derivation and drafting; root coordinates separate internal review. Same-model/shared-history work is NOT_CALIBRATED and no human/external verification is certified. Funding and conflicts were not supplied and are not invented. No external publication is claimed.
