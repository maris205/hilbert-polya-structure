---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-cubic-nls-soliton-hessian-route-a"
canonical_tex: "henon_dynamics/henon_cubic_nls_soliton_hessian_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_cubic_nls_soliton_hessian_route_a/paper/main.pdf"
source_sha256: "a60dd4286fc88af3435768a100629f9fc850b75a357e480ac9dfca66d8024a74"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Focusing Cubic NLS Soliton: Exact Hessian Spectrum and Pöschl--Teller Factorization

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_cubic_nls_soliton_hessian_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_cubic_nls_soliton_hessian_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_cubic_nls_soliton_hessian_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_cubic_nls_soliton_hessian_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close a convention-locked one-dimensional theorem for the focusing cubic nonlinear Schrödinger equation. The sech standing wave has exact mass, Hamiltonian, action and Vakhitov--Kolokolov (VK) slope. Its two real Hessians have the complete Pöschl--Teller discrete spectrum, essential threshold, kernels and Morse index. The zero-frequency and defocusing faces are separated, and no finite-box spectrum or arithmetic interpretation is used. \>0 The variational scaling and explicit eigenfunctions are included. \>1 The ladder factorization, boundary ledger, independent evidence counts and strict Route-A stop are included.
author:
- 'Route-A structural certificate HCS-C221'
title: |
  The Focusing Cubic NLS Soliton:\
  Exact Hessian Spectrum and Pöschl--Teller Factorization
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** nonlinear Schrödinger; soliton; Hessian; Pöschl--Teller; Morse index; Route A.

# Equation and standing wave

We study $$i\psi_t+\psi_{xx}+2|\psi|^2\psi=0,
 \qquad \psi(t,x)=e^{i\omega t}Q_\omega(x),\qquad \omega>0,$$ on $\mathbb R$. Direct differentiation of $Q_\omega(x)=\sqrt\omega\operatorname{sech}(\sqrt\omega x)$ gives $$-Q_\omega''+\omega Q_\omega-2Q_\omega^3=0.$$ For $$M(u)=\int_\mathbb R|u|^2dx,\quad
 H(u)=\tfrac12\int_\mathbb R|u_x|^2dx-\tfrac12\int_\mathbb R|u|^4dx,
 \quad S_\omega=H+\tfrac\omega2M,$$ the substitution $y=\sqrt\omega x$, $z=\tanh y$ yields $$M(Q_\omega)=2\sqrt\omega,\quad
 \|Q_\omega'\|_2^2=\tfrac23\omega^{3/2},\quad
 \|Q_\omega\|_4^4=\tfrac43\omega^{3/2},$$ and hence $$H(Q_\omega)=-\tfrac13\omega^{3/2},\qquad
 S_\omega(Q_\omega)=\tfrac23\omega^{3/2},\qquad
 \frac{d}{d\omega}M(Q_\omega)=\omega^{-1/2}>0.$$

# The complete Hessian spectrum

The real and imaginary second variations are the self-adjoint operators $$L_+=-\partial_x^2+\omega-6\omega\operatorname{sech}^2(\sqrt\omega x),\qquad
 L_-=-\partial_x^2+\omega-2\omega\operatorname{sech}^2(\sqrt\omega x).$$ The theorem is $$\sigma_{\rm ess}(L_+)=\sigma_{\rm ess}(L_-)=[\omega,\infty),
 \quad \sigma_{\rm disc}(L_+)=\{-3\omega,0\},
 \quad \sigma_{\rm disc}(L_-)=\{0\}.$$ The $-3\omega$ eigenfunction is $\operatorname{sech}^2(\sqrt\omega x)$; the zero eigenfunctions are $Q_\omega'$ for $L_+$ and $Q_\omega$ for $L_-$. All listed eigenvalues are simple. Thus $L_+$ has Morse index one and kernel $\operatorname{span}\{Q_\omega'\}$, while $L_-\ge0$ and has kernel $\operatorname{span}\{Q_\omega\}$.

