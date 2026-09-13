---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-erdos-renyi-connectivity-hitting-route-a"
canonical_tex: "henon_dynamics/henon_erdos_renyi_connectivity_hitting_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_erdos_renyi_connectivity_hitting_route_a/paper/main.pdf"
source_sha256: "b2fa5db5f554d5444ac46492ca38923b808906f01269889bc2d8368ec1bcaf5b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Connectivity Hitting in the Random Graph Process: Exact Finite Laws and the Gumbel Window

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_erdos_renyi_connectivity_hitting_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_erdos_renyi_connectivity_hitting_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_erdos_renyi_connectivity_hitting_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_erdos_renyi_connectivity_hitting_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Reveal the $K=\binom n2$ edges of the complete labeled graph in uniform random order, and let $\tau_{\mathrm{conn}}$ be the first connected prefix. Decomposition by the component containing vertex 1 gives an exact recurrence for every connected-graph count, hence the complete finite CDF, PMF, tail, support, and all moments of $\tau_{\mathrm{conn}}$. \>0 At $m=\lfloor(n/2)(\log n+c)\rfloor$, isolated-vertex factorial moments and a uniform spanning-tree bound excluding every other component prove $2\tau_{\mathrm{conn}}/n-\log n\Rightarrow$ the standard Gumbel law. \>1 Small-$n$, rounding, and terminal-edge faces are closed explicitly, together with an independently exhaustive finite certificate and strict claim scope.
author:
- 'Route-A source-local certificate HCS-C307'
date: 3 September 2026
title: |
  Connectivity Hitting in the Random Graph Process:\
  Exact Finite Laws and the Gumbel Window
