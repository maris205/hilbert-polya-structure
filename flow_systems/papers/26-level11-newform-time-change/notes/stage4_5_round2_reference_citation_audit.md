# Paper 26 — Stage 4.5 Round 2 reference and citation-context audit

Audit date: **2026-08-31**

Audit target: `notes/stage4_prime_revision_round2.tex` (`345c258b5a1097c67d4f7777167b90eee208d6b2d36b23655990269a4de42203`)

Fresh reference coverage: **7/7 (100%)**. Citation-context coverage: **8/8 (100%)**.

Each reference has an A0 fresh Semantic Scholar title/identifier check, an A1/A2 fresh WebSearch top-results trail, authoritative DOI/arXiv/LMFDB resolution, and a named-source correction/retraction/expression-of-concern update observation. S2_NOT_FOUND or API unavailability is explicitly downgraded to DOI/official WebSearch; it is not treated as fabrication. No DOI/title mismatch was detected.

| reference | A0 Semantic Scholar | actual method | title score | A1/A2 WebSearch | update observation |
|---|---|---|---:|---|---|
| `manin1972` | S2_VERIFIED | `s2_doi_lookup` | 1.000 | TOP_RESULTS_RECORDED (5 top results) | NONE_OBSERVED_FOR_THIS_NAMED_SOURCE |
| `merel1991` | S2_API_UNAVAILABLE | null | null | TOP_RESULTS_RECORDED (5 top results) | NONE_OBSERVED_FOR_THIS_NAMED_SOURCE |
| `ruelle1976` | S2_VERIFIED | `s2_doi_lookup` | 1.000 | TOP_RESULTS_RECORDED (5 top results) | NONE_OBSERVED_FOR_THIS_NAMED_SOURCE |
| `fried1986` | S2_API_UNAVAILABLE | null | null | TOP_RESULTS_RECORDED (5 top results) | NONE_OBSERVED_FOR_THIS_NAMED_SOURCE |
| `lmfdb112aa` | S2_API_UNAVAILABLE | null | null | TOP_RESULTS_RECORDED (5 top results) | NONE_OBSERVED_FOR_THIS_NAMED_DATABASE_RECORD |
| `Katok1985` | S2_VERIFIED | `s2_doi_lookup` | 1.000 | TOP_RESULTS_RECORDED (5 top results) | NONE_OBSERVED_FOR_THIS_NAMED_SOURCE |
| `ConstantinescuNordentoft2025` | S2_VERIFIED | `s2_doi_lookup` | 1.000 | TOP_RESULTS_RECORDED (5 top results) | NONE_OBSERVED_FOR_THIS_NAMED_SOURCE |

The update check is a current named-source observation, not a guarantee across every publisher or post-publication venue. The audit confirms bibliographic identity and the bounded role assigned in the manuscript; it does not convert ingredient/antecedent citations into ownership, priority, determinant, or global-census claims.

| line | citation keys | verdict | bounded context |
|---:|---|---|---|
| 110 | `lmfdb112aa` | VERIFIED | % Source locator: LMFDB orbit 11.2.a.a, Properties, q-expansion, and eta-quotient sections. |
| 119 | `manin1972` | VERIFIED | % Source locator: Manin, pp. 19--25, modular symbols and weight-two period setting. |
| 175 | `merel1991` | VERIFIED | % Source locator: Merel, Introduction and Sections 1--2, pp. 519--526. |
| 180 | `Katok1985` | VERIFIED | Katok's earlier work places closed-geodesic periods and modular-form arithmetic in direct contact . It is an antecedent for the period object, not for the present finite correspondence-component owner taxonomy or degree-moment obstruction. |
| 185 | `ruelle1976` | VERIFIED | % Source locator: Ruelle, Introduction and flow product discussion, pp. 231--242. |
| 187 | `fried1986` | VERIFIED | % Source locator: Fried, Section 2, pp. 496--502. |
| 192 | `ConstantinescuNordentoft2025` | VERIFIED | A modern nearest neighbor proves arithmetic-statistical nonvanishing results for automorphic-form periods over primitive closed geodesics . Its owners are primitive geodesics ordered in an asymptotic family; it does not turn a finite Hecke correspondence output into a canonical primitive-owner Euler product. |
| 677 | `Katok1985, ConstantinescuNordentoft2025` | VERIFIED | This finite owner-and-moment conclusion is distinct from existence or asymptotic nonvanishing results for closed-geodesic periods . The bounded nearest-work audit supports that distinction without asserting exhaustive coverage, global priority, or a complete primitive census. |

Verdict: **PASS** — no citation-context distortion or bibliography identity failure detected by this recorded full audit.
