---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-polyak-heavy-ball-stability-route-a"
canonical_tex: "henon_dynamics/henon_polyak_heavy_ball_stability_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_polyak_heavy_ball_stability_route_a/paper/main.pdf"
source_sha256: "ab96fbe182a63ac34b692380a4304e820ea031a250199a3e11f7be6338743f70"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Real-Parameter Heavy-Ball Dynamics on Every SPD Spectral Interval: Exact Jury Triangle, Sharp Root Factor, and Jordan Transients

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_polyak_heavy_ball_stability_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_polyak_heavy_ball_stability_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_polyak_heavy_ball_stability_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_polyak_heavy_ball_stability_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give one complete phase atlas for constant-parameter Polyak heavy-ball dynamics on every real SPD quadratic and for all real step and momentum parameters. Scalar modal reduction yields the exact Jury triangle, including negative momentum, and the exact endpoint root radius. A disk-Jury argument proves the unique minimax Polyak pair. Its endpoint blocks are defective, so the sharp root factor $q$ comes with generic $O(kq^k)$ transients rather than a uniform $Cq^k$ bound. We also close the equal-spectrum nilpotent case, full characteristic data, conformal symplectic identity and every finite-order boundary. Exact independent certificates test the formulas but do not prove the continuum theorem. No claim extends to arbitrary nonlinear objectives or to target arithmetic, and Route A is strictly rejected.
author:
- 'Route-A structural certificate C201'
title: 'Real-Parameter Heavy-Ball Dynamics on Every SPD Spectral Interval: Exact Jury Triangle, Sharp Root Factor, and Jordan Transients'
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** heavy-ball method; Polyak momentum; Jury criterion; quadratic optimization; spectral radius; Jordan block; symplectic map.

chinese-simplified

中文摘要

本文对全部实步长与实动量参数下的正定二次型重球迭代给出完整相图。 模态分解导出包含负动量的精确[Jury]{lang="en"}稳定三角；圆盘判据证明唯一极小极大 [Polyak]{lang="en"}参数。最优端点均为缺陷[Jordan]{lang="en"}块， 因此精确根收敛因子为$q$，但一般瞬态是$O(kq^k)$而非一致$Cq^k$。 本文不把二次型结论推广到一般非线性强凸函数，也不提出目标算术或路线[B]{lang="en"}结论。

关键词：重球法；稳定区域；谱半径；缺陷矩阵；辛边界。

# Modal owner and exact Jury triangle

Let $$f(x)=\tfrac12x^TAx-b^Tx,\qquad 0<mI\le A\le LI,$$ and let $x_*=A^{-1}b$. Polyak's iteration [@P64] gives $$\label{eq:hb}
 e_{k+1}=[(1+\beta)I-\alpha A]e_k-\beta e_{k-1},
 \qquad e_k=x_k-x_* .$$ For an eigenvalue $\lambda$, the scalar characteristic polynomial is $$\label{eq:p}
 p_\lambda(r)=r^2-a_\lambda r+\beta,\qquad
 a_\lambda=1+\beta-\alpha\lambda.$$ For a real monic quadratic, Jury's criterion is $|\beta|<1$, $p_\lambda(1)>0$ and $p_\lambda(-1)>0$. Here $$p_\lambda(1)=\alpha\lambda,\qquad
 p_\lambda(-1)=2(1+\beta)-\alpha\lambda.$$ Therefore the whole spectral class converges for every phase initialization if and only if $$\label{eq:triangle}
 \boxed{-1<\beta<1,\qquad 0<\alpha<2(1+\beta)/L.}$$ This is the complete real-parameter region, not merely the usual $0\le\beta<1$ sector.

For $a\in\mathbb R$, the exact root radius is $$\label{eq:radius}
 R_\beta(a)=
 \begin{cases}
 \sqrt\beta,&\beta\ge0,\ |a|\le2\sqrt\beta,\\
 (|a|+\sqrt{a^2-4\beta})/2,&\text{otherwise}.
 \end{cases}$$ It is nondecreasing in $|a|$ outside the plateau. Since $a_\lambda$ is affine, the robust radius is exactly $\max\{R_\beta(a_m),R_\beta(a_L)\}$.

\>0

# Unique minimax pair

Suppose all roots must lie in $|r|\le\rho<1$. Applying the closed Jury test after $r=\rho z$ gives $$\label{eq:disk}
 |\beta|\le\rho^2,\qquad
 |1+\beta-\alpha\lambda|\le\rho+\beta/\rho.$$ Endpoint feasibility implies $$\label{eq:necessary}
 (L-m)(1+\beta)\le(L+m)(\rho+\beta/\rho).$$ The right side minus the left is strictly increasing in $\beta$ for $0<\rho<1$, so feasibility is easiest only at $\beta=\rho^2$. Hence $$(L-m)(1+\rho^2)\le2\rho(L+m),$$ whose smaller root is $$q=\frac{\sqrt L-\sqrt m}{\sqrt L+\sqrt m}.$$ Equality forces both endpoint inequalities to be equalities and therefore, for $m<L$, uniquely $$\label{eq:polyak}
 \boxed{\alpha_*=\frac{4}{(\sqrt L+\sqrt m)^2},\qquad
 \beta_*=q^2.}$$ This is minimax within real constant-parameter heavy-ball. Related broader asymptotic quadratic optimality is studied in [@UPS23]; no finite-time or unrestricted-algorithm claim is needed here.

