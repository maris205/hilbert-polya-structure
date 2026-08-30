# Paper 25 Stage 4.5 integrity-correction Round 1 report

Date: **2026-08-30**  
Scope: **exact four-operation bibliography repair on a derived working copy**  
State: **repair applied and bounded revalidation complete; fresh full Stage 4.5 verdict not reissued; Stage 5 closed**

## Authority and preconditions

The exact session-user event is the repository-level
`BATCH_ROUND9_STAGE4_PRIME_AND_P25_AUTHOR_EVENT_20260830.txt`, SHA-256
`fc4de4ab870bcb6ff3f1c0c9fc6eb9f389edbfbb2d6b01a79a063d21f80365dd`.
The schema-valid P25 author input binds that event receipt, one explicit
`authorize` decision per issue, and the exact patch SHA-256
`c135b935ff154a9dd946f1bb9652e514ebae0cf82dc7894149a2b6872bc0cffc`.

| Artifact | SHA-256 | Control role |
|---|---|---|
| `notes/stage4_revision_round1.tex` | `39a643c05b4820b782e45a5ec240caa7223ad444229e8a89bdcc98791ce23835` | unchanged current manuscript target |
| `notes/stage4_5_references_working.bib` | `24381ded0d5d9d91fc4a3ad5250e3ccd8039c96a5f9131a8a987eb56d85bb8d6` | frozen patch base; not overwritten |
| `notes/stage4_5_references_working.bib.block-manifest.json` | `a2e27c0f8e165c0d5730c165fb16f57b6067edafc0dd065676bcb1617ba71acc` | eight-block precondition manifest |
| `notes/stage4_5_integrity_correction_list.json` | `f25c80eae179acd0f50d948447000f775575a0c962ea9de3627c87d6d9c217c7` | four proposed issue scopes |
| `notes/stage4_5_integrity_patch_round1.json` | `c135b935ff154a9dd946f1bb9652e514ebae0cf82dc7894149a2b6872bc0cffc` | exact authorized patch bytes |
| `notes/stage4_5_integrity_authorization_input_round1.json` | `50324cbe040a0b6e96a0ee96ed790910159c9811b6159f74d46b796463648abf` | explicit event receipt and decisions |
| `notes/stage4_5_integrity_authorization_round1.json` | `7c9fad9e525e8a352ee95007bfbd02b8497d905b698f8eb40598d66ef82fc966` | official deterministic authorization sidecar |

Pre-apply replay confirmed the exact base, manifest, issue-list, patch, four
old hashes, and four target/operation pairs. Every patch operation declares
`claim_strength_changes=[]` and `collateral_authorization_ids=[]`. The
structural analysis reported four of eight blocks touched, ratio `0.5` against
threshold `0.6`, no heading operation, no section-count change, and
`structural_flags.any=false`; no structural acknowledgement was used.

## Exact applied result

The official ARS apply script wrote a new artifact and its report; it did not
overwrite the frozen base.

| Artifact | SHA-256 |
|---|---|
| `notes/stage4_5_references_corrected_round1.bib` | `a0bf0cd2f022f1b5dcc0bffdd1b28d135cef7c287f77c2a46e514480e2b3b5ab` |
| `notes/stage4_5_references_corrected_round1.bib.apply-report.json` | `d7f6eea3c77837ac902258f079ee54e7fbf182c4cbe0a0f25a274ced51b6be9b` |

The apply report records four operations, no fresh block IDs, no pure-move
pairs, four of eight blocks preserved byte-identical, and
`authorization_witness.status=pass`. This is a mechanical authority/apply
witness, not a Stage 4.5 integrity verdict.

| Correction | Applied target/op | Bounded post-apply check |
|---|---|---|
| `IL-MINOR-1` | `B0001/replace_block` | erratum citation and DOI `10.1063/1.457672` match the frozen fresh source snapshot |
| `IL-MINOR-2` | `B0002/replace_block` | erratum citation and DOI `10.1063/1.457670` match the frozen fresh source snapshot |
| `IL-MINOR-3` | `B0006/replace_block` | `Ruelle1976` now carries publisher-record `number = {3}` |
| `IL-MINOR-4` | `B0008/replace_block` | `Livsic1972` now uses the authoritative initials form `A. N.` |

The source comparison reuses the exact Stage 4.5 snapshot captured at
`2026-08-30T12:21:18Z`; it does not manufacture a newer source-capture event.
All 13 manuscript citation commands resolve to eight keys in the eight-entry
corrected bibliography.

## BibTeX, citation, build, and validator replay

A marker-stripped isolated LuaLaTeX/BibTeX build used the unchanged current
draft and the corrected derived bibliography. `bibtex` used eight entries and
reported zero warnings; after the required LaTeX passes, the 13-page A4 build
had zero undefined citations/references, LaTeX/package errors, fatal errors,
overfull boxes, or missing characters. The PDF was an isolated diagnostic
output and was not promoted. No byte-reproducible-PDF claim is made.

