---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-278-positive-noise-s2-analytic-shell-transport"
canonical_tex: "zeta_mvp0/papers/RH-278-positive-noise-s2-analytic-shell-transport/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-278-positive-noise-s2-analytic-shell-transport/main.pdf"
source_sha256: "0a65e6addddac8dbf5c50b24bf942b6dada9576c99ee4ff524476cc864dbd4ec"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Positive-Noise Hilbert--Schmidt Analyticity and Local Shell Transport

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-278-positive-noise-s2-analytic-shell-transport>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-278-positive-noise-s2-analytic-shell-transport/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-278-positive-noise-s2-analytic-shell-transport/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-278-positive-noise-s2-analytic-shell-transport/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-278-positive-noise-s2-analytic-shell-transport/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Although the natural Hilbert--Schmidt family diverges at zero noise, it is analytic on every compact positive-noise interval. We use this to prove a local shell theorem: an exact isolated spectral cluster persists under one common contour with a uniform resolvent bound, and an exterior selector below the unit radius has a locally contractive quotient power. Thus the RH-269 package is automatic locally at positive noise. The theorem does not give a single rank-growing zero-noise selector.
author:
- Bin Wang
date: July 2026
title: 'Positive-Noise Hilbert--Schmidt Analyticity and Local Shell Transport'
```

## Markdown 正文

# Analytic family

For $0<\sigma_-<\sigma_+<\infty$, the folded Gaussian kernel and every $\sigma$ derivative are continuous and uniformly bounded on $[0,1]^2\times[\sigma_-,\sigma_+]$. Its row normalizer is uniformly positive.

The map $\sigma\mapsto A_\sigma$ is real analytic from $(0,\infty)$ into $\mathcal S_2(L^2(0,1))$. In particular, on every compact positive-noise interval, $\|A_\sigma-A_\tau\|_2\le L|\sigma-\tau|$ for some finite $L$.

Fix $\sigma_0>0$ and complexify the noise parameter in a disk avoiding zero. The unnormalized folded kernel and its row normalizer are holomorphic there. At $\sigma_0$ the normalizer has a positive minimum over $x\in[0,1]$; shrinking the disk keeps its complex modulus uniformly away from zero. The normalized kernel is therefore a bounded $L^2([0,1]^2)$-valued holomorphic map, by dominated difference quotients. Restriction to the real axis is real analytic. A finite cover of a compact positive-noise interval bounds the first derivative and gives the mean-value estimate.

# Local shell activation

Fix $\sigma_0>0$ and a circle $\Gamma=\{|z|=r\}$, $0<r<1$, disjoint from $\operatorname{spec}(A_{\sigma_0})$. Let $E_{\sigma_0}$ be the range of the Riesz projection for the finite exterior spectrum $|z|>r$. Nearby, write $E_\sigma$ for the transported Riesz range, $Q_\sigma$ for the orthogonal projection onto $E_\sigma^\perp$, and $C_\sigma=Q_\sigma A_\sigma Q_\sigma|_{E_\sigma^\perp}$.

For $\sigma$ near $\sigma_0$, the same circle is in the resolvent set, the exterior Riesz rank is constant, and $$\sup_{\sigma,z\in\Gamma}\|(z-A_\sigma)^{-1}\|<\infty.$$ The orthogonal quotient compressions $C_\sigma$ vary in $\mathcal S_2$, have spectral radius below $r$, and possess a uniform contractive power on a smaller neighborhood. Hence the RH-269 tail theorem applies locally.

Let $M_0=\sup_{z\in\Gamma}\|(z-A_{\sigma_0})^{-1}\|$. If $M_0\|A_\sigma-A_{\sigma_0}\|<1$, the Neumann identity gives the common resolvent and bound $M_0/(1-M_0\|A_\sigma-A_{\sigma_0}\|)$. Riesz ranks and orthogonal projections then vary continuously. Relative to $E_\sigma\oplus E_\sigma^\perp$, invariance of the Riesz range makes $A_\sigma$ block upper triangular with $C_\sigma$ as the interior diagonal block. Hence its spectrum is the interior spectral component and its radius is below $r<1$. Gelfand's formula supplies a contractive power at $\sigma_0$, stable on a smaller neighborhood by continuity.

# Boundary

This is a local fixed-rank chart. It neither glues the rank-growing noisy cloud to zero nor proves the coefficient bridge. Gates A--E remain open.
