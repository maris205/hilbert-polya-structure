---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-open-walsh-growing-k-escape-route-a"
canonical_tex: "henon_dynamics/henon_open_walsh_growing_k_escape_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_open_walsh_growing_k_escape_route_a/paper/main.pdf"
source_sha256: "1230bac8ed901c20417bf6b327ca27b910a8254d1eb8cc38f25e7d0f388268ad"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Saturated Image Escape and GCD Trace Clusters in a Growing Open Walsh Gate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_open_walsh_growing_k_escape_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_open_walsh_growing_k_escape_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_open_walsh_growing_k_escape_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_open_walsh_growing_k_escape_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a three-symbol open Walsh factor shift, we determine the image rank at every system size and time. At time proportional to tensor length, the signed log-survival rate is linear and then saturates after one full factor cycle. Fixed-period traces retain a greatest-common-divisor dependence on the system size and need not converge, but dimension-normalized traces vanish. These are source-side large-system statements, not a secular, self-adjoint, or target-matched limit.
author:
- 'Hénon Route-A Working Series, C153'
date: 25 August 2026
title: |
  Saturated Image Escape and GCD Trace Clusters\
  in a Growing Open Walsh Gate
```

## Markdown 正文

# Frozen gate and exact power rank

Let $\omega=e^{2\pi i/3}$, $$(F_3)_{j\ell}=3^{-1/2}\omega^{j\ell},\qquad
 P=\operatorname{diag}(1,0,1),\qquad A=F_3^*P.$$ On $\mathcal H_k=(\mathbb C^3)^{\otimes k}$ freeze $$B_k(v_0\otimes\cdots\otimes v_{k-1})
=v_1\otimes\cdots\otimes v_{k-1}\otimes Av_0.       \tag{1}$$ One application is one clock tick. Direct calculation gives $$\det(\lambda I-A)=\lambda(\lambda^2-\tau\lambda+q_0),\quad
\tau=\frac{\sqrt3}{6}-\frac i2,\quad
q_0=-\frac12-\frac{\sqrt3 i}{6}.$$ Since $q_0\ne0$, zero is a simple eigenvalue and the other two eigenvalues are nonzero. Hence $\operatorname{rank}(A^m)=2$ for every $m\ge1$, while $\operatorname{rank}(A^0)=3$.

For every $k\ge1$ and $n\ge0$, $$\operatorname{rank}(B_k^n)=2^{\min(n,k)}3^{k-\min(n,k)}.           \tag{2}$$

Write $n=qk+r$, with $0\le r<k$. Iterating (1) on a pure tensor gives $$B_k^n(v_0,\ldots,v_{k-1})=
(A^qv_r,\ldots,A^qv_{k-1},A^{q+1}v_0,\ldots,A^{q+1}v_{r-1}).$$ If $q=0$, exactly $n=r$ factors have positive powers of $A$; if $q\ge1$, all $k$ do. Tensor-rank multiplicativity proves (2), including the identity boundary $n=0$.

The survival fraction is therefore $$S_k(n)=\frac{\operatorname{rank}(B_k^n)}{3^k}
       =\left(\frac23\right)^{\min(n,k)}.             \tag{3}$$ For $n_k=\lfloor\alpha k\rfloor$ and $\alpha\ge0$, $$\lim_{k\to\infty}\frac1k\log S_k(n_k)
 =\min(\alpha,1)\log(2/3).                           \tag{4}$$ Thus the positive escape exponent is $E(\alpha)=\min(\alpha,1)\log(3/2)$. At $\alpha=0$ one has $n_k=0$, $S_k=1$, and $E(0)=0$; no positive-time formula is silently substituted at this identity boundary.

# Fixed-period traces

For the two nonzero roots, let their power-sum initial value be $t_0=2$; put $t_1=\tau$ and $t_m=\tau t_{m-1}-q_0t_{m-2}$. Thus $t_m=\operatorname{Tr}(A^m)$ only for $m\ge1$ (whereas $\operatorname{Tr}(A^0)=3$). Basis-index contraction along the cycles of addition by $n$ modulo $k$ gives, for $d=\gcd(n,k)$, $$\operatorname{Tr}(B_k^n)=t_{n/d}^{d}.                             \tag{5}$$ Indeed the factor permutation has $d$ independent cycles, and each cycle contracts $n/d$ ordered copies of $A$.

At fixed $n$, (5) ranges over the equality-merged set of divisor values $$\{t_{n/d}^{d}:d\mid n\}.                           \tag{6}$$ where divisors that produce the same complex number define one cluster value. For each divisor $d\mid n$, the unbounded sequence $k_j=d(1+j(n/d))$ satisfies $\gcd(n,k_j)=d$, so every divisor class occurs infinitely often. Conversely no other value can occur. Because this is a finite set, $$3^{-k}\operatorname{Tr}(B_k^n)\longrightarrow0                    \tag{7}$$ for every fixed period.

The normalization cannot be removed in general. At period two, odd $k$ have $d=1$ and even $k$ have $d=2$, so $$\begin{aligned}
t_2&=\frac56+\frac{\sqrt3}{6}i,&
t_1^2&=-\frac16-\frac{\sqrt3}{6}i,\\[-2pt]
t_2-t_1^2&=1+\frac{\sqrt3}{3}i=-2q_0\ne0.
\end{aligned}                                                    \tag{8}$$ The odd and even subsequences are distinct constants. Hence $\operatorname{Tr}(B_k^2)$ has no unnormalized $k\to\infty$ limit.

# Validation and boundary

Three controls separate rank escape from trace geometry. For $P=I_3$, the closed parent is unitary and every power has rank $3^k$, so its escape exponent is zero. For $A_{\rm R}=PF_3^*=F_3AF_3^*$, uniform tensor conjugation leaves the rank law and trace clusters unchanged. Moving the hole to $P_0=\operatorname{diag}(0,1,1)$ gives $$\det(\lambda I-F_3^*P_0)
 =\lambda(\lambda+i)(3\lambda+\sqrt3)/3.$$ Its zero root is simple and the other two roots are nonzero, so every positive one-site power has rank two and the full rank law survives. Its trace values change, showing that rank escape does not determine trace geometry.

The exact payload contains 624 rank rows, 192 macroscopic rows, and divisor ledgers through period twenty. A producer-independent checker, separate symbolic reconstruction, byte replay, and semantic mutation suite validate the implementation: the checker passes 6,193 assertions, SymPy passes 213 checks, replay is byte-identical, and all 53 hostile cases (52 repaired-hash and one stale-hash) are rejected. Finite ledgers are sentinels, not proofs of the all-parameter statements.

The strict Route-A tuple is $$(\texttt{A1\_WEAK},\texttt{A2\_FAIL},\texttt{A3\_FAIL},
 \texttt{A4\_UNITARY\_OR\_SCATTERING\_CANDIDATE}),$$ overall `ROUTE_A_EXPLORATORY`. The source-derived subunitary family and same-clock closed unitary parent support only the displayed A4 candidate: no self-adjoint or antiunitary growing-$k$ limit is constructed. We claim no full growing-$k$ secular limit, target divisor, functional equation, counting law, prime-like map, arithmetic local data, Euler factor, root number, automorphy, Hilbert--Pólya operator, or Route-B authorization. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
