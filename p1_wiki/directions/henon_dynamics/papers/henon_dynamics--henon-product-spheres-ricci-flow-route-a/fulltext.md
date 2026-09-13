---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-product-spheres-ricci-flow-route-a"
canonical_tex: "henon_dynamics/henon_product_spheres_ricci_flow_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_product_spheres_ricci_flow_route_a/paper/main.pdf"
source_sha256: "a5a5c8472bee49fd59790cdd01a85dba6dbe8e1219224270cca859d9f95ffc7a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Singularities of Homogeneous Ricci Flow on Products of Round Spheres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_product_spheres_ricci_flow_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_product_spheres_ricci_flow_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_product_spheres_ricci_flow_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_product_spheres_ricci_flow_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For arbitrary $m\geq1$, dimensions $d_i\geq1$, and scales $a_i>0$, we solve the unnormalized Ricci flow of the product metric $\bigoplus_i a_i g_{S^{d_i}}$ exactly. Every tied first-collapse factor is retained, yielding sharp scalar-curvature, full-curvature, volume, diameter, and Type-I blowup laws. \>0We derive the constant-volume conjugacy and prove that partial collapse has finite normalized lifetime, whereas full collapse is exactly the curved Einstein face and becomes a stationary forward-eternal normalized solution. \>1 The sharp normalized-time asymptotics, pointed product-shrinker limit, flat-circle and all-torus faces, executable reconstruction, collision audit, and strict Route-A obstruction are closed. This is a nonlinear metric-evolution theorem, not a heat-trace, spectral-zeta, or determinant construction.
author:
- |
  Route-A source-local certificate HCS-C281\
  Revision round 2
date: 1 September 2026
title: |
  Exact Singularities of Homogeneous Ricci Flow\
  on Products of Round Spheres
