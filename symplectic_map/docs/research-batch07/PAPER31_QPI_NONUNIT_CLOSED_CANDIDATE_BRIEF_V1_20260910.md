# Paper31 complete candidate brief: integral extensions and residue lattices at nonunit time

Date: 2026-09-10 UTC. Prepared by `/root` for one complete-candidate review, not as a manuscript or an admission decision.
`COMPLETE_CANDIDATE_BRIEF / C1–C3_UNDIVIDED / MATHEMATICS_ACCEPTED / ADMISSION_OPEN`.
`route_applicability: NOT_APPLICABLE`.

## 1. Decision to be made

The candidate studies all anticanonical powers of the original eight-blowup qPI family at fixed $q=1$ over $R=\mathbb Z[\tau]$.
It connects the entire marked adjacent extension system with an explicit integral residue lattice and arithmetic invariants of the same cohomology module.
The question is whether this complete, proved structure has sufficient novelty, independent scientific value, proof confidence, and natural substance for a standalone paper under the unchanged 22–30-page contract.
Neither the need for a fifth paper nor the amount of prior work is evidence for any gate.

The [preflight disposition][PRE] preserves the latest [C/D review][CD]: novelty **7.0/10**, independent value **7.0/10**, **CAUTION**.
Its strongest objection is that, after standard mechanisms are deducted, the remaining contribution may be a technically competent calculation and identification for one fixed arithmetic surface family.
This objection must accompany the candidate; it is not answered merely by assembling a longer input packet.
The [older I05 review][OLDCD] remains 6.5/CAUTION for its then-unclosed package. Neither score is retrospectively changed.

The manuscript, project directory, source/publication locks, and PDF do not yet exist. No trial prose or page measurement has been performed.
This brief specifies a complete mathematical object and its outputs, not a section plan and not a shortened substitute for the original proofs.

## 2. The exact geometric object

Start with $X=\mathbb P^1_R\times_R\mathbb P^1_R$ with affine coordinates $x,y$ and the original four clusters of $1+2+3+2$ section blowups:

1. Blow up $(x^{-1},y-1)=(0,0)$.
2. Blow up $(x,y^{-1})=(0,0)$, then $(u,\xi)=(0,\tau)$ in $x=u\xi,y=u^{-1}$.
3. Blow up $(x,y)=(0,0)$, then the first exceptional divisor's intersection with $y=0$, then $(u,\xi)=(0,\tau)$ in $x=u\xi,y=u^2\xi$.
4. Blow up $(x^{-1},y^{-1})=(0,0)$, then $(u,\xi)=(0,1)$ in $x=(u\xi)^{-1},y=u^{-1}$.

The cluster order is retained. The four first supports on $X$ are disjoint even if some later coordinate values agree.
Let $S/R$ be the resulting surface and $\mathscr L=\omega_{S/R}^{-1}$.
The intermediate surface $Y$ is obtained after the four node blowups: the first in cluster 2, the first two in cluster 3, and the first in cluster 4.
Residues are computed on $Y$; the cohomology below is on $S$. The [JET][JET] pushforward and evaluation-cone proof supplies their actual connection.
$\tau=0$ is part of the integral surface family; it is not an extension of invertible dynamics to zero time.

For $n\ge0$, define
$$M_n=H^1(S,\mathscr L^n),\qquad T_n=\ker(M_n\to M_n[1/\tau]),\qquad L_n=M_n/T_n,\qquad E_n=L_n^{**}/L_n.$$
All duals here are over $R$. The letters $L_n,M_n$ used for line bundles in older JET notation must not be confused with these modules.
Set $A_n=R[u,v]/(u,v)^n$ with $A_0=0$, $W_n=A_n^{\oplus4}$, and
$$V_n=R\langle x^iy^j:(i,j)\in\Lambda_n\rangle,$$
$$\Lambda_n=\{(i,j):0\le i,j\le2n,\ n+i-j\ge0,\ i+j\ge n,\ i+2j\ge2n,\ i+j\le3n\}.$$
In the actual anticanonical frames the four evaluations of $x^iy^j$, before truncation, are
$$\begin{aligned}
Q_{1,n}&=u^{2n-i}(1+v)^j,&Q_{2,n}&=u^{n+i-j}(\tau+v)^i,\\
Q_{3,n}&=u^{i+2j-2n}(\tau+v)^{i+j-n},&Q_{4,n}&=u^{3n-i-j}(1+v)^{2n-i}.
\end{aligned}$$
They define $J_n:V_n\to W_n$. JET proves the actual derived identity
$$R\Gamma(S,\mathscr L^n)\simeq[V_n\xrightarrow{J_n}W_n],\qquad
\operatorname{rank}V_n=2n(n+1)+1,\quad\operatorname{rank}W_n=2n(n+1).$$
It also proves the same geometric complex after arbitrary base change. That statement does not automatically preserve later short exact sequences under nonflat base change.

