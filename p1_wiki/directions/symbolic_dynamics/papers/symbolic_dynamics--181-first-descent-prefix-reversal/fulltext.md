---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--181-first-descent-prefix-reversal"
canonical_tex: "symbolic_dynamics/papers/181-first-descent-prefix-reversal/main.tex"
canonical_pdf: "symbolic_dynamics/papers/181-first-descent-prefix-reversal/main.pdf"
source_sha256: "95909031cae2c75f09399452a472597e72a1bf3a91d10cf4286df54e54e2fb82"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Complete Depth-Two Atlas for First-Descent Prefix Reversal

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/181-first-descent-prefix-reversal>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/181-first-descent-prefix-reversal/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/181-first-descent-prefix-reversal/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/181-first-descent-prefix-reversal/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/181-first-descent-prefix-reversal/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Given a nonidentity permutation, locate its first descent and reverse the prefix ending at the descent's smaller follower. We determine the complete functional graph of this autonomous map. Its image is the half of $\mathfrak S_n$ beginning with an ascent. For $n\ge3$, the recurrent set is the identity together with the $n!/3$ permutations having a peak at position two; the latter form $n!/6$ two-cycles. Every tail has length at most two, with exact populations $n!/3+1,n!/2,n!/6-1$. The full predecessor set of a target is indexed by the decreasing run starting at its second position. Consequently, for $n\ge4$ the maximum fibre is $n-1$, attained at exactly $n-1$ targets. The exceptional $n=1,2,3$ atlases are explicit. Arbitrary prefix reversal, pancake sorting, descent counts, and finite-map bookkeeping are treated as background. The residual conjunction is [owner\_amber]{.smallcaps}, and external circulation is [hold\_external]{.smallcaps}.
author:
- Anonymous
bibliography:
- references.bib
title: |
  A Complete Depth-Two Atlas for\
  First-Descent Prefix Reversal
