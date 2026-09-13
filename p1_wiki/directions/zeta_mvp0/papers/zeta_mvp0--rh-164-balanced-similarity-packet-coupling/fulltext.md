---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-164-balanced-similarity-packet-coupling"
canonical_tex: "zeta_mvp0/papers/RH-164-balanced-similarity-packet-coupling/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-164-balanced-similarity-packet-coupling/main.pdf"
source_sha256: "e252ca172dba70e0cd877211ea624d918780fe143125e0f271bae7bdb2affe05"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Balanced Similarities for Directed Packet Couplings Rank Rescue and the Original-Norm Conditioning Price

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-164-balanced-similarity-packet-coupling>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-164-balanced-similarity-packet-coupling/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-164-balanced-similarity-packet-coupling/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-164-balanced-similarity-packet-coupling/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-164-balanced-similarity-packet-coupling/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The two-sided Schur product of RH-163 is the sharp feedback quantity, but the single-norm RH-161 theorem remains useful when an actual block norm can be optimized. For $A=\bigl(\begin{smallmatrix}A_P&B\\C&A_Q\end{smallmatrix}\bigr)$, conjugation by $D_t=\operatorname{diag}(tI_P,I_Q)$ replaces the directed couplings by $tB$ and $t^{-1}C$. We prove $$\min_{t>0}\max(tb,c/t)=\sqrt{bc},\qquad t_*=\sqrt{c/b},$$ where $b=\lVert B\rVert$ and $c=\lVert C\rVert$. Hence the balanced RH-161 rank gate is $$\max(a,d)\sqrt{bc}<1.$$ The similarity does not come for free: transforming the Riesz projector back to the original Hilbert norm multiplies its error bound by $\max(t_*,t_*^{-1})$. Thus an imbalanced system may have stable spectral rank but a poorly conditioned packet graph. The triangular limit is treated directly because the optimizing similarity becomes singular. A 512-case audit verifies the exact off-diagonal norm and optimum. No physical all-level balance is claimed.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Balanced Similarities for Directed Packet Couplings\
  Rank Rescue and the Original-Norm Conditioning Price
