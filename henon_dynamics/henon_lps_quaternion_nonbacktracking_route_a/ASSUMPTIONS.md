# Assumptions and conventions

- `q` is a rational prime greater than five with `q = 1 mod 4`.
- `iota_q` is a square root of `-1` in `F_q`.  The least positive root is
  used only to make evidence bytes deterministic; the other root gives a
  conjugate Cayley graph.
- The six quaternions are `(1,±2,0,0)`, `(1,0,±2,0)`, and `(1,0,0,±2)`.
  Each has Hamilton norm five.
- Matrices are taken projectively.  Rescaling a representative does not
  change a vertex, adjacency, determinant square class, or dynamics.
- The Cayley convention joins `g` to `g s`.  The inverse pairs are
  `(0,1)`, `(2,3)`, and `(4,5)` in the frozen generator order.
- The Hashimoto state space consists of oriented edges.  A step may use any
  generator except the inverse of the previous generator.
- Primitive cycles are orientation-distinguished and identified under
  cyclic rotation, not under reversal.
- Connectedness and the Ramanujan adjacency bound are invoked from the LPS
  theorem.  The general determinant identity is invoked from Bass and
  Hashimoto.  All specializations and consequences are proved explicitly.
- The prime number theorem for arithmetic progressions is used only for the
  half--half conditional natural density of the two source chambers.  No
  effective error term is claimed.
