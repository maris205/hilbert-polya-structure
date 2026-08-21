# HCS-C90 joint first-passage coupling

C90 counts the exact joint survival law for every ordered pair of the twenty
C88 target variables.  For thresholds `k,l` it records

```text
J_ij(k,l) = #{pi : T_i(pi)>k and T_j(pi)>l}.
```

The receipt contains all `400 x 17 x 17 = 115,600` integer cells and reduced
probabilities, mixed raw moments through bidegree six, covariance, and the
two marginal recovery checks for every ordered pair.  Joint counts are rebuilt
from nested C88 support bitsets and exact factorial completion weights.

Evidence SHA-256:
`c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978`.

Producer, independent zeta/bitset checker, SymPy cross-check, clean replay,
and 13/13 hostile mutations pass.  Scope firewall:
`NO_BAD_EULER_OR_ROOT_NUMBER`.

No arithmetic/local-data, Euler-factor, root-number, automorphy, full
Burnside/table-of-marks, or Hilbert--Polya operator claim is made.
