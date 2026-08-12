# R401-VAL Protocol Freeze Record

Freeze date: 2026-08-06 (UTC)

## Status

`R401_VALIDATED_THEOREM_DOMAIN_PROTOCOL.md` is frozen before implementation
or production execution.  A focused independent review first returned
`REVISE`; the protocol then added a strict endpoint margin, validated
`log1prel`, exact algebraic normal coordinates, a no-gap local phase-cover
tree, connected-section monotonicity, quantitative monodromy checks, and
non-destructive failure semantics.  The second review returned `ACCEPT`
subject only to four notation repairs, all of which were applied before this
freeze.

No validated global-flow result exists at freeze time.  The only promoted
claims are the analytic A4.11a--A4.11b reductions.

## Frozen hashes

| Artifact | SHA-256 |
|---|---|
| `R401_VALIDATED_THEOREM_DOMAIN_PROTOCOL.md` | `d00d95f32ddfe4420da2cdac46ef1a3bb39bb3ea2277a21a9776652794a20d82` |
| `A411_RADIAL_PERIOD_BOUND.md` | `b991cf5ffce043db60ceaf2448f383364c66dca66812180fb996c19debcd11bb` |
| `A411_WARPED_PERIOD_FLOOR.md` | `71cc840cd6518ecb4672402fbe2517ae5096bb654872abce32ef21d02a7e26d8` |

Any scientific change to a frozen file requires a new protocol version and a
new attempt namespace.  Result code may not silently weaken a gate from this
record.

## Frozen target

The preferred target is

\[
 0\le\epsilon\le0.101,
 \qquad
 \delta_{\rm tr}\ge0.010201>0.01.
\]

`PASS_ENDPOINT` is allowed only with an explicit certified
\(0.1<\epsilon_{\max}<0.101\).  Certification ending at
\(\epsilon_{\max}=0.1\) does not place the R401 cell inside the strict A4.9
domain.

## Next authorized action

Implement a non-claiming R401-VAL smoke for exact constants, special
functions, shell coverage, normal-coordinate reconstruction, and a small
validated local-branch slab.  A global `PASS` is unauthorized until the full
production and independent proof-object replay complete.
