# P206 — actual author replay evidence

2026-09-05 UTC. Python 3.12.3, standard library only, -B, deterministic
integer arithmetic, no network/randomness/local research imports or input
data. The paper-local verify.py is byte-identical to the original standalone
CRC3 author checker; this is author evidence, not a new independent review.

The earlier paper-local pair is preserved in author_replay/run1.stdout
and run2.stdout. Root additionally executed the following complete fresh
pair while closing Round0; each producer and comparison exited zero:

```sh
python -B papers/206-ternary-cyclic-record-feedback/verify.py > papers/206-ternary-cyclic-record-feedback/qa_round0/attempt2/author_run1.stdout
cmp papers/206-ternary-cyclic-record-feedback/CANONICAL.json papers/206-ternary-cyclic-record-feedback/qa_round0/attempt2/author_run1.stdout
python -B papers/206-ternary-cyclic-record-feedback/verify.py > papers/206-ternary-cyclic-record-feedback/qa_round0/attempt2/author_run2.stdout
cmp papers/206-ternary-cyclic-record-feedback/CANONICAL.json papers/206-ternary-cyclic-record-feedback/qa_round0/attempt2/author_run2.stdout
```

Working directory `/root/autodl-tmp/symbolic_dynamics`; all four commands
were success-chained, combined exit zero. Root then compared each earlier
paper-local stdout with its corresponding fresh stdout, again raw-byte
cmp exits zero. The freeze retains the original pair, not overwritten logs;
the additionally executed pair remains at the paths above.

Each complete run records 655,256 assertions on 88,572 ternary states,
all targets through n=10, complete source sets through n=7, and the
independent integer-part DP through n=40. These are finite proof-pressure
boxes, not an all-length proof or any manuscript-review acceptance.

- Verifier SHA256: `8665dfa7342247a8dac651476b3c7ab9c134873fbc6e366f7bfae3a61eadc354`.
- Canonical and all four stdout files: `1b035b1fc2036e2e1b237c3aeaeb5cefa9af3a830f2f76cf0b43cf75ac8fb9be`.

The complete raw output includes every finite box, assertion census,
maximum/equality count and deterministic record digest. No shortened
summary was compared in place of the whole output.
