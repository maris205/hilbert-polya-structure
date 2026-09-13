# Paper28 manuscript/validator successor: actual two-root result

Date: 2026-09-05. The reviewed once-only controller actually completed exit0
(session52891, terminal; do not poll or rerun). Its new root is
build-capsule-successor-20260905. Both r0 and r1 were materialized and completed.
No original manuscript, prior validator/controller, dependency snapshot or
failure root was changed.

## Actual output

Both PDFs are 836,405 bytes and have SHA-256
ebbd943cba592de21658248779ea3fb4da2cbcbf9a297131df5a358e731b38ca.
The r0 deliverable is
[main.pdf](../build-capsule-successor-20260905/r0/work/main.pdf);
the independently built counterpart is
[r1 main.pdf](../build-capsule-successor-20260905/r1/work/main.pdf).

Each has 25 physical letter-size pages: 23 content pages and 2 References
pages. The exact final scientific sentence appears on page23; References
starts on the fresh page24 and continues through25. Both actual validator
reports say automated_status PASS, finding_count0, findings empty.
The unchanged 22–30 inclusive physical-content-page gate is satisfied.

All 18 children (nine per root) were spawned, reaped, and returned0 without
timeout: three pdfLaTeX runs and one BibTeX run, followed by pdfinfo,
pdfmeta, pdffonts, pdftotext and the new validator. Fixed-pass auxiliary
convergence and final-log checks passed in each root. The controller's full
raw cross-root work comparison and opening/closing source/control/dependency
bindings passed; no output normalization or acceptance exception was used.

The PDF metadata remains Anonymous, with empty authoring dates, creator,
producer, subject and keywords. All 22 listed font resources are embedded.
There are no final undefined references/citations or overfull boxes.
The seven retained underfull hbox reports point to the unchanged
established-neighbor table at source line258; they are not suppressed.
Their visual disposition is recorded by the final page review.

## Consumed identities and evidence

The exact executable review consumed was
HERMETIC_BUILD_SUCCESSOR_REVIEW_20260905.json, SHA-256
b31e863e82ae31265ad1e9ae295c659aff8765623004fcb4e9834f30d5dd5ee2.
It binds controller bdf7a8acdf3155612f4e190c2ea41295a9e9ee322ccababef5794097a242c611,
validator af6125f5c7499e437f9e56aa54197bcadd3402e3a33d4607a9a1319a3e72f464,
the new source, independent source review, plan, loader and historical
capture provenance.

The new source remains 84,983 bytes, LF1855, SHA-256
7beb4f783cd370dc4b0d9d1e9178e3e48ce1ef9ed1497e0e9883b10739d4a1f9.
Original-source and successor-source identities were checked separately;
the capture was not relabelled as a new-source capture.
No new host dependency was read, installed or captured by this build.

The controller's sealed outcome is
[evidence/outcome.json](../build-capsule-successor-20260905/evidence/outcome.json),
59,824 bytes, SHA-256
ff4e9440a4b055a78135996bcd9ebd70ac1b492054af5277b218f9a4531faa5b.
It seals 250 preceding evidence rows, excluding itself, and explicitly says
AUTOMATED_TWO_ROOT_PASS_VISUAL_REVIEW_PENDING / NOT_GRANTED_BY_CONTROLLER.
The r0 acceptance report is 21,476 bytes, SHA-256
d191787beede459620fdc1b4192246a65e1dbe0d7120673bad6fcec2deeb99f3.
The main agent's direct comparison found r0 readonly before/after manifests
byte-identical (1,801,838 bytes, SHA-256
a8495990bb988f5acbe45cf34cab6b5d18dd89cf8f8cbe506e522b42e9d13032).
Independent final-integrity review will distinguish its own rechecks from
these controller records; it need not reread every unchanged resource byte.

## Final handoff status

The main agent actually inspected page images4,8,9,13,14,17,18,23,24,25,
including all new mathematical blocks, the underfull table and the
content/References boundary. No clipping, overlap or missing content was
seen in those pages. Independent review of all25 page images and final
evidence integrity subsequently passed in FINAL_PDF_SUCCESSOR_REVIEW_20260905.md,
SHA-256 8a27036539f0a967430eb01438c12b216d005829bff4a0899a8cf7220419f748.
The seven inherited underfull warnings were accepted as readable cosmetic
table-spacing issues without source changes. Formal local acceptance is now
recorded separately in LOCAL_ACCEPTANCE_SUCCESSOR_20260905.md; the sealed
automated outcome and validator reports retain their original pending values.

Paper27 remains accepted and untouched. Paper28 is now locally accepted,
bringing Batch07 to2/5. Papers29–31 remain serially pending, followed by the
cross-paper audit. No external publication or cloud action was performed.
