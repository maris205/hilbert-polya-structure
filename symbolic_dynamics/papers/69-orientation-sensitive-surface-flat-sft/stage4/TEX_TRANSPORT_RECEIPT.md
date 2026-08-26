# TeX Transport Receipt — P69 Round 1

- status: complete
- revision_round: 1
- canonical_markdown_patch: `stage4/REVISION_PATCH.json`
- patch_sha256: `582765d1082077f9f5d29ef36a883dd0f1181aad7288b10ced5e6c2ee9c81bdd`
- apply_report: `stage4/REVISED_DRAFT.md.apply-report.json`
- apply_report_sha256: `7b9e1fa500740a9143682e7aab80d7063e314e7ccefcbcb273f43594d15945a3`
- revised_markdown_sha256: `564c4f4afc71403cb9808afe974352ac287c492c626edbcccbb91c13586faa8d`
- final_pdf_sha256: `b45b6839b02cd7b285cab4b90753285d6c47f4b109a4461cce92bfc42b031b14`

## Transport model

`REVISED_DRAFT.md` is the canonical patch-applied Markdown artifact. The TeX
sources are its publication-build mirror: each authorized Markdown operation
is projected to the corresponding existing TeX section, while executable code
and `CONTROL_RESULTS.md` carry the deterministic evidence requested by the
methodology item. The TeX transport does not replace, modify, or enlarge the
patch authority. The apply report remains the authority for changed Markdown
block IDs.

## Operation-to-source mapping

| Apply op | Roadmap authority | Actual Markdown block IDs | TeX mirror | Auxiliary evidence | Mirror check |
|---:|---|---|---|---|---|
| 0 — `replace_block` B0010 | REV-P69-EIC-W1 | B0010 | `sections/1_introduction.tex`, proof-roadmap paragraph beginning “The proof has three successive stages” | none | The TeX sentence makes the same two-to-three stage-count correction as B0010 and leaves the formulas and proof claims unchanged. |
| 1 — `replace_block` B0097 | REV-P69-R1-W1 | B0097 | `sections/7_scope_controls.tex`, exact-control enumerate item for the synthetic two-degree ledger | `code/verify_surface_flat_sft.py`; `CONTROL_RESULTS.md`; `stage4/FINAL_CONTROL_RUN.out` | The TeX item and Markdown B0097 state the same bases, P/Q/R moments, recovered coefficients, and synthetic-fixture limitation; the code computes those exact quantities and the receipt ends in `ALL CHECKS PASS`. |

No fresh Markdown block was created by either replacement. The apply report
records two touched blocks, 113 byte-identical preserved blocks, no structural
flag, and no operation for the declined specialist or optional-transfer items.

## File-level mirror bindings

| File | SHA-256 | Role |
|---|---|---|
| `sections/1_introduction.tex` | `37243791b160b459bde5e7917d0db83e56584d5e8581bc094f9c289245702d7a` | B0010 TeX mirror |
| `sections/7_scope_controls.tex` | `f58164cd261b8555596d9d04e83b7d2dc492f830a14b18fa8bcadcbe50d63cf5` | B0097 TeX mirror and unchanged HOLD statement |
| `code/verify_surface_flat_sft.py` | `7f0305cfae3a3fd77e8640c88d01315f17fe7687913e420939f901c23957bdb8` | Exact multi-degree fixture implementation |
| `CONTROL_RESULTS.md` | `951b7b0bbe699eac071f3aa0c67f83dee202049ae19e3fe01d0d457728e5e211` | Human-readable control and build record |
| `stage4/FINAL_CONTROL_RUN.out` | listed in `FINAL_SHA256SUMS` | Frozen replay output |
| `stage4/FINAL_COMPILE_TRACE.txt` | listed in `FINAL_SHA256SUMS` | TeX build receipt |

## Boundary and invariance checks

- `main.tex` is unchanged from the package `SHA256SUMS` baseline:
  `5a594b3109734abe2947539ebd8efd02c828ea06147e31fb8cd7222fff5e1e6c`.
- `references.bib` is unchanged from the package baseline:
  `9eab29c4ae62a26087be3a4e6ec51e519656c28d0fc2fc0d13b3b0ec72779a03`.
  Therefore new references added in Round 1: **0**.
- Frozen Stage 3 bindings remain byte-exact: anchored draft
  `c4715fd7f9f34b37911b6da11634bde04326a635393f8fdec8cacaca456ddf9d`,
  block manifest
  `c12f7f6975ab1e066999949a56bcbf5366bf149172ec550966f0bed2806f3e4d`,
  and roadmap
  `3b16cf2cd98c717f6caa38bb4db9f7323fa913c99b1d41310807ee12737650ce`.
- No other TeX section is part of the transport. B0101's specialist HOLD and
  the absence of an insertion after B0104 are preserved.
- The documented fallback compile chain completed with exit 0 because
  `latexmk` is unavailable; `main.pdf` is 11 pages and the final log has no
  warning/error/undefined/overfull/underfull match.

Conclusion: the TeX/code/control transport mirrors only the two authorized
Round 1 operations and adds no reference, new core claim, or declined-item
write.
