---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-132-canonical-partial-isometry-forcing-gauge"
canonical_tex: "zeta_mvp0/papers/RH-132-canonical-partial-isometry-forcing-gauge/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-132-canonical-partial-isometry-forcing-gauge/main.pdf"
source_sha256: "5433a7411b84783ea0087886d115f0b9909c46d118a6eb750f30eb487d6b92ff"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Canonical Partial-Isometry Gauges Principal Angles, Changing Supports, and Minimal Positive Forcing

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-132-canonical-partial-isometry-forcing-gauge>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-132-canonical-partial-isometry-forcing-gauge/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-132-canonical-partial-isometry-forcing-gauge/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-132-canonical-partial-isometry-forcing-gauge/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-132-canonical-partial-isometry-forcing-gauge/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The floor-free audit RH-130 replaced positive-definite tail transport by a semidefinite problem with rank creation, while RH-131 showed that singular Rayleigh theory is exact on a specified support. We now construct the canonical gauge between changing supports. For orthogonal projectors $P,Q$, take the polar decomposition $$QP=W|QP|.$$ The polar factor $W$ is a basis-independent partial isometry that maps the principal source directions to the principal target directions. It is the unique Procrustes optimizer when the nonzero principal cosines are simple, and in general is the canonical optimizer selected by the polar calculus. Its initial and final defects identify exactly which source and target directions cannot be connected multiplicatively.

  For a source tail $D$, target tail $D'$, and factor $b\geq0$, we prove that $$F_b=(D'-bWDW^*)_+$$ is a valid positive forcing and minimizes trace among all $F\succeq0$ with $D'\preceq bWDW^*+F$. Moreover, target mass on the complement of $WW^*$ is an unavoidable lower bound for every such forcing. A 4,096-case audit verifies partial-isometry identities, Procrustes optimality against sampled competitors, positive dominance, and the unmatched-range lower bound with zero failures.

  Applied to RH-130, the 96 adjacent pairs split canonically into 30 $0\to0$ vacuous edges, 42 $4\to4$ transport-eligible edges, and 24 $0\to4$ forcing-only edges. The minimal normalized birth strength is subunit on 22 of those 24 edges; the remaining two equal the previously identified bad value $9.4363$. The affine route is therefore neither a formal rescue nor a uniform success: it has an exact canonical decomposition and a sharply localized finite obstruction.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Canonical Partial-Isometry Gauges\
  Principal Angles, Changing Supports, and Minimal Positive Forcing
