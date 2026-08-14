# Experiments

Run `bash reproduce.sh` from this directory. Frozen settings are
`max_blocks=16`, `repeat_max=5`, and `trace_scan_max=5000`. The first phase
writes a SHA-256 manifest; the second refuses to run if the orbit ledger has
changed. No Riemann-zero data are used.
