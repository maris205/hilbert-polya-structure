# P103 — Double-adjugate matrix dynamics

Status: **FINAL QA PASS / INTERNAL FREEZE / EXTERNAL HOLD**.

Internal Route-A short paper on

\[
\Psi(A)=\operatorname{adj}(\operatorname{adj}A)
\quad\text{on }M_d(\mathbb F_q),\ d\ge3.
\]

The paper owner-subtracts Jacobi's classical identity and derives the full
finite temporal package: one-step singular collapse, every iterate, fixed
counts, projective image staircases, recurrent core, sharp transient depth,
cycle counts, and zeta.

Cross-hostile reviews A and B preserve the theorem package after strengthening
the image-staircase controls from 140,340 to **141,190 exact assertions**.
The 4-page canonical PDF, consolidated hostile ledger, final QA, and verified
SHA-256 manifest are retained locally.  External circulation and priority
language remain **HOLD**.

## Reproduce

```bash
python code/verify_double_adjugate.py > code/verification_output.txt
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
