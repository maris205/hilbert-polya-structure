# Canonical replay log

**Runtime environment:** Python standard library; `PYTHONDONTWRITEBYTECODE=1`  
**Replay date:** 2026-09-03 UTC  
**External status:** `HOLD_EXTERNAL`

## Command

```bash
PYTHONDONTWRITEBYTECODE=1 \
python3 docs/papers172_176_sequence/scouting/stochastic_matrix/verify_breadth.py \
> /tmp/p172_stochastic_matrix.json
```

## Two fresh process runs

```text
run E wall time: 19.594 s
run F wall time: 19.515 s
run E SHA-256: fa39710708dadbeb2614b64da5ef87f158081e03a782c08164eb230ac174db8c
run F SHA-256: fa39710708dadbeb2614b64da5ef87f158081e03a782c08164eb230ac174db8c
cmp exit: 0
canonical bytes: 52,821
```

The canonical payload reports:

```text
candidate_count = 23
assertions      = 129,620
schema          = p172-p176-stochastic-matrix-breadth-v1
external_status = HOLD_EXTERNAL
```

Candidate-specific assertions sum to 129,617; three additional assertions
check handle count, uniqueness, and nonempty audits.  Per handle:

```text
M01  4,158    M02  6,592    M03  3,294    M04      6
M05    595    M06      4    S01    702    S02    273
S03    340    S04    367    S05    146    S06     54
A01 10,673    H01 20,955    G01  1,374    G05    887
G02    317    G03  3,018    G04  2,752    R01 66,459
R02      3    C01  6,645    C02      3
```

Subtracting the five historical literal sentinels
`M01,H01,R01,C01,C02` leaves 18 fresh systems and 31,397 exact
candidate-specific assertions.

## Interpretation boundary

Byte identity establishes deterministic replay of the bounded computation.
It does not prove the uniform theorems, source ownership, novelty, priority,
or freedom to release.  The theorem packages give the all-parameter proof
routes separately.
