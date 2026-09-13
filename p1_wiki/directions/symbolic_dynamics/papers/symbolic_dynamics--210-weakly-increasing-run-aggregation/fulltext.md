---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--210-weakly-increasing-run-aggregation"
canonical_tex: "symbolic_dynamics/papers/210-weakly-increasing-run-aggregation/main.tex"
canonical_pdf: "symbolic_dynamics/papers/210-weakly-increasing-run-aggregation/main.pdf"
source_sha256: "969ca0deb2fd004ccf04e833d210a1b6296130076261c1a81ea724c62c16255f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Weakly Increasing Run Aggregation: A Sharp Triangular Clock and the Full Image

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/210-weakly-increasing-run-aggregation>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/210-weakly-increasing-run-aggregation/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/210-weakly-increasing-run-aggregation/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/210-weakly-increasing-run-aggregation/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/210-weakly-increasing-run-aggregation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the sharp stabilization time and the full one-step image of a map on positive integer compositions. One update replaces every maximal weakly increasing run of old parts by its sum, with all runs chosen simultaneously. For total mass $N\ge1$, the largest number of nonfixed updates is $\max\{h\in\mathbb Z_{\ge0}:1+h(h+1)/2\le N\}$. Two linked inductions force triangular mass in a delayed merger, and a descending-prefix construction attains the bound for every mass, including all surplus values. For the inverse problem, the attained minimum first part of a feasible suffix gives a three-branch right-to-left image test. We use this test to construct an explicit weight-preserving bijection from the image to nonempty compositions into positive triangular numbers. The resulting counting sequence and its generating function are known; the contribution is the identification of this particular image class. A standard endpoint-partition formula records every one-step fibre as supporting bookkeeping. All proofs are self-contained. An exact verifier checks the complete $4{,}095$-state box of masses $1$ through $12$, as finite counterexample pressure only.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Weakly Increasing Run Aggregation:\
  A Sharp Triangular Clock and the Full Image
