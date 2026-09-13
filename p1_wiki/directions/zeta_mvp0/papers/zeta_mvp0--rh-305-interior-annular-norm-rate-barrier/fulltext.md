---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-305-interior-annular-norm-rate-barrier"
canonical_tex: "zeta_mvp0/papers/RH-305-interior-annular-norm-rate-barrier/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-305-interior-annular-norm-rate-barrier/main.pdf"
source_sha256: "2675c4ba5210087e1ce1d003f3825c2f7154fde5172e80bd24581a59877c3487"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Mass-Limited Rate Barrier for Interior Annular Norms

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-305-interior-annular-norm-rate-barrier>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-305-interior-annular-norm-rate-barrier/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-305-interior-annular-norm-rate-barrier/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-305-interior-annular-norm-rate-barrier/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-305-interior-annular-norm-rate-barrier/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We turn the odd-anchor mass demand into an unconditional norm lower bound for every modulus-capped complement. Given squared spectral mass $M$, choose the first odd order at which the cap $Mq^{n-2}$ falls below half of the exact deterministic anchor. That coefficient alone forces both the $H^\infty(\rho)$ and $H^2(\rho)$ mismatch norms to be at least $C_\rho M^{-\kappa(\rho)}/\log M$, where $\kappa(\rho)=\log(1/(q_*\rho))/\log(q_*/q)$. Under $M_\sigma\le\sigma^{-1}$, no interior annular norm can decay with a power of $\sigma$ strictly larger than $\kappa(\rho)$. The lower bound tends to zero and therefore does not exclude actual annular convergence.
author:
- Bin Wang
date: July 2026
title: 'A Mass-Limited Rate Barrier for Interior Annular Norms'
```

## Markdown 正文

# Mass-dependent odd witness

Fix $R<\rho<\rho_*=q_*^{-1}$ and let $$g(z)=\sum_{n\ge2}\frac{\tau_n-a_n}{n}z^n,
 \qquad
 \tau_n=\sum_j\mu_j^n,\quad |\mu_j|\le q,\quad
 M=\sum_j|\mu_j|^2.$$ For odd $n$, $a_n=q_*^n/(1+\lambda^{-n})$. Let $N(M)$ be the least odd $n\ge3$ such that $$Mq^{n-2}\le\frac12a_n.$$ The logarithmic implementation uses this exact inequality and does not replace it by an asymptotic proxy.

# Strict and asymptotic lower bounds

[\[thm:lower\]]{#thm:lower label="thm:lower"} For $X=H^\infty(\rho)$ or $H^2(\rho)$, $$\|g\|_X\ge
 \frac{(q_*\rho)^{N(M)}}
 {2N(M)(1+\lambda^{-N(M)})}.$$ Moreover, there are constants $C_\rho>0$ and $M_{0,\rho}$ such that for $M\ge M_{0,\rho}$, $$\boxed{
 \|g\|_X\ge
 C_\rho\frac{M^{-\kappa(\rho)}}{\log(e+M)},
 \qquad
 \kappa(\rho)=
 \frac{\log(1/(q_*\rho))}{\log(q_*/q)}.}$$

At $N=N(M)$, the spectral cap gives $|\tau_N|\le Mq^{N-2}\le a_N/2$, hence $|\tau_N-a_N|\ge a_N/2$. A single coefficient of either annular norm gives the first display.

Put $r=q_*/q>1$ and $y=q_*\rho<1$. The defining inequality for $N$ and its failure two orders earlier imply $$N(M)=\frac{\log M}{\log r}+O(1).$$ Therefore $y^{N(M)}=\Theta_\rho(M^{\log y/\log r})
=\Theta_\rho(M^{-\kappa(\rho)})$, while $N(M)=\Theta(\log M)$. Absorb the bounded factors into $C_\rho$.

[\[cor:noise\]]{#cor:noise label="cor:noise"} For the actual modulus complement, $M_\sigma\le\sigma^{-1}$. Hence, after adjusting a constant for bounded masses, $$\|g_\sigma\|_X\ge
 C_\rho\frac{\sigma^{\kappa(\rho)}}
 {\log(e+1/\sigma)}.$$ In particular $\|g_\sigma\|_X=O(\sigma^\beta)$ is impossible for every $\beta>\kappa(\rho)$.

The function $M^{-\kappa}/\log(e+M)$ is eventually decreasing. Apply Theorem [\[thm:lower\]](#thm:lower){reference-type="ref" reference="thm:lower"} with $M_\sigma\le\sigma^{-1}$. If $M_\sigma$ stays bounded along a subsequence, the exact witness bound is bounded below by a positive constant and the conclusion is stronger.

# Numerical protocol and boundary

At $\rho=1.41$, $$\kappa(1.41)=0.035045705260961\ldots.$$ The computation uses the exact least odd witness at $M=10^{12}$ for $\rho=1.405,1.41,1.42$ and records the certified coefficient lower bounds. It does not treat the asymptotic expression as a unit-constant global bound.

The theorem rules out overly fast convergence, not convergence itself. It uses only the actual modulus cap, squared spectral mass, and exact odd anchors; it does not identify the head or close any determinant gate. Gates A--E remain false/open.
