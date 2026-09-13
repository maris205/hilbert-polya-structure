---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-18-branch-isolated-gaussian-return"
canonical_tex: "zeta_mvp0/papers/RH-18-branch-isolated-gaussian-return/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-18-branch-isolated-gaussian-return/branch-isolated-gaussian-return.pdf"
source_sha256: "395170c2c478d1656ba30a91da1aca174ec520a5880a09d8bcc415786063aa28"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Branch-Isolated Gaussian Return Blocks at a Quadratic Band-Merging Map: Riccati Packet Monodromy, Critical Closure, and the Bulk Spectral Edge

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-18-branch-isolated-gaussian-return>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-18-branch-isolated-gaussian-return/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-18-branch-isolated-gaussian-return/branch-isolated-gaussian-return.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-18-branch-isolated-gaussian-return/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-18-branch-isolated-gaussian-return/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At the first algebraic band-merging parameter of $f_u(x)=1-u x^2$, a parity-extracted Gaussian Markov operator has a growing small-noise resonance cloud. A preceding deterministic construction found the correct boundary cycle and exact roots-of-unity phases, but its raw inverse-Jacobian basis has condition number at least of order $\lambda^k$. Here we test the next operator-theoretic arrow: whether the actual noisy dynamics carries an adapted cyclic return block along that cycle.

  For the two-step map $S=f^2$, let $x_{k,j}$ be the ordered length-$k$ boundary cycle, $m_{k,j}=|S'(x_{k,j})|$, and $\beta_{k,j}^2=1+f'(f(x_{k,j}))^2$. We prove that the periodic Riccati system $$m_{k,j}^2t_{k,j}^2=t_{k,j+1}^2+\beta_{k,j}^2$$ has a unique positive solution. Peak-normalized Gaussian packets are then transported exactly by every affine tangent channel with coefficient $$c_{k,j}=\frac{t_{k,j+1}}
   {\sqrt{t_{k,j+1}^2+\beta_{k,j}^2}},
   \qquad
   \prod_{j=0}^{k-1}c_{k,j}=|(S^k)'(p_{2k})|^{-1}.$$ Thus Gaussian adaptation preserves the deterministic geometric-mean radius while removing its single exponentially large local weight. It does not make the problem uniformly conditioned: the canonical packet balance obeys $$\liminf_{k\to\infty}
   \frac{\log\operatorname{cond}_2(D_k^{\rm G})}{k\log\lambda}\ge\frac12.$$ At the half-logarithmic noise clock this leaves a $\sigma^{-1/4+o(1)}$ barrier.

  The final channel is genuinely non-affine. In the critical scaling $\delta_k/\sigma\to d$ and $x=x_{k,k-1}+\sqrt\sigma q$, we derive the locally uniform conditioned Gaussian--quadratic limit $$\Gamma_{d,t}(q)=
   \frac{t}{\sqrt{1+t^2}}e^{-B_d(q)^2/[2(1+t^2)]}
   \frac{\Phi\!\left(\frac{\sqrt{1+t^2}}{t}
   [A_d(q)+B_d(q)/(1+t^2)]\right)}{\Phi(A_d(q))},$$ where $A_d(q)=(\sqrt d-2u_{\mathrm c}q)^2$ and $B_d=d-A_d$. Its two symbolic preimages are separated, without a fitted cutoff, by the physical partition $b=u_{\mathrm c}^{-1/2}$.

  Time-labeled restrictions of the exact nonlinear Gaussian operator form a compact block-cyclic auxiliary operator. We prove that every nonzero return eigenvalue generates its complete roots-of-unity ring; positivity makes the principal return eigenvalue simple. Ordinary floating-point computations at seven noise levels show that the resulting branch-isolated principal ring locates the archived outer bulk radius to $5.64\times10^{-4}$ at $\sigma=10^{-4}$, and its return operator is numerically close to rank one. This is not yet a Feshbach theorem for the full Markov operator. Controlling excursions through the complementary space and the associated Schur self-energy remains the decisive missing estimate.
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
  **Branch-Isolated Gaussian Return Blocks**\
  **at a Quadratic Band-Merging Map:**\
  Riccati Packet Monodromy, Critical Closure, and the Bulk Spectral Edge
