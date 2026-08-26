# Paper 11 integrated proof, ownership, and Route audit

Audit date: **2026-08-15 (Asia/Shanghai)**  
Integrated verdict: **`CONFIRM_CONVOLUTION_COLLAPSE` with `CONFIRM_CONVENTION_SPLIT`**  
Mathematical targets: **`P11-1`--`P11-8` proved**  
Deterministic controls: **`P11-9` PASS — 57/57 tests, 12 CSVs, 642 rows, 5/5 intentional negatives**  
Typed Route serialization: **`P11-10` PASS — 7 Route-A records, 0 Route-B records**  
Independent proof findings: **0 Critical / 0 Major / 0 Minor**  
Manuscript status: **eligible for drafting; standalone release not yet granted**

## 1. Scope of this audit

This report integrates the active Phase-1 design, the final Phase-2
source/applicability/search gate, the two direct Phase-3 proof reports, the
deterministic control package, the independent Phase-3 review, and the final
typed Route evaluation. It creates no new mathematical object and does not
upgrade any theorem beyond its proved owner and domain.

The exact result is convention-sensitive:

```text
actual inherited topology + author global-QC convention
    => C_qc^glob(G_{p,a}^act) ~= C_c(R), nonzero;

actual inherited topology + raw HOpen diagnostic convention
    => C_c^HOp(G_{p,a}^act) = {0};

ordinary-circle standard proxy topology
    => a strictly larger test-function algebra, with the actual image
       equal to the proper unit-coordinate-constant subalgebra A_const.
```

The second line is `DIAGNOSTIC_ONLY`. The first line uses the author-defined
`GLOB-FIBRE-FAMILY`, `Ind_x`, and transported completion names. The third
line is a proxy statement. None is a standard groupoid C*-algebra theorem on
the actual inherited topology.

## 2. Exact-byte evidence lock

### 2.1 Phase-1 design and final gate

| Artifact | SHA-256 | Status bound here |
|---|---|---|
| `notes/research_protocol.md` | `27c0ffd9c233301528e36f401e9cdf3f4030d65cea8002aafcf6fb97e557f860` | active protocol |
| `notes/candidate_lock.md` | `a97e9c30bca6bf9cee3e5543b5d83b72ab7291e5485fa9604811dfa3ce4c8012` | final owners, conventions, and ceilings |
| `notes/phase1_design_amendment.md` | `e3124bddd6fb9bd9661c6104137086f87ca1a6e2b4fbae212a65b40304aa9572` | repaired design |
| `notes/phase1_methodology_review.md` | `5b00ff7da24c242b8fc80c1c5ecd3b870e401ad7a547ea3e18ecdadcb6805bc5` | final `PASS` |
| `notes/phase1_devils_advocate.md` | `610c9fa5c0c99419b58a70c8bf3d61b8777f2b862fb88a7247ef9e6216977c36` | final `PASS` |
| `notes/phase1_source_feasibility.md` | `8348d741aa4f477f8be84767a4a7de438393948e58cad813bf736a4dc3f84a35` | final `PASS` |
| `notes/phase1_final_gate.md` | `ac26f72f9ff1c5eb935903c20518a43aa043feb8d1572a920bfad471ca47d85f` | Phase-1 release `PASS` |
| `notes/pipeline_state.md` | `317ab9e8b3082b2d8bc75590618a6e86ca742bb8c23a899c3b612ea6304125e6` | active state bound by the proof reports |

The review history is conserved: the first methodology pass found
`C0/M6/m2`, the first devil's-advocate pass found `C0/M5/m3`, and the first
source-feasibility pass found `C0/M3/m1`. Those findings were repaired in the
design amendment and re-reviewed; they are not silently erased by the final
`PASS` labels.

### 2.2 Phase-2 framework, owner, and novelty gate

| Artifact | SHA-256 | Status bound here |
|---|---|---|
| `notes/phase2_framework_source_audit.md` | `a2345046972cc00d3031abdc214442359d0f78c7c0daf7d513ea26f924fb7439` | framework hypotheses and exact source strengths |
| `notes/sources/framework_source_manifest.md` | `b3b61a5bdfd206cb8cc4a8bf574373bc6485d96b22547698ac69fb3a9e36812f` | five-source local manifest |
| `notes/sources/framework_sources.sha256` | `057e9c32b2f654c765f40f0ddd40014c12876d22c0567470fdf04a2eb0fd2e7f` | checksum ledger, 10/10 verified in review |
| `notes/phase2_owner_proxy_audit.md` | `18116cf52c2359a840c9996fb6424fae56260f590990fac79704c040245fa761` | actual/proxy/source owner split |
| `notes/phase2_novelty_search.md` | `024398a3575cf41a7f33c6950dc1c8de8a8d5f4ec81675f8760ce7c7a87ac24e` | bounded search through 2026-08-15 |
| `notes/phase2_final_review.md` | `9607ec7eab0a947bf7de14d2c8a4233185c4e94994e19821d16b3f41b7c2638d` | independent source/owner/search synthesis |
| `notes/phase2_final_gate.md` | `96d5bb1e82bb5db416d9b52993b13fdc6c5eb25e26e0e1896b265138b800f0fb` | Phase-2 final `PASS` |

