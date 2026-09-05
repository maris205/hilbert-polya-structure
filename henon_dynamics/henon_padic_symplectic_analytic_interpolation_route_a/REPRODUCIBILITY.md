# Reproducibility

Python 3.12.3, SymPy 1.14.0 and PyYAML 6.0.2 were used. LuaLaTeX and Poppler supply PDF compilation, text, fonts and raster checks. Run from this package directory:

```bash
python -B code/c394_interpolation_producer.py
python -B code/c394_interpolation_checker.py
python -B code/c394_interpolation_sympy_crosscheck.py
python -B code/c394_interpolation_replay.py
python -B code/c394_interpolation_mutation.py
python -B -m unittest tests/test_c394_smoke.py
python -B code/c394_release_manifest.py --build-pdfs
python -B code/c394_release_manifest.py --write
python -B code/c394_release_manifest.py
```

The last command is a full nonwrite reconstruction, including fresh finite lanes and two fresh builds of every revision. The two-directory replay uses two independent working directories and the same frozen producer source; it is not a claim of two independently implemented producers or two copied source trees. The checker imports no producer. Its expected reconstruction is cached only within a process for repeated hostile checks; it is reconstructed from code and fixed inputs, not read from the submitted payload.

Six executable scripts each refuse both `-O` and `-OO`, giving twelve refusal checks. Exact integer types are compared recursively, including bool/int distinctions. YAML parsing rejects duplicates, anchors, aliases, explicit tags, merge keys, nonstring keys, implicit dates, unknown fields and semantic changes; raw bytes and semantic digest are both frozen. The release calls this gate before any write. Ten attacks exercise that actual write path in a minimal temporary copied package and assert that all copied files remain unchanged.

The manifest excludes itself and lists every other physical file. Compiler logs are retained unchanged after the settled second pass. No network is needed to reproduce the package. Finite exact checks support implementation integrity; universal claims depend on the proof.

The release explicitly refuses any symlink anywhere in the package before all build/write branches. An extra temporary actual-write attack verifies that this early refusal leaves the copied manifest and every copied file unchanged. Physical membership includes unlisted cache files rather than silently ignoring them.
