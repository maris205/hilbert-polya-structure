# Test report

All commands are run from the package root.

```text
python -B code/c348_rwre_producer.py
C348_PRODUCER_PASS beta=400 atoms=280 intervals=780 hits=2930

python -B code/c348_rwre_checker.py
C348 independent RWRE checker: PASS beta=400 atoms=280 intervals=780 hits=2930

python -B code/c348_rwre_sympy_crosscheck.py
C348 SymPy cross-check: PASS 122 symbolic/exact checks

python -B code/c348_rwre_replay.py
C348 byte replay: PASS 2 directories 953582 bytes

python -B code/c348_rwre_mutation.py
C348 hostile mutation suite: PASS 72/72
```

The producer and checker share no imports.  Replay uses two isolated temporary
directories.  The mutation suite includes repaired payload hashes, stale-hash
control, nested extra/omitted/duplicated rows, duplicate/nonfinite/root-invalid
JSON, and duplicate/anchor/alias/merge/non-string-key/timestamp/unknown-field/
type-mutated YAML.  The final release gate additionally checks `-O` and `-OO`
refusal for every executable.  The repaired-hash YAML attacks also lock the
corrected Zeitouni source-owner DOI.
