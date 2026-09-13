---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-alpha-szego-rank-one-cascade-route-a"
canonical_tex: "henon_dynamics/henon_alpha_szego_rank_one_cascade_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_alpha_szego_rank_one_cascade_route_a/paper/main.pdf"
source_sha256: "e918c40e981ad66505d1fbe1a60afba593eefefccf119fb495eeb3810eed0e02"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Alpha-Szegő Rank-One Dynamics: Exact Reduction and Global Compactness

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_alpha_szego_rank_one_cascade_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_alpha_szego_rank_one_cascade_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_alpha_szego_rank_one_cascade_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_alpha_szego_rank_one_cascade_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We reconstruct the complete rank-one rational dynamics of the perturbed cubic Szegő equation with its original physical time. An exact Fourier convolution gives a six-real-variable system preserving mass, momentum and energy. A logarithmic radial bound excludes finite-time loss of the rank-one condition. The conserved energy defect supplies an explicit lower bound on the distance of the pole from the unit circle whenever the defect is nonzero. Every negative-perturbation orbit is therefore relatively compact. At zero perturbation the exceptional zero-defect data are degree-one inner functions with a pure phase evolution. Spatially constant data form a separate rank-zero face, where the energy equality alone cannot diagnose growth. This first round closes the nonlinear definition, global existence, and the compactness and degeneracy controls needed for a sharp cascade theorem. The model and its classical threshold lineage are credited; this is a source-theorem reconstruction, not a claim of a newly discovered equation. We give a turning-point-safe proof of the full rank-one threshold for the alpha-Szegő equation. Exact Fourier convolution preserves mass, momentum and energy, while an energy-defect estimate controls every off-threshold orbit. At positive perturbation, zero defect forces a strictly positive radial discriminant. Direct differentiation yields a polynomial second-order equation, so uniqueness remains valid at the point where radial velocity vanishes. Its solution is an explicit two-sided hyperbolic-secant-squared profile with an initial-data-dependent time shift. Non-relative-compactness is thus equivalent to the classical energy equality on the entire rank-one manifold. Zero perturbation, negative perturbation and spatial constants are handled separately; constants satisfy the equality but do not cascade. The proof does not infer trajectory uniqueness from a squared first-order identity, and it does not extend the threshold to higher ranks or arbitrary Hardy-space initial data. We close the full rank-one alpha-Szegő threshold with one physical clock, an explicit radial orbit, and its exact high-frequency consequence. A conserved energy defect separates relatively compact trajectories from the positive-perturbation cascade level. On that level a directly derived second-order equation gives a two-sided hyperbolic-secant-squared profile, including its turning point. For every Sobolev exponent above one half, the logarithmic norm-growth rate is the positive radial exponent multiplied by the distance of that Sobolev exponent from one half. The critical norm remains constant while momentum leaves every fixed Fourier window. The native shifted-Hankel square has only one nonzero eigenvalue and a degree-one Fredholm determinant. At fixed positive perturbation a bounded pure mode and a cascading solution share this determinant, so auxiliary isospectrality does not determine even the recurrence type. Exact rational reconstruction and independent high-precision calculations audit the source formulas. The classical threshold is credited to Xu; no arithmetic target, generic Hardy-data classification, or Hilbert--Pólya conclusion is claimed.
author:
- 'HCS-C386 theorem and reproducibility package'
date: 5 September 2026
title:
- |
  Alpha-Szegő Rank-One Dynamics:\
  Exact Reduction and Global Compactness
- |
  Alpha-Szegő Rank-One Dynamics:\
  A Turning-Point-Safe Cascade Theorem
- |
  Alpha-Szegő Rank-One Dynamics:\
  Exact Cascades and Isospectral Blindness
