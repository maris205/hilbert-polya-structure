---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--39-affine-obstruction-dag-closure-certificate"
canonical_tex: "symbolic_dynamics/papers/39-affine-obstruction-dag-closure-certificate/main.tex"
canonical_pdf: "symbolic_dynamics/papers/39-affine-obstruction-dag-closure-certificate/main.pdf"
source_sha256: "ef1d37c986e816e556b40eff83bb1decf742236865a3d7debd622a24d08440fa"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Relative Exhaustion of an Affine Symbolic Branch: A Typed Obstruction DAG and Registry Handoff

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/39-affine-obstruction-dag-closure-certificate>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/39-affine-obstruction-dag-closure-certificate/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/39-affine-obstruction-dag-closure-certificate/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/39-affine-obstruction-dag-closure-certificate/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/39-affine-obstruction-dag-closure-certificate/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Repeated negative results do not close a research branch when their obstructions belong to different objects, clocks, operators, or determinant categories. We prove relative exhaustion for one finite affine symbolic branch by treating four hashed predecessor outcomes as typed data. Its Paper-39 encoding was assembled after those outcomes and frozen before its checker; the claim is neither prospective nor universal. The contract has 14 repair classes, 16 request tokens, and 17 internal tags. A 22-node/28-edge proof DAG retains object, marker, ownership, obstruction, and terminal types; a 6-node/5-edge spine gives a coarse executable view with explicit fibers. Every token has exactly one role: an in-domain path reaches an endpoint with a nonempty failed-coordinate set, or the request makes a typed category exit without obstruction credit. The class census is six obstructed, six exit-only, and two mixed; the token census is eight plus eight. One historical edge stays outside the quantified domain, while another resets all four candidate-state fields. The audit object owns no arithmetic source, primitive ledger, operator, determinant, or marker; all strict Route-A coordinates fail, Route B remains locked, and control returns to the pre-existing registry without ranking or authorizing a successor.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 16, 2026'
title: |
  Relative Exhaustion of an Affine Symbolic Branch:\
  A Typed Obstruction DAG and Registry Handoff
