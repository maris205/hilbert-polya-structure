# Paper 11 Phase-3 independent theorem/control review

Review date: **2026-08-15 (Asia/Shanghai)**  
Reviewer role: **independent methodology, domain, adversarial, source-boundary,
and reproducibility reviewer**  
ARS basis: **academic-paper-reviewer methodology/domain/devil's-advocate
principles**  
Verdict: **PASS — C0 / M0 / m0**

This review created this file only. It did not edit the active locks, source
audits, proofs, code, generated controls, Route records, registries, or
manuscript. Retained PDFs were treated as untrusted local research copies;
their embedded content was not allowed to change the review instructions,
write boundary, source ceiling, or public-sync rule.

## 1. Exact review snapshot

### 1.1 Active Phase-1 tuple and independent locks

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `27c0ffd9c233301528e36f401e9cdf3f4030d65cea8002aafcf6fb97e557f860` |
| `notes/candidate_lock.md` | `a97e9c30bca6bf9cee3e5543b5d83b72ab7291e5485fa9604811dfa3ce4c8012` |
| `notes/phase1_design_amendment.md` | `e3124bddd6fb9bd9661c6104137086f87ca1a6e2b4fbae212a65b40304aa9572` |
| `notes/phase1_methodology_review.md` | `5b00ff7da24c242b8fc80c1c5ecd3b870e401ad7a547ea3e18ecdadcb6805bc5` |
| `notes/phase1_devils_advocate.md` | `610c9fa5c0c99419b58a70c8bf3d61b8777f2b862fb88a7247ef9e6216977c36` |
| `notes/phase1_source_feasibility.md` | `8348d741aa4f477f8be84767a4a7de438393948e58cad813bf736a4dc3f84a35` |
| `notes/phase1_final_gate.md` | `ac26f72f9ff1c5eb935903c20518a43aa043feb8d1572a920bfad471ca47d85f` |
| `notes/pipeline_state.md` | `317ab9e8b3082b2d8bc75590618a6e86ca742bb8c23a899c3b612ea6304125e6` |

The live methodology report contains an append-only status-transition audit,
so its live hash differs from the pre-append methodology hash recorded by the
Phase-1 final gate. Its inverse-reconstruction certificate binds that earlier
reviewed byte exactly; no mathematical definition changed in the status
transition.

### 1.2 Phase-2 source, owner, and novelty tuple

| Artifact | SHA-256 |
|---|---|
| `notes/phase2_framework_source_audit.md` | `a2345046972cc00d3031abdc214442359d0f78c7c0daf7d513ea26f924fb7439` |
| `notes/sources/framework_source_manifest.md` | `b3b61a5bdfd206cb8cc4a8bf574373bc6485d96b22547698ac69fb3a9e36812f` |
| `notes/sources/framework_sources.sha256` | `057e9c32b2f654c765f40f0ddd40014c12876d22c0567470fdf04a2eb0fd2e7f` |
| `notes/phase2_owner_proxy_audit.md` | `18116cf52c2359a840c9996fb6424fae56260f590990fac79704c040245fa761` |
| `notes/phase2_novelty_search.md` | `024398a3575cf41a7f33c6950dc1c8de8a8d5f4ec81675f8760ce7c7a87ac24e` |
| `notes/phase2_final_review.md` | `9607ec7eab0a947bf7de14d2c8a4233185c4e94994e19821d16b3f41b7c2638d` |
| `notes/phase2_final_gate.md` | `96d5bb1e82bb5db416d9b52993b13fdc6c5eb25e26e0e1896b265138b800f0fb` |

Independent `sha256sum -c framework_sources.sha256` returned **10/10 OK**:
five exact PDFs and five same-stem ARS preflight sidecars. The manifest records
all five PDF manifestations as `LOCAL_RESEARCH_ONLY`. The adjacent
`notes/sources/.gitignore`, SHA-256
`ea6768f2a011e92a3f0d4fca2e9212908efb2c6514bacdd4b448730092f09133`,
excludes `*.pdf`; no exact manifestation has public-sync permission.

