---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-first-passage-hazard-residual"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_hazard_residual/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_hazard_residual/paper/main.pdf"
source_sha256: "b87d76f9ef3a4a40aea8d3b54a70a37c143ec6e6bda24c36a2d793238c4f6786"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Hazards and Residual Life for Twenty Frozen First-Passage Laws

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_hazard_residual>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_hazard_residual/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_hazard_residual/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_hazard_residual/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The frozen C88 receipt gives exact first-passage distributions for twenty subgroup targets under a uniform ordering of sixteen named labels. We derive the complete discrete hazard sequence for every target and, after every surviving prefix, the full conditional residual-life distribution, mean, and variance. All quantities are reduced rational numbers on a finite permutation space. A second implementation reconstructs the passage counts from the complete C88 hit bitsets before checking every hazard and residual cell. SymPy arithmetic, clean replay, and thirteen hostile mutations complete the audit. Empty conditioning events remain explicitly undefined. The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.
author:
- Anonymous
title: 'Exact Hazards and Residual Life for Twenty Frozen First-Passage Laws'
```

## Markdown 正文

# Frozen model and conventions

Let $L$ be the sixteen frozen labels, let $\pi$ be uniformly distributed on the $16!$ orderings of $L$, and let $A_k(\pi)$ be its first $k$ labels. For one of the twenty actual subgroup targets $H$, C88 defines $$T_H=\min\{k:H\leq\Phi(A_k)\},\qquad 0\leq T_H\leq16.$$ Write $$N_H(k)=\#\{\pi:T_H=k\},\qquad
 S_H(k)=\#\{\pi:T_H>k\}.$$ The at-risk population just before step $k$ is $$A_H(0)=16!,\qquad A_H(k)=S_H(k-1)\quad(1\leq k\leq16).$$ This distinction between $T_H\geq k$ and $T_H>k$ fixes the boundary convention. Whenever $A_H(k)>0$, the discrete hazard and transition survival are $$h_H(k)=\Pr(T_H=k\mid T_H\geq k)=\frac{N_H(k)}{A_H(k)},\qquad
 1-h_H(k)=\frac{S_H(k)}{A_H(k)}.$$ If the at-risk population is empty, neither conditional probability is defined and the receipt records `null`.

# Conditional residual-life theorem

After survival through step $k$, define $$R_{H,k}=T_H-k\ \big|\ T_H>k.$$ Thus $R_{H,k}\geq1$ whenever it is defined.

[\[thm:residual\]]{#thm:residual label="thm:residual"} For each of the twenty targets, each $0\leq k\leq16$ with $S_H(k)>0$, and $0\leq r\leq16-k$, the C94 receipt contains the exact identities $$\begin{aligned}
 \Pr(R_{H,k}>r)&=\frac{S_H(k+r)}{S_H(k)},\\
 \Pr(R_{H,k}=r)&=\frac{N_H(k+r)}{S_H(k)}\quad(1\leq r\leq16-k),\\
 m_H(k):=\mathbb E[R_{H,k}]&=\sum_{r=0}^{15-k}\frac{S_H(k+r)}{S_H(k)},\\
 q_H(k):=\mathbb E[R_{H,k}^2]&=
 \sum_{r=0}^{15-k}(2r+1)\frac{S_H(k+r)}{S_H(k)},\\
 v_H(k):=\operatorname{Var}(R_{H,k})&=q_H(k)-m_H(k)^2.\end{aligned}$$ If $S_H(k)=0$, no conditional law or moment is asserted.

On $\{T_H>k\}$, the event $R_{H,k}>r$ is exactly $T_H>k+r$, and $R_{H,k}=r$ is exactly $T_H=k+r$. Division by the nonzero conditioning count proves the first two formulas. For an integer-valued nonnegative variable $R$, the pointwise identities $$R=\sum_{r\geq0}\mathbf 1_{R>r},\qquad
 R^2=\sum_{r\geq0}(2r+1)\mathbf 1_{R>r}$$ give the two finite tail sums. The variance formula follows directly.

The hazards determine the survival law recursively: $$S_H(k)=16!\prod_{j=0}^{k}(1-h_H(j))$$ through every defined transition. Conversely, $N_H(k)=A_H(k)-S_H(k)$, so the C94 hazard atlas and the frozen C88 distribution contain equivalent finite information once the boundary convention is fixed.

The identity $S_H(k)=A_H(k)(1-h_H(k))$ starts with $A_H(0)=16!$ and uses $A_H(k)=S_H(k-1)$ thereafter. The converse is the same identity rearranged.

# Exact inventory

The receipt has $20\cdot17=340$ hazard steps and two complete $20\cdot17\cdot17=5780$ residual grids, one for survival and one for mass. There are 261 nonempty conditioning rows and 2709 defined cells in each residual grid. Structurally impossible cells $r>16-k$ and cells following an empty conditioning event are `null`, rather than assigned a numerical probability.

Representative exact values illustrate the range of laws:

    target   order       $m_H(0)$                 $v_H(0)$
  -------- ------- -------------- ------------------------
         1       2         $17/2$                   $85/4$
         2       3    $3961/1320$        $3586439/1742400$
        13       9         $34/9$             $21488/4455$
        19      54   $36499/3960$   $1652162153/109771200$

The trivial target 0 has $T_H=0$ identically, so $h_H(0)=1$ and the event $T_H>0$ is empty; accordingly its residual row at $k=0$ is undefined.

# Independent audit and scope

The producer reads only the canonical C88 evidence and manifest with SHA-256 digests $$\begin{aligned}
&\texttt{4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b},\\
&\texttt{aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5}.\end{aligned}$$ The independent checker starts from each C88 hit bitset, enumerates pivotal edges to reconstruct $N_H(k)$, and then rebuilds the entire expected receipt. SymPy verifies all 340 hazards, 5418 defined survival/mass cells, and 261 defined mean--variance rows. Clean replay preserves evidence digest $$\texttt{e185462629459a7d6602e3d1e3f49977a82d3fdee86007c3f906b224f028d1b3}.$$ All thirteen semantic mutations are rejected.

No arithmetic/local-data, Euler-factor, root-number, automorphy, full Burnside-ring/table-of-marks, or Hilbert--Polya operator claim is made.
