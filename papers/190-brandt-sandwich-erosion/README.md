# P190 — Brandt sandwich erosion

**Round:** `ROUND1_FROZEN / REVIEW_A_PASS`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

The paper studies the deterministic cyclic-word map

```text
T(x)_i = x_i x_(i+1) x_i
```

over the aperiodic Brandt semigroup `B_n={0} union [n]^2`.  It proves the
all-time inverse-compatible run normal form, exact fixed and tail formulas,
every-labelled-target trace and nonzero-anchor gap product, the all-zero
fibre spectrum, the complete image criterion, and mass conservation.  All
claims include `n=1` and `m=1,2`.

## Exact replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_p190.py
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_p190.py | \
  cmp - code/CANONICAL.txt
```

The canonical transcript ends with

```text
BOXES=26
ASSERTIONS=1555420
STATUS=HOLD_EXTERNAL
RESULT=PASS
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

The anonymous result is four A4 pages.  `main_round0_original.pdf` preserves
the frozen author artifact with SHA-256
`5fb58fae99f49f14653f5eee283e2f66c3af87c06fca65e1b982e5936123eb66`.
After Review A closed two Minor presentation findings, `main.pdf` and
`main_round1.pdf` were frozen at SHA-256
`81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d`.

## File map

- `main.tex`, `references.bib`: anonymous deterministic manuscript source and
  five verified, cited bibliography entries;
- `main.pdf`, `main_round0_original.pdf`: live PDF and immutable Round-0
  receipt;
- `main_round1.pdf`: accepted Review-A rebuild with no theorem or citation
  change;
- `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `FIGURE_PLAN.md`: story, theorem
  architecture, and no-figure decision;
- `PROOF_PACKAGE.md`: normalized assumptions and complete proof dependency;
- `CLAIMS_EVIDENCE.md`: claim-to-proof and claim-to-falsifier traceability;
- `SOURCE_VERIFICATION.md`: verified metadata and owner boundary;
- `code/verify_p190.py`, `code/CANONICAL.txt`: paper-local exact control and
  deterministic transcript;
- `BUILD.md`, `SELF_QA.md`: Round-0 build and author-handoff receipts;
- `qa_round0/`: extracted text and four rendered inspection pages;
- `SHA256SUMS`: non-self-referential Round-0 manifest.
- `docs/papers187_191_sequence/reviews/p190_a/`: Review-A hostile audit and
  accepted delta package.

Review A is complete; Review B, final QA, posting, submission, and any other
external action remain unauthorized.
