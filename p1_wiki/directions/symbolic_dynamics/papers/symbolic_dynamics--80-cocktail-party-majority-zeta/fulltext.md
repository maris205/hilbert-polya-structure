---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--80-cocktail-party-majority-zeta"
canonical_tex: "symbolic_dynamics/papers/80-cocktail-party-majority-zeta/main.tex"
canonical_pdf: "symbolic_dynamics/papers/80-cocktail-party-majority-zeta/main.pdf"
source_sha256: "68d5cccd0a3639ba36205e3bfe370c75003a5fc5ceb26e0edb846df081711aa7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact State Partition, Zeta Function, and Critical Window for Majority Dynamics on Cocktail-Party Graphs

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/80-cocktail-party-majority-zeta>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/80-cocktail-party-majority-zeta/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/80-cocktail-party-majority-zeta/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/80-cocktail-party-majority-zeta/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/80-cocktail-party-majority-zeta/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $\operatorname{CP}_n=K_{2n}\setminus M$ be the cocktail-party graph obtained by deleting a perfect matching, and apply synchronous strict majority with inertia at a tie. We determine the image of every one of its $4^n$ Boolean states after one step. The recurrent core consists of $2+2^n$ fixed states and $$\frac{1}{2}\left\{\binom{2n}{n}-2^n\right\}$$ genuine two-cycles; every other state reaches consensus in one step. This gives exact consensus-basin sizes, every iterate fixed-point count, the Artin--Mazur zeta function, and the complete symbolic natural extension. For i.i.d. Bernoulli initial data we also obtain exact outcome probabilities. In the critical window $p=1/2+a/\sqrt n$, the probability of one-consensus tends to $\Phi(2\sqrt2a)$, while the genuine two-cycle probability is asymptotic to $e^{-4a^2}/\sqrt{\pi n}$. An exhaustive implementation of the literal local rule checks all states through $n=8$ and the first twelve iterate counts.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 27 August 2026'
title: 'Exact State Partition, Zeta Function, and Critical Window for Majority Dynamics on Cocktail-Party Graphs'
```

## Markdown 正文

# Introduction

Synchronous Boolean threshold networks with symmetric interaction have no cycles longer than two, a foundational fact due to Goles and Olivos [@GolesOlivos1980]. For majority dynamics with the convention that a vertex retains its state at a tie, Ginosar and Holzman study the same local rule on infinite graphs [@GinosarHolzman2000]. Quantitative work on finite majority processes has emphasized convergence time and graph modules [@KaaserEtAl2016]. Those general results tell us the maximum possible period, but do not by themselves enumerate the recurrent states or their basins on a specified graph family.

This note performs that enumeration for the cocktail-party graph. Its vertices come in $n$ nonadjacent mate pairs, while every two vertices from different pairs are adjacent. A global imbalance forces consensus in one step. At exact balance, each mate pair evolves independently: a monochrome pair flips and a mixed pair freezes. This elementary dichotomy yields a complete state partition and, from it, several dynamical quantities that are usually studied separately.

Our scope is intentionally exact and family-specific. We use the general period-two theorem as prior art, and do not treat irreversible conversion processes, whose multipartite theory has a different update rule [@AdamsEtAl2011]. The residual contribution is the joint package of state counts, basin counts, zeta function, natural extension, and Bernoulli critical-window asymptotics for the symmetric synchronous rule on $\operatorname{CP}_n$.

# The local rule

Fix $n\geq1$. Write the vertices of $\operatorname{CP}_n$ as $$V_n=\{1,\bar1,\ldots,n,\bar n\},$$ where $i$ and $\bar i$ are mates and hence are the only distinct nonadjacent pair involving either vertex. A state is $x=(x_v)_{v\in V_n}\in\{0,1\}^{V_n}$. Let $$S(x)=\sum_{v\in V_n}x_v.$$ Every vertex has degree $2n-2$. The synchronous majority map $F_n:\{0,1\}^{V_n}\to\{0,1\}^{V_n}$ is $$(F_nx)_v=
 \begin{cases}
 1,&\sum_{w\sim v}x_w>n-1,\\
 0,&\sum_{w\sim v}x_w<n-1,\\
 x_v,&\sum_{w\sim v}x_w=n-1.
 \end{cases}$$ Thus a tie is inertial. This convention also makes $F_1$ the identity on the four states of the edgeless graph $\operatorname{CP}_1$.

[\[lem:trichotomy\]]{#lem:trichotomy label="lem:trichotomy"} For every $x\in\{0,1\}^{V_n}$:

1.  if $S(x)<n$, then $F_nx=0^{V_n}$;

2.  if $S(x)>n$, then $F_nx=1^{V_n}$;

3.  if $S(x)=n$, then on each mate pair $\{i,\bar i\}$ the map fixes the patterns $01$ and $10$ and interchanges $00$ with $11$.

The number of one-neighbors seen by $v$ is $$N_v(x)=S(x)-x_v-x_{\bar v}.$$ If $S(x)<n$, then $N_v(x)\leq n-1$. Equality can occur only when $S(x)=n-1$ and the mate pair of $v$ is $00$, so inertia still leaves $v$ equal to zero. Otherwise $N_v(x)<n-1$ and $v$ becomes zero. This proves the first assertion; complementation proves the second.

Suppose $S(x)=n$. A $00$ pair has $N_v(x)=n$ at both vertices and becomes $11$. A $11$ pair has $N_v(x)=n-2$ and becomes $00$. A mixed pair has $N_v(x)=n-1$ at both vertices, so both coordinates retain their values.

# Complete finite dynamics

Call a state *pairwise mixed* if each mate pair is either $01$ or $10$. There are exactly $2^n$ such states, all of weight $n$.

[\[thm:partition\]]{#thm:partition label="thm:partition"} For $n\geq1$, the recurrent core of $F_n$ has: $$\begin{aligned}
 \#\{\text{fixed states}\}&=2+2^n,\\
 \#\{\text{genuine two-cycles}\}
 &=\frac{1}{2}\left\{\binom{2n}{n}-2^n\right\}.\end{aligned}$$ The fixed states are the two consensus states and the $2^n$ pairwise-mixed states. Each full consensus basin has cardinality $$B_n=\frac{4^n-\binom{2n}{n}}{2}.$$ Every nonrecurrent state enters the recurrent core after exactly one step, and $F_n^3=F_n$.

By [\[lem:trichotomy\]](#lem:trichotomy){reference-type="ref" reference="lem:trichotomy"}, all states of weight below $n$ enter zero-consensus and all states of weight above $n$ enter one-consensus. Complementation is a bijection between these two sets, while the middle layer has size $\binom{2n}{n}$. Hence each consensus basin, including its consensus state, has size $$\sum_{j=0}^{n-1}\binom{2n}{j}
 =\frac{4^n-\binom{2n}{n}}2.$$

On the middle layer, pairwise-mixed states are fixed. Every other state has at least one monochrome mate pair; all monochrome pairs flip and all mixed pairs freeze. A second step therefore returns the original state, but the first step does not. Thus the remaining $\binom{2n}{n}-2^n$ middle-layer states form genuine two-cycles. The same description shows that every image is recurrent and proves $F_n^3=F_n$.

The formula is more informative than the general statement that symmetric threshold networks have period at most two: it records the complete functional graph up to the individual leaves attached to the two consensus states.

# Iterate counts, zeta function, and natural extension

For a map on a finite set, define its Artin--Mazur zeta function by $$\zeta_{F_n}(z)
 =\exp\left(\sum_{k\geq1}\frac{|\operatorname{Fix}(F_n^k)|}{k}z^k\right).$$

[\[cor:zeta\]]{#cor:zeta label="cor:zeta"} For every $k\geq1$, $$|\operatorname{Fix}(F_n^k)|=
 \begin{cases}
 2+2^n,&k\text{ odd},\\
 2+\binom{2n}{n},&k\text{ even}.
 \end{cases}$$ Consequently $$\zeta_{F_n}(z)
 =(1-z)^{-(2+2^n)}
  (1-z^2)^{-\frac12\{\binom{2n}{n}-2^n\}}.$$

An odd iterate fixes exactly the fixed states. An even iterate additionally fixes every point on a two-cycle. The Euler product of a finite dynamical system contributes $(1-z^\ell)^{-1}$ for each cycle of length $\ell$, giving the displayed formula.

There is also a canonical invertible symbolic system associated with the noninvertible map. Its natural extension is $$\widehat X_n
 =\{(x_t)_{t\in\mathbb Z}:F_n(x_t)=x_{t+1}\text{ for every }t\},
 \qquad \widehat\sigma((x_t)_t)=(x_{t+1})_t.$$

[\[cor:natural\]]{#cor:natural label="cor:natural"} The projection $(x_t)_t\mapsto x_0$ conjugates $(\widehat X_n,\widehat\sigma)$ to the restriction of $F_n$ to its recurrent core. Hence $\widehat X_n$ is the disjoint union of $2+2^n$ fixed orbits and $\frac12\{\binom{2n}{n}-2^n\}$ orbits of length two, and its zeta function is the one in [\[cor:zeta\]](#cor:zeta){reference-type="ref" reference="cor:zeta"}.

In a finite functional graph, a point has prehistories of every length that fit into a bi-infinite orbit if and only if it lies on a directed cycle. Theorem [\[thm:partition\]](#thm:partition){reference-type="ref" reference="thm:partition"} identifies all such points. On this recurrent core $F_n$ is bijective, so the zeroth coordinate uniquely determines the entire bi-infinite orbit.

# Bernoulli initial data and the critical window

Let the $2n$ initial coordinates be independent Bernoulli variables of parameter $p\in[0,1]$. Write $H_n\sim\operatorname{Bin}(2n,p)$.

[\[thm:bernoulli\]]{#thm:bernoulli label="thm:bernoulli"} Under Bernoulli$(p)$ initial data, $$\begin{aligned}
 \mathbb P(\text{one-consensus})&=\mathbb P(H_n>n),\\
 \mathbb P(\text{zero-consensus})&=\mathbb P(H_n<n),\\
 \mathbb P(\text{nonconsensus fixed state})&=[2p(1-p)]^n,\\
 \mathbb P(\text{genuine two-cycle})
 &=\left\{\binom{2n}{n}-2^n\right\}[p(1-p)]^n.\end{aligned}$$ These four events partition the probability space.

The first two identities are [\[lem:trichotomy\]](#lem:trichotomy){reference-type="ref" reference="lem:trichotomy"}. Every pairwise-mixed state contains exactly $n$ ones and has probability $p^n(1-p)^n$; there are $2^n$ such states. Every other balanced state lies on a genuine two-cycle, and there are $\binom{2n}{n}-2^n$ of them.

At $p=1/2$, the genuine two-cycle probability is $$\frac{\binom{2n}{n}-2^n}{4^n}
 =\frac{1}{\sqrt{\pi n}}(1+O(n^{-1}))-2^{-n}.$$ The next result resolves the whole $n^{-1/2}$ bias window.

[\[cor:window\]]{#cor:window label="cor:window"} Fix $a\in\mathbb R$ and put $p_n=1/2+a/\sqrt n$, for all sufficiently large $n$. Then $$\begin{aligned}
 \mathbb P_{p_n}(\text{one-consensus})&\longrightarrow\Phi(2\sqrt2a),\\
 \mathbb P_{p_n}(\text{zero-consensus})&\longrightarrow\Phi(-2\sqrt2a),\\
 \mathbb P_{p_n}(\text{genuine two-cycle})
 &\sim\frac{e^{-4a^2}}{\sqrt{\pi n}}.\end{aligned}$$ The nonconsensus fixed-state probability is exponentially small.

For $H_n\sim\operatorname{Bin}(2n,p_n)$, $$\frac{n-2np_n}{\sqrt{2np_n(1-p_n)}}\longrightarrow-2\sqrt2a.$$ The central limit theorem gives the first two limits; the atom at $n$ is $O(n^{-1/2})$ and does not affect them. Stirling's formula and $$[p_n(1-p_n)]^n
 =4^{-n}(1-4a^2/n)^n
 \sim4^{-n}e^{-4a^2}$$ give the two-cycle asymptotic. Finally, $[2p_n(1-p_n)]^n=2^{-n}(1-4a^2/n)^n$.

# Deterministic control and claim boundary

The companion script constructs the deleted-matching neighbor list and evaluates the literal local majority rule; it does not use the trichotomy as an update shortcut. It exhausts all $4^n$ states for $1\leq n\leq8$, checks $F_n^3=F_n$, the state and basin formulas, and $|\operatorname{Fix}(F_n^k)|$ for $1\leq k\leq12$. This is a finite regression control, not a substitute for the proofs.

General period-two behavior is explicitly attributed to @GolesOlivos1980, and the tie convention to the established majority literature [@GinosarHolzman2000]. A bounded search through 27 August 2026 found no exact collision with the combined cocktail-party formulas in [\[thm:partition,cor:zeta,cor:natural,thm:bernoulli,cor:window\]](#thm:partition,cor:zeta,cor:natural,thm:bernoulli,cor:window){reference-type="ref" reference="thm:partition,cor:zeta,cor:natural,thm:bernoulli,cor:window"}; this is a search record, not a worldwide priority claim. Public release and venue selection remain outside the scope of this internal draft.
