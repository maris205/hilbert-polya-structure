---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-expanding-circle-wold-route-a"
canonical_tex: "henon_dynamics/henon_expanding_circle_wold_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_expanding_circle_wold_route_a/paper/main.pdf"
source_sha256: "60233766359dc902fe04bab33a497b64d33dafd40b08368ffa99a61c6ba3a2f3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Periodic, Wold, and Mixing Structure of Integer Expanding Circle Maps

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_expanding_circle_wold_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_expanding_circle_wold_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_expanding_circle_wold_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_expanding_circle_wold_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every integer $b\ge2$, we solve the fixed points and Artin--Mazur zeta of $T_b(x)=bx\pmod1$, decompose its Haar--Koopman operator into a constant and countably many unilateral shifts, and prove a sharp Sobolev correlation law. The result couples an exact primitive-orbit ledger to its natural nonunitary operator owner and exposes a degree-only Route-A obstruction.
author:
- 'Route-A structural certificate C177'
title: 'Periodic, Wold, and Mixing Structure of Integer Expanding Circle Maps'
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** expanding circle map; Artin--Mazur zeta; Koopman isometry; Wold decomposition; primitive cycle; correlation decay.

chinese-simplified

中文摘要

本文对任意整数$b\ge2$的扩张圆映射给出全部不动点、原始周期轨道与动力 $\zeta$函数，并把自然[Koopman]{lang="en"}算子精确分解为常数部分和可数无穷个 单边移位，并证明尖锐的光滑观测相关衰减律。周期数据虽然完整，却只依赖拓扑次数， 因而构成严格的[Route-A]{lang="en"}反例。

关键词：扩张圆映射；动力$\zeta$函数；[Koopman]{lang="en"}等距算子； [Wold]{lang="en"}分解；原始周期。

# Periodic theorem

Let $\mathbb T=\mathbb R/\mathbb Z$ and $T_b(x)=bx\pmod1$. The equation $T_b^n(x)=x$ is $(b^n-1)x=0$ in $\mathbb T$, so $$\operatorname{Fix}(T_b^n)=\left\{\frac{j}{b^n-1}:0\le j<b^n-1\right\},
 \qquad F_b(n)=b^n-1.$$ Möbius inversion gives exact-period points and primitive cycles $$P_b(n)=\sum_{d\mid n}\mu(n/d)(b^d-1),\qquad C_b(n)=P_b(n)/n.$$ Consequently $$\zeta_{AM,b}(z)=\exp\!\sum_{n\ge1}\frac{(b^n-1)z^n}{n}
 =\frac{1-z}{1-bz}
 =\prod_{n\ge1}(1-z^n)^{-C_b(n)}.$$ The product is coefficientwise. Since exact-period points split into $n$-cycles, the divisibility $n\mid P_b(n)$ is intrinsic, not empirical.

# Natural operator owner

For $e_m(x)=e^{2\pi imx}$ and $U_bf=f\circ T_b$, one has $U_be_m=e_{bm}$. Every nonzero integer is uniquely $m=rb^j$ with $b\nmid r$, hence $$L^2(\mathbb T)=\mathbb C1\oplus
\bigoplus_{\substack{r\ne0\\b\nmid r}}
\overline{\operatorname{span}}\{e_{rb^j}:j\ge0\},
\qquad U_b\simeq1\oplus S^{(\aleph_0)}.$$ Each nonconstant chain is a unilateral shift. Thus the spectrum is the closed unit disk and the only eigenvalue is $1$ on constants. Moreover $$U_b^*e_m=\begin{cases}e_{m/b},&b\mid m,\\0,&b\nmid m.\end{cases}$$ The source Koopman operator is a proper isometry, not a unitary: its range omits $e_1$. It is noncompact, belongs to no finite Schatten class, and for $z\ne0$ has no ordinary Fredholm determinant $\det(I-zU_b)$.

Indeed the chain vectors form an infinite orthonormal sequence whose images remain orthonormal, ruling out compactness. All nonzero singular values of an isometry are one, so their $p$-sum diverges for every finite $p$. This also blocks trace-class ownership of $zU_b$ when $z\ne0$. The adjoint formula follows directly from $\langle e_k,U_be_m\rangle=\mathbf1_{k=bm}$ and shows that the Perron operator discards precisely the modes not divisible by $b$.

#### Boundary cases.

The hypothesis $b\ge2$ is essential. At $b=1$ the map is the identity, every fixed set is infinite, and the ordinary Artin--Mazur definition does not apply. Negative and noninteger slopes lie outside the frozen family.

# Sharp smooth-observable correlation law

For a mean-zero $f$ set $\|f\|_{\dot H^s}^2=\sum_{k\ne0}|k|^{2s}|\widehat f(k)|^2$. The Fourier action gives $$\langle f,U_b^ng\rangle
 =\sum_{m\ne0}\overline{\widehat f(b^nm)}\widehat g(m).$$ Inserting $|b^nm|^s$, using $|m|^{-s}\le1$, and applying Cauchy--Schwarz proves, for $s\ge0$, $$|\langle f,U_b^ng\rangle|
 \le b^{-ns}\|f\|_{\dot H^s}\|g\|_2.$$ For $s>0$ this exponent and constant are sharp: $f=e_{b^n}$ and $g=e_1$ give equality after division by their norms. Thus the same chain ledger simultaneously owns periodic growth, the Perron filter, and quantitative mixing; none of these layers distinguishes prime from composite degree.

# Route-A decision

  Gate   Verdict         Reason
  ------ --------------- --------------------------------------------
  A0     `FAIL`          no intrinsic arithmetic origin
  A1     `WEAK`          complete but degree-only primitive ledger
  A2     `FAIL`          generic rational source zeta
  A3     `FAIL`          no target global comparison
  A4     `FORMAL_HINT`   unitary only after inverse-limit extension

Prime and composite $b$ satisfy the identical theorem. The overall v0.2 verdict is `ROUTE_A_REJECTED`; Route B is false. The inverse-limit unitary dilation changes phase space and is not a physical quantization.

#### Evidence boundary.

Finite exact evidence contains 132 periodic rows, 1,595 Wold rows, and 352 sharp-correlation rows. A producer-independent checker passes 3,980 assertions, SymPy passes 3,927 checks, byte replay is exact, and all 19 hostile mutations are rejected. These are regression tests; the proof carries every all-parameter statement. Citation and reference populations are zero, and no novelty or priority claim is made. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

Package-local exact evidence and deterministic code accompany this manuscript.

#### Ethics.

No human, animal, clinical, personal, or sensitive data are used; approval is not applicable.

#### Author contributions (CRediT).

This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing. AI systems are not authors.

#### Funding.

No external funding is reported.

#### Conflicts of interest.

None known.

#### AI-use disclosure.

An AI coding assistant supported drafting and exact-code development; it was not an external reviewer or independent error process.
