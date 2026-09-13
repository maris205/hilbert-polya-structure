---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-repair-witness-multiplicity"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_repair_witness_multiplicity/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_repair_witness_multiplicity/paper/main.pdf"
source_sha256: "1792176160a6ee5aecdc5b28cb2423bd7bf608d4eaf726bf18615d0de8786092"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Minimum-Repair Witness Multiplicity in a Frozen Sixteen-Label Hénon Core

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_repair_witness_multiplicity>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_repair_witness_multiplicity/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_repair_witness_multiplicity/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_repair_witness_multiplicity/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We refine the finite repair geometry of the sixteen named coordinates in $Q=\mathbb Z/9\oplus\mathbb Z/3\oplus\mathbb Z/2$. For a deletion set $D$, let $\rho(D)$ be the minimum number of deleted labels that must be restored to regenerate the full core, and let $W(D)$ count all minimum restoration sets. Exhaustive enumeration of all $65536$ deletion sets gives the exact joint inventory in $(\rho,W)$: the witness values are $1,4,7,8,25$, with global counts $30400,30400,1984,192,128,1984,192,128,64,64$ across the ten $(\rho,W)$ classes. The induced trivariate polynomial $G(x,u,v)=\sum_Dx^{|D|}u^{\rho(D)}v^{W(D)}$ has $94$ nonzero coefficients, $G(x,1,1)=(1+x)^{16}$, and recovers the C78 distance marginal at $v=1$. An independent point-set closure checker, symbolic block expansion, clean replay, and $22/22$ hostile mutations certify the receipt. No arithmetic, local, Euler-factor, root-number, Burnside-ring, or Hilbert--Polya claim is made.
author:
- Anonymous
title: |
  Minimum-Repair Witness Multiplicity in a Frozen\
  Sixteen-Label Hénon Core
```

## Markdown 正文

# Object and witness observable

Let $L=\{S_1,\ldots,S_{16}\}$ be the frozen named presentation in $Q=\mathbb Z/9\oplus\mathbb Z/3\oplus\mathbb Z/2$. For $D\subseteq L$, put $A=L\setminus D$ and define $$\rho(D)=\min\{|R|:R\subseteq D,\ \Phi(A\cup R)=Q\},
 \qquad
 W(D)=\#\{R\subseteq D:|R|=\rho(D),\ \Phi(A\cup R)=Q\}.$$ Thus $W$ measures degeneracy of the minimum repair, not the number of all repairs. We study $$G(x,u,v)=\sum_{D\subseteq L}x^{|D|}u^{\rho(D)}v^{W(D)},
 \label{eq:G}$$ where $x$ marks deletions, $u$ repair distance, and $v$ minimum-witness multiplicity.

# Block theorem

The source-bound generation criterion has pivot $S_9$ and direction blocks $$B_1=\{S_1\},\quad B_2=\{S_{16}\},\quad
 B_3=\{S_7,S_{15}\},\quad
 B_4=\{S_3,S_4,S_8,S_{11},S_{12}\}.$$ The other six labels are dummy for generation. Write $t(D)$ for the number of blocks fully contained in $D$, and let their sizes be $s=(1,1,2,5)$.

For every deletion set $D$, $$\rho(D)={\bf1}_{\{S_9\in D\}}+\max(0,t(D)-2).$$ Moreover, with $I$ the set of fully deleted blocks, $$W(D)=\begin{cases}
 1,&|I|\le 2,\\
 \displaystyle\sum_{i\in I}s_i,&|I|=3,\\
 \displaystyle\sum_{i<j\in I}s_is_j,&|I|=4.
 \end{cases}$$ Hence $\rho\le3$ and $W\in\{1,4,7,8,25\}$.

The pivot must be restored exactly when it is deleted. A retained support must hit two direction blocks, so each fully deleted block beyond the first two requires one restored label. If three blocks are fully deleted, any one label from one of those blocks repairs the direction condition; if all four are deleted, one label from each of two blocks is required. Counting these choices gives the displayed $W$ formula. The independent checker instead tests every restoration subset against the reconstructed finite group closure and obtains the same values for all $65536$ masks.

# Exact joint inventory

The global $(\rho,W)$ counts are $$\begin{array}{c|rrrrr}
\toprule
\rho\backslash W&1&4&7&8&25\\
\midrule
0&30400&0&0&0&0\\
1&30400&1984&192&128&0\\
2&0&1984&192&128&64\\
3&0&0&0&0&64\\
\bottomrule
\end{array}$$ The witness marginal is therefore $$\sum_D v^{W(D)}=60800v+3968v^4+384v^7+256v^8+128v^{25},$$ while setting $v=1$ recovers $$G(x,u,1)\big|_{x=1}=30400+32704u+2368u^2+64u^3.$$ At the other boundary, $G(x,1,1)=(1+x)^{16}$.

For a compact coefficient formula, sum over the four block states $I\subseteq\{1,2,3,4\}$. The block contribution is $$x^{\sum_{i\in I}s_i}\prod_{j\notin I}((1+x)^{s_j}-x^{s_j})
 u^{\max(0,|I|-2)}v^{w(I)},$$ where $w(I)$ is the displayed piecewise witness count. Multiplying the sum by $(1+x)^6(1+xu)$ gives $G$; its expansion has $94$ nonzero coefficients and agrees coefficient-by-coefficient with direct enumeration.

# Certification and scope

The producer binds the C73, C75, C76, C77, and C78 evidence/manifests by SHA-256. The independent checker reconstructs the actual point-set closure, finds all $25$ full-core minimal supports, enumerates every restoration subset in increasing size, and checks the full trivariate coefficient table. SymPy independently expands the block-state formula; a clean replay reruns the checker in a fresh process; and $22/22$ semantic mutations are rejected.

The canonical C79 evidence hash is `147a9b77e0ee7459040a7cc3c026bb21bce950a806e4fbc3ce0441dc9bb6c879`. This is a finite named-coordinate theorem only. It does not assert arithmetic/local data, Euler factors, root numbers, automorphy, a full Burnside ring or table of marks, or a Hilbert--Polya operator.

# Conclusion

C79 shows that the C78 repair distance has a small but nontrivial witness geometry: minimum repairs are unique in most masks, while the four fully deleted direction blocks create exactly $25$ choices. The trivariate receipt preserves this multiplicity information for subsequent finite-support experiments without changing the inherited source convention.
