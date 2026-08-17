# SD-C42 exact corrected-input lock

status=FINAL_BEFORE_CANONICAL_EMPTY_RESULTS_RERUN
chronology=M1--M20_RETROSPECTIVE_CORRECTION

The provisional v1 outputs and multiple in-flight corrective smoke-test
outputs were known before this lock. This file makes one narrow timing claim:
the exact manifest and literal seeds/grids below are frozen before the single
canonical empty-results replacement rerun. It is not an untouched prospective
preregistration and grants no novelty or priority credit.

## Exact pre-canonical file set

The following 15 paths are the complete file set in this pre-canonical lock.
The verifier rejects a missing path, an extra path, or a byte mismatch.

2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041  SOURCE_LOCK.md
a9dcbc922f8c47b0b845e7c6e76422aad3a0e744940a6529c2172176f5725bc5  MAYER_SOURCE_BOUNDARY.md
0739263b6da1795bfa693ba2600e92a87fd973d9af08398d505a8fa4afa3190c  SELECTION_AUDIT.md
0c4025b6f14de1e91f76ccfe9f327b62a8e91f4e5fd5a926eb4440ecfb3d5bd8  control_reference.py
b8c64a6b55dd7aa737804af252adda341115482441297438c7fa69bd247b71dd  control_independent.py
edf7c04e96fffaa5ee082374fe7cad206697d00986dd85312faedf4541535313  test_control_reference.py
05cd8ec052080ce08fd5a0f4597c7a2f3c17a5c36d96258589c668b0cb7a5c8d  prototype_reference.py
2b503d24acdc7da0ab1559b3cf9d15c64b2fa37314f2a4ee919d3040dbb40a21  prototype_independent.py
377680b5d5b7a4faa61c7f1386e2931052d25921faf165c482cfe095fcfe0488  test_prototype_reference.py
ee47a9c90c6bfbc54ba6b09b21f416dcece58b0d0ba9a391ca196d1b41d365a2  inputs/route_cards/SD-C01.yaml
5b5e9a2fe33a0ba8d281cf59c8f5346b95033c655d258554c0f76f8cfa0a434f  inputs/route_cards/SD-C02.yaml
2263b1c7bac4336628f444ded88e4e2ad98117f430113faf1ea5a91c16380328  inputs/route_cards/SD-C03.yaml
0609076081ccd69e9ffa3e0f708d426a33f7d41e2884f90bb2792bbc90209a92  inputs/route_cards/SD-C04.yaml
4a18295b1e20245c7196f21be4e4afc52857bf981efb461556720ab9e8ab5ed1  inputs/route_cards/SD-C05.yaml
d93683662a0cbee8e07d79329477d8b60bb273fb72e4bd64c05847e09a576c1b  inputs/route_cards/SD-C06.yaml

## Literal deterministic seeds

a0_composites=42003
a0_matched_density=42002
a0_pseudoprimes=42004
a0_randomized_labels=42005
a0_shuffled_primes=42001
a1_random_phases=42103
a1_random_weights=42102
a1_same_density_lengths=42104
a1_shuffled_periods=42101

The generator is the 31-bit LCG
`x_(n+1)=(1103515245*x_n+12345) mod 2^31`, followed by the frozen
Fisher--Yates order in the locked code.

## Literal bounded grids and fixtures

control_digits=1,2
control_pair_lengths=1,2,3
prototype_D=2,3,4
prototype_pair_lengths=1,2,3,4

- Neighboring control digits: `2,3`.
- Prototype canonical alphabets: `{1,...,D}`; neighboring alphabets:
  `{2,...,D+1}`.
- Typed return-map fixture: digits `1,2,3,4,5,6,7,8`, grouped by `iota`,
  with one-pair `rho` versus digit-space `sigma^2`.
- Non-palindromic raw-transfer fixture: stored digits `1,2,2,3,1,4`,
  `z=1/4`, `s=1`; correct value/weight `442/623`, `16/388129`; same-index
  mutation `146/697`, `16/485809`.
- Collision fixtures: trace 4 reversal pair, trace 6 one-pair non-reversal,
  and trace 10 cross-pair-length non-reversal.
- Exactly three projections: trace, order discriminant, geodesic norm.

## Excluded dependent renderings

Supersession, derivation, proof, ownership, primitivity, counterexample, Route,
literature, plan, report, result, summary, manuscript, compilation, and package
manifest files are deliberately absent from the exact set above. They are
post-run dependent renderings and receive no prospective status.
