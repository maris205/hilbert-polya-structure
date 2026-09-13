---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-spherical-pendulum-monodromy-route-a"
canonical_tex: "henon_dynamics/henon_spherical_pendulum_monodromy_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_spherical_pendulum_monodromy_route_a/paper/main.pdf"
source_sha256: "2b23b3d54e90a1680d7e0db544137713d075416a5651375b165c5f06247fe1c9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Spherical Pendulum: Cubic Chambers and Focus--Focus Monodromy

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_spherical_pendulum_monodromy_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_spherical_pendulum_monodromy_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_spherical_pendulum_monodromy_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_spherical_pendulum_monodromy_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a coordinate-safe analytic atlas for the unit spherical pendulum. Energy--momentum reduction produces an exact cubic $P_{h,j}(u)$, whose discriminant and double-root parameterization delimit the critical-value components. Eight representative regular receipt rows carry independently checked period, azimuthal-angle, and action quadratures. The isolated upright value is focus--focus; with an explicitly fixed oriented basis and matrix-column convention its positive-loop monodromy is $\left[\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right]$. No elementary closed form is asserted for every quadrature, and no arithmetic or Hilbert--Pólya claim is made.
author:
- HCS Research Program
date: 30 August 2026(revision 2)
title: 'The Spherical Pendulum: Cubic Chambers and Focus--Focus Monodromy'
```

## Markdown 正文

suppressoptionalinfo 611

# Model and a pole-safe reduction

On $T^*S^2$, in the usual chart away from the poles, let $$H=\frac12\left(p_\theta^2+\frac{j^2}{\sin^2\theta}\right)+\cos\theta,
 \qquad J=j=p_\phi .                                      \label{eq:H}$$ The global embedding variables $r\cdot r=1,\ r\cdot p=0$ are retained at $\theta=0,\pi$, where $\phi$ is not a coordinate. Put $u=\cos\theta$ and write $h=H$. Hamilton's equations give $$\dot u^2=P_{h,j}(u)=2(1-u^2)(h-u)-j^2
 =2u^3-2hu^2-2u+2h-j^2 .                                  \label{eq:cubic}$$ =0 The baseline certificate records ([\[eq:cubic\]](#eq:cubic){reference-type="ref" reference="eq:cubic"}) and the endpoint labels. The focus value is kept separate from the interior critical branch; regular periods are not assigned to a double root.

# Critical-value geometry

The cubic discriminant is $$\operatorname{disc}_uP=
4(16h^4-8h^3j^2-32h^2+72hj^2-27j^4+16).                   \label{eq:disc}$$ For an interior double root $s\in(-1,0)$, solving $P(s)=P'(s)=0$ gives $$h=\frac{3s^2-1}{2s},\qquad j^2=\frac{(1-s^2)^2}{-s}.       \label{eq:crit}$$ The endpoint $u=-1,h=-1,j=0$ is elliptic--elliptic. The upright endpoint $u=1,h=1,j=0$ is an isolated focus--focus value and its fiber is pinched; it is not a point on the $s\in(-1,0)$ interior branch. \>0

[\[prop:roots\]]{#prop:roots label="prop:roots"} For each regular receipt row with $j\ne0$, the three real roots obey $r_1<r_2<1<r_3$, and the physical oscillation interval is $(r_1,r_2)\subset(-1,1)$. The endpoint-cancelled substitution $u(t)=m+d\cos t$, $m=(r_1+r_2)/2$, $d=(r_2-r_1)/2$, removes the square-root endpoint singularities.

# Three exact quadratures

On a regular chamber $P=2(u-r_1)(r_2-u)(r_3-u)$. The period, azimuthal increment and action are $$\begin{aligned}
 T&=2\int_0^\pi\frac{\,\mathrm dt}{\sqrt{2(r_3-u(t))}},&
 \Delta\phi&=2j\int_0^\pi
 \frac{\,\mathrm dt}{(1-u(t)^2)\sqrt{2(r_3-u(t))}},              \label{eq:q1}\\
 I&=\frac1\pi\int_0^\pi
 \frac{d^2\sin^2t\,\sqrt{2(r_3-u(t))}}{1-u(t)^2}\,\,\mathrm dt . \label{eq:q2}\end{aligned}$$ The square-root factor in the numerator of $I$ is essential: it is the Jacobian form of $\pi^{-1}\int_{r_1}^{r_2}\sqrt{P(u)}/(1-u^2)\,\mathrm du$. The producer and an independent SymPy script evaluate both forms at 80--90 digits. The ledger deliberately reports quadratures rather than pretending that all parameters have an elementary closed form.

   case     $(h,j)$      $r_1,r_2,r_3$ (rounded)     $T$      $I$
  ------ -------------- -------------------------- -------- --------
   R01    $(-1/2,1/4)$   $-0.9659,-0.5444,1.0103$   3.3528   0.1267
   R02     $(0,1/10)$    $-0.9975,-0.0050,1.0025$   3.7018   0.4879
   R04    $(1/4,1/10)$   $-0.9980,0.2447,1.0033$    3.9444   0.6398
   R06    $(3/4,1/20)$   $-0.9996,0.7472,1.0025$    4.9260   1.0122

  : Selected exact-rational controls and certified outputs.

=1

# Revision-one evidence

The full receipt (eight representative regular rows and seven critical rows) is accompanied by a producer-independent checker with 308 assertions, a 77-check SymPy cross-check, byte replay, and 34 repaired-hash hostile mutations. The original $u$-integral for $I$ is evaluated independently, so a misplaced square-root factor cannot survive the release gate.

# Liouville fibers and monodromy

Away from the critical-value set, the commuting pair $(H,J)$ has compact Liouville tori. Fix $\alpha$ as the vanishing cycle and $\beta$ as a transported complementary cycle. For a positive counterclockwise loop around the isolated value $(h,j)=(1,0)$, $$\alpha\longmapsto\alpha,\qquad \beta\longmapsto\beta+\alpha .$$ Our matrix convention is that *columns are transported basis vectors expressed in the initial $(\alpha,\beta)$ basis*. Consequently $$M_{(\alpha,\beta)}=
 \begin{pmatrix}1&1\\0&1\end{pmatrix}.                    \label{eq:mono}$$ This convention explains why a row-vector or transposed convention would display a different-looking matrix; no such ambiguity is left in the receipt.

For completeness, a regular torus trajectory closes exactly when $\Delta\phi/(2\pi)=p/q$ in lowest terms. The primitive closure uses $q$ u-oscillations and the $k$-fold repetition uses $kq$; irrational ratios are quasiperiodic. The resonant objects remain clean one-parameter torus families, rather than isolated primitive orbits.

\>1

# Boundaries, verification, and route decision

At $u=\pm1$ the embedding chart is used and no azimuthal value is assigned. At a double root the period is singular, so the row is marked critical rather than regular. The bottom endpoint is elliptic--elliptic; the isolated top endpoint is focus--focus. Symbolic identities, numerical root residuals, and the direct action integral are all independently checked.

The locked scope is `NO_BAD_EULER_OR_ROOT_NUMBER`. No prime/zero table, arithmetic local datum, Euler factor, root number, automorphy claim, target divisor or functional equation, target determinant, or Hilbert--Pólya operator is used. Thus the Route-A tuple is `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL, A4_NATURAL_QUANTIZATION)` and the overall verdict is `ROUTE_A_REJECTED`.

9 R. H. Cushman and J. J. Duistermaat, The quantum mechanical spherical pendulum, *Bull. Amer. Math. Soc.* 19 (1988), DOI [10.1090/S0273-0979-1988-15705-9](https://doi.org/10.1090/S0273-0979-1988-15705-9). H. R. Dullin, Semi-global symplectic invariants of the spherical pendulum, *J. Differential Equations* 254 (2013), DOI [10.1016/j.jde.2013.01.018](https://doi.org/10.1016/j.jde.2013.01.018).
