---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-beta2-dyson-ou-eigenvalue-diffusion-route-a"
canonical_tex: "henon_dynamics/henon_beta2_dyson_ou_eigenvalue_diffusion_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_beta2_dyson_ou_eigenvalue_diffusion_route_a/paper/main.pdf"
source_sha256: "ca6e190ef5292c0239d84ef6a31733ad32891fce096761a8a4f601f1ec29322d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Beta-Two Dyson--Ornstein--Uhlenbeck Diffusion: Matrix Radialization and Ordered GUE Equilibrium

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_beta2_dyson_ou_eigenvalue_diffusion_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_beta2_dyson_ou_eigenvalue_diffusion_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_beta2_dyson_ou_eigenvalue_diffusion_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_beta2_dyson_ou_eigenvalue_diffusion_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We fix a variance normalization for Hermitian Ornstein--Uhlenbeck diffusion and carry it without rescaling through the ordered eigenvalue process. Trace-metric matrix Brownian motion with drift $-H/2$ gives unit eigenvalue noise, unit reciprocal-gap repulsion, and ordered GUE equilibrium. Direct second-order perturbation yields the chamber generator, and its drift is one half the logarithmic gradient of the ordered GUE density. This first round closes matrix radialization, normalization, and reversibility only. We fix trace-metric Hermitian Ornstein--Uhlenbeck diffusion with drift $-H/2$ and derive, without rescaling, unit eigenvalue noise, reciprocal-gap repulsion, and the ordered GUE reversible density. The Karlin--McGregor determinant for killed independent scalar Ornstein--Uhlenbeck particles has an exact Vandermonde mass. Its shifted Doob transform is therefore conservative, has the eigenvalue generator, is reversible, and never reaches a collision wall from an interior start. This second round closes the exact transition kernel and boundary nonattainment as a complete endpoint. We carry one trace-metric variance convention from Hermitian Ornstein--Uhlenbeck matrix diffusion to its increasingly ordered eigenvalues. The resulting beta-two system has unit noise, reciprocal-gap repulsion, linear confinement, and the ordered GUE reversible law. An exact Karlin--McGregor determinant and Vandermonde mass identity produce the conservative Doob kernel and prove noncollision from every interior start. Slater determinants of probabilists' Hermite polynomials, divided by the Vandermonde, form a complete orthogonal basis indexed by partitions $\kappa$. Their generator eigenvalues are $-|\kappa|/2$, so level $k$ has multiplicity $p_N(k)$ and the sharp gap is $1/2$. This also gives exact norms, the finite partition-product heat trace, and the source Fredholm determinant for every finite $N$. The finite artifact checks 16,602 partition labels and 12 high-precision kernels only as regression evidence. Generic random-matrix structure does not pass the Route-A arithmetic gate.
author:
- 'HCS-C378 theorem package'
date: 4 September 2026
title:
- 'Beta-Two Dyson--Ornstein--Uhlenbeck Diffusion: Matrix Radialization and Ordered GUE Equilibrium'
- 'Beta-Two Dyson--Ornstein--Uhlenbeck Diffusion: Exact Chamber Kernel and Noncollision'
- 'Beta-Two Dyson--Ornstein--Uhlenbeck Diffusion: Exact Chamber Kernel and Complete Partition Spectrum'
```

## Markdown 正文

=3em

中文摘要

本文从厄米矩阵空间的迹度量出发，为奥恩斯坦乌伦贝克扩散固定唯一的方差约定， 并将该约定逐项传递到递增排列的特征值过程。 矩阵布朗运动的对角分量给出单位二次变差，非对角分量的二阶扰动则产生单位倒间隙排斥， 线性回复漂移保持负二分之一的系数。 由此得到有序腔室内的精确戴森型随机微分方程及其生成元， 没有再用矩阵元尺度或时间重参数作隐性修正。 生成元漂移恰为有序高斯酉系综密度对数梯度的一半， 因此该密度可逆；其归一化常数由完整厄米积分和酉共轭分解确定。 特别地，单维边界退化为普通一维回复过程， 而任意有限维的所有系数都由同一迹度量产生； 这说明可逆律不是按外部目标谱拟合得到的数值现象。 本轮的全部结论止于矩阵径向化、系数锁定与平衡分布。 本文在迹度量归一化下研究贝塔二戴森奥恩斯坦乌伦贝克特征值扩散。 二阶矩阵扰动给出单位噪声、倒间隙排斥和线性回复， 并确定有序高斯酉系综为可逆平衡分布。 为构造真正守恒的腔室转移核，先取相互独立的一维回复粒子在碰撞壁吸收的行列式核， 再证明其对范德蒙德函数的总质量恰好带有由次数决定的指数衰减。 补回这一能量位移后，杜布变换核质量为一， 其生成元逐项等于特征值生成元，并满足详细平衡。 由于该核在开腔室内给出全部有限时分布， 从内部出发的过程不会到达碰撞边界。 核的构造同时给出半群拼接和起始点极限， 但本文只主张从内部出发的非到达性， 不把它扩张成从碰撞壁起始的入口定律。 精确卡林麦格雷戈核、守恒变换与无碰撞定理共同构成第二轮的完整终点。 本文在一个自洽的迹度量方差约定中封闭贝塔二戴森奥恩斯坦乌伦贝克扩散。 厄米矩阵的二阶扰动严格导出单位特征值噪声、倒间隙排斥与线性回复， 有序高斯酉系综密度随之成为可逆平衡律。 独立一维回复粒子的吸收行列式核作用于范德蒙德函数时产生精确次数位移， 故能量修正后的杜布核守恒并给出全时间无碰撞边界。 在谱侧，以概率论型埃尔米特多项式组成严格递增的斯莱特行列式， 再除以范德蒙德函数，得到由分拆标记的完整正交基。 完备性来自反对称埃尔米特张量基，而非有限枚举。 本征值只依赖分拆大小，因而每层重数为限长分拆数，尖锐谱隙为二分之一； 同一计算还给出精确范数、分拆乘积热迹和源半群的弗雷德霍姆行列式。 这些对象仍是随机矩阵源系统的谱结构，没有素数、素数幂或对数素数时钟， 所以严格路线甲在算术入口即停止。

**Keywords:** Hermitian matrix diffusion; eigenvalue process; Ornstein--Uhlenbeck dynamics; ordered chamber; GUE equilibrium

关键词：厄米矩阵；特征值扩散；奥恩斯坦乌伦贝克过程；有序腔室；高斯酉系综 **Keywords:** Dyson diffusion; Karlin--McGregor kernel; Doob transform; Vandermonde function; noncollision; reversible diffusion

关键词：戴森扩散；卡林麦格雷戈核；杜布变换；范德蒙德函数；无碰撞；可逆扩散 **Keywords:** Dyson diffusion; Hermite polynomials; partition spectrum; spectral gap; heat trace; Fredholm determinant; Route A

关键词：戴森扩散；埃尔米特多项式；分拆谱；谱隙；热迹；弗雷德霍姆行列式；路线甲

# One normalization from matrix to chamber

Let $\mathrm{Herm}_N$ carry the real trace inner product $\langle A,B\rangle=\operatorname{Tr}(AB)$. Standard Brownian motion $\mathcal B_t$ in this Euclidean space drives $$\,\mathrm dH_t=\,\mathrm d\mathcal B_t-\frac12H_t\,\mathrm dt.       \label{eq:matrix-ou}$$ The trace-orthonormal basis consists of $E_{ii}$ and, for $i<j$, $$\frac{E_{ij}+E_{ji}}{\sqrt2},\qquad
 \frac{\mathrm i(E_{ij}-E_{ji})}{\sqrt2}.      \label{eq:trace-basis}$$ Thus every diagonal matrix martingale in an instantaneous eigenbasis has quadratic variation $\,\mathrm dt$, while every off-diagonal complex entry has expected squared modulus $\,\mathrm dt$. This sentence fixes the factor that is often hidden in matrix-entry conventions.

Write $$W_N=\{x\in\mathbb R^N:x_1<\cdots<x_N\},\qquad
 h(x)=\prod_{i<j}(x_j-x_i),\qquad d=\frac{N(N-1)}2.   \label{eq:chamber}$$

If $H_0$ has simple spectrum, then, up to their first collision, its increasingly ordered eigenvalues solve $$\,\mathrm dX_i=\,\mathrm dB_i+\sum_{j\ne i}\frac{\,\mathrm dt}{X_i-X_j}
             -\frac{X_i}{2}\,\mathrm dt,                  \label{eq:dyson-sde}$$ where the $B_i$ are independent standard real Brownian motions. \>0 The collision time is infinite. The generator on $W_N$ is $$\mathcal L=\frac12\sum_i\partial_i^2+
 \sum_i\left(\sum_{j\ne i}\frac1{x_i-x_j}-\frac{x_i}{2}\right)\partial_i.
                                                        \label{eq:generator}$$

For a normalized eigenvector $u_i$, second-order Hermitian perturbation gives $$\,\mathrm dX_i=\langle u_i,\,\mathrm dH\,u_i\rangle+
 \sum_{j\ne i}\frac{|\langle u_j,\,\mathrm d\mathcal B\,u_i\rangle|^2}{X_i-X_j}.
                                                        \label{eq:perturb}$$ The covariance statement following [\[eq:trace-basis\]](#eq:trace-basis){reference-type="eqref" reference="eq:trace-basis"} turns the first martingale term into $\,\mathrm dB_i$, the second-order term into the displayed reciprocal gaps, and the matrix drift into $-X_i\,\mathrm dt/2$. This proves the formula until the first collision. \>0 Section [2](#sec:doob){reference-type="ref" reference="sec:doob"} proves that this time is infinite.

The probability density $$\pi_N(x)=Z_N^{-1}\mathrm e^{-|x|^2/2}h(x)^2\,1_{W_N}(x),
 \qquad Z_N=(2\pi)^{N/2}\prod_{j=0}^{N-1}j!,          \label{eq:gue}$$ is reversible for [\[eq:generator\]](#eq:generator){reference-type="eqref" reference="eq:generator"}.

The drift is one half of the logarithmic gradient: $$\frac12\partial_i\log(\mathrm e^{-|x|^2/2}h^2)
 =-\frac{x_i}{2}+\sum_{j\ne i}\frac1{x_i-x_j}.       \label{eq:log-gradient}$$ Hence $\mathcal Lf=(2\pi_N)^{-1}\nabla\!\cdot(\pi_N\nabla f)$, where $\pi_N$ denotes its density, proving symmetry. For the normalizer, use $h=\det[\operatorname{He}_{i-1}(x_j)]$ and scalar Hermite orthogonality in Andréief's identity. The integral over $\mathbb R^N$ is $N!(2\pi)^{N/2}\prod_{j=0}^{N-1}j!$. The integrand is symmetric, so the ordered chamber contributes $1/N!$ of that value. The invariant matrix density is proportional to $\mathrm e^{-\operatorname{Tr}H^2/2}$; Weyl integration gives the same ordered density.

The $N=1$ face is ordinary scalar Ornstein--Uhlenbeck diffusion. No large-$N$ passage or entrance from a multiple eigenvalue is included.

\>0

# Killed determinant and conservative Doob transform {#sec:doob}

The independent scalar generator is $$\mathcal L_0=\frac12\sum_i(\partial_i^2-x_i\partial_i).
                                                        \label{eq:l0}$$ For $t>0$, put $r=\mathrm e^{-t/2}$ and $\sigma_t^2=1-r^2$. Its Lebesgue density is $$p_t(a,b)=\frac1{\sqrt{2\pi\sigma_t^2}}
 \exp[-\frac{(b-ra)^2}{2\sigma_t^2}].                 \label{eq:mehler}$$

The polynomial $h$ is harmonic and homogeneous of degree $d$. Consequently, $$\mathcal L_0h=-\frac d2h.                             \label{eq:h-energy}$$

The permutation-invariant Laplacian sends the alternating polynomial $h$ to an alternating polynomial of degree $d-2$. Every nonzero alternating polynomial is divisible by $h$, which already has degree $d$; hence $\Delta h=0$. Euler's homogeneous identity gives $x\cdot\nabla h=dh$. Substitution in [\[eq:l0\]](#eq:l0){reference-type="eqref" reference="eq:l0"} proves [\[eq:h-energy\]](#eq:h-energy){reference-type="eqref" reference="eq:h-energy"}.

The independent process killed at its first collision has density $$q_t(x,y)=\det[p_t(x_i,y_j)]_{i,j=1}^N.                \label{eq:km}$$ Its Vandermonde mass is $$\int_{W_N}q_t(x,y)h(y)\,\mathrm dy=r^dh(x).                 \label{eq:h-mass}$$ Therefore $$k_t(x,y)=r^{-d}\frac{h(y)}{h(x)}q_t(x,y)              \label{eq:doob}$$ is a conservative Markov density with generator [\[eq:generator\]](#eq:generator){reference-type="eqref" reference="eq:generator"}. Starting from any $x\in W_N$, its continuous diffusion never reaches a collision wall in finite time.

The reflection principle pairs every wall-hitting independent path with the path reflected after its first hit. The signed permutation sum that remains is the Karlin--McGregor determinant [\[eq:km\]](#eq:km){reference-type="eqref" reference="eq:km"}.

Both $q_t(x,\cdot)$ and $h$ are alternating. Their product is symmetric, so the chamber integral in [\[eq:h-mass\]](#eq:h-mass){reference-type="eqref" reference="eq:h-mass"} is $1/N!$ of the full-space integral. Write $h(y)=\det[y_j^{i-1}]$. Andréief's identity gives $$\int_{\mathbb R^N}q_t(x,y)h(y)\,\mathrm dy
 =N!\det[\int_{\mathbb R}p_t(x_i,y)y^{j-1}\,\mathrm dy]_{i,j=1}^N.
                                                        \label{eq:andreief}$$ The $(j-1)$st moment of $N(rx_i,1-r^2)$ is a degree-$(j-1)$ polynomial in $x_i$ with leading coefficient $r^{j-1}$. Lower-degree column operations reduce the determinant in [\[eq:andreief\]](#eq:andreief){reference-type="eqref" reference="eq:andreief"} to $r^{0+\cdots+(N-1)}h(x)=r^dh(x)$. This proves [\[eq:h-mass\]](#eq:h-mass){reference-type="eqref" reference="eq:h-mass"}.

Equation [\[eq:h-mass\]](#eq:h-mass){reference-type="eqref" reference="eq:h-mass"} makes [\[eq:doob\]](#eq:doob){reference-type="eqref" reference="eq:doob"} conservative. On smooth compactly supported functions, $$h^{-1}\mathcal L_0(hf)+\frac d2f
 =\mathcal L_0f+\nabla\log h\cdot\nabla f=\mathcal Lf, \label{eq:conjugacy}$$ because $\partial_i\log h=\sum_{j\ne i}(x_i-x_j)^{-1}$. The minimal transformed process has mass one at every finite time. A boundary hit by a continuous chamber path would be its killing time, so conservativity excludes such a hit. Local uniqueness before collision and the standard electrostatic-repulsion theorem identify the transform with the unique global strong solution of [\[eq:dyson-sde\]](#eq:dyson-sde){reference-type="eqref" reference="eq:dyson-sde"}.

Scalar detailed balance in [\[eq:mehler\]](#eq:mehler){reference-type="eqref" reference="eq:mehler"} passes through the determinant; the two Vandermonde factors in [\[eq:doob\]](#eq:doob){reference-type="eqref" reference="eq:doob"} then prove $\pi_N(x)k_t(x,y)=\pi_N(y)k_t(y,x)$ directly. This independently checks the generator calculation.

\>1

# Complete symmetric-Hermite spectrum

Let $\kappa=(\kappa_1\geq\cdots\geq\kappa_N\geq0)$ be a partition and define $$m_i=\kappa_{N+1-i}+i-1.                              \label{eq:m-index}$$ Then $m_{i+1}-m_i=1+\kappa_{N-i}-\kappa_{N+1-i}\geq1$ and $\sum_i m_i=d+|\kappa|$. With monic probabilists' Hermites, set $$D_m(x)=\det[\operatorname{He}_{m_i}(x_j)]_{i,j=1}^N,
 \qquad \Phi_\kappa(x)=\frac{D_m(x)}{h(x)}.            \label{eq:phi}$$ The quotient is a symmetric polynomial because every alternating polynomial is divisible by $h$.

The family $\{\Phi_\kappa\}$ is a complete orthogonal basis of $L^2(W_N,\pi_N)$ and $$\begin{aligned}
 \mathcal L\Phi_\kappa&=-\frac{|\kappa|}{2}\Phi_\kappa,
                                                        \label{eq:eigen}\\
 \|\Phi_\kappa\|_{L^2(\pi_N)}^2
 &=\frac{\prod_{i=1}^N m_i!}{\prod_{j=0}^{N-1}j!}.     \label{eq:norm}\end{aligned}$$ Thus $-k/2$ has multiplicity $p_N(k)$, the number of partitions of $k$ with at most $N$ parts.

The scalar equation $$\frac12(\operatorname{He}_n''-x\operatorname{He}_n')
 =-\frac n2\operatorname{He}_n                           \label{eq:hermite}$$ and determinant expansion give $\mathcal L_0D_m=-(\sum_i m_i)D_m/2$. Apply [\[eq:conjugacy\]](#eq:conjugacy){reference-type="eqref" reference="eq:conjugacy"} to $D_m=h\Phi_\kappa$ and subtract the filled-ground energy $d/2$ to obtain [\[eq:eigen\]](#eq:eigen){reference-type="eqref" reference="eq:eigen"}.

Scalar Hermites form a complete Gaussian $L^2(\mathbb R)$ basis. Their antisymmetrized tensor products $D_m$, indexed by strictly increasing $m$, therefore form a complete basis of the antisymmetric Gaussian sector on $\mathbb R^N$. Multiplication by $h$, followed by antisymmetric extension from $W_N$, identifies this sector with $L^2(W_N,\pi_N)$ up to a fixed scalar. Division by $h$ transfers the complete Slater basis to [\[eq:phi\]](#eq:phi){reference-type="eqref" reference="eq:phi"}; this is the step that rules out missing nonpolynomial $L^2$ spectrum.

Finally, Andréief and scalar Hermite orthogonality give $$\int_{\mathbb R^N}D_mD_n\mathrm e^{-|x|^2/2}\,\mathrm dx
 =\delta_{mn}N!(2\pi)^{N/2}\prod_i m_i!.              \label{eq:slater-norm}$$ Divide by $N!$ for the chamber and by $Z_N$ to obtain [\[eq:norm\]](#eq:norm){reference-type="eqref" reference="eq:norm"}. Equation [\[eq:m-index\]](#eq:m-index){reference-type="eqref" reference="eq:m-index"} bijects partitions with strict indices above $(0,1,\ldots,N-1)$, proving the multiplicity.

For $\int f\,\mathrm d\pi_N=0$, $$\|P_tf\|_2\leq\mathrm e^{-t/2}\|f\|_2,
 \qquad
 \operatorname{Var}_{\pi_N}(f)\leq\int_{W_N}|\nabla f|^2\,\mathrm d\pi_N.   \label{eq:poincare}$$ Both constants are sharp. For $t>0$, $$\begin{aligned}
 \operatorname{Tr}P_t&=\prod_{j=1}^N(1-\mathrm e^{-jt/2})^{-1},            \label{eq:trace}\\
 \det(I-zP_t)&=\prod_{k=0}^{\infty}
 (1-z\mathrm e^{-kt/2})^{p_N(k)}.                            \label{eq:fredholm}\end{aligned}$$

Theorem 4 has a simple zero level and first nonzero decay exponent $1/2$. The function $x_1+\cdots+x_N$ lies in that first eigenspace, proving sharpness. The partition generating function $\sum_\kappa q^{|\kappa|}=\prod_{j=1}^N(1-q^j)^{-1}$ with $q=\mathrm e^{-t/2}$ proves [\[eq:trace\]](#eq:trace){reference-type="eqref" reference="eq:trace"}. The finite value of the trace makes $P_t$ trace class, and its eigenvalue product gives [\[eq:fredholm\]](#eq:fredholm){reference-type="eqref" reference="eq:fredholm"}. This determinant belongs only to the source semigroup.

# Oscillator transform, exact receipt, and Route A

The equilibrium square root without its constant is $\psi_0=\mathrm e^{-|x|^2/4}h$. Direct differentiation, using $\Delta h=0$ and $x\cdot\nabla h=dh$, gives $$-\psi_0\mathcal L\psi_0^{-1}
 =-\frac12\Delta+\frac{|x|^2}{8}-\frac N4-\frac d2.    \label{eq:oscillator}$$ This acts on the antisymmetric Dirichlet sector; the inverse-square Calogero term cancels at beta two. It explains the filled Slater sea but is only a source-local operator equivalence.

The canonical receipt records 16 matrix dimensions, 1,040 level multiplicities, all 16,602 partitions through $N=8$ and degree 24, and 12 high-precision kernels. An independent checker reconstructs every exact row and uses a Leibniz determinant. SymPy performs 350 exact identities. These finite checks are regression evidence, not the proof of the all-$N$ theorem.

Dyson owns the eigenvalue Brownian-motion lineage [@Dyson]; Karlin--McGregor and Grabiner own the determinant/reflection lineage [@KM; @Grabiner]; Cépa--Lépingle supply strong noncollision context [@CL]; and Baker--Forrester place generalized Hermites in the Calogero--Sutherland setting [@BF]. The nearest registry owners are a deterministic Calogero--Moser scattering system, a scalar Jacobi diffusion, a hypoelliptic Kramers process, and finite discrete killed walkers. None is the continuous conservative eigenvalue diffusion closed here.

The strict assessment is $$(A0_{\rm fail},A1_{\rm fail},A2_{\rm fail},A3_{\rm fail},
 A4_{\rm formal\ hint}),\qquad \text{overall: Route A rejected}. \label{eq:route}$$ The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`. Generic GUE statistics are not arithmetic origin. We assert no target arithmetic local data, Euler factor, root number, automorphy, target divisor or counting law, target functional equation, target-zero match, Hilbert--Pólya operator, or Route B. In particular, [\[eq:oscillator\]](#eq:oscillator){reference-type="eqref" reference="eq:oscillator"} is not promoted to a target spectral realization.

9 F. J. Dyson, "A Brownian-Motion Model for the Eigenvalues of a Random Matrix," *J. Math. Phys.* 3 (1962), 1191--1198, [DOI record](https://doi.org/10.1063/1.1703862). S. Karlin and J. McGregor, "Coincidence probabilities," *Pacific J. Math.* 9 (1959), 1141--1164, [DOI record](https://doi.org/10.2140/pjm.1959.9.1141). E. Cépa and D. Lépingle, "Diffusing particles with electrostatic repulsion," *Probab. Theory Relat. Fields* 107 (1997), 429--449, [DOI record](https://doi.org/10.1007/s004400050092). D. J. Grabiner, "Brownian motion in a Weyl chamber, non-colliding particles, and random matrices," *Ann. Inst. H. Poincaré Probab. Statist.* 35 (1999), 177--204. T. H. Baker and P. J. Forrester, "The Calogero--Sutherland Model and Generalized Classical Polynomials," *Commun. Math. Phys.* 188 (1997), 175--216, [DOI record](https://doi.org/10.1007/s002200050161).

round zero matrix radialization and reversible GUE density round one determinant Doob kernel and no collision round two complete partition spectrum and Route A closure
