---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-47-logarithmic-peripheral-conditioning"
canonical_tex: "zeta_mvp0/papers/RH-47-logarithmic-peripheral-conditioning/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-47-logarithmic-peripheral-conditioning/logarithmic-peripheral-conditioning.pdf"
source_sha256: "6f5beb2001b1a6860651c05a791c733c3d7e4a1634dad3b6259799066bae0976"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Endpoint Spikes, Logarithmic Peripheral Conditioning, and Continuum-Anchored Small-Noise Deflation

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-47-logarithmic-peripheral-conditioning>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-47-logarithmic-peripheral-conditioning/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-47-logarithmic-peripheral-conditioning/logarithmic-peripheral-conditioning.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-47-logarithmic-peripheral-conditioning/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-47-logarithmic-peripheral-conditioning/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The fixed-noise Perron and negative-parity branches of the folded-Gaussian band-merging operator have validated intrinsic weighted Riesz kernels. The next question is whether their $L^2$ contour theory can remain uniformly conditioned as the noise width $\sigma$ tends to zero. It cannot.

  Let $\pi_\sigma$ be the stationary density and let $g_\sigma$ be the signed left density of the negative branch. We prove the mesoscopic endpoint law $$\sqrt t\,\pi_\sigma(1-t),
   \quad -\sqrt t\,g_\sigma(1-t)
   \longrightarrow
   c_R:=\frac{\rho_{\mathrm c}}{2\sqrt{u_{\mathrm c}}}
   =0.226423589260506\ldots$$ whenever $t\downarrow0$ and $\sigma/t\to0$. Together with the finite postcritical spike majorants, this gives $$\left\lVert\pi_\sigma\right\rVert_2,\ \left\lVert g_\sigma\right\rVert_2,\
   \left\lVert\mathcal P_{+,\sigma}\right\rVert_{\mathfrak S_2},\
   \left\lVert\mathcal P_{-,\sigma}\right\rVert_{\mathfrak S_2}
   =\Theta\!\left(\sqrt{\log(1/\sigma)}\right).$$ For every fixed-radius isolating circle, the contour resolvent is therefore at least of this order. Thus a uniform $O(1)$ $L^2$ resolvent theorem is impossible. This lower bound does not determine the reduced-resolvent upper.

  The same endpoint structure provides a bypass. Direct differentiation of the rank-two weighted kernel gives $$\left\lVert E_n\mathcal Q_{\mathrm{per},\sigma}E_n
         -\mathcal Q_{\mathrm{per},\sigma}\right\rVert_{\mathfrak S_2}
   =O(n^{-1}\sigma^{-3/2}),$$ where $E_n$ is orthogonal cell averaging. Hence the continuum-anchored bulk $$\widetilde B_{n,\sigma}
   =E_n\mathcal K_\sigma E_n-E_n\mathcal Q_{\mathrm{per},\sigma}E_n
   =E_n\mathcal B_\sigma E_n$$ satisfies $$\left\lVert\widetilde B_{n,\sigma}^2-\mathcal B_\sigma^2\right\rVert_{\mathfrak S_1}
   =O(n^{-1}\sigma^{-2})+O(n^{-2}\sigma^{-3}).$$ Thus $n\sigma^2\to\infty$ still suffices. The remaining spectral gate is the intrinsic identification defect between the finite matrix's own weighted Riesz term and the compression of the continuum term. A $204800$-dimensional floating audit supports the logarithmic law but is not part of the proof. No arithmetic trace formula, Hilbert--Pólya operator, or Riemann-hypothesis claim is made.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Endpoint Spikes, Logarithmic Peripheral Conditioning,\
  and Continuum-Anchored Small-Noise Deflation
