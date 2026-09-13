---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-random-transposition-full-spectrum-route-a"
canonical_tex: "henon_dynamics/henon_random_transposition_full_spectrum_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_random_transposition_full_spectrum_route_a/paper/main.pdf"
source_sha256: "d8ead984974a73d8e042577d2dde5547891b48379626f7b6d826ed52a7d7d289"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Partition Spectrum, Return Traces, and the Primitive-Orbit Boundary of Random Transpositions

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_random_transposition_full_spectrum_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_random_transposition_full_spectrum_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_random_transposition_full_spectrum_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_random_transposition_full_spectrum_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We resolve every spectral sector of the lazy random-transposition chain on $S_n$. Partitions give exact eigenvalues and multiplicities, hence a finite determinant, return traces, and the spectral gap $2/n$. The same theorem separates two owners: no deterministic map on frozen $S_n$ realizes $P_n$, while a canonical weighted path-cycle product appears only after changing the phase space. That lift does not repair Route A.
author:
- 'Route-A structural certificate C183'
title: |
  Partition Spectrum, Return Traces, and the Primitive-Orbit Boundary\
  of Random Transpositions
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** random transposition; symmetric group; character ratio; Markov determinant; spectral gap.

chinese-simplified

中文摘要

本文对任意对称群上的惰性随机换位链给出全部表示论谱扇区、重数、有限行列式、 返回迹与精确的二次平均混合公式，谱隙恒为$2/n$。在冻结的$S_n$上，马尔可夫算子 并非单值确定性映射；改变到加权路径空间后虽有典范的原始闭路乘积，但该提升更换了 相空间与动力对象，不能修复路线[A]{lang="en"}的算术门槛。

关键词：随机换位；对称群；特征标比；马尔可夫行列式；谱隙。

# Frozen chain and complete spectrum

Choose $(i,j)\in[n]^2$ uniformly and right-multiply by $(ij)$, with $(ii)=e$. On uniform $L^2(S_n)$ this is central convolution $$P_n=\frac1{n^2}\sum_{i,j=1}^nR_{(ij)}.$$ For $\lambda\vdash n$, let $d_\lambda$ be its hook-length dimension. If $\tau$ is a transposition, Schur's lemma and the Frobenius character formula give $$\beta_\lambda=\frac1n+\frac{n-1}{n}
 \frac{\chi_\lambda(\tau)}{d_\lambda}
 =\frac1n+\frac1{n^2}\sum_i
 \{\lambda_i^2-(2i-1)\lambda_i\}.$$ The regular multiplicity is $d_\lambda^2$, so $$\det(I-zP_n)=\prod_{\lambda\vdash n}
 (1-z\beta_\lambda)^{d_\lambda^2},\qquad
 \operatorname{Tr}(P_n^k)=\sum_{\lambda\vdash n}
 d_\lambda^2\beta_\lambda^k.$$ The hook identity $\sum_{\lambda\vdash n}d_\lambda^2=n!$ proves completeness. A zero eigenvalue contributes the unit factor, so the degree of the displayed determinant may be smaller than $n!$.

#### Proof architecture.

The step measure is constant on conjugacy classes. Its Fourier transform at an irreducible representation therefore commutes with that representation and is scalar by Schur's lemma. Taking the matrix trace gives the character ratio above. The Frobenius content formula resolves the ratio, while the regular representation contains $d_\lambda$ copies of a $d_\lambda$-dimensional module. This proves the eigenvalue and multiplicity without a finite-size assumption; multiplying and summing the sectors gives the determinant and every trace.

  Partition datum                     Operator consequence                   Probabilistic consequence
  ----------------------------------- -------------------------------------- ---------------------------
  $d_\lambda$                         multiplicity $d_\lambda^2$             Plancherel weight
  $\chi_\lambda(\tau)/d_\lambda$      eigenvalue $\beta_\lambda$             decay mode
  $\sum d_\lambda^2\beta_\lambda^k$   $\operatorname{Tr}P_n^k$               $n!\Pr(X_k=e)$
  $\lambda\mapsto\lambda'$            $\beta_{\lambda'}=2/n-\beta_\lambda$   top--bottom symmetry

# Return law and gap

