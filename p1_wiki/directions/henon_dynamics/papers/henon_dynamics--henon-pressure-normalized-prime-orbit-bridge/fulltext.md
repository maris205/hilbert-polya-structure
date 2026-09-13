---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-pressure-normalized-prime-orbit-bridge"
canonical_tex: "henon_dynamics/henon_pressure_normalized_prime_orbit_bridge/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_pressure_normalized_prime_orbit_bridge/paper/paper.pdf"
source_sha256: "95e654ea772e2cc88a1d24d40e561afaa56d707c5e7dbe65bb565e3db22710ff"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Pressure Normalization Produces an Entropy-One Prime-Orbit Law for a Hénon Instability Suspension

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_pressure_normalized_prime_orbit_bridge>)
- [规范 TeX](<../../../../../henon_dynamics/henon_pressure_normalized_prime_orbit_bridge/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_pressure_normalized_prime_orbit_bridge/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_pressure_normalized_prime_orbit_bridge/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The raw instability roof on a certified area-preserving Hénon survivor has correct local Euler-factor amplitudes but an incorrect global convergence class. We give the canonical dynamical repair. Let $h_*$ be the unique zero of the pressure $P(-s\tau)$ for the positive Hölder instability roof $\tau$. The normalized roof $\widehat\tau=h_*\tau$ remains non-lattice and has suspension entropy exactly one. Since the symbolic base is mixing, the Parry--Pollicott prime orbit theorem applies and yields $\Pi(T)\sim e^T/T$. The normalized Euler atoms are exactly $\log P_\gamma\,P_\gamma^{-rs}$ for the intrinsic positive real labels $P_\gamma=|\Lambda_\gamma|^{h_*}$. Thus the construction matches the prime-number counting exponent and all repetition amplitudes without a fitted parameter. Its remaining obstruction is arithmetic rather than dynamical: no theorem makes these real labels rational primes, and no critical-line continuation or Hilbert--Pólya operator is obtained.
author:
- |
  Liang Wang$^{*1}$\
  $^{1}$School of Artificial Intelligence and Automation, Huazhong University of Science and Technology\
  Wuhan 430074, P.R. China\
  $^*$Corresponding author
date: 'Preprint, August 2026'
title: |
  Pressure Normalization Produces an Entropy-One\
  Prime-Orbit Law for a Hénon Instability Suspension
```

## Markdown 正文

# Inherited Hénon suspension

Let $H_6(q,p)=(1-6q^2-p,q)$ and restrict it to the previously certified four-state hyperbolic survivor. The adjacency matrix $A$ satisfies $A^4>0$, so its subshift is topologically mixing. The unstable Jacobian defines a positive Hölder roof $$\tau(z)=\log J^u(z).$$ For a primitive orbit $\gamma$, its roof period is $$\ell_\gamma=\sum_{z\in\gamma}\tau(z)=\log|\Lambda_\gamma|.$$ Prior exact algebra supplies two primitive multipliers whose logarithms are incommensurable. Hence $\tau$ is non-lattice. These facts are inherited with hashes frozen in the certificate.

For real $s$, let $P(-s\tau)$ denote topological pressure. Positivity makes it strictly decreasing, and the certified pressure theorem gives a unique root $h_*$ satisfying $$\label{eq:hinterval}
0.277980<h_*<0.277987.$$

# Canonical pressure normalization

[\[thm:normalize\]]{#thm:normalize label="thm:normalize"} Define $$\widehat\tau=h_*\tau,
\qquad
\widehat\ell_\gamma=h_*\ell_\gamma.$$ Then $\widehat\tau$ is positive, Hölder, and non-lattice. Its suspension flow has topological entropy one.

Positive scalar multiplication preserves positivity and Hölder regularity. If the periods of $h_*\tau$ lay in a discrete subgroup, division by $h_*>0$ would make $\tau$ lattice, contrary to the inherited theorem. The entropy $h$ of a suspension roof is characterized by $P(-h\widehat\tau)=0$. Here $$P(-1\cdot\widehat\tau)=P(-h_*\tau)=0.$$ Uniqueness of the pressure root gives $h=1$.

The normalization is canonical within the chosen roof: it is the unique positive scalar multiple whose suspension entropy is one. It is not chosen from a prime or zero table.

# Prime orbit theorem

Let $\widehat\Pi(T)$ count primitive closed suspension orbits of least period at most $T$.

[\[thm:pot\]]{#thm:pot label="thm:pot"} For the pressure-normalized Hénon suspension, $$\boxed{\widehat\Pi(T)\sim\frac{e^T}{T}}\qquad(T\to\infty).$$

The base is a mixing finite-type shift, the roof is positive Hölder and non-lattice, and Theorem [\[thm:normalize\]](#thm:normalize){reference-type="ref" reference="thm:normalize"} gives entropy one. The prime orbit theorem for weak-mixing hyperbolic suspension flows therefore gives $e^{hT}/(hT)$ with $h=1$.

This is the exact dynamical analogue of the prime number theorem at the counting level. Non-lattice is essential: a lattice suspension has periodic fluctuations rather than this continuous asymptotic.

# Exact local labels and repetitions

Define the positive real orbit label $$P_\gamma=e^{\widehat\ell_\gamma}
=|\Lambda_\gamma|^{h_*}.$$ Then $$1-e^{-s\widehat\ell_\gamma}=1-P_\gamma^{-s}$$ and $$\label{eq:atoms}
\partial_s\log(1-P_\gamma^{-s})
=\sum_{r\ge1}\log P_\gamma\,P_\gamma^{-rs}.$$ Thus the pressure normalization simultaneously fixes the global counting exponent and preserves the exact local prime-power syntax identified in the preceding raw-clock audit.

Equation [\[eq:atoms\]](#eq:atoms){reference-type="eqref" reference="eq:atoms"} is not an arithmetic prime correspondence. It uses one positive real label per orbit. Replacing $P_\gamma$ by a nearby prime would be post-hoc fitting and is forbidden.

# Analytic and arithmetic boundaries

The associated suspension zeta has its initial Euler-product domain $\Re s>1$ and the standard entropy-one boundary singularity underlying Theorem [\[thm:pot\]](#thm:pot){reference-type="ref" reference="thm:pot"}. This removes the raw clock's absolute convergence on $\Re s=1/2$. It does not prove meromorphic continuation to that line, a functional equation, gamma factors, or equality with the completed Riemann divisor.

The exact arithmetic question is now isolated: $$\boxed{|\Lambda_\gamma|^{h_*}\stackrel{?}{\in}\mathbb P}$$ for a complete, multiplicity-preserving orbit family. No evidence in the pressure theorem addresses this statement. The first necessary audit is the algebraic type of the raw multiplier $\Lambda_\gamma$ at every period.

# Evaluator verdict

The outcome is a genuine all-period analytic structure, but not a rational- prime bridge. The strict Route-A tuple is $$(A1_{\rm WEAK},A2_{\rm ANALYTIC},A3_{\rm PARTIAL},A4_{\rm FORMAL}),$$ with overall `ROUTE_A_EXPLORATORY`. Route B is not authorized because no operator, self-adjoint domain, von Mangoldt trace identity, or xi determinant exists.

# Conclusion

Pressure normalization is the first large repair in this batch: it converts the raw Hénon instability clock into an entropy-one non-lattice suspension with a true prime orbit theorem. The bridge is now blocked at a sharply arithmetic gate---whether its intrinsic real labels can ever be rational primes---rather than at orbit density or repetition bookkeeping.

9 W. Parry and M. Pollicott, An analogue of the prime number theorem for closed orbits of Axiom A flows, *Ann. of Math.* 118 (1983), 573--591. W. Parry and M. Pollicott, *Zeta Functions and the Periodic Orbit Structure of Hyperbolic Dynamics*, Astérisque 187--188 (1990). S. P. Lalley, Renewal theorems in symbolic dynamics, *Acta Math.* 163 (1989), 1--55.
