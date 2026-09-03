# Test report

All executable lanes pass under ordinary Python and explicitly refuse both `python -O` and `python -OO`.

- Producer: deterministic canonical JSON, PASS.
- Producer-independent checker: `6776` assertions, PASS.
- Independent SymPy lane: `546` exact identities, PASS.
- Isolated byte replay: two temporary directories reproduce evidence SHA-256 `03fe83cbfc95f6c227b4318de90c35a7f91a9716a0c61a7ab90ad326ebaa675d` exactly.
- Hostile suite: `141/141` attacks rejected, including repaired payload hashes, duplicate and nonfinite JSON, noncanonical rationals, string `nan`, root/phase/period mutations, duplicate/omitted/reordered coordinates, YAML aliases/anchors/merges/non-string keys, evaluator authority/status mutations, and stale-hash control.

The final release gate additionally rebuilds all three manuscript rounds twice from fresh directories at epoch `1788393600`, compares bytes, checks logs/fonts/text/rasterization, and enforces the exact 27-payload ledger.
