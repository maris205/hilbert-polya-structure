# Pre-Review Integrity Record

Date: 2026-08-15 UTC  
Candidate: `cat_equivariant_retention_tradeoff_v1`  
Terminal state: `READY_FOR_FRESH_INDEPENDENT_MANUSCRIPT_REVIEW`

This is the terminal author-side integrity record for the frozen package sent
to a fresh independent manuscript reviewer. It is deliberately downstream of
the package, base manifests, pipeline state, and author production audit. It
does not hash itself, does not represent an independent manuscript verdict,
and does not authorize finalization.

## Integrity root

| Node | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `88e81b0c91f57eb6b66c81d2c10af6b6ce4f611113383051a50f4e74e7fb67a5` |
| `paper/math_commands.tex` | `1a057269cb071f5ba026430174b0d1b9c9651932ff2c8de286f4a8b6164e9a39` |
| `paper/build.sh` | `3526ec2fad377a51620d18318dafdd43b59620ce1b9b95fb8c3e41c544fbd27a` |
| `paper/references.bib` | `d88a3de08479c46174831a7d562405835800822850505f455831925ff06691d7` |
| `paper/manuscript.pdf` | `f0c27ce18c5f20b5192fb341a4960e2ccfbb7fd08727680912e5c1fb853b8e2e` |
| `paper/paper_pre_review.pdf` | `f0c27ce18c5f20b5192fb341a4960e2ccfbb7fd08727680912e5c1fb853b8e2e` |
| `paper/PAPER_CONFIGURATION.md` | `82a9402967537fe61ad49d081e02be5803207bb42bd4a0f6387f9d2c4f27d90c` |
| `paper/CLAIM_MANIFEST.json` | `c452d77404bd78482ed0be54d1f6a3f4736ca5220cf22c8a52c4e98143ea4bc9` |
| `paper/EXPERIMENT_PASSPORT.json` | `631b1102894d72cf608d53a7b96a7e7baf41fe0d5f638225ebe7876d52604f36` |
| `paper/FIGURE_PACKAGE.json` | `f310441a3df42cc70583ee09ab5b971b332f0c873f685e17e2c69bb143e39131` |
| `paper/PLAGIARISM_MANIFEST.json` | `a5e44ea401d1e3c52e9489dc0b2738b1d4cbbc89ea2073f90515ed53a58ba5dc` |
| `paper/PIPELINE_STATE.json` | `8f55bd719f12c2a9cf1dcd83669a6972f80f2f279a58137c9df26100aee86af0` |
| `paper/AUTHOR_PRE_REVIEW_AUDIT.md` | `9ff04282ba92caf1106fa38cc51adecb039007d05691c4601560f3d0017cce40` |

All four JSON manifests and the pipeline-state JSON parse successfully. The
review PDF and workspace manuscript PDF are byte-identical. No
`paper_final.pdf` is present.

## Frozen evidence and independent upstream gates

| Authority | SHA-256 | Bound status |
|---|---|---|
| Source lock v2 | `331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b` | immutable |
| Source rereview | `2f75d6934e3d61bdc941ee6689102a1cb08a959270a7cd87965579f1ec5cc622` | `SOURCE_LOCK_PASS` |
| Proof/formula package | `3d723fdb02c89f9b2f281da807bcd745c5991393d25e223f95d6673961c20948` | immutable; publication quantifier corrected |
| Claims/evidence matrix | `0ea191ebb1f6f0f915db096a68606099d4a315d80d333adadd3e396b11885490` | immutable |
| Raw result | `bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe` | immutable |
| Result review | `c91737c8bf860bd559eebebe08420fc5d095800c47d132381f584e918e714a20` | `RESULT_PASS` |
| Execution tree | `5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb` | immutable |
| Analyzer tree | `423082f4675a1d41622bcb3d090a2c4c67d4732ff6dc32d0298505d90d5a78c3` | immutable |
| Analyzer review | `ba63afc8c88903f15ec6ac5d82f0cd65430710ca9c132b489a7cd4f70e7660a8` | `ANALYZER_PASS` |
| Strict result manifest | `a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c` | pass |
| Scope audit | `f7b365c9e6c8933cf3cbcaf3c96692cbacdaabcc84400bdc629f1d482cb243e4` | `PASS_WITH_SCOPE_CORRECTION` |
| Paper plan | `9a6ebb212e175775673e97bfc8b5eb18a2e8f760c756cdfc21583b0fb296124c` | frozen |
| Citation verification | `29681de3379801d1f376ecaa3b3cfc0d366964666852bff8b08faaf3cd67d3ca` | frozen |
| Figure manifest | `e3a8d1d36ba8c4959b080a9661b242c40195ea08d27690fc8ee899b487cfd6dc` | frozen |
| Asset tree | `95bb23519a427ef6a73a6a04b1aef6861aa4c5e4f6b844e7866bf9c43e52b28c` | frozen |
| Asset review | `ebf1644dc03da4c1ccc03972b545688d595ed6da125de2ec831ffcf82e4e69cf` | `ASSET_PASS` |

