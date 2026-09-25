# Divisor cosine feedback: an owned half-log-five primitive

**Candidate ID:** `ANG-20260924-DCC02`  
**Paper:** `446-divisor-cosine-companion`  
**Batch:** `ADMISSION-EXIT-20260924-T`, round 2/5; 445–449 only.  
**Date:** 2026-09-24; exact mathematical audit.

Outcome: `OWNED COSINE CLOCK; HALF-LOG-5 PRIMITIVE — STOP / FORK`

The [candidate card](candidate-card.md), original lines 1–88, is unchanged. This paper proves its three-owner contract without enlarging the fixed-point window.

## Abstract

A partial map of the full real plane reads two floor labels, tests divisibility, and uses the resulting divisor and quotient in a cosine companion update. We prove its complete inverse-sheet enumeration, every-point inverse Jacobian and every-Borel IMAGE identity. The arithmetic-off and cosine-off controls have their own corresponding proofs. In the frozen square \([3,4)^2\), MAIN has exactly one actual fixed point, while both controls have none. MAIN's full two-dimensional multiplier there is \(\sqrt5\). Its entire incoming class has isotropy clock group \((\tfrac12\log5)\mathbb Z\), so the actual positive primitive is \(\tfrac12\log5\), not \(\log5\). Twice traversing the packet produces \(\log5\) only as a repetition. This violates the necessary ordinary-prime primitive condition and stops MAIN. The full source, all inverse sheets, terminal incoming, integer lag, clock kernels and real phases remain retained.

## 1. Same-object contract and divisor lineage

Each owner has \(X=\mathbb R^2\), its Borel structure, and flat Lebesgue measure \(\mu=dx\,dy\). At a current point \(z=(x,y)\), define
\[
n=|\lfloor x\rfloor|,\qquad d=|\lfloor y\rfloor|,\qquad
A=\{n,d\ge1,\ d\mid n\}.
\]
The quotient \(q=n/d\) is used only on \(A\). The separately owned maps are
\[
\begin{aligned}
D_M&=A\cap\{\sin x\ne0\},
&T_M(x,y)&=(y,\,2+d\cos x+qy),\\
D_G&=\{\sin x\ne0\},
&T_G(x,y)&=(y,\,2+\cos x+y),\\
D_L&=A,
&T_L(x,y)&=(y,\,2+dx+qy).
\end{aligned} \tag{1}
\]
Coefficients are read once per step and recomputed at the next actual state. G has no floor or divisibility guard; L has no sine guard. Every point outside the owner's domain is terminal, with its unit and all actual incoming, not an absorbing self-loop. Outputs are finite points of the full plane, whether or not the next step is permitted. All signs, axes, integer cuts and critical lines remain objects. The plane is not quotiented modulo \(2\pi\).

For positive integers \(N,D\) with \(2\le D<N\), the whole cell \([N,N+1)\times[D,D+1)\) reads \(n=N,d=D\); MAIN's arithmetic permission there is exactly \(D\mid N\), in addition to its geometric guard. A proper-divisor symbolic constraint therefore changes the actual permissible transport and its nonlinear coefficient. The next geometric coordinates determine the next arithmetic test. Unit divisors, self-divisors, noninteger states and failed tests are not filtered away.

| Field | Frozen owner | Claim boundary |
| --- | --- | --- |
| Source/action | Full Borel plane, the three partial maps (1) | Piecewise analytic, not a globally smooth conservative map |
| Reference measure/clock | Own full-plane inverse-germ determinant and IMAGE cocycle | No inserted roof or fitted prime time |
| Histories/packets | Actual triples with integer lag; entire clock isotropy | No selected sheets, centres or equal-length merging |
| Classical suspension/contact/Hamiltonian data | NOT APPLICABLE | No classical construction is inferred |
| Operator/trace/zeta/determinant | NOT CONSTRUCTED | T3 NOT AUDITED |

The constant \(2\), trigonometric feedback and hard permission are design choices; strong naturalness and PROVES_TOO_MUCH remain OPEN. The necessary arithmetic benchmark is nonemptiness, EVERY positive primitive equal to \(\log p\) for an ordinary prime, and at most one packet per prime. All-prime coverage is an additional obligation.

## 2. Complete inverse sheets, boundaries and coverage

For integers \(j\ge1\), put \(C_j=[j,j+1)\cup[-j,-j+1)\). Then \(|\lfloor x\rfloor|=j\) exactly when \(x\in C_j\). The negative interval is left-closed and right-open, just as the positive interval. No change of representative is made at a cut.

