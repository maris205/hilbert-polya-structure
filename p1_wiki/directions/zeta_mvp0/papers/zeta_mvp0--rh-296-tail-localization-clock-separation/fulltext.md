---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-296-tail-localization-clock-separation"
canonical_tex: "zeta_mvp0/papers/RH-296-tail-localization-clock-separation/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-296-tail-localization-clock-separation/main.pdf"
source_sha256: "62ee6a5c00b33eb7d92648ebb165faf09467b75b32976a2aa9b404ed44a3220a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Strict Separation Between Spectral-Tail and Orbit-Localization Clocks

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-296-tail-localization-clock-separation>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-296-tail-localization-clock-separation/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-296-tail-localization-clock-separation/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-296-tail-localization-clock-separation/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-296-tail-localization-clock-separation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The missing weighted bridge might appear approachable by extending the fixed-length Gaussian localization theorem to a logarithmic moving order. We show that the current architecture cannot overlap the projection-free tail clock. The Hilbert--Schmidt mass-and-cap tail at $q=1/2$ and $R=7/5$ requires slope at least $1/\log(10/7)=2.803673\ldots$. Boundary crowding forces the existing interior orbit-tube proof to have slope at most $1/\log\lambda=1.930709\ldots$. The two closed slope ranges are strictly disjoint. This is a rigorous proof-method obstruction. It does not rule out actual trace convergence obtained by a new moving boundary-layer or aggregate determinant argument.
author:
- Bin Wang
date: July 2026
title: 'A Strict Separation Between Spectral-Tail and Orbit-Localization Clocks'
```

## Markdown 正文

# The two clocks

Write $L_\sigma=\log(1/\sigma)$ and $m_\sigma=\lceil aL_\sigma\rceil$. The RH-283 mass-and-cap theorem gives the critical tail slope $$a_{\rm tail}=\frac1{\log(1/(qR))}
 =\frac1{\log(10/7)}
 =2.803673252057129\ldots.$$ At equality its certified mass-and-cap upper bound is $O(L_\sigma^{-1})$.

For a proposed prefix cut $m_\sigma$, let $$\ell_\sigma=2\left\lfloor\frac{m_\sigma-1}{2}\right\rfloor$$ be the largest even order below it. The boundary-cycle theorem gives cycles at this even order with clearance $$\Delta_{\ell_\sigma}\le C\lambda^{-\ell_\sigma},\qquad
 \lambda=1.678573510428322\ldots.$$ A proof uniform over every order below $m_\sigma$ must handle this even order. The existing Gaussian orbit-tube argument requires at least $\Delta_{\ell_\sigma}\gtrsim\sigma$, and its asymptotic form requires $\Delta_{\ell_\sigma}/\sigma\to\infty$. Thus its limiting prefix-slope ceiling is $$a_{\rm loc}=\frac1{\log\lambda}
 =1.930709419186936\ldots.$$

# Separation theorem

[\[thm:gap\]]{#thm:gap label="thm:gap"} There is no logarithmic slope $a$ that is both tail-admissible for the uniform RH-282 mass-and-cap estimate and admissible for the archived interior orbit-tube localization proof. Quantitatively, $$a_{\rm tail}-a_{\rm loc}
 =0.872963832870193\ldots>0,
\qquad
 \frac{a_{\rm tail}}{a_{\rm loc}}
 =1.452146669092140\ldots.$$ At the maximal localization slope the tail power exponent is $$a_{\rm loc}\log(10/7)-1=-0.3113643261\ldots,$$ so the mass-and-cap upper bound does not vanish. At every $a\ge a_{\rm tail}$, $$\frac{\Delta_{\ell_\sigma}}{\sigma}
 \le C'\sigma^{a\log\lambda-1}\longrightarrow0.$$

The first two displays are direct substitutions. Since $a_{\rm tail}>a_{\rm loc}$, the slope intervals do not meet. Also $a_{\rm tail}\log\lambda=1.452146\ldots>1$, so the clearance ratio tends to zero at the minimal tail slope and therefore at every larger slope; here $\ell_\sigma=aL_\sigma+O(1)$ absorbs parity and rounding into $C'$.

# Protocol and scope

The computation records the two exact slopes, their gap and ratio, the tail exponent at $a_{\rm loc}$, and the clearance exponents at $a_{\rm tail}$ and $a=4$. No endpoint traces are fitted.

The theorem blocks only the present isolated-interior-cycle proof. It does not prove that the physical noisy trace fails at logarithmic order, and it does not exclude cancellations, boundary-layer localization, or a direct contour aggregate. Gates A--E remain false/open.
