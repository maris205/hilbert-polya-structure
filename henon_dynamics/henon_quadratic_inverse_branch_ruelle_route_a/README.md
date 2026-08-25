# HCS-C141 — quadratic inverse-branch Ruelle operator

C141 freezes \(F(z)=z^2-6\) on \(\mathbb D_4\) and proves that its two inverse branches generate a trace-class Hardy transfer operator. The headline \(m=2\) traces retain multiplier stability, while \(m=0\) and \(m=1\) collapse exactly to \(2^n\) and zero.

## Main deliverables

- `THEOREM_PACKAGE.md`: full theorem and proof.
- `results/c141_quadratic_ruelle_evidence.json`: exact period polynomials, traces, counts, and determinant coefficients.
- `paper/main.pdf`: final short paper; round snapshots are retained.
- `evaluations/route_a/HCS-C141/2026-08-25.yaml`: strict Route-A evaluation.
- `C141_RELEASE_MANIFEST.json`: self-excluded content-addressed ledger of 27 payloads.

## Reproduce

```bash
python3 code/c141_quadratic_ruelle_producer.py
python3 code/c141_quadratic_ruelle_checker.py
python3 code/c141_sympy_crosscheck.py
python3 code/c141_replay.py
python3 code/c141_mutation.py
python3 code/c141_release_manifest.py
```

## Strict boundary

Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`. The tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall `ROUTE_A_EXPLORATORY`, and Route B is false. The source dynamical primitive product is not an arithmetic Euler product. No target divisor, functional equation, natural quantization, automorphy, root number, or Hilbert--Pólya claim is made.
