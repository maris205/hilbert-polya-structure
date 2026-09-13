---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-360-terminal-lag-exponential-tilt-phase-transition"
canonical_tex: "zeta_mvp0/papers/RH-360-terminal-lag-exponential-tilt-phase-transition/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-360-terminal-lag-exponential-tilt-phase-transition/main.pdf"
source_sha256: "4eaca94742a8c6a161870410062dfbdcac73e79004469de6329558f58f9b191a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Terminal-Lag Exponential-Tilt Phase Transition for the Complete Upper Counterloop Band

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-360-terminal-lag-exponential-tilt-phase-transition>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-360-terminal-lag-exponential-tilt-phase-transition/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-360-terminal-lag-exponential-tilt-phase-transition/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-360-terminal-lag-exponential-tilt-phase-transition/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-360-terminal-lag-exponential-tilt-phase-transition/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the full exponential-transform phase diagram of the deterministic terminal-lag distribution isolated in RH-358. Let $$\pi_k(r)=\frac{y_k^{2k-1-r}/(2k-1-r)}{C_k},
   \qquad 0\le r\le k-2,$$ where $y_k=x\exp[-\log C_M/k+o(k^{-1})]$ and $x>1$, and define $G_k(z)=\sum_rz^r\pi_k(r)$. For fixed $0\le z<x$, $$G_k(z)\longrightarrow\frac{1-x^{-1}}{1-z/x}.$$ In the critical window $z_k=x\exp(\tau/k)$, $$\frac{G_k(z_k)}k\longrightarrow
   2(1-x^{-1})\int_0^1\frac{e^{(\tau+\log C_M)s}}{2-s}\,ds.$$ For fixed $z>x$, $$G_k(z)\sim
   \frac{2C_M(1-x^{-1})}{1-x/z}\left(\frac zx\right)^{k-2}.$$ The tilted laws converge respectively to a terminal geometric distribution, a continuous critical density on the scaled lag $r/k$, and an opposite-endpoint geometric distribution. Thus $k^{-1}\log G_k(z)$ has the sharp limit $\max\{0,\log(z/x)\}$. These are normalized deterministic budget laws, not spectral or noisy stochastic distributions. Actual-head inheritance remains conditional on the original unnormalized same-clock leaf $D_{4k}(R)\to0$. No determinant, Gate A--E, Hilbert--Polya, zero-identification, or RH claim is made.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  A Terminal-Lag Exponential-Tilt Phase Transition\
  for the Complete Upper Counterloop Band
