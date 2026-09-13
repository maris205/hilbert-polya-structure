---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--155-cycle-maximum-extraction"
canonical_tex: "symbolic_dynamics/papers/155-cycle-maximum-extraction/main.tex"
canonical_pdf: "symbolic_dynamics/papers/155-cycle-maximum-extraction/main.pdf"
source_sha256: "11d9defc5f014d5c5b5cba3db860da214169dcdcb07cdf55595563a59cdb81ee"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Cycle-Maximum Extraction on Permutations: Exact Images and Weighted Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/155-cycle-maximum-extraction>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/155-cycle-maximum-extraction/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/155-cycle-maximum-extraction/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/155-cycle-maximum-extraction/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/155-cycle-maximum-extraction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Write a permutation as disjoint cycles, order the cycle supports by their least elements, read their greatest elements, and standardize the resulting word. Iterating this rule gives a rank-changing map on the disjoint union of finite symmetric groups. For a target $\sigma\in\mathfrak S_m$, we prove that its least possible source rank is $$\mu(\sigma)=2m-\operatorname{rlmin}(\sigma),$$ and construct a source in every rank at least $\mu(\sigma)$. The proof is an explicit opener--closer schedule: precisely the right-to-left minima may use one coordinate simultaneously as a cycle minimum and maximum. Independently, we resolve every target fibre as a sum over ordered set partitions, with a block of size $b$ carrying weight $(b-1)!$. The only recurrent permutations are the identities, and every other step strictly lowers rank. Static cycle maxima, ordered-cycle conventions, and set-partition endpoint technology are treated as prior inputs. A deterministic audit executes $16{,}473{,}121$ exact assertions; it is counterexample pressure rather than proof. No sharp absorption clock is claimed.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Cycle-Maximum Extraction on Permutations:\
  Exact Images and Weighted Fibres
