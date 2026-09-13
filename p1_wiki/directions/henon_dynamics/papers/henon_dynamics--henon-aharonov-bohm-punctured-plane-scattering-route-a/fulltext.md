---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-aharonov-bohm-punctured-plane-scattering-route-a"
canonical_tex: "henon_dynamics/henon_aharonov_bohm_punctured_plane_scattering_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_aharonov_bohm_punctured_plane_scattering_route_a/paper/main.pdf"
source_sha256: "1e2f147b72397318b1200a4a6091b11c6a5f488e0280f693cb3c202a4cabea93"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Friedrichs Aharonov--Bohm Dynamics: Domain and Complete Hankel Spectrum

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_aharonov_bohm_punctured_plane_scattering_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_aharonov_bohm_punctured_plane_scattering_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_aharonov_bohm_punctured_plane_scattering_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_aharonov_bohm_punctured_plane_scattering_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We fix the Friedrichs magnetic Laplacian on the punctured Euclidean plane, with one flux and one physical time convention. Angular Fourier decomposition reduces the closed form to radial Bessel operators of orders $|m-\beta|$. The Hankel Plancherel theorem gives an onto spectral transform in every channel and consequently a purely absolutely continuous spectrum $[0,\infty)$. The exceptional low-order channels retain the regular branch and exclude the singular branch; zero flux recovers the ordinary free Laplacian because a point has zero planar Sobolev capacity. This first manuscript closes the operator domain and the complete spectral representation. It is a reconstruction and audit of classical source theory, not a claim of a new Aharonov--Bohm formula. We carry a fixed Friedrichs domain and flux sign through the complete spectral and scattering theory of the punctured-plane magnetic Laplacian. Incoming and outgoing Bessel asymptotics determine the wave operators and the exact phases $S_m=\exp\{\mathrm i\pi(|m|-|m-\beta|)\}$. All angular channels are included by an onto Hankel transform and a dense-packet strong-limit argument. Abel summation then gives the full angular scattering distribution: a forward delta, a principal-value cotangent, and a constant imaginary term. The familiar differential cross section is recovered only away from the forward ray. This round closes complete source scattering without silently replacing its distributional kernel by an ordinary function. We give a single-convention audit of the Friedrichs Aharonov--Bohm Hamiltonian on the punctured plane. The angular Hankel transform yields the complete absolutely continuous spectrum, and the free wave operators give every scattering phase. Abel summation preserves both the forward delta and the principal-value part. Weber's integral produces a locally convergent heat kernel with an explicit angular tail bound. The global heat semigroup and, at noninteger flux, the scattering correction are noncompact. Two exhaustive channel windows even give different finite determinant limits. Integer gauge covariance classifies position-preserving physical time reversal, while a reflection-composed antiunitary exists at every flux. Exact finite receipts and independent spectral quadrature audit the formulas. The classical results are credited as such; the package advance is their integrated domain, distribution, symmetry, and determinant-boundary verification. This natural scattering system fails the Route-A arithmetic and primitive-orbit gates.
author:
- 'HCS-C383 theorem and reproducibility package'
date: 5 September 2026
title:
- |
  Friedrichs Aharonov--Bohm Dynamics:\
  Domain and Complete Hankel Spectrum
- |
  Friedrichs Aharonov--Bohm Dynamics:\
  Complete Scattering and the Forward Distribution
- |
  Friedrichs Aharonov--Bohm Dynamics:\
  Full Scattering, Heat Kernel, and Determinant Obstructions
