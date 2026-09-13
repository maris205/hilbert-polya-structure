---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-236-cloud-extracted-trace-moment-atlas"
canonical_tex: "zeta_mvp0/papers/RH-236-cloud-extracted-trace-moment-atlas/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-236-cloud-extracted-trace-moment-atlas/main.pdf"
source_sha256: "2538f12e3ca51e2073d02877d67390265db3a182227ea841c625a9000b3ce997"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Cloud-Extracted Trace-Moment Atlas through Order Twelve

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-236-cloud-extracted-trace-moment-atlas>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-236-cloud-extracted-trace-moment-atlas/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-236-cloud-extracted-trace-moment-atlas/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-236-cloud-extracted-trace-moment-atlas/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-236-cloud-extracted-trace-moment-atlas/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We compute the first twelve power traces of the 32 fine and Haar-coarse operators underlying the RH-222 cloud atlas. From each trace we subtract the Perron mode, parity mode, and shell-complete selected cloud. This produces 384 cloud-extracted trace moments without constructing the ill-conditioned Riesz projectors of RH-232.

  For the logarithmic unit-disk seminorm $$J_{12}(\tau)=\sum_{n=2}^{12}\frac{|\tau_n|}{n},$$ the batch maximum is $0.07593$. On the fine range $\sigma\le0.005$ it is $0.01067$. Across all endpoints and orders $2$--$12$, the largest observed root rate $|\tau_n|^{1/n}$ is $0.35989$. At the finest left endpoint the orders two through six have moduli $2.07\times10^{-2}$, $9.67\times10^{-4}$, $1.30\times10^{-5}$, $8.97\times10^{-6}$, and $5.47\times10^{-8}$.

  The atlas supplies strong finite-order evidence for a trace-based relative determinant route. It does not control order thirteen or the infinite tail, so Gate A remains open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: 'A Cloud-Extracted Trace-Moment Atlas through Order Twelve'
