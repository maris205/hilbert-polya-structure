# 059 — Primitive-lattice Hénon A0 screen

**Candidate:** `ASFS-20260914-NPH01`  
**Status:** `P0 FROZEN; A0 SCOPED FAIL — PRIMITIVITY IS A STATIC EXTERNAL STRATUM`

The nonlinear area-preserving Hénon-type map `F(x,y)=(y,y^2-x)` preserves
integer gcd and hence primitive lattice vectors. This repairs the linearity
issue of 058, but not arithmetic ownership: the map preserves every gcd stratum
and does not itself derive a prime-specific observable. A1 is intentionally not
evaluated after this decisive A0 stop.

- [paper](paper.md) · [candidate card](candidate-card.md) · [claims](claim-ledger.md) · [evidence](evidence/README.md)
