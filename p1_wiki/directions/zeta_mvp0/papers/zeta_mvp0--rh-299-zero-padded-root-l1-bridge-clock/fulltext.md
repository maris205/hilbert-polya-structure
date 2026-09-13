---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-299-zero-padded-root-l1-bridge-clock"
canonical_tex: "zeta_mvp0/papers/RH-299-zero-padded-root-l1-bridge-clock/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-299-zero-padded-root-l1-bridge-clock/main.pdf"
source_sha256: "8e7faeffad5c7a46cc299b0fed7adc44bef70c82145aabd74af3ccbbedb90fbc"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Zero-Padded Root-$\ell^1$ Transport and Its Sharp Bridge Clock

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-299-zero-padded-root-l1-bridge-clock>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-299-zero-padded-root-l1-bridge-clock/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-299-zero-padded-root-l1-bridge-clock/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-299-zero-padded-root-l1-bridge-clock/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-299-zero-padded-root-l1-bridge-clock/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The noisy modulus head and the finite counterloop shell may have unequal cardinalities, so an equal-rank matching criterion is ill typed. We repair it by padding the smaller multiset with zeros, which does not change positive power moments. The optimal padded root-$\ell^1$ cost controls every moment by a Lipschitz power bound and hence controls the weighted head constituent. For a logarithmic bridge clock with $BR>1$, the resulting power-rate threshold is $\gamma>a\log(BR)$. A single radial pair proves that strictness is sharp: equality need not vanish. At the minimal bridge clock and the limiting monodromy radius the threshold is $0.6729348509\ldots$. The theorem is a sufficient interface; no actual matching for the noisy modulus head is proved.
author:
- Bin Wang
date: July 2026
title: 'Zero-Padded Root-$\ell^1$ Transport and Its Sharp Bridge Clock'
```

## Markdown 正文

# Padded matching

Let $X=\{x_1,\ldots,x_p\}$ and $Y=\{y_1,\ldots,y_q\}$ be finite multisets. Pad the smaller one with zeros until both have size $N=\max\{p,q\}$, and put $$d_1^0(X,Y)=\min_{\pi\in S_N}\sum_{j=1}^N|x_j-y_{\pi(j)}|.$$ Zero padding leaves $\sum x_j^n$ and $\sum y_j^n$ unchanged for every $n\ge1$.

[\[thm:transport\]]{#thm:transport label="thm:transport"} If $|x_j|,|y_j|\le B$, then for every $n\ge1$, $$\left|\sum_jx_j^n-\sum_jy_j^n\right|
 \le nB^{n-1}d_1^0(X,Y).$$ Consequently, for $m\ge3$, $$D_m(R):=\sum_{n=2}^{m-1}
 \frac{\left|\sum_jx_j^n-\sum_jy_j^n\right|R^n}{n}
 \le d_1^0(X,Y)R\sum_{j=1}^{m-2}(BR)^j.$$

Choose an optimal padded matching and use $$|x^n-y^n|\le nB^{n-1}|x-y|.$$ Sum over matched pairs, then over orders. The padding contributes zero to all moments.

# Sharp logarithmic rate

[\[thm:clock\]]{#thm:clock label="thm:clock"} Assume $BR>1$, $m_\sigma=\lceil a\log(1/\sigma)\rceil$, and $d_1^0(X_\sigma,Y_\sigma)=O(\sigma^\gamma)$. The transport bound tends to zero if $\gamma>a\log(BR)$. This exponent is sharp for the information class: with $X_\sigma=\{B\}$, $Y_\sigma=\{B-\sigma^\gamma\}$, the budget is $$\Theta\!\left(\sigma^\gamma(BR)^{m_\sigma}\right).$$ It is $\Theta(1)$ at equality and diverges below the threshold.

The geometric sum in Theorem [\[thm:transport\]](#thm:transport){reference-type="ref" reference="thm:transport"} is $\Theta((BR)^{m_\sigma})$. For the radial pair, $m_\sigma\sigma^\gamma\to0$, so uniformly through the moving window $$B^n-(B-\sigma^\gamma)^n
 =nB^{n-1}\sigma^\gamma\{1+o(1)\}.$$ Substitution gives the asserted asymptotic and all three regimes.

# Target thresholds and protocol

Let $a_*=1/\log(10/7)$ and $\beta=(0.85\sqrt\lambda)^{-1}=0.9080523604\ldots$. Then $$a_*\log(\beta R)=0.6729348509145321\ldots.$$ If only the global scaled cap $B=1/0.85$ is used, the threshold is $$a_*\log(R/0.85)=1.399008185460602\ldots.$$ The computation checks the finite matching inequality and radial saturation rows; it does not use archived noisy roots.

An actual root matching with the required decay rate is not known. The theorem supplies only the $D_\sigma$ constituent and cannot replace the full-trace constituent $E_\sigma$. Gates A--E remain false/open.
