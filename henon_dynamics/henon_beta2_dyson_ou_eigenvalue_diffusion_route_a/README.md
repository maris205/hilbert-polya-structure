# HCS-C378: beta-two Dyson--OU eigenvalue diffusion

This package fixes the trace-metric Hermitian Ornstein--Uhlenbeck
normalization and proves, for every finite matrix size, the ordered
eigenvalue SDE, the Karlin--McGregor/Doob transition kernel, GUE reversibility,
noncollision, and the complete symmetric-Hermite partition spectrum with
sharp gap $1/2$.

## Artifacts

- `THEOREM_PACKAGE.md`: line-by-line proof package.
- `paper/main.pdf`: final manuscript; all three theorem-increment PDFs are
  retained.
- `results/c378_dyson_ou_evidence.json`: canonical finite regression receipt.
- `evaluations/route_a/HCS-C378/2026-09-04.yaml`: strict evaluator record.
- `SOURCE_AUDIT.md`: primary-source and collision ledger.
- `code/`: producer, code-independent checker, SymPy lane, isolated replay,
  hostile mutation suite, and release gate.
- `C378_RELEASE_MANIFEST.json`: exact self-excluded payload ledger.

Strict Route-A tuple:

```text
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
```

Overall: `ROUTE_A_REJECTED`. Scope:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
