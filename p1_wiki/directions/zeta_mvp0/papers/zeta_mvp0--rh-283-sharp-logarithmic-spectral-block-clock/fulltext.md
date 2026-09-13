---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-283-sharp-logarithmic-spectral-block-clock"
canonical_tex: "zeta_mvp0/papers/RH-283-sharp-logarithmic-spectral-block-clock/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-283-sharp-logarithmic-spectral-block-clock/main.pdf"
source_sha256: "47d92196fd36c458b4be1c16118832d06c156e311045d2c28e409840277eb93f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Sharp Logarithmic Block Clock for Hilbert--Schmidt Spectral Tails

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-283-sharp-logarithmic-spectral-block-clock>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-283-sharp-logarithmic-spectral-block-clock/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-283-sharp-logarithmic-spectral-block-clock/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-283-sharp-logarithmic-spectral-block-clock/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-283-sharp-logarithmic-spectral-block-clock/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the exact logarithmic clock forced by a Hilbert--Schmidt mass law. Let a normal diagonal spectral tail have eigenvalue moduli at most $q$ and squared mass $M_\sigma\le C\sigma^{-\alpha}$. On a disk of radius $R$ with $qR<1$, a clock $m_\sigma=\lceil a\log(1/\sigma)\rceil$ suppresses the high-order regularized-determinant tail when $a\log(1/(qR))\ge\alpha$. Equality gives only a logarithmic gain. Below that boundary a diagonal saturation family makes the tail diverge, so the threshold is sharp for this information class. The mass-and-cap root-rate upper bound is strictly below one under strict inequality, but a particular nonsaturating family may satisfy the RH-279 test at a smaller slope.
author:
- Bin Wang
date: July 2026
title: 'The Sharp Logarithmic Block Clock for Hilbert--Schmidt Spectral Tails'
```

## Markdown 正文

# Mass-and-cap class

Let $C_\sigma=\operatorname{diag}(\mu_j(\sigma))$ with $|\mu_j(\sigma)|\le q$ and $$M_\sigma=\sum_j|\mu_j(\sigma)|^2\le C\sigma^{-\alpha},
 \qquad \alpha>0.$$ For $qR<1$ and $m\ge2$, the same estimate as in RH-282 gives $$\label{eq:tail}
 T_\sigma(m,R):=
 \sum_{n\ge m}\frac{|\operatorname{Tr}C_\sigma^n|R^n}{n}
 \le\frac{Cq^{-2}\sigma^{-\alpha}(qR)^m}
 {m(1-qR)}.$$

# Sharp clock theorem

[\[thm:clock\]]{#thm:clock label="thm:clock"} Put $m_\sigma=\lceil a\log(1/\sigma)\rceil$. If $$a\log\frac1{qR}>\alpha,$$ then $T_\sigma(m_\sigma,R)$ decays by a positive power of $\sigma$. If equality holds, the right side of [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"} is $O(1/\log(1/\sigma))$ and still tends to zero.

If $a\log(1/(qR))<\alpha$, there exists a diagonal family satisfying the same mass and cap hypotheses for which $T_\sigma(m_\sigma,R)\to\infty$.

The upper assertions follow after writing $(qR)^{m_\sigma}=O(\sigma^{a\log(1/(qR))})$ in [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}. For sharpness take $N_\sigma=\lfloor c\sigma^{-\alpha}\rfloor$ copies of $q$, with $c>0$ small enough that $N_\sigma q^2\le C\sigma^{-\alpha}$. Then $$T_\sigma(m,R)=N_\sigma\sum_{n\ge m}\frac{(qR)^n}{n}.$$ The first term gives $T_\sigma\ge N_\sigma(qR)^m/m$, which diverges when the displayed strict reverse inequality holds.

For the saturation scale $M_\sigma\asymp\sigma^{-\alpha}$, $$\limsup_{\sigma\downarrow0}
 \|C_\sigma^{m_\sigma}\|_1^{1/m_\sigma}R
 \le qR e^{\alpha/a}.$$ The right-hand side is strictly smaller than one exactly when $a>\alpha/\log(1/(qR))$. Thus the mass-and-cap information uniformly guarantees the RH-279 root-rate test in the strict supercritical region. For the repeated-$q$ saturation family used above, the actual root-rate limit equals $qRe^{\alpha/a}$, so this boundary is exact for that family.

Use $\|C^m\|_1\le M_\sigma q^{m-2}$ and take $m$th roots. For $N_\sigma\asymp\sigma^{-\alpha}$ repeated entries equal to $q$, $\|C_\sigma^{m_\sigma}\|_1=N_\sigma q^{m_\sigma}$, which gives equality in the limiting root rate.

# Hardy-disk instance and boundary

For $\alpha=1$, $q=1/2$, and $R=7/5$, $$a_{\rm crit}=\frac1{\log(10/7)}=2.803673252\ldots .$$ The RH-282 choice $a=4$ has strict exponent $4\log(10/7)-1=0.426699775\ldots$.

The lower model proves sharpness only from mass and modulus information. It does not claim that the folded Gaussian spectrum has repeated roots at $q$. The spectral-to-monodromy bridge and Gates A--E remain open.
