---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-bilinear-two-stiffness-isochronous-oscillator-route-a"
canonical_tex: "henon_dynamics/henon_bilinear_two_stiffness_isochronous_oscillator_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_bilinear_two_stiffness_isochronous_oscillator_route_a/paper/main.pdf"
source_sha256: "0afaf890b76f1ab1bc27186abbe11e9f09b3ea7f19472e7ba29e05d09c7e4725"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Bilinear Isochronous Oscillator: Global Action--Angle Coordinates and Quantum Interface Spectrum

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_bilinear_two_stiffness_isochronous_oscillator_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_bilinear_two_stiffness_isochronous_oscillator_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_bilinear_two_stiffness_isochronous_oscillator_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_bilinear_two_stiffness_isochronous_oscillator_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close the classical and quantum dynamics of a joined pair of quadratic half-wells. Every nonzero classical orbit has one energy-independent least period exactly when both stiffnesses are positive. Its global action--angle chart is $C^1$ and piecewise analytic, but detects unequal stiffness at second order. The natural Friedrichs quantization has simple discrete spectrum characterized completely by a parabolic-cylinder interface Wronskian. Flat-side, free, zero-energy, and equal-frequency boundaries are kept explicit.
author:
- 'Source-local theorem reconstruction'
date: '2026-09-03'
title: 'A Bilinear Isochronous Oscillator: Global Action--Angle Coordinates and Quantum Interface Spectrum'
```

## Markdown 正文

trailerid \[\<C3572026090300000000000000000000\>\<C3572026090300000000000000000000\>\]

# The common-period owner

For $x_+=\max\{x,0\}$, $x_-=\min\{x,0\}$, and $\omega_+,\omega_-\geq0$, consider $$H(x,p)=\frac{p^2}{2}+V(x),\qquad
 V(x)=\frac{\omega_+^2x_+^2+\omega_-^2x_-^2}{2}.               \tag{1}$$ The force is continuous and globally Lipschitz, hence the flow is unique and complete, and $H$ is conserved.

[\[thm:classical\]]{#thm:classical label="thm:classical"} Every nonzero orbit of (1) is bounded and periodic with a common least period if and only if $\omega_+,\omega_->0$. In that chamber, $$T=\pi\left(\frac1{\omega_+}+\frac1{\omega_-}\right),\qquad
 J(E)=\frac E2\left(\frac1{\omega_+}+\frac1{\omega_-}\right),
 \qquad
 \Omega=\frac{dE}{dJ}=\frac2{1/\omega_++1/\omega_-}.           \tag{2}$$

At $E>0$, write $B=\sqrt{2E}$ and start at $(0,B)$. The right half-excursion is $$x=\frac B{\omega_+}\sin(\omega_+t),\quad
 p=B\cos(\omega_+t),\quad 0\leq t\leq\frac\pi{\omega_+}.$$ Starting next from $(0,-B)$, with $s=t-\pi/\omega_+$, the left one is $$x=-\frac B{\omega_-}\sin(\omega_-s),\quad
 p=-B\cos(\omega_-s),\quad 0\leq s\leq\frac\pi{\omega_-}.$$ They give the least period in (2). Their two half-ellipse areas are $\pi E/\omega_+$ and $\pi E/\omega_-$, proving the action formula. If a frequency vanishes, an orbit entering that flat half-axis with nonzero speed escapes linearly; if both vanish the motion is free. This proves the necessity.

\>0

# Seam-compatible action--angle coordinates

Put $\theta_+=\pi\Omega/\omega_+$, $B=\sqrt{2\Omega J}$, and measure $\theta=\Omega t$ from $(0,p>0)$. The inverse chart is $$\begin{array}{ll}
0\leq\theta\leq\theta_+:&
x=\dfrac B{\omega_+}\sin\dfrac{\omega_+\theta}{\Omega},\quad
p=B\cos\dfrac{\omega_+\theta}{\Omega},\\[6pt]
\theta_+\leq\theta\leq2\pi:&
x=-\dfrac B{\omega_-}\sin\dfrac{\omega_-(\theta-\theta_+)}{\Omega},\quad
p=-B\cos\dfrac{\omega_-(\theta-\theta_+)}{\Omega}.
\end{array}                                                    \tag{3}$$ Values and first $J,\theta$ derivatives agree at the two seams. On each open piece, $$x_\theta p_J-x_Jp_\theta=1,$$ so (3) is a global $C^1$, piecewise-analytic symplectic chart from $(0,\infty)\times\mathbb{R}/(2\pi\mathbb Z)$ to the punctured plane, with $dx\wedge dp=d\theta\wedge dJ$ and $\dot\theta=\Omega$. At $\theta_+$, the one-sided values of $p_{\theta\theta}$ are $B(\omega_+/\Omega)^2$ and $B(\omega_-/\Omega)^2$; the chart is not $C^2$ unless the frequencies agree. Each normalized seam-to-seam half-flow matrix is $-I_2$. Thus the common-period map and its derivative are exactly $I_2$. This is the seam-compatible action-angle owner.

\>1

# Friedrichs quantization and interface Wronskian

Let $\mathcal H$ be the Friedrichs operator of $$\mathfrak q[\psi]=\frac12\int_{\mathbb{R}}|\psi'|^2\,dx+\int_{\mathbb{R}} V|\psi|^2\,dx.$$ For positive frequencies, $V(x)\geq\min(\omega_+^2,\omega_-^2)x^2/2$. Rellich compactness locally and this tail bound make the form-domain embedding compact. Hence $\mathcal H$ is self-adjoint with compact resolvent.

[\[thm:quantum\]]{#thm:quantum label="thm:quantum"} Put $\nu_\pm(\lambda)=\lambda/\omega_\pm-1/2$. The spectrum of $\mathcal H$ consists of simple real eigenvalues tending to infinity, and $\lambda\in\mathbb{R}$ is an eigenvalue if and only if $$\sqrt{\omega_+}D'_{\nu_+}(0)D_{\nu_-}(0)
 +\sqrt{\omega_-}D'_{\nu_-}(0)D_{\nu_+}(0)=0.                  \tag{4}$$

Up to scalars, the unique decaying half-line solutions are $$D_{\nu_+}(\sqrt{2\omega_+}\,x)\quad(x>0),\qquad
 D_{\nu_-}(-\sqrt{2\omega_-}\,x)\quad(x<0).$$ Operator-domain functions and their first derivatives are continuous at zero. The determinant of these two matching conditions, after cancelling $\sqrt2$, is exactly (4), including its plus sign. Thus (4) is necessary and sufficient. Compact self-adjointness supplies the complete discrete spectrum. Two eigenfunctions for one eigenvalue have constant Wronskian, which vanishes at infinity, so they are proportional.

If $\omega_+=\omega_-=\omega$, (4) is $2\sqrt\omega D_\nu(0)D'_\nu(0)=0$. The exact gamma-function values at zero show that its zeros are precisely $\nu=0,1,2,\ldots$, recovering $\lambda_n=\omega(n+1/2)$. Classical isochrony does not assert this ladder when the frequencies differ.

# Boundaries, evidence, and scope

For positive stiffnesses, $E=0$ is only the origin and is omitted from the chart. If exactly one stiffness vanishes, the flat half-axis is a continuum of rest equilibria and other classical trajectories escape. Quantum compact resolvent is lost; nonnegativity, flat-side Weyl sequences, and the absence of an $L^2$ affine or oscillatory flat-side solution show that the spectrum as a set is $[0,\infty)$ with no eigenvalues. If both vanish, this is the free particle. No globally $C^\infty$ seam claim is made.

Exact finite receipts check 60 rational energy/frequency rows, 85 harmonic levels, both half-flow matrices, and all zero-stiffness faces. Analytic arguments, not finite rows, prove the continuum and operator theorems. Dorignac supplies model lineage and the classical/quantum warning [@Dorignac]; DLMF fixes the Weber convention [@DLMF]; Teschl supplies the one-dimensional self-adjoint framework [@Teschl]. The formulas and software are independently reconstructed without a priority claim.

The Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_PASS\_ANALYTIC},\mathrm{A2\_FAIL},
 \mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION});$$ the overall verdict is rejection. Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is false. The source interface Wronskian is not a target determinant, target-zero match, or Hilbert--Pólya operator. No target local data, Euler factor, root number, automorphy, target divisor, or target functional equation is claimed.

9 J. Dorignac, *On the quantum spectrum of isochronous potentials*, *J. Phys. A* 38 (2005), 6183--6210. DOI: [10.1088/0305-4470/38/27/007](https://doi.org/10.1088/0305-4470/38/27/007). NIST Digital Library of Mathematical Functions, [Chapter 12, Section 12.2](https://dlmf.nist.gov/12.2). G. Teschl, *Mathematical Methods in Quantum Mechanics*, 2nd ed., AMS GSM 157, 2014. DOI: [10.1090/gsm/157](https://doi.org/10.1090/gsm/157).
