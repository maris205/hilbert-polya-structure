---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--201-eventual-period-feedback"
canonical_tex: "symbolic_dynamics/papers/201-eventual-period-feedback/main.tex"
canonical_pdf: "symbolic_dynamics/papers/201-eventual-period-feedback/main.pdf"
source_sha256: "d29d83fe43b92d17403c5697a4265bdbaa513031bb02aa6e4913b4f796078797"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Sharp Rank Thresholds, Critical Extremizers,\newline and Fibres of Eventual-Period Feedback

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/201-eventual-period-feedback>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/201-eventual-period-feedback/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/201-eventual-period-feedback/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/201-eventual-period-feedback/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/201-eventual-period-feedback/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a function on the labels $0,\ldots,n-1$, replace its value at each vertex by the length of the eventual cycle reached from that vertex, minus one. Iterating this operator, rather than repeatedly composing a fixed function, always reaches the constant-zero function. We determine the sharp rank needed to have height at least $h$: the thresholds satisfy $N_2=2$ and $N_{h+1}=N_h(N_h+1)/2$. Every threshold is attained by an explicit permutation, and the resulting bound is sharp at every rank on every larger carrier. At a critical size $N_h$ we classify all deepest states and count them by a factorial recursion. Independently, a target's fibre factors over its level sets into functions with a prescribed cycle length. This gives every empty and nonempty fibre, the first image, and a unique largest fibre at zero of size $(n+1)^{n-1}$. The triangular sequence and all static cycle/forest enumeration are classical and fully subtracted. Complete checks through seven labels and larger critical witnesses provide bounded verification; external status remains `HOLD_EXTERNAL`.
author:
- Anonymous
bibliography:
- references.bib
title: 'Sharp Rank Thresholds, Critical Extremizers,and Fibres of Eventual-Period Feedback'
```

## Markdown 正文

# The labelled operator and its scope

Fix $n\ge1$ and put $\mathcal X_n=\{f:\{0,\ldots,n-1\}\to\{0,\ldots,n-1\}\}$. For a vertex $i$, let $\ell_f(i)$ be the length of the unique directed cycle eventually reached by iterating $f$ from $i$. Loops have length one. Define the simultaneous update $$\label{eq:update}
 (P_nf)(i)=\ell_f(i)-1.$$ Since $1\le\ell_f(i)\le n$, this is an autonomous self-map of $\mathcal X_n$. Numerical labels are retained at every epoch; the output is used as the next function, not as an unlabelled statistic. Write $r(f)=|\operatorname{im}f|$ and denote the constant-zero function by $\boldsymbol 0$. The identity function is not $\boldsymbol 0$ unless $n=1$.

Functional-graph decomposition into cycles with rooted trees is classical, as are labelled SET/CYC enumeration and Cayley forest counts [@FlajoletSedgewick2009]. Functional-graph reconstruction by direct products is a neighboring question: Doré et al. use the word "feedback" for a cyclic vertex's return period but study graph equations up to isomorphism [@DoreEtAl2022v2]. Equation [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} instead changes the numerical pointers and then recomputes their cycles. The distinction specifies the object; it does not establish priority.

The threshold sequence $2,3,6,21,231,26796,\ldots$ is already known. Wagner explicitly gives the triangular recurrence in the enumeration of balanced trees and identifies the sequence A007501 [@Wagner2014 Section 4]. The sequence itself, generic rank descent, cycle finding and all static inverse counts receive zero contribution credit. The temporal content here is the sequence's sharp minimum-rank interpretation, its attained all-rank bound, and the full equality classification at critical sizes. The independent inverse mechanism is the invariant-block decomposition with strict maximal-fibre comparison.

The internal comparison includes P137 rank feedback and P167 least- preimage feedback. A prior word/poset scouting lane excluded canonical statistics written back as states; that lane rule remains unchanged. The present note was separately selected under the central two-axis contract, not by silently waiving that rule. The source record preserves this scope decision and the missing P51--P56 manuscript caveat. No bounded search non-hit or computational success certifies novelty or ownership.

# Cycle-size cost and the zero attractor

Let $\mathcal L(f)$ be the set of distinct cycle lengths in the functional graph of $f$, and put $Q(s)=s(s+1)/2$.

[\[lem:rank\]]{#lem:rank label="lem:rank"} For every $f\in\mathcal X_n$, $$\label{eq:rank}
 r(P_nf)=|\mathcal L(f)|,\qquad
 r(f)\ge\sum_{d\in\mathcal L(f)}d\ge Q(r(P_nf)).$$

Every cycle has a nonempty basin, so the distinct output values are exactly $d-1$ for $d\in\mathcal L(f)$. Choose one cycle for each different length. Their vertices are disjoint and all belong to $\operatorname{im}f$, giving the first inequality. Distinct positive integers with $s$ elements sum to at least $1+\cdots+s=Q(s)$.

[\[prop:zero\]]{#prop:zero label="prop:zero"} Every orbit of $P_n$ reaches $\boldsymbol 0$. It is the sole fixed and sole recurrent state, and every eventual period is one.

If $r(P_nf)\ge2$, then $Q(r(P_nf))>r(P_nf)$, so Lemma [\[lem:rank\]](#lem:rank){reference-type="ref" reference="lem:rank"} strictly decreases rank. If the output has rank one, it is constant. A constant function has only a loop as its cycle, and its next output is $\boldsymbol 0$. Strict decreases cannot continue indefinitely, and $P_n\boldsymbol 0=\boldsymbol 0$. No other recurrent state is possible.

Define $h(f)=\min\{t\ge0:P_n^tf=\boldsymbol 0\}$, now finite by Proposition [\[prop:zero\]](#prop:zero){reference-type="ref" reference="prop:zero"}.

[\[lem:core\]]{#lem:core label="lem:core"} Suppose $1\le k\le n$, $g:\{0,\ldots,n-1\}\to\{0,\ldots,k-1\}$, and $u=g|_{\{0,\ldots,k-1\}}$. For all $t\ge0$, $$\label{eq:restriction}
 (P_n^t g)|_{\{0,\ldots,k-1\}}=P_k^t u.$$ For $t\ge1$, $P_n^t g=\boldsymbol 0$ if and only if $P_k^t u=\boldsymbol 0$. Thus $h(g)=h(u)$ if $h(u)\ge1$; if $u=\boldsymbol 0$, then $h(g)$ is zero or one according as $g=\boldsymbol 0$ or not.

Every cycle of $g$ lies in the first $k$ labels, and every outside vertex enters that core in one arrow. All periods are at most $k$, so $P_ng$ again maps into the core and restricts there to $P_ku$. Induction gives [\[eq:restriction\]](#eq:restriction){reference-type="eqref" reference="eq:restriction"} and preserves this core-mapping property at every epoch. A period-feedback vector is zero exactly when every cycle of its input is a loop. At every epoch the extension and its core restriction have precisely the same cycles. This proves the equivalence for $t\ge1$. If $u=\boldsymbol 0$, the equivalence says that $P_ng=\boldsymbol 0$; time zero must be checked separately, yielding the stated boundary.

# Sharp height at every size and rank

Define $$\label{eq:threshold}
 N_2=2,\qquad N_{h+1}=Q(N_h)\quad(h\ge2).$$ These are strictly increasing integers.

[\[thm:height\]]{#thm:height label="thm:height"} For every $h\ge2$ and every $f$ on any finite carrier, $$\label{eq:rankheight}
 h(f)\ge h\quad\Longrightarrow\quad r(f)\ge N_h.$$ There is a height-$h$ permutation on $N_h$ labels. Consequently the maximum height on $n$ labels is $$\label{eq:maxheight}
 H(1)=0,\qquad H(n)=\max\{h\ge2:N_h\le n\}\quad(n\ge2).$$ More generally, for every $2\le r\le n$, the maximum among rank-$r$ functions on $n$ labels is $H(r)$. At rank one, the maximum is one if $n\ge2$ and zero if $n=1$.

A rank-one function is constant and has height at most one, which proves [\[eq:rankheight\]](#eq:rankheight){reference-type="eqref" reference="eq:rankheight"} at $h=2$. If $h(f)\ge h+1$, then $h(P_nf)\ge h$, so induction and [\[eq:rank\]](#eq:rank){reference-type="eqref" reference="eq:rank"} give $r(f)\ge Q(r(P_nf))\ge Q(N_h)=N_{h+1}$.

To attain the bound, start with $f_2=(1,0)$. Its successive outputs are $(1,1)$ and $(0,0)$, so its height is two. Suppose $f_h$ is a height-$h$ permutation on $k=N_h$ labels. For every $j=0,\ldots,k-1$, make a block $B_j$ containing the unique old label $f_h^{-1}(j)$ and exactly $j$ fresh labels. These blocks partition $Q(k)=N_{h+1}$ labels. On each $B_j$ choose any single cycle and let $f_{h+1}$ be their disjoint union. Then $P f_{h+1}$ is constant $j$ on $B_j$, maps into the first $k$ labels, and restricts there to $f_h$. Lemma [\[lem:core\]](#lem:core){reference-type="ref" reference="lem:core"} shows that $h(P f_{h+1})=h$, so $h(f_{h+1})=h+1$.

For an arbitrary $r\ge2$, let $h=H(r)$ and take this critical permutation on $k=N_h\le r$ labels. Extend it to a permutation on $r$ labels by fixing the added labels. Its first period-feedback vector equals $P_k f_h$ on the core and zero outside. It maps into that core. Since $h(P_k f_h)=h-1\ge1$, Lemma [\[lem:core\]](#lem:core){reference-type="ref" reference="lem:core"} gives height $h-1$ for this vector, and height $h$ for the enlarged permutation. Extend further to $n\ge r$ by mapping all new vertices to zero. The new function has rank exactly $r$ and retains height $h$ by the same lemma. This proves the all-rank and all-size attainment statements. Finally, nonzero constant functions exist exactly when $n\ge2$ and have height one; the only state at $n=1$ is zero.

# All deepest states at critical sizes

The equality statement in this section concerns $n=N_h$, not arbitrary sizes between two thresholds.

[\[thm:critical\]]{#thm:critical label="thm:critical"} At size $N_h$, every height-$h$ function is a permutation. For $h\ge3$ and $k=N_{h-1}$, these are exactly the permutations $f$ satisfying:

1.  there is precisely one cycle of each length $1,2,\ldots,k$;

2.  $u=(P f)|_{\{0,\ldots,k-1\}}$ is a height-$(h-1)$ permutation of those $k$ labels.

If $D_h$ is their number, then $$\label{eq:criticalcount}
 D_2=1,\qquad D_h=D_{h-1}(N_h-N_{h-1})!\quad(h\ge3).$$ In particular, $D_3=1$, $D_4=6$, and $D_5=6\cdot15!$.

Theorem [\[thm:height\]](#thm:height){reference-type="ref" reference="thm:height"} forces $r(f)=N_h$, hence $f$ is a permutation. For $h\ge3$, $h(Pf)=h-1$ and the entire chain $$\label{eq:equalitychain}
 N_h=r(f)\ge\sum_{d\in\mathcal L(f)}d
 \ge Q(r(Pf))\ge Q(N_{h-1})=N_h$$ consists of equalities. The strictly increasing $Q$ forces $r(Pf)=k$. Equality in the distinct-positive-integer sum forces $\mathcal L(f)=\{1,\ldots,k\}$. Equality in the first inequality says that the selected cycle of each length already exhausts all vertices. There are thus no additional cycles, so condition (1) holds and $\operatorname{im}(Pf)=\{0,\ldots,k-1\}$.

By Lemma [\[lem:core\]](#lem:core){reference-type="ref" reference="lem:core"}, the restriction $u$ has height $h-1$. Applying [\[eq:rankheight\]](#eq:rankheight){reference-type="eqref" reference="eq:rankheight"} on its $k=N_{h-1}$ labels forces full rank, so it is a permutation and condition (2) holds. Conversely, conditions (1) and (2) make $Pf$ a core extension of a height-$(h-1)$ function. The same lemma gives $h(Pf)=h-1$, hence $h(f)=h$. This proves necessity and sufficiency, not just an extremal construction.

Fix an eligible $u$. Its inverse image of $j$ prescribes one old label in the cycle block $B_j$ of length $j+1$. Allocate the $N_h-k$ fresh labels among these blocks in $(N_h-k)!/\prod_{j=0}^{k-1}j!$ ways. Each block has $j!$ cyclic orders. Their product cancels the denominator. Different allocations or cyclic orders give different permutations, while the equality characterization shows that every extremizer is obtained. The count per $u$ is therefore $(N_h-k)!$. At $N_2=2$ only the transposition has height two, establishing the initial condition and [\[eq:criticalcount\]](#eq:criticalcount){reference-type="eqref" reference="eq:criticalcount"}.

# The full one-step inverse and its maximum

We isolate the classical enumerative input. Let $R(k,s)$ count forests on a fixed $k$-element label set directed toward a prescribed set of $s\ge1$ roots, with exactly one root per component. Then $$\label{eq:forest}
 R(k,s)=\begin{cases}1,&s=k,\\s k^{k-s-1},&s<k.\end{cases}$$ A root-preserving Prüfer code proves this formula directly. Repeatedly remove the least nonroot leaf and record its parent until only roots remain. There are $k-s$ recorded labels and the last is a root. Conversely, given any such sequence, remove the least remaining nonroot absent from the remaining sequence and join it to the next recorded parent. At each stage such a nonroot exists: the sequence has as many entries as remaining nonroots and at least one root entry, so it cannot contain all remaining nonroots. A deleted label cannot occur later in the sequence, and edges always lead to a still-present label. The reconstruction therefore yields a forest directed to the specified roots and reverses the encoding. There are $s k^{k-s-1}$ codes when $s<k$. This is standard labelled forest enumeration [@FlajoletSedgewick2009], not a new count.

For $d\ge1$, let $a_d(k)$ count functions on a prescribed $k$-element set whose every cycle has length $d$, with $a_d(0)=1$. For $k>0$, $$\label{eq:ad}
 a_d(k)=\sum_{c=1}^{\lfloor k/d\rfloor}
 \frac{k!}{(k-dc)!\,d^c c!}\,R(k,dc).$$ Indeed, choose the $dc$ cyclic labels, put $c$ disjoint $d$-cycles on them, and attach a forest with those prescribed roots. A nonempty such class exists exactly when $k\ge d$: use one $d$-cycle and attach all remaining vertices to a cyclic vertex. In EGF notation the same classical decomposition reads $$\label{eq:egf}
 \sum_{k\ge0}a_d(k)\frac{z^k}{k!}
 =\exp\!\left(\frac{\mathcal T(z)^d}{d}\right),
 \qquad\mathcal T(z)=z\exp(\mathcal T(z)).$$

[\[thm:inverse\]]{#thm:inverse label="thm:inverse"} For $g\in\mathcal X_n$, write $B_j=g^{-1}(j)$ and $k_j=|B_j|$. Then $$\label{eq:fibre}
 |P_n^{-1}(g)|=\prod_{j=0}^{n-1}a_{j+1}(k_j).$$ The target lies in $\operatorname{im}P_n$ exactly when each nonempty $B_j$ satisfies $k_j\ge j+1$. Consequently $$\label{eq:imagecount}
 |\operatorname{im}P_n|=\sum_{\substack{\sum_{j=0}^{n-1}k_j=n\\
                   k_j=0\ \mathrm{or}\ k_j\ge j+1}}
                \frac{n!}{\prod_{j=0}^{n-1}k_j!}.$$

An arrow $i\mapsto f(i)$ does not change the eventual cycle reached. Thus $P_nf=g$ implies that $f$ preserves every $B_j$ and all cycles of $f|_{B_j}$ have length $j+1$. Conversely these conditions force the period of every vertex in $B_j$ to be $j+1$, so they imply $P_nf=g$. The restrictions on distinct labelled blocks are independent, proving [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. The nonemptiness criterion for $a_d(k)$ gives the image condition. Each admissible vector of block sizes has $n!/\prod_j k_j!$ target words, proving [\[eq:imagecount\]](#eq:imagecount){reference-type="eqref" reference="eq:imagecount"}.

[\[thm:maxfibre\]]{#thm:maxfibre label="thm:maxfibre"} For every $n\ge1$, the unique largest fibre is at $g=\boldsymbol 0$, with size $$\label{eq:maxfibre}
 |P_n^{-1}(\boldsymbol 0)|=(n+1)^{n-1}.$$

Let $c_d(k)$ count connected functions on $k$ labels with sole cycle length $d$. For $k\ge d$, selecting the cyclic vertices and attaching their rooted forest gives $$\label{eq:connected}
 c_d(k)=(k)_d k^{k-d-1},\qquad c_1(k)=k^{k-1},$$ where $(k)_d=k(k-1)\cdots(k-d+1)$ and the first expression at $k=d$ is $(d-1)!$. Their ratio is $(k)_d/k^d\le1$, strictly less than one when $d\ge2$. For $k<d$, $c_d(k)=0$. Hence the EGF of connected $d$-cycle components is coefficientwise bounded by the rooted-tree EGF. Taking SET exponentials preserves this inequality: all coefficients are nonnegative and every product term is bounded term by term. Moreover, the coefficient at every $k\ge d\ge2$ is strictly smaller, already in the single-component term. Thus $$\label{eq:comparison}
 a_d(k)\le a_1(k),$$ with strict inequality for every nonempty admissible block with $d\ge2$.

A product of rooted-forest counts on two or more prescribed nonempty blocks is strictly smaller than the rooted-forest count on their union. Disjoint union is an injection, while a forest with one edge between two different blocks is excluded. Applying this fact and [\[eq:comparison\]](#eq:comparison){reference-type="eqref" reference="eq:comparison"} to [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}, equality with the full rooted-forest count requires a single block and $d=1$. This is exactly $g=\boldsymbol 0$. Its fibre is the set of functions having only loops as cycles, equivalently rooted forests with a loop at each root. Adjoining one extra vertex joined to every root gives a bijection with trees on $n+1$ labels rooted at that extra vertex. Cayley's formula gives $(n+1)^{n-1}$. At $n=1$ this is one and the zero target is the only target. Unsupported targets have fibre zero and cannot be maximizers.

# Exact controls and claim ceilings

    $n$   States   First image   Maximum height   Maximum fibre
  ----- -------- ------------- ---------------- ---------------
      1        1             1                0               1
      2        4             2                2               3
      3       27             6                3              16
      4      256            18                3             125
      5     3125            60                3            1296
      6    46656           240                4           16807
      7   823543          1085                4          262144

  : Complete endofunction boxes for the paper-local verifier.

The standard-library verifier computes the update by peeling noncyclic vertices and then propagating cycle periods backwards. Per-vertex orbit tracing supplies a second implementation on all inputs through six labels and a stated prefix of the seven-label box. The full source boxes check rank packing, all-rank maxima, actual target fibres and the image. Every target, including absent targets, is checked through six labels. Critical-size height counts are checked at sizes two, three and six. Recursive witnesses on $2,3,6,21,231,26796$ labels attain heights two through seven, with further leaf extensions. Two fresh processes are compared with the paper-local canonical transcript. All-size validity rests on the proofs, not on extrapolation from these boxes.

No scalar rank evolution law is asserted: [\[eq:rank\]](#eq:rank){reference-type="eqref" reference="eq:rank"} is an inequality. Nor is there a closed formula for each individual height or an all-time target inverse atlas. The equality classification is complete only at the critical sizes $N_h$. For instance, the two functions $(0,1,1)$ and $(1,0,1)$ have the same value histogram, but their period feedback vectors are $(0,0,0)$ and $(1,1,1)$. This refutes a histogram factor only; it does not waive the earlier lane's statistic-writeback filter or establish novelty. Static formulas [\[eq:forest\]](#eq:forest){reference-type="eqref" reference="eq:forest"}--[\[eq:egf\]](#eq:egf){reference-type="eqref" reference="eq:egf"} are classical inputs, not separate discoveries. External status remains `OWNER_AMBER / HOLD_EXTERNAL`.

## Reproducibility and disclosure {#reproducibility-and-disclosure .unnumbered}

The anonymous source, verifier, fixed transcript, source-scope audit and deterministic build instructions are provided with this internal note. No empirical or human-subject data are used. AI-assisted proof exploration, drafting and exact verification were used; author checks are not human expert review. Authorship, funding and conflicts are not inferred for this internal draft. The known triangular sequence and classical functional-graph counts remain attributed throughout.
