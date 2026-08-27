# C201 test report

- deterministic producer: PASS — 14 parameter cases and 28 endpoint blocks;
- independent checker: PASS — 478 assertions with exact nested key sets;
- separate SymPy route: PASS — 156 checks;
- byte replay: PASS;
- hostile mutation suite: PASS — 18 repaired-hash and 1 stale-hash rejection,
  including 2 unknown-key attacks;
- exact source ledger: PASS — 238 declared scalar controls plus matrix and
  finite-order reconstruction;
- scope and Route-B flags: PASS.

The manuscript proof, not the finite controls, establishes the all-real
parameter theorem.  PDF and manifest audits are closed in the release ledger.
