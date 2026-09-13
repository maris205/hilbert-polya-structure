---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-259-extended-quotient-block-power-diagnostic"
canonical_tex: "zeta_mvp0/papers/RH-259-extended-quotient-block-power-diagnostic/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-259-extended-quotient-block-power-diagnostic/main.pdf"
source_sha256: "f711185619d870f7cbd2b6009b68a8f75979023ea3e58cd796285fd7c1e5bc08"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Extended Quotient Block-Power Diagnostic

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-259-extended-quotient-block-power-diagnostic>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-259-extended-quotient-block-power-diagnostic/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-259-extended-quotient-block-power-diagnostic/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-259-extended-quotient-block-power-diagnostic/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-259-extended-quotient-block-power-diagnostic/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-245/RH-246 establish the exact orthogonal-quotient identity and a conditional block-power trace envelope, but the archived diagnostic stopped at dimension 512. We extend dense ordered-Schur calculations to dimension 1024, covering 23 endpoints and six new cases. Every quotient twelfth power is contractive. However the worst finite block root rate deteriorates from $0.393300$ to $0.505642$, the first contractive depth grows from seven to nine, and the unit-disk logarithmic tail diagnostic worsens by more than an order of magnitude. The mechanism survives finitely; uniform small-noise control remains open.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'Extended Quotient Block-Power Diagnostic'
```

## Markdown 正文

# Exact quotient interface

Let $E$ be the selected invariant generalized root space, let $\Pi_E$ be its orthogonal projection, and put $Q=I-\Pi_E$. RH-245 proves that the compression $C=QAQ|_{E^\perp}$ realizes the quotient trace $$\tau_n=\operatorname{Tr}(C^n)
 \label{eq:quotient}$$ at every fixed finite operator [@WangRH245]. The projection has norm one, although $E^\perp$ need not reduce $A$.

RH-246 supplies the exact block theorem: if for one integer $m$ $$\|C^m\|\le\eta<1,
 \qquad \|C^m\|_1\le L_m,
 \qquad \|C^r\|\le K_r\quad(0\le r<m),
 \label{eq:block}$$ then all later traces have a geometric envelope with $q=\eta^{1/m}$ and an explicit logarithmic tail [@WangRH246]. The theorem is exact; only the uniform hypotheses are missing.

# Dimension-1024 protocol

For every archived endpoint of dimension at most 1024 we reconstruct the Hardy-scaled folded-Gaussian matrix, order its complex Schur form at the RH-222 radial cutoff, and split selected and quotient blocks. We then compute operator norms for powers one through twelve and the trace norm at power twelve. The extension contains 23 endpoints, six beyond the old cutoff.

The selected ranks match at all endpoints. The largest Schur trace-partition error is $3.99\times10^{-15}$; the largest discrepancy with archived quotient traces is $4.76\times10^{-9}$ at the new fine scales. These are floating diagnostics, not interval enclosures.

# Finite deterioration result

  quantity                            RH-246 cutoff        present cutoff
  --------------------------- --------------------- ---------------------
  maximum dimension                             512                  1024
  endpoints                                      17                    23
  first contractive depth                      3--7                  3--9
  contractive 12th powers                     17/17                 23/23
  worst $q_{12}$                           0.393300              0.505642
  maximum $\|C^{12}\|$          $1.37\times10^{-5}$   $2.79\times10^{-4}$
  unit-disk tail diagnostic     $1.80\times10^{-5}$   $5.65\times10^{-4}$

The worst new endpoint is the right channel at $\sigma=0.0025$, dimension 1024. The finite geometric constant is $M_{12}=551.5985$, while the rate worsens by a factor $1.28564$ relative to RH-246.

For each of the 23 audited quotient matrices, $\|C^{12}\|<1$. Hence the RH-246 block theorem gives an all-order trace bound for each individual finite matrix using its audited constants.

The maximum audited twelfth-power norm is $2.7932874477\times10^{-4}$. Substitute the finite matrix constants into [\[eq:block\]](#eq:block){reference-type="eqref" reference="eq:block"}.

Nine archived endpoints are still excluded by the dimension cutoff, and the worst constant deteriorates as the cutoff increases. The proposition is a family of 23 fixed-matrix statements, not a noise-uniform or continuum theorem.

# Route decision

The signed cancellation retained by the quotient remains the correct mechanism, but finite extension gives no basis for extrapolating uniformity. RH-260 must combine this finite quotient tail with the exact analytic target tail and the still-obstructed anchored head. Gates A--E remain false/open. No Hilbert--Polya operator, Riemann-zero identification, zeta-divisor equality, or RH implication is claimed.
