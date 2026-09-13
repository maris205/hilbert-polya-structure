---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-uniform-random-mapping-functional-graph-route-a"
canonical_tex: "henon_dynamics/henon_uniform_random_mapping_functional_graph_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_uniform_random_mapping_functional_graph_route_a/paper/main.pdf"
source_sha256: "422b339d69e86bf9cb937918ef7da04a027dfb6996ab2d073b94cab650df2ad2"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Uniform Random Mapping Functional-Graph Closure: Exact Cycle--Component Counts and Marked-Orbit Limits

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_uniform_random_mapping_functional_graph_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_uniform_random_mapping_functional_graph_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_uniform_random_mapping_functional_graph_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_uniform_random_mapping_functional_graph_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a uniform random function $f:[n]\to[n]$, we give a self-contained uniform random mapping functional-graph closure. Decomposing the graph into a permutation and a rooted forest yields the exact joint count of cyclic vertices and components, its marginal, and every expected cycle count. \>0 An ordered-prefix argument gives the complete tail--cycle law of a marked orbit, identifies its collision length in distribution with the number of cyclic vertices, and proves their common Rayleigh limit. \>1 Conditional uniformity then gives the two-dimensional limiting density $e^{-(x+y)^2/2}$; exhaustive independent computation audits every map through $n=7$ without replacing the all-size proof.
author:
- 'Route-A source-local certificate HCS-C276'
date: 1 September 2026
title: |
  Uniform Random Mapping Functional-Graph Closure:\
  Exact Cycle--Component Counts and Marked-Orbit Limits
