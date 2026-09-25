# Count-dependent cuts produce infinitely many distinct log-two packets

Candidate ID: ANG-20260925-CFR01.
Outcome: OWNED COUNT CLOCK; INFINITE PRIME-2 FIXED MULTIPLICITY — STOP / FORK

Paper478-count-factor-return, version1, 2026-09-25.
Batch PRE-P0-STRUCTURE-20260925-Z, round4/5, exactly475–479.
Type: ANG measured Borel history owner; original counting × interval Lebesgue.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal coordinates UNASSIGNED; Route B NOT INVOKED.
AI-assisted same-model/shared-history work is NOT_CALIBRATED; no human, external or cross-family verification is certified.

## Abstract

The frozen source couples two nonnegative integer counts to a closed interval. Its current count ratio determines a geometric cut; the selected side executes addition, proper-divisor factorization or swapping, and the new counts determine the next cut. We prove the entire inverse atlas and original-measure IMAGE at every actual point, including both endpoints and empty-count terminals. MAIN has a continuous zero-clock fixed family and one positive fixed core \(P_k=(k,k,1)\) for every integer \(k\ge1\). Each whole \(P_k\) basin has entire clock image \((\log2)\mathbb Z\), so these are countably infinitely many distinct primitive log-two packets. The uniqueness target therefore fails. Factorization-OFF has the same fixed cores and times but different incoming; addition-OFF and count-cut-OFF have their own complete fixed ledgers. All histories, kernels, phases, terminal identities and repetitions remain. No higher-period census or modification of the frozen owner is used.

## 1. Full owner, question and lineage

The common carrier and original measure are
\[
X=\mathbb N_0^2\times[0,1],\qquad
\mu=\#_{\mathbb N_0^2}\otimes du. \tag{1}
\]
Use discrete/product Borel structure. Write \(X_0=\{(0,0,u):0\le u\le1\}\), \(X_+=X\setminus X_0\). All \(X_0\) states are terminal, with no outgoing step, not identity loops. Both endpoints, all cuts, units and zero-count axes remain.

For \((a,b,u)\in X_+\), define
\[
p=\frac a{a+b},\qquad
B(a,b)\iff 2\le b<a\ \hbox{and}\ b\mid a,\qquad
R(a,b)=(a+b,b),\quad
F(a,b)=\begin{cases}(b,a/b),&B(a,b),\\ (b,a),&\neg B(a,b).\end{cases} \tag{2}
\]
For a cut \(p\in(0,1)\), red means \(0\le u<p\), blue means \(p\le u\le1\). At \(p=1\) the entire CLOSED interval is red, with blue empty; at \(p=0\) it is blue, with red empty. The corresponding interval updates are \(u/p\) and \((u-p)/(1-p)\), respectively, using a denominator only on a nonempty side.

| Owner | Cut | Red count update | Blue count update |
| --- | --- | --- | --- |
| M MAIN | \(a/(a+b)\) | \(R\) | \(F\) |
| C factorization-OFF | \(a/(a+b)\) | \(R\) | \((b,a)\) |
| A addition-OFF | \(a/(a+b)\) | \((a,b)\) | \(F\) |
| U count-cut-OFF | \(1/2\) on every \(X_+\) component | \(R\) | \(F\) |

Each owner is its own partial map \(T:X_+\to X_+\). Indeed each listed count update remains nonempty; under \(B\), both factor outputs are positive integers. The stated interval branches stay in \([0,1]\). Thus every nonempty-count source has all forward iterates; no source can enter \(X_0\). In U, a zero red or blue count does not remove either side. The countably many fixed-count affine pieces show that each map is Borel.

At integer counts \((N,D)\), \(1<D<N\), the factor permission is exactly \(D\mid N\). It executes the equality \(N=D(N/D)\), not a prime predicate or a stored static test label. The count pair is updated and determines the next geometric cut. Failed permissions perform their actual swaps. This realizes divisor-symbolic admissibility \(\to\) changing integer action \(\to\) geometric cut feedback. The ratio choice is declared design, not a canonical measure theorem or a conservative/symplectic lift.

