# Methodology blueprint

The project uses one invariant object throughout: the lifted orbit monomial
`z^(n-S)w^S`, whose restriction `w=qz` is P70's `z^n q^S`.

- lift P69's reflected transfer polynomial before summing periods;
- apply the same odd dilation Möbius inversion and Euler repetition law as
  P70;
- regroup by `m=kr` and retain P72's exact coefficient `c_m`;
- prove `|c_m|<=1` and use a compact-polydisk tail bound for normal
  convergence;
- prove smoothness and local finiteness of the hypersurfaces `H_m`;
- restrict to `w=qz`, establish strict radius separation, and compute the
  local principal coefficient at all `2m` roots;
- keep joint-hypersurface collisions, dense boundary accumulation, Lind
  comparison away from `q=1`, operator ownership, and arithmetic semantics
  outside the theorem.

Finite code compares exact weighted coefficients and audits geometry; it is
not used to prove the all-channel assertions.
