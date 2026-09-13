---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-144-backward-block-controlled-viability"
canonical_tex: "zeta_mvp0/papers/RH-144-backward-block-controlled-viability/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-144-backward-block-controlled-viability/main.pdf"
source_sha256: "73c766c938eac12cfa5b00aea419f76a93a028745d7f17ee98b14206f5d5e5bb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Backward Kernels for Block-Controlled Tail Viability Exact Young-Envelope Preimages, Reset Criteria, and Two Unavoidable Birth Walls

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-144-backward-block-controlled-viability>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-144-backward-block-controlled-viability/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-144-backward-block-controlled-viability/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-144-backward-block-controlled-viability/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-144-backward-block-controlled-viability/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-139 reduced eventual directional support to a controlled tail tube $\limsup y_n<1$ and a positive normalized-base liminf. RH-137 propagated a greedy finite trajectory forward. We develop the dual backward theory. For $$F_{A,B,q}(y)=q+(\sqrt{Ay}+\sqrt B)^2$$ and target radius $r$, the largest input radius mapped strictly below $r$ is $$\Phi_{A,B,q}(r)=
   \begin{cases}
   0,&r\leq q+B,\\
   1,&A=0\text{ and }r>q+B,\\
   \min\!\left\{1,
   \dfrac{(\sqrt{r-q}-\sqrt B)^2}{A}\right\},&A>0, r>q+B.
   \end{cases}$$ For a finite control family, the predecessor radius is the maximum of these quantities. Backward composition gives the exact scalar viability kernel and a constructive policy. At block boundaries, if the backward kernel of every block contains a common interval $[0,r)$, then that interval is controlled invariant across arbitrarily many blocks; all intermediate safety constraints are already included.

  Recomputing the full RH-137 candidate families gives 28 of 30 chains with initial kernel $[0,1)$ and safe policies even from $0.99$. The two coarse left failures have empty initial kernels. At their decisive step, every candidate has $F(0)>9.4>1$, so no gauge choice or incoming state can cross the wall. This strengthens the prior classification: those events are candidate-family obstructions, not greedy artifacts. It also isolates them as finite-prefix births; no repeating all-level block condition is proved.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Backward Kernels for Block-Controlled Tail Viability\
  Exact Young-Envelope Preimages, Reset Criteria, and Two Unavoidable Birth Walls
