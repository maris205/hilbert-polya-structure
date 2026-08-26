# Deterministic control results

Run date: **2026-08-25 UTC**.

Environment:

```text
Python 3.12.3
Linux 5.15.0-78-generic x86_64 GNU/Linux
Python standard library only
```

Command:

```sh
python3 code/verify_plaquette_matroid.py
```

Final status: **ALL CHECKS PASS**.

## Checks performed

### Multiplicative coordinates and global reconstruction

- 10,000 integers were decomposed for the coprime pairs
  `(2,3)`, `(2,5)`, `(3,4)`, `(4,9)`, and `(6,35)`.
- Each reconstruction satisfied `n=r a^i b^j`, the root exclusions, and the
  equivalence between `ab`-nondivisibility and membership in a component
  axis.
- Fifteen deterministic global-axis assignments over fields of orders
  `2`, `3`, and `5` were reconstructed and checked against every plaquette
  contained in the cutoff.

### Prefixes and arbitrary finite projections

- 320 prefix matrices through cutoff 80 had constraint rank
  `floor(N/(ab))` and graph dimension `N-floor(N/(ab))`.
- For three multiplier/field cases, every one of the `2^12` subsets of
  `[1,12]` was checked.
- In all 12,288 cases, direct projection of the finite prefix kernel agreed
  with the root-wise bipartite graph rank.

### Exponent rectangles and Haar dependence

- All `M x N` rectangles with `1<=M,N<=6` over fields of orders `2`, `3`,
  and `5` had dimension `M+N-1` and cycle rank `(M-1)(N-1)`.
- Exact potential enumeration checked a forest, a four-cycle, and a
  disconnected shape over all three fields.
- Every finite image was uniform with the predicted fibre multiplicity.
- Every distinct coordinate pair was independent, and every four-cycle
  obeyed the alternating plaquette equation, including in characteristic two.

### Edge deletion and addition

- Eleven exact graph transitions checked all four deletions from a four-cycle,
  all three bridge deletions from a three-edge tree, and four edge additions.
- Cycle-edge deletion preserved rank and lowered cycle rank by one; bridge
  deletion lowered rank and preserved cycle rank.
- Additions joining components or introducing vertices raised rank, while the
  addition closing a cycle preserved rank and raised cycle rank.

Frozen receipt:

```text
script SHA-256:
d0a2d3a1bd0c743b375eaf7e2dc98b100ff08f30cd741641cb1fcd81ab98a158

output SHA-256:
a44506264017a8e6250e123df4477898def6c23f560c67b4e829948967c0bb26
```

The live output, `code/verify_plaquette_matroid.out`, and
`build/verify_plaquette_matroid.current.out` are byte-identical.

## Evidentiary limit

The checks use exact modular arithmetic and exact integer graph operations;
there is no numerical tolerance or randomized hash.  They remain finite
regression controls.  They do not prove the infinite root decomposition,
global product homeomorphism, arbitrary-size cycle characterization, or
literature status.  Those arguments are self-contained in the manuscript and
`PROOF_PACKAGE.md`.
