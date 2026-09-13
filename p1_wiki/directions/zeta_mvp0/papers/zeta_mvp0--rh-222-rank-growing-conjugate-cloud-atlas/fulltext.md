---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-222-rank-growing-conjugate-cloud-atlas"
canonical_tex: "zeta_mvp0/papers/RH-222-rank-growing-conjugate-cloud-atlas/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-222-rank-growing-conjugate-cloud-atlas/main.pdf"
source_sha256: "e261db5e389eb0f830c8435d35b3e1140e4d20a347075b4b00c556ce87a7f0ea"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Rank-Growing Conjugate Resonance-Cloud Atlas Shell-Complete Divisors Across Sixteen Noise Scales

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-222-rank-growing-conjugate-cloud-atlas>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-222-rank-growing-conjugate-cloud-atlas/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-222-rank-growing-conjugate-cloud-atlas/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-222-rank-growing-conjugate-cloud-atlas/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-222-rank-growing-conjugate-cloud-atlas/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The quartet analysis RH-212--RH-221 ends with an exact obstruction: a fixed quartic, even if perfectly controlled, cannot provide a growing locally finite spectral divisor. We therefore construct the first rank-growing cloud on the same folded Gaussian operators.

  At sixteen frozen noise scales $$0.04,\;0.032,\ldots,\;0.00125,$$ the fine dimension satisfies $N_\sigma\sigma\simeq5.12$ and the second channel is its Haar compression. The Perron and negative parity resonances are removed, the remaining spectrum is scaled by the inherited Hardy radius $0.85$, and a deterministic Arnoldi window is partitioned into real singletons and nonreal conjugate pairs. A cloud is admitted only as a union of complete radial shells. The predeclared target ranks are $k_\ell=4+2\ell$.

  All 32 endpoint clouds are conjugate closed. Their actual ranks grow strictly from four to $34$--$35$ on both channels. Shell completion overshoots a target by at most one root; at most one nonreal root cut by the inner Arnoldi-window boundary is discarded. The minimum resolved gap after a selected cloud is $7.3991\times10^{-5}$ and the recorded conjugacy error is zero at binary64 precision.

  The construction is an operator-derived finite atlas, not an all-level spectral theorem. In particular the linear rank schedule is a frozen stress test rather than a canonical asymptotic law. No determinant limit, zeta identification, or Gate-A closure is asserted.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  A Rank-Growing Conjugate Resonance-Cloud Atlas\
  Shell-Complete Divisors Across Sixteen Noise Scales
