# Implementation Notes — SD-C26

## Source/evaluator firewall

`code/sdc26_kraft_fredholm.py` contains only target-blind encoders, cyclic
word normalization, positive roof allocations, weighted-cycle identities,
trie construction, symbolic determinant logic, and necklace arithmetic.
Prime, square, Fibonacci, random, hash, composite, and modular predicates
occur only in `code/sdc26_evaluator.py` after the candidate is frozen.

The static AST audit rejects calls named `factorint`, `isprime`, `mangoldt`,
`primepi`, `primerange`, `zeta`, `zetazero`, or `riemannr` in the candidate
core.

## Visible code convention

Each payload is closed with one edge visibly labeled `#`. Hence every
audited orbit word has exactly one marker and belongs to the fixed local
alphabet `{0,1,#}`. Even raw binary payloads, which are not prefix-free,
become pairwise distinct as cyclic visible words. Elias prefix statistics
are retained as implementation controls but are not assumed by the theorem.

## Positive roof convention

Every disjoint block uses exact rational shares summing to one and therefore
total roof `log(atom)`. The singular values of a weighted cyclic permutation
are its edge weights. Floats merely render

`max singular >= atom^(-sigma/ell)`

and

`block S1 >= ell * atom^(-sigma/ell)`.

The inequalities and infinite noncompactness statement are proved
analytically; finite rows are regression witnesses only.

## Shared-trie representative

Every bit edge receives roof `log(2)/8`; a terminal return receives the
positive remainder. Removing the root leaves a finite DAG, so the exact
symbolic determinant is obtained directly and compared with the first-return
formula `1-F`. Primitive necklaces are counted by Möbius inversion.

## Reproducibility

JSON keys are sorted, CSV fields and row order are fixed, every text artifact
uses UTF-8/LF, timestamps and runtime metadata are forbidden, and SHA-ranked
controls are deterministic. The final runner performs two complete
generator, pytest, and analysis passes before integrity and ledger freezing.
Provenance remains `PENDING_FIRST_ARTIFACT_COMMIT` until the external
two-stage Git freeze.

