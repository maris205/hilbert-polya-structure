---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-cramer-lundberg-exponential-ruin-route-a"
canonical_tex: "henon_dynamics/henon_cramer_lundberg_exponential_ruin_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_cramer_lundberg_exponential_ruin_route_a/paper/main.pdf"
source_sha256: "8e3e2dc49020222a83830b12fe3468fe854170e6ba8bedc0dc5c29fb0f390157"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# One Joint Transform for the Complete Exponential Cramér--Lundberg Ruin Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_cramer_lundberg_exponential_ruin_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_cramer_lundberg_exponential_ruin_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_cramer_lundberg_exponential_ruin_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_cramer_lundberg_exponential_ruin_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the classical compound-Poisson surplus with exponential claims, we derive one closed joint transform of ruin time and deficit. It gives ultimate ruin on both sides of the safety-loading wall and proves conditional overshoot independence. \>0 We also obtain both finite conditional ruin-time means and prove their critical infinite-mean boundary from a square-root root cusp. \>1 An adjustment martingale closes the exact all-time supremum mixture. No periodic-orbit or arithmetic target conclusion is drawn.
author:
- HCS Research Program
date: 1 September 2026
title: 'One Joint Transform for the Complete Exponential Cramér--Lundberg Ruin Atlas'
```

## Markdown 正文

# Frozen process and joint penalty

Let $N_t$ be Poisson with rate $\nu\geq0$, let $Y_i$ be independent $\operatorname{Exp}(\beta)$ claims with $\beta>0$, and fix $c>0$, $u\geq0$. The surplus, strict ruin time, and deficit are $$U_t=u+ct-\sum_{i=1}^{N_t}Y_i,\qquad
\tau=\inf\{t\geq0:U_t<0\},\qquad D=-U_\tau. \tag{1}$$ Thus $u=0$ is not initially ruined. The Route-A dynamical owner is the killed process $$X_t=U_t\quad(t<\tau),\qquad X_t=\Delta\quad(t\geq\tau),$$ whereas the joint transform below is a first-passage functional of the underlying surplus $U$. Gerber and Shiu [@GerberShiu1998] are cited only for discounted-penalty lineage; Drekic and Willmot [@DrekicWillmot2003] are cited only for exponential-claim ruin-time lineage. No formula or proof below is outsourced.

For $q,s\geq0$ put $$\Phi_{q,s}(u)=\mathbb E_u[e^{-q\tau-sD};\tau<\infty]$$ and define $$r_q=\frac{c\beta-\nu-q+
 \sqrt{(c\beta-\nu-q)^2+4c\beta q}}{2c}. \tag{2}$$

For every frozen parameter, $$\boxed{\displaystyle
 \Phi_{q,s}(u)=\frac{\beta-r_q}{\beta+s}e^{-r_qu}.} \tag{3}$$ Here $0\leq r_q\leq\beta$. If $\nu=0$, then $r_q=\beta$ and (3) is zero. If $\nu>0$, conditional on ruin, $D\sim\operatorname{Exp}(\beta)$ and $D$ is independent of $\tau$.

First-jump conditioning gives, for $u>0$, $$\begin{aligned}
0={}&c\Phi'(u)-(\nu+q)\Phi(u)
+\nu\int_0^u\Phi(u-y)\beta e^{-\beta y}\,dy \notag\\
&+\nu\int_u^\infty e^{-s(y-u)}\beta e^{-\beta y}\,dy. \tag{4}\end{aligned}$$ The last integral is $\beta e^{-\beta u}/(\beta+s)$. To prove that an exponential ansatz is exhaustive, introduce the convolution state $$J(u)=\int_0^u\Phi(u-y)\beta e^{-\beta y}\,dy.$$ Equation (4) is equivalent to the two-dimensional inhomogeneous system $$\begin{aligned}
 c\Phi'&=(\nu+q)\Phi-\nu J
 -\frac{\nu\beta}{\beta+s}e^{-\beta u},\\
 J'&=\beta(\Phi-J),\qquad J(0)=0.
 \end{aligned} \tag{5}$$ Its homogeneous mode $e^{-ru}$ exists exactly when $$cr^2-(c\beta-\nu-q)r-q\beta=0, \tag{6}$$ so these two modes exhaust the homogeneous solution space (with the usual generalized mode at a double root). A particular solution of (5) is $(\Phi,J)=(0,-\beta e^{-\beta u}/(\beta+s))$. For $q>0$, the two roots have opposite signs, so boundedness removes the negative root and retains (2). At $q=0$ with $0<\nu<c\beta$, both $0$ and $R=\beta-\nu/c$ give bounded nonnegative local solutions. Here the strong law for $Z_t=\sum_{i\leq N_t}Y_i-ct$ gives $Z_t/t\to\nu/\beta-c<0$, hence $M=\sup_{t\geq0}Z_t<\infty$ almost surely and $\Phi_{0,s}(u)\leq\mathbb P(M>u)\to0$; this removes the constant mode and selects $R$. If $\nu>c\beta$, boundedness removes the growing negative-root mode and retains $r=0$. At equality the second generalized mode grows linearly and is again removed by boundedness. For the surviving mode, $J=A\beta e^{-ru}/(\beta-r)-\beta e^{-\beta u}/(\beta+s)$, so $J(0)=0$ forces $A=(\beta-r)/(\beta+s)$. This mode exhaustion plus the stated chamber boundaries proves uniqueness, rather than assuming it from the ansatz. If $\nu=0$ there are no claims and $\Phi\equiv0$, which is (3) with $r_q=\beta$. Continuity under the common-path coupling extends the solution from $u>0$ to $u=0$; equality at a claim has probability zero, so the strict-passage convention is preserved.

For $\nu>0$, (3) factors as $\Phi_{q,s}=\{\beta/(\beta+s)\}\Phi_{q,0}$. This identifies the conditional Laplace transform of $D$ and its independence from $\tau$. Pathwise, the same fact is exponential memorylessness beyond the pre-ruin reserve.

\>0

# Every safety-loading chamber

Put $\rho=\nu/(c\beta)$. Setting $q=s=0$ in (2)--(3) gives the following complete boundary law.

For $\nu>0$: $$\begin{array}{c@{\quad}c@{\quad}c}
\toprule
\text{chamber}&\mathbb P_u(\tau<\infty)&\mathbb E_u[\tau\mid\tau<\infty]\\
\midrule
\rho<1&\rho e^{-Ru},\ R=\beta-\nu/c&
\dfrac{1+\nu u/c}{c\beta-\nu}\\[5pt]
\rho=1&1&\infty\\[2pt]
\rho>1&1&\dfrac{\beta u+1}{\nu-c\beta}\\
\bottomrule
\end{array} \tag{7}$$ In all three chambers, $\mathbb E[D\mid\tau<\infty]=1/\beta$. If $\nu=0$, ruin is impossible and conditional ruin quantities are undefined.

At $q=0$, (2) is $R>0$ when $c\beta>\nu$ and zero otherwise, giving the middle column. Differentiate $\Phi_{q,0}$ at zero discount. In the profitable chamber, $r'_0=\nu/[c(c\beta-\nu)]$; in the adverse chamber, $r'_0=\beta/(\nu-c\beta)$. Logarithmic differentiation gives the two finite means in (7).

At criticality, $$r_q=\frac{-q+\sqrt{q^2+4c\beta q}}{2c}
 \sim\sqrt{\frac{\beta q}{c}}.$$ Hence the right derivative of $\Phi_{q,0}$ at zero is $-\infty$, proving the infinite mean rather than substituting into a singular side formula. The deficit mean follows from the first theorem.

\>1

# Adjustment martingale and exact supremum

Assume $0<\rho<1$ and set $Z_t=\sum_{i=1}^{N_t}Y_i-ct$. Since $$\nu\left(\frac{\beta}{\beta-R}-1\right)-cR=0,
 \qquad R=\beta-\nu/c, \tag{8}$$ $e^{RZ_t}$ is a mean-one martingale. If $M=\sup_{t\geq0}Z_t$, ruin from reserve $u$ is precisely $\{M>u\}$. Therefore $$\mathbb P(M=0)=1-\rho,\qquad
 \mathbb P(M>u)=\rho e^{-Ru}\quad(u\geq0). \tag{9}$$ Thus the positive part has density $\rho R e^{-Rx}$. Equation (9) is a source-local workload duality, not a new queue spectrum or target bridge.

# Evidence and Route-A boundary

The canonical receipt contains 36 exact regime rows, 448 joint-transform rows, 144 conditional-first-mean rows, 12 martingale/supremum rows, and six boundary rows. An independent checker passes 4,487 assertions; SymPy passes 15 identities; fresh replay is byte-exact; and 26/26 repaired-hash or stale-hash mutations are rejected. Finite rows are regression checks, not proof of the continuum theorem.

\>1

  Release item                                                                 Result
  --------------------------------------------------------- -------------------------
  Regime / transform / first mean / martingale / boundary           $36/448/144/12/6$
  Independent assertions / symbolic identities                      $4{,}487/15$ PASS
  Fresh replay / hostile mutations                            PASS / $26/26$ rejected
  Evidence SHA-256                                             `6551879f2a73…ded29f0`

The nearest finite queue owner studies a birth--death spectrum; it does not contain this continuous-reserve, absorbing, joint deficit/time theorem. This workspace distinction is not a literature-priority claim.

The Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
 \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}),\qquad
\mathrm{ROUTE\_A\_REJECTED}. \tag{10}$$ There is no arithmetic origin. More precisely, the killed PDMP/Markov semigroup has no intrinsic deterministic, enumerable primitive-periodic-orbit owner. No rational-prime carrier, logarithmic clock, target determinant, target zero match, Hilbert--Pólya operator, or Route-B input follows. Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

9 H. U. Gerber and E. S. W. Shiu, "On the time value of ruin," *North American Actuarial Journal* **2** (1), 48--72 (1998), [doi:10.1080/10920277.1998.10595671](https://doi.org/10.1080/10920277.1998.10595671).

S. Drekic and G. E. Willmot, "On the density and moments of the time of ruin with exponential claims," *ASTIN Bulletin* **33** (1), 11--21 (2003), [doi:10.2143/AST.33.1.1036](https://doi.org/10.2143/AST.33.1.1036).