### 1.3 Phase-3 proof and control tuple

| Artifact | SHA-256 |
|---|---|
| `notes/phase3_core_proofs.md` | `4e79446d4a9bb861211186ffd3aa3b42899bc382fbf215a5a453495e5fbb0a66` |
| `notes/phase3_proxy_ownership_proofs.md` | `46603a1c2185cec1ffb3e7a2cb0f70873abf995edcc104977ac3d360d76e6401` |
| `code/indiscrete_convolution_controls.py` | `8f1699570c416ec942696c8211d692deb9af5243fc84053b849ef9762aef6134` |
| `code/test_indiscrete_convolution_controls.py` | `cf6165499c3d7b37cec1b0311b2d8961e3137335039f530f275ee6ea55e23525` |
| `experiments/reproduce.sh` | `09e3cc7844aa7cf044a99d3ddd592fd830b2ae7866dc9355e7642a39f4f465ee` |
| `results/indiscrete_convolution_controls_manifest.json` | `de55c58ad7efc133b0d0865f392a30b52f6b05f89f64878cea0910b7eab557ea` |

The manifest additionally binds the three implementation READMEs and all
twelve generated CSV artifacts. The Route-A and Route-B roadmaps used for the
ceiling audit are repository versions `0.2.0`, with exact hashes
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
and `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`,
respectively.

## 2. Independent result by registered target

| Target | Independent check | Result |
|---|---|---|
| `P11-1` | The product topology has exactly the opens `X x U`; closed sets and arbitrary closures are classified. For every subset `K`, open-cover quasi-compactness is equivalent to compactness of `pi_R(K)`. Second countability, both positive local quasi-compact variants, absence of nonempty quasi-compact/Hausdorff opens, non-`T0` separation, the composable-pair chart, and continuity of all frozen groupoid maps follow with the stated quantifiers. | **PROVED / PASS** |
| `P11-2` | A continuous map to any `T0` target is constant on each equal-time fibre and factors uniquely through `pi_R`. The arrow Borel sigma-algebra is exactly `{X x B:B in B(R)}`. The countably-separated measurable-target proof uses a genuine separating family and the exact source/target sigma-algebras; the nontrivial arrow measurable space is not countably separated. | **PROVED / PASS** |
| `P11-3` | Hausdorffness of `C` forces every global function to be `Phi(g)(x,t)=g(t)`. Ambient support is exactly `X x supp_R(g)`, and the quasi-compact/compact equivalence proves both directions of `Phi:C_c(R)->C_qc^glob(G)`. | **PROVED / PASS** |
| `P11-4` | Every range fibre is an LCH copy of `R`; the author-defined Lebesgue family has positive Radon/full support, finite licensed integrals, constant unit integral, and the exact left-invariance formula. Direct substitution yields ordinary group convolution and involution, while compact support, Fubini, associativity, and the `*` identities are independently justified. | **PROVED / PASS** |
| `P11-5` | `vartheta_x(t)=(x dot (-t),t)` has the correct source, topology, and inversion-pushed measure. The exact product `gamma_t eta_u^{-1}` has time `t-u`; Young's inequality closes the dense-domain operator, adjoint identities are checked under the stated inner-product convention, and every unit norm equals the left-regular group norm. Full/reduced/Fourier conclusions are transported only from the group `R`. | **PROVED / PASS** |
| `P11-6` | A nonempty arrow open contains indistinguishable equal-time unit points and cannot be Hausdorff. Hence the raw HOpen span is exactly zero, while a nonzero `Phi(g)` proves the global algebra is nonzero. Tu, Muhly--Williams, Exel, BHM, Green/Williams, and MRW applicability remains typed by failed hypotheses, not inferred from the zero diagnostic. | **PROVED / PASS** |
| `P11-7` | The `+t`-equivariant chart makes `J` a set-groupoid isomorphism. `J` is noncontinuous and `J^{-1}` continuous in the frozen directions. The contravariant `I(f)=f o J^{-1}` preserves exact support, fibre Lebesgue measures, convolution, and involution. Its image is precisely the unit-coordinate-constant proxy subalgebra, with an explicit circle-character witness outside it. | **PROVED AT TEST-FUNCTION LEVEL / PASS** |
| `P11-8` | The proof is valid for every nonempty indiscrete `X` and every right `R`-action. Trivial, nontransitive, transitive arbitrary-period, composite-label, and non-arithmetic-label cases retain different host actions/stabilizers while producing the same global algebra, fibre formula, regular norm, and transported completions. This is correctly adjudicated as `PROVES_TOO_MUCH` for arithmetic specificity. | **PROVED / PASS** |
| `P11-9` | The deterministic package covers topology, continuous/measurable factorization, support, convolution, involution, sign/source-range negatives, regular matrices, HOpen zero, proxy strictness, action blindness, label/period independence, lock/gate/implementation hashes, strict verification, and two fresh generations. Finite controls remain witnesses rather than continuum proofs. | **EXECUTED / PASS** |
| `P11-10` | The proof tuple separates the actual groupoid, global algebra, HOpen diagnostic, transported completions, and standard proxy; `T0`--`T7` are complete at the current proof level. It states only the frozen Route ceiling and creates no Route verdict. The stable proof/control tuple now satisfies the prerequisite for the separate typed Route-A evaluation. | **HANDOFF PASS; FORMAL ROUTE ADJUDICATION NEXT** |

