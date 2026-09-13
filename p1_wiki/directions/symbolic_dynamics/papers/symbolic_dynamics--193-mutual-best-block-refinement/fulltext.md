---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--193-mutual-best-block-refinement"
canonical_tex: "symbolic_dynamics/papers/193-mutual-best-block-refinement/main.tex"
canonical_pdf: "symbolic_dynamics/papers/193-mutual-best-block-refinement/main.pdf"
source_sha256: "0d5b35e1b535e9cdad684cc78ce45ea6f9a442bb643347b0dbc356bef8a37b19"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Mutual-Best Block Refinement on Permutations: Recursive Clocks, Depth Layers, and Exact Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/193-mutual-best-block-refinement>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/193-mutual-best-block-refinement/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/193-mutual-best-block-refinement/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/193-mutual-best-block-refinement/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/193-mutual-best-block-refinement/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a permutation, let each position with a later smaller entry nominate the smallest such value, and let that value nominate its earliest earlier larger position. Simultaneously exchange every mutually nominating pair. We show that the selected pairs have an exact structural description: in every non-singleton direct-sum indecomposable block, exchange the first entry with the block minimum. The number of direct-sum components is then a strict Lyapunov statistic. A recursive decomposition height gives the pointwise absorption time, whose maximum on $\mathfrak S_n$ is $n-1$ and is attained by exactly $(n-1)!$ permutations. Ordinary generating functions $A_t$ and $B_t$ for depth at most $t$, respectively without and with an indecomposability restriction, satisfy $$A_t=(1-B_t)^{-1},\qquad B_0=x,\qquad
   B_{t+1}=x+x^2A_tB_t'.$$ For a target with direct-sum component sizes $(c_1,\ldots,c_s)$, its complete one-step fibre is zero unless $c_1=1$, and otherwise equals $$c_s\prod_{\substack{2\le j\le s\\c_j=1}}(1+c_{j-1}).$$ Thus the image consists of the $(n-1)!$ permutations beginning in $1$, and the unique largest fibre is the identity fibre of size $2^{n-1}$. An exact standard-library verifier checks every source and target through $\mathfrak S_9$. Direct-sum decomposition, common-master blocking pairs, and generic finite-map bookkeeping receive no contribution credit. Direct ownership remains unresolved, so the manuscript is `OWNER_AMBER/HOLD_EXTERNAL`.
