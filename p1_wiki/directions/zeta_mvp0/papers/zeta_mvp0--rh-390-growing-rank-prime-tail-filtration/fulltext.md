---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-390-growing-rank-prime-tail-filtration"
canonical_tex: "zeta_mvp0/papers/RH-390-growing-rank-prime-tail-filtration/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-390-growing-rank-prime-tail-filtration/main.pdf"
source_sha256: "fff2a95195b9c24fef209d1597d0d306833587a792e5952a9b1d43825391d7b4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Growing-Rank Prime-Tail Filtration and Fixed-Rank Necessity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-390-growing-rank-prime-tail-filtration>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-390-growing-rank-prime-tail-filtration/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-390-growing-rank-prime-tail-filtration/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-390-growing-rank-prime-tail-filtration/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-390-growing-rank-prime-tail-filtration/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $x=p_y$, $L=\log x\ge512$, and fix $0<\delta<1$. For each threshold $s$ in the moving window below, we retain exactly the strict prime tails $P_r(y)$ with $r<s$, where $$S_y=\left\lfloor\frac{(1-\delta)\log L}{\log7}\right\rfloor$$ and replace every rank $r\ge s$ by a $K$-term factorial Laplace kernel. For every exact integer $2\le s\le S_y$ and every $1\le K\le\lfloor(2s-1)L\rfloor$, a single normalized ledger bounds the source, power-kernel, and factorial errors. The exact endpoint map then gives $$\lim_{y\to\infty}
   \max_{2\le s\le S_y}\;
   \max_{1\le K\le\lfloor(2s-1)L\rfloor}
   \frac{|\operatorname{Gap}_{P}-\operatorname{Gap}_{s,K}|}{P_s(y)}=0.$$ This is a simultaneous theorem in a growing rank and the complete integer factorial window, not a collection of fixed-rank limits.

  The retention threshold is sharp at every fixed rank inside the frozen $P/J/I$ hierarchy. An all-rank endpoint coefficient $\gamma_r$ is strictly positive. Maynard's bounded-consecutive-gap theorem then shows that, for fixed $s\ge2$ and $r=s-1$, smoothing the missing rank produces endpoint error with limsup at least $\gamma_r/2$ after normalization by $p_y^{2r}\pi^2$; its ratio to $P_s(y)$ is unbounded. No growing-rank necessity, convergent factorial series, or universal obstruction for arbitrary surrogates is asserted. A 72-row exact certificate reproduces the algebraic interfaces but is not an analytic proof.
author:
- RH research program
bibliography:
- references.bib
date: 'August 9, 2026'
title: |
  Growing-Rank Prime-Tail Filtration\
  and Fixed-Rank Necessity