For the walk started at $e$, $$\Pr(X_k=e)=\frac1{n!}\sum_{\lambda\vdash n}
 d_\lambda^2\beta_\lambda^k.$$ Thus $n^{2k}\Pr(X_k=e)$ counts exactly the ordered-pair words returning to $e$. Conjugate partitions obey $\beta_{\lambda'}=2/n-\beta_\lambda$. The trivial, standard, and sign sectors yield respectively $1$, $1-2/n$, and $-1+2/n$; the spectral gap is $2/n$.

If $h_k$ is the density of the time-$k$ law relative to uniform measure, minus one, Plancherel gives the exact identity $$\|h_k\|_2^2=\sum_{\lambda\ne(n)}
 d_\lambda^2\beta_\lambda^{2k}.$$ Thus the same sector ledger owns the determinant, return probability, and $L^2$ convergence. The total-variation cutoff at $\tfrac12 n\log n$ is the classical theorem of Diaconis and Shahshahani [@DS81]; we do not claim it as new.

# Route-A boundary

The step law is inversion-invariant, hence $P_n$ is self-adjoint. It is a Markov contraction. On frozen $S_n$, every row has several positive successors, so $P_n$ is not induced by a single-valued deterministic map and is not a permutation Koopman operator. Consequently the displayed finite determinant is not an unweighted Artin--Mazur determinant on that phase space.

There is nevertheless a canonical product after changing the object. Give the directed support graph of $P_n$ edge weights $P_n(x,y)$. For primitive closed directed paths $[\gamma]$ modulo cyclic rotation, put $w(\gamma)=\prod_{e\in\gamma}P_n(e)$. The trace--log identity and grouping closed paths by primitive core give, as formal power series, $$\det(I-zP_n)^{-1}
 =\exp\!\left(\sum_{k\ge1}\frac{\operatorname{Tr}(P_n^k)}kz^k\right)
 =\prod_{[\gamma]\ \mathrm{primitive}}
  (1-w(\gamma)z^{|\gamma|})^{-1}.$$ This weighted path shift is a different phase space and dynamical owner; it is not a deterministic realization of the frozen chain on $S_n$. A1 remains FAIL because the frozen source has no primitive orbit carrying an A0 arithmetic payload, not because every enlarged primitive factorization is impossible. Prime and composite $n$ obey the same spectral theorem. An abstract unitary dilation exists for a contraction only after enlarging the Hilbert space; it neither changes this source clock nor manufactures deterministic source orbits. The strict verdict is $$(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},
 \mathrm{FAIL},\mathrm{FORMAL\ HINT}),$$ with Route B false and scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Exact evidence.

Regression evidence contains 193 partition sectors, 90 moment rows, and 163 collected determinant factors for $2\le n\le11$. An implementation-independent checker passes 2,597 assertions, including direct enumeration of all ordered-pair words for $n\le7$, $k\le6$, exact factor strings, and a weighted path-cycle control through degree eight for $n=2$. A separate symbolic path passes 2,427 checks; replay is byte exact; 58 hostile mutations are rejected. Finite rows do not prove the all-size theorem; the representation argument above does.

#### Revision-round focus.

Round 0 freezes the distinction between the Markov operator on $S_n$ and any deterministic orbit owner; it makes no absolute claim about enlarged path spaces.

#### Revision-round focus.

Round 1 adds the weighted path-space trace--log product and identifies the change of phase space as the exact reason it cannot be relabeled as the frozen owner.

#### Revision-round focus.

Round 2 locks the owner boundary into the evidence, Route-A record, exact checker, repaired-hash mutations, and release manifest, while preserving the failed A0 and A1 gates.

#### Limitations and nonclaims.

The paper does not derive the classical cutoff anew, identify rational primes with sectors, or compare the Markov polynomial with a target divisor, functional equation, counting law, or continuation. It neither identifies weighted path cycles with deterministic orbits on frozen $S_n$ nor denies cycle products after changing phase space. It proposes no Hilbert--Polya operator. The sole literature entry fixes classical ownership; this certificate is not a novelty survey or external review.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

Package-local exact evidence and deterministic code accompany this manuscript.

#### Ethics.

No human, animal, clinical, personal, or sensitive data are used; approval is not applicable.

#### Author contributions (CRediT).

This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing. AI systems are not authors.

#### Funding.

No external funding is reported.

#### Conflicts of interest.

None known.

#### AI-use disclosure.

An AI coding assistant supported drafting and exact-code development; it was not an external reviewer or independent error process.

1 P. Diaconis and M. Shahshahani, "Generating a random permutation with random transpositions," *Z. Wahrscheinlichkeitstheorie verw. Gebiete* 57 (1981), 159--179. DOI: 10.1007/BF00535487.
