# 5-quantum-flow

Paper 5 audits the canonical Koopman lift of the unchanged Frobenius
suspension `FF-FROB-SUSP-P1-F2`. The frozen operator candidate is
`FF-FROB-SUSP-P1-F2-KOOPMAN-P1`.

Release status: independent peer review **ACCEPT**.

## Main result

For every family of finite, strictly positive component weights, the Koopman
group is unitarily equivalent to the canonical counting-times-Lebesgue model.
Its self-adjoint Stone generator has

```text
point spectrum       (2*pi/log(2))*Q
point multiplicity   countably infinite at every point eigenvalue
spectrum             R
essential spectrum   R
discrete spectrum    empty
```

Hence the resolvent is noncompact, every interval of positive width has an
infinite-rank spectral projection, and the standard heat and spectral-zeta
determinant mechanisms fail. The orbit Hasse--Weil product and Deligne's
cohomological Frobenius determinant remain different operator ledgers.

## Route status

- `A4_UNITARY_OR_SCATTERING_CANDIDATE` — `PROVED`;
- `B1_COMPLETE_OPERATOR_DEFINITION` — `PROVED`;
- `B2_SELF_ADJOINT` — `PROVED`;
- `B3_FAIL` — `PROVED`;
- scoped result: `ROUTE_B_REJECTED` at Gate C;
- B4 and B5 are outside the limited audit and are not assigned verdicts;
- no Hilbert--Pólya claim is permitted.

## Artifacts

- [Manuscript PDF](paper/paper.pdf), [LaTeX source](paper/manuscript.tex),
  [bibliography](paper/references.bib), and [TikZ figures](paper/figures/)
- [Research protocol](notes/research_protocol.md), [source matrix](notes/source_matrix.md),
  [candidate lock](notes/candidate_lock.md), [proof audit](notes/proof_audit.md),
  and [composition blueprint](notes/composition_blueprint.md)
- [Independent peer review](notes/peer_review_round1.md),
  [citation audit](notes/citation_audit.md),
  [manuscript-integrity audit](notes/manuscript_integrity_audit.md), and
  [release audit](notes/release_audit.md)
- [Control implementation](code/koopman_spectral_controls.py),
  [unit tests](code/test_koopman_spectral_controls.py), and
  [one-command reproduction](experiments/reproduce.sh)
- [Closed-point controls](results/closed_point_degree_controls.csv),
  [frequency witnesses](results/frequency_multiplicity_witnesses.csv),
  [weight controls](results/weight_unitary_controls.csv), and
  [manifest](results/koopman_spectral_manifest.json)

## Reproduction

From this directory, run:

```bash
./experiments/reproduce.sh
```

The deterministic suite contains eight tests. It uses exact formulas and
finite regressions only, with no Riemann-zero data, fitting, optimization,
randomness, or network access.
