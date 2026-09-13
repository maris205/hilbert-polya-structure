---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-exponential-wall-bessel-determinant-route-a"
canonical_tex: "henon_dynamics/henon_exponential_wall_bessel_determinant_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_exponential_wall_bessel_determinant_route_a/paper/main.pdf"
source_sha256: "cae758e743a5d10fda27cf11ab2293f7843bc1af500ece36dac2657179f42a81"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Exponential Wall: \ifcase\CRevisionRound Complete Bessel Spectrum and Resolvent \or Bounded Weyl Residual and an Ordinary Spectral Determinant \else A Genuine Logarithmic Weyl Law and a Residual Counting Obstruction\fi

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_exponential_wall_bessel_determinant_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_exponential_wall_bessel_determinant_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_exponential_wall_bessel_determinant_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_exponential_wall_bessel_determinant_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The positive exponential potential on the Dirichlet half-line has a complete, simple Bessel-order spectrum and a natural self-adjoint quantization of a classical bouncing orbit family. We derive its full resolvent and the boundary derivative that normalizes every eigenfunction. \>0 An exact Bessel series supplies an eventually monotone phase, proving a frequency counting law with a bounded remainder, not merely its leading logarithmic growth. The ordinary trace-class Fredholm determinant equals a normalized modified Bessel function, without a hidden zero-free factor. \>1 We compute the logarithmic heat law, sharp Schatten threshold and a spectral zeta double pole. For every fixed positive frequency scaling and fixed energy shift, the counting function cannot coincide with the Riemann zero count up to finitely many levels: even the forced leading-coefficient alignment leaves an incompatible bounded residual. Pólya and Lagarias own the classical source mechanism; the number-theoretic oscillation input is explicitly cited, not reproved or fitted from data. A real logarithmic Weyl law is not a target spectral identification.
author:
- 'HCS-C398 theorem and reproducibility package'
date: 5 September 2026
title: |
  The Exponential Wall:\
  Complete Bessel Spectrum and Resolvent Bounded Weyl Residual and an Ordinary Spectral Determinant A Genuine Logarithmic Weyl Law and a Residual Counting Obstruction
