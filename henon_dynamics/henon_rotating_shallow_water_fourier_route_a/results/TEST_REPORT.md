# Test report

Expected commands from the package root:

    python3 code/c217_swe_producer.py
    python3 code/c217_swe_checker.py
    python3 code/c217_swe_sympy_crosscheck.py
    python3 code/c217_swe_replay.py
    python3 code/c217_swe_mutation.py

The checker uses an independent NumPy/SciPy matrix path and exact integer
divisor counts.  Scope flags are all false, Route B is denied, and the
negative-f, zero-c, zero-f, and fully-zero faces are tested.
