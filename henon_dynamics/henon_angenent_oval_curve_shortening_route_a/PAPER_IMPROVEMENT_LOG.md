# Paper improvement log

## Round 0 — original

Established the implicit solution, strict convexity, exact curvature, and
normal-speed identity with all signs frozen.

## Round 1 — substantive theorem expansion

Added the exact width, height, area and elliptic-modulus length; introduced
the punctured-strip arrival-time foliation and proved its level-set PDE;
added both round-extinction and translated Grim-Reaper limits.

## Round 2 — audit and boundary revision

Added independent evidence/accounting, collision separation and Route-A
evaluation.  Tightened the foliation statement from “open strip” to “open
strip minus the origin,” with the origin explicitly designated as the
zero-time extinction leaf.  Corrected every theorem contract to select the
central connected component; the unrestricted periodic level set is now
explicitly identified as its disjoint union of `2*pi`-translates.  Separated
source ownership from package closure.

The final source audit directly checked Angenent's 1992 source and records
it as the explicit oval-formula owner: the paper states the curvature-
pressure solution, its two Grim-Reaper ends, and its round extinction.  The
package does not rely on the paper's higher-dimensional torus theorem.
