# Results

## Theorem result

For every dominant weight in every finite reduced crystallographic root
system, all legal positive-coordinate firing sequences terminate at
`w_0 lambda`.  With `J` the zero-coordinate set, every complete sequence
accumulates to the same element `w_0w_J` and has the same length
`|Phi^+|-|Phi_J^+|`.  Strict, wall, zero, disconnected, and rank-one cases are
included; affine and indefinite types are outside scope.

## Exact evidence scale

| ledger family | rows |
|---|---:|
| locked cases | 23 |
| complete legal branches | 3332 |
| depth levels | 143 |
| boundary semantics | 8 |
| total | 3506 |

The cases cover `A1--A4`, `B2--B3`, `C2--C3`, `D4`, `G2`, and
`A2+A1`, with strict and wall branches plus rank-one and zero controls.

## Independent gates

- producer: `C286_PRODUCER_PASS`, 1,296,292 bytes;
- checker: PASS, 19,056 assertions from positive-root/inversion/coset
  reconstruction;
- SymPy: PASS, 577 symbolic matrix/root checks;
- replay: PASS in two different fresh paths;
- hostile mutation: PASS, 84/84 raw duplicate-key, repaired-hash
  semantic/schema/type/drop-replace attacks, and stale-hash control;
- evidence file SHA-256:
  `e770246fe3d448e684b2adc50465dc715ff0e4008db3c9616a28719a84588081`;
- canonical payload SHA-256:
  `d3b0b4dc922bd445ee3a71e012dd46b037acd0586b889533a41fe0d57dedd65a`.

The evidence tests implementation conventions.  The proof of the all-system
theorem is the finite parabolic weak-order argument and is independent of
small-rank enumeration.

## Route disposition

The exact tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` and the overall verdict is
`ROUTE_A_REJECTED`.  Route B is false.  The result carries no prime clock,
periodic-orbit ledger, target determinant, analytic target bridge, or natural
same-clock quantum operator.
