---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-coordinate-profile"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_coordinate_profile/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_coordinate_profile/paper/main.pdf"
source_sha256: "8f34b72dd32cd4c14617c9d7b583ff44a24731a298aa4df38e0b2851e9aee893"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Coordinate-Wise Integrality for a Restricted Table-of-Marks Map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_coordinate_profile>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_coordinate_profile/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_coordinate_profile/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_coordinate_profile/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The C66 Smith form gives the invariant factors of the frozen 16-type table-of-marks map, but it does not record how its finite cokernel sits in the named subgroup coordinates. We compute that embedding invariant directly. The least multipliers of the sixteen standard mark coordinates are $$(36,12,6,6,2,2,36,6,16,8,6,12,2,2,36,36),$$ while the transpose profile is $$(1,4,2,2,2,2,36,6,16,8,2,4,2,2,2,2).$$ Both least common multiples and the global denominator of the exact inverse are $144$, and the inverse has $43$ nonzero entries. This is a coordinate profile for the explicitly restricted 16-type map, not a canonical Smith basis or a full Burnside-ring statement.
author:
- Anonymous
title: 'Coordinate-Wise Integrality for a Restricted Table-of-Marks Map'
```

## Markdown 正文

# Set-up and scope

Let $G=W(E_6)$ be the order-$51840$ group in the preceding source package, and let $S_1,\ldots,S_{16}$ be its frozen subgroup representatives. C64 fixes the transitive sets $X_j=G/S_j$ and the integer self-mark matrix $$M_{ij}=\lvert (G/S_j)^{S_i}\rvert.$$ The matrix is nonsingular over $\mathbb Q$ and has determinant $226492416=2^{23}3^3$. C66 computes its full Smith form. C67 asks a different question: how hard is it to realize one named mark coordinate at a time by an integral virtual combination of the $X_j$?

For the standard basis vectors $e_j$ of $\mathbb Z^{16}$ define $$o_j=\min\{n>0:n e_j\in M\mathbb Z^{16}\}.$$ For the transpose map define $\widehat o_i$ in the same way with $M^T$. The scope firewall is $$\texttt{NO\_BAD\_EULER\_OR\_ROOT\_NUMBER}.$$ No claim is made about the full table of marks, the full Burnside ring, arithmetic resolvents, local fields, Euler factors, root numbers, automorphy, or a Hilbert--Polya operator.

# Exact rational method

Because $M$ is invertible over $\mathbb Q$, $$n e_j\in M\mathbb Z^{16}
 \quad\Longleftrightarrow\quad
 nM^{-1}e_j\in\mathbb Z^{16}.$$ If a rational vector $v$ has reduced coordinate denominators $d_1,\ldots,d_{16}$, the least positive $n$ for which $nv$ is integral is $\operatorname{lcm}(d_1,\ldots,d_{16})$. Thus $o_j$ is the least common multiple of the reduced denominators in column $j$ of $M^{-1}$. Similarly, $\widehat o_i$ is the least common multiple of the denominators in row $i$ of $M^{-1}$, since $(M^T)^{-1}=M^{-T}$.

The producer performs exact Gauss--Jordan elimination with rational integers. A separate checker uses a different pivot order and elimination loop, while an independent SymPy calculation checks both identity products and all denominator profiles. No floating point arithmetic is used.

In the fixed order $S_1,\ldots,S_{16}$, $$\begin{aligned}
(o_1,\ldots,o_{16})
  &=(36,12,6,6,2,2,36,6,16,8,6,12,2,2,36,36),\\
(\widehat o_1,\ldots,\widehat o_{16})
  &=(1,4,2,2,2,2,36,6,16,8,2,4,2,2,2,2).
\end{aligned}$$ Both profile least common multiples are $144$. The least common multiple of all denominators in $M^{-1}$ is $144$, and exactly $43$ entries of $M^{-1}$ are nonzero.

Exact inversion gives $M M^{-1}=M^{-1}M=I_{16}$. For each column $j$, reduce the sixteen rational entries to lowest terms and take their denominator least common multiple. In order, these values are $$(36,12,6,6,2,2,36,6,16,8,6,12,2,2,36,36).$$ Applying the same operation to each row gives $$(1,4,2,2,2,2,36,6,16,8,2,4,2,2,2,2).$$ The largest denominator lcm over all entries is $144$, and a direct support count gives $43$ nonzero entries. The denominator lemma in the preceding paragraph proves minimality of every listed multiplier.

The same frozen source bytes reproduce the C66 Smith invariants $$(1,2,2,2,2,2,2,2,2,2,2,4,4,4,24,144)$$ and determinant $226492416$. C65 compatibility remains $$\operatorname{SNF}(L_o)=(2,8),\qquad
\operatorname{SNF}(L_a)=(2,2,8),\qquad
U(L_a)/(L_a+U(L_o))\cong\mathbb Z/2.$$

These are checked as source-bound upstream certificates, independently of the rational inversion. The C67 result does not identify the C65 relative class with a direct summand of the C66 cokernel.

# Reproducibility and boundary

The evidence binds C64 mark bytes, the C64 manifest, and C66 evidence and manifest by SHA-256. The producer, structural checker, clean replay, independent rational-inverse check, and twelve hostile mutations all pass. The coordinate profile depends on the named $S_i$ ordering; it is therefore an embedding datum rather than an abstract-group invariant.

The theorem concerns only the frozen 16-type lattice map. In particular, it does not compute a full table of marks or assert any arithmetic or local-field interpretation.

# Conclusion

C66 supplies the abstract finite cokernel, while C67 supplies its coordinate-wise integrality profile. The two profiles and the global denominator $144$ are exact, replayable invariants of the named restricted mark map and provide the input for the next adaptive question.
