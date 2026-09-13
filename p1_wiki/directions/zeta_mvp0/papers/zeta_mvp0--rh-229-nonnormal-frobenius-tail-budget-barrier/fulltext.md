---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-229-nonnormal-frobenius-tail-budget-barrier"
canonical_tex: "zeta_mvp0/papers/RH-229-nonnormal-frobenius-tail-budget-barrier/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-229-nonnormal-frobenius-tail-budget-barrier/main.pdf"
source_sha256: "3734c689a7dcfb76264c26a8a06383517dd8dbb2286a348235f2f68543e2b193"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Nonnormal Frobenius Tail-Budget Barrier Why a Valid Whole-Matrix Bound Does Not Close the Determinant

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-229-nonnormal-frobenius-tail-budget-barrier>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-229-nonnormal-frobenius-tail-budget-barrier/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-229-nonnormal-frobenius-tail-budget-barrier/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-229-nonnormal-frobenius-tail-budget-barrier/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-229-nonnormal-frobenius-tail-budget-barrier/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-228 controls every complete shell resolved beyond the selected cloud, but not the unresolved operator complement. This paper tests the first whole-matrix certificate available without constructing a reducing projection.

  For any finite matrix $A$, Schur triangularization gives $$\sum_j|\lambda_j(A)|^2\le\left\lVert A\right\rVert_{\mathrm F}^2.$$ After factoring the Perron root, negative parity root, and selected bulk cloud, their squared eigenvalue masses may be subtracted from the Frobenius square. Combining the remainder with the regularized logarithmic tail inequality yields a valid finite-matrix upper bound.

  The bound fails quantitatively at every physical endpoint. On the closed unit disk it ranges from $5.15135$ to $169.27116$, so none of 32 cases passes the predeclared bound $<1$. Power fits grow as $\sigma^{-1.025}$ and $\sigma^{-1.033}$ on the two channels. The whole-matrix certificate is up to $5.56\times10^3$ times larger than the resolved-shell bound.

  This is a barrier for the raw Frobenius certificate, not for the determinant. Nonnormal singular mass can make $\left\lVert A\right\rVert_{\mathrm F}$ large without producing comparably large eigenvalue products. A useful next step must isolate a reducing complement or control a two-step trace-class object rather than apply the full one-step Frobenius norm.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  The Nonnormal Frobenius Tail-Budget Barrier\
  Why a Valid Whole-Matrix Bound Does Not Close the Determinant
