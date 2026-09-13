---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-thue-morse-induced-fredholm-owner-route-a"
canonical_tex: "henon_dynamics/henon_thue_morse_induced_fredholm_owner_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_thue_morse_induced_fredholm_owner_route_a/paper/main.pdf"
source_sha256: "e0cbf1778d516a1b53cae9ac668614e2ff9452784a6e965216668e7ef1032181"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Induced Fredholm Ownership and a Time-One Compactness Obstruction for the Thue--Morse Renewal Shift

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_thue_morse_induced_fredholm_owner_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_thue_morse_induced_fredholm_owner_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_thue_morse_induced_fredholm_owner_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_thue_morse_induced_fredholm_owner_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $S$ contain the indices at which the Thue--Morse bit is one and let $F(z)=\sum_{s\in S}z^{s+1}$ be the first-return series of the associated renewal shift. We retain each return word as a Hilbert coordinate and construct a rank-one family $K_z$ which is holomorphic in trace norm on the open unit disk. Every trace power is exact, $\operatorname{Tr}K_z^m=F(z)^m$, and adjoining the all-zero fixed orbit gives $\det_F(I-([z]\oplus K_z))=(1-z)(1-F(z))$, the inverse source zeta proved in C159. We also prove that every bounded diagonal weighted-Hilbert realization of the uninduced time-one adjacency is noncompact and belongs to no Schatten class. The source natural boundary further forbids trace-class meromorphic continuation of the owner through any unit-circle arc. Thus branch ownership is separated from both a scalar determinant chosen after the fact and a compact time-one realization. We claim no target divisor, arithmetic factorization, self-adjoint lift, or Hilbert--Pólya operator.
author:
- 'Route-A structural certificate C164'
title: 'Induced Fredholm Ownership and a Time-One Compactness Obstruction for the Thue--Morse Renewal Shift'
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** symbolic dynamics; Thue--Morse sequence; renewal shift; first-return operator; trace class; Fredholm determinant.

chinese-simplified

中文摘要

令集合 $S$ 由 [Thue--Morse]{lang="en"} 序列中取值为一的下标组成， $F(z)=\sum_{s\in S}z^{s+1}$ 为相应更新移位的首返级数。本文不把 $F$ 压缩成事后选定的 一维标量，而以每条返回字为希尔伯特坐标，构造单位圆盘内迹范数全纯的秩一算子族。 它的全部迹幂均精确等于 $F(z)^m$；再加入全零不动轨道，所得 [Fredholm]{lang="en"} 行列式恰为 [C159]{lang="en"} 源动力系统的逆 [zeta]{lang="en"}。该构造明确首返算子所有权而不把它混同于单步邻接； 我们进一步证明，原单步邻接在任何使其有界的对角加权希尔伯特空间上都不紧，因而不属于 任何 [Schatten]{lang="en"} 类。正面首返所有权与负面单步障碍由此严格分离；本文不声称目标除子、 算术分解或自伴算子实现。源系统的自然边界还排除了该迹类算子族穿过单位圆任意开弧的 亚纯延拓。

关键词：符号动力系统；[Thue--Morse]{lang="en"} 序列； 更新移位；首返算子；迹类；[Fredholm]{lang="en"} 行列式。

# Frozen source and branch construction

Write $t_s\in\{0,1\}$ for binary digit-sum parity and $S=\{s\geq0:t_s=1\}$. The renewal code is $\mathcal C=\{10^s:s\in S\}$; one shift is one clock tick and a codeword $10^s$ returns after $s+1$ ticks. C159 proves $$\zeta_{X_S}(z)^{-1}=(1-z)(1-F(z)),\qquad
 F(z)=\sum_{s\in S}z^{s+1}.                         \tag{1}$$ On $\mathcal H=\ell^2(S)$ freeze $$q_s=e^{-\sqrt{s+1}},\quad u=(q_s),\quad
 \ell_z(f)=\sum_{s\in S}q_s^{-1}z^{s+1}f_s,
 \quad K_zf=\ell_z(f)u.                              \tag{2}$$ The branch $s$ itself is retained as $B_s(z)f=q_s^{-1}z^{s+1}f_su$, so $K_z=\sum_sB_s(z)$ rather than a scalar written down from (1).