## 3. C1: the entire marked adjacent extension system

Keep the original sections
$$s_0=xy,\qquad s_1=x^2-x^2y+xy^2-\tau y.$$
For every $n\ge0$, multiplication by $s_0$ gives a degreewise injective map of the original complexes.
The [D05][EXT] proof determines the quotient complex, lifts its $H^0$ generator by $s_1^{n+1}$, and obtains
$$H^0(S,\mathscr L^n)=\bigoplus_{i=0}^n R s_0^{n-i}s_1^i,$$
$$0\longrightarrow M_n\xrightarrow{\iota_n}M_{n+1}\longrightarrow
R\oplus\bigoplus_{r=2,3}\bigoplus_{a=1}^{n}R/(\tau^{n+1-a})\longrightarrow0.\tag{C1a}$$
The free quotient summand has a specified split lift; its existence does not split the torsion quotient summands.
For $m=n+1-a$, the new target class $y_{r,a}^{(n+1)}=[u^a]_{r,n+1}$ has the actual relation
$$\tau^m y_{r,a}^{(n+1)}=\iota_n(e_{r,a}^{(n)}),\qquad
e_{r,a}^{(n)}=\left[u^{a-1}\sum_{b=0}^{m-1}(-1)^b\tau^{m-1-b}v^b\right]_{r,n}.\tag{C1b}$$
The class of this expression in $M_n/\tau^mM_n$ is the complete marked Ext class of that cyclic quotient component.
The sequence (C1a) is nonsplit for every $n\ge1$; $n=0$ is retained as its separate base case.

C1 includes D05's integer recovery of an arbitrary old jet class: compute and subtract the specified target lifts of its cyclic and free quotient coordinates, lift the remaining compatible four-edge data in the actual restricted source, subtract its actual $J_n$ image, divide by the original multiplication map, and descend strictly in degree.
All divisions are the specified exact integer divisions; the proof retains shared vertices and sufficiency of the compatibility condition.
This is a closed marked recursion for entire modules, not a canonical block classification and not a claim that $M_n$ has an $R[u,v]$-module structure.

## 4. C2: the original residue lattice and its complete defect

For $n\ge1$, $N=n-1$ and $0\le a\le N$, put
$$I_{n,a}=\left(\binom{N-b}{a}\tau^b:0\le b\le N-a\right)\subset R.$$
The [G][G] proof constructs the residue map from the four original centers and anticanonical frames, proves it kills $J_n$, and identifies the entire localized cokernel:
$$\rho_n:M_n[1/\tau]\xrightarrow{\sim}R[1/\tau]^n,\qquad
\rho_n(M_n)=\tau^{-n}\bigoplus_{a=0}^{n-1}I_{n,a},\qquad\ker(\rho_n|_{M_n})=T_n.\tag{C2a}$$
Thus $\widetilde\rho_n=\tau^n\rho_n$ gives the specified integral identification
$$L_n\simeq\bigoplus_a I_{n,a},\qquad I_{n,a}^{**}=R,\qquad E_n\simeq\bigoplus_aR/I_{n,a}.\tag{C2b}$$
Each $E_n$ is a finite abelian group. In unnormalized residue coordinates the original map is right shift;
in the displayed ideal coordinates it is **$\tau$ times right shift**. The comparison with the old compatibility functional is
$$(-1)^{n-1}\tau^n\rho_{n,0}=\Psi_n.$$

