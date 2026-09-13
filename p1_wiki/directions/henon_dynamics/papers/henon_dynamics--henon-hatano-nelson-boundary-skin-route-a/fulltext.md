---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-hatano-nelson-boundary-skin-route-a"
canonical_tex: "henon_dynamics/henon_hatano_nelson_boundary_skin_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_hatano_nelson_boundary_skin_route_a/paper/main.pdf"
source_sha256: "1504fb08f31e16a1d33b1a39d4b5803b483370db43efe33bec9a3ea09835bf31"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Boundary and Skin Atlas for the Finite Hatano--Nelson Chain

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_hatano_nelson_boundary_skin_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_hatano_nelson_boundary_skin_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_hatano_nelson_boundary_skin_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_hatano_nelson_boundary_skin_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We solve the finite asymmetric nearest-neighbor chain across its full hopping cone. Positive open-boundary hopping is diagonally similar to a symmetric path matrix, yielding the exact Chebyshev spectrum. \>0 We also obtain a canonical biorthogonal sine basis, distinguish its asymmetry-free density from the right-amplitude skin envelope, and give exact conditioning, propagation, and resolvent formulas. \>1 Periodic Fourier spectra and every Hermitian, one-sided, zero, orientation-reversed, and small-size face complete the atlas. The singular open/periodic split is proved without a topology, disorder, or arithmetic claim.
author:
- 'Route-A candidate HCS-C308'
date: 3 September 2026
title: |
  An Exact Boundary and Skin Atlas\
  for the Finite Hatano--Nelson Chain
