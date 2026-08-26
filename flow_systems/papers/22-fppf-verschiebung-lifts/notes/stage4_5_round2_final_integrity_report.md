# P22 Stage 4.5 Round 2 final integrity report

Audit date: **2026-08-25 UTC**  
Mode: **Stage 4.5 / Mode 2 / full fresh recheck after exact authorized correction**  
Final verdict: **PASS**

```text
SERIOUS = 0
MEDIUM  = 0
MINOR   = 0
```

Both frozen Stage 3-prime issues are closed and freshly verified. The exact
zero-issue boundary for the Stage 5 entry checkpoint is met. Stage 5 itself is
not entered; it remains subject to explicit user confirmation and a citation
style decision.

## Exact accepted manuscript

| Artifact | SHA-256 | Status |
|---|---|---|
| `paper/manuscript.tex` | `e90dd88109d4e53d1f789808286c15cc917003cd38b69f49ddaff8661b9158ed` | accepted Stage 4.5 source |
| `paper/paper.pdf` | `20e2d14f5a9e46b7d4f5eafac6669032c72fc69367fdf902e54440816a4a3f04` | rebuilt, 13 pages |
| `paper/references.bib` | `bd03813691db911316b18620ee4a1d212ac284fce7fb79af9f1b1cbc7ea71093` | 3 entries |
| `notes/stage4_5_integrity_revision_round2.tex` | `a93b64f5ad41ede0ddaef8ad6fa46800092a9abd5d75fb099d357b54ea2058a2` | final anchored source |
| `notes/stage4_5_revision_evidence_bundle_round2.json` | `c665cee2e8c2288fb2c8e17a0e7e7e935b8062813a42d67cc8cea892ed6c10a9` | two-round replay PASS |

Deleting only whole-line block-marker comments from the anchored source yields
the public source byte for byte. An isolated full LaTeX/BibTeX rebuild produced
13 A4 pages, 21 citation commands, 3 bibliography entries, zero unresolved
citation/reference, zero overfull box, zero missing glyph, and zero fatal
error. Its layout-preserving extracted text is byte-identical to the promoted
PDF text.

## Exact correction authority

| Item | Binding |
|---|---|
| Authorized patch | `421e969a54bcd5a783faeab1485605533e4465bd8b7e4289cdf522de0770ebc0` |
| Issue list | `6cea3cdbb7f4c33460993395eb3ec5596737af47ed4ac8495311afefe6177908` |
| Authorization carrier | `01bedd0142b6942f1df5f21ef2c15af0a87cef2e89d3152f86f095a4666fc60b` |
| Apply report | `88c2becd2a644537d3ba356f2b97eb9d3eecca00fdbab93713d02226e1b51765` |

The exact author decisions were:

- `IL-MINOR-1 -> authorize B0005/replace_block`;
- `IL-MINOR-2 -> authorize B0094/replace_block`.

Only those two blocks changed: 2/105 touched, 103/105 byte-preserved,
`touched_ratio=0.019`, no structural flag. B0005 synchronizes the displayed
date to 25 August 2026. B0094 replaces the deferred materials status with an
explicit author-owned “available upon reasonable request” policy without
inventing a public URL or repository.

## Full Mode-2 results

| Phase | Fresh Round 2 population | Result | Issues |
|---|---:|---|---:|
| A references | 3 sources | **3/3 VERIFIED** | 0 |
| B citation context | 21 citation commands | **21/21 SUPPORTED** | 0 |
| C internal/data/build | 16 consistency families | **16/16 PASS** | 0 |
| D originality | 37/74 body paragraphs plus title, two Round-2 changed surfaces, declarations, and self-reuse queries | **PASS WITH LIMITATIONS / WARN_NOT_BLOCK** | 0 actionable |
| E claims | 49 ALL claims, 63 persisted evidence rows | **49/49 and 63/63 VERIFIED** | 0 |
| E6 semantic drift | two rounds, 15 patch ops | **none detected by the recorded semantic review** | 0 |

### Phase A/B

- Deninger v1, Deninger--Mellit 2019, and the Stacks Project were independently
  re-queried against primary/official records.
- Bibliographic fields: 3/3 accurate; orphan references 0; dangling citations
  0.
- All 21 source locators and citation contexts are supported. The two
  Corollary 4.6 citations are correctly classified as attribution of the source
  assertion; the manuscript's corrective proof is internally supplied rather
  than delegated to the citation.

Carrier:
`notes/stage4_5_round2_reference_citation_audit.md`, SHA-256
`c389dcf60077c3ccde4f4e92f0463ef574964b4ae43e2a214e9c6cf04ffb616a`.

### Phase C

- C1: no statistical or empirical result surfaces; not applicable.
- C2: all 16 registered consistency families pass.
- C3: no figure, table, or caption surfaces; not applicable.
- C4: one no-experiment declaration, zero experiment claims, zero provenance
  rows, and zero alignment rows; declaration/provenance symmetry checks pass.
- `IL-MINOR-1`: **CLOSED_VERIFIED**.
- `IL-MINOR-2`: **CLOSED_VERIFIED**.

Carrier:
`notes/stage4_5_round2_phase_c_internal_consistency_audit.md`, SHA-256
`388afc5c29ddf3b13d25163a15553c660367db46e805f0963fa9c90fce774e56`.

### Phase D and seven failure modes

Fresh searches comprised 37 quoted body fragments, 37 supplementary body
queries, six non-body/changed-surface queries, and five email/topic self-reuse
queries. Grades were 29 `ORIGINAL`, 8 `COMMON_KNOWLEDGE`, and zero
`PARAPHRASE`, `CLOSE_MATCH`, or `VERBATIM`. The result is bounded and is not a
professional plagiarism determination or `CLEAN` certificate.

