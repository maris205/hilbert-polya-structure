# P143 — Boolean row-inclusion residual dynamics

Status: **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**.

Anonymous internal short paper.  The literal map replaces an (n\times n) Boolean matrix by the inclusion preorder of its row supports.  The paper proves the complete one/two-cycle dynamics and an every-target quotient-poset fibre formula.

## Reproduce

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p143.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p143.py > /tmp/p143_replay.txt
cmp -s /tmp/p143_replay.txt verification_output.txt
PYTHONDONTWRITEBYTECODE=1 python3 verify_p143_embeddings.py > /tmp/p143_embedding_replay.txt
cmp -s /tmp/p143_embedding_replay.txt embedding_verification_output.txt
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf` freezes the pre-review build;
`main_round1.pdf` freezes the repaired build; and `main_round2.pdf` is the
independently accepted build, byte-identical to current `main.pdf`.  The second
verifier is an independent labelled-embedding/bijection lane and does not call
the inclusion--exclusion formula.  Exact enumeration is a falsifier, not a
proof.  External status remains `HOLD_EXTERNAL`.
