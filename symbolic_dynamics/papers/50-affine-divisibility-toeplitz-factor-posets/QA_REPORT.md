# Paper 50 final writer-side QA report

Status: `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`.

This is a writer-side reproducibility record for the minimal overlay.  It is
not an independent audit, installation, publication, authority-write, Git,
README, mirror, or CLEAN disposition.

## Active manuscript

- Anonymous journal-neutral A4 theory article, 17 pages.
- Active PDF: `paper/main.pdf`.
- Active PDF SHA-256:
  `bf0c9ea39d55596fab6d873a4062a836451c0a65113d2d245b0a7d94e3243736`.
- Fixed build epoch: `1787270400`.
- Final log SHA-256:
  `040ce1a1306948b86a5484760ef8c761ee6c8fcdecff21f8767963264bb27a93`.
- Final bibliography SHA-256:
  `c9325f05ff00a68e8522fdd841c055945e9087102a3f93552cefbf1ce5174dde`.

Two fresh pre-closure lanes regenerated Table 2 and rebuilt from the exact 21
manuscript inputs.  Both PDF, log, BBL, and table hashes match the active
candidate.  The receipt is `evidence/FRESH_AB_REPLAY.json`, SHA-256
`b700b0d3dd36db415a0dd4e0bc118ce4561f0f4ddfecacd4480a83822b2b8bc2`.

Two further fresh lanes copied this minimal overlay, regenerated Table 2 and
the four-page figure preview, rebuilt the article, checked citation closure,
ran the independent C4 partition enumerator, and ran all six text-extraction
modes.  They reproduced PDF `bf0c9ea3...`, preview `520cb781...`, Table 2
`73562e67...`, log `040ce1a1...`, and BBL `c9325f05...`.  The receipt is
`evidence/FINAL_OVERLAY_REPLAY.json`, SHA-256
`f0682986a85922ba549bb72b5aa47e93ab0c529816e5dd2d579af64892fa2c72`.

## PDF gate

The active-PDF QA receipt is `evidence/PDF_QA.json`, SHA-256
`0b6d71529012a662e8a597118b1562e5549d61616cf0a246bce083a2cad1fbc9`.
It reports 17 A4 pages, 7,904 words in both raw bbox modes, zero out-of-page
boxes, and zero illegal C0/DEL/C1/U+FFFD/PUA characters in Poppler default,
layout, raw, bbox, bbox-layout, and PyMuPDF extraction.  Untouched bbox and
bbox-layout bytes pass both strict ElementTree and `xmllint` parsing.  The
ToUnicode repair changes no visible page raster or theorem/body source.

## Protected Stage-A closure

Before any candidate write, two raw captures of the protected live authority
tree were byte-identical at SHA-256
`b3a26554825eb11b691338ebca882997ffd0c75ba9b5046315e57398e226e9f8`.
The portable relative-path manifest has 105 nodes: 80 regular files and 25
directories.  Its SHA-256 is
`0c045bef614862e1d583ad1b72a407d4981db0cd9ce0d93281d56458bb2563ef`.
The sealed source contributes 92 nodes; the sole live delta is exactly four
directories and nine regular State-A artifacts.

The writer-owned independent-method replay authenticates the protected tree,
the exact output summary and science bytes, and four externally produced
result/report anchors.  Its SHA-256 is
`0c2d7f4c81effe852b876518db8b9cdff01c1c0d0445511a3455a47e810e153c`.
The external dispositions are recorded only as authenticated inputs: they are
not adopted as a writer-side CLEAN claim.

## External audit anchors

- Independent post-output result/report:
  `9c08d2719d4b63a503c572dce37f812042ff483f91ba05b9673033251e4d2e0d`
  and
  `ef3b13baf948711484fd15846d285835bc60728831d9e4658682a1b31e760039`.
- Fresh independent writer re-audit result/report:
  `9f57242d10556afa4a826cd0a7f7dbe6bec4cd2848add6cb1bb70add9e53c8f2`
  and
  `2edc7bf112a44de36c0a11aa8d3c58dcc01585380ef31bcfc3c7eb771a026f0b`.

The first independent writer audit's HOLD and the pre-repair writer records
remain unchanged outside this overlay for historical traceability.  The
withdrawn PDF/manifest pair is `6e3ac913...` / `7f3d3557...`; the repaired
pre-overlay manifest is `3fb69bb1...`.  None is a competing active overlay
anchor.

## Evidence boundary

Finite diagnostics, machine PASS fields, protected-tree replay, and audit
receipts validate reproducibility and provenance.  They are not substituted
for the analytic proofs in the manuscript.  This writer closure stops at an
independent-audit hold and grants no next-step authority.
