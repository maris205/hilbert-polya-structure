---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-defect-duality"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_defect_duality/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_defect_duality/paper/main.pdf"
source_sha256: "e89e1ece987468b90ca0775e91b5e63c731710d9c7917d4c7dce1a399247fc59"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Defect--Cokernel Duality for a Restricted Table-of-Marks Map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_defect_duality>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_defect_duality/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_defect_duality/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_defect_duality/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The preceding exact calculations give a restricted $16\times16$ self-mark matrix $M$ and a three-dimensional C65 saturation defect. We identify the embedded defect subgroup inside the C66 cokernel and compute the quotient on both column and row sides. The defect subgroup is $(\mathbb Z/8)\oplus(\mathbb Z/2)^2$, while the quotient has invariant factors $(1^4,2^8,4^2,12,144)$. An explicit transpose-side congruence lattice gives the dual quotient with the same invariants. Every statement concerns only the frozen sixteen subgroup types.
author:
- Anonymous
title: 'A Defect--Cokernel Duality for a Restricted Table-of-Marks Map'
```

## Markdown 正文

# Question and scope

Let $G=W(E_6)$ and let $S_1,\ldots,S_{16}$ be the fixed subgroup types from the preceding source package. Write $$M_{ij}=|(G/S_j)^{S_i}|,
 \qquad M\in\operatorname{Mat}_{16}(\mathbb Z).$$ The matrix has determinant $226492416=2^{23}3^3$ and is the exact C64 restricted self-mark map. C65 supplies three integer kernel vectors $$z_1=S_{10}-S_9,\quad
 z_2=-S_2-S_3-S_5-S_6+S_{11}+S_{12}+S_{13}+S_{14},\quad
 z_3=S_{16}-S_{15}.$$ Put $C=\mathbb Z^{16}/M\mathbb Z^{16}$. C66 computes the ambient Smith invariants, while C67 computes coordinate-wise inverse denominators. C68 asks how the C65 saturation vectors sit inside $C$ and what the transpose-side annihilator looks like.

The scope firewall is $$\texttt{NO\_BAD\_EULER\_OR\_ROOT\_NUMBER}.$$ We do not claim a full table of marks, a full Burnside ring, arithmetic resolvents, local fields, Euler factors, root numbers, automorphy, or a Hilbert--Polya operator.

# Defect subgroup in the cokernel

Let $u_1,u_2,u_3$ be the C65 saturation vectors. Direct exact multiplication gives $$Mz_1=8u_1,\qquad Mz_2=2u_2,\qquad Mz_3=2u_3.$$ Thus the classes $[u_i]$ are torsion classes in $C$. The least multipliers are detected by the exact rational matrix $M^{-1}U$, where $U=[u_1\ u_2\ u_3]$.

Let $D=\langle [u_1],[u_2],[u_3]\rangle\subseteq C$. Then $$D\cong \mathbb Z/8\oplus\mathbb Z/2\oplus\mathbb Z/2,$$ and $$C/D\cong (\mathbb Z/2)^8\oplus(\mathbb Z/4)^2
 \oplus\mathbb Z/12\oplus\mathbb Z/144.$$ Equivalently, the Smith invariants of the augmented matrix $[M\mid U]$ are $$(1,1,1,1,2,2,2,2,2,2,2,2,4,4,12,144).$$

The three displayed relations show that the classes have orders dividing $8,2,2$. Exact rational inversion shows that the corresponding columns of $M^{-1}U$ have least denominators $8,2,2$, and enumeration of the $8\cdot2\cdot2$ coefficient classes shows that no nonzero combination is integral. Hence $|D|=32$ and its invariant factors are $(2,2,8)$. Independently, Euclidean Smith reduction of $[M\mid U]$ gives the displayed diagonal. Its product is $7077888=226492416/32$, as required for $C/D$.

# Transpose-side annihilator

Define the congruence lattice $$A=\{y\in\mathbb Z^{16}:z_1^Ty\equiv0\pmod 8,\ z_2^Ty\equiv0\pmod2,\ z_3^Ty\equiv0\pmod2\}.$$ The three functionals are well-defined on the transpose quotient because $z_i^TM^T=d_i u_i^T$ with $(d_1,d_2,d_3)=(8,2,2)$. In the named coordinate order, the residue rows $([z_1^Te_j]_8,[z_2^Te_j]_2,[z_3^Te_j]_2)$ are $$\begin{array}{c|cccccccccccccccc}
j&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15&16\\\hline
\text{residue}&000&010&010&000&010&010&000&000&700&100&010&010&010&010&001&001
\end{array}$$ so the coordinate types annihilated individually are $S_1,S_4,S_7,S_8$.

The lattice $A$ contains $M^T\mathbb Z^{16}$ with index $32$, and $$A/M^T\mathbb Z^{16}\cong (C/D)^\vee.$$ Its Smith invariants are $(1^4,2^8,4^2,12,144)$, identical to those of $C/D$.

An explicit integral basis $P$ for $A$ has determinant $32$. Multiplying $P^{-1}M^T$ gives an integer matrix with Smith diagonal $(1^4,2^8,4^2,12,144)$. The congruence equations define the annihilator of $D$ under the natural pairing between the column and transpose cokernels; therefore the row quotient is the Pontryagin dual of $C/D$.

# Reproducibility and limitations

The evidence binds C64, C65, C66, and C67 source bytes by SHA-256. The producer and checker use separate exact Smith reductions; a SymPy integer Smith calculation reproduces both quotient diagonals. Clean replay passes, and seventeen hostile semantic mutations are rejected. No Smith transformation basis is treated as canonical. The theorem remains a finite integral statement on the frozen 16-type support.

# Conclusion

C68 locates the C65 dyadic defect inside the C66 cokernel rather than merely reporting either group in isolation. The explicit row congruence lattice supplies the matching annihilator and makes the column/row duality checkable without additional representation-theoretic or arithmetic assumptions.
