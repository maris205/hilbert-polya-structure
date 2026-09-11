# CPC — closed without promotion

Root author, 2026-09-06 UTC. **NO_PROMOTION**, no reserve or paper ID.
The literal and predeclared complete boxes are in [the intake](CPC_INTAKE.md).
The actual [pilot stdout](CPC_CANONICAL.jsonl) has all seven rows and
29,511 source states for $n=3,\ldots,9$. The standalone counterexample
extractor uses only the original $n=8,9$ boxes; it does not expand a cutoff.

## Temporal boundary

The complete small boxes already have genuine periods 24 and 32 at $n=8$,
and 8 and 30 at $n=9$, alongside smaller periods. Maximum tails are
$2,2,9,7,11,15,26$. No all-length temporal/core theorem follows from
these heterogeneous profiles, and none has been proved here. The separate
[counterexample stdout](CPC_COUNTEREXAMPLES.jsonl) records complete
distinct-state cycles of exact lengths 32 and 30, verified by literal
modular-difference updates at every transition. This is an author check,
not an independent gate.

## Proved weak static statement and its deduction

Claim: for every $n\ge3$, fixed words are exactly words over $\{0,2\}$
in which each two has two zero neighbours. Status: `PROVABLE AS STATED`.
Assumptions are precisely the ternary synchronous rule in the intake.
The proof uses only the local equations, then the classical independent-
set interpretation; it supplies no temporal classification.

At a fixed zero neither neighbour can be one, because one is zero's
successor colour. At a fixed two both neighbours must be zero, because
the output count is two and zero is two's successor. A fixed one would
need at least one neighbouring two, but that two would then have a
nonzero neighbour, contrary to the preceding equation. Thus no one
occurs. The zero/two conditions are also sufficient by direct substitution.
Equivalently the positions carrying two form an independent set of the
labelled cycle. The fixed count is the classical Lucas count $L_n$;
this fixed-set encoding and count have zero independent value credit.

No full-target inverse/extremal proof is claimed. A generic local
transfer matrix alone would not fill the missing axes. The prepilot
search found nearby successor-colour and cyclic-dominance descriptions;
it did not establish an exact owner. No full external source clearance,
publication novelty, submission or contact is claimed. The absence of
a qualifying temporal/inverse conjunction suffices for nonpromotion.
The original rule and all adverse finite evidence are retained.
