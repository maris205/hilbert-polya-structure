# Session 4 Candidate Registry

Candidate definitions and stop rules are frozen in
[`../SESSION4_PREREGISTRATION.md`](../SESSION4_PREREGISTRATION.md).  Formal
Route-A decisions are append-only under `../evaluations/route_a/`.

| ID | Object | Frozen Route-A tuple | Overall status | Strongest failure | Route-B |
|---|---|---|---|---|---|
| [`SD-C01`](../evaluations/route_a/SD-C01/20260812T090631Z.yaml) | finite-state function-field arithmetic skeleton | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)` | `ROUTE_A_REJECTED` | rational-prime A0 absent; divisor growth is $O(R)$ | locked |
| [`SD-C02`](../evaluations/route_a/SD-C02/20260812T090631Z.yaml) | squarefree admissible shift | `(A0_FAIL, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)` | `ROUTE_A_REJECTED` | only the all-zero periodic point | locked |
| [`SD-C03`](../evaluations/route_a/SD-C03/20260812T090631Z.yaml) | weighted renewal determinant | `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_REJECTED` | inverse-design `PROVES_TOO_MUCH`; mixed primitive words | locked |
| [`SD-C04`](../evaluations/route_a/SD-C04/20260812T090631Z.yaml) | Gauss/Mayer countable transfer | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)` | `ROUTE_A_EXPLORATORY` | modular primitive species, not rational primes | locked |
| [`SD-C05`](../evaluations/route_a/SD-C05/20260812T090631Z.yaml) | recursive wheel-sieve level shift | `(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | directed acyclic graph; no primitive cycles | locked |
| [`SD-C06`](../evaluations/route_a/SD-C06/20260812T090631Z.yaml) | Knauf binary arithmetic recursion | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_FAIL, A2_FAIL, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)` | `ROUTE_A_EXPLORATORY` | zeta quotient is not a periodic-orbit Fredholm determinant | locked |

An object is not promoted because it has an attractive finite plot.  Arithmetic
origin, primitive/repetition ledger, determinant convention, extra zeros, and
controls remain separate columns in every evaluation.

No single object reaches `A4_ROUTE_B_READY`.  In particular, the A0 strength
of `SD-C05`, the determinant of `SD-C04`, and the zeta quotient of `SD-C06`
must not be assembled coordinatewise.
