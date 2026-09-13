---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-repair-distance-geometry"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry/paper/main.pdf"
source_sha256: "d6cffc50ed7d19aa2441963bbe19544d9c736ec94c0efa7e0c71e361430099c4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Repair-Distance Geometry of a Frozen Sixteen-Label Hénon Core

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give an exact finite repair atlas for the sixteen named coordinates in $Q=\mathbb Z/9\oplus\mathbb Z/3\oplus\mathbb Z/2$. For a deletion set $D$, the retained labels are $A=L\setminus D$, and $\rho(D)$ is the minimum number of deleted labels that must be restored before $A$ generates the full core. Exhaustive enumeration of all $2^{16}=65536$ deletion sets gives $\rho\in\{0,1,2,3\}$ with counts $30400,32704,2368,64$. We record the complete bivariate polynomial $P(x,y)=\sum_D x^{|D|}y^{\rho(D)}$, where $x$ marks deletions. Its marginals are $P(x,1)=(1+x)^{16}$ and $P(1,y)=30400+32704y+2368y^2+64y^3$. A structural derivation uses the pivot $S_9$, four projective direction blocks of sizes $1,1,2,5$, and six dummy labels. Independent exact reconstruction, symbolic cross-check, clean replay, and hostile semantic mutations certify the receipt. The result is a finite named-coordinate statement, with no arithmetic, local, Euler-factor, root-number, Burnside-ring, or Hilbert--Polya claim.
author:
- Anonymous
title: 'Exact Repair-Distance Geometry of a Frozen Sixteen-Label Hénon Core'
```

## Markdown 正文

# Finite object and question

Let $$Q=\mathbb Z/9\oplus\mathbb Z/3\oplus\mathbb Z/2,
 \qquad L=\{S_1,\ldots,S_{16}\}.$$ The coordinates and their closure convention are inherited byte-for-byte from the C75/C76 receipts. For a deletion set $D\subseteq L$, put $A=L\setminus D$ and define $$\Phi(A)=\langle x_i:S_i\in A\rangle\leq Q.$$ The repair distance is $$\rho(D)=\min\bigl\{|R|:R\subseteq D,\;
       \Phi((L\setminus D)\cup R)=Q\bigr\}.
 \label{eq:rho}$$ This measures restoration cost, not the deletion count $|D|$.

The exact observable is $$P(x,y)=\sum_{D\subseteq L}x^{|D|}y^{\rho(D)}.
 \label{eq:poly}$$ Here $x$ marks deleted labels and $y$ marks repaired labels.

# A structural distance formula

The preceding generation certificate identifies $S_9$ as a pivot and says that a retained support generates the full core precisely when it contains $S_9$ and meets at least two projective direction blocks. The blocks are $$B_1=\{S_1\},\quad B_2=\{S_{16}\},\quad
 B_3=\{S_7,S_{15}\},\quad
 B_4=\{S_3,S_4,S_8,S_{11},S_{12}\}.$$ The remaining six labels $\{S_2,S_5,S_6,S_{10},S_{13},S_{14}\}$ are dummy labels for this criterion. Let $$t(D)=\#\{j:(B_j\subseteq D)\}.$$

For every deletion set $D$, $$\rho(D)={\bf 1}_{\{S_9\in D\}}+\max\{0,t(D)-2\}.
 \label{eq:structural}$$ In particular, $\rho(D)\leq3$.

If the pivot is deleted, one restoration is necessary and sufficient for the cyclic factor. Among the four blocks, each fully deleted block contributes a missing direction. Restoring one label in each of the excess blocks beyond the two already hit is necessary and sufficient. The pivot is disjoint from the blocks, so the costs add. The independent checker also computes the minimum directly from the complete set of 25 full-core minimal supports and verifies [\[eq:structural\]](#eq:structural){reference-type="eqref" reference="eq:structural"} for every mask.

# Exact bivariate atlas

The complete coefficient table of [\[eq:poly\]](#eq:poly){reference-type="eqref" reference="eq:poly"} is shown below. The entries in row $k$ are coefficients of $x^ky^0,x^ky^1,x^ky^2,x^ky^3$.

    $k=|D|$   $y^0$   $y^1$   $y^2$   $y^3$   total
  --------- ------- ------- ------- ------- -------
          0       1       0       0       0       1
          1      15       1       0       0      16
          2     105      15       0       0     120
          3     455     105       0       0     560
          4    1364     456       0       0    1820
          5    2992    1375       1       0    4368
          6    4950    3047      11       0    8008
          7    6269    5116      55       0   11440
          8    6095    6609     166       0   12870
          9    4504    6595     341       0   11440
         10    2461    5040     506       1    8008
         11     940    2871     551       6    4368
         12     224    1151     430      15    1820
         13      25     289     226      20     560
         14       0      34      71      15     120
         15       0       0      10       6      16
         16       0       0       0       1       1

The row totals are $\binom{16}{k}$, giving $$P(x,1)=(1+x)^{16}.$$ The column totals give the repair distribution $$P(1,y)=30400+32704y+2368y^2+64y^3.$$

The table also has a compact derivation. Define $$H(x,z)=\prod_{s\in\{1,1,2,5\}}
 \left(\sum_{d=0}^{s-1}\binom{s}{d}x^d+zx^s\right).
\label{eq:H}$$ The variable $z$ records the number of fully deleted blocks. Replacing each $z^r$ by $y^{\max(0,r-2)}$, and then adding the dummy and pivot factors, gives $$P(x,y)=(1+x)^6(1+xy)\,\operatorname{Transform}_{z\to y}(H(x,z)).
 \label{eq:closed}$$ Expanding [\[eq:closed\]](#eq:closed){reference-type="eqref" reference="eq:closed"} agrees coefficient-by-coefficient with direct enumeration.

# Certification and scope

The producer binds the C73 generation criterion, C75 coordinate source, C76 closure atlas, and C77 subgroup receipt by SHA-256 before computing. An independent checker reconstructs the point-set closure transitions and the 25 full-core minimal supports, derives the four blocks from the coordinates, and checks all 65536 masks. A symbolic cross-check verifies [\[eq:closed\]](#eq:closed){reference-type="eqref" reference="eq:closed"}; a fresh-process replay preserves the canonical evidence bytes; and a hostile audit rejects 19 semantic mutations.

The canonical evidence hash is `728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae`. The effective C76 label action and the preceding lifted ambient action remain source-bound distinctions, but no group-orbit assertion is needed for [\[eq:poly\]](#eq:poly){reference-type="eqref" reference="eq:poly"}. Scope is explicitly limited to this finite named presentation: there is no arithmetic/local, Euler-factor, root-number, automorphy, full Burnside-ring/table-of-marks, or Hilbert--Polya claim.

# Conclusion

The repair geometry of the frozen support is shallow: every deletion pattern can be repaired with at most three restored labels, and the exact joint atlas is determined by one pivot and four direction blocks. The result supplies a reproducible finite certificate for subsequent combinatorial work while preserving the source and interpretation boundaries of the preceding papers.
