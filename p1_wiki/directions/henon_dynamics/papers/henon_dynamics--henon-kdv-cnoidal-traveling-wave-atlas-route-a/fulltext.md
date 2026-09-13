---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-kdv-cnoidal-traveling-wave-atlas-route-a"
canonical_tex: "henon_dynamics/henon_kdv_cnoidal_traveling_wave_atlas_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_kdv_cnoidal_traveling_wave_atlas_route_a/paper/main.pdf"
source_sha256: "55fa9cef3f7236ec9fae8edaa59265b5cdba3fd402b4e960c3c4164061b861f2"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Root-Complete Cnoidal and Soliton Atlas for KdV Traveling Waves

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_kdv_cnoidal_traveling_wave_atlas_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_kdv_cnoidal_traveling_wave_atlas_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_kdv_cnoidal_traveling_wave_atlas_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_kdv_cnoidal_traveling_wave_atlas_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We classify every bounded classical real traveling profile of the plus-sign Korteweg--de Vries equation directly from its cubic first integral. Three simple real roots give one translated Jacobi-$\operatorname{cn}^2$ family with exact speed and fundamental period; a lower double root gives the $\operatorname{sech}^2$ soliton, and all remaining root topologies give only bounded constants. \>0 The classification also closes the first two period moments, the harmonic limit, Galilean covariance, and the physical-time return on a fundamental circle. Twelve rational-root rows are checked by independent regularized quadrature and exact symbolic reconstruction. \>1 The coherent periodic family is not a complete primitive-orbit census for KdV phase space. No arithmetic, target-determinant, stability, or Hilbert--Pólya claim is made.
author:
- HCS Research Program
date: 31 August 2026(revision 2)
title: |
  A Root-Complete Cnoidal and Soliton Atlas\
  for KdV Traveling Waves
