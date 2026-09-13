---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--205-conflict-triggered-cyclic-increments"
canonical_tex: "symbolic_dynamics/papers/205-conflict-triggered-cyclic-increments/main.tex"
canonical_pdf: "symbolic_dynamics/papers/205-conflict-triggered-cyclic-increments/main.pdf"
source_sha256: "081ab303f7704c0419476d84320aa9d2ff12a7e1c87fad36b2b2b3ceb6c8fd9b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Activation Distances and Extremal Fibres\protect of Conflict-Triggered Cyclic Increments

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/205-conflict-triggered-cyclic-increments>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/205-conflict-triggered-cyclic-increments/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/205-conflict-triggered-cyclic-increments/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/205-conflict-triggered-cyclic-increments/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/205-conflict-triggered-cyclic-increments/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the forward dynamics and time-one inverse of a synchronous colour update on an arbitrary finite simple undirected graph: a vertex increments modulo $q\ge3$ exactly when a neighbor has the same colour. Equal-colour edges persist, so each vertex is stationary until activation and advances forever afterwards. We prove that its first activation time is a shortest-path distance from the initial conflicts, with directed edge weights given by initial colour differences. This yields every iterate, the recurrent core and the sharp maximum entrance time $(q-1)(n-2)$ for $n\ge3$. Independently, all predecessors of a target are reconstructed by binary masks satisfying a total-cover condition and directed predecessor closure. Using a self-contained static bound, we show that the largest time-one fibre over all $n$-vertex graphs and targets is $2^{n-1}-1$ for $n\ge4$, attained exactly by constant targets on stars. The three-vertex exception is a constant target on a triangle, with four predecessors. The inverse characterization does not assume efficient general cover counting.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Activation Distances and Extremal Fibres\
  of Conflict-Triggered Cyclic Increments
