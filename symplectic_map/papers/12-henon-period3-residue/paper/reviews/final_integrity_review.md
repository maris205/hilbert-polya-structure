# Paper 12 — Independent Terminal Integrity Review

Date: 2026-08-16 UTC  
Canonical path base: `papers/12-henon-period3-residue`  
Candidate: `henon_period3_residue_proof_note_v1`  
Audit mode: fresh, independent, read-only terminal-integrity verification

## Verdict

- **Terminal-integrity verdict:** `FINAL_INTEGRITY_PASS`
- **Release disposition:** `RELEASE_CONFIRMED`
- **Mismatch count:** `0`
- **Missing binding count:** `0`
- **Unexpected sealed-terminal artifact count:** `0`
- **Scientific or manuscript change performed by this audit:** `NO`

`RELEASE_CONFIRMED` means that the exact local proof-only terminal package is
internally closed, byte-reproducible under its frozen build environment, and
identical to the manuscript and PDF approved by the independent Round-2
review. It is not a target-venue fit judgment, publisher acceptance claim, or
submission authorization. No venue binding was supplied
(`criteria_binding_unavailable`), and the terminal passport continues to state
`submission_authorized: false`.

## Auditor independence and scope boundary

This auditor did not participate in Paper 12's source-lock production,
candidate implementation, asset generation, manuscript drafting, Round-1
revision, Round-1 review, Round-2 review, or terminal finalization. The audit
was restricted to terminal identity, hash closure, history preservation,
isolated LaTeX rebuilds, PDF/package QA, and proof-only scope regression. It
did not re-adjudicate the mathematical proofs.

No candidate module or test module was run or imported. No registered audit,
postrun analyzer, figure generator, or scientific computation was run. No
network access was used. Forbidden runtime and registered-candidate material
was used only as named path/digest/inventory provenance; it was not consumed as
scientific evidence. No external or cross-model review was configured or
performed.

The only project write made by this audit is this report. Its SHA-256 is an
external write-after-completion receipt and is intentionally not embedded in
the report itself.

## Independent release gate

| Sealed input | SHA-256 | Result |
|---|---|---|
| `paper/reviews/round2_review.md` | `f56ff399b120e5fb9729e51b4d52dcde64df954fb064f32319998d678c3c0577` | `PASS / MAY_FINALIZE`; zero Critical, Major, Minor, or residual findings |
| `paper/manuscript.tex` | `5c3b09a835aa41f35899f3c720982f911acf7046559c8433f38ab38ce61a0447` | exact Round-2-approved source |
| `paper/paper_round1_revision.pdf` | `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375` | exact approved revision PDF |
| `paper/manuscript.pdf` | `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375` | byte-identical |
| `paper/paper_final.pdf` | `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375` | byte-identical terminal copy |

All three PDF files are regular files of 530,071 bytes and are byte-identical.
The final PDF therefore carries exactly the scientific and visual content that
Round 2 approved; terminalization did not alter it.

## Strict JSON and hash-binding audit

All 19 JSON files below `paper/`, together with the two explicitly allowed
experiment authorities `experiments/source_lock.json` and
`experiments/proof_only_manuscript_lock.json`, were parsed with duplicate-key
rejection and non-finite-constant rejection. Result: `21/21 PASS`.

A recursive audit of the four terminal JSON base nodes and terminal pipeline
state found 49 unique explicit path/SHA-256 bindings. Every named path exists,
and all 49 recomputed digests match. The audit includes approved source/PDFs,
R0/R1 history, proof-only authorities, asset authorities, the two frozen
runtime-provenance receipts, and the four terminal base nodes.

The six sealed terminal metadata digests recompute as:

| DAG role | Path | SHA-256 |
|---|---|---|
| base | `paper/PAPER_CONFIGURATION_FINAL.md` | `340b1a2397c118a3095a905098fc4bedc52bc9a58717412c9e396c85aafd00e2` |
| base | `paper/CLAIM_MANIFEST_FINAL.json` | `71ffb0a7009731d166b063184afaff4067f04a4360c7f4e54f619d0bc58ba310` |
| base | `paper/PROOF_ONLY_PASSPORT_FINAL.json` | `ba7eaf0cd305e1f39c57dfa990915e2238ba218167239e620c5ad7d8a60211ab` |
| base | `paper/FIGURE_PACKAGE_FINAL.json` | `5aedd6e2430f13a767001fdd26d4e54a6254b671ac4af42ddb2b6a4446ee4048` |
| state | `paper/PIPELINE_STATE_FINAL.json` | `13fa2e20c6177393386e53584841f8778f7864a7e513475fc45fa6cab809b425` |
| integrity | `paper/FINAL_INTEGRITY.md` | `7dc99f6024d7ab6f53949290ebbd4b57dec8c9d255dc8c94ab86abf7b72856be` |

