# Implementation notes — SD-C37

## Physical source/evaluator firewall

`code/source_core.py` and `code/generate_artifacts.py` own neutral affine
states, generators, words, quotients, exact operator witnesses, and diagonal
fixtures. They contain no prime classifier, accepted-support predicate,
target-zero table, or evaluator import.

`code/independent_evaluator.py` imports neither source module. It independently
reconstructs transitions, authority heights, Kahn DAGs, admissible and
primitive words, quotient maps, elementary-symmetric/Newton determinant
coefficients, operator supports, and generic controls. Its prime sieve runs
only after `source_manifest.json` hashes every neutral source artifact.

## Authority bridge corrections

The prototype's auxiliary `b+k` height was a valid strict-height proof device,
but the authority source lock freezes `b+r^k`. The authority source and
evaluator separately implement the latter. The prototype's rational edge
weights were diagnostic; authority uses the unweighted `A_+=S+T`. The Route
tuple follows strict v0.2 enums and therefore records A3/A4 as `FAIL`.

## Exact arithmetic and evidence boundary

- integers decide graph, word, quotient, and support gates;
- `Fraction` decides every weight, trace, determinant, reciprocal series, and
  bosonic coefficient;
- no floating-point comparison decides a gate;
- word enumeration is exhaustive only through the frozen length and bases;
- quotient enumeration is exhaustive only for the frozen moduli;
- boundedness, noncompactness, full infinite outdegree, and infinite diagonal
  identities remain theorem-owned rather than inferred from finite windows.

## Canonical execution and provenance

The runner builds fresh A and B plus cache-free cold C in three initially
empty `/tmp` directories. A is published only after all 23 hashes agree.
Metadata then adds the report, registries, strict Route card, research lock,
and bridge record while proving the scientific bytes unchanged.

The three provenance fields remain
`PENDING_FIRST_ARTIFACT_COMMIT`. A future root-owned metadata-only stage may
replace all three with one lowercase 40-hex artifact commit. Mixed, partial,
or self-referential provenance is forbidden; downstream hashes are not
embedded back into `SOURCE_LOCK.md`.
