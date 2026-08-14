# HCS-P56 code

`c56_incidence_ladder.py` is the primary exact producer.  It locks seven
upstream artifacts, enumerates primitive H6 cycles through period six,
certifies the all-width incidence ladder through its symbolic insertion
identity, derives the exact period-six orbit, proves the strict four-block
obstruction, and checks a unimodular width-five interpolation minor.

`independent_check.py` reconstructs the cycle census by DFS, rebuilds all
block rows with `Counter`, recomputes the period-six field and the period-five
root isolation, and compares only final invariants with the primary JSON.
It does not import the producer.

Run everything with:

```bash
bash code/run_c56.sh
```

The scripts require Python 3 and SymPy.  They set
`PYTHONDONTWRITEBYTECODE=1` and create only the two declared JSON files under
`results/`.
