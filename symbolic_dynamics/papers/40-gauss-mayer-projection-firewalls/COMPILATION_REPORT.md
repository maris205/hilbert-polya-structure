# Paper 40 writer compilation report

Status: `WRITER_FINAL`

Date: 2026-08-17 UTC.

## Installed deliverable

- PDF: `main.pdf`
- SHA-256:
  `33b88048ca5cc24ed89978ea9e323ce4c7a07425b73785214ef11e5d9ef26cec`
- size: 555,182 bytes
- format: PDF 1.5, A4
- pages: 17 total
- main text through conclusion: page 11
- references: pages 11--12
- appendices: pages 13--17
- vector TikZ figures: pages 5, 8, and 10

The installed PDF was compiled outside the authority tree. `latexmk` was not
available, so each clean build used the equivalent explicit sequence
`pdflatex -> BibTeX -> pdflatex x 3`. Two independent clean builds used the
fixed UTC source epoch 2026-08-17 00:00:00 and produced byte-identical PDFs.

## Canonical integration binding

The manuscript consumes the designated integrator's
`FINAL / POST-OUTPUT CLEAN` block:

- main evaluator: 210/210;
- independent evaluator: 208/208;
- scientific projection SHA-256:
  `340aff6f08e7cf9360d57d34ff9c66e99f9322343b3069fe37e5acc2f55aa7c5`;
- integrity audit: 83/83, SHA-256
  `61ff8805dd5bcc44dec3ea8a960786ccb72f211bf7c8d30d013eb749a536110c`;
- results ledger: 102/102, SHA-256
  `ddcda6a450c662be8432f14510569a4097f6f3909ea17a68f499d21e47edeb31`;
- exact set: 54 result files, two evaluation files, and one experiment report;
- packet mutations: 164 rejected by each evaluator (164 x 2);
- Route executions: 422 rejected, comprising 24 explicit and 398 exhaustive
  recursive mutations over 409 distinct payloads;
- strict Route checks: 18/18; and
- hidden cold-copy second-run changed paths: 0.

The writer changed none of the integration-owned code, experiment, result, or
evaluation artifacts.

## QA round 1

- Recomputed every displayed count from the sealed JSON/certificate fields.
- Verified all three displayed SHA-256 bindings against authority bytes.
- Confirmed that the canonical block occurs exactly once in the manuscript.
- Compiled the final TeX sources out of tree and visually inspected the
  canonical block, conclusion/reference boundary, and appendix provenance.
- Confirmed no clipping, overlap, missing figure, or hash overflow.

## QA round 2

- Recompiled twice from independent empty build directories and required
  byte-identical PDFs.
- Final LaTeX and BibTeX logs contain zero warnings, errors, undefined
  citations/references, overfull boxes, or underfull boxes.
- All 16 bibliography records are cited and every citation resolves.
- All 32 PDF fonts are embedded and subset.
- PDF text contains no unresolved markers, host paths, stale synchronization
  tokens, or verification tokens.
- The complete writer text set has zero trailing whitespace, zero carriage
  returns, and a final line feed in every file.
- The authority tree contains no TeX auxiliary files or bytecode caches.

## Writer source hashes

| Path | SHA-256 |
|---|---|
| `README.md` | `2979f59638ffdcbf41228ee1316665ab2f4164bcc78cb3a895db73f2ccfc2e26` |
| `NARRATIVE_REPORT.md` | `3ae5297b979894a4b112f838e403cf0f4b3dd40d4f2cceab309bf4ddcb4cb0c9` |
| `PAPER_PLAN.md` | `24ed5c63d71b4de229c024a05a71dc8529fab5a0c226637212caa2438511d1d8` |
| `main.tex` | `b51729bc88ea550736260996cb01094c3de0d8d15ff4fea74a3f41094eb49faf` |
| `math_commands.tex` | `16fb8f709991a9cc7547458064b605a54ea02c3b4a49a0cb4dac5c771a9a0c6c` |
| `references.bib` | `43daf542a1a06d11d8975de9e7f883bbf407320bd43b56d19bab78513c760096` |
| `sections/0_abstract.tex` | `f76f286f63ffbae5aaa589ccbc4aa58a099f77d8d7723764e571e5ac44558fde` |
| `sections/1_introduction.tex` | `cd2335857a0d755247ca599c11eddf6f5122744f251e9b20ff57447483516d53` |
| `sections/2_related_work.tex` | `ee74496d4066b4ddd462fdc532c1c7995deddfc4614302d573648aa9d32ed585` |
| `sections/3_source_object.tex` | `fa65e8a36639cf793c2ae0cf20ba9a43defaa10e4e900d4880bf3092457c2294` |
| `sections/4_projection_theorem.tex` | `f5dd253b730d72843bb666275681b89862bf8e103bcf0be6eaaba2a83bcb232f` |
| `sections/5_type_ownership.tex` | `60cb53816b058f4bcb91f8f09ac6b50f482c0f32cfe86b8b1cd22ab26d170299` |
| `sections/6_exact_audit.tex` | `76b5f190c41b677b713aa411ed9b223d5dd4857b2b4db40a2f441d4fea3d12da` |
| `sections/7_route_conclusion.tex` | `9bc415e9f97075ca6aa2019098414710c452865139a6afeae833a8a062e4477b` |
| `sections/A_full_proofs.tex` | `b3b17726e05bbe733d8749d7b5584f0febc6d464f00b9dce841b14e2e62d8d13` |
| `sections/B_boundaries_and_locks.tex` | `ea74160313a482eaae1ad225536bf1eacd84a12e91a45284a8df3ca7e661ee7e` |
| `figures/algebraic_firewalls.tex` | `771f3a142c7c7b042a50b1a99bcbb02363e76e8bf69e8619ea4b323956b86d41` |
| `figures/object_projection_gate.tex` | `b9d9e4064d6ce7f2689591d9e91f5c7d9f13e1c58b2ef0f4bb4e9abc58d71a2f` |
| `figures/type_source_ownership.tex` | `0ed802993ab35f5e7f0c6b9af3166a0a4b6e2edc767c65a7e82654237e1e293a` |

Only `main.pdf` and this compilation report were installed as writer build
artifacts. No auxiliary compilation file was copied into authority.