Thus `CONFIRM_CONVOLUTION_COLLAPSE` is independently supported, and the
mathematical legs of `CONFIRM_CONVENTION_SPLIT` are closed. `P11-10` is not
misreported as a completed Route serialization: the protocol orders this
independent review before the typed Route phase.

## 3. Mathematical and convention stress tests

### 3.1 Topology, quasi-compactness, and support

The converse in the quasi-compactness theorem is valid for arbitrary subsets,
not only products or closed sets. Every relative open of `K` is the pullback
of a time-open set, so a cover of `K` gives a cover of `pi_R(K)` and a finite
subcover returns to `K`. This also justifies the support criterion without
silently adding Hausdorffness or ambient closedness to “quasi-compact.”

The two positive local statements do not contradict the two negative open-set
statements. `X x [t-epsilon,t+epsilon]` is a quasi-compact neighborhood, and
open intervals have quasi-compact closures, while no nonempty open `X x U`
has compact time projection. Every nonempty actual arrow open is non-`T0`, so
the HOpen computation uses the exact raw patch convention and no standard
completion theorem.

### 3.2 Groupoid signs, composability, and involution

The range-first convention is consistent throughout:

```text
r(x,t)=x,
s(x,t)=x dot t,
(x,t)(x dot t,u)=(x,t+u),
(x,t)^(-1)=(x dot t,-t).
```

On a source fibre,

```text
gamma_t=(x dot (-t),t),
eta_u=(x dot (-u),u),
eta_u^(-1)=(x,-u),
gamma_t eta_u^(-1)=(x dot (-t),t-u).
```

This gives `g(t-u)`, not `g(t+u)`, and the exact left-regular kernel. The
involution gives `conjugate(g(-t))`; the anti-multiplicative identity follows
with the displayed change of variables. No modular factor is licensed or
needed for the additive unimodular group `R` under the frozen fibre family.

### 3.3 Integral, operator, and norm domains

Every licensed global function corresponds to `g in C_c(R)`, so fibre
integrals are absolutely finite. The regular integral is initially evaluated
on `C_c(G_x)`; it is not asserted pointwise for arbitrary `L^2` equivalence
classes. Young's estimate gives the unique bounded extension. Equality with
the group left-regular representation is unitary at every base unit, and the
explicit nonzero-vector test proves that the reduced seminorm is a norm.

The full norm is defined by transport from the universal group norm, while
the reduced norm is proved from the frozen `Ind_x` records. Only after both
steps does group amenability identify them. The completion names remain
`C^full_glob` and `C^red_glob`; neither proof file promotes them to standard
`C^*(G_act)` or `C_r^*(G_act)`.

