---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-104-source-weighted-prefix-law"
canonical_tex: "zeta_mvp0/papers/RH-104-source-weighted-prefix-law/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-104-source-weighted-prefix-law/main.pdf"
source_sha256: "051a674f649d630ffa868cb7b7f11a413db3564e6e48c80f0d2d4d97a0670d83"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Source-Weighted Finite-Prefix Laws: Directional Certificates and a Block-Contraction Barrier

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-104-source-weighted-prefix-law>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-104-source-weighted-prefix-law/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-104-source-weighted-prefix-law/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-104-source-weighted-prefix-law/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-104-source-weighted-prefix-law/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The block-contraction and effective-rank layers of the directional Hardy program control the postblock future, but they do not by themselves control the finite prefix. This paper isolates the missing object and gives a source-weighted law for it. For a finite matrix triple $(A,X,Y)$ and a block horizon $M$, define $$S_M=\sum_{r<M}\left\lVert A^rX\right\rVert_{\mathrm F}^2,
   \qquad
   P_M^2=\sum_{r<M}\left\lVert YA^rX\right\rVert_{\mathrm F}^2.$$ The exact prefix identity is $$P_M^2=\operatorname{tr}(X^*G_MX),
   \qquad
   G_M=\sum_{r<M}(A^r)^*Y^*YA^r.$$ Thus the correct finite-prefix target is the directional, source-weighted quantity $P_M$, rather than the dimension-free but potentially much looser certificate $\left\lVert Y\right\rVert_{\mathrm F}\sqrt{S_M}$. If $q=\left\lVert A^M\right\rVert_2<1$, the same source block supplies an exact transfer bound for the future tail: $$\sum_{j\ge M}\left\lVert YA^jX\right\rVert_{\mathrm F}^2
   \le \frac{\left\lVert Y\right\rVert_{\mathrm F}^2q^2}{1-q^2}S_M.$$ Consequently a polylogarithmic directional prefix law, combined with the square-root block law, is sufficient for a polylogarithmic full Hardy bound.

  The five inherited dyadic anchors remain numerically favorable: the largest actual directional prefix upper is $1.76031$ and the largest source-block upper is $3.09926$. The crude norm-product upper reaches $28.0815$, with a maximum loss factor $16.0554$. This gap is not a numerical accident. For $$A_\sigma=\begin{pmatrix}0&\sigma^{-a}\\0&0\end{pmatrix},\quad
   X=e_2,\quad Y_\sigma=\sigma^{-b}e_1^*,\quad 0\le b\le\tfrac12,$$ one has $A_\sigma^2=0$, perfect normalized one-column packet Gramians, zero postblock residual, and $\sigma\left\lVert Y_\sigma\right\rVert_{\mathrm F}^2\le1$, while the Hardy prefix has power $a+b$. Hence block contraction, normalized packet tails, and observation scaling do not imply a uniform prefix law. The five-anchor evidence supports the physical directional law, but its all-level proof remains an independent scalar gate. No Stage A, Hilbert--Polya, zero identification, or Riemann Hypothesis result is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Source-Weighted Finite-Prefix Laws:\
  Directional Certificates and a Block-Contraction Barrier
