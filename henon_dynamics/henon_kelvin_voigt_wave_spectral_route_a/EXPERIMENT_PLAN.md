# Exact-computation plan

1. Enumerate modes `n=1,...,64` for five rational damping values, plus the
   undamped boundary `b=0` and the critical sentinel `b=2`.
2. Serialize both roots, discriminants, regime labels, slow-root asymptotics,
   and the exact gap formula at 50 working digits.
3. Independently recompute the quadratic roots, Jordan criterion, energy sign,
   high-frequency limits, and the optimizer; use a separate NumPy path for
   finite block exponentials.
4. Use SymPy for the quadratic pencil, rationalized slow-root inequality, gap
   derivative, and energy identity.  Replay bytes and run repaired-hash,
   stale-hash, unknown-key, route, and sign mutations.
5. Compile three substantive revisions at a fixed epoch and close the
   self-excluded 27-payload manifest after deleting all sidecars.
