---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-goldfish-positive-root-pencil-scattering-route-a"
canonical_tex: "henon_dynamics/henon_goldfish_positive_root_pencil_scattering_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_goldfish_positive_root_pencil_scattering_route_a/paper/main.pdf"
source_sha256: "83bf4f66a0dc56c48c7cd6f0d655085b5a582a7a9badf8c42f170228ca600710"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Positive-Velocity Goldfish Flow: Global Root Interlacing and One-Carrier Scattering

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_goldfish_positive_root_pencil_scattering_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_goldfish_positive_root_pencil_scattering_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_goldfish_positive_root_pencil_scattering_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_goldfish_positive_root_pencil_scattering_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For arbitrary ordered real positions and strictly positive velocities, we prove that the Calogero goldfish polynomial pencil has simple real roots at every real time. A decreasing partial-fraction map gives exact signed-time interlacing, global collision avoidance, and strict coordinate monotonicity. \>0 The fixed roots of the invariant polynomial become scattering anchors: we derive their positive first inverse-time coefficients and, by an exact Vieta law, the intercept and first correction of the unique ballistic root. The carrier moves from the leftmost incoming rank to the rightmost outgoing rank, with sharp failures on the boundary of the positive cone. \>1 Exact rational, Sturm, high-precision, replay, and hostile-mutation evidence audits the formulas while preserving classical ownership and the strict Route-A boundary.
author:
- 'Route-A source-local certificate HCS-C315'
date: 3 September 2026
title: |
  Positive-Velocity Goldfish Flow:\
  Global Root Interlacing and One-Carrier Scattering
