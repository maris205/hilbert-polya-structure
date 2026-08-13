# 3-trace-bridge

Proposal Stage 3 asks when periodic-orbit information legitimately defines a
classical--analytic trace bridge.  It introduces a source-locked certificate
T0--T7 and compares two candidates without merging their favorable fields.

## Release status

- Proposal focus: Route A / A3--A4
- Manuscript: independently reviewed, revised, and accepted
- Frozen candidates: `DEN-WITT-Z-FIN` and `MOD-GEO`
- Main exact results: local-germ ambiguity, coordinatewise-splice failure at
  T0, and disjoint modular/prime repeated supports
- Route B: not invoked
- Forbidden inputs: Riemann-zero data, fitted scales, post-hoc clock changes,
  and a hybrid certificate assembled from distinct objects

The Deninger record retains intrinsic prime-log periods but has no
source-defined trace or analytic operator.  The modular record has an exact
same-geometry trace and natural Laplacian but its standard repeated lengths do
not meet rational-prime-power logarithms.

## Main artifacts

- [Manuscript PDF](paper/paper.pdf), [LaTeX source](paper/manuscript.tex), and
  [references](paper/references.bib)
- [Research protocol](notes/research_protocol.md), [source matrix](notes/source_matrix.md),
  [proof audit](notes/proof_audit.md), and
  [composition blueprint](notes/composition_blueprint.md)
- [Independent peer review](notes/peer_review_round1.md),
  [citation audit](notes/citation_audit.md), and
  [release audit](notes/release_audit.md)
- [Control implementation](code/trace_certificate_controls.py),
  [unit tests](code/test_trace_certificate_controls.py), and
  [one-command reproduction](experiments/reproduce.sh)
- [Run summary](results/run_summary.json), [T0 audit](results/certificate_t0_audit.json),
  and [integrity manifest](results/manifest.sha256)

## Reproduction

From this directory, run:

```bash
bash experiments/reproduce.sh
```

Build the manuscript from `paper/` with:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
```
