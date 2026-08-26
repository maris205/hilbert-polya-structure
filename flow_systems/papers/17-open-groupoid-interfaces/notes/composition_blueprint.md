# Paper 17 Technical Note composition blueprint

Blueprint date: **2026-08-16 (Asia/Shanghai)**  
Blueprint status: **FINAL PLANNING RECORD — NOT A MANUSCRIPT**  
Publication ceiling: **Technical Note candidate only**  
Standalone status: **`STANDALONE_PASS=false`**

## 1. One-way authority binding and scope

This blueprint was created only after the proof audit froze at zero findings.
It binds the proof audit in the downstream direction; the proof audit does not
depend on this file and does not embed or predict this file's hash.

| Bound authority | Final SHA-256 | Blueprint use |
|---|---|---|
| `notes/proof_audit.md` | `c6810e95d15e1ccf0f1dd48045b0f890ebd98fe637c20a9a5e153e10fa1c4934` | zero-finding proof/owner/domain/control/max-prior/Route claim firewall |
| `notes/phase2_integrated_gate.md` | `3d1b732bf02a6b2f73b9515a0531fdb77d7960d379c22393079c9e3d200c53c0` | exact seven-owner integrated authority |
| `notes/route_audit.md` | `d70ba9d029ae598863e44dbb049c49607063f682de8f7d8a8e5f2074ae531d15` | final four-exploratory/three-rejected and Route-B stop |
| `GEN-INDISC-R-ACTION-TOPOS-QF-CONTROL` Stage-17 YAML | `77db1521f1d7cdc9e030e1c26148472e4fe4a772bc4a7c90c27dcabc26822672` | generic `R` control disposition |
| `GEN-INDISC-Z-ACTION-TOPOS-CONTROL` Stage-17 YAML | `47c04d015036dcefc95f315bd862996cd3653885b09584d27ee7e07c1492848e` | disconnected-time falsifier disposition |
| `DEN-EF-ORBIT-ACTION-GRPD` Stage-17 YAML | `6ea677a679197d053520de03bade7fb3fcba89c6b10aa9eb8a97955883f7ae9d` | actual-orbit exploratory ceiling |
| `DEN-EF-PACKET-ACTION-GRPD-P` Stage-17 YAML | `d3469e7cf52ed9e84ed3a5f79fcf5ca593a6e60e7bdab8a43b47398c24c5cb91` | actual-packet exploratory ceiling |
| `DEN-EF-ORBIT-STD-CIRCLE-PROXY` Stage-17 YAML | `163dc6153aafc66bb3209ea51cf8199c32d997e921bcac6707f328aacb4de673` | standard-proxy exploratory ceiling |
| `DEN-EF-ORBIT-STD-CIRCLE-COMPARISON-P` Stage-17 YAML | `b191133dfb4a892b78800dac2b435c0ec58e80cc1ced745cdea08112d7bca727` | cross-owner comparison exploratory ceiling |
| `UNMARKED-PERIOD-SCALING-CONTROL` Stage-17 YAML | `d1de29ee6708c7846b6f03198fbd9335edfd3c6683928201772513681de58e14` | unmarked control rejection ceiling |

This record plans a future Technical Note. It is not prose for submission,
not a bibliography, not a citation audit, and not authorization to create a
manuscript, figure, table, BibTeX file, build output, release artifact, Git
change, or public record. The working title, section labels, word budgets,
claim IDs, and artifact IDs below are planning metadata only.

## 2. Editorial center and argument contract

### 2.1 Planning-only working title

`Topos and open-quantal-frame interfaces of globally indiscrete action
groupoids: owner-sensitive computations and obstructions`

The eventual title must signal an interface/obstruction Technical Note. It
must not mention a determinant, spectrum, trace, Haar system, `C*`-algebra,
priority, or Route B.

### 2.2 Central thesis

The future note should argue one tightly delimited thesis: exact owner and
domain typing yields parallel, direct classifying-topos and bare
open-quantal-frame computations for globally indiscrete action groupoids;
the same typing exposes where actual and standard owners differ and why the
unmarked interface cannot recover numerical period or support an analytic,
determinant, spectral, or Route-B promotion.

### 2.3 Argument sequence

1. Freeze the range-first convention, nonempty globally indiscrete owner,
   and the distinction between a bare quantale and localic reconstruction.
2. Prove the generic topos and bare-quantale results independently; specialize
   to usual `R` and retain discrete `Z` as the mandatory falsifier.
3. Register `q_H` and local compactness before making any localic claim.
4. Compare the actual inherited owner with the separately imposed standard
   circle without transporting topology, provenance, or coordinates.
5. Use unequal-period dilation to show what the unmarked interfaces cannot
   recover; describe strict time only as extra marker structure.
6. Apply the generic result to the fixed-prime actual orbit and packet only
   after the theorem, with the Paper-9/10/11 firewall visible.