For MAIN, enumerate every positive integer pair \(n,d\) with \(d\mid n\), set \(q=n/d\), and enumerate every \(k\in\mathbb Z,\varepsilon\in\{-1,1\}\). For a target \(w=(s,t)\), write
\[
r=\frac{t-2-qs}{d},\qquad
X_{n,d,k,\varepsilon}(s,t)=2\pi k+\varepsilon\arccos r.
\]
Here \(\arccos:(-1,1)\to(0,\pi)\). The exact inverse and actual target domain are
\[
\begin{aligned}
\theta^M_{n,d,k,\varepsilon}(s,t)&=(X_{n,d,k,\varepsilon}(s,t),s),\\
\Omega^M_{n,d,k,\varepsilon}
&=\{(s,t):s\in C_d,\ -1<r<1,\,
X_{n,d,k,\varepsilon}(s,t)\in C_n\}.
\end{aligned} \tag{2}
\]
The displayed conditions imply all remaining frozen source checks: \(\sin X\ne0\), the actual absolute-floor readouts are \(n,d\), the quotient is \(q\), and \(\cos X=r\) gives \(T_M\theta^M(s,t)=(s,t)\). Conversely a legal source has \(\cos x\in(-1,1)\), and all solutions of \(\cos x=r\) are exactly \(2\pi k\pm\arccos r\). Its actual readout labels put its target in (2), and its unique open cosine half-period determines the sheet. Thus \(\theta^M T_Mz=z\) on that sheet and every actual predecessor is covered.

G separately uses \(r_G=t-2-s\) and
\[
\theta^G_{k,\varepsilon}(s,t)
=(2\pi k+\varepsilon\arccos r_G,s),\qquad
\Omega^G_{k,\varepsilon}=\{(s,t):-1<r_G<1\}. \tag{3}
\]
The same elementary cosine identity proves both inverse identities and full coverage, without any floor tests. Different real translates are retained, not identified on a circle.

For L enumerate all positive integers \(n,d\) with \(d\mid n\), set \(q=n/d\), and define
\[
\begin{aligned}
\theta^L_{n,d}(s,t)&=\left(\frac{t-2-qs}{d},s\right),\\
\Omega^L_{n,d}
&=\left\{(s,t):s\in C_d,\ \frac{t-2-qs}{d}\in C_n\right\}.
\end{aligned} \tag{4}
\]
Solving the second coordinate of \(T_L\) gives exactly (4); membership restores the actual labels and permission, and substitution proves both identities. All L sources with \(\sin x=0\) and valid arithmetic permission remain legal.

Equations (2)–(4) are Borel domains and exhaustive inverse formulas, not proposed tests still awaiting an oracle. The full maps are Borel partial self-maps with countable predecessor sets. Distinct labels or sheets have disjoint actual source images unless the reconstructed point is identical; actual points/triples, not free sheet words, determine identity.

No formula tests whether the target itself has a next step. Critical cosine endpoints \(r=\pm1\) give no legal inverse on that sheet, but their source points remain terminal objects for M/G; another actual label must always be checked independently. Integer edges use their actual half-open cell. All countably many sheets are retained; there is no principal-sheet selection or index cutoff.

## 3. Full-plane all-point IMAGE and clock direction

At fixed MAIN labels and sheet, let \(u=\sqrt{1-r^2}>0\). The analytic inverse germ has matrix
\[
D\theta^M=
\begin{pmatrix}
\varepsilon q/(du)&-\varepsilon/(du)\\
1&0
\end{pmatrix},
\qquad
J_M(s,t)=|\det D\theta^M|=\frac1{d\sqrt{1-r^2}}. \tag{5}
\]
For G the independently owned matrix has \(d=q=1,r=r_G\), so
\[
J_G(s,t)=\frac1{\sqrt{1-r_G^2}}. \tag{6}
\]
L has its own affine inverse matrix and density
\[
D\theta^L=
\begin{pmatrix}
-q/d&1/d\\
1&0
\end{pmatrix},
\qquad J_L(s,t)=\frac1d. \tag{7}
\]
All are finite and strictly positive at every actual inverse-domain point. They need not be uniformly bounded near an excluded critical boundary.