The bounded novelty status is exactly `SUPPORTED_WITHIN_SEARCH`. It is not
an absolute priority finding. The generic indiscrete-action theorem receives
no novelty claim.

### 2.3 Phase-3 proofs, controls, review, and Route gate

| Artifact | SHA-256 | Role |
|---|---|---|
| `notes/phase3_core_proofs.md` | `4e79446d4a9bb861211186ffd3aa3b42899bc382fbf215a5a453495e5fbb0a66` | direct proofs of `P11-1`--`P11-5` |
| `notes/phase3_proxy_ownership_proofs.md` | `46603a1c2185cec1ffb3e7a2cb0f70873abf995edcc104977ac3d360d76e6401` | direct proofs of `P11-6`--`P11-8` |
| `code/indiscrete_convolution_controls.py` | `8f1699570c416ec942696c8211d692deb9af5243fc84053b849ef9762aef6134` | deterministic generator |
| `code/test_indiscrete_convolution_controls.py` | `cf6165499c3d7b37cec1b0311b2d8961e3137335039f530f275ee6ea55e23525` | 57-test suite |
| `experiments/reproduce.sh` | `09e3cc7844aa7cf044a99d3ddd592fd830b2ae7866dc9355e7642a39f4f465ee` | strict reproduction entry point |
| `results/indiscrete_convolution_controls_manifest.json` | `de55c58ad7efc133b0d0865f392a30b52f6b05f89f64878cea0910b7eab557ea` | final 13-artifact manifest |
| `notes/phase3_peer_review.md` | `b16027be916e4e6b8787bce8692dd8461f1e79fb29ea73b9b1d67f530341ad5c` | independent `PASS — C0/M0/m0` |
| `notes/route_audit.md` | `9203d37cfaa28a45a7548a9864de614c81bf6ea199b4a6736e1c5aaa84335011` | final typed Route audit |

The independent reviewer reproduced 57/57 tests, 12 CSVs and 642 rows,
detected all five intentional negatives, passed strict verification on the
checked-in results and two fresh generations, found all 13 generated
artifacts byte-identical, and passed the Python-cache scan. The final Route
review repeated the relevant validation after serialization.

## 3. Frozen domain and notation

The proof first treats a generic object. Let `X` be a nonempty indiscrete
space and let `x dot t` be any right action of the additive group `R`. Give

```text
G(X,alpha)=X x R
```

the product topology and range-first operations

```text
r(x,t)=x,
s(x,t)=x dot t,
(x,t)(x dot t,u)=(x,t+u),
(x,t)^(-1)=(x dot t,-t).
```

Every such action is jointly continuous because the codomain `X` is
indiscrete. No transitivity, freeness, period, or stabilizer is used in the
generic theorem.

Only after that theorem is proved does the rational-Witt application fix an
arbitrary prime `p` and normalized Paper-9 orbit label `a` and set

```text
X=X_{p,a}=ACT-ORBIT-p-a,
G=G_{p,a}^act,
L_p=log p.
```

Paper 9 supplies that `X_{p,a}` is nonempty, nontrivial, and indiscrete.
Deninger supplies the underlying right action and stabilizer `L_p Z`. The
proof does not import the ordinary-circle topology and does not use the
stabilizer to derive the analytic objects.

## 4. Integrated target matrix

