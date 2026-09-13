---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-127-outward-loewner-transport-guards"
canonical_tex: "zeta_mvp0/papers/RH-127-outward-loewner-transport-guards/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-127-outward-loewner-transport-guards/main.pdf"
source_sha256: "d6650da1bd5585a7ab69a903097f148ab9b475bc16712ec5cff71b09e8dfe94f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Outward Loewner Transport Guards Rigorous Cross-Assembly Congruence from Spectral-Norm Radii

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-127-outward-loewner-transport-guards>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-127-outward-loewner-transport-guards/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-127-outward-loewner-transport-guards/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-127-outward-loewner-transport-guards/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-127-outward-loewner-transport-guards/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The RH-115 audit showed that independently rounded Gram assemblies cannot be fused without an outward transport loss. We give the exact loss. Suppose $\|G-\widehat G\|\leq r_G$ and analogously for $D,G',D'$. A numerical Gram slack for $\widehat G'-aS^*\widehat GS$ becomes rigorous after subtracting $r_{G'}+a\|S\|^2r_G$. A numerical tail slack for $bS^*\widehat DS+\delta S^*\widehat GS-\widehat D'$ becomes rigorous after subtracting $r_{D'}+\|S\|^2(br_D+\delta r_G)$. Both guards are sharp for scalars. A 4,096-instance enclosure audit has zero false certifications. The theorem closes the validation logic but does not supply physical all-level radii.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Outward Loewner Transport Guards\
  Rigorous Cross-Assembly Congruence from Spectral-Norm Radii
```

## Markdown 正文

# Outward comparison theorem

[\[thm:guards\]]{#thm:guards label="thm:guards"} Assume spectral-norm enclosures for $G,D,G',D'$ with radii $r_G,r_D,r_{G'},r_{D'}$. Let $$\widehat\mu_G=\lambda_{\min}(\widehat G'-aS^*\widehat GS),$$ $$\widehat\mu_D=\lambda_{\min}(bS^*\widehat DS+delta S^*\widehat GS-\widehat D').$$ If $$\widehat\mu_G\geq r_{G'}+a\|S\|^2r_G,$$ then $G'\succeq aS^*GS$. If $$\widehat\mu_D\geq r_{D'}+\|S\|^2(br_D+\delta r_G),$$ then $D'\preceq bS^*DS+\delta S^*GS$.

Write each exact matrix as its approximation plus an error. The minimum eigenvalue changes by at most the spectral norm of the total error. Under congruence, $\|S^*ES\|\leq\|S\|^2\|E\|$. Applying the triangle inequality gives the two guards [@Moore1966; @HornJohnson1991].

# Sharpness

In dimension one, choose every enclosure error with the sign that reduces the exact slack. Then the exact Gram slack equals $\widehat\mu_G-r_{G'}-a|S|^2r_G$, and the exact tail slack equals $\widehat\mu_D-r_{D'}-|S|^2(br_D+\delta r_G)$. Hence no smaller universal guard follows from norm radii alone.

# Audit and route consequence

We sample 4,096 positive source pairs, gauges, factors, radii over five decades, and independent symmetric perturbations at their enclosure boundaries. Every generated instance has numerical reserve beyond the required guard. All 4,096 are certified and direct access to the hidden exact matrices finds zero false certifications. A scalar adversarial record attains both guard boundaries to error below $10^{-12}$.

![Certification reserve and the exact squared-gauge amplification of source radii.](<../../../../../zeta_mvp0/papers/RH-127-outward-loewner-transport-guards/figures/outward_loewner_transport_guards.pdf>){width="\\textwidth"}

RH-127 resolves the formal cross-assembly issue exposed in RH-115: a future validated recurrence may combine independent paths if it archives these radii and guards. It does not retroactively certify old unguarded paths and does not prove uniform physical radii. No Stage A, Hilbert--Polya, zeta-zero, or Riemann Hypothesis conclusion is claimed.