For each cosine sheet the displayed germ is a real-analytic diffeomorphism from the open strip \(-1<r<1\) onto the open half-period in its first source coordinate times the full second real coordinate. Its inverse is the fixed-label expression in (1). The arithmetic domains in (2) are Borel restrictions of this diffeomorphism; (3) uses its entire strip. The fixed-label L inverse is a global affine diffeomorphism restricted by (4). The ordinary two-dimensional change-of-variables theorem therefore gives, for EVERY Borel \(E\) in each actual target domain,
\[
\mu(\theta E)=\int_E J_\theta\,d\mu. \tag{8}
\]
This includes arbitrary null pieces and integer boundary subsets. The analytic extension fixes the prescribed value on those sets; the integral identity alone does not select a null-set version. Countable disjoint restrictions preserve (8), without adding masses for duplicate actual points.

On a legal source the complete real determinant and clock are
\[
\begin{array}{c|c|c}
O&\rho_O(x,y)=|\det DT_O|&\kappa_O(x,y)=-\log J_{\rm actual}(T_Oz)\\ \hline
M&d|\sin x|&\log(d|\sin x|)\\
G&|\sin x|&\log|\sin x|\\
L&d&\log d
\end{array} \tag{9}
\]
Here \(DT_O\) denotes the assigned fixed-label analytic germ, including at integer cuts, not differentiation of a discontinuous floor rule. For example \(DT_M=\left(\begin{smallmatrix}0&1\\-d\sin x&q\end{smallmatrix}\right)\), whose determinant is \(d\sin x\). Substitution into (5) gives \(J_M(T_Mz)=1/[d|\sin x|]\); the other two identities follow directly from (6)–(7). The shear entry \(q\) does not supply an additional determinant factor. No square of this real determinant is taken. At a terminal there is no one-step \(\kappa\), not an artificially assigned zero.

## 4. Full groupoids, all histories and unrestricted phases

Fix an owner \(O\). For every legal finite history, including one that ends at a terminal, set
\[
W_m(z)=\prod_{i=0}^{m-1}\rho_O(T_O^iz),\quad
S_m(z)=\log W_m(z),\quad W_0=1,\ S_0=0.
\]
Its full Borel groupoid is
\[
\mathcal G_O=\{(z,m-n,w):m,n\ge0,\ T_O^mz=T_O^nw
\text{ along legal histories}\},\qquad
c(z,m-n,w)=\log\frac{W_m(z)}{W_n(w)}. \tag{10}
\]
Source is \(w\), range is \(z\). Equal triples alone are identified; inversion negates the lag and multiplication adds lags. Borel legality/equality and countably many inverse sheets give a countable-fibre Borel groupoid on the full source.

Two presentations of one triple have their two lengths shifted by the same integer. Along the common suffix the two clock sums agree, so (10) is independent of the witness. For composition, align the two histories at the intermediate source using the larger already-legal length; the other matched history follows the same available suffix. This proves closure and clock additivity without extending any terminal illegally. The inverse arrow negates \(c\).

The three complete kernels are
\[
\begin{aligned}
K_{\rm lag}&=\{(z,0,w):T^mz=T^mw\text{ for some legal }m\},\\
K_c&=\{(z,m-n,w)\in\mathcal G_O:W_m(z)=W_n(w)\},\\
K_{\rm joint}&=\{(z,0,w)\in\mathcal G_O:
W_m(z)=W_m(w)\text{ at a common equal-depth meeting}\}.
\end{aligned} \tag{11}
\]
All zero-clock off-diagonal arrows are retained. A branch for range-from-source transport has absolute real determinant \(W_n(w)/W_m(z)=e^{-c}\); finite composition of (8) proves its IMAGE identity. In particular the forward arrow \((Tz,-1,z)\) has clock \(-\kappa_O(z)\), and its inverse has \(+\kappa_O(z)\).

Let \({\rm Pre}_O(w)\) be the union of ALL actual inverse values from (2), (3), or (4), as appropriate. Define \({\rm Pre}_O^0(w)=\{w\}\) and \({\rm Pre}_O^{j+1}(w)=\bigcup_{v\in{\rm Pre}_O^j(w)}{\rm Pre}_O(v)\) for every integer \(j\ge0\), deduplicating only equal points. Then the entire set of incoming arrows with range \(z\) is
\[
\bigcup_{\substack{m,n\ge0\\T^mz\ {\rm legal}}}
\{(z,m-n,w):w\in{\rm Pre}_O^n(T^mz)\}. \tag{12}
\]
Every witness in (10) appears here and every such predecessor supplies a witness. No restriction to the square, sign, label or depth is imposed.