7. Report finite controls at their diagnostic/serialization ceiling.
8. Close with the exact seven-owner Route table and negative limitations:
   four exploratory, three rejected, all A2--A4 fail, Route B false.

The future note must make the negative result explanatory rather than
apologetic: the contribution is the exact interface calculation plus the
sharp owner/premise/scale obstructions, not an incomplete determinant model.

## 3. Target length, page budget, and fixed order

Recommended submission scale: **4,200--4,800 English-equivalent words**, not
including references, and **12--15 typeset pages including references and
declarations**. The hard ceiling is 5,200 words or 16 pages; exceeding either
requires a new editorial decision because it risks disguising the frozen
Technical-Note ceiling as a full paper.

| Future component | Target size | Required purpose |
|---|---:|---|
| English abstract | 160--190 words | eight-fact structured narrative without headings |
| Chinese abstract | 220--300 Chinese characters | independently composed, same eight facts/order/omissions |
| Keywords | 4--6 terms in each language | owner, action groupoid, classifying topos, open quantal frame, localic boundary |
| 1. Introduction and scope | 350--450 words | question, contribution, Technical-Note and negative-result framing |
| 2. Conventions and admissible domains | 400--500 words | range-first convention, owners, `q_H`, local compactness |
| 3. Generic joint interface | 700--850 words | open/non-etale groupoid, topos, quantale, base, `R`/`Z` split |
| 4. Localic gate and actual/standard firewall | 600--750 words | premise separation, point-loss location, exact owner comparison |
| 5. Scale obstruction and fixed-prime application | 550--700 words | unmarked dilation, strict marker, P9--P11 provenance firewall |
| 6. Finite diagnostic controls | 300--450 words | exact receipt and non-proof ceiling |
| 7. Route outcome and limitations | 550--700 words | Route table, 4/3 disposition, all A2--A4 fail, no Route B |
| 8. Conclusion | 180--250 words | restate exact contribution and stops without speculation |
| Declarations | 180--300 words | mandatory availability, ethics, authorship, funding, conflict, AI statements |

Fixed document order:

```text
title and author metadata
English abstract + English keywords
Chinese abstract + Chinese keywords
1 Introduction and scope
2 Conventions and admissible domains
3 Generic joint interface
4 Localic gate and actual/standard firewall
5 Scale obstruction and fixed-prime application
6 Finite diagnostic controls
7 Route outcome and limitations
8 Conclusion
Declarations
References
```

The Stage-17 Route table is mandatory in Section 7 and must appear before the
References. No appendix may move the owner, control, or limitation firewalls
out of the main reading path.

## 4. Section/claim/evidence/locator matrix

Internal notes and YAMLs are drafting evidence, not substitutes for
publication citations. “Future source citation” below means that the final
manuscript must cite a verified primary source or exact local owner source at
the indicated claim, with a nonempty locator.

