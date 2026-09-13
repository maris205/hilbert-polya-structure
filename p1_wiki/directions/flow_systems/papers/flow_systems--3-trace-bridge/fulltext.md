---
p1_kind: "derived-fulltext-reading-copy"
route: "flow_systems"
logical_paper_id: "flow_systems--3-trace-bridge"
canonical_tex: "flow_systems/papers/3-trace-bridge/paper/manuscript.tex"
canonical_pdf: "flow_systems/papers/3-trace-bridge/paper/paper.pdf"
source_sha256: "b51a7527de679778603b3530dfb9c5f6c5336681ca3a285219baaa8eeb5cb7fb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# One Orbit Is Not a Trace: A Same-Object Certificate for Classical--Spectral Bridges

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../flow_systems/papers/3-trace-bridge>)
- [规范 TeX](<../../../../../flow_systems/papers/3-trace-bridge/paper/manuscript.tex>)
- [关联 PDF](<../../../../../flow_systems/papers/3-trace-bridge/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../flow_systems/papers/3-trace-bridge/README.md>)
- [BibTeX](<../../../../../flow_systems/papers/3-trace-bridge/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Periodic-orbit arguments often move too quickly from one exact orbit coefficient to a global spectral trace. We introduce a typed same-object certificate, with gates T0--T7, that requires the classical ledger, analytic object, trace functional, theorem extent, coefficients, clock, normalization, and arithmetic map to belong to one source-locked record. Five theorem families are then separated by data type: Duistermaat--Guillemin wave traces, the exact Selberg trace formula, foliated Lefschetz distributions, Ruelle flat traces and Pollicott--Ruelle resonances, and Gutzwiller semiclassics. We prove three exact limits on inference. First, a complete distributional germ near one period does not determine a global trace. Under an explicit prior containing every possible nonzero singular location, all nonzero singular germs leave an exactly characterized ambiguity that is smooth off zero; after the zero germ is fixed, a globally smooth ambiguity remains. Second, a record formed by borrowing coordinates from distinct candidates fails the object identity gate. Third, for every modular hyperbolic class and all positive integers $r,k$, its repeated geodesic length satisfies $r\ell_\gamma\ne k\log p$ for every rational prime $p$. Thus the exact modular Selberg coefficient cannot be transferred atom by atom to Deninger's rational-prime packet ledger while preserving the standard clocks. The two frozen candidates consequently remain complementary rather than composable: the Deninger flow has intrinsic prime-log period support but no source-defined trace or operator, whereas the modular geodesic flow has an exact same-geometry trace and natural Laplacian but fails rational-prime support. Deterministic controls use no Riemann-zero data and no fitted parameters. The result is a certificate and a candidate-specific no-splicing theorem, not a universal obstruction to future enrichments or time changes.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: 13 August 2026
title: |
  **One Orbit Is Not a Trace:**\
  A Same-Object Certificate for Classical--Spectral Bridges
```

## Markdown 正文

**摘要**

周期轨道研究中，一个精确的轨道系数常被过早提升为全局谱迹。本文提出 T0--T7"同一对象证书"，要求经典轨道账本、解析对象、迹泛函、定理适用 范围、系数、时钟、归一化与算术映射全部来自同一来源锁定对象。我们据此 区分五类常被混称为"迹"的定理：Duistermaat--Guillemin 波迹、精确 Selberg 迹公式、叶状 Lefschetz 分布、Ruelle 平坦迹及 Pollicott--Ruelle 共振，以及 Gutzwiller 半经典渐近。本文证明三条严格边界：单个周期附近的完整分布 germ 不能确定全局迹；在一个包含全部可能非零奇性位置的显式先验下，即使知道 所有非零奇性 germ，仍存在零点外光滑的精确刻画歧义；从不同候选逐坐标 拼出的记录违反对象同一性；对任意模双曲 闭测地线及正整数 $r,k$，均有 $r\ell_\gamma\ne k\log p$。因此，在标准 时钟不变时，模空间的 Selberg 系数不能逐原子转移到 Deninger 的有理素数 packet。Deninger 候选具有内生的素数对数周期，却缺少来源定义的迹与算子； 模测地流具有同一几何上的精确迹和自然 Laplace 算子，却不具有有理素数 支撑。零点数据与参数拟合均未使用。本文结论是同一对象认证与特定候选的 不可拼接定理，而非对一切未来增广、时间变换或量子化的普遍否定。

**Keywords:** trace formula; periodic orbit; same-object certificate; wave trace; Selberg trace formula; arithmetic dynamics; Hilbert--Pólya programme.

# Introduction

A closed orbit is geometric data. A trace is an analytic functional on a specified class of operators or test functions. Relating the two requires a theorem whose hypotheses identify the flow, analytic object, clock, coefficients, convergence sense, and non-orbit terms. The distinction is especially important in arithmetic dynamics, where an object may reproduce the desired periods without supplying a trace, or may carry an exact trace whose orbit support is the wrong arithmetic set.

The present study is motivated by two source-locked candidates. In `DEN-WITT-Z-FIN`, Deninger's rational-Witt flow for $\operatorname{Spec}\mathbb{Z}$ produces compact packets $\Gamma_p$ indexed by rational primes; every orbit in the packet has least period $\log p$ [@Deninger2026]. The preceding packet audit showed that the ordinary one-factor-per-individual-orbit product diverges and that the source does not yet supply the measured lift, cross-packet normalization, or operator trace needed for a replacement. In `MOD-GEO`, the unit-speed geodesic flow on the modular quotient and the automorphic Laplacian belong to one geometry, so the complete cofinite Selberg formula is an exact classical--spectral benchmark [@Selberg1956; @Hejhal1983]. Yet its hyperbolic lengths do not equal rational-prime-power logarithms.

These observations create a tempting but invalid construction: take the prime-log coordinate from the Deninger record and the trace, coefficient, and quantization coordinates from the modular record. This paper makes precise why that operation does not produce a bridge. A bridge is a predicate of one typed record, not a coordinatewise maximum over unrelated records. Moreover, the standard clocks of the two candidates have disjoint repeated atomic supports, so even the most direct clock-preserving transfer is algebraically impossible.

The paper has four contributions. First, it defines a same-object trace certificate with gates T0--T7. Second, it provides a five-way taxonomy of trace theorems, keeping local versus global, fixed versus semiclassical, and self-adjoint versus resonance or cohomological ledgers distinct. Third, it proves a local-to-global ambiguity theorem, a no-coordinatewise-maximum lemma, and the modular/prime clock-support theorem. Fourth, it applies the certificate separately to the two frozen candidates and runs deterministic controls that do not inspect Riemann zeros or fit any scale.

The scope is deliberately narrow. We do not claim that Deninger's space admits no future smooth, groupoid, cohomological, or operator enrichment. We do not claim that local trace formulae cannot be globalized after additional analytic data are constructed. A new time change or bridge morphism would be a new mathematical candidate and would have to re-establish every gate.

# Research design, source lock, and evidence vocabulary {#sec:design}

This is a theorem-hypothesis audit with exact elementary proofs and finite controls. The protocol, candidates, clocks, certificate fields, theorem candidates, and falsification cases were frozen before manuscript drafting. Primary articles or authoritative monographs support the non-elementary framework claims. The words [PROVED]{.sans-serif}, [NOT TESTABLE]{.sans-serif}, [NOT APPLICABLE]{.sans-serif}, and [REFUTED]{.sans-serif} refer to the stated claim at the stated scope; they do not form a numerical evidence scale.

The first frozen record is $$\begin{aligned}
 D={}&(\texttt{DEN-WITT-Z-FIN},\ \phi^t[P,u]=[P,\mathrm{e}^t u],\ t,\\
 &\{\Gamma_p\}_{p\ \mathrm{prime}},\ \{k\log p:k\ge1\}).
\end{aligned}$$ Its packet exhaustion and period law are source results [@Deninger2026]. A finite-dimensional smooth phase space, linearized return, trace functional, cohomological action, Hilbert space, operator domain, and quantum operator are absent from the frozen source record. Their status here is [NOT TESTABLE]{.sans-serif}, not refutation.

The second record is $$\begin{aligned}
 M={}&(\texttt{MOD-GEO},\ T^1(\mathrm{PSL}_2(\mathbb{Z})\backslash\mathbb H),
 \text{ unit-speed geodesic flow},\\
 &\text{arc-length clock},\ \Delta,\text{ complete cofinite Selberg framework}).
\end{aligned}$$ The complete cofinite identity includes discrete and continuous/scattering spectral terms and identity, elliptic, parabolic/cusp, and hyperbolic geometric terms. The original Selberg article and Hejhal's detailed monograph establish the framework [@Selberg1956; @Hejhal1983]. The exact test-function and Fourier convention was not transcribed from an acquired full copy during this stage. We therefore print only a typed schematic identity and a separately audited hyperbolic coefficient. No unverified cofinite constant, sign, or equation number is used.

The comparison controls are a closed hyperbolic surface, a smooth bump added away from an audited trace germ, a varying $\hbar$-family, the modular formula with continuous/scattering terms intentionally omitted, a post-hoc clock rescaling, and a DEN/MOD coordinate splice. A control succeeds when it exposes an invalid inference, not when it resembles the Riemann target.

# A trace is a typed mathematical object {#sec:types}

The word "trace" does not determine its own data type. A classical--analytic claim must identify at least the fields in Table [1](#tab:types){reference-type="ref" reference="tab:types"}.

::: {#tab:types}
  Field               Examples and certification question
  ------------------- -------------------------------------------------------------------------------------------------------------------------
  analytic ledger     self-adjoint spectrum, resonances, reduced cohomology, or a regularized density of states; what object is paired?
  trace functional    ordinary/distributional trace, flat trace, supertrace, $b$-trace, or asymptotic regularized trace; on which test class?
  theorem extent      local near one period, global on a test space, meromorphic in a domain, or semiclassical in a localized window?
  operator regime     one fixed operator, one generator on anisotropic spaces, a cohomological action, or a family $\widehat H_\hbar$?
  orbit geometry      isolated nondegenerate orbit, clean family, simple foliated orbit, preserved leaf, or relative fixed set?
  equality strength   exact, exact after named regularization, asymptotic with a remainder, or singular-support inclusion?

  : Independent fields suppressed by an unqualified use of "trace."
:::

These axes are not stages on a single ladder. A cohomological Lefschetz distribution can be exact without being a self-adjoint quantum trace. A flat trace can be exact in positive time while its resonances come from a generally non-self-adjoint generator. A rigorous Gutzwiller formula can have a strong remainder and still concern a varying $\hbar$-family rather than one fixed operator.

# The same-object certificate {#sec:certificate}

A trace-certificate record is a tuple whose populated fields carry a common provenance pair $(\texttt{candidate\_id},\texttt{source\_lock})$. Its fields specify the classical phase object and flow; clock; primitive and repetition ledger; analytic object and Hilbert/cohomology space; operator or action and domain; trace or regularization and test class; spectral or resonance ledger; local/global and exact/asymptotic extent; orbit coefficients; non-orbit terms; error or distributional convergence; normalization; and arithmetic map.

The record passes the following gates only when the answer is supplied by the same source-locked object.

P0.17P0.37P0.36

\
Gate & Required evidence & Typical invalid promotion\
Gate & Required evidence & Typical invalid promotion\
T0 object identity & every populated field has one candidate and source lock & coordinates borrowed from distinct objects\
T1 classical ledger & intrinsic primitive/repeated orbits, periods, multiplicity, phase, and stability or clean data & a desired amplitude attached afterward\
T2 trace definition & explicit trace/flat trace/supertrace/$b$-trace or regularization on a test class & an orbit sum merely named a trace\
T3 analytic ledger & an operator/action with domain or topology and its spectrum, resonances, or cohomology & unrelated spectral data\
T4 theorem extent & local/global and exact/asymptotic status with remainder or distributional qualification & one local coefficient made global\
T5 coefficient provenance & period, primitive factor, normal density/determinant, phase, sign, and multiplicity derived by the theorem & a Selberg or Gutzwiller weight copied to new geometry\
T6 clock and normalization & one time variable, Fourier convention, cutoff, trace normalization, and all non-orbit terms & rescaled clock or omitted continuum\
T7 arithmetic promotion & the same record derives rational-prime/prime-power support and weights & generic exact geometry called Riemann arithmetic\

[\[lem:splice\]]{#lem:splice label="lem:splice"} Let $C_D$ and $C_M$ be certificate records with distinct provenances $D\ne M$. Suppose a record $C_*$ selects at least one field datum from each record, without a theorem transporting and rederiving those data in a new object. Then $C_*$ fails T0 for every declared provenance.

The populated fields of $C_*$ retain both provenances $D$ and $M$. If T0 held with declared provenance $I$, every populated field would have provenance $I$. This would force $D=I=M$, contrary to $D\ne M$. Relabeling the container does not alter field provenance.

Lemma [\[lem:splice\]](#lem:splice){reference-type="ref" reference="lem:splice"} is a formal schema statement, not a claim that bridge morphisms never exist. A genuine morphism would be new data with specified source and target and proofs transporting and rederiving the clock, primitive and repetition ledger, analytic object and domain, trace and test class, coefficients, non-orbit terms, and normalization. Only that evidence would license a new provenance and a new certificate to audit.

# Five trace theorem families {#sec:taxonomy}

## Duistermaat--Guillemin wave trace

Let $P$ be a positive self-adjoint elliptic pseudodifferential operator of order one, with real scalar principal symbol, on a closed smooth manifold. (For a positive operator of order $m$, this is the normalized positive $m$-th root.) The distribution $$\Theta_P(t)=\operatorname{Tr}\mathrm{e}^{-itP}$$ has singular support constrained by periods of the associated Hamiltonian bicharacteristic flow. Under a clean fixed-set hypothesis, the local expansion near a period carries a canonical density and phase data [@DuistermaatGuillemin1975]. This is a fixed-operator result, but its periodic-orbit output is local: a singular-support inclusion or local germ is not a complete global orbit sum. It cannot be applied to the frozen Deninger record because that record supplies no finite-dimensional cotangent Hamiltonian system, elliptic operator, symbol, clean fixed locus, or Maslov data.

## The exact Selberg trace

The Selberg trace formula is the strongest same-object benchmark here. The geodesic flow and automorphic Laplacian arise from the same quotient. In the cofinite modular case, the established exact framework has the type $$\mathcal S_{\rm disc}(h)+\mathcal S_{\rm cont/scatt}(h)
 =\mathcal G_{\rm id}(h)+\mathcal G_{\rm ell}(h)
  +\mathcal G_{\rm par/cusp}(h)+\mathcal G_{\rm hyp}(h).
 \label{eq:selbergtyped}$$ Every displayed term is mandatory. Equation [\[eq:selbergtyped\]](#eq:selbergtyped){reference-type="eqref" reference="eq:selbergtyped"} is a typed schematic identity, not a transcription of a frozen Fourier normalization. This restraint is necessary because the exact cofinite source version was not locally acquired for formula-level checking in this stage [@Selberg1956; @Hejhal1983].

The repeated hyperbolic coefficient in the standard unit-speed convention can be written in the equivalent forms $$\frac{\ell_{\gamma_0}}{2\sinh(r\ell_{\gamma_0}/2)}
 =\frac{(\log N_{\gamma_0})N_{\gamma_0}^{-r/2}}
        {1-N_{\gamma_0}^{-r}},
 \qquad N_{\gamma_0}=\mathrm{e}^{\ell_{\gamma_0}},
 \label{eq:hyperboliccoefficient}$$ with the corresponding test transform evaluated at the repeated length. Selberg/Ruelle zeta relations in hyperbolic settings make the primitive/repetition convention explicit [@Fried1986]. Exactness does not change $N_{\gamma_0}$, a quadratic unit in the modular case, into a rational prime.

## Foliated and relative Lefschetz distributions

Positive-dimensional fixed geometry is not handled by assigning one factor to a family. Kordyukov's relative wave trace assumes a compact smooth Riemannian foliation, a transversally elliptic essentially self-adjoint operator, groupoid smoothing, and a clean relative fixed set [@Kordyukov2001]. The recent foliated-flow formula of @AlvarezKordyukovLeichtnam2026 constructs a Lefschetz distribution using actions on conormal and dual-conormal reduced leafwise cohomology, smoothing $b$-pseudodifferential operators, and regularized $b$-traces. Its hypotheses distinguish simple closed orbits from transversely simple preserved leaves.

This architecture is exact and cohomological. It does not claim a self-adjoint quantum spectrum. Nor does it identify a compact packet of closed orbits in Deninger's topological flow with a preserved leaf or a simple orbit. The smooth manifold, foliation, reduced cohomologies, and $b$-trace construction are missing from the frozen record, so application is [NOT APPLICABLE]{.sans-serif} because named hypotheses fail or are unavailable.

## Ruelle flat trace and Pollicott--Ruelle resonances

Let $V$ generate a compact smooth Anosov flow and put $P_V=(1/i)\mathcal L_V$. Under the normal-return and wavefront conditions, restriction of the propagator kernel to the diagonal defines a flat trace. On scalar functions---the $k=0$ specialization of the differential-form formula---its positive-time orbit distribution has the form $$\operatorname{Tr}^{\flat}\mathrm{e}^{-itP_V}
 =\sum_{\gamma}
   \frac{T_\gamma^\#}{|\det(I-\mathcal P_\gamma)|}
   \delta(t-T_\gamma),\qquad t>0,
 \label{eq:flattrace}$$ where $T_\gamma^\#$ is the primitive period and $\mathcal P_\gamma$ the normal Poincaré map [@DyatlovZworski2016]. On $k$-forms the numerator also carries the corresponding bundle trace $\operatorname{tr}(\wedge^k\mathcal P_\gamma)$. Microlocal anisotropic spaces then give a resonance and zeta architecture under the stated hypotheses.

The generator on anisotropic spaces is generally non-self-adjoint. Consequently an exact classical flat trace or a meromorphic resonance theory does not by itself provide a Hilbert--Pólya Hamiltonian. Equation [\[eq:flattrace\]](#eq:flattrace){reference-type="eqref" reference="eq:flattrace"} also assumes isolated nondegenerate hyperbolic returns; the uncountable equal-period Deninger packets do not satisfy this input model. The compact-manifold theorem is likewise not silently substituted for the cusped modular quotient, whose exact control is Selberg's cofinite identity.

## Gutzwiller semiclassics

Gutzwiller's periodic-orbit expansion is historically a quasiclassical quantization formula involving orbit action, period, Maslov information, and stability [@Gutzwiller1971]. In the rigorous formulation audited here, one studies a family $\widehat H_\hbar=\operatorname{Op}_\hbar(H)$, a compact regular energy shell, a finite time support, and nondegenerate or clean periodic sets. The smoothed regularized density has an orbit expansion modulo $O(\hbar^\infty)$ as $\hbar\downarrow0$ [@CombescureRalstonRobert1999].

This is a proved semiclassical asymptotic, not an exact global identity for one operator at $\hbar=1$. The frozen Deninger source supplies neither $H$, a quantization, an energy shell, nor an $\hbar$-family. A Gutzwiller coefficient cannot be copied to its packet ledger without first constructing and verifying those data.

P0.14P0.19P0.18P0.18P0.18

\
Framework & Analytic ledger & Theorem extent & Orbit geometry & Does not imply\
Framework & Analytic ledger & Theorem extent & Orbit geometry & Does not imply\
wave trace & fixed first-order self-adjoint elliptic operator with real scalar principal symbol & local singular germ / Poisson relation & clean fixed set & full global trace from one orbit\
Selberg & automorphic Laplacian plus scattering & established exact complete framework; local convention not formula-verified here & same-quotient hyperbolic classes & rational-prime support\
foliated Lefschetz & reduced cohomological action and $b$-trace & exact under full regularization & simple orbits and preserved leaves & packet-family trace or quantum spectrum\
Ruelle flat trace & $P_V=(1/i)\mathcal L_V$ and resonances & exact scalar positive-time orbit distribution; bundle trace and resonance domains retained & compact smooth Anosov returns & self-adjoint Hamiltonian\
Gutzwiller & $\hbar$-dependent quantization family & localized semiclassical asymptotic & isolated/clean classical sets & one fixed exact global spectrum\

# Local orbit data do not determine a global trace {#sec:germs}

Let $\mathcal{D}'(Y)$ denote distributions on an open set $Y\subset\mathbb{R}$ and let $\mathcal{E}(Y)=C^\infty(Y)$. Two distributions have the same *full germ* at a point if their restrictions agree on a neighborhood. They have the same *singular germ* if their difference is smooth on a neighborhood, that is, if they agree in the stalk of $\mathcal{D}'/\mathcal{E}$.

[\[prop:onegerm\]]{#prop:onegerm label="prop:onegerm"} Let $T\in\mathbb{R}$, let $U$ be an open neighborhood of $T$, and suppose $\operatorname{int}(\mathbb{R}\setminus U)\ne\varnothing$. For every $\Theta\in\mathcal{D}'(\mathbb{R})$, there is a distinct global distribution $\widetilde\Theta$ with the same full germ on $U$.

Choose nonzero real-valued $\psi\in C_c^\infty(\operatorname{int}(\mathbb{R}\setminus U))$ and put $\widetilde\Theta=\Theta+\psi$. Since $\psi|_U=0$, the restrictions agree on $U$. Globally they differ because $$\langle\widetilde\Theta-\Theta,\psi\rangle
 =\int_{\mathbb{R}}\psi(t)^2\,dt>0.$$

[\[thm:allgerms\]]{#thm:allgerms label="thm:allgerms"} Let $X=\mathbb{R}\setminus\{0\}$, let $P\subset X$, and suppose $\Theta_1,\Theta_2\in\mathcal{D}'(\mathbb{R})$ satisfy $$\operatorname{sing\,supp}(\Theta_j|_X)\subset P,\qquad j=1,2.$$ If they have the same singular germ at every $p\in P$, then $$(\Theta_1-\Theta_2)|_X\in C^\infty(X).$$ The exact ambiguity class left by all nonzero singular germs is therefore $$\mathcal A_0=\{S\in\mathcal{D}'(\mathbb{R}):S|_X\in C^\infty(X)\}.$$ If the singular germ at zero is also fixed, or both distributions are smooth near zero, the ambiguity reduces exactly to $C^\infty(\mathbb{R})$.

Put $S=\Theta_1-\Theta_2$. At each $p\in P$, equality of singular germs makes $S$ smooth on a neighborhood. At each $x\in X\setminus P$, the singular-support hypotheses make both distributions, and hence $S$, smooth near $x$. Local smoothness at every point of $X$, together with the sheaf property, gives $S|_X\in C^\infty(X)$. Conversely, adding any member of $\mathcal A_0$ changes no nonzero singular germ. If the zero germ also agrees, $S$ is smooth near zero and on $X$, hence globally smooth; every global smooth addition conversely preserves all singular germs.

Theorem [\[thm:allgerms\]](#thm:allgerms){reference-type="ref" reference="thm:allgerms"} compares already-existing distributions. It does not say that an arbitrary list of local germs glues to a distribution. If no singular-support prior is known, an unlisted delta singularity can be added, so the smooth-ambiguity conclusion is false. If a fixed operator already defines its wave trace, the theorem does not make that trace ambiguous; it only blocks reconstruction of the full trace from local orbit data alone.

# The modular and prime clocks are non-composable {#sec:clock}

[\[thm:clock\]]{#thm:clock label="thm:clock"} Let $\gamma\in\mathrm{PSL}_2(\mathbb{Z})$ be hyperbolic, let $A$ be either lift to $\mathrm{SL}_2(\mathbb{Z})$, and put $$m=|\operatorname{tr}A|>2,\qquad
 \lambda=\frac{m+\sqrt{m^2-4}}{2}>1.$$ For the unit-speed hyperbolic clock, set $\ell_\gamma=2\log\lambda$ and $N_\gamma=\mathrm{e}^{\ell_\gamma}=\lambda^2$. Then $N_\gamma^r\notin\mathbb{Q}$ for every integer $r\ge1$. Consequently, for every rational prime $p$ and all integers $r,k\ge1$, $$r\ell_\gamma\ne k\log p.$$

Let $D=m^2-4$. It is not a square. Indeed, if $D=a^2$, then $(m-a)(m+a)=4$. The two positive factors have the same parity; the only such factorization is $2\cdot2$, which gives $m=2$, a contradiction. Thus $K=\mathbb{Q}(\sqrt D)$ is quadratic. Its nontrivial automorphism $\sigma$ sends $$\lambda\longmapsto\frac{m-\sqrt D}{2}=\lambda^{-1},
 \qquad N_\gamma\longmapsto N_\gamma^{-1}.$$ If $N_\gamma^r=q\in\mathbb{Q}$, then applying $\sigma$ gives $N_\gamma^{-r}=q=N_\gamma^r$, impossible because $N_\gamma>1$. If $r\ell_\gamma=k\log p$, exponentiation gives $N_\gamma^r=p^k\in\mathbb{Q}$, the same contradiction.

[\[cor:support\]]{#cor:support label="cor:support"} Under the frozen clocks, $$\{r\ell_\gamma:\gamma\text{ primitive modular hyperbolic},\ r\ge1\}
 \cap\{k\log p:p\text{ rational prime},\ k\ge1\}=\varnothing.$$ Hence no atom-by-atom clock-preserving map can transfer the modular hyperbolic coefficient [\[eq:hyperboliccoefficient\]](#eq:hyperboliccoefficient){reference-type="eqref" reference="eq:hyperboliccoefficient"} to Deninger's rational-prime packets.

The corollary does not exclude non-atomic transforms, a new time change, a new arithmetic flow, or a future quantization. It says that the standard unit-speed modular clock and the standard Deninger flow clock cannot be identified on their repeated atoms. A fitted rescaling is not a repair of the frozen candidate; it is a new source lock.

# Separate candidate certificates and Route-A consequences {#sec:candidates}

Table [\[tab:candidatecerts\]](#tab:candidatecerts){reference-type="ref" reference="tab:candidatecerts"} applies the certificate to each candidate without averaging or taking coordinatewise maxima.

P0.12P0.34P0.20P0.235

\
Gate & `DEN-WITT-Z-FIN` & `MOD-GEO` & Boundary\
Gate & `DEN-WITT-Z-FIN` & `MOD-GEO` & Boundary\
T0 & passes source identity & passes source identity & no hybrid record is evaluated\
T1 & packet period and repetition support proved; individual stability, phase, and trace multiplicity missing & primitive hyperbolic classes, repetitions, length, and stability proved & arithmetic period support is not a coefficient\
T2 & no trace or test class; [NOT TESTABLE]{.sans-serif}& exact cofinite framework is proved; convention-dependent local trace/test-class transcription is [NOT TESTABLE]{.sans-serif} in this stage & a hyperbolic-only excerpt is not complete\
T3 & no analytic operator/action or domain; [NOT TESTABLE]{.sans-serif}& automorphic Laplacian, discrete spectrum, and scattering ledger & resonance and self-adjoint ledgers remain distinct\
T4 & cannot be stated & exact global framework; no locally transcribed normalization is claimed & local germs cannot fill missing global terms\
T5 & period only; no return coefficient & same-quotient hyperbolic coefficient & coefficients are not portable labels\
T6 & source clock fixed; trace normalization absent & unit-speed clock is fixed; exact cofinite Fourier/scattering normalization is [NOT TESTABLE]{.sans-serif} locally & convention acquisition remains an explicit obligation\
T7 & prime-log support proved; trace weights [NOT TESTABLE]{.sans-serif}& rational-prime repeated support [REFUTED]{.sans-serif}& Corollary [\[cor:support\]](#cor:support){reference-type="ref" reference="cor:support"}\

For `DEN-WITT-Z-FIN`, T0 and the packet-level part of T1 pass, but T2--T5 cannot be instantiated and T6 lacks a trace normalization. T7 has the correct support but not source-derived trace weights. The appropriate Route-A recommendation is to retain the arithmetic-origin and weak classical gates, retain conventional A2 failure from the packet-product audit, and serialize A3/A4 as downstream failures with evidence [NOT TESTABLE]{.sans-serif}. The smallest positive next theorem is a source-intrinsic analytic object together with an explicit trace or regularization, choice-independent packet disintegration, cross-packet normalization, and a theorem deriving repetition coefficients.

For `MOD-GEO`, the same quotient provides the classical geodesic flow, natural Laplacian, and exact trace architecture. It remains a positive A3/A4 calibration object: partial analytic structure and natural quantization are genuine. For the rational-prime target, however, T7 is refuted and the arithmetic-origin gate fails. Exactness on the wrong atomic support is not a Hilbert--Pólya promotion. Documentary freezing of one complete cofinite convention would improve reproducibility but cannot change Theorem [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"}.

Neither record is Route-B ready. The Deninger object lacks a trace/operator certificate; the modular object fails the target arithmetic map. Combining their favorable coordinates fails Lemma [\[lem:splice\]](#lem:splice){reference-type="ref" reference="lem:splice"} and Corollary [\[cor:support\]](#cor:support){reference-type="ref" reference="cor:support"}.

# Deterministic controls and falsification cases {#sec:controls}

The accompanying standard-library Python code implements three controls. None supplies evidence for a Riemann-zero match.

1.  For integral hyperbolic traces $3\le m\le20$ and repetitions $1\le r\le6$, 108 exact quadratic-field rows verify algebraic norm one, Galois conjugate equal to the inverse, and nonzero irrational coefficient. The finite table is a regression control for Theorem [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"}; the theorem, not decimal separation, proves the universal claim.

2.  On a 501-point grid, a compact smooth bump supported in $[2.1,2.9]$ is added to a regularized proxy whose audited neighborhood is $[0.8,1.2]$. All 41 audited samples have difference zero while the global maximum difference is $0.75$. This illustrates Proposition [\[prop:onegerm\]](#prop:onegerm){reference-type="ref" reference="prop:onegerm"}; it is not a numerical model of a distributional trace.

3.  A typed provenance audit lets incomplete same-source records pass T0, because T0 checks identity rather than completeness. It rejects a fully populated DEN/MOD splice and rejects a modular record whose clock field comes from a post-hoc rescaled source lock.

The run records zero Riemann-zero inputs, zero fitted parameters, zero network inputs, no random seed, and no transcribed cofinite Selberg formula. Eleven unit tests cover quadratic arithmetic, bump support, certificate provenance, determinism, and manifest tamper detection.

P0.28\>X Control & Falsified inference\
closed hyperbolic surface & exact same-object trace and a natural Laplacian do not imply rational-prime arithmetic\
local germ plus smooth shift & one exact orbit germ does not identify the global trace\
$\hbar$-family & a localized semiclassical asymptotic is not a fixed-operator exact identity\
modular continuum omitted & deleting scattering/continuous terms destroys completeness of the cofinite identity\
clock rescaled & post-hoc time change creates a new candidate/source lock\
DEN+MOD splice & populated coordinates do not overcome T0 or disjoint clocks\

# Limitations {#sec:limitations}

This paper certifies inference boundaries for two frozen records. It is not a universal no-go theorem for arithmetic dynamics, trace formulae, or quantization.

First, the Selberg discussion intentionally uses the typed cofinite identity [\[eq:selbergtyped\]](#eq:selbergtyped){reference-type="eqref" reference="eq:selbergtyped"}. The original article was not stored locally, and the Hejhal locator was verified from authoritative metadata rather than a locally read copy. A complete convention, including test class, Fourier normalization, signs, cusp terms, and scattering normalization, remains an acquisition obligation. No conclusion here depends on guessing those constants; the support theorem is algebraic.

Second, the five-family review is targeted rather than systematic. It selects primary theorem sources capable of deciding the semantic distinctions needed by T2--T6. It does not exhaust operator-algebraic or noncommutative-geometric trace constructions. Missing hypotheses show only that the named theorems do not apply to the frozen Deninger object.

Third, Theorem [\[thm:allgerms\]](#thm:allgerms){reference-type="ref" reference="thm:allgerms"} assumes that the possible nonzero singular support lies in the set $P$. Without that prior, additional unlisted singularities may be inserted. The theorem also does not address whether prescribed local germs are globally compatible.

Fourth, Corollary [\[cor:support\]](#cor:support){reference-type="ref" reference="cor:support"} rules out an atomwise standard-clock identification. It does not rule out non-atomic integral transforms, a new time change, or a new arithmetic object. Such modifications must be declared and audited as new candidates rather than counted as properties of either frozen record.

Finally, all computations are finite controls. Their exact rational arithmetic and checksum determinism guard the implementation, but they do not prove a trace formula, a determinant, spectral self-adjointness, or the Riemann hypothesis.

# Conclusion

One orbit contribution, however exact, is not a global trace. The analytic meaning of a trace comes from a specified functional, test class, operator or action, theorem extent, coefficient theorem, clock, normalization, and all non-orbit terms. The same-object certificate T0--T7 records these obligations without conflating wave, Selberg, foliated, flat/resonance, and semiclassical theorem types.

The frozen candidates demonstrate complementary successes. Deninger's flow derives rational primes and periods $\log p$ from arithmetic geometry, but does not yet define the trace and analytic ledger needed for A3--A4. The modular geodesic flow and Laplacian form an exact same-geometry trace benchmark, but their repeated length support is disjoint from every $k\log p$. These coordinates cannot be pasted together: the record fails T0, and a clock-preserving atomwise bridge fails by quadratic conjugation.

The useful next step is therefore constructive and source-intrinsic. For the Deninger record it is a packet-to-trace theorem that fixes the analytic object, test class, disintegration, normalization, and repeated coefficients. For the modular record it is only a documentary convention freeze, not an arithmetic rescue. Until such new mathematics exists, Route B remains closed.

# Reproducibility and declarations {#reproducibility-and-declarations .unnumbered}

#### Data and code availability.

All protocols, source matrices, proof audits, deterministic Python code, tests, experiment script, result tables, checksums, figure source, and manuscript source are included under . Run from that directory. No proprietary or Riemann-zero dataset is used.

#### Ethics statement.

This theoretical and computational study involves no human participants, animals, intervention, personal data, or identifiable information. No institutional ethics review was required.

#### CRediT authorship contribution statement.

Liang Wang: Conceptualization, Methodology, Formal analysis, Investigation, Software, Validation, Data curation, Visualization, Writing---original draft, and Writing---review and editing.

#### Funding.

No project-specific external funding source was declared for this work.

#### Conflict of interest.

The author declares no financial or non-financial conflict of interest relevant to this study.

#### AI-assistance disclosure.

OpenAI Codex assisted with literature organization, deterministic implementation, source-to-claim auditing, adversarial proof checking, and manuscript preparation. No generative system is credited as an author. The named author is responsible for source verification, mathematical claims, artifact release, and the final text.

# Claim-to-evidence ledger

P0.38P0.18P0.34

\
Claim & Status & Basis and boundary\
Claim & Status & Basis and boundary\
Deninger packets have least period $\log p$ & [PROVED]{.sans-serif}& primary source; no trace weight follows\
one local full germ determines a global trace & [REFUTED]{.sans-serif}& Proposition [\[prop:onegerm\]](#prop:onegerm){reference-type="ref" reference="prop:onegerm"}\
all nonzero singular germs determine a trace uniquely & [REFUTED]{.sans-serif}& exact ambiguity $\mathcal A_0$ in Theorem [\[thm:allgerms\]](#thm:allgerms){reference-type="ref" reference="thm:allgerms"}\
a coordinatewise DEN/MOD record passes object identity & [REFUTED]{.sans-serif}& Lemma [\[lem:splice\]](#lem:splice){reference-type="ref" reference="lem:splice"}\
modular repeated lengths meet prime-power logs & [REFUTED]{.sans-serif}& Theorem [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"} and Corollary [\[cor:support\]](#cor:support){reference-type="ref" reference="cor:support"}\
the complete modular Selberg framework is exact & framework [PROVED]{.sans-serif}; local convention [NOT TESTABLE]{.sans-serif}& primary/authority sources; no local formula normalization claimed\
DG supplies a global orbit sum from one clean orbit & not claimed & source certifies local singular information\
Ruelle resonances are a self-adjoint quantum spectrum & not claimed & analytic ledgers are distinct\
Gutzwiller is a fixed-operator exact identity & not claimed & rigorous result is a localized $\hbar\to0$ asymptotic\
all future Deninger quantizations are impossible & not claimed & outside frozen-object applicability audit\
Deninger candidate has authorized, testable Route-B entry & [NOT TESTABLE]{.sans-serif}& required Hilbert space, operator, and domain are absent; entry unauthorized\
modular candidate has Route-B entry for the rational-prime target & not authorized & Route A is rejected for that target and cannot be rescued downstream\

# Artifact map

P0.40P0.50 Relative path & Purpose\
Relative path & Purpose\
& preregistered question, objects, clocks, T0--T7, controls, and decision rules\
& primary-source ledger, locators, applicability matrix, and acquisition limitations\
& full proofs, exact claim boundaries, and candidate recommendations\
& frozen claim ledger and manuscript constraints\
& exact quadratic arithmetic, sampled germ, and provenance controls\
& eleven deterministic unit tests\
& one-command reproduction entry point\
& 108 exact finite quadratic-field rows\
& sampled smooth-shift illustration\
& same-source, splice, and clock-lock provenance results\
& parameters, theorem statuses, and forbidden-input declaration\
& artifact integrity manifest\
& certificate diagram source\
