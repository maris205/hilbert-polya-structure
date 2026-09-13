---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--206-ternary-cyclic-record-feedback"
canonical_tex: "symbolic_dynamics/papers/206-ternary-cyclic-record-feedback/main.tex"
canonical_pdf: "symbolic_dynamics/papers/206-ternary-cyclic-record-feedback/main.pdf"
source_sha256: "828d03e62e7d5182d98c4cbd830175abe30fc619608a37e2117676a9fd118484"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Two-Step Images and One-Step Fibres\protect of Ternary Cyclic Record Feedback

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/206-ternary-cyclic-record-feedback>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/206-ternary-cyclic-record-feedback/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/206-ternary-cyclic-record-feedback/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/206-ternary-cyclic-record-feedback/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/206-ternary-cyclic-record-feedback/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study the synchronous map on ternary cyclic words which replaces each letter by the number of strict records in the full forward scan beginning at that position. We identify its first image by a one-sided adjacent-step constraint and its second image by a two-sided unit-step constraint, both with minimum one. On the second image the map is reflection in the range, so the fourth iterate equals the second. The all-one word is the sole fixed state, all other recurrent states have period two, and the sharp entrance height is two for every length at least three. Independently, we reconstruct every one-step source of every target by splitting at its one positions and conditioning on the source maximum. The resulting fibre formula is an explicit product of run factors with two correction terms. It gives a maximum of one plus the largest product of positive parts summing to the word length for lengths at least three, with all labelled equality targets and the small-length exceptions determined. Standard record statistics, trace counts and integer-product optimization are supporting ingredients.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Two-Step Images and One-Step Fibres\
  of Ternary Cyclic Record Feedback
