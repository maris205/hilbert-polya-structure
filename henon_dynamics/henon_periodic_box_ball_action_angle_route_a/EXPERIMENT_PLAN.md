# Deterministic certificate plan

1. Freeze the KTT/Takagi formulas, the binary/carrier convention, the discrete clock, all `L>=2M`, and the Route-A firewall before computation.
2. Produce every partition of every `0<=M<=L/2` for `2<=L<=14`; enumerate every divisor tuple `alpha_j|gcd(m_j,p_j)` and retain the exact-period sectors with nonzero Möbius count.
3. Compute `F_alpha`, determinant, Smith factors, augmented Smith factors, every relevant `T_l` order, component fixed prefixes, and level/mass/length cycle spectra.  The theorem has no cutoff; this scan is a regression sentinel only.
4. Check independently with rational Gaussian elimination and a separate Smith/minor implementation.  Additionally enumerate all 559 binary states for `L<=9`, run the actual periodic carrier, reconstruct content from conserved energies, and compare all cycle spectra.
5. Cross-check determinants, Smith forms, Möbius inversion, order minimality, primitive-point inversion, and cycle determinants with SymPy.
6. Replay the producer byte for byte, then demand rejection of 64 semantic mutations whose payload hashes are repaired plus one stale-hash mutation.
7. Build three content-distinct paper rounds; compile the final round twice from fresh fixed-epoch directories, compare hashes, inspect logs, fonts, pages, and rendered snapshots.
8. Generate a self-excluded manifest over exactly 27 payload files and verify disk closure.

No target data, external review simulation, or acceptance scoring enters any stage.
