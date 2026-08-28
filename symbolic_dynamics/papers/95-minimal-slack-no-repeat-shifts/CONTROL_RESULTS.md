# Exact control results — P95

Command:

```text
python3 code/verify_no_repeat.py
```

Result on 2026-08-28 UTC:

```text
minimal-slack no-repeat exact control: PASS
assertions=5031
literal_cyclic_words=99058
q=3 F_1..F_3=[0, 6, 6]
q=3 u_0..u_10=1,0,1/2,1/4,3/8,5/16,11/32,21/64,43/128,85/256,171/512
q=4 F_1..F_5=[0, 0, 24, 24, 0]
q=4 u_0..u_10=1,0,0,1/2,1/4,1/8,5/16,9/32,13/64,33/128,69/256
q=5 F_1..F_7=[0, 0, 0, 120, 120, 0, 0]
q=5 u_0..u_10=1,0,0,0,1/2,1/4,1/8,1/16,9/32,17/64,25/128
q=6 F_1..F_9=[0, 0, 0, 0, 720, 720, 0, 0, 0]
q=6 u_0..u_10=1,0,0,0,0,1/2,1/4,1/8,1/16,1/32,17/64
```

The 5,031 registered assertions include state counts, exact right-action
orientation, the transposition identity, positive-word inverse identities,
in/out degrees, closure, two directed reachability tests, sparse adjacency
traces, literal cyclic-word counts, state-by-state first-hit distributions,
full return probabilities, and a full admissible-grid two-gap renewal
factorization (including zero-probability pairs).
The literal route examined 99,058 cyclic words and shares no adjacency-trace
implementation with the first route.

All arithmetic in the probability checks uses `fractions.Fraction`; no
floating-point comparison enters an evidence-bearing assertion.
