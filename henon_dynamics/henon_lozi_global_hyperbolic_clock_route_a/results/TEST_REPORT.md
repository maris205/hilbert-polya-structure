# Test report

Producer and independent cyclic-system checker passed on the frozen grid.
Symbolic/high-precision checks, two-directory byte replay and three smoke
tests are rerun by the release gate. The hostile lane rejects 26 repaired-hash
mathematical/metadata changes and 10 serialization changes. Release also refuses
optimized Python and checks frozen evaluation semantics, exact file membership,
PDF determinism, fonts, extracted text and all-page rasterization.
