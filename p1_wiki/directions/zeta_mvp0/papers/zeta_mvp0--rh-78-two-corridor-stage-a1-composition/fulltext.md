---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-78-two-corridor-stage-a1-composition"
canonical_tex: "zeta_mvp0/papers/RH-78-two-corridor-stage-A1-composition/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-78-two-corridor-stage-A1-composition/main.pdf"
source_sha256: "971c11be2c82ae2ea1d0734525f5ffea44d4338909f3ddd04387764187d620fd"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Two Corridors to Stage A1 and the Conditional Closure of Intrinsic Identification Full-Block Scaling, Effective-Rank Futures, and the Quarter-Power Exponent Ledger

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-78-two-corridor-stage-A1-composition>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-78-two-corridor-stage-A1-composition/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-78-two-corridor-stage-A1-composition/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-78-two-corridor-stage-A1-composition/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-78-two-corridor-stage-A1-composition/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-75 identified a full-block route to a polylogarithmic small-noise Hardy bound. RH-76 ruled out single-arc phase compression, while RH-77 found a second route: uniformly tiny postblock effective rank. This paper composes both alternatives with the earlier intrinsic-identification theorems and isolates the sole remaining Stage-A premise.

  In the full-block corridor, a log-square horizon together with $\left\lVert A_k^{M_k}\right\rVert=O(\sqrt{\sigma_k})$ gives $E_{B,k},E_{C,k}=\operatorname{polylog}(1/\sigma_k)$. In the effective-rank corridor, decompose $A_k^{M_k}X_k=B_{k,r}+R_{k,r}$; if the reduced future and the observability-transferred residual are polylogarithmic, the same Hardy conclusion follows. Either corridor has zero power of $\sigma$.

  RH-54's factor-aware theorem then yields $$\left\lVert I_{n,\sigma}\right\rVert_{S_2}
   =O\!\left(n^{-2}\sigma^{-13/4}
   \operatorname{polylog}(1/\sigma)\right).$$ For every strict schedule $n\sigma^2\to\infty$, this tends to zero. Thus an all-level proof of either corridor closes Stage A1 and, together with the already rigorous RH-54/RH-55 transfer, makes the intrinsic identification unconditional. No simultaneous proof of both corridors is required.

  A 256-bit Arb composition audit checks the five validated anchors. The common per-channel Hardy upper grows only from $1.079$ to $1.836$; every frozen Hardy product lies inside the conditional envelope. The Hardy sigma-power is zero, strictly below the quarter-power threshold. On the stress mesh $n=\sigma^{-2}(k+2)$, the identification envelope decreases from $0.07355$ to $0.002961$. RH-77 rank-four future errors remain below $5.35\times10^{-6}$.

  This is a conditional closure theorem, not an all-dyadic proof. The sole remaining Stage-A premise is an analytic all-level theorem for at least one corridor. Stage A1, unconditional Stage A4, Hilbert--Polya, and the Riemann Hypothesis remain open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Two Corridors to Stage A1 and the Conditional Closure of Intrinsic Identification\
  Full-Block Scaling, Effective-Rank Futures, and the Quarter-Power Exponent Ledger