The DAG and self-exclusion checks pass:

- every base node contains no path or digest for any new terminal metadata
  node and contains no self-digest;
- the pipeline node binds exactly the four base nodes, contains neither its
  own digest nor the final-integrity digest, and does not depend on the
  final-integrity node;
- `FINAL_INTEGRITY.md` binds the four base nodes and pipeline node but contains
  no self-digest;
- none of the six nodes contains its own recomputed digest.

Before this post-terminal audit report was written, the exact terminal
mutation inventory was the terminal PDF plus those six metadata nodes—seven
files total. No other top-level `FINAL`/`final` terminal variant was present.
There is no symbolic link anywhere in the Paper 12 project tree. This audit
report is a separately authorized post-terminal review artifact and is not a
member of the sealed terminal DAG.

## Preserved-history audit

Every frozen R0/R1/review digest recorded by the terminal state and integrity
record was recomputed and matched. This includes:

- R0 metadata/passport/claim/figure/plagiarism/pipeline/author/integrity nodes;
- Round-0 source snapshot
  `de706b358a6b1fdec47da2ab88704ab8011ed22a1dd7de560b8912d0c845a617`
  and pre-review PDF
  `bb3cd34efbff6ec3c2bc2803b0c68b30b701d79833d5a9b4eebeb68d101da949`;
- Round-1 review
  `a7fcbb957ecb285dd9d5fb7d1adf5b5b1237a20108b2d01ac468191f72b80f9c`,
  response
  `e1fbdbb2b9beafdbc956351c98935088d6b02966e772216fd5ec92a82bd48531`,
  patch
  `9a7c526d9bba02b1ccb241f6c28a2412ee34b73b333cde97750fb38335b49a05`,
  apply report
  `5c133824a94a4e8e8d15e6260e458972e505fa143beacdac8ffba0320928a533`,
  revision manifest
  `858dad0bec9a53b4365698bf7c671dffeccb9d27e865850763da151cdeb7badf`,
  pipeline state
  `aac89881de74526db9c81f425a84004f2b036e987dccf06016554d4aeb1fb96e`,
  and integrity record
  `186b75544f8204e3416aea44b089f25563c899c9d1c819b7a9473e1ec0c1a9f9`.

The proof, bibliography, citation, and asset authorities also close exactly.
In particular, `notes/PROOF_PACKAGE.md` is
`36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9`,
`paper/references.bib` is
`f1b6fe0807e33debf87c8be19e1b81b2a4a10f886fd9f4ae1d20bf264e978adc`,
the asset tree is
`a5006ef63be3bcc585567276f05f063fd6786c6170081e0eea8ec0ca128598ee`,
and the figure manifest is
`3adc970996ea7a6e1dc043a554c88b8007f4fe203aa30a522b0a4663dcb31096`.
All three frozen figure PDFs match their recorded digests and contain zero
raster image objects.

For registered-failure provenance only, the deployment review, durable claim,
and terminal receipt recompute as
`23000b3478e325271be5f06148037c053bd002befe17345d7f532dfb36183f0c`,
`3b7075f7d5b1b3199c213ae34327f2c80c9f03396b5a792c086416ce99d581c0`,
and
`1e0896af17907e41f7028a71c056e02d5f8fb4ddf63d3d033063979e0b1d802d`.
The frozen code manifest reports the expected tree digest
`3c625fd5357bae97a4ee990443b0a59aa79e7f2d82d5986a5b5b2d8769acd521`;
its 33 path/digest entries exactly match the 33-file code-tree inventory and
all 33 constituent file digests. These checks establish preservation only and
do not promote any registered artifact to scientific evidence.

## Two isolated deterministic rebuilds

Two new disposable build trees were created outside the project. Each
contained only the approved `manuscript.tex`, `math_commands.tex`,
`references.bib`, and the three referenced frozen figure PDFs. Neither tree
contained candidate code, tests, runtime material, or preexecution material.

Both were built using the explicit sequence
`pdflatex -> bibtex -> pdflatex -> pdflatex` with:

```text
SOURCE_DATE_EPOCH=1786838400
FORCE_SOURCE_DATE=1
TZ=UTC
LC_ALL=C
```

The two builds and workspace agree byte-for-byte on all six deterministic
outputs:

