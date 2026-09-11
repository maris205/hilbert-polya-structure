# P215 A artifact checker second failure

Actual read-only invocation chunk `d6ef09` exited 1 at the asserted unique
absolute FLS count: current P215 A build01 has 67, not the P214-derived 58
mistakenly placed in the checker. The correction changes only that expected
current-artifact count and retains the stronger requirement that every one of
the 67 paths occur in the fresh 227-row runtime manifest. No artifact or prior
failure was changed.
