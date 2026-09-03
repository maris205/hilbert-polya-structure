# Test report

- Producer: PASS, 693 audited scalar leaves.
- Independent checker: PASS, 886 checks; it imports no producer code.
- SymPy lane: PASS, 5,125 exact identities.
- Isolated byte replay: PASS, two reproductions.
- Hostile suite: PASS, 70/70 attacks rejected, including repaired hashes and
  mutation of the fixed-point initial-value closure.
- Every executable explicitly refuses optimized Python.
- The release gate additionally rebuilds every PDF round twice in fresh
  directories, checks clean logs, text, rasterization and embedded/subset
  fonts, rejects bare `qquad` rendering, and enforces exactly 27 payloads plus
  one self-excluded manifest.
