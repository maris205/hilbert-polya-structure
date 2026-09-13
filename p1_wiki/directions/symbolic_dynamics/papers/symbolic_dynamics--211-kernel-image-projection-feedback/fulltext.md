---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--211-kernel-image-projection-feedback"
canonical_tex: "symbolic_dynamics/papers/211-kernel-image-projection-feedback/main.tex"
canonical_pdf: "symbolic_dynamics/papers/211-kernel-image-projection-feedback/main.pdf"
source_sha256: "49f4f14f1ac3475bc5218b09bac9b121e609c7bac906f17c706a80a435205e4e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Kernel--image projection feedback: a sharp clock and explicit fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/211-kernel-image-projection-feedback>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/211-kernel-image-projection-feedback/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/211-kernel-image-projection-feedback/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/211-kernel-image-projection-feedback/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/211-kernel-image-projection-feedback/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the dynamics and the complete one-step inverse of a kernel--image projection feedback on the nondecreasing self-maps of a finite chain. At each step, the map is replaced by the composition of the ceiling projection onto its right kernel endpoints and the ceiling projection onto its image completed by the top element. The supports are recomputed after every step, so the operation differs from taking powers of a fixed product of projections. After one update, persistent common endpoints separate alternating strict endpoint lists. Each further update removes the two outside endpoints of every such list. This gives the exact terminal projection and the entrance time of every state; the maximum entrance time on the full carrier is zero for a one-point chain and $\lceil n/2\rceil$ for every $n\ge2$. Independently, we describe every predecessor of each labelled target by ordered choices in explicitly determined gaps and obtain a finite Laurent-coefficient formula for its fibre, including all zero fibres. The contribution is confined to this recomputed dynamics and target-specific factorization; the underlying support coordinates and static projection structure are established background.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Kernel--image projection feedback:\
  a sharp clock and explicit fibres
