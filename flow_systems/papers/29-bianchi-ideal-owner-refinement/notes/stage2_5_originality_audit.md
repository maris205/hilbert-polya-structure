# Paper 29 Stage 2.5 Phase D originality audit

Audit completed: 2026-09-03 UTC  
Mode: ARS-Codex Phase D, deterministic quoted-fragment sample plus exact local and same-author screens  
Frozen manuscript SHA-256: `5bee689a055f99819fb6df1f6e992610fe0dea7ebffc87219758116bf06bd034`  
Frozen pre-WebSearch sample SHA-256: `21d6b12fb47938c7d71965902eb284c782d7b381b4a0fcb88c95181aa15c1264`  
Completed WebSearch sample SHA-256: `019f856229ea541d6ddbb93c9185b5fdc60d1d7b5285a0207d25c65d2892ee41`  
Round-10 originality precommitment SHA-256: `01f7ffb11ad935cb08a2a1017e0599a32647e4b5bfdaabeae7359733a7d49f44`  
Round-9 author-corpus audit SHA-256: `fa434a4e75c9fbc706a0b672495e90617ded0fe648b6e649a64b14d47a887f7d`

## Determination

**PASS WITH LIMITATIONS for this bounded Phase D originality screen.** All 23/75 deterministically frozen scientific-body paragraphs (30.67%) were submitted as unchanged exact quoted normalized fragments. All 23 are graded `ORIGINAL`: no reviewed result reproduced a full fragment, and no exact or contextually authoritative matching URL existed. Broad-token results were inspected and excluded as nonmatches. This determination is Phase-D-specific and is not an overall Stage 2.5 or manuscript-acceptance verdict.

The 4,495-word normalized scientific body was compared at the exact eight-word threshold against every other local `papers/*/paper/manuscript.tex` file (25 sources). The only threshold-positive records are controlled workflow/provenance or Route-status taxonomy. **Substantive prose reuse at or above eight words: 0.** A separate declaration scan found standardized administrative boilerplate and is reported below rather than silently mixed into scientific prose.

The Round-9 Liang Wang corpus was also rechecked from current official record files: 22/22 Zenodo PDFs and 2/2 official arXiv PDFs were retrieved and text-extracted. The maximum exact run was four words, with 0/24 at or above eight words. Exact-title and email-plus-title WebSearch returned no public surface.

Numbered-section coverage (10/10): Introduction 3; Frozen literature 7; Executed methodology 1; Proof/method architecture 3; Evidence synthesis 2; Reproducibility 1; Discussion 1; Limitations 2; Future work 1; Conclusion 2.

## D1 — frozen quoted-fragment WebSearch (23/75)

Method: every stored normalized fragment was wrapped in ASCII quotation marks and submitted unchanged to OpenAI WebSearch. `none` means no exact full-fragment or contextually authoritative match was returned; unrelated keyword-level hits are not plagiarism evidence.

