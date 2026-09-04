# Results

## Exact ledger

- Degrees: \(D=4,6,8,10\).
- Radial DP: 1,156 parity-compatible state rows through time 32.
- Even returns: 260 rows through half-time 64, including time zero.
- First returns: 256 rows through half-time 64.
- Renewal convolution: 256 rows.
- Spectral/escape parameters: 4 rows.
- Rank-one boundary: 65 rows.
- Total: 1,997 exact rows and 9,483 scalar cells.

Evidence SHA-256: `15feff3f64a697dd0323d47b56add823e6c58d43eafa48cf8cc5e361f274a878`.
Self-excluding payload SHA-256: `ea6e1bda3d8c93acbd126a38b5fb62bf4ce81af53445512c04a9a2b70ba4769e`.

## Analytic outcome

The paper proves the complete pure-AC spectrum and Kesten root density, not merely finite spectral approximations.  Weighted Dyck paths prove every return/first-return coefficient.  A pathwise i.i.d. coupling with an almost surely finite boundary correction proves the strong law and radial CLT.  The \(d=1\) face is separately proved.

## Scope outcome

Route-A tuple: `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; overall `ROUTE_A_REJECTED`.  Route B is false and all forbidden scope flags are false.
