# C312 results

The exact ledger contains 801 systems and 1,843 retained trajectory states,
with 28,895 audited leaves.  On this grid the largest observed stopping time
is six and 209 cases change their arithmetic mean.  Every case stops far
inside the analytic `4n^3+2n+2` guarantee.

The producer-independent checker performs 28,870 checks.  SymPy closes 38
exact identities, replay is byte-identical, and all 26 repaired-hash/parser
attacks are rejected.  The exhaustive grid tests the implementation; the
two-step progress lemma proves the theorem for arbitrary real initial data.
