---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-9-small-noise-cycle-localization"
canonical_tex: "zeta_mvp0/papers/RH-9-small-noise-cycle-localization/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-9-small-noise-cycle-localization/small-noise-cycle-localization.pdf"
source_sha256: "c66b5c7bf408124bc1c7d27d7fe8a78886aafeba989a5e37b51519d767fbe032"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Fixed-Length Small-Noise Localization for Gaussian Quadratic Markov Cocycles Directed Periodic-Orbit Traces and Delayed Six-Step Asymptotics

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-9-small-noise-cycle-localization>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-9-small-noise-cycle-localization/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-9-small-noise-cycle-localization/small-noise-cycle-localization.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-9-small-noise-cycle-localization/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-9-small-noise-cycle-localization/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $f_u(x)=1-u x^2$ on $[-1,1]$ and let $\mathcal K_{u,\sigma}$ be its row-normalized truncated-Gaussian Markov smoothing. Fixed positive noise makes every finite product compact, whereas the zero-noise limit is a singular deterministic composition. We prove a fixed-length bridge between the two. For a parameter word $\boldsymbol u=(u_1,\ldots,u_m)$, assume that every fixed point of $F_{\boldsymbol u}=f_{u_m}\circ\cdots\circ f_{u_1}$ is simple and that its closed orbit stays in the interior. Then, for $m\ge2$, $$\mathop{\mathrm{tr}}(\mathcal K_{u_1,\sigma}\cdots\mathcal K_{u_m,\sigma})
   =\sum_{F_{\boldsymbol u}(x)=x}\frac1{|1-F_{\boldsymbol u}'(x)|}+O(\sigma^2).$$ The proof is a parameter-uniform Laplace localization of the exact closed-path integral. Its residual Jacobian has determinant $\pm(1-F_{\boldsymbol u}')$, so Gaussian covariance factors cancel and leave the periodic-orbit weight. Parameter derivatives obey the same expansion, with an explicit exponentially small but polynomially amplified remainder governed by the action gap and boundary clearance.

  Consequently, the directed three-step trace and the parity-compatible six-step trace converge to ordered differences of deterministic periodic-orbit sums. At the quadratic band-merging parameter both limits are nonzero. Dense midpoint matrices through full dimension $15360$ recover quadratic convergence for the three-step quantities. Six-step traces enter the asymptotic regime much later, reverse sign preasymptotically, and then return toward the predicted nonzero orbit target. The result is a fixed-cycle theorem; no uniform long-cycle determinant limit is asserted.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, China
bibliography:
- references.bib
date: July 2026
title: |
  Fixed-Length Small-Noise Localization for Gaussian Quadratic Markov Cocycles\
  Directed Periodic-Orbit Traces and Delayed Six-Step Asymptotics
