# P182--P186 algebra-lane breadth scout (frozen)

This directory freezes a falsification-first algebra/linear-carrier scout.  It
does **not** claim novelty or grant release clearance.  The coordinator's
frozen decision is A01 `SELECTED_P182` and A02 `RESERVE`; these are the only
two ranked survivors:

1. **A01 / CLC -- cyclic lattice comparator (`SELECTED_P182`).**  On triples of subspaces,
   rotate one register and replace the other two by their meet and join.  The
   universal identity `T^4=T^2` expands, on subspace lattices, into an exact
   two-axis `(q,d)` functional-graph census and an every-target fibre formula
   governed by ordered complementary pairs.
2. **A02 / LDS -- Lie-derived subspaces of a central thickening of
   `sl_2`.**  The map `U -> [U,U]` on all subspaces of
   `F_q^z + sl_2(F_q)` has `D^3=D^2`, exactly two recurrent states, and a
   four-case fibre atlas for every odd prime power `q` and every `z >= 0`.
   It remains the algebra-lane reserve rather than a second paper selection.

The next candidate, A03, is deliberately killed despite an exact theorem: its
square-zero transpose-commutator collapse is too transferable from P175.  All
other candidates are also killed in the breadth ledger.

## Frozen artefacts

- `SCOUT_AND_KILL_LEDGER.md`: fifteen literal systems, each with map/kernel,
  small box, proposed axes, and keep/kill decision.
- `THEOREM_SPIKES.md`: closed theorem packages for A01 and A02, with proofs.
- `COLLISION_FIREWALL.md`: explicit NFIT, P115/P178, and P172--P181 comparison.
- `OWNER_SEARCH_LOG.md`: bounded primary-source adjacency checks for only the
  two finalists; non-hits are not called novelty.
- `HISTORY_AUDIT.md`: scope and digests of the title/collision audit.
- `verify_algebra_lane.py`: standard-library exact verifier.
- `CANONICAL.txt`: deterministic expected stdout.
- `SELF_CHECK.md`: two-process replay protocol and frozen pass counts.
- `MANIFEST.json` and `SHA256SUMS`: inventory and hashes.

## One-command verification

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers182_186_sequence/scouting/algebra_lane/verify_algebra_lane.py
```

The last line must be `RESULT=PASS`; the complete stdout must byte-match
`CANONICAL.txt`.  Enumeration is exact over the listed prime-field boxes.  The
proofs, not the enumeration, establish the stated prime-power families.
