---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-chiral-chronology-threshold"
canonical_tex: "henon_dynamics/henon_chiral_chronology_threshold/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_chiral_chronology_threshold/paper/main.pdf"
source_sha256: "5c87be8dccba9bbdc4cf99f978936276bfaacaec8c64d926ecc6a8ca4a4f5e30"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Point chronology without cohomological time in a period-six chiral Hénon cover

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_chiral_chronology_threshold>)
- [规范 TeX](<../../../../../henon_dynamics/henon_chiral_chronology_threshold/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_chiral_chronology_threshold/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_chiral_chronology_threshold/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_chiral_chronology_threshold/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Starting from the published Endler--Gallas factorization of the period-six chiral doublet in the area-preserving Hénon family, we study the smooth projective normalization $E_6$ of its twelve-state ordered-edge cover. An ordered state intrinsically recovers the source radical and all six orbit coordinates, so its function field is the full splitting field rather than an extension with an externally attached phase label. Over the radical line the associated cubic has discriminant $16\eta^4+88\eta^2+125$; its splitting cover has group $S_3$, four simple transposition branch values, and no ramification at infinity. Consequently $g(E_6)=1$, while over the original parameter line the deck group is $S_3\times C_2\simeq\mathsf D_6$ of order twelve. We determine the rotation fixed field $$\mathbb Q(E_6)^{\langle\tau\rangle}=\mathbb Q(A,v),\qquad
   v^2=(A-3)(16A^2-8A+5).$$ The degree-six quotient is unramified and has genus one. After choosing a geometric origin, Hénon time is translation by a point of exact order six and acts trivially on ordinary weight-one cohomology. Thus genuine point chronology need not produce a nontrivial time sector in $H^1$. Combined with published chiral class counts and one explicitly certified period-seven component, this yields a chronology--cohomology threshold only within the source-identified and repository-certified chiral ordered components considered for $n\leq7$. A separate quadratic marker coincidence descends from period one and does not itself furnish a dominant clock-faithful bridge. No cross-period determinant or Hilbert--Pólya operator is obtained.

  **Keywords:** reversible polynomial automorphisms; periodic orbit pairing; Galois splitting curves; equivariant weight-one cohomology; dynamical-zeta obstruction; arithmetic dynamics.
author:
- Anonymous research note
bibliography:
- references.bib
date: 8 August 2026
title: |
  Point chronology without cohomological time\
  in a period-six chiral Hénon cover
```

## Markdown 正文

chinese-traditional

中文摘要

本文從 [Endler--Gallas]{lang="en"} 已發表的保面積 [Hénon]{lang="en"} 映射六週期手性雙軌道分解出發，研究其十二狀態有序邊覆蓋的光滑射影正規化 $E_6$。 一個有序狀態能內稟地恢復源根式與全部六個軌道座標，因此其函數域是真正的分裂域，而非人為附加相位標籤的擴張。 在根式參數直線上，相應三次多項式的判別式為 $16\eta^4+88\eta^2+125$；其分裂覆蓋群為 $S_3$，有四個簡單換位分支值，且在無窮遠處不分歧，故 $g(E_6)=1$。 在原參數直線上，覆蓋群為十二階群 $S_3\times C_2\simeq\mathsf D_6$。 本文進一步確定時間旋轉子群的不動域 $$\mathbb Q(E_6)^{\langle\tau\rangle}=\mathbb Q(A,v),\qquad
 v^2=(A-3)(16A^2-8A+5).$$ 該六次商映射無分歧，且商曲線同為虧格一。 選定幾何原點後，[Hénon]{lang="en"} 時間是精確六階撓平移，並在普通權一上同調上恆等作用。 這說明真實的點態時間順序不必產生非平凡的 $H^1$ 時間角色。 結合既有手性軌道計數與一個明確認證的七週期分量，本文只在 $n\leq7$ 的來源可辨識、且經本項目精確驗證的手性有序分量中得到時間與上同調之間的閾值。 另一個六、七週期二次標記場的巧合則源自一週期影子，本身不給出支配且保持忠實時鐘的橋接。 本文不構造跨週期行列式或 [Hilbert--Pólya]{lang="en"} 算子。

關鍵詞：可逆多項式自同構；週期軌道配對；[Galois]{lang="en"} 分裂曲線；等變權一上同調；動力學 $\zeta$ 阻礙；算術動力系統。

# Introduction

An ordered periodic orbit contains more information than its coordinate polynomial. The order records which point follows which, while a symmetric orbit marker retains only a quotient of that information. For a possible dynamical-zeta or Hilbert--Pólya route, however, preserving order on points is only the first test. The chronological generator must also survive in a cohomological or operator spectrum, and compatible objects at distinct primitive periods must satisfy a repetition law. These are different requirements: $$\label{eq:three-layers}
 \text{ordered point chronology}
 \longrightarrow \text{equivariant cohomology}
 \longrightarrow \text{cross-period determinant}.$$ This paper gives an exact example in which the first arrow loses every nontrivial time character in ordinary weight-one cohomology even though no chronological averaging has been performed.

The dynamical family is the quadratic area-preserving Hénon recurrence. Quadratic area-preserving maps already appear in Hénon's original study [@henon1969]. The particular normalization used here comes from Section 2.1, equation (1) of the foundational repository manuscript called Paper 5 [@wang2026henon Sec. 2.1, Eq. (1)]: $$\label{eq:paper5-recurrence}
 q_{j+1}=1-Aq_j^2-q_{j-1}.$$ For $A\ne0$, the scaling $x_j=Aq_j$ gives $$\label{eq:ham-recurrence}
 x_{j+1}=A-x_j^2-x_{j-1},
 \qquad
 H_A(x,y)=(A-x^2-y,x).$$ The orbit-polynomial method begins with the period-four construction of Endler and Gallas [@endlergallas2002 Sec. II, Eqs. (1)--(6)]; their period-six work gives a general carrier, orbit sum, and stability formula [@endlergallas2004 Eqs. (1)--(3) and Appendix]. The Hamiltonian reduction in the convention of [\[eq:ham-recurrence\]](#eq:ham-recurrence){reference-type="eqref" reference="eq:ham-recurrence"} is developed in [@endlergallas2006sums Eq. (1) and Sec. 2].

The scalar starting point is not new. Endler and Gallas published the period-six chiral marker, its conjugate-cubic coordinate factorization, and the need to choose the proper in-phase combinations of roots in Section 3 and equations (11)--(15) of [@endlergallas2006chiral]. Gallas subsequently gave Möbius formulas for the diagonal, non-diagonal, and chiral orbit classes; his equations (2)--(7) and Table 1 place the first chiral doublet at period six [@gallas2007]. The question addressed here lies above those scalar formulas:

> Does the parameter-varying ordered cover of the period-six chiral doublet carry a nontrivial weight-one representation of genuine Hénon time, and can its low-degree arithmetic connect faithfully to a different primitive period?

The answer has two negative parts. First, the twelve ordered phases form a geometrically connected genus-one curve $E_6$ with deck group $S_3\times C_2\simeq\mathsf D_6$, where $\mathsf D_6$ has order twelve. Hénon time has exact order six on generic ordered states. Nevertheless, the time quotient also has genus one, the quotient is unramified, and time is a torsion translation. It therefore acts as the identity on all of $H^1(E_6)$. Chronology survives on points but disappears from the nontrivial weight-one time sectors.

Second, a tempting quadratic field shared by one period-six reversible marker and one period-seven chiral marker is already the function field of a period-one fixed-point marker. The fiber product splits into two elementary graphs. Thus the common field does not itself provide a primitive chronology-preserving correspondence. A general divisibility lemma also rules out dominant single-valued maps that intertwine distinct faithful clocks among periods five, six, and seven. It does not rule out multivalued correspondences.

The main contributions are as follows.

1.  We construct the twelve-state ordered-edge object directly from the published cubic factors. A valid orbit recovers the source radical by an alternating sum, so the ordered cover is intrinsically the full splitting curve rather than a scalar curve with a sign label attached.

2.  We prove geometric irreducibility, identify the order-twelve dihedral deck group, compute all finite branch values over the radical line, prove that infinity is unramified there, and obtain $g(E_6)=1$.

3.  We determine the exact rotation fixed field and prove $$\tau^*|_{H^1(E_6)}=1,
      \qquad
      H^1(E_6,\mathbb Q)\simeq\varepsilon_{\mathrm{refl}}^{\oplus2}.$$

4.  Combining the period-six theorem with published class counts and the explicitly defined HCS-C20 period-seven component gives a narrowly scoped first witnessed nontrivial weight-one time sector at $n=7$. This is not a classification of the saturated period-seven scheme.

5.  We prove the period-one marker-shadow identity and the restricted clock-divisibility obstruction, then evaluate the result under Route A.

The novelty claim is deliberately bounded. A targeted search completed on 8 August 2026 did not locate a prior computation of the normalization, genus, or chronological $H^1$-representation of this specific twelve-state cover. The search was not an exhaustive MathSciNet, zbMATH, Web of Science, or Scopus audit, so no absolute priority claim is made. The new period-six, marker-shadow, and divisibility proofs below are self-contained; the scoped threshold explicitly imports the cited class-count and period-seven theorems. The released symbolic certificate and independent checker serve reproducibility, not logical substitution for any proof.

Section [2](#sec:source){reference-type="ref" reference="sec:source"} fixes the source and object boundaries. Sections [3](#sec:ordered){reference-type="ref" reference="sec:ordered"}--[5](#sec:collapse){reference-type="ref" reference="sec:collapse"} prove the ordered-cover, genus, and cohomological-collapse theorems. Section [6](#sec:threshold){reference-type="ref" reference="sec:threshold"} states the scoped comparison and the marker obstruction. Section [7](#sec:route-a){reference-type="ref" reference="sec:route-a"} records the Hilbert--Pólya boundary.

# Source model and object scope {#sec:source}

## The generic exact-period locus

Put $$K=\mathbb Q(A),\qquad K_\eta=K(\eta),\qquad \eta^2=A-3,$$ and define $$\label{eq:feta}
 f_\eta(X)
 =X^3-(1+\eta)X^2-AX+A(1+\eta)-1.$$ Let $L$ be its splitting field over $K_\eta$. In a fixed common algebraic closure, put $L_{\overline{\mathbb Q}}=L\cdot\overline{\mathbb Q}$, the base-changed splitting field over $\overline{\mathbb Q}(\eta)$. We shall prove that its geometric Galois group is $S_3$ and that $L$ is stable under the sheet involution. The curve $E_6$ is the smooth projective normalization over $\mathbb Q$ with function field $L$, viewed over the $A$-line after adjoining that involution.

The ordered-state interpretation is generic. Let $U\subset\mathbb A^1_A$ be the nonempty open set obtained by removing the discriminant values, $A=3$, and the finite locus at which a source chiral state collides or has smaller minimal period. Over $U$, the source carrier is separable and the twelve directed phases below have exact minimal period six. Statements about $E_6$ at a deleted parameter refer to the smooth projective function-field normalization, not to a finite *exact-period* fiber. Friedland--Milnor's total fixed-point multiplicity theorem for polynomial automorphisms [@friedlandmilnor1989 Thm. 3.1 and Lem. 3.2] and Hutz's formal-period framework for projective morphisms [@hutz2010 Def. 1.1, Thm. 3.1, and Prop. 4.1(2)] underscore that total multiplicity, distinct points, formal period, and minimal period are not interchangeable. No theorem of Hutz is applied to the affine Hénon map.

## The published scalar carrier

Endler and Gallas write the period-six orbit-sum factorization as $$S_6(\sigma)=
 \bigl(C_6^{\mathrm{mark}}(\sigma)\bigr)^2
 D_6^{\mathrm{mark}}(\sigma)N_6^{\mathrm{mark}}(\sigma),$$ with $$C_6^{\mathrm{mark}}(\sigma)=\sigma-2,
 \qquad
 D_6^{\mathrm{mark}}(\sigma)=\sigma^2+4\sigma-4A.$$ At the chiral value $\sigma=2$, their equation (15) is $$\label{eq:published-p6}
 P_6(A,X)=f_\eta(X)f_{-\eta}(X),
 \qquad \eta^2=A-3.$$ These formulas and the identification of the chiral doublet are prior work [@endlergallas2006chiral Sec. 3, Eqs. (11)--(15)]. Expanding the published factorization gives the directly recomputed consequence $$\begin{aligned}
\label{eq:p6-expanded}
P_6={}&X^6-2X^5+(4-3A)X^4+(4A-2)X^3\notag\\
&+(3A^2-8A+2)X^2+(-2A^2+2A)X\notag\\
&-A^3+4A^2-2A+1,\end{aligned}$$ whose discriminant is $$\label{eq:p6-disc}
 \mathop{\mathrm{Disc}}_X(P_6)=64(A-3)^3(16A^2-8A+5)^2.$$ The factorization is prior work. Equations [\[eq:p6-expanded\]](#eq:p6-expanded){reference-type="eqref" reference="eq:p6-expanded"} and [\[eq:p6-disc\]](#eq:p6-disc){reference-type="eqref" reference="eq:p6-disc"} are direct symbolic consequences recomputed here and are not claimed as independent theorem-level novelty.

## Four distinct objects

Table [1](#tab:object-boundaries){reference-type="ref" reference="tab:object-boundaries"} prevents four common conflations.

::: {#tab:object-boundaries}
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Object                           Information retained
  -------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  $C_6^{\mathrm{mark}}=\sigma-2$   Coarse orbit-sum marker of the period-six chiral doublet.

  $P_6=f_\eta f_{-\eta}$           Six-coordinate scalar carrier, without an intrinsic successor relation.

  $E_6$                            Smooth projective normalization of the twelve directed phases of the unique generic chiral doublet.

  $D_6^{\mathrm{mark}}$            A separate reversible or self-conjugate period-six marker used only in the cross-period shadow of Section [6](#sec:threshold){reference-type="ref" reference="sec:threshold"}.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Distinct period-six objects and the information each retains.
:::

The symbol $\mathsf D_6$ will denote the dihedral group of order twelve, not the polynomial $D_6^{\mathrm{mark}}$. Earlier repository work proved genus zero for smooth normalizations of the coarse marker components $C_6^{\mathrm{mark}},D_6^{\mathrm{mark}},N_6^{\mathrm{mark}}$ [@hcsc12c Sec. 4]. That result does not determine the genus of $E_6$.

## Clock convention

The code and formulas below store a forward edge $(x_i,x_{i+1})$. Its forward shift is $$\label{eq:edge-shift}
 (x_i,x_{i+1})\longmapsto(x_{i+1},x_{i+2})
 =H_A^{-1}(x_i,x_{i+1}).$$ HCS-C19 and HCS-C20 instead store $(x_i,x_{i-1})$, for which the forward map is $H_A$ [@hcsc19 Sec. 3, Cor. 3][@hcsc20 Sec. 1]. Reversal conjugates the two conventions and replaces $\tau$ by $\tau^{-1}$; quotient genera and time-isotypic dimensions are unchanged. The coordinate formulas are not identified.

Four symbols remain separate throughout: primitive Hénon period $n$, chronological phase $s$, Frobenius extension degree $r_F$, and the source radical $\eta$. No transition matrices are averaged over $s$.

# The intrinsic period-six ordered cover {#sec:ordered}

Set $$\label{eq:matching-map}
 m_\eta(X)=X^2+1-A-\eta.$$ The first step is to turn the source instruction to select proper in-phase roots into an algebraic map.

[\[lem:matching\]]{#lem:matching label="lem:matching"} After $A=\eta^2+3$, the following identities hold in $\mathbb Q[\eta,X]$: $$\begin{aligned}
 f_{-\eta}(m_\eta(X))&=-f_\eta(X)f_\eta(-X),
 \label{eq:matching-identity}\\
 m_{-\eta}(m_\eta(X))-X&=(X+\eta+1)f_\eta(X).
 \label{eq:inverse-identity}\end{aligned}$$ Consequently, on the separable locus, $m_\eta$ is a bijection from the roots of $f_\eta$ to the roots of $f_{-\eta}$, with inverse $m_{-\eta}$.

Substitution and collection of powers of $X$ give [\[eq:matching-identity\]](#eq:matching-identity){reference-type="eqref" reference="eq:matching-identity"} and [\[eq:inverse-identity\]](#eq:inverse-identity){reference-type="eqref" reference="eq:inverse-identity"}. If $f_\eta(\alpha)=0$, the first identity gives $f_{-\eta}(m_\eta(\alpha))=0$; the second sends it back to $\alpha$. Thus the induced map between the two three-element root sets is bijective.

Let $\alpha,\beta,\gamma$ be the roots of $f_\eta$, with $\alpha\ne\beta$. Vieta's formulas give $$\label{eq:vieta}
 \alpha+\beta+\gamma=1+\eta,\qquad
 \alpha\beta+\alpha\gamma+\beta\gamma=-A,\qquad
 \alpha\beta\gamma=1-A(1+\eta).$$

[\[prop:twelve-states\]]{#prop:twelve-states label="prop:twelve-states"} For an ordered pair $(\alpha,\beta)$ of distinct roots, the cyclic sequence $$\label{eq:orbit-sequence}
 \mathcal O(\alpha,\beta)=
 \bigl(\alpha,m_\eta(\beta),\gamma,m_\eta(\alpha),
       \beta,m_\eta(\gamma)\bigr)$$ satisfies $x_{i+1}=A-x_i^2-x_{i-1}$ for every $i\pmod6$. For each of the two signs of $\eta$ there are $3\cdot2=6$ distinct generic choices. These twelve states exhaust the directed phases of the source chiral doublet over $U$.

Insert [\[eq:matching-map\]](#eq:matching-map){reference-type="eqref" reference="eq:matching-map"} into the recurrence and reduce using [\[eq:vieta\]](#eq:vieta){reference-type="eqref" reference="eq:vieta"}; all six differences $x_{i+1}+x_{i-1}+x_i^2-A$ vanish. A representative calculation is $$m_\eta(\beta)+m_\eta(\alpha)+\gamma^2-A=0,$$ which follows after replacing $\alpha+\beta$ by $1+\eta-\gamma$ and using $f_\eta(\gamma)=0$. The remaining five identities are its cyclic and sheet-conjugate reductions; their exact remainder ledger is recorded in Appendix [10](#app:ledgers){reference-type="ref" reference="app:ledgers"} and recomputed independently by the released checker.

Separability makes the six ordered choices distinct on each sheet, while $$\label{eq:sheet-resultant}
 \operatorname{Res}_X(f_\eta,f_{-\eta})=8\eta^3$$ shows that the two coordinate carriers are disjoint over $U$. Hence all twelve constructed states are distinct. Endler--Gallas identify one generic period-six chiral doublet, namely two reversal-related six-cycles [@endlergallas2006chiral p. 3, discussion following Eq. (15)]; choosing a starting point on each cycle gives twelve directed phases, consistently with the class count [@gallas2007 Eqs. (2)--(7) and Table 1]. The parameter-varying normalization of those phases is the object defined here. Thus the twelve valid states exhaust that source component. Equivalently, their bipartite neighbor graph is $K_{3,3}$ with the matching $\alpha\leftrightarrow m_\eta(\alpha)$ removed.

The central point is that the radical is recovered from the dynamics rather than attached to it.

[\[prop:recovery\]]{#prop:recovery label="prop:recovery"} For the orbit [\[eq:orbit-sequence\]](#eq:orbit-sequence){reference-type="eqref" reference="eq:orbit-sequence"}, $$\label{eq:even-odd-sums}
 x_0+x_2+x_4=1+\eta,
 \qquad
 x_1+x_3+x_5=1-\eta.$$ Hence $$\label{eq:eta-recovery}
 \boxed{
 \eta=\frac{x_0-x_1+x_2-x_3+x_4-x_5}{2}.}$$ One valid ordered edge determines the complete orbit, the radical, and all three roots of $f_\eta$. Its function field is $L$.

The first equality in [\[eq:even-odd-sums\]](#eq:even-odd-sums){reference-type="eqref" reference="eq:even-odd-sums"} is Vieta's first relation. For the second, sum $m_\eta(\alpha_i)$ over the three roots and use $\sum\alpha_i^2=(1+\eta)^2+2A$ together with $A=\eta^2+3$. Subtraction gives [\[eq:eta-recovery\]](#eq:eta-recovery){reference-type="eqref" reference="eq:eta-recovery"}. Starting from an edge, recurrence [\[eq:ham-recurrence\]](#eq:ham-recurrence){reference-type="eqref" reference="eq:ham-recurrence"} gives all six coordinates. Their alternating sum gives $\eta$, while the even positions give the complete root set of $f_\eta$. Thus the edge field contains $L$; the reverse inclusion follows from the explicit construction [\[eq:orbit-sequence\]](#eq:orbit-sequence){reference-type="eqref" reference="eq:orbit-sequence"}.

[\[lem:absolute-irreducible\]]{#lem:absolute-irreducible label="lem:absolute-irreducible"} The cubic $f_\eta(X)$ is irreducible in $\overline{\mathbb Q}(\eta)[X]$.

After substituting $A=\eta^2+3$, regard $f_\eta$ as $$\label{eq:F-plane}
 F(\eta,X)=
 \eta^3-\eta^2X+\eta^2-\eta X^2+3\eta
 +X^3-X^2-3X+2.$$ If this monic cubic were reducible over $\overline{\mathbb Q}(\eta)$, it would have a root integral over the integrally closed ring $\overline{\mathbb Q}[\eta]$, hence a polynomial root $q(\eta)$. If $\deg q>1$, the term $q^3$ has strictly larger $\eta$-degree than every other term. Thus $q=c\eta+d$.

The coefficients of $F(\eta,c\eta+d)$, from degree three to degree zero, are $$\begin{aligned}
 &(c-1)^2(c+1),\\
 &3c^2d-c^2-2cd-d+1,\\
 &3cd^2-2cd-3c-d^2+3,\\
 &d^3-d^2-3d+2.\end{aligned}$$ The leading coefficient forces $c=1$ or $c=-1$. For $c=1$, the $\eta$-coefficient is $2d(d-1)$; $d=0,1$ give constants $2,-1$. For $c=-1$, the $\eta^2$-coefficient gives $d=0$, after which the $\eta$-coefficient is $6$. Every case is impossible.

# Dihedral geometry and genus {#sec:geometry}

The cubic discriminant is $$\label{eq:delta-eta}
 \Delta(\eta)=\mathop{\mathrm{Disc}}_X(f_\eta)
 =16\eta^4+88\eta^2+125.$$ It is squarefree: its derivative is $8\eta(8\eta^2+22)$, and direct substitution shows no common zero. It is therefore nonsquare in $\overline{\mathbb Q}(\eta)$. Lemma [\[lem:absolute-irreducible\]](#lem:absolute-irreducible){reference-type="ref" reference="lem:absolute-irreducible"} and the cubic Galois criterion give $$\label{eq:s3-geometric}
 \mathop{\mathrm{Gal}}(L_{\overline{\mathbb Q}}/\overline{\mathbb Q}(\eta))\simeq S_3.$$ Thus $[L_{\overline{\mathbb Q}}:\overline{\mathbb Q}(\eta)]=6$. Base extension cannot increase degree, whereas the splitting field of a cubic over $\mathbb Q(\eta)$ has degree at most six. Therefore $[L:\mathbb Q(\eta)]=6$ as well, equality is preserved after base change, and the constant field of $L$ is $\mathbb Q$. Since $L$ is a cubic splitting field of degree six, this also gives $$\label{eq:s3-arithmetic}
 \mathop{\mathrm{Gal}}(L/\mathbb Q(\eta))\simeq S_3.$$

## The twelve-state action

Represent a directed state by $(\epsilon,(a,b,c))$, where $\epsilon\in\{+1,-1\}$ records the sign of $\eta$ and $(a,b,c)$ is an ordering of the three roots on that sheet. The chronological shift and reversal act by $$\label{eq:label-actions}
 \tau(\epsilon,(a,b,c))=(-\epsilon,(b,c,a)),
 \qquad
 \rho(\epsilon,(a,b,c))=(-\epsilon,(b,a,c)).$$

[\[thm:dihedral\]]{#thm:dihedral label="thm:dihedral"} The sheet involution $\iota$ defined by $$\iota(\eta)=-\eta,\qquad
 \iota(\alpha_i)=m_\eta(\alpha_i)$$ is a well-defined central involution of $L/\mathbb Q(A)$. Moreover, $$\label{eq:d6-group}
 \mathop{\mathrm{Gal}}(L/\mathbb Q(A))\simeq S_3\times C_2\simeq\mathsf D_6,
 \qquad |\mathsf D_6|=12.$$ The elements [\[eq:label-actions\]](#eq:label-actions){reference-type="eqref" reference="eq:label-actions"} satisfy $$\label{eq:d6-relations}
 \tau^6=\rho^2=1,
 \qquad
 \rho\tau\rho=\tau^{-1},$$ and act freely and transitively on the twelve generic states.

Choose an ordering $\alpha_1,\alpha_2,\alpha_3$ of the roots. The assignment $$\eta\longmapsto-\eta,
 \qquad
 \alpha_i\longmapsto m_\eta(\alpha_i)$$ respects the elementary symmetric relations for $f_{-\eta}$ by Lemma [\[lem:matching\]](#lem:matching){reference-type="ref" reference="lem:matching"}. The universal property of a splitting field therefore extends it to a $\mathbb Q(A)$-embedding $L\hookrightarrow L$. Equation [\[eq:inverse-identity\]](#eq:inverse-identity){reference-type="eqref" reference="eq:inverse-identity"} supplies the inverse assignment, so the embedding is an involutive automorphism $\iota$. Since the matching map is applied coordinatewise, $\iota$ commutes with every permutation of the three roots. Consequently the extension over $\mathbb Q(A)$ contains the direct product $S_3\times\langle\iota\rangle$. Proposition [\[prop:recovery\]](#prop:recovery){reference-type="ref" reference="prop:recovery"} shows that the ordered-edge field contains $\eta$ and the full splitting field, so its generic degree over $\mathbb Q(A)$ is $2\cdot6=12$; there is no larger group.

If $c$ denotes a root three-cycle and $s$ a transposition, then $\tau=\iota c$ and $\rho=\iota s$. Hence $\tau^2=c^2$ generates $A_3$, $\tau^3=\iota$, and $s c s=c^{-1}$ gives [\[eq:d6-relations\]](#eq:d6-relations){reference-type="eqref" reference="eq:d6-relations"}. Formula [\[eq:label-actions\]](#eq:label-actions){reference-type="eqref" reference="eq:label-actions"} has one orbit of size twelve, proving freeness and transitivity. This also identifies the chronological action with the ordered-edge shift in [\[eq:edge-shift\]](#eq:edge-shift){reference-type="eqref" reference="eq:edge-shift"}.

## Branching over the radical line

We compute genus through the certified degree-six $S_3$ cover $$\label{eq:eta-cover}
 E_6\longrightarrow\mathbb P^1_\eta.$$ The four roots of [\[eq:delta-eta\]](#eq:delta-eta){reference-type="eqref" reference="eq:delta-eta"} are distinct. Because the cubic is monic, its splitting algebra is finite étale at every finite place where the discriminant is a unit; hence there is no other finite branch value. At each root of the discriminant the cubic has one double and one simple root, so the inertia is a transposition. In the regular degree-six cover, each branch value contributes $6(1-1/2)=3$ to Riemann--Hurwitz. It remains to exclude hidden inertia at infinity.

[\[lem:infinity\]]{#lem:infinity label="lem:infinity"} The cover [\[eq:eta-cover\]](#eq:eta-cover){reference-type="eqref" reference="eq:eta-cover"} is unramified at $\eta=\infty$.

Put $t=1/\eta$ and $X=u/t$. Equation [\[eq:F-plane\]](#eq:F-plane){reference-type="eqref" reference="eq:F-plane"} becomes $$\label{eq:infinity-chart}
 t^3F(1/t,u/t)
 =(u-1)^2(u+1)+t(1-u^2)+3t^2(1-u)+2t^3.$$ The slope $u=-1$ is simple modulo $t$ and lifts to a branch over $\overline{\mathbb Q}[[t]]$. At the double slope put $u=1+ct$ and divide the transformed equation by $t^2$. Its reduction at $t=0$ is $$2c(c-1).$$ The two roots $c=0,1$ are simple, so both lift over $\overline{\mathbb Q}[[t]]$ as well. All three $X$-roots lie in $t^{-1}\overline{\mathbb Q}[[t]]$ as distinct Laurent series. The splitting field therefore has trivial inertia at infinity.

[\[thm:genus\]]{#thm:genus label="thm:genus"} The smooth projective ordered-edge curve has genus $$\label{eq:genus-one}
 \boxed{g(E_6)=1.}$$

The four finite transposition values contribute twelve in total, while Lemma [\[lem:infinity\]](#lem:infinity){reference-type="ref" reference="lem:infinity"} contributes nothing at infinity. Riemann--Hurwitz for [\[eq:eta-cover\]](#eq:eta-cover){reference-type="eqref" reference="eq:eta-cover"} gives $$2g(E_6)-2=6(-2)+4\cdot3=0.$$

The branch theorem just proved is over $\mathbb P^1_\eta$, which is sufficient for the genus computation. We do not promote the scalar discriminant [\[eq:p6-disc\]](#eq:p6-disc){reference-type="eqref" reference="eq:p6-disc"} to a separately certified complete branch signature for the degree-twelve cover over $\mathbb P^1_A$.

# The rotation quotient and cohomological collapse {#sec:collapse}

Let $\alpha,\beta,\gamma$ be the three roots of $f_\eta$ and put $$\label{eq:vandermonde}
 w=(\alpha-\beta)(\alpha-\gamma)(\beta-\gamma),
 \qquad
 w^2=\Delta(\eta).$$ The $A_3$-fixed field in the cubic splitting field is $\mathbb Q(\eta,w)$. The sheet involution does not fix $w$.

[\[lem:vandermonde-sign\]]{#lem:vandermonde-sign label="lem:vandermonde-sign"} The central sheet involution acts by $$\label{eq:iota-vandermonde}
 \iota:(\eta,w)\longmapsto(-\eta,-w).$$

The matching map sends a difference of two roots to $$m_\eta(\alpha_i)-m_\eta(\alpha_j)
 =(\alpha_i-\alpha_j)(\alpha_i+\alpha_j).$$ It therefore multiplies the Vandermonde by $$\prod_{i<j}(\alpha_i+\alpha_j)=e_1e_2-e_3.$$ For [\[eq:feta\]](#eq:feta){reference-type="eqref" reference="eq:feta"}, Vieta gives $e_1=1+\eta$, $e_2=-A$, and $e_3=1-A(1+\eta)$, so $e_1e_2-e_3=-1$. The involution also sends $\eta$ to $-\eta$, proving [\[eq:iota-vandermonde\]](#eq:iota-vandermonde){reference-type="eqref" reference="eq:iota-vandermonde"}.

Recall from the proof of Theorem [\[thm:dihedral\]](#thm:dihedral){reference-type="ref" reference="thm:dihedral"} that, if $c$ is a root three-cycle, $$\label{eq:tau-subgroup}
 \tau=\iota c,\qquad
 \tau^2\text{ generates }A_3,\qquad
 \tau^3=\iota.$$ Hence $\langle\tau\rangle=A_3\times\langle\iota\rangle$ inside $S_3\times C_2$.

[\[prop:fixed-field\]]{#prop:fixed-field label="prop:fixed-field"} Let $v=\eta w$. Then $$\label{eq:fixed-field}
 \boxed{
 L^{\langle\tau\rangle}=\mathbb Q(A,v),
 \qquad
 v^2=(A-3)(16A^2-8A+5).}$$

Equation [\[eq:iota-vandermonde\]](#eq:iota-vandermonde){reference-type="eqref" reference="eq:iota-vandermonde"} makes $v=\eta w$ invariant under $\iota$, and $w$ is invariant under $A_3$. Thus $\mathbb Q(A,v)\subseteq L^{\langle\tau\rangle}$. Moreover, $$v^2=\eta^2\Delta(\eta)
 =(A-3)(16A^2-8A+5).$$ The right-hand side has valuation one at $A=3$ (the quadratic factor equals $125$ there), so it is not a square in $\mathbb Q(A)$ and the displayed field has degree two over $\mathbb Q(A)$. The subgroup $\langle\tau\rangle$ has order six and index two in $\mathsf D_6$. Its fixed field also has degree two. Inclusion plus equality of degrees proves [\[eq:fixed-field\]](#eq:fixed-field){reference-type="eqref" reference="eq:fixed-field"}.

Let $B_6$ be the smooth projective curve with function field $\mathbb Q(A,v)$.

[\[lem:quotient-genus\]]{#lem:quotient-genus label="lem:quotient-genus"} The curve $B_6$ has genus one, and the quotient map $$\label{eq:cyclic-quotient}
 E_6\longrightarrow B_6=E_6/\langle\tau\rangle$$ is an unramified cyclic cover of degree six.

The cubic $$(A-3)(16A^2-8A+5)$$ has discriminant $-4{,}000{,}000$ and is therefore squarefree. The smooth projective model of its hyperelliptic equation has genus one. Applying Riemann--Hurwitz to the degree-six quotient and using $g(E_6)=g(B_6)=1$ gives $$0=6\cdot0+R.$$ The total ramification $R$ is zero.

The two degree-six quotients retain different information; their relation is summarized in Figure [\[fig:quotient-diamond\]](#fig:quotient-diamond){reference-type="ref" reference="fig:quotient-diamond"}.

$$\begin{array}{ccccc}
 && E_6\ (g=1) && \\[2pt]
 & {}^{6,\,S_3}\swarrow && \searrow^{6,\,\langle\tau\rangle\ \mathrm{unramified}} & \\[2pt]
 \mathbb P^1_\eta &&&& B_6\ (g=1) \\[2pt]
 & {}_{2}\searrow && \swarrow_{2} & \\[2pt]
 && \mathbb P^1_A &&
\end{array}$$

[\[thm:collapse\]]{#thm:collapse label="thm:collapse"} After base change to $\overline{\mathbb Q}$ and a choice of origin on the genus-one curve $E_6$, the chronological generator $\tau$ is translation by a point of exact order six. It acts trivially on geometric weight-one cohomology. In particular, over $\mathbb C$, $$\label{eq:tau-charpoly}
 \boxed{
 \chi_{\tau^*}(T)=(T-1)^2,
 \qquad
 \mu_{\tau^*}(T)=T-1.}$$ For every prime $\ell$, the same identity holds on $H^1_{\textnormal{\'et}}(E_{6,\overline{\mathbb Q}},\mathbb Q_\ell)$. As a rational $\mathsf D_6$-representation, $$\label{eq:reflection-sign}
 \boxed{
 H^1(E_6(\mathbb C),\mathbb Q)
 \simeq\varepsilon_{\mathrm{refl}}^{\oplus2},}$$ where rotations act by $+1$ and reflections by $-1$.

Lemma [\[lem:quotient-genus\]](#lem:quotient-genus){reference-type="ref" reference="lem:quotient-genus"} says that the cyclic action has no fixed point. Choose a geometric origin on $E_6$. Any automorphism of a genus-one curve then has the form $t_P\circ\varphi$, where $t_P$ is translation and $\varphi$ fixes the origin. If $\varphi\ne1$, the nonzero endomorphism $1-\varphi$ is an isogeny and is surjective over $\overline{\mathbb Q}$; the equation $(1-\varphi)Q=P$ would give a fixed point. Thus $\varphi=1$ and $\tau=t_P$. The exact order of $\tau$ in Theorem [\[thm:dihedral\]](#thm:dihedral){reference-type="ref" reference="thm:dihedral"} makes $P$ an exact six-torsion point. Translation acts trivially on Betti and $\ell$-adic cohomology, proving [\[eq:tau-charpoly\]](#eq:tau-charpoly){reference-type="eqref" reference="eq:tau-charpoly"}.

Since the rotation subgroup is trivial on the two-dimensional $H^1$, the representation factors through $\mathsf D_6/\langle\tau\rangle\simeq C_2$. The invariants of the full group have dimension $2g(E_6/\mathsf D_6)=2g(\mathbb P^1_A)=0$. The reflection therefore acts by $-1$ on both dimensions, giving [\[eq:reflection-sign\]](#eq:reflection-sign){reference-type="eqref" reference="eq:reflection-sign"}.

The theorem does not assert that $E_6$ has a chosen $\mathbb Q$-rational elliptic origin, nor that the translating torsion point is rational over $\mathbb Q$. The translation statement is geometric. The cohomological identity is independent of the choice of origin.

# A scoped threshold and a lower-period shadow {#sec:threshold}

## The first witnessed low-period time sector

For a smooth projective complex curve $E$ with a finite-order chronological automorphism $T$, define, in rational Betti cohomology, $$\label{eq:delta-def}
 \delta(E,T)=
 \dim_\mathbb QH^1(E,\mathbb Q)-\dim_\mathbb QH^1(E,\mathbb Q)^{\langle T\rangle}.$$ Over characteristic zero, invariant cohomology is the cohomology of the smooth quotient, so $\delta$ is the dimension of the sum of nontrivial time isotypic sectors.

Theorem [\[thm:collapse\]](#thm:collapse){reference-type="ref" reference="thm:collapse"} gives $$\label{eq:delta6}
 \delta(E_6,\tau)=0.$$ For comparison, HCS-C20 defines a particular adopted and dynamically certified period-seven chiral ordered component $E_7$ [@hcsc20 Thms. 1 and 3 and Appendix A]. It inherits HCS-C19's explicit correction of an apparent printed constant [@hcsc19 Prop. 1, Thm. 2, and Cor. 3]; no publisher-issued erratum and no classification of the saturated period-seven scheme are asserted. Its exact genera are $$\label{eq:c20-genera}
 g(E_7)=8,
 \qquad
 g(E_7/\langle\tau\rangle)=2.$$ Consequently, $$\label{eq:delta7}
 \delta(E_7,\tau)=16-4=12.$$

[\[cor:threshold\]]{#cor:threshold label="cor:threshold"} For the explicitly source-identified and repository-certified Hamiltonian Hénon chiral ordered components considered with $n\le7$, the smallest period at which at least one component has nontrivial weight-one time cohomology is $n=7$.

Gallas's generic class count has no chiral class below period six and one chiral doublet at period six [@gallas2007 Eqs. (2)--(7) and Table 1]. That doublet's ordered cover has $\delta=0$ by [\[eq:delta6\]](#eq:delta6){reference-type="eqref" reference="eq:delta6"}. The explicitly defined period-seven component has $\delta=12$ by [\[eq:delta7\]](#eq:delta7){reference-type="eqref" reference="eq:delta7"}.

The three inputs are displayed without extrapolation in Table [2](#tab:scoped-threshold){reference-type="ref" reference="tab:scoped-threshold"}.

::: {#tab:scoped-threshold}
   Period  Object in the comparison                             Genus   $\delta(E_n,\tau)$
  -------- --------------------------------------------------- ------- --------------------
   $n<6$   no chiral class in the published generic count        --             --
    $6$    unique source chiral doublet, ordered cover $E_6$     $1$           $0$
    $7$    adopted certified HCS-C20 component $E_7$             $8$           $12$

  : The explicitly scoped low-period chronology comparison.
:::

The corollary is a first witnessed period in this explicit low-period sample. It says nothing about all diagonal or non-diagonal components at lower periods, all period-seven chiral components, or numerical real bounded orbits at a selected parameter.

## The quadratic marker is inherited from period one

The fixed-point equation for [\[eq:ham-recurrence\]](#eq:ham-recurrence){reference-type="eqref" reference="eq:ham-recurrence"} is $$\label{eq:d1}
 D_1(u)=u^2+2u-A=0.$$ Besides the period-six reversible marker already recorded in Section [2](#sec:source){reference-type="ref" reference="sec:source"}, the source program supplies a period-seven chiral quadratic marker $$\label{eq:c7-marker}
 C_7^{\mathrm{mark}}(s_7)=s_7^2-2s_7-A.$$ The input markers come from the paragraph following equation (15) and equation (16) of [@endlergallas2006chiral p. 3]; the relations below are direct consequences.

[\[prop:marker-shadow\]]{#prop:marker-shadow label="prop:marker-shadow"} The two marker curves are affine copies of the fixed-point marker: $$\label{eq:marker-alias}
 D_6^{\mathrm{mark}}(s_6)=4D_1(s_6/2),
 \qquad
 C_7^{\mathrm{mark}}(s_7)=D_1(s_7-2).$$ Their common function field is $\mathbb Q(A,\sqrt{A+1})$. Their fiber product over the $A$-line is the reduced union $$\label{eq:fiber-product}
 (s_6-2s_7+4)(s_6+2s_7)=0.$$ Its two components meet at $(A,s_6,s_7)=(-1,-2,1)$, and its normalization is the disjoint union of the two graphs $$\label{eq:two-graphs}
 s_6=2s_7-4,
 \qquad
 s_6=-2s_7.$$

Both identities in [\[eq:marker-alias\]](#eq:marker-alias){reference-type="eqref" reference="eq:marker-alias"} follow by substitution. Solving either copy of $D_1$ gives the stated quadratic field. Eliminating $A$ from $D_6^{\mathrm{mark}}=C_7^{\mathrm{mark}}=0$ gives $$s_6^2+4s_6-4s_7^2+8s_7
 =(s_6-2s_7+4)(s_6+2s_7).$$ The two lines meet only at $s_7=1,s_6=-2$, for which $A=-1$. Normalizing a reduced union of two smooth lines separates their intersection, yielding [\[eq:two-graphs\]](#eq:two-graphs){reference-type="eqref" reference="eq:two-graphs"}.

The proposition concerns $D_6^{\mathrm{mark}}$, not the chiral ordered curve $E_6$. It is an obstruction to reading a shared quadratic marker field as primitive cross-period arithmetic. It does not prove that every possible correspondence between the full covers is absent.

## A restricted clock-divisibility obstruction

[\[thm:divisibility\]]{#thm:divisibility label="thm:divisibility"} Let $X_m$ and $X_n$ be integral varieties with automorphisms $T_m,T_n$ of exact orders $m,n$. Suppose $k\in\mathbb Z$ and a dominant rational map $\phi:X_m\dashrightarrow X_n$ satisfies $$\label{eq:equivariance}
 \phi\circ T_m=T_n^k\circ\phi.$$ Then $$\label{eq:divisibility}
 \frac{n}{\gcd(n,k)}\mid m,
 \qquad\text{equivalently}\qquad n\mid km.$$ If $\gcd(k,n)=1$, then $n\mid m$.

Iterating [\[eq:equivariance\]](#eq:equivariance){reference-type="eqref" reference="eq:equivariance"} $m$ times gives $$\phi=\phi\circ T_m^m=T_n^{km}\circ\phi.$$ The image of $\phi$ is dense, so $T_n^{km}$ is the identity as a rational automorphism of $X_n$. Since $T_n$ has exact order $n$, the equality $T_n^{km}=1$ implies $n\mid km$.

Here clock-faithful means $\gcd(k,n)=1$. No dominant single-valued clock-faithful map can therefore connect distinct periods in $\{5,6,7\}$. The theorem does not exclude non-dominant maps into boundary fixed loci, $k=0$ clock-forgetting maps, nonfaithful target clocks, or multivalued algebraic correspondences. In particular, it is not a no-Hecke-correspondence theorem.

# Route-A assessment and limitations {#sec:route-a}

The ordered-edge lift passes an important dynamical sanity check: the phase is native, time is composed chronologically, and reversal conjugates time to its inverse. The lift also creates positive genus from a source whose coarse period-six marker quotients have genus zero. Neither fact is enough for a dynamical-zeta construction. Theorem [\[thm:collapse\]](#thm:collapse){reference-type="ref" reference="thm:collapse"} shows why: the point action may remain exact while ordinary $H^1$ retains no nontrivial time character at all.

The formal Route-A evaluation is $$\label{eq:route-a-tuple}
 \boxed{
 (A1_{\mathrm{weak}},A2_{\mathrm{fail}},
  A3_{\mathrm{fail}},A4_{\mathrm{formal\ hint}}).}$$ The overall status is `ROUTE_A_EXPLORATORY`. The individual judgments are summarized in Table [3](#tab:route-a){reference-type="ref" reference="tab:route-a"}.

::: {#tab:route-a}
  ----------------------------------------------------------------------------------------------------------------------------------------------------
   Layer     Verdict    Reason
  ------- ------------- ------------------------------------------------------------------------------------------------------------------------------
    A1        weak      Native phase and reversal survive, but only selected periods are certified.

    A2        fail      No primitive cross-period product, trace-class operator, or Fredholm determinant is defined.

    A3        fail      No global Euler product, functional equation, gamma factor, or Riemann divisor is present.

    A4     formal hint  The period-seven repository correspondence is finite-dimensional [@hcsc20 Sec. 4]; no Hilbert-space operator is constructed.
  ----------------------------------------------------------------------------------------------------------------------------------------------------

  : Route-A evaluation of HCS-C21.
:::

Route B is not invoked because there is no target spectral divisor to verify.

## Mathematical and evidential limits

The result has five material limitations.

1.  The period-six theorem concerns the unique source chiral doublet, not the full exact-period-six scheme. The period-seven comparison concerns one adopted, dynamically certified component, not the saturated period-seven scheme.

2.  The threshold is therefore existential and sample-scoped. It is not an intrinsic all-period theorem and does not cover every lower-period diagonal or non-diagonal ordered component.

3.  The common quadratic marker field is a coarse quotient. The divisibility theorem rules out only dominant single-valued faithful-clock maps and leaves multivalued correspondences open.

4.  No good-prime table of joint traces $\mathop{\mathrm{Tr}}(\mathrm{Frob}_p^{r_F}\tau^s)$ is computed for $E_6$. The characteristic-zero collapse theorem does not require such a table, but an arithmetic zeta proposal would.

5.  The literature audit was targeted rather than exhaustive. The core theorem is an exact repository result with two implementations, not yet an externally peer-reviewed publication.

Most importantly, no varying-period marked family with an intrinsic primitive repetition law has been constructed. Without that law, writing a formal Euler product would merely rename unrelated fixed-period data. The absence is structural, not a numerical precision issue.

## Next breadth-first experiment

The negative result changes the search strategy. Repeating larger period-six or period-seven point-count tables would be a local extension of objects whose principal obstruction is already visible. The next large test should instead change the dynamical form or find a family in which distinct primitive periods lie in one connected algebraic tower and the time generator acts faithfully on cohomology at more than one period. Only then is it meaningful to test a chronological repetition law and a weighted determinant. This is the breadth-first stop rule supplied by C21.

# Conclusion

Ordering the period-six chiral Hénon doublet repairs the loss of point chronology. A directed edge reconstructs the radical, the six-cycle, and the full cubic splitting field. The resulting curve is geometrically connected, has deck group $\mathsf D_6$ of order twelve, and has genus one. Yet its exact order-six time generator is an unramified torsion translation and acts identically on $H^1$. Positive genus and genuine point dynamics do not by themselves produce a nontrivial cohomological time spectrum.

The cross-period comparison sharpens the same lesson. In the explicitly certified chiral sample through period seven, the first witnessed nontrivial weight-one time sector occurs on the adopted period-seven component, not on the unique period-six chiral doublet. A simultaneous quadratic marker signal does not repair the gap: both marker curves are affine copies of a period-one fixed-point curve. Their common field is inherited, not a primitive clock bridge.

These are useful negative results for a Hilbert--Pólya search. They give two early rejection tests: compute the actual time representation on cohomology before interpreting a periodic cover spectrally, and factor any cross-period marker coincidence through lower-period loci before treating it as arithmetic structure. C21 stops at those tests. It supplies neither a repetition law nor a determinant, and the next round should move to a different dynamical form if no connected varying-period tower can be found.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

All exact formulas, source locks, code, machine-readable certificates, independent checks, mutation tests, and Route-A records are released in the HCS-C21 project directory at <https://github.com/maris205/hilbert-polya-structure/tree/hcs-c21-v1/henon_dynamics/henon_chiral_chronology_threshold>. The manuscript uses no Riemann-zero table, prime fitting table, learned parameter, or averaged transition matrix.

#### Author contributions (CRediT).

Anonymous author: Conceptualization, Methodology, Formal analysis, Investigation, Software, Validation, Project administration, Writing---original draft, and Writing---review and editing. AI systems are not authors.

#### Funding.

No external funding source is declared for this repository research note.

#### Conflicts of interest.

No conflict of interest is declared.

#### Ethics.

The work is a mathematical and symbolic-computational study. It involves no human participants, animals, personal data, or clinical intervention; human or animal research approval is therefore not applicable.

#### AI-use disclosure.

OpenAI Codex assisted with literature-search strategy, symbolic-code development, proof stress testing, manuscript drafting, citation checking, and formatting. The research direction and claim boundaries were directed by the author. Every released exact output is bound to a deterministic producer certificate and separately implemented checker, and all arguments new to C21 are written out in the manuscript; imported results are cited explicitly. The author takes responsibility for the accuracy and integrity of the work.

# Reproducibility and integrity {#app:reproducibility}

## Exact computation

The producer uses exact rational and symbolic algebra. From the project directory, regenerate and verify the frozen artifacts with

    python -m pip install -r requirements.txt
    python code/c21_producer.py --output results/c21_certificate.json
    python code/c21_independent_check.py \
      --certificate results/c21_certificate.json \
      --output results/c21_independent_check.json
    python -m unittest discover -s code -p 'test_c21.py' -v
    sha256sum -c results/ARTIFACT_HASHES.sha256

The independent checker imports neither the producer nor predecessor implementations. It reconstructs the source polynomial, matching map, irreducibility ledger, group action, branch and genus ledger, fixed field, marker shadow, and clock-divisibility fields. The fourteen-test suite includes ten mutation tests. These alter the candidate identity, source coefficients, cover relations, genus, sheet-separation resultant, fixed-field equation, time character, threshold scope, marker factorization, or clock-averaging flag; each mutation must be rejected.

The frozen producer certificate has SHA-256

    5386c95cbc65e6a4323cfcf230de6b41f353be909d197818f9c4fbf0a75a96fc

and the independent report has SHA-256

    0f14332f36f2f7df0ab238954c5a8531bcb9d759f8feeac60bc7bcc197452985.

The checker reports `PASS` with 133 named checks.

## Source locks

The exact run fails closed if any dependency in Table [4](#tab:source-locks){reference-type="ref" reference="tab:source-locks"} changes.

::: {#tab:source-locks}
  ----------------------------------------------------------------------------------------------
  Dependency             Frozen SHA-256
  ---------------------- -----------------------------------------------------------------------
  Paper-5 local PDF      `23dad812162728316f633081e1a1995d4` `c00614a70d0f5877d425c68d0c726b9`

  HCS-C12C certificate   `964b8c98abc850493529b8e939a9c8ff` `96c832300ad2b1629b1cff807f0e8020`

  HCS-C20 certificate    `7ee43e3253aff15ec00d78b9633c3d33` `62e71cd5a880cd3e928e7f322abb2681`
  ----------------------------------------------------------------------------------------------

  : Frozen source dependencies for the HCS-C21 exact run.
:::

The local Paper-5 bytes are frozen, but no page-specific assertion in this paper depends on an unavailable local PDF text-extraction preflight. The decisive period-six formulas were separately checked in the primary Endler--Gallas article [@endlergallas2006chiral Eq. (15)].

## Manuscript build

The bilingual manuscript uses LuaLaTeX because the host has no XeLaTeX or CJKutf8 package. It requires `latexmk`, `fontspec`, Babel's Traditional-Chinese locale, and the `Droid Sans Fallback` font. Before building, check the engine and font from the `paper/` directory, then run

    lualatex --version
    fc-match "Droid Sans Fallback"
    latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex

The font preflight must resolve to an installed CJK-capable font under that name. The Traditional-Chinese abstract uses it; the rest of the manuscript uses the default Latin Modern family.

# Exact algebraic ledgers {#app:ledgers}

## Source expansion

Multiplying the two published cubic factors [@endlergallas2006chiral Eq. (15)] gives $$\begin{aligned}
P_6(A,X)={}&X^6-2X^5+(4-3A)X^4+(4A-2)X^3\\
&+(3A^2-8A+2)X^2+(-2A^2+2A)X\\
&-A^3+4A^2-2A+1.\end{aligned}$$ Independent symbolic discriminant calculation gives $$\mathop{\mathrm{Disc}}_X(P_6)=64(A-3)^3(16A^2-8A+5)^2.$$ The certificate stores canonical representations and hashes for the factors, the expansion, and both discriminants.

## Recurrence reductions

Let $I$ be the ideal generated by $$\alpha+\beta+\gamma-(1+\eta),
 \qquad
 \alpha\beta+\alpha\gamma+\beta\gamma+A,$$ together with $\alpha\beta\gamma-1+A(1+\eta)$ and $A-\eta^2-3$. For the sequence [\[eq:orbit-sequence\]](#eq:orbit-sequence){reference-type="eqref" reference="eq:orbit-sequence"}, exact Gröbner reduction gives $$x_{i+1}+x_{i-1}+x_i^2-A\equiv0\pmod I,
 \qquad 0\le i<6.$$ The even and odd sum remainders are respectively $1+\eta$ and $1-\eta$, which binds the intrinsic recovery formula [\[eq:eta-recovery\]](#eq:eta-recovery){reference-type="eqref" reference="eq:eta-recovery"}. The same exact ledger gives $\operatorname{Res}_X(f_\eta,f_{-\eta})=8\eta^3$, separating the sheets on the generic open $U$.

## Infinity and fixed-field controls

The infinity chart [\[eq:infinity-chart\]](#eq:infinity-chart){reference-type="eqref" reference="eq:infinity-chart"} has one simple slope $u=-1$ and two branches at $u=1$ with first corrections $c=0,1$. The three branches are integral in the scaled $u$ and $c$ charts, while the original $X$-roots are Laurent series in $t^{-1}\overline{\mathbb Q}[[t]]$. The checker refuses certificates that add an infinite branch contribution to Riemann--Hurwitz.

For the rotation quotient, the checker independently verifies $$\prod_{i<j}(\alpha_i+\alpha_j)=e_1e_2-e_3=-1,
 \qquad
 v^2=(A-3)(16A^2-8A+5),$$ the nonsquare degree-two field, subgroup order six, and subgroup index two. It also verifies the squarefree cubic discriminant $-4{,}000{,}000$ and the resulting zero ramification ledger.

## Negative controls

Half-orbit elimination from a reversible seed splits after base change along $D_1$ at period six, while the period-five and period-seven controls used in the project remain irreducible over the same rational function field. These checks support the interpretation of the observed quadratic coincidence as a specific lower-period alias. They are not used to classify all primitive components and are not inputs to Corollary [\[cor:threshold\]](#cor:threshold){reference-type="ref" reference="cor:threshold"}.
