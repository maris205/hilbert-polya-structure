# All periodic cores of GOF01 switch off the nontrivial gcd feedback

Candidate ID: `ANG-AUDIT-20260924-GRF01`.
Underlying unchanged owner: `ANG-20260924-GOF01` (456).
Outcome: `GLOBAL GCD-1 CORE EQUIVALENCE — PRIME TARGET OPEN / FORK`

Paper: `460-gcd-recurrent-feedback`; batch `RECURRENCE-ADMISSION-20260924-W`, round 1/5.
Date: 2026-09-24. Status: exact global periodic-core audit, not a modified candidate.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal Route coordinates UNASSIGNED; Route B NOT INVOKED.
AI-assisted same-model/shared-history work: NOT_CALIBRATED; no certified human, external, or cross-model verification.

## Abstract

This audit leaves the entire source, original area, maps, terminal convention, inverse germs, and IMAGE clocks of GOF01 unchanged. We prove that every legal MAIN periodic orbit, of arbitrary period, lies strictly in \((-1/2,1/2)\times(-1,1)\). An independent argument proves the same bound for the arithmetic-OFF control. The original floor-gcd observable is identically one throughout both periodic sets. Consequently MAIN and arithmetic-OFF have exactly the same periodic points, least periods, cycle step clocks, entire isotropy-clock groups, and closed-packet multiplicities. Their complete basins and full groupoids are not identified. The total fold-OFF control has only the origin as a periodic point. Thus nontrivial gcd feedback affects no finite periodic core in this owner, strengthening the earlier fixed-point control concern to all periods without classifying the remaining cycles. The known prime-2 packet is retained, but prime-only lengths, global uniqueness per prime, and all-prime coverage remain OPEN.

## 1. Unchanged full owners and exact question

Every owner has \(X=\mathbb R^2\), the usual Borel structure and original unnormalized area \(\mu=dx\,dy\). Define
\[
a=\lfloor x\rfloor,\quad b=\lfloor y\rfloor,\qquad
\gamma(x,y)=\Gamma(a,b)=
\begin{cases}
\gcd(|a|,|b|),&(a,b)\ne(0,0),\\
1,&(a,b)=(0,0).
\end{cases}
\]
Thus \(\gamma\ge1\), including axes and the zero cell. With \(f(t)=t/(1+t^2)\), retain separately
\[
\begin{array}{lll}
M:&T_M(x,y)=(f(x-\gamma y),\gamma x+y),&
D_M=\{(x-\gamma y)^2\ne1\},\\
G:&T_G(x,y)=(f(x-y),x+y),&
D_G=\{(x-y)^2\ne1\},\\
L:&T_L(x,y)=(x-\gamma y,\gamma x+y),&D_L=X.
\end{array} \tag{1}
\]
MAIN reads \(\gamma\) once per whole step and then rereads the actual successor. G uses the constant coefficient one; its \(\gamma(x,y)\) below is only a read-only observable. L does not inherit a fold guard. All signs, cell faces, units, null points and terminal objects remain. A terminal has a unit and every actual incoming arrow, not an artificial next step. Targets need not admit further motion.

For each own map let
\[
\operatorname{Per}(U)=\bigcup_{p\ge1}
\{z:U^pz=z,\text{ all }p\text{ steps legal}\},\qquad
A_{\rm act}=\{z\in X:\gamma(z)>1\}. \tag{2}
\]
The new question is whether \(\operatorname{Per}(U)\cap A_{\rm act}\) is empty, separately for \(U=M,G,L\). Here “recurrent core” means an actual finite periodic core, not all topologically recurrent or nonwandering points. There is no period cutoff, bounded source selection, changed clock or new roof.

The lineage remains the exact proper-divisor interface \(\Gamma(N,D)=D\) iff \(D\mid N\), for integers \(1<D<N\), executed on their full positive cells through oblique mixing and folding. This audit asks whether that nontrivial feedback reaches any periodic core; it does not redefine the symbolic source.

