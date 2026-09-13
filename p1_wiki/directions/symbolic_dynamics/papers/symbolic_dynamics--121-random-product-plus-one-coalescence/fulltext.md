---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--121-random-product-plus-one-coalescence"
canonical_tex: "symbolic_dynamics/papers/121-random-product-plus-one-coalescence/main.tex"
canonical_pdf: "symbolic_dynamics/papers/121-random-product-plus-one-coalescence/main.pdf"
source_sha256: "209bba3a1d45b2ec79c2278643153163374264e9626ba858bd9de36513dbcf19"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Higher-Moment Pole Ladders in Product-Plus-One Coalescence: A Yule-Averaged Marked Refinement

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/121-random-product-plus-one-coalescence>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/121-random-product-plus-one-coalescence/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/121-random-product-plus-one-coalescence/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/121-random-product-plus-one-coalescence/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/121-random-product-plus-one-coalescence/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Start with $n$ ordered copies of $1$, repeatedly choose a current adjacent pair uniformly, and replace $(x,y)$ by $xy+1$; write $X_n$ for the terminal value. Disanto, Fuchs, Paningbatan, and Rosenberg proved that the number $R_n$ of root ancestral configurations in a Yule--Harding random tree obeys the same recursion after the shift $X_n=R_n+1$. We prove the identification under the common ordered-history coupling and assign their split law, finite distribution, unmarked antichain interpretation, mean analysis, and second-moment neighborhood zero contribution credit. After this subtraction, and after crediting the existing fixed-tree cardinality marker, we obtain its Yule-averaged bivariate transform in closed form. The all-order moment equation is a mechanical expansion of the owned exact law. The main residual theorem continues the two owned low-order radii to a strict ladder: for every $r\geq3$, the $r$th raw-moment series has a normalized positive simple pole at a radius $\rho_r<\rho_{r-1}$ and $\limsup_n(\mathbb EX_n^r)^{1/n}=\rho_r^{-1}$. No full coefficient asymptotic is claimed for $r\geq3$. The residual has passed only a bounded owner audit; novelty, priority, and external release remain open.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Higher-Moment Pole Ladders in Product-Plus-One Coalescence:\
  A Yule-Averaged Marked Refinement
