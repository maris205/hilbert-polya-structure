---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-182-finite-temporal-clock-physical-audit"
canonical_tex: "zeta_mvp0/papers/RH-182-finite-temporal-clock-physical-audit/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-182-finite-temporal-clock-physical-audit/main.pdf"
source_sha256: "8e147faf2df6cec088b3820c36a4aa7fb10dc7f003fd4af82bd89fe54e2b953a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Data-Derived Finite Temporal Clock Exact Weighted-Cycle Kinematics and a 126-Window Physical Closure Audit

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-182-finite-temporal-clock-physical-audit>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-182-finite-temporal-clock-physical-audit/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-182-finite-temporal-clock-physical-audit/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-182-finite-temporal-clock-physical-audit/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-182-finite-temporal-clock-physical-audit/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-181 left two candidate routes from reset memory to a physical finite spectral cloud. The finite-cycle route had exact determinant algebra but no time-domain calibration. This paper constructs the most direct clock from the normalized physical source orbit, without fitting transfer eigenvalues.

  For a nonzero matrix orbit $S_{j+1}=AS_j$, write $x_j=S_j/\left\lVert S_j\right\rVert_{\mathrm F}$ and $a_j=\left\lVert S_{j+1}\right\rVert_{\mathrm F}/\left\lVert S_j\right\rVert_{\mathrm F}$. A length-$L$ temporal synthesis $J=[x_t,\ldots,x_{t+L-1}]$ is paired with the weighted cyclic shift whose chain weights are the observed $a_j$ and whose final edge has a unimodular orientation mark. The open chain intertwines exactly. All failure is concentrated in one wrap column, while the cyclic spectrum is an exact rotated root grid of radius $(\left\lVert S_{t+L}\right\rVert_{\mathrm F}/\left\lVert S_t\right\rVert_{\mathrm F})^{1/L}$. Polar orthogonalization preserves that spectrum by similarity and gives type-correct primal and adjoint residuals in the physical Frobenius space.

  The candidate lengths are fixed in advance by the RH-179 offsets $L=r-3$ and $L=r-4$. The admissible anchors are $\sigma=0.04,0.02,0.01$, two physical channels, and 126 temporal windows. An optimal projective orientation mark is allowed. The exact radius, phase, and polar identities have zero recorded failures. Nevertheless the minimum projective wrap distance is $0.3720$, the minimum primal residual is $0.2711$, and the minimum adjoint residual is $0.7143$. No window passes the common $0.25$ wrap/primal/adjoint gate.

  Thus the literal orthogonal temporal-clock realization is rejected on the available finite anchors, even after orientation marking. This is not an all-level no-go theorem and does not exclude separate right and left packets. That biorthogonal alternative is the next target. No physical Riesz shell, Gate A result, Hilbert--Polya operator, or Riemann-hypothesis conclusion is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  A Data-Derived Finite Temporal Clock\
  Exact Weighted-Cycle Kinematics and a 126-Window Physical Closure Audit
