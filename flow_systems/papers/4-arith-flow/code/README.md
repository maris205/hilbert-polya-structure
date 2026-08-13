# Deterministic controls

`frobenius_suspension_controls.py` enumerates monic polynomials over
\(\mathbb F_2\), certifies irreducibility, reconstructs the closed-point and
fixed-point ledgers of \(\mathbb P^1/\mathbb F_2\), checks the formal orbit-zeta
identity, and runs the one-clock and arbitrary-circle controls.

The program uses no external package, network access, Riemann-zero data,
fitting, or random seed.  Generated finite tables are regression tests for the
proofs in `../notes/proof_audit.md`, not substitutes for those proofs.

Run the full suite from the paper directory with:

```bash
bash experiments/reproduce.sh
```