The actual geometric work includes all four common zeros, no omitted boundary intersections, canonical signs, the tight applicability of the compact-surface residue theorem, localized rank and actual surjectivity, and the integer simultaneous normal form
$$F=U(\tau+V),\qquad G=V.$$
The formal coordinate change is invertible and its Jacobian is a unit on the full fat-jet target, not merely on the restricted source image.
The good-chart images are included in the full bad-chart image before equality is concluded.

For each prime $p$, let $A_p=R_{(p,\tau)}$ and $d=N-a$. The [integer consumer lemma][BIN] also gives the entire coefficient-layer description
$$e_b=\min_{0\le j\le b}v_p\binom{N-j}{a}\quad(0\le b<d),\qquad
A_p/I_{n,a}A_p\simeq\bigoplus_{b=0}^{d-1}\mathbb Z_{(p)}/(p^{e_b})\cdot\tau^b.\tag{C2c}$$
This is an additive $\mathbb Z_{(p)}$-module decomposition with $\tau$ acting by the adjacent natural projections and killing the last term.
It preserves mixed-characteristic thickness and the parameter action, not just a mod-$p$ dimension.

## 5. C3: global Fitting ideals and all-characteristic lengths

Set $B_n=\sum_{j=1}^{n-1}j^2$ for $n\ge1$ and $B_0=0$, and
$$d_p(N,a)=\min\{0\le b\le N-a:p\nmid\binom{N-b}{a}\},\qquad D_n(p)=\sum_{a=0}^{n-1}d_p(n-1,a).$$
The [merged arithmetic theorem][A] proves on the original $R$-module, not just after passing to a field,
$$\operatorname{Fitt}_j(M_n)=0\quad(0\le j<n),\qquad
\operatorname{Fitt}_n(M_n)=\tau^{B_n}\prod_a I_{n,a}.\tag{C3a}$$
The proof uses the entire original kernel and a unit-triangular complement to obtain the actual resolution
$$0\to R^{n(2n+1)}\to R^{2n(n+1)}\to M_n\to0.$$
The [determinant lemma][DET] is applied to the natural torsion quotient and its correctly normalized double dual.
It retains height-two ideal information, not just a height-one divisor. Equality is then checked at all prime points to obtain (C3a) globally.

For every field $k$, with $M_{n,k}=M_n\otimes_Rk[[\tau]]$, the free rank is $n$ and
$$\ell_{k[[\tau]]}\operatorname{tors}_{\tau}M_{n,k}=
\begin{cases}B_n,&\operatorname{char}k=0,\\B_n+D_n(p),&\operatorname{char}k=p>0.\end{cases}\tag{C3b}$$
This is the torsion of the specialized original module, not an assertion that specialization commutes with taking its original torsion submodule.
The proof verifies the relevant Tor vanishing for the true adjacent quotient, computes the image-lattice index with the actual shift, and subtracts that index before summing the torsion increments.

For each prime $p$, the first excess over the characteristic-zero length at the **same degree** occurs exactly at $n=p+1$, and equals $p-1$.
At this degree the original local ideal is
$$\operatorname{Fitt}_{p+1}(M_{p+1})A_p=\tau^{\sum_{j=1}^p j^2}(p,\tau)^{p-1}.$$
For every $n\ge1$ one has
$$D_n(p)=0\iff n/p^{v_p(n)}<p\iff E_n\otimes_RA_p=0\iff L_n\otimes_RA_p\text{ is free}.\tag{C3c}$$
All later length defects $D_n(p)$ are given by a terminating digit recursion. Write $H_p(N)=D_{N+1}(p)$, $H_p(-1)=0$,
$Z_p(h)=\prod_i(h_i+1)$ for the base-$p$ digits of $h$, and $Z_p(0)=1$. For $N=ph+r$, $0\le r<p$,
$$H_p(N)=p(r+1)H_p(h)+p(p-1-r)H_p(h-1)+(r+1)(p-1-r)(Z_p(h)-1).\tag{C3d}$$
The cases $n=0,1$, $p=2$, and recursion quotient $h=0$ are included in the original proofs.
At degree zero $M_0=T_0=L_0=E_0=0$, empty sums are zero, and the empty product and $\operatorname{Fitt}_0(0)$ are $R$; $V_0=H^0(S,\mathcal O_S)=R$ is not zero.

