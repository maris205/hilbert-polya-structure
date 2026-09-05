# Test report

- producer: `C384_PRODUCER_PASS payload_sha256=3dee0493d46b7dce38a0f150a51d86fece0a2259cc59131a768b48bdf7e35e6c`
- checker: `C384_CHECKER_PASS assertions=214816`
- sympy: `C384_SYMPY_PASS exact_checks=825`
- replay: `C384_REPLAY_PASS isolated_directories=2 exact_byte_match=true`
- mutation: `C384_MUTATION_PASS rejected=58/58 json=48 yaml=10`
- smoke: `3 tests PASS`

All six scripts were run under both -O and -OO, producing twelve explicit optimized-mode refusals. Strict source/YAML gates, exact membership and PDF checks passed. Finite evidence is regression, not an infinite proof.
