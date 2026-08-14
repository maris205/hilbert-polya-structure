# 2-flow-zeta

Proposal Stage 2 studies whether the Stage-1 arithmetic survivor can support a natural dynamical trace or determinant, rather than merely a packet-indexed rewriting of the Euler product.

## Final status

- Proposal focus: Route A / A1--A3
- Research project: **complete; independently reviewed and revised**
- Primary object: `DEN-WITT-Z-FIN`, with the Stage-1 source lock unchanged
- Exact calibration object: `MOD-GEO` and its Selberg/Ruelle quotient
- Forbidden inputs: Riemann-zero data, fitted scales, manually imposed packet mass, and a hand-written prime Euler product presented as a dynamical determinant
- Route-A result: `A0_ANALYTIC_ARITHMETIC_ORIGIN`, `A1_WEAK`, conventional
  `A2_FAIL`; source-intrinsic measured alternative `NOT_TESTABLE`; overall
  `ROUTE_A_EXPLORATORY`
- Route-B status: not invocable

The ordinary one-factor-per-individual-orbit product is ruled out because every
prime packet contains uncountably many primitive orbits of the same length.
This does not rule out future measured, groupoid, or cohomological enrichments:
the frozen source does not yet supply their packet lift, cross-prime masses,
operator trace, or determinant theorem.

## Main artifacts

- [Paper PDF](paper/paper.pdf), [LaTeX source](paper/manuscript.tex), and [references](paper/references.bib)
- [Source audit](notes/phase2_deninger_source_audit.md), [trace bibliography](notes/phase2_trace_bibliography.md), and [no-go audit](notes/phase3_trace_no_go_audit.md)
- [Independent proof audit](notes/proof_audit.md), [peer review](notes/peer_review_round1.md), and [citation audit](notes/citation_audit.md)
- [Reproduction command](experiments/reproduce.sh) and [result manifest](results/packet_trace_controls_manifest.json)
- [Route-A evaluation](../../evaluations/route_a/DEN-WITT-Z-FIN/2026-08-13-stage3.yaml)

## Reproduction

Run `bash experiments/reproduce.sh` from this directory.  The deterministic
controls use no Riemann-zero data, fitted scale, or fitted packet mass.  Build
the final paper from `paper/` with
`latexmk -xelatex -interaction=nonstopmode -halt-on-error manuscript.tex`.
