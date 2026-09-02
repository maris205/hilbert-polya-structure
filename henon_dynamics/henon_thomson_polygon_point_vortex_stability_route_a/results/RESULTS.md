# Results

- Complete analytic mode rows: **2,077** (`N=3..64`, every DFT label).
- Polygon classification rows: **62**.
- Exact circulation/radius scale rows: **64**.
- Exact symmetry-slice rows: **7**.
- Explicit singular or symmetry boundary cells: **8**.
- Producer-independent raw-Hessian/slice assertions: **65,655 PASS**.
- Independent exact symbolic identities: **4,585 PASS**.
- Two-fresh-path replay: **byte-identical PASS**.
- Hostile mutations: **76/76 rejected**.
- Evidence bytes: **885,870**.
- Evidence SHA-256:
  `4fed9820df14c399e53fb3e616d3451297ebd055f78f8123fcdfb39db9462a53`.
- Embedded payload SHA-256:
  `923d0100ff00ba1e24b1740f8a530282a6c4c418d24191247ea4edef6766b6e3`.

The exact source theorem is the block identity

```text
Gamma^(-1) D^2 G_hat_m
  = c diag(2(N-1)-m(N-m), m(N-m)),
c = Gamma/(4*pi*R^2).
```

It gives reduced linear ellipticity for `N=3..6`, linear degeneracy only in
the conjugate labels `m=3,4` for `N=7`, and a real hyperbolic pair for every
`N>=8`.  The finite cells are regression certificates, not the proof of the
all-`N` statements; the root-of-unity identity and sign argument provide that
proof.  The evidence parser separately enforces exact schemas and types,
semantic row uniqueness, and rejection of duplicate JSON keys.
