# Exact finite height-distribution diagnostic

Executed from `/root/autodl-tmp/hilbert-polya-structure`:

```text
python3 -B henon_dynamics/research_c414_c418/spectral/check_height_valleys.py
```

Actual exit status: 0. Python: 3.12.3. Source SHA256:
`580f072dff6507b7eba42bd00ad0240ae19355d2370685fedc92e21ef28f5bbe`.
The script performs no file writes, uses only the Python standard library,
and prints the exact JSON receipt. It is not a numerical fit or a proof of
the infinite theorem.

The literal path enumerates **all** pairs in the specified polynomial degree
box, computes both height limits by actual polynomial arithmetic until a
strict degree-domination escape condition proves the remaining tail, and
uses exact rational heights. The comparison path enumerates only the
proposed coefficient-free edge/turn degree weights and orbit shifts. It
does not read heights from the literal path. The exhaustive degree box
contains every point below the tested height bound by the proof's inequality
`naive height <= canonical height`; that inequality was also checked on
every tested pair. These are distinct finite calculation paths, not a hash
comparison of one producer's results.

| Prime | Coefficients of f, low to high | a | Height bound | Polynomial pairs | Match |
|---|---|---:|---:|---:|---|
| 2 | (0,0,1) | 1 | 5 | 4,096 | exact |
| 2 | (1,1,1) | 1 | 5 | 4,096 | exact |
| 2 | (0,0,0,1) | 1 | 5 | 4,096 | exact |
| 2 | (1,1,1,1) | 1 | 5 | 4,096 | exact |
| 2 | (1,1,0,0,1) | 1 | 5 | 4,096 | exact |
| 3 | (0,0,1) | 1 | 3 | 6,561 | exact |
| 3 | (2,1,2) | 2 | 3 | 6,561 | exact |
| 3 | (1,0,1,1) | 1 | 3 | 6,561 | exact |
| 3 | (2,2,0,2) | 2 | 3 | 6,561 | exact |
| 5 | (3,2,4) | 3 | 2 | 15,625 | exact |
| 5 | (1,4,3,2) | 4 | 2 | 15,625 | exact |

Total: **11 cases, 77,974 pairs**, all exact distributions agree. The first
quadratic characteristic-two case produced

```text
height:       0, 3/2, 2, 9/4, 5/2, 3, 4, 33/8, 17/4, 9/2, 5
multiplicity: 4,   8, 4,   8,   8,16,16,    8,    8,  80,96
```

The nonprime-field and all-parameter conclusions are supplied by the proof,
not these prime-field tests. The arbitrary thirty-step finite iteration
guard did not fire; the proof, rather than the guard, establishes eventual
escape. No GPU, statistical confidence interval, fabricated seed, formal
Route A control panel, spectral target comparison or global novelty check
is represented by this receipt. The pole factorization and analytic
continuation need a separate reasoning check.
