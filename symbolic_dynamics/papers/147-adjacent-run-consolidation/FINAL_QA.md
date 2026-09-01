# Final internal QA — P147

**Verdict:** **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**  
**Surviving severity:** 0 Critical / 0 Major / 0 Minor

## Review closure

- Hostile Review A: REVISE, 0 Critical / 1 Major / 3 Minor.
- The formal ancestry selector, `Comp(n)` target typing, explicit all-size
  witness orbits, and closest primary-source subtraction were implemented.
- Independent Hostile Review B: ACCEPT, 0 / 0 / 0; all A1--A4 items CLOSED.

## Mathematical and ownership QA

- The literal update is a weight-preserving self-map on each `Comp(n)` and
  strictly shortens every nonfixed state.
- The state-indexed ancestry chain proves the pointwise logarithmic upper
  bound, including depth zero.
- Both witness branches and the `n=1,2,3` bases establish sharpness for every
  total.
- The fibre theorem is typed within the exact-total layer and its
  expansion/contraction constructions are mutual inverses.
- Carlitz enumeration, static run statistics, run-length encoding, random
  composition evolution, static adjacent restrictions, and the literal rule
  alone receive zero contribution credit.
- The residual is only the simultaneous map, sharp all-size clock, and
  complete target-resolved length-refined divisor-path inverse.

## Exact-control QA

- `PYTHONDONTWRITEBYTECODE=1 python3 verify_p147.py` matched the frozen
  transcript byte for byte.
- All 2,690,869 deterministic integer assertions passed over every positive
  composition of totals `1..18` and every target in each exact-total layer.
- Review B's separate witness routine passed every `1 <= n <= 100000`.
- Enumeration is recorded as falsification pressure, never as proof or source
  clearance.

## Build and visual QA

- Current `main.pdf` and `main_round1.pdf`: byte-identical, 4 A4 pages,
  338,052 bytes, SHA-256
  `1d9c5ceb72891e1c509ebeb8adfdb23d110958f129ea7ae32d3c9d427253ce20`.
- Review B's isolated deterministic build reproduced that PDF byte for byte.
- The settled log has no unresolved citation/reference, rerun request, bad
  box, or multiply defined label; reported fonts are embedded.
- Every current page was rasterized and inspected without clipping,
  collision, blank page, corrupt glyph, unresolved marker, or anonymity leak.

## Freeze boundary

`main_round2.pdf` is frozen read-only and byte-identical to the accepted
current PDF.  The final paper-local `SHA256SUMS` was regenerated after closure
and passes in full.  Nothing here authorizes public posting, circulation,
submission, author contact, or any other external action; status remains
`HOLD_EXTERNAL`.
