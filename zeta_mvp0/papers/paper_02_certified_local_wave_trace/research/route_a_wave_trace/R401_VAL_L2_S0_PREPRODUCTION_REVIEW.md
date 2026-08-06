# R401-VAL-L2-S0 preproduction review

Review date: 2026-08-06 (UTC)  
Disposition: **ACCEPT FOR FROZEN PRODUCTION**  
Review mode: independent secondary-agent release-blocking audit; no external
review-model score was available or invented.

## Frozen state audited

| Object | SHA-256 |
|---|---|
| Production freeze | `3ee95a5a93b45ac200c165a4c37cdad6e54e7dede4b4d3001899f2a8006cad55` |
| Protocol | `ced4df08866a6ed3a9fa140bd6ab7418fcc609881f5835172b662fd04d9b9767` |
| C++ evaluator | `8eabb022f92c712805c401fb07e2b741e4af4e927bc43702c95125b2a4338bd2` |
| Producer | `2f2f4aed58405ad8dcaef929623f07e543013dbb627365623da1d3cf529dbbcf` |
| Independent checker | `1227e5a5108fae23202ce26d462e4fef446117b594df5e4ec9f58c061a9defa8` |

## Accepted gates

- Exact binding of slab ID, file path, epsilon interval, precision, tree node,
  requested box, and raw CAPD transcript.
- Exactly one tree for every pair in
  `{128,256} x {S000,S025,S050}`, with no duplicate or missing pair.
- Independent reconstruction of the exact eight-shell complement, split
  midpoint, maximum-normalized-width coordinate, parent--child union,
  reachability, and per-class terminal counts.
- A complete tree requires every stored node to have been evaluated and
  `evaluated_count == len(nodes) <= 20000`; the depth limit is 40.
- Both precisions cover the same exact domains and must reach the same
  domain-level exclusion verdict, while their adaptive tree shapes may
  differ.
- The authoritative L1 chain, planned-box containment in the outward
  validated `X`, and strict Krawczyk-image containment replay successfully;
  the minimum selected strict margin is greater than `9.3725e-6`.
- The checker reconstructs each archived Newton expression `m-F/D` with exact
  rational arithmetic, verifies the guarded enclosure and strict empty gap,
  and verifies every displayed return-separation margin.
- Return exclusion is used only as a necessary-residual exclusion.  It does
  not claim a complete return, global uniqueness, or a Hilbert--Pólya result.
- The producer may emit only `PASS_S0_PRODUCER` with null milestone/final
  status.  Only a zero-failure checker and postcheck may assign
  `PASS_IMPLEMENTATION_SMOKE`; `final_status` remains null.
- The C++ evaluator passed a syntax/build audit against the pinned
  CAPD/MPFR configuration and commit.

## Boundary

At review time no production result existed.  This acceptance licenses only
execution of the frozen six-tree implementation smoke.  It does not predict
that the run will pass and does not enlarge a later pass into an all-slab
local complement, phase cover, global cover, determinant-identity cross-check,
quantitative trace domain, prime trace, zeta-zero correspondence, or RH claim.
