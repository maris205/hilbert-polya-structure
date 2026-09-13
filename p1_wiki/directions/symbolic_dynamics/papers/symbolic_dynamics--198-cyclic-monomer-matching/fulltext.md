---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--198-cyclic-monomer-matching"
canonical_tex: "symbolic_dynamics/papers/198-cyclic-monomer-matching/main.tex"
canonical_pdf: "symbolic_dynamics/papers/198-cyclic-monomer-matching/main.pdf"
source_sha256: "817002578925a0fac2337792ddcc8a31f08cca090ae6fac1219f18bcebf77cd5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Least-Monomer Map on Odd-Cycle Matchings\newline and Its Interval Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/198-cyclic-monomer-matching>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/198-cyclic-monomer-matching/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/198-cyclic-monomer-matching/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/198-cyclic-monomer-matching/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/198-cyclic-monomer-matching/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study a deterministic map on all matchings of a labelled odd cycle. When at least three vertices are unmatched, the map flips the alternating arc from the least unmatched vertex to the next unmatched vertex clockwise. With one unmatched vertex, it slides the next dimer into that vertex. Every state enters a single recurrent cycle, and its exact entry time is its deficiency from maximum matching size. The inverse problem depends on the labels: if a target has least unmatched vertex $u$, its fibre has size $\binom{\lfloor u/2\rfloor+1}{2}$, with one additional predecessor when the target is maximum. We prove this formula by a bijection with intervals of a forced dimer prefix. It includes all empty fibres, gives the first-image census, and identifies a unique largest fibre of size $1+\binom{m+1}{2}$ on a cycle of length $2m+1$. Exhaustive checks through length twenty-one support reproducibility, not the all-parameter proof. Classical augmentation and matching enumeration receive no contribution credit; external owner status remains `HOLD_EXTERNAL`.
author:
- Anonymous
bibliography:
- references.bib
title: 'A Least-Monomer Map on Odd-Cycle Matchingsand Its Interval Fibres'
```

## Markdown 正文

# The question and its classical boundary

An augmenting path explains how to increase the size of a matching. It does not determine the predecessor sets of a particular deterministic rule for selecting that path. This note fixes such a rule on an odd cycle and solves both its recurrent dynamics and its labelled one-step inverse. The distinction is between finding a maximum matching and describing the entire finite functional graph of one specified update.

Augmenting-path methods are classical [@Berge1957]. The local fact needed below is proved directly: an alternating path with unmatched endpoints gains one matching edge when flipped. Matching counts of paths and cycles, their Fibonacci identities, and the motion of a single defect in an alternating configuration are also background. None is presented as a new matching principle. Perfect-matching reconfiguration via alternating cycles is a related but different problem [@ItoEtAl2022]: there the rank is preserved, whereas the transient branch here flips a path and strictly raises rank.

The result retained here is the joint object consisting of the least-monomer scheduler, its odd-cycle recurrent splice, and an exact target-prefix interval bijection. Internally, hard-core traffic in P90, the killed path-retile scout GCM, and the stochastic augmentation scout AP1 remain close comparison surfaces. Their generic alternating-core, augmentation, and finite-map formulas receive zero credit. Our rule uses one globally selected arc, and the inverse is a finite interval choice before the target's least unmatched label. These distinctions do not constitute a novelty or priority certificate. The bounded owner audit and its incomplete historical coverage remain visible in the companion record.

# The labelled matching map

Fix $n=2m+1\ge3$. Label the vertices of the simple cycle $C_n$ by $0,1,\ldots,n-1$ clockwise, and put $e_i=\{i,i+1\pmod n\}$. Let $\mathcal M_n$ be the set of all matchings, including the empty matching. A *monomer* is an unmatched vertex. There are $n-2|M|$ monomers in $M$, an odd positive number. Least labels refer to the ordinary linear order, not to an unspecified cyclic starting point.

Define $F_n:\mathcal M_n\to\mathcal M_n$ by the following rule. If there are at least three monomers, let $a$ be the least one and $b$ the next monomer clockwise from $a$. Flip membership of every edge on the clockwise $a$--$b$ arc. If $a$ is the only monomer, flip $e_a$ and $e_{a+1}$. These cases exhaust the carrier and are recomputed from the current state.

[\[lem:closure\]]{#lem:closure label="lem:closure"} The rule is well defined. If $|M|<m$, then $|F_n(M)|=|M|+1$. If $|M|=m$ and its monomer is $a$, the output has monomer $a+2\pmod n$.

Between two consecutive monomers every internal vertex must be matched inside the arc: the only edges leaving its interior meet the unmatched endpoints. Thus the number of internal vertices is even, the arc length is odd, and its edge-membership pattern is $0,1,0,1,\ldots,0$. Flipping gives $1,0,1,0,\ldots,1$, which matches the endpoints without changing any other matched status. It gains one edge. With one monomer $a$, deleting $a$ leaves an even path with a unique perfect matching. In particular $e_a$ is absent and $e_{a+1}$ present. Their flip replaces the dimer on $a+1,a+2$ by the dimer on $a,a+1$. The new monomer is $a+2$, including when either edge crosses the label cut.

# The exact entry time and recurrent cycle

The tail $\tau(M)$ is the least nonnegative iterate at which the orbit of $M$ reaches a recurrent state.

[\[thm:time\]]{#thm:time label="thm:time"} For every $M\in\mathcal M_n$, $$\label{eq:tail}
 \tau(M)=m-|M|.$$ The $n$ maximum matchings form one directed cycle of length $n$. There are no other recurrent states and no fixed points. The largest tail is $m$, attained only by the empty matching.

Lemma [\[lem:closure\]](#lem:closure){reference-type="ref" reference="lem:closure"} strictly raises rank until rank $m$, so a state of smaller rank cannot be recurrent and reaches that rank after exactly $m-|M|$ steps. For each prescribed monomer there is precisely one maximum matching, by the unique tiling of the even path obtained on deleting that vertex. On these $n$ states the monomer moves by $+2$. Because $\gcd(2,n)=1$, this is a single $n$-cycle. It proves both the exact tail and the recurrent classification. Only rank zero has tail $m$.

[\[cor:depth\]]{#cor:depth label="cor:depth"} The depth generating polynomial is $$\label{eq:depth}
 \sum_{M\in\mathcal M_n}z^{\tau(M)}
 =\sum_{r=0}^{m}\frac{n}{n-r}\binom{n-r}{r}z^{m-r}.$$

For completeness, the classical matching count has a short direct proof. A path on $v$ vertices has $\binom{v-r}{r}$ matchings of size $r$: if its selected edge indices are $i_1<\cdots<i_r$ with successive gaps at least two, subtract $0,1,\ldots,r-1$ to obtain an ordinary $r$-subset of $v-r$ indices. A cycle matching without the wrap edge therefore has $\binom{n-r}{r}$ choices. With that edge present, remove its two endpoints and count $\binom{n-r-1}{r-1}$ choices on the remaining path. At $r=0$ the latter count is zero. Adding gives $\frac{n}{n-r}\binom{n-r}{r}$, and [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"} assigns the exponent.

# Every predecessor is a prefix interval

Fix $Y\in\mathcal M_n$, and let $u$ be its least monomer. There is always a monomer because $n$ is odd. Put $r=\lfloor u/2\rfloor$ and $T_r=r(r+1)/2$.

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} Every one-step fibre is given by $$\label{eq:fibre}
 |F_n^{-1}(Y)|=T_{\lfloor u/2\rfloor}+\mathbf1_{\{|Y|=m\}}.$$ More precisely, its transient predecessors correspond bijectively to nonempty consecutive intervals in the $r$ internal dimers before $u$. When $Y$ is maximum there is one additional, disjoint rotor predecessor.

All vertices below $u$ are matched. If $u$ is even, the prefix $0,\ldots,u-1$ is tiled by $e_0,e_2,\ldots,e_{u-2}$. To justify this, start at $u-1$, which cannot be matched to the monomer $u$, and work backwards. If $u$ is odd, the same argument forces the internal dimers $e_1,e_3,\ldots,e_{u-2}$ and then forces vertex zero to use the wrap edge $e_{n-1}$. In either case there are exactly $r$ consecutive *internal* prefix dimers; the wrap dimer in the odd case is excluded.

Suppose a nonmaximum source $M$ maps to $Y$, and its chosen endpoint monomers are $a,b$. The source has at least three monomers. Since $a$ is the least and $b$ the next, the selected arc does not cross the label cut and $a<b$. The update removes just these two monomers. Every remaining monomer is greater than $b$, so $a<b<u$. On the target arc, the flipped pattern is $1,0,\ldots,1$. Thus that arc consists of a nonempty interval of the forced prefix dimers just described.

Conversely, choose any such interval. Flip its target edges backwards. The resulting matching has two new monomers, the endpoints $a<b$ of the interval, and all former monomers of $Y$. The endpoints satisfy $b<u$. They are consequently the two least source monomers and are consecutive clockwise, so the prescribed scheduler selects this very interval and returns $Y$. Distinct intervals have distinct endpoint pairs and hence distinct sources. This proves the bijection. There are $\sum_{j=1}^r j=T_r$ nonempty intervals.

A maximum source stays maximum and has exactly one successor and predecessor within the rotor. It can therefore contribute to $Y$ exactly when $Y$ is maximum, in which case its monomer is $u-2\pmod n$. The transient predecessors have one fewer edge than $Y$, so none is this rotor predecessor. There are no other branches of the update.

[\[cor:max\]]{#cor:max label="cor:max"} A nonmaximum target lies in $\operatorname{im}(F_n)$ exactly when $u\ge2$; every maximum target lies in the image. The unique largest fibre is at the maximum matching with monomer $n-1$, and its size is $$\label{eq:max}
 1+\frac{m(m+1)}2.$$

The support statement is [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}, since $T_r>0$ exactly when $r\ge1$. The inequality $u\le2m$ gives $r\le m$. Equality $r=m$ forces $u=2m$, so every other vertex is matched and $Y$ is uniquely the maximum matching with that monomer. It has the extra rotor predecessor. All other targets have $r\le m-1$ and a no larger indicator, proving the strict maximum.

For example, on $C_7$ the target with edges $e_0,e_2,e_4$ has monomer six. Its six transient predecessors are the reversals of the six nonempty intervals of those three dimers. Its seventh predecessor is the maximum matching with monomer four. Targets with $u=0$ or $1$ have no transient predecessor at all. These cases show why the rotor indicator cannot be absorbed into the interval count.

# The first image and bounded exact controls

Write $F_0=0,F_1=1,F_{j+1}=F_j+F_{j-1}$ for Fibonacci numbers and $L_j=F_{j-1}+F_{j+1}$ for $j\ge1$.

[\[cor:image\]]{#cor:image label="cor:image"} For every odd $n\ge3$, $$\label{eq:image}
 |\operatorname{im}(F_n)|=F_{n-1}+F_{n-3}+2=L_{n-2}+2.$$

First count all targets with $u\ge2$, equivalently those matching both vertices zero and one. If $e_0$ is present, the remaining path on $n-2$ vertices has $F_{n-1}$ matchings. If $e_0$ is absent, both $e_{n-1}$ and $e_1$ must be present. For $n\ge5$ their removal leaves a path on $n-4$ vertices, counted by $F_{n-3}$. When $n=3$ this pair is incompatible, so its count is zero, agreeing with $F_0$. The path count follows from the recurrence obtained by leaving its first vertex unmatched or matching it to the next: a path on $v\ge0$ vertices has $F_{v+1}$ matchings. The two disjoint cases already include all maximum targets with monomer at least two. Corollary [\[cor:max\]](#cor:max){reference-type="ref" reference="cor:max"} adds exactly the two maximum targets with monomer zero or one. The Lucas identity is its definition.

    $n$   States   Image   Recurrent   Max tail   Max fibre
  ----- -------- ------- ----------- ---------- -----------
      3        4       3           3          1           2
      7       29      13           7          3           7
     11      199      78          11          5          16
     15     1364     523          15          7          29
     21    24476    9351          21         10          56

  : Exact complete-carrier checks. These values are consequences of the proofs; exhaustion is bounded counterexample pressure.

The paper-local standard-library verifier enumerates every matching for odd $3\le n\le21$, constructs the full transition graph, and computes tails and cycles by indegree peeling. It compares every target's actual indegree with [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}, including empty fibres, checks every depth coefficient, and tests the unique fibre extremizer. A separate endpoint- set reconstruction checks the complete inverse bijection. Two fresh processes are compared byte for byte with the retained transcript. The proofs above, rather than these finite boxes, establish all-size claims.

The scope is restricted to odd simple cycles with the stated numeric scheduler. Nothing here gives an arbitrary-graph matching algorithm, a pointwise all-time inverse formula, or an external novelty clearance. The image census and depth coefficients are classical enumeration applied to this literal map, not extra independent mechanisms. The companion source record preserves the P90/GCM/AP1 subtraction and source-access limitations. The manuscript remains `OWNER_AMBER / HOLD_EXTERNAL`.

## Reproducibility and disclosure {#reproducibility-and-disclosure .unnumbered}

The source, paper-local verifier, frozen stdout, and deterministic build instructions accompany this internal anonymous note. No empirical or human-subject data are used. AI-assisted drafting, proof exploration and exact verification were used; bounded checks and author checks are not represented as human expert review. Authorship, funding and conflict declarations are not inferred for this internal draft.
