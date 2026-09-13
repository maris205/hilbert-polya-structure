---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-open-walsh-phase-equidistribution-route-a"
canonical_tex: "henon_dynamics/henon_open_walsh_phase_equidistribution_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_open_walsh_phase_equidistribution_route_a/paper/main.pdf"
source_sha256: "f2904b08d06bc35178e98a3ba05d3f60bde6b220e172974a78f176991e03646f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Haar Phase Equidistribution for a Full-Cycle Open Walsh Gate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_open_walsh_phase_equidistribution_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_open_walsh_phase_equidistribution_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_open_walsh_phase_equidistribution_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_open_walsh_phase_equidistribution_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We retain the frozen three-symbol open Walsh gate studied at the full register cycle and resolve the phase question left open by its log-modulus law. The two surviving one-site eigenphases have ratio $r=e^{i\delta}$. We derive $2\cos\delta=(\sqrt3-\sqrt{111})/6$ and prove that its primitive irreducible integer polynomial is $3x^4-19x^2+27$, while its monic rational minimal polynomial is $x^4-(19/3)x^2+9$. The nonintegral coefficient excludes algebraic integrality, so $r$ cannot be a root of unity. The full-cycle phase measure is a multiplicity-weighted binomial walk on the circle. Its $m$th Fourier coefficient is exactly $u_-^{mk}((1+r^m)/2)^k$, so every nonzero fixed mode decays exponentially and the measures converge weakly to Haar measure. Jointly, the centered $\sqrt{k}$ log-modulus fluctuation and phase converge to a product Gaussian--Haar law. A moved-hole control realizes the complementary order-four torsion branch. The theorem concerns only the source-side subunitary scattering gate and gives no self-adjoint or target-spectrum construction.
author:
- 'Route-A structural certificate C163'
title: 'Haar Phase Equidistribution for a Full-Cycle Open Walsh Gate'
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** open quantum maps; Walsh dynamics; phase equidistribution; Haar measure; algebraic integers; Fourier coefficients.

chinese-simplified

中文摘要

本文保持三符号开放 [Walsh]{lang="en"} 门及完整寄存器周期不变，解决此前模长定理遗留的相位问题。两个非零单点特征值的单位相位之比记为 $r=e^{i\delta}$。我们精确推出 $2\cos\delta=(\sqrt3-\sqrt{111})/6$，并证明其本原不可约整系数多项式为 $3x^4-19x^2+27$，而首一有理极小多项式为 $x^4-(19/3)x^2+9$。后者含非整数系数，故 $2\cos\delta$ 不是代数整数，从而 $r$ 不可能是单位根。完整周期的相位测度是圆周上的二项乘法游走，其第 $m$ 个傅里叶系数恰为 $u_-^{mk}((1+r^m)/2)^k$。每个非零固定模态均指数衰减，因此测度弱收敛到圆周 [Haar]{lang="en"} 测度。进一步，中心化的 $\sqrt{k}$ 对数模涨落与相位联合收敛到高斯与 [Haar]{lang="en"} 测度的乘积律。移动孔洞对照实现互补的四阶有限子群分支。结论只属于源侧次酉散射门，不构造自伴算子或目标谱。

关键词：开放量子映射；[Walsh]{lang="en"} 动力学；相位等分布；[Haar]{lang="en"} 测度；代数整数；傅里叶系数。

# Frozen gate and algebraic obstruction

Let $A=F_3^*\operatorname{diag}(1,0,1)$ and let $B_k$ be the frozen cyclic register shift. One full cycle is $C_k=B_k^k=A^{\otimes k}$. The two nonzero roots of $$\lambda^2-\tau\lambda+q=0,\qquad
 \tau=\frac{\sqrt3}{6}-\frac i2,\quad
 q=-\frac12-\frac{\sqrt3 i}{6},$$ are labelled by $|\lambda_+|>|\lambda_-|$. Put $u_\pm=\lambda_\pm/|\lambda_\pm|$ and $r=u_+/u_-=e^{i\delta}$.

#### Lemma 1.

$c=r+r^{-1}=2\cos\delta=(\sqrt3-\sqrt{111})/6$ is not an algebraic integer; in particular $r$ is not a root of unity.

#### Proof.

