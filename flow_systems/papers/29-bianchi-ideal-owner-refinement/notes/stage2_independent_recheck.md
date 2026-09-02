# P29 Stage-2 Independent Recheck

Review seat: `R10-S2-RB`  
Review mode: independent, repository-local, closed-corpus, post-patch recheck  
Review date: 2026-09-02 UTC  
Final verdict: **PASS**

This seat did not participate in drafting P29. The review was read-only with
respect to the manuscript, bibliography, key map, and frozen research
artifacts. Two Minor findings were reported to the main agent; the main agent
applied narrow patches, and this seat then repeated the mechanical, build, and
PDF-surface checks. This file is the only P29 file created by this seat.

## Reviewed byte surfaces

| Surface | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `5bee689a055f99819fb6df1f6e992610fe0dea7ebffc87219758116bf06bd034` |
| `paper/references.bib` | `433638db4cd984ab195beb7643a0581b1a9a9dc0b5df46f54634bd704194c253` |
| `notes/stage2_bib_key_map.json` | `6def983dfbee83dff1fa3493add4946c669c57eb65a9885a3d1c6f6d013ff772` |
| `notes/stage2_claim_intent_manifest.json` | `019cd9197ac90260bd04dd48ee2fc6c1b4c5fb1bc69a3825a98a0e377bcf1474` |
| `notes/stage2_argument_blueprint.md` | `2c262ad39a563b3b83a1ff137030206d1fff129dc35282b7186bb8eec5b2959c` |
| `notes/stage2_paper_outline.md` | `14b819865bba74a0cf454c4424bbad0eaa1d7a10ac501fb8b41d5370fdd9c05b` |
| `notes/stage1_phase2_source_inventory.tsv` | `67ed7713bd6881d11466dc16755c7660a458c52e07ee072d086d6467f8ad7bd8` |
| `notes/stage1_phase2_source_verification.md` | `81b50e0b6b834da414d8dc4bb60a47380255a26954d613393a7d817301a506e8` |
| `notes/stage1_phase6_final_report.md` | `4000ff4875993aaa0ba3520f9a56599b5703e77f32dd9675ca4552ae3252deaa` |

The controlling batch writing contract recomputed to
`cd79c1508ada0acc02fa0413592e9772b8edad04d84a859a5642f010bac8fd08`;
the Stage-2 input freeze recomputed to
`923339d65d4fd073483d01d54cdf8eb4e1e0e540d944dae7aaf1198db9f2212c`.
Line anchors below refer to the reviewed manuscript SHA above.

## Frozen object, clock, owner, and output

| Item | Reviewed manuscript surface | Result |
|---|---|---|
| System | Unit-speed geodesic flow on the fixed torsion-free level-(3) Gaussian Bianchi manifold, line 45 | PASS |
| Clock | Hyperbolic arclength, line 45 | PASS |
| Owner | Primitive loxodromic conjugacy class; inversion gives the primary unoriented owner, line 45 | PASS |
| Repetitions | Powers remain repetitions rather than new owners, line 45 | PASS |
| Strict output | One literal nonzero Gaussian prime ideal in `Z[i]`; associates identify the same ideal while conjugate split-prime ideals remain distinct, lines 45--47 | PASS |
| Stress-test status | The literal codomain is deliberately strict, not canonical, Galois-stable, or literature-forced; alternative codomains cannot be substituted after outcome access, lines 59 and 163 | PASS |
| Gate status | Gate M and Gate Q are separate non-entailing design obligations and both remain open, lines 185--215 and 275 | PASS |
| Performance firewall | `S_H(M)` is only a prospective estimand; no value is reported and the final state is undefined rather than zero, lines 205, 215, 255, and 275 | PASS |

## Stage-2 ClaimIntent coverage: 8/8

