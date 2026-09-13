---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-rectangular-billiard-orbit-family-route-a"
canonical_tex: "henon_dynamics/henon_rectangular_billiard_orbit_family_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_rectangular_billiard_orbit_family_route_a/paper/main.pdf"
source_sha256: "b3a1a175444f03a1edfa071e43212d3f60a2dc2c9e29b1bd598494c45da402da"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Clean Primitive Families and Length Collisions in the Square Billiard

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_rectangular_billiard_orbit_family_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_rectangular_billiard_orbit_family_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_rectangular_billiard_orbit_family_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_rectangular_billiard_orbit_family_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Unfolding the unit-square billiard gives an exact census of primitive rational directions and their one-parameter periodic families. The cutoff-$40$ ledger contains 979 positive coprime ordered directions. The first length collision not induced by coordinate swap is $1^2+8^2=4^2+7^2=65$, while an irrational- aspect rectangle removes all such collisions. The full reduced Poincaré derivative has a unit eigenvalue tangent to every fixed-family curve, making the ordinary isolated-orbit denominator singular. The natural Dirichlet half-wave is clock matched and time-reversal symmetric but provides no trace bridge or target match.
author:
- 'Route-A structural certificate C147'
title: |
  Clean Primitive Families and Length Collisions\
  in the Square Billiard
```

## Markdown 正文

# Primitive unfolding

Reflect the unit square across its sides. A regular billiard trajectory becomes a straight line on the doubled square torus. A positive ordered pair $(m,n)$ is an absolute-direction representative. It owns four signed unfolded sectors $(\pm2m,\pm2n)$, paired into two by time reversal; coordinate swap is retained rather than quotiented. Return of position and oriented velocity for the displayed representative requires displacement $(2m,2n)$, so $$L_{m,n}=2\sqrt{m^2+n^2}.                         \tag{1}$$ This return is primitive exactly when $\gcd(m,n)=1$: a common divisor produces a shorter even translation, while any shorter oriented return produces a common divisor. Vertex-hitting offsets are excluded.

The line crosses $2m$ vertical and $2n$ horizontal sides. Thus its Dirichlet reflection phase is $(-1)^{2(m+n)}=+1$. The horizontal and vertical axes are the two time-reversal-quotiented boundary classes and are treated separately from the positive ledger.

# Periodic cylinders and stability obstruction

For a fixed primitive direction, offsets transverse to the straight flow form a circle. Removing the finitely many offsets that hit unfolded vertices decomposes it into open cylinders of positive transverse length. The fixed direction itself has zero angular measure, so these cylinders have zero Liouville measure in the full energy shell. The primitive return preserves the offset. Let $P_{m,n}$ be the full reduced Poincaré return on a smooth local section. Its fixed-family intersection is a curve; differentiating the fixed-curve identity gives a tangent unit multiplier. More explicitly, put $e=w/L$ along the primitive unfolded vector, use $s$ along $e_\perp$, and let $\theta$ be angular deviation from $e$. The first-return time is $L/\cos\theta$, hence $$P_{m,n}(s,\theta)=(s+L\tan\theta,\theta),\qquad
DP_{m,n}(s,0)=\begin{pmatrix}1&L\\0&1\end{pmatrix}.$$ Since $L>0$, $\ker(I-DP_{m,n})=\operatorname{span}(\partial_s)$, exactly the fixed-family tangent. Therefore $$\det(I-DP_{m,n})=0.                              \tag{2}$$ Consequently these are clean families rather than isolated periodic orbits, and the ordinary isolated-orbit determinant convention is unavailable. One label $(m,n)$ refers to the union of its regular open cylinders, not to a claim that the singular offsets leave exactly one connected component.

# Exact census and length collisions

Möbius inversion gives the number of ordered positive coprime pairs in the $M\times M$ box: $$C(M)=\sum_{d=1}^{M}\mu(d)\left\lfloor\frac Md\right\rfloor^2. \tag{3}$$ At $M=40$, this is $C(40)=979$. These representatives own 3,916 signed oriented sectors, or 1,958 after pairing by time reversal.

The ordered ledger retains coordinate swaps because they are distinct directions, while the nontrivial-collision test quotients that square symmetry. Exact exhaustion finds the first two inequivalent primitive representations at $$65=1^2+8^2=4^2+7^2,                              \tag{4}$$ giving the common length $2\sqrt{65}$. Every smaller square has at most one primitive representative after sorting the coordinates. Indeed, a positive coordinate in a representation below 65 is at most eight, so cutoff 40 contains every unrestricted candidate needed for this global minimality claim.

As a geometric control, take a rectangle of width one and height $\alpha=2^{1/4}$. Squared lengths divided by four are $m^2+\sqrt2n^2$. If two such values agree, rational independence of $1,\sqrt2$ forces equality of both integer squares and hence of the positive ordered pairs. The irrational aspect removes every distinct-direction collision, not only those below the ledger cutoff.

# Quantization, validation, and boundary

Let $-\Delta_D$ be the Dirichlet Laplacian with domain $H^2(Q)\cap H_0^1(Q)$. Its positive square root $H_D=\sqrt{-\Delta_D}$ has domain $H_0^1(Q)$ and generates the unitary half-wave group $U(t)=e^{-itH_D}$ on $L^2(Q)$. The principal symbol $|p|$ gives the same unit-speed length clock on $|p|=1$. Complex conjugation $K$ is antiunitary, $K^2=I$, and $KU(t)K=U(-t)$. Dirichlet phase $-1$ per bounce agrees with the $+1$ phase over $2(m+n)$ reflections. This natural integrable quantization neither supplies a clean-family trace bridge nor any target comparison.

The independent checker passes 1,082 assertions, SymPy passes 88 checks, byte replay passes, and all 36 hostile receipts (35 repaired-hash and one stale- hash) are rejected. The strict tuple is $$\begin{aligned}
(&\texttt{A1\_WEAK},\texttt{A2\_FAIL},\\[-2pt]
 &\texttt{A3\_FAIL},\texttt{A4\_NATURAL\_QUANTIZATION}),
\end{aligned}$$ overall `ROUTE_A_EXPLORATORY`. We claim no isolated primitive-orbit determinant, target divisor, functional equation or counting law, prime-like map, arithmetic/local factor, Euler factor, root number, automorphy, Hilbert--Pólya construction, or Route-B authorization. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.
