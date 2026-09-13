---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-11-collet-eckmann-flat-trace-completion"
canonical_tex: "zeta_mvp0/papers/RH-11-collet-eckmann-flat-trace-completion/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-11-collet-eckmann-flat-trace-completion/collet-eckmann-flat-trace-completion.pdf"
source_sha256: "41b206e2ec7bec9ce65345b2d79d0e5a7f51b056ed23763e1e62f780b882ad9a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Unconditional Parity-Centered Flat Traces at a Quadratic Band-Merging Map: Collet--Eckmann Weighted Zeta Continuation and Completion of the Small-Noise Double Limit

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-11-collet-eckmann-flat-trace-completion>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-11-collet-eckmann-flat-trace-completion/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-11-collet-eckmann-flat-trace-completion/collet-eckmann-flat-trace-completion.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-11-collet-eckmann-flat-trace-completion/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-11-collet-eckmann-flat-trace-completion/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At the algebraic band-merging parameter of $f_u(x)=1-u x^2$, a previous long-cycle analysis reduced the deterministic problem to the hypothesis $$P_m=1+(-1)^m+O(\theta^m),
   \qquad
   P_m=\sum_{f^m(x)=x}\frac{1}{|1-(f^m)'(x)|}.$$ That estimate was deliberately left conditional because the ordinary correlation gap does not itself identify a flat trace. We remove the hypothesis.

  Let $u_{\mathrm c}$ solve $u^3-2u^2+2u-2=0$, put $r=u_{\mathrm c}-1$, and $\lambda=2u_{\mathrm c}r=1.678573510428\ldots$. The critical value has the exact derivative growth $$|(f^n)'(1)|=2u_{\mathrm c}\lambda^{n-1}.$$ Moreover $T=f^2$ restricts to two topologically mixing full-branch unimodal maps on $[-r,r]$ and $[r,1]$. Their critical-value derivatives are exactly $\lambda^{2n}$ and $2u_{\mathrm c}\lambda^{2n-1}$. Thus both component maps satisfy the Collet--Eckmann condition with no numerical input.

  We apply the Keller--Nowicki weighted-zeta theorem to the two components. For the standard Perron periodic weight $$Q_m=\sum_{f^m(x)=x}\frac{1}{|(f^m)'(x)|},$$ it yields $Q_m=1+(-1)^m+O(\rho^m)$ for some $\rho<1$. Endpoint conventions change the component zeta functions only by the explicit repelling-boundary factor $1-z/\lambda^2$. The two component sums are exactly equal, and their shared fixed point contributes $\lambda^{-2n}$.

  The remaining bridge from $Q_m$ to $P_m$ is elementary but essential. Uniform hyperbolicity on periodic orbits for Collet--Eckmann maps gives $\min_{f^m p=p}|(f^m)'(p)|\ge C\Lambda^m$. Hence $$|P_m-Q_m|
   \le 2Q_m\left(\min_{f^m p=p}|(f^m)'(p)|\right)^{-1}
   =O(\Lambda^{-m}).$$ Consequently the parity-centered flat-trace gap is unconditional. This completes the earlier noncommuting-limit theorem and proves analyticity of the deterministic centered determinant in a disk strictly larger than the unit disk.

  An exhaustive audit through $m=28$ verifies the component pairing and trace identities. It also finds the sharper numerical laws $Q_{2n}-2\sim-2\lambda^{-n}$ and $P_{2n}-Q_{2n}=O(\lambda^{-3n})$. The smallest positive zero of the degree-14 centered component-zeta truncation is $1.67915634$, within $5.83\times10^{-4}$ of $\lambda$. These sharp rates and the zero at $z=\lambda$ are stated as a conjecture, not used in the proof.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: July 2026
title: |
  **Unconditional Parity-Centered Flat Traces** **at a Quadratic Band-Merging Map:**\
  Collet--Eckmann Weighted Zeta Continuation and Completion of the Small-Noise Double Limit
```

## Markdown 正文

**Keywords:** Collet--Eckmann map; weighted dynamical zeta function; flat trace; periodic orbit; parity decomposition; quadratic map; regularized determinant.

**MSC 2020:** 37E05; 37C30; 37D25; 47A10; 47B10.

# Introduction

For a smooth expanding map, periodic sums, transfer-operator eigenvalues, and dynamical zeta functions are different presentations of one spectral object. For a unimodal map with a critical point, the same statement requires an adapted Markov extension: the inverse derivative is singular at the critical value, and the invariant density has postcritical spikes. An ordinary decay of correlations theorem therefore cannot simply be relabeled as a flat-trace theorem.

This distinction arose in the long-cycle study of the normalized Gaussian perturbation of a quadratic band-merging map [@WangLongCycle2026]. Exact Markov counting and inverse branches gave a logarithmic cycle-localization horizon, while compact strong positivity gave $$\label{eq:noisy-long-limit-intro}
 \operatorname{tr}\mathcal K_\sigma^m\longrightarrow1
 \qquad(m\to\infty)$$ at every fixed $\sigma>0$. For each fixed $m\ge2$, the small-noise theorem of @WangSmallNoise2026 gave $$\label{eq:fixed-length-intro}
 \lim_{\sigma\downarrow0}\operatorname{tr}\mathcal K_\sigma^m=P_m,
 \qquad
 P_m=\sum_{f^m(x)=x}|1-(f^m)'(x)|^{-1}.$$ The opposite long-cycle limit was reduced to an explicit adapted flat-trace gap assumption. The aim here is to discharge exactly that assumption.

The key is to avoid asking the zeta theorem to produce the nonstandard denominator $|1-(f^m)'|$ directly. Introduce first the standard Perron periodic weight $$\label{eq:Q-intro}
 Q_m=\sum_{f^m(x)=x}|(f^m)'(x)|^{-1}.$$ The Keller--Nowicki theory was designed precisely for this weight at Collet--Eckmann unimodal maps: it constructs a quasicompact transfer operator on a Markov extension and identifies its isolated eigenvalues with zeta poles [@KellerNowicki1992]. At the present parameter, the hypotheses can be checked algebraically and separately on the two mixing components of $f^2$.

The second step is a uniform comparison. If $D=|(f^m)'(p)|\ge2$, then $$\label{eq:pointwise-comparison-intro}
 \left|
 \frac1{|1-(f^m)'(p)|}-\frac1D
 \right|
 \le\frac{2}{D^2}.$$ Collet--Eckmann uniform hyperbolicity on periodic orbits makes the additional factor $D^{-1}$ exponentially small [@Nowicki1988]. Thus the weighted zeta asymptotic transfers to the physical flat trace.

## Main results and status {#main-results-and-status .unnumbered}

1.  The critical orbit and all Collet--Eckmann constants needed here are explicit. No parameter-exclusion or almost-every-parameter result is used.

2.  The two restrictions of $f^2$ are mixing full-branch $S$-unimodal maps. Keller--Nowicki weighted-zeta continuation gives a component periodic weight $q_n=1+O(\rho^n)$.

3.  The component weighted sums are exactly paired. Accounting for the shared fixed point gives $$Q_{2n}=2+O(\rho^n),
      \qquad Q_{2n+1}=\lambda^{-(2n+1)}.$$

4.  Uniform periodic expansion and [\[eq:pointwise-comparison-intro\]](#eq:pointwise-comparison-intro){reference-type="eqref" reference="eq:pointwise-comparison-intro"} prove $P_m-Q_m=O(\eta^m)$ for some $\eta<1$. Therefore $$P_m=1+(-1)^m+O(\theta^m)$$ unconditionally.

5.  The two iterated small-noise/even-cycle limits are now unconditional: $$\lim_{\sigma\downarrow0}\lim_{n\to\infty}
      \operatorname{tr}\mathcal K_\sigma^{2n}=1,
      \qquad
      \lim_{n\to\infty}\lim_{\sigma\downarrow0}
      \operatorname{tr}\mathcal K_\sigma^{2n}=2.$$

6.  Numerically, the first centered component-zeta zero converges rapidly to $\lambda$. The associated sharp asymptotic is isolated as a conjecture.

The new theorem is an application and completion theorem, not a replacement for the general results of Keller and Nowicki. Its contribution is the exact verification at the band-merging map, the period-two component bookkeeping, and the bridge from the standard zeta weight to the physical Gaussian flat-trace coefficient.

# Exact band-merging and component geometry {#sec:geometry}

Let $$\label{eq:family}
 f_u(x)=1-u x^2,
 \qquad I=[-1,1].$$ Let $u_{\mathrm c}$ be the root in $(1,2)$ of $$\label{eq:parameter}
 u^3-2u^2+2u-2=0,$$ and put $$\label{eq:constants}
 r=u_{\mathrm c}-1,
 \qquad
 \lambda=2u_{\mathrm c}r.$$ Then $$\label{eq:critical-orbit}
 0\longmapsto1\longmapsto-r\longmapsto r\longmapsto r,
 \qquad f'(r)=-\lambda,$$ with $$\label{eq:numerical-constants}
 u_{\mathrm c}=1.543689012692075\ldots,
 \quad r=0.543689012692075\ldots,
 \quad \lambda=1.678573510428318\ldots.$$

The core $X=[-r,1]$ has the Markov partition $$\label{eq:partition}
 A=[-r,0],\qquad B=[0,r],\qquad C=[r,1],$$ with $f(A)=f(B)=C$ and $f(C)=A\cup B$. The corresponding transition matrix has spectrum $\{0,\sqrt2,-\sqrt2\}$, and the two cyclic components are $$\label{eq:components}
 X_0=[-r,r],
 \qquad
 X_1=[r,1].$$ The exact geometry and parity eigenmode were developed in @WangParity2026.

Put $T=f^2$. On $X_0$, the two intervals $[-r,0]$ and $[0,r]$ are full branches of $T$ onto $X_0$; the unique critical point is $c_0=0$. On $X_1$, put $$\label{eq:high-critical}
 c_1=u_{\mathrm c}^{-1/2}.$$ The intervals $[r,c_1]$ and $[c_1,1]$ are full branches of $T$ onto $X_1$. Both component transition matrices therefore have every entry equal to one and are topologically mixing.

[\[lem:exact-ce\]]{#lem:exact-ce label="lem:exact-ce"} The original critical value satisfies, for every $n\ge1$, $$\label{eq:f-ce}
 |(f^n)'(f(0))|
 =|(f^n)'(1)|
 =2u_{\mathrm c}\lambda^{n-1}.$$ For the component maps $T_j=T|_{X_j}$, $$\begin{aligned}
 |(T_0^n)'(T_0(c_0))|
 &=\lambda^{2n},\label{eq:central-ce}\\
 |(T_1^n)'(T_1(c_1))|
 &=2u_{\mathrm c}\lambda^{2n-1}.
 \label{eq:high-ce}\end{aligned}$$ In particular, $f,T_0,T_1$ satisfy the Collet--Eckmann condition.

Starting from the critical value $1$, the derivative factors are $|f'(1)|=2u_{\mathrm c}$, $|f'(-r)|=\lambda$, and then $|f'(r)|=\lambda$ forever. This gives [\[eq:f-ce\]](#eq:f-ce){reference-type="eqref" reference="eq:f-ce"}.

For $T_0$, the critical orbit is $$\label{eq:central-critical-orbit}
 c_0=0\longmapsto-r\longmapsto r\longmapsto r,$$ and $|T'(-r)|=|T'(r)|=\lambda^2$. For $T_1$, $$\label{eq:high-critical-orbit}
 c_1\longmapsto1\longmapsto r\longmapsto r,$$ with $|T'(1)|=2u_{\mathrm c}\lambda$ and $|T'(r)|=\lambda^2$. The two formulas follow.

The Schwarzian derivative of $f$ is $$\label{eq:schwarzian}
 Sf(x)=-\frac{3}{2x^2}<0$$ away from the critical point. The composition rule for the Schwarzian shows that each $T_j$ has negative Schwarzian away from its unique quadratic critical point. Thus $T_0,T_1$ are mixing $C^3$ $S$-unimodal Collet--Eckmann maps. Their absolutely continuous invariant probabilities exist by the classical Misiurewicz theory [@Misiurewicz1981; @deMeloVanStrien1993; @Young1992].

# Standard weighted traces and component pairing {#sec:weighted}

Define $$\label{eq:PQ}
 P_m=\sum_{p\in\operatorname{Fix}(f^m)}\frac1{|1-(f^m)'(p)|},
 \qquad
 Q_m=\sum_{p\in\operatorname{Fix}(f^m)}\frac1{|(f^m)'(p)|}.$$ For a component $X_j$, define its two-step weighted sum $$\label{eq:component-q}
 q_{j,n}
 =\sum_{p\in X_j:\,T_j^n(p)=p}
 \frac1{|(T_j^n)'(p)|}.$$ The common endpoint $r$ is included in both component sums.

[\[lem:component-pairing\]]{#lem:component-pairing label="lem:component-pairing"} For every $n\ge1$, $$\label{eq:q-pairing}
 q_{0,n}=q_{1,n}=:q_n$$ and $$\label{eq:Q-reconstruction}
 Q_{2n}=2q_n-\lambda^{-2n}.$$ For odd $m$, $$\label{eq:Q-odd}
 Q_m=\lambda^{-m}.$$

The map $f$ sends a fixed point of $T^n=f^{2n}$ in $X_0$ to one in $X_1$. This map is bijective on the fixed sets: the inverse along a periodic orbit is $f^{2n-1}$. The multiplier is a cyclic product and is therefore unchanged. This proves [\[eq:q-pairing\]](#eq:q-pairing){reference-type="eqref" reference="eq:q-pairing"}.

The two component fixed sets intersect only at $r$. Its $2n$-step weighted contribution is $\lambda^{-2n}$, which has been counted twice in $q_{0,n}+q_{1,n}$; this proves [\[eq:Q-reconstruction\]](#eq:Q-reconstruction){reference-type="eqref" reference="eq:Q-reconstruction"}. Finally, $f$ interchanges $X_0\setminus\{r\}$ and $X_1\setminus\{r\}$. An odd iterate can therefore fix only the shared endpoint $r$, giving [\[eq:Q-odd\]](#eq:Q-odd){reference-type="eqref" reference="eq:Q-odd"}.

# The Collet--Eckmann weighted-zeta input {#sec:zeta-input}

For a mixing interval map $S$ with regular periodic points, define the Perron weighted zeta function $$\label{eq:perron-zeta}
 \mathcal Z_S(z)
 =\exp\left[
 \sum_{n\ge1}\frac{z^n}{n}
 \sum_{S^n p=p}\frac1{|(S^n)'(p)|}
 \right].$$

We use the following published theorem in a specialized form.

[\[thm:KN\]]{#thm:KN label="thm:KN"} Let $S:J\to J$ be a topologically mixing $C^3$ $S$-unimodal map with a nonflat critical point. Suppose $S$ satisfies the Collet--Eckmann condition and has an absolutely continuous invariant probability. Then the Perron transfer operator on its Markov extension is quasicompact. For some $R>1$, the inverse of [\[eq:perron-zeta\]](#eq:perron-zeta){reference-type="eqref" reference="eq:perron-zeta"}, with the standard finite correction for periodic partition boundaries, extends holomorphically to $|z|<R$; its zeros on the closed unit disk consist only of a simple zero at $z=1$. Equivalently, the corrected zeta function is zero-free and meromorphic there, with a simple pole at $z=1$ and no other pole on the closed unit disk. Consequently, there are $C>0$ and $0<\rho<1$ such that $$\label{eq:KN-coefficients}
 \sum_{S^n p=p}\frac1{|(S^n)'(p)|}
 =1+O(\rho^n).$$

The spectral and zeta assertions are the Perron-weight specialization of @KellerNowicki1992; the Markov-extension/Fredholm mechanism is developed in @Keller1989. We recall why the final coefficient conclusion follows. Finite boundary factors are holomorphic and nonzero on a neighborhood of the closed unit disk, so we may shrink $R$ and suppress them here; the factor in the present application is computed explicitly in [\[rem:boundary\]](#rem:boundary){reference-type="ref" reference="rem:boundary"}. After removing the simple pole, the Fredholm relation makes $(1-z)\mathcal Z_S(z)$ holomorphic and nonzero on the closed unit disk. Compactness therefore lets us choose $1<R_0<R$ before the next zero or pole. Then $$\label{eq:log-derivative}
 \frac{d}{dz}\log\bigl[(1-z)\mathcal Z_S(z)\bigr]
 =\sum_{n\ge1}\left(
 \sum_{S^n p=p}|(S^n)'(p)|^{-1}-1
 \right)z^{n-1}$$ is holomorphic on $|z|<R_0$. Cauchy's estimate gives [\[eq:KN-coefficients\]](#eq:KN-coefficients){reference-type="eqref" reference="eq:KN-coefficients"} with any $\rho>R_0^{-1}$.

[\[rem:boundary\]]{#rem:boundary label="rem:boundary"} The zeta literature may include, omit, or multiply-code periodic endpoints of a monotonicity partition. In the present component maps, the only periodic partition endpoint is $r$, with weight $\lambda^{-2n}$. Adding or removing that coefficient multiplies the zeta function by $$\label{eq:boundary-factor}
 \exp\left(\pm\sum_{n\ge1}\frac{(z/\lambda^2)^n}{n}\right)
 =(1-z/\lambda^2)^{\mp1}.$$ This factor is holomorphic and nonzero on a neighborhood of the closed unit disk. Therefore [\[eq:KN-coefficients\]](#eq:KN-coefficients){reference-type="eqref" reference="eq:KN-coefficients"} is invariant under all relevant endpoint conventions.

Every assumption of [\[thm:KN\]](#thm:KN){reference-type="ref" reference="thm:KN"} for $T_0,T_1$ was verified in [2](#sec:geometry){reference-type="ref" reference="sec:geometry"}. We immediately obtain:

[\[prop:Q-gap\]]{#prop:Q-gap label="prop:Q-gap"} There are $C_Q>0$ and $0<\theta_Q<1$ such that $$\label{eq:Q-gap}
 |Q_m-1-(-1)^m|\le C_Q\theta_Q^m
 \qquad(m\ge1).$$ More explicitly, $$\label{eq:Q-parity}
 Q_{2n}=2+O(\rho^n),
 \qquad
 Q_{2n+1}=\lambda^{-(2n+1)}.$$

Apply [\[thm:KN\]](#thm:KN){reference-type="ref" reference="thm:KN"} and [\[rem:boundary\]](#rem:boundary){reference-type="ref" reference="rem:boundary"} to either component to obtain $q_n=1+O(\rho^n)$. Insert this into [\[eq:Q-reconstruction\]](#eq:Q-reconstruction){reference-type="eqref" reference="eq:Q-reconstruction"}; the shared-endpoint correction is exponentially small. The odd formula is [\[eq:Q-odd\]](#eq:Q-odd){reference-type="eqref" reference="eq:Q-odd"}. Taking $\theta_Q=\max\{\sqrt\rho,\lambda^{-1}\}<1$ gives [\[eq:Q-gap\]](#eq:Q-gap){reference-type="eqref" reference="eq:Q-gap"}.

# From the Perron weight to the physical flat trace {#sec:comparison}

The remaining argument uses uniform periodic expansion. The exact Collet--Eckmann identity [\[eq:f-ce\]](#eq:f-ce){reference-type="eqref" reference="eq:f-ce"}, negative Schwarzian, and the absence of an attracting cycle put this map under the uniform-hyperbolicity theorem of @Nowicki1988. Hence there are constants $C_*>0$ and $\Lambda_*>1$ such that $$\label{eq:uniform-periodic-expansion}
 \min_{p\in\operatorname{Fix}(f^m)}|(f^m)'(p)|
 \ge C_*\Lambda_*^m
 \qquad(m\ge1).$$

[\[lem:flat-weighted\]]{#lem:flat-weighted label="lem:flat-weighted"} There are $C_{PW}>0$ and $0<\theta_{PW}<1$ such that $$\label{eq:flat-weighted-gap}
 |P_m-Q_m|\le C_{PW}\theta_{PW}^m
 \qquad(m\ge1).$$

Put $a=(f^m)'(p)$ and $D=|a|$. Once $m$ is large enough that the lower bound [\[eq:uniform-periodic-expansion\]](#eq:uniform-periodic-expansion){reference-type="eqref" reference="eq:uniform-periodic-expansion"} exceeds $2$, $$\begin{aligned}
 \left|\frac1{|1-a|}-\frac1D\right|
 &\le\frac{2}{D^2}.
 \label{eq:pointwise-comparison}\end{aligned}$$ Indeed, for $a>1$ the left side is $[D(D-1)]^{-1}$, and for $a<-1$ it is $[D(D+1)]^{-1}$.

Let $D_m=\min_{f^m p=p}|(f^m)'(p)|$. Summing [\[eq:pointwise-comparison\]](#eq:pointwise-comparison){reference-type="eqref" reference="eq:pointwise-comparison"} gives $$\label{eq:summed-comparison}
 |P_m-Q_m|
 \le2\sum_{f^m p=p}D(p)^{-2}
 \le\frac{2Q_m}{D_m}.$$ By [\[prop:Q-gap\]](#prop:Q-gap){reference-type="ref" reference="prop:Q-gap"}, the sequence $Q_m$ is bounded. Combining [\[eq:summed-comparison\]](#eq:summed-comparison){reference-type="eqref" reference="eq:summed-comparison"} with [\[eq:uniform-periodic-expansion\]](#eq:uniform-periodic-expansion){reference-type="eqref" reference="eq:uniform-periodic-expansion"} proves the result for all sufficiently large $m$ with $\theta_{PW}=\Lambda_*^{-1}$. Enlarge the constant to absorb the finitely many remaining lengths.

[\[thm:flat-gap\]]{#thm:flat-gap label="thm:flat-gap"} There exist $C_P>0$ and $0<\theta_P<1$ such that $$\label{eq:flat-gap}
 \boxed{
 |P_m-1-(-1)^m|\le C_P\theta_P^m
 }
 \qquad(m\ge1).$$ In particular, $$\label{eq:P-limits}
 P_{2n}\longrightarrow2,
 \qquad
 P_{2n+1}\longrightarrow0$$ exponentially.

By the triangle inequality, $$\label{eq:triangle-gap}
 |P_m-1-(-1)^m|
 \le |P_m-Q_m|+|Q_m-1-(-1)^m|.$$ Use [\[lem:flat-weighted,prop:Q-gap\]](#lem:flat-weighted,prop:Q-gap){reference-type="ref" reference="lem:flat-weighted,prop:Q-gap"} and take $\theta_P=\max\{\theta_{PW},\theta_Q\}<1$.

This theorem is precisely the "adapted flat-trace gap" that was an assumption in @WangLongCycle2026. The proof also explains why it was not enough merely to cite exponential correlation decay: one first needs the weighted-zeta periodic sum and then the uniform comparison [\[eq:summed-comparison\]](#eq:summed-comparison){reference-type="eqref" reference="eq:summed-comparison"}.

# Consequences for the double limit and determinant {#sec:consequences}

## Unconditional noncommutation

Combining the fixed-noise limit [\[eq:noisy-long-limit-intro\]](#eq:noisy-long-limit-intro){reference-type="eqref" reference="eq:noisy-long-limit-intro"}, the fixed-length localization [\[eq:fixed-length-intro\]](#eq:fixed-length-intro){reference-type="eqref" reference="eq:fixed-length-intro"}, and [\[thm:flat-gap\]](#thm:flat-gap){reference-type="ref" reference="thm:flat-gap"} removes the last hypothesis from the long-cycle theorem.

[\[cor:noncommuting\]]{#cor:noncommuting label="cor:noncommuting"} For the normalized Gaussian operator at the band-merging map, $$\label{eq:noncommuting}
 \lim_{\sigma\downarrow0}\lim_{n\to\infty}
 \operatorname{tr}\mathcal K_\sigma^{2n}=1,
 \qquad
 \lim_{n\to\infty}\lim_{\sigma\downarrow0}
 \operatorname{tr}\mathcal K_\sigma^{2n}=2.$$

The first inner limit is one by compact strong positivity at fixed noise [@WangLongCycle2026]. In the opposite order, fixed-length localization gives $P_{2n}$, which tends to two by [\[thm:flat-gap\]](#thm:flat-gap){reference-type="ref" reference="thm:flat-gap"}.

## A deterministic bulk determinant beyond the unit disk

Set $$\label{eq:centered-c}
 c_m=P_m-1-(-1)^m.$$ By [\[thm:flat-gap\]](#thm:flat-gap){reference-type="ref" reference="thm:flat-gap"}, the series $$\label{eq:bulk-det}
 \widehat D_{0,\mathrm{bulk},2}(z)
 =\exp\left[-\sum_{m\ge2}\frac{c_mz^m}{m}\right]$$ is holomorphic and nonzero for $|z|<\theta_P^{-1}>1$. The two peripheral coefficients give exactly $$\label{eq:parity-factor}
 \exp\left[-\sum_{m\ge2}
 \frac{(1+(-1)^m)z^m}{m}\right]
 =1-z^2.$$ Thus the deterministic regularized cycle object has the unconditional local factorization $$\label{eq:det-factorization}
 \widehat D_{0,2}(z)
 =(1-z^2)\widehat D_{0,\mathrm{bulk},2}(z),
 \qquad |z|<\theta_P^{-1}.$$ This is an analyticity statement in a genuine disk larger than the unit disk, not merely a formal coefficient identity.

# Numerical weighted-zeta audit {#sec:numerics}

The computations enumerate every closed Markov word, solve its contracting inverse-branch equation, remove the unique doubled endpoint code, and verify the physical root count before forming any trace. The maximum length $m=28$ contains $32767$ distinct real fixed points. Each component sum includes $r$, so [\[eq:Q-reconstruction\]](#eq:Q-reconstruction){reference-type="eqref" reference="eq:Q-reconstruction"} is tested directly. NumPy, SciPy, and Matplotlib are used for the calculations [@HarrisEtAl2020; @VirtanenEtAl2020; @Hunter2007].

## Physical and Perron traces

gives representative even lengths. The component sums agree to at worst $2.30\times10^{-10}$ at the highest length, where forward multiplier conditioning is most severe. The reconstruction $2q_n-\lambda^{-2n}=Q_{2n}$ holds to $6.5\times10^{-15}$ throughout.

::: {#tab:trace-comparison}
    $m$          $P_m$          $Q_m$      $q_{m/2}$                  $P_m-Q_m$
  ----- -------------- -------------- -------------- --------------------------
      2   1.1801429862   1.2745542220   0.8147325332    $-9.44112\times10^{-2}$
      4   1.4198783447   1.4560685109   0.7910151092    $-3.61902\times10^{-2}$
      6   1.6221410887   1.6327041008   0.8387046384    $-1.05630\times10^{-2}$
     10   1.8555077105   1.8561606003   0.9308958703    $-6.52890\times10^{-4}$
     16   1.9685180854   1.9685254266   0.9843885839    $-7.34114\times10^{-6}$
     20   1.9887693744   1.9887697169   0.9944007133    $-3.42499\times10^{-7}$
     24   1.9960068858   1.9960069014   0.9980054478    $-1.56324\times10^{-8}$
     28   1.9985818867   1.9985818874   0.9992911952   $-7.05929\times10^{-10}$

  : Physical flat trace $P_m$, standard weighted trace $Q_m$, one component sum $q_{m/2}$, and their difference.
:::

Over even $14\le m\le28$, least-squares fits give $$\begin{aligned}
 \log|P_m-2|&=-0.2581396\,m+O(1),\label{eq:P-fit}\\
 \log|Q_m-2|&=-0.2581046\,m+O(1),\label{eq:Q-fit}\\
 \log|P_m-Q_m|&=-0.7694953\,m+O(1).
 \label{eq:PQ-fit}\end{aligned}$$ For comparison, $$\label{eq:reference-slopes}
 -\frac12\log\lambda=-0.2589722,
 \qquad
 -\frac32\log\lambda=-0.7769165.$$ These sharp slopes are not needed by [\[thm:flat-gap\]](#thm:flat-gap){reference-type="ref" reference="thm:flat-gap"}; the theorem only asserts some exponential rate.

![Completion audit. Top left: exact critical-value growth verifies the Collet--Eckmann input. Top right: the physical and standard weighted traces share the parity limit. Bottom left: their difference is exponentially smaller; the orange curve is the rigorous elementary bound, while the black line is only a sharp numerical reference. Bottom right: minimum periodic multipliers display the uniform expansion used in the proof.](<../../../../../zeta_mvp0/papers/RH-11-collet-eckmann-flat-trace-completion/figures/flat_trace_completion.pdf>){#fig:completion width="\\textwidth"}

## A sharp centered-zeta conjecture

For one component, write $$\label{eq:component-zeta}
 \mathcal Z(z)=\exp\left(\sum_{n\ge1}\frac{q_nz^n}{n}\right),
 \qquad
 H(z)=(1-z)\mathcal Z(z)
 =\exp\left(\sum_{n\ge1}\frac{(q_n-1)z^n}{n}\right).$$ Let $H_N$ be the degree-$N$ formal Taylor truncation obtained from $q_1,\ldots,q_N$. The smallest positive real zero $z_N$ moves monotonically toward $\lambda$ in the computed range.

::: {#tab:zeta-zero}
    $N$        $z_N$            $z_N-\lambda$   $N$        $z_N$            $z_N-\lambda$
  ----- ------------ ------------------------ ----- ------------ ------------------------
      3   1.99626296   $3.17689\times10^{-1}$     9   1.68665677   $8.08326\times10^{-3}$
      4   1.82963176   $1.51058\times10^{-1}$    10   1.68331396   $4.74045\times10^{-3}$
      5   1.75712092   $7.85474\times10^{-2}$    11   1.68136868   $2.79517\times10^{-3}$
      6   1.72150982   $4.29363\times10^{-2}$    12   1.68022757   $1.65406\times10^{-3}$
      7   1.70276673   $2.41932\times10^{-2}$    13   1.67955462   $9.81107\times10^{-4}$
      8   1.69247061   $1.38971\times10^{-2}$    14   1.67915634   $5.82832\times10^{-4}$

  : First positive real zero of the centered component-zeta truncation.
:::

The coefficients themselves show $$\label{eq:scaled-q}
 (q_n-1)\lambda^n
 =-0.92089,-0.95377,-0.97281,\ldots,-0.99929$$ for $n=5,6,7,\ldots,14$. After adding $\lambda^{-n}$, the remainder scaled by $\lambda^{2n}$ approaches one; its value at $n=14$ is $1.00017$.

[\[conj:sharp\]]{#conj:sharp label="conj:sharp"} The centered component zeta function has a simple zero at $z=\lambda$, and there is $R_*>\lambda$ such that $$\label{eq:sharp-conjecture}
 H(z)=(1-z/\lambda)G(z),$$ where $G$ is holomorphic and nonzero on $|z|<R_*$. More sharply, the observed coefficients are consistent with $$\label{eq:q-sharp}
 q_n=1-\lambda^{-n}+\lambda^{-2n}+O(\kappa^n)
 \qquad\text{for some }\kappa<\lambda^{-2}.$$

If [\[eq:q-sharp\]](#eq:q-sharp){reference-type="eqref" reference="eq:q-sharp"} holds, the exact shared-endpoint correction gives $$\label{eq:Q-sharp}
 Q_{2n}=2-2\lambda^{-n}+\lambda^{-2n}+O(\kappa^n),$$ which explains the observed slope in [\[eq:Q-fit\]](#eq:Q-fit){reference-type="eqref" reference="eq:Q-fit"}. The additional numerical law $P_{2n}-Q_{2n}=O(\lambda^{-3n})$ would then transfer the same two leading terms to the physical trace. None of these sharper statements is used in the unconditional exponential theorem.

![Centered component-zeta diagnostics. Left: the scaled coefficient approaches $-1$. Middle: the first positive truncation zero converges toward $\lambda$. Right: successive centered-zeta polynomials stabilize their crossing near the dashed algebraic value. These panels motivate [\[conj:sharp\]](#conj:sharp){reference-type="ref" reference="conj:sharp"} but are not its proof.](figures/centered_weighted_zeta.pdf){#fig:zeta width="\\textwidth"}

# Discussion

The deterministic flat-trace gap is now no longer a free-standing assumption. The proof separates three mechanisms that had previously been compressed into one heuristic statement.

First, the map is not merely a generic chaotic quadratic map: its Collet--Eckmann derivative growth is exact because the critical orbit lands on the repelling fixed point. Second, parity is handled before mixing. The raw map has period two, while each restriction of the square is mixing and falls directly under weighted-zeta theory. Third, the physical denominator $|1-(f^m)'|$ is compared to the standard Perron weight only after uniform periodic expansion has been established.

The resulting theorem is qualitative in its rate. The numerics reveal more structure: the leading centered coefficient appears to be fixed by the same multiplier $\lambda$ that controls the postcritical orbit and the logarithmic boundary-crowding scale. Proving [\[conj:sharp\]](#conj:sharp){reference-type="ref" reference="conj:sharp"} would require identifying the critical-orbit factor inside the adapted Fredholm or kneading determinant, rather than only using a zero-free annulus around the unit circle.

On the noisy side, nothing here proves the previously observed $1+\lambda_-(\sigma)\asymp\sigma^{2/3}$ law. The present result instead cleans the deterministic endpoint of that problem: any future simultaneous small-noise/long-cycle theorem can now use an unconditional deterministic bulk determinant.

# Conclusion

The postcritically finite band-merging map satisfies the hypotheses of Collet--Eckmann weighted-zeta theory by exact algebraic identities. Applying that theory to the two mixing components of the square gives the standard weighted parity trace. Uniform hyperbolicity on periodic orbits then bridges the standard weight to the physical flat trace. As a result, $$P_m=1+(-1)^m+O(\theta^m)$$ is unconditional, the two iterated small-noise/long-cycle limits are rigorously different, and the parity-renormalized deterministic determinant is analytic beyond the unit disk.

The remaining sharp problem is narrower and more concrete: explain the apparent centered-zeta zero at the algebraic multiplier $\lambda$. That zero is numerically stable but is kept outside the theorem layer until an adapted kneading or Fredholm factorization identifies it analytically.

# Data and code availability {#data-and-code-availability .unnumbered}

The source, tests, exhaustive periodic data, centered-zeta coefficients, and figure-generation script are available in the companion repository [@WangFlatTraceCode2026]. The test suite checks the exact critical orbit, Collet--Eckmann derivatives, component geometry, physical root counts, component pairing, endpoint reconstruction, flat/weighted comparison, odd trace formulas, and the finite centered-zeta algebra.
