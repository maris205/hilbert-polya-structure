# Round 9 Stage 2.5 claim-sidecar independent validation

## Post-authorization controlling addendum

The fail-closed experiment-intake gate described in this earlier independent
snapshot was closed by the scholar declaration received at
`2026-08-29T05:52:42Z`. All five passports now contain schema-valid,
non-empty provenance ledgers: **33** experiment/certificate entries, **309**
hash-bound current artifacts, and **62** registered direct claim alignments.
The three authorized bibliography corrections were applied and P25/P28 were
rebuilt; all **31/31** references now verify. Official ARS provenance and
claim-audit consistency checks pass for all five papers. The current batch
decision is **Stage 2.5 PASS AT MANDATORY CHECKPOINT** with
`stage3_authorized=false`; P28 retains one non-blocking semantic
`MINOR_DISTORTION` concerning replay-order prose.

The original sidecar audit below is retained as a timestamped historical
snapshot; its pending-gate conclusion is superseded by this addendum and the
controlling `BATCH_ROUND9_STAGE2_5_INTEGRITY_REPORT.md`.

**This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.**

Audit time: `2026-08-29T01:48:19Z`  
Stable snapshot digest: `38eeb971968dfa7e67ce7447f7b7b81def11213feb4d6fd42cddf93d519a8062`  
Scope: Papers 24--28; claim registries, coverage reports, Phase-E evidence rows, and claim-strength-drift sidecars.  
Authority: ARS-Codex `academic-research-suite` 0.1.26; Academic Pipeline 3.21.0; `claim_verification_protocol.md`; `evidence_row_protocol.md`; canonical JSON schemas; official `claim_registry_coverage.py` and `evidence_rows.py`.  
Mutation boundary: no manuscript, bibliography, PDF, or pre-existing artifact was changed by this independent audit.

## Layered verdict

1. **Claim-sidecar contract: PASS.** All five current registries are schema-valid and exactly draft-bound; high-impact tiering and random-sentinel arithmetic conform; all coverage reports replay with zero mechanical gaps; every selected claim has exactly the required `(claim_id, ref_slug-or-null)` evidence tuple(s); all evidence rows pass the official validator; all drift sidecars are valid first-pass skips.
2. **Evidence-provenance strength: LIMITATION, not a tuple failure.** Every evidence row deliberately records `excerpt.state = anchorless`. Citation-bearing tuples now preserve their exact `ref_slug`, but no row embeds a source-bound excerpt, source-content hash, artifact hash, or source span. The rows are honest explicit empty evidence states. Their claim-level `VERIFIED` verdicts are not independently proven by these sidecars.
3. **Semantic truth/extraction: NOT CERTIFIED.** The validators establish shape, hash, span, selection, and tuple consistency. They do not establish claim truth, complete semantic extraction, source support, or actual research execution. The coverage reports correctly retain `semantic_extraction_coverage: not_machine_detectable`.
4. **Overall Stage 2.5 gate: FAIL-CLOSED PENDING SCHOLAR DECLARATION.** The independent claim-sidecar defects detected in the initial build were repaired, but the post-#260 D7 `experiment_intake_declaration` is still absent. Because all five papers report project-owned computation, only an explicit scholar-owned `experiments_declared` decision plus provenance completion can close this gate. Stage 3 is not authorized yet.

## Exact final counts

| Paper | Registry total | HIGH-IMPACT | RANDOM | TOP-UP | NOT-SELECTED | Selected claims | Required/persisted tuples | Citation-bearing tuples | Coverage candidates / gaps | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P24 | 76 | 61 | 3 | 0 | 12 | 64 | 66 / 66 | 3 | 7 / 0 | PASS |
| P25 | 72 | 45 | 3 | 0 | 24 | 48 | 49 / 49 | 2 | 1 / 0 | PASS |
| P26 | 72 | 65 | 3 | 0 | 4 | 68 | 70 / 70 | 5 | 4 / 0 | PASS |
| P27 | 77 | 67 | 3 | 0 | 7 | 70 | 71 / 71 | 5 | 7 / 0 | PASS |
| P28 | 85 | 78 | 3 | 0 | 4 | 81 | 84 / 84 | 9 | 5 / 0 | PASS |
| **Total** | **382** | **316** | **15** | **0** | **51** | **331** | **340 / 340** | **24** | **24 / 0** | **PASS** |

The corrected non-high remainders contain 66 claims in total (15 / 27 / 7 / 10 / 7). They produce three RANDOM sentinels per paper because each remainder is at least 3 and `ceil(10%)` is at most 3. After those 15 sentinels, 51 claims remain NOT-SELECTED. No TOP-UP is required because each selected population exceeds 10.

## Registry, span, and tier validation

All 382 rows conform to `claim-registry/1.0`:

