# C370 executable lanes

Run from the package root with ordinary, non-optimized Python:

```bash
python code/c370_brieskorn_reeb_producer.py
python code/c370_brieskorn_reeb_checker.py
python code/c370_brieskorn_reeb_sympy_crosscheck.py
python code/c370_brieskorn_reeb_replay.py
python code/c370_brieskorn_reeb_mutation.py
python code/c370_release_manifest.py
```

The producer constructs the canonical JSON receipt. The checker imports no
producer module and recomputes all 5,469,178 fixed-time classifications. The
SymPy lane checks the Reeb normalization, tangent identities, return
determinant, period arithmetic, and index identity independently. Replay runs
the producer in two isolated directories. Mutation tests repair all declared
hashes before asking the checker to reject semantic changes. The release gate
also rebuilds and audits every PDF in fresh directories.

PyYAML and SymPy are the only non-standard Python dependencies. The PDF lane
uses LuaLaTeX, `pdfinfo`, `pdffonts`, `pdftotext`, and `pdftoppm`.
