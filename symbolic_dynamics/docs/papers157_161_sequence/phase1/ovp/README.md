# OVP focused package

Candidate: deterministic simultaneous deletion of all current odd-degree
vertices from a labelled graph on a subset of `[n]`.

Decision: **PASS_FOCUSED / UNNUMBERED / HOLD_EXTERNAL**.

The theorem-level progress is a complete strict inverse transfer whose powers
give every-time, every-target fibres, exact image layers, and the temporal
CDF, together with the sharp `floor(n/2)` clock.  The owner and internal
firewalls are recorded separately.

Cold replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_ovp_focused.py > /tmp/ovp.out
cmp -s CANONICAL.txt /tmp/ovp.out
```

Expected result: 1,350,807 exact assertions and `STATUS=PASS`.
