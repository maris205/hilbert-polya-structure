# P24 Stage-4′ Round-2 Revision Log

Date: **2026-08-30**

| Item | Obligation | Author choice | Applied targets | Result |
|---|---|---|---|---|
| `REV-001` | must fix | `will_address` | `B0015`, `B0032`, `B0034`, `B0104` | Fresh primary-source sidecar bound; exact locators and bounded novelty allocation exposed without a priority claim. |
| `REV-003` | must fix | `will_address` | `B0056`, `B0065`, `B0067`, `B0068`, `B0075`, `B0084` | Existing loxodromic manifest/code/tests/replay/outputs/receipt bound; matrix-only owner boundary retained. |

## Deterministic application

- Base: `notes/stage4_revision_round1.tex`, SHA-256 `b098630fdf8db94b6ae892e86eabafe1832b45ff72122ea722100d3541e46d16`.
- Patch 1.1: `notes/stage4_prime_revision_patch_round2.json`, SHA-256 `9b7a7dd19557488852abc5ddcd26ac431568f3dbe259ffb6da23ba44da4f6d97`.
- Revised draft: `notes/stage4_prime_revision_round2.tex`, SHA-256 `79735d058d965a35de10cc0b3655e0b1db5217bde00e02d2d48b7564cd841afc`.
- Apply report 1.3: SHA-256 `484c1436c89733aab44fd35b1243af8443836e64cf3d4548cc31b83eb9fd6ce9`.
- Applied operations: 10; preserved blocks: 101/111; touched ratio: 0.0901.
- Structural flags: none; structural acknowledgement: not used; pure moves: none.

The first applier invocation rejected the pre-image in Phase 1 because current schema 1.1 requires `emitted_by`; no output was written. The complete patch was re-emitted with that required provenance field and the single permitted whole-patch retry passed.

## Verification

- Official authority witness: PASS.
- Registered-surface replay: 10/10 exact once in the original blocks.
- Loxodromic support replay: 10/10 tests; two byte-identical isolated trees; canonical refresh false.
- Token conservation: advisory deltas only, attributable to source locators, artifact hashes, and support-test counts.
- Isolated marker-stripped build: 15 A4 pages; 0 undefined citations/references, 0 overfull boxes, 0 missing characters, 0 fatal errors.
- PDF byte reproducibility is not claimed; the preview PDF is a build-validation artifact only.

Stage status: **Stage 4′ author-side revision complete; author confirmation and fresh Stage 4.5 remain pending**.
