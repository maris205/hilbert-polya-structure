---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-coordinate-core-atlas"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_coordinate_core_atlas/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_coordinate_core_atlas/paper/main.pdf"
source_sha256: "f48d0ab935d49cce360c650941a9432aab27eea97e7c323e641bb92c41feffc8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exhaustive Named-Coordinate Atlas for a Universal Complement Core

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_coordinate_core_atlas>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_coordinate_core_atlas/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_coordinate_core_atlas/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_coordinate_core_atlas/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The common intersection of all complements to a fixed direct factor in an exact restricted mark cokernel was previously identified as $8C\cong\mathbb Z/3\oplus\mathbb Z/18$. We resolve the full incidence of the sixteen named presentation classes inside this core. An explicit $\mathbb Z/9\oplus\mathbb Z/3\oplus\mathbb Z/2$ coordinate model classifies all $2^{16}=65536$ named supports. They reach exactly twenty distinct subgroups, and these are every subgroup of the core. We give the complete ten-type distribution by support size and the generating-support polynomial. There are exactly twenty-five inclusion-minimal generating supports, all triples containing the ninth named class. This is a presentation-dependent atlas, not a canonical coordinate system.
author:
- Anonymous
title: 'An Exhaustive Named-Coordinate Atlas for a Universal Complement Core'
```

## Markdown 正文

# Core, scope, and coordinate model

Let $M$ be the frozen $16\times16$ restricted mark matrix and write $[e_j]$ for its named coordinate classes. The predecessor theorem identifies the universal complement core as $$Q=8C\cong\mathbb Z/3\oplus\mathbb Z/18,
 \qquad |Q|=54.$$ We study the labelled family $q_j=8[e_j]$ for $1\leq j\leq16$.

The scope firewall is $$\texttt{NO\_BAD\_EULER\_OR\_ROOT\_NUMBER}.$$ No canonical Smith coordinates, full table of marks or Burnside ring, arithmetic or local data, Euler factor, root number, automorphy, or Hilbert--Polya operator is claimed.

Exact rational residues modulo $M\mathbb Z^{16}$ show that $(q_1,q_3,q_9)$ gives coordinates on $$Q=\mathbb Z/9\oplus\mathbb Z/3\oplus\mathbb Z/2.$$ In this basis the sixteen rows are $$\label{eq:coordinates}
\begin{split}
&(1,0,0),(6,0,0),(0,1,0),(3,1,0),(0,0,0),(0,0,0),\\
&(4,2,0),(3,2,0),(0,0,1),(0,0,0),(0,1,0),(3,1,0),\\
&(0,0,0),(0,0,0),(2,1,0),(8,2,0).
\end{split}$$ For each row, the checker lifts the asserted relation back to an integral column of $M$. Thus Equation [\[eq:coordinates\]](#eq:coordinates){reference-type="eqref" reference="eq:coordinates"} is tied to the original presentation, not inferred only from element orders.

# The complete subgroup atlas

For $A\subseteq\{1,\ldots,16\}$ put $$Q_A=\langle q_j:j\in A\rangle.$$ The producer closes all $65536$ supports in the coordinate model. A separate queue enumeration starts from zero, adjoins every element of the 54-element group, and returns its complete subgroup lattice.

The family $\{Q_A:A\subseteq\{1,\ldots,16\}\}$ consists of twenty distinct subgroups and equals the complete subgroup lattice of $Q$. The type inventory is $$\begin{array}{c|cccccccccc}
\text{type}&1&C_2&C_3&C_6&C_3^2&C_9&C_{18}&C_3{+}C_6&C_3{+}C_9&C_3{+}C_{18}\\
\hline
\#&1&1&4&4&1&3&3&1&1&1.
\end{array}$$

Cached subgroup closure applied to Equation [\[eq:coordinates\]](#eq:coordinates){reference-type="eqref" reference="eq:coordinates"} produces twenty actual subsets of $Q$. The independent all-element enumeration also produces twenty subsets, and exact set comparison gives equality. GAP independently enumerates the same ten isomorphism types with the displayed multiplicities.

Table [1](#tab:supports){reference-type="ref" reference="tab:supports"} refines the result by support size. Its columns use the type order in the theorem. Thus it records every one of the $65536$ supports, while keeping supports that generate the same subgroup distinct.

::: {#tab:supports}
    $|A|$   $1$   $C_2$   $C_3$   $C_6$   $C_3^2$   $C_9$   $C_{18}$   $C_3{+}C_6$   $C_3{+}C_9$    $Q$   total
  ------- ----- ------- ------- ------- --------- ------- ---------- ------------- ------------- ------ -------
        0     1       0       0       0         0       0          0             0             0      0       1
        1     5       1       6       0         0       4          0             0             0      0      16
        2    10       5      32       6        13      25          4             0            25      0     120
        3    10      10      70      32        85      66         25            13           224     25     560
        4     5      10      80      70       245      95         66            85           940    224    1820
        5     1       5      50      80       411      80         95           245          2461    940    4368
        6     0       1      16      50       446      39         80           411          4504   2461    8008
        7     0       0       2      16       328      10         39           446          6095   4504   11440
        8     0       0       0       2       165       1         10           328          6269   6095   12870
        9     0       0       0       0        55       0          1           165          4950   6269   11440
       10     0       0       0       0        11       0          0            55          2992   4950    8008
       11     0       0       0       0         1       0          0            11          1364   2992    4368
       12     0       0       0       0         0       0          0             1           455   1364    1820
       13     0       0       0       0         0       0          0             0           105    455     560
       14     0       0       0       0         0       0          0             0            15    105     120
       15     0       0       0       0         0       0          0             0             1     15      16
       16     0       0       0       0         0       0          0             0             0      1       1

  : Complete named-support distribution. Each row sums to $\binom{16}{|A|}$. The penultimate type is $C_3\oplus C_9$ and the last type column $Q$ is $C_3\oplus C_{18}$.
:::

# The generating-support complex

Reading the $Q$ column of Table [1](#tab:supports){reference-type="ref" reference="tab:supports"} gives the polynomial $$\label{eq:poly}
\begin{split}
P_Q(t)={}&25t^3+224t^4+940t^5+2461t^6+4504t^7+6095t^8\\
&+6269t^9+4950t^{10}+2992t^{11}+1364t^{12}\\
&+455t^{13}+105t^{14}+15t^{15}+t^{16}.
\end{split}$$

Exactly twenty-five named supports are inclusion-minimal among those that generate $Q$. Every one has size three and contains $S_9$.

The $\mathbb Z/2$ coordinate in Equation [\[eq:coordinates\]](#eq:coordinates){reference-type="eqref" reference="eq:coordinates"} is nonzero only in row nine, so every generating support contains $S_9$. After choosing it, generation is equivalent to spanning the Frattini quotient of $\mathbb Z/9\oplus\mathbb Z/3$ over $\mathbb F_3$. Exactly twenty-five unordered pairs of the remaining named rows have nonzero determinant. Removing any member then loses either the dyadic coordinate or the required rank, proving inclusion-minimality. Exhaustive deletion independently returns the same twenty-five triples.

The number three is a property of the named list: no one or two of the $q_j$ generate $Q$. It is not the abstract generator rank. Indeed $Q\cong\mathbb Z/3\oplus\mathbb Z/18$ is abstractly two-generated. Likewise, the coordinate basis is a verified choice, not a canonical Smith basis.

# Reproducibility and conclusion

The canonical evidence binds the exact C64 matrix and C71 evidence and manifest. Producer and checker independently classify all supports and all abstract subgroups; the checker also verifies every coordinate relation in the original integer presentation. GAP reproduces the complete subgroup type inventory. Clean replay passes and twenty-eight hostile semantic mutations are rejected. C72 thus upgrades the predecessor's list of twenty-five triples to a complete labelled incidence atlas: every named support is classified, and every subgroup of the universal core is reached.
