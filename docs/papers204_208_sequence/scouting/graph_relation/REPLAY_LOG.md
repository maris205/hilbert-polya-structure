# Actual raw-byte replay receipt

Date: 2026-09-05 UTC. Scope: bounded scout controls only, not theorem or
ownership validation. Working directory:
`/root/autodl-tmp/symbolic_dynamics`.

One exploratory full execution returned code zero. It was followed by two
fresh sequential subprocess executions of the same unmodified program. The
comparison read raw stdout and stderr bytes, without normalization or JSON
reserialization. The actual wrapper asserted both return codes were zero,
both stderr values were empty, and the two raw stdout byte strings were equal.

Actual wrapper receipt:

```json
{"byte_comparison":"PASS","command":["/root/miniconda3/bin/python","-B","docs/papers204_208_sequence/scouting/graph_relation/pilot.py"],"exit_codes":[0,0],"python":"3.12.3","raw_stdout_bytes":9981,"raw_stdout_sha256":"bd75769c64bb40a24aea633b5a14dbcf540273e10bd6b8eb0cac86642d3b163d"}
```

Each subprocess printed `assertions=1981384` and
`status=PASS_BOUNDED_CONTROL_ONLY`. The count is 1,981,384 checks per run;
repeating an identical test does not create additional distinct test cases.
The saved CANONICAL.txt subsequently had its real filesystem SHA-256 checked
against the receipt and matched. The unmodified source hash was also checked:

```text
054c89321fe453c1393ecc96614ffc94b70326fe7eb93850317320fb6349d20d  pilot.py
bd75769c64bb40a24aea633b5a14dbcf540273e10bd6b8eb0cac86642d3b163d  CANONICAL.txt
```

Reproduction command for one bounded run:

```sh
python -B docs/papers204_208_sequence/scouting/graph_relation/pilot.py
```

To reproduce the stronger comparison, execute that command twice using
`subprocess.run(..., stdout=subprocess.PIPE, stderr=subprocess.PIPE)`, check
the two raw outputs and return codes directly, and compare stdout to
CANONICAL.txt in binary mode. No generated timestamp enters the program.

The controls test carrier closure, consistent orbit labels, recurrence
population, and fibre mass. They do not independently verify an all-parameter
theorem, prove a maximal-fibre conjecture, or establish external novelty.
