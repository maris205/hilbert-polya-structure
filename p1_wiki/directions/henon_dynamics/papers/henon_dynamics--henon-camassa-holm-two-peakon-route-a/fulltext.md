---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-camassa-holm-two-peakon-route-a"
canonical_tex: "henon_dynamics/henon_camassa_holm_two_peakon_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_camassa_holm_two_peakon_route_a/paper/main.pdf"
source_sha256: "e2a850081ccbcd6904ecb92b99dff4f767bd1f5b5579a111fb25371ac2510971"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Complete Signed Two-Peakon Scattering and Collision Atlas for the Camassa--Holm Equation

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_camassa_holm_two_peakon_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_camassa_holm_two_peakon_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_camassa_holm_two_peakon_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_camassa_holm_two_peakon_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  On the ordered two-peakon manifold of the Camassa--Holm equation, momentum and energy reduce the four-dimensional flow to one separable quadratic for the exponential gap. \>0 The two root orders give explicit global same-sign scattering and a finite peakon--antipeakon collision with a quadratic gap and reciprocal amplitude blow-up. \>1 We close all singular faces and an explicitly defined $\alpha$-dissipative energy ledger, while separating this finite-dimensional theorem from any claim of uniqueness for arbitrary weak PDE data or target spectral meaning.
author:
- 'Route-A source-local certificate HCS-C278'
date: 1 September 2026
title: |
  A Complete Signed Two-Peakon Scattering and Collision Atlas\
  for the Camassa--Holm Equation
