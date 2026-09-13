---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-quicksort-comparison-contraction-route-a"
canonical_tex: "henon_dynamics/henon_quicksort_comparison_contraction_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_quicksort_comparison_contraction_route_a/paper/main.pdf"
source_sha256: "1464250b660fcb020e50832d0a6a71c07d18dea2184b106e89fc2d5a93424e4e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Finite Costs and the Non-Gaussian Contraction Limit of Randomized Quicksort

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_quicksort_comparison_contraction_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_quicksort_comparison_contraction_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_quicksort_comparison_contraction_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_quicksort_comparison_contraction_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the comparison-cost distribution of classical single-pivot Quicksort by an exact probability-generating-polynomial recurrence and derive closed formulas for its mean and variance at every input size. \>0 After exact centering, the normalized costs converge in quadratic Wasserstein distance to the unique centered finite-variance fixed point of the Quicksort distributional transform. \>1 Its variance is $7-2\pi^2/3$ and its positive third moment is $16\zeta(3)-19$, proving a genuinely non-Gaussian limit; endpoint pivots, cost conventions and Route-A boundaries are closed explicitly.
author:
- 'Route-A source-local certificate HCS-C302'
date: 2 September 2026
title: |
  Exact Finite Costs and the Non-Gaussian\
  Contraction Limit of Randomized Quicksort
