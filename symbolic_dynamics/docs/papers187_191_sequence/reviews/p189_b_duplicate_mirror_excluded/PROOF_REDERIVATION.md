# P189 Review-B Proof Re-derivation

## Scope

This note is a standalone expansion of the mathematical portions of
`REVIEW.md`.  It attacks the bound Round-1 claims in
`papers/189-transpose-row-compression/main.tex:63-265` without changing the
Review-B conclusion:

- verdict: `PASS`
- exact assertions: `1493195`
- exhaustive state boxes: `n=1,2,3,4`
- partition and mass controls: `n<=10`
- transfer controls for `W_n`: `n<=12`

The verifier implementation remains `verify_review_b.py`, with the frozen
transcript in `CANONICAL.txt`.

## Independent representation

Review B does not use the author's packed-integer representation and does not
reuse Review A's row-support `frozenset` representation.  Its state carrier is

```text
Matrix = tuple[column-bit-tuples]
```

with the literal update reconstructed as:

1. read the displayed row-sum vector `r(A)` from the column bits;
2. replace source row `j` by an initial column of height `r_j(A)`;
3. encode the result again as labelled columns.

Recurrence and depth are recovered by memoized orbit repeat detection on the
literal successor map, not by indegree peeling.

## Re-derivation chain

### 1. Literal map

At `main.tex:63-77`, the paper defines

```text
F(A)_{ij} = 1{i <= r_j(A)}.
```

The column-bit verifier checks this identity on every state in the complete
carriers `n=1..4`.  The decoded first image always equals `D(r(A))`.

### 2. Height calculus

At `main.tex:90-120`, the paper defines `D(h)` and threshold conjugation
`h^*`.  Review B re-derives:

- `r(D(h)) = h^*` by counting, for each row level `i`, the columns whose
  heights reach that level.
- `(h^*)^* = h^downarrow` by explicit Ferrers-cell reflection rather than by
  any author routine.

The verifier checks both identities on all states in the exhaustive boxes.

### 3. Four-iterate collapse

From `main.tex:122-153`, the claimed normal form is

- `F(A) = D(r)`
- `F^2(A) = D(r^*)`
- `F^3(A) = D(r^downarrow)`
- `F^4(A) = F^2(A)`

Review B checks all four epochs directly for every matrix in the complete
`n=1..4` carriers and also verifies the alternating odd/even post-collapse
phase.  The reviewer witness `00/01` at `n=2` confirms both false
strengthenings fail:

- `F^2 != F`
- `F^3 != F`

### 4. Recurrent set, fixed points, and strict two-cycles

At `main.tex:166-208`, the paper identifies the recurrent set with Ferrers
states and gives counts

- recurrent states: `C(2n,n)`
- fixed states: `2^n`
- strict two-cycles: `(C(2n,n) - 2^n) / 2`

Review B does not assume those formulas.  It computes literal orbits, marks a
state recurrent exactly when the orbit reaches depth `0`, and checks:

- recurrent states are exactly the matrices whose column heights are initial
  segments in weakly decreasing order;
- every recurrent state satisfies `F^2(A)=A`;
- every nonfixed recurrent state lies in a strict two-cycle;
- the exact counts match the formulas in the exhaustive boxes and in direct
  partition controls through `n=10`.

### 5. Exact depth layers

At `main.tex:177-190`, the paper claims

- `L_0 = {D(lambda)}`
- `L_1 = {A : r_1(A) >= ... >= r_n(A)} \\ L_0`
- `L_2 = {A : r_i(A) < r_{i+1}(A) for some i < n}`

with population formulas using

```text
W_n = sum_{lambda in P_n} prod_i C(n, lambda_i)
    = [z^n] prod_{k=0}^n (1 - C(n,k) z)^(-1).
```

Review B checks depth by literal orbit distance and confirms exact agreement
with the displayed predicate on every state.  It separately verifies the two
forms of `W_n`:

- direct decreasing-partition sum through `n=10`;
- generating-function coefficient control through `n=12`.

Sharp boundary witnesses are checked independently:

- only `A_{1n}=1` has depth `1` for the stated witness family;
- only `A_{21}=1` has depth `2` for the stated witness family;
- at `n=1`, both states are fixed and the depth vector is `(2,0,0)`.

### 6. Every-target fibre formulas

At `main.tex:225-265`, the paper gives:

- time-one fibre formula for any initial-segment target `D(h)`;
- zero time-one fibre for targets with a column hole;
- time-two fibre formula for Ferrers targets `D(mu)` using
  `lambda = mu^*`;
- zero time-two fibre for non-Ferrers targets.

Review B recomputes actual one-step and two-step indegrees for every target in
every exhaustive box and checks exact equality with the formulas.

Two explicit boundary attacks are recorded:

- hole target witness `00/01` at `n=2`: time-one fibre is zero;
- non-Ferrers initial-segment witness `01/00` at `n=2`: time-one fibre is
  positive while time-two fibre is zero.

Both fibre families also sum to `2^(n^2)` after targetwise equality is
established.

### 7. Control table and assertion surface

At `main.tex:269-299`, the manuscript reports the complete-box table and the
author verifier scale.  Review B confirms the table values independently:

| n | states | \|im F\| | \|im F^2\| | fixed | strict 2-cycles | \|L_1\| | \|L_2\| |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 2 | 0 | 0 | 0 |
| 2 | 16 | 9 | 6 | 4 | 1 | 5 | 5 |
| 3 | 512 | 64 | 20 | 8 | 6 | 164 | 328 |
| 4 | 65536 | 625 | 70 | 16 | 27 | 10051 | 55415 |

Review B's own exact assertion count is `1493195`, recorded in
`CANONICAL.txt` and reproduced in `REPLAY_LOG.md`.

## Conclusion

No mathematical defect was found in the bound claims at `main.tex:63-265`.
The independent re-derivation supports the unchanged Review-B outcome:

- verdict: `PASS`
- findings: `critical=0`, `major=0`, `minor=0`
- external status: `OWNER_AMBER/HOLD_EXTERNAL`

This note is evidence for the exact bound object only.  It is not a novelty,
priority, ownership-clearance, or external-release determination.
