---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-holomorphic-complex-transfer"
canonical_tex: "henon_dynamics/henon_holomorphic_complex_transfer/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_holomorphic_complex_transfer/paper/main.pdf"
source_sha256: "4c488e548bdd0a8dda50c1b5cd583f86e44888e19349034e7ebaf68da2f86d0c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Holomorphic Hénon Cycle and Transfer-Ownership Pilot

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_holomorphic_complex_transfer>)
- [规范 TeX](<../../../../../henon_dynamics/henon_holomorphic_complex_transfer/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_holomorphic_complex_transfer/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_holomorphic_complex_transfer/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze the complex polynomial automorphism $F(z,w)=(w,w^2-z/4)$ and solve its period-one and period-two equations exactly. Lefschetz-type Jacobian weights give the trace values $L_1=0$ and $L_2=-1664/1725$, hence a formal determinant prefix $1+832z^2/1725$. The inverse pullback has coordinate degrees $2,4,8$ after three iterates, which is a precise warning that finite polynomial Galerkin truncations do not by themselves supply a source-native Fredholm owner. This is an exact finite A2 prefix; complete complex coding, nuclearity, and a positive prime-like clock remain open.
author:
- 'Anonymous Route-A report'
title: 'A Holomorphic Hénon Cycle and Transfer-Ownership Pilot'
```

## Markdown 正文

# Frozen map and cycles

Let $$F(z,w)=(w,w^2-\tfrac14z),
\qquad
DF(z,w)=\begin{pmatrix}0&1\\-1/4&2w\end{pmatrix}.$$ The fixed-point equation is $x(x-5/4)=0$. Eliminating $y$ from $y=x^2-x/4$ and $x=y^2-y/4$ gives $$\operatorname{Res}_y= -x(4x-5)(4x^2+3x+3)/16.$$ Thus $F^2$ has four fixed points, with one complex-conjugate primitive two-cycle. For a fixed point of $F^n$, use the exact weight $1/\det(I-DF^n)$.

# Exact trace prefix

The two fixed points of $F$ have denominators $5/4$ and $-5/4$, so their weights cancel and $L_1=0$. At the four points of $F^2$ the denominators are $25/16$, $-75/16$, and $-23/16$ twice. Consequently $$L_2=\frac{16}{25}-\frac{16}{75}-\frac{32}{23}=-\frac{1664}{1725}.$$ The formal trace-to-determinant relation gives $$D(z)=\exp\left(-L_1z-\frac{L_2}{2}z^2+O(z^3)\right)
 =1+\frac{832}{1725}z^2+O(z^3).$$

The resultant, the four period-two points, the two weighted traces, and the displayed determinant coefficient are independently reproduced by the exact checker and a SymPy resultant calculation.

The checker recomputes the two elimination equations and the Jacobian products without importing producer data. The symbolic cross-check verifies the same resultant and rational coefficient.

# Ownership obstruction

The inverse is $$F^{-1}(z,w)=(4z^2-4w,z).$$ Pulling back the coordinate $z$ raises total degree from $1$ to $2$, then $4$, then $8$. Hence the obvious finite polynomial-degree spaces are not invariant. A genuine holomorphic Fredholm construction would need a named function space, compactness/nuclearity, and a tail estimate; a finite matrix or a post-hoc diagonal cannot replace those arguments.

# Route-A verdict and scope

The exact finite ledger earns 'A2\_CERTIFIED\_PREFIX'; complete complex primitive-orbit coding and a positive intrinsic clock are not proved, so 'A1\_OPEN'. We do not claim a global complex repeller, an analytic Fredholm determinant, prime correspondence, Riemann zeros, automorphy, or a Hilbert--Pólya operator. All source, checker, replay, mutation, and manifest files are distributed with the paper.
