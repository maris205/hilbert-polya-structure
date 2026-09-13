---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-176-finite-cyclic-history-closure"
canonical_tex: "zeta_mvp0/papers/RH-176-finite-cyclic-history-closure/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-176-finite-cyclic-history-closure/main.pdf"
source_sha256: "6c35d1c67567a1f85e0677af735fb334d5a415114a93576ed623e097267b6184"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite Cyclic Closure of Normalized History Exact Determinants, Strong Local Approximation, and the Wrap-Edge Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-176-finite-cyclic-history-closure>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-176-finite-cyclic-history-closure/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-176-finite-cyclic-history-closure/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-176-finite-cyclic-history-closure/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-176-finite-cyclic-history-closure/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-175 proves that the literal infinite-history completion contains a weighted unilateral shift and cannot be a trace-ideal determinant operator. We replace the infinite tail by a finite clock. Let $C_L$ be the unitary cycle on $\mathbb C^L$, $C_Le_j=e_{j+1\bmod L}$. Then $$\det(I-qC_L)=1-q^L.$$ The stationary constant mode has eigenvalue one. On its orthogonal complement $\mathcal Z_L=\mathbf1^\perp$, the reduced cycle satisfies $$\det_{\mathcal Z_L}(I-qC_L)=
   \frac{1-q^L}{1-q}=1+q+\cdots+q^{L-1}.$$ Thus a finite cyclic history closure realizes the geometric polynomial exactly, without an infinite shift disk or a noncompact tail.

  The closure has a sharp topology boundary. If $S_L$ is the nilpotent finite shift, then $C_L-S_L$ is one rank-one wrap edge of operator norm one, so there is no operator-norm approximation. Under natural zero extensions, $C_L\to S$ strongly on every fixed finite-support vector: the local dynamics stabilize while the determinant is carried entirely by the distant wrap. This is precisely why the cyclic determinant can differ radically from the nilpotent finite-section determinant.

  A 240-case complex audit checks the reduced determinant identity and orientation invariance with maximum relative error $8.0\times10^{-15}$; all ten tested wrap defects have norm one and vanish on the chosen fixed-support vectors. The result supplies an exact algebraic candidate, not a physical derivation of a cycle from the reset history or noisy transfer operator.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Finite Cyclic Closure of Normalized History\
  Exact Determinants, Strong Local Approximation, and the Wrap-Edge Boundary