| Target | Exact claim and result | Proof owner / locator | Control witness | Nonpromotion ceiling |
|---|---|---|---|---|
| `P11-1` | arrow opens, closures, quasi-compactness, local variants, separation, and groupoid structure are classified; `PROVED` | core proof §§2.1--2.4 | arrow-topology and support-projection CSVs | actual product topology only; no local-Hausdorff claim |
| `P11-2` | continuous maps to `T0` targets and measurable maps to countably separated targets factor uniquely through time; `PROVED` | core proof §§3.1--3.3 | `T0` and measurable-factorization CSVs | separated targets only; actual source is not countably separated |
| `P11-3` | `Phi:C_c(R)->C_qc^glob(G)` is a bijection with exact support; `PROVED` | core proof §4.1 | support-projection CSV | open-cover quasi-compact support, not Hausdorff compact support |
| `P11-4` | `GLOB-FIBRE-FAMILY`, convolution, involution, associativity, and `*` identities satisfy their author contract; `PROVED` | core proof §§5.1--5.3 | convolution, involution, and convention-negative CSVs | not a retained standard Haar-system theorem |
| `P11-5` | source-fibre coordinates, `Ind_x`, reduced norm, transported full/reduced completions, and group Fourier model are exact; `PROVED` | core proof §§6.1--6.5 | unit-regular and convention-negative CSVs | author-defined names only; group-`R` facts are transported after direct proof |
| `P11-6` | no nonempty Hausdorff arrow open exists; raw `C_c^HOp={0}`; actual standard frameworks are inapplicable; `PROVED` | proxy/ownership proof §§3.1--3.3 | HOpen-zero CSV | zero is `DIAGNOSTIC_ONLY`, not a standard groupoid algebra |
| `P11-7` | `J` is a set-groupoid isomorphism, `J` is not continuous, `J^{-1}` is continuous, and `I` is a strict test-function `*`-monomorphism with image `A_const`; `PROVED` | proxy/ownership proof §§4.1--4.6 | proxy-strictness CSV | no bounded, isometric, dense, Morita, stable, or completion extension |
| `P11-8` | the collapse is action-blind for every nonempty indiscrete action; the rational-Witt fixed orbit is a separate application; `PROVED` | proxy/ownership proof §§6.1--6.3 | action-blind and label/period CSVs | generic theorem has no arithmetic novelty; application is fixed-orbit only |
| `P11-9` | finite exact adversarial controls reproduce all registered witnesses and negatives; `PASS` | final manifest, generator, test suite, reproduce script | 57/57; 12/642; 5/5 | controls witness formulas and failure modes; they do not prove continuous universal theorems |
| `P11-10` | seven nonconflated owners receive typed A0--A4 records; `PASS` | final Route audit and seven Stage-11 YAMLs | schema, enum, nine-A2-metric, path/hash, peer-binding checks | three exploratory negative priors, four rejected records, Route B false |

## 5. Proof dependency and conservation ledger

The proof order is one-directional:

```text
Paper-9 actual indiscrete fixed-orbit topology + Deninger right action
  -> exact arrow topology and time factorization
  -> Phi function/support classification
  -> direct author fibre and convolution formulas
  -> direct source-fibre and Ind_x formulas
  -> transported group-R full/reduced completions

exact arrow topology
  -> no nonempty Hausdorff arrow open
  -> raw HOpen diagnostic = 0
  -> retained actual standard frameworks NOT_APPLICABLE

actual/proxy set chart
  -> one-sided topology direction for J
  -> strict test-function map I with image A_const
  -> explicit stop before every completion comparison

generic nonempty-indiscrete theorem
  -> trivial/nontransitive/arbitrary-period/label controls
  -> rational-Witt fixed-orbit application
  -> typed Route obstruction.
```

Published group and proxy theorems enter only after the direct owner-specific
claims have been proved. No proxy theorem is used to prove an actual-topology
claim, and no arithmetic label is used to prove the generic theorem.

## 6. Direct mathematical audit: `P11-1`--`P11-5`

### 6.1 Arrow topology and quasi-compactness

Every arrow open has the form `X x U` with `U` open in `R`; every arrow
closed has the form `X x F` with `F` closed. For arbitrary `K subset G`,

```text
closure_G(K)=X x closure_R(pi_R(K)),
K is quasi-compact iff pi_R(K) is compact in R.
```

The criterion uses the open-cover definition of quasi-compactness. It does
not relabel a non-Hausdorff arrow subset as compact in a Hausdorff sense.
The arrow space is second countable and has the proved positive local
quasi-compact variants, but for nontrivial `X` it is not `T0` and has no
nonempty Hausdorff open subset. The range, source, multiplication, inverse,
and composable-pair chart are proved continuous directly.

### 6.2 Continuous and measurable factorization

For every `T0` space `Y`, each continuous `F:G->Y` has a unique continuous
`f:R->Y` with

```text
F=f o pi_R.
```

The exact arrow Borel sigma-algebra is

```text
B(G)={X x B : B in B(R)}.
```

