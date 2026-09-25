# Common-factor transport has nonprime fixed primitives

Candidate ID: ANG-20260925-CFT01.
Outcome: OWNED FACTOR CLOCK; NONPRIME FIXED PACKETS — STOP / FORK

Paper483-common-factor-transport, version1, 2026-09-25.
Batch PRE-P0-STRUCTURE-20260925-AA, round4/5, exactly480–484.
Type: ANG full measured Borel history owner, with original product probability.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal coordinates UNASSIGNED; Route B NOT INVOKED.
AI-assisted same-model/shared-history work is NOT_CALIBRATED; no human, external or cross-family verification is certified.

## Abstract

The frozen map consumes the first letter of a positive-integer stream after transporting its common factor with the second letter into the third. We prove the complete inverse atlas, every-Borel original-measure IMAGE and all-point history clock for MAIN and three separate controls. Without selecting a tail, MAIN's entire fixed set is \(M_m=(m,m^2,m,m,\ldots)\), \(m\ge1\). Each complete \(M_m\) basin owns primitive \(\log(m(m+1))\). The unit core supplies \(\log2\), while every \(m\ge2\) supplies an actual nonprime primitive, so prime-only purity fails. Common-factor-OFF has the same indexed fixed times but different fixed words and incoming; propagation-OFF changes the times; division-OFF has infinitely many distinct log-two fixed packets despite their identical ordinary tails. Full incoming, actual lags, clock kernels, entire isotropy images, phases and repetitions are retained. No higher-period census or measure repair is performed.

## 1. Full source, own laws and arithmetic interface

Let
\[
A=\mathbb N_{\ge1},\qquad X=A^{\mathbb N_0},\qquad
\rho(n)=\frac1{n(n+1)},\qquad \mu=\rho^{\mathbb N_0}. \tag{1}
\]
Use the full discrete-alphabet product topology and Borel structure. All positive infinite words, units, ordered repetitions, unbounded sequences and null periodic tails remain. There are no terminals, finite/empty words or added boundary states. Zero and negative letters were never in this alphabet.

For \(z=(a,b,c,\eta)\), set \(g=\gcd(a,b)\). The four independently owned maps are
\[
\begin{array}{c|c}
M\text{ MAIN}&T_Mz=(b/g,gc,\eta)\\
G\text{ common-factor-OFF}&T_Gz=(b,c,\eta)\\
P\text{ propagation-OFF}&T_Pz=(b/g,c,\eta)\\
D\text{ division-OFF}&T_Dz=(b,gc,\eta).
\end{array} \tag{2}
\]
Each is total on the same full \(X\), with its own original \(\mu\). Positivity and \(g\mid b\) make the output legal, including every unit case. Each step rereads its changed word. The finite-prefix rules make the maps continuous and Borel; no branch symbol or arithmetic label is added to the state.

For integers \(1<D<N\), the source \((N,D,c,\eta)\) has \(\gcd(N,D)=D\) iff \(D\mid N\), and MAIN then actually outputs \((1,Dc,\eta)\). Failed divisibility tests execute their own gcd transport. Thus the lineage is divisor-symbolic observation \(\to\) current common factor \(\to\) transport between adjacent letters \(\to\) the next arithmetic state. There is no static test root, prime table, fitted clock or external schedule. This rule and reference measure are declared design, not canonical naturalness or a conservative/symplectic lift.

The ONLY location gate is every owner's GLOBAL fixed set, including arbitrary tails until the equations themselves restrict them. The target separately requires positive nonemptiness, every positive primitive to be \(\log p\) for an ordinary prime, at most one full packet per prime, and all-prime coverage. No rescaling, ordinary-tail quotient or equal-time merging is allowed.

## 2. Product law and exhaustive inverse atlas

