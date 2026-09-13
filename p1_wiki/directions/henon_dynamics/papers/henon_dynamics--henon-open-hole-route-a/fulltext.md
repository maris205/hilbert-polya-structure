---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-open-hole-route-a"
canonical_tex: "henon_dynamics/henon_open_hole_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_open_hole_route_a/paper/main.pdf"
source_sha256: "c90d771ab925be8b34eeaebc961be26926007c2b9dd02662386fe7a8c7e60d5c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Open-Hole Hénon Survivor and Its Exact Escape Determinant

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_open_hole_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_open_hole_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_open_hole_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_open_hole_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze the certified four-state local Hénon symbolic interface and remove one geometric state before every iterate. The surviving three-state matrix has exact determinant $1-z-z^3$. We enumerate rooted survivor words, primitive necklaces, and escape traces through period twelve, with independent and symbolic checks. This is a discrete open-transfer certificate: it does not yet prove that a geometric open Hénon operator is analytic or nuclear, and it makes no arithmetic or Hilbert--Pólya claim.
author:
- 'Anonymous Route-A report'
title: 'An Open-Hole Hénon Survivor and Its Exact Escape Determinant'
```

## Markdown 正文

# Frozen hole

The inherited source/target adjacency is $$A=\begin{pmatrix}1&0&1&0\\1&0&0&0\\0&1&0&1\\0&1&0&0\end{pmatrix}.$$ We delete state $3$ before each iterate. The survivor matrix is therefore $$B=\begin{pmatrix}1&0&1\\1&0&0\\0&1&0\end{pmatrix}.$$ The hole is frozen; it is not selected after looking at traces or zeros.

# Exact escape ledger

Direct expansion gives $$\det(I-zB)=1-z-z^3.$$ If $t_n=\operatorname{tr}(B^n)$ and $p_n$ counts primitive survivor necklaces, then $$t_n=\sum_{d\mid n}d p_d.$$ The first twelve rooted trace counts are $$1,1,4,5,6,10,15,21,31,46,67,98.$$

The open matrix, determinant, trace sequence, and primitive inversion are reproduced exactly by an independent implementation and a SymPy calculation.

The checker reconstructs the principal submatrix from the frozen adjacency, computes matrix powers, and applies divisor inversion. The symbolic script independently expands the determinant and traces.

# Controls and boundary

Deleting states $0,1,2,3$ instead gives determinants $1$, $1-z$, $1-z$, and $1-z-z^3$, respectively. Thus the chosen hole is a genuine frozen geometry choice rather than a relabeling convention. The present theorem is only a finite symbolic open-transfer result. A future A2 upgrade must prove that the geometric hole has no boundary periodic orbits and that the same open transfer operator is compact/nuclear on a named space. The preregistered verdict is 'A1\_PARTIAL\_CERTIFIED', 'A2\_CERTIFIED\_PREFIX', 'A3\_NOT\_ADDRESSED', 'A4\_FAIL'. No prime table, zero table, Euler factor, or Route-B object is used.
