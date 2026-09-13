---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-146-projective-gram-base-recurrence"
canonical_tex: "zeta_mvp0/papers/RH-146-projective-gram-base-recurrence/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-146-projective-gram-base-recurrence/main.pdf"
source_sha256: "ed17544b0396f5c0fe9a99e14e2f5013868f4db14e5c74e191bb003bb36a30f8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Projective Gram Recurrence for the Normalized Directional Base A Sharp Sufficient Packet and Its Finite Polar-Gauge Audit

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-146-projective-gram-base-recurrence>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-146-projective-gram-base-recurrence/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-146-projective-gram-base-recurrence/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-146-projective-gram-base-recurrence/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-146-projective-gram-base-recurrence/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The remaining directional support frontier contains the normalized Gram base $$a(G)=\sqrt{\lambda_{\min}(G)/\lambda_{\max}(G)}.$$ We give a sharp multiplicative recurrence for this quantity. If $G,H$ are positive definite and $\mu_{\min},\mu_{\max}$ are the generalized eigenvalue extrema of $H$ relative to $G$, then the Hilbert projective distance $$d_{\rm proj}(G,H)=\log(\mu_{\max}/\mu_{\min})$$ satisfies $$a(H)\geq e^{-d_{\rm proj}(G,H)/2}a(G).$$ The coefficient $1/2$ is exact. Consequently, summable projective variation of an aligned Gram chain implies a positive normalized-base liminf. Merely bounded one-step distortion does not: $G_n=\operatorname{diag}(e^n,1)$ has $d_{\rm proj}(G_n,G_{n+1})=1$ while $a(G_n)\to0$.

  We audit the theorem on all 330 RH-135 Gram transitions using the physical polar alignment of the packet frames. Every one-step and cumulative bound holds. The numerical verdict is nevertheless negative for this direct sufficient route: step distances range from $3.92$ to $58.68$, chain totals from $97.53$ to $234.16$, and the resulting terminal product lower ranges from $1.66\times10^{-52}$ to $3.16\times10^{-23}$. Exact terminal bases are between $1.04\times10^{-10}$ and $5.11\times10^{-3}$, so the universal projective product discards enormous correlation. The theorem closes a rigorous logical subproblem, but the finite archive neither proves nor supports all-level projective summability.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Projective Gram Recurrence for the Normalized Directional Base\
  A Sharp Sufficient Packet and Its Finite Polar-Gauge Audit