The finite sums satisfy
\[
\sum_{n=1}^{N}\rho(n)=\sum_{n=1}^{N}(1/n-1/(n+1))=1-\frac1{N+1}.
\]
Thus \(\rho\) is a probability and its consistent cylinder products define the countable product law \(\mu\). Every nonempty finite cylinder has positive mass, giving full support. Since \(\rho(n)\le1/2\), a cylinder of length \(r\) has mass at most \(2^{-r}\); continuity from above implies \(\mu(\{z\})=0\) for every word. No null word is removed.

For target \(y=(u,v,\eta)\), all inverse branches are:

| Owner | Integer indices / actual target constraints | Predecessor |
| --- | --- | --- |
| M | \(g\mid v,\ h\ge1,\ \gcd(h,u)=1\) | \((gh,gu,v/g,\eta)\) |
| G | every \(a\ge1\) | \((a,u,v,\eta)\) |
| P | \(g,h\ge1,\ \gcd(h,u)=1\) | \((gh,gu,v,\eta)\) |
| D | \(g\mid u,\ g\mid v,\ h\ge1,\ \gcd(h,u/g)=1\) | \((gh,u,v/g,\eta)\) |

Every divisibility statement here is between positive integers. Fix \(u,v\) and all inverse indices before treating a row as a chart. Its domain is the ENTIRE cylinder \([u,v]\), and its image is its displayed three-letter cylinder. If the conditions fail, that indexed chart is absent.

**Proposition 1.** These are exact, exhaustive and uniquely source-indexed inverse families. Each owner is onto \(X\).

**Proof.** For M, a source with actual gcd \(g\) has \(a=gh,b=gu\), \(\gcd(h,u)=1\), and output second letter \(v=gc\), so \(g\mid v\). Conversely these conditions give \(\gcd(gh,gu)=g\) and reconstruct the output exactly. The actual source determines \(g\) and \(h\) uniquely. For P the same gcd computation applies, but \(v=c\); there is no \(g\mid v\) constraint. For D the target first letter is \(u=b\), so its actual gcd divides \(u\) and \(v=gc\); writing \(a=gh\) leaves precisely \(\gcd(h,u/g)=1\). Conversely that condition gives the correct gcd and output. G is the ordinary first-letter deletion and has exactly its free first-letter choices, with no gcd guard.

These arguments prove both \(T\theta=\mathrm{id}\) on every actual target cylinder and \(\theta T=\mathrm{id}\) on its corresponding source cylinder. They also prove exhaustion and prevent duplicating one actual predecessor by different gcd labels. In every owner, \((1,u,v,\eta)\) is a valid predecessor of \((u,v,\eta)\), using \(g=h=1\) when present. Hence every target has incoming. Each row is a prefix homeomorphism; the countable atlas covers all one-step inverses. \(\square\)

## 3. Every-Borel IMAGE and the prescribed null-point version

For a fixed chart \(\theta:[u,v]\to[a,b,c]\), freeze the entire-point density
\[
J_\theta=\frac{\rho(a)\rho(b)\rho(c)}{\rho(u)\rho(v)}. \tag{3}
\]
It is positive finite, including on every null tail. In particular, the four own values are
\[
\begin{array}{c|c}
M&\rho(gh)\rho(gu)\rho(v/g)/[\rho(u)\rho(v)]\\
G&\rho(a)\\
P&\rho(gh)\rho(gu)/\rho(u)\\
D&\rho(gh)\rho(v/g)/\rho(v).
\end{array} \tag{4}
\]

**Proposition 2.** For every Borel \(E\subseteq[u,v]\),
\[
\mu(\theta E)=\int_EJ_\theta\,d\mu. \tag{5}
\]

**Proof.** Write \(E=(u,v,E')\), where \(E'\) is its Borel set of tails under the cylinder's canonical product identification. Then \(\mu(E)=\rho(u)\rho(v)\mu(E')\) and \(\mu(\theta E)=\rho(a)\rho(b)\rho(c)\mu(E')\), proving (5) by multiplication, even when \(\mu(E')=0\). This is not division by the mass of \(E\). It proves the identity for arbitrary Borel tail restrictions, not just finite cylinders. The explicit source/target word identifies the frozen value at each null point, although measure identities alone would not uniquely determine an a.e. version there. \(\square\)

