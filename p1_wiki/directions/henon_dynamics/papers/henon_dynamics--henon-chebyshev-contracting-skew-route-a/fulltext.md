---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-chebyshev-contracting-skew-route-a"
canonical_tex: "henon_dynamics/henon_chebyshev_contracting_skew_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_chebyshev_contracting_skew_route_a/paper/main.pdf"
source_sha256: "d965dbfb88469acaa685683da7983172063ae385691522bb6e9afeb4a3c28ea5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# All-Period Orbits and Stability for a Chebyshev Contracting Skew Product

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_chebyshev_contracting_skew_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_chebyshev_contracting_skew_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_chebyshev_contracting_skew_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_chebyshev_contracting_skew_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze the triangular polynomial dynamics $F(x,y)=(4x^3-3x,y/4+x)$ and prove a complete all-period theorem. The base iterate is $T_{3^n}$; its fixed polynomial has exactly $3^n$ distinct real roots, and contraction gives one closing fiber coordinate above each root. Thus $\#\operatorname{Fix}(F^n)=3^n$, Möbius inversion gives every primitive orbit count, and the orbit-owned Artin--Mazur zeta is $(1-3z)^{-1}$. We also classify every fixed-point multiplier, stability determinant, orientation, and primitive repetition. Two exact controls show that unit fiber multiplier destroys isolated closure and that the nearby-looking cubic $4x^3-2x$ creates multiple roots and a neutral two-cycle. This replaces another finite orbit prefix by an all-period source theorem, but supplies no weighted target-facing Fredholm determinant, analytic completion, or natural lift.
author:
- 'Anonymous Route-A report'
title: |
  All-Period Orbits and Stability\
  for a Chebyshev Contracting Skew Product
