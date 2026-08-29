# P105 — Cycle-minimum pruning dynamics

Status: **FINAL QA PASS / INTERNAL FREEZE / EXTERNAL HOLD**.

For each `n >= 1`, this note studies a labelled self-map of `S_n`.  In every
nontrivial cycle, the least label is removed from that cyclic word, the
predecessor is reconnected to the successor, and the removed label becomes a
fixed point.  All cycles are processed simultaneously.  There is no deletion
from the ground set and no standardization.

The frozen theorem package is:

1. after `t` steps, the `t` least labels of each original cycle have become
   fixed, stopping when one label remains;
2. the absorption time is `longest_cycle(pi)-1`, with sharp maximum `n-1` and
   `(n-1)!` deepest states;
3. the identity is the only recurrent state, every iterate has one fixed
   point, and `zeta=(1-z)^(-1)`;
4. if `A[n,k]` counts permutations with cycles of length at most `k`, then
   the exact depth-`t` layer is `A[n,t+1]-A[n,t]`, with restricted-cycle EGF
   and an independent cycle-containing-1 recurrence; and
5. every one-step fiber has an exact threshold-matching formula, including a
   Garden-of-Eden criterion and the involution-number identity fiber.

Classical labelled-cycle enumeration and longest-cycle probability are
positively attributed and removed from the residual claim.  A bounded owner
search did not locate the same simultaneous map, but search absence is not a
novelty or priority certificate.

Run the exact deterministic control with:

```bash
python3 code/verify_cycle_minimum_pruning.py
```

Build with the four-stage command in [BUILD.md](BUILD.md).  Cross-hostile
ledgers A and B, the consolidated gate, final mechanical QA, and the verified
hash manifest are present.  Public release, submission, and specialist
contact remain **HOLD**.

The control's `literal_trajectory_steps` counter records repeated
trajectory-step evaluations across all starting states, not distinct edges
of the functional graph.
