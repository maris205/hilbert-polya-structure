---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--105-cycle-minimum-pruning-dynamics"
canonical_tex: "symbolic_dynamics/papers/105-cycle-minimum-pruning-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/105-cycle-minimum-pruning-dynamics/main.pdf"
source_sha256: "8bf14d50abf29591dcc55686863c8775c34b88a44edd4e0e8af428ddf304ab98"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Cycle-Minimum Pruning on Permutations: Exact Transient Layers and One-Step Fibers

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/105-cycle-minimum-pruning-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/105-cycle-minimum-pruning-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/105-cycle-minimum-pruning-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/105-cycle-minimum-pruning-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/105-cycle-minimum-pruning-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  In every nontrivial cycle of a permutation of $[n]$, simultaneously delete its least label from the cyclic word and make that label fixed. This gives a self-map $P_n$ of $\mathfrak S_n$ without standardization. After $t$ steps, the $t$ least labels of each original cycle are fixed, stopping when one label remains. Hence the absorption time is $L(\pi)-1$, where $L(\pi)$ is the longest cycle length. The identity is the unique recurrent state and the Artin--Mazur zeta function is $(1-z)^{-1}$. If $A_{n,k}$ counts permutations with all cycle lengths at most $k$, then the exact depth-$t$ layer has size $$A_{n,t+1}-A_{n,t},\qquad
   \sum_{n\geq0}A_{n,k}\frac{z^n}{n!}
   =\exp\!\left(\sum_{j=1}^k\frac{z^j}{j}\right).$$ A threshold-matching formula determines every one-step fiber and the Garden-of-Eden states. Exhaustive checks through $\mathfrak S_9$ and independent recurrences give $17{,}219{,}241$ exact assertions. Classical cycle enumeration and longest-cycle laws are owner-subtracted; release is on hold.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 29 August 2026'
