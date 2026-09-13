---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-sinkhorn-knopp-projective-scaling-route-a"
canonical_tex: "henon_dynamics/henon_sinkhorn_knopp_projective_scaling_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_sinkhorn_knopp_projective_scaling_route_a/paper/main.pdf"
source_sha256: "54c090b37afd3fe8b3507b5627f93a2d00627fc28817f3229bf6f1d5b6391845"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Sinkhorn--Knopp Dynamics on Every Support Stratum: Exact Scalability, Projective Contraction, and the Local Rate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_sinkhorn_knopp_projective_scaling_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_sinkhorn_knopp_projective_scaling_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_sinkhorn_knopp_projective_scaling_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_sinkhorn_knopp_projective_scaling_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every square nonnegative matrix we classify alternating row--column normalization by support, total support and full indecomposability. The source-locked theorem separates convergence, finite positive diagonal scalability, uniqueness of the doubly stochastic representative and gauge uniqueness of its factors. On the positive stratum, Hilbert distance gives a data-dependent geometric contraction, while direct log-coordinate differentiation gives the exact full-cycle Jacobian $S^TS$ and local rate $\sigma_2(S)^2$. Exact zero-pattern and rational-matrix oracles test every boundary without replacing the all-matrix proof. Convergence leaves no nonconstant primitive-orbit owner, and the scaling data has no intrinsic rational-prime semantics or source-native Hilbert quantization.
author:
- 'Route-A structural certificate C191'
title: |
  Sinkhorn--Knopp Dynamics on Every Support Stratum:\
  Exact Scalability, Projective Contraction, and the Local Rate
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** matrix scaling; Sinkhorn--Knopp; total support; Hilbert metric; projective contraction; local convergence rate.

chinese-simplified

中文摘要

本文对任意方形非负矩阵的交替行列归一化给出统一分层：支撑决定是否收敛，完全支撑决定 是否存在有限正对角缩放，完全不可分解决定缩放因子的规范唯一性。在严格正矩阵层， [Hilbert]{lang="en"}射影度量给出依赖数据的几何压缩；在双随机极限$S$处，对数坐标下完整一步的 [Jacobian]{lang="en"}恰为$S^TS$，局部速率为$\sigma_2(S)^2$。精确零模式与有理迭代仅作回归验证。 收敛动力学没有非平凡本原周期轨道，也不产生内生的有理素数语义或[Hilbert]{lang="en"}空间量子化。

关键词：矩阵缩放；完全支撑；射影压缩；局部收敛速率。

# One all-matrix classification

Let $A\ge0$ have no zero row or column. Write $R(B)$ and $C(B)$ for row and column normalization and freeze one clock step $\mathcal S(B)=C(R(B))$. A positive diagonal is a permutation $\pi$ with $\prod_i a_{i\pi(i)}>0$. The matrix has *support* if one exists, *total support* if every positive entry belongs to one, and is *fully indecomposable* if no independent row and column permutations expose a nontrivial rectangular zero corner.

Sinkhorn and Knopp [@SK67] prove that $\mathcal S^k(A)$ converges to a doubly stochastic limit exactly when $A$ has support. The limit is reachable as $D_1AD_2$ with finite positive diagonal factors exactly on total support. The doubly stochastic representative is unique. The Brualdi--Parter--Schneider theorem [@BPS66] identifies the sharper gauge boundary: the factors are unique up to $(D_1,D_2)\mapsto(cD_1,c^{-1}D_2)$ exactly on a fully indecomposable block. If support is not total, positive entries outside every positive diagonal tend to zero; no finite positive factors can produce that limit.

# Projective dynamics and exact local rate

Assume $A>0$. On positive column rays the full scaling-vector update is $$T_A(x)=\left[A^T\bigl((Ax)^{-1}\bigr)\right]^{-1},$$ with componentwise inverses. For Hilbert distance $d_H$, set $$\Theta(A)=\max_{i,j,k,l}\frac{a_{ik}a_{jl}}{a_{il}a_{jk}},\qquad
 \kappa(A)=\frac{\sqrt{\Theta(A)}-1}{\sqrt{\Theta(A)}+1}.$$ Birkhoff contraction applied to $A$ and $A^T$ yields $$\label{eq:contraction}
 d_H(T_Ax,T_Ay)\le\kappa(A)^2d_H(x,y),$$ the Franklin--Lorenz geometric mechanism [@FL89]. This coefficient is data-dependent and approaches one as projective diameter diverges.