| Output | Build A | Build B | Workspace |
|---|---|---|---|
| PDF | `9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375` | same | same |
| LOG | `cbbe4b13e6d38a7263956b163572741c7f3fc03621a18222ea5e57b412c7e68c` | same | same |
| BLG | `be7f60aae83be2fe4e5cc3d0d2898fcd73661df5e2333ae4173dc63bb971ad61` | same | same |
| BBL | `ac0ae8c4f0de3188e42f6f0b17775eb1cf90468431b048986ba23caa12dd522a` | same | same |
| AUX | `67a5988dcf5b5359a7933f077ca2a7f92b39f82f5ceb7b8dd23200a935da3824` | same | same |
| OUT | `7b918498371e32fa96c359d8d5fbdf195fa62091df38d36b9b6df9882a9593d1` | same | same |

No fallback build engine, candidate execution, test execution, or network call
was used.

## PDF, bibliography, reference, font, and vector QA

| Check | Recomputed result |
|---|---|
| Page count | 19 |
| PDF structure | all pages parsed/rendered by Ghostscript; unencrypted; no form; no JavaScript; no embedded files |
| Page geometry | letter, 612 x 792 pt, rotation 0 |
| Visible author | `Anonymous` |
| PDF title/subject/keywords/author metadata | blank |
| Unique cited keys | 10; all found in bibliography |
| Bibliography entries | 11 unique; sole unused optional key `BianchiHe2026` |
| Label declarations | 91, all unique |
| Reference uses | 43 over 34 unique targets; 0 missing targets |
| Font records | 38; all embedded, subsetted, and Unicode-mapped |
| Type-3 fonts | 0 |
| Raster image objects in final PDF | 0 |
| Raster image objects in three figure PDFs | 0, 0, 0 |
| LaTeX/package/pdfTeX/BibTeX warnings | 0 |
| Undefined/multiply-defined diagnostics | 0 |
| Overfull/underfull boxes | 0 / 0 |
| LaTeX error/emergency/fatal hits | 0 |
| PDF `??`, `[?]`, or `[VERIFY]` markers | 0 |

`qpdf` was unavailable in the environment. Required structural coverage was
instead obtained from `pdfinfo`, full-document Ghostscript parsing, text
extraction, `pdfdetach`, `pdffonts`, and `pdfimages`; no required check was
left unresolved. The independently approved PDF digest already carries a
19/19 visual QA result, and exact digest identity transfers that result to the
terminal copy without a new scientific or aesthetic judgment.

## Proof-only terminal-scope regression

The final source is exactly the Round-2-approved source, so no terminal source
delta exists. A separate scope regression found:

- claim IDs/statements/statuses C1--C18 and PC1/PC2 are exactly unchanged
  from the pre-review claim manifest; only the terminal wrapper omits the old
  per-claim manuscript-locator field;
- all six nonclaims are byte-semantically unchanged;
- the eight-path proof-only scientific-input allowlist is exactly unchanged;
- `registered_evidence_used` remains `false` and `proof_only` remains `true`;
- universal nonvanishing of `D_m` remains explicitly open in the abstract,
  theorem scope, figure captions, exclusions, and registered-failure
  disclosure;
- bare source/PDF `quad` artifacts: 0 / 0;
- literal D8, D9, E8, or E9 values/labels in source/PDF: 0 / 0;
- the failed registered audit remains explicitly
  `REGISTERED_AUDIT_TERMINAL_FAIL / NO_RERUN / NO_RAW_RESULT / NO_RESULT_PASS`;
- the manuscript states that no scientific mismatch was recorded and that
  this absence is not evidence of agreement; it makes no Q/R agreement,
  result-pass, or computational-certification claim;
- the approximately 0.98 Track-Q endpoint attribution remains labeled a
  forensic inference with lost child stderr, not an observed traceback or
  theorem input;
- no global quartic separator, global cutoff `P(4)=3`, method-novelty,
  historical-priority, or registered-computation claim was introduced.

This is a scope-preservation check, not a fresh proof review. The sole
scientific authority remains the frozen proof package; the registered-failure
lineage remains non-evidentiary provenance.

## Final disposition

Every required terminal identity, strict-JSON, hash-DAG, self-exclusion,
history, inventory, deterministic-build, PDF, citation, reference, font,
vector, diagnostic, and proof-only regression check passed with zero mismatch.
The exact local final package is released under:

`FINAL_INTEGRITY_PASS / RELEASE_CONFIRMED`

No further manuscript, source, science, bibliography, figure, asset, code,
preexecution, result, runtime, lifecycle, or sealed terminal-metadata mutation
is authorized by this review.
