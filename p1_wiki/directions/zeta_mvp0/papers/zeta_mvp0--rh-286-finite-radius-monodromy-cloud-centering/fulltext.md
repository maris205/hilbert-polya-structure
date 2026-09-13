---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-286-finite-radius-monodromy-cloud-centering"
canonical_tex: "zeta_mvp0/papers/RH-286-finite-radius-monodromy-cloud-centering/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-286-finite-radius-monodromy-cloud-centering/main.pdf"
source_sha256: "d0073a6969896a25ac27a1fe2a470aa4879ace267c631c3f1bfcc8f478336d48"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Radius Centering for Monodromy Cloud Audits

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-286-finite-radius-monodromy-cloud-centering>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-286-finite-radius-monodromy-cloud-centering/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-286-finite-radius-monodromy-cloud-centering/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-286-finite-radius-monodromy-cloud-centering/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-286-finite-radius-monodromy-cloud-centering/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The archived noisy-cloud audit used the limiting monodromy radius, although the exact edge-deflated shell has a finite-period radius. From the RH-17 multiplier law $|M_k|=C_M\lambda^k(1+o(1))$, we prove that comparing the $2(k-1)$ shell roots with the limiting radius creates an accumulated root-$\ell^1$ bias tending to $\beta|\log C_M|$. In contrast, the radial bias of every fixed pre-alias moment is $O(k^{-1})$. Re-centering the seven RH-15 clouds at archived multiprecision approximations to the finite-cycle radii reduces both total root errors and maximum moment defects. These are floating diagnostics, not interval or asymptotic noisy-cloud transport. The distinction explains why root-$\ell^1$ convergence to the limiting shell is stronger than the control needed for each fixed coefficientwise bridge; uniform determinant gluing still requires a growing weighted-prefix estimate.
author:
- Bin Wang
date: July 2026
title: 'Finite-Radius Centering for Monodromy Cloud Audits'
```

## Markdown 正文

# Finite shell radius

Let $$\beta=\frac1{r_H\sqrt\lambda},\qquad
 \beta_k=\frac{|M_k|^{-1/(2k)}}{r_H},\qquad r_H=0.85.$$ RH-17 proves $|M_k|=C_M\lambda^k(1+o(1))$ for a constant $C_M>0$. Hence $$\label{eq:beta-law}
 \beta_k=\beta\exp\left[-\frac{\log C_M}{2k}+o(k^{-1})\right].$$

[\[thm:centering\]]{#thm:centering label="thm:centering"} The radial matching cost between the finite and limiting edge-deflated shells satisfies $$2(k-1)|\beta_k-\beta|\longrightarrow
 \beta|\log C_M|.$$ For every fixed even $n$, $$2|\beta_k^n-\beta^n|
 =\frac{n\beta^n|\log C_M|}{k}+o(k^{-1}).$$ Odd shell moments vanish at both radii before the first alias.

Expand the exponential in [\[eq:beta-law\]](#eq:beta-law){reference-type="eqref" reference="eq:beta-law"}. There are $2(k-1)$ roots, all receiving the same radial displacement. For the moment statement, raise [\[eq:beta-law\]](#eq:beta-law){reference-type="eqref" reference="eq:beta-law"} to the fixed power $n$ and use the exact pre-alias ledger $-2\beta_k^n$ at even orders and zero at odd orders.

If $C_M\ne1$, the first limit is positive. The archived multiprecision diagnostic gives $C_M=1.9463429052\ldots$, but it is not a directed-rounding certificate; positivity of the numerical constant is therefore not promoted to a new computer-assisted theorem here.

# Seven-row re-audit

For an RH-15 cloud of effective degree $N$, we set $k=N+1$ and use the archived multiprecision approximation to the exact RH-17 radius $\beta_k$. The phase grid remains $j\pi/(N+1)$, $1\le j\le N$. The same root and moment diagnostics as RH-275 then give:

  quantity                          limiting-radius audit   finite-radius audit
  -------------------------------- ----------------------- ---------------------
  total root error range             $0.6424$--$1.2481$     $0.2841$--$0.8992$
  maximum pre-alias moment range     $0.5096$--$1.4573$     $0.3640$--$1.0450$

All seven finite-radius root errors are smaller than their limiting-radius counterparts. This comparison reuses frozen binary64 roots and multiprecision radii; it is not interval validation.

The theorem corrects the target of future aggregate audits. It does not select a canonical noisy pole cloud, certify its roots, or prove convergence as $\sigma\downarrow0$. Triggers 1 and 2 and Gates A--E remain open. No Hilbert--Polya or Riemann-hypothesis conclusion is involved.