| Claim ID | Future section and claim | Frozen evidence | Exact drafting locator | Future source-citation action |
|---|---|---|---|---|
| TN-00 | Front matter: this is a Technical Note about interface calculations and obstructions; `STANDALONE_PASS=false`. | proof audit; post-Route disposition | `proof_audit.md` Sections 1 and 10; `route_audit.md` lines 1--7 and 187--211 | no literature citation can convert editorial status into Route credit |
| TN-01 | §2: freeze the range-first action-groupoid convention and exact groupoid operations. | symbolic proof + P11 owner formulas | `phase2_topos_quantale_proofs.md` equations (2.1)--(2.2), lines 55--91; P11 manuscript lines 255--277 | preflight and cite the local P11 source at exact lines; do not cite a proxy convention |
| TN-02 | §3: `G(X,H)` is open; usual-`R` specialization is non-etale. | symbolic proof + independent re-derivation | proof Propositions 3.1--3.3, lines 93--155; peer review 3.1, lines 86--103 | verify Forssell Section 2.1 definition/locator for open groupoids; distinguish definition citation from Paper-17 proof |
| TN-03 | §3: `B(G(X,H)) ~= B_cont(H)` for a nonempty globally indiscrete right `H`-set. | symbolic proof + peer review | proof Lemma 4.1 and Theorem 4.2, equations (4.1)--(4.6), lines 157--244; peer review 3.2--3.3, lines 105--147 | cite Moerdijk/Forssell only for the framework; present the equivalence as the note's direct proof |
| TN-04 | §3: connected usual `R` gives `Set`; discrete `Z` gives nontrivial `BZ`. | symbolic proof + mandatory falsifier | proof Corollaries 4.3--4.4, lines 246--273; Route R17-02 YAML | cite framework source as needed; keep `Z` as falsifier, not finite-C3 theorem evidence |
| TN-05 | §3: bare arrow-open quantale `O(H)`, base `2`, and usual-`R` nonunitality. | symbolic proof + primary framework definitions | proof Theorem 5.1 and Propositions 5.2--5.3, lines 275--340; peer review 3.5, lines 161--178 | verify Protin--Resende pp. 203--205 and Theorem 2.41; direct computation remains the note's proof |
| TN-06 | §4: bare `O(H)`, `q_H`, and local compactness are separate; reconstruction only follows on their conjunction. | domain amendment + proof + peer review | `phase1_amendment_v2.md` Sections 1--2; proof Proposition 6.1 and Theorem 6.2, lines 342--386; peer review 3.6, lines 180--200 | verify Protin--Resende Theorems 2.41/2.45 and printed pp. 245--246 from the source PDF before citation |
| TN-07 | §4: nonsober point loss is at `Top -> Loc`, not failure of localic reconstruction. | proof + peer review | proof Corollary 6.3, lines 388--403; peer review 3.6, lines 180--200 | cite Protin--Resende only for its actual theorem/domain; label the loss-location conclusion as this note's typed inference |
| TN-08 | §4: actual `Set/O(R)/2` differs from standard `BZ/O(S_L x R)/O(S_L)`; owners remain separate. | symbolic proof + owner controls | proof Theorem 7.1, Proposition 7.2, and Section 8, lines 405--506; peer review 3.7 and S3; `actual_standard_owner_controls.csv` | cite local P11 standard-owner lines 313--324; no topology or coordinate transport |
| TN-09 | §5: unequal-period simultaneous dilation preserves unmarked plain interfaces; strict time is extra marker structure. | symbolic proof + controls | proof Propositions 9.1--9.2, lines 508--556; peer review 3.8; `dilation_strict_marker_controls.csv` | the propositions carry the claim; controls are corroboration only; do not cite a control row as theorem proof |
| TN-10 | §5: fixed-prime actual orbit/packet application occurs only after the generic theorem and imports only actual indiscreteness and literal `(log p)Z`. | symbolic proof + local Paper-9 owner source | proof Section 10, lines 558--592; P9 manuscript lines 409--426; `fixed_prime_provenance_controls.csv` | cite exact P9 locator for inherited facts; state Paper-17 contribution separately |
| TN-11 | §5: Paper 10 and Paper 11 subtraction prevents relabeling prior collapses/formulas as new topos results. | proof owner firewall | proof Section 10 table, lines 593--613; framework precheck Sections 2.1 and 7 | preflight exact P10/P11 local locators before any visible citation; use explicit “builds on” wording |
| TN-12 | §6: final finite package is 9 CSVs/3,436 rows/84 negatives/3,352 nonnegative rows/48+42 mutations/180 tests/2 fresh/3 copies/zero residue. | final controls review + manifest | `phase2_controls_review.md` closure Sections B--I, lines 575--909; `manifest.json` lines 1--170 | no external citation required for the receipt; identify it as project diagnostic evidence, not mathematical proof |
| TN-13 | §7: seven-owner Route result is four exploratory and three rejected; all seven fail A2, A3, A4; Route B false. | formal Route audit + seven YAMLs | `route_audit.md` lines 106--211; each bound Stage-17 YAML `a2`--`a4`, `overall_verdict`, and final Boolean | report the exact enums and counts; no interpretive promotion or owner aggregation |
| TN-14 | §7/§8: no `C*`, Haar, measure, trace, determinant, divisor, Weil compression, natural quantization, or standard-to-actual transfer is constructed. | proof, proof audit, Route audit/YAMLs | proof lines 558--641; `proof_audit.md` Sections 5, 8, and 9; `route_audit.md` lines 118--130 and 148--211 | retain explicit negative wording; absence is a limitation/claim boundary, not evidence of impossibility in every enrichment |

No claim may enter the future note without a row in this matrix or a later
versioned extension reviewed at `C0/M0/m0`. Claims TN-03 and TN-05 are parallel
direct computations; neither may be inferred from an etale-only
sheaf/quantale bridge.

## 5. Owner and domain firewall for drafting

Every theorem, table row, figure node, abstract sentence, and conclusion
sentence must carry one of the following owner tokens in the drafting ledger.

