---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-193-source-cyclic-spectral-quotient"
canonical_tex: "zeta_mvp0/papers/RH-193-source-cyclic-spectral-quotient/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-193-source-cyclic-spectral-quotient/main.pdf"
source_sha256: "0f575f9e8ee2399bdef32dafc13822634d2926b2d93003e2d544466b42f6e590"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Source-Cyclic Spectral Quotients A Type-Correct Reduction of Matrix-Valued Left-Multiplication Orbits

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-193-source-cyclic-spectral-quotient>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-193-source-cyclic-spectral-quotient/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-193-source-cyclic-spectral-quotient/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-193-source-cyclic-spectral-quotient/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-193-source-cyclic-spectral-quotient/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-192 proves that the full Frobenius operator $\mathcal L_A:X\mapsto AX$ is $m$ copies of $A$ and therefore cannot have the rank-one or rank-four ambient Riesz shells sought by the temporal packet. This paper constructs the exact reduced state selected by one physical matrix source: $$\mathcal K_S=\operatorname{span}\{S,AS,A^2S,\ldots\}.$$ The space is $\mathcal L_A$-invariant, cyclic, and has dimension $$\dim\mathcal K_S=\deg\mu_{A,S}\le\deg\mu_A\le n,$$ independently of the source width $m$. The restriction has minimal and characteristic polynomial $\mu_{A,S}$. Every right temporal packet built from the source orbit lies exactly in $\mathcal K_S$.

  For an observation seed $O^*$ of the same matrix type, orthogonal restriction to $\mathcal K_S$ preserves every moment $h_j=\langle O^*,A^jS\rangle_F$ and hence the complete scalar resolvent germ at infinity. A 140-case complex Arnoldi audit verifies invariance, intertwining, packet inclusion, and moment preservation with zero failures.

  The result removes the $m$-fold multiplicity obstruction at the correct source-relative type. It does not assert that $\dim\mathcal K_S$ is uniformly small in the physical limit. The next task is to determine whether the local length-four temporal roots match actual source-observable spectral modes of the base operator.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Source-Cyclic Spectral Quotients\
  A Type-Correct Reduction of Matrix-Valued Left-Multiplication Orbits
