# C87 test report

## Computational gates

```text
producer: PREFREEZE_G3_PASS
independent block-criterion checker: C87_INDEPENDENT_CHECK_PASS
SymPy multilinear/finite cross-check: C87_SYMPY_FINITE_CROSSCHECK_PASS
clean byte replay: C87_REPLAY_PASS
hostile semantic mutations: C87_MUTATION_TEST_PASS (27/27 rejected)
```

The independent checker reconstructs all 65536 truth values from C78 rather
than calling the producer predicate.  It verifies all first-order rows, all
120 pair rows, 7/27 faithful orbits, ten numerical classes, C73 baseline
agreement, exact normalizations, and the efficiency/endpoint identities.
It also verifies the C82 distance-one boundary identity
`40704+445696=16*30400` against the hash-bound C82 receipt.

The SymPy kernel expands a 475-term multilinear polynomial of degree ten,
checks it against all 65536 Boolean inputs, then derives all 16 first and 120
second coalition-size enumerators by symbolic discrete differentiation.

## Integrity and AI-failure-mode gates

Stage 2.5 and final Stage 4.5 audits both return `PASS` with zero integrity
issues.  The seven-mode checklist is:

| mode | status | evidence |
|---|---|---|
| implementation bug | CLEAR | independent structural checker plus symbolic kernel |
| hallucinated citation | CLEAR | no external citations; all local authorities are raw-hash bound |
| hallucinated result | CLEAR | every number replays from canonical code and evidence |
| shortcut reliance | CLEAR | exhaustive finite domain, no learned/statistical shortcut |
| bug reframed as insight | CLEAR | no surprise-based claim; every theorem is tied to exact identities |
| methodology fabrication | CLEAR | methods, commands, source roles, and outputs agree byte-for-byte |
| frame-lock | CLEAR | C87 explicitly audits novelty against C73 and adds only size/pair/orbit data |

All claims in the manuscript are present in the canonical evidence or follow
from the displayed definitions by exact algebra.  Scope-conformance check:
`NO_BAD_EULER_OR_ROOT_NUMBER` throughout.