## 2. Retained measured-history contract

The following are owned dependencies proved in [456, §§1–4](../456-gcd-oblique-fold/paper.md), not new theorems credited to 460. They are stated explicitly so the present global argument and packet comparison can be replayed.

For all cells \(C_{ab}=[a,a+1)\times[b,b+1)\) and their actual \(g=\Gamma(a,b)\), the MAIN inverse candidates at \(w=(u,v)\) are all finite real roots \(\tau\) of
\[
u\tau^2-\tau+u=0,\qquad
\theta_{g,\tau}(u,v)=
\left(\frac{\tau+gv}{1+g^2},\frac{v-g\tau}{1+g^2}\right). \tag{3}
\]
Retain exactly the roots in the own sheets \((-\infty,-1),(-1,1),(1,\infty)\), with reconstructed source in \(C_{ab}\), its own readout and forward equality. G uses \(g=1\) without cell labels. At \(u=0\), (3) gives only \(\tau=0\); no outer root at infinity is added. L uses the displayed linear inverse with \(\tau=u\), all actual cell tests, and no fold-sheet guard.

These give every actual inverse on Borel domains. The central sheet has target first coordinate \((-1/2,1/2)\); the outer sheets have \((-1/2,0)\) and \((0,1/2)\). Their assigned analytic inverse germs, including floor cuts, have
\[
J^{M/G}_{g,\tau}
=\frac{(1+\tau^2)^2}{(1+g^2)|1-\tau^2|},\qquad
J^L_g=\frac1{1+g^2}, \tag{4}
\]
where G uses only \(g=1\). They are positive finite at every actual point and satisfy \(\mu(\theta E)=\int_EJ_\theta\,d\mu\) for every Borel subset of the actual inverse domain. This is the original-area integral identity, not a ratio of set masses or an a.e. replacement.

The corresponding legal-source clocks are
\[
\kappa_M(z)=\log\frac{(1+\gamma(z)^2)|1-(x-\gamma(z)y)^2|}
 {(1+(x-\gamma(z)y)^2)^2},\quad
\kappa_G(z)=\log\frac{2|1-(x-y)^2|}{(1+(x-y)^2)^2},\quad
\kappa_L(z)=\log(1+\gamma(z)^2). \tag{5}
\]
They are independently \(-\log J_{\rm actual}(Uz)\); terminals have no outgoing summand. No proof below changes (4) or (5).

For each own map retain all legal histories
\[
\mathcal G_U=\{(z,m-n,w):U^mz=U^nw,\ m,n\ge0\},\quad
c_U(z,m-n,w)=S_m^U(z)-S_n^U(w), \tag{6}
\]
where \(S_0=0\), \(S_m\) is the finite own step sum, source is \(w\), range is \(z\), and only equal actual triples are identified. The cocycle descends and adds; the forward arrow \((Uz,-1,z)\) has clock \(-\kappa_U(z)\). The extension is all \(X\times\mathbb R\), with \((w,h)\to(z,h+c_U)\), and height translation acts on its orbit set.

For each owner separately let \(P_0^U(t)=\{t\}\) and
\[
P_{j+1}^U(t)=
\bigcup_{v\in P_j^U(t)}\{\theta_\alpha^U(v):v\in\Omega_\alpha^U\}. \tag{7}
\]
Every actual cell and sheet is included. Then \(P_j^U(t)=\{z:U^jz=t\text{ legally}\}\), and all arrows incoming to \(t\) are
\[
\{(t,r-j,z):U^rt\text{ legal},\ j\ge0,\ z\in P_j^U(U^rt)\}. \tag{8}
\]
All finite depths occur, including at terminals; taking inverses gives all outgoing arrows. No finite enumeration of (7)–(8) is implied.