| Claim | Manuscript anchor | Negative-constraint check | Verdict |
|---|---|---|---|
| C-001 | Frozen Literature, lines 65--111; Finding 1, line 221 | Object identity and vocabulary are not promoted to an owner map, quotient, or finite-refinement score. | PASS |
| C-002 | Quotient-completeness synthesis, lines 113--143; Gate Q, lines 191--207; Finding 2, line 223 | Adjacent algorithms are described as components only; no executed or complete quotient solver is claimed. | PASS |
| C-003 | Frozen definitions and strict-frame discussion, lines 45--61 and 145--163; Gate M, lines 185--189; Finding 3, line 225 | Codomain is neither canonical nor forced; no norm, rational prime, composite ideal, residue, or conjugate pair replaces the frozen literal ideal. Any obstruction is candidate- and frame-conditional. | PASS |
| C-004 | Two-gate distinction, line 49; Gate M/Q and performance firewall, lines 185--217; Finding 4, line 227 | Neither gate is closed. Collision performance cannot select or repair either interface, and no `S_H` value is reported. | PASS |
| C-005 | Contribution boundary, line 51; architecture and findings, lines 183--227; conclusion, lines 269--275 | Contribution is a fail-closed certificate-methods design, not a theorem, novelty determination, executed mechanism, or scientific result. | PASS |
| C-006 | Prospective certificate graph, lines 197--207; reproducibility interface, lines 229--235 | Serializers, positive/negative certificates, immutable registration, controls, and replay receipts are wholly prospective; no implementation or receipt exists. | PASS |
| C-007 | Correction/preprint source surfaces, lines 91--101; executed method, lines 165--181; limitations, lines 247--255 | P29-S06 remains correction-bound to P29-S07; P29-S09 remains a preprint; every anchor is `none`; retraction and source-COI limitations remain open. | PASS |
| C-008 | Conclusion and route ledger, lines 269--275 | No formal Route-A tuple, positive arithmetic A2, Route-B invocation, formal-claim refresh, novelty result, or scientific-result refresh is implied. | PASS |

All six manifest-level negative constraints also close: only P29-S01--S22 are
used; no retrieval, direct quotation, mechanism, quotient, computation,
certificate, or novelty assessment was introduced; the frozen
system/clock/owner/repetition/codomain remains unchanged; all passage statuses
remain inconclusive; scientific and Route surfaces remain frozen; and the AI
disclosure carries the required provider/model-family/date/build/accountability
limits.

## Closed-corpus and citation-marker audit

The five frozen Round-10 source inventories recompute to
`22 + 26 + 22 + 26 + 20 = 116` distinct admitted source identifiers. This
check is a count over the frozen inventories, not a claim that cross-paper
bibliographic works were semantically deduplicated. P29 closes exactly:

- inventory IDs: 22/22;
- BibTeX keys: 22 unique entries, exactly P29-S01--P29-S22;
- cited IDs: 22/22, with no orphan and no out-of-inventory key;
- key map: declared inventory SHA matches, and every mapping is identity;
- optional citation locators: 0;
- direct quotations: 0.

Every source-bearing sentence has an exact provenance comment immediately
before its citation:

| Source | Comment / citation lines | Marker audit |
|---|---:|---|
| P29-S01 | 68 / 69 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S02 | 72 / 73 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S03 | 76 / 77 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S08 | 80 / 81 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S04 | 84 / 85 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S05 | 88 / 89 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S06 | 92 / 93 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S07 | 96 / 97 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S09 | 100 / 101 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S17 | 104 / 105 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S18 | 108 / 109 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S10 | 116 / 117 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S11 | 120 / 121 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S15 | 124 / 125 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S16 | 128 / 129 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S12 | 132 / 133 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S13 | 136 / 137 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S14 | 140 / 141 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S19 | 148 / 149 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S20 | 152 / 153 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S21 | 156 / 157 | exact; `anchor=none`; `INCONCLUSIVE` |
| P29-S22 | 160 / 161 | exact; `anchor=none`; `INCONCLUSIVE` |

Special source boundaries are preserved. P29-S06/S07 remain a mandatory
correction pair, not a retraction clearance. P29-S09 remains a first-party
preprint and is not promoted to peer-reviewed support. The frozen P29-S11
“Some/Strong” display conflict and P29-S13 page-range discrepancy remain in the
verification ledger; the bibliography retains the frozen `Some` title and
287--305 range, and no stronger claim depends on the alternative displays.
Retraction status remains `NOT_CHECKED`, and source-level COI remains
`UNKNOWN_NOT_AUDITED`.

## Abstracts, anatomy, declarations, and disclosure

