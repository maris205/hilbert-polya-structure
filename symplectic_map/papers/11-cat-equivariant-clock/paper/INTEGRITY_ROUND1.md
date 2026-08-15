# Round-1 Revision Integrity Record

Date: 2026-08-15 UTC  
Candidate: `cat_equivariant_retention_tradeoff_v1`  
State: `READY_FOR_INDEPENDENT_ROUND2`

This is the terminal author-side integrity record for the Round-1 revision.
It is not a Round-2 review, an acceptance decision, or authorization to
finalize. No `paper_final.pdf` exists.

## Round chain

| Node | SHA-256 |
|---|---|
| Round-0 `paper/INTEGRITY_PRE_REVIEW.md` | `4e82724bdee00b1c31858585c6cd1008106b818ef7cef849661767fbdb1a300f` |
| Independent `paper/reviews/round1_review.md` | `83c6b2ccb48d776f2d23a0ea6423b16504c6f73625b8a85652aad2fa0807da21` |
| Round-0 source snapshot `paper/revisions/manuscript_round0.tex` | `88e81b0c91f57eb6b66c81d2c10af6b6ce4f611113383051a50f4e74e7fb67a5` |
| Exact patch `paper/revisions/round1_patch.json` | `94b366f0cb1531a6835f98508969ecc538cdd3e68f15a166a13ab3a396852b40` |
| Apply report `paper/revisions/round1_apply_report.json` | `dab976a6b6ef4aabe177d22845a1b11590e497185272191f4193fb59e14b6e5c` |
| Author response `paper/reviews/round1_response.md` | `b74d88f2cec9b8d0655c0ec752441a6ad8d19ee31111dc7c65da9b8842df2869` |
| `paper/ROUND1_REVISION_MANIFEST.json` | `5ed605c633038ecf0a89f03d0512f84fbb16a29744734127cd7a8df5b13a2df3` |
| `paper/PIPELINE_STATE_ROUND1.json` | `a17f4eb2e497ba09b754a259e96398fb0d1d03c5f2a25c5a15dec7f33bff7230` |

Both revision JSON sidecars, the Round-1 revision manifest, and the Round-1
pipeline state parse successfully. The graph is acyclic: this record binds the
pipeline state but contains no digest for itself.

## Revised package

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `2a49333745477cd553b97a1e14734484774621ffa7b09e405c25e23073be7958` |
| `paper/manuscript.pdf` | `9f9a0a25ba82a56d10980ecafad3be8cc893523fc494e5dd66a9307dd831888b` |
| `paper/paper_round1_revision.pdf` | `9f9a0a25ba82a56d10980ecafad3be8cc893523fc494e5dd66a9307dd831888b` |
| `paper/math_commands.tex` | `1a057269cb071f5ba026430174b0d1b9c9651932ff2c8de286f4a8b6164e9a39` |
| `paper/build.sh` | `3526ec2fad377a51620d18318dafdd43b59620ce1b9b95fb8c3e41c544fbd27a` |
| `paper/references.bib` | `d88a3de08479c46174831a7d562405835800822850505f455831925ff06691d7` |
| `paper/manuscript.log` | `36d5b80b76d0e226af83dfbbbe294dbecd8f308d2a78f8f6dbb5b8b083c9cc7b` |
| `paper/manuscript.blg` | `13d7d6e141ace109be09bce9bee17212ac6ecccac082a14ca8ae2d71200b3ef5` |
| `paper/manuscript.bbl` | `617845025a84100f82a10e7c4e5d8068e7493e8f3779f37c32da555b2ace56ca` |
| `paper/manuscript.aux` | `d7b528a949b8b97707d6af793d9c370929b5c731e36bd579b9a714f8a5b807a6` |
| `paper/manuscript.out` | `cd36533f9b25495005a0d2c92a38093d909fe5c9c0d5a4b23d2b353e55a75ec6` |

The Round-0 review PDF remains byte-preserved at
`paper/paper_pre_review.pdf`, SHA-256
`f0c27ce18c5f20b5192fb341a4960e2ccfbb7fd08727680912e5c1fb853b8e2e`.

## M1 closure and scientific-drift guard

The only revision item was `R1-M1`. Four reader-facing project labels were
replaced with standalone wording. The exact diff contains four removed and
four added lines, leaves the 1238-line source count unchanged, and reverses to
the Round-0 source digest. The revised manuscript has zero reader-facing
`Paper 10`/`Paper 11` hit.

No scientific statement changed. The `q=2` point-cardinality factor
`(1-t^3)^(-1)`, its unique locked exception status, the family-uniform
quantifier, `r_2=r_4=3`, and the
`A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC` disposition remain explicit. A scan for
the forbidden stronger quantifier found no regression.

No source lock, candidate, registered claim/run, raw result, execution tree,
analyzer tree, scope audit, figure, or bibliography artifact changed. The
three frozen figure PDFs retain SHA-256 digests
`f80ea5a21d46f7b419196689b96127efc37e842fc21b890b28a02f02a722c525`,
`9525b8c11d7da9fe00409bebc591d1d792867176e8a7e764c95bbbabafeba329`,
and
`aaef94b667ede3c309044f28be9c029ab2435b5a5d77031e292ed0dc257c8c5b`.

## Build and QA closure

- The workspace and two isolated clean builds are byte-identical for PDF,
  LOG, BLG, BBL, AUX, and OUT.
- The revised PDF is 19 pages; all 19 pages were visually inspected.
- The four edited passages render cleanly on pages 3, 8, 15, and 17.
- Figures 1--3 remain exact frozen blocks on pages 4, 12, and 13.
- LaTeX/package, BibTeX, citation, reference, overfull, and underfull warning
  or error hits are zero.
- Citation closure is 14 cited keys against 14 bibliography entries, with no
  missing or unused key.
- All 65 labels and 40 referenced targets close, with no duplicate or missing
  target.
- All 39 font records are embedded, subset, and Unicode-mapped; Type-3 fonts
  and raster image objects are zero.
- The DOI-authoritative Walton metadata remain unchanged.
- A project-local 12-word-shingle rerun has 6442 target shingles and zero
  overlap against Papers 1--10 and the proposal; this is not an external
  plagiarism certificate.

## Acyclic binding direction and stop condition

`Round-0 integrity -> independent Round-1 review -> exact patch/apply ->`
`revised source/PDF + response -> Round-1 revision manifest -> Round-1`
`pipeline state -> this integrity record`.

- `ready_for_independent_round2`: `true`
- `independent_round2_review_completed`: `false`
- `finalization_authorized`: `false`
- `final_pdf_created`: `false`

The package must stop for a fresh, hash-bound independent Round-2 review. Any
later change to a bound file invalidates this record and requires regeneration
of the downstream chain.
