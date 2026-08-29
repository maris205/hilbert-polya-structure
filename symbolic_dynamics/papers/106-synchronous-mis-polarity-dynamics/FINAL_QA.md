# P106 final QA

QA date: 2026-08-29 UTC

## Verdict

**Internal Stage 2 package: mechanical PASS after source and control repair.
External release: HOLD.**

Two nonauthor reviews confirmed the repaired source: the false DOI was
replaced, a direct path owner was added, two visible TeX tokens were fixed,
and a dead nonasserting verifier loop was removed.  The mathematical package
has no unresolved critical or major defect, but direct-system owner risk is
high.

## Exact-control gate

- command: `python3 code/verify_mis_polarity.py`;
- exit status: 0; stored stdout: byte-for-byte match;
- exact assertions: **6,462,317**;
- all simple graphs through six vertices: 33,868; simple-state evaluations:
  2,131,019;
- bipartite graphs through `3+3`: 689; bipartite-state evaluations: 37,477;
- path-state evaluations through 17 vertices: 262,143;
- separate bitset and literal-relation updates plus `K_2/K_3` sentinels.

## Build and bibliography gate

- sequence: pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX; all stages exited 0;
- LaTeX/package warnings, undefined citations/references, multiply-defined
  labels, overfull/underfull boxes, errors, and rerun requests: **0**;
- bibliography: 5 cited keys, 5 resolved entries, 0 missing, 0 uncited.

## PDF gate

- artifact: `main.pdf`;
- SHA-256: `b20aa2b9cbc33a15c3ce1f99aeab17b077e09c5f4660f617c4ed8a5fbe7687c1`;
- 4 A4 pages; 299,003 bytes; PDF 1.5; rotation 0;
- encryption, JavaScript, and forms: absent;
- visible author: Anonymous; PDF Author metadata: empty;
- fonts: 23/23 embedded, subsetted, and Unicode-mapped;
- searchable layout text: 13,379 bytes; sentinel scan: clean.

## Visual gate and release boundary

All four pages were rendered and inspected.  The open-neighborhood rule,
polarity proof, complete one/two-cycle zeta, bipartite square law, correctly
attributed path recurrence, control scope, conclusion, and all five repaired
references are legible and uncropped.  No overlap, malformed formula,
unintended blank page, or stray `qquad` token remains.

`SHA256SUMS` covers and verifies the final evidence package.  The same MIS
Boolean system has a direct nearby owner, and formal-concept polarity and the
path recurrence are classical.  The residual is only the synchronous
temporal/zeta conjunction.  External posting, submission, contact, venue
choice, and novelty or priority language remain **HOLD**.
