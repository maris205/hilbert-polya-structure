---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-periodic-clm-exact-blowup-route-a"
canonical_tex: "henon_dynamics/henon_periodic_clm_exact_blowup_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_periodic_clm_exact_blowup_route_a/paper/main.pdf"
source_sha256: "c55baa375ede416d3f0feda0a3751ce33210caa13f7eec59e9f0e8d666f5e4e4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Periodic Constantin--Lax--Majda Equation: Exact Arbitrary-Mean Riccati Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_periodic_clm_exact_blowup_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_periodic_clm_exact_blowup_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_periodic_clm_exact_blowup_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_periodic_clm_exact_blowup_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We solve the inviscid nonadvective Constantin--Lax--Majda equation on the circle for arbitrary conserved mean under one frozen periodic Hilbert transform convention. The periodic Tricomi identity turns the nonlocal PDE into a pointwise complex Riccati equation, while an invariant Hardy subspace proves that the Hilbert constraint is preserved. This yields exact Möbius formulas in both the zero- and nonzero-mean strata. \>0 For nonzero mean, forward smooth breakdown occurs if and only if the initial vorticity has a zero; the first time is an explicit compact minimum on the principal arccotangent branch. Zero-free data are global and periodic. A separate signed-zero criterion treats zero mean, and the full one-mode threshold diagram follows. \>1 At every simple first pole we prove a local inverse-time self-similar vorticity profile. A global two-sided inverse-time bound is stated only when all simultaneous first poles are simple; tangent and higher-order zeros remain in the exact breakdown theorem but outside that rate claim. The strict Route-A evaluation fails all five gates.
author:
- 'HCS-C377 theorem package'
date: 4 September 2026
title:
- 'The Periodic Constantin--Lax--Majda Equation: Exact Arbitrary-Mean Riccati Flow'
- 'The Periodic Constantin--Lax--Majda Equation: Exact Arbitrary-Mean Flow and Complete First-Pole Clock'
- 'The Periodic Constantin--Lax--Majda Equation: Exact Arbitrary-Mean Flow, First-Pole Clock, and Transverse Profiles'
```

## Markdown 正文

**Keywords:** periodic Hilbert transform; Constantin--Lax--Majda equation; complex Riccati flow; exact Möbius solution; \>0 first-pole clock; one-mode thresholdHardy constraint; conserved mean \>1 ; transverse self-similarity.

chinese-simplified

中文摘要

本文在固定的周期希尔伯特变换符号约定下，求解任意守恒均值的无粘、 无平流康斯坦丁、拉克斯和马吉达方程。周期特里科米恒等式把非局部方程 化为逐点复黎卡提方程，而不变哈代子空间保证希尔伯特约束始终保持， 由此得到零均值与非零均值两类精确莫比乌斯公式。 \>0 当均值非零时，正向光滑解失效当且仅当初始涡量存在零点；首个失效时间 由主值反余切分支上的紧致最小值精确给出。无零点数据全局存在并周期 返回；零均值情形具有不同的带符号零点判据，单傅里叶模的全部阈值情形 也被分类。 \>1 对每个简单首极点，本文证明局部逆时间自相似涡量剖面。只有全部同时首 极点均为简单零点时，才给出全局无穷范数的双边逆时间界；切触及更高阶 零点仍属于精确失效定理，但不进入该速率结论。严格甲路线五项门均未 通过。

关键词：周期希尔伯特变换；康斯坦丁、拉克斯和马吉达方程； 复黎卡提流；精确莫比乌斯解；\>0 首极点时钟； 单模阈值哈代约束；守恒均值\>1； 横截自相似。

# Convention and exact Riccati closure

Write $\mathbb T=\mathbb R/(2\pi\mathbb Z)$. For a real smooth periodic function, define $$\mathcal H(\mathrm e^{\mathrm ikx})=-\mathrm i\operatorname{sgn}(k)\mathrm e^{\mathrm ikx},
 \qquad \mathcal H1=0.                                  \label{eq:Hconvention}$$ Thus $\mathcal H\sin(kx)=-\cos(kx)$ and $\mathcal H\cos(kx)=\sin(kx)$ for $k>0$. On mean-zero functions, $\mathcal H^2=-I$; on real $L^2$, $\mathcal H$ is skew-adjoint.

Consider $$\partial_t\omega=\omega\mathcal H\omega,
 \qquad \omega(0,x)=\omega_0(x).                \label{eq:clm}$$ Let $$\mu=\langle \omega_0\rangle=\frac1{2\pi}\int_{-\pi}^{\pi}\omega_0(x)\,\mathrm dx,
 \quad f=\omega-\mu,\quad h=\mathcal Hf,\quad z=h+\mathrm if.$$

[\[lem:tricomi\]]{#lem:tricomi label="lem:tricomi"} For real mean-zero $f$, $$\mathcal H(f\mathcal Hf)=\frac{(\mathcal Hf)^2-f^2}{2}.            \label{eq:tricomi}$$ Moreover $\langle f\mathcal Hf\rangle=0$.

For a trigonometric polynomial, split its Fourier series into positive and negative Hardy parts. On those parts [\[eq:Hconvention\]](#eq:Hconvention){reference-type="eqref" reference="eq:Hconvention"} is multiplication by $-\mathrm i$ and $+\mathrm i$, respectively. Comparing the positive and negative parts of the product gives [\[eq:tricomi\]](#eq:tricomi){reference-type="eqref" reference="eq:tricomi"}; the zero Fourier coefficient vanishes by the skew-adjointness of $\mathcal H$. Density and boundedness of $\mathcal H$ on Sobolev spaces extend the identity to smooth $f$.

[\[thm:mobius\]]{#thm:mobius label="thm:mobius"} The mean $\mu$ is conserved and $$z_t=\mathrm i\mu z+\frac12z^2.                         \label{eq:riccati}$$ Before the first zero of its denominator, the exact solution is $$\begin{aligned}
 \mu=0:\quad &z(t,x)=\frac{2z_0(x)}{2-tz_0(x)},  \label{eq:zeroz}\\
 &\omega(t,x)=
 \frac{4\omega_0(x)}{[2-th_0(x)]^2+t^2\omega_0(x)^2}; \label{eq:zeroomega}\\
 \mu\ne0:\quad &z(t,x)=
 \frac{\mathrm e^{\mathrm i\mu t}z_0(x)}
 {1-[\mathrm e^{\mathrm i\mu t}-1]z_0(x)/(2\mathrm i\mu)}.        \label{eq:nonzeroz}\end{aligned}$$ If $$\Delta(t,x)=2\mathrm i\mu-[\mathrm e^{\mathrm i\mu t}-1]z_0(x),   \label{eq:delta}$$ then the real vorticity formula for $\mu\ne0$ is $$\omega(t,x)=\frac{4\mu^2\omega_0(x)}{|\Delta(t,x)|^2}. \label{eq:nonzeroomega}$$

Skew-adjointness gives $\partial_t\langle \omega\rangle=\langle \omega\mathcal H\omega\rangle=0$. Hence $$f_t=\mu h+fh,\qquad
 h_t=\mu\mathcal Hh+\mathcal H(fh)=-\mu f+\tfrac12(h^2-f^2),$$ where Lemma [\[lem:tricomi\]](#lem:tricomi){reference-type="ref" reference="lem:tricomi"} and $\mathcal Hh=-f$ were used. Combining the two real equations proves [\[eq:riccati\]](#eq:riccati){reference-type="eqref" reference="eq:riccati"}. Separation gives [\[eq:zeroz\]](#eq:zeroz){reference-type="eqref" reference="eq:zeroz"}. For $\mu\ne0$, differentiating $1/z$ gives a scalar linear equation; solving it yields [\[eq:nonzeroz\]](#eq:nonzeroz){reference-type="eqref" reference="eq:nonzeroz"}. Taking the imaginary part of [\[eq:zeroz\]](#eq:zeroz){reference-type="eqref" reference="eq:zeroz"} gives [\[eq:zeroomega\]](#eq:zeroomega){reference-type="eqref" reference="eq:zeroomega"}. Finally multiply [\[eq:nonzeroz\]](#eq:nonzeroz){reference-type="eqref" reference="eq:nonzeroz"} by $2\mathrm i\mu/\Delta$ and its complex conjugate. Using $z_0=h_0+\mathrm i(\omega_0-\mu)$ gives exactly [\[eq:nonzeroomega\]](#eq:nonzeroomega){reference-type="eqref" reference="eq:nonzeroomega"}.

It remains to check that the pointwise Riccati solution is still a solution of the nonlocal PDE, rather than merely of a larger product system. For $s>1/2$, the negative-frequency Hardy subspace of $H^s(\mathbb T)$ is a Banach algebra. Under [\[eq:Hconvention\]](#eq:Hconvention){reference-type="eqref" reference="eq:Hconvention"}, $z_0=\mathcal Hf_0+\mathrm if_0$ has only strictly negative Fourier modes. The vector field $z\mapsto\mathrm i\mu z+z^2/2$ is locally Lipschitz and preserves that subspace, so uniqueness for the Banach-space ODE shows that the explicit $z(t)$ retains strictly negative modes. Consequently its imaginary part has mean zero and its real part is exactly the Hilbert transform of its imaginary part: $h=\mathcal Hf$.

Equivalently, if $g=h-\mathcal Hf$ is the constraint defect in the product system, Lemma [\[lem:tricomi\]](#lem:tricomi){reference-type="ref" reference="lem:tricomi"} gives $$g_t=(\mathcal Hf)g+\tfrac12g^2-\mu\mathcal Hg-\mathcal H(fg).$$ This equation is locally Lipschitz in the same Sobolev algebra, and $g(0)=0$ forces $g\equiv0$. On any compact time interval where the displayed denominator has a positive lower bound, the explicit rational formula remains smooth in $x$; the same local uniqueness argument continues the PDE solution across the interval. Thus a denominator zero, not a loss of the Hilbert constraint, is the only obstruction used below.

*Round-zero certificate: round zero fixes the periodic Hilbert sign, proves the Tricomi closure, conserves the arbitrary mean, and derives both exact Möbius solutions and real vorticity formulas.*

\>0

# Complete forward-time classification

Use the principal branch $$\operatorname{arccot}:\mathbb R\longrightarrow(0,\pi),\qquad
 \frac{\,\mathrm d}{\,\mathrm dr}\operatorname{arccot}r=-\frac1{1+r^2}.        \label{eq:acot}$$

[\[thm:nonzeroclock\]]{#thm:nonzeroclock label="thm:nonzeroclock"} Suppose $\mu\ne0$, put $a=|\mu|$, and let $Z_0=\{x:\omega_0(x)=0\}$. If $Z_0$ is empty, the solution is global, smooth, and has time period $2\pi/a$ (not necessarily its least period). If $Z_0$ is nonempty, the first positive denominator pole is $$T_+=\min_{x\in Z_0}\frac2a
       \operatorname{arccot}( h_0(x)/a ),                         \label{eq:Tnonzero}$$ and the classical smooth solution breaks down at $T_+$. Thus forward breakdown occurs if and only if the initial vorticity has a zero.

For $0<t<2\pi/a$, the equation $\Delta(t,x)=0$ is equivalent to $$z_0(x)=\frac{2\mathrm i\mu}{\mathrm e^{\mathrm i\mu t}-1}
       =\mu\cot(\mu t/2)-\mathrm i\mu.$$ Its imaginary part is $\omega_0(x)-\mu=-\mu$, exactly the condition $\omega_0(x)=0$. Its real part is $$h_0(x)=\mu\cot(\mu t/2)=a\cot(at/2).$$ The last function decreases bijectively from $+\infty$ to $-\infty$ on the displayed time interval. Equation [\[eq:acot\]](#eq:acot){reference-type="eqref" reference="eq:acot"} therefore gives one and only one pole time for each initial zero, and compactness of $Z_0$ gives the minimum [\[eq:Tnonzero\]](#eq:Tnonzero){reference-type="eqref" reference="eq:Tnonzero"}. At a pole, $z$ has a Riccati pole, so its real part $h=\mathcal H(\omega-\mu)$ becomes unbounded and smooth evolution fails. If $Z_0$ is empty, $\Delta$ never vanishes. It is periodic in time and bounded away from zero on one compact time cell, proving global smoothness and the stated period.

[\[thm:zeroclock\]]{#thm:zeroclock label="thm:zeroclock"} Suppose $\mu=0$ and define $$Z_+=\{x:\omega_0(x)=0,\ h_0(x)>0\}.$$ If $Z_+$ is nonempty, the first positive denominator pole is $$T_+=\min_{x\in Z_+}\frac{2}{h_0(x)}.             \label{eq:Tzero}$$ If $Z_+$ is empty, the exact solution is global forward in time. In particular, the identically zero datum is stationary.

The denominator in [\[eq:zeroomega\]](#eq:zeroomega){reference-type="eqref" reference="eq:zeroomega"} is a sum of two real squares. It vanishes precisely when $\omega_0(x)=0$ and $2-th_0(x)=0$. A positive solution requires $h_0(x)>0$ and is then unique. Taking the first such time proves [\[eq:Tzero\]](#eq:Tzero){reference-type="eqref" reference="eq:Tzero"}; if there is none, no positive-time denominator can vanish.

# Complete one-mode phase diagram

[\[cor:onemode\]]{#cor:onemode label="cor:onemode"} Let $A\ne0$, $k\in\mathbb Z_{>0}$, and $$\omega_0(x)=\mu+A\sin(kx),\qquad h_0(x)=-A\cos(kx). \label{eq:onemode}$$ For $\mu\ne0$: $$\begin{aligned}
 |\mu|>|A|&:\quad \text{global and periodic};\\
 |\mu|=|A|&:\quad T_+=\pi/|\mu|\quad\text{(tangent zero)};\\
 0<|\mu|<|A|&:\quad
 T_+=\frac{2}{|\mu|}\operatorname{arccot}(
 \sqrt{A^2-\mu^2}/|\mu|).\end{aligned}$$ For $\mu=0$, $T_+=2/|A|$. The clock is independent of $k$; the number of spatial copies changes with $k$.

Zeros exist exactly when $|\mu|\le|A|$. At a zero, $\sin(kx)=-\mu/A$, so the two possible Hilbert values are $h_0=\pm\sqrt{A^2-\mu^2}$. Since [\[eq:acot\]](#eq:acot){reference-type="eqref" reference="eq:acot"} is decreasing, the positive value gives the first time in the crossing regime. At equality the Hilbert value is zero. For zero mean, the largest positive Hilbert value at a zero is $|A|$, and Theorem [\[thm:zeroclock\]](#thm:zeroclock){reference-type="ref" reference="thm:zeroclock"} applies.

*Round-one certificate: round one adds necessary-and- sufficient global/breakdown criteria for both mean strata, fixes the principal arccot branch, proves the first forward clock, and closes the entire one-mode phase diagram.*

\>1

# Transverse first-pole profiles

The Riccati pole always detects loss of smoothness through $h$. A vorticity rate needs spatial transversality and is not asserted at a tangent zero.

[\[thm:profile\]]{#thm:profile label="thm:profile"} Let $x_*$ be a point attaining the first forward time $T=T_+$ and assume the initial zero is simple: $\omega_0(x_*)=0$ and $\omega_0'(x_*)\ne0$. Put $$z_*=z_0(x_*),\qquad z_*'=h_0'(x_*)+\mathrm i\omega_0'(x_*),
 \qquad \tau=T-t.$$ If $\mu\ne0$, set $E_*=\mathrm e^{\mathrm i\mu T}$ and $$D_*(y)=\mathrm i\mu E_*z_*-(E_*-1)z_*'y.              \label{eq:Dnonzero}$$ Then, locally uniformly for real $y$, $$\lim_{\tau\downarrow0}\tau\,
 \omega(T-\tau,x_*+\tau y)
 =\frac{4\mu^2\omega_0'(x_*)y}{|D_*(y)|^2}.      \label{eq:Pnonzero}$$ If $\mu=0$, then $z_*=h_0(x_*)>0$, $T=2/h_0(x_*)$, and $$\lim_{\tau\downarrow0}\tau\,
 \omega(T-\tau,x_*+\tau y)
 =\frac{4\omega_0'(x_*)y}
 {|h_0(x_*)-Tz_*'y|^2}.                          \label{eq:Pzero}$$ Both denominators are nonzero for every real $y$, and both profiles are nontrivial.

For $\mu\ne0$, Taylor expansion of [\[eq:delta\]](#eq:delta){reference-type="eqref" reference="eq:delta"} at $(T,x_*)$ gives $$\Delta(T-\tau,x_*+\tau y)=\tau D_*(y)+O(\tau^2),
 \qquad
 \omega_0(x_*+\tau y)=\tau\omega_0'(x_*)y+O(\tau^2).$$ Insert these expressions into [\[eq:nonzeroomega\]](#eq:nonzeroomega){reference-type="eqref" reference="eq:nonzeroomega"}. To see that $D_*(y)$ cannot vanish for real $y$, write $E_*=\mathrm e^{\mathrm i\theta}$ and use the pole relation $z_*=2\mathrm i\mu/(E_*-1)$. The ratio of the constant and linear coefficients in [\[eq:Dnonzero\]](#eq:Dnonzero){reference-type="eqref" reference="eq:Dnonzero"} is $$\frac{\mathrm i\mu E_*z_*}{(E_*-1)z_*'}
 =\frac{\mu^2}{2\sin^2(\theta/2)}\frac1{z_*'}.$$ It is not real because $\operatorname{Im}z_*'=\omega_0'(x_*)\ne0$.

For $\mu=0$, expand $2-tz_0(x)$ at $(T,x_*)$: $$2-(T-\tau)z_0(x_*+\tau y)
 =\tau[h_0(x_*)-Tz_*'y]+O(\tau^2).$$ Equation [\[eq:zeroomega\]](#eq:zeroomega){reference-type="eqref" reference="eq:zeroomega"} gives [\[eq:Pzero\]](#eq:Pzero){reference-type="eqref" reference="eq:Pzero"}. A real zero of its linear denominator would force $\omega_0'(x_*)y=0$, then also $h_0(x_*)=0$, a contradiction. Choosing any sufficiently small nonzero $y$ proves that each profile is nontrivial.

If every point attaining $T_+$ is a simple zero, then there are constants $0<c<C<\infty$ such that, for $t$ sufficiently close to $T_+$, $$\frac{c}{T_+-t}\le\|\omega(t)\|_{L^\infty(\mathbb T)}
 \le\frac{C}{T_+-t}.                             \label{eq:rate}$$

Simple zeros on a compact circle are finite. At each first pole, the real two-variable map from $(T-t,x-x_*)$ to the complex denominator has invertible derivative by the nonvanishing argument in Theorem [\[thm:profile\]](#thm:profile){reference-type="ref" reference="thm:profile"}. Hence locally its modulus is comparable to $[(T-t)^2+(x-x_*)^2]^{1/2}$, while the numerator in either real formula is $O(|x-x_*|)$. The elementary bound $r/(\tau^2+r^2)\le1/(2\tau)$ gives the upper estimate. Away from these finitely many neighborhoods the denominator stays bounded below. A nonzero value of either limiting profile supplies the lower estimate.

# Boundary and claim atlas

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  stratum                             exact status
  ----------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  $\mu\ne0$, no initial zero          global smooth solution with period $2\pi/|\mu|$; constants may have a smaller period.

  $\mu\ne0$, simple first zero        exact clock [\[eq:Tnonzero\]](#eq:Tnonzero){reference-type="eqref" reference="eq:Tnonzero"}, local profile [\[eq:Pnonzero\]](#eq:Pnonzero){reference-type="eqref" reference="eq:Pnonzero"}, and the global rate [\[eq:rate\]](#eq:rate){reference-type="eqref" reference="eq:rate"} if all simultaneous first poles are simple.

  $\mu\ne0$, tangent or higher zero   exact Riccati breakdown still holds; no simple-pole vorticity profile or universal rate is claimed.

  $\mu=0$, $Z_+\ne\varnothing$        exact clock [\[eq:Tzero\]](#eq:Tzero){reference-type="eqref" reference="eq:Tzero"}; profile and rate only under the same simple-pole hypotheses.

  $\mu=0$, $Z_+=\varnothing$          global forward solution; the zero datum is stationary. Backward-time poles are a separate signed question.

  after $T_+$                         no classical smooth continuation through the denominator pole is selected by this theorem.

  three-dimensional Euler             CLM is a source model; no Euler singularity conclusion follows from this exact solution.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Route-A closure and exact audit

The strict tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}),$$ and the verdict is `ROUTE_A_REJECTED`. Fourier integers are not rational-prime input; the solution supplies no isolated arithmetic orbit ledger, determinant-to-target bridge, target analytic data, or natural self-adjoint quantization. Route B is locked.

Four exact A0 controls make the failure constructive: after deleting the mode label, unit, prime, and composite Fourier modes have identical clock ledgers; the affine permutation $k\mapsto1+((5(k-1)+3)\bmod16)$ preserves all such ledgers; neighboring $(\mu,A)$ cells change only at $|\mu|=|A|$; and the simpler zero-mean parent has the same nonarithmetic mechanism. Thus none of these checks supplies the missing prime carrier.

The exact artifact audits 256 Hilbert multipliers, 1,024 Tricomi polynomials, 2,560 Möbius cells across the two mean strata, 2,304 one-mode regimes, four arithmetic controls, 1,280 transverse profile cells, and seven boundaries. It includes an importing-independent checker, symbolic convention audit, isolated byte replay, repaired-hash hostile mutations, and deterministic PDF gates. The computation is a transcription certificate for the analytic proof, never a finite-sampling proof. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.

*Round-two certificate: round two adds transverse local profiles, the correctly conditional global inverse-time rate, tangent-zero and continuation boundaries, the source/collision audit, and the strict Route-A stop.*

# Sources and ownership {#sources-and-ownership .unnumbered}

The source model is P. Constantin, P. D. Lax, and A. Majda, *Communications on Pure and Applied Mathematics* 38 (1985), 715--724, doi:10.1002/cpa.3160380605. Periodic generalized-CLM context is provided by P. M. Lushnikov, D. A. Silantyev, and M. Siegel, *Journal of Nonlinear Science* 31 (2021), article 82, doi:10.1007/s00332-021-09737-x, arXiv:2010.01201. Nearby repository owners treat finite matrix Riccati flows, Hunter--Saxton, Camassa--Holm peakons, and Keller--Segel blow-up. C377 owns only the fixed-convention arbitrary-mean periodic closure, its first-pole clock, and the explicitly conditional transverse profiles. No global literature novelty is claimed.
