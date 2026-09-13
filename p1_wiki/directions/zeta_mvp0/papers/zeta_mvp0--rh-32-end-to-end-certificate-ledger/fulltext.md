---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-32-end-to-end-certificate-ledger"
canonical_tex: "zeta_mvp0/papers/RH-32-end-to-end-certificate-ledger/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-32-end-to-end-certificate-ledger/end-to-end-certificate-ledger.pdf"
source_sha256: "98a02835f10086e0eb398137a66cc2f371979c859abd524a8dec5823f92b157d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Projected Winding Certification and an End-to-End Contour Ledger Exact Stored-Model Counts, Selected-Arc Closure, and a Full-Contour Locality Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-32-end-to-end-certificate-ledger>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-32-end-to-end-certificate-ledger/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-32-end-to-end-certificate-ledger/end-to-end-certificate-ledger.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-32-end-to-end-certificate-ledger/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-32-end-to-end-certificate-ledger/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  A sequence of finite-dimensional studies near a quadratic band-merging regime constructed a rational Arnoldi Feshbach determinant, certified its arcwise approximation error conditionally on a complement-resolvent bound, isolated one dangerous singular channel, and finally proved sparse threshold-inertia bounds at three selected contour centers. Two logical questions remained entangled: whether the projected base winding itself was rigorous, and whether one selected-center resolvent certificate closed the entire contour argument.

  This paper separates those questions by an end-to-end certificate ledger. For the exact binary64 primal base realizations actually used by RH-28 at $\sigma=10^{-2}$, $4\times10^{-3}$, and $2\times10^{-3}$, we reconstruct the archived source path, freeze deterministic snapshots, and construct the $148$, $215$, and $282$ dimensional augmented matrices and enclose every eigenvalue with 256-bit Arb arithmetic. Every enclosure lies strictly inside or outside the stored circle. At each scale exactly one augmented eigenvalue lies inside, all projected Hessenberg poles lie outside, and there is no ambiguous boundary ball. Hence the projected determinant is holomorphic on the closed disk, has exactly one zero there, and has winding one. A provenance audit also detects that these extended-Arnoldi base prefixes are not bitwise identical to the earlier RH-24 short-Arnoldi discovery files; the two model families are therefore certified separately rather than silently identified.

  We then compose the sparse inertia bound with the exact one-channel Sherman--Morrison estimate and the arcwise Neumann transport, using outward arithmetic throughout. The resulting selected-arc inverse bounds are $1.0847\times10^4$, $3.5811\times10^4$, and $9.0858\times10^4$, all far below their corresponding arc budgets. However, the same one-center transport reaches exactly one of $936$, $2065$, and $6368$ archived arcs. For the nearest unselected arc its Neumann product already has rigorous lower bounds $1.0439$, $1.0167$, and $1.0078$. Thus the present local certificate cannot be promoted to a full-contour theorem.

  All consumed files are linked by SHA-256 and exact scalar-identity checks. A complete replay reproduces all 9,369 RH-28 arc rows in every one of their 30 non-timing fields, all deterministic scale-summary fields, and every frozen base-array entry bitwise. The remaining mathematical gates are now explicit: validated complement resolvent bounds on every other arc and a rigorous complement pole count, equivalently interior analyticity of the exact finite Feshbach map. No full-contour root count, continuum limit, Hilbert--Pólya construction, zeta-zero identification, or Riemann-hypothesis implication is claimed.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: July 2026
title: |
  **Projected Winding Certification and an End-to-End Contour Ledger**\
  Exact Stored-Model Counts, Selected-Arc Closure, and a Full-Contour Locality Obstruction
