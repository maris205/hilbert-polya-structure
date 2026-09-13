---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-minimum-repair-matroid"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_minimum_repair_matroid/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_minimum_repair_matroid/paper/main.pdf"
source_sha256: "c1e231bf1bc9acb20bf481115604a7bc632560873048a89baf4aa8403cde91b3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Minimum-Repair Matroids and a Basis-Exchange Atlas for a Frozen Hénon Core

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_minimum_repair_matroid>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_minimum_repair_matroid/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_minimum_repair_matroid/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_minimum_repair_matroid/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For each deletion set in a frozen sixteen-label finite model, we classify the entire family of minimum restorations that recover the full core. Every such family is the set of bases of an explicit direct sum: irrelevant deleted labels are loops, the deleted pivot is a coloop, and the remaining component is a rank-truncated partition matroid on the fully deleted direction blocks. Exhaustive point-set closure enumeration verifies this identification and basis exchange for all $65536$ deletion sets. The ten repair/multiplicity templates yield exactly five unlabeled exchange graphs, $K_1,K_4,K_7,K_8$, and $L(K_{1,1,2,5})$. In the all-deleted case the 25 bases equal the 25 minimal triples of the predecessor closure atlas. This is a finite combinatorial theorem under the firewall `NO_BAD_EULER_OR_ROOT_NUMBER`.
author:
- Anonymous
title: |
  Minimum-Repair Matroids and a Basis-Exchange Atlas\
  for a Frozen Hénon Core
```

## Markdown 正文

# Frozen repair problem

Let $L=\{S_1,\ldots,S_{16}\}$ and let $D\subseteq L$ be deleted, with $A=L\setminus D$ retained. The pivot is $p=S_9$, and the four direction blocks are $$B_1=\{S_1\},\quad B_2=\{S_{16}\},\quad
B_3=\{S_7,S_{15}\},\quad
B_4=\{S_3,S_4,S_8,S_{11},S_{12}\}.$$ The other six labels are dummy for full-core generation. Write $$I(D)=\{i:B_i\subseteq D\},\qquad t(D)=|I(D)|,
 \qquad r(D)=\max\{0,t(D)-2\}.$$ A restoration witness is $R\subseteq D$ for which $A\cup R$ generates the full finite core, and it is minimum when $|R|$ is least possible.

# Matroid theorem

Let $$E_D=D\setminus\left((\{p\}\cap D)\cup
       \bigcup_{i\in I(D)}B_i\right)$$ and let $P_D=\bigoplus_{i\in I(D)}U_{1,B_i}$ be the partition matroid with capacity one in each fully deleted block. Define $$M_D=U_{0,E_D}\oplus
 U_{1,\{p\}\cap D}\oplus \operatorname{Tr}_{r(D)}(P_D),$$ where the middle summand is absent when $p\notin D$.

For every $D\subseteq L$, the minimum restoration witnesses are exactly the bases of $M_D$. In particular, they satisfy basis exchange.

The pivot must be restored precisely when $p\in D$, so it is present in every minimum witness in that case. The retained support meets $4-t(D)$ direction blocks. Reaching two directions therefore requires one restored label from each of exactly $r(D)$ distinct fully deleted blocks. Choosing two labels from the same block creates no additional met direction and cannot occur in a minimum witness. Conversely, the pivot choice together with any $r(D)$ such distinct-block choices is a full repair. These choices are precisely the bases of the displayed direct sum.

The independent checker does not infer this result from the formula. It reconstructs the C75 point-set closure table, tests restoration subsets in increasing cardinality for every $D$, compares the resulting family with $\mathcal B(M_D)$, and checks all $198912$ ordered exchange obligations.

# Ten templates and five exchange graphs

Join two bases when their symmetric difference has size two. The exact template atlas is $$\begin{array}{@{}rrrl@{}}
\toprule
\rho&W&\#D&\text{exchange graph}\\\midrule
0&1&30400&K_1\\
1&1&30400&K_1\\
1&4&1984&K_4\\
1&7&192&K_7\\
1&8&128&K_8\\
2&4&1984&K_4\\
2&7&192&K_7\\
2&8&128&K_8\\
2&25&64&L(K_{1,1,2,5})\\
3&25&64&L(K_{1,1,2,5})\\
\bottomrule
\end{array}$$ For $t\leq2$ the direction rank is zero, giving $K_1$. For $t=3$ the direction rank is one, so all $W$ singleton choices exchange with one another, giving $K_W$ for $W=4,7,8$. For $t=4$, the rank-two bases are the edges of the complete multipartite graph $K_{1,1,2,5}$, and exchange adjacency is edge incidence; hence the basis graph is its line graph.

Aggregating the two pivot states gives the finite graph atlas $$\begin{array}{@{}lrrrrl@{}}
\toprule
\text{type}&\#D&|V|&|E|&\operatorname{diam}&\text{degree multiplicities}\\\midrule
K_1&60800&1&0&0&0^1\\
K_4&3968&4&6&1&3^4\\
K_7&384&7&21&1&6^7\\
K_8&256&8&28&1&7^8\\
L(K_{1,1,2,5})&128&25&128&2&9^{10},10^{10},13^4,14^1\\
\bottomrule
\end{array}$$

# The all-deleted atlas

When $D=L$, every basis is $$\{S_9,x,y\},\qquad x\in B_i,\quad y\in B_j,\quad i\ne j.$$ There are $$1\cdot1+1\cdot2+1\cdot5+1\cdot2+1\cdot5+2\cdot5=25$$ such bases. Expanding the seven C76 full-core-minimal representatives under the effective label generators gives the same 25 masks, not merely the same cardinality. The relevant action has order $1920$; it is distinct from the order-$11520$ ambient lift bound in C75.

For an edge joining parts of sizes $a$ and $b$ in $K_{1,1,2,5}$, the corresponding line-graph degree is $16-a-b$. This gives the exact spectrum $$\{9^{10},10^{10},13^4,14^1\}.$$ The graph has 128 edges, radius and diameter two, and 172 unordered vertex pairs at distance two (the other 128 pairs are adjacent).

# Audit boundary

The producer byte-binds C75, C76, and C79 evidence and manifests. A separate SymPy block polynomial recovers all ten support counts, while an exact $25\times25$ adjacency-matrix calculation recovers the line-graph invariants. Clean replay is byte-stable and all 18 hostile semantic mutations are rejected. The canonical evidence SHA-256 is

9c3b20c703b680a391ad1834c0f55cabaf27bfed14cee2099b0c3afa1eb259ca

No arithmetic/local data, Euler factor, root number, automorphy statement, full Burnside ring or table of marks, or Hilbert--Pólya operator is claimed.