| Owner token | Owner and domain | Allowed output | Nontransferable fields |
|---|---|---|---|
| `GENERIC_R_ACTUAL` | nonempty globally indiscrete right-`R` owner, usual nondiscrete `R` | `Set/O(R)/2`, non-etale/nonunital, conditional localic reconstruction | arithmetic labels, stabilizers, numerical period, standard topology, marked structure |
| `GENERIC_Z_FALSIFIER` | nonempty globally indiscrete right-`Z` owner, discrete locally compact `Z` | `BZ`; falsifies disconnected extension of the `Set` conclusion | connected-`R` result, finite-C3 theorem credit, arithmetic interpretation |
| `ACTUAL_ORBIT_P` | one Paper-9 actual fixed-prime inherited orbit | source A0 plus `Set/O(R)/2` after generic substitution | standard topology, numerical `log p` recovery, phase/multiplicity/amplitude, analytic/operator credit |
| `ACTUAL_PACKET_P` | actual `Gamma_p` and restricted right-`R` action | source A0 plus `Set/O(R)/2` after generic substitution | packet aggregation, orbit decomposition recovery, transverse mass, analytic/operator credit |
| `STANDARD_CIRCLE_PROXY` | separately imposed `S_L=R/(LZ)` with standard topology/translation | `BZ/O(S_L x R)/O(S_L)`, abstract integer isotropy | actual topology/A0, strict-marker credit, numerical `L` from unmarked outputs |
| `ACTUAL_STANDARD_COMPARISON` | typed comparison record with two owners preserved | exact five-field asymmetry | conversion, coordinate union, topology/Haar/completion transport |
| `UNMARKED_SCALING_CONTROL` | generic positive-period simultaneous-dilation family | unmarked isomorphism and scale nonrecovery | strict marker, arithmetic selection, determinant or operator credit |

Drafting rule: a sentence containing facts from two owner tokens must use an
explicit comparison connective (“whereas,” “separately,” or “in the typed
comparison”) and must not use an equals sign or a transfer verb between them.
Any unlabelled owner, proxy-to-actual import, marked-to-unmarked import, or
coordinate union is a release-stopping defect.

## 6. Controls-reporting contract

Section 6 should use one compact receipt paragraph plus future Table T3. It
must preserve both the historical failure and the effective closure:

- the original authorized run exited 10 with six failures P025--P030 and was
  never retried; that tuple remains downstream-invalid;
- the versioned remediation repaired only the root-specific isolated-child
  environment/test orchestration, kept all nine CSV bytes unchanged, and
  authorized one replacement run;
- the replacement exited 0 with 180 tests, zero failures/errors, 84/84
  intended negatives, two fresh generations, three-way byte identity, and
  zero frozen residue; and
- the final independent append-only controls review is `PASS C0/M0/m0` for
  the replacement tuple without relabeling the historical run.

Required ceiling sentence, in substance: the controls are deterministic
diagnostic, firewall, mutation-isolation, and serialization receipts; they do
not prove connectedness, the topos/quantale calculations, local compactness,
`q_H`, reconstruction, non-etaleness, numerical scale, priority, novelty, or
any Route coordinate.

Forbidden controls framing includes “validated the theorem computationally,”
“numerically confirmed reconstruction,” “simulation evidence for the
determinant,” or any omission of the historical first-run failure.

## 7. Limitations and negative-result framing

Section 7 must state each limitation as an owner-specific boundary and place
the exact Route table before the References.

1. **Action blindness:** the generic actual interface is unchanged for
   trivial, periodic, and nontransitive actions and therefore does not select
   arithmetic dynamics.
2. **Connectedness:** the `Set` collapse uses connected usual `R`; `BZ` is the
   explicit disconnected-time falsifier.
3. **Localic premise boundary:** a bare quantale is not alone a reconstruction
   theorem; `q_H` and local compactness remain explicit.
4. **Owner asymmetry:** actual and standard outputs are both exact but belong
   to different topology/provenance owners.
5. **Scale nonrecovery:** unmarked plain outputs do not recover numerical
   `L`; strict time is additional structure.
6. **Fixed-prime ceiling:** direct source A0 survives only on the actual
   orbit/packet owners; the evaluated interface erases the data needed for A1.
7. **Analytic/operator absence:** every owner has A2/A3/A4 failure and no
   determinant object, completed divisor, Weil compression, or natural
   quantization.
8. **Editorial ceiling:** four exploratory records are not positive analytic
   results; the note remains non-standalone and Route B remains closed.

Negative claims must be scoped to the evaluated plain owner/interface.
“This interface does not construct/recover X” is authorized; “no enrichment
can ever construct/recover X” is not.

## 8. English/Chinese abstract factual symmetry ledger

The two future abstracts must be composed independently, not by literal
translation, while preserving the same eight facts in the same order. Every
hedge and negative boundary is protected content.

