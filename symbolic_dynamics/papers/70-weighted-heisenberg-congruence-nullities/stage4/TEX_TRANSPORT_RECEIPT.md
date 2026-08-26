# TeX Transport Receipt — P70 Round 1

- status: complete
- revision_round: 1
- canonical_markdown_patch: `stage4/REVISION_PATCH.json`
- patch_sha256: `6da1b89099095f91be34459d3ffd77931d2fd79147ca8d304eb117db2e49c6a5`
- apply_report: `stage4/REVISED_DRAFT.md.apply-report.json`
- apply_report_sha256: `b15d5e253e12d9578b03721c32f1ff6af0f7fe415763eb0299174572fbd28d7c`
- revised_markdown_sha256: `c7cf7eafa10fb382f03f203917d4104be2d2a4edca815d5cf8f71164919210ed`
- final_pdf_sha256: `3091437f38faa5ef271fb2185e1c6fa7760e0762a296948c4a2d64fa012e8f9d`

## Transport model

`REVISED_DRAFT.md` is the canonical patch-applied Markdown artifact. The TeX
sources are its publication-build mirror. Each patch operation is mapped below
to its actual post-apply Markdown block ID and the matching TeX location;
executable code and `CONTROL_RESULTS.md` are auxiliary evidence for the
methodology control. This transport neither modifies nor expands the patch,
bundle, author adjudication, or Stage 3 authority.

## Operation-to-source mapping

| Apply op | Roadmap authority | Actual Markdown block IDs | TeX mirror | Auxiliary evidence | Mirror check |
|---:|---|---|---|---|---|
| 0 — `replace_block` B0007 | REV-P70-EIC-W1 | B0007 | `sections/1_introduction.tex`, bounded-contribution lead sentence | none | Both surfaces point forward to the component comparison and call the contributions bounded. |
| 1 — `replace_block` B0008 | REV-P70-EIC-W1 | B0008 | `sections/1_introduction.tex`, three-item contribution list | none | Both surfaces scope the formula to the stated cross-characteristic family and classify the matrix audit as finite regression evidence. |
| 2 — `insert_after` B0047 | REV-P70-R3-W1 | fresh B0072 | `sections/6_phase_diagram_controls.tex`, bounded coding/spectral transfer box | none | Both surfaces state length `ell^3`, proved-nullity dimension, normalized rate-like quantity, zero-eigenvalue geometric multiplicity, and the same explicit unknowns. |
| 3 — `insert_after` B0053 | REV-P70-R1-W1 | fresh B0073 | `sections/6_phase_diagram_controls.tex`, non-split F4/F2 paragraph | `code/verify_weighted_heisenberg.py`; `CONTROL_RESULTS.md`; `stage4/FINAL_CONTROL_RUN.out` | Markdown, TeX, code, and control receipt agree on `mu_3`, the two solution pairs, and gcd degree 2; the run ends in `ALL WEIGHTED HEISENBERG CONTROLS PASS`. |
| 4 — `replace_block` B0056 | REV-P70-EIC-W1 | B0056 plus fresh B0074 and B0075 | `sections/7_scope_declarations.tex`, ownership paragraph, five-row comparison matrix, and bounded residual/HOLD paragraph | verified existing `stage2_5/SOURCE_SEARCH_LEDGER.md` and `references.bib` only | The TeX matrix has the same five components and field/operator/output columns as B0074. B0075 and the TeX tail both keep priority and specialist clearance unresolved. The apply op records `COLLATERAL-AUTH-P70-EIC-over-R2-B0056`. |

The apply report records three touched pre-existing blocks, four fresh blocks,
68 byte-identical preserved blocks, and no structural flag. The declined
REV-P70-R2-W1 item is not cited as write authority; its B0056 overlap is
covered only by `COLLATERAL-AUTH-P70-EIC-over-R2-B0056` for the EIC operation.

## File-level mirror bindings

| File | SHA-256 | Role |
|---|---|---|
| `sections/1_introduction.tex` | `8746a5c2204d1273f2b138554782d9e4cc01b483a83e5bf091c29d4a0f3e1c9f` | B0007/B0008 TeX mirror |
| `sections/6_phase_diagram_controls.tex` | `fb8dc7f6c065a7b87cb7fa14188f5df7a73e35739189d17af1825dbd1f152135` | B0072/B0073 TeX mirror |
| `sections/7_scope_declarations.tex` | `9a2af5318120acf473c37e4c77361f3e7e616a36195766e835be71750dd23d21` | B0056/B0074/B0075 TeX mirror |
| `code/verify_weighted_heisenberg.py` | `88509dd5606f609db4aa28619c19039a59c38c4d1d47eb16fb9dd54c23cd5bc4` | Exact non-split enumeration implementation |
| `CONTROL_RESULTS.md` | `0b33ca5d4201f7775532f857ae18f4e79a64d5b7c27e4292c58f143c5058026f` | Human-readable control and build record |
| `stage4/FINAL_CONTROL_RUN.out` | listed in `FINAL_SHA256SUMS` | Frozen replay output |
| `stage4/FINAL_COMPILE_TRACE.txt` | listed in `FINAL_SHA256SUMS` | TeX build receipt |

## Boundary and invariance checks

- `main.tex` is unchanged from the package `SHA256SUMS` baseline:
  `dee658d7259b0aa69d2255293d87336b54def9c8ed2a47962326e16b3236c984`.
- `references.bib` is unchanged from the package baseline:
  `67a2eafcce1eba789e38f6f6781f441ecf7a2acd083fb05dfe072083c1738ee3`.
  Therefore new references added in Round 1: **0**.
- Frozen Stage 3 bindings remain byte-exact: anchored draft
  `0fa45f796d7cc3cec28313c34d20c3c3ca5a8fabb18d6bbcdf69fb42e7886fe7`,
  block manifest
  `52a2e2672262853285cb52ebb71a680dd88c85a4106788d86bf380a33d1f1713`,
  and roadmap
  `78868ad9061b4da400a50e15e70f7bafa6c476ca74fa7cdd253a9b6a17bbc29e`.
- No TeX section outside the three mapped section files is part of the
  transport. No source beyond the already verified local ledger/bibliography
  was introduced.
- The documented fallback compile chain completed with exit 0 because
  `latexmk` is unavailable; `main.pdf` is 8 pages and the final log has no
  warning/error/undefined/overfull/underfull match.

Conclusion: the TeX/code/control transport mirrors only the five authorized
Round 1 operations. It adds no reference, priority claim, specialist-clearance
claim, or declined-item authority.
