---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--123-odd-component-complementation"
canonical_tex: "symbolic_dynamics/papers/123-odd-component-complementation/main.tex"
canonical_pdf: "symbolic_dynamics/papers/123-odd-component-complementation/main.pdf"
source_sha256: "15e8193ad8568199aa3b08c13df1e2c61231b6b3ef13ef33fe804c4eb1d3ddb7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Odd-Component Complementation: Pointwise Split Clocks and an All-Depth Labelled Census

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/123-odd-component-complementation>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/123-odd-component-complementation/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/123-odd-component-complementation/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/123-odd-component-complementation/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/123-odd-component-complementation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  On a finite simple labelled graph, synchronously complement the subgraph induced by every connected component of odd order and leave every even component unchanged. We show that the resulting finite dynamics is linearized pointwise by a parity-pruned component/co-component split tree. Its active height is the exact entrance time into the recurrent set, all periods divide two, and the largest transient depth on $n$ vertices is the sharp value $\lfloor(n-1)/2\rfloor$. We then derive a recursive labelled exponential generating function for every cumulative and exact depth layer. It yields the fixed and recurrent censuses, the number of two-cycles, and the finite-order dynamical zeta function. Gallai decomposition, cographs and cotrees, labelled SET calculus, and connected-graph enumeration are treated as background. The direct-owner search is bounded; no novelty, priority, or external-release claim is made.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Odd-Component Complementation:\
  Pointwise Split Clocks and an All-Depth Labelled Census
