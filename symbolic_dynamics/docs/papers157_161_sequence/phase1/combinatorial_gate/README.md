# Focused combinatorial collision gate

**Status:** complete negative gate  
**External state:** `HOLD_EXTERNAL`

This directory records a deliberately strict Stage-1 gate.  No candidate is
allocated a paper number and no formal paper was drafted.

## Decision

- `LCP`: exact theorem package passes, but the all-iterate coordinate proof
  and inverse tower mechanically transfer from P148 (with P114/P126 support).
  **KILL.**
- `PAE`: exact threshold and weighted-fibre package passes, but it is a
  selected-subword/extraction system whose compatibility, section, and
  inverse-tower proof transfers from P156, with P149/P155 support.  It is also
  barred by the permanent selector/extraction exclusion.  **KILL.**
- `TLS`: strongest replacement; its image, rotation core, and every-target
  fibre theorem all pass.  After stripping a forced arc and rotating, however,
  its `r+1` primitive-component fibre is exactly P144's theorem, while P130
  owns the matching retraction/fibre silhouette.  **KILL.**
- Twelve replacement systems were tested.  Every one was killed at Stage 1;
  there are **zero paper-sized survivors** in this branch.

## Files

- `COLLISION_GATE.md`: five-layer LCP/PAE collision matrices and verdicts.
- `THEOREM_CONTRACTS_AND_PROOFS.md`: exact LCP/PAE contracts and proofs.
- `DIRECT_OWNER_CHAINS.md`: internal and external owner chains.
- `verify_collision_gate.py` / `COLLISION_CANONICAL.txt`: independent exact
  falsifier and frozen output.
- `REPLACEMENT_SCOUT.md`: twelve-system replacement ledger.
- `TLS_FOCUSED_GATE.md`: exact theorem and fatal P130/P144 transfer for the
  strongest replacement.
- `OWNER_SEARCH_LOG.md`: bounded direct-owner search with support boundaries.
- `verify_replacement_scout.py` / `REPLACEMENT_CANONICAL.txt`: deterministic
  replacement verifier and frozen output.

The canonical outputs must be reproduced with `python -B`; no `__pycache__`
directory is part of the package.