| Order | Fact ID | Required fact in both abstracts | Protected qualification |
|---:|---|---|---|
| 1 | AB-F1 | identify a concise owner-sensitive Technical Note on two parallel point-free interfaces | do not claim standalone/full-paper status |
| 2 | AB-F2 | state the generic topos equivalence and bare quantale/base computation | nonempty globally indiscrete owner; direct parallel computations |
| 3 | AB-F3 | state usual-`R` `Set` and discrete-`Z` `BZ` contrast | connectedness cannot be omitted |
| 4 | AB-F4 | separate bare `O(H)`, `q_H`, and local compactness; locate loss at `Top -> Loc` | do not call reconstruction a failure |
| 5 | AB-F5 | contrast actual `Set/O(R)/2` with separately imposed standard `BZ/O(S_L x R)/O(S_L)` | no owner or topology transfer |
| 6 | AB-F6 | state unmarked numerical-scale nonrecovery and strict marking as extra structure | no claim that plain outputs recover `log p` |
| 7 | AB-F7 | characterize controls as exact diagnostics and serialization receipts | do not imply computational theorem proof |
| 8 | AB-F8 | report four exploratory/three rejected, all A2--A4 fail, no determinant/Route B | preserve the Technical-Note ceiling |

### Same-omission ledger

Both abstracts must omit all of the following; if one language later receives
an editorially necessary mention, the other must be amended in the same
position and re-audited:

```text
no author names or priority claims
no DOI or reference list
no code/test implementation details beyond the diagnostic ceiling
no first-run remediation narrative
no C*-algebra, Haar-system, measure, trace, or representation claim
no determinant, divisor, zero-fit, Weil-compression, or operator claim
no standard-to-actual or marked-to-unmarked transfer
no future-work promise implying Route-B entitlement
```

Symmetry checks before manuscript freeze:

```text
FACT_ORDER_MATCH=8_OF_8
FACT_OMISSION_MATCH=PASS
NUMBER_MATCH=PASS
OWNER_TOKEN_MATCH=PASS
HEDGE_MATCH=PASS
ROUTE_COUNT_MATCH=4_EXPLORATORY_3_REJECTED
A2_A3_A4_STATUS_MATCH=ALL_FAIL
```

## 9. Planned publication artifacts and strict six-key trace registry

At most two figures may be proposed, and both must be code-native vector
artifacts (SVG/PDF generated from reviewable source). Raster generation,
AI-created bitmap art, decorative imagery, and screenshots are prohibited.
Figures are optional: if the relation is clearer in T1/T2, omit the figure.

Exactly four future tables are planned:

- T1: owner/domain/joint-interface firewall;
- T2: theorem-premise-evidence separation;
- T3: finite-control and historical/replacement receipt;
- T4: seven-owner Stage-17 Route disposition, placed in Section 7 before
  References.

No fifth table or third figure may enter without a versioned blueprint
amendment. Every future table and figure must have all six trace keys below;
omission of any key is a hard failure, and an empty `limitations` value is at
least an advisory requiring correction. The planning tables in this blueprint
are ledgers, not publication artifacts; T1--T4 and F1--F2 identify only the
future manuscript artifacts.

### T1 trace plan

```yaml
artifact_id: T1_OWNER_DOMAIN_INTERFACE_FIREWALL
source_data: "proof_audit.md sha256:c6810e95d15e1ccf0f1dd48045b0f890ebd98fe637c20a9a5e153e10fa1c4934 Sections 4-5; phase2_topos_quantale_proofs.md sha256:f6c7475b854b3d00b37d3e7f2edca8e8f2f15d92d67ae8bbcdcd71be127b3bb1 Sections 3-10"
transformation: "deterministic manual extraction of the seven frozen owner tokens and their allowed outputs/exclusions; row-by-row independent comparison to blueprint Section 5 required"
caption_claim: "The actual, standard, comparison, and control owners have distinct topology, provenance, and nontransferable interface fields."
supported_manuscript_claims: [TN-02, TN-04, TN-08, TN-10, TN-14]
limitations: "A typing summary only; it neither proves the source theorems nor licenses any field transfer between rows."
```

### T2 trace plan

```yaml
artifact_id: T2_THEOREM_PREMISE_EVIDENCE_SEPARATION
source_data: "phase1_amendment_v2.md sha256:2ce675880b171ee598f8a796edf55f9c695e2e6d0973620371d3ba460c7d1957; phase2_topos_quantale_proofs.md sha256:f6c7475b854b3d00b37d3e7f2edca8e8f2f15d92d67ae8bbcdcd71be127b3bb1 Sections 4-6; phase2_topos_quantale_peer_review.md sha256:9ad4817e32c6da461d7e15eee1bd53d24368b7c55751738c86c8b033caeb796e Sections 3.2-3.6"
transformation: "map each conclusion to direct proof, necessary owner/domain premise, primary-source framework locator, and nonproof diagnostic; no cross-column inference"
caption_claim: "The topos calculation, bare quantale calculation, q_H comparison, and localic reconstruction have different premises and evidence roles."
supported_manuscript_claims: [TN-03, TN-05, TN-06, TN-07]
limitations: "The table is not a substitute for proofs or source citations and does not extend the locally compact reconstruction domain."
```

### T3 trace plan

