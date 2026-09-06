# P206 A — actual independent execution receipt

2026-09-05 UTC. Cwd for every command:
`/root/autodl-tmp/symbolic_dynamics`. Interpreter: Python 3.12.3.
No random seed, network request, file input, local research import or
third-party Python package is used. No checker correction or failed
checker version occurred. The initial canonical producer and both
additional producers ran in genuinely fresh Python processes.

## New representation and complete comparison target

The [standalone checker](verify.py) contains complete literal forward
scanning, a separate nearest-greater depth calculation, functional-graph
walks with local cycle detection, a reverse whole-circle skyline transducer
for full source reconstruction, and a definition-level binary weak-template
DFS. Template counts are independently evaluated through the two prior
operator coefficient updates. Neither an author formula nor imported
canonical data supplies those reconstructed source sets. The manuscript's
formula is separately recomputed only as a claimed result being tested.

The full deterministic JSON includes every box, height census, target
maximum/equality census, all-template bounds, assertion count, and a digest
over complete source-set records. It is the whole stdout compared below.

## Actual commands and observed completion

```sh
python3 docs/papers204_208_sequence/reviews/p206_a/verify.py > docs/papers204_208_sequence/reviews/p206_a/CANONICAL.json 2> docs/papers204_208_sequence/reviews/p206_a/initial.stderr
```

Initial producer: actual exit **0**. The entire 6,439-byte stdout is
[CANONICAL.json](CANONICAL.json); `initial.stderr` is empty.

```sh
python3 docs/papers204_208_sequence/reviews/p206_a/verify.py > docs/papers204_208_sequence/reviews/p206_a/run1.stdout 2> docs/papers204_208_sequence/reviews/p206_a/run1.stderr && cmp docs/papers204_208_sequence/reviews/p206_a/CANONICAL.json docs/papers204_208_sequence/reviews/p206_a/run1.stdout > docs/papers204_208_sequence/reviews/p206_a/run1.cmp.stdout 2> docs/papers204_208_sequence/reviews/p206_a/run1.cmp.stderr
python3 docs/papers204_208_sequence/reviews/p206_a/verify.py > docs/papers204_208_sequence/reviews/p206_a/run2.stdout 2> docs/papers204_208_sequence/reviews/p206_a/run2.stderr && cmp docs/papers204_208_sequence/reviews/p206_a/CANONICAL.json docs/papers204_208_sequence/reviews/p206_a/run2.stdout > docs/papers204_208_sequence/reviews/p206_a/run2.cmp.stdout 2> docs/papers204_208_sequence/reviews/p206_a/run2.cmp.stderr
```

The two additional commands ran concurrently. Both success-chained shells
were actually observed completed with exit **0**, proving each producer
and its following raw-byte comparison exited zero. Both saved producer
outputs are complete; all six stderr/comparison files are empty. A digest
comparison was additionally made, not substituted for these raw `cmp`s.

| Execution | Producer exit | Full raw comparison | Assertions |
|---|---:|---:|---:|
| Initial canonical producer | 0 | Produces comparison target | 3,698,764 |
| Additional run 1 | 0 | 0 | 3,698,764 |
| Additional run 2 | 0 | 0 | 3,698,764 |

Pins:

- Checker: `45fd54e08d271b2befdf53cbe2a11b8dc29cb7f3dd3ac24b39bfd353c31fc673`.
- Canonical, run 1 and run 2 stdout:
  `6fee8997d694fd428b7b5d4594af57b72e44fbc1aa86bdbec4f702fc6b5dc8d9`.
- Complete record digest inside stdout:
  `8bec8ec6145a75f6a22821371f64583aeb44636915c95e281574d47f65e1394b`.

Bounds and interfaces: all 265,719 ternary states/targets for lengths
1–11; full source sets for every target in every box, not a sample;
797,157 maximum-three/two/one comparisons; all 8,191 binary $W/O$
templates across lengths 0–12; integer-product DP at every size 1–100.
Zero targets, empty intervals, loops and all labelled maximizers are
included. Finite checks support the mathematical audit and adapter;
they do not prove their all-length scope or certify global novelty.

## Input integrity

The workspace-root-relative [INPUT_PINS.sha256](INPUT_PINS.sha256) contains
all 23 physical freeze files, including its directory-relative index;
all pass `sha256sum -c`. The original freeze's own 22 entries also pass.
The six [supplementary pins](SUPPLEMENTARY_INPUTS.sha256) cover the actual
build helper and inspected historical manuscript inputs; all pass. The
reviewer did not alter any of these inputs. Remote web contexts were read
through their primary URLs and locators, not falsely described as locally
hashed snapshots. The new checker has no runtime dependence on any of
these documentary sources.
