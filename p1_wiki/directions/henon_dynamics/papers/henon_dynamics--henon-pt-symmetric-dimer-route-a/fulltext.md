---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-pt-symmetric-dimer-route-a"
canonical_tex: "henon_dynamics/henon_pt_symmetric_dimer_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_pt_symmetric_dimer_route_a/paper/main.pdf"
source_sha256: "fb8dc6c68aa4feef473830d94852a10f58f142d6a71ded04cdd885fd46101ed2"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Phase, Projective, and Metric Atlases for a PT-Symmetric Dimer

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_pt_symmetric_dimer_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_pt_symmetric_dimer_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_pt_symmetric_dimer_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_pt_symmetric_dimer_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the autonomous balanced-gain/loss dimer $\mathrm i\dot\psi=H_{\gamma,\kappa}\psi$, $\kappa>0$, we give an all-parameter dynamical classification. =0 The scalar identity $H^2=(\kappa^2-\gamma^2)I$ yields the exact propagator, generic periods in the unbroken chamber, a rank-one nilpotent exceptional point, and the attracting/repelling eigenrays of the broken chamber. \>0 We additionally compactify the flow on $\mathbb {CP}^1$, separate vector and ray periods, and prove the sharp positivity boundary for an explicit conserved pseudo-Hermitian metric. \>1 An independent exact receipt closes both exceptional sheets and all singular parameter faces while enforcing a literal source/target scope firewall.
author:
- 'Route-A source-local certificate HCS-C297'
date: 2 September 2026
title: |
  Exact Phase, Projective, and Metric Atlases\
  for a PT-Symmetric Dimer
