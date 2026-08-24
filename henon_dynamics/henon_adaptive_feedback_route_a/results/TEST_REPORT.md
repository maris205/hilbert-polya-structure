# Test report — C122

- Producer: PASS.
- Independent checker: PASS (`45` assertions after final validator hardening).
- Independent SymPy reconstruction: PASS (`29` identities/boundary checks).
- Canonical isolated replay: PASS.
- Hostile mutation audit: PASS (`16/16` rejected).
- Arithmetic: exact in `Q(sqrt(5))`; no tolerance or randomness.
- PDF and manifest checks are recorded in `paper/COMPILE_REPORT.md` and
  `C122_PREFREEZE_MANIFEST.json`.
