# P141 narrative report

Status: `ROUND-B OWNER-SUMMARY REPAIR COMPLETE / GO_INTERNAL (OWNER-THIN) /
HOLD_EXTERNAL`.

## Research question

This package is a specialized exact-law note on fully owned threshold-graph
support, the fully owned RSA/random-greedy process, and the fully owned
Plackett/exponential weighted order. Once all three inputs are assigned zero
contribution credit, what exact weighted distributional information remains?

## Mechanism found

The threshold creation order gives a right-to-left recursion. A last-created
zero is isolated and is always accepted. A last-created one is universal: it
forms the endpoint by itself if its exponential priority is first in the
prefix, and otherwise the first earlier accepted vertex deletes it. The
relative weighted order on the prefix is unchanged. Iteration is precisely a
reverse stick-breaking law with hazards `h_d=w_d/W_d` at dominant positions.

## Inverse and observable structure

Terminal masses recover every reverse hazard. Conversely, any strictly
positive distribution on the owned endpoint support determines hazards in
`(0,1)` and can be realized by positive rates, proving an open-simplex
parametrization. This does not recover the original vertex weights: all rate
vectors with the same hazards have the same endpoint law.

Mixing the known endpoint sizes gives the PGF of accepted active-set updates.
The same support representation gives every vertex marginal. Inclusion of an
earlier zero forces inclusion of every later zero, so zero-vertex events form
a nested family with explicit joint probabilities.

## Clock vocabulary

The note distinguishes four objects: `n` inspections in a full priority scan,
`K=|I|` accepted active-set updates, the numerical span of all exponential
priority labels, and continuous elapsed completion time. Only `K` has the
reverse-stick size PGF. Completion time obeys a state-dependent Laplace
recursion; no false substitution into the size PGF is made.

## Ownership and release boundary

Klivans owns the threshold-graph support. Pippenger and later random-greedy MIS
work own the RSA/random-greedy process family. Plackett owns the weighted
order, and its independent-exponential realization is standard owned
machinery. Theorem 3.1's weighted endpoint law and its inverse/simplex, PGF,
and marginal consequences are **owner-thin and folklore-risky**: they are
short consequences of those fully owned inputs. A bounded search found no
direct printed owner for that exact package, but this bounded direct-owner
non-hit is not novelty, priority, or owner clearance. The package is therefore
`HOLD_EXTERNAL`.

## Review history and Round-B closure

Independent hostile review A returned PASS at every critical, major, and minor
gate. It reconstructed the reverse-stick law, inverse/simplex theorem,
marginals, nesting, and clock firewall, and found no source repair. The Round-A
action is therefore an artifact freeze and audit-record update only:
`main.tex`, `references.bib`, the verifier, canonical stdout, and current PDF
remain byte-unchanged. Hostile review B and the subsequent independent
owner-repair review found only package-summary omissions; those documentary
omissions are now repaired without changing any theorem or artifact. Current
status is `GO_INTERNAL (OWNER-THIN) / HOLD_EXTERNAL`.
