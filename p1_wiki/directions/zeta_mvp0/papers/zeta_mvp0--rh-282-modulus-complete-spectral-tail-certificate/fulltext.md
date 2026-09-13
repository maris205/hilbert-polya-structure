---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-282-modulus-complete-spectral-tail-certificate"
canonical_tex: "zeta_mvp0/papers/RH-282-modulus-complete-spectral-tail-certificate/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-282-modulus-complete-spectral-tail-certificate/main.pdf"
source_sha256: "7f37a3adfc0495a65ecd3192651e5c07f13ed160a777f5c3fc38bcb331696b96"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Modulus-Complete Spectral-Tail Certificate for the Noisy Hardy Determinant

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-282-modulus-complete-spectral-tail-certificate>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-282-modulus-complete-spectral-tail-certificate/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-282-modulus-complete-spectral-tail-certificate/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-282-modulus-complete-spectral-tail-certificate/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-282-modulus-complete-spectral-tail-certificate/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The fixed-rank natural-$L^2$ quotient fails at zero noise, while the variable-rank criterion of RH-279 was previously uninstantiated. We activate its tail branch without constructing a Riesz projector. After removing the two peripheral eigenvalues of the Hardy-scaled folded Gaussian operator, take every algebraic eigenvalue of modulus greater than $q=1/2$ as the spectral head and put the remaining eigenvalues on a normal diagonal operator $C_\sigma$. The sharp Hilbert--Schmidt mass law bounds their squared sum by $\sigma^{-1}$ for small noise. With $R=7/5$ and $m_\sigma=\lceil4\log(1/\sigma)\rceil$, the trace norm, operator norm, prefix, and root-rate hypotheses of RH-279 hold, and the full logarithmic tail beyond $m_\sigma$ vanishes uniformly on $|z|\le R$. This proves a projection-free spectral-tail theorem. It does not identify the noisy head with the monodromy counterloop.
author:
- Bin Wang
date: July 2026
title: 'A Modulus-Complete Spectral-Tail Certificate for the Noisy Hardy Determinant'
```

## Markdown 正文

# Spectral realization

Let $A_\sigma=K_\sigma/r_H$, $r_H=0.85$, and remove the Perron and negative-parity eigenvalues from its algebraic spectrum. Denote the remaining sequence, counted with algebraic multiplicity, by $(\mu_j(\sigma))_{j\ge1}$. RH-276 and the Hilbert--Schmidt eigenvalue inequality give, for sufficiently small $\sigma$, $$\label{eq:mass}
 M_\sigma:=\sum_j|\mu_j(\sigma)|^2
 \le \|A_\sigma\|_{\mathcal S_2}^2\le\sigma^{-1}.$$ Fix $q=1/2$. The head $H_\sigma=\{\mu_j:|\mu_j|>q\}$ is finite. On the Hilbert space $\ell^2(\{j:|\mu_j|\le q\})$, define $$C_\sigma=\operatorname{diag}(\mu_j:|\mu_j|\le q).$$ The canonical-product factorization from RH-234 shows that $C_\sigma$ realizes exactly the complementary projection-free $\det_2$ factor.

# Variable-block theorem

[\[thm:certificate\]]{#thm:certificate label="thm:certificate"} For every integer $m\ge2$, $$\begin{aligned}
 \|C_\sigma^m\|_1&\le M_\sigma q^{m-2},&
 \|C_\sigma^m\|&\le q^m,\\
 \|C_\sigma^r\|&\le q^r\quad(0\le r<m),&
 |\operatorname{Tr}C_\sigma^n|&\le M_\sigma q^{n-2}\quad(n\ge2).\end{aligned}$$ Let $R=7/5$ and $m_\sigma=\lceil4\log(1/\sigma)\rceil$. Then $$\limsup_{\sigma\downarrow0}
 \|C_\sigma^{m_\sigma}\|_1^{1/m_\sigma}R
 \max\{1,qR\}
 \le \frac7{10}e^{1/4}<1.$$ Consequently $$\label{eq:tail}
 \sum_{n\ge m_\sigma}
 \frac{|\operatorname{Tr}C_\sigma^n|R^n}{n}\longrightarrow0.$$

The operator is normal and diagonal. Since $|\mu_j|\le q$ on the tail, $$\sum_j|\mu_j|^m\le q^{m-2}\sum_j|\mu_j|^2,$$ which gives every displayed norm and trace estimate. By [\[eq:mass\]](#eq:mass){reference-type="eqref" reference="eq:mass"}, $$\limsup (M_\sigma q^{-2})^{1/m_\sigma}\le e^{1/4}.$$ Because $qR=7/10$, the root-rate estimate follows. Finally, $$\sum_{n\ge m}\frac{|\operatorname{Tr}C_\sigma^n|R^n}{n}
 \le \frac{M_\sigma q^{-2}(qR)^m}{m(1-qR)}.$$ For the chosen clock the right side is $O(\sigma^{4\log(10/7)-1}/\log(1/\sigma))$, whose exponent is $0.426699\ldots>0$.

# Head rank and exact scope

The modulus-complete head obeys $\#H_\sigma\le M_\sigma/q^2\le4\sigma^{-1}$.

Every head eigenvalue contributes more than $q^2$ to the squared spectral mass in [\[eq:mass\]](#eq:mass){reference-type="eqref" reference="eq:mass"}.

$C_\sigma$ is a normal spectral realization of the canonical-product tail. It need not be similar to a bounded physical compression, and no estimate on the ill-conditioned Riesz projectors of RH-232 follows. The theorem supplies the variable-rank tail obligation, not the head-to-monodromy coefficient bridge. Gates A--E remain false/open; no Hilbert--Polya operator, Riemann-zero identification, zeta-divisor equality, or RH conclusion is asserted.