```

## Markdown 正文

=3em

中文摘要

本文为穿孔欧氏平面上的阿哈罗诺夫玻姆磁性动力学固定弗里德里希斯实现、磁通符号与物理时间。 角向傅里叶分解把闭二次型化为各阶径向贝塞尔算子的正交直和，阶数由角动量与磁通之差的绝对值决定。 汉克尔变换的普朗歇雷与反演定理给出每个通道的满射谱表示，因此完整谱为非负实轴上的纯绝对连续谱， 没有束缚态或奇异连续谱。低阶通道必须通过二次型选择正规分支；零阶允许常数行为而排除对数奇性， 不能误用逐点零边界条件。零磁通时，点的二维索伯列夫容量为零，穿孔不会改变自由平面拉普拉斯的闭型域。 本轮完成算子定义、边界约定与全通道谱，属于经典理论的可审查重建。 本文在同一弗里德里希斯边界条件下闭合穿孔平面磁性算子的完整散射。 径向贝塞尔函数的大参数渐近分别固定入射与出射相位，汉克尔变换的满射性与稠密波包极限给出完整波算子。 角向散射相位按正负通道分成两个常值半空间，但通道零点的归属不能省略。 通过阿贝尔求和，散射核同时包含前向狄拉克分布、余切主值与常数虚部； 缺少前向项的普通函数并不表示完整酉散射算子。 熟知的微分截面仅在离开前向射线时有函数意义，不能把分布平方当成前向截面。 这一轮把谱域、波算子相位、全通道完备性与分布归一化连接成一个可核查的散射终点。 本文在固定磁通符号与物理时间下统一验证弗里德里希斯阿哈罗诺夫玻姆动力学。 角向汉克尔变换给出完整纯绝对连续谱，贝塞尔入射出射渐近产生全部散射相位， 阿贝尔求和保留前向分布与主值项。 韦伯积分进一步给出局部热核及显式角通道尾界，但全空间热半群并不紧，因此不存在通常的有限热迹。 非整数磁通下散射修正也不紧，而且两种都穷尽整数通道的截断方式得到不同的乘积极限， 揭示普通行列式解释的缺口。 整数规范协变把保持空间点的物理时间反演限定在整数和半整数磁通；复合空间反射的反酉对称则适用于所有磁通， 两种对称不能混为一谈。精确有限记录、独立谱积分与敌对变异检验共同审查这些约定。 经典公式不作为新发现，包内进展是对域、全分布、热核、对称与行列式边界的完整贯通；路线甲仍在算术入口停止。

**Keywords:** Aharonov--Bohm Hamiltonian; Friedrichs extension; Hankel transform; Bessel spectrum; punctured plane

关键词：阿哈罗诺夫玻姆算子；弗里德里希斯扩张；汉克尔变换；贝塞尔谱；穿孔平面 **Keywords:** Aharonov--Bohm scattering; wave operators; angular channels; Abel summation; forward distribution; cross section

关键词：阿哈罗诺夫玻姆散射；波算子；角通道；阿贝尔求和；前向分布；散射截面 **Keywords:** magnetic scattering; Friedrichs domain; heat kernel; gauge covariance; time reversal; noncompactness; Route A

关键词：磁性散射；弗里德里希斯域；热核；规范协变；时间反演；非紧性；路线甲

# One operator and one boundary condition

On $\mathcal H=L^2(\mathbb R^2,r\,\mathrm dr\,\mathrm d\theta)$, set $\hbar=2M=1$ and freeze the nonnegative form, initially on smooth functions compactly supported away from zero, $$q_\beta[f]=\int_0^\infty\int_0^{2\pi}
\left(|\partial_rf|^2+\frac{|(-\mathrm i\partial_\theta-\beta)f|^2}{r^2}\right)
r\,\mathrm d\theta\,\mathrm dr.\label{eq:form}$$ Its closed Friedrichs extension defines the self-adjoint $H_\beta$. The main flux representative is $0\le\beta<1$; integer translates will only be used for gauge comparisons. No spin, contact interaction, alternate self-adjoint extension, finite-radius flux tube, or confining field enters. This choice is material: an unqualified singular differential expression does not fix its quantum dynamics.

Let $e_m(\theta)=(2\pi)^{-1/2}\mathrm e^{\mathrm im\theta}$ and $\nu_m=|m-\beta|$. Angular Parseval gives the orthogonal form sum $$q_\beta=\bigoplus_{m\in\mathbb Z}q_{\nu_m},\qquad
q_\nu[u]=\int_0^\infty\left(|u'|^2+\frac{\nu^2}{r^2}|u|^2\right)r\,\mathrm dr.
\label{eq:radialform}$$ Finite angular sums and smooth compact radial approximants form a core of this sum: Fourier truncation converges in both norm and form energy, and the radial closure then approximates each of finitely many components.

The Friedrichs operator decomposes as $$H_\beta=\bigoplus_{m\in\mathbb Z}h_{\nu_m},\qquad
h_\nu=-\partial_r^2-r^{-1}\partial_r+\nu^2r^{-2}.
\label{eq:radial}$$ The order-$\nu$ Hankel map $$(\mathcal J_\nu u)(k)=\int_0^\infty J_\nu(kr)u(r)r\,\mathrm dr
\label{eq:hankel}$$ is unitary from $L^2(r\,\mathrm dr)$ onto $L^2(k\,\mathrm dk)$ and transforms $h_\nu$ to multiplication by $k^2$. In particular, $$D(h_\nu)=\{u:k^2\mathcal J_\nu u\in L^2(k\,\mathrm dk)\}.
\label{eq:domain}$$ The full operator has purely absolutely continuous spectrum $[0,\infty)$, with no point or singular continuous spectrum.

The form-core argument proves [\[eq:radial\]](#eq:radial){reference-type="eqref" reference="eq:radial"}. For $0<\nu<1$, the two zero-energy branches are $r^\nu$ and $r^{-\nu}$. The latter has divergent form energy and its coefficient is removed in the Friedrichs realization. For $\nu=0$, the logarithmic branch is excluded but the regular constant branch is allowed. Orders $\nu\ge1$ are limit point at zero, and infinity is limit point in every channel. Thus these are precisely the regular Bessel realizations diagonalized by the Hankel Plancherel and inversion theorem [@DLMF]. The transform is onto and gives [\[eq:domain\]](#eq:domain){reference-type="eqref" reference="eq:domain"}; it is not a finite list of formal eigenfunctions. Multiplication by $k^2$ under the non-atomic measure $k\,\mathrm dk$ has the claimed spectral types, and its countable orthogonal sum preserves them.

$H_0$ is the ordinary free plane Laplacian.

For $0<\epsilon<1$, take a radial cutoff equal to zero at $r\le\epsilon^2$, equal to one at $r\ge\epsilon$, and linear in $\log r$ between those radii. Its Dirichlet energy is $2\pi/|\log\epsilon|$. Multiplying a fixed smooth function by this cutoff changes its $L^2$ norm and Dirichlet energy by terms tending to zero. Hence the puncture has zero $H^1$ capacity and the closed zero-flux form equals the full-plane free form.

The original physical effect belongs to Aharonov and Bohm [@AB]; the rigorous spectral and scattering treatment for general extension parameters is reviewed by Pankrashkin and Richard [@PR]. Their magnetic-potential sign corresponds to orders $|m+\alpha|$. Angular reflection, or $\alpha=-\beta$, translates to [\[eq:radial\]](#eq:radial){reference-type="eqref" reference="eq:radial"}. The present formulas use one sign throughout. Reconstructing and testing this classical theory is the purpose of this package; classical formula discovery is not claimed.

\>0

# Complete wave operators in the fixed sign convention

Put $\mu_m=|m|$ and $a_m=\pi(\mu_m-\nu_m)/2$. Define the free comparison by $$W_\pm=\operatorname{s-lim}_{t\to\pm\infty}\mathrm e^{\mathrm itH_\beta}\mathrm e^{-\mathrm itH_0},
\qquad S=W_+^*W_-.
\label{eq:wave}$$

The limits in [\[eq:wave\]](#eq:wave){reference-type="eqref" reference="eq:wave"} exist and are onto. Their channel restrictions and the on-shell angular scattering phases are $$W_{\pm,m}=\mathrm e^{\mp\mathrm ia_m}\mathcal J_{\nu_m}\mathcal J_{\mu_m},\qquad
S_m=\mathrm e^{\mathrm i\pi(|m|-|m-\beta|)}.
\label{eq:phases}$$ For $0<\beta<1$ this is $\mathrm e^{\mathrm i\pi\beta}$ on $m\ge1$ and $\mathrm e^{-\mathrm i\pi\beta}$ on $m\le0$.

The real-order large-argument expansion is $$J_\nu(kr)=\left(\frac2{\pi kr}\right)^{1/2}
\cos(kr-\pi\nu/2-\pi/4)+O((kr)^{-3/2}).
\label{eq:asymptotic}$$ The incoming radial coefficient has phase $\mathrm e^{\mathrm i\pi\nu/2}$ and the outgoing one phase $\mathrm e^{-\mathrm i\pi\nu/2}$. Matching them to the free order $\mu_m$ gives $\mathrm e^{\mathrm ia_m}$ for $W_-$ and $\mathrm e^{-\mathrm ia_m}$ for $W_+$. The rigorous dense-packet argument takes smooth spectral support in a compact subset of $k>0$. Stationary phase puts the incoming packet at $r\asymp2|t|k$ for negative time and the outgoing packet there for positive time. The remainder in [\[eq:asymptotic\]](#eq:asymptotic){reference-type="eqref" reference="eq:asymptotic"} tends to zero in radial $L^2$ in that region, while integration by parts controls the nonstationary complement. This proves the channel limits on a dense set. The wave-operator theorem in [@PR Lemma 7 and the original AB channel calculation] supplies the rigorous existence and completeness statement for exactly this regular extension. The explicit phase matching fixes its sign in our convention. Uniform unitary bounds extend the channel limits to all radial vectors; finite angular sums extend them to $\mathcal H$. Every Hankel product is onto, so their direct sum is onto. Multiplication of $W_{+,m}^*$ and $W_{-,m}$ gives the last formula. Splitting at $m=0$ proves the two constant phases.

# The forward distribution is part of scattering

Let $P_+$ select $m\ge1$ and $P_-$ select $m\le0$ in $L^2(S^1,\,\mathrm d\theta)$. Then $S=\mathrm e^{\mathrm i\pi\beta}P_++\mathrm e^{-\mathrm i\pi\beta}P_-$. Write $\delta_{2\pi}$ for the periodic delta with integral one, and let $\theta$ be outgoing angle minus incoming angle.

The convolution kernel relative to $\,\mathrm d\theta$ is $$K_S(\theta)=\cos(\pi\beta)\delta_{2\pi}(\theta)
-\frac{\sin(\pi\beta)}{2\pi}\operatorname{PV}\cot(\theta/2)
-\frac{\mathrm i\sin(\pi\beta)}{2\pi}.
\label{eq:distribution}$$ Under the amplitude convention $f=(2\pi\mathrm ik)^{-1/2}\sum_m(S_m-1)\mathrm e^{\mathrm im\theta}$, with $\sqrt\mathrm i=\mathrm e^{\mathrm i\pi/4}$, away from $\theta=0$ modulo $2\pi$ one has $$f=-\frac{\sin(\pi\beta)}{\sqrt{2\pi\mathrm ik}}
\big(\cot(\theta/2)+\mathrm i\big),\qquad
\frac{\,\mathrm d\sigma}{\,\mathrm d\theta}=\frac{\sin^2(\pi\beta)}{2\pi k\sin^2(\theta/2)}.
\label{eq:cross}$$

Introduce Abel weights $\rho^{|m|}$, $0<\rho<1$, in the geometric series. Their distributional limits are $$\begin{aligned}
\sum_{m\ge1}\mathrm e^{\mathrm im\theta}&=\pi\delta_{2\pi}-\frac12+\frac\mathrm i2\operatorname{PV}\cot(\theta/2),\label{eq:abelplus}\\
\sum_{m\le0}\mathrm e^{\mathrm im\theta}&=\pi\delta_{2\pi}+\frac12-\frac\mathrm i2\operatorname{PV}\cot(\theta/2).
\label{eq:abelminus}\end{aligned}$$ Multiplying by the two channel phases and dividing by $2\pi$ gives [\[eq:distribution\]](#eq:distribution){reference-type="eqref" reference="eq:distribution"}. Subtracting the identity kernel retains $(\cos\pi\beta-1)\delta_{2\pi}$. Off its support the amplitude equals the function in [\[eq:cross\]](#eq:cross){reference-type="eqref" reference="eq:cross"}; $|\cot(\theta/2)+\mathrm i|^2=\csc^2(\theta/2)$ gives the cross section. No square of a distribution is taken.

For nonzero flux in the chosen interval the integrated away-forward cross section diverges. The two angular projectors nevertheless show $S$ is exactly unitary. These statements concern different objects and are consistent.

\>1

# Local heat kernel and global noncompactness

For $t>0$ write $z=rr'/(2t)$. Weber's exponential integral [@DLMF 10.22.67] and the angular normalizer give the kernel relative to $r'\,\mathrm dr'\,\mathrm d\theta'$: $$K_\beta(t;r,\theta;r',\theta')=
\frac{\mathrm e^{-(r^2+r'^2)/(4t)}}{4\pi t}
\sum_{m\in\mathbb Z}\mathrm e^{\mathrm im(\theta-\theta')}I_{|m-\beta|}(z).
\label{eq:heat}$$ Indeed each radial term before evaluation is $$\int_0^\infty\mathrm e^{-tk^2}J_\nu(kr)J_\nu(kr')k\,\mathrm dk
=\frac{\mathrm e^{-(r^2+r'^2)/(4t)}}{2t}I_\nu(z).
\label{eq:weber}$$

For $z>0$, $\nu_0\ge0$, and $z<2(\nu_0+1)$, put $$B(\nu_0,z)=\frac{\mathrm e^{z^2/4}(z/2)^{\nu_0}}
{\Gamma(\nu_0+1)[1-z/(2(\nu_0+1))]}.
\label{eq:tailbound}$$ The absolute tail of the sum in [\[eq:heat\]](#eq:heat){reference-type="eqref" reference="eq:heat"} outside $|m|\le M$ is at most $B(M+1-\beta,z)+B(M+1+\beta,z)$ whenever both denominators are positive. Consequently the series converges locally uniformly for positive $t,r,r'$.

The positive defining series of $I_\nu$ and $(\nu+1)_j\ge j!$ imply $I_\nu(z)\le (z/2)^\nu\mathrm e^{z^2/4}/\Gamma(\nu+1)$ for $\nu\ge0$. Consecutive terms of this upper bound have ratio $z/[2(\nu+1)]$. Starting at $\nu_0$, sum the geometric majorant to get $\sum_{j\ge0}I_{\nu_0+j}(z)\le B(\nu_0,z)$. The positive and negative omitted angular orders start at $M+1-\beta$ and $M+1+\beta$ respectively. This proves the stated bound; on compact parameter sets one can take $M$ uniformly large. At $z=0$ the series limits apply.

The free-flux identity $\sum_m\mathrm e^{\mathrm im\phi}I_{|m|}(z)=\mathrm e^{z\cos\phi}$ reduces [\[eq:heat\]](#eq:heat){reference-type="eqref" reference="eq:heat"} to the ordinary free plane Gaussian.

For any flux and $t>0$, $\mathrm e^{-tH_\beta}$ is noncompact and has infinite positive extended trace. For $0<\beta<1$, $S-I$ is noncompact, so the ordinary trace-class Fredholm determinant $\det(I+(S-I))$ is unavailable. In addition, $$\prod_{m=-M}^{M}S_m=\mathrm e^{-\mathrm i\pi\beta},\qquad
\prod_{m=-M}^{M+1}S_m=1\quad(M\ge0).
\label{eq:cutoff}$$

In a single Hankel channel, the heat semigroup is multiplication by $\mathrm e^{-tk^2}$. On any fixed positive finite interval of $k$ this function is bounded below. Normalized indicators of disjoint positive-measure subsets form an orthonormal sequence whose images have disjoint supports and norms bounded below, excluding compactness. A positive trace-class operator is compact, so the positive extended trace is infinite.

For the scattering operator, the angular orthonormal vectors satisfy $\|(S-I)e_m\|=2\sin(\pi\beta/2)>0$ for every $m$; their images remain orthogonal. The same compactness criterion applies. In the first window of [\[eq:cutoff\]](#eq:cutoff){reference-type="eqref" reference="eq:cutoff"}, there are $M$ positive and $M+1$ nonpositive indices; the second has $M+1$ of each. The two products follow. Both windows exhaust all integers, so symmetric-cutoff stability by itself does not supply an exhaustion-independent determinant.

This result addresses ordinary determinants and traces. A separately specified relative or renormalized object would require its own definition and theorem.

# Gauge covariance and the precise time-reversal question

For integer $n$, let $U_nf=\mathrm e^{\mathrm in\theta}f$ and let $K$ denote position-space conjugation. Directly on the form core and then by closure, $$H_{\beta+n}=U_nH_\beta U_n^{-1},\qquad KH_\beta K=H_{-\beta}.
\label{eq:gauge}$$ Noninteger $U_n$ would not preserve single-valuedness on this Hilbert space.

Restrict physical time reversal to $T_n=U_nK$, with no spatial reflection: it fixes position and reverses mechanical momentum when it is a symmetry. It preserves $H_\beta$ exactly when $n=2\beta\in\mathbb Z$. In the fundamental interval, these fluxes are $0$ and $1/2$, and $T_n^2=I$.

Equation [\[eq:gauge\]](#eq:gauge){reference-type="eqref" reference="eq:gauge"} gives $T_nH_\beta T_n^{-1}=H_{n-\beta}$. Equality of the coefficients of $-\mathrm i\partial_\theta$ in the radial differential expressions forces $n-\beta=\beta$. Conversely that equality gives form and domain invariance. Since $KU_nK=U_{-n}$, the square is one. Under $n=2\beta$, the mechanical angular momentum is also reversed: $T_n(-\mathrm i\partial_\theta-\beta)T_n^{-1}
=-(-\mathrm i\partial_\theta-\beta)$.

The reflection $Rf(r,\theta)=f(r,-\theta)$ sends $H_\beta$ to $H_{-\beta}$, so $RK$ is a commuting antiunitary for every flux. It moves spatial points; its existence does not establish the position-preserving physical symmetry just classified. Abstract spectral antiunitaries cannot replace that test.

# Evidence, provenance, and the Route-A endpoint

The frozen receipt contains 520 exact channel rows, 680 integer-gauge rows, eight physical-symmetry rows, and 520 cutoff rows. Six high-precision Weber kernels are reconstructed independently by integration of the ordinary-Bessel spectral formula. Twelve away-forward cross sections are reconstructed from the complex amplitude. These finite checks are numerical regression where decimals occur; they are not interval certification or proofs of completeness. The separate proof document records the analytic dependencies.

The package's substantive increment is the connected audit of the Friedrichs domain, all channel phases, full distribution, local heat tail, global noncompactness, cutoff failure, and physical symmetry. Classical AB formulas remain attributed to their original literature. The nearest local magnetic owners concern compact magnetic tori, monopole spheres, and Grushin cylinders; none is this noncompact punctured-plane Friedrichs scattering problem.

Off the puncture the classical magnetic field vanishes. Mechanical momentum is therefore constant along every nonsingular trajectory of positive energy, which is a straight line and has no periodic return. A trajectory hitting the puncture is incomplete here; zero-energy stationary continua are not isolated primitive cycles. Angular integers and winding phases supply no rational-prime carrier. Free flux, neighboring fluxes, and angular-label controls preserve this failure. The strict tuple is $$(A0_{\rm fail},A1_{\rm fail},A2_{\rm fail},A3_{\rm fail},
A4_{\rm unitary/scattering}),\qquad \text{Route A rejected}.
\label{eq:route}$$ The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`. No target arithmetic local data, target Euler factors, root number, automorphy, target divisor or counting law, target functional equation, target-zero match, Hilbert--Pólya operator, or Route B is claimed. The natural source scattering Hamiltonian earns A4 alone and does not repair the failed earlier gates.

9 Y. Aharonov and D. Bohm, "Significance of Electromagnetic Potentials in the Quantum Theory," *Physical Review* 115 (1959), 485--491, [doi:10.1103/PhysRev.115.485](https://doi.org/10.1103/PhysRev.115.485). K. Pankrashkin and S. Richard, "Spectral and scattering theory for the Aharonov--Bohm operators," preprint (2009), [arXiv:0911.4715](https://arxiv.org/abs/0911.4715). NIST Digital Library of Mathematical Functions, [Section 10.17](https://dlmf.nist.gov/10.17) and [Section 10.22](https://dlmf.nist.gov/10.22), Hankel transforms and Weber's exponential integral, accessed 5 September 2026.

round zero domain and complete Hankel spectrum round one complete scattering and forward distribution round two heat kernel, symmetry, and determinant obstruction
