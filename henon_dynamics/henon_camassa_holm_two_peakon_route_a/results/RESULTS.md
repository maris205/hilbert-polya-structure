# C278 results

The ordered two-peakon manifold reduces exactly to one scalar quadratic.  With
`q=q_2-q_1`, `y=e^q`, `p=p_2-p_1`, total momentum `P`, and energy `E`, set
`D^2=2E-P^2`.  The verified identity is

```text
y_dot^2 = D^2 (y-1) (y-P^2/D^2).
```

- `P^2>D^2`: 15 exact/high-precision rows verify the global cosh branch,
  invariant reconstruction, positive gap, and ODE residuals.
- `D^2>P^2`: 12 rows verify finite collision, signed amplitudes, the
  quadratic gap law, and the `-2/(t_c-t)` amplitude-difference blow-up.
- 15 energy-ledger rows verify the complete `alpha=0,1/4,1/2,3/4,1`
  extension family for three signed chambers.
- Four separate boundary rows retain the single peak, zero momentum, zero
  field, and coincident extended state.

The independent checker reports 551 assertions; the symbolic checker proves
10 identities; replay is byte exact; all 41 repaired-hash semantic mutations
are rejected.  These rows are regression evidence, not a finite proof of the
distributional reduction.
