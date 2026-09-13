---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-dirac-monopole-magnetic-flow-spectrum-route-a"
canonical_tex: "henon_dynamics/henon_dirac_monopole_magnetic_flow_spectrum_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_dirac_monopole_magnetic_flow_spectrum_route_a/paper/main.pdf"
source_sha256: "57f128c82c2ebf9b4e5619781ab6d726111a79d6755113f9507fd5db79b0b079"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Dirac-Monopole Dynamics on the Sphere: Magnetic Circles and the Complete Covariant-Laplacian Spectrum

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_dirac_monopole_magnetic_flow_spectrum_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_dirac_monopole_magnetic_flow_spectrum_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_dirac_monopole_magnetic_flow_spectrum_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_dirac_monopole_magnetic_flow_spectrum_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We identify a conserved Poincaré vector and every magnetic circle on the unit sphere, including its least period and all zero-energy and zero-charge faces. This is the *Poincare vector and every magnetic circle* stage. \>0 For an integral charge we then derive the *complete monopole-harmonic spectrum*, its multiplicities, heat trace, and charge-conjugation symmetry. \>1 Finally we record the *Route-A obstruction and finite certificate*: Chern integrality and natural quantization do not create a rational-prime owner, an orbit determinant, or a Hilbert--Pólya operator.
author:
- 'Route-A source-local certificate HCS-C331'
date: 3 September 2026
title: |
  Dirac-Monopole Dynamics on the Sphere:\
  Magnetic Circles and the Complete Covariant-Laplacian Spectrum
