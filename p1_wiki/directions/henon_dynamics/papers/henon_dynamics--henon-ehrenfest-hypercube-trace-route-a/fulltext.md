---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-ehrenfest-hypercube-trace-route-a"
canonical_tex: "henon_dynamics/henon_ehrenfest_hypercube_trace_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_ehrenfest_hypercube_trace_route_a/paper/main.pdf"
source_sha256: "17f3a11700b578d18571d835481e05300d0c27edbcbd0c819694a7379febff1e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Walsh Traces and Krawtchouk Compression for the Ehrenfest Hypercube Walk

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_ehrenfest_hypercube_trace_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_ehrenfest_hypercube_trace_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_ehrenfest_hypercube_trace_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_ehrenfest_hypercube_trace_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every integer $d\geq1$, we diagonalize the Ehrenfest coordinate-flip operator on the $d$-dimensional sign cube. Every Walsh character indexed by $S$ has eigenvalue $1-2|S|/d$, with binomial multiplicity. This gives exact power traces, a factored determinant, and every vertex return probability; odd returns vanish by bipartiteness. Hamming weight is an exact Markov lumping to a $(d+1)$-state reversible birth--death chain. Its symmetric Jacobi similarity has off-diagonal entries $\sqrt{(k+1)(d-k)}/d$, and Krawtchouk polynomials provide its simple spectrum, retaining every distinct eigenvalue of the original $2^d$-state operator. The natural $P_d$ is self-adjoint, but exponentiation changes the frozen Markov clock and weights. The family has no intrinsic prime correspondence; the result is an all-parameter source theorem, not a target-spectrum claim.
author:
- 'Route-A structural certificate C171'
title: |
  Exact Walsh Traces and Krawtchouk Compression\
  for the Ehrenfest Hypercube Walk
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** Ehrenfest chain; hypercube dynamics; Walsh characters; Krawtchouk polynomials; reversible Markov chains; exact traces.

chinese-simplified

中文摘要

对任意整数 $d\geq1$，本文精确对角化 $d$ 维符号超立方体上的 [Ehrenfest]{lang="en"} 坐标翻转算子。由集合 $S$ 标记的 [Walsh]{lang="en"} 特征函数具有特征值 $1-2|S|/d$，其重数为二项式系数。 由此得到精确幂迹、因子化行列式与任意顶点的返回概率；二部结构使所有奇数时刻返回概率为零。 汉明重量给出到 $d+1$ 状态可逆生灭链的精确马尔可夫压缩。其对称 [Jacobi]{lang="en"} 相似矩阵的非对角元为 $\sqrt{(k+1)(d-k)}/d$，而 [Krawtchouk]{lang="en"} 多项式给出单谱， 从而保留原 $2^d$ 状态算子的每个不同特征值。自然算子 $P_d$ 虽然自伴，但取酉指数会改变冻结的 马尔可夫时钟与路径权重；本系统也不内生素数对应，因此本文不作目标谱结论。

关键词：[Ehrenfest]{lang="en"} 链；超立方体动力学； [Walsh]{lang="en"} 特征；[Krawtchouk]{lang="en"} 多项式；可逆马尔可夫链；精确迹。

# Frozen dynamics

