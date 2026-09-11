# CS gate execution receipt

Date: 2026-09-05 UTC. Working directory for the commands below:
`/root/autodl-tmp/symbolic_dynamics`. Runtime: Python 3.12.3; standard
library only, no environment variables, randomness or author imports.

## First actual execution

```sh
python docs/papers204_208_sequence/scouting/algebra/CS_GATE/verify_gate.py
```

Exit status: **0**. Complete, untruncated stdout was captured and saved
as `CANONICAL.json`, including its terminal newline. The result records
1,250,591 successful checks: 5,143 for q=2 and 1,245,448 for q=4.
It includes the full field representation, parameter boxes, per-kind
assertion counts, complete first/later fibre spectra, all cycle/depth
censuses, and the bounded times actually checked. No author output was
consulted or copied into this result.

## Second fresh execution and raw-byte replay

```sh
bash -o pipefail -c 'python docs/papers204_208_sequence/scouting/algebra/CS_GATE/verify_gate.py | cmp - docs/papers204_208_sequence/scouting/algebra/CS_GATE/CANONICAL.json'
```

Exit status: **0**. Complete stdout: empty. Pipeline failure propagation
was enabled. `cmp` compared raw bytes, not parsed JSON or normalized
text, so the second execution reproduced the entire canonical file
including its terminal newline. This was a fresh computation, not a
comparison of two archived copies.

## Input integrity

```sh
sha256sum -c docs/papers204_208_sequence/scouting/algebra/CS_GATE/INPUTS.sha256
```

Exit status: **0**. Complete stdout:

```text
docs/papers204_208_sequence/scouting/algebra/PROOF_NOTES.md: OK
docs/papers204_208_sequence/scouting/algebra/pilot.py: OK
docs/papers204_208_sequence/scouting/algebra/SOURCE_AND_COLLISION_NOTES.md: OK
papers/175-diagonal-feedback-commutator/main.tex: OK
papers/125-quadratic-state-shear/main.tex: OK
docs/papers162_166_sequence/scouting/replacement_nonlinear_algebra/SCOUT.md: OK
docs/papers197_201_sequence/scouting/algebra_lane/COLLISION_MEMO.md: OK
```

`INPUTS.sha256` is workspace-root-relative. `SHA256SUMS` is local to
this gate directory and pins all six gate artifacts except itself.
Neither hash list claims a new computation or external review.
