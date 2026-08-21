# Paper 50 final writer closure report

Status: `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`.

This is a writer-side closure record for an anonymous, journal-neutral A4
mathematical theory article.  It is neither an independent audit nor a claim
of CLEAN, installation, publication, authority mutation, Git mutation, README
registration, or mirror promotion.

## Sole active writer overlay

The exact independent-audit target is
`/tmp/paper50_writer_candidate/FINAL_WRITER_OVERLAY`.  The active manuscript is
`paper/main.pdf`, 17 A4 pages, SHA-256
`bf0c9ea39d55596fab6d873a4062a836451c0a65113d2d245b0a7d94e3243736`.

`PAPER_MANIFEST.tsv` is self-excluding and has 45 sorted content rows.  Its
SHA-256 is
`34dfb4c803bd2a96eda24272e5b70b0b1c42e7b255f73c17da00a7bbfcfdb876`.
The final overlay contains 49 regular files and 11 directories including the
root.  Every file is mode 0644 and every directory is mode 0755.  There is no
symlink, nonregular node, cache, bytecode, LaTeX auxiliary in the compile
tree, review/round/history tree, temporary lane, README, Git path, output
namespace, or plain mirror.

The manifest excludes exactly four downstream closure files:
`PAPER_MANIFEST.tsv`, `WRITER_REPORT.md`, `HANDOFF.md`, and `WRITER_SEAL.txt`.
The dependency direction is content to manifest to report to handoff to raw
self-excluded seal.  No manifest-covered file contains the manifest, report,
handoff, or seal hash, and no upstream closure node depends on a downstream
one.

## Frozen source and reproducibility

The manuscript source, eleven section files, five required figure/table
inputs, bibliography, generator, receipt, and fixed-epoch build script are
present.  Three frozen upstream anchors are vendored under `inputs/frozen/`;
their SHA-256 values remain `c070bd76...`, `8b4d54a8...`, and `e1dca456...`.

Before overlay construction, two fresh minimal lanes rebuilt the frozen
source exactly.  After construction, two further fresh overlay copies
regenerated Table 2 and the figure preview and rebuilt the paper with
`SOURCE_DATE_EPOCH=1787270400`.  Both lanes produced:

- article PDF `bf0c9ea39d55...`;
- preview PDF `520cb7814bc0...`;
- Table 2 `73562e6763d2...`;
- compile log `040ce1a13069...`; and
- bibliography `c9325f05ff00...`.

Their logs have zero diagnostics; five citation keys close exactly.  The C4
replay returns 15 total partitions, four admissible partitions, and four
Hasse covers.  `evidence/FRESH_AB_REPLAY.json` and
`evidence/FINAL_OVERLAY_REPLAY.json` have SHA-256 values
`b700b0d3dd36db415a0dd4e0bc118ce4561f0f4ddfecacd4480a83822b2b8bc2`
and
`f0682986a85922ba549bb72b5aa47e93ab0c529816e5dd2d579af64892fa2c72`.

The active PDF independently passes Poppler default/layout/raw/bbox/
bbox-layout and PyMuPDF extraction.  There are zero illegal
C0/DEL/C1/U+FFFD/PUA characters; untouched raw bbox XML parses strictly; all
7,904 words are within 17 A4 page boxes.  The portable QA record is
`evidence/PDF_QA.json`, SHA-256
`0b6d71529012a662e8a597118b1562e5549d61616cf0a246bce083a2cad1fbc9`.

## Protected Stage-A binding

The live P50 authority was read twice before any writer-candidate change.
Both 105-node raw captures were byte-identical at SHA-256
`b3a26554825eb11b691338ebca882997ffd0c75ba9b5046315e57398e226e9f8`.
The portable `PROTECTED_STAGEA_TREE.tsv`, which contains only relative paths,
types, modes, regular-file sizes, and regular-file hashes, has SHA-256
`0c045bef614862e1d583ad1b72a407d4981db0cd9ce0d93281d56458bb2563ef`.

The independent-method writer replay proves byte and metadata closure between
the 92-node output-free Stage-0 source and the live source descendants.  The
sole live delta is exactly four output directories and nine canonical State-A
files.  The run summary closes all other output sizes and hashes, and the two
science artifacts are byte-identical at `58bd79bb...`.  The 71-file frozen
source sums record has SHA-256 `2914264c...`; the combined replay receipt has
SHA-256
`0c2d7f4c81effe852b876518db8b9cdff01c1c0d0445511a3455a47e810e153c`.

That receipt also authenticates the independently produced post-output
result/report (`9c08d271...` / `ef3b13ba...`) and the fresh independent writer
re-audit result/report (`9f57242d...` / `2edc7bf1...`).  Their dispositions are
external evidence only; this writer does not adopt them as a writer-side
CLEAN claim.

## Claims and evidence boundary

The article's exact skeleton, essential-period, prime/composite constructive
split, high-center identity, arbitrary-radius pointed factor collapse, and C4
partition-poset conclusions rest on the analytic proofs in the manuscript.
Finite counts, generated tables, protected-tree checks, machine PASS fields,
and external audit receipts are reproducibility and provenance controls only.

Owner subtraction remains narrow: DKL95 owns the general over-zero
aligned-symbol criterion, while Hosseini--Yassawi owns the constructive
terminology and cross-base obstruction.  The article makes no priority,
exhaustiveness, or all-base constructiveness claim.

## Historical traceability and stop state

The first writer-audit HOLD, the withdrawn pre-ToUnicode PDF
`6e3ac913...`, withdrawn manifest `7f3d3557...`, repaired pre-overlay manifest
`3fb69bb1...`, full review transcripts, and repair history remain unchanged in
the development candidate and external audit roots.  They are intentionally
absent from this minimal overlay and are not competing active anchors.

The authority P50 tree, source Stage-0 candidate, Git, README, and mirror were
read only throughout closure.  The writer invoked the live integration entry
point zero times.  The only next permitted action is a fresh independent audit
of this exact overlay; this report grants no broader authority.
