# P124 paper plan — basin-centered theorem lock

Status: **ROUND2 GO_INTERNAL / EXTERNAL HOLD**.

## One-sentence contribution

For the literal crossed-colon map on rectangular monomial ideals, determine
the basin of every recurrent orbit and count every basin by a uniform
four-state contact-parity transfer.

## Frozen theorem contract

1. Literal colon arithmetic converts the map to independent sourced
   disjunctive paths on total-degree diagonals.
2. Upper-set compatibility leaves exactly `m` fixed powers and `m-1`
   checker two-cycles, with `3m-2` recurrent states.
3. The sharp maximum depth is `m` off the square and `max(1,m-2)` on the
   square.
4. The first occupied diagonal and its parity trace completely characterize
   the attracting fixed point or checker orbit, including the eventual
   checker phase.
5. A four-state boundary-contact recurrence gives each basin size for all
   `a,b`; its nonempty-mask sum and the terminal fixed basin have reflection
   formulas.

## Paper structure

1. Literal map, scope, and owner subtraction.
2. Staircase and diagonal normal forms.
3. Supporting recurrent/depth classification.
4. Central first-trace basin theorem.
5. Central contact-parity transfer and ballot controls.
6. Exact verification, limitations, and conclusion.

No figure is required: the diagonal source table and the `a=5,b=7` basin
table carry the exact relationships more efficiently than a diagram.

## Owner subtraction

- Goles--Hernandez and later disjunctive-network work own the OR-network
  recurrence, graph-walk interpretation, periods, and transient mechanism.
- Monomial ideals as rectangle upper sets, colon arithmetic, staircases, and
  boundary paths are standard commutative/combinatorial background.
- Ballot/reflection counting and finite-state transfers receive zero method
  credit.
- Generic algebraic basin algorithms and rowmotion/toggle work are contextual
  neighbors only.

## Claim ceiling

Allowed: exact statements for this synchronous map on monomial ideals,
including recurrent families, maximum depth, first-trace basin partition, and
the stated contact transfer.

Forbidden: first/novel/priority claims, ownership of OR-path or ballot
mechanics, extension to nonmonomial ideals, minimality of the transfer,
closed forms for the separate checker parity counts, and external-release
language.

## Round-2 theorem lock

Review B found `0 CRITICAL / 0 MAJOR / 0 MINOR` after independently auditing
all theorem statements, proof equations, degenerate boundaries, the two
verifier lanes, and the rendered artifact.  The theorem contract above is
therefore frozen at `GO_INTERNAL`.  Round 2 changes support records only:
`main.tex`, `references.bib`, verifier/canonical pairs, and all existing PDF
bytes remain untouched.  The bounded owner search is still not a novelty
certificate, so the external gate remains `HOLD`.
