# Final QA report — Papers 72–76

Checkpoint: 2026-08-27 UTC
Result: **5/5 PASS; INTERNAL FREEZE; EXTERNAL HOLD**

| Slot | Pages | Fresh control replay | Stored-output equality | Clean log | Embedded fonts | Visual first/last page |
|---:|---:|---|---|---|---|---|
| P72 | 4 | pass | exact | pass | pass | pass |
| P73 | 5 | pass | exact | pass | pass | pass |
| P74 | 4 | pass | exact | pass | pass | pass |
| P75 | 5 | pass | exact | pass | pass | pass |
| P76 | 5 | pass | exact | pass | pass | pass |

All five PDFs were built with the documented `pdflatex -> bibtex ->
pdflatex -> pdflatex` sequence after the final source changes.  A text-layer
scan found no unresolved-reference markers or leaked TeX commands.  Three
separate reverse-reading streams then checked P72/P75, P73, and P74/P76; no
internal-freeze blocker remained.

The most consequential audit corrections are preserved in the manuscripts:

- P72 counts fixed points of an actual self-map and limits its entropy
  conjugacy to strictly-positive directions.
- P73 links the printed substitution directly to its incidence/Jordan and
  recognizability certificates.
- P74 separates true context signatures from the normal-form counting proof.
- P75 confines MME and zeta multiplicities to the clique-automaton edge
  presentation, not its unadorned label factor.
- P76 makes closure equality conditional on strict feasibility and retains a
  weak-only counterexample.

This report validates internal reproducibility and artifact integrity only.
It does not establish novelty, priority, authorship, venue fit, or permission
for public or external circulation.

The five canonical PDF digests are frozen in
`CANONICAL_PDF_MANIFEST.sha256`; each paper package also carries a
`SHA256SUMS` manifest for its source, proof-control, audit, and PDF artifacts.