```

## Markdown 正文

=2em

中文摘要

本文在原始物理时间下重建带线性扰动的三次塞戈方程的完整秩一有理动力学。 精确傅里叶卷积给出六个实变量的闭合方程，并保持质量、动量与能量。 径向变量的对数导数估计排除有限时间离开秩一流形。 非零能量缺陷给出极点距单位圆的定量下界，因此相应轨道相对紧。 负扰动的全部轨道均紧；零扰动的零缺陷数据恰为一次内函数，只有纯相位演化。 空间常数是单列的秩零边界，不能用能量等式判断其增长。本轮完成全局定义与退化控制。 本文闭合塞戈方程整个秩一流形上的正扰动级联阈值，并保留径向转折点的唯一性。 质量、动量与能量先给出平方速度恒等式，再从原方程直接推导二阶径向方程。 该二阶方程在速度为零处仍有效，排除了转折点停驻的伪解。 完整径向轨道为双向双曲正割平方型，时间平移由初始位置与速度唯一确定。 由此非相对紧性等价于经典能量阈值。零扰动、负扰动和秩零常数分别处理。 结论不推广到任意哈代空间初值或高秩流形，也不把经典阈值声称为新发现。 本文在同一物理时间下闭合塞戈方程的完整秩一阈值、显式径向轨道与高频级联。 守恒能量缺陷区分紧轨道与正扰动级联，直接二阶方程保持转折点唯一性。 级联径向量具有双向双曲正割平方公式，高阶索伯列夫范数的指数增长率精确确定。 临界范数保持不变，而守恒动量逐渐离开每个固定傅里叶窗口。 原生移位汉克尔算子的平方只有一个非零特征值，其行列式不能区分同参数下的有界轨道与级联轨道。 有理重建、独立高精度积分和尾界核查仅作为回归证据；经典结果明确归属，不提出算术目标或希尔伯特波利亚结论。

**Keywords:** alpha-Szegő; rank-one dynamics; energy threshold; turning point; Sobolev cascade; isospectrality

关键词：塞戈方程；秩一动力学；能量阈值；转折点；索伯列夫级联；等谱性

# One invariant nonlinear source

A finite-rank invariant manifold need not be a finite Fourier approximation. Here it contains infinitely many modes and an exact nonlinear evolution. The cubic Szegő equation and its Hankel structure originate in Gérard--Grellier [@gerard2010]; Xu [@xu2014] established the rank-one threshold for its linear perturbation. Our contribution within this repository is a complete convention-preserving proof and reproducibility package. In particular, we retain the rank hypothesis, the turning point, and the distinction between an auxiliary determinant and physical evolution. We do not claim literature priority for the classical threshold.

Use normalized circle measure and let $\Pi$ retain nonnegative Fourier modes. For every real $\alpha$ fix $$\mathrm iu_t=\Pi(|u|^2u)+\alpha(u\mid1),\qquad
 u(z)=b+\frac{cz}{1-pz},\quad c\ne0,\quad |p|<1.
 \label{eq:pde}$$ The phase space in [\[eq:pde\]](#eq:pde){reference-type="eqref" reference="eq:pde"} is $\mathcal L(1)$; constants will be treated separately. The physical time is $t$, without rescaling. Set $$d=1-|p|^2,\quad \rho=|c|,\quad B=|b|^2,\quad
 Q=B+\frac{\rho^2}{d},\quad M=\frac{\rho^2}{d^2}>0.
 \label{eq:invariants}$$ Energy and its defect are $$E_\alpha=\frac14\|u\|_4^4+\frac\alpha2|b|^2,\qquad
 \delta=E_\alpha-\frac{Q^2}{4}-\frac{\alpha Q}{2}.
 \label{eq:defect}$$ We always take the positive square root of $M$. On a trajectory, $\rho=\sqrt M\,d$ and $B=Q-Md$.

Every initial datum in $\mathcal L(1)$ has a unique solution for all real time. Its coefficients satisfy $$\begin{aligned}
 \mathrm i\dot b&=(B+2\rho^2/d+\alpha)b+\rho^2c\bar p/d^2,\notag\\
 \mathrm i\dot c&=(2B+\rho^2/d^2)c+2b\rho^2p/d,\label{eq:ode}\\
 \mathrm i\dot p&=c\bar b+\rho^2p/d.\notag\end{aligned}$$ The quantities $Q,M,E_\alpha$ are conserved. These statements hold at $b=0$ and $p=0$ and involve no Fourier cutoff.

The geometric Fourier coefficients are $u_0=b$ and $u_n=cp^{n-1}$ for $n\ge1$. Their absolute convergence on strict subdisks justifies convolution in $\Pi(|u|^2u)$. Compare the coefficients of $1,z/(1-pz),z^2/(1-pz)^2$; the derivative of the last coordinate is $c\dot p$, not merely $\dot p$. The result is [\[eq:ode\]](#eq:ode){reference-type="eqref" reference="eq:ode"}. A direct quartic sum gives $$4E_\alpha=B^2+\frac{4B\rho^2}{d}
  +\frac{\rho^4(1+|p|^2)}{d^3}
  +\frac{4\rho^2\Re(bp\bar c)}{d^2}+2\alpha B.
 \label{eq:quartic}$$ Differentiating [\[eq:invariants\]](#eq:invariants){reference-type="eqref" reference="eq:invariants"} and [\[eq:quartic\]](#eq:quartic){reference-type="eqref" reference="eq:quartic"} along [\[eq:ode\]](#eq:ode){reference-type="eqref" reference="eq:ode"} cancels every term, giving the three conservation laws.

To justify all-time continuation, put $X=bp\bar c$. Direct differentiation gives $$\dot d=2\Im X,\qquad
 \dot\rho=2\sqrt M\,\Im X,\qquad
 |\dot\rho/\rho|\le2\sqrt{QM}.
 \label{eq:logbound}$$ Hence $\rho(t)\ge\rho(0)\mathrm e^{-2\sqrt{QM}|t|}$ on every finite time interval. The conserved quantities bound $|b|\le\sqrt Q$, $\rho\le\sqrt M$, and $d=\rho/\sqrt M$ away from zero on that interval. The real six-dimensional vector field is locally Lipschitz on $d>0$, so its continuation theorem excludes finite-time exit. The resulting geometric series solves [\[eq:pde\]](#eq:pde){reference-type="eqref" reference="eq:pde"} in every $H^s$. This argument proves the named invariant-manifold theorem, not global well-posedness for arbitrary Hardy data.

# Compactness and the exact exceptional faces

The defect is useful because it vanishes precisely where a compactness estimate could fail.

For every trajectory in $\mathcal L(1)$, $$\delta=\frac{Md}{2}\left(\left|b+\frac{c\bar p}{d}\right|^2-\alpha\right).
 \label{eq:factor}$$ If $\delta\ne0$, then for every real $t$, $$d(t)\ge
 \frac{2|\delta|}{M\big((\sqrt Q+\sqrt M)^2+|\alpha|\big)}>0.
 \label{eq:compact}$$ The orbit is relatively compact in $\mathcal L(1)$ and bounded in every $H^s$.

Subtract the two terms in [\[eq:defect\]](#eq:defect){reference-type="eqref" reference="eq:defect"} from [\[eq:quartic\]](#eq:quartic){reference-type="eqref" reference="eq:quartic"}; the remaining quadratic expression is [\[eq:factor\]](#eq:factor){reference-type="eqref" reference="eq:factor"}. Since $|b+c\bar p/d|\le\sqrt Q+\sqrt M$, taking absolute values proves [\[eq:compact\]](#eq:compact){reference-type="eqref" reference="eq:compact"}. Thus $|p|$ lies in a strict subdisk and $|c|=\sqrt M\,d$ stays positive, while $b,c$ remain bounded. These inequalities give compact closure within the coefficient manifold. Every Sobolev norm is then bounded by a convergent geometric series.

For $\alpha<0$, [\[eq:factor\]](#eq:factor){reference-type="eqref" reference="eq:factor"} has strictly positive defect; thus all rank-one orbits are relatively compact. On a compact set of initial data, the positive continuous defect has a positive minimum, making the bound uniform for that set. This does not assert uniformity across data approaching a positive-alpha zero-defect hypersurface.

For $\alpha=0$, nonzero defect is already settled. Zero defect forces $b=-c\bar p/d$. Writing $A=c/d$ yields $$Q=M=|A|^2,\qquad
 u(z)=A\,\frac{z-\bar p}{1-pz},\qquad
 u(t,z)=\mathrm e^{-\mathrm iQt}u(0,z).
 \label{eq:inner}$$ The quotient in [\[eq:inner\]](#eq:inner){reference-type="eqref" reference="eq:inner"} has modulus one on the circle. Substitution in [\[eq:ode\]](#eq:ode){reference-type="eqref" reference="eq:ode"} gives $\dot p=0$, $\dot b=-\mathrm iQb$ and $\dot c=-\mathrm iQc$, proving the formula even at $p=0$. Therefore every zero-alpha rank-one orbit is also relatively compact.

#### Rank zero cannot inherit the threshold.

If $c=0$, the parameter $p$ is redundant and the complete solution is $$u(t,z)=b(0)\mathrm e^{-\mathrm i(|b(0)|^2+\alpha)t}.
 \label{eq:constant}$$ Every constant satisfies $\delta=0$ but has constant Sobolev norm. The zero function is stationary. A nonzero constant is stationary exactly when $|b|^2+\alpha=0$; otherwise its least temporal period is $2\pi/||b|^2+\alpha|$. These facts explain why the rank-one hypothesis cannot be dropped from a positive-alpha growth criterion.

\>0

# Turning-point-safe cascade

Assume $\alpha>0$ and $\delta=0$. Define the discriminant $$\kappa^2=4QM-(\alpha-Q-M)^2.
 \label{eq:kappa}$$ The next result strengthens the usable form of the classical threshold: it provides the complete radial trajectory with a valid turning-point proof.

For initial data in $\mathcal L(1)$ and $\alpha>0$, the following are equivalent: the trajectory is not relatively compact in $\mathcal L(1)$; and $\delta=0$. On that level $\kappa>0$, and, with $$d_*=\frac{\kappa^2}{4\alpha M},\qquad
 t_*=\frac2\kappa\mathop{\mathrm{artanh}}\left(\frac{\dot d(0)}{\kappa d(0)}\right),
 \label{eq:shift}$$ the exact radial orbit for every real $t$ is $$d(t)=d_*\mathop{\mathrm{sech}}^2\left(\frac{\kappa(t-t_*)}{2}\right),\qquad
 \rho(t)=\sqrt M\,d(t).
 \label{eq:sech}$$ Here $0<d_*\le1$, and the formula includes $p=0$ at the turn.

Equation [\[eq:factor\]](#eq:factor){reference-type="eqref" reference="eq:factor"} gives $2\Re X=d(\alpha-Q-M)+2Md^2$. Together with $|X|^2=(Q-Md)Md^2(1-d)$ and [\[eq:logbound\]](#eq:logbound){reference-type="eqref" reference="eq:logbound"}, it implies $$\dot d^{\,2}=d^2(\kappa^2-4\alpha Md).
 \label{eq:squared}$$ Since $d>0$, the right side forces $\kappa^2\ge4\alpha Md>0$. Moreover, $$\kappa^2-4\alpha M=-(Q-M-\alpha)^2\le0,
 \label{eq:dstar}$$ so $d_*\le1$.

A squared velocity identity alone permits spurious sticking at a turn. To remove that ambiguity, differentiate the complex ODE itself. Put $T=\alpha-Q-M$. Then $$\begin{aligned}
 \dot X&=\mathrm i(FX+G),\qquad F=-T-4Md,\notag\\
 G&=-M^2d^2(1-d)-(Q-Md)Md^2
       +2(Q-Md)Md(1-d).
 \label{eq:xderivative}\end{aligned}$$ All coefficients $F,G$ are real. Since $\dot d=2\Im X$, substitute $\Re X=dT/2+Md^2$ in $\ddot d=2(F\Re X+G)$ to obtain the polynomial equation $$\ddot d=\kappa^2d-6\alpha Md^2.
 \label{eq:second}$$ This derivation never divides by $\dot d$ or by $p$. At $d=d_*$ it gives $\ddot d=-\kappa^2d_*/2<0$, excluding a stationary turning point.

By [\[eq:squared\]](#eq:squared){reference-type="eqref" reference="eq:squared"}, $v_0=\dot d(0)/(\kappa d(0))$ lies strictly between $-1$ and $1$, so [\[eq:shift\]](#eq:shift){reference-type="eqref" reference="eq:shift"} is finite. The function [\[eq:sech\]](#eq:sech){reference-type="eqref" reference="eq:sech"} solves [\[eq:second\]](#eq:second){reference-type="eqref" reference="eq:second"}. At time zero its logarithmic derivative is $\kappa\tanh(\kappa t_*/2)=\kappa v_0$. Also $\mathop{\mathrm{sech}}^2(\kappa t_*/2)=1-v_0^2=d(0)/d_*$, so both initial data agree. Uniqueness for the polynomial second-order initial-value problem proves [\[eq:sech\]](#eq:sech){reference-type="eqref" reference="eq:sech"} for every real $t$, including the turn.

The radial variable tends to zero at both infinite-time ends, so this orbit does not have compact closure within $\mathcal L(1)$. Every nonzero-defect orbit is compact by [\[eq:compact\]](#eq:compact){reference-type="eqref" reference="eq:compact"}. This proves both directions of the dichotomy.

The all-time clause matters. No finite-time singularity is created: $d(t)$ remains positive for every finite $t$. The expression $\kappa^2/(4\alpha M)$ can equal one, but that is the harmless event $p=0$, not the forbidden pole boundary $|p|=1$.

The source threshold appears in Xu [@xu2014 Theorem 3.1]. We do not rely on a globally positive lower bound for $|\dot d/d|$: that derivative is zero at $t=t_*$. Equations [\[eq:xderivative\]](#eq:xderivative){reference-type="eqref" reference="eq:xderivative"}--[\[eq:second\]](#eq:second){reference-type="eqref" reference="eq:second"} and uniqueness provide the complete argument instead.

\>1

# All-mode Sobolev growth and momentum escape

Define the exact norm convention $$\|u\|_{H^s}^2=\sum_{n\ge0}(1+n)^{2s}|u_n|^2.
 \label{eq:sobolev}$$ The radial theorem has an all-frequency consequence, not merely a growing finite-dimensional diagnostic.

On the positive-alpha cascade level, for every $s>1/2$, $$\begin{aligned}
 \|u(t)\|_{H^s}^2&\sim M\Gamma(2s+1)d(t)^{1-2s},
       && t\to\pm\infty,\label{eq:asymptotic}\\
 \lim_{t\to\pm\infty}\frac{\log\|u(t)\|_{H^s}}{|t|}
       &=(s-\tfrac12)\kappa.\label{eq:rate}\end{aligned}$$ At the critical exponent, $\|u(t)\|_{H^{1/2}}^2=Q+M$ exactly.

For $d\downarrow0$, the geometric sum satisfies $$d^{2s+1}\sum_{n\ge1}(n+1)^{2s}(1-d)^{n-1}
 \longrightarrow\int_0^\infty x^{2s}\mathrm e^{-x}\,\mathrm dx=\Gamma(2s+1).
 \label{eq:riemann}$$ To justify this Riemann-sum limit, use $x=dn$. On a bounded interval separated from zero, the summand converges uniformly to $x^{2s}\mathrm e^{-x}$. A multiple of $x^{2s}$ controls the interval near zero, and an exponential majorant controls the tail. These bounds allow the two omitted intervals to be made arbitrarily small, uniformly for sufficiently small $d$.

Since $|c|^2=Md^2$, multiplying [\[eq:riemann\]](#eq:riemann){reference-type="eqref" reference="eq:riemann"} gives [\[eq:asymptotic\]](#eq:asymptotic){reference-type="eqref" reference="eq:asymptotic"}; the bounded constant coefficient does not contribute to the diverging leading term. Equation [\[eq:sech\]](#eq:sech){reference-type="eqref" reference="eq:sech"} yields $$d(t)\sim\frac{\kappa^2}{\alpha M}
             \mathrm e^{-\kappa|t-t_*|},
 \label{eq:radialtail}$$ and then [\[eq:rate\]](#eq:rate){reference-type="eqref" reference="eq:rate"} follows. At $s=1/2$, direct geometric summation in [\[eq:sobolev\]](#eq:sobolev){reference-type="eqref" reference="eq:sobolev"} gives $Q+M$, proving the critical assertion.

The conserved momentum does not remain in a fixed frequency window. Indeed, $$\|u(t)-b(t)\|_2^2=Md(t)\longrightarrow0,\qquad
 \sum_{n\ge1}n|u_n(t)|^2=M.
 \label{eq:escape}$$ For each fixed $N$, the sum over $1\le n\le N$ tends to zero because $|c(t)|^2\to0$. Thus the source preserves momentum while its location moves beyond every fixed Fourier cutoff. There is no finite-time norm singularity or loss of a conserved quantity.

For the explicit data $u_0(z)=\sqrt\alpha+z$, one has $Q=1+\alpha$, $M=1$, $\kappa=2\sqrt\alpha$, $t_*=0$. Hence $d(t)=\mathop{\mathrm{sech}}^2(\sqrt\alpha\,t)$ and the rate is $(2s-1)\sqrt\alpha$, agreeing with the classical example [@xu2014 Theorem 3.2].

# The same determinant sees opposite dynamics

The relevant Hankel operator is antilinear. Fix the inner product linear in its first variable and define $H_uf=\Pi(u\bar f)$, $K_u=S^*H_u$. The matrix of $K_u$ is $(u_{j+k+1})=(cp^{j+k})$. With $v=(1,p,p^2,\ldots)$, direct multiplication gives $$K_uf=c\langle v,f\rangle v,\qquad
 K_u^2f=\frac{|c|^2}{d}\langle f,v\rangle v.
 \label{eq:hankel}$$ Since $\|v\|^2=1/d$, $K_u^2$ is complex-linear, positive, rank one, and its sole nonzero eigenvalue is $M$.

For all complex $w$ and integers $r\ge1$, $$\det(I-wK_u^2)=1-wM,\qquad \mathop{\mathrm{tr}}(K_u^{2r})=M^r.
 \label{eq:det}$$ At each fixed $\alpha>0$, this determinant is shared by a bounded pure-mode trajectory and a two-sided cascading trajectory.

The first assertions follow from the explicit rank-one linear operator in [\[eq:hankel\]](#eq:hankel){reference-type="eqref" reference="eq:hankel"} and conservation of $M$. For $u_0=z$, the source solution is $u(t)=\mathrm e^{-\mathrm it}z$, with $M=1$. For $u_0=\sqrt\alpha+z$, the preceding theorem gives a cascade, also with $M=1$. Both therefore have determinant $1-w$. Even the recurrence distinction is absent from that determinant. Allowing $\alpha$ to vary further keeps $1-w$ fixed while the growth exponent $2\sqrt\alpha$ varies continuously.

Equation [\[eq:det\]](#eq:det){reference-type="eqref" reference="eq:det"} is a native auxiliary invariant. It is not a determinant of the nonlinear time evolution, and it is not a primitive-orbit product. We do not assign a complex Fredholm determinant directly to the antilinear $K_u$. A zero-free entire factor cannot change the fact that $1-wM$ has only one zero; this polynomial is not a full target divisor.

The source has a concrete reversal on Hardy functions: $$(\mathcal Cu)(z)=\overline{u(\bar z)}.
 \label{eq:reversal}$$ It conjugates Fourier coefficients and preserves the Hardy space. The real convolution coefficients in [\[eq:pde\]](#eq:pde){reference-type="eqref" reference="eq:pde"} show that $\mathcal Cu(-t)$ solves the same alpha equation. Pointwise conjugation alone would reverse Fourier support and is not the stated Hardy-space reversal. This nonlinear Hamiltonian symmetry is not a construction of a linear quantum Hamiltonian.

# Evidence boundary and conclusion

  Source face                Defect        Established behavior
  -------------------------- ------------- ----------------------------
  Rank one, $\alpha<0$       positive      relatively compact
  Rank one, $\alpha=0$       nonzero       relatively compact
  Rank one, $\alpha=0$       zero          inner-function phase orbit
  \>0 Rank one, $\alpha>0$   nonzero       relatively compact
  Rank one, $\alpha>0$       zero          exact two-sided cascade
  Rank zero                  always zero   constant-norm phase orbit

The regime table records a rank distinction, not a fitted classifier. All complex phases are retained in the coefficient ODE. The all-time and all-frequency conclusions are proved analytically; finite computations test independent reconstructions of their formulas.

\>1 The executable ledger contains 144 generic rational rows, 72 threshold rows, 12 zero-alpha inner rows, 24 constant rows and three paired controls. A Fraction-pair producer is checked by an independent SymPy reconstruction using a factored energy expression and the differentiated $p$ equation. Thirteen symbolic identities pass. Independent 100-digit complex ODE integration tests 12 endpoints in both time directions; its largest radial error is below $3\times10^{-52}$ against the exact profile. Twelve direct Fourier sums are checked against generating functions with geometric tail bounds. These are numerical regression results, not interval certificates. Two isolated producer trees reproduce the JSON bytes; 31 hostile cases, including three actual release-write YAML attacks, are rejected, and three smoke tests pass.

The strict assessment is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
   \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).$$ Source integrability and an exact determinant do not supply an arithmetic origin, an arithmetic primitive census, or a target analytic structure.

The claim remains the rank-one source theorem. No arbitrary Hardy-data or higher-rank threshold, complete generic primitive census, target arithmetic local data, target Euler factors, root number, automorphy, target divisor, target functional equation, target-zero matching, or Hilbert--Pólya operator is claimed. Route B remains disabled. The firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Literature ownership and reproducibility.

The classical equation and threshold belong to the cited sources. Our package makes the turning-point argument, rank-zero failure, physical clock and auxiliary-determinant limitation auditable together. No publication acceptance, worldwide novelty, external-human review or cross-provider validation is asserted. AI-assisted local drafting and independent collaborating-agent review are disclosed. The source proof, locked evaluation, independent scripts and three substantive PDF revisions accompany the article.

#### Conclusion.

Round zero: exact nonlinear reduction and compactness. The rational manifold closes the full coefficient dynamics and every nonpositive-alpha and constant boundary, preparing a valid threshold question. Round one: turning-point-safe cascade theorem. The positive-alpha energy equality gives the exact two-sided radial law; the direct acceleration equation excludes an artificial stationary turn. Round two: Sobolev cascade and determinant blindness. The explicit radial law fixes all high-Sobolev exponents, while a native isospectral determinant misses even the bounded-versus-cascading distinction.

9 P. Gérard and S. Grellier. The cubic Szegő equation. *Annales scientifiques de l'École Normale Supérieure* (4) **43** (2010), 761--810. [doi:10.24033/asens.2133](https://doi.org/10.24033/asens.2133). H. Xu. Large-time blowup for a perturbation of the cubic Szegő equation. *Analysis & PDE* **7** (2014), 717--731. [doi:10.2140/apde.2014.7.717](https://doi.org/10.2140/apde.2014.7.717). Author preprint [arXiv:1307.5284](https://arxiv.org/abs/1307.5284).
