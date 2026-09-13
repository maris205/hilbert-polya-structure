---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-primitive-field-multiplier-route-a"
canonical_tex: "henon_dynamics/henon_primitive_field_multiplier_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_primitive_field_multiplier_route_a/paper/main.pdf"
source_sha256: "a3ef7409285f8eadf2ca9e3f8d958b73858a85f9a8bac13d976d6df0423b4518"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Primitive Finite-Field Multipliers: Exact Orbits, Zeta and Koopman Determinants

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_primitive_field_multiplier_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_primitive_field_multiplier_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_primitive_field_multiplier_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_primitive_field_multiplier_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $Q\geq2$ be any prime power and let $a$ generate $\mathbb F_Q^\times$. Multiplication $T_a(x)=ax$ fixes zero and acts as one cycle of length $N=Q-1$ on the nonzero field. We derive, uniformly in $Q$ and $a$, every fixed-point count and the exact Artin--Mazur zeta $((1-z)(1-z^N))^{-1}$. The natural Koopman permutation is unitary; its spectrum is one extra eigenvalue $1$ together with every $N$th root of unity, so its determinant is the reciprocal zeta. Inversion is an exact time reversor, and Koopman is self-adjoint exactly for $Q\leq3$. These are all-parameter algebraic dynamics statements. Prime-power phase-space size is intrinsic, but same-cycle controls supply no rational-prime orbit or logarithmic weight dictionary.
author:
- 'Route-A structural certificate C172'
title: |
  Primitive Finite-Field Multipliers:\
  Exact Orbits, Zeta and Koopman Determinants
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** finite fields; primitive multipliers; permutation dynamics; Artin--Mazur zeta; Koopman operators; time reversal.

chinese-simplified

中文摘要

设 $Q\geq2$ 为任意素数幂，$a$ 为 $\mathbb F_Q^\times$ 的生成元。 乘法映射 $T_a(x)=ax$ 固定零点，并在非零域元素上形成长度 $N=Q-1$ 的唯一周期。 本文对任意 $Q$ 与 $a$ 推导全部不动点计数及精确 [Artin--Mazur zeta]{lang="en"} 函数 $((1-z)(1-z^N))^{-1}$。自然 [Koopman]{lang="en"} 置换算子是酉的； 其谱由一个额外特征值 $1$ 与全部 $N$ 次单位根组成，故其行列式为该 [zeta]{lang="en"} 函数的倒数。 取逆映射给出精确时间反演，而 [Koopman]{lang="en"} 算子自伴当且仅当 $Q\leq3$。 这些结论是全参数代数动力学定理。素数幂相空间大小确属内生结构，但同周期型对照表明， 它并未给出有理素数轨道或对数权重字典。

关键词：有限域；本原乘子；置换动力学；[Artin--Mazur zeta]{lang="en"}； [Koopman]{lang="en"} 算子；时间反演。

# Frozen field dynamics

Let $Q=p^e$, let $a$ be primitive in $\mathbb F_Q^\times$, set $N=Q-1$, and define $T_a(x)=ax$. One multiplication is one clock tick.

#### Theorem 1 (complete orbit law).

Zero is fixed, $\mathbb F_Q^\times$ is one primitive $N$-cycle, and $$\#\operatorname{Fix}(T_a^n)=1+N\mathbf 1_{N\mid n}
 =\begin{cases}Q,&N\mid n,\\1,&N\nmid n.\end{cases}             \tag{1}$$ Consequently $$\zeta_{T_a}(z)=\exp\!\left(\sum_{n\geq1}
 \#\operatorname{Fix}(T_a^n)\frac{z^n}{n}\right)
 =\frac1{(1-z)(1-z^N)}.                                        \tag{2}$$

#### Proof.

Every nonzero $x$ has a unique form $a^k$ with $k\in\mathbb Z/N\mathbb Z$, and $T_a(a^k)=a^{k+1}$. This proves the cycle and (1). Separating the fixed zero contribution gives $$\sum_{n\geq1}\frac{z^n}{n}+\sum_{m\geq1}N\frac{z^{mN}}{mN}
 =-\log(1-z)-\log(1-z^N),$$ which proves (2) formally and for $|z|<1$. $\square$

# Koopman certificate

On normalized counting $L^2(\mathbb F_Q)$, set $U_af=f\circ T_a$.

#### Theorem 2.

$U_a$ is unitary and has one extra eigenvalue $1$ from zero, together with every $N$th root of unity once from the nonzero cycle. Therefore $$\det(I-zU_a)=(1-z)(1-z^N)=\zeta_{T_a}(z)^{-1}.                 \tag{3}$$

#### Proof.

Composition with a permutation preserves normalized counting measure. The fixed point supplies one $1$-eigenvector; discrete Fourier characters on the cyclic exponent coordinate diagonalize the long cycle. Their characteristic product is $1-z^N$, yielding (3). $\square$

# Reversal and the self-adjoint boundary

Define $I(0)=0$ and $I(x)=x^{-1}$ for $x\ne0$. Then $$IT_aI(x)=I(ax^{-1})=a^{-1}x=T_a^{-1}(x),                       \tag{4}$$ with the same identity at zero. Hence $\Theta f(x)=\overline{f(Ix)}$ is a same-clock antiunitary reversal and $\Theta U_a\Theta^{-1}=U_a^{-1}$.

#### Theorem 3 (sharp boundary).

$U_a$ is self-adjoint if and only if $Q\leq3$.

#### Proof.

A unitary permutation is self-adjoint exactly when it equals its inverse, equivalently when every cycle has length at most two. The only nontrivial cycle here has length $N=Q-1$, proving the claim. $\square$

At $Q=2$, both field elements are fixed and (2)--(3) become $(1-z)^{-2}$ and $(1-z)^2$. At $Q=3$, the nonzero cycle is a transposition. For every $Q\geq4$, its length exceeds two and self-adjointness fails.

# Arithmetic controls and Route-A verdict

The finite-field provenance is intrinsic, but four controls limit its force. A composite cyclic surrogate consisting of a fixed point and translation on $\mathbb Z/N\mathbb Z$ has the same orbit and determinant laws. Multiplication by $a^h$ splits the nonzero set into $\gcd(h,N)$ cycles of length $N/\gcd(h,N)$, detecting primitivity without producing target weights. Any random permutation of cycle type $(1)(N)$ has the same zeta and spectrum, and neighboring prime powers repeat the $N=Q-1$ law. Hence no intrinsic rational-prime orbit dictionary, $\log p$ clock or von Mangoldt amplitude appears.

The same-clock Koopman permutation and its antiunitary reversal are a natural A4 lift. The qualified tuple is $$(\mathrm{A0\_WEAK\_ARITHMETIC\_RELATION},\mathrm{A1\_WEAK},
 \mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
 \mathrm{A4\_NATURAL\_QUANTIZATION}).                           \tag{5}$$

# Exact validation boundary

The proof is independent of a polynomial representation of the field and covers every prime power. Exact ledgers for 18 fields, independent cycle enumeration, symbolic permutation matrices, byte replay and mutation attacks are regression sentinels rather than the proof. No target divisor, functional equation, counting law, arithmetic local datum, global Euler product, local factor, root number, automorphy, Hilbert--Polya operator or Route-B authorization is asserted. The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Declarations.

All exact data and code are included. No human or animal subjects, private data or external dataset are involved. The anonymous contribution record covers conceptualization, formal analysis, software, validation and writing. No funding is declared. No competing interest is declared. AI assistance was used for drafting and code generation; all claim-bearing formulas were deterministically reconstructed, and no external reviewer or acceptance score is represented.
