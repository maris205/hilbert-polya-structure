# Repository update handoff

## Prepared addition

Add the complete directory henon_instability_roof_zeta/ as one new research
project. It is self-contained except for two hash-locked proof premises and a
read-only period-12 validation bridge under docs/related_programs/.

The addition contains:

- a frozen source protocol and run tracker;
- independent orbit and finite-section code;
- complete raw results through period 20;
- adversarial and neighboring-parameter controls;
- an independent 38-check verifier and seven unit tests;
- a strict Route-A YAML evaluation;
- a compiled research note and reproducible figure;
- deterministic generated metadata and strict RFC 8259 JSON;
- a SHA-256 file manifest.

## Suggested registry entry

Hénon instability-roof zeta — proves a positive non-lattice instability clock
on the certified \(H_6\) survivor, audits degree-in-period cycle-section zeros
through period 20, and records an A3 analytic obstruction. Status:
ROUTE_A_EXPLORATORY.

## Source-control status

The current workspace root is not a Git worktree. No commit, branch, pull,
push, or clean/dirty assertion can therefore be made here. Run the following
only after placing this directory inside the intended Git checkout:

    git add henon_instability_roof_zeta
    git status --short

Review results/manifest.json before committing. The manifest records that Git
metadata was unavailable and binds the delivery to file hashes instead.
