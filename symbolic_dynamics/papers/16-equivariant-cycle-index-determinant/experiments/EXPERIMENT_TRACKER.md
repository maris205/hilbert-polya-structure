# Experiment Tracker

| Run ID | Milestone | Purpose | Variant | Metrics | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| R001 | M0 | `pqr` sanity | squarefree cycles | `(0,0,3)` character | MUST | DONE | exact pass |
| R002 | M0 | trace sanity | `n=2,r=2` | coefficient `2 vs 0` | MUST | DONE | exact pass |
| R003 | M1 | cycle ledger | `n=2..7` | counts, characters, marks | MUST | DONE | all 10,632 cycles across cutoffs; exact pass |
| R004 | M1 | power firewall | `n=2..8,r=1..8` | ghost witnesses, `C2` checks | MUST | DONE | 56 ghost rows; 4008 sign checks pass |
| R005 | M2 | symmetry | distinct/equal weights | stabilizer orders | MUST | DONE | `1` versus `n!` exactly |
| R006 | M2 | rank-one | `n=2..8` | isotypic dimensions/determinants | MUST | DONE | nontrivial eigenvalues `0`, determinants `1` |
| R007 | M2 | diagonal lift | `n=2..8` | rational determinant ratio | MUST | DONE | mismatch in every case |
| R008 | M3 | projective limit | `n=2..8` | zero-specialization | MUST | DONE | 7/7 maps pass |
| R009 | M3 | Schatten cutoff | prime/composite | partial products, class labels | MUST | DONE | 160 rows written |
| R010 | M4 | controls | seeds `16000..16015` | exact identity pass rates | MUST | DONE | 455/455 rows pass; PROVES_TOO_MUCH |
| R011 | M4 | freeze | full bundle | tests and SHA-256 | MUST | DONE | 17/17 tests pass; deterministic manifest frozen |