```

## Markdown 正文

**Keywords:** exponential potential; Bessel order zero; spectral determinant; Weyl remainder; heat trace; counting obstruction.

chinese-simplified

中文摘要

本文研究半直线上的正指数势阱，给出完整单重离散谱、预解式及全部特征函数的归一化。 \>0 精确贝塞尔级数提供最终单调的谱相位，由此证明带有有界余项的对数型计数律， 并将普通迹类行列式严格识别为归一化贝塞尔函数。 \>1 进一步计算热迹对数项及算子理想阈值，并证明所有固定正频率缩放与能量平移 均无法消除目标计数余项的障碍；匹配前两个主项仍然不够。 经典势阱理论与外部数论振荡定理均明确归属，不使用目标零点表拟合， 也不将自然自伴算子直接宣称为目标算子。

关键词：指数势；贝塞尔阶零点；谱行列式；计数余项；热迹；匹配障碍。

# Frozen half-line source and classical clock

For every $a>0$, let $H_a$ be the self-adjoint operator associated with $$q_a[u]=\int_0^\infty\bigl(|u'|^2+a^2e^{2x}|u|^2\bigr)\,dx,
 \quad D(q_a)=H^1_0(0,\infty)\cap L^2(e^{2x}dx).$$ Its domain consists of $u,u'$ locally absolutely continuous, $u(0)=0$, $u\in L^2$ and $-u''+a^2e^{2x}u\in L^2$. Infinity is limit point. The kinetic coefficient and $\hbar$ are one; $E$ denotes energy and $k=\sqrt E$ positive frequency. Pólya's order-zero phenomenon is classical, as documented by Lagarias [@lagarias]; that paper treats the more general right-half-line Morse potential. Our project's full-line Morse system instead has finitely many bound levels and a continuum. Changing the domain and confinement class here is mathematically essential. The source results below are reconstructed, not asserted to have new literature priority.

The classical Hamiltonian is $p^2+a^2e^{2x}$ with specular reflection at $x=0$. Every $E=k^2>a^2$ has one bouncing orbit, turning at $x_* =\log(k/a)$. Its full action and physical period are $$\begin{aligned}
 J(E)&=2\bigl[k\operatorname{arcosh}(k/a)-\sqrt{k^2-a^2}\bigr],\label{action}\\
 T(E)&=J'(E)=\operatorname{arcosh}(k/a)/k.\label{period}\end{aligned}$$ Indeed substitute $y=ae^x/k$ in $2\int_0^{x_*}\sqrt{E-a^2e^{2x}}dx$. The endpoint integrand vanishes, so differentiation gives the period; $\dot x=2p$ fixes its factor. Reversal is $(x,p)\mapsto(x,-p)$. Below $a^2$ the energy shell is empty, and equality is a degenerate wall threshold, not a nontrivial cycle. This continuous energy family is not a rational-prime-indexed list.

# Complete spectrum, Green kernel and normalization

$H_a$ has compact resolvent and a complete orthogonal basis of simple eigenfunctions. Its spectrum is exactly $$a^2<E_1<E_2<\cdots\longrightarrow\infty,\qquad
 K_{i\sqrt{E_n}}(a)=0,$$ and $y_n(x)=K_{i\sqrt{E_n}}(ae^x)$ spans the corresponding eigenspace. There are no other energy zeros of $K_{\sqrt{-E}}(a)$.

The form is dense, closed and bounded below by $a^2$. On its unit ball the squared $L^2$ tail beyond $R$ is at most $a^{-2}e^{-2R}$. Compact interval $H^1$ embedding and this tail bound give compact form embedding and compact resolvent. The spectral theorem then gives a discrete spectrum and complete basis. The inequality $q_a[u]>a^2\|u\|^2$ for nonzero $u$ gives the strict lower bound.

Set $z=ae^x$, $\nu^2=-E$. The equation becomes $z^2y_{zz}+zy_z-(z^2+\nu^2)y=0$. Its unique square-integrable solution at infinity is $K_\nu(ae^x)$: it decays as $e^{-ae^x}/\sqrt{ae^x}$, while an independent $I$ solution grows. These standard Bessel identities and conventions are recorded in DLMF [@dlmf]. Since $K_\nu$ is entire and even in $\nu$, $y_E(x)=K_{\sqrt{-E}}(ae^x)$ is entire in $E$ and independent of the square-root branch. The boundary equation is thus necessary and sufficient for an eigenvalue, including for complex $E$; self-adjointness excludes nonreal zeros. Uniqueness of the decaying solution proves simplicity.

Put $$f_E(x)=K_\nu(a)I_\nu(ae^x)-I_\nu(a)K_\nu(ae^x).$$ The Wronskian $I_\nu'K_\nu-K_\nu'I_\nu=1/z$ gives $f_E(0)=0$, $f_E'(0)=1$. For $E\notin\sigma(H_a)$ the full kernel is $$\label{green}
 (H_a-E)^{-1}(x,y)=
 \frac{f_E(\min(x,y))K_\nu(ae^{\max(x,y)})}{K_\nu(a)}.$$ It has derivative jump $-1$, the Dirichlet boundary and the decaying tail. These verify the inverse first on compactly supported functions, then by the self-adjoint resolvent bound. Any apparent order-branch ambiguity in $f_E$ cancels by uniqueness of its initial-value problem.

Differentiating the equation gives $(H_a-E)\partial_Ey_E=y_E$. Therefore the Wronskian $W=y_E(\partial_Ey_E)'-y_E'\partial_Ey_E$ satisfies $W'=-y_E^2$ and $W(\infty)=0$. At a real eigenvalue, $$\label{norm}
 \|y_n\|^2=-aK'_{i\sqrt{E_n}}(a)
       \left.\partial_E K_{\sqrt{-E}}(a)\right|_{E=E_n}>0.$$ Here prime is argument differentiation. The argument derivative is nonzero by ODE uniqueness, so the energy zero is simple as well. Equation [\[norm\]](#norm){reference-type="eqref" reference="norm"} normalizes every member of the complete basis, not just a finite collection of numerically bracketed roots.

\>0

# An exact phase and bounded Weyl residual

For fixed $a>0$, $N_a(E)=\#\{n:E_n\le E\}$ satisfies $$\begin{aligned}
 N_a(k^2)&=\frac{k\operatorname{arcosh}(k/a)-\sqrt{k^2-a^2}}\pi+O_a(1)
 \label{weyl}\\
 &=\frac{k\log k}\pi+\frac{\log(2/a)-1}\pi k+O_a(1).
 \nonumber\end{aligned}$$ The implied constants need not be uniform as $a\downarrow0$.

The exact series and connection formulas [@dlmf] give, for $k>0$, $$I_{-ik}(a)=\frac{(a/2)^{-ik}}{\Gamma(1-ik)}S_a(k),\quad
 S_a(k)=\sum_{j\ge0}\frac{(a^2/4)^j}{j!(1-ik)_j},\quad
 K_{ik}(a)=\frac{\pi\Im I_{-ik}(a)}{\sinh\pi k}.$$ For $k\ge1$, $|(1-ik)_j|\ge k^j$, so $|S_a(k)-1|\le e^{a^2/(4k)}-1=O_a(k^{-1})$. Differentiating each term introduces a factor bounded by $j/k$; the differentiated majorant is summable and gives $S_a'(k)=O_a(k^{-2})$. For all sufficiently large $k$, $S_a(k)$ is nonzero with a continuous small argument. Define $$\Psi_a(k)=k\log(2/a)+\Im\log\Gamma(1+ik)+\arg S_a(k).$$ The continuous gamma logarithm and differentiated Stirling expansion in a sector about the positive imaginary axis yield $$\Psi_a(k)=k\log(2k/a)-k+\pi/4+O_a(k^{-1}),\qquad
 \Psi_a'(k)=\log(2k/a)+O_a(k^{-2})>0$$ eventually. The exact $K$ expression is a nonzero real amplitude times $\sin\Psi_a(k)$, so every successive phase multiple of $\pi$ gives exactly one zero and there are no extra large zeros. The finitely many low zeros change the count by a bounded constant. This proves the second line of [\[weyl\]](#weyl){reference-type="eqref" reference="weyl"}. The half-action in its first line differs from $k\log(2k/a)-k$ by $O_a(k^{-1})$. This proves the first line too. An oscillatory leading approximation without phase monotonicity would not have justified this counting argument.

# The ordinary Fredholm determinant

The inverse $H_a^{-1}$ is trace class, and for every $E\in\mathbb C$, $$\label{det}
 D_a(E):=\det(I-EH_a^{-1})
 =\prod_{n\ge1}(1-E/E_n)
 =\frac{K_{\sqrt{-E}}(a)}{K_0(a)}.$$ Its order in energy is $1/2$. The resolvent belongs to the Schatten class $S_p$ exactly for $p>1/2$.

Equation [\[weyl\]](#weyl){reference-type="eqref" reference="weyl"} implies $\sqrt{E_n}\sim\pi n/\log n$. Thus $\sum E_n^{-p}$ converges precisely for $p>1/2$; the endpoint diverges. This gives the ordinary trace-class product in [\[det\]](#det){reference-type="eqref" reference="det"} and the resolvent threshold, unchanged by a fixed resolvent parameter.

The integral representation $$K_\nu(a)=\int_0^\infty e^{-a\cosh t}\cosh(\nu t)\,dt$$ gives $\log|K_{\sqrt{-E}}(a)|\le
C_a\sqrt{|E|}\log(|E|+2)+C_a$. Indeed $|\cosh(\nu t)|\le e^{|\nu|t}$ and $\cosh t\ge e^t/2$; substituting $v=ae^t/2$ bounds the integral by a gamma integral when $|\nu|\ge1$. Bounded orders follow by continuity. The energy order is at most $1/2$, and its zero count makes it exactly $1/2$. Hadamard factorization at order less than one leaves only a constant zero-free exponential factor. All zeros are already identified, and $K_0(a)>0$, so normalization at zero proves [\[det\]](#det){reference-type="eqref" reference="det"}. There is no hidden nonconstant entire prefactor.

\>1

# Heat trace and all-parameter nonmatching theorem

As $t\downarrow0$, $$\label{heat}
 \operatorname{Tr}e^{-tH_a}=
 \frac{\log(1/t)-\gamma-2\log a}{4\sqrt{\pi t}}+O_a(1).$$ The spectral zeta continues from $\Re s>1/2$ to $\Re s>0$ with a double pole at $s=1/2$, whose leading coefficient is $1/(4\pi)$. For every fixed $a,c>0$, $b\in\mathbb R$ and integer $m$, it is impossible that $$\label{no-go}
 N_a(c^2T^2+b)=N_{\rm R}(T)+m$$ for all sufficiently large $T$ away from jumps, where $N_{\rm R}$ counts all nontrivial Riemann zeros of positive ordinate, with multiplicity.

Write $N_a(E)=A\sqrt E\log E+B\sqrt E+O_a(1)$, where $A=1/(2\pi)$ and $B=(\log(2/a)-1)/\pi$. Stieltjes integration gives $\operatorname{Tr}e^{-tH_a}=t\int_0^\infty e^{-tE}N_a(E)dE$. The bounded remainder contributes $O_a(1)$, including the integrable low-energy extension of the main terms. Differentiate the gamma integral, using $\Gamma(3/2)=\sqrt\pi/2$ and $\psi(3/2)=2-\gamma-2\log2$, to obtain [\[heat\]](#heat){reference-type="eqref" reference="heat"}. The Mellin heat formula then continues the spectral zeta to $\Re s>0$: the bounded heat remainder is integrable there, while large time decays exponentially. Dividing the logarithmic term by $\Gamma(s)$ gives the leading double-pole coefficient $1/(4\pi)$. No continuation further left is claimed.

For the counting obstruction the external number-theoretic inputs are the Riemann--von Mangoldt formula and the unconditional unbounded values of $S(T)$ of both signs. They are explicitly available in Dobner [@dobner equation (1), Theorem 1]; the classical oscillation mechanism is due to Selberg and Tsang. We do not reprove that theorem. Our left side has expansion $$\frac c\pi T\log T+
 \frac c\pi\bigl[\log(2c/a)-1\bigr]T+O_{a,c,b}(1).$$ The fixed energy shift changes the main expression only by $O(\log T/T)$. On the right the two main coefficients are $1/(2\pi)$ and $-[\log(2\pi)+1]/(2\pi)$, with remainder $S(T)+O(1)$, where $S(T)=O(\log T)$. Equality first forces $c=1/2$, then $a=2\pi$. At those values it would imply $S(T)=O(1)$, contradicting its unconditional unboundedness. The fixed $m$ cannot change this conclusion.

The theorem includes finite spectral modifications but not arbitrary nonlinear reparametrization, parameters depending on height, or different potentials. The value $a=2\pi$ is a forced obstruction case, not a successful fitted candidate. The target count includes off-line zeros; no Riemann hypothesis is assumed.

# Degeneration, verification and scope

At $a=0$ the operator is the free Dirichlet half-line Laplacian, with continuous spectrum $[0,\infty)$ and no compact-resolvent inverse determinant of this convention. As $a\downarrow0$ the forms decrease on their common core; closure gives strong-resolvent convergence to that free operator. This is a singular confinement boundary, not a uniform limit of the counting constants.

The exact evidence checks 108 complex rational series terms, sixteen action substitutions and twelve derivative/tail majorants. Independent 70-digit calculations check Bessel representations, the differential equation, twelve bracketed source roots, three norm identities and the full resolvent trace against the logarithmic determinant derivative. Numerical calculations are regression observations, not interval certification and not the proof of full spectral completeness. No target zeros or prime table enter the definition or computations.

The source has a natural Friedrichs quantization and complex-conjugation time reversal, but no intrinsic rational-prime carrier. A0 and A1 fail; the target A2/A3 bridge fails, despite a true source logarithmic law. A4 records only natural source quantization. Overall the target candidate is rejected, with all nine target/Route-B flags false and no Route B: `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Revision record.

Round zero establishes the full Bessel spectrum and resolvent. Round one adds the bounded Weyl residual and ordinary determinant. Round two adds the heat law and all-parameter nonmatching theorem, after internal nonauthor mathematical review; no external peer review is claimed.

9 J. C. Lagarias, The Schrödinger operator with Morse potential on the right half line, *Commun. Number Theory Phys.* 3 (2009), 323--361. [doi:10.4310/CNTP.2009.v3.n2.a3](https://doi.org/10.4310/CNTP.2009.v3.n2.a3); [arXiv:0712.3238](https://arxiv.org/abs/0712.3238). NIST Digital Library of Mathematical Functions, [§10.25](https://dlmf.nist.gov/10.25), [§10.27](https://dlmf.nist.gov/10.27), [§10.28](https://dlmf.nist.gov/10.28), [§10.32](https://dlmf.nist.gov/10.32), [§5.11](https://dlmf.nist.gov/5.11), accessed 5 September 2026. A. Dobner, Large deviations of the argument of the Riemann zeta function, *Mathematika* 70 (2024), e12251. [doi:10.1112/mtk.12251](https://doi.org/10.1112/mtk.12251); [arXiv:2101.01747v2](https://arxiv.org/abs/2101.01747).