```

## Markdown 正文

**Keywords:** strict prime tails; growing-rank filtration; factorial Laplace remainder; bounded consecutive prime gaps; square-clock endpoint.

# Prime tails, endpoint, and statements

Let $3=p_1<p_2<\cdots$ be the odd primes and put $$x=p_y,\qquad L=\log x,\qquad
 V=L^{3/5}(\log L)^{-1/5},\qquad
 \varepsilon_x=\frac{27}{1000}L^{1801/1000}
 e^{-(1853/10000)V}.
 \label{eq:domain}$$ Johnston and Yang's Theorem 1.4, equation (1.8), printed page 2, gives $$|\vartheta(t)-t|\le t\varepsilon_t\qquad(t\ge23),
 \label{eq:JY}$$ and RH-386 proves that this envelope decreases once $\log t\ge512$ [@JohnstonYang2023; @RH386]. Thus $\varepsilon_t\le\varepsilon_x$ for $t\ge x$ in our domain. The Johnston--Yang corollary and its tabulated fallback constants are not used here.

For every exact integer $r\ge1$, define $$P_r(y)=\sum_{p>x}(p^2-1)^{-r},\quad
 J_r(x)=\int_x^\infty\frac{dt}{(t^2-1)^r\log t},\quad
 I_{2r}(x)=\int_x^\infty\frac{t^{-2r}}{\log t}\,dt,
 \label{eq:tails}$$ and, for $c\in\{1,\ldots,7\}$, $$\Phi^{P}_c=\sum_{r\ge1}\frac{c^rP_r}{r}.
 \label{eq:PhiP}$$ All prime tails are strict: the endpoint prime $x=p_y$ is excluded.

For $2\le m\le8$, set $$u_m=\prod_{p\ \mathrm{odd}}
 \frac{1-m/p^2}{1-1/p^2},\qquad
 (\alpha_m)=(-2,2,-2,2,-2,2,-2),\qquad
 (\beta_m)=(1,-2,2,-2,2,-2,2).
 \label{eq:u-alpha-beta}$$ For $z=(z_1,\ldots,z_7)$ write $$Z_m(z)=u_me^{z_{m-1}},\qquad
 C(Z)=1+\sum_{m=2}^8\alpha_mZ_m,\qquad
 W(Z)=\sum_{m=2}^8\beta_mZ_m,$$ and define the exact endpoint map $$F(z)=2\{C(u)-C(Z(z))\}
 -4W(Z(z))(1-e^{-z_1}).
 \label{eq:F}$$ The normal form of RH-383 gives, with $q_y=4\prod_{i\le y}p_i^2$, $$\operatorname{Gap}_{P}:=B_{\infty}-G(q_y)=\frac{F(\Phi^{P})}{\pi^2}.
 \label{eq:actual-gap}$$ Here and below an undecorated coordinate symbol denotes its seven-vector [@RH383].

For $r\ge1$ and $K\ge1$, put $$K_r=\frac{x^{1-2r}}{(2r-1)L},\qquad
 a_r=\frac1{(2r-1)L},\qquad
 S_K(a)=\sum_{j=0}^{K-1}(-1)^j j!a^j.
 \label{eq:factorial-defs}$$ For exact integers $s\ge2$ and $K\ge1$, define the retained coordinate $$\Psi_{c;s,K}
 =\sum_{1\le r<s}\frac{c^rP_r}{r}
 +\sum_{r\ge s}\frac{c^rK_rS_K(a_r)}r,\qquad
 \operatorname{Gap}_{s,K}=\frac{F((\Psi_{c;s,K})_{c=1}^7)}{\pi^2}.
 \label{eq:Psi-gap}$$

The three safe denominator factors used throughout are $$A_{s,c}=\frac1{(1-x^{-2})^s\{1-c/(x^2-1)\}},\quad
 B_{s,c}=\frac1{(1-x^{-2})^{s+1}\{1-c/(x^2-1)\}},\quad
 C_c=\frac1{1-c/x^2}.
 \label{eq:ABC}$$

[\[thm:finite-master\]]{#thm:finite-master label="thm:finite-master"} Let $L\ge512$, let $s\ge2$ be an exact integer, let $c\in\{1,\ldots,7\}$, and let $1\le K\le\lfloor(2s-1)L\rfloor$ be an exact integer. Then $\Phi^{P}$ and $(\Psi_{c;s,K})_{c=1}^7$ lie in $[0,1/2]^7$, and $$\begin{aligned}
 \frac{|\Phi^{P}_c-\Psi_{c;s,K}|}{K_s}
 &\le c^s\left\{
 \left(4-\frac1s\right)A_{s,c}\varepsilon_x
 +\frac{2s-1}{2s+1}\frac{B_{s,c}}{x^2}
 +\frac{C_cK!}{s\{(2s-1)L\}^K}
 \right\}.
 \label{eq:normalized-master}\end{aligned}$$ Consequently, $$\begin{aligned}
 \pi^2|\operatorname{Gap}_{P}-\operatorname{Gap}_{s,K}|
 &\le126K_s\max_{1\le c\le7}c^s\left\{
 \left(4-\frac1s\right)A_{s,c}\varepsilon_x
 +\frac{2s-1}{2s+1}\frac{B_{s,c}}{x^2}
 +\frac{C_cK!}{s\{(2s-1)L\}^K}
 \right\}.
 \label{eq:endpoint-master}\end{aligned}$$

[\[thm:growing\]]{#thm:growing label="thm:growing"} Fix $0<\delta<1$ and set $$S_y=\left\lfloor\frac{(1-\delta)\log L}{\log7}\right\rfloor.
 \label{eq:Sy}$$ Then $S_y\ge2$ eventually and $$\boxed{\lim_{y\to\infty}
 \max_{2\le s\le S_y}\;
 \max_{1\le K\le\lfloor(2s-1)L\rfloor}
 \frac{|\operatorname{Gap}_{P}-\operatorname{Gap}_{s,K}|}{P_s(y)}=0.}
 \label{eq:growing-conclusion}$$ Both maxima are over exact integers.

For the converse, define, for each fixed exact integer $r\ge1$, $$\begin{aligned}
 \operatorname{Gap}_{I,<r}&=\frac1{\pi^2}F\left(
 \left(\sum_{j<r}\frac{c^jP_j}{j}
 +\sum_{j\ge r}\frac{c^jI_{2j}}j\right)_{c=1}^7\right),
 \label{eq:GapI-def}\\
 \operatorname{Gap}_{J,<r}&=\frac1{\pi^2}F\left(
 \left(\sum_{j<r}\frac{c^jP_j}{j}
 +\sum_{j\ge r}\frac{c^jJ_j}j\right)_{c=1}^7\right).
 \label{eq:GapJ-def}\end{aligned}$$

[\[thm:necessity\]]{#thm:necessity label="thm:necessity"} Fix an exact integer $s\ge2$ and put $r=s-1$. Within the declared $P/J/I$ hierarchy, $$\begin{aligned}
 \limsup_{y\to\infty}p_y^{2r}|P_r(y)-I_{2r}(p_y)|&\ge\frac12,
 \label{eq:scalar-necessity}\\
 \limsup_{y\to\infty}p_y^{2r}\pi^2|\operatorname{Gap}_{P}-\operatorname{Gap}_{I,<r}|
 &\ge\frac{\gamma_r}{2},
 \label{eq:I-necessity}\\
 \limsup_{y\to\infty}p_y^{2r}\pi^2|\operatorname{Gap}_{P}-\operatorname{Gap}_{J,<r}|
 &\ge\frac{\gamma_r}{2},
 \label{eq:J-necessity}\end{aligned}$$ where $\gamma_r>0$ is given explicitly in Lemma [\[lem:gamma\]](#lem:gamma){reference-type="ref" reference="lem:gamma"}. Hence $$\limsup_y\frac{|\operatorname{Gap}_{P}-\operatorname{Gap}_{I,<r}|}{P_s(y)}
 =\limsup_y\frac{|\operatorname{Gap}_{P}-\operatorname{Gap}_{J,<r}|}{P_s(y)}=+\infty.
 \label{eq:necessity-ratios}$$ The theorem concerns fixed $s$ only and only these two smooth tails.

# One strict-endpoint lemma for the three transfers

Write $E(t)=\vartheta(t)-t$ and $h_r(t)=(t^2-1)^{-r}/\log t$. The strict endpoint $p>x$ gives the two identities $$\begin{aligned}
 P_r-J_r&=-E(x)h_r(x)-\int_x^\infty E(t)h_r'(t)\,dt,
 \label{eq:strict-stieltjes}\\
 P_r(y)&=(p_{y+1}^2-1)^{-r}+P_r(y+1).
 \label{eq:strict-successor}\end{aligned}$$ In particular, $$|P_r-J_r|\le\varepsilon_x\{2xh_r(x)+J_r\}.
 \label{eq:strict-bound}$$ The boundary term and the second $xh_r(x)$ arising after integration by parts are separate contributions.

For $0\le z<1$, let $$R_s(z)=\sum_{r\ge s}\frac{z^r}{r}.
 \label{eq:Rs}$$ Then $$0\le R_s(z)\le\frac{z^s}{s(1-z)},\qquad
 R_s'(z)=\frac{z^{s-1}}{1-z}.
 \label{eq:Rs-bounds}$$

[\[lem:unified-transfer\]]{#lem:unified-transfer label="lem:unified-transfer"} Under the hypotheses of Theorem [\[thm:finite-master\]](#thm:finite-master){reference-type="ref" reference="thm:finite-master"}, $$\begin{aligned}
 \frac1{K_s}\left|\sum_{r\ge s}\frac{c^r(P_r-J_r)}r\right|
 &\le c^s\left(4-\frac1s\right)A_{s,c}\varepsilon_x,
 \label{eq:source-transfer}\\
 \frac1{K_s}\sum_{r\ge s}\frac{c^r(J_r-I_{2r})}r
 &\le c^s\frac{2s-1}{2s+1}\frac{B_{s,c}}{x^2},
 \label{eq:power-transfer}\\
 \frac1{K_s}\left|\sum_{r\ge s}
 \frac{c^r\{I_{2r}-K_rS_K(a_r)\}}r\right|
 &\le c^s\frac{C_cK!}{s\{(2s-1)L\}^K}.
 \label{eq:factorial-transfer}\end{aligned}$$ All three sums extend over every integer $r\ge s$.

Absolute convergence permits Tonelli on the nonnegative majorants. Sum [\[eq:strict-bound\]](#eq:strict-bound){reference-type="eqref" reference="eq:strict-bound"} with weights $c^r/r$. At $t=x$, [\[eq:Rs-bounds\]](#eq:Rs-bounds){reference-type="eqref" reference="eq:Rs-bounds"} makes the boundary contribution, after division by $K_s$, $$c^s\frac{2(2s-1)}sA_{s,c}\varepsilon_x.$$ For the integral contribution, freeze both decreasing denominators at $x$, dominate $(t^2-1)^{-s}$ by $(1-x^{-2})^{-s}t^{-2s}$, and use $\int_x^\infty t^{-2s}dt/\log t\le K_s$. This contributes $c^sA_{s,c}\varepsilon_x/s$. The sum of the two coefficients is $4-1/s$, proving [\[eq:source-transfer\]](#eq:source-transfer){reference-type="eqref" reference="eq:source-transfer"}.

For the power-kernel comparison use, for $0\le u<1$, $$(1-u)^{-r}-1\le ru(1-u)^{-r-1}.
 \label{eq:power-mean}$$ The factor $r$ cancels the divisor $r$ in the coordinate series. Summing the remaining geometric series and integrating $t^{-2s-2}$ gives $$\sum_{r\ge s}\frac{c^r(J_r-I_{2r})}r
 \le c^sB_{s,c}\frac{x^{-2s-1}}{(2s+1)L}.$$ Division by $K_s$ proves [\[eq:power-transfer\]](#eq:power-transfer){reference-type="eqref" reference="eq:power-transfer"}; this is where the exponent $s+1$ in $B_{s,c}$ is required.

Finally, the substitution $t=xe^u$, followed by $v=(2r-1)u$, yields $$I_{2r}=K_rG(a_r),\qquad
 G(a)=\int_0^\infty\frac{e^{-v}}{1+av}\,dv.
 \label{eq:Laplace}$$ The finite geometric identity gives the exact remainder $$G(a)-S_K(a)=(-a)^K\int_0^\infty
 \frac{e^{-v}v^K}{1+av}\,dv.
 \label{eq:factorial-remainder}$$ It has sign $(-1)^K$ and absolute value at most $a^KK!$. Since $K_r/K_s\le x^{-2(r-s)}$, $(2r-1)L\ge(2s-1)L$, and $1/r\le1/s$, summing in $r$ leaves the geometric factor $(1-c/x^2)^{-1}=C_c$. This proves [\[eq:factorial-transfer\]](#eq:factorial-transfer){reference-type="eqref" reference="eq:factorial-transfer"}.

# Full factorial window, cube, and the growing rank

Put $D=(2s-1)L$, a positive real number, and $b_K=K!/D^K$. For exact integers $1\le k<\lfloor D\rfloor$, $$\frac{b_{k+1}}{b_k}=\frac{k+1}{D}\le1.
 \label{eq:b-recurrence}$$ Therefore every exact integer $1\le K\le\lfloor D\rfloor$ satisfies $$\frac{K!}{D^K}\le\frac1D.
 \label{eq:full-window}$$ The same window controls the sign of every $S_K(a_r)$ with $r\ge s$: whenever a consecutive ratio occurs, $$(j+1)a_r<1,\qquad
 j+1\le K-1<D\le(2r-1)L.$$ Pairing decreasing alternating terms in the finite sum gives $$0<S_K(a_r)\le1
 \qquad(r\ge s,\ 1\le K\le\lfloor D\rfloor).
 \label{eq:alternating-positive}$$ This is a finite identity and monotonicity argument, not a convergence claim for the formal factorial series.

We also need a common real cube for the endpoint mean-value theorem. The bridge $$x=e^L>2^{512}>256
 \label{eq:cube-bridge}$$ and $-\log(1-z)\le z/(1-z)$ imply $$\begin{aligned}
 \Phi^{P}_c
 &\le\frac{c}{1-c/(x^2-1)}
 \frac12\left(\frac1x+\frac1{x+1}\right),
 \label{eq:prime-cube}\\
 0\le\sum_{r\ge s}\frac{c^rK_rS_K(a_r)}r
 &\le\frac{c^2}{6x^3L(1-c/x^2)}.
 \label{eq:factorial-cube}\end{aligned}$$ At $x=256$, $L=512$, and $c=7$, the sum of the two right sides is less than $1/2$. Hence $\Phi^{P}$ and every admissible $\Psi_{s,K}$ lie in $[0,1/2]^7$.

The factors in [\[eq:u-alpha-beta\]](#eq:u-alpha-beta){reference-type="eqref" reference="eq:u-alpha-beta"} have summable deficits, so $u_m>0$; their $p=3$ factor and the remaining factors give $u_m\le(9-m)/8$. Consequently $$\sum_{m=2}^8|\alpha_m|u_m\le7,\qquad
 \sum_{m=2}^8|\beta_m|u_m\le\frac{49}{8}.
 \label{eq:endpoint-arrays}$$ On the cube, the derivative of the $C$ term, the derivative falling on $W$, and the derivative falling on $1-e^{-z_1}$ have coefficients $2,4,4$. Since $e^{1/2}<2$, $$\|\nabla F(z)\|_1
 \le e^{1/2}\left(2\cdot7+(4+4)\frac{49}{8}\right)<126.
 \label{eq:gradient126}$$ This is the dual $\ell^1$ norm for an $\ell^\infty$ input. Combining Lemma [\[lem:unified-transfer\]](#lem:unified-transfer){reference-type="ref" reference="lem:unified-transfer"}, the triangle inequality, the convex cube, and [\[eq:gradient126\]](#eq:gradient126){reference-type="eqref" reference="eq:gradient126"} proves Theorem [\[thm:finite-master\]](#thm:finite-master){reference-type="ref" reference="thm:finite-master"}.

The rank window is eventually nonempty. For $2\le s\le S_y$, $$7^{S_y}\le L^{1-\delta},\qquad
 \log S_y=o(V),\qquad 7S_y\varepsilon_x\le\frac12
 \quad\hbox{eventually}.
 \label{eq:growing-bridges}$$ The last two facts place the complete rank window inside the growing-order prime-tail transfer of RH-386. In particular, $$\frac{P_s(y)}{K_s}\longrightarrow1
 \quad\hbox{uniformly for }2\le s\le S_y.
 \label{eq:uniform-Ps}$$ No effective least $y$ is claimed.

It remains to make the three denominator bounds uniform in $s$. In the stated domain $s\le S_y\le\log L/\log7<L$, so $s+1\le L+1<e^L=x$. Bernoulli's inequality gives $$(1-x^{-2})^{s+1}\ge1-\frac{s+1}{x^2}
 >1-\frac1{256}=\frac{255}{256}.
 \label{eq:Bernoulli-floor}$$ Also $$1-\frac{c}{x^2-1}\ge\frac{65528}{65535},\qquad
 1-\frac{c}{x^2}\ge\frac{65529}{65536}.$$ Thus $A_{s,c}<4$, $B_{s,c}<4$, and $C_c<2$. After taking the maximum over $c\le7$, the three normalized terms in [\[eq:endpoint-master\]](#eq:endpoint-master){reference-type="eqref" reference="eq:endpoint-master"} tend uniformly to zero because $$\begin{aligned}
 7^{S_y}\varepsilon_x
 &\le\frac{27}{1000}L^{2801/1000-\delta}
 e^{-(1853/10000)V}\longrightarrow0,
 \label{eq:source-limit}\\
 \frac{4\,7^{S_y}}{x^2}
 &\le\frac{4L^{1-\delta}}{x^2}\longrightarrow0,
 \label{eq:power-limit}\\
 \frac{2\,7^{S_y}}{s(2s-1)L}
 &\le\frac13L^{-\delta}\longrightarrow0.
 \label{eq:factorial-limit}\end{aligned}$$ Here [\[eq:factorial-limit\]](#eq:factorial-limit){reference-type="eqref" reference="eq:factorial-limit"} uses the whole-window induction [\[eq:full-window\]](#eq:full-window){reference-type="eqref" reference="eq:full-window"}, not finitely many $K$ fixtures. Divide [\[eq:endpoint-master\]](#eq:endpoint-master){reference-type="eqref" reference="eq:endpoint-master"} by [\[eq:uniform-Ps\]](#eq:uniform-Ps){reference-type="eqref" reference="eq:uniform-Ps"} to obtain [\[eq:growing-conclusion\]](#eq:growing-conclusion){reference-type="eqref" reference="eq:growing-conclusion"}.

The base prime-square scale and positivity framework originates in RH-381; RH-384 identifies the fixed-rank scale $P_s\sim K_s$; RH-386 supplies the uniform growing-order transfer; and RH-387 supplies the all-order Tonelli and endpoint-Lipschitz interfaces [@RH381; @RH384; @RH386; @RH387]. The simultaneous growing-$s$ and full-$K$ filtration above is not obtained by taking a maximum of separate fixed-rank statements.

# A positive endpoint coefficient at every rank

For $r\ge1$, let $$v_r=\left(\frac{c^r}{r}\right)_{c=1}^7,
 \qquad \gamma_r=\nabla F(0)\mathbin{\cdot}v_r.
 \label{eq:vr-gamma}$$

[\[lem:gamma\]]{#lem:gamma label="lem:gamma"} For every exact integer $r\ge1$, $$\begin{aligned}
 \gamma_r=\frac4r\{&3^ru_4-2^ru_3+5^ru_6-4^ru_5
 +7^ru_8-6^ru_7\notag\\
 &+2(u_3-u_4+u_5-u_6+u_7-u_8)\}>0.
 \label{eq:gamma-formula}\end{aligned}$$

Differentiating [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"} at the origin gives the contribution $u_m\{-2\alpha_m(m-1)^r-4\beta_m\}/r$. The $m=2$ contribution cancels exactly because $-2\alpha_2-4\beta_2=0$; grouping the remaining three adjacent pairs gives [\[eq:gamma-formula\]](#eq:gamma-formula){reference-type="eqref" reference="eq:gamma-formula"}.

The exact outward rational intervals certified in RH-384 give the following strict lower bounds for $r=1,\ldots,5$:

   $r$   certified lower bound for $\gamma_r$
  ----- --------------------------------------
    1            $0.939359431238345$
    2            $1.546347671671049$
    3            $8.858054025485302$
    4            $54.027501667623385$
    5           $338.554565449603094$

The displayed decimals are downward truncations of exact rational lower endpoints, not floating-point evidence.

The same interval record gives, by exact cross multiplication, $$\frac{u_4}{u_3}>\frac23,\qquad
 \frac{u_6}{u_5}>\left(\frac45\right)^2,\qquad
 \frac{u_8}{u_7}>\left(\frac67\right)^6,
 \label{eq:ratio-bridges}$$ and $u_3>u_4$, $u_5>u_6$, $u_7>u_8$. Therefore the three power differences in [\[eq:gamma-formula\]](#eq:gamma-formula){reference-type="eqref" reference="eq:gamma-formula"} are positive for, respectively, $r\ge1$, $r\ge2$, and $r\ge6$, while the memory-difference sum is positive. Hence $\gamma_r>0$ for $r\ge6$; the five interval rows close the remaining ranks. The formula comes from RH-383's endpoint compiler, but the bridge from the finite interval record to every rank is new here [@RH383; @RH384].

# Bounded gaps and fixed-rank necessity

Maynard's unconditional Theorem 1.3, printed page 385 (PDF page 3), states $$\liminf_{n\to\infty}(p_{n+1}-p_n)\le600
 \label{eq:Maynard}$$ [@Maynard2015]. Because prime gaps are integers, this supplies infinitely many consecutive pairs $x=p_y$, $q=p_{y+1}=x+h$ with $h\le600$: otherwise all sufficiently late gaps would be at least $601$.

Fix $r\ge1$ and set $E_{r,y}=P_r(y)-I_{2r}(p_y)$. The strict successor identity [\[eq:strict-successor\]](#eq:strict-successor){reference-type="eqref" reference="eq:strict-successor"} gives $$E_{r,y}-E_{r,y+1}
 =\frac1{(q^2-1)^r}-\int_x^q\frac{t^{-2r}}{\log t}\,dt.
 \label{eq:scalar-jump}$$ Along the bounded gaps, $q/x\to1$ and $$\frac{x^{2r}}{(q^2-1)^r}\longrightarrow1,\qquad
 0\le x^{2r}\int_x^q\frac{t^{-2r}}{\log t}\,dt
 \le\frac{600}{\log x}\longrightarrow0.
 \label{eq:jump-limits}$$ The triangle inequality at the two endpoints, together with $q/x\to1$, proves [\[eq:scalar-necessity\]](#eq:scalar-necessity){reference-type="eqref" reference="eq:scalar-necessity"}.

To lift this jump, fix $r$ and define the common exact head and two tails in channel $c$ by $$H_c=\sum_{j<r}\frac{c^jP_j}{j},\qquad
 A_c=\sum_{j\ge r}\frac{c^jP_j}{j},\qquad
 B_c=\sum_{j\ge r}\frac{c^jI_{2j}}j.
 \label{eq:common-head}$$ Exact successors and Tonelli show that, along the same bounded gaps, $$x^{2r}\{(A-B)_y-(A-B)_{y+1}\}\longrightarrow v_r.
 \label{eq:vector-jump}$$ Indeed the $j=r$ prime atom tends to $c^r/r$, its smooth interval term vanishes as in [\[eq:jump-limits\]](#eq:jump-limits){reference-type="eqref" reference="eq:jump-limits"}, and every higher rank is $o(x^{-2r})$.

The endpoint Hessian ledger on $[0,1/2]^7$ is $$\sum_{i,j}|\partial_{ij}F(z)|<224.
 \label{eq:Hessian224}$$ It follows from the same endpoint arrays as [\[eq:gradient126\]](#eq:gradient126){reference-type="eqref" reference="eq:gradient126"}: the $C$ term and the Hessian, two cross derivatives, and loss Hessian in the $W(1-e^{-z_1})$ term have pre-exponential coefficients $2,4,8,4$, respectively. The resulting two-point Taylor estimate is $$\begin{aligned}
 |F(H+A)-F(H+B)-\nabla F(0)\mathbin{\cdot}(A-B)|
 &\le224\|H\|_\infty\|A-B\|_\infty\notag\\
 &\quad+112(\|A\|_\infty^2+\|B\|_\infty^2).
 \label{eq:two-point-Taylor}\end{aligned}$$ The direct prime-tail and integral estimates put $H$, $H+A$, and $H+B$ in the cube. Expanding both $F(H+A)$ and $F(H+B)$ about the common point $H$, then comparing $\nabla F(H)$ with $\nabla F(0)$, gives [\[eq:two-point-Taylor\]](#eq:two-point-Taylor){reference-type="eqref" reference="eq:two-point-Taylor"}; the square coefficient is half the Hessian bound. For fixed $r$, the prime-tail scales from RH-384 give $$\|H\|_\infty=O(x^{-1}L^{-1}),\qquad
 \|A\|_\infty+\|B\|_\infty=O(x^{1-2r}L^{-1}).
 \label{eq:head-tail-orders}$$ Thus the right side of [\[eq:two-point-Taylor\]](#eq:two-point-Taylor){reference-type="eqref" reference="eq:two-point-Taylor"} is $o(x^{-2r})$. Combining [\[eq:vector-jump\]](#eq:vector-jump){reference-type="eqref" reference="eq:vector-jump"} with $\nabla F(0)\cdot v_r=\gamma_r>0$ and applying the same two-endpoint triangle argument yields [\[eq:I-necessity\]](#eq:I-necessity){reference-type="eqref" reference="eq:I-necessity"}.

Finally, the full smooth-tail bridge satisfies $$\sum_{j\ge r}\frac{c^j(J_j-I_{2j})}{j}
 =O(x^{-2r-1}L^{-1})=o(x^{-2r})
 \label{eq:J-tail-bridge}$$ for each fixed $r$ and $c\le7$. The endpoint gradient bound transfers the same lower constant to [\[eq:J-necessity\]](#eq:J-necessity){reference-type="eqref" reference="eq:J-necessity"}: the same direct integral estimate puts the $J$-surrogate vector in $[0,1/2]^7$, and the segment joining it to the $I$-surrogate vector remains in that convex cube. Since RH-384 gives $$P_s(y)\sim\frac{x^{1-2s}}{(2s-1)L}
 =\frac{x^{-2r-1}}{(2r+1)L},
 \label{eq:Ps-fixed-scale}$$ division proves [\[eq:necessity-ratios\]](#eq:necessity-ratios){reference-type="eqref" reference="eq:necessity-ratios"} and completes the proof of Theorem [\[thm:necessity\]](#thm:necessity){reference-type="ref" reference="thm:necessity"}. RH-388 established the $s=2$ prototype; the all-r positivity lemma is what closes every fixed retention threshold [@RH388].

# Novelty, scope, and executable boundary

RH-387 resummed the entire infinite prime-tail coordinate, while RH-388 showed that retaining $P_1$ buys $P_2$-scale accuracy in a complete factorial window. The present result moves both boundaries: the exact head grows through $P_{s-1}$, the replacement frontier may be taken as high as $S_y\asymp\log\log x$, and the factorial order ranges over every integer up to $(2s-1)L$. Uniformity requires the growing-order prime estimate, the $7^{S_y}$ budget, denominator control with exponent $s+1$, and the all-rank endpoint sign. It is therefore not a direct fixed-$s$ corollary of RH-386, RH-387, or RH-388.

The negative result is deliberately narrower. It proves fixed-$s$ necessity only for the displayed $P/J/I$ hierarchy. It does not prove growing-$s$ necessity, exclude an arbitrary surrogate, or rule out cancellations purchased with additional exact prime data. The finite $S_K$ are asymptotic truncations; no convergent factorial series is claimed. Channels are the seven real integers, not complex parameters. There is no active-$c_{11}$ statement, growing clock, prefix-dependent $K_N$, operator, trace, prime-power trace, zero identification, or proof of the Riemann hypothesis. Gates A--E are all false.

The exact artifact has epistemic role `finite_exact_algebra_not_analytic_proof`. Its 72 rows comprise 12 kernel/domain/master rows, seven channel rows, 15 all-rank $\gamma$ rows, 12 factorial-window rows, ten growing-rank rows, ten necessity rows, and six theorem/firewall rows. The canonical certificate has 17,571 bytes and SHA-256

e2116abd4aeb910c24ee470a520623f29f1f454bb9b5293840875da091682b3b.

Twenty-four genuine semantic mutations are rejected by an independent field-level verifier that does not call the certificate or row builders. The stored result and closed Draft 2020--12 schema have SHA-256 digests

  -------------------------------------------------------------------
  f91eba3665de25e5572fd71de39f917da40859fb941c9b7df42e84fc02840405
  d6d0daeb126bc90373f06fcc6314a3de1cb6cfda204629945ef77c7078406039.
  -------------------------------------------------------------------

The artifact reproduces exact algebra, types, memberships, source identities, and mutations. It does not prove the prime number theorem estimate, Stieltjes or Tonelli arguments, Maynard's theorem, or an asymptotic limit.

The proof-minimal source closure contains 87 immutable Git blobs from the RH-388 release

8e6f89ee1e58e67c53c5f4719c05e881107113ac,

plus the ordered Johnston--Yang and Maynard remote logical locks, for 89 logical sources. The ordered Git and logical digests are

  -------------------------------------------------------------------
  b86cb21288fe9c48304d90ae812829f5e44f4fac0a2b725a09e5c1512ca60cab
  2255b26dd68adf09f447e251eb5d38c8b1d31fbaa1c26befd8c04165097ed922.
  -------------------------------------------------------------------

The external PDFs and Johnston--Yang source tar are not vendored. Network verification is disabled by default and requires explicit opt-in. The Johnston--Yang author-manuscript nonexclusive distribution license does not establish a third-party redistribution grant, and its version of record is Elsevier copyright. The Maynard version of record is Copyright 2015 Department of Mathematics, Princeton University; current 2022 policy materials do not establish an article-specific grant for the 2015 paper. Both release locks therefore record `redistributable_in_release=false`. Among the two remote inputs, only Johnston--Yang Theorem 1.4 and Maynard Theorem 1.3 play analytic roles. The unrelated active-log source chain is not part of this proof or closure.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

The proof, certificate compiler, strict tests, closed schema, two compact source-lock records, and offline-by-default verification accompany this paper. External source payloads are not redistributed.

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
