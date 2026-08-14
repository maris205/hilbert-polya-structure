# Code

`c55_galois_blocks.py` constructs the exact symbolic and algebraic certificate.
It enumerates every primitive H6 symbolic cycle through period five, verifies
the one-, two- and three-block incidence relations, derives the new period-four
and period-five trace fields, certifies the physical trace embedding by
Sturm/derivative signs, and rejects 17 claim/interface mutations.

`independent_check.py` reconstructs the graph cycles by DFS and independently
recomputes the exact resultants, Sturm root counts and strict excess inequality.
It does not import the producer.

Run the complete finite audit with:

```bash
bash code/run_c55.sh
```

The code certifies a finite-memory obstruction.  It does not test or refute a
general Hölder observable on all H6 periodic orbits.
