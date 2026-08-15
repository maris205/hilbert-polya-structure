# Terminal Final Integrity Record

Date: 2026-08-15 UTC  
Candidate: `cat_equivariant_retention_tradeoff_v1`  
Status: `COMPLETE_LOCAL_FINAL_REVIEW_PASS`

This record seals a purely mechanical terminal finalization after a fresh
independent Round-2 `PASS / MAY_FINALIZE`. It introduces no manuscript,
bibliography, figure, source, code, result, test, theorem-scope, citation-
evidence, or scientific change. The terminal graph is acyclic: four base
terminal manifests feed the terminal pipeline state, which feeds this final
integrity record. This record contains no digest for itself.

## Independent release gate

| Node | Path | SHA-256 | Disposition |
|---|---|---|---|
| Round-2 review | `paper/reviews/round2_review.md` | `093f79564578370992c5e74e7925cd46a07ed00c7abc3561d907d0f12f69a0e0` | `ACCEPT`; `PASS / MAY_FINALIZE` |
| Approved source | `paper/manuscript.tex` | `2a49333745477cd553b97a1e14734484774621ffa7b09e405c25e23073be7958` | exact review-bound identity |
| Approved revision PDF | `paper/paper_round1_revision.pdf` | `9f9a0a25ba82a56d10980ecafad3be8cc893523fc494e5dd66a9307dd831888b` | 19 pages |
| Terminal final PDF | `paper/paper_final.pdf` | `9f9a0a25ba82a56d10980ecafad3be8cc893523fc494e5dd66a9307dd831888b` | byte-identical copy |
| Live manuscript PDF | `paper/manuscript.pdf` | `9f9a0a25ba82a56d10980ecafad3be8cc893523fc494e5dd66a9307dd831888b` | byte-identical |

All three PDF files are byte-identical. No PDF bytes were regenerated or
altered during final copying.

## Terminal metadata chain

The base layer contains no reference to another new terminal metadata node
and no self-hash. The pipeline state binds all four base nodes. This record
binds the pipeline state and base nodes and does not hash itself.

| Layer | Path | SHA-256 |
|---|---|---|
| base | `paper/PAPER_CONFIGURATION_FINAL.md` | `569075fed19c49106fc9b59b30274683b58ae9ee53bc5452ef1aed3b6c78e9c5` |
| base | `paper/CLAIM_MANIFEST_FINAL.json` | `b4d714997f468f69933ce1c16aaa8193e54746388fed0080e062b832e10ae72a` |
| base | `paper/EXPERIMENT_PASSPORT_FINAL.json` | `79f19bd78304f891ccb54a219ca91e79e31d30b5082977a7a3877ab0b7df7220` |
| base | `paper/FIGURE_PACKAGE_FINAL.json` | `3e5c2ea6f465c4fafe95bbfae08de323565a394376b2d39f8b93b10e27769297` |
| state | `paper/PIPELINE_STATE_FINAL.json` | `14f396b3c668b8b0fada7d3fdfa305656609bf859f80801d965c9e8b60eadf8c` |

Every terminal JSON file parses under duplicate-key rejection and rejects
non-finite constants. Before this record was written, all 23 JSON files in
the project tree passed that strict parse. The five pre-integrity terminal
metadata nodes were exactly the expected inventory; this record is the sixth
and final terminal metadata node.

## Preserved R0/R1 history

The following historical files were rehashed after terminal sealing and are
unchanged:

| Historical node | SHA-256 |
|---|---|
| `paper/PAPER_CONFIGURATION.md` | `82a9402967537fe61ad49d081e02be5803207bb42bd4a0f6387f9d2c4f27d90c` |
| `paper/CLAIM_MANIFEST.json` | `c452d77404bd78482ed0be54d1f6a3f4736ca5220cf22c8a52c4e98143ea4bc9` |
| `paper/EXPERIMENT_PASSPORT.json` | `631b1102894d72cf608d53a7b96a7e7baf41fe0d5f638225ebe7876d52604f36` |
| `paper/FIGURE_PACKAGE.json` | `f310441a3df42cc70583ee09ab5b971b332f0c873f685e17e2c69bb143e39131` |
| `paper/PIPELINE_STATE.json` | `8f55bd719f12c2a9cf1dcd83669a6972f80f2f279a58137c9df26100aee86af0` |
| `paper/INTEGRITY_PRE_REVIEW.md` | `4e82724bdee00b1c31858585c6cd1008106b818ef7cef849661767fbdb1a300f` |
| `paper/ROUND1_REVISION_MANIFEST.json` | `5ed605c633038ecf0a89f03d0512f84fbb16a29744734127cd7a8df5b13a2df3` |
| `paper/PIPELINE_STATE_ROUND1.json` | `a17f4eb2e497ba09b754a259e96398fb0d1d03c5f2a25c5a15dec7f33bff7230` |
| `paper/INTEGRITY_ROUND1.md` | `7b61e118f2e63530226095bc1a9a79a9e8f219d24e08342727f0a3734eedc223` |

