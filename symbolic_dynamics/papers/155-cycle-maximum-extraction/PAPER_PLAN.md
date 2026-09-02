# P155 paper plan

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Central question

For the literal map

```text
permutation -> cycle supports ordered by minima
            -> standardized word of support maxima,
```

resolve which targets occur at each source rank and count every target fibre.
Forward dynamics is included only to classify recurrence; no absorption clock
is in the contract.

## Claim architecture

1. **Literal carrier and subtraction.** Define the map on
   `disjoint_union S_n`.  Subtract ordered-cycle conventions, block
   minima/maxima, opener/closer configurations, cycle-maxima statistics, and
   fixed-support cyclic-order counts.
2. **Sharp image theorem.** A singleton cycle support can occur only at a
   right-to-left-minimum target position.  This gives
   `n >= 2m-rlmin(sigma)`.  A greedy `O/K/S` endpoint schedule makes exactly
   those positions singleton and attains equality.
3. **All-rank section.** Split simultaneous events and then insert interior
   coordinates without changing either endpoint order.
4. **Every-target fibres.** Sum over ordered set partitions with prescribed
   standardized maxima; on each support of size `b`, count `(b-1)!` cycles.
5. **Dynamics.** The output rank is the number of cycles.  Equal rank forces
   all singleton cycles, hence the identity; every other step drops rank.
6. **Boundary and controls.** State that the power clock has no all-parameter
   proof, keep its finite profile only in Limitations, and distinguish proof
   from exact falsification pressure.

## Proof dependencies

```text
singleton necessity -> lower image threshold
RTL-min greedy schedule -> minimum-rank support section
event splitting/interior insertion -> every larger rank
unique support partition + independent cyclic orders -> fibre formula
rank = cycle count -> recurrent classification
```

The fibre proof does not rely on the scheduler, and the scheduler does not
rely on enumeration.

## Page allocation

- Map, source subtraction, and theorem: about 1 page.
- Endpoint lower bound and constructive schedule: about 1.5 pages.
- Image census, fibres, and recurrent classification: about 1 page.
- Exact control, limitations, declarations, and references: about 0.5–1 page.

Target: a narrow 4–6 page anonymous note.

## Prohibited expansion

- no sharp maximum absorption clock;
- no pointwise time formula;
- no minimum-rank theorem for iterated preimages;
- no novelty, priority, or direct-owner inference from a bounded non-hit;
- no attribution of static cycle endpoints or cycle-maxima concepts to this
  paper.

## Internal acceptance

Review A's two Minor findings were repaired in Round 1. Independent Review B
returned `ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor` and requested no
manuscript change. The Round-2 manuscript therefore remains byte-identical to
the accepted Round-1 text under `HOLD_EXTERNAL`.