```

## Markdown 正文

# The map and the subtraction boundary

All graphs are finite, simple, and labelled. For a graph $G$, define $$\Phi(G)=\bigsqcup_{C\in\operatorname{Comp}(G)}
 \begin{cases}
   \overline{G[C]},& |C|\text{ odd},\\
   G[C],& |C|\text{ even}.
 \end{cases}                                             \label{eq:map}$$ Thus no edge is added between distinct components, and every odd component is complemented synchronously. We regard $K_1$ as connected and co-connected. The *depth* of a state is its first entrance time into the recurrent set.

Component/co-component decomposition belongs to classical modular decomposition, beginning with Gallai's work [@Gallai1967]. Cographs, their cotrees, and recognition are likewise classical [@CorneilLerchsStewart1981; @CorneilPerlStewart1985]; modern labelled cotree enumeration appears, for example, in [@Stufler2021; @BassinoEtAl2022]. Labelled SET constructions and connected-graph enumeration are standard [@BergeronLabelleLeroux1998; @HararyPalmer1973]. None of those facts, nor the co-connected count used below, receives contribution credit here. Our residual question is temporal: what is the exact clock of the literal parity-triggered map [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}, and can every clock layer be counted?

[\[lem:refinement\]]{#lem:refinement label="lem:refinement"} The component partition of $\Phi(G)$ refines that of $G$. Every even component is fixed forever. If $H$ is odd and connected, then either $\overline H$ is connected and $H\leftrightarrow\overline H$, or the components of $\overline H$ are permanent separate blocks after one step.

Equation [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} never creates a cross-component edge. An even block is copied unchanged. On an odd connected block $H$, one step produces $\overline H$. If that graph is connected, the next step complements it back to $H$. If it is disconnected, no later step can join its components, so they evolve independently.

# The pointwise split clock

The classical component/co-component tree is useful here only after a parity pruning that records which blocks remain dynamically active.

[\[def:tree\]]{#def:tree label="def:tree"} For a connected odd graph $H$, build its *parity-pruned split tree* as follows. If $\overline H$ is connected, stop. Otherwise create the connected components of $\overline H$ as children; declare every even child a leaf and recurse only on odd children. Let $D(H)$ be the largest number of split nodes on a root-to-leaf branch. Equivalently, $$D(H)=
\begin{cases}
0,&\overline H\text{ connected},\\
1+\max\{D(C):C\in\operatorname{Comp}(\overline H),\ |C|\text{ odd}\},
   &\overline H\text{ disconnected},
\end{cases}                                               \label{eq:D}$$ where the maximum of the empty set is $0$. For arbitrary $G$, put $D(G)=\max D(C)$ over its odd components, with empty maximum $0$.

This is not asserted to be a new cotree or modular decomposition. It is a pointwise clock obtained by pruning the familiar split operation according to the update parity.

[\[thm:clock\]]{#thm:clock label="thm:clock"} For every graph $G$, $$\operatorname{depth}(G)=D(G).$$

Even components are recurrent fixed blocks. Distinct odd components evolve independently, so the entrance time of their disjoint union is the maximum of their entrance times. It remains to consider an odd connected $H$. If $\overline H$ is connected, $H$ already lies on a cycle. Otherwise the first step splits $H$ into the components of $\overline H$. Its even children freeze, while its odd children require exactly their individual entrance times. Hence the entrance time satisfies precisely [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"}; induction on $|H|$ finishes the proof.

[\[cor:period\]]{#cor:period label="cor:period"} Every eventual period is $1$ or $2$. A graph is recurrent exactly when every nontrivial odd component is co-connected. It is fixed exactly when every component is either a singleton or has even order. Every other recurrent graph lies on a genuine two-cycle.

Theorem [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"} reduces every state to leaves of the split tree. Even leaves are fixed. A singleton is fixed by complementation, whereas a nontrivial odd co-connected component alternates with its connected complement. A disjoint union synchronizes these periods.

# The sharp global clock

[\[thm:sharp\]]{#thm:sharp label="thm:sharp"} Among all graphs on $n\geq1$ vertices, $$\max_{|V(G)|=n}\operatorname{depth}(G)=\left\lfloor\frac{n-1}{2}\right\rfloor.
                                                               \label{eq:sharp}$$ The value for $n=0$ is $0$.

Follow an active branch from an odd parent $H$ to an odd child $C$. The complement $\overline H$ has at least two components, and the vertices outside $C$ have even positive total order because both $|H|$ and $|C|$ are odd. Thus $|C|\leq |H|-2$. Every split consumes at least two vertices along the branch, giving $D(H)\leq (|H|-1)/2$. Taking the maximum over odd components proves the upper bound for every $G$.

For sharpness, let $H_1=K_1$ and recursively set $$H_{2r+1}=\overline{\,H_{2r-1}\sqcup K_2\,}.$$ The complement of $H_{2r+1}$ has the odd child $H_{2r-1}$ and the even child $K_2$, so $D(H_{2r+1})=1+D(H_{2r-1})=r$. This attains [\[eq:sharp\]](#eq:sharp){reference-type="eqref" reference="eq:sharp"} for odd order. For even $n=2r+2$, the graph $H_{2r+1}\sqcup K_1$ has depth $r$, proving sharpness there as well.

The bound is structural, not an extrapolation from the finite census in [5](#sec:census){reference-type="ref" reference="sec:census"}.

# All-depth labelled generating functions

Let $c_n$ be the number of connected labelled graphs on $[n]$, and work throughout with formal exponential generating functions. Put $$C_{\mathrm e}(x)=\sum_{\substack{n\geq2\\n\ {\rm even}}}
 c_n\frac{x^n}{n!}.$$ For odd $n$, let $q_n$ count connected graphs whose complements are also connected, and define $$q_1=1,\qquad q_n=2c_n-2^{\binom n2}\quad(n\geq3\text{ odd}),\qquad
 Q(x)=\sum_{n\ {\rm odd}}q_n\frac{x^n}{n!}.               \label{eq:Q}$$ Indeed, a graph and its complement cannot both be disconnected when $n\geq2$, so [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"} is inclusion--exclusion; this identity is zero-credit background. For a series $A(x)$, write $\operatorname{Odd}A=(A(x)-A(-x))/2$.

[\[thm:egf\]]{#thm:egf label="thm:egf"} Let $O_t(x)$ be the EGF of connected odd graphs of depth at most $t$, and let $F_t(x)$ be the EGF of all graphs of depth at most $t$. Then $$\begin{aligned}
 O_0(x)&=Q(x),                                             \label{eq:O0}\\
 O_t(x)&=Q(x)+\operatorname{Odd}\!\left(
  \exp(C_{\mathrm e}(x)+O_{t-1}(x))-1-C_{\mathrm e}(x)-O_{t-1}(x)
                         \right),\qquad t\geq1,           \label{eq:Ot}\\
 F_t(x)&=\exp(C_{\mathrm e}(x)+O_t(x)).                   \label{eq:Ft}\end{aligned}$$ Consequently, for $t\geq1$, the number of labelled $n$-vertex graphs of exact depth $t$ is $$n![x^n]\bigl(F_t(x)-F_{t-1}(x)\bigr),                    \label{eq:layers}$$ while $n![x^n]F_0(x)$ is the recurrent count.

Depth-zero connected odd graphs are precisely the co-connected ones, giving [\[eq:O0\]](#eq:O0){reference-type="eqref" reference="eq:O0"}. Consider a positive-depth connected odd graph $H$. Complementation bijects it with a disconnected labelled graph whose connected components have odd total order. Its even components are unrestricted connected graphs, counted by $C_{\mathrm e}$; by [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"}, every odd component has depth at most $t-1$, counted by $O_{t-1}$. The labelled SET construction gives the exponential in [\[eq:Ot\]](#eq:Ot){reference-type="eqref" reference="eq:Ot"}; subtracting $1+C_{\mathrm e}+O_{t-1}$ forces at least two components, and odd extraction forces odd total order. Adding the co-connected base class $Q$ proves [\[eq:Ot\]](#eq:Ot){reference-type="eqref" reference="eq:Ot"}.

An arbitrary graph of depth at most $t$ is a SET of unrestricted even connected components and odd connected components counted by $O_t$. The exponential formula gives [\[eq:Ft\]](#eq:Ft){reference-type="eqref" reference="eq:Ft"}, and subtraction of successive cumulative classes gives [\[eq:layers\]](#eq:layers){reference-type="eqref" reference="eq:layers"}.

[\[prop:fixed\]]{#prop:fixed label="prop:fixed"} The EGF for fixed graphs is $$F_{\mathrm{fix}}(x)=\exp(x+C_{\mathrm e}(x)).            \label{eq:Ffix}$$

By [\[cor:period\]](#cor:period){reference-type="ref" reference="cor:period"}, the allowed connected components are singletons and arbitrary even connected graphs. Apply the labelled SET construction.

# Recurrent and zeta census {#sec:census}

Write $$f_n=n![x^n]F_{\mathrm{fix}}(x),\qquad
 r_n=n![x^n]F_0(x).$$ Thus $f_n$ and $r_n$ are respectively the fixed and recurrent state counts on the finite state space of labelled graphs on $[n]$.

[\[cor:zeta\]]{#cor:zeta label="cor:zeta"} The number of genuine two-cycles is $(r_n-f_n)/2$. Moreover, $$\#\operatorname{Fix}(\Phi^k)=
 \begin{cases}f_n,&k\text{ odd},\\r_n,&k\text{ even},\end{cases}
 \qquad
 \zeta_n(z)=\exp\!\left(\sum_{k\geq1}\frac{\#\operatorname{Fix}(\Phi^k)}{k}z^k\right)
 =(1-z)^{-f_n}(1-z^2)^{-(r_n-f_n)/2}.                    \label{eq:zeta}$$

Corollary [\[cor:period\]](#cor:period){reference-type="ref" reference="cor:period"} partitions the recurrent set into $f_n$ one-cycles and $(r_n-f_n)/2$ two-cycles. Transient states are fixed by no positive iterate. Hence the displayed fixed-iterate counts hold. Splitting the defining Artin--Mazur series [@ArtinMazur1965] into odd and even powers and applying the logarithmic series gives [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

For orientation, exact coefficients and exhaustive orbits give:

    $n$    $f_n$    $r_n$   two-cycles   maximum depth
  ----- -------- -------- ------------ ---------------
      0        1        1            0               0
      1        1        1            0               0
      2        2        2            0               0
      3        4        4            0               1
      4       48       48            0               1
      5      216      648          216               2
      6   27,920   30,512        1,296               2

The paper-local verifier exhausts every labelled graph through $n=6$. It compares literal orbit depth with a separately evaluated split tree, checks the refinement and fixed/recurrent criteria state by state, checks periods and depth histograms, and independently assembles the coefficients of [\[eq:Ot\]](#eq:Ot){reference-type="eqref" reference="eq:Ot"}--[\[eq:Ft\]](#eq:Ft){reference-type="eqref" reference="eq:Ft"}. It executes 203,244 exact assertions. These computations test definitions and translations; the all-order conclusions rest on the proofs above.

# Scope and conclusion

The parity-pruned split tree simultaneously exposes the pointwise and enumerative structure of odd-component complementation. It gives an exact entrance clock, the sharp maximum $\lfloor(n-1)/2\rfloor$, and a recursive EGF for every temporal layer. The recurrent and fixed specializations then produce the two-cycle and zeta censuses without further orbit analysis.

The contribution boundary is deliberately narrow. Gallai decomposition, cographs and cotrees, connected labelled graph counts, and labelled species operators remain zero-credit background. The direct-owner search was bounded rather than exhaustive, and the finite verifier stops at order six. Accordingly, this manuscript makes no novelty or priority assertion and is held from external release pending a broader owner audit.
