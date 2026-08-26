# P71 TeX Transport Receipt — Revision Round 1

- status: PASS
- transport_scope: authorized Round 1 patch operations and directly corresponding TeX/code-control surfaces
- markdown_base: stage3/ANCHORED_REVIEW_DRAFT.md
- markdown_mirror: stage4/REVISED_DRAFT.md
- apply_report: stage4/REVISED_DRAFT.md.apply-report.json
- external_release: HOLD

## Authority and mirror binding

The applied mirror is bound to base hash prefix 8fe0c932d100 and output hash prefix 4638cc54580e. The apply report records patch digest d3d00387eec8a1582d22b1da54b81e050c7d333c39629eb851dcbe01ebb44386, four operations, no structural flag, and preserved ratio 0.9577. Its authorization witness is PASS.

The transport below does not create an independent revision surface. Each TeX or auxiliary implementation is a rendering or deterministic-control realization of one authorized mirror operation.

## Operation-by-operation transport map

| op_index | roadmap item and applied operation | Applied mirror evidence | TeX transport | Auxiliary code/control transport | Result |
|---|---|---|---|---|---|
| 0 | REV-P71-EIC-W1; replace B0004 | B0004 contains the bounded-source framing, the component-table pointer, non-priority qualification, and retained high collision risk | sections/1_introduction.tex, opening contribution paragraph; includes exact \cref{tab:component-comparison} | None | MATCH |
| 1 | REV-P71-EIC-W1; replace B0005 | B0005 limits all four listed components to the stated full one-block family and marks the pressure component high-collision | sections/1_introduction.tex, four-item contribution list | None | MATCH |
| 2 | REV-P71-EIC-W1; insert after B0065; fresh blocks B0072, B0073, B0074 | B0065 remains the UFV-project anchor; B0072 is the bounded caption lead, B0073 is the comparison table, and B0074 carries the table identifier | sections/7_scope.tex, Table 2 with label tab:component-comparison; rows distinguish owner-subtracted overlap, documented differences, and unavailable theorem text while retaining HIGH collision risk, specialist gate, and external HOLD | None | MATCH |
| 3 | REV-P71-R1-W1; replace B0068 | B0068 records profile (1,1,2,4,4), exact endpoint masses 2 and 8, and limiting Legendre values log(2) and log(8) | sections/7_scope.tex, final regression-control paragraph | code/verify_degree_pressure.py adds endpoint_receipt and the repeated-extremes fixture; code/verify_degree_pressure.out, CONTROL_RESULTS.md, and stage4/FINAL_CONTROL_RUN.out record the exact PASS receipt | MATCH |

## Mirror comparison and authorization-range proof

1. The apply report names only B0004, B0005, B0065, and B0068 as operation anchors. The sole fresh IDs are B0072–B0074. The response letter uses exactly these apply-report values.
2. The revised mirror contains the authorized replacements at B0004, B0005, and B0068 and the authorized insertion B0072–B0074 after B0065. No operation targets B0067 or B0071.
3. The specialist item REV-P71-R2-W1 remains UNRESOLVABLE: B0067 receives no patch operation, the specialist gate remains, and external release remains HOLD.
4. The optional roadmap item REV-P71-R3-W1 remains a DELIBERATE_LIMITATION: B0071 receives no patch operation and remains byte-identical in the applied mirror.
5. The old and revised Markdown mirrors each contain the same 10 citation keys; set difference in both directions is empty. Therefore the table reuses only already present local-source-ledger citations.
6. references.bib SHA-256 is 66e274980a6d32bb25c9ff6c3a82b732856f105df9a2d2e3debe11b704a42e90, exactly matching stage3/INPUT_FREEZE.json. New references added: 0.

## Unchanged transport infrastructure and frozen inputs

- main.tex SHA-256: 7967e51b4c0452c0ae58c74da41fbc462a84d5d50684370b36f30881c106f8cb — exact match to stage3/INPUT_FREEZE.json.
- references.bib SHA-256: 66e274980a6d32bb25c9ff6c3a82b732856f105df9a2d2e3debe11b704a42e90 — exact match to stage3/INPUT_FREEZE.json.
- stage3/ANCHORED_REVIEW_DRAFT.md SHA-256: 8fe0c932d100144720ad8f1d0c127b6a0abe2effb5e0f9d4df06c15a4eda8c60 — exact match to the evidence-bundle chain start.
- stage3/BLOCK_MANIFEST.json SHA-256: 5a4992b5750316963255212280391379e1f0ab94f44d763dcbd7ef4d8e16b6b4 — exact match to the evidence-bundle chain start.
- stage3/REVISION_ROADMAP.json SHA-256: 99e89c9033266963c1321b5f84c18341dfae64135a2674d79d00390a9f05e2e2 — exact match to the evidence-bundle Round 1 authority.
- No Stage 3 frozen artifact was written during TeX transport or this receipt finalization.

## Verification receipts

- stage4/FINAL_CONTROL_RUN.out: ALL CHECKS PASS, exit 0.
- stage4/FINAL_COMPILE_TRACE.txt: documented pdflatex/bibtex fallback chain completes with exit 0 and produces a 10-page main.pdf.
- stage4/REVISED_DRAFT.md.apply-report.json: authorization witness PASS, four operations, no structural flag.
- Visual QA pages 1, 8, and 9 include the contribution framing, source boundary/control text, and rendered comparison table.

Conclusion: TeX and deterministic-control transport is coextensive with the authorized Round 1 mirror changes; no reference, infrastructure, specialist-clearance, optional-roadmap, or Stage 3 frozen surface was expanded.
