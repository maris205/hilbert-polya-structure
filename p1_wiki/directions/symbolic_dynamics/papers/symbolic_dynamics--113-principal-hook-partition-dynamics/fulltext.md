---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--113-principal-hook-partition-dynamics"
canonical_tex: "symbolic_dynamics/papers/113-principal-hook-partition-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/113-principal-hook-partition-dynamics/main.pdf"
source_sha256: "38a864c22d323c23f324b36ec1cf4de2c232586ad0ef0a8499fc8c4d7530fd81"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Principal-hook regrouping dynamics on integer partitions

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/113-principal-hook-partition-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/113-principal-hook-partition-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/113-principal-hook-partition-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/113-principal-hook-partition-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/113-principal-hook-partition-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a partition of a fixed positive integer, regroup the Ferrers diagram by its principal diagonal hooks and iterate the resulting partition. The principal-hook partition and first-hook identity, the adjacent-gap image and product fibre formula, and the one-step diagonal-hook formalism are all treated as owned background and receive zero credit. Our single main theorem is an exact increment identity for the first adjacent gap, from which we deduce the sharp maximum transient depth $\lfloor n/2\rfloor$. As explicit low-credit corollaries, the one-row partition is globally absorbing, the owned fibre weights give a depth-state-weighted layer transport identity, conjugation has one entrance-time exception, and each fixed-weight system has zeta function $(1-z)^{-1}$. All statements include $n=1,2$.
author:
- Anonymous
bibliography:
- references.bib
title: 'Principal-hook regrouping dynamics on integer partitions'
```

## Markdown 正文

# Introduction and scope

Let $\mathcal P(n)$ be the finite set of integer partitions of $n\geq 1$. We study the deterministic self-map obtained by replacing a Ferrers diagram with the list of its principal diagonal-hook lengths. Principal hooks and Frobenius coordinates are standard tools in partition theory [@Andrews1998]. We make the ownership subtraction item by item. Gutschwager explicitly defines the principal-hook length partition and records its first part $\lambda_1+\ell(\lambda)-1$ [@Gutschwager2011]; Goupil records the adjacent-gap image and exact product fibre weight [@Goupil2009]; and Chern--Yee give direct prior work on diagonal-hook data and an involution preserving every diagonal-hook length [@ChernYee2022]. The map object, first-hook identity, one-step image, fibre product, and standard diagonal-hook symmetries therefore receive zero credit here. Proposition [\[prop:classical\]](#prop:classical){reference-type="ref" reference="prop:classical"} is reproduced only to keep the later dynamics self-contained.

After this subtraction, the present proof package has one main theorem: a direct Ferrers-diagram calculation gives the exact increment of the first adjacent gap, a pointwise depth bound, and the sharp global depth. Global absorption from the owned first-hook identity, fibre-weighted layer transport, the conjugation timing exception, the periodic census, and zeta are labelled low-credit corollaries rather than co-equal headline results. A bounded owner search located no exact temporal owner, but this negative search is not novelty or priority evidence.

#### Firewall.

The state space here consists of unlabelled integer partitions of a fixed weight, and the update regroups cells into diagonal hooks. It is not the labelled set-partition lattice, and it uses neither a cyclic action nor a lattice join. Consequently none of the cyclic-shift join engine, Bell-number basin census, or Möbius-lattice mechanism of the separate P110 system is invoked or claimed. External novelty, priority, and dissemination status for the results below remain [hold]{.smallcaps}.

# Principal hooks and owned one-step inputs

Write a partition as $\lambda=(\lambda _1,\ldots,\lambda _{\ell})$ with $\lambda_1\geq\cdots\geq\lambda_{\ell}>0$, and write $\lambda'$ for its conjugate. Its Durfee size is $$d=d(\lambda)=\max\{i:\lambda_i\geq i\}.$$ The Frobenius arms and legs are $$\alpha_i=\lambda_i-i,
 \qquad
 \beta_i=\lambda'_i-i
 \qquad(1\leq i\leq d).$$ Both sequences are strictly decreasing and nonnegative. The $i$th principal diagonal hook has length $$h_i=\alpha_i+\beta_i+1
     =\lambda_i+\lambda'_i-2i+1.$$ These hooks partition the Ferrers diagram: a cell $(r,c)$ belongs to the hook rooted at $(\min\{r,c\},\min\{r,c\})$. Hence $\sum_i h_i=|\lambda|$, while $h_i-h_{i+1}\geq2$. Thus $$H(\lambda)=(h_1,\ldots,h_d)$$ defines a self-map of $\mathcal P(n)$. This principal-hook partition is a standard object, explicitly denoted $hl(\lambda)$ by Gutschwager [@Gutschwager2011]; its use as a one-step map receives zero credit.

Let $$\mathcal I(n)=\{(h_1,\ldots,h_r)\in\mathcal P(n):
               h_i-h_{i+1}\geq2\text{ for }1\leq i<r\}.$$ For a one-part partition the gap condition is vacuous.

[\[prop:classical\]]{#prop:classical label="prop:classical"} The image of $H:\mathcal P(n)\to\mathcal P(n)$ is exactly $\mathcal I(n)$. Moreover, if $h=(h_1,\ldots,h_r)\in\mathcal I(n)$, then $$\label{eq:fibre}
 w(h):=\#H^{-1}(h)
 =h_r\prod_{i=1}^{r-1}(h_i-h_{i+1}-1).$$ The empty product in [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} is $1$.

The preceding calculation puts every image in $\mathcal I(n)$. Conversely, Frobenius coordinates over a prescribed $h$ are precisely pairs of strictly decreasing nonnegative sequences $(\alpha_i)$ and $(\beta_i)$ satisfying $\alpha_i+\beta_i=h_i-1$. There are $h_r$ choices for $\alpha_r\in\{0,\ldots,h_r-1\}$, after which $\beta_r$ is fixed. For $i<r$, put $$x_i=\alpha_i-\alpha_{i+1}-1,
 \qquad
 y_i=\beta_i-\beta_{i+1}-1.$$ Then $x_i,y_i\geq0$ and $x_i+y_i=h_i-h_{i+1}-2$, giving $h_i-h_{i+1}-1$ choices. These choices are independent and reconstruct the two Frobenius sequences, hence a unique partition. This proves both surjectivity onto $\mathcal I(n)$ and [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. The argument and product were previously recorded by Goupil [@Goupil2009].

# The gap clock and sharp depth

A fixed point $q$ of a map on a finite set will be called *globally absorbing*, or *globally attracting in finite time*, if every state reaches $q$ after finitely many iterates. This is the only meaning of global attraction used below.

For $\lambda\in\mathcal P(n)$ define its entrance time $$\tau(\lambda)=\min\{t\geq0:H^t(\lambda)=(n)\}.$$ The next result first shows that this number is always defined.

[\[cor:absorption\]]{#cor:absorption label="cor:absorption"} For every $\lambda\in\mathcal P(n)$, $$\label{eq:firstpart}
 (H\lambda)_1=\lambda_1+\ell(\lambda)-1.$$ Unless $\lambda=(n)$, the right-hand side is strictly larger than $\lambda_1$. Consequently $(n)$ is a globally absorbing fixed point and is the unique fixed point and the unique periodic point of $H$ on $\mathcal P(n)$. The identity [\[eq:firstpart\]](#eq:firstpart){reference-type="eqref" reference="eq:firstpart"} itself is owned and receives zero credit.

The first diagonal hook consists of the first row and first column with their common corner counted once, which gives the identity already recorded in [@Gutschwager2011]. A non-one-row partition has $\ell(\lambda)\geq2$, so its first part strictly increases. Since $\mathcal P(n)$ is finite and no first part exceeds $n$, every orbit reaches $(n)$. The same strict increase excludes any other fixed or periodic point.

Pad a one-part partition by $\lambda_2=0$ and set $$g(\lambda)=\lambda_1-\lambda_2,
 \qquad
 m_1(\lambda)=\#\{i:\lambda_i=1\}.$$

[\[thm:gapdepth\]]{#thm:gapdepth label="thm:gapdepth"} Let $\lambda\in\mathcal P(n)$ be nonterminal.

1.  If $d(\lambda)\geq2$, then $$\label{eq:gapinc}
     g(H\lambda)-g(\lambda)
     =\ell(\lambda)-\lambda'_2+2
     =2+m_1(\lambda)\geq2.$$

2.  If $d(\lambda)=1$, then $\lambda=(a,1^b)$ for some $b\geq1$, $H\lambda=(n)$, and $$\label{eq:durfeeone}
     g(H\lambda)-g(\lambda)=b+1\geq2.$$

For every $\lambda\in\mathcal P(n)$, $$\label{eq:pointbound}
 \tau(\lambda)\leq
 \left\lfloor\frac{n-g(\lambda)}2\right\rfloor
 \leq\left\lfloor\frac n2\right\rfloor.$$ The global maximum is sharp: $$\label{eq:maxdepth}
 \max_{\lambda\vdash n}\tau(\lambda)=\left\lfloor\frac n2\right\rfloor.$$ It is attained by $\lambda^{\star}=(\lceil n/2\rceil,\lfloor n/2\rfloor)$, with the zero second part omitted when $n=1$.

Suppose first that $d\geq2$. The first two parts of $H\lambda$ are $$h_1=\lambda_1+\ell(\lambda)-1,
 \qquad
 h_2=\lambda_2+\lambda'_2-3.$$ Subtracting and then subtracting $g(\lambda)$ proves the first equality in [\[eq:gapinc\]](#eq:gapinc){reference-type="eqref" reference="eq:gapinc"}. Because $\lambda'_2$ counts the parts of $\lambda$ that are at least two, $\ell(\lambda)-\lambda'_2=m_1(\lambda)$, proving the second equality.

If $d=1$, every part below the first is $1$. Nonterminality gives $\lambda=(a,1^b)$ with $b\geq1$. Its sole principal hook is the entire diagram, so $H\lambda=(n)$; since $n=a+b$ and $g(\lambda)=a-1$, [\[eq:durfeeone\]](#eq:durfeeone){reference-type="eqref" reference="eq:durfeeone"} follows.

At each of the $\tau(\lambda)$ nonterminal steps the gap therefore rises by at least two, whereas the terminal gap is $g((n))=n$. This gives $2\tau(\lambda)\leq n-g(\lambda)$ and hence [\[eq:pointbound\]](#eq:pointbound){reference-type="eqref" reference="eq:pointbound"}; it also holds trivially at the terminal state.

It remains to attain the bound. For $n=1$, the state $(1)$ is terminal and has depth zero. If $a\geq b\geq2$, a direct two-row Ferrers calculation gives $$\label{eq:tworow}
 H(a,b)=(a+1,b-1),$$ whereas $H(a,1)=(a+1)$. For $n\geq2$, start from $a=\lceil n/2\rceil$ and $b=\lfloor n/2\rfloor$, so $b\geq1$. Equation [\[eq:tworow\]](#eq:tworow){reference-type="eqref" reference="eq:tworow"} applies $b-1$ times (zero times when $b=1$), ending at $(n-1,1)$; the final hook step $H(n-1,1)=(n)$ gives $b$ steps in total. Thus the upper bound is attained and [\[eq:maxdepth\]](#eq:maxdepth){reference-type="eqref" reference="eq:maxdepth"} follows.

For $n=1$, $\mathcal P(1)=\{(1)\}$ and the maximum depth is $0$. For $n=2$, $H(1,1)=(2)$, so the two depths are $0$ and $1$. These agree with Theorem [\[thm:gapdepth\]](#thm:gapdepth){reference-type="ref" reference="thm:gapdepth"}; no exceptional empty state is introduced.

# Low-credit consequences

For $t\geq0$ let $$A_t(n)=\#\{\lambda\in\mathcal P(n):\tau(\lambda)=t\}.$$

[\[cor:layers\]]{#cor:layers label="cor:layers"} For every $n\geq1$, $$\label{eq:initiallayers}
 A_0(n)=1,
 \qquad
 A_1(n)=n-1.$$ For every $t\geq2$, $$\label{eq:layerrecurrence}
 A_t(n)=
 \sum_{\substack{h=(h_1,\ldots,h_r)\in\mathcal I(n)\\
                   \tau(h)=t-1}}
 h_r\prod_{i=1}^{r-1}(h_i-h_{i+1}-1).$$ An empty sum is $0$. In particular, $A_t(n)=0$ for $t>\lfloor n/2\rfloor$ and $\sum_tA_t(n)=|\mathcal P(n)|$. This is a depth-state-weighted transport identity over $\mathcal I(n)$, not a closed scalar recurrence in the numbers $A_t(n)$ alone.

Corollary [\[cor:absorption\]](#cor:absorption){reference-type="ref" reference="cor:absorption"} makes $(n)$ the only depth-zero state. The fibre over $(n)$ has size $w((n))=n$ by Proposition [\[prop:classical\]](#prop:classical){reference-type="ref" reference="prop:classical"}; exactly one member of that fibre is $(n)$ itself. This proves [\[eq:initiallayers\]](#eq:initiallayers){reference-type="eqref" reference="eq:initiallayers"}, including $A_1(1)=0$.

If $t\geq2$, a state $\lambda$ has depth $t$ exactly when its first image $h=H\lambda$ has depth $t-1$. Every possible $h$ belongs to $\mathcal I(n)$, and the fibres over distinct $h$ are disjoint. Summing the owned fibre weight [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} gives [\[eq:layerrecurrence\]](#eq:layerrecurrence){reference-type="eqref" reference="eq:layerrecurrence"}. The vanishing range follows from Theorem [\[thm:gapdepth\]](#thm:gapdepth){reference-type="ref" reference="thm:gapdepth"}, and the mass identity follows because the depth layers partition the finite state space.

[\[cor:conjugation\]]{#cor:conjugation label="cor:conjugation"} For every $\lambda\in\mathcal P(n)$, $$\label{eq:conjugation}
 H(\lambda)=H(\lambda').$$ Consequently $H^t(\lambda)=H^t(\lambda')$ for every $t\geq1$. Entrance depth is also conjugation-invariant except for one explicit pair: if $n>1$, then $$\tau((n))=0,
 \qquad
 \tau((1^n))=1.$$ There are no other failures of $\tau(\lambda)=\tau(\lambda')$. The one-step diagonal-hook symmetry in [\[eq:conjugation\]](#eq:conjugation){reference-type="eqref" reference="eq:conjugation"} is standard and receives zero credit; only its stated timing consequence is used here.

Conjugation swaps the Frobenius arm and leg sequences, leaving every sum $\alpha_i+\beta_i+1$ unchanged. This proves [\[eq:conjugation\]](#eq:conjugation){reference-type="eqref" reference="eq:conjugation"} and the iterate statement. If neither member of a conjugate pair is terminal, then both depths equal $1+\tau(H\lambda)$. The only time exactly one member is terminal is the pair $(n),(1^n)$ for $n>1$; its displayed depths follow from the single-hook calculation. At $n=1$ the two partitions coincide.

[\[cor:zeta\]]{#cor:zeta label="cor:zeta"} For each fixed $n\geq1$, write $H_n:\mathcal P(n)\to\mathcal P(n)$ for the map above. For every $m\geq1$, $$\#\operatorname{Fix}(H_n^m)=1.$$ Hence the Artin--Mazur zeta function of this fixed finite system is $$\label{eq:zeta}
 \zeta_{H_n}(z)
 =\exp\!\left(\sum_{m\geq1}\frac{\#\operatorname{Fix}(H_n^m)}m z^m\right)
 =\frac1{1-z}$$ as a formal power series. The weight $n$ is fixed before forming the zeta function; no zeta function on the disjoint union of all weights is asserted.

Every point fixed by an iterate is periodic. Corollary [\[cor:absorption\]](#cor:absorption){reference-type="ref" reference="cor:absorption"} excludes every periodic point except $(n)$, which is fixed by all iterates. Thus every fixed-point count is one. Substitution into the definition gives $\exp(\sum_{m\geq1}z^m/m)=\exp(-\log(1-z))$, proving [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

# Two proof routes and falsification controls

The argument deliberately uses two distinct mechanisms. The *Frobenius/fibre route* decomposes each hook length into a strict arm and leg pair; it verifies the previously recorded one-step characterization and product weight, which remain zero-credit background. The *Ferrers/gap route* reads the first two diagonal hooks directly from row and column lengths; its substantive output is the main exact increment [\[eq:gapinc\]](#eq:gapinc){reference-type="eqref" reference="eq:gapinc"} and sharp depth theorem. Global absorption and the periodic census are elementary low-credit consequences of the owned first-hook identity. The layer transport joins the two routes but remains a low-credit, nonclosed identity.

Several tempting strengthenings are false. The map is not a projection: $H(2,2)=(3,1)$ and $H^2(2,2)=(4)$. Corollary [\[cor:conjugation\]](#cor:conjugation){reference-type="ref" reference="cor:conjugation"} cannot be strengthened to unconditional depth invariance, already at $(2)$ and $(1,1)$. Nor does a simple rectangular boundary describe all deepest states: for example $(4,4,4,4)\vdash16$ has depth $7$, below the maximum $8$. These examples, the formulas above, and all partitions through $n=40$ are checked by the exact standard-library verifier distributed with the manuscript. Computation is used only as a falsification and regression control; all mathematical statements have independent proofs above.