```

## Markdown 正文

trailerid \[\<C3022026090200000000000000000000\>\<C3022026090200000000000000000000\>\]

# The finite recursive law

Let $X_n$ count key comparisons made by classical single-pivot Quicksort on a uniform random permutation of $n$ distinct keys. The pivot is compared once with every other key, and $X_0=X_1=0$. If $I_n$ is uniform on $\{0,\ldots,n-1\}$, the relative orders in the two subarrays are independent uniform permutations; hence $$\label{eq:rec}
 X_n\mathrel{\mathop=\limits^d}X_{I_n}+X'_{n-1-I_n}+n-1.$$ All variables on the two recursive branches are independent conditional on $I_n$.

[\[thm:finite\]]{#thm:finite label="thm:finite"} For $G_n(z)=\mathbb Ez^{X_n}$, $G_0=G_1=1$ and $$\label{eq:pgf}
 G_n(z)=\frac{z^{n-1}}n\sum_{j=0}^{n-1}G_j(z)G_{n-1-j}(z),\qquad n\ge2.$$ Writing $H_n=\sum_{k=1}^n k^{-1}$ and $H_n^{(2)}=\sum_{k=1}^n k^{-2}$, with empty sums zero, $$\begin{aligned}
 \mu_n:=\mathbb EX_n&=2(n+1)H_n-4n,\label{eq:mean}\\
 v_n:=\operatorname{Var}X_n&=7n^2-4(n+1)^2H_n^{(2)}
                 -2(n+1)H_n+13n.\label{eq:variance}\end{aligned}$$ These formulas include $n=0,1$.

Conditioning [\[eq:rec\]](#eq:rec){reference-type="eqref" reference="eq:rec"} on the pivot rank and multiplying independent PGFs gives [\[eq:pgf\]](#eq:pgf){reference-type="eqref" reference="eq:pgf"}. Expectations satisfy $$\label{eq:mrec}
 \mu_n=n-1+\frac2n\sum_{j=0}^{n-1}\mu_j,$$ whose successive difference is solved by [\[eq:mean\]](#eq:mean){reference-type="eqref" reference="eq:mean"}. Total variance gives $$\label{eq:vrec}
 v_n=\frac2n\sum_{j=0}^{n-1}v_j
 +\operatorname{Var}\!\left(\mu_{I_n}+\mu_{n-1-I_n}\right).$$ Substitution of [\[eq:mean\]](#eq:mean){reference-type="eqref" reference="eq:mean"}, followed by the elementary harmonic-sum identities, reduces [\[eq:vrec\]](#eq:vrec){reference-type="eqref" reference="eq:vrec"} to [\[eq:variance\]](#eq:variance){reference-type="eqref" reference="eq:variance"}. Both formulas also verify the two boundary values directly.

\>0

# The contraction limit

Put $Y_n=(X_n-\mu_n)/(n+1)$ and define, with $0\log0=0$, $$\label{eq:toll}
 C(u)=1+2u\log u+2(1-u)\log(1-u).$$

[\[thm:limit\]]{#thm:limit label="thm:limit"} The laws of $Y_n$ converge in quadratic Wasserstein distance, and under a recursive coupling in $L^2$, to the unique centered finite-second-moment law satisfying $$\label{eq:fixed}
 Y\mathrel{\mathop=\limits^d} UY_1+(1-U)Y_2+C(U),$$ where $U$ is uniform on $[0,1]$ and $Y_1,Y_2$ are independent copies of $Y$, independent of $U$.

Center [\[eq:rec\]](#eq:rec){reference-type="eqref" reference="eq:rec"} using [\[eq:mean\]](#eq:mean){reference-type="eqref" reference="eq:mean"}. With $A_n=(I_n+1)/(n+1)$, $B_n=1-A_n$, the exact recurrence is $$Y_n=A_nY_{I_n}+B_nY'_{n-1-I_n}+C_n(I_n),\quad
C_n(j)=\frac{n-1+\mu_j+\mu_{n-1-j}-\mu_n}{n+1}.$$ Couple $I_n=\lfloor nU\rfloor$. Then $A_n\to U$ uniformly. Standard harmonic bounds, with the two endpoints evaluated directly, give $C_n(\lfloor nU\rfloor)\to C(U)$ in $L^2$; the exact mean recurrence gives $n^{-1}\sum_jC_n(j)=0$, hence $\int_0^1C(u)\,\mathrm du=0$.

On centered finite-second-moment laws, couple two inputs optimally and use independent copies on the two branches. Cross terms vanish and the transform $T$ in [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"} obeys $$\label{eq:contract}
 d_2(T\nu,T\nu')^2\le
 \mathbb E\{U^2+(1-U)^2\}d_2(\nu,\nu')^2
 =\frac23d_2(\nu,\nu')^2.$$ Banach's theorem gives one fixed law. On an i.i.d.-$U$ binary tree, give node $v$ the product weight $L_v$ along its root path and put $\Delta_r=\sum_{|v|=r}L_vC(U_v)$. Distinct levels are orthogonal and $\mathbb E\Delta_r^2=(\mathbb EC(U)^2)(2/3)^r$, so $\sum_r\Delta_r$ converges in $L^2$; splitting at the root realizes the unique fixed law. On the same tree realize $\widehat Y_n$ by using $I_m=\lfloor mU_v\rfloor$ whenever a node has size $m$. Then $\widehat Y_n\mathrel=^dY_n$. Put $e_n=\|\widehat Y_n-Y\|_2$. Centering and independence of the two subtrees, followed by Minkowski's inequality, give $$\label{eq:mixed}
e_n\le Q_n^{1/2}+\delta_n,\qquad
Q_n=\frac2n\sum_{j=0}^{n-1}\left(\frac{j+1}{n+1}\right)^2e_j^2,
\qquad\delta_n\to0.$$ Here $\delta_n$ is the $L^2$ norm of the coefficient and grid-toll error; the uniform coefficient error is $O(n^{-1})$, and the harmonic estimate above makes the toll part $o(1)$. Formula [\[eq:variance\]](#eq:variance){reference-type="eqref" reference="eq:variance"} makes $(e_n)$ bounded. Put $M_N=\sup_{j\ge N}e_j$, so $M_N\downarrow D=\limsup e_n$, and split $Q_n$ at this cutoff. The finitely many small-$j$ terms have total weight $O(n^{-3})$; the rest is bounded by $M_N$. Since $$\frac2n\sum_{j=0}^{n-1}\left(\frac{j+1}{n+1}\right)^2
 =\frac{2n+1}{3(n+1)}\longrightarrow\frac23,$$ the limsup of [\[eq:mixed\]](#eq:mixed){reference-type="eqref" reference="eq:mixed"} gives $D\le\sqrt{2/3}\,M_N$. Letting $N\to\infty$ yields $D\le\sqrt{2/3}\,D$, which forces $D=0$. Thus this explicit recursive coupling realizes $L^2$ convergence and, in particular, the laws converge in $d_2$.

\>1

# Exact moments and non-Gaussianity

[\[lem:l3\]]{#lem:l3 label="lem:l3"} The fixed law in Theorem [\[thm:limit\]](#thm:limit){reference-type="ref" reference="thm:limit"} has a finite absolute third moment.

On an independent binary tree set $L_\varnothing=1$, $L_{v0}=L_vU_v$, $L_{v1}=L_v(1-U_v)$, and $\Delta_r=\sum_{|v|=r}L_vC(U_v)$. The toll is bounded and centered. A conditional Rosenthal inequality at level $r$, together with $$\mathbb E\sum_{|v|=r}L_v^2=(2/3)^r,\qquad
 \mathbb E\sum_{|v|=r}L_v^3=(1/2)^r,\qquad \sum_{|v|=r}L_v^2\le1,$$ gives $\|\Delta_r\|_3\le K\{(2/3)^{r/3}+(1/2)^{r/3}\}$. Thus $\sum_r\Delta_r$ converges in $L^3$. Splitting it at the root gives [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}; its centered finite-variance law is the unique $L^2$ fixed point, proving the claim.

Taking second moments in [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}, or taking the leading coefficient in [\[eq:variance\]](#eq:variance){reference-type="eqref" reference="eq:variance"}, gives $$\label{eq:m2}
 m_2=\mathbb EY^2=7-\frac{2\pi^2}{3}>0.$$ Lemma [\[lem:l3\]](#lem:l3){reference-type="ref" reference="lem:l3"} licenses cubing the fixed-point identity. Independence and centering give $$\label{eq:m3rec}
 m_3=\frac12m_3+3m_2\int_0^1C(u)(u^2+(1-u)^2)\,\mathrm du
                  +\int_0^1C(u)^3\,\mathrm du.$$ Here the two integrals are respectively $1/18$ and $-32/3+\pi^2/9+8\zeta(3)$. Beta-function differentiation then evaluates [\[eq:m3rec\]](#eq:m3rec){reference-type="eqref" reference="eq:m3rec"} as $$\label{eq:m3}
 \mathbb EY^3=16\zeta(3)-19>0.$$ Moreover $\zeta(3)>\sum_{k=1}^{6}k^{-3}=28567/24000$, so the displayed moment exceeds $67/1500$. A centered Gaussian has zero third moment, so the limit is not Gaussian.

# Boundary, evidence, and Route A

Empty and singleton inputs cost zero; two keys cost one. Extreme pivots, including an empty branch, are already present in [\[eq:pgf\]](#eq:pgf){reference-type="eqref" reference="eq:pgf"}. The frozen cost counts comparisons only: swaps, recursion depth, repeated keys, three-way partitioning and sampled pivots are separate models. Normalization by $n$ has the same asymptotic law for $n\ge1$ but is not the exact finite recurrence used here.

The evidence artifact expands every PGF through a declared cutoff, recomputes moments from coefficients, verifies the harmonic formulas and beta derivatives independently, and attacks centering, endpoints and a false Gaussian claim. Finite rows are regression evidence; the all-$n$ theorem is the analytic recurrence and contraction argument.

C291's first-event convolution belongs to dimer adsorption, not recursive permutation splitting. The strict Route-A tuple is $(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
\mathrm{A3\_FAIL},\mathrm{A4\_FAIL})$ and Route B is locked. Input size is not an arithmetic clock, finite PGFs are not target determinants, and the distributional fixed point is not a Hilbert--Pólya operator. Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Literature ownership and AI-use statement {#literature-ownership-and-ai-use-statement .unnumbered}

Hoare introduced Quicksort [@Hoare]; Régnier [@Regnier] and Rösler [@Rosler] established its limiting distribution and contraction approach. We make no literary priority claim. AI tools assisted exact-algebra checks, hostile review and manuscript preparation; all formulas and proof obligations are exposed here and in the independent certificate.

3 C. A. R. Hoare, "Quicksort," *The Computer Journal* 5 (1962), 10--16, doi:10.1093/comjnl/5.1.10. M. Régnier, "A limiting distribution for quicksort," *RAIRO Theor. Inform. Appl.* 23 (1989), 335--343. U. Rösler, "A limit theorem for Quicksort," *RAIRO Theor. Inform. Appl.* 25 (1991), 85--100.
