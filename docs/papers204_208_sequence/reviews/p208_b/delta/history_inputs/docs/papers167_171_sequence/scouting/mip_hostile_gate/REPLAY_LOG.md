# MIP hostile-gate replay log

**Date:** 2026-09-03 UTC  
**Runtime:** CPython 3, standard library only  
**External status:** `HOLD_EXTERNAL`

## Frozen artifacts

```text
acb630523348a26f90a37aac45d9e17e33db13addfe0fc7aab1c71e9f4ab56e0  verify_mip_gate.py
d566ede8a559273ec25757c7dcf7dd6f8bbd7ef15cc855f2a38a974a2d4f5b8f  CANONICAL.json
```

The final verifier reports **12,603,676 exact assertions** and decision
`GREEN_OWNER_THIN / HOLD_EXTERNAL`.

## Independent final replays

Both runs started a new Python process and disabled bytecode output:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_mip_gate.py > /tmp/mip_gate_final_replay1.json
PYTHONDONTWRITEBYTECODE=1 python3 verify_mip_gate.py > /tmp/mip_gate_final_replay2.json
```

Their complete stdout digests were byte-identical:

```text
d566ede8a559273ec25757c7dcf7dd6f8bbd7ef15cc855f2a38a974a2d4f5b8f  /tmp/mip_gate_final_replay1.json
d566ede8a559273ec25757c7dcf7dd6f8bbd7ef15cc855f2a38a974a2d4f5b8f  /tmp/mip_gate_final_replay2.json
```

Both comparisons against the frozen transcript returned success:

```text
cmp -s CANONICAL.json /tmp/mip_gate_final_replay1.json  # exit 0
cmp -s CANONICAL.json /tmp/mip_gate_final_replay2.json  # exit 0
```

No `__pycache__` directory was created in the gate tree.

## Coverage represented in the transcript

- every one of the `873,612` carrier states for `1<=n<=7`;
- every target in `[n]^[n]` for `1<=n<=7`, comparing the closed fibre
  formula with literal preimage counts;
- every path order through nine labels, including the unique sharp
  decreasing path at each size;
- every canonical directed cycle through nine labels, with literal inversion
  and dynamical period checks;
- component recurrence and the closed recurrent EGF through order 14;
- pointwise fixed-iterate checks for powers one through six on every state
  through seven labels;
- kernel-transversal identity `f M(f) f=f`, KRR idempotence and exact kernel
  preservation;
- target/kernel-partition uniqueness through six labels and the Bell
  partition injection through seven labels; and
- the complete state-edge/tail/period/fibre tables at `n=1,2,3`.

The assertion total counts executed equality or predicate checks.  It is
falsification evidence, not an all-parameter proof or an ownership result.
