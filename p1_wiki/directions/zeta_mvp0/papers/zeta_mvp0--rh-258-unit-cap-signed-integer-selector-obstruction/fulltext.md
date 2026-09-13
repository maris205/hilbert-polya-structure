---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-258-unit-cap-signed-integer-selector-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-258-unit-cap-signed-integer-selector-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-258-unit-cap-signed-integer-selector-obstruction/main.pdf"
source_sha256: "8edffe6a7422223191a37ac9c852b7c78fdec93c070dd5f0126bb6c07cda7dab"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Unit-Cap Signed-Integer Selector Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-258-unit-cap-signed-integer-selector-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-258-unit-cap-signed-integer-selector-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-258-unit-cap-signed-integer-selector-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-258-unit-cap-signed-integer-selector-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-258-unit-cap-signed-integer-selector-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-257 proves that integer exponents are necessary for a single-valued finite determinant quotient. We audit the first bounded signed lattice by assigning each complete RH-254 shell a weight in $\{-1,0,1\}$. Mixed-integer linear optimization gives zero anchor passes at all 32 endpoints. Optimal weighted distances range from $0.106074$ to $0.353490$, which is $7.98$--$93.48$ times the local tolerance. The optimizations cover $39{,}417{,}456{,}084{,}975{,}216$ lattice points in aggregate with zero reported MIP gap. This is a unit-cap obstruction only; larger caps and operator realization remain open.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'Unit-Cap Signed-Integer Selector Obstruction'
```

## Markdown 正文

# The necessary integer lattice

For one endpoint let $v_j\in\mathbb R^{11}$ be the order-$2$--$12$ power vector of the $j$th conjugate-complete shell, and let $d$ be the anchored target difference. RH-257 shows why a continuous signed weight is not enough: noninteger exponents create monodromy [@WangRH257]. We therefore define the first integer relaxation $$\mathcal L_1=\left\{\sum_{j=1}^Jw_jv_j:w_j\in\{-1,0,1\}\right\}.
 \label{eq:lattice}$$

Every vector in $\mathcal L_1$ has a single-valued rational product at the level of formal shell factors. This remains only a necessary condition: negative or repeated shell multiplicities must still be realized by an actual quotient or superdeterminant.

[\[prop:milp\]]{#prop:milp label="prop:milp"} The distance $$\min_{w\in\{-1,0,1\}^J}
 \sum_{n=2}^{12}\frac{|d_n-(Vw)_n|}{n}
 \label{eq:objective}$$ is an exact-integrality mixed-integer linear program with $J$ integer variables and eleven nonnegative residual variables.

Introduce $u_n\ge0$ and the two linear inequalities $d_n-(Vw)_n\le u_n$ and $(Vw)_n-d_n\le u_n$. Minimize $\sum_nu_n/n$ under integer bounds $-1\le w_j\le1$.

# Finite audit

The shell counts range from 20 to 34, so one endpoint contains $3^J$ lattice points. The optimizer searches this class implicitly rather than enumerating every vector. All 32 solves report zero MIP gap.

  quantity                                            value
  -------------------------------- ------------------------
  endpoints                                              32
  aggregate lattice points           39,417,456,084,975,216
  anchor passes                                           0
  distance range                         0.106074--0.353490
  distance/tolerance range                      7.98--93.48
  minimum failure margin                           0.103574
  integrality-gap range                  0.106074--0.353490
  nonzero weights in an optimum                      20--30
  maximum branch-and-bound nodes                        368
  maximum reported MIP gap                                0

No margin-32 complete-shell weight vector with entries in $\{-1,0,1\}$ reaches the deterministic anchor within the archived endpoint tolerance.

At every endpoint the global MILP objective exceeds the local tolerance. The reported exact-integrality gap is zero.

# Boundary and route decision

The theorem does not exclude weights of magnitude two or larger. Such a fit would still not prove that the noisy operator contains the required signed copies. Rather than escalating an increasingly artificial multiplicity cap, the next paper returns to the exact orthogonal quotient and its block powers, where cancellation is operator-derived rather than fitted [@WangRH245; @WangRH246].

Gates A--E remain false/open. No Hilbert--Polya operator, Riemann-zero identification, zeta-divisor equality, or RH implication is claimed.