A source has nonzero lag isotropy exactly when it is eventually periodic: equality at unequal legal times forces a periodic future; on a future of least period \(p\), exactly multiples of \(p\) occur. If \(C\) is the sum of the own clock (9) around that least cycle, then
\[
I_z=p\mathbb Z,\qquad c(z,jp,z)=jC,\qquad H_z=C\mathbb Z. \tag{13}
\]
Tail clocks cancel. A source not eventually periodic has \(I_z=\{0\}\) and \(H_z=\{0\}\). Extension isotropy is \(I_z\cap\ker c\), hence trivial if \(C\ne0\), all of \(p\mathbb Z\) if \(C=0\), and trivial on non-eventual sources. These are full-source structural criteria, not an enumeration of cycles.

For EACH terminal \(\tau\in X\setminus D_O\), its whole source orbit is \(B_\tau=\bigcup_{j\ge0}{\rm Pre}_O^j(\tau)\). Every \(z\in B_\tau\) has a unique arrival depth \(d_\tau(z)\), because no step leaves \(\tau\). Any common future can be advanced legally to \(\tau\). Thus there is exactly one arrow from \(w\) to \(z\) in this orbit, with lag \(d_\tau(z)-d_\tau(w)\) and clock \(S_{d_\tau(z)}(z)-S_{d_\tau(w)}(w)\). All terminal-orbit isotropy and \(H\) are trivial. Distinct terminals have disjoint incoming classes. This retains all incoming to axes, failed arithmetic tests and critical lines, without making those points absorbing.

The full height extension acts on EVERY \((z,h)\in X\times\mathbb R\) by
\[
(w,h)\longmapsto(z,h+c(z,k,w)).
\]
Height translation commutes with these arrows and acts on the orbit SET; no manifold, Hausdorff quotient or global selector is asserted. Its stabilizer at a class is exactly \(H_z\), since fixing the source class after a height displacement requires a source-isotropy arrow with that clock. Phases over each source orbit form an \(\mathbb R/H_z\) torsor. For a terminal orbit an explicit real coordinate is \(h-S_{d_\tau(z)}(z)\).

If \(H_z=L\mathbb Z\) with \(L>0\), the physical primitive is exactly \(L\), with repetitions \(jL,\ j\ge1\). If \(H_z=0\), no positive primitive exists, and zero-clock source isotropy is not deleted. Distinct source orbits remain different packets even when they have equal \(L\). Aperiodic, escaping and terminal histories are part of the same definitions, not a discarded remainder of the ledger.

## 5. All actual fixed points in the frozen square

The only classified window is \(W=[3,4)\times[3,4)\). A fixed point of any companion map must have \(x=y=s\). The arithmetic owners therefore read \(n=d=3,q=1\) throughout this diagonal window.

### 5.1 MAIN: every root and exact endpoint admission

MAIN's fixed equation in this cell is
\[
2+3\cos s=0,\qquad \cos s=-\frac23. \tag{14}
\]
Let \(\alpha=\arccos(-2/3)\in(0,\pi)\). All real solutions of (14) are \(s=2\pi k\pm\alpha,\ k\in\mathbb Z\); they must still pass the actual window and source checks.

We give exact analytic bounds instead of decimal evaluation. First \(3<\pi<22/7\). For a short self-contained verification, the identity \(\pi=4\int_0^1(1+t^2)^{-1}dt\) and the finite geometric-series lower bound give
\[
\pi>4\sum_{j=0}^{7}\frac{(-1)^j}{2j+1}
=\frac{135904}{45045}>3.
\]
Polynomial division also gives
\[
\frac{22}{7}-\pi
=\int_0^1\frac{t^4(1-t)^4}{1+t^2}\,dt>0.
\]
Put \(a=\pi-3\in(0,1/7)\) and \(b=4-\pi\in(6/7,1)\). The elementary alternating Taylor bounds yield
\[
\cos a\ge1-\frac{a^2}{2}>\frac{97}{98}>\frac23.
\]
The polynomial \(P(t)=1-t^2/2+t^4/24\) is strictly decreasing on \((0,1)\), so
\[
\cos b\le P(b)<P(6/7)=\frac{1573}{2401}<\frac23.
\]
Consequently \(\cos3=-\cos a<-2/3\) and \(\cos4=-\cos b>-2/3\). Cosine strictly decreases on \([3,\pi]\), and strictly increases on \([\pi,4]\). There is therefore exactly one solution in \([3,4)\), lying strictly in \((\pi,4)\), namely
\[
s_* = 2\pi-\alpha,\qquad \xi=(s_*,s_*). \tag{15}
\]
This monotonicity argument exhausts every real solution in the whole window; it does not select a sign before checking admission. Both half-open edges are handled by the strict endpoint inequalities. Since \(3<s_*<4\), the actual labels are \(n=d=3,q=1\). Equation (14) gives \(|\sin s_*|=\sqrt5/3\ne0\), so the geometric guard also holds, and \(T_M\xi=(s_*,2-2+s_*)=\xi\). The inverse sheet at the core has \(k=1,\varepsilon=-1\), with actual \(r=-2/3\).

