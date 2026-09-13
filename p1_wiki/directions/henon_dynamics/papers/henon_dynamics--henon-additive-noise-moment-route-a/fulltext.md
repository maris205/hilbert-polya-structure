---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-additive-noise-moment-route-a"
canonical_tex: "henon_dynamics/henon_additive_noise_moment_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_additive_noise_moment_route_a/paper/main.pdf"
source_sha256: "a92f5ad4dfd725facbdc4f34d74523d7efb444f821befb2e25777ca391a9caf0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Periodic Noise Words and Exact Markov Moments for an Additive-Noise Hénon Contraction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_additive_noise_moment_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_additive_noise_moment_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_additive_noise_moment_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_additive_noise_moment_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study an iid two-branch affine Hénon system in exact arithmetic. Strict contraction makes every finite noise word own a unique periodic state. All 126 rooted words through length six yield 23 primitive necklaces. The same source law closes a 15-dimensional Markov operator on polynomials of degree at most four, from which stationary covariance and a non-Gaussian fourth cumulant are recovered. These are finite random-dynamics certificates, not a global Fredholm or arithmetic construction.
author:
- 'Route-A finite certificate C123'
title: |
  Periodic Noise Words and Exact Markov Moments\
  for an Additive-Noise Hénon Contraction
```

## Markdown 正文

# Frozen additive-noise model

Let $\sigma_n\in\{-1,+1\}$ be iid and uniform, and freeze $$F_\sigma(x,y)=\left(\frac x2-\frac y4+\frac\sigma2,\frac x4\right),
 \qquad
 A=\begin{pmatrix}1/2&-1/4\\1/4&0\end{pmatrix}.$$ The common linear part has repeated eigenvalue $1/4$ and determinant $1/16$. The eigenvalues of $A^{\mathsf T}A$ are $$\frac3{16}\pm\frac{\sqrt2}{8},$$ both strictly below one. Each branch and every finite composition is therefore a strict affine contraction.

# Periodic noise-word atlas

For a chronological word $\omega=(\sigma_0,\ldots,\sigma_{n-1})$, write $F_\omega=F_{\sigma_{n-1}}\circ\cdots\circ F_{\sigma_0}$. Its linear part is $A^n$, so $I-A^n$ is invertible and $F_\omega$ has one exact fixed state. Cyclic rotations change the phase of the same oriented word orbit. We choose the lexicographically least rotation with $-<+$ and remove repeated words.

  period $n$              1   2   3    4    5    6   total
  --------------------- --- --- --- ---- ---- ---- -------
  rooted words tested     2   4   8   16   32   64     126
  primitive necklaces     2   1   2    3    6    9      23

Every row in the evidence ledger records its canonical word, all rational states, the chosen rooted length-$n$ block probability $2^{-n}$, $A^n$, and composition determinant $16^{-n}$. This row value is neither the total mass of its necklace nor an infinite periodic-orbit probability. The cutoff $n\le6$ is literal; no all-period completeness is asserted.

# Degree-four Markov operator

The model itself defines $$(Pf)(x,y)=\frac12 f(F_+(x,y))+\frac12 f(F_-(x,y)).$$ The 15-dimensional space $$\mathcal P_{\le4}=\operatorname{span}\{x^iy^j:i+j\le4\}$$ is invariant. In the graded monomial basis, the exact source-owned matrix $K=P|_{\mathcal P_{\le4}}$ satisfies $$\operatorname{tr}K=\frac{453}{256},\qquad \det K=2^{-80}.$$ All sixteen coefficients of $\det(I-zK)$ are stored in the evidence receipt.

Solving $K^{\mathsf T}\mu=\mu$ with $\mu(1)=1$ gives zero odd moments and $$\Sigma=\begin{pmatrix}\mu(x^2)&\mu(xy)\\\mu(xy)&\mu(y^2)\end{pmatrix}
 =\frac1{3375}\begin{pmatrix}1088&128\\128&68\end{pmatrix},
 \quad \det\Sigma=\frac{256}{50625}.$$ It obeys $\Sigma=A\Sigma A^{\mathsf T}+\operatorname{diag}(1/4,0)$ exactly. The fourth cumulant $$\mu(x^4)-3\mu(x^2)^2
 =-\frac{47789203456}{359401303125}$$ is nonzero, so we do not replace the stationary law by a Gaussian closure. With noise removed, the stable deterministic system has zero stationary covariance.

# Validation and boundary

From the package directory run

    python3 code/c123_noise_producer.py
    python3 code/c123_noise_checker.py
    python3 code/c123_sympy_crosscheck.py
    python3 code/c123_replay.py
    python3 code/c123_mutation.py

The independent checker, fresh symbolic reconstruction, canonical replay, and all 19 hostile mutations pass.

The canonical verdict is $(\texttt{A1\_WEAK},\texttt{A2\_FAIL},\texttt{A3\_FAIL},
\texttt{A4\_FAIL})$, overall `ROUTE_A_EXPLORATORY`. The finite word ledger has no prime-like target correspondence. The degree-four Markov determinant has no target-divisor match or analytic bridge, and no global analytic structure is established. We claim no complete random orbit atlas, global nuclear/Fredholm owner, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Pólya operator, or Route B. The firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.