```

## Markdown 正文

# The cyclic feedback map

For $n\ge1$, put $X_n=\{1,2,3\}^n$ and read position subscripts modulo $n$. Define $R:X_n\to X_n$ by letting $R(x)_i$ count the strict left-to-right records of $$x_i,x_{i+1},\ldots,x_{i+n-1}.$$ The first letter is a record, and a later letter is a record only when it exceeds every preceding letter. Thus $1\le R(x)_i\le3$. All scans use the same old word. Positions are labelled: words differing by a rotation are not identified. We seek the exact images and recurrent dynamics of $R$, and all sources of a prescribed one-step target.

Strict and weak record statistics for words and multisets, including single-scan record counts and position templates, are classical [@myers2008maxima]. Only the first occurrence of a value can be a strict record. Repeatedly jumping to the next strictly greater value therefore traces a scan's records; this uses the strict nearest-value primitive studied in @berkman1993nearest, after reversing the order. Neither the statistic nor its static pointer description is new here. The feedback question recomputes these counts at every cyclic start. For example, $123123$ and $123213$ have the same multiset, first-occurrence order and displayed single-scan record positions, but their cyclic outputs are $321321$ and $321221$. Those conditioning data alone do not determine the joint target; this observation does not exclude more elaborate reductions.

We prove an exact two-step reflection core and, by a separate source-maximum decomposition, an evaluated one-step inverse for each target. Transfer-matrix counts, weak binary chain counts and the classical integer-product optimum are elementary consequences and tools, not separate contributions.

# Exact images and recurrent reflection

Define $$\begin{aligned}
 \mathcal D_n&=\{b\in X_n:\min b=1,\ b_i-b_{i+1}\le1\text{ for every }i\},\\
 \mathcal C_n&=\{c\in X_n:\min c=1,\ |c_i-c_{i+1}|\le1\text{ for every }i\}.\end{aligned}$$ Thus $\mathcal D_n$ forbids cyclic edge $31$, while $\mathcal C_n$ forbids both $31$ and $13$. The minimum condition is part of each definition.

[\[thm:core\]]{#thm:core label="thm:core"} For every $n\ge1$, $R(X_n)=\mathcal D_n$ and $R^2(X_n)=\mathcal C_n$. On $\mathcal C_n$, the update is $$\label{eq:reflection}
 R(c)_i=\max c+1-c_i.$$ Consequently $R^4=R^2$, the exact recurrent set is $\mathcal C_n$, the sole fixed word is $1^n$, and every other recurrent period is two. The largest entrance into the recurrent set is one for $n=1,2$ and two for $n\ge3$.

The output ones occur exactly at the source's global maxima. Comparing scans beginning at $i$ and $i+1$, every record after the initial $x_i$ in the first scan also occurs in the second: it exceeds $x_i$ and all intervening values. The first scan thus has at most one extra record, proving $R(x)_i\le R(x)_{i+1}+1$ and $R(X_n)\subseteq\mathcal D_n$. Conversely, for $b\in\mathcal D_n$ set $x_i=4-b_i$. Its maximum is three and every cyclic upward step is at most one. Starting at $x_i$, a scan must visit every integer level from $x_i$ to three before exceeding that level. These are exactly its records, giving $R(x)_i=4-x_i=b_i$.

Now let $b\in\mathcal D_n$ and $c=R(b)$. The first-image argument already gives $c_i-c_{i+1}\le1$. If $b_i<b_{i+1}$, the next letter is the first new record and $c_i=c_{i+1}+1$; if they are equal, their counts agree. If $b_i>b_{i+1}$, it is a unit drop. The scan beginning at $b_{i+1}$ can then have at most one additional record, the value $b_i$, before the shared records larger than $b_i$. This also covers a maximum at $i$, which appears at the end of the other full scan. Hence $c_{i+1}-c_i\le1$ and $R(\mathcal D_n)\subseteq\mathcal C_n$.

For $c\in\mathcal C_n$, put $M=\max c$. Its upward unit bound forces all and only the record levels $c_i,c_i+1,\ldots,M$ in the scan from $i$, proving [\[eq:reflection\]](#eq:reflection){reference-type="eqref" reference="eq:reflection"}. Reflection preserves minimum one, maximum $M$ and the adjacent unit bounds; applying it twice is the identity. Since $\mathcal C_n\subseteq\mathcal D_n$, this proves $R(\mathcal D_n)=\mathcal C_n$ and $R^4=R^2$. Every periodic state belongs to the second image. A reflection-fixed word is constant, and its minimum one then forces $1^n$, proving the recurrent classification.

For $n=1$, every source reaches $1$ and source $2$ has entrance one. For $n=2$, the first image is $\{11,12,21\}=\mathcal C_2$, and $22$ has entrance one. For $n\ge3$, the source $1^{n-2}23$ has first image $3^{n-2}21$. Its closing edge $13$ violates the two-sided unit bound, so that first image is not recurrent. The second-image theorem supplies the matching upper bound two.

[\[cor:counts\]]{#cor:counts label="cor:counts"} Let $L_0=2,L_1=3$, $L_n=3L_{n-1}-L_{n-2}$ and let $P_0=P_1=2$, $P_n=2P_{n-1}+P_{n-2}$, with the recurrences used for $n\ge2$. For $n\ge1$, $$|\mathcal D_n|=L_n-2^n,\qquad |\mathcal C_n|=P_n+1-2^n.$$ There are $(|\mathcal C_n|-1)/2$ strict two-cycles.

The edge matrices for the two constraints, in alphabet order $1,2,3$, are $$A=\begin{pmatrix}1&1&1\\1&1&1\\0&1&1\end{pmatrix},\qquad
 B=\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix}.$$ Their labelled cyclic word counts are $\mathop{\mathrm{tr}}(A^n)$ and $\mathop{\mathrm{tr}}(B^n)$. Words avoiding one contribute $2^n$ in either case. The characteristic polynomial of $A$ is $\lambda(\lambda^2-3\lambda+1)$, and $B$ has eigenvalues $1,1+\sqrt2,1-\sqrt2$. Thus their traces for $n\ge1$ are $L_n$ and $P_n+1$, including loops at $n=1$. Subtracting the words avoiding one proves the formulas. The cycle count follows from the unique fixed point and core involution.

# Evaluated one-step fibres and every maximizer

For $b\in\mathcal D_n$, call its one positions roots. Between consecutive roots, read the intervening word $u$ forward up to the next root. Each root terminates one such run, possibly empty. All letters in a run are two or three. For a run of length $m$, define $$g(u)=\begin{cases}
 m+1,&u\text{ has no three},\\
 \text{length of its terminal two-run},&u\text{ has a three}.
 \end{cases}$$ The terminal length in the second case is positive, since $31$ is forbidden. Let $\mathcal U(b)$ be the collection of these labelled runs.

[\[thm:inverse\]]{#thm:inverse label="thm:inverse"} Every target $b\in X_n$ has one-step fibre size $$\label{eq:psi}
 |R^{-1}(b)|=\Psi_n(b)=
 \begin{cases}
 \displaystyle\prod_{u\in\mathcal U(b)}g(u)
   +\mathbf 1\{3\notin b\}+\mathbf 1\{b=1^n\},&b\in\mathcal D_n,\\
 0,&b\notin\mathcal D_n.
 \end{cases}$$ The product and the two indicators respectively enumerate all sources with maximum three, two and one, without repetitions.

Invalid targets have no sources by Theorem [\[thm:core\]](#thm:core){reference-type="ref" reference="thm:core"}. Suppose $b\in\mathcal D_n$. A source of maximum one is necessarily $1^n$, contributing the last indicator. For maximum two, a source two gives output one and a source one gives output two. Thus the unique possible source is $x_i=3-b_i$, which exists exactly when $b$ has no three. Since $b$ has a one, this source really has maximum two, including when $b=1^n$.

For maximum three, the source threes are exactly the roots of $b$. Every intervening source run is binary and its forward scans stop gaining records at the next three. A source two gives output two. A source one gives output three exactly when a two occurs later in its run; otherwise it gives output two.

If a target run $u$ has no three, its source run must be weakly decreasing, $2^a1^{m-a}$, for $a=0,\ldots,m$. These $m+1$ choices all work, including the one empty choice at $m=0$. If $u$ has a three, let its last three be followed by $t\ge1$ twos. Each target three forces source one. Each target two before the last three forces source two: a source one there would see the later two needed to trigger that last three and would itself output three. The terminal $t$ source letters must have the form $2^a1^{t-a}$ with $1\le a\le t$. The positive prefix is necessary to trigger the last target three and also triggers every earlier target three. Conversely the forced prefix and every one of these $t$ terminal choices give precisely the required target run. This proves both necessity and sufficiency.

Runs are independent after their terminating source threes are fixed, so the maximum-three count is the product in [\[eq:psi\]](#eq:psi){reference-type="eqref" reference="eq:psi"}. The three source-maximum cases are disjoint and exhaustive, proving the formula and the asserted reconstruction.

Let $J(n)$ be the largest product of positive integers summing to $n$, with a single part allowed. Its values are $$\label{eq:J}
 J(1)=1,\qquad
 \begin{cases}
 J(3a)=3^a,&a\ge1,\\
 J(3a+1)=4\cdot3^{a-1},&a\ge1,\\
 J(3a+2)=2\cdot3^a,&a\ge0.
 \end{cases}$$ We recall the elementary exchange proof below, rather than treating integer-product optimization as a new ingredient.

[\[thm:extreme\]]{#thm:extreme label="thm:extreme"} The maximum one-step fibre is three for $n=1,2$ and $1+J(n)$ for $n\ge3$. The only maximizing target at $n=1$ is $1$; at $n=2$ the maximizing targets are $11,12,21$. For $n\ge3$, all maximizing targets are binary, and their cyclic root-terminated blocks $2^{s-1}1$ have the following complete lists of sizes:

1.  if $n\equiv0\pmod3$, all sizes are three;

2.  if $n\equiv1\pmod3$, sizes are threes and either one four or two twos;

3.  if $n\equiv2\pmod3$, sizes are threes and one two.

Every labelled cyclic placement of the stated blocks attains the maximum.

If $b\in\mathcal D_n$ has any three, replace its threes by twos to obtain $b^*$. Roots and run lengths are unchanged. In a run of length $m$ containing a three, the terminal-two factor is at most $m-1$, strictly less than $m+1$. All other positive factors stay the same; the maximum-two correction also appears in $b^*$. Hence $\Psi_n(b)<\Psi_n(b^*)$, excluding all such targets from the maximum. Invalid targets have zero fibres and are excluded as well.

The all-one target has fibre three. For every other valid binary target, write its successive root-block sizes as $s_1,\ldots,s_k$. Then $\sum_j s_j=n$ and [\[eq:psi\]](#eq:psi){reference-type="eqref" reference="eq:psi"} gives $1+\prod_j s_j$. Conversely every composition other than all singletons is realized by the blocks $2^{s_j-1}1$ on the labelled cycle.

For $n\ge2$ an optimal product has no part one, because merging a one with another part increases the product, including two singleton parts. A part $s\ge5$ can be replaced by $3,s-3$, increasing the product since $3(s-3)>s$. A four may be kept or split into two twos without change, while three twos are inferior to two threes since $8<9$. Thus after optionally splitting fours, every optimum consists of threes and at most two twos. The sum modulo three gives exactly [\[eq:J\]](#eq:J){reference-type="eqref" reference="eq:J"} and the listed size patterns; each listed pattern conversely has the stated product.

For $n\ge3$, $1+J(n)>3$, so the all-one target is not an extremizer. For $n=2$, the all-one target and the two placements of a size-two block each have fibre three, exhausting the image. For $n=1$ only target one is in the image, with three sources. These cases prove all assertions without quotienting by rotation.

# Scope and finite verification

The results concern the full ternary carrier at every $n\ge1$. No all-time fibre formula, transient-layer census or larger-alphabet inverse or maximum is asserted. The source-run decoder and exact feedback images are the two descriptions; matrix spectra and integer products are their elementary supporting calculations.

The standalone `verify.py` exhausts $X_n$ for $1\le n\le10$, checking images, literal arrows, recurrent cores, every target fibre and all equality targets. Complete source sets are compared through $n=7$; an independent part-choice dynamic program checks [\[eq:J\]](#eq:J){reference-type="eqref" reference="eq:J"} through $n=40$. The actual `CANONICAL.json` records $655{,}256$ assertions. These are finite falsification checks; the proofs establish the all-length statements without extrapolation.
