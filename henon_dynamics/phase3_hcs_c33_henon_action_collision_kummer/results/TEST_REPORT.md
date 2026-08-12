# HCS-C33 Phase-3 test report

## Frozen exact replay

- certificate payload hash:
  `21ba04e8518e1218550a1e70d8f73898b3fbf3afaf11931875e03ece4225c5da`;
- independent checker: `12/12 PASS`;
- regression and adversarial suite: `33/33 PASS`;
- frozen refresh wall time for the mutation suite: `328.250 s`.

## Mutation coverage

The suite rejects source drift, noncanonical JSON types, marker/action
coefficient drift, the wrong discriminant exponent, generic-reducibility or
Galois-prime ledger drift, a mutated collision value, field, or branch pair,
a degenerate tangent, chronology or slope-formula drift, omission of the
multiplier \(-1\) gate, an altered field norm, a falsified nonsquare finite
control, hidden post-hoc selection, a Route-A upgrade, a zeta promotion, and
unknown nested schema fields.  It also targets Python's boolean/integer
equality edge case inside nested factor-degree ledgers.

## Failure semantics

Expected mathematical mismatches must raise `GateFailure` or produce a
semantic `FAIL`.  Unexpected checker exceptions are reported as `ERROR` and
do not count as successful mutation rejection.

## Release command

The authoritative read-only reproduction command is `code/run_c33.sh`.
Manifest refresh is available only through the explicit
`code/run_c33.sh --refresh-manifest` release-preparation path.
