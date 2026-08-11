# HCS-C31 certificate code

`c31_producer.py` exhausts the 1156 admissible state words of length 13,
computes inclusion-preserving R059 coordinate intervals and adapted unstable
slope intervals, and emits two candidate Collatz vectors. Floating point is
used only to find those vectors.

`c31_independent_check.py` does not import the producer. It independently
reconstructs the chronological higher-block graph and every cylinder
interval, encloses square roots with integer `isqrt`, encloses logarithms and
exponentials with rational series plus outward decimal grids, and verifies
the two strict Collatz inequalities using `Fraction` arithmetic.

The legacy period-20 comparison is not hard-coded without provenance.  Both
programs byte-lock and cross-check the frozen period-20 protocol, raw
robustness root ledger, analysis summary, and the earlier independent audit
before accepting the 80-digit recorded value or its containment.

Run the frozen release check from this directory:

```bash
./run_c31.sh
```

An intentional artifact regeneration is:

```bash
./run_c31.sh --refresh-manifest
```

The latter command updates theorem-critical JSON and hashes, so it is reserved
for reviewed code or protocol changes.  The manifest requires all 40 authored
release files, including the theorem documents, Route-A record, paper source,
compiled PDF, code, and result ledgers; deletion of any required path fails
closed even during an intentional refresh.
