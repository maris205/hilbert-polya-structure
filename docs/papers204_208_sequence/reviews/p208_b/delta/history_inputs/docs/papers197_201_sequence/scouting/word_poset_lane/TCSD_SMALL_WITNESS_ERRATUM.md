# TCSD small-length witness qualification

2026-09-05 UTC, root manuscript self-check before Round 0. This adds a
qualification to the historical universal witness wording; the earlier
contract and supplements are preserved, not silently overwritten.

The maximum-tail theorem is unchanged. Use the explicit witness
`0^(n-1)1` for every `n>=2`. At `n=2,3`, the assertion that *every*
`a^(n-1)b`, `a!=b`, is sharp is false: `(-1,1)` is recurrent at length
two, and `(-1,-1,1)` is recurrent at length three. At length two the
chosen `(0,1)` enters the alternating two-cycle in one step; at length
three `(0,0,1)` enters the one-zero alternating core in one step.

For larger lengths the earlier zero-run trajectory/noncore discrepancy
argument proves sharpness for every one-exception choice. The all-word
upper bound at the small lengths follows from the run/local certificate
and direct one-exception entry, not from claiming all one-exception words
have positive tail. The new manuscript states the narrower correct
witness claim; the forthcoming paper reviews must verify the boundary.
