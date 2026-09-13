---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-318-optimal-endpoint-spectral-mass-approximation"
canonical_tex: "zeta_mvp0/papers/RH-318-optimal-endpoint-spectral-mass-approximation/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-318-optimal-endpoint-spectral-mass-approximation/main.pdf"
source_sha256: "893deac112cf3ab2ea057af2428aff3e69e6e22ae98e985df52d6729fade19c4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Optimal Endpoint Hardy Error under a Spectral Mass Budget

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-318-optimal-endpoint-spectral-mass-approximation>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-318-optimal-endpoint-spectral-mass-approximation/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-318-optimal-endpoint-spectral-mass-approximation/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-318-optimal-endpoint-spectral-mass-approximation/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-318-optimal-endpoint-spectral-mass-approximation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We solve the endpoint approximation problem inside the genuine finite normal spectral class. If all eigenvalues lie in $|\mu|\le q$ and their squared mass is at most $M$, the least possible endpoint $H^2$ mismatch has squared norm asymptotic to $d/\log M$, where $d=\log(q_*/q)$. The lower bound uses the all-order deterministic coefficient law; the upper bound uses exact integer spectral prefixes. The theorem gives a sharp information-class constant but does not prove that the actual noisy family converges.
author:
- Bin Wang
date: July 2026
title: The Optimal Endpoint Hardy Error under a Spectral Mass Budget
```

## Markdown 正文

# Extremal spectral error

For a finite conjugate multiset $\mathcal S\subset\{|\mu|\le q\}$, put $$\tau_n(\mathcal S)=\sum_{\mu\in\mathcal S}\mu^n,
 \qquad M_2(\mathcal S)=\sum_{\mu\in\mathcal S}|\mu|^2.$$ Define $$E_{\rm spec}(M)=\inf_{M_2(\mathcal S)\le M}
 \left(\sum_{n\ge2}
 \frac{|\tau_n(\mathcal S)-a_n|^2\rho_*^{2n}}{n^2}
 \right)^{1/2}.$$ Let $s=q_*/q$ and $d=\log s$.

As $M\to\infty$, $$\boxed{E_{\rm spec}(M)^2\sim\frac{d}{\log M}.}$$

For every admissible spectrum, $|\tau_n|\le Mq^{n-2}$. Fix $\varepsilon>0$ and put $$n_M=\left\lceil\frac{(1+\varepsilon)\log M}{d}\right\rceil.$$ Uniformly for $n\ge n_M$, $$\frac{|\tau_n|}{q_*^n}
 \le q^{-2}Ms^{-n}\le q^{-2}M^{-\varepsilon}\longrightarrow0,$$ whereas RH-268 gives $a_n/q_*^n\to1$. Therefore $$E_{\rm spec}(M)^2
 \ge(1-o(1))\sum_{n\ge n_M}\frac1{n^2},$$ and hence $$\liminf_{M\to\infty}\log M\,E_{\rm spec}(M)^2
 \ge\frac d{1+\varepsilon}.$$ Letting $\varepsilon\downarrow0$ proves the lower bound.

Conversely, RH-316 gives a spectrum matching the first $N$ anchors exactly, and RH-317 bounds its mass by $Cs^N$. Its endpoint-scaled spectral tail satisfies $$\sum_{n>N}\frac{|\tau_n|^2\rho_*^{2n}}{n^2}
 \le C'\sum_{n>N}\frac{s^{2(N-n)}}{n^2}=O(N^{-2}),$$ whereas the target tail has squared norm $$\sum_{n>N}\frac{|a_n|^2\rho_*^{2n}}{n^2}
 =N^{-1}(1+o(1)).$$ Thus the mismatch squared norm is $N^{-1}(1+o(1))$. For a budget $M$, choose the largest $N$ with $Cs^N\le M$; then $N=(\log M)/d+O(1)$, proving the upper bound and the asymptotic.

Numerically, $$d=0.3377217782684642\ldots,
 \qquad \sqrt d=0.5811383469264992\ldots.$$

If the actual complement has squared mass $M_\sigma\le\sigma^{-1}$, then $$\liminf_{\sigma\downarrow0}
 \log(1/\sigma)\|g_\sigma\|_{H^2(\rho_*)}^2\ge d.$$

Repeat the lower-bound argument with $n_\sigma=\left\lceil
 (1+\varepsilon)\log(1/\sigma)/d\right\rceil$. The actual mass cap gives, uniformly for $n\ge n_\sigma$, $$\frac{|\tau_{\sigma,n}|}{q_*^n}
 \le q^{-2}\sigma^{-1}s^{-n}\le q^{-2}\sigma^\varepsilon\to0.$$ The same reciprocal-square tail yields $d/(1+\varepsilon)$, and then $\varepsilon\downarrow0$ gives the claim. This direct proof applies to the countable Hilbert--Schmidt complement spectrum as well as to finite spectra.

The lower bound tends to zero and is compatible with both convergence and nonconvergence. The constructive upper spectra are not identified with the actual noisy complement. Gates A--E remain false/open.