```

## Markdown 正文

# Source lock and progress criterion

Let $$f(x)=T_3(x)=4x^3-3x,\qquad
 F(x,y)=\left(f(x),\frac14y+x\right),$$ on $\mathbb R^2$, with one application of $F$ as one clock unit. The normalization is the unweighted isolated fixed-point count, and $$\zeta_F(z)=\exp\!\left(\sum_{n\ge1}\#\operatorname{Fix}(F^n)\frac{z^n}{n}\right).$$ No source parameter is fitted and no external target data are used. The progress criterion is all-period completeness: a larger finite word table, a new low-period orbit, or a tangent matrix alone would not qualify. The period-twelve receipt later cited is a replay layer, not the proof horizon.

# Complete periodic atlas

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} For every $n\ge1$, $f^n=T_{3^n}$. The polynomial $T_{3^n}(x)-x$ has exactly $3^n$ distinct real roots, each with one unique fiber lift fixed by $F^n$. The lift preserves least period. Consequently $\#\operatorname{Fix}(F^n)=3^n$.

Put $m=3^n$. The cosine definition gives $T_a\circ T_b=T_{ab}$ and hence $f^n=T_m$. Writing $x=\cos\theta$ with $0\le\theta\le\pi$, the equation $\cos(m\theta)=\cos\theta$ yields $$\left\{\cos\frac{2\pi k}{m-1}:0\le k\le\frac{m-1}{2}\right\},\qquad
 \left\{\cos\frac{2\pi k}{m+1}:0\le k\le\frac{m+1}{2}\right\}.$$ Both lists are injective. Since $\gcd(m-1,m+1)=2$, they intersect exactly at $\{1,-1\}$ and contain $(m+1)/2+(m+3)/2-2=m$ points in total. At an interior root, $$T_m'(x)=m\frac{\sin(m\theta)}{\sin\theta}=\pm m,$$ while $T_m'(\pm1)=m^2$. Therefore $(T_m-x)'$ never vanishes at a root, so the degree-$m$ list is complete and simple.

Fiber iteration gives $$y_n=4^{-n}y+\sum_{j=0}^{n-1}4^{-(n-1-j)}T_{3^j}(x).$$ Because $1-4^{-n}\ne0$, every base root has the unique closing coordinate $$\label{eq:fiber}
 y_*(x,n)=\frac{\sum_{j=0}^{n-1}4^{-(n-1-j)}T_{3^j}(x)}{1-4^{-n}}.$$ For a base point of least period $p\mid n$, the unique $F^p$ lift is already fixed by $F^n$, so uniqueness identifies it with [\[eq:fiber\]](#eq:fiber){reference-type="eqref" reference="eq:fiber"}. Projection to the base prevents any period reduction.

# Primitive counts and orbit-owned zeta

Let $E_n$ count exact-period points and $P_n$ primitive orbits. Möbius inversion of Theorem [\[thm:atlas\]](#thm:atlas){reference-type="ref" reference="thm:atlas"} gives $$\label{eq:primitive}
 E_n=\sum_{d\mid n}\mu(d)3^{n/d},\qquad
 P_n=\frac1n\sum_{d\mid n}\mu(d)3^{n/d}.$$ The first eight exact receipt rows are shown in Table [1](#tab:counts){reference-type="ref" reference="tab:counts"}.

::: {#tab:counts}
                            $n$   1   2    3    4     5     6      7      8
  ----------------------------- --- --- ---- ---- ----- ----- ------ ------
    $\#\operatorname{Fix}(F^n)$   3   9   27   81   243   729   2187   6561
                          $P_n$   3   3    8   18    48   116    312    810
                        $P_n^+$   2   1    4    8    24    56    156    400
                        $P_n^-$   1   2    4   10    24    60    156    410

  : All formulas are unbounded in $n$; the rows are replay witnesses.
:::

The trace series therefore closes exactly: $$\label{eq:zeta}
 \zeta_F(z)=\exp\left(\sum_{n\ge1}3^n\frac{z^n}{n}\right)
 =\frac1{1-3z}
 =\prod_{\gamma\ \mathrm{primitive}}(1-z^{p_\gamma})^{-1}.$$ The logarithmic definition holds for $|z|<1/3$; the rational expression gives its meromorphic continuation. Equation [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} is an unweighted source Artin--Mazur zeta, not a target-facing weighted Fredholm determinant.

# All-period stability, orientation, and repetition

At a point fixed by $F^n$, $$\label{eq:jacobian}
 DF^n=\begin{pmatrix}T_m'(x)&0\\c_n(x)&4^{-n}\end{pmatrix},\qquad
 c_n(x)=\sum_{j=0}^{n-1}4^{-(n-1-j)}(T_{3^j})'(x).$$ The two endpoints have unstable multiplier $m^2$; among the interior points, $(m-3)/2$ have multiplier $+m$ and $(m-1)/2$ have multiplier $-m$. Every fixed point is thus a saddle and $$\label{eq:stability}
 \det(I-DF^n)=(1-T_m'(x))(1-4^{-n})\ne0.$$ The positive and negative unstable-orientation counts are $(m+1)/2$ and $(m-1)/2$. If $E_p^-$ counts exact-period points with negative primitive orientation, then $(3^n-1)/2=\sum_{p\mid n,\,n/p\ \mathrm{odd}}E_p^-$; odd-divisor Möbius inversion gives $$E_n^-=\frac12\sum_{\substack{d\mid n\\d\ \mathrm{odd}}}
 \mu(d)(3^{n/d}-1),\qquad P_n^-=E_n^-/n,$$ which gives the final two rows of Table [1](#tab:counts){reference-type="ref" reference="tab:counts"}.

For a primitive orbit $\gamma$ of period $p$ and unstable multiplier $\alpha_\gamma$, its $r$-fold repetition has multipliers $\alpha_\gamma^r$ and $4^{-pr}$. Hence the full repetition law is $$\label{eq:repeat}
 \det(I-DF^{pr})=(1-\alpha_\gamma^r)(1-4^{-pr}),\qquad
 \operatorname{or}(\gamma^r)=\operatorname{sgn}(\alpha_\gamma)^r.$$ For $p>1$, $\alpha_\gamma=\pm3^p$; at period one the endpoint multipliers are $9$ and the central multiplier is $-3$.

# Exact controls

The fiber contraction is not cosmetic. For $F_1(x,y)=(T_3(x),y+x)$, period-one closure requires $x=0$: the base point $x=0$ carries an entire fixed line, while $x=\pm1$ admits no closing fiber. The stable factor in [\[eq:stability\]](#eq:stability){reference-type="eqref" reference="eq:stability"} becomes $1-1=0$.

The Chebyshev coefficient is equally decisive. For $g(x)=4x^3-2x$, $$\begin{aligned}
 g^2(x)-x&=x(2x-1)^3(2x+1)^3(4x^2-3),\\
 g^2(x)-T_9(x)&=x(192x^6-240x^4+80x^2-5).\end{aligned}$$ Thus the second fixed equation has only five distinct roots rather than nine; $\pm1/2$ form a neutral period-two orbit. Both controls destroy named theorem clauses exactly, rather than degrading a fitted score.

# Progress, verification, and boundary

Earlier dynamics-variant reports repeatedly stopped at finite word ledgers or one low-period monodromy, whereas the source-owned trace-class contraction had only one periodic base point. Theorems [\[thm:atlas\]](#thm:atlas){reference-type="ref" reference="thm:atlas"}--[\[eq:repeat\]](#eq:repeat){reference-type="eqref" reference="eq:repeat"} place a complete nontrivial real atlas, primitive/repeated bookkeeping, an orbit-owned zeta, and stability/orientation data in one source model. This is the explicit progress of C126. A period-twelve evidence receipt, an independent checker, 73 fresh SymPy predicates, canonical byte replay, and eighteen rejected hostile mutations audit the implementation.

The result has no prime-like orbit semantics or mandatory target controls, so A1 remains weak. No weighted target-facing Fredholm owner exists, so A2 fails. No target functional equation, completion factors, counting law, or controlled target continuation is supplied, so A3 fails. No natural unitary, scattering, or Hamiltonian lift is defined, so A4 fails. The canonical verdict is $$\texttt{(A1\_WEAK, A2\_FAIL, A3\_FAIL, A4\_FAIL)},\qquad
 \texttt{ROUTE\_A\_EXPLORATORY}.$$ Route B is unauthorized. We make no claim about a target divisor, arithmetic/local data, Euler factors, root numbers, automorphy, Hilbert--Pólya, or Riemann zeros. The literal release firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`; external novelty was not assessed.
