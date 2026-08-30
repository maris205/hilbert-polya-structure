# Paper 25 Stage 4.5 E1.1 coverage adjudication

Audit date: **2026-08-30 UTC**

This is a draft-bound mechanical and semantic-census sidecar. It is not an
overall Stage-4.5 verdict and does not advance the pipeline.

## Exact bindings and counts

- Current work draft: notes/stage4_revision_round1.tex
- Draft SHA-256: 39a643c05b4820b782e45a5ec240caa7223ad444229e8a89bdcc98791ce23835
- Claim Registry SHA-256: 9e333277db2225c1e9d68afadb1c55acdb7845a28a72cb896aca8bef0cd8b90b
- Coverage report SHA-256: d8f9343806bbf42846f204a45a04ad4c7c07ae2eb7af3d5779da0d8b3cf61098
- Evidence-row file: 127 rows
- Evidence source-map SHA-256: 2134ef5b70b85d93882a6d9616c7e2d4e9e45566186525b245b096ecfe9bd711
- Registry population: 114 rows, all selection_tier=ALL
- Mechanical candidates: 5
- Mechanical candidates with exact full-span registry matches:
  5
- candidate_unregistered_count: 0
- semantic_extraction_coverage:
  not_machine_detectable

Within the frozen model-mediated population, 114 of
114 claims are registered and ALL-selected, and every
registered (claim_id, ref_slug) projection has a persisted evidence row. This
is 100% coverage of the frozen current-draft claim population. It is not a
machine proof that no additional semantic claim could be identified.

## Population census

The exact draft contains 116 anchored blocks. The semantic
census excludes only 29 inspected structural blocks: LaTeX setup and macros,
begin/end-document plumbing, keywords, heading-only blocks, and the bibliography
invocation. Every other current block from title metadata through English and
Traditional-Chinese abstracts, main text, tables, proofs, conclusion, and
declarations is included.

Seven citation-dense or compound scientific blocks and the declaration block
are split at exact sentence spans. Comment-only SOURCE carrier lines and
heading-only declaration labels are not themselves registered as claims.
B0047--B0049 are one mathematical proof surface because those three markers
are layout splits inside one proof. The five bounded candidates emitted by the
official ARS detector are exact members of this already-frozen population.

## Mechanical candidate replay

| Candidate | Line | Detector class | Exact registry row |
|---|---:|---|---|
| CAND-B12907-13099-75c08521c459 | 132 | citation_bearing_sentence | P25-S45-E1-B0026-S02 |
| CAND-B13100-13262-252b04207846 | 133 | citation_bearing_sentence | P25-S45-E1-B0026-S03 |
| CAND-B13263-13430-98a70411eab7 | 134 | citation_bearing_sentence | P25-S45-E1-B0026-S04 |
| CAND-B13431-13682-44c954546468 | 135 | citation_bearing_sentence | P25-S45-E1-B0026-S05 |
| CAND-B23293-23441-7b231865ce2a | 274 | quantitative_sentence | P25-S45-E1-B0050-S03 |

The official detector is deliberately conservative: its candidate scope is
limited to citation-bearing sentences with inline machine anchors and selected
quantitative lexical triggers. The semantic block census therefore includes
many claims outside those mechanical classes.

## Evidence projection and source boundary

- Expected evidence tuples: 127
- Persisted evidence rows: 127
- Source-bound excerpt states: 127
- Anchorless rows: 0
- Local artifact-chain rows: 114
- Fresh Stage-4.5 external-audit-carrier rows: 13
- Distinct source-map slugs: 9

P25LocalArtifactChain persists the exact current draft together with frozen
theorem, symbolic-count, physical replay, witness, lock, receipt, Revision-
Evidence Bundle, Material Passport, fresh reference snapshot, and citation
audit carriers. The eight bibliography slugs map to the exact bytes of the
current Stage-4.5 fresh Phase-A/B citation-context audit, with one short exact
excerpt for each of its 13 checked contexts. Those external rows are
source-bound to the fresh audit carrier; they are not represented as local
copies of the primary publications.
Likewise, a current-draft/local-artifact binding establishes provenance and
replayable bytes, not independent mathematical truth.

## Replay commands

~~~text
PYTHONDONTWRITEBYTECODE=1 python   /root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars/scripts/claim_registry_coverage.py   --draft /root/autodl-tmp/flow_systems/papers/25-three-disk-scattering-flow/notes/stage4_revision_round1.tex   --registry /root/autodl-tmp/flow_systems/papers/25-three-disk-scattering-flow/notes/stage4_5_claim_registry.json   --validate-report /root/autodl-tmp/flow_systems/papers/25-three-disk-scattering-flow/notes/stage4_5_claim_registry_coverage.json

PYTHONDONTWRITEBYTECODE=1 python   /root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars/scripts/evidence_rows.py validate   /root/autodl-tmp/flow_systems/papers/25-three-disk-scattering-flow/notes/stage4_5_evidence_rows.json   --source-map /root/autodl-tmp/flow_systems/papers/25-three-disk-scattering-flow/notes/stage4_5_evidence_source_map.json
~~~
