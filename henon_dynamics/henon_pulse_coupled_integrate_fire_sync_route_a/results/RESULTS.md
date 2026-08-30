# C245 results

The exact ledger has (3\times3\times7\times7=441) event rows, 63 all-equal
synchrony rows, and 441 partition-coarsening rows.  Every row stores rational
pre/post states, common threshold scale, firing indices, avalanche generations,
cluster partitions, event-word labels, and any detected return period.

The producer-independent checker passes 4,438 assertions; SymPy passes 330
symbolic/rational identities; byte replay is identical; and the hostile suite
rejects 41/41 mutations.  The synchronized rows all return in one event with
primitive word `[N]`.  These are finite event certificates, not a complete
continuous-state synchrony census.  Route-A is `ROUTE_A_REJECTED`; Route B is
disabled.
