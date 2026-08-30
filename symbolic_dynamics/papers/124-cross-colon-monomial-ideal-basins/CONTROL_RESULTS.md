# P124 exact-control results

Status: **ROUND2 GO_INTERNAL / EXTERNAL HOLD**.

Run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_alg_cross_colon.py
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_alg_cross_colon_basins.py
```

Both programs use only the Python standard library, make no network call or
random draw, and use no floating-point comparison.  Their canonical
transcripts are stored beside them in `code/`.

## Core dynamics lane

```text
cross-colon monomial-ideal dynamics independent control: PASS
assertions=1469669
path_words=131064; path_lengths=1..14; source_types=00,10,01,11
rectangles=81; parameter_grid=a,b=1..9; ideals=184736
literal_vs_staircase_vs_diagonal=PASS
fixed_two_cycle_recurrent_classification=PASS
sharp_depth_and_witnesses=PASS
global_depth_hist={0: 693, 1: 8656, 2: 27401, 3: 36536, 4: 39774, 5: 28400, 6: 25472, 7: 13192, 8: 4612}
```

## Basin lane

```text
cross-colon basin transfer independent control: PASS
assertions=265987
literal_rectangles=64; parameter_grid=a,b=1..8; ideals=48602
literal_attractors_vs_first_trace=PASS
contact_transfer_vs_exhaustive_basins=PASS
ballot_partition_and_swap_identities=PASS
large_transfer_grid=a,b=1..30; nontrivial_triples=8555
example_a5_b7_orbit_basins=[(('C', 1), 10), (('C', 2), 45), (('C', 3), 116), (('C', 4), 185), (('P', 1), 2), (('P', 2), 9), (('P', 3), 38), (('P', 4), 90), (('P', 5), 297)]
example_a5_b7_trace_phases=[(1, (4, 6, 1)), (2, (30, 15, 9)), (3, (44, 72, 38)), (4, (139, 46, 90))]
```

Combined assertions: **1,735,656**.

Canonical SHA-256 values:

- core: `b924e05c5e9ac71a25fb668d5bc2033f6ab58c325c7c73642a4dd0b096d67deb`;
- basins: `bdfd3e041b9f641101436c40918adbba59fd14b1f1381d77fa943ce00c0c76ff`.

These are finite falsification controls, not all-parameter proofs or owner
certificates.

## Round-2 fresh reproduction

Both programs were run again from the paper directory with
`PYTHONDONTWRITEBYTECODE=1`.  Fresh stdout compared byte-for-byte equal to its
corresponding canonical transcript:

| Lane | Assertions | Fresh/canonical comparison | Canonical SHA-256 |
|---|---:|---|---|
| core dynamics | 1,469,669 | `cmp` exit 0 | `b924e05c5e9ac71a25fb668d5bc2033f6ab58c325c7c73642a4dd0b096d67deb` |
| basins/transfer | 265,987 | `cmp` exit 0 | `bdfd3e041b9f641101436c40918adbba59fd14b1f1381d77fa943ce00c0c76ff` |
| **combined** | **1,735,656** | **PASS** | — |

The verifier sources themselves remain frozen at SHA-256
`950953523155868efec1491e69038b1d30c33249b1df2daa7881c74012242cbf`
and
`51ca13655933b869ce8e4b12c868d550a107496c013136e2e5fa18ad9b481f22`,
respectively.

## Internal collision firewall

- **P107:** its map is `I -> Ann(I)^r` on ideals of `Z/NZ`; CRT valuation
  coordinates and clipped reflection drive its cycles and transients.  P124
  instead uses monomial ideals in a truncated bivariate ring, crossed
  variable colons, sourced OR diagonals, and a first-trace basin transfer.
  The literal carriers and mechanisms differ, but generic language such as
  “ideal dynamics with exact cycles and depth” receives no contribution
  credit here.
- **P104:** it is a random contraction cocycle.  It has no ideal lattice,
  colon operation, diagonal Boolean dynamics, or basin transfer.  The shared
  vocabulary “monomial” and “toggle” is nonstructural and carries no value.
