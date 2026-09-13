---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-309-endpoint-hardy-mismatch-barrier"
canonical_tex: "zeta_mvp0/papers/RH-309-endpoint-hardy-mismatch-barrier/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-309-endpoint-hardy-mismatch-barrier/main.pdf"
source_sha256: "4b0d0de86b3e978f23a27bf1376d7a99b3b103204cbed2decd876ba5739fc888"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Endpoint Hardy Membership and a Logarithmic Mismatch Barrier

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-309-endpoint-hardy-mismatch-barrier>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-309-endpoint-hardy-mismatch-barrier/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-309-endpoint-hardy-mismatch-barrier/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-309-endpoint-hardy-mismatch-barrier/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-309-endpoint-hardy-mismatch-barrier/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At the deterministic coefficient radius $\rho_*=1.4267874838\ldots$, the actual complement-to-anchor mismatch has a sharp qualitative split: it belongs to $H^2(\rho_*)$ for every fixed noise, but it never belongs to $H^\infty(\rho_*)$. Endpoint $H^2$ convergence would still close the weighted prefix at $R=1.4$, with conversion constant $4.992111\ldots$. However the exact odd anchors and the complement mass cap force an endpoint norm lower bound of order $1/\sqrt{\log M_\sigma}$, hence at least order $1/\sqrt{\log(1/\sigma)}$. This barrier tends to zero, so it does not prove endpoint convergence or nonconvergence.
author:
- Bin Wang
date: July 2026
title: Endpoint Hardy Membership and a Logarithmic Mismatch Barrier
```

## Markdown 正文

# Endpoint functions

Let $$\rho_*=q_*^{-1}=0.85\lambda,\qquad q=\frac12,\qquad
 g_\sigma(z)=\sum_{n\ge2}
 \frac{\tau_{\sigma,n}-a_n}{n}z^n.$$ For the modulus complement, $|\tau_{\sigma,n}|\le M_\sigma q^{n-2}$ with finite $M_\sigma\le\sigma^{-1}$. The deterministic anchors satisfy $|a_n|<48q_*^n$ and, for odd $n$, $$a_n=\frac{q_*^n}{1+\lambda^{-n}}.$$

# Membership theorem

[\[thm:membership\]]{#thm:membership label="thm:membership"} For every fixed $\sigma>0$, $$g_\sigma\in H^2(\rho_*),\qquad
 g_\sigma\notin H^\infty(\rho_*).$$

The noisy logarithm is bounded at $\rho_*$ because $q\rho_*=q/q_*<1$ and its coefficients have the geometric mass envelope. The target logarithm belongs to $H^2(\rho_*)$ because $$\sum_{n\ge2}\frac{|a_n|^2\rho_*^{2n}}{n^2}
 \le48^2\sum_{n\ge2}\frac1{n^2}<\infty.$$ Thus their difference belongs to $H^2$.

The odd part of the target logarithm has positive radial values $$\sum_{\substack{n\ge3\\n\ {\rm odd}}}
 \frac{r^n}{n(1+\lambda^{-n})},\qquad 0<r<1,$$ which diverge as $r\uparrow1$. Hence the target is not bounded on the endpoint disk. Subtracting the bounded noisy logarithm cannot make it bounded, proving the $H^\infty$ exclusion.

# Endpoint conversion and lower barrier

Put $R=1.4$ and $x=R/\rho_*$. Every endpoint $H^2$ mismatch satisfies $$\sum_{n\ge2}\frac{|\tau_{\sigma,n}-a_n|R^n}{n}
 \le\|g_\sigma\|_{H^2(\rho_*)}
 \frac{x^2}{\sqrt{1-x^2}},$$ where $$\frac{x^2}{\sqrt{1-x^2}}
 =4.992111068649647\ldots.$$

[\[thm:barrier\]]{#thm:barrier label="thm:barrier"} Let $M>0$ and let $N(M)$ be the least odd $N\ge3$ satisfying $$Mq^{N-2}\le\frac14q_*^N.$$ Then every modulus-capped complement of squared mass $M$ obeys $$\boxed{
 \|g\|_{H^2(\rho_*)}
 \ge\frac1{\sqrt{32N(M)}}.}$$ Consequently, for constants $C,M_0>0$, $$\|g\|_{H^2(\rho_*)}
 \ge\frac{C}{\sqrt{\log(e+M)}}
 \qquad(M\ge M_0).$$ For the actual complement mass $M_\sigma\le\sigma^{-1}$, $$\|g_\sigma\|_{H^2(\rho_*)}
 \ge\frac{C'}{\sqrt{\log(e+1/\sigma)}}.$$

For every odd $n\ge N(M)$, the cap remains below $q_*^n/4$. Since $a_n\ge q_*^n/2$, $$|\tau_n-a_n|\ge\frac14q_*^n.$$ After scaling by $\rho_*^n/n$, every such odd coefficient contributes at least $1/(4n)$ in modulus. Therefore $$\|g\|_{H^2(\rho_*)}^2
 \ge\frac1{16}
 \sum_{j\ge0}\frac1{(N+2j)^2}
 \ge\frac1{32N}.$$ The defining inequality gives $N(M)=\log M/\log(q_*/q)+O(1)$. Since $M\mapsto1/\sqrt{\log(e+M)}$ is decreasing, the archived upper cap $M_\sigma\le\sigma^{-1}$ gives the final statement; bounded masses only strengthen it.

# Protocol and exact boundary

The computation reports the exact forced odd cutoff and certified lower bound for $M=10^4,10^8,10^{16}$, together with a separately named normalized logarithmic scale. Infinite model $\sum_{n>N}n^{-2}$ tails are represented by rigorous integral bounds rather than a finite truncation.

The lower bound tends to zero. It rules out endpoint $H^2$ decay faster than the displayed logarithmic scale but proves neither endpoint convergence nor divergence. The endpoint $H^\infty$ route is unavailable because the actual mismatch is not in that space. Gates A--E remain false/open.
