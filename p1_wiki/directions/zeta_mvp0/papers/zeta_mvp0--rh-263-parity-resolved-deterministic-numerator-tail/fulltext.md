---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-263-parity-resolved-deterministic-numerator-tail"
canonical_tex: "zeta_mvp0/papers/RH-263-parity-resolved-deterministic-numerator-tail/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-263-parity-resolved-deterministic-numerator-tail/main.pdf"
source_sha256: "fe3abd2558d05c01273a5567f3970a9dd44e795414c22983ef52882473c13b80"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Parity-Resolved Deterministic-Numerator Coefficients

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-263-parity-resolved-deterministic-numerator-tail>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-263-parity-resolved-deterministic-numerator-tail/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-263-parity-resolved-deterministic-numerator-tail/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-263-parity-resolved-deterministic-numerator-tail/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-263-parity-resolved-deterministic-numerator-tail/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The exact RH-15 endpoint factorization separates the deterministic numerator into an even reduced Fredholm factor and an odd endpoint factor. We use this separation to give an all-order coefficient dictionary for the Hardy-scaled target. Every odd coefficient is an explicit scalar, while every even coefficient is a reduced-sector trace plus two explicit endpoint corrections. The formula reproduces the 27 RH-253 entries through order 28 with maximum floating residual below $6.5\times10^{-14}$. This is an anchor identity for the deterministic target, not a coefficient bridge for the moving cloud.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'Parity-Resolved Deterministic-Numerator Coefficients'
```

## Markdown 正文

# Factorization and notation

Let $r_H=17/20$, $G_H(z)=G(z/r_H)$, and write $$\log G_H(z)=-\sum_{n\ge1}\frac{a_n}{n}z^n,\qquad a_1=0.$$ RH-15 gives [@WangRH15] $$G(u)=e^{P_1u}\det(I-u^2T)A_*(u^2)B(u^2)C(u).
 \label{eq:factor}$$ The logarithms are the branches normalized at zero. Put $b_n=\lambda^{-n}/(1+\lambda^{-n})$ and $d_n=\lambda^{-2n}/(1-\lambda^{-2n})$.

[\[thm:anchor\]]{#thm:anchor label="thm:anchor"} For every odd $n\ge3$, $$a_n=(r_H\lambda)^{-n}(1+\lambda^{-n})^{-1}.
 \label{eq:odd}$$ For every $k\ge1$, $$a_{2k}=r_H^{-2k}\left[
 2\operatorname{tr}(T^k)+\frac{2\lambda^{-2k}}{1+\lambda^{-k}}
 -\frac{\lambda^{-2k}}{1-\lambda^{-2k}}
 \right].
 \label{eq:even}$$

The odd logarithm is $P_1u+\log C(u)$. Since $P_1=b_1$, its linear term cancels, and the coefficient of $u^n$ for odd $n\ge3$ is $-b_n/n$. Comparison with $-\sum a_nz^n/n$ after $u=z/r_H$ proves [\[eq:odd\]](#eq:odd){reference-type="eqref" reference="eq:odd"}. For the even part, the coefficient of $u^{2k}$ in the logarithm of the Fredholm factor is $-\operatorname{tr}(T^k)/k$. The deflated endpoint factor has coefficient $(b_k-\lambda^{-k})/k=-\lambda^{-2k}/(k(1+\lambda^{-k}))$, and $B$ contributes $d_k/(2k)$. Multiplication by $-2k r_H^{-2k}$ gives [\[eq:even\]](#eq:even){reference-type="eqref" reference="eq:even"}.

For odd $n\ge3$, the coefficient is positive and obeys $$0<a_n<(r_H\lambda)^{-n}.$$ Thus odd target tails are controlled without a boundary supremum.

# Finite cross-check and its scope

The experiment reads the archived RH-253 physical traces and evaluates [\[eq:odd\]](#eq:odd){reference-type="eqref" reference="eq:odd"}--[\[eq:even\]](#eq:even){reference-type="eqref" reference="eq:even"}; it does not fit a new rate. The 27 rows (13 odd and 14 even) give a maximum absolute residual below $6.5\times10^{-14}$ in double precision. The RH-13 Arb certificate supplies the operator bounds needed for a separate all-order tail majorant [@WangRH13].

The identity does not say that noisy cloud-selected traces converge to these numbers. It also does not construct a selector, a self-adjoint operator, or a zeta divisor. In particular, the finite cross-check is not an all-order cloud fit. Gates A--E remain false/open.

# Route ledger

The target-tail and boundary-constant obligations are true after RH-262; the legal anchored head, cloud coefficient bridge, and uniform quotient tail are false/open. The next paper uses [\[eq:even\]](#eq:even){reference-type="eqref" reference="eq:even"} together with the RH-13 trace-ideal bounds to certify a direct order-29 tail, retaining the parity split rather than applying a coarse global boundary constant.
