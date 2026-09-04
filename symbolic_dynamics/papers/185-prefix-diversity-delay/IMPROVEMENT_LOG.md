# P185 improvement log

## Round 0 → Round 1

Review A replaced labelled-word enumeration by weighted
restricted-growth-word classes.  Its initial control found one Minor issue:
the abstract and “all-time” fibre heading did not delimit the transient
image/CDF/product formulas.  The source now attaches `1<=t<=n-1` to those
formulas, declares the empty product at `t=n-1`, and gives the `t=0` identity
fibres and the `t>=n-1` stabilized fibres.  The accepted Review-A control ends
with 2,104,528 assertions and zero open findings.

## Round 1 → Round 2

Review B used a weighted binary novelty automaton, exhaustive carriers through
`n=18`, and transfer stress through `n=80`.  Its 3,677,711 assertions found no
further issue.  Round 2 is therefore byte-identical to Round 1 with SHA-256
`fcd6257debd3a3e8744571a390296fe02566cc6655957011778400582bea03c3`.
Two source-only cold builds reproduce those bytes.  External status remains
`OWNER_AMBER / HOLD_EXTERNAL`.
