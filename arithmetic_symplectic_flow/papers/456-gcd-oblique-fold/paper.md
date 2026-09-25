# A prime-2 fixed packet for gcd-oblique folding, with a bounded return audit

Candidate ID: `ANG-20260924-GOF01`.
Outcome: `OWNED FOLD CLOCK; PRIME-2 FIXED PACKET — BOUNDED OPEN / FORK`

Paper: `456-gcd-oblique-fold`; batch `RECURRENCE-OWNER-20260924-V`, round 2/5.
Date: 2026-09-24. Status: exact same-owner proof; global target remains OPEN.
Classical symplectic/suspension fields NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal Route coordinates UNASSIGNED; Route B NOT INVOKED.
AI-assisted, same-model/shared-history work is NOT_CALIBRATED; no human, external, or cross-model verification is certified.

## Abstract

The full real plane with its original area measure carries a current-cell gcd-controlled linear mixing followed by folding of one mixed coordinate. Two separately owned controls remove the gcd dependence or the fold. We prove complete source-checked inverse branches and their prescribed every-point IMAGE densities, including all integer cuts, zero inputs, outer sheets, and terminal incoming histories. Each owner has exactly one global fixed point, the origin, whose entire source orbit is a singleton and whose complete clock image is \((\log2)\mathbb Z\). It therefore gives one actual prime-2 fixed packet in each owner's own height extension. MAIN and the fold-OFF control have no exact-two points with current gcd word \((2,1)\) or \((1,2)\); the gcd-OFF control has no exact-two points anywhere. Full-source kernels, isotropy, phases, and incoming are supplied by exact unrestricted history formulas, not a finite census. This proves nonemptiness but neither prime-only behavior nor global packet uniqueness or all-prime coverage. The same fixed packet in both controls limits its arithmetic significance; it does not transfer credit or failure.

## 1. Frozen full source and arithmetic execution

Every owner has \(X=\mathbb R^2\), its usual Borel structure, and the original, unnormalized area \(\mu=dx\,dy\). At the current point \(z=(x,y)\) set
\[
a=\lfloor x\rfloor,\quad b=\lfloor y\rfloor,\qquad
g=\Gamma(a,b)=
\begin{cases}\gcd(|a|,|b|),&(a,b)\ne(0,0),\\1,&(a,b)=(0,0).\end{cases}
\]
Thus \(g\ge1\). Let
\[
A_g=\begin{pmatrix}1&-g\\g&1\end{pmatrix},\quad
(t,s)=A_g(x,y),\quad f(t)=\frac{t}{1+t^2}.
\]
The three owners, with their own exact source domains, are
\[
\begin{array}{lll}
M:&T_M(x,y)=(f(x-gy),gx+y),&D_M=\{(x-gy)^2\ne1\},\\
G:&T_G(x,y)=(f(x-y),x+y),&D_G=\{(x-y)^2\ne1\},\\
L:&T_L(x,y)=(x-gy,gx+y),&D_L=X.
\end{array} \tag{1}
\]
MAIN reads its gcd once for both output coordinates; the next step reads the actual new coordinates. G has no redundant integer-cell labels. L keeps the actual gcd readout but not the removed fold's guard. All formulas give finite real outputs on their stated domains, since \(1+t^2>0\). All signs, axes, units, the origin, integer cuts, and null points remain in \(X\). A failed source is a terminal object with a unit and every actual incoming arrow, not an absorbing loop. Targets do not need to permit another step. No point at infinity is added.

For positive integer cells \([N,N+1)\times[D,D+1)\), with integers \(1<D<N\), the readout satisfies \(\Gamma(N,D)=D\) exactly when \(D\mid N\). This follows from the defining greatest-common-divisor property in both directions. The prior-work arrow is proper-divisor admissibility \(\to\) current gcd readout \(\to\) actual oblique mixing \(\to\) one-coordinate nonlinear folding \(\to\) rereading of the successor. Nondivisor states also execute their actual gcd rule. This is a geometric deformation of divisor-symbolic data, not a prime-selected subsystem, passive integer register, or inserted prime roof.

The frozen gate consists of the global fixed sets of all three owners, MAIN/L's entire exact-two sets with gcd words \((2,1)\) and \((1,2)\), and G's global exact-two set. Other gcd words and longer periods are not enumerated or classified.

## 2. Complete actual inverse branches

