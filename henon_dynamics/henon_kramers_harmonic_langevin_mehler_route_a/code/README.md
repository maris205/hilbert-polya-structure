# C237 code ledger

`c237_kramers_producer.py` generates the canonical evidence JSON from exact
rational controls and 90-digit `mpmath` arithmetic.  It contains no target
arithmetic data and writes only the requested output path.

`c237_kramers_checker.py` is producer-independent: it repeats the formulas,
checks schema closure and every regression cell, and reports its assertion
count.  `c237_kramers_sympy_crosscheck.py` checks 26 generic symbolic
identities.  `c237_kramers_replay.py` compares canonical bytes from a clean
process.  `c237_kramers_mutation.py` applies 32 hostile semantic/provenance
mutations (including all five boundary rows) and requires every one to be
rejected.

`c237_release_manifest.py` is the final gate.  It reruns all checks, verifies
the fixed-epoch three-round PDFs, font embedding, phrase coverage and exact
27-file payload closure; the manifest itself is self-excluded.

Run from this directory with `PYTHONDONTWRITEBYTECODE=1 python3 -B`.