```

## Markdown 正文

# The map and its boundary

Let $\mathcal C_N$ be the set of ordered tuples $a=(a_1,\ldots,a_\ell)$ of positive integers with sum $N\ge1$. All mass parameters and indices below are integers. Split $a$ at every strict descent $a_j>a_{j+1}$, and replace each resulting segment by its total. The output $F(a)$ belongs to $\mathcal C_N$. Every comparison uses the *old* parts: a newly formed sum is not compared again during that update. For example, $$(3,2,1,1)\longmapsto(3,2,2)\longmapsto(3,4)\longmapsto(7).$$ Write $\tau(a)=\min\{t\ge0:F^{t+1}(a)=F^t(a)\}$ and $\mathcal I_N=F(\mathcal C_N)$. We prove two results: the sharp uniform bound $\tau(a)\le H(N)=\max\{h\ge0:1+h(h+1)/2\le N\}$, and a complete suffix criterion for $\mathcal I_N$ with an explicit bijection to triangular-part compositions. The first proof follows mergers across time; the second depends on the order of target parts, not just total mass.

Run detection and run aggregation are established constructions. Wiseman's equality-run sum and weakly increasing run-leader transformations [@wiseman2022runs; @wiseman2024leaders] illustrate the distinction:

  Operation          Segment rule                            Output on $(1,2)$
  ------------------ --------------------------------------- -------------------
  Equality-run sum   Equal adjacent parts                    $(1,2)$
  Weak-run leader    Weakly increasing parts; retain first   $(1)$
  $F$                Weakly increasing parts; sum            $(3)$

Nonidentity of these rules is not a novelty argument. In particular, coarsening, decreasing length and merger ancestry receive no contribution credit here. An earlier internal equality-run analysis proves a doubling mass clock; its generic ancestry mechanism is background. The oriented left-mass induction below is the additional step needed for a triangular clock. At mass $7$ the displayed orbit lasts three rounds, whereas the equality-run clock is two. This excludes only a same-total clock-preserving conjugacy, not arbitrary changes of carrier or adapters. The accompanying source audit identifies the frozen internal comparison and its proof.

Ribbon functions enumerate positive words by weakly increasing run lengths, and weighted run networks provide general transfer machinery [@gessel2019reciprocals; @zhuang2016runs; @gesselzhuang2019homomorphisms]. Run lengths are not the vector of run *masses* used here: substituting letter weights to record the total does not preserve the separate masses. Endpoint-refined transfers recover the usual inverse bookkeeping, to which we assign no separate novelty. Likewise, triangular-part composition counts and reset/increment descriptions are prior knowledge [@wilson1998triangular; @robbins2014polygonal]. Our structural claim is their exact connection to $\mathcal I_N$, proved in Sections [3](#sec:image){reference-type="ref" reference="sec:image"} and [4](#sec:coding){reference-type="ref" reference="sec:coding"}; it is not a new sequence or counting method.

# The sharp triangular clock

View a composition as consecutive intervals partitioning $N$ labelled unit cells. Mass means interval length. Every update coarsens this interval partition, so a deleted cut never returns. A block is *born in round $t$* if it combines at least two blocks when time $t-1$ becomes time $t$; an unchanged block retains its earlier identity.

The fixed points are exactly the strictly decreasing compositions. Indeed, all runs are singletons precisely in that case. Otherwise an update strictly decreases the number of parts, proving termination. To sharpen this generic bound, we first control the left side of a delayed cut.

[\[lem:leftmass\]]{#lem:leftmass label="lem:leftmass"} If a cut disappears in round $t\ge1$, its old left block has mass at least $t$. If $t\ge2$, its old right block was born in round $t-1$.

Positivity gives the mass bound for $t=1$. For $t\ge2$, let $A,B$ be the adjacent time-$(t-1)$ blocks at the disappearing cut, so $\lvert A\rvert\le\lvert B\rvert$. At time $t-2$, let $a$ be the rightmost parent of $A$ and $c$ the leftmost parent of $B$. Their boundary survived round $t-1$, hence $\lvert a\rvert>\lvert c\rvert$. If $B$ had not been born then, it would equal $c$, and $\lvert A\rvert\ge\lvert a\rvert>\lvert c\rvert=\lvert B\rvert$, a contradiction. Thus $B$ was born in round $t-1$. Its first internal cut had left block $c$ and disappeared in that round. Induction gives $\lvert c\rvert\ge t-1$; integrality now yields $\lvert A\rvert\ge\lvert a\rvert\ge\lvert c\rvert+1\ge t$. This proves both assertions.

[\[lem:birthmass\]]{#lem:birthmass label="lem:birthmass"} Every block born in round $t\ge1$ has mass at least $M_t=1+t(t+1)/2$.

A block born in round $1$ has at least two positive parents, so its mass is at least $2=M_1$. For $t\ge2$, take the first two parents $A_1,A_2$ of a new block. Their cut disappears in round $t$. Lemma [\[lem:leftmass\]](#lem:leftmass){reference-type="ref" reference="lem:leftmass"} gives $\lvert A_1\rvert\ge t$ and says that $A_2$ was born in round $t-1$. The induction hypothesis gives $\lvert A_2\rvert\ge M_{t-1}$. The parents are disjoint, so the new mass is at least $t+M_{t-1}=M_t$. Additional parents only increase it.

[\[thm:clock\]]{#thm:clock label="thm:clock"} For every $N\ge1$, $$\max_{a\in\mathcal C_N}\tau(a)
 = H(N):=\max\{h\in\mathbb Z_{\ge0}:1+h(h+1)/2\le N\}.$$ More generally, for every $h\ge1$ and $r\ge0$, the composition $(h,h-1,\ldots,1,1+r)$ has stabilization time exactly $h$.

If $\tau(a)=t\ge1$, its last nonfixed round creates a block, so Lemma [\[lem:birthmass\]](#lem:birthmass){reference-type="ref" reference="lem:birthmass"} gives $N\ge M_t$. This proves the upper bound. For the witness, after $j$ updates, $1\le j\le h$, the state is $$\label{eq:witness}
 \bigl(h,h-1,\ldots,j+1,\;r+1+j(j+1)/2\bigr),$$ where the prefix is empty for $j=h$. At the first update only the final pair $(1,1+r)$ merges. If [\[eq:witness\]](#eq:witness){reference-type="eqref" reference="eq:witness"} holds with $j<h$, its suffix mass is at least $j+1$, and every earlier old prefix pair is a strict descent. Exactly the last prefix block joins the suffix, giving the formula for $j+1$. Thus exactly $h$ nonfixed updates lead to a single part. This argument permits every surplus $r$, however large. For $N\ge2$ choose $h=H(N)$ and $r=N-M_h$; for $N=1$, the unique state $(1)$ has time zero.

# The complete image from an attained minimum {#sec:image}

A weakly increasing refinement of $s$ is a positive weakly increasing sequence with total $s$. The following decomposition supplies the inverse language; its ordinary segmentation argument is supporting infrastructure.

[\[lem:refinement\]]{#lem:refinement label="lem:refinement"} A composition maps to $s=(s_1,\ldots,s_m)$ if and only if it is a concatenation of weakly increasing refinements $\lambda_1,\ldots,\lambda_m$ of the target parts, with $\operatorname{last}(\lambda_i)>\operatorname{first}(\lambda_{i+1})$ for $i<m$. This segmentation is unique.

An output cut is an input cut at the same cumulative mass. The target therefore uniquely specifies every input segment. Under $F$ these segments are maximal weakly increasing runs, so the stated conditions are necessary. Conversely, those conditions make the segments exactly the maximal runs; their sums are the target parts.

Call a tuple of refinements of a target suffix *feasible* if its internal boundary descents hold. When it exists, let $r_i$ be the minimum first part among feasible refinements of the entire suffix $(s_i,\ldots,s_m)$. The finite minimum is attained; we make no interval claim about the set of possible first parts.

[\[thm:image\]]{#thm:image label="thm:image"} Set $r_m=1$ and scan right to left. Given $r=r_{i+1}$, use $$\label{eq:scan}
 \begin{cases}
 \text{fail},&s_i\le r,\\
 r_i=s_i,&s_i=r+1,\\
 r_i=1,&s_i\ge r+2.
 \end{cases}$$ Then $s\in\mathcal I_N$ if and only if the scan never fails. Every successful $r_i$ is the attained suffix minimum just defined. The test takes $O(m)$ integer comparisons.

The last part has an all-one refinement, so its minimum is $1$. Suppose the suffix to the right has attained minimum $r$. A new refinement must end at $b>c$ for some attainable right first part $c\ge r$. Necessarily $b\ge r+1$. Conversely, a refinement ending at least $r+1$ can be attached to a suffix attaining $r$.

If $s_i\le r$, no ending part can suffice. If $s_i=r+1$, a sufficient ending part uses the entire mass, forcing the singleton $(s_i)$ and minimum $s_i$. If $s_i\ge r+2$, the refinement $(1,s_i-1)$ is weakly increasing and has a sufficient ending part; it attains the absolute minimum $1$. These exhaustive cases prove the induction and construct a feasible preimage whenever the scan succeeds. Selecting a larger right first part cannot avoid failure. Lemma [\[lem:refinement\]](#lem:refinement){reference-type="ref" reference="lem:refinement"} completes the equivalence.

For example, $(2,3,2)$ passes and is the image of $(2,1,2,1,1)$, whereas $(2,2,3)$ fails with backward thresholds $1,2$. Equal total mass and equal multisets of target parts thus do not determine image membership. The complexity assertion counts integer comparisons, not bit operations independent of the sizes of the integers.

# A bijection with triangular-part compositions {#sec:coding}

Put $T_k=k(k+1)/2$ for $k\ge1$, and let $\mathcal T_N$ consist of the nonempty compositions of $N$ whose parts belong to $\{T_1,T_2,\ldots\}$. This class, its count and its reset/increment representations are known [@wilson1998triangular; @robbins2014polygonal]. We identify it with the image of $F$; the test, identification and counting consequence form one structural result.

[\[thm:coding\]]{#thm:coding label="thm:coding"} There is a weight-preserving bijection $\Phi:\mathcal I_N\to\mathcal T_N$ given by the following scan and inverse parsing.

Read a successful target from right to left. Its rightmost part $b\ge1$ initializes threshold $1$. From threshold $r$, a part $r+1$ increments the threshold and a part at least $r+2$ resets it to $1$. Consequently, after the rightmost part, there is a unique sequence of complete reset cycles $$\label{eq:cycle}
 2,3,\ldots,k,\;k+2+u\qquad(k\ge1,\ u\ge0)$$ followed by a unique terminal increment string $2,3,\ldots,k$ with $k\ge1$. A string is empty when $k=1$.

Start the encoded list with $b-1$ copies of $1$. For each complete cycle [\[eq:cycle\]](#eq:cycle){reference-type="eqref" reference="eq:cycle"}, in *scan order*, append $T_{k+1}$ followed by $u$ copies of $1$. Finally append $T_k$ for the terminal increment string. The list is nonempty and has triangular parts. A complete cycle has mass $(T_k-1)+(k+2+u)=T_{k+1}+u$, and the rightmost part together with the terminal string has mass $b+T_k-1=(b-1)+T_k$. Thus total mass is preserved.

For the inverse, reserve the last triangular part, uniquely $T_k$, for the terminal increment string. Parse the preceding list as an initial string of ones and then parts at least $3$, each followed by its maximal string of ones. This parse is unique since $1$ is the only positive triangular number smaller than $3$. If there are $b-1$ initial ones, begin a target read-list with $b$. Each subsequent triangular part is uniquely $T_{j+1}$, $j\ge1$; when followed by $u$ ones, append $2,3,\ldots,j,j+2+u$ to the read-list. Append $2,3,\ldots,k$ at the end, then reverse the read-list to obtain the target.

Every reconstructed cycle and terminal string passes [\[eq:scan\]](#eq:scan){reference-type="eqref" reference="eq:scan"}, so the inverse target belongs to $\mathcal I_N$. Its unique scan recovers the parsed pieces. Conversely, reserving the last triangular part recovers the terminal string, even if that part is $T_1=1$. These operations are mutually inverse, proving the bijection.

For instance, $(2,3,2)$ encodes as $(1,3,3)$: the rightmost $2$ supplies one initial $1$, the next $3$ is a reset, and the last $2$ is a terminal increment. A one-part target $(N)$ encodes as $N$ ones.

[\[cor:series\]]{#cor:series label="cor:series"} For $i_N=\lvert\mathcal I_N\rvert$ and $\Theta(z)=\sum_{k\ge1}z^{T_k}$, one has $$\sum_{N\ge1}i_Nz^N=\frac{\Theta(z)}{1-\Theta(z)}.$$ With the auxiliary convention $i_0=1$, this gives $i_N=\sum_{T_k\le N}i_{N-T_k}$ for $N\ge1$.

Theorem [\[thm:coding\]](#thm:coding){reference-type="ref" reference="thm:coding"} identifies each coefficient with the known triangular-part count. A list of exactly $q\ge1$ triangular parts has series $\Theta^q$, so summing gives the displayed identity. Taking off the first part gives the recurrence. These are formal series: every part has positive weight, hence every coefficient is finite and $\Theta(0)=0$. The auxiliary empty list does not enlarge the carrier.

# Supporting one-step fibre bookkeeping {#sec:fibres}

For positive $s,a,b$, let $P_s(a,b)$ count weakly increasing refinements of $s$ with first part $a$ and last part $b$. It is zero outside $1\le a\le b\le s$. Inside that range, $$\label{eq:partition}
 P_s(a,a)=\mathbf 1_{a\mid s},\qquad
 P_s(a,b)=[z^s]\frac{z^{a+b}}{\prod_{j=a}^b(1-z^j)}\quad(a<b).$$ The first formula counts an all-$a$ refinement. For the second, reserve one $a$ and one $b$, then choose arbitrary additional multiplicities of sizes $a$ through $b$. Their weakly increasing order is unique.

[\[prop:fibres\]]{#prop:fibres label="prop:fibres"} For every positive target $s=(s_1,\ldots,s_m)$, $$|F^{-1}(s)|=
 \sum_{\substack{1\le a_i\le b_i\le s_i\\1\le i\le m}}
 \left(\prod_{i=1}^mP_{s_i}(a_i,b_i)\right)
 \left(\prod_{i=1}^{m-1}\mathbf 1_{b_i>a_{i+1}}\right).$$

For fixed endpoints the first product counts the independent refinements; the second imposes exactly the boundary descents of Lemma [\[lem:refinement\]](#lem:refinement){reference-type="ref" reference="lem:refinement"}. Its unique segmentation prevents overcounting, and its converse gives every preimage. Empty fibres are included.

For finite evaluation, set $v_m(a)=\sum_bP_{s_m}(a,b)$ and then $$v_i(a)=\sum_bP_{s_i}(a,b)\sum_{c<b}v_{i+1}(c),\qquad
 |F^{-1}(s)|=\sum_a v_1(a).$$ This ordinary endpoint-partition transfer is included for reproducibility, with zero separate contribution credit. It does not assert a largest fibre or a formula for higher iterates.

# Exact checks and limitations

The paper-local standard-library verifier enumerates every positive composition of every mass $1\le N\le12$, exactly $4{,}095$ states. It records the full graph, depths, fixed points, all target fibres and their source sets, both birth inequalities on every orbit, all in-box surplus witnesses, every suffix minimum, and both coding directions on all image and triangular objects. Direct old-part run sums and a suffix endpoint-partition calculation are implemented without importing earlier pilot or reviewer code. The actual canonical image counts are $$1,1,2,3,4,7,11,16,25,40,61,94.$$ Finite checks pressure the proofs; they neither prove all-size statements nor enlarge the original experimental box.

The source audit deducts the occupied sum-coarsening carrier, equality-run ancestry, random pair genealogy, leftmost unit transfer and prefix-divisibility cut machinery. The paper remains in an existing run-coarsening family. The bounded inspected sources do not supply a complete adapter for the two retained results; this is not global priority or an exclusion of all possible adapters. The archived primary extraction of Robbins was read, including its recurrence proof; its extracted table reports $93$ at mass $12$, while the recurrence gives $94$. A failed screenshot does not certify printed typography. We use neither that table nor its asymptotic claims as validation, and preserve earlier retrieval failures in the source record.

No pointwise closed time formula, complete deepest-state classification, maximum-fibre theorem, all-time inverse or asymptotic theorem is claimed. The verifier uses no external data. This anonymous author draft has not passed the two manuscript reviews or terminal acceptance. Ownership remains `OWNER_AMBER`; posting, submission and specialist contact remain `HOLD_EXTERNAL`.
