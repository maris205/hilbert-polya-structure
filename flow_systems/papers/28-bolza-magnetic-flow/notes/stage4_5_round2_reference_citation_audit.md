# Paper 28 — Stage 4.5 Round 2 reference and citation-context audit

Audit target: `notes/stage4_prime_revision_round1.tex` (`126783db66949396f7b3b494e06f55e4deedcc9f443f29e6477e6254676d472e`).

Reference existence/field/update coverage is **6/6 (100%)**; current citation-context coverage is **9/9 (100%)**; ghost references and dangling citation keys are **0**.

Every entry has a fresh Semantic Scholar Tier-0 record, a fresh WebSearch query/URL/result trail, authoritative existence and field checks, and a named-source correction/retraction/expression-of-concern observation. S2 API unavailability is downgraded to DOI/arXiv/official-source review and is not treated as fabrication. No DOI–title mismatch was found.

| key | A0 | A1/A2 | update observation | verdict |
|---|---|---|---|---|
| `Nazarenko2013` | S2_API_UNAVAILABLE (score None) | 1 reviewed result(s) | One v1 submission is displayed; no withdrawal marker is displayed. | VERIFIED |
| `Takeuchi1975` | S2_API_UNAVAILABLE (score None) | 1 reviewed result(s) | The 20 October 2006 correction changes citation-list numbering/format from unbracketed items to bracketed references; no theorem-text correction is listed. | VERIFIED_WITH_UPDATE_NOTE |
| `AigonDupuyEtAl2005` | S2_VERIFIED (score 1.0) | 2 reviewed result(s) | No correction, retraction, or expression-of-concern relation is listed in the named Crossref work object. | VERIFIED |
| `Voight2009` | S2_VERIFIED (score 1.0) | 2 reviewed result(s) | Errata correct Proposition 1.1/cycle conditions and an Algorithm 4.7 proof step; the author states the mistake does not affect the other results. | VERIFIED_WITH_UPDATE_NOTE |
| `DespreEtAl2023` | S2_API_UNAVAILABLE (score None) | 1 reviewed result(s) | No named correction, retraction, or expression of concern is displayed on the official record reviewed. | VERIFIED |
| `Popescu2024` | S2_API_UNAVAILABLE (score None) | 2 reviewed result(s) | No named correction/retraction/EoC is displayed on the publisher record reviewed; arXiv displays v1 with no withdrawal marker. | VERIFIED |

Voight's author-hosted errata are retained as an explicit update note. They do not affect P28's bounded background claim that exact fundamental-domain algorithms exist; P28 does not rely on the corrected proposition or proof step. Takeuchi's official 2006 correction is a citation-list numbering/format correction and does not alter the cited theorem condition.

| block/line | source | context role | verdict |
|---|---|---|---|
| `B0014` / 148 | `Nazarenko2013` | source-locked octagon equations and family construction | VERIFIED |
| `B0014` / 154 | `AigonDupuyEtAl2005` | family-level genus-two octagon context | VERIFIED |
| `B0022` / 263 | `Nazarenko2013` | source-locked octagon equations and family construction | VERIFIED |
| `B0031` / 349 | `Popescu2024` | Lindemann-Weierstrass transcendence implication | VERIFIED |
| `B0032` / 360 | `Takeuchi1975` | arithmetic cofinite Fuchsian-group trace-field condition | VERIFIED |
| `B0035` / 383 | `Voight2009` | neighboring exact fundamental-domain algorithm context only | VERIFIED_WITH_UPDATE_NOTE |
| `B0035` / 385 | `DespreEtAl2023` | Dirichlet-domain algorithm from polygon and side-pairing input | VERIFIED |
| `B0036` / 392 | `Nazarenko2013` | source-locked octagon equations and family construction | VERIFIED |
| `B0036` / 394 | `AigonDupuyEtAl2005` | family-level genus-two octagon context | VERIFIED |

All six bibliography entries are cited; all nine citation instances support only their recorded bounded roles. No citation is used to transfer ownership of P28's finite counts, hash values, sign classifications, or systole certificate.

Verdict: **PASS with named update notes; no blocking bibliographic or citation-context issue detected.**
