# C130 source audit

## Audit result

`PASS` for the literal source lock and `STOP_SCOPED` for target-facing claims.

The certificate is constructed entirely from the following frozen data:

| Item | Frozen value |
|---|---|
| adjacency | `[[1,1],[1,1]]` |
| roof | `(1,sqrt(2))` |
| matrix convention | `M(u,v)=B diag(u,v)` |
| determinant convention | `det(I-M)` |
| replay cutoff | periods 1--10, not a theorem cutoff |
| date | 2026-08-24 |
| scope | `NO_BAD_EULER_OR_ROOT_NUMBER` |

No external paper, database, web page, zero table, prime table, or numerical
fit is used.  Accordingly the paper has no bibliography and makes no
historical priority claim.  Every numerical count in the release is regenerated
from binary words; every determinant and trace coefficient is recomputed from
the frozen matrix.

## Independence audit

- `c130_suspension_producer.py` uses SymPy and emits the canonical receipt.
- `c130_suspension_checker.py` uses only the Python standard library.  It does
  not import the producer or SymPy and reconstructs polynomial matrix powers,
  primitive necklaces, and the truncated Euler product independently.
- `c130_sympy_crosscheck.py` is a fresh symbolic reconstruction and does not
  import producer routines.
- `c130_replay.py` requires byte identity with a newly generated receipt.
- `c130_mutation.py` repairs the internal payload hash after each of 43
  semantic mutations; it also tests one stale-hash mutation.  Thus a valid
  checksum cannot mask a forged claim.

## Terminology firewall

The primitive product is called a *dynamical Euler product*.  It is not an
arithmetic Euler product and supplies no local factors.  The phrase “clock
sector separation” means injectivity of the map
`(N0,N1) -> N0+sqrt(2)N1`; it does not mean injectivity on primitive
necklaces within one sector.

## Target audit

There is no target divisor against which the poles of `1/d_tau` are compared,
no target functional equation or counting law, and no source-defined natural
self-adjoint/quantum lift.  The strict evaluation must therefore remain
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` with Route B disabled.
