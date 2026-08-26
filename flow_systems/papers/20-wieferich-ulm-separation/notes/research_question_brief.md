# Paper 20 research-question brief

Date: **2026-08-24**
Status: **PHASE-2 RESOLVED — TECHNICAL COROLLARY / MERGE INTO PAPER 15**

## Primary question

For distinct rational primes `p` and `q`, under what explicit arithmetic
conditions can one prove the existence of a prime coordinate `r` with
`kappa_r(p) != kappa_r(q)`? The first target is a separation theorem for a
natural infinite class of prime pairs, or a structural theorem describing a
genuine finite collision pattern—not an unproved assertion that the full map
`p -> kappa(p)` is injective.

## Subquestions

1. Rewrite equality of one coordinate as explicit congruence,
   multiplicative-order, and Wieferich-depth conditions.
2. Identify natural pair classes where reciprocity or a Kummer/Chebotarev
   argument can force a separating coordinate.
3. Determine which local coordinates are provably irrelevant or forced equal.
4. Search bounded ranges only to find counterexamples, candidate lemmas, and
   minimal witnesses; never infer an infinite theorem from the search.
5. If separation fails, classify the strongest rigorous collision obstruction
   that still yields a standalone arithmetic result.

## FINER screen

| Criterion | Score / 5 | Reason |
|---|---:|---|
| Feasible | 2 | global injectivity is difficult and no separating mechanism is yet frozen |
| Interesting | 5 | it asks whether Paper 15's complete invariant recovers the prime |
| Novel | 5 | a nontrivial infinite-class separation or collision theorem would be a real new increment |
| Ethical | 5 | pure mathematics; computation/proof boundaries are explicit |
| Relevant | 5 | it is the sharpest unresolved arithmetic question left by Paper 15 |

Mean score: **4.4/5**, with feasibility as the binding risk.

## Owner and nonclaims

- The owner is the bare compact group invariant from Paper 15.
- The Paper-15 equivalence `B_p ~= B_q iff kappa(p)=kappa(q)` is imported and
  not re-proved as the new theorem.
- No marked support, packet topology, measure, flow, trace, operator,
  determinant, Route credit, or universal prime-recovery claim is available.
- A finite verified range is evidence, not a theorem of injectivity.

## Decisions

- **Promote:** a proof on a natural infinite class or a structural collision
  theorem with exact hypotheses.
- **Narrow:** a strong theorem for a sharply defined subfamily may replace the
  global question.
- **Stop:** only finite tables, random heuristics, or restatements of Paper 15
  remain.

## Phase-2 resolution

The [arithmetic/source screen](phase2_arithmetic_source_screen.md) replaces
the global separation question by an exact fixed-finite-coordinate density
corollary.  Keller--Richstein supplies the odd local count, while CRT and
fixed-modulus PNT-AP give the product distribution.  This is retained for
Paper 15; no standalone Paper-20 manuscript is authorized, and the closest
2023 paper still requires full-text comparison before any novelty wording.
