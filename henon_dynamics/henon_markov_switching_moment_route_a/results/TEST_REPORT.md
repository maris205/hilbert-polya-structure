# Test report — C117

- Deterministic producer: PASS.
- Independent semantic checker: PASS.
- SymPy/Newton cross-check: PASS (`26` exact checks).
- Canonical-byte replay: PASS.
- Hostile mutations: PASS (`12/12` rejected).
- Model arithmetic: exact over `Q`; no sampling or tolerance.
- Paper audit: fixed-date isolated double build, page/font/log checks recorded in
  `paper/COMPILE_REPORT.md`.
- Manifest: all non-generated package files are content-addressed.
