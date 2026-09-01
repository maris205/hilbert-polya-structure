# Leftmost reassociation of Dyck components

Status: **ROUND-2 INTERNAL REVIEW ACCEPTED / OWNER-THIN / HOLD_EXTERNAL**.

This short note studies one literal deterministic map on Dyck paths.  If

```text
P = C_1 C_2 ... C_k,    C_1 = U A D
```

is the primitive factorisation, the map fixes `P` for `k=1` and otherwise
sends it to

```text
U A C_2 D C_3 ... C_k.
```

The note proves the exact component-count clock, primitive recurrent set,
unique deepest path, all temporal layers, and an explicit unique source at
every feasible depth over every fixed target.  Its ownership framing now also
subtracts Pallo's deterministic leftmost-rotation precedent, the
Pallo/Chapoton comb/height-zero correspondence, and the standard ordered-tree
graft/lift model.  Only the exact temporal/target-fibre conjunction remains as
an owner-unresolved internal residual.

No priority, originality, posting, submission, specialist-contact, or
external-release decision is made.

## Contents

- `main.tex` / `main.pdf` -- anonymous `amsart` manuscript.
- `main_round0_original.pdf` -- preserved clean author-stage PDF.
- `main_round1.pdf` -- post-remediation round-1 PDF.
- `main_round2.pdf` -- accepted build after closing the sole nonblocking
  round-2 abstract-range minor; identical to current `main.pdf`.
- `NARRATIVE_REPORT.md` -- theorem story, dependency map, and owner boundary.
- `PAPER_PLAN.md` -- section and claim plan; no figure is required.
- `CLAIMS_EVIDENCE.md` -- proof/control traceability matrix.
- `SOURCE_VERIFICATION.md` -- verified metadata and source-role ledger.
- `verify_p144.py` -- focused exact finite audit.
- `verification_output.txt` -- frozen canonical verifier transcript.
- `CONTROL_RESULTS.md` -- coverage and interpretation limits.
- `references.bib` -- seven verified, cited-only entries.
- `BUILD.md` -- compilation and artifact audit.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, `IMPROVEMENT_LOG.md` -- two
  independent hostile reviews and repair closure.

## Exact replay

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p144.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p144.py | cmp - verification_output.txt
```

The frozen run exhausts every Dyck path of semilength `1..12`: 290,511
states, 82,500 fixed targets, and **6,005,502 exact assertions**.  It ends in
`STATUS=PASS`.

## Build

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The accepted artifact has 6 pages and seven cited references, with embedded
fonts, zero undefined references/citations, and no LaTeX box warnings.  See
`BUILD.md` for the exact size and hash audit.
