# Paper 25 Stage 4.5 Round-2 Phase C internal-consistency audit

Bound draft SHA-256: `39a643c05b4820b782e45a5ec240caa7223ad444229e8a89bdcc98791ce23835`

- Registered experiment claims: **6/6 ALIGNED** against the current draft and persisted provenance.
- Registered Stage-4 empirical claim surfaces: **6/6 exact-once**.
- Tables: **2/2 traced** (four-object map and locked replay).
- Full locked environment suite: **75/75 PASS**; replay inventory: **68/68 files**; two Round-8 isolated replays were byte-identical to the 2,241-row canonical result, without refresh.
- Three geometries each contain 747 rows: 3 period-two matches and 744 disagreements; six exact witness rows remain bound.
- The initial environment-unset test run intentionally failed two lock checks and is retained separately; the locked rerun passed, demonstrating fail-closed environment enforcement rather than a scientific-result change.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

All numerical statements above are claim-to-artifact/replay checks. They do not certify experimental design, statistical adequacy, scientific correctness, or reproducibility by ARS.