The frozen question is the GLOBAL fixed set of each full owner, with its entire incoming and clock ledger. A MAIN nonprime primitive or repeated prime packet stops the target. No absence of higher-period phenomena will be inferred from this gate.

## 2. Exhaustive inverse atlas and all-point IMAGE

For target \(t=(c,d,v)\), all possible integer predecessors are:

| Owner/side | Predecessor \((a,b)\) | Exact count constraints |
| --- | --- | --- |
| M/C red | \((c-d,d)\) | \(c>d\ge0\) |
| A red | \((c,d)\) | \(c>0,d\ge0\) |
| M/A blue-factor | \((cd,c)\) | \(c,d\ge2\) |
| M/A blue-swap | \((d,c)\) | \(c>0,d\ge0,\neg B(d,c)\) |
| C blue | \((d,c)\) | \(c>0,d\ge0\), no \(B\) exclusion |
| U red | \((c-d,d)\) | \(c\ge d\ge0,c>0\) |
| U blue-factor | \((cd,c)\) | \(c,d\ge2\) |
| U blue-swap | \((d,c)\) | \(c,d\ge0,c+d>0,\neg B(d,c)\) |

For M/C/A, compute \(p\) at that predecessor. A red inverse has
\[
u=pv,\quad v\in[0,1)\text{ if }p<1,\quad v\in[0,1]\text{ if }p=1; \tag{3}
\]
a blue inverse has \(u=p+(1-p)v,\ v\in[0,1]\). For U the corresponding inverses are \(u=v/2,\ v\in[0,1)\), and \(u=(1+v)/2,\ v\in[0,1]\). Every row is a Borel injective map between the specified counting components. Retain the actual source-side and forward-equality checks, including at endpoints.

**Proposition 1.** These are all actual inverse branches, with no branch to an empty-count target. At every point of an actual branch,
\[
j_\theta=
\begin{cases}
p,&\text{M/C/A red},\\
1-p,&\text{M/C/A blue},\\
1/2,&\text{U either side},
\end{cases}
\qquad
\mu(\theta E)=\int_E j_\theta\,d\mu \tag{4}
\]
for every Borel subset \(E\) of that branch domain.

**Proof.** Solving the red count equations gives the first, second and sixth rows. In M/C/A the red side is nonempty iff \(a>0\); in U it is nonempty at every nonempty count state. This gives exactly the stated inequalities. Solving a factor target gives \(b=c,a=cd\). Its permission is precisely \(c,d\ge2\). Solving a swap target gives \(a=d,b=c\); its nonempty blue side requires \(c>0\) in M/C/A, but not in U. The original \(B\) exclusion is required exactly when the owner would otherwise have used its factor branch. This proves both necessity and sufficiency of the count rows.

The affine interval equations give (3) and its blue counterpart. In particular an interior-cut red source cannot map to \(v=1\); a blue source can, and \(p=1\) red must retain that endpoint. The interval restrictions give the actual sides, and substitution gives the target. Every source uses exactly one side and one count rule, so no other predecessor is possible. None of the count rows accepts \((c,d)=(0,0)\).

The source and target singleton count labels each have counting mass one. Each inverse interval germ has positive derivative equal to its displayed branch width. One-dimensional affine change of variables proves (4); endpoint and cut subsets are included as Borel restrictions, with the SAME analytic-germ value even when their Lebesgue measure is zero. Since every actual width is positive and at most one, all values are positive finite. Arbitrary countable chart decompositions follow by measure additivity. Neither an incoming-branch count nor a normalization of total incoming mass belongs in \(j_\theta\). \(\square\)

For \(z\in X_+\), set
\[
w(z)=j_{\text{actual inverse}}(Tz),\qquad
\kappa(z)=-\log w(z)\ge0. \tag{5}
\]
This is the inverse IMAGE clock, not the negative logarithm of the forward derivative. The forward interval derivative is \(1/w(z)\). On terminal sources \(\kappa\) is NOT DEFINED, because no step exists; their identity arrows will have clock zero. U has \(w=1/2\) at every nonterminal source. All versions are fixed at null points by (4), not by an a.e. completion.

## 3. Full actual histories, kernels and time

