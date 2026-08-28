# Paper improvement log

## Round 0 — original

Introduced the ordinary `NC(n)` state space, permutation convention, CSP fixed
formula, Möbius cycle ledger, finite zeta/Koopman spectrum, and explicit scope
firewall.

## Round 1 — mathematical audit

Separated the actual order (L_n) from the abstract CSP order (G_n), which
is essential for the (n=2) kernel.  Added the rank ledger, all-reflection
reversor statement, source ownership table, and the C187 deduplication note.

## Round 2 — release audit

Added coordinate-level checker assertions, independent SymPy cyclotomic
remainders, byte replay, 32 repaired-hash plus one stale-hash mutations, and
the self-excluded manifest closure.  Corrected the Bessis--Reiner record to
Annals of Combinatorics 15(2) (2011), 197--222, DOI
`10.1007/s00026-011-0090-9`; corrected the Kreweras DOI as well.
The final proof audit also split the order-$2n$ argument by parity: odd $n$
uses rank reversal of $K^n$, while even $n$ uses the nontrivial half-turn
$K^n=(K^2)^{n/2}$.