```

## Markdown 正文

# The update and its scope

Let $G=(V,E)$ be a finite simple undirected graph, $n=|V|\ge0$, and $q\ge3$. For $x\in(\mathbb Z/q\mathbb Z)^V$, define the simultaneous update $$\label{eq:update}
 F(x)_v=x_v+\mathbf 1\{\text{some }u\sim v\text{ has }x_u=x_v\}\pmod q.$$ Isolated vertices hold. We call an equal-colour edge a conflict and its endpoints active. All tests in [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} use the old state. The entrance $h(x)$ is the least $t\ge0$ for which $F^t(x)$ is periodic. Unlike a proper-colouring algorithm, this update never removes a conflict: both endpoints increment together. The issue is how the resulting clocks activate stationary vertices, and which old conflict sets can produce a given target.

The conflict-detection model of @motskin2009lightweight [Section II-A] already allows a local function of the current colour and one conflict bit; [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} is one deterministic choice in that model. Their Algorithm 1 uses randomized recolouring, so its convergence result does not apply here. The successor-colour trigger in the cyclic cellular automaton differs from our equality trigger [@gravner2018limiting Section 1]: on a monochromatic edge it holds, whereas [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} rotates.

We give two explicit descriptions of [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}. The first uses initial-colour directed arrival distances to determine every forward coordinate, exact entrance and recurrent action. The second uses target colours to characterize all active masks in a one-step inverse and to find its uniform extremizers. Shortest paths and binary reconstruction are standard tools. The inverse uses the established class of $2$-total vertex covers [@fernau2015cover]; general total-cover counting already has complexity results [@molinero2018satisfaction Corollary 2.5]. Our elementary static bound below is supporting material, not a separately claimed new graph-counting theory.

# Exact activation distances {#sec:dynamics}

Let $S(x)$ be the endpoints of the initial conflicts. Give both directed versions of each edge the weights $$w_x(u,v)=(x_v-x_u)\bmod q\in\{0,\ldots,q-1\}.$$ Write $d_x(v)$ for the minimum total weight of a directed path from $S(x)$ to $v$, and set it to $\infty$ if no such path exists. Paths of length zero are allowed. A maximum over no finite distances means zero.

[\[thm:temporal\]]{#thm:temporal label="thm:temporal"} The first conflict time of $v$ is $d_x(v)$. For every integer $t\ge0$, $$\label{eq:iterate}
 F^t(x)_v=
 \begin{cases}
 x_v+\max\{0,t-d_x(v)\}\pmod q,&d_x(v)<\infty,\\
 x_v,&d_x(v)=\infty.
 \end{cases}$$ Moreover, $h(x)=\max_{d_x(v)<\infty}d_x(v)$. A state is recurrent exactly when each connected component is either properly coloured, hence fixed, or has a same-coloured neighbor at every vertex, hence increments globally. Every nonfixed recurrent orbit has exact period $q$. The maximum entrance over all graphs and sources on $n$ vertices is $$H_q(n)=\begin{cases}0,&n\le2,\\(q-1)(n-2),&n\ge3.\end{cases}$$

An active edge remains active after an update, since its two colours increment equally. Thus the active set only grows. If $\tau(v)$ is the first conflict time, then $v$ is stationary through time $\tau(v)$ and increments at each subsequent update. This gives [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"} with $\tau$ in place of $d_x$.

Suppose $u$ first activates at time $a<\infty$. Its colour at that time is $x_u$. Unless a neighbor $v$ activates earlier, its colour is still $x_v$, and it meets the advancing colour of $u$ at time $a+w_x(u,v)$. Consequently $\tau(v)\le\tau(u)+w_x(u,v)$. A zero-weight edge is initially monochromatic, so both its endpoints already have time zero; it cannot spontaneously activate an unseeded region. The edge inequality along every seed path proves $\tau(v)\le d_x(v)$ whenever the latter is finite.

Conversely, suppose $\tau(v)=s>0$. A neighbor $u$ meeting $v$ at time $s$ must have activated earlier. Indeed, if both first activated at $s$, both would still have their initial colours, making their equality an initial conflict. With $a=\tau(u)<s$, the first meeting of that advancing color with the stationary $v$ occurs after exactly $w_x(u,v)$ steps: an earlier congruent meeting would already activate $v$. Hence $s=a+w_x(u,v)$. Repeating backwards strictly decreases activation times until reaching a seed and yields a path of total weight $s$. Thus $d_x(v)\le\tau(v)$. This also excludes finite activation in a seedless component, and proves the first assertion including infinite distances.

Every vertex in a seeded component has finite distance. At the last such arrival all its vertices are active and hence advance together forever; unseeded components are proper and hold forever. Before the last arrival, the active set will strictly increase at a future time, so monotonicity excludes periodicity. These observations prove the exact entrance and the stated recurrent core. If any component advances, a return after $p$ steps forces $p\equiv0\pmod q$ at an advancing vertex, proving its exact period.

A seeded component contains at least two seeds. A minimum-weight path to a nonseed can be chosen simple and with no seed after its starting vertex. It therefore has at most $n-2$ edges, each of weight at most $q-1$. For $n\le2$ there is no seeded component containing a nonseed, giving height zero. For $n\ge3$ take the path $0-1-\cdots-(n-1)$ with $x_0=x_1=0$ and $x_i=-(i-1)\pmod q$ for $i\ge2$. Only the first edge is initially monochromatic. The unique simple seed route to vertex $n-1$ has $n-2$ forward edges of weight $q-1$; deleting any backtracking cannot increase a path's weight. Its distance is $(q-1)(n-2)$, attaining the bound.

# A target decoder and sharp fibres {#sec:inverse}

For a target $y$, let $H_y$ be the spanning graph of its monochromatic edges. Let $D_y$ have an arc $u\to v$ when $u\sim v$ and $y_v=y_u+1\pmod q$. A vertex cover whose induced graph has no isolated vertex is called a $2$-total cover; we allow the empty cover. In particular, isolates of $H_y$ must be outside such a cover.

[\[thm:decoder\]]{#thm:decoder label="thm:decoder"} The predecessors of $y$ are, uniquely, $x_v=y_v-\mathbf 1_A(v)\pmod q$, where $A\subseteq V$ satisfies:

1.  $A$ is a vertex cover of $H_y$;

2.  every vertex of $A$ has a neighbor in $A$ in $H_y$;

3.  an arc $u\to v$ in $D_y$ with $v\in A$ implies $u\in A$.

Let $A$ be the advancing set of any predecessor. Its old colours are necessarily $y-\mathbf 1_A$. Every old equal-colour edge has both endpoints in $A$. For two endpoints in $A$, old equality is exactly target equality; each vertex in $A$ therefore needs an internal $H_y$ neighbor. Two endpoints outside $A$ cannot be equal in the target, since both held. Finally, when $u\notin A$ and $v\in A$, old equality is equivalent to $y_v=y_u+1\pmod q$, which would contradict $u$ holding. These are the three conditions. Conversely they ensure that the endpoints of the old equal-colour edges in $y-\mathbf 1_A$ are exactly $A$. Thus precisely these vertices advance and the image is $y$. Different masks give different old states, completing the bijection.

Write $T(H)$ for the number of $2$-total covers of a simple graph $H$, with our empty-cover convention. Equivalently it counts independent sets $I$ for which $H-I$ has no isolated vertex. The decoder gives $$\label{eq:static-bound}
 |F^{-1}(y)|\le T(H_y).$$ For a constant target, $H_y=G$ and $D_y$ has no arcs, so equality holds. We include the following elementary static support proof to make the dynamical extremum self-contained.

[\[lem:cover-bound\]]{#lem:cover-bound label="lem:cover-bound"} For a graph $H$ on $n\ge4$ vertices, $T(H)\le2^{n-1}-1$, with equality exactly for a star $K_{1,n-1}$. On three vertices, $T(H)\le4$, with equality exactly for a triangle.

For a star on $k\ge3$ vertices the covers consist of the centre and any nonempty set of leaves, giving $2^{k-1}-1$. A single edge has one such cover; on three connected vertices the path has three and the triangle four.

A connected nonstar with at least four vertices contains a four-vertex path as a subgraph. To see this, if a longest path were $a,b,c$, any further vertex can attach only to $b$: attachment to $a$ or $c$, or a longer route from the path, extends it. An edge between leaves, including $a,c$, would also create a four-vertex path. The graph would therefore be a star.

Now suppose a connected nonstar has $k\ge5$ vertices. Choose a four-vertex path and an edge $uv$ from a vertex $u$ of the path to a vertex $v$ outside it. The path has eight independent sets, at least two containing each chosen $u$. Ignoring other edges gives $8\cdot2^{k-4}$ independent sets; the extra edge forbids at least $2\cdot2^{k-5}$ of them. Hence $$T(H)\le i(H)\le7\cdot2^{k-4}<2^{k-1}-1,$$ where $i(H)$ is the number of independent sets and the strict inequality uses $2^{k-4}\ge2$. For $k=4$, the connected graphs are the star, path, paw, four-cycle, diamond and complete graph. Listing independent complements with no isolated vertex left gives, respectively, $7,4,6,5,6,5$. Thus only the star attains seven.

The count $T$ multiplies over components, and an isolate contributes one. A nontrivial component of size $k$ has $T\le2^{k-1}$. Two or more nontrivial components therefore give at most $2^{n-2}<2^{n-1}-1$. One such component with isolates has strictly smaller order and again gives a strict bound, including the triangle count four. An edgeless graph has $T=1$. The three-vertex disconnected cases also have $T=1$. These cases complete the proof and the equality classification.

[\[thm:maximum\]]{#thm:maximum label="thm:maximum"} For any $q\ge3$, the maximum time-one fibre over all graphs and targets on $n$ vertices is $$M(n)=\begin{cases}1,&n\le2,\\4,&n=3,\\2^{n-1}-1,&n\ge4.\end{cases}$$ For $n=3$ the extremizers are exactly constant targets on triangles, and for $n\ge4$ exactly constant targets on stars.

Combine [\[eq:static-bound\]](#eq:static-bound){reference-type="eqref" reference="eq:static-bound"} with Lemma [\[lem:cover-bound\]](#lem:cover-bound){reference-type="ref" reference="lem:cover-bound"}. At equality $H_y$ is a spanning star, or a triangle when $n=3$. Since this monochromatic graph is connected, $y$ is constant on all vertices. Then $H_y=G$, so no extra nonmonochromatic edges are possible. Conversely every constant target on the claimed graph attains $T(G)$. For $n\le2$, an edgeless graph has the identity update; on a single edge, unequal colours hold and equal colours rotate together. This is a permutation and every fibre has size one, including the empty state.

# Scope and reproducibility

The forward formula holds at every time, but the inverse concerns one step. No efficient arbitrary-graph cover counter, all-time inverse or complete basin/recurrent-state census is asserted.

The accompanying standalone `verify.py` compares literal finite orbits with weighted distances and every target's exact source set with the mask decoder. It covers all graphs through four vertices at $q=3,4,5$, all static graphs through six vertices, and the sharp paths for $2\le n\le20$, $3\le q\le9$. Its complete `CANONICAL.json` records $1{,}029{,}769$ assertions. These finite checks pressure the deductions; the all-parameter results follow from the proofs above.