For each source point, use its unique actual inverse chart and set
\[
j(z)=J_{\text{actual inverse}}(Tz),\qquad \kappa(z)=-\log j(z). \tag{6}
\]
No invariance, positivity of every \(\kappa\), or incoming normalization is assumed. All signs and zeros are retained. Refinements by extra tail cylinders preserve (3) because their common cylinder factor cancels; the control clocks belong to their own laws, not to MAIN. The reference law agrees with the declared law in325, but no theorem or clock of that different map is transferred.

## 4. Full actual history owner and kernels

All iterates have domain \(X\). For one owner at a time, put
\[
J_0(z)=1,\quad J_r(z)=\prod_{i=0}^{r-1}j(T^iz),\qquad
S_r(z)=-\log J_r(z).
\]
Only finite products occur. The actual groupoid and its proposed clock are
\[
G_T=\{(z,r-s,w):T^rz=T^sw,\ r,s\ge0\},\quad
c(z,r-s,w)=S_r(z)-S_s(w)
=\log\frac{J_s(w)}{J_r(z)}. \tag{7}
\]
Source is \(w\), range is \(z\); equal triples alone are identified. Fixed-depth equality is Borel, and the countable inverse atlas gives countable source/range fibres. Extra free branch-word labels are not isotropy.

**Proposition 3.** Formula (7) descends to actual triples, is additive, and has history-pair IMAGE density \(e^{-c}\) from source to range.

**Proof.** Two witnesses of the same lag differ by a common integer added to their two depths. Extend the shorter witness; extra products start at its equal future, so cancel. For composition, extend witnesses until their shared-point depths agree, then cancel those terms. This proves descent and additivity on all points.

Refine a finite itinerary to fixed input letters sufficient to determine every gcd and output prefix. The resulting iterate is a finite-prefix replacement with unchanged tail, and its inverse density is the product of its one-step values by Proposition 2. A history pair applies a forward \(s\)-step branch and then an inverse \(r\)-step branch; its density is \(J_r(z)/J_s(w)=e^{-c}\). Equivalently, apply the same product-tail calculation as (5) to the whole prefix replacement. Both proofs apply to every Borel restriction and all null-point prescribed values. Countably many such charts cover all witnesses. In particular the forward arrow \((Tz,-1,z)\) has \(c=-\kappa(z)\). \(\square\)

The complete kernel tests are
\[
\ker\mathrm{lag}=\{r=s\},\qquad
\ker c=\{J_r(z)=J_s(w)\},\qquad
\ker\mathrm{lag}\cap\ker c=\{r=s,\ J_r(z)=J_r(w)\}. \tag{8}
\]
All conditions are on actual arrows and do not depend on the chosen witness.

The extension retains ALL \(X\times\mathbb R_h\), with \((w,h)\mapsto(z,h+c)\). Real height translation acts on its orbit SET. No positive roof, smooth quotient, conservative measure or operator is claimed.

For an arbitrary source \(z\), nonzero source isotropy occurs exactly when its actual orbit eventually enters a finite least-period core: equality \(T^rz=T^sz\), \(r>s\), gives a periodic future, and the converse follows by iterating that core. If its least period is \(q\) and
\[
\ell=\sum_{i=0}^{q-1}\kappa(T^iP),
\]
then exactly
\[
I_z=q\mathbb Z,\qquad c(z,kq,z)=k\ell,\qquad H_z=\ell\mathbb Z. \tag{9}
\]
Least period determines all possible lags, and common transient sums cancel. Without such a core, \(I_z=H_z=\{0\}\). Extension isotropy is \(q\mathbb Z\) when \(\ell=0\), and trivial otherwise. For \(\ell\ne0\), the ACTUAL positive physical primitive is \(|\ell|\), not a chosen sign or normalized value, with repeats \(j|\ell|\). If \(\ell=0\), ineffective source isotropy remains but there is no positive periodic time. These are full-source conditional formulas, not a higher-period census.

