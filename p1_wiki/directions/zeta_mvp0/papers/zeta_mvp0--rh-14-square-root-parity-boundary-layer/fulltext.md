---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-14-square-root-parity-boundary-layer"
canonical_tex: "zeta_mvp0/papers/RH-14-square-root-parity-boundary-layer/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-14-square-root-parity-boundary-layer/square-root-parity-boundary-layer.pdf"
source_sha256: "199d5abee0aaf7d16090cdedbb50688f177739a2d142b8e927d45e0fd5f5bb34"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Square-Root Parity Splitting at a Quadratic Band-Merging Map: Coupled Critical-Value Boundary Layers and a Corrected Small-Noise Law

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-14-square-root-parity-boundary-layer>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-14-square-root-parity-boundary-layer/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-14-square-root-parity-boundary-layer/square-root-parity-boundary-layer.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-14-square-root-parity-boundary-layer/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-14-square-root-parity-boundary-layer/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At the algebraic band-merging parameter of $f_u(x)=1-u x^2$, deterministic dynamics has two cyclic components and the zero-noise Markov operator has a parity eigenvalue $-1$. Positive Gaussian noise makes the operator strongly mixing and moves this mode to a simple real resonance $\lambda_-(\sigma)>-1$. Previous dense computations on $0.01\le\sigma\le0.03$ gave the striking fit $1+\lambda_-(\sigma)\asymp\sigma^{2/3}$. We show that this is a crossover, not the small-noise exponent.

  Two boundary layers determine the actual splitting. At the repelling component boundary $r=u_{\mathrm c}-1$, the rescaled left parity observable is exactly $$H(\xi)=-\operatorname{erf}(\kappa\xi),
   \qquad
   \kappa=\sqrt{\frac{\lambda^2-1}{2}},
   \qquad
   \lambda=2u_{\mathrm c}r.$$ It solves the Gaussian dilation equation $\mathbb E H(-\lambda\xi+Z)=-H(\xi)$. A second layer is created at the critical value $1$. If $\rho_c$ is the central-component invariant density at the critical point, then the signed right eigenmeasure satisfies $$-\sqrt\sigma\,g_{\sigma,-}(1-\sigma\xi)\longrightarrow
   R(\xi)
   =\rho_c\int_0^\infty
   \frac{\phi(u_{\mathrm c}q^2-\xi)}{\Phi(u_{\mathrm c}q^2)}\,dq.$$ Pairing the two layers gives the nonanalytic spectral law $$\boxed{
    1+\lambda_-(\sigma)=C_*\sqrt\sigma+o(\sqrt\sigma)},
   \qquad
   C_*=\int_0^\infty R(\xi)\operatorname{erfc}(a\xi)\,d\xi>0,$$ where $a=2u_{\mathrm c}\kappa/\lambda$. The exact integral evaluates numerically to $$\rho_c=0.562641254486572\ldots,
   \qquad
   C_*=0.105258535936908\ldots.$$ Consequently the parity lifetime is asymptotic to $(C_*\sqrt\sigma)^{-1}$, and the $2/3$-scaled gap diverges like $C_*\sigma^{-1/6}$.

  Sparse folded computations with up to $204800$ states reach $\sigma=10^{-4}$. They reproduce the old-window exponent $0.667416$, but the local exponent falls to $0.51613$ and $(1+\lambda_-)/\sqrt\sigma$ moves toward the predicted constant. These computations audit the asymptotic mechanism; the square-root law follows from the spectral-stability and boundary-layer argument.
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
  **Square-Root Parity Splitting**\
  **at a Quadratic Band-Merging Map:**\
  Coupled Critical-Value Boundary Layers and a Corrected Small-Noise Law