```

## Markdown 正文

# From one quartet to a growing cloud

RH-219 proves that bounded degree remains bounded under locally uniform limits, while powers of one quartic grow only multiplicity on fixed support [@WangRH219]. RH-221 consequently designates a rank-growing physical divisor as the next Gate-A object [@WangRH221]. The necessary first task is deliberately finite: construct larger clouds without breaking the conjugation symmetry of a real operator.

The point is subtler than taking the first $k$ roots by modulus. A numerical window can end between the members of a conjugate pair, and a fixed cardinality prefix can cut a pair after an odd number of real roots has entered. Either event produces a polynomial with nonreal coefficients and therefore cannot represent a real spectral factor.

# Folded Gaussian endpoints

Let $f_u(x)=1-ux^2$ at the first band-merging parameter $u=1.543689012692\ldots$. On positive midpoint nodes $x_j=(j+1/2)/N$, the folded noisy transition matrix has row weights $$\label{eq:weights}
 W_{ij}=
 \exp\!\left[-\frac{(x_j-f_u(x_i))^2}{2\sigma^2}\right]
 +\exp\!\left[-\frac{(-x_j-f_u(x_i))^2}{2\sigma^2}\right],
 \qquad
 M_{\sigma,N}(i,j)=\frac{W_{ij}}{\sum_m W_{im}}.$$ Only entries within eight Gaussian standard deviations are retained, after which each row is renormalized. The default cutoff is below binary64 roundoff at the level of omitted Gaussian mass.

For every frozen $\sigma$, set $$N_\sigma=
 \max\!\left(32,\,
 2\,\operatorname{round}\frac{5.12}{2\sigma}\right).$$ The fine endpoint is $M_{\sigma,N_\sigma}$. If $E:\mathbb C^{N_\sigma/2}\to\mathbb C^{N_\sigma}$ is the pair-average Haar isometry, $$E_{2j,j}=E_{2j+1,j}=2^{-1/2},$$ the right endpoint is $E^*M_{\sigma,N_\sigma}E$. Both matrices are real.

The historical Hardy normalization uses $r_H=0.85$. Resolve a leading eigenvalue window, remove the root nearest $1$ and the most negative resolved real root, and divide every remaining value by $r_H$. These are the bulk resonances used below. Scaling does not affect conjugation or radial order.

# Conjugate shells

[\[lem:conj\]]{#lem:conj label="lem:conj"} The eigenvalue multiset of a real finite matrix is invariant under complex conjugation, including algebraic multiplicity.

Its characteristic polynomial has real coefficients. Hence $p(\overline z)=\overline{p(z)}$, and root multiplicities are preserved.

A *shell* is either a resolved real root $\{\lambda\}$ or a nonreal pair $\{\lambda,\overline\lambda\}$. Shells are ordered by decreasing outer modulus. Given target $k$, include whole shells until their cumulative cardinality first reaches $k$.

[\[prop:prefix\]]{#prop:prefix label="prop:prefix"} Every selected cloud is conjugate closed and is the zero multiset of a monic real polynomial. Its rank is either $k$ or $k+1$.

Each shell is conjugate closed. A union of shells is therefore conjugate closed, so its monic root polynomial has real coefficients by Lemma [\[lem:conj\]](#lem:conj){reference-type="ref" reference="lem:conj"}. Every shell has size one or two. Immediately before the last shell, cumulative size is below $k$; adding at most two roots gives rank at most $k+1$.

The proposition does not require simple eigenvalues. Repeated real roots can be represented by singleton copies, and a repeated nonreal root carries the same number of conjugate copies.

## Candidate-window boundary

Arnoldi is asked for $k+16$ eigenvalues before Perron/parity removal. Its returned inner boundary may itself cut a nonreal pair. Such an unmatched boundary root is discarded; no conjugate value is synthesized. Selection continues only if the remaining complete shells still reach the target. The archive records the discarded count. It is at most one in every endpoint.

This rule separates two claims:

1.  selected clouds are exactly conjugate closed within numerical tolerance;

2.  the finite Arnoldi window is not claimed to resolve the full infinite spectrum.

# Frozen rank ladder

The sixteen targets are $$\label{eq:ranks}
 k_\ell=4+2\ell,\qquad 0\le\ell\le15.$$ This schedule was fixed before inspecting the resulting lower shells. It forces a genuine degree increase while keeping a sixteen-root candidate margin. It is not derived from a Weyl law and is not promoted to a canonical rank/noise relation.

Representative endpoint data are:

     $\sigma$   target   left rank   right rank   left inner modulus   right inner modulus
  ----------- -------- ----------- ------------ -------------------- ---------------------
    $0.04000$        4           4            4            $0.35946$             $0.35347$
    $0.02500$        8           9            9            $0.19658$             $0.19027$
    $0.01000$       16          16           17            $0.13873$             $0.12899$
    $0.00500$       22          23           23            $0.13870$             $0.13553$
    $0.00250$       28          29           29            $0.07384$             $0.08025$
    $0.00125$       34          35           34            $0.08177$             $0.10716$

Actual ranks are strictly increasing in scale index on each channel. The frequent odd ranks are not defects: they indicate that one or more real bulk resonances lie before the closing conjugate shell.

# Radial isolation and global gauge

If $\Lambda$ is the selected cloud and $\Lambda^+$ is the first omitted complete shell, define $$g(\Lambda)=\min_{\lambda\in\Lambda}|\lambda|
 -\max_{\mu\in\Lambda^+}|\mu|.$$ All 32 resolved gaps are positive; the minimum is $7.3991\times10^{-5}$. This is a finite separation certificate inside the candidate window, not a lower bound uniform in $\sigma$.

For later work the archive also records one global affine gauge: $$\label{eq:gauge}
 m_\Lambda=\frac1{\operatorname{card}\Lambda}\sum_{\lambda\in\Lambda}\lambda,\qquad
 s_\Lambda^2=\frac1{\operatorname{card}\Lambda}
 \sum_{\lambda\in\Lambda}|\lambda-m_\Lambda|^2,
 \qquad q_\lambda=\frac{\lambda-m_\Lambda}{s_\Lambda}.$$ Conjugation makes $m_\Lambda$ real up to roundoff. The left/right center difference is at most $0.01610$ and the RMS-radius difference at most $0.01490$ in the frozen atlas. These are diagnostics, not convergence rates.

Reciprocal points $1/\lambda$ are stored at the same time. They will matter because Fredholm determinants have reciprocal resonance zeros; the present paper does not yet use that fact.

# Reproducibility controls

The eigensolver receives a deterministic trigonometric start vector. Every endpoint stores the full resolved candidate list, complete-shell count, selected roots, normalized roots, reciprocal roots, Perron/parity values, radial gap, global gauge, and a whole-matrix Frobenius ledger. Unit tests check:

1.  an artificial split pair is repaired by minimal shell completion;

2.  an unmatched inner-boundary root is discarded;

3.  global centering and RMS normalization satisfy their identities;

4.  reciprocal multiplication returns one.

The archived result contains 32 endpoint records and sixteen channel comparisons. It can therefore be reused without rerunning Arnoldi or changing the root-selection rule.

# Claim boundary and next question

A rank-growing cloud now exists at every frozen endpoint, so the fixed-degree wall has been passed at the finite numerical level. Three stronger statements remain open:

1.  certification of the infinite-spectrum ordering and gaps;

2.  a canonical relation between physical scale and selected rank;

3.  a locally uniform determinant or locally finite limiting divisor.

The immediate next layer tests whether the shell-complete selection is stable under candidate-window changes and quantifies how often a naive fixed-rank prefix violates conjugation. Gates A--E remain open. No self-adjoint operator, arithmetic trace formula, or Riemann-hypothesis consequence is claimed.
