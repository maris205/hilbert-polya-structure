# Test report

- Producer: `C270_PRODUCER_PASS trajectories=800 distance=64 vertical=12
  numeric_cells=10972`.
- Independent checker: `PASS (11139 assertions; Hamilton endpoints, Jacobian,
  distance, cut boundary)`.
- SymPy: `PASS (20 symbolic identities; flow, bracket, Jacobian, distance
  limits)`.
- Byte replay: exact, 905104 evidence bytes.
- Hostile repaired-hash mutations: `PASS 27/27`.
- Manifest target: `C270_MANIFEST_PASS`, 27 payload files and 28 physical files.

No finite table is used to prove a global geometric statement.  The cut and
conjugate conclusions are analytic; the rows are deterministic regression
receipts.