### 5.2 The two controls: complete window results

For G a fixed point in W would satisfy \(2+\cos s=0\), which has no real solution because \(-1\le\cos s\le1\). Thus there is no actual G fixed point in W, even before its own sine guard is imposed.

For L the actual window labels give \(2+3s=0\). Its sole formal real root is \(s=-2/3\), outside W and with \(|\lfloor s\rfloor|=1\), not the required label \(3\). It fails the cell/source check. Therefore L also has no actual fixed point in W. No sine exclusion is used for this result. The formal point remains in the full plane; failure of this cell equation's admission does not delete it or declare it terminal under its actual labels.

| Owner | Complete actual fixed set in W | Own window conclusion |
| --- | --- | --- |
| MAIN | \(\{\xi\}\), equation (15) | One admitted fixed core; entire packet calculated below |
| G | Empty | No fixed packet supplied by this window |
| L | Empty | No fixed packet supplied by this window |

The control conclusions are not global clock or higher-period absence claims, and neither is used to substitute for MAIN's own counterexample.

## 6. The entire MAIN incoming packet and its true primitive

At \(\xi\), the full-plane formulas (5) and (9) give
\[
\rho_M(\xi)=3|\sin s_*|=\sqrt5,\qquad
J_{\rm actual}(\xi)=\frac1{\sqrt5},\qquad
L=\kappa_M(\xi)=\log\sqrt5=\frac12\log5>0. \tag{16}
\]
The absolute value of the full two-dimensional determinant is \(\sqrt5\), not \(5\). A principal-sheet or sign choice cannot change its absolute value; squaring it would change the frozen clock.

Define the unrestricted incoming class
\[
B_\xi=\bigcup_{d\ge0}{\rm Pre}_M^d(\xi).
\]
This is exactly the source-groupoid orbit of \(\xi\): any source sharing a future with a fixed core must reach that core, and every such predecessor shares that future. It includes all actual inverse generations from all real sheets and arithmetic labels. This exact recursion is not a finite enumeration or a claim of bounded basin size.

Let \(d(z)\) be the least arrival depth to \(\xi\), and put
\[
\beta(z)=S_{d(z)}(z)-d(z)L,\qquad \beta(\xi)=0.
\]
For all \(m\ge d(z)\), \(T^mz=\xi\) and \(S_m(z)=mL+\beta(z)\). Any integer \(k\) can be realized by taking two sufficiently large meeting times with difference \(k\); an earlier common meeting advances to \(\xi\) and gives the same clock. Hence
\[
\mathcal G_M|B_\xi=B_\xi\times\mathbb Z\times B_\xi,\qquad
c(z,k,w)=kL+\beta(z)-\beta(w). \tag{17}
\]
These are ALL incoming arrows at every point of this orbit, not just arrows at the fixed core. The restricted lag kernel is \(k=0\); the clock kernel is \(kL=\beta(w)-\beta(z)\); their intersection is \(k=0,\beta(z)=\beta(w)\).

For every \(z\in B_\xi\), the entire source-isotropy character and height isotropy are
\[
I_z=\mathbb Z,\qquad c(z,k,z)=kL,\qquad
H_z=L\mathbb Z,\qquad I^{\rm extension}_{(z,h)}=\{0\}. \tag{18}
\]
All real phases are represented by \(h-\beta(z)\pmod{L\mathbb Z}\): equation (17) changes this quantity by exactly \(kL\), and every such congruence is realized by an actual arrow. Thus the full source orbit supplies one height-translation packet, not one packet per tail or per real phase. Its primitive is \(L\); traversing it \(j\) times gives \(jL\). Null core points and every tail remain present.