For every countably separated measurable target, each measurable map from
`G` factors uniquely through the time coordinate. Removing target
separation is an explicit negative control. When `X` is nontrivial, the
actual arrow measurable space itself is not countably separated; no standard
Borel-source status is inferred.

### 6.3 Global function and support classification

Define

```text
Phi(g)(x,t)=g(t).
```

Then

```text
Phi:C_c(R) -> C_qc^glob(G)
```

is a linear bijection, and for every continuous `g`,

```text
supp_G(Phi(g))=X x supp_R(g).
```

Both directions of the support gate are proved: quasi-compact arrow support
projects to compact time support, and compact time support lifts to
quasi-compact arrow support. This is the exact owner of the nonzero global
algebra.

### 6.4 Author fibre and convolution algebra

For each unit `x`, the range-fibre chart `rho_x(t)=(x,t)` transports
Lebesgue measure to `lambda^x`. The named `GLOB-FIBRE-FAMILY` satisfies its
explicit positivity, Radon-on-the-fibre, support, integration, and
left-invariance contract. This direct verification does not promote the
family to a Haar system in a retained published actual-groupoid framework.

For `g,k in C_c(R)`,

```text
(g*k)(t)=integral_R g(u)k(t-u)du,
g^sharp(t)=conjugate(g(-t)),
Phi(g)*Phi(k)=Phi(g*k),
Phi(g)^*=Phi(g^sharp).
```

Absolute integrability, continuity, support control, Fubini, associativity,
anti-multiplicativity, and involutivity are checked directly. The action,
period, and stabilizer disappear as derived consequences of the formulas.

### 6.5 Source fibres, regular operators, and transported completions

The exact source fibre and measure are

```text
G_x={(x dot (-t),t):t in R},
vartheta_x(t)=(x dot (-t),t),
lambda_x=(inversion)_*lambda^x=(vartheta_x)_*(dt).
```

The resulting unitary `U_x` gives

```text
[U_x Ind_x(Phi(g)) U_x^(-1)zeta](t)
  =integral_R g(t-u)zeta(u)du
  =[lambda_R(g)zeta](t).
```

The dense-domain integral, Young bound, bounded extension, representation
law, adjoint, and faithfulness are all proved. Consequently

```text
||Phi(g)||_(red,glob)=||lambda_R(g)||.
```

The full norm is separately defined by transport from the universal group
norm on `C_c(R)`. Only then are the group-`R` amenability and Fourier results
used to obtain the author-defined identifications

```text
C^full_glob(G) ~= C^red_glob(G) ~= C_0(R).
```

These names must not be rewritten as `C^*(G_act)` or `C_r^*(G_act)`.
Full/reduced equality belongs to the amenable group `R`, not to an actual
groupoid amenability theorem.

## 7. Convention, proxy, and action-blind audit: `P11-6`--`P11-8`

### 7.1 Raw HOpen diagnostic and framework boundary

For nontrivial indiscrete `X`, every nonempty arrow open contains
topologically indistinguishable points, so it is not Hausdorff. Therefore

```text
C_c^HOp(G_act)={0}.
```

This is the span of raw zero-extensions from legal Hausdorff open patches.
It has no licensed convolution, norm, completion, or standard-framework
status. In the same actual topology, nonzero `Phi(g)` with `g in C_c(R)`
shows that `C_qc^glob(G_act)` is nonzero. The split is therefore exact and
not a change of notation for one algebra.

The retained Tu, Muhly--Williams, Exel, and Buss--Holkar--Meyer frameworks
are `NOT_APPLICABLE` to the actual owner because their exact standing
hypotheses fail. This proves only non-applicability of those audited
frameworks; it is not a universal nonexistence theorem for every possible
non-Hausdorff convolution construction.

### 7.2 Strict actual/proxy test-function boundary

The set-groupoid map and its inverse are

```text
J(x,t)=(beta(x),t),
J^(-1)([r],t)=(theta([r]),t).
```

Their topology direction is strict:

```text
J is not continuous,
J^(-1) is continuous.
```

Contravariant pullback along the continuous direction defines only

```text
I:C_qc^glob(G_act) -> C_c(G_std),
I(f)=f o J^(-1).
```

It preserves the proved test-function support, fibre integrals, convolution,
and involution, and

```text
image(I)=A_const
```

is the proper unit-coordinate-constant subalgebra. For nonzero
`k in C_c(R)`, the standard-proxy function

```text
F_out([r],t)=exp(2 pi i r/L)k(t)
```

is an explicit witness outside the image. There is no proved norm extension
of `I`; hence there is no actual-to-proxy completion map, density theorem,
Morita equivalence, stable isomorphism, or unstabilized completion
isomorphism.

