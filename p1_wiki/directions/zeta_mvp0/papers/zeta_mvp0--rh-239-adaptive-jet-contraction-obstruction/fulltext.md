---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-239-adaptive-jet-contraction-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-239-adaptive-jet-contraction-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-239-adaptive-jet-contraction-obstruction/main.pdf"
source_sha256: "9cd745e87e9afe169590f47815b6676ff0dc3efd5b8c7cb9bd32d98f852305f4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Jet Contraction and the All-Order Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-239-adaptive-jet-contraction-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-239-adaptive-jet-contraction-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-239-adaptive-jet-contraction-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-239-adaptive-jet-contraction-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-239-adaptive-jet-contraction-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The trace-adaptive selector of RH-238 enforces a noise-dependent finite-jet tolerance [@WangRH238]. We prove the exact consequence. If $J_{m,R}(\tau_\sigma)\le\varepsilon_\sigma$ and $\varepsilon_\sigma\to0$, then the residual jets are Cauchy in the $J_{m,R}$ seminorm; in fact $$J_{m,R}(\tau_\sigma-\tau_{\sigma'})
   \le\varepsilon_\sigma+\varepsilon_{\sigma'}.$$

  All 30 adjacent-scale and 16 dual-channel archived cases satisfy the corresponding triangle bound. The minimum slacks are $0.00246$ and $0.00220$. The actual adjacent distances are not monotonically contracting, and between one and ten shell prefixes can meet a given tolerance. Most importantly, fixed-$m$ Cauchy convergence does not control coefficients above order $m$. Thus adaptive finite jets advance the coefficient route but do not imply a locally uniform regularized determinant limit.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: 'Finite-Jet Contraction and the All-Order Obstruction'
```

## Markdown 正文

# Finite-jet topology

For trace vectors through order $m$, define $$J_{m,R}(\tau)=\sum_{n=2}^m\frac{|\tau_n|}{n}R^n.$$ This is a seminorm because the first coordinate is ignored. It is the natural coefficient majorant for the truncated $\det_2$ logarithm.

[\[thm:contraction\]]{#thm:contraction label="thm:contraction"} Suppose a family $\tau_\alpha$ satisfies $J_{m,R}(\tau_\alpha)\le\varepsilon_\alpha$. Then $$J_{m,R}(\tau_\alpha-\tau_\beta)
 \le\varepsilon_\alpha+\varepsilon_\beta.$$ If $\varepsilon_\alpha\to0$, the family converges to zero in the fixed finite-jet seminorm.

The first inequality is the triangle inequality. Taking $\alpha,\beta$ in a tail where both tolerances are small proves the Cauchy property. Taking the assumed one-point bounds directly gives convergence to the zero jet.

The zero limit reflects the normalization chosen in RH-238: the adaptive cloud is selected to make the residual finite jet small. It is not yet the coefficient anchor required to identify a nontrivial deterministic numerator.

[\[cor:coeff\]]{#cor:coeff label="cor:coeff"} If $R>0$ and $J_{m,R}(\tau_\alpha)\le\varepsilon_\alpha$, then for every $2\le n\le m$, $$|\tau_{\alpha,n}|\le \frac{n\varepsilon_\alpha}{R^n},
 \qquad
 |\tau_{\alpha,n}-\tau_{\beta,n}|
 \le \frac{n(\varepsilon_\alpha+\varepsilon_\beta)}{R^n}.$$

Each nonnegative weighted coefficient is bounded by the full defining sum; apply the same observation to Theorem [\[thm:contraction\]](#thm:contraction){reference-type="ref" reference="thm:contraction"}.

Thus vanishing tolerances give simultaneous convergence of every coefficient in the fixed finite window, with explicit rates inherited from the tolerance schedule.

# Archived bounds

For adjacent scales the theorem gives $J(\tau_{\sigma_i}-\tau_{\sigma_{i+1}})\le\sigma_i+\sigma_{i+1}$. For two channels at the same scale it gives the bound $2\sigma$.

  Quantity                                                    value
  --------------------------------------------------- -------------
  Adjacent cases                                                 30
  Channel cases                                                  16
  Minimum adjacent bound slack                          $0.0024624$
  Minimum channel bound slack                           $0.0022040$
  Maximum actual adjacent distance                      $0.0231244$
  Both last-four actual sequences strictly contract              no
  Admissible-prefix count range                           $1$--$10$

  : Finite-jet contraction audit.

The deterministic upper bounds decrease with the noise schedule, but the actual distances fluctuate because the selected rank and shell phases jump. This distinction matters: a theorem can provide Cauchy control even when a short finite sequence is not pointwise monotone.

The last four left-channel distances happen to contract strictly, while the right-channel sequence does not. Neither observation changes the theorem: monotonicity is not required for Cauchy convergence, and a short monotone tail would not prove the all-order determinant statement.

# Why finite jets are insufficient

For each fixed $m$, convergence of the first $m$ coefficients gives only convergence of a Taylor polynomial. A sequence of entire functions can have all first $m$ coefficients equal and still grow arbitrarily at order $m+1$. For example, $$f_k(z)=\exp(kz^{m+1})$$ has the same logarithmic jet through order $m$ for every $k$, but is not locally bounded on any disk containing a nonzero point with positive real $z^{m+1}$.

Therefore the implication $$\text{vanishing fixed finite jet}
 \Longrightarrow
 \text{normal entire family}$$ is false. Uniformity in the order is indispensable.

[\[thm:no-finite\]]{#thm:no-finite label="thm:no-finite"} Fix $m\ge2$, a nonzero point $z_0$, and $K>0$. There is an entire zero-free function $F_K$, normalized by $F_K(0)=1$, whose logarithmic coefficients through order $m$ all vanish, but $|F_K(z_0)|=e^K$. Consequently no bound involving only a fixed logarithmic $m$-jet can imply local boundedness on a neighborhood containing $z_0$.

Take $$F_K(z)=\exp\!\left(K(z/z_0)^{m+1}\right).$$ Its normalized logarithm begins at order $m+1$, while $F_K(z_0)=e^K$. Letting $K\to\infty$ violates local boundedness.

The theorem is deliberately formulated for zero-free entire functions, so the obstruction persists inside the natural class of regularized determinant quotients; it is not caused by inserting arbitrary poles or zeros.

# Two legitimate continuations

There are two ways to strengthen the topology. The direct route controls all orders at once by a geometric envelope $|\tau_n|\le Mq^n$. A second possible route lets the audited order $m=m(\sigma)$ grow, but then it must also provide a uniform tail estimate beyond $m(\sigma)$. Merely increasing the computed order without such a tail bound repeats Theorem [\[thm:no-finite\]](#thm:no-finite){reference-type="ref" reference="thm:no-finite"} at a later index.

Both routes must be combined with an anchor. Convergence of the adaptive jets to zero proves that the chosen quotient tends toward one in every fixed audited coefficient; it does not prove that one is the intended deterministic relative factor.

# Next wall

RH-240 supplies the missing sufficient form: a geometric envelope $|\tau_n(\sigma)|\le Mq^n$ for every $n\ge2$ [@WangRH240; @Simon2005]. The archived orders $2$--$12$ fit such an envelope with $q<1$, but order thirteen begins the unaudited tail. In parallel, an anchoring theorem must show that the cloud has not absorbed the regular deterministic numerator.

No Gate A closure or zeta-zero statement is made.
