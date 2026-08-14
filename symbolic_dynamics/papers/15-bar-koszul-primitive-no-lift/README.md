# Paper 15 — Primitive-Cycle No-Lift for the Tensor Bar Code

Candidate **SD-C17** tests the strongest natural bar-to-Koszul reduction of
the tensor symbolic determinant.  The squarefree subset shift has the exact
scalar determinant

\[
D_A(x,1)=\prod_{a\in A}(1-x_a),
\qquad
D_\infty(s,1)=\zeta(s)^{-1}\quad(\operatorname{Re}s>1),
\]

but it has no primitive-cycle lift compatible with temporal powers and atom
permutations.

## Main result

- At `p^2q^2`, the primitive ledger is `1+ / 2-`; its signed sum `-1` is
  canceled only by two `r=2` repetitions from content `pq`.
- At `pqr`, the virtual `S_3` character is
  `1 + sign - standard = (0,0,3)`, so no equivariant pairing exists.
- Scalar repetition `(-w)^r` is not odd supertrace `-w^r`.
- A genuine acyclic chain sector has graded determinant `1`, while Koszul and
  HKR homology retain mixed exterior classes.

Therefore:

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

## Reading map

- Paper: [`main.pdf`](main.pdf)
- Frozen object: [`SOURCE_LOCK.md`](SOURCE_LOCK.md)
- Proofs: [`PROOF_PACKAGE.md`](PROOF_PACKAGE.md)
- Derivation: [`DERIVATION_PACKAGE.md`](DERIVATION_PACKAGE.md)
- Literature boundary: [`LITERATURE_AUDIT.md`](LITERATURE_AUDIT.md)
- Exact experiment report: [`EXPERIMENT_REPORT.md`](EXPERIMENT_REPORT.md)
- Cross-family clues only: [`ROUND2_CLUES.md`](ROUND2_CLUES.md)

## Reproduction

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=code \
  pytest -q -p no:cacheprovider code/test_sdc17_bar_koszul_experiment.py
python code/sdc17_bar_koszul_experiment.py
sha256sum -c results/SHA256SUMS.txt
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The experiment uses exact integer and rational arithmetic and no Riemann-zero
data.  The next in-family obligation is a character-resolved cycle-index
determinant that retains the nontrivial representation modes erased by scalar
dimension.
