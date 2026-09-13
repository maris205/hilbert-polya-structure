---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-306-sharp-annular-coefficient-envelope-saturation"
canonical_tex: "zeta_mvp0/papers/RH-306-sharp-annular-coefficient-envelope-saturation/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-306-sharp-annular-coefficient-envelope-saturation/main.pdf"
source_sha256: "69db20bcd00cb54340958f9cc1716421ad96cdeeba0228fc85662f58a458f1ae"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Sharp Saturation of the Annular Coefficient-Envelope Rate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-306-sharp-annular-coefficient-envelope-saturation>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-306-sharp-annular-coefficient-envelope-saturation/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-306-sharp-annular-coefficient-envelope-saturation/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-306-sharp-annular-coefficient-envelope-saturation/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-306-sharp-annular-coefficient-envelope-saturation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The mass-limited rate of RH-305 is optimal at the level of its coefficient information. We truncate the actual deterministic anchor sequence at order $N$ and set every later model coefficient to zero. The resulting sequence satisfies the same cap envelope with parameter $M_N=48q^2(q_*/q)^N$, while its annular mismatch is exactly the target tail. Both its $H^\infty$ and $H^2$ norms are of order $M_N^{-\kappa(\rho)}/\log M_N$. Thus neither the power nor logarithmic factor can be improved from the coefficient envelope alone. The truncated sequence is not asserted to be a power-sum sequence of any noisy spectral complement.
author:
- Bin Wang
date: July 2026
title: 'Sharp Saturation of the Annular Coefficient-Envelope Rate'
```

## Markdown 正文

# Truncated target family

Fix $0<\rho<\rho_*$ and put $r=q_*/q>1$, $y=q_*\rho<1$. For $N\ge2$ define $$\tau_n^{(N)}=
 \begin{cases}a_n,&2\le n\le N,\\0,&n>N,\end{cases}
 \qquad
 M_N=48q^2r^N.$$ The unified target envelope gives, for every $n\ge2$, $$|\tau_n^{(N)}|\le M_Nq^{n-2}.$$ The corresponding logarithmic mismatch is $$g_N(z)=-\sum_{n>N}\frac{a_n}{n}z^n.$$

# Information-class sharpness

[\[thm:sharp\]]{#thm:sharp label="thm:sharp"} For each fixed $0<\rho<\rho_*$ there are constants $0<c_\rho<C_\rho<\infty$ such that, for $X=H^\infty(\rho)$ and $H^2(\rho)$, $$c_\rho\frac{y^N}{N}
 \le\|g_N\|_X\le
 C_\rho\frac{y^N}{N}.$$ Equivalently, $$\|g_N\|_X
 =\Theta_\rho\left(
 \frac{M_N^{-\kappa(\rho)}}{\log M_N}
 \right),
 \qquad
 \kappa(\rho)=\frac{\log(1/y)}{\log r}.$$

The upper bounds follow from $|a_n|<48q_*^n$ and the geometric estimates $$\sum_{n>N}\frac{y^n}{n}=O_\rho(y^N/N),\qquad
 \left(\sum_{n>N}\frac{y^{2n}}{n^2}\right)^{1/2}
 =O_\rho(y^N/N).$$ For the lower bound, let $n_N$ be the first odd integer greater than $N$; then $n_N\le N+2$ and $$\frac{|a_{n_N}|\rho^{n_N}}{n_N}
 =\frac{y^{n_N}}
 {n_N(1+\lambda^{-n_N})}
 \ge c_\rho\frac{y^N}{N}.$$ This one coefficient bounds the $H^2$ norm. For $H^\infty$, take the odd projection $(g_N(z)-g_N(-z))/2$, whose norm is at most $\|g_N\|_\infty$; at positive radius all its odd target-tail terms have the same sign, so the same first term gives the lower bound. Finally $M_N=48q^2r^N$ converts $y^N/N$ to the displayed mass scale.

# Protocol and firewall

The computation records rigorous lower and geometric upper bounds for the infinite constant-$48$ model tails at $\rho=1.41$ and $N=20,40,80$; it does not truncate an infinite sum silently. The numerical model checks the rate only.

The family $\tau^{(N)}$ is a coefficient array satisfying the same envelope. No multiset in $|\mu|\le q$, no noisy operator, and no physical spectral power-sum realization is constructed. Therefore the theorem proves sharpness only for the coefficient-envelope information class, not for the actual noisy complement. Gates A--E remain false/open.