Let $X_d=\{-1,+1\}^d$, let $x^{(i)}$ flip coordinate $i$, and set $$(P_df)(x)=\frac1d\sum_{i=1}^d f(x^{(i)})
 \quad\text{on }L^2(X_d,2^{-d}\#).                              \tag{1}$$ One coordinate flip is one Markov tick. For $S\subseteq\{1,\ldots,d\}$, write $\chi_S(x)=\prod_{i\in S}x_i$.

#### Theorem 1 (complete Walsh certificate).

For every $d\geq1$, the Walsh characters form an orthonormal eigenbasis and $$P_d\chi_S=\lambda_{|S|}\chi_S,\qquad
 \lambda_j=1-\frac{2j}{d},\qquad
 \operatorname{mult}(\lambda_j)=\binom dj.                     \tag{2}$$ Consequently, for every $n\geq0$, $$\begin{aligned}
 \operatorname{Tr}P_d^n&=\sum_{j=0}^d\binom dj\lambda_j^n,       \tag{3}\\
 \det(I-zP_d)&=\prod_{j=0}^d(1-z\lambda_j)^{\binom dj}.          \tag{4}\end{aligned}$$

#### Proof.

A flip contributes $-\chi_S$ for the $|S|$ coordinates in $S$ and $+\chi_S$ for the other $d-|S|$. Averaging proves (2). Walsh orthogonality and the count $\binom dj$ give a complete basis; (3)--(4) follow from the finite spectral theorem. $\square$

For $|z|<1$, the scalar power series for $-\log(1-z\lambda_j)$ gives the exact trace--log relation $$-\log\det(I-zP_d)=\sum_{n\geq1}\operatorname{Tr}(P_d^n)\frac{z^n}{n}.
                                                                    \tag{5}$$ For every $d>1$ this is a weighted closed-Markov-walk identity: $P_d$ is a genuine average rather than a deterministic map, so these traces are not fixed-point counts and (5) is not an Artin--Mazur zeta. At $d=1$, $P_1$ is the deterministic two-cycle permutation; that isolated boundary does not supply a uniform all-$d$ primitive-orbit interpretation.

# Return law and exact compression

Cube translations commute with $P_d$ and act transitively, so all diagonal entries of $P_d^n$ agree. Their sum is the trace, hence $$P_d^n(x,x)=2^{-d}\operatorname{Tr}P_d^n.                       \tag{6}$$ Every flip reverses Hamming parity, proving that (6) vanishes for odd $n$.

Let $k$ count negative coordinates. The exact lumped kernel is $$Q(k,k+1)=\frac{d-k}{d},\qquad Q(k,k-1)=\frac{k}{d}.             \tag{7}$$ For $\pi_k=2^{-d}\binom dk$, the binomial identity $\binom dk(d-k)=\binom d{k+1}(k+1)$ proves detailed balance. Therefore $D_\pi^{1/2}QD_\pi^{-1/2}$ is symmetric with upper entry $\sqrt{(k+1)(d-k)}/d$.

#### Theorem 2 (Krawtchouk compression).

Define $$K_j(k)=\sum_r(-1)^r\binom kr\binom{d-k}{j-r}.$$ Then $QK_j=(1-2j/d)K_j$. Thus $Q$ has the $d+1$ distinct eigenvalues in (2), each once, and compresses the $2^d$-state operator without losing a distinct eigenvalue.

#### Proof.

The generating function is $\sum_jK_j(k)t^j=(1-t)^k(1+t)^{d-k}$. Substitution of $k\pm1$ using (7) equals the original series minus $(2t/d)$ times its derivative. Comparing $t^j$ coefficients gives the eigenvalue equation. The eigenvalues are distinct, so the $K_j$ form a basis. $\square$

# Arithmetic and operator controls

Four frozen controls expose the scope. Random arithmetic labels do not enter $P_d$; composite-only dimension labels change no theorem; neighboring dimensions obey the same binomial law; and $\eta I+(1-\eta)P_d$ has the affinely shifted spectrum for any source-chosen $\eta$. For $d>1$ there is no deterministic primitive-orbit owner. The $d=1$ two-cycle is an isolated boundary with no all-family repetition law, $\log p$ clock, or arithmetic weight. Thus A0 fails and A1 fails for the full family.

Each coordinate flip is a self-adjoint permutation, so their average $P_d$ is a natural self-adjoint contraction. However, $e^{-itP_d}$ is not the frozen one-flip Markov dynamics: it changes both clock and path weights. This is only a formal A4 hint, not a same-clock quantization. The Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
   \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).                 \tag{8}$$ Because A0 is mandatory, the overall Route-A status is `ROUTE_A_REJECTED`; the exact source theorem is retained.

# Boundary

For $d=1$, the theorem reduces to the deterministic two-cycle with spectrum $\{1,-1\}$. At even $d$, zero has multiplicity $\binom d{d/2}$; its factor in (4) is one and contributes no polynomial degree. At $n=0$, (3) and (6) give $2^d$ and one, respectively. The unit eigenvalue makes $|z|<1$ the natural domain stated for (5).

Exact ledgers through $d=18,n=24$, independent reconstruction, brute closed-walk enumeration for $d\leq7,n\leq8$, symbolic Krawtchouk checks, byte replay and repaired-hash mutations test the implementation; they do not prove the theorem. No target divisor, functional equation, counting law, arithmetic local datum, Euler factor, root number, automorphy, Hilbert--Polya operator or Route-B authorization is asserted. The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Declarations.

All data and code needed to reproduce the exact artifact are included. No human or animal subjects, private data or external dataset are involved. The anonymous contribution record covers conceptualization, formal analysis, software, validation and writing. No funding is declared. No competing interest is declared. AI assistance was used for drafting and code generation; every claim-bearing identity was deterministically reconstructed, and no external reviewer or acceptance score is represented.