```

## Markdown 正文

**Keywords:** small-noise asymptotics; Gaussian Markov operator; periodic-orbit trace; nonautonomous cocycle; Laplace method; directed cycle curvature.

**MSC 2020:** 37C30; 37H10; 45C05; 47B10; 60J05.

# Introduction

Noise regularizes a deterministic map and simultaneously hides the singular nature of the zero-noise limit. At every fixed $\sigma>0$, a smooth Gaussian transition kernel defines a compact integral operator. At $\sigma=0$, it formally becomes the composition operator $g\mapsto g\circ f$, which is not a compact perturbation of the noisy family in any useful operator norm. Thus a spectral statement proved at fixed noise cannot simply be evaluated at $\sigma=0$.

Cycle traces are better behaved. A product trace has an exact closed-path integral whose phase is the squared defect from a deterministic orbit. In the weak-noise literature this observation leads to periodic-orbit expansions for stochastic evolution operators [@CvitanovicEtAl1998; @PallaEtAl2001]; it is also consonant with the general large-deviation geometry of random perturbations [@Kifer1988; @FreidlinWentzell2012; @DemboZeitouni1998]. The present problem adds three features that require a separate treatment:

1.  the Gaussian is normalized after truncation to a compact interval;

2.  the parameter changes inside the cycle, so the relevant orbit is a nonautonomous composition; and

3.  the observable of interest is a difference between two parameter orderings, including a parity-compatible six-step word.

Earlier fixed-noise work established continuum approximation, centered cycle determinants, and the first directed scalar traces for this quadratic Markov family [@WangContinuum2026; @WangCycle2026; @WangTimeOrdered2026]. In particular, reversing two factors cannot change their nonzero spectrum, while three factors can carry a directed trace. The missing bridge was whether that trace is merely a smoothing artifact or has a deterministic periodic-orbit limit.

## Main results {#main-results .unnumbered}

This paper supplies that bridge at every fixed cycle length.

1.  The exact $m$-factor trace is a Laplace integral with action $$\mathcal S_{\boldsymbol u}(\boldsymbol x)=\frac12\sum_{j=1}^{m}
      \bigl(x_j-f_{u_j}(x_{j-1})\bigr)^2,
      \qquad x_m=x_0.$$

2.  At a zero-action cycle, the residual Jacobian $J$ satisfies $$|\det J|=|1-F_{\boldsymbol u}'(x_0)|.$$ Hence the Gaussian prefactor cancels exactly and leaves the standard periodic-orbit weight.

3.  For a uniformly interior, nondegenerate family of words, the trace and every fixed finite number of parameter derivatives converge with a local $O(\sigma^2)$ expansion. Away from the zero-action tubes, the explicit remainder has the form $\sigma^{-N_r}\exp(-\Gamma/\sigma^2)$.

4.  The directed three-step and parity-compatible six-step traces converge to deterministic order differences. Their Vandermonde quotients therefore have well-defined deterministic diagonal curvatures whenever the admissible parameter neighborhood persists.

5.  Boundary contact and the degeneracy $F_{\boldsymbol u}'=1$ are exact failure conditions for the stated formula. A vanishing action gap as the cycle length grows also prevents this theorem from being promoted automatically to a full determinant limit.

6.  At the tested band-merging parameter, all three- and six-step cycles are interior and nondegenerate. The deterministic directed targets are nonzero, and the finite-noise matrices approach them. The six-step approach is highly nonmonotone because its boundary-action scale is much smaller.

The scope is deliberately fixed-length. The result identifies the exact deterministic shadow of the previously constructed directed traces. It does not exchange the limits $m\to\infty$ and $\sigma\to0$, and it does not claim a zero-noise limit for an entire Fredholm determinant.

# Normalized Gaussian words and their traces {#sec:operators}

Let $I=[-1,1]$, let $0<u<2$, and put $$\begin{aligned}
 f_u(x)&=1-u x^2,\label{eq:map}\\
 w_{u,\sigma}(x,y)&=
 \exp\left[-\frac{(y-f_u(x))^2}{2\sigma^2}\right],\\
 Z_{u,\sigma}(x)&=\int_Iw_{u,\sigma}(x,z)\,dz,\\
 q_{u,\sigma}(x,y)&=\frac{w_{u,\sigma}(x,y)}{Z_{u,\sigma}(x)}.
 \label{eq:kernel}\end{aligned}$$ Because $f_u(I)=[1-u,1]\subset I$, truncation never excludes the Gaussian mean, although the mean reaches the upper boundary at the critical point $x=0$. The observable Markov operator is $$(\mathcal K_{u,\sigma}g)(x)=\int_Iq_{u,\sigma}(x,y)g(y)\,dy.
 \label{eq:operator}$$ It is Hilbert--Schmidt on $H=L^2(I)$ and satisfies $\mathcal K_{u,\sigma}\mathbf 1=\mathbf 1$. Products of at least two factors are trace class [@Simon2005; @Kress2014].

Fix a word $\boldsymbol u=(u_1,\ldots,u_m)$ and define its chronological composition $$F_{\boldsymbol u}=f_{u_m}\circ\cdots\circ f_{u_1}.
 \label{eq:composition}$$ The corresponding noisy cycle trace is $$T_\sigma(\boldsymbol u)=
 \mathop{\mathrm{tr}}(\mathcal K_{u_1,\sigma}\cdots\mathcal K_{u_m,\sigma}),
 \qquad m\ge2.
 \label{eq:noisy-trace}$$

[\[lem:path-integral\]]{#lem:path-integral label="lem:path-integral"} With $x_m=x_0$, $$T_\sigma(\boldsymbol u)=
 \int_{I^m}
 \frac{\exp[-\mathcal S_{\boldsymbol u}(\boldsymbol x)/\sigma^2]}
 {\prod_{j=1}^m Z_{u_j,\sigma}(x_{j-1})}
 \,dx_0\cdots dx_{m-1},
 \label{eq:path-integral}$$ where $$\mathcal S_{\boldsymbol u}(\boldsymbol x)=\frac12\sum_{j=1}^{m}
 \left(x_j-f_{u_j}(x_{j-1})\right)^2.
 \label{eq:action}$$

The product kernel is obtained by integrating over the $m-1$ intermediate states. Integrating its diagonal gives [\[eq:path-integral\]](#eq:path-integral){reference-type="eqref" reference="eq:path-integral"}; this diagonal formula is valid because the product of two Hilbert--Schmidt factors is trace class and its iterated kernel is continuous. Multiplying the $m$ Gaussian weights yields [\[eq:action\]](#eq:action){reference-type="eqref" reference="eq:action"}.

The row normalizer has two different asymptotic regimes. Uniformly on $I$ it is of order $\sigma$. Near a path whose next state stays away from the boundary, it is the full Gaussian mass up to an exponentially small error.

[\[lem:normalizer\]]{#lem:normalizer label="lem:normalizer"} Fix a compact $U\Subset(0,2)$. There are constants $c,C>0$ such that, for $u\in U$, $x\in I$, and $0<\sigma\le1$, $$c\sigma\le Z_{u,\sigma}(x)\le C\sigma.
 \label{eq:normalizer-bounds}$$ If $\operatorname{dist}(f_u(x),\partial I)\ge\delta>0$, then $$Z_{u,\sigma}(x)=\sqrt{2\pi}\,\sigma
 \left[1+O\left(e^{-\delta^2/(2\sigma^2)}\right)\right].
 \label{eq:normalizer-interior}$$ The same assertion holds after any fixed finite number of $u$- and $x$-derivatives, at the cost of a polynomial factor in $\sigma^{-1}$.

The Gaussian mean lies in $I$. At a boundary mean, exactly one half of the full Gaussian is retained up to the remote-tail correction; all interior means retain more. This proves [\[eq:normalizer-bounds\]](#eq:normalizer-bounds){reference-type="eqref" reference="eq:normalizer-bounds"}. The standard Gaussian tail estimate proves [\[eq:normalizer-interior\]](#eq:normalizer-interior){reference-type="eqref" reference="eq:normalizer-interior"}, and differentiation only introduces Gaussian moments and powers of $\sigma^{-1}$.

# Zero-action cycles and the residual determinant {#sec:geometry}

Write $$R_j(\boldsymbol x)=x_j-f_{u_j}(x_{j-1}),
 \qquad j=1,\ldots,m,\qquad x_m=x_0.
 \label{eq:residual}$$ Then $\mathcal S_{\boldsymbol u}=\frac12|R|^2$. Its zero set is elementary but decisive.

[\[prop:zero-set\]]{#prop:zero-set label="prop:zero-set"} The following are equivalent:

1.  $\mathcal S_{\boldsymbol u}(\boldsymbol x)=0$;

2.  $x_j=f_{u_j}(x_{j-1})$ for every $j$;

3.  $x_0$ is a fixed point of $F_{\boldsymbol u}$ and all other coordinates are its ordered orbit.

Let $J_{\boldsymbol u}(\boldsymbol x)=D_{\boldsymbol x}R(\boldsymbol x)$. At a deterministic cycle, its nonzero entries are $$(J_{\boldsymbol u})_{j,j-1}=-f_{u_j}'(x_{j-1}),
 \qquad (J_{\boldsymbol u})_{j,j}=1,
 \label{eq:jacobian-entries}$$ with cyclic indices. Relabeling rows and columns gives the equivalent diagonal-plus-cyclic-shift matrix used in the numerical audit.

[\[prop:determinant\]]{#prop:determinant label="prop:determinant"} At a zero-action cycle based at $x_0$, $$\det J_{\boldsymbol u}=(-1)^{m-1}\bigl(1-F_{\boldsymbol u}'(x_0)\bigr),
 \qquad
 \det D^2\mathcal S_{\boldsymbol u}=\bigl(1-F_{\boldsymbol u}'(x_0)\bigr)^2.
 \label{eq:determinant-identity}$$ In particular, the minimum is nondegenerate exactly when $F_{\boldsymbol u}'(x_0)\ne1$.

In the determinant expansion of [\[eq:jacobian-entries\]](#eq:jacobian-entries){reference-type="eqref" reference="eq:jacobian-entries"}, only the identity permutation and the full cyclic permutation contribute. Their difference is $1-\prod_{j=1}^m f_{u_j}'(x_{j-1})=1-F_{\boldsymbol u}'(x_0)$, with the displayed orientation sign. Since $R=0$ at the cycle, $$D^2\mathcal S_{\boldsymbol u}=J_{\boldsymbol u}^{\mathsf T}J_{\boldsymbol u},$$ which proves the second identity.

[\[def:admissible\]]{#def:admissible label="def:admissible"} A parameter word $\boldsymbol u$ is *small-noise admissible* if

1.  every fixed point of $F_{\boldsymbol u}$ in $I$ is simple in the trace sense, $F_{\boldsymbol u}'(x)\ne1$; and

2.  every point of every associated closed orbit belongs to $(-1,1)$.

It is *uniformly admissible* on a compact parameter set if the boundary clearance and $|1-F_{\boldsymbol u}'|$ have positive uniform lower bounds.

The second condition is not cosmetic. If a zero-action cycle touches $\partial I$, both the integration tangent cone and the truncated normalizer enter the leading coefficient. The simple full-space weight in [\[prop:determinant\]](#prop:determinant){reference-type="ref" reference="prop:determinant"} then need not be the answer.

# The fixed-length localization theorem {#sec:localization}

For an admissible word define the deterministic orbit sum $$\mathcal P(\boldsymbol u)=\sum_{F_{\boldsymbol u}(x)=x}\frac1{|1-F_{\boldsymbol u}'(x)|}.
 \label{eq:orbit-sum}$$ This is a finite sum because $F_{\boldsymbol u}(x)-x$ is a nonzero polynomial and all its roots under consideration are simple.

[\[thm:localization\]]{#thm:localization label="thm:localization"} Let $m\ge2$ be fixed and let $\boldsymbol u$ be admissible. Then $$T_\sigma(\boldsymbol u)=\mathcal P(\boldsymbol u)+O(\sigma^2),
 \qquad \sigma\downarrow0.
 \label{eq:main-localization}$$ More precisely, the contribution of each closed deterministic orbit based at $x$ is $$\frac1{|1-F_{\boldsymbol u}'(x)|}\left[1+O(\sigma^2)\right],
 \label{eq:local-contribution}$$ and the complement of fixed disjoint orbit neighborhoods is exponentially small.

Choose disjoint neighborhoods of the finitely many zero-action cycles. Their closures remain in the interior by admissibility. In one such neighborhood, [\[lem:normalizer\]](#lem:normalizer){reference-type="ref" reference="lem:normalizer"} gives $$\prod_{j=1}^m Z_{u_j,\sigma}(x_{j-1})
 =(\sqrt{2\pi}\,\sigma)^m[1+O(e^{-c/\sigma^2})].$$ The phase has a nondegenerate minimum there, with Hessian $J^{\mathsf T}J$. The multidimensional Laplace expansion [@BleisteinHandelsman1986; @Wong2001] therefore gives $$\begin{aligned}
 \int_{\mathcal N_x}e^{-\mathcal S_{\boldsymbol u}(\boldsymbol x)/\sigma^2}\,d\boldsymbol x
 &=(2\pi\sigma^2)^{m/2}
 \frac{1+O(\sigma^2)}{\sqrt{\det(J^{\mathsf T}J)}}\\
 &=(\sqrt{2\pi}\,\sigma)^m
 \frac{1+O(\sigma^2)}{|1-F_{\boldsymbol u}'(x)|},\end{aligned}$$ where the last equality is [\[prop:determinant\]](#prop:determinant){reference-type="ref" reference="prop:determinant"}. The normalizer cancels the Gaussian volume exactly at leading order.

On the complement of the orbit neighborhoods, compactness and [\[prop:zero-set\]](#prop:zero-set){reference-type="ref" reference="prop:zero-set"} give $\mathcal S_{\boldsymbol u}\ge c>0$. The uniform lower bound in [\[eq:normalizer-bounds\]](#eq:normalizer-bounds){reference-type="eqref" reference="eq:normalizer-bounds"} makes that contribution at most a polynomial in $\sigma^{-1}$ times $e^{-c/\sigma^2}$, hence smaller than every algebraic power. Summing the local contributions proves the theorem.

The parameter-uniform form records why a formally asymptotic result can have a late numerical onset. Fix orbit tubes of radius $\rho$ and define the action gap $$\Delta_\rho(\boldsymbol u)=
 \inf\left\{\mathcal S_{\boldsymbol u}(\boldsymbol x):
 \boldsymbol x\in I^m\setminus\bigcup_x\mathcal N_\rho(x)\right\}.
 \label{eq:action-gap}$$ For an admissible word this number is positive when the tubes contain all zero-action cycles.

[\[thm:uniform\]]{#thm:uniform label="thm:uniform"} Let $\mathcal U$ be a compact uniformly admissible family of words of fixed length $m$. For every nonnegative integer $r$, there are constants $C_r,\Gamma>0$ and a finite integer $N_r$ such that $$\|T_\sigma-\mathcal P\|_{C^r(\mathcal U)}
 \le C_r\sigma^2+C_r\sigma^{-N_r}e^{-\Gamma/\sigma^2}.
 \label{eq:uniform-bound}$$ The exponent $N_r$ may be chosen to grow at most linearly with $r$ for the quadratic family.

Uniform admissibility gives a finite parameter cover on which the fixed-point branches, orbit tubes, Hessian inverses, and boundary clearances are uniformly controlled. The parameter-dependent Laplace expansion may therefore be differentiated $r$ times. Its local remainder is $O(\sigma^2)$ uniformly. Outside the tubes, take $\Gamma$ smaller than both the uniform action gap and the Gaussian boundary-tail exponent. Every parameter derivative acts either on a smooth coefficient or on an exponential divided by $\sigma^2$, producing only finitely many additional powers of $\sigma^{-1}$. This gives [\[eq:uniform-bound\]](#eq:uniform-bound){reference-type="eqref" reference="eq:uniform-bound"}.

For each fixed $r$, the exponential term in [\[eq:uniform-bound\]](#eq:uniform-bound){reference-type="eqref" reference="eq:uniform-bound"} is eventually smaller than $\sigma^2$. At a practical noise width, however, a small $\Gamma$ and the factor $\sigma^{-N_r}$ can dominate. Third-order parameter responses are especially sensitive because three differentiations can produce a factor of order $\sigma^{-6}$ before the exponential decay is felt.

# Directed three-block limits {#sec:directed}

For a block length $\ell\ge1$, set $$A_{u,\sigma}^{(\ell)}=\mathcal K_{u,\sigma}^{\ell}$$ and define $$\Omega_{\ell,\sigma}(a,b,c)=
 \mathop{\mathrm{tr}}\left(A_{a,\sigma}^{(\ell)}A_{b,\sigma}^{(\ell)}A_{c,\sigma}^{(\ell)}\right)
 -\mathop{\mathrm{tr}}\left(A_{a,\sigma}^{(\ell)}A_{c,\sigma}^{(\ell)}A_{b,\sigma}^{(\ell)}\right).
 \label{eq:directed-noisy}$$ The case $\ell=1$ is a three-step trace. The case $\ell=2$ is the minimal three-block trace that preserves a frozen two-step parity block, hence has six one-step factors.

Let $$\begin{aligned}
 \boldsymbol u_{\ell}^{+}(a,b,c)
 &=(\underbrace{a,\ldots,a}_{\ell},
   \underbrace{b,\ldots,b}_{\ell},
   \underbrace{c,\ldots,c}_{\ell}),\\
 \boldsymbol u_{\ell}^{-}(a,b,c)
 &=(\underbrace{a,\ldots,a}_{\ell},
   \underbrace{c,\ldots,c}_{\ell},
   \underbrace{b,\ldots,b}_{\ell})\end{aligned}$$ and $$\Omega_{\ell,0}(a,b,c)=
 \mathcal P(\boldsymbol u_{\ell}^{+})-\mathcal P(\boldsymbol u_{\ell}^{-}).
 \label{eq:directed-deterministic}$$

[\[cor:directed-limit\]]{#cor:directed-limit label="cor:directed-limit"} If both words in [\[eq:directed-deterministic\]](#eq:directed-deterministic){reference-type="eqref" reference="eq:directed-deterministic"} are admissible, then $$\Omega_{\ell,\sigma}(a,b,c)\longrightarrow
 \Omega_{\ell,0}(a,b,c)
 \qquad(\sigma\downarrow0).
 \label{eq:directed-limit}$$ For a compact uniformly admissible parameter family, the error satisfies the uniform bounds of [\[thm:uniform\]](#thm:uniform){reference-type="ref" reference="thm:uniform"}.

Apply [\[thm:localization\]](#thm:localization){reference-type="ref" reference="thm:localization"} to the two words and subtract.

Cyclic rotations of three blocks leave both traces unchanged. A transposition reverses the sign. Therefore $\Omega_{\ell,\sigma}$ and $\Omega_{\ell,0}$ are alternating functions of $(a,b,c)$. On a uniformly admissible neighborhood they factor as $$\Omega_{\ell,\sigma}(a,b,c)
 =V(a,b,c)G_{\ell,\sigma}(a,b,c),
 \qquad
 V(a,b,c)=(a-b)(b-c)(c-a),
 \label{eq:vandermonde}$$ with a smooth symmetric quotient $G$. The diagonal values $$\chi_{\ell,\sigma}(u)=G_{\ell,\sigma}(u,u,u),
 \qquad
 \chi_{\ell,0}(u)=G_{\ell,0}(u,u,u)
 \label{eq:curvatures}$$ are the noisy and deterministic orientation curvatures.

[\[cor:curvature\]]{#cor:curvature label="cor:curvature"} If a neighborhood of the diagonal word at $u$ is uniformly admissible, then $$\chi_{\ell,\sigma}(u)=\chi_{\ell,0}(u)+O(\sigma^2)
 +O\left(\sigma^{-N_3}e^{-\Gamma/\sigma^2}\right).
 \label{eq:curvature-limit}$$

Alternating smooth functions are divisible by the Vandermonde polynomial. The diagonal quotient is a fixed linear combination of third parameter derivatives. Apply [\[thm:uniform\]](#thm:uniform){reference-type="ref" reference="thm:uniform"} with $r=3$.

This result separates two questions that are easily conflated. A fixed separated directed trace may already be close to its orbit target while its diagonal curvature remains preasymptotic, because the latter probes three parameter derivatives and amplifies exponentially small path sectors.

# Exact failure conditions and the long-cycle obstruction {#sec:obstructions}

The proof identifies three distinct boundaries of the theorem.

## Trace degeneracy

If $F_{\boldsymbol u}'(x)=1$, then $\det J=0$ and the quadratic Laplace approximation fails. The contribution is no longer of order one with weight $|1-F_{\boldsymbol u}'|^{-1}$; its scaling depends on the first nonvanishing higher jet. This is a genuine dynamical bifurcation, not a numerical conditioning issue.

## Boundary contact

If a deterministic cycle contains $x_j=\pm1$, the local integration region is a cone rather than $\mathbb R^m$, and the relevant row normalizer may contain only a half Gaussian at leading order. One must then recompute the tangent-cone integral. Merely inserting the boundary orbit into [\[eq:orbit-sum\]](#eq:orbit-sum){reference-type="eqref" reference="eq:orbit-sum"} is not justified.

Even without exact contact, a small clearance $\delta$ delays the replacement of the truncated normalizer by $\sqrt{2\pi}\sigma$. The correction contains a scale comparable to $\exp[-\delta^2/(C\sigma^2)]$ and can be large until $\sigma\ll\delta$.

## No automatic determinant limit

For every fixed $m$, compactness supplies a positive action gap outside the orbit tubes. Nothing in [\[thm:localization\]](#thm:localization){reference-type="ref" reference="thm:localization"} prevents that gap, the minimum $|1-F_{\boldsymbol u}'|$, or the boundary clearance from collapsing as $m\to\infty$. The constants in [\[eq:uniform-bound\]](#eq:uniform-bound){reference-type="eqref" reference="eq:uniform-bound"} can therefore deteriorate with $m$. A Fredholm determinant is assembled from traces of all lengths [@Ruelle1976; @Baladi2018; @Bornemann2010]; interchanging its trace series with $\sigma\downarrow0$ requires a new uniform estimate. The present theorem does not supply one.

This is the next precise obstruction: fixed cycles have a deterministic shadow, but a long-cycle spectral object needs uniform orbit growth, nondegeneracy, and action-gap control.

# Numerical audit at the band-merging parameter {#sec:numerics}

The computations use $$u_c=1.543689012692,
 \qquad
 (a,b,c)=(u_c-0.12,u_c,u_c+0.12).
 \label{eq:numerical-parameters}$$ All fixed points are obtained independently from sign-changing brackets and the roots of the explicit composition polynomial, then refined against $F_{\boldsymbol u}(x)-x$. The residual determinant identity is checked orbit by orbit. Positive-action constrained minima are found by multistart optimization; they are an onset audit, not a proof of global minimality.

The noisy operators use the exact even-state folding. If $n$ is the folded dimension, the full midpoint dimension is $2n$. Except in the resolution audit, $n\sigma$ is held near $30.72$. The implementation uses NumPy, SciPy, and Matplotlib [@HarrisEtAl2020; @VirtanenEtAl2020; @Hunter2007].

## Deterministic admissibility

records every quantity needed by the theorem. The autonomous three-step word has one fixed point, while the six-step word has fifteen. All six tested words are interior and strongly nondegenerate.

::: {#tab:orbits}
  word               cycles   $\mathcal P(\boldsymbol u)$   min clearance   min $|1-F'|$            action audit
  ---------------- -------- ----------------------------- --------------- -------------- -----------------------
  $3$ autonomous          1                    0.17453335        0.456311        5.72956   $1.4155\times10^{-2}$
  $6$ autonomous         15                    1.62214109        0.017030        8.00615   $2.8309\times10^{-2}$
  $3$ forward             1                    0.17536312        0.440355        5.70245   $4.9074\times10^{-3}$
  $3$ reverse             1                    0.17538024        0.427628        5.70190   $2.8307\times10^{-3}$
  $6$ forward            11                    1.03996685        0.016242        6.98681   $7.7347\times10^{-4}$
  $6$ reverse            11                    1.03567599        0.015579        8.13820   $6.1547\times10^{-4}$

  : Deterministic orbit audit. The final column is the least positive boundary-constrained action found numerically. It is diagnostic rather than certified.
:::

The resulting directed targets are $$\Omega_{1,0}=-1.7114657240\times10^{-5},
 \qquad
 \Omega_{2,0}=0.004290861044.
 \label{eq:directed-targets}$$ Both are nonzero. Symmetric-separation Vandermonde quotients extrapolated quadratically in $\varepsilon^2$ give $$\chi_{1,0}(u_c)=-0.00487349098,
 \qquad
 \chi_{2,0}(u_c)=-3.11415342.
 \label{eq:curvature-targets}$$

![Deterministic geometry. Left: closure residuals for the autonomous three- and six-step compositions. Middle: all fifteen six-step weights; color encodes boundary clearance. Right: least positive constrained action found for the autonomous and directed words. The directed six-step action scale is roughly four to six times smaller than its three-step counterpart.](<../../../../../zeta_mvp0/papers/RH-9-small-noise-cycle-localization/figures/orbit_action_geometry.pdf>){#fig:geometry width="\\textwidth"}

## Small-noise localization

gives a representative subset of the fourteen noise levels. The three-step trace approaches its target monotonically after the first crossover. The six-step trace first moves away, peaks near $\sigma=0.015$, and only then returns. Its directed difference changes sign several times before recovering the positive target direction.

::: {#tab:noise}
    $\sigma$   full $d$   $\mathop{\mathrm{tr}}K_\sigma^3$   $\mathop{\mathrm{tr}}K_\sigma^6$       $\Omega_{1,\sigma}$   $\Omega_{2,\sigma}$
  ---------- ---------- ---------------------------------- ---------------------------------- ------------------------- ---------------------
       0.080        768                         0.19311344                         1.65903236   $-1.90682\times10^{-2}$             0.0490761
       0.040       1536                         0.17534062                         1.74737843   $-8.09025\times10^{-3}$             0.0392209
       0.020       3072                         0.17473087                         2.14680162   $-4.33771\times10^{-5}$          $-0.0062862$
       0.010       6144                         0.17458261                         2.04666127   $-1.71593\times10^{-5}$          $-0.0048432$
       0.006      10240                         0.17455108                         1.71644394   $-1.71307\times10^{-5}$          $-0.0017904$
       0.004      15360                         0.17454123                         1.64649700   $-1.71218\times10^{-5}$             0.0032098

  : Finite-noise traces. The deterministic targets are $0.17453335$, $1.62214109$, $-1.71147\times10^{-5}$, and $0.00429086$, respectively.
:::

At the five smallest widths, the fitted powers of the absolute errors are $$|\mathop{\mathrm{tr}}K_\sigma^3-\mathcal P_3|\sim\sigma^{2.00071},
 \qquad
 |\Omega_{1,\sigma}-\Omega_{1,0}|\sim\sigma^{2.00222},
 \label{eq:fitted-powers}$$ matching [\[thm:localization\]](#thm:localization){reference-type="ref" reference="thm:localization"}. At $\sigma=0.004$, their absolute errors are $7.88\times10^{-6}$ and $7.12\times10^{-9}$.

The six-step quantities are later but visibly turn toward their targets. At the smallest width, $$\mathop{\mathrm{tr}}K_\sigma^6=1.64649700,
 \qquad
 \Omega_{2,\sigma}=0.00320980,
 \label{eq:six-smallest}$$ compared with $1.62214109$ and $0.00429086$. The sign recovery in the second quantity is essential: the intermediate negative values are preasymptotic, not the deterministic orientation.

![Small-noise localization. Top: autonomous traces and their orbit targets. Bottom: directed traces normalized by their nonzero deterministic targets. The three-step ratio reaches one rapidly. The six-step ratio is nonmonotone and sign-changing before returning toward one. The horizontal axis is logarithmic and decreases to the right.](<../../../../../zeta_mvp0/papers/RH-9-small-noise-cycle-localization/figures/small_noise_localization.pdf>){#fig:localization width="94%"}

## Resolution and diagonal curvature

At fixed $\sigma=0.004$, the folded dimension was varied from $3072$ to $7680$, so $n\sigma$ ranged from $12.288$ to $30.72$. Across this range the spreads were $$\begin{array}{c|cccc}
 &\mathop{\mathrm{tr}}K^3&\mathop{\mathrm{tr}}K^6&\Omega_1&\Omega_2\\ \hline
 \text{spread}
 &6.11\times10^{-16}&1.18\times10^{-6}&3.05\times10^{-16}&1.76\times10^{-7}.
 \end{array}
 \label{eq:resolution-spread}$$ Thus the remaining six-step target error is a noise effect, not a midpoint resolution artifact. Fixed-$\sigma$ midpoint convergence follows the collectively compact theory developed for the same kernel family [@Anselone1971; @Atkinson1997; @WangContinuum2026].

![Deterministic Vandermonde quotients against squared symmetric separation. The star at zero is the extrapolated diagonal limit. Both the three-step and parity-compatible six-step limits are nonzero.](<../../../../../zeta_mvp0/papers/RH-9-small-noise-cycle-localization/figures/deterministic_curvature.pdf>){#fig:curvature width="91%"}

The contrast between [\[eq:fitted-powers\]](#eq:fitted-powers){reference-type="ref" reference="eq:fitted-powers"} and the six-step crossover is consistent with the geometry in [\[tab:orbits,fig:geometry\]](#tab:orbits,fig:geometry){reference-type="ref" reference="tab:orbits,fig:geometry"}. The directed six-step words have positive boundary-action scales near $6\times10^{-4}$ and orbit clearances near $1.6\times10^{-2}$. Both are much less favorable than for three steps. The uniform theorem predicts eventual localization but does not promise monotonic approach.

# Consequences and next mathematical gate {#sec:consequences}

The fixed-noise directed trace has passed a precise deterministic test. It is not created by Gaussian smoothing: at fixed length it converges to the difference between two ordered periodic-orbit sums. The parity-compatible six-step scalar also survives; its late onset explains why moderate-noise experiments can report the wrong sign.

Three distinctions remain important.

1.  A finite-noise resonance list and a deterministic orbit sum are not the same object. This paper relates fixed traces, not individual eigenvalues.

2.  A fixed-length result is not a determinant result. Uniform estimates in the cycle length are still missing.

3.  A nonzero directed orbit sum records temporal ordering. It does not by itself provide a canonical self-adjoint realization or a universal counting law.

The next mathematical gate is therefore unambiguous: control the orbit count, multipliers, boundary clearance, and action gap uniformly enough in $m$ to sum the centered trace series on a nontrivial domain. A positive result would produce a deterministic directed cycle determinant. A collapse of any one of those controls would be a rigorous obstruction rather than a failed numerical fit.

# Conclusion

The normalized Gaussian quadratic cocycle has a rigorous fixed-length zero-noise trace formula. Closed-path localization reduces the trace to deterministic cycles, and the residual determinant identity produces the weight $|1-F'|^{-1}$ without an undetermined covariance factor. The theorem is uniform under interiority and nondegeneracy and exposes the exponentially delayed sectors that parameter derivatives can amplify.

Both minimal directed constructions persist. The three-step trace converges quadratically and rapidly to a nonzero ordered orbit difference. The parity-compatible six-step trace is nonmonotone over a broad range but eventually recovers the predicted sign and moves toward a second nonzero target. Boundary contact, trace degeneracy, and loss of a uniform action gap are the exact places where the argument can fail.

The outcome is a constructive fixed-cycle bridge and a sharply stated next problem: determine whether the estimates can be made uniform in cycle length.

# Data and code availability {#data-and-code-availability .unnumbered}

The manuscript source, tested implementation, machine-readable tables, and complete figure script are available at <https://github.com/maris205/prime_dynamics_theory/tree/main/papers/RH-9-small-noise-cycle-localization>. Exact reproduction commands are listed in the accompanying README.

# Acknowledgments {#acknowledgments .unnumbered}

The author acknowledges the use of an AI language model for assistance with mathematical cross-checking, code auditing, manuscript organization, and typesetting. The author verified the final arguments and assumes responsibility for the content.
