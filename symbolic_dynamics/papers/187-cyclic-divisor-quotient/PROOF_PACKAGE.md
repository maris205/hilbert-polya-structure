# Proof package — P187

## Normalized assumptions

- `N>=1`, `m>=1`, cyclic indices.
- States are positive divisor words.
- `nu_p(x)` lies in `0..a_p` when `p^a_p || N`.

## Deductive chain

1. `nu_p(x_i/gcd(x_i,x_{i+1}))=(e_i-e_{i+1})_+`.
2. A height-`h` output can only arise from the local pair `(h,0)`; its two
   output neighbors are zero, so it freezes and separates lower-height
   intervals.
3. Induction on `h` gives `D^h` fixed. The word `(0,...,0,h,1)` has tail
   exactly `h` for `m>=3`; direct formulas settle `m=1,2`.
4. Fixedness is equivalent to cyclic nonadjacency of every prime support.
   Positive heights contribute weight `a_p` per occupied site.
5. For a target exponent `b_i`, the matrix entry
   `L_b(u,v)=1[(u-v)_+=b]` enforces exactly one local constraint. Closing the
   path is a trace; distinct primes multiply.
6. `sum_b L_b=J` gives total fibre mass.
7. Cayley--Hamilton gives the fixed-factor recurrence; cyclic monotonicity
   gives the exact all-one fibre and the common-prime image obstruction.
8. At `m=2`, the two positive-part differences cannot both be positive;
   counting their common offset yields the explicit boundary fibre.

## Failure modes explicitly excluded

- Treating `C_1` or `C_2` with an unstated simple-graph convention.
- Claiming height `max a_p` at lengths one or two.
- Forgetting that recurrence is fixedness only after stabilization is proved.
- Presenting the transfer-matrix method itself as new.
