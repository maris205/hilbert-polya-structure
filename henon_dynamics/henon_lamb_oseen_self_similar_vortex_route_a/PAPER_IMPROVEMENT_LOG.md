# Two-round paper improvement log

The manuscript was reviewed and rebuilt after each substantive revision.  Each archived PDF comes from the same parameterized source with a different `\CRevisionRound`, and each revision changes the mathematical content rather than only typography.

## Round 0 — analytic core

- Artifact: `paper/main_round0_original.pdf`
- SHA-256: `1c127bc83686c042835e589ccbfbbe84609b5ac90e336f973557f03c4a4fedc9`
- Length: 3 pages
- Content: declared-class uniqueness, exact Biot--Savart velocity, complete positive-radius particle formula, all moments and finite \(L^p\) norms, enstrophy, palinstrophy, and their dissipation identity.

Hostile reading found that the core formulas alone left singular endpoints too easy to conflate: \(\tau_0=0\) is a measure trace, \(\nu=0\) is outside the theorem, \(r=0\) must not enter the divided angle formula, and finite enstrophy does not imply finite kinetic energy.

## Round 1 — boundary completion

- Artifact: `paper/main_round1.pdf`
- SHA-256: `8e2ba5c010ae21cf61edffcfa77f69df2f49c0293c3e2a94bc2ae915ffd19de7`
- Length: 3 pages
- Added: an eight-row manuscript boundary atlas (with positive viscosity stated separately), weak zero-age and inviscid limits, the fixed-origin convention, logarithmic angular asymptotics, strict \(L^p\)-decay obstruction, and the exact logarithmic kinetic-energy coefficient.
- Sharpened: recurrence is asserted for fluid states, not inferred incorrectly from a nonautonomous particle angle.

The second hostile reading asked whether a finite grid was being presented as proof, whether nearby C206/C207 models had merely been renamed, and whether closed forms were being promoted into Route-A arithmetic claims.

## Round 2 — evidence and claim closure

- Artifacts: `paper/main_round2.pdf` and byte-identical `paper/main.pdf`
- SHA-256: `5b1a4d4dd9480e55ff970b5ae01dac8435c5c9ac4a62ee3c1f740288cd342b61`
- Length: 4 pages
- Added: the 213-cell evidence design and its explicitly regression-only role; independent symbolic, replay, mutation, parser, and deterministic-build lanes; precise C206/C207 collision boundaries; the honest five-failure Route-A tuple; reproducibility, nonclaim, and AI-use statements.

All three hashes differ.  The final visual audit found no clipping, collision, malformed mathematics, or unreadable table entries across the 10 archived pages.

## Final hostile hardening

The release audit then corrected the Oseen journal title to UTF-8 `för`, made the particle angle explicitly a continuous real-valued lift, and strengthened exact-tree and canonical-rational mutation gates.  All three archived PDFs and every dependent hash were rebuilt after these corrections.
