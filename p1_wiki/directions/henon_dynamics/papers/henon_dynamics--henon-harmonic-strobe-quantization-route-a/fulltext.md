---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-harmonic-strobe-quantization-route-a"
canonical_tex: "henon_dynamics/henon_harmonic_strobe_quantization_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_harmonic_strobe_quantization_route_a/paper/main.pdf"
source_sha256: "45a21564387384811f64daee5b01abee9fcce8fd25be9fa7db7594b6d89c8657"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# All-Angle Harmonic Strobes: Classical Resonance, Gaussian Koopman Spectrum, and Same-Clock Quantization

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_harmonic_strobe_quantization_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_harmonic_strobe_quantization_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_harmonic_strobe_quantization_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_harmonic_strobe_quantization_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the planar oscillator $H=(q^2+p^2)/2$, we give one exact spectral ledger for every physical time $\theta\in\mathbb R$. The $n$th iterate is a rotation through $n\theta$: it fixes only the origin off resonance and the whole plane at resonance. Consequently, irrational $\theta/(2\pi)$ has Artin--Mazur zeta $(1-z)^{-1}$, whereas each rational angle has infinite fixed sets and no ordinary Artin--Mazur series. On invariant Gaussian $L^2$, a Laguerre--angular orthonormal basis diagonalizes the Koopman unitary with eigenvalues $e^{im\theta}$ and infinite radial multiplicity. The natural oscillator quantization at the same clock is diagonal in the Hermite basis and is a $4\pi$-periodic metaplectic lift: a $2\pi$ shift produces the global sign $-1$. It satisfies exact Egorov and reversal but, like the Koopman unitary, is noncompact, non-Schatten, and has no ordinary trace-class Fredholm determinant. Thus natural quantization is genuine progress yet cannot repair the failed periodic-orbit and determinant gates.
author:
- 'Route-A structural certificate C178'
title: 'All-Angle Harmonic Strobes: Classical Resonance, Gaussian Koopman Spectrum, and Same-Clock Quantization'
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** harmonic oscillator; stroboscopic rotation; Gaussian Koopman spectrum; Laguerre basis; exact Egorov; Route A.

chinese-simplified

中文摘要

对平面谐振子 $H=(q^2+p^2)/2$，本文在所有物理实时间 $\theta\in\mathbb R$ 上建立统一的精确谱账本。 第 $n$ 次迭代是转角 $n\theta$ 的旋转：非共振时仅固定原点，共振时固定整个平面。 因此，无理角的 [Artin--Mazur]{lang="en"} 动力 $\zeta$ 函数为 $(1-z)^{-1}$， 而每个有理角均出现无限不动点集，普通定义失效。在不变高斯平方可积空间中， [Laguerre--]{lang="en"}角向正交基把 [Koopman]{lang="en"} 酉算子完全对角化， 其特征值为 $e^{im\theta}$ 且具有无限径向重数。同一物理时钟下的自然谐振子量子化由 [Hermite]{lang="en"} 基对角化。该量子提升具有 $4\pi$ 周期，时间平移 $2\pi$ 会保留不可忽略的 全局负号；同时它满足精确 [Egorov]{lang="en"} 关系和共轭反演。 但两个酉算子都非紧、非有限 [Schatten]{lang="en"} 类，故无普通迹类 [Fredholm]{lang="en"} 行列式。自然量子化不能弥补周期轨道与行列式闸门的失败。

关键词：谐振子；频闪旋转；高斯 [Koopman]{lang="en"} 谱； [Laguerre]{lang="en"} 基；精确 [Egorov]{lang="en"} 关系；路线 [A]{lang="en"}。

# All-angle classical theorem

Freeze physical time as $\theta\in\mathbb R$. Hamilton's equations give $$T_\theta(q,p)=(q\cos\theta+p\sin\theta,
-q\sin\theta+p\cos\theta),\quad T_\theta^n=T_{n\theta},\quad
T_{\theta+2\pi}=T_\theta.$$ Hence, for every $n\ge1$, $$\operatorname{Fix}(T_\theta^n)=
\begin{cases}
\mathbb R^2,&n\theta\in2\pi\mathbb Z,\\
\{(0,0)\},&n\theta\notin2\pi\mathbb Z.
\end{cases}\tag{1}$$ Indeed, a nonidentity planar rotation fixes only the origin, whereas the identity fixes the plane. If $\theta/(2\pi)$ is irrational, all fixed counts equal one, and the formal identity $$\zeta_{\rm AM}(z)=\exp\!\left(\sum_{n\ge1}\frac{z^n}{n}\right)
=(1-z)^{-1}\tag{2}$$ follows from $-\log(1-z)=\sum_{n\ge1}z^n/n$. If $\theta/(2\pi)=a/b$ in lowest terms, (1) equals $\mathbb R^2$ exactly when $b\mid n$; these uncountable cardinalities are not finite Artin--Mazur coefficients. Thus the ordinary series is undefined, including $b=1$. For $b>1$, every nonzero point has least period $b$. Finally, $S(q,p)=(q,-p)$ is an involution with $ST_\theta S=T_\theta^{-1}$.

# Exact Gaussian Koopman spectrum

