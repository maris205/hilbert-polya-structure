---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-319-genuine-spectral-annular-envelope-saturation"
canonical_tex: "zeta_mvp0/papers/RH-319-genuine-spectral-annular-envelope-saturation/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-319-genuine-spectral-annular-envelope-saturation/main.pdf"
source_sha256: "e765d2065084ec5054ede58ab34c557c75bb6c1f1593c60754a4c87b86979482"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Sharp Annular Rates Realized by Genuine Finite Spectra

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-319-genuine-spectral-annular-envelope-saturation>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-319-genuine-spectral-annular-envelope-saturation/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-319-genuine-spectral-annular-envelope-saturation/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-319-genuine-spectral-annular-envelope-saturation/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-319-genuine-spectral-annular-envelope-saturation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-306 proved that the annular mass-rate barrier is sharp for an abstract coefficient envelope but deliberately supplied no spectral realization. We close that scoped gap. The exact integer spectra of RH-316 attain the same power and logarithmic rate in both $H^\infty$ and $H^2$ on every strict certified annulus. This upgrades information-class sharpness to the genuine finite normal spectral class, without claiming that the actual noisy spectrum has the sharp rate.
author:
- Bin Wang
date: July 2026
title: Sharp Annular Rates Realized by Genuine Finite Spectra
```

## Markdown 正文

# Rate and spectral approximants

Put $R=7/5$. For a finite conjugate multiset $\mathcal S\subset
\{|\mu|\le q\}$, write $$\tau_n(\mathcal S)=\sum_{\mu\in\mathcal S}\mu^n,
 \qquad
 g_{\mathcal S}(z)=\sum_{n\ge2}
 \frac{\tau_n(\mathcal S)-a_n}{n}z^n,
 \qquad
 M_2(\mathcal S)=\sum_{\mu\in\mathcal S}|\mu|^2.$$ Let $$\kappa(\rho)=
 \frac{\log(1/(q_*\rho))}{\log(q_*/q)},
 \qquad R<\rho<\rho_*.$$ For $X=H^\infty(\rho)$ or $H^2(\rho)$, define the finite-spectral extremal error $$E_X(M;\rho)=\inf_{M_2(\mathcal S)\le M}\|g_{\mathcal S}\|_X.$$

For every fixed $R<\rho<\rho_*$ and either choice of $X$, $$E_X(M;\rho)=\Theta_\rho\left(
 \frac{M^{-\kappa(\rho)}}{\log M}
 \right)\qquad(M\to\infty).$$ The upper bound is attained, up to constants, by the exact-prefix spectra of RH-316.

RH-305 applies to every modulus-capped spectrum. If its actual mass is at most $M$, monotonicity of $M^{-\kappa(\rho)}/\log M$ gives the displayed lower bound for the infimum.

For the upper bound, take the RH-316 spectrum matching through order $N$. RH-317 gives $M_N\le Cs^N$, where $s=q_*/q$. The target tail after the matched prefix is $O((q_*\rho)^N/N)$. For the spectral tail, the mass envelope gives $$\sum_{n>N}\frac{|\tau_n|\rho^n}{n}
 \le M_Nq^{-2}\sum_{n>N}\frac{(q\rho)^n}{n}
 =O_\rho((q_*\rho)^N/N).$$ The same coefficient estimate gives the $H^2$ upper bound. Since $N$ may be chosen as the largest integer with $Cs^N\le M$, one has $N=(\log M)/\log s+O(1)$, and this is the displayed mass rate.

At $\rho=1.41$, $\kappa(\rho)=0.035045705260961\ldots$.

The theorem constructs genuine power sums but not the actual noisy eigenvalues. It proves spectral-class sharpness only; actual convergence and its rate remain open. Gates A--E remain false/open.
