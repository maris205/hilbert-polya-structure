# Source-lock amendment: v1 to v2

At the pre-execution integrity check, the recorded development seed in v1 did
not match its frozen derivation rule.

- Frozen rule: the unsigned big-endian integer represented by the first eight
  bytes of SHA-256(candidate-id + colon + split).
- Candidate id: pcf_markov_baker_v1.
- Split: development.
- Incorrect v1 transcription: 18394334463172922998.
- Mechanically derived v2 value: 9296786003925294372.
- v1 source-lock SHA-256:
  35cd1709ae3d5c1149830730440cb09d2eecd5f00c65d980bf07d82fc5c70f18.

The validation and test seed values already matched the same rule and were not
changed. No exact sanity run, candidate development run, validation run, or
sealed test run had occurred when this correction was made. No prediction,
threshold, control, map, clock, or stopping rule changed.