```

## Markdown 正文

# Introduction {#sec:introduction}

A sequence of failed constructions can look exhaustive while still mixing incompatible evidence. One construction may supply a selective source, another a nonempty primitive ledger, and a third a determinant, yet no single object owns the conjunction. The danger is especially acute when each repair changes the phase space, the primitive clock, or the operator category. A branch-closing argument must therefore answer two questions before it draws a negative conclusion: what is the exact request universe, and which typed object owns every failure?

This distinction mirrors a general lesson about no-go results. Their force is relative to stated goals, assumptions, frameworks, and mathematical structures; changing one of those ingredients is an escape pathway rather than another failure of the original statement [@Dardashti2021NoGo]. Paper 39 turns that lesson into a deliberately finite audit. It does not search for a fifth affine mechanism. Instead, it treats the content-addressed outcomes of Papers 35--38 as a typed history and asks whether every request admitted by one explicit encoding has already received an obstruction or a category-exit classification.

The timing matters. The four predecessor outcomes were known when the 14-class, 16-token encoding was assembled. The encoding was then frozen before the Paper-39 checker. Hashes therefore establish byte identity for the audit; they do not show that the universe was selected prospectively, independently of the outcomes, or completely with respect to every conceivable idea. Our claim is relative exhaustion of this retrospective encoding and nothing stronger.

The proof uses two graph granularities. The *structural spine* has six nodes and five edges and records the coarse sequence from the Paper-35 object firewall through the registry handoff. The *expanded proof DAG* has 22 nodes and 28 edges. It preserves the branches, source owners, category exits, and endpoint obstructions needed for a proof. A total many-to-one projection links the two graphs through explicit fibers. The spine is therefore an executable summary, not a substitute for the proof DAG.

At each in-domain endpoint we evaluate a retrospective six-coordinate consolidation of pre-existing Route and source fields, $$\ensuremath{\operatorname{Good}}(c)=\mathop{\mathrm{Intrinsic}}(c)\wedge\mathop{\mathrm{Rec}}(c)\wedge\mathop{\mathrm{Selective}}(c)
  \wedge\mathop{\mathrm{OwnedDet}}(c)\wedge\mathop{\mathrm{MarkerOK}}(c)\wedge\mathop{\mathrm{Controls}}(c).
  \label{eq:good-intro}$$ The six coordinates require an intrinsic source, primitive recurrence with repetitions, arithmetic selectivity, same-object determinant ownership, a compatible marker, and survival of the frozen controls. The underlying fields pre-date Paper 39; their conjunction is part of the retrospective encoding and is not claimed to have been selected independently of the predecessor outcomes.

Our main result says that every one of the 16 recorded requests is classified. Eight tokens reach endpoints with a nonempty set of failed coordinates in [\[eq:good-intro\]](#eq:good-intro){reference-type="ref" reference="eq:good-intro"}; eight are explicit exits with an empty failed-coordinate set. At the class level this becomes six obstructed classes, six exit-only classes, and two mixed classes whose canonical request is obstructed while one enumerated alternative leaves the category. The separation is essential: [Exit]{.smallcaps} is not evidence for $\neg\ensuremath{\operatorname{Good}}$.

The finite-graph aspect has close predecessors. In particular, the Equational Theories Project fixes a homogeneous finite universe of equational laws and uses formal proofs and countermodels to complete its implication graph [@BolanEtAl2025ETP]. Typed proof-dependency graphs and status-bearing blueprints are also established. Paper 39 claims neither the first finite mathematical graph nor the first typed DAG. Its narrower contribution is the content-addressed integration of heterogeneous historical repairs, explicit object/marker/operator exits, and a governance handoff for this affine program.

The contributions are fourfold.

1.  We freeze a finite theorem domain with exactly 14 repair classes, 16 request tokens, and 17 internal tags, and we expose both graph granularities with an exact $22/28\to6/5$ projection.

2.  We prove endpoint-obstruction totality over the encoded domain: every obstructed token has a specified endpoint with a nonempty failed-$\operatorname{Good}$ set, while every exit token has a typed boundary and no obstruction credit.

3.  We isolate two ownership hazards. Edge `E22` is a non-domain historical firewall with empty coverage fibers, and the transition `E07`/`E36_37` resets object, marker, operator owner, and determinant owner under the Paper-37 source lock.

4.  We derive the strict protocol consequence without inflating it into candidate success: all Route-A coordinates fail, Route B stays locked, and control returns to the historical registry without ranking or selecting an entry.

summarizes the exact relationship between the two graph granularities.

positions the audit against no-go methodology, proof certificates, and finite graph completion. defines the contract and typed graphs. proves relative exhaustion. isolates ownership transfer, and [\[sec:executable,sec:route\]](#sec:executable,sec:route){reference-type="ref" reference="sec:executable,sec:route"} state the executable trust boundary and Route consequence. Full token and proof ledgers appear in the appendices.

# Related work and terminology boundary {#sec:related}

Paper 39 combines established ideas but assigns them a narrow, project-specific role. The relevant comparisons are methodological: assumption-relative no-go reasoning, obstruction sets, trusted certificates, formal dependency graphs, and the symbolic/group-theoretic ingredients inherited from the four predecessors. The literature search supporting this section is frozen in the corrected audit snapshot; its negative result is moderate-confidence and vocabulary-dependent.

#### No-go reasoning and obstruction theory.

@Dardashti2021NoGo organizes no-go results by goals, frameworks, physical assumptions, mathematical structures, and background assumptions, and emphasizes that denying one component identifies an escape rather than closing every research route. Classical obstruction theory already provides stagewise extension barriers [@Olum1950Obstructions]; local coefficients are likewise established machinery [@KwasikSun2018Local]. Our typed EXIT status operationalizes the same caution in a finite audit: a changed object or determinant category is not silently relabeled as a theorem-level failure. We do not claim new obstruction theory or a general no-go taxonomy.

#### Finite obstruction sets and refinement.

Finite forbidden-obstruction characterizations are classical in graph-minor theory [@RobertsonSeymour2004GraphMinorsXX], while constructive work makes clear that existence, enumeration, and a stopping signal are separate burdens [@CattellEtAl2000ObstructionSets]. Counterexample-guided abstraction refinement uses failures to revise a model until a property is proved or a real counterexample remains [@ClarkeEtAl2000CEGAR]. These precedents motivate our insistence on an explicit universe and total classifier. They do not imply that a historically assembled research alphabet is prospectively complete.

#### Certificates and finite mathematical graph completion.

Proof-carrying code and foundational proof certificates separate certificate production from checking by a trusted consumer [@Necula1997PCC; @HeathMiller2015ProofCertificates]. The Equational Theories Project is the closest functional predecessor to the broad idea of a machine-checked finite mathematical graph [@BolanEtAl2025ETP]. It fixes 4,694 short equational laws, uses formal proofs and countermodels for generating relations, and reports the complete unrestricted implication graph. The project paper also records an important trust-boundary detail: transitive and duality expansion to the full graph is performed by external programs rather than as millions of separate end-to-end Lean theorems. ETP's universe is syntactically enumerable and homogeneous; ours is a retrospective, content-addressed map of heterogeneous repairs, ownership resets, and category exits. The comparison rules out any claim that Paper 39 is the first exhaustive finite mathematical graph.

#### Typed proof and dependency DAGs.

The mathlib ecosystem provides a mature formal-library baseline [@MathlibCommunity2020]. Recent systems organize informal and formal proof steps as dependency graphs, infer blueprint edges, track status, and use failed nodes for refinement [@CabralEtAl2025ProofFlow; @ZhuEtAl2026LeanArchitect; @ChungEtAl2026GoedelArchitect]. A recent network analysis of mathlib further separates explicit, compiler-synthesized, statement, proof, module, and namespace edges [@LiEtAl2026MathlibNetwork]. These works establish that typed DAGs and multilayer provenance are not novel by themselves. Paper 39 differs in what the nodes mean: they are outcomes of authorized candidate repairs, and completion means obstruction-or-exit coverage of a finite request contract, not completion of one proof blueprint.

#### "Closure certificate" is an occupied term.

@MuraliEtAl2024ClosureCertificates define closure certificates for dynamical verification as state-pair functions that overapproximate transition relations and establish temporal properties; the journal extension further develops that framework [@MuraliEtAl2026ClosureCertificates]. We therefore avoid the bare label. The phrases *typed affine-program closure audit* and *retrospective obstruction-coverage audit* distinguish our finite research-program artifact from their dynamical-systems certificate.

#### Presentation and symbolic machinery.

Presentation-changing Tietze moves are classical [@Tietze1908Invarianten], and universal decision claims over finite group presentations meet classical undecidability boundaries [@Rabin1958Recursive]. Bass's graph-of-groups covering theory encodes tree actions [@Bass1993Covering], while Krieger's work illustrates representation-invariant symbolic objects [@Krieger2000Invariant]. Accordingly, Paper 39 calls the Paper-38 tree canonical only for the frozen ascending-HNN splitting and presentation; it claims no presentation-invariant decision procedure.

The constituent dynamics are also prior art: non-backtracking graph-zeta operators [@Hashimoto1989Zeta], tree-lattice Ihara determinants [@Bass1992IharaSelberg], symbolic cocycles [@Schmidt1998FundamentalCocycles], group-symbolic obstruction principles [@Bartholdi2010Gardens], Cayley-graph symbolic classifications [@AubrunBitar2024SAW], marker-based subshift embeddings [@Meyerovitch2025Embedding], and recent geometric obstructions for group self-simulation [@BarbieriEtAl2025GeometricObstruction]. Paper 39 does not re-prove those theories. Its qualified novelty lies only in the exact content-addressed integration and executable relative-coverage architecture.

# Frozen contract and typed graph {#sec:contract}

The theorem domain is data, not an inferred universe. We first state the timing and trust assumptions, then define the token classifier and the two graphs that realize it.

[\[ass:timing\]]{#ass:timing label="ass:timing"} The final source, proof, derivation, clue, and Route artifacts of Papers 35--38 are fixed by the hashes in the Paper-39 source lock. Their outcomes were known when the Paper-39 encoding was assembled. The resulting contract and its checker inputs were frozen before the Paper-39 checker was run.

[\[ass:predecessors\]]{#ass:predecessors label="ass:predecessors"} The mathematical statements cited from Papers 35--38 hold under their own quantifiers and hypotheses. Paper 39 audits their typed use; it does not independently re-prove external results or turn finite execution into a proof of their infinite claims.

These assumptions separate three questions that hashes alone cannot collapse. Byte identity of the inputs is checkable. Truth of the inherited theorems is a mathematical dependency. Prospective completeness of every possible repair is neither assumed nor concluded.

## The success predicate

For a typed candidate state $c$, define $$\ensuremath{\operatorname{Good}}(c)=I(c)\wedge R(c)\wedge S(c)\wedge D(c)\wedge M(c)\wedge C(c).
\label{eq:good}$$ The coordinates are mnemonic abbreviations for the six named predicates in [\[tab:good\]](#tab:good){reference-type="ref" reference="tab:good"}. Each coordinate comes from a pre-existing Route or source field; the Paper-39 checker merely normalizes the names.

\@L1.9cmL4.1cmY@ Coordinate & Pre-existing field & Frozen meaning\
$I$: intrinsic & Route A0 arithmetic origin; allowed/forbidden data & No prime, support, target-zero, terminal-projector, or post-result oracle.\
$R$: recurrence & Route A1; object, dynamics, clock & Nonempty primitive family with compatible repetitions on the declared object.\
$S$: selectivity & Route A0/A1 arithmetic sector; generic controls & A source-proved sector that fails matched generic controls.\
$D$: owned determinant & Route A2; operator object; determinant convention & One declared operator on the same space owns the claimed determinant category.\
$M$: marker & clock; theorem marker; normalization & One free marker counts the frozen primitive step and is not a quotient clock, return time, or fugacity.\
$C$: controls & adversarial controls; proves-too-much risk; stop rule & Balanced, composite, mutation, generic, and proves-too-much controls survive.\

## Classes, tokens, and normalization

The top-level alphabet $\mathcal{A}_{14}$ has the following 14 labels: $$\begin{aligned}
\mathcal{A}_{14}=\{&\texttt{affine\_cayley\_representation},
            \texttt{finite\_rank\_local\_system},\\
          &\texttt{character},\texttt{grading},\texttt{quotient},
            \texttt{induced\_shift},\\
          &\texttt{first\_return\_map},\texttt{bass\_serre\_splitting},
            \texttt{valuation\_tree},\texttt{boundary\_model},\\
          &\texttt{modular\_phase},\texttt{basepoint\_damping},
            \texttt{finite\_total\_weight\_retrofit},\texttt{groupoid\_trace}\}.\end{aligned}$$

The request domain $\Sigma_{16}$ contains exactly 16 stable tokens. Six tokens name theorem-covered frozen families, six name explicit exits, and the two mixed classes each contribute one canonical tested token and one alternative exit token. There is no catch-all `OTHER_INSTANCE`, and no token denotes an arbitrary compound repair. The complete table appears in [\[tab:tokens\]](#tab:tokens){reference-type="ref" reference="tab:tokens"}.

The frozen normalizer is simply the finite record map $$\mathsf{norm}:\Sigma_{16}\longrightarrow
  \mathsf{ObsPath}\;\sqcup\;\mathsf{ExitPath}.
\label{eq:normalizer}$$ An obstruction record contains its class, instance scope, endpoint set, internal-edge witnesses, provenance paths, and terminal codes. An exit record contains the same scope information but an empty obstruction set and an explicit boundary/exit path. The codomain is a disjoint union, so an exit cannot be read as a failed-$\operatorname{Good}$ proof.

## Node and edge types

The invariant object is the history $$\mathcal H_{35:38}=(\mathcal V,\mathcal E,\ensuremath{\operatorname{type}},\ensuremath{\operatorname{owner}},
  \operatorname{obstruction},\ensuremath{\operatorname{status}}).
\label{eq:history}$$ Every node records an inherited obligation, source object, marker, operator owner, determinant owner, exact obstruction, forbidden escape, and terminal code. Every edge records its source and target, historical authority, one of the internal/closure/exit/firewall/guard roles, and field-transfer semantics.

An ownership label is part of the type. Consequently, an operator or determinant at one node does not travel across an object-changing edge unless a source-owned transport theorem says so. Historical successor edges may carry an audit obligation while resetting every candidate-state field. This rule prevents a coordinatewise assembly of four individually useful but mutually incompatible predecessor facts.

## Expanded DAG and structural spine

The expanded proof graph has the 22 nodes $$\begin{gathered}
\texttt{N00};\quad
\texttt{N35F,N35P,N35S,N35H,N35Q,N35D,N35B};\\
\texttt{N36F,N36G};\quad
\texttt{N37O,N37D,N37N};\quad
\texttt{N38T,N38M,N38L,N38O,N38K};\quad
\texttt{NX,NC,NR,NS}.\end{gathered}$$ Its 28 edges are partitioned exactly as $$28=17\;\text{internal}+5\;\text{closure}+3\;\text{token exits}
  +1\;\text{non-domain firewall}+2\;\text{guards}.
\label{eq:edge-partition}$$ The bridge assigns ranks $0,\ldots,11$ to the nodes, and every edge strictly increases rank. Hence the expanded graph is acyclic. The proof does not rely on a reflexive reachability formula disguised as termination; acyclicity only certifies the recorded graph structure.

The structural spine is

`N35_OBJECT_FIREWALL` $\to$ `N36_CELLULAR_CANCELLATION` $\to$ `N37_COEFFICIENT_SATURATION` $\to$ `N38_TREE_ORBITAL_TRILEMMA` $\to$ `N39_AFFINE_BRANCH_CLOSED` $\to$ `N_REGISTRY_HANDOFF`.

Its five edges retain the predecessor obligation flow and governance action. The bridge map $\pi$ sends every expanded node and edge to a spine fiber or a named auxiliary target. It is total and surjective onto the structural spine, but many-to-one. The bridge remains auditable because it stores the entire expanded record set and both fiber maps; "projection" never means that the coarse graph alone can reconstruct the proof.

## The candidate domain

Let $\mathcal{P}_{\mathrm{fr}}$ be the nonempty in-contract provenance paths through the 17 internal transitions. If $p$ ends at $v$, its candidate datum belongs only to the endpoint family $X_v(r)$. Define $$\mathfrak{C}_{\mathrm{aff}}(r)=\coprod_{p\in\mathcal{P}_{\mathrm{fr}}}\{p\}\times X_{\ensuremath{\operatorname{end}}(p)}(r).
\label{eq:candidate-domain}$$ The coproduct tag prevents histories with distinct endpoints from being identified. More importantly, a path is provenance, not cumulative repair composition. For example, the path from the Paper-36 filling node to the Paper-37 coefficient node records why the latter was tested; it does not apply finite coefficients to the filled object.

The auxiliary sink `NX` is outside [\[eq:candidate-domain\]](#eq:candidate-domain){reference-type="ref" reference="eq:candidate-domain"}. It receives explicit exit tokens and the separate historical firewall `E22`. Closure over $\mathfrak{C}_{\mathrm{aff}}(r)$ and total classification over $\Sigma_{16}$ are related finite statements, but neither quantifies over arbitrary mechanisms outside these sets.

# Relative affine-branch closure {#sec:theorem}

For $r\ge2$, write $$M_r=\langle u,v\mid vu=u^rv\rangle^+,
\qquad
G_r=\langle u,v\mid vuv^{-1}=u^r\rangle.$$ The predecessor objects associated with these presentations are not identified with each other. The symbols only index the source-owned families whose outcomes are recorded at the expanded endpoints.

## Endpoint-obstruction totality

Let $V_{\mathrm{test}}$ be the 17 tested endpoints in the expanded graph. The bridge stores the following total map to failed coordinates: $$\begin{aligned}
\ensuremath{\operatorname{Fail}}(\texttt{N35F})=\ensuremath{\operatorname{Fail}}(\texttt{N35P})&=\{R,D\},\\
\ensuremath{\operatorname{Fail}}(\texttt{N35S})=\ensuremath{\operatorname{Fail}}(\texttt{N35H})&=\{S,D,C\},\\
\ensuremath{\operatorname{Fail}}(\texttt{N35Q})&=\{S,D,M\},\\
\ensuremath{\operatorname{Fail}}(\texttt{N35D})&=\{R,S,M\},\\
\ensuremath{\operatorname{Fail}}(\texttt{N35B})&=\{I,S,M\},\\
\ensuremath{\operatorname{Fail}}(\texttt{N36F})&=\{R,S,D,M,C\},\\
\ensuremath{\operatorname{Fail}}(\texttt{N36G})&=\{R,S,C\},\\
\ensuremath{\operatorname{Fail}}(\texttt{N37O})=\ensuremath{\operatorname{Fail}}(\texttt{N37D})&=\{S,C\},\\
\ensuremath{\operatorname{Fail}}(\texttt{N37N})&=\{R,S,C\},\\
\ensuremath{\operatorname{Fail}}(\texttt{N38T})=\ensuremath{\operatorname{Fail}}(\texttt{N38M})&=\{R,D\},\\
\ensuremath{\operatorname{Fail}}(\texttt{N38L})&=\{D,C\},\\
\ensuremath{\operatorname{Fail}}(\texttt{N38O})&=\{S,D,M,C\},\\
\ensuremath{\operatorname{Fail}}(\texttt{N38K})&=\{M\}.\end{aligned}$$ Every value is nonempty. The map is not defined by graph reachability alone; each set is inherited from the source-owned theorem at that endpoint. The sink `NX` instead has an empty failed-coordinate set because it represents nonmembership, not an unsuccessful candidate.

[\[lem:endpoint-totality\]]{#lem:endpoint-totality label="lem:endpoint-totality"} For every $p\in\mathcal{P}_{\mathrm{fr}}$, the endpoint $\ensuremath{\operatorname{end}}(p)$ lies in $V_{\mathrm{test}}$. For every $c\in X_{\ensuremath{\operatorname{end}}(p)}(r)$, at least one coordinate in $\ensuremath{\operatorname{Fail}}(\ensuremath{\operatorname{end}}(p))$ is false for $c$.

The finite path table lists one nonempty provenance path for each tested endpoint and no in-contract path to `NX`, `NC`, `NR`, or `NS`. Direct inspection of the edge endpoints shows that the terminal node of every listed in-contract path is one of the 17 nodes above. The inherited theorem named by the endpoint record proves the stated coordinate failure under that endpoint's own object and quantifiers. The nonempty sets displayed above exhaust $V_{\mathrm{test}}$, which proves both assertions.

The word "totality" in [\[lem:endpoint-totality\]](#lem:endpoint-totality){reference-type="ref" reference="lem:endpoint-totality"} is deliberately local. It refers to the finite endpoint table. It is not a claim that all conceivable repair processes terminate, nor does it use reflexive reachability to manufacture a terminal witness.

## The token classifier

The normalizer in [\[eq:normalizer\]](#eq:normalizer){reference-type="ref" reference="eq:normalizer"} assigns eight tokens to obstruction paths and eight to exit paths. The obstruction tokens are the six frozen families plus the canonical Bass--Serre and groupoid-import tokens. The exit tokens are the six exit-only requests plus the two explicit alternatives from the mixed classes. Every token record names its exact instance scope; the normalizer cannot be extended by imagining an unrecorded instance.

[\[prop:token-totality\]]{#prop:token-totality label="prop:token-totality"} For every $q\in\Sigma_{16}$, exactly one of the following holds.

1.  $\mathsf{norm}(q)$ is an obstruction record with at least one endpoint $v\in V_{\mathrm{test}}$ and $\ensuremath{\operatorname{Fail}}(v)\ne\varnothing$.

2.  $\mathsf{norm}(q)$ is an exit record whose terminal endpoint is `NX`, whose obstruction-endpoint list is empty, and whose failed-$\operatorname{Good}$ set is empty.

The 16 token IDs in [\[tab:tokens\]](#tab:tokens){reference-type="ref" reference="tab:tokens"} are distinct and equal the declared domain of the finite normalizer. Eight records have disposition [Obstructed]{.smallcaps} and nonempty obstruction-endpoint/path lists; their endpoints belong to $V_{\mathrm{test}}$, so [\[lem:endpoint-totality\]](#lem:endpoint-totality){reference-type="ref" reference="lem:endpoint-totality"} applies. The remaining eight records have disposition [Exit]{.smallcaps}, empty obstruction lists, and an explicit exit edge ending at `NX`. No record has both dispositions, and the two counts sum to 16.

visualizes this finite, disjoint classifier.

At class level, the census is six obstructed, six exit-only, and two mixed (Bass--Serre splitting and groupoid trace). An exit-only row says only that its one request token changes the frozen category; a mixed row quantifies only over its two recorded tokens, not all conceivable alternatives.

## Relative closure theorem

[\[thm:closure\]]{#thm:closure label="thm:closure"} Under [\[ass:timing,ass:predecessors\]](#ass:timing,ass:predecessors){reference-type="ref" reference="ass:timing,ass:predecessors"}, for every $r\ge2$ and every $c\in\mathfrak{C}_{\mathrm{aff}}(r)$, $$\neg\ensuremath{\operatorname{Good}}(c).$$ Moreover, every request $q\in\Sigma_{16}$ is classified by [\[prop:token-totality\]](#prop:token-totality){reference-type="ref" reference="prop:token-totality"}; no request in the finite domain remains unassigned.

Take $c\in\mathfrak{C}_{\mathrm{aff}}(r)$. By [\[eq:candidate-domain\]](#eq:candidate-domain){reference-type="ref" reference="eq:candidate-domain"}, $c=(p,x)$ for a nonempty provenance path $p\in\mathcal{P}_{\mathrm{fr}}$ and an endpoint datum $x\in X_{\ensuremath{\operatorname{end}}(p)}(r)$. By [\[lem:endpoint-totality\]](#lem:endpoint-totality){reference-type="ref" reference="lem:endpoint-totality"}, the endpoint lies in $V_{\mathrm{test}}$ and at least one coordinate listed by $\ensuremath{\operatorname{Fail}}(\ensuremath{\operatorname{end}}(p))$ is false for $x$. Since $\operatorname{Good}$ is the conjunction of all six coordinates, $\ensuremath{\operatorname{Good}}(c)$ is false. The final request-classification statement is [\[prop:token-totality\]](#prop:token-totality){reference-type="ref" reference="prop:token-totality"}.

The theorem has two related conclusions but no hidden equivalence. The first quantifies over endpoint-typed candidate data on the in-contract provenance paths. The second classifies all 16 request tokens, including category exits that do not lie in $\mathfrak{C}_{\mathrm{aff}}(r)$. Exit classification completes the request table; it does not prove $\neg\ensuremath{\operatorname{Good}}$ for a changed object.

## Inherited kernels and sharp boundaries

The endpoint map packages four source-owned kernels: Paper 35 supplies the object fork; Paper 36 the filling, quotient-ownership, and clock fork; Paper 37 the finite-coefficient leakage-or-erasure fork; and Paper 38 the tree/orbital trilemma for the tree canonical to the frozen ascending-HNN splitting and presentation. Paper 39 contributes their typed coverage proof, not new versions of these kernels. Their hypotheses and dependency structure remain in the frozen packages and [8](#app:ledgers){reference-type="ref" reference="app:ledgers"}.

The quantifier $r\ge2$ is intentional. At $r=1$ some affine obstructions disappear while filling, nonproper-action, and orbital controls remain, so the balanced case is only a control. The explicit countermodels in [8](#app:ledgers){reference-type="ref" reference="app:ledgers"}---finite cycles, noninvertible deletion, summable tree damping, proper tree lattices, and first-trace cancellation---show sharply why [\[thm:closure\]](#thm:closure){reference-type="ref" reference="thm:closure"} cannot become a universal impossibility theorem.

# Ownership transfer and zero-credit firewalls {#sec:ownership}

Two records carry most of the burden of preventing an overstatement. The first stops historical succession from becoming candidate-identity transport. The second keeps an unquantified future-search prohibition from becoming coverage evidence.

## E07 and E36\_37 reset candidate identity

Expanded edge `E07` connects the Paper-36 endpoint to the independently source-locked Paper-37 coefficient object. Its coarse image is `E36_37`. The four candidate-state fields obey $$\begin{array}{c|cccc}
\text{field} & \text{object} & \text{marker} & \text{operator owner}
  & \text{determinant owner}\\
\hline
\text{mode} & \mathrm{RESET} & \mathrm{RESET} & \mathrm{RESET}
  & \mathrm{RESET}
\end{array}
\label{eq:four-resets}$$ with authority `P37_SOURCE_LOCK_SD_C39`. The target object is the separately locked unquotiented matrix-affine Hashimoto system. Its original Hashimoto-transition marker is redeclared, and its parity operators and ordinary Fredholm factors prove their ownership anew.

This edge is therefore not an operation that first removes the Paper-36 fill and then adds coefficients. Such a reading would turn a historical comparison into a compound repair and identify objects for which no transport theorem exists. The coarse projection cannot weaken an expanded reset to `CARRY_WITH_EQUIVALENCE`.

What does persist is audit context. The inherited obligation records why the Paper-37 object was tested. Historical provenance is jointly bound by the edge endpoints, E07 authority, embedded Paper-36/Paper-37 hashes, and packet locks. Neither item is a fifth candidate-state field, and neither transports candidate identity.

## E22 preserves history but earns no theorem credit

Expanded edge `E22 : N37N -> NX` records the Paper-37 post-result warning against trying an unspecified new matrix, character, fiber rank, representation, automaton, or completion. Earlier versions of the audit risked reading this prose as an alternative instance for the finite-rank, character, or grading classes. That reading would make those classes mixed and would contradict the finite token census.

The corrected type is $$\texttt{AUXILIARY\_NON\_DOMAIN\_FIREWALL}.$$ Its request-token fiber and repair-class fiber are empty. Its historical path is retained and content-addressed, but the edge is excluded from $\mathcal{A}_{14}$, $\Sigma_{16}$, the in-contract provenance domain, and the failed-$\operatorname{Good}$ map. The sink `NX` is shared with explicit exits, yet endpoint identity does not erase edge role: E22 has zero closure credit.

places the reset and zero-credit guards side by side.

[\[prop:no-assembly\]]{#prop:no-assembly label="prop:no-assembly"} No candidate in $\mathfrak{C}_{\mathrm{aff}}(r)$ may satisfy $\operatorname{Good}$ by selecting coordinates from distinct expanded endpoints or by treating a RESET edge as an equivalence.

The coproduct in [\[eq:candidate-domain\]](#eq:candidate-domain){reference-type="ref" reference="eq:candidate-domain"} types the candidate datum at one endpoint. The edge schema gives each of the four identity fields a unique source/target transfer mode. Across E07 all four modes are RESET, while no frozen transport theorem supplies an equality or equivalence. Thus a coordinate owned at the source is unavailable at the target unless re-proved there. Selecting coordinates from different coproduct summands does not produce an element of $\mathfrak{C}_{\mathrm{aff}}(r)$.

The same discipline applies to determinant categories throughout the graph. An ordinary Fredholm determinant, a graded ratio, a finite quotient determinant, a tree-lattice trace, and a groupoid determinant may all be meaningful in their own settings. They are not interchangeable certificates for one operator. Typed exits preserve this distinction without making a universal judgment about the neighboring theory.

# Executable audit and validity checks {#sec:executable}

The mathematical theorem and the executable audit have different jobs. The proof packages own the inherited infinite statements and the finite coverage argument. The implementation reconstructs the finite contract, verifies its typing and counts, and tests that common corruptions are rejected. Passing a finite checker does not prove the predecessor theorems; failing it does show that the advertised Paper-39 encoding was not faithfully materialized.

## Source, evaluator, and bridge boundary

The executable design has three inputs. A source packet materializes the structural-spine records, repair rows, source hashes, registry snapshot, and timing declaration. The immutable bridge supplies the 22 expanded nodes, 28 typed edges, 16 request records, projection fibers, endpoint classifier, and special E22/E36\_37 guards. Evaluators parse those artifacts independently; the source does not import the evaluator and the evaluator does not trust narrative prose.

The trusted finite checks fall into five groups:

1.  **Domain checks:** exact node, edge, tag, class, and token ID sets; no duplicates and no catch-all request.

2.  **Graph checks:** typed source/target records, exact edge partition, strict rank increase, path continuity, and total projection fibers.

3.  **Semantic checks:** nonempty failed-coordinate sets at all 17 obstruction endpoints, empty sets at EXIT endpoints, and exact class/token censuses.

4.  **Firewall checks:** empty E22 class/token fibers and zero credit; four RESET modes and Paper-37 authority for E36\_37, with no equivalence binding.

5.  **Governance checks:** all-FAIL Route tuple, locked Route B, nonranking registry return, and conditional-only empty-registry fallback.

## Adversarial validity

A positive baseline is insufficient for a closure audit. The test suite must also reject malformed alternatives that would make the conclusion easier to obtain. The frozen mutation families include missing graph records, duplicated or misclassified tokens, an EXIT granted obstruction credit, an E22 coverage fiber, removal of E22's firewall type, and a false prospective-preregistration claim. Four separate mutations change each E36\_37 identity field from RESET to carry/equivalence. Registry mutations insert or rank a successor, misstate the historical witness set, or activate the empty-registry fallback.

These tests are adversarial in the narrow software sense: they show that the checker responds to changes that would violate the theorem contract. They do not constitute an empirical search for mathematical counterexamples.

## Authority FINAL synchronization

After the first writer compile, the independent integrator declared one authority result block FINAL / CLEAN and then issued a corrective integrity seal. records its principal executable checks and exact hashes; the complete SHA ledger is in [\[tab:authority-ledger\]](#tab:authority-ledger){reference-type="ref" reference="tab:authority-ledger"}. The main evaluator passed $535/535$ assertions, the independent evaluator passed $278/278$, and each rejected all $29$ adversarial mutations. The Route evaluator passed $14/14$. These are finite implementation results, not empirical support for an unencoded mathematical claim.

\@L2.8cmL1.8cmY@ Artifact & Result & SHA-256\
Main evaluator & $535/535$ & `041461feaf8d34c9974606b9856be5ba5fc6c26f62c88ba38b041998bfd82394`\
Independent evaluator & $278/278$ & `21bb9b3f623215875bdf93670165da41ff5c42f7e5ccb25cc19a432f7c048398`\
Science projection & canonical & `77a45be483807b81ba61fe0f16b16be20fcd7e6e4ff1f3f74f34d052c6881d93`\
Adversarial mutations & $29/29$ each & `f5fee0209155d06c8e16aedbf44ed2003f29115ad76b7f06bafe8be8a6d26f56`\
Route evaluation & $14/14$ & `f0d7f98e06e50b1605642fda3abc47b253103c79119886fa5a5b1b0e5c6b2902`\
Integrity audit & $224/224$ & `3c8aed949d8300e327bc265cd23b982b47397981ac379fef99a6d302360d7ac6`\

Fresh A/B, cold C, hidden audit, dummy sealed B, and two full runner passes were byte-stable; all $11/11$ mixed-state controls failed. The live State A is pending/manifest-absent; legal B uses an identical lowercase nonzero 40-hex triple plus an exact self-excluding manifest and yields the same audit bytes. The $65/65$ SHA ledger contains 36 result and 67 text records, binding 39 outputs under aggregate hash `ac09cd2c3be39e4d6d6ce754b5648d8a2abf7fd7fb9848db984558ff33dc82b3`.

The trust-layer ledger in [\[tab:trust\]](#tab:trust){reference-type="ref" reference="tab:trust"} states separately what these checks establish and what remains a mathematical or governance dependency.

# Route consequence, limitations, and conclusion {#sec:route}

## The audit is not a Route-A candidate

Paper 39 owns a typed history, not a phase space or operator. It cannot inherit the structural arithmetic source of a predecessor and has no primitive orbit ledger of its own. It also owns no determinant, analytic continuation, functional equation, self-adjoint carrier, or target-zero correspondence. Its strict tuple is therefore $$(\texttt{A0\_FAIL},\texttt{A1\_FAIL},\texttt{A2\_FAIL},
  \texttt{A3\_FAIL},\texttt{A4\_FAIL}).
\label{eq:route-tuple}$$ The overall decision is `ROUTE_A_REJECTED`; Route B remains locked. Relative closure is a successful audit result, not a successful candidate coordinate.

## Registry handoff

The historical registry predicate has six source-locked witnesses, `SD-C01` through `SD-C06`. These entries were already evaluated. Their role in Paper 39 is only to establish that the historically existing registry is nonempty. Consequently, the realized terminal is

`RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY`.

No ordering, score, proposal, or reclassification is attached to the handoff. It does not assert that one of the six entries is an unevaluated live candidate.

The mutually exclusive empty-registry guard carries the conditional code

`STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR`.

That guard is inactive in the frozen snapshot. The predecessor text does not define the phrase "unspent successor," so Paper 39 does not manufacture such a predicate.

## Limitations

The closure theorem should be read with six limitations.

1.  **Retrospective universe.** The encoding was assembled after the predecessor outcomes; checker freeze proves reproducibility, not outcome-independent selection.

2.  **Finite request scope.** The 16 tokens exclude arbitrary instances, unlisted compounds, and other readings of the 14 class labels.

3.  **Inherited mathematics.** Source-owned predecessor theorems keep their own hypotheses, which Paper 39 does not re-prove.

4.  **Category exits.** Changed objects may be productive; EXIT says only that they are not the frozen candidate.

5.  **Snapshot governance.** Historical registry nonemptiness and its handoff authorize nothing.

6.  **Qualified novelty.** The bounded search found no exact combination, while every generic ingredient has prior art.

## Conclusion

Four heterogeneous negative studies support a branch decision only after their objects, markers, owners, and exits are typed separately. The retrospective 14-class/16-token encoding, 22-node/28-edge proof graph, six-node spine, and endpoint classifier close that encoded branch without treating EXIT as failure. Nothing larger follows: Paper 40 requires a newly source-locked non-affine object, which neither the DAG nor the registry handoff selects.

# Expanded ledgers and proof details {#app:ledgers}

This appendix prints the finite records used in the main proof. The canonical machine-readable form remains `DAG_BRIDGE.json`; the tables below are a human-readable rendering. give the edge, request, and terminal records used by the proof.

## Ranks and expanded edges

The topological rank is

\@L1.2cmY@ Rank & Nodes\
& `N00`\
1 & `N35F,N35P`\
2 & `N35S`\
3 & `N35H`\
4 & `N35Q,N35D,N35B,N36F`\
5 & `N36G,N37O`\
6 & `N37D`\
7 & `N37N`\
8 & `N38T`\
9 & `N38M,N38L,N38O,N38K`\
10 & `NX,NC`\
11 & `NR,NS`\

\@L1.2cmL1.4cmL1.4cmL6.2cm@

\
Edge & From & To & Role\
Edge & From & To & Role\
`E00a` & N00 & N35F & internal transition\
`E00b` & N00 & N35P & internal transition\
`E01` & N35P & N35S & internal transition\
`E02` & N35S & N35H & internal transition\
`E03` & N35H & N35Q & internal transition\
`E04a` & N35H & N35D & internal transition\
`E04b` & N35H & N35B & internal transition\
`E05` & N35H & N36F & internal transition\
`E06` & N36F & N36G & internal transition\
`E07` & N36F & N37O & internal transition; four-field reset\
`E08` & N37O & N37D & internal transition\
`E09` & N37D & N37N & internal transition\
`E10` & N37N & N38T & internal transition; object reset\
`E11` & N38T & N38M & internal transition\
`E12` & N38T & N38L & internal transition; category-import comparison\
`E13` & N38T & N38O & internal transition; object reset\
`E14` & N38T & N38K & internal transition; marker comparison\
`E15` & N38T & NC & closure\
`E16` & N38M & NC & closure\
`E17` & N38L & NC & closure\
`E18` & N38O & NC & closure\
`E19` & N38K & NC & closure\
`E20` & N35H & NX & token-associated contract exit\
`E21` & N36F & NX & token-associated contract exit\
`E22` & N37N & NX & auxiliary non-domain firewall; zero coverage\
`E23` & N38T & NX & token-associated contract exit\
`E24` & NC & NR & realized governance guard\
`E25` & NC & NS & conditional governance guard\

The rank at the target exceeds the rank at the source in each row, so the expanded graph is a DAG. The five closure edges are separate because each Paper-38 endpoint owns a different obstruction. The three exit edges collect explicit tokens by boundary location; E22 is excluded from that partition even though it shares the sink `NX`.

## The sixteen request tokens

\@L5.8cmL2.6cmL2.2cmL2.7cm@

\
Token & Repair class & Disposition & Endpoint(s)\
Token & Repair class & Disposition & Endpoint(s)\
`AFFINE_CAYLEY_FROZEN_FAMILY` & affine Cayley representation & [Obstructed]{.smallcaps}& N35F, N35P, N35S, N35H, N36F\
`FINITE_RANK_LOCAL_SYSTEM_FROZEN_FAMILY` & finite-rank local system & [Obstructed]{.smallcaps}& N37O, N37D, N37N\
`CHARACTER_FROZEN_FAMILY` & character & [Obstructed]{.smallcaps}& N37O, N36G\
`GRADING_FROZEN_FAMILY` & grading & [Obstructed]{.smallcaps}& N36G, N37D, N37N\
`QUOTIENT_FROZEN_FAMILY` & quotient & [Obstructed]{.smallcaps}& N35Q, N36F\
`MODULAR_PHASE_FROZEN_FAMILY` & modular phase & [Obstructed]{.smallcaps}& N38M, N38O\
`INDUCED_SHIFT_EXIT` & induced shift & [Exit]{.smallcaps}& NX via E21\
`FIRST_RETURN_MAP_EXIT` & first-return map & [Exit]{.smallcaps}& NX via E21\
`VALUATION_TREE_EXIT` & valuation tree & [Exit]{.smallcaps}& NX via E23\
`BOUNDARY_MODEL_EXIT` & boundary model & [Exit]{.smallcaps}& NX via E20\
`BASEPOINT_DAMPING_EXIT` & basepoint damping & [Exit]{.smallcaps}& NX via E23\
`FINITE_TOTAL_WEIGHT_RETROFIT_EXIT` & finite-total-weight retrofit & [Exit]{.smallcaps}& NX via E23\

  -------------------------
  `FROZEN_ASCENDING_HNN_`
  `BASS_SERRE_SPLITTING`
  -------------------------

& Bass--Serre splitting & [Obstructed]{.smallcaps}& N38T\
`ALTERNATIVE_BASS_SERRE_SPLITTING_EXIT` & Bass--Serre splitting & [Exit]{.smallcaps}& NX via E23\
`FROZEN_TREE_LATTICE_GROUPOID_IMPORT` & groupoid trace & [Obstructed]{.smallcaps}& N38L\
`ALTERNATIVE_GROUPOID_CATEGORY_EXIT` & groupoid trace & [Exit]{.smallcaps}& NX via E23\

The table is the complete syntax of the request quantifier. English prose in the predecessor prohibitions does not create additional tokens. In particular, there is no arbitrary rank, character, completion, splitting, or groupoid instance.

## Endpoint terminal ledger

\@L1.6cmL2.3cmL3.0cmL7.0cm@

\
Node & Class & Failed coordinates & Terminal meaning\
Node & Class & Failed coordinates & Terminal meaning\
N35F & obstructed & $R,D$ & full positive affine recurrence stop\
N35P & obstructed & $R,D$ & bounded positive recurrence stop\
N35S & obstructed & $S,D,C$ & universal backtrack pollution\
N35H & obstructed & $S,D,C$ & relation-cycle pollution\
N35Q & obstructed & $S,D,M$ & quotient ledger/marker non-descent\
N35D & obstructed & $R,S,M$ & partition-trace identification\
N35B & obstructed & $I,S,M$ & Fock/support substitution\
N36F & obstructed & $R,S,D,M,C$ & complete fill erases recurrence\
N36G & obstructed & $R,S,C$ & generic scalar erasure\
N37O & obstructed & $S,C$ & invertible factor non-deletion\
N37D & obstructed & $S,C$ & mixed normal-closure leakage\
N37N & obstructed & $R,S,C$ & local-coefficient saturation\
N38T & obstructed & $R,D$ & full-tree empty/non-Fredholm\
N38M & obstructed & $R,D$ & modular noncompactness\
N38L & obstructed & $D,C$ & tree-lattice hypotheses\
N38O & obstructed & $S,D,M,C$ & orbital genericity/divergence\
N38K & obstructed & $M$ & marker nontransport\
NX & exit & $\varnothing$ & outside frozen affine contract\
NC & closure meta & $\varnothing$ & encoded affine branch closed\
NR & governance & $\varnothing$ & return to historical registry\
NS & conditional guard & $\varnothing$ & empty-registry fallback\

The audit root `N00` has no terminal status and is omitted. The empty sets in the last four rows have different semantics: nonmembership, closure metadata, realized governance, and a conditional guard. None is an obstruction endpoint.

## Proof dependency structure

The proof of [\[thm:closure\]](#thm:closure){reference-type="ref" reference="thm:closure"} depends on four finite facts and four inherited kernels:

1.  the 16 token IDs are an exact, duplicate-free domain;

2.  every obstruction record has a continuous provenance path ending in the displayed tested endpoint set;

3.  every EXIT record has empty obstruction fields and an explicit boundary path;

4.  the endpoint failed-coordinate map is total and nonempty on the 17 tested endpoints;

5.  Paper 35 supplies the object-fork obstructions;

6.  Paper 36 supplies filling, quotient-ownership, and marker non-descent;

7.  Paper 37 supplies the finite-coefficient leakage-or-erasure fork; and

8.  Paper 38 supplies the frozen-splitting tree/orbital trilemma.

The first four are proved by the Paper-39 finite ledgers. The last four are owned by the hashed predecessor mathematical packages. This separation is why the executable audit can verify coverage without pretending to prove the infinite kernels.

## Sharp scope countermodels

For completeness, the principal countermodels are explicit.

#### Finite recurrence.

For the directed $m$-cycle with adjacency matrix $A$, $\det(I-zA)=1-z^m$. Thus a symbolic system can possess a primitive orbit and an ordinary finite determinant outside the predecessor affine objects.

#### Noninvertible deletion.

The nilpotent matrix $N=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)$ satisfies $\det(I-tN)=1$. Factor deletion is possible after leaving the frozen invertible-transport family.

#### Weighted trees.

A sufficiently summable root-dependent damping can make an infinite-tree operator trace class. The resulting operator is not the canonical undamped or modularly weighted Paper-38 object.

#### Proper tree lattices.

Discrete, proper actions with finite stabilizers can support tree-lattice determinant theories. The frozen $\operatorname{BS}(1,r)$ action fails the required hypotheses. The local failure cannot be universalized to every tree action.

#### First-trace cancellation.

The invertible traceless matrix $J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$ has $\det(I-tJ)=1+t^2$. Vanishing first trace is insufficient for deletion of all primitive factors.

# ARS Phase-1 methodology and scope ledger {#app:methodology}

Paper 39 instantiates a compact theorem-relative methodology for negative research branches. The steps below describe the audit architecture, not a general guarantee that every research program can be finitely closed.

## Methodology blueprint

#### 1. Choose a theorem-relative paradigm.

State the object family, success predicate, repair domain, and allowed terminal claims before evaluating the checker. A negative conclusion must retain these quantifiers in its title, abstract, theorem, and stop rule.

#### 2. Freeze the contract as data.

Represent the authorized request universe by stable IDs and content hashes. Disclose the temporal boundary: here, predecessor outcomes were known before the contract was assembled, and only the Paper-39 checker inputs were frozen before the checker run.

#### 3. Construct a typed graph.

Every node records the inherited obligation, source object, marker, operator owner, determinant owner, obstruction, forbidden escape, and terminal code. Every edge records endpoints, authority, role, and carry/reset modes. A coarse view may summarize the graph only if all expanded fibers remain auditable.

#### 4. Prove edge and token coverage.

Define a finite normalizer on the exact token IDs. Obstruction records must end at a source-owned failed-coordinate witness. Exit records must carry a boundary witness and no obstruction credit. A catch-all "other" token is not an exhaustiveness proof.

#### 5. Test adversarial validity.

Construct countermodels to every tempting universalization and software mutations to every finite invariant. The checker should reject missing graph records, malformed types, false coverage, illegal ownership carry, and governance expansion.

#### 6. Freeze the stop rule.

Closure of the encoded branch authorizes no repair within that branch. It also does not authorize an unencoded successor. Control returns to a separately governed registry.

#### 7. State the limitation explicitly.

Finite relative closure is not universal impossibility. Content hashes authenticate bytes, not mathematical truth or prospective completeness.

## Immutable research snapshots

The writer copied the following nine authority-local snapshots without byte changes. Mutable narrative, plan, clue, figure, TeX, PDF, and compilation files are intentionally excluded from this research lock.

\@L5.0cmL9.3cm@

\
File & SHA-256\
File & SHA-256\
`SOURCE_LOCK.md` & `70456aff0b3afff0fe78336da3af7f2fc47724eb59674bf50bb7de4f1857770b`\
`MATH_PACKAGE.md` & `9af9b4cc68edf87871b9f3d94b04a1df9a92befa59bb2561394f1b6c990c37e9`\
`PROOF_PACKAGE.md` & `cc58540cb7a2396b7578f3aa7a76de3fcd7554a9faa5f26a4f98d6334b6da621`\
`DERIVATION_PACKAGE.md` & `ba3d6686928ebc67a24080a48d759cf6395547216b37aa7eeaffddc1bdfc58ed`\
`QUANTIFIER_AUDIT.md` & `29653cc74b95b3e4e32382f138c1ac00598a5c92bfbbd3c31d8cf8a9ad244073`\
`DAG_BRIDGE.json` & `4fa3bb28e6a2371dfb134f4a45ff03c1953ea68764f1decb70c64a9d5423d240`\
`ROUTE_A_EVALUATION.yaml` & `7bdb90811575a96518c2f67510ef9deb4335e2051c965643f7e3572e806ff6cd`\
`LITERATURE_AUDIT.md` & `aaca0a1834cc9793873698a07cbf4ddedb73a409eb9bd4dbc72ec4dd857fc781`\
`DA_REPORT.md` & `ef9aacc4584125853c572802a81e7243a60472ad5c5df17af57dd92d2e1599a3`\

The Route snapshot is a mathematical working record, not the integrator-owned machine Route output. The literature and devil's-advocate files are immutable audit snapshots.

## Authority FINAL executable seal

The independent integrator declared the following unique result bytes FINAL / CLEAN. This table is an implementation ledger, not an extension of the mathematical quantifiers.

\@L3.2cmL2.3cmL8.5cm@

\
Artifact & Result & SHA-256\
Artifact & Result & SHA-256\
Science projection & canonical & `77a45be483807b81ba61fe0f16b16be20fcd7e6e4ff1f3f74f34d052c6881d93`\
Main evaluator & $535/535$ & `041461feaf8d34c9974606b9856be5ba5fc6c26f62c88ba38b041998bfd82394`\
Independent evaluator & $278/278$ & `21bb9b3f623215875bdf93670165da41ff5c42f7e5ccb25cc19a432f7c048398`\
Adversarial mutations & $29/29$ each & `f5fee0209155d06c8e16aedbf44ed2003f29115ad76b7f06bafe8be8a6d26f56`\
Analysis summary & FINAL & `acf6dfefcead90b84eb0f28f43c60bf94ad0512389a7ce50d458d6b08e87560a`\
Integrity audit & $224/224$ & `3c8aed949d8300e327bc265cd23b982b47397981ac379fef99a6d302360d7ac6`\
Ledger audit & $65/65$ & `be32c6dcf43050307668d583425c67226e2edbb6231120977448e8b4e778e067`\
Exact result set & 36 & `69dcf722a5187dfb576a2a607b72f019cd471273c5090277db8e994e09a382dd`\
Exact text set & 67 & `e92eddfec5be91fb74a617ed08c7f532e856cbc08c51d14887eafd9ee39358c5`\
Sealed-state controls & $11/11$ rejected & `f12f9890d761e5cffe62f70a743cbc0a4749fe90237aa391033321581197181a`\
Fixed Route YAML & strict tuple & `9cda64c6ddf6bfbb865cb576b1a7475e2ce477c3627102e31862ec4c647ebc4e`\
Route evaluation JSON & $14/14$ & `f0d7f98e06e50b1605642fda3abc47b253103c79119886fa5a5b1b0e5c6b2902`\
Experiment report & FINAL & `86f2184b00e25085c18abeab99ef58815290100c42cb267ea33d16f6439d4dcd`\
Managed aggregate & 39 outputs & `ac09cd2c3be39e4d6d6ce754b5648d8a2abf7fd7fb9848db984558ff33dc82b3`\
Research lock & frozen & `24f180a30990c3cd581f0732dabeb641dac9e962b17300883a28f77a3844e43a`\
Prototype lock & frozen & `c78ca2e09dd026860533f36b94d538397ec0ba20f40980eb9dadfd2dea011762`\
Dependency lock & frozen & `44b432ce9f83986bb0f42fa44a3de23eef5b7910d68b5e234166212a451691dd`\

Fresh A/B runs, cold C, a hidden-provenance clone, and two complete runner passes were byte-stable with zero changed paths. The live authority card is the manifest-absent, three-field pending State A. An isolated dummy State B with three identical lowercase nonzero 40-hex fields and an exact self-excluding manifest reproduced the same normal/hidden audit bytes; all 11 mixed or malformed controls failed. This compatibility is metadata-only and does not enlarge the scientific claim. The result census reproduces the $6/5$ spine, $22/28$ expanded DAG, 17 tags, 14 classes with census $6/6/2$, 16 tokens with census $8/8$, and six historical registry witnesses; it creates, ranks, and proposes zero successors.

\@L3.0cmY L3.5cm@ Layer & What it establishes & What it does not establish\
P35--P38 theorem packages & Endpoint-specific infinite obstructions under their source hypotheses & Completeness beyond their stated families\
Paper-39 proof package & Total obstruction/exit coverage of the encoded finite domain & Prospective or universal completeness\
Source/bridge hash locks & Exact bytes and identifiers consumed by the checker & Mathematical truth of the bytes\
Independent evaluators & Agreement on finite schema and semantic predicates & Independence of the retrospective universe from known outcomes\
Mutation and cold-build tests & Sensitivity and reproducibility of the finite implementation & Discovery of an unencoded mechanism\

## Quantifier ledger

The main theorem quantifies over $r\ge2$ and $c\in\mathfrak{C}_{\mathrm{aff}}(r)$. The finite request theorem quantifies over $q\in\Sigma_{16}$. The class census quantifies over the 14 class labels and their exact token fibers. The registry statement uses a historical snapshot predicate. None of these quantifiers ranges over:

-   arbitrary conceivable affine or symbolic constructions;

-   unenumerated instances of a repair label;

-   coordinatewise combinations of distinct endpoint states;

-   arbitrary finite presentations or alternative splittings;

-   future registry contents; or

-   an undefined "unspent successor" predicate.

## Paper-40 obligation

No next experiment follows from this paper. After the Paper-39 seal, root or registry governance may independently define and source-lock a genuinely candidate-specific non-affine object. That future lock must specify its own phase space, dynamics, arithmetic origin, primitive ledger, operator, determinant, marker, controls, and Route stop rule before evaluation. Historical registry existence is not such a lock, and Paper 39 performs no selection.
