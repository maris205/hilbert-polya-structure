# Code

`c54_pressure_pole.py` produces the exact HCS-P54 certificate.  It rebuilds
the three reciprocal trace-root ledgers, the physical pressure-pole residue
interval, the scalar-roof cohomology obstruction, and finite Euler
log-derivative identities.

`independent_check.py` does not import the producer.  It independently
recomputes all exact orbit quantities and eight dependency hashes, enforces
the claim firewall, and rejects twelve adversarial mutations.

Run the complete finite audit with:

```bash
bash code/run_c54.sh
```

The executable certificate validates the finite algebra and provenance.  The
all-period meromorphic statement is source-backed and proved separately in
`PROOF_PACKAGE.md`; it is not inferred from finite orbit truncation.
