# Response to Independent Manuscript Review — Round 1

Response date: 2026-08-14 UTC  
Candidate: `cat_torsion_primitive_divisor_capacity_v1`  
Round-1 review: `MINOR REVISION`, 3 bounded findings  
Revision status: **3/3 IMPLEMENTED; AUTHOR VERIFIED; AWAITING INDEPENDENT ROUND 2**

This response is deliberately limited to M1--M3 in
`paper/reviews/round1_review.md`. No theorem conclusion, frozen proof,
source lock, candidate code, raw result, result manifest, official report,
registered period, route status, or figure changed. The candidate was not
run, no period was added, and no external prime/zero data or network lookup
was used.

## M1 — signed unstable eigenvalue notation

**Request.** Replace the general expression `n log alpha` by a quantity that
is real and sign-independent for negative-trace hyperbolic matrices.

**Implemented.** In the proof and immediate comparison paragraph of
Theorem 5.1, the revised manuscript now defines `rho(A)>1` as the spectral
radius and states that the logarithm of the modulus of the unstable
multiplier is `n log rho(A)` (`paper/manuscript.tex:557--564`). The same
general notation is used in `PAPER_PLAN.md`; no stale general
`n log alpha` remains in manuscript, caption, claim, or current planning
surfaces.

The frozen standard-cat proof/result documents were not edited. Their
positive quantity `alpha=(3+sqrt(5))/2` belongs to the fixed positive-trace
cat matrix and is consistent with `rho(A)` in that restricted setting.

## M2 — direct ordinary-period literature bridge

**Request.** Cite the directly relevant ordinary-period baseline and keep it
separate from the prime-additive-order theorem.

**Implemented.** A single bounded paragraph was added at
`paper/manuscript.tex:87--92`:

- Kannan, Subramania Pillai, Ali Akbar, and Sankararao (2011) support only
  the statement that the ordinary period set of a hyperbolic two-torus
  automorphism is `N` or `N\{2}`;
- Seibt (2003) supports only rational-lattice/global period-formula context;
- the manuscript explicitly says that neither source imposes prime additive
  order or proves the cross-prime carrier theorem.

Both entries were already recorded with their allowed roles in the local
novelty evidence. Their metadata were transferred to
`paper/references.bib` and recorded source-by-source in
`notes/CITATION_VERIFICATION.md`. No new online search was performed.

## M3 — citation-ledger and release-state closure

**Request.** Reconcile the citation ledger's stale unchecked terminal item
with the compiled bibliography and bind the revised hashes.

**Implemented.** The ledger now records
`ROUND-1 BOUNDED CITATION CLOSURE: PASS AUTHOR SIDE / AWAITING INDEPENDENT
ROUND 2`, identifies the two locally verified additions, records the revised
bibliography hash, and closes every checklist item. It states explicitly
that URL re-resolution was not repeated during Round 1 and that the verified
2026-08-14 cutoff is retained. The revised manuscript cites 14 unique keys,
the bibliography contains exactly the same 14 entries, and BibTeX reports
zero warning.

## Regression and production checks

- Two clean deterministic builds produced byte-identical 12-page PDFs at
  SHA-256
  `5ff37aca10905bd7fd84f25a81e47601ed9883259519b02e2809f77485770d98`.
- The final LaTeX log has zero error, package warning, undefined citation,
  undefined reference, overfull box, or underfull box.
- BibTeX has 14 `bibitem` records and `warning$ -- 0`.
- All 33 PDF fonts are embedded and subset; the PDF has zero raster image
  objects.
- All 12 rendered pages were inspected. The new first-page literature
  paragraph, corrected page-7 multiplier notation, all three figures,
  tables, hashes, and the expanded 14-item bibliography are legible and
  uncropped, with no overlap or corrupt glyph.
- The original pre-review PDF remains byte-unchanged at SHA-256
  `9b7594015e3e6eb3db759ea1eea27a2249c513368ce9c063382be76e041357f8`.

## Bound revision snapshot

| Object | SHA-256 |
|---|---|
| Round-1 review | `bb64f75c96ca0b3d2e78a3b295a1d1b8321ea2143f4612e08b316594991e5ac5` |
| revised `paper/manuscript.tex` | `95ebccff1eb5f2b939be92c9a8b7020b625d4b8056cc5b6bda3b3814fcae580c` |
| `paper/paper_round1_revision.pdf` | `5ff37aca10905bd7fd84f25a81e47601ed9883259519b02e2809f77485770d98` |
| revised `paper/references.bib` | `0fd74e7688739c8a3eb44ea995f950250c0a9afcfc99699824bd57e753e21ba9` |
| revised `notes/CITATION_VERIFICATION.md` | `4d79e865326ae7209184f42a3a204e73b189d3a3f2d9ab71c25924ea72003805` |
| revised `PAPER_PLAN.md` | `6d87e00c8cf5b21c021dfe38b572ec16d5551f576615fced4abdc72f6f70a885` |
| unchanged figure manifest | `e292df2cd1d9d2c19675bc36cf30ed75e88e730fca17c7cd47420285be07fb2c` |
| unchanged raw result | `0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0` |
| unchanged final result manifest | `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f` |

## Disposition

`ROUND1_BOUNDED_REVISION_COMPLETE_READY_FOR_INDEPENDENT_ROUND2`.

This response and its mechanical checks are author-side evidence only. They
are not an independent Round-2 verdict, do not authorize finalization, and
do not authorize creation of `paper_final.pdf`.
