---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-wannier-stark-bloch-route-a"
canonical_tex: "henon_dynamics/henon_wannier_stark_bloch_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_wannier_stark_bloch_route_a/paper/main.pdf"
source_sha256: "dad71bd601fdf6dc3b97a608b8bef8a875e2901ddd75ff37054a4d8403b65276"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Bloch Oscillations and Schatten Boundaries for the Wannier--Stark Lattice

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_wannier_stark_bloch_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_wannier_stark_bloch_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_wannier_stark_bloch_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_wannier_stark_bloch_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the uniform-field tight-binding Hamiltonian on $\ell^2(\mathbb Z)$ we give one all-parameter closure: a periodic Fourier gauge, the simple Wannier--Stark ladder and Bessel basis, the exact propagator and least identity return. \>0 We also derive the delta-source probability shell and second moment, including the zero-hopping and changed-owner zero-field faces. \>1 Finally we separate compact resolvent from noncompact unitary dynamics and prove the sharp resolvent Schatten threshold. No infinite-dimensional conclusion is inferred from finite truncation.
author:
- 'Route-A source-local certificate HCS-C267'
date: 31 August 2026
title: |
  Exact Bloch Oscillations and Schatten Boundaries\
  for the Wannier--Stark Lattice
```

## Markdown 正文

trailerid \[\<C2672026083100000000000000000000\>\<C2672026083100000000000000000000\>\]

# Frozen owner and unitary normal form

For $F,J\in\mathbb R$, $F\ne0$, set $$(H\psi)_n=Fn\psi_n-J(\psi_{n+1}+\psi_{n-1})                 \tag{1}$$ on the domain of multiplication by $n$ in $\ell^2(\mathbb Z)$. This is the one-band uniform-field lattice associated with the Wannier--Stark problem [@Wannier]; exact lattice propagators in this setting were studied by Yellin [@Yellin]. These citations establish lineage, not novelty.

Fix the convention $(\mathcal F\psi)(k)=\sum_{n\in\mathbb Z}\psi_ne^{ink}$ into $L^2(\mathbb T,dk/2\pi)$. Then $$\widehat H=-iF\partial_k-2J\cos k.$$ Let $G$ multiply by $\exp[-i(2J/F)\sin k]$. Direct differentiation gives $$\widehat H=G^{-1}(-iF\partial_k)G.                         \tag{2}$$ The sign in (2) is part of the contract: reversing it reverses the hopping.

$H$ has simple pure-point spectrum $F\mathbb Z$. A complete orthonormal eigenbasis is $$\phi_m(n)=\mathrm J_{n-m}(2J/F),\qquad H\phi_m=Fm\phi_m.   \tag{3}$$

The circle momentum in (2) has the simple orthonormal eigenbasis $e^{imk}$. Applying $G^{-1}$ and using $e^{ia\sin k}=\sum_r\mathrm J_r(a)e^{irk}$ gives (3), including its index. Equivalently, the Bessel recurrence $\mathrm J_{r-1}(a)+\mathrm J_{r+1}(a)=2r\mathrm J_r(a)/a$ verifies the eigen-equation. Gauge unitarity supplies completeness and orthonormality, rather than a finite-volume limit.

# Exact evolution and least return

For all $m,n\in\mathbb Z$ and $t\in\mathbb R$, $$U_{nm}(t)=i^{n-m}e^{-iFt(n+m)/2}
 \mathrm J_{n-m}\!\left(\frac{4J}{F}\sin\frac{Ft}{2}\right). \tag{4}$$ The least positive $T$ for which $U(T)=I$ on the full space is $T_B=2\pi/|F|$.

Solving the Fourier transport equation along characteristics, or inserting (3) and applying the Bessel addition formula, yields (4). Its off-diagonal sentinel is $U_{m+1,m}(t)=+iJt+O(t^2)$, as required by $U(t)=I-itH+O(t^2)$. At $T_B$, the Bessel argument is zero and the diagonal phase is one, so $U(T_B)=I$. Conversely, $U(T)=I$ applied to the eigenvalues $0$ and $F$ forces $e^{-iFT}=1$; hence no smaller positive return exists.

\>0

# Probability shell, moment, and boundary atlas

For $\psi(0)=\delta_0$, put $z(t)=(4J/F)\sin(Ft/2)$. Formula (4) gives the exact shell $$\mathbb P\{X_t=n\}=|U_{n0}(t)|^2=\mathrm J_n(z(t))^2.       \tag{5}$$ The characteristic function of (5) is $\mathrm J_0(2z\sin(q/2))$. Its value and first two derivatives at zero give $$\sum_n\mathbb P\{X_t=n\}=1,\quad \mathbb E X_t=0,\quad
 \mathbb E X_t^2=\frac{z(t)^2}{2}=\frac{8J^2}{F^2}\sin^2\frac{Ft}{2}. \tag{6}$$ Thus spreading is bounded and returns exactly, not just asymptotically.

When $J=0$, (1) is diagonal: (2)--(4) and the least return remain valid, while (5) is frozen at zero. The limit $F=0$ with $J\ne0$ changes owner. Fourier multiplication by $-2J\cos k$ has absolutely continuous spectrum $[-2|J|,2|J|]$, kernel $i^{n-m}\mathrm J_{n-m}(2Jt)$, and no positive full-space identity return. It is therefore not inserted into the $F\ne0$ theorem.

\>1

# Sharp operator-ideal boundary

Every $U(t)$ is noncompact and belongs to no finite Schatten class. For $\lambda\notin F\mathbb Z$, $$(H-\lambda)^{-1}\in\mathcal S_p\quad\Longleftrightarrow\quad p>1.$$ In particular, the resolvent is compact and Hilbert--Schmidt but not trace class.

A unitary on an infinite-dimensional Hilbert space sends an orthonormal sequence to another orthonormal sequence, which has no norm-convergent subsequence; compactness fails. Every finite Schatten class is contained in the compact operators. By (3), the resolvent singular values are exactly $|Fm-\lambda|^{-1}$, $m\in\mathbb Z$. Their $p$th powers form a two-sided series comparable to $|F|^{-p}\sum_{m\ne0}|m|^{-p}$, which converges exactly for $p>1$.

# Executable certificate and Route-A boundary

The deterministic receipt contains 210 signed parameter--time rows, 1,050 kernel cells, 5,250 shell cells, and 1,890 eigen cells. An implementation independent of the producer closes 12,335 assertions, including direct Schrödinger residuals that fix all phases and indices. SymPy closes 142 identities, byte replay is exact, and repaired-hash hostile testing rejects 20/20 changes. These are regression sentinels; equations (2)--(6) and the operator arguments above prove the infinite-dimensional claims.

The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`. This owner supplies a natural self-adjoint quantum Hamiltonian and an exact return clock, but no target arithmetic local data, Euler factors, root numbers, automorphy, target divisor, functional equation, or target Hilbert--Pólya identification. The strict tuple is $$\texttt{(A0\_FAIL,A1\_WEAK,A2\_FAIL,A3\_FAIL,A4\_NATURAL\_QUANTIZATION)}.$$ The verdict is `ROUTE_A_REJECTED`; Route B is disabled.

9 G. H. Wannier, *Wave Functions and Effective Hamiltonian for Bloch Electrons in an Electric Field*, Phys. Rev. **117** (1960), 432, [doi:10.1103/PhysRev.117.432](https://doi.org/10.1103/PhysRev.117.432). J. Yellin, *Two exact lattice propagators*, Phys. Rev. E **52** (1995), 2208, [doi:10.1103/PhysRevE.52.2208](https://doi.org/10.1103/PhysRevE.52.2208).