| Check | Result |
|---|---|
| English body | 4,596 words by `detex`, from Introduction through the line before Author Contributions; within the 4,500 target's ten-percent band and the batch 4,000--6,500 range |
| English abstract | 194 words; bounded, self-contained, and contains no result or Route upgrade |
| Traditional-Chinese abstract | 349 Han characters; separately composed and within 300--500 |
| Keywords | 6 English and 6 Traditional-Chinese |
| Required anatomy | Title/author block, exact question and contribution boundary, frozen setting, literature, executed closed-corpus method, certificate architecture, findings, reproducibility, adversarial boundary, Route interpretation, limitations, future work, conclusion, and bibliography are present |
| Author/contact | Liang Wang; complete HUST school/address and `wangliang.f@gmail.com` |
| Declarations | Narrow CRediT-style roles, funding none, competing interests none, ethics not applicable, and data/materials boundary are present |
| AI disclosure | OpenAI Codex; GPT-5 model family; 2026-09-02 UTC; exact backend build unavailable; actual assistance and non-authorship stated; Liang Wang is accountable; no human full-text/passage verification is implied |

## Isolated build and PDF text-surface audit

The post-patch build used a new `/tmp` directory and the required chain:
`LuaLaTeX -> BibTeX -> LuaLaTeX -> LuaLaTeX`. Input hashes were recomputed
before and after the build and did not change.

| Build surface | Result |
|---|---|
| Return code | 0 |
| Effective warnings | 0 undefined citations/references, missing characters, overfull/underfull boxes, or LaTeX/package warnings |
| Temporary PDF | 13 pages; 265,174 bytes |
| Temporary PDF SHA-256 | `f93717354fd30b04e248b7c9455ca7856ab02f020b9280658b3e3534a3d8d230` |
| Text surface | `pdftotext -layout` exposes title, author/address/email, both abstracts, Gate M/Q, stress-test language, no-`S_H` boundary, declarations, AI limitation, and all 22 references |
| Post-patch reference surface | P29-S20 renders as “H. W. Lenstra, Jr.” |

The PDF was a temporary isolation build and was not copied into the repository;
its SHA records this observed build, not a canonical deterministic-PDF claim.

## Findings by severity

### Blocker

None.

### Major

None.

### Minor

1. **R10-S2-RB-P29-MINOR-01 — RESOLVED POST-PATCH.** The initial BibTeX
   author grammar for P29-S20 rendered the suffix as “Jr. Lenstra, H. W.” The
   main agent changed only the BibTeX name grammar from
   `Lenstra, H. W., Jr.` to `Lenstra, Jr., H. W.`; the frozen author
   identity was not changed. The final bibliography SHA and PDF surface above
   verify the correction.
2. **R10-S2-RB-P29-MINOR-02 — RESOLVED POST-PATCH.** The initial generic
   contribution list included unsupported `Software`, `Validation`,
   `Data curation`, and `Visualization` roles. The main agent narrowed the
   declaration to frozen, evidence-backed CRediT-style roles and the exact
   accountability narrative. Post-patch source and PDF checks pass.

There is no unresolved Minor finding.

### Observation

1. `criteria_binding_unavailable` remains appropriate: no journal or track
   was author-confirmed, so this recheck makes no venue-fit claim.
2. The machine-audit provenance comments are nonprinting; their integrity was
   checked from TeX, while their absence from PDF is expected.

## Limitations of this recheck

- No network retrieval, source replacement, novelty search, retraction query,
  or Stage-2.5 passage adjudication was performed.
- The recheck verifies citation/key/source-role closure, not theorem truth or
  exact claim-to-passage support; all such support remains
  `INCONCLUSIVE`.
- PDF inspection combined the build log and extracted text surface. It was not
  a journal-specific typography or raster-by-raster accessibility audit.
- The 116-source check recomputed the frozen batch inventories; this seat did
  not independently peer-review P31--P33 prose.
- No scientific implementation was replayed because P29 correctly reports that
  none exists.

## Gate conclusion

All eight Stage-2 ClaimIntents and all negative constraints are covered without
claim-strength drift. The two reported Minor findings are repaired and
post-patch verified. There is no unresolved Blocker or Major finding; therefore
the Stage-2 independent-recheck verdict is **PASS**.

```text
REVIEW_SEAT=R10-S2-RB
CLAIM_COVERAGE=8/8
UNRESOLVED_BLOCKER=0
UNRESOLVED_MAJOR=0
FINAL_VERDICT=PASS
STAGE2_5_STATE=STAGE2_5_NOT_STARTED
```
