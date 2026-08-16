# Methodology blueprint

The project uses the following proof-first architecture.

1. Freeze the P71 relative germ and P72 scalar coefficients with SHA-256
   dependency locks.
2. Resolve every denominator `1-2t^(2m)` into its `2m` complex roots and
   compute the exact principal coefficient at each root.
3. Test the unregularized pole family before grouping by channels; its
   absolute mass already diverges at `t=0`.
4. At level `m`, subtract Taylor degrees `0,...,m-1` from each pole.  Prove
   that the signed root sums of all subtracted terms vanish.
5. Bound the regularized level by a geometric majorant, proving absolute
   normal convergence and arbitrary pole-order independence on compact
   punctured subsets.
6. Rewrite P72's source remainder at `w=1+sqrt(2)t` and include the unique
   negative-boundary power-exponential factor and the `exp(3/2)` base-point
   normalization.
7. Verify exact formal coefficients, root ledgers, convergence bounds,
   dependency hashes, and claim firewalls with an independent implementation
   and hostile mutations.

Floating complex roots are diagnostic displays only.  All theorem-bearing
coefficient, cancellation, and bound checks use integers or `Fraction`.