```

## Markdown 正文

trailerid \[\<C3082026090300000000000000000000\>\<C3082026090300000000000000000000\>\]

# Model and the algebraic core

For $N\ge2$, let the open-boundary matrix $H_N=H_N(t_R,t_L)$ have $(H_N)_{j,j+1}=t_R$ and $(H_N)_{j+1,j}=t_L$, where $t_R,t_L\ge0$. Evolution means $\mathrm{i}\dot\psi=H_N\psi$. When both hoppings are positive, put $$g=\sqrt{t_Rt_L},\qquad q=\sqrt{t_L/t_R},\qquad
 D=\operatorname{diag}(1,q,\ldots,q^{N-1}),$$ and let $A_N$ be path adjacency. Define $$\theta_m=\frac{m\pi}{N+1},\qquad
 S_{jm}=\sqrt{\frac{2}{N+1}}\sin(j\theta_m),\qquad 1\le j,m\le N.$$

For $t_R,t_L>0$, $$D^{-1}H_ND=gA_N,
 \quad \det(zI-H_N)=g^NU_N\!\left(\frac{z}{2g}\right),
 \quad E_m=2g\cos\theta_m .                                      \tag{1}$$ The $E_m$ are real and simple. \>0 In the canonical sine gauge, $$R=DS,\quad L^T=S^TD^{-1},\quad L^TR=I,\quad
 \kappa_2(R)=\max(q,q^{-1})^{N-1}.                                \tag{2}$$ Moreover, $$\mathrm{e}^{-\mathrm{i}tH_N}=DS\operatorname{diag}(\mathrm{e}^{-\mathrm{i}tE_m})S^TD^{-1},
 \qquad (zI-H_N)^{-1}=D(zI-gA_N)^{-1}D^{-1}.                       \tag{3}$$ For $x=z/(2g)$ and $z\notin\sigma(H_N)$, $$[(zI-H_N)^{-1}]_{ij}=
 \frac{q^{i-j}U_{\min(i,j)-1}(x)U_{N-\max(i,j)}(x)}{gU_N(x)}.     \tag{4}$$ \>1 For the oriented ring with $N\ge3$, let $(Cv)_j=v_{j+1\bmod N}$ and $H_N^{\rm per}=t_RC+t_LC^{-1}$. It is normal and its Fourier spectrum is $$E_m^{\rm per}=t_R\mathrm{e}^{\mathrm{i}k_m}+t_L\mathrm{e}^{-\mathrm{i}k_m},\qquad
 k_m=2\pi m/N.                                                     \tag{5}$$ Thus $\Re E_m^{\rm per}=(t_R+t_L)\cos k_m$ and $\Im E_m^{\rm per}=(t_R-t_L)\sin k_m$.

On $t_R=t_L>0$ both matrices are Hermitian. If exactly one hopping is positive, OBC is one nilpotent $N$-Jordan block, while PBC is a unitarily diagonalizable scaled cyclic shift. If both vanish, the matrix is zero with eigenspace dimension $N$. Swapping $t_R,t_L$ transposes OBC, reverses its right-amplitude edge, and complex-conjugates the PBC ellipse.

Since $D_j^{-1}t_RD_{j+1}=t_Rq=g$ and $D_{j+1}^{-1}t_LD_j=t_L/q=g$, diagonal conjugation gives the first identity. Laplace expansion produces the continuant $$P_0=1,\quad P_1=z,\quad P_N=zP_{N-1}-t_Rt_LP_{N-2}.$$ The recurrence for $U_N$ gives (1). The discrete sine transform is orthogonal and diagonalizes $A_N$, which proves simplicity and reality. \>0 Conjugating its columns gives $R$, while $S^TD^{-1}$ is the exact left dual. Right multiplication by orthogonal $S$ preserves singular values, so the extreme diagonal entries of $D$ give (2). This equality concerns the stated sine gauge; arbitrary column rescaling changes an eigenvector-matrix condition number. Functional calculus gives (3). The standard continuant formula for the inverse of $zI-gA_N$, followed by diagonal conjugation, gives (4). Consequently, for real $t$, $$\|\mathrm{e}^{-\mathrm{i}tH_N}\|_2\le\kappa_2(D),\qquad
 \|(zI-H_N)^{-1}\|_2\le
 \frac{\kappa_2(D)}{\operatorname{dist}(z,\sigma(H_N))}.           \tag{6}$$ These are bounds, not asserted equalities. \>1 The unitary Fourier basis diagonalizes $C$, proving (5), the ellipse parametrization, and normality. On a one-sided OBC axis the surviving shift satisfies $H^N=0$, $H^{N-1}\ne0$, and $\operatorname{rank}(H^k)=N-k$; hence there is one Jordan chain of length $N$. On the ring, $C^N=I$ and its Fourier eigenvalues are distinct. Direct substitution proves the Hermitian, zero, and orientation statements.

\>0

# What is, and is not, skin localization

The right and left components in the canonical dual normalization are $$R_{jm}=q^{j-1}S_{jm},\qquad L^T_{mj}=q^{-(j-1)}S_{jm}.$$ Thus ordinary right amplitudes carry an exponential envelope toward the left for $q<1$ and toward the right for $q>1$. Pointwise biorthogonal density is a different object: $$L^T_{mj}R_{jm}=S_{jm}^2,$$ which is independent of $q$ and sums to one. We use "skin" only for the first, amplitude-level statement.

\>1

# Boundary faces and a singular limit

At fixed $N$, taking $t_L\downarrow0$ with $t_R>0$ collapses every positive-OBC eigenvalue to zero and sends the canonical conditioning in (2) to infinity. The limit is defective. Under PBC, the same limit has eigenvalues $t_R\mathrm{e}^{\mathrm{i}k_m}$ and keeps its Fourier eigenbasis. The transpose statement holds when $t_R\downarrow0$. This proves a boundary-condition-sensitive singular limit; it does not prove a winding invariant or a protected edge mode.

The one-sided OBC formulas also close dynamically: $$\mathrm{e}^{-\mathrm{i}tH}=\sum_{k=0}^{N-1}\frac{(-\mathrm{i}tH)^k}{k!},\qquad
 (zI-H)^{-1}=\sum_{k=0}^{N-1}\frac{H^k}{z^{k+1}}\quad(z\ne0).$$ For $N=2$, the OBC theorem remains unchanged. A two-site cyclic shift obeys $C=C^{-1}$, so the two oriented neighbors coincide and $H_2^{\rm per}=(t_R+t_L)C$. We therefore state the standard oriented-ring ellipse theorem for $N\ge3$ and record $N=2$ only as this explicit convention face. At finite $N$, (5) gives finitely many points on an ellipse, not the entire ellipse.

# Executable evidence and scope

The analytic proof covers all stated $N$ and parameter faces. Finite evidence is regression only: 40 positive-OBC continuants and condition numbers, 21 resolvent determinant/log-derivative traces, 18 one-sided Jordan/PBC cases, 36 PBC power-trace cases, and eight semantic boundary faces (123 rows total). An independent checker recomputes every cell with strict JSON/YAML types; a separate symbolic lane checks the identities; isolated double replay demands byte equality; and repaired-hash mutations attack formulas, owners, boundaries, types, lists, and parsers.

The Route-A tuple is $(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
\mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT})$ and the overall verdict is `ROUTE_A_REJECTED`; Route B is locked. A finite Chebyshev determinant is not an Euler factor, the finite spectrum is not a target zero set, and a nonunitary similarity to a source-local symmetric matrix is not a same-clock self-adjoint Hilbert--Pólya construction. We claim no disorder localization, interactions, topological invariant, automorphy, root number, or literature priority. The frozen scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### AI-use disclosure.

An AI system assisted with algebraic organization, code generation, and prose. Every released formula is supported by the displayed proof and independent executable checks; source ownership and claim boundaries were reviewed explicitly. No external review or authorship is represented.

9 N. Hatano and D. R. Nelson, "Localization transitions in non-Hermitian quantum mechanics," *Phys. Rev. Lett.* 77 (1996), 570--573. doi:10.1103/PhysRevLett.77.570. N. Hatano and D. R. Nelson, "Non-Hermitian delocalization and eigenfunctions," *Phys. Rev. B* 58 (1998), 8384--8390. doi:10.1103/PhysRevB.58.8384. \>1 S. Yao and Z. Wang, "Edge states and topological invariants of non-Hermitian systems," *Phys. Rev. Lett.* 121 (2018), 086803. doi:10.1103/PhysRevLett.121.086803. Used for terminology only.
