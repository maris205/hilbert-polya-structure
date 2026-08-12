# R401-VAL-V2 Composite Protocol Freeze

Freeze date: 2026-08-06 UTC.

The independently reviewed production protocol is the ordered composite of
the following immutable files:

| component | SHA-256 |
|---|---|
| base protocol | `d00d95f32ddfe4420da2cdac46ef1a3bb39bb3ea2277a21a9776652794a20d82` |
| V2 amendment | `a163be8800ecc1677ccaf2f6342becfe834d55d80ad59dcc24180e3f0f5e62aa` |
| A4.11a radial proof | `b991cf5ffce043db60ceaf2448f383364c66dca66812180fb996c19debcd11bb` |
| A4.11b warped proof | `71cc840cd6518ecb4672402fbe2517ae5096bb654872abce32ef21d02a7e26d8` |

Protocol identifier: `R401-VAL-V2`.

Production result namespace:
`results/r401_validated_theorem_domain_v2/`.

The V2 amendment received an independent `ACCEPT` after two rounds.  The
review specifically checked the shared-parameter Taylor-model replacement,
exact rational coefficient normalization, absorption of coefficient
uncertainty into the remainder, the event-projected Poincare determinant,
fixed-time monodromy convention, namespaced final statuses, and manifest
binding.

The local CAPD endpoint-slab and Arb point computations are implementation
milestones under this protocol.  They cannot change the final theorem status
or produce a lower bound for `delta_tr` until the contiguous branch,
root-complement exclusion, phase-cover tree, and global shell cover all pass.

