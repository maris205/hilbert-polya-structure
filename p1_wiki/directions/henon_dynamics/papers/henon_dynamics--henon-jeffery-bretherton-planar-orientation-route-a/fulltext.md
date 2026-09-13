---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-jeffery-bretherton-planar-orientation-route-a"
canonical_tex: "henon_dynamics/henon_jeffery_bretherton_planar_orientation_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_jeffery_bretherton_planar_orientation_route_a/paper/main.pdf"
source_sha256: "92620d7ebdd2f7cd4dd2538704301e2a1c26921e09406833ce5087f1c1a2ac49"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Complete Projective Atlas for Spheroidal Jeffery Directors in Planar Linear Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_jeffery_bretherton_planar_orientation_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_jeffery_bretherton_planar_orientation_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_jeffery_bretherton_planar_orientation_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_jeffery_bretherton_planar_orientation_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We classify a passive axisymmetric spheroid in every steady incompressible planar linear flow. The nonlinear head--tail director equation on $\mathbb{RP}^2$ is the projectivization of one traceless matrix exponential. A scalar discriminant then yields the complete elliptic, hyperbolic, nilpotent, and identity atlas. \>0 We prove the full source--saddle--sink stratification, the nilpotent fixed projective line, and the true head--tail versus oriented simple-shear periods. \>1 Every stroboscopic fixed set and every sphere, rod, disk, and zero-flow boundary is included. The result is source-local: clean periodic continua supply no arithmetic primitive-orbit owner or target determinant.
author:
- HCS Research Program
date: 1 September 2026
title: A Complete Projective Atlas for Spheroidal Jeffery Directors in Planar Linear Flow
```

## Markdown 正文

# Frozen director and its linear lift

Let $$L=\begin{pmatrix}a&b&0\\c&-a&0\\0&0&0\end{pmatrix},\qquad
 E=\tfrac12(L+L^{T}),\quad W=\tfrac12(L-L^{T}).$$ For a spheroid of finite aspect ratio $r>0$, put $$\lambda=\frac{r^2-1}{r^2+1}\in(-1,1). \tag{1}$$ The head--tail director is $[p]\in\mathbb{RP}^2$. A unit representative obeys $$\dot p=Wp+\lambda\{Ep-(p^TEp)p\}. \tag{2}$$ For $r\ne1$, $[p]$ is the intrinsic symmetry-axis director. An unmarked sphere ($r=1$) has no intrinsic shape director; whenever $r=1$ appears below, $[p]$ denotes a marked material director carried by the sphere. Jeffery [@Jeffery1922] is cited only for the isolated-ellipsoid source equation, and Bretherton [@Bretherton1962] only for rigid-particle and spheroidal-parameter lineage. No classification or proof below is outsourced.

Set $B=W+\lambda E$. Because $p^TWp=0$, (2) is $\dot p=Bp-(p^TBp)p$.

For every nonzero $q_0\in\mathbb R^3$, $$=[e^{tB}q_0],\qquad
 p(t)=\frac{e^{tB}q_0}{\lVert e^{tB}q_0\rVert}. \tag{3}$$ Conversely every solution of (2) has this form, so the flow is global on $\mathbb{RP}^2$.

If $q'=Bq$ and $p=q/\lVert q\rVert$, differentiation gives $p'=Bp-(p^TBp)p$. Conversely, multiplying a unit solution by $\exp\int_0^t p^TBp\,ds$ gives a solution of $q'=Bq$. Matrix exponentials are invertible, so normalization never vanishes. Passing to $[p]$ removes the representative sign exactly.

Write $k=(b-c)/2$ and $s=(b+c)/2$. The active block and its invariant are $$B_2=\begin{pmatrix}\lambda a&k+\lambda s\\-k+\lambda s&-\lambda a\end{pmatrix},
 \qquad
 \delta=\lambda^2(a^2+s^2)-k^2. \tag{4}$$ Direct multiplication gives $B_2^2=\delta I$ and $\delta=-\det B_2$.

# The complete sign atlas

The sign and rank in (4) give exactly four cases.

1.  If $\delta<0$ and $\omega=\sqrt{-\delta}$, the vertical director is the only fixed point. Every equatorial director has least period $\pi/\omega$; every director with nonzero horizontal and vertical parts has least period $2\pi/\omega$.

2.  If $\delta>0$ and $\rho=\sqrt\delta$, there are exactly three fixed eigen-directors $[v_+]$, $[e_0]$, $[v_-]$ with exponents $\rho,0,-\rho$. Writing $q=q_+v_++q_0e_0+q_-v_-$, its forward limit is $[v_+]$ if $q_+\ne0$, $[e_0]$ if $q_+=0,q_0\ne0$, and $[v_-]$ otherwise; backward time reverses $+$ and $-$. Thus they are sink, saddle, and source. Precisely, $$W^s([e_0])=\mathbb P\operatorname{span}(e_0,v_-)\setminus\{[v_-]\},\qquad
     W^u([e_0])=\mathbb P\operatorname{span}(e_0,v_+)\setminus\{[v_+]\}.$$ Their closures are the two invariant $\mathbb{RP}^1$ projective lines. \>0

3.  If $\delta=0$ but $B_2\ne0$, the fixed set is the entire projective line $\mathbb P(\ker B)$. Every other trajectory converges as $t\to\pm\infty$ to the unique horizontal line $\mathbb P(\operatorname{im}B_2)
    =\mathbb P(\ker B_2)$, at algebraic rate $|t|^{-1}$.

4.  If $B_2=0$, the flow is the identity on all of $\mathbb{RP}^2$.

Cayley--Hamilton gives, respectively, $$e^{tB_2}=\cos(\omega t)I+\frac{\sin(\omega t)}{\omega}B_2,\qquad
 e^{tB_2}=\cosh(\rho t)I+\frac{\sinh(\rho t)}{\rho}B_2. \tag{5}$$ In the first case there is no real horizontal eigenline. At $\pi/\omega$ the horizontal block is $-I$, which returns every equatorial head--tail line but not a mixed line; at $2\pi/\omega$ the full matrix is $I$. No earlier return is possible because a non-scalar elliptic block has no real eigenline.

In the second case, exponentiating the three eigen-coordinates gives the stated limits. Within $\mathbb P\operatorname{span}(e_0,v_-)$, every point except $[v_-]$ tends forward to $[e_0]$; within $\mathbb P\operatorname{span}(e_0,v_+)$, every point except $[v_+]$ tends backward to $[e_0]$. These are projective lines, and a point outside them has both corresponding leading coordinates, proving the stable/unstable completeness. Coordinate ratios give gaps $\rho$ or $2\rho$. \>0 At $\delta=0$, $e^{tB}=I+tB$. A nonzero nilpotent $2$ by $2$ block has rank one and image equal to kernel. Hence $\mathbb P(\ker B)$ is fixed, whereas $[q+tBq]\to[Bq]$ off that line. Finally $B_2=0$ and the zero vertical block give $B=0$.

\>0

# Simple shear and singular shape faces

For $L_2=\left(\begin{smallmatrix}0&\dot\gamma\\0&0\end{smallmatrix}\right)$ with $\dot\gamma\ne0$, substitution of (1) in (4) yields $$\delta=-\frac{\dot\gamma^2r^2}{(r^2+1)^2},\qquad
 \omega=\frac{|\dot\gamma|r}{r^2+1}. \tag{6}$$ Thus the physical head--tail equatorial period and the oriented-vector period are $$T_{\mathbb{RP}^1}=\frac{\pi(r+r^{-1})}{|\dot\gamma|},\qquad
 T_{\rm oriented}=\frac{2\pi(r+r^{-1})}{|\dot\gamma|}. \tag{7}$$ The second value is the least period of every nonvertical oriented vector and also of a mixed $\mathbb{RP}^2$ director; the vertical oriented vector is fixed. This factor two is a state-space fact, not a convention change.

At $r=1$, $\lambda=0$ and strain drops out: under the marked-material-director convention above, the marked direction follows only vorticity. The unmarked sphere itself has no observable orientation state. As $r\to\infty$ or $r\to0$, $\lambda\to\pm1$, the simple-shear generator is nilpotent and (7) diverges. These rod/disk limits are not finite-aspect periodic points. At $\dot\gamma=0$, every director is fixed.

\>1

# Every elliptic strobe

The first formula in (5) also resolves the return map without sampling.

For $\delta<0$ and $\tau>0$, $$\operatorname{Fix}_{\mathbb{RP}^2}(e^{\tau B})=
 \begin{cases}
 \{[e_0]\},&\omega\tau\notin\pi\mathbb Z,\\
 \mathbb{RP}^1_{\rm eq}\cup\{[e_0]\},&\omega\tau\in(2\mathbb Z+1)\pi,\\
 \mathbb{RP}^2,&\omega\tau\in2\pi\mathbb Z.
 \end{cases} \tag{8}$$

Away from integer half-periods the horizontal block has no real eigenline, so only the vertical eigenline fixes. At odd half-period it is $-I$ while the vertical multiplier is $+1$, fixing the two separate eigenspaces but no mixed line. At a full period every multiplier is one.

  Condition             Fixed set             Nonfixed limit           Recurrence
  --------------------- --------------------- ------------------------ -------------------------
  $\delta<0$            vertical              none                     clean periodic continua
  $\delta>0$            three lines           source/saddle/sink       none
  $\delta=0$, $B\ne0$   one $\mathbb{RP}^1$   algebraic kernel limit   none
  $B=0$                 all $\mathbb{RP}^2$   none                     stationary

# Executable receipt and claim boundary

The deterministic certificate contains 625 exact parameter rows, 320 90-digit orbit reconstructions, ten shear-period rows, five strobe rows, and six boundary rows. The producer-independent checker passes 8,328 assertions; the symbolic reconstruction passes 39 identities; replay is byte-exact; and 25/25 repaired-hash or stale-hash hostile mutations are rejected. These rows are regression oracles, not a finite proof of the arbitrary-parameter theorem.

\>1

  Release item                                                                Result
  ---------------------------------------------------- -----------------------------
  Parameter / orbit / shear / strobe / boundary rows                $625/320/10/5/6$
  Independent assertions / symbolic identities                     $8{,}328/39$ PASS
  Fresh byte replay / hostile mutations                      PASS / $25/25$ rejected
  Evidence SHA-256                                       `858a50dcdfc8…847efa308374`

The nearest projective, spin, and linear-Hamiltonian owners do not contain this passive $\mathbb{RP}^2$ shape/gradient discriminant. This workspace distinction is not a literature-priority claim.

The honest Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}),
 \qquad \mathrm{ROUTE\_A\_REJECTED}. \tag{9}$$ There is no rational-prime carrier or logarithmic clock. Elliptic periodic points occur in clean continua with continuously variable periods; the other chambers align or are stationary. Consequently no isolated primitive-orbit product, target determinant, target zero match, Hilbert--Pólya operator, or Route-B input follows. The locked scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

9 G. B. Jeffery, "The motion of ellipsoidal particles immersed in a viscous fluid," *Proc. R. Soc. Lond. A* **102** (715), 161--179 (1922), [doi:10.1098/rspa.1922.0078](https://doi.org/10.1098/rspa.1922.0078).

F. P. Bretherton, "The motion of rigid particles in a shear flow at low Reynolds number," *J. Fluid Mech.* **14** (2), 284--304 (1962), [doi:10.1017/S002211206200124X](https://doi.org/10.1017/S002211206200124X).