Since \(2<\sqrt5<3\), \(\sqrt5\) is not an ordinary integer prime. Consequently \(L\ne\log p\) for every ordinary prime \(p\). The value \(2L=\log5\) is a SECOND traversal, not an eligible replacement primitive. Equation (18) rules out both a smaller hidden primitive and a reinterpretation of the primitive as that repetition. This actual MAIN packet establishes nonemptiness but refutes the necessary ordinary-prime primitive condition.

## 7. Controls, decision and limits

G removes the arithmetic gate and coefficients but retains its own sine guard, inverse sheets, Lebesgue IMAGE and full groupoid. L retains the arithmetic gate and coefficients but removes the periodic fold and sine guard, with its own affine IMAGE. Equations (2)–(13) independently supply all of their full-source inverses, incoming, kernels, isotropy and phase conventions. Their empty window fixed sets do not imply their global \(H\) vanishes. No control's clock or absence result is borrowed by MAIN.

| Gate | Established finding | Limitation |
| --- | --- | --- |
| T0 | Full Borel owners, every-point/every-Borel IMAGE, complete signed-lag extension | No conservative or smooth quotient-flow claim |
| T1 | Divisor feedback verified; ordinary-prime clock benchmark NOT PASSED | Fixed design's strong naturalness remains OPEN |
| T2 | Full MAIN incoming packet has primitive \(\tfrac12\log5\) and exact repetitions | Prime primitive condition fails; no global periodic census |
| T3 / formal Route / B | NOT AUDITED / UNASSIGNED / NOT INVOKED | No operator, trace, determinant or external section |

The same-object ledger remains intact. Stop MAIN on the exhibited wrong primitive and fork only under a fresh frozen contract. All-prime coverage and global packet uniqueness are unproved and cannot repair this counterexample. Only W was classified for fixed points; no spatial expansion, higher-period search, parameter adjustment, null-state deletion or time rescaling was performed.

## Reproducibility, provenance and disclosures

The evidence is the exact proof above, the [claim ledger](claim-ledger.md) and the [package README](README.md). The author read the entire frozen card, lines 1–88/EOF, and measured SHA-256 `376f0e6e186bcec2df76163e410eed027d43c0d2595d9ae2971b8bab358e1041`. The local paper template was read through line 107/EOF. No 446 scope, raw proof, final review, current peer or helper manuscript was read. No helper was used for this author proof.

During definition scouting, the author read 396 card lines 1–53/nonEOF (measured full total 115), prefix SHA-256 `dc369b5baf767bc37c5402db62af481498ef49fb6daf6d87da6203624e997b83`; and 412 card lines 1–50/nonEOF (measured full total 112), prefix SHA-256 `882851254225dc4fe5f5a609c4566841b8cf3b21eda6198f5f29419609958131`. A heading command also exposed the actual short Outcome sentences at 396:102 and 412:98, not merely their titles; the following outcome/proof bodies were not read. The former definition has independent coprime integer roots and quadratic Hénon feedback, the latter integer memory and a sine-kick cylinder. The present full-plane current-floor cosine map differs as written; no nonconjugacy or literature novelty theorem is asserted, and no old result is used in this proof.

Root supplied the law and window after informal feasibility thought; the scout supplied inverse-domain design before freezing. This is shared-history work, not blind discovery or sealed preregistration. For this author turn the ARS router, academic-paper workflow, argument-builder/draft-writer contracts, writing-quality/title guidance and model-runtime policy were read completely; initially truncated instruction reads were completed in bounded follow-up ranges. The instructions support claim/evidence discipline, not a correctness certificate or expanded research authority.

Data availability: the frozen definition and all exact derivations are in this package; no external dataset or scientific numerical computation is used. Tools were used for bounded file reads, permitted Markdown edits and mechanical file/link/hash checks, not a periodic census. No network, Git, PDF, publication, operator or zero-data work was performed.

Author contributions: root supplied source design and integration; this AI author supplied definition completion, exact mathematical derivation and drafting; separate internal review is owned by root's workflow, not this author. AI agents supplied research design, derivation, drafting and internal workflow review. No human or external verification is certified. Same-model shared-history assistance remains `NOT_CALIBRATED`, not blind, cross-model or external peer review.

Ethics: this pure mathematical audit uses no human/animal participants or private empirical data. Funding and competing-interest declarations were not supplied; none is inferred on behalf of a human author or institution. No venue-specific submission or review-criteria certification is claimed.