Put
\[
B_-=(-\infty,-1),\quad B_0=(-1,1),\quad B_+=(1,\infty),
\qquad
U_-=(-\tfrac12,0),\ U_0=(-\tfrac12,\tfrac12),\ U_+=(0,\tfrac12).
\]
The function \(f\) maps each \(B_j\) analytically and bijectively onto \(U_j\). Indeed
\[
f'(t)=\frac{1-t^2}{(1+t^2)^2}, \tag{2}
\]
which is positive on \(B_0\) and negative on each outer interval; endpoint limits give the displayed images. The complete inverse roots can be written
\[
\rho_0(u)=\frac{2u}{1+\sqrt{1-4u^2}}\quad(u\in U_0),\qquad
\rho_\pm(u)=\frac{1+\sqrt{1-4u^2}}{2u}\quad(u\in U_\pm). \tag{3}
\]
In particular \(\rho_0(0)=0\), without a \(0/0\) choice. For \(u\ne0\) these are precisely the appropriate roots of \(u\tau^2-\tau+u=0\). At \(u=0\), the polynomial is \(-\tau=0\), so its only finite root is zero. At \(|u|=1/2\), its only root is forbidden \(\tau=\pm1\); for \(|u|>1/2\), there is no real root. The unbounded outer root has no extra value at \(u=0\).

For MAIN let \(C_{ab}=[a,a+1)\times[b,b+1)\), \(a,b\in\mathbb Z\), and \(g=\Gamma(a,b)\). For each \(j\in\{-,0,+\}\) define
\[
\theta^M_{abj}(u,v)=
\left(\frac{\rho_j(u)+gv}{1+g^2},
      \frac{v-g\rho_j(u)}{1+g^2}\right),\qquad
\Omega^M_{abj}=\{(u,v)\in U_j\times\mathbb R:\theta^M_{abj}(u,v)\in C_{ab}\}. \tag{4}
\]
For G use the same displayed formula with \(g=1\), no cell labels or cell restriction, and \(\Omega^G_j=U_j\times\mathbb R\). For L use
\[
\theta^L_{ab}(u,v)=
\left(\frac{u+gv}{1+g^2},\frac{v-gu}{1+g^2}\right),\qquad
\Omega^L_{ab}=\{w\in X:\theta^L_{ab}(w)\in C_{ab}\}. \tag{5}
\]
There is no fold-sheet or critical guard in (5).

**Proposition 1 (all inverse ownership).** Equations (4)–(5), and G's own branches, are exactly the actual inverse branches of (1), including every integer cut and every terminal target that has incoming. Their domains are Borel. No labels or root signs are missing.

**Proof.** The determinant of \(A_g\) is \(1+g^2>0\), and its displayed inverse gives (4)–(5). A true MAIN preimage has a unique actual cell, a unique mixed \(t\) in one \(B_j\), and \(u=f(t)\); (3) recovers precisely that \(t\), after which \(A_g^{-1}\) recovers the source. Conversely every point of (4) reconstructs the correct cell and therefore the correct actual \(g\); its mixed coordinate is \(\rho_j(u)\ne\pm1\), and substitution gives the target. G has the same two identities with fixed \(g=1\) and no cell test. For L the two identities are just \(A_g^{-1}A_g=\mathrm{id}\) and \(A_gA_g^{-1}=\mathrm{id}\), followed by its own source-cell check. Analytic root functions and Borel cells make every actual domain Borel. Overlapping formal presentations are deduplicated only when they give the same actual source. Different reconstructed sources remain different incoming arrows. \(\square\)

## 3. Original-area IMAGE and every-point clock