To retain the complete kernels, put \(W_m^U=\exp S_m^U\). Within actual triples, the lag kernel consists exactly of \((z,0,w)\) with \(z,w\in P_j^U(t)\) for some \(j,t\). The clock kernel consists exactly of witnesses \(z\in P_m^U(t)\), \(w\in P_n^U(t)\) with \(W_m^U(z)=W_n^U(w)\); the joint kernel imposes both this equality and \(m=n\). These remain each owner's own sets, not kernels transplanted from a common periodic subspace.

The source isotropy is trivial for a non-eventually-periodic source, including every terminating source. If the eventual core has least period \(p\) and own signed cycle sum \(C_U\), then
\[
I_U(z)=p\mathbb Z,\quad c_U(z,jp,z)=jC_U,\quad
H_U(z)=C_U\mathbb Z. \tag{9}
\]
The extension isotropy is the zero-clock part: trivial for \(C_U\ne0\), all \(p\mathbb Z\) for \(C_U=0\). Over an own source orbit its phase set is \(\mathbb R/H_U\). A nonzero \(C_U\) gives primitive \(|C_U|\) and all positive integer repeats; a zero \(C_U\) does not give a positive primitive but retains the entire ineffective isotropy and real phases. These are structural formulas, not an enumeration of cycles.

## 3. Uniform periodic bounds for MAIN

**Theorem 1.** Every legal MAIN periodic point belongs to
\[
\mathcal B=(-\tfrac12,\tfrac12)\times(-1,1). \tag{10}
\]
Consequently \(\operatorname{Per}(M)\cap A_{\rm act}=\varnothing\).

**Proof.** Take an arbitrary actual periodic orbit of any period \(p\ge1\), with indices read modulo \(p\):
\[
x_{i+1}=f(x_i-g_i y_i),\qquad
y_{i+1}=y_i+g_i x_i,\qquad g_i=\gamma(x_i,y_i)\ge1.
\]
For every real \(t\), \(2|t|\le1+t^2\), with equality only when \(|t|=1\). Each orbit point is the image of a legal predecessor, which excludes these equality inputs. Therefore
\[
-\tfrac12<x_i<\tfrac12\quad\text{for every }i. \tag{11}
\]
In particular a negative \(x_i\) has floor \(-1\) and hence \(g_i=1\). If \(g_i\ge2\), then \(x_i\ge0\) and \(\lfloor x_i\rfloor=0\).

First choose \(j\) with \(y_j\) minimal. Write
\[
X=x_{j-2},\quad Y=y_{j-2},\quad a=g_{j-2},\quad
t=X-aY,\quad b=g_{j-1}.
\]
Then \(x_{j-1}=f(t)\), \(y_{j-1}=Y+aX\), and
\[
y_j=Y+aX+b f(t).
\]
Minimality gives \(b f(t)=y_j-y_{j-1}\le0\). Since \(b>0\) and \(f\) preserves sign, \(t\le0\). If \(f(t)<0\), (11) gives \(b=1\); if \(f(t)=0\), the term \(b f(t)\) is zero regardless of \(b\). Thus in either case
\[
y_j=Y+aX+f(t). \tag{12}
\]
If \(a=1\), substitute \(Y=X-t\) to obtain
\[
y_j=2X-t+f(t)=2X-\frac{t^3}{1+t^2}\ge2X>-1. \tag{13}
\]
If \(a\ge2\), then \(X\ge0\). From \(t=X-aY\le0\), we have \(Y\ge X/a\ge0\). The actual readout \(a=\Gamma(0,\lfloor Y\rfloor)\ge2\) then requires \(\lfloor Y\rfloor\ge2\), hence \(Y\ge2\). Equation (12), \(aX\ge0\), and \(f(t)>-1/2\) yield \(y_j>3/2\), which in particular also gives \(y_j>-1\). The two cases establish the uniform lower bound
\[
y_i>-1\quad\text{at every point of the orbit}. \tag{14}
\]