Each source orbit's extension orbit-set fibre is \(\mathbb R/H_z\), with changes of reference given by actual arrow-clock offsets. Distinct source orbits are never identified by equal time. The global height-action kernel is trivial: all four laws obey \((T^rz)_i=z_{i+r}\) for \(i\ge2\), by induction from (2). For \(z_i=i+1\), equality of two iterates forces \(r=s\), so this retained source has \(H_z=\{0\}\). This uses a tail identity, not a new periodic search.

## 5. Entire incoming and fixed-basin phases

For any target \(t\), define
\[
\mathcal P_0(t)=\{t\},\qquad
\mathcal P_{r+1}(t)=
\bigcup_{v\in\mathcal P_r(t)}
\{\theta(v):\theta\text{ is an actual own atlas branch at }v\}. \tag{10}
\]
Proposition 1 and induction prove that this is exactly the set of ALL depth-\(r\) predecessors, with every permitted divisor and every unbounded \(h\) or \(a\) index. All incoming arrows to range \(t\) are exactly
\[
\{(t,r-s,z):r,s\ge0,\ z\in\mathcal P_s(T^rt)\}. \tag{11}
\]
Every witness supplies a listed point and vice versa. Taking inverses gives all outgoing arrows. Compatible infinite incoming histories are exactly all sequences \(z_0=t,\ Tz_{n+1}=z_n\); existence follows, for example, by repeatedly using the available first-letter-one inverse, but this example does not replace any other history.

Two source points are in the same orbit iff they have an actual common future. Extended points are equivalent iff some such witness additionally satisfies \(h_z-h_w=S_r(z)-S_s(w)\). Ordinary eventual agreement of tails alone is not the definition of this groupoid.

For any actual fixed core \(P\), set
\[
\ell_P=\kappa(P),\quad
\mathcal B(P)=\bigcup_{N\ge0}\mathcal P_N(P),\quad
\beta_P(z)=S_N(z)-N\ell_P\quad(T^Nz=P). \tag{12}
\]
Extra steps after entry are fixed-core steps, proving independence of \(N\). A common future with \(P\) must equal \(P\), so \(\mathcal B(P)\) is its ENTIRE source orbit. For two points in this basin, arbitrary extra fixed-core steps realize every integer lag \(k\); hence
\[
G_T|_{\mathcal B(P)}=\mathcal B(P)\times\mathbb Z\times\mathcal B(P),\quad
c(z,k,w)=\beta_P(z)-\beta_P(w)+k\ell_P. \tag{13}
\]
This proves the full basin ledger, not just its core value: lag kernel \(k=0\); clock kernel the zero of the right side; joint kernel both; source isotropy \(\mathbb Z\), ENTIRE \(H_z=\ell_P\mathbb Z\), and phase \([h-\beta_P(z)]\in\mathbb R/(\ell_P\mathbb Z)\). If \(\ell_P\ne0\), extension isotropy is trivial and its full phase circle is ONE physical translation orbit, with primitive \(|\ell_P|\) and all repeats. Distinct fixed cores have disjoint source orbits.

## 6. All global fixed words, without a tail assumption

Write \(m^\infty=(m,m,\ldots)\). For \(m\ge1\), define
\[
M_m=(m,m^2,m^\infty),\quad G_m=m^\infty,\quad
P_m=(m,(m^2)^\infty),\quad D_m=(m,m,1^\infty).
\]

**Theorem 4.** The entire fixed set of each owner is its correspondingly named family above. Their whole-basin positive primitives are, respectively,
\[
L(M_m)=L(G_m)=\log[m(m+1)],\quad
L(P_m)=\log[m^2(m^2+1)],\quad
L(D_m)=\log2. \tag{14}
\]