```

## Markdown 正文

# The base packet

RH-139 reduces eventual directional support to two exact-matrix conditions: a controlled squared-tail envelope $y_n$ with $\limsup y_n<1$ and a normalized base $a_n$ with $\liminf a_n>0$. RH-140--RH-145 strengthen the finite enclosure and viability side. The second condition has so far been read directly from each Gramian. The purpose of this paper is to express it as a recurrence between consecutive Gramians.

For $G,H\succ0$, let $\mu_{\min}$ and $\mu_{\max}$ denote the smallest and largest eigenvalues of $G^{-1/2}HG^{-1/2}$. Equivalently, $$\label{eq:loewner}
 \mu_{\min}G\preceq H\preceq\mu_{\max}G.$$ The quantity $$d_{\rm proj}(G,H)=\log\frac{\mu_{\max}}{\mu_{\min}}$$ is the Hilbert projective distance on the positive definite cone [@Birkhoff1957; @Bushell1973; @Bhatia2007]. It ignores common scalar rescaling and measures only shape distortion.

# Sharp projective recurrence

[\[thm:step\]]{#thm:step label="thm:step"} For every pair $G,H\succ0$, $$\label{eq:step}
 a(H)\geq e^{-d_{\rm proj}(G,H)/2}a(G).$$ The factor $1/2$ in the exponent cannot be improved uniformly.

The Loewner bounds [\[eq:loewner\]](#eq:loewner){reference-type="eqref" reference="eq:loewner"} imply $$\lambda_{\min}(H)\geq\mu_{\min}\lambda_{\min}(G),
 \qquad
 \lambda_{\max}(H)\leq\mu_{\max}\lambda_{\max}(G).$$ Taking their ratio and square root gives $$a(H)\geq
 \sqrt{\frac{\mu_{\min}}{\mu_{\max}}}
 \sqrt{\frac{\lambda_{\min}(G)}{\lambda_{\max}(G)}}
 =e^{-d_{\rm proj}(G,H)/2}a(G).$$ For sharpness take $G=I_2$ and $H=\operatorname{diag}(e^d,1)$. Then $d_{\rm proj}(G,H)=d$, $a(G)=1$, and $a(H)=e^{-d/2}$, so equality holds.

At transition $n$, the packet construction supplies an orthogonal polar alignment $O_n$. Apply Theorem [\[thm:step\]](#thm:step){reference-type="ref" reference="thm:step"} to $O_n^TG_nO_n$ and $G_{n+1}$. Since $a(O_n^TG_nO_n)=a(G_n)$, no base term is changed by the gauge.

[\[cor:sum\]]{#cor:sum label="cor:sum"} Let $G_n\succ0$, let $O_n$ be any orthogonal alignments, and put $$d_n=d_{\rm proj}(O_n^TG_nO_n,G_{n+1}).$$ Then for $n>N$, $$\label{eq:product}
 a(G_n)\geq a(G_N)
 \exp\!\left(-\frac12\sum_{j=N}^{n-1}d_j\right).$$ In particular, if $\sum_{j=N}^{\infty}d_j<\infty$, then $$\inf_{n\geq N}a(G_n)\geq
 a(G_N)e^{-\frac12\sum_{j=N}^{\infty}d_j}>0.$$

Iterate [\[eq:step\]](#eq:step){reference-type="eqref" reference="eq:step"}. Orthogonal conjugation preserves the extreme eigenvalues of the source Gramian.

This gives a complete sufficient packet for the RH-139 base condition. It does not claim necessity: exact bases can stay positive despite infinite projective path length, for example under oscillation between two fixed shapes.

# Why bounded distortion is insufficient

The natural weakening $\sup_n d_n<\infty$ does not control accumulated anisotropy.

There is an SPD chain with $d_{\rm proj}(G_n,G_{n+1})=1$ for every $n$ but $a(G_n)\to0$. Thus no positive universal base liminf follows from bounded one-step projective distortion alone.

Take $G_n=\operatorname{diag}(e^n,1)$. The relative matrix is $G_n^{-1/2}G_{n+1}G_n^{-1/2}=\operatorname{diag}(e,1)$, hence every step has distance one. Yet $a(G_n)=e^{-n/2}\to0$. Equality holds in the cumulative bound [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"} at every level.

The obstruction separates two statements that can otherwise be confused. Uniform local control prevents a single catastrophic jump; summability prevents infinitely many moderate jumps from building unbounded condition number. A block cancellation theorem or a signed shape-drift argument could replace summability, but such extra structure must be proved explicitly.

# Physical polar-gauge audit

We rebuild the RH-135 records at 80 decimal digits. For consecutive packet input frames $U_n,U_{n+1}$, the physical gauge is the orthogonal polar factor of $U_n^TU_{n+1}$. The audit then computes the generalized eigenvalues of $G_{n+1}$ relative to $O_n^TG_nO_n$, the exact normalized bases, the one-step lower, and the cumulative product lower.

All 330 one-step inequalities and all 330 cumulative inequalities pass. The finite distribution is summarized in Table [1](#tab:audit){reference-type="ref" reference="tab:audit"}. Repeated rows at finer anchors occur because all three threshold branches coincide there.

::: {#tab:audit}
   $\sigma$   median step $d_{\rm proj}$   median chain variation   maximum variation   minimum exact terminal base
  ---------- ---------------------------- ------------------------ ------------------- -----------------------------
    $0.16$             $44.75$                    $135.60$              $142.05$           $1.04\times10^{-10}$
    $0.08$             $21.67$                    $108.56$              $122.76$            $5.66\times10^{-9}$
    $0.04$             $14.24$                    $150.28$              $188.46$            $8.22\times10^{-8}$
    $0.02$              $8.84$                    $167.52$              $204.04$            $9.76\times10^{-4}$
    $0.01$             $10.81$                    $228.01$              $234.16$            $2.14\times10^{-3}$

  : Projective Gram audit by frozen scale anchor.
:::

![Step-distance distributions, accumulated projective variation, and the gap between exact terminal bases and universal product lowers.](<../../../../../zeta_mvp0/papers/RH-146-projective-gram-base-recurrence/figures/projective_gram_base_recurrence.pdf>){#fig:audit width="\\textwidth"}

The smallest observed step distance is $3.9206$, not a small perturbative increment. Total variation grows again on the two longest chains, reaching $234.16$. Consequently the direct product estimate is between many orders and nearly fifty orders below the exact terminal base. This is not a defect in Theorem [\[thm:step\]](#thm:step){reference-type="ref" reference="thm:step"}: diagonal examples attain it exactly. It means the frozen Gram path contains favorable correlations that a product of universal one-step worst cases cannot retain.

The exact terminal bases themselves improve dramatically at the two finest anchors. That observation motivates a correlated base-tail state rather than an independent projective product. It is finite evidence only; five anchors cannot establish a liminf.

# Consequence and claim boundary

The normalized-base problem now has a rigorous fallback route: $$\boxed{\sum_n d_{\rm proj}(O_n^TG_nO_n,G_{n+1})<\infty}
 \quad\Longrightarrow\quad
 \boxed{\liminf_n a(G_n)>0}.$$ The implication is exact, dimension independent, and sharp at the level of universal constants. The present data do not support the antecedent: the observed increments remain macroscopic and cumulative variation does not stabilize. Nor do finite data disprove it for a different asymptotic assembly, gauge, block grouping, or analytically normalized Gram process.

RH-146 does not prove projective summability for the intended model, a positive all-level normalized-base liminf, the controlled tail gap, Stage A, a Hilbert--Polya operator, zeta-zero identification, or the Riemann Hypothesis. The next step is to preserve the observed correlation between base recovery and tail viability instead of multiplying their separate worst-case bounds.
