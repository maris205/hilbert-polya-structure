# 6-cohomological-owner

Paper 6 closes the current five-project batch by asking which operator owns
the exact zeta determinant of the frozen Frobenius suspension of
`P^1/F_2`.

## Result

The closed-point orbit ledger and the graded étale-cohomology ledger arise
from the same arithmetic parent and satisfy an exact Lefschetz determinant
identity.  Their exact determinant owner is Frobenius `Phi` on finite
dimensional graded `Q_l`-cohomology.  The natural suspension-time owner is a
different operator: the self-adjoint periodic derivative `A_K` on the Hilbert
direct sum of all closed-point circles.

The Koopman operator passes the limited Route-B definition and
self-adjointness layers, but its point spectrum is
`(2*pi/log(2))*Q`, every eigenvalue has countably infinite multiplicity, and
its full and essential spectra are `R`.  It has no compact resolvent or
trace-class Gaussian heat operator.  Consequently:

- native finite-field Route A: `ROUTE_A_SUCCESS_ROUTE_B_NOT_READY`;
- Riemann-target Route A: `ROUTE_A_REJECTED`;
- limited Koopman Route B: `(B1_COMPLETE_OPERATOR_DEFINITION,
  B2_SELF_ADJOINT, B3_FAIL, B4_FAIL, B5_FAIL)`, hence
  `ROUTE_B_REJECTED` and no Hilbert--Pólya claim.

This is a frozen-object operator-ownership theorem, not a universal no-go
theorem for cohomological flows.

## Main artifacts

- `paper/paper.pdf`: release PDF (9 pages).
- `paper/manuscript.tex`: English paper with an independently written
  simplified-Chinese abstract.
- `paper/references.bib`: six source-locked references.
- `paper/figures/operator_ownership.tex`: native TikZ ownership diagram.
- `notes/research_protocol.md`: frozen question, conventions, and stop rules.
- `notes/source_audit.md`: source identities, hashes, locators, and boundaries.
- `notes/proof_audit.md`: complete proof and route audit.
- `notes/composition_blueprint.md`: claim and manuscript architecture.
- `notes/release_audit.md`: post-build, reproduction, and visual inspection.
- `notes/citation_audit.md`: independent source and citation audit, `ACCEPT`.
- `notes/peer_review_round1.md`: independent mathematical and release review,
  final gate `ACCEPT`.
- `code/`: exact integer/rational controls and ten unit tests.
- `results/`: generated ledgers, typed certificate, and SHA-256 manifest.

## Reproduce

From the workspace root:

```bash
bash papers/6-cohomological-owner/experiments/reproduce.sh
```

The command regenerates five hash-locked artifacts and runs 10 deterministic
tests.  It uses no Riemann zeros, fitting, random numbers, network data, or
floating-point root finder.

Build the PDF with:

```bash
cd papers/6-cohomological-owner/paper
latexmk -xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
cp manuscript.pdf paper.pdf
```

The release hash and independent review closure are frozen in
`notes/release_audit.md`, `notes/citation_audit.md`, and
`notes/peer_review_round1.md`.
