# Exact audit code

This package executes the source-locked CPU-only audit for
`integral_area_henon_multiplier_support_v1`.  It uses exact SymPy polynomial,
resultant, Groebner, and rational-isolation operations.  No external prime
table, Riemann-zero file, network target, fitted tolerance, or floating
rationality decision is present.

The ordered full run is:

```bash
python code/scripts/run_exact_audit.py
```

The command first validates the immutable source lock, performs an AST
target-isolation scan, audits the proof dependencies, executes all frozen
controls, and checks the parameter and global symplectic identities.  Only
after those gates pass does it execute candidate periods 1--3.  A controls
sanity run that leaves the candidate locked is available as:

```bash
python code/scripts/run_exact_audit.py --controls-only
```

Tests are run from the paper root with:

```bash
PYTHONPATH=code pytest -q --junitxml=results/pytest.xml
```

All-period conclusions come from `notes/PROOF_PACKAGE.md`; finite elimination
is an implementation audit and illustration only.

After the full run, the workflow replaces the pre-created
`results/EXPERIMENT_RESULTS.md` and `results/VALIDATION_REPORT.md` templates,
updates `experiments/EXPERIMENT_TRACKER.md`, runs the complete test suite, and
only then invokes `code/scripts/build_result_manifest.py`.  The manifest
fails closed if any required final artifact is missing and hashes both
executable scripts as provenance inputs.

Each of those three official Markdown artifacts must contain exactly one
machine-authoritative JSON block delimited by
`<!-- HENON_AUDIT_META_V1` and `HENON_AUDIT_META_V1_END -->`.  The parser
rejects missing or duplicate blocks, duplicate/unknown keys, unknown states,
hash disagreement, legacy bold status fields in the body, duplicate tracker
run IDs, and any tracker run set different from `run_summary.json`.  Human
prose outside this block is not searched for status substrings.
