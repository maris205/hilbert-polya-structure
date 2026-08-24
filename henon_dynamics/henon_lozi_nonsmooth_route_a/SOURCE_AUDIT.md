# Source audit and boundary — C116

## Frozen source

- Map: `L(x,y)=(1-2|x|+(1/2)y,x)`.
- Parameters: `a=2`, `b=1/2`.
- Branch `0`: `x<0`; branch `1`: `x>0`.
- Border: `x=0` is excluded before enumeration.
- Diagnostic branch weights: `rho_0=1/2`, `rho_1=2/3`.
- Prefix: every binary word of length `1 <= n <= 8`.

The preferred small rational parameters were retained because the exact pilot
is not degenerate: six of the eight length-three words already fail a strict
sign test, while 128 of the 256 length-eight words survive.  No parameter was
changed after seeing a desired determinant or route label.

## Evidence boundary

All affine candidates, orbit coordinates, monodromies, margins, and weights
use exact rational arithmetic.  The cycle-atlas operator is assembled only
from certified primitive rows and is qualified through power eight.  It is
not presented as a geometric Markov partition or a Fredholm operator.

No prime table, zero table, Euler factor, root number, or externally fitted
arithmetic parameter enters the evidence.  Novelty is `UNVERIFIED`; this is a
reproducible Route-A pilot rather than a literature claim.
