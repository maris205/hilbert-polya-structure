---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-van-der-pol-lienard-limit-cycle-route-a"
canonical_tex: "henon_dynamics/henon_van_der_pol_lienard_limit_cycle_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_van_der_pol_lienard_limit_cycle_route_a/paper/main.pdf"
source_sha256: "13d9a71802d8fe6e42e15db157a2ff5274f7b7f6b454a2ec44e7f1365867ab8d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Sign-Complete Lienard Certificate for the Van der Pol Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_van_der_pol_lienard_limit_cycle_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_van_der_pol_lienard_limit_cycle_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_van_der_pol_lienard_limit_cycle_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_van_der_pol_lienard_limit_cycle_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze the smooth polynomial Van der Pol oscillator and take one theorem-scale step beyond a local phase portrait. For $\mu>0$, its Lienard primitive has a single positive zero, so the classical theorem gives exactly one hyperbolic attracting limit cycle for positive damping; time reversal gives one repelling cycle for negative damping, while the zero face is a harmonic center with a continuum of ovals. Energy balance and planar divergence then identify the Poincare fixed section and the transverse Floquet multiplier. Five independently replayed DOP853 rows illustrate the theorem (the multiplier decreases from $0.5331$ at $\mu=0.1$ to $1.28\times10^{-25}$ at $\mu=4$). The rows are finite regression probes, not an all-state census. This source-local result makes no arithmetic, target-determinant, or Hilbert--Polya claim.
author:
- HCS Research Program
date: 30 August 2026(revision 2)
title: 'A Sign-Complete Lienard Certificate for the Van der Pol Flow'
```

## Markdown 正文

suppressoptionalinfo 611 trailerid \[\<C2492026083000000000000000000000\>\<C2492026083000000000000000000000\>\]

# Frozen model and question

We study the polynomial vector field on $\mathbb R^2$ $$\dot x=y,\qquad \dot y=\mu(1-x^2)y-x,\qquad \mu\in\mathbb R.
 \label{eq:vdp}$$ Equivalently, $x$ satisfies $$x''+\mu(x^2-1)x'+x=0 .
 \label{eq:lienard}$$ The clock is physical time $t$, and the oriented Poincare section is $\Sigma=\{(x,y):x=0,\ y>0\}$. The question is whether this smooth nonlinear family can support a complete, replayable sign and boundary statement without importing an arithmetic carrier. The answer below is analytic; the numerical receipt only supplies a transparent finite check.

=0 The baseline freezes ([\[eq:vdp\]](#eq:vdp){reference-type="ref" reference="eq:vdp"})--([\[eq:lienard\]](#eq:lienard){reference-type="ref" reference="eq:lienard"}), the section orientation, and the three parameter faces $\mu<0$, $\mu=0$, and $\mu>0$. No period is assigned by sampling alone.

# The Lienard theorem and sign boundary

Write $f(x)=\mu(x^2-1)$ and $$F(x)=\int_0^x f(s)\,\mathrm ds=\mu\left(\frac{x^3}{3}-x\right).
 \label{eq:F}$$ For $\mu>0$, $F<0$ on $(0,\sqrt3)$, has the unique positive zero $\sqrt3$, and is positive and increasing thereafter. The standard Liénard existence and uniqueness hypotheses therefore apply.

For every $\mu>0$, the flow ([\[eq:vdp\]](#eq:vdp){reference-type="ref" reference="eq:vdp"}) has exactly one hyperbolic attracting periodic orbit surrounding the origin. Its Poincare return map on $\Sigma$ has one fixed point, and the derivative at that point is the transverse Floquet multiplier. For $\mu<0$, the map $(t,x,y)\mapsto(-t,x,-y)$ transfers this orbit to exactly one hyperbolic repelling cycle. At $\mu=0$, $E=(x^2+y^2)/2$ is conserved and every level $E=c>0$ is a harmonic oval of period $2\pi$.

#### Proof sketch.

Equation ([\[eq:lienard\]](#eq:lienard){reference-type="ref" reference="eq:lienard"}) is in the classical Liénard form. The sign and monotonicity of $F$ in ([\[eq:F\]](#eq:F){reference-type="ref" reference="eq:F"}), together with the odd symmetry, give existence and uniqueness of the enclosing cycle; hyperbolicity and attraction are part of the same return-map conclusion. Reversing time and velocity changes the sign of $\mu$, hence reverses stability. Setting $\mu=0$ reduces ([\[eq:vdp\]](#eq:vdp){reference-type="ref" reference="eq:vdp"}) to the unit harmonic oscillator, proving the center face directly. This invokes no numerical fit and excludes no state by a finite cutoff.

\>0

# Energy, divergence, and Floquet data

The elementary identities are $$E=\frac{x^2+y^2}{2},\qquad \dot E=\mu(1-x^2)y^2,\qquad
 \operatorname{div}X=\mu(1-x^2).
 \label{eq:identities}$$ For a periodic orbit with $\mu\ne0$, integrating the first identity gives the exact balance $\int_0^T(1-x^2)y^2\,\mathrm dt=0$; the divided balance is not asserted on the $\mu=0$ center face. In two dimensions one Floquet multiplier is one (the tangent direction), and Liouville's formula gives $$\lambda_\perp=\exp\!\left(\int_0^T\operatorname{div}X\,\mathrm dt\right)
 =\exp\!\left(\mu\int_0^T(1-x^2)\,\mathrm dt\right).
 \label{eq:floquet}$$ For a restoring frequency $\omega>0$, the change $\tau=\omega t$ reduces $x''+\mu_0(x^2-1)x'+\omega^2x=0$ to the same normal form with effective parameter $\mu_0/\omega$.

\>0

# Finite Poincare receipt

The producer brackets the fixed point by $y\in[0.05,8]$ and integrates with DOP853 (relative tolerance $3\times10^{-12}$, absolute tolerance $3\times10^{-14}$, maximum step $0.03$). The independent checker repeats the integration and verifies the return residual and ([\[eq:identities\]](#eq:identities){reference-type="ref" reference="eq:identities"})-- ([\[eq:floquet\]](#eq:floquet){reference-type="ref" reference="eq:floquet"}). Table [1](#tab:receipt){reference-type="ref" reference="tab:receipt"} reports rounded values; all digits in the JSON receipt are retained at 15 significant figures.

::: {#tab:receipt}
   $\mu$   $y_\Sigma$     $T$      $\int\!\operatorname{div}X$     $\lambda_\perp$          \|balance\|
  ------- ------------ ---------- ----------------------------- ---------------------- ---------------------
    0.1     2.00177     6.28711            $-0.62910$            $5.33\times10^{-1}$    $6.2\times10^{-15}$
    0.5     2.04406     6.38068            $-3.23967$            $3.92\times10^{-2}$    $2.1\times10^{-13}$
     1      2.17271     6.66329            $-7.05893$            $8.60\times10^{-4}$    $1.8\times10^{-13}$
     2      2.61497     7.62987            $-18.17864$           $1.27\times10^{-8}$    $8.3\times10^{-13}$
     4      3.76234     10.20352           $-57.32131$           $1.28\times10^{-25}$   $5.4\times10^{-12}$

  : Positive-parameter return probes. These rows are finite regression receipts, not a numerical census or a proof of uniqueness.
:::

=1

#### Independent checks.

The producer-independent checker passes 264 structural and numerical assertions. A separate SymPy reconstruction passes 81 identities, including the origin characteristic polynomial, time reversal, and frequency scaling. Clean-process byte replay succeeds, and 40 repaired-hash hostile mutations are all rejected. These gates validate the receipt's provenance and algebra; they do not enlarge the theorem's scope.

\>1

# Collision audit and route boundary

The model is not a relabeling of nearby packages. C227 studies the three-dimensional Lorenz flow and local equilibrium/Hopf conditions; C232 studies a conservative Duffing separatrix; C178 uses a harmonic strobe; C237 is a stochastic Kramers system; and C245 is hybrid integrate-and-fire. C249 is the smooth polynomial Liénard case whose single-cycle theorem and Floquet receipt are absent from those certificates. This comparison is workspace bookkeeping, not a literature-priority claim.

The locked scope is `NO_BAD_EULER_OR_ROOT_NUMBER`. No prime or zero table, arithmetic local datum, Euler factor, root number, automorphy claim, target divisor or functional equation, target determinant, or Hilbert--Pólya operator is present. Accordingly the Route-A tuple is `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, with overall verdict `ROUTE_A_REJECTED`; Route B is disabled.

# Conclusion and limitations

The main result is a single sign-complete theorem package: Liénard uniqueness for positive damping, time reversal for negative damping, an exact center boundary, and a divergence-to-Floquet identity tied to one Poincare section. The receipt is deliberately modest. It does not give an elementary formula for the period at every parameter, enumerate every continuum state, or infer asymptotic coefficients from five samples. A future analytic direction is a uniform asymptotic study of the relaxation period; that direction would still be a smooth-flow problem and would not authorize arithmetic claims.

9 A. Liénard, "Étude des oscillations entretenues," *Revue Générale de l'Électricité* 23 (1928), 901--912, [Gallica scan](https://gallica.bnf.fr/ark:/12148/bpt6k5671115f). N. Levinson and O. K. Smith, "A general equation for relaxation oscillations," *Duke Mathematical Journal* 9 (1942), 382--403, DOI [10.1215/S0012-7094-42-00928-1](https://doi.org/10.1215/S0012-7094-42-00928-1). S. H. Strogatz, *Nonlinear Dynamics and Chaos*, 2nd ed., Westview Press, 2015.
