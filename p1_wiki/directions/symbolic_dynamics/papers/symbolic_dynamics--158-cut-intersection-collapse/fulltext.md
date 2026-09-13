---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--158-cut-intersection-collapse"
canonical_tex: "symbolic_dynamics/papers/158-cut-intersection-collapse/main.tex"
canonical_pdf: "symbolic_dynamics/papers/158-cut-intersection-collapse/main.pdf"
source_sha256: "31eb5758fb9ba5d2be985a9e4fbffa7a2cfbd4b3515457f6c6220e42bb78fb8f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Complementary Histories in Repeated Cut Intersections: Exact Absorption and Labelled Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/158-cut-intersection-collapse>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/158-cut-intersection-collapse/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/158-cut-intersection-collapse/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/158-cut-intersection-collapse/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/158-cut-intersection-collapse/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Starting from the labelled complete graph, intersect the current edge set at each epoch with an independent fair vertex cut. After $t$ epochs, two vertices remain adjacent exactly when their binary histories are bitwise complements. We use this pathwise representation to determine the absorption law at every time and, more strongly, the complete fibre of every labelled target graph. If $R=2^{t-1}$, $r$ is the number of nontrivial complete bipartite components, and $z$ is the number of isolates, the fibre is $(R)_r2^r A_{R-r}(z)$, where $A_R(z)=z![x^z](2e^x-1)^R$. The formula includes a necessary boundary often lost in a component-only description: when $r=R$, any isolate forces the fibre to vanish. We also obtain the labelled image exponential generating function, first-hit probabilities, an exact mean series, and a geometric tail certificate. Cuts, bicluster graphs, random-intersection terminology, and inclusion--exclusion receive no contribution credit. A deterministic audit performs $77{,}530$ exact assertions as counterexample pressure, not as proof or source clearance.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Complementary Histories in Repeated Cut Intersections:\
  Exact Absorption and Labelled Fibres
