---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-threshold-repair-atlas"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_threshold_repair_atlas/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_threshold_repair_atlas/paper/main.pdf"
source_sha256: "10e26d63bcec5235c1fdd1412494d59d4fcc61cd5210ea6e2774b9c4d48a8605"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An All-Subgroup Containment-Threshold Atlas for a Frozen Hénon Core

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_threshold_repair_atlas>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_threshold_repair_atlas/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_threshold_repair_atlas/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_threshold_repair_atlas/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We replace exact full-core repair by a target-containment observable on the twenty actual subgroup rows of $Q=\mathbb Z/9\oplus\mathbb Z/3\oplus\mathbb Z/2$. For a deletion set $D$ and retained labels $A=L\setminus D$, define $\tau_H(D)=\min\{|R|:R\subseteq D,,H\subseteq\Phi(A\cup R)\}$. An exhaustive receipt stores all $20\times65536$ integer values, their deleted-cardinality tables, and target distributions. The full target row is exactly the C78 repair distance, with distribution $30400,32704,2368,64$. An independent target-antichain reconstruction, symbolic marginal checks, clean replay, and thirteen hostile mutations pass. The result is a finite named-support atlas and makes no arithmetic, local, Burnside-ring, table-of-marks, or Hilbert--Polya claim.
author:
- Anonymous
title: 'An All-Subgroup Containment-Threshold Atlas for a Frozen Hénon Core'
```

## Markdown 正文

# Targeted repair

Let $L=\{S_1,\ldots,S_{16}\}$ be the frozen named presentation. For every subgroup row $H\leq Q$ and deletion set $D\subseteq L$, put $$\tau_H(D)=\min\{|R|:R\subseteq D,\ H\subseteq
 \Phi((L\setminus D)\cup R)\}.$$ This is deliberately a containment threshold. It does not require the generated subgroup to equal $H$; in particular, different rows of the same order remain separate named targets.

# Finite antichain identity

For a fixed target $H$, let $\mathcal M_H$ be the inclusion-minimal named supports $M$ satisfying $H\subseteq\Phi(M)$. Then $$\tau_H(D)=\min_{M\in\mathcal M_H}|M\setminus(L\setminus D)|.$$

Any feasible restoration contains a target-containing support. Removing labels one at a time while containment persists reaches a member of $\mathcal M_H$, and removing labels from the retained part is impossible by the definition of the set difference. Conversely, restoring $M\setminus A$ is feasible for every $M\in\mathcal M_H$.

The C80 checker reconstructs the point-set addition table from C75, derives each $\mathcal M_H$, and evaluates this formula for every one of the 65536 retained masks. The twenty target orders in row order are $$1,2,3,3,3,3,6,6,6,6,9,9,9,9,18,18,18,18,27,54.$$

# The exact-core boundary

The last row is $H=Q$. Its threshold values are $$\#\{D:\tau_Q(D)=0,1,2,3\}
  =(30400,32704,2368,64).$$ The source-bound pivot/block decomposition gives, independently, $$\tau_Q(D)=\mathbf1_{S_9\in D}+
 \max\bigl(0,t(D)-2\bigr),$$ where $t(D)$ counts fully deleted blocks of sizes $1,1,2,5$. Thus the C80 row is exactly C78's $\rho$ row, while the other nineteen rows describe proper-subgroup containment and can have smaller thresholds.

Every deleted-cardinality table has row sum $\binom{16}{k}$, hence each target's cardinality marginal is $(1+x)^{16}$. If $H_1\subseteq H_2$, then $$\tau_{H_1}(D)\leq\tau_{H_2}(D)\quad\text{for every }D,$$ which the receipt checks on all profiles using the actual subgroup bitsets.

# Certification and scope

The producer binds the C75, C76, and C78 evidence/manifests by raw-byte SHA-256. The canonical C80 evidence hash is `8d27428b14dbd7354e9c8308ad76b1108e3f551702165833301509cd52de7df5`. The independent checker uses target antichains rather than the producer's descending recurrence; a SymPy script verifies all twenty cardinality marginals and the exact C78 polynomial; clean replay preserves the digest; and $13/13$ hostile mutations are rejected.

This receipt concerns only the named sixteen-label finite model. It does not claim a full Burnside ring or table of marks, arithmetic/local data, Euler factors, root numbers, automorphy, or a Hilbert--Polya operator.
