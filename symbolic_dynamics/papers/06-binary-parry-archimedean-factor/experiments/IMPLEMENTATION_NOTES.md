# Paper 06 Implementation Notes

## Entry points

Run from the Paper06 directory:

```bash
python code/symbolic_archimedean_experiment.py --out results
python code/test_symbolic_archimedean_experiment.py
```

The implementation requires Python 3, NumPy, SciPy, and mpmath. It is CPU
only and completes in a few seconds in the recorded environment.

## Exact finite inventories

`recovered_multiplicative_atoms` marks every product ab <= N with a,b > 1
and returns the unmarked nonunit elements. This reconstructs the tensor
atoms from the multiplication law without reading a prime table.

The binary and biased Bernoulli laws are evaluated from log-binomial
probabilities. The K₃ and K₄ radial controls enumerate multinomial count
vectors. For regular-simplex vertices v_i, the squared norm of the count
sum is

```text
||sum_i c_i v_i||² = (q sum_i c_i² - N²)/(q-1).
```

No arbitrary Euclidean embedding or scalar projection enters the radial
control.

## Tilted trace convention

The sign observable is ordered as (-1,+1). The executable uses

```text
H_cyc(u) = K₂ diag(exp(-iu), exp(iu)).
```

Because H_cyc(u) is rank one with nonzero eigenvalue cos(u), the code checks
tr H_cyc(u)^N = cos(u)^N directly. The manuscript's symmetric form
H_sym(z) = exp(zQ/2) K₂ exp(zQ/2) is the cyclic/similar representative of
the same tilted transfer, with z = iu up to the frozen sign convention.
Both have identical power traces and characteristic determinants.

The chiral reference X = [[0,1],[1,0]] is the swap matrix. It is distinct
from the all-ones matrix J₂ used in K₂ = J₂/2.

The self-dual Mellin scale is applied as Y_N = S_N/sqrt(2 pi N).

## Numerical stability

- Binomial/multinomial probabilities are formed using `gammaln` and then
  normalized.
- Complex Gamma targets use `loggamma` before exponentiation.
- Odd binary cutoffs avoid a finite-N atom at zero for negative moments.
- Relative error can be enormous where the complex Gamma target is tiny;
  the complete grid is retained instead of clipping or selecting points.
- Algebraic chiral, determinant, and trace checks report operator-norm or
  absolute residuals.

## Controls and interpretation

Uniform and biased rank-one kernels all pass the stationary trace ledger.
The reversible lambda = 0.4 kernel is the intended failing control, with
tr K^r = 1 + 0.4^r. Arbitrary scalar CLT observables can recover the
one-dimensional Gamma target and are labeled proves-too-much. Canonical
radial K₃ and K₄ instead converge to dimension-shifted targets.

The global inventory Parry/Hellinger experiment is kept separate from the
SD-C08 binary fiber. Its shifted/random controls show that Hellinger product
identities alone are not arithmetic-specific.

## Reproducibility contract

The script writes seven frozen results deterministically. A second run to a
fresh directory must be byte-identical. The six tests cover:

1. K₂ idempotence, Euler ledger, and tilted trace identity;
2. chiral square identity;
3. completed-Gamma normalization;
4. characteristic-function and local-CLT convergence;
5. radial K₃/K₄ rejection of the binary target;
6. reversible-kernel ledger failure.

No PDF, manuscript, root README, manifest, or git operation is performed by
the experiment script.
