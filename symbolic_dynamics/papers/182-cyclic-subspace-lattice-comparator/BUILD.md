# P182 build and immutable-round ledger

**State:** `ROUND2_DUAL_REVIEW_FREEZE`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

## Paper-local exact verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 code/verify_p182.py
result: PASS
parameter boxes: 15
transitions: 328,700
exact assertions: 1,667,850
transition digest: b2bee01438caf59c10cf29da0a7bf11fcba1aeee2629eb2d86fadb1051a2ebb7
canonical lines/bytes: 23 / 1,641
canonical SHA-256: 993df5e5a286ff4ce42d28c36f417a57b1d212ebdcfd7345524a6498a3ace5e0
two fresh processes: byte-identical
```

The verifier imports no scouting or prior-paper code.  It rebuilds canonical
RREF subspaces, lattice tables, transitions, graph decompositions, and full
incoming fibres.  Enumeration is falsification pressure, not proof or owner
evidence.

## Deterministic LaTeX build

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Frozen receipt:

```text
pages: 4
bytes: 329,096
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: 880abab7db480447c0874e5da6434f7a1d0a8dfbe2ec0b2a23974b573023aa07
Round-0 copy byte-identical: yes
deterministic replay byte-identical: yes
font rows embedded/subsetted/Unicode: 25/25/25
encrypted: no
forms: none
JavaScript: no
metadata title/author/creator/producer: blank
```

The settled final-pass logs contain no warnings, bad boxes, unresolved
references/citations, rerun request, or fatal error.  The initial passes
contain the expected pre-BibTeX unresolved-citation messages and are retained
as build history.

## Frozen Round-0 core hashes

```text
9d496bf69fc3d7426c1f95bb7bacdaf0ea0cd6c7e3b36c5d3c55f64236f088c7  main.tex
5df2e5a1ab48171c72c47f261555d0bbc760b8b55dfa0e271fde59b70b6bc04c  references.bib
e97458b102d00b726594b3b191353b7d44098406bd7e8bffb2f1dac5b83a4348  code/verify_p182.py
993df5e5a286ff4ce42d28c36f417a57b1d212ebdcfd7345524a6498a3ace5e0  code/CANONICAL.txt
880abab7db480447c0874e5da6434f7a1d0a8dfbe2ec0b2a23974b573023aa07  main_round0_original.pdf
```

This section preserves the Round-0 receipt.  Round 1 and Round 2 were frozen
as byte-identical receipts after two zero-finding process-separated reviews;
two physical source-only builds also reproduce the same PDF.  Review and
terminal evidence is bound in `IMPROVEMENT_LOG.md` and `FINAL_QA.md`.
