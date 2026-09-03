# HCS-C336 hostile audit

The hostile lane rejected 70 of 70 attacks.  The attacks include repaired
semantic hashes, so success is not explained by a stale checksum alone.

## Mathematical attacks

- mutation pole sign and `2/L` normalization;
- binomial Walsh weight and retained multiplicity;
- secular coefficient, trace and interlacing interval;
- a false root below the lowest mutation pole;
- Walsh-mask, eigenvalue and residual changes;
- quotient mean-fitness and tangent-vector changes;
- wrong `s=0`, `U=0` and `L=1` conclusions;
- removal of the finite-length/no-error-threshold boundary.

## Integrity and scope attacks

- source commit, epoch, evaluator digest and literal scope;
- candidate and obstruction IDs;
- target Euler-factor, root-number, automorphy, zero-match and Route-B flags;
- JSON duplicate keys, nonfinite values, wrong root type, unknown or missing
  fields and stale payload hash;
- YAML duplicate/non-string keys, anchors, aliases, merges, implicit date,
  type changes, semantic changes, raw-byte changes and Route-B escalation.

The unmodified evidence/evaluation pair passes before every attack series.