```yaml
artifact_id: T3_FINITE_CONTROL_RECEIPT
source_data: "phase2_controls_review.md sha256:a9acf3c1e6c043b408cce774af3adfdf4a72fdb2f58cf38fbc8bf94f6dc324a1 Sections 7-13 and closure B-I; manifest.json sha256:a15cc81ca8e41b7fd76560304bf713701f416a028558b9d9c5653b58f7ebc254"
transformation: "transcribe the historical and replacement tuples separately; independently recompute only displayed arithmetic 3436-84=3352 and 48+42=90 at future table freeze"
caption_claim: "The replacement package is deterministic and mutation-audited while the historical failed run remains visible and downstream-invalid."
supported_manuscript_claims: [TN-12]
limitations: "Finite diagnostics and serialization evidence only; no mathematical theorem, novelty, numerical-scale, determinant, or Route coordinate is proved."
```

### T4 trace plan

```yaml
artifact_id: T4_STAGE17_ROUTE_DISPOSITION
source_data: "route_audit.md sha256:d70ba9d029ae598863e44dbb049c49607063f682de8f7d8a8e5f2074ae531d15 lines 106-211 plus the seven Stage-17 YAML hashes bound in blueprint Section 1"
transformation: "one row per frozen owner in R17-01 through R17-07 order; copy exact A0-A4 enums and overall_verdict; mechanically verify counts 4 exploratory/3 rejected and zero A2-A4 positives"
caption_claim: "Four owners remain exploratory, three are rejected, every owner fails A2-A4, and Route B is closed."
supported_manuscript_claims: [TN-13, TN-14]
limitations: "Route classification is owner-specific and cannot be aggregated; exploratory does not mean analytic, determinant, spectral, or publication success."
```

### F1 trace plan — recommended only if it reduces textual complexity

```yaml
artifact_id: F1_OWNER_INTERFACE_FIREWALL
source_data: "T1 frozen data plus proof_audit.md sha256:c6810e95d15e1ccf0f1dd48045b0f890ebd98fe637c20a9a5e153e10fa1c4934 Section 5"
transformation: "planned code-native SVG/PDF graph with separate actual, standard, comparison, and control lanes; generator source path and its final SHA-256 are REQUIRED_AT_ARTIFACT_FREEZE; only labelled arrows allowed, and every forbidden transfer is drawn as a stop, never as an edge"
caption_claim: "Topology and provenance determine distinct joint interfaces; comparison does not convert actual and standard owners."
supported_manuscript_claims: [TN-08, TN-10, TN-14]
limitations: "Conceptual dependency diagram only; geometry, distance, color, and arrow placement encode no magnitude, probability, or theorem strength."
```

### F2 trace plan — optional and lower priority than F1

```yaml
artifact_id: F2_EVIDENCE_TO_ROUTE_CEILING
source_data: "phase2_integrated_gate.md sha256:3d1b732bf02a6b2f73b9515a0531fdb77d7960d379c22393079c9e3d200c53c0 Sections 3-9; route_audit.md sha256:d70ba9d029ae598863e44dbb049c49607063f682de8f7d8a8e5f2074ae531d15 Sections 2-5; seven bound Stage-17 YAMLs"
transformation: "planned code-native SVG/PDF flow from symbolic proof through diagnostic controls to owner-specific Route ceilings; generator source path and final SHA-256 are REQUIRED_AT_ARTIFACT_FREEZE; no coordinate aggregation or visual promotion"
caption_claim: "Symbolic proof, finite controls, and Route adjudication are distinct evidence layers, ending with all owners at A2-A4 failure."
supported_manuscript_claims: [TN-12, TN-13, TN-14]
limitations: "A provenance flow, not a causal model or quantitative score; publication status contributes no Route coordinate."
```

Artifact release rules:

```text
MAX_FIGURES=2
FIGURE_FORMAT=CODE_NATIVE_VECTOR_ONLY
PLANNED_TABLES=4
SIX_TRACE_KEYS_REQUIRED=true
TRACE_KEYS=artifact_id,source_data,transformation,caption_claim,supported_manuscript_claims,limitations
MISSING_TRACE_KEY=HARD_FAIL
EMPTY_LIMITATIONS=ADVISORY_REQUIRING_CORRECTION
UPDATED_ARTIFACT_WITH_STALE_TRACE=HARD_FAIL
UNREGISTERED_TABLE_OR_FIGURE=HARD_FAIL
```

## 10. Source and citation preflight

No bibliography is created by this blueprint. Before drafting any visible
citation, the future composition lane must build a source registry and pass
the following preflight.

### 10.1 Minimum primary-source registry