```

## Markdown 正文

# Forward envelopes and backward questions

At time $n$, RH-137 provides a finite family of monotone Young envelopes $$F_{n,c}(y)=q_{n,c}+
 (\sqrt{A_{n,c}y}+\sqrt{B_{n,c}})^2,
 \qquad c\in\mathcal C_n.$$ A forward policy chooses $c_n$ and propagates an upper state. This answers whether one chosen trajectory is safe, but it does not directly answer two structural questions: what is the full set of states from which some future policy remains safe, and is a failed greedy step unavoidable for the entire control family?

Because every envelope is scalar and increasing, both questions have exact answers by backward dynamic programming [@Aubin1991; @Bertsekas2017]. Unlike a per-step contraction test, the backward kernel automatically allows an expanding step when later constraints still leave enough room.

# Exact one-step preimages

Fix the safety domain $0\leq y<1$, although the formulas hold for any target radius.

[\[thm:preimage\]]{#thm:preimage label="thm:preimage"} For $A,B,q\geq0$ and target $r\geq0$, the supremum of $$\{y\in[0,1]:F_{A,B,q}(y)<r\}$$ is $\Phi_{A,B,q}(r)$ displayed in the abstract. In particular the preimage is empty exactly when the zero-state floor $q+B$ is at least $r$.

The map is increasing. If $r\leq q+B=F(0)$, no input works. If $A=0$, the map is constant and every input works once its floor is below $r$. Otherwise the inequality is equivalent to $$\sqrt{Ay}<\sqrt{r-q}-\sqrt B.$$ The right side is positive precisely in the remaining case. Squaring and capping at one gives the formula.

For a control family define the predecessor operator $$\mathcal V_n(r)=\max_{c\in\mathcal C_n}\Phi_{A_{n,c},B_{n,c},q_{n,c}}(r).$$ The maximizing control is a constructive witness.

[\[thm:kernel\]]{#thm:kernel label="thm:kernel"} For a horizon $N$ with safety wall one, set $r_N=1$ and $$r_n=\mathcal V_n(r_{n+1}),\qquad n=N-1,\ldots,0.$$ Then $[0,r_n)$ is exactly the set of scalar upper states at time $n$ from which some policy keeps every later state below one through time $N$.

At the last step the claim is Theorem [\[thm:preimage\]](#thm:preimage){reference-type="ref" reference="thm:preimage"}, after maximizing over controls. Inductively, a state is viable at time $n$ exactly when one control maps it into the already characterized interval $[0,r_{n+1})$. Monotonicity makes the union of all controlled preimages the interval ending at their largest radius. Backward induction proves exactness.

# Blocks, resets, and delayed starts

Partition an infinite recurrence into blocks $[n_j,n_{j+1})$. Let $\mathcal V^{(j)}$ denote the backward operator for the whole block, including every intermediate safety wall.

[\[thm:block\]]{#thm:block label="thm:block"} Suppose there is $r>0$ such that, for every $j$ beyond some index, $$\mathcal V^{(j)}(r)\geq r.$$ Then every boundary state in $[0,r)$ admits a control policy that remains below one throughout each block and returns to $[0,r)$ at the next boundary. Consequently the controlled trajectory has $\limsup y_n<1$ if all partial block images of $[0,r)$ are uniformly bounded by some $\bar y<1$.

The inclusion $[0,r)\subseteq[0,\mathcal V^{(j)}(r))$ says exactly that every boundary state has a within-block policy ending below $r$ while satisfying all intermediate walls. Concatenate these policies. The uniform partial guard gives the stated limsup.

A reset that places the state below $r$ may start this induction after an arbitrary finite prefix. Conversely, an endpoint condition alone is not enough: a two-step block can jump above one and later return to zero. The backward block operator avoids this error because every intermediate target is imposed during composition.

# Finite candidate-family audit

The audit reconstructs every RH-137 temporal record and every polar/blended gauge candidate at 80 decimal digits. It then applies the exact scalar preimage formula backward, stores the maximizing controls, and verifies the result by starting at $0.99r_0$ and propagating the selected policy forward.

::: {#tab:audit}
  classification    count                  strongest finite statement
  ---------------- ------- ----------------------------------------------------------
  viable            $28$    full initial interval $[0,1)$; near-boundary policy safe
  obstructed         $2$        empty kernel; every control floor exceeds target
  all chains        $30$           backward and forward classifications agree

  : Exact scalar backward-kernel classification of the RH-137 families.
:::

Among the viable chains, the narrowest positive interior reset radius is $1.724\times10^{-3}$. Thus a chain can accept the whole initial interval because early zero-tail steps act as resets, yet still pass through a much narrower later gate. This distinction is precisely what block analysis is meant to record.

The two empty kernels are the left channel at $\sigma=0.08$ for thresholds $10^{-8}$ and $10^{-6}$. At the decisive final transition the birth term alone exceeds $9.4$. Since $$\min_{c\in\mathcal C_n}F_{n,c}(0)>9.4>1,$$ the predecessor of the unit safety interval is empty. No incoming tail, orthogonal gauge, Young parameter, or non-greedy future choice can repair that step within this candidate architecture.

![Backward kernels, finite classification, interior reset radii, and the two unavoidable zero-state floors.](<../../../../../zeta_mvp0/papers/RH-144-backward-block-controlled-viability/figures/backward_block_viability.pdf>){#fig:audit width="\\textwidth"}

# Consequence and claim boundary

RH-144 gives an exact method for proving the RH-139 tail packet $P_V$ from repeating controlled blocks. It also shows that the two finite failures are localized more strongly than before: they are control-family walls, not poor greedy choices. Since they occur at one coarse anchor, they do not by themselves preclude a delayed-start asymptotic theorem.

We have not proved that all finer or all future model blocks share a common positive backward radius, established a uniform partial-block gap below one, or justified a delayed start for every all-level source realization. We have not proved the normalized-base liminf, Stage A, a Hilbert--Polya operator, a zeta-zero identification, or the Riemann Hypothesis.