```

## Markdown 正文

# The autonomous rule and theorem package

Fix $n\ge1$. For $1\le k\le n$, let $\rho_k$ reverse the first $k$ entries of a permutation: $$\label{eq:prefix-reversal}
 \rho_k(\pi_1\cdots\pi_k\pi_{k+1}\cdots\pi_n)
 =\pi_k\cdots\pi_1\pi_{k+1}\cdots\pi_n.$$ Write $\iota=12\cdots n$. If $\pi\ne\iota$, let $$\label{eq:first-descent}
 d(\pi)=\min\{i: \pi_i>\pi_{i+1}\}$$ and define the first-descent prefix-reversal map $$\label{eq:map}
 F_n(\iota)=\iota,\qquad
 F_n(\pi)=\rho_{d(\pi)+1}(\pi)\quad(\pi\ne\iota).$$ The extra position after the first descent is part of the rule.

Prefix reversal and its pancake-sorting distance are classical [@GatesPapadimitriou1979]; prefix-reversal sorting on fixed-alphabet strings is also established [@HurkensEtAl2007]. Pudwell and Smith study four shuffle maps selected by a cut after the longest increasing prefix [@PudwellSmith2024], but those maps do not reverse the full prefix in [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}. We assign arbitrary prefix reversal, pancake graphs and distances, longest-increasing-prefix selection, elementary descent and peak counts, and generic finite-map bookkeeping no contribution credit.

There is also a sharp negative control. The rule called "First Sort" in Project Euler Problems 523--524 moves the follower $\pi_{d+1}$ to the front; it does not reverse the selected prefix.[^1] For example, it sends $1324$ to $2134$, whereas [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} sends $1324$ to $2314$. We therefore do not use "First Sort" as a name for $F_n$.

For $n\ge3$, set $$\label{eq:sets}
 \mathcal I_n=\{\tau\in\mathfrak S_n:\tau_1<\tau_2\},\qquad
 \mathcal P_n=\{\tau\in\mathfrak S_n:\tau_1<\tau_2>\tau_3\},\qquad
 \mathcal R_n=\{\iota\}\cup\mathcal P_n.$$ Let $\mu(\pi)$ be the distance from $\pi$ to the recurrent set of $F_n$. For $\tau\in\mathcal I_n$, let $$\label{eq:run}
 r(\tau)=\max\{r:1\le r\le n-1,
                  \ \tau_2>\tau_3>\cdots>\tau_{r+1}\},$$ where the condition is empty when $r=1$.

[\[thm:main\]]{#thm:main label="thm:main"} For every $n\ge3$, the following hold.

(i) The image is exactly $\mathcal I_n$, and $|\mathcal I_n|=n!/2$.

(ii) The recurrent set is exactly $\mathcal R_n$. The identity is fixed, while the $n!/3$ states in $\mathcal P_n$ form $n!/6$ disjoint two-cycles under $\rho_3$.

(iii) Every tail has length at most two, and $$\label{eq:tail-census}
       \#\{\mu=0\}=\frac{n!}{3}+1,\qquad
       \#\{\mu=1\}=\frac{n!}{2},\qquad
       \#\{\mu=2\}=\frac{n!}{6}-1.$$

(iv) A target outside $\mathcal I_n$ has no predecessor. For $\tau\in\mathcal I_n$, the complete set of distinct predecessors is $$\label{eq:fibre-set}
      F_n^{-1}(\tau)=
      \{\rho_k(\tau):2\le k\le r(\tau)+1\}
      \mathbin{\cup}
      \begin{cases}\{\iota\},&\tau=\iota,\\ \varnothing,&\tau\ne\iota.
      \end{cases}$$ Consequently, $$\label{eq:fibre-size}
                  |F_n^{-1}(\tau)|=r(\tau)+\mathbf1_{\{\tau=\iota\}}.$$

(v) For $n\ge4$, the maximum fibre size is $n-1$. Its complete maximizing set is $$\label{eq:maximizers}
     \mathcal M_n=\{\tau\in\mathfrak S_n:\tau_2=n,
                  \ \tau_2>\tau_3>\cdots>\tau_n\},
     \qquad |\mathcal M_n|=n-1.$$ For $n=3$, the maximum remains $2=n-1$, but the identity is one additional maximizer beyond the two states in [\[eq:maximizers\]](#eq:maximizers){reference-type="eqref" reference="eq:maximizers"}.

The five conclusions can be read at a glance as follows.

  ----------------------------------------------------------------------------------------------------------------------------------------------
  object              exact description
  ------------------- --------------------------------------------------------------------------------------------------------------------------
  image               $\tau_1<\tau_2$; population $n!/2$

  recurrent core      $\{\iota\}\cup\{\tau_1<\tau_2>\tau_3\}$; one fixed point and $n!/6$ two-cycles

  tail populations    $n!/3+1$, $n!/2$, $n!/6-1$ at depths $0,1,2$

  target fibre        decreasing-run reversals in [\[eq:fibre-set\]](#eq:fibre-set){reference-type="eqref" reference="eq:fibre-set"}

  maximum, $n\ge4$    size $n-1$ at the $n-1$ targets in [\[eq:maximizers\]](#eq:maximizers){reference-type="eqref" reference="eq:maximizers"}
  ----------------------------------------------------------------------------------------------------------------------------------------------

# Half-image and recurrent core

If $d=d(\pi)$, the first two entries of $F_n(\pi)$ are $\pi_{d+1}<\pi_d$. Thus every nonfixed output begins with an ascent; so does $\iota$. Hence $\operatorname{im}F_n\subseteq\mathcal I_n$.

Conversely, take $\tau\in\mathcal I_n$ and put $\pi=\rho_2(\tau)$. The first comparison of $\pi$ is the descent $\tau_2>\tau_1$, so $F_n(\pi)=\rho_2(\pi)=\tau$. This proves equality. Swapping the first two entries is a fixed-point-free involution pairing permutations in $\mathcal I_n$ with those beginning with a descent, and therefore $|\mathcal I_n|=n!/2$.

For $\tau\in\mathcal P_n$, the first descent is at position two. Hence $F_n(\tau)=\rho_3(\tau)$. The new first three entries are $\tau_3<\tau_2>\tau_1$, so the image is again in $\mathcal P_n$; applying $\rho_3$ once more returns to $\tau$. The two states are distinct because their first and third entries cannot agree.

Now let $\tau\in\mathcal I_n\setminus\mathcal R_n$. Since it is neither a peak at two nor the identity, its first three entries increase and its first descent occurs at some $d\ge3$. The first three entries of $F_n(\tau)$ are $$\label{eq:new-peak}
              \tau_{d+1}<\tau_d>\tau_{d-1},$$ so $F_n(\tau)\in\mathcal P_n$. Every state first enters $\mathcal I_n$ by part (i), and every image state then lies in or enters $\mathcal R_n$. This proves that no other cycle exists.

Among the six relative orders of the first three entries, exactly two put their maximum in the middle. Each order occurs for $n!/6$ permutations, so $|\mathcal P_n|=n!/3$. Pairing by $\rho_3$ gives $n!/6$ two-cycles.

# Target fibres and exact tail census

[\[lem:fibre\]]{#lem:fibre label="lem:fibre"} For $\tau\in\mathcal I_n$ and $2\le k\le n$, the state $\rho_k(\tau)$ has first descent at position $k-1$ if and only if $k\le r(\tau)+1$. These valid states are distinct as $k$ varies.

The first $k$ entries of $\rho_k(\tau)$ are $$\label{eq:inverse-word}
             \tau_k,\tau_{k-1},\ldots,\tau_2,\tau_1.$$ They increase through position $k-1$ precisely when $\tau_2>\tau_3>\cdots>\tau_k$. The next comparison is then the descent $\tau_2>\tau_1$, which holds because $\tau\in\mathcal I_n$. This condition is equivalent to $k\le r(\tau)+1$. Different $k$ give different first entries $\tau_k$, proving distinctness.

Part (i) excludes predecessors for targets outside $\mathcal I_n$. Suppose $\tau\in\mathcal I_n$. Every nonfixed predecessor $\pi$ has some first descent $d$ and satisfies $\tau=\rho_{d+1}(\pi)$; since prefix reversal is an involution, $\pi=\rho_{d+1}(\tau)$. Lemma [\[lem:fibre\]](#lem:fibre){reference-type="ref" reference="lem:fibre"} gives exactly the values $2\le d+1\le r(\tau)+1$, and it also proves the converse for every such value. The only fixed state is $\iota$, which contributes one further predecessor exactly when $\tau=\iota$. For that target, $\rho_2(\iota)$ is distinct from $\iota$, so [\[eq:fibre-size\]](#eq:fibre-size){reference-type="eqref" reference="eq:fibre-size"} follows.

Part (ii) gives the depth-zero population $n!/3+1$ and shows that every image state outside $\mathcal R_n$ has depth one. Such a state $\tau$ begins $\tau_1<\tau_2<\tau_3$, so $r(\tau)=1$. Lemma [\[lem:fibre\]](#lem:fibre){reference-type="ref" reference="lem:fibre"} says that its only predecessor is $\rho_2(\tau)$, which begins with a descent and lies outside $\mathcal I_n$. The map $$\label{eq:depth-two-bijection}
 \mathcal I_n\setminus\mathcal R_n\longrightarrow\{\pi:\mu(\pi)=2\},
 \qquad \tau\longmapsto\rho_2(\tau)$$ is therefore a bijection. Indeed, every depth-two state must map to a nonrecurrent image state, so the displayed construction also captures the reverse inclusion.

Using parts (i)--(ii), the depth-two population is $$\label{eq:depth-two-count}
 |\mathcal I_n|-|\mathcal R_n|=\frac{n!}{2}-\frac{n!}{3}-1
                 =\frac{n!}{6}-1.$$ All remaining states have depth one, giving $n!-(n!/3+1)-(n!/6-1)=n!/2$. This proves [\[eq:tail-census\]](#eq:tail-census){reference-type="eqref" reference="eq:tail-census"} and the absence of longer tails.

# Sharp fibres and the small boundaries

For a nonidentity image target, [\[eq:fibre-size\]](#eq:fibre-size){reference-type="eqref" reference="eq:fibre-size"} is at most $n-1$; the identity has fibre two. When $n\ge4$, equality can therefore occur only when $r(\tau)=n-1$, or equivalently $\tau_2>\tau_3>\cdots>\tau_n$. Since also $\tau_1<\tau_2$, the value $n$ cannot occupy the first position. It lies in the decreasing tail and must be its first, largest entry: $\tau_2=n$. Conversely, every target in [\[eq:maximizers\]](#eq:maximizers){reference-type="eqref" reference="eq:maximizers"} has the full run and hence fibre $n-1$. Choose $\tau_1$ arbitrarily from $[n-1]$; the remaining entries are then forced in decreasing order. This gives exactly $n-1$ maximizers.

At $n=3$, the two full-run targets still have fibre two, and the identity's extra fixed predecessor also gives fibre two. This is the stated exception.

[\[prop:small\]]{#prop:small label="prop:small"} At $n=1$, the sole arrow is $1\mapsto1$. Thus the image and recurrent set are both $\{1\}$, the sole state has depth zero, and its fibre has size one.

At $n=2$, the arrows are $12\mapsto12$ and $21\mapsto12$. Thus the image and recurrent set are both $\{12\}$, the depth populations are $(1,1)$, and $F_2^{-1}(12)=\{12,21\}$ is the unique maximum fibre.

At $n=3$, the full functional graph is $$\label{eq:n3-atlas}
 123\mapsto123,\qquad 132\leftrightarrow231,
 \qquad 213\mapsto123,\quad312\mapsto132,\quad321\mapsto231.$$ The image and recurrent populations are both three, the depth populations are $(3,3,0)$, and each image target has fibre two. Thus the three maximizers are $123,132,231$.

The $n=1$ claim is immediate. At $n=2,3$, applying [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} gives the listed arrows; the identity then has its fixed predecessor in addition to its two-prefix reversal. These direct calculations isolate the $n=1,2$ boundaries not covered by the $n\ge3$ recurrent count and the only tie not covered uniformly by the $n\ge4$ maximizer statement.

# Exact controls and claim boundary

The paper-local verifier reconstructs the full map, all incoming sets, and all orbit coordinates through $\mathfrak S_9$. It makes $6{,}273{,}070$ integer assertions, including complete checks of the five theorem contracts and the $n=1,2,3$ boundaries. It imports no scouting or earlier-paper code. These finite boxes are falsification pressure, not proofs or ownership evidence.

The nearest internal proof vocabulary is P122's deterministic permutation block reversal and target-local inverse cuts; that vocabulary receives zero separation credit. The killed follower-to-front spike is the Project Euler rule, not [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}. The retained owner-thin conjunction is the literal autonomous reversal together with its half-image, peak two-cycle core, depth census, and decreasing-run inverse atlas. A bounded search non-hit is not a novelty result. The gate remains [owner\_amber]{.smallcaps}, and the external lifecycle remains [hold\_external]{.smallcaps}.

[^1]: Official statements: <https://projecteuler.net/problem=523> and <https://projecteuler.net/problem=524>.
