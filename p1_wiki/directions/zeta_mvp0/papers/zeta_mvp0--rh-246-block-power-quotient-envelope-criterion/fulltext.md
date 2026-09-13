---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-246-block-power-quotient-envelope-criterion"
canonical_tex: "zeta_mvp0/papers/RH-246-block-power-quotient-envelope-criterion/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-246-block-power-quotient-envelope-criterion/main.pdf"
source_sha256: "63c04a1a64cd91bbc2ff480b0876cca2ca220e9b8ebfa0cc805f6ecc3ba5ce0f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Block-Power Quotient Envelope Criterion

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-246-block-power-quotient-envelope-criterion>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-246-block-power-quotient-envelope-criterion/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-246-block-power-quotient-envelope-criterion/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-246-block-power-quotient-envelope-criterion/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-246-block-power-quotient-envelope-criterion/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The orthogonal quotient of RH-245 has no one-step contraction, so a direct geometric estimate is unavailable. We prove the exact block-power substitute: a uniformly bounded trace norm and a uniformly contractive operator norm for one power $C^m$ imply a geometric envelope for all later quotient traces and an explicit logarithmic tail bound. A finite $m=12$ diagnostic on 17 tractable endpoints gives rate $0.393300$ and unit-disk tail bound $1.80\times10^{-5}$. The constants are not promoted to a noise-uniform certificate.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'Block-Power Quotient Envelope Criterion'
```

## Markdown 正文

# Block criterion

Let $C_\sigma\in\mathcal S_2(H)$ be the orthogonal quotient from RH-245 and $\tau_n(\sigma)=\operatorname{Tr}C_\sigma^n$ for $n\ge2$ [@WangRH245]. Fix an integer $m\ge2$. Suppose $$K_m=\sup_\sigma\|C_\sigma^m\|_1<\infty,
 \qquad
 \eta_m=\sup_\sigma\|C_\sigma^m\|<1,$$ and set $L_r=\sup_\sigma\|C_\sigma^r\|<\infty$ for $0\le r<m$ (with $L_0=1$).

[\[thm:block\]]{#thm:block label="thm:block"} For $n=\ell m+r\ge m$, $\ell\ge1$, $0\le r<m$, $$\label{eq:block-bound}
 |\tau_n(\sigma)|
 \le K_m L_r\eta_m^{\ell-1}.$$ Writing $q=\eta_m^{1/m}$, the right side is at most $M_mq^n$, where $$\label{eq:M}
 M_m=K_m\max_{0\le r<m}L_rq^{-(m+r)}.$$ If the finite head $2\le n<m$ has a uniform bound compatible with the same rate, then $|\tau_n(\sigma)|\le Mq^n$ for every $n\ge2$ and RH-240 applies.

Factor $C_\sigma^n=(C_\sigma^m)^\ell C_\sigma^r$ and use $|\operatorname{Tr}T|\le\|T\|_1$, submultiplicativity, and the ideal inequality $\|UV\|_1\le\|U\|_1\|V\|$. This gives [\[eq:block-bound\]](#eq:block-bound){reference-type="eqref" reference="eq:block-bound"}. Since $\eta_m^{\ell-1}=q^{n-(m+r)}$, [\[eq:M\]](#eq:M){reference-type="eqref" reference="eq:M"} follows. The finite head is handled by enlarging $M$ finitely; RH-240 then supplies local normality and zero-freeness of the relative determinant [@WangRH240].

The same factorization yields a useful tail estimate. For $R\ge0$ with $\eta_mR^m<1$, $$\label{eq:tail}
 \sum_{n\ge m}\frac{|\tau_n(\sigma)|R^n}{n}
 \le
 \frac{K_mR^m}{m(1-\eta_mR^m)}
 \sum_{r=0}^{m-1}L_rR^r.$$ This is a certificate template, not a claim that its hypotheses hold uniformly for the moving cloud.

# Finite 12-block diagnostic

We use the 17 ordered-Schur quotient rows of RH-245 (dimensions at most 512) and take maxima over this finite subbatch. The first contractive depth is 3--7, with no one-step contraction. For $m=12$, $$\eta_{12}\le1.3698766308677744\times10^{-5},\qquad
 K_{12}\le1.5684781027206807\times10^{-5},$$ so $$q_{12}=0.3932995547481413,
 \qquad
 \sum_{n\ge12}\frac{|\tau_n|}{n}
 \le1.7991531976413385\times10^{-5}$$ under the finite-sample constants and $R=1$. The corresponding finite remainder operator-norm maxima for orders $0$ through $11$ are retained in the JSON audit, and give $M_{12}=697.6520352674352$ through [\[eq:M\]](#eq:M){reference-type="eqref" reference="eq:M"}. The large $M$ is a reminder that a fast asymptotic block rate does not by itself make the first uncontrolled orders small.

  quantity                                           value
  -------------------------------- -----------------------
  finite endpoints                                      17
  first contractive depth                             3--7
  one-step contractive endpoints                      0/17
  $q_{12}$                                    0.3932995547
  $M_{12}$                                     697.6520353
  unit-disk tail from order 12       $1.7992\times10^{-5}$

# Boundary

The theorem is an exact conditional route to the all-order envelope. The finite diagnostic does not establish uniform $K_m$, $\eta_m$, or $L_r$ over all 32 endpoints, interval perturbations, or a continuum of noise. It also does not identify a cloud whose residual has the RH-243 deterministic anchor. The separate-absolute route is tested next; it is expected to fail because it discards the cancellation that makes the quotient small.

Gate A remains open and Gates B--E are untouched. No Hilbert--Pólya operator, zeta-divisor equality, Riemann-zero identification, or RH implication is claimed.