```

## Markdown 正文

trailerid \[\<C2782026090100000000000000000000\>\<C2782026090100000000000000000000\>\]

# Frozen equation and reduction

We use the momentum form $$m_t+u m_x+2u_xm=0,\qquad m=u-u_{xx},$$ and the ordered ansatz $$u(x,t)=\sum_{j=1}^2p_j(t)e^{-|x-q_j(t)|},\qquad q_1<q_2.$$ This is the normalization introduced with peaked solutions in Camassa and Holm [@CH1993]. Since $(1-\partial_x^2)e^{-|x-q|}=2\delta_q$, matching the $\delta'_q$ and $\delta_q$ coefficients in (1) gives $$\dot q_i=\sum_jp_je^{-|q_i-q_j|},\qquad
 \dot p_i=p_i\sum_jp_j\operatorname{sgn}(q_i-q_j)e^{-|q_i-q_j|}.$$

Put $q=q_2-q_1$, $y=e^q$, $p=p_2-p_1$, and $$P=p_1+p_2,\qquad
 E=p_1^2+p_2^2+2p_1p_2e^{-q},\qquad D^2=2E-P^2.$$

[\[lem:red\]]{#lem:red label="lem:red"} Before collision, $P$ and $E$ are constant and $$\dot y=p(y-1),\qquad \dot p=\frac{P^2-p^2}{2y},\qquad
 \dot y^2=D^2(y-1)\left(y-\frac{P^2}{D^2}\right).$$

In the ordered chart, (3) says $\dot p_1=-p_1p_2e^{-q}$ and $\dot p_2=p_1p_2e^{-q}$. Direct differentiation proves $\dot P=\dot E=0$. Substitution of $p_1=(P-p)/2$, $p_2=(P+p)/2$ into (4) gives $$2E=P^2+p^2+\frac{P^2-p^2}{y},$$ or $p^2(y-1)=D^2y-P^2$. Combining this with $\dot y=p(y-1)$ gives the last identity in (5); differentiating the algebraic identity gives the middle one.

[\[thm:main\]]{#thm:main label="thm:main"} For $q>0$, $$P^2-D^2=4p_1p_2(1-e^{-q}).$$ \>0 Consequently, every ordered solution with $p_1p_2\ne0$ belongs to exactly one of the following strict chambers. The equality face $p_1p_2=0$ is the degenerate single-peak boundary (including the zero field), not a third strict two-body chamber. At this revision stage we resolve the strict same-sign sector $p_1p_2>0$, equivalently $P^2>D^2$.

*Same sign:* if $P^2>D^2$, there is a unique time shift $t_*$ such that $$y=1+\left(\frac{P^2}{D^2}-1\right)
       \cosh^2\!\frac{D(t-t_*)}{2},\qquad
 p=D\tanh\!\frac{D(t-t_*)}{2}.$$ The solution is global and the gap remains positive.

\>0 *Opposite sign:* if $D^2>P^2$, an incoming branch has a finite collision time $t_c$ and $$y=1+\left(1-\frac{P^2}{D^2}\right)
       \sinh^2\!\frac{D(t_c-t)}{2},\qquad
 p=-D\coth\!\frac{D(t_c-t)}{2}.$$ As $t\uparrow t_c$, $$q=\frac{D^2-P^2}{4}(t_c-t)^2+O((t_c-t)^4),\qquad
 p=-\frac{2}{t_c-t}+O(t_c-t).$$

The second root of the quadratic in (5) is $P^2/D^2$. When it exceeds one, separation with the minimum at $t_*$ gives (6). \>0 When it lies below one, separation from $y=1$ gives (7). Differentiation verifies both branches. The expansions $\sinh z=z+O(z^3)$ and $\coth z=z^{-1}+O(z)$ prove (8). Differentiation verifies this branch.

\>0

# Scattering, collision, and the profile limit

For the same-sign branch, one may choose the additive centre constant so that $$q_1+q_2=Pt+2\operatorname{sgn}(P)\operatorname{artanh}
 \left(\frac{D}{|P|}\tanh\frac{D(t-t_*)}{2}\right).$$ Thus the asymptotic momenta are $(P-D)/2$ and $(P+D)/2$, and the labeled amplitudes exchange these values. This is scattering, not a periodic-orbit family.

In the signed chamber, put $c=(q_1+q_2)/2$ and $h=q/2$. Then $$\dot c=\frac{P}{2}(1+e^{-q}),$$ so finite collision time implies $c\to q_c$. For $K_a(x)=e^{-|x-a|}$, the kernel is uniformly one-Lipschitz in its centre and $$u=\frac P2(K_{c-h}+K_{c+h})
   +\frac p2(K_{c+h}-K_{c-h}),\qquad
 \lVert u-PK_c\rVert_\infty\le (|P|+|p|)h.$$ By (8), $h=O((t_c-t)^2)$ and $p=O((t_c-t)^{-1})$; hence the last bound tends to zero. Together with $c\to q_c$, this proves uniform convergence to $P e^{-|x-q_c|}$. The limiting ordinary single-peak energy is $P^2$, whereas the pre-collision invariant is $$E=\frac{P^2+D^2}{2};$$ the excess $(D^2-P^2)/2$ is the concentrated collision-energy ledger. Explicit non-symmetric dissipative peakon--antipeakon continuations are studied by Grunert and Holden [@GH2016]; we next state precisely the continuation used here.

\>1

# Declared $\alpha$ extension and boundary faces

For $0\le\alpha\le1$, conserve $P$ at collision and define $$E_+=(1-\alpha)E_-+\alpha P^2,\qquad
 D_+^2=(1-\alpha)D_-^2+\alpha P^2.$$ At $\alpha=0$, the outgoing signed branch is the conservative time reflection. At $\alpha=1$, all concentrated energy is removed and only the sticky single peak remains. For $0<\alpha<1$, $D_+^2>P^2$ and (7), with outgoing sign, restarts the signed branch. Equation (10) is a declared rule on the extended two-body state; it is not a uniqueness theorem for arbitrary weak solutions.

If one amplitude is zero, the physical field is the single traveling peak $u=p e^{-|x-q_0-pt|}$. The face $P=0<E$ remains a signed collision chamber, and $P=E=0$ is the zero field. A coincident pair $q=0$ is outside the ordered chart and appears only as the extended collision state.

# Executable receipt and Route-A boundary

The retained evidence contains 15 same-sign rows, 12 collision rows, 15 $\alpha$ ledgers, and four boundary records. A producer-independent checker reconstructs them with 551 assertions; SymPy verifies ten conservation, branch, and asymptotic identities; fresh replay is byte identical; and 41/41 repaired-hash attacks are rejected. Computation audits the convention but does not substitute for Lemma [\[lem:red\]](#lem:red){reference-type="ref" reference="lem:red"} or Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

The source has continuous amplitudes and scattering/collision rather than a rational-prime primitive clock. No target determinant, divisor, functional equation, zero match, or Hilbert--Pólya operator is constructed. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is $$\texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FORMAL\_HINT)},$$ the verdict is `ROUTE_A_REJECTED`, and Route B is disabled.

9 R. Camassa and D. D. Holm, *An integrable shallow water equation with peaked solitons*, Physical Review Letters **71**(11) (1993), 1661--1664, [doi:10.1103/PhysRevLett.71.1661](https://doi.org/10.1103/PhysRevLett.71.1661).

K. Grunert and H. Holden, *The general peakon-antipeakon solution for the Camassa--Holm equation*, Journal of Hyperbolic Differential Equations **13** (2016), 353--380, [doi:10.1142/S0219891616500119](https://doi.org/10.1142/S0219891616500119).
