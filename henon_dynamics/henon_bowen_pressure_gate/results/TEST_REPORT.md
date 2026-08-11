# HCS-C31 test report

The suite passes 30/30 tests. Positive controls cover graph census,
chronological orientation, all cylinder expansion intervals, strict endpoint
margins, integer-square-root containment, rational log/exp ordering, and
producer/checker independence.

Rehashed adversarial mutations are rejected for:

- transposed adjacency and swapped edge incidence;
- missing edges and corrupted sign chronology;
- illicitly narrowed Jacobian intervals or altered Jacobi rounds;
- changed square-root rounding grids;
- swapped root endpoints and altered bracket width;
- boolean or destroyed Collatz vectors and forged margins;
- source drift, unknown nested fields, stale payload hashes, and grafted
  numerical targets;
- false Fredholm/Hilbert--Pólya promotion.
- false Route-A A2 promotion despite the certified pressure theorem.

Malformed JSON is rejected by an isolated checker process. Run the complete
test and byte-reproduction path with `./code/run_c31.sh`.

Semantic contract violations are reported as `FAIL`. Unexpected checker
exceptions are reported separately as `ERROR`; an explicit exception sentinel
prevents implementation crashes from masquerading as successful mutation
rejection.

The release-manifest test freezes the complete 40-file authored package and
deletes every required path in an isolated fixture.  Each deletion must fail
closed, so an intentional manifest refresh cannot silently bless a package
missing its theorem, Route-A record, paper source, PDF, code, or result ledger.
