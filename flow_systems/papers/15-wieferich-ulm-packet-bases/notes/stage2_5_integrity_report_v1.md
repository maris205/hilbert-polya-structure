# Paper 15 — Stage 2.5 integrity report v1

## Verdict

**PASS — zero open SERIOUS, MEDIUM, or MINOR issues.**

The pre-review integrity gate completed after one bounded correction round. Stage 3 has **not** started: the pipeline is stopped at the mandatory user checkpoint.

## Frozen verified artifact tuple

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `paper/manuscript.tex` | 47,451 | `aff441ee124f0042470dd21270626028b3fca09423a6fdd4beb924c5d5ae195f` |
| `paper/references.bib` | 4,266 | `f4f1ac49a5cd47481d54fe7bc7da7cf14dac2a75b78844d2570eefb5fed06297` |
| `paper/figures/classification_pipeline.tex` | 1,748 | `cc6d75e797c7ca4ad5893864bd74f5b57c364dfcba599f0c5a6749d56c406375` |
| `paper/claim_intent_manifest.json` | 3,658 | `08dcdd66b1ce23718111b063ba3afe3814ea85c365a699e16275d51cf4325a21` |
| `paper/paper.pdf` | 167,484 | `7d30302714e63209766e554e6fa685208789c400e791bb04bf5cf7fe6b2fbfe8` |

Ordered tuple digest: `97c93900522fa6eaa9af9c99136d891dea1f2dfbbbed8392441b030c8297ec36`.

## Gate summary

| Phase | Coverage | Final result |
|---|---:|---|
| A — reference identity and bibliography | 10/10 references | 10 VERIFIED; 0 failed |
| B — citation context | 22/22 source-context occurrences | 22 VERIFIED; 0 open issue |
| C — data/internal/figure consistency | 8/8 claim clusters; all figures/tables | CLEAR |
| D — originality | 16/51 paragraphs (31.37%); 14 other local manuscripts | CLEAR, bounded heuristic |
| E — claim verification | 8/8 claims; 14 validated evidence rows | 8 VERIFIED; 0 distortion |
| AI research failure modes | 7/7 | CLEAR |

Citation integrity score: `1.000`. Detected fabrication risk: `0.000`.

## Closed correction round

1. `Kiehlmann2013`: the article entry had mixed the arXiv title/short author form with journal metadata. It now uses the official journal title and `Jonathan A. Kiehlmann`, while explicitly retaining arXiv v3 for technical locators.
2. `Moree2005`: two occurrences of `prescribed-order` were narrowed to multiplicative-order divisibility, matching the paper's actual statement; the journal DOI was added.
3. `ConradPadicInterpolation`: the official Math 5020 Fall 2011 course provenance replaced `n.d.`.
4. Non-gating completeness: Hill's DOI was added and the Lagarias–Odlyzko URL was changed to the stable author topic bibliography.

Every correction was followed by source re-verification, a fresh XeLaTeX/BibTeX build, PDF text extraction, and final-log checks. No open correction remains.

## Phase A/B source findings

All ten entries resolve to the named works and support only the bounded roles assigned in the manuscript:

- Deninger: compact quotient/packet provenance, not the new classification.
- Kiehlmann: dual-reduced profinite classification, torsion sequence, and infinite-height input.
- Hill/Kulikov: cyclic decomposition of the required primary residual subgroup.
- Zsigmondy: primitive divisors, with exceptions checked in the manuscript.
- Sutherland's Dirichlet and Chebotarev notes: prime occurrence after the manuscript establishes the required congruence/Galois hypotheses.
- Lagarias–Odlyzko: historical Chebotarev source; no effective bound is claimed by this paper.
- Moree: only a nearby multiplicative-order-divisibility comparator.
- Conrad's two notes: logarithm/exponential domains, valuation identity, and the 2-adic sign split.

No ghost citation, dangling key, source mashup, or unsupported citation context remains. The machine report contains the per-source URLs and correction history.
It also persists one query, top result, and confirmed-field audit-trail row for
each of the ten references, as required by the Stage-2.5 protocol.

The ARS Tier-0 Semantic Scholar batch was attempted for all ten records. The
first request remained HTTP 429 after the protocol's three retries, so the
remaining batch was recorded as `API_UNAVAILABLE_REMAINDER`. Per the ARS
graceful-degradation rule, no positive or negative reference verdict was
inferred from that outage; all ten final verdicts rest on DOI/publisher,
institutional, author-hosted, and full-text checks.

## Phase C — internal and artifact consistency

This is a theoretical paper and declares no experiments. The two concrete arithmetic checks were recomputed:

- `2^10 - 1 = 1023 = 3 × 11 × 31`;
- `3^10 - 1 = 59048 = 8 × 11^2 × 61`.

Figure 1 is a non-data proof schematic. Tables 1 and 2 are source/owner matrices. Their captions, entries, theorem boundary, and the retained PDF agree. The current PDF has 14 A4 pages, passes the ARS PDF preflight and Ghostscript null-page parse, embeds 7/7 Unicode-mapped font subsets, and has zero final LaTeX warnings, undefined citations/references, over/underfull boxes, missing glyphs, or duplicate labels. Pages 1, 11, and 14 were visually inspected after the final correction.

## Phase D — originality

The deterministic sample covered 16 of 51 eligible English research paragraphs (31.37%), including the abstract, main theorem, key proofs, Kummer–Chebotarev construction, kernel-internal roots, limitations, and conclusion. Sixteen exact 8–12-word web searches found no direct phrase match. Full continuous 20-word comparison against the other 14 repository manuscripts found zero hit.

This is bounded heuristic screening, not an iThenticate/Turnitin certificate. It may miss paywalled, unindexed, cross-language, formula-level, or external-author-corpus overlap.

## Phase E — claims

All six high-impact claims and both remaining claims were audited. The report persists 14 `evidence-row/1.0` rows spanning all 8 claim IDs; the supplied ARS validator returned PASS. No scope broadening, novelty inflation, major/minor distortion, or unverifiable claim remains.

The verified positive result remains exactly the bare compact-group classification and its local primary/Ulm structure. It does **not** establish universal recovery of the prime, actual packet topology, measure, flow, trace, operator, determinant, Route advancement, MG11 execution, or publication authority.

## Seven AI research failure modes

All seven are `CLEAR`. Modes tied to experiments/implementation are inapplicable because the paper makes no experiment or implementation-result claim; this is recorded explicitly rather than silently skipped. Citation hallucination was fully checked. Shortcut/frame-lock risks are controlled by the owner firewall, limitations section, Route screens, and the explicit non-executed MG11 boundary.

## Checkpoint and authority

- Stage 2.5: `PASS`.
- Open integrity issues: `0`.
- Stage 3 simulated peer review: `NOT_STARTED`.
- Checkpoint: `AWAITING_USER_CONFIRMATION`.
- Public release, submission, Route advancement, and repository synchronization: **not authorized**.

Machine-readable companions:

- `stage2_5_integrity_report_v1.json`
- `stage2_5_material_passport_v1.json`
- `stage2_5_pipeline_state_v1.json`