```

## Markdown 正文

suppressoptionalinfo 767 trailerid \[\<C2812026090100000000000000000000\>\<C2812026090100000000000000000000\>\]

# Frozen geometric owner

Let $$M=\prod_{i=1}^{m}S^{d_i},\qquad d_i\in\mathbb Z_{\geq1},
 \qquad g(0)=\bigoplus_{i=1}^{m}a_i g_i,\quad a_i>0,       \tag{1}$$ where $g_i$ is the unit round metric. Put $c_i=d_i-1$ and $n=\sum_i d_i$. We use the unnormalized equation $$\partial_tg=-2\operatorname{Ric}(g)                                    \tag{2}$$ with its physical clock. Hamilton's original program fixes (2) as a geometric evolution equation [@Hamilton1982]; Chow--Knopf provide standard special-geometry, scaling, and singularity conventions [@ChowKnopf2004]. Those sources are cited only for equation lineage and vocabulary. All product, endpoint, and normalization claims below are derived here.

For $d_i\geq2$ define $T_i=a_i/(2c_i)$; for $d_i=1$ define $T_i=\infty$. This convention is essential: a circle is Ricci-flat, not a factor with an undefined clock.

[\[thm:flow\]]{#thm:flow label="thm:flow"} The solution of (2) is $$g(t)=\bigoplus_i a_i(t)g_i,\qquad a_i(t)=a_i-2c_it.       \tag{3}$$ If some $c_i>0$, its maximal Riemannian interval is $(-\infty,T)$, where $T=\min_iT_i$. If every $d_i=1$, (3) is stationary for all $t\in\mathbb R$.

As a $(0,2)$ tensor, the Ricci tensor is unchanged by constant metric rescaling. The unit round factor satisfies $\operatorname{Ric}(g_i)=c_i g_i$, and the Ricci tensor of a Riemannian product is the direct sum of factor tensors. Hence (2) is exactly $a_i'=-2c_i$, proving (3). The coefficients remain positive precisely on the stated interval. The displayed solution solves the full equation; compact Ricci-flow uniqueness identifies it with the ambient solution while it exists.

# Closed geometric observables

Mixed sectional curvatures vanish, while the $i$th factor has sectional curvature $a_i(t)^{-1}$. Consequently $$\begin{aligned}
 R(t)&=\sum_i\frac{d_ic_i}{a_i(t)},
 &|\operatorname{Ric}|^2(t)&=\sum_i\frac{d_ic_i^2}{a_i(t)^2},             \tag{4}\\
 |\operatorname{Rm}|^2(t)&=\sum_i\frac{2d_ic_i}{a_i(t)^2},
 &\frac{V(t)}{V(0)}&=\prod_i\left(\frac{a_i(t)}{a_i}\right)^{d_i/2}.
                                                                    \tag{5}\end{aligned}$$ Here $V(t)=\operatorname{Vol}(M,g(t))$. Differentiation gives $$\frac{d}{dt}\log V(t)=-R(t).                              \tag{6}$$ The product distance also gives the exact diameter $$\operatorname{diam}(M,g(t))=\pi\sqrt{\sum_i a_i(t)}.                    \tag{7}$$

The initial product is Einstein with positive constant $\lambda$ exactly when every factor is curved and $c_i/a_i=\lambda$ for every $i$. Equivalently, all finite clocks coincide at $T=(2\lambda)^{-1}$, and then $$g(t)=(1-t/T)g(0).                                         \tag{8}$$ If all factors are circles, the product is instead Ricci-flat for arbitrary scales. A mixture of flat and curved factors cannot be Einstein.

\>0

# Tied collapse and the full Type-I model

Assume $T<\infty$ and freeze the complete first-collapse set $$I=\{i:T_i=T\},\qquad D=\sum_{i\in I}d_i.                 \tag{9}$$ No generic perturbation is used to split a tie. For $i\in I$, $a_i(t)=2c_i(T-t)$; for $j\notin I$, $a_j(T)>0$.

[\[thm:sing\]]{#thm:sing label="thm:sing"} As $t\uparrow T$, $$\begin{aligned}
 (T-t)R(t)&\longrightarrow \frac D2,                       \tag{10}\\
 (T-t)^2|\operatorname{Ric}|^2(t)&\longrightarrow \frac D4,              \tag{10a}\\
 (T-t)^2|\operatorname{Rm}|^2(t)&\longrightarrow
       \sum_{i\in I}\frac{d_i}{2c_i},                    \tag{11}\\
 V(t)&\sim C_I(T-t)^{D/2},                                 \tag{12}\end{aligned}$$ where $$C_I=\prod_i\operatorname{Vol}(S^{d_i},g_i)
     \prod_{i\in I}(2c_i)^{d_i/2}
     \prod_{j\notin I}a_j(T)^{d_j/2}.$$ The singularity is Type I and $$\operatorname{diam}(M,g(t))\longrightarrow
 \pi\sqrt{\sum_{j\notin I}a_j(T)}.                       \tag{13}$$ For any $t_k\uparrow T$, let $Q_k=(T-t_k)^{-1}$ and $g_k(s)=Q_kg(T+s/Q_k)$ for $s<0$. At product basepoints, $$(M,g_k(s))\longrightarrow
 \prod_{i\in I}\bigl(S^{d_i},-2c_isg_i\bigr)
 \times(\mathbb R^{n-D},g_{\rm E})                              \tag{14}$$ smoothly on compact pointed sets.

Substitution of $a_i(t)=2c_i(T-t)$ into (4)--(5) proves (10), (10a)--(12); every noncollapsing summand stays bounded. Formula (11) gives both the Type-I upper bound and a nonzero Type-I residue, while (7) gives (13). In the rescaled flow, a collapsing coefficient is exactly $-2c_is$. A survivor has coefficient $Q_ka_j(T)-2c_js$, which diverges. A round factor with scale tending to infinity converges pointed smoothly to its Euclidean tangent space. Taking products proves (14).

# Constant-volume conjugacy and endpoint theorem

Define $$C(t)=\left(\frac{V(0)}{V(t)}\right)^{2/n},\qquad
 \tau(t)=\int_0^t C(s)\,ds,\qquad
 \widehat g(\tau(t))=C(t)g(t).                            \tag{15}$$

[\[thm:norm\]]{#thm:norm label="thm:norm"} The metric $\widehat g$ has volume $V(0)$ and satisfies $$\partial_\tau\widehat g=-2\operatorname{Ric}(\widehat g)
       +\frac2n\widehat R\,\widehat g.                   \tag{16}$$ It is ancient in normalized time. At the forward endpoint:

1.  If $D=n$, then every factor is curved, (1) is Einstein, (8) holds, $C(t)=(1-t/T)^{-1}$, and $\tau=-T\log(1-t/T)$. Thus $\widehat g\equiv g(0)$ and the normalized lifetime is infinite.

2.  If $D<n$, then $\tau_T=\lim_{t\uparrow T}\tau(t)<\infty$. Every normalized collapsing scale tends to zero, every survivor scale tends to infinity, and normalized curvature blows up.

All-flat products form the separate stationary eternal case $C=1$, $\tau=t$.

Equation (15) makes $C^{n/2}V=V(0)$. From (6), $C'/C=2R/n$. Constant rescaling leaves $\operatorname{Ric}$ fixed as a $(0,2)$ tensor and gives $\widehat R=R/C$. Dividing $d(Cg)/dt$ by $d\tau/dt=C$ yields (16).

At backward infinity, if $D_c$ is the total dimension of all curved factors, then $C(t)$ is comparable to $|t|^{-D_c/n}$. Its integral diverges for $D_c<n$, and diverges logarithmically for $D_c=n$; hence normalized time tends to $-\infty$. At $T$, (12) gives $C(t)\asymp(T-t)^{-D/n}$. This is integrable exactly when $D<n$. If $D=n$, all clocks coincide and the Einstein calculation gives the explicit stationary normalization. If $D<n$, multiplication of collapsed affine scales and surviving positive scales by $C(t)$ proves the asserted limits.

\>1

# Sharp normalized-time asymptotics

The preceding proof contains exact leading information. Put $\beta=D/n<1$. There is $C_*>0$ such that, as $t\uparrow T$, $$\begin{aligned}
 C(t)&\sim C_*(T-t)^{-\beta},                              \tag{17}\\
 \tau_T-\tau(t)&\sim\frac{C_*}{1-\beta}
                  (T-t)^{1-\beta}.                        \tag{18}\end{aligned}$$ Thus, for $i\in I$, $$\widehat a_i(\tau)\sim
 2c_i(1-\beta)(\tau_T-\tau),                              \tag{19}$$ while a survivor satisfies $\widehat a_j\asymp(\tau_T-\tau)^{-\beta/(1-\beta)}$. Moreover $$\widehat R(\tau)\sim
 \frac{D}{2(1-\beta)(\tau_T-\tau)}.                       \tag{20}$$ Equations (17)--(20) show that finite normalized lifetime is a genuine curvature singularity, not merely escape of the chosen coordinates.

For nonflat data the following are equivalent: full first collapse; $D=n$; positive Einstein initial metric; homothetic unnormalized shrinking; stationary normalized flow; and infinite forward normalized lifetime. Every other nonflat product has partial collapse and a finite normalized singularity. A flat factor therefore forces the partial branch whenever a curved factor is present.

# Degenerate faces and executable reconstruction

The exact boundary ledger is:

  face                             exact behavior
  -------------------------------- --------------------------------------------------------
  $m=1,d=1$                        stationary circle for all physical and normalized time
  $m=1,d\geq2$                     full round collapse; normalized metric fixed
  all $d_i=1$                      arbitrary stationary flat torus
  mixed flat/curved                flat factors survive; normalized endpoint finite
  tied finite clocks               every minimizer retained in $I$ and in (14)
  common $a_i\mapsto\lambda a_i$   physical clock and $T$ scale by $\lambda$
  factor permutation               identical product geometry and collapse ledger
  $t=0$                            both gauges equal the declared initial metric

Zero scales, zero-dimensional factors, surgery, quotients, nonsymmetric perturbations, and general homogeneous spaces are not claimed.

The executable receipt contains 218 analytic and boundary rows across 14 families. A producer-independent checker performs 2,063 assertions; SymPy checks 20 identities; fresh replay matches all 159,616 bytes; and 52/52 repaired-hash or stale-hash hostile trials are rejected. In particular, all 21 partial-collapse tail integrals are finite independently reconstructed numbers rather than endpoint-cancellation infinities. Finite cells test the formulas but are not presented as proof of the all-parameter theorem.

# Collision and Route-A audit

The exact registry scan through C1--C280 found no Ricci-flow, homogeneous Ricci, or product-sphere evolution owner. The nearest mechanisms remain different: C185 is isospectral double-bracket matrix sorting; C270 is static sub-Riemannian geodesic geometry; C133 is metric-graph unitary scattering; C277 and C283 are linear heat-semigroup owners. In particular, HCS-C281 has no heat trace, spectral zeta, regularized determinant, or Schatten theorem.

Outside the flat face, (6) is strictly negative, so there is no nonconstant recurrent metric and no intrinsic primitive-periodic-orbit ledger. Factor dimensions and scales provide neither rational-prime carriers nor a logarithmic-prime clock. No dynamical determinant, target analytic divisor, or natural same-clock unitary lift is defined. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is $$\texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FAIL)},$$ overall `ROUTE_A_REJECTED`; Route B is disabled. No Euler factor, root number, target zero, or Hilbert--Pólya operator is claimed.

9 Richard S. Hamilton, *Three-manifolds with positive Ricci curvature*, Journal of Differential Geometry 17 (1982), 255--306, [doi:10.4310/jdg/1214436922](https://doi.org/10.4310/jdg/1214436922). Bennett Chow and Dan Knopf, *The Ricci Flow: An Introduction*, Mathematical Surveys and Monographs 110, American Mathematical Society, 2004, [doi:10.1090/surv/110](https://doi.org/10.1090/surv/110).
