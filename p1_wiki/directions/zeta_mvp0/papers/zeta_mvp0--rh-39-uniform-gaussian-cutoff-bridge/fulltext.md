---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-39-uniform-gaussian-cutoff-bridge"
canonical_tex: "zeta_mvp0/papers/RH-39-uniform-gaussian-cutoff-bridge/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-39-uniform-gaussian-cutoff-bridge/uniform-gaussian-cutoff-bridge.pdf"
source_sha256: "6f36c4ddd2201ca538e82da1ea394211d67358712d2f9d88d5170f7e2207df7d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Uniform Folded-Gaussian Cutoff Bounds for Dyadic Haar Continuation Fixed-Window Obstruction and an Adaptive Second-Order Bridge

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-39-uniform-gaussian-cutoff-bridge>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-39-uniform-gaussian-cutoff-bridge/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-39-uniform-gaussian-cutoff-bridge/uniform-gaussian-cutoff-bridge.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-39-uniform-gaussian-cutoff-bridge/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-39-uniform-gaussian-cutoff-bridge/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The stored transfer matrices in a nested-grid spectral-count program retain only a hard eight-standard-deviation window of a folded Gaussian row and then renormalize. A preceding paper proved the smooth full-kernel Haar law $E,D=O(h^2)$ and $C,B=O(h)$, but left this discontinuous cutoff as an explicit gap. We close the cutoff gate at the exact-real Markov-kernel level.

  For mesh $h=1/n$, width $\sigma$, and declared support multiple $L$, the archived builder uses $$H_h=\left\lceil\frac{L\sigma}{h}\right\rceil+2.$$ Every omitted positive midpoint is at distance at least $H_hh$ from the folded center. Put $\Lambda_h=H_hh/\sigma$. Combining this geometry, the exact twice-the-tail row identity, Gaussian lattice estimates, and Mills' ratio gives an explicit omitted-mass upper $$Q_h=
  \frac{2e^{1/2}e^{-\Lambda_h^2/2}}
       {\sigma-h}
  \left(h+\frac{\sigma}{\Lambda_h}\right).$$ We also prove a dimension-uniform Frobenius, hence Euclidean operator-norm, bound $\left\lVert P_h^{(L)}-P_h\right\rVert_2\le\varepsilon_h$ with a closed formula.

  A fixed $L$ has a positive continuum row defect and therefore does not converge to the full kernel in row-operator norm. In contrast, $$L(h)=\max\left\{5,2\sqrt{\log(1/h)}\right\}$$ gives $$\varepsilon_h=O\!\left(
  h^2(\log(1/h))^{-1/4}
  \right),$$ so the cutoff contribution preserves all four Haar rates. Thus the hard support can be bridged without differentiating its moving indicator.

  At $\sigma=10^{-2}$ and dimensions $2048,4096,8192$, 256-bit Arb evaluation gives $\varepsilon_h\le1.251,1.527,1.670\times10^{-13}$. The corresponding Haar perturbation is at most $3.20\times10^{-13}$ and is below $3.58\times10^{-9}$ of every measured stored Markov block. Nevertheless, the fixed-eight-sigma continuum omitted mass at a zero-mean row is the strictly positive value $1.244192114854\times10^{-15}$. The result closes the analytic cutoff gate, not the separate projector-convergence, binary64-transcendental, or multilevel nonnormal-resolvent gates.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Uniform Folded-Gaussian Cutoff Bounds for Dyadic Haar Continuation\
  Fixed-Window Obstruction and an Adaptive Second-Order Bridge
