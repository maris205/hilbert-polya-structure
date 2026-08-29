# Test report

Run from the package root:

\`\`\`text
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_open_toda_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_open_toda_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_open_toda_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_open_toda_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_open_toda_mutation.py
\`\`\`

The producer and checker reconstruct the same receipt.  The checker is
producer-independent and validates all 30 Lax rows, 15 closed-form rows, six
endpoint rows, nine norming rows, and six boundary rows.  SymPy validates 25
generic identities; replay is byte-identical; the hostile suite rejects 22/22
stale-hash, repaired-semantic, unknown-key, provenance, branch, and scope
mutations.  Numerical endpoint discrepancies are not used as theorem evidence.
