# Test report

The release lanes report:

- deterministic producer: `C349_PRODUCER_PASS`;
- producer-independent checker: 9,540 assertions;
- independent SymPy lane: 767 exact identities, including the repeated-face
  bracket, energy relation, and rank-two witness;
- two-directory byte replay: exact match to the checked-in evidence;
- hostile mutation suite: 152/152 attacks rejected;
- all five lane programs and the release program explicitly reject both
  `python -O` and `python -OO`;
- strict JSON duplicate/nonfinite rejection and strict YAML
  duplicate/anchor/alias/merge/non-string-key rejection;
- exact evaluator raw and semantic locks;
- three deterministic, warning-free manuscript rounds with embedded/subset
  fonts, extracted-text sentinels, and per-page raster checks;
- exact self-excluding 27-payload/28-physical release ledger.

The final release is required to pass once with `--write` and twice without
write before handoff.
