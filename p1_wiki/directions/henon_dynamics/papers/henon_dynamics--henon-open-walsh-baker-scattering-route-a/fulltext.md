---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-open-walsh-baker-scattering-route-a"
canonical_tex: "henon_dynamics/henon_open_walsh_baker_scattering_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_open_walsh_baker_scattering_route_a/paper/main.pdf"
source_sha256: "ae61a95a8cbe356dc9343e9d789455ff95d9c4307545d4560c19545cc99ddfdd"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Traces and Escape Ranks for a Three-Symbol Open Walsh Gate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_open_walsh_baker_scattering_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_open_walsh_baker_scattering_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_open_walsh_baker_scattering_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_open_walsh_baker_scattering_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study a finite three-symbol Walsh gate obtained by passing one qutrit per step through a rank-two Fourier--projection contraction. The gate has exact left and right defect projections, a tensor-power identity after one full factor cycle, and an all-period trace formula governed by a greatest common divisor. Newton recursion then gives exact secular polynomials. A tempting one-step rank formula is false: the rank is $2\,3^{k-1}$, while $2^k$ occurs only after $k$ steps. The construction is a finite scattering subgate with a closed unitary parent, not a self-adjoint or target-matched quantization.
author:
- 'Hénon Route-A Working Series, C148'
date: 25 August 2026
title: |
  Exact Traces and Escape Ranks\
  for a Three-Symbol Open Walsh Gate
