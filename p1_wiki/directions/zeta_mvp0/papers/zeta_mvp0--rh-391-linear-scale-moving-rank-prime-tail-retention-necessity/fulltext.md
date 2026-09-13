---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-391-linear-scale-moving-rank-prime-tail-retention-necessity"
canonical_tex: "zeta_mvp0/papers/RH-391-linear-scale-moving-rank-prime-tail-retention-necessity/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-391-linear-scale-moving-rank-prime-tail-retention-necessity/main.pdf"
source_sha256: "27d58b4745fe0ce8e61ed788d67f76f47ac72774e5e808d952bb51cc9cb83061"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Linear-Scale Moving-Rank Prime-Tail Retention Necessity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-391-linear-scale-moving-rank-prime-tail-retention-necessity>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-391-linear-scale-moving-rank-prime-tail-retention-necessity/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-391-linear-scale-moving-rank-prime-tail-retention-necessity/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-391-linear-scale-moving-rank-prime-tail-retention-necessity/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-391-linear-scale-moving-rank-prime-tail-retention-necessity/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Maynard's bounded-gap theorem contains an infinite subsequence of consecutive-prime edges with one fixed repeated gap $h_*\le600$. On those edges, let the same exact rank $r$ be used at both endpoints, with $r\to\infty$ and $r\le Cx$ for a fixed $C>0$. We compare the strict prime tail $P_r$ with the power and prime-density integrals $I_{2r}$ and $J_r$, and lift both comparisons through the frozen seven-channel square-clock endpoint. If $q=x+h_*$ and $$a=\left(\frac{x^2}{q^2-1}\right)^r,
   \qquad \rho=\left(\frac{x}{q}\right)^{2r},$$ then every scalar and endpoint edge jump, under its natural normalization, equals $a+o(1)$. The two endpoint scales are unequal; retaining the factor $\rho$ gives the sharp pair mechanism. If $r/x\to\lambda<\infty$, each natural pair maximum has lower profile $e^{-2\lambda h_*}/(1+e^{-2\lambda h_*})$. Without convergence of $r/x$, the linear bound gives $e^{-1200C}/2$; for $r=o(x)$ it gives $1/2$. The pair errors also dominate $P_{r+1}$ by an unbounded factor. The proof uses elementary integer-tail bounds, a uniform all-rank endpoint coefficient, and Taylor control. It does not use a linear-rank asymptotic $P_r\sim K_r$. A 60-row exact artifact records the finite algebra and source closure but is not an analytic proof.
