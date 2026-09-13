---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--149-iterated-endpoint-peak-extraction"
canonical_tex: "symbolic_dynamics/papers/149-iterated-endpoint-peak-extraction/main.tex"
canonical_pdf: "symbolic_dynamics/papers/149-iterated-endpoint-peak-extraction/main.pdf"
source_sha256: "a8e4699d6935c4ce086de311e9324da705fac709d10d9db27fcfa244194c7746"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Iterated Endpoint-Peak Extraction on Permutations: All-Rank Images, Sections, and a Sharp Clock

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/149-iterated-endpoint-peak-extraction>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/149-iterated-endpoint-peak-extraction/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/149-iterated-endpoint-peak-extraction/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/149-iterated-endpoint-peak-extraction/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/149-iterated-endpoint-peak-extraction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Give both endpoints of a permutation a fictitious neighbour value zero, read all local-maximum values from left to right, and standardize the resulting word. Iterating this rule produces a deterministic variable-rank dynamics on the finite disjoint union of symmetric groups. We prove, for every source rank $n$ and iterate $k\ge1$, the exact image $$P^k(\mathfrak S_n)=\bigsqcup_{1\le m\le\lceil n/2^k\rceil}\mathfrak S_m.$$ The reverse inclusion is constructive: top values encode any target order, small values separate consecutive peaks, and unused values form a decreasing tail; composing minimal odd lifts gives a right section at every rank. It follows that the image has size $\sum_{m\le\lceil n/2^k\rceil}m!$ and that the sharp maximum absorption time is $\lceil\log_2n\rceil$, with a recursively lifted witness for every $n$. As a secondary result, we express every one-step target multiplicity as a sum of linear-extension counts of comparison-word posets augmented by the target peak-value order. An exhaustive exact audit covers all $409{,}113$ permutations through rank nine; it tests the formulas but is not used as proof. Static zero-boundary peak distributions, ordinary pinnacle sets and admissible orders, and run-sorting equidistribution are treated as credited background.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Iterated Endpoint-Peak Extraction on Permutations:\
  All-Rank Images, Sections, and a Sharp Clock
