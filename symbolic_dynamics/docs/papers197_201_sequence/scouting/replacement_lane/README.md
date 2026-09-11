# Replacement lane: LZK and aggressive controls

This directory is the bounded replacement scout requested after GBE and SCT
were killed.  It contains no paper allocation and no novelty claim.

## Outcome

- **Theorem spike:** LZK, least-zero Kempe dynamics on proper colourings of
  labelled `K_{r,s}` (`OWNER_AMBER / HOLD_EXTERNAL`).
- **Reserve only:** LFAS, least alternating-rectangle switch.  Its current
  selector bound is not sharp enough for promotion.
- **Binding exclusion:** LSPO is an exact internal-history/P145 revival and
  is not counted.
- **Independent second signal:** FOSP is owned by the separately delegated
  Stirling-permutation replacement package, not duplicated here.

## Files

- [`LZK_THEOREM_CONTRACT.md`](LZK_THEOREM_CONTRACT.md): full functional graph,
  exact depth/recurrent census, all-time target fibres, extrema, and boundary
  cases.
- [`LFAS_RESERVE_CONTRACT.md`](LFAS_RESERVE_CONTRACT.md): rigorous reserve
  ceiling and missing theorem.
- [`BREADTH_AND_KILL_LEDGER.md`](BREADTH_AND_KILL_LEDGER.md): nine new literal
  maps and exact dispositions.
- [`COLLISION_AND_OWNER_MEMO.md`](COLLISION_AND_OWNER_MEMO.md): P1--P196
  subtraction and external owner hold.
- [`LSPO_HOSTILE_DISPOSITION.md`](LSPO_HOSTILE_DISPOSITION.md): exact-history
  kill.
- [`verify_replacement_lane.py`](verify_replacement_lane.py): dependency-free
  exact verifier.
- `CANONICAL.txt`: frozen deterministic transcript from two byte-identical
  fresh-process runs.
- `SHA256SUMS`: package-relative hashes for every non-manifest file.

Run from the workspace root:

```bash
python3 docs/papers197_201_sequence/scouting/replacement_lane/verify_replacement_lane.py
```
