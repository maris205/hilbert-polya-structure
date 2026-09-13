---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-178-orientation-marked-cycle-traces"
canonical_tex: "zeta_mvp0/papers/RH-178-orientation-marked-cycle-traces/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-178-orientation-marked-cycle-traces/main.pdf"
source_sha256: "64a4f361a4719bc74c0f2e8efb6caeea39cbf7737c4ef62aeaf6d007b140d1cc"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Orientation-Separating Marked Cycle Traces Why the Geometric Determinant Needs a Directed Rank-One Datum

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-178-orientation-marked-cycle-traces>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-178-orientation-marked-cycle-traces/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-178-orientation-marked-cycle-traces/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-178-orientation-marked-cycle-traces/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-178-orientation-marked-cycle-traces/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The double-cycle model of RH-177 realizes the RH-80 geometric cloud factor exactly, but a scalar determinant cannot determine temporal orientation. For every length $L$, the forward and reverse cycles $C_L$ and $C_L^{-1}$ have the same determinant and the same ordinary power traces. Hence the three doubled completions "forward--forward", "forward--reverse", and "reverse--reverse" are spectrally indistinguishable.

  We add one rank-one edge marker. Let $J=|e_0\rangle\langle e_1|$, let $Q=I-|\mathbf1\rangle\langle\mathbf1|$, and compress to the zero-mean cycle space. For $L>2$, $$\operatorname{Tr}(QJQ C_L)=1-\frac1L,
   \qquad
   \operatorname{Tr}(QJQ C_L^{-1})=-\frac1L.$$ The orientation gap is exactly one. Thus the enhanced finite datum $$\bigl(\det(I-zC_L^\circ),
   \{\operatorname{Tr}(J^\circ(C_L^\circ)^m)\}_{m\ge1}\bigr)$$ retains both the cloud divisor and the time arrow.

  The marker is stable. If $\left\lVert A-B\right\rVert\le\varepsilon$ and $\left\lVert A\right\rVert,\left\lVert B\right\rVert\le R$, then for trace-class $J$, $$|\operatorname{Tr}J(A^m-B^m)|
   \le \left\lVert J\right\rVert_1\,mR^{m-1}\varepsilon.$$ In particular, the one-step orientation remains separated under two perturbations whenever their total marked error is less than one. A 120-case complex perturbation audit records zero bound failures; the exact orientation gap is one for all ten tested lengths.

  This closes an algebraic directed-marker leaf and explains why RH-161 kept marked traces as data independent of the determinant. It does not establish a physical marker, common-space marked-trace convergence, or a directed limit for the noisy transfer dynamics.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Orientation-Separating Marked Cycle Traces\
  Why the Geometric Determinant Needs a Directed Rank-One Datum
