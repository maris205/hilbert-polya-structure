---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-effective-orbit-repair-profile"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_repair_profile/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_repair_profile/paper/main.pdf"
source_sha256: "ab2295f4d3e13f3af1571c41b4709440a65d793c2d193edc014aeaa72b720365"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Effective-Group Orbits of Finite Repair Profiles in a Frozen Hénon Core

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_repair_profile>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_repair_profile/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_repair_profile/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_repair_profile/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The ambient symmetry lift of the frozen named core has order $11520$, but its label action has a six-element kernel. We use the faithful $1920$-element image to quotient all $65536$ deletion masks while retaining a finite repair profile: C79's distance and witness multiplicity, generated-subgroup order, and C80 threshold histograms grouped by target subgroup order. The quotient has exactly $3024$ orbits and fourteen profile classes. A weighted orbit polynomial recovers $(1+x)^{16}$, and a fixed-support identity independently recovers the orbit count. No complete Burnside ring, table of marks, arithmetic, or Hilbert--Polya claim is made.
author:
- Anonymous
title: 'Effective-Group Orbits of Finite Repair Profiles in a Frozen Hénon Core'
```

## Markdown 正文

# Two group orders

C75 records an ambient lift of order $11520$. Its action on the sixteen named labels has a kernel of order six, so the effective permutation group used here has order $$|E|=11520/6=1920.$$ This distinction is substantive: orbit sizes and stabilizers below are those of $E$, not of the nonfaithful lift.

# Invariant repair profile

For a retained mask $A$ and deletion set $D=L\setminus A$, let $$\Pi(D)=\bigl(\rho(D),W(D),|\Phi(A)|,H_D\bigr),$$ where $H_D$ lists, for each of the eight distinct subgroup orders, the counts of C80 thresholds $0,1,2,3$ among the target rows of that order. An effective label automorphism preserves $|\Phi(A)|$ and permutes targets within order classes, while C79's $(\rho,W)$ is preserved. Thus $\Pi$ is constant on $E$-orbits.

The effective action partitions the 65536 masks into 3024 orbits. Their size spectrum is $$\begin{array}{c|rrrrrrrrrrr}
\toprule
|O|&1&2&4&5&8&10&16&20&40&80&160\\
\midrule
\#O&128&256&416&128&192&384&16&672&608&208&16\\
\bottomrule
\end{array}$$

The weighted orbit inventory is exact: if $r(O)$ is a representative's cardinality, then $$\sum_O |O|x^{r(O)}=(1+x)^{16}.$$ The profile quotient contains fourteen distinct profile classes. In particular, the '(rho,W)' mask marginal remains $$(0,1):30400,\ (1,1):30400,\ (1,4):1984,\ (1,7):192,\ (1,8):128,$$ $$(2,4):1984,\ (2,7):192,\ (2,8):128,\ (2,25):64,\ (3,25):64.$$

# Orbit-count audit

For a permutation $g\in E$, the number of fixed label subsets is $2^{c(g)}$, where $c(g)$ is its cycle count on sixteen labels. The stored cycle-count spectrum therefore gives the elementary identity $$\frac1{1920}\sum_{g\in E}2^{c(g)}=3024.$$ This is an orbit partition check only; it is not a computation of a full Burnside ring or table of marks.

# Certification and scope

The producer and checker bind C76/C78/C79/C80 evidence and manifests by raw bytes, rebuild the five generators and closure, and compare every orbit representative, size, stabilizer, and profile. The canonical evidence hash is `c3cc35f45e1c8f7c9d4ecaecca820bf9dbc4db1c6a5769c20c75bad21f32fd9f`. A separate SymPy check verifies the weighted polynomial, class partition, and fixed-support identity; clean replay preserves the digest and all fourteen hostile mutations are rejected. The result is a finite named-coordinate quotient under the explicit scope firewall 'NO\_BAD\_EULER\_OR\_ROOT\_NUMBER'.
