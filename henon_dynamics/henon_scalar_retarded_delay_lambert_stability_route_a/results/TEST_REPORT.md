# C210 test report

The exact producer and producer-independent checker agree on all 12 cases,
13 times and 156 symbolic cells.  SymPy checks the characteristic substitution,
multiple-root derivative, delayed Laplace term, zero-delay $(a+b)$ branch,
Hopf modulus and evidence cells.  Replay is byte-identical.  Mutation tests
cover source/evaluator/scope locks, theorem corruption, route escalation,
duplicated times, formula rows, summary counts, unknown top/nested keys and
stale hashes.