```

## Markdown 正文

suppressoptionalinfo 611 trailerid \[\<C2562026083100000000000000000000\>\<C2562026083100000000000000000000\>\]

# Frozen equation and cubic reduction

We fix $$u_t+6uu_x+u_{xxx}=0,\qquad u(x,t)=U(\xi),\quad \xi=x-ct,
 \label{eq:kdv}$$ with $U\in C^3(\mathbb R;\mathbb R)$ bounded. Integrating the traveling equation twice gives $$U''=cU-3U^2+A,\qquad
 (U')^2=-2U^3+cU^2+2AU+B.                 \label{eq:first}$$ If the cubic has real roots $r_1\le r_2\le r_3$, its compact allowed branch has the convention $$(U')^2=2(r_3-U)(U-r_2)(U-r_1),           \label{eq:factor}$$ and coefficient comparison forces $$c=2(r_1+r_2+r_3),\quad
 A=-(r_1r_2+r_1r_3+r_2r_3),\quad B=2r_1r_2r_3. \label{eq:coeff}$$ These signs are part of the frozen object: switching the sign of $6uu_x$ would change every speed convention.

# Complete bounded-profile theorem

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} Every nonconstant bounded entire profile satisfying [\[eq:first\]](#eq:first){reference-type="eqref" reference="eq:first"} is, up to translation of $\xi$, exactly one of the following.

1.  If $r_1<r_2<r_3$, put $$m=\frac{r_3-r_2}{r_3-r_1},\qquad
     k=\sqrt{\frac{r_3-r_1}{2}}.$$ Then $0<m<1$ and $$U(\xi)=r_2+(r_3-r_2)\operatorname{cn}^2(k\xi;m).       \label{eq:cnoid}$$

2.  If $r_1=r_2<r_3$, then $$U(\xi)=r_1+(r_3-r_1)\operatorname{sech}^2(k\xi),
     \qquad k=\sqrt{(r_3-r_1)/2}.             \label{eq:soliton}$$

An upper double root, a triple root, or a cubic with only one real root has no nonconstant bounded entire profile. Constant profiles remain solutions, but do not select a traveling speed.

#### Proof.

The negative leading coefficient in [\[eq:first\]](#eq:first){reference-type="eqref" reference="eq:first"} leaves a compact positive interval only for three simple roots, namely $[r_2,r_3]$, or for the lower-double-root closure $[r_1,r_3]$. Simple endpoints are reached and reflected in finite time; the lower double root is approached only at infinite time. Every other positive component is unbounded, proving exhaustion. For $q=\operatorname{cn}^2(k\xi;m)$, $$q_\xi^2=4k^2q(1-q)(1-m+mq).$$ Substitution of the displayed $m$ and $k$ is exactly [\[eq:factor\]](#eq:factor){reference-type="eqref" reference="eq:factor"}; its derivative gives the profile ODE. The identity $\operatorname{cn}(s;1)=\operatorname{sech}s$ gives the homoclinic face. Thus the result is a root classification, not an ansatz selected from a numerical plot.

=0 The baseline stops here: it fixes the all-root theorem, the plus-sign speed, and both double-root conventions before moments or executable receipts are added.

\>0

# Period, moments, degenerations, and clock

Since $\operatorname{cn}^2$ has period $2K(m)$, the *fundamental* spatial period and mean are $$L=2\sqrt{\frac2{r_3-r_1}}K(m),\qquad
 \langle U\rangle=r_1+(r_3-r_1)\frac{E(m)}{K(m)}.       \label{eq:periodmean}$$ The common $4K$ convention for $\operatorname{cn}$ would double $L$ incorrectly. With $$C_2=\frac{E-(1-m)K}{mK},\quad
 C_4=1-\frac{2(K-E)}{mK}
 +\frac{(2+m)K-2(1+m)E}{3m^2K},$$ one further exact observable is $$\langle U^2\rangle=r_2^2+2r_2(r_3-r_2)C_2+(r_3-r_2)^2C_4. \label{eq:second}$$ As $r_2\downarrow r_1$, [\[eq:cnoid\]](#eq:cnoid){reference-type="eqref" reference="eq:cnoid"} tends to [\[eq:soliton\]](#eq:soliton){reference-type="eqref" reference="eq:soliton"}; its excess mass is $2\sqrt{2(r_3-r_1)}$. As $r_2\uparrow r_3$ with $r_1$ fixed, the amplitude vanishes and $$L\longrightarrow\frac{2\pi}{\sqrt{2(r_3-r_1)}}.$$ For every $a\in\mathbb R$, $u_a(x,t)=u(x-6at,t)+a$ solves [\[eq:kdv\]](#eq:kdv){reference-type="eqref" reference="eq:kdv"}; all roots shift by $a$ and $c$ by $6a$, while $m$ and $L$ are unchanged. On a circle of length $L$, $c\ne0$ gives primitive physical-time return $T=L/|c|$; $c=0$ is stationary.

# Independent finite receipt

The producer evaluates twelve ordered rational-root triples at 90 decimal digits. The checker does not infer [\[eq:periodmean\]](#eq:periodmean){reference-type="eqref" reference="eq:periodmean"} from those values: it independently computes $$L=2\sqrt2\int_0^{\pi/2}
 \frac{\,\mathrm d\theta}{\sqrt{r_2-r_1+(r_3-r_2)\sin^2\theta}}$$ and uses the same regularized weight for $\langle U\rangle$ and $\langle U^2\rangle$. It then checks separate elliptic nodes.

   row   $r_1$   $r_2$   $r_3$    $m$     $c$      $L$
  ----- ------- ------- ------- ------- ------- ----------
   P01   $-5$    $-2$     $1$    $1/2$   $-12$   $2.1409$
   P06   $-1$     $0$     $1$    $1/2$    $0$    $3.7081$
   P09    $0$     $1$     $3$    $2/3$    $8$    $3.3133$
   P12    $2$     $5$     $9$    $4/7$   $32$    $2.0524$

  : Representative rows; JSON retains 75 significant digits.

The full gate contains 602 independent-checker assertions, 245 SymPy identities, clean-process byte replay, and 49/49 repaired-hash hostile mutation rejections. These counts certify implementation and boundary conventions, not the continuum theorem by enumeration.

\>1

# Collision and Route-A boundaries

The initial porous-medium proposal was rejected because C207 already owns the full Barenblatt exponent atlas. C256 instead owns a dispersive KdV cubic root theorem. C195 (viscous Burgers), C202 (Fisher--KPP), C221 (cubic NLS), C231 (Allen--Cahn), and C236 (sine--Gordon) do not contain [\[eq:factor\]](#eq:factor){reference-type="eqref" reference="eq:factor"}--[\[eq:second\]](#eq:second){reference-type="eqref" reference="eq:second"}. This is workspace bookkeeping, not a literature-priority claim.

The coherent circle returns are an exact family but not a full primitive orbit and monodromy census of KdV phase space, hence `A1_WEAK`. The Lax formalism is source-native but supplies no target quantization, hence only `A4_FORMAL_HINT`. There is no intrinsic rational-prime owner, logarithmic clock, target-weighted zeta, global target analytic structure, or Weil compression. The strict tuple is $$\texttt{(A0\_FAIL,A1\_WEAK,A2\_FAIL,A3\_FAIL,A4\_FORMAL\_HINT)},$$ with `ROUTE_A_REJECTED` and Route B false. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`. No arithmetic local data, Euler factors, root numbers, automorphy, target divisor or functional equation, Hilbert--Pólya operator, or target spectral claim is made.

# Conclusion and limitations

The result is one complete coherent-family advance: cubic-root exhaustion, cnoidal and soliton formulas, exact period observables, all declared degenerations, and the physical circle clock. It is not a nonlinear or spectral stability theorem and does not classify arbitrary KdV solutions. Its formulas are classical and re-derived source-locally; no arithmetic or literature-priority conclusion is inferred.

9 D. J. Korteweg and G. de Vries, "On the change of form of long waves advancing in a rectangular canal, and on a new type of long stationary waves," *Philosophical Magazine* 39 (1895), 422--443, [doi:10.1080/14786449508620739](https://doi.org/10.1080/14786449508620739). M. Leitner and A. Mikikits-Leitner, "Nonlinear differential identities for cnoidal waves," *Mathematische Nachrichten* 287 (2014), 2040--2056, [doi:10.1002/mana.201300233](https://doi.org/10.1002/mana.201300233). P. D. Lax, "Integrals of nonlinear equations of evolution and solitary waves," *Communications on Pure and Applied Mathematics* 21 (1968), 467--490, [doi:10.1002/cpa.3160210503](https://doi.org/10.1002/cpa.3160210503).
