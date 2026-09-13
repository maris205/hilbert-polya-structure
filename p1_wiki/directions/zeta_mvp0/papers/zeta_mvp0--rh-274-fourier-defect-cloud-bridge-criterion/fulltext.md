---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-274-fourier-defect-cloud-bridge-criterion"
canonical_tex: "zeta_mvp0/papers/RH-274-fourier-defect-cloud-bridge-criterion/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-274-fourier-defect-cloud-bridge-criterion/main.pdf"
source_sha256: "ebc2d3dbc38cddb478f6a817e4640ca58f0204977b1167d05281ad5e040a3e2f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Aggregate Fourier Defects in Rank-Growing Cloud Bridges

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-274-fourier-defect-cloud-bridge-criterion>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-274-fourier-defect-cloud-bridge-criterion/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-274-fourier-defect-cloud-bridge-criterion/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-274-fourier-defect-cloud-bridge-criterion/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-274-fourier-defect-cloud-bridge-criterion/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The canonical pole counterloop is a rank-growing root-of-unity shell. We show that pointwise radial and phase convergence of its roots is not enough to transport trace moments. Fixed moments are controlled by aggregate low-frequency Fourier defects. A common phase shift tending to zero as $(N+1)^{-1/2}$ makes the third moment grow like $\sqrt N$, giving an exact counterexample to any maximum-phase-only bridge. The example is logical and is not asserted to describe the noisy cloud.
author:
- Bin Wang
date: July 2026
title: 'Aggregate Fourier Defects in Rank-Growing Cloud Bridges'
```

## Markdown 正文

# Aggregate criterion

Let $\theta_{N,j}=j\pi/(N+1)$ and consider conjugate pairs $r_{N,j}e^{\pm i(\theta_{N,j}+\varepsilon_{N,j})}$. Put $r_{N,j}=\beta+\delta_{N,j}$, and let $S^*_{N,n}$ denote the moment with $r_{N,j}=\beta$ and $\varepsilon_{N,j}=0$.

For each fixed $n$, if $0\le r_{N,j},\beta\le B$ uniformly, then $$|S_{N,n}-S^*_{N,n}|
 \le 2nB^n\sum_{j=1}^N|\varepsilon_{N,j}|
 +2nB^{n-1}\sum_{j=1}^N|\delta_{N,j}|.$$ Consequently aggregate $\ell^1$ phase and radial defects tending to zero imply the RH-272 moment bridge at every fixed order.

Use $|e^{in\varepsilon}-1|\le n|\varepsilon|$ and the mean-value bound $|r^n-\beta^n|\le nB^{n-1}|r-\beta|$, then sum both conjugate members.

# Maximum-phase counterexample

Take the exact radii $r_{N,j}=\beta$ and the common shift $\varepsilon_{N,j}=\Delta_N=(N+1)^{-1/2}$. The maximum phase error tends to zero. Since the unshifted third moment vanishes, $$S_{N,3}=2\beta^3\sum_{j=1}^N
 \cos\!\left(\frac{3j\pi}{N+1}+3\Delta_N\right).$$ The exact sine sum is $\sum_{j=1}^N\sin(3j\pi/(N+1))=\cot(3\pi/(2(N+1)))$. Hence

$$S_{N,3}=-\frac{4\beta^3}{\pi}\sqrt{N+1}+o(\sqrt N).$$ Thus $\max_j|\varepsilon_{N,j}|\to0$ does not imply even a bounded third moment.

# Boundary

The theorem invalidates a logical extrapolation from finite phase fits. It does not prove that the archived family has a coherent shift or fails the aggregate criterion. No Gate status changes.
