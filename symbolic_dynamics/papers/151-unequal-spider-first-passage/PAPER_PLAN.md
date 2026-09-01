# Paper plan — P151

**Status:** **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**

## One-sentence contribution

For simple random walk on a finite labelled spider with arbitrary unequal
integer arms, derive an explicit continuant factorization of the generic
leaf-marked first-passage law and use it to obtain a compact scalar variance,
sharp fixed-total mean extremizers, and the
exact endpoint-only versus endpoint-plus-mean geometry-identifiability
boundary.

## Claim ceiling

The P151 entry of
`docs/papers147_151_sequence/phase1/FINAL_THEOREM_CONTRACTS.md` is absolute.
The manuscript may narrow but may not broaden it.  In particular, endpoint
probabilities, the expected absorption time, equal-arm laws, general
tree-resolvent/time-place/PGF methods, spider spectral methods, and generic inverse
first-passage language are zero-credit background.

## Structure

1. Literal process, ownership boundary, notation, and main theorem.
2. Killed path transforms and centre-excursion renewal proof of the
   leaf-marked transform, parity, and first atom.
3. Excursion moments and compact variance formula.
4. Sharp fixed-`(r,L)` mean bounds and equality classes.
5. Coarse-data inverse theorem and its exact dilation boundary.
6. Exact-arithmetic audit, owner subtraction, limitations, and declarations.

## Claims--evidence map

| claim | proof support | executable support | ownership boundary |
|---|---|---|---|
| explicit arbitrary-profile continuant form `F_i(z)` | killed-path recurrence plus centre renewal | literal state DP versus rational-series expansion | generic time/place laws, tree-PGF algorithms, equal-arm distribution, and resolvents are zero credit |
| parity and first atom | bipartiteness and unique shortest path | coefficient support through profile-dependent horizons | elementary corollaries, bundled with transform |
| compact scalar variance | one-attempt moment recurrences plus stopped renewal | transform derivatives and an additional shared-engine parameter sweep | generic second moments and Pearce endpoint/mean are inputs only |
| sharp fixed-mass interval | strict reciprocal unit transfers | exhaustive positive compositions in bounded boxes | convexity/majorization is a tool |
| inverse boundary | endpoint ratios, primitive integer ray, mean scale | gcd normalization and dilation controls | tomography framing is zero credit; no unknown topology/kernel |

## Sources and subtraction

- Pearce: finite-tree absorbing endpoints and expected length.
- Pal--Mesikepp: unequal-arm endpoint probability as an explicit exercise.
- Castella--Sericola: equal-arm star hitting distributions and moments.
- Sericola: generic finite-chain joint hitting-time/place laws and moment
  matrices.
- Chen: algorithms for hitting-time generating functions on general trees.
- de la Peña--Gzyl--McDonald: known-topology inverse transition recovery from
  richer boundary time/place data.
- de la Iglesia--Juarez: spectral and factorization framework for half-line
  spider chains, including constant-transition random walks.

All seven are cited as primary owners or nearest frameworks, never as evidence
of novelty.

## Presentation

Realized format: anonymous six-page A4 `amsart`.  One compact audit table is
used; no decorative figure is required.  Main text contains complete proofs
because each proof is short and structural.

## Review realization

Review A returned 0 Critical / 1 Major / 3 Minor.  The Sericola/Chen direct-
owner subtraction, de la Iglesia--Juarez journal metadata,
exact-versus-independent wording, and `Q(0)/Q(1)/D(1)` bridge were repaired.
Review B returned ACCEPT with 0 / 0 / 0 findings after cold replay, independent
mathematical pressure, two isolated builds, and all-page inspection.  The
accepted residual remains exactly the claim ceiling above.  External status
remains `HOLD_EXTERNAL`; `main_round2.pdf` is a pending archival copy, not a
new scientific round.