```

## Markdown 正文

# Introduction and scope

Consider the following rank-decreasing random dynamics. Begin with the ordered word $(1,\ldots,1)$ of length $n$. If the current word has $j$ entries, choose one of its $j-1$ adjacent pairs with probability $1/(j-1)$ and apply $$\label{eq:merge}
                 (x,y)\longmapsto xy+1.$$ After $n-1$ mergers a positive integer $X_n$ remains. The local rule is nonassociative, so $X_n$ depends on the entire merger genealogy. The first nondegenerate law already occurs at $n=4$: $$\mathbb P(X_4=4)=\frac23,\qquad \mathbb P(X_4=5)=\frac13.$$

The decisive owner is not merely a generic random-tree neighbor. @DisantoEtAl2022 study the number $R_n$ of root ancestral configurations under the Yule--Harding model. Their Proposition 3.5 gives $R_1=0$ and the uniform-split recurrence $R_n\overset d=(R_I+1)(R'_{n-I}+1)$, including the exact finite law. Their Section 3.2 identifies root configurations with nonempty antichains of the pruned internal-node tree; Sections 5.2--5.3 derive the mean and second-moment Riccati analyses. Thus $X_n=R_n+1$ is the same statistic in shifted notation. All of those statements, including the mean pole $1-\exp(-2\pi/(3\sqrt3))$ and the order-two growth analysis, receive zero contribution credit here.

Two further owners narrow the residual. The cardinality refinement on a fixed rooted-tree poset is studied by @AndriantianaWagnerWang2013; only its average under the Yule/uniform ordered-history law and the resulting closed bivariate transform are at issue here. Moreover, @ChangFuchs2010 [Table 1] give the exact Yule--Harding probability $2^{n-2}/(n-1)!$ of an $n$-caterpillar, building on the caterpillar analysis of @Rosenberg2006. Both the minimizing shape and its probability therefore receive zero credit.

The genealogy itself is also classical. Each current boundary is an undeleted original boundary, and successive uniform choices form a uniform permutation. Its max-Cartesian tree has the usual random binary-search-tree (BST) root-split law. The same subtraction applies to deterministic subtree enumeration [@Ruskey1981Subtrees], ideals of forest posets [@KodaRuskey1993Ideals], antichain statistics on rooted plane trees [@Klazar1997Twelve], and random forest ideals [@Janson2002Ideals]. Random-BST generating-function schemes and singularity methods are also established [@FlajoletGourdonMartinez1997Patterns; @MartinezPanholzerProdinger1998Descendants; @FlajoletSedgewick2009].

After those deductions, the paper records only the following residual package:

1.  the Yule-averaged bivariate ordinary generating function for the owned fixed-tree cardinality marker, together with its closed Euler form; and

2.  beginning at $r=3$, a strict continuation of the moment-radius ladder with unit residues and exact exponential limsups. The all-order triangular identity is retained only as the mechanical interface from the owned exact law.

The higher-moment conclusion is deliberately limited to a positive simple pole and an exact exponential *limsup*. Without control of all complex singularities, no full asymptotic is asserted for $r\geq3$. The direct owner has a stronger order-two conclusion than the ceiling used here.

Two complementary viewpoints organize the proofs. The temporal viewpoint uses uniform deletion orders, conditional root splits, moments, and Riccati--Euler equations. The structural viewpoint regards the same orders as heap labelings of Cartesian trees and interprets the output as a cardinality-marked antichain count. Both viewpoints use the same split law; we do not present them as probabilistically independent proofs. The second viewpoint supplies a Yule-averaged cardinality transform and exact comb controls rather than a new random-tree model. A focused search of the direct owner's citation neighborhood and current root-configuration formulations did not locate the averaged transform or a strict $r\geq3$ continuation of the owned low-order pole ladder. This bounded non-hit is not evidence of novelty or priority. External circulation remains [hold]{.smallcaps}.

# Direct-owner interface and the exact shift

Label the $n-1$ original boundaries by $1,\ldots,n-1$. A merger deletes exactly the boundary separating the two merged blocks; every other current boundary retains its original label.

[\[thm:split\]]{#thm:split label="thm:split"} Let $I_n$ be uniform on $\{1,\ldots,n-1\}$. Conditional on $I_n=i$, let $X_i$ and $X'_{n-i}$ be independent copies generated on the two sides of the last-deleted boundary. Then $$\label{eq:split}
 X_1=1,\qquad
 X_n\ \overset d=\ 1+X_{I_n}X'_{n-I_n}\quad(n\geq2).$$ Consequently, if $p_n(v)=\mathbb P(X_n=v)$, then $p_1(v)=\mathbf 1_{\{v=1\}}$ and $$\label{eq:law}
 p_n(v)=\frac1{n-1}\sum_{i=1}^{n-1}
 \sum_{\substack{a,b\geq1\\1+ab=v}}p_i(a)p_{n-i}(b).$$ Every law in [\[eq:law\]](#eq:law){reference-type="eqref" reference="eq:law"} has finite support. Moreover, couple the merger process to the ordered unlabeled history having the same boundary order. If $R_n$ counts its root configurations, then $$\label{eq:shift}
                         X_n=R_n+1$$ for every history, not only in distribution.

When $j$ blocks remain, precisely $j-1$ original boundaries remain, and the process selects each with probability $1/(j-1)$. Thus the complete deletion order is a uniform permutation of $\{1,\ldots,n-1\}$. Its last element is uniform. Conditional on that element being $i$, the relative orders of the $i-1$ left boundaries and the $n-i-1$ right boundaries are independent and uniform. All mergers on each side occur before the last deletion, after which [\[eq:merge\]](#eq:merge){reference-type="eqref" reference="eq:merge"} combines the two terminal side values. This proves [\[eq:split\]](#eq:split){reference-type="eqref" reference="eq:split"}. Conditioning on $I_n$ and the two side values gives [\[eq:law\]](#eq:law){reference-type="eqref" reference="eq:law"}. Finiteness follows inductively. These distributional statements reproduce Proposition 3.5 of @DisantoEtAl2022 after a shift and receive zero credit.

For the objectwise identification, let $T$ be the common ordered evaluation tree. At a leaf, its root-configuration count is $R(T)=0$, while the merger value is $V(T)=1$. At an internal root, the standard root-configuration decomposition gives $$R(T)=\bigl(R(T_L)+1\bigr)\bigl(R(T_R)+1\bigr).$$ Induction and $V(T)=1+V(T_L)V(T_R)$ now give $V(T)=R(T)+1$. This proves [\[eq:shift\]](#eq:shift){reference-type="eqref" reference="eq:shift"}; the root-configuration recurrence and its unmarked antichain interpretation are owned by @DisantoEtAl2022.

The proof also fixes the orientation: the *last* deleted boundary is the root of the evaluation tree. Reversing the deletion order exchanges maxima and minima in the Cartesian-tree description and is not the process above.

# Heap labelings and a marked antichain transform

For a fixed deletion order, let $T$ be the ordered full binary evaluation tree. Its leaves carry $1$, and every internal vertex applies $V(T)=1+V(T_L)V(T_R)$. Order the internal vertices by ancestry. For an indeterminate $s$, define $$P_T(s)=\sum_{B} s^{|B|},$$ where $B$ ranges over antichains of internal vertices, including the empty antichain. Put $P_{\mathrm{leaf}}(s)=1$.

[\[lem:antichain\]]{#lem:antichain label="lem:antichain"} For every evaluation tree, $$\label{eq:treepoly}
 P_T(s)=s+P_{T_L}(s)P_{T_R}(s),\qquad V(T)=P_T(1).$$

An antichain either contains the root, in which case it is the singleton root, or excludes the root, in which case its restrictions to the two subtrees are arbitrary antichains and can be chosen independently. The first identity follows. Its specialization at $s=1$ is the same recursion and initial condition as $V(T)$.

At $s=1$, this is precisely the direct owner's correspondence: $R(T)$ counts nonempty antichains and $X(T)=R(T)+1$ also includes the empty one. For general $s$, the fixed-tree cardinality marker and the equivalent root-subtree leaf statistic are also owned by @AndriantianaWagnerWang2013. Only averaging this marker under the Yule/uniform ordered-history law and solving the resulting bivariate equation belong to the residual claim set.

Let $T_n$ denote the tree induced by a uniform boundary order and write $$a_n(s)=\mathbb EP_{T_n}(s),\qquad
 A(z,s)=\sum_{n\geq1}a_n(s)z^{n-1}.$$

[\[thm:marked\]]{#thm:marked label="thm:marked"} Coefficientwise as a formal series in $z$ and $s$, $$\label{eq:markedriccati}
 \partial_z A=A^2+\frac{s}{(1-z)^2},\qquad A(0,s)=1.$$ Set $w=1-z$, $$\delta=\sqrt{1-4s},\qquad
 \beta_\pm=\frac{1\pm\delta}{2},$$ and $$\label{eq:Y}
 Y(w,s)=\frac{\beta_+w^{\beta_+}-\beta_-w^{\beta_-}}{\delta}.$$ With the removable value $$Y(w,1/4)=w^{1/2}\left(1+\frac12\log w\right),$$ the solution is $$\label{eq:markedclosed}
                     A(z,s)=\frac{Y_w(1-z,s)}{Y(1-z,s)}.$$ In particular, $[z^{n-1}s^k]A$ is the exact expected number of $k$-element internal-node antichains, and $A(z,1)$ is the mean series of $X_n$.

The split law and [\[lem:antichain\]](#lem:antichain){reference-type="ref" reference="lem:antichain"} give, for $n\geq2$, $$\label{eq:markedrec}
 a_n(s)=s+\frac1{n-1}\sum_{i=1}^{n-1}a_i(s)a_{n-i}(s).$$ Multiplying by $(n-1)z^{n-2}$ and summing gives [\[eq:markedriccati\]](#eq:markedriccati){reference-type="eqref" reference="eq:markedriccati"}. The function in [\[eq:Y\]](#eq:Y){reference-type="eqref" reference="eq:Y"} satisfies $$Y_{ww}+\frac{s}{w^2}Y=0,\qquad Y(1,s)=Y_w(1,s)=1.$$ Because $\partial_z=-\partial_w$, the logarithmic derivative $A=Y_w/Y$ satisfies [\[eq:markedriccati\]](#eq:markedriccati){reference-type="eqref" reference="eq:markedriccati"} and the initial condition. Uniqueness of formal solutions proves [\[eq:markedclosed\]](#eq:markedclosed){reference-type="eqref" reference="eq:markedclosed"}. Taking the limit $\delta\to0$ in [\[eq:Y\]](#eq:Y){reference-type="eqref" reference="eq:Y"} gives the displayed removable value. The coefficient interpretation is the definition of $a_n(s)$, and [\[lem:antichain\]](#lem:antichain){reference-type="ref" reference="lem:antichain"} gives $a_n(1)=\mathbb EX_n$.

Equation [\[eq:markedclosed\]](#eq:markedclosed){reference-type="eqref" reference="eq:markedclosed"} is interpreted formally near $s=0$, or analytically with consistent branches. At $s=0$ it gives $A(z,0)=(1-z)^{-1}$, recording the unique empty antichain. The marked transform adds a coefficient-level statement, but its derivation still uses the same classical root split as [\[thm:split\]](#thm:split){reference-type="ref" reference="thm:split"}.

# All raw moments and a strict radius cascade

For integers $r\geq0$ set $$m_{r,n}=\mathbb EX_n^r,\qquad
 F_r(z)=\sum_{n\geq1}m_{r,n}z^{n-1}.$$ Thus $m_{0,n}=1$ and $F_0(z)=(1-z)^{-1}$.

[\[prop:moments\]]{#prop:moments label="prop:moments"} For $n\geq2$ and $r\geq0$, $$\label{eq:momentrec}
 (n-1)m_{r,n}=\sum_{i=1}^{n-1}\sum_{k=0}^r
       \binom rk m_{k,i}m_{k,n-i}.$$ Equivalently, $$\label{eq:momentode}
 F_r'(z)=\sum_{k=0}^r\binom rk F_k(z)^2,
 \qquad F_r(0)=1.$$ At level $r$, the only new function on the right is $F_r^2$.

Condition on the split in [\[eq:split\]](#eq:split){reference-type="eqref" reference="eq:split"}, expand $(1+ab)^r=\sum_{k=0}^r\binom rk a^k b^k$, and use conditional independence. This gives [\[eq:momentrec\]](#eq:momentrec){reference-type="eqref" reference="eq:momentrec"}. Coefficient extraction from the square of each $F_k$ gives [\[eq:momentode\]](#eq:momentode){reference-type="eqref" reference="eq:momentode"}.

The cases $r=1,2$ lie in the mean/variance analysis of @DisantoEtAl2022. More generally, the displayed identity is a one-line binomial expansion of their exact distributional recurrence. It therefore receives zero contribution credit and serves only as the interface for the strict higher-order theorem; no elementary solution is claimed at every level.

[\[thm:radii\]]{#thm:radii label="thm:radii"} There are numbers $$\label{eq:rholadder}
             1=\rho_0>\rho_1>\rho_2>\cdots>0$$ such that $\rho_r$ is the radius of convergence of $F_r$. For every $r\geq1$, $$\label{eq:localpole}
 F_r(z)=\frac1{\rho_r-z}+O(1)\qquad(z\to\rho_r),$$ and $$\label{eq:limsup}
 \limsup_{n\to\infty}\bigl(\mathbb EX_n^r\bigr)^{1/n}=\rho_r^{-1}.$$ The residual assertion begins at $r=3$: the cases $r=1,2$ are retained only as the owned base of the continuation.

Proceed by induction from $F_0(z)=(1-z)^{-1}$ and $\rho_0=1$. For $r\geq1$, separate the new unknown in [\[eq:momentode\]](#eq:momentode){reference-type="eqref" reference="eq:momentode"}: $$\label{eq:Gr}
 F_r'=F_r^2+G_r,\qquad
 G_r=\sum_{k=0}^{r-1}\binom rk F_k^2.$$ On $|z|<\rho_{r-1}$, let $U_r$ solve $$\label{eq:Ur}
 U_r''+G_rU_r=0,\qquad U_r(0)=1,\quad U_r'(0)=-1.$$ The logarithmic derivative $-U_r'/U_r$ satisfies [\[eq:Gr\]](#eq:Gr){reference-type="eqref" reference="eq:Gr"} and agrees with $F_r$ near zero.

By induction, all terms in $G_r$ except the one containing $F_{r-1}$ are analytic at $\rho_{r-1}$, while [\[eq:localpole\]](#eq:localpole){reference-type="eqref" reference="eq:localpole"} gives $$\label{eq:Gedge}
 G_r(x)=\frac{r}{(\rho_{r-1}-x)^2}
        +O\!\left(\frac1{\rho_{r-1}-x}\right)
 \quad (x\uparrow\rho_{r-1}).$$ Choose $c$ with $1/4<c<r$. Close enough to $\rho_{r-1}$, $G_r(x)\geq c(\rho_{r-1}-x)^{-2}$. Every nonzero solution of the Euler comparison equation $$V''+\frac{c}{(\rho_{r-1}-x)^2}V=0$$ has infinitely many zeros accumulating at $\rho_{r-1}$: after putting $s=\rho_{r-1}-x$, it is a linear combination of $s^{1/2}\cos(\nu\log s)$ and $s^{1/2}\sin(\nu\log s)$, with $\nu=\sqrt{4c-1}/2$. If $U_r$ has not already vanished, choose two consecutive comparison zeros after the point where the coefficient inequality holds. The Sturm comparison theorem forces a zero of $U_r$ strictly between them [@Zettl2005 Chapter 1]. Hence $U_r$ vanishes strictly before $\rho_{r-1}$. Let $\rho_r$ be its first positive zero. Then $0<\rho_r<\rho_{r-1}$.

The coefficient $G_r$ is analytic at $\rho_r$. A double zero of $U_r$ would contradict uniqueness for [\[eq:Ur\]](#eq:Ur){reference-type="eqref" reference="eq:Ur"}, so the zero is simple. Consequently $-U_r'/U_r$ has the normalized local form [\[eq:localpole\]](#eq:localpole){reference-type="eqref" reference="eq:localpole"}.

It remains to identify the positive pole with the complex radius. The coefficients of $F_r$ are positive. If its radius $R$ were smaller than $\rho_r$, Pringsheim's theorem would force a singularity at the positive point $R$ [@FlajoletSedgewick2009 Section IV.6]. Yet $G_r$ is analytic there and $U_r$ has no positive zero before $\rho_r$, so $-U_r'/U_r$ is analytic in a neighborhood of $R$, a contradiction. Thus $R=\rho_r$. Cauchy--Hadamard now gives [\[eq:limsup\]](#eq:limsup){reference-type="eqref" reference="eq:limsup"}; replacing the exponent $1/(n-1)$ by $1/n$ does not change the limit superior.

[\[rem:ceiling\]]{#rem:ceiling label="rem:ceiling"} The local pole in [\[eq:localpole\]](#eq:localpole){reference-type="eqref" reference="eq:localpole"} lies at the positive convergence radius, but the proof does not exclude other singularities of the same modulus. Accordingly, [\[thm:radii\]](#thm:radii){reference-type="ref" reference="thm:radii"} claims only [\[eq:limsup\]](#eq:limsup){reference-type="eqref" reference="eq:limsup"} for $r\geq3$. A statement such as $\mathbb EX_n^r\sim\rho_r^{-n}$ would require an additional dominant-singularity theorem and is not part of this paper. The stronger order-two asymptotic in @DisantoEtAl2022 is not weakened or reclaimed.

# Owned mean and endpoint normalizations

At $r=1$, the forcing in [\[eq:Gr\]](#eq:Gr){reference-type="eqref" reference="eq:Gr"} is explicit. This permits a complete coefficient asymptotic, unlike the higher levels.

[\[thm:mean\]]{#thm:mean label="thm:mean"} Let $M=F_1$ and $w=1-z$. Then $$\label{eq:meanode}
 M'=M^2+\frac1{(1-z)^2},\qquad M(0)=1,$$ and $$\label{eq:meanclosed}
 M(z)=\frac1w\left[
 \frac12-\frac{\sqrt3}{2}
 \tan\!\left(\frac{\sqrt3}{2}\log w-\frac\pi6\right)
 \right].$$ Its unique dominant singularity is the simple pole $$\label{eq:rho}
 \rho=1-\exp\!\left(-\frac{2\pi}{3\sqrt3}\right)
      =0.7015639408\ldots .$$ For some $R>\rho$, $$\label{eq:meanasymptotic}
 \mathbb EX_n=\rho^{-n}+O(R^{-n}),\qquad
 \rho^{-1}=1.4253868276\ldots .$$ In particular, the leading coefficient is one.

Equation [\[eq:meanode\]](#eq:meanode){reference-type="eqref" reference="eq:meanode"} is the case $r=1$ of [\[prop:moments\]](#prop:moments){reference-type="ref" reference="prop:moments"}. Write $M=-U'/U$. Then $$U''+\frac{U}{(1-z)^2}=0,\qquad U(0)=1,\quad U'(0)=-1.$$ With $\alpha=\sqrt3/2$, the solution is $$\label{eq:Umean}
 U(z)=\frac2{\sqrt3}w^{1/2}
 \cos\!\left(\alpha\log w-\frac\pi6\right).$$ Since $M=U_w/U$, differentiation yields [\[eq:meanclosed\]](#eq:meanclosed){reference-type="eqref" reference="eq:meanclosed"}.

In $|z|<1$, the number $w=1-z$ lies in the right half-plane, so the principal logarithm is analytic. The zeros of the cosine in [\[eq:Umean\]](#eq:Umean){reference-type="eqref" reference="eq:Umean"} satisfy $$w_k=\exp\!\left[\frac2{\sqrt3}
       \left(\frac{2\pi}{3}+k\pi\right)\right],
 \qquad k\in\mathbb Z.$$ They are positive real because all complex zeros of cosine are real. The zero $k=-1$ gives [\[eq:rho\]](#eq:rho){reference-type="eqref" reference="eq:rho"}. The zeros with $k\leq-2$ correspond to larger positive $z<1$, while those with $k\geq0$ give $|z|>1$; the logarithm first branches at $z=1$. Hence $\rho$ is the unique singularity on its circle and is isolated from the next one. The logarithmic derivative of a simple zero has local form $1/(\rho-z)+O(1)$. Coefficient extraction gives [\[eq:meanasymptotic\]](#eq:meanasymptotic){reference-type="eqref" reference="eq:meanasymptotic"}.

The theorem is the shifted form of the Yule--Harding mean analysis in @DisantoEtAl2022 [Section 5.2]; no part of it is counted as a residual advance.

The opposite edge of the distribution also has a closed form.

[\[prop:minimum\]]{#prop:minimum label="prop:minimum"} For every $n\geq1$, $X_n\geq n$. For $n\geq2$, $$\label{eq:minatom}
       \min\operatorname{supp}X_n=n,
       \qquad
       \mathbb P(X_n=n)=\frac{2^{n-2}}{(n-1)!}.$$

For positive integers, $xy+1\geq x+y$, with equality exactly when $x=1$ or $y=1$. Induct on $n$ in [\[eq:split\]](#eq:split){reference-type="eqref" reference="eq:split"}. If the root split has sizes $i$ and $j=n-i$, then $$1+X_iX'_j\geq1+ij=i+j+(i-1)(j-1)\geq n.$$ Equality requires minimal values in both subtrees and an endpoint split $i=1$ or $j=1$. Iterating this condition gives precisely the planar combs. Among the $(n-1)!$ boundary orders, their number $c_n$ satisfies $c_2=1$ and $c_n=2c_{n-1}$ for $n\geq3$. Thus $c_n=2^{n-2}$, which proves [\[eq:minatom\]](#eq:minatom){reference-type="eqref" reference="eq:minatom"}.

The fact that the caterpillar minimizes the number of root configurations is already recorded by @DisantoEtAl2022 [Section 2.4.4]. The displayed mass is exactly the Yule--Harding $n$-caterpillar probability printed by @ChangFuchs2010 [Table 1]; @Rosenberg2006 is the earlier caterpillar-pattern owner. The proof is retained only as a translation to the adjacent-deletion encoding, and the entire proposition receives zero contribution credit.

# Exact coefficient controls and proof dependencies

The first marked polynomials make the coefficient interpretation concrete. They were obtained both from [\[eq:markedrec\]](#eq:markedrec){reference-type="eqref" reference="eq:markedrec"} and by averaging over every boundary order through $n=9$.

::: {#tab:marked}
    $n$ $a_n(s)=\mathbb EP_{T_n}(s)$                                   $\mathbb EX_n$
  ----- -------------------------------------------------------------- ------------------
      1 $1$                                                            $1$
      2 $1+s$                                                          $2$
      3 $1+2s$                                                         $3$
      4 $1+3s+\frac13s^2$                                              $\frac{13}{3}$
      5 $1+4s+\frac76s^2$                                              $\frac{37}{6}$
      6 $1+5s+\frac{13}{5}s^2+\frac{2}{15}s^3$                         $\frac{131}{15}$
      7 $1+6s+\frac{47}{10}s^2+\frac{59}{90}s^3$                       $\frac{556}{45}$
      8 $1+7s+\frac{263}{35}s^2+\frac{121}{63}s^3+\frac{17}{315}s^4$   $\frac{787}{45}$

  : Exact expected cardinality-marked antichain polynomials. At $s=1$, the owned root-configuration statistic satisfies $R_n=X_n-1$. The machine-readable artifact continues through $n=12$.
:::

The standard-library verifier implements two independent finite calculations where such independence is literal: direct adjacent merging for each boundary permutation and dynamic programming from the split law. It also compares the marked tree polynomials with [\[eq:markedriccati\]](#eq:markedriccati){reference-type="eqref" reference="eq:markedriccati"}, raw moments with [\[eq:momentode\]](#eq:momentode){reference-type="eqref" reference="eq:momentode"}, the Euler-series logarithmic derivative with the mean coefficients, and the comb count with [\[eq:minatom\]](#eq:minatom){reference-type="eqref" reference="eq:minatom"}. The exact artifact records $a_n(s)$, the first two moments, minimum mass, and support size through $n=12$.

These checks do not prove the singularity statements. Conversely, the analytic proof does not turn the heap-labeling viewpoint into a second probability law: both temporal and structural calculations inherit the same uniform split from [\[thm:split\]](#thm:split){reference-type="ref" reference="thm:split"}. The honest dependency chain is $$\text{uniform boundaries}
 \Longrightarrow \text{BST split}
 \Longrightarrow
 \begin{cases}
   \text{finite law and moment Riccati hierarchy},\\
   \text{heap-labeled tree and marked antichains}.
 \end{cases}$$ The two branches cross-check finite coefficients and extremal combs, while the Sturm--Pringsheim argument is specific to the temporal moment branch.

# Ownership boundary and conclusion

Most importantly, @DisantoEtAl2022 own the same statistic under $R_n=X_n-1$: the Yule split and finite law, root configurations and unmarked antichains, the mean Riccati equation and pole, and the second-moment/variance neighborhood all receive zero credit. Uniform random-BST splitting, Cartesian trees, forest ideals, Riccati linearization, Pringsheim's theorem, and generic singularity extraction are also background. @AndriantianaWagnerWang2013 own fixed-tree cardinality-marked antichains, and @ChangFuchs2010 [@Rosenberg2006] own the caterpillar probability neighborhood. The residual recorded here is only the Yule-averaged bivariate transform and, centrally, the strict pole/radius continuation for every $r\geq3$. The all-order identity is a mechanical interface, not a separate advance. We do not claim that all equivalent terminology or unpublished work has been exhausted.

The product-plus-one encoding is useful because it turns the owned root-configuration statistic into a literal adjacent dynamics. Retaining a fixed-tree cardinality marker and averaging it under the Yule law yields the exact transform, while the triangular Riccati system lets the two low-order owner results propagate to a strict hierarchy at every higher order. Those higher moments stop at the exact limsup in [\[rem:ceiling\]](#rem:ceiling){reference-type="ref" reference="rem:ceiling"}. Novelty, priority, and external dissemination remain [hold]{.smallcaps} pending specialist review.
