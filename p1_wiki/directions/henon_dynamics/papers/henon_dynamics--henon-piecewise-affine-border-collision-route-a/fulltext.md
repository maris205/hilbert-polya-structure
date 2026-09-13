---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-piecewise-affine-border-collision-route-a"
canonical_tex: "henon_dynamics/henon_piecewise_affine_border_collision_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_piecewise_affine_border_collision_route_a/paper/main.pdf"
source_sha256: "dc2f500ee6477caeb893f18b2900ccf6bb7a99b09aab0d893894020f6b83aafa"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Piecewise-Affine Border-Collision Hénon Pilot

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_piecewise_affine_border_collision_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_piecewise_affine_border_collision_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_piecewise_affine_border_collision_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_piecewise_affine_border_collision_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze a two-branch piecewise-affine Hénon map with a border at $x=0$. Exact affine returns verify every binary itinerary through period eight and give 71 primitive necklaces. A separately frozen branch weight produces an exact finite weighted transfer determinant. The construction is a switching pilot only: it does not assert a global Markov partition or an analytic Fredholm operator.
author:
- 'Anonymous Route-A report'
title: 'A Piecewise-Affine Border-Collision Hénon Pilot'
```

## Markdown 正文

# Frozen switching map

For $s\in\{0,1\}$ let $$P_s(x,y)=(-5x+c_s-y,x),\qquad (c_0,c_1)=(-2,2),$$ with domains $x<0$ and $x>0$. The border $x=0$ is excluded rather than assigned after counting. Both branch derivatives equal $$B=\begin{pmatrix}-5&-1\\1&0\end{pmatrix},\qquad\det B=1.$$ The affine translation is retained in the orbit check, so the calculation is not an averaged transition matrix.

# Exact finite ledger

For each binary word $w$ of length at most eight we solve $(I-B^n)q=t_w$ over the rationals and iterate the resulting point. Every word has a unique non-border point with the declared itinerary. Cyclic canonicalization gives the primitive counts $$(2,1,2,3,6,9,18,30),$$ for periods one through eight, totaling 71. The identity

$$t_n=\sum_{d\mid n}d p_d$$ is therefore a finite exact necklace relation.

To expose branch chronology without fitting a parameter, freeze $\rho_0=1/2$ and $\rho_1=2/3$ and put the destination-weighted block $\rho_jB$ on every allowed transition $i\to j$. The resulting four-dimensional screening matrix $A$ has $$\det(I-zA)=\frac{49z^2+210z+36}{36},
 \qquad \det(I-zA_{\rm unweighted})=1+10z+4z^2.$$ The weighted trace prefix begins $$-\frac{35}{6},\quad \frac{1127}{36},\quad -\frac{18865}{108},\quad
 \frac{1265327}{1296}.$$

The affine-return ledger, primitive quotient, determinant, and trace prefix are reproduced by an independent implementation and a SymPy calculation.

The checker reconstructs the affine return and branch inequalities without calling producer functions. The symbolic script independently expands the four-by-four determinant and powers.

# Route-A boundary

The finite switching certificate earns 'A1\_PARTIAL\_CERTIFIED' and 'A2\_CERTIFIED\_PREFIX'. It does not prove that the border map has a complete geometric coding, that boundary orbits are absent at all periods, or that the weighted matrix is a Fredholm determinant. The package makes no arithmetic or Route-B claim. All evidence is protected by the 'NO\_BAD\_EULER\_OR\_ROOT\_NUMBER' scope firewall.
