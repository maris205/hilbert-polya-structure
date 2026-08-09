# Exact code

`c24_producer.py` rebuilds the literal labeled Rauzy class, transports the
state-dependent intersection form, enumerates primitive labeled directed free cycles,
and emits the eventual-positive and metaplectic-character singular ledgers.

`c24_independent_check.py` does not import the producer.  It starts from the
seven-word hyperelliptic automaton, verifies completeness with the
Möbius--trace formula, and reconstructs all released matrices and rational
Perron intervals.

Run the full release with:

```bash
./code/run_c24.sh
```

The mutation tests reject matrix transposition, reversed chronology,
move-word-only cycle keys, proper powers, phase-dependent positivity filters,
and silent finite assignment on the distribution-character singular locus.