```

## Markdown 正文

**Keywords:** finite-prefix transient; source-weighted Gramian; directional Hardy energy; block contraction; nonnormal barrier.

**MSC 2020:** 47A10; 47B35; 65F15; 93B28; 65G20.

# Introduction

The recent packet papers have made the postblock part of the directional route increasingly explicit. RH-75 identified the square-root contraction scale needed to offset the mesh growth in the observation operator [@WangBlockLaw2026]. RH-77 then showed that a low-rank approximation of the postblock state can be transferred through the complete future by a finite observability Gramian [@WangEffectiveRank2026]. RH-103 exposed the remaining sigma powers in a max-plus ledger and, importantly, separated the finite prefix from the reduced future and the observation--residual term [@WangPowerLedger2026].

The prefix is easy to overlook because a block tail estimate is often written with a source norm and an observation norm. That estimate is valid, but it does not identify the physical quantity being measured. The finite transfer already contains the same source and observation directions that define the Hardy energy. A scalar product of two separate norms can erase their alignment, and in the present family that loss grows with the mesh.

This paper makes four precise contributions:

1.  it defines the exact source-weighted prefix Gramian and proves its finite-prefix identity;

2.  it gives a block-tail transfer theorem and a dyadic sufficient criterion showing how a directional prefix law closes the full Hardy estimate;

3.  it audits the five available anchors and quantifies the loss of the crude norm product;

4.  it proves an elementary nilpotent barrier showing that block contraction and normalized packet success cannot substitute for the missing all-level directional law.

The negative result is deliberately narrow. It does not say that the folded-Gaussian production family fails. It says that the present abstract packet hypotheses do not contain enough absolute information to prove the physical prefix bound. That distinction keeps the route honest and gives the next papers a sharply stated target.

# The source-weighted prefix object {#sec:object}

Let $A\in\mathbb C^{d\times d}$, $X\in\mathbb C^{d\times m}$, and $Y\in\mathbb C^{p\times d}$. All state and transfer matrices below are measured in Frobenius norm unless a subscript $2$ is displayed. Fix an integer horizon $M\ge1$ and define $$\begin{aligned}
 S_M(A,X)&=\sum_{r=0}^{M-1}\left\lVert A^rX\right\rVert_{\mathrm F}^2,
 \label{eq:source}\\
 P_M(A,X,Y)^2&=\sum_{r=0}^{M-1}\left\lVert YA^rX\right\rVert_{\mathrm F}^2,
 \label{eq:prefix}\\
 G_M(A,Y)&=\sum_{r=0}^{M-1}(A^r)^*Y^*YA^r.
 \label{eq:gram}\end{aligned}$$

A family of triples and horizons satisfies a source-weighted finite-prefix law if there are constants $C_P\ge0$, $a>0$, and $p\ge0$ such that, on a dyadic schedule $\sigma_k=\sigma_0 2^{-k}$, $$P_{M_k}(A_k,X_k,Y_k)^2\le C_P(k+a)^p.$$ The exponent $p$ is allowed to be logarithmic; it carries zero power of $\sigma_k$.

[\[prop:identity\]]{#prop:identity label="prop:identity"} For every finite triple and every $M$, $$P_M(A,X,Y)^2=\operatorname{tr}\!\bigl(X^*G_M(A,Y)X\bigr).
  \label{eq:identity}$$ In particular, $G_M$ is positive semidefinite and $P_M$ depends on the source through its actual orientation, not only through $\left\lVert X\right\rVert_{\mathrm F}$.

For each $r$, $$\left\lVert YA^rX\right\rVert_{\mathrm F}^2
 =\operatorname{tr}\!\bigl(X^*(A^r)^*Y^*YA^rX\bigr).$$ Summing and using linearity of the trace gives [\[eq:identity\]](#eq:identity){reference-type="eqref" reference="eq:identity"}. Each summand in [\[eq:gram\]](#eq:gram){reference-type="eqref" reference="eq:gram"} is positive semidefinite.

The identity is elementary, but its placement in the route matters. It is the finite analogue of the full observability Gramian, with the source kept inside the quadratic form. Replacing it immediately by two separate norms throws away precisely the directional cancellation that the production matrices may provide.

[\[prop:crude\]]{#prop:crude label="prop:crude"} For every $M$, $$P_M(A,X,Y)\le \left\lVert Y\right\rVert_{\mathrm F}\sqrt{S_M(A,X)}.
  \label{eq:crude}$$

The Frobenius submultiplicativity inequality gives $\left\lVert YA^rX\right\rVert_{\mathrm F}\le\left\lVert Y\right\rVert_{\mathrm F}\left\lVert A^rX\right\rVert_{\mathrm F}$ for every $r$. Square, sum, and take the square root.

The bound in [\[prop:crude\]](#prop:crude){reference-type="ref" reference="prop:crude"} is useful for a black-box certificate and is sometimes the only available estimate. It is not an equivalent definition of the prefix law. In particular, $P_M$ may remain bounded while $\left\lVert Y\right\rVert_{\mathrm F}\sqrt{S_M}$ grows with the mesh.

# Block transfer and the finite-prefix criterion {#sec:block}

Let the complete directional Hardy energy be $$H(A,X,Y)^2=\sum_{j\ge0}\left\lVert YA^jX\right\rVert_{\mathrm F}^2,
 \label{eq:hardy}$$ whenever the series converges. Put $q=\left\lVert A^M\right\rVert_2$.

[\[thm:tail\]]{#thm:tail label="thm:tail"} If $q<1$, then $$\sum_{j\ge M}\left\lVert YA^jX\right\rVert_{\mathrm F}^2
 \le
 \frac{\left\lVert Y\right\rVert_{\mathrm F}^2q^2}{1-q^2}\,S_M(A,X).
 \label{eq:tail}$$ Consequently, $$H(A,X,Y)^2\le P_M(A,X,Y)^2
 +\frac{\left\lVert Y\right\rVert_{\mathrm F}^2q^2}{1-q^2}S_M(A,X).
 \label{eq:full}$$

Write each $j\ge M$ uniquely as $j=bM+r$ with $b\ge1$ and $0\le r<M$. Since powers of one matrix commute, $A^{bM+r}=A^{bM}A^r$. Therefore $$\left\lVert YA^{bM+r}X\right\rVert_{\mathrm F}
 \le \left\lVert Y\right\rVert_{\mathrm F}\,q^b\left\lVert A^rX\right\rVert_{\mathrm F}.$$ Square and sum first over $b$ and then over $r$: $$\sum_{b\ge1}\sum_{r<M}\left\lVert YA^{bM+r}X\right\rVert_{\mathrm F}^2
 \le \left\lVert Y\right\rVert_{\mathrm F}^2S_M\sum_{b\ge1}q^{2b},$$ which is [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}. Adding the finite prefix gives [\[eq:full\]](#eq:full){reference-type="eqref" reference="eq:full"}.

The theorem deliberately uses $S_M$ for the tail, because a contraction of $A^M$ acts on the state after the source block. The finite prefix itself is more sharply represented by the directional Gramian $G_M$.

[\[thm:dyadic\]]{#thm:dyadic label="thm:dyadic"} Let $\sigma_k=\sigma_0 2^{-k}$ and suppose that for all $k\ge0$ there are horizons $M_k$ and constants $C_P,C_S,C_Y,C_q\ge0$, $a>0$, and $p,s\ge0$ such that $$\begin{aligned}
 P_{M_k}(A_k,X_k,Y_k)^2&\le C_P(k+a)^p,
 \label{eq:dyadic-p}\\
 S_{M_k}(A_k,X_k)&\le C_S(k+a)^s,
 \label{eq:dyadic-s}\\
 \sigma_k\left\lVert Y_k\right\rVert_{\mathrm F}^2&\le C_Y,
 \label{eq:dyadic-y}\\
 \left\lVert A_k^{M_k}\right\rVert_2&\le C_q\sqrt{\sigma_k}.
 \label{eq:dyadic-q}
 \end{aligned}$$ If $C_q^2\sigma_0<1$, then $$H(A_k,X_k,Y_k)^2
 \le C_P(k+a)^p
 +\frac{C_YC_q^2C_S}{1-C_q^2\sigma_0}(k+a)^s.
 \label{eq:dyadic-full}$$ In particular, the full Hardy energy is polylogarithmic in $1/\sigma_k$.

Apply [\[thm:tail\]](#thm:tail){reference-type="ref" reference="thm:tail"}. The last two hypotheses imply $$\frac{\left\lVert Y_k\right\rVert_{\mathrm F}^2\left\lVert A_k^{M_k}\right\rVert_2^2}
      {1-\left\lVert A_k^{M_k}\right\rVert_2^2}
 \le
 \frac{(C_Y/\sigma_k)C_q^2\sigma_k}
      {1-C_q^2\sigma_0}.$$ Insert [\[eq:dyadic-p\]](#eq:dyadic-p){reference-type="eqref" reference="eq:dyadic-p"} and [\[eq:dyadic-s\]](#eq:dyadic-s){reference-type="eqref" reference="eq:dyadic-s"}. Since $k=\log_2(\sigma_0/\sigma_k)$, polynomial growth in $k$ is polylogarithmic in $1/\sigma_k$.

If the prefix itself has signed power $p_\mathrm{dir}$, then it enters the directional Hardy ledger directly. If one only inserts separate powers for $\left\lVert Y\right\rVert$ and $S_M$, the crude certificate has power $p_Y+\tfrac12p_S$. The two numbers need not agree. RH-103's max-plus ledger therefore has a genuine finite-prefix leaf; it cannot be replaced by a source norm leaf without an additional alignment theorem [@WangPowerLedger2026].

# Five-anchor audit {#sec:audit}

The audit reads the exact dyadic source and transfer certificates from the RH-75 production ledger. For every channel it records the certified source block upper $S_M$, the directional prefix upper $P_M$, the observation norm, and the contraction $q$. The displayed values are outward-rounded inputs or direct consequences of them; the audit is intended as a reproducible finite check, not as an all-level theorem.

::: {#tab:anchors}
    $k$   $\sigma$   $M$   $\max P_M$   $\max S_M$   $\max\left\lVert Y\right\rVert_{\mathrm F}$   $\max q$
  ----- ---------- ----- ------------ ------------ --------------------------------------------- ----------
      0       0.16     4        1.003        1.156                                         4.000     0.0210
      1       0.08     9        1.265        1.600                                         5.657     0.0158
      2       0.04    16        1.485        2.205                                         8.000     0.0172
      3       0.02    25        1.634        2.671                                        11.314     0.0120
      4       0.01    32        1.760        3.099                                        16.000     0.0082

  : Largest left/right channel values at each inherited anchor.
:::

The directional prefix remains below $1.761$ over all ten channels, and the source block remains below $3.100$. These are exactly the type of finite envelopes required in [\[thm:dyadic\]](#thm:dyadic){reference-type="ref" reference="thm:dyadic"}. The same data show why the separate norm certificate is not a satisfactory proxy:

::: {#tab:loss}
    $\sigma$   $\max P_M$   $\max\left\lVert Y\right\rVert_{\mathrm F}\sqrt{S_M}$   maximum ratio
  ---------- ------------ ------------------------------------------------------- ---------------
        0.16        1.003                                                   4.051           4.041
        0.08        1.265                                                   6.968           5.682
        0.04        1.485                                                  11.722           8.031
        0.02        1.634                                                  18.371          11.355
        0.01        1.760                                                  28.082          16.055

  : Directional prefix versus the crude product certificate.
:::

At the finest anchor, the crude bound is more than sixteen times the actual directional certificate. The gap grows while the observation norm grows, which is exactly the sigma-power concern exposed by RH-103.

![The left panel compares the physical directional prefix with the separate norm product at the five anchors. The right panel is the nilpotent barrier family: its block contraction and normalized packet tail are both zero, yet the prefix has power $3/2$.](<../../../../../zeta_mvp0/papers/RH-104-source-weighted-prefix-law/figures/source_weighted_prefix_law.pdf>){#fig:audit width="98%"}

# A nilpotent independence barrier {#sec:barrier}

The next proposition isolates the exact logical boundary. It is finite dimensional, stable in the strongest possible block sense, and intentionally independent of the production construction.

[\[prop:barrier\]]{#prop:barrier label="prop:barrier"} Let $a\ge0$ and $0\le b\le\tfrac12$, and for $0<\sigma<1$ set $$A_\sigma=\begin{pmatrix}0&\sigma^{-a}\\0&0\end{pmatrix},
 \qquad X=e_2,\qquad Y_\sigma=\sigma^{-b}e_1^*.
 \label{eq:barrier-family}$$ With block horizon $M=2$, $$\begin{aligned}
 A_\sigma^2&=0, & q&=0,\\
 \sigma\left\lVert Y_\sigma\right\rVert_{\mathrm F}^2&=\sigma^{1-2b}\le1,\\
 H(A_\sigma,X,Y_\sigma)&=P_2(A_\sigma,X,Y_\sigma)
 =\sigma^{-(a+b)}.
 \label{eq:barrier-values}
 \end{aligned}$$ Every nonzero state in the orbit has a one-column normalized Gram matrix equal to $[1]$, and the postblock residual after $M=2$ is zero. Hence the block contraction, normalized packet tail, and observation-scaling gates can all be perfect while the prefix has any prescribed power $\gamma=a+b>0$.

Since $A_\sigma e_2=\sigma^{-a}e_1$ and $A_\sigma e_1=0$, $$Y_\sigma X=0,\qquad
 Y_\sigma A_\sigma X=\sigma^{-(a+b)},\qquad
 Y_\sigma A_\sigma^jX=0\quad(j\ge2).$$ This proves [\[eq:barrier-values\]](#eq:barrier-values){reference-type="eqref" reference="eq:barrier-values"}. The matrix $A_\sigma^2$ is zero, so the block contraction and postblock state vanish. A nonzero one-column state $z$ satisfies $z^*z/\left\lVert z\right\rVert_{\mathrm F}^2=[1]$, which proves the normalized Gram assertion. Finally, for any $\gamma>0$, choose $b=\min\{\gamma,1/2\}$ and $a=\gamma-b$.

The barrier does not contradict a physical source-weighted prefix law. It shows only that such a law is additional information. In particular, a proof based on RH-75's contraction and RH-77's postblock rank transfer must still establish how the physical source and observation directions interact before the block horizon.

# Route consequence and open theorem {#sec:route}

The finite-prefix target can now be stated without ambiguity. For the intended dyadic production family, the next all-level theorem should prove $$\sum_{r<M_k}\left\lVert Y_kA_k^rX_k\right\rVert_{\mathrm F}^2
 \le \operatorname{polylog}(1/\sigma_k),
 \label{eq:open-law}$$ preferably through a structural identity for the source-weighted Gramian $G_{M_k}$. A bound obtained only by multiplying $\left\lVert Y_k\right\rVert_{\mathrm F}^2$ and $S_{M_k}$ is sufficient only if its sigma powers cancel; the five-anchor data show that this route is substantially more expensive.

Combining [\[eq:open-law\]](#eq:open-law){reference-type="eqref" reference="eq:open-law"} with the square-root block law gives the conditional conclusion of [\[thm:dyadic\]](#thm:dyadic){reference-type="ref" reference="thm:dyadic"}. The postblock effective-rank theorem can then be applied to the remaining future, while the observation-- residual product remains a separate ledger term. Thus RH-104 does not close Stage A, but it changes the next question from a vague "prefix bound" to a specific source-weighted Gramian estimate.

The logical status is therefore:

-   the exact finite-prefix identity and block-tail transfer are proved;

-   the five-anchor directional envelope is numerically green;

-   the nilpotent family proves that the packet hypotheses alone do not imply the all-level law;

-   uniform directional prefix control remains open.

No statement here constructs a Hilbert--Polya operator, proves a $T\log T$ counting law, identifies dynamical zeros with zeta zeros, or proves the Riemann Hypothesis.

# Reproducibility

The directory contains the scalar bound implementation, the audit builder, the smoke audit, tests, figures, and a hash-checked archive. From this directory, run:

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \\
      experiments/build_prefix_audit.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \\
      experiments/build_prefix_audit.py --smoke
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \\
      experiments/make_figures.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/pytest -q -p no:cacheprovider

The archive builder records all external inputs and publication hashes. The separate verification script checks them again.
