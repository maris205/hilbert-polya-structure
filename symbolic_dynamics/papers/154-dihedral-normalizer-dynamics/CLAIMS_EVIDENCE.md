# Claims and evidence

Status: `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

| ID | Claim | Formal support | Deterministic control | Credit boundary |
|---|---|---|---|---|
| GDN-1 | complete subgroup coordinates | cyclic rotation part plus one reflection coset | key count and set uniqueness | Cavior and Conrad; zero credit |
| GDN-2 | complete one-step normalizer formula | conjugation conditions d divides 2u and 2(u-j) | literal ambient conjugation for every audited subgroup | Frenkel and Shelash et al.; zero credit |
| GDN-3 | t-fold halving and binary forest | iterate GDN-2 and enumerate residue lifts | literal depths and fixed roots | dynamical synthesis begins here |
| GDN-4 | depth polynomial and fixed counts | count each binary level and rotations | exhaustive depth multiset | derived from GDN-3 |
| GDN-5 | every image and target fibre | reachable levels and residue lifts | every target through a+3 | all-time pointwise atlas |
| GDN-6 | iff signature | recover fixed roots, a, and repaired total-vertex tau; construct matching | four explicit equal-signature pairs; bounded pressure | full graph classification only |
| GDN-7 | 33/35 and lifted collisions | explicit base conjugacy plus signature theorem | literal base boxes and commuting map | graph conjugacy, not group isomorphism |

The all-parameter theorem is proved in main.tex. Exact replay is a bounded
regression seal.

Review-A quantifier closure: the iterated rule now states
`t >= 0`, `0 <= k <= a`, `e | m`, and `0 <= j < 2^k e`; the positive-level
fibre theorem states `t >= 1`, `1 <= k <= a`, and the complete carrier domain.

Hostile Review B independently rederived every claim row, verified the
Review-A quantifier/source/build repairs, and returned
`ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor`. No claim, proof,
bibliography, verifier, or transcript changed in Round 2. The only source
change is the post-review build-only `microtype` option that disables font
expansion while retaining protrusion and removes a latent pdfTeX warning.
