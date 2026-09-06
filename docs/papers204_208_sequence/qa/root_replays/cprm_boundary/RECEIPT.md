# CPRM elementary-boundary author checks

2026-09-06 UTC. **Author evidence / NO_PROMOTION**, not independent review.

The corrected CPRM-only pilot ran all original 30 boxes successfully and
its full stdout matched the 30 CPRM rows emitted before the combined first
program's CSGD carrier failure. The failed combined program, complete
partial stdout and traceback remain preserved under the intake's names.
No clipped or zero-guard CSGD rule was introduced.

The new standalone `verify_cprm_boundary.py` reads no files and imports
only the standard library. It actually produced the complete canonical,
then two additional executions were run from the workspace root:

```sh
python3 -B docs/papers204_208_sequence/scouting/word_local/verify_cprm_boundary.py > docs/papers204_208_sequence/qa/root_replays/cprm_boundary/run1.stdout 2> docs/papers204_208_sequence/qa/root_replays/cprm_boundary/run1.stderr
cmp docs/papers204_208_sequence/scouting/word_local/CPRM_BOUNDARY_CANONICAL.json docs/papers204_208_sequence/qa/root_replays/cprm_boundary/run1.stdout
python3 -B docs/papers204_208_sequence/scouting/word_local/verify_cprm_boundary.py > docs/papers204_208_sequence/qa/root_replays/cprm_boundary/run2.stdout 2> docs/papers204_208_sequence/qa/root_replays/cprm_boundary/run2.stderr
cmp docs/papers204_208_sequence/scouting/word_local/CPRM_BOUNDARY_CANONICAL.json docs/papers204_208_sequence/qa/root_replays/cprm_boundary/run2.stdout
cmp docs/papers204_208_sequence/qa/root_replays/cprm_boundary/run1.stdout docs/papers204_208_sequence/qa/root_replays/cprm_boundary/run2.stdout
```

The two producer and three raw comparator commands were joined by `&&`;
the observed complete command exited zero. Each producer performed
**1,234,850 assertions**, on the unchanged 30 boxes / 82,179 source states.
Every target fibre, quotient-code injection and maximum is checked there;
full independently reconstructed source sets are compared at $n=2,3,4$,
$m=1,2,3,4$. No larger full atlas is used. Both stderr streams are empty.
Each stdout is 14,122 bytes, the complete canonical bytes.

Scientific hashes checked after the pair (not claimed as an additional
pre-run hash snapshot):

- Proof: `7331f44b1fd0fd0a4134fe2f89b9ecf7d419555effa36d8a212477f061f3dd5a`.
- Standalone checker: `3f9cbaf179d0b1aca604a9579fc74c27a72a0240ca9e2b340a2aceb61fa0f5c2`.
- Complete canonical and both raw outputs: `9d4a9504e8aa0f29e84f0ca8acc68c54b1c30a3175a0bf2fe484c71c8d8e5dde`.

Python 3.12.3, `-B`, exact integer arithmetic; no random, external data,
network, author/scout runtime import, locale-dependent formatting or
hash-order-dependent output. These checks pressure the written elementary
proof, not establish its all-parameter quantifiers. Root's conservative
NO_PROMOTION disposition remains unchanged; no candidate gate is claimed.