For each owner separately, \(D_0=X\) and \(D_r=X_+\) for \(r\ge1\). On \(D_r\), put
\[
W_0=1,\quad W_r(z)=\prod_{i=0}^{r-1}w(T^iz),\qquad
S_r(z)=-\log W_r(z). \tag{6}
\]
Each finite product is positive; no infinite-product clock is used. The retained-lag Borel groupoid is
\[
G_T=\{(z,r-s,w):z\in D_r,w\in D_s,T^rz=T^sw\},\qquad
c(z,r-s,w)=S_r(z)-S_s(w)
=\log\frac{W_s(w)}{W_r(z)}. \tag{7}
\]
Here the letter \(w\) in a triple denotes its source point, distinct from the step-width function in (5). Equal triples alone are identified; no free inverse-word labels are added. Each fixed-depth equality is Borel, so their countable union is Borel; the inverse atlas gives countable source/range fibres.

**Proposition 2.** Formula (7) is a well-defined additive cocycle, and each actual finite history-pair chart from \(w\) to \(z\) has IMAGE density \(e^{-c}\).

**Proof.** If two witnesses of one lag differ by \(h\ge0\) in both depths, the additional products begin at the same common future and cancel. At \(X_+\) all later iterates exist, so any two witnesses can be aligned. A terminal has no incoming and no outgoing, hence only its depth-zero identity, and causes no ambiguity. To compose two triples, align their shared-point depths; cancellation of that shared history yields the sum of clocks.

On fixed finite branch histories, \((T^r|_{\rm branch})^{-1}\circ T^s|_{\rm branch}\) is an affine interval chart between fixed count components, restricted to its actual Borel domain. Its derivative is \(W_r(z)/W_s(w)=e^{-c}\). Apply Proposition 1 successively, or ordinary affine change of variables on the whole restricted chart. This proves every-Borel IMAGE, including singleton endpoint charts, with the prescribed product germ. These countably many history charts cover all triples. The forward arrow \((Tz,-1,z)\) has \(c=-\kappa(z)\), fixing the orientation. \(\square\)

The exact full kernels, with witnesses as in (7), are
\[
\ker(\mathrm{lag})=\{r=s\},\qquad
\ker c=\{W_r(z)=W_s(w)\},\qquad
\ker(\mathrm{lag})\cap\ker c=\{r=s,\ W_r(z)=W_r(w)\}. \tag{8}
\]
These are tests on actual triples, independent of the chosen witnesses. For U, \(c=(r-s)\log2\) on the nonterminal part, so its clock and lag kernels coincide; terminal identity arrows are in both.

Keep the whole extension \(X\times\mathbb R_h\): an arrow sends \((w,h)\) to \((z,h+c)\). Height translation defines the owned real action on the orbit SET. No Hausdorff quotient, smooth flow or invariant physical probability is asserted.

For every source \(z\), a nonzero isotropy lag is equivalent to eventual entry into a finite cycle. Indeed \(T^rz=T^sz\), \(r>s\), exhibits such a cycle; conversely cycling supplies these equalities. If its least period is \(q\) and
\[
L=\sum_{i=0}^{q-1}\kappa(T^iP)\ge0,
\]
then exactly
\[
I_z=q\mathbb Z,\qquad c(z,kq,z)=kL,\qquad H_z=L\mathbb Z. \tag{9}
\]
Least source period gives precisely the lag multiples; transient sums cancel, giving the clock assertion. Extension isotropy is \(q\mathbb Z\) if \(L=0\) and trivial if \(L>0\). Without an eventual cycle, \(I_z=H_z=\{0\}\), including every terminal. These are full-source criteria, not a classification of longer cycles.

Fixing a reference in a source orbit identifies its extension orbit-set fibre with \(\mathbb R/H_z\); changes of reference use actual arrow-clock offsets. Thus \(L>0\) gives one entire physical translation orbit with primitive \(L\) and repeats \(jL\), \(j\ge1\). A zero-clock core retains its source isotropy but has real phases and no positive periodic time. Distinct source orbits are not merged by equal \(L\). The global height-action kernel is \(\bigcap_zH_z=\{0\}\) for all four owners because the retained terminal components have \(H_z=\{0\}\).

## 4. Exhaustive incoming and actual phase tests

