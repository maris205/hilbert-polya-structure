# Evidence and validation plan

The experiment is a deterministic theorem audit, not a numerical discovery
claim.

## Finite receipts

- Enumerate 18 rational parameter cases in dimensions 1–6.
- Independently convolve one-dimensional square counts to obtain
  \(r_d(n)\) for the first 12 shells.
- Record exact rational eigenvalues and energy coefficients, integer Morse
  indices/kernels, fastest ties, and 72-digit trace terms at \(t=1/3\).
- Test six actual-support projections and all three \(\kappa=0\) chambers.
- Record the analytic exhaustion cutoff derived from \(\alpha/\kappa\);
  never treat the 12-shell receipt window as the fastest-shell proof.

## Independent gates

1. Producer writes canonical JSON with a self-excluding SHA-256 payload hash.
2. Checker imports no producer and reconstructs exact JSON/YAML trees, types,
   IDs, shell counts, rational/decimal syntax, and all 1653 audited leaves.
3. SymPy verifies Fourier, energy, tie, analytic-exhaustion, semigroup, and
   singular-face identities.
4. Replay runs two isolated producers and demands byte identity.
5. Hostile suite changes semantics while repairing the payload hash and also
   attacks duplicate/nonfinite JSON and duplicate/anchor/alias/merge YAML.
6. Release gate builds each of the three round variants twice in fresh
   directories at the fixed epoch, checks the final PDF as a byte-identical
   Round-2 alias, and audits warnings, page count, fonts, text sentinels, and
   the exact 27-file payload ledger.

Any discrepancy fails the release rather than being averaged away.
