---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-thermal-qubit-lindblad-entanglement-breaking-route-a"
canonical_tex: "henon_dynamics/henon_thermal_qubit_lindblad_entanglement_breaking_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_thermal_qubit_lindblad_entanglement_breaking_route_a/paper/main.pdf"
source_sha256: "d3b6bd0cfbfab3328e14e8b1be6faea001bd3f814a301eb277b4d5e8359a19a9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Entanglement-Breaking Time for a Thermal Qubit with Pure Dephasing: Flow, Choi Geometry, and Every Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_thermal_qubit_lindblad_entanglement_breaking_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_thermal_qubit_lindblad_entanglement_breaking_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_thermal_qubit_lindblad_entanglement_breaking_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_thermal_qubit_lindblad_entanglement_breaking_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We solve the phase-covariant qubit GKSL semigroup with thermal excitation, relaxation, Hamiltonian phase, and pure dephasing on the entire nonnegative rate cone. With the convention that $(\gamma_\phi/2)
  (\sigma_z\rho\sigma_z-\rho)$ damps coherence at rate $\gamma_\phi$, we give the exact density flow and Liouvillian spectrum. Its normalized Choi state is separable precisely when $p(1-p)(1-\eta)^2\geq\eta^q$. This yields one finite entanglement-breaking time exactly for faithful thermal baths and an explicit radical when pure dephasing vanishes. \>0 We further prove the sharp trace-distance contraction coefficient and classify all one-sided, dephasing, unitary, and identity boundaries. \>1 Independent exact evidence and a hostile inference audit separate the complete source theorem from arithmetic determinant and Hilbert--Pólya claims.
author:
- 'Route-A source-local certificate HCS-C303'
date: 2 September 2026
title: |
  Exact Entanglement-Breaking Time for a Thermal Qubit\
  with Pure Dephasing: Flow, Choi Geometry, and Every Boundary
