# Root spike R01 — synchronous graph Bellman envelopes

Status: `PROVISIONAL_SURVIVOR / OWNER_AMBER / HOLD_EXTERNAL`.

Let `G=(V,E)` be a finite simple graph, let `h>=0`, and put
`X_{G,h}={0,...,h}^V`.  The literal synchronous map is

`T(x)_v=min({x_v} union {x_u+1:u~v})`.

The proposed all-parameter contract is:

1. `T^t(x)_v=min_{d(v,u)<=t}(x_u+d(v,u))`, with disconnected distances
   excluded from the minimum.
2. Every orbit reaches a fixed point; the fixed points are exactly the
   integer `1`-Lipschitz height functions on `G`.  The pointwise tail is the
   largest, over `v`, of the least distance to a minimizer of
   `x_u+d(v,u)`.  The sharp global height is
   `min(diam_component(G), max(0,h-1))`, where the first term is the largest
   component diameter.
3. Fixed points are graph homomorphisms into the reflexive path on
   `{0,...,h}`.  For paths and cycles this becomes an explicit transfer trace.
4. For every `t>=0` and every labelled target `y`, define
   `ell_u=max(0,max_{d(v,u)<=t}(y_v-d(v,u)))`.  Then

   `|T^{-t}(y)| = sum_{S subset V} (-1)^|S|
      product_u [h-max(ell_u,max_{v in S,d(v,u)<=t}
      (y_v-d(v,u)+1))+1]_+`.

   Thus image recognition, all transient layers, terminal basins, zero
   fibres, and total mass are target-resolved rather than inferred from a
   generic state count.

The Bellman/shortest-path relaxation and the metric-envelope identity receive
zero originality credit.  The retained residual, if owner checking survives,
is the finite functional-graph clock together with the all-time labelled
inverse formula.  P90's particle min-plus formula is a method neighbour, not
the same phase space or map; closure-only and graph-flood claims remain
excluded.
