# Stage 4 author-decision interpretation

Date: `2026-08-26` (UTC)  
Round: P67--P71, revision round 1  
External release: `HOLD`

## Explicit author event

The author approved the already stated next-stage policy with the exact
session message (UTF-8 bytes, no trailing newline):

> 可以，进行下一阶段

The event is recorded as
`AUTHOR-EVENT-2026-08-26-stage4-approval`; its SHA-256 is copied into each
canonical `author-adjudication/1.0` sidecar by
`build_stage4_authority.py`.

This approval is read together with the standing authorization to carry each
five-paper round through internal stage transitions without another
conversation checkpoint.  It authorizes the exact bounded policy announced
before execution:

- address every decision-bearing `must_fix` item;
- address each `should_fix` item that can be closed by local mathematical
  argument, source evidence already verified in Stage 2.5, or a deterministic
  finite control;
- retain an item as `wont_address` when it requires an unavailable external
  specialist review, and preserve the associated non-priority/HOLD language;
- defer `consider` items that expand the paper beyond this revision round.

No author choice is inferred from silence: all four roadmap items for every
paper are represented exactly once in the machine-readable sidecars.

## Exact dispositions

| Paper | `will_address` | `wont_address`: external specialist HOLD | `wont_address`: optional defer |
|---|---|---|---|
| P67 | EIC notation; R1 extension-field control | R2 owner boundary | R3 adjacent application |
| P68 | EIC contract hierarchy; R1 singleton control; R3 statistical-mechanics dictionary | R2 owner boundary | none |
| P69 | EIC roadmap correction; R1 mixed-indicator control | R2 collision review | R3 transfer checklist |
| P70 | EIC theorem-component comparison; R1 non-split control; R3 coding/spectral bridge | R2 exact-neighbour specialist review | none |
| P71 | EIC theorem-component comparison and narrowed headline; R1 repeated-extremal control | R2 exact-neighbour specialist review | R3 weighted-transition roadmap |

P70's EIC item and declined R2 item both touch `B0056`.  The exact collateral
authorization `COLLATERAL-AUTH-P70-EIC-over-R2-B0056` permits only the EIC's
`replace_block` operation while requiring the new prose to say that specialist
clearance remains unresolved.

## Chain-start scope

The five `integrity-pass-receipt/1.0` files bind the exact Stage 3 anchored
write bases after replay of the Stage 2.5 mathematical/source gate, Stage 3
base/manifest validation, and the five frozen deterministic controls.  Their
`open_issue_count: 0` refers only to defects in those internal write bases.
It does not clear or supersede priority, specialist, author-identity,
venue-disclosure, or external-release gates; all of those remain `HOLD`.

