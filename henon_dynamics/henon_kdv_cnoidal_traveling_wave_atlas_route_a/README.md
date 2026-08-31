# HCS-C256 — KdV cnoidal traveling-wave atlas

C256 closes one theorem-scale coherent-family problem for

```text
u_t + 6 u u_x + u_xxx = 0.
```

Every bounded classical traveling profile is classified by the real-root
topology of its cubic first integral.  The nonconstant cases are the complete
three-simple-root cnoidal family and its lower-double-root soliton face.  The
package gives the exact profile, speed, fundamental period, first two period
moments, Galilean covariance, harmonic and constant boundaries, and the
physical-time return on the fundamental circle.

## Reproduce

```bash
python3 -B code/c256_kdv_producer.py
python3 -B code/c256_kdv_checker.py
python3 -B code/c256_kdv_sympy_crosscheck.py
python3 -B code/c256_kdv_replay.py
python3 -B code/c256_kdv_mutation.py
python3 -B code/c256_release_manifest.py
```

The 12 finite root rows are exact/high-precision regression oracles, not a
substitute for the all-root proof.  The strict Route-A tuple is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall
`ROUTE_A_REJECTED`, and Route B is false.  Scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.

The formulas are classical and are re-derived source-locally; no
literature-priority claim is made.  No arithmetic local datum, Euler factor,
root number, automorphy statement, target divisor, Hilbert--Pólya operator, or
Route-B input is introduced.