- manuscript SHA-256 equals `draft_raw_sha256`;
- every half-open UTF-8 byte span decodes exactly to `claim_text`;
- claim IDs and exact span pairs are unique within each paper;
- all 316 high-impact rows carry a non-empty `high_impact_basis`;
- no row marked `quantitative` or `causal` remains outside `HIGH-IMPACT`;
- every quantitative high-impact row records `numerical`, and every causal high-impact row records `causal` in its basis;
- the RANDOM count equals the protocol calculation for every corrected remainder;
- evidence-row claim text, tier, and writer locator agree with the registry.

The final RANDOM IDs are P24 `E1-002/E1-005/E1-040`, P25 `E1-016/E1-043/E1-064`, P26 `E1-016/E1-022/E1-036`, P27 `E1-030/E1-033/E1-073`, and P28 `E1-050/E1-052/E1-083`. Their count and eligibility are auditable; the registry schema has no field for a PRNG seed or draw receipt, so unbiasedness of the particular identities is not mechanically proven by the sidecars.

The registries retain nested/overlapping exact spans: P24 7 overlap pairs, P25 1, P26 3, P27 7, and P28 5. The schema does not prohibit overlap, so this is not a contract failure. It is a semantic-granularity caveat: paragraph-sized composite rows can bundle several theorem, result, and limitation assertions under one claim verdict.

## Coverage replay and mechanical-candidate limitation

Each `stage2_5_claim_registry_coverage.json` replayed against the exact current manuscript and exact serialized registry:

```text
claim-registry coverage replay: PASS
```

All five reports bind the current draft and registry, record `candidate_unregistered_count = 0`, and retain `semantic_extraction_coverage = not_machine_detectable`.

The zero-gap result is bounded to the detector grammar. Only 24 candidates were detected across 382 registered claims. Conservative manual inspection finds obvious LaTeX/scaffolding false positives in P24 (`\label{cor:d9}` / an environment heading), P27 (`[x^d]...` classified as citation-bearing), and all five P28 candidates (equation-label/range or identifier tokens such as `g01`, `g23`, `G2`). These false positives are registered-span matched, so they do not create false gaps; they do show why the replay cannot certify semantic completeness.

## Evidence rows and tuple audit

Official validation returned:

```text
P24: PASS: 66 evidence row(s)
P25: PASS: 49 evidence row(s)
P26: PASS: 70 evidence row(s)
P27: PASS: 71 evidence row(s)
P28: PASS: 84 evidence row(s)
```

The before/after aggregate snapshot digest was identical, so validation ran on stable bytes. Row IDs and canonical row hashes replay; every selected claim appears; no NOT-SELECTED claim appears; rows sharing a claim agree on claim metadata and verdict; all 340 rows record the claim-level verdict `VERIFIED`.

Tuple accounting now passes exactly:

- a selected claim with no `ref_slugs` has one row whose `source.ref_slug` is null;
- a selected sourced claim has one separate row for every exact registry `ref_slug`;
- no required ref slug is missing or duplicated;
- the distinct evidence-row claim-ID set equals the selected claim-ID set.

### P28 repair detail

The earlier P28 violation is closed. `P28-E1-004` at `manuscript.tex:L132-L141` records `AigonDupuyEtAl2005` and `Nazarenko2013`; it now has two separate rows preserving those source slugs. The same one-row-per-source rule also covers P28-E1-010, E1-020, E1-021, E1-023, and E1-024. P28 therefore has 81 selected claims but 84 required and persisted tuples.

### Anchorless evidence limitation

All 340 rows have `excerpt.state = anchorless` and `anchor.kind = none`. The 24 citation-bearing rows preserve their source slug but still have null source-content/artifact hashes, excerpts, and spans. This is allowed by the evidence-row schema and protocol as an explicit empty evidence state, and failure/empty states do not change the Phase-E claim-verdict taxonomy. It is not source-bound proof.

Accordingly:

- **tuple contract:** PASS;
- **row structural integrity:** PASS;
- **embedded source provenance:** unavailable/anchorless;
- **semantic `VERIFIED` verdict:** carried consistently but not independently established by the row itself.

No consumer may upgrade `anchorless` to `verified_exact_match` or `agent_extracted`, infer a human-read mark, or describe these rows as source-bound verification receipts. If a later checkpoint needs replayable source evidence, rebuild the cited tuples with explicit session-held source bytes and a quote/page/section anchor through `evidence_rows.py`; do not hand-edit the rows.

## Claim-strength-drift sidecars

All five `claim-strength-drift-findings/1.0` files pass the canonical schema and record the correct first-pass state:

- `status = skipped_no_revision_evidence`;
- `revision_evidence_bundle_sha256 = null`;
- `findings = []`;
- `final_draft_sha256` equals the current manuscript;
- protocol SHA-256 equals `f26d4e0b876f323db5fccc1bbc3120189e69282e45ec6b6cc0cee1e3b1e7a537`.