```

## Markdown 正文

**Keywords:** conditional composition; Hardy energy; effective rank; dyadic mesh; intrinsic Riesz identification.

**MSC 2020:** 47A10; 47B10; 47B35; 65G20.

# Introduction

The Stage-A route now has a cleaner logical structure than it did at RH-50. Finite-scale assembly and Hardy completion are rigorous end to end. Adaptive strong--weak Riesz transfer is available. The only missing ingredient is a uniform directional Hardy budget over the physical dyadic family.

RH-75 gave a sufficient full-operator law [@WangScaling2026]. RH-77 gave a different, source-specific reduction based on postblock singular values [@WangRank2026]. The purpose of this paper is to show that these are alternative corridors into the same downstream theorem. This matters because the full Frobenius block law may be harder to prove than directional rank decay; the program should not require the stronger statement if the weaker physical one suffices.

# Corridor I: full-block scaling

Let $\sigma_k=\sigma_0 2^{-k}$. The RH-75 hypotheses give $$M_k=O(k^2),\quad
 \left\lVert A_k^{M_k}\right\rVert\le C_q\sqrt{\sigma_k},\quad
 \sigma_k\left\lVert Y_k\right\rVert^2\le C_y,$$ together with polylogarithmic one-block source and finite-prefix energies. The block theorem then implies $$E_k^2\le C_f(k+a)^f+C_t(k+a)^s.
 \label{eq:block-corridor}$$ Thus $E_k$ is polylogarithmic and carries no negative power of $\sigma_k$.

# Corridor II: effective-rank future

Let $B_k=A_k^{M_k}X_k$ and choose a rank-$r_k$ approximation $B_{k,r}$. Split the Hardy energy into its finite prefix and future. RH-77 gives $$|T_k(B_k)-T_k(B_{k,r})|
 \le G_k^{1/2}\left\lVert B_k-B_{k,r}\right\rVert_{S_2},
 \label{eq:rank-error}$$ where $G_k=\left\lVert O_{k,M_k}\right\rVert/(1-\left\lVert A_k^{M_k}\right\rVert^2)$.

[\[thm:rank-corridor\]]{#thm:rank-corridor label="thm:rank-corridor"} Suppose the finite prefix, reduced future $T_k(B_{k,r})$, and right side of [\[eq:rank-error\]](#eq:rank-error){reference-type="eqref" reference="eq:rank-error"} are each polylogarithmic in $1/\sigma_k$. Then the full Hardy energy is polylogarithmic. The rank schedule itself may be fixed or polylogarithmic.

Apply the triangle inequality to the finite-prefix/future decomposition and then [\[eq:rank-error\]](#eq:rank-error){reference-type="eqref" reference="eq:rank-error"}. A finite sum of polylogarithmic quantities is polylogarithmic.

This corridor is strictly directional. It does not imply a small full-space operator norm and therefore does not conflict with fixed-depth no-go results.

# Composition into intrinsic identification

RH-54 proved that if $$E_B=O(\sigma^{-\alpha_B}),\qquad
 E_C=O(\sigma^{-\alpha_C}),$$ and the range-restricted residues are bounded, then $$\left\lVert I_{n,\sigma}\right\rVert_{S_2}
 =O\!\left(n^{-2}\sigma^{-13/4-\alpha_B-\alpha_C}\right).
 \label{eq:rh54}$$ Every strict $n\sigma^2\to\infty$ schedule survives when $\alpha_B+\alpha_C\le1/4$ [@WangFactor2026]. RH-55 supplies the adaptive strong--weak Riesz/cutoff transfer needed by that theorem [@WangStrongWeak2026].

[\[thm:composition\]]{#thm:composition label="thm:composition"} Assume the already established RH-54/RH-55 residue and transfer hypotheses. If either the full-block corridor [\[eq:block-corridor\]](#eq:block-corridor){reference-type="eqref" reference="eq:block-corridor"} or the effective- rank corridor of [\[thm:rank-corridor\]](#thm:rank-corridor){reference-type="ref" reference="thm:rank-corridor"} holds at every dyadic level for both left and right channels, then:

1.  Stage A1 has a polylogarithmic directional Hardy budget;

2.  $\alpha_B=\alpha_C=0$, so the RH-54 quarter-power gate is strict;

3.  for every schedule $n\sigma^2\to\infty$, $$\left\lVert I_{n,\sigma}\right\rVert_{S_2}
      =O\!\left(n^{-2}\sigma^{-13/4}
      \operatorname{polylog}(1/\sigma)\right)\longrightarrow0.
      \label{eq:identification}$$

Either corridor gives polylogarithmic $E_B,E_C$, hence zero sigma powers. Insert them into [\[eq:rh54\]](#eq:rh54){reference-type="eqref" reference="eq:rh54"}. Write $n=\sigma^{-2}L(\sigma)$ with $L(\sigma)\to\infty$; the right side of [\[eq:identification\]](#eq:identification){reference-type="eqref" reference="eq:identification"} becomes $O(\sigma^{3/4}L(\sigma)^{-2}\operatorname{polylog}(1/\sigma))$, which tends to zero.

The theorem is a logical closure: it identifies a single missing family premise, but does not assert that premise.

# Five-anchor composition audit

The RH-75 common constants give $$E_{B,k}^2,E_{C,k}^2
 \le0.552(k+2)+0.058788.
 \label{eq:anchor-envelope}$$ The audit evaluates this and the RH-54 expression at 256-bit Arb precision [@Johansson2017]. Every RH-70 frozen product is enclosed by [\[eq:anchor-envelope\]](#eq:anchor-envelope){reference-type="eqref" reference="eq:anchor-envelope"}.

::: {#tab:audit}
    $\sigma$   Hardy   product       rank-4 error   identification
  ---------- ------- --------- ------------------ ----------------
        0.16   1.079     1.163    $5.05\,10^{-9}$          0.07355
        0.08   1.310     1.715    $3.40\,10^{-9}$          0.02867
        0.04   1.506     2.267    $3.48\,10^{-8}$          0.01268
        0.02   1.679     2.819   $6.77\,10^{-10}$         0.005997
        0.01   1.836     3.371    $5.35\,10^{-6}$         0.002961

  : Conditional common Hardy upper, product upper, rank-four future error, and identification envelope on $n=\sigma^{-2}(k+2)$.
:::

The anchor envelope has logarithmic energy-squared growth, so both Hardy sigma powers are zero. The effective-rank residual is much smaller than the common energy budget. The stress identification envelope decreases at every stored level.

![Conditional Hardy envelope, actual product inclusion, rank-four remainder, and strict-mesh identification decay.](<../../../../../zeta_mvp0/papers/RH-78-two-corridor-stage-A1-composition/figures/two_corridor_stage_A1_composition.pdf>){#fig:audit width="98%"}

# Exact remaining frontier

After RH-72--RH-78, the Stage-A dependency graph is: $$\boxed{\text{all-level block law}}
 \quad\text{or}\quad
 \boxed{\text{all-level effective-rank law}}
 \Longrightarrow
 \text{Stage A1}
 \Longrightarrow
 \text{intrinsic identification}.$$ Finite-scale inclusion, normalized factors, terminal Hardy arithmetic, adaptive cutoff transfer, and downstream exponent composition are no longer open in their stated scopes.

RH-79 will examine how this conditional identification feeds the Stage-A4 intrinsic determinant statement and precisely which limit interchanges remain. The present paper does not prove either all-level premise, so Stage A1 and unconditional Stage A4 remain open. It constructs no renormalized determinant limit, Hilbert--Polya operator, $T\log T$ law, prime-power trace formula, zeta-zero identity, or proof of the Riemann Hypothesis.

# Conclusion

The route no longer depends on rescuing a failed phase-arc picture. There are two mathematically sufficient corridors, and the effective-rank corridor is strongly supported at the five validated scales. Proving one all-level corridor is now the sole Stage-A analytic wall.
