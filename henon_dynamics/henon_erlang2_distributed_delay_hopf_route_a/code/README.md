# Reproduction

From this package root, with PYTHONDONTWRITEBYTECODE=1, run:

    python -B code/c343_erlang2_delay_producer.py
    python -B code/c343_erlang2_delay_checker.py
    python -B code/c343_erlang2_delay_sympy_crosscheck.py
    python -B code/c343_erlang2_delay_replay.py
    python -B code/c343_erlang2_delay_mutation.py
    python -B code/c343_release_manifest.py --write
    python -B code/c343_release_manifest.py
    python -B code/c343_release_manifest.py

All six scripts refuse optimized Python (-O or -OO).  The checker is
producer-independent and does not import or name the producer module.  The
replay uses two isolated temporary directories.  The release gate rebuilds
all three PDF rounds twice in fresh directories.
