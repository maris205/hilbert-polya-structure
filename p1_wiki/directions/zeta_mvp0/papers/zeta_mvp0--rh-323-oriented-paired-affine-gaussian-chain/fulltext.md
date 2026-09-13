---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-323-oriented-paired-affine-gaussian-chain"
canonical_tex: "zeta_mvp0/papers/RH-323-oriented-paired-affine-gaussian-chain/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-323-oriented-paired-affine-gaussian-chain/main.pdf"
source_sha256: "33d5d8cd57f2ffb8d9eaa4ba3a795c6928df860f9ccc26d418da3c43e1bca0d4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Oriented Paired Affine Gaussian Chain at Critical Clearance

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-323-oriented-paired-affine-gaussian-chain>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-323-oriented-paired-affine-gaussian-chain/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-323-oriented-paired-affine-gaussian-chain/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-323-oriented-paired-affine-gaussian-chain/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-323-oriented-paired-affine-gaussian-chain/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The critical endpoint row of RH-322 has a half-line Gaussian limit indexed by the clearance phase. We propagate that probability law through the two signed affine tangent legs from the endpoint to the repelling boundary. The resulting joint law $$J_d(v,u,w)=g_d(v)\phi(u+2u_cv)\phi(w+\lambda u)$$ retains the source coordinate and therefore transfers the exact RH-322 $L^1$ error isometrically. Its intermediate and output marginals are explicit extended-skew-normal densities, not single Gaussians, and we give their complete first and second moments. At zero clearance, both nominal orientations have positive leakage of order one. This is an exact theorem for the local affine probability chain. It does not control the finite-noise curvature and normalization remainder, combine the neighboring sibling or parity layer, or prove a joint first-alias trace law.
author:
- Bin Wang
date: July 2026
title: An Oriented Paired Affine Gaussian Chain at Critical Clearance
```

## Markdown 正文

# The signed tangent chain

Let $u_c$ be the root in $(1,2)$ of $$u^3-2u^2+2u-2=0,
 \qquad r=u_c-1,
 \qquad \lambda=2u_cr.$$ The archived values are $$u_c=1.543689012692076\ldots,
 \qquad \lambda=1.678573510428322\ldots.$$ Set $$\label{eq:constants}
 \alpha=2u_c,
 \qquad \kappa_{\mathrm{aff}}=\alpha\lambda,
 \qquad \beta=\sqrt{1+\lambda^2},$$ so that $$\alpha=3.087378025384153\ldots,
 \quad \kappa_{\mathrm{aff}}=5.182390970088339\ldots,
 \quad \beta=1.953870269468181\ldots.$$ The subscript in $\kappa_{\mathrm{aff}}$ is essential: RH-14 already uses the unadorned $\kappa$ for a different parity-profile constant.

The two local expansions extracted in RH-14 are $$\begin{aligned}
 f(1-\sigma v)
  &=-r+\alpha\sigma v+O(\sigma^2v^2),
  \label{eq:endpoint-expansion}\\
 f(r+\sigma u)
  &=r-\lambda\sigma u-u_c\sigma^2u^2.
  \label{eq:repelling-expansion}\end{aligned}$$ After folding the negative first image, the signed tangent coordinates obey $$\label{eq:oriented-chain}
 U=-\alpha V-Z_1,
 \qquad W=-\lambda U+Z_2,$$ where $Z_1,Z_2$ are independent standard normals. Hence $$\label{eq:collapsed-chain}
 W=\kappa_{\mathrm{aff}}V+\lambda Z_1+Z_2
   =\kappa_{\mathrm{aff}}V+\beta Z$$ with $Z$ standard normal and independent of $V$. The variable $W$ is centered at the fixed point $r$. RH-17 gives $x_{k,1}-r=\kappa_{\mathrm{aff}}\delta_k(1+o(1))$, so comparison with a packet centered at the actual cycle point requires the translated coordinate $W-\kappa_{\mathrm{aff}}d$.

Equations [\[eq:oriented-chain\]](#eq:oriented-chain){reference-type="eqref" reference="eq:oriented-chain"}--[\[eq:collapsed-chain\]](#eq:collapsed-chain){reference-type="eqref" reference="eq:collapsed-chain"} define the limiting tangent model. They are not asserted as exact finite-$\sigma$ physical dynamics; the omitted terms in [\[eq:endpoint-expansion\]](#eq:endpoint-expansion){reference-type="eqref" reference="eq:endpoint-expansion"}--[\[eq:repelling-expansion\]](#eq:repelling-expansion){reference-type="eqref" reference="eq:repelling-expansion"}, fold changes, and finite row normalizers are the RH-324 interface.

# Exact Markov lifting of the RH-322 row

Write $$\phi(t)=\frac{e^{-t^2/2}}{\sqrt{2\pi}},
 \qquad
 \Phi(t)=\int_{-\infty}^t\phi(s)\,ds,
 \qquad \overline\Phi=1-\Phi,$$ and, for $d\ge0$, $$\label{eq:entrance-profile}
 g_d(v)=\frac{\phi(v-d)}{\Phi(d)}\mathbf1_{[0,\infty)}(v).$$ For any probability density $p$ on $\mathbb R_+$, define its oriented affine lift $$\label{eq:affine-lift}
 (\mathcal A p)(v,u,w)
 =p(v)\phi(u+\alpha v)\phi(w+\lambda u).$$

[\[thm:isometry\]]{#thm:isometry label="thm:isometry"} For any probability densities $p,q$ on $\mathbb R_+$, $$\label{eq:isometry}
 \|\mathcal A p-\mathcal A q\|_{L^1(\mathbb R_+\times\mathbb R^2)}
 =\|p-q\|_{L^1(\mathbb R_+)}.$$ Every marginalization of the lifted laws is an $L^1$ contraction.

The two conditional Gaussian densities in [\[eq:affine-lift\]](#eq:affine-lift){reference-type="eqref" reference="eq:affine-lift"} are nonnegative and each integrates to one. Tonelli's theorem gives $$\int_{\mathbb R_+\times\mathbb R^2}
 |p(v)-q(v)|\phi(u+\alpha v)\phi(w+\lambda u)\,dv\,du\,dw
 =\int_{\mathbb R_+}|p-q|.$$ Integrating out coordinates before taking the absolute value gives the marginal contraction statement.

To retain the exact RH-322 physical seed, put $L=\sigma^{-1}$ and $$\label{eq:finite-seed}
 \widetilde h_{\sigma,a}(v)=
 \frac{\phi(v-a)+\phi(2L-v-a)}
 {\Phi(a)-\overline\Phi(2L-a)}\mathbf1_{[0,L]}(v).$$ Define $$J_{\sigma,a}=\mathcal A\widetilde h_{\sigma,a},
 \qquad J_d=\mathcal A g_d.$$ The first object is an exact physical endpoint row followed by the exact *affine* lift; it is not the actual finite-noise two-step row.

[\[cor:finite-seed\]]{#cor:finite-seed label="cor:finite-seed"} For $\sigma>0$, $0\le a\le\sigma^{-1}$, and $d\ge0$, $$\begin{aligned}
 \|J_{\sigma,a}-J_d\|_1
 &=\|\widetilde h_{\sigma,a}-g_d\|_1,
 \label{eq:joint-base-equality}\\
 \|J_{\sigma,a}-J_d\|_1
 &\le |a-d|+
 \frac{2\overline\Phi(\sigma^{-1}-a)}{\Phi(a)}.
 \label{eq:joint-bound}\end{aligned}$$ In particular, $$\label{eq:same-phase}
 \|J_{\sigma,a}-J_a\|_1
 =\frac{2\overline\Phi(\sigma^{-1}-a)}{\Phi(a)}.$$ The same right side bounds every marginal distance. Under the convention $d_{\mathrm{TV}}=\tfrac12\|\cdot\|_1$, all statements divide by two.

The identity is [\[thm:isometry\]](#thm:isometry){reference-type="ref" reference="thm:isometry"}. RH-322 proves the exact same-phase tail in [\[eq:same-phase\]](#eq:same-phase){reference-type="eqref" reference="eq:same-phase"} and $\|g_a-g_d\|_1\le|a-d|$; the triangle inequality gives [\[eq:joint-bound\]](#eq:joint-bound){reference-type="eqref" reference="eq:joint-bound"}.

The equality in [\[eq:joint-base-equality\]](#eq:joint-base-equality){reference-type="eqref" reference="eq:joint-base-equality"} requires retaining $V$. After $V$ is marginalized, only contraction is available; no marginal isometry is claimed.

# Explicit marginals and a non-Gaussian output

Put $$\label{eq:scales}
 s_1=\sqrt{1+\alpha^2},
 \qquad s_2=\sqrt{\kappa_{\mathrm{aff}}^2+\beta^2}.$$

[\[prop:marginals\]]{#prop:marginals label="prop:marginals"} The intermediate and output densities of $J_d$ are $$\begin{aligned}
 p_d(u)
 &=\frac1{s_1\Phi(d)}
 \phi\!\left(\frac{u+\alpha d}{s_1}\right)
 \Phi\!\left(\frac{d-\alpha u}{s_1}\right),
 \label{eq:intermediate-density}\\
 q_d(w)
 &=\frac1{s_2\Phi(d)}
 \phi\!\left(\frac{w-\kappa_{\mathrm{aff}}d}{s_2}\right)
 \Phi\!\left(
 \frac{\kappa_{\mathrm{aff}}w+\beta^2d}{\beta s_2}
 \right).
 \label{eq:output-density}\end{aligned}$$ The joint $(U,W)$ density is $p_d(u)\phi(w+\lambda u)$.

Let $V_0\sim N(d,1)$ before conditioning on $V_0\ge0$. The unconditioned $U_0=-\alpha V_0-Z_1$ has law $N(-\alpha d,s_1^2)$, while $$V_0\mid U_0=u
 \sim N\!\left(\frac{d-\alpha u}{s_1^2},\frac1{s_1^2}\right).$$ Multiplying the unconditioned $U_0$ density by $\Pr(V_0\ge0\mid U_0=u)/\Phi(d)$ proves [\[eq:intermediate-density\]](#eq:intermediate-density){reference-type="eqref" reference="eq:intermediate-density"}. Likewise $W_0=\kappa_{\mathrm{aff}}V_0+\beta Z$ has law $N(\kappa_{\mathrm{aff}}d,s_2^2)$ and $$V_0\mid W_0=w
 \sim N\!\left(
 \frac{\kappa_{\mathrm{aff}}w+\beta^2d}{s_2^2},
 \frac{\beta^2}{s_2^2}
 \right),$$ which gives [\[eq:output-density\]](#eq:output-density){reference-type="eqref" reference="eq:output-density"}. The joint formula follows directly from $W\mid U=u\sim N(-\lambda u,1)$.

The output is not a single Gaussian. Indeed, let $$h_d(w)=\frac1{s_2}\phi\!\left(\frac{w-\kappa_{\mathrm{aff}}d}{s_2}\right).$$ Then [\[eq:output-density\]](#eq:output-density){reference-type="eqref" reference="eq:output-density"} gives the exact ratio $$\label{eq:tail-ratio}
 \frac{q_d(w)}{h_d(w)}
 =\frac1{\Phi(d)}
 \Phi\!\left(\frac{\kappa_{\mathrm{aff}}w+\beta^2d}{\beta s_2}\right)
 \longrightarrow\frac1{\Phi(d)}>1
 \quad(w\to+\infty)$$ for every finite $d\ge0$. A ratio of two Gaussian densities can have a finite nonzero right-tail limit only when their means and variances agree; then the ratio is identically one. Thus [\[eq:tail-ratio\]](#eq:tail-ratio){reference-type="eqref" reference="eq:tail-ratio"} proves the scoped negative result that $q_d$ is not any ordinary Gaussian.

# Moments and surviving orientations

Let $$\label{eq:mills}
 r_d=\frac{\phi(d)}{\Phi(d)},
 \qquad m_d=d+r_d,
 \qquad \nu_d=1-dr_d-r_d^2.$$

[\[prop:moments\]]{#prop:moments label="prop:moments"} The mean vector is $$\label{eq:mean-vector}
 \mathbb E(V,U,W)=m_d(1,-\alpha,\kappa_{\mathrm{aff}}).$$ The nonredundant covariance entries are $$\begin{aligned}
 \operatorname{Var}V&=\nu_d,&
 \operatorname{Var}U&=\alpha^2\nu_d+1,&
 \operatorname{Var}W&=\kappa_{\mathrm{aff}}^2\nu_d+\beta^2,
 \label{eq:variances}\\
 \operatorname{Cov}(V,U)&=-\alpha\nu_d,&
 \operatorname{Cov}(V,W)&=\kappa_{\mathrm{aff}}\nu_d,&
 \operatorname{Cov}(U,W)&=-\lambda(\alpha^2\nu_d+1).
 \label{eq:covariances}\end{aligned}$$ Relative to the deterministic centers $(d,-\alpha d,\kappa_{\mathrm{aff}}d)$, the conditioning bias is $$\label{eq:bias}
 r_d(1,-\alpha,\kappa_{\mathrm{aff}}).$$

The RH-322 entrance law has mean $m_d$ and variance $\nu_d$. Apply the independent-noise identities [\[eq:oriented-chain\]](#eq:oriented-chain){reference-type="eqref" reference="eq:oriented-chain"} and [\[eq:collapsed-chain\]](#eq:collapsed-chain){reference-type="eqref" reference="eq:collapsed-chain"}. In particular, $\operatorname{Cov}(U,W)=-\lambda\operatorname{Var}(U)$; the first-leg noise prevents replacing this entry by a deterministic-product formula.

At $d=0$, planar Gaussian wedge probabilities give $$\begin{aligned}
 \Pr(U>0)
 &=\frac1\pi\arctan\frac1\alpha
 =0.0997061646699731\ldots,
 \label{eq:u-leak}\\
 \Pr(W<0)
 &=\frac1\pi\arctan\frac\beta\kappa_{\mathrm{aff}}
 =0.1147638712758368\ldots.
 \label{eq:w-leak}\end{aligned}$$ These are unconditional marginal probabilities. They show that the nominally negative $U$ and positive $W$ orientations both have surviving opposite-sign mass in the affine limit. They are not parity weights and do not determine a conditional branch-return probability.

# Protocol and route firewall

The reproduction code uses only the standard library. Composite Simpson quadrature checks the two closed-form marginals against their defining convolutions, their normalization and moments, the exact finite-seed tail, and the two wedge probabilities. No parameter fitting or finite-order spectral inference enters the argument.

This probability calculation must also be separated from RH-18. That paper propagates peak-normalized Gaussian observables by a backward affine operator and obtains an amplitude coefficient from peak normalization. Here every object is a forward probability density of mass one; no RH-18 packet coefficient is a probability-loss factor. RH-19 further proves that the neighboring critical sibling has order-one natural $L^2$ mass. The sibling is not contained in $J_d$ and cannot be dismissed as a Gaussian tail.

No actual finite-noise two-leg curvature or normalization remainder is proved. No parity cancellation, sibling/shell matching, moving-order Duhamel composition, branch-isolated return, full-trace replacement, or joint error $o(kR^{-2k})$ with $R=1.4$ is obtained. Gates A--E remain false/open. The paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt trace formula or zeta-divisor equality, and does not imply RH.

The next interface is RH-324: turn one tangent leg into a quantitative finite-noise physical-kernel approximation by controlling curvature, fold changes, state-boundary tails, and exact row normalization on one weighted domain. Moving-order composition begins only after that local remainder is available.
