# Round-three owner-repair build record — P121

Status: **PASS / DIRECT-OWNER REWRITE / EXTERNAL HOLD**.

Run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Settled result

- exact verifier: **PASS, 139,589 assertions**;
- fresh stdout: **536 bytes**, byte-identical to `code/verify.out`;
- finite horizons: all boundary orders through `n=9`, laws through
  `n=12`, raw moments through order 6, coefficient identities through
  `n=60`;
- `code/marked_antichain_coefficients.tsv`: parsed and exactly matched;
- four-stage LaTeX/BibTeX build plus one settling pass: **PASS**;
- `main_round0_original.pdf`: frozen pre-owner-rewrite snapshot, 6 A4
  pages, 385,106 bytes;
- `main_round2.pdf`, `main_round3.pdf`, and current `main.pdf`:
  byte-identical, **7 A4 pages, 395,097 bytes**;
- bibliography: 12 cited entries, including the direct statistic, fixed
  marker, caterpillar-probability, and Sturm-comparison owners, all resolved;
- settled warnings, errors, undefined citations/references, box warnings,
  and rerun requests: zero;
- fonts: 30/30 embedded, subsetted, and Unicode-mapped;
- PDF metadata: empty Author, date-free, no form, JavaScript, or encryption.

The rewrite proves the objectwise coupling `X_n=R_n+1` and assigns the
direct owner zero credit for the split/law, unmarked antichains, mean, and
second-moment neighborhood.  The round-three owner repair also credits
Andriantiana--Wagner--Wang for the fixed-tree cardinality marker and
Chang--Fuchs/Rosenberg for the caterpillar probability.  The residual is now
only the Yule-averaged bivariate transform and the strict pole/radius
continuation at `r>=3`.  Novelty, priority, and external circulation remain
**HOLD**.