If $m=L$, the class contains only $A=mI$. Then $\alpha=1/m,\beta=0$ annihilate the error after one update; the two-step state block is nilpotent of index two. This boundary is not obtained by dividing a Jordan formula by $q=0$.

# The Jordan correction

At [\[eq:polyak\]](#eq:polyak){reference-type="eqref" reference="eq:polyak"}, $$a_m=2q,\quad a_L=-2q,\qquad
 p_m(r)=(r-q)^2,\quad p_L(r)=(r+q)^2.$$ Each endpoint companion matrix is defective. If $M_m=qI+N_+$ and $M_L=-qI+N_-$, then $N_\pm^2=0\ne N_\pm$ and $$M_m^k=q^k(I+kN_+/q),\qquad
 M_L^k=(-q)^k(I-kN_-/q).$$ Thus $q$ is the exact worst-case root-convergence factor, but generic endpoint transients are $O(kq^k)$. For the hostile sentinel $m=1,L=4$, $\alpha_*=4/9$, $\beta_*=1/9$, $q=1/3$ and $e_{-1}=e_0=1$, $$\label{eq:counter}
 e_k=(1+2k/3)3^{-k}.$$ The ratio $|e_k|/q^k$ is unbounded, refuting a uniform $Cq^k$ statement. More generally, for $\beta>0$ the defective mode curves are $\alpha\lambda=(1\pm\sqrt\beta)^2$; at $\beta=0,\alpha\lambda=1$ the block is nilpotent instead.

\>1

# Full phase geometry and finite-order boundary

On $\mathbb R^{2d}$ write $$M_A=\begin{pmatrix}(1+\beta)I-\alpha A&-\beta I\\I&0\end{pmatrix}.$$ Orthogonal diagonalization proves $$\det(rI-M_A)=\prod_{\lambda\in\sigma(A)}p_\lambda(r),\quad
 \operatorname{tr}M_A=d(1+\beta)-\alpha\operatorname{tr}A,
 \quad\det M_A=\beta^d.$$ For $J=\left(\begin{smallmatrix}0&I\\-I&0\end{smallmatrix}\right)$, symmetry of $A$ gives the exact identity $$\label{eq:conformal}M_A^TJM_A=\beta J.$$ At $\beta=1$ a mode with $0<\alpha\lambda<4$ has eigenvalues $e^{\pm i\theta_\lambda}$, where $\cos\theta_\lambda=1-\alpha\lambda/2$. A fixed $A$ gives a finite-order full map precisely when every angle is a rational multiple of $2\pi$ and no endpoint block is parabolic. The other finite-order case is the trivial $\beta=-1,\alpha=0$ swap. A nontrivial continuous interval of $\lambda$ contains irrational angles, so it has no uniform nontrivial finite order.

Fourteen real-parameter sentinels, 28 endpoint blocks, four optimum intervals, the exact sequence [\[eq:counter\]](#eq:counter){reference-type="eqref" reference="eq:counter"}, a rotated SPD control and three finite-order matrices form the release ledger. A checker importing no producer code enforces exact nested schemas; a separate SymPy route, byte replay, eighteen repaired-hash and one stale-hash attacks all pass. These are regression controls, not a finite proof of [\[eq:triangle\]](#eq:triangle){reference-type="eqref" reference="eq:triangle"}.

The theorem is restricted to quadratics. Polyak parameters need not give the same global behavior for arbitrary nonlinear smooth strongly convex objectives; control-theoretic analyses make that boundary important [@LRP16]. There is also no intrinsic prime carrier, prime-power repetition, $\log p$ clock or target determinant. Conformal symplecticity gives only a formal lift hint because the minimax map has $\beta=q^2<1$. Strictly, $$(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},
 \mathrm{FAIL},\mathrm{FORMAL\ HINT}),$$ overall `ROUTE_A_REJECTED`, Route B false, under `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Claim firewall.

We claim no classical priority, unrestricted algorithmic optimality, nonlinear global theorem, target zero or prime data, arithmetic local datum, Euler factor, root number, automorphy, target functional equation, Weil compression, Hilbert--Pólya operator, external review or acceptance score.

#### Revision focus.

Round 0 closes the modal family, exact all-real Jury triangle and endpoint radius.

#### Revision focus.

Round 1 adds the unique minimax proof, equal-spectrum boundary and Jordan-correct hostile counterexample.

#### Revision focus.

Round 2 adds phase determinants, conformal symplecticity, finite-order controls, validation and all claim firewalls.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

Package-local synthetic exact evidence and deterministic code accompany the manuscript.

#### Ethics.

No human, animal, personal or sensitive data are used; approval is not applicable.

#### Author contributions (CRediT).

This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing. AI systems are not authors.

#### Funding.

No external funding is reported.

#### Conflicts of interest.

None known.

#### AI-use disclosure.

An AI coding assistant supported drafting and exact-code development; it was not an external reviewer or independent error process.

3 B. T. Polyak, "Some methods of speeding up the convergence of iteration methods," *USSR Comput. Math. Math. Phys.* 4 (1964), 1--17. DOI: 10.1016/0041-5553(64)90137-5. V. Ugrinovskii, I. R. Petersen and I. Shames, "A robust control approach to asymptotic optimality of the heavy ball method for optimization of quadratic functions," *Automatica* 155 (2023), 111129. DOI: 10.1016/j.automatica.2023.111129. L. Lessard, B. Recht and A. Packard, "Analysis and design of optimization algorithms via integral quadratic constraints," *SIAM J. Optim.* 26 (2016), 57--95. DOI: 10.1137/15M1009597.
