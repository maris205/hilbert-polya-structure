# P145 — Vertex-push chains as folded-hypercube products

Status: **ROUND-2 INTERNAL REVIEW ACCEPTED / OWNER-REPAIRED /
HOLD_EXTERNAL**.

The uniform vertex-push chain on a connected component of order `s` is the
folded-hypercube walk `FQ_(s-1)` in quotient coordinates.  Round 1 treats that
identification, the single-component spectrum, folded-cube bipartiteness and
random-walk facts, vertex pushing, and generic abelian Fourier machinery as
directly owned zero-credit inputs.

The reduced paper records the degree-weighted multi-component product and a
known-`n` spectral inverse.  Its exact recovery routine takes only `(n,Q)` and
returns the component-order multiset, including isolates.  Internal adjacency
is genuinely nonidentifiable (`P_4` and `K_4` are constructed controls), a
starting orientation is not marked in an unmarked transition kernel, and
without supplied `n` every positive-order edgeless graph has the same
one-state spectrum.  No novelty or priority claim is made.

## Exact replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p145.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p145.py | \
  cmp - verification_output.txt
```

The round-1 transcript terminates with:

```text
exact_assertions=155901
status=PASS
external_status=HOLD_EXTERNAL
```

Coverage includes 1,099 labelled graphs, 14,149 orbit states, 28,628
input-only component recoveries, 624,834 exact candidate division attempts,
and constructed `P_4/K_4`, affine-orbit, and unknown-`n` witnesses.

## Build

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

- `main_round0_original.pdf` is the untouched author-round artifact.
- `main_round1.pdf` is the settled owner-repaired round-1 build.
- `main.pdf` and `main_round2.pdf` are the accepted build after the direct
  journal-locator polish and proof-closure clarification.
- `IMPROVEMENT_LOG.md` maps every hostile-review requirement to its repair.

No figure is required: the pivot quotient, weighted kernel, exact recovery
algorithm, and root separator are formula-level objects.  Two independent
hostile-review rounds are preserved; no Git operation is part of the
paper-local review.
