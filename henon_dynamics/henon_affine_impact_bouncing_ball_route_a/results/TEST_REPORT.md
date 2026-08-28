# Test report

Commands run from the package root:

    python3 code/c212_bouncing_producer.py          PASS (12 controls / 96 cells)
    python3 code/c212_bouncing_checker.py           PASS (368 assertions)
    python3 code/c212_bouncing_sympy_crosscheck.py  PASS (11 identities)
    python3 code/c212_bouncing_replay.py            PASS (byte replay)
    python3 code/c212_bouncing_mutation.py          PASS (14/14 rejected)

The checker uses exact Fraction arithmetic and no producer imports. It verifies
both the regular positive-flight section and the separately named closed affine
section, including the strict Zeno and r=0 sticking edge conditions. Scope flags
are all false and Route B is denied.