# Trace ownership

The vector $u$ is square summable. For every $\rho<1$, $$\sum_{s\in S}\|B_s(z)\|_1
 \leq \|u\|_2\sum_{s\in S}e^{\sqrt{s+1}}\rho^{s+1}<\infty
 \quad(|z|\leq\rho).                                  \tag{3}$$ The differentiated series obeys the same comparison. Thus (2) is a trace-norm holomorphic rank-at-most-one family. Gauge factors cancel: $\operatorname{Tr}B_s(z)=z^{s+1}$ and $\ell_z(u)=F(z)$. Consequently $$K_z^m=F(z)^{m-1}K_z,\quad
 \operatorname{Tr}K_z^m=F(z)^m,
 \quad\det_F(I-K_z)=1-F(z).                            \tag{4}$$ With $\mathcal L_z=[z]\oplus K_z$, (1) and (4) give $$\det_F(I-\mathcal L_z)=(1-z)(1-F(z))=\zeta_{X_S}(z)^{-1}. \tag{5}$$ The branch sum, compact-subdisk convergence, and all-power trace law are the ownership certificate. Equation (5) alone, realized by a post-hoc scalar, would be tautological.

# The uninduced compactness obstruction

The uninduced one-step adjacency remains a different operator: $$A\delta_n=\delta_{n+1}+t_n\delta_0.                    \tag{6}$$ Give $\ell^2(\mathbb N_0,w)$ positive diagonal weights and normalize $e_n=\delta_n/\sqrt{w_n}$. Then $$Ae_n=\sqrt{w_{n+1}/w_n}\,e_{n+1}
      +t_n\sqrt{w_0/w_n}\,e_0.                           \tag{7}$$ If the bounded operator $A$ were compact, the weakly null orthonormal sequence $(e_n)$ would satisfy $\|Ae_n\|\to0$. The first coefficient in (7) would tend to zero, hence eventually $w_{n+1}\leq w_n/4$ and $w_n\to0$. Along the infinite set $S$, the second coefficient would instead force $w_n\to\infty$, a contradiction. Thus every bounded realization is noncompact and is in no Schatten class. The quantifier is nonvacuous: $w_n=2^n$ gives a bounded shift of norm $\sqrt2$ and a return functional with squared norm $\sum_{s\in S}2^{-s}<\infty$.

# Maximal trace-class domain

C159 proves that $F$ has no meromorphic continuation through a unit-circle arc. The scalar trace is continuous on trace class. Therefore a trace-class meromorphic extension of $K_z$ would continue $\operatorname{Tr}K_z=F(z)$; an extension of $\mathcal L_z$ would continue $z+F(z)$ and hence $F$. Both are impossible. The induced owner is thus holomorphic exactly on the open disk in this meromorphic-extension sense.

The 128-bit, 32-branch, and degree-48 ledgers are finite sentinels. The strict tuple is $$\begin{aligned}
(&\texttt{A1\_WEAK},\texttt{A2\_FAIL},\\[-2pt]
 &\texttt{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},\texttt{A4\_FAIL}).
\end{aligned}$$ We claim no target divisor or counting law, arithmetic/local factor, target functional equation, root number, automorphy, unitary/Hamiltonian or natural self-adjoint lift, Hilbert--Pólya construction, or Route-B authorization. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

Package-local exact evidence and code expose the producer, independent checker, symbolic reconstruction, replay, and mutation audit.

#### Ethics.

No human participants, animals, personal, clinical, or sensitive data are used; approval is not applicable.

#### Author contributions (CRediT).

This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing. AI systems are not authors.

#### Conflicts and funding.

No conflict is known and no external funding is reported.

#### AI-use disclosure.

An AI coding assistant supported drafting, exact-code development, and internal checking. It was not an external reviewer; every released claim is exposed to deterministic hostile tests.