```

## Markdown 正文

**Keywords:** Feshbach map; verified eigenvalue enclosure; argument principle; rational Arnoldi realization; matrix Rouché theorem; nonnormal resolvent; reproducible certificate ledger.

**MSC 2020:** 15A18; 47A10; 47A11; 65F15; 65F50; 65G20; 65P30.

# Introduction {#sec:introduction}

The contour program studied in this series is finite-dimensional. At each noise scale a stored transfer matrix is split into a small packet block and a large complement. Eliminating the complement produces a matrix-valued Feshbach map whose determinant records a full-minus-complement spectral count. A shift-invariant Arnoldi reduction then gives a small rational matrix valid on one complete contour [@WangContourFeshbach2026; @SjoestrandZworski2007].

The subsequent layers made the comparison increasingly rigorous. A primal--dual residual identity was enclosed with outward arithmetic; an adaptive dyadic arc cover converted sampled contour evidence into a finite family of conditional Rouché inequalities [@WangArcwise2026; @GohbergSigal1971]. One-channel deflation reduced the missing complement inverse estimate to a lifted bulk inverse [@WangDeflated2026]. Sparse Grushin linearization and threshold inertia then certified the lifted inverse at three selected centers [@WangSparseGrushin2026; @WangThresholdInertia2026].

Those results do not automatically compose into a full-contour count. The reason is simple but consequential. The selected center lies on the arc with the smallest admissible *budget*; this does not imply that it is the location of the largest complement resolvent. A local inverse bound can be transported only while a resolvent-identity Neumann denominator remains positive. Moreover, even a complete boundary comparison needs interior analyticity, which requires a complement pole count.

There was a second, independent gap. The rational projected model had a floating winding one, no numerically observed projected pole, and one augmented eigenvalue in the circle. The determinant identity was exact, but the numerical eigenvalue classification itself had not been verified. Therefore "base winding one" remained evidence rather than a theorem.

The present paper audits the complete implication chain and closes every tractable gate without merging logically different evidence levels. Its contributions are:

1.  a verified eigenvalue-ball criterion converting an augmented realization into an exact zero-minus-pole count;

2.  256-bit Arb certificates of projected winding one and projected holomorphy on the stored disks at three scales;

3.  exact reproduction of the RH-28 base snapshots and every deterministic field in its three relevant arc archives;

4.  an outward composition of the RH-31 threshold, the RH-29 rank-one formula, and the RH-28 selected-arc transport;

5.  a rigorous all-arc audit proving that this one-center transport reaches exactly one archived arc at each scale;

6.  a SHA-256 and scalar-identity dependency graph separating object provenance from mathematical implication; and

7.  a minimal conditional theorem stating exactly which two gates would complete the finite stored-contour count.

The distinction among statement types is maintained throughout:

-   algebraic determinant, resolvent, and Rouché implications are exact theorems;

-   Arb and sparse-inertia statements are rigorous computer-assisted theorems for exact serialized binary64 inputs; and

-   no claim is made that those dyadic inputs enclose an exact continuum kernel, exact critical constants, or a zero-noise limit.

# Stored rational realization and exact counting identity {#sec:realization}

Let the packet rank be $m$. The stored columnwise Arnoldi realization has reduced packet block $D\in\mathbb C^{m\times m}$, square Hessenberg blocks $H_i\in\mathbb C^{J\times J}$, output couplings $G_i\in\mathbb C^{m\times J}$, and forcing columns $\beta_i e_1$. Set $$\mathcal H=\operatorname{diag}(H_1,\ldots,H_m),
 \qquad
 \mathcal G=[G_1\ \cdots\ G_m],
 \label{eq:block-h}$$ and let $\mathcal C\in\mathbb C^{mJ\times m}$ have $i$th block column $\beta_i e_1$. The rational projected Feshbach matrix is $$F_J(z)=z\mathrm I_m-D-\mathcal G(z\mathrm I_{mJ}-\mathcal H)^{-1}\mathcal C.
 \label{eq:projected-feshbach}$$ Its augmented realization is $$M_J=
 \begin{pmatrix}
  D&\mathcal G\\
  \mathcal C&\mathcal H
 \end{pmatrix}
 \in\mathbb C^{(m+mJ)\times(m+mJ)}.
 \label{eq:augmented}$$

[\[prop:det-identity\]]{#prop:det-identity label="prop:det-identity"} For $z\notin\operatorname{spec}\mathcal H$, $$\det(z\mathrm I-M_J)
 =\det(z\mathrm I-\mathcal H)\det F_J(z)
 =\left[\prod_{i=1}^m\det(z\mathrm I-H_i)\right]\det F_J(z).
 \label{eq:det-identity}$$ Consequently, for every contour $\Gamma$ avoiding both spectra, $$\operatorname{wind}_\Gamma\det F_J
 =N_\Gamma(M_J)-\sum_{i=1}^m N_\Gamma(H_i),
 \label{eq:count-identity}$$ where eigenvalues are counted with algebraic multiplicity.

Take the Schur complement of $z\mathrm I-\mathcal H$ in $z\mathrm I-M_J$. This gives [\[eq:det-identity\]](#eq:det-identity){reference-type="ref" reference="eq:det-identity"}; the argument principle gives [\[eq:count-identity\]](#eq:count-identity){reference-type="ref" reference="eq:count-identity"}.

The identity is exact and was already available in the preceding rational model. What remained was to certify the two ordinary eigenvalue counts in [\[eq:count-identity\]](#eq:count-identity){reference-type="ref" reference="eq:count-identity"}.

# Verified circle classification {#sec:verified-count}

Let $\overline{\mathbb D}(c,R)=\{z:|z-c|\leq R\}$. Suppose a validated eigensolver returns complex balls $E_1,\ldots,E_n$ enclosing all eigenvalues of a matrix, including multiplicity. Define $$\begin{aligned}
 E_j\text{ inside} &\quad\Longleftrightarrow\quad
   \sup_{z\in E_j}|z-c|<R,\label{eq:inside-test}\\
 E_j\text{ outside} &\quad\Longleftrightarrow\quad
   \inf_{z\in E_j}|z-c|>R.\label{eq:outside-test}\end{aligned}$$ A ball satisfying neither test is ambiguous and invalidates the count.

[\[thm:verified-disk-count\]]{#thm:verified-disk-count label="thm:verified-disk-count"} Assume every eigenvalue ball of $M_J$ and every $H_i$ is classified strictly by [\[eq:inside-test,eq:outside-test\]](#eq:inside-test,eq:outside-test){reference-type="ref" reference="eq:inside-test,eq:outside-test"}. Let $n_M$ and $n_H$ be the respective numbers of inside balls, counting repeated balls according to certified multiplicity. Then $$\operatorname{wind}_{|z-c|=R}\det F_J(z)=n_M-n_H.
 \label{eq:verified-winding}$$ If $n_H=0$, then $F_J$ is holomorphic on a neighborhood of $\overline{\mathbb D}(c,R)$ and $\det F_J$ has exactly $n_M$ zeros in the disk, counting multiplicity.

Strict classification excludes eigenvalues on the circle and gives the exact algebraic counts of $M_J$ and $\mathcal H$. Apply [\[prop:det-identity\]](#prop:det-identity){reference-type="ref" reference="prop:det-identity"}. If $n_H=0$, every pole of [\[eq:projected-feshbach\]](#eq:projected-feshbach){reference-type="ref" reference="eq:projected-feshbach"} lies outside the closed disk, so the projected map is holomorphic there and the zero-minus-pole count is an ordinary zero count.

## Exact dyadic input convention

RH-28 builds an Arnoldi model to a deeper level and then uses its first $J$ columns as the base rational map. We replay that exact source path, freeze the three base prefixes in deterministic NPZ archives, and verify them against a second fresh rebuild bit for bit. Every real and imaginary component is then embedded as its exact dyadic real value in Arb, not as a decimal uncertainty interval. The augmented matrices are assembled from those exact entries. Python-flint's validated nonsymmetric eigensolver is run at 256-bit precision with multiple-eigenvalue handling; overlapping enclosures are allowed, provided each enclosure remains on one strict side of the circle. Moduli and all boundary comparisons are Arb interval operations [@Johansson2017; @Rump2010].

The replay is tied to the original RH-28 archive more strongly than by source hashes alone: all $936+2065+6368=9369$ accepted arc rows reproduce exactly in all 30 non-timing fields, and every deterministic scale-summary field also agrees exactly. Timing fields are intentionally excluded.

This convention proves a theorem about the serialized RH-28 realization itself. It does not absorb the earlier construction error from an exact integral operator into the NPZ entries.

## Three computer-assisted counts

The minimum certified boundary clearances are respectively $$1.44191037\times10^{-2},\qquad
 1.43560126\times10^{-2},\qquad
 1.07815294\times10^{-2}.
 \label{eq:count-clearances}$$ There are no ambiguous balls among $148+215+282$ augmented enclosures or among the $144+210+276$ projected-pole enclosures.

[\[thm:three-projected-counts\]]{#thm:three-projected-counts label="thm:three-projected-counts"} For each of the three exact stored binary64 realizations in [\[tab:projected-counts\]](#tab:projected-counts){reference-type="ref" reference="tab:projected-counts"}, the rational projected Feshbach map is holomorphic on a neighborhood of the closed stored disk, its determinant has exactly one zero in that disk, and $$\operatorname{wind}_\Gamma\det F_J=1.
 \label{eq:three-windings}$$

The archived Arb output gives complete strict classifications with one inside augmented ball and no inside projected-pole ball. Apply [\[thm:verified-disk-count\]](#thm:verified-disk-count){reference-type="ref" reference="thm:verified-disk-count"}.

This theorem closes the projected-base count missing from the earlier arcwise audit. The earlier RH-24 discovery NPZ realizations have a separate archived Arb certificate with the same $1/0/1$ counts, but they are not used as substitutes in this theorem. Nothing here yet concerns the exact complement map.

# Outward composition of the selected-center certificates {#sec:composition}

Fix one selected RH-28 arc with center $z_0$, disc radius $\rho$, and downward admissible budget $L^-$. Write $$A=A(z_0)=z_0\mathrm I-B
 \label{eq:complement-center}$$ for the stored complement shift. The RH-29 singular-channel data consist of unit directions $u,v$, a stored scalar $\widehat s>0$, residuals $$r=Av-\widehat s u,
 \qquad
 q=A^*u-\widehat s v,
 \label{eq:singular-residuals}$$ and lift $\tau=1$. With $$c=\tau-\widehat s,
 \qquad
 \widetilde A=A+cuv^*,
 \label{eq:lift}$$ the exact rank-one estimate is $$\left\lVert A^{-1}\right\rVert_2
 \leq \Phi(K):=
 K+\frac{|c|(1+K\left\lVert r\right\rVert_2)(1+K\left\lVert q\right\rVert_2)}
 {\tau(\widehat s-|c|K\left\lVert r\right\rVert_2)},
 \label{eq:phi}$$ provided $\left\lVert\widetilde A^{-1}\right\rVert_2\leq K$ and the denominator is positive [@WangDeflated2026].

RH-31 proves $s_{\min}(\mathcal G)>\alpha$ for a sparse Grushin matrix and hence $$\left\lVert\widetilde A^{-1}\right\rVert_2\leq\left\lVert\mathcal G^{-1}\right\rVert_2<\alpha^{-1}.
 \label{eq:rh31-bound}$$ The archived threshold is the next binary64 value above $2/K_*^-$, where $K_*^-$ is the RH-29 admissible lifted budget. In the present composition we recompute $K=\operatorname{up}(1/\alpha)$ in Arb instead of trusting the printed decimal inverse.

[\[lem:disc-transport\]]{#lem:disc-transport label="lem:disc-transport"} If $\left\lVert A(z_0)^{-1}\right\rVert_2\leq M_0$ and $$dM_0<1,
 \label{eq:neumann-premise}$$ then every $z$ satisfying $|z-z_0|\leq d$ obeys $$\left\lVert A(z)^{-1}\right\rVert_2\leq\frac{M_0}{1-dM_0}.
 \label{eq:transported-bound}$$

Factor $A(z)=A(z_0)[\mathrm I+(z-z_0)A(z_0)^{-1}]$ and apply the Neumann lemma.

For the selected arc take $d=\rho$. Every scalar operation in [\[eq:phi,eq:transported-bound\]](#eq:phi,eq:transported-bound){reference-type="ref" reference="eq:phi,eq:transported-bound"} is evaluated with Arb; upstream upper bounds are embedded as exact dyadic upper constants and upstream lower budgets as exact dyadic lower constants.

[\[thm:selected-arcs\]]{#thm:selected-arcs label="thm:selected-arcs"} Assume the exact stored-target hypotheses of the three RH-31 inertia certificates. Then the corresponding exact stored complement inverses satisfy the RH-28 conditional Rouché requirement throughout selected arcs $433$, $1348$, and $5453$ at $\sigma=10^{-2}$, $4\times10^{-3}$, and $2\times10^{-3}$, respectively.

RH-31 gives [\[eq:rh31-bound\]](#eq:rh31-bound){reference-type="ref" reference="eq:rh31-bound"}. The positive $\delta^-$ values in [\[tab:composition\]](#tab:composition){reference-type="ref" reference="tab:composition"} activate [\[eq:phi\]](#eq:phi){reference-type="ref" reference="eq:phi"}. The products $\mu^+<1$ activate [\[lem:disc-transport\]](#lem:disc-transport){reference-type="ref" reference="lem:disc-transport"}, and each transported upper bound is strictly below the corresponding downward RH-28 budget.

# Why the selected arc does not close the contour {#sec:locality}

Let the $a$th RH-28 arc be enclosed by the stored disc $$\overline{\mathbb D}(z_a,\rho_a).
 \label{eq:arc-disc}$$ Starting from the selected center $z_0$ and its certified bound $M_0$, the same one-center argument uses $$d_a=|z_a-z_0|+\rho_a,
 \qquad
 \mu_a=d_aM_0.
 \label{eq:arc-distance}$$ If $\mu_a<1$, the transported bound is $M_0/(1-\mu_a)$ and must then be compared with the arc-specific budget $L_a^-$. If a rigorous lower bound for $\mu_a$ exceeds one, this particular certificate cannot even activate the Neumann lemma on arc $a$.

[\[prop:budget-not-resolvent\]]{#prop:budget-not-resolvent label="prop:budget-not-resolvent"} Knowing that $a_*$ minimizes the numerical thresholds $L_a^-$ and proving a resolvent bound on $a_*$ imply no resolvent bound on any disjoint arc.

The thresholds are coefficients in an approximation-error inequality; they contain no ordering information about $\left\lVert(z\mathrm I-B)^{-1}\right\rVert$. Already in the scalar family $A(z)=z-\lambda$, one may place $\lambda$ on a second arc while keeping the selected arc disjoint from $\lambda$. Then the selected arc has a finite inverse bound and the second arc contains a pole, independently of which threshold is smaller.

The actual stored model gives a stronger quantitative audit than this logical counterexample.

::: {#tab:coverage}
            $\sigma$   selected   total arcs   closed   failed   nearest other   $\min_{a\ne a_*}\mu_a^-$
  ------------------ ---------- ------------ -------- -------- --------------- --------------------------
           $10^{-2}$        433          936        1      935             432                  1.0439217
    $4\times10^{-3}$       1348         2065        1     2064            1347                  1.0167183
    $2\times10^{-3}$       5453         6368        1     6367            5452                  1.0078263

  : Rigorous one-center transport coverage. The "nearest other" column is the smallest lower Neumann product over every unselected arc. It already exceeds one, so all remaining arcs fail the premise of [\[lem:disc-transport\]](#lem:disc-transport){reference-type="ref" reference="lem:disc-transport"} for the composed center bound.
:::

There are no ambiguous Neumann classifications and no arc that passes the Neumann premise but fails only at the budget comparison. Exactly the selected arc passes. The gaps are small at the nearest neighbor, especially at $\sigma=2\times10^{-3}$, but strict failure is still failure.

[\[thm:locality\]]{#thm:locality label="thm:locality"} At each of the three stored scales, the current RH-31 $\to$ RH-29 one-center bound and the RH-28 archived disc geometry rigorously certify one arc and no other arc through [\[lem:disc-transport\]](#lem:disc-transport){reference-type="ref" reference="lem:disc-transport"}. Therefore [\[thm:selected-arcs\]](#thm:selected-arcs){reference-type="ref" reference="thm:selected-arcs"} does not establish a full-contour Rouché inequality.

The selected upper products are below one by [\[tab:composition\]](#tab:composition){reference-type="ref" reference="tab:composition"}. The minimum lower product over every unselected arc is above one by [1](#tab:coverage){reference-type="ref" reference="tab:coverage"}. Thus the sufficient Neumann premise is rigorously true only for the selected arc. Since RH-28 requires the complement inequality on every leaf of its exact partition, the full-contour hypothesis is not proved.

The theorem concerns the reach of the *current upper bound*. It does not assert that the true complement inverse is large on the other arcs. A sharper center bound, a new center, or a different nonnormal resolvent argument may close them.

# The exact end-to-end implication and the two open gates {#sec:end-to-end}

Let $\Omega$ be one stored circle interior and let $F$ denote the exact finite stored Feshbach map before rational Arnoldi projection. The RH-28 arc theorem proves $$\left\lVert F_J(z)^{-1}(F(z)-F_J(z))\right\rVert_2<1
 \label{eq:matrix-rouche}$$ on an arc whenever its complement-resolvent requirement is met. The following theorem records the minimal finite-dimensional closure.

[\[thm:conditional-closure\]]{#thm:conditional-closure label="thm:conditional-closure"} Fix one of the three scales in [\[thm:three-projected-counts\]](#thm:three-projected-counts){reference-type="ref" reference="thm:three-projected-counts"}. Suppose:

1.  $\operatorname{spec}B\cap\overline\Omega=\varnothing$, so the exact finite Feshbach map $F$ is holomorphic on a neighborhood of $\overline\Omega$;

2.  on every RH-28 arc $a$, $\sup_{z\in a}\left\lVert(z\mathrm I-B)^{-1}\right\rVert_2<L_a^-$.

Then $F$ has determinant winding one and exactly one zero in $\Omega$, counting multiplicity. Under the exact finite Schur determinant identity, the corresponding full stored matrix also has exactly one eigenvalue in $\Omega$.

By [\[thm:three-projected-counts\]](#thm:three-projected-counts){reference-type="ref" reference="thm:three-projected-counts"}, $F_J$ is holomorphic on the closed disk and its determinant has one zero. Assumption 1 makes $F$ holomorphic. Assumption 2 activates the RH-28 inequality [\[eq:matrix-rouche\]](#eq:matrix-rouche){reference-type="ref" reference="eq:matrix-rouche"} on every leaf of the exact dyadic cover, hence on the whole boundary. Matrix Rouché theory gives equal determinant winding and equal zero count for $F$ and $F_J$ [@GohbergSigal1971]. Finally, the exact Schur determinant identity adds the complement eigenvalue count, which is zero by Assumption 1.

[\[cor:current-status\]]{#cor:current-status label="cor:current-status"} The present archive proves the projected premise of [\[thm:conditional-closure\]](#thm:conditional-closure){reference-type="ref" reference="thm:conditional-closure"} and one selected arc at each scale. It does not prove either full-contour assumption. Therefore no exact full stored root count follows from the current chain.

The two open gates are independent:

1.  **Boundary resolvent atlas.** Every remaining RH-28 arc needs a validated complement inverse bound below its own budget. A local certificate at the budget minimizer is insufficient.

2.  **Interior complement pole count.** Even complete boundary inequalities do not by themselves exclude complement eigenvalues in $\Omega$. One needs a pole-free homotopy, a complement argument- principle count, or another rigorous interior spectral exclusion.

The first gate controls the Rouché comparison. The second determines whether that comparison is an ordinary zero count or only a meromorphic zero-minus-pole statement.

# Cross-paper object identity and provenance {#sec:provenance}

Numerically compatible tables do not guarantee that two theorems concern the same serialized object. RH-32 therefore verifies both file hashes and scalar identities.

The hash graph checks:

1.  every model-construction source hash recorded by RH-24 and RH-25, and every arc-construction source hash recorded by RH-28;

2.  the RH-28 metadata-recorded SHA-256 values of the RH-24 contour summary and RH-27 residual summary;

3.  the RH-29 metadata-recorded SHA-256 value of the RH-28 arc file;

4.  every RH-29 triplet hash printed in its scale table;

5.  every RH-31 exact-target certificate hash recorded independently in its summary JSON and threshold table; and

6.  the deterministic RH-28 base snapshots consumed by the new Arb count and the independent replay certificate linking them to all archived arc fields.

The exact object-identity audit checks, at each scale, $$\begin{aligned}
 (c,R)_{\rm RH24}&=(c,R)_{\rm RH28},\label{eq:id-contour}\\
 (z_0,\rho,L^-)_{\rm RH28}&=(z_0,\rho,L^-)_{\rm RH29},\label{eq:id-arc}\\
 \alpha_{\rm RH31}
 &=\operatorname{nextafter}\!\left(\frac{2}{K_{*,\rm RH29}^-},+\infty\right),
 \label{eq:id-threshold}\\
 K_{\rm RH31}^+
 &=\operatorname{nextafter}(1/\alpha,+\infty).
 \label{eq:id-inverse}\end{aligned}$$ The physical dimensions and scale labels are also required to agree. Every check passes.

One identity is deliberately *not* asserted. The RH-28 base snapshots are not bitwise equal to the earlier RH-24 discovery NPZ files. Their maximum entrywise differences are $2.28\times10^{-7}$, $2.43\times10^{-8}$, and $7.57\times10^{-9}$ at the three scales. This is consistent with constructing a deeper Arnoldi model and retaining its prefix rather than stopping Arnoldi at the discovery depth. RH-32 records the nonidentity in `results/model_reconstruction_audit.json` and certifies both model families separately. Treating them as one object would have been a provenance error even though their projected counts agree.

::: {#tab:dependency}
  edge                                      mechanism                                                status
  ----------------------------------------- -------------------------------------------------------- ----------
  RH-24/RH-27 $\to$ RH-28                   metadata-recorded input SHA-256                          verified
  RH-24/25/28 source $\to$ RH-28 snapshot   recorded source hashes and bitwise fresh rebuild         verified
  RH-28 snapshot $\to$ arc archive          all non-timing arc and scale fields reproduced exactly   verified
  RH-28 $\to$ RH-29                         metadata-recorded arc-file SHA-256                       verified
  RH-29 triplets $\to$ RH-31                triplet hashes plus exact selected-object identities     verified
  RH-31 $\to$ RH-32                         certificate hashes and threshold identities              verified

  : Dependency ledger. A hash edge proves object provenance, not the mathematical correctness of the source theorem; that remains a separate logical layer.
:::

The complete node list, edge list, actual hashes, expected hashes, and boolean checks are archived in `results/dependency_ledger.json`. The full field-by-field replay is archived in `results/rh28_reconstruction_verification.json`. The 9,369 per-arc transport classifications are stored separately rather than summarized only in the manuscript.

# Interpretation and next route {#sec:interpretation}

![Left: rigorous composition on the selected arc. Right: the exact status of the finite stored-model gates. Green means certified; red means open, not numerically false.](<../../../../../zeta_mvp0/papers/RH-32-end-to-end-certificate-ledger/figures/end_to_end_ledger.pdf>){#fig:ledger width="\\textwidth"}

The result is simultaneously positive and negative.

The positive part is structural. The projected winding is no longer a phase-unwrapping observation. It is an exact consequence of completely classified eigenvalue balls for the dyadic rational realization actually used by RH-28. The audit also catches and resolves the distinct RH-24/RH-28 Arnoldi prefixes rather than relying on their numerical closeness. The selected local resolvent chain composes without a hidden change of center, radius, triplet, threshold, or rounding direction.

The negative part prevents an invalid shortcut. The smallest RH-28 budget identifies the strictest *allowable error threshold*; it does not locate the maximum complement resolvent. The actual one-center radius is so local that the nearest adjacent arc already lies just outside its certified Neumann domain. Large selected-arc budget margins cannot repair this geometric failure.

The nearest-neighbor products suggest a concrete next route. They exceed one by only $4.39\%$, $1.67\%$, and $0.78\%$. Rather than seek one global nonnormal resolvent bound, one may build a *multi-center certified resolvent atlas*: certify selected centers, transport each certificate over its local neighborhood, and add centers only at uncovered frontier arcs. This converts the next question from "can one center control the circle?" to "how many rigorously linked local charts are needed?" The interior pole count should remain a separate theorem rather than being inferred from boundary coverage.

# Limitations {#sec:limitations}

The following limitations are part of the result.

1.  The main verified eigenvalue counts concern three exactly replayed RH-28 rational base models; the supplementary RH-24 discovery counts concern a distinct model family. Neither is the exact unprojected complement or an infinite-dimensional operator.

2.  The upstream sparse inertia certificates are inherited with their stated IEEE, no-pivot, and exact-binary64 target assumptions.

3.  Failure of the current Neumann premise on an arc is not evidence of an actual pole or a large true resolvent there.

4.  Hash agreement proves that the same archived objects were consumed; it is not a substitute for the mathematical proofs attached to those objects.

5.  No limit as $\sigma\to0$, no self-adjoint generator, no $T\log T$ counting law, no prime-power trace formula, and no relation to Riemann zeros is established.

# Reproducibility {#sec:reproducibility}

The repository archives:

-   exact source for loading the rational realizations and constructing $M_J$;

-   deterministic RH-28 base snapshots, a full 9,369-arc replay, and an explicit nonidentity audit against the RH-24 discovery snapshots;

-   a strict inside/outside/ambiguous eigenvalue-ball classifier;

-   the 256-bit projected count certificates;

-   the outward RH-31 $\to$ RH-29 $\to$ RH-28 scalar composition;

-   all 9,369 per-arc transport classifications;

-   cross-paper object-identity and SHA-256 dependency ledgers;

-   nine fast tests, including synthetic ambiguous-ball rejection and archive-hash verification; and

-   scripts for the figure, manuscript, and final archive audit.

The snapshot rebuild and full count recomputation take about three minutes on the archived server. The complete RH-28 field replay is run one scale per process because the original pipeline uses Linux `fork` and should not continue ARPACK in the same interpreter afterward. The composition and provenance layers can be rebuilt independently from the frozen projected-count JSON. Code and data are available at <https://github.com/maris205/prime_dynamics_theory/tree/main/papers/RH-32-end-to-end-certificate-ledger>.

# Conclusion {#sec:conclusion}

The end-to-end audit closes one genuine theoretical gap and exposes another without ambiguity. At three finite stored scales, the exactly replayed RH-28 projected rational Feshbach determinant has a rigorous winding-one certificate, not merely a stable floating phase. The audit identifies the distinct RH-24 discovery realization and certifies it separately. The sparse threshold-inertia result also propagates rigorously through one-channel deflation and resolvent transport to the selected RH-28 arc.

What does not follow is equally precise. The selected-center certificate reaches exactly one arc, while the nearest other arc already violates its Neumann premise. A full-contour result still needs a validated local atlas or another global complement-resolvent theorem, together with an independent interior complement pole count. Those are now the only two finite stored- model gates between the present ledger and a legitimate contour root count.