```

## Markdown 正文

trailerid \[\<C3152026090300000000000000000000\>\<C3152026090300000000000000000000\>\]

# Polynomial linearization and global interlacing

Fix $N\geq2$, positions $x_1<\cdots<x_N$, and velocities $v_i>0$. Define $$\label{eq:pencil}
 P(z)=\prod_{i=1}^N(z-x_i),\qquad
 Q(z)=\sum_{i=1}^Nv_i\prod_{j\ne i}(z-x_j),\qquad
 p(z,t)=P(z)-tQ(z).$$ Let $y_1<\cdots<y_{N-1}$ denote the roots of $Q$.

[\[thm:global\]]{#thm:global label="thm:global"} For every $t\in\mathbb R$, $p(\cdot,t)$ has $N$ simple real roots $z_1(t)<\cdots<z_N(t)$. They obey $$\begin{aligned}
 t>0:&\quad x_i<z_i(t)<y_i\ (i<N),\qquad x_N<z_N(t),\label{eq:pos}\\
 t<0:&\quad z_1(t)<x_1,\qquad y_i<z_{i+1}(t)<x_{i+1}\ (i<N).
 \label{eq:neg}\end{aligned}$$ Every $\dot z_i$ is positive, $\sum_i\dot z_i=V:=\sum_i v_i$, and $$\label{eq:goldfish}
 \ddot z_i=2\sum_{j\ne i}\frac{\dot z_i\dot z_j}{z_i-z_j}.$$ Thus [\[eq:pencil\]](#eq:pencil){reference-type="eqref" reference="eq:pencil"} is a complete collision-free goldfish solution with $z_i(0)=x_i$ and $\dot z_i(0)=v_i$.

Off the poles $x_i$, partial fractions give $$\label{eq:R}
 R(z):=\frac{Q(z)}{P(z)}=\sum_{i=1}^N\frac{v_i}{z-x_i},
 \qquad R'(z)=-\sum_{i=1}^N\frac{v_i}{(z-x_i)^2}<0.$$ Hence $R=0$ has exactly one root $y_i$ in each interval $(x_i,x_{i+1})$. When $t\ne0$, $p(z,t)=0$ is equivalent to $R(z)=1/t$. Strict decrease and the one-sided pole limits give exactly the intervals in [\[eq:pos\]](#eq:pos){reference-type="eqref" reference="eq:pos"}--[\[eq:neg\]](#eq:neg){reference-type="eqref" reference="eq:neg"}, including the sign-selected exterior interval. All roots are simple. At $t=0$ they are the simple roots of $P$, so this construction covers all real time.

For $t\ne0$, differentiation of $R(z_i(t))=1/t$ gives $$\label{eq:velocity}
 \dot z_i=-\frac1{t^2R'(z_i)}>0.$$ At zero, implicit differentiation instead gives $\dot z_i(0)=Q(x_i)/P'(x_i)=v_i$. The coefficient of $z^{N-1}$ in $p$ gives the exact law $$\label{eq:vieta}
 \sum_i z_i(t)=\sum_i x_i+Vt,$$ and therefore $\sum_i\dot z_i=V$. Differentiating $p(z,t)=\prod_i(z-z_i(t))$ in $t$ shows that the time-independent $Q$ is $$\label{eq:invariant}
 Q(z)=\sum_i\dot z_i(t)\prod_{j\ne i}(z-z_j(t)).$$ At a root $z_i$, elementary logarithmic differentiation gives $$\begin{aligned}
 \frac{p_{zz}}{p_z}&=2\sum_{j\ne i}\frac1{z_i-z_j},\label{eq:pzz}\\
 \frac{Q'}{p_z}&=\sum_{j\ne i}\frac{\dot z_i+\dot z_j}{z_i-z_j}.
 \label{eq:qprime}\end{aligned}$$ Twice differentiating $p(z_i(t),t)=0$ and inserting [\[eq:pzz\]](#eq:pzz){reference-type="eqref" reference="eq:pzz"}--[\[eq:qprime\]](#eq:qprime){reference-type="eqref" reference="eq:qprime"} yields [\[eq:goldfish\]](#eq:goldfish){reference-type="eqref" reference="eq:goldfish"}. Finally, $p(z,t+s)=p(z,t)-sQ(z)$ proves the exact flow group law.

\>0

# One-carrier scattering and boundary sharpness

Put $$\label{eq:data}
 M=\sum_i v_ix_i,\qquad c=\frac MV,\qquad
 \beta_i=-\frac{P(y_i)}{Q'(y_i)},\qquad B=\sum_{i=1}^{N-1}\beta_i.$$

[\[thm:scatter\]]{#thm:scatter label="thm:scatter"} Every $\beta_i$ is positive. As $t\to-\infty$, $$\begin{aligned}
 z_1(t)&=Vt+c+\frac Bt+O(t^{-2}),\label{eq:ballminus}\\
 z_{i+1}(t)&=y_i-\frac{\beta_i}{t}+O(t^{-2})\quad(i<N),
 \label{eq:finminus}\end{aligned}$$ whereas, as $t\to+\infty$, $$\begin{aligned}
 z_i(t)&=y_i-\frac{\beta_i}{t}+O(t^{-2})\quad(i<N),
 \label{eq:finplus}\\
 z_N(t)&=Vt+c+\frac Bt+O(t^{-2}).\label{eq:ballplus}\end{aligned}$$ All expansions differentiate termwise. Thus the incoming velocity vector tends to $(V,0,\ldots,0)$ and the outgoing vector to $(0,\ldots,0,V)$ in rank order.

At a simple zero $y_i$ of $Q$, the implicit-function theorem with $s=1/t$ applied to $sP(z)-Q(z)=0$ gives $$\label{eq:finite-expansion}
 z=y_i+\frac{P(y_i)}{tQ'(y_i)}+O(t^{-2})
   =y_i-\frac{\beta_i}{t}+O(t^{-2}).$$ Since $y_i\in(x_i,x_{i+1})$, the signs of $P(y_i)$ and $Q'(y_i)$ are opposite; hence $\beta_i>0$. Comparing the two leading coefficients in $Q=V\prod_i(z-y_i)$ yields $$\label{eq:anchor-sum}
 \sum_{i=1}^{N-1}y_i=\sum_{i=1}^Nx_i-c.$$ Subtracting all finite expansions [\[eq:finite-expansion\]](#eq:finite-expansion){reference-type="eqref" reference="eq:finite-expansion"} from the exact sum [\[eq:vieta\]](#eq:vieta){reference-type="eqref" reference="eq:vieta"}, and using [\[eq:anchor-sum\]](#eq:anchor-sum){reference-type="eqref" reference="eq:anchor-sum"}, gives the ballistic expansions including the $B/t$ term. Interlacing [\[eq:pos\]](#eq:pos){reference-type="eqref" reference="eq:pos"}--[\[eq:neg\]](#eq:neg){reference-type="eqref" reference="eq:neg"} fixes their ordered ranks. Analyticity in $s$ justifies differentiated remainders and completes the velocity claim.

The strict positive cone is sharp. For $x=(0,1)$ and $v=(1,0)$, $p=(z-1)(z-t)$ collides at $t=1$. For $v=(1,-1)$, $p=z^2-z+t$ has a double root at $t=1/4$ and nonreal roots afterwards. The $N=1$ face is a free particle; coincident initial positions are singular; all-negative velocities follow by time reversal but are not merged into Theorems [\[thm:global\]](#thm:global){reference-type="ref" reference="thm:global"}--[\[thm:scatter\]](#thm:scatter){reference-type="ref" reference="thm:scatter"}.

\>1

# Evidence, collisions, and Route-A boundary

Fourteen rational cases in dimensions two through seven supply 98 signed-time rows, 413 root-time cells, 45 fixed anchors, 28 asymptotic rows, and 1,892 audited evidence leaves. An independent checker performs 2,047 checks; SymPy closes seven identity groups; isolated replay is byte exact; and 45 repaired-hash, stale-hash, strict-parser and optimized-Python attacks must fail. Exact Sturm intervals certify every sampled real-root statement. The evidence regresses formulas; the proofs own arbitrary finite $N$ and untruncated time.

C196 treats repulsive inverse-square Calogero--Moser motion through a Hermitian eigenvalue pencil and $N$ asymptotic free velocities. C292 uses sticky merger resolution, while C296 uses event-driven elastic hard-rod relabeling. None owns this smooth velocity-coupled pencil or its one-carrier positive-cone scattering theorem.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).$$ The arbitrary continuous data have no prime owner or logarithmic clock; strict monotonicity supplies no primitive periodic ledger; and no target determinant or Weil compression is defined. Polynomial linearization is only a formal A4 hint, not a canonical self-adjoint quantization. Route A is rejected and Route B remains locked. No target local data, Euler factors, root number, automorphy, divisor/counting law, functional equation, zero match, or Hilbert--Pólya operator is asserted.

#### AI use.

A generative language model assisted drafting and code scaffolding. The displayed proofs, independent reconstruction, hostile tests and deterministic artifacts define the audit record.

# Source lineage {#source-lineage .unnumbered}

9 F. Calogero, "The 'neatest' many-body problem amenable to exact treatments (a 'goldfish'?)," *Physica D* 152--153 (2001), 78--84. DOI: [10.1016/S0167-2789(01)00160-9](https://doi.org/10.1016/S0167-2789(01)00160-9). F. Calogero, "Motion of poles and zeros of special solutions of nonlinear and linear partial differential equations, and related 'solvable' many-body problems," *Nuovo Cimento B* 43 (1978), 177--241. Handle: [11573/11324](http://hdl.handle.net/11573/11324). M. C. Nucci, "Calogero's 'goldfish' is indeed a school of free particles," *Journal of Physics A* 37 (2004), 11391--11400. DOI: [10.1088/0305-4470/37/47/008](https://doi.org/10.1088/0305-4470/37/47/008).
