# C77 test report

Required release gates and their intended outputs are:

```text
producer: PREFREEZE_G3_PASS
independent checker: PASS
Möbius/direct polynomial cross-check: SYMPY_CROSSCHECK_PASS
clean replay: REPLAY_PASS
hostile semantic mutations: MUTATION_TEST_PASS (25/25 rejected)
```

The checker must verify, independently and exactly:

- all six C73/C75/C76 authority bytes and the scope literal;
- the twenty subgroup containment relation;
- all `n_H` values and integer Möbius coefficients;
- all `65536` support closures and direct coefficient vectors;
- normalization `sum_H P_{=H}(q)=1`;
- the top polynomial and its C73 factorization.

The expected top coefficient vector (exponent `q` to coefficient) is

```text
{0:1, 1:-1, 4:-1, 5:1, 7:-1, 8:-1, 9:5, 10:-3}.
```

The clean replay must reproduce the canonical evidence byte-for-byte.  The
hostile audit mutates semantic values rather than only JSON syntax; every
mutation must be rejected.  Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Canonical evidence SHA-256:
`f7e2db84698ec61bf6283175368d2749d7f17ac77baeda37fd0a5cb8caf1c634`.
