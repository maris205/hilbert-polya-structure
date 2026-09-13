---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-108-finite-memory-fourth-cross-support"
canonical_tex: "zeta_mvp0/papers/RH-108-finite-memory-fourth-cross-support/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-108-finite-memory-fourth-cross-support/main.pdf"
source_sha256: "ca847d49a1265761cf1ba2849c339d186cd26bccd4c0a48b04cab648de8e819f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Memory Fourth-Cross Support A Weyl Certificate, Reduced Moments, and a Normalized-Memory Barrier

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-108-finite-memory-fourth-cross-support>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-108-finite-memory-fourth-cross-support/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-108-finite-memory-fourth-cross-support/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-108-finite-memory-fourth-cross-support/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-108-finite-memory-fourth-cross-support/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-107 reduced the fine-scale quotient problem to a single missing statement: the fourth projected-cross singular ratio must eventually stay above the adaptive cutoff. This paper asks whether the reduced moments of RH-95 and the finite-memory action law of RH-101 supply that statement.

  Let $V$ be an isometric packet, $P=VV^*$, and $K_t=(I-P)G_tV$, where $G_t=\sum_{j=0}^{t}\eta^jQ_{t-j}$ is the normalized memory Gramian. For the recent-memory truncation $\widetilde G_{t,m}$, we prove the exact Weyl support certificate $$\frac{s_4(K_t)}{s_1(K_t)}
   \ge
   \frac{\bigl(\widehat s_4-\delta_{t,m}\bigr)_+}
        {\widehat s_1+\delta_{t,m}},
   \qquad
   \delta_{t,m}=\frac{\eta^m(1-\eta^{t-m+1})}{1-\eta},
   \label{eq:abstract-certificate}$$ whenever $m\le t$, with zero tail for a complete history. Here $\widehat s_j$ are the singular values of $\widehat K_{t,m}=(I-P)\widetilde G_{t,m}V$. Equivalently, the support is certified at threshold $\tau$ when $\widehat s_4-\tau\widehat s_1\ge(1+\tau)\delta_{t,m}$. The RH-95 identity $\widehat K_{t,m}^*\widehat K_{t,m}=\widehat M_2-\widehat A^2$ shows that only the first two packet moments are needed for this exact finite-dimensional test; the third moment remains necessary for the full Ritz block but not for support.

  On the 120 source-seeded updates at the five archived scales, a five-snapshot audit certifies every one of the 78 updates on the two finest scales for all three cutoffs $10^{-8},10^{-6},10^{-4}$. The smallest certified fine-scale ratio is $7.36045\times10^{-4}$, giving a minimum margin of $7.36045$ at $\tau=10^{-4}$. The moment identity is exact, but binary64 moment subtraction becomes unreliable in weak branches, with a largest observed relative discrepancy $0.7272$; the support certificate therefore uses the direct recent cross action and treats moments as an algebraic reduction and consistency audit.

  The result is conditional rather than all-level. We give an exact barrier family of trace-one normalized snapshots whose memory clock, packet block, complement block, and first three cross singular values are fixed while $s_4/s_1=\varepsilon/4\to0$. Thus generic positivity, trace normalization, finite memory, and source seeding do not imply a positive fourth-cross lower bound. An additional physical transversality or volume law is required. No unconditional fine-support separation, Stage A theorem, Hilbert--Polya operator, zero identification, or Riemann Hypothesis result is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Finite-Memory Fourth-Cross Support\
  A Weyl Certificate, Reduced Moments, and a Normalized-Memory Barrier
