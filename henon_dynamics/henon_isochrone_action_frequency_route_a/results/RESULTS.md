# Results

The exact certificate contains 116 audited cells: 108 action–frequency orbit cells and eight boundary cells.  Its frozen orbit partition is 36 `closed_degenerate`, 18 `closed_radial`, 14 `closed_resonant`, and 40 `nonclosed_irrational` cells.

| Gate | Result |
|---|---:|
| Independent exact/schema/quadrature checker | 11,254 assertions passed |
| Independent SymPy/exact cross-check | 1,099 checks passed |
| Fresh-path replay | two isolated byte-identical reproductions |
| Hostile validation | 87/87 attacks rejected |

Evidence payload SHA-256: `55c88124800ae58a683a1914b9ddb0dd40e54f514a36e8cf54bd00c32a39e82e`

Evidence file SHA-256: `3eafe6ca64829ce4389efe8d11b89f556f018e67bdd59595e2330e28c702f472`

Evaluation semantic SHA-256: `371a0e27dcd17ba950b06ab7ece415469ea998b244ba1eb6e208851182ec365d`

The finite cells are regression controls.  The all-parameter conclusion is proved analytically in `THEOREM_PACKAGE.md` and the paper.