```

## Markdown 正文

# Why a partial isometry is the correct gauge

Let $E,F$ be closed subspaces of a finite-dimensional Hilbert space $H$, with orthogonal projectors $P,Q$. A full invertible gauge presupposes equal dimensions and hides the possibility that a target direction has no source ancestor. RH-130 showed that precisely this event occurs in the discarded memory tail: zero tail support can become four-dimensional at the next scale. No change of coordinates turns that birth into multiplicative transport.

The operator $QP:E\to F$ contains all geometry shared by the two supports. Its nonzero singular values are the principal cosines $\cos\theta_1,\ldots,\cos\theta_k$. Its polar factor maps the corresponding principal vectors isometrically and leaves orthogonal or dimension-mismatched directions unmatched. Unlike an ordered eigenframe gauge, this construction depends only on the two support projectors and is invariant under basis changes inside either support [@Kato1995; @Bhatia1997].

# Canonical polar transport

Choose orthonormal frame matrices $U$ and $V$ for $E$ and $F$. If $$V^*U=L\Sigma R^*,$$ then the polar partial isometry is $$W=V L_kR_k^*U^*,$$ where $k$ is the number of nonzero principal cosines. Its initial and final projectors are $$W^*W=U R_kR_k^*U^*,\qquad
 WW^*=V L_kL_k^*V^*.$$

[\[thm:polar\]]{#thm:polar label="thm:polar"} The operator $W$ is the polar factor of $QP$. It is independent of the chosen frames $U,V$, maps paired principal source vectors to paired target vectors, and has rank $k=\operatorname{rank}(QP)$. Among rank-$k$ partial isometries with initial space in $E$ and final space in $F$, it maximizes $$\Re\operatorname{Tr}(X^*QP)=\sum_{j=1}^k\cos\theta_j.$$ For equal-dimensional transverse supports it equivalently minimizes the orthogonal Procrustes displacement between their frames.

The displayed singular-value decomposition gives $QP=VL\Sigma R^*U^*$ on $E$, hence its polar decomposition has partial factor $V L_kR_k^*U^*$. Replacing $U,V$ by different orthonormal frames conjugates the reduced factors and leaves the ambient operator unchanged. Von Neumann's trace inequality bounds the objective for every admissible $X$ by the sum of the first $k$ singular values of $QP$; the polar factor attains equality. In the equal-rank case, $\|VO-U\|_F^2=2r-2\Re\operatorname{Tr}(O^*V^*U)$, so the same maximizer solves the Procrustes problem [@GolubVanLoan2013].

The theorem gives a natural geometry-only gauge, but it does not yet make the gauge dynamical: a future paper must show that the memory/packet update actually produces these adjacent support projectors or a controlled approximation to them.

# Unmatched directions are forcing

Let $D\succeq0$ be supported on $E$, let $D'\succeq0$ be supported on $F$, and set $\widetilde D=WDW^*$. Fix a proposed multiplicative factor $b$. The Hermitian residual is $$X_b=D'-b\widetilde D.$$ Write $X_b=X_{b,+}-X_{b,-}$ for its positive and negative parts.

[\[thm:forcing\]]{#thm:forcing label="thm:forcing"} The operator $$F_b=X_{b,+}$$ satisfies $F_b\succeq0$ and $D'\preceq b\widetilde D+F_b$. Among all positive $F$ satisfying this inequality, it has minimum trace: $$\operatorname{Tr}F\geq\operatorname{Tr}X_{b,+}=\operatorname{Tr}F_b.$$

Since $F_b-X_b=X_{b,-}\succeq0$, the displayed forcing is feasible. Let $P_+$ be the positive spectral projector of $X_b$. For any feasible $F$, compression of $F-X_b\succeq0$ to $P_+H$ gives $\operatorname{Tr}(P_+FP_+)\geq\operatorname{Tr}X_{b,+}$. Positivity gives $\operatorname{Tr}F\geq\operatorname{Tr}(P_+FP_+)$, proving optimality.

This result does not claim that $F_b$ is the least element in Loewner order; positive majorants need not form a lattice. Trace is the exact convex cost for which the positive part is canonical and sharp.

[\[cor:unmatched\]]{#cor:unmatched label="cor:unmatched"} Let $Q_0=I-WW^*$ be the unmatched target projector. Every feasible forcing satisfies $$Q_0FQ_0\succeq Q_0D'Q_0,
 \qquad
 \operatorname{Tr}F\geq\operatorname{Tr}(Q_0D'Q_0).$$

The transported tail is supported on $WW^*$, so $Q_0\widetilde DQ_0=0$. Compress the defining inequality to $Q_0H$ and take traces.

Thus a target dimension excess is not just a poor principal angle. It is an additive source with a quantitative, gauge-independent lower bound. When $D=0$ and $D'\neq0$, the whole target tail is forcing and $F_b=D'$ for every $b$.

# Synthetic audit

We sample 4,096 pairs of subspaces in ambient dimension twelve. Half have equal ranks one through six; half have target rank strictly larger than source rank. In every case the SVD polar map satisfies its initial and final projector identities. On the 2,048 equal-rank cases, it beats all 48 random orthogonal Procrustes competitors sampled per instance. Random positive source and target tails then test Theorem [\[thm:forcing\]](#thm:forcing){reference-type="ref" reference="thm:forcing"}: every positive-part forcing dominates the residual, and its trace exceeds the unmatched target lower bound. No failure occurs. The tests are numerical checks of exact finite-dimensional theorems, not evidence for all-level dynamical coherence.

![Procrustes advantage of the polar gauge, unavoidable unmatched forcing, and the exact RH-130 transition classification.](<../../../../../zeta_mvp0/papers/RH-132-canonical-partial-isometry-forcing-gauge/figures/canonical_partial_isometry_forcing_gauge.pdf>){#fig:audit width="\\textwidth"}

# RH-130 decomposition and affine implications

The 120 RH-130 states have tail rank either zero or four. Pairing adjacent scales, 30 edges are $0\to0$, 42 are $4\to4$, and 24 are $0\to4$; there are no $4\to0$ edges. The polar-gauge interpretation is immediate.

On a $0\to0$ edge, tail transport is vacuous. On a $4\to4$ edge, the full reduced support is transport-eligible; 37 of these 42 edges give a positive floor-free multiplicative candidate, while five have a finite factor but push the transferred Rayleigh constant to at least one. On every $0\to4$ edge, the source tail is zero and the target tail is entirely a birth term. The infinite factors of RH-130 are exactly these 24 cases.

In normalized target coordinates the least scalar forcing for a birth edge is its target squared Rayleigh constant. Across the 24 births this value ranges from $6.19\times10^{-24}$ to $9.4363$, with median $1.51\times10^{-12}$. Twenty-two births are subunit. The two superunit births are the left-channel final-phase states at $\sigma=0.08$ already isolated in RH-130. Hence additive forcing repairs the rank logic on every edge, but does not automatically restore positivity on those two states.

The next task is no longer ambiguous. One must derive adjacent supports and their polar map from the actual packet recursion, decompose the next tail as transported old tail plus a born-memory block, and estimate the normalized trace or Rayleigh cost of that block. Post hoc optimization over arbitrary exact-Gram gauges is no longer the target.

We have constructed a canonical support gauge, proved its principal-angle optimality, and identified the trace-minimal positive forcing and unmatched lower bound. We have not derived this gauge from the physical memory recursion, proved all-level affine coefficients, controlled the two finite superunit birth states, established a normalized-base liminf or uniform Stage A, constructed a Hilbert--Polya operator, identified zeta zeros, or proved the Riemann Hypothesis.
