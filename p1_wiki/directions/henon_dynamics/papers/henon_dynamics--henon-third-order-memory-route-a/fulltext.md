---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-third-order-memory-route-a"
canonical_tex: "henon_dynamics/henon_third_order_memory_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_third_order_memory_route_a/paper/main.pdf"
source_sha256: "a0d54d78013f69960dd65a140ce9af336da275764f75d8e8cb1517b64258d9e6"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Third-Order Memory Hénon Map: An Exact Low-Period Pilot

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_third_order_memory_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_third_order_memory_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_third_order_memory_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_third_order_memory_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study the three-dimensional recurrence $G(x,y,z)=(x^2-55/16-y-z/2,x,y)$, in which two delay coordinates are part of the state. Exact symbolic elimination gives two fixed points and one genuine primitive period-two cycle. The ordered Jacobian product has determinant $1/4$ and trace $-15/4$. Degree growth $2,4,8$ shows why these finite monodromy data do not automatically define a polynomial Fredholm owner.
author:
- 'Anonymous Route-A report'
title: 'A Third-Order Memory Hénon Map: An Exact Low-Period Pilot'
```

## Markdown 正文

# Map and fixed locus

The map is $$G(x,y,z)=(x^2+a-y-\kappa z,x,y),\qquad
 (a,\kappa)=(-55/16,1/2).$$ Its Jacobian at a state with first coordinate $u$ is $$J(u)=\begin{pmatrix}2u&-1&-1/2\\1&0&0\\0&1&0\end{pmatrix},
 \qquad \det J(u)=-1/2.$$ The fixed equations force $x=y=z$ and give $$x=5/4-\sqrt5,\qquad x=5/4+\sqrt5.$$

# Primitive two-cycle and monodromy

Direct substitution gives the exact cycle $$p_0=(-7/4,1/4,-7/4)\longmapsto
 p_1=(1/4,-7/4,1/4)\longmapsto p_0.$$ It is not fixed. With $M_2=J(1/4)J(-7/4)$, exact multiplication gives $$M_2=\begin{pmatrix}-11/4&-1&-1/4\\-7/2&-1&-1/2\\1&0&0\end{pmatrix},
 \quad \det M_2=1/4,\quad \operatorname{tr}M_2=-15/4,$$ and $$\det(\lambda I-M_2)=
 \frac{4\lambda^3+15\lambda^2-2\lambda-1}{4}.$$ The fixed-point characteristic polynomials are recorded in the exact evidence receipt and independently recomputed by SymPy.

The fixed locus, primitive two-cycle, Jacobian determinants, and displayed monodromy polynomial are reproduced by an independent symbolic checker.

The checker solves the three fixed equations, evaluates both directions of the proposed cycle, and recomputes the ordered Jacobian product without importing producer functions.

# Memory and Route-A boundary

The first coordinate degrees after three forward iterates are $2,4,8$. Thus a finite polynomial-degree truncation is not invariant by inspection; any analytic transfer construction would need a named function space and a tail estimate. The finite ledger earns 'A1\_WEAK' and 'A2\_CERTIFIED\_PREFIX', with 'A3\_NOT\_ADDRESSED' and 'A4\_FAIL'. No complete three-dimensional orbit atlas, arithmetic data, analytic Fredholm determinant, or Route-B object is claimed. The scope firewall is 'NO\_BAD\_EULER\_OR\_ROOT\_NUMBER'.
