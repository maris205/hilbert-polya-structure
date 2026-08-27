# P24 Round-4 validation

Date: **2026-08-27**

## Executed checks

```text
unit tests                                  9/9 PASS
independent build trees                     2
byte comparison                             IDENTICAL
existing-artifact verification              PASS
primary complex-length groups               18
primitive classes by multiplicity           31
alternative-algorithm prefix classes         9
alternative prefix groups                    6
maximum cross-algorithm length residual      2.2944137070481165e-31
core SHA-256                                 54dc289c26ef8466405576c29d819d2ccc0464d57c78386e1a021464d78f6875
```

The reproduction entry point is:

```bash
bash experiments/reproduce_round4.sh
```

It requires the pinned dependency `snappy==3.3.2`, runs the 9-test suite,
generates two independent temporary artifact trees, checks byte identity, and
then compares a fresh rendering with the checked-in files.  Individual file
hashes and sizes are recorded in `round4_receipt.json`.

## Verification semantics

- **Source-proved:** the named control is a finite-volume one-cusped
  non-arithmetic hyperbolic 3-manifold.  This status comes from the cited
  HIKMOT and Reid theorem chain plus the rigorous positive SnapPy isometry
  result.
- **Replayed exactly:** topology contract fields, render logic, CSV/JSON bytes,
  group counts, multiplicity totals, and two-algorithm numerical agreement.
- **Not interval verified:** decimal volume, shapes, cusp parameter, and
  complex lengths.  SageMath was unavailable; official SnapPy documentation
  limits its interval verification mode to that runtime.
- **Not evaluated:** cross-system arithmetic score, formal Route-A tuple,
  A2--A4, Route B, and Gates A--E.

No prime table, zero table, arithmetic label join, `log p` roof, or fitted
target statistic is read by the code.
