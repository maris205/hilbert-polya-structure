# P164 Review B — fresh owner audit

**Search date:** 2026-09-03  
**Disposition:** bounded non-hit for the residual conjunction  
**External status:** `HOLD_EXTERNAL`

This is a new Review-B search, not a novelty certificate.  Classical engines
and direct prior owners receive zero contribution credit whether or not they
are needed in the short proof.

## Primary records checked directly

1. Martin, Odlyzko, and Wolfram, [*Algebraic Properties of Cellular
   Automata*](https://doi.org/10.1007/BF01223745), *Communications in
   Mathematical Physics* 93 (1984), 219--258.  This owns the algebraic
   finite-cellular-automaton background and transition-diagram machinery.
2. Kim, [*Cycles of Characteristic Matrices of Cellular Automata with
   Periodic Boundary
   Condition*](https://kkms.org/index.php/kjm/article/viewFile/107/80),
   *Korean Journal of Mathematics* 19 (2011), 291--300.  The paper explicitly
   defines periodic Rule 102 by `x_i(t+1)=x_i(t) xor x_(i+1)(t)`, studies its
   characteristic-matrix powers, and gives the power-of-two vanishing result.
   It is a direct owner of the binary `D=I+S` tail.
3. Zhao, Li, Yang, Fu, and Shum,
   [*Weight Distribution of Repeated-Root Cyclic Codes with Prime Power
   Lengths*](https://arxiv.org/abs/2304.00762v3), arXiv:2304.00762v3
   (revised 2025).  The current v3 primary record confirms the printed title,
   five-author list, revision year, and the substantially broader repeated-
   root weight-distribution scope.  Homogeneous repeated-root enumerators are
   therefore fully subtracted.
4. Bolognesi and Ciancia, [*Exploring Nominal Cellular
   Automata*](https://doi.org/10.1016/j.jlamp.2017.08.001), *Journal of
   Logical and Algebraic Methods in Programming* 93 (2017), 23--41.  This is
   the closest primary equality-pattern vocabulary hit.  Its carrier is a
   countably infinite nominal alphabet with equivariant local reactions; it
   does not state the finite q-ary map reviewed here or its affine-code fibre
   atlas.

The four bibliography entries in `references.bib` match those current
records.  In particular, arXiv:2304.00762 changed title and author list by
version 3; the manuscript correctly cites the current 2025 version rather
than the older metadata still returned by some indexes.

## Bounded direct-owner search

The following query families were searched with exact-map terms and primary
publisher/arXiv restrictions:

- `cyclic equality feedback cellular automaton`;
- `q-ary adjacent equality indicator cellular automaton`;
- `equal to right neighbour binary output cellular automaton`;
- `equality indicator Rule 102 finite cyclic words`;
- `change mask q-ary cyclic word adjacent unequal`;
- `Rule 102 periodic boundary preimage fibre`;
- `repeated-root cyclic code affine coset weight enumerator`;
- `nominal equality cellular automata adjacent pair`.

No inspected primary record stated the literal finite map
`w -> (1{w_i=w_(i+1)})_i` together with its q-weighted all-time affine target
fibres, sharp dyadic shell census, and both evaluated fibre spectra.  Search
results that discussed generic additive CA, Rule 102 powers, nominal equality
patterns, or repeated-root code weights were already captured by the four
owners above and are explicitly zero-credit in the manuscript.

## Residual after subtraction

The following receive zero contribution credit:

- finite additive/affine CA theory and the Rule-102/153 tail;
- dyadic nilpotence, kernel/image dimensions, and repeated-root code weights;
- the cycle chromatic polynomial and Fourier inversion;
- generic equality-pattern cellular automata.

The residual conjunction begins only with the literal q-ary equality front:
its nonuniform change-mask multiplicity, the induced q-weighted every-target
affine fibres, and the target-parameter evaluations at time two and at the
midpoint, coupled to the exact source-depth shells.  The bounded search did
not find a direct owner of that conjunction.  This supports only the
manuscript's cautious `owner-thin` language, not novelty, priority, or release.

