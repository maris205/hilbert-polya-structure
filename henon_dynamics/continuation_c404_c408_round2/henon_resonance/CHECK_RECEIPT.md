# Bounded exact-check receipt

Date: 2026-09-06. Command from repository root:

```sh
python -B henon_dynamics/continuation_c404_c408_round2/henon_resonance/exact_checks.py
```

The successful run exited **0** in approximately **0.61 s**. Its output is preserved, with JSON whitespace compacted, in [exact_results.json](exact_results.json). Environment: Python 3.12.3, SymPy 1.14.0. The program prints to stdout and does not read old results, write registry/state files, or run any prior sealed package.

## What was actually checked

Literal composition of $H$ constructs both fixed polynomials. It does not use the proved degree recurrence to construct them. Exact field arithmetic then computes their actual degrees, highest homogeneous terms, and Jacobian determinant. The count derived from coprime highest monomials uses the same elementary quotient-length principle as the proof, so this is not described as a wholly independent mathematical proof.

Three prime-subfield coefficient cases were additionally passed to SymPy's F5B Gröbner routine, and their standard-monomial lengths independently computed from the returned basis. The two genuine $\mathbb F_4$ coefficient cases are explicitly marked `NOT_RUN_NONPRIME_FIELD_COEFFICIENTS` for that secondary method; SymPy's `GF(4)` was not misused as a field.

For $\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)$, the integer codes $2,3$ mean $\alpha,\alpha+1$. Those cases use $a=\alpha+1$ and

$$
g(y)=\alpha y^3+(\alpha+1)y^2+y+\alpha.
$$

| Case | Period | Literal degrees | Geometric count | Role |
|---|---:|---|---:|---|
| $q=5$, $a=2$, $g=2y^3+3y^2+y+4$ | 2 | $(25,15)$ | 375 | Prime-to-$p$ clock with lower-coefficient perturbation |
| $q=9$, $a=2$, $g=2y^2+y+1$ | 3 | $(729,92)$ | 67068 | Wild clock over a nonprime base-field size |
| Genuine $\mathbb F_4$ coefficients above | 2 | $(16,11)$ | 176 | Non-prime-field leading and lower coefficients |
| Same genuine $\mathbb F_4$ map | 4 | $(256,171)$ | 43776 | Next $p$-power level, not only the first cancellation |
| $q=8$, $a=1$, $g=y^6+y^3+1$ | 2 | $(64,44)$ | 2816 | Deliberately outside $p\nmid m$: invalid extension predicts 2944 |

These are new inputs, not reruns of the sealed monomial examples. Agreement of the value 176 with an older result is an expected consequence of coefficient-uniformity, not reuse of its equations or output.

The out-of-scope example remains genuinely nonadditive. Its leading degree $m=6$ is divisible by $p=2$, and the theorem is not applied to it. The successful discrepancy test establishes that the coprimality assumption cannot simply be deleted; it is not a classification of all degrees divisible by $p$.

## Actual initial failure and repair

The first invocation exited **1** after approximately **0.26 s**, with `TypeError: Object of type nmod is not JSON serializable`. The failure occurred when hashing the first case after the SymPy check: `Poly.from_dict` had normalized coefficients in the supplied dictionary. No complete result set was produced or treated as successful.

The repair was to give SymPy copies of the two dictionaries, preserving the exact-field producer's original values. The subsequent invocation is the successful run recorded above. No mathematical formula or expected count was adjusted to accommodate this implementation failure.

No timing benchmark, large census, numerical zeta extrapolation, or all-period validation claim is made. The universal argument is [PROOF_PACKAGE.md](PROOF_PACKAGE.md), and independent manuscript-level review is a separate gate.