The independent Round-1 review remains
`83c6b2ccb48d776f2d23a0ea6423b16504c6f73625b8a85652aad2fa0807da21`,
and its response remains
`b74d88f2cec9b8d0655c0ec752441a6ad8d19ee31111dc7c65da9b8842df2869`.
The preserved Round-0 source snapshot and pre-review PDF remain
`88e81b0c91f57eb6b66c81d2c10af6b6ce4f611113383051a50f4e74e7fb67a5`
and
`f0c27ce18c5f20b5192fb341a4960e2ccfbb7fd08727680912e5c1fb853b8e2e`.

## Frozen scientific, result, and scope closure

| Authority | Path or role | SHA-256 | Verdict/boundary |
|---|---|---|---|
| source lock | `experiments/source_lock.json` | `331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b` | frozen |
| source rereview | `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md` | `2f75d6934e3d61bdc941ee6689102a1cb08a959270a7cd87965579f1ec5cc622` | `SOURCE_LOCK_PASS` |
| proof package | `notes/PROOF_PACKAGE.md` | `3d723fdb02c89f9b2f281da807bcd745c5991393d25e223f95d6673961c20948` | formulas frozen; overstrong prose superseded by scope audit |
| claims/evidence matrix | `notes/CLAIMS_EVIDENCE_MATRIX.md` | `0ea191ebb1f6f0f915db096a68606099d4a315d80d333adadd3e396b11885490` | frozen |
| raw result | `results/EXPERIMENT_RESULTS.json` | `bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe` | exact nine-row ledger plus typed control |
| strict result manifest | `results/result_manifest.json` | `a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c` | `PASS` |
| independent result review | `results/INDEPENDENT_RESULT_INTEGRITY.md` | `c91737c8bf860bd559eebebe08420fc5d095800c47d132381f584e918e714a20` | `RESULT_PASS` |
| immutable execution tree | registered authority | `5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb` | 36 closed paths |
| separate analyzer tree | validator-only authority | `423082f4675a1d41622bcb3d090a2c4c67d4732ff6dc32d0298505d90d5a78c3` | 12 closed paths |
| analyzer review | `results/POSTRUN_ANALYZER_REVIEW.md` | `ba63afc8c88903f15ec6ac5d82f0cd65430710ca9c132b489a7cd4f70e7660a8` | `ANALYZER_PASS` |
| theorem-scope audit | `notes/INDEPENDENT_POSTRUN_SCOPE_AUDIT.md` | `f7b365c9e6c8933cf3cbcaf3c96692cbacdaabcc84400bdc629f1d482cb243e4` | `PASS_WITH_SCOPE_CORRECTION` |

The scope correction remains explicit in source and rendered PDF:

- the locked `q=2` point-cardinality factor is `(1-t^3)^(-1)`;
- it is the sole locked row/type source-support/unit-exponent exception;
- no one scalar-reduction type works uniformly across all nine locked rows;
- `r_2=r_4=3` prevents modulus specificity;
- A0 means failure to obtain a common intrinsic modulus/prime clock, not
  absence of every local one-cycle factor.

The deterministic forbidden-stronger-claim scan returned zero hits. The
reader-facing source and PDF contain zero `Paper 10`/`Paper 11` internal
sequence label. No new zeta/stack theorem, universal no-go, priority, or
numeric novelty claim was introduced.

## Frozen bibliography and figure assets

The bibliography remains
`d88a3de08479c46174831a7d562405835800822850505f455831925ff06691d7`.
The publication-layer Walton record remains *Journal of Number Theory* 192
(2018), 386--405, DOI `10.1016/j.jnt.2018.03.023`; the frozen design-side
transcription is unchanged provenance and no scientific inference is drawn
from its correction.

