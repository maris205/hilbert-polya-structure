# Response to Independent Manuscript Review — Round 1

Date: 2026-08-15 UTC  
Manuscript: *An Equivariant-Zeta Audit of Cat-Map Centralizer Quotients*  
Round-1 review SHA-256:
`83c6b2ccb48d776f2d23a0ea6423b16504c6f73625b8a85652aad2fa0807da21`  
Round-1 recommendation: `MINOR REVISION`  
Revision state: `READY_FOR_INDEPENDENT_ROUND2`

We thank the reviewer for the careful mathematical and production audit. We
implemented the sole requested item, M1, as four exact manuscript-side wording
replacements. The revision removes project-sequence labels from reader-facing
prose and uses standalone descriptions of the present note, the preceding
centralizer audit, the registered execution, and the frozen upstream audit PDF.
No theorem, formula, qualifier, evidence row, figure, citation, bibliography
entry, source artifact, code artifact, or result was changed.

## Response to M1: internal “Paper 10/11” numbering

**Reviewer comment.** Four occurrences of “Paper 10” or “Paper 11” are
undefined outside the local research sequence and prevent a fully standalone
article.

**Response.** We agree. The preceding centralizer audit is not introduced here
as a newly citable companion article, so we selected neutral standalone wording
rather than adding a reference. The four replacements are:

| Source location | Round-0 wording | Round-1 wording | Rendered page |
|---|---|---|---:|
| Prior-art boundary, line 190 | “Paper 11 neither” | “The present note neither” | 3 |
| Regular-torsor specialization, line 627 | “No Paper-10 candidate or calculation is rerun here” | “No candidate or calculation from that centralizer-quotient audit is rerun here” | 8 |
| Audit limitation, line 1028 | “selected before Paper-11 execution” | “selected before the registered execution” | 15 |
| Provenance table, line 1144 | “upstream Paper-10 final PDF” | “frozen upstream centralizer-audit PDF” | 17 |

The revised reader-facing manuscript contains zero `Paper 10`/`Paper 11`
sequence labels. Internal batch numbering remains only where it belongs in
non-reader provenance artifacts frozen before this review.

**Status:** `RESOLVED`.

## Scope and change-control record

The exact-replacement patch is
`paper/revisions/round1_patch.json`, SHA-256
`94b366f0cb1531a6835f98508969ecc538cdd3e68f15a166a13ab3a396852b40`.
Its application report is
`paper/revisions/round1_apply_report.json`, SHA-256
`dab976a6b6ef4aabe177d22845a1b11590e497185272191f4193fb59e14b6e5c`.
The diff has four removed and four added source lines, with no line-count
change. Mechanically reversing the four replacements reproduces the Round-0
manuscript SHA-256
`88e81b0c91f57eb6b66c81d2c10af6b6ce4f611113383051a50f4e74e7fb67a5`.
A byte-exact Round-0 source snapshot is retained at
`paper/revisions/manuscript_round0.tex` under that digest.

The revised source SHA-256 is
`2a49333745477cd553b97a1e14734484774621ffa7b09e405c25e23073be7958`.
The rendered text changes by five words. No reference, figure, table, equation,
label, or section was added or removed.

The correction does not move any scientific claim along a claim-strength
ladder. In particular, it leaves unchanged the `q=2` factor
`(1-t^3)^(-1)`, its unique locked-row exception status, the family-uniform
quantifier, the collision `r_2=r_4=3`, and the
`A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC` disposition.

## Rebuild and QA

The deterministic build was rerun in the workspace and in two isolated clean
trees. The PDF, terminal log, BLG, BBL, AUX, and outline artifacts are
byte-identical across all three builds.

| Artifact | SHA-256 |
|---|---|
| Revised `paper/manuscript.tex` | `2a49333745477cd553b97a1e14734484774621ffa7b09e405c25e23073be7958` |
| `paper/manuscript.pdf` | `9f9a0a25ba82a56d10980ecafad3be8cc893523fc494e5dd66a9307dd831888b` |
| `paper/paper_round1_revision.pdf` | `9f9a0a25ba82a56d10980ecafad3be8cc893523fc494e5dd66a9307dd831888b` |
| Terminal `manuscript.log` | `36d5b80b76d0e226af83dfbbbe294dbecd8f308d2a78f8f6dbb5b8b083c9cc7b` |
| `manuscript.blg` | `13d7d6e141ace109be09bce9bee17212ac6ecccac082a14ca8ae2d71200b3ef5` |
| `manuscript.bbl` | `617845025a84100f82a10e7c4e5d8068e7493e8f3779f37c32da555b2ace56ca` |
| `manuscript.aux` | `d7b528a949b8b97707d6af793d9c370929b5c731e36bd579b9a714f8a5b807a6` |
| `manuscript.out` | `cd36533f9b25495005a0d2c92a38093d909fe5c9c0d5a4b23d2b353e55a75ec6` |

The revised PDF remains 19 pages. All 19 pages were inspected; the four edited
passages render cleanly on pages 3, 8, 15, and 17. Figures 1--3 remain exact
copies of the frozen LaTeX blocks and appear on pages 4, 12, and 13. Terminal
warnings and errors are zero. Citation closure is 14 of 14; 65 labels and 40
referenced targets close with no missing target. All 39 font records are
embedded, subset, and Unicode-mapped; Type-3 fonts and raster image objects are
zero.

The Round-0 PDF remains unchanged as `paper/paper_pre_review.pdf`, SHA-256
`f0c27ce18c5f20b5192fb341a4960e2ccfbb7fd08727680912e5c1fb853b8e2e`.
The bibliography, three figure PDFs, source lock, candidate, registered
claim/run, raw result, execution tree, analyzer tree, and scope audit retain
their frozen digests.

## Answers to the reviewer’s questions

1. The manuscript uses a neutral “preceding centralizer audit” formulation.
   Adding a public companion-paper title or citation was outside this bounded
   revision and would have changed the frozen citation asset.
2. The specialist-note framing is retained. We did not enlarge the novelty,
   venue, priority, or scientific claims in response to the review.

## Commitment ledger

```yaml
- concern_id: R1-M1
  commitment_extracted:
    - commitment_text: "Replace all four reader-facing Paper 10/11 sequence labels with standalone scholarly wording."
      commitment_type: add_clarification
      required_evidence_type: prose_edit
      fulfillment_status: fulfilled
```

## Round boundary

Round 1 resolves M1 but does not authorize finalization. The revised package is
stopped at `READY_FOR_INDEPENDENT_ROUND2`. No `paper_final.pdf` exists. A fresh,
hash-bound Round-2 reviewer must verify the four standalone replacements and
the regenerated downstream integrity chain.
