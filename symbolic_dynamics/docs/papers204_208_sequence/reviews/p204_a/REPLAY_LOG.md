# Review A actual execution and raw-byte receipt

2026-09-05 UTC. Interpreter:

```text
Python 3.12.3 | packaged by Anaconda, Inc. | (main, Apr 19 2024, 16:50:38) [GCC 11.2.0]
```

Working directory for the pair:
`/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p204_a/`.
Both physical child processes executed `python -B verify.py` with the same
fixed source and no arguments, external input files, network, randomness,
third-party package or imported project implementation. `-B` prevents bytecode
artifacts. Integer arithmetic and iteration orders are deterministic.

| Actual execution | Child exit | Complete stdout artifact | Result |
|---|---:|---|---|
| Pair run 1: `python -B verify.py` | 0 | `replays/run1.stdout` | 1,755,236 successful assertions |
| Pair run 2: `python -B verify.py` | 0 | `replays/run2.stdout` | 1,755,236 successful assertions |

The complete returned stdout bytes were retained in the two files, and
run 1 supplies `CANONICAL.json`. No abbreviated table was substituted for
stdout. The actual pair ran in separate Python processes (execution chunks
`b205a1` and `67fe26`); wall times were approximately 5.84 and 5.78 seconds.
An earlier development execution also exited zero, but is not used instead
of either member of this pair.

The following physical comparisons were executed after retaining the files:

```sh
cmp replays/run1.stdout CANONICAL.json
cmp replays/run2.stdout CANONICAL.json
cmp replays/run1.stdout replays/run2.stdout
```

All returned exit 0 and empty stdout. These are raw `cmp` byte comparisons,
not parsed-JSON or whitespace-normalized comparisons. A further fresh direct
stdout check was executed independently of materializing the pair:

```sh
cmp CANONICAL.json <(python -B verify.py)
```

It returned exit 0 with empty stdout (execution chunk `50635b`). This is
additional evidence that the canonical retains the actual interpreter
stdout bytes; it is not a claim that the earlier files alone ran a program.

## Complete dependency/input pins

- `verify.py`: `a6ea7483dc80e6c3db6bb09343c8301d4c87a4bfc69c47d95110a5ba0014fa39`.
- `CANONICAL.json`, run 1 and run 2 each:
  `f09ce8357277001f3df6e0df116e81204dc19e59111f656fba06d81d420738e6`.
- `INPUT_PINS.sha256`:
  `e3ffa207e9859050d4521182fc52849dc4f9fde0644c276851657c90467a604e`.

The checker has no runtime file dependency besides its own source and the
listed Python standard library. Fixed ranges and times are in that pinned
source. The full 23-file freeze input inventory is workspace-root-relative.
From `/root/autodl-tmp/symbolic_dynamics`, the command

```sh
sha256sum -c docs/papers204_208_sequence/reviews/p204_a/INPUT_PINS.sha256
```

returned exit 0 with all 23 entries OK after review. Supporting contracts,
the actual build helper and both internal collision manuscripts are pinned
separately in `SUPPORTING_INPUTS.sha256`; those are reviewed context, not
imports into this verifier. Downloaded primary-source PDFs are covered by
the package manifest and their use/read limits are recorded separately.

## Evidence interpretation

The output's `mathematical_checks` field is PASS, while its paper value
verdict is KILL_VALUE. The 1,785 exact static-adapter cells and the all-size
double count in `SOURCE_AND_PROOF.md` establish the reason for the adverse
review; more passing small boxes cannot repair that contribution failure.
The field is not a fake accepted review or a substitute for the written
deductive proof. All complete per-tag counts and graph reports are in the
canonical; no undocumented assertion total is used.

This is Review A's actual pair, not reuse of the author's or candidate's
execution. A future replay must retain the full dependency key and its
own truthful receipt. No Round1, Round2, Review B or final-paper completion
is claimed.