Now choose \(j\) with \(y_j\) maximal, using the same two-predecessor notation. This time \(b f(t)=y_j-y_{j-1}\ge0\), so \(t\ge0\). Suppose \(a\ge2\). By (11), \(X\ge0\), and by (14), \(Y>-1\). With floor \(X=0\), the readout \(a\ge2\) cannot arise from floor \(Y=-1,0,1\); it therefore requires \(Y\ge2\). But then \(t=X-aY<1/2-4<0\), a contradiction. Thus \(a=1\).

It follows that \(y_{j-1}=Y+X=2X-t<1\). Together with (14) this gives \(-1<y_{j-1}<1\). Also \(0\le x_{j-1}=f(t)<1/2\), so its actual floors are \(0\) and either \(-1\) or \(0\). In both cases the frozen convention gives \(b=1\), including \(x_{j-1}=0\). Consequently
\[
y_j=2X-t+f(t)
    =2X-\frac{t^3}{1+t^2}\le2X<1. \tag{15}
\]
This bounds the maximum and proves (10). In \(\mathcal B\), both floor coordinates belong to \(\{-1,0\}\). The three nonzero pairs have gcd one, and the pair \((0,0)\) has the prescribed value one. Hence \(g_i=1\) at every point of every MAIN cycle. \(\square\)

The argument includes \(p=1\), repeated indices for short periods, zero increments, axes and the actual faces \(x=0,y=0\). The strict bounds exclude \(x=\pm1/2\) and \(y=-1,1,2\) from periodic points by proof, not by removing them from \(X\). The rectangle \(\mathcal B\) was not assumed invariant or substituted for the full carrier.

## 4. The two controls, independently

**Theorem 2 (G).** Every legal G periodic point also belongs to \(\mathcal B\), so \(\operatorname{Per}(G)\cap A_{\rm act}=\varnothing\) for its read-only original gcd observable.

**Proof.** Take any own legal periodic orbit, with \(x_{i+1}=f(x_i-y_i)\) and \(y_{i+1}=y_i+x_i\). The same legal fold bound gives (11). At a maximum of \(y_j\), set \(t=x_{j-2}-y_{j-2}\); then \(x_{j-1}=f(t)=y_j-y_{j-1}\ge0\), so \(t\ge0\). Directly from this control's recurrence,
\[
y_j=2x_{j-2}-t+f(t)
    =2x_{j-2}-\frac{t^3}{1+t^2}<1.
\]
At a minimum, \(t\le0\), and the same expression is at least \(2x_{j-2}>-1\). Thus (10) holds for G independently of MAIN's theorem. The floor check in \(\mathcal B\) gives \(\gamma=1\). No gcd rule has been inserted into G's evolution. \(\square\)

**Theorem 3 (L).** The total fold-OFF control has \(\operatorname{Per}(L)=\{(0,0)\}\); in particular its periodic active-gcd intersection is empty.

**Proof.** For this control's own actual coefficient \(g\),
\[
\|T_L(x,y)\|^2=(x-gy)^2+(gx+y)^2
              =(1+g^2)(x^2+y^2).
\]
On any period-\(p\) orbit,
\[
\|z\|^2=\left(\prod_{i=0}^{p-1}(1+g_i^2)\right)\|z\|^2,
\qquad \prod_{i=0}^{p-1}(1+g_i^2)\ge2^p>1.
\]
Thus \(z=0\). Conversely the origin is fixed and its own readout is one. No fold or critical guard has been imposed on L. \(\square\)

The stronger arbitrary-period conclusion for L is a separately proved control result. Its origin has the retained own primitive \(\log2\); it supplies neither MAIN recurrence exclusion nor MAIN prime credit.

## 5. Exact periodic-core and closed-ledger comparison

**Theorem 4.** For every \(p\ge1\), the complete actual fixed sets of \(T_M^p\) and \(T_G^p\) coincide. Their least-period core cycles are the same point sets, with the same cyclic dynamics, all-point step clocks, signed cycle sums, entire \(H\), positive primitive times when present, and repetition multiplicities. This does not identify their full basins or full groupoids.

