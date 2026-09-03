# Test report

- Producer: PASS.
- Independent checker: PASS, 4,414 checks.
- SymPy: PASS, 2,621 exact identities.
- Isolated replay: PASS, two byte-identical reproductions.
- Hostile suite: PASS, 80/80 attacks rejected.
- Every Python executable rejects optimized mode.
- Release gate additionally rebuilds each PDF twice, verifies raster/text/font properties, enforces the 28/27 ledger, and checks the self-excluding manifest.
