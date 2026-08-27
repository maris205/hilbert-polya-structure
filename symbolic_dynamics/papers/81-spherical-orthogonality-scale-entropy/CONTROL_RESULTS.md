# Deterministic control results

Command:

```bash
python3 code/verify_orthogonality_shift.py
```

Status: **PASS**.

- signed-coordinate bridge/closing checks: `18,240`;
- exact Jacobian rank/dimension checks: `192`;
- Gegenbauer/Funk spectral checks: `208`.

Total reported checks: **18,640**.  These exact controls probe the geometric
constructions and formulas but do not replace the continuum proofs.