Let \(\mathcal P_0(t)=\{t\}\) and, using ALL applicable rows of Proposition 1, define
\[
\mathcal P_{j+1}(t)=
\bigcup_{v\in\mathcal P_j(t)}\{\theta(v):v\in\operatorname{dom}\theta\}. \tag{10}
\]
Induction on \(j\), using the proved one-step completeness, gives exactly all legal depth-\(j\) predecessors. There is no label, depth, endpoint or count cutoff. In particular, a terminal has \(\mathcal P_j(t)=\varnothing\) for \(j\ge1\). All arrows incoming to range \(t\) are exactly
\[
\{(t,r-j,z):r,j\ge0,\ t\in D_r,\ z\in\mathcal P_j(T^rt)\}. \tag{11}
\]
Every actual witness occurs, and every listed triple has that witness. Inverses give all outgoing arrows. Compatible infinite incoming histories are exactly all sequences \(z_0=t,\ Tz_{i+1}=z_i\); none is selected or artificially completed.

Two source points are equivalent precisely when they have a legal common future. Extended points are equivalent precisely when some such witness also satisfies
\[
h_z-h_w=S_r(z)-S_s(w). \tag{12}
\]
Equations (10)–(12) constitute exact unrestricted incoming and phase tests on the entire source.

For any actual fixed point \(P\), set \(\ell_P=\kappa(P)\) and
\[
\mathcal B(P)=\bigcup_{N\ge0}\mathcal P_N(P),\qquad
\beta_P(z)=S_N(z)-N\ell_P\quad(T^Nz=P). \tag{13}
\]
The offset is independent of \(N\), since any extra steps occur at \(P\). The basin is exactly the whole source orbit of \(P\): a common future with a fixed point must equal that point. For any \(z,w\in\mathcal B(P)\), every integer lag \(k\) occurs by extending both histories sufficiently far after entry, and
\[
G_T|_{\mathcal B(P)}=\mathcal B(P)\times\mathbb Z\times\mathcal B(P),\qquad
c(z,k,w)=\beta_P(z)-\beta_P(w)+k\ell_P. \tag{14}
\]
This proves the ENTIRE fixed-basin kernels, isotropy and phases: lag kernel \(k=0\); clock kernel the zero of the right side; joint kernel both conditions; \(I_z=\mathbb Z\), \(H_z=\ell_P\mathbb Z\); extension isotropy \(\mathbb Z\) if \(\ell_P=0\), otherwise trivial; phase \([h-\beta_P(z)]\in\mathbb R/(\ell_P\mathbb Z)\). Distinct fixed points have disjoint such source orbits.

## 5. Complete global fixed sets of the four owners

Write
\[
Z_{a,t}=(a,0,t)\ (a\ge1,\ 0\le t\le1),\qquad
P_k=(k,k,1)\ (k\ge1),\qquad Q_{a,b}=(a,b,0)\ (a,b\ge1).
\]

**Theorem 3.** With no restriction of the carrier,
\[
\begin{array}{c|c|c}
\text{owner}&\text{ALL actual fixed states}&\text{own step clock}\\ \hline
M&\{Z_{a,t}\}\cup\{P_k\}&0\text{ on }Z;\ \log2\text{ on }P\\
C&\{Z_{a,t}\}\cup\{P_k\}&0\text{ on }Z;\ \log2\text{ on }P\\
A&\{Z_{a,t}\}\cup\{Q_{a,b}\}\cup\{P_k\}
&0\text{ on }Z;\ \log((a+b)/a)\text{ on }Q;\ \log2\text{ on }P\\
U&\{Z_{a,0}\}\cup\{P_k\}&\log2\text{ on every fixed state}.
\end{array} \tag{15}
\]
Terminals are absent from this table because no \(Tz=z\) equation exists there.

**Proof.** A red fixed point of M/C requires \((a+b,b)=(a,b)\), hence \(b=0,a\ge1\). Its cut is \(p=1\), so every \(t\in[0,1]\) is fixed with width one. For A, red leaves counts unchanged and requires \(u=u/p\). When \(b=0\), this again gives all \(Z_{a,t}\). When \(a,b>0\), it gives \(u=0\), which belongs to the red side, yielding exactly \(Q_{a,b}\). At \(a=0\) no red side exists.

