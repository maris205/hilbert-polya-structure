# P155 author-side self-QA

**Date:** 2026-09-02 UTC.  **Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Contract audit

- The literal map agrees with the freeze contract.
- The image theorem is exactly `n>=2m-rlmin(sigma)`.
- The section construction covers the minimum rank and every larger rank.
- The fibre formula retains the ordered-support condition and factorial
  weights.
- Equal rank is correctly reduced to singleton cycles.
- The power-of-two clock is excluded from the abstract, theorem, conclusions,
  and claim ledger.

## Proof-interface attacks

1. **Could a non-RTL-minimum block be singleton?** No: every later block has
   larger minimum and therefore larger maximum.
2. **Can all RTL minima be synchronized simultaneously?** Yes: when such an
   opener is next, all smaller closer values belong to earlier openers and are
   exhausted by closer priority.
3. **Can the greedy scheduler stall?** No: if the next closer is unavailable,
   either the designated simultaneous move or the next opener is available;
   after all openers, every closer is available.
4. **Does enlargement change endpoint orders?** Adjacent splitting preserves
   both orders; interior insertion changes neither endpoint.
5. **Are fibre classes disjoint and exhaustive?** Yes: cycle supports are
   unique and a cycle order on every block reconstructs exactly one source.
6. **Does minimum rank force all allowed singletons?** Yes: equality in the
   lower bound uses all `rlmin(sigma)` singleton slots and size two elsewhere.

## Source and claim audit

All four bibliography entries are primary sources/official records and are
cited.  Endpoint sets, opener/closer configurations, ordered cycles, cycle
maxima, cyclic-order weights, and Stirling distributions receive zero credit.
The exact-map non-hit is described only as bounded.

## Computational audit

`verify_p155.py` uses standard-library exact arithmetic, no randomness, and
no runtime network.  Fresh stdout is required to match
`verification_output.txt` byte for byte.  The replay has 16,473,121
assertions and explicitly prints `power_of_two_clock=NOT_CLAIMED`.

## Artifact boundary

The manuscript is anonymous and contains Limitations, Data Availability,
Ethics, Author Contributions, Conflict of Interest, and Funding declarations.
Hostile Review A is preserved separately; its two Minor findings are closed
in `IMPROVEMENT_LOG.md`. Independent Hostile Review B returned
`ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor` and requested no
manuscript change. Round 2 is therefore a byte-identical acceptance freeze of
the Round-1 manuscript. This self-QA remains author-side and does not
authorize external release.
