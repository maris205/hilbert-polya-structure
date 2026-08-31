# Exact control — P132

The paper-local verifier is deterministic, dependency-free, and uses Python
integers only.  It exhausts every binary word and every target through length
16, for 131,070 source states and 131,070 target cells.  It also checks ten
sharp witnesses through length 511.

Frozen result:

```text
ASSERTIONS=524452
EXACT_ARITHMETIC=python_integers
FLOATING_POINT=none
SAMPLING=none
STATUS=PASS
```

Finite computation does not prove any all-length statement.  Its purpose is to
attack boundary conventions, off-by-one clocks, empty fibres, and strictness of
the extremal claim independently of the written derivation.
