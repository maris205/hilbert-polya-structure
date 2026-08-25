# C166 test report

The deterministic producer passes and writes the released evidence.  The
producer-independent checker passes 53,348 assertions while reconstructing
25,200 clock cases, 27,788 direct state periods, and 90 closed-form reversor
matrices.  The separate SymPy path passes 7,519 exact checks.  Canonical replay
reproduces the evidence byte for byte.  The hostile suite rejects 35
repaired-hash semantic mutations and one stale-hash mutation.

PDF determinism, embedded fonts, warning scans, rendered-page inspection, and
manifest closure are recorded in `paper/COMPILE_REPORT.md`.
