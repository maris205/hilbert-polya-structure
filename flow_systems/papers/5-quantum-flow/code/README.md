# Deterministic Koopman Controls

The code checks finite, exact consequences of the Paper 5 proof:

- Möbius counts for closed points of \(\mathbb P^1/\mathbb F_2\);
- fixed-point reconstruction from the primitive degree ledger;
- finite prefixes of the degree-\(kb\), mode-\(ka\) multiplicity witnesses;
- a finite Fourier-vector regression for the positive-weight unitary
  intertwiner.

It does not infer the infinite spectral theorems from finite samples. Those
proofs are in `../notes/proof_audit.md`. The program contains no target-zero
data, fit, optimization, randomness, or network access.

Reproduce from the Paper 5 directory with:

```bash
./experiments/reproduce.sh
```