**Proof.** If \(Tz=z\), the common tail identity from (2) gives \(z_i=z_{i+1}\) for every \(i\ge2\). Thus \(z=(a,b,c,c,\ldots)\) is forced, not selected.

For MAIN, the first two fixed equations are \(a=b/g,\ b=gc\), with \(g=\gcd(a,b)\). The first gives \(b=ga\), hence \(g=\gcd(a,ga)=a\). The second then gives \(c=a\) and \(b=a^2\). This yields exactly \(M_a\), and substitution verifies every such word.

For G, deletion fixes precisely \(a=b=c\), giving \(G_a\). For P, the equations are \(a=b/g,\ b=c\). Again \(g=a,b=a^2\), now with \(c=a^2\), giving \(P_a\). For D, the equations are \(a=b,\ b=gc\); then \(g=a\) and positivity forces \(c=1\), giving \(D_a\). Substitution verifies both control families. This covers every positive integer and every possible tail.

At a fixed word the source prefix and target prefix in (3) cancel as follows:
\[
j(M_m)=\frac{\rho(m)\rho(m^2)\rho(m)}
{\rho(m)\rho(m^2)}=\rho(m),\qquad j(G_m)=\rho(m),
\]
\[
j(P_m)=\frac{\rho(m)\rho(m^2)^2}{\rho(m)\rho(m^2)}
=\rho(m^2),\qquad
j(D_m)=\frac{\rho(m)^2\rho(1)}{\rho(m)^2}=\rho(1).
\]
All resulting \(\ell_P=-\log j(P)\) are positive. Formula (13) proves their ENTIRE \(H=\ell_P\mathbb Z\), so these are actual primitive times, not merely one return time or an upper bound. This proves (14), including \(m=1\). \(\square\)

## 7. Full fixed-packet multiplicity and controls

To make the unrestricted basin recipe explicit for every family, their complete first inverse layers are
\[
\begin{array}{c|l}
M_m&(gh,gm,m^2/g,m^\infty),\quad g\mid m^2,\ \gcd(h,m)=1\\
G_m&(a,m^\infty),\quad a\ge1\\
P_m&(gh,gm,(m^2)^\infty),\quad g,h\ge1,\ \gcd(h,m)=1\\
D_m&(gh,m,m/g,1^\infty),\quad g\mid m,\ \gcd(h,m/g)=1.
\end{array} \tag{15}
\]
All indices not otherwise bounded are positive integers. These are direct substitutions into the proved own atlases, so include every predecessor, not just one visible cycle. Iterate (10) with those same actual atlas checks for all further depths; (12)–(13) then determine all real offsets, phases, kernels and compatible histories for EVERY fixed family.

Each owner has countably infinitely many different fixed cores. Two different cores cannot have a common future, because they are fixed. Hence each listed core supplies exactly one full positive packet and no two are merged. In D, all cores even have the SAME ordinary tail \(1^\infty\), yet \(D_m\ne D_n\) remain distinct actual packets for \(m\ne n\). Replacing \(G_D\) by an unrestricted tail-equivalence groupoid would change the object and its multiplicity.

MAIN has one prime-valued fixed packet, \(M_1\), of primitive \(\log2\). For every \(m\ge2\), \(m(m+1)\) is a product of two integers greater than one, so \(L(M_m)\) is NOT the logarithm of an ordinary prime. In particular \(M_2=(2,4,2,2,\ldots)\) owns primitive \(\log6\). It cannot be split into log-two and log-three packets or relabelled a repetition: its entire return image is exactly \((\log6)\mathbb Z\). The numbers \(m(m+1)\) are strictly increasing, so the MAIN fixed times are pairwise different; this is only fixed-gate uniqueness, not a full-source uniqueness theorem.