```

## Markdown 正文

trailerid \[\<C3032026090200000000000000000000\>\<C3032026090200000000000000000000\>\]

# Frozen convention and exact semigroup

Use the ordered basis $|0\rangle,|1\rangle$, with $|0\rangle$ ground, $$\sigma_z=|1\rangle\langle1|-|0\rangle\langle0|,
 \quad \sigma_-=|0\rangle\langle1|,
 \quad \sigma_+=|1\rangle\langle0|.$$ For $\gamma_\downarrow,\gamma_\uparrow,\gamma_\phi\geq0$ and $\omega\in\mathbb R$, consider $$\label{eq:gksl}
 \mathcal L(\rho)=-i[(\omega/2)\sigma_z,\rho]
 +\gamma_\downarrow\mathcal D[\sigma_-]\rho
 +\gamma_\uparrow\mathcal D[\sigma_+]\rho
 +\frac{\gamma_\phi}{2}(\sigma_z\rho\sigma_z-\rho),$$ where $\mathcal D[L]\rho=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\}$. The factor $1/2$ in the last term is part of the model: pure dephasing alone sends $\rho_{01}$ to $\mathrm e^{(-\gamma_\phi+i\omega)t}\rho_{01}$. Set $$\Gamma_1=\gamma_\downarrow+\gamma_\uparrow,
 \qquad \Gamma_2=\frac{\Gamma_1}{2}+\gamma_\phi.$$

[\[thm:flow\]]{#thm:flow label="thm:flow"} If $\Gamma_1>0$, put $$p=\frac{\gamma_\uparrow}{\Gamma_1},\qquad
 \eta=\mathrm e^{-\Gamma_1t},\qquad
 c=\mathrm e^{(-\Gamma_2+i\omega)t}.$$ Then, for every density matrix and $t\geq0$, $$\label{eq:solution}
 \rho_{11}(t)=p+\eta(\rho_{11}(0)-p),\qquad
 \rho_{01}(t)=c\rho_{01}(0).$$ The Liouvillian is diagonalizable on every parameter face and $$\label{eq:char}
 \det(\lambda I-\mathcal L)=
 \lambda(\lambda+\Gamma_1)\bigl((\lambda+\Gamma_2)^2+\omega^2\bigr).$$

In the matrix-unit coordinate order $(E_{00},E_{01},E_{10},E_{11})$, direct substitution in [\[eq:gksl\]](#eq:gksl){reference-type="eqref" reference="eq:gksl"} gives $$[\mathcal L]=\begin{pmatrix}
 -\gamma_\uparrow&0&0&\gamma_\downarrow\\
 0&-\Gamma_2+i\omega&0&0\\
 0&0&-\Gamma_2-i\omega&0\\
 \gamma_\uparrow&0&0&-\gamma_\downarrow
 \end{pmatrix}.$$ The population block and two scalar coherence blocks yield [\[eq:solution\]](#eq:solution){reference-type="eqref" reference="eq:solution"} and [\[eq:char\]](#eq:char){reference-type="eqref" reference="eq:char"}. They also supply independent eigenoperators even at accidental eigenvalue collisions. When $\Gamma_1=0$, nonnegativity forces $\gamma_\downarrow=\gamma_\uparrow=0$, and the same block decomposition applies directly.

# Choi geometry and the exact EB time

Let $|\Omega\rangle=(|00\rangle+|11\rangle)/\sqrt2$ and use the normalized Choi state $J_t=(I\otimes\Phi_t)(|\Omega\rangle\langle\Omega|)$. From Theorem [\[thm:flow\]](#thm:flow){reference-type="ref" reference="thm:flow"}, in the order $|00\rangle,|01\rangle,|10\rangle,
|11\rangle$, $$\label{eq:choi}
 J_t=\frac12\begin{pmatrix}
 a&0&0&c\\0&b&0&0\\0&0&d&0\\\bar c&0&0&e
 \end{pmatrix},$$ where $$a=1-p(1-\eta),\quad b=p(1-\eta),\quad
 d=(1-p)(1-\eta),\quad e=\eta+p(1-\eta).$$ Define $q=2\Gamma_2/\Gamma_1\geq1$, so $|c|^2=\eta^q$.

[\[thm:eb\]]{#thm:eb label="thm:eb"} For $\Gamma_1>0$, $\Phi_t$ is entanglement breaking if and only if $$\label{eq:eb}
 p(1-p)(1-\eta)^2\geq\eta^q.$$ If $0<p<1$, there is a unique $\eta_*\in(0,1)$ solving equality, and $$t_{\rm EB}=-\frac{\log\eta_*}{\Gamma_1},\qquad
 \Phi_t\text{ is EB}\Longleftrightarrow t\geq t_{\rm EB}.$$ If $\gamma_\phi=0$, writing $r=p(1-p)$ gives $$\label{eq:radical}
 \eta_*=\frac{1+2r-\sqrt{1+4r}}{2r};
 \qquad p=\tfrac12:\ \eta_*=3-2\sqrt2.$$ For $p=0$ or $p=1$, no finite $t$ is EB, but the limiting constant channel is.

First, [\[eq:choi\]](#eq:choi){reference-type="eqref" reference="eq:choi"} is positive: all diagonal entries are nonnegative and $$ae-|c|^2=p(1-p)(1-\eta)^2+\eta-\eta^q\geq0.$$ Partial transpose moves $c$ into the middle $2\times2$ block. Its determinant is $$\frac{bd-|c|^2}{4}
 =\frac{p(1-p)(1-\eta)^2-\eta^q}{4}.$$ For a two-qubit state, positivity under partial transpose is equivalent to separability; a channel is EB exactly when its Choi state is separable. This proves [\[eq:eb\]](#eq:eb){reference-type="eqref" reference="eq:eb"}. For $r=p(1-p)>0$, $F(\eta)=r(1-\eta)^2-\eta^q$ obeys $$F(0)=r>0,\quad F(1)=-1,\quad
 F'(\eta)=-2r(1-\eta)-q\eta^{q-1}<0$$ on $(0,1)$. Hence the root is unique; $\eta$ decreases with time. Setting $q=1$ and taking the root in $(0,1)$ gives [\[eq:radical\]](#eq:radical){reference-type="eqref" reference="eq:radical"}. At $p=0,1$, the left side of [\[eq:eb\]](#eq:eb){reference-type="eqref" reference="eq:eb"} is zero while $\eta^q>0$ at finite time.

\>0

# Sharp contraction and complete boundary atlas

For Hermitian traceless $\Delta=(v\cdot\sigma)/2$, $\|\Delta\|_1=\|v\|_2$. The affine translation cancels on differences, while the Bloch linear part is a rotation composed with $$\operatorname{diag}(\mathrm e^{-\Gamma_2t},\mathrm e^{-\Gamma_2t},\mathrm e^{-\Gamma_1t}).$$ Its largest singular value is attained on a coordinate axis. Thus:

[\[prop:contract\]]{#prop:contract label="prop:contract"} For $\Gamma_1>0$, $$\sup_{\rho\ne\sigma}
 \frac{\|\Phi_t(\rho)-\Phi_t(\sigma)\|_1}{\|\rho-\sigma\|_1}
 =\max\{\mathrm e^{-\Gamma_1t},\mathrm e^{-\Gamma_2t}\}.$$ It is strictly below one for $t>0$. Hence $\operatorname{diag}(1-p,p)$ is the unique stationary state and every recurrent orbit is constant.

The singular-value calculation gives the upper bound and a sufficiently small pair of Bloch vectors separated along a maximizing axis gives equality. If a trajectory returned after $T>0$, iterating the strict contraction at time $T$ against the fixed state would force its initial distance to be zero.

The degeneracies are not obtained by dividing by $\Gamma_1$:

  -----------------------------------------------------------------------------------------------------------------------------------------------
  Face                                     Fixed states                    EB and recurrence
  ---------------------------------------- ------------------------------- ----------------------------------------------------------------------
  $\Gamma_1>0$, $0<p<1$                    unique faithful thermal state   one finite EB time; no nonconstant recurrence

  $\Gamma_1>0$, $p=0$ or $1$               unique pure endpoint            EB only as $t\to\infty$; no nonconstant recurrence

  $\Gamma_1=0$, $\gamma_\phi>0$            all diagonal states             complete dephasing is EB only at infinity; no nonconstant recurrence

  $\Gamma_1=\gamma_\phi=0$, $\omega\ne0$   all diagonal states             unitary; coherent states have period $2\pi/|\omega|$; never EB

  $\Gamma_1=\gamma_\phi=\omega=0$          every state                     identity; never EB
  -----------------------------------------------------------------------------------------------------------------------------------------------

The Liouvillian kernel has dimension one in the first two rows, two in the third and fourth, and four at the identity corner. This last distinction is essential: the zero generator does not have merely the diagonal kernel.

\>1

# Exact evidence, collisions, and the Route-A firewall

The machine-readable certificate contains 75 exact rational Choi/PPT cells, 12 Liouvillian cases, 10 contraction cases, 12 exact semigroup-composition cells, eight threshold brackets narrower than $10^{-70}$, and seven boundary rows: 124 audited rows in total. An independent checker reconstructs every cell and the exact-type YAML tree; a separate SymPy script derives the algebra; byte replay enforces determinism; and 35 repaired-hash hostile mutations test semantic rejection.

This state space and theorem do not duplicate nearby repository models: C223 is unitary Jaynes--Cummings block motion; C224 is nonautonomous Landau--Zener scattering; C237 is classical Kramers diffusion; C243 is nonlinear Bose--Josephson Hamiltonian flow; C297 is non-CPTP PT-symmetric ray dynamics; and C298 is Grassmann projection flow. Here the state is a density matrix in the Bloch ball, the maps form a CPTP semigroup, and the new boundary is the Choi/PPT entanglement-breaking time.

#### Proves-too-much counterexamples.

A finite Choi determinant exists for every finite-dimensional channel and a finite characteristic polynomial exists for every finite-dimensional Liouvillian, including channels with continuously arbitrary rates. Their mere existence therefore cannot imply prime-power weights or a target global zero divisor. Stinespring dilation does not repair the gap: it is nonunique, enlarges the state space, and is not an autonomous same-clock unitary group for the dissipative semigroup. On the unitary boundary there is only one continuously tunable frequency and a continuum of fixed diagonal states.

The Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
   \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}),$$ with overall verdict `ROUTE_A_REJECTED`. Obstruction HEN-O287 says that exact finite GKSL, Choi, and Liouvillian data do not create arithmetic local data, a prime-log clock, a target analytic divisor, or a same-clock self-adjoint realization. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, Route B is not invoked. No Euler factor, root number, automorphy, target functional equation or zero match, or Hilbert--Pólya operator is claimed.

#### AI-use statement.

AI assistance was used to draft code and prose. The released claims are limited to identities reproduced by the independent exact checks and proofs printed here; no external peer review is represented.

\>1

# Source owners {#source-owners .unnumbered}

The generator form is owned by Gorini--Kossakowski--Sudarshan (DOI [10.1063/1.522979](https://doi.org/10.1063/1.522979)) and Lindblad (DOI [10.1007/BF01608499](https://doi.org/10.1007/BF01608499)). The complete-positivity matrix criterion is due to Choi (DOI [10.1016/0024-3795(75)90075-0](https://doi.org/10.1016/0024-3795(75)90075-0)); the EB characterization follows Horodecki--Shor--Ruskai (DOI [10.1142/S0129055X03001709](https://doi.org/10.1142/S0129055X03001709)) and the two-qubit PPT theorem follows Horodecki--Horodecki--Horodecki (DOI [10.1016/S0375-9601(96)00706-2](https://doi.org/10.1016/S0375-9601(96)00706-2)). No priority claim is made for those standard mechanisms.
