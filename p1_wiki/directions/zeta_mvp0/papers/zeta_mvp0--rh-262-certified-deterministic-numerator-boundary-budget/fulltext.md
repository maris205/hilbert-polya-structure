---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-262-certified-deterministic-numerator-boundary-budget"
canonical_tex: "zeta_mvp0/papers/RH-262-certified-deterministic-numerator-boundary-budget/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-262-certified-deterministic-numerator-boundary-budget/main.pdf"
source_sha256: "f81c7882eac5d22b1deb6e13cd08ebe4ba89600dfce34280d8507934dd28b331"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Certified Deterministic-Numerator Boundary Budget

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-262-certified-deterministic-numerator-boundary-budget>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-262-certified-deterministic-numerator-boundary-budget/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-262-certified-deterministic-numerator-boundary-budget/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-262-certified-deterministic-numerator-boundary-budget/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-262-certified-deterministic-numerator-boundary-budget/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We turn the all-order Cauchy interface of RH-252 into a usable numerical certificate. The exact RH-15 factorization and the RH-13 Arb bounds imply, without angular sampling, that the normalized Hardy-scaled deterministic numerator satisfies $M_{7/5}<108$. The order-28 anchor of RH-253 then gives an order-29 unit-disk logarithmic tail below $0.021866475$ and relative multiplicative error below $0.022107298$. This certifies only the target boundary constant. It supplies neither a legal cloud head, a cloud-to-target coefficient bridge, nor a uniform quotient tail.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'A Certified Deterministic-Numerator Boundary Budget'
```

## Markdown 正文

# Factorization and nuclear input

Let $G$ be the one-step deterministic numerator and let $G_H(z)=G(z/r_H)$ with $r_H=17/20$. RH-15 proves the exact factorization [@WangRH15] $$G(u)=e^{P_1u}\widetilde D_{1,+}(u^2)A_*(u^2)B(u^2)C(u),
 \qquad \widetilde D_{1,+}(w)=\det(I-wT).
 \label{eq:factor}$$ The logarithms below are the branches normalized to vanish at the origin. RH-13 realizes $T$ on a Wiener algebra of radius $R=0.7$ and certifies its finite section and tail with Arb arithmetic [@WangRH13].

For $k\ge1$, the nonzero reduced columns have the form $$C_{2k}=2a(x)\left(t(x)^k/R^{2k}-m_{2k}\right),
 \qquad
 m_{2k}=\binom{2k}{k}\left(\frac{r}{2R}\right)^{2k}.$$ If $\tau=\|t\|_R/R^2<1$, summing the column norms gives the nuclear bound $$\nu_1:=\nu(T)\le2\|a\|_R\left\{
 \frac{\tau}{1-\tau}
 +\frac1{\sqrt{1-(r/R)^2}}-1\right\}.
 \label{eq:nuclear}$$ Indeed, the first term sums $\tau^k$, while the second follows from $\sum_{k\ge0}\binom{2k}{k}x^k=(1-4x)^{-1/2}$.

Let $M$ be the RH-13 finite section and let $\varepsilon$ bound the operator remainder. Then $$p_1=\|M\|+\varepsilon\ge\|T\|,
 \qquad
 p_2=\|M^2\|+2\|M\|\varepsilon+\varepsilon^2\ge\|T^2\|.
 \label{eq:p12}$$ Thus $\nu(T^2)\le p_1\nu_1$ and $\nu(T^3)\le p_2\nu_1$ by the nuclear-ideal inequality.

# A uniform boundary theorem

Put $S=7/5$, $U=S/r_H=28/17$, $W=U^2$, and $t=U/\lambda$. The choice is strict: $U<\lambda$. Write $q\ge\|T^3\|$ for the RH-13 certified cube bound.

[\[thm:fredholm\]]{#thm:fredholm label="thm:fredholm"} If $qW^3<1$, then throughout $|w|=W$, $$|\log\det(I-wT)|
 \le
 \frac{\nu_1W+(p_1\nu_1)W^2/2+(p_2\nu_1)W^3/3}
 {1-qW^3}.
 \label{eq:fredholm}$$

For $j=1,2,3$ and $k\ge0$, the nuclear-ideal inequality gives $\nu(T^{3k+j})\le q^k\nu(T^j)$. Combine this with $|\operatorname{tr}T^n|\le\nu(T^n)$ in the Fredholm logarithm, group the series modulo three, and replace $3k+j$ in the denominator by $j$. The remaining series is geometric with ratio $qW^3$.

The endpoint factors also admit exact scalar bounds. With $b_n=\lambda^{-n}/(1+\lambda^{-n})$ and $d_n=\lambda^{-2n}/(1-\lambda^{-2n})$, coefficientwise absolute majorants give $$\begin{aligned}
 |\log A_*(u^2)|&\le-\log(1-t^2),\label{eq:A}\\
 |\log B(u^2)|&\le
 \frac{-\log(1-t^2)}{2(1-\lambda^{-2})}.\label{eq:B}\end{aligned}$$ The identity $P_1=b_1$ cancels the linear term of $\log C$, so $$|P_1u+\log C(u)|\le\operatorname{artanh}(t)-t.
 \label{eq:C}$$

[\[thm:budget\]]{#thm:budget label="thm:budget"} For the normalized logarithm of $G_H$, $$\boxed{M_{7/5}:=\sup_{|z|=7/5}|\log G_H(z)|<107.906078<108.}$$

The 200-decimal-place Arb replay of the RH-13 certificate gives

  --------------- ---------------- ----------------- ----------------
  $\nu_1$           $<4.623248864$ $p_1$               $<0.633964866$
  $p_2$             $<0.174350001$ $qW^3$              $<0.715126024$
  Fredholm term      $<100.715071$ $A_*$ term             $<3.291531$
  $B$ term             $<2.551222$ linear+$C$ term        $<1.348256$
  --------------- ---------------- ----------------- ----------------

All entries are outward endpoints, and every displayed strict comparison is checked again at 100 and 150 decimal places. Summing [\[eq:fredholm\]](#eq:fredholm){reference-type="eqref" reference="eq:fredholm"}--[\[eq:C\]](#eq:C){reference-type="eqref" reference="eq:C"} proves the claim. This is a uniform factor majorant on the entire circle, not a sampled maximum.

# Order-29 consequence and boundary

RH-252 proves that Cauchy's estimate converts $M_S$ into an all-order target tail [@WangRH252]; RH-253 supplies deterministic coefficients through order 28 [@WangRH253]. Hence the first omitted order is $N=29$.

On $|z|\le1$, $$\sum_{n\ge29}\frac{|a_n|}{n}
 \le M_{7/5}\frac{(5/7)^{29}}{1-5/7}
 <0.021866475.$$ The corresponding relative multiplicative error is below $e^{0.021866475}-1<0.022107298$.

The protocol reruns the RH-13 Arb certificate at 100, 150, and 200 decimal places, evaluates only interval expressions, checks twelve outward decimal claims, and archives source hashes. It deliberately does not use the mislabelled $\lambda^2$ radius field in an older RH-46 JSON: the one-step zero-free radius used here is $\lambda$.

In the five-component RH-260 ledger [@WangRH260], the status changes from $(0,0,0,1,0)$ to $(0,0,0,1,1)$. The legal anchored head, current-cloud coefficient bridge, and uniform quotient tail remain open, so the complete certificate count is zero. A finite order-28 anchor is not promoted to an all-order identification. Gates A--E remain false/open. No Hilbert--Polya operator, Riemann-zero identification, completed-zeta divisor equality, or implication of RH is asserted.
