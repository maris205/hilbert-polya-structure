# Final Integrity Record

## Decision

- Candidate: `pcf_markov_baker_v1`
- Manuscript: *Finite-Rank Obstructions for Locally Constant Multiplier
  Clocks: An Audited PCF Markov--Baker Note*
- Final independent verdict: **PASS_WITH_MINORS**, score **7.5/10**
- Local paper status: **COMPLETE**
- Scientific decision: `A0_FAIL / STRUCTURAL_ONLY`, `A1_WEAK`,
  `ROUTE_A_REJECTED`; A2--A4 and Route B remain closed
- External prime or Riemann-zero data accessed: **false**

The final reviewer confirmed that the round-2 nested-cylinder and homterval
repair proves the generating property, least-period preservation, and the
single boundary replacement at all periods.  The two remaining suggestions
were exposition-only and were applied before the final build: finite cylinders
are named as compact intervals, and the interval-dynamics citation now points
to Chapter II, Lemma 3.1 and Theorems 6.1--6.2 of de Melo--van Strien.

## Final artifacts

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `be36bf3ac1cf3e0236dcf9cc90c8f2c5dbabe12d212d0ded349ec64c247d4c78` |
| `paper/manuscript.pdf` | `d94bc574bd7128b777c075569234e76c76c3d2e13694b0c8239220f0aebb69bf` |
| `paper/paper_final.pdf` | `d94bc574bd7128b777c075569234e76c76c3d2e13694b0c8239220f0aebb69bf` |
| `paper/references.bib` | `ae6e2f8785e5cd1bfc55b1373de8137d8dc3cd63f032795b732966fb23df1dac` |
| `paper/reviews/final_review.md` | `ff1d9fc241328504f08901caa7177fbe365efb004ac327b9568f20cde40f06f9` |
| `results/REPORT.sha256` | `3d9233d067640deb0b5008555b1cf42e65f630014c1bc747b012fce320865da2` |

The final PDF has 17 letter-size pages.  The production sequence was
`pdflatex -> bibtex -> pdflatex -> pdflatex`.  The retained log has no
undefined citation or reference, no overfull or underfull box, and no
multiply-defined-label warning.  All fonts are embedded; the PDF is
unencrypted and contains no JavaScript or form objects.

## Claim, experiment, and figure alignment

The retrospective manifests were rebound to the final manuscript source hash:

| Registry | SHA-256 | Status |
|---|---|---|
| `paper/CLAIM_MANIFEST.json` | `9b6f45dcd75dd694399f576163b11358e42adae2e759d1b17916b3f185fd4ede` | JSON valid; 17 claims aligned |
| `paper/EXPERIMENT_PASSPORT.json` | `ae9402116638b83c3a174818f4a6ab74d78ee1c8386baf86ebca988db5d3afa8` | JSON valid; frozen protocol retained; claim-manifest cross-reference reconciled during batch audit |
| `paper/FIGURE_PACKAGE.json` | `16fe56458b11fe3506965433a2dc043c7edf65a5ed9041537319e2344b189b3a` | JSON valid; three figures source-linked |

These are retrospective audit registries.  The contemporaneous scientific
commitment remains `experiments/source_lock.json`; none of its commitments or
any frozen result was changed during manuscript revision.

## Reproducibility checks

- `PYTHONPATH=code pytest -q`: **89 passed**.
- `sha256sum -c results/REPORT.sha256`: **25/25 OK** from the Session root.
- Exact primitive ledger through period 20: two methods agree, total 226.
- Independent 100-digit parent audit: maximum residual
  (9.706\times10^{-98}), below (10^{-75}).
- Development, validation, and sealed-test floating audits: each completed
  (65{,}536\times256=16{,}777{,}216) checks; common maximum error
  (1.388\times10^{-16}<2\times10^{-13}); zero boundary failures.
- The three publication figures remain the audited vector-PDF artifacts; the
  final polish did not modify their generators, inputs, or outputs.

## Historical provenance

`INTEGRITY_PRE_CITATIONS_DATA.md`, `INTEGRITY_PRE_REVIEW.md`, prior PDFs, and
round-1/round-2 reviews are retained as historical snapshots.  Their embedded
manuscript hashes are intentionally not rewritten.  `FINAL_INTEGRITY.md` is
the authoritative integrity record for the final locally completed paper.

GitHub synchronization is deliberately deferred to the five-paper batch close,
where the existing clone-and-sync procedure will exclude every nested `.git/`
and `.ipynb_checkpoints/` directory before a single scoped commit.
