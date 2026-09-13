---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-first-passage-generating-polynomial"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_generating_polynomial/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_generating_polynomial/paper/main.pdf"
source_sha256: "9b01854013f8ee6462dbbb5b81273d3d6d4e6116f1f2a165603033acf886a4cb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Generating Polynomials for Finite First Passage

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_generating_polynomial>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_generating_polynomial/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_generating_polynomial/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_generating_polynomial/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We encode the twenty frozen first-passage laws of C88 as exact integer generating polynomials. Every polynomial has all seventeen coefficients, support spectrum, and derivatives at one through order six. Stirling inversion recovers the C89 ordinary moments exactly. The certificate is finite combinatorics under the stated scope firewall.
author:
- Anonymous
title: Exact Generating Polynomials for Finite First Passage
```

## Markdown 正文

# Polynomial certificate

For target $H_i$ let $N_i(t)=\#\{\pi:T_i(\pi)=t\}$ and $$G_i(z)=\sum_{t=0}^{16}N_i(t)z^t,\qquad P_i(z)=G_i(z)/16!.$$ Then $P_i^{(m)}(1)=\mathbb E[(T_i)_m]$. With $S(r,m)$ denoting a Stirling number of the second kind, $$\mathbb E[T_i^r]=\sum_{m=0}^r S(r,m)P_i^{(m)}(1).$$

All 20 polynomials have normalized nonnegative integer coefficients and the identity above recovers every C89 raw moment of orders $0$ through $6$.

The coefficients are the exact C88 first-passage counts. Differentiating a finite polynomial gives falling-factorial moments, and Stirling inversion is the standard finite change of basis from falling factorials to powers.

  certified object                 count
  ------------------------------ -------
  target polynomials                  20
  coefficient cells                  340
  support/degree/gcd rows             20
  derivative orders per target         7
  raw-moment recoveries              140

# Scope

No arithmetic/local data, Euler factors, root numbers, automorphy, full Burnside/table-of-marks, or Hilbert--Pólya operator is claimed.
