# Relation Homology at the Projective-Residue Boundary

Paper 33 / Candidate `SD-C35`.

This paper executes the mandatory continuation of Paper 32.  It keeps the same
projective-residue recurrent object

```text
X_n = P^1(Z/nZ),  n >= 2,
S[a:b]=[-b:a],  R[a:b]=[-b:a+b],
```

with the same cusps, cross edges, roofs, and free edge marker.  The only new
operation is the rational Manin-relation quotient

```text
M_n = Q[X_n] / (im(1+S) + im(1+R+R^2))
```

and the chain-level filling of every `n -> 2n -> 6n <- 3n <- n` cusp diamond.

## Main result

The quotient is classical Manin-symbol machinery, and it does not repair the
primitive ledger:

- `dim M_n = |P^1(Z/nZ)| - o_S(n) - o_R(n) + 1`;
- every `n >= 2` retains the primitive cusp word `R` then `S`;
- filling all cross diamonds makes the cross complex contractible;
- the global homology is `H_1 = direct_sum_n M_n^*`, while the finite-support
  cohomology ledger is `L_fs = direct_sum_n M_n`;
- character/supercharacter controls either do not kill cycle relators or
  kill them generically while retaining the cusp word;
- the inherited adjacency `S+R` does not descend to the quotient, already at
  `n=2`.

## Exact audit

The frozen census uses all moduli `2..192`, rank checks over `F_1000003`, 191
matched relabels, 64 random transitive `C2*C3` controls, all six honest
one-dimensional characters, and all fifteen zero-superdimension differences.

Key outputs:

| Surface | Result |
|---|---:|
| relative quotient nonzero | 191 / 191 |
| composite relative survivors | 148 / 148 |
| cusp `R,S` witness returns | 191 / 191 |
| original adjacency descends | 0 / 191 |
| matched relabel exact | 191 / 191 |
| random controls residual nonzero | 64 / 64 |
| cross `H1` after filling | 0 |
| source-only generator checks | 21 / 21 |
| prototype bridge checks | 25 / 25 |
| independent low-level reconstruction | 8349 / 8349 |
| authority unit/integration tests | 1932 / 1932 |
| source-separated double run | 20 / 20 payloads |
| paper-root SHA ledger | 40 entries; 21 result payloads |

## Route-A decision

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

overall: ROUTE_A_REJECTED
route_b: LOCKED
branch_action: CLOSE_SEMIRING_RESIDUE_FAMILY
```

The next route should leave the `P^1(Z/nZ)` semiring-residue family rather than
add another static projector, Manin quotient, or character twist.

## Reproduction

```bash
cd symbolic_dynamics/papers/33-relation-homology-operator-non-descent
PYTHONDONTWRITEBYTECODE=1 python3 code/write_run_locks.py --result-dir results_check
PYTHONDONTWRITEBYTECODE=1 python3 code/source_generator.py --result-dir results_check
PYTHONDONTWRITEBYTECODE=1 python3 code/audit_source_separation.py --result-dir results_check
PYTHONDONTWRITEBYTECODE=1 python3 code/post_census_classifier.py --result-dir results_check
PYTHONDONTWRITEBYTECODE=1 python3 code/independent_evaluator.py --result-dir results_check
PYTHONDONTWRITEBYTECODE=1 python3 code/run_tests.py --result-dir results_check
python3 experiments/run_exact_suite.py
python3 code/freeze_artifacts.py --result-dir results
python3 code/audit_artifact_integrity.py --result-dir results
python3 code/audit_idempotence.py --result-dir results
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Files

- `main.pdf` — compiled paper.
- `SOURCE_LOCK.md` — frozen source object and forbidden inputs.
- `DERIVATION_PACKAGE.md`, `PROOF_PACKAGE.md`, `LITERATURE_AUDIT.md` — research
  authority packages.
- `results/` — exact CSV/JSON payloads and SHA ledgers.
- `evaluations/route_a/SD-C35/2026-08-15.yaml` — strict Route-A record.