```

## Markdown 正文

**Keywords:** random perturbation; transfer operator; parity resonance; boundary layer; quadratic map; metastable spectrum; critical value; nonanalytic eigenvalue splitting.

**MSC 2020:** 37E05; 37D25; 47A55; 60J05; 65P30.

# Introduction {#sec:introduction}

Noise destroys exact cyclic decompositions. The subtle question is how quickly. At a quadratic band-merging parameter, the deterministic attractor has two components exchanged by one iterate. The associated Markov operator therefore has peripheral eigenvalues $1$ and $-1$. Every positive Gaussian noise makes the transition kernel strictly positive, leaving only the Perron root on the unit circle. The former parity mode becomes a long-lived negative resonance.

The preceding long-cycle study isolated this resonance and found $$\label{eq:old-fit}
 1+\lambda_-(\sigma)simeq
 0.2881505\,\sigma^{0.6674161}$$ over its five smallest noise levels $0.01\le\sigma\le0.03$ [@WangLongCycle2026]. It explicitly kept the $2/3$ exponent outside the theorem layer. Subsequent work completed the deterministic side: an analytic circle lift exposed the postcritical factors, and validated Wiener--Taylor bounds proved their noncancellation [@WangPostcritical2026; @WangValidatedGap2026]. Thus the stochastic splitting in [\[eq:old-fit\]](#eq:old-fit){reference-type="eqref" reference="eq:old-fit"} is now the remaining parity question.

The main point of this paper is that a single local layer gives the wrong answer. Smoothing the component jump at the repelling fixed point produces an exact error-function profile, but that profile is locally balanced and does not split the eigenvalue at leading order. Splitting occurs one preimage farther away, at the endpoint $x=1$ that maps exactly onto the component boundary. The invariant density there is itself a noise-rounded square-root spike created by the critical point. Its height is $\sigma^{-1/2}$ and its width is $\sigma$; their product forces the $\sqrt\sigma$ law.

## Main results and status {#main-results-and-status .unnumbered}

1.  Standard stochastic spectral stability for the postcritically finite quadratic map gives a unique simple real resonance $\lambda_-(\sigma)\to-1$.

2.  The component-boundary observable has the exact universal profile $H(\xi)=-\operatorname{erf}(\kappa\xi)$. No fitted parameter enters $\kappa$.

3.  The critical point and the truncation normalizer produce a second, explicit endpoint-density profile $R$. The factor $\Phi(u_{\mathrm c}q^2)^{-1}$ in $R$ is essential; dropping row normalization changes the leading constant.

4.  A solvability pairing between the left profile $H$ and the signed right density $R$ proves $$1+\lambda_-(\sigma)=C_*\sqrt\sigma+o(\sqrt\sigma),
      \qquad C_*>0.$$

5.  Hence the parity e-folding time is $(C_*\sqrt\sigma)^{-1}(1+o(1))$. For $m\sqrt\sigma\to t$, the peripheral mode has the crossover $(-1)^m e^{-C_*t}$.

6.  The former $2/3$ law is ruled out asymptotically: $(1+\lambda_-)/\sigma^{2/3}\to\infty$. Its accurate appearance on the old window is reproduced exactly and explained as preasymptotic drift.

7.  All finite matrices, fitted exponents, and profile comparisons are diagnostics. The decimal evaluation of $C_*$ is numerical, while its positive integral formula and the exponent $1/2$ are analytic conclusions.

# The folded Gaussian operator and deterministic parity {#sec:operator}

Let $u=u_{\mathrm c}$ be the real root in $(1,2)$ of $$\label{eq:cubic}
 u^3-2u^2+2u-2=0,$$ and put $$\label{eq:constants}
 r=u_{\mathrm c}-1,
 \qquad
 \lambda=2u_{\mathrm c}r.$$ Then $$\label{eq:critical-orbit}
 0\longmapsto1\longmapsto-r\longmapsto r\longmapsto r,$$ and $$\label{eq:numerical-constants}
 u_{\mathrm c}=1.543689012692076\ldots,
 \quad
 r=0.543689012692076\ldots,
 \quad
 \lambda=1.678573510428322\ldots.$$

Write $f=f_{u_{\mathrm c}}$ and fold the signed state by $x\mapsto|x|$. On $[0,1]$ the deterministic map is $$\label{eq:folded-map}
 T(x)=|1-u_{\mathrm c}x^2|.$$ Up to the common endpoint $r$, the intervals $$\label{eq:components}
 B=[0,r],
 \qquad
 C=[r,1]$$ are exchanged by $T$. Thus $$\label{eq:hard-parity}
 h_0=\mathbf1_B-\mathbf1_C,
 \qquad
 h_0\circ T=-h_0$$ away from the two boundary preimages.

Let $$\label{eq:gaussian}
 \phi_\sigma(t)=\frac1{\sqrt{2\pi}\sigma}
 e^{-t^2/(2\sigma^2)},
 \qquad
 Z_\sigma(x)=\int_{-1}^1\phi_\sigma(y-f(x))\,dy.$$ The normalized folded Markov operator acting on observables is $$\label{eq:markov-operator}
 (\mathcal K_\sigma h)(x)
 =\frac1{Z_\sigma(x)}
 \int_{-1}^1\phi_\sigma(y-f(x))h(|y|)\,dy.$$ It is compact and strongly positive for every $\sigma>0$. Its dual density operator is denoted by $\mathcal P_\sigma$.

## Peripheral spectral stability

The map is postcritically finite and Misiurewicz. Its deterministic transfer operator is quasi-compact on the standard tower/spike space $\mathcal B$: a regular bounded-variation part is augmented by the finitely generated one-sided square-root singularities along [\[eq:critical-orbit\]](#eq:critical-orbit){reference-type="eqref" reference="eq:critical-orbit"} [@Misiurewicz1981; @KellerNowicki1992; @Baladi2000]. We use $L^1$ as the weak norm. The two mixing components give two simple peripheral eigenvalues $1$ and $-1$.

For completeness, we check the only feature of the present perturbation that is not covered verbatim by the usual additive-noise construction. Before folding, choose a slightly larger ambient interval $J\supset[-1,1]$ with $f(J)\subset\operatorname{int}J$; the ordinary tower estimates are applied there. Let $Q_\sigma$ denote Gaussian convolution after extension by zero, and put $M_\sigma g=Z_\sigma^{-1}g$. Restriction and conditioning on the physical state interval then have the exact factorization $$\label{eq:conditioned-factorization}
 \mathcal P_\sigma g
 =\mathbf1_{[-1,1]}Q_\sigma\mathcal P_0(M_\sigma g).$$ On a fixed neighborhood of the critical point, $$\label{eq:normalizer-local}
 Z_\sigma(x)
 =\Phi\!\left(\frac{u_{\mathrm c}x^2}{\sigma}\right)
  +O(e^{-c/\sigma^2}).$$ Here $\Phi$ is the standard normal distribution function. Consequently $1\le M_\sigma\le2+o(1)$, $\operatorname{var}M_\sigma=O(1)$, and, because the regular part of $\mathcal B$ is bounded near $x=0$, $$\label{eq:normalizer-weak-bound}
 \|(M_\sigma-\mathrm I)g\|_{L^1}
 \le C\sqrt\sigma\,\|g\|_{\mathcal B},
 \qquad
 \|M_\sigma g\|_{\mathcal B}
 \le C\|g\|_{\mathcal B}.$$ Indeed, outside $|x|=O(\sqrt\sigma)$ the first difference has a Gaussian tail in $x^2/\sigma$. The tower proof of the uniform Lasota--Yorke estimate uses only critical nonrecurrence and derivative growth; topological mixing is used later only to remove nontrivial peripheral roots [@BaladiViana1996]. Inserting [\[eq:normalizer-weak-bound\]](#eq:normalizer-weak-bound){reference-type="eqref" reference="eq:normalizer-weak-bound"} leaves that proof unchanged. The compact-support estimates extend to the Gaussian kernel by applying their variation bounds on dyadic tail shells and summing the exponentially decaying shell masses. Thus, for some $A,B<\infty$ and $\vartheta<1$, uniformly for small $\sigma$, $$\label{eq:strong-weak-estimates}
 \|\mathcal P_\sigma^n g\|_{\mathcal B}
 \le A\vartheta^n\|g\|_{\mathcal B}+B\|g\|_{L^1},
 \qquad
 \|\mathcal P_\sigma-\mathcal P_0\|_{\mathcal B\to L^1}=o(1).$$ These are precisely the strong/weak hypotheses of the Keller--Liverani theorem [@KellerLiverani1999]. Notice that the order-one limit of $M_\sigma$ at $x=0$ is weakly small but cannot be discarded in the boundary layer calculation below.

[\[prop:spectral-stability\]]{#prop:spectral-stability label="prop:spectral-stability"} There exist $\sigma_0>0$ and $\epsilon>0$ such that, for $0<\sigma<\sigma_0$, the spectrum of $\mathcal K_\sigma$ in $|z+1|<\epsilon$ consists of one simple real eigenvalue $\lambda_-(\sigma)$. Moreover $$\label{eq:lambda-convergence}
 \lambda_-(\sigma)\longrightarrow-1.$$ There is a real signed eigenmeasure $g_\sigma(x)\,dx$ of $\mathcal P_\sigma$, normalized as below, which converges in $L^1$ to the deterministic signed component density and locally uniformly away from the postcritical set.

On the tower/spike space, $-1$ is isolated and simple because the square map is mixing on each component. The analytic circle realization and its validated reduced-sector gap provide, for this parameter, an explicit isolation of the component spectrum [@WangValidatedGap2026]. The uniform Lasota--Yorke inequality and weak convergence in [\[eq:strong-weak-estimates\]](#eq:strong-weak-estimates){reference-type="eqref" reference="eq:strong-weak-estimates"}, together with the compact strong-to-weak embedding, give stability of its rank-one spectral projector. A simple eigenvalue of a real operator remains real as long as it remains isolated: otherwise its complex conjugate would be a second eigenvalue in the same disk. Applying the convergent projector to $g_0$ and fixing the pairing normalization below gives $g_\sigma\to g_0$ in $L^1$. On compact sets avoiding the finite postcritical set, all relevant inverse branches have derivative bounded away from zero. The local transfer equation then upgrades the regular part to uniform convergence; in particular, for some $\delta>0$, $$\label{eq:central-uniform-convergence}
 \sup_{0\le x\le\delta}|g_\sigma(x)-\rho_D(x)|\longrightarrow0.$$

Near a postcritical spike, the same tower bound gives, after reducing $\delta$ if necessary, $$\label{eq:spike-majorant}
 |g_\sigma(r+\sigma\xi)|
 \le C\sigma^{-1/2}(1+|\xi|)^{-1/2},
 \qquad |\xi|\le\delta/\sigma.$$ This estimate and [\[eq:central-uniform-convergence\]](#eq:central-uniform-convergence){reference-type="eqref" reference="eq:central-uniform-convergence"} are the two local consequences used below.

# The deterministic central density {#sec:density}

Let $$\label{eq:central-square}
 S=f^2|_{[-r,r]}.$$ This is a mixing full-branch map on the central component. Its cosine lift $\pi(\theta)=-r\cos\theta$ is an analytic expanding circle map. Let $v(x)$ be the even analytic invariant density in interval coordinates, normalized by $$\label{eq:v-normalization}
 \frac1{2\pi}\int_0^{2\pi}v(-r\cos\theta)\,d\theta=1.$$ The exact Wiener--Taylor construction of the preceding two papers gives $\mathcal T_1v=v$ and proves that this Perron eigenvalue is simple [@WangPostcritical2026; @WangValidatedGap2026].

Pushing normalized circle measure through the two-sheeted cover gives the central-component probability density $$\label{eq:rho-D}
 \rho_D(x)=\frac{v(x)}{\pi\sqrt{r^2-x^2}},
 \qquad -r<x<r.$$ It is even, integrates to one, is analytic at the critical point $x=0$, and has the expected square-root endpoint spikes. Define $$\label{eq:rho-c}
 \rho_c:=\rho_D(0)=\frac{v(0)}{\pi r}>0.$$

The Taylor implementation solves the normalized Perron equation at degrees $80,120,160$ and obtains the identical displayed values $$\label{eq:rho-c-numerical}
 v(0)=0.961019061704572\ldots,
 \qquad
 \rho_c=0.562641254486572\ldots.$$ These decimals are used only to evaluate the final integral; the theorem uses the exact quantity in [\[eq:rho-c\]](#eq:rho-c){reference-type="eqref" reference="eq:rho-c"}.

For later normalization, the zero-noise signed parity density on the folded space is $$\label{eq:signed-zero-density}
 g_0(x)=
 \begin{cases}
  \rho_D(x),&x\in B,\\
  -\frac12\rho_C(x),&x\in C,
 \end{cases}$$ where $\rho_C=f_*\rho_D$ is the normalized density on the outer component. Evenness of $\rho_D$ and normalization of $\rho_C$ give $$\label{eq:folded-masses}
 \int_0^r\rho_D(x)\,dx=\frac12,
 \qquad
 \int_r^1\rho_C(x)\,dx=1.$$ Thus both pieces in [\[eq:signed-zero-density\]](#eq:signed-zero-density){reference-type="eqref" reference="eq:signed-zero-density"} have total absolute mass $1/2$, and $$\label{eq:pair-normalization}
 \int_0^1h_0(x)g_0(x)\,dx=1.$$ We normalize $g_\sigma$ by continuation of [\[eq:pair-normalization\]](#eq:pair-normalization){reference-type="eqref" reference="eq:pair-normalization"}.

# The repelling-boundary eigenprofile {#sec:left-layer}

Let $Z$ be standard normal and define $$\label{eq:kappa-H}
 \kappa=\sqrt{\frac{\lambda^2-1}{2}},
 \qquad
 H(\xi)=-\operatorname{erf}(\kappa\xi).$$ Then $H(-\infty)=1$, $H(+\infty)=-1$, so it smooths the hard parity jump in the correct orientation.

[\[lem:exact-profile\]]{#lem:exact-profile label="lem:exact-profile"} For every $\xi\in\mathbb R$, $$\label{eq:dilation-equation}
 \mathbb E\,H(-\lambda\xi+Z)=-H(\xi).$$

The elementary Gaussian identity $$\label{eq:erf-identity}
 \mathbb E\,\operatorname{erf}(A+BZ)
 =\operatorname{erf}\!\left(\frac{A}{\sqrt{1+2B^2}}\right)$$ follows by differentiating both sides in $A$ and matching the value at zero. Since $1+2\kappa^2=\lambda^2$, substituting $A=-\kappa\lambda\xi$ and $B=\kappa$ proves [\[eq:dilation-equation\]](#eq:dilation-equation){reference-type="eqref" reference="eq:dilation-equation"}.

Use the global approximate parity observable $$\label{eq:h-sigma}
 \widehat h_\sigma(x)=H\!\left(\frac{x-r}{\sigma}\right).$$ Near $r$, write $x=r+\sigma\xi$. Since $$\label{eq:f-at-r}
 f(r+\sigma\xi)=r-\lambda\sigma\xi-u_{\mathrm c}\sigma^2\xi^2,$$ the full-Gaussian leading part of $\mathcal K_\sigma\widehat h_\sigma$ is exactly the left side of [\[eq:dilation-equation\]](#eq:dilation-equation){reference-type="eqref" reference="eq:dilation-equation"}. The row normalizer tends to one exponentially fast because $r$ is an interior target. Hence the apparent $O(1)$ smoothing at $r$ is locally balanced and contributes no leading eigenvalue defect.

The other preimage of the component boundary is the endpoint $x=1$. Put $x=1-\sigma\xi$, $\xi\ge0$. Then $$\label{eq:f-at-one}
 f(1-\sigma\xi)
 =-r+2u_{\mathrm c}\sigma\xi+O(\sigma^2\xi^2).$$ After folding, the target boundary coordinate is $-2u_{\mathrm c}\xi-Z+o(1)$. Applying [\[lem:exact-profile\]](#lem:exact-profile){reference-type="ref" reference="lem:exact-profile"} gives a second exact Gaussian identity.

[\[lem:endpoint-defect\]]{#lem:endpoint-defect label="lem:endpoint-defect"} Let $$\label{eq:a-definition}
 a=\frac{2u_{\mathrm c}\kappa}{\lambda}.$$ For every fixed $\xi\ge0$, $$\label{eq:endpoint-defect}
 (\mathcal K_\sigma\widehat h_\sigma+\widehat h_\sigma)
 (1-\sigma\xi)
 \longrightarrow-\operatorname{erfc}(a\xi).$$ If $D_\sigma=\mathcal K_\sigma\widehat h_\sigma+\widehat h_\sigma$, there are $\delta,C,c>0$ such that $$\begin{aligned}
 |D_\sigma(r+\sigma\xi)|
 &\le C\sigma(1+\xi^2)e^{-c\xi^2}+Ce^{-c/\sigma^2},
 && |\xi|\le\delta/\sigma,
 \label{eq:r-defect-majorant}\\
 |D_\sigma(1-\sigma\xi)|
 &\le Ce^{-c\xi^2}+Ce^{-c/\sigma^2},
 && 0\le\xi\le\delta/\sigma.
 \label{eq:one-defect-majorant}\end{aligned}$$ Outside these two fixed $\delta$-neighborhoods, $D_\sigma=O(e^{-c/\sigma^2})$.

By [\[eq:f-at-one\]](#eq:f-at-one){reference-type="eqref" reference="eq:f-at-one"}, $$(\mathcal K_\sigma\widehat h_\sigma)(1-\sigma\xi)
 \longrightarrow
 \mathbb E H(-2u_{\mathrm c}\xi-Z)
 =\operatorname{erf}\!\left(\frac{2u_{\mathrm c}\kappa}{\lambda}\xi\right).$$ Meanwhile $\widehat h_\sigma(1-\sigma\xi)\to-1$. Their sum is $-\operatorname{erfc}(a\xi)$. The remaining estimates follow from Gaussian tails and the Taylor remainders in [\[eq:f-at-r\]](#eq:f-at-r){reference-type="eqref" reference="eq:f-at-r"} and [\[eq:f-at-one\]](#eq:f-at-one){reference-type="eqref" reference="eq:f-at-one"}. More explicitly, convolution with $H'$ turns the quadratic displacement $u_{\mathrm c}\sigma\xi^2$ in the rescaled $r$-coordinate into the first bound in [\[eq:r-defect-majorant\]](#eq:r-defect-majorant){reference-type="eqref" reference="eq:r-defect-majorant"}; the convolved derivative has Gaussian decay in $\xi$. At the endpoint and on the complement, the distance of the image from the parity boundary gives [\[eq:one-defect-majorant\]](#eq:one-defect-majorant){reference-type="eqref" reference="eq:one-defect-majorant"} and the stated off-layer estimate.

Numerically, $$\label{eq:profile-constants}
 \kappa=0.953312391063827\ldots,
 \qquad
 a=1.753414854465239\ldots.$$

# The critical-value endpoint density {#sec:right-layer}

The defect in [\[lem:endpoint-defect\]](#lem:endpoint-defect){reference-type="ref" reference="lem:endpoint-defect"} must be paired with the signed right eigenmeasure near $x=1$. That density cannot be replaced by its formal zero-noise spike at the scale $1-x=O(\sigma)$, because the critical source and the truncation normalizer are resolved on exactly the same scale.

Let $\phi(t)=(2\pi)^{-1/2}e^{-t^2/2}$ and let $\Phi$ be its distribution function. Set $$\label{eq:R-profile}
 R(\xi)=\rho_c\int_0^\infty
 \frac{\phi(u_{\mathrm c}q^2-\xi)}{\Phi(u_{\mathrm c}q^2)}\,dq,
 \qquad \xi\ge0.$$

[\[lem:endpoint-density\]]{#lem:endpoint-density label="lem:endpoint-density"} For each compact interval of $\xi\ge0$, $$\label{eq:endpoint-density-limit}
 -\sqrt\sigma\,g_\sigma(1-\sigma\xi)
 \longrightarrow R(\xi)$$ locally uniformly. Moreover there is an integrable majorant after multiplication by the endpoint defect: for some $\delta,C>0$, $$\label{eq:endpoint-density-majorant}
 \sqrt\sigma\,|g_\sigma(1-\sigma\xi)|
 \le C(1+\xi)^{-1/2},
 \qquad 0\le\xi\le\delta/\sigma.$$ In addition, $$\label{eq:R-tail}
 R(\xi)\sim\frac{\rho_c}{2\sqrt{u_{\mathrm c}\xi}}
 \qquad(\xi\to\infty).$$

The only deterministic sources that can reach $1-\sigma\xi$ lie at $x=O(\sqrt\sigma)$ in the central component. Write $x=\sqrt\sigma q$. Then $$\label{eq:critical-scaling}
 f(x)=1-u_{\mathrm c}\sigma q^2,
 \qquad
 Z_\sigma(x)=\Phi(u_{\mathrm c}q^2)+O(e^{-c/\sigma^2}).$$ At $y=1-\sigma\xi$, the transition density is therefore $$\label{eq:kernel-scaling}
 \frac1\sigma
 \frac{\phi(u_{\mathrm c}q^2-\xi)}{\Phi(u_{\mathrm c}q^2)}
 (1+o(1)).$$ More precisely, the folded eigenrelation gives $$\begin{aligned}
 -\sqrt\sigma\,g_\sigma(y)
  ={}&\frac{\sqrt\sigma}{-\lambda_-(\sigma)}
  \int_0^1\frac{g_\sigma(x)}{Z_\sigma(x)}
  \bigl\{\phi_\sigma(y-f(x))+\phi_\sigma(-y-f(x))\bigr\}\,dx.
 \label{eq:endpoint-eigenrelation}\end{aligned}$$ By [\[eq:central-uniform-convergence\]](#eq:central-uniform-convergence){reference-type="eqref" reference="eq:central-uniform-convergence"}, $g_\sigma(\sqrt\sigma q)\to\rho_D(0)=\rho_c$ uniformly on compact $q$-sets. The second Gaussian in [\[eq:endpoint-eigenrelation\]](#eq:endpoint-eigenrelation){reference-type="eqref" reference="eq:endpoint-eigenrelation"} and all sources outside a fixed central neighborhood are exponentially small. Using $dx=\sqrt\sigma\,dq$ in the first Gaussian, and $-\lambda_-(\sigma)\to1$, proves [\[eq:endpoint-density-limit\]](#eq:endpoint-density-limit){reference-type="eqref" reference="eq:endpoint-density-limit"}.

For the uniform bound, choose $\delta$ so that every source of $[1-\delta,1]$ belongs to the central neighborhood on which $g_\sigma$ is uniformly bounded, apart from exponentially unlikely Gaussian jumps. Split the $q$-integral at $q=2\sqrt{(1+\xi)/u_{\mathrm c}}$ and use Gaussian decay on the outer part; on the inner part $\Phi(u_{\mathrm c}q^2)\ge1/2$. The same change of variables as above gives [\[eq:endpoint-density-majorant\]](#eq:endpoint-density-majorant){reference-type="eqref" reference="eq:endpoint-density-majorant"}. Applied to $R$, it gives $R(\xi)\le C(1+\xi)^{-1/2}$. Finally, Laplace expansion about $q=\sqrt{\xi/u_{\mathrm c}}$ yields [\[eq:R-tail\]](#eq:R-tail){reference-type="eqref" reference="eq:R-tail"}. Together with [\[eq:one-defect-majorant\]](#eq:one-defect-majorant){reference-type="eqref" reference="eq:one-defect-majorant"}, the product needed below has an integrable majorant.

The denominator in [\[eq:R-profile\]](#eq:R-profile){reference-type="eqref" reference="eq:R-profile"} has a direct probabilistic meaning. At the critical scale, an untruncated Gaussian centered at $1-u_{\mathrm c}\sigma q^2$ remains inside the upper state boundary with probability $\Phi(u_{\mathrm c}q^2)$. The Markov kernel conditions on that event. Replacing the denominator by one changes the leading constant and is therefore not a harmless normalization simplification.

# Square-root splitting and parity lifetime {#sec:main-theorem}

The two layers now meet through a one-line spectral solvability identity. For the signed eigenmeasure $g_\sigma dx$, $$\begin{aligned}
 &(\lambda_-(\sigma)+1)
 \int_0^1\widehat h_\sigma(x)g_\sigma(x)\,dx
 \notag\\
 &\hspace{4em}=
 \int_0^1
 (\mathcal K_\sigma\widehat h_\sigma+\widehat h_\sigma)(x)
 g_\sigma(x)\,dx.
 \label{eq:solvability}\end{aligned}$$ The denominator on the left tends to one by [\[eq:pair-normalization\]](#eq:pair-normalization){reference-type="eqref" reference="eq:pair-normalization"}. The endpoint $x=1$ supplies the only $\sqrt\sigma$ contribution on the right.

[\[thm:square-root\]]{#thm:square-root label="thm:square-root"} As $\sigma\downarrow0$, $$\label{eq:main-law}
 \boxed{
  1+\lambda_-(\sigma)
  =C_*\sqrt\sigma+o(\sqrt\sigma),}$$ where $$\begin{aligned}
 C_*
 &=\int_0^\infty R(\xi)\operatorname{erfc}(a\xi)\,d\xi
 \label{eq:C-first}\\
 &=\rho_c\int_0^\infty\frac{dq}{\Phi(u_{\mathrm c}q^2)}
 \int_0^\infty
 \phi(u_{\mathrm c}q^2-\xi)\operatorname{erfc}(a\xi)\,d\xi.
 \label{eq:C-double}\end{aligned}$$ In particular $0<C_*<\infty$.

In [\[eq:solvability\]](#eq:solvability){reference-type="eqref" reference="eq:solvability"}, split the state interval into fixed $\delta$-neighborhoods of $r$ and $1$ and their complement. On the complement, the residual in [\[lem:endpoint-defect\]](#lem:endpoint-defect){reference-type="ref" reference="lem:endpoint-defect"} is exponentially small, while $\|g_\sigma\|_{L^1}$ is uniformly bounded. In the $r$-layer, put $x=r+\sigma\xi$. From [\[eq:r-defect-majorant\]](#eq:r-defect-majorant){reference-type="eqref" reference="eq:r-defect-majorant"} and [\[eq:spike-majorant\]](#eq:spike-majorant){reference-type="eqref" reference="eq:spike-majorant"}, $$\begin{aligned}
 \int_{|x-r|\le\delta}|D_\sigma(x)g_\sigma(x)|\,dx
 &\le C\sigma^{3/2}
 \int_{\mathbb R}(1+\xi^2)(1+|\xi|)^{-1/2}e^{-c\xi^2}\,d\xi
  +O(e^{-c/\sigma^2})\\
 &=O(\sigma^{3/2}).\end{aligned}$$ This also controls the rescaled tails that are invisible in a merely local boundary-layer expansion.

In the endpoint layer put $x=1-\sigma\xi$. By [\[lem:endpoint-defect,lem:endpoint-density\]](#lem:endpoint-defect,lem:endpoint-density){reference-type="ref" reference="lem:endpoint-defect,lem:endpoint-density"}, $$\begin{aligned}
 &(\mathcal K_\sigma\widehat h_\sigma+\widehat h_\sigma)(x)
 g_\sigma(x)\,dx\\
 &\qquad=
 \sqrt\sigma\,
 R(\xi)\operatorname{erfc}(a\xi)\,d\xi+o(\sqrt\sigma).\end{aligned}$$ The majorant in [\[lem:endpoint-density\]](#lem:endpoint-density){reference-type="ref" reference="lem:endpoint-density"} permits dominated convergence. This yields $C_*\sqrt\sigma+o(\sqrt\sigma)$ on the right of [\[eq:solvability\]](#eq:solvability){reference-type="eqref" reference="eq:solvability"}. Its left pairing tends to one. Positivity and finiteness follow immediately from [\[eq:C-double\]](#eq:C-double){reference-type="eqref" reference="eq:C-double"}.

Numerical Taylor solution of the exact component-density equation and nested quadrature give $$\label{eq:C-numerical}
 \boxed{C_*=0.105258535936908\ldots.}$$ The integral formula, not the displayed decimal, is the theorem.

[\[cor:not-two-thirds\]]{#cor:not-two-thirds label="cor:not-two-thirds"} The old scaling satisfies $$\label{eq:two-thirds-divergence}
 \frac{1+\lambda_-(\sigma)}{\sigma^{2/3}}
 =C_*\sigma^{-1/6}(1+o(1))\longrightarrow+\infty.$$ Thus no finite nonzero $2/3$-law constant exists.

[\[cor:lifetime\]]{#cor:lifetime label="cor:lifetime"} Let $$\label{eq:lifetime-definition}
 m_{\mathrm{par}}(\sigma)
 =-\frac1{\log|\lambda_-(\sigma)|}.$$ Then $$\label{eq:lifetime-law}
 m_{\mathrm{par}}(\sigma)
 \sim\frac1{C_*\sqrt\sigma}.$$ If $m=m(\sigma)$ has fixed parity and $m\sqrt\sigma\to t\in[0,\infty)$, then $$\label{eq:peripheral-crossover}
 \lambda_-(\sigma)^m
 \longrightarrow(-1)^m e^{-C_*t}.$$

Write $\lambda_-(\sigma)=-(1-C_*\sqrt\sigma+o(\sqrt\sigma))$ and expand the logarithm. Both conclusions follow.

The crossover concerns the isolated parity factor. A statement replacing the full trace by $1+\lambda_-^m$ additionally requires uniform control of all bulk resonances as $\sigma\to0$; that separate assertion is not used here.

# Sparse spectral and profile audit {#sec:numerics}

The numerical work has three purposes: extend the old noise window, test the two local profiles independently, and verify spatial resolution. It is not used to infer the exponent in [\[thm:square-root\]](#thm:square-root){reference-type="ref" reference="thm:square-root"}.

For midpoint nodes $x_i=(i+1/2)/d$ on $[0,1]$, the folded row weights are $$\label{eq:matrix-weights}
 K_{ij}\propto
 \exp\!\left[-\frac{(x_j-f(x_i))^2}{2\sigma^2}\right]
 +
 \exp\!\left[-\frac{(-x_j-f(x_i))^2}{2\sigma^2}\right].$$ Only destinations within eight standard deviations of $|f(x_i)|$ are stored; the rows are then normalized exactly. Keeping $d\sigma\simeq20.48$ makes the number of nonzeros linear in $d$. ARPACK resolves the largest-modulus eigenvalues. NumPy, SciPy, and Matplotlib are used for the implementation [@HarrisEtAl2020; @VirtanenEtAl2020; @Hunter2007].

## The exponent crossover

gives representative values. The row-sum error is at most $5.6\times10^{-16}$ throughout.

::: {#tab:spectrum}
                $\sigma$      $d$            $1+\lambda_-$   $(1+\lambda_-)/\sqrt\sigma$   $(1+\lambda_-)/\sigma^{2/3}$   local power
  ---------------------- -------- ------------------------ ----------------------------- ------------------------------ -------------
    $3\!\times\!10^{-2}$      683   $2.80506\times10^{-2}$                      0.161950                       0.290532           ---
    $1\!\times\!10^{-2}$     2048   $1.34466\times10^{-2}$                      0.134466                       0.289698       0.62787
    $5\!\times\!10^{-3}$     4096   $8.84596\times10^{-3}$                      0.125101                       0.302528       0.57272
    $2\!\times\!10^{-3}$    10240   $5.26120\times10^{-3}$                      0.117644                       0.331435       0.56022
    $1\!\times\!10^{-3}$    20480   $3.61072\times10^{-3}$                      0.114181                       0.361072       0.54465
    $5\!\times\!10^{-4}$    40960   $2.50024\times10^{-3}$                      0.111814                       0.396889       0.53022
    $2\!\times\!10^{-4}$   102400   $1.54905\times10^{-3}$                      0.109534                       0.452945       0.52248
    $1\!\times\!10^{-4}$   204800   $1.08316\times10^{-3}$                      0.108316                       0.502746       0.51613

  : Negative parity resonance across the extended noise window.
:::

A log--log fit on exactly the old five-point window $0.01\le\sigma\le0.03$ reproduces $$\label{eq:old-fit-reproduced}
 p_{\mathrm{old}}=0.6674161083,
 \qquad
 A_{\mathrm{old}}=0.2881504866.$$ On $10^{-4}\le\sigma\le0.002$, the fitted power is already $$\label{eq:new-fit}
 p_{\mathrm{new}}=0.52749\ldots,$$ and the final two-point local exponent is $0.51613$. More decisively, the $2/3$-scaled column grows monotonically while the square-root-scaled column moves toward [\[eq:C-numerical\]](#eq:C-numerical){reference-type="eqref" reference="eq:C-numerical"}.

![Square-root boundary-layer audit. Top left: the extended parity gap and the analytic square-root law; the dotted $2/3$ reference only follows the intermediate window. Top right: local exponents drift from the old fit toward $1/2$. Bottom left: the right matrix eigenvector collapses onto the exact error-function boundary profile. Bottom right: the left signed eigenvector density approaches the independently derived critical-value profile $R$.](<../../../../../zeta_mvp0/papers/RH-14-square-root-parity-boundary-layer/figures/square_root_parity_boundary_layer.pdf>){#fig:boundary-layer width="\\textwidth"}

## Resolution and profile checks

At $\sigma=0.001$, increasing $d\sigma$ from $10.24$ to $30.72$ changes the negative eigenvalue by only $6.40\times10^{-6}$, or $0.18\%$ of the parity gap. The value at $d\sigma=20.48$ differs from the finest one by $9.98\times10^{-7}$.

The lower panels of [1](#fig:boundary-layer){reference-type="ref" reference="fig:boundary-layer"} test the two ingredients of the proof separately at $\sigma=0.001$, $d=20480$. The observed parity observable differs from $H$ by at most about $3.7\%$ on $|\xi|\le4$. The endpoint signed density has an $8$--$10\%$ preasymptotic offset but follows the full shape of $R$, including its nonmonotone maximum. Neither profile is fitted to the matrix data: $\kappa$, $a$, $\rho_c$, and the row-normalization factor are fixed before diagonalization.

![The scaled gap $(1+\lambda_-)/\sqrt\sigma$ approaches the boundary-layer constant $C_*$. The horizontal value comes from [\[eq:C-double\]](#eq:C-double){reference-type="eqref" reference="eq:C-double"}, not from regression against the resonance data.](figures/square_root_constant_convergence.pdf){#fig:constant width="76%"}

## Reproducibility and numerical status

The sparse calculation at $\sigma=10^{-4}$ has $204800$ states and $6.77\times10^7$ nonzeros. The archived output contains all sixteen noise levels, five independent resolutions, both profile tables, software versions, and source hashes. The test suite checks the sparse/dense spectral match, the Taylor stability of $\rho_c$, the exact Gaussian eigenprofile identity, the nested integral for $C_*$, and a finite-noise parity resonance.

The quadrature and matrix eigenvalues are ordinary floating-point computations. They support the displayed decimals and figures but are not a computer-assisted proof. The theorem asserts an exact positive integral constant and the exponent $1/2$; neither assertion depends on a rounded eigenvalue or fitted slope.

# Discussion {#sec:discussion}

## Why the exponent is one half

The critical source scale is $x=O(\sqrt\sigma)$ because $1-f(x)=u_{\mathrm c}x^2$. It creates an endpoint density of height $\sigma^{-1/2}$ over a layer of width $\sigma$. The endpoint then maps to the parity boundary, where the error-function profile has an $O(1)$ solvability defect. Thus $$\label{eq:dimensional-balance}
 \underbrace{\sigma^{-1/2}}_{\text{critical density}}
 \times
 \underbrace{\sigma}_{\text{endpoint width}}
 \times
 \underbrace{1}_{\text{parity defect}}
 =\sqrt\sigma.$$ The exponent is therefore geometric, not a free regression parameter.

The repelling boundary $r$ is essential but does not itself generate the splitting. Its local Gaussian dilation problem is exactly solvable at eigenvalue $-1$. The gap appears because the second preimage $x=1$ ends at the state boundary and is fed by a quadratic critical point. This is why a one-layer leakage estimate misses both the constant and, over moderate noise, the apparent exponent.

## The corrected two-clock picture

The deterministic periodic-orbit localization method has the logarithmic ceiling $$\label{eq:log-clock}
 m_{\mathrm{loc}}(\sigma)
 \lesssim\frac{\log(1/\sigma)}{\log\lambda}$$ because some cycles approach the state boundary exponentially [@WangLongCycle2026]. The parity lifetime is now $$\label{eq:sqrt-clock}
 m_{\mathrm{par}}(\sigma)
 \sim C_*^{-1}\sigma^{-1/2}.$$ It remains parametrically longer than [\[eq:log-clock\]](#eq:log-clock){reference-type="eqref" reference="eq:log-clock"}, although shorter than the previously conjectured $\sigma^{-2/3}$ scale. At $\sigma=10^{-4}$, the resolved e-folding time is about $923$, while the leading formula gives $950$ and the logarithmic orbit ceiling is only about $17.8$.

This separation is constructive. It says that a simultaneous small-noise/long-cycle determinant cannot be obtained by extending isolated periodic Gaussian tubes to the parity lifetime. The correct intermediate description must first extract the factor $1-z\lambda_-(\sigma)$ and treat the two coupled boundary layers before attempting a bulk determinant limit.

# Conclusion

The noisy parity resonance at the quadratic band-merging parameter has a nonanalytic but explicit small-noise splitting. The component-boundary observable is an exact error function, the critical endpoint density is a normalized Gaussian--quadratic integral, and their solvability pairing gives $$1+\lambda_-(\sigma)
 =0.105258535936908\ldots\sqrt\sigma+o(\sqrt\sigma).$$ The formerly observed $2/3$ exponent is a genuine and reproducible intermediate-window fit, but it is not the asymptotic law.

This closes the stochastic parity question left by the long-cycle analysis: the negative resonance converges to $-1$, its lifetime scale is $\sigma^{-1/2}$, and the crossover profile is explicit. The next spectral gate is no longer an exponent fit. It is to determine whether the parity-extracted noisy bulk determinant has a target-independent scaling or scattering limit.

# Data and code availability {#data-and-code-availability .unnumbered}

The source, tests, sparse spectra, resolution audit, boundary profiles, figures, and machine-readable summary are archived with this paper [@WangBoundaryLayerCode2026].
