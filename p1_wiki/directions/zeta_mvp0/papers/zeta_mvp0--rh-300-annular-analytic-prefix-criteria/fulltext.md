---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-300-annular-analytic-prefix-criteria"
canonical_tex: "zeta_mvp0/papers/RH-300-annular-analytic-prefix-criteria/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-300-annular-analytic-prefix-criteria/main.pdf"
source_sha256: "852a543a9718d7385034214c3c8281f642c0f0f19186054b558cbac68d18dc5c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Annular $H^\infty$ and Hardy Criteria for the Direct Weighted Prefix

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-300-annular-analytic-prefix-criteria>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-300-annular-analytic-prefix-criteria/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-300-annular-analytic-prefix-criteria/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-300-annular-analytic-prefix-criteria/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-300-annular-analytic-prefix-criteria/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The remaining determinant bridge is an absolute weighted coefficient norm, but it need not be proved coefficient by coefficient or root by root. We give two direct analytic criteria. If the logarithmic mismatch is small in $H^\infty$ on any circle strictly outside the target disk, Cauchy's estimate controls the full weighted coefficient norm. A vanishing $H^2$ boundary norm on the same annulus also suffices by Cauchy--Schwarz. Both bounds are explicit. At radius $1.41$, which lies between the target radius $1.4$ and the certified deterministic radius $1.426787\ldots$, their constants are $139.007\ldots$ and $8.292\ldots$. An endpoint polynomial family shows that vanishing $H^2$ norm on the target circle alone is insufficient. No actual noisy annular convergence is asserted.
author:
- Bin Wang
date: July 2026
title: Annular $H^\infty$ and Hardy Criteria for the Direct Weighted Prefix
```

## Markdown 正文

# Logarithmic mismatch

Let $$g_\sigma(z)=\sum_{n\ge2}
 \frac{\tau_{\sigma,n}-a_n}{n}z^n$$ be holomorphic on a neighborhood of the closed disk $|z|\le\rho$, where $\rho>R>0$. Define the full absolute coefficient norm $$P_\sigma^\infty(R)=\sum_{n\ge2}
 \frac{|\tau_{\sigma,n}-a_n|R^n}{n}.$$

# Two annular criteria

[\[thm:analytic\]]{#thm:analytic label="thm:analytic"} Put $x=R/\rho<1$.

1.  If $\sup_{|z|\le\rho}|g_\sigma(z)|\le M_\sigma$, then $$P_\sigma^\infty(R)\le M_\sigma\frac{x^2}{1-x}.$$

2.  If $$\|g_\sigma\|_{H^2(\rho)}^2:=
     \sum_{n\ge2}
     \frac{|\tau_{\sigma,n}-a_n|^2\rho^{2n}}{n^2}
     \le H_\sigma^2,$$ then $$P_\sigma^\infty(R)\le
     H_\sigma\frac{x^2}{\sqrt{1-x^2}}.$$

In particular, $M_\sigma\to0$ or $H_\sigma\to0$ makes the full norm vanish. Every moving prefix is bounded by $P_\sigma^\infty(R)$, so the RH-292 shortened prefix follows.

Cauchy's coefficient estimate gives $$\frac{|\tau_{\sigma,n}-a_n|}{n}\le M_\sigma\rho^{-n},$$ and summing the geometric series proves the first bound. For the second, apply Cauchy--Schwarz to $$\sum_{n\ge2}
 \left(
 \frac{|\tau_{\sigma,n}-a_n|\rho^n}{n}
 \right)x^n.$$ The square sum of $x^n$ from $n=2$ onward is $x^4/(1-x^2)$.

# Endpoint obstruction

[\[thm:endpoint\]]{#thm:endpoint label="thm:endpoint"} The strict radius gap in the $H^2$ criterion cannot be removed uniformly. For every $N\ge1$, let $$g_N(z)=\frac1N\sum_{n=2}^{N+1}(z/R)^n.$$ Then $$\|g_N\|_{H^2(R)}=N^{-1/2}\longrightarrow0,
\qquad
 \sum_{n=2}^{N+1}|[z^n]g_N|R^n=1.$$

There are $N$ coefficients, each with boundary-scaled modulus $1/N$. Their square sum is $1/N$, while their absolute sum is one.

# Certified annulus and protocol

The deterministic coefficient radius is $\rho_*=0.85\lambda=1.426787483864073\ldots$. Taking $\rho=1.41$ and $R=1.4$ gives $$\frac{x^2}{1-x}=139.0070921986\ldots,\qquad
 \frac{x^2}{\sqrt{1-x^2}}=8.2924678943\ldots.$$ The computation records these constants and the endpoint family. It does not estimate $g_\sigma$ for the noisy operator.

The theorem is a reopening criterion, not a verified annular bridge. If activated it supplies the direct $P_\sigma^\infty$ bound, but no such $H^\infty$ or $H^2$ convergence is currently proved. Gates A--E remain false/open and no Hilbert--Polya, zeta-divisor, or RH statement follows.
