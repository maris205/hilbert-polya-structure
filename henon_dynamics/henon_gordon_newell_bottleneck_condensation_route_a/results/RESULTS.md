# Results — HCS-C285

## Theorem result

The frozen arbitrary finite irreducible Gordon–Newell owner is proved as
stated. The theorem covers nonreversible routing and closes:

- `pi_N(n)=Z_N^(-1) product_i w_i^(n_i)` with `Z_N=h_N(w)`;
- every joint factorial/ordinary occupancy moment and covariance by weight
  derivatives;
- exact busy probabilities, station throughput, directed service-event flow,
  and divergence-free stationary currents;
- `p*_ij=e_j p_ji/e_i`, involution, and reversibility iff traffic detailed
  balance for `N>=1`;
- the full normalizer asymptotic and joint independent-geometric plus
  `Dirichlet(1,...,1)` bottleneck limit;
- unique, tied, all-equal, `N=0`, `N=1`, `m=1`, zero-edge, self-route, traffic
  gauge, zero-service/zero-weight, reducible, and invalid-population faces.

The all-parameter and thermodynamic statements are carried by the written
proof. Finite cells are regression evidence only.

## Exact executable result

- network case rows: 9
- complete state rows: 177
- `Z_N` rows, each with three independent routes: 9
- moment rows: 9
- joint factorial cells through total degree three: 165
- flow rows: 9
- reversal rows: 9
- finite condensation rows: 28
- boundary rows: 12
- producer-independent checker assertions: 11,628
- SymPy identities: 28
- repaired/structural/type/stale/duplicate-key hostile rejections: 64/64
- evidence bytes: 158,346
- evidence payload SHA-256:
  `1a301c0b96ff32590088ea1a46f62d52fb90dd3aeee447050e6315e5c5511bb0`
- evidence file SHA-256:
  `981db83511e8bcccd0f8296ca98ae7a7035a475cba0661b3361836488c062106`

Two fresh output paths reproduce the exact evidence bytes and each passes the
independent checker.

## Paper result

| round | pages | SHA-256 |
|---|---:|---|
| 0 | 2 | `281d88d391a2ca9fdf79ba30ac840959150bf9081954571e7c9543c0ea798fe5` |
| 1 | 3 | `ab2bf74aa9be4ab4a1a33b1b584755ab505e807134514b40e9bdb781ea13052d` |
| 2/final | 4 | `088d2ca85d86d1e1fc797071bef5aa8c4a4364178f0ab61f454d77df14e6000e` |

The three hashes are distinct; `paper/main.pdf` is byte-identical to round 2.
Every fresh-build pair matches the archived round. All PDF fonts are embedded
and subset, logs are warning-free, extracted text contains the theorem,
boundary, source and Route-A contracts, and all nine rendered pages passed
visual inspection.

## Ownership and Route-A result

Gordon and Newell (1967) are the explicitly cited classical owner; no
originality claim is made. The closest repository mechanisms remain distinct.
The strict result is

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,

overall `ROUTE_A_REJECTED`, Route B `false`, with literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`. No formal quantization is offered.
