---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--78-complete-bipartite-sandpile-translations"
canonical_tex: "symbolic_dynamics/papers/78-complete-bipartite-sandpile-translations/main.tex"
canonical_pdf: "symbolic_dynamics/papers/78-complete-bipartite-sandpile-translations/main.pdf"
source_sha256: "7629a2137d5dabdf34404b329463de0d29f4da4e8d6f3117f0f51fea20d325ef"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Localized Addition Periods and Zeta Functions for Complete-Bipartite Sandpiles

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/78-complete-bipartite-sandpile-translations>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/78-complete-bipartite-sandpile-translations/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/78-complete-bipartite-sandpile-translations/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/78-complete-bipartite-sandpile-translations/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/78-complete-bipartite-sandpile-translations/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Choose a sink in the $n$-vertex part of the complete bipartite graph $K_{m,n}$. On recurrent Abelian sandpiles, any integral loading profile $w$ defines a permutation $T_w$. We compute every coordinate of $Q_{m,n}^{-1}w$ and hence the exact order $L(w)$ as a finite least common multiple of explicit reduced denominators. All $m^{n-1}n^{m-1}$ recurrent states then split into cycles of the same length $L(w)$, giving every iterate fixed-point count, the Artin--Mazur zeta function, all ergodic invariant measures, and the Koopman spectrum. A two-site specialization has up to four denominator classes, with three when $n=2$. In particular, adding at a vertex opposite the sink has period $mn$, whereas adding at another vertex in the sink part has period $m$. Exact reduced-Laplacian checks cover both arbitrary and two-site profiles; literal burning, stabilization, and orbit enumeration cover every $K_{m,n}$ with $2\leq m,n\leq4$.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 27 August 2026'
title: 'Localized Addition Periods and Zeta Functions for Complete-Bipartite Sandpiles'
```

## Markdown 正文

# Introduction

The Abelian sandpile model turns local chip addition followed by stabilization into a finite dynamical system. Dhar's addition operators commute, and their restriction to recurrent configurations forms a finite Abelian group [@Dhar1990; @DharEtAl1995]. Algebraically this group is the cokernel of the reduced graph Laplacian. These facts convert a dynamical question---the period of a prescribed loading protocol---into an integral lattice question.

Complete bipartite graphs have an especially explicit critical group. Lorenzini computed its bipartite form [@Lorenzini1991]; @JacobsonEtAl2003 review that case and solve the complete multipartite problem. Recurrent and parking configurations on $K_{m,n}$ also have a rich operator and cyclic-lemma description [@AvalEtAl2016], and recent work compares Abelian and stochastic recurrent models on the same graph family [@SeligZhu2025]. We take these structures as prior art. Our narrower objective is to retain the physical coordinates of an arbitrary loading profile relative to a fixed sink, rather than pass immediately to an abstract Smith normal form, and to compute the resulting deterministic orbit data.

The calculation has a useful asymmetry. The sink breaks the exchange between the two parts. A chip added at a vertex opposite the sink generates a cycle of length $mn$, while a chip added beside the sink has period only $m$. For a general loading, the exact period is an elementary but nontrivial arithmetic function of the entire profile. Once that period is known, translation on a finite group forces a uniform cycle decomposition, and the zeta function and Koopman spectrum become closed formulas.

# Sandpile translations

Let $$A=\{a_1,\ldots,a_m\},\qquad
 B=\{b_1,\ldots,b_{n-1},q\}$$ be the two parts of $K_{m,n}$, with $q$ designated as the sink. We assume $m,n\geq2$. A stable sandpile has heights $0,\ldots,n-1$ on vertices of $A$ and $0,\ldots,m-1$ on nonsink vertices of $B$. When a nonsink reaches its degree, it topples one chip along every incident edge; chips reaching $q$ disappear. Stabilization is independent of toppling order.

Let $\mathcal R_{m,n}$ be the recurrent configurations. Stabilized componentwise addition makes $\mathcal R_{m,n}$ a group isomorphic to $$\mathbb Z^{m+n-1}/Q_{m,n}\mathbb Z^{m+n-1},$$ where, in the order $A,B\setminus\{q\}$, $$\label{eq:laplacian}
 Q_{m,n}=
 \begin{pmatrix}
 nI_m&-J_{m,n-1}\\
 -J_{n-1,m}&mI_{n-1}
 \end{pmatrix}.$$ The matrix-tree theorem gives $$\label{eq:tree-count}
 |\mathcal R_{m,n}|=\det Q_{m,n}=m^{n-1}n^{m-1}.$$

Let $$w=(\alpha_1,\ldots,\alpha_m,
       \beta_1,\ldots,\beta_{n-1})\in\mathbb Z^{m+n-1}.$$ For a nonnegative profile, $T_w$ adds the indicated chips and stabilizes. It is a permutation of $\mathcal R_{m,n}$. Integral profiles are then defined using inverse addition operators on the recurrent group. In the cokernel, $T_w$ is translation by $[w]$. Put $$A_w=\sum_{i=1}^{m}\alpha_i,
 \qquad B_w=\sum_{j=1}^{n-1}\beta_j.$$

For $N\geq1$ and $t\in\mathbb Z$, put $$d_N(t)=\frac{N}{\gcd(N,t)}.$$ Thus $d_N(0)=1$ and $d_N(t)$ is the reduced denominator of $t/N$.

# The localized period formula

[\[lem:denominator\]]{#lem:denominator label="lem:denominator"} If $Q$ is an invertible integer matrix and $w\in\mathbb Z^r$, then the order of $[w]$ in $\mathbb Z^r/Q\mathbb Z^r$ is the least positive integer $L$ for which $LQ^{-1}w\in\mathbb Z^r$. Equivalently, it is the least common multiple of the reduced denominators of the coordinates of $Q^{-1}w$.

The multiple $L[w]$ vanishes exactly when $Lw=Qz$ for some $z\in\mathbb Z^r$, which is equivalent to $LQ^{-1}w=z$ being integral.

For an arbitrary profile define $$\label{eq:general-period}
 \begin{split}
 L_{m,n}(w)=\operatorname{lcm}\Big(&
 \{d_{mn}((n-1)A_w+nB_w+m\alpha_i):1\leq i\leq m\},\\
 &\{d_m(A_w+B_w+\beta_j):1\leq j<n\}\Big).
 \end{split}$$

[\[thm:general-period\]]{#thm:general-period label="thm:general-period"} For every $m,n\geq2$ and $w\in\mathbb Z^{m+n-1}$, $$\operatorname{ord}(T_w)=L_{m,n}(w).$$ More explicitly, $$\begin{aligned}
 (Q_{m,n}^{-1}w)_{a_i}
 &=\frac{(n-1)A_w+nB_w+m\alpha_i}{mn},\label{eq:general-A}\\
 (Q_{m,n}^{-1}w)_{b_j}
 &=\frac{A_w+B_w+\beta_j}{m}.\label{eq:general-B}\end{aligned}$$

Write $u_i$ and $v_j$ for the coordinates of $Q_{m,n}^{-1}w$, and put $U=\sum_i u_i$, $V=\sum_jv_j$. The reduced-Laplacian equations are $$nu_i-V=\alpha_i,\qquad mv_j-U=\beta_j.$$ Summing the two families gives $$nU-mV=A_w,\qquad mV-(n-1)U=B_w.$$ Thus $U=A_w+B_w$ and $mV=(n-1)A_w+nB_w$. Substitution proves equations [\[eq:general-A\]](#eq:general-A){reference-type="eqref" reference="eq:general-A"} and [\[eq:general-B\]](#eq:general-B){reference-type="eqref" reference="eq:general-B"}. The order formula follows from [\[lem:denominator\]](#lem:denominator){reference-type="ref" reference="lem:denominator"}.

Fix $a=a_1$ and $b=b_1$, specialize to $w_{\alpha,\beta}=\alpha e_a+\beta e_b$, and write $T_{\alpha,\beta}=T_{w_{\alpha,\beta}}$. Define $$\begin{aligned}
 L_{m,n}(\alpha,\beta)
 =\operatorname{lcm}\big(&d_{mn}(\alpha(m+n-1)+\beta n),
 d_{mn}(\alpha(n-1)+\beta n),\notag\\
 &d_m(\alpha+2\beta),
 d_m(\alpha+\beta)\big),\label{eq:period}\end{aligned}$$ where the final term is omitted when $n=2$.

[\[cor:period\]]{#cor:period label="cor:period"} For every $m,n\geq2$ and $\alpha,\beta\in\mathbb Z$, $$\operatorname{ord}(T_{\alpha,\beta})=L_{m,n}(\alpha,\beta).$$ In particular, $$\operatorname{ord}(T_{1,0})=mn,\qquad \operatorname{ord}(T_{0,1})=m.$$

Specializing [\[thm:general-period\]](#thm:general-period){reference-type="ref" reference="thm:general-period"} gives the following coordinates at the distinguished vertex $a$ and at each other vertex of $A$, respectively: $$\label{eq:A-coordinates}
 \frac{\alpha(m+n-1)+\beta n}{mn},
 \qquad
 \frac{\alpha(n-1)+\beta n}{mn}.$$ At $b$ and at every other nonsink vertex of $B$, respectively, they are $$\label{eq:B-coordinates}
 \frac{\alpha+2\beta}{m},
 \qquad
 \frac{\alpha+\beta}{m}.$$ The second kind in [\[eq:B-coordinates\]](#eq:B-coordinates){reference-type="eqref" reference="eq:B-coordinates"} is absent when $b$ is the sole nonsink vertex of $B$. These reduced denominators prove [\[eq:period\]](#eq:period){reference-type="eqref" reference="eq:period"}.

For $(\alpha,\beta)=(0,1)$, the $A$ coordinates already have denominator $m$, and every displayed denominator divides $m$. Thus the order is $m$. For $(1,0)$, integrality of the difference between the two $A$ coordinates forces $n\mid L$, and the $B$ coordinates force $m\mid L$. If $g=\gcd(m,n)>1$, write any common multiple of $m,n$ as $L=(mn/g)t$. The other-$A$ coordinate after multiplication by $L$ is $t(n-1)/g$. Since $g\mid n$ and $\gcd(g,n-1)=1$, integrality forces $g\mid t$. Thus $mn\mid L$, and the least common multiple is $mn$.

The formula retains more information than the abstract decomposition $$K(K_{m,n})\cong(\mathbb Z/m\mathbb Z)^{n-2}\oplus
 (\mathbb Z/n\mathbb Z)^{m-2}\oplus\mathbb Z/(mn)\mathbb Z$$ because it locates the physical loading vector relative to a chosen sink and the vertex parts.

# Orbit census, zeta function, and spectrum

Put $M_{m,n}=m^{n-1}n^{m-1}$ and $L=L_{m,n}(w)$.

[\[thm:dynamics\]]{#thm:dynamics label="thm:dynamics"} The map $T_w$ partitions $\mathcal R_{m,n}$ into exactly $M_{m,n}/L$ cycles, all of length $L$. For every $k\geq1$, $$|\operatorname{Fix}(T_w^k)|=
 \begin{cases}
 M_{m,n},&L\mid k,\\
 0,&L\nmid k.
 \end{cases}$$ Its Artin--Mazur zeta function is $$\zeta_{T_w}(z)
 =\exp\left(\sum_{k\geq1}\frac{|\operatorname{Fix}(T_w^k)|}{k}z^k\right)
 =(1-z^L)^{-M_{m,n}/L}.$$

On the recurrent group, the map is translation by an element $g$ of order $L$. The orbit through any $x$ is the coset $x+\langle g\rangle$, so it has exactly $L$ points. The cosets partition the group. Translation by $kg$ has a fixed point exactly when $kg=0$, in which case it is the identity. The fixed-count formula follows, and $$\exp\left(\frac{M_{m,n}}L
       \sum_{j\geq1}\frac{z^{jL}}j\right)
 =(1-z^L)^{-M_{m,n}/L}$$ gives the zeta function.

[\[cor:spectrum\]]{#cor:spectrum label="cor:spectrum"} The ergodic invariant probability measures are precisely the uniform measures on the $M_{m,n}/L$ cycles. On $\ell^2(\mathcal R_{m,n})$ with counting measure, every $L$th root of unity is a Koopman eigenvalue with multiplicity $M_{m,n}/L$, and there are no other eigenvalues. The topological and measure-theoretic entropies are zero.

Each finite orbit supports one ergodic invariant measure, and every invariant measure is a convex combination of these. On each $L$-cycle the Koopman operator is the regular cyclic permutation, whose eigenvalues are the $L$th roots of unity, each once. Taking the direct sum over all cycles gives the multiplicities. A finite permutation has zero entropy.

For example, a single chip added opposite the sink has $$\zeta_{T_{1,0}}(z)
 =(1-z^{mn})^{-m^{n-2}n^{m-2}},$$ whereas a single chip added in the sink part has $$\zeta_{T_{0,1}}(z)
 =(1-z^{m})^{-m^{n-2}n^{m-1}}.$$

# Literal finite control and ownership boundary

The companion script carries out two independent checks. First, for $2\leq m,n\leq8$, it constructs $Q_{m,n}$, verifies its determinant, computes $Q_{m,n}^{-1}w$ over exact rationals for both two-site and arbitrary deterministic profiles, and compares all reduced denominators with equations [\[eq:general-period\]](#eq:general-period){reference-type="eqref" reference="eq:general-period"} and [\[eq:period\]](#eq:period){reference-type="eqref" reference="eq:period"}. Second, for every $2\leq m,n\leq4$, it enumerates stable configurations, applies Dhar's burning test, performs literal legal stabilization, and checks the predicted cycle length for four nonnegative loading vectors. These are regression controls, not replacements for the proof.

The sandpile group and addition-operator framework are owned by @Dhar1990 [@DharEtAl1995]; the bipartite critical group is due to @Lorenzini1991 and is reviewed in the multipartite treatment of @JacobsonEtAl2003; detailed $K_{m,n}$ configuration operators and cyclic combinatorics appear in @AvalEtAl2016; and @SeligZhu2025 is a current comparator on recurrent complete-bipartite sandpiles. Finite-group translation orbit facts are also not claimed. The residual statement here is only the sink-relative coordinate/order formula for physical loading profiles and its recorded dynamical consequences. A bounded search through 27 August 2026 found no exact collision with that combined package. This is not an absolute priority claim, and the manuscript remains on external-release hold.
