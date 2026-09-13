---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-skew-brownian-interface-route-a"
canonical_tex: "henon_dynamics/henon_skew_brownian_interface_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_skew_brownian_interface_route_a/paper/main.pdf"
source_sha256: "194816982cd3411e5e89b62b18fa378d4be0887d606bb90ae8e60c8dea3162f8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Kernel, Exit, and Occupation Laws of a Skew Brownian Interface

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_skew_brownian_interface_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_skew_brownian_interface_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_skew_brownian_interface_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_skew_brownian_interface_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give one convention-complete theorem for zero-drift skew Brownian motion. Symmetric local time is frozen explicitly; the Lebesgue kernel and its jump, the speed-measure symmetric kernel, complete resolvent, every two-sided exit probability, both discounted exit transforms, mean exit time, and generalized arcsine occupation law are derived. Ordinary Brownian motion and both one-sided reflected limits remain in the atlas. Executable checks separate finite regression from proof and enforce a strict Route-A stopping boundary.
author:
- 'Route-A source-local certificate HCS-C266'
date: 31 August 2026
title: |
  Kernel, Exit, and Occupation Laws\
  of a Skew Brownian Interface
```

## Markdown 正文

trailerid \[\<C2662222222222222222222222222222\>\<C2662222222222222222222222222222\>\]

# Frozen interface and transition law

Let $B$ be standard Brownian motion and let $L^0(X)$ denote *symmetric semimartingale local time*. For $p\in[0,1]$, put $\theta=2p-1$ and freeze $$X_t=x+B_t+\theta L_t^0(X).$$ Harrison and Shepp proved strong existence and pathwise uniqueness exactly for $|\theta|\le1$ and identified the solution by independently making each reflected Brownian excursion positive with probability $p$ [@HS]. Thus (1) fixes a normalization; replacing symmetric by right local time without changing the coefficient defines a different equation.

Write $\phi_t(z)=(2\pi t)^{-1/2}e^{-z^2/(2t)}$.

For $t>0$, the transition density with respect to Lebesgue measure is $$q_p(t;x,y)=\phi_t(y-x)+(2p-1)\operatorname{sgn}(y)
 \phi_t(|x|+|y|).$$ It is nonnegative, conservative, and satisfies Chapman--Kolmogorov. On the standard Feller core, $Af=f''/2$ off zero and $$p f'(0+)=(1-p)f'(0-).$$

In each open quadrant, (2) is a sum of Gaussian images and solves the heat equation. As a function of the starting point it is continuous at zero; the two derivatives obey (3). Split integration at zero. Half-Gaussian integration gives mass one and positivity, while the same split followed by the Gaussian convolution identity gives Chapman--Kolmogorov. Hence (2) identifies the Feller semigroup of the excursion-sign solution.

The one-sided terminal limits satisfy $q_p(t;x,0+)/q_p(t;x,0-)=p/(1-p)$ when $0<p<1$. Thus the Lebesgue density is not continuous across the terminal interface unless $p=1/2$.

# Speed symmetry and resolvent

For $0<p<1$, choose scale and speed densities $$s'(x)=\begin{cases}(1-p)^{-1},&x<0,\\p^{-1},&x>0,
\end{cases}\qquad
m'(x)=\begin{cases}2(1-p),&x<0,\\2p,&x>0.
\end{cases}$$ The scale condition is exactly (3). Although (2) jumps in its terminal Lebesgue coordinate, $k_p(t;x,y)=q_p(t;x,y)/m'(y)$ is symmetric. Indeed, for $x>0>y$ the forward and reversed Lebesgue densities are $2(1-p)\phi_t(|x|+|y|)$ and $2p\phi_t(|x|+|y|)$. Same-side symmetry is immediate. The semigroup is therefore self-adjoint and contractive on $L^2(m)$.

For $\lambda>0$ and $k=\sqrt{2\lambda}$, $$r_\lambda(x,y)=\int_0^\infty e^{-\lambda t}q_p(t;x,y)\,dt
 =\frac{e^{-k|x-y|}+(2p-1)\operatorname{sgn}(y)
 e^{-k(|x|+|y|)}}{k}.$$

Apply $\int_0^\infty e^{-\lambda t}\phi_t(z)\,dt=e^{-k|z|}/k$ to both images in (2). Formula (4) independently satisfies $(\lambda-A)r=0$ off the pole and interface, condition (3), and the unit resolvent source normalization: its $x$-derivative has jump $-2$ at $x=y$, so $-(1/2)$ times that jump is the unit delta mass.

# Every two-sided exit observable

Let $a,b>0$ and $\tau=\inf\{t\ge0:X_t\notin(-a,b)\}$. Boundary labels are retained rather than folded into one transform.

With $D=pa+(1-p)b$, $$\mathbb P_x(X_\tau=b)=
\begin{cases}
p(x+a)/D,&-a\le x\le0,\\
[pa+(1-p)x]/D,&0\le x\le b.
\end{cases}$$ Put $D_m=(1-p)b+pa$ and $$A=\frac{(1-p)(b^2-a^2)}{D_m},\quad
C=\frac{p(b^2-a^2)}{D_m},\quad
B=\frac{ab[pb+(1-p)a]}{D_m}.$$ Then $$\mathbb E_x\tau=
\begin{cases}-x^2+Cx+B,&x\le0,\\-x^2+Ax+B,&x\ge0.
\end{cases}$$

Equation (5) is the unique piecewise affine solution of $h''=0$ with boundary values zero and one, continuity, and (3). Equivalently it is $(s(x)-s(-a))/(s(b)-s(-a))$ using the scale density displayed above (4). Equation (6) is the unique piecewise quadratic solution of $v''/2=-1$, with zero boundary data and the same two interface conditions.

For $0<p<1$, let $\rho=(1-p)/p$, $k=\sqrt{2\lambda}$, and $$Q=\cosh(kb)\sinh(ka)+\rho\sinh(kb)\cosh(ka).$$ The right-boundary transform $R_\lambda(x)=
\mathbb E_x[e^{-\lambda\tau};X_\tau=b]$ is $$R_\lambda(x)=
\begin{cases}
\sinh(k(x+a))/Q,&x\le0,\\
[\cosh(kx)\sinh(ka)+\rho\sinh(kx)\cosh(ka)]/Q,&x\ge0.
\end{cases}$$ The left transform is $R_\lambda^{,1-p}(-x;b,a)$, and the sum is $\mathbb E_xe^{-\lambda\tau}$.

Solve $u''/2=\lambda u$ on each half. Propagation of $(u,u'/k)$ uses $M(\ell)=\left(\begin{smallmatrix}\cosh(k\ell)&\sinh(k\ell)\\
\sinh(k\ell)&\cosh(k\ell)\end{smallmatrix}\right)$. At zero continuity preserves the first coordinate while (3) multiplies the second by $\rho$. Applying $u(-a)=0,u(b)=1$ gives (7). Reflection exchanges the two boundary labels.

# Occupation law and endpoint atlas

Start at zero and set $U_t=t^{-1}\int_0^t\mathbf1_{\{X_s>0\}}\,ds$.

For $0<p<1$, $U_t$ has a law independent of $t>0$, with density $$f_p(u)=\frac{p(1-p)}{\pi\sqrt{u(1-u)}
 [p^2(1-u)+(1-p)^2u]},\qquad0<u<1.$$ It satisfies $\mathbb EU_t=p$. At $p=0$ and $p=1$ the law is respectively an atom at zero and one.

At inverse local time, positive and negative excursion durations are independent stable-$1/2$ subordinators with Laplace coefficients $p$ and $1-p$. For iid standard positive stable-$1/2$ variables $S_+,S_-$, the ratio is therefore $$\frac{p^2S_+}{p^2S_++(1-p)^2S_-}.$$ The standard ratio calculation gives (8), the two-ray Lamperti law; this occupation construction is also treated in [@ABTWW]. The source has two published corrections [@ABTWWe; @ABTWWse]; no corrected multivariate-density or transform formula is imported here, since (8) follows directly from the stable ratio above. Substitution $u=\sin^2 v$ verifies normalization, and $f_p(u)=f_{1-p}(1-u)$. Finally Fubini and $\mathbb P_0(X_s>0)=p$ give $\mathbb EU_t=p$.

For $p=1/2$, the image term in (2) vanishes, the speed measure $m$ is Lebesgue measure, and (8) is the classical arcsine density. At $p=1$ or $0$, after the first hit of zero all excursions have one sign, producing one-sided reflection. A coefficient $|\theta|>1$ admits no solution and is not part of the model. Drifted, unequal-diffusivity, and sticky interfaces are not claimed.

# Executable receipt and Route-A boundary

The certificate stores 135 kernel, 9 speed-symmetry, 18 resolvent, 50 exact exit, 54 discounted-exit, 6 Chapman--Kolmogorov, and 3 occupation rows. A producer-independent implementation closes 963 assertions, SymPy closes 133 generic and exact identities, fresh replay is byte-identical, and 16/16 stale/repaired-hash mutations are rejected. These 275 rows are regression oracles; the preceding proofs hold for all admissible parameters.

This recurrent noncompact diffusion has no isolated primitive source-orbit ledger, rational-prime carrier, logarithmic prime clock, or source Artin--Mazur product. Speed-space self-adjointness is a formal source hint, not a target operator. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the tuple is $$\texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FORMAL\_HINT)}.$$ The verdict is `ROUTE_A_REJECTED`; Route B is disabled. We claim no target arithmetic local data, Euler factor, root number, automorphy, target divisor, functional equation, target zero match, or Hilbert--Pólya operator.

9 J. M. Harrison and L. A. Shepp, *On skew Brownian motion*, Ann. Probab. **9** (1981), 309--313, [doi:10.1214/aop/1176994472](https://doi.org/10.1214/aop/1176994472). T. Appuhamillage, V. Bokil, E. Thomann, E. Waymire, and B. Wood, *Occupation and local times for skew Brownian motion with applications to dispersion across an interface*, Ann. Appl. Probab. **21** (2011), 183--214, [doi:10.1214/10-AAP691](https://doi.org/10.1214/10-AAP691). T. Appuhamillage, V. Bokil, E. Thomann, E. Waymire, and B. Wood, *Corrections: Occupation and local times for skew Brownian motion with applications to dispersion across an interface*, Ann. Appl. Probab. **21** (2011), 2050--2051, [doi:10.1214/11-AAP775](https://doi.org/10.1214/11-AAP775). T. Appuhamillage, V. Bokil, E. Thomann, E. Waymire, and B. Wood, *Second errata to "Occupation and local times for skew Brownian motion with applications to dispersion across an interface"*, Ann. Appl. Probab. **34** (2024), 5842--5844, [doi:10.1214/24-AAP2106](https://doi.org/10.1214/24-AAP2106).
