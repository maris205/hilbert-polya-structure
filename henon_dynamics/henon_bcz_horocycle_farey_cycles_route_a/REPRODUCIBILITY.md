# Reproducibility

Run commands from this package directory using the pinned requirements.
All six entrypoints reject -O and -OO. No external model, target dataset,
network service or GPU participates in deterministic evidence production.

```bash
python -B code/c395_bcz_producer.py
python -B code/c395_bcz_checker.py
python -B code/c395_bcz_sympy_crosscheck.py
python -B code/c395_bcz_replay.py
python -B code/c395_bcz_mutation.py
python -B -m unittest discover -s tests
python -B code/c395_release_manifest.py --build-pdfs
python -B code/c395_release_manifest.py --write
python -B code/c395_release_manifest.py
```

PDF builds use LuaLaTeX, two passes per fresh directory, two unrelated
build directories per round, SOURCE_DATE_EPOCH=1788566400 and fixed optional
metadata. The final main.pdf is byte-identical to round two. Settled TeX logs
are retained verbatim in paper/compile_round[012].txt. The self-excluding
manifest enumerates every physical payload and its SHA, with exact membership.
Both write and nonwrite modes run strict YAML validation, all lanes, fresh
PDF rebuild comparison and font/text/raster checks. The actual-write hostile
lane reaches the preflight gate and verifies no manifest change.

Hashes certify bytes and replay contracts, not correctness or model-output
reproducibility. Ninety-digit quadrature is explicitly not interval arithmetic.
