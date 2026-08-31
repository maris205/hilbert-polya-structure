# Exact control — P134

The paper-local verifier is deterministic, dependency-free, and uses Python
integers only.  It recomputes border arrays both by the linear fallback
algorithm and by literal prefix/suffix comparison, exhausts the finite carrier,
checks every recurrent state, every target fibre, the complete mismatch
automaton, and enlarged sharp witnesses.

Frozen result:

```text
EXHAUSTIVE_RANGE=n=1..9
STATES=409113
TARGET_CELLS=409113
STANDARDIZATION_CASES=3279
LARGE_WITNESS_SIZES=29
ASSERTIONS=1694506
EXACT_ARITHMETIC=python_integers
FLOATING_POINT=none
SAMPLING=none
STATUS=PASS
```

The finite profiles reproduce image sizes
`1,2,4,9,20,47,110,263,630`, recurrent counts `1,2,4,...,16`, the
piecewise sharp depths, and factorial maximum fibres through length nine.
Larger witness trajectories are checked for every `4<=n<=32`.

Replay without creating bytecode and require the original stdout bytes:

```bash
cmp -s code/verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py)
```

Finite computation is falsification evidence only; every all-length statement
is proved in `main.tex`.
