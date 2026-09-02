# P165 exact control results

**Status:** `PASS / ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

The paper-local verifier begins with the literal padded-shortening update.  It
does not import the scouting implementation or any repository library.

```text
binary boxes                 n=0,...,7
ternary boxes                n=0,...,4
quaternary boxes             n=0,...,3
quinary boxes                n=0,...,3
binary states at n=7         29,212
assertions                   605,733
status                       PASS
canonical SHA-256            0fc0aac73b62b039fb9e82918a141927b33fb2aecb8b1f28ae3940c1481590bd
verifier SHA-256             391c47dd3be9931c4b525025722ade224bd3b583c75d5da8564f6b75f347bcaf
fresh canonical replays      2/2 byte-identical
```

The `F_4` branch uses an explicit field table for
`F_2[x]/(x^2+x+1)`; it is not arithmetic modulo four.  Checked interfaces
include:

- closure, proper descent, and distance doubling;
- exact pointwise depths and the sharp height in every box;
- every target in every enumerated time image;
- dimension and new-support lower bounds for every source with nonzero
  endpoint;
- the pure dyadic-line structure and exact count of every simultaneous
  extremizer;
- exact-depth zero-target minimizers, kept separate from the complete zero
  fibre;
- `n=0`, `t=0`, full-support targets, exhausted capacity, padded ambient
  coordinates, and strict-versus-weak threshold sentinels;
- visible theorem-statement sentinels in `main.tex`, including the
  `HOLD_EXTERNAL` lifecycle marker.

Finite enumeration supplies counterexample pressure and regression control.
It is neither an all-parameter proof nor an ownership or novelty test.