```

## Markdown 正文

# The scalar block-similarity family

Let $P$ be an orthogonal projection, $Q=I-P$, and write $$A=\begin{pmatrix}A_P&B\\C&A_Q\end{pmatrix}.$$ For $t>0$ put $$D_t=\begin{pmatrix}tI_P&0\\0&I_Q\end{pmatrix},\qquad
 \widetilde A_t=D_tAD_t^{-1}
 =\begin{pmatrix}A_P&tB\\t^{-1}C&A_Q\end{pmatrix}.$$ The block diagonal part and its resolvent are unchanged. The off-diagonal part $\widetilde E_t$ satisfies the exact identity $$\lVert\widetilde E_t\rVert
 =\max\{t\lVert B\rVert,t^{-1}\lVert C\rVert\}.$$ Indeed, $\widetilde E_t^*\widetilde E_t$ is block diagonal with diagonal blocks $t^{-2}C^*C$ and $t^2B^*B$.

# Optimal balance

[\[thm:balance\]]{#thm:balance label="thm:balance"} Let $b,c>0$. Then $$\inf_{t>0}\max(tb,c/t)=\sqrt{bc},$$ and the unique minimizer is $t_*=\sqrt{c/b}$.

For every $t$, the maximum is at least the geometric mean $\sqrt{(tb)(c/t)}=\sqrt{bc}$. At $t_*$ the two arguments are equal to that value, proving optimality and uniqueness.

The Schur feedback $adbc$ is unchanged by this similarity. Balancing is not a new spectral invariant; it is the optimal way to feed the same directed data into a one-norm Neumann theorem.

# Balanced Neumann certificate

Let $\Gamma$ isolate the packet block from the complement and suppose $$\sup_{z\in\Gamma}\lVert(z-A_P)^{-1}\rVert\le a,qquad
 \sup_{z\in\Gamma}\lVert(z-A_Q)^{-1}\rVert\le d.$$ Put $M=\max(a,d)$ and let $L=|\Gamma|$.

[\[thm:certificate\]]{#thm:certificate label="thm:certificate"} If $$\theta=M\sqrt{bc}<1,$$ then $\Gamma$ remains in the resolvent under the full off-diagonal homotopy, and the enclosed Riesz rank equals $\operatorname{rank}P$. In the balanced norm, $$\lVert\widetilde\Pi-P\rVert
 \le \delta_t:=\frac{L}{2\pi}
 \frac{M^2\sqrt{bc}}{1-M\sqrt{bc}}.$$ In the original norm, $$\lVert\Pi-P\rVert\le
 \max(t_*,t_*^{-1})\,\delta_t.$$ If the last quantity is below one, it supplies a graph certificate.

Apply the RH-161 Neumann theorem to $\widetilde A_{t_*}$, whose off-diagonal norm is $\sqrt{bc}$ by Theorem [\[thm:balance\]](#thm:balance){reference-type="ref" reference="thm:balance"} [@WangRH161]. Similar operators have the same spectrum and Riesz rank. Since $D_t$ commutes with $P$, $$\widetilde\Pi-P=D_t(\Pi-P)D_t^{-1}.$$ Thus $\lVert\Pi-P\rVert\le\lVert D_t^{-1}\rVert\lVert D_t\rVert\lVert\widetilde\Pi-P\rVert$, and $\lVert D_t^{-1}\rVert\lVert D_t\rVert=\max(t,t^{-1})$.

Because $ad\le M^2$, the Schur gate $adbc<1$ from RH-163 is never weaker than the squared balanced gate $M^2bc<1$ [@WangRH163]. The value of the balanced theorem is its direct compatibility with single-norm perturbation machinery and its transparent conditioning ledger.

# Triangular systems and graph asymmetry

If $c=0$ or $b=0$, the infimum in Theorem [\[thm:balance\]](#thm:balance){reference-type="ref" reference="thm:balance"} is zero but is not attained by an invertible $D_t$. One must not insert $t=0$ or $t=\infty$ as a similarity. Instead, the original block operator is triangular and the enclosed rank is preserved exactly under spectral separation.

If $c=0$ but $b$ is large, the packet range is invariant although the Riesz projection can have a large complementary-to-packet off-diagonal block. This explains the divergent similarity condition number: rank needs closed feedback, while a well-conditioned two-sided projection needs control of both directions.

# The full feasible scaling interval

Balancing is the center of an explicit interval, not merely one lucky scale.

For $b,c,M>0$, the transformed RH-161 gate $$M\max(tb,c/t)<1$$ holds exactly for $$Mc<t<\frac1{Mb}.$$ This interval is nonempty if and only if $M^2bc<1$. The balanced scale $t_*=\sqrt{c/b}$ is its logarithmic midpoint and maximizes the smaller logarithmic distance to its two endpoints.

The maximum is below $M^{-1}$ precisely when both $tb<M^{-1}$ and $c/t<M^{-1}$, giving the interval. It is nonempty exactly when $Mc<(Mb)^{-1}$. Taking logarithms shows that the midpoint is $$\tfrac12\bigl(\log(Mc)+\log((Mb)^{-1})\bigr)
 =\tfrac12\log(c/b)=\log t_*.$$

The interval is useful for graph optimization. One may move away from $t_*$ to reduce $\max(t,t^{-1})$ while remaining inside the rank-feasible region. The optimal graph scale therefore need not be the optimal coupling scale; it is a one-dimensional certified minimization over this explicit interval.

# Finite audit and route consequence

The audit draws 512 rectangular pairs $(B,C)$, computes the exact norm of $\bigl(\begin{smallmatrix}0&tB\\t^{-1}C&0\end{smallmatrix}\bigr)$, and compares it with $\max(tb,c/t)$. It also tests the analytic minimizer against four neighboring scales. No failure occurs.

RH-164 supplies an optimized fallback certificate and a warning: a rescued rank gate is not automatically a usable packet graph. The next geometric task is to choose $\Gamma$ so that $a$ and $d$ are controlled rather than postulated. No physical realization, contour, all-level margin, Gate A, self-adjoint operator, zeta identity, or RH claim is made.
