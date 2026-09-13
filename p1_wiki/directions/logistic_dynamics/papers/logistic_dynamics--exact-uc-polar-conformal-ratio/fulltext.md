---
p1_kind: "derived-fulltext-reading-copy"
route: "logistic_dynamics"
logical_paper_id: "logistic_dynamics--exact-uc-polar-conformal-ratio"
canonical_tex: "logistic_dynamics/projects/exact_uc_polar_conformal_ratio/paper/main.tex"
canonical_pdf: "logistic_dynamics/projects/exact_uc_polar_conformal_ratio/paper/main.pdf"
source_sha256: "76b771f221bbefac059d3d68510efffc1b5f324f080b9013b3e634bd95e02792"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Explicit Conformal Restriction Bounds for the Exact-$U_c$ Polar Fredholm Determinant

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../logistic_dynamics/projects/exact_uc_polar_conformal_ratio>)
- [规范 TeX](<../../../../../logistic_dynamics/projects/exact_uc_polar_conformal_ratio/paper/main.tex>)
- [关联 PDF](<../../../../../logistic_dynamics/projects/exact_uc_polar_conformal_ratio/paper/main.pdf>)
- [支撑 Markdown](<../../../../../logistic_dynamics/projects/exact_uc_polar_conformal_ratio/README.md>)
- [BibTeX](<../../../../../logistic_dynamics/projects/exact_uc_polar_conformal_ratio/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the unchanged exact-$U_c$ polar Fredholm determinant, we make the normalized conformal restriction constants in its nuclear Taylor factorization completely explicit. The frozen operator domains are thin stadiums of radius $10^{-3}$, while the proof-only inner stadiums have radius $6\times10^{-4}$. Domain monotonicity of the curvature-$-1$ Poincare metric bounds a midpoint--projection--point path by $D_*=500\pi+\log4$. Hyperbolic invariance of the normalized Riemann maps then gives $$r_L=r_R\le \tanh(D_*/2)=:r_*<1.$$ A 4096-bit outward Arb certificate resolves $1-r_*=3.2418512480136249798\ldots\times10^{-683}$, a gap that ordinary floating-point arithmetic rounds away. Inserting the bound into the inherited two-stream Fredholm coefficient estimate yields the fully numerical same-determinant envelope $$|D_{\mathrm{pol}}(s)|\le
   \exp\!\left(3.45\times10^{689}
   +4.20\times10^{682}(1+|s|)^2\right).$$ The result closes an explicit-proof-constant obligation. It does not compute the exact conformal ratios, determine the true growth type, evaluate a determinant root, or provide arithmetic divisor or quantization evidence.
author:
- Anonymous
date: August 2026
title: |
  Explicit Conformal Restriction Bounds\
  for the Exact-$U_c$ Polar Fredholm Determinant
```

## Markdown 正文

# Frozen determinant and main result

Let $u=U_c$ be the real root of $$u^3-2u^2+2u-2=0,
 \qquad \rho=u-1.$$ The inherited real dynamics is the exact two-full-branch polar map on $I_L=[-\pi/2,0]$ and $I_R=[0,\pi/2]$. Its complex transfer family acts on $$X=A(U_L)\oplus A(U_R),
 \qquad
 B=\{(v_L,v_R):v_L(0)=v_R(0)\},$$ where $U_L,U_R$ are the radius-$10^{-3}$ stadiums about the two branch intervals. With the inherited inverse branches and common logarithmic weight, the operator is $$(\mathcal L_s v)_j(z)=\mathrm e^{s\ell(z)}
 \bigl[v_L(\phi_L(z))+v_R(\phi_R(z))\bigr].
 \tag{1}$$ The preceding stage proves that $\mathcal L_s|_B$ is nuclear of order zero and that $$D_{\mathrm{pol}}(s)=\operatorname{det}_{\mathrm{Fr}}(I-\mathcal L_s|_B)
 \tag{2}$$ is entire. Equation (2), its roof clock, and its signed trace convention are fixed throughout this paper.

For $R=10^{-3}$ and $r_0=6\times10^{-4}$, define $$U_\sigma=\{z:\operatorname{dist}(z,I_\sigma)<R\},
 \qquad
 V_\sigma=\{z:\operatorname{dist}(z,I_\sigma)<r_0\}.
 \tag{3}$$ Normalize $h_\sigma:\mathbb D\to U_\sigma$ by $$h_L(0)=-\frac\pi4,
 \qquad h_R(0)=\frac\pi4,
 \qquad h_\sigma'(0)>0,$$ and put $$r_\sigma=\max_{z\in\overline V_\sigma}
 |h_\sigma^{-1}(z)|.
 \tag{4}$$ Compact containment makes the maximum in (4) well defined.

Set $$D_*=500\pi+\log4,
 \qquad
 r_*=\tanh(D_*/2).
 \tag{5}$$ Then $$r_L=r_R\le r_*<1.
 \tag{6}$$ Moreover, the same determinant (2) satisfies $$|D_{\mathrm{pol}}(s)|\le
 \exp\!\left(3.45\times10^{689}
 +4.20\times10^{682}(1+|s|)^2\right)
 \qquad(s\in\mathbb C).
 \tag{7}$$

The theorem gives an explicit upper envelope only. It does not identify the exact conformal modulus or the true entire-function type.

# A hyperbolic path inside each stadium

Use the curvature-$-1$ Poincare convention $$\lambda_{\mathbb D}(w)=\frac{2}{1-|w|^2},
 \qquad
 d_{\mathbb D}(0,w)=2\operatorname{artanh}|w|.
 \tag{8}$$ Fix $\sigma$ and $z\in\overline V_\sigma$. Let $p$ be the Euclidean projection of $z$ onto $I_\sigma$. The path used in the proof first travels along the real interval from its midpoint $c_\sigma$ to $p$, and then follows the line segment from $p$ to $z$.

Every disk $B(x,R)$, with $x\in I_\sigma$, lies in $U_\sigma$. Hyperbolic density monotonicity therefore gives $$\lambda_{U_\sigma}(x)\le \frac2R.$$ The branch interval has length $L=\pi/2$, and its midpoint is at distance at most $L/2$ from $p$. Consequently $$d_{U_\sigma}(c_\sigma,p)
 \le \frac2R\frac L2
 =500\pi.
 \tag{9}$$

The second segment lies in $B(p,R)$, including when $z\in\partial V_\sigma$, because $|z-p|\le r_0<R$. Disk distance and domain monotonicity give $$d_{U_\sigma}(p,z)
 \le 2\operatorname{artanh}\frac{r_0}{R}
 =\log\frac{R+r_0}{R-r_0}
 =\log4.
 \tag{10}$$ Thus $$d_{U_\sigma}(c_\sigma,z)\le D_*.
 \tag{11}$$ Since $h_\sigma$ is a hyperbolic isometry, (8) and (11) imply $$|h_\sigma^{-1}(z)|\le\tanh(D_*/2)=r_*.$$ Translation by $\pi/2$ maps the left normalized stadium pair to the right one, so uniqueness of the normalized Riemann map also gives $r_L=r_R$.

The small gap below one must be evaluated stably. With $t=\mathrm e^{-D_*}$, write $$r_*=\frac{1-t}{1+t},
 \qquad
 \delta_*=1-r_*=\frac{2t}{1+t},
 \qquad
 \beta_*=-\log r_*=\log\frac{1+t}{1-t}.
 \tag{12}$$ These formulas preserve positivity without subtracting two ordinary-precision numbers that both display as one.

# From the conformal gap to numerical growth constants

The inherited matching-space factorization has two geometric rank-one streams. Its weight satisfies $$W(s)\le \mathrm e^{L_\ell|s|},
 \qquad L_\ell=\frac{103}{125}.
 \tag{13}$$ For one stream, the exact elementary-symmetric identity contains $\prod_{h=1}^k(1-r_\sigma^h)^{-1}$. Since $r_\sigma\le r_*$, each inverse factor is at most $\delta_*^{-1}$. Splitting rank $q$ as $q=k+(q-k)$ between the two streams and retaining the inherited Hadamard factor gives the determinant coefficients $$|a_q(s)|\le q^{q/2}(q+1)
 \left(\frac{\mathrm e^{L_\ell|s|}}{\delta_*}\right)^q
 r_*^{q^2/4-q/2}.
 \tag{14}$$ This is a bound for the same canonical determinant, not for a finite matrix or a separately glued product.

Choose $\theta=1/4096$ and define $$b_\theta=-\log\delta_*+\frac{\beta_*}{2}
 +\frac12\left(\log\frac1{\theta\beta_*}-1\right)+\log2.
 \tag{15}$$ The elementary inequalities $$\log q\le \theta\beta_*q+
 \log\frac1{\theta\beta_*}-1,
 \qquad
 \log(q+1)\le q\log2
 \tag{16}$$ turn (14) into $$|a_q(s)|\le
 \exp\left[-\frac{\beta_*(1-2\theta)}4q^2
 +(L_\ell|s|+b_\theta)q\right].
 \tag{17}$$

Completing the square and summing the shifted Gaussian over the integer lattice yields $$|D_{\mathrm{pol}}(s)|\le
 \left(1+\sqrt{\frac{4\pi}{\beta_*(1-2\theta)}}\right)
 \exp\left(
 \frac{(L_\ell|s|+b_\theta)^2}{\beta_*(1-2\theta)}
 \right).
 \tag{18}$$ Finally, write $L_\ell|s|+b_\theta=L_\ell(1+|s|)+(b_\theta-L_\ell)$ and apply $(x+y)^2\le2x^2+2y^2$. The resulting formulas are $$C_0=
 \log\left(1+\sqrt{\frac{4\pi}{\beta_*(1-2\theta)}}\right)
 +\frac{2(b_\theta-L_\ell)^2}{\beta_*(1-2\theta)},
 \tag{19}$$ $$C_1=\frac{2L_\ell^2}{\beta_*(1-2\theta)}.
 \tag{20}$$

# Outward interval certificate

The companion program evaluates (5), (12), and (15)--(20) with 4096-bit Arb balls. Table [1](#tab:constants){reference-type="ref" reference="tab:constants"} lists the central displayed values; the machine-readable artifact retains the outward radii.

::: {#tab:constants}
  Quantity     Certified displayed value
  ------------ -----------------------------------------------------
  $D_*$        $1572.18262115601650985015615588\ldots$
  $\delta_*$   $3.24185124801362497983758530\ldots\times10^{-683}$
  $\beta_*$    $3.24185124801362497983758530\ldots\times10^{-683}$
  $b_\theta$   $2361.58624122710446397702901049\ldots$
  $C_0$        $3.43996102886264722070369148\ldots\times10^{689}$
  $C_1$        $4.19086282028397353977286883\ldots\times10^{682}$

  : Target-free outward interval calculation. The decimal ceilings $3.45\times10^{689}$ and $4.20\times10^{682}$ lie strictly above the certified balls for $C_0$ and $C_1$.
:::

The artifact also checks the exact rational geometry $$\frac{r_0}{R}=\frac35,
 \qquad
 \frac{R+r_0}{R-r_0}=4,
 \qquad
 \frac2R\frac{\pi}{4}=500\pi,$$ freezes 'python-flint 0.9.0' and FLINT '3.6.0', records source hashes, and reproduces byte for byte. Its data firewall marks every prime table, Riemann-zero table, zeta or xi evaluation, Fredholm evaluation, conformal solver, and fitting flag as false.

The certificate does not validate a numerical approximation of a Riemann map. It validates only scalar consequences of the analytic path theorem.

# Limitations and conclusion

The explicit conformal estimate closes a narrow but necessary reproducibility gap in the LOG-0001 growth theorem. Every constant in the quadratic exponential envelope can now be evaluated from the frozen stadium geometry and the inherited logarithmic-weight bound. No fitted conformal map or external arithmetic data enters the calculation.

The estimate is intentionally elementary. The outer stadium is long relative to its radius, so a path from its midpoint to an endpoint has hyperbolic length of order $10^3$. The resulting gap below one is therefore of order $10^{-683}$, and the determinant constants are correspondingly large. These numbers certify finiteness; they do not describe the true conformal radius or Fredholm growth type.

The Route-A status is unchanged. The construction has a genuine entire dynamical determinant and partial global analytic control, but it still has no log-prime primitive-orbit law, von-Mangoldt trace weights, sharp divisor asymptotic, completed-xi identity, or natural quantization. In particular, the present theorem gives no determinant root and no Route-B authorization.

A smallest follow-up is a structural precheck for lower growth: one must name an explicit coefficient or signed trace contribution together with a cancellation-safe mechanism that transfers it to a lower bound for the same determinant. Without such a mechanism, the lower-growth task is not testable and should not be replaced by numerical root fitting.

# Auxiliary proofs

For $a>0$ and $x>0$, $$\log x\le ax+\log(1/a)-1.$$

The function $\log x-ax$ reaches its global maximum at $x=1/a$, where its value is $\log(1/a)-1$.

For $\alpha>0$ and $c\in\mathbb R$, $$\sum_{q\in\mathbb Z}\mathrm e^{-\alpha(q-c)^2}
 \le 1+\sqrt{\frac\pi\alpha}.$$

Poisson summation shows that the shifted sum is maximized when $c$ is an integer, because every Fourier coefficient of the Gaussian is positive. At an integral shift, $$\sum_{q\in\mathbb Z}\mathrm e^{-\alpha q^2}
 =1+2\sum_{q\ge1}\mathrm e^{-\alpha q^2}.$$ Since $x\mapsto\mathrm e^{-\alpha x^2}$ decreases on $[0,\infty)$, each term in the positive tail is bounded by the integral over the preceding unit interval. Thus $$2\sum_{q\ge1}\mathrm e^{-\alpha q^2}
 \le2\int_0^\infty\mathrm e^{-\alpha x^2}\,dx
 =\sqrt{\frac\pi\alpha}.$$

Suppose $a_0=1$ and for $q\ge1$, $$|a_q|\le\exp(-\alpha q^2+Bq),
 \qquad \alpha>0.$$ Then $$\left|\sum_{q\ge0}a_q\right|
 \le\left(1+\sqrt{\frac\pi\alpha}\right)
 \exp\left(\frac{B^2}{4\alpha}\right).$$

Extend the positive majorant from $q\ge0$ to all integer $q$, complete the square, and apply the preceding lemma with $c=B/(2\alpha)$.

The passage from finite Taylor truncations to $D_{\mathrm{pol}}$ is inherited from the order-zero nuclear theorem. The present paper changes only the numerical majorant and does not introduce a second determinant limit.

# References {#references .unnumbered}

No external references are cited in this self-contained stage report. The argument uses the frozen determinant established in the preceding project stage and standard facts about the Poincare metric, Riemann maps, Fredholm coefficients, and Gaussian sums.