| Planned source slug | Claim role | Locator that must be verified against source bytes |
|---|---|---|
| `moerdijk-1988-classifying-topos` | foundational continuous-groupoid classifying-topos framework | DOI `10.1090/S0002-9947-1988-0973173-9`; exact theorem/definition page must be checked before use |
| `forssell-2013-subgroupoids` | open topological groupoid, equivariant sheaf, Moerdijk site | Section 2.1, journal pp. 542--543 / arXiv physical pp. 2--3; Proposition 2.1.1 and following paragraph |
| `protin-resende-2012-quantales` | `O(G)` definitions, open quantal frames, localic reconstruction, pullback/frame warning | DOI `10.4171/JNCG/90`; printed pp. 203--205, Theorems 2.41 and 2.45 at pp. 214--215, and pp. 245--246 |
| `paper9-actual-owner` | actual packet/orbit indiscreteness and literal stabilizer only | local manuscript lines 409--426; final source hash must be frozen before citation |
| `paper11-range-first-owner` | range-first formulas, standard-circle owner, arrow-open/composable-pair facts, open sheaf owner | local manuscript lines 255--277, 313--324, 337--405, 1079--1087; final source hash must be frozen before citation |

Resende's etale-only quantale-sheaf/module sources may be cited only to mark
their etale scope; they cannot license a Paper-17 topos/quantale equivalence
on the non-etale owner.

### 10.2 Per-citation hard checks

For every future citation:

1. source bytes exist and are readable; title, author, venue, year, DOI/URL,
   and edition/version metadata agree across primary records;
2. the cited page, theorem, proposition, equation, or section has been opened
   and directly supports the adjacent claim;
3. the locator is nonempty and specific—no `none`, search-result page,
   abstract-only stand-in, or unchecked secondary paraphrase;
4. a visible citation is paired in the drafting source with a stable source
   slug and exact anchor, e.g. `<!--ref:slug--><!--anchor:...-->`, or the
   format-equivalent registry keys required by the chosen journal template;
5. quotation, if unavoidable, remains within the applicable source limit and
   is checked character-for-character; paraphrase is preferred;
6. one citation is not made to support both a framework definition and a new
   Paper-17 theorem unless its role is explicitly split;
7. every in-text citation has one reference entry and every reference entry is
   cited—zero orphans in either direction; and
8. DOI resolution, metadata match, locator existence, claim alignment, and
   reference-format checks all pass before manuscript freeze.

No citation may be invented from memory. A missing source, inaccessible
locator, DOI conflict, unsupported claim, placeholder, or unverified local
manuscript hash is a hard stop. Source preflight must occur before bibliography
generation, and the later claim/reference alignment audit must report 100%
claim coverage for the claims it marks as citation-requiring.

## 11. Declarations plan

The future note must include complete, journal-shaped declarations before the
References. Exact author/institution facts must come from the authors; the
composition lane may not infer them.

| Declaration | Planned content boundary | Stop condition |
|---|---|---|
| Data and materials availability | identify the exact symbolic ledgers and finite control package; distinguish existing project artifacts from newly collected data | do not claim public availability until a stable public repository/identifier is verified |
| Code availability | identify the deterministic control generator/test/reproduction package only if release is separately authorized | no repository URL, license, or archival DOI may be guessed |
| Ethics approval | state whether human participants, animals, personal data, or intervention were involved; expected scope is none, but author confirmation is required | missing author confirmation stops release |
| Consent | state not applicable only after the ethics scope is confirmed | do not auto-fill from topic alone |
| Competing interests | author-supplied disclosure | placeholder or inferred “none” stops release |
| Funding | exact funder and grant metadata, or author-confirmed no specific funding | no fabricated grant or inferred no-funding statement |
| Author contributions | CRediT roles mapped to verified author list | no role may be assigned without author confirmation |
| Acknowledgements | only verified contributors/permissions | no invented names or permissions |
| AI-use disclosure | describe the actual assistance used for planning/drafting/checking under journal policy; authors retain verification responsibility | omission or inaccurate scope stops release |
| Limitations | retain the owner/domain/control/Route ceilings from Sections 5--7 | limitations cannot be weakened at formatting stage |

## 12. Composition, integrity, formatting, and release stops

### 12.1 Manuscript-entry gate

Before any manuscript file is created, all of the following must be true:

```text
PROOF_AUDIT_HASH_MATCH=true
INTEGRATED_GATE_HASH_MATCH=true
ROUTE_AUDIT_HASH_MATCH=true
SEVEN_YAML_HASH_MATCH=7_OF_7
CLAIM_MATRIX_FROZEN=true
OWNER_FIREWALL_FROZEN=true
SOURCE_REGISTRY_PREFLIGHT=PASS
MANUSCRIPT_AUTHORIZATION_FROM_NEW_GATE=true
```

This blueprint itself supplies no manuscript authorization.

### 12.2 Draft freeze checks

The future drafting/review lane must independently verify:

- every theorem statement matches its owner, topology, hypotheses, and proof
  locator;
- all TN-00--TN-14 claims are present or explicitly marked omitted, with no
  new unregistered claim;