To see the signs without a box discretization, put $y=\sqrt\omega x$ and $$A_\ell=\partial_y+\ell\tanh y,\qquad
 A_\ell^*=-\partial_y+\ell\tanh y.$$ Multiplication gives $$-\partial_y^2+1-6\operatorname{sech}^2y=A_2^*A_2-3,
 \qquad -\partial_y^2+1-2\operatorname{sech}^2y=A_1^*A_1.$$ The $\ell=1,2$ ladder has exactly the bound states displayed in (6); the free remainder starts at one, which rescales to the threshold $\omega$.

\>0

# Boundaries and evidence

At $\omega\downarrow0$, the profile and discrete eigenvalues collapse to the essential threshold. Reversing the cubic sign has no nonzero bright $H^1$ sech branch. A periodic domain gives elliptic/cnoidal waves, and dimensions $d\ge2$ have different criticality; neither is silently included. \>1 The executable receipt contains 15 profile, 3 integral, 15 spectral and 15 factorization rows. An independent checker passes 497 assertions, SymPy passes 19 identities, replay is byte exact, and 17 repaired/stale-hash hostile mutations are rejected. These rows are regression evidence only; they do not prove the continuum statement by sampling. In particular, no full nonlinear orbital-stability theorem is asserted.

# Strict Route-A boundary

The continuum NLS coefficients carry no intrinsic rational-prime or prime-power clock, and the standing-wave symmetry supplies only a weak relative orbit hint. The strict tuple is $$(A0,A1,A2,A3,A4)=\texttt{(A0\_FAIL,A1\_WEAK,A2\_FAIL,A3\_FAIL,}
 \texttt{A4\_NATURAL\_QUANTIZATION)}.$$ The result is `ROUTE_A_REJECTED`; Route B is disabled. The final entry records only a natural Hamiltonian quantization hint, not a Hilbert--Pólya operator. Hessian traces and continuous spectra are not dynamical zeta functions, Euler factors or target divisors. The locked scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`. The source baseline lock for this round is `86c7bb8a39cdd1b8e941e45833b068170ca06287`.

The source-attributed references are Zakharov--Shabat [\[ZS72\]](https://www.jetp.ras.ru/cgi-bin/dn/e_034_01_0062), Weinstein [\[Weinstein85\]](https://doi.org/10.1137/0516034), and the historical Pöschl--Teller solvable-potential/ladder source [\[PT33\]](https://doi.org/10.1007/BF01331132); no priority claim is made.

#### Revision focus.

Round 0 freezes (1)--(2) and the operator owner.

#### Revision focus.

Round 1 adds (3)--(6), explicit kernels and the zero-frequency/defocusing boundary.

#### Revision focus.

Round 2 adds factorization (7), all scope faces, independent evidence counts, provenance and the strict Route-A stop.

3 V. E. Zakharov and A. B. Shabat, "Exact theory of two-dimensional self-focusing and one-dimensional self-modulation of waves in nonlinear media," *Soviet Physics JETP* 34 (1972), 62--69. [Official record](https://www.jetp.ras.ru/cgi-bin/dn/e_034_01_0062). M. I. Weinstein, "Modulational Stability of Ground States of Nonlinear Schrödinger Equations," *SIAM J. Math. Anal.* 16 (1985), 472--491. DOI: [10.1137/0516034](https://doi.org/10.1137/0516034). G. Pöschl and E. Teller, "Bemerkungen zur Quantenmechanik des anharmonischen Oszillators," *Zeitschrift für Physik* 83 (1933), 143--151. DOI: [10.1007/BF01331132](https://doi.org/10.1007/BF01331132). Cited only as the historical solvable Pöschl--Teller potential/ladder source.

# Declarations {#declarations .unnumbered}

**Data and code.** Synthetic exact probes and package-local deterministic code accompany the manuscript; no training data are used. **Ethics/funding.** No human or animal data; no external funding reported. **AI disclosure.** An AI coding assistant supported drafting and exact-code development; it was not an external reviewer or independent error process.
