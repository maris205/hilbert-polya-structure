# P155 exact-control results

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Frozen replay

```text
literal_states_through_rank_10=4037913
max_tail_ranks_1_to_10=[0, 1, 2, 2, 3, 3, 3, 3, 4, 4]
image_counts_ranks_1_to_10=[1, 2, 4, 8, 17, 39, 96, 253, 706, 2074]
image_target_rank_cells=145684
constructive_section_cells=3161
endpoint_dp_targets=46233
every_target_fibre_cells=53218
ordered_support_terms=5295
boxes=26
assertions=16473121
status=PASS
```

The complete canonical stdout is `verification_output.txt`.

## Independent interfaces

1. **Literal functional graph.** Disjoint cycles are computed directly from
   every permutation through rank ten.  The verifier checks closure, output
   rank, strict drop, fixed states, tail censuses, and image sets.
2. **Endpoint optimum.** A two-chain dynamic program independently minimizes
   opener/closer/simultaneous schedules.  Its answer is compared with
   `2m-rlmin(sigma)` for every target through rank eight.
3. **Constructive sections.** A separate greedy scheduler produces supports,
   then a canonical cycle is placed on each support and the literal map is
   rerun.
4. **Fibres.** Restricted-growth words generate ordered set partitions and
   factorial weights.  Their full target dictionary is compared with literal
   predecessor counts through source rank eight.

## Replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p155.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p155.py > /tmp/p155_replay.txt
cmp -s /tmp/p155_replay.txt verification_output.txt
```

No randomness, floating point, external CAS, runtime network access, or
third-party Python dependency is used.  The test does not prove the theorem,
ownership, novelty, or the excluded clock.

Hostile Review B cold-replayed all 16,473,121 assertions, reproduced the
frozen transcript and four-page PDF, and returned
`ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor`. No control code,
transcript, or manuscript change was made for Round 2.
