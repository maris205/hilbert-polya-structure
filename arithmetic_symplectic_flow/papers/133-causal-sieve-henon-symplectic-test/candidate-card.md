# Scope card — ASFS-SCOUT-20260914-97

**Version:** 1, frozen before audit, 2026-09-14.  
**Initial status:** `PRE-P0 GEOMETRY HYPOTHESIS — OPEN`.

This screen tests a precise finite-dimensional construction scheme before
classical P0. For each fixed integer N>=4 let V_N=R^{N-1}, indexed by 2,...,N,
and extend the binary sieve of 050 by its exact divisor polynomial

G_n(q)=product_{2<=d<=floor(sqrt(n)), d|n}(1-q_d).

Freeze H_N(x,y)=(y,2G(y)-x) on V_N x V_N, with the canonical form
omega_N=sum_{n=2}^N dx_n wedge dy_n. No alternative form or coefficient is
included in this card. N=4 is the decisive lowest-coordinate test, rather than
a fitted parameter. There is no claim that a finite N supplies all primes.

| Field | Frozen specification |
| --- | --- |
| Lineage | 050 candidate-support sieve -> real divisor polynomial -> second-order Hénon-type dimensional lift; exact fixed-point and geometric preservation to test |
| Object type | specified family of finite-dimensional polynomial maps with specified candidate 2-form; pre-P0 scheme test |
| Arithmetic data | divisibility and candidate coordinates; no primes, prime indicator or zero data supplied to the defining formula |
| Proposed arithmetic bridge | diagonal equilibrium equation q=G(q); interpretation OPEN before audit |
| Geometry check | inverse, determinant, and H_N^*omega_N=omega_N tested separately |
| Orbit / roof / analytic owner | no suspension or determinant selected; no A1 study before geometry gate |
| Controls | N=3 decoupled comparator; first dependency G_4=1-q_2; general scalar-force Hénon form; changed symplectic form excluded from this record |
| Decision budget | exact differential test at N=4; stop the construction scheme on failure |
| Route | classical P0 not admitted; A0/A1/A2 UNASSIGNED; Route B NOT INVOKED |

The family is not a single frozen classical ASFS candidate. A different force,
form, roof, dimension selected to evade failure, or infinite-dimensional
completion would require its own card and new proof.

## Audit outcome (same version and formulas)

**Final status:** PRE-P0 STOP — CANONICAL SYMPLECTICITY FAILS.
The derivative test fails at N=4 and at every larger N. The inverse,
unit determinant, and finite prime-indicator equilibrium remain exact controls.
Classical A0/A1/A2 stay unassigned; Route B NOT INVOKED.
See [paper](paper.md) and [claim ledger](claim-ledger.md).