```

## Markdown 正文

trailerid \[\<C2762026090100000000000000000000\>\<C2762026090100000000000000000000\>\]

# Model and theorem

Choose each of the $n^n$ functions $f:[n]\to[n]$ with equal probability. Its directed functional graph has edges $v\to f(v)$. Let $C_n$ be the number of cyclic vertices and $K_n$ its number of weak components. Write $c(k,r)$ for the unsigned Stirling number of the first kind and $(n)_{k}=n(n-1)\cdots(n-k+1)$.

[\[thm:main\]]{#thm:main label="thm:main"} For $1\le r\le k\le n$, $$\#\{f:C_n=k,K_n=r\}
 =\binom nk c(k,r)\,k n^{n-k-1},\label{eq:joint}$$ where the last factor means the unique empty forest when $k=n$. Hence $$\mathbb P(C_n=k)=\frac{(n)_{k}\,k}{n^{k+1}},\qquad
 \mathbb EZ_{n,\ell}=\frac{(n)_{\ell}}{\ell n^\ell}.\label{eq:marginal}$$ where $Z_{n,\ell}$ counts directed $\ell$-cycles. \>0 Fix a starting vertex. If $\mu$ is its tail length, $\lambda$ its eventual cycle length, and $R_n=\mu+\lambda$, then $$\mathbb P(\mu=u,\lambda=\ell)
 =\frac{(n-1)_{u+\ell-1}}{n^{u+\ell}}
 \quad(u\ge0,\ \ell\ge1,\ u+\ell\le n).\label{eq:marked}$$ $R_n\overset d=C_n$, and both variables divided by $\sqrt n$ converge to the Rayleigh density $x e^{-x^2/2}\mathbf 1_{x\ge0}$. \>1 Moreover, $$(\mu/\sqrt n,\lambda/\sqrt n)\Rightarrow(U,V),\qquad
 f_{U,V}(x,y)=e^{-(x+y)^2/2}\mathbf 1_{x,y\ge0}.\label{eq:jointlimit}$$

These distributions are classical random-mapping statistics [@Harris1960; @FO1990]. Our contribution is a source-locked proof synthesis and executable boundary audit, not a literature-priority claim.

# Permutation and forest proof

Fix the set $S$ of $k$ cyclic labels. The restriction to $S$ is a permutation, and $c(k,r)$ permutations have $r$ cycles. Every label outside $S$ lies in an in-tree directed toward a root in $S$. The corresponding complete-graph Laplacian minor, of size $m=n-k$, is $$L_S=nI_m-J_m.$$ For $m>0$ its eigenvalues are $k$ once and $n$ with multiplicity $m-1$, so $\det L_S=k n^{n-k-1}$. At $m=0$ the empty determinant is one. Choosing $S$, its permutation, and this forest is bijective with the maps in [\[eq:joint\]](#eq:joint){reference-type="eqref" reference="eq:joint"}.

Summing over $r$ and using $\sum_r c(k,r)=k!$ gives $$\#\{f:C_n=k\}=\binom nk k!\,k n^{n-k-1}.$$ After division by $n^n$, this is the first formula in [\[eq:marginal\]](#eq:marginal){reference-type="eqref" reference="eq:marginal"}. There are $\binom n\ell(\ell-1)!=(n)_{\ell}/\ell$ possible directed $\ell$-cycles. Each prescribes $\ell$ independent function values and has probability $n^{-\ell}$, so indicator linearity proves the second formula. In particular, $n=1$ gives the single fixed-point map, while $k=n$ reduces [\[eq:joint\]](#eq:joint){reference-type="eqref" reference="eq:joint"} to $c(n,r)$ as it must for permutations.

\>0

# Marked orbit and the Rayleigh bridge

Put $t=u+\ell$. Before its first repeat, the marked orbit visits $t$ distinct labels. After the fixed starting label, the ordered prefix has $(n-1)_{t-1}$ choices. Its next edge is forced to the prefix label at index $u$, and all $n-t$ unexposed function values remain arbitrary. The cell therefore contains $(n-1)_{t-1}n^{n-t}$ maps, proving [\[eq:marked\]](#eq:marked){reference-type="eqref" reference="eq:marked"}.

For each $t$ there are exactly $t$ possible tail positions. Consequently $$\mathbb P(R_n=t)=\frac{t(n-1)_{t-1}}{n^t}
 =\frac{(n)_{t}\,t}{n^{t+1}}=\mathbb P(C_n=t).\label{eq:identity}$$ which proves the finite distributional identity. It also proves that $\mu$ conditional on $R_n=t$ is uniform on $\{0,\ldots,t-1\}$.

No collision during the first $m$ transitions has probability $$\mathbb P(R_n>m)=\frac{(n-1)_{m}}{n^m}
 =\prod_{j=1}^m\left(1-\frac jn\right).\label{eq:survival}$$ For $m=\lfloor x\sqrt n\rfloor$, logarithmic expansion gives $\log\mathbb P(R_n>m)=-m(m+1)/(2n)+O(m^3/n^2)\to-x^2/2$. The bound $\log(1-z)\le-z$ supplies tail tightness, so [\[eq:survival\]](#eq:survival){reference-type="eqref" reference="eq:survival"} converges to the Rayleigh survival function. Equation [\[eq:identity\]](#eq:identity){reference-type="eqref" reference="eq:identity"} transfers the limit to $C_n$. The boundary cells $\mu=0$, $\lambda=1$, and $t=n$ are already included in [\[eq:marked\]](#eq:marked){reference-type="eqref" reference="eq:marked"}, without limiting conventions.

\>1

# The two-dimensional limit

Let $W_n=\mu/R_n$. Given $R_n=t$, this variable is uniform on the grid $\{0,1/t,\ldots,(t-1)/t\}$. The Rayleigh limit implies $R_n\to\infty$ in probability. Conditional Riemann sums therefore show $$(R_n/\sqrt n,W_n)\Rightarrow(S,W),$$ where $S$ has density $s e^{-s^2/2}$ and $W$ is independent uniform on $[0,1]$. Under $(s,w)\mapsto(sw,s(1-w))$, the Jacobian is $s$; cancellation with the radial factor gives [\[eq:jointlimit\]](#eq:jointlimit){reference-type="eqref" reference="eq:jointlimit"}. Its normalization is transparent: $$\int_0^\infty\!\int_0^\infty e^{-(x+y)^2/2}\,dx\,dy
 =\int_0^\infty s e^{-s^2/2}\,ds=1.$$

# Executable certificate and scope

Exact receipts enumerate all 873,612 maps for $1\le n\le7$, closing 84 cycle--component cells, 84 marked cells, and 28 cycle-length aggregates. Formula atlases add 528 cyclic masses, 560 collision tails, and 528 cycle expectations; 28 high-precision samples audit the scaling code. A producer-independent orbit tracer closes 821 assertions, SymPy closes 918 identities, fresh replay is byte-identical, and repaired-hash hostile testing rejects 24/24 changes. These computations audit formulas and boundaries; Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} is proved above.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, ensemble averages supply no arithmetic local datum, Euler factor, root number, automorphy statement, target divisor, functional equation, or Hilbert--Pólya operator. There is also no natural same-clock self-adjoint operator for this random ensemble. The tuple is $$\texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FAIL)},$$ the verdict is `ROUTE_A_REJECTED`, and Route B is disabled.

9 B. Harris, *Probability distributions related to random mappings*, Ann. Math. Statist. **31** (1960), 1045--1062, [doi:10.1214/aoms/1177705677](https://doi.org/10.1214/aoms/1177705677).

P. Flajolet and A. M. Odlyzko, *Random mapping statistics*, Advances in Cryptology---EUROCRYPT '89, LNCS 434 (1990), 329--354, [doi:10.1007/3-540-46885-4\_34](https://doi.org/10.1007/3-540-46885-4_34).
