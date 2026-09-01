# P137 — Rank-feedback splitting of finite abelian p-groups

Status: **INTERNAL THEOREM DRAFT / HOLD_EXTERNAL**.

This anonymous short-note package studies the literal self-map

```text
G -> p^d(G) G direct_sum G[p^d(G)]
```

on isomorphism classes of finite abelian `p`-groups of fixed order.  It
proves the exact type rule, the fixed/recurrent classification and fixed OGF,
a pointwise marker budget and unique sharp triangular entry clock, and an
exact fibre/image decoder for every target type.

All standard finite abelian group structure, cyclic kernel/image formulas,
torsion terminology, partitions, Ferrers rectangles, and Gaussian
polynomials are explicitly assigned zero contribution credit.

## Reproduce

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
cmp -s code/verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py)

pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The verifier uses exact integers and tuples only.  Its frozen terminus is
`TOTAL_ASSERTIONS=18504770` and `STATUS=PASS`.

See `PAPER_PLAN.md` for the theorem contract, `CLAIMS_EVIDENCE.md` for the
claim ledger, `CONTROL_RESULTS.md` for exact controls,
`SOURCE_VERIFICATION.md` for citation metadata, and `FINAL_QA.md` for the
author-side artifact audit.

No novelty, priority, authorship, posting, submission, specialist contact, or
external-release decision is made.  External status remains
`HOLD_EXTERNAL`.