```

## Markdown 正文

# The feedback operation and its scope

Replacing a map by canonical projections associated with its kernel and image gives a deterministic operation on maps, not just another composition in the underlying transformation monoid. We study that operation on the finite chain $[n]=\{1,\ldots,n\}$, where $n\ge1$. Let $\mathcal{O}_n$ be the set of all nondecreasing functions $[n]\to[n]$. No extensivity or condition $f(n)=n$ is imposed on the initial state.

Every $f\in\mathcal{O}_n$ has a unique representation $f=f_{Y,X}$ with $$X=\{x_1<\cdots<x_r=n\},\qquad
 Y=\{y_1<\cdots<y_r\},\qquad
 f(i)=y_j\quad(x_{j-1}<i\le x_j),$$ where $x_0=0$. Thus $X$ records the right endpoints of the kernel blocks and $Y=\mathop{\mathrm{im}}(f)$. For $S\subseteq[n]$ containing $n$, define the ceiling retraction $$\label{eq:ceiling}
 e_S(i)=\min\{s\in S:i\le s\}.$$ The feedback operation is $$\label{eq:update}
 T(f_{Y,X})=e_X\circ e_A,\qquad A=Y\cup\{n\}.$$ The right factor acts first. For the next update, both sets are extracted anew from the current whole function. Write $T^t$ for iteration of this operation. A state is recurrent if it lies on a cycle of $T$; its entrance time $\tau(f)$ is the least $t\ge0$ for which $T^t(f)$ is fixed, when such a time exists.

#### Published support structure.

These coordinates and retractions are established background. Stein [@stein2025order Section 5.1] gives the supports $f^*=e_X$ and $f^+=e_{Y\cup\{n\}}$. The paragraph following his Lemma 5.12 also explicitly gives the completed-support reconstruction: for $n\in X\cap A$, a corresponding source exists precisely when $|A|-|X|\in\{0,1\}$; it is unique, with $Y=A$ in the zero branch and $Y=A\setminus\{n\}$ in the one branch. We claim no new support parametrization, completion convention, rank condition or reconstruction at this level. Formula [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} asks instead about the dynamics of recomputing those supports.

#### Static products and version-specific neighbors.

The Catalan specialization in Andrenšek's April version [@andrensek2026endomorphismsv1 Section 4, Proposition 4.1, Theorem 4.4 and Lemma 4.6] describes floor retractions and criteria for a fixed pair's product to be idempotent. His August version [@andrensek2026homomorphismsv3 Theorem 3.6] gives the general directed-path criterion for products of idempotents in a Hecke--Kiselman monoid. The graph-generator content sets in these statements are not our kernel/image endpoint sets. The v1 Catalan theorem numbers are not v3 theorem numbers. Passing from floor to ceiling by order duality, or recognizing a static idempotent product, supplies no new contribution here. Nor is an encoding of monoid homomorphisms an inverse description for the feedback map [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}.

  Established ingredient                            Question addressed in this note
  ------------------------------------------------- ---------------------------------------------------------
  Completed supports and ranks $0,1$                Exact behaviour when the supports are recomputed
  Static retractions and idempotent-product tests   Pointwise entrance time and sharp full-carrier clock
  Validity of a source support pair                 All support pairs producing a specified labelled target

The results have two parts. First, we determine the complete one-step image, all recurrent states, every terminal projection and entrance time, and the sharp bound $\max_{f\in\mathcal{O}_n}\tau(f)=\lceil n/2\rceil$ for $n\ge2$. Second, we give a target-local predecessor bijection and a finite Laurent/binomial fibre formula. Their proofs use, respectively, alternating endpoint lists and ordered choices in free target gaps. Generic deletion is not a separate contribution; the precise recomputed normal form, initial-step accounting and target factorization are the bounded objects of this note. Section [2](#sec:image){reference-type="ref" reference="sec:image"} identifies the first image, Section [3](#sec:clock){reference-type="ref" reference="sec:clock"} proves the clock, and Section [4](#sec:inverse){reference-type="ref" reference="sec:inverse"} resolves the inverse.

# The first image and common anchors {#sec:image}

The following direct calculation is the common starting point for the temporal and inverse arguments. It is a supporting projection-product calculation, not an independent novelty claim about static retractions.

[\[lem:product\]]{#lem:product label="lem:product"} Let $X,A\subseteq[n]$ contain $n$, and write $e_X\circ e_A=f_{Z,W}$, with the sets in increasing order. Then $$\label{eq:image}
 w_i\le z_i<w_{i+1}\quad(1\le i<k),\qquad w_k=z_k=n,$$ where $k=|W|=|Z|$. Moreover, $$\label{eq:anchors}
 W\subseteq A,\qquad Z\subseteq X,\qquad W\cap Z=X\cap A.$$ A target $g=f_{Z,W}\in\mathcal{O}_n$ belongs to $T(\mathcal{O}_n)$ if and only if it satisfies [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}.

For each $z\in e_X(A)$, let $$B_z=\{a\in A:e_X(a)=z\},\qquad w_z=\max B_z.$$ The nonempty set $B_z$ is consecutive in the ordered set $A$. The kernel block with output value $z$ under $e_X\circ e_A$ is the union of the consecutive $e_A$-blocks indexed by $B_z$, so its right endpoint is $w_z$. Hence $Z=e_X(A)$, $W=\{w_z:z\in Z\}$, and $w_i\le z_i$. An element of $A$ giving the next output value cannot be at most $z_i$: since $z_i\in X$, its ceiling in $X$ would then be at most $z_i$. Consequently $z_i<w_{i+1}$. The shared top element gives $w_k=z_k=n$.

The first two containments in [\[eq:anchors\]](#eq:anchors){reference-type="eqref" reference="eq:anchors"} follow from the construction. If $c\in X\cap A$, then $e_X(c)=c$, and no $a>c$ can have ceiling $c$. Thus $w_c=c$, so $c\in W\cap Z$. Conversely, $W\cap Z\subseteq A\cap X$ by those containments. This proves the anchor identity.

Necessity of [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"} for $T(\mathcal{O}_n)$ now follows by taking $A=Y\cup\{n\}$. For sufficiency, suppose the target satisfies [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}. Take the source $f=f_{W,Z}$, whose kernel endpoints are $Z$ and image is $W$. Both sets contain $n$ and have $k$ elements. With $z_0=0$, the inequalities $z_{i-1}<w_i\le z_i$ give $e_Z(w_i)=z_i$. Distinct $w_i$ have distinct resulting values, so $T(f)=e_Z\circ e_W=f_{Z,W}=g$.

In particular, the first image lies in the extensive top-fixing submonoid, although the initial carrier in [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} is all of $\mathcal{O}_n$. This normalization step matters for the sharp full-carrier clock.

# Exact entrance times and a sharp clock {#sec:clock}

Let $g=f_{Z,W}\in T(\mathcal{O}_n)$. Call an equal pair $(c,c)$ in its ordered endpoint/value list an *anchor*. The last pair $(n,n)$ is an anchor. Before the first anchor and between consecutive anchors, the strict pairs have the form $$\label{eq:strictlist}
 w_1<z_1<w_2<z_2<\cdots<w_r<z_r<c,$$ where $c$ is the following anchor and the indices are local to this interval. Define $R(g)$ as the maximum number $r$ of strict pairs in one such list, allowing empty lists and setting $R(g)=0$ if there are no strict pairs.

[\[lem:peeling\]]{#lem:peeling label="lem:peeling"} Under one update of $T$, the anchors of $g$ persist exactly. The list [\[eq:strictlist\]](#eq:strictlist){reference-type="eqref" reference="eq:strictlist"} becomes $$\label{eq:peeling}
 (z_1,w_2),\ (z_2,w_3),\ldots,(z_{r-1},w_r),\ (c,c),$$ where only the final anchor remains if $r=0$ or $r=1$. The lists in different anchor intervals evolve independently.

For the source $g=f_{Z,W}$, the next support pair is $X=W$, $A=Z$, because $n\in Z$. Lemma [\[lem:product\]](#lem:product){reference-type="ref" reference="lem:product"} preserves their intersection. For $i<r$, the least member of $W$ not below $z_i$ is $w_{i+1}$. The two final labels $z_r$ and $c$ both have ceiling $c$ in $W$. Recomputing the rightmost kernel endpoints therefore gives precisely [\[eq:peeling\]](#eq:peeling){reference-type="eqref" reference="eq:peeling"}. If the list is empty, $c$ remains its own ceiling. Each anchor belongs to both supports and separates their ceiling intervals, so no selected label crosses an anchor. This proves the independence of the intervals as well as the update formula.

[\[thm:time\]]{#thm:time label="thm:time"} The fixed states and recurrent states of $T$ are exactly $e_C$ with $n\in C\subseteq[n]$. Every source $f=f_{Y,X}$ terminates at $$\label{eq:terminal}
 e_{X\cap(Y\cup\{n\})}.$$ For an image state $g$, its entrance time is $\tau(g)=R(g)$. For a general source, $$\label{eq:time}
 \tau(f)=
 \begin{cases}
 0,& f=e_C\text{ for some }n\in C\subseteq[n],\\
 1+R(T(f)),&\text{otherwise}.
 \end{cases}$$

By Lemma [\[lem:peeling\]](#lem:peeling){reference-type="ref" reference="lem:peeling"}, each nonempty list loses its first and last endpoints. After $t$ updates, a list initially containing $2r$ labels retains exactly its middle $2\max\{r-t,0\}$ labels, with their two endpoint roles alternating. Thus it disappears at exactly time $r$. At every earlier step a strict pair remains; that list changes because its two distinct outside endpoints are removed. Hence $g$ reaches an anchor-only state at exactly time $R(g)$.

An anchor-only state has $W=Z=C$ and is $e_C$, which is fixed by [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}. Every source reaches the image after one step, so all orbits stabilize and no nontrivial cycle exists. The anchors in that first image are $X\cap(Y\cup\{n\})$ by [\[eq:anchors\]](#eq:anchors){reference-type="eqref" reference="eq:anchors"}; they never change. This proves [\[eq:terminal\]](#eq:terminal){reference-type="eqref" reference="eq:terminal"}. A fixed initial source has entrance time zero. Every other source needs its initial step and then the exact remaining image-state time, proving [\[eq:time\]](#eq:time){reference-type="eqref" reference="eq:time"}.

[\[thm:sharp\]]{#thm:sharp label="thm:sharp"} For $H_n=\max_{f\in\mathcal{O}_n}\tau(f)$, $$H_1=0,\qquad H_n=\left\lceil\frac n2\right\rceil\quad(n\ge2).$$

A strict list of $r$ pairs uses $2r$ distinct labels below its following anchor. Therefore $R(g)\le\lfloor(n-1)/2\rfloor$ for every image state. Theorem [\[thm:time\]](#thm:time){reference-type="ref" reference="thm:time"} gives $H_n\le1+\lfloor(n-1)/2\rfloor=\lceil n/2\rceil$ for $n\ge2$.

For $n=2m+1\ge3$, take $$X=\{2,4,\ldots,2m,n\},\qquad
 Y=\{1,3,\ldots,2m-1,n\}.$$ The first image of $f_{Y,X}$ consists of the $m$ strict pairs $(1,2),(3,4),\ldots,(2m-1,2m)$ followed by $(n,n)$. The source is not fixed: its value at $1$ is $1$, whereas its successor's value there is $2$. Thus its entrance time is $1+m$.

For $n=2m\ge2$, take $$X=\{2,4,\ldots,2m\},\qquad Y=\{1,3,\ldots,2m-1\}.$$ Completing $Y$ by $n$ makes the last two second-projection values merge under $e_X$. The first image has $m-1$ strict pairs $(1,2),\ldots,(2m-3,2m-2)$ and the anchor $(n,n)$. Again the value at $1$ changes from $1$ to $2$, so the entrance time is $m$. This includes $m=1$: the first image is already the constant-2 projection. Finally, at $n=1$ the sole map is fixed.

# Every labelled-target predecessor {#sec:inverse}

The inverse problem fixes the whole target function, including its endpoint labels. Its solution is not a test involving an unknown source map: the following construction lists all sources directly from the target.

For a nonnegative integer $d$, define the finite Laurent polynomial $$\label{eq:gap_poly}
 P_d(u)=\sum_{\substack{a,b\ge0\\a+b\le d}}
             \binom{d}{a+b}u^{b-a}.$$ The notation $[u^j]Q(u)$ denotes the coefficient of $u^j$ in a Laurent polynomial $Q$.

[\[thm:inverse\]]{#thm:inverse label="thm:inverse"} A target $g=f_{Z,W}$ failing [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"} has no predecessor. Otherwise put $z_0=0$ and $$D_i=\{z_{i-1}+1,\ldots,w_i-1\},\qquad
 d_i=|D_i|=w_i-z_{i-1}-1\quad(1\le i\le k).$$ Every predecessor is obtained uniquely as follows.

1.  Start with $X=Z$ and $A=W$.

2.  In each $D_i$, select disjoint sets of extra $X$-sites and extra $A$-sites such that every selected $X$-site precedes every selected $A$-site. Sites not selected belong to neither set. Add no other sites outside these free gaps.

3.  Retain the choices with $\delta=|A|-|X|\in\{0,1\}$. Set $Y=A$ if $\delta=0$ and $Y=A\setminus\{n\}$ if $\delta=1$. The reconstructed source is $f_{Y,X}$.

In particular, $$\label{eq:fibre}
 |T^{-1}(g)|=\bigl([u^0]+[u^1]\bigr)
                    \prod_{i=1}^{k}P_{d_i}(u).$$

The zero-fibre assertion is Lemma [\[lem:product\]](#lem:product){reference-type="ref" reference="lem:product"}. Suppose the image condition holds and $T(f_{Y,X})=g$, with $A=Y\cup\{n\}$. The product calculation forces $z_i\in X$ and $w_i\in A$. For every strict pair $w_i<z_i$, it also forces $$\label{eq:forbidden}
 X\cap[w_i,z_i)=\varnothing,\qquad
 A\cap(w_i,z_i]=\varnothing.$$ The first condition is necessary for $e_X(w_i)=z_i$. For the second, an extra $a\in A$ with $w_i<a\le z_i$ would also have ceiling $z_i$, contradicting that $w_i$ is the final domain endpoint of that output block. These prohibitions, the forced endpoints and the $D_i$ partition all sites of $[n]$.

A free site cannot belong to both supports, because the identity $X\cap A=W\cap Z$ would give a further target anchor. In $D_i$, no selected $A$-site may precede a selected $X$-site. Indeed, if $a<x$ with $a\in A$, $x\in X$ and both in $D_i$, then $$z_{i-1}<a\le e_X(a)\le x<w_i\le z_i.$$ The extra value $e_X(a)$ lies strictly between two consecutive target values, a contradiction. Thus the ordered-colour condition is necessary.

It is also sufficient. Make any choices in the stated free gaps and include the forced endpoints. Every selected $A$-site in $(z_{i-1},w_i]$ lies after all extra $X$-sites in that gap and has ceiling exactly $z_i$ in $X$. Its last such site is $w_i$. The product $e_X\circ e_A$ therefore has precisely the prescribed values $z_i$ and kernel endpoints $w_i$, and equals $g$.

It remains to impose the source-rank condition. The forced sets $Z,W$ have the same size, even when they meet at an anchor. If $a_i,b_i$ extra sites of the two respective colours are chosen in $D_i$, then $$|A|-|X|=\sum_{i=1}^{k}(b_i-a_i).$$ We now use the published completed-support reconstruction [@stein2025order Section 5.1, after Lemma 5.12]: the allowed differences are zero and one, recovering $Y=A$ and $Y=A\setminus\{n\}$, respectively. This support-rank fact is not a new part of the inverse theorem. In the one branch, $|A|=|X|+1\ge2$, so removing $n$ does not produce an empty image. Each retained pair gives exactly one source, and the necessity argument recovers its unique gap description.

For fixed $a_i,b_i$, choose $a_i+b_i$ positions of $D_i$; their first $a_i$ positions must have colour $X$ and their last $b_i$ colour $A$. There are exactly $\binom{d_i}{a_i+b_i}$ choices. The Laurent weight records their contribution $b_i-a_i$ to the rank difference. Independent gap choices multiply, and selecting the zero and one coefficients gives [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. This count and the full decoder use no temporal theorem.

Empty gaps cause no exception: $P_0(u)=1$ and contribute no extra sites. At $n=1$, the sole target has $d_1=0$, so the formula gives its single predecessor. Formula [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} is a finite target-specific evaluation; no maximization over targets is asserted.

# Verification design and limitations

The proofs establish the all-$n$ claims without enumeration. The accompanying standalone author verifier enumerates every member of $\mathcal{O}_n$ for $1\le n\le7$, a total of $2353$ maps. It constructs literal successors and whole-function orbits, then compares them with the image condition, terminal/entrance formulas and sharp witnesses. For every labelled target, it compares the complete observed predecessor list with the gap decoder and the Laurent count. Its full output records all sources and targets, including zero fibres, with explicit canonical ordering. Such finite checks pressure the proofs but cannot prove their all-size statements.

The new verifier has completed one initial production and a separately recorded strict author replay pair. Each invocation checked $14523$ predicates over the same $2353$ maps. The complete initial stdout was adopted as the canonical; three native comparisons checked each replay against that canonical and the two replays against one another. These are supporting finite checks, not additional proofs or independent manuscript reviews; the execution milestone supplies neither a manuscript build nor review acceptance. An earlier exploratory author pilot remains separate: its strict runtime-prelock audit failed and its archived output is not reused as the canonical or as strict manuscript verification. The new initial production and pair have separately recorded source, parameter and bounded runtime-closure evidence.

The scope is the exact clock and one-step inverse of [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}. We do not determine a global maximum fibre or its maximizers, basin cardinalities, or all-time inverse sets. The cited support/rank structure, static projection criteria and generic deletion are not new results. Our comparison with those sources is bounded to their stated objects; it is not a proof excluding every possible owner, factor, lift or transfer. The short note supplies explicit formulas for this recomputed operation, not a broader classification of finite semigroup feedback systems.
