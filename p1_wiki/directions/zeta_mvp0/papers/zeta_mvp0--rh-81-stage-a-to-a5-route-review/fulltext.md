---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-81-stage-a-to-a5-route-review"
canonical_tex: "zeta_mvp0/papers/RH-81-stage-A-to-A5-route-review/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-81-stage-A-to-A5-route-review/main.pdf"
source_sha256: "2118b4d1b28f44a37aff180fc56062b5157ab6e486247273a7ddf1e28db16a68"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# From Validated Assembly to Moving-Cloud Renormalization A Ten-Layer Audit and the Minimal Stage-A/A5 Completion Frontiers

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-81-stage-A-to-A5-route-review>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-81-stage-A-to-A5-route-review/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-81-stage-A-to-A5-route-review/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-81-stage-A-to-A5-route-review/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-81-stage-A-to-A5-route-review/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-72--RH-80 carried the small-noise directional program from validated folded-Gaussian assembly through intrinsic square determinants and into the first relative fixed-disk construction. This tenth-layer review determines exactly which primitive gates remain, including the disjunctive structure hidden by a linear roadmap.

  We prove a completion-antichain theorem for monotone AND/OR dependency formulas. Closed leaves contribute the empty completion, open leaves their singleton, OR takes the inclusion-minimal union of child families, and AND takes inclusion-minimal unions across their Cartesian product. The resulting family is exactly the set of inclusion-minimal open-gate bundles whose closure makes the target true.

  For the archived program, $$\mathsf A_1=F\wedge(L\vee E),$$ where the finite-scale chain $F$ is now closed, $L$ is the all-level log-square block law, and $E$ is the all-level postblock effective-rank law. Thus Stage A has exactly two singleton completion alternatives: $\{L\}$ and $\{E\}$. The effective-rank corridor is preferred after the single-arc route failed and rank four captured at least $99.9999\%$ at all anchors. Either corridor would also close unconditional intrinsic identification and shrinking-disk determinants by RH-78--RH-79.

  The relative fixed-disk target has two minimal four-gate bundles: $$\{L,P,C,U\},\qquad \{E,P,C,U\},$$ where $P$ is an actual moving-cloud Riesz projection, $C$ its coefficient bridge, and $U$ a uniform trace-class complementary limit. Generic absolute continuity and fixed scalar pole cancellation are both closed false shortcuts, while moving-cloud factorization is green algebraically.

  A 256-bit Arb audit certifies the archived route margins: at least $99.783\%$ of the finite Hardy slack remains, the shrinking-disk determinant bound improves by a factor exceeding $100.37$, the fixed-disk bound reverses by a factor exceeding $19.47$, and the RH-80 inside/outside pole-fork contrast exceeds $5.19\times10^8$. These certify the finite and model-level verdicts, not the open all-level or cloud-complement theorems. No Hilbert--Polya or Riemann-hypothesis conclusion is made.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  From Validated Assembly to Moving-Cloud Renormalization\
  A Ten-Layer Audit and the Minimal Stage-A/A5 Completion Frontiers
