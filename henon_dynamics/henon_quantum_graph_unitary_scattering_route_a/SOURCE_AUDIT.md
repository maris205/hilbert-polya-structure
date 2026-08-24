# Source audit — HCS-C133

## Frozen source

- graph: two vertices with three parallel undirected edges;
- metric lengths: `(1,2,3)`;
- vertex rule: degree-three Kirchhoff continuity/current conservation;
- directed-bond order: `e1_LR,e2_LR,e3_LR,e1_RL,e2_RL,e3_RL`;
- scattering convention: `sigma_fe=2/3-delta_fe`;
- propagation convention: `U(k)=P(k) S P(k)` with one half of each traversed
  edge phase on either side of scattering;
- determinant: `D(rho,k)=det(I-rho U(k))`;
- arithmetic: exact rationals and symbolic Laurent/polynomial identities.

The source contains no fitted parameter and no external dataset.  The edge
lengths and vertex rule were fixed before computation.

## Evidence boundary

The paper proves a finite-dimensional unitary/scattering candidate and an
intrinsic primitive directed-bond expansion.  It does not prove that these
orbits have prime-like semantics, that the secular zeros match a target
divisor, or that the graph realizes a Hilbert--Pólya operator.  The scope
firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`; prime/zero tables, arithmetic local
factors, Euler factors, root numbers, automorphy, and Route-B inputs are
forbidden.

## Controls

- replacing `2/3` by `1/2` in the vertex rule produces a nonzero rational
  unitarity defect;
- changing only the reverse length of the third edge destroys the physical
  `J K` reversal because it is no longer one metric length per undirected
  edge;
- finite replay periods are sentinels only; the determinant/trace/product
  statements are matrix identities for all orders.
