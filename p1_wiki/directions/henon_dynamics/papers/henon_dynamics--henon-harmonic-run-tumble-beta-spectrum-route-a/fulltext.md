---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-harmonic-run-tumble-beta-spectrum-route-a"
canonical_tex: "henon_dynamics/henon_harmonic_run_tumble_beta_spectrum_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_harmonic_run_tumble_beta_spectrum_route_a/paper/main.pdf"
source_sha256: "2566fd12b19496baf84868b56a863fba37d46554d1a5a3c93b4d020eb800fe9f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Harmonic Run-and-Tumble Dynamics: Beta Stationarity, Correlations, and Polynomial Jordan Resonances

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_harmonic_run_tumble_beta_spectrum_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_harmonic_run_tumble_beta_spectrum_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_harmonic_run_tumble_beta_spectrum_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_harmonic_run_tumble_beta_spectrum_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close the invariant law of a one-dimensional harmonic run-and-tumble particle, including its two orientation components and every polynomial moment. \>0 The full stationary two-by-two correlation matrix is explicit, with its coalescent Jordan formula at $\mu=2\lambda$. \>1 Every finite polynomial filter is classified: for $v>0$, integer $2\lambda/\mu$ produces size-two Jordan blocks exactly at odd integers, whereas even integers are semisimple. No full $L^2$ spectrum is claimed.
author:
- 'Route-A source-local certificate HCS-C328'
date: 3 September 2026
title: |
  Harmonic Run-and-Tumble Dynamics:\
  Beta Stationarity, Correlations, and Polynomial Jordan Resonances
