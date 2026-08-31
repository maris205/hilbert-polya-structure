# Paper 27 — Stage 4.5 Round 2 reference and citation-context audit

Audit date: **2026-08-31**

Audit target: `notes/stage4_prime_revision_round1.tex` (`803d9e7d69c233363d912b4fee25f5915b7f07d48937b794ee11c807ca182ef7`)

Fresh reference coverage: **5/5 (100%)**. Citation-context coverage: **5/5 (100%)**.

Each reference has an A0 fresh Semantic Scholar title/identifier check, an A1/A2 fresh WebSearch top-results trail, authoritative DOI/arXiv/LMFDB resolution, and a named-source correction/retraction/expression-of-concern update observation. S2_NOT_FOUND or API unavailability is explicitly downgraded to DOI/official WebSearch; it is not treated as fabrication. No DOI/title mismatch was detected.

| reference | A0 Semantic Scholar | actual method | title score | A1/A2 WebSearch | update observation |
|---|---|---|---:|---|---|
| `martinez2016` | S2_API_UNAVAILABLE | null | null | TOP_RESULTS_RECORDED (5 top results) | NONE_OBSERVED_FOR_THIS_NAMED_SOURCE |
| `penner2008` | S2_VERIFIED | `s2_doi_lookup` | 1.000 | TOP_RESULTS_RECORDED (5 top results) | NONE_OBSERVED_FOR_THIS_NAMED_SOURCE |
| `alcalde2026` | S2_VERIFIED | `s2_doi_lookup` | 1.000 | TOP_RESULTS_RECORDED (5 top results) | NONE_OBSERVED_FOR_THIS_NAMED_SOURCE |
| `hurder2019` | S2_VERIFIED | `s2_doi_lookup` | 1.000 | TOP_RESULTS_RECORDED (5 top results) | NONE_OBSERVED_FOR_THIS_NAMED_SOURCE |
| `nica2013` | S2_VERIFIED | `s2_title_search` | 1.000 | TOP_RESULTS_RECORDED (5 top results) | NONE_OBSERVED_FOR_THIS_NAMED_SOURCE |

The update check is a current named-source observation, not a guarantee across every publisher or post-publication venue. The audit confirms bibliographic identity and the bounded role assigned in the manuscript; it does not convert ingredient/antecedent citations into ownership, priority, determinant, or global-census claims.

| line | citation keys | verdict | bounded context |
|---:|---|---|---|
| 136 | `martinez2016` | VERIFIED | % Source locator: arXiv:0711.2307v4, pp. 2--3 Section 2.2; p. 12 Example 4; pp. 15--16 Example 6. |
| 142 | `penner2008` | VERIFIED | % Source locator: Introduction pp. 1--2; Section 2, Definition 2.1 and following discussion. |
| 148 | `alcalde2026` | VERIFIED | % Source locator: arXiv:2411.18418v2, p. 7 Definition 4; p. 8 Definition 5; pp. 12--14 Definition 7 and tower setup. |
| 154 | `hurder2019` | VERIFIED | % Source locator: arXiv:1702.03032, p. 17, Definition 5.5 and following paragraph. |
| 157 | `nica2013` | VERIFIED | % Source locator: arXiv:1306.2385v1, p. 1, displayed Malcev theorem and following definition. |

Verdict: **PASS** — no citation-context distortion or bibliography identity failure detected by this recorded full audit.