```

## Markdown 正文

# Position inside the physical interface

RH-171 decomposed the packet-to-Riesz interface into ambient realization, validated finite data, uniform margins, and shellwise transport [@WangRH171]. RH-172--181 then proved the finite history realization, rejected the literal infinite-history determinant, and identified an exact finite cyclic determinant model [@WangRH181]. The unresolved point was not cycle algebra. It was whether a clock of the required length is present in the physical time-domain data.

The protocol here is deliberately one-way:

1.  choose $L$ from the reset rank before examining target eigenvalues;

2.  construct the clock from normalized source states and their norms;

3.  allow only a time-domain endpoint orientation mark;

4.  measure wrap, primal, adjoint, radial, and phase defects;

5.  reject the orthogonal branch if no candidate passes one declared gate.

The construction cannot manufacture phase agreement by spectral regression: the root grid follows algebraically from the weighted cycle.

# Normalized orbit and temporal synthesis

Let $\mathcal H$ be the Frobenius Hilbert space of $n\times m$ matrices and let $\mathcal A X=AX$. Suppose $S_0\ne0$ and $S_j=\mathcal A^jS_0\ne0$ over the finite horizon under consideration. Define $$\label{eq:normalized-orbit}
 x_j=\frac{S_j}{\left\lVert S_j\right\rVert_{\mathrm F}},
 \qquad
 a_j=\frac{\left\lVert S_{j+1}\right\rVert_{\mathrm F}}{\left\lVert S_j\right\rVert_{\mathrm F}}.$$ Then $\left\lVert x_j\right\rVert_{\mathrm F}=1$ and $$\label{eq:normalized-step}
 \mathcal A x_j=a_jx_{j+1}.$$

For a start time $t$ and length $L\ge3$, define $$\label{eq:synthesis}
 J_{t,L}:\mathbb C^L\longrightarrow\mathcal H,
 \qquad
 J_{t,L}e_j=x_{t+j},\quad 0\le j<L.$$ Its Gram matrix is $G_{t,L}=J_{t,L}^*J_{t,L}$. Whenever $G_{t,L}>0$, the canonical polar frame is $$\label{eq:polar-frame}
 V_{t,L}=J_{t,L}G_{t,L}^{-1/2},
 \qquad V_{t,L}^*V_{t,L}=I_L.$$ This is the orthogonal temporal packet tested below.

# The weighted cycle and its exact spectrum

For $\omega\in\mathbb T$, define the weighted cyclic shift $$\begin{aligned}
 C_{t,L}(\omega)e_j&=a_{t+j}e_{j+1},&&0\le j<L-1,
 \label{eq:cycle-chain}\\
 C_{t,L}(\omega)e_{L-1}&=\omega a_{t+L-1}e_0.
 \label{eq:cycle-wrap}\end{aligned}$$

[\[thm:rank-one\]]{#thm:rank-one label="thm:rank-one"} The temporal synthesis satisfies $$\label{eq:rank-one-defect}
 \mathcal A J_{t,L}-J_{t,L}C_{t,L}(\omega)
 =a_{t+L-1}(x_{t+L}-\omega x_t)e_{L-1}^*.$$ In particular, every non-wrap column intertwines exactly and the defect has rank at most one.

For $j<L-1$, equations [\[eq:normalized-step\]](#eq:normalized-step){reference-type="eqref" reference="eq:normalized-step"} and [\[eq:cycle-chain\]](#eq:cycle-chain){reference-type="eqref" reference="eq:cycle-chain"} give $\mathcal A J_{t,L}e_j=a_{t+j}x_{t+j+1}
=J_{t,L}C_{t,L}(\omega)e_j$. For $e_{L-1}$ the two sides are $a_{t+L-1}x_{t+L}$ and $\omega a_{t+L-1}x_t$, respectively. Collecting the sole nonzero column gives [\[eq:rank-one-defect\]](#eq:rank-one-defect){reference-type="eqref" reference="eq:rank-one-defect"}.

[\[thm:root-grid\]]{#thm:root-grid label="thm:root-grid"} Let $$\label{eq:radius}
 \rho_{t,L}=
 \left(\prod_{j=0}^{L-1}a_{t+j}\right)^{1/L}
 =\left(\frac{\left\lVert S_{t+L}\right\rVert_{\mathrm F}}{\left\lVert S_t\right\rVert_{\mathrm F}}\right)^{1/L}.$$ Then $$\label{eq:cycle-power}
 C_{t,L}(\omega)^L=\omega\rho_{t,L}^L I_L,$$ and its eigenvalues are $$\label{eq:cycle-roots}
 \rho_{t,L}\exp\left(
 i\frac{\arg\omega+2\pi k}{L}
 \right),\qquad 0\le k<L.$$

Every basis vector traverses all $L$ directed edges in $L$ steps, acquiring the product of the $L$ positive weights and the single wrap phase. This proves [\[eq:cycle-power\]](#eq:cycle-power){reference-type="eqref" reference="eq:cycle-power"}; its scalar $L$th roots give [\[eq:cycle-roots\]](#eq:cycle-roots){reference-type="eqref" reference="eq:cycle-roots"}. The telescoping product gives [\[eq:radius\]](#eq:radius){reference-type="eqref" reference="eq:radius"}.

The polar-reduced clock $$\label{eq:polar-clock}
 K_{t,L}(\omega)=G_{t,L}^{1/2}C_{t,L}(\omega)G_{t,L}^{-1/2}$$ is similar to $C_{t,L}(\omega)$ and therefore has exactly the same spectrum. Moreover, $$\label{eq:polar-intertwining}
 \mathcal A V_{t,L}-V_{t,L}K_{t,L}(\omega)
 =a_{t+L-1}(x_{t+L}-\omega x_t)e_{L-1}^*G_{t,L}^{-1/2}.$$ Thus phase quantization in this model is an identity, not a fit. Physical content resides in the wrap and two directed residuals.

# Orientation mark and audit metrics

The time-domain optimal mark is $$\label{eq:mark}
 \omega_{t,L}=
 \frac{\langle x_t,x_{t+L}\rangle}
 {|\langle x_t,x_{t+L}\rangle|}$$ when the inner product is nonzero, and $1$ otherwise. It minimizes $\left\lVert x_{t+L}-\omega x_t\right\rVert_{\mathrm F}$ over $\omega\in\mathbb T$. This uses only the endpoint and seed states. It does not inspect transfer eigenvalues.

With $K=K_{t,L}(\omega_{t,L})$ and $V=V_{t,L}$, record $$\begin{aligned}
 d_{\rm proj}&=
 \sqrt{1-|\langle x_t,x_{t+L}\rangle|^2},
 \label{eq:projective}\\
 \epsilon_{\rm pr}&=
 \frac{\left\lVert\mathcal AV-VK\right\rVert}
 {\left\lVert\mathcal AV\right\rVert},
 \label{eq:primal}\\
 \epsilon_{\rm ad}&=
 \frac{\left\lVert\mathcal A^*V-VK^*\right\rVert}
 {\left\lVert\mathcal A^*V\right\rVert}.
 \label{eq:adjoint}\end{aligned}$$ The adjoint residual is independent information: a right-invariant temporal range need not be reducing for a nonnormal operator [@Kato1995].

The declared physical gate is $$\label{eq:gate}
 d_{\rm proj}\le0.25,
 \qquad \epsilon_{\rm pr}\le0.25,
 \qquad \epsilon_{\rm ad}\le0.25.$$

# Predeclared lengths and physical data

RH-179 derived the rank-to-cycle offsets three and four. Hence this paper uses $$\label{eq:lengths}
 L\in\{r-3,r-4\},\qquad L\ge3.$$ For the available reset anchors this leaves

   $\sigma$   clock rank $r$   admissible $L$    channels
  ---------- ---------------- ---------------- -------------
    $0.04$         $6$              $3$         left, right
    $0.02$         $6$              $3$         left, right
    $0.01$         $7$             $3,4$        left, right

The larger anchors have $L<3$ and are excluded before the audit. Across all starts there are 126 windows in eight scale/side/length groups.

The $\sigma=0.01,L=4$ branch is especially important: it is the only actual reset-atlas overlap with the RH-15 cloud degree $N=3$, for which $L=N+1=4$ [@WangRH15; @WangRH181].

# Results

The groupwise minima are:

   $\sigma$   side    $L$   $\min d_{\rm proj}$   $\min\epsilon_{\rm pr}$   $\min\epsilon_{\rm ad}$   negative marks
  ---------- ------- ----- --------------------- ------------------------- ------------------------- ----------------
    $0.04$    left     3         $0.9660$                $1.2623$                  $1.1161$                 0
    $0.04$    right    3         $0.9420$                $0.9444$                  $0.8924$                 1
    $0.02$    left     3         $0.7720$                $1.0868$                  $1.0457$                 0
    $0.02$    right    3         $0.8196$                $0.6869$                  $0.8520$                 2
    $0.01$    left     3         $0.6513$                $0.9618$                  $0.8833$                 2
    $0.01$    right    3         $0.7087$                $0.6138$                  $0.8557$                 0
    $0.01$    left     4         $0.3926$                $0.4441$                  $0.7540$                 19
    $0.01$    right    4         $0.3720$                $0.2711$                  $0.7143$                 19

The orientation mark is active in 43 of 126 windows and greatly improves some endpoint chords. It does not bring any projective distance below $0.25$. The best primal residual, $0.2711$, also misses the gate, while the adjoint residual never falls below $0.7143$. Therefore $$\label{eq:zero-success}
 \#\{\text{windows satisfying \eqref{eq:gate}}\}=0.$$

The exact implementation checks are separate from this negative physical result. The cycle-radius formula, root-grid phase formula, radial equality, and frame-isometry identity have zero failures at tolerance $10^{-10}$. Their success only confirms that the proposed clock was evaluated correctly.

At $\sigma=0.01,L=4$, the median data-derived radius is approximately $0.7825$ in both channels, close to the RH-15 threshold radius $0.77184\ldots$. This radial proximity is not enough: the physical range is not a two-sided orthogonal packet.

# Why the adjoint gate is logically independent

The two residuals in [\[eq:primal\]](#eq:primal){reference-type="eqref" reference="eq:primal"}--[\[eq:adjoint\]](#eq:adjoint){reference-type="eqref" reference="eq:adjoint"} are not duplicate measurements. Let $P=VV^*$ be the orthogonal projection onto the temporal range.

If $\mathcal AV=VK$, then $\operatorname{Ran}V$ is invariant under $\mathcal A$. If, in addition, $\mathcal A^*V=VK^*$, then $\operatorname{Ran}V$ is reducing and $$\label{eq:commuting-projection}
 P\mathcal A=\mathcal AP.$$

The first identity maps every column combination $Vc$ to $VKc$, hence back into $\operatorname{Ran}V$. The adjoint identity gives invariance of the same range under $\mathcal A^*$. Orthogonal complements are then invariant under the opposite operators, which is equivalent to [\[eq:commuting-projection\]](#eq:commuting-projection){reference-type="eqref" reference="eq:commuting-projection"}.

Thus a small primal residual alone would at most indicate an approximately invariant right packet. A spectral block that can be isolated by an orthogonal Riesz projection needs the adjoint direction as well. In the present data the separation is decisive: the primal minimum is only $0.0211$ above the declared threshold, whereas the adjoint minimum is $0.4643$ above it. The branch rejection is therefore not driven by a rounding-level miss of a single scalar gate.

# Finite decision margins and audit discipline

The three best observed margins relative to the common threshold are $$\begin{aligned}
 \min d_{\rm proj}-0.25&=0.12202,\label{eq:wrap-margin}\\
 \min\epsilon_{\rm pr}-0.25&=0.02106,\label{eq:primal-margin}\\
 \min\epsilon_{\rm ad}-0.25&=0.46433.\label{eq:adjoint-margin}\end{aligned}$$ These are finite floating margins, not interval certificates. They do, however, distinguish the logical roles of the tests. Endpoint projective return already fails before polar conditioning is considered; polar conditioning leaves the best primal case just outside the gate; and the adjoint dynamics remain far from the same orthogonal packet.

The audit also keeps algebraic checks separate from physical gates. The root-grid and radial equalities are consequences of how $C_{t,L}$ is built, so their zero error is a software and formula check. They are not votes in favor of physical closure. Conversely, a failed physical gate does not invalidate the exact weighted-cycle identity. This separation prevents a tautological spectral grid from being counted as empirical spectral agreement.

The complete decision rule was fixed before replay: lengths, anchors, orientation mark, norms, and threshold were not changed after inspecting the minima. A future audit may declare a different threshold or a different temporal span, but it would be a new branch with a new ledger rather than a retroactive repair of this one.

# Interpretation and branch decision

The audit rejects one precise statement:

> The consecutive normalized source orbit, polar-orthogonalized over one of the predeclared lengths, is a physical reducing clock for the frozen transfer model at the tested anchors.

The failure is robust to the natural orientation mark and appears most strongly in the adjoint direction.

It does not reject the exact cycle determinant of RH-176--180. It also does not reject a Petrov--Galerkin construction with distinct right and left temporal spaces. The physical models already provide both a source and an observation. Their forward and adjoint Krylov histories can define a biorthogonal packet without demanding that one orthogonal range reduce a nonnormal operator. That is the next controlled branch.

# Reproducibility and theorem boundary

The archive contains all 126 window records, including Gram conditioning, orientation mark, endpoint correlation, three closure metrics, cycle radius, and phase/radial formula errors. The full calculation uses one BLAS thread to make the stored result deterministic at the reported precision.

This paper proves the finite weighted-cycle identities [\[eq:rank-one-defect\]](#eq:rank-one-defect){reference-type="eqref" reference="eq:rank-one-defect"}--[\[eq:polar-intertwining\]](#eq:polar-intertwining){reference-type="eqref" reference="eq:polar-intertwining"} and reports the finite floating audit. It does not prove an all-level rejection, a unique cycle calibration, a biorthogonal realization, a validated contour resolvent, a physical Riesz projection, physical interface R, Gate A, a self-adjoint operator, a prime-power trace formula, or the Riemann Hypothesis.