| Asset authority | SHA-256 |
|---|---|
| independent asset review (`ASSET_PASS`) | `ebf1644dc03da4c1ccc03972b545688d595ed6da125de2ec831ffcf82e4e69cf` |
| paper plan | `9a6ebb212e175775673e97bfc8b5eb18a2e8f760c756cdfc21583b0fb296124c` |
| citation verification | `29681de3379801d1f376ecaa3b3cfc0d366964666852bff8b08faaf3cd67d3ca` |
| figure manifest | `e3a8d1d36ba8c4959b080a9661b242c40195ea08d27690fc8ee899b487cfd6dc` |
| 25-path asset tree | `95bb23519a427ef6a73a6a04b1aef6861aa4c5e4f6b844e7866bf9c43e52b28c` |
| LaTeX includes contract | `bad78636f7e25f94a2d2cae50f299e4b7a46feb1ad890526a1128ae5d554671b` |
| determinism audit | `3f5f3dcd6fd9f2ffa6782b2d383f6e4d4178e74709b1ceb384f91c99957325ea` |
| figure QA | `f3188fd4511bdf513bdfe9c79e7833ed324f07579c125c31fe82f91492418e7c` |
| provenance | `9efeae7cd81e4e3d548609f5b019e3cace99781de28f11020a1e49ee5180fdc8` |
| trace | `a66e8302b085091faec02fb50165a300506aa29b176de731af4b4797db218d1b` |

The three integrated vector PDF identities remain:

1. Figure 1:
   `f80ea5a21d46f7b419196689b96127efc37e842fc21b890b28a02f02a722c525`;
2. Figure 2:
   `9525b8c11d7da9fe00409bebc591d1d792867176e8a7e764c95bbbabafeba329`;
3. Figure 3:
   `aaef94b667ede3c309044f28be9c029ab2435b5a5d77031e292ed0dc257c8c5b`.

They appear on pages 4, 12, and 13, respectively. No asset was regenerated
or changed.

## Deterministic terminal rebuild

Two new isolated clean builds were created only after the Round-2, source,
PDF, bibliography, and figure identities passed their preflight gate. Both
builds exited successfully and reproduced every approved deterministic
artifact byte for byte:

| Artifact | Build A | Build B | Approved workspace |
|---|---|---|---|
| PDF | `9f9a0a25ba82a56d10980ecafad3be8cc893523fc494e5dd66a9307dd831888b` | same | same |
| LOG | `36d5b80b76d0e226af83dfbbbe294dbecd8f308d2a78f8f6dbb5b8b083c9cc7b` | same | same |
| BLG | `13d7d6e141ace109be09bce9bee17212ac6ecccac082a14ca8ae2d71200b3ef5` | same | same |
| BBL | `617845025a84100f82a10e7c4e5d8068e7493e8f3779f37c32da555b2ace56ca` | same | same |
| AUX | `d7b528a949b8b97707d6af793d9c370929b5c731e36bd579b9a714f8a5b807a6` | same | same |
| OUT | `cd36533f9b25495005a0d2c92a38093d909fe5c9c0d5a4b23d2b353e55a75ec6` | same | same |

No candidate, registered audit, test suite, analyzer, independent verifier,
figure generator, or scientific computation was run. No network access was
used.

## PDF, citation, font, vector, and visual QA

- PDF: 19 pages, letter size, unencrypted, no JavaScript or form.
- Visual: every page 1--19 was rendered at original page aspect and inspected
  after terminal copying; all text, equations, tables, captions, figures,
  footnotes, appendices, declarations, and references are clean, with no
  clipping, overlap, missing glyph, broken link text, or unreadable annotation.
- Figures: frozen vector PDFs on pages 4, 12, and 13; raster image objects 0.
- Fonts: 39 records; 39 embedded, 39 subset, 39 Unicode-mapped; Type-3 fonts 0.
- Build diagnostics: LaTeX/package warnings 0, BibTeX warnings 0,
  overfull/underfull boxes 0, undefined citations/references 0, multiply
  defined labels 0, terminal errors 0.
- Citations: 14 unique cited keys and 14 unique bibliography entries; missing
  keys 0, unused entries 0.
- Cross-references: 65 labels, all unique; 40 referenced targets; missing
  targets 0.
- Metadata: anonymous author, appropriate title/subject/keywords, no custom
  metadata stream or identifying local path.
- Inventory: expected terminal files present, no unexpected terminal variant,
  no symlink in the project tree, and all explicit terminal path/hash bindings
  close.

## Terminal disposition

The only authorized terminal mutation was creation of a byte-identical
`paper_final.pdf` and the six explicitly terminal-versioned metadata nodes.
All R0/R1 history remains immutable. The terminal status is exactly:

`COMPLETE_LOCAL_FINAL_REVIEW_PASS`

No further local manuscript, science, source, code, result, bibliography,
figure, scope, citation-evidence, or lifecycle mutation is authorized under
this completed run.