```

## Markdown 正文

trailerid \[\<C3282026090300000000000000000000\>\<C3282026090300000000000000000000\>\]

# Stationary beta law and all moments

Let $\sigma_t\in\{-1,1\}$ flip to its opposite at rate $\lambda$, and let $$\label{eq:model}
 dx_t=(v\sigma_t-\mu x_t)\,dt,
 \qquad \mu,v,\lambda>0.$$ The generator is $$Lf_\sigma=(v\sigma-\mu x)\partial_xf_\sigma
 +\lambda(f_{-\sigma}-f_\sigma).$$ Set $a=v/\mu$, $y=x/a$, and $\alpha=\lambda/\mu$.

[\[thm:stationary\]]{#thm:stationary label="thm:stationary"} The process has a unique stationary probability on $[-a,a]\times\{-1,1\}$. With respect to $dy$, its marginal and joint component densities are $$\begin{aligned}
 p(y)&=\frac{\Gamma(\alpha+\tfrac12)}
 {\sqrt\pi\,\Gamma(\alpha)}(1-y^2)^{\alpha-1},\label{eq:beta}\\
 p_+(y)&=\frac{1+y}{2}p(y),&
 p_-(y)&=\frac{1-y}{2}p(y).\label{eq:components}\end{aligned}$$ For every $n\geq0$, $$\begin{aligned}
 \mathbb Ex^{2n}&=a^{2n}\frac{(1/2)_n}{(\alpha+1/2)_n},&
 \mathbb Ex^{2n+1}&=0,\label{eq:moments}\\
 \mathbb E(\sigma x^{2n})&=0,&
 \mathbb E(\sigma x^{2n+1})
 &=a^{2n+1}\frac{(1/2)_{n+1}}{(\alpha+1/2)_{n+1}}.\end{aligned}$$

The deterministic vector fields point inward at $\pm a$. In stationarity, adding the two forward equations makes total probability flux constant; the no-flux boundary gives $(1-y)p_+-(1+y)p_-=0$. Hence [\[eq:components\]](#eq:components){reference-type="eqref" reference="eq:components"} holds. Substitution in either remaining equation gives $p'/p=-2(\alpha-1)y/(1-y^2)$, and beta normalization gives [\[eq:beta\]](#eq:beta){reference-type="eqref" reference="eq:beta"}. Positive flip rate makes the compact process irreducible in its accessible interior, giving uniqueness. Symmetry gives odd moments zero. Finally, integration by parts applied to $y^{2n+1}(1-y^2)^\alpha$ yields $$\frac{\mathbb Ey^{2n+2}}{\mathbb Ey^{2n}}
 =\frac{n+1/2}{n+\alpha+1/2},$$ The component imbalance in [\[eq:components\]](#eq:components){reference-type="eqref" reference="eq:components"} is $yp(y)$, so parity gives every even mixed moment zero and the displayed odd mixed moments.

\>0

# Complete stationary correlation matrix

For $t\geq0$, put $Z=(x,\sigma)^{\mathsf T}$ and $R(t)=\mathbb E[Z_tZ_0^{\mathsf T}]$. Since $Lx=-\mu x+v\sigma$ and $L\sigma=-2\lambda\sigma$, $$\label{eq:R}
 R(t):=\mathbb E[Z_tZ_0^{\mathsf T}]=e^{At}\Sigma,\quad
 A=\begin{pmatrix}-\mu&v\\0&-2\lambda\end{pmatrix},\quad
 \Sigma=\begin{pmatrix}
 \dfrac{v^2}{\mu(\mu+2\lambda)}&\dfrac v{\mu+2\lambda}\\[3pt]
 \dfrac v{\mu+2\lambda}&1
 \end{pmatrix}.$$ For $\mu\ne2\lambda$, the upper-right entry of $e^{At}$ is $$b(t)=v\frac{e^{-2\lambda t}-e^{-\mu t}}{\mu-2\lambda}.$$ Thus all four entries are fixed by [\[eq:R\]](#eq:R){reference-type="eqref" reference="eq:R"}; explicitly, $$\begin{aligned}
 R_{xx}(t)&=\frac{v^2[\mu e^{-2\lambda t}
       -2\lambda e^{-\mu t}]}
 {\mu(\mu+2\lambda)(\mu-2\lambda)},\label{eq:cxx}\\
 R_{x\sigma}(t)&=e^{-\mu t}\frac v{\mu+2\lambda}+b(t),\nonumber\\
 R_{\sigma x}(t)&=e^{-2\lambda t}\frac v{\mu+2\lambda},&
 R_{\sigma\sigma}(t)&=e^{-2\lambda t}.\end{aligned}$$ On the Jordan face $\mu=2\lambda$, $b(t)=vt e^{-\mu t}$ and $$\label{eq:jordan-corr}
 R_{xx}(t)=\frac{v^2(1+\mu t)e^{-\mu t}}{2\mu^2}.$$ These are removable limits, not an omitted parameter case. For negative lag, stationarity gives the separate convention $R(-t)=R(t)^{\mathsf T}$ for $t\geq0$; the one-sided semigroup formula in [\[eq:R\]](#eq:R){reference-type="eqref" reference="eq:R"} is not applied with negative time.

At $\mu=0$ there is no compact stationary probability on the line. At $\lambda=0$, arbitrary mixtures of the two attracting endpoint atoms are stationary. At $v=0$ with $\lambda>0$, the joint stationary law is $\delta_0$ tensored with uniform orientations; the polynomial couplings below disappear and all repeated diagonal values are semisimple. At the intersection $v=\lambda=0$, orientation is frozen and every orientation mixture over $\delta_0$ is stationary. For positive parameters the density in [\[eq:beta\]](#eq:beta){reference-type="eqref" reference="eq:beta"} diverges, is uniform, or vanishes at the endpoints according as $\alpha<1$, $\alpha=1$, or $\alpha>1$; it has no endpoint atoms.

\>1

# Every finite polynomial filter

Let $$A_n=x^n,\qquad B_n=\sigma x^n,\qquad
 \mathcal P_N=\operatorname{span}\{A_n,B_n:0\leq n\leq N\}.$$ Direct application of the generator gives $$\label{eq:ladder}
 LA_n=-n\mu A_n+nvB_{n-1},\qquad
 LB_n=-(n\mu+2\lambda)B_n+nvA_{n-1},$$ with the negative-index terms absent.

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} Every $\mathcal P_N$ is invariant and $$\det(z-L|_{\mathcal P_N})=
 \prod_{n=0}^N(z+n\mu)\prod_{n=0}^N(z+n\mu+2\lambda).$$ If $2\lambda/\mu\notin\mathbb N$, all roots are simple. If $2\lambda/\mu=k\in\mathbb N$ and $v>0$, the repeated pair $A_n,B_{n-k}$ occurs for every $k\leq n\leq N$. Each pair forms one size-two Jordan block when $k$ is odd, while both eigenvectors survive and the repeated eigenvalue is semisimple when $k$ is even.

Equation [\[eq:ladder\]](#eq:ladder){reference-type="eqref" reference="eq:ladder"} proves invariance and triangularity. Split by the involution $(x,\sigma)\mapsto(-x,-\sigma)$. In either parity sector, ordering by descending degree makes $L$ bidiagonal, and every available off-diagonal coefficient is nonzero because $v>0$. The parity of $A_n$ is $(-1)^n$, whereas that of $B_{n-k}$ is $(-1)^{n-k+1}$. The repeated pair therefore lies in the same bidiagonal chain exactly for odd $k$. In that case the unique nonzero connecting path leaves geometric multiplicity one. For even $k$ the pair lies in different parity chains; within either chain the diagonal entries are distinct, so each chain is diagonalizable and the combined geometric multiplicity is two.

The certificate records 12 parameter triples through degree eight: 108 moment rows, 60 correlation rows, 216 spectral cells, 33 resonances, and 1,989 scalar leaves. An independent checker performs 2,226 checks and computes exact rational nullities; SymPy closes 61 identities. Two isolated replays are byte exact and 66 hostile attacks are rejected. The grid is a regression; Theorems [\[thm:stationary\]](#thm:stationary){reference-type="ref" reference="thm:stationary"}--[\[thm:spectrum\]](#thm:spectrum){reference-type="ref" reference="thm:spectrum"} are analytic for all declared parameters and finite $N$.

The closest registered systems are C213, an unconfined circular telegraph process with Fourier blocks; C237, Gaussian harmonic Kramers--Langevin dynamics; and C265, a self-exciting affine Hawkes jump process.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, every Route-A layer fails. There is no arithmetic prime owner, primitive deterministic orbit ledger, Euler product, target determinant, functional equation, counting law, target-zero match, natural self-adjoint lift, or Hilbert--Pólya operator. Route A is rejected and Route B stays locked. No full $L^2$ spectrum, target local data, root number, or automorphy is claimed.

#### AI use.

A generative language model assisted drafting and code scaffolding. The proofs, independent recomputation, hostile tests, and deterministic artifacts define the audit record.

# Source lineage {#source-lineage .unnumbered}

9 A. Dhar, A. Kundu, S. N. Majumdar, S. Sabhapandit, and G. Schehr, "Run-and-tumble particle in one-dimensional confining potentials: steady-state, relaxation and first-passage properties," *Phys. Rev. E* 99 (2019), 032132. DOI: [10.1103/PhysRevE.99.032132](https://doi.org/10.1103/PhysRevE.99.032132). R. Garcia-Millan and G. Pruessner, "Run-and-tumble motion in a harmonic potential: field theory and entropy production," *J. Stat. Mech.* (2021), 063203. DOI: [10.1088/1742-5468/ac014d](https://doi.org/10.1088/1742-5468/ac014d).