```

## Markdown 正文

# The process and the theorem {#sec:setup}

Fix a labelled vertex set $[n]$, with $n\geq2$, and put $G_0=K_n$. At epoch $s\geq1$, assign independent fair bits $b_s(v)$ to all vertices. Let $C_s$ contain $uv$ precisely when $b_s(u)\ne b_s(v)$, and set $$\label{eq:update}
 G_s=G_{s-1}\cap C_s,
 \qquad
 T=\min\{s\geq1:E(G_s)=\varnothing\}.$$ Thus time counts sampled cuts, including cuts that remove no surviving edge.

The ingredients around [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} are standard and are not claimed. Erdős and Pyber study complete-bipartite graph coverings [@ErdosPyber1997]; Guo--Hüffner--Komusiewicz--Zhang treat disjoint unions of complete bipartite graphs as the bicluster target class [@GuoHuffnerKomusiewiczZhang2008]; and Zhao--Yağan--Gligor study random intersection graphs generated from random item assignments [@ZhaoYaganGligor2015]. The last model creates edges from shared items, whereas [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} retains an edge only under exact complementarity of all history bits. These sources subtract the graph-class and random-label neighbourhoods; they do not certify novelty or ownership completeness. Our scope is only the following finite, labelled process-and-fibre conjunction.

For $t\geq1$, put $R=2^{t-1}$ and define $$\label{eq:A}
 A_R(m)=\sum_{j=0}^{R}(-1)^{R-j}\binom Rj2^j j^m
       =m![x^m](2e^x-1)^R.$$ We use the exact boundary conventions $$\label{eq:A-boundary}
 A_0(0)=1,\qquad A_0(m)=0\ (m>0),\qquad A_R(0)=1.$$ If every nontrivial component of a labelled graph $H$ is complete bipartite, write $r(H)$ for the number of these components and $z(H)$ for the number of isolated vertices. As usual, $(R)_r=R(R-1)\cdots(R-r+1)$.

[\[thm:main\]]{#thm:main label="thm:main"} For every $n\geq2$ and $t\geq1$, with $R=2^{t-1}$:

1.  The absorption distribution is $$\label{eq:cdf}
     \mathbb P(T\leq t)=\frac{A_R(n)}{2^{tn}}.$$ Writing $F_0=0$ and $F_t=A_{2^{t-1}}(n)/2^{tn}$ gives $\mathbb P(T=t)=F_t-F_{t-1}$. Moreover, $$\label{eq:tail-mean}
     \mathbb P(T>t)\leq\binom n2 2^{-t},\qquad
     \mathbb ET=1+\sum_{t\geq1}(1-F_t)\leq1+\binom n2.$$

2.  A graph $H$ has a positive time-$t$ fibre if and only if every nontrivial component is complete bipartite, $$\label{eq:image-condition}
     r(H)\leq R,
     \qquad
     z(H)=0\ \text{or}\ r(H)<R.$$ If every nontrivial component is complete bipartite and $r(H)\leq R$, its fibre is $$\label{eq:fibre}
     \#\{(b_s(v)):G_t=H\}
       =(R)_{r(H)}2^{r(H)}A_{R-r(H)}(z(H)).$$ Formula [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} remains valid with value zero when $r(H)=R$ and $z(H)>0$; graphs with $r(H)>R$ or outside the component class have fibre zero. Division by $2^{tn}$ gives the complete time-$t$ law.

3.  With $$\label{eq:B}
     B(x)=\frac{(e^x-1)^2}{2},$$ the labelled image size is $$\label{eq:image-egf}
     |\operatorname{im}(G_t)|
     =n![x^n]\left[
     e^x\sum_{j=0}^{R-1}\frac{B(x)^j}{j!}
     +\frac{B(x)^R}{R!}\right].$$

The two axes are deliberately stated together. The absorption formula resolves only the empty target, while [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} resolves every labelled target and its zero fibres.

[\[rem:boundary\]]{#rem:boundary label="rem:boundary"} Take $n=5$ and $t=2$, so $R=2$. A graph made of two disjoint edges and one isolate has $r=R=2$ and $z=1$, but $$(2)_2\,2^2A_0(1)=0.$$ It is therefore not attainable. The shorthand "a union of at most $R$ complete bipartite components and isolates" is false without the second condition in [\[eq:image-condition\]](#eq:image-condition){reference-type="eqref" reference="eq:image-condition"}.

# Complement histories and absorption {#sec:history}

For each vertex, collect its first $t$ bits into $$c_t(v)=(b_1(v),\ldots,b_t(v))\in\{0,1\}^t.$$ The $2^t$ words form $R$ unordered pairs $\{w,\overline{w}\}$.

[\[lem:complement\]]{#lem:complement label="lem:complement"} For distinct vertices $u,v$, $$\label{eq:complement}
 uv\in E(G_t)\quad\Longleftrightarrow\quad
 c_t(u)=\overline{c_t(v)}.$$ For $m$ labelled vertices, the number of word assignments that occupy at most one side of every complementary pair is $A_R(m)$.

The edge $uv$ survives precisely when $b_s(u)\ne b_s(v)$ for every $s\leq t$. Over the binary alphabet, coordinatewise inequality is bitwise complementation, proving [\[eq:complement\]](#eq:complement){reference-type="eqref" reference="eq:complement"}. The passage from all cut bits to vertex words is bijective and retains all $tn$ labelled coordinates.

For one complementary pair, an admissible inverse image is empty, a nonempty labelled set using its first word, or a nonempty labelled set using its second word. Its labelled exponential generating function is $1+2(e^x-1)=2e^x-1$. The $R$ pairs are distinguished, so multiplication and coefficient extraction give the second expression in [\[eq:A\]](#eq:A){reference-type="eqref" reference="eq:A"}. Expanding the $R$th power gives the finite sum there and also proves all conventions in [\[eq:A-boundary\]](#eq:A-boundary){reference-type="eqref" reference="eq:A-boundary"}.

The graph is empty at time $t$ exactly when every complementary pair is occupied on at most one side. Lemma [\[lem:complement\]](#lem:complement){reference-type="ref" reference="lem:complement"} counts $A_R(n)$ successful assignments among the $2^{tn}$ equally likely histories, giving [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"}. Since the edge sets decrease, $\{T\leq t\}=\{G_t=\varnothing\}$, and CDF differences give the first-hit law.

For a fixed edge, choose the first history word freely; the second has one successful word among $2^t$, so its survival probability is $2^{-t}$. A union bound over the $\binom n2$ edges proves the tail inequality. It tends to zero, hence $T$ is almost surely finite. The tail-sum identity for a positive integer-valued random variable and the geometric series prove the remaining statements in [\[eq:tail-mean\]](#eq:tail-mean){reference-type="eqref" reference="eq:tail-mean"}.

# The labelled fibre atlas {#sec:fibres}

Fix a complementary pair $\{w,\overline{w}\}$. Equation [\[eq:complement\]](#eq:complement){reference-type="eqref" reference="eq:complement"} puts every possible edge between the vertices using $w$ and those using $\overline{w}$, and no edge within either side. If both sides are nonempty they form one connected complete bipartite component; if only one is occupied, all its vertices are isolated. Different word pairs have no edges between them.

Thus every nontrivial component of an image is complete bipartite. Two such components cannot use the same word pair: all cross edges between opposite sides would join them. Hence $r(H)\leq R$. If all $R$ pairs are consumed by components, an extra isolate has no legal word, because either word in a consumed pair joins it to the nonempty opposite side. This proves necessity of [\[eq:image-condition\]](#eq:image-condition){reference-type="eqref" reference="eq:image-condition"}.

Conversely, suppose $H$ satisfies the stated conditions and put $r=r(H)$, $z=z(H)$. A connected bipartite graph has a unique bipartition up to swapping its two sides. Injectively assigning the $r$ components to complementary pairs gives $(R)_r$ choices, and orienting every bipartition inside its assigned pair gives $2^r$ choices. No isolate can use a consumed pair. On the $R-r$ unused pairs, isolates must avoid occupying both sides, or two of them would form an edge. Lemma [\[lem:complement\]](#lem:complement){reference-type="ref" reference="lem:complement"} gives exactly $A_{R-r}(z)$ assignments.

Each assignment constructed this way yields $H$. In the reverse direction, the history assignment uniquely recovers the component-pair injection, orientations, and residual isolate assignment. Multiplication proves [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}; [\[eq:A-boundary\]](#eq:A-boundary){reference-type="eqref" reference="eq:A-boundary"} gives the claimed zero boundary. Necessity already proves zero fibres outside the component class.

On a labelled set of size $s\geq2$, a nontrivial complete bipartite graph is specified by a nonempty proper subset modulo complementation. There are $2^{s-1}-1$ choices, whose labelled EGF is $B(x)$ from [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"}. An unordered set of exactly $j$ such components has EGF $B(x)^j/j!$.

When $j<R$, an arbitrary labelled set of isolates is allowed and contributes $e^x$. When $j=R$, the resource boundary forces the isolate set to be empty. The two disjoint cases give the bracket in [\[eq:image-egf\]](#eq:image-egf){reference-type="eqref" reference="eq:image-egf"}, and labelled coefficient extraction completes the proof.

The finite formula [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} also explains why a static component classification is insufficient: it retains the time resource $R$, the orientation of every labelled component, and the one-sided occupancy of all remaining histories.

# Exact controls, scope, and declarations {#sec:audit}

A standard-library verifier enumerates every word assignment and, independently, every labelled simple target in the frozen boxes. For every history it computes the successive cut intersections and separately computes the complement-word graph, then compares them before accumulating fibres. It compares all observed and predicted fibres, including zero fibres, checks the empty target against [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"}, verifies an independent labelled image count, checks the first edge moment, and tests temporal monotonicity and the tail bound. Representative boxes are shown in Table [1](#tab:audit){reference-type="ref" reference="tab:audit"}.

::: {#tab:audit}
    $n$   $t$   histories   image   empty fibre
  ----- ----- ----------- ------- -------------
      2     1           4       2             2
      3     1           8       4             2
      4     2         256      29            60
      4     3       4,096      29         1,880
      5     2       1,024     121           124
      5     3      32,768     136         9,368
      6     2       4,096     497           252

  : Exact finite falsification. "Empty" is the fibre of the empty graph; enumeration is not an all-parameter proof.
:::

The complete audit executes $77{,}530$ integer assertions. Its canonical transcript has SHA-256 (the following two lines concatenate):

`3e69dfb7d0653c140f2945a6fe4888afc`\
`569756a25acf20c1e7eaf2d9f432f0d`.

This evidence is counterexample pressure only. It does not prove the theorem, exhaust alternate terminology, establish novelty or priority, or authorize release.

# Limitations {#limitations .unnumbered}

The theorem requires independent fair cuts, starts from the labelled complete graph, and counts full cut histories rather than quotienting by graph automorphisms. It does not cover biased or correlated cuts, arbitrary starting graphs, unlabelled fibres, or asymptotic limit laws. Complete bipartite components, bicluster terminology, labelled exponential generating functions, and inclusion--exclusion are owned background. The source screen was bounded; a direct owner under different terminology would require the claim boundary to be reopened.

# Data Availability {#data-availability .unnumbered}

No external data were used. The paper-local verifier and frozen transcript contain the complete deterministic exact control.

# Ethics Statement {#ethics-statement .unnumbered}

This mathematical study involved no human participants, animals, personal data, or field intervention.

# Author Contributions {#author-contributions .unnumbered}

The anonymous author performed the derivation, proof, exact checks, source-boundary audit, and manuscript preparation.

# Conflict of Interest {#conflict-of-interest .unnumbered}

The author declares no conflict of interest.

# Funding {#funding .unnumbered}

No external funding is declared.

# External Status {#external-status .unnumbered}

This artifact remains `HOLD_EXTERNAL`; it is not cleared for posting, submission, circulation, or author contact.
