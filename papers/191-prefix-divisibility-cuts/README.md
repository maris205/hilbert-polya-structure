# P191 — Prefix-divisibility cuts

**Round:** `ROUND1_FROZEN / REVIEW_A_PASS`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

The paper studies the deterministic map on positive compositions that retains
an internal prefix cut exactly when its current incoming part divides that
prefix.  It proves monotone convergence and an exact fixed-state recurrence,
the sharp `N-3` transient with its unique deepest state, and two equivalent
every-target fibre formulas: a global no-skipped-cut path recurrence and a
product of arithmetic interval counts.  All claims include `N=1,2,3`.

## Exact replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp - code/CANONICAL.txt
```

The canonical transcript ends with

```text
transitions=262143
assertions=3408240
transition_digest=e6f5f4476101705df494a808aec8bf2fa8281f66caf5e3f36bcbf98b1bd30c82
status=PASS
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

The anonymous result is four A4 pages.  `main.pdf`,
`main_round0_original.pdf`, and `main_round1.pdf` are byte-identical with
SHA-256 `d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b`.

## File map

- `main.tex`, `references.bib`: anonymous deterministic manuscript source and
  five verified, cited bibliography entries;
- `main.pdf`, `main_round0_original.pdf`: live PDF and immutable Round-0
  receipt;
- `main_round1.pdf`: immutable Review-A receipt of the unchanged theorem
  package;
- `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `FIGURE_PLAN.md`: story, theorem
  architecture, and the no-figure decision;
- `PROOF_PACKAGE.md`: normalized assumptions, full proof dependency, boundary
  audit, and limitations;
- `CLAIMS_EVIDENCE.md`: theorem-to-proof and theorem-to-falsifier traceability;
- `SOURCE_VERIFICATION.md`: verified metadata, bounded owner search, and
  internal-history subtraction;
- `code/verify.py`, `code/CANONICAL.txt`: paper-local exact control and
  deterministic transcript;
- `BUILD.md`, `SELF_QA.md`: Round-0 build and author-handoff receipts;
- `qa_round0/`: two verifier transcripts, extracted text, and four rendered
  pages inspected at 220 dpi;
- `SHA256SUMS`: non-self-referential Round-0 manifest.
- `docs/papers187_191_sequence/reviews/p191_a/`: Review-A hostile audit and
  no-change acceptance package.

Review A is complete; Review B, final QA, posting, submission, and any other
external action remain unauthorized.