**Proof.** Every MAIN cycle lies in \(\mathcal B\) by Theorem 1 and has current \(g=1\). At each of its points the MAIN formula and guard are exactly G's formula and guard, so all of its steps are actual G steps and its \(p\)-step return is unchanged. Conversely Theorem 2 gives \(g=1\) at every actual G cycle point, so every step is an actual MAIN step with the same successor. This proves both inclusions for every \(p\), hence equality of least periods and cyclic core identifications, not just equality of a list of lengths.

At each common core point the assigned fixed-label MAIN germ has \(g=1\), equal to G's own germ. Thus (4)–(5) agree pointwise, including the retained floor/null faces, not merely almost everywhere. Each common least-\(p\) cycle has the same signed sum \(C\) and therefore the same source isotropy \(p\mathbb Z\), clock map \(jp\mapsto jC\), and entire \(H=C\mathbb Z\). The extension isotropy and phases agree on that core according to (9).

It remains to count whole packets rather than chosen cycle points. In each deterministic partial owner, a periodic core and all its finite incoming form exactly one source orbit. Indeed an arrow meeting a cycle has a common future on that cycle, so its other endpoint must eventually enter it; conversely every such finite entrant is connected. Two different cycle cores cannot be in one source orbit, because their forward cycles cannot meet without being the same cycle. Thus a nonzero-\(C\) core gives exactly one closed height-translation orbit over its own full basin, with phase set \(\mathbb R/(C\mathbb Z)\), primitive \(|C|\), and all positive integer repeats. Non-eventually-periodic source orbits have trivial \(H\) and add no positive closed packet.

The identical core-cycle sets therefore give a bijection of the complete positive closed-packet ledgers, with multiplicities and repetitions retained. For \(C=0\), both retain the source isotropy and real phases but neither turns it into a positive primitive. Equal lengths of different core cycles do not merge those packets. This argument does not match individual incoming sources or their cross-point clocks between M and G. \(\square\)

All source objects outside \(\mathcal B\), including every arithmetic-active point, remain. Theorems 1–2 exclude them only from finite periodic cores. Whether such a point terminates, reaches a unit-gcd core, or follows an infinite nonperiodic itinerary is not newly classified. Its own clock (5), incoming (7)–(8), kernels and phase offsets remain its own. In particular periodic-core coincidence is not a proof of equal basins, global maps, full groupoids, measure-preserving conjugacy, or identical nonperiodic recurrence.

## 6. Audit decision and prime-target boundary

| Owner / comparison | New all-period evidence | What remains unclaimed |
| --- | --- | --- |
| MAIN | Every periodic point lies in \(\mathcal B\), hence \(\gamma=1\) | No classification of those unit-gcd cycles or nonperiodic dynamics |
| G | Same strict bound from its own recurrence; original observable \(\gamma=1\) on every cycle | No inserted arithmetic feedback and no classification of G cycles |
| L | Only the origin is periodic, by its own total-map norm identity | No transfer of this complete control classification to MAIN |
| MAIN versus G | Exact core sets and full closed-packet ledgers coincide, including own clocks, least periods and multiplicity | No identification of full basins, groupoids or nonperiodic sources |

The global activity gate has the exclusion exit, not the bounded-OPEN exit: all three \(\operatorname{Per}(U)\cap A_{\rm act}\) are empty. MAIN's nontrivial gcd feedback therefore supplies no distinction from G at the level of any finite periodic core or its primitive clock. This is recurrence-level PROVES_TOO_MUCH evidence about this unchanged owner.

It is not a proof that every MAIN primitive is nonprime or that a nonarithmetic map cannot happen to have prime-logarithmic data. The retained origin packet has primitive \(\log2\), so nonemptiness remains established by 456. Prime-only behavior for every positive primitive, global uniqueness per prime, and all-prime coverage are still OPEN. The new proof does not classify G's cycles to settle those questions.