On a fixed MAIN cell the smooth ambient formula has derivative determinant \((1+g^2)f'(t)\); its zeros are exactly the frozen excluded mixed lines \(t=\pm1\). The same statement with \(g=1\) applies to G. On each open strip \(A_g^{-1}(B_j\times\mathbb R)\), the fixed-\(g\) folded map is an analytic diffeomorphism onto \(U_j\times\mathbb R\). Restricting its inverse to the actual Borel cell domain gives the prescribed germ, even at a cut.

Its absolute inverse determinant is, at every actual target,
\[
J^M_{abj}(u,v)=
\frac{(1+\rho_j(u)^2)^2}{(1+g^2)|1-\rho_j(u)^2|},
\qquad
J^G_j(u,v)=
\frac{(1+\rho_j(u)^2)^2}{2|1-\rho_j(u)^2|},\qquad
J^L_{ab}=\frac1{1+g^2}. \tag{6}
\]
All these values are finite and strictly positive on their own domains. In particular the central \(u=0\) value comes from its actual analytic germ, not a freely chosen null-point completion.

The change-of-variables identity on each ambient analytic or linear diffeomorphism proves, for every Borel \(E\) in its actual restricted domain,
\[
\mu(\theta E)=\int_E J_\theta\,d\mu. \tag{7}
\]
This remains valid for null subsets and integer-face subsets; the identity uses an integral, not a ratio of two set masses. Infinite Borel sets are allowed, with nonnegative integrals possibly infinite. Borel images follow from the ambient homeomorphism. No continuity of the whole piecewise map across a floor cut is asserted.

Thus each owner independently admits the frozen all-point version and has legal-source clock
\[
\begin{aligned}
\kappa_M(x,y)&=\log\frac{(1+g^2)|1-(x-gy)^2|}{(1+(x-gy)^2)^2},\\
\kappa_G(x,y)&=\log\frac{2|1-(x-y)^2|}{(1+(x-y)^2)^2},\\
\kappa_L(x,y)&=\log(1+g^2).
\end{aligned} \tag{8}
\]
These are \(-\log J_{\rm actual}(Tz)\) in the prescribed IMAGE orientation. Signed and zero values remain; no clock is assigned to a terminal's nonexistent next step. No density or time from a different owner is used.

## 4. Full histories, kernels, isotropy, incoming, and phases

For each owner separately, \(T^0=\mathrm{id}_X\), and \(T^m z\) exists only when all \(m\) steps are legal. Write
\[
S_m(z)=\sum_{i=0}^{m-1}\kappa(T^iz),\quad S_0=0,\qquad W_m(z)=\exp S_m(z)>0.
\]
The quantities \(W_m\) are finite products of the absolute forward determinants in (8), with \(W_0=1\). No infinite product or terminal padding is taken. Retain
\[
\mathcal G=\{(z,m-n,w):m,n\ge0,\ T^mz=T^nw\text{ legally}\},\quad
c(z,m-n,w)=S_m(z)-S_n(w), \tag{9}
\]
with source \(w\), range \(z\), equal triples identified, and integer lag retained.

**Proposition 2 (actual measured history).** These are Borel groupoids, and \(c\) is a well-defined additive real cocycle. The forward arrow \((Tz,-1,z)\) has clock \(-\kappa(z)\).

**Proof.** The domains and maps of finite iterates are Borel by induction, so the actual-triple set is a countable union of Borel equality sets in \(X\times\mathbb Z\times X\). Inversion swaps endpoints and changes the lag sign; units are \((z,0,z)\). Given \(T^mz=T^nw\) and \(T^pw=T^qv\), if \(p\ge n\) continue the first meeting along the already legal additional \(p-n\) steps of \(w\), obtaining \(T^{m+p-n}z=T^qv\); if \(p<n\), continue the second meeting for the already legal \(n-p\) steps instead. This proves closure with added lag without adding any terminal steps.

Two witnesses for the same triple have the same lag, hence differ by equal shifts in their two depths. The later witness adds precisely the same clock sum at their common future point, which cancels. Thus (9) descends. The same common-future alignment in a product gives additivity, since, for example, \(S_{m+p-n}(z)=S_m(z)+S_p(w)-S_n(w)\) when \(p\ge n\). The forward sign follows directly using depths \(0,1\). \(\square\)

On each specified finite-history branch, the actual endpoint transformation is an own inverse iterate composed with an own forward iterate. From (7) and the determinant chain rule its forward IMAGE density is \(W_n(w)/W_m(z)=\exp(-c(z,m-n,w))\). The identity holds on every Borel subset of its actual domain, with the fixed-label/sheet germ at every point. Proposition 2 ensures agreement of these values for different witnesses of the same actual triple.

Here are exact formulas retaining every incoming label and depth. Let \(P_0(t)=\{t\}\), and use all own branches in (4)–(5) to set
\[
P_{j+1}(t)=\bigcup_{v\in P_j(t)}\{\theta_\alpha(v):v\in\Omega_\alpha\}. \tag{10}
\]
Induction using Proposition 1 gives \(P_j(t)=\{z:T^jz=t\text{ legally}\}\). The full set of arrows incoming to \(t\) is
\[
\{(t,r-j,z):r\ge0,\ T^rt\text{ legal},\ j\ge0,\ z\in P_j(T^rt)\}. \tag{11}
\]
Inverting (11) gives all outgoing arrows and its endpoints give the full source orbit. Terminal incoming is included by \(r=0\). Neither (10) nor (11) is a finite census or a selection of basin representatives.

The complete lag, clock, and joint kernels are
\[
\begin{aligned}
K_\ell&=\bigcup_{j,t}\{(z,0,w):z,w\in P_j(t)\},\\
K_c&=\bigcup_{m,n,t}\{(z,m-n,w):z\in P_m(t),\ w\in P_n(t),\quad
 W_m(z)=W_n(w)\},\\
K_{\ell,c}&=\bigcup_{j,t}\{(z,0,w):z,w\in P_j(t),\quad
 W_j(z)=W_j(w)\}.
\end{aligned} \tag{12}
\]
Here all depths are nonnegative integers and \(t\) ranges over the whole \(X\). These formulas are fully specified by (4)–(5), (8), and (10); they do not replace an unknown density by zero.

For completeness the entire source-isotropy and clock-image formulas are also exact. If \(z\) is not eventually periodic along legal iterates, including any terminating source, then \(I(z)=\{k:(z,k,z)\in\mathcal G\}=\{0\}\) and \(H(z)=\{0\}\). Otherwise let \(p\) be the least period of its eventual cycle \(a_0,\ldots,a_{p-1}\), and put
\[
B=\sum_{i=0}^{p-1}\kappa(a_i)=\log\prod_{i=0}^{p-1}\exp\kappa(a_i).
\]
Then
\[
I(z)=p\mathbb Z,\qquad c(z,jp,z)=jB,\qquad H(z)=B\mathbb Z. \tag{13}
\]
Indeed any equality of unequal iterates produces an actual eventual cycle. On a cycle, two iterates coincide exactly at depth differences divisible by its least period; all such differences occur after entry. Common initial and terminal segments cancel from clock sums, leaving precisely \(jB\). Cyclically shifting the cycle does not change its sum. This proves (13), not a classification or enumeration of which other eventual cycles exist.

The extension is the full \(X\times\mathbb R\) with arrows \((w,h)\to(z,h+c(z,k,w))\). At \((z,h)\) its isotropy is \(I(z)\cap\ker c\): it is trivial for a non-eventually-periodic source or when \(B\ne0\), and is the entire \(p\mathbb Z\) when \(B=0\). For any full source orbit, choose an anchor solely to describe phases; clock values of two arrows from that anchor to a given point differ exactly by \(H\). Hence all extension orbits over the source orbit are parametrized by \(\mathbb R/H\), with height translation induced by addition and stabilizer exactly \(H\). This describes an orbit set, not a chosen source subsystem, a Hausdorff quotient, or a borrowed physical section.

When \(B\ne0\), the actual primitive time is \(|B|\), with all positive integer repeats. When \(B=0\) or there is no eventual cycle, there is no positive primitive, and every real phase and all zero-clock isotropy remain. Distinct source orbits with the same nonzero \(|B|\) remain distinct packets. These unrestricted statements apply to all three owners, including unexamined cycles; only the frozen return sets below receive an explicit census.

## 5. All global fixed points and their complete prime-2 packets

**Proposition 3.** Each of \(M,G,L\) has the global fixed set \(\{o\}\), \(o=(0,0)\). Its full source orbit is exactly \(\{o\}\), with no additional incoming at any depth. In each owner's own extension this gives one actual primitive packet of length \(\log2\).

**Proof.** For MAIN, the second coordinate of a fixed point requires \(gx+y=y\). Since \(g\ge1\), \(x=0\). The first coordinate then requires \(f(-gy)=0\), so \(y=0\). The same proof for G uses \(g=1\). For L its first coordinate after \(x=0\) is \(-gy=0\), again forcing \(y=0\). At \(o\), the actual cell is \(C_{00}\), \(g=1\), and the mixed coordinate is zero. Thus \(o\) is legal and fixed for all three owners.

For target \(o\), the fold inverse polynomial has only \(\tau=0\). Every proposed MAIN or G preimage therefore equals \(o\); MAIN's actual label is uniquely \(C_{00}\). Every L fixed-label inverse of \(o\) also equals \(o\), and only \(C_{00}\) passes the source check. Induction in (10) yields \(P_j(o)=\{o\}\) for every depth. With the forward fixed point, (11) proves that its whole source orbit is the singleton, not a selected center of a larger basin.

Equations (6)–(8), evaluated in each own owner, give \(J(o)=1/2\) and \(\kappa(o)=\log2\). The full isotropy group is \(\mathbb Z\), its clock map is \(k\mapsto k\log2\), and \(H(o)=(\log2)\mathbb Z\). The extension isotropy at each \((o,h)\) is trivial, and its full phase set is \(\mathbb R/(\log2)\mathbb Z\). Translation has least positive period \(\log2\), with all positive integer repetitions. The forward arrow has clock \(-\log2\); this sign does not change the entire period group. Thus the primitive is derived from the original measure, not inserted. \(\square\)

The result is global uniqueness of the fixed source point and of its associated fixed packet, not global uniqueness of all positive packets or of every possible packet of length \(\log2\).

## 6. Complete frozen exact-two tests

### 6.1 MAIN: the words \((2,1)\) and \((1,2)\)

Suppose an actual two-step return starts with current gcd \(2\), then \(1\). Write \(z=(x,y)\), \(T_Mz=(u,v)\). The two second-coordinate equations imply
\[
v=2x+y,\qquad y=u+v,\qquad u=-2x. \tag{14}
\]
The first equations are \(u=f(x-2y)\) and \(x=f(u-v)\). The function \(f\) has the sign of its argument and vanishes only at zero.
If \(x>0\), then \(u<0\), so \(x-2y<0\), whence \(y>x/2>0\) and \(v>0\). Thus \(u-v<0\), contradicting \(x=f(u-v)>0\). If \(x<0\), then \(u>0\); hence \(y<x/2<0\), \(v<0\), and \(u-v>0\), contradicting the returned negative \(x\). Finally \(x=0\) forces \(u=0\) and \(f(-2y)=0\), hence \(y=0\). But the actual origin gcd is \(1\), not \(2\).

Therefore no legal two-step return with word \((2,1)\) exists, in any integer cells or at any cut. A legal exact-two point with word \((1,2)\), shifted to its other actual point, would give a legal return with word \((2,1)\). Both specified exact-two sets are empty. This is not a conclusion about MAIN's other words or longer periods.

### 6.2 Fold-OFF L: the same two words

For a legal word \((2,1)\), the two-step formula is \(A_1A_2z\), and
\[
A_1A_2-I=
\begin{pmatrix}-2&-3\\3&-2\end{pmatrix},\qquad
\det(A_1A_2-I)=13.
\]
The only solution of \(T_L^2z=z\) with these displayed coefficients is therefore \(z=0\), whose actual gcd fails the starting value \(2\). Thus this word has no return after the necessary readout check. Cyclic shifting excludes \((1,2)\) as well. No MAIN fold or terminal guard has been imposed on this total control.

### 6.3 G: its global two-step-return set

Let \(t=x-y\), and suppose both G steps are legal and \(T_G^2(x,y)=(x,y)\). With \(T_G(x,y)=(u,v)\), the second return equation gives \(u+v=y\), so \(u=-x\), \(x=-f(t)\). The second folded argument is
\[
t'=u-v=-2x-y=t-3x=t+3f(t)
   =t\,\frac{t^2+4}{t^2+1}.
\]
The first return equation would require \(f(t')=x=-f(t)\). If \(t\ne0\), then \(t'\), \(f(t')\), and \(f(t)\) have the same nonzero sign, a contradiction. Thus \(t=0\), \(x=0\), and \(y=0\). The origin is indeed legal for both steps, but is already fixed. Consequently \(\operatorname{Fix}(T_G^2)=\{o\}\) and G's global exact-two set is empty.

No core is counted twice through cyclic starting points. In particular the two-step return at the origin is a repetition of the fixed packet, not an exact-two core.

## 7. Decision, controls, and remaining limits

| Owner | Global fixed set and entire fixed-packet clock | Frozen exact-two result | Outside this return audit |
| --- | --- | --- | --- |
| MAIN | Only \(o\); singleton full source orbit; \(H=(\log2)\mathbb Z\) | Both gcd words \((2,1),(1,2)\) empty | Other words and all higher periods OPEN |
| G, gcd-OFF | Only \(o\); its own \(H=(\log2)\mathbb Z\) | Global exact-two set empty | Periods above two OPEN |
| L, fold-OFF | Only \(o\); its own \(H=(\log2)\mathbb Z\) | Both specified words empty, without fold guard | Other words and higher periods not classified |

The original-area full-point IMAGE, actual history owner, and all-state structural ledger are established. MAIN's required nonempty positive ledger is established by a complete, unselected packet. However the “every positive primitive is an ordinary-prime logarithm,” global uniqueness per prime, and all-prime coverage requirements remain OPEN. The generic full-source formulas (9)–(13) are not a proof that the exhibited packet exhausts the source.

Both controls independently reproduce the same fixed packet. This proves that the fixed-point witness does not discriminate the current-gcd mechanism or nonlinear folding from their removals. It is a PROVES_TOO_MUCH concern, not transferred MAIN failure and not a substitute proof of arithmetic naturalness. Strong naturalness of the readout, formula, and area law remains OPEN; arithmetic T1 is NOT PASSED. T2's actual fixed-packet/repetition accounting is proved within the stated audit, not the global prime-packet target.

Decision: **BOUNDED OPEN / FORK** under the frozen stop rule. There is no expanded cycle census, parameter or measure repair, new source selection, or additional candidate in this paper. Classical symplectic/suspension fields are NOT APPLICABLE, T3 is NOT AUDITED, formal Route coordinates are UNASSIGNED, and Route B is NOT INVOKED. No operator, trace, zeta, zero-matching or physical Hamiltonian realization is supplied.

## 8. Provenance, reproducibility, and declarations

The sole new scientific input was the [frozen card](candidate-card.md), read personally at original lines 1–86 through its provided and measured EOF. The original-prefix SHA-256 is `84ee5f19a6910b63bff4e401f17c03fc9a667bbdc843c52bc951a16352152e46`. Root released author mathematics after its full CP1 read. No CP1 report, reviewer raw proof, answer, other current manuscript, or later outcome was read by this author.

The design-stage definition reads were [430](../430-euclidean-complex-degree/candidate-card.md), lines 1–52, non-EOF, measured total 117, prefix SHA-256 `b3b57d032ff79284e2be15868962f68fd77d3aaf6d311ba2e9ed742ae4535791`; and [442](../442-divisor-radial-compression/candidate-card.md), lines 1–53, non-EOF, measured total 118, prefix SHA-256 `7e8fa6c675b3c7e689974c8cd89e0dad8ac13e1c72102bdcb800e46932991df2`. Heading metadata also exposed Outcome titles 269:124, 425:95, 333:172, 430:102, 442:106, not outcome bodies. Other scouting access was filename-only location. The read prefixes included definitions and proposed IMAGE/history obligations, not their appended scientific outcomes.

430 uses content/remainder-controlled complex squaring; its degree-OFF linear mixing is shared ancestry, not a new device claimed here. 442 folds both coordinates by a radial denominator, whereas this source folds one obliquely mixed coordinate. These are distinctions between displayed definitions, not a global novelty or nonconjugacy theorem. This author previously authored 430 and retains shared historical exposure; no old proof was reread or imported. Informal inverse/control feasibility informed design, so it was not blind or sealed.

A bounded same-model author helper, `gof_g_author_aid`, read only the original 456 card lines 1–86 and returned G's own inverse/IMAGE and global fixed/two-step derivation. That is disclosed author assistance, not an independent reviewer seat. MAIN/L and the common full-source history proof were authored locally. ARS's academic-paper discipline was used for scope, evidence, limitations, and explicit AI-assistance reporting; it did not authorize a literature campaign.

The paper consists of exact symbolic proofs; no scientific program, numerical orbit search, external lookup, network/API call, Git operation, or PDF was used. Input receipts used `nl -ba .../candidate-card.md`, `wc -l`, and `head -n 86 .../candidate-card.md | sha256sum`. Author verification uses full EOF rereads of these three author surfaces and mechanical identity, link, control-character, delimiter and hash checks only. The source outside the frozen return window is retained through (9)–(13), not silently declared classified. No topology for the height orbit-set quotient is assumed.

Evidence index: [card](candidate-card.md), [claim ledger](claim-ledger.md), [overview](README.md). Root owns append-only card outcome, separate internal review integration, and batch records. No round 460 is opened here.

Data availability: no empirical dataset; complete frozen definitions, analytic proofs and local provenance are supplied. Ethics: no human participants, personal data or animal subjects. Contributions: AI agents supplied design assistance, mathematical derivation, drafting and a bounded G-control author check; root coordinates separate internal review and integration. AI assistance is explicit; no human/external verification is certified, and same-model/shared-history review remains NOT_CALIBRATED. Funding and conflicts: declarations were not supplied and are not invented. No external submission or publication is claimed.