The manuscript binds the independent scope correction: the locked `q=2`
point-cardinality factor `(1-t^3)^(-1)` is the unique local exception, the
negative conclusion is uniform only across all nine locked rows, and the
collision `r_2=r_4=3` rules out reading that exception as a modulus-specific
clock. The resulting A0 classification is
`A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC`, not a claim that every local scalar
factor fails.

## Figure and bibliography identities

The frozen LaTeX include contract has SHA-256
`bad78636f7e25f94a2d2cae50f299e4b7a46feb1ad890526a1128ae5d554671b`.
The three exact manuscript blocks occur in contract order. Their publication
PDF identities are:

| Figure | Label | PDF SHA-256 | Page |
|---|---|---|---|
| 1 | `fig:retention-hierarchy` | `f80ea5a21d46f7b419196689b96127efc37e842fc21b890b28a02f02a722c525` | 4 |
| 2 | `fig:nine-row-retention` | `9525b8c11d7da9fe00409bebc591d1d792867176e8a7e764c95bbbabafeba329` | 12 |
| 3 | `fig:effectivity-counterexamples` | `aaef94b667ede3c309044f28be9c029ab2435b5a5d77031e292ed0dc257c8c5b` | 13 |

The bibliography is the independently gated publication-layer asset. The
Walton entry uses DOI `10.1016/j.jnt.2018.03.023` and *Journal of Number
Theory* 192 (2018), 386--405. The frozen design-side typo is retained in its
immutable provenance source; this bibliographic correction changes no
scientific claim.

## Reproducibility and QA closure

The workspace build and two isolated clean builds are byte-identical for all
six compared artifacts:

| Artifact | SHA-256 |
|---|---|
| PDF | `f0c27ce18c5f20b5192fb341a4960e2ccfbb7fd08727680912e5c1fb853b8e2e` |
| LOG | `89adf923399cb2257d58470c8e2e08514205d0b8389833fa2e8e6c99799a2b1c` |
| BLG | `13d7d6e141ace109be09bce9bee17212ac6ecccac082a14ca8ae2d71200b3ef5` |
| BBL | `617845025a84100f82a10e7c4e5d8068e7493e8f3779f37c32da555b2ace56ca` |
| AUX | `d7b528a949b8b97707d6af793d9c370929b5c731e36bd579b9a714f8a5b807a6` |
| OUT | `cd36533f9b25495005a0d2c92a38093d909fe5c9c0d5a4b23d2b353e55a75ec6` |

Closed checks:

- 19 of 19 integrated pages inspected at original rendered resolution;
- zero LaTeX/package, BibTeX, citation, reference, overfull, or underfull
  warnings;
- 65 labels, 40 referenced targets, zero missing target;
- 14 cited keys, 14 bibliography entries, zero missing or unused key;
- 39 embedded/subset/Unicode-mapped fonts, zero Type-3 font;
- zero raster image objects;
- exact 9-of-9 row transcription and 36-of-36 scalar-cell transcription;
- zero forbidden stronger theorem-scope hit;
- zero reader-facing numeric novelty-score hit;
- zero local 12-word-shingle overlap against Papers 1--10 and the proposal,
  with the explicit boundary that this is only a project-local heuristic.

## Acyclic provenance graph

The binding direction is:

`frozen evidence + independent upstream gates + frozen assets`

`-> manuscript sources + bibliography + figures`

`-> deterministic PDF + build artifacts`

`-> base pre-review manifests`

`-> PIPELINE_STATE.json`

`-> AUTHOR_PRE_REVIEW_AUDIT.md`

`-> INTEGRITY_PRE_REVIEW.md`.

The terminal record contains no digest for itself. Neither the pipeline-state
node nor the author-audit node points forward. This preserves a verifiable,
acyclic pre-review chain.

## Release boundary

- `ready_for_fresh_independent_manuscript_review`: `true`
- `independent_manuscript_review_completed`: `false`
- `finalization_authorized`: `false`
- `final_pdf_created`: `false`

The package must now stop for a fresh independent manuscript review. Any later
change to a bound file invalidates this record and requires downstream hashes
and QA to be regenerated; final release remains prohibited until an authorized
independent review supplies the next gate.
