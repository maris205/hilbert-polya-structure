---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-couette-shear-enhanced-dissipation-route-a"
canonical_tex: "henon_dynamics/henon_couette_shear_enhanced_dissipation_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_couette_shear_enhanced_dissipation_route_a/paper/main.pdf"
source_sha256: "59e0a850ca773de1b7293ff1e16ef8f31a61c5be0e490d2ddfb9b88b7c18aace"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Couette Shear on the Infinite Periodic Channel: Exact Fourier Semigroup, Sharp Enhanced Dissipation, and Every Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_couette_shear_enhanced_dissipation_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_couette_shear_enhanced_dissipation_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_couette_shear_enhanced_dissipation_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_couette_shear_enhanced_dissipation_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every real shear $a$, viscosity $\nu\ge0$, and physical time, we derive the complete Fourier semigroup of scalar Couette advection--diffusion on $\mathbb T\times\mathbb R$. Completing one exact quadratic integral gives the exact and sharp $k$-sector norm $\exp\{-\nu(k^2t+a^2k^2t^3/12)\}$ and its cubic enhanced-dissipation scale, together with the precise norm-attainment boundary. We prove composition, inviscid unitary mixing, all no-shear/zero-mode/zero-time boundaries, the full $L^2$ periodic-state classification, and noncompactness excluding an ordinary Fredholm determinant. Finite exact cells audit conventions but do not prove the continuous theorem. The inviscid unitary is only a formal lift: all arithmetic and determinant gates fail, so Route A is rejected.
author:
- 'Route-A structural certificate C206'
title: |
  Couette Shear on the Infinite Periodic Channel:\
  Exact Fourier Semigroup, Sharp Enhanced Dissipation, and Every Boundary
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** Couette flow; shear mixing; enhanced dissipation; Fourier semigroup; noncompactness.

chinese-simplified

中文摘要

本文对无限周期通道上的[Couette]{lang="en"}对流扩散方程给出全部实剪切、非负黏性与物理时间下的精确傅里叶半群。一次平方配方得到精确且尖锐的扇区范数、范数取等边界和三次增强耗散尺度，并统一处理无黏、无剪切、零模、零时刻、周期态及非迹类边界。有限证书只校验约定；由于不存在内生素数载体与目标行列式，路线[A]{lang="en"}仍被拒绝。

# Frozen equation and Fourier sign

Let $\mathbb T=\mathbb R/(2\pi\mathbb Z)$ and consider $$\label{eq:pde}
 \partial_t f+a y\partial_xf=\nu(\partial_x^2+\partial_y^2)f,
 \qquad (x,y)\in\mathbb T\times\mathbb R,\quad a\in\mathbb R,\ \nu\ge0.$$ The clock is physical PDE time. We freeze $$\widehat f_k(\eta)=\frac1{2\pi}\int_{\mathbb T}\int_\mathbb R
 f(x,y)\mathrm e^{-i(kx+\eta y)}\,dy\,dx.$$ Since multiplication by $y$ becomes $i\partial_\eta$, the transformed equation is $$\label{eq:fourier}
 \partial_t\widehat f_k-a k\partial_\eta\widehat f_k
 =-\nu(k^2+\eta^2)\widehat f_k.$$ Couette damping and enhanced-dissipation context is classical [@BMV]; we claim a convention-complete derivation and certificate, not priority.

# Exact semigroup and composition