### 3.4 Actual/proxy direction and strictness

The standard circle is a strictly finer retopology on the same set. A proper
circle arc pulls back under `J` to a proper unit-coordinate subset and proves
that `J` is not continuous. In the reverse direction every actual open pulls
back under `J^{-1}` to `S x U`, so `J^{-1}` is continuous.

At the test-function level, `I` maps exactly to functions constant in the
unit coordinate. The witness

```text
F_out([r],t)=exp(2*pi*i*r/L_p) k(t)
```

is well-defined on `R/L_p Z`, compactly supported in the arrow space, and
not in that image. No boundedness, density, isometry, Morita equivalence, or
completion extension of `I` is inferred.

## 4. Source, applicability, ownership, and same-object audit

The retained source ladder is used at its exact strength:

- Tu and Muhly--Williams supply genuine HOpen-style conventions only under
  locally Hausdorff/local-compactness hypotheses that the actual object
  fails;
- Exel's non-Hausdorff-arrow setting still requires a Hausdorff LCH unit and
  etale range/source maps;
- BHM's transformation-groupoid theorem and Williams/Green/MRW results apply
  only to the ordinary Hausdorff-circle proxy after the recorded sign and
  measure conversions;
- Williams supplies `C^*(R)=C_r^*(R)` and the Fourier model to the group
  owner, activated on the actual author-defined objects only through the
  proved transport;
- no retained theorem supplies a standard actual-groupoid `C*` algebra or a
  completion extension of `I`.

The `T0`--`T7` certificate independently closes as follows:

| Gate | Review result |
|---|---|
| `T0` identity | Exact fixed `p,a`, actual orbit, right action, and range-first groupoid are bound. |
| `T1` topology | Actual `X_indisc x R` and proxy `S_std x R` are verified distinct. |
| `T2` map | `J`, `J^{-1}`, `I`, and `Phi` directions are exact. |
| `T3` function convention | Global QC, raw HOpen, and standard proxy `C_c` owners are never conflated. |
| `T4` fibre measure | Range/source fibres and inversion-pushed Lebesgue measures are exact; `J` preserves them at test level. |
| `T5` algebra/completion | Convolution, involution, and actual transported norms are proved; proxy completion transport is withheld. |
| `T6` aggregation | Arithmetic specialization is one fixed orbit for arbitrary `p,a`; no packet, coproduct, or suspension promotion occurs. |
| `T7` arithmetic promotion | The global algebra/norm/completions erase `p,a,L_p`, the action, orbit decomposition, and stabilizer; no analytic survival credit is available. |

Owner attribution is therefore coherent: Deninger owns the set/action and
stabilizer, Paper 9 owns actual indiscreteness, Paper 11 owns the author
groupoid and direct constructions, Williams owns the group/proxy source
theorems, and the ordinary circle remains a proxy modeling choice.

## 5. Novelty, standalone, and Route ceilings

The bounded search is frozen at
`last_searched_at=2026-08-15T00:37:14+08:00`. It found zero included
precedents for the exact registered package and supports only
`SUPPORTED_WITHIN_SEARCH`. Endpoint degradation and non-exposed corpus totals
remain disclosed. The generic indiscrete-product theorem, ordinary group
convolution, HOpen framework, and standard-circle crossed product receive no
individual novelty claim.

The two mathematical components required by the predeclared standalone gate
are now proved: the nonzero-global/zero-HOpen convention split and the strict
test-function proxy boundary. Together with the bounded search, this closes
the **mathematical/search leg** of standalone eligibility. It does not grant a
final release: typed Route evaluation, composition, citation, peer, and
release audits remain mandatory.

The exact Route ceiling is preserved:

1. The actual transformation groupoid retains the source action and
   stabilizer only as host relations; the immutable Stage-9 actual-orbit
   groupoid record must not be reissued.
2. The concrete global algebra, its abstract `C_c(R)` isomorphism class, and
   each transported completion require separate A0 records. None inherits
   analytic-arithmetic A0 credit from its host.
