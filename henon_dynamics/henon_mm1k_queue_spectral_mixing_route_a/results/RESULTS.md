# Results — HCS-C225

The exact ledger has 20 stationary rows (four rate cases × five capacities),
60 nonzero Jacobi modes, 240 entrywise kernel rows and 240 linked TV/mixing
rows.  Sixteen rows track `K=4,8,16,32` capacity limits for each rate case;
eight rows state the singular and recurrence faces.

The finite theorem passes an independent 3,655-assertion checker.  SymPy
returns 46 exact identities, clean replay is byte-for-byte, and the hostile
mutation suite rejects 25 repaired-hash mutations (including two unknown-key
schema attacks) plus one stale-hash mutation.  See `TEST_REPORT.md` for the
command transcript and the release manifest for sealed hashes.

Route-A remains `ROUTE_A_REJECTED` with tuple
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route B is false.
