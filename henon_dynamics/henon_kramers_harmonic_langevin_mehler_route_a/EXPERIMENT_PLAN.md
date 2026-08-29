# Experiment and verification plan — HCS-C237

1. Freeze the SDE, parameter domain, physical clock, source commit and scope
   literal.
2. Generate exact rational controls spanning all damping regimes, zero
   damping, positive-time transitions, correlations, Kalman rank, Gibbs
   moments, and the two boundary faces.
3. Serialize 40 regression rows with 90-digit working arithmetic and 64
   significant digits; hash the payload after removing its hash field.
4. Recompute all rows in a producer-independent checker; reject unknown keys
   and all provenance/scope/theorem drift.
5. Reconstruct generic matrix, Lyapunov, Gaussian, Kalman, rate and Hamiltonian
   identities in SymPy; replay producer bytes in a clean process.
6. Run 32 hostile mutations, including repaired-hash semantic mutations for
   all five boundary rows, then compile two substantive paper revisions
   under fixed epoch `1787875200` with two LuaLaTeX passes each.
7. Require deterministic round PDFs, embedded subset fonts, no layout/reference
   warnings, and manifest closure before release.

There is no simulation or fitted target data: all tests are exact identities
and finite rational controls.
