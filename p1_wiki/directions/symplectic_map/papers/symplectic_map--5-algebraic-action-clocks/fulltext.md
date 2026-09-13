---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--5-algebraic-action-clocks"
canonical_tex: "symplectic_map/papers/5-algebraic-action-clocks/paper/manuscript.tex"
canonical_pdf: "symplectic_map/papers/5-algebraic-action-clocks/paper/manuscript.pdf"
source_sha256: "41ed1c1492da4f1cc8ff1cb7747c97c2ecf1f313c2390469219485b5c1d087aa"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Normalized Algebraic Periodic Actions versus Prime Logarithms: A Hénon Design Certificate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/5-algebraic-action-clocks>)
- [规范 TeX](<../../../../../symplectic_map/papers/5-algebraic-action-clocks/paper/manuscript.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/5-algebraic-action-clocks/paper/manuscript.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/5-algebraic-action-clocks/README.md>)
- [BibTeX](<../../../../../symplectic_map/papers/5-algebraic-action-clocks/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let an exact symplectic map, a Liouville primitive, and a single-valued rational exact potential be defined over $\overline{\mathbb Q}$. If the potential is regular on an algebraic period-$n$ orbit, then its one-traversal action is a finite sum of algebraic values and hence algebraic. Hermite--Lindemann therefore prevents this normalized action from equalling any branch of $\log\beta$ for nonzero algebraic $\beta\ne1$, in particular the positive real value $\log p$ for a rational prime. The conclusion persists under fixed algebraic scales, averages, repetitions, and algebraic exact gauges, provided the full endpoint term is retained. It fails as a map-only statement: for the identity map, the constant potential $G\equiv\log 2$ is a symbolic exact countercontrol once transcendental normalization is allowed.

  For $H_a(q,p)=(q^2-a-p,q)$ we verify $H_a^*(p\,dq)-p\,dq=d(2q^3/3-pq)$ and show that the usual type-1 generating function has the opposite sign on the graph. Every finite periodic point is algebraic for algebraic $a$. If $a$ is $S$-integral in a base field, then in the orbit field only $3\mathcal A$ is certified $S$-integral in general; the fixed-point action $-1/3$ makes this denominator sharp. A source-locked eight-stage static audit and 82 passing tests verify the implementation while computing no candidate orbit or action. This is a narrow normalization-aware design certificate, not a universal no-go theorem for symplectic clocks.
author:
- Anonymous
bibliography:
- references.bib
date: 'Pre-review manuscript, August 2026'
title: |
  **Normalized Algebraic Periodic Actions versus Prime Logarithms:\
  A Hénon Design Certificate**
```

## Markdown 正文

# Introduction {#sec:introduction}

Periodic-orbit descriptions of spectral problems naturally suggest looking for a dynamical quantity proportional to a prime logarithm. The Berry--Keating discussion is one familiar source of this heuristic scale [@berry1999riemann]. Here we ask a strictly prior design question: can a closed generating-function action of an algebraic exact-symplectic map, with its representative fixed before any orbit is evaluated, equal $\log p$ *exactly*? We import neither prime tables nor zero ordinates, and we do not attempt a trace formula or an approximate fit.

This question contains a normalization trap. If $F^*\theta-\theta=dG$, then $G+C$ is another exact potential for every constant $C$. A period-$n$ action changes by $nC$. Absolute action is therefore not a map-only invariant; one must record the primitive, potential, additive representative, domain, and any endpoint convention. Exact symplectic literature routinely uses generating actions, action differences, and variational principles [@kook1989periodic; @mackay1984transport; @meiss1992symplectic; @delshams1997melnikov], while action and average-action spectra emphasize the importance of iteration conventions [@ginzburg2009action; @mazzucchelli2013degenerate]. Our contribution is not a new definition of action. It is a provenance certificate for one frozen arithmetic representative.

The certificate has four parts.

1.  Regular evaluation of a $\overline{\mathbb Q}$-rational potential on a finite algebraic orbit places the action in $\overline{\mathbb Q}$ at every period. Hermite--Lindemann then excludes every logarithm branch of every nontrivial algebraic target.

2.  A complete stepwise gauge ledger shows exactly what telescopes and what remains. Algebraic endpoint mismatches and constants alter the value but not its algebraicity. A transcendental constant defeats the conclusion and is therefore an assumption boundary, not an inconvenient special case.

3.  The quadratic Hénon automorphism gives an explicit specialization: the exact potential and type-1 generating function have opposite signs, all finite periodic points are algebraic, and the justified integral refinement is $3\mathcal A\in\mathcal O_{K,S}$, not $\mathcal A\in\mathcal O_{K,S}$.

4.  A source-locked static program audits identities, domain gates, normalization controls, and proof dependencies. It performs no candidate periodic-point solve or candidate action evaluation, so its outputs are implementation evidence rather than empirical support for the theorem.

Figure [1](#fig:action-certificate){reference-type="ref" reference="fig:action-certificate"} displays both the implication and its normalization boundary. The scope is intentionally narrow. We do not exclude $\log|\mathcal A|$, multiplier or return-time clocks, multivalued potentials, closed non-exact changes of primitive, transcendental normalizations, or approximate matching.

![The all-period implication is conditional on regular algebraic evaluation and a frozen algebraic representative. Algebraic gauges and constants remain inside the certificate when the full endpoint ledger is retained. The symbolic identity-map control shows that a transcendental additive constant can inject the target. The right-hand box lists observables and cocycles not decided here. All categorical statuses are read from the frozen static-audit package.](<../../../../../symplectic_map/papers/5-algebraic-action-clocks/paper/figures/fig1_action_certificate.pdf>){#fig:action-certificate width="\\linewidth"}

# Exact action and arithmetic context {#sec:context}

Let $X$ be an algebraic variety over $\overline{\mathbb Q}$, let $U\subset X$ be an open set, and let $F:U\dashrightarrow X$ be a rational map. On the associated complex phase space, suppose a single-valued one-form $\theta$ and a single-valued rational function $G\in\overline{\mathbb Q}(X)$ satisfy $$F^*\theta-\theta=dG
  \label{eq:exact-potential}$$ where all terms are defined. For an orbit $P_{j+1}=F(P_j)$ with $P_n=P_0$, define the one-traversal potential action $$\mathcal A_G(P_0)=\sum_{j=0}^{n-1}G(P_j).
  \label{eq:action-definition}$$ The regularity clause is part of the definition used here: every map step is defined, every $P_j$ lies in $X(\overline{\mathbb Q})$, and $G$ has no pole at any $P_j$.

The distinction between absolute actions and action differences is essential. The latter often remove additive constants and carry geometric information about transport [@mackay1984transport; @meiss1992symplectic]; the present proposal needs an absolute value. Likewise, a discrete type-1 generating function can define a variational sum [@kook1989periodic; @mazzucchelli2013degenerate; @bialy2023locally], but its sign and endpoint convention must be matched to [\[eq:exact-potential\]](#eq:exact-potential){reference-type="eqref" reference="eq:exact-potential"} rather than assumed. Exact potential conventions and their additive ambiguity are standard [@delshams1997melnikov].

The arithmetic input is elementary until the last step. Rational functions defined over $\overline{\mathbb Q}$ take algebraic values at algebraic points whenever their denominators do not vanish; $\overline{\mathbb Q}$ is a field; and a finite sum remains algebraic. The transcendence input is the classical Hermite--Lindemann theorem: if $0\ne\alpha\in\overline{\mathbb Q}$, then $e^\alpha$ is transcendental [@baker2022transcendental]. We use this theorem, not any stronger result on linear forms in logarithms.

The Hénon example belongs to the standard class of polynomial plane automorphisms [@friedland1989dynamical]. Quadratic symplectic maps and their normal forms have a long history [@moser1994quadratic], and recent work continues to study arithmetic periodic points and broader open problems [@dehenon2024open; @kim2024many]. None of these sources is cited for the paper-specific algebraic-action certificate or the denominator-three calculation.

::: {#tab:context}
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Theme                Typical role                                                           Boundary in this paper
  -------------------- ---------------------------------------------------------------------- ---------------------------------------------------------------------------------------
  Generating actions   Variational characterization of periodic orbits                        We freeze one algebraic exact potential and audit its absolute value.

  Action differences   Transport, barriers, and geometry                                      Constant ambiguity often cancels; our proposed clock needs an absolute normalization.

  Action spectra       Periodic values and behavior under iteration                           We distinguish one traversal, averages, and repetitions explicitly.

  Hénon dynamics       Polynomial automorphisms, symplectic normal forms, arithmetic cycles   Supplies an exact specialization, not evidence for a universal statement.

  Transcendence        Algebraic values versus exponentials                                   Hermite--Lindemann converts algebraicity into an exact exclusion of $\log\beta$.

  This paper           Pre-execution arithmetic provenance                                    Certifies one normalized algebraic action route and leaves other clocks open.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : The present question relative to adjacent uses of periodic action.
:::

# The algebraic-action certificate {#sec:certificate}

We first separate finite evaluation from transcendence.

[\[thm:evaluation\]]{#thm:evaluation label="thm:evaluation"} Let $F$, $G$, and $(P_0,\ldots,P_{n-1})$ satisfy the hypotheses above. Then $$\mathcal A_G(P_0)\in\overline{\mathbb Q}.
  \label{eq:algebraic-action}$$ The conclusion holds for every finite $n$; it does not arise from a bounded period search.

Because $P_j\in X(\overline{\mathbb Q})$ and $G\in\overline{\mathbb Q}(X)$ is regular at $P_j$, evaluation gives $G(P_j)\in\overline{\mathbb Q}$ for each $j$. The action is a sum of exactly $n$ such values. Closure of $\overline{\mathbb Q}$ under finite addition proves [\[eq:algebraic-action\]](#eq:algebraic-action){reference-type="eqref" reference="eq:algebraic-action"}.

The theorem also applies to step-dependent maps and potentials: if every $F_j$ is defined over $\overline{\mathbb Q}$, every step is defined at its current point, and every $G_j(P_j)$ is pole-free, then $\sum_jG_j(P_j)$ is algebraic. One must check the terms before summation. A formal cancellation of undefined expressions cannot certify an action.

[\[cor:log-target\]]{#cor:log-target label="cor:log-target"} Under Theorem [\[thm:evaluation\]](#thm:evaluation){reference-type="ref" reference="thm:evaluation"}, let $\beta\in\overline{\mathbb Q}$. If $\beta\ne0,1$, then $\mathcal A_G(P_0)$ is not any complex logarithm of $\beta$. If $\beta=0$, no complex logarithm exists. For $\beta=1$, equality with a branch is possible only in the algebraic case $\mathcal A_G(P_0)=0$, corresponding to the zero branch. In particular, $$\mathcal A_G(P_0)\ne\log p
  \qquad\text{for every rational prime }p,
  \label{eq:prime-log-exclusion}$$ where $\log p$ denotes the positive real logarithm.

If $\mathcal A_G$ were a complex logarithm of a nonzero $\beta$, then $e^{\mathcal A_G}=\beta$. When $\mathcal A_G\ne0$, Hermite--Lindemann says that the left side is transcendental, contradicting algebraicity of $\beta$. Thus an algebraic logarithm must be zero, forcing $\beta=1$. The zero target has no logarithm in $\mathbb C$. Equation [\[eq:prime-log-exclusion\]](#eq:prime-log-exclusion){reference-type="eqref" reference="eq:prime-log-exclusion"} follows because $p\in\overline{\mathbb Q}\setminus\{0,1\}$.

The same argument closes several nearby conventions, provided every new coefficient is frozen and algebraic.

[\[prop:extensions\]]{#prop:extensions label="prop:extensions"} Let $A=\mathcal A_G(P_0)\in\overline{\mathbb Q}$, let $c\in\overline{\mathbb Q}^*$, and let $r,n\in\mathbb Z_{>0}$. Then $cA$, $A/n$, and $rA$ are algebraic and cannot equal $\log\beta$ for $\beta\in\overline{\mathbb Q}\setminus\{0,1\}$. Under the standard embedding $\overline{\mathbb Q}\hookrightarrow\mathbb C$, the numbers $\operatorname{Re}A$, $\operatorname{Im}A$, and $|A|$ are algebraic and obey the same exclusion.

The scaled, averaged, and repeated values are algebraic by field closure. If $A$ is algebraic, so is its complex conjugate $\bar A$; hence $\operatorname{Re}A=(A+\bar A)/2$ and $\operatorname{Im}A=(A-\bar A)/(2i)$ are algebraic. Also $|A|^2=A\bar A$ is algebraic, and any square root of an algebraic number is algebraic. Corollary [\[cor:log-target\]](#cor:log-target){reference-type="ref" reference="cor:log-target"} applies to each resulting algebraic value.

Proposition [\[prop:extensions\]](#prop:extensions){reference-type="ref" reference="prop:extensions"} proves that $|A|$ cannot itself equal $\log p$. It says nothing about $\log|A|$. Indeed, an algebraic action with $|A|=p$ would produce $\log|A|=\log p$ by post-processing. The argument also does not control $\arg A$ or approximate equality.

# Gauge ledger and normalization countercontrols {#sec:gauge}

Suppose first that $\theta'=\theta+d\chi$ for a single-valued rational function $\chi$. Then $$\begin{aligned}
F^*\theta'-\theta'
 &=F^*\theta-\theta+d(\chi\circ F-\chi) \\
 &=d\bigl(G+\chi\circ F-\chi+C\bigr)\end{aligned}$$ for an arbitrary constant $C$. Thus one may take $$G'=G+\chi\circ F-\chi+C.
  \label{eq:autonomous-gauge}$$ On a closed period-$n$ orbit, single-valuedness gives $$\mathcal A_{G'}-\mathcal A_G=nC.
  \label{eq:autonomous-shift}$$ Consequently $C=0$ preserves the numerical action; any algebraic $C$ preserves its algebraicity; a transcendental $C$ may destroy the certificate.

For a stepwise sequence, the general endpoint formula is more informative. Let $P_{j+1}=F_j(P_j)$ and take $$G'_j=G_j+\chi_{j+1}\circ F_j-\chi_j+C_j.
 \label{eq:step-gauge}$$ Every transition, gauge value, and potential value is assumed separately defined. Direct summation telescopes to $$\sum_{j=0}^{n-1}G'_j(P_j)-\sum_{j=0}^{n-1}G_j(P_j)
 =\chi_n(P_n)-\chi_0(P_0)+\sum_{j=0}^{n-1}C_j.
 \label{eq:general-endpoint}$$ Endpoint compatibility $\chi_n(P_n)=\chi_0(P_0)$ permits the shorter constant-sum formula. Without compatibility the endpoint mismatch remains; if it and all $C_j$ are algebraic, the shifted action is still algebraic and the prime-log exclusion still holds. Compatibility is a value-simplifying condition, not a prerequisite for algebraicity.

Figure [2](#fig:gauge-scope){reference-type="ref" reference="fig:gauge-scope"} summarizes exact positive, negative, and edge controls. A pole or undefined step stops evaluation. A multivalued gauge with untracked monodromy lies outside the formula. The $\beta=0$ and $\beta=1$ rows record the two necessary logarithm edge cases. The matrix is categorical: each cell is derived from named frozen-result predicates or marked as theorem-defined in an explicit scope ledger; it does not numerically evaluate a logarithm.

![The stepwise gauge ledger and source-locked scope matrix. "Certified" means that the stated formula or algebraicity consequence is justified under the row's assumptions; "stop/out" means that the action certificate cannot be applied; "edge" marks a logarithm-domain exception or a statement needing separate interpretation. The cell provenance is recorded separately as frozen-JSON-derived or theorem-defined; the latter is not presented as a raw computational result. In particular, an algebraic endpoint mismatch retains the prime-log exclusion, while $\log|\mathcal A|$ remains outside the theorem.](<../../../../../symplectic_map/papers/5-algebraic-action-clocks/paper/figures/fig2_gauge_scope_matrix.pdf>){#fig:gauge-scope width="\\linewidth"}

[\[prop:identity-control\]]{#prop:identity-control label="prop:identity-control"} Exactness of the map alone does not force algebraicity of its absolute action. On $X=\mathbb A^2$ take $F=\operatorname{id}$ and $\theta=p\,dq$. The constant potential $G\equiv\log 2$ satisfies $F^*\theta-\theta=0=dG$, while every point is fixed and has one-step action $\log 2$.

The proposition is a symbolic control: "$\log 2$" is a formal constant label and no decimal logarithm or external target table is evaluated. It shows why the hypothesis $G\in\overline{\mathbb Q}(X)$, including its additive normalization, cannot be removed. More generally, after an orbit and its action $A$ are known, the post-hoc choice $$C=\frac{\log p-A}{n}
  \label{eq:target-injection}$$ forces the shifted action to equal $\log p$. This is target injection, not an intrinsic clock. The source lock forbids orbit-dependent or target-dependent normalization.

Three nearby constructions require new ledgers rather than a silent reuse of [\[eq:general-endpoint\]](#eq:general-endpoint){reference-type="eqref" reference="eq:general-endpoint"}: a multivalued $\chi$ may carry monodromy; a closed but non-exact change of primitive need not be $d\chi$; and a local potential may not extend single-valuedly around the orbit. None is ruled out by the present certificate.

# The algebraic Hénon certificate {#sec:henon}

For $a\in\overline{\mathbb Q}$, consider $$H_a(q,p)=(q^2-a-p,q),
  \qquad H_a^{-1}(q,p)=(p,p^2-a-q).
  \label{eq:henon-map}$$ Its Jacobian matrix is $$DH_a(q,p)=\begin{pmatrix}2q&-1\\1&0\end{pmatrix},
  \qquad \det DH_a=1.$$ With $\theta=p\,dq$, direct pullback gives $$\begin{aligned}
 H_a^*\theta-
 \theta
 &=q\,d(q^2-a-p)-p\,dq \\
 &=(2q^2-p)\,dq-q\,dp \\
 &=d\left(\frac23q^3-pq\right).
 \label{eq:henon-potential}\end{aligned}$$ Thus our potential convention is $$G(q,p)=\frac23q^3-pq.
  \label{eq:G}$$

The type-1 generating function $$L_a(q,Q)=\frac13q^3-aq-qQ
  \label{eq:L}$$ satisfies $p=\partial_qL_a=q^2-a-Q$ and $P=-\partial_QL_a=q$, so its graph is precisely $Q=q^2-a-p$, $P=q$. Substitution on the graph gives $$L_a(q,Q)=-\frac23q^3+pq=-G(q,p).
  \label{eq:sign}$$ The two conventional closed sums therefore have opposite sign. Both remain algebraic and both are excluded from $\log p$ under the frozen algebraic normalization; nevertheless, sign must not be hidden in a comparison of numerical action values.

Writing a periodic orbit as $P_j=(q_j,p_j)$ gives $p_j=q_{j-1}$ and the cyclic recurrence $$q_{j+1}+q_{j-1}=q_j^2-a,
  \qquad j\in\mathbb Z/n\mathbb Z.
  \label{eq:recurrence}$$ For $n=1$ the two ordered neighbor slots both equal $q_0$; for $n=2$ they both equal the other coordinate. The multiplicity is structural and must not be collapsed.

[\[thm:henon\]]{#thm:henon label="thm:henon"} Let $a\in\overline{\mathbb Q}$. Every finite periodic point of $H_a$ has coordinates in $\overline{\mathbb Q}$. For every such period-$n$ orbit, $$\mathcal A_G
  =\sum_{j=0}^{n-1}\left(\frac23q_j^3-q_{j-1}q_j\right)
  \in\overline{\mathbb Q},
  \label{eq:henon-action}$$ and $\sum_jL_a(q_j,q_{j+1})=-\mathcal A_G$. Neither action convention equals $\log p$ for a rational prime.

Homogenize the $n$ equations [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} in $[Q_0:\cdots:Q_{n-1}:Z]\in\mathbb P^n$. At $Z=0$, every equation reduces to $Q_j^2=0$, hence every $Q_j=0$, which is not a projective point. Thus the projective zero scheme has no point on the hyperplane at infinity. A positive-dimensional projective component would intersect the fixed hyperplane $Z=0$, where we just proved that there is no point. Hence the projective scheme is zero-dimensional. Consequently the affine cyclic system has finitely many points and is cut out over the number field $\mathbb Q(a)$; all $q_j$ are algebraic over $\mathbb Q(a)$ and hence over $\mathbb Q$. Since $p_j=q_{j-1}$, all phase-space coordinates are algebraic. Formula [\[eq:henon-action\]](#eq:henon-action){reference-type="eqref" reference="eq:henon-action"} follows from [\[eq:G\]](#eq:G){reference-type="eqref" reference="eq:G"}, and each term is algebraic. The sign identity follows from [\[eq:sign\]](#eq:sign){reference-type="eqref" reference="eq:sign"}; the logarithmic exclusion follows from Corollary [\[cor:log-target\]](#cor:log-target){reference-type="ref" reference="cor:log-target"}.

The elementary argument above proves algebraicity, not a count of exact periodic points or a transversality statement. Scheme multiplicities are irrelevant to the evaluation conclusion.

[\[cor:s-integral\]]{#cor:s-integral label="cor:s-integral"} Let $K_0$ be a number field, let $S_0$ contain its archimedean places, and assume $a\in\mathcal O_{K_0,S_0}$. For a finite periodic orbit choose a finite extension $K/K_0$ containing every orbit coordinate, and let $S$ be the places of $K$ above $S_0$, together with all archimedean places. Then every $q_j,p_j$ lies in $\mathcal O_{K,S}$ and $$3\mathcal A_G\in\mathcal O_{K,S}.
  \label{eq:three-action}$$ Equivalently, $\mathcal A_G$ is integral away from $S$ and places above the rational prime $3$.

Fix a non-Archimedean place $v\notin S$. Then $|a|_v\le1$. If $R=\max_j|q_j|_v>1$, choose $j$ with $|q_j|_v=R$. By the ultrametric inequality, $$|q_j^2-a|_v=R^2,
 \qquad
 |q_{j+1}+q_{j-1}|_v\le R,$$ contradicting [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}. Hence every $q_j$ and thus every $p_j=q_{j-1}$ is $S$-integral. Finally, $$3\mathcal A_G
 =\sum_{j=0}^{n-1}\left(2q_j^3-3q_{j-1}q_j\right)$$ is an integer-coefficient polynomial in those coordinates.

The factor $3$ is necessary in general. At $a=-1$, the point $(q,p)=(1,1)$ is fixed because $1^2-(-1)-1=1$, and $$\mathcal A_G=G(1,1)=\frac23-1=-\frac13,
  \qquad 3\mathcal A_G=-1.
  \label{eq:sharp-third}$$ Thus we claim only [\[eq:three-action\]](#eq:three-action){reference-type="eqref" reference="eq:three-action"}; we do not claim that $\mathcal A_G$ is integral at places above $3$.

Figure [3](#fig:henon-static){reference-type="ref" reference="fig:henon-static"} records the exact identity and proof ledgers. The no-infinity rows at periods $1,2,3,5$ audit the generic leading-system construction; they are not a finite-period proof of Theorem [\[thm:henon\]](#thm:henon){reference-type="ref" reference="thm:henon"}. The theorem uses the displayed all-$n$ argument.

![The Hénon specialization as an exact static certificate. The top panels track the one-form identity, determinant, $G/L$ sign, and low-period neighbor multiplicity. The lower panels distinguish the all-period no-infinity proof ledger from the valuation refinement. The fixed point with action $-1/3$ makes the denominator-three boundary sharp. No periodic equation was solved to construct the figure.](<../../../../../symplectic_map/papers/5-algebraic-action-clocks/paper/figures/fig3_henon_static_certificate.pdf>){#fig:henon-static width="\\linewidth"}

# Source-locked static implementation audit {#sec:audit}

The mathematical conclusion is all-period and deductive. The accompanying software has a narrower role: it checks whether the implemented formulas, scope stops, normalization controls, and proof dependencies match the frozen protocol. Before the formal static run, a versioned source lock fixed the candidate ID, hypotheses, nonclaims, registered stages, forbidden data, and zero-candidate-execution rule. An independent pre-run Round-3 review issued `DEPLOYMENT_PASS` for that static protocol.

The official registry contains eight ordered entries:

  Stage        Result   Role
  ------------ -------- --------------------------------------------------------
  R000         PASS     source-lock hash and zero-execution provenance
  R001         PASS     executable-source isolation scan
  R002         PASS     structured proof-contract integrity
  R010--R019   PASS     controls-first gauge, domain, target, and edge checks
  R020         PASS     Hénon inverse, Jacobian, one-form, and sign identities
  R021         PASS     low-period ordered-slot multiplicity
  R022         PASS     projective leading-system proof ledger
  R023         PASS     orbit-field valuation and denominator-three ledger

All controls ran before the Hénon static stages. The official safe suite reported 82 tests, zero failures, and zero errors. The final result manifest closed exactly over 35 declared files, including seven JSON outputs, three human-readable reports, JUnit XML, the proof package, source lock, experiment documents, and executable sources. Every registered stage passed.

Most importantly, the audit records all of the following as false: candidate parameter substitution, candidate periodic-point computation, candidate action computation, external prime-table access, Riemann-zero-data access, network access by the executable, and floating-point equality evidence. The symbolic label `LOG_OF_TARGET_TWO` is used only to exercise the normalization boundary. R020--R023 manipulate generic symbols and exact identities; they do not open a candidate search.

This division of labor prevents a common category error. The JSON outputs do not establish that every period has algebraic action; Theorem [\[thm:henon\]](#thm:henon){reference-type="ref" reference="thm:henon"} does. Conversely, the theorem does not establish that a particular software path honors the intended endpoints and stop rules; the static audit tests that implementation. Appendix [10](#app:reproducibility){reference-type="ref" reference="app:reproducibility"} gives hashes and reproduction commands.

# Interpretation, route decision, and limitations {#sec:interpretation}

The strongest justified decision is

> `GO_AS_NARROW_DESIGN_CERTIFICATE`: close only the frozen, normalized algebraic absolute action as an exact prime-logarithm clock.

This is stronger than a finite non-observation because it holds at every period under stated hypotheses. It is weaker than a map-level obstruction because Proposition [\[prop:identity-control\]](#prop:identity-control){reference-type="ref" reference="prop:identity-control"} shows that normalization can change the arithmetic class. The certificate should therefore be used as a pre-execution filter: before searching or fitting, ask whether the proposed observable is already forced into $\overline{\mathbb Q}$.

The precise surviving directions are as follows.

-   **Logarithmic post-processing.** The theorem excludes $|\mathcal A|=\log p$, not $\log|\mathcal A|=\log p$.

-   **Transcendental normalization.** A frozen, target-independent transcendental constant is outside the theorem. Its mathematical origin would need separate justification; post-hoc target injection is not admissible.

-   **Multivalued or topological cocycles.** Monodromy and closed non-exact primitive changes require a branch or cohomology ledger.

-   **Different observables.** Multiplier logs, return times, energy derivatives, infinite-place or adelic quantities are not actions of the form [\[eq:action-definition\]](#eq:action-definition){reference-type="eqref" reference="eq:action-definition"}.

-   **Approximation.** Algebraicity does not prevent algebraic numbers from approximating transcendental ones. No quantitative separation or fit statistic is proved here.

The Hénon result is equally scoped. We prove algebraicity of finite periodic points and $S$-integrality of $3\mathcal A_G$ for the stated quadratic map. We do not classify periodic points, periods, branches at infinity, multiplier clocks, or analytic continuations. We do not assert a prime-orbit correspondence, a dynamical zeta identity, a spectral determinant, a trace formula, or a quantization. In particular, the paper is not a universal no-go theorem for symplectic or arithmetic dynamics.

The individual ingredients are classical or elementary. The literature audit located no basis for a historical-first claim, and none is made. The standalone contribution is the complete normalization-aware, source-locked certificate and its exact Hénon instantiation. If a publication venue requires substantially deeper standalone novelty, the planned disposition is : merge this certificate into a broader obstruction synthesis rather than claim greater standalone depth.

# Conclusion {#sec:conclusion}

A regular finite sum of a frozen $\overline{\mathbb Q}$-rational exact potential on an algebraic periodic orbit is algebraic. Hermite--Lindemann then rules out an exact equality with $\log p$ at every period. The statement survives algebraic scales and algebraic exact gauges only when endpoints and constants are tracked; the symbolic identity-map control shows why arbitrary transcendental normalization cannot be ignored. For the quadratic Hénon map the exact potential is opposite in sign to the type-1 generating function, all finite periodic points are algebraic, and only $3\mathcal A$ is generally $S$-integral, sharply.

The result is best understood as an arithmetic provenance test, not as a new transcendence theorem and not as a universal obstruction to dynamical clocks. A natural next project is a separately source-locked intrinsic nonalgebraic or multivalued clock with a complete branch, endpoint, and target independence ledger.

[\[page:conclusion-end\]]{#page:conclusion-end label="page:conclusion-end"}

# Hénon geometry and valuation details {#app:henon-details}

This appendix records the two degeneracies most likely to be lost in a compressed implementation. For period one, cyclic indexing in [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} yields $$2q_0=q_0^2-a.$$ The two neighbor *slots* coincide but must both be retained. For period two the system is $$2q_1=q_0^2-a,
  \qquad
  2q_0=q_1^2-a.$$ At period $n\ge3$, the neighbors are written separately even if a special solution happens to make their values equal.

For arbitrary $n$, the homogenized $j$th equation has the form $$Q_j^2-Q_{j+1}Z-Q_{j-1}Z-aZ^2=0.$$ At $Z=0$ it becomes $Q_j^2=0$. Hence the entire projective zero scheme is disjoint from infinity. The argument uses the fact that a positive-dimensional projective subvariety cannot be contained in the affine chart $Z\ne0$. It does not require the affine equations to be reduced, and therefore proves finiteness even in the presence of multiplicity.

For Corollary [\[cor:s-integral\]](#cor:s-integral){reference-type="ref" reference="cor:s-integral"}, the orbit field is explicit in the quantifiers. Starting from $(K_0,S_0)$, one first chooses a finite extension $K$ containing every coordinate and then extends $S_0$ to all places of $K$ above it. The maximum argument is applied only at non-Archimedean $v\notin S$. This ordering avoids silently treating an algebraic coordinate as if it belonged to the base field. The sharp example [\[eq:sharp-third\]](#eq:sharp-third){reference-type="eqref" reference="eq:sharp-third"} shows that the denominator in $G$ cannot be discarded.

# Static audit and reproducibility record {#app:reproducibility}

The prospective lock is `experiments/source_lock.json`, SHA-256

d15f5084900aa043e80ada46d3ce22772cd10bbdb348d4fcb000aa9fa2ca49d7.

The official proof package hash is

c579e2da093a8ab588a5818bab0df59a47804792fcdfa338777f48e1bd1a1214.

The independent pre-run review record used for deployment authorization has SHA-256

629ed6bfe06f73ad387712c53f28aa73ee6c466098dd22ef502fd34f2d32ba58.

The official JUnit XML has SHA-256

c29e6bc5f805f32d9a9620dfad42bfe9474973f430c857531970e0f28782fa62,

and records 82 tests, zero failures, and zero errors. The final result manifest contains 35 paths and has SHA-256

6b3dbfed68dbd058056c35139756d5ccbb4e9f3b9a263ccaddef64bb183326e7.

From the project directory, the official frozen static audit was produced by

    PYTHONDONTWRITEBYTECODE=1 pytest -q --junitxml=results/pytest.xml
    PYTHONDONTWRITEBYTECODE=1 python code/scripts/run_static_audit.py \
      --project-root .
    python code/scripts/build_result_manifest.py --project-root .

Those commands are provenance only; they need not be rerun to build the paper. Publication figures are regenerated from the frozen JSON package by

    python paper/figures/generate_all.py

and the manuscript by

    paper/build.sh

Each figure has PDF and SVG vector masters plus a PNG review copy. The figure loader verifies the source-lock hash, all eight PASS stages, controls-first ordering, a closed candidate gate, and zero prime/zero access before writing an output. Fixed PDF/SVG metadata makes consecutive regenerations byte-for-byte reproducible.

No candidate parameter, periodic point, or candidate action appears in the paper package. The Hénon formulas use the generic algebraic parameter $a$, and the only substituted values are the predeclared sharp control $a=-1$, $(q,p)=(1,1)$ and small rational gauge controls. Static identities are implementation audits. The all-period conclusion comes from Theorems [\[thm:evaluation\]](#thm:evaluation){reference-type="ref" reference="thm:evaluation"} and [\[thm:henon\]](#thm:henon){reference-type="ref" reference="thm:henon"}.