The exact one-site invariants are $|\tau|^2=1/3$, $|\lambda_+|^2+|\lambda_-|^2=(1+\sqrt{37})/6$, and $|\lambda_+\lambda_-|=1/\sqrt3$. Expanding $|\lambda_++\lambda_-|^2$ gives the formula for $c$, and $$c^2=\frac{19-\sqrt{37}}6,\qquad 3c^4-19c^2+27=0.$$ The polynomial of $c^2$ has discriminant $37$. Also $c\notin\mathbb Q(\sqrt{37})$, since otherwise its radical expression would put $\sqrt3$ in that distinct quadratic field. Hence the displayed primitive integer quartic is irreducible. Dividing by $3$ gives the monic rational minimal polynomial $x^4-(19/3)x^2+9$, whose coefficient $-19/3$ is not integral. An algebraic integer has its monic rational minimal polynomial in $\mathbb Z[x]$. If $r$ were a root of unity, $r+r^{-1}$ would be an algebraic integer, a contradiction. $\square$

# All-length Fourier law

Sampling the nonzero spectrum of $C_k$ with algebraic-multiplicity weight gives $$\mu_k=2^{-k}\sum_{j=0}^k{\binom kj}\delta_{u_-^k r^j}.$$

#### Theorem 2.

For every $m\in\mathbb Z$, $$\widehat\mu_k(m)=u_-^{mk}\left(\frac{1+r^m}{2}\right)^k.       \tag{1}$$ Thus $\mu_k$ converges weakly to normalized Haar measure on $\mathbb T$.

#### Proof.

Equation (1) is the binomial theorem. Lemma 1 gives $r^m\ne1$ for every $m\ne0$, whence $|\widehat\mu_k(m)|=|\cos(m\delta/2)|^k\to0$. Trigonometric-polynomial density completes the proof. $\square$

For $p(z)=\sum_{|m|\le M}a_mz^m$, the same argument gives the finite-cutoff bound $$|\mu_k(p)-\!\int p\,d\mathrm{Haar}|
 \le\sum_{0<|m|\le M}|a_m|\,|\cos(m\delta/2)|^k.                 \tag{2}$$

# Joint law and the torsion control

Let $d=\log(|\lambda_+|/|\lambda_-|)$, $\sigma^2=d^2/4$, and $Y_k=\sqrt{k}(k^{-1}\log|\rho|+\log(3)/4)$. With $J_k$ fair binomial, $Y_k=d(J_k-k/2)/\sqrt{k}$ and the phase is $u_-^kr^{J_k}$. Therefore $$\begin{aligned}
 &\mathbb E[e^{itY_k}\operatorname{phase}(\rho)^m]\notag\\[-2mm]
 &\quad=u_-^{mk}e^{-itd\sqrt{k}/2}
 \left(\frac{1+r^me^{itd/\sqrt{k}}}{2}\right)^k.                \tag{3}\end{aligned}$$ For $m=0$ this tends to $e^{-\sigma^2t^2/2}$; for $m\ne0$ its base tends to a number of modulus below one. Hence $$(Y_k,\operatorname{phase}(\rho))
 \ \Longrightarrow\ N(0,\sigma^2)\otimes\mathrm{Haar},          \tag{4}$$ so the two coordinates become asymptotically independent.

More generally, if a binary phase ratio has exact order $h$, finite Fourier inversion gives convergence in total variation to the uniform measure on the moving coset $u_-^k\langle r\rangle$, with $$\mathrm{TV}\le\frac{h-1}{2}
 \max_{1\le m<h}|\cos(\pi m/h)|^k.                              \tag{5}$$ Moving the frozen hole to $\operatorname{diag}(0,1,1)$ gives nonzero roots $-i,-1/\sqrt3$, phase ratio $i$, and the order-four branch $\mathrm{TV}\le(3/2)(\sqrt2/2)^k$. Projector order is a unitary similarity and preserves the non-torsion branch. The closed parent has three phases and is outside this binary statement.

# Evidence and boundary

The producer freezes 32 binomial/control ledgers and the exact rational recurrence for $r^m+r^{-m}$ through $m=24$. Independent strict and symbolic reconstructions, byte replay, and hostile mutations test the implementation; the finite receipts do not prove the all-$k$ theorem. The original gate clears the unconditional phase gate, so the preregistered model pivot is not used. The result is source-side and subunitary. It asserts no self-adjoint or antiunitary limit, target divisor or counting law, arithmetic local factor, Euler factor, root number, automorphy, Hilbert--Polya operator, or Route-B authorization. The literal scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Declarations.

All package data, exact code, validators, mutations, and build receipts are included with the manuscript. No human or animal subjects, private data, or external dataset are involved. The anonymous contribution record comprises conceptualization, formal analysis, software, validation, visualization, and writing. No funding or competing interest is declared. AI assistance was used for drafting and code generation; all claim-bearing formulas were reconstructed by deterministic independent checks, and no external reviewer or acceptance score is represented.
