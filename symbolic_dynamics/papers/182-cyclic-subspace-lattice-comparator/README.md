# P182 — cyclic subspace-lattice comparator

**Round:** `ROUND2_DUAL_REVIEW_FREEZE`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

The paper studies the deterministic map

```text
(A,B,C) -> (C,A∩B,A+B)
```

on triples of subspaces of `F_q^d`.  It proves the universal lattice identity
`T^4=T^2`, identifies the fixed and two-periodic core, gives exact Gaussian-
binomial formulas for every depth population, and determines every target
fibre through ordered complements in `J/M`.  The theorem holds for every
prime power `q` and every `d>=0`; sharp height two begins at `d>=1`.

## Exact replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_p182.py
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_p182.py | \
  cmp - code/CANONICAL.txt
```

The canonical transcript ends with

```text
boxes=15
transitions=328700
exact_assertions=1667850
status=PASS
external_status=HOLD_EXTERNAL
```

## Deterministic Round-0 build

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The anonymous result is four A4 pages.  All three immutable PDF rounds and the
live PDF are byte-identical.  Two process-separated hostile reviews completed
4,127,707 reviewer assertions with zero findings, and two source-only cold
builds reproduced the frozen bytes.  No external action is authorized.

## File map

- `main.tex`, `references.bib`: anonymous deterministic manuscript source and
  five verified, cited bibliography entries.
- `main.pdf`, `main_round0_original.pdf`, `main_round1.pdf`,
  `main_round2.pdf`: live PDF and immutable lifecycle receipts.
- `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `FIGURE_PLAN.md`: story, theorem
  matrix/page plan, and proof-only no-figure decision.
- `PROOF_PACKAGE.md`: expanded symbolic dependency chain.
- `CLAIMS_EVIDENCE.md`: claim-to-proof and claim-to-falsifier traceability.
- `SOURCE_VERIFICATION.md`: verified source metadata, owner boundary, and
  internal collision subtraction.
- `code/verify_p182.py`, `code/CANONICAL.txt`: independent paper-local exact
  verifier and deterministic transcript.
- `BUILD.md`, `SELF_QA.md`, `IMPROVEMENT_LOG.md`, `FINAL_QA.md`: build,
  dual-review, repair, and terminal-QA records.
- `SHA256SUMS`: non-self-referential source/artifact manifest.