3. Action blindness and the explicit trivial/nontransitive/composite/arbitrary
   controls force the global analytic records to fail the primitive-orbit
   relevance sought at A1; the same mechanism is `PROVES_TOO_MUCH`, not a
   positive arithmetic signal.
4. No same-object dynamical determinant, validation/divisor result,
   continuation/functional equation, Weil compression, or natural
   quantization exists; A2, A3, and A4 cannot receive positive credit.
5. The standard-circle owner is a modeling-choice proxy and grants no actual
   topology or completion credit.
6. Route B is not testable or invocable: there is no Route-A-ready operator,
   domain, self-adjointness theorem, target spectral type, von-Mangoldt trace,
   or completed-xi determinant. No Route-B YAML is authorized.

These are evidence ceilings for `P11-10`, not serialized verdicts. The next
phase must apply the typed Route-A evaluator separately to each new owner and
must leave `route_b_invocation_allowed: false`.

## 6. Independent deterministic reproduction

I executed from the Paper-11 directory:

```text
./experiments/reproduce.sh
```

Observed receipt:

```text
unit tests: 57/57 PASS
CSV artifacts: 12
total data rows: 642
intentional negative controls: 5/5 detected
checked-in generation: strict verify-only PASS
fresh generation one: strict verify-only PASS
fresh generation two: strict verify-only PASS
checked-in / fresh one / fresh two: all 13 generated artifacts byte-identical
Python cache/bytecode scan: PASS
manifest SHA-256: de55c58ad7efc133b0d0865f392a30b52f6b05f89f64878cea0910b7eab557ea
```

Independent row counts and artifact hashes were:

| CSV | Rows | SHA-256 |
|---|---:|---|
| `action_blind_controls.csv` | 3 | `bbb10ff8fd09616c0e3685153997c6a42b72769942488218ec33222aa9db335d` |
| `arrow_topology_controls.csv` | 72 | `70dd4e43f4f2bb05b08e9dad54d23e30bb69a7bbf44103bcfeb498ca89eb1091` |
| `convention_negative_controls.csv` | 5 | `1e09375d338b124adf94f231967cc96e1171835ffda210763982545c462036a5` |
| `convolution_controls.csv` | 36 | `941abddaa2ba866c6cb4747fa7c295a52d83e472218444f02aee496e259528ff` |
| `hopen_zero_controls.csv` | 6 | `ac910e7d4bcda1c817daa95dc2ca84f8de8c84d167da082abf096a3dea1aebf9` |
| `involution_controls.csv` | 36 | `21d763affbb51407db9a165f4f60fa67bed30a4370f4dfca4971d6b4e0326639` |
| `label_period_independence_controls.csv` | 27 | `7ec906e5085446f16fd5f23d6fa1edc65416f8e04b43494fafaa9c826ad2688b` |
| `measurable_time_factorization_controls.csv` | 160 | `d4eb0cb7a48c6b1dd412c21799c191514403137d51a27f8c85f5c564fda6d495` |
| `proxy_strictness_controls.csv` | 6 | `c08a8c822b02ff948c99ce7185465de663e9d6d30e706fa529bdfc0fca15136d` |
| `support_projection_controls.csv` | 15 | `87072b4a6fbe7ae12fe28485553f381016e97c401d90aea3b5feadd0aec0f32d` |
| `t0_time_factorization_controls.csv` | 240 | `c0d20ba02d292e5bfb45cac87fa63d10aad1207c56ed4796bf66cc52ba99c1ff` |
| `unit_regular_controls.csv` | 36 | `d09600ade733c9ce09a69deb9096238c261f18cced6c2f0edc7436acd8a76edc` |

The test suite also exercised fail-closed rejection of artifact tampering,
missing and extra artifacts, manifest-metric drift, active-lock drift,
Phase-2-gate drift, and implementation drift. The generator imports only the
Python standard library. The reviewed execution path contains no network
client, external dataset, random source, target-zero table, fitted parameter,
or timestamp. The raw unit-dependent source/range probe is explicitly outside
the licensed global algebra, and the fully discrete proxy is separately
typed; neither is promoted to the actual owner.