```

## Markdown 正文

# Exact transform identity

The source-locked radial law is $$\label{eq:y}
 y_k=x\exp\left[-\frac{\log C_M}{k}+o(k^{-1})\right],
 \qquad x>1,\quad C_M>0.$$ RH-358 defines the complete deterministic strict upper budget $$\label{eq:C}
 C_k=\sum_{r=0}^{k-2}\frac{y_k^{2k-1-r}}{2k-1-r}$$ and the terminal-lag probability $$\label{eq:pi}
 \pi_k(r)=\frac{y_k^{2k-1-r}/(2k-1-r)}{C_k},
 \qquad 0\le r\le k-2,$$ extended by zero to $\mathbb Z_{\ge0}$ [@WangTerminalLag2026]. It converges in total variation to the geometric law $(1-x^{-1})x^{-r}$. That convergence alone does not control arbitrary exponential observables; the present theorem finds the exact uniform-integrability boundary.

For $z\ge0$, define $$\label{eq:G}
 G_k(z):=\sum_{r=0}^{k-2}z^r\pi_k(r).$$ For $u\ge0$, introduce the finite sum $$\label{eq:A}
 A_k(u):=\sum_{r=0}^{k-2}u^r\frac{2k-1}{2k-1-r}.$$

[\[prop:quotient\]]{#prop:quotient label="prop:quotient"} For every $z\ge0$, $$\label{eq:quotient}
 \boxed{G_k(z)=\frac{A_k(z/y_k)}{A_k(1/y_k)}.}$$ Moreover, $$\label{eq:denominator}
 A_k(1/y_k)\longrightarrow\frac1{1-x^{-1}}.$$

Multiply numerator and denominator of [\[eq:G\]](#eq:G){reference-type="eqref" reference="eq:G"} by $(2k-1)y_k^{-(2k-1)}$ to obtain [\[eq:quotient\]](#eq:quotient){reference-type="eqref" reference="eq:quotient"}. For each fixed $r$, $y_k^{-r}(2k-1)/(2k-1-r)\to x^{-r}$. Choose $1<\xi<x$ with $y_k\ge\xi$ eventually. On the support, $(2k-1)/(2k-1-r)<2$, so the summands are bounded by $2\xi^{-r}$. Dominated convergence gives [\[eq:denominator\]](#eq:denominator){reference-type="eqref" reference="eq:denominator"}.

# Subcritical, critical, and supercritical transforms

[\[thm:three-regimes\]]{#thm:three-regimes label="thm:three-regimes"} The following statements hold.

1.  If $0\le z<x$ is fixed, then $$\label{eq:subcritical}
     \boxed{G_k(z)\longrightarrow
     \frac{1-x^{-1}}{1-z/x}.}$$ The convergence is locally uniform on $[0,x)$.

2.  Fix $\tau\in\mathbb R$ and put $$\label{eq:critical-z}
     z_k=x\exp(\tau/k),
     \qquad \eta:=\tau+\log C_M.$$ Then $$\label{eq:critical}
     \boxed{
     \frac{G_k(z_k)}k\longrightarrow
     \Phi(\eta):=
     2(1-x^{-1})\int_0^1\frac{e^{\eta s}}{2-s}\,ds.}$$

3.  If $z>x$ is fixed, then $$\label{eq:supercritical}
     \boxed{
     G_k(z)\sim
     \frac{2C_M(1-x^{-1})}{1-x/z}
     \left(\frac zx\right)^{k-2}.}$$

For the first statement, $z/y_k\to z/x<1$. On any compact subinterval below $x$, the numerator in [\[eq:quotient\]](#eq:quotient){reference-type="eqref" reference="eq:quotient"} is dominated by one common geometric sequence. Thus $$A_k(z/y_k)\longrightarrow\frac1{1-z/x};$$ combine with [\[eq:denominator\]](#eq:denominator){reference-type="eqref" reference="eq:denominator"}.

In the critical window, [\[eq:y\]](#eq:y){reference-type="eqref" reference="eq:y"} gives $$\label{eq:critical-u}
 k\log(z_k/y_k)\longrightarrow\eta.$$ Uniformly for $0\le r\le k-2$, $$(z_k/y_k)^r=e^{\eta r/k+o(1)},
 \qquad
 \frac{2k-1}{2k-1-r}
 =\frac{2}{2-r/k}+o(1).$$ Therefore the Riemann sum satisfies $$\frac1kA_k(z_k/y_k)
 \longrightarrow2\int_0^1\frac{e^{\eta s}}{2-s}\,ds.$$ Division by [\[eq:denominator\]](#eq:denominator){reference-type="eqref" reference="eq:denominator"} proves [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"}.

For $z>x$, write $u_k=z/y_k\to z/x>1$ and reverse the numerator sum: $$\label{eq:reverse-super}
 A_k(u_k)=u_k^{k-2}\frac{2k-1}{k+1}
 \sum_{\ell=0}^{k-2}u_k^{-\ell}\frac{k+1}{k+1+\ell}.$$ Dominated convergence gives a sum limit $(1-x/z)^{-1}$, while the prefactor ratio tends to two. Finally, $$\label{eq:super-power}
 u_k^{k-2}\sim C_M(z/x)^{k-2}$$ by [\[eq:y\]](#eq:y){reference-type="eqref" reference="eq:y"}. Use [\[eq:denominator\]](#eq:denominator){reference-type="eqref" reference="eq:denominator"} to obtain [\[eq:supercritical\]](#eq:supercritical){reference-type="eqref" reference="eq:supercritical"}.

[\[cor:free-energy\]]{#cor:free-energy label="cor:free-energy"} For every fixed $z\ge0$, $$\label{eq:free-energy}
 \boxed{
 \lim_{k\to\infty}\frac1k\log G_k(z)
 =\max\left\{0,\log\frac zx\right\},}$$ where the right side is interpreted as zero at $z=0$.

For $z<x$, [\[eq:subcritical\]](#eq:subcritical){reference-type="eqref" reference="eq:subcritical"} has a finite positive limit. At $z=x$, use [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"} with $\tau=0$ to get $G_k(x)\sim k\Phi(\log C_M)$. For $z>x$, take logarithms in [\[eq:supercritical\]](#eq:supercritical){reference-type="eqref" reference="eq:supercritical"}.

The subcritical transform forgets $C_M$. At $z=x$, the leading constant is $\Phi(\log C_M)$, and above $x$ the factor $C_M$ appears explicitly. Replacing $y_k$ by $x$ before taking the critical or supercritical limit loses a leading constant.

# The three tilted distribution limits

Whenever $G_k(z)>0$, define the mathematical tilted probability $$\label{eq:tilted}
 \pi_{k,z}(r):=\frac{z^r\pi_k(r)}{G_k(z)}.$$

[\[thm:tilted\]]{#thm:tilted label="thm:tilted"} The tilted laws have the following limits.

1.  For fixed $0\le z<x$, extended by zero off the finite support, $$\label{eq:sub-tilt}
     \pi_{k,z}\longrightarrow
     (1-z/x)(z/x)^r$$ in total variation on $\mathbb Z_{\ge0}$, with the $z=0$ law interpreted as $\delta_0$.

2.  For $z_k=x\exp(\tau/k)$, the scaled lag $R_k/k$ under $\pi_{k,z_k}$ converges weakly on $[0,1]$ to the density $$\label{eq:critical-density}
     f_\eta(s)=
     \frac{e^{\eta s}/(2-s)}
     {\displaystyle\int_0^1e^{\eta u}/(2-u)\,du},
     \qquad \eta=\tau+\log C_M.$$

3.  For fixed $z>x$, let $L_k=k-2-R_k$. Then $$\label{eq:super-tilt}
     \mathbb P_{\pi_{k,z}}(L_k=\ell)
     \longrightarrow(1-x/z)(x/z)^\ell$$ in total variation on $\mathbb Z_{\ge0}$.

The tilted unnormalized weights are $$\label{eq:tilted-weights}
 (z/y_k)^r\frac{2k-1}{2k-1-r}.$$ Below $x$, these weights converge pointwise to $(z/x)^r$ and have a common summable geometric envelope. Dominated convergence before and after normalization proves [\[eq:sub-tilt\]](#eq:sub-tilt){reference-type="eqref" reference="eq:sub-tilt"}.

In the critical window, for every continuous $g$ on $[0,1]$, the same Riemann sum used in [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"} gives $$\frac1k\sum_{r=0}^{k-2}g(r/k)
 (z_k/y_k)^r\frac{2k-1}{2k-1-r}
 \longrightarrow2\int_0^1g(s)\frac{e^{\eta s}}{2-s}\,ds.$$ Divide by the case $g=1$ to obtain [\[eq:critical-density\]](#eq:critical-density){reference-type="eqref" reference="eq:critical-density"}.

Above $x$, substitute $r=k-2-\ell$ into [\[eq:tilted-weights\]](#eq:tilted-weights){reference-type="eqref" reference="eq:tilted-weights"} and divide by the $\ell=0$ weight. The ratio tends to $(x/z)^\ell$ and is dominated by a common geometric sequence. Normalization proves [\[eq:super-tilt\]](#eq:super-tilt){reference-type="eqref" reference="eq:super-tilt"}.

The probabilities in [\[eq:tilted\]](#eq:tilted){reference-type="eqref" reference="eq:tilted"} are normalized deterministic absolute budget weights. They are not eigenvalue distributions, root-counting measures, Gibbs states of the noisy operator, or local probability laws for the dynamics.

# Conditional actual-head inheritance

Let $\pi_k^{\mathcal H}$ be the actual even-weight lag distribution defined in RH-358. Under the original same-clock unnormalized leaf $$\label{eq:D}
 D_{4k}(R):=\sum_{2\le n<4k}
 \frac{|h_{\sigma,n}-s_{k,n}|R^n}{n}\longrightarrow0,$$ RH-358 proves the stronger coordinatewise conclusion $$\label{eq:coordinate-transfer}
 \delta_k:=\sup_{0\le r\le k-2}
 \left|\frac{\pi_k^{\mathcal H}(r)}{\pi_k(r)}-1\right|\longrightarrow0.$$ For any sequence $z_k\ge0$, put $$\label{eq:actual-G}
 G_k^{\mathcal H}(z_k):=\sum_rz_k^r\pi_k^{\mathcal H}(r).$$

[\[thm:conditional\]]{#thm:conditional label="thm:conditional"} Assume [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"}. For every nonnegative tilt sequence, $$\label{eq:G-transfer}
 \left|\frac{G_k^{\mathcal H}(z_k)}{G_k(z_k)}-1\right|\le\delta_k\longrightarrow0.$$ Moreover, if $z_k>0$ and $\pi_{k,z_k}^{\mathcal H}$ is the normalized actual tilted law, then $$\label{eq:tilt-transfer}
 \sup_r\left|
 \frac{\pi_{k,z_k}^{\mathcal H}(r)}{\pi_{k,z_k}(r)}-1
 \right|\longrightarrow0.$$ If $z_k=0$, both tilted laws are exactly $\delta_0$ whenever they are defined. Consequently every transform and tilted-law conclusion above transfers only under [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"}.

The ratio in [\[eq:G-transfer\]](#eq:G-transfer){reference-type="eqref" reference="eq:G-transfer"} is a weighted average of $\pi_k^{\mathcal H}(r)/\pi_k(r)$ with nonnegative weights $z_k^r\pi_k(r)$, so its distance from one is at most $\delta_k$. Equation [\[eq:tilt-transfer\]](#eq:tilt-transfer){reference-type="eqref" reference="eq:tilt-transfer"} follows by dividing the coordinatewise ratio by $G_k^{\mathcal H}(z_k)/G_k(z_k)$.

The hypothesis [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"} remains open. This conditional theorem transfers budget laws only and contains no root, rank, or determinant identification.

# Finite protocol, boundary, and review trigger

The artifact uses the exact rational fixture $x=2352/1445$, $C_M=1$ to reproduce exact subcritical and supercritical transforms, plus high-precision critical-window Riemann-integral diagnostics and tilted-law distances. Finite rows do not prove the limiting regimes.

The next paper is RH-361, the ten-layer review of RH-352--RH-361. It should audit the deterministic/actual boundary, preserve every open hypothesis, build the batch archive, and update the repository handoff.

RH-360 does not prove [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"}; identify actual roots, ranks, or spectra; close a determinant, $p$, the unrelated open $q$, or $E_{\rm off}$; close the moving noisy envelope of RH-241 [@WangEnvelopeReview2026]; or activate the gluing criterion of RH-288 [@WangGluing2026]. Gates A--E remain false/open. There is no Hilbert--Polya operator, Riemann-zero identification, von Mangoldt trace theorem, completed-zeta divisor equality, or proof of RH.
