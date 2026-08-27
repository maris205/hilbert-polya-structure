# C200 test report

- deterministic producer: PASS — 9 cases, 1,206 exact scalar identities;
- independent checker: PASS — 1,819 assertions and exact nested key sets;
- separate SymPy route: PASS — 171 checks;
- byte replay: PASS;
- hostile mutation suite: PASS — 15 repaired-hash and 1 stale-hash
  rejection, including 2 unknown-key attacks;
- continuous theorem boundary: PASS — manuscript proof, not finite-grid
  inference;
- scope and Route-B flags: PASS.

PDF reproducibility, fonts, log, text, page inspection and the 27-payload
ledger are closed by the release manifest.
