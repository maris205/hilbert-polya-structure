# Deterministic control results

Run date: **2026-08-26 UTC**.

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

### Nonprime extension-field control

- Exact polynomial-basis arithmetic used
  $\mathbb F_4=\mathbb F_2[u]/(u^2+u+1)$; field addition, multiplication,
  inversion, and Gaussian elimination were implemented without numerical
  approximation or a prime-field surrogate.
- All 80 prefix ranks through cutoff 80 for $(a,b)=(2,3)$ agreed with
  $\lfloor N/6\rfloor$.
- Every one of the $2^{12}=4096$ coordinate subsets had the direct
  $\mathbb F_4$ projection dimension predicted by its root-wise graph rank.
- All 36 exponent rectangles through side length six and three exact Haar
  forest/cycle enumerations satisfied the stated rank, fibre, pairwise
  independence, and four-cycle relations.

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
8cd3bee21428e8b1701e02ff054d5627dc1f1c7e5e1389694e51f5e370491431

output SHA-256:
f3eeb1dbdc67b81bf6848c2aa92f92a5b29dad3bfac8fff61c0cee343b5b2432
```

The live output, `code/verify_plaquette_matroid.out`, and
`stage4/CONTROL_RUN.out` are byte-identical.

## Evidentiary limit

The checks use exact modular arithmetic and exact integer graph operations;
there is no numerical tolerance or randomized hash.  They remain finite
regression controls.  They do not prove the infinite root decomposition,
global product homeomorphism, arbitrary-size cycle characterization, or
literature status.  Those arguments are self-contained in the manuscript and
`PROOF_PACKAGE.md`.
