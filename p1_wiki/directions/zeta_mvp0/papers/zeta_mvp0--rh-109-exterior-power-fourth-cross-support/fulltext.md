---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-109-exterior-power-fourth-cross-support"
canonical_tex: "zeta_mvp0/papers/RH-109-exterior-power-fourth-cross-support/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-109-exterior-power-fourth-cross-support/main.pdf"
source_sha256: "b42c51a1b8041cf1528ff050f323210ac28c715e76397267073657d0d093b21a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exterior-Power Fourth-Cross Support Finite-Memory Volume Certificates and a Sharp Scalar-Volume Barrier

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-109-exterior-power-fourth-cross-support>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-109-exterior-power-fourth-cross-support/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-109-exterior-power-fourth-cross-support/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-109-exterior-power-fourth-cross-support/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-109-exterior-power-fourth-cross-support/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-108 reduced eventual source-seeded support to a physical lower bound for the fourth projected-cross singular ratio. This paper tests the first determinantal surrogate for that missing statement.

  Let $K_t=(I-VV^*)G_tV$ be the projected cross, let $s_1\ge\cdots\ge s_r\ge0$ be its singular values, and put $$q_4(K_t)=\frac{s_4}{s_1},
   \qquad
   \nu_4(K_t)=\frac{\left\lVert\wedge^4K_t\right\rVert_2}{s_1^4}
   =\frac{s_1s_2s_3s_4}{s_1^4}.$$ For a depth-$m$ recent cross with singular values $\widehat s_j$ and the positive memory-tail radius $\delta$, we prove the finite-memory spectral exterior certificate $$q_4(K_t)\ge\nu_4(K_t)\ge
   \frac{\prod_{j=1}^4(\widehat s_j-\delta)_+}
        {(\widehat s_1+\delta)^4}.$$ We also prove a reduced trace exterior certificate. If $D_r=\binom r4$, it is $$q_4(K_t)\ge
   \frac{\bigl[\operatorname{e}_4((\widehat s_1-\delta)_+^2,\ldots,
   (\widehat s_r-\delta)_+^2)/D_r\bigr]^{1/2}}
        {(\widehat s_1+\delta)^4}.$$ The distinction is structural: for $C=K^*K=M_2-A^2$, the spectral four-volume squared is $\lambda_{\max}(\wedge^4C)$, whereas $\operatorname{e}_4(C)=\operatorname{tr}(\wedge^4C)$ is the Frobenius four-volume squared. They coincide with $\det C$ only when the packet rank is four.

  On the two finest archived scales, the spectral certificate covers $78/78$, $72/78$, and $55/78$ updates at cutoffs $10^{-8},10^{-6},10^{-4}$; the trace certificate covers $78/78$, $65/78$, and $42/78$. The minimum fine spectral lower bound is $5.10911\times10^{-8}$. Finally, we prove the sharp scalar-volume interval $$\nu_4\le q_4\le\nu_4^{1/3}$$ and realize both endpoints by trace-one source-seeded memory families with the same scalar volume, trace clock, packet block, and complement block. Thus exterior volume closes the archived $10^{-8}$ gate but cannot by itself recover stronger fourth-mode support in the intermediate information band. No all-level Stage A, Hilbert--Polya operator, zero identification, or Riemann Hypothesis result is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Exterior-Power Fourth-Cross Support\
  Finite-Memory Volume Certificates and a Sharp Scalar-Volume Barrier