```

## Markdown 正文

# From an ambient no-go to a cyclic state

Let $A\in\mathbb C^{n\times n}$, let $S\in\mathbb C^{n\times m}$ be nonzero, and equip $\mathcal H_F=\mathbb C^{n\times m}$ with the Frobenius inner product. Define $\mathcal L_A X=AX$. RH-192 identifies $\mathcal L_A$ with $I_m\otimes A$, so its full Riesz multiplicities are multiples of $m$ [@WangRH192].

The physical experiment, however, never initializes an arbitrary element of $\mathcal H_F$. It initializes the single vector $S$ and observes its orbit. The smallest invariant state containing that experiment is therefore a cyclic subspace, not the complete direct sum.

# The source annihilator

Define the ideal $$\label{eq:annihilator-ideal}
 \mathcal I_{A,S}=\{p\in\mathbb C[z]:p(A)S=0\}.$$ It is nonzero because the characteristic polynomial of $A$ belongs to it. Since $\mathbb C[z]$ is a principal ideal domain, there is a unique monic generator, denoted $\mu_{A,S}$.

[\[prop:divisibility\]]{#prop:divisibility label="prop:divisibility"} The source minimal polynomial $\mu_{A,S}$ divides the ordinary minimal polynomial $\mu_A$ and therefore $$\label{eq:degree-bound}
 \deg\mu_{A,S}\le\deg\mu_A\le n.$$

Since $\mu_A(A)=0$, one has $\mu_A(A)S=0$, so $\mu_A\in\mathcal I_{A,S}=(\mu_{A,S})$.

The polynomial depends on the complete matrix source. Equivalently it is the least common multiple of the vector minimal polynomials of the columns of $S$. The columns can activate more modes, but they do not create $m$ independent copies when the entire matrix is treated as one source vector.

# Exact cyclic restriction

Set $$\label{eq:cyclic-space}
 \mathcal K_S=\operatorname{span}\{A^jS:j\ge0\}\subset\mathcal H_F.$$

[\[thm:cyclic-realization\]]{#thm:cyclic-realization label="thm:cyclic-realization"} The space $\mathcal K_S$ is invariant under $\mathcal L_A$ and $$\label{eq:cyclic-dimension}
 \dim\mathcal K_S=\deg\mu_{A,S}\le n.$$ The restricted operator $T_S=\mathcal L_A|_{\mathcal K_S}$ is cyclic with cyclic vector $S$. Its minimal and characteristic polynomials both equal $\mu_{A,S}$.

Invariance follows from $$\mathcal L_A(A^jS)=A^{j+1}S.$$ If $d=\deg\mu_{A,S}$, then $S,AS,\ldots,A^{d-1}S$ are linearly independent; otherwise a polynomial of degree below $d$ would annihilate $S$. The relation $\mu_{A,S}(A)S=0$ expresses every later power in their span, proving the dimension statement. The restriction is generated by $S$, so it is a cyclic $d$-dimensional operator. For a cyclic operator the minimal polynomial has degree $d$ and equals the characteristic polynomial.

The theorem is exact and contains no numerical-rank threshold. In a floating implementation, numerical cyclic dimension can be delicate because long power sequences become ill-conditioned. This affects computation, not the algebraic state type.

# Coordinate realization

Let $$\label{eq:isometry}
 Q:\mathbb C^d\longrightarrow\mathcal K_S$$ be any Frobenius isometry onto the cyclic space. Define $$\label{eq:reduced-data}
 T=Q^*\mathcal L_AQ,
 \qquad b=Q^*S.$$

[\[prop:intertwining\]]{#prop:intertwining label="prop:intertwining"} One has $$\label{eq:intertwining}
 \mathcal L_AQ=QT,
 \qquad
 A^jS=QT^jb
 \quad(j\ge0).$$ The spectrum and algebraic multiplicities of $T$ are those of the source-relative cyclic restriction, with no forced factor $m$.

Because $\operatorname{Ran}Q$ is invariant, $\mathcal L_AQ$ lies in $\operatorname{Ran}Q$ and equals $QQ^*\mathcal L_AQ=QT$. Induction gives the orbit identity.

If the source is cyclic for $A$ in the matrix sense, then $d=n$. This still reduces the ambient dimension from $nm$ to $n$, which is decisive at the physical widths 64--256.

# Exact inclusion of temporal packets

For indices $t_1,\ldots,t_L$, let the unnormalized temporal synthesis be $$\label{eq:synthesis}
 J=[A^{t_1}S,\ldots,A^{t_L}S].$$ Column normalization, polar orthogonalization, and invertible right coordinate changes do not alter its range.

[\[cor:packet-inclusion\]]{#cor:packet-inclusion label="cor:packet-inclusion"} Every right temporal subspace constructed from the source orbit is contained in $\mathcal K_S$. In reduced coordinates, $$\label{eq:reduced-synthesis}
 J=Q[T^{t_1}b,\ldots,T^{t_L}b].$$

This includes the RH-182 orthogonal packet and the right half of the RH-185 balanced bi-Krylov packet. The left temporal vectors need not lie in the same cyclic space, but they restrict to bounded coordinate functionals $Q^*W$. If $W^*V=I$ and $V\subset\mathcal K_S$, then $$\label{eq:left-restriction}
 (Q^*W)^*(Q^*V)=W^*QQ^*V=W^*V=I.$$ Thus biorthogonality is preserved when the left frame is restricted to the source-cyclic state.

# Observation moments

Let $O^*\in\mathcal H_F$ be an observation seed and define the scalar moments $$\label{eq:moments}
 h_j=\langle O^*,A^jS\rangle_F.$$ Write $c=Q^*O^*$.

[\[thm:moments\]]{#thm:moments label="thm:moments"} For every $j\ge0$, $$\label{eq:moment-realization}
 h_j=c^*T^jb.$$ For $|z|>\rho(T)$, $$\label{eq:transfer}
 \langle O^*,(zI-\mathcal L_A)^{-1}S\rangle_F
 =c^*(zI-T)^{-1}b
 =\sum_{j\ge0}\frac{h_j}{z^{j+1}}.$$

Insert $A^jS=QT^jb$ and use that $Q$ is an isometry. The resolvent formula follows from the convergent Neumann series.

The source-cyclic restriction therefore loses no scalar input-output data. Modes absent from $T$ are exactly modes not excited by the matrix source. A further observability quotient can remove modes whose residues vanish.

# Riesz projectors in the cyclic state

For a contour $\Gamma$ in the resolvent set of $T$, let $P_\Gamma(T)$ be its Riesz projector. Intertwining and holomorphic functional calculus give $$\label{eq:riesz-intertwining}
 P_\Gamma(\mathcal L_A)Q=QP_\Gamma(T).$$ The rank on $\mathcal K_S$ is therefore $\operatorname{rank}P_\Gamma(T)$, not $m\operatorname{rank}P_\Gamma(A)$. For one simple source-excited base eigenvalue it can equal one.

There is no contradiction with RH-192. The full ambient eigenspace has $m$ copies, while the cyclic orbit chooses at most one polynomially generated direction through that eigenspace. The remaining $m-1$ directions are not reachable from the single matrix seed.

# Finite Arnoldi audit

The implementation performs Frobenius Arnoldi on complex nonnormal matrices of dimensions 2 through 8 and source widths 1 through 4. Five independent trials per pair give 140 cases. Each matrix is similar to a diagonal matrix with distinct eigenvalues, and each random source activates all modes.

The audit checks:

1.  Frobenius orthogonality of the computed basis;

2.  closure and the intertwining defect $\mathcal L_AQ-QT$;

3.  inclusion of the first temporal powers;

4.  equality of $2n$ full and reduced moments for an independent observation seed.

All 140 cases pass the declared tolerances. This audit tests the implementation of exact identities; it is not evidence for a uniform physical numerical rank.

# What is and is not gained

The gain is structural: $$nm\text{-dimensional repeated spectrum}
 \quad\longrightarrow\quad
 d\le n\text{-dimensional source-cyclic spectrum}.$$ The temporal packet is now in the correct invariant state, and its left observation functionals restrict without breaking biorthogonality.

What remains open is equally important. The physical value of $d$ may grow with refinement. A four-vector temporal window does not imply $d=4$. Moreover, the cyclic space is source-dependent. Gate A eventually needs a selection that is canonical enough to transport between levels and to feed an intrinsic cloud ledger.

The immediate falsifiable question is finite: do the four temporal roots in the surviving $\sigma=0.01$ windows lie near actual eigenvalues activated by the source and seen by the observation? RH-194 performs that audit.
