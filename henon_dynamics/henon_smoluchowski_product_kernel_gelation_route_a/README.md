# HCS-C228 — product-kernel gelation and postgel closure boundary

This package closes the monodisperse multiplicative-kernel concentration law
before gelation, proves the moment blow-up and critical tail, and then verifies
two inequivalent postgel equations instead of conflating them.

## Main progress

- every pregel cluster concentration and both tree generating functions;
- exact \(M_0,M_1,M_2,M_3\), gel time and \(k^{-5/2}\) critical tail;
- explicit Smoluchowski/Stockmayer continuation with sol mass \(1/t\);
- gel-reactive Flory continuation with Lambert-W mass \(q\);
- direct proof that the postgel branches use different loss masses;
- exact, symbolic, replay, mutation, PDF and manifest closure.

Artifacts include `THEOREM_PACKAGE.md`, `SOURCE_AUDIT.md`, the canonical
`results/c228_coagulation_evidence.json`, all checkers under `code/`, the final
`paper/main.pdf`, and the self-excluded `C228_RELEASE_MANIFEST.json`.

Route-A tuple:
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`; overall
`ROUTE_A_REJECTED`; Route B false.  Scope:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
