# C85 theorem package

Let `H_0,...,H_19` be the C75 actual-subgroup order.  For retained support
`A subset L`, put `D=L\A` and use C80's containment-repair coordinates

```text
v(A) = (tau_H0(D), ..., tau_H19(D)).
```

## Theorem: threshold-vector subgroup-poset rigidity

For all `65536` supports:

1. `v(A)` depends only on `Phi(A)`, and exactly twenty distinct vectors occur.
2. The zero set is the principal ideal
   `I_0(v(A))={i:tau_Hi(D)=0}={i:H_i <= Phi(A)}`.
3. Consequently the twenty vector classes are in bijection with the twenty
   actual subgroups.
4. Writing `w_H` for the vector class attached to closure `H`,
   `H_0 <= H_1` if and only if `w_H0 >= w_H1` coordinatewise.

The exact closure/vector fibre spectrum is

```text
{32:6, 64:4, 96:4, 192:2, 1760:2, 30400:2}.
```

## Proof and certificate split

The identity `tau_H(D)=0 iff H <= Phi(A)` follows directly from the C80
definition: no restored label is needed exactly when the retained closure
already contains the target.  Hence the zero coordinates form the principal
ideal below `Phi(A)`, and that ideal recovers its unique maximum.

The finite certificate checks constancy on every closure fibre and finds one
distinct vector for each of the twenty positive C76 fibres.  It also checks
the forward coordinatewise inequality on all `400` ordered subgroup pairs.
For the converse, `w_H0 >= w_H1` implies
`I_0(w_H0) subseteq I_0(w_H1)`, hence `H_0 <= H_1` by principal-ideal
recovery.  Thus the map is an order-reversing embedding, not merely a count
coincidence.

The producer reads the frozen C80 matrix.  The independent checker does not
reuse its dynamic-programming thresholds: it reconstructs the group closure,
enumerates the inclusion-minimal support antichain for every target, and uses
`tau_H(D)=min_M |M\A|`.  A SymPy check verifies the exact zeta inverse and all
finite-lattice meet/join pairs.

This theorem does not construct or claim a full Burnside ring, a full table of
marks, arithmetic/local data, Euler factors, root numbers, automorphy, or a
Hilbert--Polya operator.
