# Source and scope audit

## What is source-native

* The polynomial candidate \(x^3-3x+1/7\) and its Hénon lift are stated
  explicitly.
* The three intervals are the actual monotonicity intervals of the cubic.
* The branch Jacobian template has determinant one, matching the
  area-preserving Hénon form.
* All word, matrix, trace, and determinant values in the evidence are exact
  integer calculations reproduced independently by a second implementation
  and by SymPy.

## What is not yet source-native

* No invariant compact set or complete Markov partition has been proved.
* The full shift \(\Sigma_3\) is a deliberately frozen pilot model, not a
  theorem about the real Hénon map.
* The points \(-2,0,3\) are representative derivative samples. Their
  matrices are not asserted to be monodromies of periodic Hénon orbits.
* The 6 by 6 transfer matrix is a finite matrix-valued screening device, not a
  function-space transfer operator.

## Controls and exclusions

The evidence uses a canonical JSON serialization, exact integer arithmetic,
an independent checker, a SymPy characteristic-polynomial/Newton check, a
byte-level replay, and nine semantic mutations. The paper and code use no
prime lookup, local factors, root numbers, automorphy input, fitted roots,
or external arithmetic data. The scope firewall is
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproducibility boundary

The evidence is deterministic for Python 3 and the listed frozen constants.
Changing the representative points, branch convention, maximum length, or
matrix convention creates a new experiment and invalidates the manifest; it
is not a harmless post-processing choice.