```

## Markdown 正文

**Keywords:** projected-cross singular values; exterior power; four-volume; elementary symmetric polynomial; finite memory; support barrier.

**MSC 2020:** 15A18; 15A75; 47A75; 65F15; 37M25.

# Introduction

The source-seeded route updates a low-dimensional right packet through a frozen physical prefix by adjoining projected-cross directions [@WangSourceSeeded2026; @WangWeakMode2026]. The reduced identity of RH-95 removes the ambient cross solve: $$K^*K=M_2-A^2,
 \qquad
 A=V^*GV,
 \qquad M_2=V^*G^2V.
 \label{eq:reduced-intro}$$ RH-101 supplies a finite-memory action formula, and RH-108 converts its positive tail into a direct Weyl certificate for $s_4/s_1$ [@WangReducedCross2026; @WangFiniteMemory2026; @WangFourthCross2026]. The remaining all-level input is physical nondegeneracy: why should the recent fourth mode stay large enough?

A four-column determinant or exterior volume is the first natural surrogate. It vanishes exactly at rank loss and is intrinsic under changes of packet coordinates. Two cautions are necessary. First, a normalized four-volume contains the second and third relative singular ratios in addition to the fourth. Second, when the packet rank exceeds four, $\operatorname{e}_4(K^*K)$ is a sum of squared four-volumes, not the leading four-volume itself. Ignoring either distinction makes a determinant argument appear stronger than it is.

This paper makes the exterior route exact. Its contributions are:

1.  a finite-memory spectral exterior certificate for the fourth ratio;

2.  a trace certificate expressed by $\operatorname{e}_4(M_2-A^2)$ with the exact exterior-dimension penalty;

3.  a sharp scalar-volume inversion theorem and an admissible source-seeded realization of both endpoints;

4.  a five-scale audit locating precisely which support thresholds are closed by volume and which remain open.

# Projected crosses and two four-volumes {#sec:setting}

Let $V\in\mathbb R^{d\times r}$ satisfy $V^*V=I_r$, put $P=VV^*$, and let $H\succeq0$. The projected cross is $$K_H=(I-P)HV.
 \label{eq:cross}$$ Write its singular values as $s_1\ge s_2\ge\cdots\ge s_r\ge0$, padding by zero if necessary, and assume $s_1>0$. Define $$q_4(K_H)=\frac{s_4}{s_1},
 \qquad
 \nu_4(K_H)=\frac{\left\lVert\wedge^4K_H\right\rVert_2}{s_1^4}
 =\frac{s_1s_2s_3s_4}{s_1^4}.
 \label{eq:qnu}$$ The second quantity is the normalized *spectral* four-volume. The normalized trace or Frobenius four-volume is $$\phi_4(K_H)
 =\frac{\left\lVert\wedge^4K_H\right\rVert_F}{s_1^4}
 =\frac{\bigl[\operatorname{e}_4(s_1^2,\ldots,s_r^2)\bigr]^{1/2}}{s_1^4}.
 \label{eq:phi}$$ Here $\operatorname{e}_4$ is the fourth elementary symmetric polynomial. Since $\wedge^4K_H$ has at most $$D_r=\binom r4
 \label{eq:dimension}$$ singular values, the operator/Frobenius inequalities give $$\frac{\phi_4}{\sqrt{D_r}}\le\nu_4\le\phi_4.
 \label{eq:operator-frobenius}$$

For the memory recursion, let $$G_t=Q_t+\eta G_{t-1},
 \qquad G_{-1}=0,
 \qquad Q_t\succeq0,
 \qquad \operatorname{tr}Q_t=1,
 \qquad 0\le\eta<1.
 \label{eq:memory}$$ At depth $m$, set $$\widetilde G_{t,m}=\sum_{j=0}^{m-1}\eta^jQ_{t-j},
 \qquad
 \widehat K_{t,m}=(I-P)\widetilde G_{t,m}V.
 \label{eq:recent}$$ For $m\le t$, RH-108 proves $$\left\lVert K_t-\widehat K_{t,m}\right\rVert_2\le
 \delta_{t,m}:=eta^m\frac{1-\eta^{t-m+1}}{1-\eta};
 \label{eq:tail}$$ the tail is zero when the recent window contains the complete history.

# Finite-memory exterior certificates {#sec:certificates}

Let $\widehat s_1\ge\cdots\ge\widehat s_r$ be the singular values of the recent cross. For any certified radius $\delta\ge
\left\lVert K_t-\widehat K_{t,m}\right\rVert_2$, define $$\ell_j=(\widehat s_j-\delta)_+,
 \qquad u_1=\widehat s_1+\delta.
 \label{eq:ell}$$

[\[thm:spectral\]]{#thm:spectral label="thm:spectral"} If $s_1(K_t)>0$, then $$q_4(K_t)\ge\nu_4(K_t)\ge
 B_4^{\mathrm{sp}}
 :=\frac{\ell_1\ell_2\ell_3\ell_4}{u_1^4}.
 \label{eq:spectral-certificate}$$ Consequently, $B_4^{\mathrm{sp}}\ge\tau$ is a sufficient no-quotient support certificate at relative cutoff $\tau$.

Singular-value perturbation gives $s_j(K_t)\ge(\widehat s_j-\delta)_+=\ell_j$ and $s_1(K_t)\le\widehat s_1+\delta=u_1$ [@Bhatia1997; @StewartSun1990]. Therefore $$\nu_4(K_t)
 =\frac{\prod_{j=1}^4s_j(K_t)}{s_1(K_t)^4}
 \ge\frac{\prod_{j=1}^4\ell_j}{u_1^4}.$$ Also $\nu_4=(s_2/s_1)(s_3/s_1)q_4\le q_4$. This proves both inequalities. The support implication follows from the selector equivalence in RH-107 [@WangSupportLaw2026].

The spectral certificate is simply the multiplicative form of four Weyl inequalities. It is weaker than the direct RH-108 ratio bound because it also pays for the first three relative singular factors. Its advantage is structural: it is a coordinate-free exterior nondegeneracy target that can in principle be estimated from determinants, wedge products, or reduced moments.

[\[thm:trace\]]{#thm:trace label="thm:trace"} Let $D_r=\binom r4$. Under the assumptions of [\[thm:spectral\]](#thm:spectral){reference-type="ref" reference="thm:spectral"}, $$q_4(K_t)\ge
 B_4^{\mathrm{tr}}
 :=\frac{\bigl[\operatorname{e}_4(\ell_1^2,\ldots,\ell_r^2)/D_r\bigr]^{1/2}}
          {u_1^4}.
 \label{eq:trace-certificate}$$ Moreover, $$0\le B_4^{\mathrm{tr}}\le B_4^{\mathrm{sp}}.
 \label{eq:trace-order}$$ At packet rank $r=4$, the two certificates coincide.

Coordinatewise Weyl bounds imply $$\operatorname{e}_4(s_1(K_t)^2,\ldots,s_r(K_t)^2)
 \ge \operatorname{e}_4(\ell_1^2,\ldots,\ell_r^2).$$ Apply the left inequality in [\[eq:operator-frobenius\]](#eq:operator-frobenius){reference-type="eqref" reference="eq:operator-frobenius"}, followed by the upper bound $s_1(K_t)\le u_1$, to obtain [\[eq:trace-certificate\]](#eq:trace-certificate){reference-type="eqref" reference="eq:trace-certificate"}. Every four-fold product in $\operatorname{e}_4(\ell_1^2,\ldots,\ell_r^2)$ is at most $\ell_1^2\ell_2^2\ell_3^2\ell_4^2$. Averaging over the $D_r$ products proves [\[eq:trace-order\]](#eq:trace-order){reference-type="eqref" reference="eq:trace-order"}. If $r=4$, there is one product and equality holds.

The binomial factor is not a numerical convenience. It is the exact price of converting a trace on the fourth exterior space into its leading eigenvalue without any concentration information.

# Reduced moments: spectral versus trace exterior data {#sec:moments}

For $H\succeq0$, define $$A_H=V^*HV,
 \qquad M_{2,H}=V^*H^2V,
 \qquad C_H=K_H^*K_H.$$ The RH-95 identity is $$C_H=M_{2,H}-A_H^2\succeq0.
 \label{eq:moment}$$ Let $\lambda_1\ge\cdots\ge\lambda_r\ge0$ be the eigenvalues of $C_H$. Then $\lambda_j=s_j^2$, and exterior functoriality gives $$\begin{aligned}
 \left\lVert\wedge^4K_H\right\rVert_2^2
 &=\lambda_{\max}(\wedge^4C_H)
 =\lambda_1\lambda_2\lambda_3\lambda_4,
 \label{eq:spectral-moment}\\
 \left\lVert\wedge^4K_H\right\rVert_F^2
 &=\operatorname{tr}(\wedge^4C_H)
 =\operatorname{e}_4(C_H)
 =\sum_{|I|=4}\prod_{i\in I}\lambda_i.
 \label{eq:trace-moment}\end{aligned}$$ These standard exterior-power identities may be read directly from the singular values of $\wedge^4K_H$ [@HornJohnson1991].

Equations [\[eq:spectral-moment\]](#eq:spectral-moment){reference-type="eqref" reference="eq:spectral-moment"} and [\[eq:trace-moment\]](#eq:trace-moment){reference-type="eqref" reference="eq:trace-moment"} are equal only in special cases. If $r=4$, both are $\det C_H$. If $r>4$, $\operatorname{e}_4(C_H)$ is the sum of all principal four-by-four minors; it is not the leading exterior eigenvalue. For trace-only evaluation one may use Newton's identity $$\operatorname{e}_4(C)=\frac{p_1^4-6p_1^2p_2+3p_2^2+8p_1p_3-6p_4}{24},
 \qquad p_j=\operatorname{tr}(C^j).
 \label{eq:newton}$$ No moments of $H$ beyond $A_H$ and $M_{2,H}$ are algebraically needed once $C_H$ has been formed.

This is an exact reduction, not an automatic positivity theorem. It also does not remove floating-point cancellation in $M_{2,H}-A_H^2$. As in RH-108, the finite audit therefore evaluates the recent thin cross directly and uses [\[eq:moment\]](#eq:moment){reference-type="eqref" reference="eq:moment"} as an algebraic identification and consistency check [@Higham2002].

# A sharp scalar-volume information barrier {#sec:barrier}

The normalized spectral volume factors exactly as $$\nu_4=\alpha_2\alpha_3q_4,
 \qquad \alpha_j=\frac{s_j}{s_1}.
 \label{eq:lossfactor}$$ The missing factor $\alpha_2\alpha_3$ quantifies how much a scalar four-volume loses relative to the fourth singular ratio.

[\[thm:interval\]]{#thm:interval label="thm:interval"} For every projected cross with $s_1>0$, $$\nu_4\le q_4\le\nu_4^{1/3}.
 \label{eq:sharpinterval}$$ Both endpoints are sharp for every $0\le\nu_4\le1$.

The singular ordering gives $1\ge\alpha_2\ge\alpha_3\ge q_4\ge0$. Hence $$q_4^3\le\alpha_2\alpha_3q_4=\nu_4\le q_4,$$ which is equivalent to [\[eq:sharpinterval\]](#eq:sharpinterval){reference-type="eqref" reference="eq:sharpinterval"}. For a prescribed $\nu\in[0,1]$, the spectrum $(1,1,1,\nu)$ attains $q_4=\nu$, while $(1,\nu^{1/3},\nu^{1/3},\nu^{1/3})$ attains $q_4=\nu^{1/3}$. Both have normalized spectral volume $\nu$.

For a support threshold $\tau$, volume $\nu_4\ge\tau$ is sufficient and $q_4\ge\tau$ forces $\nu_4\ge\tau^3$. In the open band $$\tau^3<\nu_4<\tau,
 \label{eq:band}$$ the same scalar volume is compatible with both $q_4<\tau$ and $q_4>\tau$. No universal scalar-volume rule can decide support there.

The endpoint spectra can be embedded in the same normalized-memory class as the preceding route.

[\[thm:sourcebarrier\]]{#thm:sourcebarrier label="thm:sourcebarrier"} Let $V=[e_1,\ldots,e_4]$, $U=[e_5,\ldots,e_8]$, and for a diagonal $D=\operatorname{diag}(d_1,\ldots,d_4)$ with $0\le d_j\le1$ define $$Q_D=\frac18
 \begin{pmatrix}I_4&D\\D&I_4\end{pmatrix},
 \qquad
 Q_{\rm src}=\frac1{12}\operatorname{diag}(2I_4,I_4),
 \qquad
 G_D=Q_D+\eta Q_{\rm src}.
 \label{eq:barrierfamily}$$ Then $Q_D$ and $Q_{\rm src}$ are trace-one positive semidefinite snapshots, $V$ is the unique leading rank-four packet of $Q_{\rm src}$, and $$\begin{aligned}
 \operatorname{tr}G_D&=1+\eta,\nonumber\\
 V^*G_DV&=\left(\frac18+\frac\eta6\right)I_4,\nonumber\\
 U^*G_DU&=\left(\frac18+\frac\eta{12}\right)I_4,\label{eq:fixedblocks}\\
 (I-VV^*)G_DV&=\frac18UD.\nonumber\end{aligned}$$ For any $\nu\in[0,1]$, the choices $$D_{\rm lin}=\operatorname{diag}(1,1,1,\nu),
 \qquad
 D_{\rm cub}=\operatorname{diag}(1,\nu^{1/3},\nu^{1/3},\nu^{1/3})
 \label{eq:endpoints}$$ have the same normalized spectral volume $\nu$ and the same data in [\[eq:fixedblocks\]](#eq:fixedblocks){reference-type="eqref" reference="eq:fixedblocks"}, while their fourth ratios are respectively $\nu$ and $\nu^{1/3}$.

The eigenvalues of $Q_D$ are $(1\pm d_j)/8$, so it is positive semidefinite and has trace one. The assertions for $Q_{\rm src}$ are immediate from its two distinct diagonal eigenvalues. Block multiplication gives [\[eq:fixedblocks\]](#eq:fixedblocks){reference-type="eqref" reference="eq:fixedblocks"} and the displayed cross. Its singular values are $d_j/8$, so [\[eq:endpoints\]](#eq:endpoints){reference-type="eqref" reference="eq:endpoints"} realizes exactly the endpoint spectra from [\[thm:interval\]](#thm:interval){reference-type="ref" reference="thm:interval"}.

The barrier is compatible with generic normalized snapshots, source seeding, and one-step memory. It is not asserted to belong to the specific folded-Gaussian production family. Its role is to show exactly which additional physical information a better volume inversion would require.

# Five-scale exterior audit {#sec:audit}

We replay the RH-96 source-seeded chains at $$\sigma\in\{0.16,0.08,0.04,0.02,0.01\}$$ with the inherited RH-94 horizons, $\eta=1/512$, depth $m=5$, and cutoffs $10^{-8},10^{-6},10^{-4}$. Packet ranks range from four to seven. At each update we form the recent thin action, pay the analytic tail [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}, add the same absolute $2\times10^{-14}$ binary64 action guard as RH-108, and evaluate both exterior certificates. The full cross is formed only to continue the finite comparator and audit the implications. This is a guarded finite replay, not an all-level floating-point theorem [@Rump2010].

::: {#tab:counts}
  $\tau$        $0.16$   $0.08$    $0.04$    $0.02$    $0.01$   fine trace   fine Weyl
  ----------- -------- -------- --------- --------- --------- ------------ -----------
  $10^{-8}$      $1/8$   $5/12$   $15/22$   $34/34$   $44/44$      $78/78$     $78/78$
  $10^{-6}$      $0/8$   $3/12$   $10/22$   $31/34$   $41/44$      $65/78$     $78/78$
  $10^{-4}$      $0/8$   $2/12$    $8/22$   $23/34$   $32/44$      $42/78$     $78/78$

  : Exterior support counts. The five middle columns show the spectral certificate count at each scale. The last columns compare the trace and direct Weyl certificates on the two fine scales, which contain 78 updates for each threshold.
:::

There are 360 threshold-update records. On the two fine scales, the minimum spectral certificate is $$5.1091096\times10^{-8},
 \label{eq:minspec}$$ and the minimum trace certificate is $1.3191664\times10^{-8}$. Therefore both exterior routes close every fine update at $\tau=10^{-8}$. The corresponding minimum actual normalized volume is $5.1119586\times10^{-8}$, and the minimum actual fourth ratio is $7.3649339\times10^{-4}$.

The gap between these two scales is explained exactly by [\[eq:lossfactor\]](#eq:lossfactor){reference-type="eqref" reference="eq:lossfactor"}. The minimum observed fine loss factor is $$\min\alpha_2\alpha_3=5.2335553\times10^{-5},
 \label{eq:lossvalue}$$ while its maximum is $0.38764$. Thus a normalized four-volume can be roughly $2\times10^4$ smaller than the direct fourth ratio on the same archived chain. This is why the exterior certificate is complete at $10^{-8}$ but not at the larger cutoffs.

All spectral and trace certificate implications hold, all observed recent cross errors lie below the guarded tail, and all selector equivalences agree. The exact reduced moment identity remains numerically delicate: the largest binary64 discrepancy between $M_2-A^2$ and the direct recent cross Gramian is $0.7272$, with cancellation index $3.89\times10^{15}$. The audit therefore uses the thin SVD for numerical values and does not interpret unstable moment subtraction as a failure of the algebra.

![Left: minimum spectral and trace exterior lower bounds over the five archived scales; dashed lines are the selector cutoffs. Right: fine replay points lie inside the sharp scalar-volume interval. The two boundary curves are realized exactly by the source-seeded family in [\[thm:sourcebarrier\]](#thm:sourcebarrier){reference-type="ref" reference="thm:sourcebarrier"}.](figures/exterior_power_fourth_cross_support.pdf){#fig:audit width="\\textwidth"}

# Route consequence and claim boundary {#sec:route}

RH-109 gives a genuine positive result: a recent physical wedge estimate can be propagated through forgotten memory and becomes a valid fourth-mode support certificate. It also identifies two distinct losses: $$\underbrace{\operatorname{e}_4\ \longrightarrow\ \lambda_{\max}(\wedge^4C)}_{
 \text{exterior concentration, factor at most }\sqrt{D_r}}
 \qquad\text{and}\qquad
 \underbrace{\nu_4\ \longrightarrow\ q_4}_{
 \text{relative capacity }\alpha_2\alpha_3}.
 \label{eq:twolosses}$$ The first loss concerns the use of a trace moment instead of a spectral exterior value. The second is present even when the leading four-volume is known exactly.

The next analytic target is consequently sharper than "prove a determinant bound." One needs either

1.  a physical lower bound for $\nu_4$ together with an upper law for $\alpha_2\alpha_3$, so that $q_4=\nu_4/(\alpha_2\alpha_3)$; or

2.  a direct physical fourth-mode transversality estimate that bypasses scalar volume inversion.

If the reduced $\operatorname{e}_4$ route is used, exterior concentration must also be controlled to improve the generic binomial factor.

The claim boundary is:

1.  proved: the finite-memory spectral and trace exterior certificates;

2.  proved: the exact reduced-moment spectral/trace distinction;

3.  proved: the sharp scalar-volume interval and source-seeded barrier;

4.  validated: complete fine exterior support at $\tau=10^{-8}$ on the five archived scales;

5.  open: an all-level physical exterior lower bound and loss-factor law;

6.  open: unconditional fine-support separation and Stage A closure;

7.  not addressed: a Hilbert--Polya operator, zeta-zero identification, a prime-power trace formula, or the Riemann Hypothesis.

Thus the determinant route remains open, but only in a model-specific form. Generic exterior algebra supplies the correct certificate and also proves why a scalar volume cannot finish the route alone.

# Reproducibility

The directory contains the exterior bounds, exact barrier constructor, full and smoke audits, figures, tests, and hash-checked archive. Run:

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_exterior_support_audit.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_exterior_support_audit.py --smoke
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/make_figures.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/pytest -q -p no:cacheprovider
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
    cp main.pdf exterior-power-fourth-cross-support.pdf
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_archive.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/verify_archive.py
