# Paper 38 figure specification — SD-C40

All artwork is writer-owned pure TikZ.  No external image, rasterization,
opacity, color-only distinction, or data-driven plotting script is used.
Labels must remain legible at ordinary A4 scale and in grayscale.

## Figure 1 — full-tree/orbital terminal trilemma

File: `figures/tree_orbit_trilemma.tex`.

- Common source box: original presentation-canonical ascending HNN splitting
  of `BS(1,r)`, canonical modular cocycle, and a new tree-edge marker.
- Upper branch: literal full-tree geodesic shift; badge `no reduced closed
  path`; output `primitive ledger empty`.
- Middle branch: full-tree Hashimoto operator; infinite orthogonal
  constant-norm columns; output `noncompact / no ordinary Fredholm`.
- Lower branch: group-orbital substitution; `r>=2` goes to the generic
  necklace law, while `r=1` goes to divergence.
- Side firewall: quotient, von Neumann, groupoid, and radial-weight objects
  cannot cross into the full-tree determinant box.
- Shared terminal badge: `CLOSE_ENTIRE_AFFINE_BRANCH`.
- Caption must state that the three rows are different ownership categories
  and none gives a nonempty selective same-object Fredholm ledger.

## Figure 2 — conjugacy-to-necklace pipeline

File: `figures/orbital_necklace.tex`.

- Left: semidirect product `Z[1/r] semidirect Z` and the conjugation formula.
- Next: fixed-height quotient `Z/(r^k-1)Z` with multiplication by `r`.
- Center: a circular necklace sketch showing cyclic rotation and the special
  endpoint identification `0^k ~ (r-1)^k`.
- Next: Burnside and Möbius badges for `C_r(k)` and `P_r(k)`.
- Right: rational output `(1-z)/(1-rz)` and modular substitution
  `z -> r^{-s}z`.
- A dashed barrier below the pipeline says `group conjugacy != full-tree
  periodic point`.
- Caption must identify the formula as exact but generic, not as a rescue of
  the frozen object.

## Figure 3 — marker and determinant-category firewall

File: `figures/marker_fredholm_firewall.tex`.

- Top comparison: old written Cayley paths `u^m`, `u^m v`, and the defining
  relator with lengths `m`, `m+1`, and `r+3`.
- Bottom comparison: Bass--Serre translation lengths `0`, `1`, and `0`.
- A many-to-one funnel visually demonstrates marker incompatibility.
- Right-side category table:
  - full-tree ordinary Fredholm: fails trace class;
  - discrete tree-lattice/von Neumann: for `r>=2` the faithful image is
    non-discrete; for `r=1` the image is discrete but the frozen action has
    infinite kernel, is non-proper, and fails finite-stabilizer hypotheses;
  - finite-total-weight graph: needs a different summable weight;
  - groupoid/double-coset: different trace or invariant.
- Caption must make clear that alternative determinant theories are valid in
  their own categories but do not transfer ownership.

## Shared visual language

- `formalblue`: frozen source, definitions, and exact maps.
- `deepgreen`: valid derivations and independently owned neighboring theory.
- `warningamber`: object changes, genericity, or incompatibility.
- `stopred`: emptiness, non-Fredholm status, divergence, and terminal stop.
- `softgray`: quotient/state-space grouping.
- Solid arrows denote proved implications or exact maps.
- Dashed arrows denote blocked credit transfer and are never claimed maps.

## Figure quality checklist

- vector TikZ output;
- no internal decorative title;
- minimum text size consistent with the 11pt body;
- no red/green-only encoding;
- line styles and labels remain meaningful in grayscale;
- no crowded crossing arrows;
- self-contained captions in the manuscript;
- every figure is referenced before or at first placement.