```

## Markdown 正文

**Keywords:** dependency frontier; monotone formula; validated numerics; effective rank; relative determinant; small noise.

**MSC 2020:** 47A55; 47B10; 37C30; 65G20; 68R10.

# Scope and outcome

The previous checkpoint ended with two open Stage-A tasks: complete the finite upstream interval chain and prove uniform small-noise scaling. The first is now closed. RH-72 validated exact stochastic folded-Gaussian and Haar assembly [@WangAssembly2026]; RH-73 validated Perron/parity rank-two deflation [@WangDeflation2026]; and RH-74 joined these layers to the frozen terminal Hardy certificate at all five scales [@WangBridge2026].

The uniform problem then split. RH-75 isolated a sufficient log-square block law [@WangBlockLaw2026]. RH-76 proved that a single narrow phase arc does not explain the observed horizons [@WangArcBarrier2026]. RH-77 found a stronger surviving finite-scale phenomenon: the postblock future is nearly finite rank [@WangRankCompression2026]. RH-78 proved that an all-level theorem for either phenomenon closes Stage A with zero Hardy power and hence closes strict-mesh intrinsic identification [@WangTwoCorridors2026].

RH-79 propagated that conditional result to trace-norm squares and shrinking-disk determinants, while locating the generic fixed-disk exponential wall [@WangDiagonalTransfer2026]. RH-80 then proved that multiplication by the fixed limiting pole factor also fails across the cloud circle; the viable object is a quotient by the actual moving spectral cloud [@WangMovingCloud2026].

The outcome is not a linear list of five equally immediate tasks. It is an AND/OR network with two Stage-A alternatives followed by three simultaneous A5 gates. The purpose of this paper is to make that logic exact.

# Minimal completion antichains

A dependency formula is built recursively from primitive leaves using $\wedge$ and $\vee$. Each primitive leaf is currently either closed or open. A completion set is a set of open leaves which, when declared closed while all other statuses are held fixed, makes the formula true. It is minimal if no proper subset is a completion set.

For a finite family $\mathcal F$ of sets, let $\operatorname{Min}(\mathcal F)$ delete every member that strictly contains another member. Define $\mathfrak M(\Phi)$ recursively by $$\begin{aligned}
 \mathfrak M(x)&=\{\varnothing\}, &&x\text{ a closed leaf},\\
 \mathfrak M(x)&=\{\{x\}\}, &&x\text{ an open leaf},\\
 \mathfrak M\!\left(\bigvee_i\Phi_i\right)
 &=\operatorname{Min}\!\left(\bigcup_i\mathfrak M(\Phi_i)\right),\\
 \mathfrak M\!\left(\bigwedge_i\Phi_i\right)
 &=\operatorname{Min}\!\left\{
     \bigcup_i S_i:S_i\in\mathfrak M(\Phi_i)\right\}.\end{aligned}$$

[\[thm:completion\]]{#thm:completion label="thm:completion"} For every finite monotone dependency formula $\Phi$, the family $\mathfrak M(\Phi)$ is exactly the set of inclusion-minimal completion sets of $\Phi$. In particular, it is an antichain.

Proceed by structural induction. The leaf statements are immediate. An OR formula becomes true exactly when at least one child becomes true, so its completion sets are the union of the child completion families; deleting supersets leaves precisely the minimal ones. An AND formula becomes true exactly when every child becomes true. One must therefore choose a completion for each child and close their union. Every completion arises this way, and again deleting supersets leaves exactly the inclusion-minimal choices. This proves the recursion and the antichain property.

The theorem is elementary but useful: it prevents a closed prerequisite from remaining on the active frontier, preserves genuine alternative corridors, and removes dominated route bundles automatically.

# Application to Stage A and A5

Let

-   $F$: the finite-scale assembly/deflation/Hardy chain;

-   $L$: the all-level RH-75 log-square block law;

-   $E$: the all-level RH-77 postblock effective-rank law;

-   $P$: an actual moving-cloud Riesz projection;

-   $C$: the actual cloud coefficient bridge;

-   $U$: a uniform trace-class complementary limit.

The archived composition, square-transfer, and moving-cloud factorization theorems are closed in their conditional or algebraic scopes. The active formulas therefore reduce to $$\begin{aligned}
 \mathsf A_1&=F\wedge(L\vee E), \label{eq:A1}\\
 \mathsf A_4&=\mathsf A_1\wedge(\text{closed conditional composition}), \label{eq:A4}\\
 \mathsf A_{5,\mathrm{rel}}&=\mathsf A_4\wedge P\wedge C\wedge U
 \wedge(\text{closed moving-cloud algebra}). \label{eq:A5}\end{aligned}$$

[\[cor:frontiers\]]{#cor:frontiers label="cor:frontiers"} The minimal completion families are $$\begin{aligned}
 \mathfrak M(\mathsf A_1)=\mathfrak M(\mathsf A_4)
 &=\bigl\{\{L\},\{E\}\bigr\},\\
 \mathfrak M(\mathsf A_{5,\mathrm{rel}})
 &=\bigl\{\{L,P,C,U\},\{E,P,C,U\}\bigr\}.\end{aligned}$$ The unconditional shrinking-disk determinant has the same two singleton completion alternatives as Stage A.

RH-74 closes $F$. Substitute the current leaf statuses into [\[eq:A1,eq:A4,eq:A5\]](#eq:A1,eq:A4,eq:A5){reference-type="ref" reference="eq:A1,eq:A4,eq:A5"} and apply [\[thm:completion\]](#thm:completion){reference-type="ref" reference="thm:completion"}.

The corollary separates two meanings of "the next wall." Stage A has one logical wall with two alternative theorem forms. A5 has three additional conjunctive operator gates after either Stage-A choice. Those A5 gates may be studied in parallel, but the relative fixed-disk target needs all three.

# Nine-paper theorem ledger

The build script hashes and reads every RH-72--RH-80 summary. They contain forty-one boolean theorem gates, all true in their stated scopes. This is an archive consistency count, not a claim of forty-one independent mathematical theorems.

::: {#tab:ledger}
    Paper Route effect        Durable result                       Remaining boundary
  ------- ------------------- ------------------------------------ --------------------------
       72 validated advance   folded-Gaussian assembly             peripheral factors
       73 validated advance   Perron/parity rank-two deflation     Hardy propagation
       74 finite closure      end-to-end five-scale bridge         all-level scaling
       75 analytic corridor   sufficient log-square law            all-level proof
       76 branch no-go        single-arc barrier                   other compression routes
       77 positive fallback   postblock rank compression           analytic rank decay
       78 synthesis           either corridor closes Stage A       corridor premise
       79 advance/barrier     square and shrinking-disk transfer   fixed disk
       80 route correction    moving-cloud relative gate           actual cloud/complement

  : The nine inputs to the RH-81 synthesis. "No-go" applies only to the named branch or proof method.
:::

Three false shortcuts are now durably marked:

1.  single-arc phase compression as the source of the production horizons;

2.  generic absolute determinant continuity on a fixed small-noise disk;

3.  fixed scalar double-pole cancellation across the finite-cloud circle.

None is a no-go theorem for the full program. Each one redirects the route to a surviving alternative already encoded in [\[cor:frontiers\]](#cor:frontiers){reference-type="ref" reference="cor:frontiers"}.

# Validated route margins

The review audit uses Arb at 256-bit precision and exact binary64 rational lifting of the archived summary bounds. The six values in [2](#tab:margins){reference-type="ref" reference="tab:margins"} serve different diagnostic roles and are not combined into one probability or theorem constant.

::: {#tab:margins}
  Certified metric                                     Lower bound Interpretation
  --------------------------------------- ------------------------ -------------------------------------------------------------------
  finite Hardy slack fraction remaining                 0.99783070 RH-74 uses only about $0.217\%$ of inherited slack
  rank-two capture excess above $99\%$      $8.45345\times10^{-4}$ every RH-77 channel clears the rank-two gate
  rank-four excess above $99.9999\%$        $9.20296\times10^{-7}$ every channel clears the six-nine target
  shrinking-disk improvement factor                       100.3731 RH-79 error decreases by over two orders of magnitude
  fixed-disk reversal factor                               19.4789 the standard bound worsens after its minimum
  pole-fork inside/outside contrast            $5.19408\times10^8$ RH-80 sharply separates interior convergence from exterior growth

  : Outward-certified margins inherited by the route review.
:::

The finite-scale chain is therefore not marginal, and the effective-rank corridor is quantitatively compelling at the anchors. Conversely, the two fixed-disk negative verdicts are not artifacts of tiny numerical differences. The open issue in each case is theorem-level uniformity or operator construction, not additional floating precision.

![RH-72--RH-81 in one diagram: the input timeline, AND/OR completion architecture, certified margin audit, and revised stage ledger.](<../../../../../zeta_mvp0/papers/RH-81-stage-A-to-A5-route-review/figures/stage_A_to_A5_route_review.pdf>){#fig:review width="\\textwidth"}

# Revised route and next theorem

The preferred immediate target is an all-level postblock singular-value decay theorem. A representative sufficient form is $$s_{r+1}(O_kA_k^{M_k}S_k)
 \le C\,\operatorname{polylog}(k)e^{-cr},
 \label{eq:rank-target}$$ or any estimate giving a $\operatorname{polylog}(k)$ rank with zero power of $\sigma_k$. The proof should exploit smoothing after one production block, rank-two peripheral removal, and the low-dimensional source/observation geometry. RH-76 shows why compressing the raw phase measure into one arc is the wrong object.

If a rigorous lower bound defeats [\[eq:rank-target\]](#eq:rank-target){reference-type="eqref" reference="eq:rank-target"} with a forbidden noise power, the RH-75 full-block law remains the exact fallback. Stage A should be reassessed only if both singleton completion alternatives are ruled out under every admissible mesh schedule.

In parallel, A5 preparation should construct a moving contour and Riesz projection for the actual cloud, prove the cloud coefficient bridge, and control the complementary two-step trace norm. A5 should be reassessed only if every natural cloud extraction leaves a non-normal relative family on the required fixed domain.

The updated detailed roadmap is archived as `UPDATED_ROADMAP.md`. Later Stages B--D remain unopened. There is no canonical scattering completion, self-adjoint generator, intrinsic $T\log T$ counting law, prime-power trace formula, completed zeta identity, Hilbert--Polya operator, or Riemann Hypothesis result in this block.