```

## Markdown 正文

# Frozen open gate

Let $\omega=e^{2\pi i/3}=(-1+i\sqrt3)/2$ and $$(F_3)_{j\ell}=3^{-1/2}\omega^{j\ell},\qquad
 P=\operatorname{diag}(1,0,1),\qquad A=F_3^*P.$$ On $\mathcal H_k=(\mathbb C^3)^{\otimes k}$, with lexicographic qutrit basis, freeze $$B_k(v_0\otimes\cdots\otimes v_{k-1})
 =v_1\otimes\cdots\otimes v_{k-1}\otimes Av_0.       \tag{1}$$ One application is one clock tick, and $D_k(z)=\det(I_{3^k}-zB_k)$. No spectral rescaling is performed.

For every $k,n\ge1$, with $d=\gcd(n,k)$, $$\begin{aligned}
 \|B_k\|&=1,& \operatorname{rank}B_k&=2\,3^{k-1},
 &B_k^k&=A^{\otimes k},& \operatorname{rank}B_k^k&=2^k,             \tag{2}\\
 \operatorname{Tr}(B_k^n)&=\operatorname{Tr}(A^{n/d})^d.                           \tag{3}\end{aligned}$$ The subunitarity defects are the rank-$3^{k-1}$ projections $$\begin{aligned}
 I-B_k^*B_k&=(I-P)\otimes I_{3^{k-1}},\tag{4}\\
 I-B_kB_k^*&=I_{3^{k-1}}\otimes F_3^*(I-P)F_3.\tag{5}\end{aligned}$$

Write $S(v_0,\ldots,v_{k-1})=(v_1,\ldots,v_{k-1},v_0)$ and $C=I^{\otimes(k-1)}\otimes A$. Then $B_k=CS$, while $A^*A=P$ and $AA^*=F_3^*PF_3$. This proves the norm, one-step rank, and both Gram formulas. Tracking a pure tensor for $k$ steps sends every factor through $A$ once and restores its position, proving the tensor identity and its rank.

For (3), multiplication of basis matrix elements identifies factor positions along the cycles of addition by $n$ modulo $k$. This permutation has $d$ cycles, indexed by residues modulo $d$. During the $n$ successive shifts, the departing positions are $0,1,\ldots,n-1$ modulo $k$; each residue modulo $d$ occurs exactly $n/d$ times. Thus every permutation cycle contracts exactly $n/d$ ordered copies of $A$, and its free qutrit-index sum is $\operatorname{Tr}(A^{n/d})$. The $d$ cycles are independent, giving the displayed power. This proves every period; no finite replay is used.

The distinction in (2) is substantive. One tick opens only the factor crossing the cut; the full tensor opening occurs only after $k$ ticks.

# Secular and path formulas

The one-qutrit characteristic polynomial is $$\det(\lambda I-A)=\lambda(\lambda^2-\tau\lambda+q),\qquad
 \tau=\frac{\sqrt3}{6}-\frac i2,\quad
 q=-\frac12-\frac{\sqrt3 i}{6}.$$ Put $t_0=2,t_1=\tau$ and $t_m=\tau t_{m-1}-qt_{m-2}$. Thus $t_m=\operatorname{Tr}(A^m)$. If $D_k(z)=\sum_jc_{k,j}z^j$, then $$c_{k,0}=1,\qquad
 c_{k,m}=-\frac1m\sum_{j=1}^m c_{k,m-j}
 t_{j/\gcd(j,k)}^{\gcd(j,k)}.                         \tag{6}$$ This is a reproducible expression in $\mathbb Q(\sqrt3,i)$. In particular, $$\begin{aligned}
 D_1(z)&=1+\left(-\frac{\sqrt3}{6}+\frac i2\right)z
 +\left(-\frac12-\frac{\sqrt3 i}{6}\right)z^2,\\
 D_2(z)&=1+\left(-\frac{\sqrt3}{6}+\frac i2\right)z
 +\left(-\frac{\sqrt3}{6}+\frac i6\right)z^3
 +\left(-\frac16-\frac{\sqrt3 i}{6}\right)z^4.\end{aligned}$$ To prove the endpoint, triangularize $A$. It has one zero and two nonzero eigenvalues, counted algebraically, so $A^{\otimes k}=B_k^k$ has exactly $3^k-2^k$ zero eigenvalues. Spectral mapping preserves that total at zero: zero is the only eigenvalue of $B_k$ whose $k$th power is zero. Hence $$\det(\lambda I-B_k)=\lambda^{3^k-2^k}
 \sum_{j=0}^{2^k}c_{k,j}\lambda^{2^k-j},             \tag{7}$$ and the last coefficient is nonzero. The exact payload lists every coefficient through $k=5$; its compact receipt is

   $k$   $3^k$   $\operatorname{rank}B_k$   $\deg D_k$   nonzero $c_{k,j}$
  ----- ------- -------------------------- ------------ -------------------
    1      3                2                   2                3
    2      9                6                   4                4
    3     27                18                  8                9
    4     81                54                  16              13
    5     243              162                  32              21

In the frozen basis, a directed edge carries its complex matrix entry. Matrix multiplication and primitive-root decomposition give $$\operatorname{Tr}(B_k^n)=\sum_{w\ \mathrm{rooted\ closed}}a(w),\qquad
 D_k(z)=\prod_{[p]\ \mathrm{primitive}}
 (1-a(p)z^{|p|}).                                    \tag{8}$$ All signed and complex cancellations are retained. Since the maximum absolute column sum is $\sqrt3$, the absolute rooted-path mass at time $n$ is at most $3^k(\sqrt3)^n$. Thus the logarithmic majorant converges for $|z|<1/\sqrt3$, where the raw product is absolutely regroupable. The determinant is globally a polynomial; no larger raw product domain is claimed.

# Controls and boundary

For $P=I_3$, $A=F_3^*$ and the corresponding $B_k$ is unitary of rank $3^k$, with vanishing defects. This is the closed parent from which the opening is defined. Projector order is an isospectral negative control: if $A_{\rm R}=PF_3^*$, then $$A_{\rm R}=F_3AF_3^*,\qquad
 \operatorname{Tr}(A_{\rm R}^m)=\operatorname{Tr}(A^m).$$ Formula (3) therefore leaves every $D_k$ unchanged, although matrix entries and the left/right Gram placements change. By contrast, moving the hole to $P_0=\operatorname{diag}(0,1,1)$ preserves opening rank but gives $$\operatorname{Tr}(F_3^*P_0)=-\frac{\sqrt3}{3}-i,\qquad
 [z]D_k^{(P_0)}=\frac{\sqrt3}{3}+i,$$ rather than $[z]D_k=-\sqrt3/6+i/2$. Hole location, but not this projector order, changes the secular data.

Exact replay checks 60 traces and all 67 coefficients for $k=1,\ldots,5$. The $k=2$ prefix through period eight totals 510 rooted paths and 71 primitive cycles; it is not the proof of (2), (3), or (8). A producer-independent checker passes 748 assertions, SymPy passes 141 checks, byte replay passes, and 40 repaired-hash plus one stale-hash mutations are rejected.

The strict Route-A verdict is

`A1_WEAK / A2_FAIL / A3_FAIL /` `A4_UNITARY_OR_SCATTERING_CANDIDATE`,\
overall `ROUTE_A_EXPLORATORY`.

This finite-$k$ subunitary gate is not self-adjoint and has no semiclassical target matching. We claim no target divisor or counting law, prime-like map, arithmetic local data, Euler factor, root number, automorphy, antiunitary symmetry, Hilbert--Pólya operator, or Route-B authorization. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