G independently reproduces the indexed MAIN fixed times at constant words, not the same fixed states for \(m>1\). P has its own integer products in (14), and D has countably infinite duplicate prime-2 fixed packets. These are control results, not additional MAIN counterexamples. Their different inverse layers in (15) remain; no isomorphism of their full groupoids follows from matching times.

The MAIN nonprime cores have actual common factor \(m>1\), so both division and propagation are active in their fixed equations even though the resulting full word is unchanged. Nevertheless common-factor-OFF already produces the same set of fixed primitive values. This gate does not establish arithmetic necessity for prime specificity. Identical product-law input does not license transferring a control's return structure.

## 8. Decision, limits and provenance

Positive MAIN nonemptiness is established and prime-only purity is REFUTED by its own fixed packets. Thus the portfolio decision is STOP / FORK, with no endpoint, alphabet, map, measure, roof or packet repair. Among fixed packets only \(\log2\) is prime-valued and occurs once. Whether other actual cycles duplicate it or realize other primes is not decided; global uniqueness and all-prime coverage remain OPEN. No high-period census or new return gate was added.

T0 and the original-measure full-point history obligations are established. Arithmetic T1 target success is NOT PASSED; complete T2 accounting is not prime-target success. Strong naturalness and PROVES_TOO_MUCH remain OPEN. T3 NOT AUDITED; classical NOT APPLICABLE; formal coordinates UNASSIGNED; Route B NOT INVOKED. No operator, trace, determinant or smooth/conservative flow is constructed.

The sole new scientific input was the [clarified frozen card](candidate-card.md), personally read lines1–90 through measured EOF, SHA-256 2205c8e385b779d3d6722a98adad100bd31c46ab921edcc287cf67a2f50043a5. Its original80-line prefix and pre-proof target clarification were both included. Root reported complete CP1 PASS and issued DISTINCT AUTHOR RELEASE; no scope file, raw proof, reviewer answer, peer paper or old proof was read. No helper was used.

Design collision reads were [325 card](../325-gcd-split-coprime-merge/candidate-card.md) lines1–65 of197, prefix SHA-256 cd1fbc966a3e97f20923c8ad20a9996b1ef490995b391653bb81e8a5382fa463, and [471 card](../471-factor-word-return-skeleton/candidate-card.md) lines1–49 of116, prefix SHA-256 d7ba94f6deb6ebc924e83a3f9408a2ea3f505b8163353e0e7a24b2036f9e637f. Neither read reached EOF. Filename discovery preceded heading checks restricted to each first65 lines;471's Short gate heading was exposed, not its body or appended Outcome. Original initial OPEN labels were visible. 325 uses conditional two-to-three splitting/two-to-one merging;471 uses finite factor words with interval ports. Those are definition comparisons only, not global novelty or nonconjugacy claims.

Inherited325/471 context and478 authorship remain disclosed. The scout considered inverse and fixed-equation feasibility before freeze, so this was not blind or outcome-sealed preregistration. The mathematical proof here was completed after release. ARS's fully read applicable scoping/writing instructions and local paper template support evidence separation and disclosure; they do not enlarge the frozen gate.

Methods are exact integer algebra, product-measure identities and finite-history induction; no scientific code or numerical search. Reading and mechanical checks use bounded sed/nl, line counts, SHA-256, full EOF self-reading and local link/identity checks. Only paper.md, README.md and claim-ledger.md are author writes. Root owns card outcome and integration. No network/API, Git mutation, old edit, PDF, external publication or round485.

Evidence: [card](candidate-card.md), [claim ledger](claim-ledger.md), [overview](README.md). Data availability: the frozen local definitions and self-contained proofs; no empirical dataset. Ethics: no human participants, personal data or animal subjects. Contributions: AI agents supplied source design, mathematical derivation and drafting; root coordinates separate internal review. Same-model/shared-history work is NOT_CALIBRATED; no human, external or cross-family verification is certified. Funding/conflict information was not supplied and is not invented. No submission or formal Route success is claimed.
