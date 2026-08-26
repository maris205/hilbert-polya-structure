# P70 strict ARS 0.1.27 closure receipt

**UTC date:** 2026-08-26  
**Scope:** Stage-2.5 sidecars/state/QA only; manuscript, bibliography, and PDF
were not edited.  The package manifest was regenerated only after the complete
five-paper Stage-2.5 seal.

## Artifact results

| Artifact/check | Result |
|---|---|
| active passport | `docs/papers67_71_sequence/stage2_5/MATERIAL_PASSPORT.yaml`; SHA-256 `097d6d3cc38d0dc8a97889ba40966bd82d422c8a4c4bc8ae0851015b85ea6f99`; status `VERIFIED`; declaration `no_experiments_declared` |
| registry | 35 claims; 30 selected; SHA-256 `4dbfd4362e4691973411ee7a7079c2687c217cad55f930f479f38c0f230fb10b` |
| evidence rows | 34 total = 13 source-bound + 21 anchorless; SHA-256 `1cb809cd125ffc5f6be47248dab1f23a5113d173eb9a94d53754baf40a1680fd` |
| source map | 7 exact held source texts; SHA-256 `a2deaaf2f8819af4e6d54309c7659569cf634fd957d7fe8784d8d63346465fa2` |
| source manifest | SHA-256 `14f9c903f12486141ccd27166f7c5a5308f46c80579bc8d891db448edbaaccec` |
| ARS validator | PASS: 34 evidence rows; every cited excerpt replays exactly; full tuple order matches registry/ref order |
| D1 | 14/46 = 30.43%; all 8 major sections |
| E6 | schema-valid `skipped_no_revision_evidence`; SHA-256 `d7383f574fd4e30ad6eb44e56ec95aea1b51149063451cf083cbc7bd13affa69` |
| seven modes | CLEAR 7; SUSPECTED 0; INSUFFICIENT EVIDENCE 0; Mode 7 is bounded to the checked frame-lock mechanism |
| disposition | PASS_WITH_NOTES; SHA-256 `894a83176afc14769a73357ca55d76fb32b778b8e374e9689a9a702f91f4d370` |

## Replay commands

The builder was run twice to materialize and then cache-replay the stable rows,
followed by check-only construction and the ARS source-map validator:

```text
python3 build_strict_evidence_rows.py --ars-builder <ARS-0.1.27>/evidence_rows.py
python3 build_strict_evidence_rows.py --ars-builder <ARS-0.1.27>/evidence_rows.py
python3 build_strict_evidence_rows.py --ars-builder <ARS-0.1.27>/evidence_rows.py --check-only
python3 <ARS-0.1.27>/evidence_rows.py validate evidence_rows_round1.json --source-map evidence_source_map_round1.json
```

Observed validator line: `PASS: 34 evidence row(s)`.  A separate replay
expanded every selected registry claim, preserved each `ref_slugs` array in
order, required a positive exact excerpt for every cited tuple, and required a
null source plus `anchorless` state for every no-ref tuple; it returned PASS.
The E6 JSON validates against the exact ARS
`claim_strength_drift_findings.schema.json` Draft-2020-12 schema.

## Frozen package check

- Bibliography/citations: 7 defined, 7 distinct cited, 14 citation commands,
  16 key mentions, zero ghost/dangling/undefined keys.
- `main.log`: no undefined citation/reference or LaTeX/package warning matched.
- Live deterministic control stdout remains byte-identical to the frozen
  receipt, SHA-256
  `fe26d12a4fd332b87027db685563980b788fb097bd633dc974b091de0bc2f42f`.
- Canonical PDF is unchanged: 7 A4 pages, 345,028 bytes, SHA-256
  `61398af7a4ab61ea3ace029ec315721d4a855bf8f60986c84b2fdc94d9bd0142`.

External release remains **HOLD**.  Positive source rows prove exact binding to
the held bounded passages, not full-work human attestation or priority.