## 6. Complete proof responsibilities and actual status

The [mathematics disposition][MATH] accepts the actual D05/G/BIN/DET/A chain with its non-author checks, not merely compatible independent abstract lemmas.
Original author files retain their historical “awaiting review” text; their later scoped status is supplied by the dispositions, not by editing frozen source history.
DET's former unnormalized abstract-ideal corollary was corrected and independently checked; the current application supplies $I_{n,a}^{**}=R$ in the specified embeddings.

| Output / bridge | Existing complete proof responsibility |
|---|---|
| Original $S$ and actual cohomology complex | JET Steps 1–4: reorder the disjoint clusters, regular blowup charts and canonical change, arbitrary fat pushforward, four-node unit right inverses, final frames and evaluation cone, actual base change |
| C1, including entire kernel and recovery | D05 Steps 1–8, not just the formal long exact sequence or its dimensions |
| C2 and actual multiplication | G Steps 1–8, the actual JET/D05 inputs, and the precise global residue theorem with its hypotheses verified |
| Full coefficient layers and characteristic lengths | BIN Steps 1–6, including actual H1–H3 matching in A and the specialization/image/Tor distinction |
| First nonzero global ideal | DET's complete current normalized lemma, A's real resolution and local-to-global argument |
| All-degree arithmetic statements | A Steps 3–5 plus BIN's integer coefficient and digit proofs |

The two [C1][IC] and [G][IG] consumer inventories locate the existing upstream proofs without creating new ones.
The complete proof map prepared alongside this brief is an index to those proofs, not permission to omit them.
The old unit-time cohomology/trace/Hasse/Jacobian chain is not an upstream dependency of this selected proof.
Standard general tools must be correctly stated and applied; all topic-specific necessary proofs remain in the future body.

The exact fixed $n=4$ integral block and D05's $4\to5$ prime-3 pullback/pushout example remain accepted contextual checks, not extra pillars of the complete candidate.
They are not required by any all-degree proof, do not add novelty credit, and are not mandatory material to fill the body.
If a later manuscript elects to state an optional result, it must retain that result's actual scope and proof; no old certificate is silently repurposed as a full classification.

## 7. Prior-art deductions, portfolio delta, and strongest limitation

The [Phase B disposition][PB] and its four complete source/portfolio reports record bounded searches, actual primary reading, and failures.
No globally exhaustive search or exclusion theorem is claimed.

| Existing mechanism or baseline | What is deducted; what is still being evaluated |
|---|---|
| Full Pascal equivalences; principal-parts/Taylor transition formulas | Binomial manipulations and the abstract row-independent image calculation are standard. The original restricted four-cluster Ext system and the full integral comparison to that image are the remaining object-specific work. |
| Global and toric residues; formal inverse coordinates | Residue theory and coordinate inversion are not new. G supplies the actual four centers, frames, signs, full Jacobian action, quotient identification, and integer image. |
| Double duals, Fitting ideals, complementary minors, Lucas/Fine digits | These are tools, not separate innovations. C3 is a unified consumer of the same original lattice and adjacent sequence. |
| 2024/2025 principal-parts/cohomology recursions | A strong all-degree positive-characteristic precedent, including double-graded multiplication interfaces. An exact map matching original source, quotient, truncation, $\tau$ action, and $s_0$ has not been supplied; neither its existence nor its nonexistence is asserted. |
| 2026 reflexive-defect and first-Fitting work; Ohm | The general determinant/defect mechanism receives no novelty credit. Full-text inclusion remains unresolved; failure of one visible primary-height-one hypothesis does not exclude all other results. |
| Original JET, zero-time dimensions, second/third degree and fixed M4 | All are established baseline. The current claims are the new closed all-degree structures, not the first observation of nonfreeness, a defect, or a length jump. |
| P18/P29/P30 | General Fitting/base-change tools, digit selection, and the unit-time computation are deducted. The actual compared results do not presently supply the complete nonunit integer lattice and marked connection; a unit cannot be sent to zero by a base-change map. |