```

## Markdown 正文

**Keywords:** Gaussian transfer operator; Riccati equation; block-cyclic operator; critical boundary layer; Krein--Rutman theorem; Grushin problem; non-normal spectrum; quadratic map.

**MSC 2020:** 37E05; 37D25; 47A10; 47B65; 47H07; 60J05; 65P30.

# Introduction {#sec:introduction}

The small-noise spectral problem at the quadratic band-merging map has progressed through three logically distinct constructions. First, after the Perron and parity modes are extracted, the deterministic bulk determinant has a genuine local pole factor $$\label{eq:intro-pole}
 \widehat D_{0,\mathrm{bulk},2}(z)
 =\frac{\mathcal G(z)}{1-z^2/\lambda},
 \qquad \mathcal G(z)\ne0\quad (|z|<\lambda),$$ so a fixed finite set of noisy resonances cannot provide a locally uniform entire approximation through the pole [@WangBoundaryLayer2026; @WangBulkScattering2026]. Second, the endpoint Gaussian row family has intrinsic Hellinger and linear-kernel ranks $$\label{eq:intro-rank}
 N_\sigma=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),$$ without using a computed Markov eigenvalue [@WangEndpointRank2026]. Third, the boundary word $CA(CB)^{k-1}$ supplies an exact time-ordered cycle. Its deterministic inverse-Jacobian monodromy has the edge-deflated determinant $$\label{eq:intro-geometric}
 \Pi_{k-1}(\rho_kz^2)
 =1+\rho_kz^2+\cdots+(\rho_kz^2)^{k-1},
 \qquad
 \rho_k=|(S^k)'(p_{2k})|^{-1/k},$$ and hence the observed roots-of-unity phase grid [@WangTimeOrdered2026].

Those results do not yet identify a spectral block of the noisy operator. The deterministic cycle is strongly unbalanced: one critical-return weight is exponentially large, and the diagonal similarity to a constant cyclic shift costs at least $c\lambda^k$. At the rank scale [\[eq:intro-rank\]](#eq:intro-rank){reference-type="eqref" reference="eq:intro-rank"}, this is a $\sigma^{-1/2}$ obstruction in the raw Euclidean orbit basis. The natural next attempt is to let Gaussian smoothing choose the packet widths instead of imposing inverse-Jacobian amplitudes. That is the subject of this paper.

There are two separate issues. Along an ordinary affine noisy channel, a Gaussian observable remains Gaussian and its width is determined by a periodic Lyapunov--Riccati equation. At the closing edge of the boundary cycle, however, the source packet has physical width $O(\sqrt\sigma)$ and straddles the quadratic critical partition. Linearization is then invalid. The final return must retain both the quadratic map and the normalization caused by conditioning the state to $[-1,1]$ before folding.

## Main results and logical status {#main-results-and-logical-status .unnumbered}

The paper keeps analytic statements, exact auxiliary-block algebra, and floating-point evidence separate.

1.  **Periodic Gaussian packet theorem.** For every repelling boundary cycle, the affine two-step channels admit a unique positive periodic width vector. Their exact Gaussian channel coefficients lie in $(0,1)$ and telescope to the inverse cycle multiplier. Hence the adapted scalar cycle has exactly the same geometric-mean radius as the RH-17 deterministic monodromy.

2.  **A remaining quarter-power barrier.** The endpoint width converges to a positive constant, while the width at the critical source grows like $C_t\lambda^k$. At the midpoint of the cycle the width is subexponential. These facts imply $\operatorname{cond}_2(D_k^{\rm G})\ge\lambda^{k/2-o(k)}$. Numerically the exponent tends to $1/2$, but only the lower bound is asserted analytically.

3.  **Conditioned critical closure.** The last two-step pullback has the explicit Gaussian--quadratic limit $\Gamma_{d,t}$. It contains a non-removable Gaussian distribution-function ratio caused by state conditioning. The profile is symmetric about the limiting coordinate of $b=u_{\mathrm c}^{-1/2}$; retaining $x<b$ selects the boundary word's branch.

4.  **Exact root-ring algebra.** Time-labeled local channels $A_j=\chi_j\mathcal K_\sigma^2\chi_{j+1}$ define a compact block-cyclic operator. Every nonzero eigenvalue $\eta$ of one full return produces all $k$ roots in component time and all $2k$ roots after the one-step bipartite lift. The principal return is positive and simple, so its roots form the exact outer ring of the auxiliary block.

5.  **Seven-noise audit.** With $k=N_\sigma^{\rm H}+1$ selected by the independent RH-16 half-energy rank and with a fixed six-width window, the nonlinear local-return radius approaches the archived full-operator bulk edge. The tail-three radial RMS error is $1.96\times10^{-3}$, compared with $1.72\times10^{-2}$ for the deterministic-cycle radius. These are ordinary floating-point comparisons, not error-controlled spectral enclosures.

6.  **Unproved Feshbach arrow.** We do not prove that the branch-isolated direct-sum block is similar to, or is the Schur complement of, the full Gaussian Markov operator. The sharp windows discard trajectories that leave and later re-enter the packet tube. A complement-resolvent estimate and a bound on that return self-energy are still required.

The status can be summarized as $$\label{eq:logical-status}
 \boxed{
 \begin{gathered}
 \text{boundary cycle}
 \Longrightarrow
 \text{periodic Gaussian tube}
 \Longrightarrow
 \text{conditioned critical closure},\\
 \text{conditioned critical closure}
 \Longrightarrow
 \text{exact auxiliary root ring},\\
 \text{auxiliary root ring}
 \quad\Longrightarrow?\quad
 \text{full Markov Feshbach block}.
 \end{gathered}}$$ The entire upper line is proved here or reduced to previously proved cycle asymptotics. The lower arrow is tested numerically and remains open.

# Boundary dynamics and the folded Gaussian operator {#sec:setup}

Let $u_{\mathrm c}$ be the root in $(1,2)$ of $$\label{eq:cubic}
 u^3-2u^2+2u-2=0,$$ and set $$\label{eq:constants}
 f(x)=1-u_{\mathrm c}x^2,
 \qquad r=u_{\mathrm c}-1,
 \qquad \lambda=2u_{\mathrm c}r.$$ Then $$\label{eq:postcritical}
 0\longmapsto1\longmapsto-r\longmapsto r\longmapsto r,$$ and $$\label{eq:numerical-constants}
 u_{\mathrm c}=1.543689012692076\ldots,
 \quad r=0.543689012692076\ldots,
 \quad \lambda=1.678573510428322\ldots.$$ Write $S=f^2$. The component fixed point has $S'(r)=\lambda^2$.

For $y\in[-r,1]$, define $$\label{eq:inverse-branches}
 g_+(y)=\sqrt{\frac{1-y}{u_{\mathrm c}}},
 \qquad
 g_-(y)=-\sqrt{\frac{1-y}{u_{\mathrm c}}},$$ and $$\label{eq:hq}
 h=g_+\circ g_+,
 \qquad q=g_+\circ g_-.$$ Thus $S\circ h=S\circ q=\mathrm I$ on the corresponding branches, $h(r)=r$, and $h'(r)=\lambda^{-2}$.

Let $p_k=p_{2k}$ be the fixed point of $q\circ h^{k-1}$ and put $$\label{eq:clearance}
 \delta_k=1-p_k.$$ The boundary-cycle theorem gives $$\label{eq:clearance-asymptotic}
 \delta_k=C_{\rm b}\lambda^{-2k}(1+o(1)),
 \qquad
 C_{\rm b}=0.4608051492\ldots>0.$$ Its component-time orbit is $$\label{eq:ordered-cycle}
 x_{k,0}=p_k,
 \qquad
 x_{k,j}=h^{k-j}(p_k)\quad(1\le j\le k-1),$$ with $$\label{eq:cycle-order}
 S(x_{k,j})=x_{k,j+1\pmod k}.$$ The multiplier satisfies $$\label{eq:multiplier-asymptotic}
 M_k:=(S^k)'(p_k)
 =-C_M\lambda^k(1+o(1)),
 \qquad C_M=1.9463429052\ldots>0.$$ Equations [\[eq:clearance-asymptotic\]](#eq:clearance-asymptotic){reference-type="eqref" reference="eq:clearance-asymptotic"}--[\[eq:multiplier-asymptotic\]](#eq:multiplier-asymptotic){reference-type="eqref" reference="eq:multiplier-asymptotic"} are analytic results from the preceding boundary-cycle construction; the displayed decimals are multiprecision evaluations [@WangTimeOrdered2026].

The point $$\label{eq:partition-b}
 b=h(1)=u_{\mathrm c}^{-1/2}$$ is the source-side critical partition. The final cycle point $x_{k,k-1}=h(p_k)$ lies to its left and approaches it as $$\label{eq:last-point-scale}
 b-x_{k,k-1}
 =\frac{\sqrt{\delta_k}}{2u_{\mathrm c}}+O(\delta_k).$$

## The row-normalized folded kernel

Let $$\label{eq:normal-density}
 \phi_\sigma(t)=\frac1{\sqrt{2\pi}\sigma}
 e^{-t^2/(2\sigma^2)},
 \qquad
 \Phi(a)=\frac1{\sqrt{2\pi}}\int_{-\infty}^a e^{-z^2/2}\,dz.$$ For $x,y\in[0,1]$, define $$\begin{aligned}
 Z_\sigma(x)
 &=\int_0^1\{\phi_\sigma(y-f(x))+\phi_\sigma(y+f(x))\}\,dy,
 \label{eq:normalization}\\
 P_\sigma(x,y)
 &=\frac{\phi_\sigma(y-f(x))+\phi_\sigma(y+f(x))}
 {Z_\sigma(x)}.
 \label{eq:folded-kernel}\end{aligned}$$ The folded backward Markov operator is $$\label{eq:markov-operator}
 (\mathcal K_\sigma g)(x)=\int_0^1P_\sigma(x,y)g(y)\,dy.$$ Probabilistically, one adds $N(0,\sigma^2)$ noise to $f(x)$, conditions the result to lie in $[-1,1]$, and then folds by absolute value. For each fixed $\sigma>0$, the kernel is continuous and strictly positive. Hence $\mathcal K_\sigma$ and its restrictions below are compact on $L^2(0,1)$.

# The periodic affine Gaussian tube {#sec:riccati}

Along the ordered cycle define $$\label{eq:m-beta}
 m_{k,j}=|S'(x_{k,j})|,
 \qquad
 \beta_{k,j}^2=1+f'(f(x_{k,j}))^2.$$ The second formula is the variance of the two independent one-step noises after linearizing their two-step composition. In coordinates $x=x_{k,j}+\sigma q$, the tangent channel has the form $$\label{eq:affine-channel}
 (\mathcal L_{k,j}^{\rm aff}g)(q)
 =\int_\mathbb Rg(m_{k,j}q+\beta_{k,j}z)
 \frac{e^{-z^2/2}}{\sqrt{2\pi}}\,dz.$$ The sign of $S'$ is immaterial for centered even Gaussian observables.

[\[thm:periodic-riccati\]]{#thm:periodic-riccati label="thm:periodic-riccati"} For every $k$ for which $|M_k|>1$, there is a unique vector $v_{k,j}=t_{k,j}^2>0$ satisfying $$\label{eq:riccati-recurrence}
 m_{k,j}^2v_{k,j}=v_{k,j+1}+\beta_{k,j}^2,
 \qquad j\pmod k.$$ It is given explicitly by $$\label{eq:variance-explicit}
 v_{k,j}=
 \frac{1}{1-|M_k|^{-2}}
 \sum_{\ell=0}^{k-1}
 \frac{\beta_{k,j+\ell}^2}
 {\prod_{s=0}^{\ell}m_{k,j+s}^2},$$ where all indices are cyclic.

Rewrite [\[eq:riccati-recurrence\]](#eq:riccati-recurrence){reference-type="eqref" reference="eq:riccati-recurrence"} as $$v_{k,j}=m_{k,j}^{-2}v_{k,j+1}
 +m_{k,j}^{-2}\beta_{k,j}^2.$$ Iterating once around the cycle gives $$v_{k,j}=|M_k|^{-2}v_{k,j}
 +\sum_{\ell=0}^{k-1}
 \frac{\beta_{k,j+\ell}^2}
 {\prod_{s=0}^{\ell}m_{k,j+s}^2}.$$ Since $|M_k|>1$, solving for $v_{k,j}$ yields [\[eq:variance-explicit\]](#eq:variance-explicit){reference-type="eqref" reference="eq:variance-explicit"}, which is positive. The difference of any two periodic solutions would satisfy the homogeneous recurrence and therefore would equal $|M_k|^{-2}$ times itself after one circuit; it must vanish.

For this width vector, put $$\label{eq:gaussian-packets}
 G_{k,j}(q)=e^{-q^2/(2t_{k,j}^2)}.$$

[\[thm:packet-monodromy\]]{#thm:packet-monodromy label="thm:packet-monodromy"} The affine tangent channels transport the peak-normalized packets exactly: $$\label{eq:channel-identity}
 \mathcal L_{k,j}^{\rm aff}G_{k,j+1}
 =c_{k,j}G_{k,j},$$ where $$\label{eq:channel-coefficient}
 c_{k,j}
 =\frac{t_{k,j+1}}
 {\sqrt{t_{k,j+1}^2+\beta_{k,j}^2}}
 =\frac{t_{k,j+1}}{m_{k,j}t_{k,j}}
 \in(0,1).$$ Their product is the exact inverse cycle multiplier: $$\label{eq:coefficient-product}
 \boxed{\prod_{j=0}^{k-1}c_{k,j}=|M_k|^{-1}.}$$

For $m,\beta,T>0$, completing the square gives $$\label{eq:gaussian-integral}
 \int_\mathbb R
 e^{-(mq+\beta z)^2/(2T^2)}
 \frac{e^{-z^2/2}}{\sqrt{2\pi}}\,dz
 =\frac{T}{\sqrt{T^2+\beta^2}}
 e^{-m^2q^2/[2(T^2+\beta^2)]}.$$ Take $T=t_{k,j+1}$ and use [\[eq:riccati-recurrence\]](#eq:riccati-recurrence){reference-type="eqref" reference="eq:riccati-recurrence"}. This proves [\[eq:channel-identity\]](#eq:channel-identity){reference-type="eqref" reference="eq:channel-identity"}--[\[eq:channel-coefficient\]](#eq:channel-coefficient){reference-type="eqref" reference="eq:channel-coefficient"}. Multiplication around the cycle cancels every packet width and leaves $$\prod_jc_{k,j}
 =\frac{\prod_jt_{k,j+1}}
 {\prod_jm_{k,j}t_{k,j}}
 =\frac1{|M_k|}.$$

[\[cor:packet-radius\]]{#cor:packet-radius label="cor:packet-radius"} Let $W_k^{\rm G}$ be the scalar weighted cyclic shift with local weights $c_{k,j}$. Its spectral radius is $$\label{eq:packet-radius}
 \operatorname{spr}(W_k^{\rm G})
 =\left(\prod_jc_{k,j}\right)^{1/k}
 =|M_k|^{-1/k}=\rho_k.$$ Thus covariance adaptation changes the distribution of local weights but not their geometric mean.

## Endpoint and critical-source width asymptotics

The periodic solution is narrow at the endpoint but broad at the source of the critical closing channel.

[\[prop:width-asymptotics\]]{#prop:width-asymptotics label="prop:width-asymptotics"} Put $$\begin{aligned}
 v_{\rm r}&=\frac{1+\lambda^2}{\lambda^4-1}
 =\frac1{\lambda^2-1},
 \label{eq:repelling-variance}\\
 v_{\rm e}&=\frac{v_{\rm r}+1+\lambda^2}{(2u_{\mathrm c}\lambda)^2},
 \label{eq:endpoint-variance}\\
 C_t&=\frac{\sqrt{v_{\rm e}+1}}
 {4u_{\mathrm c}\sqrt{C_{\rm b}}}.
 \label{eq:critical-width-constant}\end{aligned}$$ Then $$\label{eq:width-limits}
 t_{k,0}\longrightarrow\sqrt{v_{\rm e}}
 =0.403274090775398\ldots,
 \qquad
 \frac{t_{k,k-1}}{\lambda^k}\longrightarrow C_t
 =0.257242247329236\ldots.$$ If $n_k=\lfloor k/2\rfloor$, then $$\label{eq:midpoint-width}
 \log t_{k,n_k}=o(k).$$ In fact, the midpoint widths remain bounded above and below along each parity subsequence.

For a fixed number of initial internal steps, the cycle points converge to $r$. There $m^2=\lambda^4$ and $\beta^2=1+\lambda^2$, so the attracting backward variance recurrence has the fixed value $v_{\rm r}$ in [\[eq:repelling-variance\]](#eq:repelling-variance){reference-type="eqref" reference="eq:repelling-variance"}. Formula [\[eq:variance-explicit\]](#eq:variance-explicit){reference-type="eqref" reference="eq:variance-explicit"}, together with the uniform contraction of $h$ near $r$, shows $v_{k,1}\to v_{\rm r}$: contributions from the closing edge are divided by the squared derivative of a repelling segment whose length tends to infinity.

At $x_{k,0}\to1$, $$m_{k,0}\to|S'(1)|=2u_{\mathrm c}\lambda,
 \qquad
 \beta_{k,0}^2\to1+\lambda^2.$$ The $j=0$ Riccati equation therefore gives $v_{k,0}\to v_{\rm e}$.

At the final source, the critical-return derivative theorem gives $$\label{eq:last-multiplier}
 m_{k,k-1}
 =4u_{\mathrm c}\sqrt{C_{\rm b}}\,\lambda^{-k}(1+o(1)),$$ while $f(x_{k,k-1})\to0$, and hence $\beta_{k,k-1}^2\to1$. The closing Riccati equation $$m_{k,k-1}^2v_{k,k-1}=v_{k,0}+\beta_{k,k-1}^2$$ proves the second limit in [\[eq:width-limits\]](#eq:width-limits){reference-type="eqref" reference="eq:width-limits"}.

For $n_k=\lfloor k/2\rfloor$, propagate the last variance backward using [\[eq:variance-explicit\]](#eq:variance-explicit){reference-type="eqref" reference="eq:variance-explicit"}. The Koenigs linearization of $h$ gives $$\prod_{j=n_k}^{k-2}m_{k,j}
 =\lambda^{2(k-1-n_k)+O(1)}.$$ The terminal contribution is therefore of order $\lambda^{2k-4(k-n_k)}=e^{O(1)}$, and the accumulated noise terms form a uniformly bounded geometric sum away from the finitely many terminal indices. Positivity gives the lower bound. This proves [\[eq:midpoint-width\]](#eq:midpoint-width){reference-type="eqref" reference="eq:midpoint-width"}.

The last physical width has a different noise scale. If $k=\log(1/\sigma)/(2\log\lambda)+O(1)$, then $$\label{eq:physical-width-scales}
 \sigma t_{k,0}=\Theta(\sigma),
 \qquad
 \sigma t_{k,k-1}=\Theta(\sqrt\sigma).$$ This is why the final channel sees the quadratic critical geometry.

# The quarter-power conditioning barrier {#sec:conditioning}

Let $$\label{eq:packet-rho}
 \rho_k=|M_k|^{-1/k}.$$ The canonical positive diagonal balance of the packet cycle is defined by $$\label{eq:packet-balance}
 d_{k,j+1}=\frac{c_{k,j}}{\rho_k}d_{k,j},
 \qquad
 D_k^{\rm G}=\operatorname{diag}(d_{k,0},\ldots,d_{k,k-1}).$$ Equation [\[eq:coefficient-product\]](#eq:coefficient-product){reference-type="eqref" reference="eq:coefficient-product"} closes the recurrence, and $(D_k^{\rm G})^{-1}W_k^{\rm G}D_k^{\rm G}$ is the constant cyclic shift of weight $\rho_k$.

[\[lem:half-cycle-product\]]{#lem:half-cycle-product label="lem:half-cycle-product"} For $n_k=\lfloor k/2\rfloor$, $$\begin{aligned}
 \prod_{j=0}^{n_k-1}m_{k,j}
 &=\lambda^{2n_k+o(k)},
 \label{eq:partial-multiplier}\\
 \prod_{j=0}^{n_k-1}c_{k,j}
 &=\lambda^{-2n_k+o(k)}.
 \label{eq:partial-coefficients}\end{aligned}$$

For $1\le j<n_k$, the identity $x_{k,j}=h(x_{k,j+1})$ gives $m_{k,j}=1/h'(x_{k,j+1})$. Applying the derivative form of the Koenigs identity to $h^{n_k-1}$ shows $$\prod_{j=1}^{n_k-1}m_{k,j}
 =\lambda^{2(n_k-1)+o(k)}.$$ The omitted endpoint factor converges to $2u_{\mathrm c}\lambda>0$, proving [\[eq:partial-multiplier\]](#eq:partial-multiplier){reference-type="eqref" reference="eq:partial-multiplier"}. Telescoping [\[eq:channel-coefficient\]](#eq:channel-coefficient){reference-type="eqref" reference="eq:channel-coefficient"} over the same segment gives $$\prod_{j=0}^{n_k-1}c_{k,j}
 =\frac{t_{k,n_k}}
 {t_{k,0}\prod_{j=0}^{n_k-1}m_{k,j}}.$$ Use [\[prop:width-asymptotics\]](#prop:width-asymptotics){reference-type="ref" reference="prop:width-asymptotics"} to obtain [\[eq:partial-coefficients\]](#eq:partial-coefficients){reference-type="eqref" reference="eq:partial-coefficients"}.

[\[thm:packet-conditioning\]]{#thm:packet-conditioning label="thm:packet-conditioning"} The canonical Gaussian-packet balance satisfies $$\label{eq:conditioning-liminf}
 \boxed{
 \liminf_{k\to\infty}
 \frac{\log\operatorname{cond}_2(D_k^{\rm G})}{k\log\lambda}
 \ge\frac12.}$$ Equivalently, $$\label{eq:conditioning-growth}
 \operatorname{cond}_2(D_k^{\rm G})\ge\lambda^{k/2-o(k)}.$$ If $$\label{eq:noise-clock}
 k_\sigma=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),$$ then $$\label{eq:quarter-power}
 \operatorname{cond}_2(D_{k_\sigma}^{\rm G})
 \ge\sigma^{-1/4+o(1)}.$$

Iterating [\[eq:packet-balance\]](#eq:packet-balance){reference-type="eqref" reference="eq:packet-balance"} to $n_k$ gives $$\frac{d_{k,n_k}}{d_{k,0}}
 =\rho_k^{-n_k}\prod_{j=0}^{n_k-1}c_{k,j}.$$ By [\[eq:multiplier-asymptotic\]](#eq:multiplier-asymptotic){reference-type="eqref" reference="eq:multiplier-asymptotic"}, $\rho_k=\lambda^{-1+o(1)}$. Combining this with [\[lem:half-cycle-product\]](#lem:half-cycle-product){reference-type="ref" reference="lem:half-cycle-product"} yields $$\frac{d_{k,n_k}}{d_{k,0}}
 =\lambda^{-n_k+o(k)}.$$ The ratio of the largest to the smallest diagonal entry is at least the reciprocal of this ratio, proving [\[eq:conditioning-liminf\]](#eq:conditioning-liminf){reference-type="eqref" reference="eq:conditioning-liminf"}--[\[eq:conditioning-growth\]](#eq:conditioning-growth){reference-type="eqref" reference="eq:conditioning-growth"}. Substitution of [\[eq:noise-clock\]](#eq:noise-clock){reference-type="eqref" reference="eq:noise-clock"} gives [\[eq:quarter-power\]](#eq:quarter-power){reference-type="eqref" reference="eq:quarter-power"}.

[\[rem:conditioning-interpretation\]]{#rem:conditioning-interpretation label="rem:conditioning-interpretation"} Every local coefficient in [\[eq:channel-coefficient\]](#eq:channel-coefficient){reference-type="eqref" reference="eq:channel-coefficient"} is below one, so the exponentially large critical-return weight of the raw inverse-Jacobian cycle has disappeared. The obstruction is now distributed across roughly half of the cycle: coefficients are near $\lambda^{-2}$ during the narrow repelling segment and near one while the broad packet contracts toward the critical source. The theorem proves a remaining half-exponent lower bound; it does not prove the matching upper bound. The numerical exponent at $k=100$ is $0.49220$.

# Conditioned quadratic closure of the last channel {#sec:critical-closure}

The affine packet theorem is exact for the tangent model, not for the nonlinear operator. The distinction becomes leading order at the final source because of [\[eq:physical-width-scales\]](#eq:physical-width-scales){reference-type="eqref" reference="eq:physical-width-scales"}.

For $d,t>0$, define $$\label{eq:A-B}
 A_d(q)=(\sqrt d-2u_{\mathrm c}q)^2,
 \qquad
 B_d(q)=d-A_d(q).$$

[\[thm:critical-profile\]]{#thm:critical-profile label="thm:critical-profile"} Let $d_\sigma\to d>0$, $t_\sigma\to t>0$, and put $$\label{eq:critical-scaling}
 p_\sigma=1-\sigma d_\sigma,
 \qquad
 s_\sigma=h(p_\sigma),
 \qquad
 g_\sigma(y)=
 \exp\!\left[-\frac{(y-p_\sigma)^2}{2\sigma^2t_\sigma^2}\right].$$ Then, locally uniformly for $q\in\mathbb R$, $$\label{eq:profile-limit}
 (\mathcal K_\sigma^2g_\sigma)(s_\sigma+\sqrt\sigma q)
 \longrightarrow \Gamma_{d,t}(q),$$ where $$\label{eq:Gamma}
 \boxed{
 \Gamma_{d,t}(q)=
 \frac{t}{\sqrt{1+t^2}}
 \exp\!\left[-\frac{B_d(q)^2}{2(1+t^2)}\right]
 \frac{
 \Phi\!\left[
 \frac{\sqrt{1+t^2}}{t}
 \left(A_d(q)+\frac{B_d(q)}{1+t^2}\right)
 \right]}
 {\Phi(A_d(q))}.}$$

Because $f(s_\sigma)=g_+(p_\sigma)$, Taylor expansion on compact $q$-sets gives $$\label{eq:first-critical-expansion}
 f(s_\sigma+\sqrt\sigma q)
 =\frac{\sqrt\sigma}{\sqrt u_{\mathrm c}}
 (\sqrt{d_\sigma}-2u_{\mathrm c}q)+O(\sigma).$$ The first noisy step is a distance of order one from the state endpoints, so its row normalization tends to one. Folding does not alter its square. If $Y_1$ denotes that first folded state, then $$\label{eq:first-square-limit}
 \frac{u_{\mathrm c}Y_1^2}{\sigma}
 \longrightarrow A_d(q)$$ in probability, locally uniformly in $q$. The first noise has size $\sigma$, whereas the deterministic intermediate value has size $\sqrt\sigma$; at its zero, the remaining squared noise is $O(\sigma^2)$ and still vanishes after division by $\sigma$.

Consequently the mean of the second step is $$\label{eq:second-mean}
 f(Y_1)=1-\sigma A_d(q)+o_{\mathbb P}(\sigma).$$ The lower state boundary is exponentially remote. The upper boundary conditions the standardized second noise $Z$ to $Z\le A_d(q)+o(1)$, with normalization $\Phi(A_d(q))$. Since $$\frac{f(Y_1)+\sigma Z-p_\sigma}{\sigma}
 =B_d(q)+Z+o_{\mathbb P}(1),$$ dominated convergence reduces the limit to $$\label{eq:profile-integral}
 \Gamma_{d,t}(q)
 =\frac1{\Phi(A_d(q))}
 \int_{-\infty}^{A_d(q)}
 e^{-[B_d(q)+z]^2/(2t^2)}
 \frac{e^{-z^2/2}}{\sqrt{2\pi}}\,dz.$$ Completing the square evaluates this integral as [\[eq:Gamma\]](#eq:Gamma){reference-type="eqref" reference="eq:Gamma"}. The estimates above are uniform on compact $q$-sets, proving locally uniform convergence.

[\[cor:critical-midpoint\]]{#cor:critical-midpoint label="cor:critical-midpoint"} The profile is symmetric under reflection about $$\label{eq:q-midpoint}
 q_{\rm b}=\frac{\sqrt d}{2u_{\mathrm c}}:
 \qquad
 \Gamma_{d,t}(q_{\rm b}+s)
 =\Gamma_{d,t}(q_{\rm b}-s).$$ Moreover, $$\label{eq:partition-coordinate}
 \frac{b-s_\sigma}{\sqrt\sigma}
 \longrightarrow q_{\rm b}.$$ Thus the two limiting lobes are the two quadratic preimages separated by the physical partition $b=u_{\mathrm c}^{-1/2}$. The boundary word selects the left branch $x<b$.

The function $A_d(q)$ depends only on $(q-q_{\rm b})^2$, and $B_d=d-A_d$, proving the symmetry. Expanding $h(1-\sigma d_\sigma)$ in [\[eq:last-point-scale\]](#eq:last-point-scale){reference-type="eqref" reference="eq:last-point-scale"} proves [\[eq:partition-coordinate\]](#eq:partition-coordinate){reference-type="eqref" reference="eq:partition-coordinate"}.

[\[rem:conditioning-profile\]]{#rem:conditioning-profile label="rem:conditioning-profile"} If the upper state boundary is ignored, [\[eq:profile-integral\]](#eq:profile-integral){reference-type="eqref" reference="eq:profile-integral"} is integrated over all $z$ and reduces to $$\label{eq:unconditioned-profile}
 \Gamma_{d,t}^{\rm uncond}(q)
 =\frac{t}{\sqrt{1+t^2}}
 e^{-B_d(q)^2/[2(1+t^2)]}.$$ This drops both the numerator and denominator distribution functions. An affine approximation additionally replaces the quadratic $A_d$ by its linear variation on one lobe. Neither operation is asymptotically justified when $d=O(1)$; the numerical audit in [7](#sec:numerics){reference-type="ref" reference="sec:numerics"} resolves the difference directly.

# Branch-isolated block-cyclic return operators {#sec:block-cyclic}

Fix $\sigma>0$, a component period $k$, and a window multiple $L>0$. Let $$\label{eq:packet-windows}
 I_{k,j}(\sigma,L)
 =\{x\in[0,1]:|x-x_{k,j}|\le L\sigma t_{k,j}\},$$ except that the final interval is branch isolated: $$\label{eq:branch-window}
 I_{k,k-1}(\sigma,L)
 =\{x:|x-x_{k,k-1}|\le L\sigma t_{k,k-1},\ x<b\}.$$ Write $\chi_j$ for multiplication by its indicator and $\mathcal H_j=L^2(I_{k,j})$. The backward local channel is $$\label{eq:local-channel}
 A_j=\chi_j\mathcal K_\sigma^2\chi_{j+1}:
 \mathcal H_{j+1}\longrightarrow\mathcal H_j,
 \qquad j\pmod k.$$ The time labels are part of the construction. Even if two spatial windows overlap, their copies in the direct sum remain distinct.

Define $$\label{eq:block-cyclic-operator}
 \mathfrak C_{\sigma,k}:\bigoplus_{j=0}^{k-1}\mathcal H_j
 \longrightarrow\bigoplus_{j=0}^{k-1}\mathcal H_j,
 \qquad
 (\mathfrak C_{\sigma,k}v)_j=A_jv_{j+1}.$$ The return to the endpoint window is $$\label{eq:return-operator}
 \mathcal R_{\sigma,k}=A_0A_1\cdots A_{k-1}:\mathcal H_0\to\mathcal H_0.$$

[\[thm:root-ring\]]{#thm:root-ring label="thm:root-ring"} The operators $A_j$, $\mathfrak C_{\sigma,k}$, and $\mathcal R_{\sigma,k}$ are compact. Their nonzero spectra satisfy $$\label{eq:root-spectrum}
 \operatorname{spec}(\mathfrak C_{\sigma,k})\setminus\{0\}
 =\{\zeta\in\mathbb C:\zeta^k\in
 \operatorname{spec}(\mathcal R_{\sigma,k})\setminus\{0\}\}.$$ In particular, every nonzero return eigenvalue $\eta$ generates the complete ring $$\label{eq:k-root-ring}
 \zeta_\ell=\eta^{1/k}e^{2\pi i\ell/k},
 \qquad 0\le\ell<k,$$ with the same algebraic multiplicity for each root.

Each local channel has a square-integrable continuous kernel on bounded intervals and is therefore compact. Direct multiplication gives $$\label{eq:Ck-diagonal}
 \mathfrak C_{\sigma,k}^k
 =\operatorname{diag}(\mathcal R_0,\ldots,\mathcal R_{k-1}),$$ where $\mathcal R_j=A_jA_{j+1}\cdots A_{j-1}$. Cyclic products have the same nonzero spectrum, including algebraic multiplicity, by repeated use of the $AB$--$BA$ correspondence for compact operators.

If $\mathcal R_0v_0=\eta v_0$ and $\zeta^k=\eta\ne0$, define successively $$v_{k-1}=\zeta^{-1}A_{k-1}v_0,
 \quad
 v_{k-2}=\zeta^{-2}A_{k-2}A_{k-1}v_0,
 \quad\ldots.$$ Then $v=(v_0,\ldots,v_{k-1})$ satisfies $\mathfrak C_{\sigma,k}v=\zeta v$. Conversely, [\[eq:Ck-diagonal\]](#eq:Ck-diagonal){reference-type="eqref" reference="eq:Ck-diagonal"} sends every nonzero eigenvalue $\zeta$ to a return eigenvalue $\zeta^k$. The same construction for generalized eigenspaces proves the multiplicity statement.

The map $f$ exchanges two dynamical components in one step. As in the deterministic construction, introduce the algebraic bipartite lift $$\label{eq:bipartite-lift}
 \mathfrak B_{\sigma,k}
 =\begin{pmatrix}0&\mathrm I\\ \mathfrak C_{\sigma,k}&0\end{pmatrix}.$$ It satisfies $\mathfrak B_{\sigma,k}^2=operatorname{diag}(\mathfrak C_{\sigma,k},
\mathfrak C_{\sigma,k})$.

[\[cor:one-step-ring\]]{#cor:one-step-ring label="cor:one-step-ring"} Every nonzero return eigenvalue $\eta$ generates the $2k$ one-step values $$\label{eq:2k-ring}
 \mu_\ell=\eta^{1/(2k)}e^{\pi i\ell/k},
 \qquad 0\le\ell<2k.$$ Their radius is $|\eta|^{1/(2k)}$ and their phases are exact, independent of the rank or detailed shape of the local channels.

[\[rem:lift-normalization\]]{#rem:lift-normalization label="rem:lift-normalization"} The identity block in [\[eq:bipartite-lift\]](#eq:bipartite-lift){reference-type="eqref" reference="eq:bipartite-lift"} is an algebraic normalization, not an identification of the separate one-step noisy channels. More generally, a lift with off-diagonal blocks $B$ and $C$ has determinant controlled by $BC$ and $CB$. The two-step return is the invariant object used here; splitting it into physical one-step Grushin blocks is part of the remaining global problem.

[\[thm:principal-return\]]{#thm:principal-return label="thm:principal-return"} For every fixed $\sigma,k,L$ with all windows of positive measure, $\mathcal R_{\sigma,k}$ has a spectral radius $\eta_0>0$ that is an algebraically simple eigenvalue with a strictly positive eigenfunction. Every other return eigenvalue $\eta$ satisfies $|\eta|<\eta_0$. Consequently the $2k$ roots of $\eta_0$ in [\[eq:2k-ring\]](#eq:2k-ring){reference-type="eqref" reference="eq:2k-ring"} form the exact outer spectral ring of the branch-isolated auxiliary lift.

The kernel of $\mathcal K_\sigma^2$ is strictly positive. Integrating products of these kernels over the intermediate windows shows that $\mathcal R_{\sigma,k}$ is positivity improving on $\mathcal H_0$. It is compact by [\[thm:root-ring\]](#thm:root-ring){reference-type="ref" reference="thm:root-ring"}. The Jentzsch--Krein--Rutman theorem therefore gives a positive algebraically simple spectral radius and excludes every other eigenvalue from its peripheral circle [@Schaefer1974]. The root-ring conclusion follows from [\[cor:one-step-ring\]](#cor:one-step-ring){reference-type="ref" reference="cor:one-step-ring"}.

For comparison with the parity-extracted cloud, the two real roots $\pm\eta_0^{1/(2k)}$ play the role of the distinguished edge pair and are removed. The remaining $2k-2$ roots have exactly the degree associated with $k=N_\sigma+1$.

# Seven-noise numerical audit {#sec:numerics}

The analytic results through [\[thm:principal-return\]](#thm:principal-return){reference-type="ref" reference="thm:principal-return"} do not depend on the following finite computations. The audit asks a narrower question: does the principal eigenvalue of the branch-isolated nonlinear return have the radial size of the already archived full-operator cloud?

## Protocol

For each of the seven RH-15 noise levels, the folded kernel is discretized by a row-normalized midpoint Nyström matrix with $$\label{eq:grid-scaling}
 n\sigma=20.48.$$ Gaussian entries beyond eight standard deviations are omitted. The maximum row-sum error is $5.6\times10^{-16}$. The component period is selected before reading a bulk radius: $$\label{eq:period-selection}
 k=N_\sigma^{\rm H}+1,$$ where $N_\sigma^{\rm H}$ is the RH-16 Hellinger half-energy rank. Every window uses $L=6$, and only the final window receives the fixed physical cut $x<b$. Nine positive power iterations resolve $\eta_0$; the computed relative residuals are at most $2.6\times10^{-9}$ and are near machine precision except at the coarsest noise.

The comparison target is the archived *bulk radius*, the largest modulus among the automatically selected parity-extracted outer cloud. It is not the cloud's radial mean. No local-return parameter is fitted to that radius.

## The nonlinear local return reaches the edge

::: {#tab:edge-audit}
            $\sigma$   $k$     $\eta_0$   local radius   RH-17 radius   bulk radius
  ------------------ ----- ------------ -------------- -------------- -------------
           $10^{-2}$     3   0.16523051     0.74076713     0.70350068    0.67466935
    $4\times10^{-3}$     4   0.09550137     0.74559194     0.71507601    0.71794136
    $2\times10^{-3}$     5   0.05608219     0.74969135     0.72415158    0.73627786
           $10^{-3}$     6   0.03022240     0.74706905     0.73108951    0.73914154
    $5\times10^{-4}$     6   0.03236519     0.75134577     0.73108951    0.74801500
    $2\times10^{-4}$     7   0.01959402     0.75510757     0.73642348    0.75474882
           $10^{-4}$     8   0.01149664     0.75645948     0.74059474    0.75702308

  : Branch-isolated principal-return radius versus the archived full bulk edge. The RH-17 column is the deterministic cycle radius $|M_k|^{-1/(2k)}$.
:::

At the three smallest noises, local minus full-edge errors are $$\label{eq:tail-errors}
 3.331\times10^{-3},
 \qquad 3.588\times10^{-4},
 \qquad -5.636\times10^{-4}.$$ Their RMS is $$\label{eq:tail-rms}
 \begin{array}{c|c}
 \text{model}&\text{tail-three radial RMS}\\ \hline
 \text{nonlinear branch return}&0.0019613\\
 \text{RH-17 deterministic cycle}&0.0172451
 \end{array}$$ The coarse-noise mismatch is substantial and is not hidden: at $\sigma=10^{-2}$ the local block overshoots the archived edge by $0.0661$. The evidence concerns the small-noise tail, not a uniform seven-point fit.

![Branch-isolated return and full-spectrum comparison. Top left: the principal local-return radius selected by the Hellinger rank, the linear-row alternative, the deterministic cycle, and the archived full bulk edge. Top right: absolute radial errors. Bottom left: the smallest noise cloud, the edge-deflated local root ring, and the RH-17 deterministic ring. Bottom right: moduli of the first five return eigenvalues relative to the principal one. All full spectra are imported unchanged from RH-15.](<../../../../../zeta_mvp0/papers/RH-18-branch-isolated-gaussian-return/figures/branch_isolated_bulk_edge.pdf>){#fig:edge-audit width="\\textwidth"}

The deterministic and nonlinear constructions need not have the same radial role. The deterministic multiplier is the first stability channel of one orbit and previously tracked an interior finite-section radius. The local return includes finite-noise spreading, nonlinear closure, state conditioning, and branch loss. The data suggest that the latter controls the outer edge while the former remains an interior reference. This is an interpretation of the audit, not an asymptotic theorem.

## The critical profile is the required local correction

For every noise, the endpoint Gaussian is pulled back by the full sparse $\mathcal K_\sigma^2$ and compared on the final branch window with [\[eq:Gamma\]](#eq:Gamma){reference-type="eqref" reference="eq:Gamma"}. No amplitude is fitted for the direct error.

::: {#tab:critical-errors}
            $\sigma$   $k$   conditioned   unconditioned     affine
  ------------------ ----- ------------- --------------- ----------
           $10^{-2}$     3      0.050670        0.263161   0.473874
    $4\times10^{-3}$     4      0.025979        0.266454   0.480685
    $2\times10^{-3}$     5      0.013019        0.325964   0.513897
           $10^{-3}$     6      0.007617        0.353751   0.489578
    $5\times10^{-4}$     6      0.008196        0.234486   0.448693
    $2\times10^{-4}$     7      0.004461        0.264965   0.480745
           $10^{-4}$     8      0.002411        0.332190   0.511101

  : Relative direct errors of the conditioned critical profile, the unconditioned quadratic profile, and an affine Gaussian profile.
:::

At $\sigma=10^{-3}$, a least-squares amplitude applied only as an audit is $1.000872$; the direct and fitted errors are $0.007617$ and $0.007567$. Thus the agreement is not created by amplitude renormalization. The unconditioned and affine errors stay of order one because their omitted terms remain leading at $\delta_k/\sigma=O(1)$.

![Riccati packet and critical closure audit. Top left: periodic widths and affine channel coefficients at $k=20$. Top right: raw and Gaussian-adapted balancing conditions; the reference exponents are one and one half. Bottom left: the exact folded two-step pullback and three local models at $\sigma=10^{-3}$. Bottom right: direct profile errors at all seven noises.](<../../../../../zeta_mvp0/papers/RH-18-branch-isolated-gaussian-return/figures/riccati_packet_critical_closure.pdf>){#fig:riccati-critical width="\\textwidth"}

## Return spectral gap and discretization checks

At $\sigma=10^{-4}$ and $k=8$, the first five computed return eigenvalue moduli relative to $\eta_0$ are $$\label{eq:return-gap-data}
 1,quad
 5.398\times10^{-3},quad
 1.776\times10^{-5},quad
 4.706\times10^{-8},quad
 1.055\times10^{-10}.$$ At $\sigma=10^{-3}$ and $k=6$, the corresponding first subleading ratio is $1.101\times10^{-2}$. This supports a rank-one leading return, but no uniform small-noise singular-value theorem is inferred from two spectra.

The window audit at $\sigma=10^{-3}$ gives $$\label{eq:window-audit}
 \begin{array}{c|ccccc}
 L&4&5&6&8&10\\ \hline
 \eta_0^{1/(2k)}
 &0.747062438&0.747069010&0.747069051&0.747069051&0.747069051
 \end{array}$$ so the range from four through ten widths is $6.61\times10^{-6}$. With $n\sigma=10.24,20.48,40.96$, the radii are respectively $$\label{eq:grid-audit}
 0.747075397,qquad0.747069051,qquad0.746955952.$$ The total resolution spread is $1.19\times10^{-4}$. This is a conventional convergence check, not a directed-rounding bound.

## Reproducibility and numerical status

The analytic Gaussian identities are tested against independent quadrature. The Riccati recurrence, multiplier product, critical-profile integral, block-cyclic spectrum, folded row normalization, branch masks, and principal return are covered by the test suite. NumPy, SciPy, and Matplotlib provide the numerical implementation [@HarrisEtAl2020; @VirtanenEtAl2020; @Hunter2007]. The audit records software versions, source hashes, every table row, the two return spectra, window and grid checks, and both figures. No interval arithmetic is used; all decimal comparisons in this section are ordinary floating-point evidence.

# What remains for a genuine Feshbach theorem {#sec:feshbach}

The branch-isolated return uses the exact nonlinear Gaussian kernel, but it is still an auxiliary operator. At every component step it applies a sharp window and discards the complement. The full Markov operator allows a path to leave the tube, travel through the bulk, and later return. Root symmetry inside $\mathfrak C_{\sigma,k}$ says nothing by itself about the size of those omitted paths.

To make the distinction explicit, suppose an adapted finite-dimensional entrance/exit construction produces a packet projection $P_\sigma$ and $Q_\sigma=\mathrm I-P_\sigma$. Wherever the complement inverse exists, the spectral Schur map contains the self-energy $$\label{eq:schur-self-energy}
 \Sigma_\sigma(z)
 =z^2P_\sigma\mathcal K_\sigma Q_\sigma
 (\mathrm I-zQ_\sigma\mathcal K_\sigma Q_\sigma)^{-1}
 Q_\sigma\mathcal K_\sigma P_\sigma.$$ The branch-isolated block models the direct time-ordered return. It does not bound [\[eq:schur-self-energy\]](#eq:schur-self-energy){reference-type="eqref" reference="eq:schur-self-energy"}.

A global identification requires at least the following four estimates.

1.  **Adapted packet maps.** Construct entrance and exit maps along all $x_{k,j}$ that include the non-Gaussian profile [\[eq:Gamma\]](#eq:Gamma){reference-type="eqref" reference="eq:Gamma"} at the closing edge. Their Gram and dual-Gram bounds must be compatible with the unavoidable $\sigma^{-1/4+o(1)}$ balance, rather than assumed uniform in a raw Euclidean basis.

2.  **Complement resolvent.** After the Perron and parity boundary layers are removed, prove a resolvent bound for $Q_\sigma\mathcal K_\sigma Q_\sigma$ on an annulus containing the bulk root ring. Compactness at each fixed noise is insufficient for a uniform small-noise estimate.

3.  **Excursion and re-entry control.** Show that [\[eq:schur-self-energy\]](#eq:schur-self-energy){reference-type="eqref" reference="eq:schur-self-energy"}, including paths that cross the other critical branch, is small in the adapted norm on the phase-spacing scale $1/k$. A Euclidean operator error alone can be amplified by the packet balance and does not yield eigenvalue control for this non-normal block [@Kato1995; @TrefethenEmbree2005].

4.  **Determinant comparison.** Prove that the residual determinant after principal-ring extraction is nonzero and locally normal on the target annulus. This is needed to turn a collection of quasimodes into the zero count and to connect back to the deterministic factor [\[eq:intro-pole\]](#eq:intro-pole){reference-type="eqref" reference="eq:intro-pole"}. A Grushin formulation is a natural framework for this step [@SjoestrandZworski2007].

The desired theorem would compare the full Feshbach determinant with that of $\mathfrak B_{\sigma,k_\sigma}$ after the two real edge channels are deflated, uniformly on contours separating consecutive roots. Nothing in the present numerical match proves such a contour estimate.

# Discussion {#sec:discussion}

## What has changed since the deterministic monodromy

The RH-17 cycle already fixed the phase mechanism: a closed time order, not a finite unilateral shift, produces the geometric polynomial. The present construction inserts the actual Gaussian covariance into that time order. The exact coefficient product shows that this insertion is compatible with the deterministic multiplier, while the Riccati widths explain how smoothing redistributes the extreme critical-return weight.

The redistribution is useful but incomplete. The raw basis has a $\lambda^k$ lower-bound barrier; the Gaussian packet basis retains at least $\lambda^{k/2-o(k)}$. Thus the natural normalization has moved from a $\sigma^{-1/2}$ to a $\sigma^{-1/4+o(1)}$ obstruction at the intrinsic rank clock. This is a quantitative narrowing of the problem, not a proof that an adapted Grushin reduction exists.

The critical profile is equally structural. The width selected by the Riccati equation reaches $O(\sqrt\sigma)$ exactly where the source approaches $b$. At that scale, the quadratic fold, the upper state boundary, and the two symbolic preimages all survive in the limit. The distribution-function ratio in [\[eq:Gamma\]](#eq:Gamma){reference-type="eqref" reference="eq:Gamma"} is therefore not a finite-noise correction that can be absorbed into a fitted amplitude.

## How far the spectral evidence reaches

Within the auxiliary local block, the phase ring is a theorem and the principal radius is a well-defined positive eigenvalue. The smallest-noise edge agreement is then a nontrivial test because the period comes from row geometry, the branch cut comes from dynamics, and the window multiple is held fixed. The comparison nevertheless reuses the same Gaussian kernel and the same state discretization as the archived full spectrum. It should be read as a successful localization diagnostic, not as independent experimental confirmation.

The large return gap makes the next analysis plausible: one can try to reduce each time-labeled channel to its principal packet plus a controlled orthogonal remainder. The quarter-power theorem warns that the norm in which this is done matters. The complement coupling in [\[eq:schur-self-energy\]](#eq:schur-self-energy){reference-type="eqref" reference="eq:schur-self-energy"} is now the central obstruction; if it is not small, the present direction can still fail despite the radial match.

## No arithmetic or self-adjoint spectral claim

All operators in this paper arise from one explicit noisy quadratic map. The roots-of-unity phases follow from finite cyclic time labels, and the principal return is a positive compact-operator eigenvalue. No result here identifies these values with zeros of the Riemann zeta function, constructs a self-adjoint Hilbert--Pólya operator, proves a prime-power trace formula, or implies the Riemann hypothesis. Any arithmetic comparison would require separate operator and trace identities not present in this work.

# Conclusion

The first noisy return-block test gives a positive but deliberately limited answer. Along the ordered boundary cycle, affine Gaussian packets possess a unique periodic Riccati tube and an exact monodromy whose total coefficient is the inverse deterministic multiplier. The adaptation removes the single exploding local weight, but a rigorous $\lambda^{k/2-o(k)}$ conditioning barrier remains. The last channel cannot be affine: its exact scaling limit is the conditioned Gaussian--quadratic profile [\[eq:Gamma\]](#eq:Gamma){reference-type="eqref" reference="eq:Gamma"}, and the dynamical partition $b=u_{\mathrm c}^{-1/2}$ selects one of its two symbolic branches.

Restricting the full nonlinear Gaussian operator to these time-labeled branch windows produces a compact cyclic return. Its principal eigenvalue is simple and generates an exact $2k$-root outer ring. With the period selected from the independent endpoint rank, that ring reaches the archived full bulk edge to $5.64\times10^{-4}$ at the smallest computed noise and is numerically separated from all subleading return rings.

What remains is also precise. The local construction discards complement excursions, so it is not yet the Feshbach block of the Markov operator. The next gate is a uniform complement-resolvent and Schur-self-energy estimate in an adapted norm that tolerates the quarter-power balance. Passing that gate would convert the present exact local algebra and floating-point edge match into a genuine noisy-cloud theorem; failing it would identify where the boundary-cycle route ceases to control the global spectrum.

# Data and code availability {#data-and-code-availability .unnumbered}

The source code, tests, CSV and JSON audits, sparse local-return spectra, window and grid checks, figures, and manuscript are available with this paper [@WangGaussianReturnCode2026].
