---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-244-anchored-shell-prefix-availability-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-244-anchored-shell-prefix-availability-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-244-anchored-shell-prefix-availability-obstruction/main.pdf"
source_sha256: "690b2a29e32f8b06af520191b5a6938a57783381d1789a42cff0891cff8a0fd9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Anchored Shell-Prefix Availability Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-244-anchored-shell-prefix-availability-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-244-anchored-shell-prefix-availability-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-244-anchored-shell-prefix-availability-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-244-anchored-shell-prefix-availability-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-244-anchored-shell-prefix-availability-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The shell-prefix selector of RH-238 makes a finite cloud-extracted trace jet small relative to zero. The deterministic numerator dictionary of RH-243 instead prescribes a nonzero coefficient anchor. We first prove that the two equal-tolerance jet balls are disjoint throughout the archived noise range. We then scan every shell-complete prefix in the frozen RH-222 candidate windows against the anchor: none of 543 prefixes passes at any of 32 endpoints. This is a finite obstruction for one candidate class and one tolerance rule, not a nonexistence theorem for alternative clouds.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'Anchored Shell-Prefix Availability Obstruction'
```

## Markdown 正文

# Two selection problems

For jets $x=(x_2,\ldots,x_N)$ and $y=(y_2,\ldots,y_N)$ define $$d_N(x,y)=\sum_{n=2}^{N}\frac{|x_n-y_n|}{n},
 \qquad \mathcal J_N(x)=d_N(x,0).$$ This is the radius-one logarithmic jet metric used in RH-237 and RH-238 [@WangRH238]. Let $a=(a_2,\ldots,a_{12})$ be the Hardy-scaled deterministic numerator anchor of RH-243 [@WangRH243]. Its norm is $$\label{eq:anchor-norm}
 \mathcal J_{12}(a)=0.49450543569144195.$$

The RH-238 condition is $\mathcal J_{12}(\tau)\le\varepsilon_\sigma$. The anchored condition required for coefficient identification is instead $d_{12}(\tau,a)\le\varepsilon_\sigma$. The following elementary separation is decisive before any candidate scan.

[\[thm:balls\]]{#thm:balls label="thm:balls"} For every normed jet space and every nonzero anchor $a$, the closed balls $B(0,\varepsilon)$ and $B(a,\varepsilon)$ are disjoint if $\|a\|>2\varepsilon$. More quantitatively, if $\|x\|\le\varepsilon$, then $$\|x-a\|\ge \|a\|-\varepsilon.$$

The reverse triangle inequality gives $\|x-a\|\ge|\|a\|-\|x\||\ge\|a\|-\varepsilon$. If $x$ belonged to both equal-radius balls, the ordinary triangle inequality would give $\|a\|\le2\varepsilon$, a contradiction.

[\[cor:archive\]]{#cor:archive label="cor:archive"} For $\varepsilon_\sigma=\sigma$ and every archived $0.00125\le\sigma\le0.04$, a jet satisfying the RH-238 zero-target condition cannot satisfy the RH-243 anchored condition at the same tolerance. The smallest strict separation margin $\mathcal J_{12}(a)-2\sigma$ is $0.41450543569144194$.

Thus the earlier 32/32 zero-target success is not evidence for anchored availability. This conclusion is exact for the displayed finite metric and does not depend on floating root locations.

# Frozen prefix scan

We next ask the different question whether some other prefix in the same finite candidate class meets the anchor. At each noise/side endpoint let $A_\sigma$ be the archived scaled matrix, $p_\sigma$ and $e_\sigma$ its Perron and parity roots, and $$S_{\sigma,1},\ldots,S_{\sigma,m_\sigma}$$ the conjugation-complete shells obtained from the ordered RH-222 candidate window [@WangRH222]. For prefix $k$ put $$\tau_n^{(k)}
 =\operatorname{tr}A_\sigma^n-p_\sigma^n-e_\sigma^n
  -\sum_{s\in S_{\sigma,1}\cup\cdots\cup S_{\sigma,k}}s^n,
 \qquad 2\le n\le12.$$ We retain RH-238's minimum rank four and scan every eligible prefix, but now test $$\label{eq:test}
 d_{12}(\tau^{(k)},a)\le\sigma.$$ The full traces come from RH-236 [@WangRH236]; the anchor is read from the independent RH-243 archive.

[\[prop:scan\]]{#prop:scan label="prop:scan"} Across the 32 frozen endpoints, all 543 eligible shell-complete prefixes fail [\[eq:test\]](#eq:test){reference-type="eqref" reference="eq:test"}. Endpointwise best distances range from $0.39723767197524446$ to $0.48457639371229216$. Their ranks range from 4 to 18. The minimum and maximum ratios of best distance to tolerance are $10.479757156015458$ and $343.82932788167034$.

The accompanying deterministic audit reconstructs the conjugate shells, forms every eligible cumulative prefix, evaluates the exact finite spectral power sums, and applies the displayed weighted metric. The archived JSON records every endpointwise optimum and count. Unit tests independently check the trace subtraction, metric, target-ball theorem, and aggregate failure ledger.

  quantity                                    archived value
  --------------------------------- ------------------------
  endpoints                                               32
  eligible prefixes                                      543
  anchored passes                                          0
  best-distance range                 $0.397238$--$0.484576$
  best-rank range                                      4--18
  minimum best-distance/tolerance                $10.479757$

# Scope and route consequence

Proposition [\[prop:scan\]](#prop:scan){reference-type="ref" reference="prop:scan"} is exhaustive only inside the frozen RH-222 candidate windows, their radial shell ordering, the shell-complete prefix class, orders 2--12, radius one, minimum rank four, and the rule $\varepsilon_\sigma=\sigma$. The Arnoldi roots are floating approximations, not interval enclosures. The result does not exclude non-prefix subsets, weighted cancellations, expanded candidate windows, different tolerances, or a continuum small-noise selector. It therefore cannot be promoted to an asymptotic cloud nonexistence theorem.

The useful route consequence is narrower: zero-target compression and deterministic numerator identification must remain separate obligations. A new anchored selector is needed. Independently, the all-order envelope should be pursued through cancellation-preserving loop grouping rather than absolute physical and atomic sectors. Gate A remains open, and Gates B--E are untouched. No Hilbert--Pólya operator, zeta-divisor identification, Riemann-zero identification, or Riemann-hypothesis implication is claimed.