```

## Markdown 正文

trailerid \[\<C3072026090300000000000000000000\>\<C3072026090300000000000000000000\>\] suppressoptionalinfo 767

# The monotone process and connected counts

Let $e_1,\ldots,e_K$ be a uniformly random permutation of the edges of $K_n$, and put $G_m=(\{1,\ldots,n\},\{e_1,\ldots,e_m\})$. Thus $G_m$ is uniform over the $\binom Km$ labeled graphs with $m$ edges. Edge addition is monotone, and the connected graphs form an absorbing upper set. We take $\tau_{\mathrm{conn}}=\min\{m:G_m\text{ is connected}\}$, with $\tau_{\mathrm{conn}}=0$ when $n=1$.

Write $C(n,m)$ for the number of connected labeled graphs on $n$ vertices with $m$ edges. Set $C(1,0)=1$, and interpret both $C(s,j)$ and binomial coefficients as zero outside their natural ranges.

[\[thm:finite\]]{#thm:finite label="thm:finite"} For $n\geq2$, $K=\binom n2$, and every integer $m$, $$\label{eq:recurrence}
 C(n,m)=\binom Km-\sum_{s=1}^{n-1}\binom{n-1}{s-1}
 \sum_j C(s,j)\binom{\binom{n-s}{2}}{m-j}.$$ Moreover $C(n,m)=0$ for $m<n-1$, $$\label{eq:endpoints}
 C(n,n-1)=n^{n-2},\qquad C(n,K)=1.$$ For $0\leq m\leq K$, with $F_n(-1)=0$, $$\begin{aligned}
 F_n(m):=\mathbb P(\tau_{\mathrm{conn}}\leq m)&=\frac{C(n,m)}{\binom Km},\label{eq:cdf}\\
 \mathbb P(\tau_{\mathrm{conn}}=m)&=F_n(m)-F_n(m-1),\label{eq:pmf}\\
 \mathbb P(\tau_{\mathrm{conn}}>m)&=1-F_n(m).\label{eq:tail}\end{aligned}$$ For every integer $r\geq1$, $$\label{eq:moments}
 \mathbb E[\tau_{\mathrm{conn}}^{\,r}]=\sum_{m=0}^{K-1}\bigl((m+1)^r-m^r\bigr)
 \{1-F_n(m)\}.$$ Finally, for $n\geq2$, $$\label{eq:last}
 n-1\leq\tau_{\mathrm{conn}}\leq\binom{n-1}{2}+1.$$

If a graph is disconnected, let $s$ be the size of the component containing vertex 1. Choose its other $s-1$ labels, choose its connected $j$-edge subgraph, and place every remaining edge among the other $n-s$ vertices. This decomposition is unique and subtracting it from all $m$-edge graphs gives [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}. A connected graph needs at least $n-1$ edges; at equality it is a tree, counted by the Prüfer-code value $n^{n-2}$. The complete graph is unique, proving [\[eq:endpoints\]](#eq:endpoints){reference-type="eqref" reference="eq:endpoints"}.

The first $m$ positions of a uniform edge permutation form a uniform $m$-subset, which proves [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"}. Monotonicity gives [\[eq:pmf\]](#eq:pmf){reference-type="eqref" reference="eq:pmf"}--[\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}. For every nonnegative integer-valued $T$, $T^r=\sum_{m=0}^{T-1}((m+1)^r-m^r)$; expectation proves [\[eq:moments\]](#eq:moments){reference-type="eqref" reference="eq:moments"}. The smallest connected graph is a tree. A disconnected graph has at most $\binom{n-1}{2}$ edges, since convexity maximizes the sum of within-component edge capacities at component sizes $n-1$ and 1. This proves [\[eq:last\]](#eq:last){reference-type="eqref" reference="eq:last"}.

\>0

# The connectivity window

For fixed $c\in\mathbb R$, let $$\label{eq:window}
 m_n(c)=\left\lfloor\frac n2(\log n+c)\right\rfloor .$$ This lies in $[0,K]$ for all sufficiently large $n$. Let $I_n$ be the number of isolated vertices in $G(n,m_n(c))$.

[\[lem:poisson\]]{#lem:poisson label="lem:poisson"} $I_n$ converges in law to $\operatorname{Poisson}(e^{-c})$.

For fixed $r\geq1$, an ordered $r$-tuple is isolated exactly when every chosen edge lies among the other $n-r$ vertices. Hence, with $K=\binom n2$, $$\label{eq:factorial}
 \mathbb E(I_n)_{r\downarrow}=(n)_{r\downarrow}
 \frac{\binom{\binom{n-r}{2}}{m_n(c)}}{\binom K{m_n(c)}}.$$ Put $D_r=K-\binom{n-r}{2}=rn-r(r+1)/2$ and $m=m_n(c)$. Since $m=O(n\log n)$, $$\begin{aligned}
 \log\frac{\binom{K-D_r}{m}}{\binom Km}
 &=\sum_{j=0}^{m-1}\log\left(1-\frac{D_r}{K-j}\right)\\
 &=-D_r\frac mK+O\left(\frac{D_rm^2}{K^2}
                     +\frac{D_r^2m}{K^2}\right)
 =-r(\log n+c)+o(1).\end{aligned}$$ Together with $(n)_{r\downarrow}\sim n^r$, formula [\[eq:factorial\]](#eq:factorial){reference-type="eqref" reference="eq:factorial"} tends to $e^{-rc}$. These are all factorial moments of $\operatorname{Poisson}(e^{-c})$; the factorial-moment criterion proves the claim.

Isolated vertices are the only asymptotically relevant obstruction. The following proof retains the without-replacement law rather than silently switching to $G(n,p)$.

[\[lem:other\]]{#lem:other label="lem:other"} At $m=m_n(c)$, $$\mathbb P\{G(n,m)\text{ is disconnected and }I_n=0\}\longrightarrow0.$$

Let $X_s$ count components with exactly $s$ vertices. If a fixed $s$-set is a component, some one of its $s^{s-2}$ spanning trees is present and all $b=s(n-s)$ crossing edges are absent. For a fixed tree with $a=s-1$ edges, sampling $m$ edges without replacement gives $$\begin{aligned}
 \mathbb P\{A\subseteq G_m,\ B\cap G_m=\varnothing\}
 &=\frac{(m)_{a\downarrow}(K-m)_{b\downarrow}}{(K)_{a+b\downarrow}}\notag\\
 &\leq\left(\frac mK\right)^a
 \exp\left\{-\frac{b(m-a)}{K-a}\right\}.\end{aligned}$$ Consequently $$\label{eq:componentbound}
 \mathbb EX_s\leq\binom ns s^{s-2}\left(\frac mK\right)^{s-1}
 \exp\left\{-\frac{s(n-s)(m-s+1)}{K-s+1}\right\}.$$ Here $m/K\asymp(\log n)/n$. Uniformly for $2\leq s\leq n/\log n$, the exponent in [\[eq:componentbound\]](#eq:componentbound){reference-type="eqref" reference="eq:componentbound"} is at least $s(\log n-O_c(1))$; using $\binom ns\leq(en/s)^s$ and summing gives $$\sum_{2\leq s\leq n/\log n}\mathbb EX_s
 \leq\sum_{s\geq2}n\left(\frac{C_c\log n}{n}\right)^s=o(1).$$ For $n/\log n\leq s\leq n/2$, one has $n-s\geq n/2$ and $m-s+1\geq m/2$ for large $n$. The exponent is then at least $s\log n/8$, while the remaining factors are at most $n(C\log n)^s$. Thus $$\sum_{n/\log n\leq s\leq n/2}\mathbb EX_s
 \leq\sum_{s\geq n/\log n}n
       \left(\frac{C\log n}{n^{1/8}}\right)^s=o(1).$$ If a graph is disconnected and has no isolated vertex, one of its components has size between 2 and $\lfloor n/2\rfloor$. Markov's inequality and the two sums prove the lemma.

[\[thm:gumbel\]]{#thm:gumbel label="thm:gumbel"} For every real $c$, $$\label{eq:gumbel}
 \lim_{n\to\infty}\mathbb P\left\{\frac{2\tau_{\mathrm{conn}}}n-\log n\leq c\right\}
 =\exp\{-e^{-c}\}.$$

Lemmas [\[lem:poisson\]](#lem:poisson){reference-type="ref" reference="lem:poisson"}--[\[lem:other\]](#lem:other){reference-type="ref" reference="lem:other"} give $\mathbb P\{G(n,m_n(c))\text{ connected}\}=\mathbb P(I_n=0)+o(1)
\to\exp\{-e^{-c}\}$. Because $\tau_{\mathrm{conn}}$ is integer, the event on the left of [\[eq:gumbel\]](#eq:gumbel){reference-type="eqref" reference="eq:gumbel"} is exactly $\{\tau_{\mathrm{conn}}\leq m_n(c)\}$; equation [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"} finishes the proof.

\>1

# Boundary, evidence, and Route A

For $n=1$, $K=0$ and $\tau_{\mathrm{conn}}=0$ by convention. For $n=2$, the sole edge arrives at step one, so $\tau_{\mathrm{conn}}=1$. Formula [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"} includes $m=0$ and $m=K$; the upper support in [\[eq:last\]](#eq:last){reference-type="eqref" reference="eq:last"} is no larger than $K$. The floor in [\[eq:window\]](#eq:window){reference-type="eqref" reference="eq:window"} exactly matches the integer hitting event. For finite $n,c$ outside the asymptotic range one may clip a software query to $[0,K]$, but that clipping is not part of Theorem [\[thm:gumbel\]](#thm:gumbel){reference-type="ref" reference="thm:gumbel"}.

The evidence artifact applies [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} through $n=12$, recording 298 exact count/probability cells and the first four moments. An independent checker exhausts all 33,867 labeled graph masks through $n=6$. A separate SymPy lane verifies polynomial component decompositions, tail-moment telescoping, and exact isolated-vertex cells. Finite isolated-factorial decimals are diagnostics only; the limits are owned by the displayed proof.

The deterministic-window equivalence between connectivity and absence of isolated vertices does not assert a pathwise identity between $\tau_{\mathrm{conn}}$ and the time when the last isolated vertex disappears. Equation [\[eq:gumbel\]](#eq:gumbel){reference-type="eqref" reference="eq:gumbel"} is weak convergence only; no convergence of its unbounded moments is claimed. The exact finite process is $G(n,m)$ without replacement, not the independent-edge process $G(n,p)$.

The nearest repository collisions are model-distinct. C301 is a parallel fair-bit partition-refinement birthday process; C291 is random greedy dimer adsorption on finite paths and cycles; and C276 samples a whole uniform random mapping. None uses the without-replacement complete-graph edge clock or owns the exact connectivity-hitting law and its Gumbel window proved here.

The strict Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}).$$ The overall verdict is `ROUTE_A_REJECTED` and Route B is locked. Edge count is not an arithmetic prime clock, graph counts are not target determinants, and no self-adjoint target-zero lift exists. The scope literal is displayed separately: $$\texttt{NO\_BAD\_EULER\_OR\_ROOT\_NUMBER}.$$ No arithmetic local datum, Euler factor, root number, automorphy, target divisor law, functional equation, zero match, or Hilbert--Pólya operator is claimed.

# Source ownership and AI-use statement {#source-ownership-and-ai-use-statement .unnumbered}

Erdős and Rényi [@ER] established the random-graph evolution and connectivity threshold. We claim no priority for that result. The present package supplies a self-contained frozen-model derivation, exact finite hitting atlas, and auditable boundary ledger. AI tools assisted symbolic checks, hostile mutation design, and manuscript preparation; all proof obligations, cutoffs, and nonclaims are explicit.

1 P. Erdős and A. Rényi, "On the evolution of random graphs," *Publications of the Mathematical Institute of the Hungarian Academy of Sciences* 5 (1960), 17--61.
