# Results

The deterministic Stage-1 run produced:

| Artifact | Meaning |
|---|---|
| `orbit_ledger_manifest.json` | local analysis-freeze hashes, source lock, cutoff, orientation and completeness boundaries |
| `modular_orbit_ledger.csv` | 8,798 primitive oriented cyclic conjugacy classes through 16 S-R blocks; inversion retained |
| `orbit_growth.csv` | oriented and inversion-quotiented counts by block length |
| `arithmetic_audit_summary.json` | theorem-derived no-collision result plus post-freeze prime-proxy controls |
| `modular_repetition_ledger.csv` | repetitions 1--5 and independently evaluated Selberg/Ruelle amplitudes |
| `near_prime_proxy_scan.csv` | declared scan of \(q=t^2-2\) for integer traces \(3\le t\le5000\) |

The ledger is complete for its cyclic-word/block convention, not below a
geometric-length cutoff. Every reported equal-trace multiplicity is only a
within-cutoff lower bound. The checksum is a local reproducibility safeguard,
not an immutable third-party preregistration. Rational primes appear only in
the separately declared audit; Riemann-zero data never appear.
