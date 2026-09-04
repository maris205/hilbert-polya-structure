# Test report

All five computational lanes pass under ordinary Python and explicitly refuse both `python -O` and `python -OO`:

- producer: canonical payload PASS;
- independent checker: 167 assertions PASS, including exact schema/date/path
  literals and ordered mass/lattice coordinate ledgers;
- SymPy: 17 exact identities PASS;
- isolated replay: two byte-identical runs PASS;
- hostile mutation: 57 attacks PASS.

The release gate additionally validates strict JSON/YAML, raw and semantic evaluation locks, exact 27-payload ledger, deterministic PDFs, warnings, embedded subset fonts, extracted text, rasterization, and self-excluding manifest closure.
