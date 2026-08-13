# Reproduction

Run:

```bash
bash experiments/reproduce.sh
```

The script first executes the standard-library `unittest` suite, then
regenerates every CSV and the JSON hash manifest in `results/` at degree cutoff
12.  It is deterministic and requires only Python 3.