```

## Markdown 正文

# The map and its ownership boundary {#sec:map}

Let $\mathfrak S_n$ be the permutations of $[n]$ in functional notation. For $\pi\in\mathfrak S_n$, write $B_1,\ldots,B_m$ for the supports of its disjoint cycles, ordered so that $$\min B_1<\min B_2<\cdots<\min B_m.$$ For a word of distinct integers, $\operatorname{std}$ replaces its smallest letter by $1$, its next smallest by $2$, and so on. Define the *cycle-maximum extraction map* $$\label{eq:map}
 \mathsf C(\pi)=\operatorname{std}(\max B_1,\ldots,\max B_m)\in\mathfrak S_m.$$ On $\mathfrak S_{\le N}=\bigsqcup_{1\le n\le N}\mathfrak S_n$, this is a finite self-map. For example, the permutation with supports $$\{1,3,5\},\quad\{2,4\},\quad\{6\}$$ maps to $\operatorname{std}(5,4,6)=213$; cyclic order within a support is invisible to [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}.

The ingredients around [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} are mature and receive no contribution credit. Chen--Deng--Du--Stanley--Yan fix block minima and maxima in their crossing/nesting theory [@ChenDengDuStanleyYan2005]; Rubey--Stump preserve opener and closer configurations [@RubeyStump2009]; Mongelli explicitly orders cycles by increasing minima [@Mongelli2012]; and Andrews--Egge--Gawronski--Littlejohn use prescribed sets of cycle maxima [@AndrewsEggeGawronskiLittlejohn2011]. We therefore claim neither the endpoint language, the ordering convention, nor the elementary count of cyclic orders. The scope here is the exact inverse geometry of the literal map [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}: target-dependent image thresholds, all-rank sections, and target-resolved weighted fibres. The source search was bounded; a non-hit for the exact map is not evidence of novelty, priority, or clearance.

For $\sigma=\sigma_1\cdots\sigma_m$, let $\operatorname{rlmin}(\sigma)$ denote the number of indices $i$ such that $\sigma_i<\sigma_j$ for all $j>i$. Put $$\label{eq:mu}
 \mu(\sigma)=2m-\operatorname{rlmin}(\sigma).$$ For $n\ge m$, let $\mathcal P_n(\sigma)$ consist of the ordered set partitions $(B_1,\ldots,B_m)$ of $[n]$ satisfying $$\label{eq:support-class}
 \min B_1<\cdots<\min B_m,
 \qquad \operatorname{std}(\max B_1,\ldots,\max B_m)=\sigma.$$

[\[thm:main\]]{#thm:main label="thm:main"} For every $\sigma\in\mathfrak S_m$ and $n\ge m$:

1.  [\[it:image\]]{#it:image label="it:image"} $\sigma\in\mathsf C(\mathfrak S_n)$ if and only if $n\ge\mu(\sigma)$. The proof constructs a deterministic right section in every admissible rank.

2.  [\[it:fibre\]]{#it:fibre label="it:fibre"} The complete target fibre is $$\label{eq:fibre}
     |\mathsf C_n^{-1}(\sigma)|
     =\sum_{(B_1,\ldots,B_m)\in\mathcal P_n(\sigma)}
           \prod_{i=1}^m(|B_i|-1)!.$$ In particular, the sum is zero precisely below the threshold in [\[it:image\]](#it:image){reference-type="ref" reference="it:image"}.

3.  [\[it:recurrent\]]{#it:recurrent label="it:recurrent"} $\mathsf C(\pi)=\pi$ holds exactly for identity permutations. Every nonidentity step strictly lowers rank, so the recurrent states of $\mathfrak S_{\le N}$ are $\mathrm{id}_1,\ldots,\mathrm{id}_N$.

The image and fibre assertions are logically independent: the first resolves existence and least rank through endpoints, whereas the second retains all support choices and all cyclic orders.

# The endpoint schedule {#sec:image}

We first prove the lower bound in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}([\[it:image\]](#it:image){reference-type="ref" reference="it:image"}). Suppose $(B_1,\ldots,B_m)$ satisfies [\[eq:support-class\]](#eq:support-class){reference-type="eqref" reference="eq:support-class"}. If $B_i$ is a singleton, then for every $j>i$, $$\max B_j\ge\min B_j>\min B_i=\max B_i.$$ Thus $\sigma_i$ is a right-to-left minimum. At most $\operatorname{rlmin}(\sigma)$ supports are singletons; all remaining supports use at least two coordinates. Hence $$n=\sum_i|B_i|\ge\operatorname{rlmin}(\sigma)+
 2\bigl(m-\operatorname{rlmin}(\sigma)\bigr)=\mu(\sigma).$$

The reverse implication is constructive. Introduce formal opener and closer chains $$\label{eq:chains}
 O_1<\cdots<O_m,\qquad K_1<\cdots<K_m,$$ and pair $O_i$ with $K_{\sigma_i}$. An opener records $\min B_i$, while its paired closer records $\max B_i$. A simultaneous event $S_i=O_i=K_{\sigma_i}$ will encode a singleton.

[\[lem:schedule\]]{#lem:schedule label="lem:schedule"} There is a precedence-respecting endpoint word of length $2m-\operatorname{rlmin}(\sigma)$ in which $O_i$ and $K_{\sigma_i}$ are simultaneous exactly at the right-to-left minima of $\sigma$.

Let $i$ openers and $j$ closers have already been emitted, and continue while $i<m$ or $j<m$. If $i=m$, emit $K_{j+1}$; this is the forced final-closing phase. Otherwise $j<m$ as well, because an emitted closer requires its owner to have opened. Consider $O_{i+1}$ and $K_{j+1}$ and apply the following deterministic rule:

1.  if $i+1$ is a right-to-left-minimum position and $\sigma_{i+1}=j+1$, emit the simultaneous event $S_{i+1}$;

2.  otherwise, if the opener paired with $K_{j+1}$ has already appeared, emit $K_{j+1}$;

3.  otherwise emit $O_{i+1}$.

The rule cannot become stuck: the boundary branch exhausts all remaining closers after the last opener, and before then the third move is available whenever the first two are not.

It remains to show that every designated simultaneous event is reached. Let $i+1$ be a right-to-left-minimum position and put $v=\sigma_{i+1}$. Every value smaller than $v$ occurs at a position at most $i$. Its opener is therefore available before $O_{i+1}$, and the closer-priority rule exhausts $K_1,\ldots,K_{v-1}$ before opening $O_{i+1}$. The next closer is then $K_v$, so the first move applies. No other position is declared simultaneous. Starting from $2m$ formal endpoints and making exactly $\operatorname{rlmin}(\sigma)$ identifications gives the stated length.

Assign the integers $1,2,\ldots,\mu(\sigma)$ successively to the events in Lemma [\[lem:schedule\]](#lem:schedule){reference-type="ref" reference="lem:schedule"}. For each $i$, take the coordinates at $O_i$ and $K_{\sigma_i}$ as the endpoints of $B_i$; a simultaneous event gives a singleton. The opener chain orders the minima by $i$, and the closer chain orders the maxima by their values, so [\[eq:support-class\]](#eq:support-class){reference-type="eqref" reference="eq:support-class"} holds.

This construction also gives every larger source rank. Replacing a simultaneous event by adjacent separate opener and closer events adds one coordinate without changing either endpoint order. After all simultaneous events have been split, every support has two endpoints; further coordinates may be inserted strictly between the opener and closer of one support. Thus there is a support family in $\mathcal P_n(\sigma)$ for every $n\ge\mu(\sigma)$. To obtain a permutation, put any one cycle on each support---for instance, map its elements in increasing order cyclically. This proves Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}([\[it:image\]](#it:image){reference-type="ref" reference="it:image"}), including the asserted right sections.

For illustration, $\sigma=231$ has one right-to-left minimum, so $\mu(231)=5$. The supports of the permutation $$\pi=(4,5,3,1,2)$$ are $\{1,4\},\{2,5\},\{3\}$, and their maxima standardize to $231$. The lower bound shows that rank five is best possible.

The scheduler is algorithmic as well as existential. The inverse word $\sigma^{-1}$ identifies which block owns the next closer; a right-to-left scan marks the simultaneous positions. The three-case rule in Lemma [\[lem:schedule\]](#lem:schedule){reference-type="ref" reference="lem:schedule"} then emits a minimum schedule in linear time after these two scans. Splits and interior insertions give a deterministic section at any requested admissible rank.

[\[cor:image-count\]]{#cor:image-count label="cor:image-count"} Let $\genfrac{[}{]}{0pt}{}{m}{r}$ be the unsigned Stirling number of the first kind. Then $$\label{eq:image-count}
 |\mathsf C(\mathfrak S_n)|=
 \sum_{m=1}^n\ \sum_{r=\max(1,2m-n)}^m \genfrac{[}{]}{0pt}{}{m}{r}.$$ At the minimum source rank of a target, $$\label{eq:min-fibre}
 |\mathsf C_{\mu(\sigma)}^{-1}(\sigma)|
 =|\mathcal P_{\mu(\sigma)}(\sigma)|.$$

Right-to-left minima on $\mathfrak S_m$ have the unsigned first-kind Stirling distribution: inserting the largest letter either creates a distinguished record position or inserts into one of the existing gaps, giving the usual Stirling recurrence. The threshold $2m-r\le n$ now gives [\[eq:image-count\]](#eq:image-count){reference-type="eqref" reference="eq:image-count"}. This classical distribution receives no contribution credit; the corollary merely specializes the target threshold.

If $n=\mu(\sigma)$, equality in the singleton lower bound forces precisely the right-to-left-minimum blocks to have size one and every other block to have size two. Each factor in [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} is then either $0!$ or $1!$, so every feasible support family has weight one, proving [\[eq:min-fibre\]](#eq:min-fibre){reference-type="eqref" reference="eq:min-fibre"}.

For orientation, [\[eq:image-count\]](#eq:image-count){reference-type="eqref" reference="eq:image-count"} gives the first exact image sizes shown below.

::: {#tab:profile}
  $n$                              1   2   3   4    5    6    7     8     9     10
  ------------------------------ --- --- --- --- ---- ---- ---- ----- ----- ------
  $|\mathsf C(\mathfrak S_n)|$     1   2   4   8   17   39   96   253   706   2074

  : Exact literal profile used only as falsification pressure.
:::

# Weighted fibres and dynamics {#sec:fibre}

The support partition of a permutation is unique. Fix $(B_1,\ldots,B_m)\in\mathcal P_n(\sigma)$. On a labelled set $B_i$ of size $b_i$, there are $(b_i-1)!$ cyclic permutations: anchor one element and order the remaining $b_i-1$ elements around it. Cyclic orders on disjoint supports are independent, giving $\prod_i(b_i-1)!$ sources with this support family.

Conversely, a support family satisfying [\[eq:support-class\]](#eq:support-class){reference-type="eqref" reference="eq:support-class"}, equipped with one cyclic order on every block, determines a unique permutation, and [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} sends it to $\sigma$. Distinct support families or cyclic orders give distinct sources. Summing the disjoint classes proves [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}.

The rank of $\mathsf C(\pi)$ is the number of cycles of $\pi$. Equality with the source rank $n$ occurs only when all $n$ cycles are singletons, that is, only for $\pi=\mathrm{id}_n$. Identities are fixed. Every other orbit therefore strictly decreases in positive integer rank until it reaches an identity, so no other recurrent state exists.

# Exact control and declarations {#sec:control}

The accompanying standard-library verifier independently constructs the literal map through rank ten. It checks $4{,}037{,}913$ source states, the fixed/recurrent classification, $145{,}684$ target/rank image cells, $46{,}233$ minimum endpoint dynamic programs, $3{,}161$ explicit all-rank sections, and $53{,}218$ fibre cells through source rank eight. Restricted-growth words generate the support side of [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}; literal permutations generate the other side. The frozen run has $16{,}473{,}121$ exact assertions and ends in `PASS`. Enumeration is used only to look for counterexamples and implementation errors; the proofs above are all-parameter arguments.

#### Limitations.

The paper treats only the literal map [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}. It neither classifies absorption times nor proves a sharp global clock. Exact enumeration through rank ten gives finite maximum tails $0,1,2,2,3,3,3,3,4,4$, suggesting a power-of-two pattern, but this is an open computational observation only: no all-parameter bound, pointwise clock, or global minimum-rank theorem for iterated preimages is asserted. Static endpoint and cycle statistics are fully subtracted, and the bounded direct-map search is not a novelty or priority claim. No conclusion is offered for other rules that choose representatives from cycles.

#### Data availability.

All exact-control source code and its frozen text transcript are included in the accompanying internal artifact. They use no external data, runtime network access, random sampling, or nonstandard Python package.

#### Ethics statement.

This mathematical study involves no human participants, animals, personal data, or field intervention.

#### Author contributions.

The anonymous author is responsible for the definitions, proofs, software, source audit, and manuscript.

#### Conflict of interest.

The author declares no conflict of interest.

#### Funding.

No external funding is declared.
