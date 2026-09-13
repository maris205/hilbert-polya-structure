---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--23-hamiltonian-quartic-spectral-escape"
canonical_tex: "symplectic_map/papers/23-hamiltonian-quartic-spectral-escape/paper/main.tex"
canonical_pdf: "symplectic_map/papers/23-hamiltonian-quartic-spectral-escape/paper/main.pdf"
source_sha256: "1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Four-Mode Hamiltonian Product Shears Beyond Cubic Collapse: Exact Degree Growth and Quartic Perron Subfamilies

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/23-hamiltonian-quartic-spectral-escape>)
- [规范 TeX](<../../../../../symplectic_map/papers/23-hamiltonian-quartic-spectral-escape/paper/main.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/23-hamiltonian-quartic-spectral-escape/paper/main.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/23-hamiltonian-quartic-spectral-escape/notes/CLAIMS_EVIDENCE_MATRIX.md>)
- [BibTeX](<../../../../../symplectic_map/papers/23-hamiltonian-quartic-spectral-escape/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $K$ be an arbitrary field of characteristic zero and let $g\geq10$ be an integer. We determine the exact degree growth of a positive-sign polynomial symplectic automorphism on $K^8$, obtained by composing two gradient shears whose product potentials each carry two pure-power spikes. The eight gradient supports yield four competitive choices. We construct one explicit sufficient invariant ratio cone, verify its six walls by hand, and prove that the selected pure branches win in both phases. Separate temporal carry inequalities and positivity of all forward coefficients show that the resulting weighted degrees are actual coordinate degrees, with no cancellation. If $A_g$ and $B_g$ are the two selected phase matrices and $C_g=B_gA_g$, then strict $q_4$ visibility for $n\geq1$ holds, the tied identity case at $n=0$ is handled directly, and $$\deg(F_g^n)=\mathbf{e}_4^{\mathsf{T}}C_g^n\mathbf{1}
  \qquad(n\geq0).$$ We derive all principal minors of $C_g$, its quartic characteristic polynomial, and the induced order-four scalar recurrence. Positivity gives $\lambda_1(F_g)=\rho(C_g)$. Reduction modulo five proves that the parameters $g=13,18,23,\ldots$ form a certified residue-class quartic Perron subfamily of pairwise distinct values. Finally, a common-kernel calculation explains why this support profile has no forced unit eigendirection, while making no classification claim. All arguments are finite, explicit, and independent of analytic assumptions.
author:
- Anonymous
bibliography:
- references.bib
title: 'Four-Mode Hamiltonian Product Shears Beyond Cubic Collapse: Exact Degree Growth and Quartic Perron Subfamilies'
```

## Markdown 正文

# Introduction {#sec:introduction}

The degree of an iterate of a polynomial automorphism is easy to bound from the degrees of its displayed coordinate polynomials and often difficult to compute exactly. Composition repeatedly exposes several possible outer monomials. A matrix obtained by choosing one support exponent per row describes the correct degree dynamics only if those choices remain strict along the orbit, fresh nonlinear terms beat the coordinates carried from the preceding phase, and the selected leading forms survive algebraically. Each of these requirements is visible in the four-mode Hamiltonian product shears studied here.

Fix an arbitrary field $K$ of characteristic zero. For an integer $g\geq10$, write $q=(q_1,q_2,q_3,q_4)$ and $p=(p_1,p_2,p_3,p_4)$, and consider $$\label{eq:intro-potentials}
\begin{aligned}
V_g(q)&=q_1^2q_2^2q_3^2q_4^2+q_1^g+q_2^{g-1},\\
W_g(p)&=p_1^2p_2^2p_3^2p_4^2+p_3^{g-1}+p_4^g.
\end{aligned}$$ The positive gradient shears and their prescribed order are $$\label{eq:intro-map}
S_g^+(q,p)=(q,p+\nabla V_g(q)),\qquad
T_g^+(q,p)=(q+\nabla W_g(p),p),\qquad
F_g=T_g^+\circ S_g^+.$$ Both shears are polynomial automorphisms preserving the standard symplectic form. The main issue is not invertibility or symplecticity, but the exact competition among the mixed product derivative and the four pure derivative branches under repeated composition.

For the displayed fixed positive-sign four-mode family, the selected first- and second-phase matrices are $$\label{eq:intro-phase-matrices}
A_g=
\begin{pmatrix}
g-1&0&0&0\\
0&g-2&0&0\\
2&2&1&2\\
2&2&2&1
\end{pmatrix},
\qquad
B_g=
\begin{pmatrix}
1&2&2&2\\
2&1&2&2\\
0&0&g-2&0\\
0&0&0&g-1
\end{pmatrix}.$$ The complete-step matrix $C_g=B_gA_g$ is genuinely four-dimensional. Unlike an endpoint-spiked support pattern with a common negative eigenspace for the two phases, the shifted kernels of $A_g$ and $B_g$ here are disjoint. This observation is explanatory, not a separate realization theorem: exact degree growth still requires the selector, cone, carry, survival, and visibility proofs below.

The article makes exactly four contributions.

1.  It gives the fixed positive-sign four-mode family, proves polynomial symplecticity directly, establishes the four strict phase selectors, and derives the exact complete-step matrix $C_g=B_gA_g$.

2.  It provides one explicit sufficient invariant ratio cone, proves all six walls and both temporal carries, establishes characteristic-zero leading-form survival and seven-competitor visibility, and obtains $\deg(F_g^n)=\mathbf{e}_4^{\mathsf{T}}C_g^n\mathbf{1}$ for every $n\geq0$.

3.  It hand-derives the characteristic quartic, the scalar recurrence, $R_g(1)$, and the equality $\lambda_1(F_g)=\rho(C_g)$.

4.  It gives the complete modulo-five certificate, an infinite pairwise-distinct quartic Perron subfamily, and the restricted $g=9$ boundary for the ordinary seed and selected itinerary.

These statements are deliberately bounded. They concern the displayed signs, coefficients, supports, and composition order in characteristic zero. They do not cover arbitrary coefficients, arbitrary shear words, other sign patterns, or positive characteristic. The ratio cone is a sufficient certificate, not a largest or necessary chamber. Irreducibility is proved only on one residue class, and the spectral-radius identity is not an assertion about entropy.

The proof is organized in the order demanded by the iteration. Section [2](#sec:related){reference-type="ref" reference="sec:related"} positions the result within a bounded literature neighborhood. Section [3](#sec:family){reference-type="ref" reference="sec:family"} records the family, the direct symplectic calculation, and the main theorems. Sections [4](#sec:supports){reference-type="ref" reference="sec:supports"}--[6](#sec:degree){reference-type="ref" reference="sec:degree"} prove support selection, cone invariance, carry, survival, and visibility. Section [7](#sec:spectrum){reference-type="ref" reference="sec:spectrum"} derives the quartic and recurrence. Section [8](#sec:modfive){reference-type="ref" reference="sec:modfive"} proves the residue-class statement and audits the boundary $g=9$. Section [9](#sec:comparison){reference-type="ref" reference="sec:comparison"} closes with an explanatory common-kernel calculation and the precise limitations.

# Related Work and Bounded Positioning {#sec:related}

Dynamical degree is a broad invariant, and spectral descriptions of degree growth appear in settings much more general than the concrete affine automorphisms considered here. @DangFavreSpectralInterpretations develop spectral interpretations for dynamical degrees using spaces of numerical classes, while @DesertiDegreeGrowthExamples exhibits varied degree-growth behavior for higher-dimensional polynomial automorphisms and birational maps. These works motivate the spectral language but do not supply the row-by-row selector certificate needed for [\[eq:intro-potentials\]](#eq:intro-potentials){reference-type="eqref" reference="eq:intro-potentials"}.

Affine-triangular automorphisms form a particularly close algebraic neighbor. @BlancVanSantenAffineTriangular study their possible dynamical degrees and realize broad Perron phenomena, so no priority or general Perron-realization claim is intended here. The current preprint of @ShaoSunDimensionFour gives dimension-four bounds and constructions for affine-triangular automorphisms. We cite its arXiv version and do not assume a journal version. Our narrower issue is an exact, all-iterate calculation for one Hamiltonian gradient-shear word: a formal $4\times4$ matrix becomes valid only after four dynamically phased support choices, six invariant-cone walls, two carries, and a no-cancellation argument have all been proved.

The classical and contemporary Hénon-map literature provides another neighbor for polynomial automorphisms and their degree behavior; the multi-author problem list published under the collective name @HenonOpenProblems illustrates the range of open higher-dimensional questions. We use that context only to delimit the problem. The present map is not asserted to have any particular Hénon normal form, periodic structure, or geometric classification.

On the symplectic side, polynomial and holomorphic symplectic maps have long been studied from several perspectives. @ForstnericComplexSymplectic treats holomorphic symplectic automorphisms, and @RangarajanPolynomialSymplectic develops polynomial map factorizations for symplectic maps. The approximation and generation results of @BergerTuraevHamiltonianMaps emphasize the importance of position- and momentum-dependent shears. The distinction between cubic and higher-degree Hamiltonian behavior also appears in the straight-line-flow analysis of @KochLomeliStraightLineFlows. None of these references is used as a proof transfer: symplecticity, exact degrees, and the quartic calculation are all established directly here.

The nearest mechanism for the present comparison is the following simple one. If two selected phase matrices have the form $-I$ plus a small number of rank-one support corrections, a common kernel of the correction covectors produces a unit eigenspace for their product. An endpoint-spiked product-shear pattern can therefore collapse to a cubic residual factor even in many modes. Adding the second pure branch in each phase changes the combined covector profile. In the displayed four-mode case the two shifted kernels are different lines with zero intersection, and the characteristic polynomial remains quartic. This is an explanatory, nonnovel support-profile common-kernel lemma, not a classification and not a sufficient condition for quartic behavior.

Three distinctions keep this comparison precise. First, a general realization or bounded-degree theorem for affine-triangular maps does not identify the coordinate degree of every iterate of a prescribed symplectic word. The former may organize possible spectral values; the latter must control the actual support branch visited at every phase. Second, a construction from symplectic shears does not automatically carry an exact algebraic-degree calculation. Symplecticity is a differential identity, whereas degree selection is a piecewise-linear support problem with an additional algebraic survival condition. Third, a spectral interpretation of a dynamical degree does not determine which finite matrix, if any, computes the sequence of ordinary coordinate degrees for a particular affine map. Here the matrix is not introduced as an abstract linearization: it is derived from the eight supports and justified along the entire ordinary-degree orbit.

These distinctions also determine what information is and is not imported from the cited sources. From the affine-triangular literature we take only the broad fact that Perron behavior and degree-four algebraic phenomena belong to an established larger landscape. From the symplectic literature we take only context for gradient or position--momentum shears. From the general dynamical-degree literature we take the vocabulary of spectral growth. None of the four selector inequalities, six cone walls, temporal carry comparisons, principal minors, or finite-field factor exclusions below is delegated to a cited theorem.

Conversely, the present calculation does not subsume those broader theories. The potentials have a very small, deliberately asymmetric support: two pure branches occur in the $q$-phase and two complementary pure branches occur in the $p$-phase. The proof exploits that exact placement. Changing a coefficient, deleting a branch, or switching the composition order changes the relevant row comparisons and may change the complete-step matrix. The result should therefore be read as a fully resolved example family, not as a normal form for polynomial symplectomorphisms.

Our literature positioning is intentionally nonexhaustive. It supports only the distinction between general spectral frameworks and the explicit proof obligations discharged below. In particular, the article makes no claim of firstness, optimality, genericity, or priority.

# Family, Symplecticity, and Main Theorems {#sec:family}

## The fixed family

Let $K$ be any field with $\operatorname{char}K=0$, and fix an integer $g\geq10$. We work on $K^8=K_q^4\times K_p^4$ with standard symplectic matrix and form $$\label{eq:omega}
\Omega=
\begin{pmatrix}
0&I_4\\
-I_4&0
\end{pmatrix},
\qquad
\omega=\sum_{i=1}^4dq_i\wedge dp_i.$$ The potentials and maps are those in [\[eq:intro-potentials\]](#eq:intro-potentials){reference-type="eqref" reference="eq:intro-potentials"}--[\[eq:intro-map\]](#eq:intro-map){reference-type="eqref" reference="eq:intro-map"}. Literal differentiation gives $$\label{eq:grad-v}
\nabla V_g(q)=
\begin{pmatrix}
2q_1q_2^2q_3^2q_4^2+gq_1^{g-1}\\
2q_1^2q_2q_3^2q_4^2+(g-1)q_2^{g-2}\\
2q_1^2q_2^2q_3q_4^2\\
2q_1^2q_2^2q_3^2q_4
\end{pmatrix}$$ and $$\label{eq:grad-w}
\nabla W_g(p)=
\begin{pmatrix}
2p_1p_2^2p_3^2p_4^2\\
2p_1^2p_2p_3^2p_4^2\\
2p_1^2p_2^2p_3p_4^2+(g-1)p_3^{g-2}\\
2p_1^2p_2^2p_3^2p_4+gp_4^{g-1}
\end{pmatrix}.$$ The signs and integer coefficients in these two displays will later be used in the leading-form survival argument.

[\[prop:symplectic\]]{#prop:symplectic label="prop:symplectic"} The maps $S_g^+$, $T_g^+$, and $F_g=T_g^+\circ S_g^+$ are polynomial automorphisms of $K^8$. Each preserves $\omega$.

The subtraction shears $$(S_g^+)^{-1}(q,p)=(q,p-\nabla V_g(q)),\qquad
(T_g^+)^{-1}(q,p)=(q-\nabla W_g(p),p)$$ are polynomial inverses. Let $H_V=\nabla^2V_g(q)$ and $H_W=\nabla^2W_g(p)$. Formal differentiation is valid over $K$, and the Hessians are symmetric. The Jacobians are $$J_{S_g^+}=
\begin{pmatrix}I_4&0\\H_V&I_4\end{pmatrix},
\qquad
J_{T_g^+}=
\begin{pmatrix}I_4&H_W\\0&I_4\end{pmatrix}.$$ Block multiplication with $\Omega$ gives $$J_{S_g^+}^{\mathsf{T}}\Omega J_{S_g^+}
=
\begin{pmatrix}
H_V-H_V^{\mathsf{T}}&I_4\\
-I_4&0
\end{pmatrix}
=\Omega$$ and $$J_{T_g^+}^{\mathsf{T}}\Omega J_{T_g^+}
=
\begin{pmatrix}
0&I_4\\
-I_4&H_W^{\mathsf{T}}-H_W
\end{pmatrix}
=\Omega.$$ Thus both shears and their composition are symplectic.

## Degree vectors and the main statements

For a polynomial vector $G=(G_1,\ldots,G_m)$, write $\operatorname{deg}G=(\operatorname{deg}G_1,\ldots,\operatorname{deg}G_m)^{\mathsf{T}}$, where total degree is taken in all eight original variables. Put $$(Q^{(n)},P^{(n)})=F_g^n(q,p),
\qquad
u_n=\operatorname{deg}Q^{(n)},\qquad v_n=\operatorname{deg}P^{(n)}.$$ At the identity, $u_0=v_0=\mathbf{1}$.

There are two levels of information in these vectors. The ordinary degree of a sum is at most the maximum of the summand degrees, with equality if the top homogeneous parts do not cancel. The degree of a product is the sum of the factor degrees because a polynomial ring over a field is a domain. Accordingly, substituting polynomials of degree vector $u$ into a support monomial $q^\alpha$ gives candidate degree $\alpha^{\mathsf{T}}u$. Taking the maximum over a gradient row is a piecewise-linear operation. A fixed matrix represents that operation only inside a region where a fixed exponent wins in every competitive row.

The shear form introduces a second maximum. During $S_g^+$, each new $p_i$ equals the old $p_i$ plus a derivative of $V_g$ evaluated at the current $q$-coordinates. Even after choosing a support exponent, the fresh derivative must outrun the old $p_i$. During $T_g^+$, the same issue recurs between the old $q_i$ and a derivative of $W_g$, now evaluated at the already updated $p$-coordinates. The first comparison is a support selector, the second is a temporal carry. They are logically independent: a uniquely selected term within a gradient could still have smaller degree than the carried coordinate.

Finally, degrees alone do not remember coefficients. A uniquely maximal support exponent prevents competition between different original support faces, but after polynomial substitution the selected monomial expands. Several products can land on the same monomial in the original variables. The characteristic-zero positive-coefficient argument in Proposition [\[prop:survival\]](#prop:survival){reference-type="ref" reference="prop:survival"} ensures that such contributions add rather than cancel. Thus the proof of [\[eq:vector-recurrence\]](#eq:vector-recurrence){reference-type="eqref" reference="eq:vector-recurrence"} must establish, in order, support strictness, invariant ratios, temporal domination, and coefficient survival. The later visibility proof is a fifth obligation because total map degree is the largest entry across both phase vectors.

With that distinction understood, the complete-step matrix obtained from [\[eq:intro-phase-matrices\]](#eq:intro-phase-matrices){reference-type="eqref" reference="eq:intro-phase-matrices"} is $$\label{eq:C}
C_g=B_gA_g=
\begin{pmatrix}
g+7&2g+4&6&6\\
2g+6&g+6&6&6\\
2g-4&2g-4&g-2&2g-4\\
2g-2&2g-2&2g-2&g-1
\end{pmatrix}.$$

The ratio cone used throughout the proof is $$\label{eq:cone}
\mathcal K_g=\left\{
u_1(1,x,y,z)^{\mathsf{T}}:
u_1>0,\
1\leq x\leq a_g,\
1\leq y\leq z\leq a_gy,\
y+z<H_g
\right\},$$ where $$\label{eq:a-h}
a_g=\frac{g-1}{g-2},
\qquad
H_g=\frac{g-5}{2}.$$ The closed faces in [\[eq:cone\]](#eq:cone){reference-type="eqref" reference="eq:cone"} are intentional; the selector gaps will remain strict throughout this region.

[\[thm:degree\]]{#thm:degree label="thm:degree"} For every characteristic-zero field $K$, every integer $g\geq10$, and the map $F_g$ in [\[eq:intro-map\]](#eq:intro-map){reference-type="eqref" reference="eq:intro-map"}, the cone $\mathcal{K}_g$ is a sufficient complete-step invariant cone: $$\mathbf{1}\in\mathcal{K}_g,\qquad C_g\mathcal{K}_g\subseteq\mathcal{K}_g.$$ The actual phase degrees satisfy $$\label{eq:vector-recurrence}
v_{n+1}=A_gu_n,\qquad u_{n+1}=C_gu_n
\qquad(n\geq0).$$ The fourth $q$-coordinate is the unique coordinate of maximal degree for every $n\geq1$. All eight coordinates tie at $n=0$, and $$\label{eq:exact-degree}
\operatorname{deg}(F_g^n)=\mathbf{e}_4^{\mathsf{T}}C_g^n\mathbf{1}
\qquad(n\geq0).$$

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} The characteristic polynomial of $C_g$ is $$\label{eq:R-preview}
\begin{aligned}
R_g(t)={}&t^4-(4g+10)t^3+(-2g^2-26g+45)t^2\\
&+(12g^3-70g^2+126g-72)t
+9(g-1)^2(g-2)^2.
\end{aligned}$$ If $d_n=\operatorname{deg}(F_g^n)$, then $$\label{eq:recurrence-preview}
\begin{aligned}
d_{n+4}={}&(4g+10)d_{n+3}
+(2g^2+26g-45)d_{n+2}\\
&-(12g^3-70g^2+126g-72)d_{n+1}\\
&-9(g-1)^2(g-2)^2d_n.
\end{aligned}$$ Moreover, $$\lambda_1(F_g)=\rho(C_g).$$ For $g=13,18,23,\ldots$, this number is a Perron algebraic integer of degree four, and the resulting values are pairwise distinct.

Two kinds of scalars appear in these statements and should not be conflated. Polynomial coefficients and coordinate identities live in the arbitrary characteristic-zero field $K$. Degree vectors, ratios, and inequalities live in $\mathbb{R}$; they are combinatorial records of exponents, not elements of $K$. In particular, no ordering or absolute value on $K$ is assumed. The positive matrix $C_g$ is an integer matrix whose Perron theory is considered over $\mathbb{R}$, while its entries simultaneously describe exponents for polynomials over $K$. This separation is what allows the exact degree theorem to hold over every characteristic-zero field without choosing an embedding into $\mathbb C$.

The integer hypothesis on $g$ has several uses. It makes the pure powers in [\[eq:intro-potentials\]](#eq:intro-potentials){reference-type="eqref" reference="eq:intro-potentials"} polynomial, keeps all derivative coefficients positive integers, and turns the boundary comparison $g\geq10$ into a discrete statement. The cone itself is a region of real weights even though the iterated degree vectors are integral. Proving invariance for the whole real cone is stronger than checking only the countable orbit $C_g^n\mathbf{1}$, but it provides simple uniform inequalities for all later steps.

The two main theorems also have different logical dependencies. Theorem [\[thm:degree\]](#thm:degree){reference-type="ref" reference="thm:degree"} is entirely a statement about the polynomial map and its ordinary coordinate degrees. Theorem [\[thm:spectrum\]](#thm:spectrum){reference-type="ref" reference="thm:spectrum"} first uses that exact scalar formula, then invokes linear algebra for $C_g$, and finally uses finite-field irreducibility on a restricted set of parameters. Without Theorem [\[thm:degree\]](#thm:degree){reference-type="ref" reference="thm:degree"}, the same quartic matrix calculation would describe only a proposed weighted description. Conversely, the degree theorem holds for every $g\geq10$ even when the irreducibility of $R_g$ is not certified by the modulo-five argument.

The proofs of Theorems [\[thm:degree\]](#thm:degree){reference-type="ref" reference="thm:degree"} and [\[thm:spectrum\]](#thm:spectrum){reference-type="ref" reference="thm:spectrum"} occupy the next five sections. The order matters: the characteristic polynomial alone does not establish that $C_g$ governs actual polynomial degrees.

# Weighted Supports and Four Phase Selectors {#sec:supports}

## The complete support ledger

For $u\in\mathbb{R}_{>0}^4$ and a polynomial $h(q)=\sum_\alpha c_\alpha q^\alpha$, define its $u$-weighted degree by $$\operatorname{deg}_u h=\max_{\alpha\in\mathop{\mathrm{supp}}(h)}\alpha^{\mathsf{T}}u.$$ If the coordinates substituted for $q_i$ have actual total degrees $u_i$, this maximum is the formal degree candidate supplied by the support of $h$. Equality with the degree after substitution is a separate question because distinct terms can in principle cancel. We postpone that question until Section [5](#sec:cone){reference-type="ref" reference="sec:cone"}; at present we record every exponent that can compete.

::: {#tab:supports}
  $\displaystyle\textnormal{Gradient row}$     Phase   Status        Exponent support             Selected exponent
  ------------------------------------------ --------- ------------- ---------------------------- -------------------
  $\displaystyle\partial_{q_1}V_g$            $S_g^+$  competitive   $(1,2,2,2)$, $(g-1,0,0,0)$   $(g-1,0,0,0)$
  $\displaystyle\partial_{q_2}V_g$            $S_g^+$  competitive   $(2,1,2,2)$, $(0,g-2,0,0)$   $(0,g-2,0,0)$
  $\displaystyle\partial_{q_3}V_g$            $S_g^+$  rigid         $(2,2,1,2)$                  $(2,2,1,2)$
  $\displaystyle\partial_{q_4}V_g$            $S_g^+$  rigid         $(2,2,2,1)$                  $(2,2,2,1)$
  $\displaystyle\partial_{p_1}W_g$            $T_g^+$  rigid         $(1,2,2,2)$                  $(1,2,2,2)$
  $\displaystyle\partial_{p_2}W_g$            $T_g^+$  rigid         $(2,1,2,2)$                  $(2,1,2,2)$
  $\displaystyle\partial_{p_3}W_g$            $T_g^+$  competitive   $(2,2,1,2)$, $(0,0,g-2,0)$   $(0,0,g-2,0)$
  $\displaystyle\partial_{p_4}W_g$            $T_g^+$  competitive   $(2,2,2,1)$, $(0,0,0,g-1)$   $(0,0,0,g-1)$

  : The eight literal gradient supports, phase status, and selected exponents.
:::

The support ledger in Table [1](#tab:supports){reference-type="ref" reference="tab:supports"} has two consequences. First, the proposed first-phase matrix selects the pure exponents in the first two rows and uses the unique mixed exponent in the last two rows. This is exactly $A_g$ in [\[eq:intro-phase-matrices\]](#eq:intro-phase-matrices){reference-type="eqref" reference="eq:intro-phase-matrices"}. Second, the proposed second-phase matrix uses the unique mixed exponent in the first two rows and selects the pure exponents in the last two rows, giving $B_g$. Since $S_g^+$ acts before $T_g^+$, the complete product is $B_gA_g$, not $A_gB_g$. Direct multiplication yields [\[eq:C\]](#eq:C){reference-type="eqref" reference="eq:C"}; on the ordinary seed, $$\label{eq:seed-phases}
A_g\mathbf{1}=(g-1,g-2,7,7)^{\mathsf{T}},
\qquad
C_g\mathbf{1}=(3g+23,3g+24,7g-14,7g-7)^{\mathsf{T}}.$$

[\[lem:conditional-phases\]]{#lem:conditional-phases label="lem:conditional-phases"} Let $u\in\mathbb{R}_{>0}^4$. If the pure exponents win in the first two competitive rows of $\nabla V_g$, then the four fresh first-phase weighted degrees are $A_gu$. If $v=A_gu$ and the pure exponents win in the last two competitive rows of $\nabla W_g$, then the four fresh second-phase weighted degrees are $B_gv=C_gu$.

For the first phase, the selected pure terms in rows one and two have weighted degrees $$(g-1)u_1,\qquad(g-2)u_2.$$ The third and fourth rows have no alternative support, so their weighted degrees are $$2u_1+2u_2+u_3+2u_4,\qquad
2u_1+2u_2+2u_3+u_4.$$ These four linear forms are precisely the rows of $A_g$.

Now regard $v$ as the degree vector entering the second phase. The first two rows there are singleton supports and give $$v_1+2v_2+2v_3+2v_4,\qquad
2v_1+v_2+2v_3+2v_4.$$ Under the stated pure selections, the last two rows give $$(g-2)v_3,\qquad(g-1)v_4.$$ Those are exactly the four rows of $B_gv$. Since the first phase acts first, $v=A_gu$, and hence the complete fresh vector is $B_gA_gu=C_gu$.

Lemma [\[lem:conditional-phases\]](#lem:conditional-phases){reference-type="ref" reference="lem:conditional-phases"} is deliberately conditional. It records the support arithmetic and the temporal order but does not establish that the required inequalities hold, that the fresh vector dominates the carried coordinates, or that its leading form is nonzero after substitution. The next selector calculation proves the first point; the remaining two are settled in Section [5](#sec:cone){reference-type="ref" reference="sec:cone"}.

## Selectors in the first phase

Let $$u=u_1(1,x,y,z)^{\mathsf{T}}\in\mathcal{K}_g.$$ In the first row of $\nabla V_g$, the pure exponent has weighted value $(g-1)u_1$, whereas the mixed exponent has weighted value $u_1+2u_2+2u_3+2u_4$. The pure-minus-mixed gap, divided by $u_1$, is $$\label{eq:S1}
\Delta_{S,1}=(g-2)-2x-2y-2z.$$ The same calculation in the second row gives $$\label{eq:S2}
\Delta_{S,2}=(g-3)x-2-2y-2z.$$ The use of $g-3$, rather than $g-2$, in [\[eq:S2\]](#eq:S2){reference-type="eqref" reference="eq:S2"} reflects the $x$ already present in the mixed weighted value.

The cone inequalities make both gaps strict. Because $x\leq a_g$ and $y+z<H_g$, $$\label{eq:S1-bound}
\begin{aligned}
\Delta_{S,1}
&>g-2-2a_g-2H_g\\
&=3-2a_g
=\frac{g-4}{g-2}>0.
\end{aligned}$$ Likewise, $x\geq1$ gives $$\label{eq:S2-bound}
\Delta_{S,2}
\geq(g-3)-2(1+y+z)
>g-3-2(1+H_g)=0.$$ Thus the first phase selects its two pure rows throughout $\mathcal{K}_g$, not merely at the seed.

## Phase-correct selectors in the second phase

The second-phase competition must be evaluated after the first phase has changed the degree vector. From the selected rows of $A_g$, $$\label{eq:intermediate-ratios}
\frac{A_gu}{u_1}=
\begin{pmatrix}
g-1\\
(g-2)x\\
2+2x+y+2z\\
2+2x+2y+z
\end{pmatrix}.$$ Write $v=A_gu$. The third row of $\nabla W_g$ compares the pure value $(g-2)v_3$ against $2v_1+2v_2+v_3+2v_4$. Substitution of [\[eq:intermediate-ratios\]](#eq:intermediate-ratios){reference-type="eqref" reference="eq:intermediate-ratios"} and collection of coefficients gives $$\label{eq:T3}
\Delta_{T,3}
=-8-6x+(g-7)y+(2g-8)z.$$ Similarly, the fourth row compares $(g-1)v_4$ against $2v_1+2v_2+2v_3+v_4$, producing $$\label{eq:T4}
\Delta_{T,4}
=-6-4x+(2g-6)y+(g-6)z.$$ These are the two phase-correct selectors. Evaluating either competition at $u$ instead of $A_gu$ would test a different iteration.

[\[lem:selectors\]]{#lem:selectors label="lem:selectors"} For every $g\geq10$ and every $u\in\mathcal{K}_g$, the four gaps in [\[eq:S1\]](#eq:S1){reference-type="eqref" reference="eq:S1"}, [\[eq:S2\]](#eq:S2){reference-type="eqref" reference="eq:S2"}, [\[eq:T3\]](#eq:T3){reference-type="eqref" reference="eq:T3"}, and [\[eq:T4\]](#eq:T4){reference-type="eqref" reference="eq:T4"} are strictly positive.

The first two gaps were handled in [\[eq:S1-bound\]](#eq:S1-bound){reference-type="eqref" reference="eq:S1-bound"}--[\[eq:S2-bound\]](#eq:S2-bound){reference-type="eqref" reference="eq:S2-bound"}. For the second phase, note that $$a_g=1+\frac{1}{g-2}\leq\frac98.$$ The coefficients of $y$ and $z$ in [\[eq:T3\]](#eq:T3){reference-type="eqref" reference="eq:T3"} are positive, while the coefficient of $x$ is negative. Hence $x\leq a_g$ and $y,z\geq1$ give $$\label{eq:T3-bound}
\begin{aligned}
\Delta_{T,3}
&\geq-8-6a_g+(g-7)+(2g-8)\\
&=3g-23-6a_g
\geq\frac{12g-119}{4}>0.
\end{aligned}$$ The same monotonicity for [\[eq:T4\]](#eq:T4){reference-type="eqref" reference="eq:T4"} yields $$\label{eq:T4-bound}
\begin{aligned}
\Delta_{T,4}
&\geq-6-4a_g+(2g-6)+(g-6)\\
&=3g-18-4a_g
\geq\frac{6g-45}{2}>0.
\end{aligned}$$ Thus all four proposed outer exponents win uniquely.

The ordinary-degree seed corresponds to $(x,y,z)=(1,1,1)$. It lies in $\mathcal{K}_g$ because $1\leq a_g$ and $$2<H_g=\frac{g-5}{2}$$ for every integer $g\geq10$. At this seed the four selector margins, listed in phase order, are $$\label{eq:seed-margins}
g-8,\qquad g-9,\qquad 3g-29,\qquad 3g-22.$$ They equal $(2,1,1,8)$ at $g=10$. Seed strictness alone would not be enough for iteration; the next section proves that every complete step returns the ratio vector to the same cone.

# Ratio Cone, Carry, and Leading-Form Survival {#sec:cone}

## The six target walls

Take $u=u_1(1,x,y,z)^{\mathsf{T}}\in\mathcal{K}_g$, and write $$\label{eq:D-and-N}
C_gu=u_1(D,N_2,N_3,N_4)^{\mathsf{T}},$$ where $$\label{eq:D-and-N-expanded}
\begin{aligned}
D&=g+7+(2g+4)x+6y+6z,\\
N_2&=2g+6+(g+6)x+6y+6z,\\
N_3&=2g-4+(2g-4)x+(g-2)y+(2g-4)z,\\
N_4&=2g-2+(2g-2)x+(2g-2)y+(g-1)z.
\end{aligned}$$ All four expressions are positive. The output ratios are therefore $$X'=\frac{N_2}{D},\qquad
Y'=\frac{N_3}{D},\qquad
Z'=\frac{N_4}{D}.$$ The normalization by the first coordinate is legitimate because every entry of $C_g$ and every component of $u$ is positive. It also makes the proof homogeneous: multiplying an input weight by a positive scalar does not change its ratios or any selector sign. To return to $\mathcal{K}_g$, the output must satisfy exactly six independent conditions: the lower and upper bounds on $X'$, the lower bound on $Y'$, the order of $Y'$ and $Z'$, the slanted upper bound for $Z'/Y'$, and the strict height bound. Positivity of $D$ lets each ratio condition be tested by a polynomial numerator without reversing a sign.

Some target faces are weak because the cone was defined with weak order constraints, while selector strictness is maintained separately. In particular, $X'=1$ or $Z'=a_gY'$ is compatible with membership in the cone. The height face must remain strict: it is used directly in [\[eq:S1-bound\]](#eq:S1-bound){reference-type="eqref" reference="eq:S1-bound"} and [\[eq:S2-bound\]](#eq:S2-bound){reference-type="eqref" reference="eq:S2-bound"}. Keeping this distinction visible prevents a weak cone wall from being mistaken for a support tie. Table [2](#tab:walls){reference-type="ref" reference="tab:walls"} states the six wall numerators used below. Weak and strict inequalities are displayed exactly as needed by the definition of $\mathcal{K}_g$.

::: {#tab:walls}
   [Target wall]{.nodecor}  [Exact numerator]{.nodecor}           [Input bounds used]{.nodecor}   [Certified sign]{.nodecor}
  ------------------------- ------------------------------------- ------------------------------- --------------------------------
          $X'\geq1$         $N_2-D=(g-1)-(g-2)x$                  $x\leq a_g$                     $\geq0$
          $X'<a_g$          $(g-1)D-(g-2)N_2$                     $x\geq1,\ y+z\geq2$             $\geq2g+25>0$
           $Y'>1$           $N_3-D=g-11-8x+(g-8)y+(2g-10)z$       $x\leq a_g,\ y,z\geq1$          $\geq4g-29-8a_g\geq2$
           $Z'>Y'$          $N_4-N_3=2+2x+gy-(g-3)z$              $z\leq a_gy$                    $\geq2+2x+\frac{2g-3}{g-2}y>0$
       $Z'\leq a_gY'$       $(g-1)N_3-(g-2)N_4=(g-1)(g-2)(z-y)$   $z\geq y$                       $\geq0$
         $Y'+Z'<H_g$        $E_H=(g-5)D-2(N_3+N_4)$               $x,z\geq1,\ y+z<H_g$            $>3g^2-31g+26>0$

  : The six ratio-cone walls for one complete step.
:::

[\[prop:invariance\]]{#prop:invariance label="prop:invariance"} For every integer $g\geq10$, $$C_g\mathcal{K}_g\subseteq\mathcal{K}_g.$$

We verify the faces in the order of Table [2](#tab:walls){reference-type="ref" reference="tab:walls"}. The lower $X'$-face follows from $$N_2-D=(g-1)-(g-2)x\geq0,$$ because $x\leq a_g=(g-1)/(g-2)$. Equality is allowed on this target face.

For the upper $X'$-face, multiplication by the positive denominator and by $g-2$ shows that $X'<a_g$ is equivalent to positivity of $$E_X:=(g-1)D-(g-2)N_2.$$ Expansion gives $$\label{eq:EX}
E_X=-g^2+4g+5+(g^2-2g+8)x+6(y+z).$$ The coefficient of $x$ is positive, and $x\geq1$, $y+z\geq2$. Consequently $$E_X\geq-g^2+4g+5+(g^2-2g+8)+12=2g+25>0.$$

For $Y'>1$, direct subtraction in [\[eq:D-and-N-expanded\]](#eq:D-and-N-expanded){reference-type="eqref" reference="eq:D-and-N-expanded"} yields $$\label{eq:Y-lower}
N_3-D=g-11-8x+(g-8)y+(2g-10)z.$$ The only negative variable coefficient is that of $x$. Using $x\leq a_g$ and $y,z\geq1$, $$N_3-D\geq4g-29-8a_g\geq4g-38\geq2.$$ Thus this lower face is reached strictly.

The ordering wall $Z'>Y'$ has numerator $$\label{eq:Z-Y}
N_4-N_3=2+2x+gy-(g-3)z.$$ The cone inequality $z\leq a_gy$ implies $$\label{eq:Z-Y-bound}
\begin{aligned}
N_4-N_3
&\geq2+2x+\bigl(g-(g-3)a_g\bigr)y\\
&=2+2x+\frac{2g-3}{g-2}y>0.
\end{aligned}$$

For the slanted upper wall, an exact cancellation gives $$\label{eq:slanted-wall}
(g-1)N_3-(g-2)N_4
=(g-1)(g-2)(z-y)\geq0.$$ After division by $g-2$, this is $a_gN_3-N_4=(g-1)(z-y)\geq0$, proving $Z'\leq a_gY'$. The possible equality on this target wall does not create a support tie: Lemma [\[lem:selectors\]](#lem:selectors){reference-type="ref" reference="lem:selectors"} proved strict gaps on the entire cone, including its closed faces.

It remains to prove the strict height condition. Since $D>0$, $Y'+Z'<H_g$ is equivalent to $$E_H:=(g-5)D-2(N_3+N_4)>0.$$ Full expansion, with no discarded term, is $$\label{eq:EH}
E_H=
g^2-6g-23+(2g^2-14g-8)x-22y-20z.$$ For $g\geq10$, $$2g^2-14g-8=52+(g-10)(2g+6)>0,$$ so the lower bound $x\geq1$ may be used in the positive direction. The height bound and $z\geq1$ also give $$-22y-20z=-22(y+z)+2z>-22H_g+2.$$ Substitution into [\[eq:EH\]](#eq:EH){reference-type="eqref" reference="eq:EH"} yields $$\label{eq:EH-bound}
\begin{aligned}
E_H
&>g^2-6g-23+(2g^2-14g-8)-22H_g+2\\
&=3g^2-31g+26\\
&=16+(g-10)(3g-1)>0.
\end{aligned}$$ All six defining walls are preserved with their required weak or strict signs, which proves the claim.

Proposition [\[prop:invariance\]](#prop:invariance){reference-type="ref" reference="prop:invariance"} certifies one convenient cone. It does not show that $\mathcal{K}_g$ is necessary, maximal, or optimal, and it does not classify other selector chambers.

## The two temporal carries

Support selection compares terms within a fresh gradient row. A shear coordinate is instead a sum of a carried coordinate and a fresh gradient, so one must also prove that the fresh selected degree wins. The base first phase is immediate from [\[eq:seed-phases\]](#eq:seed-phases){reference-type="eqref" reference="eq:seed-phases"}: $$\label{eq:first-base-carry}
A_g\mathbf{1}=(g-1,g-2,7,7)^{\mathsf{T}}>\mathbf{1}.$$ For the complete second phase, observe that $$\label{eq:C-minus-I}
C_g-I_4=
\begin{pmatrix}
g+6&2g+4&6&6\\
2g+6&g+5&6&6\\
2g-4&2g-4&g-3&2g-4\\
2g-2&2g-2&2g-2&g-2
\end{pmatrix}.$$ Every entry is positive for $g\geq10$. Thus $$\label{eq:second-carry-general}
(C_g-I_4)u>0$$ for every positive $u$, including $u=\mathbf{1}$.

[\[lem:phase-induction\]]{#lem:phase-induction label="lem:phase-induction"} There are formal candidate vectors $\widetilde u_0=\widetilde v_0=\mathbf{1}$ such that, for all $n\geq0$, $\widetilde u_n\in\mathcal{K}_g$ and $$\widetilde v_{n+1}=A_g\widetilde u_n,\qquad
\widetilde u_{n+1}=C_g\widetilde u_n.$$ At each phase, the fresh selected candidate strictly exceeds the corresponding carried candidate.

At $n=0$, the seed belongs to $\mathcal{K}_g$, Lemma [\[lem:selectors\]](#lem:selectors){reference-type="ref" reference="lem:selectors"} selects all four proposed supports, [\[eq:first-base-carry\]](#eq:first-base-carry){reference-type="eqref" reference="eq:first-base-carry"} handles the first carried vector, and [\[eq:second-carry-general\]](#eq:second-carry-general){reference-type="eqref" reference="eq:second-carry-general"} handles the second. Define $\widetilde v_1=A_g\mathbf{1}$ and $\widetilde u_1=C_g\mathbf{1}$.

Suppose the candidate assertions hold through a given complete step, so $$\widetilde u_n=C_g\widetilde u_{n-1},\qquad
\widetilde v_n=A_g\widetilde u_{n-1},\qquad
\widetilde u_n\in\mathcal{K}_g.$$ Entrywise positivity in [\[eq:C-minus-I\]](#eq:C-minus-I){reference-type="eqref" reference="eq:C-minus-I"} gives the first temporal difference $$\label{eq:temporal-u}
\widetilde u_n-\widetilde u_{n-1}
=(C_g-I_4)\widetilde u_{n-1}>0.$$ The matrix $A_g$ is nonnegative and every row contains a positive entry. Applying it to [\[eq:temporal-u\]](#eq:temporal-u){reference-type="eqref" reference="eq:temporal-u"} gives the second comparison needed for the first phase: $$\label{eq:temporal-v}
A_g(\widetilde u_n-\widetilde u_{n-1})>0.$$ The fresh first-phase candidate $A_g\widetilde u_n$ therefore beats the carried candidate $\widetilde v_n=A_g\widetilde u_{n-1}$, coordinate by coordinate. Define $$\widetilde v_{n+1}=A_g\widetilde u_n.$$

Lemma [\[lem:selectors\]](#lem:selectors){reference-type="ref" reference="lem:selectors"} applies to this same $\widetilde u_n$, with the second phase evaluated at $A_g\widetilde u_n$. Its fresh candidate is $B_gA_g\widetilde u_n=C_g\widetilde u_n$. By [\[eq:second-carry-general\]](#eq:second-carry-general){reference-type="eqref" reference="eq:second-carry-general"}, this candidate strictly beats $\widetilde u_n$. Define $$\widetilde u_{n+1}=C_g\widetilde u_n.$$ Finally, Proposition [\[prop:invariance\]](#prop:invariance){reference-type="ref" reference="prop:invariance"} returns $\widetilde u_{n+1}$ to $\mathcal{K}_g$. This closes all parts of the simultaneous induction.

## Why the selected degrees survive

Lemma [\[lem:phase-induction\]](#lem:phase-induction){reference-type="ref" reference="lem:phase-induction"} has so far established a formal support-and-carry recurrence. We now exclude cancellation in the actual coordinate polynomials. This step is specific to the fixed positive-sign family.

[\[prop:survival\]]{#prop:survival label="prop:survival"} Every degree selected in Lemma [\[lem:phase-induction\]](#lem:phase-induction){reference-type="ref" reference="lem:phase-induction"} occurs in the corresponding coordinate polynomial over $K$. Consequently, $$\label{eq:actual-vectors}
u_n=C_g^n\mathbf{1}\quad(n\geq0),\qquad
v_n=A_gC_g^{n-1}\mathbf{1}\quad(n\geq1)$$ are actual total-degree vectors.

All coefficients in [\[eq:grad-v\]](#eq:grad-v){reference-type="eqref" reference="eq:grad-v"} and [\[eq:grad-w\]](#eq:grad-w){reference-type="eqref" reference="eq:grad-w"} are positive integers, namely $2$, $g-1$, or $g$. The initial coordinate polynomials have coefficients in $\{0,1\}$. Forward application of $S_g^+$ and $T_g^+$ uses only addition and multiplication; hence, inductively, every coefficient in every coordinate of every forward iterate is a nonnegative integer before it is mapped into $K$.

We prove simultaneously that the actual vectors $u_n,v_n$ equal the formal candidates in Lemma [\[lem:phase-induction\]](#lem:phase-induction){reference-type="ref" reference="lem:phase-induction"}. This holds at $n=0$. Suppose it holds through a complete step. In each competitive row, Lemma [\[lem:selectors\]](#lem:selectors){reference-type="ref" reference="lem:selectors"} selects one outer support exponent strictly at $\widetilde u_n$; every noncompetitive row has a singleton support. Substitution can expand a selected support monomial into several monomials of the same leading degree. If different products contribute to the same monomial, their coefficients add inside $\mathbb Z_{\geq0}$; a selected contribution makes that sum a positive integer. No negative term is present to cancel it. Because $\operatorname{char}K=0$, that positive integer remains nonzero in $K$.

Thus the fresh first-phase polynomials have actual degree vector $A_g\widetilde u_n=\widetilde v_{n+1}$. The first formal carry inequality makes them strictly dominate the actual carried vector $v_n=\widetilde v_n$, so the updated actual vector is $v_{n+1}=\widetilde v_{n+1}$. Applying the same positivity argument in the second phase gives fresh actual vector $B_g\widetilde v_{n+1}=C_g\widetilde u_n
=\widetilde u_{n+1}$. The second formal carry inequality makes it dominate the carried vector $u_n=\widetilde u_n$. Hence $u_{n+1}=\widetilde u_{n+1}$, closing the induction. Since the candidate recursion has the stated matrix solution, [\[eq:actual-vectors\]](#eq:actual-vectors){reference-type="eqref" reference="eq:actual-vectors"} follows.

One can make the survival induction more explicit. Suppose each current coordinate is represented by a polynomial in $\mathbb Z_{\geq0}[q_1,\ldots,q_4,p_1,\ldots,p_4]$ and has a nonzero homogeneous part in its recorded top degree. A mixed derivative monomial, after substitution, is a product of positive powers of four such coordinates. Choosing one nonzero top monomial in each factor produces a top-degree product with positive coefficient. A pure derivative branch is handled in the same way using a positive power of one coordinate. Multiplication may cause different choices to produce the same exponent, but this only increases its coefficient in the nonnegative integer semiring.

Addition inside a gradient row also preserves nonnegativity. Strict selector inequalities say that terms from the losing support exponent have smaller degree, so they cannot alter the selected homogeneous part. Strict temporal carry says that the old coordinate has smaller degree than the fresh gradient; it likewise cannot alter that top part. Hence the updated coordinate again has a nonzero recorded leading part and nonnegative integer coefficients. Starting from the eight variables closes this induction simultaneously through both shears and every iterate. Passing from $\mathbb Z_{\geq0}$ to $K$ preserves every positive coefficient exactly because the canonical map $\mathbb Z\to K$ is injective in characteristic zero.

This survival argument does not extend automatically to arbitrary signs or coefficients. It also explains why characteristic zero is part of the theorem rather than a cosmetic convention.

# Visibility and Exact Total Degree {#sec:degree}

The vector recurrence determines four $q$-degrees and four $p$-degrees, but the total degree of $F_g^n$ is the maximum over all eight coordinates. This section identifies that maximum. For a complete step with input $u\in\mathcal{K}_g$, the final vectors are $C_gu$ in the $q$-block and $A_gu$ in the $p$-block. Their coordinatewise difference is $$\label{eq:C-minus-A}
C_g-A_g=
\begin{pmatrix}
8&2g+4&6&6\\
2g+6&8&6&6\\
2g-6&2g-6&g-3&2g-6\\
2g-4&2g-4&2g-4&g-2
\end{pmatrix}.$$ This matrix is entrywise positive for $g\geq10$, so each complete $q_i$-degree strictly exceeds the corresponding final $p_i$-degree. It remains to compare the fourth $q$-row with the first three $q$-rows.

Let $u=u_1(1,x,y,z)^{\mathsf{T}}$. Subtracting the first row of $C_g$ from the fourth gives $$\label{eq:q4-q1}
\frac{(C_gu)_4-(C_gu)_1}{u_1}
=g-9-6x+(2g-8)y+(g-7)z.$$ The negative coefficient requires $x\leq a_g$, whereas $y,z\geq1$ can be used for the positive terms. Therefore $$\label{eq:q4-q1-bound}
g-9-6x+(2g-8)y+(g-7)z
\geq4g-24-6a_g>0.$$ For the second row, $$\label{eq:q4-q2}
\frac{(C_gu)_4-(C_gu)_2}{u_1}
=-8+(g-8)x+(2g-8)y+(g-7)z.$$ All three variable coefficients are positive, and hence $$\label{eq:q4-q2-bound}
-8+(g-8)x+(2g-8)y+(g-7)z\geq4g-31>0.$$ The third comparison is $$\label{eq:q4-q3}
\frac{(C_gu)_4-(C_gu)_3}{u_1}
=2+2x+gy-(g-3)z.$$ This is the same expression as the strict ordering wall in [\[eq:Z-Y\]](#eq:Z-Y){reference-type="eqref" reference="eq:Z-Y"}. From [\[eq:Z-Y-bound\]](#eq:Z-Y-bound){reference-type="eqref" reference="eq:Z-Y-bound"}, $$\label{eq:q4-q3-bound}
2+2x+gy-(g-3)z
\geq2+2x+\frac{2g-3}{g-2}y>0.$$

[\[prop:visibility\]]{#prop:visibility label="prop:visibility"} After every positive iterate, the fourth $q$-coordinate has degree strictly larger than each of the other seven coordinate degrees.

Proposition [\[prop:survival\]](#prop:survival){reference-type="ref" reference="prop:survival"} and cone invariance put the input to every complete step in $\mathcal{K}_g$. Equations [\[eq:q4-q1-bound\]](#eq:q4-q1-bound){reference-type="eqref" reference="eq:q4-q1-bound"}, [\[eq:q4-q2-bound\]](#eq:q4-q2-bound){reference-type="eqref" reference="eq:q4-q2-bound"}, and [\[eq:q4-q3-bound\]](#eq:q4-q3-bound){reference-type="eqref" reference="eq:q4-q3-bound"} show that the fourth $q$-row strictly beats the first, second, and third $q$-rows. By [\[eq:C-minus-A\]](#eq:C-minus-A){reference-type="eqref" reference="eq:C-minus-A"}, each of those three $q$-rows strictly beats its matching $p$-row. This handles $p_1,p_2,p_3$. The fourth row of [\[eq:C-minus-A\]](#eq:C-minus-A){reference-type="eqref" reference="eq:C-minus-A"} directly shows that $q_4$ beats $p_4$. Together these are the seven required comparisons.

## Index and maximum audit

The indexing in Proposition [\[prop:visibility\]](#prop:visibility){reference-type="ref" reference="prop:visibility"} can be checked directly against the two shears. For $n\geq1$, the $n$th complete step starts with $q$-degree vector $u_{n-1}$. After $S_g^+$, its updated $p$-degree vector is $A_gu_{n-1}=v_n$. After $T_g^+$, its updated $q$-degree vector is $C_gu_{n-1}=u_n$. Thus the two blocks compared in [\[eq:C-minus-A\]](#eq:C-minus-A){reference-type="eqref" reference="eq:C-minus-A"} belong to the same final iterate; no degree from an earlier or later phase is mixed into the visibility claim.

There are exactly seven competitors to the fourth $q$-coordinate. Equations [\[eq:q4-q1\]](#eq:q4-q1){reference-type="eqref" reference="eq:q4-q1"}--[\[eq:q4-q3\]](#eq:q4-q3){reference-type="eqref" reference="eq:q4-q3"} compare it directly with the other three $q$-coordinates. For each $i=1,2,3$, row $i$ of [\[eq:C-minus-A\]](#eq:C-minus-A){reference-type="eqref" reference="eq:C-minus-A"} then gives the strict chain $$(C_gu_{n-1})_4>(C_gu_{n-1})_i>(A_gu_{n-1})_i.$$ The fourth row gives $$(C_gu_{n-1})_4>(A_gu_{n-1})_4.$$ These three chains and the last direct inequality exhaust the four $p$-competitors without assuming that the $p$-degrees are ordered among themselves.

Our convention for the degree of a polynomial map is the maximum of the ordinary total degrees of its coordinate polynomials. Proposition [\[prop:survival\]](#prop:survival){reference-type="ref" reference="prop:survival"} guarantees that every entry in the two displayed degree vectors is actual, so the strict maximum just identified is not merely a weighted upper bound. This audit is also why visibility cannot be replaced by the assertion that $C_g$ is positive: positivity orders a matrix against zero, not one row against the other seven final coordinates.

At $n=0$, no strict comparison is true: $F_g^0$ is the identity and all eight coordinate degrees equal one. This is the tied identity case at $n=0$, not an exceptional failure of the recurrence. Since $\mathbf{e}_4^{\mathsf{T}}\mathbf{1}=1$, Proposition [\[prop:visibility\]](#prop:visibility){reference-type="ref" reference="prop:visibility"} and [\[eq:actual-vectors\]](#eq:actual-vectors){reference-type="eqref" reference="eq:actual-vectors"} give the uniform statement $$\label{eq:degree-all-n}
d_n:=\operatorname{deg}(F_g^n)=\mathbf{e}_4^{\mathsf{T}}C_g^n\mathbf{1}
\qquad\text{for every }n\geq0.$$ This proves Theorem [\[thm:degree\]](#thm:degree){reference-type="ref" reference="thm:degree"}. Notice the division of labor: support selection identifies a formal matrix, cone invariance keeps its choices valid, carry proves the new gradient is not hidden by the old coordinate, coefficient positivity makes the chosen degree real, and visibility converts a vector recurrence into the scalar total degree.

# Quartic Spectrum and the Scalar Recurrence {#sec:spectrum}

## Principal-minor derivation

For a $4\times4$ matrix $C$, let $e_j(C)$ denote the sum of its principal $j\times j$ minors. The characteristic polynomial is $$\label{eq:principal-formula}
\det(tI_4-C)
=t^4-e_1(C)t^3+e_2(C)t^2-e_3(C)t+e_4(C).$$ For $C_g$, the trace is immediately $$\label{eq:e1}
e_1(C_g)=4g+10.$$ For completeness, all remaining nontrivial principal minors are displayed in Table [3](#tab:minors){reference-type="ref" reference="tab:minors"}. Their signs are retained before summation; replacing the table by only its two sums would hide most of the quartic calculation.

::: {#tab:minors}
  ---------------------- --------------- --------- ----------------------

   (r)1-2(l)3-4 Indices                   Indices
           $12$            $-3g^2-7g+18$   $123$     $-3g^3+23g^2-52g+36$
           $13$              $g^2-7g+10$   $124$     $-3g^3+20g^2-35g+18$
           $14$               $g^2-6g+5$   $134$      $-3g^3+12g^2-15g+6$
           $23$              $g^2-8g+12$   $234$     $-3g^3+15g^2-24g+12$
           $24$               $g^2-7g+6$
           $34$             $-3g^2+9g-6$
  ---------------------- --------------- --------- ----------------------

  : The six principal $2\times2$ minors and four principal $3\times3$ minors of $C_g$.
:::

Here is the arithmetic behind the table. For the order-two minors, direct diagonal subtraction gives $$\label{eq:two-minor-expansions}
\begin{aligned}
M_{12}
&=(g+7)(g+6)-(2g+4)(2g+6)
=-3g^2-7g+18,\\
M_{13}
&=(g+7)(g-2)-6(2g-4)
=g^2-7g+10,\\
M_{14}
&=(g+7)(g-1)-6(2g-2)
=g^2-6g+5,\\
M_{23}
&=(g+6)(g-2)-6(2g-4)
=g^2-8g+12,\\
M_{24}
&=(g+6)(g-1)-6(2g-2)
=g^2-7g+6,\\
M_{34}
&=(g-2)(g-1)-(2g-4)(2g-2)
=-3g^2+9g-6.
\end{aligned}$$ This list also checks that principal means using the same index set for rows and columns; several nonprincipal minors have superficially similar entries but do not enter [\[eq:principal-formula\]](#eq:principal-formula){reference-type="eqref" reference="eq:principal-formula"}.

For the four order-three minors, expanding along the first displayed row of each principal submatrix yields $$\label{eq:three-minor-123}
\begin{aligned}
M_{123}
={}&(g+7)\bigl((g+6)(g-2)-6(2g-4)\bigr)\\
&-(2g+4)\bigl((2g+6)(g-2)-6(2g-4)\bigr)\\
&+6\bigl((2g+6)(2g-4)-(g+6)(2g-4)\bigr)\\
={}&-3g^3+23g^2-52g+36,
\end{aligned}$$ $$\label{eq:three-minor-124}
\begin{aligned}
M_{124}
={}&(g+7)\bigl((g+6)(g-1)-6(2g-2)\bigr)\\
&-(2g+4)\bigl((2g+6)(g-1)-6(2g-2)\bigr)\\
&+6\bigl((2g+6)(2g-2)-(g+6)(2g-2)\bigr)\\
={}&-3g^3+20g^2-35g+18,
\end{aligned}$$ $$\label{eq:three-minor-134}
\begin{aligned}
M_{134}
={}&(g+7)\bigl((g-2)(g-1)-(2g-4)(2g-2)\bigr)\\
&-6\bigl((2g-4)(g-1)-(2g-4)(2g-2)\bigr)\\
&+6\bigl((2g-4)(2g-2)-(g-2)(2g-2)\bigr)\\
={}&-3g^3+12g^2-15g+6,
\end{aligned}$$ and $$\label{eq:three-minor-234}
\begin{aligned}
M_{234}
={}&(g+6)\bigl((g-2)(g-1)-(2g-4)(2g-2)\bigr)\\
&-6\bigl((2g-4)(g-1)-(2g-4)(2g-2)\bigr)\\
&+6\bigl((2g-4)(2g-2)-(g-2)(2g-2)\bigr)\\
={}&-3g^3+15g^2-24g+12.
\end{aligned}$$ The last two expansions share their final two cofactors, but their leading diagonal entry differs by one. This accounts for the difference between their cubic expressions and supplies a quick cross-check on their signs.

Adding the six entries in the left half gives $$\label{eq:e2}
e_2(C_g)=-2g^2-26g+45.$$ Adding the four entries in the right half gives $$\label{eq:e3}
e_3(C_g)=-12g^3+70g^2-126g+72.$$ There is also a short independent calculation of the determinant. In $A_g$, the first two rows provide diagonal factors $g-1$ and $g-2$, while the remaining $2\times2$ diagonal block is $$\begin{pmatrix}1&2\\2&1\end{pmatrix}$$ with determinant $-3$. Thus $$\det A_g=-3(g-1)(g-2).$$ The matrix $B_g$ has the same mixed block in its first two coordinates and diagonal factors $g-2$, $g-1$ in the last two, so $$\det B_g=-3(g-1)(g-2).$$ Consequently, $$\label{eq:e4}
e_4(C_g)=\det C_g=9(g-1)^2(g-2)^2.$$

Substitution of [\[eq:e1\]](#eq:e1){reference-type="eqref" reference="eq:e1"}--[\[eq:e4\]](#eq:e4){reference-type="eqref" reference="eq:e4"} into [\[eq:principal-formula\]](#eq:principal-formula){reference-type="eqref" reference="eq:principal-formula"} proves $$\label{eq:R}
\begin{aligned}
R_g(t)=\det(tI_4-C_g)
={}&t^4-(4g+10)t^3+(-2g^2-26g+45)t^2\\
&+(12g^3-70g^2+126g-72)t\\
&+9(g-1)^2(g-2)^2.
\end{aligned}$$ The positive $t$-coefficient admits the useful check $$\label{eq:t-factor}
12g^3-70g^2+126g-72
=2(g-3)(2g-3)(3g-4).$$ Evaluation at one is another independent check: $$\label{eq:R-one}
R_g(1)=3g(g-1)(3g^2-11g+4)>0
\qquad(g\geq10).$$ In particular, $1$ is not an eigenvalue of $C_g$. This fact will agree with the shifted-kernel comparison in Section [9](#sec:comparison){reference-type="ref" reference="sec:comparison"}.

## The exact scalar recurrence

Cayley--Hamilton applied to [\[eq:R\]](#eq:R){reference-type="eqref" reference="eq:R"} gives $$R_g(C_g)=0.$$ Multiplying this matrix identity on the right by $C_g^n\mathbf{1}$ and on the left by $\mathbf{e}_4^{\mathsf{T}}$, then using [\[eq:degree-all-n\]](#eq:degree-all-n){reference-type="eqref" reference="eq:degree-all-n"}, yields the order-four relation $$\label{eq:recurrence}
\begin{aligned}
d_{n+4}={}&(4g+10)d_{n+3}
+(2g^2+26g-45)d_{n+2}\\
&-(12g^3-70g^2+126g-72)d_{n+1}\\
&-9(g-1)^2(g-2)^2d_n
\end{aligned}$$ for all $n\geq0$. This is an exact annihilating recurrence for the total degree sequence. No claim that it is a minimal recurrence is needed here; the irreducibility result in the next section applies only to the certified residue class.

The signs in [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} follow directly from moving the last four terms of $R_g(C_g)C_g^n=0$ to the opposite side. In particular, the negative coefficient of $t^2$ in $R_g$ becomes the positive coefficient $2g^2+26g-45$ of $d_{n+2}$, whereas the positive coefficients of $t$ and of the constant term become negative recurrence coefficients. This sign audit is useful because positivity of the degree sequence does not mean that every coefficient in one of its linear recurrences must be positive.

The matrix formula supplies the initial data without a separate extrapolation: $$d_0=1,\qquad d_1=\mathbf{e}_4^{\mathsf{T}}C_g\mathbf{1}=7g-7,$$ and, more generally, $d_j=\mathbf{e}_4^{\mathsf{T}}C_g^j\mathbf{1}$ for $j=0,1,2,3$. Thus [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}, together with these four explicit matrix values, determines the same sequence as [\[eq:degree-all-n\]](#eq:degree-all-n){reference-type="eqref" reference="eq:degree-all-n"}. We retain the matrix form for the later initial values because it is shorter and preserves their provenance from actual coordinate degrees.

## Perron pairing and the dynamical degree

Every entry of $C_g$ in [\[eq:C\]](#eq:C){reference-type="eqref" reference="eq:C"} is strictly positive for $g\geq10$. Thus $C_g$ is primitive. Perron--Frobenius supplies a simple positive eigenvalue $\rho(C_g)$, positive right and left eigenvectors $r$ and $\ell$, and strict domination in modulus over the other eigenvalues. With the normalization $\ell^{\mathsf{T}}r=1$, $$\rho(C_g)^{-n}C_g^n\longrightarrow r\ell^{\mathsf{T}}.$$ Both relevant pairings are nonzero and positive: $$\mathbf{e}_4^{\mathsf{T}}r>0,\qquad
\ell^{\mathsf{T}}\mathbf{1}>0.$$ It follows from [\[eq:degree-all-n\]](#eq:degree-all-n){reference-type="eqref" reference="eq:degree-all-n"} that $$\frac{d_n}{\rho(C_g)^n}
\longrightarrow
(\mathbf{e}_4^{\mathsf{T}}r)(\ell^{\mathsf{T}}\mathbf{1})>0,$$ and hence $$\label{eq:lambda-rho}
\lambda_1(F_g)
:=\lim_{n\to\infty}\operatorname{deg}(F_g^n)^{1/n}
=\rho(C_g).$$ The limit here is proved from the exact visible recurrence and positive matrix. Equation [\[eq:lambda-rho\]](#eq:lambda-rho){reference-type="eqref" reference="eq:lambda-rho"} is not an entropy statement and is not used to infer any analytic or measure-theoretic property of $F_g$.

# Modulo Five, Perron Infinitude, and the $g=9$ Boundary {#sec:modfive}

## Reduction and exclusion of linear factors

Assume $$g\equiv3\pmod5.$$ Reducing every coefficient in [\[eq:R\]](#eq:R){reference-type="eqref" reference="eq:R"} modulo five gives the fixed polynomial $$\label{eq:f-five}
\overline{R}_g(t)
=f(t):=t^4-2t^3-t^2+1\in\mathbb{F}_{5}[t].$$ Direct substitution gives $$\label{eq:f-values}
\bigl(f(0),f(1),f(2),f(3),f(4)\bigr)=(1,4,2,4,3)
\quad\text{in }\mathbb{F}_{5}.$$ Thus $f$ has no root in $\mathbb{F}_{5}$, and hence no linear factor.

## Exclusion of quadratic factors

A reducible monic quartic without a linear factor must be a product of two monic quadratics. Suppose, for contradiction, that $$f(t)=(t^2+at+b)(t^2+ct+d)$$ with $a,b,c,d\in\mathbb{F}_{5}$. Coefficient comparison with [\[eq:f-five\]](#eq:f-five){reference-type="eqref" reference="eq:f-five"} gives the complete system $$\label{eq:factor-system}
a+c=3,\qquad
ac+b+d=4,\qquad
ad+bc=0,\qquad
bd=1.$$ The last equation leaves exactly four ordered pairs: $$\label{eq:bd-pairs}
(b,d)\in\{(1,1),(2,3),(3,2),(4,4)\}.$$

If $(b,d)=(1,1)$ or $(4,4)$, then the coefficient of $t$ is $$ad+bc=b(a+c)=3b\neq0,$$ contradicting [\[eq:factor-system\]](#eq:factor-system){reference-type="eqref" reference="eq:factor-system"}. If $(b,d)=(2,3)$, the first and third equations in [\[eq:factor-system\]](#eq:factor-system){reference-type="eqref" reference="eq:factor-system"} become $$a+c=3,\qquad3a+2c=0.$$ They give $a=c=4$. The $t^2$-coefficient would then be $$ac+b+d=4\cdot4+2+3=1\neq4
\quad\text{in }\mathbb{F}_{5},$$ again a contradiction. For $(b,d)=(3,2)$, the equations are $$a+c=3,\qquad2a+3c=0.$$ They again give $a=c=4$, followed by the same contradiction in the $t^2$-coefficient. The four possibilities in [\[eq:bd-pairs\]](#eq:bd-pairs){reference-type="eqref" reference="eq:bd-pairs"} are exhausted. Therefore $f$ has neither a linear factor nor a quadratic factor and is irreducible in $\mathbb{F}_{5}[t]$.

For clarity, the preceding case split is exhaustive for a structural reason. A proper factorization of a degree-four polynomial has factor degrees $1+3$ or $2+2$. Equation [\[eq:f-values\]](#eq:f-values){reference-type="eqref" reference="eq:f-values"} excludes the first case. In the second, the factors may be taken monic because $f$ is monic, which gives exactly the coefficient system [\[eq:factor-system\]](#eq:factor-system){reference-type="eqref" reference="eq:factor-system"}. Moreover, the nonzero constant term forces both $b$ and $d$ to be nonzero, and the four ordered pairs in [\[eq:bd-pairs\]](#eq:bd-pairs){reference-type="eqref" reference="eq:bd-pairs"} are precisely all solutions of $bd=1$ in $\mathbb{F}_{5}$. Hence no factor shape is omitted.

[\[prop:perron\]]{#prop:perron label="prop:perron"} For $$g=13,18,23,\ldots,$$ the number $\lambda_1(F_g)$ is a Perron algebraic integer of degree four. These numbers are pairwise distinct.

The polynomial $R_g$ is monic with integer coefficients, and its monic degree-four reduction $f$ is irreducible modulo five. Reduction together with Gauss's lemma makes $R_g$ irreducible over $\mathbb Q$. The spectral radius $\rho(C_g)$ is an algebraic integer because it is a root of the monic characteristic polynomial of the integer matrix $C_g$. Irreducibility makes $R_g$ its minimal polynomial, so the algebraic degree is four.

Recall that a Perron number is a real algebraic integer greater than one whose other algebraic conjugates have strictly smaller modulus. The spectral radius here is greater than one without an asymptotic approximation: applying $C_g$ to $\mathbf{1}$ gives a vector whose least entry already exceeds $\mathbf{1}$, so the elementary row-sum bound for a positive matrix gives $\rho(C_g)>1$. The irreducible characteristic polynomial is essential for the conjugate comparison. It ensures that every conjugate of $\rho(C_g)$ occurs among the four roots of $R_g$, and those roots are exactly the eigenvalues of $C_g$.

Every algebraic conjugate is another root of $R_g$, hence another eigenvalue of $C_g$. Since $C_g$ is positive, Perron--Frobenius makes the modulus of each other eigenvalue strictly smaller than $\rho(C_g)$. Thus $\rho(C_g)=\lambda_1(F_g)$ is a Perron number.

If two different parameters $g$ and $g'$ in the progression produced the same algebraic number, their monic irreducible minimal polynomials would be equal. Their $t^3$-coefficients would then satisfy $$-(4g+10)=-(4g'+10),$$ which forces $g=g'$. Therefore all values are distinct.

Proposition [\[prop:perron\]](#prop:perron){reference-type="ref" reference="prop:perron"} is exactly a certified residue-class quartic Perron subfamily. It does not assert irreducibility for parameters outside $g\equiv3\pmod5$, nor does it claim that quartic Perron numbers are new as a general class of dynamical degrees.

## The restricted boundary at $g=9$

The four seed margins in [\[eq:seed-margins\]](#eq:seed-margins){reference-type="eqref" reference="eq:seed-margins"} become, at $g=9$, $$\label{eq:g9-margins}
(1,0,-2,5).$$ Thus the second first-phase row ties at the ordinary seed, and the proposed pure branch in the third second-phase row loses there. Independently, the height constraint reaches equality: $$y+z=2=\frac{g-5}{2}=H_9$$ at $(x,y,z)=(1,1,1)$. The strict cone-and-selector induction used in this article therefore cannot start at $g=9$.

This boundary conclusion is narrow. The threshold statement is sharp only for the ordinary seed and selected itinerary proved here. The calculation does not exclude a different branch pattern, a different sufficient cone, or a different theorem at $g=9$ or below. In particular, it is not a global threshold for all degree dynamics of the displayed potentials.

# Cubic-Collapse Comparison, Limitations, and Conclusion {#sec:comparison}

## A common-kernel mechanism

We first isolate the elementary linear-algebra mechanism behind cubic collapse. It concerns the correction covectors in two matrices and is independent of the selector proof.

[\[lem:common-kernel\]]{#lem:common-kernel label="lem:common-kernel"} Let $$A=-I_r+\sum_{i=1}^{p}u_iv_i^{\mathsf{T}},
\qquad
B=-I_r+\sum_{j=1}^{q}s_jt_j^{\mathsf{T}}$$ be matrices over a field. Define $$E=
\bigcap_{i=1}^{p}\ker(v_i^{\mathsf{T}})
\cap
\bigcap_{j=1}^{q}\ker(t_j^{\mathsf{T}}).$$ Then $$E\subseteq\ker(BA-I_r),
\qquad
\dim E=r-\dim\mathop{\mathrm{span}}\{v_1,\ldots,v_p,t_1,\ldots,t_q\}
\geq r-p-q.$$

If $x\in E$, each rank-one correction vanishes on $x$. Therefore $$Ax=-x,\qquad Bx=-x,$$ and $$BAx=B(-x)=-Bx=x.$$ The inclusion follows. The dimension formula is rank--nullity applied to the linear map whose rows are the listed covectors; its rank is their span dimension and is at most $p+q$.

Equivalently, $$\ker(A+I_r)\cap\ker(B+I_r)\subseteq\ker(BA-I_r).$$ If $m=\dim E$, then the geometric multiplicity of the eigenvalue $1$ for $BA$ is at least $m$, so its algebraic multiplicity is also at least $m$. Consequently, $\det(tI_r-BA)$ is divisible by $(t-1)^m$. The lower bound $m\geq r-p-q$ implies that the residual factor has degree at most $p+q$ whenever that bound is nonnegative. This conclusion does not require the unit eigenspace to be semisimple, and it does not say that the residual degree equals $p+q$.

When the combined correction profile is small compared with $r$, this forces a unit eigenspace in the product and bounds the degree of the non-unit residual factor. It does not identify that residual factor and does not prove that the bound is attained. Thus Lemma [\[lem:common-kernel\]](#lem:common-kernel){reference-type="ref" reference="lem:common-kernel"} is an explanatory, nonnovel support-profile common-kernel lemma.

## The shifted kernels of the four-mode phases

For the matrices in [\[eq:intro-phase-matrices\]](#eq:intro-phase-matrices){reference-type="eqref" reference="eq:intro-phase-matrices"}, the two shifted matrices have the exact rank-one decompositions $$\label{eq:A-shift}
A_g+I_4
=g\mathbf{e}_1\mathbf{e}_1^{\mathsf{T}}
+(g-1)\mathbf{e}_2\mathbf{e}_2^{\mathsf{T}}
+2(\mathbf{e}_3+\mathbf{e}_4)\mathbf{1}^{\mathsf{T}}$$ and $$\label{eq:B-shift}
B_g+I_4
=2(\mathbf{e}_1+\mathbf{e}_2)\mathbf{1}^{\mathsf{T}}
+(g-1)\mathbf{e}_3\mathbf{e}_3^{\mathsf{T}}
+g\mathbf{e}_4\mathbf{e}_4^{\mathsf{T}}.$$ The first two rows of [\[eq:A-shift\]](#eq:A-shift){reference-type="eqref" reference="eq:A-shift"} force $x_1=x_2=0$, and the last two then force $x_3+x_4=0$. Hence $$\label{eq:A-shifted-kernel}
\ker(A_g+I_4)
=\mathop{\mathrm{span}}\{(0,0,1,-1)^{\mathsf{T}}\}.$$ Similarly, [\[eq:B-shift\]](#eq:B-shift){reference-type="eqref" reference="eq:B-shift"} forces $x_3=x_4=0$ and $x_1+x_2=0$, so $$\label{eq:B-shifted-kernel}
\ker(B_g+I_4)
=\mathop{\mathrm{span}}\{(1,-1,0,0)^{\mathsf{T}}\}.$$ The two lines in [\[eq:A-shifted-kernel\]](#eq:A-shifted-kernel){reference-type="eqref" reference="eq:A-shifted-kernel"} and [\[eq:B-shifted-kernel\]](#eq:B-shifted-kernel){reference-type="eqref" reference="eq:B-shifted-kernel"} have zero intersection.

It is important not to confuse these shifted kernels with ordinary kernels. The determinant calculation in Section [7](#sec:spectrum){reference-type="ref" reference="sec:spectrum"} gives $$\det A_g=\det B_g=-3(g-1)(g-2)\neq0
\qquad(g\geq10),$$ and therefore $$\label{eq:ordinary-kernels}
\ker(A_g)=\ker(B_g)=\{0\}.$$ The combined covector profile visible in [\[eq:A-shift\]](#eq:A-shift){reference-type="eqref" reference="eq:A-shift"}--[\[eq:B-shift\]](#eq:B-shift){reference-type="eqref" reference="eq:B-shift"} is $$\{\mathbf{e}_1^{\mathsf{T}},\mathbf{e}_2^{\mathsf{T}},\mathbf{1}^{\mathsf{T}},
\mathbf{e}_3^{\mathsf{T}},\mathbf{e}_4^{\mathsf{T}}\},$$ which spans the full four-dimensional dual space. Accordingly, the common-kernel mechanism forces no unit eigendirection. The independent characteristic-polynomial calculation agrees: $$R_g(1)=3g(g-1)(3g^2-11g+4)\neq0.$$

An endpoint-spiked product-shear profile with fewer independent correction covectors may leave a large common shifted kernel and hence a cubic non-unit spectral sector. The two extra pure branches in the present four-mode profile remove that forced sector. This is the precise sense in which the family lies beyond that cubic-collapse mechanism. Full covector span is not, by itself, sufficient for a quartic exact degree law: Theorems [\[thm:degree\]](#thm:degree){reference-type="ref" reference="thm:degree"} and [\[thm:spectrum\]](#thm:spectrum){reference-type="ref" reference="thm:spectrum"} also require the four selectors, all cone walls, both carries, leading-form survival, visibility, and the principal-minor and irreducibility calculations.

## Limitations

The boundaries of the result can now be stated without ambiguity.

-   The proof applies to the exact potentials [\[eq:intro-potentials\]](#eq:intro-potentials){reference-type="eqref" reference="eq:intro-potentials"}, their positive integer coefficients, and the order $T_g^+\circ S_g^+$. It does not cover arbitrary signs, coefficients, supports, or reversed and longer shear words.

-   Characteristic zero is used in Proposition [\[prop:survival\]](#prop:survival){reference-type="ref" reference="prop:survival"}. No positive-characteristic version is asserted.

-   The cone $\mathcal{K}_g$ is one explicit sufficient invariant ratio cone. The six-wall proof gives neither necessity nor a global optimality or maximality statement.

-   The boundary calculation at $g=9$ concerns the ordinary seed and the selected itinerary only. It is not a classification of smaller parameters.

-   The order-four relation [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} is an annihilating recurrence for all $g\geq10$. Minimality and irreducibility are not claimed for every parameter; irreducibility is certified only when $g\equiv3\pmod5$.

-   The common-kernel lemma is a diagnostic obstruction, not a classification of support profiles and not a sufficient-quartic theorem.

-   The degree and Perron conclusions do not imply entropy, integrability, conjugacy, genericity, periodic-point behavior, a minimal ambient dimension, or optimal sparsity.

## Conclusion

For the fixed Hamiltonian product-shear family, exact degree growth follows from a chain of certificates rather than from a guessed exponent matrix. The eight literal supports isolate four competitions. The four selectors are strict on $\mathcal{K}_g$; the six walls return every complete-step ratio to that cone; the two temporal carries ensure that fresh gradients dominate old coordinates; and positive integer coefficients in characteristic zero preserve the selected leading forms. Three further row comparisons and the positive matrix $C_g-A_g$ then establish strict fourth-coordinate visibility after every positive iterate, while the identity iterate is handled by its eight-way tie.

Each hypothesis has a visible point of use. The lower bound on $g$ controls selector and cone signs; integrality of $g$ defines the pure powers and the residue progression; the positive signs control coefficient survival; characteristic zero keeps positive integer coefficients nonzero; and the prescribed phase order fixes $C_g=B_gA_g$. Removing any one of these inputs would require a new argument rather than a formal restatement of the present proof.

The resulting certificate is therefore reproducible from the displayed supports and inequalities alone: every transition from the polynomial word to the scalar recurrence has an explicit intermediate statement that can be checked independently.

The resulting scalar formula is exact for all $n\geq0$, and its spectrum is computed without an omitted determinant step: the ten principal minors, two phase determinants, quartic polynomial, value at one, and Cayley--Hamilton recurrence are all explicit. A complete modulo-five linear-and-quadratic factor exclusion yields infinitely many pairwise distinct quartic Perron values. The shifted-kernel calculation finally explains why no unit sector is structurally forced in this support profile. These conclusions exhaust the stated scope; no priority, global classification, or optimality claim is attached to them.
