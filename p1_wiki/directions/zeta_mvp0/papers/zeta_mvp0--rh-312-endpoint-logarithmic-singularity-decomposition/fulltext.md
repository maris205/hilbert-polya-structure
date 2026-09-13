---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-312-endpoint-logarithmic-singularity-decomposition"
canonical_tex: "zeta_mvp0/papers/RH-312-endpoint-logarithmic-singularity-decomposition/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-312-endpoint-logarithmic-singularity-decomposition/main.pdf"
source_sha256: "34b5b7a554b02dec74e8da467804b1b0bde28c815a8310edcb4fb3179e2c985f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Universal Logarithmic Singularity of the Endpoint Numerator

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-312-endpoint-logarithmic-singularity-decomposition>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-312-endpoint-logarithmic-singularity-decomposition/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-312-endpoint-logarithmic-singularity-decomposition/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-312-endpoint-logarithmic-singularity-decomposition/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-312-endpoint-logarithmic-singularity-decomposition/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The sharp deterministic coefficient law identifies the endpoint radius but does not by itself identify the boundary singularity. Using the exact odd anchor and the exponentially decaying even trace remainder, we prove that the endpoint-scaled logarithm is exactly $\log(1-w)+w$ plus a function analytic on a strictly larger disk. A repository-certified block constant gives an explicit lower radius $1.0376199\ldots$ for that remainder. This is an all-order deterministic theorem, not convergence of a noisy spectrum.
author:
- Bin Wang
date: July 2026
title: The Universal Logarithmic Singularity of the Endpoint Numerator
```

## Markdown 正文

# Normalized anchors

Put $q_*=(r_H\lambda)^{-1}$, $\rho_*=q_*^{-1}$, and $b_n=a_n\rho_*^n$. The odd formula of RH-263 gives $$b_n=(1+\lambda^{-n})^{-1}\qquad(n\ge3\text{ odd}).$$ For $n=2m$, RH-268 writes $$b_{2m}=2\lambda^{2m}\operatorname{tr}(T^m)
       +\frac{1-2\lambda^{-m}}{1-\lambda^{-2m}}.$$ If $m=3k+j$, the certified trace estimate is $$|\lambda^{2m}\operatorname{tr}(T^m)|
 \le C_j\delta^k,\qquad \delta<0.801254.$$

# Singularity theorem

There is a function $H_{\rm reg}$ analytic for $$|w|<r_{\rm reg},\qquad
 r_{\rm reg}\ge0.801254^{-1/6}=1.0376199142\ldots,$$ such that $$-\sum_{n\ge2}\frac{a_n\rho_*^n}{n}w^n
 =\log(1-w)+w+H_{\rm reg}(w).$$

Write $b_n=1+r_n$. At odd orders, $r_n=O(\lambda^{-n})$. The explicit even endpoint fraction differs from one by $O(\lambda^{-m})=O(\lambda^{-n/2})$. The trace term is $O(\delta^{n/6})$ after separating the three residue classes of $m$. Consequently $\sum r_nw^n/n$ converges normally on every compact subdisk of radius $\min\{\lambda,\sqrt\lambda,\delta^{-1/6}\}>1$. Finally, $$-\sum_{n\ge2}\frac{w^n}{n}=\log(1-w)+w,$$ which proves the claim.

The logarithmic branch point at $w=1$ is the complete nonanalytic endpoint part of the deterministic numerator logarithm. In particular, subtracting $\log(1-w)+w$ strictly enlarges the analytic disk.

# Scope

The result uses exact all-order coefficient identities and a certified geometric trace remainder; no finite-order fit is promoted. It neither constructs a positive or integer spectral cloud nor proves endpoint $H^2$ convergence of the actual mismatch. Gates A--E remain false/open.