In particular the source report explicitly computes a Taylor map with image $\bigoplus I_{n,a}$ and shows its multiplication rule is the same $\tau$-shift.
The candidate cannot count “lattice + shift + double dual” as three new methods.
C1 does contain marked extension information not recoverable from C2/C3 alone; however C3 does not consume every Ext class individually.
Its full value is evaluated as structural information, not as a claimed collection of independent applications.

The source gaps in Hadjirezaei/Ohm full texts, the Perkinson diagram, other limited passages, and Scholar/S2 access are retained exactly as reported.
Reading a source report is not the reviewer's personal full reading of all papers it cites.
The strongest objection remains the fixed-family/application character of the result; unresolved stronger goals cannot be borrowed to raise its score.

## 8. Nonclaims and unchanged admission contract

No claim is made of $M_n=T_n\oplus L_n$, the old strong block conjecture (P), every Smith exponent, every higher Fitting ideal, arbitrary $q$, a nonadditive classification, or reversible zero-time dynamics.
Specified pullbacks/pushouts are not asserted to be direct summands of the original module.
The three claims above belong to one construction, with no target-zero fitting, parameter mixing, changed thresholds, or cross-family additions.
No numerical experiment, CAS run, Lean formalization, or actual manuscript/PDF verification substitutes for these paper proofs.

Each of two fresh non-author reviewers must personally assess all four gates on the same complete scientific input, even if an earlier gate fails:
novelty at least 7.5/10, independent scientific value at least 7.5/10, complete proof confidence at least 9/10, and a credible natural-body-capacity PASS.
Capacity means anonymous English, single column, 11pt article, letter paper, 1 inch margins, ordinary spacing, **22–30 pages of complete substantive body**, with references separate.
Report low/central/high estimates by actual necessary proof modules, explaining both under- and over-window risk; they are estimates, not measured or rigorous bounds.
Do not use file counts, source line counts, accumulated effort, padding, narrower claims, smaller typography, appendices for necessary proofs, split papers, or trial layouts.
There is no additional rule that the central estimate itself must lie inside the window. P30's later 40-page exception does not apply here.

Each reviewer gives their own conjunction, and admission requires both complete conjunctions. Scores are not averaged, rounded into a pass, calibrated, or selected by taking different reviewers' best gates.
Historical source and mathematical contacts are disclosed; the two current reports remain mutually unseen until submission.
Unavailable GPT-5.4 MCP is not claimed to have run; use of the available Codex reviewer is not cross-model verification or human certification.
Submission freezes each report; factual clarification must not silently become a new favorable vote.

[PRE]: PAPER31_QPI_NONUNIT_CLOSED_PREFLIGHT_DISPOSITION_V1_20260910.md
[CD]: PAPER31_QPI_NONUNIT_CLOSED_NOVELTY_CD_V1_20260910.md
[OLDCD]: PAPER31_QPI_NOVELTY_CD_I05_I09_V1_20260909.md
[JET]: PAPER30_QPI_NONUNIT_TAU_ALL_DEGREE_JET_COMPLEX_V1_20260909.md
[EXT]: PAPER31_QPI_NONUNIT_ADJACENT_EXTENSION_DIAGNOSTIC_V1_20260909.md
[G]: PAPER31_QPI_NONUNIT_LATTICE_CONTROL_LEMMA_V1_20260909.md
[BIN]: PAPER31_QPI_NONUNIT_BINOMIAL_CONSUMERS_LEMMA_V1_20260909.md
[DET]: PAPER31_QPI_NONUNIT_DETERMINANT_IDEAL_LEMMA_V1_20260909.md
[A]: PAPER31_QPI_NONUNIT_ALL_DEGREE_ARITHMETIC_THEOREM_V1_20260909.md
[MATH]: PAPER31_QPI_NONUNIT_ALL_DEGREE_MATHEMATICS_DISPOSITION_V1_20260910.md
[IC]: PAPER31_QPI_NONUNIT_C1_PROOF_CONSUMER_INVENTORY_V1_20260910.md
[IG]: PAPER31_QPI_NONUNIT_G_PROOF_CONSUMER_INVENTORY_V1_20260910.md
[PB]: PAPER31_QPI_NONUNIT_CLOSED_PHASE_B_DISPOSITION_V1_20260910.md
