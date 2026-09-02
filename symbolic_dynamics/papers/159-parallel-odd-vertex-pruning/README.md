# P159 — parallel odd-vertex pruning

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

This anonymous short note studies the deterministic map that simultaneously
deletes every currently odd-degree vertex from a simple labelled graph.  Its
narrow claim-bearing package is:

- a target-uniform strict predecessor count from one connected binary
  incidence system;
- correctly oriented rank-transfer powers for every target and time;
- the even/non-even split between a strict power and a geometric sum; and
- exact image layers, image counts, fixed counts, depth CDFs, and shells.

The handshaking lemma, incidence rank, cycle-space enumeration, parity
deletion games, Eulerian/parity editing, generic parallel peeling, matrix
powers, absorption language, and the sharp path clock receive zero
contribution credit.

## Exact control

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p159.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p159.py > /tmp/p159_replay.txt
cmp -s /tmp/p159_replay.txt verification_output.txt
```

The frozen transcript contains **3,167,525** exact assertions and ends in
`PASS`.  It covers all 41,658 labelled graph states through ambient order six,
511 independently row-reduced parity systems through total order nine, all
target/source-rank fibres at every audited time, image sets and counts, CDFs
and shells, matrix orientation, nilpotence, and every mandatory boundary.
Enumeration is counterexample pressure, not proof or owner clearance.

## Rebuild

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf` remains the immutable pre-review freeze.  The
current `main.pdf`, `main_round1.pdf`, and `main_round2.pdf` freeze the
post-review manuscript and are byte-identical; exact hashes and sizes are
recorded in `BUILD.md`.  The settled build
has no citation/reference warning, rerun request, build error, overfull box,
or underfull box.  All font rows are embedded, subsetted, and Unicode mapped.

## Package map

- `main.tex`, `references.bib`: anonymous amsart manuscript and six verified,
  cited sources.
- `main_round0_original.pdf`, `main_round1.pdf`: immutable review rounds.
- `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `PROOF_PACKAGE.md`: readable story,
  claim architecture, and expanded proof spine.
- `CLAIMS_EVIDENCE.md`, `CONTROL_RESULTS.md`: evidence ledger and exact-control
  boundary.
- `SOURCE_VERIFICATION.md`: source metadata, subtraction, and bounded owner
  search ledger.
- `verify_p159.py`, `verification_output.txt`: paper-local exact falsifier and
  frozen transcript.
- `HOSTILE_REVIEW_A.md`, `IMPROVEMENT_LOG.md`: zero-finding independent
  review and explicit no-mathematics-change disposition.
- `BUILD.md` and retained build logs: reproducible review artifact record.

The phase-one `PRE_PAPER_HOSTILE_GATE.md` constrained the theorem before
drafting; formal Review A subsequently returned zero findings.  Review B
found and closed one stale lifecycle sentence only.  Posting, submission,
circulation, author contact,
and other external action remain prohibited.
