# Exact validation plan

1. Sweep `k=1,...,12`, five exact values of `beta^(1/k)`, two fertility
   scales, and three mortality scales: 360 parameter cases.
2. Expand every characteristic polynomial exactly over the rationals.
3. Generate all 2,340 roots at 90-digit precision and classify each as an
   `L1` eigenvalue, essential-edge root, or algebraic root below the edge.
4. Audit the isolated-real-pole threshold `beta=1` separately from the
   population threshold `(1+mu/gamma)^k`.
5. Check six zero-birth boundaries, symbolic Erlang transforms, byte replay,
   and repaired-hash semantic mutations.

No GPU run is appropriate.  The experiment is a deterministic convention and
boundary audit for an analytic semigroup theorem.
