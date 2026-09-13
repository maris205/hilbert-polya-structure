---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-two-site-inclusion-hahn-spectrum-route-a"
canonical_tex: "henon_dynamics/henon_two_site_inclusion_hahn_spectrum_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_two_site_inclusion_hahn_spectrum_route_a/paper/main.pdf"
source_sha256: "ee643cc54ecb286ac2cde5da83a2e637b63e1142b645376b2b3d09b93260d8d8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Two-Site Inclusion Process: Complete Hahn Spectrum and the Absorbing Face

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_two_site_inclusion_hahn_spectrum_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_two_site_inclusion_hahn_spectrum_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_two_site_inclusion_hahn_spectrum_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_two_site_inclusion_hahn_spectrum_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We diagonalize the convention-locked two-site symmetric inclusion process. The result includes its beta-binomial law, every Hahn mode and finite-sum norm, the full semigroup kernel, sharp $L^2$ decay, and the singular zero-parameter absorbing limit. Exact rational grids audit, but do not prove, the theorem.
author:
- 'HCS-C326 theorem-and-evidence package'
date: '3 September 2026 --- revision round '
title: |
  The Two-Site Inclusion Process:\
  Complete Hahn Spectrum and the Absorbing Face
```

## Markdown 正文

# Frozen generator and reversible law

Fix $N\in\mathbb Z_{\geq0}$ and $\alpha>0$. State $x\in S_N=\{0,\ldots,N\}$ is the first-site occupancy; the second is $N-x$. Our unscaled continuous-time generator is $$\label{eq:L}
 (Lf)(x)=b_x[f(x+1)-f(x)]+d_x[f(x-1)-f(x)],\quad
 b_x=(N-x)(\alpha+x),\quad d_x=x(\alpha+N-x),$$ with unavailable endpoint terms zero. Put $$\label{eq:pi}
 \pi(x)=\frac{N!(\alpha)_x(\alpha)_{N-x}}
 {x!(N-x)!(2\alpha)_N}.$$

[\[thm:main\]]{#thm:main label="thm:main"} For $N\geq1$, [\[eq:pi\]](#eq:pi){reference-type="eqref" reference="eq:pi"} is the unique reversible law. Define $$H_j(x)={}_3F_2\!(\begin{smallmatrix}-j,j+2\alpha-1,-x\\
                         \alpha,-N\end{smallmatrix};1),\quad
 h_j=\sum_{x=0}^N\pi(x)H_j(x)^2,\quad 0\leq j\leq N.$$ Then $h_j>0$, the $H_j$ are a complete orthogonal basis, and $$LH_j=-\lambda_jH_j,\qquad \lambda_j=j(j-1+2\alpha).$$ The complete transition kernel is $$\label{eq:kernel}
 p_t(x,y)=\pi(y)\sum_{j=0}^Ne^{-\lambda_jt}
 \frac{H_j(x)H_j(y)}{h_j}.$$ For centered $f$, $\lVert e^{tL}f\rVert_{2,\pi}\leq e^{-2\alpha t}\lVert f\rVert_{2,\pi}$; the exponent is sharp. At $\alpha=0$, the endpoints absorb, absorption is almost sure, and $\mathbb P_x(X_\infty=N)=x/N$ for $N\geq1$. Moreover $\{c\delta_0+(1-c)\delta_N:0\leq c\leq1\}$ is the complete stationary family, and $\pi_{\alpha,N}\Rightarrow(\delta_0+\delta_N)/2$ as $\alpha\downarrow0$. For $N=0$ the process and law are the singleton.

The adjacent identity $\pi(x)b_x=\pi(x+1)d_{x+1}$ follows by cancelling Pochhammer factors; Chu--Vandermonde gives the denominator in [\[eq:pi\]](#eq:pi){reference-type="eqref" reference="eq:pi"}. For $N\geq1$ all interior edge rates are positive, proving irreducibility, uniqueness, and self-adjointness in $L^2(\pi)$.

The evidence grid uses $\alpha\in\{1/2,1,3/2,2\}$ and $0\leq N\leq8$: 36 parameter rows, 180 states, and 180 full Hahn vectors. All entries are exact rationals independently reconstructed; finite evidence is not a proof.

\>0

# Full Hahn diagonalization

[\[lem:tri\]]{#lem:tri label="lem:tri"} The degree-$j$ polynomial filtration is invariant under $L$, and the diagonal entry on its one-dimensional quotient is $-j(j-1+2\alpha)$. The terminating series defining $H_j$ has degree $j$, satisfies $LH_j=-j(j-1+2\alpha)H_j$, and obeys $H_j(0)=1$.

For $f(x)=x^j$, the prospective $x^{j+1}$ terms in [\[eq:L\]](#eq:L){reference-type="eqref" reference="eq:L"} cancel. The $x^j$ coefficient is $$j[(N-\alpha)-(N+\alpha)]-j(j-1)=-j(j-1+2\alpha).$$ For identification, write the finite expression $$H_j(x)=\sum_{k=0}^j
 \frac{(-j)_k(j+2\alpha-1)_k(-x)_k}
      {(\alpha)_k(-N)_k k!}.$$ Put $\phi_k(x)=(-x)_k$. Direct forward and backward differencing gives $$L\phi_k=-k(k-1+2\alpha)\phi_k
 -k(N-k+1)(\alpha+k-1)\phi_{k-1}.$$ For $H_j=\sum_kc_k\phi_k$, the eigenvalue equation requires $$\frac{c_{k+1}}{c_k}=
 \frac{\lambda_j-\lambda_k}{(k+1)(N-k)(\alpha+k)}
 =\frac{(j-k)(j+k+2\alpha-1)}{(k+1)(N-k)(\alpha+k)}.$$ This is exactly the ratio of consecutive coefficients in the displayed terminating sum, by $(a)_{k+1}=(a+k)(a)_k$. Consequently every coefficient on the left of $$b_x[H_j(x+1)-H_j(x)]+d_x[H_j(x-1)-H_j(x)]
 +j(j-1+2\alpha)H_j(x)$$ is zero. This proves the finite difference identity. Its denominators do not vanish for $j\leq N$ and $\alpha>0$; its final coefficient is nonzero, while substitution $x=0$ gives one.

Because $\lambda_{j+1}-\lambda_j=2(j+\alpha)>0$, these are all the distinct diagonal values from Lemma [\[lem:tri\]](#lem:tri){reference-type="ref" reference="lem:tri"}. Self-adjointness makes their eigenvectors orthogonal. There are $N+1$ of them, hence they are complete, and each displayed finite-sum norm $h_j$ is positive. Expanding any function in this normalized basis proves [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"}. Parseval on the constants' orthogonal complement gives the stated bound because $\lambda_1=2\alpha$; $H_1(x)=1-2x/N$ gives equality and therefore sharpness. When $N=1$, this says exactly that the spectrum is $\{0,2\alpha\}$ and $\pi=(1/2,1/2)$.

# Revision certificate: complete Hahn spectrum and semigroup {#revision-certificate-complete-hahn-spectrum-and-semigroup .unnumbered}

This round adds polynomial triangularity, the terminating difference identity, orthogonality with positive finite-sum norms, the full kernel, and sharp decay.

\>1

# The singular face, ownership, and Route A

At $\alpha=0$, $b_x=d_x=x(N-x)$. Thus both endpoints absorb and, from an interior state, the embedded chain is the finite simple symmetric walk. Absorption is almost sure. Since $Lx=0$, bounded optional stopping yields $x=N\mathbb P_x(X_\infty=N)$. A stationary law cannot charge the transient interior: stationarity makes that mass time-independent, whereas finite-state almost-sure absorption makes it tend to zero. Thus all and only stationary laws are $c\delta_0+(1-c)\delta_N$, $0\leq c\leq1$. For fixed $N\geq1$, each endpoint numerator in [\[eq:pi\]](#eq:pi){reference-type="eqref" reference="eq:pi"} is asymptotic to $\alpha/N$, the denominator to $2\alpha/N$, and every interior numerator is $O(\alpha^2)$; this proves the weak limit. For $N=0$ only $\delta_0$ exists. At $N=1$ the hitting formula remains valid.

The inclusion model is sourced to Giardina--Redig--Vafayi [@grv]; the Hahn normalization, representation, and difference equation are checked against DLMF Sections 18.19, 18.20.5, and 18.22(ii) [@dlmf]. We claim no priority. C253 owns Moran fixation, C263 a growing Polya urn, C285 Gordon--Newell product form, and C322 Kac sphere collisions; none owns this theorem. We assert no multisite, open-boundary, or condensation-scaling result.

The Route-A tuple is $(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},
\mathrm{FAIL},\mathrm{FORMAL\ HINT})$, with verdict `ROUTE_A_REJECTED`; Route B is false. The final entry records only a finite self-adjoint spectral analogy, not a Hilbert--Polya operator. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, no target local datum, Euler factor, root number, automorphy, divisor, functional equation, or zero match is asserted.

# Revision certificate: absorbing face and scope closure {#revision-certificate-absorbing-face-and-scope-closure .unnumbered}

This final round proves absorption, hitting probabilities, the stationary weak limit, all degenerate cases, source and collision ownership, and the firewall.

# Revision certificate: frozen inclusion chain and reversible law {#revision-certificate-frozen-inclusion-chain-and-reversible-law .unnumbered}

This original round fixes the generator and clock, derives beta-binomial detailed balance, states the complete theorem, and records the exact grid.

2 C. Giardina, F. Redig, and K. Vafayi, Correlation inequalities for interacting particle systems with duality, *J. Stat. Phys.* 141 (2010); DOI: 10.1007/s10955-010-0055-0; arXiv:0906.4664. NIST Digital Library of Mathematical Functions, Sections 18.19, 18.20.5, and 18.22(ii), Hahn definitions, representation, and difference equations.