```

## Markdown 正文

trailerid \[\<C2972026090200000000000000000000\>\<C2972026090200000000000000000000\>\]

# Frozen system and exact propagator

The frozen release obstruction identifier is `HEN-O281`. Let $$H=H_{\gamma,\kappa}=
 \begin{pmatrix}\mathrm i\gamma&\kappa\\ \kappa&-\mathrm i\gamma\end{pmatrix},
 \qquad \kappa>0,\quad\gamma\in\mathbb R,
 \qquad \mathrm i\dot\psi=H\psi.$$ Parity is $\mathcal P=\sigma_x$ and time reversal is componentwise complex conjugation, so $\mathcal P H^*\mathcal P=H$. Time is the physical propagation parameter; it is not adjusted to external data. Put $\delta=\kappa^2-\gamma^2$.

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} The propagator is $$e^{-\mathrm itH}=\begin{cases}
\cos(\omega t)I-\mathrm i\omega^{-1}\sin(\omega t)H,
 &\delta>0,\quad\omega=\sqrt\delta,\\[3pt]
I-\mathrm itH,&\delta=0,\\[3pt]
\cosh(\nu t)I-\mathrm i\nu^{-1}\sinh(\nu t)H,
 &\delta<0,\quad\nu=\sqrt{-\delta}.
\end{cases}$$ If $\delta>0$, a ray having nonzero components in both eigenlines has least projective period $\pi/\omega$, while its vector representative has least period $2\pi/\omega$. The eigenrays themselves are stationary. If $\delta=0$, $H$ is nonzero rank-one nilpotent with one eigenline, and every generalized state has linear leading growth. If $\delta<0$, there are two fixed rays; one attracts every generic forward ray and the other repels it, with exponential rate $2\nu$ in their affine ratio.

Multiplication gives $$H^2=(\kappa^2-\gamma^2)I=\delta I.$$ The even and odd terms of the exponential series give the three formulae. For $\delta>0$ the eigenvalues are $\pm\omega$. In their eigenbasis a generic component ratio is multiplied by $e^{2\mathrm i\omega t}$, proving the ray period; equality of both vector phases first occurs at $2\pi/\omega$. For $\delta=0$, nonzero determinant-zero $H$ has rank one and the exponential terminates. For $\delta<0$ the eigenvalues are $\pm\mathrm i\nu$, so the evolution multipliers are $e^{\pm\nu t}$ and their ratio proves the final assertion.

This proof is uniform at the exceptional point: it does not diagonalize there or suppress the generalized eigenvector. It also prevents a common factor of two error between vector and ray periods.

\>0

# Projective flow and conserved metrics

On the affine chart $\psi_1\ne0$, set $z=\psi_2/\psi_1$. Direct differentiation gives the Riccati equation $$\label{eq:riccati}
 \dot z=\mathrm i\kappa(z^2-1)-2\gamma z.$$ The reciprocal chart extends it across infinity to a complete holomorphic vector field on $\mathbb {CP}^1$. The complex quadratic discriminant of its fixed point equation is $-4\delta$; the matrix characteristic discriminant is $+4\delta$. Thus the two fixed rays merge precisely on $|\gamma|=\kappa$. These opposite signs are conventionally harmless but must not be conflated.

[\[thm:metric\]]{#thm:metric label="thm:metric"} With $$Q=\sigma_x,\qquad
 \eta=I+\frac{\gamma}{\kappa}\sigma_y,$$ one has $H^\dagger Q=QH$ and $H^\dagger\eta=\eta H$. Both quadratic forms are conserved. The form $Q$ is indefinite for every parameter, while $\eta$ is positive definite exactly when $|\gamma|<\kappa$, singular positive semidefinite at $|\gamma|=\kappa$, and indefinite when $|\gamma|>\kappa$.

The intertwining identities follow by direct Pauli-matrix multiplication. For either matrix $M$, differentiation gives $$\frac{\mathrm d}{\mathrm dt}(\psi^\dagger M\psi)
 =\mathrm i\psi^\dagger(H^\dagger M-MH)\psi=0.$$ The eigenvalues of $\eta$ are $1+|\gamma|/\kappa$ and $1-|\gamma|/\kappa$, proving the signature claim.

The standard Euclidean norm is not substituted for these forms: $$\frac{\mathrm d}{\mathrm dt}\|\psi\|^2
 =2\gamma\,\psi^\dagger\sigma_z\psi.$$ It is generally not conserved. In the unbroken phase the two real-energy eigenlines have opposite $Q$-Krein signs; their collision makes the normalized positive metric singular at the exceptional point.

\>1

# Boundary closure and independent evidence

Table [1](#tab:boundary){reference-type="ref" reference="tab:boundary"} records the faces excluded from abbreviated phase diagrams.

::: {#tab:boundary}
  Face                                Exact outcome
  ----------------------------------- -------------------------------------------------------------
  $\gamma=0$                          Hermitian $H=\kappa\sigma_x$ and $\eta=I$
  $\gamma=\pm\kappa$                  two nilpotent sheets, one eigenline on each
  $\kappa\downarrow0$, $\gamma\ne0$   uncoupled amplification/decay; no positive displayed $\eta$
  $(\kappa,\gamma)=(0,0)$             zero generator, not an exceptional point
  eigenray initial data               projectively stationary, not generic-periodic
  $\psi=0$                            fixed vector with no point in $\mathbb {CP}^1$

  : Boundary atlas.
:::

A canonical exact receipt enumerates all 168 integer cells $1\le\kappa\le8$, $-10\le\gamma\le10$: 64 are unbroken, 16 exceptional, and 88 broken. A producer-independent checker reconstructs them with 6,475 assertions. A separate symbolic route contributes 516 identities and grid checks; two fresh paths reproduce the same exact evidence byte. All 52 hostile schema, repaired-hash, duplicate-key, obstruction-ID, scope, and YAML graph-sharing attacks are rejected. The finite rectangle is regression evidence; Theorems [\[thm:atlas\]](#thm:atlas){reference-type="ref" reference="thm:atlas"}--[\[thm:metric\]](#thm:metric){reference-type="ref" reference="thm:metric"} are all-parameter algebraic statements.

# Route-A result, ownership, and limitations

The foundational PT-symmetric setting belongs to Bender and Boettcher [@BB1998]; positive-metric pseudo-Hermiticity is treated by Mostafazadeh [@M2002], and balanced optical gain/loss has an experimental owner in Rueter et al. [@R2010]. Our result is a source-model closure and does not claim those mechanisms as literature originality.

Under evaluator v0.2.0 the strict tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
 \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}),$$ with overall verdict `ROUTE_A_REJECTED`. A1 is only a clean projective family, not an isolated arithmetic periodic-orbit bridge. A4 is only a finite-dimensional, parameter-dependent metric hint. No fixed Hilbert-space self-adjoint realization across the exceptional point is asserted.

The literal scope is `NO_BAD_EULER_OR_ROOT_NUMBER`. We construct no arithmetic local data, Euler factors, root numbers, automorphy, target divisor or functional equation, target zero match, Hilbert--Pólya operator, or Route-B input.

9 C. M. Bender and S. Boettcher, "Real spectra in non-Hermitian Hamiltonians having PT symmetry," *Phys. Rev. Lett.* 80 (1998), 5243--5246. A. Mostafazadeh, "Pseudo-Hermiticity versus PT symmetry," *J. Math. Phys.* 43 (2002), 205--214. C. E. Rueter et al., "Observation of parity-time symmetry in optics," *Nature Phys.* 6 (2010), 192--195.
