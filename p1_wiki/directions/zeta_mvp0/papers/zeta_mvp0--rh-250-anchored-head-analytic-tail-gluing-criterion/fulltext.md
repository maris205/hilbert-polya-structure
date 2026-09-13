---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-250-anchored-head-analytic-tail-gluing-criterion"
canonical_tex: "zeta_mvp0/papers/RH-250-anchored-head-analytic-tail-gluing-criterion/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-250-anchored-head-analytic-tail-gluing-criterion/main.pdf"
source_sha256: "5fed5ea8f8e4c1250598ef4adf73d51f0d7d001d35879724a8f36a57b0a4df1c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Anchored Head--Analytic Tail Gluing Criterion

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-250-anchored-head-analytic-tail-gluing-criterion>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-250-anchored-head-analytic-tail-gluing-criterion/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-250-anchored-head-analytic-tail-gluing-criterion/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-250-anchored-head-analytic-tail-gluing-criterion/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-250-anchored-head-analytic-tail-gluing-criterion/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We isolate the exact finite-head/analytic-tail gluing step needed to turn cloud-extracted trace control into a locally uniform relative determinant. The logarithmic error is the sum of a finite anchored head error, a quotient tail, and the deterministic target tail; exponentiation gives an explicit determinant bound. Applying the ledger to the current relaxed shell class finds no complete certificate: the anchored head fails at all 32 endpoints, the quotient tail is certified only on 17 finite matrices, and the target tail is unbounded. This is a scoped route stop, not a global impossibility claim.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'Anchored Head--Analytic Tail Gluing Criterion'
```

## Markdown 正文

# Exact gluing estimate

Let $\tau_n(\sigma)$ be a residual trace sequence and $a_n$ a deterministic target. For $R$ inside both logarithmic convergence domains, define $$L_\sigma(z)=-\sum_{n\ge2}\frac{\tau_n(\sigma)}{n}z^n,
 \qquad
 L_*(z)=-\sum_{n\ge2}\frac{a_n}{n}z^n.$$ For a finite head through $N$ put $$H_N(\sigma,R)=\sum_{n=2}^{N}\frac{|\tau_n(\sigma)-a_n|R^n}{n},$$ and let $T_\sigma(N,R)$ and $T_*(N,R)$ be the analogous absolute tails from $n>N$.

[\[thm:glue\]]{#thm:glue label="thm:glue"} For every $|z|\le R$, $$\label{eq:log-error}
 |L_\sigma(z)-L_*(z)|
 \le H_N(\sigma,R)+T_\sigma(N,R)+T_*(N,R).$$ If additionally $|L_\sigma(z)|,|L_*(z)|\le B$ on the disk, then for $D_\sigma=e^{L_\sigma}$ and $D_*=e^{L_*}$, $$\label{eq:det-error}
 |D_\sigma(z)-D_*(z)|
 \le e^B\bigl(H_N+T_\sigma+T_*\bigr).$$ Uniform convergence follows if the three budgets tend uniformly to zero along a sequence of heads and radii.

Subtract the two absolutely convergent series and apply the triangle inequality separately to the finite head and the two tails. For the second claim, integrate the derivative of $e^u$ along the line segment between the two logarithms; its modulus is at most $e^B$.

RH-246 supplies a conditional bound for $T_\sigma$ from a contractive block: $$T_\sigma(N,R)\le
 \frac{K_mR^m}{m(1-\eta_mR^m)}\sum_{r=0}^{m-1}L_rR^r$$ whenever $N\ge m-1$; using a bound beginning at $m$ is conservative for a tail beginning at $m+1$ [@WangRH246]. The target tail $T_*$ is a separate coefficient theorem, not supplied by the finite RH-243 dictionary.

# Current certificate ledger

We use the RH-248 convex shell relaxation for the head, so any failure also rules out the legal single-use shell class [@WangRH243; @WangRH248]. The minimum and maximum anchored head distances are $$0.14649763462315904\quad\text{and}\quad0.4240179027308174,$$ with zero passes at the 32 archived endpoints. The RH-246 12-block tail diagnostic gives $1.7991531976413385\times10^{-5}$ on only 17 endpoints. The smallest head distance is therefore $8142.588125081018$ times this finite tail budget. The target tail is not bounded, and the two endpoint sets do not yet form a uniform family.

  certificate                                            status
  ------------------------------------ ------------------------
  anchored head, 32 endpoints                       0/32 passes
  quotient tail, 17 finite endpoints     finite diagnostic only
  deterministic target tail                         not bounded
  complete head/tail certificates                             0

# Boundary and route stop

Theorem [\[thm:glue\]](#thm:glue){reference-type="ref" reference="thm:glue"} is exact and remains the correct interface to RH-240 [@WangRH240]. The negative ledger is scoped to the frozen candidate class, order-12 head, unit disk, and finite subbatch used in RH-246. It does not exclude a new anchored cloud, an expanded window, a different function space, or a future target-tail theorem. It does establish that adding the current analytic-tail diagnostic cannot rescue the missing anchored head.

Gate A remains open and Gates B--E are untouched. No Hilbert--Polya operator, zeta-divisor equality, Riemann-zero identification, or RH implication is claimed.