Self-reuse remains `INSUFFICIENT EVIDENCE FOR CLEAN`; no actionable signal was
found in the reliably email-linked public subset. Integrated with the fresh
Phase A/B source audit, hallucinated-citation mode is clear on the enumerated
citation population. Early frame-lock remains an insufficient-evidence warning.
No mode is `SUSPECTED`, so the seven-mode carrier is `WARN_NOT_BLOCK`.

Carrier:
`notes/stage4_5_round2_originality_failure_mode_audit.md`, SHA-256
`b212e5c5cf877d4d7d4f0726a08e072bfe615115b298ae7171055025aa914bed`.

### Phase E/E6

| Carrier | SHA-256 | Replay |
|---|---|---|
| Claim Registry | `eddfa08f0b9d8f9e1b0b6c9433d28da7ffef078b886b77b0c29f44055955b240` | 49 ALL claims |
| Evidence rows | `1f0d696a8988aebd0b00924c30c1dd8ec12a70b6a5ce7ffbd2156c38192ded1a` | 63 rows, all VERIFIED |
| Coverage receipt | `6ad28465bfd126a748440957389f01264ef1546956bf09c81cc3caaee302c749` | exact-input replay PASS |
| Coverage adjudication | `491502d67255dbecaff5ae9090ff889ac01669406d86470a557aac2174af37c7` | six lexical false positives rebound |
| E6 findings | `9f3e7795831e2086686d6f527b51c117d6d73afbccd2453685e1df30b652e982` | schema PASS; `findings=[]` |
| E6 semantic audit | `c8f4de2bd76e6cd30607047b4976229705e299910a47cae17fdb2d6da7c33150` | no finding recorded |

Coverage enumerates ten lexical candidates: four exact registry matches and
six adjudicated LaTeX/formula/line-fragment false positives. The raw count
remains visible; `semantic_extraction_coverage=not_machine_detectable` is not
upgraded to a completeness claim.

The Round 2 token checker has one advisory, the exact authorized `24 -> 25`
metadata change. Across the continuous two-round chain there are five token
advisories; none supplies or overrides the independent E6 semantic result.

## Machine handoff and compliance advisory

- Machine handoff:
  `notes/stage4_5_round2_integrity_report.json`, SHA-256
  `e877ee2014bb8b3722bc94d35d560e6278f7cce9a8ab0bc7984e7c8555b65e33`.
- Embedded evidence-row replay: PASS, 63 rows.
- Schema-12 compliance report:
  `notes/stage4_5_round2_compliance_report.json`, SHA-256
  `a34c4a2009b855fbbcef69d460ccf7abe1fab4feb854af5fcfa8ea552e0970e6`.
- Compliance status: `warn`, primary-research principles-only extension.

The compliance warning records material gaps in human-reviewer
documentation, model/prompt/configuration disclosure, `repro_lock`, and
task-specific fit evidence. It is not official RAISE compliance and is not a
Stage 4.5 hard block. The new materials policy closes the frozen manuscript
issue but does not itself fill the configuration-level reproducibility gap.

## Route A / Route B roadmap correspondence

The two governing files remain byte-identical to their frozen hashes:

- Route A v0.2.0:
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
- Route B v0.2.0:
  `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

P22 is a pure-algebra theorem paper. It does not define Route A's required
dynamical candidate, clock, orbit ledger, determinant convention, or data
split. It also lacks Route B's Hilbert space, operator, domain, boundary
conditions, self-adjointness, spectral type, prime-power trace, and completed-xi
identity. Therefore:

```text
Route A = NOT_TESTABLE; no A0--A4 tuple; no advancement
Route B = ROUTE_B_NOT_TESTABLE; no B1--B5 tuple; invocation disallowed
Gates A--E = NOT_REACHED
gate credit = NONE
```

The sheaf-theoretic word “lift” is not A4 quantization or a Route-B operator
lift. The detailed carrier is
`notes/stage4_5_round2_route_crosswalk.md`, SHA-256
`67a7a4abf8a5c425b19cf679c3bd5d0d0348e6c6632f51738a269d98b80cae5b`.

## Mandatory pre-Stage-5 advisories

The fixed post-PASS order was executed on accepted artifact ID
`p22-stage4.5-round2-accepted-draft` and source SHA
`e90dd88109d4e53d1f789808286c15cc917003cd38b69f49ddaff8661b9158ed`:

1. **#660** emitted a schema-valid `HEURISTIC-ADVISORY / UNMEASURED`
   `not_checked` carrier because no permitted snapshot/manifest was supplied.
   This is not a clean-draft certificate.
2. **#672** returned
   `ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE` and wrote no final carrier,
   because no exact builder-produced preregistration sidecar exists and no
   explicit caller status was available from which one could lawfully be
   built. This is neither agreement nor inconsistency.

Both are advisory-only and leave the zero-issue PASS unchanged. Detailed
checkpoint carrier:
`notes/stage4_5_round2_stage5_entry_checkpoint.md`, SHA-256
`6eae478c85a1aeff1f07218b131a9e2fa76ee526a1f2c243b4f7b11d4c87f959`.

## Boundary and next required decision

Stage 4.5 Round 2 is complete at exact zero-issue PASS. Cross-model checking
was not configured or authorized. The process stops at the mandatory Stage 5
entry checkpoint. The next action requires the user's explicit instruction to
enter Stage 5 and the desired citation/format style; until then, source,
content, PDF, and route status remain frozen.
