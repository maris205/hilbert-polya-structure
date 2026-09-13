---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-128-conditional-eventual-directional-support"
canonical_tex: "zeta_mvp0/papers/RH-128-conditional-eventual-directional-support/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-128-conditional-eventual-directional-support/main.pdf"
source_sha256: "86e4ade049a0f7207a2f33ba8e0ef0bbd163b717e2494c327aa12f45b86e8db0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Conditional Eventual Directional Support Contractive Rayleigh Recurrences and an Explicit Liminf Floor

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-128-conditional-eventual-directional-support>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-128-conditional-eventual-directional-support/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-128-conditional-eventual-directional-support/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-128-conditional-eventual-directional-support/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-128-conditional-eventual-directional-support/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close the RH-120--RH-127 directional algebra conditionally. Let $x_n=\gamma_n^2$ and suppose eventually $x_{n+1}\leq\rho x_n+q$ with $0\leq\rho<1$. Then $\limsup x_n\leq x_*=q/(1-\rho)$. If $x_*<1$ and $$\liminf_n\frac{V_n}{L_n^4C_n}\geq A_*>0,$$ the directional candidates satisfy $$\liminf_n B_n\geq(1-\sqrt{x_*})^4A_*.$$ Every threshold strictly below this value is eventually supported. The constant-coefficient floor is sharp. A 4,096-recurrence audit has zero failures. The theorem isolates, but does not prove, the remaining physical all-level packet.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Conditional Eventual Directional Support\
  Contractive Rayleigh Recurrences and an Explicit Liminf Floor
```

## Markdown 正文

# Affine limsup theorem

[\[thm:affine\]]{#thm:affine label="thm:affine"} Suppose nonnegative $x_n$ obeys, for all sufficiently large $n$, $x_{n+1}\leq\rho x_n+q$ with $0\leq\rho<1$. Then $$\limsup_{n\to\infty}x_n\leq\frac{q}{1-\rho}.$$ The same conclusion holds if eventually $\rho_n\leq\rho$ and $q_n\leq q$.

Iteration gives $x_{N+k}\leq\rho^kx_N+q(1-\rho^k)/(1-\rho)$. Let $k\to\infty$. The nonstationary version is dominated by the same recurrence.

# Eventual support closure

Let $A_n=V_n/(L_n^4C_n)$ and $B_n=(1-\sqrt{x_n})_+^4A_n$. RH-125 proves that $B_n$ is a valid lower candidate whenever its finite matrix hypotheses and RH-127 guards hold.

[\[thm:support\]]{#thm:support label="thm:support"} Under Theorem [\[thm:affine\]](#thm:affine){reference-type="ref" reference="thm:affine"}, suppose $x_*=q/(1-\rho)<1$ and $\liminf A_n\geq A_*>0$. Then $$\liminf B_n\geq(1-\sqrt{x_*})^4A_*.$$ Consequently every $\tau<(1-\sqrt{x_*})^4A_*$ satisfies $B_n>\tau$ for all sufficiently large $n$.

The map $x\mapsto(1-\sqrt x)_+^4$ is continuous and decreasing. Combine the limsup bound for $x_n$ with the liminf bound for $A_n$, then use the definition of liminf. Strict inequality for $\tau$ gives eventual support.

For constant equality $x_{n+1}=\rho x_n+q$ and $A_n=A_*$, the limit equals the displayed floor, proving sharpness. The argument is elementary but its inputs preserve the one-sided matrix logic developed in the previous layers [@HornJohnson1991; @Bhatia2007].

# Audit and exact remaining packet

The audit samples 4,096 contractive coefficient caps, subunit fixed points, positive bases, and nonstationary recurrences dominated by those caps. There are zero affine-envelope or support-floor failures. A constant coefficient record approaches the theorem floor to relative error below $10^{-10}$.

![The support factor over the contractive phase diagram and representative affine envelopes.](<../../../../../zeta_mvp0/papers/RH-128-conditional-eventual-directional-support/figures/conditional_eventual_directional_support.pdf>){width="\\textwidth"}

The remaining physical packet is now explicit: validated all-level coefficients with $\rho<1$ and $q/(1-\rho)<1$, a positive liminf for $V_n/(L_n^4C_n)$, and either a common operator assembly or RH-127 outward radii. The four finite RH-125 edges cannot establish these eventual facts. No uniform Stage A, Hilbert--Polya operator, zeta-zero identification, or Riemann Hypothesis conclusion is claimed.
