# P171 — Boolean Gram closure as a finite dynamical system

**Round:** Round 2 dual-review no-change freeze  
**Gate:** `GREEN_OWNER_THIN`  
**External lifecycle:** `HOLD_EXTERNAL`  
**Literal map:** `Gamma_n(A)=A A^T` on `n x n` Boolean matrices, with
Boolean-semiring multiplication.

This directory is a self-contained anonymous short note.  Its exact residual
package is deliberately narrow:

1. the all-time orbit identity `Gamma_n^t(A)=G^(2^(t-1))` after the
   row-intersection graph `G=AA^T`;
2. the source-dependent diameter clock, complete recurrent classification,
   fixed census `Bell(n+1)`, and sharp carrier height
   `1+ceil(log2(n-1))` for `n>=2`;
3. an independent every-target formula for the full ordered-column fibre,
   together with the loop-sensitive clique-cover image criterion.

Boolean powers, repeated-squaring closure, partial equivalence relations,
set-intersection graphs, edge clique covers, symmetric Boolean factorization,
Bell numbers, and inclusion--exclusion are all treated as owner-subtracted
background.  The manuscript makes no novelty or priority claim.

## Files

- `main.tex`, `references.bib`: anonymous source.
- `main.pdf`: canonical deterministic Round-2 PDF.
- `main_round0_original.pdf`: preserved byte-identical Round-0 copy.
- `main_round1.pdf`: byte-identical no-change post-Review-A copy.
- `main_round2.pdf`: byte-identical final dual-review copy.
- `verify_p171.py`: standalone standard-library exact verifier.
- `verification_output.txt`: frozen verifier stdout.
- `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`: claim spine and narrative.
- `CLAIMS_EVIDENCE.md`: theorem-to-proof-to-check map.
- `SOURCE_VERIFICATION.md`: primary-source owner audit and internal
  collision subtraction.
- `HOSTILE_GATE.md`: independent re-entry decision.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`: two independent manuscript
  reviews.
- `IMPROVEMENT_LOG.md`: explicit no-change review closeout.
- `BUILD.md`, `SELF_QA.md`: compilation and artifact QA ledgers.
- `SHA256SUMS`: final integrity manifest.

## Reproduce

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p171.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
sha256sum -c SHA256SUMS
```

The verifier exhausts every Boolean source and every Boolean target for
`1<=n<=4`; it also replays the sharp path family through `n=64`.  These finite
controls are falsification evidence, while `main.tex` contains the uniform
proofs.

Both hostile reviews returned `PROVABLE AS STATED / 0 Critical / 0 Major /
0 Minor`.  Review B used a separately implemented column-support carrier and
729,535 assertions, including every five-vertex fully looped graph.  No
review changed the manuscript, bibliography, author verifier, theorem
ceiling, PDF, owner-thin decision, or lifecycle.
