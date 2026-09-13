---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-network-sis-threshold-critical-route-a"
canonical_tex: "henon_dynamics/henon_network_sis_threshold_critical_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_network_sis_threshold_critical_route_a/paper/main.pdf"
source_sha256: "e98f8455e135a424e2458dac982ce815b416addd956f72030c6d32b7f47fca0b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Sharp Threshold Atlas for Irreducible Network SIS: Global Endemicity and the Critical Perron Law

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_network_sis_threshold_critical_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_network_sis_threshold_critical_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_network_sis_threshold_critical_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_network_sis_threshold_critical_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close the full phase portrait of the deterministic susceptible--infected--susceptible flow on an irreducible heterogeneous network. The spectral abscissa of the linearized Metzler matrix separates extinction from a unique endemic state. \>0 Above threshold, strict subhomogeneity gives global attraction, a Hurwitz endemic Jacobian, and componentwise transmission-rate monotonicity. \>1 At equality, normalized Perron vectors give the sharp vector law $t x(t)\to v/[\beta w^T\!\operatorname{diag}(v)Av]$; 240 exact parameter rows and 720 equality samples audit every convention. No epidemic object is promoted to an arithmetic orbit or target determinant.
author:
- 'Route-A source-local certificate HCS-C271'
date: 1 September 2026
title: |
  A Sharp Threshold Atlas for Irreducible Network SIS:\
  Global Endemicity and the Critical Perron Law
```

## Markdown 正文

suppressoptionalinfo 767 trailerid \[\<C2712026090100000000000000000000\>\<C2712026090100000000000000000000\>\]

# Frozen network flow

Let $A\ge0$ be irreducible, let $D=\operatorname{diag}(\delta_i)$ with $\delta_i>0$, and let $\beta>0$. On $Q=[0,1]^n$ consider $$\dot x=\beta\operatorname{diag}(1-x)Ax-Dx,
 \qquad M=\beta A-D.                                      \tag{1}$$ This is the physical ODE clock. Lajmanovich and Yorke established the classical nonhomogeneous deterministic epidemic lineage [@LY]; all normalizations below are stated locally.

At $x_i=0$, the $i$th component of the vector field is nonnegative; at $x_i=1$ it equals $-\delta_i$. Thus $Q$ is invariant. Irreducibility and cooperativity make every nonzero orbit strictly positive for positive time.

If $s(M)<0$, zero is globally exponentially stable. If $s(M)=0$, zero is globally asymptotically stable. If $s(M)>0$, (1) has exactly one $x_*\in(0,1)^n$, and $x_*$ attracts every nonzero point of $Q$.

For $s=s(M)\le0$, choose $w\gg0$ with $w^TM=sw^T$. Then $$\frac d{dt}w^Tx=s w^Tx-\beta w^T\operatorname{diag}(x)Ax.$$ This proves exponential decay for $s<0$ and, by positivity and LaSalle's argument, convergence to zero at equality. For $s>0$, a small Perron vector is a strict subsolution and $\mathbf1$ is a strict supersolution. Existence follows by monotone iteration. On positive states, $$f(\theta x)-\theta f(x)=
 \beta\theta(1-\theta)\operatorname{diag}(x)Ax\gg0,
 \quad0<\theta<1.                                        \tag{2}$$ Largest- and smallest-ratio comparisons use (2) to prove uniqueness and to squeeze every positive orbit to $x_*$.

\>0

# Endemic stability and monotonicity

At the endemic state, $$J_*=\beta\operatorname{diag}(1-x_*)A
 -\beta\operatorname{diag}(Ax_*)-D.                      \tag{3}$$ It is irreducible Metzler and $J_*x_*=-\beta\operatorname{diag}(Ax_*)x_*\ll0$; hence $J_*$ is Hurwitz. Differentiating the equilibrium equation gives $$\frac{dx_*}{d\beta}=-J_*^{-1}\operatorname{diag}(1-x_*)Ax_*\gg0, \tag{4}$$ because $-J_*^{-1}$ is strictly positive. Equations (3)--(4) close both the local spectrum and the parameter direction, rather than stopping at an existence threshold.

\>1

# The critical $1/t$ law

Assume $s(M)=0$. Normalize $Mv=0$, $w^TM=0$, $v,w\gg0$ by $w^Tv=1$, and set $$\kappa=\beta w^T\operatorname{diag}(v)Av>0.              \tag{5}$$ The zero eigenvalue is simple and the complementary spectrum is strictly stable. Put $P=vw^T$, $Q=I-P$, $E=\ker w^T$, and write $x=av+y$ with $a=w^Tx>0$ and $y=Qx\in E$. For $N(x)=-\beta\operatorname{diag}(x)Ax$, $$\dot a=w^TN(x),\qquad \dot y=M|_E y+QN(x).               \tag{6}$$ Because $w\gg0$ and $x\ge0$, $a\asymp\lVert x\rVert_1$; hence $y=O(a)$ and $|\dot a|=O(a^2)$. The bounded quotient $z=y/a$ obeys $$\dot z=M|_E z+QN(x)/a-(\dot a/a)z.$$ Critical extinction makes the last two terms tend to zero, while $M|_E$ is exponentially stable. Variation of constants gives $z\to0$. Therefore $$-\dot a/a^2=\beta w^T\operatorname{diag}(x/a)A(x/a)\to\kappa.$$ Thus $(1/a)'\to\kappa$, $ta\to1/\kappa$, and $x/a=v+z\to v$. Consequently $$t x(t)\longrightarrow v/\kappa.              \tag{7}$$ For an $r$-regular graph with uniform recovery $\delta$, $v=\mathbf1$ and $w=\mathbf1/n$; equality means $\beta r=\delta$, so (7) becomes $t x(t)\to\mathbf1/\delta$. The invariant diagonal solves exactly $y'=-\delta y^2$.

# Executable receipt and Route-A boundary

The canonical receipt contains 20 irreducible regular graphs, 240 exact threshold rows, and 720 rational critical samples. A producer-independent checker rebuilds connectivity, spectra, equilibria, Jacobian rates, and critical solutions; a separate symbolic reconstruction, fresh byte replay, and repaired-hash hostile suite close the release. Finite rows test formulas; the preceding argument proves the arbitrary-network theorem.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is $$\texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FAIL)},$$ overall `ROUTE_A_REJECTED`; Route B is disabled. A threshold, Perron vector, or endemic Jacobian is not a prime clock, primitive-orbit ledger, target divisor, or Hilbert--Pólya operator.

9 A. Lajmanovich and J. A. Yorke, *A deterministic model for gonorrhea in a nonhomogeneous population*, Mathematical Biosciences 28 (1976), 221--236, [doi:10.1016/0025-5564(76)90125-5](https://doi.org/10.1016/0025-5564(76)90125-5).