```

## Markdown 正文

**Keywords:** small noise; Riesz projection; endpoint spike; resolvent conditioning; Hilbert--Schmidt operator; Galerkin deflation.

**MSC 2020:** 47A10; 47B10; 37M25; 37C30; 65R20.

# Introduction

For a fixed positive Gaussian width, the Perron and negative-parity eigenvalues of the folded quadratic Markov operator can be isolated by explicit Euclidean contours. Their weighted Riesz terms are gauge-free, rank one, and have smooth Hilbert--Schmidt kernels [@WangRieszBridge2026; @WangEuclideanContour2026; @WangRankTwo2026]. Subtracting them gives the intrinsic bulk $$\mathcal B_\sigma
 =\mathcal K_\sigma-\mathcal Q_{+,\sigma}-\mathcal Q_{-,\sigma}.
 \label{eq:bulk}$$ At $\sigma=10^{-2}$, full and adaptive discretizations converge to this bulk in Hilbert--Schmidt norm, and their squares converge in trace norm.

The small-noise problem separates spatial resolution from spectral conditioning. The raw Gaussian kernel obeys $$\left\lVert\mathcal K_\sigma\right\rVert_{\mathfrak S_2}=O(\sigma^{-1/2}),
 \qquad
 \left\lVert E_n\mathcal K_\sigma E_n-\mathcal K_\sigma\right\rVert_{\mathfrak S_2}
 =O(n^{-1}\sigma^{-3/2}).
 \label{eq:raw-mesh}$$ Consequently $n\sigma^2\to\infty$ is sufficient for the raw two-step trace-ideal limit [@WangSmallNoiseMesh2026]. Extending that theorem to the intrinsic bulk was left under a uniform peripheral transport condition. The coarsest proposed route assumed that the continuum and discrete contour resolvents were $O(\sigma^{-\beta})$ and paid for two resolvents in the first resolvent identity.

The present paper shows that interpreting $\beta=0$ as a uniform $O(1)$ $L^2$ contour is already excluded by the invariant density. The deterministic Misiurewicz density has one-sided square-root spikes. Gaussian smoothing cuts each spike off at distance $O(\sigma)$, and the squared density accumulates a logarithm between $\sigma$ and a fixed macroscopic scale. The Riesz projection itself therefore becomes ill-conditioned in $L^2$, even though its eigenvalue remains isolated in the natural tower/spike space.

This is not a contradiction. Keller--Liverani stability is a two-norm statement on a strong dynamical space and a weak $L^1$ space [@KellerLiverani1999]. The $L^2$ norm sees the increasingly sharp postcritical density spikes. Spectral isolation and Hilbert-space conditioning are different questions.

The logarithmic obstruction can nevertheless be bypassed for the spatial part of the problem. Instead of comparing two Riesz integrals with two large resolvents, we differentiate the already identified rank-one kernels. Their target derivatives have the same $\sigma^{-3/2}$ scale as the raw Gaussian kernel. Orthogonal cell averaging then preserves the $p>2$ two-step mesh law for the continuum-anchored bulk.

The outcome is a sharper map of the remaining maze:

1.  fixed-geometry $O(1)$ $L^2$ resolvents are impossible;

2.  peripheral kernel size grows only logarithmically, hence more slowly than every negative power of $\sigma$;

3.  spatial compression of the continuum peripheral kernel is controlled at the raw Markov exponent $n^{-1}\sigma^{-3/2}$;

4.  the unresolved quantity is only the identification of the actual finite-matrix Riesz term with that compressed continuum kernel.

# Operator and peripheral factors {#sec:operator}

Let $$f(x)=1-u_{\mathrm c}x^2,
 \qquad
 u_{\mathrm c}=1.543689012692076\ldots,
 \label{eq:map}$$ where $u_{\mathrm c}$ is the first band-merging parameter. On the folded state space $I=[0,1]$, put $$k_\sigma(x,y)
 =\frac{\phi_\sigma(y-f(x))+\phi_\sigma(-y-f(x))}
 {Z_\sigma(x)},
 \quad
 Z_\sigma(x)=\int_0^1
 \{\phi_\sigma(y-f(x))+\phi_\sigma(-y-f(x))\}\,dy,
 \label{eq:kernel}$$ where $\phi_\sigma(s)=(2\pi\sigma^2)^{-1/2}e^{-s^2/(2\sigma^2)}$. The Markov operator on observables is $$(\mathcal K_\sigma v)(x)=\int_0^1k_\sigma(x,y)v(y)\,dy.
 \label{eq:operator}$$ It is compact and strongly positive for every $\sigma>0$.

Let $\pi_\sigma$ be the stationary density, $$\mathcal K_\sigma^*\pi_\sigma=\pi_\sigma,
 \qquad
 \int_0^1\pi_\sigma=1.
 \label{eq:stationary}$$ The small-noise parity theorem supplies a simple real eigenvalue $\lambda_-(\sigma)\to-1$, a right observable $h_\sigma$, and a signed left density $g_\sigma$ such that $$\mathcal K_\sigma h_\sigma=\lambda_-(\sigma)h_\sigma,
 \quad
 \mathcal K_\sigma^*g_\sigma=\lambda_-(\sigma)g_\sigma,
 \quad
 \int_0^1h_\sigma g_\sigma=1.
 \label{eq:parity-factors}$$ The normalization is chosen so that $h_\sigma$ tends to $+1$ on the central component and to $-1$ on the outer component. The signed density tends in $L^1$ to the deterministic signed component density [@WangBoundaryLayer2026].

The Riesz projections and weighted terms have exact kernels $$\begin{aligned}
 p_{+,\sigma}(x,y)&=\pi_\sigma(y),
 &q_{+,\sigma}(x,y)&=\pi_\sigma(y),
 \label{eq:perron-kernel}\\
 p_{-,\sigma}(x,y)&=h_\sigma(x)g_\sigma(y),
 &q_{-,\sigma}(x,y)&=\lambda_-(\sigma)h_\sigma(x)g_\sigma(y).
 \label{eq:parity-kernel}\end{aligned}$$ Their sum is denoted $$\mathcal Q_{\mathrm{per},\sigma}=\mathcal Q_{+,\sigma}+\mathcal Q_{-,\sigma}.
 \label{eq:qper}$$

The deterministic central density has the form $$\rho_D(x)=\frac{v(x)}{\pi\sqrt{r^2-x^2}},
 \qquad r=u_{\mathrm c}-1,
 \label{eq:central-density}$$ where $v$ is positive and analytic. Its value at the critical point is $$\rho_{\mathrm c}=\rho_D(0)=0.562641254486572\ldots.
 \label{eq:rho-c}$$

# The mesoscopic endpoint law {#sec:mesoscopic}

The preceding boundary-layer theorem resolved the microscopic scale $1-y=O(\sigma)$. For fixed $\xi\ge0$ it gives $$\sqrt\sigma\,\pi_\sigma(1-\sigma\xi)\longrightarrow R(\xi),
 \qquad
 -\sqrt\sigma\,g_\sigma(1-\sigma\xi)\longrightarrow R(\xi),
 \label{eq:microscopic-profile}$$ where the stationary statement follows by the same positive eigenrelation, and $$R(\xi)=\rho_{\mathrm c}\int_0^\infty
 \frac{\phi(u_{\mathrm c}q^2-\xi)}{\Phi(u_{\mathrm c}q^2)}\,dq,
 \qquad
 R(\xi)\sim\frac{\rho_{\mathrm c}}{2\sqrt{u_{\mathrm c}\xi}}.
 \label{eq:R-profile}$$ The next theorem makes the overlap with the deterministic spike uniform.

[\[thm:mesoscopic\]]{#thm:mesoscopic label="thm:mesoscopic"} Let $t=t(\sigma)$ satisfy $$t\longrightarrow0,
 \qquad
 \frac{\sigma}{t}\longrightarrow0.
 \label{eq:mesoscopic-regime}$$ Then $$\sqrt t\,\pi_\sigma(1-t)\longrightarrow c_R,
 \qquad
 -\sqrt t\,g_\sigma(1-t)\longrightarrow c_R,
 \qquad
 c_R=\frac{\rho_{\mathrm c}}{2\sqrt u_{\mathrm c}}.
 \label{eq:mesoscopic-law}$$ The convergence is uniform on every overlap window $$\sigma^a\le t\le\delta,
 \qquad 0<a<1,
 \label{eq:overlap-window}$$ after first taking $\sigma\downarrow0$ and then $\delta\downarrow0$.

Put $y=1-t$. The only sources that reach $y$ without an exponentially unlikely jump lie near the positive critical preimage $$x_t=\sqrt{t/u_{\mathrm c}}.
 \label{eq:critical-preimage}$$ Since $t/\sigma\to\infty$, this source is many Gaussian widths from the conditioned target boundary. Hence $Z_\sigma(x)=1+o(1)$ uniformly on the relevant source window. Write $$x=x_t+\frac{\sigma s}{2\sqrt{u_{\mathrm c}t}}.
 \label{eq:source-scaling}$$ Then $$\frac{u_{\mathrm c}x^2-t}{\sigma}=s+o(1),
 \qquad
 dx=\frac{\sigma}{2\sqrt{u_{\mathrm c}t}}\,ds.
 \label{eq:source-jacobian}$$ Stochastic stability and regularity on the central component give $\pi_\sigma(x)=\rho_{\mathrm c}+o(1)$ uniformly on this window. Gaussian tails permit restriction to bounded $s$ before sending the bound to infinity. The first term in [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"} therefore gives $$\pi_\sigma(1-t)
 =\frac{\rho_{\mathrm c}+o(1)}{2\sqrt{u_{\mathrm c}t}}\int_\mathbb R\phi(s)\,ds
 =\frac{\rho_{\mathrm c}+o(1)}{2\sqrt{u_{\mathrm c}t}}.
 \label{eq:stationary-laplace}$$ The folded second Gaussian and all other sources are exponentially small.

For the signed density, $$\lambda_-(\sigma)g_\sigma(y)
 =\int_0^1g_\sigma(x)k_\sigma(x,y)\,dx.
 \label{eq:g-eigenrelation}$$ On the central source window, $g_\sigma(x)=\rho_{\mathrm c}+o(1)$, while $\lambda_-(\sigma)\to-1$. Repeating the same calculation proves the second limit with the negative sign.

For $\sigma^a\le t\le\delta$, the relative Taylor error in [\[eq:source-jacobian\]](#eq:source-jacobian){reference-type="eqref" reference="eq:source-jacobian"} is $O(\sigma/t)$, hence uniformly small. The central source tends uniformly to zero as $\delta\downarrow0$, and Gaussian tail bounds remain uniform. This proves the overlap statement.

Numerically, $$c_R=0.22642358926050635\ldots,
 \qquad
 c_R^2=0.05126764177361048\ldots.
 \label{eq:cR-numerical}$$ The second number is the endpoint contribution per unit logarithmic scale to the squared $L^2$ norm.

# Logarithmic Riesz conditioning {#sec:conditioning}

The tower/spike estimates for a postcritically finite Misiurewicz map give a finite collection of local bounds $$|\pi_\sigma(s+\sigma\xi)|
 +|g_\sigma(s+\sigma\xi)|
 \le C\sigma^{-1/2}(1+|\xi|)^{-1/2}
 \label{eq:spike-majorant}$$ near every one-sided square-root spike $s$, and a uniform bound on their complement [@Misiurewicz1981; @KellerNowicki1992; @Baladi2000; @WangBoundaryLayer2026]. Squaring and integrating gives an upper logarithm. The endpoint matching theorem gives the lower logarithm.

[\[thm:left-log\]]{#thm:left-log label="thm:left-log"} As $\sigma\downarrow0$, $$\left\lVert\pi_\sigma\right\rVert_{L^2}^2=\Theta(\log(1/\sigma)),
 \qquad
 \left\lVert g_\sigma\right\rVert_{L^2}^2=\Theta(\log(1/\sigma)).
 \label{eq:left-log}$$ Moreover the endpoint alone satisfies $$\liminf_{\sigma\downarrow0}
 \frac{\left\lVert\pi_\sigma\right\rVert_{L^2}^2}{\log(1/\sigma)}
 \ge c_R^2,
 \qquad
 \liminf_{\sigma\downarrow0}
 \frac{\left\lVert g_\sigma\right\rVert_{L^2}^2}{\log(1/\sigma)}
 \ge c_R^2.
 \label{eq:endpoint-liminf}$$

Integrating [\[eq:spike-majorant\]](#eq:spike-majorant){reference-type="eqref" reference="eq:spike-majorant"} over the finitely many spike neighborhoods yields $$\left\lVert\pi_\sigma\right\rVert_2^2+\left\lVert g_\sigma\right\rVert_2^2
 \le C\log(1/\sigma).
 \label{eq:log-upper}$$ For the lower bound, fix $0<a<1$. On $\sigma^a\le t\le\delta$, [\[thm:mesoscopic\]](#thm:mesoscopic){reference-type="ref" reference="thm:mesoscopic"} gives, after shrinking $\delta$, $$\pi_\sigma(1-t)^2,\ g_\sigma(1-t)^2
 \ge(c_R-o(1))^2t^{-1}.$$ Its integral is $$a c_R^2\log(1/\sigma)+o(\log(1/\sigma)).$$ Letting $a\uparrow1$ proves [\[eq:endpoint-liminf\]](#eq:endpoint-liminf){reference-type="eqref" reference="eq:endpoint-liminf"} and the lower half of [\[eq:left-log\]](#eq:left-log){reference-type="eqref" reference="eq:left-log"}.

The right parity observable satisfies $$0<c\le\left\lVert h_\sigma\right\rVert_{L^2}\le
 \left\lVert h_\sigma\right\rVert_{L^\infty}\le C.
 \label{eq:h-bounds}$$ Indeed, spectral stability gives convergence to the component-sign observable away from its $O(\sigma)$ transition layer; the exact error-function profile controls that layer [@WangBoundaryLayer2026].

[\[cor:projector-log\]]{#cor:projector-log label="cor:projector-log"} The simple Riesz projections and weighted terms satisfy $$\begin{aligned}
 \left\lVert\mathcal P_{+,\sigma}\right\rVert_{\mathfrak S_2}
 &=\left\lVert\pi_\sigma\right\rVert_2
 =\Theta(\sqrt{\log(1/\sigma)}),
 \label{eq:perron-projector-log}\\
 \left\lVert\mathcal P_{-,\sigma}\right\rVert_{\mathfrak S_2}
 &=\left\lVert h_\sigma\right\rVert_2\left\lVert g_\sigma\right\rVert_2
 =\Theta(\sqrt{\log(1/\sigma)}),
 \label{eq:parity-projector-log}\\
 \left\lVert\mathcal Q_{\mathrm{per},\sigma}\right\rVert_{\mathfrak S_2}
 &=O(\sqrt{\log(1/\sigma)}).
 \label{eq:qper-log}\end{aligned}$$ Thus the peripheral size has regular-variation index zero: it is $O(\sigma^{-\epsilon})$ for every $\epsilon>0$, but it is not $O(1)$.

Equations [\[eq:perron-kernel\]](#eq:perron-kernel){reference-type="eqref" reference="eq:perron-kernel"}--[\[eq:parity-kernel\]](#eq:parity-kernel){reference-type="eqref" reference="eq:parity-kernel"} are rank-one kernels, so their Hilbert--Schmidt norms factor exactly. Since $|\lambda_-(\sigma)|\to1$, [\[thm:left-log\]](#thm:left-log){reference-type="ref" reference="thm:left-log"} and [\[eq:h-bounds\]](#eq:h-bounds){reference-type="eqref" reference="eq:h-bounds"} prove the first two statements. The third follows by the triangle inequality.

## The fixed-contour resolvent obstruction

Let $\Gamma$ be a circle of radius $r_\Gamma$ that isolates one peripheral branch for all sufficiently small $\sigma$. Such fixed geometry is compatible with strong/weak perturbation theory; the obstruction below concerns its $L^2$ norm, not its existence.

[\[thm:resolvent-lower\]]{#thm:resolvent-lower label="thm:resolvent-lower"} For either peripheral circle, $$\sup_{z\in\Gamma}\left\lVert(z-\mathcal K_\sigma)^{-1}\right\rVert_{L^2\to L^2}
 \ge
 \frac{1}{r_\Gamma}\left\lVert\mathcal P_{\pm,\sigma}\right\rVert_{L^2\to L^2}
 \ge c\sqrt{\log(1/\sigma)}.
 \label{eq:resolvent-lower}$$ In particular, no $O(1)$ $L^2$ contour-resolvent theorem is possible on fixed-radius circles.

The Riesz formula and the arclength of a circle give $$\left\lVert\mathcal P_{\pm,\sigma}\right\rVert
 \le r_\Gamma
 \sup_{z\in\Gamma}\left\lVert(z-\mathcal K_\sigma)^{-1}\right\rVert.
 \label{eq:riesz-circle}$$ For a rank-one operator, the operator and Hilbert--Schmidt norms agree. Apply [\[cor:projector-log\]](#cor:projector-log){reference-type="ref" reference="cor:projector-log"}.

[\[rem:reduced-resolvent\]]{#rem:reduced-resolvent label="rem:reduced-resolvent"} The lower bound [\[eq:resolvent-lower\]](#eq:resolvent-lower){reference-type="eqref" reference="eq:resolvent-lower"} comes entirely from the residue. It does not upper-bound the reduced resolvent on the complementary spectral subspace. Nonnormal pseudospectral growth may be larger [@GohbergKrein1969; @Kato1995]. Thus this paper disproves uniform $O(1)$ conditioning but does not identify a matching upper or a polynomial exponent $\beta$ for the complete resolvent.

# Direct peripheral-kernel resolution {#sec:kernel-resolution}

The resolvent obstruction does not force a worse spatial mesh exponent. The already isolated weighted term has a rank-two kernel whose derivatives can be estimated from the eigenrelations without differentiating a contour resolvent.

[\[lem:gaussian-derivatives\]]{#lem:gaussian-derivatives label="lem:gaussian-derivatives"} For sufficiently small $\sigma$, $$\begin{aligned}
 \sup_x\left\lVert\partial_y k_\sigma(x,\cdot)\right\rVert_{L^2_y}
 &\le C\sigma^{-3/2},
 \label{eq:target-row-derivative}\\
 \sup_x\int_0^1|\partial_x k_\sigma(x,y)|\,dy
 &\le C\sigma^{-1}.
 \label{eq:source-row-variation}\end{aligned}$$

For an unconditioned normalized Gaussian, the first derivative has $L^2$ scale $\sigma^{-3/2}$ and total-variation scale $\sigma^{-1}$. Folding adds two terms. Differentiating the row normalizer contributes the same scales. Near a conditioned endpoint, the normalizer is bounded below by a positive Gaussian half-mass in normalized coordinates; away from the endpoint it tends to one. Finally $f'$ is uniformly bounded. These are the normalized-kernel versions of the explicit Gaussian moment bounds in [@WangSmallNoiseMesh2026].

[\[prop:peripheral-derivatives\]]{#prop:peripheral-derivatives label="prop:peripheral-derivatives"} The left densities and right parity observable satisfy $$\begin{aligned}
 \left\lVert\pi_\sigma'\right\rVert_2+\left\lVert g_\sigma'\right\rVert_2
 &=O(\sigma^{-3/2}),
 \label{eq:left-derivatives}\\
 \left\lVert h_\sigma'\right\rVert_2&=O(\sigma^{-1}).
 \label{eq:right-derivative}\end{aligned}$$ Consequently the rank-two weighted kernel $q_{\mathrm{per},\sigma}$ obeys $$\begin{aligned}
 \left\lVert\partial_x q_{\mathrm{per},\sigma}\right\rVert_{L^2(I^2)}
 &=O\!\left(\sigma^{-1}\sqrt{\log(1/\sigma)}\right),
 \label{eq:q-source}\\
 \left\lVert\partial_y q_{\mathrm{per},\sigma}\right\rVert_{L^2(I^2)}
 &=O(\sigma^{-3/2}).
 \label{eq:q-target}\end{aligned}$$

Differentiate [\[eq:stationary\]](#eq:stationary){reference-type="eqref" reference="eq:stationary"} and the left equation in [\[eq:parity-factors\]](#eq:parity-factors){reference-type="eqref" reference="eq:parity-factors"}. Minkowski's inequality, [\[lem:gaussian-derivatives\]](#lem:gaussian-derivatives){reference-type="ref" reference="lem:gaussian-derivatives"}, $\left\lVert\pi_\sigma\right\rVert_1=1$, and the uniform $L^1$ bound for $g_\sigma$ give [\[eq:left-derivatives\]](#eq:left-derivatives){reference-type="eqref" reference="eq:left-derivatives"}. Differentiating the right equation in [\[eq:parity-factors\]](#eq:parity-factors){reference-type="eqref" reference="eq:parity-factors"}, using [\[eq:source-row-variation\]](#eq:source-row-variation){reference-type="eqref" reference="eq:source-row-variation"}, [\[eq:h-bounds\]](#eq:h-bounds){reference-type="eqref" reference="eq:h-bounds"}, and $|\lambda_-(\sigma)|\ge1/2$ gives [\[eq:right-derivative\]](#eq:right-derivative){reference-type="eqref" reference="eq:right-derivative"}.

Differentiating [\[eq:perron-kernel\]](#eq:perron-kernel){reference-type="eqref" reference="eq:perron-kernel"} and [\[eq:parity-kernel\]](#eq:parity-kernel){reference-type="eqref" reference="eq:parity-kernel"}, rank-one factorization gives $$\left\lVert\partial_xq_{-,\sigma}\right\rVert_2
 =|\lambda_-|\left\lVert h_\sigma'\right\rVert_2\left\lVert g_\sigma\right\rVert_2,
 \qquad
 \left\lVert\partial_yq_{-,\sigma}\right\rVert_2
 =|\lambda_-|\left\lVert h_\sigma\right\rVert_2\left\lVert g_\sigma'\right\rVert_2.$$ The Perron source derivative vanishes and its target derivative is $\pi_\sigma'$. Apply [\[thm:left-log\]](#thm:left-log){reference-type="ref" reference="thm:left-log"}.

Let $E_n$ denote orthogonal averaging on the $n$ equal cells of $I$. The tensor cell average of a kernel represents $E_nTE_n$.

[\[thm:peripheral-projection\]]{#thm:peripheral-projection label="thm:peripheral-projection"} The compressed continuum weighted term satisfies $$\boxed{
 \left\lVert E_n\mathcal Q_{\mathrm{per},\sigma}E_n-\mathcal Q_{\mathrm{per},\sigma}\right\rVert_{\mathfrak S_2}
 =O(n^{-1}\sigma^{-3/2}).}
 \label{eq:peripheral-projection}$$

The one-dimensional Poincaré--Wirtinger inequality on each cell, applied successively in the two variables, gives $$\left\lVert E_nTE_n-T\right\rVert_{\mathfrak S_2}
 \le\frac{1}{\pi n}
 \left(\left\lVert q_x\right\rVert_{L^2(I^2)}+\left\lVert q_y\right\rVert_{L^2(I^2)}\right).
 \label{eq:kernel-poincare}$$ Insert [\[eq:q-source\]](#eq:q-source){reference-type="eqref" reference="eq:q-source"}--[\[eq:q-target\]](#eq:q-target){reference-type="eqref" reference="eq:q-target"} and use $\sqrt{\log(1/\sigma)}=O(\sigma^{-1/2})$.

# Continuum-anchored bulk-square convergence {#sec:anchored}

Define the continuum intrinsic bulk by [\[eq:bulk\]](#eq:bulk){reference-type="eqref" reference="eq:bulk"} and its anchored Galerkin compression by $$\begin{aligned}
 \widetilde B_{n,\sigma}
 &:=E_n\mathcal K_\sigma E_n-E_n\mathcal Q_{\mathrm{per},\sigma}E_n
 \notag\\
 &=E_n\mathcal B_\sigma E_n.
 \label{eq:anchored-bulk}\end{aligned}$$ This is an exact algebraic identity. The term *anchored* emphasizes that the peripheral kernel comes from the continuum operator, not from a new diagonalization of the finite matrix.

[\[thm:anchored-mesh\]]{#thm:anchored-mesh label="thm:anchored-mesh"} Uniformly for sufficiently small $\sigma$, $$\begin{aligned}
 \left\lVert\mathcal B_\sigma\right\rVert_{\mathfrak S_2}&=O(\sigma^{-1/2}),
 \label{eq:bulk-size}\\
 \left\lVert\widetilde B_{n,\sigma}-\mathcal B_\sigma\right\rVert_{\mathfrak S_2}
 &=O(n^{-1}\sigma^{-3/2}),
 \label{eq:anchored-hs}\\
 \left\lVert\widetilde B_{n,\sigma}^2-\mathcal B_\sigma^2\right\rVert_{\mathfrak S_1}
 &=O(n^{-1}\sigma^{-2})+O(n^{-2}\sigma^{-3}).
 \label{eq:anchored-trace}\end{aligned}$$ In particular, $$n(\sigma)\sigma^2\longrightarrow\infty
 \label{eq:p-two-condition}$$ is sufficient for anchored bulk-square trace-norm convergence. For $n(\sigma)\asymp\sigma^{-p}$, every $p>2$ closes the theorem.

The raw Markov bounds [\[eq:raw-mesh\]](#eq:raw-mesh){reference-type="eqref" reference="eq:raw-mesh"} and [\[eq:qper-log\]](#eq:qper-log){reference-type="eqref" reference="eq:qper-log"} give $$\left\lVert\mathcal B_\sigma\right\rVert_{\mathfrak S_2}
 \le O(\sigma^{-1/2})+O(\sqrt{\log(1/\sigma)})
 =O(\sigma^{-1/2}).$$ Add the raw cell-average error in [\[eq:raw-mesh\]](#eq:raw-mesh){reference-type="eqref" reference="eq:raw-mesh"} to [\[thm:peripheral-projection\]](#thm:peripheral-projection){reference-type="ref" reference="thm:peripheral-projection"} to obtain [\[eq:anchored-hs\]](#eq:anchored-hs){reference-type="eqref" reference="eq:anchored-hs"}. Products of Hilbert--Schmidt operators are trace class, and $$\begin{aligned}
 \left\lVert A_n^2-A^2\right\rVert_{\mathfrak S_1}
 &\le\left\lVert A_n-A\right\rVert_{\mathfrak S_2}
       (\left\lVert A_n\right\rVert_{\mathfrak S_2}+\left\lVert A\right\rVert_{\mathfrak S_2})
 \notag\\
 &\le\varepsilon(2\left\lVert A\right\rVert_{\mathfrak S_2}+\varepsilon).
 \label{eq:hs-product}\end{aligned}$$ With $\varepsilon=O(n^{-1}\sigma^{-3/2})$, this is [\[eq:anchored-trace\]](#eq:anchored-trace){reference-type="eqref" reference="eq:anchored-trace"}. Condition [\[eq:p-two-condition\]](#eq:p-two-condition){reference-type="eqref" reference="eq:p-two-condition"} sends both terms to zero.

The logarithmic peripheral growth therefore does not alter the raw Markov power threshold. It is asymptotically smaller than the $\sigma^{-1/2}$ Hilbert--Schmidt size of the narrowing Gaussian kernel.

# The exact remaining identification defect {#sec:identification}

Let $$G_{n,\sigma}=E_n\mathcal K_\sigma E_n
 \label{eq:galerkin-markov}$$ on the cell space. When its two peripheral branches are intrinsically identified, its actual finite-dimensional bulk is $$B_{n,\sigma}^{\mathrm{int}}
 =G_{n,\sigma}-\mathcal Q_{\mathrm{per}}(G_{n,\sigma}).
 \label{eq:intrinsic-discrete-bulk}$$

[\[def:identification\]]{#def:identification label="def:identification"} Define $$\mathcal I_{n,\sigma}
 :=\mathcal Q_{\mathrm{per}}(G_{n,\sigma})
   -E_n\mathcal Q_{\mathrm{per}}(\mathcal K_\sigma)E_n.
 \label{eq:identification-defect}$$ Then $$B_{n,\sigma}^{\mathrm{int}}-\widetilde B_{n,\sigma}
 =-\mathcal I_{n,\sigma}.
 \label{eq:identification-identity}$$

[\[cor:intrinsic-closure\]]{#cor:intrinsic-closure label="cor:intrinsic-closure"} If $$\left\lVert\mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
 =O(n^{-1}\sigma^{-3/2}),
 \label{eq:identification-target}$$ then [\[thm:anchored-mesh\]](#thm:anchored-mesh){reference-type="ref" reference="thm:anchored-mesh"} holds with $B_{n,\sigma}^{\mathrm{int}}$ in place of $\widetilde B_{n,\sigma}$.

Equation [\[eq:identification-identity\]](#eq:identification-identity){reference-type="eqref" reference="eq:identification-identity"} and the triangle inequality give the same Hilbert--Schmidt rate. Apply [\[eq:hs-product\]](#eq:hs-product){reference-type="eqref" reference="eq:hs-product"}.

This isolates the remaining problem more sharply than a global peripheral transport condition. The spatial compression $$E_n\mathcal Q_{\mathrm{per}}(\mathcal K_\sigma)E_n
 -\mathcal Q_{\mathrm{per}}(\mathcal K_\sigma)$$ is already controlled by [\[thm:peripheral-projection\]](#thm:peripheral-projection){reference-type="ref" reference="thm:peripheral-projection"}. Only the spectral identification of the finite matrix's own Riesz term remains. A proof should target a reduced resolvent or a Feshbach/Grushin complement around the two known factors. Paying for two complete $L^2$ resolvents is sufficient but, in view of [\[thm:resolvent-lower\]](#thm:resolvent-lower){reference-type="ref" reference="thm:resolvent-lower"}, structurally wasteful.

# Floating sparse audit {#sec:numerics}

The theorem is analytic. We nevertheless audit the predicted clocks on the same row-normalized eight-sigma sparse family used in the preceding small-noise studies. The dimension is chosen by $$n\sigma\simeq20.48,
 \label{eq:numerical-resolution}$$ and the calculation reaches $n=204800$ at $\sigma=10^{-4}$. Right and left eigenvectors are normalized as in [\[eq:parity-factors\]](#eq:parity-factors){reference-type="eqref" reference="eq:parity-factors"}. All low-rank Hilbert--Schmidt and singular values are evaluated from $2\times2$ Gram matrices; the full rank-two kernel is never formed.

::: {#tab:pilot}
            $\sigma$        $n$   $\left\lVert P_+\right\rVert_{\mathfrak S_2}$   $\left\lVert P_-\right\rVert_{\mathfrak S_2}$   $\left\lVert Q_{\rm per}\right\rVert_{\mathfrak S_2}$   Perron resolvent lower
  ------------------ ---------- ----------------------------------------------- ----------------------------------------------- ------------------------------------------------------- ------------------------
    $4\times10^{-3}$     $5120$                                       $1.15508$                                       $1.14811$                                               $1.63226$                $23.1016$
           $10^{-3}$    $20480$                                       $1.24273$                                       $1.21532$                                               $1.74451$                $24.8547$
    $2\times10^{-4}$   $102400$                                       $1.35334$                                       $1.31207$                                               $1.89259$                $27.0667$
           $10^{-4}$   $204800$                                       $1.40097$                                       $1.35583$                                               $1.95758$                $28.0194$

  : Floating peripheral-factor audit. The resolvent column is the algebraic lower formula $\left\lVert P_+\right\rVert/0.05$ applied to floating projector data; the data themselves are not validated enclosures.
:::

Over the six smallest noise levels, least-squares fits of squared norms against $\log(1/\sigma)$ give slopes $$0.17154\quad(P_+),
 \qquad
 0.14244\quad(P_-),
 \qquad
 0.31906\quad(Q_{\mathrm{per}}).
 \label{eq:fitted-slopes}$$ These slopes include all postcritical spikes and are not identified with the single-endpoint coefficient $c_R^2$. The median mesoscopic coefficients at $\sigma=10^{-4}$ are $$0.241782\quad(\pi_\sigma),
 \qquad
 0.245491\quad(-g_\sigma),
 \label{eq:observed-tail}$$ compared with $c_R=0.226424$. Their monotone drift is consistent with [\[thm:mesoscopic\]](#thm:mesoscopic){reference-type="ref" reference="thm:mesoscopic"}.

![Logarithmic peripheral conditioning and the anchored bypass. (a) Squared Perron, parity, and rank-two norms against $\log(1/\sigma)$, with floating linear fits. (b) Division by the logarithmic clock. (c) Mesoscopic endpoint coefficients approaching $c_R$. (d) Normalized anchored trace-error ledgers: $p=2$ is critical and every displayed $p>2$ decays. Panels (a)--(c) are floating diagnostics; panel (d) displays the proved exponents with unknown constants normalized to one.](<../../../../../zeta_mvp0/papers/RH-47-logarithmic-peripheral-conditioning/figures/logarithmic_peripheral_conditioning.pdf>){#fig:summary width="\\textwidth"}

The numerical data do not upper-bound a reduced resolvent and do not prove [\[eq:identification-target\]](#eq:identification-target){reference-type="eqref" reference="eq:identification-target"}. They test only the factor growth and endpoint mechanism already isolated analytically.

# What is closed and what remains {#sec:conclusion}

The small-noise contour gate has split into three distinct statements.

1.  **Spectral geometry.** The Perron and negative branches remain simple and isolated on the natural dynamical space. Their eigenvalue locations do not force a shrinking contour.

2.  **$L^2$ conditioning.** Fixed-radius $O(1)$ resolvents are impossible because the residues themselves grow like $\sqrt{\log(1/\sigma)}$.

3.  **Spatial resolution.** Direct rank-two kernel estimates bypass that obstruction and retain the $n\sigma^2\to\infty$ two-step law for continuum-anchored deflation.

The next positive gate is precisely [\[eq:identification-target\]](#eq:identification-target){reference-type="eqref" reference="eq:identification-target"}. A useful proof should separate the logarithmic residue from the reduced complement and transport the two known factors through a one-sided Feshbach/Grushin system. If that succeeds, the actual intrinsic finite bulk---not only its continuum-anchored compression---inherits the $p>2$ small-noise theorem.

None of the present results identifies a dynamical trace with primes or prime powers, constructs a self-adjoint operator, derives a $T\log T$ counting law, or locates a Riemann zero. The result is an endpoint, conditioning, and trace-ideal theorem for one explicit noisy transfer family.

# Data and code availability {#data-and-code-availability .unnumbered}

All source code, certificates, floating factor data, tests, figures, hashes, and the manuscript are available in <https://github.com/maris205/prime_dynamics_theory/tree/main/papers/RH-47-logarithmic-peripheral-conditioning>.
