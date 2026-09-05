# Reproducibility

From this package directory, run:

```bash
python -B code/c379_multibaker_producer.py
python -B code/c379_multibaker_checker.py
python -B code/c379_multibaker_sympy_crosscheck.py
python -B code/c379_multibaker_replay.py
python -B code/c379_multibaker_mutation.py
python -B -m unittest tests/test_c379_smoke.py
python -B code/c379_release_manifest.py
```

The last command is a nonwrite release reconstruction. A maintainer creating
the initial artifacts may use `--build-pdfs`, then `--write`; neither option
changes the frozen theorem or authority. Every executable refuses optimized
Python. Exact JSON rejects duplicate keys and nonfinite values. Evaluation
YAML rejects duplicate/non-string keys, aliases, anchors, merges, implicit
dates, unknown fields and semantic type substitutions.

PDFs use LuaLaTeX, fixed epoch 1788566400 and two fresh builds per round,
each with two passes. Final logs are retained as source artifacts. Font,
text and raster audits are performed independently of the TeX exit status.
The manifest excludes itself and hashes the exact complete physical payload.
