---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--209-ordered-fibre-threading"
canonical_tex: "symbolic_dynamics/papers/209-ordered-fibre-threading/main.tex"
canonical_pdf: "symbolic_dynamics/papers/209-ordered-fibre-threading/main.pdf"
source_sha256: "d06e900162ef9c494aa333ed96215fa6778a18bf8cdae4add42998b3ab7b880d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Recurrent Functions and Inverse Fibres of Ordered Fibre Threading

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/209-ordered-fibre-threading>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/209-ordered-fibre-threading/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/209-ordered-fibre-threading/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/209-ordered-fibre-threading/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/209-ordered-fibre-threading/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the recurrent functions and one-step inverse fibres of an ordered threading operation on finite labelled endofunctions. In each old fibre, the operation links its members in increasing order and retains the old destination at the largest member. This familiar local rewiring does not force convergence to a permutation: noncycle paths can rotate their attachments indefinitely. We prove that the recurrent graphs are exactly directed cycles with disjoint unbranched feeding paths, at most one per cycle vertex, whose final labels lie below every label of their cycle. The exact period of a whole function is the least common multiple of the lengths of cycles with nonempty feeding paths; pure cycles are fixed. The necessity proof uses all iterated vertex-image sets to freeze backward heights. Independently, admissible increasing path covers of a target give a nonredundant decoder for every predecessor. For nonempty label sets, the maximum fibre is $2^{n-1}$, uniquely at the cyclic successor permutation. Empty and singleton cases are included. No sharp entrance-time or general-time inverse formula is asserted.
author:
- Anonymous
bibliography:
- references.bib
title: Recurrent Functions and Inverse Fibres of Ordered Fibre Threading
```

## Markdown 正文

# The operation and its scope

Let $[n]=\{0,\ldots,n-1\}$ and $\mathcal X_n=[n]^{[n]}$, with $n\ge0$. For each nonempty fibre $f^{-1}(v)=\{i_1<\cdots<i_k\}$, set $$\label{eq:rule}
 (Tf)(i_j)=i_{j+1}\quad(1\le j<k),
 \qquad (Tf)(i_k)=v.$$ Every fibre and its order are computed from the old function. Since the fibres partition $[n]$, this simultaneous prescription defines $T:\mathcal X_n\to\mathcal X_n$. The empty function is fixed. We retain all labels; there is no quotient by rotation or graph isomorphism.

The functional digraph of $f$ has arrows $i\to f(i)$. Its directed cycles, including loops, are called *vertex cycles*. In contrast, $f$ is *recurrent* when $T^p(f)=f$ for some $p\ge1$, and $\operatorname{per}(f)$ is the least such $p$. These refer to the update on whole functions. Every permutation is fixed by [\[eq:rule\]](#eq:rule){reference-type="eqref" reference="eq:rule"}, whatever its vertex-cycle lengths, but nonpermutations can have nontrivial periods: $$\label{eq:two-cycle}
 (1,2,1)\ \longmapsto\ (2,2,1)\ \longmapsto\ (1,2,1).$$ Here $1\leftrightarrow2$ is unchanged and the arrow from vertex $0$ alternates between its two attachments.

Our results answer two separate questions. Section [2](#sec:recurrence){reference-type="ref" reference="sec:recurrence"} classifies exactly the labelled graphs supporting recurrent motion and determines their periods. Section [3](#sec:inverse){reference-type="ref" reference="sec:inverse"} reconstructs every one-step predecessor directly from the target and proves that the cyclic successor permutation uniquely maximizes the fibre, with value $2^{n-1}$ for $n\ge1$. All proofs are given here; finite checks are supplementary.

#### Known rewiring primitives.

Replacing ordered stars by chains is established graph linearization. Onus, Richa and Scheideler's pure linearization algorithm operates on connected undirected graphs, separates smaller and larger neighbours, and uses an add-wins convention when updates conflict [@onus2007linearization Algorithm 1 and Section 2]. Connectivity by replacing old edges with paths is also a shared primitive. Those operations and their proofs are not claimed as new here.

The successor-repair protocols of Cramer and Fuhrmann [@cramer2005ring Sections 4 and 5.1--5.3] and Shaker and Reeves [@shaker2005ring Figure 3 and Section 5.1] provide a closer directed comparison. Their successor changes shorten clockwise successor distance. In [\[eq:two-cycle\]](#eq:two-cycle){reference-type="eqref" reference="eq:two-cycle"}, the successor of $0$ instead moves from $1$ to $2$ before returning. Thus this loop-free transition is neither a literal successor repair nor a batch consisting only of such shortening repairs. This witness does not exclude every abstract conjugacy or enlarged-state construction. Aradhya and Scheideler's tree-to-path construction [@aradhya2025tree Section 3.4, Algorithm 10 and Appendix B] also rewires ordered siblings, but takes a rooted tree with depth-parity labels; its distributed version additionally has supervisor and message state. It is not repeated [\[eq:rule\]](#eq:rule){reference-type="eqref" reference="eq:rule"} on arbitrary endofunctions with vertex cycles. We credit these primitives, ordinary path covers and rotation/LCM calculations. The contribution here is the exact recurrent and inverse/extremal conjunction for [\[eq:rule\]](#eq:rule){reference-type="eqref" reference="eq:rule"}, not a general rewiring method or a global priority claim.

# The exact recurrent geometry {#sec:recurrence}

A *feeding path* has at least one noncycle vertex and is directed towards a vertex cycle. Its *final vertex* $a$ is the noncycle vertex whose image lies on that cycle. Internal path labels are unrestricted.

[\[thm:recurrent\]]{#thm:recurrent label="thm:recurrent"} A function $f\in\mathcal X_n$ is recurrent under $T$ if and only if each weak component of its functional digraph consists of a directed cycle $C$ and pairwise disjoint unbranched feeding paths, at most one at each cycle vertex, with every final path vertex $a$ satisfying $$\label{eq:label-bound}
 a<\min C.$$ On this set, all cycle and internal-path arrows are unchanged. Each path attachment moves one cycle predecessor backwards, and $$\label{eq:period}
 \operatorname{per}(f)=\operatorname{lcm}\{|C|:C\text{ carries a nonempty feeding path}\}.$$ The empty least common multiple is one; a pure vertex cycle is fixed.

Write $I_r(f)=f^r([n])$, where $f^r$ denotes composition on vertices, not iteration of $T$. The backward height at $v$ is $$\label{eq:height}
 h_f(v)=\sup\{r\ge0:v\in I_r(f)\}
 \in\{0,\ldots,n-1\}\cup\{\infty\}.$$ It is infinite exactly on vertex cycles. Off a cycle it is the largest length of a directed path ending at $v$. Indeed, an arbitrarily long backward walk repeats a vertex; the resulting cycle cannot have a forward exit, so its terminal vertex also lies on that cycle. We order $\infty$ above every finite height.

*Image inclusions.* An old arrow $i_j\to v$ in a fibre is replaced by the new directed walk $$i_j\to i_{j+1}\to\cdots\to i_k\to v.$$ The walk has positive length even when its final destination is a fibre member. Replacing and concatenating all arrows of an old length-$r$ walk ending at $v$ gives a new walk of length at least $r$ ending there. Its last $r$ arrows witness $$\label{eq:image-monotone}
 I_r(f)\subseteq I_r(Tf)\qquad(r\ge0).$$ Every new arrow stays inside one old weak component, while each old arrow has the displayed replacement joining its endpoints. Hence the component vertex sets are preserved.

*Frozen heights.* Suppose $T^p(f)=f$. For every $r$, inclusion [\[eq:image-monotone\]](#eq:image-monotone){reference-type="eqref" reference="eq:image-monotone"} around the periodic orbit forces equality at each epoch. Thus every labelled vertex has an epoch-independent height, denoted $h(v)$, and the vertex-cycle set is fixed. For any old arrow $j\to v$, a finite height at $v$ satisfies $h(v)\ge h(j)+1$. If its height is infinite, then $h(j)\le h(v)$ still holds. Consequently $$\label{eq:arrow-height}
 h(j)\le h(v),\qquad
 h(j)=h(v)\ \Longrightarrow\ h(j)=h(v)=\infty.$$

Fix a source coordinate $i$. If it is maximal in its fibre, its head is retained. Otherwise its new head is the next sibling $j$, where $f(j)=f(i)=v$. Equation [\[eq:arrow-height\]](#eq:arrow-height){reference-type="eqref" reference="eq:arrow-height"} gives $$\label{eq:head-height}
 h((Tf)(i))\le h(f(i)).$$ Because heights were already proved fixed at the vertices, this is a nonincreasing sequence of head heights around a periodic whole-function orbit. It must be constant. In the next-sibling case, [\[eq:arrow-height\]](#eq:arrow-height){reference-type="eqref" reference="eq:arrow-height"} therefore forces $j$ onto a vertex cycle. This also covers $j=v$: a selected sibling arrow may numerically equal the retained old arrow, and is not discarded from the argument.

*Necessary geometry.* Each fibre contains at most one cycle vertex, since a cycle target has exactly one cycle predecessor and an off-cycle target has none. Every member after the first in an ordered fibre is a next-sibling head, hence is on a cycle. Therefore a fibre has at most two members, and a two-member fibre is a smaller noncycle vertex followed by a cycle vertex. In particular, off-cycle indegree is at most one, while a cycle vertex has at most one noncycle predecessor. Following arrows towards cycles now partitions the noncycle vertices into unbranched paths, at most one per cycle target. A cycle arrow is retained because its source is maximal in the corresponding fibre; an internal-path arrow is retained because its target has a singleton fibre.

Let $a$ be a final path vertex with $f(a)=v\in C$, and let $u$ be the cycle predecessor of $v$. The fibre is $(a,u)$, so the new attachment is $T(f)(a)=u$. Cycle arrows remain unchanged at every epoch. Repeated predecessor motion visits every label of $C$. At each epoch $a$ must remain smaller than the relevant cycle predecessor, giving [\[eq:label-bound\]](#eq:label-bound){reference-type="eqref" reference="eq:label-bound"}.

*Sufficiency and exactness.* Conversely assume the stated geometry and label bound. At every cycle target with an attached path, its cycle predecessor exceeds the path-final vertex. The rule therefore retains cycle and internal-path arrows and moves all attachments one predecessor backwards. Distinct attachments remain distinct because the predecessor map is bijective, and the label bound is preserved. After $|C|$ updates, all attachments on $C$ return.

A component without a path is fixed. In a component with a path, choose one final labelled vertex $a$. Its head visits all $|C|$ distinct cycle labels, so its first return is exactly at time $|C|$. Labels are not identified by an unlabelled symmetry. Components update independently, and their return times synchronize precisely at the least common multiple in [\[eq:period\]](#eq:period){reference-type="eqref" reference="eq:period"}. The empty function obeys the same convention.

# Every inverse fibre and its unique maximum {#sec:inverse}

This inverse argument does not use the recurrent classification. Given $g\in\mathcal X_n$, put $E_+(g)=\{i\in[n]:i<g(i)\}$. For $S\subseteq E_+(g)$ select precisely the arrows $i\to g(i)$ with $i\in S$. Call $S$ *admissible* when $$\label{eq:admissible}
 \begin{split}
 &(g(i))_{i\in S}\text{ are pairwise distinct},\\
 &(g(j))_{j\notin S}\text{ are pairwise distinct}.
 \end{split}$$ The first condition gives selected indegree at most one. Since every selected arrow strictly increases its label, the selected graph consists of disjoint increasing paths and singleton vertices. Its endpoints are exactly the vertices outside $S$. Let $e_S(i)$ be the endpoint of the path containing $i$.

[\[thm:inverse\]]{#thm:inverse label="thm:inverse"} For every target $g\in\mathcal X_n$, the assignment $S\mapsto f_S$ defined by $$\label{eq:decoder}
 f_S(i)=g(e_S(i))$$ is a bijection from admissible subsets $S\subseteq E_+(g)$ to $T^{-1}(g)$. Consequently $$\label{eq:fibre}
 |T^{-1}(g)|=\#\{S\subseteq E_+(g):S\text{ satisfies }\eqref{eq:admissible}\},$$ including zero fibres and the unique empty target.

Suppose $T(f)=g$ and select every nonmaximal member of every old fibre. The selected arrows are the consecutive increasing links of these fibres, so their heads are distinct. Each path endpoint is a fibre maximum, where $g$ retains the old fibre value. Distinct old fibres have distinct values, proving the second condition in [\[eq:admissible\]](#eq:admissible){reference-type="eqref" reference="eq:admissible"}. Every coordinate of a fibre has its endpoint's value in $f$, yielding [\[eq:decoder\]](#eq:decoder){reference-type="eqref" reference="eq:decoder"}.

Conversely take an admissible $S$. The selected paths are disjoint and increasing. Assigning to each path its endpoint's $g$-value gives $f_S$. By the second condition of [\[eq:admissible\]](#eq:admissible){reference-type="eqref" reference="eq:admissible"}, its fibres are exactly the path vertex sets, with no unintended merger. Threading them restores the selected arrows and retains $g$ at each endpoint, so $T(f_S)=g$. Recovering all nonmaximal members of these fibres recovers $S$, proving injectivity as well as surjectivity. For the empty target the empty selection reconstructs the empty function.

The selection is not the set of coordinates that change numerically. For example $T(1,1)=(1,1)$, but its predecessor code selects coordinate $0$. Nor are these increasing inverse-code paths the arbitrary-labelled feeding paths of Theorem [\[thm:recurrent\]](#thm:recurrent){reference-type="ref" reference="thm:recurrent"}.

[\[thm:maximum\]]{#thm:maximum label="thm:maximum"} For $n\ge1$, the maximum one-step fibre has size $2^{n-1}$, attained only at $$\label{eq:successor}
 g_*(i)=i+1\quad(0\le i<n-1),\qquad g_*(n-1)=0.$$ At $n=0$ the unique target has fibre one.

For $n\ge1$, the largest label is not eligible. Theorem [\[thm:inverse\]](#thm:inverse){reference-type="ref" reference="thm:inverse"} therefore gives $$\label{eq:boolean-bound}
 |T^{-1}(g)|\le2^{|E_+(g)|}\le2^{n-1}.$$ For $g_*$ the eligible arrows form $0\to1\to\cdots\to n-1$. Every subset has distinct heads, and every set of endpoints has distinct values because $g_*$ is a permutation. Thus all $2^{n-1}$ subsets work.

If equality holds in [\[eq:boolean-bound\]](#eq:boolean-bound){reference-type="eqref" reference="eq:boolean-bound"}, then all $n-1$ lower labels are eligible and every subset is admissible. Taking $S=\varnothing$ shows that $g$ is a permutation. Since $g(i)>i$ for every $i<n-1$, downward elimination forces $g(n-2)=n-1$, then $g(n-3)=n-2$, and eventually $g(0)=1$. The remaining value is $g(n-1)=0$. At $n=1$ the only permutation is already $(0)$ and its fibre is one. The empty case follows directly from the definition.

# Finite checks and limitations

The companion standalone program enumerates every endofunction for $n=0,\ldots,5$, a total of $1+1+4+27+256+3125=3414$ states. It constructs the literal transition independently of the graph predicate, follows each whole-function orbit, and compares recurrence and exact period with Theorem [\[thm:recurrent\]](#thm:recurrent){reference-type="ref" reference="thm:recurrent"}. For every target it enumerates all eligible subsets and compares the decoded source set with the complete literal predecessor set, then checks every equality target in Theorem [\[thm:maximum\]](#thm:maximum){reference-type="ref" reference="thm:maximum"}. It also checks all vertex-image inclusions in the finite boxes and retains selected numerically unchanged arrows. Complete per-state output, not merely summary counts, is the canonical verification payload. These finite checks pressure the deductive proofs; they are not their justification.

The recurrent theorem does not determine a sharp entrance-time bound for arbitrary starting functions. Observed orbit entrance indices in the finite output make no all-size claim. We also assert no general-time inverse, recurrent generating function, arbitrary-size period census or unrestricted owner-nonexistence result. The source comparison is bounded, and the familiar local rewiring, path-cover and rotation mechanisms are credited. The conclusions are the exact labelled recurrent geometry and the independent all-target inverse with its unique extremizer.
