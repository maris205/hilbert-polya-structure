# C246 results

The receipt covers 27 rational ((beta,a,rho)) tuples, embedded square
moments through order 8, 12-term q-product prefixes with three spot values,
generator moment coefficients, four boundary faces, and six-step exact reward
skeletons.  The pre-jump recurrence contains the required factor
(2a/rho): (Y_{n+1}^2=beta^2Y_n^2+2aE_{n+1}/rho).

The independent checker passes 75 assertions, SymPy passes 96 identities, byte
replay is identical, and the hostile suite rejects 36/36 mutations.  For
(beta>0) all occupation language is stationary Markov-renewal/Palm; only
(beta=0) is called a reset/regeneration face.  Route-A is
`ROUTE_A_REJECTED`; Route B is disabled.