```

## Markdown 正文

# From resolved roots to a whole operator

The finite bound of RH-228 depends on the actual omitted roots [@WangRH228]. For an unresolved finite matrix, one can seek an upper bound on their squared moduli. The Frobenius norm is natural because it is exactly computable from the sparse physical matrix.

Let the eigenvalues of $A\in\mathbb C^{N\times N}$, with algebraic multiplicity, be partitioned into selected values $S$ and omitted values $T$.

# Schur--Frobenius control

[\[thm:schur\]]{#thm:schur label="thm:schur"} For every finite matrix $A$, $$\label{eq:schur}
 \sum_{j=1}^N|\lambda_j(A)|^2\le\left\lVert A\right\rVert_{\mathrm F}^2.$$ Consequently, $$\label{eq:tailmass}
 \sum_{\lambda\in T}|\lambda|^2
 \le H_T(A):=
 \left\lVert A\right\rVert_{\mathrm F}^2-\sum_{\lambda\in S}|\lambda|^2.$$

Take a unitary Schur decomposition $A=URU^*$ with $R$ upper triangular and diagonal entries $\lambda_j(A)$. Unitary invariance gives $$\left\lVert A\right\rVert_{\mathrm F}^2=\left\lVert R\right\rVert_{\mathrm F}^2
 =\sum_j|\lambda_j(A)|^2+\sum_{i<j}|R_{ij}|^2,$$ which proves [\[eq:schur\]](#eq:schur){reference-type="eqref" reference="eq:schur"}. Subtract the selected eigenvalue masses to get [\[eq:tailmass\]](#eq:tailmass){reference-type="eqref" reference="eq:tailmass"}.

For a normal matrix, the off-diagonal Schur term vanishes and the bound is exact. For a strongly nonnormal matrix it can dominate.

[\[cor:det\]]{#cor:det label="cor:det"} Suppose every omitted eigenvalue obeys $|\lambda|\le\rho_T$ and $R\rho_T<1$. Then $$\label{eq:detbound}
 \sup_{|z|\le R}
 \left|\sum_{\lambda\in T}
 [\log(1-z\lambda)+z\lambda]\right|
 \le
 \frac{R^2H_T(A)}{2(1-R\rho_T)}.$$

Combine Theorem [\[thm:schur\]](#thm:schur){reference-type="ref" reference="thm:schur"} with the logarithmic tail theorem of RH-228.

The corollary is rigorous when the selected eigenvalues and the tail radius are exact. In the physical audit they come from a deterministic floating-point spectral ordering, so the resulting number is a numerical certificate candidate rather than an interval proof.

# Physical budget

For each raw folded Markov matrix $M$, use the Hardy-scaled matrix $A=M/0.85$. The selected set contains:

1.  the scaled Perron resonance;

2.  the scaled negative parity resonance;

3.  the RH-222 shell-complete bulk cloud.

The next complete shell supplies the numerical tail-radius upper candidate $$\rho_T=
 \min_{\lambda\in\Lambda_{\rm sel}}|\lambda|
 -g_{\rm shell}.$$ The sparse Frobenius square is computed directly from all matrix entries.

The disk radius is frozen at $R=1$, and the gate is $$\frac{H_T(A)}{2(1-\rho_T)}<1.$$ No endpoint passes.

  diagnostic                       left/right minimum   left/right maximum
  ------------------------------ -------------------- --------------------
  next-shell modulus                     below $0.30$         below $0.30$
  full logarithmic upper bound                 $5.15$             $169.27$
  resolved-shell upper bound                 positive            $0.16804$
  full/resolved ratio                greater than one            $5563.49$

The condition $R\rho_T<1$ is comfortably satisfied. The failure is entirely in the squared-mass budget.

# Small-noise scaling

For each channel, fit $$B_\sigma=C\sigma^{-\alpha}$$ to the sixteen whole-matrix upper bounds in logarithmic least squares. The descriptive exponents are $$\alpha_L=1.02472,\qquad \alpha_R=1.03258.$$ The fit is not an asymptotic theorem, but it identifies the scale of the certificate failure: the bound worsens rather than stabilizes as noise decreases.

The behavior is consistent with narrow stochastic rows. As $\sigma$ shrinks, the transition matrix approaches a sparse near-deterministic transport; many singular directions remain large even though most nonperipheral eigenvalues may be small. The Frobenius norm records those directions.

# Why the negative result is limited

Theorem [\[thm:schur\]](#thm:schur){reference-type="ref" reference="thm:schur"} cannot distinguish eigenvalue mass from the strictly upper triangular part of the Schur form. Therefore failure of [\[eq:detbound\]](#eq:detbound){reference-type="eqref" reference="eq:detbound"} does not imply divergence of $$\sum_{\lambda\in T}|\lambda|^2.$$ It only says that the raw Frobenius norm is too coarse to prove a useful bound.

Several stronger routes remain:

1.  construct a Riesz or reducing projection for the moving outer cloud and measure the actual complementary block;

2.  remove dominant singular directions before applying an ideal norm;

3.  square the complement, seeking a trace-class bound for a two-step Fredholm determinant;

4.  use power traces and phase cancellation instead of singular values.

These possibilities are compatible with the abstract relative determinant route in RH-80 [@WangRH80] and with trace-ideal determinant theory [@Simon2005]. None is constructed here.

# Route consequence

The resolved shell tail is small, while the whole-matrix Frobenius tail is large. This sharply locates the next wall: $$\text{explicit outer roots}
 \quad\longleftrightarrow\quad
 \text{unresolved nonnormal complement}.$$ Before attacking that complement, RH-230 tests whether the selected regularized factors at least agree between the two physical channels and whether their adjacent-scale differences contract.

No determinant divergence, self-adjoint realization, or arithmetic identification is proved. Gate A remains open.
