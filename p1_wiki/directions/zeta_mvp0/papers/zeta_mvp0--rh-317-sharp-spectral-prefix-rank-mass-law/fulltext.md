---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-317-sharp-spectral-prefix-rank-mass-law"
canonical_tex: "zeta_mvp0/papers/RH-317-sharp-spectral-prefix-rank-mass-law/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-317-sharp-spectral-prefix-rank-mass-law/main.pdf"
source_sha256: "ab91a8de5912491f1e268bb692f7e8298e354db81fabfa573f62889f0bf6ba68"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Sharp Rank and Squared-Mass Cost of Spectral Prefix Realization

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-317-sharp-spectral-prefix-rank-mass-law>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-317-sharp-spectral-prefix-rank-mass-law/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-317-sharp-spectral-prefix-rank-mass-law/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-317-sharp-spectral-prefix-rank-mass-law/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-317-sharp-spectral-prefix-rank-mass-law/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Exact finite-prefix realizations exist by RH-316. We determine their optimal complexity scale. If $s=q_*/q$, then both the least rank and the least squared spectral mass needed to match through order $N$ are $\Theta(s^N)$. The lower bound is a one-moment consequence of the modulus cap; the recursive packet construction gives the matching upper bound. The result concerns synthetic spectra and does not identify an actual noisy rank.
author:
- Bin Wang
date: July 2026
title: 'The Sharp Rank and Squared-Mass Cost of Spectral Prefix Realization'
```

## Markdown 正文

# Universal lower bounds

Let $\mathcal S$ be a finite multiset in $|\mu|\le q$, with rank $r$ and squared mass $M_2=\sum|\mu|^2$. If its $N$th moment equals $a_N$, then $$|a_N|\le rq^N,
 \qquad
 |a_N|\le M_2q^{N-2}.$$ Since RH-268 proves $a_N/q_*^N\to1$, both $r$ and $M_2$ are bounded below by positive constant multiples of $s^N$, where $s=q_*/q>1$.

# Recursive upper bound

For the deterministic anchor prefix through order $N$, the RH-316 recursion can be chosen so that $$r_N\le C_1s^N,
 \qquad M_{2,N}\le C_2s^N.$$ Consequently the minimal rank and minimal squared mass are both $\Theta(s^N)$.

Let $\mathcal P_e$ be the packet inserted at order $e$, and write $b_e$ and $r_e$ for its squared mass and rank, taking both to be zero if no packet is needed. The all-order envelope gives $|a_d|\le A q_*^d$ for a fixed $A$.

The decisive point is the divisor sparsity of RH-315: an $e$-packet contributes to the $d$th moment only when $e\mid d$. Hence, for $d\ge2$, the residual before the $d$th correction obeys $$|w_d|\le A q_*^d+q^{d-2}
 \sum_{\substack{e\mid d\\e<d}}b_e.$$ Indeed each contributing packet satisfies $|p_d(\mathcal P_e)|\le q^{d-2}b_e$. With $L_d=\lceil |w_d|/(dq^d)\rceil$ when $w_d\ne0$, one has $$r_d=dL_d\le A s^d+q^{-2}
 \sum_{\substack{e\mid d\\e<d}}b_e+d,$$ and, because the new packet lies in $|\mu|\le q$, $$b_d\le q^2r_d
 \le Aq^2s^d+
 \sum_{\substack{e\mid d\\e<d}}b_e+q^2d.$$

Every proper divisor of $d$ is at most $d/2$. Thus, if $b_e\le Cs^e$ for $e<d$, the divisor sum is at most $Cd s^{d/2}$. Since $d s^{-d/2}\to0$, enlarging $C$ to cover finitely many initial orders closes the induction and gives $b_d=O(s^d)$. The rank display then also gives $r_d=O(s^d)$. Finally $$M_{2,N}=\sum_{d\le N}b_d=O(s^N),\qquad
 r_N=\sum_{d\le N}r_d=O(s^N).$$ The preceding one-moment inequalities give the matching lower bounds.

Numerically, $$s=1.4017504517095518\ldots,
 \qquad \log s=0.3377217782684642\ldots.$$

The theorem is an extremal law inside the finite normal spectral class. It does not assert that the actual noisy complement has minimal rank, obeys this mass asymptotic, or matches the deterministic prefix. Gates A--E remain false/open.