### 7.3 Generic theorem first, rational-Witt application second

For every nonempty indiscrete `X` and every right `R`-action, the global
algebra, fibre formulas, `Ind_x` family, regular norm, and transported
completions reduce to the corresponding group-`R` records. If `X` is also
nontrivial, the raw HOpen diagnostic is zero. The singleton exception affects
only the HOpen-zero statement, not the global convolution collapse.

This generic theorem is then applied to each fixed rational-Witt orbit. In
the abstract algebra, fibre formula, regular norm, and transported
completion, none of

```text
p, a, L_p, the action, the orbit decomposition, or the stabilizer L_p Z
```

survives. The concrete host still retains its action and stabilizer as
relations. The result is not a packet theorem, prime coproduct theorem,
full-suspension theorem, or new Deninger source theorem.

## 8. Claim-owner-source-domain matrix

| Record | Exact owner and domain | Source of authority | Licensed claim | Forbidden inheritance |
|---|---|---|---|---|
| right action and `L_p Z` | Deninger fixed-prime rational-Witt orbit | Deninger source, as locked in Phase 2 | arithmetic input only | actual topology, author algebra, or completion |
| actual inherited orbit topology | Paper-9 `ACT-ORBIT-p-a` | Paper-9 proof/source audits locked by Phase 1 | nonempty, nontrivial, indiscrete | ordinary-circle topology |
| actual arrow topology | Paper-11 `G_{p,a}^act=X_{p,a} x R` | direct `P11-1` proof | topology, groupoid maps, quasi-compactness | standard local-Hausdorff framework status |
| `C_qc^glob` | globally continuous functions with open-cover-quasi-compact support | direct `P11-2`--`P11-4` proofs | `*`-isomorphic to `C_c(R)` | standard `C_c(G_act)` or actual groupoid C* terminology |
| `C_c^HOp` | raw span of zero-extensions from Hausdorff arrow opens | direct `P11-6` proof | exact value `{0}` | convolution, norm, completion, or standard algebra status |
| `GLOB-FIBRE-FAMILY` | author range-fibre family on the named global domain | direct `P11-4` proof | exact contract and formula | retained standard Haar-system credit |
| `Ind_x` | author source-fibre operator family | direct `P11-5` proof | unitary equivalence to `lambda_R` | standard actual-groupoid regular representation terminology |
| `C^full_glob` | norm transported from `C^*(R)` after `Phi` | author definition plus Williams group theorem | transported full completion | `C^*(G_act)` or proxy completion |
| `C^red_glob` | supremum of directly proved `Ind_x` norms | direct proof, then Williams group theorem | transported reduced completion | `C_r^*(G_act)` or proxy reduced algebra |
| `C^*(R)=C_r^*(R)~=C_0(R)` | additive group `R` | Williams group results | group classification and transport target | arithmetic, actual-groupoid, or determinant credit |
| `G_std` and `C_c(G_std)` | ordinary-circle Hausdorff proxy | direct `P11-7` proof plus proxy-only source ladder | strict test-function comparison | actual topology or actual completion credit |
| proxy crossed-product/tensor/Morita records | standard proxy only | BHM, Green, MRW, BGR, Williams at audited strengths | proxy classifications only | actual theorem or a completion extension of `I` |
| generic action-blind control | all nonempty indiscrete actions | direct `P11-8` theorem | reusable obstruction | arithmetic novelty or fixed-orbit owner credit |

## 9. Framework and source-applicability matrix

| Source/framework | Exact role retained | Actual `G_act` | Standard proxy / group owner | Ceiling |
|---|---|---|---|---|
| Deninger | right action and stabilizer; fixed-orbit arithmetic input | input only | not a completion source | no new Deninger theorem |
| Tu 2004 | terminology and Hausdorff-open comparison | `NOT_APPLICABLE` | not used for proxy classification here | local-Hausdorff requirement fails |
| Muhly--Williams 2008 | raw Hausdorff-open-span practice and equivalence context | `NOT_APPLICABLE` | selected proxy full-level context only | Hausdorff-unit/neighborhood hypotheses fail actual |
| Exel 2009 | independent étale boundary | `NOT_APPLICABLE` | no positive claim needed | unit and local-homeomorphism hypotheses fail |
| Buss--Holkar--Meyer 2018 | full transformation-groupoid/crossed-product proxy theorem | `NOT_APPLICABLE` | `APPLICABLE_PROXY_ONLY` | no reduced bridge or actual theorem |
| Green / MRW / BGR | Morita, equivalence, and stable strengths at the audited levels | `NOT_APPLICABLE_ACTUAL` | `APPLICABLE_PROXY_ONLY` | strengths are not interchangeable; no cancellation of `K` |
| Williams | group `R` Fourier/amenability and separate proxy theorems | group transport only after direct proof | `APPLICABLE_GROUP_R` or `APPLICABLE_PROXY_ONLY` | never a standard actual-groupoid theorem |
| Paper-11 author constructions | direct global-QC fibre/regular/completion objects | `AUTHOR_DEFINED_DIRECT` | not proxy records | exact names and direct proofs required |