- English and Chinese abstracts pass the eight-fact order and same-omission
  ledgers;
- historical and replacement control tuples remain separate, with diagnostic
  ceiling visible;
- T4 precedes References and has exactly seven rows in frozen order;
- every future table/figure has the six-key trace record and an exact current
  source/generator hash;
- visible citations, source slugs, anchors, and reference entries have no
  missing or orphan elements;
- declarations are complete and author-verified; and
- `STANDALONE_PASS=false`, four exploratory/three rejected, all A2--A4 fail,
  and Route-B false are unchanged in abstract, main text, tables, captions,
  conclusion, and metadata.

### 12.3 Formatter and visual QA stops

After a separately authorized build, formatting review must stop on any
missing section, unresolved citation/reference, equation-number drift,
cross-reference error, overfull/clipped object, illegible vector label,
table overflow, empty page, font substitution affecting symbols, or mismatch
between source and PDF. Visual figure verification must compare each rendered
vector to its trace `caption_claim` and `limitations`; a semantically correct
source with a misleading rendering still fails.

### 12.4 Absolute release stops

Release is prohibited if any of the following occurs:

```text
UPSTREAM_HASH_DRIFT
NONZERO_CRITICAL_MAJOR_OR_MINOR_FINDING
OWNER_OR_DOMAIN_SPLICE
BARE_QUANTALE_PROMOTED_WITHOUT_Q_H_AND_LOCAL_COMPACTNESS
STANDARD_TO_ACTUAL_TRANSFER
MARKED_TO_UNMARKED_TRANSFER
CONTROLS_REPORTED_AS_THEOREM_PROOF
ROUTE_COORDINATE_AGGREGATION
EXPLORATORY_RELABELED_AS_ANALYTIC_SUCCESS
ANY_A2_A3_A4_VALUE_NOT_FAIL
ANY_DETERMINANT_OBJECT_INTRODUCED_WITHOUT_NEW_OWNER_AND_GATE
ROUTE_B_IMPLIED_OR_INVOKED
UNVERIFIED_SOURCE_OR_LOCATOR
MISSING_OR_ORPHAN_CITATION
BILINGUAL_FACT_ORDER_OR_OMISSION_MISMATCH
MISSING_OR_STALE_SIX_KEY_ARTIFACT_TRACE
INCOMPLETE_OR_UNVERIFIED_DECLARATION
FORMAT_OR_RENDERING_DEFECT
STANDALONE_OR_FULL_PAPER_PROMOTION
MISSING_INDEPENDENT_INTEGRITY_AND_CLAIM_REFERENCE_AUDITS
MISSING_EXPLICIT_RELEASE_AUTHORIZATION
```

No later formatter, abstract writer, citation processor, figure generator, or
editor may widen the mathematical claim surface. Any requested widening must
return to a new versioned proof/owner/domain/Route gate before composition.

## 13. Final planning receipt

```text
P17_COMPOSITION_BLUEPRINT=FINAL
DOCUMENT_TYPE_PLANNED=TECHNICAL_NOTE
THIS_FILE_IS_MANUSCRIPT=false
STANDALONE_PASS=false
BOUND_PROOF_AUDIT_SHA256=c6810e95d15e1ccf0f1dd48045b0f890ebd98fe637c20a9a5e153e10fa1c4934
BOUND_INTEGRATED_GATE_SHA256=3d1b732bf02a6b2f73b9515a0531fdb77d7960d379c22393079c9e3d200c53c0
BOUND_ROUTE_AUDIT_SHA256=d70ba9d029ae598863e44dbb049c49607063f682de8f7d8a8e5f2074ae531d15
BOUND_STAGE17_YAMLS=7
SECTION_CLAIM_LOCATOR_MATRIX=FROZEN_TN00_TO_TN14
OWNER_FIREWALL=FROZEN_SEVEN_TOKENS
ROUTE_TABLE_BEFORE_REFERENCES=true
BILINGUAL_FACT_ORDER_LEDGER=EIGHT_FACTS
BILINGUAL_SAME_OMISSION_REQUIRED=true
TARGET_WORDS=4200_TO_4800
TARGET_PAGES=12_TO_15
MAX_CODE_NATIVE_VECTOR_FIGURES=2
PLANNED_TABLES=4
STRICT_SIX_KEY_TRACE_REQUIRED_FOR_ALL_FIGURES_AND_TABLES=true
SOURCE_CITATION_PREFLIGHT_REQUIRED=true
DECLARATIONS_REQUIRED=true
MANUSCRIPT_AUTHORIZED=false
BIBLIOGRAPHY_AUTHORIZED=false
CITATION_AUDIT_AUTHORIZED=false
FIGURE_ARTIFACT_AUTHORIZED=false
BUILD_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
COMPOSITION_BLUEPRINT_SHA256=EXTERNAL_BY_CONSTRUCTION
```
