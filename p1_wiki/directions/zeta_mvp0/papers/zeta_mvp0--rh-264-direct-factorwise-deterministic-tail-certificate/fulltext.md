---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-264-direct-factorwise-deterministic-tail-certificate"
canonical_tex: "zeta_mvp0/papers/RH-264-direct-factorwise-deterministic-tail-certificate/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-264-direct-factorwise-deterministic-tail-certificate/main.pdf"
source_sha256: "408864b3a14d554bc922c29ecb3bb45d6329dd0834581627a93b996e7ef01c63"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Direct Factorwise Deterministic-Numerator Tail Certificate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-264-direct-factorwise-deterministic-tail-certificate>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-264-direct-factorwise-deterministic-tail-certificate/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-264-direct-factorwise-deterministic-tail-certificate/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-264-direct-factorwise-deterministic-tail-certificate/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-264-direct-factorwise-deterministic-tail-certificate/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We derive a direct all-order target-tail bound from the parity-resolved factorization of RH-263. At the unit disk and first omitted order $29$, the Fredholm trace ideal, the two even endpoint factors, and the exact odd factor give a certified logarithmic budget below $2.6624745\times10^{-5}$. The relative exponential error is below $2.6625100\times10^{-5}$. The argument uses no angular sampling and does not assert a cloud coefficient bridge or a uniform quotient theorem.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'A Direct Factorwise Deterministic-Numerator Tail Certificate'
```

## Markdown 正文

# Tail decomposition

Let $u=z/r_H$, $r_H=17/20$, $W=|u|^2$, and $t=|u|/\lambda$. The RH-15 factorization is $$\log G(u)=P_1u+\log\det(I-u^2T)+\log A_*(u^2)+\log B(u^2)+\log C(u).$$ At $|z|=1$, put $W=(20/17)^2$ and $t=20/(17\lambda)$. The RH-13 certificate supplies a nuclear bound $\nu_1$ and bounds $p_1\ge\|T\|$, $p_2\ge\|T^2\|$, $q\ge\|T^3\|$ as in RH-262 [@WangRH13].

For $n=3k+j$, $j\in\{1,2,3\}$, the trace ideal gives $$\nu(T^n)\le q^k\nu_j,
 \qquad \nu_2=p_1\nu_1,\quad \nu_3=p_2\nu_1.$$ If $n\ge n_0$, then $$\sum_{n\ge n_0}\frac{|\operatorname{tr}T^n|W^n}{n}
 \le \sum_{j=1}^3
 \frac{\nu_jW^j(qW^3)^{k_j}}
 {(3k_j+j)(1-qW^3)},
 \label{eq:fredtail}$$ where $k_j$ is the first integer with $3k_j+j\ge n_0$.

For $n_0\ge1$ and $y=t^2<1$, $$\sum_{n\ge n_0}\frac{|[u^{2n}]\log A_*|W^n}{1}
 \le\frac{y^{n_0}}{n_0(1-y)},$$ and the corresponding $B$ bound is this quantity divided by $2(1-\lambda^{-2})$. For odd order $m\ge3$ the exact coefficient is $t^m/(1+\lambda^{-m})$ before the $1/m$ logarithmic normalization.

Use $|\lambda^{-2n}/(1+\lambda^{-n})|\le\lambda^{-2n}$ for $A_*$, $d_n\le\lambda^{-2n}/(1-\lambda^{-2})$ for $B$, and sum a geometric series after replacing each denominator by its first denominator. The odd statement is the exact RH-263 identity.

# Certified order-29 budget

The first omitted even trace power is $n_0=15$ and the first omitted odd order is $29$. The 100-, 150-, and 200-decimal Arb replays all satisfy the strict outward comparisons

  component                      certified upper bound
  ---------------------------- -----------------------
  Fredholm even tail                  $0.000019045786$
  $A_*$ tail                          $0.000003066234$
  $B$ tail                            $0.000002376597$
  even total                          $0.000024488616$
  odd endpoint tail                   $0.000002136130$
  total logarithmic tail              $0.000026624745$
  relative exponential error          $0.000026625100$

[\[thm:tail\]]{#thm:tail label="thm:tail"} For the deterministic Hardy-scaled numerator at $|z|\le1$, $$\sum_{n\ge29}\frac{|a_n|}{n}<0.000026624745,
 \qquad
 \exp\!\left(\sum_{n\ge29}\frac{|a_n|}{n}\right)-1
 <0.000026625100.$$

Orders $n\ge29$ split into even $n=2m$ with $m\ge15$ and odd orders. Apply [\[eq:fredtail\]](#eq:fredtail){reference-type="eqref" reference="eq:fredtail"} to the Fredholm logarithm, the proposition to $A_*$ and $B$, and the exact odd series to $C$ after the $P_1=b_1$ cancellation. The displayed outward endpoints sum to the stated bounds.

The result is deterministic and all-order in the sense of the analytic factorization; it is not an all-order theorem about noisy selected clouds. The five-component ledger remains $(0,0,0,1,1)$: no legal anchored head, cloud coefficient bridge, or uniform quotient tail has been supplied. Gates A--E remain false/open, and no Hilbert--Polya or zeta conclusion is made.