```

## Markdown 正文

# From the shift wall to a finite clock

The infinite-history operator remembers every past block by shifting it one position. Its constant nonzero tail weight produces the spectral disk and non-Schatten obstruction of RH-175 [@WangRH175]. A finite memory of length $L$ has two obvious boundary conditions:

1.  truncate the oldest block, producing a nilpotent shift;

2.  return the oldest block to the current boundary, producing a cycle.

The first has trivial determinant $1$ and hides the shift disk in its pseudospectrum. The second is unitary and stores the boundary information in one wrap edge. This paper analyzes the second choice.

# Full and reduced cycle determinants

Let $L\ge2$ and let $C_L$ act on the standard basis of $\mathbb C^L$ by $$\label{eq:cycle}
 C_Le_j=e_{j+1\bmod L}.$$ The eigenvalues are the $L$th roots of unity $\omega_k=e^{2\pi ik/L}$, $0\le k<L$.

[\[thm:full\]]{#thm:full label="thm:full"} For every $q\in\mathbb C$, $$\label{eq:full-det}
 \det(I-qC_L)=\prod_{k=0}^{L-1}(1-q\omega_k)=1-q^L.$$ The same identity holds for the reverse cycle $C_L^{-1}$.

The polynomial $x^L-1$ factors as $\prod_{k=0}^{L-1}(x-\omega_k)$. Substitute $x=q^{-1}$ and multiply by $q^L$, with continuity at $q=0$. Inversion permutes the roots, so it leaves the determinant unchanged.

The vector $$\mathbf1_L=L^{-1/2}(1,\ldots,1)^T$$ is the stationary eigenvector with eigenvalue one. Let $$Q_L=I-\mathbf1_L\mathbf1_L^*,
 \qquad \mathcal Z_L=Q_L\mathbb C^L.$$ Because $Q_L$ commutes with $C_L$, the zero-mean space reduces the cycle.

[\[thm:reduced\]]{#thm:reduced label="thm:reduced"} For every $q\in\mathbb C$, $$\label{eq:geometric}
 \det_{\mathcal Z_L}(I-qC_L|_{\mathcal Z_L})
 =\prod_{k=1}^{L-1}(1-q\omega_k)
 =\Pi_{L-1}(q),$$ where $$\Pi_{L-1}(q)=1+q+\cdots+q^{L-1}.$$ The apparent quotient at $q=1$ is removable with value $L$.

The full determinant splits over the stationary line and zero-mean space: $$1-q^L=(1-q)
 \det_{\mathcal Z_L}(I-qC_L|_{\mathcal Z_L}).$$ Division by $1-q$ gives the finite geometric identity for $q\ne1$, and continuity gives the value at one.

This theorem is the first positive reason to prefer cyclic boundary conditions: the same polynomial that arose as the canonical pole section in RH-15 and RH-80 is already the reduced cycle determinant [@WangRH15; @WangRH80].

# The wrap edge

Let $S_L$ be the nilpotent finite shift $$S_Le_j=e_{j+1}\quad(0\le j<L-1),
 \qquad S_Le_{L-1}=0.$$ Then $$\label{eq:wrap}
 C_L-S_L=|e_0\rangle\langle e_{L-1}|.$$

[\[prop:wrap\]]{#prop:wrap label="prop:wrap"} The cyclic and nilpotent finite shifts differ by rank one and $$\label{eq:norm-wall}
 \left\lVert C_L-S_L\right\rVert=1$$ for every $L$.

Equation [\[eq:wrap\]](#eq:wrap){reference-type="eqref" reference="eq:wrap"} is immediate from the basis action. A rank-one operator $|u\rangle\langle v|$ has operator norm $\left\lVert u\right\rVert\left\lVert v\right\rVert=1$.

# The determinant is exactly the wrap contribution

The rank-one determinant lemma gives a second proof of Theorem [\[thm:full\]](#thm:full){reference-type="ref" reference="thm:full"} that exposes the boundary mechanism. Since $$C_L=S_L+|e_0\rangle\langle e_{L-1}|,$$ write $$I-qC_L=(I-qS_L)
 \left[I-q(I-qS_L)^{-1}|e_0\rangle\langle e_{L-1}|\right].$$ The nilpotent factor has determinant one. The matrix determinant lemma then gives $$\begin{aligned}
 \det(I-qC_L)
 &=1-q\langle e_{L-1},(I-qS_L)^{-1}e_0\rangle
 \label{eq:det-lemma}\\
 &=1-q^L,\end{aligned}$$ because $$(I-qS_L)^{-1}e_0=e_0+qe_1+\cdots+q^{L-1}e_{L-1}.$$

[\[prop:return\]]{#prop:return label="prop:return"} The coefficient $-q^L$ in the full cyclic determinant is the product of the $L-1$ forward shift edges and the single wrap edge. Removing any one edge makes the graph acyclic and returns determinant one.

Equation [\[eq:det-lemma\]](#eq:det-lemma){reference-type="eqref" reference="eq:det-lemma"} shows that the wrap marker reads the amplitude of the unique path from $e_0$ to $e_{L-1}$ through the nilpotent shift. That amplitude is $q^{L-1}$, and the wrap contributes the final factor $q$. If an edge is removed, no closed permutation cycle of length $L$ remains, so the finite shift can be ordered triangularly with zero diagonal.

This derivation clarifies why the wrap is invisible to every fixed local observation but decisive for the determinant: it is detected only after the longest possible return.

For $m$ independent reduced cycles of the same length, $$\det\left(I-q\bigoplus_{j=1}^m C_L^\circ\right)
 =\Pi_{L-1}(q)^m.$$ Thus the exponent of the geometric factor counts cyclic channels. The RH-80 square corresponds algebraically to two channels, while their physical interpretation and orientation remain separate questions.

The determinant distinction is entirely concentrated in this one edge: $$\det(I-qS_L)=1,
 \qquad
 \det(I-qC_L)=1-q^L.$$ Rank one is small in normalized rank but not small in operator norm, and its effect occurs at the longest cycle length $L$.

# Strong local approximation without norm approximation

Embed $\mathbb C^L$ as the first $L$ coordinates of $\ell^2(\mathbb N_0)$ and extend $C_L$ by zero on the complement; call the extension $\widetilde C_L$. Let $S$ be the unilateral shift.

[\[thm:strong\]]{#thm:strong label="thm:strong"} For every $x\in\ell^2(\mathbb N_0)$, $$\label{eq:strong}
 \widetilde C_Lx\longrightarrow Sx
 \quad\text{in norm}.$$ However, $$\label{eq:no-norm}
 \left\lVert\widetilde C_L-S\right\rVert\ge1$$ for every $L$. Thus convergence is strong but not in operator norm.

For a vector supported in coordinates $0,\ldots,m$, the two actions agree exactly once $L>m+1$: no mass reaches the wrap edge. Finite-support vectors are dense, and both operators are contractions, so the convergence extends to every $x$. On the other hand, for $e_L$ the cyclic extension vanishes while $Se_L=e_{L+1}$, proving [\[eq:no-norm\]](#eq:no-norm){reference-type="eqref" reference="eq:no-norm"}.

This topology split is structurally useful. Any fixed finite-time observation sees the unilateral history dynamics for sufficiently large $L$, while the determinant remembers the remote boundary through the term $q^L$. There is no contradiction: determinants are not continuous under strong operator convergence without trace-ideal control [@Simon2005].

# Fourier modes, traces, and root spacing

The discrete Fourier basis $$f_k=L^{-1/2}(1,\omega_k^{-1},\ldots,
 \omega_k^{-(L-1)})^T,
 \qquad \omega_k=e^{2\pi ik/L},$$ diagonalizes the cycle: $C_Lf_k=\omega_kf_k$. The stationary vector is $f_0$, so the reduced cycle contains exactly the modes $f_1,\ldots,f_{L-1}$.

[\[prop:ledger\]]{#prop:ledger label="prop:ledger"} For every integer $m\ge1$, $$\label{eq:reduced-trace}
 \operatorname{Tr}(C_L^\circ)^m=
 \begin{cases}
 L-1,&L\mid m,\\
 -1,&L\nmid m.
 \end{cases}$$ The minimum distance between distinct reduced eigenvalues is $$\label{eq:root-spacing}
 \min_{j\ne k}|\omega_j-\omega_k|=2\sin(\pi/L).$$ Consequently, circles of radius less than $\sin(\pi/L)$ isolate individual cycle roots.

The full power trace is $L$ when $L\mid m$ and zero otherwise. Removing the stationary eigenvalue subtracts one, proving [\[eq:reduced-trace\]](#eq:reduced-trace){reference-type="eqref" reference="eq:reduced-trace"}. The nearest roots are adjacent on the unit circle; their chord length is $|e^{2\pi i/L}-1|=2\sin(\pi/L)$.

The Fourier description makes the later physical obligations transparent. The geometric determinant fixes the phase grid, the trace ledger tests its periodic alignment, and the spacing determines the largest disjoint contour radius. As $L$ grows, the spacing is asymptotic to $2\pi/L$, so any physical cycle approximation used for separate Riesz shells must improve with the clock length. RH-180 turns this elementary geometry into a directed Schur certificate.

Orientation reversal sends $f_k$ to the eigenvalue $\omega_k^{-1}$ and hence permutes the same Fourier grid. This is why determinant and ordinary traces remain blind to the time arrow even though the edge action is reversed.

# Cycle length as a memory clock

The reduced polynomial has degree $L-1$, exactly the number of nonstationary cycle modes. Thus three integer quantities become equivalent within the model: $$\text{cycle length }L
 \quad\Longleftrightarrow\quad
 \text{reduced dimension }L-1
 \quad\Longleftrightarrow\quad
 \deg\Pi_{L-1}.$$ This does not yet specify how $L$ depends on noise. It only gives a precise dictionary once one of the three quantities is known. RH-179 will compare this dictionary with the half-log packet clock and observed cloud degrees.

# Finite audit

The audit uses lengths $$L=3,4,5,8,12,16,24,32,48,64$$ and 24 random complex parameters per length inside $|q|<0.75$, for 240 determinant cases. It compares the eigenvalue product of both orientations with $\Pi_{L-1}(q)$. The maximum relative geometric identity error is $7.99\times10^{-15}$, and the maximum forward--reverse determinant mismatch is below $10^{-12}$.

For every tested length, the explicit wrap defect has operator norm one. A test vector supported strictly before the boundary has action defect zero, illustrating Theorem [\[thm:strong\]](#thm:strong){reference-type="ref" reference="thm:strong"}. These calculations verify the implementation; Theorems [\[thm:full\]](#thm:full){reference-type="ref" reference="thm:full"}--[\[thm:strong\]](#thm:strong){reference-type="ref" reference="thm:strong"} are exact algebra.

# What is gained and what remains open

Finite cyclic closure solves two problems of the literal infinite history:

1.  it is finite rank, so its determinant is ordinary and exact;

2.  after removing the stationary mode, its determinant is the canonical geometric section.

It also creates two obligations. First, the wrap edge must be derived from physical time evolution rather than inserted because it gives the desired polynomial. Second, scalar determinants cannot distinguish $C_L$ from $C_L^{-1}$, so temporal orientation needs an enhanced observable.

RH-177 addresses the exact doubled cloud factor; RH-178 supplies a directed rank-one marker. No claim is made that the physical reset history, noisy transfer operator, or Riesz cloud is unitarily equivalent to this cycle. Gate A and every Hilbert--Polya conclusion remain open.
