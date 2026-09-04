# P1--P181 title and mechanism inventory

**Audit date:** 2026-09-03 UTC  
**Scope:** numbered directories under `papers/`, plus the current historical
collision seed  
**Lifecycle:** `HOLD_EXTERNAL`

The mechanical scan found **176 numbered directories representing 175
distinct paper numbers**.  The duplication is P96; P51--P56 are absent from
`papers/`.  The newline-terminated, version-sorted directory-name stream has
SHA-256

```text
1c7d3fed5c1452a69e67c7dd2a1845fe5124c2d61166aef739eedae4b2b0206b
```

The scan command was

```text
find papers -maxdepth 1 -mindepth 1 -type d -printf '%f\n' |
  awk '$0 ~ /^[0-9]+-/' | sort -V
```

The missing numbers are not treated as empty territory: the sequence records
retain their topics, and the full collision seeds remain authoritative.  A
directory-name nonmatch is never a mechanism noncollision.

## Mechanism-pressure slice used in this lane

The following occupied papers were inspected beyond their directory names.
They are the closest pressure points for the twelve scouts, not an exhaustive
restatement of all 181 projects.

| papers | occupied mechanism relevant here |
|---|---|
| P100 | least-valuation digit erasure and exact absorption by a digit statistic |
| P105, P122, P155, P181 | cycle/record/descent-selected permutation updates and target-local inverse analysis |
| P110, P169, P179 | partition joins, cyclic successor transfer, and singleton isolation |
| P113, P143, P160 | partition/tableau/hook/corner canonical reductions |
| P114, P159 | graph/forest vertex peeling and pruning clocks |
| P117, P132, P134, P138, P139, P164, P176 | run, prefix, border, palindrome, Lyndon, equality, and frequency feedback on words |
| P126, P147 | composition refinement and adjacent-run consolidation |
| P127, P137, P156, P167 | transpose, rank, weak-excedance, and inverse-position feedback |
| P163, P165, P171 | shadow/support shortening and Boolean Gram transforms |
| P178 | state-selected finite-difference image towers and fibres |

The literal PDD and RCS updates are absent from the inspected internal
definitions.  That only clears the internal literal-duplication check.  Their
proof engines are compared explicitly in `COLLISION_FIREWALL.md`, and external
adjacency is recorded in `OWNER_SEARCH_LOG.md`.

## Frozen seed inputs

At the audit point:

```text
b691d71d8af5fc12314405f2c908158a942c0c96709e70115dfae93d6d6f47cc  docs/papers182_186_sequence/HISTORICAL_COLLISION_SEED.md
bbcfd687ebf99c7b37b389c6dd8067f51db561399c7aa89d33cb819ad047b80e  docs/papers177_181_sequence/HISTORICAL_COLLISION_SEED.md
ed539e25bd4b6c6694fb49bc91d2617a558c8265de209a1b4b75663acb9ede76  docs/papers177_181_sequence/phase1/SYSTEM_COLLISION_FIREWALL.md
```

This inventory is reproducibility evidence, not novelty, priority, ownership,
freedom-to-operate, or release evidence.

