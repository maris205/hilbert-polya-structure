---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--77-digit-weight-automatic-towers"
canonical_tex: "symbolic_dynamics/papers/77-digit-weight-automatic-towers/main.tex"
canonical_pdf: "symbolic_dynamics/papers/77-digit-weight-automatic-towers/main.pdf"
source_sha256: "89d4c764d5de6533498c3e0d12e941e872b3999a8b8333a4f7eb58235ca2b973"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Digit-Weight Automatic Towers: Cantor--Bendixson Layers, Nilpotent Cellular Automata, and Conjugacy Rigidity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/77-digit-weight-automatic-towers>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/77-digit-weight-automatic-towers/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/77-digit-weight-automatic-towers/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/77-digit-weight-automatic-towers/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/77-digit-weight-automatic-towers/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix integers $q\geq2$ and $d\geq1$, and mark the nonnegative integers whose base-$q$ expansion has exactly $d$ digits equal to $1$ and every other digit equal to $0$. We determine the two-sided orbit closure of this indicator sequence. It is a countable transitive subshift consisting of one fixed point and exactly $d+1$ free shift orbits, indexed by the number of retained digits. Its Cantor--Bendixson derivatives delete these orbits one at a time, and its height is $d+2$. Centered limits define continuous lowering cellular automata $D_r$. They generate, together with the shift, the full endomorphism monoid: $$\operatorname{End}(X_{q,d})=\{\mathbf 0\}\cup
   \{\sigma^aD_r:a\in\mathbb Z,\ 0\leq r\leq d\},$$ with truncated-addition composition and an absorbing zero. Consequently $\operatorname{Aut}(X_{q,d})\cong\mathbb Z$. We also prove arithmetic rigidity: $X_{q,d}$ and $X_{p,e}$ are conjugate exactly when $(q,d)=(p,e)$. The only invariant probability is the point mass at the zero configuration, and the entropy is zero. The exponential-support case $d=1$ is treated as an owned base case; the residual contribution is the exact package for $d\geq2$.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal preprint, 27 August 2026'
title: |
  Digit-Weight Automatic Towers:\
  Cantor--Bendixson Layers, Nilpotent Cellular Automata, and Conjugacy Rigidity
