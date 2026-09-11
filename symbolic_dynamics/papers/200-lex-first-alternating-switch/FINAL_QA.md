# P200 final manuscript QA

2026-09-05 UTC. Round2 is frozen after two actual process-separated
manuscript reviews and accepted no-change deltas, with no open Critical,
Major or Minor finding. OWNER_AMBER / HOLD_EXTERNAL is unchanged.
This is one retained paper, not a five-paper batch completion.

## Exact evidence

The root evidence audit has actually rerun the author, A and B verifiers
twice each and compared each full stdout byte-for-byte with its canonical.
The counts per run are author 3595488, A 3823696, B 4026047.
The successful receipt is docs/papers197_201_sequence/qa/RETAINED_EVIDENCE_AUDIT.txt.
All-size proofs are in the accepted manuscript and full reviews; finite
assertion counts are not theorem, subclass, novelty or independent-experiment
counts. The final package audit receipt is separately recorded under the
batch qa directory; this document does not replace that mechanical gate.

## Two actual terminal builds and final page views

New qa_final/cold_build_1 and cold_build_2 directories started with only
main.tex and references.bib. Each ran pdflatex -recorder, bibtex, pdflatex,
pdflatex under SOURCE_DATE_EPOCH=1704067200, FORCE_SOURCE_DATE=1, LC_ALL=C,
TZ=UTC. Both PDFs exactly match main.pdf and the accepted main_round2.pdf:
7226b56257356fe3869a957983e0c92a7dbc79470f3e504f0f031c4b6248b3ea.

Both final logs are free of Warning, Undefined, Overfull, Underfull and Error
matches. The four-page PDF is A4, unrotated, unencrypted, without JavaScript,
forms or metadata streams. Title/author/subject/keywords/creator/producer
fields are blank. Every font is embedded, subsetted and Unicode-mapped.
There are no unresolved citation/reference tokens; all three bibliography
keys resolve. No old auxiliary file or PDF was used as cold-build input.

Root actually opened all four final 180-dpi page images, not just a sample:
1: map, ownership and notation; 2: invariant pivot, recurrent iff and two-visits bound; 3: wide witness and complete target inverse with sentinel; 4: maximum/equality theorem, 2x2 exception, controls, scope and all references.
All equations, signs, tables and references are legible and unclipped.
Renderer metadata and the source PDF digest accompany the images.
These two terminal builds are distinct from earlier review/author builds.

## Preserved versions and scientific limits

Original Round0, accepted Round1 and accepted Round2 PDF/source snapshots
remain physically present. Round2 copies unchanged accepted bytes and is
not represented as an invented repair. ROUND1_RECEIPT.md and ROUND2_RECEIPT.md
state review identities, exact pin checks and replay provenance. Earlier
Round0 status text in preserved companions records its historical checkpoint.
The current SHA256SUMS covers the final package; any retained old handoff
manifest is historical, not the current completeness manifest.

Sharp tail equality requires s>=r+1. Narrow/square sharp values stay unproved; no transpose conjugacy or all-time inverse is asserted. Classical interchange, lonesum and generic selector/reverse filtering remain credited.
Missing P51--P56 and bounded source access remain limitations. A future
exact owner or full joint transfer may reopen internal acceptance. No
external upload, public release, submission or specialist approval is authorized.