The five retained source PDFs and their preflight records remain local
research evidence. They are excluded from public synchronization by the
repository PDF rule; this audit grants no permission to publish them.

## 10. Deterministic-control matrix

| CSV artifact | Rows | SHA-256 | Exact witness role |
|---|---:|---|---|
| `results/action_blind_controls.csv` | 3 | `bbb10ff8fd09616c0e3685153997c6a42b72769942488218ec33222aa9db335d` | one signature across trivial, transitive, and nontransitive action models |
| `results/arrow_topology_controls.csv` | 72 | `70dd4e43f4f2bb05b08e9dad54d23e30bb69a7bbf44103bcfeb498ca89eb1091` | finite indiscrete-product opens and topology operations |
| `results/convention_negative_controls.csv` | 5 | `1e09375d338b124adf94f231967cc96e1171835ffda210763982545c462036a5` | five wrong-sign/source-range conventions detected |
| `results/convolution_controls.csv` | 36 | `941abddaa2ba866c6cb4747fa7c295a52d83e472218444f02aee496e259528ff` | exact finite convolution identities |
| `results/hopen_zero_controls.csv` | 6 | `ac910e7d4bcda1c817daa95dc2ca84f8de8c84d167da082abf096a3dea1aebf9` | raw HOpen zero in nontrivial indiscrete controls |
| `results/involution_controls.csv` | 36 | `21d763affbb51407db9a165f4f60fa67bed30a4370f4dfca4971d6b4e0326639` | exact involution and `*` identities |
| `results/label_period_independence_controls.csv` | 27 | `7ec906e5085446f16fd5f23d6fa1edc65416f8e04b43494fafaa9c826ad2688b` | independent prime/composite/arbitrary labels crossed with periods |
| `results/measurable_time_factorization_controls.csv` | 160 | `d4eb0cb7a48c6b1dd412c21799c191514403137d51a27f8c85f5c564fda6d495` | measurable factorization and nonseparated negatives |
| `results/proxy_strictness_controls.csv` | 6 | `c08a8c822b02ff948c99ce7185465de663e9d6d30e706fa529bdfc0fca15136d` | constant actual image versus unit-dependent proxy witnesses |
| `results/support_projection_controls.csv` | 15 | `87072b4a6fbe7ae12fe28485553f381016e97c401d90aea3b5feadd0aec0f32d` | support/quasi-compactness projection gate |
| `results/t0_time_factorization_controls.csv` | 240 | `c0d20ba02d292e5bfb45cac87fa63d10aad1207c56ed4796bf66cc52ba99c1ff` | exhaustive finite `T0` factorization |
| `results/unit_regular_controls.csv` | 36 | `d09600ade733c9ce09a69deb9096238c261f18cced6c2f0edc7436acd8a76edc` | identical unit-regular matrices and sign-sensitive kernels |
| **Total** | **642** | manifest `de55c58ad7efc133b0d0865f392a30b52f6b05f89f64878cea0910b7eab557ea` | **57/57 tests; 5/5 intentional negatives** |

The controls use exact finite analogues and Gaussian-integer arithmetic where
appropriate. They are adversarial witnesses and reproducibility records,
not numerical evidence for the universal continuous proofs. Their strongest
interpretive result is `PROVES_TOO_MUCH`: the same success on arithmetically
irrelevant actions prevents arithmetic promotion of the collapsed analytic
objects.

## 11. Typed Route-A ledger

The final Stage-11 serialization consists of exactly seven Route-A YAMLs and
zero Route-B YAMLs:

| Candidate | SHA-256 | `(A0,A1,A2,A3,A4)` | Overall |
|---|---|---|---|
| `DEN-EF-ACTUAL-GLOB-QC-CONV-P` | `ce52ba0fddf39652a37992ff7babeb590bfcb5ce8853ee6aa87b2c877634e551` | `(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-EF-GLOB-QC-ABSTRACT-CCR` | `775fb3ac86771744d3f15f708a73fc634992f770a8d7b3d04f570563054a6ccd` | `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` | `ROUTE_A_REJECTED` |
| `DEN-EF-GLOB-FULL-TRANSPORT-R` | `fb1f8bf736099a2eca5175d818ad7a00f7f1de2d0ddb699135e035ab311d8830` | `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` | `ROUTE_A_REJECTED` |
| `DEN-EF-GLOB-RED-REGULAR-R` | `45887d091bb97853febaf0329e7035655e69ec44c49ee7919ce55a8ef3de24b5` | `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` | `ROUTE_A_REJECTED` |
| `DEN-EF-ACTUAL-HOPEN-DIAGNOSTIC-P` | `25908c995d5a1f2a6f8478d62715e7cf4fc653b76ae2f6bf9fdfe71f8cc3c6d7` | `(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-EF-ACTUAL-STD-TEST-MAP-P` | `e904f85d078e84188f6d40a07e3e1fb1c7426068b8c4a9c4a773df221fd2cfac` | `(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `INDISC-R-ACTION-GLOB-CONV-CONTROL` | `23480710707367d9f77b4896a7c85e073b17dcc5a4f8aae3814bff972d27ba1b` | `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` | `ROUTE_A_REJECTED` |

The test-map row's `A0_WEAK_ARITHMETIC_RELATION` has evidence status
`MODELING_CHOICE`; the actual and HOpen weak relations are direct host
relations and still receive no analytic-arithmetic credit. All seven rows
have `A1_FAIL / REFUTED`, `A2_FAIL`, `A3_FAIL`, and `A4_FAIL`; every A2--A4
failure is `NOT_TESTABLE` because the same owner has no determinant, global
analytic object, or natural lift. Every row has
`route_b_invocation_allowed: false`.

The concrete global algebra, raw diagnostic, and strict test-map records are
valuable exact negative structural priors, hence `ROUTE_A_EXPLORATORY`. The
abstract algebra, transported completions, and generic control have already
erased the source action and are `ROUTE_A_REJECTED`. No coordinate may be
spliced across these owners to simulate a positive Route result.

## 12. Same-object certificate `T0`--`T7`

| Gate | Exact binding | Integrated status |
|---|---|---|
| `T0` identity | fixed `p,a`, exact `X_{p,a}`, right action, and range-first groupoid | `BOUND` |
| `T1` topology | actual `X_indisc x R` and proxy `S_std x R` remain distinct | `VERIFIED_DISTINCT` |
| `T2` map | `J`, `J^{-1}`, and contravariant `I` have the proved directions | `VERIFIED` |
| `T3` function convention | global QC, raw HOpen, and standard-proxy `C_c` are never conflated | `VERIFIED` |
| `T4` fibre measure | exact range fibres and Lebesgue pushforwards; source measure is inversion-pushed | `VERIFIED_TEST_LEVEL` |
| `T5` algebra/completion | dense operations proved; `I` completion extension withheld | `DENSE_LEVEL_ONLY` |
| `T6` aggregation | arithmetic application is one fixed orbit for every `p,a`; no packet/global promotion | `FIXED_ORBIT_ONLY` |
| `T7` arithmetic promotion | analytic objects erase `p,a,L_p`, action, orbit decomposition, and stabilizer | `NO_ANALYTIC_SURVIVAL_BASIS` |

## 13. Correction and terminology-conservation matrix

| Risk found during design/review | Frozen correction | Final verification |
|---|---|---|
| conflating function conventions | separate `C_qc^glob`, raw `C_c^HOp`, and standard-proxy `C_c` | `P11-3`, `P11-6`, `P11-7`; peer `PASS` |
| using ambiguous compact support on a non-Hausdorff owner | use open-cover quasi-compactness and ambient support closure | `P11-1`, `P11-3`; support controls |
| claiming all continuous/measurable maps collapse without target hypotheses | require `T0` or countably separated targets and keep negative controls | `P11-2`; factorization controls |
| importing a standard Haar system or regular representation | name `GLOB-FIBRE-FAMILY` and `Ind_x`, then prove their contracts directly | `P11-4`, `P11-5`; peer `PASS` |
| losing the source/range or inversion sign | freeze `lambda_x=(inversion)_*lambda^x`, `vartheta_x`, and the range-first formulas | direct kernel proof; five intentional negatives |
| treating the set chart as a homeomorphism | prove `J` noncontinuous and `J^{-1}` continuous | `P11-7`; proxy controls |
| extending the proxy map without a norm theorem | stop `I` at test functions | completion stop and Route ceiling |
| importing proxy tensor/Morita results into the actual owner | keep BHM/Green/MRW/BGR/Williams results proxy-only at exact strengths | Phase-2 audit and owner matrix |
| calling HOpen zero a standard algebra | label it raw and `DIAGNOSTIC_ONLY` | `P11-6` and Route record |
| calling transported completions actual groupoid C*-algebras | retain `C^full_glob` and `C^red_glob` | `P11-5`, Route ledger |
| attributing full/reduced equality to the actual groupoid | assign equality to amenability of group `R` after transport | Williams locator ledger and direct norm proof |
| deriving arithmetic specificity from the host label | prove the generic theorem first and apply it separately to rational-Witt fixed orbits | `P11-8`; action/label/period controls |
| promoting finite controls to universal proofs | label controls as witnesses only | manifest and independent review |
| overstating novelty | use only `SUPPORTED_WITHIN_SEARCH` for the exact package | Phase-2 novelty gate |
| opening Route B from a bounded convolution representation | require same-owner A4 evidence; none exists | seven `A4_FAIL`; Route-B count zero |

The final independent reviewer found no new correction requirement:
`PASS — C0/M0/m0`.

## 14. Standalone and manuscript handoff matrix

| Gate | Evidence | Status after this audit |
|---|---|---|
| design lock | final Phase-1 gate and repaired owner dictionary | `PASS` |
| source/applicability | five-source manifest, owner audit, exact source strengths | `PASS` |
| bounded novelty search | exact-package search through 2026-08-15 | `SUPPORTED_WITHIN_SEARCH` |
| direct mathematics | `P11-1`--`P11-8` proofs | `PASS` |
| deterministic controls | final manifest and independent reproduction | `PASS` |
| independent Phase-3 review | C0/M0/m0 | `PASS` |
| typed Route | seven Route-A, zero Route-B | `PASS_NEGATIVE/SCOPED` |
| integrated proof audit | this report | `PASS` |
| manuscript composition | separate `notes/composition_blueprint.md` handoff | `READY_NEXT` |
| manuscript, citation, editorial peer, and release gates | not performed by this report | `PENDING` |

The mathematical/search/controls/Route legs needed to draft a standalone
technical paper are closed. Final standalone release is not granted here. A
later manuscript, citation, peer, or release failure may still route the work
to a technical note or merge.

## 15. Manuscript-safe claim boundary

The strongest permitted central claim is:

> On each actual inherited-indiscrete rational-Witt fixed-orbit
> transformation groupoid, the author-defined globally continuous,
> open-cover-quasi-compact-support convolution `*`-algebra is canonically
> `C_c(R)`, whereas the raw Hausdorff-open span is zero; the standard-circle
> proxy contains the actual algebra only as a proper unit-coordinate-constant
> test-function subalgebra, and the generic theorem and controls show that the
> resulting algebra, unit-regular family, and transported completions are
> action- and arithmetic-blind.

The manuscript may state the bounded search result only as:

> As of 2026-08-15, the documented bounded Phase-2 search located no
> precedent for the exact rational-Witt actual-orbit convention-split
> package.

It may not say `first`, `only`, `unprecedented`, or claim novelty for the
generic topology/convolution ingredients.

## 16. Explicitly forbidden conclusions

This audit does not license any of the following:

- a standard groupoid C*-algebra or standard Haar system on `G_act`;
- the notation `C^*(G_act)` or `C_r^*(G_act)` for the author completions;
- interpreting `C_c^HOp={0}` as more than a raw diagnostic;
- a norm-bounded, isometric, dense, or completion extension of `I`;
- actual/proxy Morita equivalence, stable isomorphism, or tensor
  classification;
- arithmetic credit inherited from the concrete host after the analytic
  object has erased the action, period, and stabilizer;
- a determinant, target-zero fit, functional equation, explicit formula,
  Weil compression, quantization, Hilbert--Pólya operator, or Route-B entry;
- a packet, prime-coproduct, full-suspension, or global arithmetic theorem;
- a universal claim that no other non-Hausdorff convolution theory can
  exist; or
- an absolute novelty or priority claim.

## 17. Integrity statement

All universal mathematical conclusions in this audit are owned by the two
direct proof reports and were independently reviewed. The controls were used
only as exact witnesses, convention checks, and adversarial
`PROVES_TOO_MUCH` tests. The Route records bind the independent review hash
and preserve owner separation. No source PDF, manuscript, Route YAML, source
note, or control implementation was modified in producing this audit.

This report is therefore the stable proof/ownership handoff for manuscript
composition, not itself a release decision.
