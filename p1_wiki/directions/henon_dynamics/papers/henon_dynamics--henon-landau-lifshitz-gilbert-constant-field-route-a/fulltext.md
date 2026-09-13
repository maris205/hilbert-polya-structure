---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-landau-lifshitz-gilbert-constant-field-route-a"
canonical_tex: "henon_dynamics/henon_landau_lifshitz_gilbert_constant_field_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_landau_lifshitz_gilbert_constant_field_route_a/paper/main.pdf"
source_sha256: "8394852e7c16b8cd877e3ad37fd8bfc5ee2dcc1051005ac30c8aeb77ae923772"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact constant-field Landau--Lifshitz--Gilbert flow on the sphere

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_landau_lifshitz_gilbert_constant_field_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_landau_lifshitz_gilbert_constant_field_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_landau_lifshitz_gilbert_constant_field_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_landau_lifshitz_gilbert_constant_field_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close the complete source-local dynamics of the constant-field Landau--Lifshitz--Gilbert equation on the unit sphere. In the stereographic coordinate $z=(m_1+i m_2)/(1+m_3)$, the nonlinear vector field becomes $\dot z=(-\alpha\omega+i\omega)z$, while $m_3$ is an exact tanh trajectory. The energy law, north/south stability, pure-precession latitude periods, identity face, and every sampled-time fixed set follow in one boundary atlas. The periodic face is a continuum and therefore does not provide an isolated primitive-orbit or arithmetic determinant. Independent exact reconstruction and symbolic checks accompany the paper.
author:
- HCS Research Program
date: 29 August 2026(revision 2)
title: 'Exact constant-field Landau--Lifshitz--Gilbert flow on the sphere'
```

## Markdown 正文

suppressoptionalinfo 611

# Model and exact chart

Let $e_3=(0,0,1)$, $m(t)\in\mathbb S^2$, and $\alpha,\omega\geq0$. We freeze $$\dot m=-\omega m\times e_3-\alpha\omega m\times(m\times e_3).
 \tag{1}$$ This is the normalized Landau--Lifshitz/Gilbert convention: the usual factor $1+\alpha^2$ in the unreduced Gilbert equation has been absorbed into the declared frequency $\omega$ (equivalently, into the time unit). The vector field is tangent to the sphere. On $m_3>-1$ put $z=(m_1+i m_2)/(1+m_3)$. The inverse formulas are $$m_1+i m_2=\frac{2z}{1+|z|^2},\qquad
 m_3=\frac{1-|z|^2}{1+|z|^2}.
 \tag{2}$$

[\[thm:flow\]]{#thm:flow label="thm:flow"} For $-1<m_3(0)<1$, equation (1) has $$z(t)=z(0)e^{(-\alpha\omega+i\omega)t},\qquad
 m_3(t)=\tanh\!\left(\alpha\omega t+\operatorname{artanh}m_3(0)\right).
 \tag{3}$$ The two poles are equilibria. With $E=1-m_3$, $$\dot E=-\alpha\omega(1-m_3^2)\leq0. \tag{4}$$ If $\alpha\omega>0$, the north pole is asymptotically stable and the south pole is unstable. Their transverse eigenvalues have real parts $-\alpha\omega$ and $+\alpha\omega$, respectively, and precession frequency $\omega$.

Writing (1) in components gives $\dot m_1=-\omega m_2-\alpha\omega m_1m_3$, $\dot m_2=\omega m_1-\alpha\omega m_2m_3$, and $\dot m_3=\alpha\omega(m_1^2+m_2^2)$. The complex combination and the unit-sphere identity yield the scalar linear equation and the logistic equation in (3). Substitution in (2) proves reconstruction and (4). Linearizing the complex equation at the two chart ends gives the stated real parts; the pole cases themselves are immediate from (1).

# Periodic and sampled-time faces

[\[prop:faces\]]{#prop:faces label="prop:faces"} If $\alpha=0$ and $\omega>0$, latitude is conserved and every nonpolar point runs on a circle of period $2\pi/\omega$. If $\omega=0$, the flow is the identity for every $\alpha$. For a sampled time $\tau>0$, when $\alpha\omega>0$ the fixed set is exactly the two poles. On the pure precession face it is all of $\mathbb S^2$ iff $\omega\tau\in2\pi\mathbb Z$, and otherwise it is the two poles; the $\omega=0$ and $\tau=0$ faces are identity maps.

Equation (3) preserves $|z|$ exactly when $\alpha=0$, and its phase is t. If $\alpha>0$, the modulus can return to its initial value only at a pole. The listed resonance and identity alternatives then follow directly from the exponential flow.

\>0

# A complete source boundary ledger

The physical transverse radius is not the stereographic modulus: it is $r_\perp(t)=\sqrt{1-m_3(t)^2}=2|z(t)|/(1+|z(t)|^2)$. Thus damping is exponential in the chart but nonlinear after sphere reconstruction. The following table records the exact fixed-set dimensions for representative faces; the evidence file contains the corresponding high-precision rows.

  face         condition             flow type           sampled fixed set ($\tau>0$)
  ------------ --------------------- ------------------- ------------------------------
  identity     $\omega=0$            constant            $\mathbb S^2$
  precession   $\alpha=0,\omega>0$   latitude rotation   all or two poles
  damped       $\alpha>0,\omega>0$   north attractor     two poles
  north        $m=e_3$               equilibrium         north pole
  south        $m=-e_3$              equilibrium         south pole

The pure-precession circles are a continuous family, not isolated primitive cycles. This distinction is essential: the exact ODE has a physical clock, but no canonical primitive-orbit product or target divisor.

\>1

# Independent receipt and Route-A decision

The producer stores six flow rows, four pole-stability rows, five boundary rows and six sampled-time rows at 90 working decimal digits. A checker that does not import the producer reconstructs the chart, tanh solution, sphere norm, energy derivative, stability signs and resonance classification. Fourteen SymPy identities, byte replay and a hostile suite of 37 mutations cover numerical cells, theorem text, all five boundary-row semantics, corrected citation metadata, nested and top-level unknown keys, stale hashes, row counts, route flags and scope flags. The boundary atlas is therefore checked as a semantic table rather than as a collection of labels.

The strict tuple is $$(\mathtt{A0\_FAIL},\mathtt{A1\_WEAK},\mathtt{A2\_FAIL},\mathtt{A3\_FAIL},
 \mathtt{A4\_FORMAL\_HINT}),
\qquad \mathtt{overall=ROUTE\_A\_REJECTED}.$$ The latitude family and the identity face explain the A1 stop. No target prime or zero table, arithmetic local datum, Euler factor, root number, automorphy statement, Hilbert--Pólya operator or Route-B input is claimed.

9 M. Lakshmanan, "The fascinating world of the Landau--Lifshitz--Gilbert equation: an overview," *Philosophical Transactions of the Royal Society A* 369(1939), 1280--1300 (2011). DOI: [10.1098/rsta.2010.0319](https://doi.org/10.1098/rsta.2010.0319).

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; the source theorem contains no target arithmetic, Euler-factor, target-zero, automorphy or Hilbert--Pólya claim. **Data and code.** Exact formulas, regression rows and independent audit programs accompany HCS-C234. **AI-use disclosure.** Generative tools assisted drafting and code generation; internal checks validate the displayed identities. This is not external peer review.
