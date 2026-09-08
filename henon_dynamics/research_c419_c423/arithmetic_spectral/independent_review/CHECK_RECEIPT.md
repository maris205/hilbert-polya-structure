# Exact check receipt

The [bounded contract](FROZEN_CHECK.md) and
[script](exact_check.py) were written before the first execution.
Exactly one numerical/symbolic run was performed; there was no search.

Command from `/root/autodl-tmp/hilbert-polya-structure`:

```text
python henon_dynamics/research_c419_c423/arithmetic_spectral/independent_review/exact_check.py
```

Execution date: 2026-09-07. Exit code: 0. Reported command wall time:
0.609524137 seconds. Full stdout:

```json
{
  "scope": "N=50 only; s=2, t=3; exact Q(i) arithmetic",
  "young_formula_reconstruction": "PASS at s=2,3,-1,-2",
  "fixed_plus_block_s2": "Matrix([[0, 8/17 - 36*I/17], [8/17 + 36*I/17, 0]])",
  "fixed_plus_block_s3": "Matrix([[0, 32/65 - 264*I/65], [32/65 + 264*I/65, 0]])",
  "normalized_plus_commutator": "Matrix([[384*I/221, 0], [0, -384*I/221]])",
  "full_normalized_fixed_block_commutator_nonzero": true,
  "classification_claimed": false
}
```

The script reconstructs $C_\chi(s)$ from Young's actual divisor sum,
not from the proposed closed matrix alone. The values $-1,-2$ are the
functional-equation arguments corresponding to $2,3$, not additional
scattering probes. The analytic scalar, regularity, full Fourier basis,
and true invariant-subspace arguments are proved in
[PROOF_PACKAGE.md](PROOF_PACKAGE.md); the finite computation does not
certify those mathematical prerequisites by itself.

No old principal-character probe, all-level census, manuscript,
evaluation, Git mutation, GPU job, paid model, or external upload was
performed by this independent review.
