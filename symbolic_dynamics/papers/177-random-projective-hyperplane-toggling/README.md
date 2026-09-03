# P177 — random projective-hyperplane toggling

**Round:** Round 2 dual-review freeze  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

On the subset carrier of the nonzero points of `F_2^d`, this chain samples a
nonzero linear form and toggles its projective hyperplane.  The paper proves
that every communicating class is a crown-graph walk, derives the exact
every-time/every-target history kernel, separates parity-phase convergence
from ordinary periodic non-mixing, and gives the complete four-point spectrum
on the full carrier.

The coding/design dictionary, Cayley and finite-Fourier machinery, the named
crown graph and its spectrum, and generic finite-chain facts receive zero
contribution credit.  The bounded owner search does not justify novelty or
external circulation.

## Reproduce the exact controls

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p177.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p177.py | \
  cmp - verification_output.txt
```

The canonical transcript ends with

```text
exact_assertions=1095999
status=PASS
external_status=HOLD_EXTERNAL
```

## Reproduce the deterministic PDF

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The settled Round-2 output is four A4 pages.  `main_round0_original.pdf`
preserves the original author artifact; `main_round1.pdf`, `main_round2.pdf`,
and the live PDF are byte-identical repaired receipts.  Review A exposed the
exact-time support defect at `t=0,1`; both process-separated reviews now close
with zero open findings.  No external release action is authorized.

## File map

- `main.tex`, `references.bib`: anonymous deterministic manuscript source.
- `main.pdf`, `main_round0_original.pdf`, `main_round1.pdf`,
  `main_round2.pdf`: live final and all immutable round receipts.
- `NARRATIVE_REPORT.md`: literal system, theorem spine, and claim ceiling.
- `PAPER_PLAN.md`: claim–evidence matrix and section/page budget.
- `FIGURE_PLAN.md`: no-figure proof-only decision.
- `CLAIMS_EVIDENCE.md`: proof and executable pressure for each contract.
- `SOURCE_VERIFICATION.md`: verified bibliography and owner subtraction.
- `verify_p177.py`, `verification_output.txt`: standalone exact falsifier and
  canonical output.
- `IMPROVEMENT_LOG.md`, `BUILD.md`, `SELF_QA.md`: repair, build, and
  author-side closure ledgers.
- `SHA256SUMS`: non-self-referential artifact manifest.
- `qa_round0/`, `qa_final/`: original and final rendered/cold-build evidence.