title: 'Cycle-Minimum Pruning on Permutations: Exact Transient Layers and One-Step Fibers'
```

## Markdown 正文

# Introduction

Deleting an entry from a permutation cycle is elementary, but applying a label-sensitive deletion simultaneously to every cycle produces a rigid finite dynamics. Let $[n]=\{1,\ldots,n\}$. At each time step, we remove the minimum from every cycle of length at least two, reconnect the predecessor to the successor, and retain the removed label as a one-cycle. Labels are never compressed: the phase space remains the same symmetric group $\mathfrak S_n$.

Two complementary structures govern this map. Orbitwise, each original cycle loses its labels in increasing order while retaining its cyclic orientation. Enumeratively, the absorption depth is the longest cycle length minus one, so restricted-cycle exponential generating functions give every depth layer. A third structure appears when the map is reversed: nontrivial output cycles must be matched to smaller fixed points, while the unmatched fixed points encode an involution.

The finite-dynamics package proved here has four parts.

1.  We give the exact $t$-step state of every permutation and the induced evolution of every cycle type.

2.  We classify recurrence, all iterate-fixed counts, least periods, and the formal Artin--Mazur zeta function.

3.  We determine every transient layer by a restricted-cycle generating function and a second, cycle-containing-$1$ recurrence, including sharp deepest layers.

4.  We count every one-step fiber and characterize the states with no ancestor.

The depth statistic itself is classical. Labelled permutation cycles and their exponential formula are standard material [@FlajoletSedgewick2009; @Stanley2011], and Shepp and Lloyd own the classical distribution theory of ordered cycle lengths, including the longest cycle [@SheppLloyd1966]. Random deletion-consistent permutation and partition structures also have an established literature [@Pitman2006]. None of those results is re-claimed below. The residual object is the deterministic simultaneous surgery just described, its exact orbit normal form, and especially its one-step fiber geometry. A bounded search through 29 August 2026 did not locate this same combined package; search absence is not a novelty or priority certification.

# The exact map and its iterates {#sec:map}

Every nontrivial cycle has a unique minimum-first display $$C=(m,c_1,\ldots,c_{\ell-1}),\qquad m=\min C.$$

[\[def:map\]]{#def:map label="def:map"} For a cycle $C$ as above, set $$P(C)=(m)(c_1,\ldots,c_{\ell-1}),$$ where a one-letter parenthesis is a fixed point. A fixed cycle is left unchanged. Apply this rule to all disjoint cycles of $\pi\in\mathfrak S_n$ in parallel; the resulting permutation is $P_n(\pi)$.

Equivalently, if $p$ is the predecessor of $m$ and $s$ its successor in $C$, the surgery changes the arrows $p\mapsto m\mapsto s$ to $p\mapsto s$ and $m\mapsto m$. Because distinct cycles have disjoint arrow sets, the parallel update is unambiguous. In particular, $P_n$ is a self-map of $\mathfrak S_n$, not a map to $\mathfrak S_{n-r}$ followed by standardization.

For a cycle $C$, write its labels increasingly as $s_1<\cdots<s_\ell$. If $0\leq t\leq\ell-1$, let $C[t]$ be the cycle on $C\setminus\{s_1,\ldots,s_t\}$ with cyclic order inherited from $C$. When one label remains, $C[t]$ denotes its one-cycle.

[\[thm:iterate\]]{#thm:iterate label="thm:iterate"} Let $\pi\in\mathfrak S_n$ have disjoint cycles $C_1,\ldots,C_q$, with $\ell_i=\lvert C_i\rvert$. For every $t\geq0$, the contribution of $C_i$ to $P_n^t(\pi)$ consists of $$(s_{i,1})\cdots(s_{i,r_i})\,C_i[r_i],
 \qquad r_i=\min\{t,\ell_i-1\}.$$ Consequently a cycle of initial length $\ell$ contributes $\min\{t,\ell-1\}$ new one-cycles and one cycle of length $\max\{\ell-t,1\}$ at time $t$.

At time zero the assertion is tautological. Suppose the displayed form holds at time $t<\ell_i-1$. Its surviving cycle has label set $C_i\setminus\{s_{i,1},\ldots,s_{i,t}\}$, whose minimum is $s_{i,t+1}$. Definition [\[def:map\]](#def:map){reference-type="ref" reference="def:map"} fixes that label and deletes it from the inherited cyclic word. This gives $C_i[t+1]$. Once one label remains, all labels from the original cycle are fixed and further pruning does nothing. The cycles evolve independently, completing the induction.

Let $L(\pi)$ be the largest cycle length, and define the absorption time $$\tau_n(\pi)=\min\{t\geq0:P_n^t(\pi)=\mathrm{id}_{[n]}\}.$$

[\[cor:depth\]]{#cor:depth label="cor:depth"} For every $\pi\in\mathfrak S_n$, $$\boxed{\tau_n(\pi)=L(\pi)-1.}$$ The global maximum is $n-1$, attained precisely by the $(n-1)!$ $n$-cycles.

An original $\ell$-cycle becomes pointwise fixed after exactly $\ell-1$ steps. All cycles are processed simultaneously, so the slowest cycle gives the maximum. Depth $n-1$ is equivalent to having an $n$-cycle, of which there are $(n-1)!$.

# Recurrence, periodic blindness, and recovery {#sec:periodic}

At every nonidentity state, $P_n$ creates at least one new fixed point and never destroys a fixed point. This Lyapunov statistic closes the periodic ledger.

[\[thm:zeta\]]{#thm:zeta label="thm:zeta"} For every $n\geq1$:

1.  the identity is the unique recurrent state and the unique fixed point of $P_n^r$ for every $r\geq1$;

2.  the number $C_n(r)$ of cycles of least temporal period $r$ is $C_n(1)=1$ and $C_n(r)=0$ for $r>1$;

3.  as an identity in $\mathbb Q[[z]]$, $$\zeta_{P_n}(z)
       =\exp\!\left(\sum_{r\geq1}
          \frac{\lvert \operatorname{Fix}(P_n^r)\rvert}r z^r\right)
       =\frac1{1-z}.$$

The iterate normal form shows that every nonidentity state reaches the identity and cannot return to itself. Thus every iterate fixes only the identity. Möbius inversion of $\lvert \operatorname{Fix}(P_n^r)\rvert=\sum_{d\mid r}dC_n(d)$ gives the stated cycle census. Finally, $\exp(\sum_{r\geq1}z^r/r)=\exp(-\log(1-z))=(1-z)^{-1}$. The definition of this periodic-point zeta ledger is due to Artin and Mazur [@ArtinMazur1965].

The periodic data are identical for all $n$ and therefore cannot recover the phase parameter. The transient profile does recover it: its greatest occupied depth is $n-1$. This differs from a digit-erasure absorber, where time is a digit sum on a changing ring family. Here the update preserves the labelled ground set, processes several cycles in parallel, and has the fiber structure proved in [5](#sec:fibers){reference-type="ref" reference="sec:fibers"}.

# Every transient layer {#sec:layers}

For $n,k\geq0$, let $$A_{n,k}=\#\{\pi\in\mathfrak S_n:L(\pi)\leq k\},$$ with $A_{0,k}=1$ and $A_{n,0}=0$ for $n\geq1$. Let $D_{n,t}=\#\{\pi\in\mathfrak S_n:\tau_n(\pi)=t\}$.

[\[thm:profile\]]{#thm:profile label="thm:profile"} For $0\leq t\leq n-1$, $$\label{eq:layers}
 \boxed{D_{n,t}=A_{n,t+1}-A_{n,t}.}$$ The cumulative counts have the formal exponential generating function $$\label{eq:egf}
 \boxed{
 \sum_{n\geq0}A_{n,k}\frac{z^n}{n!}
 =\exp\!\left(\sum_{j=1}^k\frac{z^j}{j}\right).}$$ Independently, they satisfy the exact recurrence $$\label{eq:recurrence}
 A_{n,k}=\sum_{j=1}^{\min\{k,n\}}
 \frac{(n-1)!}{(n-j)!}\,A_{n-j,k}
 \qquad(n\geq1).$$ In particular, $$\begin{aligned}
 D_{n,0}&=1,\label{eq:first-layer}\\
 D_{n,n-1}&=(n-1)!,\label{eq:deepest}\\
 D_{n,n-2}&=n(n-2)!\qquad(n\geq3).\label{eq:penultimate}\end{aligned}$$

Corollary [\[cor:depth\]](#cor:depth){reference-type="ref" reference="cor:depth"} identifies depth at most $t$ with longest cycle at most $t+1$. Subtracting adjacent cumulative counts proves [\[eq:layers\]](#eq:layers){reference-type="eqref" reference="eq:layers"}.

For [\[eq:egf\]](#eq:egf){reference-type="eqref" reference="eq:egf"}, a labelled cycle of length $j$ contributes $z^j/j$. Taking an unordered set of cycles with allowed lengths $1,\ldots,k$ gives the exponential. This is the classical labelled exponential formula for permutations, used here as an enumerative input [@FlajoletSedgewick2009].

For the second route, expose the cycle containing label $1$. If it has length $j$, choose its other $j-1$ labels and arrange them around $1$ in $(j-1)!$ ways, giving $$\binom{n-1}{j-1}(j-1)!=\frac{(n-1)!}{(n-j)!}.$$ The remaining labels carry any permutation counted by $A_{n-j,k}$, which proves [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}.

Depth zero contains only the identity. The deepest formula was proved in [\[cor:depth\]](#cor:depth){reference-type="ref" reference="cor:depth"}. At depth $n-2$, one chooses the singleton outside an $(n-1)$-cycle and then chooses that cycle, giving $n(n-2)!$.

The first exact profiles are shown in [1](#tab:profiles){reference-type="ref" reference="tab:profiles"}. These are raw state counts, not normalized probabilities.

::: {#tab:profiles}
    $n$ depth histogram
  ----- -----------------------------------------
      4 $(1,9,8,6)$
      5 $(1,25,40,30,24)$
      6 $(1,75,200,180,144,120)$
      7 $(1,231,980,1260,1008,840,720)$
      8 $(1,763,5152,8820,8064,6720,5760,5040)$

  : Depth histograms $(D_{n,0},\ldots,D_{n,n-1})$ from the closed formula and exhaustive functional graphs.
:::

For a uniform random permutation, $\tau_n=L-1$ transfers any theorem about the longest cycle to the absorption time by a deterministic shift. In particular, its scaling limits and moment asymptotics are consequences of classical longest-cycle theory [@SheppLloyd1966]; they are not residual claims of this paper.

# Exact one-step fibers {#sec:fibers}

The forward depth depends only on cycle lengths, but the reverse graph sees the labels. Fix $\sigma\in\mathfrak S_n$. Let $F(\sigma)$ be its fixed-point set and put $f=\lvert F(\sigma)\rvert$. Order the nontrivial cycles $B_1,\ldots,B_r$ so that $$b_1<\cdots<b_r,
 \qquad b_i=\min B_i.$$ Write $\ell_i=\lvert B_i\rvert$ and $$e_i=\#\{x\in F(\sigma):x<b_i\}.$$ Finally, let $$\label{eq:involution}
 I_s=\sum_{q=0}^{\lfloor s/2\rfloor}
 \frac{s!}{2^q q!(s-2q)!}$$ be the number of involutions on an $s$-element set.

[\[thm:fiber\]]{#thm:fiber label="thm:fiber"} If $e_i<i$ for some $i$, then $P_n^{-1}(\sigma)$ is empty. Otherwise $$\label{eq:fiber}
 \boxed{
 \lvert P_n^{-1}(\sigma)\rvert
 =I_{f-r}\prod_{i=1}^r \ell_i(e_i-i+1).}$$ Thus $\sigma$ is a Garden-of-Eden state exactly when $e_i<i$ for at least one $i$.

Consider a source cycle of length at least three. Pruning separates its minimum $m$ as a fixed point and leaves one nontrivial output cycle $B$. Necessarily $m<\min B$. Distinct source cycles supply distinct fixed points, so every nontrivial output cycle must be matched injectively to an eligible point of $F(\sigma)$.

Process $B_1,\ldots,B_r$ in increasing order of their minima. Cycle $B_i$ has $e_i$ eligible fixed points. The $i-1$ earlier choices are all among those $e_i$ points, leaving $e_i-i+1$ choices. Hence the number of eligible matchings is $\prod_i(e_i-i+1)$, and such a matching exists exactly when $e_i\geq i$ for every $i$.

After matching a point $m$ to $B_i$, insert $m$ into one of the $\ell_i$ directed edges of that cycle. This gives all $\ell_i$ source cycles whose pruning is $(m)B_i$, with no duplication. The remaining $f-r$ fixed points are either source fixed points or are paired into source transpositions. Choosing an arbitrary involution on those labels records exactly that singleton/pair decomposition, giving the factor $I_{f-r}$. These choices are independent, and every source cycle has been recovered uniquely, which proves [\[eq:fiber\]](#eq:fiber){reference-type="eqref" reference="eq:fiber"}.

[\[cor:identity-fiber\]]{#cor:identity-fiber label="cor:identity-fiber"} The identity has exactly $I_n$ one-step ancestors. Equivalently, $P_n(\pi)=\mathrm{id}$ precisely when every cycle of $\pi$ has length at most two.

In [\[thm:fiber\]](#thm:fiber){reference-type="ref" reference="thm:fiber"}, the identity has $f=n$ and $r=0$. The equivalent description also follows directly from the fact that one pruning step shortens every nontrivial cycle by one.

# Exact controls and limitations {#sec:controls}

The deterministic program `code/verify_cycle_minimum_pruning.py` uses two separately coded representations of time evolution. The literal route edits predecessor and successor arrows at the minimum of each cycle. The closed route deletes the successive smallest labels from every original cyclic word. Exhaustive enumeration of $\mathfrak S_1$ through $\mathfrak S_9$ covers $409{,}113$ states and performs $1{,}981{,}326$ nontrivial trajectory-step evaluations. The latter count includes repeated visits to the same functional-graph edge from different starting states; it is not a count of distinct edges. The program checks every full orbit, cycle-type evolution, absorption depth, iterate-fixed predicate, and depth histogram.

The same enumeration constructs every literal one-step indegree and compares all $409{,}113$ values with [\[eq:fiber\]](#eq:fiber){reference-type="eqref" reference="eq:fiber"}. A separate implementation of [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} checks all depth layers through $n=50$, including the sharp endpoint formulas, while Möbius and formal-zeta coefficients are checked through period $60$. The stored run contains $17{,}219{,}241$ exact assertions. It uses only integers and rational numbers; there is no random seed, floating-point theorem check, symbolic simplifier, or optimization solver.

The controls test conventions and finite instances; the proofs establish the infinite family. The manuscript does not claim a new theorem about the classical longest-cycle distribution, random permutation asymptotics, or general deletion-consistent structures. It also does not classify arbitrary label-pruning rules or all multi-step fibers. Public posting, submission, venue selection, specialist contact, and absolute novelty language remain **HOLD**.