The following checks completed without a failing exit status:

```text
python .../scripts/revision_roadmap.py build-integrity-authorization \
  notes/stage4_5_integrity_correction_list.json \
  --base notes/stage4_5_references_working.bib \
  --patch notes/stage4_5_integrity_patch_round1.json \
  --author-choices notes/stage4_5_integrity_authorization_input_round1.json \
  --output notes/stage4_5_integrity_authorization_round1.json

python .../scripts/ars_apply_revision_patch.py \
  notes/stage4_5_references_working.bib \
  notes/stage4_5_integrity_patch_round1.json \
  --block-manifest notes/stage4_5_references_working.bib.block-manifest.json \
  --integrity-issue-list notes/stage4_5_integrity_correction_list.json \
  --integrity-authorization notes/stage4_5_integrity_authorization_round1.json \
  --output notes/stage4_5_references_corrected_round1.bib

python .../scripts/revision_roadmap.py validate-integrity-authorization \
  notes/stage4_5_integrity_correction_list.json \
  --base notes/stage4_5_references_working.bib \
  --patch notes/stage4_5_integrity_patch_round1.json \
  notes/stage4_5_integrity_authorization_round1.json

python .../scripts/claim_registry_coverage.py \
  --draft notes/stage4_revision_round1.tex \
  --registry notes/stage4_5_claim_registry.json \
  --validate-report notes/stage4_5_claim_registry_coverage.json

python .../scripts/evidence_rows.py validate \
  notes/stage4_5_evidence_rows.json \
  --source-map notes/stage4_5_evidence_source_map.json

python .../scripts/revision_roadmap.py validate-bundle \
  notes/stage4_revision_evidence_bundle.json --root papers/25-three-disk-scattering-flow

python .../scripts/check_revision_token_conservation.py patch \
  --patch notes/stage4_revision_patch_round1.json \
  --base notes/stage3_revision_base.tex

python .../scripts/check_compliance_report.py \
  notes/stage4_5_compliance_report.json

bash experiments/reproduce_stage4.sh

# In an isolated temporary directory after stripping working-copy markers:
lualatex --interaction=nonstopmode --halt-on-error paper.tex
bibtex paper
lualatex --interaction=nonstopmode --halt-on-error paper.tex
lualatex --interaction=nonstopmode --halt-on-error paper.tex
```

Replay results were: claim-coverage replay passed; 127 evidence rows validated;
the existing manuscript Revision-Evidence Bundle validated; Schema-12
compliance validated; the claim-strength-drift finding set validated; and all
75 Stage-4 tests passed. The closed replay reported
`canonical_results_modified=false`, `scientific_value_changed=false`, and two
byte-identical isolated Round-8 core builds. That last statement is limited to
the named deterministic core replay, not a global binary-reproducibility
claim. The existing token-conservation checker still emits its four previously
adjudicated Stage-4 advisories; the recorded E6 finding set remains empty, but
that model-mediated result is not a deterministic semantic-completeness
guarantee.

## Preserved bytes and boundaries

| Preserved artifact | SHA-256 after repair |
|---|---|
| `notes/stage4_revision_round1.tex` | `39a643c05b4820b782e45a5ec240caa7223ad444229e8a89bdcc98791ce23835` |
| `paper/manuscript.tex` | `283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb` |
| `paper/references.bib` | `de776cc0bf16e6c837917f4a289f8c07b8b4f7e9146183b9a9e0e6294db99e6b` |
| `notes/stage4_5_references_working.bib` | `24381ded0d5d9d91fc4a3ad5250e3ccd8039c96a5f9131a8a987eb56d85bb8d6` |
| `notes/stage4_5_evidence_rows.json` | `752504e737d4162dff1e189c878f4c1492054207cbd36752dfc6ff86cacce146` |
| `notes/stage4_revision_evidence_bundle.json` | `bf368e5757d30bf182eca18fe574814ecc11e750f5060b528bd1022b68b9fd51` |

The claim registry, coverage artifact, evidence source map, drift finding set,
canonical results, Route records, and old Stage 4.5 reports/passport also remain
unchanged. The evidence builder was not run, and no `captured_at` value was
refreshed.

## Remaining gates

1. Run a fresh, from-scratch Stage 4.5 gate against the unchanged manuscript
   together with the corrected derived bibliography; do not treat this repair
   report as that gate.
2. If the fresh gate supports closure, issue new versioned human/machine
   integrity reports and a new Material Passport. The current Round-1 report
   still records four MINOR items and the current passport remains
   `UNVERIFIED`.
3. Keep `paper/references.bib` unchanged until a separately authorized
   canonical-promotion step. This round authorizes no manuscript, result,
   Route, release, submission, or canonical bibliography edit.
4. Stage 5 remains closed until the fresh Stage 4.5 terminal resolution and
   its mandatory entry checkpoint. Professional originality screening remains
   recommended; no global originality claim is made here.
