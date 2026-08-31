# Exact control — P129 round 1

## Canonical command

```bash
cd papers/129-rootward-active-pile-coalescence
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

Byte comparison:

```bash
cmp -s \
  <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py) \
  code/verification_output.txt
```

Fresh post-repair result: **PASS / byte-identical**.  Review-A repairs changed
the proof and owner boundary, not the literal verifier or its canonical
transcript.

## Exact ranges

- Arithmetic: integer and `fractions.Fraction`; no floating point or
  randomness.
- Rooted Bellman/interface comparison: every rooted subset through `n=14`,
  16,383 states and 98,305 literal transitions.
- Complete hitting distributions and support: every rooted subset through
  `n=11`, 2,047 states.
- Pair recurrence: every `0<=a<=b<=80`, 3,321 states.
- Independent stopped-ballot sum: every adjacent pair through `m=80`.
- Full-start exact laws: `n=1..11`.
- Total assertions: **506,663**.

The upper maximum-time endpoint check is printed as
`PILOT_ONLY ... MANUSCRIPT_CLAIM=NO`. It contributes no theorem or promotion
credit.

## Hashes

```text
fe79e8e3dfa1d15b16d04138d39ef653ac45bbd6addea50d3b53adf34f5aa272  code/verify.py
3e40359274ae4bb033db5efe16d463b28af3fcd7464f9589bc5b136626acd080  code/verification_output.txt
```

Finite control corroborates the proofs; it does not replace the
all-parameter Poissonization, interface, support, or ballot arguments.