This is a valid E6 skip, not a no-drift certificate.

## Remaining fail-closed gate: experiment intake

D7 remains unresolved for all five papers:

- the runs are treated as post-#260;
- the manuscripts report project-owned computation;
- `no_experiments_declared` would contradict the manuscripts;
- no explicit scholar-owned `experiment_intake_declaration` is present;
- an agent cannot infer or sign `declared_by = scholar`.

The exact requested statement is already recorded in `BATCH_ROUND9_STAGE2_5_EXPERIMENT_INTAKE_REQUEST.md`. Until the scholar confirms it, the corresponding `experiment_provenance[]` entries are populated and validated, and claim-to-provenance alignment is run, the overall Stage 2.5 verdict remains **FAIL-CLOSED** even though the claim sidecars now pass.

## Executable replay rules

For any further rebuild:

```text
1. Freeze manuscript bytes and registry population.
2. HIGH-IMPACT := every numerical, causal, headline, methods-critical,
   or disputed claim; persist every applicable high_impact_basis.
3. Compute RANDOM only from the frozen non-high remainder:
   all if remainder < 3, else min(10, max(3, ceil(0.10*remainder))).
4. Add TOP-UP only when HIGH + RANDOM < min(10, registry_total).
5. For each selected claim:
   - no ref_slugs -> exactly one (claim_id, null, none) row;
   - ref_slugs -> at least one separate row per exact ref_slug and actual anchor/state.
6. Require selected claim-ID set == evidence-row claim-ID set, exact tuple
   coverage with no duplicates, and consistent claim view/verdict per claim.
7. Replay registry schema/spans, coverage report, evidence-row validator,
   drift schema/bindings, and aggregate counts from one stable snapshot.
```

Anchorless rows remain honest absence states. A `VERIFIED` semantic verdict still requires the verifier's actual source/data comparison outside the row's structural validator.

## Stable audited hashes

| Paper | Manuscript | Claim registry | Coverage report | Evidence rows | Drift sidecar |
|---|---|---|---|---|---|
| P24 | `e43ba0f77332b79df4d84346dcb6e3041c20f4bdded5a91f42caac348ea9fd11` | `6a6fc0ebc3f76814638e49e378f2d64b086d06658cf54f1ccb877c0a8eedcdd4` | `9e8c46db07e97ecadff4cda8e33f5c3ac754843ac2d7ab294594f59e58e20634` | `fe1a8634f6e0a09f0be623b23dd248257a1844a5ed54ce9ce86cfdd0ea7f9890` | `48e1d83d8a8fc265fd5c4c8afcc4dcb2be416ad47ff7eb8f79d8153474c7284c` |
| P25 | `283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb` | `57063b60063a873d909506e6fcf8c3bd938c4fed57de06cb58beee0daca76956` | `0b68204e8a47ae36c68467dddd6fbde480f7de7063e5eabc213ff1dddc481a8d` | `26e7fd2a6f628e463c5fb8f224f17851d55bd65fb67d726aa4dcd0b72e27eb89` | `da3d25474167f4323266361a4271ae23e7f1cf22ee51bf757e20a0c8f525ddff` |
| P26 | `00a21246f496b12f98389522d762ad6c4e10683e0eb21163b881d7b035f9c2fe` | `1d27b238ae1fd5485192c7044f135e530d68aba6c997041fd441d7db4ded9cf2` | `0d9b8e7d83e6c443e3eab02939511ce454d070377ccd8cdad5d3093a9aa47d20` | `7cdc6095fae6ef317059ce46104bfaeee4a7707f51fb4dcd78005e1bf8f0a842` | `3b1a79c16d06ef0ab9b46cac322f5636c321b7f48f50f1d3c5620bb5045c3c30` |
| P27 | `c2809011a722b81732952d889f194549adea58875b605dbafe58ada93de9b4b9` | `05455f35794381fc5f472baaa56cdd2fedaf3d3cbdb99f58f344364c26893452` | `407174b357de7e718d6d379de4807fc20ea694610091789f176444debdbbb07d` | `2f47adea1276a72469fddd8c1ee666796e2b73dcd388acc986c9088756be0496` | `d8679aed864b0bd8ebbf8dc126a7dbf7303e77ec2dd804b35ca6c50451b8f0ca` |
| P28 | `864d2f6ce0f76245d4d4237ba2981b3e82fc8e31f7991f1f331817f7c028aec7` | `031e04aae854667ba03e4b39d8df28fa61391264ab7f8c1fee55d6d6a3514f07` | `312bd9883bd4a15993ce40702e696e125e1ba550b762204a9c9956b76fd2b35a` | `31c68cf97a63af5709c7c48883b3df1765449bb47b3efe0cc8fff89872c4cc3f` | `c5a134885af90e327aa32f6112eab32cc9d1288df2409be85b897a93596a92a9` |