```

## Markdown 正文

# A variable-rank self-map

For a word of distinct values, $\operatorname{std}$ replaces its smallest value by $1$, its next smallest by $2$, and so on. Fix $N\ge1$ and use the finite carrier $$\mathfrak S_{\le N}:=\bigsqcup_{1\le n\le N}\mathfrak S_n.$$ For $\pi=\pi_1\cdots\pi_n$, set $\pi_0=\pi_{n+1}=0$. Let $$\operatorname{Peak}(\pi):=(\pi_i:\pi_{i-1}<\pi_i>\pi_{i+1})$$ in left-to-right order, and define $$\label{eq:P-def}
                         P(\pi):=\operatorname{std}(\operatorname{Peak}(\pi)).$$ The global maximum is always selected, so the output is nonempty. For example, $$\pi=4,1,6,2,5,3,
  \qquad \operatorname{Peak}(\pi)=4,6,5,
  \qquad P(\pi)=1,3,2.$$ Thus $P$ is a literal self-map of $\mathfrak S_{\le N}$, not of a single $\mathfrak S_n$. Because $N$ is arbitrary, the rank-wise theorems are stated for every $n$; inside a fixed carrier they are read with $1\le n\le N$.

We call $\operatorname{Peak}(\pi)$ the *endpoint-inclusive peak-value word*. It is not literally the conventional pinnacle set, whose peaks are restricted to interior positions. Fu's exterior-peak convention admits the left endpoint but excludes the right endpoint [@Fu2018]; it differs from our rule already on the permutation $12$. Ji uses exactly $\pi_0=\pi_{n+1}=0$ and admits every position $1\le i\le n$ in the static exterior-peak statistic [@Ji2025]. Those same-convention static distributions and Fu's neighbouring one-sided distributions receive zero contribution credit. The bridge to ordinary pinnacle theory is the padding $$\pi_1\cdots\pi_n\longmapsto
       1,(\pi_1+2),\ldots,(\pi_n+2),2.$$ Its ordinary interior peak values, in left-to-right order, are precisely the entries of $\operatorname{Peak}(\pi)$ shifted by two. Thus ordinary pinnacle sets and their admissible orders are nearest background rather than literal same-convention owners [@DavisEtAl2018; @RusuTenner2021; @DiazLopezEtAl2021; @DomagalskiEtAl2022; @Fang2022; @FalqueEtAl2024]. Alexandersson--Nabawanda construct an auxiliary bijection giving a multivariate equidistribution between input peak-value sets and peak-value sets after run-sorting; run-sorting itself is not a pointwise invariant map [@AlexanderssonNabawanda2022]. Static peak/pinnacle distributions, admissible orders, fixed-set counts, that equidistribution, and generic zigzag-poset technology all receive zero contribution credit. The lead result below is instead the ordered zero-boundary peak-value word followed by standardization and iteration, its images at every iterate, and explicit right sections.

# One-step packing and a right section

No two peak positions are adjacent. Hence every $\pi\in\mathfrak S_n$ satisfies $$\label{eq:packing}
                    1\le |P(\pi)|\le\left\lceil\frac n2\right\rceil.$$ Since $\lceil n/2\rceil<n$ for $n>1$, every nonsingleton step strictly decreases rank; equality in the displayed packing bound may occur.

Fix $\sigma=\sigma_1\cdots\sigma_m\in\mathfrak S_m$ and $n\ge2m-1$. Define high values $h_i=n-m+\sigma_i$ and the lift $$\label{eq:lift}
 L_{n,m}(\sigma):=
 h_1,1,h_2,2,\ldots,h_{m-1},m-1,h_m,
 n-m,n-m-1,\ldots,m,$$ where the terminal decreasing block is omitted if $n-m<m$. The high values are exactly $n-m+1,\ldots,n$; the displayed valleys use $1,\ldots,m-1$; and the tail contains every remaining value. Thus [\[eq:lift\]](#eq:lift){reference-type="eqref" reference="eq:lift"} is a permutation of $[n]$.

[\[lem:section\]]{#lem:section label="lem:section"} For every $\sigma\in\mathfrak S_m$ and $n\ge2m-1$, $$\label{eq:right-inverse}
                       P(L_{n,m}(\sigma))=\sigma.$$

The first high value exceeds the fictitious left boundary and its following valley. Every interior high lies between smaller valleys. The last high exceeds its left valley and either the first tail value or the fictitious right boundary. Hence all highs are peaks. A valley has a larger high neighbour, and every tail entry has a larger left neighbour, so no low value is a peak. The selected word is $h_1\cdots h_m$, whose standardization is $\sigma$.

Already, [\[eq:packing\]](#eq:packing){reference-type="eqref" reference="eq:packing"} and Lemma [\[lem:section\]](#lem:section){reference-type="ref" reference="lem:section"} show that the one-step image consists of every permutation of each rank at most $\lceil n/2\rceil$. The section is value-explicit rather than a counting argument.

# Every iterate image and the sharp clock

[\[thm:images\]]{#thm:images label="thm:images"} For every $n,k\ge1$, $$\label{eq:iterate-image}
 P^k(\mathfrak S_n)=
 \bigsqcup_{1\le m\le\lceil n/2^k\rceil}\mathfrak S_m,
 \qquad
 |P^k(\mathfrak S_n)|=\sum_{m=1}^{\lceil n/2^k\rceil}m!.$$ Moreover, every target in the displayed union has an explicit right section obtained by composing the lifts [\[eq:lift\]](#eq:lift){reference-type="eqref" reference="eq:lift"}.

Iterating [\[eq:packing\]](#eq:packing){reference-type="eqref" reference="eq:packing"} gives $$|P^k(\pi)|\le
 \left\lceil\frac{1}{2}
   \left\lceil\cdots\left\lceil\frac n2\right\rceil\cdots\right\rceil
 \right\rceil
 =\left\lceil\frac n{2^k}\right\rceil,$$ which proves the forward inclusion.

For the reverse inclusion, fix $\sigma\in\mathfrak S_m$ under this rank bound. The integer inequality $m\le\lceil n/2^k\rceil$ is equivalent to $$\label{eq:min-length}
                    n\ge 2^km-(2^k-1).$$ Put $a_k=m$ and recursively $a_j=2a_{j+1}-1$ for $j=k-1,\ldots,1$. Starting with $\sigma_k=\sigma$, set $$\sigma_j=L_{a_j,a_{j+1}}(\sigma_{j+1})
       \quad(j=k-1,\ldots,1),
 \qquad
 \pi=L_{n,a_1}(\sigma_1).$$ Condition [\[eq:min-length\]](#eq:min-length){reference-type="eqref" reference="eq:min-length"} is exactly what makes the outer lift legal; all inner lifts use their minimal odd length. Lemma [\[lem:section\]](#lem:section){reference-type="ref" reference="lem:section"} gives $P(\pi)=\sigma_1$ and $P(\sigma_j)=\sigma_{j+1}$, hence $P^k(\pi)=\sigma$. This proves the reverse inclusion constructively. The cardinality follows because different ranks are disjoint in the carrier. If some $a_j=1$, the corresponding $L_{1,1}$ is the identity, so the construction also covers arbitrarily large iterate ranks.

Let $\tau(\pi)$ be the first time the orbit reaches the one-letter permutation.

[\[thm:clock\]]{#thm:clock label="thm:clock"} The singleton is the unique recurrent state. Every $\pi\in\mathfrak S_n$ satisfies $\tau(\pi)\le\lceil\log_2n\rceil$, and for every $n\ge1$, $$\label{eq:clock}
                 \max_{\pi\in\mathfrak S_n}\tau(\pi)=\lceil\log_2n\rceil.$$ There is a recursively defined equality witness for every $n$.

For $n>1$, [\[eq:packing\]](#eq:packing){reference-type="eqref" reference="eq:packing"} strictly decreases rank, proving the recurrent claim and the upper bound in [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}. Define $w_1=1$ and, for $n>1$, $$\label{eq:witness}
 w_n:=L_{n,\lceil n/2\rceil}
           (w_{\lceil n/2\rceil}).$$ The lift is legal because $n\ge2\lceil n/2\rceil-1$, and Lemma [\[lem:section\]](#lem:section){reference-type="ref" reference="lem:section"} gives $P(w_n)=w_{\lceil n/2\rceil}$. Induction between consecutive powers of two now yields $\tau(w_n)=1+\tau(w_{\lceil n/2\rceil})=\lceil\log_2n\rceil$.

Theorem [\[thm:images\]](#thm:images){reference-type="ref" reference="thm:images"}, rather than the fibre formula below, is the primary axis: it proves both inclusions at every iterate and supplies a target-level inverse, not only an image census.

# A target-resolved one-step multiplicity

For $n>1$, a comparison word $w=w_1\cdots w_{n-1}\in\{U,D\}^{n-1}$ records $U$ when $\pi_i<\pi_{i+1}$ and $D$ otherwise. Its endpoint-inclusive peak positions are $$\label{eq:peak-positions}
 \{1:w_1=D\}\ \cup\
 \{i:1<i<n,\ w_{i-1}=U,w_i=D\}\ \cup\
 \{n:w_{n-1}=U\}.$$ For $n=1$, the empty comparison word has the unique position as a peak.

Let $p_1<\cdots<p_m$ be the positions in [\[eq:peak-positions\]](#eq:peak-positions){reference-type="eqref" reference="eq:peak-positions"}. The adjacent-comparison poset has relations $$\label{eq:zigzag}
 i<_w i+1\quad(w_i=U),
 \qquad
 i+1<_w i\quad(w_i=D).$$ For $\sigma\in\mathfrak S_m$, adjoin the peak chain $$\label{eq:peak-chain}
 p_{\sigma^{-1}(1)}<p_{\sigma^{-1}(2)}<\cdots
 <p_{\sigma^{-1}(m)}$$ and denote the resulting poset by $Q(w,\sigma)$. Every base peak is maximal under [\[eq:zigzag\]](#eq:zigzag){reference-type="eqref" reference="eq:zigzag"}, so adjoining [\[eq:peak-chain\]](#eq:peak-chain){reference-type="eqref" reference="eq:peak-chain"} creates no cycle. Write $e(Q)$ for the number of linear extensions of $Q$.

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} For every $\sigma\in\mathfrak S_m$, $$\label{eq:fibre}
 |P^{-1}(\sigma)\cap\mathfrak S_n|
 =\sum_{\substack{w\in\{U,D\}^{n-1}\\
                   w\text{ has }m\text{ endpoint-inclusive peaks}}}
       e(Q(w,\sigma)).$$ If $m>\lceil n/2\rceil$, the sum and the fibre are both empty.

Fix $w$. A linear extension of $Q(w,\sigma)$, read from smaller to larger, assigns the ranks $1,\ldots,n$ to positions. Relations [\[eq:zigzag\]](#eq:zigzag){reference-type="eqref" reference="eq:zigzag"} force exactly the comparison word $w$, while [\[eq:peak-chain\]](#eq:peak-chain){reference-type="eqref" reference="eq:peak-chain"} forces the left-to-right peak-value word to standardize to $\sigma$. Conversely, a permutation with comparison word $w$ and extracted target $\sigma$ orders its positions by increasing value and gives one such linear extension. This is a bijection for each $w$. Every source permutation has a unique comparison word, so summing the disjoint classes proves [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. The rank boundary follows from [\[eq:packing\]](#eq:packing){reference-type="eqref" reference="eq:packing"}; the case $n=m=1$ has one empty word and one extension.

Formula [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} uses standard poset technology and is deliberately a secondary inverse atlas. It does not reclaim static pinnacle-set or admissible-order results.

# Exact audit and conclusion

An independent standard-library verifier enumerates every permutation through rank nine. It compares full iterate image *sets* through five steps, constructs a right section for every feasible target through rank eight, checks that [\[eq:witness\]](#eq:witness){reference-type="eqref" reference="eq:witness"} saturates every intermediate packing bound, and compares every target fibre through rank eight with an independent subset-DP linear-extension count. All $1{,}228{,}181$ exact assertions pass. Table [1](#tab:audit){reference-type="ref" reference="tab:audit"} is frozen counterexample pressure, not proof evidence.

::: {#tab:audit}
  $n$                      1   2   3    4     5     6      7       8        9
  ---------------------- --- --- --- ---- ----- ----- ------ ------- --------
  $|\mathfrak S_n|$        1   2   6   24   120   720   5040   40320   362880
  $|P(\mathfrak S_n)|$     1   1   3    3     9     9     33      33      153
  $\max\tau$               0   1   2    2     3     3      3       3        4

  : Exact source-rank profile.
:::

Repeated endpoint-peak extraction therefore has a complete rank geometry: packing gives every upper boundary, and explicit lifts fill every rank below it. The same lifts provide equality witnesses for the sharp clock, while the comparison-poset sum resolves one-step multiplicities target by target.

# Limitations {#limitations .unnumbered}

The theorem uses positive permutations, boundary value zero, and standardization after each extraction. Different endpoint conventions, words with ties, cyclic peaks, or unstandardized value dynamics are outside scope. Ji's exact-convention static distributions, Fu's one-sided exterior- peak distributions, ordinary pinnacle theory under the padding bridge, run-sorting equidistribution, and generic zigzag-poset methods receive zero contribution credit. The primary-source audit was bounded, and no novelty or priority claim is made. Finite enumeration cannot replace the proofs. The manuscript remains under `HOLD_EXTERNAL`.

# Data Availability {#data-availability .unnumbered}

No external data were used. The anonymous artifact contains the standard-library verifier and frozen exact output. External release of the artifact is not authorized at this stage.

# Ethics Statement {#ethics-statement .unnumbered}

The work uses no human participants, animals, personal data, or deployed decision system.

# Author Contributions {#author-contributions .unnumbered}

Contributor identities are withheld for anonymous review. The anonymous author team takes responsibility for conceptualization, formal analysis, software, validation, and writing.

# Conflict of Interest {#conflict-of-interest .unnumbered}

The authors declare no known conflict of interest relevant to this internal mathematical study.

# Funding {#funding .unnumbered}

No funding claim is made in this anonymous internal draft.