```

## Markdown 正文

# Trace extraction without a complement matrix

For a finite matrix $A$ with listed peripheral values $p,q$ and selected cloud $C$, define $$\label{eq:tau}
 \tau_n(A;C)=\operatorname{tr}(A^n)-p^n-q^n
 -\sum_{\lambda\in C}\lambda^n.$$ This quantity depends only on the finite matrix trace and selected eigenvalue multiset. It is therefore insensitive to the norm of the associated spectral projector.

[\[prop:reality\]]{#prop:reality label="prop:reality"} If $A$ is real, $p,q\in\mathbb R$, and $C$ is closed under complex conjugation with multiplicity, then $\tau_n(A;C)\in\mathbb R$ for every $n\ge1$.

The trace of a real matrix power is real. Every nonreal pair $\lambda,\overline\lambda$ contributes $\lambda^n+\overline\lambda^n=2\operatorname{Re}(\lambda^n)$, and real cloud values contribute real powers.

The archived imaginary parts are consequently roundoff diagnostics rather than independent spectral data. Their scale stays near ordinary floating arithmetic, providing a useful check that shell completion and multiplicity bookkeeping were preserved.

[\[prop:jet\]]{#prop:jet label="prop:jet"} Let $R_C(z)$ be the projection-free complementary product from RH-234. Near the origin, $$\log R_C(z)=-\sum_{n=2}^{m}\frac{\tau_n(A;C)}{n}z^n+O(z^{m+1}).$$ Consequently $$\sup_{|z|\le R}
 \left|\sum_{n=2}^{m}\frac{\tau_n(A;C)}{n}z^n\right|
 \le \sum_{n=2}^{m}\frac{|\tau_n(A;C)|}{n}R^n.$$

Expand each regularized eigenvalue factor using $\log((1-w)e^w)=-\sum_{n\ge2}w^n/n$, then subtract the selected cloud powers. The inequality is the triangle inequality.

# Sparse computation

The fine matrices have dimensions from $128$ to $4096$; the coarse matrices have half those dimensions. We form sparse powers recursively and take the diagonal sum. No unresolved eigenvalue decomposition is used. At the finest left endpoint, the twelfth power has approximately $1.49\times10^7$ stored entries, still below the dense $4096^2$ count.

The numerical traces are exact for the frozen double-precision sparse matrices up to ordinary floating arithmetic. They are not interval enclosures for a continuum operator.

# Moment decay across orders

    $n$      max all $|\tau_n|$      max fine $|\tau_n|$   all rate   fine rate
  ----- ----------------------- ------------------------ ---------- -----------
      2   $1.2952\times10^{-1}$    $2.0670\times10^{-2}$   $0.3599$    $0.1438$
      3   $2.9813\times10^{-2}$    $1.0758\times10^{-3}$   $0.3101$    $0.1025$
      4   $3.6811\times10^{-3}$    $1.6452\times10^{-4}$   $0.2463$    $0.1133$
      5   $7.6942\times10^{-4}$    $8.9640\times10^{-6}$   $0.2384$    $0.0978$
      6   $6.1019\times10^{-4}$    $2.9136\times10^{-6}$   $0.2912$    $0.1195$
      7   $3.0091\times10^{-4}$    $4.4089\times10^{-7}$   $0.3140$    $0.1236$
      8   $1.1350\times10^{-4}$    $2.2973\times10^{-8}$   $0.3213$    $0.1110$
      9   $3.7095\times10^{-5}$    $2.8206\times10^{-9}$   $0.3219$    $0.1122$
     10   $1.0776\times10^{-5}$   $1.9058\times10^{-10}$   $0.3186$    $0.1067$
     11   $2.7665\times10^{-6}$   $1.9500\times10^{-11}$   $0.3124$    $0.1063$
     12   $5.9728\times10^{-7}$   $1.9573\times10^{-12}$   $0.3029$    $0.1058$

  : Complete determinant-relevant order atlas. "Fine" means $\sigma\le0.005$, and each rate is the corresponding maximum modulus raised to the power $1/n$.

The sequence is not monotonically decreasing in every endpoint or every order. Complex phase cancellation and rank changes produce local spikes. The relevant observation is that the entire finite envelope stays far below the failed Hilbert--Schmidt budget of RH-229 [@WangRH229; @WangRH235].

Three summaries answer different questions. The root rate $|\tau_n|^{1/n}$ tests compatibility with geometric decay; the jet norm $J_{12}$ bounds a truncated logarithm on the unit disk; and the raw modulus records the actual coefficient scale. A small jet norm can be dominated by order two even if later root rates rise, which is why all three are archived rather than a single fitted exponent.

# Scale behavior

The fine-scale jet norms are small but not monotone. For example, the left channel rises again at $\sigma=0.00125$ because the fixed rank schedule changes by another shell. This prevents a direct Cauchy conclusion from the current selection. It motivates two separate tests:

1.  compare the same finite jet between the fine and coarse discretizations;

2.  choose the shell prefix by a trace tolerance rather than a predetermined rank.

RH-237 and RH-238 perform these tests.

# Numerical protocol and reproducibility boundary

The 384 cases are $32$ endpoints times orders one through twelve. Only the $352$ cases at orders two through twelve enter the regularized logarithm. The order-one values are retained as a bookkeeping check on peripheral subtraction. For each endpoint the recursion starts with the frozen sparse matrix and repeatedly multiplies by that same matrix; the trace is read from the diagonal after every multiplication. The cloud contribution is then subtracted from the stored shell-complete eigenvalue list.

This procedure avoids the two unstable operations diagnosed earlier in the route: no left/right overlap is inverted, and no full unresolved spectrum is diagonalized. Its cost is memory growth in the sparse powers. At dimension $4096$, the order-twelve power contains about $1.49\times10^7$ stored entries, which explains why twelve is a computational horizon rather than a mathematically distinguished order.

The archive verifies conjugacy closure, trace-array lengths, the unit-disk majorants, and consistency with the RH-235 second moments. It does not bound sparse multiplication roundoff or discretization error relative to a continuum transfer operator.

# The missing theorem

An order-$12$ jet can neither exclude large coefficients at later orders nor guarantee a zero-free disk for the full complementary determinant. The necessary strengthening is a uniform estimate $$|\tau_n(\sigma)|\le Mq^n,
 \qquad n\ge2,$$ with $q<1/R$ on a target disk $|z|\le R$. RH-240 proves that this all-order condition is sufficient. The present paper supplies only its first eleven nontrivial data points.

At least three tails remain compatible with the table: continued geometric decay, a delayed high-order spike, or a small tail produced by extracting too many regular modes into the moving cloud. The first would advance the determinant route, the second would block the proposed unit disk, and the third would give the wrong normalization despite excellent numerical bounds. This trichotomy is why an all-order envelope and a coefficient anchor are separate theorem obligations.

Gates A--E remain open, and no arithmetic spectral identification is claimed.
