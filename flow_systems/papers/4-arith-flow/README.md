# 4-arith-flow

Proposal Stage 4 uses a Frobenius suspension as an exact native positive
control and then tests whether its one-clock mechanism transfers to the
rational-prime target.

## Manuscript status

- Proposal focus: Route A / A0--A3
- Manuscript: frozen release; independent review `ACCEPT`
- Frozen candidate: `FF-FROB-SUSP-P1-F2`
- Native result: exact closed-point/primitive-orbit dictionary and
  `A0_ANALYTIC_ARITHMETIC_ORIGIN`, `A1_PASS_ANALYTIC`,
  `A2_ANALYTIC_DETERMINANT`, `A3_CONTROLLED_CONTINUATION`
- Riemann-target result: `ROUTE_A_REJECTED` by the one-clock support
  obstruction and incompatible determinant structure
- Negative control: `SPECZ-TAUT-NORM-CIRCLES` is an exact target-encoded
  product with `A0_FAIL / PROVES_TOO_MUCH`
- Route B: not invoked; no Hilbert--Pólya claim

The square Frobenius on the discretized geometric points of
`P^1/F_2`, suspended with roof `log(2)`, has one primitive orbit per closed
point and least period `deg(x) log(2) = log N(x)`.  Its unweighted orbit zeta
is exactly the native Hasse--Weil zeta.  A fixed `Q = ell^f` clock, however,
can intersect a rational-prime-power clock only in characteristic `ell`, while
disjoint `log(p)` circles merely compile the target Euler factors.

## Main artifacts

- [Manuscript PDF](paper/paper.pdf), [LaTeX source](paper/manuscript.tex),
  [references](paper/references.bib), and [TikZ figures](paper/figures/)
- [Research protocol](notes/research_protocol.md), [source audit](notes/source_audit.md),
  [candidate lock](notes/candidate_lock.md), [proof audit](notes/proof_audit.md),
  and [composition blueprint](notes/composition_blueprint.md)
- [Independent peer review](notes/peer_review_round1.md),
  [citation audit](notes/citation_audit.md), and
  [release audit](notes/release_audit.md)
- [Control implementation](code/frobenius_suspension_controls.py),
  [unit tests](code/test_frobenius_suspension_controls.py), and
  [one-command reproduction](experiments/reproduce.sh)
- [Closed-point ledger](results/closed_point_ledger.csv),
  [formal zeta check](results/zeta_formal_series_identity.csv), and
  [integrity manifest](results/frobenius_suspension_manifest.json)

## Reproduction

From this directory, run:

```bash
bash experiments/reproduce.sh
```

Build the manuscript from `paper/` with:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
```
