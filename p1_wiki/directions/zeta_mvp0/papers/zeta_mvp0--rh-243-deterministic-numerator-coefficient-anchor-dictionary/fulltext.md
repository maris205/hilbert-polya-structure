---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-243-deterministic-numerator-coefficient-anchor-dictionary"
canonical_tex: "zeta_mvp0/papers/RH-243-deterministic-numerator-coefficient-anchor-dictionary/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-243-deterministic-numerator-coefficient-anchor-dictionary/main.pdf"
source_sha256: "bf4e977894bdaa28b8e3f816938257f558e5f8c3629573583b2ba7bc2944bddf"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Deterministic Numerator Coefficient-Anchor Dictionary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-243-deterministic-numerator-coefficient-anchor-dictionary>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-243-deterministic-numerator-coefficient-anchor-dictionary/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-243-deterministic-numerator-coefficient-anchor-dictionary/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-243-deterministic-numerator-coefficient-anchor-dictionary/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-243-deterministic-numerator-coefficient-anchor-dictionary/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-242 separates the all-order trace envelope from the deterministic numerator anchor but leaves the anchor coefficients unspecified. We now derive them from the exact deterministic factorization. Let $$\widehat D_{0,\mathrm{bulk},2}(z)
   =\frac{G(z)}{1-z^2/\lambda},
   \qquad
   \log G(z)=-\sum_{n\ge2}\frac{g_n}{n}z^n,$$ and let $P_n$ be the deterministic flat periodic trace. Then $$g_n=P_n-1-(-1)^n+2\mathbf{1}_{\{2\mid n\}}\lambda^{-n/2}.$$ After the current Hardy scaling $r_H=0.85$, the required one-step target is $a_n=r_H^{-n}g_n$.

  For the symmetric two-step numerator $H(w)=G(\sqrt w)G(-\sqrt w)$, the trace-style coefficient is exactly $b_k=a_{2k}$. Thus the two-step anchor sees every even one-step coefficient and loses every odd one exactly. Orders $2$--$12$ give a target unit-disk logarithmic norm $0.494505$. The smallest distance from the existing RH-222-selected residual jets to this target is $0.419190$, a finite diagnostic only. The present paper defines the independent target; it does not prove the noisy cloud coefficient bridge or the all-order envelope.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: 'A Deterministic Numerator Coefficient-Anchor Dictionary'