```

## Markdown 正文

# Introduction

For $q\geq2$ and $d\geq1$, let $$S_{q,d}=\left\{\sum_{i\in A}q^i:
 A\subseteq\mathbb N_0,\ |A|=d\right\}.$$ Thus $S_{q,d}$ consists of integers whose base-$q$ expansion has exactly $d$ unit digits and no other nonzero digits. Its indicator is $q$-automatic: a finite automaton rejects digits outside $\{0,1\}$ and counts unit digits up to $d$. This is a direct instance of the classical automatic-sequence framework initiated by Cobham [@Cobham1972]. Sparse automatic supports and their polylogarithmic growth have a substantial general theory; a recent graph-theoretic account and precise ownership map are given by Wessel [@Wessel2025].

We study a different invariant: the complete two-sided orbit closure of the indicator, including its topology and every continuous shift-commuting self-map. The answer is a finite tower of countably infinite orbits. A bounded difference of two fixed-cardinality sums of $q$-powers forces their escaping exponent sets to agree. This arithmetic rigidity classifies every centered limit, including the binary case where an informal "no carry" argument would be insufficient. The same classification makes the natural layer-lowering maps continuous.

The endomorphism calculation is then forced by transitivity. An endomorphism is determined by the image of the generating point. Every possible image is realized by a shift followed by a lowering map, and the lowering maps form a nilpotent chain. The return scales from the top layer to the next layer are the powers of $q$; requiring these scales in both directions under a conjugacy recovers the base itself, including when the two bases are powers of a common integer.

The case $d=1$ is not claimed as a new system. Gheorghiciuc treats the exact exponential occurrence function $G(n)=q^{n-1}$ and its word complexity [@Gheorghiciuc2007]. Salo and Törmä explicitly use the binary powers-of-two orbit closure, with a slightly different initial-index convention, as a one-dimensional gadget [@SaloTorma2012]. General automatic points in automatic systems and under factor maps are now characterized through quasi-fixed points [@Krawczyk2026]. We retain $d=1$ in all theorem statements because it is the first level of the same proof, but our novelty claims concern $d\geq2$.

The precise residual package is:

1.  the exact orbit decomposition and Cantor--Bendixson tower;

2.  continuous lowering cellular automata and the full endomorphism monoid, not merely the automorphism group;

3.  conjugacy rigidity in both parameters $(q,d)$;

4.  the complete periodic-point and invariant-measure description.

A bounded primary-source search through 27 August 2026, covering the exact defining equation, fixed-digit-weight automatic sets, powers-of-two orbit closures, countable automatic systems, and endomorphism calculations, found no source stating this combined $d\geq2$ package. This is a bounded search report, not a claim of absolute priority.

# Setup and the main theorem

Write $\mathbb N_0=\{0,1,2,\ldots\}$. For a finite set $A\subseteq\mathbb N_0$, put $$P_q(A)=\sum_{i\in A}q^i.$$ The map $P_q$ is injective because its values have base-$q$ digits in $\{0,1\}$. Set $S_{q,0}=\{0\}$ and define $x_{q,s}\in\{0,1\}^{\mathbb Z}$ by $$x_{q,s}(n)=\begin{cases}
 1,&n\in S_{q,s},\\
 0,&n\notin S_{q,s}.
 \end{cases}$$ In particular, $x_{q,0}$ is the single marker at the origin. We use the left shift $$(\sigma^a x)(n)=x(n+a),
 \qquad \operatorname{supp}(\sigma^a x)=\operatorname{supp}(x)-a.$$ Let $$X_{q,d}=\overline{\{\sigma^a x_{q,d}:a\in\mathbb Z\}},
 \qquad
 \mathcal O_s=\{\sigma^a x_{q,s}:a\in\mathbb Z\}.$$ The symbol $0^{\mathbb Z}$ denotes the all-zero configuration. We reserve $\mathbf 0$ for the constant map with value $0^{\mathbb Z}$.

By an endomorphism we mean a continuous map $F:X_{q,d}\to X_{q,d}$ satisfying $F\sigma=\sigma F$; surjectivity is not part of the definition. Hedlund's theorem [@Hedlund1969] identifies these maps with sliding block codes on the subshift.

[\[thm:main\]]{#thm:main label="thm:main"} For $q\geq2$ and $d\geq1$, the following hold.

1.  The orbit decomposition is the disjoint union $$\label{eq:orbit-decomposition}
     X_{q,d}=\{0^{\mathbb Z}\}\sqcup\bigsqcup_{s=0}^{d}\mathcal O_s.$$

2.  For $0\leq j\leq d$, $$\label{eq:derivatives}
     X_{q,d}^{(j)}=\{0^{\mathbb Z}\}\cup
     \bigcup_{s=0}^{d-j}\mathcal O_s,$$ while $X_{q,d}^{(d+1)}=\{0^{\mathbb Z}\}$ and $X_{q,d}^{(d+2)}=\varnothing$. Hence the Cantor--Bendixson height is $d+2$.

3.  There are continuous lowering maps $D_r$, $0\leq r\leq d$, such that $$\label{eq:lowering-definition}
     D_r(0^{\mathbb Z})=0^{\mathbb Z},
     \qquad
     D_r(\sigma^a x_{q,s})=
     \begin{cases}
     \sigma^a x_{q,s-r},&s\geq r,\\
     0^{\mathbb Z},&s<r.
     \end{cases}$$ They satisfy $D_0=\mathrm{id}$ and $$\label{eq:lowering-composition}
     D_rD_t=
     \begin{cases}
     D_{r+t},&r+t\leq d,\\
     \mathbf 0,&r+t>d.
     \end{cases}$$

4.  The full endomorphism monoid is $$\label{eq:end-monoid}
     \operatorname{End}(X_{q,d})=\{\mathbf 0\}\cup
     \{\sigma^aD_r:a\in\mathbb Z,\ 0\leq r\leq d\}.$$ Its multiplication is $$\label{eq:end-multiplication}
     (\sigma^aD_r)(\sigma^bD_t)=
     \begin{cases}
     \sigma^{a+b}D_{r+t},&r+t\leq d,\\
     \mathbf 0,&r+t>d.
     \end{cases}$$ Consequently $\operatorname{Aut}(X_{q,d})=\langle\sigma\rangle\cong\mathbb Z$.

5.  If $p\geq2$ and $e\geq1$, then $$\label{eq:conjugacy-rigidity}
     (X_{q,d},\sigma)\cong(X_{p,e},\sigma)
     \quad\Longleftrightarrow\quad (q,d)=(p,e).$$

6.  The only periodic point is $0^{\mathbb Z}$, the unique invariant Borel probability is $\delta_{0^{\mathbb Z}}$, and $h_{\mathrm{top}}(X_{q,d})=0$.

The restriction $d,e\geq1$ in the rigidity statement is necessary. At $d=0$, the orbit closure of the single marker is independent of $q$.

# Bounded differences of digital sums

The following lemma is the arithmetic engine of every limit argument below.

[\[lem:bounded-difference\]]{#lem:bounded-difference label="lem:bounded-difference"} Fix $q\geq2$ and $M\geq0$. Let $(A_j)$ and $(B_j)$ be sequences of finite subsets of $\mathbb N_0$ with $|A_j|,|B_j|\leq M$. Suppose that $$|P_q(A_j)-P_q(B_j)|\leq C$$ for a constant $C$ independent of $j$. After passing to a subsequence, there are fixed finite sets $A,B\subseteq\mathbb N_0$ and finite sets $E_j$ such that $$\label{eq:common-escape}
 A_j=A\sqcup E_j,
 \qquad B_j=B\sqcup E_j,
 \qquad \min E_j\longrightarrow\infty,$$ where the last condition is vacuous when $E_j$ is empty.

The indicator functions of subsets of $\mathbb N_0$ lie in the compact product space $\{0,1\}^{\mathbb N_0}$. A diagonal extraction makes membership of every fixed exponent eventually constant in both sequences. Let $A$ and $B$ be the respective pointwise limits. They are finite and have cardinality at most $M$: otherwise $M+1$ distinct exponents would eventually belong to one of the approximating sets.

After discarding finitely many indices, write $$A_j=A\sqcup A'_j,
 \qquad B_j=B\sqcup B'_j,$$ where the least exponent in $A'_j\cup B'_j$ tends to infinity whenever that union is nonempty. Remove the common part $E_j=A'_j\cap B'_j$, and put $$U_j=A'_j\setminus E_j,
 \qquad V_j=B'_j\setminus E_j.$$ The sets $U_j$ and $V_j$ are disjoint. Moreover, $$|P_q(U_j)-P_q(V_j)|
 \leq C+P_q(A)+P_q(B)=:C'.$$ If $U_j\cup V_j$ is nonempty, let $m_j$ be its least exponent. Then $P_q(U_j)-P_q(V_j)$ is divisible by $q^{m_j}$. For large $j$, one has $q^{m_j}>C'$, so this difference must be zero. Injectivity of $P_q$ gives $U_j=V_j$; disjointness then forces both sets to be empty. Thus $A'_j=B'_j=E_j$ for all sufficiently large $j$, proving [\[eq:common-escape\]](#eq:common-escape){reference-type="eqref" reference="eq:common-escape"}.

The proof uses divisibility only after every stable low exponent has been removed. It therefore covers $q=2$ without assuming that subtraction is carry-free.

# Centered limits and orbit decomposition

[\[prop:centered-limits\]]{#prop:centered-limits label="prop:centered-limits"} Fix $0\leq s\leq d$. Suppose $$\sigma^{n_j}x_{q,s}\longrightarrow y\neq0^{\mathbb Z}.$$ After passing to a subsequence, there exist $t\in\{0,\ldots,s\}$, an integer $a$, and sets $E_j\subseteq\mathbb N_0$ such that $$\label{eq:center-normal-form}
 |E_j|=s-t,
 \qquad \min E_j\longrightarrow\infty,
 \qquad n_j=a+P_q(E_j),$$ and $$\label{eq:center-limit}
 y=\sigma^a x_{q,t}.$$ Conversely, every sequence satisfying [\[eq:center-normal-form\]](#eq:center-normal-form){reference-type="eqref" reference="eq:center-normal-form"} converges as in [\[eq:center-limit\]](#eq:center-limit){reference-type="eqref" reference="eq:center-limit"}.

Choose $k_0\in\mathbb Z$ with $y(k_0)=1$. Coordinatewise convergence in the discrete alphabet implies that, for all sufficiently large $j$, $$n_j+k_0=P_q(A_j)$$ for a unique $s$-element set $A_j$. Pass to a subsequence on which the membership of every fixed exponent stabilizes. There is then a fixed finite set $B$ and sets $E_j$ whose least exponents tend to infinity such that $$A_j=B\sqcup E_j.$$ After one further extraction, $|E_j|$ is constant. Put $t=|B|$ and $a=P_q(B)-k_0$. This gives [\[eq:center-normal-form\]](#eq:center-normal-form){reference-type="eqref" reference="eq:center-normal-form"}.

We identify the support of $y$. If $a+k=P_q(C)$ for a $t$-element set $C$, then $C\cap E_j=\varnothing$ for large $j$, and $$n_j+k=P_q(E_j\sqcup C)\in S_{q,s}.$$ Hence $y(k)=1$. Conversely, suppose $y(k)=1$. For large $j$ there are $s$-element sets $C_j$ satisfying $$P_q(C_j)=n_j+k,
 \qquad
 P_q(C_j)-P_q(A_j)=k-k_0.$$ Apply [\[lem:bounded-difference\]](#lem:bounded-difference){reference-type="ref" reference="lem:bounded-difference"} to $(C_j)$ and $(A_j)$. The stable part of $(A_j)$ is $B$, so the lemma gives a fixed $t$-element set $C$ and, after relabelling the common escaping part, $C_j=C\sqcup E_j$. Therefore $$P_q(C)-P_q(B)=k-k_0,
 \qquad P_q(C)=a+k.$$ We have proved $$y(k)=1\quad\Longleftrightarrow\quad a+k\in S_{q,t},$$ which is exactly $y=\sigma^a x_{q,t}$.

For the converse, assume [\[eq:center-normal-form\]](#eq:center-normal-form){reference-type="eqref" reference="eq:center-normal-form"}. If $a+k\in S_{q,t}$, adjoining its unique $t$ exponents to $E_j$ proves that $n_j+k\in S_{q,s}$ for large $j$. If $n_j+k\in S_{q,s}$ along an infinite subsequence, compare the representing $s$-element sets with $E_j$ by [\[lem:bounded-difference\]](#lem:bounded-difference){reference-type="ref" reference="lem:bounded-difference"}; it follows that $a+k\in S_{q,t}$. Thus every coordinate converges to that of $\sigma^a x_{q,t}$.

Every nonzero limit of shifts of $x_{q,d}$ belongs to one of the displayed orbits by [\[prop:centered-limits\]](#prop:centered-limits){reference-type="ref" reference="prop:centered-limits"}. The zero configuration also occurs: $\sigma^{-j}x_{q,d}\to0^{\mathbb Z}$ as $j\to\infty$, since the support of $x_{q,d}$ is contained in $\mathbb N_0$. Conversely, for $0\leq t\leq d$, choose $(d-t)$-element sets $E_j$ whose least exponent tends to infinity. gives $$\sigma^{P_q(E_j)}x_{q,d}\longrightarrow x_{q,t},$$ and shifting this convergence produces every point of $\mathcal O_t$.

It remains to verify disjointness. Every nonzero point in $\mathcal O_t$ has counting function $$\#\bigl(\operatorname{supp}(x)\cap[-N,N]\bigr)=\Theta((\log N)^t)$$ for $t\geq1$, while points of $\mathcal O_0$ have singleton support. Translation does not change the exponent of this polylogarithmic growth, so different layers cannot meet. Indeed, the upper bound follows because every exponent in a representation of a point of $S_{q,t}\cap[0,N]$ is at most $\lfloor\log_q N\rfloor$, while the lower bound follows by choosing all $t$ exponents below $\lfloor\log_q(N/t)\rfloor$; injectivity of $P_q$ makes these choices distinct. Within one layer, a nonzero period would make a nonempty support that is bounded below invariant under a nonzero translation, which is impossible. Thus every $\mathcal O_t$ is a free orbit.

# The Cantor--Bendixson tower

Let $$Y_s=\{0^{\mathbb Z}\}\cup\bigcup_{t=0}^{s}\mathcal O_t,
 \qquad 0\leq s\leq d.$$

[\[lem:one-orbit\]]{#lem:one-orbit label="lem:one-orbit"} For $s\geq1$, the derived set of $Y_s$ is $Y_{s-1}$, while the derived set of $Y_0$ is $\{0^{\mathbb Z}\}$ and the derived set of $\{0^{\mathbb Z}\}$ is empty.

Every point $\sigma^a x_{q,t}$ with $t<s$ is approached by points of $\mathcal O_s$: choose $(s-t)$-element escaping sets $E_j$ and use $$\sigma^{a+P_q(E_j)}x_{q,s}\longrightarrow\sigma^a x_{q,t}.$$ The zero configuration is an accumulation point of every $Y_s$: for $s=0$, translate the single marker to infinity; for $s\geq1$, use $\sigma^{-j}x_{q,s}\to0^{\mathbb Z}$.

We show that every point of $\mathcal O_s$ is isolated in $Y_s$. Otherwise a sequence of distinct points of $Y_s$ would converge to a point of $\mathcal O_s$. After taking a subsequence, all points lie in one layer $\mathcal O_t$, $t\leq s$. If their shift parameters are unbounded, [\[prop:centered-limits\]](#prop:centered-limits){reference-type="ref" reference="prop:centered-limits"} says that every nonzero limit belongs to a layer of index strictly below $t$. It therefore cannot lie in $\mathcal O_s$. If the parameters are bounded, a subsequence is constant; freeness of the orbit then contradicts distinctness. This proves $(Y_s)'=Y_{s-1}$.

The same argument for $Y_0$ says that all single-marker points are isolated and their shifts accumulate only at $0^{\mathbb Z}$. Finally, the singleton $\{0^{\mathbb Z}\}$ has empty derived set.

Since $X_{q,d}=Y_d$, iterating [\[lem:one-orbit\]](#lem:one-orbit){reference-type="ref" reference="lem:one-orbit"} gives [\[eq:derivatives\]](#eq:derivatives){reference-type="eqref" reference="eq:derivatives"}, followed by $\{0^{\mathbb Z}\}$ and then the empty set. In the convention where the height is the least ordinal with empty derivative, the height is $d+2$. Equivalently, it is the least stable derivative index. The point rank of every member of $\mathcal O_s$ is $d-s$, and the point rank of $0^{\mathbb Z}$ is $d+1$.

For example, when $d=1$ the derivative chain is $$X_{q,1}\supset \mathcal O_0\cup\{0^{\mathbb Z}\}
 \supset\{0^{\mathbb Z}\}\supset\varnothing.$$ This makes the otherwise easy off-by-one error visible.

# Lowering maps and their continuity

The orbit decomposition makes [\[eq:lowering-definition\]](#eq:lowering-definition){reference-type="eqref" reference="eq:lowering-definition"} a well-defined set map. Shift commutation is immediate. Its continuity is the nonlocal point of the construction.

[\[prop:lowering-continuity\]]{#prop:lowering-continuity label="prop:lowering-continuity"} For each $0\leq r\leq d$, the map $D_r$ in [\[eq:lowering-definition\]](#eq:lowering-definition){reference-type="eqref" reference="eq:lowering-definition"} is continuous. Hence it is a cellular automaton on $X_{q,d}$.

Because $X_{q,d}$ is compact metrizable, it suffices to prove sequential continuity. Let $y_j\to y$. There are only finitely many layers, so every subsequence has a further subsequence which either consists entirely of $0^{\mathbb Z}$ or lies in a fixed nonzero layer. The former case is immediate. In the latter case, write $$y_j=\sigma^{n_j}x_{q,s}.$$ We prove that its $D_r$-images have a further subsequence converging to $D_r(y)$. This subsequence criterion implies convergence of the full image sequence.

First suppose $y=\sigma^a x_{q,t}$ is nonzero. By [\[prop:centered-limits\]](#prop:centered-limits){reference-type="ref" reference="prop:centered-limits"}, after a further extraction the centers have the form $$n_j=a+P_q(E_j),
 \qquad |E_j|=s-t,
 \qquad \min E_j\to\infty.$$ If $s<r$, then $t\leq s<r$ and both $D_r(y_j)$ and $D_r(y)$ are zero. Assume $s\geq r$. If $t\geq r$, then $$D_r(y_j)=\sigma^{n_j}x_{q,s-r}
 \longrightarrow \sigma^a x_{q,t-r}=D_r(y)$$ by the converse half of [\[prop:centered-limits\]](#prop:centered-limits){reference-type="ref" reference="prop:centered-limits"}.

If $t<r$, we claim that $D_r(y_j)\to0^{\mathbb Z}$. Were there a nonzero sublimit, [\[prop:centered-limits\]](#prop:centered-limits){reference-type="ref" reference="prop:centered-limits"} would express the same centers as $$n_j=b+P_q(F_j),
 \qquad |F_j|\leq s-r,
 \qquad \min F_j\to\infty.$$ The difference $P_q(E_j)-P_q(F_j)=b-a$ is bounded. Applying [\[lem:bounded-difference\]](#lem:bounded-difference){reference-type="ref" reference="lem:bounded-difference"} to the two escaping families forces $|E_j|=|F_j|$ eventually. This is impossible because $$|E_j|=s-t>s-r\geq|F_j|.$$ Thus the only sublimit is $0^{\mathbb Z}=D_r(y)$.

It remains to consider $y=0^{\mathbb Z}$. If $D_r(y_j)$ had a nonzero sublimit, then necessarily $s\geq r$ (the case $s<r$ is identically zero), and the same normal form would give $$n_j=b+P_q(F_j),
 \qquad |F_j|=h\leq s-r$$ after a further extraction. The sets $F_j$ escape to infinity. Applying the converse part of [\[prop:centered-limits\]](#prop:centered-limits){reference-type="ref" reference="prop:centered-limits"} to the original layer $s$ would then give the nonzero limit $\sigma^b x_{q,s-h}$, where $s-h\geq r$, contradicting $y_j\to0^{\mathbb Z}$. Therefore $D_r(y_j)\to0^{\mathbb Z}$.

The map is continuous and commutes with $\sigma$. Hedlund's theorem now supplies a finite-radius local rule, so $D_r$ is a cellular automaton.

Only the composition law remains. On a layer $\mathcal O_s$, applying $D_t$ and then $D_r$ lowers the index by $r+t$ when $s\geq r+t$ and gives $0^{\mathbb Z}$ otherwise. This is $D_{r+t}$ when $r+t\leq d$. If $r+t>d$, every layer is sent to $0^{\mathbb Z}$, so the composite is $\mathbf 0$.

In particular, $D_1^{d+1}=\mathbf 0$. The law is truncation to an absorbing zero, not saturation at the bottom nonzero layer.

# The full endomorphism monoid

The orbit of $x_{q,d}$ is dense in $X_{q,d}$. Consequently two continuous shift-commuting maps that agree on $x_{q,d}$ agree on its orbit and hence on all of $X_{q,d}$.

Let $F\in\operatorname{End}(X_{q,d})$. If $F(x_{q,d})=0^{\mathbb Z}$, then $F(\sigma^a x_{q,d})=0^{\mathbb Z}$ for every $a$, so continuity and density give $F=\mathbf 0$. Otherwise [\[eq:orbit-decomposition\]](#eq:orbit-decomposition){reference-type="eqref" reference="eq:orbit-decomposition"} gives unique $a\in\mathbb Z$ and $0\leq s\leq d$ such that $$F(x_{q,d})=\sigma^a x_{q,s}.$$ The endomorphism $\sigma^aD_{d-s}$ has the same value at $x_{q,d}$, hence $F=\sigma^aD_{d-s}$. This proves that [\[eq:end-monoid\]](#eq:end-monoid){reference-type="eqref" reference="eq:end-monoid"} contains every endomorphism; [\[prop:lowering-continuity\]](#prop:lowering-continuity){reference-type="ref" reference="prop:lowering-continuity"} proves the reverse inclusion.

The displayed maps are distinct. Different lowering indices send $x_{q,d}$ to different layers. At a fixed lowering index, different shift exponents give different points because every nonzero orbit is free. The constant map is separate. Since the lowering maps commute with the shift, [\[eq:end-multiplication\]](#eq:end-multiplication){reference-type="eqref" reference="eq:end-multiplication"} follows from [\[eq:lowering-composition\]](#eq:lowering-composition){reference-type="eqref" reference="eq:lowering-composition"}.

For $r>0$, the image of $\sigma^aD_r$ misses the top $r$ layers; $\mathbf 0$ is also not invertible. Every $\sigma^aD_0=\sigma^a$ is invertible. The units are therefore precisely the shift powers, proving $\operatorname{Aut}(X_{q,d})\cong\mathbb Z$.

Some authors reserve "endomorphism" for onto shift-commuting maps. Under that convention the preceding proof shows that the surjective endomorphism monoid equals the automorphism group $\langle\sigma\rangle$. Throughout this paper, $\operatorname{End}$ uses the broader cellular-automaton convention.

# Conjugacy rigidity

We first isolate the arithmetic consequence of a one-digit degeneration.

[\[lem:one-digit-scales\]]{#lem:one-digit-scales label="lem:one-digit-scales"} Let $p\geq2$, $s\geq1$, and $u_j\to+\infty$. If $$\sigma^{u_j}x_{p,s}\longrightarrow\sigma^b x_{p,s-1},$$ then for all sufficiently large $j$ there is an exponent $m_j\in\mathbb N_0$ such that $$\label{eq:one-digit-centers}
 u_j=b+p^{m_j}.$$

Every subsequence has, by [\[prop:centered-limits\]](#prop:centered-limits){reference-type="ref" reference="prop:centered-limits"}, a further subsequence of the form $u_j=a+p^{m_j}$ whose limit is $\sigma^a x_{p,s-1}$. Freeness of $\mathcal O_{s-1}$ forces $a=b$. If [\[eq:one-digit-centers\]](#eq:one-digit-centers){reference-type="eqref" reference="eq:one-digit-centers"} failed along infinitely many indices, applying this argument to precisely those indices would give a contradiction.

[\[lem:exponential-matching\]]{#lem:exponential-matching label="lem:exponential-matching"} Let $p,q\geq2$. Suppose that for all sufficiently large $N$ there are integers $m_N$ and a fixed integer $K$ such that $$\label{eq:exponential-difference}
 q^N-p^{m_N}=K.$$ Then $q=p^u$ for an integer $u\geq1$, and in fact $K=0$ and $m_N=uN$ eventually. If the analogous conclusion also holds with $p$ and $q$ interchanged, then $p=q$.

The right side of $p^{m_N}=q^N-K$ is eventually strictly increasing, so $m_N$ is eventually strictly increasing. Dividing consecutive equations gives $$p^{m_{N+1}-m_N}
 =\frac{q^{N+1}-K}{q^N-K}\longrightarrow q.$$ The left side lies in the discrete set $\{p,p^2,\ldots\}$. It is therefore eventually constant and equal to $q$, so $q=p^u$ for some $u\geq1$. Next, $$p^{m_N-uN}=\frac{p^{m_N}}{q^N}\longrightarrow1.$$ This is a sequence in the discrete set $p^{\mathbb Z}$, hence it eventually equals $1$. Thus $m_N=uN$ and [\[eq:exponential-difference\]](#eq:exponential-difference){reference-type="eqref" reference="eq:exponential-difference"} gives $K=0$.

If also $p=q^v$ for an integer $v\geq1$, then $q=q^{uv}$. Since $q>1$, one has $uv=1$, so $u=v=1$ and $p=q$.

The forward implication is immediate when $(q,d)=(p,e)$. Conversely, let $H:X_{q,d}\to X_{p,e}$ be a conjugacy. Cantor--Bendixson height is a topological invariant, so $d+2=e+2$ and hence $d=e$.

The isolated points of $X_{q,d}$ are exactly $\mathcal O_d$, while the points of rank one are exactly $\mathcal O_{d-1}$. Thus there are integers $b,c$ with $$H(x_{q,d})=\sigma^c x_{p,d},
 \qquad
 H(x_{q,d-1})=\sigma^b x_{p,d-1}.$$ For every $N$, $$\sigma^{q^N}x_{q,d}\longrightarrow x_{q,d-1}.$$ Applying $H$ and using shift commutation gives $$\sigma^{q^N+c}x_{p,d}\longrightarrow\sigma^b x_{p,d-1}.$$ By [\[lem:one-digit-scales\]](#lem:one-digit-scales){reference-type="ref" reference="lem:one-digit-scales"}, $$q^N+c=b+p^{m_N}$$ for all sufficiently large $N$. Hence $q^N-p^{m_N}=b-c$ and [\[lem:exponential-matching\]](#lem:exponential-matching){reference-type="ref" reference="lem:exponential-matching"} gives $q=p^u$. Applying the same argument to $H^{-1}$ gives $p=q^v$. The last part of [\[lem:exponential-matching\]](#lem:exponential-matching){reference-type="ref" reference="lem:exponential-matching"} yields $p=q$.

The inverse conjugacy is essential. For example, every power of $4$ is a power of $2$, but the odd powers of $2$ have no matching return scale in base $4$.

# Periodic points, invariant measures, and entropy

The point $0^{\mathbb Z}$ is fixed. Every other point has a nonempty support bounded below. If such a point had nonzero period $k$, its support would be invariant under translation by $k$ and would consequently be unbounded in both directions. This contradiction proves $$\operatorname{Per}(X_{q,d})=\{0^{\mathbb Z}\}.$$

The space $X_{q,d}$ is countable by [\[eq:orbit-decomposition\]](#eq:orbit-decomposition){reference-type="eqref" reference="eq:orbit-decomposition"}. Let $\mu$ be an invariant Borel probability. All atoms on a fixed infinite orbit have the same mass. That mass must be zero, since otherwise the orbit would have infinite total mass. There are only finitely many such orbits, so their union has measure zero. Therefore $\mu(\{0^{\mathbb Z}\})=1$ and $\mu=\delta_{0^{\mathbb Z}}$.

The measure-theoretic entropy of $\delta_{0^{\mathbb Z}}$ is zero. The variational principle for continuous maps of compact metric spaces now gives $h_{\mathrm{top}}(X_{q,d})=0$.

The system is therefore topologically transitive but uniquely ergodic on a fixed point; its transitive point is not recurrent. The nontrivial structure is topological and functorial rather than measure-theoretic.

# Ownership boundary and reproducible checks

The sequence $x_{q,1}$ has support $1,q,q^2,\ldots$. Gheorghiciuc's exponential occurrence function is exactly this one-sided word and yields linear factor complexity [@Gheorghiciuc2007]. In the binary case, Salo and Törmä call the orbit closure with markers at $2^n$, $n>0$, the binary powers-of-two shift [@SaloTorma2012]. Their starting convention differs by one initial marker from ours. These sources prevent any claim that the $d=1$ seed, exponential sparsity, or zero entropy is new.

Cobham's theory owns automaticity [@Cobham1972]; Wessel and the sources therein own the general sparse-support dichotomy and automatic rank [@Wessel2025]; Krawczyk owns the general characterization of automatic points in an automatic system and its factors [@Krawczyk2026]. None of those results is restated here as a contribution. Our residual object is the $d\geq2$ tower, and the residual claims are the exact centered-limit normal form, Cantor--Bendixson filtration, full nilpotent endomorphism monoid, and two-parameter conjugacy rigidity.

The accompanying script `code/verify_digit_weight.py` checks finite shadows of the fragile statements. It tests many centered windows with nonconsecutive escaping exponents and nonzero phases, the absorbing truncated-addition law, a divisibility form of [\[lem:bounded-difference\]](#lem:bounded-difference){reference-type="ref" reference="lem:bounded-difference"}, and bidirectional return-scale separation. These computations are deterministic controls, not substitutes for the all-scale proofs.

# Conclusion

Fixed unit-digit weight converts an elementary regular language into a countable transitive subshift with a rigid finite topological tower. The same escaping-digit mechanism controls the orbit closure, every derivative, every cellular automaton, and every conjugacy. The resulting endomorphism monoid is the product of integer shifts with a finite nilpotent lowering chain, completed by an absorbing zero. The construction gives such a tower at every finite height at least three, while the base $q$ remains visible in the one-digit return scales.

Two limitations are deliberate. First, the paper treats only unit digits; allowing arbitrary nonzero digit values introduces genuine carry relations. Second, the ownership statement is bounded to the primary-source search described above and does not assert absolute priority. Both extensions are natural directions for further work.
