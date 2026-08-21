# HCS-C85 threshold-vector subgroup-poset rigidity

C85 compresses C80's complete `20 x 65536` threshold atlas without losing the
actual subgroup poset.  For retained support `A`, the twenty-coordinate vector
`v(A)` is constant precisely on the closure fibre of `Phi(A)`.  Exactly twenty
vectors occur, one for each actual subgroup of
`Q = Z/9 + Z/3 + Z/2`.

The zero coordinates satisfy

```text
{i : v(A)_i = 0} = {i : H_i <= Phi(A)},
```

so they recover the principal ideal and its unique maximum `Phi(A)`.  For the
twenty closure vectors `w_H`, the complete order law is

```text
H0 <= H1  iff  w_H0 >= w_H1 coordinatewise.
```

The exact vector/closure fibre spectrum is
`{32:6,64:4,96:4,192:2,1760:2,30400:2}`.  It accounts for all `65536`
supports.  The recovered poset has `40` cover relations and `102` comparable
ordered pairs when reflexive pairs are included.

The canonical evidence SHA-256 is
`22bdaf9fa2fe08532b45eae51cf7704a1509764b5a09f10eebb98012224be152`.
The producer, independent antichain checker, SymPy/finite-lattice check, clean
replay, and `23/23` hostile-mutation rejection all pass.

C75's ambient lifted group order `11520` and C76's effective label-action
order `1920` remain distinct.  This is a finite named-support theorem only:
no arithmetic/local, Euler-factor, root-number, automorphy, full
Burnside/table-of-marks, or Hilbert--Polya claim is made.  Scope firewall:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