author:
- RH research program
bibliography:
- references.bib
date: 'August 10, 2026'
title: 'Linear-Scale Moving-Rank Prime-Tail Retention Necessity'
```

## Markdown 正文

**Keywords:** moving rank; strict prime tails; bounded consecutive-prime gaps; endpoint retention; square-clock gap.

# Definitions and main theorem

Let $3=p_1<p_2<\cdots$ be the odd primes. At the endpoint $x=p_y$ and for every exact integer $j\ge1$, define the strict and smooth tails $$P_j(y)=\sum_{p>x}(p^2-1)^{-j},\qquad
 I_{2j}(x)=\int_x^\infty\frac{t^{-2j}}{\log t}\,dt,
 \qquad
 J_j(x)=\int_x^\infty\frac{dt}{(t^2-1)^j\log t}.
 \label{eq:tails}$$ The endpoint prime is excluded from $P_j(y)$. For the rank $r$ under consideration, put $$E^{I}_r(y)=P_r(y)-I_{2r}(x),\qquad
 E^{J}_r(y)=P_r(y)-J_r(x).
 \label{eq:scalar-errors}$$

We recall only the endpoint data needed below. For $2\le m\le8$, set $$u_m=\prod_{p\ \mathrm{odd}}\frac{1-m/p^2}{1-1/p^2},\quad
 (\alpha_m)=(-2,2,-2,2,-2,2,-2),\quad
 (\beta_m)=(1,-2,2,-2,2,-2,2).
 \label{eq:endpoint-data}$$ For $z=(z_1,\ldots,z_7)$ write $$Z_m(z)=u_me^{z_{m-1}},\qquad
 C(Z)=1+\sum_{m=2}^8\alpha_mZ_m,\qquad
 W(Z)=\sum_{m=2}^8\beta_mZ_m,$$ and $$F(z)=2\{C(u)-C(Z(z))\}-4W(Z(z))(1-e^{-z_1}).
 \label{eq:endpoint-map}$$ RH-383 proves the exact normal form $\operatorname{Gap}_{P}(y)=F(\Phi^{P}(y))/\pi^2$, where $$\Phi^{P}_c(y)=\sum_{j\ge1}\frac{c^jP_j(y)}j,
 \qquad 1\le c\le7.
 \label{eq:actual-coordinate}$$ The two retained-head surrogates use the same exact rank $r$: $$\begin{aligned}
 \Phi^{I,<r}_c(y)&=\sum_{j<r}\frac{c^jP_j(y)}j
      +\sum_{j\ge r}\frac{c^jI_{2j}(x)}j,
 \label{eq:I-coordinate}\\
 \Phi^{J,<r}_c(y)&=\sum_{j<r}\frac{c^jP_j(y)}j
      +\sum_{j\ge r}\frac{c^jJ_j(x)}j.
 \label{eq:J-coordinate}\end{aligned}$$ Define $\operatorname{Gap}_{I,<r}=F(\Phi^{I,<r})/\pi^2$, $\operatorname{Gap}_{J,<r}=F(\Phi^{J,<r})/\pi^2$, and the unscaled endpoint discrepancies $$\Delta^{I}_r(y)=\pi^2\{\operatorname{Gap}_{P}(y)-\operatorname{Gap}_{I,<r}(y)\},\qquad
 \Delta^{J}_r(y)=\pi^2\{\operatorname{Gap}_{P}(y)-\operatorname{Gap}_{J,<r}(y)\}.
 \label{eq:endpoint-errors}$$

For $r\ge1$, let $$\begin{aligned}
 v_r&=\left(\frac{c^r}{r}\right)_{c=1}^7,
 &\gamma_r&=\nabla F(0)\mathbin{\cdot}v_r \notag\\
 &=\frac4r\{3^ru_4-2^ru_3+5^ru_6-4^ru_5 \notag\\
 &\hspace{3.2em}+7^ru_8-6^ru_7
   +2(u_3-u_4+u_5-u_6+u_7-u_8)\}.
 \label{eq:gamma}\end{aligned}$$ Let $\underline u_8$ denote the exact outward rational lower endpoint for $u_8$ frozen in RH-384, and set $$\kappa_\gamma=\frac{4\underline u_8}{7}
 >0.0347017856545.
 \label{eq:kappa}$$

[\[thm:main\]]{#thm:main label="thm:main"} There is a fixed positive integer $h_*\le600$ and there are infinitely many consecutive-prime edges $$x=p_y,\qquad q=p_{y+1}=x+h_*.
 \label{eq:fixed-edges}$$ Fix $C>0$. Along any sequence of these edges choose exact integers $r=r_y$ such that $$r\longrightarrow\infty,\qquad r\le Cx,
 \label{eq:linear-rank}$$ and use this same $r$ at both endpoints. Put $$a=\left(\frac{x^2}{q^2-1}\right)^r,\qquad
 \rho=\left(\frac{x}{q}\right)^{2r}.
 \label{eq:a-rho}$$ Then $\rho/a=(1-q^{-2})^r\to1$, and $$\begin{aligned}
 x^{2r}\{E^{I}_r(y)-E^{I}_r(y+1)\}&=a+o(1),
 &x^{2r}\{E^{J}_r(y)-E^{J}_r(y+1)\}&=a+o(1),
 \label{eq:scalar-jumps}\\
 \frac{x^{2r}}{\gamma_r}\{\Delta^{I}_r(y)-\Delta^{I}_r(y+1)\}&=a+o(1),
 &\frac{x^{2r}}{\gamma_r}\{\Delta^{J}_r(y)-\Delta^{J}_r(y+1)\}&=a+o(1).
 \label{eq:endpoint-jumps}\end{aligned}$$ Here $\gamma_r\ge\kappa_\gamma7^r/r>0$ once $r\ge7$.

For each of $$Q_r\in\left\{E^{I}_r,\ E^{J}_r,\ \Delta^{I}_r/\gamma_r,\qquad
                         \Delta^{J}_r/\gamma_r\right\},
 \label{eq:four-errors}$$ the natural two-scale maximum satisfies $$\liminf_{y\to\infty}\frac{1+\rho}{a}
 \max\{x^{2r}|Q_r(y)|,q^{2r}|Q_r(y+1)|\}\ge1.
 \label{eq:natural-profile}$$ If, in addition to [\[eq:linear-rank\]](#eq:linear-rank){reference-type="eqref" reference="eq:linear-rank"}, $r/x\to\lambda\in[0,\infty)$, then with $a_0=e^{-2\lambda h_*}$, $$\liminf_y\max\{x^{2r}|Q_r(y)|,q^{2r}|Q_r(y+1)|\}
 \ge\frac{a_0}{1+a_0}.
 \label{eq:lambda-profile}$$ Without assuming that $r/x$ converges, the right side may be replaced by $e^{-1200C}/2$. In particular, $r=o(x)$ gives the lower bound $1/2$. Finally, $$\frac{\max\{|Q_r(y)|,|Q_r(y+1)|\}}{P_{r+1}(y)}
 \longrightarrow\infty
 \qquad\text{for every $Q_r$ in \eqref{eq:four-errors}.}
 \label{eq:next-rank-divergence}$$

The optional hypothesis $r/x\to\lambda$ is used only for [\[eq:lambda-profile\]](#eq:lambda-profile){reference-type="eqref" reference="eq:lambda-profile"}. The jump identities, the natural profile, and the coarse $C$-bound allow $r/x$ to oscillate.

# Uniform edge and endpoint estimates

Maynard's unconditional Theorem 1.3, printed page 385 (PDF page 3), states $$\liminf_{n\to\infty}(p_{n+1}-p_n)\le600
 \label{eq:Maynard}$$ for consecutive primes [@Maynard2015]. Hence there are infinitely many consecutive gaps at most $600$. Only finitely many positive integer values can occur there, so one value $h_*\le600$ repeats infinitely often. This proves the extraction in [\[eq:fixed-edges\]](#eq:fixed-edges){reference-type="eqref" reference="eq:fixed-edges"}; no nonconsecutive prime-pair statement is substituted for it.

The strict endpoint gives the exact successor identity $$P_j(y)-P_j(y+1)=(q^2-1)^{-j}.
 \label{eq:successor}$$ Using the same rank $r$ at $x$ and $q$ in [\[eq:scalar-errors\]](#eq:scalar-errors){reference-type="eqref" reference="eq:scalar-errors"}, $$\begin{aligned}
 E^{I}_r(y)-E^{I}_r(y+1)
 &=\frac1{(q^2-1)^r}-\int_x^q\frac{t^{-2r}}{\log t}\,dt,
 \label{eq:I-edge}\\
 E^{J}_r(y)-E^{J}_r(y+1)
 &=\frac1{(q^2-1)^r}-\int_x^q
       \frac{dt}{(t^2-1)^r\log t}.
 \label{eq:J-edge}\end{aligned}$$ The atom becomes exactly $a$ after multiplication by $x^{2r}$. The two smooth terms obey $$\begin{aligned}
 0\le x^{2r}\int_x^q\frac{t^{-2r}}{\log t}\,dt
 &\le\frac{h_*}{\log x},
 \label{eq:I-smooth}\\
 0\le x^{2r}\int_x^q\frac{dt}{(t^2-1)^r\log t}
 &\le\frac{h_*}{\log x}(1-x^{-2})^{-r}=o(1).
 \label{eq:J-smooth}\end{aligned}$$ Indeed $r\le Cx$ makes $r\{-\log(1-x^{-2})\}=O_C(x^{-1})$. Equations [\[eq:I-edge\]](#eq:I-edge){reference-type="eqref" reference="eq:I-edge"}--[\[eq:J-smooth\]](#eq:J-smooth){reference-type="eqref" reference="eq:J-smooth"} prove [\[eq:scalar-jumps\]](#eq:scalar-jumps){reference-type="eqref" reference="eq:scalar-jumps"} uniformly in the declared rank regime.

The two edge factors are close but not interchangeable: $$\frac{\rho}{a}=(1-q^{-2})^r\longrightarrow1,
 \qquad
 \log a=-r\log\left(1+\frac{2h_*}{x}
                       +\frac{h_*^2-1}{x^2}\right).
 \label{eq:edge-factor-identities}$$ Thus $r/x\to\lambda$ implies $a,\rho\to e^{-2\lambda h_*}$. For the general linear regime, $\log(1+u)\le u$ gives $$\liminf a\ge e^{-2Ch_*}\ge e^{-1200C}.
 \label{eq:coarse-a}$$

The endpoint lift requires estimates uniform in $r$. They are recorded next in the form used in the proof. All bounds are elementary integer-tail or integral comparisons; their threshold $x_0(C)$ need not be effective here.

[\[lem:tails\]]{#lem:tails label="lem:tails"} Fix $C>0$. For $x\ge x_0(C)$, $r\ge7$, $r\le Cx$, and $1\le c\le7$, $$\begin{aligned}
 P_{r+1}(y)&\le\frac{4x^{-2r-1}}{2r+1},
 \label{eq:next-P-upper}\\
 \sum_{j>r}\frac{c^jP_j(y)}j
 &\le\frac{4c^{r+1}x^{-2r-1}}{(r+1)(2r+1)},
 \label{eq:P-integer-tail}\\
 \sum_{j>r}\frac{c^jI_{2j}(x)}j
 &\le\frac{2c^{r+1}x^{-2r-1}}
 {(r+1)(2r+1)\log x},
 \label{eq:I-integer-tail}\\
 0\le\sum_{j\ge r}\frac{c^j\{J_j(x)-I_{2j}(x)\}}j
 &\le\frac{4c^rx^{-2r-1}}{(2r+1)\log x}.
 \label{eq:JI-bridge}\end{aligned}$$ Also, if $H_c=\sum_{j<r}c^jP_j(y)/j$, then $$\|H\|_\infty\le\frac{14}{x}.
 \label{eq:head-bound}$$

Replace the odd primes beyond $x$ by the larger set of integers. If $S_P$ denotes the left side of [\[eq:P-integer-tail\]](#eq:P-integer-tail){reference-type="eqref" reference="eq:P-integer-tail"}, Tonelli and $1/j\le1/(r+1)$ give $$\begin{aligned}
 S_P
 &\le\frac{c^{r+1}}{r+1}\sum_{n>x}
 \frac{(n^2-1)^{-r-1}}{1-c/(n^2-1)} \notag\\
 &\le\frac{4c^{r+1}x^{-2r-1}}{(r+1)(2r+1)}.
 \label{eq:SP-payment}\end{aligned}$$ Indeed, the geometric denominator is at least $1/2$ eventually, the summand is decreasing, and $$\sum_{n>x}(n^2-1)^{-r-1}
 \le\int_x^\infty(t^2-1)^{-r-1}\,dt
 \le\frac{2x^{-2r-1}}{2r+1}.
 \label{eq:integer-payment}$$ The last factor $2$ follows from $(1-x^{-2})^{-r-1}\le2$ once $x\ge x_0(C)$. The same comparison without the geometric sum proves [\[eq:next-P-upper\]](#eq:next-P-upper){reference-type="eqref" reference="eq:next-P-upper"}. For the integral tail, $$\sum_{j>r}\frac{c^jI_{2j}(x)}j
 \le\frac{c^{r+1}}{r+1}\int_x^\infty
 \frac{t^{-2r-2}}{\log t\{1-c/t^2\}}\,dt
 \le\frac{2c^{r+1}x^{-2r-1}}
 {(r+1)(2r+1)\log x},
 \label{eq:SI-payment}$$ which proves [\[eq:I-integer-tail\]](#eq:I-integer-tail){reference-type="eqref" reference="eq:I-integer-tail"}.

For [\[eq:JI-bridge\]](#eq:JI-bridge){reference-type="eqref" reference="eq:JI-bridge"}, the mean-value inequality $$(1-u)^{-j}-1\le ju(1-u)^{-j-1}\qquad(0\le u<1)$$ cancels the coordinate divisor $j$. Summing the remaining geometric series under the integral yields $$\begin{aligned}
 \sum_{j\ge r}\frac{c^j\{J_j-I_{2j}\}}j
 &\le\int_x^\infty\frac{c^r\,dt}
 {(t^2-1)^{r+1}\{1-c/(t^2-1)\}\log t} \notag\\
 &\le\frac{4c^rx^{-2r-1}}{(2r+1)\log x},
 \label{eq:JI-payment}\end{aligned}$$ where the geometric denominator and $(1-x^{-2})^{-r-1}$ each cost at most $2$.

Finally, positivity permits extension of the head to all ranks, and the logarithmic series and an exact telescoping sum give $$\begin{aligned}
 H_c
 &\le\sum_{n>x}-\log\left(1-\frac{c}{n^2-1}\right)
 \le2c\sum_{n>x}\frac1{n^2-1} \notag\\
 &=c\left(\frac1x+\frac1{x+1}\right)\le\frac{14}{x}.
 \label{eq:H-payment}\end{aligned}$$ No prime number theorem estimate and no asymptotic formula for $P_r$ enter these comparisons.

The endpoint coefficient has enough growth to absorb all seven channels.

[\[lem:gamma\]]{#lem:gamma label="lem:gamma"} For every exact integer $r\ge7$, $$\gamma_r\ge\kappa_\gamma\frac{7^r}{r}>0.
 \label{eq:gamma-lower}$$

The exact outward intervals of RH-384 give, by directed rational cross multiplication, $$\frac{u_4}{u_3}>\frac23,
 \qquad \frac{u_6}{u_5}>\left(\frac45\right)^2,
 \qquad \frac{u_8}{u_7}>\left(\frac67\right)^6,
 \label{eq:ratio-locks}$$ and $u_3>u_4$, $u_5>u_6$, $u_7>u_8$. Hence the first two power differences and the memory term in [\[eq:gamma\]](#eq:gamma){reference-type="eqref" reference="eq:gamma"} are positive for $r\ge7$. The last ratio in [\[eq:ratio-locks\]](#eq:ratio-locks){reference-type="eqref" reference="eq:ratio-locks"} yields $$7^ru_8-6^ru_7\ge\frac17\,7^r\underline u_8.$$ Substitution into [\[eq:gamma\]](#eq:gamma){reference-type="eqref" reference="eq:gamma"} proves [\[eq:gamma-lower\]](#eq:gamma-lower){reference-type="eqref" reference="eq:gamma-lower"}. The endpoint formula is inherited from RH-383, while the exact directed intervals are those of RH-384 [@RH383; @RH384].

Put $$\begin{aligned}
 D^I_c(y)&=(\Phi^{P}_c-\Phi^{I,<r}_c)(y),&
 D^J_c(y)&=(\Phi^{P}_c-\Phi^{J,<r}_c)(y).\end{aligned}$$ The rank-$r$ term in [\[eq:successor\]](#eq:successor){reference-type="eqref" reference="eq:successor"}, the smooth bounds [\[eq:I-smooth\]](#eq:I-smooth){reference-type="eqref" reference="eq:I-smooth"}--[\[eq:J-smooth\]](#eq:J-smooth){reference-type="eqref" reference="eq:J-smooth"}, and Lemma [\[lem:tails\]](#lem:tails){reference-type="ref" reference="lem:tails"} give, for $S\in\{I,J\}$, $$x^{2r}\{D^S(y)-D^S(y+1)\}=a v_r+\eta^S,
 \qquad
 \frac{r}{7^r}\|\eta^S\|_\infty\longrightarrow0.
 \label{eq:coordinate-jump}$$ The $J$ statement uses [\[eq:JI-bridge\]](#eq:JI-bridge){reference-type="eqref" reference="eq:JI-bridge"}; it is not inferred from a fixed-rank limit.

For completeness, the Taylor step can be kept quantitative. On the eventual cube $[0,1/2]^7$, the frozen endpoint ledger gives $$\sum_{i,j=1}^7|\partial_{ij}F(z)|<224.
 \label{eq:Hessian}$$ If $A$ is the actual tail from rank $r$, $B$ is either smooth tail, and $H$ is their common exact head, then $$\begin{aligned}
 |F(H+A)-F(H+B)-\nabla F(0)\mathbin{\cdot}(A-B)|
 &\le224\|H\|_\infty\|A-B\|_\infty \notag\\
 &\quad+112(\|A\|_\infty^2+\|B\|_\infty^2).
 \label{eq:Taylor}\end{aligned}$$ Direct versions of Lemma [\[lem:tails\]](#lem:tails){reference-type="ref" reference="lem:tails"} give $$\begin{aligned}
 \|A\|_\infty&\le
 \frac{4\,7^rx^{1-2r}}{r(2r-1)},
 &\|B\|_\infty&\le
 \frac{2\,7^rx^{1-2r}}{r(2r-1)\log x}
 \label{eq:tail-norms}\end{aligned}$$ for the $I$ tail, with [\[eq:JI-bridge\]](#eq:JI-bridge){reference-type="eqref" reference="eq:JI-bridge"} handling the $J$ tail. After division by $\gamma_rx^{-2r}$, the cross and square remainders in [\[eq:Taylor\]](#eq:Taylor){reference-type="eqref" reference="eq:Taylor"} are at most $$\frac{18816}{\kappa_\gamma(2r-1)},
 \qquad
 \frac{2240}{\kappa_\gamma}
 \frac{7^rx^{2-2r}}{r(2r-1)^2},
 \label{eq:Taylor-remainders}$$ respectively. Both tend to zero. Apply [\[eq:Taylor\]](#eq:Taylor){reference-type="eqref" reference="eq:Taylor"} separately at $x$ and $q$, subtract, and combine [\[eq:coordinate-jump\]](#eq:coordinate-jump){reference-type="eqref" reference="eq:coordinate-jump"} with $\nabla F(0)\cdot v_r=\gamma_r$. This proves [\[eq:endpoint-jumps\]](#eq:endpoint-jumps){reference-type="eqref" reference="eq:endpoint-jumps"}.

# Two-endpoint profile and next-rank separation

The retention constant is pairwise because an edge jump alone does not select one endpoint. Let $Q_r$ be any error in [\[eq:four-errors\]](#eq:four-errors){reference-type="eqref" reference="eq:four-errors"} and set $$L_y=x^{2r}|Q_r(y)|,\qquad
 R_y=q^{2r}|Q_r(y+1)|.
 \label{eq:L-R}$$ The corresponding jump formula and the triangle inequality give $$a+o(1)\le L_y+\rho R_y
 \le(1+\rho)\max\{L_y,R_y\}.
 \label{eq:pair-inequality}$$ Because [\[eq:coarse-a\]](#eq:coarse-a){reference-type="eqref" reference="eq:coarse-a"} keeps $a$ away from zero, division by $a$ proves [\[eq:natural-profile\]](#eq:natural-profile){reference-type="eqref" reference="eq:natural-profile"}. If $r/x\to\lambda$, then $a,\rho\to a_0=e^{-2\lambda h_*}$, which proves [\[eq:lambda-profile\]](#eq:lambda-profile){reference-type="eqref" reference="eq:lambda-profile"}. In the general linear regime, $\rho<1$ and [\[eq:coarse-a\]](#eq:coarse-a){reference-type="eqref" reference="eq:coarse-a"} give $e^{-1200C}/2$. Taking $\lambda=0$ gives the sublinear constant $1/2$.

It remains to compare with the next prime-tail rank. The coarse pair bound and $q/x=1+h_*/x$ show that, for some constant depending only on $C$, at least one raw endpoint error is bounded below by a positive multiple of $q^{-2r}$. Lemma [\[lem:tails\]](#lem:tails){reference-type="ref" reference="lem:tails"} gives $$P_{r+1}(y)\le\frac{4x^{-2r-1}}{2r+1}.$$ Moreover $(x/q)^{2r}=\rho$ has the positive lower limit bound inherited from [\[eq:coarse-a\]](#eq:coarse-a){reference-type="eqref" reference="eq:coarse-a"}. The quotient is therefore bounded below by a positive multiple of $x(2r+1)$ and tends to infinity. This proves [\[eq:next-rank-divergence\]](#eq:next-rank-divergence){reference-type="eqref" reference="eq:next-rank-divergence"}. The argument uses a one-sided integer upper bound for $P_{r+1}$, not $P_{r+1}\sim K_{r+1}$.

# Relation to prior work and scope

The exact endpoint normal form and its gradient are supplied by RH-383. RH-384 supplies the directed $u_m$ intervals and establishes fixed-rank prime-tail scale separation. Its fixed-rank asymptotic is background only: it is not used when $r$ grows linearly with $x$. RH-388 proved the rank-one bounded-gap/Taylor prototype, and RH-390 extended endpoint positivity to all fixed ranks while proving a growing-rank sufficiency filtration and fixed-rank necessity [@RH383; @RH384; @RH388; @RH390]. The present theorem is the same-rank pair obstruction through the full linear scale $r=O(x)$, including the exact finite-slope profile. It is not obtained by inserting a moving rank into a fixed-rank asymptotic.

The quantifiers are part of the claim. The rank is identical at the two consecutive-prime endpoints and tends to infinity. Necessity is for a pair maximum in the frozen $P/J/I$ hierarchy. No arbitrary single-vertex rank schedule, arbitrary surrogate, or regime $r/x\to\infty$ is covered. The theorem has no dependency on RH-389, TPC-137, or the Tao active-log source chain. It makes no claim about ordinary Cesàro limits, growing clocks, complex channels, operators, traces, zeta zeros, or the Riemann hypothesis. Gates A--E remain false.

# Executable artifact and source closure

The exact artifact has epistemic role `finite_exact_algebra_not_analytic_proof`. Its 60 semantic rows comprise 10 definition, 12 edge, 12 coefficient, 12 vector, eight profile, and six contract rows. The canonical certificate has 10,062 bytes and SHA-256

cc2874435e62205a3e969e841d80d37243d95826855bd242f0eff3478dccf367.

Twenty-four genuine semantic mutations are rejected by exact leaf seals and an independent field-level verifier whose false mode calls no row or certificate builder. The stored result and closed Draft 2020--12 schema have SHA-256 digests

  -------------------------------------------------------------------
  023aa55c4a4e3795994eed866cc9d1412aef90bc0df9b27831f3718c069c1046
  f5fd98019eefdf600432ca59c6546a6c6d5c7c832a4f8da0603512d20ee40f54.
  -------------------------------------------------------------------

These checks reproduce finite identities, exact memberships, source roles, and mutation rejection. They do not establish Maynard's theorem, the integer and integral estimates, Taylor's theorem, or any asymptotic limit.

The proof-minimal closure freezes 97 Git objects from release

a3aa5977e9b3338e4c3035c6c42b60d50bc3ac3b,

in groups of sizes $87$, $8$, and $2$. Their ordered group digests are

  -------------------------------------------------------------------
  098fdd54388471145bb2ffa8647c23b2f07e995a34e247c4e9a60ae45cd2435d
  e9a95e0c52d6063b56a0fa19479efbf419ba91f486f1697a4128c238d3312c93
  335f7b279a604eaf2259f826770d066173eab66f0fbfcd3a171770ee5ec4c460.
  -------------------------------------------------------------------

The ordered digest of all 97 Git sources is

1250b73311e3fef4b2e7139db887043164f3f20a527cd45c0d5f2fad7f69bd96.

Adding the Johnston--Yang and Maynard logical locks gives 99 logical sources with ordered digest

760d1e8babf789588a4238e179193f03319de04d276d7180dd4c85b6359bccbb.

Among the two remote inputs, Maynard's Theorem 1.3 is the only analytic theorem invoked here. The Johnston--Yang object is inherited provenance only and is not invoked for a linear-rank prime-tail asymptotic [@JohnstonYang2023]. No new remote source was added. External PDFs and source archives are not vendored, network verification is disabled by default, and both remote locks conservatively record `redistributable_in_release=false`.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

The proof, exact certificate compiler, tests, closed schema, and two compact source-lock records accompany this paper. External source payloads are not redistributed.

#### Author contributions.

The author is responsible for conceptualization, proof, software, validation, writing, and release auditing.

#### Funding.

No external funding was received.

#### Competing interests.

The author declares no competing interests.

#### Ethics.

No human participants, animals, personal data, or clinical interventions are involved.

#### AI assistance.

AI-assisted tools were used for exact symbolic-interface enumeration, adversarial testing, manuscript drafting, and release auditing. All mathematical claims, citations, source locks, and final text remain under author responsibility.