| Sample | TeX line / major section | Exact query | Top exact or authoritative URL | Search result | Grade |
|---|---|---|---|---|---|
| `29-D1-001` | L45; introduction research question and contribution boundary | `"unit-speed geodesic flow on a torsion-free level- gaussian bianchi manifold hyperbolic arclength"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-002` | L57; introduction research question and contribution boundary | `"classification prevents several common but consequential substitutions a well-defined ideal factorization algorithm"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-003` | L61; introduction research question and contribution boundary | `"which interface lacks evidence without granting conclusions about other mechanisms broader codomains"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-004` | L67; frozen literature and theoretical frame | `"picard manifold supplies direct context for the quotient associated with psl z"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-005` | L79; frozen literature and theoretical frame | `"conjugacy-class language including inversion-aware or unoriented formulations in a nearby arithmetic hyperbolic"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-006` | L87; frozen literature and theoretical frame | `"hyperbolic-three-manifold explicit-formula work similarly broadens the analytic setting without supplying"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-007` | L107; frozen literature and theoretical frame | `"picard actions and imaginary-quadratic arithmetic are likewise part of the structural setting"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-008` | L111; frozen literature and theoretical frame | `"taken together these records support the registered distinction between knowing the object"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-009` | L131; frozen literature and theoretical frame | `"no-transfer rule an algorithm for groups of oriented geometrizable three-manifolds has differently"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-010` | L155; frozen literature and theoretical frame | `"practical computational number-theory interfaces clarify what an implementation would need to serialize"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-011` | L167; executed methodology frozen evidence synthesis only | `"screening seventeen admitted records were counted within the workflow's peer-reviewed journal-or-correction numerator"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-012` | L187; review-adjudicated proof and method architecture | `"by immutable formula bytes source trace admissible domain exact codomain normalization treatment"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-013` | L199; review-adjudicated proof and method architecture | `"exclusion code rather than being silently discarded the ledger would also bind"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-014` | L217; review-adjudicated proof and method architecture | `"relabeling invariance test not arithmetic specificity replacing literal primes with composite objects"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-015` | L221; evidence-synthesis findings | `"picard bianchi geodesic object and supplies primitive inversion group-algorithm and ideal-arithmetic vocabulary"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-016` | L225; evidence-synthesis findings | `"galois orbit or another equivariant output might avoid that problem but considering"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-017` | L231; reproducibility and prospective implementation interface | `"screening counts row-level source status correction relation claim-use boundaries and review findings"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-018` | L239; discussion and implications | `"intrinsic data to select a non-galois-stable branch yet failure would primarily speak"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-019` | L249; acknowledged limitations | `"standalone reproducibility supplement existing upstream inventories and matrices improve traceability but do"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-020` | L253; acknowledged limitations | `"requires them those elements support machine audit while leaving final passage adjudication"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-021` | L263; future work | `"few premises closest to an owner formula group-root decision and literal split-branch"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-022` | L271; conclusion | `"makes the construct boundary explicit the literal gaussian-prime-ideal codomain is deliberately strict"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |
| `29-D1-023` | L273; conclusion | `"computation novelty finding or route advance the formal route-a tuple remains unassigned"` | none | `NO_EXACT_PUBLIC_WEB_MATCH` | `ORIGINAL` |

Result totals: **23 ORIGINAL; 0 COMMON_KNOWLEDGE; 0 PARAPHRASE; 0 CLOSE_MATCH; 0 VERBATIM; 0 SEARCH_ACCESS_LIMITATION**.

## D2a — exhaustive local exact-run comparison

The frozen precommitment comparison uses the project tokenizer (casefolded alphabetic words, hyphenated forms retained) over each scientific body. A supplementary paragraph-preserving guard scan casefolded alphanumeric tokens, did not bridge paragraph boundaries, compared this target body to every complete source manuscript, and human-adjudicated every exact eight-word candidate. The two tokenizations explain the reported 18-versus-22-word P29–P30 maximum; both point to the same workflow inventory, not scientific prose.

| Comparison surface | Maximum exact run | Representative candidate at 8+ words | Human classification |
|---|---:|---|---|
| 21 prior manuscripts (P1–P28) | 5 | none | `NO_OVERLAP_AT_THRESHOLD` |
| P30 | 18; 22 under the supplementary alphanumeric tokenizer | phase/source-effect artifact inventory | `CONTROLLED_WORKFLOW_BOILERPLATE` |
| P31 | 10 | the formal route-a tuple remains unassigned positive arithmetic a remains | `CONTROLLED_ROUTE_STATUS_BOILERPLATE` |
| P32 | 10 | the formal route-a tuple remains unassigned positive arithmetic a remains | `CONTROLLED_ROUTE_STATUS_BOILERPLATE` |
| P33 | 6 | none | `NO_OVERLAP_AT_THRESHOLD` |

Supplementary guard-scan total: **40 unique exact eight-word window values and 12 maximal paragraph-pair records across three source files (P30, P31, P32)**. The longest P29–P30 record is the 22-token artifact-list fragment `the phase 3 source effect matrix and synthesis the phase 4 report and claim manifest all four phase 5 role reviews the`. Other candidates concern the executed literature workflow, source/provenance artifacts, retained citation comments, or the explicit Route-A status sentence. None is a theorem, proof step, datum, experiment result, domain-specific interpretation, or distinctive scientific exposition.

## Declaration boilerplate separated from scientific prose

The full-file guard scan separately compared the declaration region (Author Contributions through the last declaration before the bibliography). For this target, 213 unique shared exact eight-word windows formed 16 maximal comparison records across five source manuscripts. The principal runs were: AI-assistance disclosure, 66 words; verification-limitation disclosure, 60; author-contribution statement, 58; ethics statement, 39; data/materials availability prefix, 18; stage-gate confirmation wording, 11.

These passages are visibly segregated administrative/declaration templates—funding, conflicts, ethics, CRediT-style contribution roles, data availability, and AI-assistance disclosure. They are excluded from the scientific-body originality denominator and classified as **standardized administrative boilerplate**, not substantive scientific reuse. This classification does not imply that a target journal will accept the wording unchanged.

## D2b — Liang Wang public-corpus and title screen

Identity scope follows the Round-9 audit: Liang Wang; `wangliang.f@gmail.com`; HUST; ORCID `0000-0001-9006-6924`. The 22 official Zenodo records enumerated there were individually re-opened, their current PDF files retrieved, and their full extracted text compared to this scientific body; the two older official arXiv PDFs were handled identically. Normalization was casefolded alphabetic exact-token comparison.

Exact-title query: `"A Fail-Closed Certificate Architecture for Literal Gaussian-Prime-Ideal Ownership in a Level-(3) Bianchi Flow"` → no result.  
Email-plus-title query: `"wangliang.f@gmail.com" "Fail-Closed Certificate Architecture"` → no result.

| Public record | Public title | Maximum exact run | 8+ word result |
|---|---|---:|---|
| [21720147](https://zenodo.org/records/21720147) | Boundary-Aligned Ulam Approximation and Grid Leakage in a Cyclic Postcritically Finite Quadratic Map | 4 | none |
| [21712436](https://zenodo.org/records/21712436) | Periodic-Orbit Collapse in B-Admissible Shifts: Exact Prime-Wheel Zeta Functions and Infinite Coprime Limits | 4 | none |
| [20711935](https://zenodo.org/records/20711935) | A Sequential Birkhoff Theorem for Slow Logarithmic Drift in Non-Uniformly Expanding Unimodal Maps | 4 | none |
| [20565112](https://zenodo.org/records/20565112) | The Emergence of Prime Distribution from Low-Dimensional Deterministic Chaos | 4 | none |
| [20463341](https://zenodo.org/records/20463341) | Transient Chaos and Topological Bounds in Prime Dynamics | 4 | none |
| [19995437](https://zenodo.org/records/19995437) | Unitarity Enables Grokking | 3 | none |
| [19682685](https://zenodo.org/records/19682685) | Differentiable Discrete Symplectic Cosmology | 4 | none |
| [19677694](https://zenodo.org/records/19677694) | Spectral Analysis of the Transfer Operator in the Period-3 Logistic Sandbox | 4 | none |
| [19657875](https://zenodo.org/records/19657875) | An Empirical Logarithmic Relation Between Gravitational and Electromagnetic Coupling Constants | 3 | none |
| [19455383](https://zenodo.org/records/19455383) | Physical Emergence of Riemann Zeros in Dissipative Chaotic Circuits | 3 | none |
| [19429778](https://zenodo.org/records/19429778) | Discrete Symplectic Cosmology | 4 | none |
| [19218674](https://zenodo.org/records/19218674) | Cosmological Evolution as a Non-autonomous Dynamical System | 3 | none |
| [19135531](https://zenodo.org/records/19135531) | Ab Initio Quantum Emulation of the Riemann Zeros | 3 | none |
| [19084735](https://zenodo.org/records/19084735) | The Physical Topology of Riemann Zeros | 4 | none |
| [19045440](https://zenodo.org/records/19045440) | Spectral Isomorphism between Renormalization Flow in Non-Autonomous Quadratic Maps and Riemann Zeros | 4 | none |
| [18596290](https://zenodo.org/records/18596290) | The Riemann Standard Model | 4 | none |
| [18535934](https://zenodo.org/records/18535934) | Riemann Zero Truncation in Physical Systems | 3 | none |
| [18493585](https://zenodo.org/records/18493585) | The Relaxation of Cosmic Expansion | 4 | none |
| [18459475](https://zenodo.org/records/18459475) | Cosmological Evolution as a Non-autonomous Chaotic System | 4 | none |
| [17926196](https://zenodo.org/records/17926196) | OpenSciEval | 3 | none |
| [17926116](https://zenodo.org/records/17926116) | OpenSciEval Scientific Creativity Evaluation Guide | 3 | none |
| [17832139](https://zenodo.org/records/17832139) | Humanity's Final Conjecture | 3 | none |
| [arXiv:1306.3626](https://arxiv.org/abs/1306.3626) | Describe Prime number gaps pattern by Logistic mapping | 3 | none |
| [arXiv:1006.4114](https://arxiv.org/abs/1006.4114) | Translate gene sequence into gene ontology terms based on statistical machine translation | 3 | none |

Public-corpus denominator: **24/24 PDFs retrieved and text-extracted**; maximum exact run: **4 words**; exact runs at or above eight words: **0**. This bounded same-author screen found no exact self-reuse signal. It is not a claim that no other Liang Wang surface exists.

## Limitations and boundary

This is a WebSearch and exact-run heuristic, **not Turnitin or iThenticate**, and not a global originality certificate. Public search can miss private, paywalled, unindexed, image-only, recently posted, differently rendered, translated, or paraphrased material. The quoted-fragment lane samples just over 30% of eligible body paragraphs, although every numbered major section is represented. The local 26-manuscript and known 24-PDF lanes are exhaustive only within their declared corpora, boundaries, and normalization. Professional similarity checking remains recommended on the final submission PDF.

No manuscript, bibliography, PDF, pipeline state, README, scientific result, experiment, or Route evaluation was changed by this audit.
