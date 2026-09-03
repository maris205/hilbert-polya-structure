# Code and release commands

Run from the package root:

    python -B code/c351_jackson_producer.py
    python -B code/c351_jackson_checker.py
    python -B code/c351_jackson_sympy_crosscheck.py
    python -B code/c351_jackson_replay.py
    python -B code/c351_jackson_mutation.py
    python -B code/c351_release_manifest.py --write
    python -B code/c351_release_manifest.py
    python -B code/c351_release_manifest.py

The producer alone writes canonical evidence. The checker does not import the
producer and uses an independent exact traffic solver. Replay writes only to
two isolated temporary directories. The mutation lane checks repaired-hash
semantic attacks as well as duplicate/nonfinite JSON and strict YAML. The
release script regenerates every lane in temporary locations, checks -O and
-OO refusal, rebuilds all three manuscript rounds twice from fresh
directories, and closes the exact 27-payload ledger.
