# Independent validation report

## Material Passport

- Origin Skill: `ars-codex academic-research-suite / experiment-agent`
- Origin Mode: `validate`
- Origin Date: `2026-08-09T11:20:00Z`
- Verification Status: `VERIFIED`
- Version Label: `validation_v1`

The independent checker does not import the producer.  It rebuilds the graph
from the seven hyperelliptic word states, uses the Möbius--trace formula as an
independent completeness oracle, and reconstructs all 146 released
eventually-positive labeled cycles from directed edge tokens.

Verified exact outputs:

- seven states and fourteen transported-form edges;
- 828 primitive labeled free cycles through length 12;
- eventual-positive counts `1,6,14,36,89` at lengths 8--12;
- 146 total eventually-positive labeled cycles;
- 21 distribution-character singular cycles, split `6,6,9` at lengths
  10--12;
- chronological matrices, reciprocal polynomials, symplectic checks,
  repetition determinants, and rational Perron intervals for every released
  row;
- central first-return decomposition without loss of elementary chronology.

The machine-readable outcome is `c24_independent_check.json`; every registered
check is true.  The test suite additionally rejects transposed edge matrices,
right-multiplied chronology, move-word-only identities, proper powers,
phase-dependent positivity selection, and silent finite weighting on the
singular character locus.
