---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-minimal-brauer-jump"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/paper/main.pdf"
source_sha256: "e20e8905ec4f50d3a237ce5a36fba75b971e64e917cb556f886601803b6d01b0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Minimal Degree of a 2-Primary Brauer Jump on the Fourth Hénon Yukawa Surface

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the first finite base changes at which the algebraic Brauer quotient of a fixed smooth cubic surface can acquire 2-primary torsion. The normal field of the surface's twenty-seven lines has Galois group $W(E_6)$, and for every finite extension $L/\mathbf Q$ a nonzero 2-primary quotient forces the sharp divisibility $$36\mid [K\cap L:\mathbf Q]\mid [L:\mathbf Q].$$ Equality occurs exactly at the thirty-six conjugate fixed fields of double-six stabilizers; for a double-six $D$, the attaining field $F_D=K^{U_1}$, where $U_1\cong S_6\times C_2$, has an oriented quadratic extension $F_D(\sqrt{\delta_D})$. We construct a unique normalized quartic $Q_D$ by a determinant in a $60\times31$ exact restriction matrix and prove $\operatorname{div}(Q_D)=\mathcal E+\mathcal G$, the sum of the twelve lines of $D$. The quaternion $(\delta_D,Q_D/u_0^4)$ is then unramified and represents the unique nonzero element of $\mathop{\mathrm{Br}}(Y_{F_D})/\operatorname{im}\mathop{\mathrm{Br}}(F_D)$. The exact evidence enumerates thirty-six double-sixes, proves a rank-$30$ restriction theorem, and passes an independent theorem checker importing no producer theorem helper. The bounded 2026-08-15 screen did not locate a prior exact computation of this field--orientation--quaternion package for the fixed surface; generic resolvers and double-six Brauer classes are prior constructions rather than contributions of this paper. We make no local-evaluation, rational-point, or Brauer--Manin claim.
author:
- Anonymous Authors
bibliography:
- references.bib
date: August 2026
title: |
  The Minimal Degree of a 2-Primary Brauer Jump\
  on the Fourth Hénon Yukawa Surface
