# C87 results

Canonical evidence SHA-256:
`bedeb7a3d912330e5eadc72629ee24d773648993f73f20f23eaf477028334d6e`.

The evidence retains:

- 16 complete first-order rows, each with 16 coalition-size cells;
- 120 complete unordered-pair rows, each with 15 positive, negative, and
  signed coalition-size cells plus zero and total counts;
- exact raw, uniform Banzhaf, and factorial-weighted Shapley values;
- seven faithful label orbits and all 27 faithful unordered-pair orbits;
- ten exact pair numerical classes and their full pair memberships;
- first-order efficiency, all per-label pair endpoint identities, and orbit
  constancy checks.

The first-order totals are 40704 raw swings, Banzhaf sum `159/128`, and
Shapley sum `1`.  Across unordered pairs, the Shapley interaction sum is
`1/2` and the uniform Banzhaf interaction sum is `-119/256`.  Seventy-five
pairs have identically zero second difference; the other 45 occupy nine
nonzero numerical classes.

The distance-one boundary identity with C82 is
`40704 + 445696 = 16 * 30400 = 486400`.

The 1920-element faithful label action is explicitly separated from the
11520-element ambient lift and its order-six label-action kernel.
