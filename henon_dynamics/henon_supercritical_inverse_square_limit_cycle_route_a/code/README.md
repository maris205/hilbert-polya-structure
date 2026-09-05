# Executable lanes

`c391_producer.py` generates canonical evidence; `c391_checker.py` independently reconstructs exact rows, strict metadata and numerical coefficients. `c391_sympy_crosscheck.py` checks symbolic and Green/Stone identities. `c391_replay.py` tests two working directories. `c391_mutation.py` exercises repaired-hash, serialization and YAML attacks. `c391_release_manifest.py` owns deterministic PDFs and closed manifests. All six reject Python -O and -OO before assertions.

The checker does not import the producer. Numeric strings are parsed with a finite-decimal grammar, and exact metadata comparisons preserve the distinction between bool and int. YAML is raw-hash-locked even in release-write mode, with duplicate/anchor/alias/merge rejection before use.
