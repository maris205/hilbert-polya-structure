---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-flat-magnetic-torus-landau-route-a"
canonical_tex: "henon_dynamics/henon_flat_magnetic_torus_landau_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_flat_magnetic_torus_landau_route_a/paper/main.pdf"
source_sha256: "0ac912474a7c9497ade0ae2a782e19a0c674cea42fc68b5baea3d38d1e4a08c2"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Charged Particle on a Flat Magnetic Torus: Clean Cyclotron Return and Sharp Flux Quantization

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_flat_magnetic_torus_landau_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_flat_magnetic_torus_landau_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_flat_magnetic_torus_landau_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_flat_magnetic_torus_landau_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close, in one normalization, the classical and quantum dynamics of a charged unit-mass particle on a rectangular flat two-torus with nonzero constant magnetic field. Every positive-energy classical trajectory has least period $2\pi/|B|$; each return is maximally clean, whereas no other time fixes a point of an energy shell. The cyclotron center identifies the orbit quotient as a two-torus. A quantum line bundle with curvature $-\mathrm iB\,\mathrm dx\wedge\,\mathrm dy$ exists precisely at integral flux $N=BL_xL_y/(2\pi)$. Necessity follows from Chern--Weil theory and sufficiency from an explicit rectangle cocycle. This first round closes the global classical return and topological existence questions only. We fix one normalization for a charged unit-mass particle on a rectangular flat two-torus. At nonzero field, every positive-energy classical orbit has least period $2\pi/|B|$, and every return is maximally clean. Curvature $-\mathrm iB\,\mathrm dx\wedge\,\mathrm dy$ admits a Hermitian line bundle exactly when $N=BL_xL_y/(2\pi)$ is integral. On that bundle the physical Bochner Hamiltonian has levels $|B|(n+1/2)$, each with multiplicity $|N|$ for every flat holonomy. For the fixed positively oriented division vectors, the magnetic translations obey $UV=\zeta_{|N|}^{\operatorname{sgn}N}VU$; hence negative flux carries the conjugate clock--shift representation rather than an erased sign. This round proves the clean return, global quantization, complete Landau ladder, and signed finite-Heisenberg action. We close, in one normalization, the classical and quantum dynamics of a charged unit-mass particle on a rectangular flat two-torus with nonzero constant magnetic field. Every positive-energy classical trajectory has least period $2\pi/|B|$, and each return is maximally clean. Quantum curvature $-\mathrm iB\,\mathrm dx\wedge\,\mathrm dy$ exists globally precisely at integral flux $N=BL_xL_y/(2\pi)$. The physical Bochner Hamiltonian has levels $|B|(n+1/2)$ of multiplicity $|N|$; fixed positive division vectors retain the field orientation through $UV=\zeta_{|N|}^{\operatorname{sgn}N}VU$. We derive the heat trace, Hurwitz spectral zeta, scale-independent determinant $\det_\zeta H_B=2^{|N|/2}$, and two distinct least times: one classical period gives the scalar $-I$, whereas two give the identity. The boundary atlas includes the exact lattice-normalized zero-field closure criterion. Topological flux integrality is not arithmetic provenance, so the strict Route-A tuple begins with A0 fail and the candidate is rejected.
author:
- 'HCS-C376 theorem package'
date: 4 September 2026
title:
- 'A Charged Particle on a Flat Magnetic Torus: Clean Cyclotron Return and Sharp Flux Quantization'
- 'A Charged Particle on a Flat Magnetic Torus: Clean Return, Flux Quantization, and Signed Landau Multiplets'
- 'A Charged Particle on a Flat Magnetic Torus: Clean Cyclotron Return, Landau Multiplets, and Two Revival Times'
```

## Markdown 正文

=3em

中文摘要

本文在同一套符号和物理单位中研究矩形平坦二环面上的恒定磁场运动。 经典部分不从局部轨道猜测周期，而是在普适覆盖上直接积分方程： 动量作匀速旋转，回旋中心保持不变，位置由同一旋转精确重建。 由此证明任意正能量轨道的最小相空间周期均为二派除以磁场绝对值； 非返回时刻没有不动点，返回时刻整个能量层连同其切空间同时固定， 因此所得周期族是最大干净的连续族，其轨道商仍为二环面。 量子存在性则由全局拓扑决定。 对曲率负虚数乘以磁场面积形式的厄米线丛，第一陈数恰为磁通除以二派； 只有该数为整数时对象存在。必要性来自陈类积分， 充分性由基本矩形上的显式过渡函数给出。 本轮只封闭经典回归与磁通量子化，不预告后续谱结论。 本文统一处理平坦磁二环面的经典回归、全局量子化和朗道能级。 经典方程在普适覆盖上可完全积分，守恒回旋中心把所有正能量轨道锁定到共同的最小周期， 并说明返回映射在整个能量层上都是恒等，从而得到最大干净而非孤立的周期族。 曲率积分给出有符号磁通整数，它既是线丛存在的充要条件，也是线丛次数； 任意平坦荷洛诺米只改变连接而不改变能谱。 采用带零点半位移的正博赫纳哈密顿量后， 升降算符与亏格一的黎曼罗赫定理共同给出完整等距能级及每层磁通绝对值重简并。 为避免抹去负磁通，本文固定正向的两条细分格矢， 证明磁平移交换相位为单位根的磁通符号次幂， 并在每个能级上构造相应的共轭钟移表示。 本轮止于完整朗道阶梯和有符号有限海森堡作用。 本文在固定物理归一化下封闭恒定磁场中矩形平坦二环面的经典与量子动力学。 经典解由刚性动量旋转和守恒回旋中心组成， 因此每条正能量轨道都有共同最小周期，且返回映射在整个能量层上为恒等； 这是一族最大干净轨道而非孤立周期点。 量子对象存在当且仅当总磁通给出整数第一陈数。 正博赫纳哈密顿量的升降代数和环面黎曼罗赫定理给出带零点半位移的全部朗道能级及磁通绝对值重简并。 固定正向细分格矢后，磁平移交换相位保留磁通符号，负磁场对应共轭钟移表示。 由完整谱进一步求得热迹、赫维茨谱泽塔、与磁场尺度无关的泽塔行列式， 并严格区分一个经典周期产生的负恒等标量复现和两个周期产生的真正恒等复现。 边界分析还给出零场直线流按环面格矢归一化的闭轨条件， 分别处理轴向、静止与稠密情形。 最后指出陈数整数性属于拓扑而非素数算术，故严格路线甲判据在首道算术门即失败。

**Keywords:** magnetic torus; cyclotron flow; clean return; flux quantization; line bundle

关键词：磁环面；回旋流；干净回归；磁通量子化；线丛 **Keywords:** magnetic torus; Bochner Laplacian; Landau levels; flux quantization; magnetic translations; finite Heisenberg group

关键词：磁环面；博赫纳拉普拉斯；朗道能级；磁通量子化；磁平移；有限海森堡群 **Keywords:** magnetic torus; Landau levels; magnetic translations; spectral zeta; zeta determinant; quantum revival; Route A

关键词：磁环面；朗道能级；磁平移；谱泽塔；泽塔行列式；量子复现；路线甲

# Classical magnetic flow

Let $$\mathbb T^2=\mathbb R^2/(L_x\mathbb Z\oplus L_y\mathbb Z),\qquad A=L_xL_y,$$ where $L_x,L_y>0$. On $T^*\mathbb T^2$ use lifted coordinates $(q,p)=(x,y,p_x,p_y)$ and the twisted form and Hamiltonian $$\omega_B=\,\mathrm dx\wedge\,\mathrm dp_x+\,\mathrm dy\wedge\,\mathrm dp_y
       +B\,\mathrm dx\wedge\,\mathrm dy,
 \qquad H_{\rm cl}=\tfrac12|p|^2.                 \label{eq:classical}$$ Fix $B\ne0$ and write $J(u,v)=(-v,u)$. Our Hamiltonian convention gives $$\dot q=p,\qquad \dot p=BJp.                     \label{eq:lorentz}$$

[\[thm:classical\]]{#thm:classical label="thm:classical"} On every energy shell $\Sigma_E=\{H_{\rm cl}=E\}$ with $E>0$, every orbit has the same least period $$T_{\rm cl}=\frac{2\pi}{|B|}.$$ For $t\notin T_{\rm cl}\mathbb Z$, $\operatorname{Fix}(\Phi_t|_{\Sigma_E})$ is empty. For $t\in T_{\rm cl}\mathbb Z$, the return is the identity and $$\operatorname{Fix}(\Phi_t|_{\Sigma_E})=\Sigma_E,\qquad
 \ker(D\Phi_t-I)=T\Sigma_E.$$ Thus every nonzero return is maximally clean. The orbit space of the circle action on $\Sigma_E\cong\mathbb T^2\times S^1$ is a two-torus.

Let $R_\theta=\exp(\theta J)$. Direct integration of [\[eq:lorentz\]](#eq:lorentz){reference-type="eqref" reference="eq:lorentz"} gives $$p(t)=R_{Bt}p_0,\qquad
 c=q+\frac{Jp}{B}=q_0+\frac{Jp_0}{B},\qquad
 q(t)=c-\frac{J R_{Bt}p_0}{B}.                   \label{eq:solution}$$ This formula is well defined after reducing $q$ modulo the lattice and proves completeness. Since $E>0$, $p_0\ne0$. A phase-space return forces $R_{Bt}p_0=p_0$, hence $Bt\in2\pi\mathbb Z$; the position then returns as well. This proves both the period and its minimality. At an integral multiple of $T_{\rm cl}$, formula [\[eq:solution\]](#eq:solution){reference-type="eqref" reference="eq:solution"} is the identity for all initial data, so its derivative is the identity. At every other time its rotation has no nonzero fixed momentum. These two observations give the stated fixed sets and clean tangent equality. Finally $c$ modulo the lattice labels an orbit, proving the quotient assertion.

#### Geometric meaning.

The continuous center $c$ is the classical accidental symmetry. Compact configuration does not isolate trajectories: at a return time the entire three-dimensional energy shell is fixed. This fact is decisive for the Route-A verdict below.

# Flux integrality and the quantum object

We use units $\hbar=q_{\rm charge}=m=1$. A quantum magnetic field means a Hermitian line bundle $\mathcal L\to\mathbb T^2$ with unitary connection $\nabla$ whose curvature is $$F_\nabla=-\mathrm iB\,\mathrm dx\wedge\,\mathrm dy.                \label{eq:curvature}$$

[\[thm:flux\]]{#thm:flux label="thm:flux"} A pair $(\mathcal L,\nabla)$ satisfying [\[eq:curvature\]](#eq:curvature){reference-type="eqref" reference="eq:curvature"} exists if and only if $$N=\frac{BA}{2\pi}\in\mathbb Z.                        \label{eq:flux}$$ Its degree is $N$. For a fixed $N$, tensoring by a flat line bundle gives the two holonomy parameters and does not change the curvature.

Chern--Weil theory gives $$c_1(\mathcal L)[\mathbb T^2]=\frac{\mathrm i}{2\pi}
 \int_{\mathbb T^2}F_\nabla=\frac{BA}{2\pi},$$ which proves necessity. Conversely, for $N\in\mathbb Z$ take on the fundamental rectangle the gauge $A_y=Bx$, $A_x=0$. Identify the vertical sides trivially and identify $x=L_x$ with $x=0$ by the unitary multiplier $\exp(\mathrm iBL_xy)$. Its change around the horizontal cycle is $\exp(\mathrm iBA)=\exp(2\pi\mathrm iN)=1$, so the corner cocycle closes and defines the required bundle and connection. Multiplying the two gluing maps by constant phases produces all flat holonomy twists.

*Round-zero certificate: round zero proves complete clean classical return and the sharp global flux condition.*

\>0

# Bochner Landau ladder

Put $\Pi_j=-\mathrm i\nabla_j$. Equations [\[eq:curvature\]](#eq:curvature){reference-type="eqref" reference="eq:curvature"} and [\[eq:flux\]](#eq:flux){reference-type="eqref" reference="eq:flux"} give $$=\mathrm iB,
 \qquad H_B=\tfrac12(\Pi_x^2+\Pi_y^2)=\tfrac12\nabla^*\nabla. \label{eq:HB}$$ This physical Bochner normalization is important: it includes the zero-point half-shift and is not the unshifted Dolbeault number operator.

Assume $N\ne0$. The self-adjoint elliptic operator [\[eq:HB\]](#eq:HB){reference-type="eqref" reference="eq:HB"} has $$\operatorname{Spec}(H_B)=
 \{E_n=|B|(n+\tfrac12):n\in\mathbb Z_{\ge0}\}.         \label{eq:levels}$$ Every $E_n$ has multiplicity $|N|$. The level locations and multiplicities are independent of both flat holonomies.

It is enough to take $B>0$; negative field is obtained by complex conjugation and interchange of chirality. Define $$a=\frac{\Pi_x+\mathrm i\Pi_y}{\sqrt{2B}},\qquad
 a^*=\frac{\Pi_x-\mathrm i\Pi_y}{\sqrt{2B}}.$$ Then $[a,a^*]=1$ and $$H_B=B(a^*a+\tfrac12),\qquad [H_B,a]=-Ba.         \label{eq:ladder}$$ In the complex structure of the rectangular torus, $\ker a$ is the space of holomorphic sections of the positive degree-$N$ bundle. Riemann--Roch on a genus-one curve and vanishing for the inverse negative-degree bundle give $\dim\ker a=N$, for every flat twist.

The compact elliptic operator has discrete spectrum. Repeated application of $a$ to an eigenvector must terminate, because [\[eq:ladder\]](#eq:ladder){reference-type="eqref" reference="eq:ladder"} lowers energy by $B$ while $H_B\ge B/2$. It terminates in $\ker a$, so every eigenvalue is one of [\[eq:levels\]](#eq:levels){reference-type="eqref" reference="eq:levels"}. Conversely $(a^*)^n$ takes $\ker a$ injectively onto the $n$th level; the lowering argument makes it surjective. Hence every multiplicity equals $N$. Complex conjugation replaces this by $|N|$ when $B<0$.

# Finite magnetic translations

Let $M=|N|$, $\sigma=\operatorname{sgn}N$, and $\zeta_M=\exp(2\pi\mathrm i/M)$. Fix the positively oriented ordered $M$-division vectors $(L_x/M,0)$ and $(0,L_y/M)$. Their translations lift projectively to the magnetic bundle. After harmless scalar rephasings, call the corresponding lifts $U,V$.

On every Landau eigenspace one can choose an orthonormal basis $e_0,\ldots,e_{M-1}$, with indices modulo $M$, such that $$Ue_j=e_{j+1},\qquad Ve_j=\zeta_M^{-\sigma j}e_j,
 \qquad U^M=V^M=I,\qquad UV=\zeta_M^\sigma VU.  \label{eq:clockshift}$$ For $M>1$ this representation is irreducible; for $M=1$ it is the trivial one-dimensional boundary case. Flat holonomies change the lifts by phases, not the commutator or the Landau data.

The bundle cocycle in Theorem [\[thm:flux\]](#thm:flux){reference-type="ref" reference="thm:flux"} makes the commutator of the two fixed-orientation lifted division translations equal to the exponential of the flux through one $M$-by-$M$ cell. Since $$\frac{BA}{M^2}=\frac{2\pi N}{M^2}=\frac{2\pi\sigma}{M},$$ this phase is $\zeta_M^\sigma$; in particular, negative flux cannot be removed by scalar rephasing. Rephasing does make both $M$th powers the identity. They commute with $H_B$, hence act on each eigenspace. Diagonalize $V$. The commutator cycles its $M$ distinct characters, yielding [\[eq:clockshift\]](#eq:clockshift){reference-type="eqref" reference="eq:clockshift"}. Since the eigenspace has dimension $M$, the cycle is a basis and any invariant subspace containing one character contains all. The raising operator intertwines the action, so the same model occurs on every level.

*Round-one certificate: round one adds the complete Bochner Landau ladder, exact multiplicity, holonomy rigidity, and the finite magnetic-translation representation.*

\>1

# Heat trace, spectral zeta, and determinant

[\[thm:zeta\]]{#thm:zeta label="thm:zeta"} For $\beta>0$ and initially for $\Re s>1$, $$\begin{aligned}
 \operatorname{Tr}(\mathrm e^{-\beta H_B})
   &=M\frac{\mathrm e^{-\beta|B|/2}}{1-\mathrm e^{-\beta|B|}}, \label{eq:heat}\\
 \zeta_{H_B}(s)
   &=M|B|^{-s}\zeta(s,\tfrac12)
     =M|B|^{-s}(2^s-1)\zeta(s).                 \label{eq:zeta}\end{aligned}$$ The meromorphic continuation is regular at zero and $$\zeta_{H_B}(0)=0,\qquad
 \zeta'_{H_B}(0)=-\frac{M}{2}\log2,\qquad
 \det_{\zeta}H_B=2^{M/2}.                       \label{eq:det}$$ In particular, the zeta determinant is independent of $|B|$ once the flux multiplicity $M$ is fixed.

Insert [\[eq:levels\]](#eq:levels){reference-type="eqref" reference="eq:levels"} with multiplicity $M$. The heat sum is geometric, giving [\[eq:heat\]](#eq:heat){reference-type="eqref" reference="eq:heat"}; the Dirichlet sum gives the first equality in [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}. Separating the odd positive integers proves $\zeta(s,1/2)=(2^s-1)\zeta(s)$ and supplies the continuation. The standard Hurwitz values $$\zeta(0,a)=\tfrac12-a,\qquad
 \zeta'(0,a)=\log\Gamma(a)-\tfrac12\log(2\pi)$$ give $\zeta(0,1/2)=0$ and $\zeta'(0,1/2)=-(\log2)/2$. Differentiating the factor $|B|^{-s}$ contributes nothing because the value at zero vanishes. Finally use $\det_\zeta H_B=\exp[-\zeta'_{H_B}(0)]$.

#### Interpretive boundary.

Equation [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} is a source spectral zeta. This paper gives it no dynamical-determinant, Euler-product, or target-function interpretation.

# Two exact revival times

[\[thm:revival\]]{#thm:revival label="thm:revival"} The least positive time at which the propagator is a scalar is $$T_{\rm scalar}=\frac{2\pi}{|B|}=T_{\rm cl},
 \qquad \mathrm e^{-\mathrm iT_{\rm scalar}H_B}=-I.$$ The least positive identity time is $$T_{\rm identity}=\frac{4\pi}{|B|}=2T_{\rm cl},
 \qquad \mathrm e^{-\mathrm iT_{\rm identity}H_B}=I.$$

The ratio of phases on adjacent levels is $\exp(-\mathrm i|B|t)$. A scalar propagator therefore requires and, by [\[eq:levels\]](#eq:levels){reference-type="eqref" reference="eq:levels"}, is implied by $|B|t\in2\pi\mathbb Z$. At the least positive such time the $n$th phase is $\exp[-2\pi\mathrm i(n+1/2)]=-1$. At scalar times $2\pi k/|B|$, this common phase is $(-1)^k$, so the least identity occurs at $k=2$.

# Boundary atlas

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  face                 exact status
  -------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  $E>0$, $B\ne0$       Theorem [\[thm:classical\]](#thm:classical){reference-type="ref" reference="thm:classical"}; all orbits have the common least period and form a clean family.

  $E=0$, $B\ne0$       $p=0$ gives the zero-section of stationary classical points. Quantum mechanics still has positive ground energy $|B|/2$.

  $N>0$ versus $N<0$   Reversing $B$ reverses classical orientation and complex-conjugates quantum chirality; energies and multiplicities use $|B|$ and $|N|$, while fixed positive division vectors give conjugate commutator phases $\zeta_M^{\pm1}$.

  $|N|=1$              Every Landau level is simple and the finite Heisenberg action is one-dimensional; all spectral formulas remain valid.

  $N\notin\mathbb Z$   The classical twisted flow remains valid, but no global Hermitian line bundle has the stipulated curvature.

  $B=0$                Classical motion is $q(t)=q_0+tp$ modulo the lattice and closes iff $p_xt\in L_x\mathbb Z$ and $p_yt\in L_y\mathbb Z$ for some $t>0$. For $p_xp_y\ne0$ this is equivalent to $p_yL_x/(p_xL_y)\in\mathbb Q$; nonzero axial motion closes, while $p=0$ is stationary and has no positive least period. A nonaxial irrational normalized ratio gives a dense orbit. The quantum object becomes a flat-holonomy shifted torus Laplacian, not a zero-field continuation of the Landau multiplicity theorem.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Route-A closure and reproducibility

The strict tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},
  \mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
  \mathrm{A4\_NATURAL\_QUANTIZATION}),$$ so the overall verdict is `ROUTE_A_REJECTED`. Flux integrality is a genuine source topological condition, but topology alone is not arithmetic provenance and supplies no rational-prime data, prime-power repetition, or logarithmic-prime clock; consequently A0 fails. The classical returns are continuous clean families, and the exact Hurwitz zeta is not a dynamical determinant. No target continuation or zero correspondence is asserted. Route B is locked.

The companion artifact checks 256 exact classical cells, 16,512 Landau labels, 4,160 signed clock--shift basis cells, 1,024 heat cells, 64 determinant controls, 129 revival phases, and every listed boundary. Producer, independent checker, symbolic cross-check, byte replay, hostile mutation, and PDF gates are separate. These computations audit formula transcription; the proofs above carry the infinite statements. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.

*Round-two certificate: round two adds exact heat and Hurwitz zeta closure, the zeta determinant, both least revival times, the full boundary atlas, and the strict Route-A stop.*

# Source and ownership note {#source-and-ownership-note .unnumbered}

The torus magnetic-translation source is M. H. Al-Hashimi and U.-J. Wiese, *Annals of Physics* 324 (2009), 343--360, doi:10.1016/j.aop.2008.07.006, arXiv:0807.0630. E. Onofri, *International Journal of Theoretical Physics* 40 (2001), 537--549, doi:10.1023/A:1004115827959, arXiv:quant-ph/0007055, treats the finite-volume Landau-level subtlety. I. Burban and S. Klevtsov, *Communications in Mathematical Physics* 406 (2025), article 97, doi:10.1007/s00220-025-05267-9, provides modern line-bundle and finite-Heisenberg context. Its holomorphic ground-space normalization is not substituted for the physical Bochner half-shift used here. Nearby repository owners cover the Penning trap, hyperbolic and Grushin magnetic systems, the spherical Dirac monopole, and Harper lattice dynamics. This package claims only the displayed joint flat-torus closure, not global literature novelty and not ownership of its standard ingredients.
