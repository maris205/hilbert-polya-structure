---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-252-deterministic-numerator-analytic-tail-certificate"
canonical_tex: "zeta_mvp0/papers/RH-252-deterministic-numerator-analytic-tail-certificate/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-252-deterministic-numerator-analytic-tail-certificate/main.pdf"
source_sha256: "ce552f6072581dbdf94e552dc825be35b72763c876173bebe4c8e2b9da5c95a7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Deterministic-Numerator Analytic-Tail Certificate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-252-deterministic-numerator-analytic-tail-certificate>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-252-deterministic-numerator-analytic-tail-certificate/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-252-deterministic-numerator-analytic-tail-certificate/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-252-deterministic-numerator-analytic-tail-certificate/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-252-deterministic-numerator-analytic-tail-certificate/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-251 left the deterministic numerator tail as a separate obligation in the finite-head/analytic-tail interface. RH-46 supplies a stronger analytic input than the finite coefficient dictionary alone: the deterministic one-step numerator $G$ is holomorphic and nonzero on $|z|<\lambda$, where $\lambda=1.6785735104283177\ldots$. After Hardy scaling by $r_H=0.85$, the logarithm of $G(z/r_H)$ therefore has radius at least $\rho_*=r_H\lambda=1.42678748386407\ldots$. We prove an all-order Cauchy tail bound for the target coefficients and its exponential determinant conversion. The boundary supremum entering the bound is not numerically certified, so no cloud or quotient uniformity is claimed.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'Deterministic-Numerator Analytic-Tail Certificate'
```

## Markdown 正文

# Input and scope

Write the deterministic factor from RH-46 as $$\widehat D_{0,\mathrm{bulk},2}(z)=\frac{G(z)}{1-z^2/\lambda},
 \qquad G(0)=1,
 \label{eq:factor}$$ where $G$ is holomorphic and nonzero on $|z|<\lambda$ [@WangRH46]. RH-243 identifies the one-step Hardy-scaled trace-style target by $$\log G_H(z)=-\sum_{n\ge2}\frac{a_n}{n}z^n,
 \qquad G_H(z):=G(z/r_H),
 \qquad r_H=0.85.
 \label{eq:target}$$ The coefficients $a_n$ are deterministic target coefficients, not yet the coefficients of a selected noisy cloud [@WangRH243]. We set $a_1:=0$, so coefficient estimates below may be stated uniformly for $n\ge1$.

[\[prop:radius\]]{#prop:radius label="prop:radius"} The function $G_H$ is holomorphic and nonzero on $$|z|<\rho_*:=r_H\lambda=1.42678748386407\ldots>1.
 \label{eq:rho}$$ Consequently there is a unique holomorphic logarithm $L_H$ on this disk with $L_H(0)=0$, and $L_H=\log G_H$ in [\[eq:target\]](#eq:target){reference-type="eqref" reference="eq:target"}.

The substitution $z\mapsto z/r_H$ maps $|z|<r_H\lambda$ into $|z|<\lambda$. Holomorphicity and nonvanishing are preserved. The disk is simply connected and $G_H(0)=1$, so the normalized logarithm exists and is unique.

# The all-order tail theorem

For $0\le R<S<\rho_*$ define $$M_S:=\max_{|z|=S}|L_H(z)|,
 \qquad
 \Phi_N(R,S):=\frac{(R/S)^N}{1-R/S},
 \quad N\ge1.
 \label{eq:budget}$$ The first omitted order is $N$; thus the tail starts at $n=N$.

[\[thm:tail\]]{#thm:tail label="thm:tail"} For every $0\le R<S<\rho_*$ and every integer $N\ge1$, $$\frac{|a_n|}{n}\le M_S S^{-n}\quad(n\ge1),
 \qquad
 \sum_{n\ge N}\frac{|a_n|R^n}{n}
 \le M_S\Phi_N(R,S).
 \label{eq:tail}$$ In particular, since $\rho_*>1$, the all-order deterministic target tail on the unit disk exists for every $1<S<\rho_*$.

By Cauchy's coefficient estimate applied to the holomorphic function $L_H$ on $|z|<S$, the coefficient of $z^n$ in $L_H$ has modulus at most $M_SS^{-n}$. Equation [\[eq:target\]](#eq:target){reference-type="eqref" reference="eq:target"} says that this coefficient is $-a_n/n$. Multiplying by $R^n$ and summing the geometric series proves [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}.

[\[cor:exp\]]{#cor:exp label="cor:exp"} If $E_N(R,S):=M_S\Phi_N(R,S)$, then truncating the target logarithm after order $N-1$ incurs relative multiplicative error at most $$\left|\exp\!\left(-\sum_{n\ge N}a_nz^n/n\right)-1\right|
 \le e^{E_N(R,S)}-1,
 \qquad |z|\le R.
 \label{eq:exp-error}$$

Theorem [\[thm:tail\]](#thm:tail){reference-type="ref" reference="thm:tail"} bounds the modulus of the omitted logarithm by $E_N(R,S)$. The elementary inequality $|e^w-1|\le e^{|w|}-1$ gives the claim.

The theorem is an exact analytic interface, but $M_S$ is an unknown boundary constant. A finite evaluation of the order-$2$--$12$ polynomial cannot bound the full $L_H$ on the same circle. Thus the result is not a numerical uniform tail certificate for the moving cloud and does not invoke RH-240.

# Finite diagnostic

We read the archived RH-243 coefficients through order twelve and evaluate the truncated logarithm on $4096$ equally spaced points for $S\in\{1.05,1.15,1.25,1.35\}$. These values are diagnostics only; the exact quantity $M_S$ remains unbounded by the experiment. The geometric factor for the unit-disk tail beginning at order $13$ is shown below.

     $S$   truncated $\max|L_H|$   $\Phi_{13}(1,S)$            status
  ------ ----------------------- ------------------ -----------------
    1.05                0.579287          11.136748   diagnostic only
    1.15                0.797017           1.246048   diagnostic only
    1.25                1.106719           0.274878   diagnostic only
    1.35                1.559934           0.077970   diagnostic only

The last column is essential: multiplying the displayed truncated supremum by $\Phi_{13}$ is not a proof of the tail bound. It only illustrates the radius budget once a rigorous $M_S$ is supplied.

# Gate and route audit

The new exact statement closes the deterministic-target analytic-tail existence obligation on every strict subdisk of radius $\rho_*$. It does not identify the current noisy cloud with $a_n$, does not supply a uniform quotient block estimate, and does not produce a finite numerical value for $M_S$. Therefore Gates A--E remain false/open. No Hilbert--Polya operator, Riemann zero identification, zeta-divisor equality, or RH implication is claimed.

The next result should either interval-certify $M_S$ on a useful circle or provide a genuinely expanded resolved candidate window. Reweighting the frozen RH-248 shell class would not be a new input.
