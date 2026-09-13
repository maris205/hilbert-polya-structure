---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-cir-square-root-diffusion-affine-spectral-route-a"
canonical_tex: "henon_dynamics/henon_cir_square_root_diffusion_affine_spectral_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_cir_square_root_diffusion_affine_spectral_route_a/paper/main.pdf"
source_sha256: "7340e8f1ae24b7ae02d09c281f956f2ba6cf080e702cb843ea969f311e5711ca"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An All-Face Affine and Laguerre Theorem for the CIR Square-Root Diffusion

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_cir_square_root_diffusion_affine_spectral_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_cir_square_root_diffusion_affine_spectral_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_cir_square_root_diffusion_affine_spectral_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_cir_square_root_diffusion_affine_spectral_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close one theorem across the full nonnegative parameter cone of the Cox--Ingersoll--Ross square-root diffusion. The scale/speed test separates the entrance face $2\kappa\theta\geq\sigma^2$ from the regular, instantaneously reflecting face, while zero-dimensional and zero-noise faces are treated as distinct degenerations. A single affine Riccati flow gives all Laplace transforms and, in the interior, the noncentral chi-square transition law. The invariant Gamma law puts the generator in Laguerre form: the exact reversible kernel, sharp gap $\kappa$, and $L^2$/chi-square/TV contraction follow from one orthogonal expansion. This is a stochastic Markov-semigroup result, not a primitive-orbit zeta or a Hilbert--Pólya construction. Independent exact reconstruction (235 assertions), symbolic identities (18), byte replay and 20 hostile mutations audit the certificate.
author:
- HCS Research Program
date: 29 August 2026(revision 2)
title: 'An All-Face Affine and Laguerre Theorem for the CIR Square-Root Diffusion'
```

## Markdown 正文

suppressoptionalinfo 611

# Object and boundary atlas

We freeze, in physical time $t\geq0$, $$dX_t=\kappa(\theta-X_t)\,dt+\sigma\sqrt{X_t}\,dW_t,
 \qquad X_0=x\geq0,\quad \kappa,\theta,\sigma\geq0 . \tag{1}$$ The square-root modulus gives a unique nonnegative strong solution. The interior generator is $\mathcal Lf=\kappa(\theta-x)f'+(\sigma^2/2)xf''$.

[\[thm:feller\]]{#thm:feller label="thm:feller"} Assume $\kappa,\theta,\sigma>0$ and write $\alpha=2\kappa\theta/\sigma^2$. The origin is an entrance (hence inaccessible from $x>0$) iff $\alpha\geq1$, including equality $2\kappa\theta=\sigma^2$. If $0<\alpha<1$, it is regular and the canonical CIR solution is instantaneously reflecting. If $\theta=0$ or $\kappa=0$ with $\sigma>0$, the dimension is zero and $0$ is absorbing. If $\sigma=0$ and $\kappa>0$, the path is deterministic, $X_t=\theta+(x-\theta)e^{-\kappa t}$; when also $\theta=0$ it decays toward the absorbing origin. If $\kappa=\sigma=0$, every starting point is constant.

Near zero the scale density is proportional to $x^{-\alpha}$ and the speed density to $x^{\alpha-1}$. The scale integral diverges exactly for $\alpha\geq1$, while the speed integral is finite for every $\alpha>0$; Feller's test gives entrance versus regular. At dimension zero the SDE has no inward drift at the boundary and pathwise uniqueness makes it absorbing. Setting $\sigma=0$ reduces (1) to the displayed ODE, which also resolves the remaining faces.

# Affine transform and transition law

For $u\geq0$, use $\mathbb E_xe^{-uX_t}=\exp[-\phi_t(u)-\psi_t(u)x]$. Substitution in the backward equation gives $$\psi'=-\kappa\psi-\tfrac12\sigma^2\psi^2,\quad
 \phi'=\kappa\theta\psi,\qquad \psi(0)=u,\ \phi(0)=0. \tag{2}$$ For $\kappa,\sigma>0$, put $h_t=\sigma^2(1-e^{-\kappa t})/(2\kappa)$; then $$\psi_t=\frac{ue^{-\kappa t}}{1+h_tu},\qquad
 \phi_t=\frac{2\kappa\theta}{\sigma^2}\log(1+h_tu). \tag{3}$$ The continuous faces are $\psi=u/(1+\sigma^2tu/2),\phi=0$ for $\kappa=0$, and $\psi=ue^{-\kappa t},\phi=\theta u(1-e^{-\kappa t})$ for $\sigma=0$; with both rates zero, $(\phi,\psi)=(0,u)$.

Equation (3) is equivalently $$X_t=c_t\,\chi'^2_{\,4\kappa\theta/\sigma^2}(\lambda_t),\quad
 c_t=\frac{\sigma^2(1-e^{-\kappa t})}{4\kappa},\quad
 \lambda_t=\frac{4\kappa e^{-\kappa t}x}{\sigma^2(1-e^{-\kappa t})}. \tag{4}$$ For dimension zero, (4) is interpreted with its atom at zero; for example when $\theta=0$, $\mathbb P_x(X_t=0)=\exp[-xe^{-\kappa t}/h_t]$.

# Gamma law, Laguerre kernel and gap

On the positive interior set $\beta=\sigma^2/(2\kappa)$. The density $$\pi(x)=\frac{x^{\alpha-1}e^{-x/\beta}}{\Gamma(\alpha)\beta^\alpha}
 \tag{5}$$ is invariant and unique; its mean and variance are $\theta$ and $\theta\sigma^2/(2\kappa)$. With $z=x/\beta$, $$\mathcal L=\kappa\{z\partial_z^2+(\alpha-z)\partial_z\}. \tag{6}$$ The Laguerre equation and orthogonality are $$zL_n''+(\alpha-z)L_n'+nL_n=0,\qquad
 \int_0^\infty L_nL_m z^{\alpha-1}e^{-z}dz
 =\frac{\Gamma(n+\alpha)}{n!}\delta_{nm}.$$ Consequently, for $t>0$ the exact reversible transition kernel is $$p_t(x,y)=\pi(y)K_t(x,y),\quad
 K_t=\sum_{n\geq0}e^{-\kappa nt}\frac{n!\Gamma(\alpha)}{\Gamma(n+\alpha)}
 L_n^{(\alpha-1)}(x/\beta)L_n^{(\alpha-1)}(y/\beta). \tag{7}$$

[\[prop:gap\]]{#prop:gap label="prop:gap"} For $f\in L^2(\pi)$, $$\operatorname{Var}_\pi(P_tf)\leq e^{-2\kappa t}\operatorname{Var}_\pi(f).$$ If $d\mu/d\pi\in L^2(\pi)$, then $\chi^2(\mu P_t\,||\,\pi)\leq e^{-2\kappa t}\chi^2(\mu\,||\,\pi)$ and $\|\mu P_t-\pi\|_{\rm TV}\leq\tfrac12e^{-\kappa t}
\sqrt{\chi^2(\mu\,||\,\pi)}$. The first Laguerre mode attains equality, so the gap is exactly $\kappa$.

Equation (6) is symmetric in $L^2(\pi)$ and (7) diagonalizes its closure. All nonconstant modes have eigenvalues at most $-\kappa$; Parseval gives the variance and chi-square bounds, and Cauchy--Schwarz gives TV. The mode $L_1^{(\alpha-1)}=\alpha-z$ has eigenvalue $-\kappa$.

\>0

# Controls and claim boundary

The certificate freezes eight rational boundary controls, seven transform controls and three Gamma controls, together with nine Laguerre modes, three kernel rows, five gap rows and three dimension-zero atom rows. The noncentral-chi-square and Gamma statements are exact identities; decimals are only 90-digit regression serialization. Cox--Ingersoll--Ross [(1985)](https://doi.org/10.2307/1911252), Feller [(1951)](https://doi.org/10.2307/1906748), and standard square-root diffusion analyses provide context, not hidden data.

\>1

# Reproducibility and Route-A result

The producer-independent checker passes 235 assertions; SymPy reconstructs 18 generic identities; clean replay is byte identical; and 20/20 repaired-hash, schema, numeric, provenance and scope mutations are rejected. The two substantive revisions and fixed-epoch double builds are recorded beside this PDF.

The strict evaluator tuple is $$(\mathtt{A0\_FAIL},\mathtt{A1\_FAIL},\mathtt{A2\_FAIL},\mathtt{A3\_FAIL},
 \mathtt{A4\_FORMAL\_HINT}),\qquad
\mathtt{overall=ROUTE\_A\_REJECTED}.$$ The Laguerre modes are stochastic semigroup modes, not primitive arithmetic orbits; (7) is not a target Fredholm determinant, and no analytic continuation, arithmetic counting law, Euler factor, target divisor or Hilbert--Pólya operator is claimed. Route B is false.

9 J. C. Cox, J. E. Ingersoll and S. A. Ross, "A Theory of the Term Structure of Interest Rates," *Econometrica* 53 (1985), 385--407. [DOI](https://doi.org/10.2307/1911252). W. Feller, "Two singular diffusion problems," *Annals of Mathematics* 54 (1951), 173--182. [DOI](https://doi.org/10.2307/1969318). A. Alfonsi, "High order discretization schemes for the CIR process," *Monte Carlo Methods and Applications* 16 (2010), 1--28. [DOI](https://doi.org/10.1090/S0025-5718-09-02252-2).

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic, Euler-factor, target-zero, automorphy, or Hilbert--Pólya claim. **Data and code.** All exact formulas, ledgers and audit programs accompany HCS-C229. **AI-use disclosure.** Generative tools assisted drafting and code generation; internal checks validate the displayed identities. This is not external peer review.
