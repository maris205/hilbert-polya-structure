---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--c423-two-cycle-preperiodicity"
canonical_tex: "henon_dynamics/research_c419_c423/papers/C423_two_cycle_preperiodicity/main.tex"
canonical_pdf: "henon_dynamics/research_c419_c423/papers/C423_two_cycle_preperiodicity/main.pdf"
source_sha256: "dc722535544c9cd6def684c3808e5e281f53033b642bbc0b19f66f8d71d5c31c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A two-cycle test for simultaneous preperiodicity in characteristic three

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/research_c419_c423/papers/C423_two_cycle_preperiodicity>)
- [规范 TeX](<../../../../../henon_dynamics/research_c419_c423/papers/C423_two_cycle_preperiodicity/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/research_c419_c423/papers/C423_two_cycle_preperiodicity/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/research_c419_c423/papers/C423_two_cycle_preperiodicity/README.md>)
- [BibTeX](<../../../../../henon_dynamics/research_c419_c423/papers/C423_two_cycle_preperiodicity/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We classify simultaneous preperiodicity in the polynomial family $F_\lambda(X)=f(X)+\lambda$, where $f(X)=X^4+X^6$, over every field of characteristic three. For any two marked points $a,b$, infinitely many parameters in an algebraic closure make both points preperiodic if and only if both points are algebraic over the prime field or $a^4+a^6=b^4+b^6$. The equal exponent weights place this family outside the strict-weight classification: a known reduction still allows the two differences $f(b)-f(a)=1,-1$ when the points are not both constant. In this nonconstant case we eliminate both by an explicit two-cycle test. For the positive difference, the parameter $1-a-f(a)$ makes the first point alternate between $a$ and $1-a$, while the second point reaches that parameter after three steps and then escapes at a pole of $a$. Its local canonical height is exactly $\log|a|_v/36$, contradicting the known equality of local heights forced by infinitely many common parameters. We give the reduction from arbitrary fields and an elementary argument producing infinitely many periodic parameters for a single nonconstant marked point. The classification concerns this fixed equal-weight binomial, not all equal-weight families.
bibliography:
- references.bib
date: 'September 8, 2026'
title: |
  A two-cycle test for simultaneous preperiodicity\
  in characteristic three
```

## Markdown 正文

# The classification and its source boundary {#sec:result}

The family $X^4+X^6+\lambda$ in characteristic three admits a parameter at which one prescribed nonconstant point has period two and a potentially exceptional second point escapes. This observation closes the specific equal-weight example in @LeeNam2025 [Remark 4.5]. The large height-theoretic input and the reduction to three possible differences are due to the cited sources; the new step is the uniform orbit calculation and its application to the remaining cases.

Fix any field $L$ of characteristic three and an algebraic closure $\overline L$. Throughout, $k$ is the algebraic closure of $\mathbb F_3$ inside $\overline L$. Thus *constant* means belonging to $k$, even when $L$ has transcendence degree greater than one. Put $$f(X)=X^4+X^6,\qquad F_\lambda(X)=f(X)+\lambda .$$ For $a,b\in L$ define $$\operatorname{Prep}(f;a,b)=
 \{\lambda\in\overline L:
      a\text{ and }b\text{ have finite forward orbits under }F_\lambda\}.$$ Parameters are geometric: they need not belong to $L$. One application of $F_\lambda$ is one iteration, with the chosen parameter held fixed.

[\[thm:main\]]{#thm:main label="thm:main"} For every field $L$ of characteristic three and every $a,b\in L$, $$\label{eq:classification}
 |\operatorname{Prep}(f;a,b)|=\infty
 \quad\Longleftrightarrow\quad
 \bigl(a,b\in k\bigr)\ \text{or}\ \bigl(f(a)=f(b)\bigr).$$

For binomial degrees $d_i=3^{\ell_i}s_i$ with $3\nmid s_i$, the weights relevant to the known classification are $3^{\ell_i}(s_i-1)$. Here $$d_1=4=3^0\cdot4,\qquad d_2=6=3^1\cdot2,\qquad
 3^0(4-1)=3^1(2-1)=3.$$ Neither strict inequality between these weights holds. @LeeNam2025 [Theorems 1.5 and 4.4] show that an infinite common-parameter set for a pair not both constant forces $$\label{eq:three}
 f(b)-f(a)\in\{0,1,-1\}.$$ Their Remark 4.5 identifies the nonzero possibilities for this polynomial as a residual example. Our proof uses a two-cycle parameter to rule them out.

::: {#tab:scope}
  Family or regime                            Established scope                                                              Role in this note
  ------------------------------------------- ------------------------------------------------------------------------------ ------------------------------------------------------------------------------
  Monomials $X^d$                             Complete classification, with the additional prime-power case                  Background only; does not cover $X^4+X^6$.
  Strict-weight cases in the cited theorems   Classification in the Ghioca--Hsia and Lee--Nam regimes                        The two weights here are equal, so neither case applies.
  Equal weights, nonadditive                  Lee--Nam's necessary relation on $f(b)-f(a)$                                   Gives exactly $0,1,-1$ for the present polynomial.
  $X^4+X^6$, characteristic three             Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}   Excludes both nonzero differences using an exact two-cycle and local escape.

  : Source scope and the fixed residual conclusion. The first three rows summarize the source statements discussed in the text; they are not new claims of this note.
:::

The monomial background in Table [1](#tab:scope){reference-type="ref" reference="tab:scope"} is recalled through the accounts in @LeeNam2025 [Theorem 1.1] and @GhiocaHsia2026; no monomial theorem is needed in our proof. For the strict-weight Ghioca--Hsia result and the local-height input, we use the statements explicitly given in Lee--Nam, with their original attribution retained. The original Ghioca--Hsia proof is not reconstructed here.

Section [2](#sec:inputs){reference-type="ref" reference="sec:inputs"} specifies the two external inputs. Section [3](#sec:witness){reference-type="ref" reference="sec:witness"} gives the separating parameter and exact height. Section [4](#sec:proof){reference-type="ref" reference="sec:proof"} proves the theorem, including sufficiency and the arbitrary-field reduction.

# Local heights and the two external inputs {#sec:inputs}

We isolate the source-dependent part of the argument. All subsequent orbit, field and parameter-infinitude calculations are proved below.

[\[prop:reduction\]]{#prop:reduction label="prop:reduction"} If $|\operatorname{Prep}(f;a,b)|=\infty$ and $a,b$ are not both in $k$, then [\[eq:three\]](#eq:three){reference-type="eqref" reference="eq:three"} holds.

This is the specialization of @LeeNam2025 [Theorem 1.5, proved as Theorem 4.4]. Both prime-to-three degree parts exceed one, and the weights are equal as calculated above. In the nonzero case their relation reads $$(f(b)-f(a))^{\,3^1-3^0}=-\frac{4}{2}=1
 \quad\text{in characteristic three},$$ whose roots are $1$ and $-1$. We use the cited theorem for the necessity of this relation, not just the elementary solution of it.

For the second input, let $K$ be a finite extension of the perfect closure of $k(t)$. A place $v$ extends a function-field place trivial on $k$; write $|\cdot|_v$ for a compatible nonarchimedean absolute value. It extends to an algebraic closure and its completion $\mathbb C_v$. For $x,\lambda\in\mathbb C_v$ the local canonical height for our degree-six polynomial is $$\label{eq:height}
 \widehat h_{v,\lambda}(x)
 =\lim_{n\to\infty}6^{-n}\log^+|F_\lambda^n(x)|_v,\qquad
 \log^+u=\log\max\{1,u\}.$$ In particular any point with finite forward orbit has local height zero.

[\[prop:heights\]]{#prop:heights label="prop:heights"} Let $a,b\in K$, with $K$ as above. If infinitely many distinct $\lambda\in\overline K$ make both $a$ and $b$ preperiodic under $F_\lambda$, then $$\label{eq:equalheight}
 \widehat h_{v,\lambda}(a)=\widehat h_{v,\lambda}(b)
 \quad\text{for every place }v
 \text{ and every }\lambda\in\mathbb C_v .$$

We use @LeeNam2025 [Theorem 2.1], stated there from Ghioca--Hsia [@GhiocaHsia2026 Theorem 2.13]. The polynomial conditions for that input are monicity, degree at least two and $f(0)=0$, all satisfied here. There is no strict exponent-weight hypothesis in this height statement. It asserts equality at *every* parameter, not only at the original common-preperiodicity parameters. That quantifier is essential: our separating parameter will contradict the equality, not belong to the common-parameter set.

No discreteness of the extended value group will be needed. At a place over the pole of a transcendental $a$, nonzero elements of $k$ have absolute value one and $|a|_v>1$. These facts suffice for the strict dominance estimates below.

# The two-cycle parameter and escape {#sec:witness}

[\[lem:witness\]]{#lem:witness label="lem:witness"} Suppose $a$ is transcendental over $k$ and $f(b)=f(a)+1$. Set $$\label{eq:parameter}
 \lambda_*=1-a-f(a).$$ Then $a$ has least period two under $F_{\lambda_*}$. At every extension $v$ of the pole of $a$ in $k(a)$, $$\label{eq:separation}
 \widehat h_{v,\lambda_*}(a)=0,\qquad
 \widehat h_{v,\lambda_*}(b)=\frac{\log|a|_v}{36}>0 .$$

Direct expansion in characteristic three gives $$\label{eq:translations}
 \begin{aligned}
 f(-X)&=f(X),\\
 f(X+1)&=f(X)+X-1,\\
 f(X-1)&=f(X)-X-1.
 \end{aligned}$$ Consequently the two orbit segments are $$\label{eq:orbits}
 \begin{aligned}
 a&\longmapsto 1-a\longmapsto a,\\
 b&\longmapsto -a-1\longmapsto0\longmapsto\lambda_* .
 \end{aligned}$$ For completeness, the nontrivial second images follow from $$\begin{aligned}
 F_{\lambda_*}(1-a)
  &=f(a-1)+1-a-f(a)=-2a=a,\\
 F_{\lambda_*}(-a-1)
  &=f(a+1)+1-a-f(a)=0.
 \end{aligned}$$ The first image of $b$ uses $f(b)=f(a)+1$ and $2=-1$. The two points $a$ and $1-a$ are distinct, since their equality would force $a=-1\in k$. Thus the first orbit has least period two.

Write $C=|a|_v>1$. Since constants are units, the sixth-power term strictly dominates the other terms at $a$, giving $$\label{eq:radius}
 |f(a)|_v=C^6,\qquad |\lambda_*|_v=C^6.$$ If $|z|_v>C$, then $|z|_v^6$ is strictly larger than both $|z|_v^4$ and $|\lambda_*|_v$. The ultrametric inequality therefore gives the exact identity $$\label{eq:escape}
 |F_{\lambda_*}(z)|_v=|z|_v^6\qquad(|z|_v>C).$$ The second orbit in [\[eq:orbits\]](#eq:orbits){reference-type="eqref" reference="eq:orbits"} reaches $\lambda_*$ after three iterations; by [\[eq:radius\]](#eq:radius){reference-type="eqref" reference="eq:radius"}, this point is outside that radius. Induction using [\[eq:escape\]](#eq:escape){reference-type="eqref" reference="eq:escape"} yields $$|F_{\lambda_*}^n(b)|_v=C^{\,6^{n-2}}\qquad(n\ge3).$$ Substitution in [\[eq:height\]](#eq:height){reference-type="eqref" reference="eq:height"} gives $$\widehat h_{v,\lambda_*}(b)
   =\lim_{n\to\infty}6^{-n}6^{n-2}\log C
   =\frac{\log C}{36}.$$ The finite first orbit has height zero, proving the lemma.

The orbit identity is uniform in the pair: after the single relation $f(b)=f(a)+1$ is imposed, $\lambda_*$ depends only on $a$. The nonzero height does not come from a finite orbit sample; the strict escape inequality proves it for all subsequent iterations. The negative difference requires no separate construction: exchange the roles of $a$ and $b$.

# Parameter infinitude and the arbitrary-field proof {#sec:proof}

[\[lem:onepoint\]]{#lem:onepoint label="lem:onepoint"} For every $a\in L$, infinitely many $\lambda\in\overline L$ make $a$ preperiodic under $F_\lambda$. If $a\notin k$, then for every prime integer $\ell\ge2$ there is a parameter at which $a$ has least period $\ell$.

If $a\in k$, every $\lambda\in k$ works: $a$ and $\lambda$ belong to a common finite field, which the polynomial preserves. The field $k$ is infinite.

Otherwise $a$ is transcendental over $k$. For $n\ge1$ put $$P_n(T)=F_T^n(a)-a\in k(a)[T].$$ The first polynomial is monic of degree one. At each subsequent iteration the sixth power of the preceding iterate is the unique term of largest degree in $T$. Thus $P_n$ is monic of degree $6^{n-1}$. There is exactly one parameter fixing $a$: $$T_0=a-f(a).$$ Since $f'(X)=X^3$ in characteristic three, the chain rule at this fixed parameter gives $$\label{eq:simple}
 P_n'(T_0)=\sum_{j=0}^{n-1}a^{3j}\ne0.$$ Indeed the derivative obeys $D_{n+1}=a^3D_n+1$ with $D_1=1$; the displayed polynomial cannot vanish at a transcendental $a$. Hence $T_0$ is a simple root of every $P_n$.

For any prime integer $\ell\ge2$, the degree of $P_\ell$ exceeds one, so it has a root $\lambda_\ell\ne T_0$ in $\overline L$. The least period of $a$ at this parameter divides $\ell$ and is not one; it is exactly $\ell$. Two different primes cannot give the same parameter, since the least period at one parameter is unique. This produces infinitely many parameters. In particular, the argument includes $\ell=3$; no separability of all roots of $P_\ell$ is asserted or required.

Suppose first that $a,b\in k$. Every $\lambda\in k$ gives finite orbits for both points. If instead $f(a)=f(b)$, then $F_\lambda(a)=F_\lambda(b)$ for every parameter. Apply Lemma [\[lem:onepoint\]](#lem:onepoint){reference-type="ref" reference="lem:onepoint"} to the fixed marked point $a$. Whenever its orbit is finite, the orbit of $b$ joins it after one step. This proves sufficiency in both cases.

Now suppose $|\operatorname{Prep}(f;a,b)|=\infty$ and the two points are not both constant. Proposition [\[prop:reduction\]](#prop:reduction){reference-type="ref" reference="prop:reduction"} gives the three differences in [\[eq:three\]](#eq:three){reference-type="eqref" reference="eq:three"}. Difference zero is the desired conclusion. In either nonzero case both points are transcendental over $k$: if one were in $k$, the equation for the other's $f$-value would make it algebraic over the algebraically closed field $k$, hence also constant. Exchanging the marks if necessary, we may assume $$\label{eq:exception}
 f(b)=f(a)+1.$$

We now justify applying the function-field height input even when the original $L$ is arbitrary. Equation [\[eq:exception\]](#eq:exception){reference-type="eqref" reference="eq:exception"} makes $b$ algebraic over $k(a)$. Inside $\overline L$ let $$\label{eq:K}
 K_0=\bigcup_{r\ge0}k(a^{1/3^r}),\qquad K=K_0(b).$$ The purely inseparable roots in this union are unique. The field $K_0$ is the perfect closure of $k(a)$, and $K/K_0$ is finite. Thus $K$ has precisely the form required by Proposition [\[prop:heights\]](#prop:heights){reference-type="ref" reference="prop:heights"}.

Every parameter making $a$ preperiodic is algebraic over $k(a)$. Indeed it satisfies $$F_T^n(a)-F_T^m(a)=0
 \quad\text{at }T=\lambda,\qquad n>m\ge0.$$ For $m\ge1$ the two terms have different degrees $6^{n-1}$ and $6^{m-1}$ in $T$; for $m=0$ the second term is constant. This is therefore a nonzero polynomial equation over $k(a)$. The relative algebraic closure of $K$ inside the algebraically closed field $\overline L$ is an algebraic closure of $K$: any root in $\overline L$ of a polynomial over that relative closure is still algebraic over $K$, by transitivity of algebraicity. It contains every parameter in the assumed infinite set. Consequently the passage from $L$ to this function-field setting loses none of those parameters, including inseparable ones.

Choose a place $v$ of $K$ over the pole of $a$ in $k(a)$ and a compatible extension to its completed algebraic closure. Then $|a|_v>1$. Proposition [\[prop:heights\]](#prop:heights){reference-type="ref" reference="prop:heights"} forces equality of the two local heights at $\lambda_*=1-a-f(a)\in K$. But Lemma [\[lem:witness\]](#lem:witness){reference-type="ref" reference="lem:witness"} gives zero for $a$ and $\log|a|_v/36>0$ for $b$. This contradiction removes the positive difference, and exchanging the marks removes the negative one. Only $f(a)=f(b)$ remains. Necessity follows.

# Scope and dependence {#sec:scope}

Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} closes the classification for one fixed polynomial, with no restriction on the ambient field or the marked pair beyond characteristic three. Its proof is short because two substantial results have already reduced the question to a local height separation. The new parameter replaces the fixed-point test by a two-cycle test; it does not supply a new general equidistribution or local-height theorem.

The argument does not classify arbitrary equal-weight binomials, nor does it address infinitely intersecting orbits of two fixed polynomials. It gives a parameter-infinitude criterion, not a quantitative bound for the finite exceptional parameter sets in the other cases. There is no change of the iteration clock or identification of source arithmetic with target Euler factors, root numbers or a spectral realization.

#### Preparation and reproducibility.

All nonexternal mathematical steps are written out in this note; no experimental enumeration supports an infinite assertion. The accompanying research record preserves the exact source versions, full proof review and manuscript-transcription checks. Lee--Nam is cited at arXiv version 2, dated 11 October 2025. The Ghioca--Hsia journal metadata were verified at the publisher; the precise height statement was inspected in Lee--Nam rather than the original publisher proof. This manuscript was prepared with AI assistance. Its recorded reviews are internal AI-assisted checks, not human peer review or global-priority certification.
