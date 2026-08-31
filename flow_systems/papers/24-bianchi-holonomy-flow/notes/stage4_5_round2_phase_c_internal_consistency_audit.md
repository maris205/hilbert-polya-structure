# Paper 24 Stage 4.5 Round-2 Phase C internal-consistency audit

Bound draft SHA-256: `79735d058d965a35de10cc0b3655e0b1db5217bde00e02d2d48b7564cd841afc`

- Registered experiment claims: **11/11 ALIGNED** against the current draft and persisted provenance.
- Registered Stage-4′ empirical claim surfaces: **10/10 exact-once** in the bound revision.
- Tables: **3/3 traced** (pooled collision, loxodromic derivative profile, and control panel).
- Full current unit suite: **81/81 PASS**; Stage-4 derivative replay: **10/10 PASS**, two isolated derivative builds byte-identical, canonical results not refreshed.
- Pooled rows: 11,481; loxodromic derivative rows: 10,976; 144 scalar descriptors; 508 joint descriptors; 364/10,832 scalar-collision rows separated; 10,468 joint collision rows remain.
- Four executed control families / five subpanels provide 6,396 exact control rows but still cover only two of three prespecified canonical control types.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

All numerical statements above are claim-to-artifact/replay checks. They do not certify experimental design, statistical adequacy, scientific correctness, or reproducibility by ARS.