```

## Markdown 正文

**Keywords:** projected-cross singular values; finite memory; Weyl perturbation; reduced moments; source-seeded packet; nondegeneracy barrier.

**MSC 2020:** 15A18; 47A75; 65F15; 65G20; 37M25.

# Introduction

The source-seeded route of RH-94 carries a low-dimensional packet through a complete frozen prefix by repeatedly enriching it with projected-cross directions [@WangSourceSeeded2026]. RH-95 removed the ambient cross spectral solve algebraically [@WangReducedCross2026]: if $A=V^*GV$ and $M_j=V^*G^jV$, then $$K^*K=M_2-A^2,
 \qquad K=(I-VV^*)GV.
 \label{eq:rh95}$$ RH-101 removed ambient Gram assembly from the packet action [@WangFiniteMemory2026]. For normalized snapshot Gramians $Q_t$ and $0\le\eta<1$, $$G_tV=\sum_{j=0}^{m-1}\eta^jQ_{t-j}V+\eta^mG_{t-m}V.
 \label{eq:rh101}$$ RH-107 then isolated the remaining fine-scale question [@WangSupportLaw2026]. For a maximum width-four selector, no quotient is proposed exactly when $s_4(K_t)/s_1(K_t)\ge\tau$.

The two earlier identities look close to closing this gate, but they solve different problems. Equation [\[eq:rh95\]](#eq:rh95){reference-type="eqref" reference="eq:rh95"} is an exact measurement identity; it does not make the smallest eigenvalue of $M_2-A^2$ positive. Equation [\[eq:rh101\]](#eq:rh101){reference-type="eqref" reference="eq:rh101"} is an exact memory decomposition; its positive tail controls the error between a recent cross and the full cross, but it does not prevent the recent cross itself from becoming rank deficient.

This paper joins the two facts in the strongest elementary way. A singular value perturbation theorem turns a recent fourth-cross margin into a full memory support certificate. The certificate is useful on the two finest archived scales. A separate exact construction proves that no positive margin can follow from the generic normalized-memory data alone.

The contributions are:

1.  a finite-memory Weyl certificate for the relative fourth-cross ratio;

2.  a reduced-moment realization showing that support needs only $M_1$ and $M_2$, while $M_3$ belongs to the downstream Ritz compression;

3.  a sharpness observation for the perturbation radius;

4.  an exact source-seeded normalized-memory barrier with $s_4/s_1\to0$ and fixed diagonal memory data;

5.  a five-snapshot audit connecting the certificate to the RH-107 fine-support boundary.

# Memory cross operators {#sec:setting}

Let $\mathcal K=\mathbb R^d$ (the complex case is identical), let $V\in\mathbb R^{d\times r}$ satisfy $V^*V=I_r$, and put $P=VV^*$. A normalized snapshot Gramian has the form $$Q_j=\frac{X_j^*X_j}{\left\lVert X_j\right\rVert_F^2},
 \qquad Q_j\succeq0,
 \qquad \operatorname{tr}Q_j=1.
 \label{eq:snapshot}$$ The finite-memory recursion is $$G_{-1}=0,
 \qquad G_t=Q_t+\eta G_{t-1},
 \qquad 0\le\eta<1.
 \label{eq:memory}$$ The projected-cross operator at time $t$ is $$K_t=(I-P)G_tV.
 \label{eq:fullcross}$$ For $m\ge1$, define the recent operator and its cross by $$\begin{aligned}
 \widetilde G_{t,m}&=\sum_{j=0}^{m-1}\eta^jQ_{t-j},
 \label{eq:recentgram}\\
 \widehat K_{t,m}&=(I-P)\widetilde G_{t,m}V.
 \label{eq:recentcross}\end{aligned}$$ If $m>t+1$, the sum is understood to stop at $j=t$.

Iterating [\[eq:memory\]](#eq:memory){reference-type="eqref" reference="eq:memory"} gives $$G_t-\widetilde G_{t,m}=\eta^mG_{t-m}
 \quad (m\le t),
 \label{eq:tailidentity}$$ and the difference is zero for a complete history. Since every $Q_j$ has unit trace, $$\operatorname{tr}G_u=\frac{1-\eta^{u+1}}{1-\eta}
 \le\frac1{1-\eta}.
 \label{eq:traceclock}$$ The crucial point for singular values is that the packet is an isometry: the operator norm, rather than the Frobenius norm, is enough.

# The finite-memory support certificate {#sec:certificate}

Write $\widehat s_1\ge\widehat s_2\ge\cdots$ for the singular values of $\widehat K_{t,m}$ and $s_1\ge s_2\ge\cdots$ for those of $K_t$.

[\[thm:weyl\]]{#thm:weyl label="thm:weyl"} For $m\le t$, define $$\delta_{t,m}
 =\eta^m\frac{1-\eta^{t-m+1}}{1-\eta}.
 \label{eq:delta}$$ Then $$\left\lVert K_t-\widehat K_{t,m}\right\rVert_2\le\delta_{t,m},
 \label{eq:crossperturbation}$$ and, whenever $\widehat s_4>\delta_{t,m}$, $$\frac{s_4}{s_1}
 \ge
 \frac{\widehat s_4-\delta_{t,m}}
      {\widehat s_1+\delta_{t,m}}.
 \label{eq:ratio-bound}$$ For $m=t+1$, take $\delta_{t,m}=0$ and $\widehat K_{t,m}=K_t$.

By [\[eq:tailidentity\]](#eq:tailidentity){reference-type="eqref" reference="eq:tailidentity"}, $$\begin{aligned}
 K_t-\widehat K_{t,m}
 &=(I-P)\eta^mG_{t-m}V.\end{aligned}$$ Orthogonal projection and multiplication by an isometry are nonexpansive in operator norm. Since a positive semidefinite matrix is bounded in operator norm by its trace, $$\begin{aligned}
 \left\lVert K_t-\widehat K_{t,m}\right\rVert_2
 &\le\eta^m\left\lVert G_{t-m}\right\rVert_2
 \le\eta^m\operatorname{tr}G_{t-m}
 =\delta_{t,m}.\end{aligned}$$ Weyl's singular-value perturbation inequality [@Bhatia1997; @StewartSun1990] gives $$s_j\ge\widehat s_j-\delta_{t,m},
 \qquad
 s_j\le\widehat s_j+\delta_{t,m}.$$ Applying these statements for $j=4$ and $j=1$ proves [\[eq:ratio-bound\]](#eq:ratio-bound){reference-type="eqref" reference="eq:ratio-bound"}.

[\[cor:threshold\]]{#cor:threshold label="cor:threshold"} For a relative cutoff $\tau>0$, the full cross satisfies $s_4/s_1\ge\tau$ whenever $$\widehat s_4-\tau\widehat s_1
 \ge (1+\tau)\delta_{t,m}.
 \label{eq:margin}$$ Thus [\[eq:margin\]](#eq:margin){reference-type="eqref" reference="eq:margin"} is a sufficient no-quotient certificate for the maximum-width-four selector.

Rearranging [\[eq:ratio-bound\]](#eq:ratio-bound){reference-type="eqref" reference="eq:ratio-bound"} gives exactly [\[eq:margin\]](#eq:margin){reference-type="eqref" reference="eq:margin"}. The adaptive support equivalence of RH-107 then implies that the selector keeps width four.

The operator-norm tail in Theorem [\[thm:weyl\]](#thm:weyl){reference-type="ref" reference="thm:weyl"} is sharper for support than the Frobenius packet-action estimate from RH-101. The latter contains a $\sqrt r$ factor because it bounds a matrix in Frobenius norm; singular-value perturbation needs only the operator norm of the positive tail.

[\[prop:sharp\]]{#prop:sharp label="prop:sharp"} Fix $a>b>\delta\ge0$ and set $$\widehat K=\operatorname{diag}(a,a,a,b),
 \qquad E=-\delta e_4e_4^*.$$ Then $\left\lVert E\right\rVert_2=\delta$ and the fourth singular value of $\widehat K+E$ is $b-\delta$. Hence no lower bound based only on $(\widehat s_4,\left\lVert E\right\rVert_2)$ can improve the numerator $(\widehat s_4-\delta)_+$ in general.

The matrices are diagonal and their singular values are displayed directly.

# Reduced moments and what they do not prove {#sec:moments}

For any positive semidefinite $H$ and packet $V$, define $$A_H=V^*HV,
 \qquad M_{2,H}=V^*H^2V,
 \qquad K_H=(I-P)HV.$$ The RH-95 calculation gives the exact identity $$C_H:=K_H^*K_H=M_{2,H}-A_H^2\succeq0.
 \label{eq:momentcross}$$ Consequently, for the recent memory, $$\widehat s_j^2
 =\lambda_j\!\left(
 V^*\widetilde G_{t,m}^{\,2}V
 -(V^*\widetilde G_{t,m}V)^2
 \right).
 \label{eq:moment-eigen}$$ The support certificate can therefore be evaluated in three algebraically equivalent ways:

1.  form the thin action $\widetilde G_{t,m}V$ and take the SVD of its projected cross;

2.  form the small matrix $C_H$ and diagonalize it;

3.  use a validated enclosure for either of the preceding objects.

The first two are not numerically interchangeable. The difference $M_{2,H}-A_H^2$ can be much smaller than either summand. The exact identity does not prevent cancellation [@Higham2002]. The third moment $$N_H=V^*H^3V-M_{2,H}A_H-A_HM_{2,H}+A_H^3
 \label{eq:thirdmoment}$$ is needed to assemble the complement Ritz block in RH-95, but it is not needed to decide whether the fourth cross mode is supported. This separates the current gate from the downstream Ritz-conditioning problem.

Equation [\[eq:momentcross\]](#eq:momentcross){reference-type="eqref" reference="eq:momentcross"} says that the fourth mode is exactly measurable from reduced moments. It does not imply $\lambda_4(C_H)>0$, let alone a scale-uniform lower bound for $\lambda_4(C_H)/\lambda_1(C_H)$. Such a lower bound is a separate nondegeneracy statement.

# An exact normalized-memory barrier {#sec:barrier}

We now show that generic assumptions used by RH-95 and RH-101 cannot supply the missing nondegeneracy. Let $V=[e_1,e_2,e_3,e_4]$ in $\mathbb R^8$ and let $U=[e_5,e_6,e_7,e_8]$. For $0\le\varepsilon\le1$, define $$D_\varepsilon=\operatorname{diag}(4,3,2,\varepsilon),
 \qquad
 Q_\varepsilon=\frac1{34}
 \begin{pmatrix}
 I_4&D_\varepsilon\\
 D_\varepsilon&\operatorname{diag}(16,9,4,1)
 \end{pmatrix}.
 \label{eq:qbarrier}$$

[\[thm:barrier\]]{#thm:barrier label="thm:barrier"} The matrix $Q_\varepsilon$ is a trace-one positive semidefinite snapshot Gramian. Let $$Q_{\mathrm{src}}=\frac1{12}\operatorname{diag}(2,2,2,2,1,1,1,1),
 \qquad G_1=Q_\varepsilon+\eta Q_{\mathrm{src}}.
 \label{eq:barriermemory}$$ The unique leading rank-four packet of $Q_{\mathrm{src}}$ is $V$. With this source packet, $$\begin{aligned}
 \operatorname{tr}G_1&=1+\eta,
 \\
 V^*G_1V&=\left(\frac1{34}+\frac\eta6\right)I_4,
 \\
 U^*G_1U&=\frac1{34}\operatorname{diag}(16,9,4,1)+\frac\eta{12}I_4,
 \label{eq:barrierblocks}
 \\
 s(K_1)&=\frac1{34}(4,3,2,\varepsilon),
 \\
 \frac{s_4(K_1)}{s_1(K_1)}&=\frac\varepsilon4.
 \label{eq:barrierratio}\end{aligned}$$ In particular, the memory clock and both diagonal packet/complement blocks are independent of $\varepsilon$, while the fourth-cross ratio can be zero.

The block matrix in [\[eq:qbarrier\]](#eq:qbarrier){reference-type="eqref" reference="eq:qbarrier"} is the sum of four rank-one or positive two-by-two blocks. More explicitly, define the $5\times8$ matrix whose rows are $$e_1^*+4e_5^*,\quad e_2^*+3e_6^*,\quad
 e_3^*+2e_7^*,\quad e_4^*+\varepsilon e_8^*,\quad
 \sqrt{1-\varepsilon^2}\,e_8^*.
 \label{eq:factorbarrier}$$ Its squared Frobenius norm is $34$, and its normalized Gramian is exactly $Q_\varepsilon$. Thus $Q_\varepsilon\succeq0$ and $\operatorname{tr}Q_\varepsilon=1$.

The source matrix $Q_{\mathrm{src}}$ has eigenvalue $2/12$ on $\operatorname{Ran}V$ and $1/12$ on its complement, so its top rank-four packet is $V$. Since $Q_{\mathrm{src}}$ has no packet/complement cross block, the cross of $G_1$ is the cross of $Q_\varepsilon$: $$(I-P)G_1V=UD_\varepsilon/34.$$ The remaining identities follow by taking the displayed blocks and singular values.

The construction is compatible with the finite-memory snapshot class, not with a claim about the specific folded-Gaussian production operator. If an actual one-step matrix realization is desired, take square state factors of $Q_{\mathrm{src}}$ and $Q_\varepsilon$ and set $A=cQ_\varepsilon^{1/2}Q_{\mathrm{src}}^{-1/2}$ with $c>0$ small enough that $\rho(A)<1$; multiplying a state by $c$ does not change its normalized snapshot Gramian. The barrier therefore identifies missing physical input, not a failure of the finite-memory algebra.

The barrier also clarifies the role of moments. The full matrix $M_2-A^2$ changes in its fourth direction as $\varepsilon$ changes, so exact moments can detect the collapse. What they do not provide automatically is a lower bound on that changing eigenvalue. Any all-level proof must control that eigenvalue by a model-specific transversality, determinant, or volume estimate.

# Five-scale certificate audit {#sec:audit}

We replay the two source-seeded channels at $$\sigma\in\{0.16,0.08,0.04,0.02,0.01\}$$ using the RH-94 frozen horizons and the RH-96 adaptive packet updates [@WangWeakMode2026]. The memory parameter is $\eta=1/512$, the recent depth is $m=5$, and the three relative cutoffs are $10^{-8},10^{-6},10^{-4}$. At each update we compute the recent cross action, apply Theorem [\[thm:weyl\]](#thm:weyl){reference-type="ref" reference="thm:weyl"}, and compare the certificate with the full assembled cross. The full chain is used only as the finite comparator and to continue the inherited packet; the certificate itself uses the recent action.

The exact geometric tail bound is evaluated first. To protect the finite binary64 comparison against summation error, the audit adds an absolute $2\times10^{-14}$ action guard. Every observed full-minus-recent cross error lies below this guarded bound. This is a finite numerical guard, not an all-level rounding theorem [@Rump2010].

::: {#tab:counts}
  threshold     $0.16$    $0.08$    $0.04$    $0.02$    $0.01$  fine margin
  ----------- -------- --------- --------- --------- --------- -------------
  $10^{-8}$      $4/8$   $11/12$   $20/22$   $34/34$   $44/44$   $7.36045$
  $10^{-6}$      $1/8$   $10/12$   $20/22$   $34/34$   $44/44$   $736.045$
  $10^{-4}$      $0/8$    $4/12$   $16/22$   $34/34$   $44/44$   $7.36045$

  : Certified support counts. Each entry is the number of updates whose five-snapshot lower bound clears the indicated threshold, out of the total updates at that scale (two channels combined). The last two scales are fully certified for every threshold.
:::

There are 360 threshold-update records. On the fine pair $\sigma\in\{0.02,0.01\}$, all 234 threshold-update records are certified; equivalently, all 78 physical updates clear all three cutoffs. The minimum certified ratio over the fine records is $$7.3604523\times10^{-4},
 \label{eq:finevalue}$$ which occurs at $\tau=10^{-4}$ on the finest right channel. The maximum analytic tail bound is $2.84774\times10^{-14}$; after the binary64 guard it is $4.84774\times10^{-14}$. No selector-equivalence failure and no observed tail-bound failure occurred.

The reduced-moment audit tells a complementary story. The largest relative discrepancy between the moment evaluation of $\widehat K^*\widehat K$ and the direct recent-cross Gramian is $0.7272$, and the largest cancellation index is $3.89\times10^{15}$. These are not failures of [\[eq:momentcross\]](#eq:momentcross){reference-type="eqref" reference="eq:momentcross"}; they are failures of naive binary64 subtraction in the weak regime. Direct thin actions are therefore the numerically stable implementation of the exact certificate on this dataset.

![Left: minimum five-snapshot lower bounds at the five archived scales; dashed lines are the three selector cutoffs. Right: the exact normalized-memory barrier has fixed diagonal memory data while its fourth cross ratio follows $\varepsilon/4$ to zero.](<../../../../../zeta_mvp0/papers/RH-108-finite-memory-fourth-cross-support/figures/finite_memory_fourth_cross_support.pdf>){#fig:audit width="\\textwidth"}

# Route consequence and claim boundary {#sec:route}

RH-108 closes one conditional implication that was previously implicit: $$\begin{gathered}
 \text{recent fourth-cross margin}\\[-2pt]
 +\ \text{positive finite-memory tail bound}
 \end{gathered}
 \quad\Longrightarrow\quad
 \text{full-memory no-quotient support}.
 \label{eq:route}$$ This is enough to certify the last two archived scales and explains why the observed RH-107 fine boundary is numerically robust. It does not yet make that boundary uniform in the level.

The exact barrier identifies the missing theorem in a sharper form. One must prove, for the physical source-seeded family, a lower bound of the type $$\widehat s_4-\tau\widehat s_1
 \ge (1+\tau)\delta_{t,m}+\Gamma_t,
 \qquad \Gamma_t\ge0,
 \label{eq:openlaw}$$ on all sufficiently fine levels, or replace it with a model-specific volume or determinant estimate that implies the same inequality. Generic trace normalization, positivity, source packet rank, and finite-memory decay do not control $\Gamma_t$.

The claim boundary is therefore:

1.  proved: the finite-memory Weyl support certificate;

2.  proved: exact realization through the first two reduced moments;

3.  proved: the normalized-memory/source-seed barrier;

4.  validated: all fine updates at the two smallest archived scales;

5.  open: an all-level physical fourth-cross lower bound;

6.  open: unconditional fine-support separation and closure of the quotient supply;

7.  not addressed: a Hilbert--Polya operator, zeta-zero identification, a prime-power trace formula, or the Riemann Hypothesis.

In particular, the present result moves the route forward by converting the next analytic task into a concrete nondegeneracy problem. If that problem is solved for the physical folded-Gaussian family, RH-107's finite coarse support reduction applies. If it is not, the barrier explains exactly why the generic moment/memory architecture cannot substitute for it.

# Reproducibility

The directory contains the certificate helpers, exact barrier constructor, full and smoke audits, figures, tests, and hash-checked archive. Run:

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_support_certificate_audit.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_support_certificate_audit.py --smoke
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/make_figures.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/pytest -q -p no:cacheprovider
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
    cp main.pdf finite-memory-fourth-cross-support.pdf
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_archive.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/verify_archive.py