author:
- Anonymous
bibliography:
- references.bib
title: 'Mutual-Best Block Refinement on Permutations: Recursive Clocks, Depth Layers, and Exact Fibres'
```

## Markdown 正文

# The literal map and the subtraction boundary

Write permutations in one-line notation. For $\pi\in\mathfrak S_n$ and $i<j$, call $(i,j)$ an *active pair* when $$\begin{aligned}
 \pi_j&=\min\{\pi_\ell:\ell>i,\ \pi_\ell<\pi_i\},
 \label{eq:left-choice}\\
 i&=\min\{\ell:\ell<j,\ \pi_\ell>\pi_j\}.
 \label{eq:right-choice}\end{aligned}$$ The pair is considered only when the sets displayed in [\[eq:left-choice\]](#eq:left-choice){reference-type="eqref" reference="eq:left-choice"}--[\[eq:right-choice\]](#eq:right-choice){reference-type="eqref" reference="eq:right-choice"} are nonempty. Thus the left position nominates its smallest later smaller value, while that value nominates its earliest earlier larger position. All nominations are computed from the old permutation.

[\[def:map\]]{#def:map label="def:map"} Simultaneously exchange $\pi_i$ and $\pi_j$ for every active pair $(i,j)$, leaving all other entries in place. Denote the resulting permutation by $F_n(\pi)$.

The rule is literal and contains no scheduler. Its apparent matching language is optional. If men and women both use the common master order $1<\cdots<n$, and $\pi_i$ is the partner of man $i$, then blocking pairs are exactly inversions. Having each participant choose its best blocking partner gives [\[eq:left-choice\]](#eq:left-choice){reference-type="eqref" reference="eq:left-choice"}--[\[eq:right-choice\]](#eq:right-choice){reference-type="eqref" reference="eq:right-choice"}, and exchanging the two partners gives Definition [\[def:map\]](#def:map){reference-type="ref" reference="def:map"}. Stable matching and blocking pairs themselves are classical [@GaleShapley1962]. Schipper and Zhang study a decentralized stochastic process that prioritizes one mutual optimal blocking pair [@SchipperZhang2025]; that process is not the simultaneous map here, but its mutual-best dynamics terminology is also assigned zero contribution credit. P193 fixes common master orders, computes all nominations from one old permutation, and exchanges every mutual pair in parallel. The matching wrapper receives no contribution credit.

We instead analyze the map through direct sums. For $\alpha\in\mathfrak
S_r$ and $\beta\in\mathfrak S_s$, their direct sum is $$\alpha\oplus\beta=
 (\alpha_1,\ldots,\alpha_r,\beta_1+r,\ldots,\beta_s+r).$$ A cut after position $r<n$ is a *sum cut* when $\{\pi_1,\ldots,\pi_r\}=[r]$. Every permutation has a unique factorization $$\label{eq:sum-factorization}
             \pi=\beta_1\oplus\cdots\oplus\beta_s$$ into sum-indecomposable permutations. These elementary permutation notions are standard background [@Bona2012; @Stanley2011EC1] and also receive zero credit.

For example, $23154=231\oplus21$. Its active pairs, in one-based positions, are $(1,3)$ and $(4,5)$, so $$23154\longmapsto13245.$$

# Block surgery and the exact clock

The first result removes both the matching vocabulary and any possible ambiguity about simultaneous exchanges.

[\[prop:block\]]{#prop:block label="prop:block"} In each non-singleton factor $\beta_r$ of [\[eq:sum-factorization\]](#eq:sum-factorization){reference-type="eqref" reference="eq:sum-factorization"}, the unique active pair consists of the first position of that block and the position of its minimum. Singleton factors have no active pair. Consequently the active pairs are disjoint, and $F_n$ acts by making these first--minimum exchanges in all non-singleton factors simultaneously. In particular, $$\label{eq:sum-compatible}
                  F(\alpha\oplus\beta)=F(\alpha)\oplus F(\beta).$$

There is no inversion between two different direct-sum factors, so an active pair cannot cross a sum cut. Standardization preserves all comparisons and nominations, and it therefore suffices to work in one indecomposable block $\beta\in\mathfrak S_m$.

If $m>1$, the minimum $1$ cannot be first, since that would create a sum cut after position one. The first position nominates $1$, and every entry before $1$ is larger than $1$, so $1$ nominates the first position. This gives one active pair.

Conversely, suppose $(i,j)$ is active and put $b=\beta_j$. By [\[eq:right-choice\]](#eq:right-choice){reference-type="eqref" reference="eq:right-choice"}, every position before $i$ contains a value below $b$. By [\[eq:left-choice\]](#eq:left-choice){reference-type="eqref" reference="eq:left-choice"}, no value below $b$ occurs after $i$; the entry $\beta_i$ itself is above $b$. Hence the first $i-1$ positions contain exactly the $b-1$ values $1,\ldots,b-1$, and so $i-1=b-1$. If $i>1$, this is a proper sum cut, contrary to indecomposability. Therefore $i=1$ and $b=1$. The description and disjointness now follow block by block, as does [\[eq:sum-compatible\]](#eq:sum-compatible){reference-type="eqref" reference="eq:sum-compatible"}.

Let $\operatorname{comp}(\pi)$ be the number of factors in [\[eq:sum-factorization\]](#eq:sum-factorization){reference-type="eqref" reference="eq:sum-factorization"}. If $\beta$ is non-singleton and indecomposable, Proposition [\[prop:block\]](#prop:block){reference-type="ref" reference="prop:block"} gives a unique $\gamma\in
\mathfrak S_{|\beta|-1}$ such that $$\label{eq:one-gamma}
                         F(\beta)=1\oplus\gamma.$$ Thus every changed block splits into at least two factors.

[\[cor:functional\]]{#cor:functional label="cor:functional"} If $F_n(\pi)\ne\pi$, then $$\operatorname{comp}(F_n(\pi))>\operatorname{comp}(\pi).$$ The identity is the unique fixed and recurrent state. Hence the functional graph consists of one rooted in-tree, with a loop at the identity and no other directed cycle.

We next refine this monotone statistic into a pointwise clock. For a word of distinct letters, let $\operatorname{std}$ denote standardization. Define the *selection-decomposition height* $h$ recursively by $$\begin{aligned}
 h(1)&=0,\label{eq:height-singleton}\\
 h(\beta)&=1+h(\gamma)
 &&\text{if $\beta$ is non-singleton indecomposable and
          $F(\beta)=1\oplus\gamma$},\label{eq:height-indec}\\
 h(\beta_1\oplus\cdots\oplus\beta_s)
   &=\max_{1\le r\le s}h(\beta_r).
 \label{eq:height-sum}\end{aligned}$$ When a factor occupies a translated alphabet, $h$ is applied after standardization. The recursion is well-founded because [\[eq:height-indec\]](#eq:height-indec){reference-type="eqref" reference="eq:height-indec"} lowers size.

[\[thm:clock\]]{#thm:clock label="thm:clock"} For every $\pi\in\mathfrak S_n$, the first time at which its orbit reaches the identity is exactly $$\tau(\pi)=h(\pi).$$ Moreover, $$\label{eq:max-tail}
                  \max_{\pi\in\mathfrak S_n}\tau(\pi)=n-1,$$ and exactly $(n-1)!$ permutations attain this maximum.

Equation [\[eq:sum-compatible\]](#eq:sum-compatible){reference-type="eqref" reference="eq:sum-compatible"} says that the factors evolve independently and simultaneously, so the absorption time of a direct sum is the maximum of the factor absorption times. For a non-singleton indecomposable factor, one epoch produces $1\oplus\gamma$; the leading singleton is thereafter inert, so its absorption time is one plus that of $\gamma$. This proves the pointwise formula by induction on size.

The same induction gives $h(\pi)\le n-1$. Equality is attained by $$\label{eq:witness}
                         \omega_n=(2,3,\ldots,n,1),$$ because it is indecomposable and its first update is $1\oplus\omega_{n-1}$.

Let $d_n$ count the states of depth $n-1$. Such a state must be indecomposable: if it had two or more factors, every factor would have size at most $n-1$ and hence depth at most $n-2$. Its image is therefore $1\oplus\gamma$, where $\gamma$ has the maximum depth $n-2$ in $\mathfrak S_{n-1}$ and is itself indecomposable. Lemma [\[lem:core-fibre\]](#lem:core-fibre){reference-type="ref" reference="lem:core-fibre"} below shows that $1\oplus\gamma$ has exactly $n-1$ indecomposable parents. Conversely, every such parent has depth $n-1$. Therefore $$d_n=(n-1)d_{n-1},\qquad d_1=1,$$ which yields $d_n=(n-1)!$.

# All transient layers

The recursive clock converts directly into a coefficient recurrence. Let $a_{n,t}$ be the number of permutations in $\mathfrak S_n$ of depth at most $t$, and let $b_{n,t}$ count only the sum-indecomposable ones. Include the empty permutation in the first class and define the ordinary formal series $$A_t(x)=\sum_{n\ge0}a_{n,t}x^n,
 \qquad
 B_t(x)=\sum_{n\ge1}b_{n,t}x^n.$$

[\[thm:layers\]]{#thm:layers label="thm:layers"} For every $t\ge0$, $$\label{eq:AB-recurrence}
 A_t(x)=\frac{1}{1-B_t(x)},\qquad B_0(x)=x,
 \qquad B_{t+1}(x)=x+x^2A_t(x)B_t'(x).$$ Consequently the exact depth-$t$ population in $\mathfrak S_n$ is $$\label{eq:exact-layer}
                    [x^n]\bigl(A_t(x)-A_{t-1}(x)\bigr),$$ where $A_{-1}(x)=1$.

Unique direct-sum factorization makes a permutation of depth at most $t$ a possibly empty sequence of indecomposable blocks of depth at most $t$. This proves $A_t=(1-B_t)^{-1}$. At depth zero, the only indecomposable permutation is the singleton, so $B_0=x$.

It remains to count non-singleton indecomposable blocks of depth at most $t+1$. By [\[eq:one-gamma\]](#eq:one-gamma){reference-type="eqref" reference="eq:one-gamma"}, each maps to $1\oplus\gamma$ with $h(\gamma)\le t$. Decompose nonempty $\gamma$ into an arbitrary prefix sequence of indecomposable blocks followed by its last block. If that last block has size $r$, Lemma [\[lem:core-fibre\]](#lem:core-fibre){reference-type="ref" reference="lem:core-fibre"} gives exactly $r$ indecomposable parents. The arbitrary prefix contributes $A_t$, while a last block marked with one of its $r$ positions contributes $xB_t'$. The new leading entry contributes another factor $x$. Adding the singleton gives $B_{t+1}=x+x^2A_tB_t'$. Subtracting cumulative classes proves [\[eq:exact-layer\]](#eq:exact-layer){reference-type="eqref" reference="eq:exact-layer"}.

For reference, the exact depth populations for $n=8$ are $$1,127,1064,3484,7614,11722,11268,5040$$ at depths $0,\ldots,7$. These numbers are consequences of Theorem [\[thm:layers\]](#thm:layers){reference-type="ref" reference="thm:layers"}, not hypotheses inferred from computation.

# The complete one-step inverse atlas

The inverse theorem rests on a local fact that also closed the deepest-state count. For nonempty $\gamma$, write $\lambda(\gamma)$ for the size of its last direct-sum indecomposable component.

[\[lem:core-fibre\]]{#lem:core-fibre label="lem:core-fibre"} For every $\gamma\in\mathfrak S_m$, exactly $\lambda(\gamma)$ sum-indecomposable permutations $\beta\in\mathfrak S_{m+1}$ satisfy $$F(\beta)=1\oplus\gamma.$$ They are obtained by exchanging the leading $1$ of $1\oplus\gamma$ with an entry whose position in $\gamma$ lies in its last indecomposable component.

Let the chosen position in $\gamma$ be $r$, and perform the stated exchange. For any prefix ending before the moved $1$, the value $1$ is absent, so that prefix cannot be a sum cut. For a prefix containing both exchanged entries, the set of values is unchanged from $1\oplus\gamma$; a proper sum cut there is equivalent to a sum cut of $\gamma$ at or after position $r$. No such cut exists precisely when $r$ belongs to the last indecomposable component. Thus exactly its $\lambda(\gamma)$ positions give indecomposable parents. Every indecomposable parent must arise in this way by Proposition [\[prop:block\]](#prop:block){reference-type="ref" reference="prop:block"}, proving completeness.

Let a target $\sigma$ have factorization $$\sigma=\delta_1\oplus\cdots\oplus\delta_s,
                \qquad c_j=|\delta_j|.$$

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} The target $\sigma\in\mathfrak S_n$ belongs to the image of $F_n$ if and only if $$c_1=1,
 \qquad\text{equivalently}\qquad \sigma_1=1.$$ For every target, including Garden-of-Eden states, $$\label{eq:fibre-product}
 |F_n^{-1}(\sigma)|=
 \begin{cases}
 c_s\displaystyle\prod_{\substack{2\le j\le s\\c_j=1}}
        (1+c_{j-1}),&c_1=1,\\[3mm]
 0,&c_1>1.
 \end{cases}$$ Hence $$\label{eq:image-size}
                         |\operatorname{im}F_n|=(n-1)!.$$ The maximum fibre size is $2^{n-1}$, and the identity is its unique maximizing target.

The image of each source component is either a singleton or, by [\[eq:one-gamma\]](#eq:one-gamma){reference-type="eqref" reference="eq:one-gamma"}, a permutation beginning with a singleton component. Hence any target in the image has $c_1=1$.

Conversely, suppose $c_1=1$. A source is reconstructed by grouping consecutive target components into source blocks. Each group must begin with a singleton target component, and this condition is sufficient by Lemma [\[lem:core-fibre\]](#lem:core-fibre){reference-type="ref" reference="lem:core-fibre"}. A group ending with target component $e$ has exactly $c_e$ indecomposable parents; this statement includes a singleton group, whose unique parent has weight $c_e=1$.

Besides the compulsory first group, a new group may begin before index $j\ge2$ exactly when $c_j=1$. If that boundary is chosen, the preceding group ends at $j-1$ and contributes $c_{j-1}$; if it is not chosen, it contributes no factor at that point. The final group always ends at $s$ and contributes $c_s$. Summing independently over all optional boundaries gives $$c_s\sum_{J\subseteq\{j\ge2:c_j=1\}}\prod_{j\in J}c_{j-1}
 =c_s\prod_{\substack{2\le j\le s\\c_j=1}}(1+c_{j-1}),$$ which proves [\[eq:fibre-product\]](#eq:fibre-product){reference-type="eqref" reference="eq:fibre-product"}. The image condition is now complete; there are $(n-1)!$ targets beginning with $1$, proving [\[eq:image-size\]](#eq:image-size){reference-type="eqref" reference="eq:image-size"}.

For the maximum, set $E=\{i<s:c_{i+1}=1\}$. The elementary inequalities $$1+c_i\le2^{c_i},\qquad c_s\le2^{c_s-1}$$ give $$|F_n^{-1}(\sigma)|
 \le2^{c_s-1+\sum_{i\in E}c_i}
 \le2^{n-1}.$$ Equality in the second bound forces $E=\{1,\ldots,s-1\}$; otherwise the positive size of an omitted component causes a strict exponent loss. Thus $c_2=\cdots=c_s=1$, while image membership already gives $c_1=1$. The target is therefore the identity. Its fibre formula is indeed $2^{n-1}$, completing the proof.

[\[cor:mass\]]{#cor:mass label="cor:mass"} For every $n\ge1$, $$\sum_{\sigma\in\mathfrak S_n}|F_n^{-1}(\sigma)|=n!.$$

The labelled fibres partition the source carrier $\mathfrak S_n$.

# Exact controls, internal separation, and limitations

The paper-local verifier exhausts every permutation through $\mathfrak S_9$. For each source it compares the literal active-pair set with the block-surgery set, follows the orbit, and compares its length with [\[eq:height-singleton\]](#eq:height-singleton){reference-type="eqref" reference="eq:height-singleton"}--[\[eq:height-sum\]](#eq:height-sum){reference-type="eqref" reference="eq:height-sum"}. For every target it compares literal indegree with [\[eq:fibre-product\]](#eq:fibre-product){reference-type="eqref" reference="eq:fibre-product"} before checking image size and mass. It also compares every coefficient of [\[eq:AB-recurrence\]](#eq:AB-recurrence){reference-type="eqref" reference="eq:AB-recurrence"} in the complete range. Selected boxes are shown in Table [1](#tab:controls){reference-type="ref" reference="tab:controls"}.

::: {#tab:controls}
    $n$    states    image   max tail   deepest   max fibre
  ----- --------- -------- ---------- --------- -----------
      4        24        6          3         6           8
      5       120       24          4        24          16
      6       720      120          5       120          32
      7     5,040      720          6       720          64
      8    40,320    5,040          7     5,040         128
      9   362,880   40,320          8    40,320         256

  : Complete author-side controls. "Deepest" counts all states at the displayed maximum tail. Enumeration is not used as proof.
:::

The local history firewall is literal rather than title-based. P105 deletes the least label from every nontrivial permutation cycle; its clock is the longest cycle length minus one. Here cycles are irrelevant and one-line direct-sum blocks are refined. For example, on $3412$, P105 produces the identity while the present map produces $1432$. P122 reverses parity-selected record blocks and reparses left-to-right maxima. P155 and P156 are rank-changing extraction maps, respectively using cycle maxima and weak excedances. None performs the first--minimum exchange inside every current sum-indecomposable block.

P181 is the most important same-carrier negative control. It locates one first descent and reverses the prefix through its smaller follower; it has a depth-two recurrent atlas with two-cycles. The present map instead performs many disjoint exchanges, strictly refines direct-sum components, and has one absorber with height $n-1$. The maps already disagree on $$132:\qquad F_{193}(132)=123,
 \qquad F_{181}(132)=231.$$ Their inverse mechanisms also differ: P181 uses decreasing-prefix runs, whereas [\[eq:fibre-product\]](#eq:fibre-product){reference-type="eqref" reference="eq:fibre-product"} sums compatible groupings of target direct-sum components. Shared use of minima, blocks, an $n-1$ scale, or permutation fibres earns no separation credit by itself.

This manuscript does not claim a closed nonrecursive expression for every depth layer, an all-time target fibre formula, an asymptotic limit law, or an external ownership result. The common-master matching interpretation and mutual-best blocking-pair dynamics, including sequential or stochastic one-pair satisfaction, are zero-credit background; so is direct-sum factorization. The retained object is the conjunction of the literal deterministic all-pair parallel update under fixed common orders, its strict adaptive block refinement, the pointwise recursive clock and layer recurrence, and the target-resolved product fibre. The direct-owner search is not complete: a bounded non-hit would not prove novelty, priority, or freedom to operate. The release state therefore remains `OWNER_AMBER/HOLD_EXTERNAL`.

# Declarations {#declarations .unnumbered}

#### Data and code.

No external dataset is used. A deterministic standard-library verifier and its exact replay instructions accompany the manuscript.

#### External status.

This anonymous Round-0 artifact is an internal mathematical draft. Posting, submission, and claims of novelty or priority are not authorized.