```

## Markdown 正文

# Introduction {#sec:introduction}

For a smooth cubic surface whose twenty-seven lines have the full incidence-compatible Galois group $W(E_6)$, the algebraic Brauer quotient may be trivial over the base yet acquire 2-torsion after a finite extension. How small can that extension be? We answer this for the exact surface $Y/\mathbf Q$ in [\[eq:cubic\]](#eq:cubic){reference-type="ref" reference="eq:cubic"}. The companion theorem package `henon_mu3_yukawa_line_field`, included in the anonymous supplement, proves that the common normal field $K$ of its lines satisfies $$\mathop{\mathrm{Gal}}(K/\mathbf Q)\cong W(E_6),\qquad |W(E_6)|=51840.$$ The degree-$27$ field $E$ of one line is non-Galois and differs from $K$. These are frozen inputs: we locate the first jump inside $K$, not recompute the line scheme.

Nonzero 2-primary cohomology has two classical branches. A quotient $\mathbf Z/2$ places the Galois image in a conjugate of the double-six stabilizer $U_1\cong S_6\times C_2$, of index $36$; a quotient $(\mathbf Z/2)^2$ places it in a conjugate of $U_3$, of index $720$. Finding one invariant double-six does not eliminate the second branch. The complete Swinnerton-Dyer--Elsenhans--Jahnel classification supplies this universal dichotomy [@SwinnertonDyer1993; @ElsenhansJahnel2010Brauer].

The result combines that classification with exact configuration arithmetic and a written descent argument. For an abelian group $A$, write $A[2]$ for its subgroup annihilated by $2$. For a finite extension $L/\mathbf Q$, set $$G_L=\mathop{\mathrm{Gal}}(\overline{\mathbf Q}/L),\qquad
 H_L=\mathop{\mathrm{im}}(G_L\to W(E_6)),\qquad
 N_L=\ker(G_L\to H_L).
\label{eq:intro-GL-HL-NL}$$ The cohomological passage from $G_L$ to $H_L$ is proved in [\[lem:inflation,eq:brauer-picard-bridge\]](#lem:inflation,eq:brauer-picard-bridge){reference-type="ref" reference="lem:inflation,eq:brauer-picard-bridge"}, applied with $k=L$.

[\[thm:main\]]{#thm:main label="thm:main"} Let $Y/\mathbf Q$ be the cubic surface in [\[eq:cubic\]](#eq:cubic){reference-type="ref" reference="eq:cubic"}, and let $K/\mathbf Q$ be the common normal field of its twenty-seven lines. For every finite extension $L/\mathbf Q$, $$\bigl(\operatorname{Br}(Y_{L})/\operatorname{im}\operatorname{Br}(L)\bigr)[2]\ne0
 \quad\Longrightarrow\quad
 36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q].
\label{eq:intro-divisibility}$$ Consequently the least possible degree is $36$. If $[L:\mathbf Q]=36$ and the left side of [\[eq:intro-divisibility\]](#eq:intro-divisibility){reference-type="ref" reference="eq:intro-divisibility"} is nonzero, then, inside the fixed algebraic closure, $$L=K\cap L=K^{wU_1w^{-1}}$$ for some $w\in W(E_6)$, and this subgroup stabilizes a unique embedded double-six. The thirty-six embedded fields so obtained form one $\mathbf Q$-isomorphism type.

For a selected double-six $D=\{\mathcal E,\mathcal G\}$, put $F_D=K^{U_1}$. There are exact invariants $\theta_D,\delta_D\in K$ such that $$\mathbf Q(\theta_D)=F_D=\mathbf Q(\delta_D),\qquad
 F_D'=K^{U_1^+}=F_D(\sqrt{\delta_D}),$$ where $U_1^+\cong S_6$ preserves the two sixers separately. Moreover, $$\operatorname{Br}(Y_{\mathbf Q})/\operatorname{im}\operatorname{Br}(\mathbf Q)=0,\qquad \operatorname{Br}(Y_{F_D})/\operatorname{im}\operatorname{Br}(F_D)\cong\mathbf Z/2.$$ There is a unique normalized determinant-defined quartic $Q_D$ satisfying $$\operatorname{div}_{Y_{F_D}}(Q_D)=\mathcal E+\mathcal G,$$ and the quaternion $$\mathcal A_D=(\delta_D,Q_D/u_0^4)$$ is unramified and represents the unique nonzero element of $\operatorname{Br}(Y_{F_D})/\operatorname{im}\operatorname{Br}(F_D)$.

The contributions are:

1.  the full divisibility chain and equality classification through both $U_1/U_3$ branches;

2.  exact degree-$36$ fields, their common normal closure $K$, and the oriented quadratic extension;

3.  a determinant quartic whose degree-exhausted divisor and integral Picard cocycle prove that $(\delta_D,Q_D/u_0^4)$ is unramified and nonzero.

Invariant double-sixes, orientation fields, and cyclic algebras are established mechanisms [@ElsenhansJahnel2010Brauer; @ElsenhansJahnel2010DoubleSix]; degree-$36$ resolvers and their moduli context are also prior art [@ElsenhansJahnel2012OrderThree; @FarbWolfson2019]. Our claim is instance-specific: the bounded 2026-08-15 screen did not locate a prior exact computation of the degree-36 double-six field, its orientation square, and the determinant-defined quaternion generator for this frozen Yukawa surface.

The proof is organized around the path visible in [\[fig:field-subgroup\]](#fig:field-subgroup){reference-type="ref" reference="fig:field-subgroup"}. fixes the surface, notation, sources, and evidence contract. proves the universal minimum. identify the fields and cohomological jump. The determinant quartic is constructed in [6](#sec:canonical-quartic){reference-type="ref" reference="sec:canonical-quartic"}; its divisor and quaternion class are proved in [7](#sec:quaternion){reference-type="ref" reference="sec:quaternion"}. Exact replay and limitations appear in [8](#sec:replay-scope){reference-type="ref" reference="sec:replay-scope"}. We compute no local evaluation and draw no conclusion about rational points, the Hasse principle, weak approximation, or a Brauer--Manin obstruction.

# Prior results, the frozen object, and the proof contract {#sec:setup-sources}

## The fixed surface and its line fields

In homogeneous coordinates $u_0,u_1,u_2,u_3$, let $$\begin{aligned}
F={}&75081586157u_0^3-28576620789u_0^2u_1
-122000922135u_0^2u_2-5364921951u_0^2u_3\nonumber\\
&+164150208636u_0u_1^2-415458334296u_0u_1u_2
+151070718312u_0u_1u_3\nonumber\\
&+1158143874300u_0u_2^2+114691988016u_0u_2u_3
+113572676646u_0u_3^2\nonumber\\
&+6898957820u_1^3+1132596902196u_1^2u_2
-30413540316u_1^2u_3\nonumber\\
&-2054867641020u_1u_2^2+151980984216u_1u_2u_3
+36794420832u_1u_3^2\nonumber\\
&+2646295985484u_2^3+560186573940u_2^2u_3
+706181383584u_2u_3^2+1884468968u_3^3,
\label{eq:cubic}\end{aligned}$$ and set $Y=V(F)\subset\mathbf P^3_{\mathbf Q}$. Its primitive, positive-leading normalization fixes the common scalar. The upstream exact theorem proves that $Y$ is smooth and geometrically irreducible and that its Fano scheme of lines is connected of degree $27$. Write $E/\mathbf Q$ for that non-Galois residue field and $K/\mathbf Q$ for its normal closure. The frozen arithmetic input is $$=27,\qquad E\ne K,\qquad
 \mathop{\mathrm{Gal}}(K/\mathbf Q)\cong W(E_6),\qquad |W(E_6)|=51840.
\label{eq:frozen-line-field}$$ Thus $K$ is the common normal field of the lines; $E$ is not used as a configuration field.

Let $$\Lambda=\operatorname{Pic}(Y_{\overline{\mathbf Q}})$$ be the rank-seven geometric Picard lattice. In a marked blow-up model we use the basis $h,e_1,\ldots,e_6$, with intersection form $\operatorname{diag}(1,-1,\ldots,-1)$, and hyperplane class $$H_Y=3h-e_\Sigma,\qquad e_\Sigma=e_1+\cdots+e_6.
\label{eq:picard-basis}$$ The $27$ line classes are $e_i$, $h-e_i-e_j$, and $2h-\sum_{j\ne i}e_j$. Their intersection graph is the exact Schläfli configuration used throughout. The anonymous supplement names the surface package `henon_mu3_rational_yukawa_surface` and the companion line-field package `henon_mu3_yukawa_line_field`; no external bibliographic claim is attached to those internal package names.

## Double-sixes and fixed fields

A *sixer* is a set of six pairwise skew lines. A double-six is an unordered pair $D=\{\mathcal E,\mathcal G\}$ of opposite sixers; the same symbols $\mathcal E$ and $\mathcal G$ denote the corresponding effective sums of six lines. Fix one $D$, and choose the marking in [\[eq:picard-basis\]](#eq:picard-basis){reference-type="ref" reference="eq:picard-basis"} so that $$=e_\Sigma,\qquad [\mathcal G]=12h-5e_\Sigma.
\label{eq:marked-double-six}$$ Define $$\begin{aligned}
 U_1&=\mathop{\mathrm{Stab}}_{W(E_6)}(D)\cong S_6\times C_2,\\
 U_1^+&=\mathop{\mathrm{Stab}}_{W(E_6)}(\mathcal E)\cap\mathop{\mathrm{Stab}}_{W(E_6)}(\mathcal G)\cong S_6,\\
 F_D&=K^{U_1},\qquad F_D'=K^{U_1^+}.
\label{eq:basic-fields}\end{aligned}$$ Thus $U_1^+$ has index two in $U_1$; the nontrivial element of the quotient exchanges the two sixers. The other subgroup needed for the universal argument is $$U_3\cong(S_3\times S_3)\rtimes C_2,\qquad
 |U_3|=72,\qquad [W(E_6):U_3]=720.$$ It stabilizes a classical triple of azygetic double-sixes. The selected machine model of $U_1$ will not be used as a substitute for the theorem classifying every subgroup with nonzero 2-primary cohomology. Whenever an $S_6$-action appears below, it means this embedded subgroup $U_1^+$, not an unspecified abstract copy.

## Prior work by mathematical role

#### Picard cohomology and the 2-primary alternatives.

Swinnerton-Dyer identifies the algebraic Brauer quotient over an algebraic number field with Picard cohomology and proves that its possible nonzero 2-primary parts on a cubic surface are $\mathbf Z/2$ and $(\mathbf Z/2)^2$ [@SwinnertonDyer1993]. Elsenhans and Jahnel place the corresponding Galois images inside $U_1$ and $U_3$, respectively, and prove the restriction and class-map statements [@ElsenhansJahnel2010Brauer]. These source theorems, not the selected subgroup computation, supply the universal quantifier in [\[thm:degree\]](#thm:degree){reference-type="ref" reference="thm:degree"}.

#### Orientation and cyclic algebras.

The index-two orientation field and the cyclic algebra obtained from a norm divisor are prior mechanisms [@ElsenhansJahnel2010Brauer]. Explicit descent, including a full-$U_1$ example with line orbits $[12,15]$, also predates this instance [@ElsenhansJahnel2010DoubleSix]. What is computed here is the orientation square and canonical norm-divisor quartic for [\[eq:cubic\]](#eq:cubic){reference-type="ref" reference="eq:cubic"}.

#### Resolvers and moduli.

A degree-$36$ double-six resolver is already explicit [@ElsenhansJahnel2012OrderThree], and the associated moduli covers occur in resolvent-degree theory [@FarbWolfson2019]. We claim no generic resolver construction; the resolver here selects an exact subfield of $K$.

#### The number-field bridge.

The subgroup statements concern only finite subgroups of $W(E_6)$, the integral lattice, and line configurations, while Swinnerton-Dyer works over algebraic number fields. We construct the norm divisor directly over $F_D$ and use the number-field Hochschild--Serre sequence, for which Viray is a modern supporting locator [@Viray2023].

## Source, machine, and written-bridge contract

Source theorems control every possible image, exact arithmetic verifies this instance, and written algebraic geometry connects them to fields, divisors, and Brauer classes. Their division of labor is recorded in [1](#tab:dependency-contract){reference-type="ref" reference="tab:dependency-contract"}.

::: {#tab:dependency-contract}
  Claim              Source theorem                                                         Exact instance input                                      Written bridge
  ------------------ ---------------------------------------------------------------------- --------------------------------------------------------- ---------------------------------------------------------------
  Universal degree   Complete $\mathbf Z/2$--$U_1$, $(\mathbf Z/2)^2$--$U_3$ alternatives   Full $W(E_6)$ line field                                  $K^{H_L}=K\cap L$, index factors, tower law
  Equality fields    Same classification                                                    $U_1$ index, core, normalizer, and 36 configurations      Equality of indices and Galois correspondence
  Brauer jump        Number-field Picard/Brauer identification                              Integral $H^1(W(E_6),\Lambda)$ and $H^1(U_1,\Lambda)$     Inflation and Hochschild--Serre
  Exact fields       General resolver/descent context only                                  Resolver coefficients, irreducibility, stabilizers        Orbit--stabilizer and fixed fields
  Quartic            None                                                                   Gauge, $60\times31$ matrix, nonzero pivot, restrictions   Hilbert--90 descent and ambient lifting
  Quaternion         General double-six class mechanism                                     Orientation, line distinctness, Picard action             Degree exhaustion, norm-divisor criterion, cocycle comparison

  : Every theorem claim is split into its source, exact-instance, and written components. No column silently certifies another.
:::

The exact tuple used below has the intentionally layer-specific machine status

`PREFREEZE_CODE_RESULTS_PASS`

Paper and full-project identities are separate external records, so the machine envelope is never cited as its own release provenance.

# The universal minimum-degree theorem {#sec:minimal-degree}

This section proves the part of [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} that quantifies over every finite extension $L/\mathbf Q$. The exact $U_1$ calculation enters only after the complete source theorem has reduced the possibilities to two branches.

[\[lem:intersection-fixed-field\]]{#lem:intersection-fixed-field label="lem:intersection-fixed-field"} Let $L/\mathbf Q$ be finite, put $G_L=\mathop{\mathrm{Gal}}(\overline{\mathbf Q}/L)$, and let $$H_L=\mathop{\mathrm{im}}\!\left(G_L\longrightarrow\mathop{\mathrm{Gal}}(K/\mathbf Q)\right).
\label{eq:def-HL}$$ Then $$K^{H_L}=K\cap L,\qquad
 [K\cap L:\mathbf Q]=[W(E_6):H_L].$$

Because $K/\mathbf Q$ is finite Galois, restriction identifies the image of $G_L$ with $\mathop{\mathrm{Gal}}(K/K\cap L)$. Its fixed field in $K$ is therefore $K\cap L$. The degree formula follows from the Galois correspondence and [\[eq:frozen-line-field\]](#eq:frozen-line-field){reference-type="ref" reference="eq:frozen-line-field"}.

[\[thm:degree\]]{#thm:degree label="thm:degree"} If $L/\mathbf Q$ is finite and $\bigl(\operatorname{Br}(Y_{L})/\operatorname{im}\operatorname{Br}(L)\bigr)[2]\ne0$, then $$36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q].
\label{eq:degree-chain}$$ If $[L:\mathbf Q]=36$ and $\bigl(\operatorname{Br}(Y_{L})/\operatorname{im}\operatorname{Br}(L)\bigr)[2]\ne0$, then $$L=K\cap L=K^{wU_1w^{-1}}
\label{eq:equality-field}$$ for some $w\in W(E_6)$, with a unique double-six embedded in the fixed algebraic closure. Conversely, each field $K^{wU_1w^{-1}}$ has degree $36$, and its Brauer quotient is nonzero.

Since $Y_{\overline{\mathbf Q}}$ is rational, $\mathop{\mathrm{Br}}(Y_{\overline{\mathbf Q}})=0$. The inflation and number-field Hochschild--Serre identifications in [\[lem:inflation,eq:brauer-picard-bridge\]](#lem:inflation,eq:brauer-picard-bridge){reference-type="ref" reference="lem:inflation,eq:brauer-picard-bridge"}, applied with $k=L$, turn the hypothesis into $$H^1(H_L,\Lambda)[2]\ne0.$$ The complete 2-primary classification [@SwinnertonDyer1993; @ElsenhansJahnel2010Brauer] gives exactly the two containments in [2](#tab:two-branches){reference-type="ref" reference="tab:two-branches"}, for a suitable $w\in W(E_6)$.

::: {#tab:two-branches}
   2-primary quotient      forced containment              ambient index
  -------------------- --------------------------- ------------------------------
     $\mathbf Z/2$      $H_L\subseteq wU_1w^{-1}$        $[W(E_6):U_1]=36$
   $(\mathbf Z/2)^2$    $H_L\subseteq wU_3w^{-1}$   $[W(E_6):U_3]=720=36\cdot20$

  : Both complete classification branches force divisibility by $36$, but only the $U_1$ branch can attain index $36$.
:::

In the first branch, the subgroup index factors as $$=36[U_1:w^{-1}H_Lw].
\label{eq:u1-index-factor}$$ In the second, $$=720[U_3:w^{-1}H_Lw].
\label{eq:u3-index-factor}$$ Thus $36\mid[W(E_6):H_L]$ in either case. By [\[lem:intersection-fixed-field\]](#lem:intersection-fixed-field){reference-type="ref" reference="lem:intersection-fixed-field"}, this is the first divisibility in [\[eq:degree-chain\]](#eq:degree-chain){reference-type="ref" reference="eq:degree-chain"}. The inclusion $K\cap L\subseteq L$ and the tower law give the second.

Now suppose, in addition, that $[L:\mathbf Q]=36$. Every factor in [\[eq:degree-chain\]](#eq:degree-chain){reference-type="ref" reference="eq:degree-chain"} is one, so $L=K\cap L$ and $[W(E_6):H_L]=36$. The index-$720$ branch is impossible. forces $H_L=wU_1w^{-1}$, and the fixed-field statement in [\[eq:equality-field\]](#eq:equality-field){reference-type="ref" reference="eq:equality-field"} follows.

The exact configuration action verifies that $U_1$ is self-normalizing and is the stabilizer of exactly one double-six. Therefore its conjugates are indexed by $$[W(E_6):N_{W(E_6)}(U_1)]=[W(E_6):U_1]=36,$$ and they correspond to the thirty-six double-sixes. Distinct conjugate subgroups have distinct fixed fields by Galois correspondence. This proves uniqueness of the embedded field attached to $D$. The fields are permuted transitively by $W(E_6)=\mathop{\mathrm{Gal}}(K/\mathbf Q)$, hence form a single $\mathbf Q$-isomorphism type.

Conversely, $K^{wU_1w^{-1}}$ has degree $36$. The exact integral calculation $H^1(U_1,\Lambda)\cong\mathbf Z/2$, together with the arithmetic bridge proved in [5](#sec:brauer-jump){reference-type="ref" reference="sec:brauer-jump"}, shows that its Brauer quotient is nonzero.

[\[cor:sharp-threshold\]]{#cor:sharp-threshold label="cor:sharp-threshold"} The smallest degree of a finite extension $L/\mathbf Q$ for which $\bigl(\operatorname{Br}(Y_{L})/\operatorname{im}\operatorname{Br}(L)\bigr)[2]\ne0$ is $36$. Every such degree is divisible by $36$.

The divisibility is [\[eq:degree-chain\]](#eq:degree-chain){reference-type="ref" reference="eq:degree-chain"}; existence in degree $36$ is the converse part of [\[thm:degree\]](#thm:degree){reference-type="ref" reference="thm:degree"}.

The existence of a selected $U_1$-fixed configuration proves attainment, not universal minimality. Without the $(\mathbf Z/2)^2$--$U_3$ row in [2](#tab:two-branches){reference-type="ref" reference="tab:two-branches"}, the proof would leave an uncontrolled family of Galois images. The fact that $720$ is itself divisible by $36$ is what allows the two branches to yield one sharp divisibility theorem.

# Exact double-six and orientation fields {#sec:double-six-fields}

The degree theorem identifies the subgroup that must occur at equality. We now identify its fixed field inside the particular extension $K/\mathbf Q$. The construction begins with characteristic-zero incidence, passes to two separating orbit invariants, and ends with a degree-$12$ carrier for the selected lines.

## The exact configuration set

On the complete Grassmann chart used to construct $E$, let $\widetilde g(d)\in\mathbf Z[d]$ be the raw primitive degree-$27$ eliminant, let $c_g=[d^{27}]\widetilde g\ne0$, and put $$g(d)=c_g^{-1}\widetilde g(d).
\label{eq:monic-eliminant}$$ A geometric line is recovered from a root $x=d$ of the monic eliminant $g$. The remaining line coordinates are rational polynomial functions of $x$. For roots $x,y$, exact divided differences give a polynomial $J(x,y)$ whose vanishing is equivalent to incidence of the corresponding lines. In the algebra $(\mathbf Q[x]/(g(x)))[y]$, put $$H_x(y)=\gcd_y(g(y),J(x,y)).
\label{eq:incidence-gcd}$$ The characteristic-zero identities are $$\deg_yH_x=10,\qquad \gcd(H_x,y-x)=1,\qquad
 g(y)=H_x(y)Q_x(y),\quad \deg_yQ_x=17.
\label{eq:incidence-identities}$$ Thus every line meets exactly ten other lines, with no diagonal counted. The number of unordered meeting pairs is $27\cdot10/2=135$. Exact independent set enumeration then gives $$135\text{ meeting pairs},\qquad
 72\text{ sixers},\qquad
 36\text{ double-sixes}.
\label{eq:configuration-counts}$$ Good-prime graphs provide label-compatible cross-checks, while [\[eq:incidence-identities\]](#eq:incidence-identities){reference-type="ref" reference="eq:incidence-identities"} is the characteristic-zero authority; no ordering of approximate roots enters [\[eq:configuration-counts\]](#eq:configuration-counts){reference-type="ref" reference="eq:configuration-counts"}.

The exact $W(E_6)$-action on these configurations has stabilizer data $$|U_1|=1440,\quad [W(E_6):U_1]=36,\quad
 \mathop{\mathrm{core}}_{W(E_6)}(U_1)=1,\quad N_{W(E_6)}(U_1)=U_1.
\label{eq:u1-exact-data}$$ Its action on the twenty-seven lines has orbits of sizes $12$ and $15$, and $U_1$ fixes exactly the selected double-six.

## Separating invariants and resolvers

Let $d_i$ be the corresponding root of $g$, and define the fixed integral scaled coordinate $$\alpha_i=c_gd_i.
\label{eq:alpha-scaling}$$ For an unordered double-six $D$, define $$\theta_D=\sum_{\ell_i\in D}\alpha_i.
\label{eq:theta-def}$$ For an orientation $D=(\mathcal E,\mathcal G)$, define $$\beta_D=\sum_{\ell_i\in\mathcal E}\alpha_i-
          \sum_{\ell_i\in\mathcal G}\alpha_i,\qquad
 \delta_D=\beta_D^2.
\label{eq:beta-delta-def}$$ The orbit products $$R_\theta(T)=\prod_D(T-\theta_D),\qquad
 R_\delta(T)=\prod_D(T-\delta_D)
\label{eq:resolvers}$$ belong to $\mathbf Q[T]$, are separable and irreducible, and have degree $36$. Candidate-blind Chinese remaindering, with proved coefficient bounds, is recorded in [11](#app:incidence-resolvers){reference-type="ref" reference="app:incidence-resolvers"}. At two good reductions the factor-degree patterns are $$,\qquad [9,9,9,9].
\label{eq:resolver-factor-patterns}$$ Their proper subset-sum degree sets are disjoint, whereas a rational factor would give a degree in both. Hence the resolvers are irreducible.

The action on the exact orbit values gives $$\mathop{\mathrm{Stab}}(\theta_D)=\mathop{\mathrm{Stab}}(\delta_D)=U_1,\qquad
 \mathop{\mathrm{Stab}}(\beta_D)=U_1^+.
\label{eq:invariant-stabilizers}$$ The $36$ values $\delta_D$ are distinct, the $36$ values $\beta_D$ are nonzero, and all $72$ oriented values are separated exactly. The central involution $\iota\in U_1\setminus U_1^+$ sends $\beta_D$ to $-\beta_D$.

[\[thm:configuration-fields\]]{#thm:configuration-fields label="thm:configuration-fields"} For every double-six $D$, $$\mathbf Q(\theta_D)=F_D=\mathbf Q(\delta_D),
 \qquad
 F_D'=F_D(\beta_D)=F_D(\sqrt{\delta_D}).
\label{eq:field-identities}$$ Both resolvers in [\[eq:resolvers\]](#eq:resolvers){reference-type="ref" reference="eq:resolvers"} have normal closure $K$.

The stabilizers in [\[eq:invariant-stabilizers\]](#eq:invariant-stabilizers){reference-type="ref" reference="eq:invariant-stabilizers"} and the Galois correspondence give $$\mathbf Q(\theta_D)=K^{U_1}=\mathbf Q(\delta_D).$$ Their orbit sizes are $36$, so the degree-$36$ orbit polynomials are the minimal polynomials. The kernel of the coset action on the roots is $\mathop{\mathrm{core}}_{W(E_6)}(U_1)$, which is trivial by [\[eq:u1-exact-data\]](#eq:u1-exact-data){reference-type="ref" reference="eq:u1-exact-data"}. Hence the splitting field of either polynomial is the full $K$.

The same argument for $\beta_D$ gives $\mathbf Q(\beta_D)=K^{U_1^+}$. Since $U_1^+$ has index two in $U_1$ and $\beta_D^2=\delta_D$, this field is exactly the quadratic extension in [\[eq:field-identities\]](#eq:field-identities){reference-type="ref" reference="eq:field-identities"}.

summarizes the three invariants. The equality $\mathbf Q(\theta_D)=\mathbf Q(\delta_D)$ is a labeled stabilizer theorem. We neither need nor certify an expanded polynomial identity $\delta_D=P(\theta_D)$.

::: {#tab:field-invariants}
  invariant    stabilizer   orbit size   generated field   role
  ------------ ------------ ------------ ----------------- -----------------------------
  $\theta_D$   $U_1$        $36$         $F_D$             carrier primitive
  $\delta_D$   $U_1$        $36$         $F_D$             orientation square/radicand
  $\beta_D$    $U_1^+$      $72$         $F_D'$            oriented sixer

  : Exact orbit invariants, their stabilizers, and fixed fields.
:::

## The twelve-line carrier

Let $d_1,\ldots,d_{12}$ be the line parameters in $D$, and let the remaining fifteen roots of $g$ be $d_{13},\ldots,d_{27}$. The orbit decomposition $[12,15]$ gives monic polynomials $$A_{12}(d)=\prod_{i=1}^{12}(d-d_i)\in F_D[d],\qquad
 B_{15}(d)=\prod_{i=13}^{27}(d-d_i)\in F_D[d].
\label{eq:carrier-factors}$$ By [\[eq:theta-def,eq:alpha-scaling\]](#eq:theta-def,eq:alpha-scaling){reference-type="ref" reference="eq:theta-def,eq:alpha-scaling"}, its subtop coefficient is $$A_{12}=-\sum_{i=1}^{12}d_i=-\theta_D/c_g.
\label{eq:carrier-subtop}$$ With the fixed monic normalization of $g$, exact division and an independent forward product prove $$g(d)=A_{12}(d)B_{15}(d).
\label{eq:carrier-identity}$$ The $13\times36$ coefficient table is reconstructed with certified CRT bounds. Exact division and an independent forward product agree in all $28$ coefficients. Together with the orbit binding, this identity---not the stored table alone---certifies that $A_{12}$ cuts out exactly the twelve lines of $D$; see [11](#app:incidence-resolvers){reference-type="ref" reference="app:incidence-resolvers"}.

# Picard cohomology and the Brauer jump {#sec:brauer-jump}

The preceding sections locate the smallest possible image subgroup. To prove that its fixed field actually attains the bound, we now pass from exact integral group cohomology to the arithmetic Brauer quotient. This passage is a written number-field argument, not a semantic label attached to a Smith normal form.

## Integral cohomology

The exact Picard action is generated from the six standard $E_6$ reflections on the marked lattice $\Lambda$. Rebuilding cocycle relations and principal cocycles over $\mathbf Z$, and then computing Smith normal forms, gives $$H^1(W(E_6),\Lambda)=0,\qquad
 H^1(U_1,\Lambda)\cong\mathbf Z/2.
\label{eq:exact-H1}$$ The calculation is integral: it does not tensor with $\mathbf Q$, reduce modulo two, or infer torsion from a rational rank. The full Smith data and the independent cochain convention appear in [12](#app:cohomology){reference-type="ref" reference="app:cohomology"}.

[\[lem:inflation\]]{#lem:inflation label="lem:inflation"} Let $k/\mathbf Q$ be a number field, and suppose the $G_k$-action on $\Lambda$ has finite image $H\subseteq W(E_6)$. Then $$H^1(k,\Lambda)\cong H^1(H,\Lambda).$$

Let $N$ be the kernel of $G_k\to H$. It acts trivially on $\Lambda$. Hence $$H^1(N,\Lambda)=\operatorname{Hom}_{\mathrm{cont}}(N,\Lambda).$$ A continuous image of the profinite group $N$ in the discrete lattice $\Lambda$ is finite, while the torsion-free group $\Lambda$ has no nonzero finite subgroup. Thus $H^1(N,\Lambda)=0$. The inflation--restriction sequence now makes inflation $H^1(H,\Lambda)\to H^1(k,\Lambda)$ an isomorphism.

## The number-field Hochschild--Serre bridge

Over $\overline{\mathbf Q}$, a smooth cubic surface is rational, so $$\mathop{\mathrm{Br}}(Y_{\overline{\mathbf Q}})=0.
\label{eq:geometric-brauer-zero}$$ For a number field $k$, the low-degree Hochschild--Serre sequence has the segment $$\mathop{\mathrm{Br}}(Y_k)/\operatorname{im}\mathop{\mathrm{Br}}(k)
 \longrightarrow H^1(k,\operatorname{Pic}(Y_{\overline{\mathbf Q}}))
 \longrightarrow H^3(k,\mathbf G_m).
\label{eq:HS-segment}$$ The last group vanishes in this number-field setting. Because of [\[eq:geometric-brauer-zero\]](#eq:geometric-brauer-zero){reference-type="ref" reference="eq:geometric-brauer-zero"}, every Brauer class on $Y_k$ is algebraic, and [\[eq:HS-segment\]](#eq:HS-segment){reference-type="ref" reference="eq:HS-segment"} yields $$\mathop{\mathrm{Br}}(Y_k)/\operatorname{im}\mathop{\mathrm{Br}}(k)
 \cong H^1(k,\Lambda).
\label{eq:brauer-picard-bridge}$$ This is the number-field form of the Picard/Brauer bridge used by Swinnerton-Dyer [@SwinnertonDyer1993]; a modern account of the relevant low-degree sequence is given by Viray [@Viray2023].

[\[thm:brauer-jump\]]{#thm:brauer-jump label="thm:brauer-jump"} For the fixed cubic surface, $$\mathop{\mathrm{Br}}(Y)/\operatorname{im}\mathop{\mathrm{Br}}(\mathbf Q)=0,
\label{eq:base-brauer-zero}$$ whereas for every double-six field $F_D$, $$\mathop{\mathrm{Br}}(Y_{F_D})/\operatorname{im}\mathop{\mathrm{Br}}(F_D)\cong\mathbf Z/2.
\label{eq:FD-brauer}$$

Over $\mathbf Q$, the image on $\Lambda$ is the full group $W(E_6)$ by [\[eq:frozen-line-field\]](#eq:frozen-line-field){reference-type="ref" reference="eq:frozen-line-field"}. Apply [\[lem:inflation,eq:brauer-picard-bridge\]](#lem:inflation,eq:brauer-picard-bridge){reference-type="ref" reference="lem:inflation,eq:brauer-picard-bridge"} and the first equality in [\[eq:exact-H1\]](#eq:exact-H1){reference-type="ref" reference="eq:exact-H1"}; this proves [\[eq:base-brauer-zero\]](#eq:base-brauer-zero){reference-type="ref" reference="eq:base-brauer-zero"}.

For $k=F_D=K^{U_1}$, the image of $G_{F_D}$ on the lines and Picard lattice is $U_1$. The same two bridges and the second equality in [\[eq:exact-H1\]](#eq:exact-H1){reference-type="ref" reference="eq:exact-H1"} give [\[eq:FD-brauer\]](#eq:FD-brauer){reference-type="ref" reference="eq:FD-brauer"}. Thus the field constructed in [\[thm:configuration-fields\]](#thm:configuration-fields){reference-type="ref" reference="thm:configuration-fields"} attains the lower bound of [\[thm:degree\]](#thm:degree){reference-type="ref" reference="thm:degree"}.

identifies an algebraic/cohomological quotient. It neither evaluates its nonzero element at a completion of $F_D$ nor compares adelic points. The explicit global representative will be constructed in [7](#sec:quaternion){reference-type="ref" reference="sec:quaternion"}; no local conclusion is implicit in the group isomorphism above.

# The canonical determinant quartic {#sec:canonical-quartic}

We next turn the twelve-line carrier into one canonical quartic. Two rank bounds have different origins. Geometry produces a section and hence an upper bound on the restriction rank; exact arithmetic supplies a nonzero pivot and hence the lower bound. Keeping both halves visible prevents a finite-field minor from being mistaken for an existence proof.

## A proved quotient gauge

The space $H^0(\mathbf P^3_{F_D},\mathcal O(4))$ has dimension $35$. Since $F$ is a nonzero cubic, multiplication by $F$ embeds the four-dimensional space of linear forms: $$F\cdot H^0(\mathbf P^3_{F_D},\mathcal O(1))
 \subset H^0(\mathbf P^3_{F_D},\mathcal O(4)).
\label{eq:F-linear-subspace}$$ The quotient therefore has dimension $31$.

Put $$c=[u_0^3]F=75081586157.$$ Using the source basis $(Fu_0,Fu_1,Fu_2,Fu_3)$ and projecting to the coefficients of $$u_0^4,\quad u_0^3u_1,\quad u_0^3u_2,\quad u_0^3u_3,$$ gives the triangular block $$B_F=
 \begin{pmatrix}
 75081586157&0&0&0\\
 -28576620789&75081586157&0&0\\
 -122000922135&0&75081586157&0\\
 -5364921951&0&0&75081586157
 \end{pmatrix}.
\label{eq:gauge-block}$$ Its determinant is $$\det B_F=c^4
 =31778526453059635681033276764499400992765201\ne0.
\label{eq:gauge-determinant}$$ Consequently the four coefficient functionals restrict isomorphically to the subspace in [\[eq:F-linear-subspace\]](#eq:F-linear-subspace){reference-type="ref" reference="eq:F-linear-subspace"}. Every class modulo $F$ times a linear form has a unique representative in which those four coefficients vanish. This proves the gauge; deleting four monomials is not a convention made after inspecting the answer.

Let $$\mathcal M=(m_0,m_1,\ldots,m_{30})$$ be the remaining degree-four monomials in the locked descending lexicographic order, with $$m_0=u_0^2u_1^2.
\label{eq:normalization-monomial}$$ The complete order appears in [13](#app:quartic-specification){reference-type="ref" reference="app:quartic-specification"}.

## Restriction matrix

For each of the twelve carrier lines, restriction of $$Q=\sum_{j=0}^{30}q_jm_j$$ is a binary quartic and supplies five scalar equations. We use the monic carrier in the $d$-variable with the scaling $\alpha_i=c_gd_i$ and subtop normalization of [\[eq:alpha-scaling,eq:carrier-subtop\]](#eq:alpha-scaling,eq:carrier-subtop){reference-type="ref" reference="eq:alpha-scaling,eq:carrier-subtop"}. Reducing the five coefficients against that degree-$12$ carrier gives the exact matrix $$M_D\in\operatorname{Mat}_{60\times31}(F_D),\qquad M_Dq=0.
\label{eq:restriction-matrix}$$ Rows are ordered first by binary degree $0,\ldots,4$ and then by carrier degree $0,\ldots,11$. The column order is $\mathcal M$.

[\[prop:rank-upper\]]{#prop:rank-upper label="prop:rank-upper"} The matrix $M_D$ satisfies $\mathop{\mathrm{rank}}_{F_D}M_D\le30$.

By the marking fixed in [\[eq:marked-double-six\]](#eq:marked-double-six){reference-type="ref" reference="eq:marked-double-six"}, the divisor classes of the two sixers are $$[\mathcal E]=e_\Sigma,\qquad [\mathcal G]=12h-5e_\Sigma.$$ Hence $$\mathcal E+\mathcal G\sim12h-4e_\Sigma=4H_Y.
\label{eq:double-six-class}$$ This geometric equivalence does not by itself provide an $F_D$-rational section, so we descend it explicitly.

Put $k=F_D$, and choose a $k$-rational hyperplane section $H_0=\operatorname{div}_Y(\ell)$. Both the unordered divisor $\mathcal E+\mathcal G$ and $4H_0$ are $k$-rational. Over $\bar k$, choose $r\in\bar k(Y)^\times$ such that $$\operatorname{div}(r)=\mathcal E+\mathcal G-4H_0.$$ For $\sigma\in G_k$, the rational function $c_\sigma=\sigma(r)/r$ has zero divisor. Since $Y_{\bar k}$ is projective and integral, $c_\sigma\in\bar k^\times$. These scalars form a multiplicative cocycle. Hilbert theorem 90 gives $a\in\bar k^\times$ with $$c_\sigma=\frac{\sigma(a)}{a}.$$ It follows that $r_0=r/a$ lies in $k(Y)^\times$. The section $$s_D=r_0\ell^4\in H^0(Y_k,\mathcal O_Y(4))$$ is defined over $k$ and vanishes along $\mathcal E+\mathcal G$.

The hypersurface restriction sequence $$0\longrightarrow\mathcal O_{\mathbf P^3_k}(1)
 \xrightarrow{\;\cdot F\;}\mathcal O_{\mathbf P^3_k}(4)
 \longrightarrow\mathcal O_{Y_k}(4)\longrightarrow0
\label{eq:restriction-sequence}$$ is surjective on global sections because $H^1(\mathbf P^3_k,\mathcal O(1))=0$. Thus $s_D$ lifts to a nonzero ambient quartic class over $k$ that restricts to zero on the twelve lines. After applying the unique gauge, this class is a nonzero vector in $\ker M_D$. Therefore $\mathop{\mathrm{rank}}M_D\le30$.

[\[prop:rank-lower\]]{#prop:rank-lower label="prop:rank-lower"} The matrix $M_D$ has rank at least $30$.

Delete the $m_0$-column and select the zero-based row set $$\mathcal R=\{0,\ldots,10,12,\ldots,20,24,\ldots,29,36,37,38,48\}.
\label{eq:pivot-rows}$$ The resulting matrix $N_D$ is $30\times30$. Exact arithmetic at the denominator-good prime $7$ computes the norm of its determinant as $$\mathop{\mathrm{Norm}}_{F_D/\mathbf Q}(\det N_D)\equiv3\pmod7.$$ Thus $\det N_D\ne0$ in $F_D$. The replay verifies the same nonvanishing for all thirty-six conjugate configurations, and so $\mathop{\mathrm{rank}}M_D\ge30$.

[\[thm:canonical-quartic\]]{#thm:canonical-quartic label="thm:canonical-quartic"} For every double-six $D$, $$\mathop{\mathrm{rank}}_{F_D}M_D=30,\qquad \dim_{F_D}\ker M_D=1.$$ There is a unique kernel vector $$q_D=(1,q_1,\ldots,q_{30}),$$ and hence a unique normalized gauge representative $$Q_D=\sum_{j=0}^{30}q_jm_j
\label{eq:QD-definition}$$ whose restrictions to all twelve lines vanish. Every $q_j$ is defined by Cramer's rule from the locked matrix $N_D$.

give rank $30$, hence a one-dimensional kernel. If a kernel vector had $q_0=0$, its entries in columns $1,\ldots,30$ would lie in the kernel of the invertible selected minor $N_D$, so the vector would be zero. Thus $q_0\ne0$ on the kernel line and can be uniquely normalized to one. Solving the selected equations by Cramer's rule gives [\[eq:QD-definition\]](#eq:QD-definition){reference-type="ref" reference="eq:QD-definition"}; the independent replay then checks all $60$ equations, not only the pivot rows, at all $36$ conjugates.

::: {#tab:quartic-invariants}
  quartic invariant                           exact value
  -------------------------------------- ---------------------
  ambient monomials                              $35$
  subspace $F\cdot H^0(\mathcal O(1))$            $4$
  gauge columns                                  $31$
  restriction equations                      $12\cdot5=60$
  locked pivot size                          $30\times30$
  restriction rank / kernel dimension           $30/1$
  normalization                           $[u_0^2u_1^2]Q_D=1$

  : Dimension, gauge, rank, and normalization data for $Q_D$.
:::

At this stage we know that $Q_D$ is a nonzero quartic class and vanishes on the twelve carrier lines. We have not yet promoted those restrictions to a divisor equality; that is a separate geometric argument in [7](#sec:quaternion){reference-type="ref" reference="sec:quaternion"}.

# Divisor exhaustion and the explicit Brauer generator {#sec:quaternion}

The linear system in [6](#sec:canonical-quartic){reference-type="ref" reference="sec:canonical-quartic"} only proves vanishing on twelve lines. We first show that those lines exhaust the quartic divisor. We then use the oriented quadratic field to express the divisor of a rational function as a norm. Finally, and separately, we compare the associated Picard cocycle with the unique nonzero cohomology class.

## The exact divisor

[\[prop:divisor-exhaustion\]]{#prop:divisor-exhaustion label="prop:divisor-exhaustion"} The normalized determinant quartic satisfies $$\operatorname{div}_{Y_{F_D}}(Q_D)=\mathcal E+\mathcal G.
\label{eq:QD-divisor}$$

The exact carrier and restriction replay supplies twelve distinct lines and shows that $Q_D$ vanishes identically on each. Thus every line in $\mathcal E+\mathcal G$ is a prime component of $\operatorname{div}(Q_D)$ with multiplicity at least one. The quartic is not $F$ times a linear form: its gauge class is the normalized nonzero vector in $\ker M_D$. It therefore defines a nonzero effective divisor on $Y_{F_D}$ of class $4H_Y$.

Intersecting with a hyperplane gives $$(4H_Y)\cdot H_Y=4H_Y^2=4\deg(Y)=12.
\label{eq:quartic-degree}$$ Each of the twelve distinct carrier lines has hyperplane degree one, so the known components already contribute the full degree $12$. Every nonzero effective residual divisor has positive hyperplane degree, and any multiplicity greater than one would also increase the degree. Neither is possible. Hence [\[eq:QD-divisor\]](#eq:QD-divisor){reference-type="ref" reference="eq:QD-divisor"} holds exactly.

This argument is the geometric boundary between the last two machine gates: the $60\times31$ rank calculation constructs $Q_D$, while distinctness and [\[eq:quartic-degree\]](#eq:quartic-degree){reference-type="ref" reference="eq:quartic-degree"} identify its divisor. Restriction vanishing alone would not rule out a residual curve.

## The norm divisor and unramifiedness

Let $$\ell=u_0,\qquad \mathcal L_0=\operatorname{div}_Y(\ell),\qquad
 f_D=\frac{Q_D}{\ell^4}.
\label{eq:fD-def}$$ The exact line replay verifies that no carrier line is contained in the hyperplane $\ell=0$. Over the oriented field $F_D'$, define $$\mathcal D=\mathcal E-2\mathcal L_0.
\label{eq:oriented-divisor}$$ The nontrivial automorphism $\iota$ of $F_D'/F_D$ exchanges $\mathcal E$ and $\mathcal G$, and fixes $\mathcal L_0$. Therefore $$\begin{aligned}
 \mathop{\mathrm{Norm}}_{F_D'/F_D}(\mathcal D)
 &=\mathcal D+\iota(\mathcal D)\nonumber\\
 &=\mathcal E+\mathcal G-4\mathcal L_0\nonumber\\
 &=\operatorname{div}(f_D).
\label{eq:norm-divisor}\end{aligned}$$ The cyclic-algebra divisor criterion now shows that $$\mathcal A_D=(F_D'/F_D,f_D)
             =(\delta_D,Q_D/u_0^4)
\label{eq:quaternion}$$ has zero residue at every codimension-one point of $Y_{F_D}$, and hence extends to an unramified class in $\mathop{\mathrm{Br}}(Y_{F_D})$. This is the same general double-six mechanism that appears in the prior class construction [@ElsenhansJahnel2010Brauer]; the input specific to this surface is the exact divisor [\[eq:QD-divisor\]](#eq:QD-divisor){reference-type="ref" reference="eq:QD-divisor"}.

## Unramified does not yet mean nonzero

We identify the class of [\[eq:quaternion\]](#eq:quaternion){reference-type="ref" reference="eq:quaternion"} in $H^1(U_1,\Lambda)$. In the basis of [\[eq:picard-basis\]](#eq:picard-basis){reference-type="ref" reference="eq:picard-basis"}, put $$d_0=e_\Sigma-2h.
\label{eq:d0-def}$$ The first sixer has class $e_\Sigma$, while its opposite has class $12h-5e_\Sigma$. Since $[\mathcal L_0]=H_Y$, $$=e_\Sigma-2H_Y
       =3e_\Sigma-6h
       =3d_0.
\label{eq:D-class}$$

Write $U_1=U_1^+\times\langle\iota\rangle$, with $\iota$ the central involution exchanging the sixers. The exact Picard action gives $$\iota(h)=5h-2e_\Sigma,\qquad
 \iota(e_\Sigma)=12h-5e_\Sigma,\qquad
 \iota(d_0)=-d_0.
\label{eq:iota-action}$$ Moreover, $$\Lambda^{U_1^+}=\mathbf Zh\oplus\mathbf Ze_\Sigma.
\label{eq:S6-invariants}$$ For $x=ah+be_\Sigma$, direct substitution into [\[eq:iota-action\]](#eq:iota-action){reference-type="ref" reference="eq:iota-action"} yields $$(1+\iota)x=(6a+12b)h-(2a+4b)e_\Sigma,$$ and $$(\iota-1)x=4(a+3b)h-2(a+3b)e_\Sigma.$$ Consequently $$\ker(1+\iota\mid\Lambda^{S_6})=\mathbf Zd_0,\qquad
 (\iota-1)\Lambda^{S_6}=2\mathbf Zd_0.
\label{eq:coboundary-lattice}$$

With the norm-divisor convention in [\[eq:norm-divisor\]](#eq:norm-divisor){reference-type="ref" reference="eq:norm-divisor"}, the Hochschild--Serre cocycle of $\mathcal A_D$ is zero on $U_1^+=S_6$ and takes $\iota$ to $$[\mathcal D]=3d_0.$$ If this cocycle were a $U_1$-coboundary, its vanishing on $S_6$ would force a cobounding class into $\Lambda^{S_6}$. Its value at $\iota$ would then lie in $(\iota-1)\Lambda^{S_6}=2\mathbf Zd_0$, contrary to $$3d_0\notin2\mathbf Zd_0.$$ Thus the class is nonzero.

[\[thm:explicit-generator\]]{#thm:explicit-generator label="thm:explicit-generator"} The quaternion $$\mathcal A_D=(\delta_D,Q_D/u_0^4)$$ is unramified on $Y_{F_D}$ and represents the unique nonzero element of $$\mathop{\mathrm{Br}}(Y_{F_D})/\operatorname{im}\mathop{\mathrm{Br}}(F_D)\cong\mathbf Z/2.$$

Unramifiedness follows from [\[eq:norm-divisor\]](#eq:norm-divisor){reference-type="ref" reference="eq:norm-divisor"}. The calculation [\[eq:D-class,eq:coboundary-lattice\]](#eq:D-class,eq:coboundary-lattice){reference-type="ref" reference="eq:D-class,eq:coboundary-lattice"} proves that its Picard cocycle is nonzero. By [\[eq:exact-H1,eq:brauer-picard-bridge\]](#eq:exact-H1,eq:brauer-picard-bridge){reference-type="ref" reference="eq:exact-H1,eq:brauer-picard-bridge"}, this cocycle is the unique nonzero cohomology class and therefore the generator of the displayed Brauer quotient.

The proof separates three logically different assertions: the norm divisor proves unramifiedness, the integral lattice proves nontriviality, and neither computes a local evaluation. In particular, [\[thm:explicit-generator\]](#thm:explicit-generator){reference-type="ref" reference="thm:explicit-generator"} does not assert that $Y(F_D)$ is empty or nonempty, and it does not establish a Brauer--Manin obstruction, a Hasse-principle failure, or a failure of weak approximation.

# Exact replay, claim boundary, and limitations {#sec:replay-scope}

The proof combines finite exact arithmetic with arguments that are not reducible to certificate booleans. This section records the boundary at theorem-relevant granularity. Full artifact identities and evidence hashes are deferred to [14](#app:certificate){reference-type="ref" reference="app:certificate"}.

## Numbered gates and the separate scope firewall

summarizes the eight mathematical gates. The final row is deliberately not a ninth gate: it is a fail-closed negative-scope firewall.

::: {#tab:gates}
  row     exact payload                                                   inference used in the paper                                                                                 not inferred
  ------- --------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------- --------------------------------------------------
  G0      frozen surface and line-field import                            correct $Y,E,K$, full $W(E_6)$ premise                                                                      a new upstream line-field theorem
  G1      characteristic-zero incidence and all-and-only configurations   counts $135,72,36$ and exact double-six carrier                                                             the universal 2-primary subgroup classification
  G2      $U_1,U_1^+$, Picard action, integral cohomology                 selected subgroup facts and [\[eq:exact-H1\]](#eq:exact-H1){reference-type="ref" reference="eq:exact-H1"}   classification of every possible $H_L$
  G3      exact degree-$36$ resolvers                                     coefficients, irreducibility, orbit binding                                                                 novelty of a general resolver construction
  G4      orientation square and stabilizers                              $F_D'=F_D(\sqrt{\delta_D})$                                                                                 an expanded identity $\delta=P(\theta)$
  G5      exact $A_{12}B_{15}=g$                                          the twelve-line carrier over $F_D$                                                                          any unrelated line-field conclusion
  G6      gauge, pivot, all restrictions                                  rank $30$ and canonical $Q_D$                                                                               divisor equality before degree exhaustion
  G7      line distinctness, degree and norm inputs, Picard action        exact divisor, unramified nonzero generator with written bridges                                            local evaluation or a rational-point consequence
  SCOPE   negative flags and hostile mutations                            preservation of the stated claim boundary                                                                   a positive mathematical theorem

  : Exact gate contract. G6 ends at the determinant quartic and rank; G7 contains divisor exhaustion, the norm/quaternion step, and nonzero-class matching.
:::

The independent checker calls no producer theorem helper. It executes G0--G7, reconstructs $492$ payload and $28$ schema leaves, and rejects $535$ semantic/structural mutations plus nine malformed parser cases; the canonical suite has $33$ tests. Five deterministic gzip witnesses are checked after decompression, since compressed digests alone are not authority. A self-excluding manifest binds $18$ code files and $10$ non-manifest results, for $29$ live files including the manifest. The external-directory runner compares byte, size, mode, nanosecond-mtime, and inode snapshots. The sole official atomic refresh and mandatory nonmutating replay passed.

The exact arithmetic does not prove the complete $U_1/U_3$ source theorem, the fixed-field identity in [\[lem:intersection-fixed-field\]](#lem:intersection-fixed-field){reference-type="ref" reference="lem:intersection-fixed-field"}, the number-field Hochschild--Serre bridge, the Hilbert--90 upper rank bound, the degree-exhaustion argument, or the comparison of the quaternion cocycle with $3d_0$. Those steps remain written in [\[sec:minimal-degree,sec:brauer-jump,sec:canonical-quartic,sec:quaternion\]](#sec:minimal-degree,sec:brauer-jump,sec:canonical-quartic,sec:quaternion){reference-type="ref" reference="sec:minimal-degree,sec:brauer-jump,sec:canonical-quartic,sec:quaternion"}. Conversely, the cited general theorems do not verify a coefficient, carrier, minor, or restriction for [\[eq:cubic\]](#eq:cubic){reference-type="ref" reference="eq:cubic"}.

## Status and provenance boundary

The machine envelope has payload digest $$\texttt{72e498b544599dbb8c7c56b2fd999ed8be80bdb0abd19393b5e47ddf60ae4574}$$ and certificate digest $$\texttt{3078baf167d2344982d9f93811f1fd59a8258c8178ecce4decbd2b054b16092f}.$$ The independent machine-layer status is `PASS_PREFREEZE_CODE_RESULTS`. It supports the exact premises but is not reused as a paper or full-project identity. Those larger identities are recorded externally after their own inventories are closed, avoiding a self-referential digest.

## Data and code availability

The anonymous supplement contains this project under the stable relative directory

`henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/`.

The executable entrypoint is `code/run_all.sh`; the certificate, check report, schema, five deterministic evidence archives, and self-excluding machine manifest are in `results/`. The companion surface and line-field theorem packages are present under the sibling relative directories `henon_mu3_rational_yukawa_surface/` and `henon_mu3_yukawa_line_field/`. The scoped manifest identifies the machine lane. The full project and paper identities are supplied externally because embedding either digest in the object it hashes would create a cycle.

## Limitations and nonclaims

The theorem concerns only the global algebraic/cohomological quotient of [\[eq:cubic\]](#eq:cubic){reference-type="ref" reference="eq:cubic"}. It supplies neither a generic resolver or classification nor a theorem for arbitrary cubic, Yukawa, or Hénon surfaces; it certifies neither $\delta=P(\theta)$ nor an expanded quartic table. The fields $E,K,F_D,F_D'$ retain distinct roles, and no unrelated determinant field is identified with $F_D'/F_D$.

There is no claim about rational points, (stable) rationality, local evaluation, the Hasse principle, weak approximation, or a Brauer--Manin obstruction. Nor is there a complete bad-prime inertia or Picard--Artin package, conductor, Euler factor, root number, motive, variation of Hodge structure, automorphy, Calabi--Yau realization, dynamical theorem, Riemann-hypothesis statement, Hilbert--Pólya operator, or announcement of a later adaptive-sequence project.

# Conclusion {#sec:conclusion}

For the fixed cubic surface [\[eq:cubic\]](#eq:cubic){reference-type="ref" reference="eq:cubic"}, full $W(E_6)$ line arithmetic delays every nonzero 2-primary algebraic Brauer quotient until a degree divisible by $36$: $$36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q].$$ The equality fields are precisely the conjugate fixed fields of double-six stabilizers. Exact stabilizers identify $\mathbf Q(\theta_D)=\mathbf Q(\delta_D)=F_D$ and the oriented quadratic extension $F_D'=F_D(\sqrt{\delta_D})$. A Hilbert--90 rank sandwich and one exact pivot define the normalized quartic $Q_D$; degree exhaustion gives $\operatorname{div}(Q_D)=\mathcal E+\mathcal G$; and the class $[\mathcal D]=3d_0\notin2\mathbf Zd_0$ proves that $(\delta_D,Q_D/u_0^4)$ is the unique nonzero Brauer class over $F_D$.

The result moves from the certified full line-field action to the first possible cohomological jump for this one surface. It does not evaluate that class locally or decide rational points, rationality, or a Brauer--Manin obstruction. The exact code/results tuple is independently replayable from the anonymous supplement using the relative entrypoint described in [8](#sec:replay-scope){reference-type="ref" reference="sec:replay-scope"}; paper and full-project identities remain separate from the self-excluding machine manifest.

# Primary-source ledger and the number-field bridge {#app:sources}

The bibliography is deliberately restricted to the six entries audited before drafting. records the precise result imported from each source and, equally important, the instance facts that the source does not supply.

::: {#tab:source-ledger}
  source                             exact locator                                                                                                                                                               use here                                                                                                                                               not supplied
  ---------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  source                             exact locator                                                                                                                                                               use here                                                                                                                                               not supplied
  [@SwinnertonDyer1993]              p. 449; §2; Lemma 1, pp. 451--452; Lemma 2, p. 453; concluding classification, p. 458                                                                                       number-field Picard/Brauer description; invariant-double-six criterion; complete nonzero 2-primary possibilities $\mathbf Z/2$ and $(\mathbf Z/2)^2$   the frozen resolvers, fixed fields, orientation square, quartic, or quaternion representative
  [@ElsenhansJahnel2010Brauer]       introduction §1.3; Lemma 2.5; Remark 3.3 and Notation 3.4; Theorems 3.5 and 4.4; §4.3; Definition 4.1; Proposition 5.8; Theorem 5.11; Fact 6.2, Remark 6.3, Corollary 6.4   $U_1/U_3$ containment and restriction; orientation; invariant double-six class map; cyclic/quaternion precedent                                        the degree-$36$ field or determinant quartic for [\[eq:cubic\]](#eq:cubic){reference-type="ref" reference="eq:cubic"}; Corollary 6.4 is not used for a local evaluation
  [@ElsenhansJahnel2010DoubleSix]    Theorem 6.6; Algorithm 6.7; Propositions 7.1 and 7.4; Example 9.2                                                                                                           explicit invariant-double-six descent, tritangent-plane context, sixer-splitting radicand, and a full-$U_1$ $[12,15]$ example                          inversion of the present frozen full-$W(E_6)$ line field
  [@ElsenhansJahnel2012OrderThree]   Remark 4.34(iii), printed p. 22                                                                                                                                             prior-art boundary: a degree-$36$ resolver with roots corresponding to double-sixes                                                                    either resolver polynomial or the Brauer class in this paper
  [@FarbWolfson2019]                 Theorem 5.6 and Corollary 5.9                                                                                                                                               moduli-cover and resolvent-degree context for double-sixes and ordered sixers                                                                          an arithmetic fixed field for the present surface
  [@Viray2023]                       §2.1, p. 10, equation (24) and the following low-degree exact sequence                                                                                                      supporting Hochschild--Serre exposition                                                                                                                any instance computation or automatic Brauer--Manin conclusion

  : Primary-source locators and claim boundaries.
:::

## Why the subgroup theorem applies over $F_D$

The attaining base is the number field $F_D$, not $\mathbf Q$. Swinnerton-Dyer's Picard/Brauer theorem already works over algebraic number fields [@SwinnertonDyer1993]; the Elsenhans--Jahnel containment and restriction statements concern finite subgroups of $W(E_6)$, the Picard lattice, and line configurations [@ElsenhansJahnel2010Brauer]. Thus for any number field $k$ they apply to $$H=\mathop{\mathrm{im}}(G_k\to W(E_6))$$ without a $\mathbf Q$-specific step. For the representative, we construct $F_D'/F_D,\mathcal D,f_D$ in the present tower, prove $\operatorname{div}(f_D)=\mathop{\mathrm{Norm}}(\mathcal D)$, calculate its Picard cocycle, and only then use [\[eq:brauer-picard-bridge\]](#eq:brauer-picard-bridge){reference-type="ref" reference="eq:brauer-picard-bridge"}.

## Bounded novelty screen

The 2026-08-15 audit screened exact coefficients and title phrases, configuration/Brauer queries, and the sources' identifiers. It supports only:

> The bounded 2026-08-15 screen did not locate a prior exact computation of the degree-36 double-six field, its orientation square, and the determinant-defined quaternion generator for this frozen Yukawa surface.

This is not an absolute priority claim: the generic constructions remain prior art.

# Incidence, resolvers, and the twelve-line carrier {#app:incidence-resolvers}

## Characteristic-zero incidence formula

On the complete chart, a line has row matrix $$\begin{pmatrix}1&0&a&b\\0&1&c&d\end{pmatrix}$$ and points $(s,t,as+ct,bs+dt)$. The frozen lexicographic shape writes $$a(x)=-\frac{h_a(x)}{A_a},\qquad
 b(x)=-\frac{h_b(x)}{A_b},\qquad
 c(x)=-\frac{h_c(x)}{A_c},\qquad d(x)=x,$$ where the three denominators are nonzero constants. Here (x=d), the raw primitive eliminant is $\widetilde g(d)$, its leading coefficient is $c_g$, and the monic eliminant and integral orbit coordinate are $g=c_g^{-1}\widetilde g$ and $\alpha_i=c_gd_i$, respectively, as in [\[eq:monic-eliminant,eq:alpha-scaling\]](#eq:monic-eliminant,eq:alpha-scaling){reference-type="ref" reference="eq:monic-eliminant,eq:alpha-scaling"}. Two chart lines at $x\ne y$ meet precisely when $$(a(y)-a(x))(d(y)-d(x))
 -(b(y)-b(x))(c(y)-c(x))=0.
\label{eq:two-line-determinant}$$ For $\nu\in\{a,b,c\}$, put $$D_\nu(x,y)=\frac{h_\nu(y)-h_\nu(x)}{y-x}.$$ After dividing [\[eq:two-line-determinant\]](#eq:two-line-determinant){reference-type="ref" reference="eq:two-line-determinant"} by $(y-x)^2$ and clearing the constant denominators, the exact incidence carrier is $$J(x,y)=-D_aA_bA_c-D_bD_cA_a.
\label{eq:divided-J}$$ The polynomial $J$ remains defined on the diagonal. Its gcd has no diagonal root and satisfies [\[eq:incidence-identities\]](#eq:incidence-identities){reference-type="ref" reference="eq:incidence-identities"}. At each good specialization all $27$ copies of $H_x$ equal the monic modular gcd. Specialization gives the upper degree bound $10$, while the exact factor gives the lower bound.

The sixers are enumerated as six-element independent sets in the meeting graph. For a sixer $S$, its opposite is $$S^\vee=\{\ell\notin S:\ell\text{ meets exactly five lines in }S\}.$$ Every exact sixer has $|S^\vee|=6$, and pairing $S$ with $S^\vee$ produces the $36$ double-sixes in [\[eq:configuration-counts\]](#eq:configuration-counts){reference-type="ref" reference="eq:configuration-counts"}.

## Resolver reconstruction and irreducibility

Resolver arrays run from constant to leading term and are monic. Every CRT prime is proved prime; the eliminant remains squarefree, denominators are units, and the modular orbit product is multiplied back. Signed reconstruction requires a modulus exceeding twice the coefficient bound.

At a squarefree good reduction, the degree of any rational factor is a proper subset sum of the modular factor degrees. The two sets arising from [\[eq:resolver-factor-patterns\]](#eq:resolver-factor-patterns){reference-type="ref" reference="eq:resolver-factor-patterns"} are disjoint, proving irreducibility of both resolvers. Separately, the exact configuration action binds their roots all-and-only to the $36$ double-sixes.

::: {#tab:resolver-ledger}
  object                reconstruction witness                                                             independent identity
  --------------------- ---------------------------------------------------------------------------------- ----------------------------------------------------------------------
  incidence $H_x,Q_x$   characteristic-zero monic degrees $10,17$; good primes $7,37,10^{50}+12477$        $g=H_xQ_x$, $H_x\mid J$, no diagonal, all modular graphs agree
  $R_\theta$            $99$ primes; $4951$-digit CRT modulus                                              orbit product, exact factors, incompatible subset sums
  $R_\delta$            $198$ primes; $9901$-digit modulus exceeding the $9858$-digit height requirement   orbit product, exact factors, incompatible subset sums
  $A_{12}$              $1048$ primes; $100609$-digit modulus; $13\times36$ coefficient table              $28$ zero division remainders and $28$ matching forward coefficients

  : Compact reconstruction ledger. Large arrays are kept in exact electronic witnesses rather than printed as decimal tables.
:::

## Carrier identity over $\mathbf Q(\theta_D)$

Write $$A_{12}(d)=d^{12}+a_{11}d^{11}+\cdots+a_0,
 \qquad a_i\in\mathbf Q(\theta_D).$$ The subtop coefficient has the exact normalization $$A_{12}=-\sum_{i=1}^{12}d_i=-\theta_D/c_g.
\label{eq:appendix-carrier-subtop}$$ Exact long division by $A_{12}$ yields $B_{15}$ with zero remainder, and an independent convolution recomputes all $28$ product coefficients. The $[12,15]$ orbit partition binds the roots of $A_{12}$ to $D$, not merely to an arbitrary degree-$12$ factor.

The stable carrier-table digest is $$\texttt{72d4aef5120926ec09904b08219cba7cf2b49323bd085d05274e5c17e1ed90a1}.$$ This digest identifies the compact table but does not replace the division, forward-product, or orbit-binding checks.

# Integral cohomology and class matching {#app:cohomology}

## Cochain convention and Smith forms

For a finite group $\Gamma$ acting on $\Lambda$, a crossed homomorphism is a map $z:\Gamma\to\Lambda$ satisfying $$z(gh)=z(g)+g\,z(h).$$ After fixing the exact group generators, the values on those generators form an integral vector. Multiplication relations in the enumerated group give an integral relation matrix whose kernel is $Z^1(\Gamma,\Lambda)$. Principal cocycles are the image of $$\Lambda\longrightarrow Z^1(\Gamma,\Lambda),\qquad
 v\longmapsto(g\mapsto gv-v).$$ The checker rebuilds the group, both integer lattices, and the Smith normal form of their quotient; it does not accept a stored cohomology label.

For both $\Gamma=W(E_6)$ and $\Gamma=U_1$, the relation matrix has rank $36$ and the cocycle kernel has rank $6$. The quotient data are $$\begin{array}{c|c|c}
\Gamma & \text{Smith diagonal} & H^1(\Gamma,\Lambda)\\
\hline
W(E_6)& (1,1,1,1,1,1) & 0\\
U_1 & (1,1,1,1,1,2) & \mathbf Z/2.
\end{array}
\label{eq:smith-table}$$ All matrices use the marked basis $(h,e_1,\ldots,e_6)$. The result is unchanged under conjugating $U_1$, so every embedded double-six field has the same cohomological jump.

## The $S_6$-fixed plane and the central involution

The exact $S_6$-invariant basis is $$h=(1,0,0,0,0,0,0),\qquad
 e_\Sigma=(0,1,1,1,1,1,1).$$ In the ordered basis $(h,e_\Sigma)$, the central sixer swap acts by $$\iota(h)=5h-2e_\Sigma,\qquad
 \iota(e_\Sigma)=12h-5e_\Sigma.$$ For completeness, if $x=ah+be_\Sigma$, then $$(1+\iota)x
  =6(a+2b)h-2(a+2b)e_\Sigma
  =2(a+2b)H_Y,$$ where $d_0=e_\Sigma-2h$. Hence its kernel is obtained from $a+2b=0$: $$\ker(1+\iota\mid\Lambda^{S_6})=\mathbf Zd_0.$$ Similarly, $$(\iota-1)x
 =4(a+3b)h-2(a+3b)e_\Sigma
 =-2(a+3b)d_0,$$ and therefore $$(\iota-1)\Lambda^{S_6}=2\mathbf Zd_0.$$ These formulas are an independent two-dimensional check on the $\mathbf Z/2$ factor in [\[eq:smith-table\]](#eq:smith-table){reference-type="ref" reference="eq:smith-table"}.

## Cocycle carried by the quaternion

Let $\chi:U_1\to U_1/U_1^+\cong C_2$ be the orientation character. The norm-divisor equality [\[eq:norm-divisor\]](#eq:norm-divisor){reference-type="ref" reference="eq:norm-divisor"} defines a cyclic class whose Picard cocycle vanishes on $\ker\chi=U_1^+$ and, with the fixed divisor convention, has $$z(\iota)=[\mathcal D].$$ The marked line classes give $$[\mathcal E]=e_\Sigma,\qquad [\mathcal L_0]=3h-e_\Sigma,$$ so $$z(\iota)=[\mathcal D]
 =e_\Sigma-2(3h-e_\Sigma)
 =3(e_\Sigma-2h)=3d_0.$$ This is a cocycle because $(1+\iota)3d_0=0$. If it were principal, its zero restriction to $S_6$ would force the cobounding vector to lie in $\Lambda^{S_6}$, and its value at $\iota$ would lie in $2\mathbf Zd_0$. Since $3d_0\notin2\mathbf Zd_0$, the class is nonzero. The last line of [\[eq:smith-table\]](#eq:smith-table){reference-type="ref" reference="eq:smith-table"} then shows that it is the unique nonzero element.

This calculation is the class-map bridge used in [\[thm:explicit-generator\]](#thm:explicit-generator){reference-type="ref" reference="thm:explicit-generator"}. The norm-divisor identity is necessary for unramifiedness, but the parity of $3d_0$ against the coboundary lattice is what proves nontriviality.

# Determinant specification of $Q_D$ {#app:quartic-specification}

This appendix fixes every convention needed to recover the quartic without printing its expanded degree-$36$ coefficient table.

## Gauge and monomial order

List all exponent vectors $$(e_0,e_1,e_2,e_3),\qquad e_i\ge0,\qquad
 e_0+e_1+e_2+e_3=4,$$ in descending lexicographic order. Delete $$(4,0,0,0),\quad(3,1,0,0),\quad(3,0,1,0),\quad(3,0,0,1).$$ The validity and uniqueness of this deletion are proved by the gauge block [\[eq:gauge-block,eq:gauge-determinant\]](#eq:gauge-block,eq:gauge-determinant){reference-type="ref" reference="eq:gauge-block,eq:gauge-determinant"}. The remaining ordered monomials are $$\begin{aligned}
m_0&=u_0^2u_1^2,&
m_1&=u_0^2u_1u_2,&
m_2&=u_0^2u_1u_3,\\
m_3&=u_0^2u_2^2,&
m_4&=u_0^2u_2u_3,&
m_5&=u_0^2u_3^2,\\
m_6&=u_0u_1^3,&
m_7&=u_0u_1^2u_2,&
m_8&=u_0u_1^2u_3,\\
m_9&=u_0u_1u_2^2,&
m_{10}&=u_0u_1u_2u_3,&
m_{11}&=u_0u_1u_3^2,\\
m_{12}&=u_0u_2^3,&
m_{13}&=u_0u_2^2u_3,&
m_{14}&=u_0u_2u_3^2,\\
m_{15}&=u_0u_3^3,&
m_{16}&=u_1^4,&
m_{17}&=u_1^3u_2,\\
m_{18}&=u_1^3u_3,&
m_{19}&=u_1^2u_2^2,&
m_{20}&=u_1^2u_2u_3,\\
m_{21}&=u_1^2u_3^2,&
m_{22}&=u_1u_2^3,&
m_{23}&=u_1u_2^2u_3,\\
m_{24}&=u_1u_2u_3^2,&
m_{25}&=u_1u_3^3,&
m_{26}&=u_2^4,\\
m_{27}&=u_2^3u_3,&
m_{28}&=u_2^2u_3^2,&
m_{29}&=u_2u_3^3,\\
m_{30}&=u_3^4.&&&\end{aligned}$$ The normalization is $q_0=1$; equivalently, $[u_0^2u_1^2]Q_D=1$.

## The $60\times31$ matrix

For a carrier root $d$, write the corresponding line as $$(s,t,a(d)s+c(d)t,b(d)s+dt).$$ For every $m_j$, expand $$m_j(s,t,a(d)s+c(d)t,b(d)s+dt)
 =\sum_{\tau=0}^4r_{\tau j}(d)s^{4-\tau}t^\tau.
\label{eq:binary-restriction}$$ Reduce $r_{\tau j}(d)$ modulo the monic carrier $A_{12}(d)$: $$r_{\tau j}(d)\equiv
 \sum_{\rho=0}^{11}M_{12\tau+\rho,j}d^\rho
 \pmod{A_{12}(d)}.$$ This fixes the row convention $$\operatorname{row}=12(\text{binary degree})+(\text{carrier degree}),
\label{eq:row-convention}$$ with both degrees increasing. The matrix $$M_D=(M_{rj})_{\substack{0\le r<60\\0\le j<31}}$$ is therefore determined by the surface, chart shape, carrier, gauge, and orders above.

## Pivot and Cramer's rule

Let $$\mathcal R=\{0,1,\ldots,10,12,\ldots,20,24,\ldots,29,36,37,38,48\}.$$ Define $$N_D=(M_{rj})_{\substack{r\in\mathcal R\\1\le j\le30}},
 \qquad
 b_D=(M_{r0})_{r\in\mathcal R}.$$ The exact pivot certificate proves $\det N_D\ne0$. If $N_D^{(j)}(b_D)$ denotes $N_D$ with its $j$-th column replaced by $b_D$, then $$q_j=-\frac{\det N_D^{(j)}(b_D)}{\det N_D},
 \qquad 1\le j\le30.
\label{eq:cramer-Q}$$ , together with the monomial list, define $Q_D$ exactly.

The pivot determinant has nonzero norm $3$ modulo $7$. The exact orbit replay checks all $36$ conjugate determinant values and all $36\cdot60=2160$ restriction equations. Stable internal fingerprints are

  --------------------------------------------------------------------
  pivot determinant coefficient digest:
  `1af5bfdc9b2f945094835fd81281305fb84dfc8208cb542874f2803420cd3a9e`
  canonical solution digest:
  `eb9e803e16f5623647843dd7636fe3d511af60f8f31c453ea6826cd3e4d25573`
  --------------------------------------------------------------------

The fingerprints audit the exact arrays. They are not mathematical substitutes for gauge invertibility, the Hilbert--90 upper bound, pivot nonvanishing, or the complete restriction replay.

# Machine certificate and fail-closed contract {#app:certificate}

The identities below bind the exact machine input. Paper and full-project identities are external, non-self-referential records.

## Envelope and upstream locks

::: {#tab:envelope-hashes}
  object                     [sha]{.smallcaps}-256                                                bytes
  -------------------------- ------------------------------------------------------------------ -------
  certificate                3078baf167d2344982d9f93811f1fd59a8258c8178ecce4decbd2b054b16092f     27326
  independent check report   fb0afb77f130fb2d0a792af8d949e5c1a8e1b7864525dd62f1d1a41d99a79bcf      2176
  schema file                81942b5f8012071cbc1bd24f8a85e04a2e7fea10b3f5cb8e8ca3014c6e822f72      1040
  scoped manifest            864c05b18e0bdcafbc5b5e3206840a1b25afa355b9737ebcc9d1806e33fcec5d      4855

  : Authoritative live envelope. The manifest is self-excluding.
:::

The canonical payload digest is $$\texttt{72e498b544599dbb8c7c56b2fd999ed8be80bdb0abd19393b5e47ddf60ae4574},$$ the canonical schema digest is $$\texttt{4c4675b71556867a5699574b5f3f54aa40551c76a14e22ac21c62370add61cc4},$$ and the independent replay-summary digest is $$\texttt{17b383c762b20f45767c4daffc704cbfd2f6e9a54f97886de641d11018b3ac68}.$$ The envelope is `PREFREEZE_CODE_RESULTS_PASS`; this machine-layer status is intentionally distinct from the paper and full-project identities.

The upstream import uses the review-safe logical objects `I56`, `P56`, and `R56` from the companion anonymous-supplement package `henon_mu3_yukawa_line_field`. Their exact object names are rebound inside the machine certificate rather than printed as public-repository locators here. The import replays the upstream certificate $$\texttt{26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4}.$$ It also binds the upstream payload, check report, manifest, and Route, while preserving $E\ne K$.

## Semantic evidence artifacts

::: {#tab:evidence-hashes}
  artifact                            compressed [sha]{.smallcaps}-256 and bytes   decompressed [sha]{.smallcaps}-256 and bytes
  ----------------------------------- -------------------------------------------- ----------------------------------------------
  `a12_crt_transcript.json.gz`
  d3afd2970ccd91c431b5283587f7a22f
  bytes
  ccbddeed9c3ff6043cd34d16ec311fb2
  bytes
  `a12_table.json.gz`
  f51f3986be642643dfdf5f66711e3f6
  bytes
  c389934a62a38057b915955c117c3cc
  bytes
  `delta_crt.json.gz`
  330874a3b5156ceaeb1371fcb495f685
  bytes
  c2d9cdaebf9e87dd0d0e76da899999a9
  bytes
  `incidence_char0_witness.json.gz`
  f191bac960a989e8e85aede117cf8060
  bytes
  0b0b5a05da544b7455f960e47448a392
  bytes
  `theta_crt.json.gz`
  7a25913784ef8ad9d3be59c430a4fadd
  bytes
  d9b793dab8efa0864505903cf9e1bcb3
  bytes

  : The five large evidence inputs. Each has gzip mtime zero and must survive deterministic decompression and semantic replay.
:::

## Gate and executable separation

The independent check report binds the gate payloads:

  ---- ------------------------------------------------------------------
   G0  7b4b72505f6480ae085a5b8e27749c28c9fab87e26c883b1d74da33f5baa7fc8
   G1  a25b718a28f5260b7cbfa1c5ee954f10de7f8b586b0cd573ac33038b49d90d58
   G2  a462027bf02dac1f1d54a373130d11e262db76247821feffb7143accb88af3e9
   G3  323f89c767f44a705009a05b0eaecc2804a1201ff46ab52949eabb1582f9fea1
   G4  f07c2ed52daddb00428e016bc17c1e299df218553b58aca725f0254f171f328c
   G5  fce3d88a04abdf2b6c3e6ebd76a7776d4e14daaba048ffa74b76276d4f367e32
   G6  3f5d2802efb69942dd79e74e9b3c5aae47091b04223b90dda08183880637245b
   G7  ea63a74a6db2024f0cc937dc90675986f122659e2decf629ad2020dcdcb6d798
  ---- ------------------------------------------------------------------

The producer, independent checker, pipeline, atomic promoter, manifest builder, runner, and test-suite digests are respectively $$\begin{gathered}
\texttt{30b6aae77ceaa33fb2adf2d0ec69477afe2a8b11c789e4dce857873f46e52941},\\
\texttt{a44ad192b7840bba4b4a74899de0d369e79f3a8d41853a84c854ed34739e0064},\\
\texttt{00dfc9e376525c16bb0925f1fc7af2a0b7adef3945e4f3020fbba0fd900faf0e},\\
\texttt{c2057c74e4973576a3e67b6ef27a1da261ff7263480e91342c91da04d1a32558},\\
\texttt{822e291876ca6df1822fbb2a8930fd8fd842d7bf4e58a2c95307f7e0036a4a8b},\\
\texttt{8bcb6f206c991c827b8af63bedfd63b7991d9f376cfdb969ff2333e88fbfc6f4},\\
\texttt{e883b79c1e104054526155ccc5c459b430779a8a16779cec4d4ec082d91eb591}.
\end{gathered}$$ The manifest binds $18$ code files and $10$ non-manifest results; the live inventory adds the manifest.

## Fail-closed behavior

The suite mutates every classified scalar leaf while rebinding exposed hashes, and independently rejects semantic changes. It also tests malformed parsing, optimized execution, import-path injection, deterministic gzip, special links/files, stale output, lock replacement, and hostile shell startup. Failure injection into the fixed nine-file refresh must restore hash, size, mode, and nanosecond mtime. The nonmutating default runner compares byte/mode/mtime/inode snapshots from an external directory and retains uncertain stages fail-closed. These checks protect evidence identity; they do not prove the source classification, Hilbert--90 descent, divisor exhaustion, or cocycle comparison.