```

## Markdown 正文

# The scalar blindness problem

RH-177 constructs the finite normal cloud $$K_N=\lambda^{-1}(C_{N+1}^\circ\oplus C_{N+1}^\circ)$$ with determinant $\Pi_N(w/\lambda)^2$ [@WangRH177]. The construction contains a hidden choice: each cycle can run forward or backward. Spectral data alone cannot recover that choice because inversion merely permutes the roots of unity.

This is the finite-cycle version of a general obstruction in noncommutative dynamics. Products $AB$ and $BA$ have the same nonzero spectrum, while directed words can differ. RH-8 and RH-161 therefore retained marked traces as an independent output type [@WangRH8; @WangRH161]. The present model allows the need for that enhancement to be proved in one line and repaired by one rank-one marker.

# Forward and reverse cycles are spectrally identical

Let $L>2$ and define $$C_Le_j=e_{j+1\bmod L}.$$ Its inverse is the reverse cycle. Both have eigenvalue multiset $\{e^{2\pi ik/L}:0\le k<L\}$.

[\[thm:blind\]]{#thm:blind label="thm:blind"} For every $z\in\mathbb C$ and every integer $m\ge1$, $$\begin{aligned}
 \det(I-zC_L)&=\det(I-zC_L^{-1})=1-z^L,
 \label{eq:det-blind}\\
 \operatorname{Tr}C_L^m&=\operatorname{Tr}C_L^{-m}
 =\begin{cases}L,&L\mid m,\\0,&L\nmid m.
 \end{cases}
 \label{eq:trace-blind}\end{aligned}$$ The same equalities hold after restriction to the zero-mean space.

Inversion permutes the $L$th roots of unity, proving [\[eq:det-blind\]](#eq:det-blind){reference-type="eqref" reference="eq:det-blind"}. A cyclic permutation has a fixed basis vector under the $m$th power exactly when $L\mid m$; in that case every basis vector is fixed. Removing the common stationary eigenvalue one subtracts one from both power traces and divides both determinants by $1-z$.

Thus even the complete sequence of ordinary traces contains no orientation information. An additional noncentral observable is necessary.

# A rank-one edge marker

Define $$\label{eq:J}
 J=|e_0\rangle\langle e_1|.$$ For every matrix $X$, $$\operatorname{Tr}(JX)=\langle e_1,Xe_0\rangle.$$ The marker therefore asks whether one application of the dynamics transports the vertex $0$ to the vertex $1$.

[\[thm:marker\]]{#thm:marker label="thm:marker"} For $L>2$, $$\label{eq:full-marker}
 \operatorname{Tr}(JC_L)=1,
 \qquad
 \operatorname{Tr}(JC_L^{-1})=0.$$ Let $P=L^{-1}|\mathbf1\rangle\langle\mathbf1|$ be the stationary projection, $Q=I-P$, and $J^\circ=QJQ$. Then on the zero-mean cycle, $$\label{eq:reduced-marker}
 \operatorname{Tr}(J^\circ C_L^\circ)=1-\frac1L,
 \qquad
 \operatorname{Tr}(J^\circ(C_L^\circ)^{-1})=-\frac1L.$$ In both the full and reduced models, the forward--reverse gap equals one.

Since $C_Le_0=e_1$ and $C_L^{-1}e_0=e_{L-1}\perp e_1$, the full identities follow. Because $Q$ commutes with the cycle and $PC_L=C_LP=P$, $$\operatorname{Tr}(QJQ C_L)=\operatorname{Tr}(J(C_L-P))
 =\operatorname{Tr}(JC_L)-\operatorname{Tr}(JP).$$ Now $\operatorname{Tr}(JP)=\langle e_1,Pe_0\rangle=1/L$. Apply the same calculation to $C_L^{-1}$.

The compression correction $-1/L$ is the marker analogue of the $-1$ background in the reduced power-trace ledger. It affects both orientations equally and therefore preserves the unit gap.

# Higher marked words

For $m\ge1$, $$\operatorname{Tr}(JC_L^m)=
 \begin{cases}
 1,&m\equiv1\pmod L,\\
 0,&\text{otherwise},
 \end{cases}$$ whereas $$\operatorname{Tr}(JC_L^{-m})=
 \begin{cases}
 1,&m\equiv-1\pmod L,\\
 0,&\text{otherwise}.
 \end{cases}$$ Thus the entire marked sequence records the orientation and cycle length. One step already separates direction; the longer sequence supplies redundancy and can diagnose a noisy or perturbed cycle.

# Reconstruction and marker minimality

The determinant and one marked trace form a complete descriptor of an exact oriented single cycle within this model class.

[\[prop:reconstruct\]]{#prop:reconstruct label="prop:reconstruct"} Suppose $A$ is known a priori to be either $C_L^\circ$ or $(C_L^\circ)^{-1}$ for some $L>2$. Then:

1.  the degree of $\det(I-zA)=\Pi_{L-1}(z)$ determines $L$;

2.  the sign relative to $-1/L$ of $\operatorname{Tr}(J^\circ A)$ determines the orientation.

Specifically, the marked value is $1-1/L$ in the forward case and $-1/L$ in the reverse case.

The reduced dimension and determinant degree are $L-1$. Once $L$ is known, Theorem [\[thm:marker\]](#thm:marker){reference-type="ref" reference="thm:marker"} gives two distinct marked values separated by one.

No scalar augmentation can use rank zero, while Theorem [\[thm:marker\]](#thm:marker){reference-type="ref" reference="thm:marker"} shows rank one suffices. In that elementary sense the edge marker is minimal. The claim is model-relative: a physical system may require a more complicated state--observable marker to remain target independent.

For a doubled cloud, retain ordered channel markers $J_1,J_2$. Put $a=1-1/L$ and $b=-1/L$. The four orientation choices have signatures

  orientation         first mark   second mark
  ------------------ ------------ -------------
  forward--forward       $a$           $a$
  forward--reverse       $a$           $b$
  reverse--forward       $b$           $a$
  reverse--reverse       $b$           $b$

If only the sum $J_1+J_2$ is observed, the two mixed orientations coincide. Thus an unordered scalar marker distinguishes three classes, whereas an ordered marker pair distinguishes all four. This is directly relevant when the two cloud copies are assigned to left/right or parity channels.

For a double cycle, choose markers $J_1,J_2$ on the two summands. The scalar determinant is the same for all orientation pairs, while $$\bigl(\operatorname{Tr}(J_1K),\operatorname{Tr}(J_2K)\bigr)$$ distinguishes forward--forward, forward--reverse, and reverse--reverse after the common scale $\lambda^{-1}$ is removed.

# Perturbative stability

[\[thm:stability\]]{#thm:stability label="thm:stability"} Let $A,B$ be bounded operators with $\left\lVert A\right\rVert,\left\lVert B\right\rVert\le R$, let $J\in\mathcal S_1$, and let $m\ge1$. Then $$\label{eq:stability}
 |\operatorname{Tr}J(A^m-B^m)|
 \le \left\lVert J\right\rVert_1\,mR^{m-1}\left\lVert A-B\right\rVert.$$

Use the telescoping identity $$A^m-B^m=\sum_{k=0}^{m-1}A^{m-1-k}(A-B)B^k.$$ Every summand has operator norm at most $R^{m-1}\left\lVert A-B\right\rVert$. The trace duality inequality $|\operatorname{Tr}(JX)|\le\left\lVert J\right\rVert_1\left\lVert X\right\rVert$ and the triangle inequality give [\[eq:stability\]](#eq:stability){reference-type="eqref" reference="eq:stability"} [@Simon2005].

Let $A_+$ and $A_-$ approximate $C_L$ and $C_L^{-1}$ with errors $\varepsilon_+$ and $\varepsilon_-$. For the reduced marker, $$|\operatorname{Tr}(J^\circ A_+)-\operatorname{Tr}(J^\circ A_-)|
 \ge1-\left\lVert J^\circ\right\rVert_1(\varepsilon_++\varepsilon_-).$$ Hence the marked traces remain distinct whenever the rightmost error term is less than one.

This criterion is target independent: the marker is specified by the cycle edge, not fitted to the perturbed eigenvectors. A physical application must still identify what state--observable pair corresponds to that edge.

# Enhanced finite determinant datum

The natural finite cyclic output is not the scalar determinant alone but $$\label{eq:enhanced}
 \mathfrak D_L(A,J)=
 \left(
 \det(I-zA),
 \{\operatorname{Tr}(JA^m)\}_{m\in\mathcal M}
 \right),$$ where $\mathcal M$ is a fixed set of directed word lengths. The first component determines the spectral divisor. The second records temporal orientation. They are logically independent: Theorem [\[thm:blind\]](#thm:blind){reference-type="ref" reference="thm:blind"} shows that the first cannot reconstruct the second.

For the prime-dynamics route, the finite enhanced datum should eventually be transported through the Riesz projection and then shown to converge in common coordinates. RH-161 names this downstream obligation $T$; the present paper only proves that the finite model has a minimal and stable directional observable.

# Audit

The exact audit uses lengths $3,4,5,7,11,16,24,32,48,64$. In every case the reduced forward and reverse one-step marked traces have gap one to floating precision, while ordinary traces agree. The minimum recorded gap is $0.9999999999999998$.

For each length, twelve complex perturbations with operator norms $0.01,0.02,0.03$ are applied at powers one through five. The exact observed marked error is compared with Theorem [\[thm:stability\]](#thm:stability){reference-type="ref" reference="thm:stability"}. All 120 cases satisfy the bound, with zero failures. The audit validates arithmetic and does not certify a physical noisy cycle.

# Boundary and next interface

RH-178 proves an algebraic directed-marker leaf: $$\text{cycle determinant} + \text{rank-one marked traces}
 \quad\text{retains spectrum and orientation}.$$ It does not prove that the physical transfer dynamics carries this marker, that the marker is trace class uniformly across scales, or that marked words converge after Riesz transport. Those remain parts of the physical $T$ leaf.

The next paper turns to the integer calibration problem: how should the cycle length $L$ relate to the half-log reset rank and the observed RH-15 cloud degree? No Gate-A closure, self-adjoint completion, zeta identity, or Riemann-hypothesis conclusion is made.
