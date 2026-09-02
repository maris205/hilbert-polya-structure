# P156 exact-control results

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

Both hostile reviews are complete with zero unresolved findings.  Review B's
0 Critical / 0 Major / 1 Minor result concerned only a stale author-ledger
font-row count; it did not change this verifier, its frozen transcript, any
mathematical claim, or the PDF.

## Frozen replay

```text
literal_states_through_rank_9=409113
max_tail_ranks_1_to_9=[0, 1, 2, 2, 3, 3, 3, 4, 4]
image_counts_ranks_1_to_9=[1, 2, 4, 8, 18, 44, 120, 356, 1152]
image_target_rank_cells=99451
constructive_section_cells=1704
every_target_fibre_cells=6985
fibre_n_lt_m_boundary_cells=316646
fibre_n_eq_m_boundary_cells=46233
bell_identity_basin_checks_zero_credit=7
tower_targets_through_rank_8=46225
tower_levels_per_target=6
boxes=40
assertions=3689489
status=PASS
```

The full canonical stdout is `verification_output.txt`.

## Independent interfaces

1. **Literal graph.** Every permutation through rank nine is mapped directly;
   closure, strict rank drop, fixed points, tails, fibres, and images are
   recorded.
2. **Images and sections.** Every target through rank eight is tested against
   the `m+d(sigma)` threshold in every available source rank, and every
   admissible high-shift/low-tail section is remapped literally.
3. **Fibres.** Subset enumeration and deficient-board products are compared
   with literal predecessor dictionaries for all targets through source rank
   seven. A separate lane checks every `n<m` and `n=m` boundary cell through
   target rank eight.
4. **Owned aggregate.** Identity fibres are summed and checked against Bell
   numbers, explicitly as zero-credit source consistency.
5. **Inverse tower.** Every nonidentity target through rank eight is lifted
   six times; each forward edge, rank/drop update, Fibonacci formula, and tail
   shift is checked.
6. **Exclusion witness.** The rank-11 source
   `(11,10,9,4,1,2,3,8,5,6,7)` reproduces the false old pointwise clock.

## Replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p156.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p156.py > /tmp/p156_replay.txt
cmp -s /tmp/p156_replay.txt verification_output.txt
```

No randomness, floating point, external CAS, runtime network access, or
third-party Python dependency is used.  The replay does not prove any
all-rank theorem or support an ownership/novelty conclusion.
