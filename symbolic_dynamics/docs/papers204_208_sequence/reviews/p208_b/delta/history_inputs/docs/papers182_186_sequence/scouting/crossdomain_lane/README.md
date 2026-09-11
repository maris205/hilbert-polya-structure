# P182--P186 Route-A cross-domain breadth scout

This directory is a sealed scouting lane.  It proposes literal finite dynamics,
checks the strongest early signals exactly, and makes no claim of novelty or
publication readiness.  Nothing here changes a paper or another scouting lane.

## Outcome

Sixteen mechanism-distinct systems were specified and triaged.  Three received
exhaustive standard-library pilots.  Two survive the internal collision and
theorem-spike filters:

1. **RICS**, random incoming-copy symmetrization of loopless directed graphs;
2. **CGT**, co-gcd translation on residues modulo a prime power.

The third pilot, suffix-set compression, was killed despite exact formulas: it
is a transparent power-automaton/de Bruijn reset construction and collides in
theme with P55.  All recommendations retain `HOLD_EXTERNAL`; a bounded search
non-hit is not evidence of novelty.

## Reproduction

Run from this directory:

```sh
python3 verify_crossdomain.py
python3 self_check.py
sha256sum -c SHA256SUMS
```

`verify_crossdomain.py` is deterministic, uses only the Python standard
library, and writes nothing.  `CANONICAL.txt` is its byte-exact expected stdout.
The self-check performs two fresh verifier executions and compares both with
the canonical transcript.

## File roles

- `TITLE_AND_COLLISION_INVENTORY.md`: P1--P181 title/collision intake.
- `SCOUT_AND_KILL_LEDGER.md`: sixteen exact rules, signals, axes, and verdicts.
- `COLLISION_FIREWALL.md`: literal and proof-obligation separations.
- `THEOREM_SPIKES.md`: formal conjecture packages for the two survivors and the
  documented post-pilot kill.
- `OWNER_SEARCH_LOG.md`: bounded primary-source checks and epistemic status.
- `verify_crossdomain.py`, `CANONICAL.txt`: executable exact evidence.
- `self_check.py`, `SELF_CHECK.md`: clean replay and integrity protocol.
- `SHA256SUMS`: directory-local integrity manifest, excluding itself.