A fixed point on a blue factor branch would require \(b=a\) from its first count coordinate, contradicting \(b<a\). On a blue swap branch, equality of counts forces \(a=b=k\ge1\); all these states fail \(B\) and have cut \(1/2\). The interval equation \(u=2u-1\) forces \(u=1\), which is retained. This yields exactly \(P_k\) for M/A; C has the same own swap calculation without a \(B\) guard. If precisely one count is zero, swapping cannot fix the counts.

For U, the red count equation still forces \(b=0,a\ge1\), but its own interval equation is \(u=2u\), hence \(u=0\), an actual red point. Its blue factor/swap equations give exactly the same \(P_k\); no extra zero-count blue state is fixed. The widths from (4) give all clocks in (15). The cases exhaust both sides, including cuts and endpoints. \(\square\)

The \(P_k\) are null endpoint states, but their clocks are determined by the frozen affine inverse germs. Replacing \([0,1]\) by \([0,1)\), declaring endpoint values arbitrary, or choosing one count representative would change the owner.

## 6. All fixed-core basins and control comparison

Equations (10) and (13)–(14), with the explicit rows of Proposition 1, give full-X incoming, ENTIRE \(H\), kernels, all phases and repetitions for EVERY fixed state in (15). The following first-step evaluations clarify the differences; higher incoming is always the complete recursion, not a selected subtree.

For M/C/A, every \(Z_{a,t}\) has exactly the two one-step predecessors
\[
Z_{a,t},\qquad (0,a,t). \tag{16}
\]
The second point has no predecessor under these owners: its target first count is zero, excluding all their inverse rows. Hence its complete basin is exactly those two points; all actual steps have width one and \(\beta=0\). Its whole \(H\) is zero, its source/extension isotropy is \(\mathbb Z\), and all real phases remain.

For C, \(\mathcal P_1(P_k)=\{P_k\}\), since its red row requires \(c>d\); therefore its entire \(P_k\) basin is a singleton. For M, A and U,
\[
\mathcal P_1(P_k)=
\begin{cases}\{P_1\},&k=1,\\
\{P_k,(k^2,k,1)\},&k\ge2.
\end{cases} \tag{17}
\]
The red rows fail either their count condition or the strict target-endpoint condition \(v<1\); the two blue rows give exactly (17). Thus C and MAIN do NOT have identical incoming when \(k\ge2\), despite equal fixed cores and their primitive times.

For A, the other positive fixed core \(Q_{a,b}\) has its red self-predecessor, additionally
\[
(ab,a,b/(b+1))\quad\text{if }a,b\ge2,\qquad
(b,a,b/(a+b))\quad\text{if }\neg B(b,a). \tag{18}
\]
These are precisely the factor and swap inverse rows at target \(v=0\), with their actual source cuts. For U, \(Z_{a,0}\) has exactly
\[
Z_{a,0},\qquad (0,a,1/2) \tag{19}
\]
as one-step predecessors. In (17)–(19), iterate (10) without restriction to obtain all finite depths, and retain all compatible infinite histories. Proposition 2 and (14) supply their true offsets; clocks are not copied between these different owners.

In MAIN, every \(\mathcal B(P_k)\) has ENTIRE \(H=(\log2)\mathbb Z\), source isotropy \(\mathbb Z\), trivial extension isotropy, phase circle \(\mathbb R/(\log2)\mathbb Z\), primitive \(\log2\), and repeats \(j\log2\). Distinct \(k\)'s cannot have a common future because each core is fixed; no incoming tree can merge them. Therefore the fixed gate alone supplies exactly countably infinitely many positive MAIN packets, all of primitive \(\log2\). This statement is limited to packets whose core is fixed, not the entire higher-period ledger.

C supplies its own countably infinite family with the same primitive times and singleton positive basins. A has each \(P_k\) and every \(Q_{a,b}\) as a separate positive packet of the time in (15), with its full basin and phases from (14). For example, its OWN \(Q_{2,1}\) has primitive \(\log(3/2)\), not an ordinary-prime logarithm; this is not a MAIN counterexample. U has distinct positive packets for every \(Z_{a,0}\) and \(P_k\), all of primitive \(\log2\), with no merging of the two families.

