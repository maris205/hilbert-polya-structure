# P162 — Random Translation Intersection

Anonymous internal theorem draft for the process

```text
A <- A intersection (A+v),   v uniform in F_2^d.
```

**Lifecycle:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`  
**External release:** prohibited

## Files

- `main.tex` — manuscript source.
- `references.bib` — four directly relevant owned-background sources.
- `PAPER_PLAN.md` — theorem and proof architecture.
- `CLAIMS_EVIDENCE.md` — claim, proof, verification, and owner boundary.
- `NARRATIVE_REPORT.md` — concise research progression and scope.
- `code/verify.py` — independent standard-library exact verifier.
- `code/CANONICAL.txt` — frozen deterministic verifier transcript.
- `BUILD.md` — cold-build, PDF, font, anonymity, and log record.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md` — the two independent review
  records.
- `IMPROVEMENT_LOG.md` — round-by-round disposition and frozen PDF hashes.
- `FINAL_QA.md` — final verifier, review, build, PDF, and lifecycle closure.
- `main_round0_original.pdf`, `main_round1.pdf`, `main_round2.pdf` — preserved
  review artifacts; `main.pdf` is byte-identical to Round 2.

## Reproduce the exact control

```bash
python3 code/verify.py
cmp code/CANONICAL.txt <(python3 code/verify.py)
```

The verifier is a finite falsification tool.  It does not replace the
all-parameter proofs in `main.tex` and does not establish novelty.

## Rebuild the paper

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The erosion interpretation, generic morphology iteration, stochastic
morphology, and finite-field random-rank law are explicitly subtracted as
owned inputs.  Only the combined theorem package is assessed here, and it
remains `HOLD_EXTERNAL`.