```

## Markdown 正文

# Which coefficient is being anchored?

Let $$\label{eq:centered}
 c_n=P_n-1-(-1)^n,
 \qquad n\ge2,$$ where $$P_n=\sum_{f^n(x)=x}\frac{1}{|1-(f^n)'(x)|}$$ is the deterministic flat periodic trace. Its parity-centered exponential decay is unconditional after RH-11 [@WangRH10; @WangRH11].

The deterministic one-step regularized bulk germ identified before the moving-cloud program is $$\label{eq:factor}
 \widehat D_{0,\mathrm{bulk},2}(z)
 =\exp\left[-\sum_{n\ge2}\frac{c_n}{n}z^n\right]
 =\frac{G(z)}{1-z^2/\lambda},
 \qquad \lambda=1.678573510428318\ldots .$$ The numerator $G$ is holomorphic and nonzero on the required disk [@WangRH46]. An anchor for the current cloud-extracted traces must use the logarithmic trace-style coefficients of $G$, not its ordinary Taylor coefficients. Those two coefficient systems are related nonlinearly by exponentiation.

# Exact one-step dictionary

[\[thm:one-step\]]{#thm:one-step label="thm:one-step"} Write $$\log G(z)=-\sum_{n\ge2}\frac{g_n}{n}z^n.$$ Then $$\label{eq:g}
 \boxed{
 g_n=c_n+2\mathbf{1}_{\{2\mid n\}}\lambda^{-n/2}.}$$ For the Hardy-scaled operator $A_\sigma=B_\sigma/r_H$, define $G_H(z)=G(z/r_H)$. Its trace-style coefficients are $$\label{eq:a}
 \boxed{
 a_n=r_H^{-n}
 \left[P_n-1-(-1)^n+2\mathbf{1}_{\{2\mid n\}}\lambda^{-n/2}\right].}$$

Taking logarithms in [\[eq:factor\]](#eq:factor){reference-type="eqref" reference="eq:factor"} gives $$\log G(z)
 =-\sum_{n\ge2}\frac{c_n}{n}z^n+\log(1-z^2/\lambda).$$ Since $$\log(1-z^2/\lambda)
 =-\sum_{k\ge1}\frac{z^{2k}}{k\lambda^k}
 =-\sum_{k\ge1}\frac{2\lambda^{-k}}{2k}z^{2k},$$ comparison with the trace-style logarithm proves [\[eq:g\]](#eq:g){reference-type="eqref" reference="eq:g"}. Substitution $z\mapsto z/r_H$ proves [\[eq:a\]](#eq:a){reference-type="eqref" reference="eq:a"}.

Equation [\[eq:a\]](#eq:a){reference-type="eqref" reference="eq:a"} is the independent coefficient target requested in RH-238 [@WangRH238]. It does not yet say that any positive-noise selected cloud leaves these coefficients behind.

# Two-step conversion and exact information loss

The earlier two-step numerator uses $w=z^2$: $$\label{eq:H}
 H(w)=G(\sqrt w)G(-\sqrt w).$$ After Hardy scaling, put $H_H(w)=H(w/r_H^2)$.

[\[thm:two-step\]]{#thm:two-step label="thm:two-step"} If $$\log H_H(w)=-\sum_{k\ge1}\frac{b_k}{k}w^k,$$ then $$\label{eq:b}
 \boxed{b_k=a_{2k}.}$$ No collection of coefficients of $H_H$ determines any odd coefficient $a_{2k+1}$ without an additional one-step input.

Add $\log G_H(z)$ and $\log G_H(-z)$. Odd powers cancel and the even part is $$-2\sum_{k\ge1}\frac{a_{2k}}{2k}z^{2k}
 =-\sum_{k\ge1}\frac{a_{2k}}{k}w^k,$$ which proves [\[eq:b\]](#eq:b){reference-type="eqref" reference="eq:b"}. For nonidentifiability, multiply any admissible $G_H(z)$ by $e^{\psi(z)}$, where $\psi$ is an odd holomorphic germ. The product at $z$ and $-z$ is unchanged, while the odd logarithmic coefficients change arbitrarily.

This corrects a possible ambiguity in the phrase "coefficient anchor to $H$.": $H$ is a complete two-step anchor, but only an even one-step anchor. The current order-$2$ through order-$12$ one-step trace jet also contains orders $3,5,7,9,11$, so it requires $G$ or equivalent odd data.

# Trace coefficients versus ordinary numerator coefficients

If $$G_H(z)=\sum_{m\ge0}h_mz^m,
 \qquad h_0=1,$$ then differentiating the exponential identity gives the exact recursion $$\label{eq:recursion}
 h_m=-\frac1m\sum_{k=1}^m a_k h_{m-k},
 \qquad a_1=0.$$ For example, $$h_2=-\frac{a_2}{2},\qquad
 h_3=-\frac{a_3}{3},\qquad
 h_4=-\frac{a_4}{4}+\frac{a_2^2}{8}.$$ Thus a power trace is a logarithmic coefficient, not an ordinary numerator Taylor coefficient. The archive stores both systems separately.

# Short-orbit target through order twelve

We evaluate [\[eq:a\]](#eq:a){reference-type="eqref" reference="eq:a"} from the exact finite periodic-point formulas in RH-11. The displayed decimals are floating evaluations of those formulas.

    $n$      $P_n$   unscaled $g_n$   Hardy-scaled $a_n$
  ----- ---------- ---------------- --------------------
      2   1.180143         0.371631             0.514368
      3   0.174533         0.174533             0.284198
      4   1.419878         0.129700             0.248465
      5   0.069803         0.069803             0.157318
      6   1.622141         0.045013             0.119351
      7   0.025942         0.025942             0.080923
      8   1.763873         0.015797             0.057971
      9   0.009364         0.009364             0.040428
     10   1.855508         0.005590             0.028391
     11   0.003344         0.003344             0.019980
     12   1.912575         0.001985             0.013954

The finite target norm is $$J_{12}(a)=\sum_{n=2}^{12}\frac{|a_n|}{n}=0.4945054357\ldots .$$ By contrast, the RH-236 residual norms measured relative to zero are small [@WangRH236]. Directly comparing all 32 stored residual jets with $a$ gives anchored distances between $0.419190$ and $0.514505$. This is already enough to show that "small relative to zero" and "close to the deterministic numerator" are different finite tests. It is not an asymptotic rejection of the cloud route: the ranks, candidate windows, and noise levels are all finite, and the stored roots are not interval certified.

The symmetric log-jet identity in Theorem [\[thm:two-step\]](#thm:two-step){reference-type="ref" reference="thm:two-step"} is reproduced to $3.5\times10^{-18}$ in the numerical audit. Ordinary numerator coefficients through degree twelve are generated by [\[eq:recursion\]](#eq:recursion){reference-type="eqref" reference="eq:recursion"}.

# Boundary and next test

RH-243 closes the target-definition ambiguity. The all-order uniform envelope remains a separate size theorem, and the actual coefficient bridge remains an identification theorem: one must prove that the selected noisy cloud removes the pole contribution and leaves the coefficients [\[eq:a\]](#eq:a){reference-type="eqref" reference="eq:a"}. Neither follows from the exact superloop identity of RH-242 [@WangRH242].

The next finite test is now forced rather than chosen: run the RH-238 shell-prefix selector against $a_n$, not zero. Failure would be a scoped obstruction for the frozen Arnoldi windows and prefix class; success would be only a finite anchored candidate. Gates A--E remain open. No Hilbert--Pólya operator, zeta-divisor identification, or Riemann-hypothesis conclusion is claimed.
