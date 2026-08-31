# HCS-C257 hostile audit

The mutation suite changes one semantic field at a time, repairs the payload
hash whenever applicable, and invokes the producer-independent quick checker
in a clean subprocess.  All 41 attacks are rejected.

Covered attack classes include:

- schema, candidate, date, source commit, epoch, evaluator, scope, and unknown
  top-level fields;
- frozen phase space, Newton map, and Cayley coordinate;
- A1 grade, overall verdict, Route-B permission, forbidden flags, and the
  degree-only obstruction;
- global conjugacy, basin/Julia theorem, root-order tail theorem, and C141/C177
  ownership boundary;
- period row count/index, fixed and exact counts, primitive quotient, and
  multiplier;
- root-order count, $v_2$ tail, odd part, landing period, and periodic versus
  strictly-preperiodic class;
- exact basin iterate, basin label, Cauchy map, and Cauchy density;
- identity deletion/corruption, citation URL, nonclaim deletion, and stale
  payload hash.

The repaired-hash design demonstrates that content addressing alone is not
the semantic gate.  The checker rejects false claims even when an attacker
recomputes a valid hash for the altered payload.
