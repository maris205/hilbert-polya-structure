# Root's actual P205 A replay pair

2026-09-05 UTC. Both fresh complete producer processes and both raw-byte
comparisons exited zero (combined shell exit 0). Each execution passed
11,265,033 assertions. Complete outputs are run1.stdout and run2.stdout;
both stderr files are empty. The canonical SHA256, equal to each stdout,
is `742ab7299ac4e44f15f42f56393abce02c41271164d1ae33a3b1cc80f093a626`.
The unchanged independent script SHA256 is
`3a4cbce7210f93addc9a65bed2aef822b0cae3f859a9c93df66beb57f7bebeaa`.

The script pin is also recorded in the reviewed package's SHA256SUMS and
REPLAY_LOG.md. Root ran the literal standalone file, not an imported author
or candidate implementation. Python 3.12.3, standard library, -B, no random
or external input. Mathematical and source report originals were read.

Working directory: `/root/autodl-tmp/symbolic_dynamics`. Actual command
pattern for k=1 and then k=2, chained by &&:

```sh
python -B docs/papers204_208_sequence/reviews/p205_a/verify.py > docs/papers204_208_sequence/qa/root_replays/p205_a/runK.stdout 2> docs/papers204_208_sequence/qa/root_replays/p205_a/runK.stderr
cmp docs/papers204_208_sequence/reviews/p205_a/CANONICAL.json docs/papers204_208_sequence/qa/root_replays/p205_a/runK.stdout
```

K denotes the two literal file suffixes, not a shell environment variable.
After both comparisons succeeded, root checked all 23 INPUT_PINS, all six
SUPPLEMENTARY_INPUTS, and all 52 entries of the initial review manifest;
every entry passed and the combined process exited zero. That manifest
predates A delta acceptance, which remains a distinct obligation. The raw
canonical and review package retain the full finite boxes; no all-size
proof is inferred from the execution count.
