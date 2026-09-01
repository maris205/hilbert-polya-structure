# Improvement log — P142

## Round 1

Hostile review A found no theorem defect and requested one clarity repair.
The fibre proof now states explicitly that the two branch labels overlap at
3a=e because their values agree, with set union handling the coincident
source.  The repaired PDF is frozen as `main_round1.pdf`.

## Round 2

Independent hostile review B returned ACCEPT with zero critical and zero
major findings.  Its two nonblocking minors were closed:

1. The recurrence proof now excludes outside recurrent states directly by
   eventual entrance into, and permanent residence in, the invariant set.
2. README and BUILD now distinguish immutable round 0, repaired round 1, and
   the current round-2 artifact.

The canonical 319,074-assertion replay and isolated build remain exact.  No
theorem was broadened; external status remains `HOLD_EXTERNAL`.
