# Reproduction

Use Python 3 with the pinned packages in requirements.txt, LuaLaTeX, TeX Gyre Pagella and Pagella Math, Droid Sans Fallback, and Poppler PDF utilities. Every Python validation entry point refuses optimized `-O` and `-OO` mode.

From the package directory:

```sh
python3 -B code/c383_ab_producer.py
python3 -B code/c383_ab_checker.py
python3 -B code/c383_ab_sympy_crosscheck.py
python3 -B code/c383_ab_replay.py
python3 -B code/c383_ab_mutation.py
python3 -B -m unittest tests/test_c383_smoke.py
python3 -B code/c383_release_manifest.py --build-pdfs
python3 -B code/c383_release_manifest.py --write
python3 -B code/c383_release_manifest.py
```

The producer and explicit build/write switches regenerate artifacts. The last release command only verifies, including fresh temporary PDF rebuilds; it does not rewrite package artifacts. Both isolated producer directories and both PDF builds use fresh temporary directories. Epoch is fixed at 1788566400 and the baseline is 0596f9d680277288225062a6fdd7ad7ce116e01d. The manifest excludes only itself and transient Python caches; its exact membership list rejects unexpected package files.

The independent checker imports no producer code. It binds strict YAML raw and semantic hashes and reconstructs every receipt row. The manuscript and proof are auditable prose, not byte-reproducible generative output; only their frozen bytes and deterministic checks are bound.

Every release mode first executes `c383_ab_checker.py --yaml-only`, which parses without duplicate keys, aliases, merge keys, or implicit datetime conversion, then checks the hard-coded raw evaluation hash and literal false types. Thus even `--write` with no existing manifest rejects YAML changes. The hostile lane exercises that actual entry point in three isolated trees. The actual settled compile logs are stored under the non-ignored `.txt` names `paper/build_round0.txt`, `paper/build_round1.txt`, and `paper/build_round2.txt` and included in the exact manifest ledger.
