# P149 — iterated endpoint-peak extraction

Status: **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**.

The paper studies the self-map of `S_{<=N}` obtained by reading all
endpoint-inclusive local-maximum values and standardizing them.  Its lead
theorem gives every iterate image and an explicit right section at every
rank, followed by a sharp logarithmic clock.  A comparison-poset fibre formula
is included only as a secondary axis after subtracting Ji's exact
two-zero-boundary static statistic, Fu's one-sided exterior-peak convention,
and the ordinary pinnacle literature via an explicit padding bridge.

## Reproduce

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p149.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p149.py | cmp - verification_output.txt
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf` is the pre-self-QA build and `main_round1.pdf`
freezes the first owner repair.  Review B found no theorem error but caught a
Major source-role error: Fu excludes the right endpoint.  Round 2 replaces
that role by directly inspected Ji 2025, retains Fu only as a one-sided
neighbour, and makes no Carlitz--Scoville priority claim without direct access
to the original text.  `main_round2.pdf` is the canonical four-page reviewed
build (374,480 bytes; SHA-256
`7a9e801bfecc08000db82ea37ff9b1e206e4e3ec0ca211c46481db1f401bbacb`).
Enumeration is a falsifier, not a proof.  No external release is authorized.
