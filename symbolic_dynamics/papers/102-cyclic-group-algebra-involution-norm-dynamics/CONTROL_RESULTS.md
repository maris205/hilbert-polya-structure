# Exact control results — P102

Command:

```text
python3 code/verify_involution_norm.py
```

Result on 2026-08-29 UTC:

```text
cyclic group-algebra involution norm verification: PASS
literal_lanes=9
rigidity_lanes=85
assertions=116278
```

The 116,278 registered assertions cover:

- seven prime-field full phase spaces:
  `(q,n)=(3,1),(3,2),(5,2),(5,4),(7,3),(11,2),(13,3)`;
- two explicitly constructed extension fields,
  `F_4=F_2[t]/(t^2+t+1)` and
  `F_16=F_2[t]/(t^4+t+1)`, both at `n=3`;
- coefficient-level cyclic convolution and reversal for every state, compared
  with independently calculated Fourier reversal and norm products;
- the algebraic and Fourier iterate formulas through time five for every
  enumerated state;
- complete literal functional graphs, recurrent membership, recurrent-core
  cardinality, and the maximum distance to the recurrent set;
- fixed counts through time 12, Möbius integrality, exact cycle dictionaries,
  cycle support, and recurrent-state accounting; and
- 85 recovery lanes: every divisor `n|(q-1)` over
  `q in {2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,49}`.

## Frozen diagnostic signals

| `(q,n)` | first fixed counts | recurrent size | max depth | cycle inventory |
|---|---|---:|---:|---|
| `(7,3)` | `4,16,4,16,4,16,4,16` | 16 | 2 | `{1:4, 2:6}` |
| `(11,2)` | `4,4,4,36,4,4,4,36` | 36 | 1 | `{1:4, 4:8}` |
| `(5,4)` | `8,8,8,8,8,8,8,8` | 8 | 3 | `{1:8}` |
| `(4,3)` | `4,16,4,16,4,16,4,16` | 16 | 1 | `{1:4, 2:6}` |
| `(16,3)` | `4,16,4,256,4,16,4,256` | 256 | 1 | `{1:4, 2:6, 4:60}` |

All calculations are deterministic and exact.  There is no random seed,
floating-point tolerance, numerical eigensolver, or computer-algebra black
box.  The complete stdout is stored in
`code/verification_output.txt`; rerunning the command must reproduce it byte
for byte.
