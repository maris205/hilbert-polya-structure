# C305 hostile audit

## Mathematical attacks

- **Wrong strong root:** rejected. First contact is \(T_-\); \(T_+\) is the
  last attainable time, not the minimum.
- **Nested strong-wind balls:** rejected. Strong-wind attainable times form a
  finite closed window; they are not a lower ray.
- **Critical sign loss:** rejected. Nonzero critical targets require strictly
  \(p>0\), and \(T=r^2/(2p)\).
- **Optimizer nonuniqueness:** rejected for nonzero finite targets. First
  contact saturates the norm of the average control, and strict convexity
  forces the single constant vector a.e.
- **HJB sign error:** rejected by implicit differentiation and 12 independent
  probes of \(W\cdot\nabla T+c|\nabla T|=1\).
- **Cone overclaim:** rejected. Square-root regularity is asserted only at a
  nontrivial strong-wind boundary; \(c=0\), \(d=1\), and zero are separate.
- **Global Finsler promotion:** rejected. The strong value is finite only on
  its forward cone.

## Digital attacks

All 85 attacks must be rejected. Repaired payload hashes accompany changes
to full model/theorem/proof trees, root branches, reachability booleans,
interval endpoints, controls, HJB/scaling values, IDs, exact keys, and Route
A. Parser attacks cover stale hashes, duplicate/nonfinite JSON and
duplicate/anchor/alias/merge/wrong-type YAML.

## Scope outcome

No arithmetic bridge or operator candidate exists. The exact tuple has five
failures, overall `ROUTE_A_REJECTED`, and Route B is not invoked.
