# P181 — first-descent prefix reversal

**Round:** Round 2, dual hostile review accepted with zero open findings  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

This deterministic map fixes the increasing permutation and otherwise
reverses the prefix ending immediately after the first descent.  The short
paper proves the exact half-image, the identity-plus-peak two-cycle core, all
tail populations, a complete target-local predecessor formula, and the sharp
maximum fibre with its full maximizing set.  The `n=1,2,3` atlases are stated
separately.

Generic prefix reversal, pancake sorting, longest-increasing-prefix cuts,
descent/peak counts, and finite-map bookkeeping receive zero contribution
credit.  Project Euler First Sort is recorded as a different
follower-to-front rule, not as a name or owner for P181.

## Exact replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p181.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p181.py | \
  cmp - verification_output.txt
```

The canonical transcript ends with

```text
exact_assertions=6273070
status=PASS
external_status=HOLD_EXTERNAL
```

## Deterministic PDF build

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The settled Round-2 output is three A4 pages.  `main_round0_original.pdf`
preserves the author artifact; `main_round1.pdf`, `main_round2.pdf`, and the
live repaired PDF are byte-identical.  Review A's sole boundary finding was
closed by adding the complete `S_1` atlas and exact controls.  Review A then
accepted the repair with `0 Critical / 0 Major / 0 Minor` open, and the
process-separated Review B accepted the complete theorem package with zero
open findings.  No external action is authorized.

## File map

- `main.tex`, `references.bib`: anonymous deterministic manuscript source.
- `main.pdf`, `main_round0_original.pdf`, `main_round1.pdf`,
  `main_round2.pdf`: live settled, original Round-0, accepted Round-1, and
  final Round-2 PDFs.
- `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `FIGURE_PLAN.md`: story, claim
  matrix/page budget, and no-figure proof-only decision.
- `SOURCE_VERIFICATION.md`: verified journal sources and collision boundary.
- `verify_p181.py`, `verification_output.txt`: paper-local exact falsifier
  and canonical transcript.
- `CLAIMS_EVIDENCE.md`, `IMPROVEMENT_LOG.md`, `BUILD.md`, `SELF_QA.md`:
  traceability, repair, build, and author-side closure ledgers.
- `FINAL_QA.md`: final paper-local replay, dual-review, PDF, source, and
  lifecycle gate.
- `SHA256SUMS`: non-self-referential artifact manifest.
- `qa_round0/`: three rendered Round-0 pages and extracted text.
- `qa_final/`: two source-only cold builds and the three-page final raster.
