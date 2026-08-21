# C81 experiment plan

1. Bind C76/C78/C79/C80 evidence and manifests by raw-byte SHA-256.
2. Reconstruct the five C75 generator permutations and their effective group.
3. Form an invariant repair profile from C79's `(rho,W)`, closure order, and
   C80 threshold histograms by subgroup order.
4. Partition all 65536 masks into effective-group orbits, check profile
   invariance, and record class and stabilizer summaries.
5. Verify the weighted orbit polynomial and Burnside fixed-support identity in
   a separate symbolic script, then replay, mutate, compile twice, inspect,
   and freeze a manifest.

The ambient 11520 lift is recorded for provenance only; all quotient counts use
the effective 1920 label action.