[\[thm:main\]]{#thm:main label="thm:main"} For every $k\in\mathbb Z$, $\eta\in\mathbb R$, and $t\ge0$, $$\label{eq:semigroup}
 \widehat{S_tf}_k(\eta)=\exp\!\left[-\nu\left\{k^2t+
 t\left(\eta+\frac{akt}{2}\right)^2+\frac{a^2k^2t^3}{12}\right\}\right]
 \widehat f_k(\eta+akt).$$ Moreover $S_tS_s=S_{t+s}$ on $L^2(\mathbb T\times\mathbb R)$.

The characteristic ending at $(t,\eta)$ is $\eta(r)=\eta+ak(t-r)$. Integrating [\[eq:fourier\]](#eq:fourier){reference-type="eqref" reference="eq:fourier"} gives $$D_t(\eta)=k^2t+\int_0^t(\eta+akr)^2dr
 =k^2t+\eta^2t+ak\eta t^2+\frac{a^2k^2t^3}{3}.$$ Completing the square yields [\[eq:semigroup\]](#eq:semigroup){reference-type="eqref" reference="eq:semigroup"}. Direct expansion gives $D_t(\eta)+D_s(\eta+akt)=D_{t+s}(\eta)$ and the shifts add, proving composition.

# Sharp sector norm and scale

[\[prop:norm\]]{#prop:norm label="prop:norm"} On the $k$-th Fourier sector, $$\label{eq:norm}
 \|S_t\|_{k\to k}=
 \exp\!\left[-\nu\left(k^2t+\frac{a^2k^2t^3}{12}\right)\right].$$ If $\nu t>0$, no nonzero $L^2$ vector attains this norm; frequency-localized packets approach it. If $\nu t=0$, every nonzero vector attains the norm.

Write the sector operator as $\mathcal M_{m_t}U_t$, where $U_tg(\eta)=g(\eta+akt)$ is unitary and $m_t(\eta)$ is the positive exponential in [\[eq:semigroup\]](#eq:semigroup){reference-type="eqref" reference="eq:semigroup"}. Its essential supremum is the value in [\[eq:norm\]](#eq:norm){reference-type="eqref" reference="eq:norm"}: continuity and the unique quadratic minimizer $\eta_0=-akt/2$ give the upper bound, while normalized functions supported in shrinking intervals about $\eta_0$ approach equality.

Let $N$ denote the value in [\[eq:norm\]](#eq:norm){reference-type="eqref" reference="eq:norm"}. If $\nu t>0$ and a nonzero $g\in L^2(\mathbb R_\eta)$ attained the norm, equality of squared norms would give $$\int_\mathbb R\bigl(N^2-|m_t(\eta)|^2\bigr)|U_tg(\eta)|^2\,d\eta=0.$$ The first factor is strictly positive away from the singleton $\{\eta_0\}$, so $U_tg$ would be supported on a null set and hence vanish, a contradiction. If $\nu t=0$, $m_t\equiv1$ and $\mathcal M_{m_t}U_t$ is unitary (the identity when $t=0$), so every nonzero vector attains its norm.

For $a\nu k\ne0$, the cubic factor reaches order one at $t=(12/(\nu a^2k^2))^{1/3}$; the ordinary heat term $\nu k^2t$ remains.

\>0

# Inviscid mixing and every degenerate boundary

At $\nu=0$, [\[eq:pde\]](#eq:pde){reference-type="eqref" reference="eq:pde"} is the unitary shear group $$f_k(y,t)=\mathrm e^{-iakty}f_k(y,0).$$ For $f_k\overline g\in L^1$, its pairing with $g$ tends to zero for $ak\ne0$ by the Riemann--Lebesgue lemma, while its $L^2$ norm is constant. Thus weak mixing is not dissipative decay. The involution $(x,y)\mapsto(-x,y)$ reverses this same clock. Positive viscosity destroys unitarity.

If $a=0$, [\[eq:semigroup\]](#eq:semigroup){reference-type="eqref" reference="eq:semigroup"} is ordinary heat. If $k=0$, it is one-dimensional heat in $y$, whose operator norm is one on the noncompact line. If $t=0$, it is the identity. These statements include the joint $a=\nu=0$ identity boundary.

# Periodic states and the trace-class stop

[\[prop:periodic\]]{#prop:periodic label="prop:periodic"} Let $T>0$. If $\nu>0$ and $S_Tf=f$ in $L^2$, then $f=0$. If $\nu=0$ and $aT\ne0$, the $T$-periodic states are exactly the streamwise means.

For $k\ne0$ and $\nu>0$, [\[eq:norm\]](#eq:norm){reference-type="eqref" reference="eq:norm"} is strictly below one. For $k=0$, the equality $(1-\mathrm e^{-\nu T\eta^2})\widehat f_0(\eta)=0$ confines support to the null set $\{0\}$. In the inviscid case, periodicity makes every nonzero $k$ component periodic in $\eta$ with nonzero period $akT$; an $L^2(\mathbb R)$ periodic function is zero. The $k=0$ component is fixed.

For $t>0$, the $k=0$ sector is multiplication by $\mathrm e^{-\nu t\eta^2}$ on the nonatomic space $L^2(\mathbb R_\eta)$. A nonzero multiplication operator there is not compact. Hence the full semigroup is noncompact and not trace class (the inviscid unitary and $t=0$ identity are also noncompact). We therefore define no ordinary Fredholm determinant.

\>1

# Executable closure and strict Route-A stop

The canonical ledger has 675 rational Fourier cells and 54 composition cells. A checker importing no producer closes 9,646 assertions. A separate SymPy path closes 2,713 identities. Exponentials use 100 working decimal digits; all 1,350 multiplier and sector-norm fields are serialized to 82 significant digits, and both executable paths lock this distinction. Replay is byte exact; seventeen repaired-hash semantic/schema attacks and one stale-hash attack are rejected. These are convention sentinels; Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} and its proofs carry every continuous quantifier.

The inviscid unitary supports only a formal hint. There is no arithmetic origin, rational-prime primitive owner, isolated periodic ledger, target determinant, target analytic structure, or Weil compression. Thus $$(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},
 \mathrm{FAIL},\mathrm{FORMAL\ HINT}),$$ overall `ROUTE_A_REJECTED`, Route B false, under `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Claim firewall.

We claim no nonlinear Couette stability, bounded-wall theorem, arithmetic local data, Euler factor, root number, automorphy, target divisor or functional equation, Hilbert--Pólya operator, finite-regression proof, exhaustive priority, external review, or acceptance score.

#### Revision focus.

Round 0 freezes the Fourier convention and proves the exact semigroup, composition, sharp norm, and cubic scale.

#### Revision focus.

Round 1 adds inviscid mixing, every parameter boundary, all periodic states, reversal, and the non-trace-class theorem.

#### Revision focus.

Round 2 adds independent executable closure, source ownership, Route-A evaluation, disclosures, and the claim firewall.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

Package-local exact synthetic evidence and deterministic code accompany the paper; no observational data are used.

#### Ethics.

No human, animal, personal, or sensitive data are used.

#### Author contributions (CRediT).

This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing. AI systems are not authors.

#### Funding.

No external funding is reported.

#### Conflicts of interest.

None known.

#### AI-use disclosure.

An AI coding assistant supported derivation, drafting, and exact-code development; it was not an external reviewer or an independent peer-review process.

1 J. Bedrossian, N. Masmoudi, and V. Vicol, "Enhanced dissipation and inviscid damping in the inviscid limit of the Navier--Stokes equations near the two dimensional Couette flow," *Arch. Rational Mech. Anal.* 219 (2016), 1087--1159. DOI: 10.1007/s00205-015-0917-3.