Write $q-ip=re^{i\varphi}$, so $T_\theta$ advances $\varphi$ by $\theta$, and freeze $$d\gamma=\pi^{-1}e^{-r^2}\,dq\,dp,\qquad
U_\theta f=f\circ T_\theta .$$ Rotation preserves $\gamma$, hence $U_\theta$ is unitary and $U_{\theta+2\pi}=U_\theta$. For $m\in\mathbb Z$ and $k\ge0$, define $$\psi_{k,m}=\sqrt{\frac{k!}{(k+|m|)!}}\,
r^{|m|}L_k^{|m|}(r^2)e^{im\varphi}.$$ The angular Fourier basis and, after $x=r^2$, the identity $$\int_0^\infty e^{-x}x^{|m|}L_k^{|m|}(x)L_\ell^{|m|}(x)\,dx
=\frac{(k+|m|)!}{k!}\delta_{k\ell}$$ prove orthonormality and completeness. Direct substitution gives the all-parameter diagonalization $$U_\theta\psi_{k,m}=e^{im\theta}\psi_{k,m}.\tag{3}$$ For irrational $\theta/(2\pi)$, the eigenvalues indexed by $m$ are distinct and dense on the unit circle. For reduced $a/b$, they are exactly the $b$th roots of unity. In both cases, varying $k$ gives each eigenvalue countably infinite multiplicity. Thus $U_\theta$ is noncompact; all its singular values are one, so it lies in no finite Schatten class and $\det(I-zU_\theta)$ is not an ordinary trace-class Fredholm determinant for $z\ne0$. If $V_Sf=f\circ S$ and $K$ denotes complex conjugation, then the antiunitary $\Theta_G=V_SK$ obeys $\Theta_GU_\theta\Theta_G^{-1}=U_\theta^{-1}$.

# Natural same-clock quantum lift

On $L^2(\mathbb R)$, let $$\widehat H=\frac12\left(-\frac{d^2}{dx^2}+x^2\right),\qquad
Q_\theta=e^{-i\theta\widehat H}.$$ The standard Hermite basis gives $$\widehat Hh_j=(j+\tfrac12)h_j,\qquad
Q_\theta h_j=e^{-i\theta(j+1/2)}h_j.\tag{4}$$ Here $\theta$ remains real physical time; it is not replaced by a class modulo $2\pi$. Equation (4) gives $$Q_{\theta+2\pi}=-Q_\theta,\qquad Q_{\theta+4\pi}=Q_\theta.\tag{5}$$ Thus the metaplectic lift is $4\pi$-periodic and only projectively $2\pi$-periodic; the global sign is retained. Irrational times give distinct dense pure point phases. For the exact real-time representative $\theta/(2\pi)=a/b$ in lowest terms, the spectrum is $e^{-i\pi a/b}$ times the $b$th roots, each with infinite multiplicity. Replacing $a$ by $a+b$ multiplies $Q_\theta$ by $-1$. On the Schwartz core, with $\widehat p=-i\,d/dx$, $$[\widehat H,\widehat q]=-i\widehat p,
\qquad[\widehat H,\widehat p]=i\widehat q.$$ Integrating the Heisenberg equations proves the exact, same-clock Egorov law $$Q_\theta^*\widehat qQ_\theta=\widehat q\cos\theta+\widehat p\sin\theta,
\quad
Q_\theta^*\widehat pQ_\theta=-\widehat q\sin\theta+\widehat p\cos\theta.
\tag{6}$$ Complex conjugation satisfies $KQ_\theta K=Q_\theta^{-1}$. Equation (4) also supplies an orthonormal image sequence, so $Q_\theta$ is noncompact, belongs to no finite Schatten class, and has no ordinary trace-class Fredholm determinant. Although $e^{-t\widehat H}$ is trace class for $t>0$, it uses imaginary time. Heat damping, Wick rotation, and Hermite truncation are different clocks or objects and cannot serve as determinants of $T_\theta$, $U_\theta$, or $Q_\theta$.

# Route-A decision and evidence boundary

  Gate   Verdict                  Exact reason
  ------ ------------------------ ------------------------------------------------------------------
  A0     `FAIL`                   no intrinsic arithmetic origin or finite all-angle orbit carrier
  A1     `FAIL`                   trivial irrational ledger; rational fixed sets are infinite
  A2     `FAIL`                   ordinary Koopman and quantum determinants are unavailable
  A3     `FAIL`                   no target divisor, functional equation, or counting-law match
  A4     `NATURAL_QUANTIZATION`   real-time metaplectic lift, Egorov, and reversal

The exact tuple is

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.

The overall verdict is `ROUTE_A_REJECTED`, and Route B is false. The positive A4 theorem cannot compensate for A0--A3.

Finite regression ledgers contain 1,656 rational fixed-set rows, 108 irrational rows, 209 Laguerre rows, 874 Koopman-phase rows, and 736 quantum phase rows. A producer-independent checker passes 26,271 assertions, SymPy passes 10,465 exact checks, byte replay is exact, and all 65 hostile mutations are rejected. These sentinels test implementations; the all-parameter results rest on the proofs above. No external novelty, priority, reviewer, or acceptance claim is made.

#### Limitations.

We use ordinary Artin--Mazur and trace-class Fredholm definitions, do not introduce regularized determinants, and never identify $Q_{\theta+2\pi}$ with $Q_\theta$ as unitaries. No target zero or prime table, fitted parameter, arithmetic local datum, Euler factor, root number, automorphy object, Hilbert--Pólya operator, or Route-B authorization enters the package. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Declarations {#declarations .unnumbered}

**Data and code availability.** Package-local exact evidence and deterministic code accompany this manuscript. **Ethics.** No human, animal, clinical, personal, private, or sensitive data are used; approval is not applicable. **Author contributions (CRediT).** This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing; AI systems are not authors. **Funding.** No external funding is reported. **Conflicts of interest.** None known. **AI-use disclosure.** An AI coding assistant supported drafting and exact-code development; it was not an external reviewer or an independent error process.