Let $S>0$ be the doubly stochastic limit. In logarithmic column-scaling coordinates $u$, the convention-locked map is $$F(u)=-\log\!\left(S^T\exp[-\log(S\exp u)]\right).$$ Differentiating at zero gives $DF(0)=S^TS$. The gauge vector $\mathbf 1$ has eigenvalue one; on the quotient $\mathbf 1^\perp$ the spectral radius is $$\label{eq:rate}
 \rho_{\rm loc}=\sigma_2(S)^2<1,$$ in agreement with the local-rate analysis of Knight [@K08]. Equation [\[eq:rate\]](#eq:rate){reference-type="eqref" reference="eq:rate"} is local and asymptotic, not a global equality at every step.

# Sharp boundaries, evidence, and Route-A stop

The exact ledger contains all 272 declared order-two and order-three patterns, four positive scaling cases, four hostile boundary cases, 242 repaired-hash rejections and one stale-hash rejection. A producer-independent matching/connectivity checker passes 2,411 assertions; a separate SymPy/Ryser path passes 951 checks; replay is byte exact. The nonsymmetric target makes $S^TS\ne S^2$ and closes a transpose blind spot. These are regression oracles, not a finite proof of the source theorems.

Every supported full-cycle orbit converges. If such an orbit is periodic, it is therefore fixed. This algorithmic fixed point is not an arithmetic primitive orbit. Matchings, scaling factors and singular values provide no rational-prime carrier, prime-power repetition, $\log p$ clock, target divisor, functional equation or source-native self-adjoint quantization. Thus $$(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},
 \mathrm{FAIL},\mathrm{FAIL}),$$ overall `ROUTE_A_REJECTED`, Route B false, under `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Ownership and limitations.

The convergence, scalability, uniqueness, Hilbert-contraction and local-rate results belong to the cited sources. This package owns only their convention-consistent synthesis, elementary Jacobian derivation, executable boundary certificate and strict Route-A audit. It claims no dimension-only rate, no positive factors without total support, no classical priority, no target arithmetic object and no external review.

#### Revision-round focus.

Round 0 freezes the full support, total-support and factor-gauge classification.

#### Revision-round focus.

Round 1 adds the positive Hilbert contraction, exact local Jacobian and four sharp zero-pattern boundaries.

#### Revision-round focus.

Round 2 separates source ownership from finite regression and closes recurrence, semantic mutation and Route-A gates.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

Package-local exact evidence and deterministic code accompany this manuscript.

#### Ethics.

No human, animal, clinical, personal or sensitive data are used; approval is not applicable.

#### Author contributions (CRediT).

This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing. AI systems are not authors.

#### Funding.

No external funding is reported.

#### Conflicts of interest.

None known.

#### AI-use disclosure.

An AI coding assistant supported drafting and exact-code development; it was not an external reviewer or independent error process.

4 R. Sinkhorn and P. Knopp, "Concerning nonnegative matrices and doubly stochastic matrices," *Pacific J. Math.* 21(2) (1967), 343--348. DOI: 10.2140/pjm.1967.21.343. R. A. Brualdi, S. V. Parter and H. Schneider, "The diagonal equivalence of a nonnegative matrix to a stochastic matrix," *J. Math. Anal. Appl.* 16(1) (1966), 31--50. DOI: 10.1016/0022-247X(66)90184-3. J. Franklin and J. Lorenz, "On the scaling of multidimensional matrices," *Linear Algebra Appl.* 114--115 (1989), 717--735. DOI: 10.1016/0024-3795(89)90490-4. P. A. Knight, "The Sinkhorn--Knopp algorithm: convergence and applications," *SIAM J. Matrix Anal. Appl.* 30(1) (2008), 261--275. DOI: 10.1137/060659624.