```

## Markdown 正文

# Introduction

The nested-grid count certificates in @WangNested2026 [@WangIterated2026] concern exact stored binary64 matrices at dimensions $2048,4096,8192$. Their dyadic block decompositions were subsequently explained by a smooth-kernel theorem [@WangHaar2026]: $$\left\lVert E_h\right\rVert_2,\left\lVert D_h\right\rVert_2=O(h^2),\qquad
\left\lVert C_h\right\rVert_2,\left\lVert B_h\right\rVert_2=O(h).$$ One Haar difference extracts one derivative and two differences extract a mixed second derivative. Discrete row normalization, smooth finite-rank subtraction, and operator squaring preserve those powers.

The stored Gaussian matrix, however, is not the full smooth midpoint matrix. Each folded row keeps a finite window around $|f_u(x)|$, discards the remainder, and is normalized on the retained indices. The support window moves by integer jumps as the source point and dimension change. Applying a $C^2$ theorem directly to that indicator-truncated kernel is therefore invalid.

The exact rowwise identity behind this issue was already proved in @WangResponse2026: if a stochastic row omits full-row mass $q$ and is renormalized on its retained support, its $\ell^1$ error is exactly $2q$. That result is the correct starting point, but it does not yet provide the Euclidean norm needed by the Haar and Schur calculations, nor does it resolve whether a fixed cutoff is compatible with an all-grid theorem.

This paper supplies the missing bridge. The main contributions are:

1.  an exact support-buffer lemma for the actual archived $\lceil L\sigma n\rceil+2$ indexing rule;

2.  a uniform omitted-mass bound and a closed Frobenius/spectral-norm bound for the full-versus-cutoff folded Markov matrices;

3.  a proof that fixed $L$ has a positive full-kernel row defect;

4.  the sufficient adaptive law $L(h)=2\sqrt{\log(1/h)}$, which restores an $O(h^2)$ Euclidean bridge;

5.  exact propagation of this defect through the four dyadic Haar blocks; and

6.  256-bit Arb enclosures and a floating three-grid mechanism audit for the stored parameter values.

The conclusion is both positive and restrictive. The eight-sigma cutoff is far smaller than every currently measured Markov Haar block, and it exceeds the sufficient adaptive schedule through dimension $\lfloor e^{16}\rfloor=8{,}886{,}110$. It is therefore harmless at the archived levels. It is not, however, a mathematically vanishing perturbation when $L=8$ is held forever. An infinite-grid theorem must either increase $L$, compare against the fixed truncated continuum operator instead of the full operator, or prove a separate cancellation unavailable from norm bounds alone.

Three evidence levels are kept separate throughout:

Analytic theorem

:   Exact real-arithmetic inequalities for the archived support rule.

Validated constants

:   256-bit Arb interval evaluations of the closed upper bounds.

Floating diagnostic

:   Dense-row calculations used to show sharp scale, never as interval proof.

# The archived folded Gaussian rule {#sec:model}

Let $n\ge2$, $h=1/n$, and let $$x_i=y_i=\left(i+\frac12\right)h,
\qquad 0\le i<n.$$ The quadratic map is $f_u(x)=1-ux^2$. At the band-merging parameter used in the stored matrices, $1<u<2$, so $$m_i=f_u(x_i)\in[1-u,1],
\qquad a_i=|m_i|\in[0,1].$$

For fixed $\sigma\in(0,1]$, define $$G_\sigma(t)=e^{-t^2/(2\sigma^2)},
\qquad
r_a(y)=G_\sigma(y-a)+G_\sigma(y+a).$$ Because $G_\sigma$ is even, $$G_\sigma(y-m)+G_\sigma(-y-m)=r_{|m|}(y).$$ The full folded midpoint Markov matrix is $$(P_h)_{ij}
=\frac{r_{a_i}(y_j)}{Z_h(a_i)},
\qquad
Z_h(a)=\sum_{k=0}^{n-1}r_a(y_k).
\label{eq:full-matrix}$$

Fix a declared multiple $L>0$. The archived sparse builder uses $$H_h=\left\lceil\frac{L\sigma}{h}\right\rceil+2,
\qquad
c_i=\left\lfloor\frac{a_i}{h}-\frac12\right\rfloor,
\label{eq:archived-support}$$ and retains $$S_i=\{j\in\{0,\ldots,n-1\}:|j-c_i|\le H_h\}.$$ The exact-real cutoff row is $$(P_h^{(L)})_{ij}=
\begin{cases}
(P_h)_{ij}/(1-q_i),&j\in S_i,\\
0,&j\notin S_i,
\end{cases}
\qquad
q_i=\sum_{j\notin S_i}(P_h)_{ij}.
\label{eq:cutoff-matrix}$$

This is the mathematical matrix defined by the archived support rule. The actual stored arrays evaluate exponentials, logarithmic sums, and row normalizers in binary64. Their transcendental roundoff is a distinct issue and is not hidden inside the exact-real cutoff bound.

[\[lem:support-buffer\]]{#lem:support-buffer label="lem:support-buffer"} If $j\notin S_i$, then $$|y_j-a_i|\ge H_hh.
\label{eq:support-buffer}$$ Consequently every omitted midpoint is at least $L\sigma+2h$ from the folded center.

Write $a=a_i$ and $c=c_i$. The floor in [\[eq:archived-support\]](#eq:archived-support){reference-type="eqref" reference="eq:archived-support"} gives $$(c+\tfrac12)h\le a<(c+\tfrac32)h.$$ If $j\ge c+H_h+1$, then $$y_j-a>(c+H_h+\tfrac32)h-(c+\tfrac32)h=H_hh.$$ If $j\le c-H_h-1$, then $$a-y_j\ge(c+\tfrac12)h-(c-H_h-\tfrac12)h
=(H_h+1)h.$$ The clipping to $0\le j<n$ only removes impossible indices. Finally, $H_hh\ge L\sigma+2h$.

# Row tails and a Gaussian lattice bound {#sec:tails}

We first recall the elementary identity that makes row renormalization exact.

[\[prop:twice-tail\]]{#prop:twice-tail label="prop:twice-tail"} For every row in [\[eq:full-matrix\]](#eq:full-matrix){reference-type="eqref" reference="eq:full-matrix"}--[\[eq:cutoff-matrix\]](#eq:cutoff-matrix){reference-type="eqref" reference="eq:cutoff-matrix"}, $$\sum_{j=0}^{n-1}|(P_h^{(L)})_{ij}-(P_h)_{ij}|=2q_i.
\label{eq:twice-tail}$$ Hence $$\left\lVert P_h^{(L)}-P_h\right\rVert_\infty=2\max_iq_i.$$

The omitted entries contribute $q_i$. On the retained set, the increase is $(P_h)_{ij}q_i/(1-q_i)$, whose sum is also $q_i$. This is the identity of @WangResponse2026 specialized to the folded support.

The next lemma controls shifted midpoint lattices without assuming that the Gaussian center is itself a grid point.

[\[lem:lattice-tail\]]{#lem:lattice-tail label="lem:lattice-tail"} Let $F:[0,\infty)\to[0,\infty)$ be nonincreasing. For any shifted lattice of spacing $h$, any center $a$, and $R>0$, $$\sum_{z:\,|z-a|\ge R}F(|z-a|)
\le2\left\{F(R)+\frac1h\int_R^\infty F(t)\,dt\right\}.
\label{eq:lattice-tail}$$ The sum may be restricted to any finite subset of the lattice.

On either side of $a$, the admissible distances form a sequence with gaps at least $h$. Its sum is bounded by the first rectangle $F(R)$ plus the upper Riemann sum $h^{-1}\int_R^\infty F$. Add the two sides.

We also need a denominator lower bound that remains valid at the endpoints.

[\[lem:normalizer\]]{#lem:normalizer label="lem:normalizer"} Assume $0<h<\sigma\le1$. Uniformly for $a\in[0,1]$, $$Z_h(a)\ge e^{-1/2}\left(\frac\sigma h-1\right).
\label{eq:normalizer-lower}$$

The interval $[a-\sigma,a+\sigma]\cap[0,1]$ has length at least $\sigma$ and contains at least $\sigma/h-1$ positive midpoints. At each such midpoint, $G_\sigma(y-a)\ge e^{-1/2}$. The second folded Gaussian is nonnegative.

Put $$\Lambda_h=\frac{H_hh}{\sigma}.
\label{eq:effective-multiple}$$ The extra two support cells make $\Lambda_h>L$ at every finite grid.

[\[thm:row-tail\]]{#thm:row-tail label="thm:row-tail"} Assume $0<h<\sigma\le1$. Define $$Q_h=
\frac{2e^{1/2}e^{-\Lambda_h^2/2}}
     {\sigma-h}
\left(h+\frac{\sigma}{\Lambda_h}\right).
\label{eq:Q-bound}$$ Then $$q_i\le Q_h
\quad\text{for every row},
\qquad
\left\lVert P_h^{(L)}-P_h\right\rVert_\infty\le2Q_h.
\label{eq:row-tail-result}$$

The positive and negative folded terms combine into the symmetric midpoint lattice $\{\pm y_j\}$. By [\[lem:support-buffer\]](#lem:support-buffer){reference-type="ref" reference="lem:support-buffer"}, every omitted lattice point has distance at least $R=\Lambda_h\sigma$ from $a_i$: for the negative counterpart, $|-y_j-a_i|=y_j+a_i\ge|y_j-a_i|$. Apply [\[lem:lattice-tail\]](#lem:lattice-tail){reference-type="ref" reference="lem:lattice-tail"} with $F(t)=e^{-t^2/(2\sigma^2)}$ and use Mills' inequality [@Gordon1941] $$\int_R^\infty e^{-t^2/(2\sigma^2)}\,dt
\le\frac{\sigma^2}{R}e^{-R^2/(2\sigma^2)}
=\frac\sigma{\Lambda_h}e^{-\Lambda_h^2/2}.$$ Divide the resulting omitted raw sum by [\[eq:normalizer-lower\]](#eq:normalizer-lower){reference-type="eqref" reference="eq:normalizer-lower"}. Equation [\[eq:twice-tail\]](#eq:twice-tail){reference-type="eqref" reference="eq:twice-tail"} completes the proof.

# A uniform Euclidean cutoff bridge {#sec:euclidean}

The row norm is natural for Markov observables, but the dyadic block and Schur arguments use Euclidean spectral norm. A Frobenius estimate supplies a dimension-uniform conversion.

Assume $Q_h<1$ and put $$A_h=\frac{Q_h}{1-Q_h}.
\label{eq:A-bound}$$ Define $$\begin{aligned}
\Omega_h
&=
\frac{4e\,e^{-\Lambda_h^2}}
     {(\sigma-h)^2}
\left(h+\frac{\sigma}{2\Lambda_h}\right),
\label{eq:Omega-bound}\\
\mathcal R_h
&=
\frac{eA_h^2}{(\sigma-h)^2}
\left(4h+2\sqrt\pi\,\sigma\right),
\label{eq:R-bound}\\
\varepsilon_h
&=\sqrt{\Omega_h+\mathcal R_h}.
\label{eq:epsilon-bound}\end{aligned}$$

[\[thm:euclidean\]]{#thm:euclidean label="thm:euclidean"} Under the preceding assumptions, $$\left\lVert P_h^{(L)}-P_h\right\rVert_2
\le\left\lVert P_h^{(L)}-P_h\right\rVert_{\mathrm F}
\le\varepsilon_h.
\label{eq:euclidean-result}$$ The term $\Omega_h$ bounds the omitted entries and $\mathcal R_h$ bounds the renormalization increase on retained entries.

Let $p_{ij}=(P_h)_{ij}$. On omitted entries the absolute difference is $p_{ij}$; on retained entries it is $p_{ij}q_i/(1-q_i)\le A_hp_{ij}$.

For the omitted part, use $$r_a(y)^2
\le2\{e^{-(y-a)^2/\sigma^2}+e^{-(y+a)^2/\sigma^2}\}.$$ After folding to the symmetric lattice, [\[lem:lattice-tail\]](#lem:lattice-tail){reference-type="ref" reference="lem:lattice-tail"} with $F(t)=e^{-t^2/\sigma^2}$ and $$\int_R^\infty e^{-t^2/\sigma^2}\,dt
\le\frac{\sigma^2}{2R}e^{-R^2/\sigma^2}$$ gives a per-row raw square sum bounded by $$4e^{-\Lambda_h^2}
\left(1+\frac{\sigma}{2h\Lambda_h}\right).$$ Divide by [\[eq:normalizer-lower\]](#eq:normalizer-lower){reference-type="eqref" reference="eq:normalizer-lower"} squared and sum over $n=1/h$ rows. The result is [\[eq:Omega-bound\]](#eq:Omega-bound){reference-type="eqref" reference="eq:Omega-bound"}.

For the retained part, apply the same square inequality to the full symmetric lattice. On either side of the center, $$\sum e^{-t^2/\sigma^2}
\le1+\frac1h\int_0^\infty e^{-t^2/\sigma^2}\,dt
=1+\frac{\sqrt\pi\sigma}{2h}.$$ Thus the full per-row raw square sum is at most $4+2\sqrt\pi\sigma/h$. Divide by the normalizer lower bound squared, sum over all rows, and multiply by $A_h^2$. This gives [\[eq:R-bound\]](#eq:R-bound){reference-type="eqref" reference="eq:R-bound"}. The Frobenius and spectral inequalities follow.

The exponential $e^{-\Lambda_h^2}$ in the square tail is why the Euclidean bound is much smaller than a crude $\sqrt n$ conversion of the row norm. No derivative of the moving support indicator is used.

# Fixed windows and adaptive windows {#sec:schedules}

The distinction between a numerically tiny error and a vanishing asymptotic error is essential.

[\[prop:fixed-obstruction\]]{#prop:fixed-obstruction label="prop:fixed-obstruction"} Suppose $L\sigma<1$ and there are source midpoints converging to a zero of $f_u$. Then $$\liminf_{h\to0}
\left\lVert P_h^{(L)}-P_h\right\rVert_\infty
\ge2q_0^{(L,\sigma)}>0,
\label{eq:fixed-obstruction}$$ where $$q_0^{(L,\sigma)}
=
\frac{\displaystyle\int_{L\sigma}^{1}
e^{-y^2/(2\sigma^2)}\,dy}
{\displaystyle\int_{0}^{1}
e^{-y^2/(2\sigma^2)}\,dy}.
\label{eq:continuum-tail}$$

At a zero-mean row the folded raw kernel is $2e^{-y^2/(2\sigma^2)}$. Composite midpoint sums for the full and retained normalizers converge to the denominator and its restriction to $[0,L\sigma]$. The extra two support cells vanish physically as $h\to0$. Rows with $f_u(x_i)\to0$ therefore have $q_i\to q_0^{(L,\sigma)}$. Apply [\[prop:twice-tail\]](#prop:twice-tail){reference-type="ref" reference="prop:twice-tail"}.

For $L=8$ and $\sigma=10^{-2}$, 256-bit interval arithmetic gives $$q_0^{(8,10^{-2})}
=1.2441921148543568\ldots\times10^{-15}.
\label{eq:eight-tail-value}$$ This is negligible at current scales but mathematically nonzero.

[\[thm:adaptive\]]{#thm:adaptive label="thm:adaptive"} Fix $\sigma>0$ and define $$L(h)=\max\left\{L_0,2\sqrt{\log(1/h)}\right\},
\qquad L_0>0.
\label{eq:adaptive-schedule}$$ Use the archived support rule with $L=L(h)$. Then, until the support has already saturated to the full interval, $$Q_h=O\!\left(
\frac{h^2}{\sqrt{\log(1/h)}}
\right),
\label{eq:adaptive-row}$$ and $$\varepsilon_h
=O\!\left(
\frac{h^2}{(\log(1/h))^{1/4}}
\right).
\label{eq:adaptive-two}$$ In particular, $\left\lVert P_h^{(L(h))}-P_h\right\rVert_2=O(h^2)$.

Since $\Lambda_h\ge L(h)$, $$e^{-\Lambda_h^2/2}\le e^{-L(h)^2/2}\le h^2.$$ Substitution in [\[eq:Q-bound\]](#eq:Q-bound){reference-type="eqref" reference="eq:Q-bound"} gives [\[eq:adaptive-row\]](#eq:adaptive-row){reference-type="eqref" reference="eq:adaptive-row"}. Similarly, $e^{-\Lambda_h^2}\le h^4$, so $$\Omega_h=O\!\left(
\frac{h^4}{\sqrt{\log(1/h)}}
\right),
\qquad
\mathcal R_h=O\!\left(
\frac{h^4}{\log(1/h)}
\right).$$ Taking the square root proves [\[eq:adaptive-two\]](#eq:adaptive-two){reference-type="eqref" reference="eq:adaptive-two"}. Once the retained window covers every destination, the defect is exactly zero.

The archived $L=8$ exceeds the adaptive prescription exactly while $$2\sqrt{\log n}\le8,
\qquad n\le e^{16}=8{,}886{,}110.52\ldots.$$ The current largest dimension $8192$ is more than three orders of magnitude below this crossover.

# Propagation through dyadic Haar blocks {#sec:haar}

Let $J,W$ be replication and alternating-detail injections, and let $R=J^*/2$, $S=W^*/2$. As in @WangHaar2026, $$\left\lVert R\right\rVert_2\left\lVert J\right\rVert_2
=\left\lVert R\right\rVert_2\left\lVert W\right\rVert_2
=\left\lVert S\right\rVert_2\left\lVert J\right\rVert_2
=\left\lVert S\right\rVert_2\left\lVert W\right\rVert_2=1.$$ Let $E_h,C_h,B_h,D_h$ be the full-kernel Haar blocks and let $E_h^{(L)},C_h^{(L)},B_h^{(L)},D_h^{(L)}$ be the cutoff blocks. Put $F_h=P_h^{(L)}-P_h$.

[\[thm:haar-bridge\]]{#thm:haar-bridge label="thm:haar-bridge"} If $\left\lVert F_h\right\rVert_2\le\varepsilon_h$ and $\left\lVert F_{h/2}\right\rVert_2\le\varepsilon_{h/2}$, then $$\begin{aligned}
\left\lVert E_h^{(L)}-E_h\right\rVert_2
&\le\varepsilon_h+\varepsilon_{h/2},
\label{eq:haar-E}\\
\left\lVert C_h^{(L)}-C_h\right\rVert_2,
\left\lVert B_h^{(L)}-B_h\right\rVert_2,
\left\lVert D_h^{(L)}-D_h\right\rVert_2
&\le\varepsilon_{h/2}.
\label{eq:haar-CBD}\end{aligned}$$ Under the adaptive schedule [\[eq:adaptive-schedule\]](#eq:adaptive-schedule){reference-type="eqref" reference="eq:adaptive-schedule"}, every cutoff contribution is $O(h^2)$. It therefore preserves the smooth full-kernel law $$E,D=O(h^2),\qquad C,B=O(h).$$

The consistency difference is $$RF_{h/2}J-F_h,$$ while each remaining difference is one coordinate compression of $F_{h/2}$. Apply the unit coordinate-product bounds and [\[thm:adaptive\]](#thm:adaptive){reference-type="ref" reference="thm:adaptive"}.

This theorem is the main bridge to RH-38. It avoids assigning derivatives to the hard cutoff itself: the cutoff matrix is compared in norm with the smooth full matrix before Haar cancellation is invoked.

# Validated finite-grid constants {#sec:constants}

We now evaluate the closed formulas at the exact stored parameters $$\sigma=10^{-2},\qquad L=8,
\qquad n\in\{2048,4096,8192\}.$$ All entries in [1](#tab:arb){reference-type="ref" reference="tab:arb"} are upper endpoints of 256-bit Arb balls [@Johansson2017; @Rump2010]. They enclose the analytic expressions in [\[eq:Q-bound,eq:epsilon-bound\]](#eq:Q-bound,eq:epsilon-bound){reference-type="ref" reference="eq:Q-bound,eq:epsilon-bound"}; they are not claims about unvalidated binary64 transcendental evaluation.

::: {#tab:arb}
     $n$   $H_h$   $\Lambda_h$                   $Q_h$         $\varepsilon_h$
  ------ ------- ------------- ----------------------- -----------------------
    2048     166      8.105469   $3.234\times10^{-15}$   $1.251\times10^{-13}$
    4096     330      8.056641   $4.035\times10^{-15}$   $1.527\times10^{-13}$
    8192     658      8.032227   $4.464\times10^{-15}$   $1.670\times10^{-13}$

  : Arb-enclosed fixed-eight-sigma analytic bounds.
:::

The corresponding Haar perturbation uppers are

::: {#tab:haar-cutoff}
  refinement                          $E$                     $C$                     $B$                     $D$
  --------------- ----------------------- ----------------------- ----------------------- -----------------------
  $2048\to4096$     $2.778\times10^{-13}$   $1.527\times10^{-13}$   $1.527\times10^{-13}$   $1.527\times10^{-13}$
  $4096\to8192$     $3.197\times10^{-13}$   $1.670\times10^{-13}$   $1.670\times10^{-13}$   $1.670\times10^{-13}$

  : Analytic cutoff contributions to the Markov Haar blocks.
:::

Dividing these uppers by the floating leading singular values of the stored Markov blocks from RH-38 gives the diagnostic ratios in [3](#tab:relative){reference-type="ref" reference="tab:relative"}.

::: {#tab:relative}
  refinement                         $E$                    $C$                    $B$                    $D$
  --------------- ---------------------- ---------------------- ---------------------- ----------------------
  $2048\to4096$     $7.77\times10^{-10}$   $9.28\times10^{-12}$   $9.56\times10^{-12}$   $6.27\times10^{-10}$
  $4096\to8192$      $3.58\times10^{-9}$   $2.03\times10^{-11}$   $2.09\times10^{-11}$    $2.74\times10^{-9}$

  : Analytic cutoff upper divided by a floating stored Markov block norm. The denominator is diagnostic, so these are not interval ratios.
:::

Thus, at the two certified refinements, the analytic cutoff bridge is at least eight orders of magnitude below the measured Markov block scale.

## Floating full-versus-cutoff pilot

A chunked dense-row calculation independently formed the full folded rows, applied the archived support mask, and evaluated the absolute difference from the exactly renormalized cutoff formula. The results are in [4](#tab:floating){reference-type="ref" reference="tab:floating"}.

::: {#tab:floating}
     $n$              $\max q_i$   $\left\lVert F_h\right\rVert_{\mathrm F}$             Schur upper   analytic/Frobenius
  ------ ----------------------- ------------------------------------------- ----------------------- --------------------
    2048   $5.276\times10^{-16}$                       $6.368\times10^{-15}$   $2.293\times10^{-15}$                19.64
    4096   $7.225\times10^{-16}$                       $1.035\times10^{-14}$   $3.572\times10^{-15}$                14.75
    8192   $9.570\times10^{-16}$                       $1.329\times10^{-14}$   $4.782\times10^{-15}$                12.57

  : Floating mechanism diagnostic. No entry is promoted to a rigorous enclosure.
:::

The maximum numerical defect in the twice-the-tail identity was below $8\times10^{-31}$. This only checks internal arithmetic consistency. The Arb bounds are deliberately one order of magnitude looser than the floating Frobenius values.

![Fixed and adaptive cutoff behavior. (a) The floating omitted mass approaches a positive fixed-window floor, while the analytic row upper remains conservative. (b) The full-versus-cutoff Euclidean bridge is below $2\times10^{-13}$ at every stored dimension. (c) The archived eight-sigma window exceeds the sufficient adaptive schedule through dimension $e^{16}$. (d) Normalization by $h^2$ exposes the fixed-window obstruction and the bounded adaptive second-order bridge.](<../../../../../zeta_mvp0/papers/RH-39-uniform-gaussian-cutoff-bridge/figures/uniform_gaussian_cutoff_bridge.pdf>){#fig:summary width="\\textwidth"}

# What is closed and what remains {#sec:boundary}

The cutoff question now has a precise answer.

1.  **At the current grids: closed analytically.** The exact-real full-versus-cutoff Markov perturbation is bounded by $1.67\times10^{-13}$, and its Haar contribution is negligible relative to the measured block scale.

2.  **At all grids with fixed $L=8$: not a vanishing bridge.** The row defect tends to the positive value in [\[eq:eight-tail-value\]](#eq:eight-tail-value){reference-type="eqref" reference="eq:eight-tail-value"} along zero-mean rows.

3.  **At all grids with adaptive $L(h)$: closed.** The schedule in [\[eq:adaptive-schedule\]](#eq:adaptive-schedule){reference-type="eqref" reference="eq:adaptive-schedule"} restores an $O(h^2)$ Euclidean perturbation and hence preserves the RH-38 block law.

This closes one of the three gates listed in RH-38, but not the entire continuum continuation problem. The remaining issues are:

1.  **Stored binary64 kernel evaluation.** The present Arb certificate encloses the analytic tail formulas, not every libm exponential, logarithmic sum, and normalization operation used to construct the committed sparse arrays.

2.  **Peripheral projector convergence.** The computed Perron/parity projectors must still be compared with a smooth isolated continuum projector. Cutoff control for $P_h$ does not automatically control the Riesz projector of a nonnormal matrix [@Kato1995; @StewartSun1990].

3.  **Hierarchical resolvent recursion.** Even an $O(h^2)$ matrix bridge must be combined with a summable or bootstrapped bound for the successive Schur resolvents.

The next natural paper is therefore the projector gate, not another cutoff calculation. The cutoff branch of the maze is now mapped: fixed width leads to a tiny nonzero floor, while logarithmically growing width reaches the smooth full-kernel theorem.

# Archive and reproducibility {#sec:archive}

The machine-readable certificate records:

-   the exact archived support geometry and all analytic formulas;

-   256-bit Arb balls and upper endpoints for the three stored grids;

-   the positive fixed-eight-sigma continuum tail enclosure;

-   the two Haar cutoff ledgers and the adaptive crossover dimension;

-   hashes of the RH-5 identity, RH-18 sparse builder, and RH-38 block inputs; and

-   the precise theorem limitations.

The fast replay is

    python -m pytest -q -p no:cacheprovider
    python experiments/build_cutoff_certificate.py
    MPLBACKEND=Agg python experiments/make_figures.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
    cp main.pdf uniform-gaussian-cutoff-bridge.pdf
    python experiments/build_archive.py
    python experiments/verify_archive.py

The dense floating pilot can be rebuilt in a few seconds on the archived three grids:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    python experiments/run_cutoff_pilot.py

No zero-noise limit, zeta-zero identification, Hilbert--Pólya operator, or Riemann-hypothesis conclusion is asserted.

# Conclusion

The hard folded-Gaussian cutoff does not need to be differentiated. Its actual integer support rule supplies a deterministic buffer; Gaussian lattice tails and the exact row-renormalization identity then give a uniform full-versus-cutoff norm bound. This perturbation passes directly through the unitary Haar coordinates.

At the stored dimensions, the eight-sigma bridge is below $3.20\times10^{-13}$ at block level and is numerically irrelevant. As a matter of analysis, fixed eight sigma still converges to a truncated operator, not the full Gaussian operator. Growing the support by only $2\sqrt{\log(1/h)}$ standard deviations restores a second-order Euclidean bridge and therefore closes the cutoff gate in the all-grid route.

The remaining obstruction is sharper than before: one must now validate the dimension-dependent peripheral projectors and control their interaction with the multilevel nonnormal resolvent recursion.