## 7. Decisive target failure and limits

MAIN's positive ledger is nonempty, and its necessary one-packet-per-prime condition is REFUTED: \(P_1\) and \(P_2\) already give different entire packets of primitive \(\log2\), and all \(k\ge1\) remain. This failure is not the terminal ledger, not a zero-clock argument, and not an assumed finite-index proxy.

The factor permission is false on every \(P_k\) because its counts are equal. Factorization-OFF consequently reproduces the positive fixed-core data. Yet MAIN executes genuine factorization on the incoming state \((k^2,k,1)\) for \(k\ge2\), so the arithmetic is not globally absent and the full histories are not identified with C. This gate fails to make the desired prime specificity depend on factorization.

No MAIN nonprime primitive is established here. MAIN's global prime-only purity, all-prime coverage, higher-period structure, strong naturalness and PROVES_TOO_MUCH remain OPEN. Count-cut-OFF is an independently changed action, not a post hoc density repair. The result neither constructs a classical Hamiltonian/contact flow nor an operator, trace or zeta.

T0 and the same-original-measure all-point history obligations are established. Arithmetic T1 target success is NOT PASSED. Full T2 ledger accounting is not prime-target success. T3 NOT AUDITED; classical fields NOT APPLICABLE; formal coordinates UNASSIGNED; Route B NOT INVOKED. Decision: STOP / FORK without changing counts, endpoints, measure, clock or packet convention. No higher-period search or round480 is added.

## 8. Reproducibility, access and declarations

The sole new scientific input was the [frozen card](candidate-card.md), personally read lines1–103 through measured EOF, SHA-256 0ed468c07a3ccf3f84806aa5bfbabe89ad12b08cc716c465e3bc0093e012fc03. Root reported full CP1 PASS and issued DISTINCT AUTHOR RELEASE. No scope file, raw proof, reviewer report, peer answer or old proof was read. No helper was used. All proofs here were derived after that release.

Design-only collision reads were [364 card](../364-symbolic-index-branching-gate/candidate-card.md) lines1–65 and [370 card](../370-divisor-renewal-clock/candidate-card.md) lines1–64, both non-EOF, each full file mechanically measured at123 lines. Their prefix SHA-256 values were 0a11e12d6450d01be979910a63f0ac5d38a5c6abfd1e34e325f3f3f6b40c342c and 0c98c2a33ae3f989da2412380fc8911f30c8f0f4e55ccb382b1a44f8db5557b4. Heading discovery also exposed appended Outcome TITLES at364 line115 and370 line114, not their bodies. 364 specifies an abstract reciprocal-index path class;370 specifies a residual renewal law. Neither supplies this count-feedback proof. No global novelty or nonconjugacy is claimed.

Earlier364 reviewer participation and370-batch context remain shared history. Scout/root informally considered inverse and endpoint-fixed feasibility before freeze: this is not blind, outcome-sealed preregistration. ARS supplies bounded scope, proof/evidence separation, drafting and disclosure discipline; its applicable router/workflows and retained author instructions were read, alongside the local paper template. The frozen card, not an expanded generic pipeline, controls this deliverable.

Methods are exact algebra, integer case exhaustion, affine change of variables and finite-history induction. File checks use bounded sed/nl reads, line counts, SHA-256, identity/link/control-character checks and full EOF self-reading. No scientific code, numerical search, network/API, Git mutation, old-file edit, PDF or external publication was used. Only paper.md, README.md and claim-ledger.md are author writes; root owns card outcome and integration.

Evidence: [card](candidate-card.md), [claim ledger](claim-ledger.md), [overview](README.md). Data availability: local frozen definitions and the self-contained proofs above; no empirical dataset. Ethics: no human participants, personal data or animal subjects. Contributions: AI agents supplied design, mathematical derivation and drafting; root coordinates separate internal review. Same-model/shared-history work is NOT_CALIBRATED; no human, external or cross-family verification is certified. Funding and conflict information were not supplied and are not invented. No submission-readiness or formal Route claim is made.