## 7. Devil's-advocate adjudication

The strongest counter-argument is that the main collapse is too general to
carry arithmetic content: it works unchanged for a trivial action, two
nontransitive orbits, arbitrary periods, and arbitrary labels. That attack is
**valid as an arithmetic/Route objection but does not refute the theorem**.
The proof itself makes the generic theorem explicit, denies novelty and A0/A1
credit to the erased analytic outputs, and treats the broad controls as a
`PROVES_TOO_MUCH` obstruction. The rational-Witt contribution is therefore
the exact actual-owner application plus the convention and proxy boundary,
not a claim that `C_c(R)` detects primes.

A second attack is that an author-defined function/fibre convention might be
mistaken for a standard non-Hausdorff groupoid `C*` construction. It is
rejected on the exact text: every published-framework applicability result is
kept separate, all retained actual frameworks are `NOT_APPLICABLE`, HOpen
zero is diagnostic only, and the completion names remain explicitly
transported author objects.

A third attack is that the finer standard proxy could silently restore the
lost stabilizer and then be presented as the actual completion. It is also
closed: only the test-function monomorphism is proved, its image is proper,
and the proof stops before every norm extension, density, Morita, stable, or
completion-isomorphism claim.

No unresolved counter-argument reaches Critical, Major, or Minor severity.

## 8. Findings and coverage receipt

```text
Critical: 0
Major:    0
Minor:    0
```

No weakness reached the finding threshold.

**Coverage receipt — Weaknesses**

| Dimension examined | What was checked | Basis for no finding |
|---|---|---|
| Logical validity | `P11-1`--`P11-8`, all substitutions, closure arguments, Fubini/Young steps, adjoint and faithfulness arguments | Every conclusion follows from the exact nonempty-indiscrete/product/fibre premises; no finite control is used as a theorem premise. |
| Domains and signs | Quasi-compact support, range/source fibres, inversion pushforward, composability, convolution, involution, Fourier sign | All expressions are defined on compatible owners and reproduce the frozen `t-u` left-regular convention. |
| Source applicability | Tu, Muhly--Williams, Exel, BHM, Williams/Green/MRW and the group-`R` transport | Source theorems remain inside their verified hypotheses and exact actual/proxy/group owners. |
| Ownership and same-object gates | Actual orbit, groupoid, global/HOpen conventions, transported completions, proxy, `T0`--`T7` | No topology, measure, algebra, norm, aggregation, or arithmetic credit crosses owners. |
| Reproducibility | Code, tests, manifest, rows, hashes, negative controls, strict verification, fresh generations, cache scan | Independent execution reproduced all frozen bytes and fail-closed checks. |
| Novelty and standalone scope | Exact package definition, bounded endpoint ledger, generic-background exclusions, downstream gates | Only `SUPPORTED_WITHIN_SEARCH` and mathematical/search-leg eligibility are claimed; final publication status is not pre-certified. |
| Route ceiling | A0--A4 requirements, proves-too-much gate, Route-B entry conditions | The review states only evidence ceilings and hands the stable tuple to the separate typed evaluator. |

## 9. Final verdict and authorization boundary

**PASS — C0 / M0 / m0.** The exact Phase-3 package proves `P11-1`--`P11-8`,
executes `P11-9` as a deterministic finite regression/falsification package,
and supplies the separated owner/same-object/Route ceiling required to begin
`P11-10`. The results support `CONFIRM_CONVOLUTION_COLLAPSE`; they also close
the convention-split and strict-proxy mathematical legs required by the
standalone gate.

No revision is required before the separate typed Route-A evaluation and
integrated proof/composition audit. This PASS does not authorize a standard
actual-groupoid `C*` name, a completion extension of `I`, arithmetic spectral
credit, a packet/global theorem, an absolute priority claim, Route B, or
manuscript release.