Portfolio decision: **FORK after the completed global activity gate**. No formula, carrier, inverse version, measure, roof or terminal rule is repaired. Strong naturalness is not proved; arithmetic T1 remains NOT PASSED. T2's complete core-comparison statement is not target success. T3 is NOT AUDITED, classical fields NOT APPLICABLE, formal Route coordinates UNASSIGNED, Route B NOT INVOKED. No operator, trace, zeta, external realization or round 465 is introduced.

## 7. Dependencies, actual access, and research declarations

The new [audit card](candidate-card.md) was personally read at original lines 1–91 through its provided and measured EOF (91 lines), SHA-256 `e96d599790a383ada12996bda67363a308713cd7cfd1e5bfa184191a0d3a543d`. Root supplied its full-CP1 PASS and distinct author release; the CP1 file itself, current reviewer raw, answers and other current manuscripts were not read by this author.

Named unchanged dependency: [456 original card](../456-gcd-oblique-fold/candidate-card.md), original lines 1–86 only, prefix SHA-256 `84ee5f19a6910b63bff4e401f17c03fc9a667bbdc843c52bc951a16352152e46`; [456 paper](../456-gcd-oblique-fold/paper.md), lines 1–242 through EOF, SHA-256 `10174a938cae1b5c38fd2e94c44a098b95f9abed4c23bfae857dd8137fdc9220`. Its author [README](../456-gcd-oblique-fold/README.md), 18 lines, SHA-256 `35b1a8d6d6da0316c20b4a51577dc3cdfd09550cd683dbce712a155fc5008aa8`, and [ledger](../456-gcd-oblique-fold/claim-ledger.md), 24 lines, SHA-256 `8faa5246bd8203cfabd9b95b1ad616afd25144d3b97c55921f459c186afdba19`, were also fully reread during design.

This author designed and authored 456, so its positive and bounded negative outcomes are known. Root separately disclosed that 456 raw contains a stronger two-step sign argument for arbitrary positive coefficients. Its raw file and proof body were not read here; the disclosed statement is prior exposure and is not repackaged as a new 460 theorem. The new proof is the arbitrary-period extremum argument, not another two-word test.

During scoping the ARS router (488 lines), deep-research workflow (602), runtime policy (113), research-architect role (298), local AGENTS (221) and plan (411) were completely refreshed. The root readme lines 1–45 additionally exposed the preceding two batches' summary outcomes, not their proofs or peer files. No additional collision-card search was undertaken for this unchanged-owner audit. Existing design/history exposure is retained; this was not blind discovery or sealed preregistration.

One bounded same-model author helper, `gof_g_author_aid`, received only the new original card lines 1–91 and returned the own G and L global control arguments. It retained its earlier 456 card-only G context and reported no additional rereads. This is author assistance, not an independent reviewer seat. MAIN's global bound and the full-owner comparison were derived locally. ARS supplied scope, evidence and disclosure discipline; it did not authorize external literature or model transport.

All new science is exact symbolic proof. No numerical search, scientific program, web/API query, network upload, Git operation, old-file edit or PDF was used. Input checks were `nl -ba`, `sed`, `wc -l` and `SHA-256` hashing; final author checks use full EOF rereads and text/link/identity validation only. The audit relies on 456's owned measured-history theorem as identified in §2, without claiming it again as a new result.

Evidence index: [card](candidate-card.md), [claim ledger](claim-ledger.md), [overview](README.md). Root owns the append-only outcome, independent internal review integration and batch record; this author writes only these three author surfaces.

Data availability: no empirical dataset; frozen definitions, exact proofs and dependency hashes are local. Ethics: no human participants, personal data or animal subjects. Contributions: AI agents supplied design, mathematical derivation, drafting and bounded control-author assistance; root coordinates separate internal review. AI assistance is explicit; same-model/shared-history work remains NOT_CALIBRATED and no human/external verification is certified. Funding and conflict declarations were not supplied and are not invented. No external submission or publication is claimed.