```

## Markdown 正文

trailerid \[\<C3312026090300000000000000000000\>\<C3312026090300000000000000000000\>\]

# The classical flow

Let $S^2\subset\mathbb R^3$ be the oriented unit sphere and let $Jv=x\times v$ on $T_xS^2$. Fix $q\in\mathbb Z$, put $b=q/2$, and consider $$\label{eq:magnetic}
 \nabla_t\dot x=bJ\dot x,\qquad |\dot x|^2=2E.$$

[\[thm:classical\]]{#thm:classical label="thm:classical"} The vector $$K=x\times\dot x+b x$$ is constant and satisfies $$K\cdot x=b,\qquad |K|^2=2E+b^2.$$ If $E>0$, the trajectory is the oriented small circle cut out by $K\cdot x=b$ and its least positive period is $$\label{eq:period}
 T(E,q)=\frac{2\pi}{\sqrt{2E+q^2/4}}.$$ If $E=0$, the trajectory is stationary. If $q=0$ and $E>0$, the circle is a great circle.

Skew-symmetry of $J$ preserves $|\dot x|$. The ambient acceleration is $\ddot x=b\,x\times\dot x-2E x$. Consequently, $$\dot K=x\times\ddot x+b\dot x
 =b\,x\times(x\times\dot x)+b\dot x=0.$$ Orthogonality gives the two displayed identities. The triple-product identity also gives $K\times x=\dot x$, so $x$ is a rigid rotation about the fixed axis $K$ with angular speed $|K|$. Its squared circle radius is $2E/(2E+b^2)$, positive exactly when $E>0$. A nonconstant circle first returns with its tangent after angle $2\pi$, proving [\[eq:period\]](#eq:period){reference-type="eqref" reference="eq:period"}. The two boundary statements follow directly.

Time reversal gives the precise sign pairing: if $x_q(t)$ solves charge $q$, then $x_q(-t)$, with its initial velocity reversed, solves charge $-q$ and traverses the same geometric circle oppositely. This does not identify the solutions having the same initial velocity. The conserved-plane proof does not rely on coordinates or a gauge potential.

\>0

# Integral charge and the complete quantum spectrum

Let $L_q\to S^2$ be a Hermitian line bundle with unitary connection of curvature $$\label{eq:curvature}
 F_\nabla=i\frac q2\,dA.$$ Its first Chern number is $$\frac{1}{2\pi i}\int_{S^2}F_\nabla=q.$$ Thus integrality of $q$ is exactly the global bundle boundary; a nonintegral local magnetic charge is not admitted to this quantum model.

Complex line bundles over $S^2$ are classified by $c_1\in H^2(S^2;\mathbb Z)\cong\mathbb Z$. Hence $L_q$ is unitarily isomorphic to the standard degree-$q$ homogeneous monopole bundle. After transport to one bundle, two unitary connections with curvature [\[eq:curvature\]](#eq:curvature){reference-type="eqref" reference="eq:curvature"} differ by $i\alpha$, where $d\alpha=0$. Since $H^1_{\mathrm{dR}}(S^2)=0$, $\alpha=df$; the gauge $g=e^{if}$ carries one connection to the other. Thus the arbitrary frozen connection is unitarily gauge equivalent to the standard homogeneous one.

On $C^\infty(S^2,L_q)=C_c^\infty(S^2,L_q)$ set $$\mathfrak q_q[s]=\int_{S^2}|\nabla s|^2\,dA,$$ and let $\Delta_q$ be its Friedrichs realization. The symmetric Laplace-type expression $\nabla^*\nabla$ on a compact manifold without boundary is essentially self-adjoint on smooth sections. Its unique self-adjoint closure therefore equals this positive Friedrichs operator; the resolvent is compact. Gauge-equivalent connections give unitarily conjugate operators.

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} The complete spectrum is $$\label{eq:spectrum}
 \lambda_{n,q}=n(n+|q|+1)+\frac{|q|}{2},\qquad n=0,1,\ldots,$$ and the multiplicity of $\lambda_{n,q}$ is $2n+|q|+1$. Hence, for $t>0$, $$\label{eq:heat}
 \operatorname{Tr}e^{-t\Delta_q}
 =\sum_{n=0}^{\infty}(2n+|q|+1)e^{-t\lambda_{n,q}}.$$ The degree $-q$ bundle is the complex conjugate of $L_q$ and has the same spectrum.

It now suffices to use the standard homogeneous connection. Its sections are degree-$q$ equivariant functions on $SU(2)$. Peter--Weyl decomposition contains exactly one copy of each spin $\ell=|q|/2+n$, $n\geq0$. The horizontal Laplacian is the total Casimir minus the fixed vertical weight square; it therefore acts by $$\ell(\ell+1)-\frac{q^2}{4}
 =n(n+|q|+1)+\frac{|q|}{2}.$$ The spin space has dimension $2\ell+1=2n+|q|+1$. Peter--Weyl completeness excludes further levels. The operator realization above and quadratic eigenvalue growth justify the absolutely convergent heat trace. Complex conjugation changes $q$ to $-q$, while [\[eq:spectrum\]](#eq:spectrum){reference-type="eqref" reference="eq:spectrum"} depends only on $|q|$.

At $q=0$, formula [\[eq:spectrum\]](#eq:spectrum){reference-type="eqref" reference="eq:spectrum"} becomes the ordinary spherical harmonic spectrum $n(n+1)$ with multiplicity $2n+1$. At $n=0$, the lowest monopole level has energy $|q|/2$ and multiplicity $|q|+1$.

\>1

# Certificate and obstruction

The checked artifact contains 39 positive-energy classical rows, 195 quarter-turn samples, 357 exact spectral cells, 36 degree-80 heat-trace partial sums, 25 Chern rows, and 18 time-reversal pairings, for 3,167 audited scalar leaves. An independent implementation performs 4,414 checks. SymPy verifies 2,621 exact identities, two isolated reproductions are byte-identical, and 80 hostile parser, schema, semantic, and repaired-hash attacks are rejected. These finite data are convention-sensitive regression receipts; the proofs of Theorems [\[thm:classical\]](#thm:classical){reference-type="ref" reference="thm:classical"} and [\[thm:spectrum\]](#thm:spectrum){reference-type="ref" reference="thm:spectrum"} establish the all-parameter statements.

The nearest registered owners are C313, the $q=0$ round-sphere boundary; C289, noncompact hyperbolic magnetic flow; C293, singular magnetic Grushin dynamics; and C274, the Euclidean Penning trap. None owns the simultaneous Chern, magnetic-circle, and monopole-spectrum contract.

The conservative Route-A tuple is $$\begin{gathered}
 (\mathrm{A0\_WEAK\_ARITHMETIC\_RELATION},\mathrm{A1\_WEAK},\\
 \mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
 \mathrm{A4\_NATURAL\_QUANTIZATION}).\end{gathered}$$ Chern integrality is not a rational-prime or prime-power carrier. The circles form clean continuous families rather than isolated hyperbolic cycles. The heat trace is not an Euler product or target determinant, and the covariant Laplacian is not asserted to realize target zeros. Route A is therefore rejected and Route B remains locked under `NO_BAD_EULER_OR_ROOT_NUMBER`. We claim no target local data, root number, automorphy, divisor, functional equation, zero match, or Hilbert--Pólya operator.

#### AI use.

A generative language model assisted drafting and code scaffolding. The displayed proofs, independent recomputation, hostile tests, and deterministic artifacts define the audit record.

# Source lineage {#source-lineage .unnumbered}

This paper is a source-local reconstruction and makes no priority claim.

9 P. A. M. Dirac, "Quantised Singularities in the Electromagnetic Field," *Proc. Roy. Soc. A* 133 (1931), 60--72. DOI: [10.1098/rspa.1931.0130](https://doi.org/10.1098/rspa.1931.0130). T. T. Wu and C. N. Yang, "Dirac Monopole Without Strings: Monopole Harmonics," *Nucl. Phys. B* 107 (1976), 365--380. DOI: [10.1016/0550-3213(76)90143-7](https://doi.org/10.1016/0550-3213(76)90143-7). T. T. Wu and C. N. Yang, "Some Properties of Monopole Harmonics," *Phys. Rev. D* 16 (1977), 1018--1021. DOI: [10.1103/PhysRevD.16.1018](https://doi.org/10.1103/PhysRevD.16.1018). T. T. Wu and C. N. Yang, "Dirac's Monopole Without Strings: Classical Lagrangian Theory," *Phys. Rev. D* 14 (1976), 437--445. DOI: [10.1103/PhysRevD.14.437](https://doi.org/10.1103/PhysRevD.14.437).
