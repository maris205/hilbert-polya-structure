# P67 strict ARS 0.1.27 closure receipt

**UTC date:** 2026-08-26  
**Scope:** Stage-2.5 sidecars/state/QA only; manuscript, bibliography, and PDF
were not edited.  The package manifest was regenerated only after the complete
five-paper Stage-2.5 seal.

## Artifact results

| Artifact/check | Result |
|---|---|
| active passport | `docs/papers67_71_sequence/stage2_5/MATERIAL_PASSPORT.yaml`; SHA-256 `097d6d3cc38d0dc8a97889ba40966bd82d422c8a4c4bc8ae0851015b85ea6f99`; status `VERIFIED`; declaration `no_experiments_declared` |
| registry | 33 claims; 23 selected; SHA-256 `cf405439753be62b5939d64de3314dbdbe304f785262c4c8d8848ecf39bc29ea` |
| evidence rows | 27 total = 11 source-bound + 16 anchorless; SHA-256 `2ee12d21799c6b11084c476c7277b569a295dc5c668d2082319befb4aea34347` |
| source map | 8 exact held source texts; SHA-256 `b3329d9f580a9ba117948eecaa34f5988d2cbf0209eed074dcc02c5a9117ad68` |
| source manifest | SHA-256 `a313c85ffa40643099bb150274a06010d3a527dad5ed4cee623d0d2dfa00a75a` |
| ARS validator | PASS: 27 evidence rows; every cited excerpt replays exactly; full tuple order matches registry/ref order |
| D1 | 26/85 = 30.59%; all 7 major sections |
| E6 | schema-valid `skipped_no_revision_evidence`; SHA-256 `9bfee5c9683555f28d67575074e3fd2bfebf26fb27fa278a7bcf60cb7c7a33e1` |
| seven modes | CLEAR 7; SUSPECTED 0; INSUFFICIENT EVIDENCE 0; Mode 7 is bounded to the checked frame-lock mechanism |
| disposition | PASS_WITH_NOTES; SHA-256 `7d8d924be13ffa0cdd0aded72f0fbe35a7548460f50d1a522b39da257fa32e29` |

## Replay commands

The builder was run twice to materialize and then cache-replay the stable rows,
followed by check-only construction and the ARS source-map validator:

```text
python3 build_strict_evidence_rows.py --ars-builder <ARS-0.1.27>/evidence_rows.py
python3 build_strict_evidence_rows.py --ars-builder <ARS-0.1.27>/evidence_rows.py
python3 build_strict_evidence_rows.py --ars-builder <ARS-0.1.27>/evidence_rows.py --check-only
python3 <ARS-0.1.27>/evidence_rows.py validate evidence_rows_round1.json --source-map evidence_source_map_round1.json
```

Observed validator line: `PASS: 27 evidence row(s)`.  A separate replay
expanded every selected registry claim, preserved each `ref_slugs` array in
order, required a positive exact excerpt for every cited tuple, and required a
null source plus `anchorless` state for every no-ref tuple; it returned PASS.
The E6 JSON validates against the exact ARS
`claim_strength_drift_findings.schema.json` Draft-2020-12 schema.

## Frozen package check

- Bibliography/citations: 11 defined, 11 distinct cited, 17 citation commands,
  21 key mentions, zero ghost/dangling/undefined keys.
- `main.log`: no undefined citation/reference or LaTeX/package warning matched.
- Live deterministic control stdout remains byte-identical to the frozen
  receipt, SHA-256
  `a44506264017a8e6250e123df4477898def6c23f560c67b4e829948967c0bb26`.
- Canonical PDF is unchanged: 11 A4 pages, 408,243 bytes, SHA-256
  `ed2ffeedc97cc82d006bf540468ef7bf9c1655cad3f4600fb393f8d6451fc7da`.

External release remains **HOLD**.  Positive source rows prove exact binding to
the held bounded passages, not full-work human attestation or priority.
