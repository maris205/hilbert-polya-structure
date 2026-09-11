# Repository-wide literal-history recheck

This pass used literal formulas, operator descriptions, and sufficient-
statistic synonyms across `papers/` and `docs/`, not just paper titles.

## Collisions found

1. **RC02 / cyclic gcd smoothing:** exact match to C2 in the P107–P111
   combinatorial scout.  That record already contains the window iterate,
   constant endpoints, fixed census, product basins, threshold-run pointwise
   depth, sharp `m-1` clock, and prime-blind conjugacy.  Status:
   `KILL_DIRECT_SCOUT_REPEAT`.
2. **RC05 / left stabilizer of a group subset:** exact match to A13 in the
   P172–P176 algebra scout.  That record explicitly kills the idempotent map
   and divisor-Möbius/necklace fibres as shallow stabilizer dynamics.  Status:
   `KILL_DIRECT_SCOUT_REPEAT`.
3. **RC04 / self-cardinality completion:** current-lane explicit conjugacy to
   RC03 under complement plus order reversal.  Status: `KILL_CONJUGATE`.
4. **RC14 / cardinality translation:** exact occupied mechanism P166.
   Status: `KILL_P166_LITERAL_ENGINE`.

## No internal literal hit in this pass

RC01 (cyclic divisor quotient / positive difference) and RC03
(self-cardinality truncation) produced no literal formula hit outside the new
lane.  This is only an internal collision result.  It has no force for
external novelty, ownership, priority, or circulation readiness.
