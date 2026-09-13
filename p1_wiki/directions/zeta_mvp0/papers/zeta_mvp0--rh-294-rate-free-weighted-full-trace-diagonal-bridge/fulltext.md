---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-294-rate-free-weighted-full-trace-diagonal-bridge"
canonical_tex: "zeta_mvp0/papers/RH-294-rate-free-weighted-full-trace-diagonal-bridge/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-294-rate-free-weighted-full-trace-diagonal-bridge/main.pdf"
source_sha256: "c6fd44fa7b2bf449d62a31ce15c715a128129e79a6ab38d65048ad0819de652d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Rate-Free Weighted Diagonal Bridge for Full Noisy Traces

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-294-rate-free-weighted-full-trace-diagonal-bridge>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-294-rate-free-weighted-full-trace-diagonal-bridge/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-294-rate-free-weighted-full-trace-diagonal-bridge/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-294-rate-free-weighted-full-trace-diagonal-bridge/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-294-rate-free-weighted-full-trace-diagonal-bridge/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The archived noisy-trace/counterloop bridge was growing-prefix but unweighted. We show that the same fixed-order inputs already imply a weighted theorem after a sharper diagonal choice. At level $j$, choose the coefficient tolerance inversely proportional to $j\sum_{n=2}^jR^n/n$. Fixed-order noisy trace convergence and fixed-order finite-radius counterloop convergence then provide clocks $h_\sigma,k_\sigma\to\infty$, with $h_\sigma<2k_\sigma$, on which the full weighted constituent error tends to zero. The construction remains nonquantitative: $h_\sigma$ need not dominate any prescribed function of $\log(1/\sigma)$. It therefore does not reach the minimal RH-292 bridge clock and does not close the determinant interface.
author:
- Bin Wang
date: July 2026
title: 'A Rate-Free Weighted Diagonal Bridge for Full Noisy Traces'
```

## Markdown 正文

# Fixed-order inputs

Let $$e_{\sigma,k,n}=c_{\sigma,n}-s_{k,n}-a_n.$$ For each fixed $n\ge2$, the archived limits give $$c_{\sigma,n}\to c_n,\qquad s_{k,n}\to p_n,\qquad a_n=c_n-p_n.$$ Fix $R>1$ and define $$A_j(R)=\sum_{n=2}^j\frac{R^n}{n},\qquad
 \eta_j=\frac1{2jA_j(R)}.$$

# Weighted diagonal theorem

[\[thm:weighted\]]{#thm:weighted label="thm:weighted"} There are integer-valued clocks $h_\sigma,k_\sigma$ such that $$h_\sigma\to\infty,\qquad k_\sigma\to\infty,\qquad
 h_\sigma<2k_\sigma,$$ and $$E_\sigma^{(h)}(R):=
 \sum_{n=2}^{h_\sigma}
 \frac{|e_{\sigma,k_\sigma,n}|R^n}{n}\longrightarrow0.$$

For each $j\ge2$, fixed-order noisy convergence supplies $\delta_j>0$ such that $$\max_{2\le n\le j}|c_{\sigma,n}-c_n|\le\eta_j
 \quad(0<\sigma\le\delta_j).$$ Choose the $\delta_j$ strictly decreasing with $\delta_j\le j^{-1}$. Fixed-order shell convergence supplies $K_j^0$ such that $$\max_{2\le n\le j}|s_{k,n}-p_n|\le\eta_j
 \quad(k\ge K_j^0).$$ Set $K_1=0$, and recursively choose $K_j>\max\{K_{j-1},j/2,K_j^0\}$. On the slab $\delta_{j+1}<\sigma\le\delta_j$, set $h_\sigma=j$ and $k_\sigma=K_j$. Then $|e_{\sigma,k_\sigma,n}|\le2\eta_j$ for $2\le n\le j$, and hence $$E_\sigma^{(h)}(R)\le2\eta_jA_j(R)=j^{-1}.$$ For $\sigma>\delta_2$, define both clocks arbitrarily. Both clocks diverge and the recursive inequality gives the pre-alias condition.

# Protocol and exact boundary

The computation lists $A_j(7/5)$, the chosen tolerance $\eta_j$, and the resulting certified budget $1/j$. It evaluates the proof schedule only; it does not infer the unknown slab thresholds $\delta_j$ from finite data.

The theorem proves a weighted full-trace constituent on an unspecified slow clock. It gives no lower bound comparable with $\log(1/\sigma)/\log(10/7)$ and says nothing about the noisy modulus head. Thus the required logarithmic $E_\sigma$ and $D_\sigma$ budgets remain open. Gates A--E remain false/open, with no Hilbert--Polya or RH conclusion.
