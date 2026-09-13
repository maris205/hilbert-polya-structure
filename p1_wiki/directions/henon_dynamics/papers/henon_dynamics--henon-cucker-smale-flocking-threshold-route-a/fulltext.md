---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-cucker-smale-flocking-threshold-route-a"
canonical_tex: "henon_dynamics/henon_cucker_smale_flocking_threshold_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_cucker_smale_flocking_threshold_route_a/paper/main.pdf"
source_sha256: "291c746e5223c291c5a0cf7da7fddf118a1931c0072d5b662c71b29522562f81"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Sharp Tail Barrier for Cucker--Smale Flocking

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_cucker_smale_flocking_threshold_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_cucker_smale_flocking_threshold_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_cucker_smale_flocking_threshold_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_cucker_smale_flocking_threshold_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the normalized Cucker--Smale flow we prove global existence, conserved mean velocity, exact variance dissipation, and a diameter comparison principle. The communication tail gives explicit confinement and exponential alignment, including unconditional flocking at the critical exponent $\beta=1/2$. A scalar two-particle reduction proves the short-range threshold sharp and separates its zero-speed/unbounded-distance equality orbit from positive-speed escape. This round is the **global diameter-barrier owner**.
author:
- 'HCS-C362 / HEN-O346'
date: 4 September 2026
title: 'A Sharp Tail Barrier for Cucker--Smale Flocking'
```

## Markdown 正文

suppressoptionalinfo 512 trailerid \[\<C3622026090400000000000000000000\>\<C3622026090400000000000000000000\>\]

# Model and all-particle barrier

For $N\ge2$, $d\ge1$, $K>0$, and $\beta\ge0$, set $$\label{eq:model}
 \dot x_i=v_i,\qquad
 \dot v_i=\frac K N\sum_{j=1}^N\psi(|x_j-x_i|)(v_j-v_i),
 \qquad \psi(r)=(1+r^2)^{-\beta}.$$ Write $\bar v=N^{-1}\sum_i v_i$ and $X=\max_{i,j}|x_i-x_j|$, $V=\max_{i,j}|v_i-v_j|$.

[\[thm:main\]]{#thm:main label="thm:main"} Equation [\[eq:model\]](#eq:model){reference-type="eqref" reference="eq:model"} has a unique global classical solution. The mean velocity is constant and $$\label{eq:energy}
 \frac d{dt}\frac1N\sum_i|v_i-\bar v|^2
 =-\frac K{N^2}\sum_{i,j}\psi(|x_i-x_j|)|v_i-v_j|^2.$$ The upper Dini derivatives satisfy $$\label{eq:diam}
 D^{+}X\le V,\qquad D^{+}V\le-K\psi(X)V.$$ If $$\label{eq:condition}
 V(0)<K\int_{X(0)}^\infty\psi(s)\,ds,$$ there is a unique $R\ge X(0)$ such that $K\int_{X(0)}^R\psi=V(0)$, and $$\label{eq:bounds}
 X(t)\le R,\qquad V(t)\le V(0)e^{-K\psi(R)t}.$$ Every $x_i-x_j$ converges and every $v_i$ converges to $\bar v$. Consequently every initial state flocks when $0\le\beta\le1/2$.

For any direction, the largest velocity projection cannot increase and the smallest cannot decrease; hence the velocity convex hull is invariant. Velocities remain bounded, positions grow at most linearly, and local existence extends globally. Pair symmetry gives $\sum_i\dot v_i=0$ and, after pairing $(i,j)$ with $(j,i)$, gives [\[eq:energy\]](#eq:energy){reference-type="eqref" reference="eq:energy"} with its ordered-pair normalization.

If $V=0$, all velocities coincide, every alignment acceleration vanishes, and the second inequality in [\[eq:diam\]](#eq:diam){reference-type="eqref" reference="eq:diam"} is immediate. Otherwise, at a velocity-diameter pair $(p,q)$ put $e=(v_p-v_q)/V$ and $z_j=e\cdot v_j$. Then $z_q\le z_j\le z_p$. Every weight is at least $\psi(X)$, so $$\dot z_p-\dot z_q\le\frac{K\psi(X)}N
 \sum_j[(z_j-z_p)-(z_j-z_q)]=-K\psi(X)V.$$ Maximizing over active pairs proves the second Dini inequality; the identical active-pair argument for positions gives the first. Thus $$D^{+}\left(V+K\int_{X(0)}^X\psi(s)\,ds\right)\le0.$$ The radius $R$ supplied by [\[eq:condition\]](#eq:condition){reference-type="eqref" reference="eq:condition"} is a first-crossing barrier. Since $\psi(X)\ge\psi(R)$, Gronwall yields [\[eq:bounds\]](#eq:bounds){reference-type="eqref" reference="eq:bounds"}. Integrability of $V$ makes relative positions Cauchy, and conservation identifies the common velocity. Finally $\psi(s)\sim s^{-2\beta}$, so its tail diverges precisely for $\beta\le1/2$.

\>0

# Explicit radius and sharp two-body boundary

This revision is the **critical-tail and scalar-sharpness owner**. Put $$\Phi_\beta(r)=\int_0^r(1+s^2)^{-\beta}ds
 =r\,{}_2F_1(1/2,\beta;3/2;-r^2).$$ The confinement radius is $R=\Phi_\beta^{-1}(\Phi_\beta(X(0))+V(0)/K)$. In particular, $\Phi_{1/2}=\operatorname{arsinh}$; the logarithmic divergence retains the endpoint $\beta=1/2$ in the unconditional chamber.

[\[prop:sharp\]]{#prop:sharp label="prop:sharp"} Take $N=2$, $d=1$, and orient the initial data so that $r(0)=r_0\ge0$ and $u(0)=u_0\ge0$. Then $$\label{eq:two}
 r'=u,\qquad u'=-K\psi(r)u,\qquad
 u(r)=u_0-K\int_{r_0}^{r}\psi(s)\,ds.$$ For $\beta>1/2$ let $A=K\int_{r_0}^{\infty}\psi$. If $u_0<A$, then $r$ converges to the unique finite zero of [\[eq:two\]](#eq:two){reference-type="eqref" reference="eq:two"} and $u\to0$. If $u_0=A$, then $r\to\infty$ while $u\to0$. If $u_0>A$, then $u\to u_0-A>0$ and $r(t)/t\to u_0-A$.

Subtracting the two equations gives [\[eq:two\]](#eq:two){reference-type="eqref" reference="eq:two"}; while $u>0$, division by $r'=u$ gives $du/dr=-K\psi(r)$. Below threshold its strictly decreasing right side has one finite zero. At equality it stays positive at every finite $r$, so a finite limiting separation is impossible, while the tail tends to zero. Above threshold the positive limiting speed is $u_0-A$, and averaging $r'=u$ proves the last limit. Thus the strict all-particle barrier is sharp on this subfamily, but its failure is not claimed necessary for general flocks.

\>1

# Degenerate faces, evidence, and route boundary

This revision is the **boundary-atlas and scope-firewall owner**. For $N=1$, both diameters vanish. At $K=0$, velocities are constant and flocking occurs exactly when $V(0)=0$. If $V(0)=0$ for any $K\ge0$, relative positions remain fixed. Coincident agents are regular because $\psi(0)=1$. The two-body equality face is not classical flocking: velocity alignment holds but spatial confinement fails.

Exact rational rows audit mean conservation, the ordered-pair factor in [\[eq:energy\]](#eq:energy){reference-type="eqref" reference="eq:energy"}, and active-diameter inequalities. Symbolic rows audit five communication primitives and the $\beta=3/2$ below/equality/above threshold trichotomy. Finite evidence is regression only; the proof owns all $N,d$.

Cucker and Smale introduced this flocking model [@CS]; Ha and Liu developed the explicit Lyapunov-tail proof lineage [@HL]. We claim no priority. Nearby packages own fixed signed-Laplacian consensus, randomized gossip, and noisy Kuramoto synchronization, not this coevolving position--velocity flow.

The source parameters carry no rational-prime semantics, primitive-orbit ledger, dynamical zeta, target analytic bridge, or natural same-clock quantum lift. Route A is therefore rejected as $(A0_{\rm FAIL},A1_{\rm FAIL},A2_{\rm FAIL},A3_{\rm FAIL},A4_{\rm FAIL})$. Route B remains locked under `NO_BAD_EULER_OR_ROOT_NUMBER`; no target zero match or Hilbert--Pólya operator is claimed.

9 F. Cucker and S. Smale, *Emergent behavior in flocks*, IEEE Trans. Automat. Control 52 (2007), 852--862. <https://doi.org/10.1109/TAC.2007.895842>. S.-Y. Ha and J.-G. Liu, *A simple proof of the Cucker--Smale flocking dynamics and mean-field limit*, Commun. Math. Sci. 7 (2009), 297--325. <https://doi.org/10.4310/CMS.2009.v7.n2.a2>.
